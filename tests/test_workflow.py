from pathlib import Path
import copy
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import Mock

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from icml_audit.core import Ledger,Blocked,atomic_json,confined,file_hash
from icml_audit.storage import Budget,Downloader,validate_url
from icml_audit.legacy import load_helpers


class Base(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='p1_',dir=ROOT/'cache/tmp')
        self.root=Path(self.temp.name)
        for name in ('AGENTS.md','PROJECT_SPEC.md','configs/project_policy.json','configs/rubric.json',
                     'tools/workflow.py','tools/openreview_session.py','Login-OpenReview-and-Fetch.cmd',
                     'reference/v2/icml2026_genealogy_v2/audit_helpers.py'):
            dst=self.root/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,dst)
        shutil.copytree(ROOT/'src',self.root/'src')
        self.ledger=Ledger(self.root)
    def tearDown(self):
        if self.ledger is not None:
            self.ledger.close()
        self.temp.cleanup()
    def task(self,name='t',sources=()):
        self.ledger.enqueue(name,name,'extract',{'text':'中文合成任务'},sources,kind='synthetic')
        return self.ledger.claim(name)
    def source(self,name='s',data=b'evidence'):
        p=self.root/(name+'.txt');p.write_bytes(data)
        return self.ledger.source(name,'prior_work','https://icml.cc/'+name,p.name)


