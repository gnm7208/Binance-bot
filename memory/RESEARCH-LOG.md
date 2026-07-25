# Research Log

Daily morning research entries appended below.

---

## 2026-07-10 — Morning Research

### Account Snapshot
- **BLOCKED:** Binance API returned HTTP 451 ("restricted location") on account/positions/orders — could not verify live state.
- Perplexity also unavailable (PERPLEXITY_API_KEY empty) — used WebSearch fallback for all market research.
- Last known state (TRADE-LOG Day 0 baseline): $10,000 USDT, 0 positions, 0/3 trades this week.
- ClickUp alert sent re: API outage.

### Market Context
- BTC: ~$62,650 (+1.9% 24h), market cap $1.27T
- BTC Dominance: ~56% (near one-month high; capital consolidating in BTC, not rotating to alts)
- Fear & Greed Index: 22-26 (Extreme Fear) per most sources; one outlier reads 45 (Neutral)
- DXY: ~100.7-101, dollar firm on Middle East safe-haven demand; forecasts see DXY climbing toward 103.6 by year-end
- Fed: funds rate steady 3.50-3.75% under new Chair Warsh; July FOMC odds ~79.5% hold, ~19.4% hike — soft jobs data cooling near-term hike fears
- Macro notes: digital-asset legislation hopes for Senate action; BTC spot ETFs snapped a 10-day, $2.7B outflow streak with $221.7M inflow
- Sector leaders: AI/GameFi altcoins (Bittensor, Autonolas) leading on narrative strength despite broad Extreme Fear; RWA tokenization (Solana RWA ATH $3.41B); DeFi maturing toward institutional infra

### On-Chain / Derivatives
- Exchange flows: BTC ETF inflows resumed ($221.7M July 2) after $2.7B outflow streak
- Funding rates: BTC funding ~0.0087% (moderate, no euphoria)
- Open interest: ~$47.71B, down from ~368k BTC to ~342-346k BTC in early July — OI falling while price rises = short squeeze, not fresh conviction buying

### News on Held Positions
- N/A — no open positions (bot has not yet made its first trade)

### Trade Ideas
1. No high-conviction setup today — BTC dominance rising (56%) while Fear & Greed sits in Extreme Fear is a mixed signal; move looks like a short squeeze (falling OI) rather than confirmed trend. Wait for confirmation before first deployment.
2. Watch AI/GameFi altcoin narrative (e.g. Bittensor/TAO) for a pullback entry if momentum holds and a clean catalyst emerges.
3. Watch Solana RWA strength as a secondary theme if BTC dominance rolls over and alts catch a bid.

### Risk Factors
- Cannot verify account/position state — trading blind on capital allocation is unacceptable per Buy-Side Gate; do not trade until Binance API access is restored.
- Extreme Fear + falling open interest suggests current BTC strength is short-covering, not durable trend — chasing here risks a fast reversal.
- DXY strength forecast to continue into H2 2026 — headwind for risk assets broadly.
- Fed hike optionality (19.4% priced) not fully off the table — macro uncertainty into next FOMC.

### Decision
HOLD — no trade today. Binance API inaccessible (HTTP 451), so account/position state cannot be confirmed; buy-side gate cannot be satisfied. Re-check API access before morning-execution.

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

## 2026-07-16 — Morning Research (via morning-execution, research entry missing)

### Account Snapshot
- **BLOCKED**: Binance API returned HTTP 451 "Service unavailable from a restricted location" on `account`, `positions`, `orders` — confirmed via direct curl to `/api/v3/ping`, same 451 geo-restriction message. Identical failure to 2026-07-11, unresolved for 5 days.
- Last known state (Day 0 baseline, TRADE-LOG.md, unchanged since no trades ever executed): $10,000.00 USDT, 100% cash, 0 open positions.
- Trades this week: 0/3.
- ClickUp alert sent naming the outage.

### Market Context (WebSearch fallback — Perplexity key not set)
- BTC: ~$65,244 (24h % change not confirmed via this source)
- BTC Dominance: ~56% (Jul 9 reading, most recent available)
- Fear & Greed Index: 36 (Fear) per one tracker; readings range 22-46 across providers — treat as Fear-leaning, not confirmed
- No DXY / macro / on-chain data pulled — execution is blocked regardless, so full research sweep skipped.

