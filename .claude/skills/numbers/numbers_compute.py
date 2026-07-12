#!/usr/bin/env python3
"""
numbers_compute.py — deterministic label→FMP-field mapping, delta computation,
and materiality classification for /numbers (Fix #4, 2026-07-08).

Scope is deliberately the bug-prone ARITHMETIC only (Step 3 map + Step 5 deltas
+ materiality). It emits the new RAW numeric value + the old value's format hint;
the LLM renders the final formatted cell, because currency preservation
(KRW/JPY/GBp/EUR, mixed conventions) carries correctness risk that must not be
hard-coded into thesis content. Fetch (Step 4 curl) and snapshot (Step 7) stay
in the skill; this script consumes the already-fetched JSON.

Usage:
  python3 numbers_compute.py --json-dir /tmp/numbers_NVDA --rows-file /tmp/rows.tsv
    # json-dir holds: quote.json ratios.json km.json growth.json income.json est.json
    # rows.tsv: one row per existing Key Metrics row, tab-separated:  label \t value_raw
Output: JSON array, one object per row (mapped | skipped), with delta + material flag.
Exit: 0 ok; 3 self-validation (json-dir missing / rows-file unreadable).
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

TODAY = date.today().isoformat()

# label (normalized) -> (json file stem, field, delta_type, material_threshold)
# delta_type: pct | pp | abs ; threshold interpreted per type
FIELD_MAP = {
    "market cap": ("quote", "marketCap", "pct", 25),
    "market capitalization": ("quote", "marketCap", "pct", 25),
    "stock price": ("quote", "price", "pct", 25),
    "price": ("quote", "price", "pct", 25),
    "share price": ("quote", "price", "pct", 25),
    "ev/revenue": ("ratios", ["evToSalesTTM", "enterpriseValueOverRevenueTTM"], "pct", 25),
    "ev/sales": ("ratios", ["evToSalesTTM", "enterpriseValueOverRevenueTTM"], "pct", 25),
    "ev/ebitda": ("ratios", ["evToEbitdaTTM", "enterpriseValueOverEBITDATTM"], "pct", 25),
    "trailing p/e": ("ratios", "peRatioTTM", "pct", 25),
    "p/e": ("ratios", "peRatioTTM", "pct", 25),
    "revenue growth": ("growth", "growthRevenue", "pp", 10),
    "revenue growth (yoy)": ("growth", "growthRevenue", "pp", 10),
    "sales growth": ("growth", "growthRevenue", "pp", 10),
    "gross margin": ("ratios", "grossProfitMarginTTM", "pp", 3),
    "operating margin": ("ratios", "operatingProfitMarginTTM", "pp", 3),
    "op margin": ("ratios", "operatingProfitMarginTTM", "pp", 3),
    "net margin": ("ratios", "netProfitMarginTTM", "pp", 3),
    "fcf yield": ("km", "freeCashFlowYieldTTM", "pp", 1),
    "free cash flow yield": ("km", "freeCashFlowYieldTTM", "pp", 1),
    "net debt/ebitda": ("km", "netDebtToEBITDATTM", "abs", 0.5),
    "leverage": ("km", "netDebtToEBITDATTM", "abs", 0.5),
    "dividend yield": ("ratios", "dividendYieldTTM", "pp", 0.5),
}
# margins/yields that FMP returns as fractions (0.72) but theses show as % (72)
FRACTION_FIELDS = {"grossProfitMarginTTM", "operatingProfitMarginTTM",
                   "netProfitMarginTTM", "growthRevenue", "freeCashFlowYieldTTM",
                   "dividendYieldTTM"}


def norm_label(lbl):
    s = re.sub(r"^\*{1,2}|\*{1,2}$", "", lbl.strip()).strip()  # strip **bold**/*italic* markdown wrapping some theses use on the label cell
    s = re.sub(r"\s*\((?:ttm|gaap|non-gaap)\)\s*", "", s, flags=re.I).lower()
    return re.sub(r"\s*/\s*", "/", s)  # canonicalize slash spacing ("net debt / ebitda" → "net debt/ebitda")


def load_json(d, stem):
    p = Path(d) / f"{stem}.json"
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
        return data[0] if isinstance(data, list) and data else (data if isinstance(data, dict) else None)
    except (ValueError, IndexError):
        return None


def get_field(obj, field):
    if obj is None:
        return None
    if isinstance(field, list):
        for f in field:
            if f in obj and obj[f] is not None:
                return obj[f]
        return None
    return obj.get(field)


def parse_old_numeric(value_raw):
    """Extract the leading numeric magnitude from a formatted cell for delta math."""
    # Strip thousands-commas between digits FIRST — otherwise the regex stops at the
    # first comma and reads only the leading group: "¥35,950" -> 35.0, "₹10,000 crore"
    # -> 10.0, garbaging every delta on comma-formatted (mostly foreign) cells.
    v = re.sub(r"(?<=\d),(?=\d)", "", value_raw or "")
    m = re.search(r"(-?\d+(?:\.\d+)?)\s*(T|B|M|%|x)?", v, re.I)
    if not m:
        return None, None
    num = float(m.group(1))
    suffix = (m.group(2) or "").upper()
    scale = {"T": 1e12, "B": 1e9, "M": 1e6}.get(suffix, 1)
    return num * scale, suffix


def _fmt_suffix(v):
    # `%` has no trailing word boundary ("74.1%" ends the token), so the prior
    # r"(…|%)\b" never matched a percent — every % cell hinted suffix: null.
    # Require the magnitude letter to follow a digit (optional space) so a currency
    # prefix like "NT$" doesn't have its leading 'T' misread as Trillion.
    m = re.search(r"\d\s*([TBMx])\b", v, re.I)
    if m:
        return m.group(1).upper() if m.group(1).lower() != "x" else "x"
    return "%" if "%" in v else None


def format_hint(value_raw):
    v = value_raw or ""
    cur = re.search(r"NT\$|[$£¥€₹]|KRW|JPY|GBp|EUR|INR|crore|lakh", v)
    return {
        "raw": v,
        "has_tilde": v.strip().startswith("~"),
        "currency": cur.group(0) if cur else None,
        "suffix": _fmt_suffix(v),
        "decimals": len((re.search(r"\.(\d+)", v) or [None, ""])[1]) if "." in v else 0,
    }


def compute_delta(old_val, new_val, dtype):
    if old_val is None or new_val is None:
        return None
    if dtype == "pct":
        return None if old_val == 0 else round((new_val - old_val) / abs(old_val) * 100, 1)
    if dtype == "pp":
        return round(new_val - old_val, 2)  # both in same unit (pp)
    return round(new_val - old_val, 3)  # abs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json-dir", required=True)
    ap.add_argument("--rows-file", required=True)
    args = ap.parse_args()

    if not Path(args.json_dir).is_dir():
        print(f"SELF-VALIDATION FAILED: json-dir not found: {args.json_dir}", file=sys.stderr)
        return 3
    try:
        rows_text = Path(args.rows_file).read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        print(f"SELF-VALIDATION FAILED: cannot read rows-file: {e}", file=sys.stderr)
        return 3

    objs = {s: load_json(args.json_dir, s)
            for s in ("quote", "ratios", "km", "growth", "income", "est")}

    out = []
    for line in rows_text.split("\n"):
        if not line.strip() or "\t" not in line:
            continue
        label, value_raw = line.split("\t", 1)
        nl = norm_label(label)
        rec = {"label": label.strip(), "value_raw": value_raw.strip()}

        # derived metrics
        if nl in ("forward p/e", "p/e (forward)", "ntm p/e", "fwd p/e"):
            price = get_field(objs["quote"], "price")
            eps = _forward_eps(args.json_dir)
            new = round(price / eps, 2) if price and eps else None
            _map(rec, new, value_raw, "pct", 25)
        elif nl in ("fcf margin", "free cash flow margin"):
            fcf = get_field(objs["km"], "freeCashFlowTTM")
            rev = get_field(objs["km"], "revenueTTM")  # NO revenuePerShareTTM fallback: dividing
            new = round(fcf / rev * 100, 1) if fcf and rev else None  # total FCF by a per-share value is a units error
            _map(rec, new, value_raw, "pp", 3)
        elif re.match(r"(fy\s?\d{4}|20\d\d)\s+revenue", nl):
            yr = re.search(r"(\d{4})", nl).group(1)
            inc = objs["income"]
            new = None
            # income endpoint returned limit=3; load array separately
            arr = _load_json_array(args.json_dir, "income")
            for row in arr:
                if str(row.get("calendarYear") or row.get("date", ""))[:4] == yr:
                    new = row.get("revenue")
                    break
            _map(rec, new, value_raw, "pct", 5)
        elif nl in FIELD_MAP:
            stem, field, dtype, thr = FIELD_MAP[nl]
            new = get_field(objs[stem], field)
            fname = field[0] if isinstance(field, list) else field
            if new is not None and fname in FRACTION_FIELDS and abs(new) <= 1.5:
                new = round(new * 100, 2)  # fraction -> percent
            _map(rec, new, value_raw, dtype, thr)
        else:
            rec["status"] = "skipped"
            rec["reason"] = "no FMP mapping (custom metric)"
        out.append(rec)

    print(json.dumps(out, indent=2))
    return 0


def _load_json_array(d, stem):
    p = Path(d) / f"{stem}.json"
    if not p.exists():
        return []
    try:
        data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
        return data if isinstance(data, list) else [data]
    except ValueError:
        return []


def _forward_eps(d):
    """Next-fiscal-year consensus EPS for a forward P/E: the earliest analyst-
    estimate row dated after today (NTM). The prior code took est[0] — but FMP's
    estimate array is not guaranteed next-FY-first, so [0] could be a past or a
    far-out year, silently producing a wrong forward multiple. Falls back to the
    latest available row only if none are future-dated."""
    dated = []
    for row in _load_json_array(d, "est"):
        if not isinstance(row, dict):
            continue
        ds = str(row.get("date") or row.get("calendarYear") or "")[:10]
        eps = row.get("estimatedEpsAvg")
        if eps is None:
            eps = row.get("epsAvg")
        if ds and eps is not None:
            dated.append((ds, eps))
    if not dated:
        return None
    future = sorted(x for x in dated if x[0] > TODAY)
    return future[0][1] if future else sorted(dated)[-1][1]


def _map(rec, new_val, value_raw, dtype, thr):
    old_val, _ = parse_old_numeric(value_raw)
    if new_val is None:
        rec["status"] = "fetch_gap"
        rec["reason"] = "FMP field missing/null"
        return
    rec["status"] = "mapped"
    rec["new_value_numeric"] = new_val
    rec["old_value_numeric"] = old_val
    rec["delta_type"] = dtype
    delta = compute_delta(old_val, new_val, dtype)
    rec["delta"] = delta
    rec["material"] = (delta is not None and abs(delta) > thr)
    rec["material_threshold"] = thr
    rec["format_hint"] = format_hint(value_raw)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"SELF-VALIDATION FAILED: numbers_compute.py crashed: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(3)
