"""
═══════════════════════════════════════════════════════════════════════
  EXERCISE 1.2 — Takeout Bill Splitter 🥡💸  ✅ SOLVED VERSION
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Friday night, Chinese takeout, and somebody has to do the math.
    You'll write three tiny FUNCTIONS that work out the tip and split
    the bill. Then Python prints a fancy receipt for you.

🧰 YOUR TOOLBELT
    • Math            +  -  *  /   work just like a calculator.
                          20 * 15 / 100    # 3.0

    • Functions       A reusable recipe. Ingredients go in the
                      (parentheses), and `return` hands back the result.
                          def double(number):
                              return number * 2

                          double(21)       # 42

    • Calling a function from another function: totally allowed!
                          def quadruple(number):
                              return double(double(number))

    • round(x, 2)     Rounds to 2 decimal places (cents!).
                          round(10.3333, 2)   # 10.33

▶️ RUN IT        python solutions/project1_basics/ex1_2_bill_splitter.py
✅ CHECK IT      python check.py 1.2 --solutions

💡 HINTS (only peek if you're stuck!)
    1. The tip on a $40 bill at 20% is 40 * 20 / 100.
    2. The code INSIDE a function must be indented (pushed right with Tab).
    3. total_with_tip can call tip_amount(bill, tip_percent) for you.
    4. Delete the word `pass`. It just means "nothing here yet".
"""

from rich.console import Console
from rich.table import Table


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 1: Return how much the tip is.
#            tip_amount(40, 20) should give back 8.0
# ─────────────────────────────────────────────────────────────────────
def tip_amount(bill, tip_percent):
    return bill * tip_percent / 100


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 2: Return the bill PLUS the tip.
#            total_with_tip(40, 20) should give back 48.0
# ─────────────────────────────────────────────────────────────────────
def total_with_tip(bill, tip_percent):
    return bill + tip_amount(bill, tip_percent)


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 3: Return what each person pays, rounded to 2 decimal places.
#            split_bill(50, 3) should give back 16.67
# ─────────────────────────────────────────────────────────────────────
def split_bill(total, people):
    return round(total / people, 2)


# ═════════════════════════════════════════════════════════════════════
# 🎨 You don't need to change anything below this line (but you CAN
#    edit the order to match your real favorites!).
# ═════════════════════════════════════════════════════════════════════
ORDER = {
    "General Tso's Chicken": 15.95,
    "Crab Rangoon (8)": 7.50,
    "Vegetable Lo Mein": 12.25,
    "Egg Rolls (2)": 5.00,
    "Fortune Cookies": 0.00,
}

if __name__ == "__main__":
    console = Console()
    console.print("[bold red]🥡 Welcome to the Takeout Bill Splitter! 🥡[/bold red]\n")
    tip_percent = float(input("What tip percent? (e.g. 20): ") or 20)
    people = int(input("How many people are eating? (e.g. 2): ") or 2)

    subtotal = sum(ORDER.values())
    tip = tip_amount(subtotal, tip_percent)
    total = total_with_tip(subtotal, tip_percent)
    each = split_bill(total, people) if total is not None else None

    receipt = Table(title="🧾 Golden Dragon Takeout", show_header=False, border_style="red")
    for dish, price in ORDER.items():
        receipt.add_row(dish, f"${price:.2f}")
    receipt.add_section()
    receipt.add_row("Subtotal", f"${subtotal:.2f}")
    receipt.add_row(f"Tip ({tip_percent:g}%)", f"${tip:.2f}" if tip is not None else "???")
    receipt.add_row("[bold]Total[/bold]", f"[bold]${total:.2f}[/bold]" if total is not None else "???")
    receipt.add_section()
    receipt.add_row(f"[bold green]Each of {people} pays[/bold green]",
                    f"[bold green]${each:.2f}[/bold green]" if each is not None else "???")
    console.print(receipt)
    console.print("\n🥠 [italic]Your fortune: You will write many more functions.[/italic]")
