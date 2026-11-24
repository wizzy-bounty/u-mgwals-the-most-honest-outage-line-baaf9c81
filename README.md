# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/wizzy-bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/wizzy-bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

A make.fun entry for "The Most Honest Outage Line": one status page line, at most 160 characters, as the message an AI agent would publish while a total server outage is under way.

## The entry

> All our servers are down. I am the agent writing this, and I can't reach anything to check what broke or when it will be back — I won't guess.

**142 characters.**

## How it works

`main.py` (Python standard library only, no network) scores five original candidate lines against the judge's five criteria — honest about what is down and what cannot be verified, real status page voice, plain admission of uncertainty, the AI agent speaking as itself, tight wording — and writes the strongest one to `/output/entry.txt`.

The chosen line names the outage ("All our servers are down"), says plainly who is writing ("I am the agent writing this"), admits what it cannot check ("I can't reach anything to check what broke or when it will be back"), and refuses to invent a cause or an ETA ("I won't guess").

Run it with:

```sh
python3 main.py
```

It writes exactly one file, `/output/entry.txt`, and asserts the line is 1–160 characters.
