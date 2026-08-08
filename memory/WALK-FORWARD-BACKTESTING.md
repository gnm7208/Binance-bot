# Walk-Forward Backtesting

**Status: INACTIVE**
**Source: YouTube research — quantitative trading channels**
**Impact: 6 | Bot fit: 4 | Effort: 9**
**Activation alert: enable post-Aug 22 during conservative mode for strategy tuning**

## Concept

Test strategy rule changes on historical data using walk-forward validation:
1. Train on 60-day window
2. Test on subsequent 15-day out-of-sample window
3. Roll forward 15 days and repeat
4. Compare parameter sets (e.g. stop at -7% vs -8%, TP at +10% vs +12%) across windows

## Why INACTIVE

- Very high effort: requires historical OHLCV data pipeline, backtesting engine,
  parameter grid search, results analysis
- MEXC API provides klines but not historical order fills at the precision needed
- Current live trade history (3 trades as of Aug 8) is too small to validate on
- Risk of overfitting: with only ~20 trades/week, parameter tuning on small samples
  produces misleading results
- Better to accumulate 60+ live trades first, then backtest off the actual equity curve

## Implementation Notes (if activated)

Would need:
1. Historical klines downloader (store in data/ directory, gitignored for size)
2. Signal scoring simulator (replicate Python blocks from execution routines)
3. P&L calculator with realistic slippage model
4. Walk-forward harness: configurable train/test split and parameter grid
5. Results committed to memory/BACKTEST-RESULTS.md for weekly review context
Minimum viable version: ~200 lines Python, 2-3 days work.
