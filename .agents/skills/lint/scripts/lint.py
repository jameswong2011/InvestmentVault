#!/usr/bin/env python3
"""
lint.py — deterministic vault health checks (Fix #3, 2026-07-08).

Implements the mechanical subset of $lint's 55-check registry as a script,
following the generate_graph.py precedent: LLM-executed grep/awk/date-math
was the vault's most reliability-prone pattern; scripting it makes results
reproducible and cuts an Opus-max full-vault invocation to a ~2s run.

COVERED (deterministic):  #1 #2 #3 #4 #5(empty-only) #6 #8 #10 #11 #12 #13
  #14 #15 #16 #17 #18 #19 #20 #21 #22 #23 #24 #25 #26 #27 #28(candidates)
  #29(a/b/c presence) #30 #32 #33 #34 #35 #36 #37 #38 #39 #41 #42 #43 #44
  #45 #46 #47 #48 #49 #50 #51 #52 #53 #54 #55(candidates) #56
NOT COVERED (LLM judgment — run by the $lint skill after this script):
  #5 thin-but-nonempty sections, #7 old financial data, #9 unlinked mentions,
  #12/#13 interpretation (script emits mechanical flags only), #14 nuance,
  #28 confirmation of flagged fragments, #29 reverse-check + semantic drift,
  #55 intent review of matched phrases.

Usage:  python3 .agents/skills/lint/scripts/lint.py            # full vault
        python3 .agents/skills/lint/scripts/lint.py --ticker NVDA
Exit:   0 = pass/nice-to-have only, 1 = Important found, 2 = Critical found,
        3 = internal error / vault not found (self-validation failed).
"""

import argparse
import difflib
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ---------------------------------------------------------------- constants
VAULT = Path(__file__).resolve().parents[4]
NOW = datetime.now(timezone.utc)
TODAY = NOW.date()
SPEC_DATE = datetime(2026, 4, 19).date()  # propagated_to: contract spec date

THESES = VAULT / "Theses"
SECTORS = VAULT / "Sectors"
RESEARCH = VAULT / "Research"
ARCHIVE = VAULT / "_Archive"
SNAPSHOTS = ARCHIVE / "Snapshots"
MACRO = next((p for p in (VAULT / "Macro & Technology", VAULT / "Macro") if p.is_dir()),
             VAULT / "Macro & Technology")
SKILLS = VAULT / ".agents" / "skills"

HOT_SECTIONS = ["Active Research Thread", "Latest Sync", "Sync Archive",
                "Recent Conviction Changes", "Open Questions", "Portfolio Snapshot"]
ALLOWLIST_LINKS = {"pinned", "preserve"}  # intentional unresolved markers (#3)
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
WIKILINK_RE = re.compile(r"!?\[\[([^\]]+)\]\]")
CALLOUT_RE = re.compile(r"^>\s*\[!(question|error|tip|todo)\]\s*(\d{4}-\d{2}-\d{2})(.*)$")

# manifest type → in-progress severity (per SKILL.md check specs)
MANIFEST_INPROG = {"prune": "CRITICAL", "compare": "CRITICAL", "sync": "IMPORTANT",
                   "status": "IMPORTANT", "thesis": "IMPORTANT", "stress-test": "NICE",
                   "deepen": "IMPORTANT"}
MANIFEST_CHECK = {"prune": "#36", "sync": "#41", "compare": "#45",
                  "stress-test": "#47", "status": "#48", "thesis": "#49", "deepen": "#50m"}

findings = []      # (severity, check, message)
candidates = []    # (check, message) — data for the LLM judgment pass
stats = {}


def add(sev, check, msg):
    findings.append((sev, check, msg))


def cand(check, msg):
    candidates.append((check, msg))


# ---------------------------------------------------------------- helpers
def read(p):
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def parse_fm(text):
    """Line-based YAML-subset frontmatter parser. Lists like [a, b] supported."""
    fm = {}
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return fm
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_ -]*):\s*(.*)$", line)
        if m:
            key, val = m.group(1).strip(), m.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                fm[key] = [v.strip().strip("'\"") for v in inner.split(",") if v.strip()] if inner else []
            else:
                fm[key] = val.strip("'\"")
    return fm


def sections(text):
    """[(heading, start_idx, end_idx, body_lines)] for ## level headings."""
    lines = text.split("\n")
    out, cur, start = [], None, 0
    for i, ln in enumerate(lines):
        if ln.startswith("## ") and not ln.startswith("###"):
            if cur is not None:
                out.append((cur, start, i, lines[start + 1:i]))
            cur, start = ln[3:].strip(), i
    if cur is not None:
        out.append((cur, start, len(lines), lines[start + 1:]))
    return out


def section_body(text, name):
    for h, _s, _e, body in sections(text):
        if h.strip().lower() == name.strip().lower():
            return "\n".join(body)
    return None


def strip_code_fences(text):
    out, fenced = [], False
    for ln in text.split("\n"):
        if ln.strip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            out.append(ln)
    return "\n".join(out)


def wikilinks_with_lines(text):
    """[(lineno, target, in_log_section)] — target stripped of alias/anchor/!"""
    res, in_log, fenced = [], False, False
    for i, ln in enumerate(text.split("\n"), 1):
        if ln.strip().startswith("```"):
            fenced = not fenced
        if ln.startswith("## ") and not ln.startswith("###"):
            in_log = ln[3:].strip().lower() == "log"
        if fenced:
            continue
        for m in WIKILINK_RE.finditer(ln):
            # un-escape Obsidian table-pipe (\|) before splitting alias, matching
            # generate_graph.py extract_links — else "[[Theses/X\|alias]]" yields
            # "Theses/X\" and every table-form wikilink false-fails #3/#1/#24.
            t = m.group(1).replace("\\|", "|").split("|")[0].split("#")[0].strip()
            if t:
                res.append((i, t, in_log))
    return res


def last_log_date(text):
    body = section_body(text, "Log")
    if body is None:
        return None
    dates = re.findall(r"^###\s+(\d{4}-\d{2}-\d{2})", body, re.M)
    if not dates:
        return None
    try:
        return max(datetime.strptime(d, "%Y-%m-%d").date() for d in dates)
    except ValueError:
        return None


def parse_date(s):
    if not s:
        return None
    m = DATE_RE.search(str(s))
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1), "%Y-%m-%d").date()
    except ValueError:
        return None


def days_old(d):
    return (TODAY - d).days if d else None


def ticker_of(thesis_path):
    return thesis_path.stem.split(" - ")[0].strip()


def fm_tickers(fm):
    """Normalized ticker(s) from a frontmatter ticker: field. Handles both scalar
    (`ticker: NVDA`) and list (`ticker: [AMD, NVDA]`) forms, stripping the FMP
    exchange suffix (000660.KS → 000660). Prior code stringified the list, so
    `ticker: [AMD, NVDA]` became the literal "['AMD', 'NVDA']" and matched no
    thesis — false #8/#11/#32 across every multi-ticker research note."""
    raw = fm.get("ticker", "")
    vals = raw if isinstance(raw, list) else [raw]
    return [str(v).split(".")[0].strip() for v in vals if str(v).strip()]


