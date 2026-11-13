"""
═══════════════════════════════════════════════════════════════════════
  EXERCISE 1.3 — The Sorting Hat 🎩⚡@@SOLVED@@
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Teach the computer to make DECISIONS. You'll write the brain of a
    Sorting Hat quiz: one function picks the house with the most points,
    and another picks the house's color. Then take the quiz yourself
    and see where you land!

🧰 YOUR TOOLBELT
    • Comparisons give back True or False (called BOOLEANS):
          5 > 3          # True
          "cat" == "dog" # False   (== means "is equal to")

    • if / elif / else lets your code choose a path:
          if weather == "rain":
              return "umbrella"
          elif weather == "sun":
              return "sunglasses"
          else:
              return "jacket"

    • max(...) gives back the biggest number:
          max(3, 9, 4)   # 9

▶️ RUN IT        python @@ROOT@@/project1_basics/ex1_3_sorting_hat.py
✅ CHECK IT      python check.py 1.3@@CHECK@@

💡 HINTS (only peek if you're stuck!)
    1. Notice the colon : at the end of every if/elif/else line.
    2. For pick_house, first find the winning score:
           best = max(gryffindor, hufflepuff, ravenclaw, slytherin)
       then ask "is gryffindor's score the best?" and so on.
    3. House names need to match EXACTLY, including capital letters.
"""

from rich.console import Console
from rich.panel import Panel


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 1: Return the color for each house:
#              "Gryffindor" -> "red"      "Hufflepuff" -> "yellow"
#              "Ravenclaw"  -> "blue"     "Slytherin"  -> "green"
#            Anything else -> "white"
# ─────────────────────────────────────────────────────────────────────
def house_color(house):
    # <<SOLVE
    if house == "Gryffindor":
        return "red"
    elif house == "Hufflepuff":
        return "yellow"
    elif house == "Ravenclaw":
        return "blue"
    elif house == "Slytherin":
        return "green"
    else:
        return "white"
    # ==STUB
    if house == "Gryffindor":
        return "red"
    # Keep going with elif for the other houses...
    # >>END


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 2: Return the NAME of the house with the most points.
#            If there's a tie, the house listed first wins.
#            pick_house(1, 5, 2, 0) should give back "Hufflepuff"
# ─────────────────────────────────────────────────────────────────────
def pick_house(gryffindor, hufflepuff, ravenclaw, slytherin):
    # <<SOLVE
    best = max(gryffindor, hufflepuff, ravenclaw, slytherin)
    if gryffindor == best:
        return "Gryffindor"
    elif hufflepuff == best:
        return "Hufflepuff"
    elif ravenclaw == best:
        return "Ravenclaw"
    else:
        return "Slytherin"
    # ==STUB
    pass
    # >>END


# ═════════════════════════════════════════════════════════════════════
# 🎨 The quiz itself. You don't need to change anything below, but you
#    could add your own question to QUESTIONS once you're done! Each
#    answer gives a point to (G)ryffindor, (H)ufflepuff, (R)avenclaw or
#    (S)lytherin.
# ═════════════════════════════════════════════════════════════════════
QUESTIONS = [
    ("Pick a takeout order:", {
        "a": ("Spicy Szechuan everything", "G"), "b": ("A family-style feast to share", "H"),
        "c": ("Something you've never tried", "R"), "d": ("Peking duck. Only the best.", "S")}),
    ("Pick a Taylor Swift era:", {
        "a": ("Fearless", "G"), "b": ("Lover", "H"),
        "c": ("folklore", "R"), "d": ("reputation", "S")}),
    ("Your cat knocks a glass off the table. You...", {
        "a": ("Dive to catch it", "G"), "b": ("Give the cat a cuddle anyway", "H"),
        "c": ("Study the physics of the fall", "R"), "d": ("Respect the power move", "S")}),
    ("Perfect date night:", {
        "a": ("An adventure somewhere new", "G"), "b": ("Cozy blanket + movie", "H"),
        "c": ("Learning to code together 😉", "R"), "d": ("Fancy dinner reservation", "S")}),
]

if __name__ == "__main__":
    console = Console()
    console.print("[bold]🎩 Hmm... difficult. VERY difficult. Let's see...[/bold]\n")
    points = {"G": 0, "H": 0, "R": 0, "S": 0}
    for question, answers in QUESTIONS:
        console.print(f"[bold cyan]{question}[/bold cyan]")
        for letter, (text, _) in answers.items():
            console.print(f"   {letter}) {text}")
        choice = ""
        while choice not in answers:
            choice = input("Your answer (a/b/c/d): ").strip().lower()
        points[answers[choice][1]] += 1
        console.print()

    house = pick_house(points["G"], points["H"], points["R"], points["S"])
    color = house_color(house) or "white"
    console.print(Panel(f"[bold {color}]🎉 {str(house).upper()}! 🎉[/bold {color}]",
                        title="The Sorting Hat has decided", border_style=color, expand=False))
