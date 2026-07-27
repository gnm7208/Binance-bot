# Trading Strategy

## Mission
Outperform BTC buy-and-hold over the challenge window using active swing trades on
MEXC Spot. Spot only — no margin, no futures, no leverage, ever.

## Capital & Constraints
- Starting capital: variable (see TRADE-LOG for current equity)
- Platform: MEXC Spot
- Instruments: Spot crypto only (USDT pairs preferred)
- Market hours: 24/7 — but focus research during US morning (6-10 AM CT)

## Core Rules
1. SPOT ONLY — no margin, no futures, no leverage, ever
2. 75-85% deployed; hold 15-25% USDT as dry powder
3. 5-6 positions max; 20% of total portfolio per position
4. Every position gets a stop-limit GTC order immediately after fill — no exceptions
5. Cut losers at -7% from entry: cancel stop order, market sell
6. Take profit at +7%: cancel stop order, market sell — no exceptions
7. Trailing stop (manual — MEXC has no native trailing stop):
   - Entry: stop at -10% below fill price
   - At +3% gain: tighten stop to 7% below current price (locks in near-breakeven)
   - At +7% gain: close for take profit
   - Never tighten within 3% of current price; never move a stop down
8. Max 25 new trades per week; max 5 new trades per day
9. Weekly circuit breaker: if ≥ 40% of this week's closed trades are losses (min 5 trades) → halt new entries; resume when F&G > 50 AND BTC 24h > 0%
10. Daily gate: if ≥ 5 trades placed today AND today's win rate < 60% → halt new entries until tomorrow
11. Momentum filter: only enter if 24h price change ≥ +2% OR a strong confirmed catalyst justifies entry against trend
12. Follow sector momentum (L1s, DeFi, AI/data layer, gaming/NFT, BTC dominance)
13. Exit a sector after 2 consecutive failed trades

## Entry Checklist (document ALL before placing order)
- Specific catalyst today?
- Sector in momentum?
- Stop level (7-10% below entry)?
- Target (minimum 2:1 R:R)?

## Buy-Side Gate (every check must pass)
- Weekly circuit breaker NOT active (< 40% loss rate on min 5 closed trades this week)
- Daily gate NOT active (if ≥ 5 trades today, today's win rate ≥ 60%)
- Total positions after fill ≤ 6
- Trades placed today + 1 ≤ 5
- Trades placed this week + 1 ≤ 25
- Position cost ≤ 20% of total portfolio USDT value
- Position cost ≤ available USDT balance
- Entry signal: EITHER a strong catalyst documented in today's RESEARCH-LOG (news event,
  protocol upgrade, whale accumulation, sector rotation) OR 24h price change ≥ +2% with
  no catalyst needed. Catalyst alone is sufficient — do not require both.
- Instrument is spot crypto (USDT pair on MEXC)

## Order Shapes
```bash
# Market buy (spend USDT amount)
bash scripts/mexc.sh order \
  '{"symbol":"BTCUSDT","side":"BUY","type":"MARKET","quoteOrderQty":"2000"}'

# Stop-limit GTC (10% below fill price — place immediately after fill)
bash scripts/mexc.sh order \
  '{"symbol":"BTCUSDT","side":"SELL","type":"STOP_LOSS_LIMIT","quantity":"0.001","price":"89900","stopPrice":"90000","timeInForce":"GTC"}'

# Take-profit at +10% (cancel stop first, then market sell)
bash scripts/mexc.sh cancel BTCUSDT <stop_order_id>
bash scripts/mexc.sh close BTCUSDT

# Tightened stop-limit (cancel old stop first, then place new at 7% or 5% below current price)
bash scripts/mexc.sh cancel BTCUSDT <old_order_id>
bash scripts/mexc.sh order \
  '{"symbol":"BTCUSDT","side":"SELL","type":"STOP_LOSS_LIMIT","quantity":"0.001","price":"94905","stopPrice":"95000","timeInForce":"GTC"}'
```

## Sell-Side Rules (evaluated at midday scan)
- Unrealized loss ≤ -7%: close immediately (cancel stop, market sell)
- Up +7% or more: close immediately — take profit (cancel stop, market sell)
- Up +3% to +6%: tighten stop to 7% below current price (trailing stop adjustment)
- Thesis broken (catalyst invalidated, sector rolling over): close even if not at -7%
- Sector has 2 consecutive failed trades: exit all positions in that sector

## Research Priorities (morning-research workflow)
- BTC price and dominance
- Crypto market sentiment (Fear & Greed Index)
- Top performing sectors this week
- Macro: DXY, Fed policy, rate expectations, risk-on/risk-off
- On-chain: exchange inflows/outflows, funding rates, open interest
- News on held tokens
- 2-3 actionable trade ideas with full entry/stop/target

## Notes from Experience
(Updated weekly; see WEEKLY-REVIEW.md for context)
- Week 1 (ending 2026-07-19): 0 trades. Grade F. Root cause is OPERATIONAL, not strategic —
  exchange API geo-blocked from this environment. Binance = HTTP 451; migrated to Bybit,
  which returns HTTP 403 (CloudFront geo-block) on both auth and public endpoints. Bot has
  never traded. No trading rule is at fault; connectivity must be fixed before strategy matters.
- **Reachability gate:** every run must first confirm the exchange API responds
  (`bash scripts/mexc.sh price BTCUSDT`). If it fails, HALT, alert, and place no orders —
  do not migrate exchanges again without verifying the new venue is reachable from this IP.
- **Stop-order gate (2026-07-25):** MEXC spot REST API does NOT support stop orders —
  `exchangeInfo.orderTypes` is `[LIMIT, MARKET, LIMIT_MAKER]` for every pair incl. BTCUSDT;
  `STOP_LOSS_LIMIT` orders will be rejected. Rule 4 (mandatory stop-limit after every fill)
  is therefore unexecutable on MEXC via API. Do NOT buy — a position with no resting stop
  violates Rule 4. Blocker until either a working spot-stop mechanism is found on MEXC or we
  move to a venue whose API supports resting stop-limit GTC orders AND is reachable from this IP.
  Verify order-type support (`exchangeInfo.orderTypes`) as part of every reachability check.
