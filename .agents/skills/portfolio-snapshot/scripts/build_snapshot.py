#!/usr/bin/env python3
"""
portfolio-snapshot generator (deterministic, pure stdlib).

Reads the live tracker note, extracts ONLY the Holdings table, bakes the
holdings bar chart to static SVG (faithfully porting the chart math in
"Live Portfolio.md"), and writes a stripped snapshot note plus its SVG
asset(s) into the Portfolio Snapshot folder. The scatter chart is opt-in
(--scatter); by default only the bar chart is emitted.

Everything that is instruction/engine/log — the refresh dataviewjs block, the
`[!tip]` callouts, Upcoming Earnings, Column Legend, Notes, Log — is dropped.
The source note is NEVER modified (read-only on the source).

Section order in the snapshot: Trades (empty) FIRST, then Holdings, then Charts.

Modeled on `.agents/skills/graph/scripts/generate_graph.py`: the script writes files
directly so large SVG never streams through a model response.

Usage:
  python3 build_snapshot.py [--source "Live Portfolio.md"]
                            [--out-dir "Portfolio Snapshot"]
                            [--date YYYY-MM-DD] [--time HH:MM]
                            [--mode dated|single]
                            [--bar-metric "Return 1M"]
                            [--scatter] [--scatter-x "Rev Gr CFY"] [--scatter-y "EV/EBIT NTM"]
"""

import argparse
import datetime
import math
import os
import re
import sys

# --------------------------------------------------------------------------
# Table extraction
# --------------------------------------------------------------------------
TABLE_RE = re.compile(r"<!--TABLE-START-->([\s\S]*?)<!--TABLE-END-->")

# Column indices AFTER dropping the empty cells around the outer pipes.
# 0 #  1 Stock  2 Ticker  3 Exchange  4 Weight  5 Price
# 6 1W 7 1M 8 3M 9 1Y  10 PE-LTM 11 PE-NTM  12 EVEBIT-LTM 13 EVEBIT-NTM
# 14 ROIC-LTM 15 ROIC-NTM  16 RevGr-LFY 17 RevGr-CFY  18 EPSGr-LFY 19 EPSGr-CFY
BAR_METRICS = {
    "Return 1W":   (6,  "%", True),
    "Return 1M":   (7,  "%", True),
    "Return 3M":   (8,  "%", True),
    "Return 1Y":   (9,  "%", True),
    "P/E NTM":     (11, "x", False),
    "P/E LTM":     (10, "x", False),
    "EV/EBIT NTM": (13, "x", False),
    "EV/EBIT LTM": (12, "x", False),
    "Rev Gr CFY":  (17, "%", True),
    "EPS Gr CFY":  (19, "%", True),
    "Rev Gr LFY":  (16, "%", True),
    "EPS Gr LFY":  (18, "%", True),
}
SCATTER_METRICS = {
    "Rev Gr CFY":  (17, "%"),
    "Rev Gr LFY":  (16, "%"),
    "EPS Gr CFY":  (19, "%"),
    "EPS Gr LFY":  (18, "%"),
    "P/E NTM":     (11, "x"),
    "P/E LTM":     (10, "x"),
    "EV/EBIT NTM": (13, "x"),
    "EV/EBIT LTM": (12, "x"),
    "ROIC NTM":    (15, "%"),
    "ROIC LTM":    (14, "%"),
}
# Weight tiers — colour + dot radius, mirroring the scatter block.
TIERS = [
    ("Full",   re.compile(r"^Full"),   "#d4504e", 8),
    ("High",   re.compile(r"^High"),   "#e08c3b", 7),
    ("Medium", re.compile(r"^Medium"), "#3aa675", 6),
    ("Low",    re.compile(r"^Low"),    "#8a8f98", 5),
]


def parse_table(md):
    """Return (raw_table_markdown, [row_cells,...]). Fails loudly if absent."""
    m = TABLE_RE.search(md)
    if not m:
        sys.exit("ERROR: Holdings markers <!--TABLE-START--> / <!--TABLE-END--> "
                 "not found in source. Is this the Live Portfolio tracker?")
    raw = m.group(1).strip()
    rows = []
    for line in m.group(1).split("\n"):
        s = line.strip()
        if not s.startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.split("|")][1:-1]  # drop outer-pipe empties
        if len(cells) < 20 or cells[1] == "Stock":
            continue
        rows.append(cells)
    if not rows:
        sys.exit("ERROR: Holdings table found but contains no data rows.")
    return raw, rows


