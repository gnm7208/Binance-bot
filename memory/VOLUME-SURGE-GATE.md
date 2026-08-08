# Volume Surge Gate

**Status: ACTIVE**
**Source: YouTube research — swing trading channel analysis**
**Impact: 7 | Bot fit: 8 | Effort: 4**
**Implemented: 2026-08-08**

## What It Does

Signal scoring bonus (+1 pt) in Layer 2. Computes today's USDT volume against the
20-day average. Confirms that today's move has genuine volume backing rather than
thin-market noise.

- Today vol >= 1.5x 20-day avg → +1 signal pt (surge_pts)
- Below threshold → +0

## Implementation

Execution routines: step 4f in `routines/morning-execution.md` and `routines/afternoon-execution.md`
Signal table: `memory/TRADING-STRATEGY.md` — "Volume surge" row (+1)

Uses klines index [7] = quote USDT volume (not base volume at index [5]).

```python
klines = fetch(f'https://api.mexc.com/api/v3/klines?symbol={TICKER}&interval=1d&limit=21')
avg_vol = sum(float(k[7]) for k in klines[:-1]) / 20
today_vol = float(klines[-1][7])
surge_pts = 1 if today_vol >= avg_vol * 1.5 else 0
```
