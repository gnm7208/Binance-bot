# Research Log

Daily morning research entries appended below.

---

<!-- Format for each entry:

## YYYY-MM-DD — Morning Research

### Account Snapshot
- Total portfolio value: $X,XXX USDT
- Free USDT: $X,XXX (X%)
- Open positions: N
- Trades this week: N/3

### Market Context
- BTC: $X,XXX (X% 24h)
- ETH: $X,XXX (X% 24h)
- BTC Dominance: X%
- Fear & Greed Index: XX (label)
- DXY: X.XX
- Crypto sector leaders today: ...
- Macro notes: ...

### On-Chain / Derivatives
- Exchange inflows/outflows: ...
- Funding rates (BTC/ETH): ...
- Open interest trend: ...

### News on Held Positions
- TICKER: ...

### Trade Ideas
1. TICKER — catalyst: ..., entry $X, stop $X (X%), target $X (X:1), sector: ...
2. TICKER — ...
3. TICKER — ...

### Risk Factors
- ...

### Decision
TRADE: [list tickers] or HOLD (default — no strong edge today)
-->

## 2026-07-23 — Morning Research

### Account Snapshot
- Total portfolio value: $32.32 USDT
- Free USDT: $32.32 (100%)
- Open positions: 0
- Trades this week: 0/25
- MEXC API: **live and healthy** (account, price, quote all responding). Prior Binance 451 block resolved by MEXC migration.

### Market Context
- BTC: $65,714 (-0.00% 24h; intraday range $65,365–$66,384)
- ETH: $1,929 (+0.40% 24h)
- SOL: $77.60 (+0.36% 24h, but ~+16% on the week)
- BNB: $570 (+0.08% 24h)
- BTC Dominance: ~56–58% (sources vary); Altcoin Season Index ~57 (threshold for altseason is 75 — not there yet)
- Fear & Greed: readings scattered again — 51/46 (Neutral) on some trackers, 33/23 (Fear/Extreme Fear) on others. Treat as **Neutral, fragile**.
- Sector leaders: selective rotation, not broad altseason — SOL (L1) + Hyperliquid (DeFi) leading; capital rotating into a narrow set of names rather than a full alt rally.
- Macro: DXY / current Fed print not confirmed via WebSearch this run (Perplexity key unset). June context: spot-ETF outflows were the largest since launch; BTC fell >20% in June. Risk tone cautious.

### On-Chain / Derivatives
- SOL on-chain activity climbing toward yearly highs as price attempts to base — constructive.
- Bitwise SOL ETF: +$2.64M net inflow Jul 21, cumulative ~$1.14B — institutional interest holding.
- Funding / OI: no real-time print (Perplexity unavailable; would need CoinGlass direct).

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
1. **No qualifying entry today.** Momentum filter (24h ≥ +2%) FAILS on every major — BTC/ETH/SOL/BNB all within ±0.4% on 24h. Choppy, directionless tape.
2. **Watchlist — SOL:** best-looking setup if it wakes up. +16% weekly bounce, ETF inflows, on-chain highs, Alpenglow consensus upgrade a potential Q3 catalyst. Trigger: 24h ≥ +2% AND clean break/hold above $80. Entry ~$80.50, stop ~$74.85 (-7%), target ~$86.15 (+7%), R:R ~1:1 on the rule set — sector L1.
3. **Watchlist — HYPE (Hyperliquid):** DeFi revenue leader in rotation; only if listed/liquid on MEXC Spot and it prints ≥ +2% 24h with a fresh catalyst.

### Risk Factors
- Momentum filter fails market-wide — forcing an entry here would violate rule 11.
- F&G Neutral-but-fragile; June ETF-outflow / -20% BTC backdrop still fresh — risk-off can resume fast.
- Perplexity API key unset — degraded macro/derivatives visibility; running on WebSearch + MEXC only.
- Tiny capital ($32.32): 20% cap ≈ $6.46/position — check MEXC min-notional before any live order.

