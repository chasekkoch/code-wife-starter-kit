"""
═══════════════════════════════════════════════════════════════════════
  EXERCISE 2.1 — Eras Tour Stats 🎤📊
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Real programs spend most of their time digging through DATA. Here,
    every album is a DICTIONARY (a set of labeled facts), and all the
    albums together are a LIST. You'll answer questions about the
    discography, and Python will turn your answers into a stats board.

🧰 YOUR TOOLBELT
    • Dictionaries    Labeled values in {curly braces}. Look up a value
                      with its label (called a KEY) in [square brackets].
          album = {"title": "Lover", "year": 2019, "tracks": 18}
          album["year"]        # 2019

    • Looping over a list of dictionaries:
          for album in ALBUMS:
              print(album["title"])

    • Adding up       Start a running total at 0 and keep adding.
          total = 0
          for n in [1, 2, 3]:
              total = total + n     # or the shortcut:  total += n

    • Counting with a dictionary:
          counts = {}
          counts["cats"] = counts.get("cats", 0) + 1
          # .get(key, 0) means "give me the value, or 0 if it's not there yet"

▶️ RUN IT        python exercises/project2_puzzles/ex2_1_eras_stats.py
✅ CHECK IT      python check.py 2.1

💡 HINTS (only peek if you're stuck!)
    1. total_tracks: running total, adding album["tracks"] each loop.
    2. albums_from_year: start with an empty list and .append() the
       title when album["year"] == year.
    3. albums_per_year: use the counting pattern above, with album["year"]
       as the key.
    4. longest_album: remember the best album so far. If the current one
       has MORE tracks, it becomes the new best. Return its title.
"""

from rich.console import Console
from rich.table import Table

ALBUMS = [
    {"title": "Taylor Swift", "year": 2006, "tracks": 11},
    {"title": "Fearless", "year": 2008, "tracks": 13},
    {"title": "Speak Now", "year": 2010, "tracks": 14},
    {"title": "Red", "year": 2012, "tracks": 16},
    {"title": "1989", "year": 2014, "tracks": 13},
    {"title": "reputation", "year": 2017, "tracks": 15},
    {"title": "Lover", "year": 2019, "tracks": 18},
    {"title": "folklore", "year": 2020, "tracks": 16},
    {"title": "evermore", "year": 2020, "tracks": 15},
    {"title": "Midnights", "year": 2022, "tracks": 13},
    {"title": "The Tortured Poets Department", "year": 2024, "tracks": 16},
    {"title": "The Life of a Showgirl", "year": 2025, "tracks": 12},
]


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 1: Return the total number of tracks across ALL albums.
# ─────────────────────────────────────────────────────────────────────
def total_tracks(albums):
    pass


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 2: Return a list of the TITLES of albums released in `year`.
#            albums_from_year(ALBUMS, 2020) -> ["folklore", "evermore"]
# ─────────────────────────────────────────────────────────────────────
def albums_from_year(albums, year):
    pass


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 3: Return a dictionary of {year: how many albums that year}.
#            e.g. {2006: 1, 2008: 1, ..., 2020: 2, ...}
# ─────────────────────────────────────────────────────────────────────
def albums_per_year(albums):
    pass


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 4: Return the TITLE of the album with the most tracks.
# ─────────────────────────────────────────────────────────────────────
def longest_album(albums):
    pass


# ═════════════════════════════════════════════════════════════════════
# 🎨 The stats board. No changes needed below!
# ═════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    console = Console()
    table = Table(title="🎤 The Eras Stats Board 🎤", border_style="magenta")
    table.add_column("Year", justify="right")
    table.add_column("Album", style="bold")
    table.add_column("Tracks")
    for album in ALBUMS:
        table.add_row(str(album["year"]), album["title"], "[magenta]" + "█" * album["tracks"] + f"[/magenta] {album['tracks']}")
    console.print(table)

    console.print(f"\n🎶 Total tracks: [bold]{total_tracks(ALBUMS)}[/bold]")
    console.print(f"📅 Released in 2020: [bold]{albums_from_year(ALBUMS, 2020)}[/bold]")
    console.print(f"🏆 Longest album: [bold]{longest_album(ALBUMS)}[/bold]")
    per_year = albums_per_year(ALBUMS)
    if per_year:
        busiest = max(per_year, key=per_year.get)
        console.print(f"🔥 Busiest year: [bold]{busiest}[/bold] with {per_year[busiest]} albums")
