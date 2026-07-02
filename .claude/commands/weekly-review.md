---
description: Run the weekly review locally (reads from .env, no auto-commit)
---

Run the weekly review workflow. Use local .env for credentials.

Follow every step in routines/weekly-review.md EXCEPT:
- Skip the env-var pre-check block (credentials come from .env automatically)
- Skip STEP 7 (commit and push) — ask before committing locally

Always send the ClickUp notification (STEP 6). If a strategy rule needs updating, show the
proposed change and ask for approval before writing to memory/TRADING-STRATEGY.md.
