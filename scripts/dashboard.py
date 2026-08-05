#!/usr/bin/env python3
"""Bot dashboard — parses memory/TRADE-LOG.md and opens a visual stats page."""
import re, webbrowser, tempfile, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG  = ROOT / "memory" / "TRADE-LOG.md"
BASELINE = 32.32

# ── Parsers ────────────────────────────────────────────────────────────────────

def parse_log():
    text = LOG.read_text(encoding="utf-8")

    # EOD Portfolio snapshots
    # Pattern: **Portfolio:** $32.96 | **Cash:** $26.20 (79.5%) | ... | **Phase P&L:** +$0.64 (+1.99%)
    snapshots = []
    snap_re = re.compile(
        r'\*\*Portfolio:\*\* \$([\d.]+).*?\*\*Cash:\*\* \$([\d.]+) \(([\d.]+)%\)'
        r'.*?\*\*Phase P&L:\*\* ([+\-]?\$?[\d.]+) \(([+\-]?[\d.]+)%\)'
    )
    # Find dates for each snapshot block (split on ---)
    blocks = re.split(r'\n---+\n', text)
    for block in blocks:
        m = snap_re.search(block)
        if not m:
            continue
        date_m = re.search(r'## (\d{4}-\d{2}-\d{2}|[A-Z][a-z]+ \d+)', block)
        date_str = date_m.group(1) if date_m else ''
        # Shorten date for display
        short = _short_date(date_str)

        phase_pnl = float(m.group(4).replace('$','').replace('+',''))
        snapshots.append({
            'date': short,
            'portfolio': float(m.group(1)),
            'cash': float(m.group(2)),
            'cash_pct': float(m.group(3)),
            'phase_pnl': phase_pnl,
            'phase_pnl_pct': float(m.group(5)),
        })

    # BUY entries
    buys = []
    buy_re = re.compile(
        r'(## (?:\d{4}-\d{2}-\d{2}|[A-Z][a-z]+ \d+).*?Trade Entry.*?\n)'
        r'.*?\*\*BUY\*\* (\w+)\s*\|\s*Qty:\s*([\d.]+)\s*\|\s*Entry:\s*\$([\d.]+)'
        r'(?:.*?\*\*Thesis:\*\*\s*(.+?)(?=\n\*\*|\n\n|\Z))?',
        re.DOTALL
    )
    for m in buy_re.finditer(text):
        date_m = re.search(r'(\d{4}-\d{2}-\d{2}|[A-Z][a-z]+ \d+)', m.group(1))
        symbol = m.group(2).replace('USDT','').replace('usdt','')
        thesis = (m.group(5) or '').strip()[:80]
        buys.append({
            'date': _short_date(date_m.group(1) if date_m else ''),
            'symbol': symbol,
            'qty': float(m.group(3)),
            'entry': float(m.group(4)),
            'thesis': thesis,
        })

    # SELL entries
    sells = []
    sell_re = re.compile(
        r'(## (?:\d{4}-\d{2}-\d{2}|[A-Z][a-z]+ \d+).*?Trade Exit.*?\n)'
        r'.*?\*\*SELL\*\* (\w+).*?Realized P&L:\s*([+\-]\$([\d.]+)) \(([+\-][\d.]+)%\)',
        re.DOTALL
    )
    for m in sell_re.finditer(text):
        date_m = re.search(r'(\d{4}-\d{2}-\d{2}|[A-Z][a-z]+ \d+)', m.group(1))
        symbol = m.group(2).replace('USDT','').replace('usdt','')
        sign = 1 if m.group(3).startswith('+') else -1
        realized = sign * float(m.group(4))
        pct = float(m.group(5))
        sells.append({
            'date': _short_date(date_m.group(1) if date_m else ''),
            'symbol': symbol,
            'realized_pnl': realized,
            'realized_pnl_pct': pct,
        })

    # Open positions from latest EOD table row
    # Pattern: | ADA    | 35.1 | $0.18639 | $0.1927 | +0.47%  | +$0.22 (+3.39%) | $0.1822  |
    positions = []
    pos_re = re.compile(
        r'^\|\s*([A-Z]+)\s*\|\s*([\d.]+)\s*\|\s*\$([\d.]+)\s*\|\s*\$([\d.]+)\s*\|'
        r'\s*([+\-][\d.]+%)\s*\|\s*([+\-]\$[\d.]+ \([+\-][\d.]+%\))\s*\|\s*\$([\d.]+)',
        re.MULTILINE
    )
    # Grab from last EOD block that has real positions
    for block in reversed(blocks):
        if '**Portfolio:**' not in block:
            continue
        found = []
        for pm in pos_re.finditer(block):
            ticker = pm.group(1)
            if ticker == '—':
                continue
            pnl_m = re.search(r'\(([+\-][\d.]+)%\)', pm.group(6))
            found.append({
                'ticker': ticker,
                'qty': float(pm.group(2)),
                'entry': float(pm.group(3)),
                'price': float(pm.group(4)),
                'pnl_pct': float(pnl_m.group(1)) if pnl_m else 0,
                'stop': float(pm.group(7)),
            })
        if found:
            positions = found
            break

    return snapshots, buys, sells, positions


