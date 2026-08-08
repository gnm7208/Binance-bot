# Self-Learning Trade Review

**Status:** ACTIVE | **Impact:** 8 | **Bot Fit:** 9 | **Effort:** 5

## What It Does

At the start of every morning-research session (STEP 1B), the bot reads its own
TRADE-LOG and computes win rates by signal score band and by sector. Results are
logged in RESEARCH-LOG under "Self-learning" and used to adjust watchlist priorities.

## Logic

Signal score bands (based on current 0-20 scale):
- Low band (5-8): if win_rate < 40% → flag LOW_BAND_UNDERPERFORMING → prefer score >= 9
- Mid band (9-12): if win_rate < 50% → flag MID_BAND_UNDERPERFORMING
- High band (>=13): if win_rate < 60% → flag HIGH_BAND_UNDERPERFORMING

Sector tracking: if any sector has win_rate < 40% across >= 3 closed trades →
flag SECTOR_WEAK (softer than SECTOR_BLOCKED which requires 2 consecutive losses).

Also includes anomaly scan (STEP 1E):
- A: consecutive HOLD days with tradeable macro → alert if >= 3
- D: rolling 10-trade loss rate > 50% → alert

## Implementation

Added as STEP 1B and STEP 1E in morning-research.md. No extra API calls — uses
TRADE-LOG data already read in STEP 1.

## Why

A stateless bot running from git-as-memory can drift without realizing it. Reading
closed-trade outcomes before each session closes the feedback loop: if low-score
entries are consistently losing, the bot should self-correct by raising its bar —
without a human having to notice and intervene.

## Source

YouTube video research (algorithmic trading feedback loop content), Aug 2026.
