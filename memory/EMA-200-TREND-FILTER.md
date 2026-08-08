# EMA-200 Trend Filter

**Status:** ACTIVE | **Impact:** 8 | **Bot Fit:** 8 | **Effort:** 4

## What It Does

Before any buy, verify the coin's daily price is above its 200-day EMA.
If price < EMA-200 → SKIP (downtrend pump). Exception: OPTION_B catalyst with signal
score >= 10 may override with explicit Layer 3 justification.

## Implementation

Inserted in morning-execution.md and afternoon-execution.md as Step 4e (after 3-candle gate).
Fetches 210 daily klines, computes EMA with Wilder's exponential smoothing (k = 2/201),
compares live close to EMA. Also in TRADING-STRATEGY.md Buy-Side Gate.

```python
klines = fetch(f'https://api.mexc.com/api/v3/klines?symbol={TICKER}&interval=1d&limit=210')
closes = [float(k[4]) for k in klines]
k_factor = 2 / (200 + 1)
ema = closes[0]
for c in closes[1:]: ema = c * k_factor + ema * (1 - k_factor)
above_ema = closes[-1] > ema
```

## Why

Avoids buying dead-cat bounces in confirmed downtrends. EMA-200 is the most widely
watched institutional trend line — price below it signals bears in control.

## Source

YouTube video research (Algo Trading / MEXC bot strategy content), Aug 2026.
