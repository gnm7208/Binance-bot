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

## 2026-07-19 — Morning Research

### Account Snapshot
- **BLOCKED**: `BYBIT_API_KEY` and `BYBIT_SECRET_KEY` are **empty in the cloud routine environment** — `scripts/bybit.sh` aborts before any request. No account, positions, orders, or stop visibility. Cannot place/cancel/manage orders.
- `PERPLEXITY_API_KEY` also empty → research done via WebSearch fallback (no Perplexity).
- Last known state (Day 0 baseline, TRADE-LOG): $10,000.00 USDT, 100% cash, 0 open positions. **Still 0 trades placed on Day 8** — system has never been able to execute since launch (Binance 451 → migrated to Bybit → creds not configured).

### Market Context
- BTC: ~$64,376 (roughly flat 24h; mid-July range ~$63,900–$64,900)
- ETH: ~$1,840 (−0.75% 24h, laggard)
- BTC Dominance: ~56–60% (≈57% consensus)
- Total crypto market cap: ~$2.19T
- Fear & Greed: mixed across providers 22–54 — **Fear-leaning (~25–40)**, driven by geopolitics, thin volume, pending US inflation data
- DXY: ~100.6–100.9 (firm but easing from early-July ~101.4 highs)
- Macro: FOMC Jul 28–29 — ~65% priced for **hold** at 3.50–3.75%; weak June payrolls (57k) pushed any hike odds to September; risk-neutral backdrop
- Sector leaders: alts **stabilizing but no altseason** — BTC still commands flows; SOL = risk-on tell (watch for SOL outperformance as fear-easing signal); ETH ETFs +$36.7M small inflows
- Catalyst: CLARITY Act (market-structure bill) optimism lifting BTC/ETH/XRP sentiment

### On-Chain / Derivatives
- Funding: near-neutral/mildly positive (~0.003%) — leverage washed out vs early-2026 froth; low cascade risk
- Open interest: BTC futures ~$48.9B (+3.5%), balanced positioning
- ETF flows: recent 2-day +$191M bounce reversing a 10-day −$2.73B streak; **net outflows still dominate 7d/30d**
- On-chain: subdued retail demand, negative Coinbase premium, low chain activity → caution

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
_No executable ideas — account is unreachable (empty Bybit creds). Watchlist only, pending fixed connectivity + live quotes:_
1. SOL — thesis: first mover if fear eases / altseason builds; risk-on proxy. Enter only on confirmed BTC-relative strength. Levels TBD on live quotes.
2. ETH — thesis: ETF inflows resuming, stablecoin/RWA platform narrative; but currently a laggard. Wait for reclaim of relative strength vs BTC.
3. BTC — thesis: dominance high + low leverage = cleanest risk-on vehicle if CLARITY Act catalyst lands. Default beta.

### Risk Factors
- **Bybit credentials not set in cloud routine env — top operational risk.** The entire bot cannot trade; morning-execution (9 AM) will fail. 8 days live, still $0 deployed. Escalating via ClickUp.
- Fear-leaning sentiment + choppy range-bound BTC — no strong directional edge
- Net ETF outflows / subdued retail — demand-side weakness
- DXY firm + hawkish-lean Fed — risk-asset headwind
- Thin summer volume amplifies whipsaw

### Decision
TRADE: none. HOLD — mandatory: Bybit API credentials missing from cloud environment; cannot verify account or place/manage orders. Even absent the outage, sentiment is Fear-leaning with no clear edge → HOLD is the correct discretionary call. Fix credential configuration before 9 AM execution routine.
