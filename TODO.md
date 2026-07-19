# Trading Bot — To-Do

## Blockers (Bot Cannot Trade Until Fixed)

### 1. Binance API — Enable Trading Permission
- **Problem:** API key only has "Enable Reading" checked. Bot cannot place orders.
- **Steps:**
  1. Go to binance.com → Profile → API Management → find your key → **Edit**
  2. Under IP restrictions: select **"Restrict access to trusted IPs only"**
  3. Add your home/office IP (find it at whatismyip.com)
  4. Check **"Enable Spot & Margin Trading"**
  5. Save
- **Note:** Cloud routine IPs will also need to be added after the first successful run. Check the run logs for the outbound IP and add it to the Binance API whitelist.

### 2. Cloud Routine Network Access — Allow External APIs
- **Problem:** Cloud routine network policy is blocking calls to `api.binance.com` and `api.clickup.com` (both returned 403 on the first live run).
- **Steps:**
  1. Open any routine in claude.ai/code → Edit → **Behavior** tab (or network settings)
  2. Change network access from **Trusted** to **All** (or unrestricted)
  3. Save and apply to all 5 routines
- **Why:** Without this, the bot can research (WebSearch works) but cannot read account state or place orders.

### 3. Unrestricted Branch Push — Save Fails in Claude Code UI
- **Problem:** "Allow unrestricted git push" toggle fails to save in the Permissions tab.
- **Current workaround:** GitHub Action (`.github/workflows/merge-bot-branch.yml`) auto-merges `claude/*` branches into `main`. This works but adds ~30s delay.
- **Ideal fix:** Report this bug at github.com/anthropics/claude-code/issues and retry when fixed.

---

## High Priority (Do Soon)

### 4. Fix Weekly Review Schedule
- **Problem:** Weekly review routine shows "Every Sunday at 11:45 PM" — should be 6:00 PM CT.
- **Steps:** Edit routine → change cron to `0 18 * * 0` with timezone `America/Chicago`

### 5. Verify First Successful End-to-End Run
- After fixing items 1 and 2 above, run morning-research and confirm:
  - [ ] `bash scripts/binance.sh account` returns real JSON (not 403)
  - [ ] Research entry committed and merged to `main` (check GitHub Actions tab)
  - [ ] ClickUp receives the notification (if configured)
- Then let morning-execution run at 9 AM and confirm it reads the research and evaluates trades

### 6. Add Binance Cloud IPs to API Whitelist
- After the first successful routine run, find the outbound IP in the run logs
- Add it to binance.com → API Management → your key → Edit → IP whitelist
- This is separate from your home IP

---

## Optional Improvements

### 7. ClickUp Notifications (Optional but Recommended)
- Currently falling back to `NOTIFICATIONS.md` (local file) because ClickUp credentials are missing or blocked
- Set `CLICKUP_API_KEY`, `CLICKUP_WORKSPACE_ID`, `CLICKUP_CHANNEL_ID` in each routine's environment
- Verify the channel ID format: `4-XXXXXXX-X` from your ClickUp chat channel URL

### 8. Perplexity API (Optional)
- Bot currently uses WebSearch fallback — this works fine
- Add `PERPLEXITY_API_KEY` to routine environments for higher-quality cited research
- Usage-based pricing, fractions of a cent per query

### 9. Rename "morning excecution" Typo
- Routine name has a typo: "excecution" → "execution"
- Fix: Edit routine → change Name field → Save

### 10. Local Testing with `.env`
- Copy `env.template` to `.env` and fill in credentials
- Test locally before relying on cloud runs:
  ```bash
  bash scripts/binance.sh account          # should return JSON
  bash scripts/binance.sh positions        # should return balances
  bash scripts/clickup.sh "test message"   # should post to ClickUp
  ```
- Run `/portfolio` in Claude Code to get a read-only account snapshot

---

## Future / Nice-to-Have

| Item | Description |
|---|---|
| Sector watchlist | Add a curated list of L1/DeFi/AI tokens to `TRADING-STRATEGY.md` for the bot to scan |
| Take-profit orders | Add OCO orders (limit take-profit + stop) once the basic stop-limit flow is proven |
| Position sizing calculator | Script to compute exact quantity given USDT amount and current price |
| Weekly performance chart | Artifact showing P&L vs BTC over time |
| Telegram notifications | Alternative to ClickUp if ClickUp proves unreliable |
