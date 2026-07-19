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
- **BLOCKED (still unresolved, day 8):** `bash scripts/binance.sh account/positions/orders` all return `curl: (22) ... 451` from `api.binance.com`. Same geo-restriction error as 2026-07-11 — no fix has landed in 8 calendar days.
- `BINANCE_BASE_URL` confirmed set to `https://api.binance.com` (default, unchanged) — not a misconfigured env var, the execution environment's IP is geo-blocked by Binance.
- Last known state (Day 0 baseline, TRADE-LOG.md): $10,000.00 USDT, 100% cash, 0 open positions. No trades have executed since bot launch — account has been completely idle.
- `PERPLEXITY_API_KEY` also missing from environment this run; `scripts/perplexity.sh` fell back to WebSearch automatically (all queries below via WebSearch).
- Trades this week: 0/3 (no TRADE-LOG entries exist beyond Day 0 baseline).

### Market Context
- BTC: ~$63,900–$64,250 (+0.2–0.4% 24h), off the ~$65K local high on Jul 15; failed to hold low-$70Ks range earlier in the month
- BTC Dominance: conflicting reads, 54–60% depending on source/methodology; broad theme is dominance easing off highs as capital rotates to select alts
- Fear & Greed Index: 25 (Extreme Fear) — essentially unchanged from Jul 11 (23-26) and Jul 5 (24); sentiment has been stuck in Fear/Extreme Fear for 2+ weeks
- DXY: ~100.6–100.9, softening off early-July highs (~101.4) on cooler inflation data, but Mideast conflict keeping a safe-haven floor under it
- Macro: Fed Chair Kevin Warsh (Powell now a regular Governor) holding a hawkish, data-dependent neutral stance; 9 of 18 FOMC members now pencil in at least one more hike in 2026 — a meaningfully more hawkish tilt than prior meetings
- Crypto sector leaders: total mkt cap ~$2.27-2.28T. 2026 YTD by narrative: AI tokens +42.9%, Gaming +2.1%, but L1s -28.0% and DeFi -25.6% — momentum has rotated hard toward AI-narrative names and away from L1/DeFi. RWA tokenization (Ondo, +17% on the day in one report) a bright spot within DeFi
- Catalysts: fresh US strikes on Iran (5th day of escalation) pushing BTC below $63K intraday on risk-off flows; Friday's CLARITY Act hearing (market-structure bill) and Q2 options expiry both live this week; AI-stock fatigue bleeding into AI-token sentiment

### On-Chain / Derivatives
- Spot BTC ETFs: snapped a 10-day outflow streak with a $221.7M single-day inflow (largest in 2 months); week-to-date ETF inflows ~$1.2B, a sharp reversal from June's ~$4.5B net outflows — first clearly positive institutional signal in over a month
- Binance retail positioning: BTCUSDT longs 54.1% / shorts 45.9%, below the 30-day average long share of 62.9% — retail has de-risked relative to its recent norm
- Open interest: reported as falling in several trackers, suggesting the recent bounce lacks broad conviction
- No Binance-specific funding-rate print available via WebSearch fallback (would need direct CoinGlass/Binance futures pull, out of scope for spot-only bot)

### News on Held Positions
- None — 0 open positions (unchanged since Day 0).

### Trade Ideas
1. No new entries proposed — account API remains unreachable (451), so no execution is possible regardless of setup quality. This is the 2nd consecutive research cycle blocked this way (8 days apart), suggesting the outage is not transient.
2. Watchlist once connectivity restored: AI-narrative names (sector +42.9% YTD, still holding despite today's AI-stock-fatigue pullback) — need Binance Spot listing check + fresh catalyst/levels before any entry.
3. RWA/tokenization within DeFi (Ondo +17% one-day move cited) — DeFi sector broadly down YTD but RWA sub-theme showing relative strength; watch for continuation vs. one-off pop.

### Risk Factors
- **Binance API geo-blocked (451), unresolved for 8+ days across two research cycles — top operational risk.** No account visibility, no order placement/cancellation/stop management. The bot has been fully idle since launch; every day this persists is a day the strategy cannot execute regardless of market opportunity.
- Fear & Greed stuck at Extreme Fear (25) for 2+ weeks — sentiment fragile, no confirmed reversal
- Hawkish FOMC tilt (9/18 members penciling a hike) under new Fed Chair Warsh — headwind for risk assets
- Active US-Iran conflict (5th day of strikes) — geopolitical tail risk driving intraday BTC drawdowns
- L1s (-28% YTD) and DeFi (-25.6% YTD) sector weakness — avoid new entries in these sectors even once API access returns, per momentum/exit rules
- `PERPLEXITY_API_KEY` missing from environment — research quality this cycle relies on WebSearch fallback only, not cross-verified against Perplexity

### Decision
TRADE: none. HOLD — mandatory: Binance API still unreachable (451) after 8 days, cannot verify account state or place/manage orders. Escalating via ClickUp (repeat/persistent outage, distinct from one-off alert). Re-run research/execution once connectivity is confirmed restored; recommend a human check the account's API key IP-restriction settings and Binance's compliance/geo-restriction status for this environment's egress IP.
