#!/usr/bin/env python3
"""
verify_note.py — deterministic post-write verification gate for $ingest
(Fix #4, 2026-07-08). Implements SKILL.md checks #1–#14 as a script so every
ingest pays a reproducible ~50ms validation instead of LLM-executed regex.

The LLM keeps only the judgment residue: interpreting a BLOCK verdict, choosing
whether a manually-curated local file's advisory flags are acceptable, and the
report prose. This script computes the mechanical verdict.

Usage:
  python3 verify_note.py Research/NOTE.md \
      --mode url|pdf|local \
      --source-type earnings|analyst-report|news|deep-dive|video-transcript|web-clip|data|... \
      --source-words 31000 \
      --url "https://..."          # required for #13 in url mode

Verdict semantics (mirrors SKILL.md failure-handling lines 214–236):
  PASS       -> exit 0
  ADVISORY   -> exit 1  (note KEPT, flags reported — local manual files, OR any
                         mode where only advisory-tier flags fired, e.g. #13)
  BLOCK      -> exit 2  (url/pdf: caller DELETEs the note, retains source)
  self-fail  -> exit 3  (note unreadable)

Checks 1–4 structural block in ALL modes. Checks 5–14 block for url/pdf, advisory
for local. #8–#11,#14 skipped for source_type web-clip/data. #5 retention floor
exempts source_type earnings (delta notes, not compressions). #13 (title-URL
overlap) is url-only AND advisory-only — a redirect hint that never deletes.
"""

import argparse
import re
import sys
from pathlib import Path

# retention ladder (source_words upper-bound, R). Absolute min 300 words.
RETENTION = [(800, 0.65), (2000, 0.58), (5000, 0.46), (15000, 0.36),
             (30000, 0.28), (60000, 0.22), (float("inf"), 0.18)]

PAYWALL = [
    "subscribe to continue", "subscribers only", "become a member", "paywall",
    "please enable javascript", "enable javascript to view",
    "verify you are a human", "verify you are human", "complete the captcha",
    "cloudflare protection", "prove you're not a robot",
    "access denied", "403 forbidden", "404 not found", "page not found",
    "sign in to read", "log in to continue", "register to read",
    "create a free account to", "cookie consent required", "accept cookies to continue",
]
REQUIRED_SECTIONS = ["Thesis Delta", "Summary", "Evidence", "Contradiction Check"]
RATINGS = ["buy", "sell", "hold", "neutral", "overweight", "underweight",
           "outperform", "underperform", "market perform", "strong buy",
           "reduce", "accumulate"]
NEWS_TEMPORAL = ["today", "yesterday", "last week", "this morning", "announced",
                 "reported", "disclosed", "released", "filed"]
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
PERIOD_TOKENS = re.compile(r"\b(Q[1-4]|[1-4]Q|H[12]|FY2\d{2,3}|fiscal year|full year)\b", re.I)
CURRENCY_FIG = re.compile(r"(\$\s?\d|\d+\s*(million|billion|M\b|B\b)|revenue of|EPS of|"
                          r"operating income|net income)", re.I)
TICKER_SHAPE = re.compile(r"\b[A-Z]{1,5}\b")


def read(p):
    return Path(p).read_text(encoding="utf-8", errors="replace")


def split_fm(text):
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return "", text


def body_words(body):
    # exclude fenced code + headings
    out, fenced = [], False
    for ln in body.split("\n"):
        if ln.strip().startswith("```"):
            fenced = not fenced
            continue
        if fenced or ln.lstrip().startswith("#"):
            continue
        out.append(ln)
    return len(re.findall(r"\S+", "\n".join(out)))


def sections(body):
    out = {}
    cur = None
    for ln in body.split("\n"):
        m = re.match(r"^##\s+(?!#)(.*)$", ln)
        if m:
            cur = m.group(1).strip()
            out[cur] = []
        elif cur is not None:
            out[cur].append(ln)
    return out


def section_nonempty(secs, name):
    for h, buf in secs.items():
        if re.sub(r"\s+", " ", h.lower()).startswith(name.lower()):
            return bool([l for l in buf if l.strip() and not l.strip().startswith("<!--")])
    return None  # absent


