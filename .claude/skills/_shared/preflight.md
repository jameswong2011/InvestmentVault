---
type: shared-contract
purpose: Canonical pre-flight checks every skill runs before modifying vault state. Covers vault locking (concurrency), rename-marker awareness, and name normalization.
last_reviewed: 2026-04-21
---

<!--
This file is a load-bearing contract. Every skill that writes to the vault must call the appropriate pre-flight checks defined here BEFORE any destructive operation. `/lint` check #43 enforces coverage.

Consumers: every skill except pure-read skills (`/lint` read path, `/rollback` list mode).
-->

# Pre-flight Safety Contract

> **Why this exists**: Without shared pre-flight logic, every skill would duplicate concurrency checks, marker-awareness checks, and input sanitization. Each duplicate is a drift point. Centralizing the contract here — with every skill calling by reference — eliminates silent divergence across 17 skills.

## Procedures defined in this contract

1. **Vault lock acquisition / release** — prevents concurrent skill invocations from racing on shared files (`_hot.md`, `.last_sync`, thesis Logs, `_graph.md`, `.graph_invalidations`).
2. **Rename-marker pre-flight check** — blocks ticker-scoped skills from running on a thesis mid-rename repair.
3. **Name sanitization** — whitelist/NFC validator for any user-supplied name that becomes a filename (currently only `/rename`, but reusable).
4. **Section existence probe** — verify a `## Heading` exists in a target file before editing.

---

## Procedure 1 — Vault lock

> **Design note**: Claude Code's Bash tool is stateless — shell state (including `trap` handlers) does NOT persist across Bash tool invocations. Each Bash block runs in a fresh subshell. The lock scheme must therefore be stateless at the shell level and durable across multiple tool calls (Bash / Read / Edit / Write) within a single skill run. The LLM running the skill carries lock identity in its conversation context between tool calls.

### 1.1 Lock file format

Locks live at vault root as markdown files with YAML frontmatter:
- **Vault-wide lock**: `.vault-lock` (only one skill can hold this)
- **Ticker lock**: `.vault-lock.TICKER` (one per ticker; concurrent distinct tickers allowed)
- **Read-only lock**: `.vault-lock.readonly` (multiple readers allowed, blocks vault-wide writers)

**Multi-ticker scope** (`/compare A vs B [vs C]`): acquires N **separate per-ticker locks**, not one joint lock. Prevents delimiter-collision bugs with hyphen-containing tickers (`BRK-B`, `BF-A`, `PBR-A`). See §1.3c.

Lock frontmatter:

```yaml
---
token: a7f3b2e8-1729432842                # skill-run identity (unique per skill invocation)
skill: /sync                              # skill name (exactly as invoked)
scope: vault-wide                         # vault-wide | ticker:TICKER | read-only
started_at: 2026-04-19T15:30:42Z          # ISO 8601 UTC
timeout_at: 2026-04-19T15:40:42Z          # started_at + skill timeout budget
session_id: <claude-session-id or "unknown">
---

# Vault lock

Held by /sync (token a7f3b2e8-1729432842) since 2026-04-19T15:30:42Z. Scope: vault-wide.
```

**`token` replaces the prior `pid:` field** (rationale: shell PID at `$$` is only valid within one Bash block; subsequent blocks have different PIDs; PID-based ownership was unreliable). The token is a skill-run-unique identifier generated at acquisition (Step 0.1) and carried by the LLM through all subsequent tool calls as a literal string. The `session_id` remains as auxiliary info but ownership is keyed on `token`.

### 1.2 Scope taxonomy

| Skill | Lock scope | Typical timeout |
|---|---|---|
| `/sync all`, `/graph` (any mode), `/prune` (full or sector), `/lint` (full), `/clean`, `/catalyst`, `/ingest` (any mode — URL, single file, or batch all lock vault-wide per ingest SKILL.md 0.1), `/scenario` (forward or reverse), `/surface` (unscoped or sector-scoped), `/rollback` (cascade) | `vault-wide` | 10m (`/sync all`, `/graph`), 15m (`/prune`), 5m (others) |
| `/sync TICKER`, `/deepen`, `/stress-test`, `/status TICKER`, `/brief`, `/rename`, `/thesis`, `/surface TICKER` | `ticker:TICKER` | 3–10m per skill (see individual SKILL.md) |
| `/compare A vs B [vs C]` | N × `ticker:TICKER` (one lock per ticker in the compare set) | 10m |
| `/rollback` (list mode), `/lint TICKER` | `read-only` | 2m |

