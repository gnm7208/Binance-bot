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

---

## 2026-07-19 — Morning Research

### Account Snapshot
- **BLOCKED**: Bybit API returns HTTP 403 via CloudFront — "The Amazon CloudFront distribution is configured to block access from your country." Hits both authed (`account`, `positions`, `orders`) and public (`price`, `quote`) endpoints. Confirmed via direct curl to `/v5/market/time`.
- **The Binance→Bybit migration did NOT restore exchange access** — same geo-block wall, different exchange (Binance was 451, Bybit is 403/CloudFront). Root cause is the cloud exit IP's country, not the exchange.
- Perplexity also unavailable (PERPLEXITY_API_KEY not set in cloud env) — research via WebSearch fallback only.
- Last known state (Day 0 baseline, TRADE-LOG.md): $10,000.00 USDT, 100% cash, 0 open positions → **no open risk exposure, no stops to manage.**
- Trades this week: 0/3 (no entries yet).

### Market Context
- BTC: ~$64,600 (rebounded from <$58k earlier in July); options flow betting $72k by month-end
- ETH: ~$1,737 (-2.9% 24h) · SOL: ~$77.28 (-5.2% 24h) · XRP: ~$1.09 (-2.9% 24h) — alts broadly red
- BTC Dominance: ~58.8% (rising; total crypto mcap ~$1.30T) — capital rotating INTO BTC, OUT of alts
- Fear & Greed Index: ~36 (Fear); range 27–46 across trackers mid-July → cautious sentiment
- DXY: ~100.7 (eased from ~101.4 early July); hawkish Waller put a July hike back on the table, but market ~65% odds Fed HOLDS on Jul 29
- Macro: inflation 4.2% (argues tighten) vs weak 57k payrolls (argues hold) — Fed split; Middle East/Iran tension adding risk-off + energy-inflation pressure
- Sector leaders: Polkadot ecosystem, XRP Ledger ecosystem (only green pockets today)

### On-Chain / Derivatives
- Spot BTC ETF inflows: +$132M/day; ETH products +$36.7M — institutional bid intact despite volatility
- Funding/OI: no real-time print (Perplexity down, exchange geo-blocked) — would need CoinGlass direct

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
1. **No entries possible** — exchange API geo-blocked, cannot place or manage orders regardless of setup quality.
2. Environment is also poor for alt entries even if live: rising BTC dominance + alts red + Fear sentiment + geopolitical risk-off = not a momentum window for alts. BTC itself is the relative strength but strategy is spot swing on alts/sectors.
3. Watchlist for when access is restored: BTC (relative strength, ETF bid, $72k options target) as a dominance-play anchor; monitor Polkadot/XRP ecosystems if rotation continues.

### Risk Factors
- **Exchange API geo-blocked from this execution environment — highest-priority operational risk, now confirmed across BOTH Binance and Bybit.** The migration did not fix it; the challenge cannot run from this cloud IP. Needs an infra fix (proxy/VPN/allowed region or a different exit), not another exchange swap.
- Rising BTC dominance — alt headwind
- Fear sentiment + Middle East geopolitical risk — fragile risk appetite
- Hawkish Fed tail risk (Waller) — DXY/rates headwind for crypto

### Decision
TRADE: none. HOLD — mandatory: Bybit API geo-blocked (403 CloudFront), cannot verify account or place/manage orders. No open positions, so no exposure at risk. Escalating: exchange access is an infra/geo problem that a second exchange migration did not solve. Re-run once a non-geo-blocked route to a spot exchange is in place.
