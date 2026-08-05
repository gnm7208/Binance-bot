# Reversal Candle Gate — Future Feature (NOT YET ACTIVE)

## Status
INACTIVE — documented for future activation. Do NOT apply this rule until explicitly
enabled in TRADING-STRATEGY.md.

## The Rule (when active)
Before entering any position, require a reversal candle to appear OUTSIDE the opening
range box on a 5-minute chart within 90 minutes of the US market open (13:30–15:00 UTC).

**Reversal candle types (must appear BELOW the range for a long, ABOVE for a short):**
- Hammer: small body at top, long lower wick >= 2× body size, after a clear down move
- Bullish engulfing: large green candle that fully engulfs the prior red candle body
- Inverted hammer: small body at bottom, long upper wick, after clear up move (bearish)
- Bearish engulfing: large red candle that fully engulfs the prior green candle body

**Entry mechanics (once reversal candle confirmed):**
- Hammer/inverted hammer: enter at break of next candle (open of candle after reversal)
- Engulfing candle: set limit order at high of the candle PRIOR to the engulfing candle
- Stop: at extreme of the reversal candle (hammer low, inv-hammer high)
- TP: opposite end of the opening range box

**Detection logic (5m klines):**
```python
curl -s "https://api.mexc.com/api/v3/klines?symbol=TICKERUSDT&interval=5m&limit=18" | python3 -c "
import json, sys
candles = json.load(sys.stdin)
# Look for hammer: lower wick >= 2x body, below opening range low
for i in range(1, len(candles)-1):
    o, h, l, c = [float(candles[i][j]) for j in [1,2,3,4]]
    body = abs(c - o); upper_wick = h - max(c,o); lower_wick = min(c,o) - l
    is_hammer = lower_wick >= 2*body and upper_wick <= body*0.5 and c > o
    # For engulfing: compare with prior candle
    po, pc = float(candles[i-1][1]), float(candles[i-1][4])
    is_bull_engulf = c > o and o < pc and c > po  # green engulfs prior red
    if is_hammer or is_bull_engulf:
        pattern = 'HAMMER' if is_hammer else 'BULL ENGULF'
        print(f'Reversal candle found at {candles[i][0]}: {pattern} | o={o} h={h} l={l} c={c}')
print('No reversal candle detected in last 18 5m candles')
"
```

## Why it exists
From the Quick Flip Scalper strategy (Carl, 20-year trader, Aug 2026 transcript): the
reversal candle is the entry trigger that confirms institutions have absorbed the
liquidity flush and are now moving price back. Without this confirmation, the
manipulation candle could simply be the start of a trend continuation, not a reversal.

## Trade-offs
- **Pro**: High win-rate when combined with ATR manipulation flush signal (+1 pt)
- **Pro**: Specific, visual confirmation that reversal is underway before committing
- **Pro**: Integrates naturally with existing Layer 2 signal scoring
- **Con**: Only meaningful for entries timed around US market open (13:30-15:00 UTC)
- **Con**: Adds 5m kline fetch and pattern detection to execution routines
- **Con**: Reversal candle can appear and fail — not a guaranteed entry
- **Con**: Our routines fire at fixed times; may miss the reversal candle window

## When to activate
Consider activating if:
- ATR manipulation flush signal (+1 pt) is generating trades but win rate < 60%
- Adding a reversal candle confirmation step would filter the false flush signals
- Bot is running a version timed closer to the US market open window

## Relationship to ATR manipulation flush
The ATR flush (+1 signal score) already identifies the manipulation event.
This gate would add a second confirmation at EXECUTION time that the reversal is
confirmed by candle structure — higher conviction, lower entry frequency.
See also: [[3CANDLE-CONFIRMATION-GATE]] for a simpler 3-candle variant.

## Activation checklist (manual — requires user approval)
- [ ] User explicitly approves activation
- [ ] Add 5m kline reversal check to morning-execution.md STEP 5 (between research and order)
- [ ] Add "REVERSAL_CANDLE_GATE: ACTIVE" line to TRADING-STRATEGY.md
- [ ] Accept: fewer entries triggered (confirmation filter), higher win rate expected
