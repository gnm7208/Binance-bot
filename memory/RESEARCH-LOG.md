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

## 2026-07-21 — Morning Research

### Account Snapshot
- **PARTIAL API OUTAGE**: MEXC `/api/v3/account` returns `code 700007 "No permission to access the endpoint"` (HTTP 400). Breaks `account`/`balance`/`positions`/`close` (all read /account). Signed `openOrders` returns 200 `[]`; `order`/`cancel`/public price/quote all work. Key present (18-char key / 32-char secret), timestamp skew ~1.5s (fine). → API-key permission/whitelist issue, human fix needed.
- Open orders: **0** (openOrders empty → no active stop orders).
- Last known state (TRADE-LOG): $10,000 USDT, 100% cash, 0 positions. Cannot re-verify balances due to 700007.
- Trades this week: 0/15.

### Market Context
- BTC: ~$66,377 (+2.3% 24h) — reclaiming $66k on renewed ETF demand
- ETH: ~$1,935 (+2.7% 24h) — laggard, ~49% below Oct-2025 high; Glamsterdam upgrade slipped to Q3
- SOL $78.4 (+1.8%), BNB $577 (+1.2%), XRP $1.136 (+2.9%) — majors broadly green
- BTC Dominance: ~56.3–56.6% (elevated) — risk-off consolidation, no alt season (Alt Season Index ~30–35)
- Total crypto mcap: ~$2.3T (≈-47% from Oct-2025 peak)
- Fear & Greed: **25 (Extreme Fear)**, down from 29 prior day — sentiment fragile despite green tape
- DXY: ~101 (firm) — safe-haven bid on Middle-East tension + rising oil/yields
- Macro: Fed held 3.50–3.75% (Jun); **FOMC Jul 28–29 = week's dominant catalyst**. Soft Jun CPI (Jul 14) cut Jul-hike odds to ~6%, but Sep-hike odds ~55%; Chair Warsh hawkish lean
- Sector leaders: DeFi (UNI first higher-high in months; Curve LlamaLend 2 activated on ETH mainnet today), AI (TAO/RENDER), RWA (ONDO); privacy (ZEC) hot but "privacy crackdown" headline risk; DeXe (DEXE) at record high

### On-Chain / Derivatives
- Spot BTC ETF: **5 consecutive inflow days**, +$227M on Jul 20 (outflow streak ended)
- Open interest: total derivatives OI +10.6% to ~$418B; BTC futures OI ~$48.9B; funding neutral-to-slightly-positive
- Short liquidations ~$31.7M — mild squeeze fueling the bounce

### News on Held Positions
- None — 0 open positions.

### Trade Ideas (watchlist — see Decision)
1. **BTC** — catalyst: 5-day ETF inflow streak + $66k reclaim; best risk-adjusted long in high-dominance/risk-off regime. Entry on dip ~$65,000, stop ~$60,450 (-7%), TP ~$71,500 (+10% cap). R:R ~1.4:1 (capped by +10% rule) — modest.
2. **UNI** — catalyst: DeFi momentum, first higher-high in months, Curve LlamaLend 2 activation today. Confirm MEXC spot liquidity + levels before any entry; stop -7%, TP +10%.
3. **SOL** — catalyst: L1 leader holding $78 with market; add-on-strength candidate if BTC.D rolls over post-FOMC. Stop -7%, TP +10%.

### Risk Factors
- **F&G 25 (Extreme Fear) + BTC.D ~56.5%** = risk-off; alts fragile, capital hiding in BTC
- **FOMC Jul 28–29 = binary event ~1 week out** — avoid heavy deployment into it
- DXY ~101 + hawkish Warsh Fed + Middle-East/oil = macro headwind for risk assets
- **Operational: /account 700007** — cannot verify balances/positions or use `close` (market-sell) until key permission fixed; risk-management path is degraded

### Decision
**HOLD — no new entries.** Rationale: (1) Extreme Fear + elevated dominance + binary FOMC in ~1 week argue for standing aside; (2) account/balance API (700007) is down, so pre-trade balance gate can't be verified and the `close` exit path is broken — trading blind on a live account violates risk discipline. Re-run execution once F&G/dominance improve post-FOMC AND MEXC /account access is restored. Escalated.

