"""Disposable subprocess stopped by its parent at an actual durable import boundary."""
from pathlib import Path
import json
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from icml_audit.core import Ledger,atomic_json
from icml_audit.exchange import Exchange
from icml_audit.storage import Budget
root=Path(sys.argv[1])
with Ledger(root) as ledger:
    policy=json.loads((root/'configs/project_policy.json').read_text())
    budget=Budget(ledger,policy,{'project':str(root)},0,free=lambda _:100_000_000_000,size=lambda:1_000_000)
    exchange=Exchange(ledger,budget)
    def pause(*args):
        atomic_json(root/'ready.json',{'boundary':'raw_saved_attempt_running'})
        while True:time.sleep(.1)
    exchange.validate_return=pause
    exchange.import_return('r1','exchange/inbox/return.json')
