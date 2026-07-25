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

## 2026-07-25 — Morning Research

### Account Snapshot
- Total portfolio value: $32.32 USDT (MEXC Spot API healthy — `account`/`positions`/`balance` all returned; the old Binance 451 block does not apply, we are on MEXC)
- Free USDT: $32.32 (100%)
- Open positions: 0
- Trades this week: 0/25

### Market Context
- BTC: $64,113 (−1.3% 24h)
- ETH: $1,860 (−, soft recovery attempt)
- SOL: $74.35 (−2.18% 24h)
- BTC Dominance: ~56.4% (high/rising — capital NOT rotating to alts; broad alt weakness)
- Fear & Greed Index: 27 (Fear) on alt.me trackers / 46 (Neutral) on CFGI — Fear-to-Neutral, cautious
- DXY: ~100.6 (range-bound, ~2pts off late-June high)
- Total crypto mcap: ~$2.28T (−1.1% 24h) — broad risk-off tape today
- Macro: **FOMC Jul 28–29** (Chair Warsh, statement Wed 2pm ET). Consensus = hold 3.50–3.75%; ~33% pricing a 25bp HIKE; no dot plot this meeting. Month-end options expiry + Big Tech earnings same week → elevated event risk.
- Sector leaders bucking the red tape: DeXe (DEXE), LayerZero (ZRO), BEAT, Lorenzo Protocol (BANK, near ATH); narrative flow in Solana ecosystem, AI (Venice/VVV, TAO), Telegram-DeFi (TAC)

### On-Chain / Derivatives
- Perplexity key not set in cloud env → WebSearch fallback; no real-time funding/OI print retrieved
- Context: broad −1% tape with rising BTC dominance = defensive rotation into BTC, alts underperforming
- Prior signal (stale): net BTC exchange inflows / mild distribution — monitor, unconfirmed today

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
Tape is red into FOMC — only relative-strength names that are GREEN today qualify (strategy gate: 24h ≥ +2% OR strong catalyst). Majors (BTC/SOL) FAIL the momentum gate today. Candidates below must be re-validated for live ≥ +2% 24h at 9AM execution before any order:
1. **BANK (Lorenzo Protocol)** — px $0.3116. Catalyst: pressing new ATH while broad tape is red (relative-strength breakout). Entry ~$0.312, stop-limit −10% $0.2805 (hard cut −7% $0.290), target +7% $0.334. Sector: DeFi/RWA yield. *Confirm it's still ≥+2% 24h at execution.*
2. **DEXE / ZRO / BEAT** — flagged as today's top gainers vs a down market. No live MEXC level captured yet; pull `price` + 24h at execution, enter only the one printing ≥ +2% 24h with the cleanest structure. Entry = live px, stop −10%, target +7%.
3. **VVV (Venice)** — px $12.51. Watch-only: AI narrative + product traction, but need a confirmed +2% day or fresh catalyst; not qualifying on today's tape.

### Risk Factors
- **FOMC Jul 28–29 with a live ~33% hike tail** — binary event risk 3 sessions out; avoid getting caught in size before it. Prefer waiting or tiny size.
- Red broad tape (−1.1% mcap) + rising BTC dominance → alt longs fighting the current; momentum entries fragile, whipsaw risk high.
- Tiny account ($32.32): 20% cap = ~$6.46/position. MEXC min-notional (~$1–5) makes positions viable but fees/slippage are a larger % drag — size deliberately, avoid over-trading.
- F&G in Fear — sentiment thin.

### Decision
HOLD-biased. No high-conviction entry on a red pre-FOMC tape. If 9AM execution confirms a candidate (BANK first) still printing ≥ +2% 24h with clean structure, ONE small starter (~$6, ≤20%) with immediate −10% stop-limit is acceptable; otherwise stay 100% cash into FOMC. Do not deploy broadly before Jul 29.
