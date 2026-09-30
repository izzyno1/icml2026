from pathlib import Path
import hashlib
import json
import sys
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import doctor
import verify_bundle

class ProbeTests(unittest.TestCase):
    def policy(self):
        return {'storage': {'project_soft_budget_gb': 40, 'project_hard_budget_gb': 50,
                            'min_free_per_used_volume_gb': 30}}
    def test_sizes(self):
        with tempfile.TemporaryDirectory() as t:
            r = Path(t); (r/'a').write_bytes(b'1234'); (r/'nested').mkdir()
            (r/'nested'/'utf8.txt').write_text('中文', encoding='utf-8')
            info = doctor.scan_project(r)
            self.assertEqual(info['logical_bytes'], 10)
            self.assertEqual(info['file_count'], 2)
            self.assertTrue(info['complete'])
    def test_entry_limit(self):
        with tempfile.TemporaryDirectory() as t:
            r=Path(t); (r/'a').touch(); (r/'b').touch()
            self.assertFalse(doctor.scan_project(r, 1)['complete'])
    def test_symlink_skipped(self):
        with tempfile.TemporaryDirectory() as t:
            r=Path(t); (r/'real').write_bytes(b'abc')
            try: (r/'alias').symlink_to(r/'real')
            except (OSError, NotImplementedError): self.skipTest('Symlink creation unavailable')
            x=doctor.scan_project(r)
            self.assertEqual(x['logical_bytes'],3);self.assertEqual(x['skipped_links'],1)
    def test_disallow_escape(self):
        with tempfile.TemporaryDirectory() as t:
            r=Path(t)
            with self.assertRaises(ValueError):doctor.within_root(r, r/'..'/'outside')
    def test_smoke_cleanup(self):
        with tempfile.TemporaryDirectory() as t:
            r=Path(t);(r/'existing').write_text('keep')
            x=doctor.smoke(r)
            self.assertEqual(x['sqlite_reopen'],'pass')
            self.assertEqual(list((r/'cache/setup_smoke').iterdir()),[])
            self.assertEqual((r/'existing').read_text(),'keep')
    def test_soft(self):
        x=doctor.storage_status(41*doctor.GB,[40*doctor.GB],self.policy())
        self.assertTrue(x['project_soft_reached']);self.assertFalse(x['pause_new_large_writes'])
    def test_hard(self):
        self.assertTrue(doctor.storage_status(50*doctor.GB,[40*doctor.GB],self.policy())['pause_new_large_writes'])
    def test_low_temp_space(self):
        self.assertTrue(doctor.storage_status(1,[100*doctor.GB,29*doctor.GB],self.policy())['pause_new_large_writes'])
    def test_report_no_overwrite(self):
        with tempfile.TemporaryDirectory() as t:
            r=Path(t);a=doctor.save_report(r,{'x':1});b=doctor.save_report(r,{'x':2})
            self.assertNotEqual(a,b);self.assertEqual(json.loads(a.read_text())['x'],1)
    def test_invalid_policy(self):
        p=self.policy();p['storage']['project_hard_budget_gb']=20
        with self.assertRaises(ValueError):doctor.storage_status(0,[doctor.GB],p)

class ManifestTests(unittest.TestCase):
    def manifest(self):
        return {'files':[{'path':'x.txt','bytes':3,'sha256':hashlib.sha256(b'abc').hexdigest()}]}
    def test_pass(self):
        with tempfile.TemporaryDirectory() as t:
            r=Path(t);(r/'x.txt').write_bytes(b'abc')
            self.assertTrue(verify_bundle.verify(r,self.manifest())['ok'])
    def test_change(self):
        with tempfile.TemporaryDirectory() as t:
            r=Path(t);(r/'x.txt').write_bytes(b'abd')
            self.assertEqual(verify_bundle.verify(r,self.manifest())['changed'],['x.txt'])
    def test_missing(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(verify_bundle.verify(Path(t),self.manifest())['missing'],['x.txt'])
    def test_escape(self):
        with tempfile.TemporaryDirectory() as t:
            m=self.manifest();m['files'][0]['path']='../x.txt'
            self.assertEqual(verify_bundle.verify(Path(t),m)['invalid_paths'],['../x.txt'])
    def test_duplicate(self):
        with tempfile.TemporaryDirectory() as t:
            r=Path(t);(r/'x.txt').write_bytes(b'abc');m=self.manifest();m['files']*=2
            self.assertEqual(verify_bundle.verify(r,m)['invalid_paths'],['x.txt'])
if __name__=='__main__':unittest.main()