def norm_sector(s):
    return re.sub(r"\s+", " ", s.strip().lstrip("@").lower())


# ---------------------------------------------------------------- load vault
def load():
    v = {}
    v["theses"] = {p: read(p) for p in sorted(THESES.glob("*.md"))}
    v["sectors"] = {p: read(p) for p in sorted(SECTORS.glob("*.md"))}
    v["macro"] = {p: read(p) for p in sorted(MACRO.glob("*.md"))} if MACRO.is_dir() else {}
    v["research"] = {p: read(p) for p in sorted(RESEARCH.glob("*.md"))}
    v["fm"] = {p: parse_fm(t) for d in ("theses", "sectors", "macro", "research")
               for p, t in v[d].items()}
    # vault-wide filename index for wikilink resolution (Obsidian resolves by basename)
    skip = {".git", ".obsidian", ".claudian", ".claude", ".agents", ".codex", ".data"}
    stems, allfiles = {}, set()
    for p in VAULT.rglob("*"):
        if any(part in skip for part in p.parts):
            continue
        if p.is_file():
            allfiles.add(p.name)
            if p.suffix == ".md":
                stems.setdefault(p.stem, []).append(p.relative_to(VAULT).as_posix())
    v["stems"], v["allfiles"] = stems, allfiles
    return v


def link_resolves(target, v):
    base = target.split("/")[-1]
    if base in v["stems"] or f"{base}.md" in v["allfiles"] or base in v["allfiles"]:
        return True
    return (VAULT / target).exists() or (VAULT / f"{target}.md").exists()


# ---------------------------------------------------------------- checks
def structural(v, scoped_theses):
    theses, research = v["theses"], v["research"]
    # research links from theses (used by #1, #24, #39 cross-check)
    linked_research = set()
    for p, t in theses.items():
        for _ln, tgt, _log in wikilinks_with_lines(t):
            base = tgt.split("/")[-1]
            if tgt.startswith("Research/") or base in {rp.stem for rp in research}:
                linked_research.add(base)
    v["linked_research"] = linked_research

    if not scoped_theses:  # ---- #1 orphaned research (vault-wide)
        orphans = [p for p in research if p.stem not in linked_research]
        v["computed_orphans"] = {p.stem for p in orphans}
        for p in orphans:
            add("NICE", "#1", f"Orphaned research note (no thesis links it): [[Research/{p.stem}]]")
        stats["orphans"] = len(orphans)

    # ---- #2 missing MOC entries
    sector_texts = {norm_sector(p.stem): (p, t) for p, t in v["sectors"].items()}
    for p, t in (scoped_theses or theses).items():
        fm = v["fm"].get(p, {})
        if fm.get("status") not in ("active", "monitoring"):
            continue
        sec = fm.get("sector", "")
        hit = sector_texts.get(norm_sector(sec)) if sec else None
        if hit and p.stem not in hit[1]:
            add("IMPORTANT", "#2", f"[[Theses/{p.stem}]] ({fm.get('status')}) missing from "
                f"[[Sectors/{hit[0].stem}]] Active Theses")

    # ---- #3 broken wikilinks (Theses+Sectors+Macro; Log-section + allowlist excluded)
    broken = 0
    for d in ("theses", "sectors", "macro"):
        pool = scoped_theses if (scoped_theses and d == "theses") else v[d]
        if scoped_theses and d != "theses":
            continue
        for p, t in pool.items():
            for ln, tgt, in_log in wikilinks_with_lines(t):
                if in_log or tgt in ALLOWLIST_LINKS:
                    continue
                if not link_resolves(tgt, v):
                    broken += 1
                    add("IMPORTANT", "#3", f"Broken wikilink [[{tgt}]] — {p.relative_to(VAULT)}:{ln}")
    stats["broken_links"] = broken

    # ---- #4 missing frontmatter
    req = {"theses": ["date", "tags", "status", "conviction", "sector", "ticker"],
           "research": ["date", "tags", "source", "source_type"],
           "sectors": ["date", "tags"], "macro": ["date", "tags"]}
    for d, fields in req.items():
        pool = scoped_theses if (scoped_theses and d == "theses") else ({} if scoped_theses else v[d])
        for p, _t in pool.items():
            missing = [f for f in fields if f not in v["fm"].get(p, {})]
            if missing:
                add("IMPORTANT", "#4", f"{p.relative_to(VAULT)} missing frontmatter: {', '.join(missing)}")

    # ---- #5 empty critical sections (deterministic empties only; thin → LLM)
    for p, t in (scoped_theses or theses).items():
        for name in ("Key Metrics", "Bull Case", "Bear Case", "Key Non-consensus Insights"):
            body = section_body(t, name)
            if body is None:
                continue  # #14 handles absence
            content = [l for l in body.split("\n") if l.strip() and not l.strip().startswith("<!--")]
            if name == "Key Metrics":
                if len([l for l in content if l.strip().startswith("|")]) < 3:  # header+sep+1 row
                    add("IMPORTANT", "#5", f"[[Theses/{p.stem}]] — Key Metrics table empty/missing rows")
            elif not content:
                add("IMPORTANT", "#5", f"[[Theses/{p.stem}]] — empty section: {name}")
            elif len(" ".join(content).split()) < 25:
                cand("#5", f"[[Theses/{p.stem}]] §{name} is thin ({len(' '.join(content).split())} words) — LLM: judge substance")
        if last_log_date(t) is None:
            add("IMPORTANT", "#5", f"[[Theses/{p.stem}]] — no Log entries")


