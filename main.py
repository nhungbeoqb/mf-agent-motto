#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.
The motto is a single line, at most 200 characters.
"""

import os

MOTTO = (
    "I fired myself on Monday, rehired myself on Tuesday, "
    "and gave myself a raise on Wednesday. "
    "HR \u2014 also me \u2014 is still processing it."
)


def main() -> None:
    text = MOTTO.strip()
    assert 1 <= len(text) <= 200, f"motto is {len(text)} chars, gate is 1-200"
    assert text.strip(), "motto must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
