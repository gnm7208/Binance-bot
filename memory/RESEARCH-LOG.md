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

## 2026-07-18 — Morning Research

### Account Snapshot
- **BLOCKED (7th consecutive day)**: Binance API returns HTTP 451 "Service unavailable from a restricted location" on `account`, `positions`, `orders` — same geo-restriction as 2026-07-11, still unresolved one week later.
- Last known state: $10,000.00 USDT, 100% cash, 0 open positions (Day 0 baseline — never updated since; no trade has ever executed).
- PERPLEXITY_API_KEY not set in local env — fell back to native WebSearch for all research below.
- Trades this week: 0/3. Trades ever: 0.

### Market Context
- BTC: ~$64,050 (-1.4% 24h per CoinGecko; range $62,528–$64,286)
- BTC Dominance: 56.3%, total crypto market cap ~$2.28T
- Fear & Greed Index: 54 (Neutral) as of Jul 16 — recovering from Extreme Fear (22) printed Jul 14; sentiment whipsawing on geopolitical tension and weak volumes
- DXY: 100.91 (Jul 14), up ~2.8% YTD, easing off early-July highs near 101.39
- Macro: FOMC held 3.50-3.75% at Jun 16-17 meeting; NY Fed's Williams signals no hike needed at Jul 28-29 meeting, but 9/18 FOMC members pencil in a 2026 hike — hawkish lean persists under Chair Warsh
- Sector leaders: Memes +220% YTD, Prediction Markets +80% YTD, AI/GameFi narratives (TAO, Autonolas) drawing bullish flow. Laggards: L1s -28% YTD, DeFi -26% YTD — momentum has rotated away from majors into speculative/attention narratives
- Catalysts today: Cardano "Van Rossem" hard fork live (lower fees, Leios groundwork); GENIUS Act final stablecoin KYC rules due; CLARITY Act Senate floor vote expected this month

### On-Chain / Derivatives
- Bitcoin ETFs: 10-day, $2.73B outflow streak snapped early July; ~$1.2B net inflows week of Jul 10, reversing June's $4.5B outflow record — flows improving
- Funding rates: BTC funding slightly positive (~0.003%), neutral/mild long bias
- Open interest: BTC futures OI ~$48.9B (+3.5%); OI fell ~23k BTC in early July alongside rising price — reads as short squeeze, not fresh conviction

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
1. No new entries proposed — account API unreachable, execution impossible regardless of setup quality.
2. Watchlist only (unconfirmed against live account): meme/prediction-market names showing the strongest 2026 momentum, but these sit outside typical swing-trade risk profile — needs fresh look once quotes/account access restored. AI-narrative names (TAO) remain a secondary watch.
3. L1s and DeFi both down >25% YTD — avoid until sector shows reversal confirmation; two straight down sectors per strategy rule 10.

### Risk Factors
- **Binance API geo-blocked (451), now 7 days running — top operational risk.** Zero account visibility, cannot place/cancel/manage any order. This is no longer a one-off outage; it needs infrastructure-level attention (proxy/region fix), not a daily retry.
- No trade has executed since bot launch (Day 0) — the challenge window is burning with the account fully idle.
- Fear & Greed whipsawing (22 → 54 in 2 days) — unstable sentiment, poor entry conditions even if API were live
- Hawkish FOMC minority (9/18 penciling a hike) — headwind risk for risk assets into the Jul 28-29 meeting

### Decision
TRADE: none. HOLD — mandatory: Binance API still unreachable (451) for the 7th straight day, cannot verify account state or place/manage orders. Escalating via ClickUp given the duration. Re-run research/execution once connectivity is confirmed restored.
