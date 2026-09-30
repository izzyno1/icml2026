"""Allowlisted development-storage accounting using metadata only, never file reads."""
from pathlib import Path
import os
import stat
from datetime import datetime, timezone
from .core import Blocked


def metadata_bytes(path, max_entries=250_000, allow_internal_aliases=False):
    path = Path(path)
    if not path.is_absolute():
        raise Blocked('Accounting root must be absolute')
    total = visited = files = aliases = 0
    try:
        root_info = path.lstat()
        pending = [(path, root_info)]
        while pending:
            current, info = pending.pop()
            visited += 1
            if visited > max_entries:
                raise Blocked('Accounting entry limit exceeded')
            if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
                # A version alias within the same scanned tree adds no new data.
                # Never follow it or scan a target outside the explicit inventory.
                if allow_internal_aliases and current != path:
                    target = current.resolve(strict=True)
                    if target.is_relative_to(path) and target != current:
                        aliases += 1
                        continue
                raise Blocked('Accounting cannot follow external/unknown reparse points')
            if stat.S_ISDIR(info.st_mode):
                with os.scandir(current) as entries:
                    pending.extend((Path(e.path), e.stat(follow_symlinks=False)) for e in entries)
            elif stat.S_ISREG(info.st_mode):
                total += info.st_size
                files += 1
            else:
                raise Blocked('Unaccounted special file')
    except OSError as exc:
        # Do not expose individual state/credential filenames in diagnostics.
        raise Blocked('Accounting metadata scan incomplete: '+type(exc).__name__) from None
    return {'logical_bytes': total, 'files': files, 'entries': visited, 'internal_aliases_not_double_counted': aliases}


class ExternalAccounting:
    def __init__(self, root, config):
        if config.get('mode') != 'live_metadata_allowlist' or not config.get('external_roots'):
            raise Blocked('Live external storage inventory is required')
        self.roots = {k: Path(v) for k, v in config['external_roots'].items()}
        project = Path(root).absolute()
        checked = []
        for path in self.roots.values():
            if not path.is_absolute() or path == Path(path.anchor):
                raise Blocked('Accounting needs dedicated absolute development paths')
            if path.is_relative_to(project) or project.is_relative_to(path):
                raise Blocked('External accounting overlaps the project')
            if any(path.is_relative_to(p) or p.is_relative_to(path) for p in checked):
                raise Blocked('External accounting roots overlap')
            checked.append(path)
        self.last = None

    def __call__(self):
        observed = {}
        for role, path in self.roots.items():
            try:
                observed[role] = metadata_bytes(path, allow_internal_aliases=True)
            except Blocked as exc:
                raise Blocked(f'External storage role {role}: {exc}') from None
        total = sum(item['logical_bytes'] for item in observed.values())
        self.last = {'at': datetime.now(timezone.utc).isoformat(),
                     'status': 'pass', 'external_attributable_bytes_upper_bound': total,
                     'roots': observed, 'content_reads': 0,
                     'method': 'Entire allowlisted shared development directories; logical metadata only'}
        return total