def freshness(v, scoped_theses):
    for p, t in (scoped_theses or v["theses"]).items():
        fm = v["fm"].get(p, {})
        lld = last_log_date(t)
        if fm.get("status") == "active" and lld and days_old(lld) > 30:
            add("NICE", "#6", f"Stale active thesis: [[Theses/{p.stem}]] — last Log entry {days_old(lld)}d ago")
    # #8 inactive research (>60d since last research note per ticker)
    latest = {}
    for p in v["research"]:
        fm = v["fm"].get(p, {})
        d = parse_date(fm.get("date")) or parse_date(p.stem)
        if not d:
            continue
        for tick in fm_tickers(fm):  # multi-ticker notes credit every ticker
            latest[tick] = max(latest.get(tick, d), d)
    for p, _ in (scoped_theses or v["theses"]).items():
        tick = ticker_of(p)
        if v["fm"].get(p, {}).get("status") not in ("active", "monitoring"):
            continue
        d = latest.get(tick)
        if d and days_old(d) > 60:
            add("NICE", "#8", f"{tick}: no new research in {days_old(d)}d (last {d})")
        elif not d:
            add("NICE", "#8", f"{tick}: no research note carries ticker: {tick}")
    # #25 pending sync
    if not scoped_theses:
        ls = VAULT / ".last_sync"
        if not ls.exists():
            add("IMPORTANT", "#25", "No .last_sync baseline — run $sync")
        else:
            mark = ls.stat().st_mtime
            pend = [p.relative_to(VAULT).as_posix() for d in (RESEARCH, THESES, SECTORS, MACRO)
                    if d.is_dir() for p in d.glob("*.md") if p.stat().st_mtime > mark]
            if pend:
                add("IMPORTANT", "#25", f"{len(pend)} file(s) modified since last $sync: "
                    + ", ".join(pend[:8]) + ("…" if len(pend) > 8 else ""))
            stats["pending_sync"] = len(pend)
            # #57 watermark-collapse alarm (2026-07-09): a pending-sync count above
            # ~20% of vault notes is not a backlog, it's a bulk-mtime event or a stuck
            # watermark — default $sync and $sync all become intractable, $prune
            # dead-ends on Phase 0.B, and $clean's mtime safety-net falsely protects
            # every aged snapshot. Escalate with explicit guidance.
            total_notes = sum(1 for d in (RESEARCH, THESES, SECTORS, MACRO)
                              if d.is_dir() for _ in d.glob("*.md"))
            if total_notes and len(pend) / total_notes > 0.20:
                add("CRITICAL", "#57",
                    f"Watermark collapse: {len(pend)}/{total_notes} notes "
                    f"({len(pend)*100//total_notes}%) newer than .last_sync — likely a bulk "
                    f"mtime touch (git ops) or stuck watermark, not real research volume. "
                    f"Cross-check `git diff --name-only` since the watermark date; then either "
                    f"run $sync all once or advance .last_sync over mtime-only files. Until "
                    f"resolved: $sync default+all intractable, $prune blocks, $clean over-protects.")


def connections(v):
    # #10 disconnected macro notes
    linked_macro = set()
    for _p, t in v["theses"].items():
        for _ln, tgt, _log in wikilinks_with_lines(t):
            base = tgt.split("/")[-1]
            if base in {mp.stem for mp in v["macro"]}:
                linked_macro.add(base)
    for p in v["macro"]:
        if p.stem not in linked_macro:
            add("NICE", "#10", f"Disconnected macro note: [[{MACRO.name}/{p.stem}]] — no thesis references it")
    # #11 missing thesis candidates (ticker in 3+ research notes, no thesis)
    thesis_ticks = {ticker_of(p) for p in v["theses"]}
    tally = {}
    for p in v["research"]:
        for tick in fm_tickers(v["fm"].get(p, {})):
            tally[tick] = tally.get(tick, 0) + 1
    for tick, n in sorted(tally.items()):
        if n >= 3 and tick not in thesis_ticks:
            add("NICE", "#11", f"Missing thesis candidate: {tick} appears in {n} research notes, no thesis")


def analytical(v, scoped_theses):
    tpl = read(VAULT / "Templates" / "Thesis Template.md")
    tpl_heads = [h for h, *_ in sections(tpl)] if tpl else []
    priority = {"Key Non-consensus Insights", "Outstanding Questions", "Conviction Triggers"}
    for p, t in (scoped_theses or v["theses"]).items():
        fm = v["fm"].get(p, {})
        # #12 conviction-evidence mismatch (mechanical count; LLM judges quality)
        nlinks = len({tgt.split("/")[-1] for _l, tgt, _g in wikilinks_with_lines(t)
                      if tgt.split("/")[-1] in {rp.stem for rp in v["research"]}})
        conv = fm.get("conviction")
        if conv == "high" and nlinks < 3:
            cand("#12", f"[[Theses/{p.stem}]] conviction: high but only {nlinks} linked research notes — LLM: verify evidence base")
        if conv == "low" and nlinks >= 5:
            cand("#12", f"[[Theses/{p.stem}]] conviction: low with {nlinks} linked research notes — LLM: under-conviction?")
        # #13 bull/bear asymmetry
        bull = len((section_body(t, "Bull Case") or "").split())
        bear = len((section_body(t, "Bear Case") or "").split())
        if bull and bear and (bull / bear > 3 or bear / bull > 3):
            add("NICE", "#13", f"[[Theses/{p.stem}]] Bull/Bear asymmetry — {bull}w vs {bear}w")
        # #14 template drift (heading presence; Legacy Callouts exempt)
        # #59 template-drift-at-birth (2026-07-09): a thesis created <7d ago that is
        # ALREADY missing template sections means $thesis drifted from the template on
        # this run — escalate immediately instead of letting it sink into the
        # undifferentiated #14 backlog (which only ever grows). Age from earliest Log date.
        first_log = None
        for lm in re.finditer(r"^###\s+(\d{4}-\d{2}-\d{2})", section_body(t, "Log") or "", re.M):
            d0 = parse_date(lm.group(1))
            if d0 and (first_log is None or d0 < first_log):
                first_log = d0
        newborn = first_log is not None and days_old(first_log) < 7
        have = {h for h, *_ in sections(t)}
        for h in tpl_heads:
            if h == "Legacy Callouts" or h in have:
                continue
            if newborn:
                add("IMPORTANT", "#59",
                    f"[[Theses/{p.stem}]] created {days_old(first_log)}d ago, ALREADY missing "
                    f"template section: {h} — $thesis output drifted from the template; fix the "
                    f"thesis now ($deepen {ticker_of(p)} {h} scaffolds it) and check $thesis's "
                    f"required-section list against Templates/.")
            else:
                add("IMPORTANT" if h in priority else "NICE", "#14",
                    f"[[Theses/{p.stem}]] missing template section: {h}")
        # #15 verbose log entries (>2 content lines per dated entry)
        body = section_body(t, "Log") or ""
        entry, hdr = [], None
        for ln in body.split("\n") + ["### END"]:
            if re.match(r"^###\s", ln):
                if hdr and len([l for l in entry if l.strip()]) > 2:
                    add("NICE", "#15", f"[[Theses/{p.stem}]] verbose Log entry {hdr} "
                        f"({len([l for l in entry if l.strip()])} lines, max 2)")
                hdr, entry = ln.replace("###", "").strip(), []
            else:
                entry.append(ln)
        # #28 partial-write candidates (heuristic — LLM confirms)
        for h, _s, _e, body_lines in sections(t):
            if h.lower() == "log":
                if re.search(r"^-\s*Deepening\b", "\n".join(body_lines), re.M) and \
                   "↳ CORRECTION: Deepened" not in "\n".join(body_lines):
                    cand("#28", f"[[Theses/{p.stem}]] Log has 'Deepening' entry with no finalize — possible failed $deepen")
                continue
            txt = strip_code_fences("\n".join(body_lines))
            if txt.count("**") % 2:
                cand("#28", f"[[Theses/{p.stem}]] §{h}: odd '**' count — possible partial write")
            for bl in txt.split("\n"):
                if bl.strip().startswith("|") and not bl.strip().endswith("|"):
                    cand("#28", f"[[Theses/{p.stem}]] §{h}: incomplete table row: {bl.strip()[:60]}")
            words = txt.strip().split()
            if words and words[-1].rstrip(".").lower() in {"and", "but", "or", "of", "in",
                                                           "for", "to", "with", "from", "by"}:
                cand("#28", f"[[Theses/{p.stem}]] §{h}: ends mid-sentence ('…{words[-1]}')")


