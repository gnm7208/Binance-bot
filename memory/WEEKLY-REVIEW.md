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

---

## Week ending 2026-07-26 (Week 2)

### Stats
| Metric              | Value  |
|---------------------|--------|
| Starting portfolio  | $32.32 (real MEXC account, funded 2026-07-22; Week 1's $10,000 was a stale pre-funding placeholder) |
| Ending portfolio    | $32.29 |
| Week return         | $0.00 (0.0%) — the $0.03 delta is display rounding, no trades |
| BTC week return     | ~+0.4% (~$64,376 on 07-19 close → $64,661 on 07-26) |
| Bot vs BTC          | −0.4% |
| Trades              | 0 (W:0 / L:0 / open:0) |
| Win rate            | N/A (no closed trades) |
| Best trade          | N/A |
| Worst trade         | N/A |
| Profit factor       | N/A |

### Closed Trades
None. No orders placed all week.

### Open Positions at Week End
None — 100% USDT cash ($32.29 free, 0 locked). Reachability gate PASS (MEXC `account`/`price`/`positions` all healthy).

### What Worked
- **Operational blocker resolved.** The Binance/Bybit geo-block that killed Week 1 is gone — the account now runs on MEXC Spot and the API is live and healthy every run (`canTrade=true`). This is the single biggest improvement over Week 1: the bot *can* trade now.
- **Discipline into a binary event.** Sat 100% cash ahead of FOMC (Jul 28–29, live ~33% hike tail) rather than getting caught in size before a coin-flip macro print on a $32 account. Defensible risk control.
- **Momentum gate did its job** on most sessions — majors (BTC/ETH/SOL) were flat-to-red and failed the +2% filter, correctly blocking low-quality entries.

### What Didn't Work
- **Second straight zero-trade week.** The mandate is "disciplined AND active" and to beat BTC; 0 trades = 0 pursuit of the mission. BTC rose ~0.4% while we held cash, so we lost ground again (small, but the direction is the point).
- **Declined valid gate-passing setups.** On 07-25, BANK (+28.66%), VVV (+5.07%) and ZRO (+5.00%) all passed the +2% momentum gate. All were declined on FOMC caution. Reasonable once — but the pattern of finding qualifying signals and taking none needs to break after FOMC clears.
- **Tiny-capital friction.** At $32.29, the 20% cap ≈ $6.46/position; MEXC min-notional plus fee/slippage is a heavier % drag than normal. Real, but not a reason to stay flat — it argues for a small number of higher-conviction entries, not zero.

### Key Lessons
- Capability is restored; the constraint is now *decision-making*, not connectivity. Week 1's excuse (API dark) no longer applies — inactivity from here is a choice, and it must be justified per-session, not defaulted to.
- Holding cash into a genuine binary macro event (FOMC) is fine. Holding cash *after* it clears, when gate-passing setups exist, is not.

### Adjustments for Next Week
- **Post-FOMC (after Jul 29): resume active deployment.** Once the FOMC print is out and digested, take the best gate-passing setup(s) — target 75–85% deployed per strategy — rather than defaulting to HOLD. First look: relative-strength names that held up pre-FOMC (BANK/VVV/ZRO) if still in momentum.
- Fixed a stale operational note in TRADING-STRATEGY.md: the reachability gate still referenced `scripts/bybit.sh` though the bot migrated to MEXC — corrected to `scripts/mexc.sh price BTCUSDT`.
- No hard trading-rule change warranted this week — the strategy behaved as designed (gate caution into a binary event). The gap is execution follow-through, not the rulebook.

### Overall Grade: D
Up from Week 1's F because the operational blocker is resolved and the account is genuinely trade-ready, and holding cash into a live-tail FOMC on a $32 account is defensible. But it is still a zero-trade week that trailed BTC by ~0.4%, with gate-passing setups declined. Two straight weeks of no trades in an "aggressive, active" mandate keeps the grade low; the bar for next week is clear — deploy after FOMC.
