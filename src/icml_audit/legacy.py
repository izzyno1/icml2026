"""Reuse the reviewed V2 pure graph/estimation helpers without editing history."""
from pathlib import Path
import importlib.util

def load_helpers(root):
    path=Path(root)/'reference/v2/icml2026_genealogy_v2/audit_helpers.py'
    spec=importlib.util.spec_from_file_location('icml_historical_helpers',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
