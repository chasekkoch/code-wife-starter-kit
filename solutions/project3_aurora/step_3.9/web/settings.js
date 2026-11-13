/*
═══════════════════════════════════════════════════════════════════════
  PROJECT 3 — settings.js: THE SETTINGS MENU 🎛️  ✅ SOLVED THROUGH STEP 3.9
═══════════════════════════════════════════════════════════════════════

✏️ STEP 3.7 — Build a settings menu for every knob in PARAMS.

This uses lil-gui, a tiny library that turns an object's values into
sliders, checkboxes, color pickers and dropdowns. You just tell it
WHICH object and WHICH key, and it does the rest:

  gui.add(PARAMS, "speed", 0, 5)          a slider from 0 to 5
  gui.add(PARAMS, "trailFade", 1, 100, 1) a slider that moves in steps of 1
  gui.add(PARAMS, "glow")                 true/false becomes a checkbox
  gui.add(PARAMS, "mood", ["a", "b"])     a list becomes a dropdown
  gui.addColor(PARAMS, "colorA")          a color picker

You can group controls into folders:
  const look = gui.addFolder("🎨 Look");
  look.add(PARAMS, "particleSize", 0.5, 5);

Some knobs need a nudge after they change:
  .onChange(showTitle)               run showTitle every time it changes
  .onFinishChange(createParticles)   run createParticles when you let go
  .name("Pretty label")              change the label

🧰 Remember the music needs applySoundSettings() after a music knob changes.
   And Object.keys(MOODS) is the list of mood names from sound.js.
*/

let gui;   // the settings menu

function setupSettings() {
  gui = new lil.GUI({ title: "⚙️ Settings" });
  gui.add(PARAMS, "title").onChange(showTitle);

  const look = gui.addFolder("🎨 Look");
  look.addColor(PARAMS, "background");
  look.addColor(PARAMS, "colorA").name("top color");
  look.addColor(PARAMS, "colorB").name("bottom color");
  look.add(PARAMS, "particleCount", 100, 5000, 100).onFinishChange(createParticles);
  look.add(PARAMS, "particleSize", 0.5, 6);
  look.add(PARAMS, "particleAlpha", 5, 255, 1).name("brightness");
  look.add(PARAMS, "trailFade", 1, 100, 1);
  look.add(PARAMS, "glow");

  const wind = gui.addFolder("🌬️ Wind");
  wind.add(PARAMS, "speed", 0.1, 6);
  wind.add(PARAMS, "noiseScale", 0.0005, 0.02).name("pattern zoom");
  wind.add(PARAMS, "noiseSpeed", 0, 0.02).name("pattern change");
  wind.add(PARAMS, "swirl", 0.5, 8);

  const music = gui.addFolder("🎵 Music");
  music.add(PARAMS, "volume", -40, 0, 1).onChange(applySoundSettings);
  music.add(PARAMS, "mood", Object.keys(MOODS));
  music.add(PARAMS, "rootNote", ["C3", "D3", "E3", "F3", "G3", "A3"]);
  music.add(PARAMS, "chordSeconds", 1, 10).onFinishChange(applySoundSettings);
  music.add(PARAMS, "reverb", 1, 20).onFinishChange(applySoundSettings);
  music.add(PARAMS, "brightness", 300, 8000, 100);

  gui.add(PARAMS, "showSelfCheck").name("✅ self-check").listen();
}

// 🔧 Already done: makes the menu show the newest values (used when loading a preset).
function refreshSettings() {
  if (gui) gui.controllersRecursive().forEach(c => c.updateDisplay());
}
