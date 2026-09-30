#!/usr/bin/env python3
"""Run only bounded local unit tests; not browser/network or real-corpus tests."""
from pathlib import Path
import subprocess
import sys
import argparse

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--active-only',action='store_true',help='Run published active tests; historical fixture suites remain local')
    args=parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    suites = [('unified', root / 'tests', 'test_*.py'),
              ('v1', root / 'reference/v1/icml2026_audit/tests', 'test_audit.py'),
              ('v2', root / 'reference/v2/icml2026_genealogy_v2/tests', 'test_helpers.py'),
              ('v3', root / 'reference/v3/icml2026_longrun_v3/tests', 'test_storage_budget.py')]
    if args.active_only:
        suites=suites[:1]
    failures = []
    for name, directory, pattern in suites:
        print(f'\n=== {name}: offline unit tests ===', flush=True)
        try:
            p = subprocess.run([sys.executable, '-X', 'utf8', '-m', 'unittest',
                                'discover', '-s', str(directory), '-p', pattern, '-v'],
                               cwd=root, timeout=120, check=False)
            if p.returncode:
                failures.append(name)
        except (OSError, subprocess.TimeoutExpired) as exc:
            print(f'{name}: {type(exc).__name__}', file=sys.stderr)
            failures.append(name)
    print('\nOffline result:', 'PASS' if not failures else f'FAIL {failures}')
    print('Not tested here: native sandbox/auth, live network, real corpus, semantic evidence, full desktop restart or OS-wide quota. Ledger/recovery and managed storage are covered by synthetic tests.')
    return int(bool(failures))
if __name__ == '__main__':
    raise SystemExit(main())