class LedgerTests(Base):
    def test_entrypoint_change_blocks_old_result(self):
        packet=self.task();self.ledger.write_result(packet,{'claims':[]})
        with (self.root/'tools/workflow.py').open('a',encoding='utf-8') as f:
            f.write('\n# changed entrypoint\n')
        with self.assertRaises(Blocked):self.ledger.accept(packet['attempt_id'])
    def test_missing_entrypoint_blocks_enqueue(self):
        (self.root/'tools/workflow.py').unlink()
        with self.assertRaises(Blocked):self.task()
    def test_single_writer_lock(self):
        with self.assertRaises(Blocked):Ledger(self.root)
    def test_duplicate_enqueue_and_conflict(self):
        self.ledger.enqueue('t','p','extract',{},kind='synthetic')
        self.ledger.enqueue('t','p','extract',{},kind='synthetic')
        with self.assertRaises(Blocked):self.ledger.enqueue('t','p','extract',{'changed':True},kind='synthetic')
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM tasks').fetchone()[0],1)
    def test_idempotent_accept_and_unknown(self):
        packet=self.task();self.ledger.write_result(packet,{'claims':[],'novelty_label':'L3'})
        self.assertTrue(self.ledger.accept(packet['attempt_id']))
        self.assertFalse(self.ledger.accept(packet['attempt_id']))
        result=json.loads(self.ledger.db.execute('SELECT payload FROM results').fetchone()[0])
        self.assertEqual(result['novelty_label'],'U')
        self.assertFalse(result['human_adjudicated'])
        self.assertEqual(self.ledger.db.execute("SELECT COUNT(*) FROM events WHERE event='result_accepted'").fetchone()[0],1)
    def test_double_claim(self):
        self.task()
        with self.assertRaises(Blocked):self.ledger.claim('t')
    def test_expired_and_late_attempt(self):
        packet=self.task();self.ledger.db.execute('UPDATE attempts SET expires=0')
        self.ledger.recover();new=self.ledger.claim('t')
        self.ledger.write_result(packet,{'claims':[]})
        with self.assertRaises(Blocked):self.ledger.accept(packet['attempt_id'])
        self.assertNotEqual(packet['attempt_id'],new['attempt_id'])
    def test_expired_result_not_accepted(self):
        packet=self.task();self.ledger.write_result(packet,{'claims':[]});self.ledger.db.execute('UPDATE attempts SET expires=0')
        with self.assertRaises(Blocked):self.ledger.accept(packet['attempt_id'])
    def test_rule_conflict_blocks_recovery(self):
        p=self.task();self.ledger.write_result(p,{'claims':[]})
        (self.root/'AGENTS.md').write_text('new rule',encoding='utf-8')
        result=self.ledger.recover()
        self.assertEqual(result[0]['action'],'blocked')
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM results').fetchone()[0],0)
    def test_code_conflict(self):
        p=self.task();self.ledger.write_result(p,{'claims':[]})
        (self.root/'src/icml_audit/new.py').write_text('# changed',encoding='utf-8')
        with self.assertRaises(Blocked):self.ledger.accept(p['attempt_id'])
    def test_accepted_result_becomes_stale_on_changed_rules(self):
        p=self.task();self.ledger.write_result(p,{'claims':[]});self.ledger.accept(p['attempt_id'])
        (self.root/'PROJECT_SPEC.md').write_text('changed',encoding='utf-8')
        self.ledger.recover()
        self.assertEqual(self.ledger.db.execute('SELECT status FROM tasks').fetchone()[0],'stale')
    def test_source_hash_conflict(self):
        s=self.source();p=self.task(sources=[s]);self.ledger.write_result(p,{'claims':[]})
        (self.root/'s.txt').write_bytes(b'tampered')
        with self.assertRaises(Blocked):self.ledger.accept(p['attempt_id'])
    def test_source_change_only_related_tasks_stale(self):
        s=self.source();p=self.task('dependent',[s]);q=self.task('unrelated')
        for packet in (p,q):
            self.ledger.write_result(packet,{'claims':[]});self.ledger.accept(packet['attempt_id'])
        (self.root/'s_new.txt').write_bytes(b'new version')
        self.ledger.source('s','prior_work','https://icml.cc/s','s_new.txt')
        states={r['id']:r['status'] for r in self.ledger.db.execute('SELECT * FROM tasks')}
        self.assertEqual(states,{'dependent':'stale','unrelated':'accepted'})
        self.assertEqual((self.root/'s.txt').read_bytes(),b'evidence')
    def test_receipt_tamper(self):
        p=self.task();self.ledger.write_result(p,{'claims':[]})
        path=self.root/p['output'];path.write_bytes(path.read_bytes()+b' ')
        with self.assertRaises(Blocked):self.ledger.accept(p['attempt_id'])
    def test_metadata_is_not_read_evidence(self):
        sid=self.ledger.source('s','official_catalog','https://icml.cc/s')
        p=self.task(sources=[sid]);self.ledger.write_result(p,{'claims':[{'kind':'direct_evidence','text':'x','evidence':[{'source_id':sid,'locator':'p1','read_range':'p1'}]}]})
        with self.assertRaises(Blocked):self.ledger.accept(p['attempt_id'])
    def test_missing_locators_rejected(self):
        sid=self.source();p=self.task(sources=[sid]);self.ledger.write_result(p,{'claims':[{'kind':'direct_evidence','text':'x','evidence':[{'source_id':sid}]}]})
        with self.assertRaises(Blocked):self.ledger.accept(p['attempt_id'])
    def test_ten_paper_bound(self):
        for n in range(10):self.ledger.enqueue('t'+str(n),'p'+str(n),'extract',{})
        with self.assertRaises(Blocked):self.ledger.enqueue('t10','p10','extract',{})
    def test_paths_and_no_delete(self):
        with self.assertRaises(Blocked):confined(self.root,'../escape')
        sid=self.source()
        with self.assertRaises(Blocked):self.ledger.delete_source(sid)
        self.assertTrue((self.root/'s.txt').exists())
    def test_utf8_snapshot_derived_from_db(self):
        self.task();self.ledger.block('t','缺少原稿')
        self.ledger.snapshot()
        self.assertIn('缺少原稿',(self.root/'NOW.md').read_text(encoding='utf-8'))
        self.assertEqual(json.loads((self.root/'state/snapshot.json').read_text(encoding='utf-8'))['tasks'][0]['status'],'blocked')


class Stream(io.BytesIO):
    def __init__(self,data,headers=None,on_read=None):
        super().__init__(data);self.headers=headers or {};self.on_read=on_read
    def read(self,n=-1):
        if self.on_read:self.on_read()
        return super().read(n)


