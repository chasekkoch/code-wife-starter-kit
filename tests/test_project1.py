"""Checks for Project 1. Run them with `python check.py 1` (friendlier) or `pytest`."""

import random

import pytest
from conftest import call, exercise_path, load_module

P1 = "project1_basics/"


class TestHelloBirdie:
    FILE = P1 + "ex1_1_hello_birdie.py"

    def test_message_changed(self):
        source = exercise_path(self.FILE).read_text(encoding="utf-8")
        assert 'print("Hello, World!")' not in source, "TODO 1: change the message inside print(...) to something new."

    @pytest.mark.parametrize("variable", ["name", "favorite_food", "hogwarts_house", "dream_cat_name"])
    def test_variables_filled_in(self, variable):
        module = load_module(self.FILE)
        value = getattr(module, variable, None)
        assert isinstance(value, str), f"TODO 2: `{variable}` should be text in quotes, like \"something\"."
        assert value.strip() and value != "???", f"TODO 2: replace the ??? in `{variable}` with your own answer."

    def test_greeting_uses_variables(self):
        module = load_module(self.FILE)
        assert module.greeting != "???", "TODO 3: build `greeting` with an f-string."
        assert module.name in module.greeting, "TODO 3: your greeting should include {name}."
        assert module.favorite_food in module.greeting, "TODO 3: your greeting should include {favorite_food}."


class TestBillSplitter:
    FILE = P1 + "ex1_2_bill_splitter.py"

    def test_tip_amount(self):
        module = load_module(self.FILE)
        assert call(module.tip_amount, 40, 20) == pytest.approx(8), "TODO 1: tip_amount(40, 20) should be 8."
        assert call(module.tip_amount, 50, 15) == pytest.approx(7.5), "TODO 1: tip_amount(50, 15) should be 7.5."

    def test_total_with_tip(self):
        module = load_module(self.FILE)
        assert call(module.total_with_tip, 40, 20) == pytest.approx(48), "TODO 2: total_with_tip(40, 20) should be 48."
        assert call(module.total_with_tip, 100, 0) == pytest.approx(100), "TODO 2: with a 0% tip, the total is just the bill."

    def test_split_bill(self):
        module = load_module(self.FILE)
        assert call(module.split_bill, 50, 2) == pytest.approx(25), "TODO 3: split_bill(50, 2) should be 25."
        assert call(module.split_bill, 50, 3) == 16.67, "TODO 3: split_bill(50, 3) should be 16.67. Did you round to 2 places?"


class TestSortingHat:
    FILE = P1 + "ex1_3_sorting_hat.py"

    @pytest.mark.parametrize("house, color", [
        ("Gryffindor", "red"), ("Hufflepuff", "yellow"), ("Ravenclaw", "blue"), ("Slytherin", "green"),
        ("Durmstrang", "white"),
    ])
    def test_house_color(self, house, color):
        module = load_module(self.FILE)
        assert call(module.house_color, house) == color, f"TODO 1: house_color(\"{house}\") should be \"{color}\"."

    @pytest.mark.parametrize("scores, house", [
        ((5, 1, 1, 1), "Gryffindor"), ((1, 5, 2, 0), "Hufflepuff"), ((0, 1, 4, 2), "Ravenclaw"),
        ((0, 1, 1, 3), "Slytherin"), ((2, 2, 1, 1), "Gryffindor"), ((0, 1, 3, 3), "Ravenclaw"),
    ])
    def test_pick_house(self, scores, house):
        module = load_module(self.FILE)
        assert call(module.pick_house, *scores) == house, f"TODO 2: pick_house{scores} should be \"{house}\"."


class TestTurtleSpiral:
    FILE = P1 + "ex1_4_turtle_spiral.py"

    def test_spiral_lengths(self):
        module = load_module(self.FILE)
        assert call(module.spiral_lengths, 4, 10) == [10, 20, 30, 40], "TODO 1: spiral_lengths(4, 10) should be [10, 20, 30, 40]."
        assert call(module.spiral_lengths, 3, 5) == [5, 10, 15], "TODO 1: spiral_lengths(3, 5) should be [5, 10, 15]."

    def test_color_for_wraps_around(self):
        module = load_module(self.FILE)
        colors = ["red", "gold", "blue"]
        assert call(module.color_for, 1, colors) == "gold", "TODO 2: color_for(1, [...]) should be the 2nd color."
        assert call(module.color_for, 3, colors) == "red", "TODO 2: color_for(3, 3 colors) should wrap back to the 1st color. Try %."
        assert call(module.color_for, 5, colors) == "blue", "TODO 2: color_for(5, 3 colors) should be the 3rd color."


class TestFortuneCookie:
    FILE = P1 + "ex1_5_fortune_cookie.py"

    def test_pick_fortune(self):
        module = load_module(self.FILE)
        assert call(module.pick_fortune) in module.FORTUNES, "TODO 1: return a fortune from the FORTUNES list."

    def test_lucky_numbers(self):
        module = load_module(self.FILE)
        random.seed(7)
        for _ in range(20):
            numbers = call(module.lucky_numbers, 6)
            assert len(numbers) == 6, "TODO 2: lucky_numbers(6) should give back 6 numbers."
            assert len(set(numbers)) == 6, "TODO 2: the numbers should all be different."
            assert all(1 <= n <= 49 for n in numbers), "TODO 2: numbers should be between 1 and 49."
            assert numbers == sorted(numbers), "TODO 2: the numbers should be sorted."


class TestCatQuilt:
    FILE = P1 + "ex1_6_cat_quilt.py"

    def test_grid_positions(self):
        module = load_module(self.FILE)
        expected = [(0, 0), (100, 0), (200, 0), (0, 100), (100, 100), (200, 100)]
        assert call(module.grid_positions, 2, 3, 100) == expected, f"grid_positions(2, 3, 100) should be {expected}."

    def test_grid_size(self):
        module = load_module(self.FILE)
        assert len(call(module.grid_positions, 4, 5, 10)) == 20, "A 4 x 5 grid should have 20 spots."
