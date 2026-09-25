from pathlib import Path
import sys
import tempfile
import unittest
import os
import subprocess
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from icml_audit.accounting import ExternalAccounting,metadata_bytes
from icml_audit.core import Blocked


class AccountingTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(dir=ROOT/'cache/tmp')
        self.base=Path(self.temp.name)
        self.project=self.base/'project';self.project.mkdir()
        self.external=self.base/'external';self.external.mkdir()
    def tearDown(self):
        self.temp.cleanup()
    def meter(self,roots=None):
        return ExternalAccounting(self.project,{'mode':'live_metadata_allowlist','external_roots':roots or {'test':str(self.external)}})
    def test_metadata_only_and_live_growth(self):
        p=self.external/'synthetic.txt';p.write_bytes(b'abc')
        meter=self.meter()
        with patch('builtins.open',side_effect=AssertionError('no file content reads')),patch.object(Path,'open',side_effect=AssertionError('no file content reads')):
            self.assertEqual(meter(),3)
        p.write_bytes(b'abcdefgh')
        self.assertEqual(meter(),8)
    def test_missing_and_permission_errors_fail_closed(self):
        with self.assertRaises(Blocked):metadata_bytes(self.external/'missing')
        with patch('os.scandir',side_effect=PermissionError()):
            with self.assertRaises(Blocked):self.meter()()
    def test_overlapping_and_project_roots_rejected(self):
        for roots in ({'a':str(self.base)}, {'a':str(self.external),'b':str(self.external/'nested')}, {'a':str(self.project)}):
            with self.assertRaises(Blocked):self.meter(roots)
    def test_entry_limit(self):
        (self.external/'a').write_bytes(b'x')
        with self.assertRaises(Blocked):metadata_bytes(self.external,max_entries=1)
    def test_file_root(self):
        p=self.external/'bundle.zip';p.write_bytes(b'synthetic')
        self.assertEqual(self.meter({'bundle':str(p)})(),9)
    @unittest.skipUnless(os.name=='nt','Windows junction integration')
    def test_internal_junction_counted_once_external_target_blocked(self):
        target=self.external/'version';target.mkdir()
        (target/'synthetic.txt').write_bytes(b'abc')
        link=self.external/'latest'
        for destination, allowed in ((target,True),(self.project,False)):
            p=subprocess.run(['cmd.exe','/d','/c','mklink','/J',str(link),str(destination)],capture_output=True,timeout=10)
            self.assertEqual(p.returncode,0,'Junction fixture creation failed')
            try:
                if allowed:
                    self.assertEqual(self.meter()(),3)
                    with self.assertRaises(Blocked):metadata_bytes(self.external)
                else:
                    with self.assertRaises(Blocked):self.meter()()
            finally:
                # Remove only this fixture junction, never its target directory.
                self.assertEqual(link.parent,self.external)
                os.rmdir(link)


if __name__=='__main__':unittest.main()
