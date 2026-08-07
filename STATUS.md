# Trading Bot — Current Status

## What Is Built

An autonomous crypto trading bot where **Claude IS the bot**. Seven scheduled Claude Code
cloud routines fire throughout the day, read git-committed markdown memory, make decisions,
place real trades on **MEXC Spot**, and write memory back to the repo. No persistent Python process.

Repo: `github.com/gnm7208/MEXC-bot` | Branch: `main`

---

### Files Implemented

| File | Status | Purpose |
|---|---|---|
| `CLAUDE.md` | Done | Auto-loaded rulebook — hard rules, schedule, API usage |
| `env.template` | Done | Credential template for local `.env` setup |
| `scripts/bybit.sh` | Kept (unused) | Bybit Spot API wrapper — superseded by mexc.sh |
| `scripts/mexc.sh` | Done | MEXC Spot API wrapper with HMAC-SHA256 (X-MEXC-APIKEY header) |
| `scripts/perplexity.sh` | Done | Research wrapper — exits code 3 if key unset (WebSearch fallback) |
| `scripts/clickup.sh` | Done | ClickUp Chat v3 notifications — falls back to NOTIFICATIONS.md |
| `memory/TRADING-STRATEGY.md` | Done | Bot rulebook — MEXC order shapes, rules, entry checklist |
| `memory/TRADE-LOG.md` | Done | Trade journal — seeded with $10k USDT baseline |
| `memory/RESEARCH-LOG.md` | Done | Daily research log — running since 2026-07-03 |
| `memory/WEEKLY-REVIEW.md` | Done | Weekly review template |
| `memory/PROJECT-CONTEXT.md` | Done | Architecture overview and schedule reference |
| `routines/morning-research.md` | Done | Cloud routine prompt — 6:00 AM CT daily |
| `routines/morning-execution.md` | Done | Cloud routine prompt — 9:00 AM CT daily |
| `routines/midday.md` | Done | Cloud routine prompt — 2:00 PM CT daily |
| `routines/daily-summary.md` | Done | Cloud routine prompt — 6:00 PM CT daily |
| `routines/weekly-review.md` | Done | Cloud routine prompt — 6:00 PM CT Sunday |
| `.claude/commands/` | Done | 7 local slash commands for manual testing |
| `.github/workflows/merge-bot-branch.yml` | Done | Auto-merges claude/* bot branches into main |

---

### Cloud Routines (claude.ai/code)

| Routine | Schedule | Status |
|---|---|---|
| Trading bot - morning research | 6:00 AM daily | Running — 16+ consecutive successful runs |
| Trading bot - morning execution | 9:00 AM daily | Created |
| Trading bot - midday scan | 2:00 PM daily | Created |
| Trading bot - daily summary | 6:00 PM daily | Created |
| Trading bot - weekly review | 6:00 PM Sunday | Cron wrong — fix to 0 18 * * 0 |

---

### Exchange Migration History
- Original: Binance — blocked HTTP 451 from cloud provider IPs (Jul 11-19)
- Migrated to: Bybit (Jul 19) — also blocked, CloudFront 403 same as Binance
- Migrated to: MEXC (Jul 21) — no cloud IP blocking, 0% maker fees
- MEXC API key: create at mexc.com/user/openapi, Spot Trade only

---

## Trading Strategy Summary

- Exchange: **MEXC Spot** (0% maker fees, no cloud IP blocking)
- Spot only — no margin, futures, leverage ever
- Max 3 open positions; 30-35% of portfolio per position (aggressive mode Aug 4-22)
- Hold 10-20% USDT as dry powder
- Stops enforced manually (MEXC spot API has no stop-limit orders) — monitored every scan
- Cut losers at -7%; trailing stop tightens to 7% below current at +4% gain
- Take profit at +12%; no exceptions
- Max 20 new trades per week; max 5 per day
- Benchmark: outperform BTC buy-and-hold
- Current state: $33.58 USDT | 2W/0L phase record | +3.91% vs ~+1.9% BTC
