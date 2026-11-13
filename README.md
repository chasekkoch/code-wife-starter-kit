# 💻✨ Code Wife Starter Kit

### For Birdie 🐦

A gentle, date-night-sized introduction to programming. No experience needed, ever.
You'll go from your very first line of code to a glowing, musical, interactive
**Aurora** in your web browser that *you* built. Along the way: cats 🐈, Chinese takeout 🥡,
Taylor Swift 🎤, and Harry Potter ⚡.

Every exercise is already set up. You never have to create files or folders or make
setup decisions. Just open a file, read the friendly comments, fill in the `TODO`s,
and **run it to see something happen right away**.

---

## 📚 Table of contents

1. [The roadmap](#-the-roadmap)
2. [One-time setup](#-one-time-setup) ([Windows](#-windows-11) · [macOS](#-macos) · [Linux](#-linux))
3. [How every exercise works](#-how-every-exercise-works)
4. [Project 3: running the Aurora](#-project-3-running-the-aurora)
5. [Save points with git](#-save-points-with-git)
6. [Tips for a happy date night](#-tips-for-a-happy-date-night)
7. [Troubleshooting](#-troubleshooting)
8. [Coach's corner (for the helper)](#-coachs-corner-for-the-helper)

---

## 🧭 The roadmap

Three projects, each a little bigger than the last. ⭐ = optional bonus. Skip them freely, or come back later.

### Project 1: The Basics 🐣 (Python)
*Variables, printing, math, decisions, loops, and drawing.*

| # | Exercise | You'll learn | You'll see |
|---|---|---|---|
| 1.1 | Hello, Birdie | `print`, variables, f-strings | a personalized greeting |
| 1.2 | Takeout Bill Splitter 🥡 | math, functions, `return` | a receipt for your takeout order |
| 1.3 | The Sorting Hat ⚡ | `if` / `elif` / `else` | a quiz that sorts you into a house |
| 1.4 | The Eras Spiral 🎤 | `for` loops, lists | a colorful spiral drawn by a turtle 🐢 |
| ⭐1.5 | Fortune Cookie 🥠 | `random`, `while` loops | your fortune and lucky numbers |
| ⭐1.6 | Cat Quilt 🐈 | nested loops | a quilt of cat faces |

### Project 2: Puzzles & Power Tools 🧩 (Python)
*Dictionaries, list tricks, classes, files, and handling errors.*

| # | Exercise | You'll learn | You'll see |
|---|---|---|---|
| 2.1 | Eras Tour Stats 🎤 | lists of dictionaries, counting | fun stats about every album |
| 2.2 | Takeout Menu Wizard 🥡 | filtering and sorting | an interactive ordering wizard |
| 2.3 | Cat Café 🐈 | classes (`dataclass`) | a little game: keep 4 cats happy |
| 2.4 | Spell Book ⚡ | JSON files, `try` / `except` | a spell book you can cast from and add to |
| ⭐2.5 | Palette Potion 🎨 | colors as numbers | a generated color palette |
| ⭐2.6 | Marauder's Map 🗺️ | comprehensions, animation | an animated map with footsteps |

### Project 3: The Flow-Field Aurora 🌌 (JavaScript + Python)
*A real web app: graphics with p5.js, music with Tone.js, a settings menu, and a Python web server.*

| # | Step | You'll see / hear |
|---|---|---|
| 3.1 | Make it yours | your title and colors |
| 3.2 | A sky full of particles | a starfield |
| 3.3 | The flow field | stars that flow like silk ✨ |
| 3.4 | Color & glow | a real glowing aurora |
| 3.5 | Make some music | dreamy chords 🎹 |
| 3.6 | Let the wind play | music that follows the visuals |
| 3.7 | Settings menu | sliders and color pickers for everything |
| 3.8 | Presets API 🐍 | save and load your favorite looks |
| 3.9 | Surprise me! 🐍 | a random new Aurora on every click |
| ⭐3.10 | Your own sliders | sliders you built by hand |
| ⭐3.11 | Wand mode 🪄 | push particles with the mouse and play sparkles |
| ⭐3.12 | Snapshots & shortcuts 📸 | save pictures, go fullscreen |

---

## 🧰 One-time setup

You'll install four things, then set up the project once. Pick your operating system below.

**What you need:**

| Tool | What it is |
|---|---|
| **Python 3.10 or newer** (3.12+ recommended) | the programming language |
| **Visual Studio Code** (VS Code) | the app you write code in |
| **git** | saves your progress ("save points") and downloads this project |
| **A modern browser** (Chrome, Edge, Firefox or Safari) | for Project 3 |

> 💡 **What's a terminal?** It's a window where you type commands instead of clicking.
> The easiest one to use is **inside VS Code**: menu **Terminal → New Terminal**.
> When this guide shows a command in a gray box, type it there and press **Enter**.

### 🪟 Windows 11

1. **Install Python** from [python.org/downloads](https://www.python.org/downloads/).
   - ⚠️ On the first installer screen, **tick "Add python.exe to PATH"**, then click *Install Now*.
2. **Install VS Code** from [code.visualstudio.com](https://code.visualstudio.com/).
3. **Install git** from [git-scm.com/download/win](https://git-scm.com/download/win) (the default options are fine).
4. **Close and re-open** any terminals so they notice the new installs, then check:
   ```powershell
   python --version
   git --version
   ```
   You should see `Python 3.1x.x` and `git version ...`.
   - If `python` opens the Microsoft Store instead, use `py` in place of `python` for step 6, or turn off
     *Settings → Apps → Advanced app settings → App execution aliases → python.exe*.
5. **Download the project** (pick a folder you like, e.g. Documents):
   ```powershell
   cd $HOME\Documents
   git clone https://github.com/chasekkoch/code-wife-starter-kit.git
   cd code-wife-starter-kit
   code .
   ```
   (`code .` opens the folder in VS Code. You can also use *File → Open Folder…*.)
6. **In VS Code's terminal**, create the project's private Python toolbox (a "virtual environment"):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
   - 🛑 If you see *"running scripts is disabled on this system"*, run this once, then try `Activate.ps1` again:
     ```powershell
     Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
     ```
   - ✅ When it works, your terminal line starts with **`(.venv)`**.

### 🍎 macOS

1. **Install Python** from [python.org/downloads](https://www.python.org/downloads/) (the macOS installer).
   - Use the python.org installer rather than Homebrew: it includes everything the turtle drawings need.
     (Using Homebrew Python anyway? Also run `brew install python-tk`.)
2. **Install VS Code** from [code.visualstudio.com](https://code.visualstudio.com/). Drag it into *Applications*.
   - Then open VS Code, press **Cmd+Shift+P**, type `shell command`, and choose
     **"Shell Command: Install 'code' command in PATH"**.
3. **Install git**: open the **Terminal** app and run `git --version`.
   If git isn't installed, macOS offers to install the *Command Line Developer Tools*. Click **Install**.
4. **Check** in Terminal:
   ```bash
   python3 --version
   git --version
   ```
5. **Download the project**:
   ```bash
   cd ~/Documents
   git clone https://github.com/chasekkoch/code-wife-starter-kit.git
   cd code-wife-starter-kit
   code .
   ```
6. **In VS Code's terminal** (*Terminal → New Terminal*):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
   ✅ Your terminal line now starts with **`(.venv)`**. While it's active, plain `python` works (no `3` needed).

### 🐧 Linux

1. **Install Python, venv, the turtle graphics library (Tk), and git.** On Ubuntu / Debian / Mint:
   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-tk git
   ```
   - Fedora: `sudo dnf install python3 python3-tkinter git`
   - Arch: `sudo pacman -S python tk git`
2. **Install VS Code** from [code.visualstudio.com](https://code.visualstudio.com/) (.deb / .rpm), or via snap: `sudo snap install code --classic`.
3. **Download the project and set it up:**
   ```bash
   cd ~
   git clone https://github.com/chasekkoch/code-wife-starter-kit.git
   cd code-wife-starter-kit
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   code .
   ```

### 🧩 Finish setting up VS Code (all systems)

1. When VS Code asks *"Do you want to install the recommended extensions?"*, click **Install**. You'll get:
   - **Python** + **Pylance**: run buttons, autocomplete, and spotting mistakes
   - **Error Lens**: shows mistakes right on the line where they happen
2. Press **Ctrl+Shift+P** (Windows/Linux) or **Cmd+Shift+P** (Mac), type **Python: Select Interpreter**,
   and pick the one that mentions **`.venv`**.
3. Make sure everything works:
   ```bash
   python check.py
   ```
   You should see your **🌟 Progress Board**. 🎉 Setup is done, forever!

> 🔁 **Every time you come back:** open the folder in VS Code and open a terminal. VS Code usually
> activates `(.venv)` for you. If the terminal line doesn't start with `(.venv)`, run
> `.venv\Scripts\Activate.ps1` (Windows) or `source .venv/bin/activate` (Mac/Linux).

---

## 🎯 How every exercise works

All your work happens in the **`exercises/`** folder.

1. **Open the exercise file**, e.g. `exercises/project1_basics/ex1_1_hello_birdie.py`.
2. **Read the big comment at the top.** It explains the goal, your 🧰 toolbelt, and hints.
3. **Find each `✏️ TODO`** and write your code there.
4. **Run it** to see what happens. Either click the ▶️ button in VS Code's top-right corner, or:
   ```bash
   python exercises/project1_basics/ex1_1_hello_birdie.py
   ```
5. **Check it:**
   ```bash
   python check.py 1.1
   ```
   You'll get ✅ for each part that's right, and a 💡 hint for each part that isn't yet.
6. **Celebrate** 🎉, make a [save point](#-save-points-with-git), and move on!

| Command | What it does |
|---|---|
| `python check.py` | shows your 🌟 Progress Board |
| `python check.py 1.3` | checks exercise 1.3 |
| `python check.py 2` | checks all of Project 2 |

> 💡 Hints in the comments get more specific as you go. Peek at only one at a time!
> 🐛 Typo? `check.py` points you to the exact line, with tips for the usual suspects.

---

## 🌌 Project 3: running the Aurora

Project 3 is a real web app: a **Python server** sends a **web page** to your browser.

```bash
python exercises/project3_aurora/server/main.py
```

- Your browser opens **http://localhost:8000** automatically. (If not, open it yourself.)
- Keep the terminal running while you work. Stop it with **Ctrl+C**.
- After editing a **JavaScript/HTML** file: save, then **refresh** the browser (Ctrl+R / Cmd+R).
- After editing a **Python** file: just save. The server restarts by itself.
- 🔊 Browsers only play sound after you click, so press **Start sound** in the toolbar.
- ✅ The **Self-check** panel in the corner ticks off each step. Press **C** to hide or show it.
- 📖 The step-by-step guide is **`exercises/project3_aurora/STEPS.md`**.
  (In VS Code, right-click it → *Open Preview* to read it nicely.)
- 🐍→🟨 Keep the **[Python → JavaScript cheat sheet](docs/python-to-js-cheatsheet.md)** handy.

**Port 8000 already in use?** Use another one:
`python exercises/project3_aurora/server/main.py --port 8001`

### 📴 Offline mode (optional)

The Aurora loads three free libraries from the internet (p5.js, Tone.js and lil-gui).
To work without internet (on a plane, say), download them once, from the project folder:

**Mac / Linux:**
```bash
mkdir -p exercises/project3_aurora/web/vendor
cd exercises/project3_aurora/web/vendor
curl -L -o p5.min.js https://cdn.jsdelivr.net/npm/p5@1.11.13/lib/p5.min.js
curl -L -o Tone.js https://cdn.jsdelivr.net/npm/tone@15.1.22/build/Tone.js
curl -L -o lil-gui.umd.min.js https://cdn.jsdelivr.net/npm/lil-gui@0.21.0/dist/lil-gui.umd.min.js
```

**Windows (PowerShell):**
```powershell
mkdir exercises\project3_aurora\web\vendor
cd exercises\project3_aurora\web\vendor
curl.exe -L -o p5.min.js https://cdn.jsdelivr.net/npm/p5@1.11.13/lib/p5.min.js
curl.exe -L -o Tone.js https://cdn.jsdelivr.net/npm/tone@15.1.22/build/Tone.js
curl.exe -L -o lil-gui.umd.min.js https://cdn.jsdelivr.net/npm/lil-gui@0.21.0/dist/lil-gui.umd.min.js
```

Then in `exercises/project3_aurora/web/index.html`, change the three library `<script>` lines to:

```html
<script src="vendor/p5.min.js"></script>
<script src="vendor/Tone.js"></script>
<script src="vendor/lil-gui.umd.min.js"></script>
```

(The `vendor/` folder is git-ignored, so it won't clutter your save points.)

---

## 💾 Save points with git

Think of git like save points in a video game. Make one every time an exercise works!

```bash
git add -A
git commit -m "Finished 1.2, the bill splitter!"
```

| I want to... | Command |
|---|---|
| see what I've changed since my last save | `git status` |
| see all my save points | `git log --oneline` |
| undo my changes to one file (back to the last save point) | `git restore path/to/file.py` |
| see exactly what changed in a file | in VS Code, click the **Source Control** icon (the branch shape) on the left |

> 💡 The first time you commit, git may ask who you are. Run these once (with your own name and email):
> ```bash
> git config --global user.name "Birdie"
> git config --global user.email "you@example.com"
> ```

---

## 💕 Tips for a happy date night

- **Bite-size sessions.** One or two exercises a night is perfect. Stop while it's still fun.
- **Read the comments out loud** together. They're written to be read, not skimmed.
- **Errors are normal!** Professional programmers see red error messages all day. An error is just the computer saying "I didn't understand, can you rephrase?" Read the *last* line of the message first.
- **Run your code often**, even half-finished. Every exercise is built to run without crashing, even before you're done.
- **Play with the knobs.** Every exercise has numbers and colors to tweak. Change them just to see what happens; you can't break anything.
- **Bonuses ⭐ are truly optional.** Skip them, come back later, or never. Totally fine.
- **Coaches: hands off the keyboard!** 🙌 Ask questions ("what do you think `for` does here?") instead of giving answers.

A possible pace (go faster or slower as you like):

| Session | Exercises |
|---|---|
| 1 | Setup + 1.1, 1.2 |
| 2 | 1.3, 1.4 (+ ⭐1.5, ⭐1.6) |
| 3 | 2.1, 2.2 |
| 4 | 2.3, 2.4 (+ ⭐2.5, ⭐2.6) |
| 5 | 3.1 – 3.4 (the Aurora comes alive!) |
| 6 | 3.5 – 3.7 (music + settings) |
| 7 | 3.8 – 3.9 (+ ⭐ 3.10 – 3.12) |

---

## 🆘 Troubleshooting

| Problem | Fix |
|---|---|
| `python` is not recognized (Windows) | Re-install Python with **"Add python.exe to PATH"** ticked, or use `py` instead of `python`. Close and re-open the terminal. |
| `python: command not found` (Mac/Linux) | Use `python3`, or activate the venv (`source .venv/bin/activate`). Then `python` works. |
| `ModuleNotFoundError: No module named 'rich'` (or fastapi, pytest…) | The venv isn't active. Activate it (see [Every time you come back](#-finish-setting-up-vs-code-all-systems)), then `pip install -r requirements.txt` if needed. |
| "running scripts is disabled" (Windows) | `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |
| VS Code's ▶️ button uses the wrong Python | **Ctrl/Cmd+Shift+P → Python: Select Interpreter →** the `.venv` one. |
| Turtle window: `No module named '_tkinter'` | Linux: `sudo apt install python3-tk`. Mac + Homebrew Python: `brew install python-tk`. |
| Turtle window doesn't appear | Check behind VS Code. It sometimes opens underneath! |
| Emojis look like boxes in the terminal (Windows) | Use VS Code's terminal or **Windows Terminal** (not the old Command Prompt). |
| Aurora page says "can't reach the server" | Is `main.py` still running in the terminal? Start it again. |
| `address already in use` | Another server is running. Stop it (Ctrl+C) or use `--port 8001`. |
| Aurora shows a red 🐛 banner | It names the file and line. Look there (and the line above) for a missing `)`, `}` or `,`. |
| Aurora page is blank, no banner | Open DevTools (F12, or Cmd+Option+J on a Mac) → **Console** for details. Also check your internet (or use [offline mode](#-offline-mode-optional)). |
| No sound | Click **🔊 Start sound**, check the volume, and finish step 3.5. Safari: also make sure the tab isn't muted. |
| The Aurora is slow | Lower `particleCount` in the ⚙️ Settings or in `params.js`. |
| I messed up a file and want to start it over | `git restore path/to/file` (back to your last save point), or copy the original from GitHub. |

---

## 🧑‍🏫 Coach's corner (for the helper)

### Solutions
**`solutions/`** mirrors `exercises/` with every `TODO` filled in. Use it to compare results,
not to copy from. 😉

- Check that all solutions pass: `python check.py --solutions`
- Run a solution: `python solutions/project1_basics/ex1_3_sorting_hat.py`
- **Compare her file with the solution in VS Code:** right-click her file → **Select for Compare**,
  then right-click the solution → **Compare with Selected**. Or from a terminal:
  `code --diff exercises/project1_basics/ex1_2_bill_splitter.py solutions/project1_basics/ex1_2_bill_splitter.py`

### Project 3 step snapshots
Project 3 builds up over many steps, so `solutions/project3_aurora/` has a **snapshot after every step**:
`step_3.1/` (only 3.1 solved) … `step_3.12/` (everything solved). Compare her project with the
snapshot for the step she's on, or run one to show what's coming next:

```bash
python solutions/project3_aurora/step_3.4/server/main.py --port 8001
```

(Using a different port lets you run it next to hers.)

### How the kit is built (maintainers)
Exercises and solutions are **generated** from one set of templates, so they never drift apart.

- Source of truth: **`tools/templates/`**. Each file has blocks like:
  ```python
  # <<SOLVE        (Project 3 uses step numbers, e.g.  // <<SOLVE 3.4)
  solved code
  # ==STUB
  starter code
  # >>END
  ```
  Comments outside the blocks appear in both versions.
- Rebuild **solutions** after editing a template: `python tools/build.py`
- Rebuild **exercises** too: `python tools/build.py --exercises`
  ⚠️ This **erases all learner work** in `exercises/` (it asks you to type `reset` first).
- Tests live in `tests/`, and their failure messages are the learner's hints.
  Run them against the solutions with:
  - Mac/Linux: `CODE_KIT_TARGET=solutions python -m pytest`
  - Windows: `$env:CODE_KIT_TARGET="solutions"; python -m pytest`
  - Project 3 snapshot tests: also set `CODE_KIT_P3_STEP=step_3.8` (default `step_3.12`).
- Project 3's browser steps are checked live by `web/selfcheck.js`.

### Why these tools?
- **Python** first: it reads almost like English, and it's used everywhere.
- **p5.js**: made for artists and beginners; beautiful results with tiny amounts of code.
- **Tone.js**: real music theory (chords, scales, reverb) in a few lines.
- **lil-gui**: a polished settings menu in one line per knob.
- **FastAPI**: a modern Python web server, so Project 3 ties back to the Python she learned.

### Content note
Themes use names, titles and facts only. No song lyrics or book text are included.
