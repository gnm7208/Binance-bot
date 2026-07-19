---
description: Read-only snapshot of account, positions, open orders, and stops
---

Print a clean ad-hoc snapshot. No state changes, no orders, no file writes.

1. bash scripts/bybit.sh account
2. bash scripts/bybit.sh positions
3. bash scripts/bybit.sh orders
4. For each non-USDT position: bash scripts/bybit.sh price <TICKER>USDT

Compute total portfolio value = free USDT + sum(qty × current_price).

Format output as:

Portfolio — <today's date>
Total value: $X,XXX | Free USDT: $X,XXX (X%) | Open positions: N
Phase P&L: ±$X (±X%) vs $10,000 starting capital

Positions:
TICKER | Qty | Entry | Price | Unrealized P&L | Stop order ID
...

Open stop orders:
SYMBOL | side | type | stopPrice | qty | orderId
...

Flags (add if true):
⚠️  TICKER has no stop order — SET IMMEDIATELY
⚠️  TICKER stop price is above current price — CHECK ORDER
⚠️  X trades placed this week (max 3)
