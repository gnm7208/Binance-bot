---
description: Manual trade helper with strategy-rule validation. Usage — /trade SYMBOL USDT_AMOUNT buy|sell
---

Execute a manual trade with full rule validation. Refuse if any rule fails.

Args: SYMBOL (e.g. BTC), USDT_AMOUNT, SIDE (buy or sell). If missing, ask.
Pair = SYMBOL + "USDT" (e.g. BTCUSDT).

1. Pull live state:
   bash scripts/bybit.sh account
   bash scripts/bybit.sh positions
   bash scripts/bybit.sh orders
   bash scripts/bybit.sh quote <PAIR>

2. For BUY, validate ALL of these. If ANY fail, STOP and print the failed checks:
   ✓ Total positions after fill ≤ 6
   ✓ Trades this week + 1 ≤ 3 (check memory/TRADE-LOG.md for this week's count)
   ✓ USDT_AMOUNT ≤ 20% of total portfolio value
   ✓ USDT_AMOUNT ≤ free USDT balance
   ✓ Catalyst documented (ask for thesis if not in today's RESEARCH-LOG)
   ✓ PAIR is a spot USDT pair (no derivatives)

3. For SELL, confirm position exists. No other validation needed.

4. Print order params + validation results. Ask: "Execute? (y/n)"

5. On "y":
   bash scripts/bybit.sh order \
     '{"category":"spot","symbol":"<PAIR>","side":"Buy","orderType":"Market","qty":"<USDT_AMOUNT>","marketUnit":"quoteCoin"}'

6. For BUYs, immediately place stop-limit at 10% below fill price:
   stop_price = fill_price × 0.90
   limit_price = stop_price × 0.999
   bash scripts/bybit.sh order \
     '{"category":"spot","symbol":"<PAIR>","side":"Sell","orderType":"Limit","qty":"<qty>","price":"<limit_price>","triggerPrice":"<stop_price>","triggerBy":"LastPrice","orderFilter":"StopOrder","timeInForce":"GTC"}'

7. Append to memory/TRADE-LOG.md (full thesis, entry, stop, target, R:R, stop order ID).

8. bash scripts/clickup.sh with trade details.

9. Commit and push:
   git add memory/TRADE-LOG.md
   git commit -m "manual trade $(date +%Y-%m-%d)"
   git push origin main
