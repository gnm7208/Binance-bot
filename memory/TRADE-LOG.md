# Trade Log

## Day 0 — EOD Snapshot (pre-launch baseline)

**Portfolio:** $10,000.00 USDT | **Cash:** $10,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0

No positions. Bot launching tomorrow. Starting capital confirmed in Binance account.

---

## Jul 09 — EOD Note (no snapshot — Binance API unreachable)

Binance API returned HTTP 451 "restricted location" on every endpoint, including
unauthenticated `/api/v3/ping` — this session's egress IP is geo-blocked by Binance,
not a proxy/credential issue. Could not pull account/positions/orders, so no EOD
P&L snapshot was computed (avoiding fabricated numbers). Day 0 baseline above still
stands for tomorrow's day P&L calc. ClickUp alert sent. No trades attempted.

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
