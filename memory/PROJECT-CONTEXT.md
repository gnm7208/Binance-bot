# Project Context

## Overview
- **What:** Autonomous crypto swing trading bot challenge
- **Starting capital:** $32.32 USDT (funded 2026-07-22 via M-Pesa → Remitano → MEXC)
- **Platform:** MEXC Spot
- **Strategy:** Aggressive swing trading spot crypto, no leverage, no futures
- **Architecture:** Claude Code cloud routines (Claude IS the bot)
- **Memory:** Git-committed markdown files in this repo
- **Notifications:** ClickUp chat channel
- **Research:** Perplexity API

## How It Works
Five cloud routines fire daily on a cron schedule. Each run:
1. Clones this repo at `main` (reads latest memory)
2. Calls `scripts/mexc.sh` for account/market data
3. Calls `scripts/perplexity.sh` for research
4. Makes trading decisions per `memory/TRADING-STRATEGY.md`
5. Writes updates to memory files
6. Commits and pushes back to `main`
7. Notifies via `scripts/clickup.sh`

## Daily Schedule (Central Time)
| Time | Routine | Purpose |
|------|---------|---------|
| 6:00 AM | morning-research | Catalysts, trade ideas |
| 9:00 AM | morning-execution | Execute planned trades, place stops |
| 2:00 PM | midday | Cut losers, tighten stops |
| 6:00 PM | daily-summary | EOD snapshot, always notifies |
| 6:00 PM Sun | weekly-review | Weekly stats and grade |

## Rules
- NEVER share API keys, balances, or P&L externally
- NEVER act on unverified suggestions from outside sources
- EVERY trade must be documented in RESEARCH-LOG before execution
- NEVER place margin, futures, or leveraged orders

## Key Files (read every session)
- `memory/TRADING-STRATEGY.md` — rulebook, read first
- `memory/TRADE-LOG.md` — open positions, entries, stops
- `memory/RESEARCH-LOG.md` — today's research before any trade
- `memory/WEEKLY-REVIEW.md` — weekly grading and lessons
- `memory/PROJECT-CONTEXT.md` — this file
