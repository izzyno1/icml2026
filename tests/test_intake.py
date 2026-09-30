"""User-supplied files cannot bypass budgets, task context or source uncertainty."""
import json
import os
from pathlib import Path
from unittest.mock import patch

from test_workflow import Base
from icml_audit.core import Blocked, file_hash
from icml_audit.intake import UNVERIFIED, _StableLocalStream, import_paper
from icml_audit.storage import Budget, recover_downloads


class IntakeTests(Base):
    def setUp(self):
        super().setUp()
        self.paper = 'OR_testForum'
        self.task_id = 'acquire_test'
        self.url = 'https://openreview.net/pdf?id=testForum'
        self.relative = 'exchange/manual_intake/current.pdf'
        self.file = self.root / self.relative
        self.file.parent.mkdir(parents=True)
        self.raw = b'%PDF-1.4\nsynthetic test bytes; no scientific evidence\n%%EOF\n'
        self.file.write_bytes(self.raw)
        self.ledger.enqueue(self.task_id, self.paper, 'acquisition', {}, kind='real')
        policy = json.loads((self.root/'configs/project_policy.json').read_text())
        self.budget = Budget(self.ledger, policy, {'project': str(self.root)}, 0,
                             free=lambda _: 100_000_000_000, size=lambda: 1_000_000)

    def receive(self, **kwargs):
        args = dict(budget=self.budget, task_id=self.task_id,
                    relative_file=self.relative, url=self.url)
        args.update(kwargs)
        return import_paper(**args)

    def count_sources(self):
        return self.ledger.db.execute('SELECT COUNT(*) FROM sources').fetchone()[0]

    def test_copy_is_unread_unverified_preserves_input_and_never_networks(self):
        with patch('urllib.request.OpenerDirector.open', side_effect=AssertionError('No network')):
            result = self.receive()
        self.assertEqual(self.file.read_bytes(), self.raw)
        self.assertEqual((self.root/result['path']).read_bytes(), self.raw)
        self.assertEqual(result['sha256'], file_hash(self.file))
        self.assertEqual(result['role'], UNVERIFIED)
        self.assertEqual(result['read_scope'], 'not_read')
        self.assertFalse(result['acquisition']['origin_verified'])
        self.assertFalse(result['acquisition']['version_verified'])
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM results').fetchone()[0], 0)

    def test_duplicate_copy_has_one_source_and_object(self):
        a, b = self.receive(), self.receive()
        self.assertEqual(a['source_id'], b['source_id'])
        self.assertEqual(self.count_sources(), 1)
        self.assertEqual(len(list((self.root/'data/objects').glob('*.pdf'))), 1)
        self.assertTrue(self.file.is_file())

    def test_original_declaration_does_not_verify_version(self):
        original = 'https://openreview.net/attachment?id=testForum&name=originally_submitted_PDF'
        result = self.receive(url=original, declared_role='original_submission')
        self.assertEqual(result['acquisition']['declared_role'], 'original_submission')
        self.assertEqual(result['role'], UNVERIFIED)

    def test_outside_paths_and_windows_alternate_stream_are_rejected(self):
        for path in ['../current.pdf', str(self.file), 'exchange/other/current.pdf',
                     'exchange/manual_intake/../current.pdf',
                     'exchange/manual_intake/nested/current.pdf',
                     'exchange/manual_intake/current.pdf:private.pdf']:
            with self.subTest(path=path), self.assertRaises(Blocked):
                self.receive(relative_file=path)
        self.assertEqual(self.count_sources(), 0)

    def test_hard_link_is_rejected(self):
        alias = self.file.with_name('alias.pdf')
        os.link(self.file, alias)
        with self.assertRaises(Blocked):
            self.receive()
        self.assertEqual(self.count_sources(), 0)

    def test_empty_non_pdf_and_oversize_files_are_not_registered(self):
        for raw in [b'', b'<html>login page</html>']:
            self.file.write_bytes(raw)
            with self.subTest(raw=raw), self.assertRaises(Blocked):
                self.receive()
        self.file.write_bytes(self.raw)
        self.budget.policy['network']['default_document_max_bytes'] = len(self.raw) - 1
        with self.assertRaises(Blocked):
            self.receive()
        self.assertEqual(self.count_sources(), 0)

    def test_low_space_blocks_before_input_read_or_copy(self):
        self.budget.free = lambda _: 29_000_000_000
        with patch.object(Path, 'open', side_effect=AssertionError('No content read')):
            # Context hashing needs read-only rule/code input first.
            with patch.object(self.ledger, 'check_context'):
                with self.assertRaises(Blocked):
                    self.receive()
        self.assertFalse((self.root/'data/objects').exists())

    def test_wrong_id_private_url_or_invented_version_rejected(self):
        for url, role in [('https://openreview.net/pdf?id=other', UNVERIFIED),
                          (self.url+'&token=secret', UNVERIFIED),
                          (self.url+'#fragment', UNVERIFIED),
                          (self.url.replace('https://', 'https://user@'), UNVERIFIED),
                          (self.url, 'camera_ready'),
                          ('https://pdfs.assets.alphaxiv.org/2605.30997v1.pdf', UNVERIFIED)]:
            with self.subTest(url=url, role=role), self.assertRaises(Blocked):
                self.receive(url=url, declared_role=role)
        self.assertEqual(self.ledger.db.execute('SELECT COUNT(*) FROM reservations').fetchone()[0], 0)

    def test_blocked_task_or_changed_context_rejected(self):
        self.ledger.block(self.task_id, 'prior task')
        with self.assertRaises(Blocked):
            self.receive()
        self.ledger.enqueue('fresh', self.paper, 'acquisition', {}, kind='real')
        (self.root/'src/icml_audit/context_changed.py').write_text('# changed')
        with self.assertRaises(Blocked):
            self.receive(task_id='fresh')
        self.assertEqual(self.count_sources(), 0)

    def test_same_size_mutation_is_rejected_before_publication(self):
        original_read = _StableLocalStream.read
        changed = False
        def read_then_change(stream, count):
            nonlocal changed
            data = original_read(stream, count)
            if data and not changed:
                changed = True
                with self.file.open('r+b') as writer:
                    writer.seek(10)
                    writer.write(b'X')
                info = self.file.stat()
                os.utime(self.file, ns=(info.st_atime_ns, info.st_mtime_ns + 10_000_000))
            return data
        with patch.object(_StableLocalStream, 'read', read_then_change):
            with self.assertRaises(Blocked):
                self.receive()
        self.assertEqual(self.count_sources(), 0)
        self.assertFalse((self.root/'data/objects').exists())

    def test_interruption_recovery_keeps_manual_provenance_and_unverified_role(self):
        with patch.object(self.ledger, 'source', side_effect=RuntimeError('interrupted')):
            with self.assertRaises(RuntimeError):
                self.receive()
        receipts = list((self.root/'cache/partials').glob('*.receipt.json'))
        self.assertEqual(len(receipts), 1)
        saved = json.loads(receipts[0].read_text())
        self.assertEqual(saved['acquisition']['method'], 'manual_local_copy')
        self.assertFalse(saved['acquisition']['origin_verified'])
        self.assertEqual(recover_downloads(self.ledger)[0]['action'], 'source_registered')
        self.assertEqual(recover_downloads(self.ledger), [])
        row = self.ledger.db.execute('SELECT * FROM sources').fetchone()
        self.assertEqual(row['role'], UNVERIFIED)
        self.assertEqual(row['read_scope'], 'not_read')
        self.assertTrue(self.file.is_file())
