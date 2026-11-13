"""
✅ The Starter Kit checker ✅

    python check.py            -> show your progress board for every exercise
    python check.py 1.2        -> check one exercise and get friendly hints
    python check.py 1          -> check every exercise in Project 1
    python check.py --solutions [...]   -> (coach) check the solved versions instead

You never need to edit this file. 🙂
"""

import argparse
import contextlib
import io
import os
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")  # emoji-safe output on Windows

try:
    import pytest
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
except ImportError:
    print("Oops! Some tools aren't installed yet.")
    print("Make sure your virtual environment is active, then run:  pip install -r requirements.txt")
    sys.exit(1)

console = Console()


@dataclass
class Exercise:
    number: str
    title: str
    file: str  # relative to exercises/ (or solutions/)
    test: str | None  # relative to tests/ ; None = checked in the browser
    bonus: bool = False


EXERCISES = [
    Exercise("1.1", "Hello, Birdie", "project1_basics/ex1_1_hello_birdie.py", "test_project1.py::TestHelloBirdie"),
    Exercise("1.2", "Takeout Bill Splitter", "project1_basics/ex1_2_bill_splitter.py", "test_project1.py::TestBillSplitter"),
    Exercise("1.3", "The Sorting Hat", "project1_basics/ex1_3_sorting_hat.py", "test_project1.py::TestSortingHat"),
    Exercise("1.4", "The Eras Spiral", "project1_basics/ex1_4_turtle_spiral.py", "test_project1.py::TestTurtleSpiral"),
    Exercise("1.5", "Fortune Cookie", "project1_basics/ex1_5_fortune_cookie.py", "test_project1.py::TestFortuneCookie", bonus=True),
    Exercise("1.6", "Cat Quilt", "project1_basics/ex1_6_cat_quilt.py", "test_project1.py::TestCatQuilt", bonus=True),
    Exercise("2.1", "Eras Tour Stats", "project2_puzzles/ex2_1_eras_stats.py", "test_project2.py::TestErasStats"),
    Exercise("2.2", "Takeout Menu Wizard", "project2_puzzles/ex2_2_menu_wizard.py", "test_project2.py::TestMenuWizard"),
    Exercise("2.3", "Cat Café", "project2_puzzles/ex2_3_cat_cafe.py", "test_project2.py::TestCatCafe"),
    Exercise("2.4", "Spell Book", "project2_puzzles/ex2_4_spell_book.py", "test_project2.py::TestSpellBook"),
    Exercise("2.5", "Palette Potion", "project2_puzzles/ex2_5_palette_potion.py", "test_project2.py::TestPalettePotion", bonus=True),
    Exercise("2.6", "Marauder's Map", "project2_puzzles/ex2_6_marauders_map.py", "test_project2.py::TestMaraudersMap", bonus=True),
    Exercise("3.1", "Make it yours (PARAMS)", "project3_aurora/web/params.js", None),
    Exercise("3.2", "A sky full of particles", "project3_aurora/web/sketch.js", None),
    Exercise("3.3", "The flow field", "project3_aurora/web/sketch.js", None),
    Exercise("3.4", "Color & glow", "project3_aurora/web/sketch.js", None),
    Exercise("3.5", "Make some music", "project3_aurora/web/sound.js", None),
    Exercise("3.6", "Let the wind play", "project3_aurora/web/sound.js", None),
    Exercise("3.7", "Settings menu", "project3_aurora/web/settings.js", None),
    Exercise("3.8", "Presets API", "project3_aurora/server/main.py", "test_project3.py::TestPresetsApi"),
    Exercise("3.9", "Surprise me generator", "project3_aurora/server/generator.py", "test_project3.py::TestGenerator"),
    Exercise("3.10", "Your own sliders", "project3_aurora/web/my_panel.js", None, bonus=True),
    Exercise("3.11", "Wand mode", "project3_aurora/web/sketch.js", None, bonus=True),
    Exercise("3.12", "Snapshots & shortcuts", "project3_aurora/web/sketch.js", None, bonus=True),
]


class ResultCollector:
    """A tiny pytest plugin that remembers what passed and what failed."""

    def __init__(self):
        self.passed = []
        self.failed = []  # (test name, friendly message, location)

    def pytest_runtest_logreport(self, report):
        name = report.nodeid.split("::")[-1].split("[")[0].replace("test_", "").replace("_", " ")
        if report.when == "call" and report.passed:
            self.passed.append(name)
        elif report.failed:
            self.failed.append((name, *_friendly_failure(report)))

    def pytest_collectreport(self, report):
        if report.failed:
            self.failed.append(("loading the tests", str(report.longrepr).strip().splitlines()[-1], ""))


def _friendly_failure(report):
    crash = getattr(report.longrepr, "reprcrash", None)
    if crash is None:
        return str(report.longrepr).strip().splitlines()[-1], ""
    message = crash.message.strip()
    message = message.removeprefix("Failed: ").removeprefix("AssertionError: ")
    if "\nassert " in message:  # drop pytest's internal "assert x == y" detail
        message = message.split("\nassert ")[0]
    location = ""
    if "exercises" in crash.path or "solutions" in crash.path:
        location = f"{Path(crash.path).relative_to(ROOT)}, line {crash.lineno}"
    return message, location


def run_tests(test: str) -> ResultCollector:
    collector = ResultCollector()
    quiet = io.StringIO()
    with contextlib.redirect_stdout(quiet), contextlib.redirect_stderr(quiet):
        pytest.main([str(ROOT / "tests" / test), "-q", "--no-header", "-p", "no:cacheprovider"], plugins=[collector])
    return collector


