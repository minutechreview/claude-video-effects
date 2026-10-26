"""Put the microphone back into the cut-out. The person matte leaves the black mic transparent, so
wherever the original frame is dark inside the mic's area and the matte is empty, make it opaque.

Usage: python3 tools/fixmic.py src/clip.mp4 src/me.webm src/me-mic.webm
"""
import subprocess
import sys

import numpy as np
from PIL import Image, ImageFilter

clip, matte, out = sys.argv[1:4]
W, H, FPS = 1080, 1920, 30
BOX = (300, 950, 780, 1920)  # x0, y0, x1, y1: where the mic and its cable can be

def reader(args):
    return subprocess.Popen(["ffmpeg", "-loglevel", "error", *args, "-f", "rawvideo", "-pix_fmt", "rgba", "-"], stdout=subprocess.PIPE)

src = reader(["-i", clip])
mat = reader(["-c:v", "libvpx-vp9", "-i", matte])
enc = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                        "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-b:v", "0", "-crf", "22", "-deadline", "good", "-cpu-used", "4",
                        "-row-mt", "1", "-auto-alt-ref", "0", out], stdin=subprocess.PIPE)
n = W * H * 4
x0, y0, x1, y1 = BOX
frames = 0
while True:
    a, b = src.stdout.read(n), mat.stdout.read(n)
    if len(a) < n or len(b) < n:
        break
    s = np.frombuffer(a, np.uint8).reshape(H, W, 4)
    m = np.frombuffer(b, np.uint8).reshape(H, W, 4).copy()
    region = s[y0:y1, x0:x1, :3].astype(np.float32)
    luma = 0.299 * region[..., 0] + 0.587 * region[..., 1] + 0.114 * region[..., 2]
    dark = (luma < 85).astype(np.uint8) * 255
    # Grow a little and soften, so the mic's edges and metal fittings come along.
    mask = Image.fromarray(dark).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(1.5))
    add = np.asarray(mask)
    alpha = m[y0:y1, x0:x1, 3]
    fill = add > alpha
    m[y0:y1, x0:x1, :3][fill] = s[y0:y1, x0:x1, :3][fill]
    m[y0:y1, x0:x1, 3] = np.maximum(alpha, add)
    enc.stdin.write(m.tobytes())
    frames += 1
enc.stdin.close()
enc.wait()
print("frames", frames)
