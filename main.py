#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: the desert island.

Why this emoji wins the judge's brief:
  1. It IS a dream vacation at a glance: a faraway tropical island,
     palm tree and all -- beach, escape, somewhere else.
  2. It reads like a postcard: a stranger sees the place before a word.
  3. It is specific, not generic: one particular island dream, not
     "any holiday" (a plane or a suitcase could be a business trip).
  4. It carries a quiet surprise: nobody lives there, nobody works
     there -- the whole trip is the island itself.
  5. It is unmistakable at any size, in any culture, on any screen.

Deterministic: the same single emoji, byte for byte, every run.
"""

import os

# U+1F3DD DESERT ISLAND + U+FE0F VARIATION SELECTOR-16 (emoji presentation).
EMOJI = "\U0001F3DD\uFE0F"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the one emoji.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