class StorageTests(Base):
    def setUp(self):
        super().setUp()
        self.policy=json.loads((self.root/'configs/project_policy.json').read_text(encoding='utf-8'))
    def budget(self,free=None,size=None,external=0,paths=None):
        return Budget(self.ledger,self.policy,paths or {'project':str(self.root)},external,free or (lambda _:100_000_000_000),size or (lambda:1_000_000))
    def fetch(self,stream,maximum=100,budget=None):
        return Downloader(budget or self.budget()).store_stream(stream,'https://icml.cc/test.pdf','p','camera_ready',maximum)
    def test_low_volume_blocks_before_network(self):
        budget=self.budget(free=lambda _:29_000_000_000)
        dl=Downloader(budget);dl.opener.open=Mock(side_effect=AssertionError('network must not run'))
        with self.assertRaises(Blocked):dl.fetch('https://icml.cc/test.pdf','p','camera_ready',100)
        dl.opener.open.assert_not_called()
    def test_external_unknown_not_zero(self):
        with self.assertRaises(Blocked):self.budget(external=None).check()
    def test_per_volume_override_requires_explicit_policy(self):
        paths={'project':str(self.root),'controller':'C:\\controller'}
        free=lambda volume:22_000_000_000 if volume.upper().startswith('C:') else 100_000_000_000
        with self.assertRaises(Blocked):self.budget(paths=paths,free=free).check()
        self.policy['storage']['min_free_by_volume_gb']={'C:\\':20}
        self.budget(paths=paths,free=free).check()
        low_c=lambda volume:19_000_000_000 if volume.upper().startswith('C:') else 100_000_000_000
        with self.assertRaises(Blocked):self.budget(paths=paths,free=low_c).check()
    def test_volume_override_keeps_project_floor(self):
        other_volume='D:\\' if self.root.anchor.upper()=='C:\\' else 'C:\\'
        self.policy['storage']['min_free_by_volume_gb']={other_volume:20}
        with self.assertRaises(Blocked):self.budget(free=lambda _:29_000_000_000).check()
    def test_invalid_volume_override_and_negative_extra(self):
        for volume,amount in [('C:\\nested',20),('C:',20),('C:\\',float('nan')),('C:\\',-1)]:
            self.policy['storage']['min_free_by_volume_gb']={volume:amount}
            with self.assertRaises(Blocked):self.budget().check()
        self.policy['storage'].pop('min_free_by_volume_gb')
        with self.assertRaises(Blocked):self.budget().check(-1)
    def test_external_usage_is_refreshed(self):
        values=iter([1_000_000,50_000_000_000])
        budget=self.budget(external=lambda:next(values))
        budget.check()
        with self.assertRaises(Blocked):budget.check()
    def test_soft_hard_and_reservation(self):
        self.assertTrue(self.budget(size=lambda:41_000_000_000).check()['warning_40GB'])
        with self.assertRaises(Blocked):self.budget(size=lambda:50_000_000_000).check()
        budget=self.budget(size=lambda:49_900_000_000)
        budget.reserve(40_000_000)
        with self.assertRaises(Blocked):budget.reserve(40_000_000)
    def test_unknown_length_cap(self):
        with self.assertRaises(Blocked):self.fetch(Stream(b'%PDF-'+b'x'*200),maximum=100)
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM sources').fetchone()[0],0)
        for path in (self.root/'cache/partials').glob('*.part'):self.assertLessEqual(path.stat().st_size,100)
    def test_lying_small_length(self):
        with self.assertRaises(Blocked):self.fetch(Stream(b'%PDF-hello',{'Content-Length':'2'}))
    def test_truncation(self):
        with self.assertRaises(Blocked):self.fetch(Stream(b'%PDF-hello',{'Content-Length':'50'}))
    def test_declared_oversize(self):
        stream=Stream(b'%PDF-hello',{'Content-Length':'1000000'})
        with self.assertRaises(Blocked):self.fetch(stream)
        self.assertEqual(stream.tell(),0)
    def test_html_rejected(self):
        with self.assertRaises(Blocked):self.fetch(Stream(b'<html>login required</html>'))
    def test_encoded_rejected(self):
        with self.assertRaises(Blocked):self.fetch(Stream(b'%PDF-',{'Content-Encoding':'gzip'}))
    def test_midstream_disk_drop(self):
        available=[100_000_000_000]
        stream=Stream(b'%PDF-'+b'x'*70000,on_read=lambda:available.__setitem__(0,29_000_000_000))
        with self.assertRaises(Blocked):self.fetch(stream,100000,self.budget(free=lambda _:available[0]))
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM sources').fetchone()[0],0)
    def test_sha_dedup_and_distinct_versions(self):
        first=self.fetch(Stream(b'%PDF-version1'));same=self.fetch(Stream(b'%PDF-version1'))
        newer=self.fetch(Stream(b'%PDF-version2'))
        self.assertEqual(first['source_id'],same['source_id'])
        self.assertNotEqual(first['source_id'],newer['source_id'])
        self.assertEqual(len(list((self.root/'data/objects').glob('*.pdf'))),2)
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM sources').fetchone()[0],2)
    def test_saved_blob_before_registration_recovered(self):
        original=self.ledger.source
        self.ledger.source=Mock(side_effect=RuntimeError('simulated crash window'))
        with self.assertRaises(RuntimeError):self.fetch(Stream(b'%PDF-durable'))
        self.ledger.source=original
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM sources').fetchone()[0],0)
        result=self.ledger.recover()
        self.assertEqual(result[0]['action'],'source_registered')
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM sources').fetchone()[0],1)
        saved=json.loads(next((self.root/'cache/partials').glob('*.receipt.json')).read_text(encoding='utf-8'))
        self.assertEqual(self.ledger.db.execute('SELECT retrieved FROM sources').fetchone()[0],saved['retrieved_at'])
    def test_url_policy(self):
        for url in ('http://icml.cc/x','https://127.0.0.1/x','https://user:pass@icml.cc/x','https://icml.cc:444/x'):
            with self.assertRaises((Blocked,ValueError)):validate_url(url)


