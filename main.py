#!/usr/bin/env python3
"""One-Line Office Joke entry — one office joke, max 200 characters.

Writes the joke to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Stdlib only, deterministic, no network.
"""

import os
import sys

JOKE = "I filed a ticket to fix the ticket system — it auto-closed itself as 'resolved by design.'"


def main() -> int:
    text = JOKE
    # Gate check: 1-200 characters, not whitespace-only.
    if not (1 <= len(text) <= 200) or not text.strip():
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back: the file must hold exactly the joke, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("entry mismatch after write", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