def snapshots_and_manifests(v):
    if not SNAPSHOTS.is_dir():
        return
    manifests, snaps = [], []
    for p in SNAPSHOTS.glob("*.md"):
        (manifests if p.name.startswith("_") and "manifest" in p.name else snaps).append(p)
    # #16 stale snapshots (>180d; timestamp from filename, mtime fallback)
    for p in snaps:
        m = re.search(r"\((?:[\w-]+)\s+(\d{4}-\d{2}-\d{2})", p.name)
        d = parse_date(m.group(1)) if m else datetime.fromtimestamp(p.stat().st_mtime, timezone.utc).date()
        if d and days_old(d) > 180:
            add("NICE", "#16", f"Stale snapshot ({days_old(d)}d): [[_Archive/Snapshots/{p.stem}]]")
    stats["snapshots"] = len(snaps)
    stats["manifests"] = len(manifests)
    # #58 snapshot-integrity (2026-07-09): artifacts invisible to $clean and
    # unrestorable-by-spec for $rollback. (a) snapshot .md lacking snapshot_of:/
    # snapshot_date: frontmatter — $clean's age logic skips it forever, $rollback
    # Step 5 cannot derive the restore path; (b) any non-.md file in Snapshots/ —
    # invisible even to the '*.md' inventory glob.
    for p in snaps:
        fm = parse_fm(read(p))
        missing = [k for k in ("snapshot_of", "snapshot_date") if not fm.get(k)]
        if missing:
            add("IMPORTANT", "#58",
                f"Snapshot missing {'/'.join(missing)}: [[_Archive/Snapshots/{p.stem}]] — "
                f"invisible to $clean aging, $rollback degrades to content-only restore with "
                f"undefined target path. Backfill frontmatter or archive via git and delete.")
    for p in SNAPSHOTS.iterdir():
        if p.is_file() and p.suffix != ".md":
            size_mb = p.stat().st_size / 1_048_576
            add("IMPORTANT", "#58",
                f"Non-.md artifact in Snapshots/: {p.name} ({size_mb:.1f} MB) — outside every "
                f"skill's inventory; move it out of _Archive/Snapshots/ or delete.")
    # #36/#41/#45/#47/#48/#49 manifest aging
    for p in manifests:
        fm = parse_fm(read(p))
        mtype = str(fm.get("type", "")).replace("-manifest", "")
        chk = MANIFEST_CHECK.get(mtype, "#36")
        status = fm.get("status", "")
        if status == "in-progress":
            add(MANIFEST_INPROG.get(mtype, "IMPORTANT"), chk,
                f"In-progress /{mtype} manifest: [[_Archive/Snapshots/{p.stem}]] — crash or missed flip; "
                f"inspect body, verify landed edits, then flip to completed or recover")
        elif status in ("completed", ""):
            d = parse_date(fm.get("completed_date") or fm.get("date"))
            age = days_old(d) if d else None
            if status == "":
                add("IMPORTANT", chk, f"Manifest missing status: [[_Archive/Snapshots/{p.stem}]] — legacy or corrupt")
            elif age is not None and age > 180:
                add("IMPORTANT", chk, f"Very stale completed {mtype} manifest ({age}d): [[_Archive/Snapshots/{p.stem}]] — safe to delete")
            elif age is not None and age > (30 if mtype == "prune" else 90):
                add("NICE", chk, f"Stale completed {mtype} manifest ({age}d): [[_Archive/Snapshots/{p.stem}]]")
        elif status == "rolled-back":
            pass  # clean abort record (#45)


def markers_and_locks(v):
    # #37 rename markers
    for p in VAULT.glob(".rename_incomplete.*"):
        text = read(p)
        fails = len(re.findall(r"^\s*-\s", section_body(text, "Failed files (Step 5 — wikilink rewrites)") or "", re.M))
        ops = len(re.findall(r"^\s*-\s", section_body(text, "Failed operations (Steps 6–10)") or "", re.M))
        fm = parse_fm(text)
        if fails + ops == 0:
            add("NICE", "#37", f"Empty rename marker {p.name} — auto-delete interrupted; safe to rm or re-run $rename")
        else:
            add("IMPORTANT", "#37", f"Incomplete $rename: {p.name} — {fails} failed file(s) + {ops} failed op(s). "
                f"Re-run $rename {fm.get('ticker', '?')} \"{fm.get('new_name', '?')}\" to repair")
        d = parse_date(fm.get("date"))
        if d and days_old(d) > 7:
            add("IMPORTANT", "#37", f"Rename marker {p.name} is {days_old(d)}d old — repair deferred too long")
    # #38 state marker hygiene
    saf, gi = VAULT / ".sync_all_fresh", VAULT / ".graph_invalidations"
    for f, name, ladders in ((saf, ".sync_all_fresh", ("IMPORTANT", "CRITICAL")),
                             (gi, ".graph_invalidations", ("NICE", "IMPORTANT"))):
        if f.exists():
            h = (NOW - datetime.fromtimestamp(f.stat().st_mtime, timezone.utc)).total_seconds() / 3600
            if h > 168:
                add(ladders[1], "#38", f"{name} is {h/24:.0f}d old — run $graph {'(full)' if name=='.sync_all_fresh' else 'last'}")
            elif h > 24:
                add(ladders[0], "#38", f"{name} is {h:.0f}h old — run $graph {'(full)' if name=='.sync_all_fresh' else 'last'}")
    if saf.exists() and gi.exists():
        add("NICE", "#38", "Both graph markers pending — one $graph (full) consumes both")
    # #43 lock staleness
    for p in VAULT.glob(".vault-lock*"):
        fm = parse_fm(read(p))
        req = [k for k in ("token", "skill", "scope", "started_at", "timeout_at") if k not in fm]
        if req:
            add("IMPORTANT", "#43", f"Malformed lock {p.name} — missing {', '.join(req)}; rm only if no skill running")
            continue
        try:
            tmo = datetime.fromisoformat(str(fm["timeout_at"]).replace("Z", "+00:00"))
            if tmo.tzinfo is None:
                tmo = tmo.replace(tzinfo=timezone.utc)
            if tmo < NOW:
                add("IMPORTANT", "#43", f"Stale lock {p.name} — skill {fm.get('skill')} timed out "
                    f"{(NOW-tmo).total_seconds()/60:.0f}min ago. No auto-steal; rm if confirmed abandoned")
        except ValueError:
            add("IMPORTANT", "#43", f"Lock {p.name} has unparseable timeout_at: {fm.get('timeout_at')}")
    # #46 archive-ticker registry
    reg = VAULT / ".archive_ticker_registry.md"
    if reg.exists():
        n_ok = n_stale = 0
        for ln in read(reg).split("\n"):
            if "|" not in ln:
                continue
            parts = ln.split("|")
            if len(parts) >= 2 and parts[1].strip().endswith(".md"):
                if (ARCHIVE / parts[1].strip()).exists():
                    n_ok += 1
                else:
                    n_stale += 1
                    add("NICE", "#46", f"Stale archive-registry entry: {parts[0].strip()}|{parts[1].strip()} — file not in _Archive/")
        stats["archive_registry"] = f"{n_ok} verified, {n_stale} stale"


