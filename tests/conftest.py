"""
Shared helpers for the exercise checks.

Every test loads the learner's file straight from disk, so the same tests can check either
`exercises/` (the default) or `solutions/` (when CODE_KIT_TARGET=solutions).
"""

import importlib.util
import os
import sys
import uuid
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
P3_FINAL_STEP = "step_3.12"


def target_root() -> Path:
    return REPO_ROOT / os.environ.get("CODE_KIT_TARGET", "exercises")


def exercise_path(relative: str) -> Path:
    root = target_root()
    if root.name == "solutions" and relative.startswith("project3_aurora/"):
        step = os.environ.get("CODE_KIT_P3_STEP", P3_FINAL_STEP)
        relative = relative.replace("project3_aurora/", f"project3_aurora/{step}/", 1)
    return root / relative


def load_module(relative: str):
    """Import a learner file by path (fresh every time, so edits are always picked up)."""
    path = exercise_path(relative)
    if not path.exists():
        pytest.fail(f"Couldn't find {path}. Did the file get renamed or moved?", pytrace=False)

    # Let files import their neighbours (e.g. server/main.py imports generator.py).
    folder = str(path.parent)
    if folder not in sys.path:
        sys.path.insert(0, folder)
    for neighbour in path.parent.glob("*.py"):
        sys.modules.pop(neighbour.stem, None)

    spec = importlib.util.spec_from_file_location(f"kit_{path.stem}_{uuid.uuid4().hex}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def call(func, *args, **kwargs):
    """Call a learner function and give a friendly message if it isn't finished yet."""
    result = func(*args, **kwargs)
    if result is None:
        pytest.fail(
            f"{func.__name__}() gave back None. Did you finish the TODO and remember to `return` the answer?",
            pytrace=False,
        )
    return result
