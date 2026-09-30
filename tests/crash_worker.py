"""Synthetic crash fixture only. Parent test kills this exact process."""
from pathlib import Path
import json
import sys
import time

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from icml_audit.core import Ledger,atomic_json

root=Path(sys.argv[1]);mode=sys.argv[2]
with Ledger(root) as ledger:
    ledger.enqueue('crash','synthetic','extract',{'test':'crash'},kind='synthetic')
    packet=ledger.claim('crash',lease_seconds=300 if mode!='partial' else 0.2)
    if mode=='partial':
        atomic_json(root/'runs'/packet['id']/packet['attempt_id']/'result.json.tmp',{'partial':True})
    else:
        ledger.write_result(packet,{'claims':[],'novelty_label':'U'})
        if mode=='committed':
            ledger.accept(packet['attempt_id'])
    atomic_json(root/'ready.json',{'attempt':packet['attempt_id']})
    while True:
        time.sleep(0.1)