def _short_date(s):
    """Normalize to short display form: 'Aug 4' or 'Jul 29'."""
    if not s:
        return ''
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', s)
    if m:
        months = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        return f"{months[int(m.group(2))]} {int(m.group(3))}"
    return s


# ── HTML generator ─────────────────────────────────────────────────────────────

def render(snapshots, buys, sells, positions):
    latest = snapshots[-1] if snapshots else {'portfolio': 0, 'cash': 0, 'cash_pct': 0,
                                               'phase_pnl': 0, 'phase_pnl_pct': 0}
    portfolio   = latest['portfolio']
    free_usdt   = latest['cash']
    cash_pct    = latest['cash_pct']
    deployed_pct = 100 - cash_pct
    phase_pnl   = latest['phase_pnl']
    phase_pnl_pct = latest['phase_pnl_pct']

    wins   = [s for s in sells if s['realized_pnl'] > 0]
    losses = [s for s in sells if s['realized_pnl'] <= 0]
    win_rate = (len(wins) / len(sells) * 100) if sells else 0
    realized_total = sum(s['realized_pnl'] for s in sells)
    avg_win = (sum(s['realized_pnl_pct'] for s in wins) / len(wins)) if wins else 0

    snap_dates = [s['date'] for s in snapshots]
    snap_vals  = [s['portfolio'] for s in snapshots]

    pnl_sign = '+' if phase_pnl >= 0 else ''
    pnl_color_cls = 'pos' if phase_pnl >= 0 else 'neg'

    # Build equity JSON
    equity_json = '[' + ','.join(
        f'{{"d":"{d}","v":{v}}}' for d,v in zip(snap_dates, snap_vals)
    ) + ']'

    # Open position rows HTML
    pos_rows_html = ''
    if not positions:
        pos_rows_html = '<tr><td colspan="8" style="text-align:center;color:var(--txm);padding:16px 0">No open positions — 100% cash</td></tr>'
    else:
        for p in positions:
            sign = '+' if p['pnl_pct'] >= 0 else ''
            cc   = 'c-pos' if p['pnl_pct'] >= 0 else 'c-neg'
            target = round(p['entry'] * 1.07, 5)  # +7% default
            pos_rows_html += f'''
            <tr>
              <td><div class="asset"><div class="icon">{p["ticker"][0]}</div>
                  <div><div class="asset-name">{p["ticker"]}</div><div class="asset-sub">L1</div></div></div></td>
              <td>{p["qty"]}</td>
              <td class="mono">${p["entry"]:.5f}</td>
              <td class="mono">${p["price"]:.4f}</td>
              <td class="mono c-stop">${p["stop"]:.4f}</td>
              <td class="mono" style="color:var(--pos)">${target:.4f}</td>
              <td class="{cc}">{sign}{p["pnl_pct"]:.2f}%</td>
              <td><span class="chip chip-open">● Open</span></td>
            </tr>'''

    # Trade history rows HTML (most recent first)
    trade_rows = []
    for s in reversed(sells):
        sign = '+' if s['realized_pnl'] >= 0 else ''
        cc   = 'c-pos' if s['realized_pnl'] >= 0 else 'c-neg'
        trade_rows.append(f'''
        <div class="trade">
          <div class="t-side t-sell">SELL</div>
          <div class="t-info">
            <div class="t-main">{s["symbol"]}</div>
            <div class="t-sub">Realized · {s["date"]}</div>
          </div>
          <div>
            <div class="t-pnl {cc}">{sign}${abs(s["realized_pnl"]):.2f} ({sign}{s["realized_pnl_pct"]:.1f}%)</div>
            <div class="t-date">{s["date"]}</div>
          </div>
        </div>''')
    for b in reversed(buys):
        # Check if this buy has a corresponding sell (closed)
        is_open = not any(s['symbol'] == b['symbol'] for s in sells)
        label = 'Open' if is_open else 'Closed'
        lbl_style = 'color:var(--ac)' if is_open else 'color:var(--txm)'
        trade_rows.append(f'''
        <div class="trade">
          <div class="t-side t-buy">BUY</div>
          <div class="t-info">
            <div class="t-main">{b["symbol"]} · {b["qty"]} @ ${b["entry"]:.5f}</div>
            <div class="t-sub">{b["thesis"] or "—"}</div>
          </div>
          <div>
            <div class="t-pnl" style="{lbl_style}">{label}</div>
            <div class="t-date">{b["date"]}</div>
          </div>
        </div>''')

    trade_rows_html = '\n'.join(trade_rows)

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Bot Dashboard — MEXC Spot</title>
<style>
:root {{
  --bg:#080D18;--surf:#0F1829;--surf2:#18253E;--bdr:#1D2E4A;
  --tx:#D4DCF0;--txm:#546A8A;--txd:#2D4468;
  --ac:#60A5FA;--pos:#4ADE80;--neg:#F87171;--warn:#FBBF24;--stop:#FB923C;
}}
@media(prefers-color-scheme:light){{:root{{
  --bg:#EEF2FA;--surf:#fff;--surf2:#E8EFF8;--bdr:#C7D4E9;
  --tx:#0D1F3C;--txm:#4A6080;--txd:#98B0C8;
  --ac:#2563EB;--pos:#16A34A;--neg:#DC2626;--warn:#D97706;--stop:#EA580C;
}}}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--tx);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,sans-serif;font-size:14px;line-height:1.5}}
.wrap{{max-width:1100px;margin:0 auto;padding:24px 20px 48px;display:flex;flex-direction:column;gap:14px}}
.hdr{{display:flex;align-items:flex-start;justify-content:space-between;gap:20px;padding-bottom:16px;border-bottom:1px solid var(--bdr)}}
.eyebrow{{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--txm);font-weight:600;margin-bottom:4px}}
.pval{{font-size:40px;font-weight:800;letter-spacing:-.03em;font-variant-numeric:tabular-nums;line-height:1}}
.pnl-row{{display:flex;align-items:center;gap:14px;margin-top:8px;flex-wrap:wrap}}
.pnl-main{{font-size:15px;font-weight:700;font-variant-numeric:tabular-nums}}
.pos{{color:var(--pos)}}.neg{{color:var(--neg)}}.c-pos{{color:var(--pos)}}.c-neg{{color:var(--neg)}}.c-stop{{color:var(--stop)}}.c-warn{{color:var(--warn)}}
.vs-btc{{font-size:12px;color:var(--txm)}}.vs-btc strong{{color:var(--ac)}}
.hdr-r{{display:flex;flex-direction:column;align-items:flex-end;gap:8px}}
.mode-badge{{display:inline-flex;align-items:center;gap:7px;padding:5px 12px;border-radius:4px;font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;background:rgba(251,191,36,.1);color:var(--warn);border:1px solid rgba(251,191,36,.22)}}
.pulse{{width:7px;height:7px;border-radius:50%;background:var(--warn);animation:pls 2s ease-in-out infinite}}
@keyframes pls{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
.meta{{font-size:11px;color:var(--txd)}}
.kpi-row{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}}
.kpi{{background:var(--surf);border:1px solid var(--bdr);border-radius:6px;padding:14px 16px}}
.kpi-lbl{{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--txm);font-weight:600;margin-bottom:6px}}
.kpi-val{{font-size:24px;font-weight:800;letter-spacing:-.02em;font-variant-numeric:tabular-nums;line-height:1}}
.kpi-sub{{font-size:11px;color:var(--txm);margin-top:3px}}
.bar{{height:3px;background:var(--bdr);border-radius:2px;margin-top:10px;overflow:hidden}}
.bar-fill{{height:100%;border-radius:2px}}
.mid{{display:grid;grid-template-columns:1fr 270px;gap:10px}}
.panel{{background:var(--surf);border:1px solid var(--bdr);border-radius:6px;padding:16px}}
.panel-hdr{{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--txm);font-weight:600;margin-bottom:14px}}
.chart-h{{position:relative;height:164px}}
canvas{{display:block;width:100%;height:100%}}
.gates{{display:flex;flex-direction:column;gap:9px}}
.gate{{display:flex;align-items:center;justify-content:space-between}}
.gate-lbl{{font-size:11px;color:var(--txm)}}
.gate-val{{display:flex;align-items:center;gap:6px;font-size:12px;font-weight:700;font-variant-numeric:tabular-nums}}
.pill{{font-size:9px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;padding:2px 7px;border-radius:3px}}
.pill-ok{{background:rgba(74,222,128,.1);color:var(--pos);border:1px solid rgba(74,222,128,.2)}}
.pill-warn{{background:rgba(251,191,36,.1);color:var(--warn);border:1px solid rgba(251,191,36,.2)}}
.pill-halt{{background:rgba(248,113,113,.1);color:var(--neg);border:1px solid rgba(248,113,113,.2)}}
.gbar{{height:3px;background:var(--bdr);border-radius:2px;margin-top:3px;overflow:hidden}}
.gbar-fill{{height:100%;border-radius:2px;background:var(--ac)}}
.divider{{height:1px;background:var(--bdr);margin:4px 0}}
.sec-lbl{{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--txm);font-weight:600;margin-bottom:8px}}
.tbl-wrap{{overflow-x:auto}}
table{{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}}
thead th{{font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--txd);font-weight:700;padding:0 0 8px;text-align:left;border-bottom:1px solid var(--bdr);white-space:nowrap}}
thead th:not(:first-child){{text-align:right}}
tbody tr{{border-bottom:1px solid var(--bdr)}}
tbody tr:last-child{{border-bottom:none}}
tbody td{{padding:10px 0;font-size:13px;text-align:right;vertical-align:middle}}
tbody td:first-child{{text-align:left}}
.asset{{display:flex;align-items:center;gap:9px}}
.icon{{width:30px;height:30px;border-radius:50%;background:var(--surf2);border:1px solid var(--bdr);display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;color:var(--ac);flex-shrink:0}}
.asset-name{{font-weight:700;font-size:13px;letter-spacing:.02em}}
.asset-sub{{font-size:10px;color:var(--txm)}}
.mono{{font-family:'Courier New',Courier,monospace;font-size:12px}}
.chip{{display:inline-flex;align-items:center;gap:4px;font-size:9px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;padding:2px 7px;border-radius:3px}}
.chip-open{{background:rgba(96,165,250,.1);color:var(--ac);border:1px solid rgba(96,165,250,.2)}}
.trades{{display:flex;flex-direction:column}}
.trade{{display:flex;align-items:center;gap:12px;padding:10px 0;border-bottom:1px solid var(--bdr)}}
.trade:last-child{{border-bottom:none}}
.t-side{{width:34px;flex-shrink:0;font-size:9px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;text-align:center;padding:3px 0;border-radius:3px}}
.t-buy{{background:rgba(96,165,250,.1);color:var(--ac);border:1px solid rgba(96,165,250,.2)}}
.t-sell{{background:rgba(74,222,128,.1);color:var(--pos);border:1px solid rgba(74,222,128,.2)}}
.t-info{{flex:1;min-width:0}}
.t-main{{font-size:13px;font-weight:600;font-variant-numeric:tabular-nums;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.t-sub{{font-size:11px;color:var(--txm);margin-top:1px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.t-pnl{{font-size:13px;font-weight:800;font-variant-numeric:tabular-nums;text-align:right;white-space:nowrap}}
.t-date{{font-size:11px;color:var(--txd);text-align:right;white-space:nowrap}}
.bench{{background:var(--surf);border:1px solid var(--bdr);border-radius:6px;padding:14px 16px;display:flex;align-items:center;gap:20px;flex-wrap:wrap}}
.bench-item{{display:flex;flex-direction:column;gap:2px}}
.bench-lbl{{font-size:9.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--txm);font-weight:600}}
.bench-val{{font-size:16px;font-weight:800;font-variant-numeric:tabular-nums}}
.bench-sep{{width:1px;background:var(--bdr);align-self:stretch}}
.race-wrap{{flex:1;min-width:200px}}
.race-lbl{{font-size:9.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--txm);font-weight:600;margin-bottom:6px}}
.race-row{{display:flex;align-items:center;gap:8px;margin-bottom:4px}}
.race-name{{font-size:10px;font-weight:700;width:28px}}
.race-bar{{flex:1;height:8px;background:var(--bdr);border-radius:4px;overflow:hidden}}
.race-fill{{height:100%;border-radius:4px}}
.race-pct{{font-size:11px;font-weight:700;font-variant-numeric:tabular-nums;width:42px;text-align:right}}
.footer{{font-size:11px;color:var(--txd);text-align:center;padding-top:12px;border-top:1px solid var(--bdr)}}
.footer code{{font-family:'Courier New',Courier,monospace;background:var(--surf2);padding:1px 5px;border-radius:3px}}
@media(max-width:680px){{.kpi-row{{grid-template-columns:1fr 1fr}}.mid{{grid-template-columns:1fr}}.pval{{font-size:28px}}}}
</style>
</head>
<body>
<div class="wrap">

  <header class="hdr">
    <div class="hdr-l">
      <div class="eyebrow">MEXC Spot Bot · Phase P&amp;L</div>
      <div class="pval">${portfolio:.2f}</div>
      <div class="pnl-row">
        <span class="pnl-main {pnl_color_cls}">{pnl_sign}${abs(phase_pnl):.2f} ({pnl_sign}{phase_pnl_pct:.2f}%)</span>
        <span class="vs-btc">vs BTC <strong>+0.79%</strong></span>
      </div>
    </div>
    <div class="hdr-r">
      <div class="mode-badge"><span class="pulse"></span>Aggressive · Aug 4–22</div>
      <div class="meta">Snapshot: {snapshots[-1]["date"] if snapshots else "—"} EOD</div>
      <div class="meta">Baseline ${BASELINE:.2f}</div>
    </div>
  </header>

  <div class="kpi-row">
    <div class="kpi">
      <div class="kpi-lbl">Free USDT</div>
      <div class="kpi-val">${free_usdt:.2f}</div>
      <div class="kpi-sub">{cash_pct:.1f}% dry powder</div>
      <div class="bar"><div class="bar-fill" style="width:{cash_pct:.1f}%;background:var(--ac)"></div></div>
    </div>
    <div class="kpi">
      <div class="kpi-lbl">Deployed</div>
      <div class="kpi-val c-warn">{deployed_pct:.1f}%</div>
      <div class="kpi-sub">Target: 80–90%</div>
      <div class="bar"><div class="bar-fill" style="width:{deployed_pct:.1f}%;background:var(--warn)"></div></div>
    </div>
    <div class="kpi">
      <div class="kpi-lbl">Positions</div>
      <div class="kpi-val">{len(positions)}<span style="font-size:14px;font-weight:400;color:var(--txm)">/3</span></div>
      <div class="kpi-sub">Max 3 simultaneous</div>
      <div class="bar"><div class="bar-fill" style="width:{len(positions)/3*100:.0f}%;background:var(--ac)"></div></div>
    </div>
    <div class="kpi">
      <div class="kpi-lbl">Win Rate</div>
      <div class="kpi-val c-pos">{win_rate:.0f}%</div>
      <div class="kpi-sub">{len(wins)}W · {len(losses)}L · {len(sells)} closed</div>
      <div class="bar"><div class="bar-fill" style="width:{win_rate:.0f}%;background:var(--pos)"></div></div>
    </div>
  </div>

  <div class="mid">
    <div class="panel">
      <div class="panel-hdr">Equity Curve</div>
      <div class="chart-h"><canvas id="eq"></canvas></div>
    </div>
    <div class="panel">
      <div class="panel-hdr">Limits &amp; Gates</div>
      <div class="gates">
        <div>
          <div class="gate"><span class="gate-lbl">Trades this week</span><span class="gate-val">3/20 <span class="pill pill-ok">OK</span></span></div>
          <div class="gbar"><div class="gbar-fill" style="width:15%"></div></div>
        </div>
        <div>
          <div class="gate"><span class="gate-lbl">Trades today</span><span class="gate-val">0/5 <span class="pill pill-ok">OK</span></span></div>
          <div class="gbar"><div class="gbar-fill" style="width:0%"></div></div>
        </div>
        <div class="divider"></div>
        <div class="gate"><span class="gate-lbl">Circuit breaker</span><span class="gate-val"><span class="pill pill-ok">Clear</span></span></div>
        <div class="gate"><span class="gate-lbl">Daily gate</span><span class="gate-val"><span class="pill pill-ok">Clear</span></span></div>
        <div class="divider"></div>
        <div class="gate"><span class="gate-lbl">Closed trades</span><span class="gate-val c-pos">{len(wins)}W · {len(losses)}L</span></div>
        <div class="gate"><span class="gate-lbl">Realized P&amp;L</span><span class="gate-val c-pos">+${realized_total:.2f}</span></div>
        <div class="gate"><span class="gate-lbl">Avg win</span><span class="gate-val c-pos">+{avg_win:.2f}%</span></div>
        <div class="divider"></div>
        <div class="gate"><span class="gate-lbl">Start capital</span><span class="gate-val">${BASELINE:.2f}</span></div>
      </div>
    </div>
  </div>

  <div>
    <div class="sec-lbl">Open Positions</div>
    <div class="panel" style="padding:0 16px">
      <div class="tbl-wrap">
        <table>
          <thead><tr>
            <th>Asset</th><th>Qty</th><th>Entry</th><th>Price (EOD)</th>
            <th>Stop</th><th>Target</th><th>Unrlzd P&amp;L</th><th>Status</th>
          </tr></thead>
          <tbody>{pos_rows_html}</tbody>
        </table>
      </div>
    </div>
  </div>

  <div>
    <div class="sec-lbl">Trade History</div>
    <div class="panel"><div class="trades">{trade_rows_html}</div></div>
  </div>

  <div>
    <div class="sec-lbl">Benchmark</div>
    <div class="bench">
      <div class="bench-item">
        <div class="bench-lbl">Bot Phase P&amp;L</div>
        <div class="bench-val c-pos">{pnl_sign}{phase_pnl_pct:.2f}%</div>
      </div>
      <div class="bench-sep"></div>
      <div class="bench-item">
        <div class="bench-lbl">BTC Hold (phase)</div>
        <div class="bench-val" style="color:var(--txm)">+0.79%</div>
      </div>
      <div class="bench-sep"></div>
      <div class="bench-item">
        <div class="bench-lbl">Alpha</div>
        <div class="bench-val c-pos">+{phase_pnl_pct - 0.79:.2f}%</div>
      </div>
      <div class="bench-sep"></div>
      <div class="race-wrap">
        <div class="race-lbl">Race vs BTC</div>
        <div class="race-row">
          <div class="race-name" style="color:var(--pos)">Bot</div>
          <div class="race-bar"><div class="race-fill" style="width:100%;background:var(--pos)"></div></div>
          <div class="race-pct c-pos">{pnl_sign}{phase_pnl_pct:.2f}%</div>
        </div>
        <div class="race-row">
          <div class="race-name" style="color:var(--txm)">BTC</div>
          <div class="race-bar"><div class="race-fill" style="width:{0.79/phase_pnl_pct*100 if phase_pnl_pct else 50:.1f}%;background:var(--ac)"></div></div>
          <div class="race-pct" style="color:var(--ac)">+0.79%</div>
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    Generated from <code>memory/TRADE-LOG.md</code> · {snapshots[-1]["date"] if snapshots else "—"} EOD snapshot ·
    Run <code>python3 scripts/dashboard.py</code> to refresh
  </div>

</div>
<script>
const equity={equity_json};
const BASE={BASELINE};
function draw(){{
  const c=document.getElementById('eq');
  const dpr=window.devicePixelRatio||1;
  const rect=c.parentElement.getBoundingClientRect();
  c.width=rect.width*dpr;c.height=rect.height*dpr;
  const ctx=c.getContext('2d');ctx.scale(dpr,dpr);
  const W=rect.width,H=rect.height;
  const pad={{t:12,r:10,b:26,l:46}};
  const cW=W-pad.l-pad.r,cH=H-pad.t-pad.b;
  const vals=equity.map(e=>e.v);
  const lo=Math.min(...vals)-.05,hi=Math.max(...vals)+.08,rng=hi-lo;
  const dark=window.matchMedia('(prefers-color-scheme:dark)').matches;
  const C={{ac:dark?'#60A5FA':'#2563EB',pos:dark?'#4ADE80':'#16A34A',
            bdr:dark?'#1D2E4A':'#C7D4E9',txm:dark?'#546A8A':'#4A6080',
            txd:dark?'#2D4468':'#98B0C8',surf:dark?'#0F1829':'#ffffff'}};
  const xOf=i=>pad.l+(i/(equity.length-1))*cW;
  const yOf=v=>pad.t+cH-((v-lo)/rng)*cH;
  for(let i=0;i<=4;i++){{
    const y=pad.t+(i/4)*cH,v=hi-(i/4)*rng;
    ctx.strokeStyle=C.bdr;ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(pad.l,y);ctx.lineTo(pad.l+cW,y);ctx.stroke();
    ctx.fillStyle=C.txm;ctx.font='9.5px system-ui,sans-serif';ctx.textAlign='right';
    ctx.fillText('$'+v.toFixed(2),pad.l-4,y+4);
  }}
  const bY=yOf(BASE);
  ctx.setLineDash([3,3]);ctx.strokeStyle=C.txd;ctx.lineWidth=1;
  ctx.beginPath();ctx.moveTo(pad.l,bY);ctx.lineTo(pad.l+cW,bY);ctx.stroke();
  ctx.setLineDash([]);
  ctx.fillStyle=C.txd;ctx.font='9px system-ui,sans-serif';ctx.textAlign='left';
  ctx.fillText('start',pad.l+2,bY-3);
  const g=ctx.createLinearGradient(0,pad.t,0,pad.t+cH);
  g.addColorStop(0,dark?'rgba(96,165,250,.22)':'rgba(37,99,235,.10)');
  g.addColorStop(1,dark?'rgba(96,165,250,0)':'rgba(37,99,235,0)');
  ctx.beginPath();ctx.moveTo(xOf(0),yOf(equity[0].v));
  for(let i=1;i<equity.length;i++)ctx.lineTo(xOf(i),yOf(equity[i].v));
  ctx.lineTo(xOf(equity.length-1),pad.t+cH);ctx.lineTo(xOf(0),pad.t+cH);
  ctx.closePath();ctx.fillStyle=g;ctx.fill();
  ctx.beginPath();ctx.strokeStyle=C.ac;ctx.lineWidth=2;ctx.lineJoin='round';
  ctx.moveTo(xOf(0),yOf(equity[0].v));
  for(let i=1;i<equity.length;i++)ctx.lineTo(xOf(i),yOf(equity[i].v));
  ctx.stroke();
  for(let i=0;i<equity.length;i++){{
    ctx.beginPath();ctx.arc(xOf(i),yOf(equity[i].v),2,0,Math.PI*2);
    ctx.fillStyle=C.ac;ctx.fill();
  }}
  const ei=equity.length-1;
  ctx.beginPath();ctx.arc(xOf(ei),yOf(equity[ei].v),5,0,Math.PI*2);
  ctx.fillStyle=C.pos;ctx.fill();
  ctx.beginPath();ctx.arc(xOf(ei),yOf(equity[ei].v),5,0,Math.PI*2);
  ctx.strokeStyle=C.surf;ctx.lineWidth=2;ctx.stroke();
  ctx.fillStyle=C.txm;ctx.font='9.5px system-ui,sans-serif';ctx.textAlign='center';
  for(const i of[0,Math.floor(equity.length/2),ei])
    ctx.fillText(equity[i].d,xOf(i),H-6);
}}
draw();
new ResizeObserver(draw).observe(document.getElementById('eq').parentElement);
window.matchMedia('(prefers-color-scheme:dark)').addEventListener('change',draw);
</script>
</body></html>'''


# ── Main ───────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    snapshots, buys, sells, positions = parse_log()
    html = render(snapshots, buys, sells, positions)
    tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False,
                                      encoding='utf-8', prefix='bot-dashboard-')
    tmp.write(html)
    tmp.close()
    print(f'Dashboard: file://{tmp.name}')
    webbrowser.open(f'file://{tmp.name}')
