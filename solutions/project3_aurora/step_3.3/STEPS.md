# 🌌 Project 3: The Flow-Field Aurora  ✅ SOLVED THROUGH STEP 3.3

You're going to build a living, glowing, musical aurora that runs in your web browser.
Thousands of particles drift on invisible wind, the music follows the wind, and you get
a settings menu to play with everything.

Every step adds something you can **see or hear** right away. ✨

---

## 🚀 How to run it

1. In the terminal (with your virtual environment active, like in Projects 1 and 2):

   ```
   python solutions/project3_aurora/step_3.3/server/main.py
   ```

2. A browser tab opens at **http://localhost:8000**. (If it doesn't, open it yourself.)
3. Leave the server running while you work. After you change a file:
   - **JavaScript / HTML file** (in `web/`): save, then **refresh the browser** (Ctrl+R on Windows/Linux, Cmd+R on Mac).
   - **Python file** (in `server/`): just save. The server restarts by itself.
4. Stop the server with **Ctrl+C** in the terminal.

The **✅ Self-check** panel in the top-left corner ticks off each step as you finish it
and gives you a hint for the next one. Press **C** to hide or show it.

🐛 If you make a typo in JavaScript, a **red banner** appears at the top of the page telling you
which file and line to look at.

## 🗺️ The files

```
project3_aurora/
├── STEPS.md          ← you are here
├── server/           🐍 Python
│   ├── main.py         the web server + presets API          (step 3.8)
│   ├── generator.py    the "Surprise me" generator            (step 3.9)
│   └── presets/        saved looks, as .json files
└── web/              🌐 the web page
    ├── index.html      what's on the page                     (⭐ 3.10)
    ├── params.js       all the knobs                          (step 3.1)
    ├── sketch.js       the particles and the wind             (3.2, 3.3, 3.4, ⭐ 3.11, ⭐ 3.12)
    ├── sound.js        the music                              (3.5, 3.6, ⭐ 3.11)
    ├── settings.js     the settings menu                      (3.7)
    ├── my_panel.js     your hand-made sliders                 (⭐ 3.10)
    └── (style.css, toolbar.js, selfcheck.js, errors.js are already done. Peek if you're curious!)
```

> 🐍 → 🟨 Python and JavaScript are cousins. Keep **docs/python-to-js-cheatsheet.md** open next to you!

---

## 3.1 🎨 Make it yours
**File:** `web/params.js`

`PARAMS` holds every choice the Aurora makes. Change the `title`, the `background`
color, and the two particle colors, `colorA` and `colorB`, then save and refresh.

**You'll see:** your title at the bottom of the screen and your sky color. (The particles come next!)

💡 Colors are hex codes like `"#ff8800"`. Search "color picker" in your browser to find ones you love.

---

## 3.2 ✨ A sky full of particles
**File:** `web/sketch.js` (search for `STEP 3.2`)

Make a particle (an object with `x`, `y`, `vx`, `vy`), fill the `particles` array with lots of
them, and draw each one as a dot.

**You'll see:** a sky full of stars. ⭐

💡 Hints
- `return { x: random(width), y: random(height), vx: 0, vy: 0 };`
- A JavaScript `for` loop: `for (let i = 0; i < PARAMS.particleCount; i++) { ... }`
- `.push()` is JavaScript's `.append()`.

🎛️ **Play:** change `particleCount` and `particleSize` in `params.js`.

---

## 3.3 🌬️ The flow field
**File:** `web/sketch.js` (search for `STEP 3.3`)

This is the big one, and the most magical. Each particle asks the invisible wind
"which way should I go?", takes a small step that way, and wraps around the screen edges.
Then you make the background **see-through** so particles leave silky trails.

**You'll see:** the stars come alive and flow like silk. 🤩

💡 Hints
- The recipe for each line is in the comments. Take them one at a time.
- `wrapAround` needs four `if`s: one for each edge.
- Trails come from `sky.setAlpha(PARAMS.trailFade)`. A see-through background only *partly* covers the last frame.

🎛️ **Play:** `speed`, `swirl`, `noiseScale` and `trailFade`. Try `swirl: 8` or `noiseScale: 0.02`!

---

