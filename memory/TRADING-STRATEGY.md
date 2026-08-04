# Trading Strategy — AGGRESSIVE MODE (Aug 4–22)
# Conservative version saved in TRADING-STRATEGY-CONSERVATIVE.md
# Revert after Aug 22.

## Mission
Maximize returns before Aug 22 on MEXC Spot. Accept higher risk for higher reward.
Spot only — no margin, no futures, no leverage, ever.

## Capital & Constraints
- Platform: MEXC Spot | Instruments: Spot USDT pairs
- Target deployment: 80-90% (hold 10-20% USDT dry powder only)
- Max 3 simultaneous positions at 30-35% each

## Core Rules (Aggressive)
1. SPOT ONLY — no margin, no futures, no leverage, ever
2. 80-90% deployed; only 10-20% USDT dry powder
3. Max 3 open positions; 30-35% of portfolio per position
4. Every position gets stop price recorded in TRADE-LOG immediately after fill
5. Cut losers at -7% from entry: market sell immediately
6. Take profit at +12%: market sell — no exceptions
7. Trailing stop (manual — enforced by monitoring routines):
   - Entry: stop at -10% below fill price (recorded in TRADE-LOG)
   - At +4% gain: tighten stop to 7% below current price (update TRADE-LOG)
   - At +12% gain: close for take profit
   - Never tighten within 3% of current price; never move a stop down
8. LADDER BUY RULE (from video — buy dips with conviction):
   - If open position drops -6% to -9% from entry AND thesis still intact:
     → Buy a second tranche (same USDT size as first)
     → New average cost = (entry1 + entry2) / 2
     → New stop = average cost × 0.90
     → New target = average cost × 1.12
     → Log in TRADE-LOG: "Ladder buy at $X, avg cost now $X"
   - Never ladder if thesis is broken or sector is rolling over
   - Max 1 ladder per position
9. Max 20 new trades per week; max 5 new trades per day
10. Weekly circuit breaker: if ≥ 40% of this week's closed trades are losses
    (min 5 trades) → halt; resume when F&G > 50 AND BTC 24h > 0%
11. Daily gate: if ≥ 5 trades today AND win rate < 60% → halt until tomorrow
12. Entry signal (aggressive — either is sufficient):
    - OPTION A: 5%+ 24h momentum on volume ≥ $3M (higher bar than conservative)
    - OPTION B: Strong catalyst (ETF filing, protocol upgrade, whale accumulation,
      VC fund entry) documented in RESEARCH-LOG — ANY 24h move qualifies
    - OPTION C: Coin appears in 3+ signal sources (CoinGecko + DeFiLlama + whale alert
      + trader call) regardless of 24h move
13. Smart money priority: coins flagged by whale alert OR VC accumulation OR
    top trader calls get priority over pure momentum plays
14. Exit a sector after 2 consecutive failed trades

## Entry Checklist (document ALL before placing order)
- Signal source count (1-5)?
- Whale/smart money signal present?
- Catalyst documented?
- Sector in momentum?
- Stop level (-10% below entry)?
- Target (+12%)?
- Ladder buy level (-7% from entry)?

## Buy-Side Gate (every check must pass)
- Weekly circuit breaker NOT active
- Daily gate NOT active
- Total positions after fill ≤ 3
- Trades today + 1 ≤ 5 | Trades this week + 1 ≤ 20
- Position cost ≤ 35% of total portfolio USDT value
- Position cost ≤ available USDT balance (keep ≥ 10% dry powder)
- Entry signal: Option A OR B OR C above
- Instrument is spot crypto (USDT pair on MEXC)

## Smart Money Signal Sources (crypto equivalent of Capitol Trades)
Priority order:
1. Whale Alert — transactions > $1M on-chain
2. VC wallet accumulation (a16z, Paradigm, Multicoin public wallets)
3. Top trader calls: CryptoKaleo, pentoshi, Bluntz_Capital, Crypto_Cobain
4. CoinGecko trending (retail momentum)
5. DeFiLlama TVL gainers (protocol-level smart money)
Highest conviction = coin appears in 3+ of the above

## Order Shapes
```bash
# Market buy (spend USDT amount)
bash scripts/mexc.sh order \
  '{"symbol":"BTCUSDT","side":"BUY","type":"MARKET","quoteOrderQty":"<amount>"}'

# Take-profit / cut loser / ladder buy (market sell or buy full position)
bash scripts/mexc.sh close SYMBOL UST
bash scripts/mexc.sh order \
  '{"symbol":"XYZUSDT","side":"BUY","type":"MARKET","quoteOrderQty":"<amount>"}'

# NOTE: MEXC spot API only supports LIMIT, MARKET, LIMIT_MAKER.
# Stops enforced by monitoring routines. Record stop/target/ladder in TRADE-LOG.
```

## Sell-Side Rules (evaluated at EVERY midday and afternoon scan)

- Price ≤ stop price in TRADE-LOG OR P&L ≤ -7%: market sell immediately
- P&L ≥ +12%: market sell immediately — take profit, no exceptions
- P&L +4% to +11%: update stop in TRADE-LOG to 7% below current price
- Thesis broken (catalyst invalidated, sector rolling over): sell even if not at -7%
- Sector has 2 consecutive failed trades: exit all positions in that sector
- Ladder buy check: if -6% to -9% AND thesis intact → execute ladder buy

## Research Priorities
- Smart money signals FIRST (whale alert, VC moves, top trader calls)
- BTC price and dominance
- Crypto market sentiment (Fear & Greed Index)
- Top performing sectors this week
- Macro: DXY, Fed policy, rate expectations
- News on held tokens
- 3-5 actionable trade ideas with full entry/ladder/stop/target

## Notes from Experience
- Week 1-2 (Jul 22 - Aug 2): 1 closed trade (ADA +7.0%), 1 open (ADA re-entry).
  Phase P&L +$0.53 (+1.65%) vs BTC flat. Conservative strategy worked but
  under-deployed (20% vs 80-90% target). Switching to aggressive mode Aug 4.
- Stop mechanism: MEXC has no resting stop-limit orders. Enforced by midday +
  afternoon monitoring routines. Record stop price in TRADE-LOG at every entry.
- Reachability gate: run `bash scripts/mexc.sh price BTCUSDT` before any order.
- Smart money note: ADA entry was pure momentum — no whale signal. Next entries
  should prioritize coins with smart money backing for higher conviction.
