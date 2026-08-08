# YouTube Sources & Creator Recommendations

## Videos Used for Bot Features

### Foundational Build
| Video | Creator | URL | Used For |
|---|---|---|---|
| Nate Herk Trading Bot Guide (playlist #3) | Nate Herk | https://www.youtube.com/watch?v=6MC1XqZSltw | Complete bot architecture — Claude IS the bot, git memory, cloud routines |

### Feature Videos (Aug 2026 research session)
| Video | Creator | URL | Features Extracted |
|---|---|---|---|
| How I Built a Self-Learning AI Trading Bot (Claude Code Live Build) | Nate Herk | https://www.youtube.com/watch?v=6I1wGCuFpbk | EMA-200 Trend Filter ✅ ACTIVE, Self-Learning Trade Review ✅ ACTIVE |
| How To Actually Build a Trading Bot With Claude Code (Fully Automated) | Unknown | https://www.youtube.com/watch?v=y_bsjZThP0o | VWAP Confirmation ✅ ACTIVE, HMM Market Regime ⏸ INACTIVE |
| Full AI Trading Bot Using Claude Code! (Insane Results) | Unknown | https://www.youtube.com/watch?v=tsCI72TWzsg | TradingView Webhooks ⏸ INACTIVE |
| I Built An Entire AI Trading Team With Claude Code in 14 min | Unknown | https://www.youtube.com/watch?v=HfEu7XPUnAU | Multi-Agent Specialization ⏸ INACTIVE |
| Perplexity swing trading research (not a single video) | — | — | Volume Surge Gate ✅ ACTIVE, RSI Signal Gate ✅ ACTIVE, Pullback Entry Mode ⏸ INACTIVE, Walk-Forward Backtesting ⏸ INACTIVE |

### Other Videos Found (reviewed but not directly implemented)
| Video | URL |
|---|---|
| I Built a FREE AI Trading Bot With Claude + TradingView (Full Guide) | https://www.youtube.com/watch?v=G6l6HfMbOLc |
| I Built an AI Trading Bot with Claude Code (Better Than Kimi 3?) | https://www.youtube.com/watch?v=ITo2bcYaBJE |
| How I Built an AI Trading Bot Using Claude (Full Step-by-Step Guide) | https://www.youtube.com/watch?v=AhHsaSt3UXA |

---

## Channel Recommendations

### Tier 1 — Direct Bot Signal Feed
Subscribe to these for Option B/C entry signals (catalysts, momentum, whale flow):

| Channel | Why | Bot Signal Type |
|---|---|---|
| **Crypto Banter** | Live altcoin momentum, breaking stories, real-time market discussion | Option C: multi-source confirmation |
| **Altcoin Daily** | High-frequency altcoin news, one of the largest channels | Option B catalysts (ETF, upgrades) |
| **Crypto Kirby** | Daily Bitcoin trade signals, short-term setups | Momentum gate confirmation |
| **Crypto Jebb** | Chart-based swing trading, explicit entry/exit levels | Option A momentum + Layer 3 review |

### Tier 2 — Market Context & Macro Gate
These channels feed the morning-research macro gate score:

| Channel | Why | Bot Signal Type |
|---|---|---|
| **Benjamin Cowen** | Data-driven on-chain analysis, cycle positioning, most cited credible analyst | Macro gate, BTC dominance context |
| **On Chain Mine** | On-chain analytics, wallet flows | Whale signal proxy (free alternative to Whale Alert) |
| **Coin Bureau** | Deep fundamental research | Option B catalyst validation |
| **DataDash** | Macro framing for crypto, risk-adjusted positioning | SIZE_MULTIPLIER context |

### Tier 3 — Bot Architecture & Strategy
New videos from these channels = potential new features to implement:

| Channel | Why | Bot Signal Type |
|---|---|---|
| **Nate Herk** | Built the exact architecture this bot runs on | New features, routing improvements |
| **CryptoBotMastery** | 487K subscribers, #1 ranked crypto bot channel | Strategy variants to evaluate |
| **Crypto Automation Lab** | Python bot coding, MEXC API integration | Script improvements |

---

## Top 5 to Subscribe To Now

1. **Nate Herk** — mandatory; he's the architect, new videos = new bot features
2. **Benjamin Cowen** — best macro/on-chain context for morning-research macro gate
3. **Crypto Banter** — highest signal density for altcoin momentum calls
4. **Altcoin Daily** — best for spotting Option B catalysts early (ETF filings, protocol upgrades)
5. **Coin Bureau** — deep research that validates Option B before sizing in

---

## Implementation Scorecard (Aug 2026 batch)

| Feature | Impact | Bot Fit | Effort | Status | Memory File |
|---|---|---|---|---|---|
| EMA-200 Trend Filter | 8 | 8 | 4 | ✅ ACTIVE | EMA-200-TREND-FILTER.md |
| Self-Learning Trade Review | 8 | 9 | 5 | ✅ ACTIVE | SELF-LEARNING-TRADE-REVIEW.md |
| Volume Surge Gate | 7 | 8 | 4 | ✅ ACTIVE | VOLUME-SURGE-GATE.md |
| RSI Signal Gate | 7 | 7 | 4 | ✅ ACTIVE | RSI-SIGNAL-GATE.md |
| VWAP Confirmation | 7 | 7 | 4 | ✅ ACTIVE | VWAP-CONFIRMATION.md |
| TradingView Webhooks | 7 | 4 | 8 | ⏸ INACTIVE | TRADINGVIEW-WEBHOOKS.md |
| Pullback Entry Mode | 6 | 5 | 6 | ⏸ INACTIVE | PULLBACK-ENTRY-MODE.md |
| HMM Market Regime | 5 | 4 | 9 | ⏸ INACTIVE | HMM-MARKET-REGIME.md |
| Multi-Agent Specialization | 5 | 3 | 9 | ⏸ INACTIVE | MULTI-AGENT-SPECIALIZATION.md |
| Walk-Forward Backtesting | 5 | 3 | 10 | ⏸ INACTIVE | WALK-FORWARD-BACKTESTING.md |
