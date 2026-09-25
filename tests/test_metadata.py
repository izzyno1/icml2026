"""The catalog uses the same fail-closed storage path as PDF retrieval."""
import io, json
from unittest.mock import patch
from test_workflow import Base
from icml_audit.core import Blocked
from icml_audit.storage import Budget, Downloader, recover_downloads

class MetadataTests(Base):
    def setUp(self):
        super().setUp()
        policy=json.loads((self.root/'configs/project_policy.json').read_text())
        self.budget=Budget(self.ledger,policy,{'project':str(self.root)},0,
                           free=lambda _:100_000_000_000,size=lambda:1_000_000)
        self.down=Downloader(self.budget)
    def stream(self,raw=b'{"notes":[]}',mime='application/json',maximum=1000):
        response=io.BytesIO(raw);response.headers={'Content-Type':mime}
        return self.down.store_stream(response,'https://api2.openreview.net/notes',
                                      'catalog','official_catalog',maximum,media='metadata')
    def test_small_json_is_registered_as_unread_raw_bytes(self):
        item=self.stream()
        self.assertTrue(item['path'].endswith('.txt'))
        self.assertEqual((self.root/item['path']).read_bytes(),b'{"notes":[]}')
        self.assertEqual(item['status'],'available_not_read')
    def test_html_is_evidence_not_executed(self):
        raw=b'<html><script>throw 1</script>catalog</html>'
        item=self.stream(raw,'text/html; charset=utf-8')
        self.assertEqual((self.root/item['path']).read_bytes(),raw)
    def test_invalid_json_binary_mime_and_cap_rejected(self):
        for raw,mime,maximum in [(b'{','application/json',1000),
                                 (b'abc','application/octet-stream',1000),
                                 (b'\x00','text/plain',1000),
                                 (b'x'*1001,'text/plain',1000),
                                 (b'{}','application/json',1_000_001)]:
            with self.assertRaises((Blocked,ValueError)):
                self.stream(raw,mime,maximum)
        self.assertEqual(self.ledger.db.execute('SELECT count(*) FROM sources').fetchone()[0],0)
    def test_low_disk_prevents_any_socket(self):
        self.budget.free=lambda _:29_000_000_000
        with patch.object(self.down.opener,'open') as socket:
            with self.assertRaises(Blocked):
                self.down.fetch('https://api2.openreview.net/notes','catalog','official_catalog',media='metadata')
            socket.assert_not_called()
    def test_metadata_recovers_after_bytes_saved_before_registration(self):
        with patch.object(self.ledger,'source',side_effect=RuntimeError('interrupted')):
            with self.assertRaises(RuntimeError):self.stream()
        outcome=recover_downloads(self.ledger)
        self.assertEqual(outcome[0]['action'],'source_registered')
        self.assertEqual(self.ledger.db.execute('SELECT count(*) FROM sources').fetchone()[0],1)
