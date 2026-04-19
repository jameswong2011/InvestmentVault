---
type: shared-contract
purpose: Canonical pre-flight checks every skill runs before modifying vault state. Covers vault locking (concurrency), rename-marker awareness, and name normalization.
last_reviewed: 2026-04-19
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

### 1.1 Lock file format

Locks live at vault root:
- **Vault-wide lock**: `.vault-lock` (only one skill can hold this)
- **Ticker lock**: `.vault-lock.TICKER` (one per ticker, concurrent tickers allowed)
- **Read-only lock**: `.vault-lock.readonly` (multiple readers allowed, blocks vault-wide writers)

Each lock is a markdown file with YAML frontmatter:

```yaml
---
pid: 48234                               # owning process PID (from $PPID or echo $$)
skill: /sync                             # skill name (exactly as invoked)
scope: vault-wide                        # vault-wide | ticker:TICKER | ticker:A+B+... | read-only
started_at: 2026-04-19T15:30:42Z         # ISO 8601 UTC
timeout_at: 2026-04-19T15:40:42Z         # started_at + skill timeout budget
session_id: <uuid>                       # Claude Code session ID if available, else "unknown"
---

# Vault lock

Held by /sync (PID 48234) since 2026-04-19T15:30:42Z. Scope: vault-wide.
```

### 1.2 Scope taxonomy

| Skill | Lock scope | Typical timeout |
|---|---|---|
| `/sync all`, `/graph` (any mode), `/prune` (full or sector), `/lint` (full), `/clean`, `/catalyst`, `/ingest` (batch), `/scenario` (forward or reverse), `/surface` (any mode), `/rollback` (cascade) | `vault-wide` | 10m (`/sync all`, `/graph`), 15m (`/prune`), 5m (others) |
| `/sync TICKER`, `/deepen`, `/stress-test`, `/status TICKER`, `/brief`, `/rename`, `/thesis`, `/ingest [URL or file]` (single) | `ticker:TICKER` | 3m |
| `/compare A vs B [vs C]` | `ticker:A+B+C` (sorted alphabetically, `+`-joined) | 5m |
| `/rollback` (list mode), `/lint TICKER` | `read-only` | 2m |

### 1.3 Acquisition

Pseudo-logic (implementations use `Bash` tool with `mkdir -p` / `[ -e ]` / `cat` / `echo`):

```
function acquire_lock(skill, scope, timeout_minutes):
  lockfile = ".vault-lock"  if scope == "vault-wide"
             ".vault-lock.TICKER"  if scope == "ticker:TICKER"
             ".vault-lock.readonly"  if scope == "read-only"
             ".vault-lock.A+B+C"  if scope == "ticker:A+B+C"
  
  # Collision checks — run in this order:
  #   1) vault-wide lock held by another skill
  #   2) ticker lock for any ticker in our scope (for ticker-scoped skills)
  #   3) our-scope lock already held
  #   4) for vault-wide acquisition: any existing ticker-lock

  For each candidate conflicting lock:
    If the file exists:
      Read its frontmatter.
      If pid not running (kill -0 PID fails) → steal the lock (print warning)
      If timeout_at < now → expired, steal the lock (print warning)
      Else → HARD BLOCK with collision message (see 1.4)
  
  # Write our lock atomically
  Write lockfile with YAML frontmatter populated
  Register a shell trap (or equivalent finalizer) to remove lockfile on exit
  Return acquired lock path
```

**Implementation hint for skills**: use a `Bash` tool block at Step 0:

```bash
# Example for a ticker-scoped skill with ticker $TICKER and timeout 180s
LOCK_FILE=".vault-lock.$TICKER"
VAULT_WIDE_LOCK=".vault-lock"

# Check vault-wide lock
if [ -e "$VAULT_WIDE_LOCK" ]; then
  PID=$(grep '^pid:' "$VAULT_WIDE_LOCK" | sed 's/pid: //')
  TIMEOUT=$(grep '^timeout_at:' "$VAULT_WIDE_LOCK" | sed 's/timeout_at: //')
  SKILL=$(grep '^skill:' "$VAULT_WIDE_LOCK" | sed 's/skill: //')
  NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  if kill -0 "$PID" 2>/dev/null && [ "$TIMEOUT" \> "$NOW" ]; then
    echo "LOCK_HELD|vault-wide|$SKILL|$PID|$TIMEOUT"
    exit 1
  else
    echo "STALE_LOCK|vault-wide|$SKILL|$PID"
    rm -f "$VAULT_WIDE_LOCK"
  fi
fi

# Check our scope lock (same pattern)
if [ -e "$LOCK_FILE" ]; then
  # ... same stale/held logic ...
fi

# Write our lock
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
TIMEOUT_AT=$(date -u -v+3M +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d '+3 minutes' +%Y-%m-%dT%H:%M:%SZ)
cat > "$LOCK_FILE" <<EOF
---
pid: $$
skill: /stress-test
scope: ticker:$TICKER
started_at: $NOW
timeout_at: $TIMEOUT_AT
session_id: ${CLAUDE_SESSION_ID:-unknown}
---

# Vault lock
EOF
```

### 1.4 Collision message (hard block)

```
❌ Another skill is running — vault lock held.
   Skill:       [skill]
   PID:         [pid]
   Scope:       [scope]
   Started:     [started_at] ([X] minutes ago)
   Times out:   [timeout_at] (in [Y] minutes)

Wait for the other skill to finish, or force-unlock if you are certain it has crashed:
   rm [lockfile_path]

(If the other PID is not actually running, this skill would have stolen the lock
 automatically — so if you see this message, the holder appears live.)
```

### 1.5 Release

On skill exit (success, failure, or interrupt), remove the lockfile. Implementations register a `trap`:

```bash
trap "rm -f '$LOCK_FILE'" EXIT INT TERM
```

If a skill emits multiple Bash blocks, the trap must be set in the same block that holds the lock (it's shell-scoped). For skills that don't naturally produce a long-running Bash session, release the lock in the final reporting step via a final Bash call.

### 1.6 Stale lock detection

A lock is stale if:
- `pid` is not a running process (`kill -0 $pid` fails) — the holder died without cleanup, OR
- `timeout_at` < current time — the skill exceeded its timeout budget (genuinely hung OR exited without trap firing)

Stale locks are stolen automatically with a warning: `ℹ️ Stale lock detected: [skill] (PID [pid]) — holder [not running | timed out]. Reclaiming.`

### 1.7 `/lint` enforcement

`/lint #43` (new — see `/lint` SKILL.md) globs `.vault-lock*` files, checks each is held by a live process, and surfaces orphans.

---

## Procedure 2 — Rename-marker pre-flight

### 2.1 When this check runs

At Step 0 of every **ticker-scoped** skill. Applies to: `/status`, `/sync TICKER`, `/stress-test`, `/compare` (per-ticker iteration), `/deepen`, `/brief`, `/surface TICKER`, `/thesis` (at Step 1.1.5 before archive-collision check).

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
