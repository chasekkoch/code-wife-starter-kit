"""
═══════════════════════════════════════════════════════════════════════
  EXERCISE 1.4 — The Eras Spiral 🌀🎤  ✅ SOLVED VERSION
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Make the computer REPEAT things with a LOOP, then watch a turtle
    draw a hypnotic spiral in every Taylor Swift era color. 🐢✨

🧰 YOUR TOOLBELT
    • Lists           A collection of things in [square brackets].
                          snacks = ["dumplings", "bao", "boba"]
                          snacks[0]          # "dumplings"  (counting starts at 0!)
                          len(snacks)        # 3

    • .append(...)    Adds something to the end of a list.
                          snacks.append("mochi")

    • for loops       Do something once for every item.
                          for snack in snacks:
                              print(snack)

    • range(...)      Makes a sequence of numbers to loop over.
                          for n in range(1, 4):
                              print(n)       # prints 1, then 2, then 3
                                             # (stops BEFORE the 4!)

    • %  (modulo)     The remainder after dividing. Great for "wrapping
                      around" a list:   7 % 3  is 1    9 % 3  is 0

▶️ RUN IT        python solutions/project1_basics/ex1_4_turtle_spiral.py
✅ CHECK IT      python check.py 1.4 --solutions

💡 HINTS (only peek if you're stuck!)
    1. spiral_lengths(4, 10) should give [10, 20, 30, 40].
       Start with an empty list:  lengths = []
       Loop with:                 for n in range(1, count + 1):
       Add to it with:            lengths.append(n * step)
       Then:                      return lengths
    2. color_for(5, ["red", "gold"]) should be "gold" because 5 % 2 is 1.
    3. 🎛️ Once it works, play with TURN_ANGLE, COUNT and STEP below!
"""


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 1: Return a list of line lengths that grow by `step` each time.
#            spiral_lengths(4, 10) -> [10, 20, 30, 40]
# ─────────────────────────────────────────────────────────────────────
def spiral_lengths(count, step):
    lengths = []
    for n in range(1, count + 1):
        lengths.append(n * step)
    return lengths


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 2: Return the color to use for line number `index`, wrapping
#            back to the start of the list when we run out of colors.
#            color_for(0, ["red", "gold"]) -> "red"
#            color_for(3, ["red", "gold"]) -> "gold"
# ─────────────────────────────────────────────────────────────────────
def color_for(index, colors):
    return colors[index % len(colors)]


# ═════════════════════════════════════════════════════════════════════
# 🎛️ KNOBS. Change these and re-run to get totally different art!
# ═════════════════════════════════════════════════════════════════════
TURN_ANGLE = 91   # try 59, 89, 121, 144...
COUNT = 200       # how many lines to draw
STEP = 2          # how much longer each line gets

ERA_COLORS = [
    "#7cc6ee",  # debut
    "#e8c26a",  # Fearless
    "#a66fd1",  # Speak Now
    "#d2203f",  # Red
    "#8ec5e8",  # 1989
    "#c0c0c0",  # reputation
    "#f4a6c9",  # Lover
    "#bdbdbd",  # folklore
    "#d08a4e",  # evermore
    "#5f7fdf",  # Midnights
    "#efe9dc",  # The Tortured Poets Department
    "#f28c28",  # The Life of a Showgirl
]

if __name__ == "__main__":
    import turtle

    screen = turtle.Screen()
    screen.title("The Eras Spiral 🐢")
    screen.bgcolor("black")
    screen.tracer(4)  # draw faster
    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(2)

    for i, length in enumerate(spiral_lengths(COUNT, STEP)):
        pen.pencolor(color_for(i, ERA_COLORS))
        pen.forward(length)
        pen.left(TURN_ANGLE)

    pen.hideturtle()
    screen.update()
    print("✨ Done! Close the turtle window when you're finished admiring it.")
    turtle.done()
