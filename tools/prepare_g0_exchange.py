"""Prepare a tiny synthetic evidence task; never simulates an external return."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from icml_audit.core import Ledger,confined

def main():
    task='G0_02_synthetic_001'
    path=confined(ROOT,'data/synthetic/g0_marker.txt')
    content=b'Line 1: This is synthetic evidence, not a real paper.\nLine 2: The marker is BLUE.\nLine 3: No prior work or novelty conclusion is supplied.\n'
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists() and path.read_bytes()!=content:
        raise RuntimeError('Preserve conflicting fixture; inspect before proceeding')
    if not path.exists():
        with path.open('xb') as f:f.write(content)
    with Ledger(ROOT) as ledger:
        source=ledger.source('G0_synthetic','synthetic','https://example.org/synthetic-not-a-paper',
                             str(path.relative_to(ROOT)))
        ledger.enqueue(task,'G0_synthetic','protocol_review',
            {'objective':'Test visible-file reporting and evidence locators; report the synthetic marker, retain novelty U, and identify missing prior work.',
             'provided_ranges':{source:['lines 1-3']},
             'missing_ranges':{source:['No real paper or prior work; protocol test only']}},
            [source],kind='synthetic',prompt='G0 protocol smoke test, not scientific analysis')
        ledger.snapshot()
    print(task)

if __name__=='__main__':main()
