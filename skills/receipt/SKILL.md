---
name: receipt
description: A paper receipt slides up beside the speaker and prints one line per step as they say it ("1 clip filmed ✓ … rendered ✓"), ending with a TOTAL line and a cash-register ding. Great for "I did X, then Y, then Z" lines. Needs /fx-setup.
---

# /receipt: steps print on a receipt as they're spoken

**Inputs:** the steps, with the time each one is said, plus the TOTAL text (e.g. `0 apps`).

## HTML (in `#front`)
```html
<div id="receipt"><div class="r-head">CLAUDE ✳ EDIT RECEIPT</div><div class="r-sub">order #0001 · one clip</div><div id="r-lines"></div><div id="r-total"><span>TOTAL</span><span>0 apps</span></div><div class="r-foot">thank you, come again ✌</div></div>
```

## Timeline
```js
const IN = 3.24, OUT = 8.95, TOTAL_AT = 8.58;
const LINES = [[3.5, "1 clip filmed"], [4.7, "dropped in folder"], [5.68, "claude took over"], [6.6, "cut me out"], [7.32, "added the text"], [7.96, "rendered"]];
LINES.forEach(([t, label]) => {
  const d = el("div", null, `<span>${label}</span><span>✓</span>`); $("#r-lines").append(d);
  tl.fromTo(d, { opacity: 0, x: -14 }, { opacity: 1, x: 0, duration: 0.12, ease: "steps(3)" }, t);
});
tl.fromTo("#receipt", { opacity: 0, y: 420, rotation: 2 }, { opacity: 1, y: 0, rotation: -4, duration: 0.45, ease: "back.out(1.4)" }, IN);
tl.fromTo("#r-total", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.25, ease: "back.out(3)" }, TOTAL_AT);
tl.to("#receipt", { y: 700, rotation: 10, duration: 0.4, ease: "power3.in" }, OUT);
chip(IN + 0.06, OUT - 0.1, "receipt");
```

## Sound
- A swoosh when it slides in.
- A typewriter under the printing, at 0.55.
- A cash register on TOTAL, at 0.75.

## Tips
- It sits on the right side over the speaker's arm. Move `left` / `top` in `style.css` (`#receipt`) if a hand gesture matters.
- Keep each label to 18 characters or fewer.
