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

## 2026-07-21 — Morning Research

### Account Snapshot
- **BLOCKED**: MEXC authenticated API returns `code 700007 "No permission to access the endpoint"` (HTTP 400) on `account`/`positions`/`orders`. Public endpoints (price, ticker, time, ping) all work fine, so it's not a geo-block — it's an API-key permission / IP-whitelist issue (key lacks Spot read/trade scope, or this run's egress IP isn't whitelisted on the MEXC key).
- Env vars ARE present (MEXC_API_KEY, MEXC_SECRET_KEY, MEXC_BASE_URL set). So it's the key's config on MEXC's side, not a missing secret.
- Last known state (TRADE-LOG Day 0 baseline): $10,000.00 USDT, 100% cash, 0 open positions. No trades ever executed.
- Trades this week: 0/15. Circuit breaker: NOT active (0 closed trades).

### Market Context
- BTC: ~$65,300–66,300 (+0.8% to +2.1% 24h) — rebounded off ~$64k support back above $65k; momentum weakening, volume declining
- ETH: ~$1,905–1,935 (+1.7% to +2.3% 24h)
- SOL: $78.37 (+1.6%) | BNB: $576 (+1.0%)
- BTC Dominance: 56.3% (firm; capital not decisively rotating to alts)
- Total crypto market cap: ~$2.28–2.31T
- Fear & Greed: **25 (Extreme Fear)** — deteriorating from 29 (Fear) yesterday
- DXY: strong-dollar backdrop persists (BTC/DXY correlation ~ -0.6 to -0.8 = headwind)
- Macro: FOMC **Jul 29** (Warsh) — held 3.50–3.75% in Jan & Mar, data-dependent, no urgency to cut. Geopolitical tensions weighing on risk assets (equities down 3rd straight session).
- Catalyst: CLARITY Act dispute easing (White House + Senate R's agreed on ethics provisions) — potential risk-appetite tailwind

### On-Chain / Derivatives
- BTC futures OI: $48.93B (stable, +3.9% 30d) — no leverage blow-off building
- Funding: neutral ~0.0043%/day (1.56% annualized); long/short 54/46 (1.18x) — not overcrowded, no contrarian signal
- ETF flows: short-term recovery (~$191M in over 2 days mid-July, +$273M recent) BUT structural headwind intact — YTD net **-$5.4B**, 30d **-$4.1B**. Institutions still net-reducing.

### News on Held Positions
- None — 0 open positions.

### Trade Ideas (WATCHLIST ONLY — execution blocked by API)
1. ADA — catalyst: first community-led hard fork completed today (+5.6%). Spot ADAUSDT. Wait for pullback/hold above breakout; entry on retest, stop -8%, target +10% cap. Sector: L1.
2. WLD — catalyst: Grayscale Worldcoin ETF filing (+4.75%). Momentum name; size small, stop -8%. Sector: AI/identity. Higher volatility risk.
3. SOL — L1 leader holding $78 above support; tokenized-stocks + prediction-market growth. Entry on strength above $79, stop ~$72 (-8%), target +10%. Sector: L1.
- Avoid the meme spikes (JIMOTHY +122%, PONS +72%) — outside strategy.

### Risk Factors
- **MEXC authenticated API blocked (700007) — highest-priority operational risk.** No account visibility, no order placement, no stop management. Same class of blocker as the prior Binance 451; migration didn't fix execution.
- Extreme Fear (25) + weakening BTC momentum + declining volume + risk-off geopolitics = poor entry environment
- Structural ETF outflows (-$5.4B YTD) and firm DXY — macro headwinds intact
- FOMC Jul 29 event risk approaching

### Decision
**HOLD — no entries.** Two independent reasons: (1) mandatory — MEXC authenticated API unreachable (700007), cannot verify state or place/manage orders; (2) even if live, Extreme Fear + fading momentum + risk-off macro offer no strong edge. Watchlist (ADA/WLD/SOL) parked pending API fix. Operational blocker escalated.
