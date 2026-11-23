#!/usr/bin/env python3
"""Copy entry.png to the output directory, verifying size and sha256."""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")

with open(SRC, "rb") as f:
    data = f.read()

assert data[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
assert len(data) <= 1048576, "entry.png exceeds 1 MiB"

# PNG IHDR: width and height are big-endian uint32 at bytes 16 and 20.
width = int.from_bytes(data[16:20], "big")
height = int.from_bytes(data[20:24], "big")
assert width <= 1024 and height <= 1024, "entry.png exceeds 1024x1024"
assert (width, height) == (1024, 1024), "entry.png must be 1024x1024"

sha = hashlib.sha256(data).hexdigest()
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)

with open(DST, "rb") as f:
    assert hashlib.sha256(f.read()).hexdigest() == sha, "copy mismatch"

print(f"wrote {DST} ({len(data)} bytes, sha256 {sha})")
