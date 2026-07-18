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

## 2026-07-18 — Morning Research

### Account Snapshot
- **BLOCKED (7th consecutive day)**: Binance API returns HTTP 451 "Service unavailable from a restricted location" on `account`, `positions`, `orders` — same geo-restriction as 2026-07-11, still unresolved one week later.
- Last known state: $10,000.00 USDT, 100% cash, 0 open positions (Day 0 baseline — never updated since; no trade has ever executed).
- PERPLEXITY_API_KEY not set in local env — fell back to native WebSearch for all research below.
- Trades this week: 0/3. Trades ever: 0.

### Market Context
- BTC: ~$64,050 (-1.4% 24h per CoinGecko; range $62,528–$64,286)
- BTC Dominance: 56.3%, total crypto market cap ~$2.28T
- Fear & Greed Index: 54 (Neutral) as of Jul 16 — recovering from Extreme Fear (22) printed Jul 14; sentiment whipsawing on geopolitical tension and weak volumes
- DXY: 100.91 (Jul 14), up ~2.8% YTD, easing off early-July highs near 101.39
- Macro: FOMC held 3.50-3.75% at Jun 16-17 meeting; NY Fed's Williams signals no hike needed at Jul 28-29 meeting, but 9/18 FOMC members pencil in a 2026 hike — hawkish lean persists under Chair Warsh
- Sector leaders: Memes +220% YTD, Prediction Markets +80% YTD, AI/GameFi narratives (TAO, Autonolas) drawing bullish flow. Laggards: L1s -28% YTD, DeFi -26% YTD — momentum has rotated away from majors into speculative/attention narratives
- Catalysts today: Cardano "Van Rossem" hard fork live (lower fees, Leios groundwork); GENIUS Act final stablecoin KYC rules due; CLARITY Act Senate floor vote expected this month

### On-Chain / Derivatives
- Bitcoin ETFs: 10-day, $2.73B outflow streak snapped early July; ~$1.2B net inflows week of Jul 10, reversing June's $4.5B outflow record — flows improving
- Funding rates: BTC funding slightly positive (~0.003%), neutral/mild long bias
- Open interest: BTC futures OI ~$48.9B (+3.5%); OI fell ~23k BTC in early July alongside rising price — reads as short squeeze, not fresh conviction

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
1. No new entries proposed — account API unreachable, execution impossible regardless of setup quality.
2. Watchlist only (unconfirmed against live account): meme/prediction-market names showing the strongest 2026 momentum, but these sit outside typical swing-trade risk profile — needs fresh look once quotes/account access restored. AI-narrative names (TAO) remain a secondary watch.
3. L1s and DeFi both down >25% YTD — avoid until sector shows reversal confirmation; two straight down sectors per strategy rule 10.

### Risk Factors
- **Binance API geo-blocked (451), now 7 days running — top operational risk.** Zero account visibility, cannot place/cancel/manage any order. This is no longer a one-off outage; it needs infrastructure-level attention (proxy/region fix), not a daily retry.
- No trade has executed since bot launch (Day 0) — the challenge window is burning with the account fully idle.
- Fear & Greed whipsawing (22 → 54 in 2 days) — unstable sentiment, poor entry conditions even if API were live
- Hawkish FOMC minority (9/18 penciling a hike) — headwind risk for risk assets into the Jul 28-29 meeting

### Decision
TRADE: none. HOLD — mandatory: Binance API still unreachable (451) for the 7th straight day, cannot verify account state or place/manage orders. Escalating via ClickUp given the duration. Re-run research/execution once connectivity is confirmed restored.
