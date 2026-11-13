"""Checks for Project 2. Run them with `python check.py 2` (friendlier) or `pytest`."""

import json

import pytest
from conftest import call, load_module

P2 = "project2_puzzles/"


class TestErasStats:
    FILE = P2 + "ex2_1_eras_stats.py"
    SAMPLE = [
        {"title": "A", "year": 2001, "tracks": 10},
        {"title": "B", "year": 2002, "tracks": 14},
        {"title": "C", "year": 2002, "tracks": 9},
    ]

    def test_total_tracks(self):
        module = load_module(self.FILE)
        assert call(module.total_tracks, self.SAMPLE) == 33, "TODO 1: 10 + 14 + 9 tracks should add up to 33."
        assert call(module.total_tracks, module.ALBUMS) == 172, "TODO 1: all the real albums should add up to 172 tracks."

    def test_albums_from_year(self):
        module = load_module(self.FILE)
        assert call(module.albums_from_year, module.ALBUMS, 2020) == ["folklore", "evermore"], \
            "TODO 2: albums_from_year(ALBUMS, 2020) should be [\"folklore\", \"evermore\"]."
        assert call(module.albums_from_year, self.SAMPLE, 1999) == [], "TODO 2: a year with no albums should give an empty list []."

    def test_albums_per_year(self):
        module = load_module(self.FILE)
        assert call(module.albums_per_year, self.SAMPLE) == {2001: 1, 2002: 2}, \
            "TODO 3: albums_per_year should count albums by year, like {2001: 1, 2002: 2}."

    def test_longest_album(self):
        module = load_module(self.FILE)
        assert call(module.longest_album, self.SAMPLE) == "B", "TODO 4: return the TITLE of the album with the most tracks."
        assert call(module.longest_album, module.ALBUMS) == "Lover", "TODO 4: the longest real album is Lover (18 tracks)."


class TestMenuWizard:
    FILE = P2 + "ex2_2_menu_wizard.py"

    def test_vegetarian_dishes(self):
        module = load_module(self.FILE)
        names = call(module.vegetarian_dishes, module.MENU)
        expected = [d["name"] for d in module.MENU if d["vegetarian"]]
        assert names == expected, "TODO 1: return the NAMES of the vegetarian dishes, in menu order."

    def test_dishes_under(self):
        module = load_module(self.FILE)
        cheap = call(module.dishes_under, module.MENU, 7.50)
        assert all(isinstance(d, dict) for d in cheap), "TODO 2: return the whole dish dictionaries, not just names."
        assert sorted(d["name"] for d in cheap) == sorted(
            ["Crab Rangoon", "Vegetable Spring Rolls", "Hot & Sour Soup", "Scallion Pancake"]
        ), "TODO 2: dishes that cost exactly max_price should be included too (use <=)."

    def test_cheapest_first(self):
        module = load_module(self.FILE)
        ordered = call(module.cheapest_first, module.MENU)
        prices = [d["price"] for d in ordered]
        assert len(ordered) == len(module.MENU), "TODO 3: keep every dish, just reorder them."
        assert prices == sorted(prices), "TODO 3: dishes should go from cheapest to priciest."

    def test_order_total(self):
        module = load_module(self.FILE)
        order = [{"price": 1.10}, {"price": 2.20}, {"price": 3.30}]
        assert call(module.order_total, order) == 6.6, "TODO 4: 1.10 + 2.20 + 3.30 should be 6.6 (rounded to 2 places)."
        assert call(module.order_total, []) == 0, "TODO 4: an empty order costs 0."


class TestCatCafe:
    FILE = P2 + "ex2_3_cat_cafe.py"

    def test_pet(self):
        module = load_module(self.FILE)
        cat = module.Cat("Test", "tabby", mood=50)
        cat.pet()
        assert cat.mood == 65, "TODO 1: petting a cat with mood 50 should make it 65."
        cat = module.Cat("Test", "tabby", mood=95)
        cat.pet()
        assert cat.mood == 100, "TODO 1: mood should never go above 100."

    def test_feed(self):
        module = load_module(self.FILE)
        cat = module.Cat("Test", "tabby", mood=50, hunger=50)
        cat.feed()
        assert cat.hunger == 20, "TODO 2: feeding a cat with hunger 50 should make it 20."
        assert cat.mood == 55, "TODO 2: feeding should also raise mood by 5."
        cat = module.Cat("Test", "tabby", mood=98, hunger=10)
        cat.feed()
        assert cat.hunger == 0, "TODO 2: hunger should never go below 0."
        assert cat.mood == 100, "TODO 2: mood should never go above 100."

    @pytest.mark.parametrize("mood, hunger, happy", [(70, 30, True), (90, 0, True), (69, 0, False), (100, 31, False)])
    def test_is_happy(self, mood, hunger, happy):
        module = load_module(self.FILE)
        cat = module.Cat("Test", "tabby", mood=mood, hunger=hunger)
        assert cat.is_happy() is happy, f"TODO 3: a cat with mood {mood} and hunger {hunger} should be {'happy' if happy else 'NOT happy'} (return True or False)."


