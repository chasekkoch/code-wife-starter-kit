/*
═══════════════════════════════════════════════════════════════════════
  PROJECT 3 — sketch.js: THE AURORA ✨  ✅ SOLVED THROUGH STEP 3.6
═══════════════════════════════════════════════════════════════════════

This file uses p5.js, a JavaScript library made for artists. p5 calls
two special functions for you:

   setup()  runs ONCE when the page opens.
   draw()   runs about 60 TIMES PER SECOND, forever. Each run paints one
            "frame", like a flip-book. Moving things = small changes per frame.

🗺️ The screen is a grid of pixels:  x goes RIGHT →, y goes DOWN ↓.
   (0, 0) is the TOP-LEFT corner. `width` and `height` are the screen size.

🐍 → 🟨 Coming from Python? Peek at docs/python-to-js-cheatsheet.md.
   The big ones: lines end with ; blocks use { curly braces },
   variables start with `let` or `const`, and `//` starts a comment.

📍 Your steps in this file: 3.2, 3.3, 3.4  (and ⭐ 3.11, 3.12)
   Search for "STEP 3." to jump to each one. See STEPS.md for the guide.
*/

let particles = [];      // every particle lives in this list (JavaScript calls lists "arrays")
let wandDown = false;    // is the mouse being held down on the Aurora?
let wandEverWorked = false;

// ═════════════════════════════════════════════════════════════════════
// 🔧 setup() and draw(): already done. Read them to see how the pieces
//    you write fit together!
// ═════════════════════════════════════════════════════════════════════
function setup() {
  createCanvas(windowWidth, windowHeight);
  background(PARAMS.background);
  showTitle();
  createParticles();
  setupSettings();   // settings.js (STEP 3.7)
  setupMyPanel();    // my_panel.js (⭐ STEP 3.10)
  setupSelfCheck();  // selfcheck.js
}

function draw() {
  blendMode(BLEND);
  paintBackground();
  applyGlow();

  const colorA = color(PARAMS.colorA);
  const colorB = color(PARAMS.colorB);
  colorA.setAlpha(PARAMS.particleAlpha);
  colorB.setAlpha(PARAMS.particleAlpha);

  let flowX = 0;
  let flowY = 0;
  for (const p of particles) {
    if (!p) continue;   // skip unfinished particles (until makeParticle is done)
    // Now and then a particle hops to a new random spot, so they don't all clump into a few rivers.
    if (random() < 0.005) Object.assign(p, makeParticle());
    moveParticle(p);
    const before = [p.x, p.y];
    applyWand(p);
    if (p.x !== before[0] || p.y !== before[1]) wandEverWorked = true;
    drawParticle(p, colorA, colorB);
    flowX += p.vx;
    flowY += p.vy;
  }

  // Tell the music which way the wind is blowing (sound.js, STEP 3.6).
  const count = max(particles.length, 1);
  updateSound(flowX / count / PARAMS.speed, flowY / count / PARAMS.speed);
}

function showTitle() {
  document.getElementById("title").textContent = PARAMS.title;
  document.title = PARAMS.title;
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
  background(PARAMS.background);
}


// ═════════════════════════════════════════════════════════════════════
// ✏️ STEP 3.2 — A sky full of particles
//
// A particle is a JavaScript OBJECT (like a Python dictionary) that
// remembers where it is:   { x: 120, y: 45, vx: 0, vy: 0 }
//   x, y   = position on screen
//   vx, vy = velocity (how far it moves each frame). Start them at 0.
//
// 🧰 Tools:
//   random(width)        a random number from 0 up to the screen width
//   particles.push(p)    add p to the end of the array (Python's .append)
//   for (let i = 0; i < 10; i++) { ... }   repeat 10 times
//   point(x, y)          draws a dot
// ═════════════════════════════════════════════════════════════════════

// ✏️ TODO A: return a new particle at a random spot on the screen.
function makeParticle() {
  return { x: random(width), y: random(height), vx: 0, vy: 0 };
}

// ✏️ TODO B: fill `particles` with PARAMS.particleCount new particles.
//            (The first line, which empties the array, is done for you.)
function createParticles() {
  particles = [];
  for (let i = 0; i < PARAMS.particleCount; i++) {
    particles.push(makeParticle());
  }
}

// ✏️ TODO C: draw the particle as a dot at its x and y.
//            (Its color and size are already set for you.)
function drawParticle(p, colorA, colorB) {
  stroke(getParticleColor(p, colorA, colorB));
  strokeWeight(PARAMS.particleSize);
  point(p.x, p.y);
}


