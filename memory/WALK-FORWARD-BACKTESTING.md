# Walk-Forward Backtesting

**Status:** INACTIVE | **Impact:** 5 | **Bot Fit:** 3 | **Effort:** 10

## What It Does

Splits historical price data into rolling in-sample / out-of-sample windows.
Optimizes strategy parameters (stop %, TP target, signal score threshold) on the
in-sample period, then validates on unseen out-of-sample data. Repeats the roll
forward to avoid curve-fitting.

## Why Inactive

Effort: 10 — requires a full backtesting harness with historical MEXC OHLCV data,
parameter optimization loop, and evaluation metrics. The current strategy was
designed from first principles and is still in live calibration (< 10 closed trades).
Backtesting is most valuable after >= 30 live trades to validate against real slippage
and spread data specific to MEXC's liquidity profile.

## Activation Alert

Activate when: >= 30 closed trades in TRADE-LOG. Use live fills as ground truth
to calibrate backtest assumptions (fill price vs mid, slippage). Review parameter
assumptions per TRADING-STRATEGY.md "Phase Parameter Validation" section.

## Source

YouTube video research (quantitative finance / backtesting content), Aug 2026.
