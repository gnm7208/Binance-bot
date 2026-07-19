# Trading Strategy

## Mission
Outperform BTC buy-and-hold over the challenge window using disciplined swing trades on
Bybit Spot. Spot only — no margin, no futures, no leverage, ever.

## Capital & Constraints
- Starting capital: ~$10,000 USDT
- Platform: Bybit Spot
- Instruments: Spot crypto only (USDT pairs preferred)
- Market hours: 24/7 — but focus research during US morning (6-10 AM CT)

## Core Rules
1. SPOT ONLY — no margin, no futures, no leverage, ever
2. 75-85% deployed; hold 15-25% USDT as dry powder
3. 5-6 positions max; 20% of total portfolio per position (~$2,000 on a $10k account)
4. Every position gets a stop-limit GTC order immediately after fill — no exceptions
5. Cut losers at -7% from entry: cancel stop order, market sell
6. Tighten stop-limit: 7% below current price at +15%, 5% at +20%
7. Never tighten within 3% of current price; never move a stop down
8. Max 3 new trades per week — patience > activity
9. Follow sector momentum (L1s, DeFi, AI/data layer, gaming/NFT, BTC dominance)
10. Exit a sector after 2 consecutive failed trades

## Entry Checklist (document ALL before placing order)
- Specific catalyst today?
- Sector in momentum?
- Stop level (7-10% below entry)?
- Target (minimum 2:1 R:R)?

## Buy-Side Gate (every check must pass)
- Total positions after fill ≤ 6
- Trades placed this week + 1 ≤ 3
- Position cost ≤ 20% of total portfolio USDT value
- Position cost ≤ available USDT balance
- Catalyst documented in today's RESEARCH-LOG entry
- Instrument is spot crypto (USDT pair on Bybit)

## Order Shapes
```bash
# Market buy (spend USDT amount)
bash scripts/bybit.sh order \
  '{"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qty":"2000","marketUnit":"quoteCoin"}'

# Stop-limit GTC (10% below fill price — place immediately after fill)
bash scripts/bybit.sh order \
  '{"category":"spot","symbol":"BTCUSDT","side":"Sell","orderType":"Limit","qty":"0.001","price":"89900","triggerPrice":"90000","triggerBy":"LastPrice","orderFilter":"StopOrder","timeInForce":"GTC"}'

# Tightened stop-limit (cancel old stop first, then place new at 7% or 5% below current price)
bash scripts/bybit.sh cancel BTCUSDT <old_order_id>
bash scripts/bybit.sh order \
  '{"category":"spot","symbol":"BTCUSDT","side":"Sell","orderType":"Limit","qty":"0.001","price":"94905","triggerPrice":"95000","triggerBy":"LastPrice","orderFilter":"StopOrder","timeInForce":"GTC"}'
```

## Sell-Side Rules (evaluated at midday scan)
- Unrealized loss ≤ -7%: close immediately
- Thesis broken (catalyst invalidated, sector rolling over): close even if not at -7%
- Up +20%: tighten stop to 5% below current price
- Up +15%: tighten stop to 7% below current price
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
  (`bash scripts/bybit.sh price BTCUSDT`). If it fails, HALT, alert, and place no orders —
  do not migrate exchanges again without verifying the new venue is reachable from this IP.