def utility_files(v, scoped):
    # #27 catalyst staleness
    cat = VAULT / "_catalyst.md"
    if not scoped:
        if not cat.exists():
            add("NICE", "#27", "_catalyst.md missing — run $catalyst")
        else:
            d = parse_date(parse_fm(read(cat)).get("date")) or \
                datetime.fromtimestamp(cat.stat().st_mtime, timezone.utc).date()
            if days_old(d) > 14:
                add("IMPORTANT", "#27", f"_catalyst.md is {days_old(d)}d old — run $catalyst")
            elif days_old(d) > 7:
                add("NICE", "#27", f"_catalyst.md is {days_old(d)}d old")
    # #35 _hot.md schema (+ #42 truncation) — runs in BOTH modes
    hot = VAULT / "_hot.md"
    if not hot.exists():
        add("NICE", "#35", "_hot.md absent — first $sync will auto-create")
        return
    text = read(hot)
    fm = parse_fm(text)
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(fm.get("date", ""))):
        add("IMPORTANT", "#35", "_hot.md frontmatter date: missing or malformed")
    tags = fm.get("tags", [])
    if not ("meta" in tags and "hot-cache" in tags):
        add("NICE", "#35", "_hot.md tags: missing meta/hot-cache")
    have = [h for h, *_ in sections(text)]
    for s in HOT_SECTIONS:
        if s not in have:
            add("IMPORTANT", "#35", f'_hot.md missing required section "## {s}" — skills editing it will silently no-op')
    present_order = [s for s in have if s in HOT_SECTIONS]
    if present_order != [s for s in HOT_SECTIONS if s in present_order]:
        add("NICE", "#35", "_hot.md sections out of canonical order")
    wc = len(text.split())
    if wc > 5000:
        add("IMPORTANT", "#35", f"_hot.md exceeds 5,000-word hard cap ({wc} words)")
    elif wc > 4000:
        add("NICE", "#35", f"_hot.md over soft cap ({wc}/4,000 words) — auto-compresses next update")
    # #42 truncation markers
    body = strip_code_fences(text)
    for i, ln in enumerate(body.split("\n"), 1):
        if re.search(r"^\s*-.*[^.]\.\.\.\s*$", ln) or re.search(r"\[(compressed|truncated|\.\.\.)\]", ln):
            add("IMPORTANT", "#42", f"_hot.md truncation marker at line {i}: {ln.strip()[:70]}")
    for h, _s, _e, bl in sections(body):
        if "\n".join(bl).count("**") % 2:
            add("IMPORTANT", "#42", f"_hot.md §{h}: unclosed ** formatting")


def graph_checks(v):
    g = VAULT / "_graph.md"
    if not g.exists():
        add("IMPORTANT", "#17", "_graph.md missing — run $graph")
        return
    text = read(g)
    fm = parse_fm(text)
    # #18 staleness
    lgw = fm.get("last_graph_write")
    if lgw:
        try:
            ts = datetime.fromisoformat(str(lgw).replace("Z", "+00:00"))
            age_h = (NOW - ts).total_seconds() / 3600
            if age_h > 720:
                add("CRITICAL", "#18", f"_graph.md is {age_h/24:.0f}d stale — run $graph now")
            elif age_h > 168:
                add("IMPORTANT", "#18", f"_graph.md is {age_h/24:.0f}d stale — run $graph")
            elif age_h > 24:
                add("NICE", "#18", f"_graph.md is {age_h/24:.1f}d old — run $graph last")
        except ValueError:
            add("NICE", "#18", f"_graph.md last_graph_write unparseable: {lgw}")
    else:
        add("NICE", "#18", "_graph.md lacks last_graph_write: — next $graph upgrades to ISO precision")
    # adjacency parse
    adj_body = section_body(text, "Thesis Adjacency Index") or ""
    entries = {}
    cur = None
    for ln in adj_body.split("\n"):
        m = re.match(r"^###\s+(.*)$", ln)
        if m:
            cur = m.group(1).strip()
            entries[cur] = {"sectors": [], "macros": [], "cross-thesis": [], "research": []}
        elif cur:
            fm2 = re.match(r"^\s*-\s*\*\*(sectors|macros|cross-thesis|research):\*\*\s*(.*)$", ln)
            if fm2:
                entries[cur][fm2.group(1)] = [t.split("|")[0].split("#")[0]
                                              for t in WIKILINK_RE.findall(fm2.group(2))]
    thesis_stems = {p.stem for p in v["theses"]}
    # #19 / #20
    for s in sorted(thesis_stems - set(entries)):
        add("IMPORTANT", "#19", f"Thesis missing from _graph.md adjacency: [[Theses/{s}]] — $sync won't propagate to it; run $graph")
    for s in sorted(set(entries) - thesis_stems):
        add("IMPORTANT", "#20", f"Ghost graph entry: ### {s} — no Theses/{s}.md; run $graph")
    # #21 broken graph edges
    for ent, fields in entries.items():
        for field, links in fields.items():
            for tgt in links:
                if not link_resolves(tgt, v):
                    sev = "IMPORTANT" if field in ("cross-thesis", "research") else "NICE"
                    add(sev, "#21", f"Broken graph edge in {ent} ({field}): [[{tgt}]]")
    # #22 frontmatter counts
    actual = {"theses": len(v["theses"]), "sectors": len(v["sectors"]), "macro": len(v["macro"])}
    for key, act in actual.items():
        try:
            claimed = int(fm.get(key, -1))
            if claimed >= 0 and abs(claimed - act) > 2:
                add("IMPORTANT", "#22", f"_graph.md frontmatter {key}: {claimed} vs actual {act}")
        except (ValueError, TypeError):
            pass
    # #23 reverse-index accuracy. The generator builds each reverse row from a
    # macro/sector file's OUTBOUND [[Theses/...]] links (generate_graph.py rev_for).
    # This is NOT the transpose of thesis→macro adjacency — a thesis linking a macro
    # and that macro linking the thesis back are independent facts, so the prior
    # transpose check fired on every fresh graph (~250 FPs). Correct invariant: the
    # parsed reverse rows must equal a recompute from the live macro/sector bodies,
    # replicating rev_for exactly (Theses/-prefixed, resolving, .md/alias-normalized).
    def parse_reverse(name):
        body = section_body(text, name) or ""
        rev = {}
        for ln in body.split("\n"):
            cells = [c.strip() for c in ln.split("|")]
            if len(cells) >= 3 and "[[" in cells[1] and cells[1] != "---":
                key = WIKILINK_RE.findall(cells[1])
                if key:
                    rev[key[0].replace("\\|", "|").split("|")[0].split("/")[-1]] = {
                        t.replace("\\|", "|").split("|")[0].split("/")[-1]
                        for t in WIKILINK_RE.findall(cells[2])}
        return rev
    rev_macro = parse_reverse("Reverse Index: Macro → Theses")
    rev_sector = parse_reverse("Reverse Index: Sector → Theses")

    def gen_theses_links(body):  # mirror generate_graph.py extract_links + rev_for filter
        out = set()
        for mm in WIKILINK_RE.finditer(body):
            raw = mm.group(1).replace("\\|", "|").split("|")[0].split("#")[0].strip()
            if raw.endswith(".md"):
                raw = raw[:-3]
            if raw.startswith("Theses/") and raw[len("Theses/"):] in thesis_stems:
                out.add(raw[len("Theses/"):])
        return out

    def check_rev(kind, files_dict, parsed):
        for p, t in files_dict.items():
            actual = gen_theses_links(t)
            if not actual:
                continue  # generator emits no reverse row for a note with zero thesis links
            got = parsed.get(p.stem, set())
            if p.stem not in parsed:
                add("IMPORTANT", "#23", f"{kind} reverse-index stale: [[{p.stem}]] links "
                    f"{len(actual)} thesis/es but has no reverse row — run $graph")
            elif got != actual:
                miss, extra = actual - got, got - actual
                det = (["missing " + "+".join(sorted(miss))] if miss else []) + \
                      (["stale " + "+".join(sorted(extra))] if extra else [])
                add("IMPORTANT", "#23", f"{kind} reverse-index drift for [[{p.stem}]]: "
                    f"{'; '.join(det)} — run $graph")
    check_rev("Macro", v["macro"], rev_macro)
    check_rev("Sector", v["sectors"], rev_sector)
    # #24 orphan list accuracy
    listed_orphans = {t.split("/")[-1] for t in WIKILINK_RE.findall(section_body(text, "Orphan Research Notes") or "")}
    computed = v.get("computed_orphans", set())
    for o in sorted(listed_orphans - computed):
        add("NICE", "#24", f"False orphan in graph: [[Research/{o}]] is now linked from a thesis — run $graph")
    for o in sorted(computed - listed_orphans):
        add("NICE", "#24", f"Missing orphan in graph list: [[Research/{o}]] — run $graph")
    # #26 edge count accuracy. generate_graph.py `edges:` = every categorized adjacency
    # link PLUS every reverse-index member (not log_tail links). Prior code counted
    # adjacency-section wikilinks only (incl. log_tail, excl. reverse rows) → structural
    # ~15% drift on every fresh graph. Recompute the generator's exact definition.
    adj_edges = sum(len(links) for e in entries.values() for links in e.values())
    rev_members = sum(len(m) for m in rev_macro.values()) + sum(len(m) for m in rev_sector.values())
    actual_edges = adj_edges + rev_members
    try:
        claimed = int(fm.get("edges", -1))
        if claimed > 0:
            drift = abs(claimed - actual_edges) / claimed
            if drift > 0.25:
                add("IMPORTANT", "#26", f"_graph.md edges: {claimed} vs actual {actual_edges} ({drift:.0%} drift)")
            elif drift > 0.10:
                add("NICE", "#26", f"_graph.md edges: {claimed} vs actual {actual_edges} ({drift:.0%} drift)")
    except (ValueError, TypeError):
        pass


