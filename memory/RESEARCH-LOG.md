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

## 2026-07-21 — Morning Research

### Account Snapshot
- **BLOCKED (egress policy)**: `bash scripts/bybit.sh account/positions` → HTTP 403. Root cause confirmed: `api.bybit.com` is **denied by this environment's organization egress policy** (agent-proxy status: 403 on even the public `/v5/market/time` endpoint; API keys ARE set in env). Not a credential problem — the exchange host is not on the allow-list. Proxy README: "Do not retry or route around it — report the blocked host."
- Prior 2026-07-11 outage was Binance 451 (geo). Exchange connectivity has now been down ~10 days across the switch to Bybit. **No account visibility, no order placement/cancellation, no stop management possible.**
- Last known state (Day 0 baseline): $10,000.00 USDT, 100% cash, 0 open positions, 0/3 trades this week.

### Market Context
- BTC: ~$64,200 (Jul 20 print; range $64.2k–$64.7k). Roughly flat, range-bound low-$60s. Recovered from Jul 14 flush (Extreme Fear, F&G 22, mkt cap dipped to ~$2.23T).
- Total crypto mkt cap: ~$2.28T.
- BTC Dominance: ~56–58% (sources vary). **Bitcoin Season** — Altcoin Season Index 46–55, below the 50–60 breakout zone. Any alt strength = selective rotation, not confirmed altseason.
- Fear & Greed: ~44–50 (Neutral), recovered from 22 (Extreme Fear) on Jul 14.
- DXY: ~100.6–100.9, easing from early-July highs ~101.4 but structurally firm; hawkish Fed backdrop.
- Macro: June CPI (rel. Jul 14) eased to 3.5% YoY (below 3.8% consensus, down from 4.2%). BUT Fed Chair Warsh maintains inflation "too high." **FOMC Jul 28–29** — markets price ~25–46% odds of a 25bp HIKE (dot plot leans toward a rise, not a cut before year-end). Hawkish risk into month-end.

### On-Chain / Derivatives
- Spot BTC ETF: outflow streaks ended early July; modest inflows returning (~$510M over 3 sessions early July; +$197M week ending Jul 10). Context: June was worst-ever ETF month (-$4.5B), YTD flows turned negative for first time. Net signal: stabilizing but not yet risk-on.
- Funding rates: neutral (~0.0043%/day, ~1.56% annualized) — no leverage froth.
- Open interest: stable ~$48.9B (up only ~3.5–3.9% over 30d) — recovery not driven by speculative leverage (constructive, low-blowup-risk).

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
1. **No executable ideas** — exchange API egress-blocked, so no quote/fill/stop is possible regardless of setup quality.
2. Even if live: setup is a HOLD. Bitcoin Season (alts unconfirmed), neutral sentiment, and a hawkish FOMC Jul 28–29 with live hike odds = poor risk/reward for new alt entries this week.
3. Watchlist when access restored (need fresh catalyst + live levels): SOL (L1), TAO/FET (AI — but currently rolling over, wait for stabilization), and BTC itself on any hold of the low-$60s. Avoid chasing PUMP-style social-hype spikes (+20% on chatter, no fundamental catalyst).

### Risk Factors
- **Exchange API egress-blocked (403) — top operational risk.** Bot is non-functional for its core mission; requires environment network-policy change to allow `api.bybit.com`.
- Hawkish FOMC Jul 28–29 with ~25–46% hike odds — risk-asset headwind into month-end.
- DXY firm, Fed Chair calling inflation "too high" despite softer CPI.
- YTD ETF flows negative — institutional demand still net-fragile.

### Decision
TRADE: none. **HOLD** — mandatory: exchange API unreachable (egress-blocked 403), cannot verify account or place/manage orders. Secondary: even with access, unfavorable setup (Bitcoin Season + hawkish FOMC). Escalating connectivity block to owner. Re-run once `api.bybit.com` is allow-listed on the environment.
