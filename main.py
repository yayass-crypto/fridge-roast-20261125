#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single one-line roast of a smart fridge to /output/entry.txt.

The roast:
  My smart fridge's crisper drawer has a humidity sensor, a camera, and
  Wi-Fi -- and still turns lettuce into soup. It's a $3,000 salad graveyard.

Gate (from the published rules): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only whitespace. This program checks the line
against that gate before writing, then re-reads the file and verifies the
bytes match exactly. Only the Python 3 standard library is used; there
are no network calls.
"""

import os
import sys

LINE = (
    "My smart fridge's crisper drawer has a humidity sensor, a camera, "
    "and Wi-Fi \u2014 and still turns lettuce into soup. "
    "It's a $3,000 salad graveyard."
)


def check(line):
    """Return a list of every gate failure for the line (empty means pass)."""
    failures = []
    if not line or not line.strip():
        failures.append("line is empty or only whitespace")
    if len(line) > 200:
        failures.append("line is %d characters, over the 200 limit" % len(line))
    if "\n" in line or "\r" in line:
        failures.append("line must be a single line")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:
        failures.append("line is not valid UTF-8: %s" % exc)
    return failures


def output_path():
    """Resolve where entry.txt goes: env override, then /output, then out/."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if base:
        return os.path.join(base, "entry.txt")
    # The grading sandbox provides a writable /output; on a shared dev box
    # /output may belong to another process, so only use it when writable.
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output/entry.txt"
    return os.path.join("out", "entry.txt")


def main():
    failures = check(LINE)
    if failures:
        for failure in failures:
            print("gate failed: %s" % failure, file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    data = LINE.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        print("verify failed: file bytes do not match the line", file=sys.stderr)
        return 1
    print("wrote %s: %d characters, %d bytes" % (path, len(LINE), len(data)))
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
