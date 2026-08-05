# Trading Strategy - AGGRESSIVE MODE (Aug 4-22)
# Conservative version saved in TRADING-STRATEGY-CONSERVATIVE.md
# Revert after Aug 22.

## Mission
Maximize returns before Aug 22 on MEXC Spot. Accept higher risk for higher reward.
Spot only - no margin, no futures, no leverage, ever.

## Capital & Constraints
- Platform: MEXC Spot | Instruments: Spot USDT pairs
- Target deployment: 80-90% (hold 10-20% USDT dry powder only)
- Max 3 simultaneous positions at 30-35% each

## 3-Layer Architecture

### Layer 1 — Macro Gate (morning-research STEP 3)

Compute MACRO_SCORE (0-100) from these weighted signals:

| Signal | Scoring Formula | Weight |
|---|---|---|
| Fear & Greed (F&G) | raw value 0-100 | 30% |
| BTC 24h momentum | clamp((btc_24h_pct + 5) * 10, 0, 100) | 25% |
| BTC dominance | clamp((65 - btc_dom_pct) * 6.67, 0, 100) | 20% |
| Alt breadth | >70% green=80-100; mixed=40-70; <40% green=0-40 | 15% |
| Recent loss rate | clamp(100 - loss_pct * 2.5, 0, 100); default 75 if <5 trades | 10% |

MACRO_SCORE = sum of each signal score * its weight

SIZE_MULTIPLIER from MACRO_SCORE:
- >= 70: SIZE_MULTIPLIER = 1.0 (full aggressive sizing)
- 40-69: SIZE_MULTIPLIER = 0.6 (reduced sizing)
- < 40:  SIZE_MULTIPLIER = 0.0 (NO new entries — monitor only)

### Layer 2 — Weighted Signal Scoring (morning-research STEPS 4-6)

Every candidate coin gets a score 0-16 built from these signals:

| Signal | Points |
|---|---|
| Whale Alert exchange->wallet flow (accumulation) — <24h: +3 \| 24-48h: +2 \| >48h: 0 | +3 |
| VC/fund accumulation (a16z, Paradigm, Multicoin) — <48h: +3 \| >48h: +2 | +3 |
| Top trader call (Kaleo, pentoshi, Bluntz named ticker) — <48h: +2 \| >48h: +1 | +2 |
| DeFiLlama TVL gaining >10% 24h (underlying token) | +2 |
| CoinGecko trending top 5 | +1 |
| 24h price >= +5% on MEXC | +2 |
| MEXC volume >= $3M USD | +1 |
| Price within 5% of prev-day low (near support) | +1 |
| Price within 2% of prev-day high (near resistance) | -2 |
| ATR manipulation flush: largest 15m candle in last 2h >= 25% of 14-day ATR AND bearish | +1 |

Entry eligibility:
- SCORE >= 5: ELIGIBLE (proceed to Layer 3 review)
- SCORE < 5: watchlist only — do NOT enter
- If near prev-day high (-2 pts applied) AND SCORE < 7: SKIP — low conviction into resistance
- OPTION_B override: strong catalyst (ETF filing, protocol upgrade, exchange listing) = eligible regardless of score

Position sizing by signal score (before macro multiplier):
- Score 5-7:  BASE_SIZE = 25% of portfolio
- Score 8-10: BASE_SIZE = 30%
- Score >= 11: BASE_SIZE = 35%

FINAL_SIZE_USDT = portfolio_value * BASE_SIZE * SIZE_MULTIPLIER
Minimum position: $3 USDT (MEXC min-notional). Below minimum: skip.

### Layer 3 — Structured Review Gate (execution routines STEP 6)

Run before EVERY order fires. Answer all 5 questions:

1. Bear case: "What is the strongest argument AGAINST entering right now?"
2. Blind spots: "What am I most likely missing or underweighting?"
3. Exit liquidity: "Is exit realistic at target price? MEXC volume >= $1M?"
4. Sector momentum: "Is this sector net positive or fading?"
5. Correlation: "Does this conflict with an existing open position?"

REVIEW OUTCOME rules:
- Bear case overwhelming OR blind spot is confirmed blocker OR exit liquidity fails: SKIP
- 2+ questions raise soft concerns: size down one tier (35%->30%, 30%->25%, 25%->skip)
- Otherwise: proceed at planned size

Log outcome in TRADE-LOG: "Review: [Proceed/Skip/Size down] - reason"

## Core Rules
1. SPOT ONLY - no margin, no futures, no leverage, ever
2. 80-90% deployed; only 10-20% USDT dry powder
3. Max 3 open positions; 30-35% of portfolio per position
4. Every position: stop price recorded in TRADE-LOG immediately after fill
5. Cut losers at -7% from entry: market sell immediately
6. Take profit at +12%: market sell - no exceptions
7. Trailing stop (manual - enforced by monitoring routines):
   - Entry: stop at -10% below fill price (in TRADE-LOG)
   - At +4% gain: tighten stop to 7% below current price (update TRADE-LOG)
   - At +12%: close for take profit
   - Never tighten within 3% of current price; never move a stop down
