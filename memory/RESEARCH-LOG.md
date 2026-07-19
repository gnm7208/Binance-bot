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
- **BLOCKED**: Bybit API unreachable. `bybit.sh account` and direct `curl https://api.bybit.com/v5/market/time` both return **HTTP 403 CloudFront** — "distribution is configured to block access from your country" (proxy egress POP `IAD61`, US-East). Bybit does not serve US IPs; this is a hard geo-block, not transient. Same class of failure as the 07-11 Binance 451 — now the **second exchange blocked** from this environment.
- Last known state (Day 0 baseline, TRADE-LOG.md): $10,000.00 USDT, 100% cash, 0 open positions. No unmanaged stop risk, but zero trading capability.
- Perplexity key not set → research done via WebSearch/WebFetch fallback. ClickUp wrapper also erroring (500 / key not configured).
- Trades this week: 0/3 (no entries ever placed).

### Market Context
- BTC: ~$64,376 (roughly flat 24h), total crypto mcap ~$2.27T
- ETH: ~$1,867 (+1.44% 24h)
- BTC Dominance: **57.1%** (up from ~54–56% on 07-11 — BTC leading, alts losing relative ground)
- Fear & Greed Index: **28 (Fear)**
- DXY: ~100.6 (easing from early-July high ~101.4; softer labor data)
- Macro: Fed held 3.50–3.75% (Jun 17). Next FOMC Jul 28–29 (no SEP). Markets price ~12% hike odds in July, ~56% by September; hawkish lean persists.
- Sector leaders (weekly): DeXe (DEXE) +61% to record $49.43; Zcash (ZEC) and Uniswap (UNI) double-digit gains. Dated catalysts: Solana, Hyperliquid (HYPE), Zcash. H2 narratives: SUI, ONDO, LINK, RNDR. Themes: RWA, AI infra, DeFi.

### On-Chain / Derivatives
- Spot BTC ETFs: 4-day net-inflow streak; +$132.3M on Jul 17 (IBIT +$136.5M led); cumulative +$51.4B — mildly supportive.
- BTC perp OI rising with positive funding = leverage building, but **not backed by spot demand** (spot ETFs saw ~$7B outflows May–Jun) — squeeze-risk / fragile setup either direction.

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
1. No new entries possible — Bybit account unreachable (geo-block); execution impossible regardless of setup quality.
2. Environment even so favors caution: dominance rising to 57%, F&G in Fear, leverage-led (not spot-led) derivatives = poor alt-entry conditions. Best posture is patience.
3. Watchlist once connectivity restored: SOL, HYPE, ZEC (fresh momentum) — require dated catalyst + live levels before any entry.

### Risk Factors
- **Bybit API geo-blocked (403 CloudFront) from this cloud environment — highest-priority operational risk.** No account visibility, no order placement/cancellation, no stop management. Two consecutive exchanges (Binance, Bybit) blocked → the cloud egress region (US) cannot reach either exchange's retail API. Needs a fix: non-US egress route, or an exchange that serves the proxy's region.
- Rising BTC dominance + Fear sentiment — alts underperforming, risk-off tilt.
- Derivatives leverage building without spot support — volatility / liquidation risk.

### Decision
TRADE: none. HOLD — mandatory: Bybit API unreachable (403 geo-block), cannot verify account or place/manage orders. Operational blocker escalated. Re-run once exchange connectivity from this environment is resolved.
