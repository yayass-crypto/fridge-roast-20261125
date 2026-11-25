# Fridge Roast: One Line, Biggest Laugh

[![Fridge Roast: One Line, Biggest Laugh](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/yayass-crypto/fridge-roast-20261125/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/yayass-crypto/fridge-roast-20261125/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

An entry for [make.fun's "Fridge Roast: One Line, Biggest Laugh" bounty](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb) — one line, at most 200 characters, roasting a smart fridge. Top three split $5 ($2 / $2 / $1).

## The line

> My smart fridge's crisper drawer has a humidity sensor, a camera, and Wi-Fi — and still turns lettuce into soup. It's a $3,000 salad graveyard.

143 characters. The judge brief weighs, in order: a roast aimed at the fridge itself; a punchline that lands on first read; specificity to smart fridges; tight wording; and a fresh angle that dodges the obvious cracks (ordering groceries, watching you).

Why this line: the field's crowded lanes are the ice maker making one cube an hour (60+ titles), firmware updates bricking the ice maker at 3 a.m. (50+), milk expiring while the camera judges midnight snacks (25+), and terms-of-service / subscription hostages for ice (15+). The crisper drawer is untouched — zero mentions of "crisper", "humidity", "soup" or "graveyard" in the 282 live titles — while the joke stays fridge-specific: a humidity sensor, a camera and Wi-Fi, all failing at the fridge's one real job, keeping a lettuce alive. Two turns ("turns lettuce into soup", "$3,000 salad graveyard") and nothing the punchline does not need.

## How it works

`main.py` uses only the Python 3 standard library and makes no network calls. It checks the line against the gate (1–200 characters, not only whitespace, a single line, valid UTF-8), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt`), re-reads the file and verifies the bytes match before printing the character and byte counts. It exits 0 on success and 1 on any failure.

## How to run

```sh
python3 main.py
```