### Decision
TRADE: none. **HOLD** — no setup passes the momentum gate today (all majors flat on 24h, no strong same-day catalyst). Market is Neutral/choppy. SOL and HYPE on watch for a ≥ +2% breakout with volume. Re-evaluate at morning-execution / midday.

## 2026-07-11 — Morning Research

### Account Snapshot
- **BLOCKED**: Binance API returned HTTP 451 "Service unavailable from a restricted location" on `account`, `positions`, `orders` — all wrapper calls to api.binance.com failed. Confirmed via direct curl to `/api/v3/ping` and `/api/v3/time`, same 451 with geo-restriction message.
- Last known state (Day 0 baseline, TRADE-LOG.md): $10,000.00 USDT, 100% cash, 0 open positions.
- ClickUp alert sent naming the outage.
- Trades this week: 0/3 (per TRADE-LOG, no entries yet).

### Market Context
- BTC: ~$63,800–$64,000 (+1.2% 24h, ~+4% week), total crypto market cap ~$1.28T (WebSearch fallback, sources vary slightly)
- BTC Dominance: ~54–56% (range across sources, one-month low per some reports as capital rotates to alts)
- Fear & Greed Index: readings inconsistent across providers this cycle — 23-26 (Extreme Fear/Fear) on some trackers, 45 (Neutral) on another dated Jul 8. Treat as Fear-leaning, not confirmed.
- DXY: ~100.9, up ~3% YTD / ~5% since late Jan; 13-month high 101.8 in late June
- Macro: FOMC held rates at 3.50-3.75% (Jun 16-17 meeting); markets price ~79.5% odds of no change at Jul 28-29 meeting under new Fed Chair Kevin Warsh, hawkish lean, inflation above target
- Sector leaders: Solana (L1) strength, RWA ecosystem ATH $3.41B; DeFi resilience (Hyperliquid, Aave revenue-generating, HYPE +160% YTD); AI tokens (Bittensor/TAO) narrative intact; gaming/Tap-to-Earn drawing presale flow
- Catalysts: Senate returns Jul 13 on CLARITY Act (SEC/CFTC market-structure bill); SEC rule proposal expected this month easing crypto startup conditions; Swift blockchain ledger pilot with HSBC/UBS/Wells Fargo/Citi; scheduled token unlocks today (IO, ALLO, IMX) — minor cap impact

### On-Chain / Derivatives
- Exchange inflows: net ~4,933 BTC into CEXs over 7 days to Jul 5; Binance largest single-exchange inflow (~2,007 BTC) — mild bearish/distribution signal
- Bitcoin ETF outflows: >$1.6B in June 2026
- Funding rates / OI: no real-time figure retrieved via WebSearch fallback (Perplexity unavailable); would need CoinGlass/Binance futures direct for current print

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
1. No new entries proposed today — account API is unreachable, so no execution is possible regardless of setup quality.
2. Watchlist for when API access is restored: SOL (L1 momentum, RWA growth), HYPE (DeFi revenue leader, but check liquidity/listing on Binance Spot), TAO (AI narrative) — need fresh catalyst + levels once live quotes available.

### Risk Factors
- **Binance API geo-blocked (451) from this execution environment — highest-priority operational risk.** No account visibility, no order placement/cancellation, no stop management possible until resolved.
- DXY strength / hawkish Fed under new chair — headwind for risk assets
- Fear & Greed near "Fear" territory — sentiment fragile, mixed signal on entries
- Net exchange BTC inflows — mild distribution/sell-pressure signal
- Token unlocks (IO, ALLO, IMX) today — localized volatility risk in those names only

### Decision
TRADE: none. HOLD — mandatory: Binance API unreachable (451), cannot verify account state or place/manage orders. Escalated via ClickUp. Re-run research/execution once connectivity is confirmed restored.
