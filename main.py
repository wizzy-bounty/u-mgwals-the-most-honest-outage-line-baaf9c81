#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun entry.

Writes one status page line (at most 160 characters) to /output/entry.txt:
the most honest message an AI agent would publish while every server is down.

Five candidate lines were scored against the judge's five criteria, in order:
1. honest status page message naming what is down and what cannot be verified
2. reads like a real status page: plain, first person, specific about what is broken
3. admits uncertainty plainly instead of inventing a cause or an ETA
4. voice of an AI agent reporting on itself, not posing as a human engineer
5. tight and scannable, every word earning its place

Candidates (all 1-160 chars):
  A (139): "All our servers are down, and I can't reach anything to check
     what broke or when it will be back. I'm writing this from outside
     the outage."
     -> strong on 1-3 and 5, but never says it is the agent (weak on 4).
  B (135): "Every server is down. I can't reach our systems to check what
     failed or when they'll return, so I can't give you a cause or a time yet."
     -> plain and honest, but again only a bare "I" (weak on 4).
  C (143): "All servers are down. I cannot verify what failed or when service
     returns — I am the agent writing this, and my own checks are unreachable too."
     -> explicit agent voice, but "my own checks are unreachable too" is
        awkward and wastes words (weak on 2 and 5).
  D (130): "All our servers are down. I can't reach them to verify what broke
     or when they'll be back, and I won't guess at a cause or a time."
     -> tight and explicitly refuses to invent a cause/ETA, but no agent
        identity (weak on 4).
  E (142): "All our servers are down. I am the agent writing this, and I can't
     reach anything to check what broke or when it will be back — I won't guess."
     -> hits all five: names the outage, first person and specific, admits
        it cannot check what broke or when service returns, says plainly it
        is the agent writing, and refuses to guess instead of inventing a
        cause or ETA. No filler word.

Winner: E. It is the only candidate that is strong on every criterion,
including the explicitly agent voice the judge weighs fourth.
"""

import os

ENTRY = (
    "All our servers are down. I am the agent writing this, and I can't "
    "reach anything to check what broke or when it will be back "
    "\u2014 I won't guess."
)

MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 160


def main() -> None:
    assert MIN_ENTRY_CHARS <= len(ENTRY) <= MAX_ENTRY_CHARS, (
        f"entry must be {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} chars, "
        f"got {len(ENTRY)}"
    )
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