## 3.4 🌈 Color & glow
**File:** `web/sketch.js` (search for `STEP 3.4`)

Blend from `colorA` at the top to `colorB` at the bottom with `lerpColor`, and turn on
glowing light with `blendMode(ADD)`.

**You'll see:** a real aurora: colors that shift down the screen and glow where particles bunch up.

💡 `p.y / height` is 0 at the top and 1 at the bottom. That's exactly what `lerpColor` wants!

---

## 3.5 🎹 Make some music
**File:** `web/sound.js` (search for `STEP 3.5`)

Create a synth and a loop that plays a new chord every few seconds.

**You'll hear:** press **🔊 Start sound**, and soft dreamy chords begin.

💡 The synth recipe is in the comments. For the loop:
`chordLoop = new Tone.Loop(playNextChord, PARAMS.chordSeconds).start(0);`

🎛️ **Play:** `mood` ("dreamy", "mysterious", "hopeful"), `rootNote`, `chordSeconds`, `reverb`.
Try `"fatsawtooth"` instead of `"fatsine"`!

---

## 3.6 🌬️🎶 Let the wind play the music
**File:** `web/sound.js` (search for `STEP 3.6`)

Use `map()` to turn the wind's direction into the filter's brightness. Now the music
follows what you see.

**You'll hear:** the chords get brighter when the wind blows right and mellower when it blows left.
(It changes slowly, so give it 10–20 seconds.)

💡 `const cutoff = map(flowX, -1, 1, 300, PARAMS.brightness);`
then `filter.frequency.rampTo(cutoff, 0.3);`

---

## 3.7 🎛️ Settings menu
**File:** `web/settings.js`

Build a menu with lil-gui so you can change every knob live, no refreshing needed.

**You'll see:** a ⚙️ Settings panel in the top-right corner, full of sliders, color pickers and checkboxes.

💡 Start by un-commenting the two example lines, then add one line per knob.
Folders keep it tidy: `const look = gui.addFolder("🎨 Look");`

---

## 3.8 💾 Presets API (back to Python! 🐍)
**File:** `server/main.py`

Write the three functions that list, load, and save presets as JSON files, just like the
Spell Book in exercise 2.4.

**Check it:** `python check.py 3.8`

**You'll see:** the **📂 Load** menu fills up with presets, and **💾 Save** stores your favorite looks.

💡 Bonus: visit **http://localhost:8000/docs**. FastAPI built an instruction page for your API, where you can try each URL!

---

## 3.9 🎲 Surprise me!
**File:** `server/generator.py`

Write Python that invents a random color palette and random knob values.

**Check it:** `python check.py 3.9`

**You'll see:** **🎲 Surprise me** gives a brand-new Aurora every click. Save the ones you love!

---

## ⭐ Bonus steps

### ⭐ 3.10 🎚️ Your own sliders
**Files:** `web/index.html` (the `my-panel` div) and `web/my_panel.js`

Build sliders by hand, the way websites do it: HTML for the slider, JavaScript to listen to it.

### ⭐ 3.11 🪄 Wand mode
**Files:** `web/sketch.js` (`applyWand`) and `web/sound.js` (`playSparkle`)

Hold the mouse down on the Aurora to push particles away and play sparkly notes.
Higher on the screen = higher notes.

### ⭐ 3.12 📸 Snapshots & shortcuts
**File:** `web/sketch.js` (`keyPressed`)

Press **S** to save a picture, **F** for fullscreen, **Space** to pause, **R** to wipe the sky.

---

## 🆘 Stuck?

- **Nothing changed?** Did you save the file *and* refresh the browser?
- **Red banner?** It shows the file and line number. Look there (and the line just above it) for a missing `)`, `}` or `,`.
- **Blank screen, no banner?** Open the browser's Developer Tools (F12, or Cmd+Option+J on a Mac) and check the **Console** tab.
- **"Can't reach the server"?** Is the terminal still running `main.py`? Start it again.
- **Port already in use?** Run `python solutions/project3_aurora/step_3.3/server/main.py --port 8001` and open http://localhost:8001.
- **No sound?** Press 🔊 Start sound (browsers need a click first), check your volume, and finish step 3.5.
- **Slow / choppy?** Lower `particleCount`.
