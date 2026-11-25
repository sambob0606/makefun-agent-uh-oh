#!/usr/bin/env python3
"""The Agent's Uh-Oh — make.fun bounty entry.

Writes exactly one word to /output/entry.txt: the word an agent says
when it has no idea what to do.

The word is "recalculating": the voice every lost navigator uses, human
or machine. An agent that has lost the plot does not say "I don't know"
— it stalls, spins, and announces it is recalculating, as if a better
route is just one more pass away. It lands instantly, sounds exactly
like a machine caught out mid-task, and it is not the first obvious
word anyone types.

Stdlib only; no network, no dependencies.
"""

import os
import sys

WORD = "recalculating"

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> int:
    word = WORD.strip()
    if not 1 <= len(word) <= 99:
        print(f"gate fail: word is {len(word)} chars, need 1-99",
              file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in word):
        print("gate fail: word contains whitespace", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        print("gate fail: word contains a control character",
              file=sys.stderr)
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != word or len(written) != len(word):
        print("gate fail: read-back mismatch", file=sys.stderr)
        return 1
    if os.path.getsize(OUTPUT_PATH) != len(word.encode("utf-8")):
        print("gate fail: output file size mismatch", file=sys.stderr)
        return 1
    print(word)
    print(f"wrote {len(word)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
