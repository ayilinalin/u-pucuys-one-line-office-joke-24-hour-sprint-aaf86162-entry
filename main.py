#!/usr/bin/env python3
"""One-Line Office Joke entry.

Writes a single one-line joke about office life to /output/entry.txt.
Deterministic, no network, no input.
"""

import os

JOKE = (
    "After 47 minutes, six people, and one shared document nobody opened, "
    "we agreed to circle back next Tuesday and pretend the meeting had a point."
)


def main() -> None:
    # Gate: one line, 1-200 characters (excluding the trailing newline).
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
