"""Fail-closed streaming storage. One coordinator, no deletion, no automatic retries."""
from __future__ import annotations
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import math
import os
import shutil
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
import uuid
from .core import Blocked, atomic_json, confined, file_hash, validate_source_role
from .accounting import metadata_bytes

HOSTS = {'icml.cc', 'openreview.net', 'api2.openreview.net', 'proceedings.mlr.press', 'arxiv.org', 'export.arxiv.org'}
# Public download links observed on the publishers' pages, 2026-09-25.
# These are preprint mirrors, not evidence of an original or camera-ready version.
# Exact URLs deliberately do not authorize a whole hosting service or bulk fetches.
REVIEWED_MIRROR_URLS = frozenset({
    # NeurIPS publisher PDF linked from its official abstract record, 2026-09-26.
    'https://papers.nips.cc/paper_files/paper/2025/file/95738b4062a7fed00bb9db468475ae53-Paper-Conference.pdf',
    # Author-hosted 2014 journal PDF, title/DOI checked against the first page.
    'https://lecueguillaume.github.io/assets/AOS1190.pdf',
    'https://pdfs.assets.alphaxiv.org/2605.30997v1.pdf',
    'https://www.researchgate.net/publication/405562119_Hedging_on_the_Frontier_Learning_New_Tasks_with_Few_Samples/fulltext/6a1d06097076b91843485bd4/Hedging-on-the-Frontier-Learning-New-Tasks-with-Few-Samples.pdf',
})
UA = 'ICMLContributionAudit/0.2 (bounded personal research)'


def validate_url(url):
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != 'https' or (parsed.hostname not in HOSTS and url not in REVIEWED_MIRROR_URLS) or parsed.username or parsed.password or parsed.port not in (None,443):
        raise Blocked('Unapproved scholarly HTTPS URL')
    return url


def validate_download_role(url, role):
    validate_source_role(role)
    if url in REVIEWED_MIRROR_URLS and role not in {'preprint', 'prior_work'}:
        raise Blocked('Reviewed preprint mirror cannot establish an official version role')


def logical_size(root):
    return metadata_bytes(root)['logical_bytes']


