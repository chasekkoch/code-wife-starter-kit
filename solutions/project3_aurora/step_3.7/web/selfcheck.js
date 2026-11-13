/*
═══════════════════════════════════════════════════════════════════════
  PROJECT 3 — selfcheck.js: THE CHECKLIST ✅  (already done, no changes needed!)
═══════════════════════════════════════════════════════════════════════

The little panel in the corner that ticks off each step as you finish
it. Press C (or the ✅ button) to hide or show it.
*/

const selfCheck = {
  filterValues: new Set(),    // filter frequencies we've seen (for STEP 3.6)
  server: { presets: false, presetsHint: "", random: false, randomHint: "" },
  snapshotTaken: false,
};

// Each check gives back true (done!) or a string (a hint for what's missing).
const CHECKS = [
  ["3.1", "Make it yours", () => {
    if (PARAMS.title === "My Aurora") return "Change the title in params.js";
    if (PARAMS.colorA === "#ffffff" && PARAMS.colorB === "#ffffff") return "Pick your own colorA and colorB in params.js";
    return true;
  }],
  ["3.2", "A sky full of particles", () => {
    if (particles.length === 0) return "createParticles() made no particles yet";
    if (!particles[0]) return "makeParticle() gave back null. Return a particle object!";
    if (typeof particles[0].x !== "number") return "Each particle needs a number x and y";
    if (particles.length !== PARAMS.particleCount) return `Expected ${PARAMS.particleCount} particles, found ${particles.length}`;
    return true;
  }],
  ["3.3", "The flow field", () => {
    if (!particles[0]) return "Finish step 3.2 first";
    const mover = { x: width / 2, y: height / 2, vx: 0, vy: 0 };
    moveParticle(mover);
    if (mover.x === width / 2 && mover.y === height / 2) return "Particles aren't moving yet (moveParticle)";
    const test = { x: -5, y: height + 5 };
    wrapAround(test);
    if (test.x !== width) return "wrapAround: off the LEFT edge should come back at x = width";
    if (test.y !== 0) return "wrapAround: off the BOTTOM edge should come back at y = 0";
    return true;
  }],
  ["3.4", "Color & glow", () => {
    const a = color(PARAMS.colorA);
    const b = color(PARAMS.colorB);
    if (PARAMS.colorA === PARAMS.colorB) return "Make colorA and colorB different to test this";
    const top = getParticleColor({ x: 0, y: 0 }, a, b).toString();
    const bottom = getParticleColor({ x: 0, y: height }, a, b).toString();
    if (top === bottom) return "Top and bottom particles are the same color (getParticleColor)";
    const glowWas = PARAMS.glow;
    PARAMS.glow = true;  applyGlow();  const withGlow = drawingContext.globalCompositeOperation;
    PARAMS.glow = false; applyGlow();  const noGlow = drawingContext.globalCompositeOperation;
    PARAMS.glow = glowWas;
    blendMode(BLEND);
    if (withGlow !== "lighter") return "applyGlow: when glow is true, use blendMode(ADD)";
    if (noGlow !== "source-over") return "applyGlow: when glow is false, use blendMode(BLEND)";
    return true;
  }],
  ["3.5", "Make some music", () => {
    if (!soundStarted) return "Press 🔊 Start sound to test this step";
    if (!synth) return "No synth yet (TODO A)";
    if (!chordLoop) return "No chordLoop yet (TODO B)";
    if (Tone.getTransport().state !== "started") return "Start Tone's clock (TODO C)";
    return true;
  }],
  ["3.6", "Let the wind play", () => {
    if (!soundStarted) return "Press 🔊 Start sound to test this step";
    selfCheck.filterValues.add(Math.round(filter.frequency.value));
    if (selfCheck.filterValues.size < 3) return "The filter's frequency isn't changing yet (updateSound)";
    return true;
  }],
  ["3.7", "Settings menu", () => {
    if (!gui) return "No menu yet. Create gui in settings.js";
    const count = gui.controllersRecursive().length;
    if (count < 10) return `Your menu has ${count} controls. Add at least 10!`;
    return true;
  }],
  ["3.8", "Presets API (Python)", () => selfCheck.server.presets || selfCheck.server.presetsHint],
  ["3.9", "Surprise me (Python)", () => selfCheck.server.random || selfCheck.server.randomHint],
];

