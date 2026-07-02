---
description: Run the midday scan locally (reads from .env, no auto-commit)
---

Run the midday scan workflow. Use local .env for credentials.

Follow every step in routines/midday.md EXCEPT:
- Skip the env-var pre-check block (credentials come from .env automatically)
- Skip STEP 8 (commit and push) — ask before committing locally

For any sell or stop-tighten action, print the proposed action and ask for confirmation
before executing.
