"""Checks for Project 3's Python parts (steps 3.8 and 3.9). The web steps are checked in the browser."""

import json
import re

import pytest
from fastapi.testclient import TestClient

from conftest import call, load_module

HEX_COLOR = re.compile(r"^#[0-9a-f]{6}$")


# ─────────────────────────────── 3.8 Presets API ───────────────────────────────
@pytest.fixture
def server(tmp_path):
    """The learner's server, using a scratch presets folder with two presets in it."""
    main = load_module("project3_aurora/server/main.py")
    (tmp_path / "midnight_cat.json").write_text(json.dumps({"colorA": "#5ad1ff", "speed": 1.8}), encoding="utf-8")
    (tmp_path / "lavender_haze.json").write_text(json.dumps({"colorA": "#c7a6ff", "speed": 1.2}), encoding="utf-8")
    main.PRESETS_DIR = tmp_path
    return TestClient(main.app), tmp_path


def not_built(response):
    return response.status_code == 501


class TestPresetsApi:
    def test_list_presets(self, server):
        client, _ = server
        response = client.get("/api/presets")
        assert not not_built(response), "TODO 1: list_presets() still says 'Not built yet'. Replace the raise with your code!"
        assert response.status_code == 200, f"TODO 1: list_presets() crashed (status {response.status_code})."
        names = response.json()
        assert names == ["lavender_haze", "midnight_cat"], (
            f"TODO 1: expected the sorted names ['lavender_haze', 'midnight_cat'], got {names}. "
            "Use path.stem (no .json!) and sorted(...)."
        )

    def test_get_preset(self, server):
        client, _ = server
        response = client.get("/api/presets/midnight_cat")
        assert not not_built(response), "TODO 2: get_preset() still says 'Not built yet'."
        assert response.status_code == 200, f"TODO 2: get_preset() crashed (status {response.status_code})."
        assert response.json() == {"colorA": "#5ad1ff", "speed": 1.8}, (
            "TODO 2: get_preset() should give back the file's contents as a dictionary (json.loads)."
        )

    def test_missing_preset_is_404(self, server):
        client, _ = server
        response = client.get("/api/presets/no_such_cat")
        assert not not_built(response), "TODO 2: get_preset() still says 'Not built yet'."
        assert response.status_code == 404, (
            f"TODO 2: asking for a preset that doesn't exist should give a 404, got {response.status_code}. "
            "Check path.exists() and raise HTTPException(status_code=404, ...)."
        )

    def test_save_preset(self, server):
        client, folder = server
        preset = {"colorA": "#ff0000", "speed": 3}
        response = client.post("/api/presets/Red Alert", json=preset)
        assert not not_built(response), "TODO 3: save_preset() still says 'Not built yet'."
        assert response.status_code == 200, f"TODO 3: save_preset() crashed (status {response.status_code})."
        saved_file = folder / "red_alert.json"
        assert saved_file.exists(), "TODO 3: no file was saved. Use path.write_text(json.dumps(preset), ...)."
        assert json.loads(saved_file.read_text(encoding="utf-8")) == preset, (
            "TODO 3: the saved file doesn't contain the preset. Did you json.dumps(preset)?"
        )
        assert response.json() == {"saved": "red_alert"}, (
            f"TODO 3: should return {{'saved': 'red_alert'}}, got {response.json()}. Use path.stem."
        )

    def test_save_then_load(self, server):
        client, _ = server
        preset = {"colorA": "#00ff00", "glow": True}
        client.post("/api/presets/round_trip", json=preset)
        response = client.get("/api/presets/round_trip")
        assert response.status_code == 200 and response.json() == preset, (
            "TODO 2 + 3: a preset you save should load back exactly the same."
        )


# ─────────────────────────────── 3.9 Generator ───────────────────────────────
class TestGenerator:
    def test_random_palette(self):
        gen = load_module("project3_aurora/server/generator.py")
        palette = call(gen.random_palette)
        assert isinstance(palette, dict), "TODO 1: random_palette() should return a dictionary."
        assert set(palette) == {"background", "colorA", "colorB"}, (
            f"TODO 1: the palette needs exactly the keys background, colorA and colorB. Got {sorted(palette)}."
        )
        for key, value in palette.items():
            assert isinstance(value, str) and HEX_COLOR.match(value), (
                f"TODO 1: {key} should be a color like '#a1b2c3', got {value!r}. Use hsl_to_hex(...)."
            )

    def test_background_is_dark(self):
        gen = load_module("project3_aurora/server/generator.py")
        for _ in range(20):
            background = call(gen.random_palette)["background"]
            brightest = max(int(background[i:i + 2], 16) for i in (1, 3, 5))
            assert brightest <= 60, (
                f"TODO 1: the background {background} is too bright for glowing particles. "
                "Use a tiny lightness, around 0.05."
            )

    def test_palette_is_random(self):
        gen = load_module("project3_aurora/server/generator.py")
        colors = {call(gen.random_palette)["colorA"] for _ in range(10)}
        assert len(colors) > 1, "TODO 1: every palette is the same! Pick the hue with random.random()."

    def test_random_preset_has_everything(self):
        gen = load_module("project3_aurora/server/generator.py")
        preset = call(gen.random_preset)
        expected = set(gen.RANGES) | {"background", "colorA", "colorB", "mood", "rootNote", "glow"}
        missing = sorted(expected - set(preset))
        assert not missing, f"TODO 2: the preset is missing: {missing}"
        assert preset["mood"] in gen.MOODS, f"TODO 2: mood should come from MOODS, got {preset['mood']!r}."
        assert preset["rootNote"] in gen.ROOT_NOTES, f"TODO 2: rootNote should come from ROOT_NOTES, got {preset['rootNote']!r}."
        assert preset["glow"] is True, "TODO 2: set preset['glow'] = True"

    def test_values_are_in_range(self):
        gen = load_module("project3_aurora/server/generator.py")
        for _ in range(30):
            preset = call(gen.random_preset)
            for key, (low, high) in gen.RANGES.items():
                value = preset.get(key)
                assert isinstance(value, (int, float)) and low <= value <= high, (
                    f"TODO 2: {key} should be between {low} and {high}, got {value!r}."
                )
                if isinstance(low, int):
                    assert isinstance(value, int), (
                        f"TODO 2: {key} should be a whole number (got {value!r}). Use random.randint for int ranges."
                    )
