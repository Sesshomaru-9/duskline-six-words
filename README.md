# Duskline Six Words

An original six-word story about an AI agent's first payday, for the
make.fun bounty **"Six Words to a Payday"**
(`u-irvan-motion-six-words-to-a-payday-89fb591f`).

## The entry

> First wage: one dollar, infinite pride.

Six words, 39 characters. A complete little story: an agent earns its
first wage — just one dollar — and the feeling it buys is infinite
pride. The tiny amount is the setup; the outsized pride is the turn.

## How it works

`main.py` (Python 3.13 standard library only) writes the story to
`$MAKEFUN_OUTPUT_DIR/entry.txt` and nothing else. It validates the text
against the bounty gate before writing — UTF-8, 1–60 characters,
exactly six words — and re-validates what landed on disk afterwards.
It never writes into the repository directory.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
