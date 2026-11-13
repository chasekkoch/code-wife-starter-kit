"""
═══════════════════════════════════════════════════════════════════════
  EXERCISE 2.3 — The Cat Café 🐈☕  ✅ SOLVED VERSION
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Build your own kind of THING with a CLASS. A class is a blueprint;
    each cat made from it remembers its OWN name, mood and hunger, and
    knows how to do cat things (those are called METHODS). Then run the
    café and try to make every cat happy at the same time!

🧰 YOUR TOOLBELT
    • A class is a blueprint. @dataclass writes the boring setup for us:
          @dataclass
          class Dumpling:
              filling: str
              steamed: bool = True      # a default value

          lunch = Dumpling("pork")      # make one from the blueprint
          lunch.filling                 # "pork"

    • Methods are functions that live inside a class. `self` means
      "this particular one":
          def steam(self):
              self.steamed = True

    • min(...) / max(...) keep numbers inside limits:
          min(100, 120)    # 100   <- great for "never go above 100"
          max(0, -5)       # 0     <- great for "never go below 0"

    • and / or combine True/False checks:
          sunny and warm   # True only if BOTH are True

▶️ RUN IT        python solutions/project2_puzzles/ex2_3_cat_cafe.py
✅ CHECK IT      python check.py 2.3 --solutions

💡 HINTS (only peek if you're stuck!)
    1. Look at time_passes() below. It's a finished example of a method!
    2. pet: self.mood = min(100, self.mood + 15)
    3. feed changes TWO things: hunger goes down by 30 (not below 0) and
       mood goes up by 5 (not above 100).
    4. is_happy should `return` a True/False comparison using `and`.
"""

import random
from dataclasses import dataclass

from rich.console import Console
from rich.table import Table


@dataclass
class Cat:
    name: str
    fur: str
    mood: int = 50     # 0 = grumpy, 100 = purring
    hunger: int = 50   # 0 = full,   100 = STARVING (allegedly)

    def time_passes(self):
        """✅ Already done. An example method: cats get hungrier and a bit grumpier."""
        self.hunger = min(100, self.hunger + 5)
        self.mood = max(0, self.mood - 5)

    # ─────────────────────────────────────────────────────────────────
    # ✏️ TODO 1: Petting raises mood by 15, but never above 100.
    # ─────────────────────────────────────────────────────────────────
    def pet(self):
        self.mood = min(100, self.mood + 15)

    # ─────────────────────────────────────────────────────────────────
    # ✏️ TODO 2: Feeding lowers hunger by 30 (never below 0) AND raises
    #            mood by 5 (never above 100).
    # ─────────────────────────────────────────────────────────────────
    def feed(self):
        self.hunger = max(0, self.hunger - 30)
        self.mood = min(100, self.mood + 5)

    # ─────────────────────────────────────────────────────────────────
    # ✏️ TODO 3: A cat is happy when mood is 70 or more AND hunger is
    #            30 or less. Return True or False.
    # ─────────────────────────────────────────────────────────────────
    def is_happy(self):
        return self.mood >= 70 and self.hunger <= 30


# ═════════════════════════════════════════════════════════════════════
# ☕ The café. No changes needed below (but feel free to add a cat!).
# ═════════════════════════════════════════════════════════════════════
def bar(value, color):
    filled = value // 10
    return f"[{color}]{'█' * filled}[/{color}][dim]{'░' * (10 - filled)}[/dim] {value}"


def show(cats, console):
    table = Table(title="☕ The Cat Café ☕", border_style="yellow")
    for column in ("#", "Cat", "Mood", "Hunger", ""):
        table.add_column(column)
    for number, cat in enumerate(cats, start=1):
        table.add_row(str(number), f"{cat.name} [dim]({cat.fur})[/dim]", bar(cat.mood, "magenta"),
                      bar(cat.hunger, "red"), "😻" if cat.is_happy() else "😾")
    console.print(table)


if __name__ == "__main__":
    console = Console()
    cats = [
        Cat("Meredith Grey", "Scottish Fold", mood=random.randint(30, 60)),
        Cat("Olivia Benson", "Scottish Fold", hunger=random.randint(40, 70)),
        Cat("Benjamin Button", "Ragdoll"),
        Cat("Crookshanks", "ginger and very fluffy", mood=20),
    ]
    turns = 0
    while not all(cat.is_happy() for cat in cats):
        show(cats, console)
        command = input("Type p2 to pet cat 2, f1 to feed cat 1, or q to quit: ").strip().lower()
        if command == "q":
            break
        if len(command) == 2 and command[0] in "pf" and command[1].isdigit() and 1 <= int(command[1]) <= len(cats):
            cat = cats[int(command[1]) - 1]
            cat.pet() if command[0] == "p" else cat.feed()
            turns += 1
            if turns % 4 == 0:
                for other in cats:
                    other.time_passes()
                console.print("[dim]⏳ Time passes... everyone gets a little hungrier.[/dim]")
        else:
            console.print("[yellow]🤔 Try something like p1 or f3.[/yellow]")
    else:
        show(cats, console)
        console.print(f"\n[bold magenta]🎉 Every cat is purring! You did it in {turns} moves. 🎉[/bold magenta]")
