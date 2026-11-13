"""
═══════════════════════════════════════════════════════════════════════
  ⭐ BONUS EXERCISE 2.5 — Palette Potion 🎨🧪
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Computers describe colors as HEX codes like "#ff8800" (that's how
    websites, and Project 3, name colors). You'll convert between hex
    and red/green/blue numbers, then brew a matching color palette from
    any starting color.

    🔮 Project 3's "Surprise me" button uses this exact idea!

🧰 YOUR TOOLBELT
    • A hex color is "#" + 3 pairs of hex digits: red, green, blue.
          "#ff8800"  ->  ff = 255 red, 88 = 136 green, 00 = 0 blue

    • Slicing grabs part of a string:
          code = "#ff8800"
          code[1:3]      # "ff"    (from position 1 up to, not including, 3)

    • int(text, 16) reads a hex number:
          int("ff", 16)  # 255

    • f"{number:02x}" writes a number as 2 hex digits:
          f"{255:02x}"   # "ff"
          f"{8:02x}"     # "08"

    • Tuples hold a few values together:  (255, 136, 0)

▶️ RUN IT        python exercises/project2_puzzles/ex2_5_palette_potion.py
✅ CHECK IT      python check.py 2.5

💡 HINTS (only peek if you're stuck!)
    1. hex_to_rgb: red is int(code[1:3], 16). Green and blue are the next
       two pairs. return (red, green, blue)
    2. rgb_to_hex: return f"#{red:02x}{green:02x}{blue:02x}"
    3. potion_palette: the HUE is the position on the color wheel (0 to 1).
       Spread `count` colors evenly: hue + i / count. Use % 1.0 to wrap
       around the wheel.
"""

import colorsys

from rich.console import Console


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 1: "#ff8800" -> (255, 136, 0)
# ─────────────────────────────────────────────────────────────────────
def hex_to_rgb(code):
    pass


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 2: (255, 136, 0) -> "#ff8800"
# ─────────────────────────────────────────────────────────────────────
def rgb_to_hex(rgb):
    red, green, blue = rgb
    pass


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 3: Return `count` hex colors spread evenly around the color
#            wheel, starting with `base` itself.
#            The two conversion lines are done for you; you write the loop!
# ─────────────────────────────────────────────────────────────────────
def potion_palette(base, count):
    red, green, blue = hex_to_rgb(base)
    hue, lightness, saturation = colorsys.rgb_to_hls(red / 255, green / 255, blue / 255)
    palette = []
    # For each i: new_hue = ...
    #             r, g, b = colorsys.hls_to_rgb(new_hue, lightness, saturation)
    #             (r, g, b are 0-1, so multiply by 255 and round() them)
    #             palette.append(rgb_to_hex(...))
    return palette


if __name__ == "__main__":
    console = Console()
    if hex_to_rgb("#000000") is None or rgb_to_hex((0, 0, 0)) is None:
        console.print("[yellow]🧪 The cauldron is cold... finish TODO 1 and TODO 2 first![/yellow]")
        raise SystemExit
    base = input("🧪 Starting color as hex (Enter for lavender #b497e7): ").strip() or "#b497e7"
    if not base.startswith("#"):
        base = "#" + base
    for count in (2, 3, 5):
        console.print(f"\n[bold]{count}-color potion:[/bold]")
        for color in potion_palette(base, count) or []:
            console.print(f"   [on {color}]          [/] {color}")
