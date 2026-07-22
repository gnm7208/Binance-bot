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

## 2026-07-22 — Morning Research

### Account Snapshot
- MEXC API reachable (SPOT, canTrade=true). Binance 451 issue resolved via migration to MEXC wrapper.
- **Free USDT: $0.00 — account UNFUNDED. 0 open positions, empty balances.** No execution possible regardless of setup quality.
- Trades this week: 0/15.

### Market Context
- BTC: ~$66,321 (live MEXC) — first push above $66k since Jun 17, recovering on institutional demand
- ETH: ~$1,931 (live MEXC) — notably weak vs BTC; ETH/BTC underperforming, laggard
- BTC Dominance: ~56.4% — elevated; capital NOT yet rotating into alts
- Fear & Greed: inconsistent across providers (29 on Jul 20 → some show 72 Jul 22, others 34/46). Treat as Neutral, improving-but-unconfirmed. Not confirmed Greed.
- Altcoin Season index: 55/100 — highest in months, but mixed follow-through
- DXY: strong; would reverse (crypto tailwind) only if Fed pivots to easing
- Macro: **FOMC meeting late July = event risk.** 5 straight days of spot BTC ETF inflows (~$727M, BlackRock IBIT leading $116.5M); total BTC ETF AUM > $79B
- Sector notes: AI tokens weak today (FET -2.9%, TAO -2.6%); DePIN/AI mixed; PUMP social-driven memecoin surge. Majors/BTC leading, alts lagging.

### On-Chain / Derivatives
- BTC ETF: 5-session inflow streak, ~$727.3M total; last session +$226.9M (best since Jul 6) — bullish institutional demand
- Funding rate: ~0.0043%/day (neutral, ~1.56% annualized) — no overheating, healthy
- Open interest: ~$48.9B, stable (+3.5-3.9% 30d) — no crowded leverage
- Long/short: 54.1/45.9 (1.18x) — only mildly long-biased

### News on Held Positions
- None — 0 open positions.

### Trade Ideas (watchlist — NOT executable, account unfunded; levels off live MEXC quotes)
1. BTC — best risk-adjusted in a high-dominance tape. Catalyst: 5-day ETF inflow streak + reclaim of $66k, neutral funding (room to run). Entry: hold above ~$66,300; stop ~$61,700 (-7%); target ~$72,950 (+10%). Sector: majors/BTC.
2. BNB — exchange/L1, holds up in BTC-led regimes. Live ~$572.5. Entry ~$573; stop ~$533 (-7%); target ~$630 (+10%). Sector: exchange/L1. Conditional on BTC staying bid.
3. SOL — L1 leader, live ~$78.1. Only if dominance starts rolling over / alt-season index >60. Entry ~$78.1; stop ~$72.6 (-7%); target ~$85.9 (+10%). Sector: L1. Higher beta — wait for confirmation.

### Risk Factors
- **Account unfunded ($0 USDT) — hard operational blocker. No trade can execute. Highest priority.**
- Late-July FOMC event risk — avoid entering into the meeting
- High BTC dominance (56.4%) + weak ETH → alts fragile; favor majors if/when funded
- F&G readings contradictory — sentiment signal unreliable this print
- DXY strength — macro headwind unless Fed pivots

### Decision
HOLD. No entries. Even with a constructive BTC tape (ETF inflows, neutral funding, $66k reclaim), the account holds $0 and cannot execute; late-July FOMC also argues against fresh risk. Watchlist above ready for when funding lands and post-FOMC. Fund the MEXC account to resume operations.
