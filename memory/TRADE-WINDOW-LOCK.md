---
name: TRADE-WINDOW-LOCK
status: INACTIVE
source: Carl futures day-trading transcript (2026-08-06)
impact: 5 | bot_fit: 5 | effort: 6
---

# Trade Window Lock — Session-Open Only Entries (INACTIVE)

Only allow new BUY entries within 2 hours of a major market session open.
Avoids dead-zone entries during low-liquidity mid-session periods.

**Rationale:** Carl trades the first 60-90 min after futures open (9:30 AM ET). The market
has the most reliable setups and highest volume immediately after major session opens.
Dead-zone entries (middle of night, mid-afternoon drift) tend to have lower follow-through.

**Why INACTIVE:** Our current schedule already targets session opens (morning-execution fires
at 14:00 UTC = US pre-market, afternoon-execution at 21:00 UTC = US market open, evening-scan
at 03:00 UTC = Asian open). Adding a hard gate needs win-rate data by time-of-entry first.

## Activation Condition

Activate when:
- ≥ 20 closed trades in TRADE-LOG with recorded entry timestamps
- Win rate analysis shows dead-zone entries (>2h after any session open) win rate < 40%

## Implementation When Active

In morning-execution.md STEP 5 / afternoon-execution.md STEP 5, before buy:
```
WINDOW_CHECK: is current UTC time within 2h of a major session open?
  Asian open:  00:00-02:00 UTC
  EU open:     07:00-09:00 UTC
  US pre-open: 13:30-15:30 UTC
  US open:     14:30-16:30 UTC
If NOT in a window: log "TRADE-WINDOW: outside session window — skip new entries"
```