# --------------------------------------------------------------------------
# Numeric helpers (ported 1:1 from the dataviewjs chart blocks)
# --------------------------------------------------------------------------
def parse_num(s):
    if s is None:
        return None
    t = re.sub(r"[+%x]", "", s.replace(",", "")).strip()
    if t in ("", "—", "-"):
        return None
    try:
        v = float(t)
    except ValueError:
        return None
    return v if math.isfinite(v) else None


def jsround(x):
    """JS Math.round: round-half-up toward +inf (Python's round is banker's)."""
    return math.floor(x + 0.5)


def pctile(arr, p):
    if not arr:
        return 0.0
    s = sorted(arr)
    return s[min(len(s) - 1, jsround(p * (len(s) - 1)))]


def median(arr):
    return pctile(arr, 0.5)


def fence(vals):
    """Tukey IQR fence -> robust axis domain."""
    q1, q3 = pctile(vals, 0.25), pctile(vals, 0.75)
    iqr = q3 - q1
    lo = max(min(vals), q1 - 1.5 * iqr)
    hi = min(max(vals), q3 + 1.5 * iqr)
    if lo == hi:
        lo -= 1
        hi += 1
    pad = (hi - lo) * 0.08
    return (lo - pad, hi + pad)


def tier_of(w):
    w = (w or "").replace("<br>", " ").strip()
    for name, rx, color, r in TIERS:
        if rx.search(w):
            return (name, color, r)
    return TIERS[3][0], TIERS[3][2], TIERS[3][3]  # default Low


def fmt_val(v, unit):
    """Scatter formatter: % -> 0dp, x -> 1dp (0dp above 1000)."""
    if v is None:
        return "—"
    if unit == "%":
        return ("+" if v >= 0 else "") + f"{v:.0f}%"
    return (f"{v:.0f}" if abs(v) >= 1000 else f"{v:.1f}") + "x"


def fmt_bar(v, unit):
    """Bar formatter: % -> 1dp, x -> 1dp (0dp above 1000)."""
    if v is None:
        return "—"
    if unit == "%":
        return ("+" if v >= 0 else "") + f"{v:.1f}%"
    return (f"{v:.0f}" if abs(v) >= 1000 else f"{v:.1f}") + "x"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


FONT = "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"


# --------------------------------------------------------------------------
# Bar chart -> static SVG (the live block renders HTML divs; we render SVG)
# --------------------------------------------------------------------------
def build_bar_svg(rows, metric):
    if metric not in BAR_METRICS:
        sys.exit(f"ERROR: unknown --bar-metric '{metric}'. "
                 f"Options: {', '.join(BAR_METRICS)}")
    idx, unit, sign = BAR_METRICS[metric]
    series = [(r[1], parse_num(r[idx])) for r in rows]
    present = [(n, v) for (n, v) in series if v is not None]
    missing = [(n, v) for (n, v) in series if v is None]
    present.sort(key=lambda t: t[1], reverse=True)     # high -> low
    ordered = present + missing

    W, pad = 720, 16
    title_h, bar_h, row_gap, cap_h = 34, 16, 4, 40
    label_w, col_gap, value_w = 150, 10, 70
    track_x = pad + label_w + col_gap
    value_x = W - pad - value_w
    track_w = value_x - col_gap - track_x
    n = len(ordered)
    H = title_h + n * (bar_h + row_gap) + cap_h + pad

    cap = max(pctile([abs(v) for (_, v) in present], 0.90), 1e-9) if present else 1e-9
    has_neg = any(v < 0 for (_, v) in present)

    GREEN, RED, ACC = "#3aa675", "#c0504d", "#5b6bf0"

    def color_of(v):
        if sign:
            return GREEN if v >= 0 else RED
        return ACC if v >= 0 else RED

    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="{W}" height="{H}" font-family="{FONT}">']
    p.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="10" '
             f'fill="#ffffff" stroke="#e2e2e7"/>')
    p.append(f'<text x="{pad}" y="22" font-size="14" font-weight="600" '
             f'fill="#1f2430">{esc("Holdings — " + metric)}</text>')

    center = track_x + track_w / 2
    for i, (name, v) in enumerate(ordered):
        cy = title_h + i * (bar_h + row_gap)
        ty = cy + bar_h - 4
        p.append(f'<text x="{track_x - col_gap}" y="{ty}" font-size="11.5" '
                 f'text-anchor="end" fill="#1f2430">{esc(name)}</text>')
        p.append(f'<rect x="{track_x}" y="{cy}" width="{track_w}" height="{bar_h}" '
                 f'rx="3" fill="#eceef2"/>')
        if v is not None:
            frac = min(abs(v), cap) / cap
            col = color_of(v)
            if has_neg:
                half = frac * (track_w / 2)
                bx = center if v >= 0 else center - half
                p.append(f'<rect x="{bx:.2f}" y="{cy}" width="{half:.2f}" '
                         f'height="{bar_h}" fill="{col}"/>')
                p.append(f'<line x1="{center:.2f}" y1="{cy}" x2="{center:.2f}" '
                         f'y2="{cy + bar_h}" stroke="#b8bcc4" stroke-width="1"/>')
            else:
                p.append(f'<rect x="{track_x}" y="{cy}" width="{frac * track_w:.2f}" '
                         f'height="{bar_h}" rx="3" fill="{col}"/>')
        val = fmt_bar(v, unit)
        vcol = "#9aa0ab" if v is None else "#5b6270"
        p.append(f'<text x="{value_x}" y="{ty}" font-size="11.5" fill="{vcol}">{esc(val)}</text>')

    note = (f"{metric} · {len(present)} holdings"
            + (f" (+{len(missing)} with no data)" if missing else "")
            + f" · bars scaled to {fmt_bar(cap, unit)}; outliers max out, "
              f"labels show true values"
            + (" · diverging from a zero center line" if has_neg else ""))
    p.append(f'<text x="{pad}" y="{title_h + n * (bar_h + row_gap) + 20}" '
             f'font-size="10.5" fill="#8a8f98">{esc(note)}</text>')
    p.append("</svg>")
    return "\n".join(p)


