---
name: orbit
description: Glass cards orbit around the speaker's head, passing BEHIND them on the far side and IN FRONT on the near side, like a 3D ring. Great for showing features or tools. Needs /fx-setup (the cut-out makes the behind/in-front work).
---

# /orbit: cards circling the speaker in 3D

Every card exists twice: one copy in `#behind` and one in `#front`. Each frame, the copy on the correct side is shown, depending on the card's angle. That's what makes them pass behind the head and come round in front.

**Inputs:** 4–8 cards as an icon plus a short label, start and end times, and the centre of the ring (usually head height).

## HTML
- In `#behind`: `<div id="orbit-back"></div>`
- In `#front`: `<div id="orbit-front"></div>`

## Timeline
```js
const START = 11.84, END = 13.7, CX = 540, CY = 760, RX = 430, RY = 130;
const TILES = [["✂️", "cut-out"], ["Aa", "text"], ["🎬", "render"], ["🔊", "sound"], ["✨", "effects"], ["⚡", "1 command"]];
const pairs = TILES.map(([icon, label]) => {
  const back = el("div", "tile glass", `<i>${icon}</i>${label}`), front = el("div", "tile glass", `<i>${icon}</i>${label}`);
  $("#orbit-back").append(back); $("#orbit-front").append(front); return [back, front];
});
const orbit = { a: 0, k: 0 };
const placeOrbit = () => pairs.forEach(([back, front], i) => {
  const th = orbit.a + (i / pairs.length) * Math.PI * 2;
  const x = CX + Math.cos(th) * RX, y = CY + Math.sin(th) * RY - Math.cos(th) * 40;   // a tilted ring
  const s = (0.72 + 0.38 * (Math.sin(th) + 1) / 2) * orbit.k;                        // nearer = bigger
  for (const [node, show] of [[back, Math.sin(th) <= 0], [front, Math.sin(th) > 0]]) {
    node.style.transform = `translate(${x}px, ${y}px) scale(${s}) rotate(${Math.cos(th) * -8}deg)`;
    node.style.opacity = show ? String(Math.min(1, orbit.k * 1.4)) : "0";
  }
});
placeOrbit();
tl.to(orbit, { k: 1, duration: 0.35, ease: "back.out(1.6)", onUpdate: placeOrbit }, START);
tl.to(orbit, { a: Math.PI * 2.4, duration: END - START, ease: "power1.inOut", onUpdate: placeOrbit }, START);
tl.to(orbit, { k: 0, duration: 0.25, ease: "power2.in", onUpdate: placeOrbit }, END - 0.25);
chip(START + 1.1, END - 0.1, "orbit");
```

## Sound
A magic-wand whoosh at START (0.6), and a soft "orb" pop when the word "orbit" is said.

## Tips
- Keep RY small (100–150) so it reads as a ring seen from the front.
- 6 cards look best. More than 8 gets crowded.
