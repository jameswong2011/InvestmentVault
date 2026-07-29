#!/usr/bin/env python3
"""Stop hook — rebuild _graph.md once per turn if a note edit dirtied it.

Debounced counterpart to mark-graph-dirty.py. If .claude/.graph_dirty exists,
run the deterministic generator in `last` mode (rebuild-only-if-changed), then
clear the flag. Automates step 4 of the vault's core loop (`/graph last` after
edits) so the graph never silently drifts from the theses.

Never blocks the stop: emits only `systemMessage` (no decision:block /
continue:false), so it cannot create a stop-hook loop.

Note: runs the generator WITHOUT the /graph skill's vault-wide lock. Safe for a
single-user vault — the generator is deterministic (same vault state -> same
output), so a rare race with a manual /graph resolves to identical bytes.
"""
import sys, json, os, subprocess

VAULT_FALLBACK = "/Users/alexcohen/InvestmentVault"


def main():
    project = os.environ.get("CLAUDE_PROJECT_DIR", VAULT_FALLBACK)

    # Re-arm the Tier-1 guard every turn: never let the explicit-edit sentinel
    # (.claude/.allow-protected) outlive the turn that created it.
    try:
        os.remove(os.path.join(project, ".claude", ".allow-protected"))
    except OSError:
        pass

    flag = os.path.join(project, ".claude", ".graph_dirty")
    if not os.path.exists(flag):
        sys.exit(0)

    gen = os.path.join(project, ".claude", "skills", "graph", "generate_graph.py")
    msg = "🔗 _graph.md refreshed (thesis/sector/macro edits detected this turn)."
    try:
        r = subprocess.run(
            ["python3", gen, "last"],
            cwd=project, capture_output=True, text=True, timeout=180,
        )
        if r.returncode != 0:
            tail = ((r.stderr or r.stdout or "").strip().splitlines() or [""])[-1]
            msg = (f"⚠️ _graph.md auto-refresh exited {r.returncode}: "
                   f"{tail[:200]} — run /graph manually.")
    except subprocess.TimeoutExpired:
        msg = "⚠️ _graph.md auto-refresh timed out (180s) — run /graph manually."
    except Exception as e:
        msg = f"⚠️ _graph.md auto-refresh failed: {str(e)[:200]} — run /graph manually."
    finally:
        try:
            os.remove(flag)
        except OSError:
            pass

    print(json.dumps({"systemMessage": msg, "suppressOutput": True}))
    sys.exit(0)


if __name__ == "__main__":
    main()
