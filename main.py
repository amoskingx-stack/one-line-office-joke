#!/usr/bin/env python3
"""One-Line Office Joke — make.fun bounty entry.

Writes one original one-line joke about office life to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Stdlib only, no network, no randomness: every run writes the exact same
bytes, so the entry is deterministic as the harness requires.
"""

import os
from pathlib import Path

# Original joke, written for this entry: one line, one sentence, setup and
# punchline on the same line. 90 characters, well inside the 200 limit.
JOKE = (
    "My boss says we're a family here, "
    "so I asked HR if I can be adopted by another department."
)


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
