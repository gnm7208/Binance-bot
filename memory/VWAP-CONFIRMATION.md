# VWAP Confirmation

**Status: ACTIVE**
**Source: YouTube research — swing trading channel analysis**
**Impact: 7 | Bot fit: 7 | Effort: 4**
**Implemented: 2026-08-08**

## What It Does

Signal scoring bonus (+1 pt) in Layer 2. Computes the session VWAP from today's 1h klines
(typical price × volume / total volume) and compares to live price.

- Live price > session VWAP → buyers in control → +1 pt
- Live price <= VWAP → selling pressure / mean-reversion risk → +0 pts

## Implementation

Execution routines: step 4g in `routines/morning-execution.md` and `routines/afternoon-execution.md`
Signal table: `memory/TRADING-STRATEGY.md` — "VWAP confirmation" row (+1)

Reuses the 24 hourly klines already fetched in prior steps where possible.

```python
klines = fetch(f'https://api.mexc.com/api/v3/klines?symbol={TICKER}&interval=1h&limit=24')
tp_vol = sum((float(k[2])+float(k[3])+float(k[4]))/3 * float(k[5]) for k in klines)
vol_sum = sum(float(k[5]) for k in klines)
vwap = tp_vol / vol_sum if vol_sum > 0 else 0
vwap_pts = 1 if float(klines[-1][4]) > vwap else 0
```

Note: this is a rolling 24h VWAP, not a pure calendar-day VWAP, since MEXC klines
don't distinguish session open. Close enough for signal scoring purposes.
