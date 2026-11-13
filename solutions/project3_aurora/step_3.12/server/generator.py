"""
═══════════════════════════════════════════════════════════════════════
  PROJECT 3, STEP 3.9 — The "Surprise me!" Generator 🎲🎨  ✅ SOLVED THROUGH STEP 3.12
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Write the Python that invents a brand-new random Aurora every time
    you press 🎲 Surprise me. You'll pick a random color palette that
    actually looks good together, plus random values for every knob.

🧰 YOUR TOOLBELT
    • random.random()            a random decimal from 0 to 1
    • random.uniform(2, 8)       a random decimal from 2 to 8
    • random.randint(2, 8)       a random WHOLE number from 2 to 8
    • random.choice(["a", "b"])  a random item from a list
    • round(3.14159, 2)          3.14
    • isinstance(5, int)         True if 5 is a whole number (an int)
    • for key, (low, high) in RANGES.items():    loop over a dictionary's
                                                 keys AND values together
    • hsl_to_hex(hue, saturation, lightness)     (already written below!)
          hue        0-1: position on the color wheel (0 red, 0.33 green, 0.66 blue)
          saturation 0-1: 0 = grey, 1 = super colorful
          lightness  0-1: 0 = black, 0.5 = pure color, 1 = white

✅ CHECK IT      python check.py 3.9 --solutions
👀 SEE IT        press 🎲 Surprise me in the Aurora (no restart needed)

💡 HINTS (only peek if you're stuck!)
    1. Colors that sit near each other on the color wheel look great
       together. Pick one random hue, then nudge it: (hue + 0.1) % 1.0
    2. The background should be VERY dark (lightness around 0.05) so the
       glowing particles pop.
    3. In random_preset, start with  preset = random_palette()  and then
       ADD keys to it:  preset["mood"] = random.choice(MOODS)
"""

import colorsys
import random

# The lowest and highest value for each knob. (Whole numbers = whole-number knobs.)
RANGES = {
    "particleCount": (800, 3000),
    "particleSize": (0.8, 3.0),
    "particleAlpha": (30, 120),
    "speed": (0.5, 3.0),
    "noiseScale": (0.001, 0.006),
    "swirl": (1.0, 4.0),
    "trailFade": (10, 30),
    "chordSeconds": (2.0, 8.0),
    "reverb": (3.0, 15.0),
}
MOODS = ["dreamy", "mysterious", "hopeful"]
ROOT_NOTES = ["C3", "D3", "E3", "F3", "G3", "A3"]


def hsl_to_hex(hue, saturation, lightness):
    """✅ Already done. Turns hue/saturation/lightness (each 0-1) into a "#rrggbb" color."""
    red, green, blue = colorsys.hls_to_rgb(hue % 1.0, lightness, saturation)
    return f"#{round(red * 255):02x}{round(green * 255):02x}{round(blue * 255):02x}"


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 1: Return a dictionary with three colors:
#              "background": a VERY dark color
#              "colorA":     a bright, colorful color
#              "colorB":     another bright color with a nearby hue
# ─────────────────────────────────────────────────────────────────────
def random_palette():
    hue = random.random()
    return {
        "background": hsl_to_hex(hue, 0.6, 0.05),
        "colorA": hsl_to_hex(hue + 0.05, 0.9, 0.6),
        "colorB": hsl_to_hex(hue + random.uniform(0.15, 0.35), 0.9, 0.6),
    }


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 2: Return a whole random preset: the palette, PLUS a random
#            value (between low and high) for every knob in RANGES, PLUS
#            a random "mood" and "rootNote", PLUS "glow": True.
#            Whole-number ranges should give whole numbers!
# ─────────────────────────────────────────────────────────────────────
def random_preset():
    preset = random_palette()
    for key, (low, high) in RANGES.items():
        if isinstance(low, int):
            preset[key] = random.randint(low, high)
        else:
            preset[key] = round(random.uniform(low, high), 4)
    preset["mood"] = random.choice(MOODS)
    preset["rootNote"] = random.choice(ROOT_NOTES)
    preset["glow"] = True
    return preset


if __name__ == "__main__":
    # Try it on its own:  python generator.py
    print(random_preset())
