#!/usr/bin/env python3
"""Build SOURCE.md (core digest) and SOURCE-full.md (full pack) from all
publish: true notes in the vault. Deterministic — no LLM involved.

Usage:  python3 .claude/scripts/build_source.py [--tier core|full|both]
                                                [--only theses,sectors,macro]

Tiers:
  full  — every analytical section verbatim; noise stripped (callouts,
          Legacy Callouts, Related Research, frontmatter -> meta line,
          Log truncated to 3 newest entries)
  core  — full noise-strip PLUS per-type section allowlist, Log dropped.
          Target: fits a single LLM context window.

Output files carry `publish: false` and contain no embedded `publish: true`
lines, so the GitHub->website pipeline never picks them up.
"""
import argparse
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]

EXCLUDE_TOP = {"_Archive", "_Inbox", "Templates"}  # + all dot-dirs
FOLDER_TYPE = {"Theses": "thesis", "Sectors": "sector", "Macro & Technology": "macro"}
FOLDER_ORDER = ["Sectors", "Macro & Technology", "Theses"]  # frames -> forces -> names

# Sections dropped in BOTH tiers (working/audit state, dead links)
DROP_ALWAYS = {"legacy callouts", "related research"}

# Core-tier section allowlists (canonical casefolded heading text)
CORE_KEEP = {
    "thesis": [
        "summary",
        "key non-consensus insights",
        "key metrics",
        "bull case",
        "bear case",
        "catalysts",
        "conviction triggers",
    ],
    "sector": [
        "active theses",
        "key industry questions",
        "competitive dynamics",
        "investor heuristics",
        "macro shifts",
    ],
    "macro": None,  # None => keep full body (ad-hoc headings, no template)
    "other": None,
}

# Index-tier: minimal always-in-context map. "first" => preamble + first H2 section.
INDEX_KEEP = {
    "thesis": ["summary", "conviction triggers"],
    "sector": ["key industry questions"],
    "macro": "first",
    "other": "first",
}

TIER_KEEP = {
    "full": {"thesis": None, "sector": None, "macro": None, "other": None},
    "core": CORE_KEEP,
    "index": INDEX_KEEP,
}
INDEX_FIRST_SECTION_CAP = 800  # words

CALLOUT_RE = re.compile(r"^>\s*\[!(question|error|tip|todo)\]", re.IGNORECASE)
LOG_DATE_RE = re.compile(r"^###\s+(\d{4}-\d{2}-\d{2})")
META_KEYS = ["status", "conviction", "sector", "date", "key_metrics_last_refreshed"]