def yaml_ok(fm):
    """Real parse if PyYAML present; else heuristic for the dominant failure
    (unquoted scalar containing ': ' or em-dash)."""
    try:
        import yaml
        yaml.safe_load(fm)
        return True, None
    except ImportError:
        # Heuristic fallback (PyYAML absent). Flag ONLY the dominant real break —
        # an unquoted scalar containing a colon-space, which YAML reads as nested
        # mapping. The prior `"—" in val` disjunct false-BLOCKED valid frontmatter
        # like `sector: Semiconductors — Cross-sector (ABF Substrates + Test)` (an
        # em-dash is not a YAML special character), and in url/pdf mode that BLOCK
        # deletes a good note. Em-dash removed; colon-space retained.
        for ln in fm.split("\n"):
            m = re.match(r"^([A-Za-z_][\w -]*):\s+(.*)$", ln)
            if m:
                val = m.group(2)
                if val and val[0] not in "'\"[" and re.search(r"\S: \S", val):
                    return False, f"unquoted value with colon-space: {ln.strip()[:60]}"
        return True, None
    except Exception as e:
        return False, str(e).split("\n")[0][:80]


def retention_floor(sw):
    for ub, r in RETENTION:
        if sw < ub:
            return max(300, int(sw * r)), r
    return max(300, int(sw * 0.18)), 0.18


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("note")
    ap.add_argument("--mode", choices=["url", "pdf", "local"], required=True)
    ap.add_argument("--source-type", default="")
    ap.add_argument("--source-words", type=int, default=0)
    ap.add_argument("--url", default="")
    args = ap.parse_args()

    try:
        text = read(args.note)
    except OSError as e:
        print(f"SELF-VALIDATION FAILED: cannot read {args.note}: {e}", file=sys.stderr)
        return 3

    fm, body = split_fm(text)
    secs = sections(body)
    bw = body_words(body)
    st = args.source_type.lower()
    blocks_hard = args.mode in ("url", "pdf")  # 5-14 block; local=advisory
    skip_domain = st in ("web-clip", "data")

    struct_fail = []   # 1-4 (block all modes)
    quality_fail = []  # 5-14 (block url/pdf, advisory local)
    soft_fail = []     # advisory in ALL modes, never blocks (e.g. #13 redirect hint)

    # --- #1 YAML parses ---
    ok, why = yaml_ok(fm)
    if not ok:
        struct_fail.append(f"#1 YAML frontmatter invalid ({why})")
    # --- #2 required fm fields ---
    for f in ("date:", "tags:", "source:", "source_type:"):
        if not re.search(rf"(?m)^{re.escape(f)}", fm):
            struct_fail.append(f"#2 missing frontmatter field {f}")
    # --- #3 body non-empty + ≥1 section ---
    if not secs:
        struct_fail.append("#3 body has no ## section header")
    # --- #4 last line not mid-sentence ---
    tail = [l for l in body.split("\n") if l.strip()]
    if tail:
        last = tail[-1].strip().rstrip("*_`").rstrip()
        # A line ending in terminal punctuation or a closer is a complete sentence
        # regardless of its final ALPHABETIC token. The old check scanned only
        # [A-Za-z'] tokens, so a line like '...respectively, in 2026."' resolved its
        # "last word" to the stopword "in" (skipping the digits, period and quote)
        # and false-BLOCKED a valid note. Only run the trailing-conjunction / open-
        # bracket test when the line does NOT already end on a sentence terminator.
        if last and last[-1] not in ".!?\"')]”’":
            w = re.findall(r"[A-Za-z']+|[,([]$", last)
            if last[-1] in ",([" or (w and w[-1].lower() in
                     {"and", "but", "or", "of", "in", "for", "to", "with", "from", "by", "the", "a"}):
                struct_fail.append(f"#4 last line ends mid-sentence: '…{last[-40:]}'")

    # --- #5 retention floor ---
    # The retention curve assumes source COMPRESSION. `earnings` notes (from
    # $transcript or an earnings-call ingest) are thesis-DELTA analyses — an
    # 8k-word transcript legitimately yields a ~2k-word delta — so the curve
    # over-floors them and deletes good notes. Exempt earnings; structural checks
    # (#7 required sections, #3/#4) still guarantee substance.
    if args.source_words > 0 and st != "earnings":
        floor, r = retention_floor(args.source_words)
        if bw < floor:
            quality_fail.append(f"#5 body {bw}w < floor {floor}w (source {args.source_words}w × R={r})")
        if args.source_words > 15000 and section_nonempty(secs, "Key Segments") is None:
            quality_fail.append(f"#5 missing required Key Segments section (source >15,000 words)")
    # --- #6 paywall/anti-bot sentinels ---
    low = body.lower()
    hits = [s for s in PAYWALL if s in low]
    if hits:
        quality_fail.append(f"#6 paywall/anti-bot sentinel(s): {', '.join(hits[:3])}")
    if bw < 50 and len(secs) == 0:
        quality_fail.append("#6 nav-only body (<50 words, no sections)")
    # --- #7 all 4 required sections non-empty ---
    for name in REQUIRED_SECTIONS:
        state = section_nonempty(secs, name)
        if state is None:
            quality_fail.append(f"#7 missing required section ## {name}")
        elif state is False:
            quality_fail.append(f"#7 required section ## {name} is empty")

    # --- domain validators #8-11,#14 (skip web-clip/data) ---
    if not skip_domain:
        if st == "earnings":
            if not PERIOD_TOKENS.search(body):
                quality_fail.append("#8 earnings: no quarterly-period token")
            if len(CURRENCY_FIG.findall(body)) < 2:
                quality_fail.append("#8 earnings: <2 currency figures")
            if not TICKER_SHAPE.search(body):
                quality_fail.append("#8 earnings: no ticker-shaped token")
        elif st == "analyst-report":
            if not any(rt in low for rt in RATINGS):
                quality_fail.append("#9 analyst-report: no rating token")
            if not (re.search(r"price target|target price|fair value|12-month target|\bPT\b", body, re.I)
                    or re.search(r"target[\s\S]{0,200}\$\d|\$\d[\s\S]{0,200}target", body, re.I)):
                quality_fail.append("#9 analyst-report: no price-target reference")
        elif st == "news":
            if not TICKER_SHAPE.search(body):
                quality_fail.append("#10 news: no ticker/company reference")
            dated = (re.search(r"\d{4}-\d{2}-\d{2}", body)
                     or re.search(r"[A-Z][a-z]+ \d{1,2},? \d{4}", body)
                     or any(t in low for t in NEWS_TEMPORAL)
                     or any(d in body for d in WEEKDAYS))
            if not dated:
                quality_fail.append("#10 news: no dated event reference")
        elif st == "deep-dive":
            substantive = sum(1 for h, buf in secs.items() if [l for l in buf if l.strip()])
            if substantive < 3:
                quality_fail.append(f"#11 deep-dive: only {substantive} substantive sections (<3)")
        elif st == "video-transcript":
            spk = (len(re.findall(r"^[A-Z][A-Za-z .'-]{1,40}:", body, re.M))
                   + len(re.findall(r'"[^"]{10,}"', body))
                   + len(re.findall(r"\b(said|says|according to)\b", body, re.I)))
            if spk < 3:
                quality_fail.append(f"#14 video-transcript: <3 speaker-attribution instances ({spk})")

    # --- #12 numerical integrity (all types) ---
    cap_o_bad = [m for m in re.finditer(r"[0-9O]*O[0-9O]*", body)
                 if re.search(r"[0-9]", m.group()) and "O" in m.group()]
    if len(cap_o_bad) > 3 or any(re.search(r"[$]|20\d\d", body[max(0, m.start()-4):m.end()+4])
                                 for m in cap_o_bad):
        if cap_o_bad:
            quality_fail.append(f"#12 numerical integrity: capital-O-as-zero ({len(cap_o_bad)} sites)")
    # I/l-as-1: only count runs adjacent to $ or a digit (corrupted numbers like
    # "$II" / "II5"). Bare Roman numerals in prose ("Phase III", "Type II", "Gen III")
    # have no numeric neighbor and are legitimate — the prior context-free count
    # false-blocked (and deleted) any note with 4+ Roman numerals.
    il_bad = [m for m in re.finditer(r"\b[Il]{2,}\b", body)
              if re.search(r"[$0-9]", body[max(0, m.start() - 2):m.end() + 2])]
    if len(il_bad) > 3:
        quality_fail.append(f"#12 numerical integrity: I/l-as-1 ({len(il_bad)})")
    # dropped decimal point: "$1.5B" → "$1 5B". Require a magnitude suffix so ordinary
    # spacing ("$50 000", "$5 to 10") doesn't match; allow 1+ leading digits (spec ex. $1 5B).
    dec = re.findall(r"\$\d+\s+\d{1,2}\s*(?:[BMT]\b|billion|million|trillion)", body, re.I)
    if len(dec) >= 2:
        quality_fail.append(f"#12 numerical integrity: decimal-dropped currency ({len(dec)})")

    # --- #13 title-URL Jaccard (url mode only) — ADVISORY, never a hard block ---
    # A low title↔slug overlap is a redirect/wrong-page HINT, not proof: API/data
    # URLs (FMP) and query-carried slugs legitimately score ~0 (the actual redirect-
    # to-paywall case is caught by #6 sentinels). Blocking on #13 deleted more good
    # notes than it caught bad ones, so it now only surfaces for review. Also strip
    # the query string + fragment — #13 compares PATH/slug segments (SKILL.md:214),
    # not the query (FMP puts symbol=/year= there, tanking the overlap on valid notes).
    if args.mode == "url" and args.url:
        hm = re.search(r"(?m)^#\s+(.*)$", body) or re.search(r"(?m)^title:\s*(.*)$", fm)
        title_tokens = set(re.findall(r"[A-Za-z]{4,}", hm.group(1).lower())) if hm else set()
        path = re.sub(r"[?#].*$", "", re.sub(r"^https?://[^/]+", "", args.url))
        url_tokens = set(re.findall(r"[A-Za-z]{4,}", path.lower()))
        if len(url_tokens) < 3:
            pass  # graceful skip (opaque slug / API path)
        elif title_tokens:
            inter = title_tokens & url_tokens
            union = title_tokens | url_tokens
            jac = len(inter) / len(union) if union else 0
            if jac < 0.50:
                soft_fail.append(f"#13 title-URL overlap {jac:.0%} < 50% (redirect/wrong-page risk — "
                                 f"review; not auto-blocked)")

    # --- #15 consensus-contrast (ADVISORY-only, all modes; skip web-clip/data) ---
    # SKILL.md requires Thesis Delta to state a consensus-vs-source contrast
    # ("consensus assumes X -> source implies Y") and Contradiction Check to name a
    # specific thesis section. This check makes the requirement visible without ever
    # blocking (quality rides on the model; the gate only surfaces the miss).
    if st not in ("web-clip", "data"):
        def _sec_text(name):
            for h, buf in secs.items():
                if re.sub(r"\s+", " ", h.lower()).startswith(name):
                    return "\n".join(buf)
            return ""
        td = _sec_text("thesis delta")
        cc = _sec_text("contradiction check")
        # Match the INTENT (contrast with a prevailing/prior view), not one phrasing.
        contrast_re = (r"consensus|priced[- ]in|market (assumes|expects|misses|prices)|"
                       r"bear (case|kill|narrative)|bull (case|narrative)|most-cited|"
                       r"widely (held|assumed|expected)|street|thesis assum|kill[- ]switch|"
                       r"non[- ]consensus|contrary to|conventional (view|wisdom)")
        anchor_re = (r"§|\[\[Theses/|Outstanding Q|Risk #|Insight #|thesis assum|"
                     r"thesis section|conviction trigger|falsif")
        if td and not re.search(contrast_re, td, re.I):
            soft_fail.append("#15 consensus-contrast: Thesis Delta has no consensus-vs-source "
                             "contrast ('consensus assumes X -> source implies Y') — review; not blocked")
        if cc and not re.search(anchor_re, cc, re.I):
            soft_fail.append("#15 consensus-contrast: Contradiction Check anchors to no specific "
                             "thesis element (§Section / [[Theses/...]] / named assumption) — review; not blocked")

    # ---- verdict ----
    verdict, rc = "PASS", 0
    if struct_fail:
        verdict, rc = "BLOCK", 2   # structural blocks in all modes
    elif quality_fail:
        if blocks_hard:
            verdict, rc = "BLOCK", 2
        else:
            verdict, rc = "ADVISORY", 1
    elif soft_fail:
        verdict, rc = "ADVISORY", 1   # advisory-only flags never delete

    print(f"VERDICT: {verdict}")
    print(f"note: {args.note} | mode: {args.mode} | source_type: {st or '(none)'} | "
          f"body_words: {bw} | source_words: {args.source_words}")
    if struct_fail:
        print("STRUCTURAL failures (block all modes):")
        for f in struct_fail:
            print(f"  - {f}")
    if quality_fail:
        cat = "BLOCK" if blocks_hard else "ADVISORY"
        print(f"CONTENT/DOMAIN failures ({cat} in {args.mode} mode):")
        for f in quality_fail:
            print(f"  - {f}")
    if soft_fail:
        print("ADVISORY-only flags (never block — review before $sync):")
        for f in soft_fail:
            print(f"  - {f}")
    if verdict == "PASS":
        print("all checks passed")
    elif verdict == "BLOCK":
        print("ACTION: delete the just-written note (retain source in _Inbox/); "
              "do NOT propagate corrupted content via $sync")
        print(f"first 200 chars of body: {body.strip()[:200]!r}")
    else:
        print("ACTION: note kept (manually-curated local file); review flagged checks before $sync")
    return rc


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"SELF-VALIDATION FAILED: verify_note.py crashed: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(3)