class RecoveryTests(Base):
    def killed_worker(self,mode):
        self.ledger.close();self.ledger=None
        env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
        with (self.root/'worker.stderr').open('w',encoding='utf-8') as error:
            child=subprocess.Popen([sys.executable,'-B','-X','utf8',str(ROOT/'tests/crash_worker.py'),str(self.root),mode],env=env,stdout=subprocess.DEVNULL,stderr=error)
            try:
                deadline=time.monotonic()+10
                while not (self.root/'ready.json').exists() and child.poll() is None and time.monotonic()<deadline:time.sleep(.03)
                self.assertTrue((self.root/'ready.json').exists(),'worker did not reach durable crash point')
                child.kill();child.wait(timeout=5)
            finally:
                if child.poll() is None:child.kill();child.wait(timeout=5)
        self.assertNotEqual(child.returncode,0)
        if mode=='partial':time.sleep(.25)
        # A genuinely new OS process opens the SQLite DB and reconstructs state.
        resumed=subprocess.run([sys.executable,'-B','-X','utf8',str(ROOT/'tools/workflow.py'),'--root',str(self.root),'recover'],env=env,capture_output=True,text=True,encoding='utf-8',timeout=10)
        self.assertEqual(resumed.returncode,0,resumed.stderr+resumed.stdout)
        self.ledger=Ledger(self.root)
        self.assertEqual(self.ledger.db.execute('PRAGMA integrity_check').fetchone()[0],'ok')
    def test_kill_after_result_before_accept(self):
        self.killed_worker('result')
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM results').fetchone()[0],1)
        self.ledger.recover()
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM results').fetchone()[0],1)
    def test_kill_partial_and_retry(self):
        self.killed_worker('partial')
        self.assertEqual(self.ledger.db.execute('SELECT status FROM tasks').fetchone()[0],'pending')
        packet=self.ledger.claim('crash')
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM attempts').fetchone()[0],2)
    def test_kill_after_commit_before_snapshot(self):
        self.killed_worker('committed')
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM results').fetchone()[0],1)
        self.assertIn('accepted',(self.root/'NOW.md').read_text(encoding='utf-8'))


class LegacyTests(unittest.TestCase):
    def test_comparison_not_lineage(self):
        helpers=load_helpers(ROOT)
        graph={'nodes':[{'id':'a'},{'id':'b'}],'types':{'comparison':{'count_as_lineage':False}},'sources':{'s':{}},
               'edges':[{'id':'e','parent':'a','child':'b','type':'comparison','parent_source':{'source_id':'s','locator':'p1'},'child_source':{'source_id':'s','locator':'p2'}}]}
        self.assertEqual(helpers.descendants(graph,'a')['descendant_count'],0)
    def test_pilot_cannot_estimate_population(self):
        with self.assertRaises(ValueError):load_helpers(ROOT).identification_bounds({'population_role':'nonprobability_pilot'})


if __name__=='__main__':unittest.main()
