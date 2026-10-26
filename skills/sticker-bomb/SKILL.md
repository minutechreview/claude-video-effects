---
name: sticker-bomb
description: Paper stickers slap onto the frame one per word ("TEMPLATES", "SUBSCRIPTIONS"…), then a red marker X scribbles through each, and they fly off. Perfect for "no X, no Y, no Z" lines. Needs /fx-setup.
---

# /sticker-bomb: slap, cross out, fly away

**Inputs:** each sticker's text, the time it's said, a position (x, y) and a tilt; plus OUT (when they all fly off).

## HTML (in `#front`)
```html
<div id="stickers"></div>
```

## Timeline
```js
const OUT = 18.15;
const STICKERS = [[15.36, "TEMPLATES", 60, 300, -8], [15.98, "SUBSCRIPTIONS", 300, 470, 6], [17.3, "TIMELINE DRAGGING", 70, 1290, -5]];
STICKERS.forEach(([t, text, x, y, rot], i) => {
  const s = el("div", "sticker", `${text}<svg viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M4 18 L96 82" pathLength="1"/><path d="M96 18 L4 82" pathLength="1"/></svg>`);
  s.style.left = `${x}px`; s.style.top = `${y}px`; $("#stickers").append(s);
  const paths = s.querySelectorAll("path");
  gsap.set(paths, { strokeDasharray: 1, strokeDashoffset: 1, opacity: 0 });   // hidden until drawn (no stray round caps)
  tl.fromTo(s, { opacity: 0, scale: 2.2, rotation: rot * 3 }, { opacity: 1, scale: 1, rotation: rot, duration: 0.22, ease: "back.out(2.2)" }, t);
  paths.forEach((p, k) => tl.to(p, { opacity: 1, strokeDashoffset: 0, duration: 0.14 }, t + 0.28 + k * 0.12));
  tl.to(s, { x: x < 400 ? -900 : 900, rotation: rot * 4, duration: 0.35, ease: "power3.in" }, OUT + i * 0.05);
});
chip(STICKERS[0][0], OUT + 0.2, "sticker-bomb");
```

## Sound
A slap on each sticker (0.8). Optionally a marker scribble on each X.

## Tips
- Place them so they don't cover the eyes. The empty wall above and beside the head works best.
- Keep each sticker to 2 words at most. Long ones get a smaller `font-size`.
