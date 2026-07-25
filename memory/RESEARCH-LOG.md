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

## 2026-07-08 — Morning Research

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

## 2026-07-12 — Morning Research

### Account Snapshot
- **BLOCKED (2nd consecutive day)**: Binance API returned HTTP 451 (geo-restricted) on `account`, `positions`, `orders` — same failure as 2026-07-11, unresolved.
- Last known state (Day 0 baseline, TRADE-LOG.md): $10,000.00 USDT, 100% cash, 0 open positions.
- ClickUp alert sent flagging persistent outage — needs infra fix (proxy/region), not a retry issue.
- Trades this week: 0/3 (per TRADE-LOG, no entries yet).
- Perplexity also unavailable today: `PERPLEXITY_API_KEY not set`, exit code 3 → fell back to native WebSearch for all queries per fallback rule.

### Market Context
- BTC: ~$64,000–$64,300 (+0.5-0.9% 24h), total crypto market cap ~$1.29T (WebSearch, sources vary)
- BTC Dominance: ~54-58% depending on source; broad consensus mid-to-high 50s%, one report flags "Bitcoin Season" (Altcoin Season Index 46/100)
- Fear & Greed Index: 26 (Fear) most-cited reading today; other trackers show 20-45 across methodologies — treat as Fear-leaning
- DXY: ~100.5-100.7, down from a 5-week high (~101.5) in late June; Fed funds decision July 28-29, market pricing ~62% odds of a September hike, mixed/uncertain outlook
- Sector leaders: DeFi maturing (Aave, Uniswap, Compound — regulatory clarity tailwind); AI/blockchain fusion (TAO, Autonolas); gaming presale flow continues; Solana RWA ecosystem at ATH $3.41B; Robinhood Chain now #2 Uniswap deployment chain by volume
- Catalysts: APT unlocks 1.31% of supply (~$6.78M) today; Senate targeting Aug 7 for final CLARITY Act draft; US-Iran geopolitical situation remains a TBD macro risk

### On-Chain / Derivatives
- Binance-wide aggregate flow/funding data not retrievable via WebSearch fallback (no CoinGlass/Binance-direct access)
- XRP-specific data point only: Binance funding rate recovered to 0.007 (+266% WoW) after briefly negative in late June; XRP OI falling ($500M mid-June → $399M by Jul 10); long liquidations +94% WoW
- No BTC/ETH funding or OI figures obtained today — gap in coverage

### News on Held Positions
- None — 0 open positions.

### Trade Ideas
1. No new entries proposed today — Binance API unreachable (451), so no execution possible regardless of setup quality.
2. Watchlist unchanged from 2026-07-11, pending API access: SOL (L1 momentum, RWA growth ATH), TAO (AI/blockchain narrative), DeFi blue-chips (AAVE/UNI on regulatory clarity) — need fresh catalyst + live levels once connectivity restored.

### Risk Factors
- **Binance API geo-blocked (451), unresolved for 2 straight sessions — top operational risk.** No account visibility, no order placement/cancellation/stop management possible.
- Perplexity API key also missing today — research quality degraded to WebSearch-only, less precise/current data (e.g., no direct BTC/ETH funding rates).
- DXY off recent highs but Fed policy still uncertain/hawkish-leaning — mixed macro backdrop
- Fear & Greed in Fear territory — fragile sentiment, not a green light for aggressive entries
- APT token unlock today — localized volatility in that name only (not held)

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
