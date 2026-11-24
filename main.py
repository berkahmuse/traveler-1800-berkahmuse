#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 -- @berkahmuse entry.

Writes a single sentence (at most 200 characters) that explains the
modern internet to a time traveler who has just stepped out of the
year 1800, using only things a person of that year already knows: a
road, a post office, a library, a market stall, a letter, a book.

The sentence is fixed in this file, so the program is fully
deterministic: every run writes the exact same bytes to
/output/entry.txt. The gate is checked here too (UTF-8, 1-200
characters, not only whitespace, exactly one line) and the run fails
loudly if the sentence ever stops passing it; after writing, the file
is read back and verified byte-for-byte against the sentence.
"""

import hashlib
import os
import sys

SENTENCE = (
    "Picture one road joining every library, post office, and market "
    "stall on earth, so a letter you send arrives before your ink "
    "dries and the book you seek is in your hands at once."
)


def main() -> int:
    text = SENTENCE
    chars = len(text)
    if not 1 <= chars <= 200:
        print(f"gate fail: sentence is {chars} chars, must be 1-200",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: sentence is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate fail: sentence must be exactly one line",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        if f.read() != data:
            print("gate fail: written file does not match the sentence",
                  file=sys.stderr)
            return 1
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {path}: {chars} chars, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
