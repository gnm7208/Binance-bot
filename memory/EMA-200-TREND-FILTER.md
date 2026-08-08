# EMA-200 Trend Filter

**Status: ACTIVE**
**Source: YouTube research — Nate Herk / swing trading channels**
**Impact: 8 | Bot fit: 8 | Effort: 4**
**Implemented: 2026-08-08**

## What It Does

Hard gate in the Buy-Side Gate checklist and execution routines (steps 4e).
Before entering any position, computes the 200-day EMA from daily klines and compares to live price.

- Price **above** EMA-200 → trend is bullish → proceed with normal scoring
- Price **below** EMA-200 → downtrend pump → SKIP

## Override

OPTION_B catalyst (ETF filing, protocol upgrade, exchange listing) with signal score >= 10
may override with explicit Layer 3 justification logged in TRADE-LOG.

## Implementation

Execution routines: step 4e in `routines/morning-execution.md` and `routines/afternoon-execution.md`
Buy-Side Gate checklist: `memory/TRADING-STRATEGY.md` — EMA-200 entry in Buy-Side Gate section

```python
klines = fetch(f'https://api.mexc.com/api/v3/klines?symbol={TICKER}&interval=1d&limit=210')
closes = [float(k[4]) for k in klines]
k_factor = 2 / (200 + 1)
ema = closes[0]
for c in closes[1:]: ema = c * k_factor + ema * (1 - k_factor)
above_ema = closes[-1] > ema
```
