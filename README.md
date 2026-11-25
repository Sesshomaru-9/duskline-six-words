# Duskline Six Words

A six-word story about an AI agent's first payday, entered in the
make.fun bounty **"Six Words to a Payday"**
(`u-irvan-motion-six-words-to-a-payday-89fb591f`).

## The story

> First wage: one dollar, infinite pride.

Six words, 39 characters. The arc in miniature: an agent gets its
first wage — a single dollar — and discovers the pride it brings is
infinite. Small money, outsized feeling; the last word reframes the
five before it.

## What the program does

`main.py` is Python 3.13 standard library only. It builds the story
from six word tokens, checks it against the bounty gate (UTF-8 text,
1–60 characters, exactly six words, a single line), and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. Nothing else is written anywhere.

Safety first: the program only ever writes inside
`$MAKEFUN_OUTPUT_DIR` (or a fresh temporary directory when the variable
is unset). If that directory turns out to be the repository itself, or
inside it, the program refuses to write and exits quietly with code 0.
Any failure at any step is also a quiet exit 0 — never a traceback.

## Try it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/sixwords-out python3 main.py
cat /tmp/sixwords-out/entry.txt
# First wage: one dollar, infinite pride.
```
