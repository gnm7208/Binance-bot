# Anomaly Detector

## Status
ACTIVE — implemented 2026-08-06. impact: 7 | bot_fit: 9 | effort: 4
Applied in: morning-research.md STEP 1E (checks A/C/D) and STEP 2B (check B).
Note: checks C and D self-activate once enough trade history exists (7+ stop-outs / 10+ closed trades).

## The Rule (when active)
At the start of morning-research STEP 1, after reading TRADE-LOG and RESEARCH-LOG,
check for four anomaly patterns and alert via ClickUp if any are detected:

### Anomaly A — Consecutive skips (under-deployment drift)
```
N_skip_days = count consecutive days where Decision = HOLD or MACRO_HALTED in RESEARCH-LOG
If N_skip_days >= 3 AND MACRO_SCORE >= 40 (macro is tradeable):
    bash scripts/clickup.sh "ANOMALY: 3+ consecutive HOLD days with tradeable macro — review signal thresholds"
```

### Anomaly B — TP ghost (position stuck above target)
```
For each open position:
    If live_price >= target_price AND position still open:
        If position has been above target for > 2 routine checks:
            bash scripts/clickup.sh "ANOMALY: TICKER above +12% target for >2 checks — TP not executing?"
```
Catches cases where take-profit monitoring failed (network error, API timeout).

### Anomaly C — Repeated stop-outs at same time of day
```
From TRADE-LOG, find last 7 closed trades that were stop-outs.
Check if >= 3 of them occurred during the same 2-hour UTC window (e.g. all at 08:00-10:00 UTC).
If yes:
    bash scripts/clickup.sh "ANOMALY: 3+ stop-outs clustered in UTC HH:00-HH:00 window — time-based risk pattern"
```
Catches systematic vulnerability at a specific session (Asian open dump, US open flush, etc.).

### Anomaly D — Win rate deterioration outpacing circuit breaker
```
N_recent = last 10 closed trades (not just this week)
N_loss_recent = losses in those 10
loss_rate_10 = N_loss_recent / N_recent
If loss_rate_10 > 0.50 AND circuit_breaker NOT already active:
    bash scripts/clickup.sh "ANOMALY: 50%+ loss rate in last 10 trades — strategy drift, review signal scoring"
```
This is a leading indicator that catches deterioration before the circuit breaker's weekly window.

## Implementation location
Add as STEP 1E in morning-research.md, after the existing TRADE-LOG tail read:

```
STEP 1E — Anomaly scan (runs every morning-research):
  (Read last 30 TRADE-LOG entries + last 7 RESEARCH-LOG decisions — already done in STEP 1)
  Check A: consecutive HOLD/HALTED days vs macro score
  Check B: any position whose live price >= target (from STEP 2 positions check)
  Check C: time clustering in stop-outs
  Check D: rolling 10-trade loss rate
  Send ClickUp alert for any that trigger. Log in today's RESEARCH-LOG: "Anomaly: [A/B/C/D detected or none]"
```

## Why it exists
From GPT-5.4 nano bot improvement analysis (Aug 2026): circuit breaker and daily gate
catch acute failures (40% loss rate this week) but miss chronic drift — e.g., a bot
that has been in HOLD mode for 5 days during a good macro environment, or that
repeatedly loses at the Asian open. The anomaly detector surfaces these patterns before
they compound into a large drawdown or missed opportunity.

## Trade-offs
- **Pro**: Catches systematic issues the circuit breaker cannot — especially time-based and deployment-based
- **Pro**: No new API calls — all data is already read in STEP 1 and STEP 2
- **Pro**: ClickUp alert is already our notification pattern; fits naturally
- **Con**: Adds noise risk — may alert during legitimate HOLD periods (e.g., MACRO_HALTED for 3 days)
- **Con**: Requires enough history to be meaningful (< 15 trades → false signals)
- **Con**: Anomaly C (time clustering) needs >= 7 stop-outs to detect reliably

## When to activate
Consider activating if:
- >= 15 closed trades recorded in TRADE-LOG
- Have experienced at least one case where a systematic problem wasn't caught by circuit breaker
- Aug 22 phase review identifies any of these patterns in the Aug 4-22 data

## Activation checklist (manual — requires user approval)
- [ ] >= 15 closed trades in TRADE-LOG for meaningful pattern detection
- [ ] User explicitly approves activation
- [ ] Add STEP 1E block to morning-research.md
- [ ] Define thresholds based on observed data (N_skip_days, time windows, etc.)
- [ ] Add "ANOMALY_DETECTOR: ACTIVE" to TRADING-STRATEGY.md
