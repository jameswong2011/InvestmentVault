#!/usr/bin/env python3
"""/graph engine — deterministic vault-graph generator.

Replaces the legacy LLM extraction + incremental machinery. Reads the vault and
writes _graph.md directly, so the file never streams through a model response —
this eliminates the max-output-token failure that broke /graph at vault scale
(2026-06-04: 57-min runs ending in max-output-token errors on /graph + /graph last).

Usage:  generate_graph.py [full|last|N]
  full      always (re)write _graph.md          (disaster-recovery semantics)
  last | N  write only if the body changed OR a force-marker is present;
            otherwise leave _graph.md untouched and report up-to-date.
            (N is accepted for backward-compat with `/graph [N]`; treated as `last`.)

Force-markers (any present => write even on no-op, then delete after success):
  .sync_all_fresh        (written by `/sync all`)
  .graph_invalidations   (written by `/status`, `/prune` on thesis closures)

Exit codes:  0 ok (written or up-to-date) | 2 self-validation failed | 1 runtime error
"""
import os, re, sys, glob, datetime
from collections import Counter

# --- locate vault root (works regardless of cwd) ---
_here = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(_here, "..", "..", ".."))
if not os.path.isdir(os.path.join(VAULT, "Theses")):
    VAULT = os.getcwd()
os.chdir(VAULT)

MODE = (sys.argv[1].strip() if len(sys.argv) > 1 else "full")
GRAPH_MODE = "full" if MODE == "full" else ("last" if MODE == "last" else f"{MODE}")

WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")


def basenames(folder):
    return set(os.path.splitext(os.path.basename(p))[0] for p in glob.glob(f"{folder}/*.md"))


THESES, SECTORS = basenames("Theses"), basenames("Sectors")
MACROS, RESEARCH = basenames("Macro & Technology"), basenames("Research")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def extract_links(text):
    out = []
    for m in WIKILINK.finditer(text):
        inner = m.group(1).replace("\\|", "|")  # Obsidian table-escaped alias pipe (\|)
        raw = inner.split("|")[0].split("#")[0].strip()
        if raw.endswith(".md"):
            raw = raw[:-3]
        out.append(raw)
    return out


dangling = []  # (source, link) for known-prefix links that don't resolve


def categorize(src, links):
    sec, mac, cross, res = set(), set(), set(), set()
    for l in links:
        if l in ("pinned", "preserve"):
            continue
        if l.startswith("Sectors/"):
            n = l[len("Sectors/"):]
            sec.add(n) if n in SECTORS else dangling.append((src, l))
        elif l.startswith("Macro & Technology/"):
            n = l[len("Macro & Technology/"):]
            mac.add(n) if n in MACROS else dangling.append((src, l))
        elif l.startswith("Macro/"):
            dangling.append((src, l + " [legacy Macro/ prefix]"))
        elif l.startswith("Theses/"):
            n = l[len("Theses/"):]
            cross.add(n) if n in THESES else dangling.append((src, l))
        elif l.startswith("Research/"):
            n = l[len("Research/"):]
            res.add(n) if n in RESEARCH else dangling.append((src, l))
        # bare / other -> ignore per skill Step 2 categorization rule
    return sec, mac, cross, res