class TestSpellBook:
    FILE = P2 + "ex2_4_spell_book.py"
    SPELLS = {"lumos": {"effect": "Light!", "color": "yellow"}}

    def test_load_spells(self, tmp_path):
        module = load_module(self.FILE)
        path = tmp_path / "spells.json"
        path.write_text(json.dumps(self.SPELLS), encoding="utf-8")
        assert call(module.load_spells, path) == self.SPELLS, "TODO 1: load_spells should return the dictionary from the file."

    def test_load_missing_file(self, tmp_path):
        module = load_module(self.FILE)
        assert call(module.load_spells, tmp_path / "nope.json") == {}, \
            "TODO 1: if the file doesn't exist, return {} (catch FileNotFoundError)."

    def test_cast(self):
        module = load_module(self.FILE)
        assert call(module.cast, self.SPELLS, "lumos") == "Light!", "TODO 2: cast should return the spell's effect."
        assert call(module.cast, self.SPELLS, "  LuMoS ") == "Light!", "TODO 2: ignore extra spaces and capital letters."
        assert call(module.cast, self.SPELLS, "avada") == module.FIZZLE, "TODO 2: unknown spells should return FIZZLE."

    def test_save_spells(self, tmp_path):
        module = load_module(self.FILE)
        path = tmp_path / "saved.json"
        module.save_spells(path, self.SPELLS)
        assert path.exists(), "TODO 3: save_spells should create the file."
        assert json.loads(path.read_text(encoding="utf-8")) == self.SPELLS, "TODO 3: the file should contain the spells as JSON."


class TestPalettePotion:
    FILE = P2 + "ex2_5_palette_potion.py"

    def test_hex_to_rgb(self):
        module = load_module(self.FILE)
        assert call(module.hex_to_rgb, "#ff8800") == (255, 136, 0), "TODO 1: \"#ff8800\" should become (255, 136, 0)."
        assert call(module.hex_to_rgb, "#000000") == (0, 0, 0), "TODO 1: \"#000000\" should become (0, 0, 0)."

    def test_rgb_to_hex(self):
        module = load_module(self.FILE)
        assert call(module.rgb_to_hex, (255, 136, 0)) == "#ff8800", "TODO 2: (255, 136, 0) should become \"#ff8800\"."
        assert call(module.rgb_to_hex, (1, 2, 3)) == "#010203", "TODO 2: small numbers need 2 digits each (use :02x)."

    def test_potion_palette(self):
        module = load_module(self.FILE)
        palette = call(module.potion_palette, "#ff0000", 3)
        assert len(palette) == 3, "TODO 3: potion_palette(base, 3) should give back 3 colors."
        assert palette == ["#ff0000", "#00ff00", "#0000ff"], "TODO 3: red split 3 ways should be red, green, blue."


class TestMaraudersMap:
    FILE = P2 + "ex2_6_marauders_map.py"

    def test_make_map(self):
        module = load_module(self.FILE)
        assert call(module.make_map, 3, 2) == [[".", ".", "."], [".", ".", "."]], \
            "TODO 1: make_map(3, 2) should be 2 rows of 3 dots."

    def test_rows_are_separate(self):
        module = load_module(self.FILE)
        grid = call(module.make_map, 2, 2)
        grid[0][0] = "X"
        assert grid[1][0] == ".", "TODO 1: each row must be its own list (build them with a comprehension)."

    @pytest.mark.parametrize("start, direction, end", [
        ((2, 2), "down", (2, 3)), ((2, 2), "up", (2, 1)), ((2, 2), "left", (1, 2)), ((2, 2), "right", (3, 2)),
        ((0, 0), "left", (0, 0)), ((0, 0), "up", (0, 0)), ((4, 4), "right", (4, 4)), ((4, 4), "down", (4, 4)),
    ])
    def test_move(self, start, direction, end):
        module = load_module(self.FILE)
        assert call(module.move, start, direction, 5, 5) == end, f"TODO 2: move({start}, \"{direction}\", 5, 5) should be {end}."
