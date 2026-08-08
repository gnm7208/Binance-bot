# Pullback Entry Mode

**Status:** INACTIVE | **Impact:** 6 | **Bot Fit:** 5 | **Effort:** 6

## What It Does

Instead of chasing momentum breakouts, waits for a pullback to a key support level
(EMA-20, VWAP, or prior day's high) after the initial move. Enters on the first
confirmed bullish candle off support.

## Why Inactive

Bot_fit: 5 — our cloud routines run on a schedule (not tick-by-tick), so detecting
the exact pullback reversal candle requires more scan frequency than current
2-4 scans/day architecture allows. Risk of entering mid-pullback before reversal
confirmation is confirmed.

## Activation Alert

Activate when: scan frequency increases to hourly or continuous monitoring is added.
Prerequisite: continuous monitoring routine (not yet built).

## Source

YouTube video research (swing trading / entry timing content), Aug 2026.
