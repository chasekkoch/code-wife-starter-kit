"""
═══════════════════════════════════════════════════════════════════════
  EXERCISE 1.1 — Hello, Birdie! 👋🐈  ✅ SOLVED VERSION
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Write your very first lines of code! You'll make the computer say
    something, store a few facts about yourself in VARIABLES, and glue
    them together into a sentence. At the end, Python draws you a
    personalized name card (with a cat, obviously).

🧰 YOUR TOOLBELT
    • print(...)      Shows something on the screen.
                          print("Hi there!")

    • "text"          Words in quotes are called STRINGS.
                          "Crookshanks"

    • variables       A labeled box that holds a value. The = sign
                      means "put the thing on the right into the box".
                          favorite_color = "lavender"

    • f-strings       Put an f before the quotes and you can drop
                      variables into the text with {curly braces}.
                          pet = "Mittens"
                          sentence = f"My cat is named {pet}!"
                          # sentence is now "My cat is named Mittens!"

▶️ RUN IT        python solutions/project1_basics/ex1_1_hello_birdie.py
✅ CHECK IT      python check.py 1.1 --solutions

💡 HINTS (only peek if you're stuck!)
    1. Keep the quotes! name = "Birdie" works, name = Birdie doesn't.
    2. Variable names can't have spaces. That's why we use_underscores.
    3. In TODO 3, start with:  greeting = f"Hi! I'm {name} and ..."
"""

from rich.console import Console
from rich.panel import Panel

# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 1: Run this file first, exactly as it is. 🏃‍♀️
#            Then change the message inside the quotes to anything
#            you like, save (Ctrl+S / Cmd+S), and run it again!
# ─────────────────────────────────────────────────────────────────────
print("I just wrote my first line of code!")


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 2: Replace each "???" with your own answer (keep the quotes!).
# ─────────────────────────────────────────────────────────────────────
name = "Birdie"
favorite_food = "crab rangoon"  # Takeout counts. Especially takeout.
hogwarts_house = "Ravenclaw"
dream_cat_name = "Benjamin Button"


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 3: Build a sentence with an f-string that uses AT LEAST
#            your name and your favorite food.
#            Example idea: "Hi! I'm ___, I love ___, and ..."
# ─────────────────────────────────────────────────────────────────────
greeting = f"Hi! I'm {name}, I love {favorite_food}, and one day I'll have a cat named {dream_cat_name}."


# ═════════════════════════════════════════════════════════════════════
# 🎨 You don't need to change anything below this line. It just draws
#    your name card using the variables you made above. (Peek if you're
#    curious, though!)
# ═════════════════════════════════════════════════════════════════════
CAT = r"""
   /\_/\
  ( o.o )
   > ^ <
"""

if __name__ == "__main__":
    card = (
        f"[bold magenta]{greeting}[/bold magenta]\n"
        f"{CAT}\n"
        f"🏰 House: [bold]{hogwarts_house}[/bold]\n"
        f"🥡 Fuel: [bold]{favorite_food}[/bold]\n"
        f"🐈 Future cat: [bold]{dream_cat_name}[/bold]"
    )
    Console().print(Panel(card, title=f"✨ {name}'s Name Card ✨", border_style="bright_magenta", expand=False))