### 1.3 Acquisition (Step 0.1 — single Bash block)

Step 0.1 emits one Bash block that:
1. Generates a run-token.
2. Checks for conflicting locks per the taxonomy.
3. On collision → aborts with the collision message (§1.4).
4. On no collision → writes the lockfile(s).
5. Echoes the token on stdout for the LLM to capture.
6. Installs `trap "rm -f '$LOCK_FILE'" INT TERM` only (NOT `EXIT`) — handles Ctrl-C / kill signals; does NOT remove lock on normal block exit.

The LLM MUST capture the echoed token and carry it in working memory through every subsequent tool call. Step 0 instructions in each skill remind the LLM of this explicitly.

#### 1.3a — Vault-wide acquisition

```bash
LOCK_FILE=".vault-lock"
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
TOKEN="$(printf '%08x' $RANDOM$RANDOM)-$(date -u +%s)"
TIMEOUT_AT=$(date -u -v+10M +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d '+10 minutes' +%Y-%m-%dT%H:%M:%SZ)

# Enable null-glob so unmatched .vault-lock.* expands to nothing.
# Portable across zsh (macOS default) and bash — one of these two will succeed.
# Without this, zsh throws "no matches found: .vault-lock.*" on a clean vault
# and the acquisition block exits non-zero on first attempt every time.
setopt NULL_GLOB 2>/dev/null || shopt -s nullglob 2>/dev/null || true

# Collision check: vault-wide OR any existing ticker lock OR read-only lock
for existing in .vault-lock .vault-lock.* ; do
  [ -f "$existing" ] || continue
  # Read timeout_at; if expired → stale; if future → live collision
  EX_TIMEOUT=$(grep '^timeout_at:' "$existing" | sed 's/timeout_at: //')
  EX_SKILL=$(grep '^skill:' "$existing" | sed 's/skill: //')
  EX_TOKEN=$(grep '^token:' "$existing" | sed 's/token: //')
  if [ "$EX_TIMEOUT" \> "$NOW" ]; then
    echo "LOCK_HELD|$existing|$EX_SKILL|$EX_TOKEN|$EX_TIMEOUT"
    exit 1
  else
    echo "STALE_LOCK|$existing|$EX_SKILL|$EX_TOKEN|timeout_exceeded_at|$EX_TIMEOUT"
    # Do NOT auto-steal (see §1.6). Surface for user confirmation.
    exit 2
  fi
done

# No conflicts — write the lock
cat > "$LOCK_FILE" <<EOF
---
token: $TOKEN
skill: /sync all
scope: vault-wide
started_at: $NOW
timeout_at: $TIMEOUT_AT
session_id: ${CLAUDE_SESSION_ID:-unknown}
---

# Vault lock

Held by /sync all (token $TOKEN) since $NOW.
EOF

trap "rm -f '$LOCK_FILE'" INT TERM
echo "ACQUIRED|$LOCK_FILE|$TOKEN"
```

#### 1.3b — Ticker-scoped acquisition

