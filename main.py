"""One Star for Monday - make.fun entry.

Writes a one-star review of Monday, written as if Monday were a
restaurant, to /output/entry.txt. The gate requires UTF-8 text of
1-180 characters, non-blank, on a single line of at most 25 words,
with no hashtags, stage directions or explanation attached.
"""

import os
import re
import sys

ENTRY = "One star. The host seated me at 7 a.m. next to the printer, the special was yesterday's emails, and the waiter billed me Monday twice."

MAX_WORDS = 25
MAX_CHARS = 180


def validate(line):
    """Check the entry against the competition gate. Returns (words, chars)."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    words = line.split()
    if not 1 <= len(words) <= MAX_WORDS:
        raise ValueError(f"entry must be 1-{MAX_WORDS} words, got {len(words)}")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "#" in line or "[" in line or "]" in line:
        raise ValueError("entry must be plain text: no hashtags or stage directions")
    if not re.search(r"[A-Za-z]", line):
        raise ValueError("entry must contain text")
    line.encode("utf-8")  # gate requires UTF-8 text
    return len(words), len(line)


def main():
    words, chars = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote /output/entry.txt ({words} words, {chars} chars)")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"gate check failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
