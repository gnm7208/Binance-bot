# Trading Bot — To-Do

## Blockers (Bot Cannot Trade Until Fixed)

### 1. Update Cloud Routine Environment Variables (Bybit)
- **Problem:** All 5 routines still have BINANCE_* env vars — need replacing with BYBIT_*.
- **Steps:** For each of the 5 routines in claude.ai/code → Edit → environment variables:
  - Remove: `BINANCE_API_KEY`, `BINANCE_SECRET_KEY`, `BINANCE_BASE_URL`
  - Add: `BYBIT_API_KEY` = your Bybit API key
  - Add: `BYBIT_SECRET_KEY` = your Bybit secret key
  - Add: `BYBIT_BASE_URL` = `https://api.bybit.com`

### 2. Verify Bybit API Works from Cloud
- After updating env vars, click **Run now** on morning-research
- Check logs: `bash scripts/bybit.sh account` should return wallet balance JSON (not a 4xx error)
- If successful: Bybit access confirmed, bot can proceed to trade

### 3. Fix Weekly Review Schedule
- **Problem:** Weekly review shows "Every Sunday at 11:45 PM" — should be 6:00 PM CT.
- **Fix:** Edit routine → cron `0 18 * * 0`, timezone `America/Chicago`

---

## High Priority (Do Soon)

### 4. Add Bybit Cloud IP to API Whitelist (after first successful run)
- Currently: No IP restriction (necessary until we know the cloud server's IP)
- After first successful run: find outbound IP in the run logs
- Go to bybit.com → Account → API Management → Edit key → switch to IP whitelist → add cloud IP

### 5. Fix "Allow unrestricted branch push" Toggle
- **Current workaround:** GitHub Action auto-merges `claude/*` branches into `main` (working)
- **Ideal fix:** Report at github.com/anthropics/claude-code/issues and retry when fixed

---

## Optional Improvements

### 6. ClickUp Notifications
- Set `CLICKUP_API_KEY`, `CLICKUP_WORKSPACE_ID`, `CLICKUP_CHANNEL_ID` in routine environments
- Currently falling back to `NOTIFICATIONS.md` local file

### 7. Perplexity API (Optional)
- Leave blank — WebSearch fallback works fine
- Add `PERPLEXITY_API_KEY` later for higher-quality cited research

### 8. Fix Routine Name Typo
- "morning excecution" → "morning execution"

---

## Future / Nice-to-Have

| Item | Description |
|---|---|
| Sector watchlist | Add curated L1/DeFi/AI token list to `TRADING-STRATEGY.md` |
| Take-profit orders | OCO orders once basic stop-limit flow is proven |
| Weekly P&L chart | Artifact showing performance vs BTC over time |
