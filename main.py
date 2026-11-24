"""One-line office joke entry for make.fun.

The joke: a meeting to declare the last meeting an email. Numbers up
front (45 minutes, 12 people) ground the setup; the line runs straight
to the punchline — the decision was emailed to no one, so the cycle
repeats on Thursday. One sentence, one line, 136 characters.
"""

import os
import sys

TEXT = (
    "45 minutes, 12 people, one meeting to declare the last meeting "
    "an email \u2014 the decision was emailed to no one, "
    "so we meet again Thursday."
)


def main() -> int:
    # Gate: one line, 1-200 characters, not only whitespace.
    if not TEXT or not TEXT.strip():
        print("gate failed: empty entry", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print(f"gate failed: {len(TEXT)} chars > 200", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("gate failed: entry is not one line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Read back and verify byte-for-byte.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