8. LADDER BUY: if open position drops -6% to -9% AND thesis still intact:
   - Buy a second tranche (same USDT size as first)
   - New stop = avg cost * 0.90 | New target = avg cost * 1.12
   - Log in TRADE-LOG: "Ladder buy at $X, avg cost now $X"
   - Never ladder if thesis broken or sector rolling over
   - Max 1 ladder per position
9. Max 20 new trades per week; max 5 new trades per day
10. Weekly circuit breaker: if >= 40% of closed trades this week are losses
    (min 5 trades) -> halt; resume when F&G > 50 AND BTC 24h > 0%
11. Daily gate: if >= 5 trades today AND win rate < 60% -> halt until tomorrow

## Sector P&L Tracking
- Record sector in every TRADE-LOG entry: L1 / DeFi / AI / Gaming / Other
- At each research session (Step 1): scan TRADE-LOG for sector win/loss counts
- SECTOR_BLOCKED: any sector with 2+ CONSECUTIVE losses -> avoid until sector recovers
- Record sector status in RESEARCH-LOG Macro Gate section each morning

## Buy-Side Gate (every check must pass before any order)
- Macro gate NOT halted (SIZE_MULTIPLIER > 0)
- Weekly circuit breaker NOT active
- Daily gate NOT active
- Total positions after fill <= 3
- Trades today + 1 <= 5 | Trades this week + 1 <= 20
- FINAL_SIZE_USDT <= available USDT balance (keep >= 10% dry powder)
- Entry signal: score >= 5 OR OPTION_B catalyst
- Ticker NOT in SECTOR_BLOCKED sector
- Layer 3 review OUTCOME = Proceed (or Size down, not Skip)
- Instrument is spot crypto (USDT pair on MEXC)

## Smart Money Signal Sources (priority order)
1. Whale Alert - large on-chain transactions (exchange->wallet = accumulation)
2. VC wallet accumulation (a16z, Paradigm, Multicoin public wallets)
3. Top trader calls: CryptoKaleo, pentoshi, Bluntz_Capital, Crypto_Cobain
4. CoinGecko trending (retail momentum, top 5 = signal)
5. DeFiLlama TVL gainers (protocol-level smart money, >10% 24h)
Highest conviction = coin appears in 3+ of the above

## Order Shapes
```bash
# Market buy (spend USDT amount)
bash scripts/mexc.sh order \
  '{"symbol":"BTCUSDT","side":"BUY","type":"MARKET","quoteOrderQty":"<amount>"}'

# Close position (take-profit / cut loser)
bash scripts/mexc.sh close SYMBOLUSDT

# NOTE: MEXC spot API only supports LIMIT, MARKET, LIMIT_MAKER - NO stop-limit orders.
# Stops enforced manually by midday + afternoon monitoring routines.
# Record stop/target/ladder in TRADE-LOG at every entry.
```

## Sell-Side Rules (evaluated at EVERY midday and afternoon scan)
- Price <= stop price in TRADE-LOG OR P&L <= -7%: market sell immediately
- P&L >= +12%: market sell immediately - take profit, no exceptions
- P&L +4% to +11%: update stop in TRADE-LOG to 7% below current price
- Thesis broken (catalyst invalidated, sector rolling over): sell even if not at -7%
- SECTOR_BLOCKED: exit all positions in blocked sector
- Ladder buy check: if -6% to -9% AND thesis intact -> execute ladder buy

## Phase Parameter Validation (review before Aug 22 revert)
Compare actual results against these assumptions:
- Were +12% targets hit? Or did most positions reverse before reaching target?
- Was -7% cut too tight? (if consecutive ladders triggered) or too loose?
- Did ladder buys improve avg P&L vs single-entry trades?
- Did macro gate (SIZE_MULTIPLIER) correctly filter bad market days?
- Did signal score >= 5 threshold have better win rate than score < 5 entries?
- Was 30-35% position sizing appropriate for portfolio size ($30-50 range)?
Use this review to calibrate conservative strategy settings for post-Aug-22.

## Notes from Experience
- Week 1-2 (Jul 22 - Aug 2): 1 closed trade (ADA +7.0%), 1 open (ADA re-entry).
  Phase P&L +$0.53 (+1.65%) vs BTC flat. Conservative strategy worked but
  under-deployed (20% vs 80-90% target). Switched to aggressive mode Aug 4.
- Stop mechanism: MEXC has no resting stop-limit orders. Enforced by midday +
  afternoon monitoring routines. Record stop price in TRADE-LOG at every entry.
- Smart money note: ADA entry was pure momentum - no whale signal. Next entries
  should prioritize coins with smart money backing for higher conviction.
