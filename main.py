"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler from the year 1800, to /output/entry.txt.

The sentence is built only from things a person from 1800 already knows
-- a library, a post office, a marketplace, a road, a letter -- so the
traveler can actually picture it. One image carries the whole idea:
every library, post office and marketplace in the world joined by one
road, where any letter arrives in a blink and anyone may read it or
answer back. That covers what the internet *is* (one road joining the
world's stores of knowledge, mail and trade) and what it *does* (any
message arrives at once, and anyone may read or reply).

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
only white space. This program checks the length itself and exits
non-zero if the sentence ever falls outside the gate.
"""

import os
import sys

ENTRY = (
    "Imagine every library, post office, and marketplace in the world "
    "joined by one road, so any letter arrives in a blink and anyone "
    "may read it or answer back."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(text):
    """Check the sentence against the bounty gate. Returns an error string or None."""
    if not text or not text.strip():
        return "entry is empty or only white space"
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        return "entry is %d characters, outside the %d-%d gate" % (
            len(text),
            MIN_CHARS,
            MAX_CHARS,
        )
    if text.strip().count(".") != 1 or not text.strip().endswith("."):
        return "entry must be exactly one sentence"
    return None


def write_entry(text, path=OUTPUT_PATH):
    """Write the sentence to path, creating the output directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def main(argv=None):
    """Validate the sentence, write it, and report its length."""
    error = validate_entry(ENTRY)
    if error is not None:
        print("invalid entry: %s" % error, file=sys.stderr)
        return 1
    path = write_entry(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), path))
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
