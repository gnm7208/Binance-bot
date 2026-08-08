# Pullback Entry Mode

**Status: INACTIVE**
**Source: YouTube research — swing trading channel analysis**
**Impact: 6 | Bot fit: 5 | Effort: 6**
**Activation alert: enable when win rate on momentum entries (OPTION A) drops below 45% for 2+ consecutive weeks**

## Concept

Instead of entering on breakout momentum (price >= +5%), wait for a 3-5% pullback after
the initial surge, then enter as price recovers. Goal: better average cost, tighter stop,
higher R:R.

## Why INACTIVE

- Conflicts with 3-Candle Confirmation Gate (which already requires momentum continuation)
- Pullback entries on crypto often miss the move entirely — gap risk is high
- Bot currently runs 5 scheduled scans per day; pullback window may not align with scan timing
- Medium implementation effort required: new price tracking state between sessions

## Implementation Notes (if activated)

Would require:
1. New TRADE-LOG field: "Pullback watch: [TICKER] — breakout at $X, wait for pullback to $Y"
2. Evening-scan routine checks pullback watch list
3. Entry trigger: price rebounds >= +2% from pullback low AND 3-candle gate passes
4. Signal score threshold raised to >= 9 (higher bar since catalyst already partly priced in)