### On-Chain / Derivatives
- Not pulled — account API blocked, no position-specific need; skipped given execution is impossible today.

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
- None generated — cannot verify account state, quotes, spreads, or place orders while Binance API is geo-blocked.

### Risk Factors
- **Binance API geo-blocked (451) from this execution environment for 5+ consecutive days (2026-07-11 → 2026-07-16). Highest-priority operational risk — no execution capability at all until resolved.**
- PERPLEXITY_API_KEY not set in this environment — research quality degraded to WebSearch fallback even once trading resumes.
- Fear & Greed near "Fear" territory — sentiment fragile.

### Decision
TRADE: none. HOLD — mandatory: Binance API unreachable (451), cannot verify account state, quotes, or place/manage orders. ClickUp alert sent. This is the second consecutive blocked session since 2026-07-11; recommend escalating environment/network-egress configuration outside the bot's control.

## 2026-07-11 — Morning Research

### Account Snapshot
- **BLOCKED**: `bash scripts/binance.sh account/positions/orders` all returned HTTP 451
  ("Service unavailable from a restricted location according to 'b. Eligibility'") from
  every api*.binance.com host tried (api, api1, api2, api3, api-gcp) — the cloud
  environment's outbound IP is geo-restricted for private/signed Binance endpoints.
  Public data mirror (data-api.binance.vision) still works, used for market prices below.
- Per Trade Log: still Day 0, no positions opened yet, so no open-position exposure to
  verify — but position count / cash / weekly trade count cannot be confirmed from here.
- Trades this week: 0/3 (per Trade Log, no entries yet)

### Market Context
- BTC: $63,008 (-0.55% 24h) — live pull from data-api.binance.vision
- ETH: $1,759.48 (-1.15% 24h) — live pull from data-api.binance.vision
- BTC Dominance: ~55.5-56.2% (sources vary; stablecoin-adjusted would run a few pts higher)
- Fear & Greed Index: ~22-24 (Extreme Fear)
- DXY: ~100.9, holding below 101 — softer June NFP (+57k vs 110k expected) cut Fed hike
  odds, pressuring dollar and supporting risk assets incl. crypto
- Macro notes: Weak labor data reduced Sept rate-hike odds to ~50% (from ~66%); real wages
  negative (3.5% nominal earnings vs 4.2% CPI) keeps Fed's Warsh boxed in on dovish easing;
  July 29 FOMC is next major catalyst
- Sector leaders: DeFi firming (AAVE +9% wk, strongest Ethereum new-wallet day since 2021,
  ~$12.2B TVL) despite broader weakness. L1s weakest narrative, -22.8% in Q2. AI tokens
  mixed (TAO, FET, ICP cited as leaders) but breadth poor (21 gainers/35 losers). Gaming
  narrow/momentum-driven (BEAT +112% on burn news, not broad strength).
- Note: initial WebSearch pass for BTC price returned a conflicting $99,887/+4.18% figure
  from a low-quality source — discarded in favor of the direct Binance public-data pull
  above, which is authoritative.

### On-Chain / Derivatives
- Spot BTC ETFs: snapped 10-day, $2.7B outflow streak with +$221.7M inflow (largest daily
  haul in 2 months), timed with the soft payrolls print
- BTC funding rates: ~0.0087%, moderate — fresh leverage building, no euphoria
- Open interest: ~$47.7B; short liquidations ($86.6M) outweighing longs ($54.0M), i.e.
  shorts getting squeezed on the bounce

### News on Held Positions
- None — no open positions (Day 0)

### Trade Ideas
No trade ideas this session — account state (cash, position count, weekly trade count)
cannot be verified due to the Binance API access blocker above, so the buy-side gate
cannot be evaluated regardless of setup quality. DeFi (AAVE) is the strongest momentum
sector today and worth first look once account access is restored.

### Risk Factors
- Binance private/signed API endpoints are geo-blocked (HTTP 451) from this environment —
  hard blocker on account state, execution, and stop management until resolved
  (proxy/network config or environment IP change needed)
- Fear & Greed at extreme fear (~22) — contrarian bounce signal but also reflects real
  downside risk/volatility
- Sentiment/price data conflicting across sources today — cross-check before acting
- July 29 FOMC and pending CLARITY Act / XRP catalyst could move the market sharply

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
