/*
═══════════════════════════════════════════════════════════════════════
  PROJECT 3 — toolbar.js: THE BUTTONS 🔘  (✅ already done, just read!)
═══════════════════════════════════════════════════════════════════════

The buttons at the top of the page. This file talks to YOUR Python
server using fetch(), which is how a web page asks a server for data:

   fetch("/api/presets")             → runs list_presets() in main.py
   fetch("/api/presets/midnight_cat") → runs get_preset("midnight_cat")
   fetch("/api/random-preset")       → runs surprise_me() → generator.py

Until you finish STEP 3.8 and 3.9, some buttons will politely tell you so.
*/

// Knobs that are NOT saved in presets (your title stays yours!)
const NOT_IN_PRESETS = ["title", "showSelfCheck"];

function toast(message) {
  const box = document.getElementById("toast");
  box.textContent = message;
  box.classList.add("show");
  clearTimeout(toast.timer);
  toast.timer = setTimeout(() => box.classList.remove("show"), 3500);
}

// Asks the server for something. Gives back the data, or null (and shows why).
async function askServer(url, options = {}, quiet = false) {
  let response;
  try {
    response = await fetch(url, options);
  } catch (err) {
    if (!quiet) toast("😿 Can't reach the server. Is it running?  (python main.py)");
    return null;
  }
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    if (!quiet) {
      const icon = response.status === 501 ? "🔒" : "😿";
      toast(`${icon} ${data.detail || "The server said: " + response.status}`);
    }
    return null;
  }
  return data;
}

function applyPreset(preset, label) {
  for (const key of NOT_IN_PRESETS) delete preset[key];
  Object.assign(PARAMS, preset);
  createParticles();
  background(PARAMS.background);
  showTitle();
  applySoundSettings();
  refreshSettings();
  toast(`✨ ${label}`);
}

function prettyName(name) {
  return name.replace(/_/g, " ").replace(/\b\w/g, letter => letter.toUpperCase());
}

async function refreshPresetList() {
  const select = document.getElementById("load");
  const names = await askServer("/api/presets", {}, true);
  select.innerHTML = "";
  select.add(new Option(names ? "📂 Load a preset…" : "📂 Load (finish step 3.8)", ""));
  for (const name of names || []) select.add(new Option(prettyName(name), name));
}

document.getElementById("sound").addEventListener("click", async (event) => {
  const button = event.currentTarget;
  if (!soundStarted) {
    button.textContent = "⏳ Loading…";
    await startSound();
    if (!chordLoop) toast("🤫 Sound is on, but there's no music yet. That's STEP 3.5!");
  } else {
    Tone.getDestination().mute = !Tone.getDestination().mute;
  }
  button.textContent = Tone.getDestination().mute ? "🔇 Unmute" : "🔊 Mute";
});

document.getElementById("save").addEventListener("click", async () => {
  const name = prompt("Name your Aurora (letters, numbers and _ only):", "my_aurora");
  if (!name) return;
  const preset = { ...PARAMS };
  for (const key of NOT_IN_PRESETS) delete preset[key];
  const result = await askServer(`/api/presets/${encodeURIComponent(name)}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(preset),
  });
  if (result) {
    toast(`💾 Saved as "${prettyName(result.saved)}"`);
    refreshPresetList();
  }
});

document.getElementById("load").addEventListener("change", async (event) => {
  const name = event.target.value;
  if (!name) return;
  const preset = await askServer(`/api/presets/${encodeURIComponent(name)}`);
  if (preset) applyPreset(preset, prettyName(name));
  event.target.value = "";
});

document.getElementById("surprise").addEventListener("click", async () => {
  const preset = await askServer("/api/random-preset");
  if (preset) applyPreset(preset, "Surprise!");
});

document.getElementById("checklist").addEventListener("click", () => {
  PARAMS.showSelfCheck = !PARAMS.showSelfCheck;
});

refreshPresetList();
