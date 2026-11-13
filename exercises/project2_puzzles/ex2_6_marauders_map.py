"""
═══════════════════════════════════════════════════════════════════════
  ⭐ BONUS EXERCISE 2.6 — The Marauder's Map 🗺️👣
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Build a GRID (a list of lists, like rows and columns in a
    spreadsheet) and animate cats wandering around a castle, leaving
    footprints wherever they go. "I solemnly swear that I am up to no good."

🧰 YOUR TOOLBELT
    • A list of lists is a grid. grid[row][col] gets one square:
          grid = [[".", "."],
                  [".", "."]]
          grid[1][0] = "🐈"        # row 1, column 0

    • Comprehensions can build lists of lists:
          [["." for col in range(3)] for row in range(2)]
          # [[".", ".", "."], [".", ".", "."]]

    • Dictionaries can hold tuples:
          STEPS = {"up": (0, -1), "down": (0, 1)}
          dx, dy = STEPS["up"]       # dx is 0, dy is -1

    • min / max keep things inside the walls:
          max(0, min(x, width - 1))

▶️ RUN IT        python exercises/project2_puzzles/ex2_6_marauders_map.py
✅ CHECK IT      python check.py 2.6

💡 HINTS (only peek if you're stuck!)
    1. make_map(3, 2) should be [[".", ".", "."], [".", ".", "."]]
       (`height` rows, each `width` wide).
    2. move: look up (dx, dy) in STEPS, add them to x and y, then keep
       x between 0 and width - 1 (and y between 0 and height - 1).
"""

import random
import time

from rich.console import Console
from rich.live import Live
from rich.panel import Panel

STEPS = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 1: Return a grid `height` rows tall and `width` columns wide,
#            where every square is "." (an empty castle floor).
# ─────────────────────────────────────────────────────────────────────
def make_map(width, height):
    pass


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 2: Return the new (x, y) after one step in `direction`,
#            without walking through the outer walls.
#            move((0, 0), "left", 5, 5) -> (0, 0)   (bonk, wall!)
#            move((2, 2), "down", 5, 5) -> (2, 3)
# ─────────────────────────────────────────────────────────────────────
def move(position, direction, width, height):
    x, y = position
    pass


# ═════════════════════════════════════════════════════════════════════
# 🗺️ The map animation. No changes needed below!
# ═════════════════════════════════════════════════════════════════════
WIDTH, HEIGHT, TICKS = 24, 12, 80
WANDERERS = {"🐈": "Crookshanks", "🐱": "Mrs Norris", "🐾": "Meredith"}


def render(grid, positions):
    rows = []
    for y, row in enumerate(grid):
        cells = []
        for x, cell in enumerate(row):
            here = [icon for icon, pos in positions.items() if pos == (x, y)]
            cells.append(here[0] if here else ("[yellow]··[/yellow]" if cell == "·" else "[dim]. [/dim]"))
        rows.append("".join(cells))
    legend = "   ".join(f"{icon} {name}" for icon, name in WANDERERS.items())
    return Panel("\n".join(rows) + f"\n\n{legend}", title="🗺️ The Marauder's Map", border_style="yellow", expand=False)


if __name__ == "__main__":
    console = Console()
    console.print("[italic]I solemnly swear that I am up to no good...[/italic]\n")
    grid = make_map(WIDTH, HEIGHT)
    if not grid:
        console.print("[yellow]The map is blank... finish TODO 1 first![/yellow]")
        raise SystemExit
    positions = {icon: (random.randrange(WIDTH), random.randrange(HEIGHT)) for icon in WANDERERS}
    with Live(render(grid, positions), console=console, refresh_per_second=10) as live:
        for _ in range(TICKS):
            for icon, (x, y) in positions.items():
                grid[y][x] = "·"  # leave a footprint
                positions[icon] = move((x, y), random.choice(list(STEPS)), WIDTH, HEIGHT) or (x, y)
            live.update(render(grid, positions))
            time.sleep(0.15)
    console.print("\n[italic]Mischief managed.[/italic] 🌙")
