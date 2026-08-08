# Volume Surge Gate

**Status:** ACTIVE | **Impact:** 7 | **Bot Fit:** 8 | **Effort:** 4

## What It Does

Adds +1 signal point when today's USDT quote volume >= 1.5x the 20-day average.
Computed live at execution time using daily klines from MEXC API.

## Implementation

Inserted in morning-execution.md and afternoon-execution.md as Step 4f.
Also added as a signal row (+1) in TRADING-STRATEGY.md Layer 2 signal table.

```python
klines = fetch(f'https://api.mexc.com/api/v3/klines?symbol={TICKER}&interval=1d&limit=21')
avg_vol = sum(float(k[7]) for k in klines[:-1]) / 20  # k[7] = USDT quote volume
today_vol = float(klines[-1][7])
surge_pts = 1 if today_vol >= avg_vol * 1.5 else 0
```

## Why

Volume surge confirms that price movement has institutional participation, not just thin
retail action. 1.5x average is a meaningful threshold — catches real breakouts without
triggering on every small daily fluctuation.

## Source

YouTube video research (technical analysis / momentum trading content), Aug 2026.
