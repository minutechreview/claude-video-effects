---
name: portal
description: A glowing ring tears open behind the speaker and grows until they're standing in a completely different place (any image or video), then snaps shut. The speaker stays in front the whole time. Needs /fx-setup.
---

# /portal: open a doorway to another world behind the speaker

**Inputs:**
- The world image or video: 1080×1920, at `assets/img/portal-world.jpg`.
- OPEN (the word that triggers it) and CLOSE times.
- The ring centre. The default is 50% / 40%, which is behind the head.

## HTML (first thing inside `#behind`)
```html
<div id="portal" class="layer"><div id="portal-world"></div><div id="portal-rim"></div></div>
```

## Timeline
```js
const OPEN = 13.68, CLOSE = 14.85;
const portal = { r: 0 };
const placePortal = () => {
  $("#portal-world").style.clipPath = `circle(${portal.r}px at 50% 40%)`;
  const rim = $("#portal-rim"); rim.style.width = rim.style.height = `${portal.r * 2}px`; rim.style.margin = `${-portal.r}px 0 0 ${-portal.r}px`;
};
placePortal();
tl.set("#portal", { opacity: 1 }, OPEN);
tl.fromTo("#portal-rim", { opacity: 0 }, { opacity: 1, duration: 0.1 }, OPEN);
tl.to(portal, { r: 120, duration: 0.4, ease: "back.out(2)", onUpdate: placePortal }, OPEN);           // a small glowing ring
tl.to(portal, { r: 1250, duration: 0.55, ease: "expo.in", onUpdate: placePortal }, OPEN + 0.42);     // bursts open
tl.to("#portal-rim", { opacity: 0, duration: 0.15 }, OPEN + 0.92);
tl.to(portal, { r: 0, duration: 0.3, ease: "expo.in", onUpdate: placePortal }, CLOSE);              // snaps shut
tl.set("#portal", { opacity: 0 }, CLOSE + 0.31);
chip(OPEN + 0.78, CLOSE + 0.17, "portal");
```

## Sound
A shockwave whoosh as it bursts open, at 0.8.

## Tips
- The world should be bright and very different from the room: a beach, a stadium, space, a game world.
- To use a video as the world, put a `<video class="clip fill" muted>` inside `#portal-world` with matching data-start / data-duration.
