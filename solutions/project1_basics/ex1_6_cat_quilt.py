"""
═══════════════════════════════════════════════════════════════════════
  ⭐ BONUS EXERCISE 1.6 — The Cat Quilt 🐈🧶  ✅ SOLVED VERSION
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Put a loop INSIDE another loop (a "nested loop") to build a grid,
    then watch the turtle stitch a quilt of cat faces.

🧰 YOUR TOOLBELT
    • Nested loops    The inner loop runs completely for EACH step of
                      the outer loop.
          for row in range(2):
              for col in range(3):
                  print(row, col)
          # prints: 0 0, 0 1, 0 2, 1 0, 1 1, 1 2

    • Tuples          Like a list, but in (parentheses) and can't change.
                      Perfect for coordinates!
          spot = (100, 50)
          x, y = spot          # x is 100, y is 50

▶️ RUN IT        python solutions/project1_basics/ex1_6_cat_quilt.py
✅ CHECK IT      python check.py 1.6 --solutions

💡 HINTS (only peek if you're stuck!)
    1. grid_positions(2, 3, 100) should give
       [(0, 0), (100, 0), (200, 0), (0, 100), (100, 100), (200, 100)]
    2. x comes from the column, y comes from the row.
    3. positions.append((x, y))   ← note the DOUBLE parentheses: one for
       append, one for the tuple.
"""


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO: Return a list of (x, y) spots for a grid with `rows` rows and
#          `cols` columns, each `spacing` apart. Go row by row.
# ─────────────────────────────────────────────────────────────────────
def grid_positions(rows, cols, spacing):
    positions = []
    for row in range(rows):
        for col in range(cols):
            positions.append((col * spacing, row * spacing))
    return positions


# ═════════════════════════════════════════════════════════════════════
# 🎛️ KNOBS
# ═════════════════════════════════════════════════════════════════════
ROWS = 4
COLS = 5
SPACING = 110
CAT_COLORS = ["#f4a261", "#9e9e9e", "#2b2b2b", "#e9c46a", "#f6f1e9"]  # ginger, grey, black, gold, cream


def draw_cat(pen, x, y, fur):
    """Draws one cat face centered at (x, y). (Already done for you!)"""
    pen.penup()
    pen.goto(x, y - 35)
    pen.pendown()
    pen.color("black", fur)
    pen.begin_fill()
    pen.circle(35)  # head
    pen.end_fill()
    for side in (-1, 1):  # ears
        pen.penup()
        pen.goto(x + side * 30, y + 15)
        pen.pendown()
        pen.begin_fill()
        pen.goto(x + side * 30, y + 50)
        pen.goto(x + side * 8, y + 32)
        pen.goto(x + side * 30, y + 15)
        pen.end_fill()
        pen.penup()  # eyes
        pen.goto(x + side * 12, y + 5)
        pen.dot(9, "#7cd67c")
    pen.goto(x, y - 8)  # nose
    pen.dot(7, "pink")


if __name__ == "__main__":
    import turtle

    screen = turtle.Screen()
    screen.title("The Cat Quilt 🐈")
    screen.bgcolor("#fdf0d5")
    screen.tracer(0)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.width(2)

    offset_x = -(COLS - 1) * SPACING / 2
    offset_y = -(ROWS - 1) * SPACING / 2
    for i, (x, y) in enumerate(grid_positions(ROWS, COLS, SPACING)):
        draw_cat(pen, x + offset_x, y + offset_y, CAT_COLORS[i % len(CAT_COLORS)])
        screen.update()

    print("🐈 Meow! Close the turtle window when you're done.")
    turtle.done()
