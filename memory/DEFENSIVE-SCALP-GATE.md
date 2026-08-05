# Defensive Scalp Gate — Future Feature (NOT YET ACTIVE)

## Status
INACTIVE — documented for future activation. Do NOT apply this rule until explicitly
enabled in TRADING-STRATEGY.md.

## When to activate
Consider activating if ALL of the following are true:
- Phase portfolio is down >= 5% from its peak equity value
- At least 3 consecutive days with no qualifying entry (score >= 5)
- Macro gate is REDUCED or FULL (SIZE_MULTIPLIER > 0) — market is tradeable
- Standard +12% TP / -7% stop rules are not generating entries

## The rule (when active)
If the above conditions hold AND a coin scores >= 7 with +3% to +5% short momentum:
- Enter at 15% of portfolio (half the minimum standard size)
- TP: +5% (not the standard +12%)
- Stop: -3% (not the standard -7%)
- Max 1 defensive scalp position at a time
- Does NOT count toward the 3-position max (it's a separate recovery lane)
- DOES count toward the 5/day and 20/week trade limits
- Must be recorded in TRADE-LOG with type: "Defensive Scalp"
- Deactivate this mode the moment portfolio recovers to within 2% of phase peak

## Why it exists
From the 30-day AI bot challenge analysis (Aug 2026): Salmon's bot recovered
a significant drawdown by switching to scalping when standard swing trades were
not triggering. The approach was accidental but effective. This formalizes it as
a deliberate recovery mechanism, with tighter parameters suited to our small
portfolio (~$30-50) and MEXC's liquidity constraints.

## Risks
- Adds a rule exception to the strategy — complexity cost
- Tight -3% stop in volatile crypto = frequent stop-outs
- May generate churn (multiple small trades) that fragments attention
- Only worth activating with >= 5 closed trades to confirm the standard strategy
  is underperforming, not just in a normal drawdown

## Activation checklist (manual — requires user approval)
- [ ] Portfolio down >= 5% from phase peak for >= 3 consecutive days
- [ ] Standard strategy producing 0 qualifying entries for >= 3 days
- [ ] Macro gate is REDUCED or FULL
- [ ] User has explicitly approved activation in this conversation
- [ ] Add "DEFENSIVE_SCALP_GATE: ACTIVE" line to TRADING-STRATEGY.md
- [ ] Deactivate by removing that line when portfolio recovers
