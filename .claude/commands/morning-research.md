---
description: Run the morning research workflow locally (reads from .env, no auto-commit)
---

Run the morning-research workflow. Use local .env for credentials.

Follow every step in routines/morning-research.md EXCEPT:
- Skip the env-var pre-check block (credentials come from .env automatically)
- Skip STEP 6 (commit and push) — you control when to commit locally

After writing to memory/RESEARCH-LOG.md, print a summary of:
- Account state
- Today's trade ideas
- Decision: TRADE or HOLD
