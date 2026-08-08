# Multi-Agent Specialization

**Status:** INACTIVE | **Impact:** 5 | **Bot Fit:** 3 | **Effort:** 9

## What It Does

Splits the bot into specialized sub-agents: a Research Agent (finds setups),
a Risk Agent (sizes positions, manages stops), an Execution Agent (places orders),
and a Review Agent (audits decisions). Each agent has a focused prompt and
independent git branch.

## Why Inactive

Bot_fit: 3 — the current architecture is intentionally single-Claude stateless.
Multi-agent coordination requires message passing, conflict resolution, and
shared-state management that is significantly more complex than the current design.
Overkill for a $30-50 portfolio with max 3 open positions.

## Activation Alert

Activate when: portfolio exceeds $500 and trade frequency exceeds 10 trades/day.
At that scale, specialized agents justify the coordination overhead.

## Source

YouTube video research (advanced bot architecture / multi-agent content), Aug 2026.
