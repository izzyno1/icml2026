"""Offline synthetic exchanges only. No claim of a real Pro conversation."""
import json
from pathlib import Path
import subprocess
import sys
import time
from unittest.mock import patch

from test_workflow import Base, ROOT
from icml_audit.core import Blocked, atomic_json
from icml_audit.exchange import Exchange
from icml_audit.storage import Budget


class ExchangeTests(Base):
    def setUp(self):
        super().setUp()
        policy=json.loads((self.root/'configs/project_policy.json').read_text())
        budget=Budget(self.ledger,policy,{'project':str(self.root)},0,
                      free=lambda _:100_000_000_000,size=lambda:1_000_000)
        self.ex=Exchange(self.ledger,budget)
        self.sid=self.source(data=b'# Synthetic evidence\nThe marker is BLUE.\n')
        self.ledger.enqueue('g0','synthetic','review',
            {'objective':'Report synthetic marker only','provided_ranges':{self.sid:['lines 1-2']}},
            [self.sid],kind='synthetic')
        self.ex.export('g0','r1')
        self.return_path=Path('exchange/inbox/return.json')
        self.value=json.loads((self.ex.bundle('r1')/'review.template.json').read_text())
        self.value.update(origin='local_simulation',visible_files=['materials/'+self.sid+'.txt'],
            read_sources=[{'source_id':self.sid,'ranges':['lines 1-2']}],
            claims=[{'claim_id':'c1','kind':'direct_evidence','text':'Marker is BLUE',
                'evidence':[{'source_id':self.sid,'locator':'lines 1-2'}],
                'prior_comparison':'Synthetic; no prior work','conditions':'Synthetic only',
                'uncertainty':'No real paper conclusion','suggested_label':'U'}])
        self.save()

    def save(self):
        atomic_json(self.root/self.return_path,self.value)

    def receive(self):
        return self.ex.import_return('r1',self.return_path)

    def test_wait_has_no_running_lease_and_format_is_not_fact(self):
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM attempts').fetchone()[0],0)
        self.assertEqual(self.ex.row('r1')['status'],'waiting_external')
        result=self.receive()
        self.assertTrue(result['new_reception'])
        self.assertEqual(result['fact_validation'],'not_run')
        self.assertEqual(result['human_audit'],'not_run')
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM results').fetchone()[0],0)
        self.assertEqual(self.ledger.db.execute('SELECT status FROM tasks').fetchone()[0],'awaiting_fact_check')

    def test_duplicate_is_idempotent_conflicting_draft_rejected(self):
        self.receive()
        self.assertFalse(self.receive()['new_reception'])
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM pro_attempts').fetchone()[0],1)
        self.value['claims'][0]['text']='Changed';self.save()
        with self.assertRaises(Blocked):self.receive()

    def test_export_idempotent_round_conflict(self):
        self.ex.export('g0','r1')
        with self.assertRaises(Blocked):self.ex.export('g0','r1','independent_ai_review')

    def test_corrupt_package_hash(self):
        (self.ex.bundle('r1')/'TASK.md').write_text('tampered')
        with self.assertRaises(Blocked):self.receive()
        self.assertEqual(self.ex.row('r1')['status'],'stale')

    def test_return_old_binding_is_quarantined(self):
        self.value['binding']['code_hash']='old';self.save()
        with self.assertRaises(Blocked):self.receive()
        self.assertEqual(self.ex.row('r1')['status'],'waiting_external')
        self.assertEqual(len(list((self.root/'exchange/inbox/r1').glob('*.json'))),1)

    def test_stale_code(self):
        (self.root/'src/icml_audit/new.py').write_text('# changed')
        with self.assertRaises(Blocked):self.receive()

    def test_stale_rules(self):
        (self.root/'configs/rubric.json').write_text('{}')
        self.ledger.recover()
        self.assertEqual(self.ex.row('r1')['status'],'stale')

    def test_stale_source_bytes(self):
        (self.root/'s.txt').write_bytes(b'changed')
        with self.assertRaises(Blocked):self.receive()

    def test_source_version_changed(self):
        (self.root/'new.txt').write_text('new version')
        self.ledger.source('s','prior_work','https://icml.cc/s','new.txt')
        with self.assertRaises(Blocked):self.receive()

    def test_wrong_source_and_outside_locator(self):
        for key,value in [('source_id','wrong'),('locator','page 900')]:
            before=self.value['claims'][0]['evidence'][0][key]
            self.value['claims'][0]['evidence'][0][key]=value;self.save()
            with self.assertRaises(Blocked):self.receive()
            self.value['claims'][0]['evidence'][0][key]=before

    def test_empty_return_not_promoted(self):
        self.value['claims']=[];self.save()
        with self.assertRaises(Blocked):self.receive()

    def test_schema_failure_retry(self):
        self.value['claims'][0]['conditions']=None;self.save()
        with self.assertRaises(Blocked):self.receive()
        self.value['claims'][0]['conditions']='synthetic';self.save()
        self.assertTrue(self.receive()['new_reception'])

    def test_path_and_size_limits(self):
        for name in ('../return.json','configs/rubric.json'):
            with self.assertRaises(Blocked):self.ex.import_return('r1',name)
        (self.root/self.return_path).write_bytes(b'x'*1_000_001)
        with self.assertRaises(Blocked):self.receive()

    def test_budget_required(self):
        with self.assertRaises(Blocked):Exchange(self.ledger).import_return('r1',self.return_path)

    def test_low_disk_blocks_import_before_attempt(self):
        self.ex.budget.free=lambda _:29_000_000_000
        with self.assertRaises(Blocked):self.receive()
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM pro_attempts').fetchone()[0],0)

    def test_received_draft_corruption_is_detected_on_recovery(self):
        self.receive()
        saved=self.root/'exchange/inbox/r1'/(self.ex.row('r1')['return_hash']+'.json')
        saved.write_text('{}')
        self.ledger.recover()
        self.assertEqual(self.ex.row('r1')['status'],'stale')

    def test_orphan_export_retained_and_new_id_can_retry(self):
        self.ledger.enqueue('g2','synthetic','review',
            {'objective':'synthetic','provided_ranges':{self.sid:['lines 1-2']}},[self.sid],kind='synthetic')
        original=atomic_json
        def crash(path,obj):
            original(path,obj)
            if Path(path).name=='manifest.json':raise RuntimeError('before ledger commit')
        with patch('icml_audit.exchange.atomic_json',side_effect=crash):
            with self.assertRaises(RuntimeError):self.ex.export('g2','r2')
        self.ledger.recover()
        self.assertTrue((self.ex.bundle('r2')/'manifest.json').exists())
        with self.assertRaises(Blocked):self.ex.export('g2','r2')
        self.ex.export('g2','r3')
        self.assertEqual(self.ex.row('r3')['status'],'waiting_external')

    def test_real_task_cannot_use_uncommitted_baseline(self):
        self.ledger.enqueue('real','paper','review',
            {'objective':'real','provided_ranges':{self.sid:['lines 1-2']}},[self.sid],kind='real')
        with self.assertRaises((Blocked,OSError)):self.ex.export('real','real_review')

    def test_duplicate_json_keys_rejected(self):
        (self.root/self.return_path).write_text('{"binding":{},"binding":{}}')
        with self.assertRaises(Blocked):self.receive()

    def test_after_commit_before_receipt_recovers(self):
        with patch.object(self.ex,'receipt',side_effect=RuntimeError('crash after commit')):
            with self.assertRaises(RuntimeError):self.receive()
        self.ledger.recover()
        self.assertFalse(self.receive()['new_reception'])

    def test_kill_during_local_validation_then_new_process_recovery(self):
        self.ledger.close();self.ledger=None
        child=subprocess.Popen([sys.executable,'-B','-X','utf8',str(ROOT/'tests/exchange_crash_worker.py'),str(self.root)],
                               stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
        try:
            deadline=time.monotonic()+10
            while not (self.root/'ready.json').exists() and child.poll() is None and time.monotonic()<deadline:
                time.sleep(.03)
            self.assertTrue((self.root/'ready.json').exists())
            child.kill();child.wait(timeout=5)
        finally:
            if child.poll() is None:child.kill();child.wait(timeout=5)
            child.stderr.close()
        proc=subprocess.run([sys.executable,'-B','-X','utf8',str(ROOT/'tools/workflow.py'),'--root',str(self.root),'recover'],capture_output=True,timeout=10)
        self.assertEqual(proc.returncode,0,proc.stdout)
        from icml_audit.core import Ledger
        self.ledger=Ledger(self.root)
        policy=json.loads((self.root/'configs/project_policy.json').read_text())
        budget=Budget(self.ledger,policy,{'project':str(self.root)},0,free=lambda _:100_000_000_000,size=lambda:1_000_000)
        self.ex=Exchange(self.ledger,budget)
        self.assertEqual(self.ex.row('r1')['status'],'waiting_external')
        self.assertTrue(self.receive()['new_reception'])
        self.assertEqual(self.ledger.db.execute('PRAGMA integrity_check').fetchone()[0],'ok')
