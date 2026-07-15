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

## 2026-07-15 — Morning Research

### Account Snapshot
- **BLOCKED — Day 4 of outage**: `account`, `positions`, `orders` all fail with HTTP 451 "Service unavailable from a restricted location" (same geo-block first hit 2026-07-11, unresolved 4 calendar days straight).
- Last known state: Day 0 baseline (TRADE-LOG.md) — $10,000.00 USDT, 100% cash, 0 open positions. No trades have been recorded since, so this is still the most current confirmed figure.
- PERPLEXITY_API_KEY / PERPLEXITY_MODEL also missing from environment — used WebSearch fallback for all market research below (per STEP 3 fallback rule).
- Trades this week: 0/3 (per TRADE-LOG, no entries recorded).

### Market Context
- BTC: ~$62,500–$63,000 (down slightly on the day; June 2026 was BTC's worst month in 4 years, some "green July" seasonal rebound chatter)
- BTC Dominance: ~56–58%, still elevated (some sources show a brief one-month-low dip to ~54% dip earlier in the month before recovering); CMC Altcoin Season Index 46/100 — Bitcoin Season territory
- Fear & Greed Index: sources disagree sharply — 22 (Extreme Fear) vs. 44-48 (Neutral); treat as fear-leaning but unconfirmed, same cross-provider divergence as 07-11
- DXY: ~100.7-100.9, range-bound 100.5-102 for 3 weeks; softer June CPI (3.5% vs 3.8% expected) cooled hike odds, but 9 of 18 FOMC members now pencil in a 2026 hike — hawkish tail risk into the Jul 28-29 FOMC under Fed Chair Warsh
- Macro: US resumed strikes on Iran / naval blockade reinstated after interim peace deal broke down — fresh Strait of Hormuz tension, risk-off drag on crypto Monday; CLARITY Act 2026 passage odds trimmed to ~48% (Senate cloture math unresolved, White House had wanted July 4 deadline)
- Sector leaders: DEX (+10.2%) and Lending (+8.8%) led gains this week; Meme -5.5%. YTD: AI +42.9%, Gaming +2.1%, DeFi -25.6%, Layer1 -28% (broad L1 underperformance). AI narrative reviving (DeXe breakout, TAO/NEAR near technical inflections); Solana RWA TVL fresh ATH $3.41B

### On-Chain / Derivatives
- Could not pull current CoinGlass/Binance funding-rate or OI prints via WebSearch fallback — no live figure (same gap as 07-11 entry); flagged as recurring blind spot while Perplexity access is down.
- Prior data point (07-11, may be stale): net BTC exchange inflows ~4,933 BTC/7d, Binance largest single inflow (~2,007 BTC) — mildly bearish distribution signal; June 2026 BTC ETF outflows >$1.6B

### News on Held Positions
- None — 0 confirmed open positions (per last verified account state).

### Trade Ideas
1. No new entries proposed — account API still unreachable (451, day 4), so no execution is possible regardless of setup quality. Buy-side gate requires live position count + USDT balance, which we cannot verify.
2. Watchlist only (unchanged thesis from 07-11, re-confirmed by this week's sector data): SOL (L1 momentum via RWA growth, though broader L1 sector is down ~28% YTD — mixed signal), TAO (AI narrative strength, DeXe/NEAR also near breakouts), DEX/Lending-sector names (best-performing categories this week) — need fresh catalyst + live levels once account access is restored.

### Risk Factors
- **Binance API geo-blocked (451), now 4 consecutive days — escalating operational risk.** No account visibility, no order placement/cancellation/stop management. This is no longer a one-off outage; needs infra/access investigation, not just a daily retry.
- Geopolitical: renewed US-Iran conflict / Strait of Hormuz risk — active risk-off driver for crypto
- Fear & Greed readings fear-leaning but inconsistent across providers — low-conviction signal either way
- DXY range-bound with hawkish 2026-hike tail risk into July 28-29 FOMC — potential headwind
- Layer1 sector down ~28% YTD — avoid until momentum turns; DEX/Lending and AI are the week's relative strength
- Perplexity API key missing — research quality degraded to WebSearch-only until credential is restored

### Decision
TRADE: none. HOLD — mandatory: Binance API unreachable (451) for a 4th straight day, cannot verify account state or place/manage orders. Escalating via ClickUp given outage duration. Re-run research/execution once connectivity is confirmed restored.
