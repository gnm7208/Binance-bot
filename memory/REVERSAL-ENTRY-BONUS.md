---
name: REVERSAL-ENTRY-BONUS
status: INACTIVE
source: Carl futures day-trading transcript (2026-08-06)
impact: 6 | bot_fit: 6 | effort: 5
---

# Reversal Entry Bonus — Counter-Trend Into Support (INACTIVE)

Award +1 signal point when price has pulled back 10-20% from its 7-day high AND
an ATR manipulation flush is detected. This identifies potential reversal setups
where institutional money flushed weak hands before re-accumulating.

**Rationale:** Carl's entire strategy is reversal trades — he looks for a move to reverse,
not a continuation. In crypto, the ATR flush (large bearish candle = stop-hunt / shake-out)
followed by a bounce back is exactly this pattern: price dropped hard, smart money absorbed it,
reversal likely.

**Why INACTIVE:** Our current system is momentum-first (24h >= +5% gate). Adding a reversal
bonus while the strategy is still momentum-based would create conflicting signals. Need to
validate that reversal setups have a competitive win rate vs pure momentum plays first.

## Activation Condition

Activate when:
- ≥ 20 closed trades tracked
- At least 5 ATR flush entries closed — compare their win rate vs non-flush entries
- If flush entries win rate >= 55%: add this bonus to the scoring rubric

## Implementation When Active

In morning-research.md STEP 6 ATR flush block, add:
```python
# Check 7-day high for reversal setup
daily7 = fetch(f'https://api.mexc.com/api/v3/klines?symbol={TICKER}&interval=1d&limit=7')
high7 = max(float(d[2]) for d in daily7)
pullback_pct = (high7 - float(daily7[-1][4])) / high7 * 100
reversal_bonus = 1 if (10 <= pullback_pct <= 20 and manip_pts == 1) else 0
print(f'Reversal bonus: {pullback_pct:.1f}% from 7d high | {"+1pt" if reversal_bonus else "0pt"}')
```
Add `reversal_bonus` to SCORE finalization.
Add column `Rev(+1)` to Weighted Signal Table.
