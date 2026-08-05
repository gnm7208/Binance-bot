# Volatility-Adjusted Stops & Targets — Future Feature (NOT YET ACTIVE)

## Status
INACTIVE — documented for future activation. Do NOT apply this rule until explicitly
enabled in TRADING-STRATEGY.md. Requires ≥10 closed trades to calibrate first.

## The Rule (when active)
Instead of fixed -7% stop / +12% TP for all positions, compute per-coin stop and
target distances based on that coin's 14-day ATR (average true range):

```python
# At entry time, after fill price is known:
daily = fetch(f'https://api.mexc.com/api/v3/klines?symbol={TICKER}&interval=1d&limit=15')
ranges = [float(d[2])-float(d[3]) for d in daily[:-1]]
daily_atr = sum(ranges) / len(ranges)
atr_pct   = daily_atr / fill_price * 100  # ATR as % of price

# Stop and TP distance based on ATR
stop_pct   = max(6.0, min(10.0, atr_pct * 1.0))   # 1x ATR, clamped 6-10%
target_pct = max(10.0, min(16.0, atr_pct * 2.0))  # 2x ATR, clamped 10-16%

stop_price   = fill_price * (1 - stop_pct / 100)
target_price = fill_price * (1 + target_pct / 100)
ladder_level = fill_price * (1 - stop_pct * 0.7 / 100)  # 70% of stop dist
```

## Why it exists
From GPT-5.4 nano bot improvement analysis (Aug 2026): fixed -7%/+12% is too tight
for high-volatility coins (e.g., a coin with 15% daily ATR will stop out on noise)
and too loose for low-volatility coins (a coin with 2% daily ATR needs a 4% stop,
not 7%). Per-coin volatility sizing improves win rate without changing overall risk.

From the Quick Flip Scalper strategy (Carl, Aug 2026): ATR is already the correct
benchmark for distinguishing "normal" candles from "manipulation" candles.
Extending ATR to set the stop/TP bracket is a natural next step.

## Parameter boundaries (aggressive phase)
- Stop: min 6%, max 10% (never less than 6% to avoid noise stops)
- TP: min 10%, max 16% (never less than 10% to preserve R:R ratio)
- Ladder: 70% of stop distance (e.g., stop at 8% → ladder at 5.6%)
- Risk:Reward must be >= 2.0 after ATR adjustment; if not, skip the entry

## Trade-offs
- **Pro**: High-vol coins (DOGE, SHIB) get wider stops — fewer premature stop-outs
- **Pro**: Low-vol coins (BTC, stable L1s) get tighter stops — less capital at risk
- **Pro**: ATR already computed during signal scoring (no extra API call needed)
- **Con**: Complicates TRADE-LOG entries (stop% varies per position)
- **Con**: Monitoring routines need to read the per-position stop% from TRADE-LOG
- **Con**: Needs calibration data — unknown whether 1x/2x ATR multipliers suit our portfolio

## When to activate
Consider activating if:
- >= 10 closed trades with fixed -7%/+12% in hand for comparison
- Analysis shows >= 3 stop-outs that would NOT have been hit with ATR-based stops
- Phase P&L is negative and stops are the root cause (not bad signal selection)
- Post-Aug-22 phase with more calibration data available

## TRADE-LOG format change (when active)
Entry format adds ATR fields:
```
**BUY** SYMBOL | Qty: X | Entry: $X.XX | Stop: $X.XX (-X.X% / 1.0x ATR) | Target: $X.XX (+X.X% / 2.0x ATR)
**ATR:** $X.XXXXX (X.X% of price)
```

## Activation checklist (manual — requires user approval)
- [ ] >= 10 closed trades to compare against
- [ ] User explicitly approves activation
- [ ] Update stop/TP calculation in morning-execution.md STEP 8
- [ ] Update stop/TP calculation in afternoon-execution.md STEP 8
- [ ] Update monitoring routines to read stop% per position (not assume -7%)
- [ ] Add "VOLATILITY_ADJUSTED_STOPS: ACTIVE" to TRADING-STRATEGY.md
