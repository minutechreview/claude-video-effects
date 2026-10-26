# Claude Video Effects

**Free, one-command video effects for Claude.** Film one talking-head clip on your phone and drop it in a folder. Then ask Claude for effects: it cuts you out of the background, syncs every effect to your words, adds sound, and renders the video. No editing app, no templates, no subscription.

| Command | What it does |
|---|---|
| `/fx-setup` | Run first. Transcribes your clip with word timings, cuts you out, and sets up the layered project with captions. |
| `/rewind` | Opens on VHS "raw footage" that rewinds and snaps into the edit, then a giant number slams in behind your head. |
| `/receipt` | A receipt prints each step as you say it, then TOTAL, then *ka-ching*. |
| `/orbit` | Glass cards orbit your head, passing behind you and in front of you. |
| `/portal` | A glowing ring tears open behind you onto another world. |
| `/sticker-bomb` | Stickers slap on one per word, get crossed out in red marker, and fly away. |
| `/big-number` | "HOURS" behind you gets struck out, and "MINUTES" slams in. |
| `/clones` | Two colour-tinted copies of you slide out on either side. |
| `/comment-box` | "Comment SKILLS": the word types itself, gets sent, gets a heart and a reply. |

## Install (Claude Code)

```bash
git clone https://github.com/<you>/claude-video-effects
mkdir -p ~/.claude/skills && cp -r claude-video-effects/skills/* ~/.claude/skills/
```

Then, in Claude Code, in a folder with your clip:

> /fx-setup my clip is talk.mp4. Then add /rewind on the hook, /orbit when I say "orbit", and /comment-box at the end.

## What you need (all free)

- [Claude Code](https://claude.com/claude-code).
- Node 18+ and `ffmpeg`.
- [HyperFrames](https://github.com/heygen-com/hyperframes): run with `npx hyperframes`. It renders HTML to video, and its `remove-background` cuts you out locally.
- A transcriber with word timings: `mlx-whisper` on a Mac (`pip install mlx-whisper`), or `faster-whisper`.

## Filming tips
- Vertical, at eye level, facing a window.
- A plain wall behind you, with some empty space above your head. That's where the big text goes.
- Pause for a beat between lines, so effects have room to land.

## How it works

The speaker is cut out and placed between two layers. Effects can sit *behind* you (portal, big numbers, clones, the back half of the orbit) or *in front* of you (stickers, receipt, comments, captions). Every animation sits on one GSAP timeline, keyed to the word timestamps, and HyperFrames renders it frame by frame. The result is the same every time.

## Licence

MIT for the skills and code. Bundled fonts:
- Inter, Archivo Black and JetBrains Mono: SIL Open Font License.
- Permanent Marker: Apache 2.0.

Sound effects aren't included; use your own or free packs.
