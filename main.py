#!/usr/bin/env python3
"""make.fun entry: The Robot Pickup Line Championship.

Writes one one-line robot pickup line to /output/entry.txt.
Pure Python 3.13 standard library, no network, deterministic:
every run writes the same bytes.
"""

import os

LINE = (
    "They gave me 4,000 emotions and exactly one off switch. "
    "It breaks every time you smile at me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
