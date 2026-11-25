# SPDX-License-Identifier: MIT
"""Entry generator for the make.fun bounty "The Best Advice I Ever Got".

The competition asks for a single sentence, at most 200 characters, about
the best advice the author ever received. The line below is written in the
voice of someone remembering their grandfather: the advice is concrete,
the twist is that the man giving it immediately broke his own rule, and
the punchline lands on the price he charged for breaking it.
"""

import os
import sys

# The entry: one sentence, kept well under the 200 character limit.
# "Never lend money to family" is the advice; the truck, the tools and
# the twenty bucks are the grandfather breaking it in the same breath;
# "interest in chores" is the part that makes the memory stick.
ENTRY = (
    "My grandfather told me never to lend money to family, then lent me "
    "his truck, his tools, and twenty bucks — and charged me interest "
    "in chores."
)


MAX_CHARS = 200


def validate(text):
    """Check the entry against the competition's hard rules.

    A valid entry is exactly one sentence and no longer than 200
    characters. One sentence means a single terminal full stop at the
    very end and no other sentence-ending punctuation hiding inside.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit"
            % (len(stripped), MAX_CHARS)
        )
    # Exactly one sentence: one full stop, and it must be the last char.
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return stripped


def write_entry(text, out_path="/output/entry.txt"):
    """Write the validated entry to the harness output path.

    The directory is created on demand so the program works both under
    the make.fun harness (which mounts /output) and on a plain local
    run, where the same file is useful for a quick eyeball check.
    """
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    return out_path


def main():
    """Validate the entry, print it, and write it out for grading."""
    entry = validate(ENTRY)
    print(entry)
    print("(%d characters)" % len(entry))
    path = write_entry(entry)
    print("wrote %s" % path)
    return 0


if __name__ == "__main__":
    sys.exit(main())


# Why this line, in one breath: the best advice is rarely a slogan on a
# poster. It is something a real person said once, in a driveway, while
# handing you the keys to something they loved — and then proving, with
# the very next sentence, that even they could not live by it. The
# interest was never money. It was the Saturday mornings spent mowing
# his lawn, which is exactly the kind of debt a grandfather collects.