```bash
TICKER="NVDA"
LOCK_FILE=".vault-lock.$TICKER"
VAULT_WIDE_LOCK=".vault-lock"
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
TOKEN="$(printf '%08x' $RANDOM$RANDOM)-$(date -u +%s)"
TIMEOUT_AT=$(date -u -v+3M +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d '+3 minutes' +%Y-%m-%dT%H:%M:%SZ)

# Collision checks
for existing in "$VAULT_WIDE_LOCK" "$LOCK_FILE" ; do
  [ -f "$existing" ] || continue
  EX_TIMEOUT=$(grep '^timeout_at:' "$existing" | sed 's/timeout_at: //')
  EX_SKILL=$(grep '^skill:' "$existing" | sed 's/skill: //')
  EX_TOKEN=$(grep '^token:' "$existing" | sed 's/token: //')
  if [ "$EX_TIMEOUT" \> "$NOW" ]; then
    echo "LOCK_HELD|$existing|$EX_SKILL|$EX_TOKEN|$EX_TIMEOUT"
    exit 1
  else
    echo "STALE_LOCK|$existing|$EX_SKILL|$EX_TOKEN|timeout_exceeded_at|$EX_TIMEOUT"
    exit 2
  fi
done

cat > "$LOCK_FILE" <<EOF
---
token: $TOKEN
skill: /stress-test
scope: ticker:$TICKER
started_at: $NOW
timeout_at: $TIMEOUT_AT
session_id: ${CLAUDE_SESSION_ID:-unknown}
---

# Vault lock

Held by /stress-test $TICKER (token $TOKEN) since $NOW.
EOF

trap "rm -f '$LOCK_FILE'" INT TERM
echo "ACQUIRED|$LOCK_FILE|$TOKEN"
```

#### 1.3c — Multi-ticker acquisition (per-ticker individual locks)

`/compare A vs B vs C` acquires THREE separate ticker locks, not one joint lock. Handles hyphen-containing tickers (`BRK-B`) correctly because each lock file uses only ONE ticker in its name.

Acquisition is ordered + rollback-on-failure:

```bash
TICKERS="NVDA AAPL BRK-B"
VAULT_WIDE_LOCK=".vault-lock"
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
TOKEN="$(printf '%08x' $RANDOM$RANDOM)-$(date -u +%s)"
TIMEOUT_AT=$(date -u -v+10M +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d '+10 minutes' +%Y-%m-%dT%H:%M:%SZ)

# Pre-flight: vault-wide lock?
if [ -f "$VAULT_WIDE_LOCK" ]; then
  EX_TIMEOUT=$(grep '^timeout_at:' "$VAULT_WIDE_LOCK" | sed 's/timeout_at: //')
  if [ "$EX_TIMEOUT" \> "$NOW" ]; then
    echo "LOCK_HELD|$VAULT_WIDE_LOCK"
    exit 1
  fi
  echo "STALE_LOCK|$VAULT_WIDE_LOCK"
  exit 2
fi

# Attempt per-ticker acquisition with rollback on failure
ACQUIRED=""
FAILED=""
for T in $TICKERS; do
  LF=".vault-lock.$T"
  if [ -f "$LF" ]; then
    EX_TIMEOUT=$(grep '^timeout_at:' "$LF" | sed 's/timeout_at: //')
    if [ "$EX_TIMEOUT" \> "$NOW" ]; then
      FAILED="$LF"
      break
    fi
    echo "STALE_LOCK|$LF"
    exit 2
  fi
  cat > "$LF" <<EOF
---
token: $TOKEN
skill: /compare
scope: ticker:$T
started_at: $NOW
timeout_at: $TIMEOUT_AT
session_id: ${CLAUDE_SESSION_ID:-unknown}
multi_scope: $TICKERS
---

# Vault lock

Held by /compare (token $TOKEN) since $NOW. Part of multi-ticker scope: $TICKERS.
EOF
  ACQUIRED="$ACQUIRED $LF"
done

# Rollback on partial acquisition
if [ -n "$FAILED" ]; then
  for LF in $ACQUIRED; do rm -f "$LF"; done
  echo "LOCK_HELD|$FAILED"
  exit 1
fi

trap "rm -f $ACQUIRED" INT TERM
echo "ACQUIRED_MULTI|$TOKEN|$ACQUIRED"
```

The `multi_scope:` frontmatter field records all peer tickers in the same run — used by `/rollback` and `/lint` for audit. Rollback on partial acquisition guarantees the skill never ends up holding a proper subset of its intended ticker set.

### 1.4 Collision message (hard block)

When Step 0.1 Bash echoes `LOCK_HELD|...`:

