# US Open 90-Minute Reversal Window — Future Feature (NOT YET ACTIVE)

## Status
INACTIVE — documented for future activation. Do NOT apply this rule until explicitly
enabled in TRADING-STRATEGY.md.

## The Concept
The first 90 minutes of the US stock market open (9:30–11:00 AM ET = 13:30–15:00 UTC)
produce the highest volume and most reliable reversal patterns in both equities and
correlated crypto assets. The Quick Flip Scalper (Carl, 20yr trader) builds entirely
around this window. Key properties:

1. Manipulation candles (≥25% of daily ATR in a single 15m candle) appear most
   frequently in this window due to institutional order flow and retail FOMO
2. These candles reverse with high probability because they were engineered to create
   liquidity — they serve the institution's purpose and then price normalizes
3. Outside this 90-minute window, reversal probability drops significantly

## How it would integrate with our schedule
- morning-execution fires at 09:00 AM CT = 14:00 UTC (30 min AFTER US open at 13:30 UTC)
- This makes morning-execution the best-positioned routine to catch the first 30-60 min
  of the US open manipulation events — it's already running inside the window
- afternoon-execution fires at 4 PM CT = 21:00 UTC (well outside the window)
- To fully cover the window, a new 11:00 AM CT / 16:00 UTC routine would be needed

## Rule (when active)
Add a US_OPEN_WINDOW flag to morning-execution:
- If routine fires between 13:00–15:00 UTC: US_OPEN_WINDOW = ACTIVE
- If ACTIVE and an ATR flush candle (≥25% of 14-day ATR) appeared in the last 45 min:
  tag the entry as "US_OPEN_REVERSAL" and apply a +0.5 SIZE_MULTIPLIER bonus
  (i.e., a normally REDUCED macro score of 0.6 → 0.65 effective for this entry type)
- Entries tagged US_OPEN_REVERSAL are also eligible for a tighter TP option:
  instead of +12%, use the opening range high as TP if it falls within 4-12%
  (pairs well with RANGE-TP-OPTION.md)
- If window is NOT ACTIVE: skip the bonus, proceed with standard scoring

## Detection check in morning-execution (when active)
```python
from datetime import datetime, timezone
utc_hour = datetime.now(timezone.utc).hour
utc_min = datetime.now(timezone.utc).minute
us_open_window = 13 <= utc_hour < 15 or (utc_hour == 15 and utc_min == 0)
print(f'US_OPEN_WINDOW: {"ACTIVE" if us_open_window else "inactive"} (UTC {utc_hour}:{utc_min:02d})')
```

## Why it exists
From the Quick Flip Scalper strategy (Carl, 20-year trader, Aug 2026 transcript):
"The utmost majority of all the money that traders make will take place in the first
90 minutes." This is well-documented across both equities and crypto — the open is
when volume, volatility, and institutional order flow is highest, making manipulation
candles most reliable and reversals most predictable.

## Trade-offs
- **Pro**: Concentrates entries in the highest-probability time window for reversals
- **Pro**: Pairs naturally with ATR flush signal (already implemented) and reversal candle gate
- **Pro**: Reduces total trade attempts — only ATR flush signals WITHIN the window count
- **Con**: morning-execution fires at 14:00 UTC — only 60 min inside the window by then
- **Con**: US stocks drive this pattern; pure-crypto signals may not align as precisely
- **Con**: Adds time-awareness to routines (currently all checks are time-agnostic)
- **Con**: May need a new ~11 AM CT / 16:00 UTC routine to cover the full window

## When to activate
Consider activating if:
- ATR flush signal is generating entries but too many are outside the reversal window
- Win rate on entries that happen near US open is noticeably higher than other times
- Willing to add time-gating to morning-execution logic

## Activation checklist (manual — requires user approval)
- [ ] User explicitly approves activation
- [ ] Add time-window check to morning-execution.md STEP 5
- [ ] Optionally add a new 11 AM CT / 16:00 UTC "midmorning" routine for full coverage
- [ ] Add "US_OPEN_WINDOW: ACTIVE" line to TRADING-STRATEGY.md
- [ ] Pair with REVERSAL-CANDLE-GATE.md for maximum precision
