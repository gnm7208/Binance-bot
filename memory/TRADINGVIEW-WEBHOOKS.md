# TradingView Webhooks

**Status:** INACTIVE | **Impact:** 7 | **Bot Fit:** 4 | **Effort:** 8

## What It Does

TradingView Pine Script alerts fire webhooks to a hosted endpoint when technical
signals trigger (e.g. EMA cross, RSI threshold, volume spike). The endpoint queues
the signal and the bot executes on the next routine run.

## Why Inactive

Bot_fit: 4 — requires: (1) a persistent webhook receiver (server or serverless
function), (2) TradingView Pro+ subscription for webhook alerts, (3) signal queue
storage between the webhook receipt and routine execution. Conflicts with the
stateless git-as-memory architecture.

## Activation Alert

Activate when: a persistent signal queue (Redis, Supabase, or simple S3/git file)
is added and a webhook endpoint is hosted. TradingView Pro+ subscription required.

## Source

YouTube video research (TradingView automation content), Aug 2026.
