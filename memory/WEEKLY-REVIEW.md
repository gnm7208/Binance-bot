# Weekly Review

Friday/Sunday reviews appended below.

---

<!-- Format for each entry:

## Week ending YYYY-MM-DD

### Stats
| Metric              | Value  |
|---------------------|--------|
| Starting portfolio  | $X     |
| Ending portfolio    | $X     |
| Week return         | ±$X (±X%) |
| BTC week return     | ±X%    |
| Bot vs BTC          | ±X%    |
| Trades              | N (W:X / L:Y / open:Z) |
| Win rate            | X%     |
| Best trade          | SYM +X% |
| Worst trade         | SYM -X% |
| Profit factor       | X.XX   |

### Closed Trades
| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|

### Open Positions at Week End
| Ticker | Entry | Price | Unrealized | Stop |
|--------|-------|-------|------------|------|

### What Worked
- ...

### What Didn't Work
- ...

### Key Lessons
- ...

### Adjustments for Next Week
- ...

### Overall Grade: X
-->

## Week ending 2026-07-19 (Week 1)

### Stats
| Metric              | Value  |
|---------------------|--------|
| Starting portfolio  | $10,000 |
| Ending portfolio    | $10,000 (last known — UNVERIFIED, API geo-blocked) |
| Week return         | $0 (0%) |
| BTC week return     | ~+0.9% (~$63,800 → ~$64,376) |
| Bot vs BTC          | −0.9% |
| Trades              | 0 (W:0 / L:0 / open:0) |
| Win rate            | N/A (no closed trades) |
| Best trade          | N/A |
| Worst trade         | N/A |
| Profit factor       | N/A |

### Closed Trades
None. No orders placed all week.

### Open Positions at Week End
None (last known: 100% USDT cash).

### What Worked
- Nothing to credit — the strategy was never exercised. Cash preservation is not a decision when no trade was possible.

### What Didn't Work
- **Exchange connectivity blocked the entire week — the bot has never traded.**
  - 2026-07-11: Binance API returned HTTP 451 (geo-restricted location).
  - Repo migrated Binance → Bybit Spot to resolve it (commits `b3138f8`, `8edc1c4`).
  - 2026-07-19: Bybit (`api.bytick.com` / `api.bybit.com`) returns HTTP 403 — CloudFront body: *"configured to block access from your country."* Same geo-block class, different exchange. Public market endpoints (`/v5/market/tickers`, `/v5/market/time`) also 403, so it is not a signing/auth issue.
- The migration did not fix the root cause: this execution environment's egress IP is geo-blocked by major exchange CDNs. Swapping exchanges without confirming reachability burned a week.

### Key Lessons
- Confirm the exchange API is actually reachable from the routine's egress **before** any trading logic matters. A reachability smoke test (`bybit.sh price BTCUSDT`) should gate every run and hard-fail loudly.
- Migrating exchanges to dodge a geo-block only helps if the new exchange isn't blocked from the same IP. Bybit and Binance are both blocked here.

### Adjustments for Next Week
- **Unblock connectivity is the only priority.** Options: (a) an exchange whose CDN is not geo-blocked from this environment (e.g. Kraken/Coinbase — verify reachability first), (b) a routing/egress change so exchange APIs are reachable, or (c) confirm whether the intended venue is US-accessible at all. No trading rule change will matter until quotes/orders resolve.
- Until then the bot is dark: 0 trades, 0 P&L, losing ground to BTC by whatever BTC does each week.

### Overall Grade: F
Zero trades executed in Week 1 of the challenge. The mission (beat BTC) was not pursued at all because the account/market API is unreachable, and the mid-week exchange migration did not restore access. Full week of the challenge window lost.
