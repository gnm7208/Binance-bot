# Trading Bot — Current Status

## What Is Built

### Core Architecture
The bot follows the Nate Herk cloud-routines pattern: **Claude IS the bot**.
Five cron-scheduled Claude Code cloud routines fire throughout the day, read
git-committed markdown memory, call bash wrapper scripts to interact with Binance,
make decisions, and write memory back to the repo. No persistent Python process.

Repo: `github.com/gnm7208/Binance-bot` | Branch: `main`

---

### Files Implemented

| File | Status | Purpose |
|---|---|---|
| `CLAUDE.md` | ✅ Done | Auto-loaded rulebook — hard rules, schedule, API usage |
| `env.template` | ✅ Done | Credential template for local `.env` setup |
| `.gitignore` | ✅ Done | Excludes `.env`, `NOTIFICATIONS.md`, `.venv/` |
| `scripts/binance.sh` | ✅ Done | Full Binance Spot API wrapper with HMAC-SHA256 signing |
| `scripts/perplexity.sh` | ✅ Done | Research wrapper — exits code 3 if key unset (triggers WebSearch fallback) |
| `scripts/clickup.sh` | ✅ Done | ClickUp Chat v3 notifications — falls back to `NOTIFICATIONS.md` |
| `memory/TRADING-STRATEGY.md` | ✅ Done | Bot rulebook — seeded, ready to evolve |
| `memory/TRADE-LOG.md` | ✅ Done | Trade journal — seeded with $10k USDT baseline |
| `memory/RESEARCH-LOG.md` | ✅ Done | Daily research log — first live entry written by bot on 2026-07-03 |
| `memory/WEEKLY-REVIEW.md` | ✅ Done | Weekly review template |
| `memory/PROJECT-CONTEXT.md` | ✅ Done | Architecture overview and schedule reference |
| `routines/morning-research.md` | ✅ Done | Cloud routine prompt — 6:00 AM CT daily |
| `routines/morning-execution.md` | ✅ Done | Cloud routine prompt — 9:00 AM CT daily |
| `routines/midday.md` | ✅ Done | Cloud routine prompt — 2:00 PM CT daily |
| `routines/daily-summary.md` | ✅ Done | Cloud routine prompt — 6:00 PM CT daily |
| `routines/weekly-review.md` | ✅ Done | Cloud routine prompt — 6:00 PM CT Sunday |
| `.claude/commands/portfolio.md` | ✅ Done | Local slash command — read-only account snapshot |
| `.claude/commands/trade.md` | ✅ Done | Local slash command — manual trade with rule validation |
| `.claude/commands/morning-research.md` | ✅ Done | Local slash command — manual research run |
| `.claude/commands/morning-execution.md` | ✅ Done | Local slash command — manual execution run |
| `.claude/commands/midday.md` | ✅ Done | Local slash command — manual midday scan |
| `.claude/commands/daily-summary.md` | ✅ Done | Local slash command — manual daily summary |
| `.claude/commands/weekly-review.md` | ✅ Done | Local slash command — manual weekly review |
| `.github/workflows/merge-bot-branch.yml` | ✅ Done | Auto-merges `claude/*` bot branches into `main` |

---

### Cloud Routines Created (claude.ai/code)

| Routine | Schedule | Status |
|---|---|---|
| Trading bot - morning research | 6:00 AM daily | ✅ Created — ran successfully on 2026-07-03 |
| Trading bot - morning execution | 9:00 AM daily | ✅ Created |
| Trading bot - midday scan | 2:00 PM daily | ✅ Created |
| Trading bot - daily summary | 6:00 PM daily | ✅ Created |
| Trading bot - weekly review | 6:00 PM Sunday | ✅ Created — needs cron fix (currently 11:45 PM) |

---

### First Live Run Results (2026-07-03)
- Research completed via WebSearch fallback (Perplexity key not set — expected)
- `memory/RESEARCH-LOG.md` written with market data
- Commit pushed to `claude/inspiring-faraday-o9z2cb` (not `main` — branch push blocker, now fixed via GitHub Action)
- Binance API returned 403 — network policy blocked external calls
- ClickUp 403 — same network policy issue
- Decision: HOLD (macro bearish + infra not yet unblocked)

---

## Trading Strategy Summary

- **Spot only** — no margin, futures, leverage ever
- Max 5-6 open positions; 20% of portfolio per position (~$2,000 on $10k)
- Hold 15-25% USDT as dry powder
- Every position gets a **stop-limit GTC at 10% below entry** immediately after fill
- Cut losers at **-7%**; tighten stop at **+15%** and **+20%**
- Max **3 new trades per week**
- Follow sector momentum; exit sector after 2 consecutive losses
- Benchmark: outperform BTC buy-and-hold
