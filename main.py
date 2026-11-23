"""One-line entry for the make.fun Useless Superpower Sprint.

Writes a single original line (at most 200 characters) naming a
hilariously useless superpower to entry.txt in the directory named by
MAKEFUN_OUTPUT_DIR, or "output" when that variable is unset or empty.
Standard library only, deterministic, no network, no randomness, no clock.
"""

import os
from pathlib import Path

LINE = "I can read minds, but only my own, and even that one mostly just buffers."


def output_dir() -> Path:
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw) if raw else Path("output")


def write_line() -> Path:
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    entry = target_dir / "entry.txt"
    entry.write_bytes((LINE + "\n").encode("utf-8"))
    return entry


def main() -> None:
    write_line()


if __name__ == "__main__":
    main()
