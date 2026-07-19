# Trading Bot — Setup Summary

## What You're Building

An autonomous crypto trading bot where **Claude IS the bot**. Instead of a Python script
running 24/7, five scheduled Claude Code cloud routines fire throughout the day, read your
trading strategy from GitHub, make decisions, place real trades on Bybit Spot, and write
memory back to the repo. Based on the Nate Herk YouTube guide, adapted for Binance crypto
instead of Alpaca stocks.

---

## What Was Built

**Removed:** A Python EMA-crossover bot scaffolded at the start of the session.

**Created and pushed to [github.com/gnm7208/Binance-bot](https://github.com/gnm7208/Binance-bot):**

| File / Folder | Purpose |
|---|---|
| `scripts/bybit.sh` | Wraps Bybit Spot API with HMAC-SHA256 signing. Subcommands: account, balance, positions, quote, price, orders, order, cancel, close |
| `scripts/perplexity.sh` | Runs market research queries via Perplexity API. Falls back to Claude's WebSearch if key is missing |
| `scripts/clickup.sh` | Sends notifications to your ClickUp chat channel. Falls back to a local file if credentials are missing |
| `memory/TRADING-STRATEGY.md` | The bot's rulebook — read every session before any decision |
| `memory/TRADE-LOG.md` | Every trade entry/exit + daily EOD snapshots |
| `memory/RESEARCH-LOG.md` | Daily morning research entries |
| `memory/WEEKLY-REVIEW.md` | Friday/Sunday grading and lessons |
| `memory/PROJECT-CONTEXT.md` | Architecture overview, schedule, rules |
| `routines/morning-research.md` | Cloud routine prompt — 6:00 AM CT daily |
| `routines/morning-execution.md` | Cloud routine prompt — 9:00 AM CT daily |
| `routines/midday.md` | Cloud routine prompt — 2:00 PM CT daily |
| `routines/daily-summary.md` | Cloud routine prompt — 6:00 PM CT daily |
| `routines/weekly-review.md` | Cloud routine prompt — 6:00 PM CT Sunday |
| `.claude/commands/` | 7 local slash commands for manual testing |
| `CLAUDE.md` | Auto-loaded rulebook every Claude Code session |
| `env.template` | Credential template — copy to `.env` locally |

---

## Trading Strategy

- **Spot only** — no margin, no futures, no leverage, ever
- Max 5-6 open positions; max 20% of portfolio per position (~$2,000 on a $10k account)
- Hold 15-25% as USDT dry powder
- Every position gets a **stop-limit GTC order at 10% below entry** immediately after fill
- Cut losers at **-7%** (cancel stop, market sell)
- Tighten stop to 7% below price at **+15%**; tighten to 5% at **+20%**
- Max **3 new trades per week** — patience beats activity
- Follow crypto sector momentum (L1s, DeFi, AI tokens, gaming)
- Exit a sector after 2 consecutive losses
- Research runs through Perplexity (or WebSearch fallback) every morning

---

## Daily Schedule (Central Time)

| Time | Routine | What It Does |
|---|---|---|
| 6:00 AM | morning-research | Queries BTC price, dominance, Fear & Greed, macro, sector momentum, on-chain data. Writes trade ideas to RESEARCH-LOG. Silent unless urgent. |
| 9:00 AM | morning-execution | Reads today's research. Validates each trade idea against buy-side rules (positions ≤6, trades ≤3, size ≤20%, catalyst documented). Places market buys + immediate stop-limit orders. Notifies ClickUp only if a trade fires. |
| 2:00 PM | midday | Scans all positions. Cuts anything at -7%. Tightens stop-limits on +15% and +20% winners. Checks if any thesis broke. Notifies only if action taken. |
| 6:00 PM | daily-summary | Computes day P&L, phase P&L, positions table. Appends EOD snapshot to TRADE-LOG. Always sends ClickUp message. Always commits — tomorrow's P&L math depends on it. |
| 6:00 PM Sun | weekly-review | Full week stats vs BTC, win rate, profit factor, letter grade. Updates TRADING-STRATEGY.md if a rule needs changing. Always commits and notifies. |

---

## Environment Variables

Set these in `.env` locally and in each cloud routine's settings:

```
BYBIT_API_KEY        = (your key from Binance API Management)
BYBIT_SECRET_KEY     = (your secret — only shown once at creation)
BINANCE_BASE_URL       = https://api.binance.com
PERPLEXITY_API_KEY     = (optional — leave blank to use WebSearch fallback)
CLICKUP_API_KEY        = (from ClickUp Settings → Apps)
CLICKUP_WORKSPACE_ID   = (the number in your ClickUp URL)
CLICKUP_CHANNEL_ID     = (4-XXXXXXX-X format from your chat channel URL)
```

---

## Current Blockers (Still Needs To Be Done)

### 1. Binance API — Enable Trading
- **Problem:** Only "Enable Reading" is checked. Bot cannot place orders.
- **Fix:**
  1. Go to binance.com → Profile → API Management
  2. Find your key → click **Edit**
  3. Select **"Restrict access to trusted IPs only"**
  4. Enter your current IP address (find it at whatismyip.com)
  5. Check **"Enable Spot & Margin & Stock Trading"**
  6. Save

> **Note:** For cloud routines, the bot runs from Claude's cloud servers which have
> different IPs. Start with local testing first. We'll identify the cloud IPs after
> the first routine run.

### 2. GitHub App — Grant Repo Access
- **Problem:** Cloud routines show "no repository found."
- **Fix:**
  1. Go to [github.com/settings/installations](https://github.com/settings/installations)
  2. Find the **Claude** app → click **Configure**
  3. Under "Repository access" → add **gnm7208/Binance-bot**
  4. Save
  - If Claude isn't listed: go to [github.com/apps/claude](https://github.com/apps/claude) → Install

### 3. Create the Five Cloud Routines
- **Where:** claude.ai/code → Routines → New Routine
- **What to paste:** Contents of each file in the `routines/` folder
- **Settings per routine:**
  - Repository: `gnm7208/Binance-bot`
  - Branch: `main`
  - Toggle ON: **"Allow unrestricted branch pushes"** (critical — without this, git push silently fails)
  - Add all 7 environment variables from the table above

| Routine Name | Prompt File | Cron | Timezone |
|---|---|---|---|
| Trading bot — morning research | `routines/morning-research.md` | `0 6 * * *` | America/Chicago |
| Trading bot — morning execution | `routines/morning-execution.md` | `0 9 * * *` | America/Chicago |
| Trading bot — midday scan | `routines/midday.md` | `0 14 * * *` | America/Chicago |
| Trading bot — daily summary | `routines/daily-summary.md` | `0 18 * * *` | America/Chicago |
| Trading bot — weekly review | `routines/weekly-review.md` | `0 18 * * 0` | America/Chicago |

### 4. Test Before Going Live
1. After creating the morning-research routine, click **"Run now"**
2. Watch the logs — you should see env var checks pass, Binance account data returned, research written to memory
3. Go to [github.com/gnm7208/Binance-bot/commits/main](https://github.com/gnm7208/Binance-bot/commits/main) and confirm a new commit appears
4. If that works, the other routines are good to go on their schedules

### 5. Perplexity (Optional)
- The API costs money (usage-based, ~fractions of a cent per query)
- Leave `PERPLEXITY_API_KEY` blank — the bot automatically falls back to Claude's built-in WebSearch
- Add a Perplexity key later if you want higher-quality research citations

---

## Key Facts to Remember

- **BINANCE_BASE_URL is always** `https://api.binance.com` — it's the same for every user, not something found in your account
- **Secret Key is only shown once** — if you didn't copy it, you must delete and recreate the API key
- **Never commit `.env`** — it's in `.gitignore`. Cloud routines get credentials from environment variables set in the routine UI, not from a file
- **Git is the bot's memory** — if a cloud run doesn't commit and push, nothing is saved
- **"Allow unrestricted branch pushes" toggle** in each routine is mandatory — without it, the bot's memory never persists
