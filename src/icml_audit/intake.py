"""Bounded, offline intake of one user-supplied OpenReview PDF.

The source URL and version are declarations, not verified provenance. Imported
bytes stay unread and have an unverified version role until a separate review.
"""
from pathlib import Path
import os
import stat

from .core import Blocked, confined, safe_id
from .storage import Downloader


UNVERIFIED = 'current_attachment_unverified_role'


def _fingerprint(info):
    # Windows stat/fstat may disagree on deprecated ctime semantics. Bind file
    # identity, bytes/mtime and link count; the copied bytes also receive SHA-256.
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_nlink)


class _StableLocalStream:
    def __init__(self, handle, path, root, relative, initial):
        self.handle, self.path = handle, path
        self.root, self.relative, self.initial = root, relative, initial
        self.headers = {'Content-Length': str(initial.st_size),
                        'Content-Type': 'application/pdf'}

    def read(self, count):
        chunk = self.handle.read(count)
        if not chunk:
            # This runs before store_stream publishes the object or its receipt.
            current_path = confined(self.root, self.relative)
            if (current_path != self.path or
                    _fingerprint(os.fstat(self.handle.fileno())) != _fingerprint(self.initial) or
                    _fingerprint(current_path.stat()) != _fingerprint(self.initial)):
                raise Blocked('Intake file changed during copying')
        return chunk


def import_paper(budget, task_id, relative_file, url, declared_role=UNVERIFIED):
    """No sockets, no private-directory scan, no deletion of the supplied file."""
    ledger, root = budget.ledger, budget.root
    task = ledger.db.execute('SELECT * FROM tasks WHERE id=?', (task_id,)).fetchone()
    if not task or task['kind'] != 'real' or task['stage'] != 'acquisition' or task['status'] != 'pending':
        raise Blocked('Manual intake needs a pending real acquisition task')
    ledger.check_context(task)
    paper = task['paper']
    if not paper.startswith('OR_'):
        raise Blocked('This minimal intake supports explicit OR_<forum_id> papers only')
    forum = paper[3:]
    safe_id(forum)
    expected = {
        UNVERIFIED: f'https://openreview.net/pdf?id={forum}',
        'original_submission': f'https://openreview.net/attachment?id={forum}&name=originally_submitted_PDF',
    }
    if declared_role not in expected or url != expected[declared_role]:
        raise Blocked('Declared source URL/version does not match this OpenReview paper')
    relative = Path(relative_file)
    if (relative.is_absolute() or len(relative.parts) != 3 or
            relative.parts[:2] != ('exchange', 'manual_intake') or
            relative.suffix.lower() != '.pdf' or ':' in relative.name):
        raise Blocked('Use one PDF directly inside project-relative exchange/manual_intake/')
    path = confined(root, relative)
    info = path.stat()
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        raise Blocked('Intake must be a regular file, without hard links or reparse points')
    maximum = budget.policy['network']['default_document_max_bytes']
    if not 5 <= info.st_size <= maximum:
        raise Blocked('Intake PDF is empty or exceeds the document byte limit')
    budget.check(info.st_size)
    provenance = {
        'method': 'manual_local_copy', 'task_id': task_id,
        'input_path': relative.as_posix(), 'declared_role': declared_role,
        'origin_verified': False, 'version_verified': False,
        'external_download_at': None, 'network_requests': 0,
        'limits_scope': 'Local ingestion only; external manual download was not managed by this program',
    }
    with path.open('rb') as handle:
        opened = os.fstat(handle.fileno())
        if _fingerprint(opened) != _fingerprint(info):
            raise Blocked('Intake file changed before opening')
        stream = _StableLocalStream(handle, path, root, relative, opened)
        result = Downloader(budget).store_stream(
            stream, url, paper, UNVERIFIED, info.st_size, provenance=provenance)
    ledger.event('manual_pdf_imported_unverified', {
        'task': task_id, 'source_id': result['source_id'],
        'reservation': result['reservation'], 'sha256': result['sha256'],
        'provenance': provenance,
    })
    return result
