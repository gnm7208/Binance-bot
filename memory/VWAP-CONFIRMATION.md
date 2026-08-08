# VWAP Confirmation

**Status:** ACTIVE | **Impact:** 7 | **Bot Fit:** 7 | **Effort:** 4

## What It Does

Adds +1 signal point when live price > session VWAP (volume-weighted average price).
VWAP computed from today's 24 x 1h klines using typical price × base volume.

## Implementation

Inserted in morning-execution.md and afternoon-execution.md as Step 4g.
Also added as a signal row (+1) in TRADING-STRATEGY.md Layer 2 signal table.

```python
klines = fetch(f'https://api.mexc.com/api/v3/klines?symbol={TICKER}&interval=1h&limit=24')
tp_vol = sum((float(k[2])+float(k[3])+float(k[4]))/3 * float(k[5]) for k in klines)
vol_sum = sum(float(k[5]) for k in klines)
vwap = tp_vol / vol_sum if vol_sum > 0 else 0
vwap_pts = 1 if float(klines[-1][4]) > vwap else 0
```

## Why

Price above VWAP = institutions net buyers on the day; market makers are long.
Price below VWAP = institutions net sellers; buying into institutional distribution is
a poor-risk setup. VWAP is the intraday institutional benchmark.

## Source

YouTube video research (institutional trading / order flow content), Aug 2026.