```
❌ Another skill is running — vault lock held.
   Skill:       [skill from existing lock]
   Token:       [token from existing lock]
   Scope:       [scope from existing lock]
   Started:     [started_at] ([X] minutes ago)
   Times out:   [timeout_at] (in [Y] minutes)

Wait for the other skill to finish. If you are certain the holder has crashed
(terminal closed, session killed) and the timeout hasn't yet expired, you can
manually force-unlock:
   rm [lockfile_path]

If the holder's timeout has expired, /lint #43 surfaces stale locks; run /lint
to confirm staleness before removing.
```

When Step 0.1 Bash echoes `STALE_LOCK|...`:

```
⚠️ Stale lock detected — timeout exceeded.
   Skill:       [skill from existing lock]
   Token:       [token]
   Scope:       [scope]
   Started:     [started_at] ([X] minutes ago)
   Timeout at:  [timeout_at] ([Y] minutes ago)

The lock has exceeded its timeout budget. The prior run may have crashed, OR
may still be legitimately running (long web-research runs, large PDF ingests,
slow LLM responses).

This skill does NOT auto-steal. Choose:
  (a) Wait — the prior skill may still complete. Re-run this skill later.
  (b) Force-unlock if you can confirm the prior run is truly abandoned:
        rm [lockfile_path]
      Then re-run this skill.
  (c) Inspect the lock's manifest (if any — sync/status/prune manifests in
      _Archive/Snapshots/ expose in-progress state): /lint surfaces them.

Timeout-based auto-steal was removed intentionally (prior behavior risked
racing a legitimately long-running skill). Staleness recovery is a user
confirmation, not an automatic action.
```

### 1.5 Ownership verification (mandatory at start of every subsequent Bash block)

After Step 0.1 succeeds with `ACQUIRED|...`, the LLM has captured `$TOKEN`. Every subsequent Bash block in the skill MUST begin with:

```bash
EXPECTED_TOKEN="<paste-token-captured-from-step-0.1>"
LOCK_FILE="<paste-lockfile-path-from-step-0.1>"

if [ ! -f "$LOCK_FILE" ]; then
  echo "❌ LOCK_LOST: $LOCK_FILE no longer exists. Another skill may have force-unlocked."
  exit 3
fi

ACTUAL_TOKEN=$(grep '^token:' "$LOCK_FILE" | sed 's/token: //')
if [ "$ACTUAL_TOKEN" != "$EXPECTED_TOKEN" ]; then
  echo "❌ LOCK_STOLEN: $LOCK_FILE has token $ACTUAL_TOKEN (expected $EXPECTED_TOKEN)."
  echo "   Another skill has overwritten the lock since Step 0.1."
  exit 4
fi

# Lock ownership confirmed. Proceed with skill work.
```

**Multi-ticker case**: verification runs once per ticker lock held.

**If verification fails** (`LOCK_LOST` or `LOCK_STOLEN`): abort the skill immediately. Any in-progress transaction manifest remains in `status: in-progress` for `/rollback` recovery. Write a final report noting the lock-loss and what work landed before the loss was detected.

Between-block tool calls (Read / Edit / Write without Bash) do NOT need verification — they cannot release or overwrite the lockfile. The lock persists until either (a) an explicit release in the skill's final Bash block, (b) a user `rm`, or (c) the INT/TERM trap fires on signal.

### 1.6 Stale detection (NO auto-steal)

A lock is **stale** if `timeout_at` < now. Staleness does NOT trigger automatic removal. Recovery is always a user decision:

1. On collision with a stale lock, Step 0.1 Bash exits with `STALE_LOCK|...` status.
2. The skill surfaces the `⚠️ Stale lock detected` message (§1.4) with recovery options.
3. User either waits, manually `rm`s, or inspects the prior run's manifest before acting.
4. `/lint #43` globs `.vault-lock*` and surfaces all stale locks (timeout exceeded) as Important — this is the canonical discovery path for abandoned locks.

**Why no auto-steal**: the original design stole locks when `timeout_at < now` regardless of whether the prior skill was still running. Long LLM stalls, slow web research, or large batch operations could legitimately exceed the timeout while the skill was still making progress — auto-steal raced the legitimate worker. User-confirmed recovery eliminates this race at the cost of slightly more manual intervention on true crashes.

