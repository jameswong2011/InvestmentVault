#!/usr/bin/env python3
"""PreToolUse guard — deny Write/Edit to Tier-1 protected vault files.

Enforces CLAUDE.md > Change Safety Rules > Tier 1 (Protected Files) at the
harness level, so protection no longer depends on the model remembering the
rule. Fires on Write | Edit | MultiEdit.

Escape hatch: set CLAUDE_VAULT_ALLOW_PROTECTED=1 for the session to allow
intentional edits (export before launching Claude, or add to settings.json
`env`). Fail-open on any parse error — a guard that mis-parses must never
block legitimate work.
"""
import sys, json, os, re

VAULT_FALLBACK = "/Users/alexcohen/InvestmentVault"

# (regex on vault-relative path, human label). Mirrors CLAUDE.md Tier 1 exactly.
PROTECTED = [
    (r"^CLAUDE\.md$",        "CLAUDE.md (system instructions)"),
    (r"^Templates/",         "Templates/ (vault-wide note structure)"),
    (r"^\.obsidian/",        ".obsidian/ (Obsidian config)"),
    (r"^\.claude/skills/",   ".claude/skills/ (skill definitions)"),
]


def allow():
    sys.exit(0)


def main():
    # Session-level override (launch-time env var; always-on if set in settings.json env).
    if os.environ.get("CLAUDE_VAULT_ALLOW_PROTECTED") == "1":
        allow()

    project = os.environ.get("CLAUDE_PROJECT_DIR", VAULT_FALLBACK)

    # Explicit-intent escape hatch: a sentinel file dropped for a deliberate,
    # user-requested edit to a protected file. Unlike the env var it is toggleable
    # mid-session (`touch .claude/.allow-protected` to unlock, `rm` after). The Stop
    # hook deletes it at turn end, so the guard always re-arms next turn.
    if os.path.exists(os.path.join(project, ".claude", ".allow-protected")):
        allow()

    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        allow()

    tin = data.get("tool_input") or {}
    fp = tin.get("file_path") or tin.get("path") or tin.get("notebook_path") or ""
    if not fp:
        allow()

    rel = fp
    for base in (project, VAULT_FALLBACK):
        if base and rel.startswith(base):
            rel = rel[len(base):]
            break
    rel = rel.lstrip("/")

    for pat, label in PROTECTED:
        if re.search(pat, rel):
            reason = (
                f"BLOCKED by vault Tier-1 guard: '{rel}' -> {label}. "
                "Per CLAUDE.md Change Safety Rules, Tier-1 files change vault-wide "
                "behavior and must not be modified without explicit instruction. "
                "To edit intentionally this session, set CLAUDE_VAULT_ALLOW_PROTECTED=1 "
                "(export it before launching Claude, or add it to .claude/settings.json "
                "`env`), then retry — or edit the file directly outside Claude."
            )
            print(json.dumps({
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }))
            sys.exit(0)

    allow()


if __name__ == "__main__":
    main()