TYPO_TIPS = (
    "Common culprits: a missing [bold]:[/bold] at the end of a def/if/for line, a missing closing "
    "[bold])[/bold] or [bold]\"[/bold], or a line that isn't indented the same as its neighbours."
)


def syntax_problem(path: Path) -> str | None:
    """Return a friendly description of a typo that stops Python from reading the file at all."""
    try:
        compile(path.read_text(encoding="utf-8"), str(path), "exec")
    except SyntaxError as err:
        code = (err.text or "").rstrip()
        pointer = " " * max((err.offset or 1) - 1 - (len(err.text or "") - len((err.text or "").lstrip())), 0) + "^"
        return (f"🐛 Python couldn't read the file. There's a typo on [bold]line {err.lineno}[/bold]:\n\n"
                f"   [cyan]{code.strip()}[/cyan]\n   [red]{pointer}[/red]\n"
                f"   {err.msg}\n\n{TYPO_TIPS}")
    return None


def run_path(target: str, rel: str) -> str:
    """Where a file lives, e.g. solutions/project3_aurora/step_3.12/server/main.py for the final P3 snapshot."""
    if target == "solutions" and rel.startswith("project3_aurora/"):
        step = os.environ.get("CODE_KIT_P3_STEP", "step_3.12")
        rel = rel.replace("project3_aurora/", f"project3_aurora/{step}/", 1)
    return f"{target}/{rel}"


def browser_panel(exercises: list, target: str):
    steps = "\n".join(f"   {'⭐ ' if ex.bonus else '• '}{ex.number} {ex.title}" for ex in exercises)
    console.print(Panel(
        f"These steps are checked [bold]in the browser[/bold]! 🌌\n{steps}\n\n"
        f"1. Start the server:  [cyan]python {run_path(target, 'project3_aurora/server/main.py')}[/cyan]\n"
        f"2. Open [link]http://localhost:8000[/link] (it usually opens by itself)\n"
        f"3. Look at the ✅ checklist in the corner (press [bold]C[/bold] to show/hide it).",
        title="🌐 Check it in the browser", border_style="magenta"))


def check_one(ex: Exercise, target: str):
    title = f"{'⭐ Bonus ' if ex.bonus else ''}Exercise {ex.number}: {ex.title}"
    file_path = ROOT / run_path(target, ex.file)
    problem = syntax_problem(file_path) if file_path.exists() else None
    if problem:
        console.print(Panel(problem, title=title, border_style="red"))
        return

    result = run_tests(ex.test)
    if not result.failed:
        console.print(Panel(
            f"🎉 All {len(result.passed)} checks passed! Amazing work!\n\n"
            f"Run it to see it in action:\n   [cyan]python {run_path(target, ex.file)}[/cyan]",
            title=title, border_style="green"))
        return

    lines = []
    for name in dict.fromkeys(result.passed):
        count = result.passed.count(name)
        lines.append(f"[green]✅ {name}{f' (x{count})' if count > 1 else ''}[/green]")
    seen = set()
    for name, message, location in result.failed:
        if (name, message) in seen:
            continue
        seen.add((name, message))
        lines.append(f"[red]❌ {name}[/red]")
        lines.append(f"   💡 {message}")
        if location:
            lines.append(f"   📍 [dim]{location}[/dim]")
    lines.append("\n[italic]You've got this! Fix one ❌ at a time, save the file, and run the check again.[/italic]")
    console.print(Panel("\n".join(lines), title=title, border_style="yellow"))


def progress_board(target: str):
    table = Table(title="🌟 Your Progress Board 🌟", show_lines=False)
    table.add_column("#", justify="right")
    table.add_column("Exercise")
    table.add_column("Status")
    done = total = 0
    for ex in EXERCISES:
        name = f"{'⭐ ' if ex.bonus else ''}{ex.title}"
        if ex.test is None:
            status = "[magenta]🌐 check in the browser[/magenta]"
        elif (ROOT / run_path(target, ex.file)).exists() and syntax_problem(ROOT / run_path(target, ex.file)):
            status = "[red]🐛 has a typo (run the check for details)[/red]"
            total += not ex.bonus
        else:
            result = run_tests(ex.test)
            ok = not result.failed
            if not ex.bonus:
                total += 1
                done += ok
            if ok:
                status = "[green]✅ done![/green]"
            elif result.passed:
                status = f"[yellow]🚧 {len(result.passed)}/{len(result.passed) + len(result.failed)} checks[/yellow]"
            else:
                status = "[dim]⬜ not started[/dim]"
        table.add_row(ex.number, name, status)
    console.print(table)
    console.print(f"\n[bold]{done} of {total}[/bold] Python exercises complete (not counting ⭐ bonuses).")
    console.print("Check one exercise with:  [cyan]python check.py 1.1[/cyan]")


def main():
    parser = argparse.ArgumentParser(description="Check your exercises.")
    parser.add_argument("which", nargs="?", help="exercise number like 1.2, or a project number like 1")
    parser.add_argument("--solutions", action="store_true", help="check the solutions/ folder instead")
    args = parser.parse_args()

    target = "solutions" if args.solutions else "exercises"
    os.environ["CODE_KIT_TARGET"] = target

    if args.which is None:
        progress_board(target)
        return

    chosen = [ex for ex in EXERCISES if ex.number == args.which or ex.number.split(".")[0] == args.which]
    if not chosen:
        console.print(f"🤔 I don't know an exercise called [bold]{args.which}[/bold]. Try something like [cyan]1.1[/cyan].")
        sys.exit(1)
    in_browser = [ex for ex in chosen if ex.test is None]
    if in_browser:
        browser_panel(in_browser, target)
    for ex in chosen:
        if ex.test is not None:
            check_one(ex, target)


if __name__ == "__main__":
    main()
