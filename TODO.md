# Trading Bot — To-Do

## Blockers (Bot Cannot Trade Until Fixed)

### 1. Create MEXC Account & API Key
- Go to mexc.com → sign up
- Account → API Management → Create API key
- Permissions: Read + Spot Trade only (no margin, no futures)
- Copy API key and secret

### 2. Update Cloud Routine Environment Variables (MEXC)
- For each of the 5 routines in claude.ai/code → Edit → environment variables:
  - Remove any old Binance or Bybit vars if present
  - Add: `MEXC_API_KEY` = your MEXC API key
  - Add: `MEXC_SECRET_KEY` = your MEXC secret key
  - Add: `MEXC_BASE_URL` = `https://api.mexc.com`

### 3. Verify MEXC API Works from Cloud
- After updating env vars, click **Run now** on morning-research
- Check logs: `bash scripts/mexc.sh account` should return wallet balance JSON
- If successful: MEXC access confirmed, bot can proceed to trade

### 4. Fix Weekly Review Schedule
- **Problem:** Weekly review cron is wrong — should be 6:00 PM CT Sunday.
- **Fix:** Edit routine → cron `0 18 * * 0`, timezone `America/Chicago`

---

## High Priority (Do Soon)

### 5. Fix "Allow unrestricted branch push" Toggle
- **Current workaround:** GitHub Action auto-merges `claude/*` branches into `main` (working)
- **Ideal fix:** Report at github.com/anthropics/claude-code/issues and retry when fixed

### 6. Fix Routine Name Typo
- "morning excecution" → "morning execution" (typo in routine name on claude.ai/code)

---

## Optional Improvements

### 7. ClickUp Notifications
- Set `CLICKUP_API_KEY`, `CLICKUP_WORKSPACE_ID`, `CLICKUP_CHANNEL_ID` in routine environments
- Currently falling back to `NOTIFICATIONS.md` local file

### 8. Perplexity API (Optional)
- Leave blank — WebSearch fallback works fine
- Add `PERPLEXITY_API_KEY` later for higher-quality cited research

---

## Future / Nice-to-Have

| Item | Description |
|---|---|
| Sector watchlist | Add curated L1/DeFi/AI token list to `TRADING-STRATEGY.md` |
| Weekly P&L chart | Artifact showing performance vs BTC over time |
| IP whitelist | After first successful MEXC run, add cloud server IP to API key |
