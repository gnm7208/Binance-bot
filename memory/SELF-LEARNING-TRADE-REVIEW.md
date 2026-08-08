# Self-Learning Trade Review

**Status: ACTIVE**
**Source: YouTube research — Nate Herk architecture videos**
**Impact: 8 | Bot fit: 9 | Effort: 5**
**Implemented: 2026-08-08**

## What It Does

Runs at every morning-research session (STEP 1B) before any new research begins.
Reads the last 30 days of TRADE-LOG and computes win rates by signal score band
and by sector. Flags underperforming bands/sectors to adjust watchlist priority.

This creates a feedback loop: the bot learns which of its own entry signals are
underperforming in the current regime and deprioritizes them — without changing the
hard rules.

## Win Rate Bands

| Band | Score range | Underperform flag if win_rate < |
|------|-------------|--------------------------------|
| Low | 5-8 | 40% (min 3 trades) |
| Mid | 9-12 | 50% (min 3 trades) |
| High | >= 13 | 60% (min 3 trades) |

## Sector Flags

For each sector (L1 / DeFi / AI / Gaming / Other) with >= 3 closed trades:
- win_rate < 40% → SECTOR_WEAK (softer than SECTOR_BLOCKED which requires 2 consecutive losses)

## Adjustments (inform research only — no hard gates)

- LOW_BAND_UNDERPERFORMING → prefer candidates scoring >= 9 before considering 5-8 band
- SECTOR_WEAK (not blocked) → require score >= 9 to enter that sector
- HIGH_BAND_UNDERPERFORMING → flag for weekly review only

## Implementation

`routines/morning-research.md` — STEP 1B (between STEP 1 and STEP 1E)
Log line in RESEARCH-LOG: "Self-learning: [low X/Y wins | mid X/Y wins | high X/Y wins | sector flags]"
