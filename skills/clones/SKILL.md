---
name: clones
description: Two colour-tinted copies of the speaker slide out from behind them, one each side, so there are three of them on screen talking in sync. Great for "packed all of them" / "times three" / team moments. Needs /fx-setup (uses the cut-out video).
---

# /clones: three of you

The clones are extra copies of the cut-out video (`src/me.webm`), placed in `#behind`. They're scaled down a little, pushed left and right, and tinted with CSS filters. Because they sit behind, the real speaker overlaps them.

**Inputs:** IN and OUT times, and optionally a big label that slams in at the top.

## HTML (in `#behind`; the start times must differ slightly or the renderer dedupes them)
```html
<div id="clone-l" class="clone"><video class="clip fill" src="src/me.webm" muted playsinline data-start="22.3" data-media-start="22.3" data-duration="3.4" data-track-index="2"></video></div>
<div id="clone-r" class="clone"><video class="clip fill" src="src/me.webm" muted playsinline data-start="22.34" data-media-start="22.34" data-duration="3.36" data-track-index="3"></video></div>
```
`data-media-start` must equal `data-start`, so the clones lip-sync with the speaker.

Optional label (in `#front`):
```html
<div id="toolkit"><span>FREE</span><b>TOOLKIT</b><small>for Claude</small></div>
```

## Timeline
```js
const IN = 22.52, OUT = 25.3, LABEL = 23.7;
gsap.set(".clone", { transformOrigin: "50% 100%" });
tl.fromTo("#clone-l", { opacity: 0, x: 0, scale: 0.86 }, { opacity: 1, x: -330, scale: 0.8, duration: 0.45, ease: "back.out(1.5)" }, IN);
tl.fromTo("#clone-r", { opacity: 0, x: 0, scale: 0.86 }, { opacity: 1, x: 330, scale: 0.8, duration: 0.45, ease: "back.out(1.5)" }, IN + 0.08);
tl.to(".clone", { x: 0, opacity: 0, duration: 0.3, ease: "power2.in" }, OUT);
tl.fromTo("#toolkit", { opacity: 0, y: -40 }, { opacity: 1, y: 0, duration: 0.3, ease: "back.out(2)" }, LABEL);
tl.fromTo("#toolkit b", { scale: 1.6 }, { scale: 1, duration: 0.3, ease: "expo.out" }, LABEL + 0.2);
tl.to("#toolkit", { opacity: 0, y: -80, duration: 0.25 }, OUT + 0.1);
chip(IN + 0.04, OUT + 0.1, "clones");
```

## Sound
A fast whoosh when they slide out (0.9), and a pop on the label.

## Tips
- Change the tints in `style.css` (`#clone-l video`, `#clone-r video`): e.g. brand orange and blue, or plain `grayscale(1)`.
