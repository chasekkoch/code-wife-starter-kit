/*
═══════════════════════════════════════════════════════════════════════
  PROJECT 3 — sound.js: THE MUSIC 🎵  ✅ SOLVED THROUGH STEP 3.8
═══════════════════════════════════════════════════════════════════════

This file uses Tone.js, a JavaScript library for making music in the
browser. Our music is a slow, dreamy loop of chords whose "brightness"
follows the wind of the Aurora.

🔊 Browsers only allow sound after you click something, so the music
   starts when you press the 🔊 Start sound button.

🎹 How sound flows (like plugging guitar pedals together):

      synth ──► filter ──► reverb ──► your speakers
     (notes)   (brightness) (echo)

📍 Your steps in this file: 3.5, 3.6  (and ⭐ 3.11)
*/

let soundStarted = false;
let synth;        // plays the chords        (STEP 3.5)
let chordLoop;    // repeats the chords      (STEP 3.5)
let filter;       // controls brightness     (STEP 3.6)
let reverb;       // the echo
let sparkle;      // twinkly wand notes      (⭐ STEP 3.11)
let chordNumber = 0;

// Each mood is 4 chords. Each chord is a list of notes, written as
// "how many piano keys above the root note" (0 = the root itself).
const MOODS = {
  dreamy:     [[0, 4, 7, 11], [9, 12, 16, 19], [5, 9, 12, 16], [7, 11, 14, 18]],
  mysterious: [[0, 3, 7, 10], [-4, 0, 3, 7], [3, 7, 10, 14], [-2, 2, 5, 9]],
  hopeful:    [[0, 4, 7, 14], [7, 11, 14, 19], [9, 12, 16, 21], [5, 9, 12, 17]],
};

// ═════════════════════════════════════════════════════════════════════
// 🔧 Helpers: already done!
// ═════════════════════════════════════════════════════════════════════

// Turns MOODS into real note names, e.g. chordsFor("C3", "dreamy")[0] → ["C3","E3","G3","B3"]
function chordsFor(rootNote, mood) {
  const shapes = MOODS[mood] || MOODS.dreamy;
  return shapes.map(shape => shape.map(n => Tone.Frequency(rootNote).transpose(n).toNote()));
}

// A pretty 10-note scale (pentatonic), two octaves above the root. Every note sounds good!
function scaleFor(rootNote) {
  return [0, 2, 4, 7, 9, 12, 14, 16, 19, 21].map(n => Tone.Frequency(rootNote).transpose(24 + n).toNote());
}

// Plays the next chord in the mood. The chord loop (STEP 3.5) calls this.
function playNextChord(time) {
  const chords = chordsFor(PARAMS.rootNote, PARAMS.mood);
  const chord = chords[chordNumber % chords.length];
  synth.triggerAttackRelease(chord, PARAMS.chordSeconds * 0.9, time);
  chordNumber += 1;
}

async function startSound() {
  await Tone.start();
  await buildSound();
  soundStarted = true;
  applySoundSettings();
}

// Call this after changing a music knob, so the music catches up.
function applySoundSettings() {
  if (!soundStarted) return;
  Tone.getDestination().volume.rampTo(PARAMS.volume, 0.1);
  reverb.decay = PARAMS.reverb;
  if (chordLoop) chordLoop.interval = PARAMS.chordSeconds;
}


// ═════════════════════════════════════════════════════════════════════
// ✏️ STEP 3.5 — Make some music 🎹
//
// The echo, the brightness filter and the wand's sparkle synth are
// already built. You'll add the main SYNTH, and a LOOP that plays a
// chord every few seconds.
//
// 🧰 Tools:
//   new Tone.PolySynth(...)    a synth that can play many notes at once
//   .connect(filter)           plug it into the filter
//   new Tone.Loop(callback, seconds).start(0)
//                              calls callback every `seconds` seconds
//   Tone.getTransport().start()   presses ▶️ on Tone's clock
// ═════════════════════════════════════════════════════════════════════
async function buildSound() {
  reverb = new Tone.Reverb({ decay: PARAMS.reverb, wet: 0.5 }).toDestination();
  filter = new Tone.Filter(PARAMS.brightness, "lowpass").connect(reverb);
  sparkle = new Tone.PolySynth(Tone.FMSynth, { volume: -10 }).connect(reverb);
  await reverb.ready;

  synth = new Tone.PolySynth(Tone.Synth, {
    oscillator: { type: "fatsine" },
    envelope: { attack: 1.5, release: 4 },
  }).connect(filter);
  chordLoop = new Tone.Loop(playNextChord, PARAMS.chordSeconds).start(0);
  Tone.getTransport().start();
}


// ═════════════════════════════════════════════════════════════════════
// ✏️ STEP 3.6 — Let the wind play the music 🌬️🎶
//
// sketch.js calls updateSound() every frame with the AVERAGE direction
// of all the particles:
//   flowX = -1 means "everything blows LEFT", 1 means "everything blows RIGHT"
//   flowY = -1 means "everything blows UP",   1 means "everything blows DOWN"
//
// Let's make the music get BRIGHTER when the wind blows right, and darker
// when it blows left, by moving the filter's cutoff frequency.
//
// 🧰 Tools:
//   map(value, fromLow, fromHigh, toLow, toHigh)
//        converts a number from one range to another. Example:
//        map(0.5, 0, 1, 0, 100) → 50
//   filter.frequency.rampTo(newValue, 0.3)
//        glides the filter to newValue over 0.3 seconds
// ═════════════════════════════════════════════════════════════════════
function updateSound(flowX, flowY) {
  if (!soundStarted || frameCount % 6 !== 0) return;   // only every 6th frame, to keep things smooth
  const cutoff = map(flowX, -1, 1, 300, PARAMS.brightness);
  filter.frequency.rampTo(cutoff, 0.3);
  // 💡 The wind changes slowly, so give it 10-20 seconds to hear the difference.
  //    Want it more obvious? Turn up the 🌬️ "pattern change" knob.
}


// ═════════════════════════════════════════════════════════════════════
// ⭐ BONUS STEP 3.11 — Sparkles for the wand 🪄
// sketch.js calls this when you click or drag on the Aurora.
//
// 🧰 Tools:
//   scaleFor(PARAMS.rootNote)    a list of 10 notes, low to high
//   map(y, height, 0, 0, 9, true)   bottom of screen → 0, top → 9
//   floor(3.7)                   3   (rounds down to a whole number)
//   sparkle.triggerAttackRelease(note, "8n")   plays a short note
// ═════════════════════════════════════════════════════════════════════
function playSparkle(x, y) {
  if (!soundStarted) return;
  // ✏️ TODO: pick a note from scaleFor(...) based on how HIGH the mouse is,
  //          and play it on the sparkle synth.
}
