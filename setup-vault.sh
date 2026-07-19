#!/bin/bash
# Post-clone bootstrap for the Investment Research vault.
# Companion to "Build documents/Setup Guide.md" §7.1 — run once after git clone.
#
# Idempotent and non-destructive: creates only what is missing, never overwrites,
# and NEVER touches skill runtime markers (.last_sync etc. — those are owned by
# the skills; creating .last_sync by hand silently marks pending files as synced).
#
# Usage: cd /path/to/InvestmentVault && bash setup-vault.sh

set -u
cd "$(dirname "$0")"

echo "Investment Vault — post-clone bootstrap"
echo "======================================="

# ---- 1. Sanity: are we in the right place? -------------------------------
fail=0
for probe in CLAUDE.md Theses .claude/skills; do
  if [ ! -e "$probe" ]; then
    echo "✗ Missing $probe — run this from the cloned vault root."
    fail=1
  fi
done
[ "$fail" -eq 1 ] && exit 1
echo "✓ Vault root confirmed"

# ---- 2. Tooling checks (warn, don't block) -------------------------------
if command -v claude >/dev/null 2>&1; then
  echo "✓ Claude Code found: $(command -v claude) ($(claude --version 2>/dev/null | head -1))"
else
  echo "⚠ Claude Code not found — install: npm install -g @anthropic-ai/claude-code (Setup Guide §2.2)"
fi
if command -v python3 >/dev/null 2>&1; then
  echo "✓ python3 found (skill helper scripts need it)"
else
  echo "⚠ python3 not found — several skills (/lint, /graph, /numbers) depend on it"
fi
if command -v git >/dev/null 2>&1; then
  echo "✓ git found"
else
  echo "⚠ git not found — install via: brew install git"
fi

# ---- 3. Untracked working directories ------------------------------------
# These hold machine-generated or ignored content, so a fresh clone lacks them.
for d in "Daily Intel" "_Inbox/processed" ".data"; do
  if [ -d "$d" ]; then
    echo "✓ $d/ exists"
  else
    mkdir -p "$d" && echo "✓ Created $d/"
  fi
done

# ---- 4. FMP key placeholder (gitignored) ----------------------------------
CONFIG=".data/config.json"
if [ -f "$CONFIG" ]; then
  echo "✓ $CONFIG exists — left untouched"
else
  printf '{"fmp_api_key": "YOUR_FMP_KEY_HERE"}\n' > "$CONFIG"
  echo "✓ Created $CONFIG (placeholder)"
  echo "  → Edit it now and paste your real key: open -e $CONFIG"
  echo "    Without it, /numbers, /transcript, Live Portfolio refresh, and n8n Workflow 1 abort gracefully."
fi

# ---- 5. Next steps --------------------------------------------------------
cat <<'NEXT'

Bootstrap complete. Remaining setup (Setup Guide, "Build documents/Setup Guide.md"):
  1. Obsidian: Open folder as vault → turn off restricted mode → enable the 5
     community plugins (Claudian, Templater, Dataview, Git, BRAT).        [§5]
  2. Claudian settings: set the Claude CLI path if not auto-detected.     [§6]
  3. Put your real FMP key in .data/config.json (if not done above).      [§7.1]
  4. First-run metadata bootstrap — in Claudian or `claude`:
         /sync      (slow first run is expected — it baselines the vault)
         /graph                                                            [§7.2]
  5. Optional automation layer (n8n, Telegram, X harvesting):             [§8]
NEXT
