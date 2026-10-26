"""Print word timings and ready-made caption chunks from a whisper JSON (word_timestamps on).

Usage: python3 tools/words.py src/a.json
"""
import json
import sys

data = json.load(open(sys.argv[1]))
words = [w for s in data["segments"] for w in s.get("words", [])]
print("WORDS:", " ".join(f"{w['word'].strip()}@{w['start']:.2f}" for w in words))
print("\nconst CAPS = [")
chunk, start = [], None
for i, w in enumerate(words):
    text = w["word"].strip().upper()
    if start is None:
        start = w["start"]
    chunk.append(text)
    nxt = words[i + 1] if i + 1 < len(words) else None
    gap = (nxt["start"] - w["end"]) if nxt else 1
    if len(chunk) >= 3 or text.endswith((".", ",", "?", "!")) or gap > 0.25 or nxt is None:
        end = nxt["start"] if nxt and gap < 0.4 else w["end"] + 0.15
        print(f'  [{start:.2f}, {end:.2f}, "{" ".join(chunk).rstrip(".,")}"],')
        chunk, start = [], None
print("];")
