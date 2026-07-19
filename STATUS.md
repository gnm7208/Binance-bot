# Trading Bot — Current Status

## What Is Built

An autonomous crypto trading bot where **Claude IS the bot**. Five scheduled Claude Code
cloud routines fire throughout the day, read git-committed markdown memory, make decisions,
place real trades on Bybit Spot, and write memory back to the repo. No persistent Python process.

Repo: `github.com/gnm7208/Binance-bot` | Branch: `main`

---

### Files Implemented

| File | Status | Purpose |
|---|---|---|
| `CLAUDE.md` | Done | Auto-loaded rulebook — hard rules, schedule, API usage |
| `env.template` | Done | Credential template for local `.env` setup |
| `scripts/bybit.sh` | Done | Bybit Spot API wrapper with HMAC-SHA256 (X-BAPI-* headers) |
| `scripts/perplexity.sh` | Done | Research wrapper — exits code 3 if key unset (WebSearch fallback) |
| `scripts/clickup.sh` | Done | ClickUp Chat v3 notifications — falls back to NOTIFICATIONS.md |
| `memory/TRADING-STRATEGY.md` | Done | Bot rulebook — Bybit order shapes, rules, entry checklist |
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
- Original: Binance — blocked with HTTP 451 geo-restriction from cloud provider IPs (Jul 11-Jul 19)
- Migrated to: Bybit — same HMAC-SHA256 auth, same spot features, no cloud IP blocks
- Migration date: 2026-07-19
- Bybit API key: Read-Write + SPOT Trade only, No IP restriction (tighten after first run)

---

## Trading Strategy Summary

- Exchange: Bybit Spot
- Spot only — no margin, futures, leverage ever
- Max 5-6 open positions; 20% of portfolio per position (~$2,000 on $10k)
- Hold 15-25% USDT as dry powder
- Every position gets a stop-limit GTC immediately after fill
- Cut losers at -7%; tighten stop at +15% and +20%
- Max 3 new trades per week
- Benchmark: outperform BTC buy-and-hold
- Current state: $10,000 USDT, 0 positions, 0 trades — idle since launch due to API blocks now resolved