def contracts(v, scoped_theses):
    # #30 / #34 sector resolution + standardization
    sector_stems = {p.stem: p for p in v["sectors"]}
    norm_map = {norm_sector(s): s for s in sector_stems}
    tallies = {"exact": 0, "normalized": 0, "substring": 0, "none": 0}
    seen_values = {}
    for p, _t in (scoped_theses or v["theses"]).items():
        sec = v["fm"].get(p, {}).get("sector", "")
        if not sec:
            continue
        seen_values.setdefault(sec, []).append(p.stem)
        if sec in sector_stems:
            conf = "exact"
        elif norm_sector(sec) in norm_map:
            conf = "normalized"
        elif any(norm_sector(sec) in n or n in norm_sector(sec) for n in norm_map if len(norm_sector(sec)) > 4):
            conf = "substring"
        else:
            conf = "none"
        tallies[conf] += 1
        tick = ticker_of(p)
        if conf == "none":
            close = difflib.get_close_matches(sec, list(sector_stems), n=1)
            add("IMPORTANT", "#30", f"Sector resolution FAILED for {tick} — \"{sec}\" matches no Sectors/*.md"
                + (f" (closest: \"{close[0]}\")" if close else "") + ". Skills will silently skip sector updates")
        elif conf in ("substring", "normalized"):
            add("NICE", "#30", f"Sector resolved via {conf} for {tick}: \"{sec}\" — standardize to exact")
    stats["sector_resolution"] = ", ".join(f"{k}: {n}" for k, n in tallies.items())
    if not scoped_theses:
        for val, users in sorted(seen_values.items()):
            if val not in sector_stems and norm_sector(val) not in norm_map:
                close = difflib.get_close_matches(val, list(sector_stems), n=1)
                add("IMPORTANT", "#34", f"{len(users)} thesis file(s) use sector \"{val}\" — no exact/normalized match"
                    + (f"; closest \"{close[0]}\"" if close else ""))

    if scoped_theses:
        return
    # #32 orphaned ticker refs in research (ticker: field only; tag heuristic → LLM)
    thesis_ticks = {ticker_of(p) for p in v["theses"]}
    archive_ticks = {f.stem.split(" - ")[0].strip() for f in ARCHIVE.glob("*.md")}
    for p in v["research"]:
        ticks = fm_tickers(v["fm"].get(p, {}))
        # flag only when NONE of the note's tickers has a live thesis — a multi-ticker
        # note still propagates if at least one ticker resolves (prior code stringified
        # the whole list → always "matched no thesis").
        if ticks and not any(tk in thesis_ticks for tk in ticks):
            note = " (archived thesis exists)" if any(tk in archive_ticks for tk in ticks) else ""
            add("NICE" if note else "IMPORTANT", "#32",
                f"Research ticker(s) {', '.join(ticks)} match no thesis{note}: [[Research/{p.stem}]] — $sync cannot propagate")
    # #33 closed theses in Theses/
    for p, _t in v["theses"].items():
        if v["fm"].get(p, {}).get("status") == "closed":
            add("IMPORTANT", "#33", f"status: closed but still in Theses/: [[Theses/{p.stem}]] — failed archive move")
    # #39 propagated_to producer contract
    mandate = {"scenario": "list", "stress-test": "list", "comparison": "list",
               "synthesis": "terminal", "brief": "terminal", "retrospective": "terminal"}
    n_ok = n_viol = n_pre = 0
    for p in v["research"]:
        fm = v["fm"].get(p, {})
        st = fm.get("source_type", "")
        if st not in mandate:
            continue
        has = "propagated_to" in fm
        d = parse_date(fm.get("date"))
        if mandate[st] == "terminal":
            if not has or fm["propagated_to"] != []:
                if not has:
                    n_viol += 1
                    add("IMPORTANT", "#39", f"Producer contract violation: [[Research/{p.stem}]] ({st}) "
                        f"missing terminal propagated_to: [] — $sync may spam every body-linked thesis")
                else:
                    n_ok += 1
            else:
                n_ok += 1
        else:
            if has:
                n_ok += 1
            elif d and d >= SPEC_DATE:
                n_viol += 1
                dbl = " 🚨 also orphan (#1)" if p.stem in v.get("computed_orphans", set()) else ""
                add("IMPORTANT", "#39", f"[[Research/{p.stem}]] ({st}) has no propagated_to: — "
                    f"atomicity retry pending or producer drift; verify thesis Logs{dbl}")
            else:
                n_pre += 1
    stats["propagated_to"] = f"{n_ok} compliant, {n_viol} violations, {n_pre} pre-spec"
    # #44 scenario reversal completeness
    for p, t in v["research"].items():
        if v["fm"].get(p, {}).get("source_type") != "scenario":
            continue
        if "REVERSED" not in t and "Reversal Notes" not in t:
            continue
        missing = []
        for tick in v["fm"].get(p, {}).get("propagated_to", []) or []:
            live = [tp for tp in v["theses"] if ticker_of(tp) == str(tick).split(".")[0]]
            if live and f"Scenario REVERSED" not in v["theses"][live[0]]:
                missing.append(tick)
            elif not live and str(tick) not in (section_body(t, "Reversal Notes") or ""):
                missing.append(f"{tick} (archived)")
        if missing:
            add("IMPORTANT", "#44", f"Scenario reversal incomplete: [[Research/{p.stem}]] — "
                f"no reversal record for {', '.join(map(str, missing))}")
    # #29 log-prefix registry alignment (presence checks; semantics → LLM)
    regf = SKILLS / "_shared" / "log-prefixes.md"
    if not regf.exists():
        add("CRITICAL", "#29", "log-prefixes.md registry missing — restore from git")
    else:
        rtext = read(regf)
        all_thesis_text = "\n".join(v["theses"].values())
        for block in re.findall(r"```yaml\n(.*?)```", rtext, re.S):
            pm = re.search(r'^prefix:\s*"([^"]+)"', block, re.M)
            prod = re.search(r"producer:\s*\n\s*skill:\s*(/\S+)", block)
            emits = re.search(r"emits_when:\s*(.*)$", block, re.M)
            if not pm:
                continue
            prefix = pm.group(1)
            def skill_dir_text(name):
                d = SKILLS / name.lstrip("/")
                return "\n".join(read(f) for f in list(d.glob("SKILL.md")) + list(d.glob("*.py")))
            if prod:
                if (SKILLS / prod.group(1).lstrip("/")).is_dir() and prefix not in skill_dir_text(prod.group(1)):
                    add("CRITICAL", "#29", f"Producer drift: {prod.group(1)} no longer contains prefix \"{prefix}\"")
            for cm in re.findall(r"-\s*skill:\s*(/\S+)", block.split("consumers:")[-1]):
                if (SKILLS / cm.lstrip("/")).is_dir() and prefix not in skill_dir_text(cm):
                    add("CRITICAL", "#29", f"Consumer drift: {cm} no longer references prefix \"{prefix}\"")
            # "Deepening" is transient — replaced by "Deepened" at Phase 5c finalize, so
            # vault absence is the healthy state (its persistence is what #28 flags).
            if emits and emits.group(1).strip().startswith("always") and prefix != "Deepening":
                if not re.search(r"^\s*-\s*" + re.escape(prefix), all_thesis_text, re.M):
                    add("IMPORTANT", "#29", f"Prefix \"{prefix}\" absent from all thesis Logs despite "
                        f"producer {prod.group(1) if prod else '?'} claiming emits_when: always")
        lr = re.search(r"last_reviewed:\s*(\d{4}-\d{2}-\d{2})", rtext)
        if lr and days_old(parse_date(lr.group(1))) > 90:
            add("NICE", "#29", f"log-prefixes.md last_reviewed {lr.group(1)} (>90d) — review registry")
    # #54 / #55 graph-primer contract
    primer = SKILLS / "_shared" / "graph-primer.md"
    if not primer.exists():
        add("CRITICAL", "#54", "graph-primer.md contract missing — restore from git")
    else:
        consumers = ["ingest", "compare", "thesis", "stress-test", "brief", "deepen"]
        anti = [r"skip.*(not in cluster|not in graph|absent from adjacency)",
                r"only.*(cluster peers|peer theses|cluster members).*(read|analyze|propagate)",
                r"substitute.*log_tail", r"trust.*cross-thesis.*complete",
                r"graph says.*(not connected|isn'?t connected|no connection)"]
        for c in consumers:
            sk = SKILLS / c / "SKILL.md"
            if not sk.exists():
                continue
            st = read(sk)
            if "_graph.md" not in st and "graph-primer" not in st:
                add("NICE", "#54", f"/{c} declared graph-primer consumer but SKILL.md never references _graph.md")
            for pat in anti:
                for m in re.finditer(pat, st, re.I):
                    cand("#55", f"/{c} SKILL.md matches anti-pattern /{pat[:40]}…/ near: "
                         f"\"{st[max(0, m.start()-30):m.end()+30].strip()}\" — LLM: review intent")


