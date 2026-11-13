# 🐍 → 🟨 Python to JavaScript Cheat Sheet

You already know Python! JavaScript is its cousin: same ideas, slightly different spelling.
Keep this open next to you during Project 3.

## The big five differences

| | 🐍 Python | 🟨 JavaScript |
|---|---|---|
| 1. Blocks | indentation + `:` | `{ curly braces }` (indentation is just for looks) |
| 2. Line endings | nothing | `;` at the end of a statement (usually optional, but we use it) |
| 3. New variables | `speed = 2` | `let speed = 2;` (can change) or `const speed = 2;` (can't) |
| 4. Comments | `# comment` | `// comment` or `/* many lines */` |
| 5. True / False | `True`, `False`, `None` | `true`, `false`, `null` |

## Side by side

### Printing
```python
print("Hello", name)
```
```js
console.log("Hello", name);   // shows up in DevTools → Console (F12 / Cmd+Option+J)
```

### Variables and math
```python
count = 10
count += 1
half = count / 2
whole = count // 2
```
```js
let count = 10;
count += 1;          // count++ also works
const half = count / 2;
const whole = Math.floor(count / 2);
```

### Text (strings)
```python
f"Hello {name}, you are {age}"
len(word)
word.upper()
```
```js
`Hello ${name}, you are ${age}`     // backticks ` and ${...}
word.length                          // no parentheses!
word.toUpperCase()
```

### If / else
```python
if speed > 3 and glow:
    print("fast!")
elif speed > 1:
    print("medium")
else:
    print("slow")
```
```js
if (speed > 3 && glow) {
  console.log("fast!");
} else if (speed > 1) {
  console.log("medium");
} else {
  console.log("slow");
}
```

| 🐍 | 🟨 |
|---|---|
| `and` | `&&` |
| `or` | `\|\|` |
| `not` | `!` |
| `==` | `===` (three equals! the safe one) |
| `!=` | `!==` |

### Lists ↔ Arrays
```python
cats = ["Meredith", "Olivia"]
cats.append("Benjamin")
cats[0]
len(cats)
```
```js
const cats = ["Meredith", "Olivia"];
cats.push("Benjamin");
cats[0]
cats.length
```

### Loops
```python
for i in range(10):
    print(i)

for cat in cats:
    print(cat)
```
```js
for (let i = 0; i < 10; i++) {
  console.log(i);
}

for (const cat of cats) {        // "of", not "in"!
  console.log(cat);
}
```

### Dictionaries ↔ Objects
```python
particle = {"x": 10, "y": 20}
particle["x"]
particle["x"] = 15
```
```js
const particle = { x: 10, y: 20 };   // no quotes needed on keys
particle.x                           // dot works...
particle["x"] = 15;                  // ...and so do brackets
```

### Functions
```python
def double(n):
    return n * 2
```
```js
function double(n) {
  return n * 2;
}
```

## p5.js toolbelt (Project 3)

| Want to... | Use |
|---|---|
| random number 0 → n | `random(n)` |
| smooth random 0 → 1 | `noise(x, y, z)` |
| screen size | `width`, `height` |
| mouse position | `mouseX`, `mouseY` |
| frames drawn so far | `frameCount` |
| draw a dot | `point(x, y)` |
| fill the screen | `background(color)` |
| make a color | `color("#ff8800")` |
| blend two colors | `lerpColor(c1, c2, 0.5)` |
| convert a range | `map(value, fromLow, fromHigh, toLow, toHigh)` |
| distance | `dist(x1, y1, x2, y2)` |
| angle → x/y step | `cos(angle)`, `sin(angle)` |

## When something breaks 🐛

1. Look for the **red banner** at the top of the Aurora page. It names the file and line.
2. Typical culprits: a missing `)` or `}`, a missing `,` between object items, or a misspelled name (JavaScript is case-sensitive: `PARAMS.Speed` ≠ `PARAMS.speed`).
3. For more detail, open **DevTools → Console**: F12 or Ctrl+Shift+J on Windows/Linux, Cmd+Option+J on a Mac.