# --------------------------------------------------------------------------
# Scatter chart -> static SVG (faithful port of the live SVG block; opt-in)
# --------------------------------------------------------------------------
def build_scatter_svg(rows, xk, yk):
    for k in (xk, yk):
        if k not in SCATTER_METRICS:
            sys.exit(f"ERROR: unknown scatter metric '{k}'. "
                     f"Options: {', '.join(SCATTER_METRICS)}")
    xi, xunit = SCATTER_METRICS[xk]
    yi, yunit = SCATTER_METRICS[yk]
    pts = []
    for r in rows:
        x, y = parse_num(r[xi]), parse_num(r[yi])
        if x is None or y is None:
            continue
        pts.append({"name": r[1], "ticker": r[2], "tier": tier_of(r[4]), "x": x, "y": y})
    dropped = len(rows) - len(pts)

    W = 720
    title_h, legend_h, caption_h = 30, 26, 34
    Hp, mL, mR, mT, mB = 470, 60, 18, 16, 54
    plotW, plotH = W - mL - mR, Hp - mT - mB
    oy = title_h
    H = title_h + Hp + legend_h + caption_h

    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="{W}" height="{H}" font-family="{FONT}">']
    p.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="10" '
             f'fill="#ffffff" stroke="#e2e2e7"/>')
    p.append(f'<text x="16" y="21" font-size="14" font-weight="600" fill="#1f2430">'
             f'{esc(f"Scatter — {xk} vs {yk}")}</text>')

    if len(pts) < 2:
        p.append(f'<text x="16" y="{oy + 40}" font-size="12" fill="#8a8f98">'
                 f'Not enough data for this pair — refresh the live tracker first.</text>')
        p.append("</svg>")
        return "\n".join(p)

    xs = [q["x"] for q in pts]
    ys = [q["y"] for q in pts]
    xDom, yDom = fence(xs), fence(ys)

    def clamp(v, d):
        return max(d[0], min(d[1], v))

    def sx(v):
        return mL + (clamp(v, xDom) - xDom[0]) / (xDom[1] - xDom[0]) * plotW

    def sy(v):
        return oy + mT + plotH - (clamp(v, yDom) - yDom[0]) / (yDom[1] - yDom[0]) * plotH

    GRID, TXT, AXIS = "#dcdfe4", "#6b7280", "#b8bcc4"
    p.append(f'<rect x="{mL}" y="{oy + mT}" width="{plotW}" height="{plotH}" '
             f'fill="none" stroke="{GRID}" stroke-width="1"/>')

    for i in range(5):
        xv = xDom[0] + (xDom[1] - xDom[0]) * i / 4
        px = mL + plotW * i / 4
        p.append(f'<line x1="{px:.2f}" y1="{oy + mT}" x2="{px:.2f}" '
                 f'y2="{oy + mT + plotH}" stroke="{GRID}" stroke-width="0.5" '
                 f'stroke-dasharray="2 3"/>')
        p.append(f'<text x="{px:.2f}" y="{oy + mT + plotH + 16}" fill="{TXT}" '
                 f'font-size="10" text-anchor="middle">{esc(fmt_val(xv, xunit))}</text>')
        yv = yDom[0] + (yDom[1] - yDom[0]) * i / 4
        py = oy + mT + plotH - plotH * i / 4
        p.append(f'<line x1="{mL}" y1="{py:.2f}" x2="{mL + plotW}" y2="{py:.2f}" '
                 f'stroke="{GRID}" stroke-width="0.5" stroke-dasharray="2 3"/>')
        p.append(f'<text x="{mL - 6}" y="{py + 3:.2f}" fill="{TXT}" font-size="10" '
                 f'text-anchor="end">{esc(fmt_val(yv, yunit))}</text>')

    mx, my = sx(median(xs)), sy(median(ys))
    p.append(f'<line x1="{mx:.2f}" y1="{oy + mT}" x2="{mx:.2f}" y2="{oy + mT + plotH}" '
             f'stroke="{AXIS}" stroke-width="1" stroke-dasharray="5 4" opacity="0.7"/>')
    p.append(f'<line x1="{mL}" y1="{my:.2f}" x2="{mL + plotW}" y2="{my:.2f}" '
             f'stroke="{AXIS}" stroke-width="1" stroke-dasharray="5 4" opacity="0.7"/>')

    for q in pts:
        cx, cy = sx(q["x"]), sy(q["y"])
        off = (q["x"] < xDom[0] or q["x"] > xDom[1] or q["y"] < yDom[0] or q["y"] > yDom[1])
        _, color, r = q["tier"]
        stroke = "#1f2430" if off else "#ffffff"
        dash = ' stroke-dasharray="2 2"' if off else ""
        p.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" fill="{color}" '
                 f'fill-opacity="0.78" stroke="{stroke}" '
                 f'stroke-width="{1.5 if off else 1}"{dash}>'
                 f'<title>{esc(q["name"])} ({esc(q["ticker"])})\n'
                 f'{esc(xk)}: {esc(fmt_val(q["x"], xunit))}\n'
                 f'{esc(yk)}: {esc(fmt_val(q["y"], yunit))}</title></circle>')
        p.append(f'<text x="{cx + r + 2:.2f}" y="{cy + 3:.2f}" fill="#1f2430" '
                 f'font-size="9.5">{esc(q["ticker"])}</text>')

    # Axis titles
    p.append(f'<text x="{mL + plotW / 2:.2f}" y="{oy + Hp - 6}" fill="#1f2430" '
             f'font-size="12" font-weight="600" text-anchor="middle">{esc(xk)}</text>')
    ymid = oy + mT + plotH / 2
    p.append(f'<text x="15" y="{ymid:.2f}" fill="#1f2430" font-size="12" '
             f'font-weight="600" text-anchor="middle" '
             f'transform="rotate(-90 15 {ymid:.2f})">{esc(yk)}</text>')

    # Legend
    lx, ly = mL, title_h + Hp + 16
    for name, rx, color, r in TIERS:
        p.append(f'<circle cx="{lx + 6:.2f}" cy="{ly - 4:.2f}" r="5" fill="{color}"/>')
        p.append(f'<text x="{lx + 16:.2f}" y="{ly:.2f}" font-size="11" fill="{TXT}">{esc(name)}</text>')
        lx += 20 + 12 + len(name) * 7

    cap = (f"{len(pts)} holdings"
           + (f" ({dropped} missing a value, omitted)" if dropped else "")
           + " · dashed crosshair = medians (quadrants) · dot size/colour = "
             "weight tier · axes clipped to the IQR fence; ringed dots are "
             "off-scale, pinned to the edge")
    p.append(f'<text x="16" y="{title_h + Hp + legend_h + 20}" font-size="10.5" '
             f'fill="#8a8f98">{esc(cap)}</text>')
    p.append("</svg>")
    return "\n".join(p)


