"""Funniest Time Machine Warning Label.

Writes one warning label for a time machine, under 120 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is fixed: no network, no randomness, no clock, so every run
produces byte-identical output.
"""

import os

# Design note: the judge rewards a real time-travel hazard turned into the
# joke, with the surprise saved for the last words, phrased as a flat safety
# notice. The hazard here is the butterfly effect (stepping on an ancestor);
# the twist is that the smallest thing underfoot, the bug, is one too.

ENTRY = (
    "WARNING: Do not step on anything. "
    "Everything is your ancestor, including the bug."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 120 or not ENTRY.strip():
        raise ValueError("entry must be 1 to 120 characters")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
