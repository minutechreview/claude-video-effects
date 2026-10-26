---
name: rewind
description: VHS "raw footage" opening that rewinds and snaps into the edited video, then slams a giant number BEHIND the speaker (e.g. "0 EDITING APPS"). Use for a hook in the first 1–3 seconds. Needs a project from /fx-setup.
---

# /rewind: VHS rewind into the edit, plus a big number behind the head

**What it looks like**
- 0 to ~0.9 s: the clip looks like raw tape. It's desaturated, with scanlines, "● REC RAW", a blinking "◀◀ REWIND", a tracking bar rolling through, and a timecode spinning down.
- Then a white flash, a quick zoom snap, and the edited look is back.
- On a chosen word, a huge accent-coloured number slams in behind the speaker's head, with a label under it.

**Ask for (or pick from the transcript)**
- `SNAP`: when the rewind ends. Default 0.95 s, or on the first strong word.
- `BIG`: the number and label, e.g. `0` / `EDITING APPS`.
- `HIT`: the word it slams on.

## HTML
- After `#flash`, in the finish area:
```html
<div id="vhs" class="layer"><div class="scan"></div><div id="vhs-rec">● REC  RAW</div><div id="vhs-rew">◀◀ REWIND</div><div id="vhs-time">00:00:00</div><div id="tracking"></div></div>
```
- In `#behind`:
```html
<div id="title-behind"><span id="zero">0</span><span id="zero-label">EDITING APPS</span></div>
```

## Timeline (paste at `// FX: effects go here`)
```js
const SNAP = 0.95, HIT = 2.36;   // ← from the transcript
const desat = el("div", "layer"); desat.style.cssText = "background:#808080;mix-blend-mode:saturation"; $("#vhs").prepend(desat);
tl.set("#vhs", { opacity: 1 }, 0);
tl.fromTo("#vhs-rew", { opacity: 0 }, { opacity: 1, duration: 0.05, repeat: 5, yoyo: true }, 0.3);
tl.fromTo("#tracking", { y: 900 }, { y: -1300, duration: SNAP / 2, ease: "none", repeat: 1 }, 0.05);
tl.fromTo("#plate-wrap, #me-wrap", { x: 0 }, { x: 10, duration: 0.05, repeat: 9, yoyo: true, ease: "none" }, 0.35);
const clock = { s: 154 };
tl.to(clock, { s: 0, duration: SNAP, ease: "power2.in", onUpdate: () => { const s = Math.round(clock.s); $("#vhs-time").textContent = `00:0${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`; } }, 0);
tl.set("#vhs", { opacity: 0 }, SNAP);
tl.fromTo("#flash", { opacity: 0.9 }, { opacity: 0, duration: 0.25, immediateRender: false }, SNAP);
tl.fromTo("#plate-wrap, #me-wrap", { scale: 1.06 }, { scale: 1, duration: 0.5, ease: "expo.out", immediateRender: false }, SNAP);
tl.fromTo("#title-behind", { opacity: 0 }, { opacity: 1, duration: 0.01 }, HIT);
tl.fromTo("#zero", { scale: 1.8, y: -60 }, { scale: 1, y: 0, duration: 0.35, ease: "expo.out" }, HIT);
tl.fromTo("#zero-label", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.25 }, HIT + 0.14);
tl.to("#title-behind", { y: -220, opacity: 0, duration: 0.3, ease: "power2.in" }, HIT + 0.75);
chip(0.05, SNAP - 0.05, "rewind");
```

## Sound
- A reversed cymbal over 0–SNAP, at 0.6.
- A glitch click at SNAP, at 0.9.
- A bass impact on HIT, at 0.8.

## Tips
- Keep `#zero` short: 1–3 characters. It needs the empty wall above the head.
- If the speaker's head is high in frame, lower the font size or move `#title-behind` down.
