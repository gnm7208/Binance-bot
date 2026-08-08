# RSI Signal Gate

**Status:** ACTIVE | **Impact:** 7 | **Bot Fit:** 7 | **Effort:** 4

## What It Does

Adds +1 if 1h RSI(14) is in the 30-60 zone (recovering momentum, not overbought).
Adds -1 if 1h RSI(14) > 70 (overbought — chasing an extended move).
RSI computed via Wilder's smoothing on 30 x 1h klines.

## Implementation

Inserted in morning-execution.md and afternoon-execution.md as Step 4h.
Also added as two signal rows in TRADING-STRATEGY.md Layer 2 signal table.

```python
klines = fetch(f'https://api.mexc.com/api/v3/klines?symbol={TICKER}&interval=1h&limit=30')
closes = [float(k[4]) for k in klines]
gains, losses = [], []
for i in range(1, len(closes)):
    d = closes[i] - closes[i-1]
    gains.append(max(d,0)); losses.append(max(-d,0))
ag = sum(gains[:14])/14; al = sum(losses[:14])/14
for i in range(14, len(gains)):
    ag = (ag*13+gains[i])/14; al = (al*13+losses[i])/14
rsi = 100 - (100/(1+ag/al)) if al > 0 else 100
rsi_pts = 1 if 30 <= rsi <= 60 else (-1 if rsi > 70 else 0)
```

## Why

RSI in 30-60 = momentum building from oversold, highest risk-reward zone.
RSI > 70 = already extended; entries here statistically underperform (chasing the move).

## Source

YouTube video research (technical analysis / momentum trading content), Aug 2026.
