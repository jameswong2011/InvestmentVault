#!/usr/bin/env python3
"""
extract_transcript_signals.py — deterministic Step 4 signal extraction for
$transcript (Fix #4, 2026-07-08).

Replaces the LLM-executed word-frequency math of SKILL.md Step 4.1–4.7 with a
reproducible script (the generate_graph.py / lint.py precedent). The LLM keeps
Step 6 (cross-referencing signals against the thesis Bull/Bear/Triggers) — the
genuinely qualitative work. This script only computes the counts/deltas.

Input: the cached FMP transcript JSON files (each an array; content in [0].content),
target quarter + up to 2 prior quarters. Emits one JSON object matching the
Step 4 output contract consumed by Steps 6/7/10/11/12.

Usage:
  python3 extract_transcript_signals.py \
      --current .data/transcripts/NVDA_Q1-2026.json \
      --prior   .data/transcripts/NVDA_Q4-2025.json \
      --prior   .data/transcripts/NVDA_Q3-2025.json
  # 0, 1, or 2 --prior allowed. With <2 priors, comparison flags note the gap.

Exit: 0 on success (JSON to stdout); 3 on self-validation failure (unreadable /
unparseable current transcript, empty content).
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ---- vocabularies (verbatim from SKILL.md Step 4, list-counts corrected) ----
# 4.1 exclusion: 7 seed phrases from SKILL.md + 23 authored generic fillers = 30.
EXCLUDE_PHRASES = {
    "during the quarter", "year over year", "as we look ahead", "let me start by",
    "thank you for joining", "as we discussed", "going forward",
    "thank you operator", "turn it over to", "turn the call over",
    "i will turn it over", "with that i will", "as you can see",
    "at the end of", "in the fourth quarter", "in the third quarter",
    "in the second quarter", "in the first quarter", "compared to the prior",
    "we are pleased to", "pleased to report", "i want to thank",
    "in terms of the", "as i mentioned earlier", "on the call today",
    "before i turn", "questions and answers", "ladies and gentlemen",
    "thank you everyone", "good afternoon everyone",
}
# 4.3 hedging — 25 terms (multi-word terms matched as substrings)
HEDGING = [
    "approximately", "roughly", "around", "about", "expected to", "expecting",
    "anticipate", "anticipating", "we believe", "we think", "we feel", "should",
    "could", "might", "may", "likely", "unlikely", "probably", "potentially",
    "if all goes well", "assuming", "subject to", "pending", "tentatively",
    "roughly speaking",
]
# 4.4 specificity — 5 regexes
SPECIFICITY_RES = [
    re.compile(r"\$[0-9]"),
    re.compile(r"[0-9]+\.[0-9]+%"),
    re.compile(r"[0-9]+%"),
    re.compile(r"[0-9]+\.?[0-9]*\s*(million|billion|trillion|M|B|T)\b"),
    re.compile(r"Q[1-4]\s+(of|FY)?\s*[0-9]{2,4}"),
]
# 4.5 Q&A skeptical — 23 terms
SKEPTICAL = [
    "concern", "concerned", "headwind", "pressure", "slowdown", "decel",
    "moderation", "moderating", "softer", "softening", "weakness",
    "disappointed", "missed", "below expectations", "light vs", "challenged",
    "difficult", "tough", "competitive pressure", "pricing pressure",
    "margin compression", "cyclical", "inventory correction",
]
# 4.7 guidance patterns
GUID_QUARTERLY = [re.compile(r"Q[1-4]\s+revenue\s+(of|in)\s+", re.I),
                  re.compile(r"we expect\s+Q[1-4]", re.I),
                  re.compile(r"guiding\s+to\s+", re.I)]
GUID_ANNUAL = [re.compile(r"full year", re.I), re.compile(r"fiscal year", re.I),
               re.compile(r"FY[0-9]{2,4}", re.I)]
GUID_RANGE = re.compile(r"between\s+\$[\d.]+\s+and\s+\$[\d.]+", re.I)
GUID_POINT = re.compile(r"approximately\s+\$[\d.]+", re.I)

# split heuristics (Step 3)
QA_MARKERS = [r"\bQ\s*&\s*A\b", r"questions and answers",
              r"question[- ]and[- ]answer session"]
QA_OPERATOR = ["we'll now open the line for questions",
               "we will now open the line for questions",
               "we'll now open the call for questions",
               "we will now open the call for questions",
               "our first question comes from"]
STOPWORDS = set("the a an and or but of to in on for with from at by as is are was "
                "were be been being that this these those it its we you they he she "
                "our your their his her do does did have has had will would can could "
                "about your how what when where why who which than then so if".split())


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s%$.]", " ", s.lower())).strip()


def load_content(path):
    data = json.loads(Path(path).read_text(encoding="utf-8", errors="replace"))
    if isinstance(data, list):
        data = data[0] if data else {}
    return (data.get("content") or "").strip(), data


# forward-looking preambles that precede the boilerplate "…a Q&A session" mention
# in the operator's opening remarks (NOT the real transition). Any Q&A marker whose
# preceding ~45 chars contain one of these is the announcement, not the boundary.
QA_LEADINS = ("there will be", "there will also be", "will be a", "will be held",
              "we will host", "we'll host", "will host", "we will conduct",
              "we'll conduct", "conduct a", "hold a", "followed by", "will then",
              "will include", "including a", "to conduct a")


def split_qa(content):
    """Return (prepared_text, qa_text_or_None) at the FIRST reliable transition.

    Bug class this guards (2026-07-09): every US call's operator preamble says
    "…after the speakers' remarks, there will be a question and answer session"
    ~1% into the transcript. The prior code split there, collapsing prepared
    remarks to ~50 words and firing bogus hedging/specificity deltas. Fix:
    (1) prefer operator floor-open / first-question phrases; (2) accept generic
    Q&A markers only past the opening zone (first 12%) AND not preceded by a
    forward-looking preamble; take the earliest surviving candidate."""
    low = content.lower()
    n = len(content)
    floor = int(n * 0.12)
    cands = []
    # 1. Operator floor-open / first-question phrases — the reliable transition.
    for phrase in QA_OPERATOR:
        p = low.find(phrase)
        if p >= 0:
            cands.append(p)
    # 2. Generic Q&A markers, boilerplate-filtered.
    for pat in QA_MARKERS:
        for m in re.finditer(pat, content, re.I):
            if m.start() < floor:
                continue  # opening-remarks boilerplate zone
            pre = low[max(0, m.start() - 45):m.start()]
            if any(b in pre for b in QA_LEADINS):
                continue  # "there will be a Q&A session" — announcement, not boundary
            cands.append(m.start())
    idx = min(cands) if cands else None
    if idx is None:
        # speaker-pattern shift: ≥3 analyst-style "Name - Firm" tags close together
        tags = [m.start() for m in re.finditer(r"\n[A-Z][A-Za-z.\- ]+\s+[-–]\s+[A-Z][A-Za-z.& ]+", content)]
        for i in range(len(tags) - 2):
            if tags[i + 2] - tags[i] < 1500:  # ~200 words
                idx = tags[i]
                break
    if idx is None:
        return content, None
    return content[:idx], content[idx:]


def ngrams(text, n):
    words = norm(text).split()
    return [" ".join(words[i:i + n]) for i in range(len(words) - n + 1)]


def phrase_counts(text):
    """3-5 word phrase -> count, across the text."""
    counts = {}
    for n in (3, 4, 5):
        for g in ngrams(text, n):
            counts[g] = counts.get(g, 0) + 1
    return counts


def wc(text):
    return max(1, len(norm(text).split()))


def per_1000(count, words):
    return round(count / words * 1000, 2)


def hedging_count(text):
    low = " " + norm(text) + " "
    return sum(low.count(" " + t + " ") if " " not in t else low.count(t) for t in HEDGING)


def skeptical_count(text):
    low = " " + norm(text) + " "
    return sum(low.count(" " + t + " ") if " " not in t else low.count(t) for t in SKEPTICAL)


def specificity_count(text):
    return sum(len(r.findall(text)) for r in SPECIFICITY_RES)


def delta_pct(cur, prior):
    if prior == 0:
        return None if cur == 0 else 100.0
    return round((cur - prior) / prior * 100, 1)


def qa_turns(qa_text):
    """Split Q&A into speaker turns. Tolerates line-start AND inline speaker
    labels ('Operator:', 'Jane Doe:', 'John Smith - Morgan Stanley:') since FMP
    content formatting varies by company (may be single-line)."""
    if not qa_text:
        return []
    # a speaker label = 1-4 Capitalized words, optional ' - Firm', then a colon
    label = r"([A-Z][A-Za-z.'&]+(?:\s+[A-Z][A-Za-z.'&]+){0,3}(?:\s*[-–]\s*[A-Z][A-Za-z.&'/ ]+?)?)\s*:\s"
    parts = re.split(r"(?:^|\s)" + label, qa_text)
    turns = []
    for i in range(1, len(parts), 2):
        speaker = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        turns.append((speaker, body))
    return turns


def _is_operator(spk):
    return spk.strip().lower().startswith("operator")


def _is_analyst(spk):
    # FMP analyst turns carry a firm affiliation formatted "Jane Doe - Morgan
    # Stanley" — a SPACE-PADDED dash. Require the surrounding spaces so hyphenated
    # personal names (e.g. "Jen-Hsun Huang", the CEO) are NOT misread as analysts.
    # When a transcript's labels carry no affiliation at all, zero analysts are
    # found → evasiveness returns None (honest 'not computable' — see evasiveness()).
    return bool(re.search(r"\s[-–]\s", spk)) and not _is_operator(spk)


def evasiveness(qa_text):
    """Fraction of analyst questions whose answer ignores the question's content
    words. Scores ONLY analyst-question → next-speaker-answer pairs — the prior
    code paired every adjacent turn (incl. operator hand-offs and exec→exec
    continuations), inflating the rate to a meaningless ~85%. Returns None when
    speaker labels lack firm affiliations (can't identify analysts) — an honest
    'not computable' beats a confident wrong number."""
    turns = qa_turns(qa_text)
    if len(turns) < 2:
        return None
    evasive = pairs = 0
    for i in range(len(turns) - 1):
        spk, q = turns[i]
        nxt_spk, a = turns[i + 1]
        if not _is_analyst(spk):        # question must come from an analyst
            continue
        if _is_operator(nxt_spk):       # operator hand-off, not the management answer
            continue
        content_words = [w for w in norm(q).split()
                         if w not in STOPWORDS and len(w) > 3][:7]
        if not content_words:
            continue
        pairs += 1
        ans_head = set(norm(a).split()[:50])
        if not any(w in ans_head for w in content_words):
            evasive += 1
    if pairs == 0:
        return None
    return {"evasive_turns": evasive, "total_qa_turns": pairs,
            "evasive_pct": round(evasive / pairs * 100, 1),
            "basis": "analyst-question → management-answer pairs only"}


def guidance(text):
    q = sum(len(r.findall(text)) for r in GUID_QUARTERLY)
    a = sum(len(r.findall(text)) for r in GUID_ANNUAL)
    ranges = len(GUID_RANGE.findall(text))
    points = len(GUID_POINT.findall(text))
    return {"quarterly_hits": q, "annual_hits": a,
            "range_constructs": ranges, "point_constructs": points}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--current", required=True)
    ap.add_argument("--prior", action="append", default=[])
    ap.add_argument("--label", default="", help="optional quarter label for current")
    args = ap.parse_args()

    try:
        cur_content, cur_meta = load_content(args.current)
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(f"SELF-VALIDATION FAILED: cannot load current transcript {args.current}: {e}",
              file=sys.stderr)
        return 3
    if len(cur_content) < 500:
        print(f"SELF-VALIDATION FAILED: current transcript content <500 chars "
              f"({len(cur_content)}) — likely tier-gated / empty", file=sys.stderr)
        return 3

    priors = []
    for p in args.prior[:2]:
        try:
            c, _ = load_content(p)
            if len(c) >= 500:
                priors.append(c)
        except (OSError, ValueError, json.JSONDecodeError):
            pass  # missing prior degrades gracefully

    cur_prep, cur_qa = split_qa(cur_content)
    prior_preps = [split_qa(c)[0] for c in priors]
    prior_qas = [split_qa(c)[1] for c in priors]

    n_priors = len(priors)
    degraded = n_priors < 2

    # 4.1 new language
    cur_ph = phrase_counts(cur_prep)
    prior_ph_union = {}
    for pp in prior_preps:
        for g, ct in phrase_counts(pp).items():
            prior_ph_union[g] = prior_ph_union.get(g, 0) + ct
    new_lang = [{"phrase": g, "count_current": ct}
                for g, ct in cur_ph.items()
                if ct >= 2 and g not in EXCLUDE_PHRASES and prior_ph_union.get(g, 0) == 0]
    new_lang.sort(key=lambda x: -x["count_current"])
    new_lang = new_lang[:10]

    # 4.2 dropped language (phrase ≥2 in BOTH priors, 0 in current)
    dropped = []
    if n_priors == 2:
        pc = [phrase_counts(pp) for pp in prior_preps]
        for g in set(pc[0]) & set(pc[1]):
            if pc[0][g] >= 2 and pc[1][g] >= 2 and cur_ph.get(g, 0) == 0 \
                    and g not in EXCLUDE_PHRASES:
                dropped.append({"phrase": g, "count_prior_combined": pc[0][g] + pc[1][g]})
    elif n_priors == 1:
        for g, ct in phrase_counts(prior_preps[0]).items():
            if ct >= 2 and cur_ph.get(g, 0) == 0 and g not in EXCLUDE_PHRASES:
                dropped.append({"phrase": g, "count_prior_combined": ct})
    dropped.sort(key=lambda x: -x["count_prior_combined"])
    dropped = dropped[:10]

    # 4.3 hedging density
    cur_hedge = per_1000(hedging_count(cur_prep), wc(cur_prep))
    prior_hedge = round(sum(per_1000(hedging_count(pp), wc(pp)) for pp in prior_preps)
                        / n_priors, 2) if n_priors else None
    hedge_d = delta_pct(cur_hedge, prior_hedge) if prior_hedge is not None else None

    # 4.4 specificity
    cur_spec = per_1000(specificity_count(cur_prep), wc(cur_prep))
    prior_spec = round(sum(per_1000(specificity_count(pp), wc(pp)) for pp in prior_preps)
                       / n_priors, 2) if n_priors else None
    spec_d = delta_pct(cur_spec, prior_spec) if prior_spec is not None else None

    # 4.5 Q&A skeptical density
    if cur_qa:
        cur_skep = per_1000(skeptical_count(cur_qa), wc(cur_qa))
        pq = [q for q in prior_qas if q]
        prior_skep = round(sum(per_1000(skeptical_count(q), wc(q)) for q in pq) / len(pq), 2) if pq else None
        skep_d = delta_pct(cur_skep, prior_skep) if prior_skep is not None else None
    else:
        cur_skep = prior_skep = skep_d = None

    # 4.6 evasiveness
    cur_evas = evasiveness(cur_qa)
    prior_evas_vals = [e["evasive_pct"] for e in (evasiveness(q) for q in prior_qas if q) if e]
    prior_evas = round(sum(prior_evas_vals) / len(prior_evas_vals), 1) if prior_evas_vals else None

    # 4.7 guidance
    guid = guidance(cur_content)
    guid["range_vs_point"] = ("range" if guid["range_constructs"] > guid["point_constructs"]
                              else "point" if guid["point_constructs"] > guid["range_constructs"]
                              else "mixed/none")

    # split-reliability guard: a healthy call has >500-word prepared remarks and a
    # Q&A section. If the split collapsed (bad transcript / unmatched boundary),
    # suppress the confident hedging/specificity/skeptical flags rather than emit a
    # spurious −100% delta as a "management retreated to qualitative framing" signal.
    prep_wc, qa_wc = wc(cur_prep), (wc(cur_qa) if cur_qa else 0)
    prep_reliable = prep_wc >= 500
    qa_reliable = qa_wc >= 500

    out = {
        "ticker": cur_meta.get("symbol"),
        "current_label": args.label or _period_label(cur_meta),
        "current_date": cur_meta.get("date"),
        "priors_used": n_priors,
        "degraded_single_prior": degraded,
        "qa_detected": cur_qa is not None,
        "prepared_word_count": prep_wc,
        "qa_word_count": qa_wc,
        "split_reliable": prep_reliable and (cur_qa is None or qa_reliable),
        "new_language": new_lang,
        "dropped_language": dropped,
        "hedging": {"current": cur_hedge, "prior2_avg": prior_hedge,
                    "delta_pct": hedge_d,
                    "direction": _dir(hedge_d, "more hedged", "more confident"),
                    "flag_gt25pct": prep_reliable and hedge_d is not None and abs(hedge_d) > 25},
        "specificity": {"current": cur_spec, "prior2_avg": prior_spec,
                        "delta_pct": spec_d,
                        "direction": _dir(spec_d, "more specific", "less specific"),
                        "flag_drop_ge20pct": prep_reliable and spec_d is not None and spec_d <= -20},
        "qa_skeptical": {"current": cur_skep, "prior2_avg": prior_skep,
                         "delta_pct": skep_d,
                         "flag_rise_ge50pct": qa_reliable and skep_d is not None and skep_d >= 50},
        "evasiveness": {"current": cur_evas, "prior2_avg_pct": prior_evas,
                        "caveat": "heuristic scored over analyst-question→management-answer "
                                  "pairs; null when FMP speaker labels carry no firm "
                                  "affiliation (analysts unidentifiable — most FMP transcripts). "
                                  "Even when computed, disclosure-restricted topics (M&A/legal/"
                                  "pricing) read as evasive but are legitimate non-disclosure; "
                                  "surface as evidence to inspect, not a conclusion"},
        "guidance": guid,
    }
    print(json.dumps(out, indent=2))
    return 0


def _period_label(meta):
    """FMP transcript JSON carries `period: "Q1"` (+ `year`), not `quarter`.
    The prior f-string read `quarter` → always "Q?-YYYY"."""
    p = meta.get("period") or meta.get("quarter")
    yr = meta.get("year", "?")
    if p is None or str(p).strip() == "":
        return f"Q?-{yr}"
    ps = str(p).strip()
    return f"{ps if ps.upper().startswith('Q') else 'Q' + ps}-{yr}"


def _dir(delta, pos_label, neg_label):
    if delta is None:
        return "n/a"
    if delta > 5:
        return pos_label
    if delta < -5:
        return neg_label
    return "unchanged"


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"SELF-VALIDATION FAILED: extract_transcript_signals.py crashed: "
              f"{type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(3)
