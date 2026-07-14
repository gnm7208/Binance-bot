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

## 2026-07-14 — Morning Research

### Account Snapshot
- **BLOCKED (3rd consecutive day)**: `account`, `positions`, `orders` all fail with HTTP 451 "Service unavailable from a restricted location" — identical error to 2026-07-11, unresolved since. Execution environment's IP is Binance-geo-blocked; this is an infra issue, not fixable from within the bot.
- Last known state: Day 0 baseline (TRADE-LOG.md) — $10,000.00 USDT, 100% cash, 0 open positions. No trades have executed since bot launch.
- Trades this week: 0/3.
- PERPLEXITY_API_KEY not set in this environment (wrapper exited code 3 as designed) — all market research below via native WebSearch fallback.
- ClickUp alert sent flagging the persistent 3-day outage.

### Market Context
- BTC: ~$61,900 (-3.5% 24h; down from ~$64,000 on Jul 13); July candle down ~18% from month open
- BTC Dominance: ~56% (range 56-58% across sources; stablecoin-adjusted reading higher)
- Fear & Greed Index: reported 26 (Fear) on some trackers, 44 (Neutral) on others — treat as Fear-leaning, sentiment fragile
- DXY: ~100.7-100.9, near 13-month high; Fed (new Chair Kevin Warsh) held rates 3.50-3.75% in June, hawkish dot plot (median year-end rate 3.8%, up from 3.4% in March)
- Macro: June CPI print due today (Jul 14) — flagged as the key pivot point for the week; May inflation ran hot at 4.2%; next FOMC Jul 28-29, markets pricing ~62% odds of a September hike (not a cut)
- Sector leaders: Solana strongest major (+16% over 7d, trading $80-85), Solana DeFi fees surging (Orca +150% 30d), RWA transfer volume on Solana doubled to $8.7B/30d, institutional inflows (Clearstream custody, MoneyGram validator); AI-adjacent tokens also drawing speculative flow
- Catalysts: Pump.fun (Solana meme launchpad) unlocked 23.3% of supply Jul 12 — volatility risk in that ecosystem; broader market still lacks a strong bullish catalyst (regulatory clarity / strategic BTC reserve cited as what's needed)

### On-Chain / Derivatives
- Exchange inflows: ~49,000 BTC into exchanges early July — mild bearish/distribution signal, consistent with Jul 11 note
- BTC futures open interest: ~$47.7B notional, down from ~$21.6-31B BTC-denominated peaks earlier in 2026; funding rate modest (~0.0087%, mild long bias) — no leverage euphoria
- Spot BTC ETFs: swung from >$4.1B June outflows to a brief early-July inflow (ended a 10-day/$2.7B outflow streak), fragile improvement

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
1. No new entries proposed — account API still unreachable (451), execution impossible regardless of setup quality. Third day in a row.
2. Watchlist once API access is restored: SOL (L1 momentum + DeFi fee growth + RWA/institutional adoption, but confirm CPI-day volatility has settled and check for pullback entry rather than chasing the 7d run); reassess AI-adjacent names once market has a clearer catalyst.
3. No action on BTC directly — macro (hawkish Fed, hot CPI risk today) argues against fresh risk-on entries until the CPI print and Fed path are clearer.

### Risk Factors
- **Binance API geo-blocked (451), unresolved for 3+ days — top operational risk, needs a human fix to the execution environment/IP, not a bot-side workaround.**
- Hawkish Fed under new chair + DXY near 13-month high — headwind for risk assets
- June CPI release today is a binary near-term volatility catalyst
- Fear & Greed mixed but Fear-leaning — fragile sentiment, poor backdrop for fresh entries
- Net BTC exchange inflows — mild distribution signal
- Pump.fun supply unlock — localized Solana-ecosystem volatility

### Decision
TRADE: none. HOLD — Binance API still unreachable (451) for a 3rd straight day; cannot verify account state or place/manage orders. Re-escalated via ClickUp. Macro backdrop (hawkish Fed, CPI today, Fear-leaning sentiment) would argue for caution even if execution were available. Re-run research/execution once connectivity is confirmed restored.
