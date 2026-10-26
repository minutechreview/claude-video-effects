---
name: comment-box
description: An Instagram-style comment sheet slides up, the keyword types itself ("SKILLS"), it's sent, a heart pops, and a reply lands ("Link sent! check your DMs 📩"). The call to action for "comment X and I'll send you the link". Needs /fx-setup.
---

# /comment-box: the "comment X" call to action, acted out

**Inputs:**
- `KEYWORD` and when it's typed.
- The reply text.
- The account name shown on the reply.

## HTML (in `#front`)
```html
<div id="comment"><div class="c-sheet"><div class="c-title">Comments</div><div id="c-posted"></div><div class="c-row"><div class="c-avatar"></div><div class="c-input"><span id="c-typed"></span><i class="caret"></i></div><div id="c-send">➤</div></div></div></div>
```

## Timeline
```js
const IN = 25.98, TYPE = 26.45, SEND = 26.86, REPLY = 28.2, OUT = 31.25;
const KEYWORD = "SKILLS", HANDLE = "yourhandle";
tl.fromTo("#comment", { opacity: 0, y: 260 }, { opacity: 1, y: 0, duration: 0.4, ease: "back.out(1.3)" }, IN);
for (let i = 1; i <= KEYWORD.length; i++) tl.call(() => { $("#c-typed").textContent = KEYWORD.slice(0, i); }, null, TYPE + i * 0.065);
tl.to("#c-send", { opacity: 1, scale: 1.3, duration: 0.1, yoyo: true, repeat: 1 }, SEND);
tl.call(() => { $("#c-typed").textContent = ""; }, null, SEND + 0.09);
const mine = el("div", "post", `<div class="c-avatar"></div><div><b>you</b><p>${KEYWORD} 🔥</p></div><span class="heart">♥</span>`);
const reply = el("div", "post", `<div class="c-avatar"></div><div><b>${HANDLE}</b><p>Link sent! check your DMs 📩</p></div>`);
$("#c-posted").append(mine, reply);
tl.fromTo(mine, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.25 }, SEND + 0.09);
tl.call(() => mine.querySelector(".heart").classList.add("on"), null, SEND + 0.34);
tl.fromTo(mine.querySelector(".heart"), { scale: 1 }, { scale: 1.7, duration: 0.12, yoyo: true, repeat: 1 }, SEND + 0.34);
tl.fromTo(reply, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.25 }, REPLY);
tl.to("#comment", { y: 40, opacity: 0, duration: 0.3, ease: "power2.in" }, OUT);
chip(IN, OUT - 0.05, "comment-box");
```

## Sound
- A swoosh on IN.
- Keyboard taps while typing (0.5).
- A click on send.
- A "favourite" sparkle on the heart.
- A message ding on the reply.

## Tips
- The sheet sits mid-low, over the hands. Keep captions below it (`#captions` is at `top: 1700px`).
- Use the creator's real handle for the reply.