def get_status(text):
    m = re.search(r"^status:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else "unknown"


def get_log_tail(text):
    in_log, pending, entries = False, None, []
    for ln in text.splitlines():
        if re.match(r"^## Log\s*$", ln):
            in_log = True
            continue
        if in_log and re.match(r"^## ", ln):
            break
        if in_log:
            m = re.match(r"^### (\d{4}-\d{2}-\d{2}.*)$", ln)
            if m:
                pending = m.group(1).strip()
                continue
            if pending and re.match(r"^- ", ln):
                body = ln[2:].strip()
                if len(body) > 100:
                    body = body[:100] + "…"  # horizontal ellipsis (… ) — /lint #42 safe
                entries.append(f"{pending} | {body}")
                pending = None
    return entries[-3:] if entries else ["—"]  # em dash if no Log


def rev_for(path):
    out = set()
    for l in extract_links(read(path)):
        if l.startswith("Theses/"):
            n = l[len("Theses/"):]
            out.add(n) if n in THESES else dangling.append((os.path.basename(path), l))
    return sorted(out)


def fmt(prefix, names):
    return ", ".join(f"[[{prefix}{n}]]" for n in names) if names else "—"


def build_body():
    """Return (body_str, stats). body_str is everything after the closing '---\\n'."""
    adj = {}
    for t in sorted(THESES):
        text = read(f"Theses/{t}.md")
        sec, mac, cross, res = categorize(t, extract_links(text))
        cross.discard(t)
        adj[t] = dict(sectors=sorted(sec), macros=sorted(mac), cross=sorted(cross),
                      research=sorted(res), status=get_status(text), log_tail=get_log_tail(text))

    macro_rev = {m: rev_for(f"Macro & Technology/{m}.md") for m in MACROS}
    sector_rev = {s: rev_for(f"Sectors/{s}.md") for s in SECTORS}

    # clusters: bidirectional cross-thesis, union-find
    edges_set = {(a, b) for a, d in adj.items() for b in d["cross"]}
    bidir = {frozenset((a, b)) for (a, b) in edges_set if (b, a) in edges_set}
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        r = x
        while parent[r] != r:
            r = parent[r]
        while parent[x] != r:
            parent[x], x = r, parent[x]
        return r

    for pair in bidir:
        a, b = tuple(pair)
        parent[find(a)] = find(b)
    comps = {}
    for n in list(parent):
        comps.setdefault(find(n), set()).add(n)
    clusters = sorted((sorted(m) for m in comps.values() if len(m) >= 2), key=lambda c: c[0])

    def basis(members):
        c = Counter(s for m in members for s in adj[m]["sectors"])
        shared = sorted(s for s, n in c.items() if n == len(members))
        if shared:
            return f"Shared sector: {', '.join(shared)} — bidirectional cross-reference"
        if c:
            top, n = c.most_common(1)[0]
            return f"Overlap: {top} ({n}/{len(members)}) — bidirectional cross-reference"
        return "Bidirectional cross-reference"

    edge_count = sum(len(d["sectors"]) + len(d["macros"]) + len(d["cross"]) + len(d["research"])
                     for d in adj.values())
    edge_count += sum(len(v) for v in macro_rev.values()) + sum(len(v) for v in sector_rev.values())
    linked = set().union(*(d["research"] for d in adj.values())) if adj else set()
    orphans = sorted(RESEARCH - linked)

    L = []
    L.append("\n# Investment Vault Graph\n")
    L.append(f"Structural metadata regenerated by /graph (deterministic full rebuild). "
             f"{len(THESES)} theses × {edge_count} validated edges across {len(SECTORS)} "
             f"sector notes, {len(MACROS)} macro notes, {len(RESEARCH)} research notes.\n")
    L.append("## Thesis Adjacency Index\n")
    for t in sorted(THESES):
        d = adj[t]
        L.append(f"### {t}")
        L.append(f"  - **sectors:** {fmt('Sectors/', d['sectors'])}")
        L.append(f"  - **macros:** {fmt('Macro & Technology/', d['macros'])}")
        L.append(f"  - **cross-thesis:** {fmt('Theses/', d['cross'])}")
        L.append(f"  - **research:** {fmt('Research/', d['research'])}")
        L.append(f"  - **status:** {d['status']}")
        L.append("  - **log_tail:**")
        for e in d["log_tail"]:
            L.append(f"    - {e}")
        L.append("")
    L.append("## Reverse Index: Macro → Theses\n")
    L.append("| Macro Note | Theses |\n|---|---|")
    for m in sorted(MACROS):
        if macro_rev[m]:
            L.append(f"| [[Macro & Technology/{m}]] | {fmt('Theses/', macro_rev[m])} |")
    L.append("")
    L.append("## Reverse Index: Sector → Theses\n")
    L.append("| Sector Note | Theses |\n|---|---|")
    for s in sorted(SECTORS):
        if sector_rev[s]:
            L.append(f"| [[Sectors/{s}]] | {fmt('Theses/', sector_rev[s])} |")
    L.append("")
    L.append("## Cross-Thesis Clusters\n")
    L.append("| # | Members | Shared Basis |\n|---|---|---|")
    for i, members in enumerate(clusters, 1):
        mem = ", ".join(f"[[Theses/{m}]]" for m in members)
        L.append(f"| {i} | {mem} | {basis(members)} |")
    L.append("\n---\n")
    L.append("## Orphan Research Notes\n")
    L.append("_Research notes not linked from any thesis. Consider linking to a thesis's Related "
             "Research or running `/ingest` to create a new thesis._\n")
    for o in orphans:
        L.append(f"- [[Research/{o}]]")
    body = "\n".join(L) + "\n"

    stats = dict(theses=len(THESES), sectors=len(SECTORS), macro=len(MACROS),
                 research=len(RESEARCH), edges=edge_count, orphans=orphans,
                 clusters=clusters, sector_rows=sum(1 for s in SECTORS if sector_rev[s]),
                 empty_sectors=sorted(s for s in SECTORS if not sector_rev[s]))
    return body, stats


def frontmatter(stats, now_iso, today):
    return ("---\n"
            "type: vault-graph\n"
            f"date: {today}\n"
            f"last_graph_write: {now_iso}\n"
            f"graph_mode: {GRAPH_MODE}\n"
            f"theses: {stats['theses']}\n"
            f"sectors: {stats['sectors']}\n"
            f"macro: {stats['macro']}\n"
            f"research: {stats['research']}\n"
            f"edges: {stats['edges']}\n"
            f"orphans: {len(stats['orphans'])}\n"
            "---\n")


def existing_body():
    if not os.path.exists("_graph.md"):
        return None
    parts = read("_graph.md").split("---\n", 2)
    return parts[2] if len(parts) == 3 else None


def self_validate(stats):
    """Re-read written file; return list of failures (empty == pass)."""
    txt = read("_graph.md")
    fails = []
    for h in ["## Thesis Adjacency Index", "## Reverse Index: Macro → Theses",
              "## Reverse Index: Sector → Theses", "## Cross-Thesis Clusters",
              "## Orphan Research Notes"]:
        if h not in txt:
            fails.append(f"missing section: {h}")
    n_entries = len(re.findall(r"^### ", txt, re.M))
    if n_entries != stats["theses"]:
        fails.append(f"### entries {n_entries} != theses {stats['theses']}")
    for field in ["status", "log_tail"]:
        c = txt.count(f"**{field}:**")
        if c != stats["theses"]:
            fails.append(f"{field}: count {c} != theses {stats['theses']}")
    return fails


def main():
    now = datetime.datetime.now(datetime.timezone.utc)
    now_iso, today = now.strftime("%Y-%m-%dT%H:%M:%SZ"), now.strftime("%Y-%m-%d")

    body, stats = build_body()
    markers = [m for m in (".sync_all_fresh", ".graph_invalidations") if os.path.exists(m)]
    prior = existing_body()
    forced = (MODE == "full") or bool(markers) or prior is None
    changed = (prior != body)

    if not forced and not changed:
        print(f"STATUS=up-to-date mode={GRAPH_MODE} (body unchanged; _graph.md left untouched)")
        print(f"theses={stats['theses']} sectors={stats['sectors']} macro={stats['macro']} "
              f"research={stats['research']} edges={stats['edges']} orphans={len(stats['orphans'])} "
              f"clusters={len(stats['clusters'])}")
        return 0

    with open("_graph.md", "w", encoding="utf-8") as f:
        f.write(frontmatter(stats, now_iso, today))
        f.write(body)

    fails = self_validate(stats)
    cleared = []
    if not fails:
        for m in markers:
            try:
                os.remove(m); cleared.append(m)
            except OSError:
                pass

    reason = "full-rebuild" if MODE == "full" else \
             ("force-marker:" + ",".join(markers) if markers else
              ("file-missing" if prior is None else "body-changed"))
    print(f"STATUS={'written' if not fails else 'written-with-validation-errors'} "
          f"mode={GRAPH_MODE} reason={reason}")
    print(f"theses={stats['theses']} sectors={stats['sectors']} macro={stats['macro']} "
          f"research={stats['research']} edges={stats['edges']} orphans={len(stats['orphans'])} "
          f"clusters={len(stats['clusters'])} sector_rows={stats['sector_rows']}")
    print("markers_cleared=" + (",".join(cleared) if cleared else "none"))
    for c in stats["clusters"]:
        print("CLUSTER: " + " + ".join(c))
    print(f"orphans ({len(stats['orphans'])}): " + (", ".join(stats["orphans"]) or "none"))
    print(f"dangling_dropped={len(dangling)} (unique={len(set(l for _, l in dangling))})")
    if stats["empty_sectors"]:
        print("empty_sectors: " + ", ".join(stats["empty_sectors"]))
    if fails:
        print("VALIDATION FAILURES:")
        for x in fails:
            print("  ! " + x)
        return 2
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