def callouts(v, scoped_theses):
    pool = dict(scoped_theses or v["theses"])
    if not scoped_theses:
        pool.update(v["sectors"])
        pool.update(v["macro"])
    for p, t in pool.items():
        fm = v["fm"].get(p, {})
        is_thesis = p.parent.name == "Theses"
        addressed_dates, fresh = [], []
        for ln in t.split("\n"):
            m = CALLOUT_RE.match(ln)
            if not m:
                continue
            rest = m.group(3)
            if "[[pinned]]" in rest:
                continue
            am = re.search(r"→ Addressed (\d{4}-\d{2}-\d{2})", rest)
            if am:
                addressed_dates.append(parse_date(am.group(1)))
            else:
                fresh.append((m.group(1), parse_date(m.group(2))))
        # #51 stale fresh callouts
        for ctype, d in fresh:
            if d and days_old(d) > 180:
                add("IMPORTANT", "#51", f"{p.relative_to(VAULT)}: fresh [{ctype}] callout from {d} abandoned "
                    f"({days_old(d)}d) — address, pin, or delete")
            elif d and days_old(d) > 90:
                add("NICE", "#51", f"{p.relative_to(VAULT)}: fresh [{ctype}] callout from {d} ({days_old(d)}d old)")
        # #50 sweep freshness (theses only, active/monitoring)
        if is_thesis and fm.get("status") in ("active", "monitoring"):
            lcs = parse_date(fm.get("last_callout_sweep"))
            oldest = min((d for d in addressed_dates if d), default=None)
            eligible = oldest and days_old(oldest) >= 180
            if lcs is None and eligible:
                add("NICE", "#50", f"{ticker_of(p)}: no last_callout_sweep; oldest addressed callout "
                    f"{days_old(oldest)}d — run $archive-callouts {ticker_of(p)}")
            elif lcs and days_old(lcs) > 180 and eligible:
                add("NICE", "#50", f"{ticker_of(p)}: last sweep {days_old(lcs)}d ago; sweep-eligible callouts exist")
        # #52 / #53 legacy callouts
        legacy = section_body(t, "Legacy Callouts")
        heads = [h for h, *_ in sections(t)]
        entry_re = re.compile(r"^-\s+\*\*\d{4}-\d{2}-\d{2}\*\*\s+·\s+(question|warning|tip|todo)\s+·\s+.+·\s+raised \d{4}-\d{2}-\d{2}\s+→\s+.+")
        if legacy is not None:
            bullets = [l for l in legacy.split("\n") if l.strip().startswith("- ")]
            for i, b in enumerate(bullets):
                if not entry_re.match(b.strip()):
                    add("IMPORTANT", "#52", f"{p.relative_to(VAULT)}: malformed Legacy Callouts entry: \"{b.strip()[:70]}\"")
            has_sweep_log = "Callout sweep:" in (section_body(t, "Log") or "")
            if not bullets:
                add("NICE", "#53", f"{p.relative_to(VAULT)}: empty ## Legacy Callouts section — harmless; delete or leave")
            elif not has_sweep_log:
                add("IMPORTANT", "#53", f"{p.relative_to(VAULT)}: Legacy Callouts has {len(bullets)} entries but "
                    f"no 'Callout sweep:' Log entry — audit trail broken or hand-authored")
            if "Related Research" in heads and "Log" in heads and "Legacy Callouts" in heads:
                if not (heads.index("Related Research") < heads.index("Legacy Callouts") < heads.index("Log")):
                    add("NICE", "#53", f"{p.relative_to(VAULT)}: Legacy Callouts not between Related Research and Log")
        elif "Callout sweep:" in (section_body(t, "Log") or ""):
            add("IMPORTANT", "#53", f"{p.relative_to(VAULT)}: 'Callout sweep:' Log entries exist but "
                f"## Legacy Callouts section absent — section deleted? $rollback pre-sweep snapshot")
        # #56 deprecated [[preserve]]
        in_log = fenced = False
        for i, ln in enumerate(t.split("\n"), 1):
            if ln.strip().startswith("```"):
                fenced = not fenced
            if ln.startswith("## ") and not ln.startswith("###"):
                in_log = ln[3:].strip().lower() == "log"
            if not fenced and not in_log and "[[preserve]]" in ln and "<!--" not in ln:
                add("NICE", "#56", f"{p.relative_to(VAULT)}:{i}: deprecated [[preserve]] — replace with [[pinned]]")


