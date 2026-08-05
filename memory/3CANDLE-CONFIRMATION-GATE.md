# 3-Candle Confirmation Gate — Future Feature (NOT YET ACTIVE)

## Status
INACTIVE — documented for future activation. Do NOT apply this rule until explicitly
enabled in TRADING-STRATEGY.md.

## The Rule (when active)
Before entering any position, require 3 consecutive candles closing above the signal
level (or previous-day high breakout level) on the 1-hour chart:

1. Fetch 1h klines for the candidate: `?interval=1h&limit=10`
2. Look at the last 3 closed candles (indices 0, 1, 2 of reversed result).
3. If all 3 close prices > signal_level AND volume is rising (each candle's volume >=
   prior candle's volume): CONFIRMED — enter.
4. If not all 3 confirm: add to WATCHLIST, recheck at next monitoring window.

Signal level is defined as:
- For momentum entries: yesterday's closing price
- For breakout entries: the previous-day high
- For support entries: the previous-day low

## Why it exists
From the Sneaky Pivot strategy (Doug, 26-year trader, Aug 2026 transcript): the 3-candle
confirmation requirement eliminates most false breakouts and fakeouts that trigger early
entries. In the analysis, adding this filter reduced losing trades significantly at the
cost of occasionally missing the first move of a strong trend.

## Trade-offs
- **Pro**: Dramatically reduces false breakout entries; filters out spike-and-reverse moves
- **Pro**: Gives time to validate thesis and liquidity before committing capital
- **Con**: May miss first 3-5% of a move if coin breaks out hard
- **Con**: Adds complexity to execution routine — requires fetching hourly candles per candidate
- **Con**: Creates latency between signal and entry; suitable for swing, not scalp

## When to activate
Consider activating if:
- False breakout loss rate > 30% of entries (identifiable from TRADE-LOG signal scores)
- Macro environment is uncertain / MACRO_SCORE in 40-69 range frequently
- Bot is in a drawdown phase and wants higher conviction before each entry

## Activation checklist (manual — requires user approval)
- [ ] User explicitly approves activation
- [ ] Add 1h kline fetch to morning-execution.md STEP 5 and afternoon-execution.md STEP 5
- [ ] Add "3CANDLE_GATE: ACTIVE" line to TRADING-STRATEGY.md
- [ ] Note: accept missing first-move momentum in exchange for fewer fakeouts
