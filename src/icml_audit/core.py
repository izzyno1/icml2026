from __future__ import annotations
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import re
import sqlite3
import time
import uuid


class Blocked(RuntimeError):
    pass


SOURCE_ROLES = frozenset({'original_submission', 'camera_ready', 'revised', 'preprint',
                          'prior_work', 'official_catalog',
                          'current_attachment_unverified_role', 'synthetic'})


def validate_source_role(role):
    if role not in SOURCE_ROLES:
        raise ValueError('Declare a valid version role')


def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode('utf-8')


def digest(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()


def file_hash(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def safe_id(value):
    if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,100}', value):
        raise ValueError('Unsafe identifier')
    return value


def confined(root, relative):
    root = Path(root).resolve(strict=True)
    relative = Path(relative)
    if relative.is_absolute() or '..' in relative.parts:
        raise Blocked('Path must be project-relative')
    current = root
    for part in relative.parts:
        current /= part
        if current.exists() and (current.is_symlink() or getattr(current.lstat(), 'st_file_attributes', 0) & 0x400):
            raise Blocked('Reparse/symlink path rejected')
    resolved = current.resolve()
    if not resolved.is_relative_to(root):
        raise Blocked('Path escapes project')
    return resolved


def atomic_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    with temp.open('xb') as f:
        f.write(canonical(obj) + b'\n')
        f.flush()
        os.fsync(f.fileno())
    os.replace(temp, path)


def versions(root):
    root = Path(root)
    required = ['AGENTS.md', 'PROJECT_SPEC.md', 'configs/project_policy.json', 'configs/rubric.json']
    rules = {name: file_hash(root / name) for name in required}
    sources = sorted((root / 'src/icml_audit').glob('*.py'))
    if not sources:
        raise Blocked('Implementation version unavailable')
    sources += [root / 'tools/workflow.py', root / 'tools/openreview_session.py',
                root / 'Login-OpenReview-and-Fetch.cmd',
                root / 'reference/v2/icml2026_genealogy_v2/audit_helpers.py']
    if any(not p.is_file() for p in sources):
        raise Blocked('Entrypoint or reused implementation version unavailable')
    code_files = {p.relative_to(root).as_posix(): file_hash(p) for p in sources}
    return {'rules_hash': digest(rules), 'rule_files': rules,
            'code_hash': digest(code_files), 'code_files': code_files}


class WriterLock:
    """OS-held lock released by process death; the persistent file is harmless."""
    def __init__(self, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.file = path.open('a+b')
        if path.stat().st_size == 0:
            self.file.write(b'0')
            self.file.flush()
        self.file.seek(0)
        try:
            if os.name == 'nt':
                import msvcrt
                msvcrt.locking(self.file.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            self.file.close()
            raise Blocked('Another coordinator holds the writer lock') from exc

    def close(self):
        if not self.file.closed:
            self.file.close()


SCHEMA = '''
CREATE TABLE IF NOT EXISTS tasks(
 id TEXT PRIMARY KEY,paper TEXT NOT NULL,stage TEXT NOT NULL,kind TEXT NOT NULL,
 inputs TEXT NOT NULL,input_hash TEXT NOT NULL,rules_hash TEXT NOT NULL,code_hash TEXT NOT NULL,
 prompt_hash TEXT NOT NULL,model TEXT NOT NULL,status TEXT NOT NULL,current_attempt TEXT,reason TEXT);
CREATE TABLE IF NOT EXISTS attempts(
 id TEXT PRIMARY KEY,task TEXT NOT NULL REFERENCES tasks(id),number INTEGER NOT NULL,
 token TEXT NOT NULL,expires REAL NOT NULL,status TEXT NOT NULL,result_hash TEXT,
 UNIQUE(task,number));
CREATE TABLE IF NOT EXISTS sources(
 id TEXT PRIMARY KEY,paper TEXT NOT NULL,role TEXT NOT NULL,url TEXT NOT NULL,final_url TEXT NOT NULL,
 retrieved TEXT NOT NULL,sha256 TEXT,bytes INTEGER,path TEXT,read_scope TEXT NOT NULL,
 status TEXT NOT NULL,family TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS current_sources(family TEXT PRIMARY KEY,source TEXT NOT NULL REFERENCES sources(id));
CREATE TABLE IF NOT EXISTS dependencies(task TEXT REFERENCES tasks(id),source TEXT REFERENCES sources(id),PRIMARY KEY(task,source));
CREATE TABLE IF NOT EXISTS results(task TEXT PRIMARY KEY REFERENCES tasks(id),attempt TEXT NOT NULL,
 sha256 TEXT NOT NULL,payload TEXT NOT NULL,accepted TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS events(seq INTEGER PRIMARY KEY AUTOINCREMENT,event TEXT NOT NULL,payload TEXT NOT NULL,at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS reservations(id TEXT PRIMARY KEY,maximum INTEGER NOT NULL,written INTEGER NOT NULL,status TEXT NOT NULL,path TEXT NOT NULL);
'''


class Ledger:
    def __init__(self, root):
        self.root = Path(root).resolve(strict=True)
        self.lock = WriterLock(confined(self.root, 'state/writer.lock'))
        try:
            self.db = sqlite3.connect(confined(self.root, 'state/ledger.sqlite3'), isolation_level=None)
            self.db.row_factory = sqlite3.Row
            self.db.execute('PRAGMA foreign_keys=ON')
            self.db.execute('PRAGMA journal_mode=WAL')
            self.db.execute('PRAGMA synchronous=FULL')
            self.db.executescript(SCHEMA)
        except Exception:
            self.lock.close()
            raise

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def close(self):
        self.db.close()
        self.lock.close()

    @contextmanager
    def tx(self):
        self.db.execute('BEGIN IMMEDIATE')
        try:
            yield
            self.db.execute('COMMIT')
        except BaseException:
            self.db.execute('ROLLBACK')
            raise

    def event(self, name, payload):
        self.db.execute('INSERT INTO events(event,payload,at) VALUES(?,?,?)',
                        (name, canonical(payload).decode('utf-8'), datetime.now(timezone.utc).isoformat()))

    def source(self, paper, role, url, path=None, final_url=None, read_scope='not_read', retrieved_at=None):
        safe_id(paper)
        validate_source_role(role)
        # A reference may later be promoted to a target; enforce the same ten-target
        # boundary at that transition without changing historical task identities.
        if role != 'prior_work' and self.prior_only(paper) and self.db.execute(
                "SELECT 1 FROM tasks WHERE paper=? AND kind='real'", (paper,)).fetchone():
            if len(self.p2_target_papers() | {paper}) > 10:
                raise Blocked('P2 boundary: at most ten real papers')
        if not url.startswith('https://'):
            raise ValueError('Source URL must be HTTPS')
        p = confined(self.root, path) if path else None
        sha = file_hash(p) if p else None
        family = digest([paper, role, url])
        sid = digest([family, sha])
        with self.tx():
            old = self.db.execute('SELECT source FROM current_sources WHERE family=?', (family,)).fetchone()
            self.db.execute('INSERT OR IGNORE INTO sources VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',
                            (sid, paper, role, url, final_url or url, retrieved_at or datetime.now(timezone.utc).isoformat(),
                             sha, p.stat().st_size if p else None, str(p.relative_to(self.root)) if p else None,
                             read_scope, 'available' if p else 'metadata_only', family))
            self.db.execute('INSERT OR REPLACE INTO current_sources VALUES(?,?)', (family, sid))
            if old and old['source'] != sid:
                self.db.execute("UPDATE tasks SET status='stale',reason='source_version_changed' WHERE id IN (SELECT task FROM dependencies WHERE source=?)", (old['source'],))
            self.event('source_registered', {'source': sid, 'family': family})
        return sid

    def prior_only(self, paper):
        """Explicit reference-only identities; unknown/mixed identities stay targets.

        A prior URL can be registered before acquisition (metadata_only). This is
        a purpose declaration, never evidence that bytes exist or were read.
        """
        roles = {r[0] for r in self.db.execute('SELECT DISTINCT role FROM sources WHERE paper=?', (paper,))}
        return roles == {'prior_work'}

    def p2_target_papers(self):
        return {r[0] for r in self.db.execute("SELECT DISTINCT paper FROM tasks WHERE kind='real'")
                if not self.prior_only(r[0])}

    def enqueue(self, task, paper, stage, inputs, sources=(), kind='real', prompt='manual_evidence_review', model='not_invoked'):
        safe_id(task); safe_id(paper); safe_id(stage)
        if kind not in {'real', 'synthetic', 'catalog'}:
            raise ValueError('Invalid task kind')
        v = versions(self.root)
        packet = {'inputs': inputs, 'sources': sorted(set(sources))}
        ih = digest(packet)
        with self.tx():
            old = self.db.execute('SELECT * FROM tasks WHERE id=?', (task,)).fetchone()
            if old:
                if old['input_hash'] != ih or old['stage'] != stage or old['paper'] != paper or old['rules_hash'] != v['rules_hash'] or old['code_hash'] != v['code_hash'] or old['prompt_hash'] != digest(prompt) or old['model'] != model or old['kind'] != kind:
                    raise Blocked('Task identity/version conflict; use a new explicit task id')
                return task
            targets = self.p2_target_papers()
            if kind == 'real' and not self.prior_only(paper) and len(targets | {paper}) > 10:
                raise Blocked('P2 boundary: at most ten real papers')
            self.db.execute('INSERT INTO tasks VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',
                (task, paper, stage, kind, canonical(packet).decode('utf-8'), ih, v['rules_hash'], v['code_hash'], digest(prompt), model, 'pending', None, None))
            for source in packet['sources']:
                self.db.execute('INSERT INTO dependencies VALUES(?,?)', (task, source))
            self.event('task_enqueued', {'task': task})
        return task

    def check_context(self, task):
        current = versions(self.root)
        if task['rules_hash'] != current['rules_hash'] or task['code_hash'] != current['code_hash']:
            raise Blocked('Rule/code hash conflict')
        if digest(json.loads(task['inputs'])) != task['input_hash']:
            raise Blocked('Input manifest hash conflict')
        for source in self.db.execute('SELECT s.* FROM dependencies d JOIN sources s ON d.source=s.id WHERE d.task=?', (task['id'],)):
            cur = self.db.execute('SELECT source FROM current_sources WHERE family=?', (source['family'],)).fetchone()
            if not cur or cur['source'] != source['id']:
                raise Blocked('Source version is stale')
            if source['path'] and file_hash(confined(self.root, source['path'])) != source['sha256']:
                raise Blocked('Source byte hash conflict')

    def claim(self, task, lease_seconds=300):
        if not 0 < lease_seconds <= 3600:
            raise ValueError('Lease must be bounded')
        with self.tx():
            row = self.db.execute('SELECT * FROM tasks WHERE id=?', (task,)).fetchone()
            if not row or row['status'] != 'pending':
                raise Blocked('Task is not pending')
            self.check_context(row)
            number = self.db.execute('SELECT COUNT(*) FROM attempts WHERE task=?', (task,)).fetchone()[0] + 1
            if number > 3:
                raise Blocked('Attempt limit reached')
            aid, token = uuid.uuid4().hex, uuid.uuid4().hex
            self.db.execute('INSERT INTO attempts VALUES(?,?,?,?,?,?,?)', (aid, task, number, token, time.time()+lease_seconds, 'running', None))
            self.db.execute("UPDATE tasks SET status='running',current_attempt=?,reason=NULL WHERE id=?", (aid, task))
            self.event('attempt_claimed', {'task': task, 'attempt': aid})
        packet = {key: row[key] for key in ('id','paper','stage','kind','input_hash','rules_hash','code_hash','prompt_hash','model')}
        packet.update(attempt_id=aid, lease_token=token, inputs=json.loads(row['inputs']),
                      evidence=[dict(s) for s in self.db.execute('SELECT s.* FROM dependencies d JOIN sources s ON d.source=s.id WHERE d.task=?', (task,))],
                      rule_files=versions(self.root)['rule_files'],
                      budget={'max_attempts':3,'worker_concurrency':1,'max_result_bytes':1000000},
                      output=str(Path('runs') / task / aid / 'result.json'),
                      unread='All evidence is unread unless a submitted locator explicitly records otherwise',
                      acceptance='Schema and hashes only; human/semantic verification remain separate')
        atomic_json(confined(self.root, Path('runs') / task / aid / 'packet.json'), packet)
        return packet

    def heartbeat(self, attempt, token):
        with self.tx():
            row = self.db.execute('SELECT a.*,t.current_attempt FROM attempts a JOIN tasks t ON a.task=t.id WHERE a.id=?', (attempt,)).fetchone()
            if not row or row['current_attempt'] != attempt or row['token'] != token or row['status'] != 'running' or row['expires'] < time.time():
                raise Blocked('Expired or superseded attempt')
            self.db.execute('UPDATE attempts SET expires=? WHERE id=?', (time.time()+300, attempt))

    def write_result(self, packet, findings):
        """Worker-local durable output. Does not accept or change shared task state."""
        task, aid = safe_id(packet['id']), safe_id(packet['attempt_id'])
        relative = Path('runs') / task / aid
        payload = {'context': packet, 'findings': findings}
        result = confined(self.root, relative / 'result.json')
        if len(canonical(payload)) > 1_000_000:
            raise Blocked('Result exceeds bounded task output limit')
        if result.exists():
            raise Blocked('Attempt output already exists')
        atomic_json(result, payload)
        receipt = {'result_sha256': file_hash(result), 'task': task, 'attempt': aid}
        atomic_json(confined(self.root, relative / 'receipt.json'), receipt)
        return receipt

    def accept(self, attempt):
        row = self.db.execute('SELECT * FROM attempts WHERE id=?', (attempt,)).fetchone()
        if not row:
            raise Blocked('Unknown attempt')
        task = self.db.execute('SELECT * FROM tasks WHERE id=?', (row['task'],)).fetchone()
        if task['current_attempt'] != attempt:
            raise Blocked('Superseded attempt')
        if task['status'] not in {'running','accepted'}:
            raise Blocked('Task is blocked or stale')
        base = Path('runs') / task['id'] / attempt
        path = confined(self.root, base / 'result.json')
        receipt_path = confined(self.root, base / 'receipt.json')
        if path.stat().st_size > 1_000_000 or receipt_path.stat().st_size > 4096:
            raise Blocked('Oversized result or receipt')
        receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
        sha = file_hash(path)
        if receipt != {'result_sha256': sha, 'task': task['id'], 'attempt': attempt}:
            raise Blocked('Result receipt/hash conflict')
        self.check_context(task)
        value = json.loads(path.read_text(encoding='utf-8'))
        ctx = value['context']
        for key in ('id','paper','stage','kind','input_hash','rules_hash','code_hash','prompt_hash','model'):
            if ctx.get(key) != task[key]:
                raise Blocked('Result context conflict')
        if ctx.get('attempt_id') != attempt or ctx.get('lease_token') != row['token'] or digest(ctx.get('inputs')) != task['input_hash']:
            raise Blocked('Attempt/input conflict')
        # An already accepted identical result is idempotent even after its lease expires.
        if task['status'] == 'accepted':
            accepted = self.db.execute('SELECT * FROM results WHERE task=?', (task['id'],)).fetchone()
            if not accepted or accepted['sha256'] != sha:
                raise Blocked('Accepted result cannot be overwritten')
            return False
        if row['expires'] < time.time():
            raise Blocked('Lease expired; result requires a new explicit attempt')
        findings = value['findings']
        if not isinstance(findings, dict) or not isinstance(findings.get('claims'), list):
            raise Blocked('Invalid findings schema')
        known = {r[0] for r in self.db.execute('SELECT source FROM dependencies WHERE task=?', (task['id'],))}
        for claim in findings['claims']:
            if claim.get('kind') not in {'author_claim','direct_evidence','inference','unknown'} or not claim.get('text'):
                raise Blocked('Claim kind/text missing')
            for evidence in claim.get('evidence', []):
                if evidence.get('source_id') not in known or not evidence.get('locator') or not evidence.get('read_range'):
                    raise Blocked('Evidence must bind known source, locator, and read range')
                src = self.db.execute('SELECT status FROM sources WHERE id=?', (evidence['source_id'],)).fetchone()
                if src['status'] != 'available':
                    raise Blocked('Metadata-only source cannot support a read evidence claim')
            if claim['kind'] == 'direct_evidence' and not claim.get('evidence'):
                raise Blocked('Direct evidence needs source locators')
        prior_ids = set(findings.get('prior_sources', []))
        if not prior_ids <= known:
            raise Blocked('Unknown prior source')
        read_ids = {e['source_id'] for c in findings['claims'] for e in c.get('evidence', [])}
        priors_read = bool(prior_ids) and prior_ids <= read_ids and all(
            self.db.execute('SELECT role FROM sources WHERE id=?', (s,)).fetchone()['role'] == 'prior_work' for s in prior_ids)
        normal = dict(findings)
        normal['novelty_label'] = findings.get('novelty_label', 'U') if priors_read else 'U'
        if normal['novelty_label'] not in {'U','L0','L1','L2','L3'}:
            raise Blocked('Unknown novelty label')
        if normal['novelty_label'] == 'L0' and not findings.get('prior_coverage_documented'):
            normal['novelty_label'] = 'U'
        normal.update(assessment='model_screening_unvalidated', population_role='nonprobability_pilot', human_adjudicated=False)
        with self.tx():
            self.db.execute('INSERT OR REPLACE INTO results VALUES(?,?,?,?,?)',
                (task['id'], attempt, sha, canonical(normal).decode('utf-8'), datetime.now(timezone.utc).isoformat()))
            self.db.execute("UPDATE tasks SET status='accepted',reason=NULL WHERE id=?", (task['id'],))
            self.db.execute("UPDATE attempts SET status='accepted',result_hash=? WHERE id=?", (sha, attempt))
            self.event('result_accepted', {'task': task['id'], 'attempt': attempt, 'sha256': sha})
        return True

    def block(self, task, reason):
        with self.tx():
            if not self.db.execute('SELECT 1 FROM tasks WHERE id=?', (task,)).fetchone():
                raise ValueError('Unknown task')
            self.db.execute("UPDATE tasks SET status='blocked',reason=? WHERE id=?", (reason, task))
            self.event('task_blocked', {'task': task, 'reason': reason})

    def recover(self):
        from .storage import recover_downloads
        from .exchange import Exchange
        outcome = recover_downloads(self)
        outcome.extend(Exchange(self).recover())
        for task in self.db.execute("SELECT * FROM tasks WHERE status IN ('pending','running','accepted')").fetchall():
            try:
                self.check_context(task)
            except (Blocked,OSError,ValueError) as exc:
                with self.tx():
                    state='stale' if task['status']=='accepted' else 'blocked'
                    self.db.execute('UPDATE tasks SET status=?,reason=? WHERE id=?',(state,str(exc),task['id']))
                    self.event('context_conflict',{'task':task['id'],'reason':str(exc)})
                outcome.append({'task':task['id'],'action':'blocked','reason':str(exc)})
        for task in self.db.execute("SELECT * FROM tasks WHERE status='running'").fetchall():
            attempt = self.db.execute('SELECT * FROM attempts WHERE id=?', (task['current_attempt'],)).fetchone()
            base = Path('runs') / task['id'] / attempt['id']
            if confined(self.root, base / 'receipt.json').exists():
                try:
                    self.accept(attempt['id'])
                    outcome.append({'task': task['id'], 'action': 'accepted_durable_result'})
                    continue
                except (Blocked, OSError, ValueError, KeyError, TypeError) as exc:
                    self.block(task['id'], str(exc))
                    outcome.append({'task': task['id'], 'action': 'blocked', 'reason': str(exc)})
                    continue
            if attempt['expires'] < time.time():
                with self.tx():
                    self.db.execute("UPDATE tasks SET status='pending',reason='interrupted_attempt' WHERE id=?", (task['id'],))
                    self.db.execute("UPDATE attempts SET status='interrupted' WHERE id=?", (attempt['id'],))
                    self.event('attempt_interrupted', {'task': task['id'], 'attempt': attempt['id']})
                outcome.append({'task': task['id'], 'action': 'retry_ready'})
        # Uncommitted/partial downloads are retained; no source is silently promoted.
        with self.tx():
            self.db.execute("UPDATE reservations SET status='interrupted' WHERE status='active'")
        self.snapshot()
        return outcome

    def snapshot(self):
        rows = [dict(r) for r in self.db.execute('SELECT id,paper,stage,kind,status,current_attempt,reason FROM tasks ORDER BY rowid')]
        events = [dict(r) for r in self.db.execute('SELECT * FROM events ORDER BY seq')]
        atomic_json(confined(self.root, 'state/snapshot.json'), {'tasks': rows, 'event_count': len(events), 'source': 'SQLite ledger'})
        export = confined(self.root, 'state/events.jsonl')
        tmp = export.with_suffix('.jsonl.tmp')
        with tmp.open('w', encoding='utf-8', newline='\n') as f:
            for row in events:
                f.write(canonical(row).decode('utf-8')+'\n')
            f.flush(); os.fsync(f.fileno())
        os.replace(tmp, export)
        lines = ['# NOW — generated from SQLite', '', 'Do not edit task status here.', '',
                 '| Task | Stage | State | Reason |', '| --- | --- | --- | --- |']
        for row in rows:
            reason = (row['reason'] or '').replace('|','/').replace('\n',' ')
            lines.append(f"| {row['id']} | {row['stage']} | {row['status']} | {reason} |")
        text = '\n'.join(lines)+'\n'
        path = confined(self.root, 'NOW.md')
        tmp = path.with_suffix('.md.tmp')
        with tmp.open('w', encoding='utf-8', newline='\n') as f:
            f.write(text); f.flush(); os.fsync(f.fileno())
        os.replace(tmp, path)
        return rows

    def delete_source(self, source):
        raise Blocked('Deletion disabled: no configured, readback-verified archive and cleanup authorization')
