# MEXC Trading Bot — To-Do

## Remaining Blockers

### 1. Set Perplexity API Key in Cloud Routine Environments
- For each of the 7 routines in claude.ai/code → Edit → environment variables:
  - Add: `PERPLEXITY_API_KEY` = your Perplexity key (from perplexity.ai/settings/api)
  - Add: `PERPLEXITY_MODEL` = `sonar`
- Without this, cloud runs fall back to WebSearch — max signal score drops 17 → 10

---

## High Priority

### 2. Fix "Allow unrestricted branch push" Toggle
- **Current workaround:** GitHub Action auto-merges `claude/*` branches into `main` (working)
- **Ideal fix:** Report at github.com/anthropics/claude-code/issues and retry when fixed

### 3. Update Cloud Routine Repo Reference
- After the GitHub rename from `Binance-bot` → `MEXC-bot`, verify each routine
  still points to the correct repo (GitHub auto-redirects but confirm in routine settings)

### 4. Fix Weekly Review Schedule (if not already fixed)
- Should fire at 6:00 PM CT Sunday
- Cron: `0 18 * * 0`, timezone `America/Chicago`

---

## Optional Improvements

### 5. MEXC IP Whitelist
- After confirming cloud IPs from a successful run, add them to the MEXC API key
  restrictions at mexc.com/user/openapi for additional security

### 6. ClickUp Notifications
- Verify `CLICKUP_API_KEY`, `CLICKUP_WORKSPACE_ID`, `CLICKUP_CHANNEL_ID` are set
  in all 7 cloud routine environments

---

## Future / Nice-to-Have

| Item | Description |
|---|---|
| Sector watchlist | Add curated L1/DeFi/AI token list to `memory/TRADING-STRATEGY.md` |
| Whale Alert key | Free tier gives whale signal points (+3 to score) — high impact |
| Volatility-adjusted stops | Activate after ≥10 closed trades if stop-outs are root cause of losses |
