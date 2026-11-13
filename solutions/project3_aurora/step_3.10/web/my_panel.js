/*
═══════════════════════════════════════════════════════════════════════
  ⭐ BONUS STEP 3.10 — my_panel.js: BUILD YOUR OWN SLIDERS 🎚️  ✅ SOLVED THROUGH STEP 3.10
═══════════════════════════════════════════════════════════════════════

lil-gui built a menu for you. Now build one BY HAND, the way websites
do it: an HTML slider (in index.html) + JavaScript that listens to it.

  1. In index.html, find the <div id="my-panel"> and add sliders there.
     A slider looks like this:

        <label>Speed <input id="speed-slider" type="range" min="0.1" max="6" step="0.1"></label>

  2. Here, finish connectSlider(), then call it once per slider in
     setupMyPanel().

🧰 Tools:
   document.getElementById("speed-slider")   finds the element with that id
   slider.value                              the slider's value (as TEXT!)
   Number("2.5")                             turns text into a number: 2.5
   slider.addEventListener("input", () => { ... })
                                             runs the { ... } every time the slider moves
   PARAMS[param]                             reads a knob by name, e.g. PARAMS["speed"]
*/

// Hooks up the slider with this id to the PARAMS knob called `param`.
function connectSlider(id, param) {
  const slider = document.getElementById(id);
  if (!slider) {
    toast(`🔍 There's no element with id="${id}" in index.html`);
    return;
  }
  slider.value = PARAMS[param];   // start the slider at the knob's current value

  // ✏️ TODO A: when the slider moves, set PARAMS[param] to the slider's
  //            value (as a Number!), then call refreshSettings() so the
  //            ⚙️ menu shows the new value too.
  slider.addEventListener("input", () => {
    PARAMS[param] = Number(slider.value);
    refreshSettings();
  });
}

function setupMyPanel() {
  // ✏️ TODO B: connect each of your sliders, like:
  //            connectSlider("speed-slider", "speed");
  connectSlider("speed-slider", "speed");
  connectSlider("swirl-slider", "swirl");
  connectSlider("size-slider", "particleSize");

  // 🔧 Only show the panel once it has something in it.
  const panel = document.getElementById("my-panel");
  panel.hidden = panel.querySelector("input") === null;
}