# --------------------------------------------------------------------------
# Snapshot assembly
# --------------------------------------------------------------------------
def build_note(raw_table, date_iso, ddmmyyyy, stamp, chart_names, source_basename):
    src_link = os.path.splitext(source_basename)[0]  # wikilink target w/o .md
    fm = [
        "---",
        "Publish_Snapshot: true",
        f"date: {date_iso}",
        f'snapshot_of: "[[{src_link}]]"',
        "tags:",
        "  - portfolio",
        "  - snapshot",
        "status: active",
        "---",
    ]
    # Section order: Trades FIRST (user fills it), then Holdings, then Charts.
    body = [
        f"# Portfolio Snapshot — {ddmmyyyy}",
        "",
        f"*Snapshot of [[{src_link}]] as of {stamp}. Static export — the live "
        f"tracker remains the source of truth.*",
        "",
        "## Trades",
        "",
        "## Holdings",
        "",
        raw_table,
        "",
    ]
    if chart_names:
        body.append("## Charts")
        body.append("")
        for cn in chart_names:
            body.append(f"![[{cn}]]")
            body.append("")
    return "\n".join(fm) + "\n" + "\n".join(body) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Build a static Portfolio Snapshot.")
    ap.add_argument("--source", default="Live Portfolio.md")
    ap.add_argument("--out-dir", default="Portfolio Snapshot")
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    ap.add_argument("--time", default=None, help="HH:MM (default: now)")
    ap.add_argument("--mode", choices=["dated", "single"], default="dated")
    ap.add_argument("--bar-metric", default="Return 1M")
    ap.add_argument("--scatter", action="store_true",
                    help="also emit the scatter chart (omitted by default)")
    ap.add_argument("--scatter-x", default="Rev Gr CFY")
    ap.add_argument("--scatter-y", default="EV/EBIT NTM")
    args = ap.parse_args()

    if not os.path.isfile(args.source):
        sys.exit(f"ERROR: source note not found: {args.source}")

    now = datetime.datetime.now()
    date_iso = args.date or now.strftime("%Y-%m-%d")
    try:
        d = datetime.datetime.strptime(date_iso, "%Y-%m-%d").date()
    except ValueError:
        sys.exit(f"ERROR: --date must be YYYY-MM-DD, got '{date_iso}'")
    ddmmyyyy = d.strftime("%d-%m-%Y")
    stamp = f"{date_iso} {args.time or now.strftime('%H:%M')}"

    with open(args.source, "r", encoding="utf-8") as f:
        md = f.read()
    raw_table, rows = parse_table(md)

    os.makedirs(args.out_dir, exist_ok=True)
    note_base = ddmmyyyy if args.mode == "dated" else "Portfolio Snapshot"
    bar_name = f"{note_base} - bar.svg"
    scatter_name = f"{note_base} - scatter.svg"
    bar_path = os.path.join(args.out_dir, bar_name)
    scatter_path = os.path.join(args.out_dir, scatter_name)
    note_path = os.path.join(args.out_dir, f"{note_base}.md")

    chart_names = []

    bar_svg = build_bar_svg(rows, args.bar_metric)
    with open(bar_path, "w", encoding="utf-8") as f:
        f.write(bar_svg + "\n")
    chart_names.append(bar_name)

    if args.scatter:
        scatter_svg = build_scatter_svg(rows, args.scatter_x, args.scatter_y)
        with open(scatter_path, "w", encoding="utf-8") as f:
            f.write(scatter_svg + "\n")
        chart_names.append(scatter_name)
    elif os.path.exists(scatter_path):
        # Remove a stale scatter asset left by an earlier run of this same snapshot.
        os.remove(scatter_path)

    note = build_note(raw_table, date_iso, ddmmyyyy, stamp, chart_names,
                      os.path.basename(args.source))
    with open(note_path, "w", encoding="utf-8") as f:
        f.write(note)

    # Concise machine-readable summary for the calling skill to relay.
    print("OK portfolio-snapshot")
    print(f"  source        : {args.source}")
    print(f"  holdings rows : {len(rows)}")
    print(f"  bar chart     : {args.bar_metric}")
    print(f"  scatter chart : "
          + (f"{args.scatter_x} (x) vs {args.scatter_y} (y)" if args.scatter else "omitted"))
    print(f"  note          : {note_path}")
    for cn in chart_names:
        print(f"  svg           : {os.path.join(args.out_dir, cn)}")


if __name__ == "__main__":
    main()