// ═════════════════════════════════════════════════════════════════════
// ✏️ STEP 3.3 — The flow field (this is where the magic happens 🌌)
//
// Imagine invisible wind blowing across the screen. At every spot, the
// wind points in some direction (an ANGLE). Each frame, every particle
// looks up the angle where it's standing and takes a small step that way.
//
// The secret ingredient is noise(): a smooth kind of random. Nearby spots
// get SIMILAR values, so the wind swirls instead of jittering.
//
// 🧰 Tools:
//   noise(a, b, c)        smooth random number from 0 to 1
//   frameCount            how many frames have been drawn so far
//   TWO_PI                one full turn of a circle (in radians)
//   cos(angle), sin(angle)   turn an angle into an x step and a y step
//   p.x += 5              shortcut for p.x = p.x + 5
//   if (p.x > width) { p.x = 0; }
// ═════════════════════════════════════════════════════════════════════

// ✏️ TODO A: move the particle along the wind.
function moveParticle(p) {
  const angle = noise(p.x * PARAMS.noiseScale, p.y * PARAMS.noiseScale, frameCount * PARAMS.noiseSpeed)
    * TWO_PI * PARAMS.swirl;
  p.vx = cos(angle) * PARAMS.speed;
  p.vy = sin(angle) * PARAMS.speed;
  p.x += p.vx;
  p.y += p.vy;
  wrapAround(p);
}

// ✏️ TODO B: if a particle drifts off one edge, bring it back on the
//            opposite edge (like Pac-Man!).
function wrapAround(p) {
  if (p.x > width) { p.x = 0; }
  if (p.x < 0) { p.x = width; }
  if (p.y > height) { p.y = 0; }
  if (p.y < 0) { p.y = height; }
}

// ✏️ TODO C: paint the sky SEE-THROUGH so old frames fade slowly into
//            trails, instead of being wiped away instantly.
function paintBackground() {
  const sky = color(PARAMS.background);
  sky.setAlpha(PARAMS.trailFade);
  background(sky);
}


// ═════════════════════════════════════════════════════════════════════
// ✏️ STEP 3.4 — Color & glow 🌈
//
// 🧰 Tools:
//   lerpColor(c1, c2, amount)   blends two colors. amount 0 = all c1,
//                               1 = all c2, 0.5 = halfway
//   p.y / height                0 at the top of the screen, 1 at the bottom
//   blendMode(ADD)              overlapping colors ADD UP into light (glow!)
//   blendMode(BLEND)            normal painting
// ═════════════════════════════════════════════════════════════════════

// ✏️ TODO A: return a color between colorA (top) and colorB (bottom),
//            depending on how far down the screen the particle is.
function getParticleColor(p, colorA, colorB) {
  return lerpColor(colorA, colorB, p.y / height);
}

// ✏️ TODO B: if PARAMS.glow is true use blendMode(ADD), otherwise BLEND.
function applyGlow() {
  if (PARAMS.glow) {
    blendMode(ADD);
  } else {
    blendMode(BLEND);
  }
}


// ═════════════════════════════════════════════════════════════════════
// ⭐ BONUS STEP 3.11 — Wand mode 🪄
// Hold the mouse down to push particles away from the cursor (and play
// sparkly notes, in sound.js).
//
// 🧰 Tools:
//   wandDown                  true while the mouse is held on the Aurora
//   mouseX, mouseY            where the mouse is
//   dist(x1, y1, x2, y2)      distance between two points
//   atan2(dy, dx)             the angle pointing from one point to another
// ═════════════════════════════════════════════════════════════════════
function applyWand(p) {
  // 1. If the wand isn't down, `return;` right away.
  // 2. If the particle is closer than PARAMS.wandRadius to the mouse...
  // 3. ...find the angle pointing AWAY from the mouse:
  //        const away = atan2(p.y - mouseY, p.x - mouseX);
  // 4. ...and push it: p.x += cos(away) * PARAMS.wandStrength;  (same for y with sin)
}

function mousePressed(event) {
  wandDown = event.target.tagName === "CANVAS";   // ignore clicks on buttons & menus
  if (wandDown) playSparkle(mouseX, mouseY);
}

function mouseDragged() {
  if (wandDown && frameCount % 8 === 0) playSparkle(mouseX, mouseY);
}

function mouseReleased() {
  wandDown = false;
}


// ═════════════════════════════════════════════════════════════════════
// ⭐ BONUS STEP 3.12 — Snapshots & keyboard shortcuts 📸
//
// p5 calls keyPressed() whenever a key is pressed, and puts it in `key`.
// 🧰 Tools:
//   saveCanvas("my-aurora", "png")    downloads a picture of the Aurora
//   fullscreen(!fullscreen())         toggles full screen
//   noLoop() / loop()                 pause / resume draw()
//   isLooping()                       true if draw() is running
//   background(PARAMS.background)     wipes the sky clean
// ═════════════════════════════════════════════════════════════════════
function keyPressed(event) {
  if (["INPUT", "SELECT", "TEXTAREA"].includes(event.target.tagName)) { return; }   // typing in a box
  // if (key === "s") { ... }   ← take a snapshot
  // f = fullscreen,  space = pause,  r = wipe the sky
}
