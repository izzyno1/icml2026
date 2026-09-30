#!/usr/bin/env python3
"""Verify original delivery files without installing dependencies or making network calls.
Extra files created during setup are allowed. Changed tracked files mean a modified
working copy, not necessarily damage. Does not interpret or validate paper claims.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys

def verify(root: Path, manifest: dict) -> dict:
    root = root.resolve(strict=True)
    missing, changed, invalid = [], [], []
    entries = manifest.get('files', [])
    if not isinstance(entries, list) or not entries:
        raise ValueError('Manifest must contain nonempty files array')
    seen = set()
    for row in entries:
        rel = row['path']
        posix = PurePosixPath(rel)
        if (not rel or '\\' in rel or ':' in rel or posix.is_absolute()
                or '..' in posix.parts or rel in seen):
            invalid.append(rel)
            continue
        seen.add(rel)
        file = root.joinpath(*posix.parts)
        if not file.resolve().is_relative_to(root) or file.is_symlink():
            invalid.append(rel)
            continue
        if not file.is_file():
            missing.append(rel)
            continue
        h = hashlib.sha256()
        with file.open('rb') as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b''):
                h.update(chunk)
        if file.stat().st_size != row['bytes'] or h.hexdigest() != row['sha256']:
            changed.append(rel)
    return {'ok': not (missing or changed or invalid), 'listed_files': len(entries),
            'missing': missing, 'changed': changed, 'invalid_paths': invalid,
            'scope': 'Original delivery bytes only; not factual or Windows integration validation'}

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    a = ap.parse_args()
    try:
        m = json.loads((a.root / 'MANIFEST.sha256.json').read_text(encoding='utf-8'))
        report = verify(a.root, m)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report['ok'] else 1
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'ERROR: {type(exc).__name__}: {exc}', file=sys.stderr)
        return 2
if __name__ == '__main__':
    raise SystemExit(main())
