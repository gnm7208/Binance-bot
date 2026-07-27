# Trade Log

## Day 0 — EOD Snapshot (pre-launch baseline)

**Portfolio:** $32.32 USDT | **Cash:** $32.32 (100%) | **Day P&L:** $0 | **Phase P&L:** $0

No positions. Starting capital: 4,500 KES → 34.32 USDT via Remitano M-Pesa P2P, 2 USDT withdrawal fee, net 32.32 USDT deposited to MEXC on 2026-07-22.

---

## Jul 23 — EOD Snapshot (Day 1, Thursday)

**Portfolio:** $32.32 | **Cash:** $32.32 (100%) | **Day P&L:** $0 (0.00%) | **Phase P&L:** $0 (0.00%)

| Ticker | Qty | Entry | Price | Day Chg | Unrealized P&L | Stop |
|--------|-----|-------|-------|---------|----------------|------|
| — | — | — | — | — | — | — |

**Notes:** No positions. 0 trades today, 0 this week. 100% cash — deployment (75-85%) still pending first entry. No morning-research/execution entries logged today. BTC ref $64,824.93. Account live on MEXC Spot (canTrade=true), USDT free $32.32 / locked $0. No open orders.

---

<!-- New entries appended below. Format:

## YYYY-MM-DD — Trade Entry
**BUY** SYMBOL | Shares: X | Entry: $X.XX | Stop: $X.XX (X%) | Target: $X.XX (X:1 R:R)
**Thesis:** ...
**Catalyst:** ...
**Sector:** ...

## YYYY-MM-DD — Trade Exit
**SELL** SYMBOL | Exit: $X.XX | Realized P&L: ±$X (±X%) | Reason: ...

## MMM DD — EOD Snapshot (Day N, Weekday)
**Portfolio:** $X | **Cash:** $X (X%) | **Day P&L:** ±$X (±X%) | **Phase P&L:** ±$X (±X%)
| Ticker | Qty | Entry | Price | Day Chg | Unrealized P&L | Stop |
|--------|-----|-------|-------|---------|----------------|------|
**Notes:** ...
-->

## Jul 24 — EOD Snapshot (Day 2, Friday)

**Portfolio:** $32.32 | **Cash:** $32.32 (100%) | **Day P&L:** $0.00 (0.0%) | **Phase P&L:** $0.00 (0.0%)

| Ticker | Qty | Entry | Price | Day Chg | Unrealized P&L | Stop |
|--------|-----|-------|-------|---------|----------------|------|
| — | — | — | — | — | — | — |

**Notes:** No positions; 100% cash at $32.32 baseline. No trades placed. MEXC Spot API confirmed reachable (`account`, `positions` OK; `orders` needs a symbol arg). BTC $64,063.8. 0/25 trades this week. Deployment 0% vs 75-85% target — still awaiting a qualifying setup (momentum ≥ +2% or confirmed catalyst) before first entry.

## 2026-07-25 — Trade Entry (afternoon)
**BUY** VVV | Qty: 0.45 | Entry: $13.1395 | Stop: intended $11.8255 (-10%) | Target: $14.06 (+7%)
Stop order ID: **NONE — could not be placed, see blocker below**
**Thesis:** First MEXC live-trade attempt. VVV printing +11.78% 24h (accelerated from +5.07% at intraday research refresh), on morning watchlist, preferred over extended BANK per research decision.
**Catalyst:** Venice Token reducing annual emissions 5M→3M VVV effective Jul 2026 (supply-side bullish); Jul 21 short-liquidation breakout out of month-long downtrend.
**Sector:** AI

## 2026-07-25 — Trade Exit (afternoon, immediate — operational halt)
**SELL** VVV | Exit: $13.0831 | Realized P&L: -$0.0254 (-0.43% of position, -0.08% of portfolio) | Reason: **Closed immediately — could not place mandatory stop-limit GTC order.**

**CRITICAL OPERATIONAL BLOCKER — MEXC Spot API does not support stop orders at all:**
- Placing `STOP_LOSS_LIMIT` on VVVUSDT returned `{"code":500,"msg":"invalid type"}`.
- Confirmed via `exchangeInfo`: `orderTypes` for VVVUSDT, BANKUSDT, ZROUSDT, and **BTCUSDT** (the CLAUDE.md example symbol itself) are all `["LIMIT","MARKET","LIMIT_MAKER"]` — no stop type listed for any pair tested.
- Tried alternate type names (`STOP_LIMIT`, `STOP`, `LIMIT_STOP`, `TAKE_PROFIT_STOP_LIMIT`) — all rejected. This is an exchange/API-wide limitation, not a symbol-specific or wrapper-syntax issue.
- Strategy rule 4/CLAUDE.md hard rule ("every position gets a stop-limit GTC order immediately after fill — no exceptions") is currently **impossible to satisfy** on MEXC Spot via this API.
- Per "no exceptions," the only compliant action on discovering this mid-trade was to immediately market-sell the unprotected position rather than hold it uncovered.
- **Also fixed in this run:** `scripts/mexc.sh` `_auth_post()` had a separate bug (sent signed params as a form-urlencoded POST body → MEXC returned `{"code":700013,"msg":"Invalid content Type."}` on every order/cancel call). Fixed to send params in the query string (matching `_auth_get`/`_auth_delete` pattern) — market buy/sell now work. This fix is unrelated to the stop-order blocker above, which remains open.
- **HALTING new entries** for the rest of this session and until the stop-order gate is resolved (need to confirm correct MEXC stop-order mechanism — may require a different endpoint, e.g. OCO or a algo-order API, or MEXC Spot may not offer stop orders via API at all and only via UI). ClickUp alert sent.
