#!/usr/bin/env python3
"""Write a Monday morning punchline to /output/entry.txt."""

# Monday declines to start until the coffee threshold is met.
import os
from pathlib import Path

LINE = "Monday walked in, saw my to-do list, and said: 'I'll come back when you've had coffee.'"

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
