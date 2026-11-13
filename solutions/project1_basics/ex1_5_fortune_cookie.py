"""
═══════════════════════════════════════════════════════════════════════
  ⭐ BONUS EXERCISE 1.5 — Fortune Cookie Factory 🥠  ✅ SOLVED VERSION
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Use RANDOMNESS and a WHILE loop to build an endless fortune cookie
    machine, complete with lucky numbers.

🧰 YOUR TOOLBELT
    • import random   Borrow Python's dice-rolling toolbox.
          random.randint(1, 6)            # a random whole number from 1 to 6
          random.choice(["a", "b", "c"])  # a random item from a list

    • while loops     Keep repeating AS LONG AS something is True.
          count = 0
          while count < 3:
              count = count + 1

    • in / not in     Check if something is (or isn't) in a list.
          7 in [1, 7, 9]       # True
          7 not in [1, 7, 9]   # False

    • sorted(...)     Gives back a sorted copy of a list.
          sorted([3, 1, 2])    # [1, 2, 3]

▶️ RUN IT        python solutions/project1_basics/ex1_5_fortune_cookie.py
✅ CHECK IT      python check.py 1.5 --solutions

💡 HINTS (only peek if you're stuck!)
    1. pick_fortune is one line: return random.choice(FORTUNES)
    2. For lucky_numbers: keep looping WHILE the list is too short.
       Roll a number; only append it if it's NOT already in the list.
"""

import random

from rich.console import Console
from rich.panel import Panel

FORTUNES = [
    "A cat will choose you. Accept the honor.",
    "Your code will run on the first try. (Just this once.)",
    "The dumplings you seek are already in the fridge.",
    "A bug is just a feature you haven't met yet.",
    "You are someone's favorite era.",
    "Mischief managed. Now go to bed.",
    "Today you will learn something your past self couldn't do.",
    "Leftover lo mein tastes better at midnight.",
]


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 1: Return one random fortune from the FORTUNES list.
# ─────────────────────────────────────────────────────────────────────
def pick_fortune():
    return random.choice(FORTUNES)


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 2: Return `how_many` DIFFERENT random numbers between 1 and 49,
#            sorted from smallest to biggest.
#            lucky_numbers(3) might give [4, 17, 42]
# ─────────────────────────────────────────────────────────────────────
def lucky_numbers(how_many):
    numbers = []
    while len(numbers) < how_many:
        number = random.randint(1, 49)
        if number not in numbers:
            numbers.append(number)
    return sorted(numbers)


if __name__ == "__main__":
    console = Console()
    while True:
        answer = input("\n🥠 Press Enter to crack a cookie (or type q to quit): ")
        if answer.strip().lower() == "q":
            console.print("Bye! May your fortunes be ever accurate. 👋")
            break
        numbers = "  ".join(str(n) for n in lucky_numbers(6))
        console.print(Panel(f"[italic]{pick_fortune()}[/italic]\n\n🍀 Lucky numbers: [bold]{numbers}[/bold]",
                            border_style="yellow", expand=False))
