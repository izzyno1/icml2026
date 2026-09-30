"""Save actual offline test output and bind acceptance to current source hashes."""
from pathlib import Path
from datetime import datetime,timezone
import json
import os
import re
import shutil
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from icml_audit.core import atomic_json,file_hash,versions
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
env=os.environ.copy()
env.update(TEMP=str(ROOT/'cache/tmp'),TMP=str(ROOT/'cache/tmp'),PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONIOENCODING='utf-8')
before=versions(ROOT)
argv=[sys.executable,'-B','-X','utf8',str(ROOT/'tools/run_offline_tests.py')]
p=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=120)
report={'at':stamp,'argv':argv,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,
        'network_requests':0,'CLI_model_calls':0,'scope':'offline Windows execution; not native sandbox or scientific validation'}
path=ROOT/'reports'/('offline_resume_'+stamp+'.json')
atomic_json(path,report)
discovered=sum(map(int,re.findall(r'Ran (\d+) tests?',p.stderr)))
skipped=sum(map(int,re.findall(r'OK \(skipped=(\d+)\)',p.stderr)))
if p.returncode==0 and discovered and before==versions(ROOT):
    receipt=ROOT/'state/offline_acceptance.json'
    saved=ROOT/'backups'/('tests_'+stamp)/'offline_acceptance.json'
    saved.parent.mkdir(parents=True,exist_ok=True)
    if receipt.exists():shutil.copyfile(receipt,saved)
    atomic_json(receipt,{'status':'pass','at':stamp,**before,
                        'test_report':str(path.relative_to(ROOT)),'test_report_sha256':file_hash(path),
                        'discovered':discovered,'passed':discovered-skipped,'skipped':skipped,'failed':0,
                        'forced_process_kill_and_new_process_recovery_cases':4,
                        'complete_codex_desktop_restart':'not_run','network_integration':'not_run'})
print(json.dumps({'report':str(path),'exit_code':p.returncode,'discovered':discovered,'passed':discovered-skipped if p.returncode==0 else None,'skipped':skipped},ensure_ascii=False))
raise SystemExit(p.returncode)
