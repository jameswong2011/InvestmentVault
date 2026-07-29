#!/usr/bin/env python3
"""PostToolUse marker — flag _graph.md as stale after a graph-relevant edit.

Fires on Write | Edit | MultiEdit. If the written file is a Thesis / Sector /
Macro note (the only inputs that change graph adjacency), touch
.claude/.graph_dirty. The Stop hook (refresh-graph.py) reads the flag once per
turn and rebuilds — so a burst of N edits triggers a single rebuild, not N.

Deliberately does NOT run the generator here: doing so on every edit would
re-scan the 80+ note vault on each keystroke-level write. Debounce > eager.
"""
import sys, json, os

VAULT_FALLBACK = "/Users/alexcohen/InvestmentVault"
WATCHED = ("Theses/", "Sectors/", "Macro & Technology/")


def main():
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        sys.exit(0)

    tin = data.get("tool_input") or {}
    fp = tin.get("file_path") or tin.get("path") or ""
    if not fp:
        sys.exit(0)

    project = os.environ.get("CLAUDE_PROJECT_DIR", VAULT_FALLBACK)
    rel = fp
    for base in (project, VAULT_FALLBACK):
        if base and rel.startswith(base):
            rel = rel[len(base):]
            break
    rel = rel.lstrip("/")

    if rel.endswith(".md") and any(rel.startswith(w) for w in WATCHED):
        try:
            open(os.path.join(project, ".claude", ".graph_dirty"), "w").close()
        except OSError:
            pass

    sys.exit(0)


if __name__ == "__main__":
    main()
