/*
═══════════════════════════════════════════════════════════════════════
  PROJECT 3 — settings.js: THE SETTINGS MENU 🎛️  ✅ SOLVED THROUGH STEP 3.3
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
  // ✏️ TODO A: create the menu. Un-comment the next line (delete the //), save, refresh!
  // gui = new lil.GUI({ title: "⚙️ Settings" });

  // ✏️ TODO B: a box to edit your title. (Un-comment this too.)
  // gui.add(PARAMS, "title").onChange(showTitle);

  // ✏️ TODO C: a "🎨 Look" folder with background, colorA, colorB,
  //            particleCount, particleSize, particleAlpha, trailFade, glow.
  //            (particleCount needs .onFinishChange(createParticles))

  // ✏️ TODO D: a "🌬️ Wind" folder with speed, noiseScale, noiseSpeed, swirl.
  //    💡 tiny numbers need tiny ranges: noiseScale works from 0.0005 to 0.02

  // ✏️ TODO E: a "🎵 Music" folder with volume, mood, rootNote,
  //            chordSeconds, reverb, brightness.
  //    💡 rootNote dropdown: ["C3", "D3", "E3", "F3", "G3", "A3"]
  //    💡 volume, chordSeconds and reverb need .onChange(applySoundSettings)
}

// 🔧 Already done: makes the menu show the newest values (used when loading a preset).
function refreshSettings() {
  if (gui) gui.controllersRecursive().forEach(c => c.updateDisplay());
}
