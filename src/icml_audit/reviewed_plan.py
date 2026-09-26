"""Validate a bounded, version-bound OpenReview PDF plan before any authentication."""
from pathlib import Path
import json
import re
from .core import Blocked,confined,file_hash

API='https://api2.openreview.net'

def read_small(root,relative,limit):
    path=confined(root,relative)
    if not path.is_file() or path.stat().st_nlink!=1 or path.stat().st_size>limit:
        raise Blocked('Invalid bounded plan input file')
    return path,json.loads(path.read_text(encoding='utf-8'))

def validate_jobs(jobs):
    if not isinstance(jobs,(tuple,list)) or not 1<=len(jobs)<=20:
        raise Blocked('P2 plan must contain 1 to 20 PDF jobs')
    checked=[]
    for job in jobs:
        if not isinstance(job,(tuple,list)) or len(job)!=3:
            raise Blocked('Invalid PDF job')
        paper,role,url=job
        if not isinstance(paper,str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,100}',paper):
            raise Blocked('Invalid forum identity')
        expected={'current_attachment_unverified_role':API+'/pdf?id='+paper,
                  'original_submission':API+'/attachment?id='+paper+'&name=originally_submitted_PDF'}
        if role not in expected or url!=expected[role]:
            raise Blocked('PDF URL or version role differs from reviewed endpoint')
        checked.append((paper,role,url))
    if len({p for p,_,_ in checked})>10 or len({u for _,_,u in checked})!=len(checked):
        raise Blocked('Duplicate PDF job or more than ten target papers')
    return tuple(checked)

def load_reviewed_plan(ledger,relative):
    relative=Path(relative)
    if relative.parent!=Path('exchange/download_plans') or relative.suffix!='.json':
        raise Blocked('Use one project exchange/download_plans JSON file')
    path,value=read_small(ledger.root,relative,131072)
    if not isinstance(value,dict) or value.get('schema_version')!='p2-fixed-pilot-1' or value.get('maximum_papers')!=10 or value.get('maximum_pdf_requests')!=20:
        raise Blocked('Unsupported bounded plan schema or limits')
    records=value.get('jobs')
    if not isinstance(records,list) or not all(isinstance(x,dict) for x in records):
        raise Blocked('Invalid PDF plan records')
    jobs=validate_jobs([(x.get('paper'),x.get('role'),x.get('url')) for x in records])
    task=ledger.db.execute('SELECT * FROM tasks WHERE id=?',(value.get('catalog_task_id'),)).fetchone()
    if not task or task['kind']!='catalog' or task['status']!='accepted':
        raise Blocked('A current accepted catalog task is required')
    ledger.check_context(task)
    inputs=json.loads(task['inputs'])
    if inputs['inputs'].get('catalog_report_sha256')!=value.get('catalog_report_sha256'):
        raise Blocked('Catalog report is not bound to the accepted task')
    report_path,report=read_small(ledger.root,value.get('catalog_report',''),524288)
    if file_hash(report_path)!=value.get('catalog_report_sha256'):
        raise Blocked('Catalog report byte hash conflict')
    report_records={r['forum_id']:r for r in report['records']}
    bindings=[]
    for job in records:
        paper=job['paper'];sid=job.get('metadata_source_id')
        s=ledger.db.execute('SELECT * FROM sources WHERE id=?',(sid,)).fetchone()
        if not s or s['paper']!='OR_'+paper or s['role']!='official_catalog' or s['status']!='available' or sid not in inputs['sources']:
            raise Blocked('PDF identity needs bound available official metadata')
        if s['url']!='https://openreview.net/forum?id='+paper or s['sha256']!=job.get('metadata_sha256'):
            raise Blocked('Official metadata identity or hash conflict')
        cur=ledger.db.execute('SELECT source FROM current_sources WHERE family=?',(s['family'],)).fetchone()
        if not cur or cur[0]!=sid:
            raise Blocked('Official metadata source is stale')
        meta_path,meta=read_small(ledger.root,s['path'],2_000_000)
        if file_hash(meta_path)!=s['sha256']:
            raise Blocked('Official metadata byte hash conflict')
        url=meta.get('url',meta.get('tab',{}).get('url'));snapshot=meta.get('snapshot','')
        required=['ICML 2026 spotlight','Accept (spotlight)','/pdf?id='+paper,
                  '/attachment?id='+paper+'&name=originally_submitted_PDF']
        if url!=s['url'] or not all(x in snapshot for x in required):
            raise Blocked('Saved official record lacks reviewed pilot identity/version links')
        record=report_records.get(paper,{})
        if record.get('source_id')!=sid or record.get('source_sha256')!=s['sha256']:
            raise Blocked('Catalog report/source binding mismatch')
        bindings.append(sid)
    return {'path':relative.as_posix(),'sha256':file_hash(path),'jobs':jobs,
            'metadata_source_ids':sorted(set(bindings)),
            'catalog_task_id':task['id'],'catalog_report_sha256':file_hash(report_path)}
