"""Synthetic secrets and endpoints only; never authenticate in the test suite."""
import io
import json
import urllib.error
import urllib.request
from unittest.mock import Mock,patch
from test_workflow import Base,Stream
from icml_audit.core import Blocked,atomic_json,versions,file_hash
from icml_audit.openreview_session import API,PILOT,AUTH_LIMIT,ScopedBearer,LoginSession,safe_failure,hidden_prompt,run
from icml_audit.storage import Budget,Downloader

FAKE='SYNTHETIC_NOT_A_REAL_SESSION'

def response(value,path='/login',**headers):
    r=Stream(json.dumps(value).encode(),{'Content-Type':'application/json',**headers})
    r.status=200;r.geturl=lambda:API+path
    return r

class OpenReviewSessionTests(Base):
    def test_auth_only_exact_pdf_requests(self):
        auth=ScopedBearer(FAKE)
        for _,_,url in PILOT:
            request=auth.https_request(urllib.request.Request(url))
            self.assertEqual(request.get_header('Authorization'),'Bearer '+FAKE)
            self.assertIn('Authorization',request.unredirected_hdrs)
        for url in [API+'/robots.txt',API+'/notes?id=J4wRLmh29t',PILOT[0][2]+'&extra=1',
                    PILOT[0][2].replace('https:','http:'),PILOT[0][2].replace('api2.openreview.net','api2.openreview.net.evil.test')]:
            self.assertIsNone(auth.https_request(urllib.request.Request(url)).get_header('Authorization'))
        self.assertIsNone(auth.https_request(urllib.request.Request(PILOT[0][2],data=b'x')).get_header('Authorization'))

    def test_invalid_token_and_clear(self):
        for bad in ['',None,'a\r\nb','x'*16385,'non-ascii-中']:
            with self.subTest(bad=type(bad).__name__),self.assertRaises(Blocked):ScopedBearer(bad)
        auth=ScopedBearer(FAKE);auth.clear();self.assertEqual(auth._value,'')
        self.assertIsNone(auth.https_request(urllib.request.Request(PILOT[0][2])).get_header('Authorization'))
        self.assertNotIn(FAKE,repr(auth))

    def test_budget_denial_precedes_login_request(self):
        gate=Mock(side_effect=Blocked('space'))
        op=Mock()
        with self.assertRaises(Blocked):LoginSession(gate,op).post('/login',{})
        op.open.assert_not_called()

    def test_login_endpoint_credentials_not_persisted(self):
        op=Mock();op.open.return_value=response({'token':FAKE,'user':{'private':'never saved'}})
        prompt=Mock(side_effect=['synthetic-user','synthetic-password'])
        auth=LoginSession(Mock(),op).login(prompt)
        req=op.open.call_args.args[0]
        self.assertEqual(req.full_url,API+'/login')
        self.assertEqual(json.loads(req.data),{'id':'synthetic-user','password':'synthetic-password','expiresIn':3600})
        self.assertEqual(auth._value,FAKE)
        self.assertEqual(prompt.call_count,2)

    def test_noninteractive_input_is_rejected_without_getpass(self):
        with patch('icml_audit.openreview_session.sys.stdin.isatty',return_value=False),patch('icml_audit.openreview_session.getpass.getpass') as prompt:
            with self.assertRaises(Blocked):hidden_prompt('Hidden: ')
            prompt.assert_not_called()

    def test_login_cap_wrong_type_encoding_and_redirect_are_rejected(self):
        oversized=response({'padding':'x'*AUTH_LIMIT})
        wrong=response({'token':FAKE},**{'Content-Type':'text/html'})
        encoded=response({'token':FAKE},**{'Content-Encoding':'gzip'})
        redirect=response({'token':FAKE});redirect.geturl=lambda:'https://example.test/login'
        for value in [oversized,wrong,encoded,redirect,response([])]:
            with self.subTest(case=type(value).__name__),self.assertRaises(Blocked):
                op=Mock();op.open.return_value=value
                LoginSession(Mock(),op).post('/login',{})

    def test_auth_operation_is_restricted(self):
        op=Mock()
        with self.assertRaises(Blocked):LoginSession(Mock(),op).post('/messages',{})
        op.open.assert_not_called()

    def test_totp_flow_and_unsupported_mfa(self):
        client=LoginSession(Mock())
        with patch.object(client,'post',side_effect=[{'mfaPending':True,'mfaMethods':['totp'],'mfaPendingToken':'SYNTHETIC_PENDING'},{'token':FAKE}]) as call:
            auth=client.login(Mock(side_effect=['test-user','test-password','123456']))
            self.assertEqual(call.call_args.args[0],'/mfa/verify')
            self.assertEqual(auth._value,FAKE)
        with patch.object(client,'post',return_value={'mfaPending':True,'mfaMethods':['passkey']}) as call:
            with self.assertRaises(Blocked):client.login(Mock(side_effect=['test-user','test-password']))
            self.assertEqual(call.call_count,1)

    def test_failure_redaction_and_challenge_classification(self):
        error=urllib.error.HTTPError(API+'/pdf',403,FAKE,{'Set-Cookie':FAKE},io.BytesIO(json.dumps({'name':'ChallengeRequiredError','message':FAKE,'token':FAKE}).encode()))
        result=safe_failure(error)
        self.assertEqual(result['error'],'ChallengeRequiredError')
        self.assertNotIn(FAKE,json.dumps(result))
        self.assertNotIn(FAKE,json.dumps(safe_failure(RuntimeError(FAKE))))

    def test_email_otp_flow_uses_only_official_challenge(self):
        client=LoginSession(Mock())
        with patch.object(client,'post',side_effect=[{'mfaPending':True,'mfaMethods':['emailOtp'],'mfaPendingToken':'SYNTHETIC_PENDING'},{},{'token':FAKE}]) as call:
            client.login(Mock(side_effect=['test-user','test-password','123456']))
            self.assertEqual([c.args[0] for c in call.call_args_list],['/login','/mfa/challenge','/mfa/verify'])

    def test_plan_stays_three_papers_four_files(self):
        self.assertEqual(len(PILOT),4)
        self.assertEqual(len({p for p,_,_ in PILOT}),3)
        self.assertEqual(sum(r=='original_submission' for _,r,_ in PILOT),1)

    def test_login_wait_releases_ledger_and_failed_session_saves_no_secrets(self):
        # Build an explicitly synthetic current baseline and isolated accounting stub.
        (self.root/'reports').mkdir(exist_ok=True)
        report=self.root/'reports/tests.json';report.write_text('{}')
        atomic_json(self.root/'state/offline_acceptance.json',{'status':'pass',**versions(self.root),'test_report':'reports/tests.json','test_report_sha256':file_hash(report)})
        (self.root/'configs/setup_paths.json').write_text('{}')
        self.ledger.close();self.ledger=None
        fake_budget=Mock();fake_budget.check.return_value={'synthetic':True}
        def factory(gate):
            gate()
            class Session:
                def login(inner,prompt):
                    from icml_audit.core import Ledger
                    with Ledger(self.root):pass
                    raise RuntimeError(FAKE)
            return Session()
        with patch('icml_audit.openreview_session.configured_budget',return_value=fake_budget):
            result,path=run(self.root,prompt=Mock(),session_factory=factory)
        self.assertEqual(result['status'],'blocked')
        self.assertNotIn(FAKE,path.read_text())
        self.assertEqual(result['downloads'],[])

    def test_download_failure_stops_batch_and_redacts_receipt(self):
        (self.root/'reports').mkdir(exist_ok=True)
        report=self.root/'reports/tests.json';report.write_text('{}')
        atomic_json(self.root/'state/offline_acceptance.json',{'status':'pass',**versions(self.root),'test_report':'reports/tests.json','test_report_sha256':file_hash(report)})
        self.ledger.close();self.ledger=None
        def budget(ledger):
            return Budget(ledger,json.loads((self.root/'configs/project_policy.json').read_text()),{'project':str(self.root)},0,free=lambda _:100_000_000_000,size=lambda:1000)
        error=urllib.error.HTTPError(PILOT[0][2],403,FAKE,{},io.BytesIO(json.dumps({'name':'ChallengeRequiredError','message':FAKE}).encode()))
        session=Mock();session.login.return_value=ScopedBearer(FAKE)
        with patch('icml_audit.openreview_session.configured_budget',side_effect=budget),patch.object(Downloader,'fetch',side_effect=error) as fetch:
            result,path=run(self.root,session_factory=lambda gate:session)
        self.assertEqual(fetch.call_count,1)
        self.assertEqual(result['authentication'],'success')
        self.assertEqual(result['status'],'blocked_after_login')
        self.assertNotIn(FAKE,path.read_text())
        self.assertEqual(session.login.return_value._value,'')

    def test_new_entrypoints_are_version_bound(self):
        packet=self.task()
        self.ledger.write_result(packet,{'claims':[]})
        with (self.root/'tools/openreview_session.py').open('a') as f:f.write('\n# changed\n')
        with self.assertRaises(Blocked):self.ledger.accept(packet['attempt_id'])
