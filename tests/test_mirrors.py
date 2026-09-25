"""Reviewed public mirrors retain version, robots, recovery and network gates."""
import io
import json
import urllib.error
from unittest.mock import patch
from test_workflow import Base, Stream
from icml_audit.core import Blocked
from icml_audit.storage import Budget, Downloader, validate_url, recover_downloads

URL = 'https://pdfs.assets.alphaxiv.org/2605.30997v1.pdf'


class MirrorTests(Base):
    def setUp(self):
        super().setUp()
        policy = json.loads((self.root/'configs/project_policy.json').read_text())
        budget = Budget(self.ledger, policy, {'project': str(self.root)}, 0,
                        free=lambda _: 100_000_000_000, size=lambda: 1_000_000)
        self.down = Downloader(budget)

    def test_exact_link_does_not_allow_other_paths_or_authentication(self):
        self.assertEqual(validate_url(URL), URL)
        for url in [URL.replace('v1.pdf', '.pdf'), URL.replace('v1', 'v2'),
                    URL+'?download=1', URL.replace('https:', 'http:'),
                    URL.replace('https://', 'https://user@'),
                    URL.replace('alphaxiv.org', 'alphaxiv.org.example.com')]:
            with self.subTest(url=url), self.assertRaises(Blocked):
                validate_url(url)

    def test_preprint_is_unread_and_idempotent_not_camera_ready(self):
        a = self.down.store_stream(Stream(b'%PDF-preprint'), URL, 'p', 'preprint', 100)
        b = self.down.store_stream(Stream(b'%PDF-preprint'), URL, 'p', 'preprint', 100)
        self.assertEqual(a['source_id'], b['source_id'])
        row = self.ledger.db.execute('SELECT * FROM sources').fetchone()
        self.assertEqual(row['role'], 'preprint')
        self.assertEqual(row['read_scope'], 'not_read')

    def test_invalid_role_rejected_before_reservation_or_network(self):
        with patch.object(self.down.opener, 'open') as network:
            with self.assertRaises(ValueError):
                self.down.fetch(URL, 'p', 'preprint_v1')
            network.assert_not_called()
        self.assertEqual(self.ledger.db.execute('SELECT count(*) FROM reservations').fetchone()[0], 0)

    def test_mirror_cannot_be_marked_as_official_version(self):
        for role in ['camera_ready', 'original_submission', 'revised', 'official_catalog']:
            with self.subTest(role=role), patch.object(self.down.opener, 'open') as network:
                with self.assertRaises(Blocked):
                    self.down.fetch(URL, 'p', role)
                network.assert_not_called()

    def test_robots_denial_never_requests_pdf(self):
        for denial in [io.BytesIO(b'User-agent: *\nDisallow: /\n'),
                       urllib.error.HTTPError(URL, 403, 'Forbidden', {}, None)]:
            with self.subTest(denial=type(denial).__name__), patch.object(self.down, 'wait'), \
                    patch.object(self.down.opener, 'open', side_effect=[denial]) as network:
                with self.assertRaises(Blocked):
                    self.down.fetch(URL, 'p', 'preprint')
                self.assertEqual(network.call_count, 1)
        self.assertEqual(self.ledger.db.execute('SELECT count(*) FROM sources').fetchone()[0], 0)

    def test_robots_404_uses_same_guarded_stream_and_no_redirect(self):
        pdf = Stream(b'%PDF-fixture', {'Content-Length': '12'})
        pdf.status = 200
        pdf.geturl = lambda: URL
        missing = urllib.error.HTTPError(URL, 404, 'Not found', {}, None)
        with patch.object(self.down, 'wait'), \
                patch.object(self.down.opener, 'open', side_effect=[missing, pdf]) as network:
            result = self.down.fetch(URL, 'p', 'preprint', 100)
        self.assertEqual(network.call_count, 2)
        self.assertEqual(result['role'], 'preprint')
        self.assertEqual(result['bytes'], 12)

    def test_recovery_keeps_preprint_role_and_exact_hash(self):
        with patch.object(self.ledger, 'source', side_effect=RuntimeError('interrupted')):
            with self.assertRaises(RuntimeError):
                self.down.store_stream(Stream(b'%PDF-preserve'), URL, 'p', 'preprint', 100)
        result = recover_downloads(self.ledger)
        self.assertEqual(result[0]['action'], 'source_registered')
        self.assertEqual(recover_downloads(self.ledger), [])
        row = self.ledger.db.execute('SELECT * FROM sources').fetchone()
        self.assertEqual(row['role'], 'preprint')
        self.assertEqual((self.root/row['path']).read_bytes(), b'%PDF-preserve')
