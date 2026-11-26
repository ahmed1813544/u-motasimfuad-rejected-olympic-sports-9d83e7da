#!/usr/bin/env python3
"""Rejected Olympic Sports — program/v1 entry.

Writes one funny single-line sport the Olympics rejected to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only. Deterministic: same bytes on every run.
The line is a single invented event, written to be read aloud by a
broadcaster with a straight face.
"""

import os

LINE = (
    "Synchronised queuing: four athletes stand perfectly still in a "
    "British post office queue, judged on patience, posture, and not "
    "sighing audibly."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
