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
- **STILL BLOCKED (Day 8 of outage)**: Binance API returns HTTP 451 "restricted location" on all calls (`price`, `account`, `positions`). Confirmed again today via `scripts/binance.sh`. No account visibility, no order placement/management possible.
- Env note: `PERPLEXITY_API_KEY` is empty in this cloud run (len 0) → research via WebSearch fallback. `BYBIT_*` keys unset; live infra is Binance (creds present) despite CLAUDE.md referencing Bybit. ClickUp wrapper works.
- Last known state (Day 0 baseline, TRADE-LOG.md): $10,000.00 USDT, 100% cash, 0 open positions. Unchanged for 8 days — no trades executable.
- Trades this week: 0/3.

### Market Context
- BTC: ~$64,376 (roughly flat 24h, ~+1% vs last week's ~$63,800)
- BTC Dominance: ~56–60% across sources (call it ~57%); still elevated, mild alt rotation
- Fear & Greed: wide dispersion — 22–25 (Extreme Fear) on most trackers, 54 (Neutral) on one; Fear-leaning
- DXY: ~100.5, at a ~4-week low, cooling from early-July 101.4 after weak June payrolls (+57k, May revised to 129k)
- Macro: Fed hold now the base case — ~65% odds of no change at Jul 29 (range 3.50–3.75%). Tension: inflation 4.2% (tighten) vs soft labor (hold). Geopolitical/energy adds upside inflation risk.
- Sector leaders: SOL strongest major (+~16% on the week, record on-chain activity, Alpenglow upgrade catalyst); AI (TAO/Bittensor) narrative intact; DeFi (Uniswap/Robinhood partnership) firm

### On-Chain / Derivatives
- Spot BTC ETFs: turned net positive — ~$1.2B weekly inflow, reversing a 10-day/$2.73B outflow streak and June's record $4.5B outflow. AUM recovered to ~$78B. But 30-day trend still net outflow.
- Funding: neutral (balanced positioning)
- Open interest: BTC futures OI ~$48.9B, +3.5% — mild leverage rebuild

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
1. **No executable entries** — Binance API unreachable, so no order can be placed regardless of setup quality. All ideas are watchlist-only.
2. Watchlist (execute only once connectivity restored + fresh levels): **SOL** — strongest-sector L1 momentum, Alpenglow upgrade catalyst, record activity; **TAO** — AI narrative leader; **UNI** — DeFi + Robinhood distribution.

### Risk Factors
- **Binance API geo-blocked (451) for 8 consecutive days — top operational risk.** Bot is fully non-functional: no account read, no execution, no stop management. Persisting unresolved.
- Extreme Fear sentiment + still-elevated BTC dominance → fragile alt setups; not a clean risk-on entry backdrop
- Inflation 4.2% with hawkish-leaning Fed under Warsh — headwind for risk assets despite DXY softening
- ETF flows improving but 30-day trend still net outflow — not confirmation yet

### Decision
TRADE: none. HOLD — mandatory. Binance API unreachable (451), 8th straight day; cannot verify account or place/manage orders. Re-escalated via ClickUp. Even absent the outage, backdrop (Extreme Fear + high dominance) argues patience. Re-run once connectivity confirmed.
