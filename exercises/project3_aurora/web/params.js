/*
═══════════════════════════════════════════════════════════════════════
  PROJECT 3 — params.js: THE KNOBS 🎛️
═══════════════════════════════════════════════════════════════════════

Every visual and musical choice in the Aurora lives in this ONE object,
called PARAMS. The rest of the code just READS from it. So when you
change a number here and refresh the page, the whole Aurora changes.

In STEP 3.7 you'll build an on-screen settings menu that changes these
same values live, without touching code.

🧰 JavaScript objects look a lot like Python dictionaries:
      Python:      {"speed": 2, "glow": True}
      JavaScript:  { speed: 2, glow: true }
   (no quotes needed around the keys, and true/false are lowercase)

   Colors are hex strings, just like Palette Potion in Project 2:
      "#ff8800"   ← need ideas? search "color picker" in your browser.

✏️ STEP 3.1: Make it yours! (See STEPS.md for the full guide.)
   1. Change `title` to anything you like.
   2. Change `background`, `colorA` and `colorB` to colors you love.
   3. Save, then refresh the browser tab (Ctrl+R / Cmd+R).
*/

const PARAMS = {
  title: "My Aurora",
  showSelfCheck: true,     // the ✅ checklist in the corner (press C to toggle)

  // 🎨 LOOK
  background: "#000000",   // the night sky
  colorA: "#ffffff",       // particle color at the TOP of the screen
  colorB: "#ffffff",       // particle color at the BOTTOM of the screen
  particleCount: 1500,     // how many particles (more = prettier but slower)
  particleSize: 1.5,       // how big each particle is
  particleAlpha: 60,       // see-through-ness: 0 = invisible, 255 = solid
  trailFade: 12,           // 1-100: LOW = long silky trails, HIGH = short trails
  glow: true,              // overlapping particles add up into a glow

  // 🌬️ WIND (the flow field)
  speed: 1.5,              // how fast particles move
  noiseScale: 0.003,       // zoom of the wind pattern: small = big lazy swirls
  noiseSpeed: 0.002,       // how quickly the wind pattern changes over time
  swirl: 2,                // how twisty the wind is

  // 🎵 MUSIC
  volume: -14,             // in decibels: 0 = loud, -40 = whisper
  mood: "dreamy",          // "dreamy", "mysterious" or "hopeful"
  rootNote: "C3",          // the musical key: "C3", "D3", "E3", "F3", "G3", "A3"
  chordSeconds: 4,         // how long each chord lasts
  reverb: 8,               // how big the room sounds (seconds of echo)
  brightness: 2500,        // how bright/sparkly the music can get

  // ⭐ WAND (bonus step 3.11)
  wandRadius: 120,
  wandStrength: 3,
};