### 1.7 Release (explicit final Bash block)

The skill's FINAL Bash block (typically in the reporting phase) runs:

```bash
# Ticker-scoped or vault-wide release
rm -f "$LOCK_FILE"
echo "RELEASED|$LOCK_FILE"
```

For multi-ticker (compare):
```bash
for LF in $ACQUIRED; do rm -f "$LF"; done
echo "RELEASED_MULTI|$ACQUIRED"
```

The release Bash block is unconditional — it runs whether the skill succeeded or hit a non-fatal error. If the skill aborts before reaching the release step (crash, hard abort on section missing, etc.), the lock persists and appears stale on the next collision / `/lint` run.

Trap on INT/TERM handles Ctrl-C and kill signals within the acquisition Bash block only — subsequent blocks don't inherit the trap (by design; the LLM's explicit final-release block is the primary cleanup path).

### 1.8 `/lint` enforcement

`/lint #43` globs `.vault-lock*` files and surfaces:
- **Stale** (timeout_at < now): Important — `⚠️ Stale vault lock: [lockfile]. Skill [X] (token [T]) started [started_at], timeout [timeout_at]. Recovery: rm the lockfile if you can confirm the holder is truly abandoned.`
- **Active** (timeout_at > now): Pass (lock is legitimately held).

No PID check anymore — the token + timeout model is the authoritative signal.

---

## Procedure 2 — Rename-marker pre-flight

### 2.1 When this check runs

At Step 0 of every **ticker-scoped** skill. Applies to: `/status`, `/sync TICKER`, `/stress-test`, `/compare` (per-ticker iteration), `/deepen`, `/brief`, `/surface TICKER`, `/thesis` (defined at Step 0.2, executed as part of the Step 1.0 parallel probe batch — hard-block priority beats active-thesis and archive-collision results).

**Exceptions** (skill proceeds regardless of marker):
- `/lint` — read-only; marker already surfaced via `/lint #37`
- `/rollback` — may be the recovery path (user restores pre-rename snapshot, then manually `rm` marker)
- `/graph` (any mode) — read-only for theses; refreshes graph regardless of pending wikilink repairs
- `/rename` — this skill OWNS the marker; its own logic handles the presence

### 2.2 Procedure

For a ticker-scoped skill operating on TICKER:

```
marker_path = ".rename_incomplete.TICKER"
if exists(marker_path):
    read marker's YAML frontmatter: new_name, old_name, batch, date
    read marker body: list of "Failed files"
    abort with collision message (see 2.3)
```

For `/compare` (multi-ticker), the check runs for each ticker in `$ARGUMENTS`; the skill aborts on the FIRST marker found.

### 2.3 Collision message

```
❌ Rename repair incomplete for TICKER.
   Marker:      .rename_incomplete.TICKER
   In-flight:   TICKER - [old_name] → TICKER - [new_name]
   Batch:       [batch]
   Dated:       [date]
   Failed files ([N]):
     - [path 1]
     - [path 2]
     ...

This skill modifies content that references TICKER's thesis wikilink, but the
prior rename left [N] inbound wikilink(s) unrepaired. Proceeding would propagate
edits keyed to the new name into files that still reference the old name —
silently splitting propagation across two naming conventions.

Complete the rename first:
   /rename TICKER "[new_name]"    # retries only the failed Edit(s)

Or accept broken wikilinks and proceed:
   rm .rename_incomplete.TICKER    # then re-run this skill
                                   # /lint #3 will flag broken wikilinks
```

Wait for user to resolve externally; do NOT proceed silently.

### 2.4 Why hard-block (not warn)

A soft warning would leave the user to judge — but the blast radius of "proceed with a half-renamed thesis" is wide: every Log append, every sector note edit, every `_hot.md` mention written keyed to the new name bypasses the files still carrying the old name. Mass silent wikilink drift accumulates within a single session. Hard block forces explicit resolution.

---

## Procedure 3 — Name sanitization

### 3.1 When this applies

