#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261124.

Validates the bundled entry.png (a whole PNG, at most 1 MiB and at most
1024 by 1024 pixels) and copies it byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png.

Standard library only. No network access. Deterministic: the same input
bytes always produce the same output bytes.

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import struct
import sys
import zlib

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
MAX_DIMENSION = 1024


def fail(message):
    print("main.py: error: " + message, file=sys.stderr)
    return 1


def read_chunks(data):
    """Yield (chunk_type, chunk_data) for every chunk in a PNG byte string.

    Raises ValueError on any structural problem: bad magic, truncated
    chunk header, chunk length running past the end of the file, or a
    chunk CRC mismatch.
    """
    if data[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file (bad magic bytes)")
    pos = 8
    while pos < len(data):
        if pos + 8 > len(data):
            raise ValueError("truncated chunk header")
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        chunk_type = data[pos + 4:pos + 8]
        start = pos + 8
        end = start + length
        if end + 4 > len(data):
            raise ValueError("chunk %r runs past end of file" % chunk_type)
        chunk_data = data[start:end]
        stored_crc = struct.unpack(">I", data[end:end + 4])[0]
        actual_crc = zlib.crc32(chunk_type + chunk_data) & 0xFFFFFFFF
        if stored_crc != actual_crc:
            raise ValueError("CRC mismatch in chunk %r" % chunk_type)
        yield chunk_type, chunk_data
        pos = end + 4
        if chunk_type == b"IEND":
            if pos != len(data):
                raise ValueError("trailing bytes after IEND")
            break


def validate(data):
    """Check the PNG against the bounty limits. Raises ValueError."""
    if len(data) > MAX_BYTES:
        raise ValueError(
            "file is %d bytes, over the 1048576 byte limit" % len(data))
    if len(data) < 8:
        raise ValueError("file too small to be a PNG")
    chunks = list(read_chunks(data))
    if not chunks or chunks[0][0] != b"IHDR":
        raise ValueError("first chunk is not IHDR")
    ihdr = chunks[0][1]
    if len(ihdr) != 13:
        raise ValueError("IHDR chunk has wrong length")
    width, height, bit_depth, color_type = struct.unpack(">IIBB", ihdr[:10])
    if width == 0 or height == 0:
        raise ValueError("image has zero width or height")
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(
            "image is %dx%d, over the 1024x1024 limit" % (width, height))
    if bit_depth not in (1, 2, 4, 8, 16):
        raise ValueError("unsupported bit depth %d" % bit_depth)
    if color_type not in (0, 2, 3, 4, 6):
        raise ValueError("unsupported color type %d" % color_type)
    if chunks[-1][0] != b"IEND":
        raise ValueError("missing trailing IEND chunk")
    if not any(c[0] == b"IDAT" for c in chunks):
        raise ValueError("no IDAT chunk found")
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    target = os.path.join(output_dir, "entry.png")

    try:
        with open(source, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        return fail("cannot read %s: %s" % (source, exc))

    try:
        width, height = validate(data)
    except ValueError as exc:
        return fail(str(exc))

    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(target, "wb") as handle:
            handle.write(data)
    except OSError as exc:
        return fail("cannot write %s: %s" % (target, exc))

    print("main.py: wrote %s (%dx%d PNG, %d bytes)"
          % (target, width, height, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
