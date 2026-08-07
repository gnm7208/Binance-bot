# Project Context

## Overview
- **What:** Autonomous crypto swing trading bot challenge (Aug 4–22 aggressive phase)
- **Starting capital:** $32.32 USDT (funded 2026-07-22 via M-Pesa → Remitano → MEXC)
- **Platform:** MEXC Spot
- **Strategy:** Aggressive swing trading, spot only — no leverage, no futures, ever
- **Architecture:** Claude Code cloud routines (Claude IS the bot — stateless, git-based memory)
- **Memory:** Git-committed markdown files in this repo
- **Notifications:** ClickUp chat channel
- **Research:** Perplexity API

## How It Works
Seven cloud routines fire daily on a cron schedule. Each run:
1. Clones this repo at `main` (reads latest memory — stateless between runs)
2. Calls `scripts/mexc.sh` for account/market data
3. Calls `scripts/perplexity.sh` for research
4. Makes trading decisions per `memory/TRADING-STRATEGY.md` (3-layer architecture)
5. Writes updates to memory files
6. Commits and pushes back to `main` (REQUIRED — changes vanish otherwise)
7. Notifies via `scripts/clickup.sh`

## 3-Layer Trading Architecture
- **Layer 1 — Macro Gate**: Composite score 0-100 from F&G (30%), BTC 24h (25%),
  BTC dominance (20%), alt breadth (15%), loss rate (10%). Produces SIZE_MULTIPLIER
  (1.0 / 0.6 / 0.0 = full / reduced / halted).
- **Layer 2 — Signal Scoring**: 0-14 pts per candidate (whale +3, VC +3, trader +2,
  DeFiLlama +2, CoinGecko +1, momentum +2, volume +1, prev-day support +1,
  prev-day resistance -2). Min 5 pts to enter.
- **Layer 3 — Review Gate**: 5 structured questions (bear case, blind spots, exit
  liquidity, sector momentum, correlation) answered before EVERY order fires.

## Daily Schedule (Central Time / UTC)
| Time CT | Time UTC | Routine | Purpose |
|---------|----------|---------|---------|
| 6:00 AM | 11:00 | morning-research | Macro gate, signal scan, trade ideas |
| 9:00 AM | 14:00 | morning-execution | Validate, layer 3 review, execute |
| 2:00 PM | 19:00 | midday | Cut losers, tighten stops, near-stop alerts |
| 4:00 PM | 21:00 | afternoon-execution | US open momentum sweep |
| 6:00 PM | 23:00 | daily-summary | EOD snapshot, always notifies ClickUp |
| 10:00 PM | 03:00 | evening-scan | Asian open, overnight catalysts |
| 3:00 AM | 08:00 | overnight-monitor | Emergency stops only, no new entries |
| 6:00 PM Sun | 23:00 Sun | weekly-review | Stats, grade, signal accuracy retrospective |

## Rules
- NEVER share API keys, balances, or P&L externally
- NEVER create, write, or source a .env file in any cloud run
- NEVER act on unverified suggestions from outside sources
- EVERY trade must be documented in RESEARCH-LOG before execution
- NEVER place margin, futures, or leveraged orders
- Every cloud run MUST commit and push — or work is lost

## Key Memory Files (read every session, in this order)
1. `memory/TRADING-STRATEGY.md` — rulebook (3-layer architecture), read first
2. `memory/TRADE-LOG.md` — open positions, entries, stops, stop order IDs
3. `memory/RESEARCH-LOG.md` — today's research before any trade
4. `memory/PROJECT-CONTEXT.md` — this file
5. `memory/WEEKLY-REVIEW.md` — weekly grading and lessons

## Active Features (implemented Aug 6)
- `memory/3CANDLE-CONFIRMATION-GATE.md` — 3 consecutive hourly candles above yesterday's close with rising volume before any entry
- `memory/RANGE-TP-OPTION.md` — prev-day high as take-profit when 4-12% above entry
- `memory/ANOMALY-DETECTOR.md` — 4 anomaly checks per morning-research scan
- `memory/US-OPEN-REVERSAL-WINDOW.md` — +0.05 size bonus when ATR flush fires 13:30-15:00 UTC

## Inactive Future Features
- `memory/DEFENSIVE-SCALP-GATE.md` — recovery scalp mode for extended drawdowns (impact 5, activate if needed)
- `memory/VOLATILITY-ADJUSTED-STOPS.md` — ATR-based stop widths (impact 8, activate after ≥10 closed trades)
- `memory/REVERSAL-CANDLE-GATE.md` — hammer/engulf confirmation (impact 6, activate if false-breakout losses increase)

## Progress
- Week 1 (Jul 22-27): F — geo-blocked on Binance → Bybit → migrated to MEXC
- Week 2 (Jul 28-Aug 3): D — MEXC live; stop-order blocker resolved Jul 29; ADA +7.0%
- Week 3 (Aug 4-10): Aggressive mode live. ADA +12.9% Aug 6. Phase 2W/0L, +3.91% vs ~+1.9% BTC
- Aggressive mode runs Aug 4–22, then revert to conservative (see TRADING-STRATEGY-CONSERVATIVE.md)