Any skill accepting a user-supplied string that becomes part of a filename (currently `/rename` new_name; future: a potential `/reticker` skill). Does NOT apply to body content or frontmatter values.

### 3.2 Rules

Apply in order:

1. **NFC normalize**: unicode-normalize to NFC (handles composed/decomposed diacritic mismatches that break filename matching on case-preserving-but-insensitive filesystems like macOS default APFS).
2. **Trim**: strip leading/trailing whitespace. If result is empty → reject.
3. **Length cap**: 100 bytes post-normalization → reject if exceeded.
4. **Character whitelist**: allowed set `[a-zA-Z0-9 \-_.,'&()]`. Any other character (including `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`, control chars, most unicode punctuation) → reject.
5. **Leading dot**: reject (hidden-file convention).
6. **Reserved filesystem names** (Windows/cross-platform portability): reject if the first whitespace-separated token case-insensitively equals `CON`, `PRN`, `AUX`, `NUL`, `COM1`–`COM9`, `LPT1`–`LPT9`.

### 3.3 Rejection message

```
❌ Invalid name: "[input]"
   Reason:   [specific rule that failed — e.g., "Disallowed character: /"]
   Allowed:  alphanumerics, spaces, and -_.,'&()
   Max:      100 characters, no leading dot, not a reserved filesystem name

Suggestion: [propose a cleaned variant where possible, e.g., replace / with ' ' or remove]
```

### 3.4 Implementation hint

```bash
validate_name() {
  local name="$1"
  # NFC normalize — printf is locale-aware on most systems; a no-op for ASCII input
  # For unicode normalization in full, the skill's LLM layer does the check pre-call
  
  # Trim
  name="$(echo -n "$name" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
  
  # Empty check
  [ -z "$name" ] && { echo "REJECT|empty"; return 1; }
  
  # Length cap
  [ ${#name} -gt 100 ] && { echo "REJECT|too-long: ${#name} > 100"; return 1; }
  
  # Character whitelist
  if echo -n "$name" | grep -qE "[^a-zA-Z0-9 .,'&()_-]"; then
    bad=$(echo -n "$name" | grep -oE "[^a-zA-Z0-9 .,'&()_-]" | sort -u | tr -d '\n')
    echo "REJECT|bad-chars: $bad"
    return 1
  fi
  
  # Leading dot
  [[ "$name" == .* ]] && { echo "REJECT|leading-dot"; return 1; }
  
  # Reserved names
  first=$(echo "$name" | awk '{print toupper($1)}')
  case "$first" in
    CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])
      echo "REJECT|reserved-name: $first"
      return 1
      ;;
  esac
  
  echo "OK|$name"
  return 0
}
```

The LLM running a skill can also perform these checks in its reasoning layer — the Bash snippet above is an optional concrete implementation.

---

## Procedure 4 — Section existence probe

### 4.1 When this applies

Any skill that edits a specific `## Heading` section of a target file (currently `/deepen`, `/compare` sector-section edits, `/stress-test` Log append, `/sync` cross-section edits).

### 4.2 Procedure

```
function check_section_exists(file_path, section_heading):
  # section_heading is the exact heading text including "## " prefix
  Read the file's content.
  Scan for a line matching: ^## [exact section text]$
  Return true iff found.
```

### 4.3 On missing section

The calling skill decides its own handling, but the contract is:

- **Hard abort** (default — used by `/deepen`): report `❌ Section "## [heading]" not found in [path]. Aborted.` plus list of sections that DO exist. Do NOT silently create the section.
- **Graceful skip** (used by `/sync` when an expected section is missing — e.g., macro notes without `## Log`): log `ℹ️ [path] missing "## [heading]" — skipping idempotency check for this file.`

Never silently insert a `## Heading` — structural changes to thesis/sector templates must be explicit user action.

---

## Contract version & drift

This file's `last_reviewed:` frontmatter anchors the contract version. When any procedure here changes, update every skill's pre-flight call to match and bump `last_reviewed:`.

`/lint #43` (vault lock orphan detection), `/lint #37` (rename marker surfacing), `/lint #1.4` (archive consistency) all depend on this contract's stability.
