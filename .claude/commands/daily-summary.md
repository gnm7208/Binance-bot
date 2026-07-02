---
description: Run the daily summary locally (reads from .env, no auto-commit)
---

Run the daily summary workflow. Use local .env for credentials.

Follow every step in routines/daily-summary.md EXCEPT:
- Skip the env-var pre-check block (credentials come from .env automatically)
- Skip STEP 6 (commit and push) — ask before committing locally

Always send the ClickUp notification (STEP 5) — this is the daily status message.
