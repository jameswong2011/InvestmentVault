#!/bin/bash
# Unattended vault-skill runner for launchd (item 4: weekly /catalyst + /lint).
#
#   Usage: run-vault-skill.sh <skill> [model]
#   e.g.:  run-vault-skill.sh catalyst
#          run-vault-skill.sh lint sonnet
#
# Runs a vault skill headlessly via `claude -p` with permission prompts bypassed
# (personal machine, own skills, no human present). The skill's own pre-flight
# lock/snapshot machinery still runs, so a scheduled run coordinates safely with
# any live interactive session. Invoke manually to test before trusting the cron.
set -uo pipefail

SKILL="${1:?usage: run-vault-skill.sh <skill> [model]}"
VAULT="/Users/alexcohen/InvestmentVault"
export HOME="${HOME:-/Users/alexcohen}"
# launchd gives a minimal PATH — set one that finds claude/node/python3/defuddle.
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$HOME/.local/bin"

case "$SKILL" in
  catalyst) MODEL="${2:-opus}"   ;;   # heavy cross-portfolio analysis
  lint)     MODEL="${2:-sonnet}" ;;   # structural/freshness checks
  *)        MODEL="${2:-sonnet}" ;;
esac

LOGDIR="$VAULT/.claude/schedule/logs"
mkdir -p "$LOGDIR"
LOG="$LOGDIR/$SKILL.log"
start_ts="$(date '+%Y-%m-%d %H:%M:%S %Z')"

cd "$VAULT" || { echo "[$start_ts] FATAL: cannot cd to $VAULT" >>"$LOG"; exit 1; }

if ! command -v claude >/dev/null 2>&1; then
  echo "[$start_ts] FATAL: claude CLI not on PATH ($PATH)" >>"$LOG"; exit 127
fi

{
  echo ""
  echo "========================================================================"
  echo "=== [$start_ts] START /$SKILL  (model=$MODEL) ==="
  echo "========================================================================"
} >>"$LOG"

if [ "$SKILL" = "lint" ]; then
  # /lint is a read-only report — capture the clean final output as JSON and publish
  # it as a dated note in Daily Intel/ so the headless run is visible in Obsidian.
  JSON="$LOGDIR/lint.last.json"
  claude -p "/lint" --model "$MODEL" --dangerously-skip-permissions --output-format json >"$JSON" 2>>"$LOG"
  RC=$?
  today="$(date +%F)"
  python3 "$VAULT/.claude/schedule/publish-lint-note.py" \
      "$JSON" "$VAULT/Daily Intel/$today - Vault Health - lint.md" "$today" >>"$LOG" 2>&1
else
  # /catalyst and others write their own durable artifact (e.g. _catalyst.md);
  # stream the run narration to the log.
  claude -p "/$SKILL" --model "$MODEL" --dangerously-skip-permissions >>"$LOG" 2>&1
  RC=$?
fi

echo "=== [$(date '+%Y-%m-%d %H:%M:%S %Z')] END /$SKILL  rc=$RC ===" >>"$LOG"
exit $RC