const BONUS_CHECKS = [
  ["3.10", "Your own sliders", () => {
    const count = document.querySelectorAll("#my-panel input[type=range]").length;
    return count >= 2 || `Add 2 sliders to #my-panel in index.html (found ${count})`;
  }],
  ["3.11", "Wand mode", () => wandEverWorked || "Hold the mouse down on the Aurora to test"],
  ["3.12", "Snapshots & shortcuts", () => selfCheck.snapshotTaken || "Press S to take a snapshot"],
];

function runCheck(check) {
  try {
    return check();
  } catch (err) {
    return `⚠️ Error: ${err.message}`;
  }
}

async function checkServer() {
  const presets = await fetch("/api/presets").catch(() => null);
  if (!presets) {
    selfCheck.server.presetsHint = selfCheck.server.randomHint = "Server isn't running (python main.py)";
    return;
  }
  const names = presets.ok ? await presets.json() : null;
  if (!Array.isArray(names)) {
    selfCheck.server.presetsHint = "list_presets() isn't finished (TODO 1)";
  } else if (names.length === 0) {
    selfCheck.server.presetsHint = "No presets found in the presets folder";
  } else {
    const one = await fetch(`/api/presets/${names[0]}`);
    if (!one.ok) selfCheck.server.presetsHint = "get_preset() isn't finished (TODO 2)";
    else selfCheck.server.presets = true;   // python check.py 3.8 tests the rest (404s and saving)
  }
  const random = await fetch("/api/random-preset");
  const data = random.ok ? await random.json() : null;
  if (!data) selfCheck.server.randomHint = "random_preset() isn't finished (generator.py)";
  else if (!data.colorA || !data.mood) selfCheck.server.randomHint = "random_preset() is missing some keys";
  else selfCheck.server.random = true;
}

function renderCheckList() {
  const panel = document.getElementById("selfcheck");
  panel.hidden = !PARAMS.showSelfCheck;
  if (panel.hidden) return;

  let html = "<h2>✅ Self-check</h2><ul>";
  let allDone = true;
  for (const [step, name, check] of CHECKS) {
    const result = runCheck(check);
    if (result === true) {
      html += `<li class="done">✅ <b>${step}</b> ${name}</li>`;
    } else {
      html += `<li>⬜ <b>${step}</b> ${name}<small>${result}</small></li>`;
      allDone = false;
    }
  }
  html += "</ul><h3>⭐ Bonus</h3><ul>";
  for (const [step, name, check] of BONUS_CHECKS) {
    const result = runCheck(check);
    if (result === true) html += `<li class="done">🌟 <b>${step}</b> ${name}</li>`;
    else html += `<li class="bonus">☆ <b>${step}</b> ${name}<small>${result}</small></li>`;
  }
  html += "</ul>";
  if (allDone) html += "<p class='party'>🎉 Every step done. You built this! 🎉</p>";
  html += "<p class='tip'>Press C to hide</p>";
  panel.innerHTML = html;
}

function setupSelfCheck() {
  // Notice when a snapshot is taken (⭐ STEP 3.12).
  const realSaveCanvas = window.saveCanvas;
  window.saveCanvas = function (...args) {
    selfCheck.snapshotTaken = true;
    return realSaveCanvas.apply(this, args);
  };

  document.addEventListener("keydown", (event) => {
    if (["INPUT", "SELECT", "TEXTAREA"].includes(event.target.tagName)) return;
    if (event.key === "c" || event.key === "C") PARAMS.showSelfCheck = !PARAMS.showSelfCheck;
  });

  setInterval(renderCheckList, 500);
  checkServer();
  setInterval(() => { if (PARAMS.showSelfCheck) checkServer(); }, 5000);
}
