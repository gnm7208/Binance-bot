# TradingView Webhooks

**Status: INACTIVE**
**Source: YouTube research — bot automation channels**
**Impact: 5 | Bot fit: 3 | Effort: 7**
**Activation alert: not recommended — conflicts with stateless architecture**

## Concept

TradingView Pine Script alerts firing webhooks to trigger entries in real-time,
replacing scheduled Claude cloud routines. Would enable sub-minute entry timing
on technical signals.

## Why INACTIVE

- Fundamentally conflicts with Nate Herk stateless architecture — Claude IS the bot;
  webhooks require always-on server or serverless function to receive payloads
- No persistent server in current setup; cloud routines are ephemeral
- Adding a webhook receiver introduces new infrastructure (Lambda, Render, Railway, etc.)
  with cost, maintenance, and additional failure modes
- TradingView premium required for webhook alerts ($15-60/month)
- Scheduled 5-scan-per-day cadence is sufficient for current strategy
- Real-time entries would increase trade frequency beyond the 20/week cap anyway

## Implementation Notes (if activated)

Would require major architecture change:
1. Persistent webhook receiver (serverless function or always-on container)
2. Authentication/signature verification on webhook payloads
3. Stateful position tracking (can't rely on fresh TRADE-LOG read each time)
4. Pine Script alerts configured per signal
Not compatible with current design. Consider only if moving to persistent bot architecture.
