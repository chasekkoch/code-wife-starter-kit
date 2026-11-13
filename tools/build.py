"""
🛠️ Maintainer tool. The learner never needs this file.

Every exercise is written ONCE in tools/templates/, with solved and stubbed code side by side:

    # <<SOLVE            (or  // <<SOLVE 3.4   or  <!-- <<SOLVE 3.10 -->)
    ...solved code...
    # ==STUB
    ...starter code the learner sees...
    # >>END

This script renders the templates into:
    solutions/                          every block solved
    solutions/project3_aurora/step_X/   Project 3 snapshots: blocks up to step X solved
    exercises/                          every block stubbed  (ONLY with --exercises, because it
                                        would overwrite the learner's work!)

Tokens:  @@ROOT@@ -> folder to run from,  @@SOLVED@@ -> a "solved" label (empty in exercises)

    python tools/build.py               # rebuild solutions/
    python tools/build.py --exercises   # ALSO reset exercises/ (asks for confirmation)
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
TEMPLATES = ROOT / "tools" / "templates"
P3 = "project3_aurora"
P3_STEPS = ["3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8", "3.9", "3.10", "3.11", "3.12"]
BINARY_SUFFIXES = {".png", ".jpg", ".ico", ".mp3", ".wav"}

MARKER = re.compile(r"^\s*(?:#|//|<!--|/\*)\s*(<<SOLVE|==STUB|>>END)\s*([\d.]*)\s*(?:-->|\*/)?\s*$")


def step_key(step: str) -> tuple[int, ...]:
    return tuple(int(part) for part in step.split("."))


def render(text: str, is_solved) -> str:
    """is_solved(step_or_None) -> bool decides which half of each block to keep."""
    out, mode, keep = [], None, True
    for line_no, line in enumerate(text.splitlines(keepends=True), 1):
        match = MARKER.match(line)
        if not match:
            if mode is None or keep:
                out.append(line)
            continue
        kind, step = match.groups()
        if kind == "<<SOLVE":
            if mode is not None:
                raise ValueError(f"line {line_no}: nested <<SOLVE")
            mode, keep = "solve", is_solved(step or None)
        elif kind == "==STUB":
            if mode != "solve":
                raise ValueError(f"line {line_no}: ==STUB without <<SOLVE")
            mode, keep = "stub", not keep
        else:
            if mode is None:
                raise ValueError(f"line {line_no}: >>END without <<SOLVE")
            mode, keep = None, True
    if mode is not None:
        raise ValueError("unclosed <<SOLVE block")
    return "".join(out)


def write_tree(src: Path, dest: Path, is_solved, tokens: dict[str, str]):
    for path in sorted(src.rglob("*")):
        if path.is_dir() or "__pycache__" in path.parts:
            continue
        target = dest / path.relative_to(src)
        target.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix in BINARY_SUFFIXES:
            shutil.copyfile(path, target)
            continue
        try:
            text = render(path.read_text(encoding="utf-8-sig"), is_solved)
        except ValueError as err:
            sys.exit(f"❌ {path.relative_to(ROOT)}: {err}")
        for token, value in tokens.items():
            text = text.replace(token, value)
        target.write_text(text, encoding="utf-8", newline="\n")


def reset(folder: Path):
    if folder.exists():
        try:
            shutil.rmtree(folder)
        except PermissionError as err:
            sys.exit(f"❌ Couldn't clear {folder.relative_to(ROOT)}: a file is in use ({err.filename}).\n"
                     "   Stop any running Aurora server (Ctrl+C) and close terminals 'cd'-ed into it, then retry.")
    folder.mkdir(parents=True)


def build_solutions():
    out = ROOT / "solutions"
    reset(out)
    for project in sorted(TEMPLATES.iterdir()):
        if project.name == P3:
            continue
        write_tree(project, out / project.name, lambda step: True,
                   {"@@ROOT@@": "solutions", "@@SOLVED@@": "  ✅ SOLVED VERSION", "@@CHECK@@": " --solutions"})
    for step in P3_STEPS:
        def solved_through(block_step, current=step):
            return block_step is None or step_key(block_step) <= step_key(current)
        write_tree(TEMPLATES / P3, out / P3 / f"step_{step}", solved_through,
                   {"@@ROOT@@": f"solutions/{P3}/step_{step}", "@@SOLVED@@": f"  ✅ SOLVED THROUGH STEP {step}",
                    "@@CHECK@@": " --solutions"})
    print(f"✅ Built {out.relative_to(ROOT)}/ (including {len(P3_STEPS)} Project 3 snapshots)")


def build_exercises():
    out = ROOT / "exercises"
    reset(out)
    for project in sorted(TEMPLATES.iterdir()):
        root = f"exercises/{project.name}" if project.name == P3 else "exercises"
        write_tree(project, out / project.name, lambda step: False,
                   {"@@ROOT@@": root, "@@SOLVED@@": "", "@@CHECK@@": ""})
    print(f"✅ Built {out.relative_to(ROOT)}/")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exercises", action="store_true", help="also reset exercises/ (destroys learner edits!)")
    parser.add_argument("--yes", action="store_true", help="skip the confirmation prompt")
    args = parser.parse_args()

    build_solutions()
    if args.exercises:
        if not args.yes and input("⚠️  This ERASES all work in exercises/. Type 'reset' to continue: ") != "reset":
            print("Cancelled. exercises/ was not touched.")
            return
        build_exercises()


if __name__ == "__main__":
    main()
