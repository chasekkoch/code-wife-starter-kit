"""
═══════════════════════════════════════════════════════════════════════
  EXERCISE 2.4 — The Spell Book 📖⚡  ✅ SOLVED VERSION
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Make your program REMEMBER things after it closes by saving to a
    FILE, and handle mistakes gracefully instead of crashing. Your spell
    book lives in data/spells.json. Cast spells, mistype them (the wand
    should fizzle, not explode!), and teach the book brand-new spells.

    🔮 Fun fact: JSON is exactly how the Aurora in Project 3 will save
       your favorite looks!

🧰 YOUR TOOLBELT
    • JSON is a text format that looks just like Python dictionaries.
          import json
          with open(path) as file:          # open the file...
              data = json.load(file)        # ...and turn JSON into a dict

          with open(path, "w") as file:     # "w" = write mode
              json.dump(data, file, indent=2)

    • try / except catches errors so your program can keep going:
          try:
              price = menu["unicorn noodles"]
          except KeyError:                  # KeyError = "no such key"
              price = 0

    • Cleaning up text:
          "  LuMoS ".strip().lower()        # "lumos"

▶️ RUN IT        python solutions/project2_puzzles/ex2_4_spell_book.py
✅ CHECK IT      python check.py 2.4 --solutions

💡 HINTS (only peek if you're stuck!)
    1. load_spells: put the `with open(...)` part inside `try:` and
       `return {}` inside `except FileNotFoundError:`.
    2. cast: clean the words first, then try spells[words]["effect"].
       If that raises KeyError, return the fizzle message.
    3. save_spells: the "w" in open(path, "w") is the key ingredient!
"""

import json
from pathlib import Path

from rich.console import Console

SPELL_FILE = Path(__file__).parent / "data" / "spells.json"
FIZZLE = "💨 The wand fizzles... nothing happens."


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 1: Read the JSON file at `path` and return the dictionary.
#            If the file doesn't exist, return an empty dictionary {}.
# ─────────────────────────────────────────────────────────────────────
def load_spells(path):
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 2: Return the effect of the spell. Ignore extra spaces and
#            CAPITAL letters. Unknown spell? Return FIZZLE.
#            cast(spells, "  LUMOS ") -> "The tip of your wand glows..."
# ─────────────────────────────────────────────────────────────────────
def cast(spells, words):
    words = words.strip().lower()
    try:
        return spells[words]["effect"]
    except KeyError:
        return FIZZLE


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 3: Save the `spells` dictionary to `path` as JSON.
# ─────────────────────────────────────────────────────────────────────
def save_spells(path, spells):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(spells, file, indent=2)


# ═════════════════════════════════════════════════════════════════════
# 📖 The spell book app. No changes needed below!
# ═════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    console = Console()
    spells = load_spells(SPELL_FILE)
    if spells is None:
        console.print("[yellow]📕 The book is sealed shut... finish TODO 1 (load_spells) to open it![/yellow]")
        spells = {}
    console.print(f"[bold]📖 Your spell book knows {len(spells)} spells.[/bold]")
    console.print("Type a spell to cast it, [cyan]list[/cyan] to see them all, "
                  "[cyan]learn[/cyan] to add one, or [cyan]q[/cyan] to quit.\n")
    while True:
        words = input("🪄 > ").strip()
        if words.lower() == "q":
            console.print("Mischief managed. 🌙")
            break
        elif words.lower() == "list":
            for name in sorted(spells):
                console.print(f"   • [{spells[name].get('color', 'white')}]{name}[/]")
        elif words.lower() == "learn":
            name = input("   New spell name: ").strip().lower()
            effect = input("   What does it do? ").strip()
            spells[name] = {"effect": effect, "color": "bright_magenta"}
            save_spells(SPELL_FILE, spells)
            console.print(f"   ✨ Learned [bold]{name}[/bold]! (Saved, so it's still there next time.)")
        elif words:
            effect = cast(spells, words) or "🤷 (Nothing yet... finish TODO 2, cast(), to bring spells to life!)"
            color = spells.get(words.lower(), {}).get("color", "white")
            console.print(f"   [{color}]{effect}[/]")
