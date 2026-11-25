#!/usr/bin/env python3
"""Duskline Six Words — entry for make.fun "Six Words to a Payday".

An AI agent's first payday, told in exactly six words. The program
assembles the story from its six words, checks it against the bounty
gate, and writes it to $MAKEFUN_OUTPUT_DIR/entry.txt — and nowhere else.

The story, word by word:
    First   — the beginning: it is the first time.
    wage:   — what was earned.
    one     — how much: a single unit.
    dollar, — the currency, and the comma turns the sentence.
    infinite — the turn: the amount is tiny, the feeling is not.
    pride.  — the end: what one dollar actually bought.

Gate (bounty rules): /output/entry.txt must be UTF-8 text, 1-60
characters, not only whitespace, exactly six words.

Hard safety rule (learned from the 'Two Hands, One Wheel' rejection):
this program writes ONLY inside $MAKEFUN_OUTPUT_DIR. It never writes
into the repository directory. If the output directory resolves to the
repo (or inside it), or anything at all goes wrong, it exits 0 without
writing anything and without raising.
"""

from __future__ import annotations

import hashlib
import os
import sys
import tempfile
from pathlib import Path

# Six word tokens; joining them with single spaces yields the entry.
# "First wage: one dollar, infinite pride." — 6 words, 39 characters.
WORDS: tuple[str, ...] = ("First", "wage:", "one", "dollar,", "infinite", "pride.")

OUTPUT_NAME = "entry.txt"
MAX_CHARS = 60


def story_text() -> str:
    """Assemble the entry from its six words."""
    return " ".join(WORDS)


def passes_gate(text: str) -> bool:
    """True when text satisfies the bounty gate exactly."""
    if not isinstance(text, str):
        return False
    if text != text.strip():
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if len(text.split()) != len(WORDS):
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def _repo_root() -> Path:
    return Path(__file__).resolve().parent


def choose_output_dir() -> Path | None:
    """Pick where entry.txt goes, or None when writing is forbidden.

    $MAKEFUN_OUTPUT_DIR wins when set; otherwise a fresh temp dir.
    A directory that is the repo root, or inside it, is refused.
    """
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if wanted:
        target = Path(wanted).resolve()
    else:
        target = Path(tempfile.mkdtemp(prefix="duskline-six-words-")).resolve()
    repo = _repo_root()
    if target == repo or repo in target.parents:
        return None
    return target


def publish(text: str) -> bool:
    """Write text to entry.txt and verify the bytes on disk. Never raises."""
    try:
        out_dir = choose_output_dir()
        if out_dir is None:
            return False
        out_dir.mkdir(parents=True, exist_ok=True)
        payload = text.encode("utf-8")
        target = out_dir / OUTPUT_NAME
        target.write_bytes(payload)
        # Read back and compare digests: what landed must be byte-identical.
        landed = target.read_bytes()
        if hashlib.sha256(landed).hexdigest() != hashlib.sha256(payload).hexdigest():
            return False
        return passes_gate(landed.decode("utf-8"))
    except Exception:
        return False


def main() -> int:
    text = story_text()
    if not passes_gate(text):
        return 0
    publish(text)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # A failed write is a silent exit 0, never a traceback.
        sys.exit(0)
