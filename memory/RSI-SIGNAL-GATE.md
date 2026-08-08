# RSI Signal Gate

**Status: ACTIVE**
**Source: YouTube research — swing trading channel analysis**
**Impact: 7 | Bot fit: 7 | Effort: 4**
**Implemented: 2026-08-08**

## What It Does

Signal scoring adjustment in Layer 2 based on RSI-14 on the 1h chart.

- RSI 30–60 (oversold recovery / momentum building) → +1 pt
- RSI > 70 (overbought / chasing extended move) → -1 pt
- RSI 60–70 → 0 pts

Prevents chasing already-extended moves and rewards entries at momentum build phase.

## Implementation

Execution routines: step 4h in `routines/morning-execution.md` and `routines/afternoon-execution.md`
Signal table: `memory/TRADING-STRATEGY.md` — two RSI rows (+1 recovering, -1 overbought)

Uses Wilder's smoothing (not simple average) over 30 hourly klines, 14-period:

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
