#!/bin/bash
# n8n keep-alive watchdog (item: n8n auto-start/keep-alive, added 2026-08-27).
#
# Root cause it guards against: pm2 is registered as a RunAtLoad+KeepAlive LaunchAgent
# (~/Library/LaunchAgents/pm2.alexcohen.plist) that runs `pm2 resurrect` to bring n8n back
# after a reboot. That plist also sets LaunchOnlyOnce=true, so launchd fires it exactly once
# per login session and never retries. On 2026-08-15 15:58 the Mac rebooted and n8n never
# came back — `pm2 resurrect` either didn't run in time or failed once — and because nothing
# ever checked again, n8n silently stayed down for the next 11 days (every scheduled workflow:
# UC1-UC5) until someone noticed and started it by hand on 2026-08-27.
#
# This script is the "checked again" — runs every 15 min via launchd StartInterval, confirms
# pm2 reports n8n online AND the app actually answers on :5678, and self-heals if not.
set -uo pipefail

VAULT="/Users/alexcohen/InvestmentVault"
export HOME="${HOME:-/Users/alexcohen}"
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$HOME/.local/bin"

LOGDIR="$VAULT/.claude/schedule/logs"
mkdir -p "$LOGDIR"
LOG="$LOGDIR/n8n-watchdog.log"
ts() { date '+%Y-%m-%d %H:%M:%S %Z'; }

pm2_status() {
  pm2 jlist 2>/dev/null | python3 -c "
import json, sys
try:
    procs = json.load(sys.stdin)
    n8n = [p for p in procs if p.get('name') == 'n8n']
    print(n8n[0]['pm2_env']['status'] if n8n else 'missing')
except Exception:
    print('error')
"
}

STATUS="$(pm2_status)"
HTTP_CODE="$(curl -s -o /dev/null -m 5 -w '%{http_code}' http://localhost:5678/healthz 2>/dev/null || echo 000)"

if [ "$STATUS" = "online" ] && [ "$HTTP_CODE" = "200" ]; then
  echo "$(ts) OK status=$STATUS healthz=$HTTP_CODE" >>"$LOG"
  exit 0
fi

echo "$(ts) UNHEALTHY status=$STATUS healthz=$HTTP_CODE — attempting recovery" >>"$LOG"

if [ "$STATUS" = "missing" ] || [ "$STATUS" = "error" ]; then
  pm2 resurrect >>"$LOG" 2>&1
else
  pm2 restart n8n >>"$LOG" 2>&1
fi

sleep 8
STATUS2="$(pm2_status)"
HTTP_CODE2="$(curl -s -o /dev/null -m 5 -w '%{http_code}' http://localhost:5678/healthz 2>/dev/null || echo 000)"
echo "$(ts) POST-RECOVERY status=$STATUS2 healthz=$HTTP_CODE2" >>"$LOG"

if [ "$STATUS2" = "online" ] && [ "$HTTP_CODE2" = "200" ]; then
  exit 0
else
  echo "$(ts) ALERT: recovery attempt did not bring n8n back — manual check needed" >>"$LOG"
  exit 1
fi
