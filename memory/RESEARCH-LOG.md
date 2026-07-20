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

## 2026-07-20 — Morning Research

### Account Snapshot
- **BLOCKED**: Bybit API returned HTTP 403 on both private (`account`) and public (`price`) calls. Direct curl to `https://api.bybit.com/v5/market/time` returns CloudFront geo-block: *"The Amazon CloudFront distribution is configured to block access from your country."* The Binance→Bybit migration (commits b3138f8, 8edc1c4) did NOT resolve the geo-restriction — same execution environment, same block, different exchange.
- Last known state (Day 0 baseline, TRADE-LOG.md): $10,000.00 USDT, 100% cash, 0 open positions. No live risk exposed.
- Trades this week: 0/3 (no entries yet).
- Perplexity API key present in env but wrapper reports "not set" and falls back to WebSearch — research below via WebSearch only.

### Market Context
- BTC: ~$64,712 (+0.39% 24h) — rangebound low-$60Ks for 2+ weeks
- ETH: ~$1,871 (+0.32%) — weak vs BTC
- SOL: ~$76.31 (+0.31%)
- BTC Dominance: ~57.2% (up from ~54-56% on Jul 11) — **rising dominance = alt headwind**, capital rotating back to BTC
- Total crypto mkt cap: ~$2.22T
- Fear & Greed: ~50 (Neutral) as of Jul 19; dipped to 22 (Extreme Fear) Jul 14. Choppy, no conviction
- DXY: ~100.76, on a weekly decline; softer US inflation scaled back near-term rate-hike bets — mild risk-on tailwind
- Macro: FOMC Jul 28-29. Market ~77% hold, but hike odds elevated (~23-46% across trackers) — hawkish tail risk into month-end. Rate 3.50-3.75%.

### On-Chain / Derivatives
- Not retrievable — Bybit blocked, Perplexity unavailable, no CoinGlass access this run.

### News on Held Positions
- None — 0 open positions.

### Sector Momentum
- L1: SUI active despite unlocks; SOL flat
- RWA: ONDO — institutional tokenized-treasury interest intact
- AI infra: RNDR/RENDER on watch as AI-GPU demand narrative continues
- DeFi: HYPE (Hyperliquid) still sector leader, >$1B cumulative fees + buybacks
- LINK strength noted

### Trade Ideas
1. No executable entries — Bybit API geo-blocked, cannot place or manage orders regardless of setup quality.
2. Watchlist (pending API access + confirm Bybit Spot listing/liquidity): HYPE (DeFi leader), SUI (L1), ONDO (RWA), RENDER (AI). All need fresh catalyst + live levels once execution is possible.

### Risk Factors
- **Bybit API geo-blocked (403 CloudFront) from this environment — top operational risk. Bot cannot trade. Migration did not fix it.** A US-blocked exchange (Binance/Bybit) is the wrong venue for this environment; needs a geo-permitted exchange or a proxy/allowlist fix.
- Rising BTC dominance (~57%) — headwind for alts, favors sitting in BTC/cash
- Hawkish Fed tail risk into Jul 28-29 FOMC
- Neutral/choppy sentiment, no directional edge

### Decision
TRADE: none. HOLD — mandatory: Bybit API unreachable (403 geo-block), cannot verify account or place/manage orders. Also no directional edge (rising BTC dominance, neutral sentiment, Fed risk). Even with access restored, no compelling setup today. Operational blocker escalated.
