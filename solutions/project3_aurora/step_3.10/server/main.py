"""
═══════════════════════════════════════════════════════════════════════
  PROJECT 3 — The Aurora Server 🌌🐍  ✅ SOLVED THROUGH STEP 3.10
═══════════════════════════════════════════════════════════════════════

This little Python program is a WEB SERVER. It does two jobs:
  1. It sends the Aurora web page (everything in ../web) to your browser.
  2. It has an API (a menu of URLs that answer with data instead of a page)
     so the Aurora can SAVE and LOAD your favorite looks, called PRESETS.

Presets are just JSON files in server/presets/ (just like the Spell Book
in exercise 2.4!).

▶️ RUN IT        python solutions/project3_aurora/step_3.10/server/main.py
                 (then open http://localhost:8000 if it doesn't open by itself)
                 Stop it with Ctrl+C.
🔁 The server restarts by itself whenever you save this file.
📖 Bonus: visit http://localhost:8000/docs to see and try your API in the browser!

✏️ You only touch this file in STEP 3.8. See STEPS.md for the full guide.
"""

import argparse
import json
import re
import threading
import webbrowser
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from generator import random_preset

HERE = Path(__file__).resolve().parent
WEB_DIR = HERE.parent / "web"
PRESETS_DIR = HERE / "presets"

app = FastAPI(title="✨ Aurora Server", description="Save and load Aurora presets.")


def preset_path(name):
    """✅ Already done. Turns a preset name like "Lavender Haze" into a safe
    file path like presets/lavender_haze.json (and blocks sneaky names)."""
    safe_name = re.sub(r"[^a-z0-9]+", "_", name.strip().lower()).strip("_")
    if not safe_name:
        raise HTTPException(status_code=400, detail="Please give the preset a name with some letters in it!")
    return PRESETS_DIR / f"{safe_name}.json"


# ═════════════════════════════════════════════════════════════════════
# ✏️ STEP 3.8 — The Presets API
#
# Each function below is connected to a URL by the @app.get / @app.post
# line above it (that's called a DECORATOR). Whatever the function returns
# gets sent back to the browser as JSON. Python lists and dicts work great.
#
# 🧰 Tools in your toolbelt:
#     PRESETS_DIR.glob("*.json")   every .json file in the presets folder
#     path.stem                    a file's name without .json
#     sorted(...)                  sorts a list (or anything loop-able!)
#     path.exists()                True if the file is there
#     path.read_text(encoding="utf-8")         the file's text
#     path.write_text(text, encoding="utf-8")  saves text into the file
#     json.loads(text) / json.dumps(data, indent=2)   text <-> dict
#     raise HTTPException(status_code=404, detail="...")   "not found!"
# ═════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 1: Return a sorted list of every preset's NAME (the file name
#            without .json), e.g. ["fortune_cookie_gold", "lavender_haze"]
# ─────────────────────────────────────────────────────────────────────
@app.get("/api/presets")
def list_presets():
    return sorted(path.stem for path in PRESETS_DIR.glob("*.json"))


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 2: Return the preset called `name` as a dictionary.
#            If there's no such file, raise a 404 HTTPException.
#            (preset_path(name) gives you the file's path.)
# ─────────────────────────────────────────────────────────────────────
@app.get("/api/presets/{name}")
def get_preset(name: str):
    path = preset_path(name)
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"There's no preset called '{name}'.")
    return json.loads(path.read_text(encoding="utf-8"))


# ─────────────────────────────────────────────────────────────────────
# ✏️ TODO 3: Save `preset` (a dictionary sent by the browser) as JSON
#            into the file for `name`, then return {"saved": path.stem}
# ─────────────────────────────────────────────────────────────────────
@app.post("/api/presets/{name}")
def save_preset(name: str, preset: dict):
    path = preset_path(name)
    path.write_text(json.dumps(preset, indent=2), encoding="utf-8")
    return {"saved": path.stem}


# ═════════════════════════════════════════════════════════════════════
# 🎲 STEP 3.9 happens in generator.py. This URL is already wired up to it.
# ═════════════════════════════════════════════════════════════════════
@app.get("/api/random-preset")
def surprise_me():
    preset = random_preset()
    if preset is None:
        raise HTTPException(status_code=501, detail="Not built yet. Finish STEP 3.9 in generator.py!")
    return preset


# ═════════════════════════════════════════════════════════════════════
# 🔧 Plumbing. No changes needed below!
# ═════════════════════════════════════════════════════════════════════
@app.middleware("http")
async def always_fresh(request, call_next):
    """Tell the browser never to cache, so a refresh always shows your newest code."""
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    return response


PRESETS_DIR.mkdir(exist_ok=True)
app.mount("/", StaticFiles(directory=WEB_DIR, html=True), name="web")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Aurora server.")
    parser.add_argument("--port", type=int, default=8000, help="which port to use (default 8000)")
    parser.add_argument("--no-browser", action="store_true", help="don't open a browser tab")
    args = parser.parse_args()

    url = f"http://localhost:{args.port}"
    print(f"\n🌌 The Aurora is live at {url}   (press Ctrl+C to stop)\n")
    if not args.no_browser:
        threading.Timer(1.5, lambda: webbrowser.open(url)).start()
    uvicorn.run("main:app", host="127.0.0.1", port=args.port, reload=True,
                app_dir=str(HERE), reload_dirs=[str(HERE)], log_level="warning")
