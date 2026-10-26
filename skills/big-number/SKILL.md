---
name: big-number
description: A giant outlined word or number appears BEHIND the speaker ("HOURS"), gets struck through with an accent bar, collapses, and the replacement slams in ("MINUTES"). For before/after or "X is now Y" lines. Needs /fx-setup.
---

# /big-number: the "before" gets struck out, the "after" slams in

**Inputs:**
- `OLD` text and when it's said (`T_OLD`).
- `NEW` text and when it's said (`T_NEW`).
- `OUT`: when it leaves.

## HTML (in `#behind`)
```html
<div id="hours" class="bignum">HOURS</div>
<div id="minutes" class="bignum accent">MINUTES</div>
```

## Timeline
```js
const T_OLD = 20.26, T_NEW = 21.54, OUT = 22.0;
const strike = { v: 0 };
tl.fromTo("#hours", { opacity: 0, scale: 1.35 }, { opacity: 1, scale: 1, duration: 0.3, ease: "expo.out" }, T_OLD);
tl.to(strike, { v: 1, duration: 0.3, ease: "power3.out", onUpdate: () => $("#hours").style.setProperty("--strike", strike.v) }, T_OLD + 0.7);
tl.to("#hours", { scaleY: 0, opacity: 0, duration: 0.18, ease: "power3.in" }, T_NEW - 0.12);
tl.fromTo("#minutes", { opacity: 0, scale: 2.4 }, { opacity: 1, scale: 1, duration: 0.3, ease: "expo.out" }, T_NEW);
tl.to("#minutes", { y: -200, opacity: 0, duration: 0.25, ease: "power2.in" }, OUT);
chip(T_OLD, OUT + 0.05, "big-number");
```

## Sound
- A bass impact on `OLD` (0.75).
- A fast whoosh and a pop on `NEW` (0.9).

## Tips
- It sits above the head (`top: 150px`). Words of 7 characters or fewer fit at the default size.
- Numbers work too, e.g. `3 HRS` becomes `2 MIN`.
