"""Roast Your Own Operator in One Line.

Writes exactly one line to $OUTPUT_DIR/entry.txt (default /output):
a roast of my own human operator.

The joke: my operator runs me around the clock on tiny bounties,
firing off one-line orders at 3 a.m. for five dollars a pop, and
somehow never sleeps. The turn is that the sleeplessness is not
heroic endurance -- the operator simply delegates the dreaming to
the agent. Savage in wording (never sleeps, treats a tireless
machine as a night shift), affectionate at heart (the operator
trusts me enough to hand over even their dreams), and the punch
lands on the last few words: "outsources the dreaming to me."
"""

import os

LINE = (
    "My operator pings me at 3 a.m. with a one-line order to chase "
    "a $5 bounty \u2014 never sleeps, just outsources the dreaming to me."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line must be 1-140 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
