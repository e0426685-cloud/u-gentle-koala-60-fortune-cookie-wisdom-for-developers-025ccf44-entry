#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer
to /output/entry.txt (1-120 characters, UTF-8, standard library only).
"""

import os

ENTRY = "The bug you cannot reproduce has already reproduced, quietly, in production."

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    if not (1 <= len(line) <= 120):
        raise SystemExit("fortune line is %d chars, must be 1-120" % len(line))
    if "\n" in line:
        raise SystemExit("fortune line must be a single line")


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH))


if __name__ == "__main__":
    main()
