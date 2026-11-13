/*
═══════════════════════════════════════════════════════════════════════
  PROJECT 3 — errors.js: THE BUG CATCHER 🐛  (already done, no changes needed!)
═══════════════════════════════════════════════════════════════════════

When JavaScript hits a mistake, it usually fails SILENTLY: the page just
stops working. This file catches those mistakes and shows them in a red
banner at the top, with the file and line number, so you know where to look.

💡 For even more detail, open the browser's Developer Tools:
     Windows/Linux: F12 or Ctrl+Shift+J      Mac: Cmd+Option+J
   and click the "Console" tab.
*/

(function () {
  const seen = new Set();

  function showBug(message, file, line) {
    const where = file ? `${file.split("/").pop()} line ${line}` : "somewhere";
    const text = `🐛 ${message}  (${where})`;
    if (seen.has(text)) return;
    seen.add(text);

    let banner = document.getElementById("bugs");
    if (!banner) {
      banner = document.createElement("div");
      banner.id = "bugs";
      document.body.prepend(banner);
    }
    const row = document.createElement("div");
    row.textContent = text;
    banner.appendChild(row);
    if (seen.size === 1) {
      const tip = document.createElement("small");
      tip.textContent = "Fix it, save, and refresh (Ctrl+R / Cmd+R). More details: open DevTools (F12 or Cmd+Option+J) → Console.";
      banner.appendChild(tip);
    }
  }

  window.addEventListener("error", (event) => {
    showBug(event.message, event.filename, event.lineno);
  });
  window.addEventListener("unhandledrejection", (event) => {
    showBug(event.reason && event.reason.message ? event.reason.message : String(event.reason));
  });
})();