## 2026-07-11 — Morning Research

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

## 2026-07-21 — Morning Research

### Account Snapshot
- **BLOCKED**: MEXC authenticated API returns `code 700007 "No permission to access the endpoint"` (HTTP 400) on `account`/`positions`/`orders`. Public endpoints (price, ticker, time, ping) all work fine, so it's not a geo-block — it's an API-key permission / IP-whitelist issue (key lacks Spot read/trade scope, or this run's egress IP isn't whitelisted on the MEXC key).
- Env vars ARE present (MEXC_API_KEY, MEXC_SECRET_KEY, MEXC_BASE_URL set). So it's the key's config on MEXC's side, not a missing secret.
- Last known state (TRADE-LOG Day 0 baseline): $10,000.00 USDT, 100% cash, 0 open positions. No trades ever executed.
- Trades this week: 0/15. Circuit breaker: NOT active (0 closed trades).

### Market Context
- BTC: ~$65,300–66,300 (+0.8% to +2.1% 24h) — rebounded off ~$64k support back above $65k; momentum weakening, volume declining
- ETH: ~$1,905–1,935 (+1.7% to +2.3% 24h)
- SOL: $78.37 (+1.6%) | BNB: $576 (+1.0%)
- BTC Dominance: 56.3% (firm; capital not decisively rotating to alts)
- Total crypto market cap: ~$2.28–2.31T
- Fear & Greed: **25 (Extreme Fear)** — deteriorating from 29 (Fear) yesterday
- DXY: strong-dollar backdrop persists (BTC/DXY correlation ~ -0.6 to -0.8 = headwind)
- Macro: FOMC **Jul 29** (Warsh) — held 3.50–3.75% in Jan & Mar, data-dependent, no urgency to cut. Geopolitical tensions weighing on risk assets (equities down 3rd straight session).
- Catalyst: CLARITY Act dispute easing (White House + Senate R's agreed on ethics provisions) — potential risk-appetite tailwind

### On-Chain / Derivatives
- BTC futures OI: $48.93B (stable, +3.9% 30d) — no leverage blow-off building
- Funding: neutral ~0.0043%/day (1.56% annualized); long/short 54/46 (1.18x) — not overcrowded, no contrarian signal
- ETF flows: short-term recovery (~$191M in over 2 days mid-July, +$273M recent) BUT structural headwind intact — YTD net **-$5.4B**, 30d **-$4.1B**. Institutions still net-reducing.

### News on Held Positions
- None — 0 open positions.

### Trade Ideas (WATCHLIST ONLY — execution blocked by API)
1. ADA — catalyst: first community-led hard fork completed today (+5.6%). Spot ADAUSDT. Wait for pullback/hold above breakout; entry on retest, stop -8%, target +10% cap. Sector: L1.
2. WLD — catalyst: Grayscale Worldcoin ETF filing (+4.75%). Momentum name; size small, stop -8%. Sector: AI/identity. Higher volatility risk.
3. SOL — L1 leader holding $78 above support; tokenized-stocks + prediction-market growth. Entry on strength above $79, stop ~$72 (-8%), target +10%. Sector: L1.
- Avoid the meme spikes (JIMOTHY +122%, PONS +72%) — outside strategy.

### Risk Factors
- **MEXC authenticated API blocked (700007) — highest-priority operational risk.** No account visibility, no order placement, no stop management. Same class of blocker as the prior Binance 451; migration didn't fix execution.
- Extreme Fear (25) + weakening BTC momentum + declining volume + risk-off geopolitics = poor entry environment
- Structural ETF outflows (-$5.4B YTD) and firm DXY — macro headwinds intact
- FOMC Jul 29 event risk approaching

### Decision
**HOLD — no entries.** Two independent reasons: (1) mandatory — MEXC authenticated API unreachable (700007), cannot verify state or place/manage orders; (2) even if live, Extreme Fear + fading momentum + risk-off macro offer no strong edge. Watchlist (ADA/WLD/SOL) parked pending API fix. Operational blocker escalated.
