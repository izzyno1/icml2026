"""Interactive API2 login and a fixed, bounded PDF pilot. Secrets stay in this process.

Uses the REST login and Bearer flow in OpenReview's official Python client.
Does not inspect browser/session files or credential environment variables.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import getpass
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import warnings
from .core import Ledger, Blocked, atomic_json, file_hash, versions
from .storage import Budget, Downloader, NoRedirect, UA
from .accounting import ExternalAccounting

API = 'https://api2.openreview.net'
AUTH_LIMIT = 65536
PILOT = (
    ('J4wRLmh29t', 'current_attachment_unverified_role', API+'/pdf?id=J4wRLmh29t'),
    ('J4wRLmh29t', 'original_submission', API+'/attachment?id=J4wRLmh29t&name=originally_submitted_PDF'),
    ('aIH1jyU37z', 'current_attachment_unverified_role', API+'/pdf?id=aIH1jyU37z'),
    ('wsA8LgHU5U', 'current_attachment_unverified_role', API+'/pdf?id=wsA8LgHU5U'),
)
KNOWN_ERRORS = {'ChallengeRequiredError', 'TokenExpiredError', 'ForbiddenError',
                'NotFoundError', 'ValidationError', 'AuthenticationError', 'RateLimitError'}


def safe_failure(exc):
    """Never propagate provider messages/headers, which may contain credentials."""
    if isinstance(exc, urllib.error.HTTPError):
        name = 'HTTPError'
        try:
            data = json.loads(exc.read(4096))
            if isinstance(data, dict) and data.get('name') in KNOWN_ERRORS:
                name = data['name']
        except (OSError, ValueError, TypeError):
            pass
        finally:
            exc.close()
        return {'status': 'blocked', 'http_status': exc.code, 'error': name}
    if isinstance(exc, Blocked):
        return {'status': 'blocked', 'error': 'LocalGuardOrProtocolRejected'}
    if isinstance(exc, (EOFError, KeyboardInterrupt)):
        return {'status': 'cancelled', 'error': 'InteractiveLoginCancelled'}
    return {'status': 'blocked', 'error': 'NetworkOrLocalFailure'}


def hidden_prompt(prompt):
    if not sys.stdin.isatty():
        raise Blocked('Use your own interactive console; never pipe credentials')
    with warnings.catch_warnings():
        warnings.simplefilter('error', getpass.GetPassWarning)
        value = getpass.getpass(prompt)
    if not value or len(value)>4096:
        raise Blocked('Empty or oversized input')
    return value


class ScopedBearer(urllib.request.BaseHandler):
    """Attach the fresh session only to the four reviewed PDF URLs, never robots."""
    def __init__(self, value):
        if not isinstance(value,str) or not value or len(value)>16384 or not value.isascii() or any(c.isspace() for c in value):
            raise Blocked('Invalid authentication response')
        self._value = value

    def https_request(self, request):
        if self._value and request.get_method()=='GET' and request.full_url in {job[2] for job in PILOT}:
            request.add_unredirected_header('Authorization','Bearer '+self._value)
        return request

    def clear(self):
        self._value = ''


class LoginSession:
    def __init__(self, gate, opener=None):
        self.gate = gate
        self.opener = opener or urllib.request.build_opener(NoRedirect())
        self.last_request = 0

    def post(self, path, body):
        if path not in {'/login','/mfa/challenge','/mfa/verify'}:
            raise Blocked('Unsupported authentication operation')
        self.gate()
        time.sleep(max(0,5-(time.monotonic()-self.last_request)))
        self.last_request=time.monotonic()
        request=urllib.request.Request(API+path,data=json.dumps(body).encode('utf-8'),
            headers={'User-Agent':UA,'Content-Type':'application/json','Accept':'application/json','Accept-Encoding':'identity'},method='POST')
        with self.opener.open(request,timeout=60) as response:
            if response.status!=200 or response.geturl()!=API+path:
                raise Blocked('Unexpected login endpoint')
            if response.headers.get('Content-Encoding','identity').lower() not in ('identity',''):
                raise Blocked('Encoded login response unsupported')
            if response.headers.get('Content-Type','').split(';')[0].lower()!='application/json':
                raise Blocked('Login response is not JSON')
            raw=response.read(AUTH_LIMIT+1)
        if len(raw)>AUTH_LIMIT:
            raise Blocked('Oversized login response')
        value=json.loads(raw)
        if not isinstance(value,dict):
            raise Blocked('Invalid login response')
        return value

    def login(self, prompt=hidden_prompt):
        username=prompt('OpenReview email (hidden): ')
        password=prompt('OpenReview password (hidden): ')
        try:
            result=self.post('/login',{'id':username,'password':password,'expiresIn':3600})
        finally:
            username=password=None
        if result.get('mfaPending'):
            # TOTP/email OTP are documented; unsupported passkey/challenge is a stop.
            methods=result.get('mfaMethods',[])
            method='totp' if 'totp' in methods else ('emailOtp' if 'emailOtp' in methods else None)
            if method is None:
                raise Blocked('MFA method needs a separately supported official flow')
            pending=result.get('mfaPendingToken')
            if not isinstance(pending,str) or len(pending)>16384:
                raise Blocked('Invalid MFA response')
            if method=='emailOtp':
                self.post('/mfa/challenge',{'mfaPendingToken':pending,'method':method})
            code=prompt(('Email verification' if method=='emailOtp' else 'Authenticator')+' code (hidden): ')
            try:
                result=self.post('/mfa/verify',{'mfaPendingToken':pending,'method':method,'code':code})
            finally:
                pending=code=None
        bearer=ScopedBearer(result.get('token'))
        result.clear()
        return bearer


def configured_budget(ledger):
    root=ledger.root
    policy=json.loads((root/'configs/project_policy.json').read_text(encoding='utf-8'))
    paths=json.loads((root/'configs/setup_paths.json').read_text(encoding='utf-8'))
    meter=ExternalAccounting(root,json.loads((root/'configs/storage_accounting.json').read_text(encoding='utf-8')))
    return Budget(ledger,policy,{**paths['used_paths'],**{'accounting_'+k:str(v) for k,v in meter.roots.items()}},meter)


def check_baseline(root):
    receipt=json.loads((root/'state/offline_acceptance.json').read_text(encoding='utf-8'))
    v=versions(root)
    if receipt.get('status')!='pass' or any(receipt.get(k)!=v[k] for k in ('code_hash','rules_hash')) or file_hash(root/receipt['test_report'])!=receipt['test_report_sha256']:
        raise Blocked('Run offline acceptance for the current code first')
    return v


def run(root, prompt=hidden_prompt, session_factory=LoginSession):
    root=Path(root).resolve(strict=True)
    v=check_baseline(root)
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    receipt_path=root/'exchange/sync_receipts'/('openreview_api_session_'+stamp+'.json')
    receipt={'at':stamp,'status':'awaiting_private_local_login','authentication':'not_run',
      'secret_persistence':False,'browser_credentials_accessed':False,'scope':'3 preselected papers, at most 4 PDF requests',
      'versions':v,'downloads':[],'paper_loops':0,'identity_version_reading':'separate_validation_required'}
    def gate():
        with Ledger(root) as ledger:
            check_baseline(root)
            return configured_budget(ledger).check(60_000_000)
    receipt['storage_before']=gate()
    atomic_json(receipt_path,receipt)
    bearer=None
    try:
        # No writer lock or running lease is held while the human enters credentials.
        bearer=session_factory(gate).login(prompt)
        receipt.update(status='authenticated_fetching',authentication='success')
        atomic_json(receipt_path,receipt)
        with Ledger(root) as ledger:
            budget=configured_budget(ledger)
            downloader=Downloader(budget)
            downloader.last_request=time.monotonic()
            downloader.opener=urllib.request.build_opener(NoRedirect(),bearer)
            for index,(paper,role,url) in enumerate(PILOT):
                check_baseline(root)
                task='P2_api_'+stamp+'_'+str(index+1)
                ledger.enqueue(task,'OR_'+paper,'acquisition',{'url':url,'role':role,'objective':'One authenticated guarded PDF acquisition; no paper-loop or version certification'},kind='real')
                existing=ledger.db.execute('SELECT * FROM sources WHERE paper=? AND role=? AND url=? AND status=?',('OR_'+paper,role,url,'available')).fetchone()
                if existing and existing['path'] and file_hash(root/existing['path'])==existing['sha256']:
                    item={'task_id':task,'url':url,'status':'existing_bytes_verified','source_id':existing['id'],'sha256':existing['sha256']}
                else:
                    try:
                        item={'task_id':task,**downloader.fetch(url,'OR_'+paper,role)}
                    except (Exception, KeyboardInterrupt) as exc:
                        item={'task_id':task,'url':url,**safe_failure(exc)}
                        ledger.block(task,'Authenticated acquisition stopped: '+item['error'])
                        receipt['downloads'].append(item)
                        receipt.update(status='blocked_after_login',failure=item)
                        atomic_json(receipt_path,receipt)
                        break
                receipt['downloads'].append(item)
                packet=ledger.claim(task)
                ledger.write_result(packet,{'claims':[],'novelty_label':'U','acquisition_receipt':item,
                  'scope':'bytes only; title, version and semantic reading remain separate','real_paper_loop_complete':False})
                ledger.accept(packet['attempt_id'])
                atomic_json(receipt_path,receipt)
            else:
                receipt['status']='bounded_download_plan_finished'
            receipt['storage_after']=budget.check(0)
            ledger.snapshot()
    except (Exception, KeyboardInterrupt) as exc:
        receipt.update(safe_failure(exc))
        if receipt['authentication']=='not_run':receipt['authentication']='not_completed'
    finally:
        if bearer is not None:bearer.clear()
        atomic_json(receipt_path,receipt)
        atomic_json(root/'exchange/sync_receipts/openreview_api_session_latest.json',receipt)
    return receipt,receipt_path


def main(root):
    parser=argparse.ArgumentParser(description='One private interactive API login; bounded 3-paper/4-PDF acquisition, no stored credentials or bulk corpus.')
    parser.add_argument('--run',action='store_true',help='Prompt in your own console for hidden credentials, then execute the fixed pilot')
    parser.add_argument('--plan',action='store_true',help='Show the fixed nonsecret URL plan; no network or login')
    args=parser.parse_args()
    if not args.run:
        print(json.dumps({'papers':3,'maximum_pdf_requests':4,'jobs':[{'paper':p,'role':r,'url':u} for p,r,u in PILOT],'login':'private_console_only','live_authentication_tested':False},ensure_ascii=False,indent=2))
        return 0
    try:
        receipt,path=run(root)
        print(json.dumps({'status':receipt['status'],'authentication':receipt['authentication'],'pdf_results':len(receipt['downloads']),'receipt':str(path)},ensure_ascii=False,indent=2))
        return 0 if receipt['status']=='bounded_download_plan_finished' else 2
    except (Exception,KeyboardInterrupt) as exc:
        print(json.dumps(safe_failure(exc)))
        return 2
