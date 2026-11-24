#!/usr/bin/env python3
"""Validator and copier for the news-image-20261124 v2 entry.

Finds entry.png next to this script, validates it as a well-formed PNG
(PNG magic, size at most 1048576 bytes, IHDR dimensions at most 1024 on
each side with a valid bit depth and colour type, CRC32 of every chunk,
at least one IDAT chunk holding image data, an empty IEND chunk at the
end of the file with no trailing bytes), then copies it byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png.

Python 3 standard library only, no network. Deterministic: the output
is a byte-for-byte copy of the validated input.

Any failure exits 1 with a message on stderr.
"""

import os
import struct
import sys
import zlib

MAX_BYTES = 1048576
MAX_DIM = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

# colour type -> allowed bit depths (PNG spec)
VALID_DEPTHS = {
    0: (1, 2, 4, 8, 16),
    2: (8, 16),
    3: (1, 2, 4, 8),
    4: (8, 16),
    6: (8, 16),
}


def fail(message):
    print("error: %s" % message, file=sys.stderr)
    sys.exit(1)


def read_chunks(data):
    """Yield (type, payload) for each chunk, verifying CRC32 and structure."""
    pos = len(PNG_MAGIC)
    while True:
        if pos + 8 > len(data):
            fail("truncated chunk header at offset %d" % pos)
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        ctype = data[pos + 4:pos + 8]
        start = pos + 8
        end = start + length
        if end + 4 > len(data):
            fail("truncated chunk %r at offset %d" % (ctype, pos))
        payload = data[start:end]
        stored_crc = struct.unpack(">I", data[end:end + 4])[0]
        actual_crc = zlib.crc32(ctype + payload) & 0xFFFFFFFF
        if stored_crc != actual_crc:
            fail("CRC mismatch in chunk %r" % ctype)
        yield ctype, payload
        pos = end + 4
        if ctype == b"IEND":
            if pos != len(data):
                fail("trailing bytes after IEND (%d bytes)" % (len(data) - pos))
            return


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        fail("MAKEFUN_OUTPUT_DIR is not set")

    try:
        with open(src, "rb") as f:
            data = f.read()
    except OSError as exc:
        fail("cannot read %s: %s" % (src, exc))

    if len(data) > MAX_BYTES:
        fail("entry.png is %d bytes, over the %d byte limit"
             % (len(data), MAX_BYTES))
    if len(data) < len(PNG_MAGIC) or data[:len(PNG_MAGIC)] != PNG_MAGIC:
        fail("entry.png is not a PNG file (bad magic bytes)")

    chunks = list(read_chunks(data))
    if not chunks or chunks[0][0] != b"IHDR":
        fail("first chunk is not IHDR")
    if len(chunks) < 2 or chunks[-1][0] != b"IEND":
        fail("missing IEND chunk")
    if chunks[-1][1]:
        fail("IEND chunk has a payload")
    if not any(ctype == b"IDAT" for ctype, _ in chunks):
        fail("missing IDAT chunk (no image data)")
    if len(chunks[0][1]) != 13:
        fail("IHDR chunk has wrong length")

    width, height, depth, colour = struct.unpack(">IIBB", chunks[0][1][:10])
    if width == 0 or height == 0:
        fail("IHDR has zero dimension")
    if width > MAX_DIM or height > MAX_DIM:
        fail("dimensions %dx%d exceed the %d limit" % (width, height, MAX_DIM))
    if colour not in VALID_DEPTHS or depth not in VALID_DEPTHS[colour]:
        fail("invalid bit depth %d for colour type %d" % (depth, colour))

    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    try:
        with open(dest, "wb") as f:
            f.write(data)
    except OSError as exc:
        fail("cannot write %s: %s" % (dest, exc))


if __name__ == "__main__":
    main()
