---
name: EXTENDED-TP-HIGH-CONVICTION
status: INACTIVE
source: Carl futures day-trading transcript (2026-08-06)
impact: 6 | bot_fit: 6 | effort: 7
---

# Extended Take-Profit for High-Conviction Entries (INACTIVE)

When signal score >= 11/17, use +18% take-profit target instead of the standard +12%.
Same stop logic (-10% entry, trailing tighten at +4%). Just a wider TP for the
highest-conviction positions.

**Rationale:** Carl's core insight — with a 1:3 R:R, you only need a 30% win rate to be
profitable. Our highest-conviction entries (score >=11) deserve more room to run.

**Why INACTIVE:** Need ≥15 closed trades to calibrate whether score-11+ entries
historically reach +18% before reversing, or get stopped out first.

## Activation Condition

Activate when:
- ≥ 15 closed trades in TRADE-LOG
- Win rate on score ≥ 11 entries is ≥ 60% over those trades
- At least 3 of those trades hit +12% TP cleanly (not stopped out on the way)

## Implementation When Active

In TRADING-STRATEGY.md Sell-Side Rules:
> "Take profit: +12% (standard) | Score >= 11: +18% target — log EXTENDED_TP in TRADE-LOG"

In morning-research.md STEP 7 Trade Ideas format:
> "Target $X (+18% for score>=11, +12% otherwise)"

In all monitoring routines: replace `P&L >= +12%` check with:
> "If SCORE >= 11 AND recorded as EXTENDED_TP: close at +18%. Else close at +12%."