class Budget:
    def __init__(self, ledger, policy, used_paths, external_bytes=None, free=None, size=None):
        self.ledger, self.root, self.policy = ledger, ledger.root, policy
        self.used_paths, self.external_bytes = used_paths, external_bytes
        self.free = free or (lambda volume: shutil.disk_usage(volume).free)
        self.size = size or (lambda: logical_size(self.root))
        if not used_paths:
            raise Blocked('Used-volume inventory is required')
        s=policy['storage']
        if not (0 < s['project_soft_budget_gb'] < s['project_hard_budget_gb'] and s['min_free_per_used_volume_gb']>=0 and s['preflight_reserve_bytes']>=0):
            raise Blocked('Invalid storage policy')
        self.volume_floors = {}
        for volume, amount in s.get('min_free_by_volume_gb', {}).items():
            if (not isinstance(volume, str) or not Path(volume).is_absolute()
                    or str(Path(volume)) != str(Path(volume).anchor)
                    or isinstance(amount, bool) or not isinstance(amount, (int, float))
                    or not math.isfinite(amount) or amount < 0):
                raise Blocked('Invalid per-volume free-space policy')
            self.volume_floors[str(Path(volume).anchor).casefold()] = int(amount*1e9)

    def check(self, extra=0):
        if isinstance(extra, bool) or not isinstance(extra, int) or extra < 0:
            raise Blocked('Additional reservation must be nonnegative integer bytes')
        s = self.policy['storage']
        floor = int(s['min_free_per_used_volume_gb']*1e9)
        reserve = int(s['preflight_reserve_bytes'])
        active = self.ledger.db.execute("SELECT COALESCE(SUM(maximum-written),0) FROM reservations WHERE status='active'").fetchone()[0]
        observed = {}
        for value in self.used_paths.values():
            anchor = str(Path(value).anchor)
            if not anchor:
                raise Blocked('Used paths must be absolute')
            observed[anchor] = self.free(anchor)
        for anchor, available in observed.items():
            selected_floor = self.volume_floors.get(anchor.casefold(), floor)
            needed = selected_floor + reserve + (active + extra if anchor == self.root.anchor else 0)
            if available < needed:
                raise Blocked(f'Volume {anchor} below required reserve: free={available}, required={needed}')
        external = self.external_bytes() if callable(self.external_bytes) else self.external_bytes
        if external is None:
            raise Blocked('External attributable storage is not accounted; do not assume zero')
        if not isinstance(external, int) or isinstance(external, bool) or external < 0:
            raise Blocked('Invalid external storage accounting')
        used = self.size() + external
        if used + active + extra + reserve >= int(s['project_hard_budget_gb']*1e9):
            raise Blocked('Project 50 GB hard budget/reservations exhausted')
        return {'project_and_external_bytes': used, 'remaining_reservations': active,
                'warning_40GB': used >= int(s['project_soft_budget_gb']*1e9),
                'volumes_free_bytes': observed, 'scope': 'Managed downloader only; not OS quota'}

    def reserve(self, maximum):
        if not isinstance(maximum, int) or isinstance(maximum,bool) or maximum < 1 or maximum > self.policy['network']['default_document_max_bytes']:
            raise Blocked('Invalid document byte limit')
        # The OS writer lock remains held for the whole transfer. No competing coordinator.
        self.check(maximum)
        rid = uuid.uuid4().hex
        relative = str(Path('cache/partials') / (rid+'.part'))
        path = confined(self.root, relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        with self.ledger.tx():
            self.ledger.db.execute('INSERT INTO reservations VALUES(?,?,?,?,?)', (rid,maximum,0,'active',relative))
            self.ledger.event('download_reserved', {'reservation':rid,'maximum':maximum})
        return rid, path

    def finish(self, rid, state):
        with self.ledger.tx():
            self.ledger.db.execute('UPDATE reservations SET status=? WHERE id=?',(state,rid))
            self.ledger.event('download_reservation_closed', {'reservation':rid,'state':state})


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise Blocked('Redirect needs separately verified source URL; no automatic follow')


def recover_downloads(ledger):
    outcomes=[]
    for row in ledger.db.execute("SELECT * FROM reservations WHERE status IN ('active','interrupted')").fetchall():
        receipt_path=confined(ledger.root,Path('cache/partials')/(row['id']+'.receipt.json'))
        if not receipt_path.exists():
            continue
        try:
            if receipt_path.stat().st_size>8192:
                raise Blocked('Oversized download receipt')
            receipt=json.loads(receipt_path.read_text(encoding='utf-8'))
            media=receipt.get('media','pdf')
            if media not in {'pdf','metadata'}:
                raise Blocked('Unknown recovered media type')
            expected=str(Path('data/objects')/(receipt['sha256']+('.pdf' if media=='pdf' else '.txt')))
            if receipt['reservation']!=row['id'] or receipt['path']!=expected:
                raise Blocked('Download receipt identity/path mismatch')
            validate_url(receipt['url']);validate_url(receipt['final_url'])
            validate_download_role(receipt['url'], receipt['role'])
            obj=confined(ledger.root,receipt['path'])
            if obj.stat().st_size!=receipt['bytes'] or file_hash(obj)!=receipt['sha256']:
                raise Blocked('Recovered source hash conflict')
            sid=ledger.source(receipt['paper'],receipt['role'],receipt['url'],receipt['path'],receipt['final_url'],retrieved_at=receipt['retrieved_at'])
            with ledger.tx():
                ledger.db.execute("UPDATE reservations SET status='complete' WHERE id=?",(row['id'],))
                ledger.event('download_recovered',{'reservation':row['id'],'source':sid})
            outcomes.append({'reservation':row['id'],'action':'source_registered','source':sid})
        except (Blocked,OSError,ValueError,KeyError,TypeError) as exc:
            outcomes.append({'reservation':row['id'],'action':'blocked','reason':str(exc)})
    return outcomes


class Downloader:
    def __init__(self, budget):
        self.budget, self.ledger, self.root = budget, budget.ledger, budget.root
        self.opener = urllib.request.build_opener(NoRedirect())
        self.last_request = 0

    def wait(self):
        delay = self.budget.policy['network']['minimum_request_spacing_seconds']
        time.sleep(max(0, delay-(time.monotonic()-self.last_request)))
        self.last_request=time.monotonic()

    def fetch(self, url, paper, role, maximum=None, media='pdf'):
        """Production network path. Budget gate is evaluated before *any* socket request."""
        validate_url(url)
        validate_download_role(url, role)
        if media not in {'pdf','metadata'}:
            raise Blocked('Unsupported media type')
        maximum = maximum or (1_000_000 if media=='metadata' else self.budget.policy['network']['default_document_max_bytes'])
        if media=='metadata' and maximum>1_000_000:
            raise Blocked('Metadata response cap is 1 MB; use bounded pagination')
        rid, path = self.budget.reserve(maximum)
        try:
            parsed = urllib.parse.urlsplit(url)
            robots_url = f'https://{parsed.hostname}/robots.txt'
            self.wait()
            try:
                with self.opener.open(urllib.request.Request(robots_url, headers={'User-Agent':UA}), timeout=15) as response:
                    raw = response.read(1_000_001)
                if len(raw)>1_000_000:
                    raise Blocked('robots.txt exceeds bounded response size')
                robot = urllib.robotparser.RobotFileParser()
                robot.parse(raw.decode('utf-8','replace').splitlines())
                if not robot.can_fetch(UA,url):
                    raise Blocked('Provider robots policy disallows retrieval')
                crawl = robot.crawl_delay(UA)
                if crawl and crawl > self.budget.policy['network']['minimum_request_spacing_seconds']:
                    raise Blocked('Provider requires longer request spacing; adjust reviewed policy first')
            except urllib.error.HTTPError as exc:
                if exc.code != 404:
                    raise Blocked(f'Cannot verify provider robots policy: HTTP {exc.code}') from exc
            self.wait()
            accept='application/pdf' if media=='pdf' else 'application/json,text/html,text/plain'
            req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':accept,'Accept-Encoding':'identity'})
            with self.opener.open(req,timeout=self.budget.policy['network']['request_timeout_seconds']) as response:
                if response.status != 200 or response.geturl() != url:
                    raise Blocked('Unexpected response status/URL')
                return self.store_stream(response,url,paper,role,maximum,rid,path,media)
        except BaseException:
            self.budget.finish(rid,'interrupted')
            raise

    def store_stream(self, response, url, paper, role, maximum, rid=None, path=None, media='pdf', provenance=None):
        """Common streaming implementation; offline tests inject bounded synthetic streams."""
        validate_url(url)
        validate_download_role(url, role)
        if media not in {'pdf','metadata'} or (media=='metadata' and maximum>1_000_000):
            raise Blocked('Unsupported media or metadata byte cap')
        if rid is None:
            rid,path=self.budget.reserve(maximum)
        written=0
        deadline=time.monotonic()+self.budget.policy['network']['request_timeout_seconds']
        try:
            header=response.headers.get('Content-Length')
            declared=None
            if header is not None:
                if not str(header).isdigit():
                    raise Blocked('Invalid Content-Length')
                declared=int(header)
                if declared>maximum:
                    raise Blocked('Declared document exceeds limit')
            if response.headers.get('Content-Encoding','identity').lower() not in ('','identity'):
                raise Blocked('Encoded transfer unsupported; avoid decompression bombs')
            h=hashlib.sha256()
            signature=b''
            with path.open('xb') as output:
                while True:
                    if time.monotonic()>=deadline:
                        raise Blocked('Transfer total-time budget exceeded')
                    self.budget.check()
                    # One sentinel byte detects a lying/unknown length, never written past cap.
                    # Reserve the full document first; check the actual disk before
                    # and after each bounded 1 MiB read. Recounting all registered
                    # development storage every 64 KiB dominated real transfers.
                    chunk=response.read(min(1024*1024,maximum-written+1))
                    if not chunk:
                        break
                    if written+len(chunk)>maximum:
                        raise Blocked('Stream exceeds document limit')
                    self.budget.check()
                    if len(signature)<16:
                        signature=(signature+chunk)[:16]
                    output.write(chunk)
                    output.flush()
                    written+=len(chunk)
                    h.update(chunk)
                    with self.ledger.tx():
                        self.ledger.db.execute('UPDATE reservations SET written=? WHERE id=?',(written,rid))
                output.flush();os.fsync(output.fileno())
            if declared is not None and declared!=written:
                raise Blocked('Content-Length mismatch/truncated transfer')
            if media=='pdf' and not signature.lstrip().startswith(b'%PDF-'):
                raise Blocked('Response is not PDF bytes; not a successful source')
            if media=='metadata':
                mime=response.headers.get('Content-Type','').split(';')[0].strip().lower()
                if mime not in {'application/json','text/html','text/plain','application/xhtml+xml'}:
                    raise Blocked('Unexpected metadata content type')
                content=path.read_text(encoding='utf-8-sig')
                if not content.strip() or '\x00' in content:
                    raise Blocked('Empty or binary metadata')
                if mime=='application/json':
                    json.loads(content)
            digest=h.hexdigest()
            dest=confined(self.root,Path('data/objects')/(digest+('.pdf' if media=='pdf' else '.txt')))
            dest.parent.mkdir(parents=True,exist_ok=True)
            if dest.exists():
                if file_hash(dest)!=digest:
                    raise Blocked('Existing evidence object hash conflict')
                # Delete only this freshly downloaded duplicate after exact hash verification.
                if path.parent != confined(self.root,'cache/partials'):
                    raise Blocked('Scratch cleanup boundary mismatch')
                path.unlink()
            else:
                os.replace(path,dest)
            receipt={'reservation':rid,'url':url,'final_url':url,'paper':paper,'role':role,
                     'retrieved_at':datetime.now(timezone.utc).isoformat(),
                     'sha256':digest,'bytes':written,'path':str(dest.relative_to(self.root)),
                     'read_scope':'not_read','status':'bytes_saved_not_yet_registered','media':media,
                     'content_type':response.headers.get('Content-Type')}
            if provenance is not None:
                receipt['acquisition']=provenance
            atomic_json(confined(self.root,Path('cache/partials')/(rid+'.receipt.json')),receipt)
            sid=self.ledger.source(paper,role,url,receipt['path'],retrieved_at=receipt['retrieved_at'])
            self.budget.finish(rid,'complete')
            return {**receipt,'source_id':sid,'status':'available_not_read'}
        except BaseException:
            # Retain .part or hashed blob, never label a partial download successful.
            self.budget.finish(rid,'interrupted')
            raise
