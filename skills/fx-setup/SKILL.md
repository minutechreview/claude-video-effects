---
name: fx-setup
description: Set up a talking-head clip for Claude video effects. Transcribes it with word timings, cuts the speaker out of the background (so effects can go behind AND in front of them), and scaffolds a layered HyperFrames project with synced captions. Run this first, then add effects with /rewind, /receipt, /orbit, /portal, /sticker-bomb, /big-number, /clones, /comment-box.
---

# fx-setup: get a clip ready for effects

You turn one vertical talking-head clip (phone video, 9:16) into a layered HyperFrames project:

```
plate  (the original video, keeps the voice)
behind (effects that pass BEHIND the speaker)
me     (the speaker, cut out with a transparent background)
front  (effects in FRONT of the speaker: stickers, cards, captions)
finish (flashes, VHS overlay, vignette)
```

Because the speaker is cut out and sits between "behind" and "front", text and cards can go behind their head, orbit around them, or open a portal behind them while they stay on top.

## Needs (all free, all local)
- Node 18+, `ffmpeg`, and HyperFrames: `npx hyperframes` (https://github.com/heygen-com/hyperframes).
- A transcriber with word timestamps.
  - On a Mac, `mlx_whisper` (`pip install mlx-whisper`).
  - Anywhere else, `whisper` / `faster-whisper`.

## Steps

1. **Make a project folder** and copy `template/` from this skill into it. Put the clip at `src/raw.mp4`.
2. **Make a clean H.264 copy.** Phone clips are often HEVC.
   ```bash
   ffmpeg -i src/raw.mp4 -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart src/clip.mp4
   ```
3. **Transcribe with word timings:**
   ```bash
   ffmpeg -i src/clip.mp4 -ar 16000 -ac 1 a.wav
   mlx_whisper a.wav --model mlx-community/whisper-large-v3-turbo --word-timestamps True -f json -o src
   python3 tools/words.py src/a.json      # prints every word with its start time, and caption chunks
   ```
   Sync every effect to these times. A hit should land on the word that names it.
4. **Cut the speaker out.** This is the slow step: about 1 minute per second of 1080p video on a laptop.
   ```bash
   npx hyperframes remove-background src/clip.mp4 -o src/me.webm --quality best
   ```
   `me.webm` is VP9 with alpha.
   **Holding a mic or a phone?** The person matte often drops dark props, so the mic turns see-through and effects behind you show through it. Put it back:
   ```bash
   python3 tools/fixmic.py src/clip.mp4 src/me.webm src/me-mic.webm   # then use src/me-mic.webm everywhere
   ```
   Edit `BOX` at the top of `fixmic.py` to the area where the prop moves (x0, y0, x1, y1 in pixels). It needs numpy and Pillow.
5. **Captions:** paste the chunks from `words.py` into `CAPS` in `index.html`. Use 2–4 words per chunk and wrap key words in `<em>` for the accent colour.
6. **Set the root duration:** `data-duration` on `#root`, plus `data-duration` on `#plate` and `#me`, all equal to the clip length (`ffprobe`).
7. **Add effects** with the effect skills. Each one says which layer its HTML goes in, what CSS it needs (already in `style.css`), and the timeline code to paste where it says `// FX: effects go here`.
8. **Check and render:**
   ```bash
   npx hyperframes lint && npx hyperframes snapshot --at 1,5,10 -o snaps   # look at the snapshots!
   npx hyperframes render --fps 30 -q delivery -o renders/out.mp4 .
   ffmpeg -i renders/out.mp4 -c:v libx264 -crf 20 -preset slow -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:a aac -b:a 192k -movflags +faststart final.mp4
   ```

## Rules that keep it working
- Keep the GSAP script **inline** in `index.html`; the linter looks for `window.__timelines["main"]` there.
- Don't animate a `<video>`'s own size. Animate its wrapper (`#plate-wrap`, `#me-wrap`, `.clone`).
- Two `<video>` tags with the same `src`, start and duration get deduped. Offset clones by a few hundredths of a second.
- Don't tween `top` / `left`; use `x` / `y` (the renderer snaps layout properties).
- Every `<audio>` needs an `id`, or it's silent.
- Sound effects: mix them loud enough to hear (0.6–0.9) and land them on the visual hit.
