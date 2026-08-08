# HMM Market Regime Detection

**Status:** INACTIVE | **Impact:** 5 | **Bot Fit:** 4 | **Effort:** 9

## What It Does

Hidden Markov Model trained on BTC price/volume data to classify the current market
into regimes: bull trend, bear trend, sideways chop. Routes strategy parameters
(position size, stop width, TP target) differently per regime.

## Why Inactive

Effort: 9 — requires training data pipeline, model fitting (hmmlearn or custom),
and regime inference at runtime. Not compatible with the stateless cloud routine
architecture (no persistent model state between runs). Would need a hosted model
endpoint or pre-computed regime labels committed to git.

## Activation Alert

Activate when: a persistent model serving layer is added, or regime labels can be
pre-computed and committed as a daily file.

## Source

YouTube video research (quantitative / ML trading content), Aug 2026.
