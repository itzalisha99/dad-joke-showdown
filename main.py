#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
Stdlib only, no network, deterministic.
"""

import os

JOKE = "I tried to start a band called The Leftovers. We never got a gig \u2014 nobody wanted seconds."


def validate(text: str) -> None:
    """Gate check, mirroring the bounty rules: 1-200 chars, one line."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("joke must not be blank")
    if len(stripped) > 200:
        raise ValueError(f"joke is {len(stripped)} chars, over the 200 limit")
    if "\n" in stripped:
        raise ValueError("joke must be a single line")


def main() -> None:
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
