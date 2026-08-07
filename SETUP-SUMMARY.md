# MEXC Trading Bot — Setup Summary

## What This Is

An autonomous crypto trading bot where **Claude IS the bot**. Seven scheduled Claude Code
cloud routines fire throughout the day, read trading strategy and memory from GitHub, make
decisions, place real trades on **MEXC Spot**, and write memory back to the repo.
No persistent Python process. Based on the Nate Herk YouTube architecture, adapted for
MEXC crypto spot trading.

Repo: [github.com/gnm7208/MEXC-bot](https://github.com/gnm7208/MEXC-bot) | Branch: `main`

---

## Exchange History

The bot went through two exchange migrations before landing on MEXC:

| Phase | Exchange | Dates | Outcome |
|---|---|---|---|
| Initial scaffold | Alpaca (stocks) | Jul 2026 | Replaced with crypto bot |
| Attempt 1 | Binance | Jul 11–19 | HTTP 451 geo-block from cloud IPs |
| Attempt 2 | Bybit | Jul 19–21 | CloudFront 403 block same as Binance |
| **Current** | **MEXC Spot** | **Jul 21 → present** | **No cloud IP blocking, 0% maker fees** |

Legacy scripts `scripts/binance.sh` and `scripts/bybit.sh` remain in the repo for
reference. Active API wrapper is `scripts/mexc.sh`.

---

## Files

| File / Folder | Purpose |
|---|---|
| `scripts/mexc.sh` | **MEXC Spot API wrapper** — HMAC-SHA256 signing, X-MEXC-APIKEY header |
| `scripts/perplexity.sh` | Research queries via Perplexity API — exits code 3 if key unset (WebSearch fallback) |
| `scripts/clickup.sh` | ClickUp Chat v3 notifications — falls back to NOTIFICATIONS.md |
| `scripts/binance.sh` | Legacy — Binance wrapper (unused, kept for reference) |
| `scripts/bybit.sh` | Legacy — Bybit wrapper (unused, kept for reference) |
| `memory/TRADING-STRATEGY.md` | Bot rulebook — MEXC order shapes, 3-layer architecture, all rules |
| `memory/TRADE-LOG.md` | Every trade entry/exit + daily EOD snapshots |
| `memory/RESEARCH-LOG.md` | Daily morning research entries |
| `memory/WEEKLY-REVIEW.md` | Friday/Sunday grading and lessons |
| `memory/PROJECT-CONTEXT.md` | Architecture overview, schedule, rules |
| `routines/morning-research.md` | Cloud routine — 6:00 AM CT daily |
| `routines/morning-execution.md` | Cloud routine — 9:00 AM CT daily |
| `routines/midday.md` | Cloud routine — 2:00 PM CT daily |
| `routines/afternoon-execution.md` | Cloud routine — 4:00 PM CT daily |
| `routines/daily-summary.md` | Cloud routine — 6:00 PM CT daily |
| `routines/evening-scan.md` | Cloud routine — 10:00 PM CT daily |
| `routines/overnight-monitor.md` | Cloud routine — 3:00 AM CT daily (emergency stops only) |
| `routines/weekly-review.md` | Cloud routine — 6:00 PM CT Sunday |
| `.claude/commands/` | Local slash commands for manual testing |
| `CLAUDE.md` | Auto-loaded rulebook every Claude Code session |
| `env.template` | Credential template — copy to `.env` locally |

---

## Current Trading Strategy (Aggressive Mode Aug 4–22)

- **Exchange: MEXC Spot** — no margin, futures, leverage ever
- Max 3 open positions; 30-35% of portfolio per position
- Hold 10-20% USDT as dry powder; target 80-90% deployed
- Stops monitored manually every scan (MEXC spot API has no resting stop-limit orders)
- Cut losers at -7%; trailing stop to 7% below current at +4% gain
- Take profit at +12%
- Max 20 new trades per week; max 5 per day
- Benchmark: outperform BTC buy-and-hold

---

## Daily Schedule (Central Time)

| Time | Routine | What It Does |
|---|---|---|
| 6:00 AM | morning-research | Macro gate, signal scan, trade ideas → RESEARCH-LOG |
| 9:00 AM | morning-execution | Validate + execute planned trades |
| 2:00 PM | midday | Cut losers, tighten stops, near-stop alerts |
| 4:00 PM | afternoon-execution | US market open momentum sweep |
| 6:00 PM | daily-summary | EOD snapshot, always notifies ClickUp |
| 10:00 PM | evening-scan | Asian open, overnight catalysts |
| 3:00 AM | overnight-monitor | Emergency stop enforcement only |
| 6:00 PM Sun | weekly-review | Full week stats, grade, strategy update |

---

## Environment Variables

Set in `.env` locally and in each cloud routine's settings panel:

```
MEXC_API_KEY         = (from mexc.com/user/openapi — Read + Spot Trade)
MEXC_SECRET_KEY      = (shown once at creation)
MEXC_BASE_URL        = https://api.mexc.com
PERPLEXITY_API_KEY   = (optional — exits code 3 if unset, WebSearch fallback kicks in)
PERPLEXITY_MODEL     = sonar
CLICKUP_API_KEY      = (from ClickUp Settings → Apps)
CLICKUP_WORKSPACE_ID = (the number in your ClickUp URL)
CLICKUP_CHANNEL_ID   = (4-XXXXXXX-X format from chat channel URL)
```

---

## Key Facts

- **MEXC_BASE_URL is always** `https://api.mexc.com`
- **Secret Key is only shown once** — if you didn't copy it, delete and recreate the API key
- **Never commit `.env`** — it's in `.gitignore`; cloud routines get credentials from the routine UI env vars
- **Git is the bot's memory** — if a cloud run doesn't commit and push, nothing is saved
- **MEXC spot has no stop-limit orders** — stops are enforced by comparing live price to the stop recorded in TRADE-LOG at every midday and afternoon scan
