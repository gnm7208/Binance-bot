# Range Take-Profit Option

## Status
ACTIVE — implemented 2026-08-06. impact: 8 | bot_fit: 8 | effort: 4
Applied in: morning-execution.md STEP 5 (step 4c) + STEP 8, afternoon-execution.md STEP 5 + STEP 8.
All monitoring routines updated to check target_price from TRADE-LOG instead of hard-coded +12%.

## The Rule (when active)
Instead of a fixed +12% take-profit, use the previous-day high as the take-profit target
when it is CLOSER than +12%:

1. At entry, fetch previous-day high: `?interval=1d&limit=2` → data[0][2]
2. Compute:
   - standard_tp  = fill_price * 1.12
   - range_tp     = prev_day_high
   - dist_range   = (range_tp - fill_price) / fill_price * 100
3. If dist_range >= 4% AND dist_range < 12%: use range_tp as take-profit level
   Record in TRADE-LOG: `Target: $X.XX (prev-day high, range TP)`
4. If dist_range < 4%: SKIP entry entirely — not enough room to target
5. If dist_range >= 12%: use standard +12% TP as usual

## Why it exists
From the Sneaky Pivot strategy (Doug, 26-year trader, Aug 2026 transcript): previous-day
high acts as a ceiling for many coins — momentum stalls and reverses there. Targeting the
range TP vs holding for +12% increases the probability of a clean exit, especially in
ranging or uncertain macro conditions. More consistent partial wins vs fewer but larger wins.

## Trade-offs
- **Pro**: Higher fill rate on exits — prev-day high is a known magnet level
- **Pro**: Reduces risk of holding through a reversal from resistance
- **Pro**: Better suited to ranging markets (MACRO_SCORE 40-69) than trend markets
- **Con**: Smaller gains per trade — may reduce overall P&L vs +12% in strong trends
- **Con**: Doesn't apply cleanly if prev-day high is above +12% (rare, covered above)
- **Con**: Adds a lookback fetch to every entry calculation

## When to activate
Consider activating if:
- More than 3 trades have touched +8% to +11% and reversed before reaching +12%
- MACRO_SCORE is consistently in 40-69 range (reduced / ranging market)
- Sector momentum is mixed — alternating winners and losers within same sector

## Relationship to current rules
- Still applies the -10% stop from entry (unchanged)
- Still applies trailing stop tighten at +4% gain (unchanged)
- Replaces the +12% fixed target ONLY when prev-day high is in 4%-12% range
- The 3-candle gate (see 3CANDLE-CONFIRMATION-GATE.md) pairs well with this:
  confirm breakout past prev-day high BEFORE entry → use +12% standard TP

## Activation checklist (manual — requires user approval)
- [ ] User explicitly approves activation
- [ ] Add prev-day high TP logic to morning-execution.md STEP 8 and afternoon-execution.md STEP 8
- [ ] Add "RANGE_TP: ACTIVE" line to TRADING-STRATEGY.md
- [ ] Update TRADE-LOG format to record `Target: $X.XX (type: range/standard)`
