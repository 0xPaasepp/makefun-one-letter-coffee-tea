#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- entry program.

Writes exactly one letter to /output/entry.txt: "A", for coffee.

Why coffee: of the two drinks, coffee is the more vivid answer -- dark,
bitter, steaming, a jolt that starts the day -- and the funnier one, the
drink behind every "don't talk to me before coffee" joke. It is also the
truer one: the honest admission that the day does not start until the
first cup. One letter, nothing beside it: no word, no gloss, no
punctuation, no trailing newline.
"""

import os

LETTER = "A"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(LETTER) != 1 or not LETTER.isascii() or not LETTER.isalpha():
        raise ValueError("entry must be exactly one ASCII letter")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