def parse_frontmatter(text):
    """Return (meta dict, body str). Minimal YAML: key: value + '- item' lists."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text
    meta, key = {}, None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return meta, "\n".join(lines[i + 1:])
        m = re.match(r"^([A-Za-z_][\w -]*):\s*(.*)$", line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip().strip('"')
            if val.startswith("[") and val.endswith("]"):
                meta[key] = [v.strip() for v in val[1:-1].split(",") if v.strip()]
            elif val == "":
                meta[key] = []
            else:
                meta[key] = val
        elif key is not None and re.match(r"^\s+-\s+", line):
            if isinstance(meta.get(key), list):
                meta[key].append(line.split("-", 1)[1].strip())
    return {}, text  # unterminated frontmatter


def is_publish_true(meta):
    v = meta.get("publish")
    return isinstance(v, str) and v.lower() == "true"


def strip_callouts(lines):
    """Remove the 4 feedback-callout block types entirely. Returns (lines, n)."""
    out, n, i = [], 0, 0
    while i < len(lines):
        if CALLOUT_RE.match(lines[i]):
            n += 1
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                i += 1
        else:
            out.append(lines[i])
            i += 1
    return out, n


def split_sections(lines):
    """Split body into (preamble, [(heading_line, [lines])]) on H2s.
    Code-fence aware so '## ' inside fences is not a heading."""
    pre, sections, cur, in_fence = [], [], None, False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            cur = (line, [])
            sections.append(cur)
        elif cur is None:
            pre.append(line)
        else:
            cur[1].append(line)
    return pre, sections


def canon(heading_line):
    return re.sub(r"\s+", " ", heading_line.lstrip("#").strip()).casefold()


def truncate_log(sec_lines, keep=3):
    """Keep the `keep` newest '### YYYY-MM-DD' groups (Logs are not reliably
    date-ordered). Fallback: keep last 8 lines."""
    groups, cur = [], None
    header = []
    for line in sec_lines:
        m = LOG_DATE_RE.match(line)
        if m:
            cur = {"date": m.group(1), "lines": [line]}
            groups.append(cur)
        elif cur is None:
            header.append(line)
        else:
            cur["lines"].append(line)
    if not groups:
        tail = sec_lines[-8:]
        return tail if len(sec_lines) <= 8 else ["*[log truncated]*", ""] + tail
    newest = sorted(groups, key=lambda g: g["date"], reverse=True)[:keep]
    out = []
    for g in newest:
        out.extend(l for l in g["lines"])
    omitted = len(groups) - len(newest)
    if omitted > 0:
        out.append(f"*[{omitted} earlier log entries omitted]*")
    out.append("")
    return out


def replace_dataview(text):
    return re.sub(r"```dataview\w*\n.*?```", "*[dynamic dataview table omitted]*",
                  text, flags=re.DOTALL)


def process_note(path, tier):
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    rel = path.relative_to(VAULT).as_posix()
    ntype = FOLDER_TYPE.get(path.relative_to(VAULT).parts[0], "other")

    lines, n_callouts = strip_callouts(body.split("\n"))
    # Drop the note's own H1 (we emit our own header with the filename)
    lines = [l for i, l in enumerate(lines) if not (l.startswith("# ") and i < 6)]
    pre, sections = split_sections(lines)

    spec = TIER_KEEP[tier].get(ntype)
    out_sections = []
    for heading, sec in sections:
        c = canon(heading)
        if c in DROP_ALWAYS:
            continue
        if c == "log":
            if tier != "full":
                continue
            sec = truncate_log(sec)
        if isinstance(spec, list) and c not in spec:
            continue
        out_sections.append((heading, sec))
    if spec == "first" and out_sections:
        heading, sec = out_sections[0]
        capped, words = [], 0
        for l in sec:
            words += len(l.split())
            capped.append(l)
            if words > INDEX_FIRST_SECTION_CAP:
                capped += ["", "*[truncated — full note in SOURCE.md / SOURCE-full.md]*"]
                break
        out_sections = [(heading, capped)]

    parts = list(pre)  # preamble kept in both tiers (usually empty after H1 removal)
    for heading, sec in out_sections:
        parts.append(heading)
        parts.extend(sec)

    body_out = replace_dataview("\n".join(parts))
    body_out = re.sub(r"\n{3,}", "\n\n", body_out).strip()

    meta_bits = [ntype]
    ticker = meta.get("ticker") or (rel.split("/")[-1].split(" - ")[0] if ntype == "thesis" else None)
    if ticker:
        meta_bits.append(f"ticker: {ticker}")
    for k in META_KEYS:
        if meta.get(k):
            label = "metrics as of" if k == "key_metrics_last_refreshed" else k
            meta_bits.append(f"{label}: {meta[k]}")
    if tier == "full":
        tags = meta.get("tags")
        if isinstance(tags, list) and tags:
            meta_bits.append("tags: " + ", ".join(tags))
        if meta.get("source"):
            meta_bits.append(f"source: {meta['source']}")

    return {
        "rel": rel, "type": ntype, "meta": meta, "ticker": ticker,
        "meta_line": " · ".join(meta_bits), "body": body_out,
        "src_words": len(text.split()), "out_words": len(body_out.split()),
        "callouts": n_callouts,
    }


def build_index(notes):
    out = ["## Index", ""]
    for folder in FOLDER_ORDER + ["other"]:
        sub = [n for n in notes if n["_folder"] == folder]
        if not sub:
            continue
        out.append(f"### {folder} ({len(sub)})")
        out.append("")
        if folder == "Theses":
            out.append("| Ticker | Note | Status | Conviction | Sector |")
            out.append("|---|---|---|---|---|")
            for n in sub:
                m = n["meta"]
                out.append(f"| {n['ticker'] or ''} | {n['rel'].split('/')[-1][:-3]} | "
                           f"{m.get('status','')} | {m.get('conviction','')} | {m.get('sector','')} |")
        else:
            out.append("| Note | Status | Date |")
            out.append("|---|---|---|")
            for n in sub:
                m = n["meta"]
                out.append(f"| {n['rel'].split('/')[-1][:-3]} | {m.get('status','')} | {m.get('date','')} |")
        out.append("")
    return out


def build_pack(notes, tier, generated):
    total_out = sum(n["out_words"] for n in notes)
    total_src = sum(n["src_words"] for n in notes)
    head = [
        "---",
        f"generated: {generated}",
        f"tier: {tier}",
        "publish: false",
        f"notes: {len(notes)}",
        f"source_words: {total_src}",
        f"pack_words: {total_out}",
        "tags: [meta, llm-context-pack]",
        "---",
        "",
        f"# SOURCE — investment vault publish-set compilation (tier: {tier})",
        "",
        "Single-file compilation of every vault note carrying `publish: true` "
        "(all Theses, Sector notes, and Macro & Technology notes; excludes Research, "
        "Website, Templates, and _Archive). Built deterministically by "
        "`.claude/scripts/build_source.py` — regenerate after research sessions.",
        "",
        "**How to read.** Each note starts with `# [k/N] <vault path>` plus a metadata "
        "line (type · ticker · status · conviction · sector · dates). Sector notes are "
        "industry frames, Macro & Technology notes are cross-cutting forces, Thesis notes "
        "are single-name investment cases. `[[wikilinks]]` reference other vault notes — "
        "resolve tickers against the Index below; linked Research notes are outside this pack.",
        "",
        "**Stripped from every note:** user-feedback callout blocks, `## Legacy Callouts` "
        "and `## Related Research` sections (audit state and dead links).",
    ]
    if tier == "core":
        head += [
            "**Core tier additionally keeps only:** Theses — Summary, Key Non-consensus "
            "Insights, Key Metrics, Bull/Bear Case, Catalysts, Conviction Triggers; "
            "Sectors — Active Theses, Key industry questions, Competitive dynamics, "
            "Investor heuristics, Macro shifts; Macro notes — kept whole. Logs dropped. "
            "Full bodies live in SOURCE-full.md.",
        ]
    elif tier == "index":
        head += [
            "**Index tier keeps only:** Theses — Summary + Conviction Triggers; Sectors — "
            "Key industry questions; Macro — opening section. Use this file as an "
            "always-in-context map of the whole book; pull the matching note chunk from "
            "SOURCE.md (analytical digest) or SOURCE-full.md (complete) when writing about "
            "a specific name. Chunk either file on the regex `^# \\[` — one note per chunk.",
        ]
    else:
        head += ["**Full tier:** all other sections verbatim; Logs truncated to the 3 newest entries."]
    head.append("")
    out = head + build_index(notes)
    for i, n in enumerate(notes, 1):
        out.append("---")
        out.append("")
        out.append(f"# [{i}/{len(notes)}] {n['rel']}")
        out.append(f"**{n['meta_line']}**")
        out.append("")
        out.append(n["body"])
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", choices=["index", "core", "full", "all"], default="all")
    ap.add_argument("--only", help="comma list: theses,sectors,macro")
    args = ap.parse_args()

    import subprocess
    generated = subprocess.run(["date", "+%Y-%m-%d %H:%M"], capture_output=True,
                               text=True).stdout.strip()

    files = []
    for p in sorted(VAULT.rglob("*.md")):
        parts = p.relative_to(VAULT).parts
        if any(seg.startswith(".") for seg in parts) or parts[0] in EXCLUDE_TOP:
            continue
        meta, _ = parse_frontmatter(p.read_text(encoding="utf-8"))
        if is_publish_true(meta):
            files.append(p)

    if args.only:
        alias = {"theses": "thesis", "thesis": "thesis", "sectors": "sector",
                 "sector": "sector", "macro": "macro", "macros": "macro"}
        want = {alias.get(w.strip(), w.strip()) for w in args.only.lower().split(",")}
        files = [p for p in files
                 if FOLDER_TYPE.get(p.relative_to(VAULT).parts[0], "other") in want]

    def folder_key(p):
        top = p.relative_to(VAULT).parts[0]
        return (FOLDER_ORDER.index(top) if top in FOLDER_ORDER else 99, p.as_posix().casefold())

    files.sort(key=folder_key)

    dest_names = {"index": "SOURCE-index.md", "core": "SOURCE.md", "full": "SOURCE-full.md"}
    for tier in (["index", "core", "full"] if args.tier == "all" else [args.tier]):
        notes = []
        for p in files:
            n = process_note(p, tier)
            n["_folder"] = p.relative_to(VAULT).parts[0] if p.relative_to(VAULT).parts[0] in FOLDER_ORDER else "other"
            notes.append(n)
        pack = build_pack(notes, tier, generated)
        dest = VAULT / dest_names[tier]
        dest.write_text(pack, encoding="utf-8")
        pw = len(pack.split())
        print(f"\n=== tier {tier} -> {dest.name} ===")
        print(f"notes: {len(notes)}  pack words: {pw:,}  est. tokens: ~{int(pw*1.35):,}")
        for folder in FOLDER_ORDER + ["other"]:
            sub = [n for n in notes if n["_folder"] == folder]
            if sub:
                print(f"  {folder:22s} {len(sub):3d} notes  "
                      f"{sum(n['src_words'] for n in sub):9,} src -> {sum(n['out_words'] for n in sub):9,} out words")
        print(f"  callout blocks stripped: {sum(n['callouts'] for n in notes)}")
        top = sorted(notes, key=lambda n: -n["out_words"])[:5]
        print("  largest packed notes: " + "; ".join(f"{n['rel'].split('/')[-1][:-3]} ({n['out_words']:,}w)" for n in top))


if __name__ == "__main__":
    main()
