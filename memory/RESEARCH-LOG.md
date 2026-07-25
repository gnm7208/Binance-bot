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
- **BLOCKED**: Bybit API returned HTTP 403 (Amazon CloudFront "configured to block access from your country") on `account` and all public/authed endpoints. Confirmed via direct curl to `/v5/market/time` and `/v5/market/tickers` — geo-block, not a key/auth issue. Same operational failure mode as 2026-07-11 (Binance 451). No account visibility, no order placement/cancellation, no stop management possible.
- Last known state (Day 0 baseline, TRADE-LOG.md): $10,000.00 USDT, 100% cash, 0 open positions.
- Trades this week: 0/3.
- Market data below sourced from CoinGecko + alternative.me + WebSearch (all reachable); only the trading venue is blocked.

### Market Context
- BTC: $64,541 (+0.47% 24h)
- ETH: $1,866.74 (+1.19% 24h)
- SOL: $75.89 (+1.12% 24h)
- Total crypto market cap: ~$2.29T (+0.47% 24h)
- BTC Dominance: 56.5% (ETH 9.8%) — "Bitcoin Season" (Altcoin Season Index ~46/100)
- Fear & Greed Index: 28 (Fear)
- DXY: ~100.9, easing from late-June 13-month high (~101.6) on softer labor data
- Macro: FOMC Jul 28-29 — markets price ~94% odds of a hold (no SEP); any move pushed to September. Softer US inflation print mid-July gave risk assets a tailwind.
- Sector leaders: L1s (Solana), DeFi (Hyperliquid), privacy (Zcash) showing relative strength with clear catalysts; AI / DePIN drawing rotational interest. Broad market rangebound near BTC $64k.
- Catalysts: SEC added 3 crypto rulemaking items to its 2026 agenda (Jul 7) — asset sales, custody, market structure; renewed hopes for crypto legislation in H2 2026.

### On-Chain / Derivatives
- Crypto ETF flows: turned positive — week ending Jul 10 saw +$197.4M net (ending 8 weeks of outflows); spot BTC ETFs +$368M over a recent 3-session streak; ETH ETFs leading weekly inflows (~$105M). Institutional flow improving.
- Funding rates: BTC ~+0.32% (43.7% APR), ETH ~+0.40%, SOL ~+0.48% — sustained but moderate long bias; not frothy.
- OI trend: no real-time print retrieved (would need CoinGlass direct); funding suggests measured positioning.

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
1. No executable entries — trading venue (Bybit) is geo-blocked; no order can be placed regardless of setup quality.
2. Watchlist for when access is restored: SOL (L1 leader, +momentum, funding constructive), HYPE (DeFi revenue leader — verify Bybit Spot listing/liquidity), ZEC (privacy narrative reviving). Need fresh catalyst + live quotes before any entry.

### Risk Factors
- **Bybit API geo-blocked (403 CloudFront) from this execution environment — highest-priority operational risk.** Live ~$10k account is untradeable and unmonitored until connectivity is resolved. Recurring: Binance was 451-blocked on Jul 11; venue has changed but the block persists 8 days on.
- Fear & Greed at 28 (Fear) + "Bitcoin Season" — weak breadth, poor environment for aggressive alt entries.
- DXY still elevated near 101 — latent headwind for risk assets despite recent easing.
- FOMC Jul 28-29 event risk — hold widely expected but any hawkish surprise hits crypto.

### Decision
TRADE: none. HOLD — mandatory: Bybit API geo-blocked (403), cannot verify account state or place/manage orders. Even absent the block, environment (Fear + BTC-season + FOMC ahead) does not warrant new entries. Re-run research/execution once venue connectivity is confirmed restored.
