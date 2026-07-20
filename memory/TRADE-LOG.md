# Trade Log

## Day 0 — EOD Snapshot (pre-launch baseline)

**Portfolio:** $10,000.00 USDT | **Cash:** $10,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0

No positions. Bot launching tomorrow. Starting capital confirmed in Binance account.

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

## Jul 20 — EOD Snapshot (Monday) — DATA UNAVAILABLE (exchange geo-blocked)

**Portfolio:** $10,000.00 (last known) | **Cash:** $10,000.00 (100%) | **Day P&L:** $0 (0%) | **Phase P&L:** $0 (0%)

| Ticker | Qty | Entry | Price | Day Chg | Unrealized P&L | Stop |
|--------|-----|-------|-------|---------|----------------|------|
| —      | —   | —     | —     | —       | —              | —    |

**Trades today:** none | **Trades this week:** 0/3

**Notes:** Could not pull live account state — Bybit API is geo-blocked from the cloud
environment. `api.bybit.com` and `api.bytick.com` both return HTTP 403 (Amazon CloudFront
"configured to block access from your country"). Env vars (BYBIT_API_KEY, BYBIT_SECRET_KEY,
BYBIT_BASE_URL, ClickUp keys) are all present and correct — this is a network/geo block, not a
credential issue. This is the **same class of outage that blocked Binance (451)**; the Bybit
migration did not resolve it. No account visibility, no order placement/cancellation, no stop
management possible. Bot has still never executed a live trade. Values above carry forward the
Day 0 baseline unchanged. **Operational escalation required: exchange API is unreachable from
this environment — needs a non-geo-blocked egress/region or a different exchange before the bot
can function.**
