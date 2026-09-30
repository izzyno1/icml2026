"""Local ledger/recovery CLI. Never launches Codex, paper code, or a bulk download."""
from pathlib import Path
import argparse
import json
import os
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from icml_audit.core import Ledger,Blocked,versions
from icml_audit.storage import Budget,Downloader
from icml_audit.accounting import ExternalAccounting
from icml_audit.exchange import Exchange
from icml_audit.intake import import_paper


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=ROOT)
    sub=ap.add_subparsers(dest='command',required=True)
    for name in ('init','status','recover','preflight'):
        sub.add_parser(name)
    en=sub.add_parser('enqueue')
    en.add_argument('--task',required=True);en.add_argument('--paper',required=True)
    en.add_argument('--stage',required=True);en.add_argument('--kind',choices=['real','catalog'],default='real')
    en.add_argument('--objective',required=True)
    claim=sub.add_parser('claim');claim.add_argument('--task',required=True)
    accept=sub.add_parser('accept');accept.add_argument('--attempt',required=True)
    export=sub.add_parser('export-pro')
    export.add_argument('--task',required=True);export.add_argument('--review',required=True)
    export.add_argument('--round',choices=['screening','independent_ai_review'],default='screening')
    imp=sub.add_parser('import-pro')
    imp.add_argument('--review',required=True);imp.add_argument('--file',required=True)
    fetch=sub.add_parser('fetch-one')
    fetch.add_argument('--paper',required=True);fetch.add_argument('--url',required=True)
    fetch.add_argument('--role',required=True)
    metadata=sub.add_parser('fetch-metadata',help='One protected official metadata response, at most 1 MB')
    metadata.add_argument('--task',required=True);metadata.add_argument('--url',required=True)
    intake=sub.add_parser('import-paper',help='Offline bounded copy of one user-supplied PDF; provenance remains unverified')
    intake.add_argument('--task',required=True)
    intake.add_argument('--file',required=True,help='Project-relative exchange/manual_intake/<name>.pdf')
    intake.add_argument('--url',required=True,help='Exact public OpenReview URL for the task paper')
    intake.add_argument('--declared-role',choices=['current_attachment_unverified_role','original_submission'],
                        default='current_attachment_unverified_role',help='User declaration only; stored version remains unverified')
    a=ap.parse_args();root=a.root.resolve(strict=True)
    # All controlled scratch/cache writes stay on the project volume; no script activation.
    (root/'cache/tmp').mkdir(parents=True,exist_ok=True)
    os.environ['TEMP']=str(root/'cache/tmp');os.environ['TMP']=str(root/'cache/tmp')
    os.environ['PYTHONDONTWRITEBYTECODE']='1'
    try:
        with Ledger(root) as ledger:
            if a.command in ('init','status'):
                value=ledger.snapshot()
            elif a.command=='recover':
                value=ledger.recover()
            elif a.command=='enqueue':
                value={'task':ledger.enqueue(a.task,a.paper,a.stage,{'objective':a.objective},kind=a.kind)}
                ledger.snapshot()
            elif a.command=='claim':
                value=ledger.claim(a.task);ledger.snapshot()
            elif a.command=='accept':
                value={'new_acceptance':ledger.accept(a.attempt)};ledger.snapshot()
            else:
                policy=json.loads((root/'configs/project_policy.json').read_text(encoding='utf-8'))
                paths=json.loads((root/'configs/setup_paths.json').read_text(encoding='utf-8'))
                accounting_path=root/'configs/storage_accounting.json'
                accounting=json.loads(accounting_path.read_text(encoding='utf-8')) if accounting_path.exists() else {}
                meter=ExternalAccounting(root,accounting)
                used_paths={**paths['used_paths'], **{('accounting_'+k):str(v) for k,v in meter.roots.items()}}
                budget=Budget(ledger,policy,used_paths,meter)
                if a.command=='preflight':
                    value=budget.check(policy['network']['default_document_max_bytes'])
                    value['external_accounting']=meter.last
                elif a.command=='export-pro':
                    value=Exchange(ledger,budget).export(a.task,a.review,a.round)
                elif a.command=='import-pro':
                    value=Exchange(ledger,budget).import_return(a.review,a.file)
                else:
                    approval=root/'state/offline_acceptance.json'
                    if not approval.is_file():
                        raise Blocked('Offline/recovery acceptance receipt is missing')
                    receipt=json.loads(approval.read_text(encoding='utf-8'))
                    current=versions(root)
                    if receipt.get('status')!='pass' or any(receipt.get(k)!=current[k] for k in ('code_hash','rules_hash')):
                        raise Blocked('Offline acceptance does not match current implementation/rules')
                    if a.command=='import-paper':
                        value=import_paper(budget,a.task,a.file,a.url,a.declared_role)
                    elif a.command=='fetch-metadata':
                        task=ledger.db.execute('SELECT * FROM tasks WHERE id=?',(a.task,)).fetchone()
                        if not task or task['kind'] not in {'catalog','real'} or task['status'] not in {'pending','running'}:
                            raise Blocked('Metadata retrieval needs an explicit active catalog/real task')
                        ledger.check_context(task)
                        value=Downloader(budget).fetch(a.url,task['paper'],'official_catalog',media='metadata')
                    else:
                        # A manually enqueued real task is required; no historical sample default.
                        papers={r[0] for r in ledger.db.execute("SELECT DISTINCT paper FROM tasks WHERE kind='real'")}
                        if a.paper not in papers:
                            raise Blocked('Enqueue an explicit real-paper task before retrieval')
                        value=Downloader(budget).fetch(a.url,a.paper,a.role)
            print(json.dumps(value,ensure_ascii=False,indent=2))
            return 0
    except (Blocked,OSError,ValueError,KeyError) as exc:
        print(json.dumps({'status':'blocked','reason':str(exc)},ensure_ascii=False))
        return 2


if __name__=='__main__':
    raise SystemExit(main())