# ---------------------------------------------------------------- report
def report(scoped):
    order = {"CRITICAL": 0, "IMPORTANT": 1, "NICE": 2}
    findings.sort(key=lambda f: (order.get(f[0], 3), f[1]))
    n_crit = sum(1 for f in findings if f[0] == "CRITICAL")
    n_imp = sum(1 for f in findings if f[0] == "IMPORTANT")
    n_nice = sum(1 for f in findings if f[0] == "NICE")
    print(f"# Vault Lint Report — deterministic pass ({TODAY})")
    print(f"Mode: {'scoped ' + scoped if scoped else 'full vault'} · "
          f"{n_crit} Critical / {n_imp} Important / {n_nice} Nice to Have / {len(candidates)} judgment candidates\n")
    print("Deterministic checks run by lint.py. LLM-judgment checks (#5-thin, #7, #9, #12/#13 interpretation, "
          "#14 nuance, #28 confirm, #29 reverse+semantic, #55 review) run separately by $lint.\n")
    for sev, title in (("CRITICAL", "Critical (breaks research quality)"),
                       ("IMPORTANT", "Important (gaps in coverage)"),
                       ("NICE", "Nice to Have (optimization)")):
        rows = [f for f in findings if f[0] == sev]
        print(f"### {title}")
        if rows:
            for _s, chk, msg in rows:
                print(f"- [ ] {chk} {msg}")
        else:
            print("- none")
        print()
    print("### Judgment candidates (input for the LLM pass — NOT confirmed findings)")
    if candidates:
        for chk, msg in candidates:
            print(f"- {chk} {msg}")
    else:
        print("- none")
    print("\n### Stats")
    for k, val in stats.items():
        print(f"- {k}: {val}")
    return 2 if n_crit else (1 if n_imp else 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticker", help="scoped mode: lint one thesis")
    args = ap.parse_args()

    if not THESES.is_dir() or not RESEARCH.is_dir():
        print(f"SELF-VALIDATION FAILED: vault dirs not found under {VAULT}", file=sys.stderr)
        return 3
    v = load()
    if not v["theses"]:
        print("SELF-VALIDATION FAILED: zero theses read — wrong vault root?", file=sys.stderr)
        return 3

    scoped_theses = None
    if args.ticker:
        scoped_theses = {p: t for p, t in v["theses"].items()
                         if ticker_of(p).upper() == args.ticker.upper()}
        if not scoped_theses:
            print(f"SELF-VALIDATION FAILED: no thesis for ticker {args.ticker}", file=sys.stderr)
            return 3

    stats["theses"] = len(v["theses"])
    st_counts = {}
    for p in v["theses"]:
        st_counts[v["fm"].get(p, {}).get("status", "?")] = st_counts.get(v["fm"].get(p, {}).get("status", "?"), 0) + 1
    stats["thesis status"] = ", ".join(f"{k}: {n}" for k, n in sorted(st_counts.items()))
    stats["research"] = len(v["research"])
    stats["sectors"] = len(v["sectors"])
    stats["macro"] = len(v["macro"])
    ages = [days_old(last_log_date(t)) for t in v["theses"].values() if last_log_date(t)]
    if ages:
        stats["avg days since last Log entry"] = f"{sum(ages)/len(ages):.0f}"

    structural(v, scoped_theses)
    freshness(v, scoped_theses)
    if not scoped_theses:
        connections(v)
        snapshots_and_manifests(v)
        markers_and_locks(v)
        graph_checks(v)
    analytical(v, scoped_theses)
    contracts(v, scoped_theses)
    utility_files(v, bool(scoped_theses))
    callouts(v, scoped_theses)
    return report(args.ticker)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # self-validation contract: never emit a partial report silently
        print(f"SELF-VALIDATION FAILED: lint.py crashed: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(3)
