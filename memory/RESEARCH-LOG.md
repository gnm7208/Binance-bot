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
