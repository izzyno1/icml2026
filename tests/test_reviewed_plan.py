"""Offline fixtures only: bounded plan/source and credential-scope regression checks."""
from pathlib import Path
import json,os,urllib.request
from unittest.mock import Mock,patch
from test_workflow import Base
from icml_audit.core import Ledger,Blocked,atomic_json,file_hash,versions
from icml_audit.reviewed_plan import API,load_reviewed_plan,validate_jobs
from icml_audit.openreview_session import ScopedBearer,run

class ReviewedPlanTests(Base):
    def plan(self):
        paper='SYNTHETIC1';url='https://openreview.net/forum?id='+paper
        meta=self.root/'meta.json'
        atomic_json(meta,{'url':url,'snapshot':'ICML 2026 spotlight; Accept (spotlight); /pdf?id='+paper+' /attachment?id='+paper+'&name=originally_submitted_PDF'})
        sid=self.ledger.source('OR_'+paper,'official_catalog',url,'meta.json')
        report=self.root/'reports/catalog.json'
        atomic_json(report,{'records':[{'forum_id':paper,'source_id':sid,'source_sha256':file_hash(meta)}]})
        sha=file_hash(report)
        self.ledger.enqueue('catalog','ICML2026','catalog',{'catalog_report_sha256':sha},[sid],kind='catalog')
        packet=self.ledger.claim('catalog');self.ledger.write_result(packet,{'claims':[]});self.ledger.accept(packet['attempt_id'])
        data={'schema_version':'p2-fixed-pilot-1','maximum_papers':10,'maximum_pdf_requests':20,'catalog_task_id':'catalog','catalog_report':'reports/catalog.json','catalog_report_sha256':sha,
              'jobs':[{'paper':paper,'role':'current_attachment_unverified_role','url':API+'/pdf?id='+paper,'metadata_source_id':sid,'metadata_sha256':file_hash(meta)}]}
        name='exchange/download_plans/test.json';atomic_json(self.root/name,data)
        return name,data

    def test_valid_plan_and_bearer_exact_scope(self):
        name,_=self.plan();plan=load_reviewed_plan(self.ledger,name)
        auth=ScopedBearer('SYNTHETIC');auth.set_jobs(plan['jobs'])
        url=plan['jobs'][0][2]
        self.assertEqual(auth.https_request(urllib.request.Request(url)).get_header('Authorization'),'Bearer SYNTHETIC')
        for bad in [url+'&extra=1',API+'/robots.txt',url.replace('https:','http:'),url.replace('api2.openreview.net','evil.test')]:
            self.assertIsNone(auth.https_request(urllib.request.Request(bad)).get_header('Authorization'))
        self.assertIsNone(auth.https_request(urllib.request.Request(url,data=b'x')).get_header('Authorization'))
        auth.clear();self.assertIsNone(auth.https_request(urllib.request.Request(url)).get_header('Authorization'))

    def test_bad_jobs_duplicate_roles_hosts_and_limits(self):
        good=('p','current_attachment_unverified_role',API+'/pdf?id=p')
        bads=[[],[good]*2,[('p','prior_work',good[2])],[('p','original_submission',good[2])],[('p','current_attachment_unverified_role',good[2]+'&x=1')],
              [(str(n),'current_attachment_unverified_role',API+'/pdf?id='+str(n)) for n in range(11)],
              [('p/x','current_attachment_unverified_role',API+'/pdf?id=p/x')]]
        for bad in bads:
            with self.subTest(bad=bad),self.assertRaises(Blocked):validate_jobs(bad)

    def test_stale_or_changed_source_and_catalog_hash(self):
        name,data=self.plan()
        (self.root/'meta.json').write_text('{}')
        with self.assertRaises(Blocked):load_reviewed_plan(self.ledger,name)

    def test_new_source_version_stales_catalog(self):
        name,data=self.plan();atomic_json(self.root/'newmeta.json',{'changed':True})
        self.ledger.source('OR_SYNTHETIC1','official_catalog','https://openreview.net/forum?id=SYNTHETIC1','newmeta.json')
        with self.assertRaises(Blocked):load_reviewed_plan(self.ledger,name)

    def test_report_tampering_or_unbound_identity_rejected(self):
        name,data=self.plan();(self.root/'reports/catalog.json').write_text('{}')
        with self.assertRaises(Blocked):load_reviewed_plan(self.ledger,name)

    def test_path_escape_and_hardlink_rejected(self):
        name,_=self.plan()
        for p in ['../test.json',str(self.root/name),'meta.json','exchange/download_plans/../test.json']:
            with self.subTest(path=p),self.assertRaises(Blocked):load_reviewed_plan(self.ledger,p)
        os.link(self.root/name,self.root/'exchange/download_plans/alias.json')
        with self.assertRaises(Blocked):load_reviewed_plan(self.ledger,'exchange/download_plans/alias.json')

    def test_plan_change_during_auth_sends_no_pdf(self):
        name,data=self.plan()
        report=self.root/'reports/tests.json';report.write_text('{}')
        atomic_json(self.root/'state/offline_acceptance.json',{'status':'pass',**versions(self.root),'test_report':'reports/tests.json','test_report_sha256':file_hash(report)})
        self.ledger.close();self.ledger=None
        auth=ScopedBearer('SYNTHETIC')
        def factory(gate):
            class Session:
                def login(inner,prompt):
                    (self.root/name).write_text('{}')
                    return auth
            return Session()
        budget=Mock();budget.check.return_value={'synthetic':True}
        with patch('icml_audit.openreview_session.configured_budget',return_value=budget),patch('icml_audit.openreview_session.Downloader') as download:
            receipt,path=run(self.root,session_factory=factory,reviewed_plan=name)
        download.return_value.fetch.assert_not_called()
        self.assertEqual(receipt['status'],'blocked');self.assertEqual(auth._value,'')
        self.assertNotIn('Bearer',path.read_text())

    def test_stale_code_rejects_plan_before_login(self):
        name,_=self.plan()
        (self.root/'tools/workflow.py').write_text('# changed')
        with self.assertRaises(Blocked):load_reviewed_plan(self.ledger,name)

    def test_priors_excluded_and_unknown_targets_still_bounded(self):
        for n in range(3):
            p='prior'+str(n);self.ledger.source(p,'prior_work','https://icml.cc/'+p)
            self.ledger.enqueue('r'+str(n),p,'acquire',{})
        for n in range(10):self.ledger.enqueue('m'+str(n),'main'+str(n),'acquire',{})
        with self.assertRaises(Blocked):self.ledger.enqueue('m10','main10','acquire',{})
        self.assertEqual(len(self.ledger.p2_target_papers()),10)
        with self.assertRaises(Blocked):self.ledger.source('prior0','current_attachment_unverified_role','https://icml.cc/promoted')

    def test_mixed_prior_and_target_counts_and_does_not_change_old_tasks(self):
        sid=self.source('mixed')
        self.ledger.source('mixed','official_catalog','https://icml.cc/catalog')
        self.ledger.enqueue('mixedtask','mixed','acquire',{})
        before=dict(self.ledger.db.execute('SELECT * FROM tasks WHERE id=?',('mixedtask',)).fetchone())
        self.assertIn('mixed',self.ledger.p2_target_papers())
        self.assertEqual(before,dict(self.ledger.db.execute('SELECT * FROM tasks WHERE id=?',('mixedtask',)).fetchone()))
