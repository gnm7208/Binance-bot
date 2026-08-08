# HMM Market Regime Detection

**Status: INACTIVE**
**Source: YouTube research — quantitative trading channel**
**Impact: 6 | Bot fit: 4 | Effort: 9**
**Activation alert: enable after conservative mode ends (post Aug 22) if macro gate accuracy < 60%**

## Concept

Hidden Markov Model trained on BTC price/volume to classify market into regimes:
- Regime 0: Low volatility accumulation → favor mean-reversion entries
- Regime 1: Trending breakout → favor momentum entries (current strategy)
- Regime 2: High volatility distribution → reduce size, tighten stops

## Why INACTIVE

- Very high implementation effort: requires scikit-learn or hmmlearn, training data pipeline,
  model persistence between cloud runs
- Cloud routines are stateless — model weights would need to be committed to repo each run
- Current macro gate (composite score) already approximates regime detection with much less complexity
- Marginal improvement over existing system doesn't justify engineering cost now
- Good candidate for post-Aug 22 review if macro gate is consistently miscalibrated

## Implementation Notes (if activated)

Would need:
1. Historical BTC 4h klines pipeline (fetch + store in memory/)
2. HMM training script (run weekly, commit model weights)
3. Morning-research STEP 3 extension: load weights, classify today's regime
4. SIZE_MULTIPLIER adjustments per regime (e.g. Regime 2 → cap at 0.7x)
