#!/usr/bin/env python3
"""Offline project probe; no installs, network, model calls, or credential reads.
Reports logical project size, not snapshots/other-device storage. Budget checks here
are diagnostics; they do not implement a downloader quota or cache eviction system.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import sqlite3
import stat
import sys
import tempfile
from datetime import datetime, timezone
from typing import Any

GB = 1_000_000_000
GIB = 1024 ** 3

def within_root(root: Path, path: Path) -> Path:
    root = root.resolve(strict=True)
    resolved = path.resolve()
    if not resolved.is_relative_to(root):
        raise ValueError('Output must remain inside the selected project root')
    return resolved

def scan_project(root: Path, max_entries: int = 100_000) -> dict[str, Any]:
    """Size metadata only. Skip all symlinks and Windows reparse points."""
    root = root.resolve(strict=True)
    if not root.is_dir() or root.parent == root or root == Path.home().resolve():
        raise ValueError('Choose a dedicated project folder, not a volume root or user home')
    if max_entries < 1:
        raise ValueError('max_entries must be positive')
    total = count = visited = skipped = 0
    pending = [root]
    issues: list[dict[str, str]] = []
    complete = True
    while pending:
        folder = pending.pop()
        try:
            with os.scandir(folder) as entries:
                for entry in entries:
                    visited += 1
                    if visited > max_entries:
                        complete = False
                        issues.append({'path': '.', 'reason': 'entry_limit_reached'})
                        return dict(logical_bytes=total, file_count=count, entries_visited=visited,
                                    skipped_links=skipped, complete=complete, issues=issues)
                    try:
                        s = entry.stat(follow_symlinks=False)
                        if entry.is_symlink() or (getattr(s, 'st_file_attributes', 0) & 0x400):
                            skipped += 1
                            continue
                        if stat.S_ISDIR(s.st_mode):
                            pending.append(Path(entry.path))
                        elif stat.S_ISREG(s.st_mode):
                            total += s.st_size
                            count += 1
                    except OSError as exc:
                        complete = False
                        issues.append({'path': str(Path(entry.path).relative_to(root)),
                                       'reason': type(exc).__name__})
        except OSError as exc:
            complete = False
            issues.append({'path': str(folder.relative_to(root)), 'reason': type(exc).__name__})
    return dict(logical_bytes=total, file_count=count, entries_visited=visited,
                skipped_links=skipped, complete=complete, issues=issues)

def storage_status(size_bytes: int, free_values: list[int], policy: dict[str, Any]) -> dict[str, Any]:
    s = policy['storage']
    soft = float(s['project_soft_budget_gb']) * GB
    hard = float(s['project_hard_budget_gb']) * GB
    floor = float(s['min_free_per_used_volume_gb']) * GB
    if not (0 < soft < hard and floor >= 0) or size_bytes < 0:
        raise ValueError('Invalid storage policy or measured size')
    hard_hit = size_bytes >= hard
    low_free = any(f < floor for f in free_values)
    return {'project_soft_reached': size_bytes >= soft,
            'project_hard_reached': hard_hit, 'observed_volume_low_free': low_free,
            'pause_new_large_writes': hard_hit or low_free,
            'scope': 'Observed project and project/TEMP free-space checks only; external caches not audited',
            'enforcement': 'diagnostic_only_not_a_quota_manager'}

def smoke(root: Path) -> dict[str, str]:
    """Use only freshly created project scratch; explicitly close SQLite on Windows."""
    parent = within_root(root, root / 'cache' / 'setup_smoke')
    parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='doctor_', dir=parent) as tmp:
        d = Path(tmp)
        payload = {'text': '论文谱系：未知不能变成已验证', 'status': 'synthetic_test_only'}
        raw = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        staging, final = d / 'result.tmp', d / 'result.json'
        staging.write_bytes(raw)
        os.replace(staging, final)
        if json.loads(final.read_text(encoding='utf-8')) != payload:
            raise RuntimeError('UTF-8 roundtrip failed')
        con = sqlite3.connect(d / 'smoke.sqlite3')
        try:
            con.execute('CREATE TABLE item (id INTEGER PRIMARY KEY, text TEXT NOT NULL)')
            con.execute('INSERT INTO item VALUES (?,?)', (1, payload['text']))
            con.commit()
        finally:
            con.close()
        con = sqlite3.connect(d / 'smoke.sqlite3')
        try:
            row = con.execute('SELECT text FROM item WHERE id=?', (1,)).fetchone()
            if row != (payload['text'],):
                raise RuntimeError('SQLite reopen failed')
            integrity = con.execute('PRAGMA integrity_check').fetchone()
            if integrity != ('ok',):
                raise RuntimeError('SQLite integrity check failed')
        finally:
            con.close()
        result = {'utf8_roundtrip': 'pass', 'atomic_replace': 'pass',
                  'sqlite_reopen': 'pass', 'sqlite_integrity': 'pass',
                  'fixture_sha256': hashlib.sha256(raw).hexdigest(),
                  'scope': 'local_synthetic_io_not_scheduler_recovery'}
    result['scratch_cleanup'] = 'pass'
    return result

def probe(root: Path, run_smoke: bool = False) -> dict[str, Any]:
    root = root.resolve(strict=True)
    config_path = within_root(root, root / 'configs' / 'project_policy.json')
    policy = json.loads(config_path.read_text(encoding='utf-8'))
    measured = scan_project(root)
    volumes = []
    for label, path in [('project', root), ('temp', Path(tempfile.gettempdir()))]:
        usage = shutil.disk_usage(path)
        volumes.append({'role': label, 'path': str(path), 'free_bytes': usage.free,
                        'free_GB': round(usage.free / GB, 3), 'free_GiB': round(usage.free / GIB, 3)})
    candidates = {'git': ['git.exe', 'git'], 'codex_cli': ['codex.exe', 'codex.cmd', 'codex'],
                  'node_optional': ['node.exe', 'node'], 'npm_optional': ['npm.cmd', 'npm'],
                  'python_launcher_optional': ['py.exe', 'py']}
    located = {name: next((p for x in names if (p := shutil.which(x))), None)
               for name, names in candidates.items()}
    return {'generated_at_utc': datetime.now(timezone.utc).isoformat(),
            'report_kind': 'offline_environment_probe_not_setup_acceptance',
            'project_root': str(root),
            'platform': {'system': platform.system(), 'release': platform.release(),
                         'machine': platform.machine()},
            'python': {'version': platform.python_version(), 'executable': sys.executable,
                       'in_virtualenv': sys.prefix != sys.base_prefix,
                       'sqlite_version': sqlite3.sqlite_version},
            'tools_on_path_not_executed': located,
            'project_size': measured, 'volume_observations': volumes,
            'storage_diagnostic': storage_status(measured['logical_bytes'],
                                                 [v['free_bytes'] for v in volumes], policy),
            'local_smoke': smoke(root) if run_smoke else {'status': 'not_run'},
            'not_checked': ['Codex login or account', 'Codex CLI execution', 'GUI settings',
                            'Windows sandbox enforcement', 'HTTP or web search',
                            'project-external caches', 'real corpus', 'scheduler or disk quota'],
            'credential_files_read': False, 'network_requests': 0,
            'notes': ['Project size is logical bytes at scan time; sparse allocation, snapshots and other caches differ.',
                      'Do not treat a located executable as a successfully tested tool.']}

def save_report(root: Path, report: dict[str, Any]) -> Path:
    folder = within_root(root, root / 'reports')
    folder.mkdir(exist_ok=True, parents=True)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    dest = within_root(root, folder / f'environment_probe_{stamp}.json')
    with dest.open('x', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
        f.write('\n')
    return dest

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--smoke', action='store_true', help='Tiny synthetic I/O test inside project scratch')
    p.add_argument('--write-report', action='store_true', help='Write timestamped non-secret report inside project')
    args = p.parse_args()
    try:
        result = probe(args.root, args.smoke)
        if args.write_report:
            result['saved_report'] = str(save_report(args.root.resolve(), result))
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, RuntimeError, sqlite3.Error) as exc:
        print(f'ERROR: {type(exc).__name__}: {exc}', file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
