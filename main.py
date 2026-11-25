#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email — make.fun entry.

Writes one line of plain text, at most 200 characters, to
/output/entry.txt: a single joke about a meeting that should have
been an email. Deterministic, no network, no input, stdlib only.
"""

import os
from pathlib import Path

LINE = (
    "The meeting's only action item was to email a summary of the "
    "meeting \u2014 an email, but with snacks and a calendar invite."
)


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 characters, got {len(text)}"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
