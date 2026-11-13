"""
═══════════════════════════════════════════════════════════════════════
  EXERCISE 2.2 — The Takeout Menu Wizard 🥡🧙
═══════════════════════════════════════════════════════════════════════

🎯 GOAL
    Learn some of Python's neatest shortcuts. LIST COMPREHENSIONS filter
    a whole list in one line, and sorted() with a KEY sorts by whatever
    you want. Then the Menu Wizard plans the perfect order for your budget.

🧰 YOUR TOOLBELT
    • List comprehensions  Build a new list from an old one, in ONE line:
          numbers = [1, 2, 3, 4]
          big = [n for n in numbers if n > 2]        # [3, 4]
          doubled = [n * 2 for n in numbers]          # [2, 4, 6, 8]

      It reads like English: "n, for each n in numbers, if n > 2".

    • sorted(..., key=...)  Sort by a specific thing. A LAMBDA is a tiny
                            one-line function written inline:
          cats = [{"name": "Tom", "age": 5}, {"name": "Kit", "age": 2}]
          sorted(cats, key=lambda cat: cat["age"])   # Kit first, then Tom

    • sum(...)              Adds up numbers, and works with comprehensions!
          sum(n * 2 for n in [1, 2, 3])               # 12

▶️ RUN IT        python exercises/project2_puzzles/ex2_2_menu_wizard.py
✅ CHECK IT      python check.py 2.2

💡 HINTS (only peek if you're stuck!)
    1. vegetarian_dishes: [dish["name"] for dish in menu if dish["vegetarian"]]
    2. dishes_under: same idea, but keep the whole `dish` (not just the name)
       and check dish["price"] <= max_price.
    3. cheapest_first: sorted(menu, key=lambda dish: ...)
    4. order_total: sum(...) of every dish's price, then round(..., 2).
"""

from rich.console import Console
from rich.table import Table

MENU = [
    {"name": "Crab Rangoon", "price": 7.50, "vegetarian": False, "spicy": False},
    {"name": "Vegetable Spring Rolls", "price": 4.95, "vegetarian": True, "spicy": False},
    {"name": "Hot & Sour Soup", "price": 4.25, "vegetarian": True, "spicy": True},
    {"name": "General Tso's Chicken", "price": 15.95, "vegetarian": False, "spicy": True},
    {"name": "Kung Pao Shrimp", "price": 17.50, "vegetarian": False, "spicy": True},
    {"name": "Ma Po Tofu", "price": 13.25, "vegetarian": True, "spicy": True},
    {"name": "Vegetable Lo Mein", "price": 12.25, "vegetarian": True, "spicy": False},
    {"name": "Pork Soup Dumplings", "price": 11.00, "vegetarian": False, "spicy": False},
    {"name": "Scallion Pancake", "price": 6.75, "vegetarian": True, "spicy": False},
    {"name": "Orange Beef", "price": 16.50, "vegetarian": False, "spicy": True},
    {"name": "Egg Fried Rice", "price": 9.95, "vegetarian": True, "spicy": False},
]


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 1: Return a list of the NAMES of every vegetarian dish.
#            Try to do it in ONE line with a list comprehension!
# ─────────────────────────────────────────────────────────────────────
def vegetarian_dishes(menu):
    pass


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 2: Return the dishes (the whole dictionaries) that cost
#            max_price or less.
# ─────────────────────────────────────────────────────────────────────
def dishes_under(menu, max_price):
    pass


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 3: Return the menu sorted from cheapest to priciest.
# ─────────────────────────────────────────────────────────────────────
def cheapest_first(menu):
    pass


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 4: Return the total price of every dish in `order`, rounded
#            to 2 decimal places.
# ─────────────────────────────────────────────────────────────────────
def order_total(order):
    pass


# ═════════════════════════════════════════════════════════════════════
# 🧙 The Menu Wizard. No changes needed below!
# ═════════════════════════════════════════════════════════════════════
def wizard_order(menu, budget):
    """Picks the most dishes that fit the budget (cheapest first)."""
    order = []
    for dish in cheapest_first(menu) or []:
        if (order_total(order + [dish]) or 0) <= budget:
            order.append(dish)
    return order


if __name__ == "__main__":
    console = Console()
    console.print("[bold red]🧙 The Takeout Menu Wizard 🧙[/bold red]\n")
    budget = float(input("What's your budget? (e.g. 40): ") or 40)
    veggie = input("Vegetarian only? (y/n): ").strip().lower() == "y"

    menu = MENU
    if veggie:
        names = vegetarian_dishes(MENU) or []
        menu = [dish for dish in MENU if dish["name"] in names]

    table = Table(title=f"🥡 Everything under ${budget:.2f}", border_style="red")
    table.add_column("Dish")
    table.add_column("Price", justify="right")
    for dish in cheapest_first(dishes_under(menu, budget) or []) or []:
        table.add_row(dish["name"] + (" 🌶️" if dish["spicy"] else ""), f"${dish['price']:.2f}")
    console.print(table)

    order = wizard_order(menu, budget)
    console.print(f"\n✨ The Wizard recommends [bold]{len(order)} dishes[/bold]:")
    for dish in order:
        console.print(f"   • {dish['name']}")
    console.print(f"💰 Total: [bold green]${order_total(order) or 0:.2f}[/bold green]")
