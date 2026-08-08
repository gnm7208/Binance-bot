# Multi-Agent Specialization

**Status: INACTIVE**
**Source: YouTube research — Nate Herk advanced architecture video**
**Impact: 5 | Bot fit: 4 | Effort: 8**
**Activation alert: enable when managing >= 5 positions simultaneously or >= $10K portfolio**

## Concept

Split the bot into specialized sub-agents:
- Research agent: macro gate + watchlist scoring
- Execution agent: order placement + position sizing
- Risk agent: stop monitoring + exit decisions
- Review agent: weekly stats + strategy updates

Each runs independently; master agent orchestrates via shared memory files.

## Why INACTIVE

- Current portfolio size ($33 USDT) doesn't justify complexity
- Single-agent stateless architecture works well at current scale
- Multi-agent coordination overhead would slow execution
- Shared state via TRADE-LOG already provides inter-routine communication
- Additional API costs (each agent = separate Claude call)

## Implementation Notes (if activated)

Would require:
1. Separate routine files per agent (already partly there: morning-research, morning-execution, etc.)
2. Handoff protocol: structured JSON blocks in RESEARCH-LOG for execution agent to consume
3. Conflict resolution when agents disagree (e.g. research says buy, risk agent says sector blocked)
4. Master orchestrator routine that sequences agents
Current structure is already moving this direction — routines ARE specialized agents.
The main gap is the handoff format between research and execution.
