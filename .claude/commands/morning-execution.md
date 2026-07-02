---
description: Run the morning execution workflow locally (reads from .env, no auto-commit)
---

Run the morning-execution workflow. Use local .env for credentials.

Follow every step in routines/morning-execution.md EXCEPT:
- Skip the env-var pre-check block (credentials come from .env automatically)
- Skip STEP 8 (commit and push) — ask before committing locally

Before placing any order, print the full buy-side gate results and ask for confirmation.
