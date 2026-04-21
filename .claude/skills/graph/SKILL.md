---
name: graph
description: Rebuild the vault dependency graph (_graph.md). Three modes — /graph (full rebuild), /graph last (true incremental: re-extract only changed thesis adjacencies, always rebuild reverse indexes), /graph [N] (catch-up incremental from N days ago). Use /graph last after every /sync, /graph [N] for catch-up, /graph for full disaster-recovery rebuild.
model: sonnet
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(find * wc * date * grep * rm * cat * sort *)
---

Rebuild `_graph.md` from vault state. Structural metadata only — no content files modified, no snapshots, no `_hot.md` changes.

**`.last_sync` is owned exclusively by `/sync`.** `/graph` never touches it.

Design rationale in `.claude/skills/graph/RATIONALE.md` (§N.M anchors).

## Step 0: Pre-flight

### 0.1: Acquire vault lock

`vault-wide` scope per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout: 5 min (incremental) or 10 min (full rebuild). Capture token, verify (Procedure 1.5) at every subsequent block, release in final Bash block.

`/graph` is vault-wide because it reads every thesis file — concurrent writer could produce mid-read inconsistent extraction.

### 0.2: No rename-marker check

`/graph` is read-only for theses. Graph faithfully reflects current filenames + wikilinks. `/lint #37` separately surfaces pending rename markers.

## Mode Detection

Parse `$ARGUMENTS`:
- **`/graph last`** — True incremental. Skip if no changes since watermark. Re-extract adjacency for changed theses only; always rebuild reverse indexes.
- **`/graph [N]`** — Catch-up incremental. Same as `last` but watermark = today − N days.
- **`/graph`** (no arguments) — Full rebuild. Re-extract adjacency for ALL theses.

Resolution: `last` literal → incremental. Integer N → catch-up. Empty/unrecognized → full.

**Drift-safety design** (§1): forward adjacency incremental; reverse indexes, clusters, orphan list always rebuild fully from in-memory state.

## Watermark Check (incremental modes only)

For `/graph last` and `/graph [N]`, check before any other work. If no changes → skip Incremental Path AND Steps 1-8 entirely.

### Pre-watermark: `.sync_all_fresh` marker

```bash
ls .sync_all_fresh 2>/dev/null
```

If present:
- Log: `⚠️ .sync_all_fresh marker detected — prior /sync all requires full rebuild. Falling back to Steps 1-8 (full path) regardless of mode.`
- Proceed to Step 1 (full rebuild). Step 7's cleanup handles marker deletion after successful full rebuild.

If absent, proceed to Watermark Resolution.

### Watermark Resolution (T6.10 — ISO precision + legacy fallback)

- **`/graph last`**: read `_graph.md`. File missing → warn `⚠️ _graph.md missing — falling back to full rebuild`, proceed to Step 1. Otherwise:
  - **Preferred**: `last_graph_write:` frontmatter — ISO 8601 (`YYYY-MM-DDThh:mm:ssZ`). Use directly as watermark.
  - **Legacy fallback**: `last_graph_write:` absent → use `date:` (YYYY-MM-DD) with implicit 00:00:00 UTC. Log: `ℹ️ _graph.md lacks last_graph_write: frontmatter — using conservative watermark (date: YYYY-MM-DD, 00:00:00 UTC). Next /graph last will upgrade.` (§2.2 — may reprocess same-day edits, safely idempotent).
- **`/graph [N]`**: watermark = `today - N days` as `YYYY-MM-DDT00:00:00Z`. File missing → warn + full rebuild.

### Change Detection (reference-file pattern — §3.1)

Fuse change detection with `.graph_invalidations` pre-read in ONE Bash block:

```bash
# WATERMARK_ISO from resolved watermark.
# /graph last: last_graph_write frontmatter (ISO with Z suffix).
# /graph [N]: "$(date -u -v-${N}d +%Y-%m-%dT00:00:00Z)" on macOS,
#             "$(date -u -d "$N days ago" +%Y-%m-%dT00:00:00Z)" on GNU.

WATERMARK_ISO="2026-04-19T14:19:33Z"   # example
touch -d "$WATERMARK_ISO" /tmp/graph-watermark
echo "=== CHANGED FILES SINCE WATERMARK ==="
find Theses/ Research/ Sectors/ Macro/ -name '*.md' -newer /tmp/graph-watermark | sort
echo "=== .graph_invalidations ==="
cat .graph_invalidations 2>/dev/null || echo "(file absent)"
rm -f /tmp/graph-watermark
```

**Critical**: use `touch -d <ISO>` + `find -newer`, NOT `find -newermt`; NOT `touch -t <stamp>` (§3.1, §3.2 — cross-platform portability).

**Invalidation pre-check**: theses in `.graph_invalidations` need re-extraction regardless of mtime (neighbors of closed theses with stale `cross-thesis:` references — §1.3). See Step I.2.5.

- **No files changed AND no invalidations**: report `Graph is up to date — no changes since [watermark date]; no pending invalidations.` Stop. Do NOT write `_graph.md`.
- **No files changed but invalidations present**: proceed to Incremental Path. Only work is re-extracting invalidated theses + rebuilding reverse indexes + deleting `.graph_invalidations` at I.9. Report `No watermark changes, but [N] invalidations pending — processing.`
- **One or more files changed**: proceed to Incremental Path. Do NOT proceed to Steps 1-8 (those are full rebuild).

## Incremental Path (`/graph last` and `/graph [N]` when changes detected)

Forward adjacency updates per changed thesis; reverse indexes/clusters/orphans always rebuild fully from in-memory state.

**Tool-call budget** (§4.1 + §10.4): Incremental Path Path A (surgical Edits) typical 1-3 changed theses: 1 Read + 2 Bash (extraction + validation/release) + 1 Bash (watermark/lock) + ~5-10 Edits = ~10-14 tool calls, ~2 KB total model output. Path B (full Write) fallback: ~5-6 calls, ~15 KB output. Edits stream 5-7× faster end-to-end.

### Step I.1: Parse Existing Graph

Read `_graph.md`, parse:
- Thesis Adjacency Index → map `TICKER - Name → {sectors, macros, cross-thesis, research, status, log_tail}`
- Existing orphan list (diff reporting)
- Existing cluster table (diff reporting)

Baseline for incremental updates. Parse failure → warn `⚠️ _graph.md unparseable — falling back to full rebuild`, proceed to Step 1.

**Pre-T7.3 compatibility**: if any entry lacks `status:` or `log_tail:`, flag for re-extraction in Step I.4 (treat as invalidated). Upgrades cache on next incremental pass. Log: `ℹ️ Adjacency entry [TICKER] missing T7.3 cache fields (status/log_tail) — will re-extract to upgrade schema.`

**Single-Read directive** (§4.3): ONE `Read` on `_graph.md` in full. No preview-read + re-read. Legitimate split only when file exceeds Read's 2000-line default — pass `limit:` + `offset:` in ≤2 reads.

### Step I.2: Bucket Changed Files

Separate by directory:
- **Changed Thesis** (`Theses/*.md`): re-extract in Step I.4
- **Changed Sector/Macro** (`Sectors/*.md`, `Macro/*.md`): no per-file action — reverse indexes rebuild fully in Step I.5
- **Changed Research** (`Research/*.md`): no per-file action — orphan list recomputes in Step I.7

### Step I.2.5: Fold `.graph_invalidations` into Changed-Thesis Bucket

`.graph_invalidations` is written by `/status` Step 7.6 and `/prune` Stage 4.5 on thesis closures — neighbor theses whose `cross-thesis:` references point to the now-archived thesis. These neighbors may not have been modified since last graph write; watermark check misses them but their adjacency is stale.

Processing:
1. File absent → skip, proceed to I.3.
2. Read. Each non-empty, non-comment line is a relative thesis path.
3. Per listed path:
   - Exists in `Theses/` → add to Changed Thesis bucket (dedup).
   - Does NOT exist → log `ℹ️ .graph_invalidations: [path] no longer in Theses/ — skipped (likely archived after invalidation).` Ignore.
4. **Do NOT delete yet** — deletion happens at I.9 after graph write succeeds. Crash mid-path → list persists for next run.

Report count at I.11: `Invalidations consumed: [N] neighbor theses (from .graph_invalidations)`.

### Step I.3: Detect Thesis Additions and Removals

Compare current `Theses/*.md` vs baseline adjacency:
- **Added** (on disk, not in baseline): fresh extraction in Step I.4
- **Removed** (in baseline, not on disk): remove from baseline map. Also disappear from I.6 cluster recomputation.

### Step I.4: Re-extract Adjacency for Changed + Added + Invalidated Theses

For each thesis flagged in I.2 (watermark), I.2.5 (invalidations), I.3 (added), or I.1 (missing T7.3 cache fields):

1. Extract outbound `[[wikilinks]]`.
2. Categorize:
   - `Sectors/` → sector
   - `Macro/` → macro
   - `Theses/` → cross-thesis
   - `Research/` → research
3. **Validate target existence** — drop dangling references, log each at `ℹ️` severity (e.g., `ℹ️ Dropped dangling cross-thesis: [TICKER] → [[Theses/TARGET - ...]] (file not in Theses/, likely archived).`). Completes the invalidation cycle opened at I.2.5 (§1.3).
4. **Extract `status:` and `log_tail:`** per Step 2b (same fused Bash block captures both alongside wikilinks).
5. Replace baseline entry with new validated categorization + fresh cache fields.

Unchanged (non-invalidated) theses retain baseline entries — no re-read.

**Single-Bash for ALL changed theses** (N → 1 tool calls):

```bash
for f in "Theses/TICKER1 - Name1.md" "Theses/TICKER2 - Name2.md" "Theses/TICKER3 - Name3.md"; do
  echo "=== FILE: $f ==="
  echo ">>> WIKILINKS"
  grep -oE '\[\[[^]]+\]\]' "$f" \
    | sed 's|^\[\[||; s|\]\]$||; s|\.md$||; s|\|.*$||; s|#.*$||' \
    | sort -u
  echo ">>> STATUS"
  grep -m1 '^status:' "$f" | sed 's/^status: *//' || echo "unknown"
  echo ">>> LOG_TAIL"
  awk '
    BEGIN { in_log=0; pending_date=""; }
    /^## Log[[:space:]]*$/ { in_log=1; next }
    in_log && /^## / { exit }
    in_log && /^### [0-9]{4}-[0-9]{2}-[0-9]{2}/ { pending_date=$2; next }
    in_log && pending_date != "" && /^- / {
      line=$0; sub(/^- /, "", line);
      if (length(line) > 100) line = substr(line, 1, 100) "…";
      entries[++n] = pending_date " | " line;
      pending_date="";
    }
    END {
      start = (n > 3) ? n - 2 : 1;
      for (i = start; i <= n; i++) print entries[i];
      if (n == 0) print "—";
    }
  ' "$f"
done
```

**Regex gotcha** (§3.3): `[^]]+` NOT `[^\]]+` — BSD grep silently returns empty output with the backslash form.

### Step I.5: Rebuild Reverse Indexes (Always Full)

Read every `Sectors/*.md` and `Macro/*.md` unconditionally (~13 + 6 = 19 files, bounded):

#### Macro → Theses
1. Extract `[[Theses/...]]` wikilinks.
2. **Validate target existence**: drop dangling (e.g., `ℹ️ Reverse-index drop: [[Macro/X]] → [[Theses/CLOSED - ...]] (file not in Theses/, likely archived).`). Mirrors I.4 validation to prevent asymmetric state.
3. Build mapping: `Macro/Note → sorted [tickers]` (validated only).

#### Sector → Theses
Same procedure for `Sectors/*.md`.

**Single-Bash** (2 → 1 tool calls):

```bash
for dir in Macro Sectors; do
  echo "=== $dir REVERSE INDEX ==="
  for f in "$dir"/*.md; do
    [ -f "$f" ] || continue
    name=$(basename "$f" .md)
    echo "--- $name"
    grep -oE '\[\[Theses/[^]|#]+' "$f" \
      | sed 's|\[\[Theses/||; s|\.md$||' \
      | sort -u
  done
done
```

Existence validation runs in LLM parse layer against `Theses/` on-disk set known from I.3 — no additional Bash.

### Step I.6: Recompute Cross-Thesis Clusters

Clusters depend only on forward adjacency `cross-thesis:` (fully current after I.4). Recompute from scratch:
1. Pairs (A, B) where A's `cross-thesis:` includes B AND vice versa.
2. Group connected pairs via union-find.
3. Format as cluster table.

### Step I.7: Recompute Orphan List

From in-memory adjacency map:
1. Collect all research wikilinks from every thesis's `research:` → `linked_research`.
2. Inventory `Research/*.md` on disk → `all_research`.
3. Orphans = `all_research − linked_research`, sorted.

**Single-Bash** (2-3 → 1 tool calls):

```bash
ls Research/*.md | sed 's|^Research/||; s|\.md$||' | sort -u > /tmp/all_research.txt
for t in Theses/*.md; do
  grep -oE '\[\[Research/[^]|#]+' "$t"
done | sed 's|\[\[Research/||; s|\.md$||' | sort -u > /tmp/disk_linked.txt
echo "=== ALL RESEARCH (inventory) ==="
cat /tmp/all_research.txt
echo "=== DISK-LINKED RESEARCH (sanity check vs in-memory map) ==="
cat /tmp/disk_linked.txt
echo "=== ORPHANS per disk state (cross-check only) ==="
comm -23 /tmp/all_research.txt /tmp/disk_linked.txt
rm -f /tmp/all_research.txt /tmp/disk_linked.txt
```

**Authoritative orphan set = in-memory**. Disk-linked cross-check surfaces baseline drift: if disk-linked set references files NOT in baseline, log `ℹ️ Baseline drift: [TICKER] has wikilink to [research note] not in baseline adjacency — consider /graph full rebuild.`

### Step I.8: Recount Edges

From updated in-memory state:
- Forward adjacency: per thesis, count of `sectors + macros + cross-thesis + research`.
- Reverse indexes: per row, count of theses listed.

### Step I.9: Apply Changes to `_graph.md` (diff-aware — §10)

Enumerate deltas between the in-memory new state and the Step I.1 parsed baseline. Prefer surgical `Edit`s for small diffs; escalate to full `Write` only when the diff is wide or baseline is legacy.

**Rationale**: full `Write` emits ~400 lines (~15 KB) regardless of change size. Typical post-T7.3 `/graph last` touches 1-3 theses and 0-2 reverse-index rows — surgical Edits emit ~2 KB and stream 5-7× faster end-to-end (§10.4).

#### Step I.9.A: Surgical Edit Path (preferred)

Compute the delta set in memory (no tool calls):

- `frontmatter_changes`: `{date, last_graph_write, theses, sectors, macro, research, edges, orphans, graph_mode}` fields whose values differ from baseline.
- `added_theses` / `removed_theses`: from Step I.3.
- `modified_theses`: TICKERs whose baseline adjacency or cache differs from newly-extracted (Step I.4 set).
  - **log_tail-only modification**: common case — thesis body edited, wikilinks unchanged, only `log_tail:` differs. Emit a granular Edit targeting just the `- **log_tail:**` line + its ≤3 bullets.
  - **Full-block modification**: any wikilink field changed → replace entire block.
- `modified_reverse_rows`: sector/macro rows whose member list differs.
- `added_orphans` / `removed_orphans`: from Step I.7.
- `cluster_table_changed`: true iff cluster set or members differ.

**Escalation triggers** (§10.2) — if ANY true, abort Path A and take Path B:
- Baseline parse failed at Step I.1.
- Pre-T6.10 legacy frontmatter (no `last_graph_write:` field to Edit).
- Pre-T7.3 upgrade scope wide: ≥10 baseline entries missing `status:` or `log_tail:` (upgrading each via granular Edit costs more than one full Write).
- `|modified_theses| > 0.5 × |baseline_theses|` (output-token math favors Write).
- Any anchor uniqueness check fails (§10.3).

**Edit emission order** (per-Edit atomicity — §10.5):

1. **Frontmatter**: one `Edit` per changed field. `old_string = "field: old-value\n"`, `new_string = "field: new-value\n"`. Always advance `date:` + `last_graph_write:`; other counters only if changed.
2. **Removed thesis blocks**: `old_string` = full block (header + field lines + trailing blank line), `new_string` = ``.
3. **Modified thesis — full-block variant**: `old_string` = baseline block verbatim, `new_string` = new block.
4. **Modified thesis — log_tail-only variant**: `old_string` = `  - **log_tail:**\n[baseline bullet lines]`, `new_string` = `  - **log_tail:**\n[new bullet lines]`. Anchor via preceding `### TICKER - Name` header to disambiguate if bullet lines aren't globally unique.
5. **Added thesis blocks**: find alphabetical successor `S` in baseline; `Edit old_string = "### [S]\n"`, `new_string = "[new block]\n\n### [S]\n"`. If new entry is alphabetically last, anchor on `## Reverse Index: Macro → Theses` and prepend block + blank line.
6. **Modified reverse-index rows**: per row, `Edit` old_string = full row line (pipe-delimited), new_string = new row.
7. **Cluster table**: if changed, one `Edit` replaces the whole table (anchor on `## Cross-Thesis Clusters` header through the blank line before `## Orphan Research Notes`).
8. **Orphans**: per add, Insert at sorted position (`old_string` = alphabetical successor's line, `new_string` = new line + successor's line). Per remove, `Edit old_string = "- [[Research/...]]\n"`, `new_string = ""`.

**Mid-cascade failure**: if any Edit errors, `_graph.md` is partially updated. Do NOT retry that Edit — escalate immediately to Path B (re-render full file from in-memory state and `Write` over the partial result). Log: `⚠️ Path A Edit failed for [delta]: [reason] — escalating to full Write to restore consistency.`

#### Step I.9.B: Full Write Path (escalation + initial upgrade runs)

Write merged graph using same format as full rebuild:
- Frontmatter `date:` → today; `last_graph_write:` → Step 0.1 NOW; counts updated.
- Sections: Thesis Adjacency Index (all entries sorted), Macro Reverse Index, Sector Reverse Index, Clusters (from I.6), Orphans (from I.7).

#### Post-edit cleanup

**After Path A last Edit OR Path B Write succeeds**, delete `.graph_invalidations` if exists:
```bash
rm -f .graph_invalidations
```
Order matters (§9.1): delete only AFTER graph update succeeds. Failure → `.graph_invalidations` persists for next run. Report outcome at I.11.

### Step I.10 + I.11: Validate + Release

Single-Bash fuses validation + invalidation cleanup + lock release (2 → 1 tool calls):

```bash
# Validation probes
echo "=== FRONTMATTER ==="
head -15 _graph.md
echo "=== SECTION HEADINGS (expect ≥5 ## and 40 ### adjacency entries) ==="
grep -cE '^## ' _graph.md
grep -cE '^### ' _graph.md
echo "=== REQUIRED SECTION PRESENCE ==="
for h in "## Thesis Adjacency Index" "## Reverse Index: Macro → Theses" "## Reverse Index: Sector → Theses" "## Cross-Thesis Clusters" "## Orphan Research Notes"; do
  grep -qF "$h" _graph.md && echo "✓ $h" || echo "✗ MISSING: $h"
done

# Delete .graph_invalidations AFTER validation succeeds
rm -f .graph_invalidations 2>/dev/null && echo "=== .graph_invalidations cleared ===" || echo "=== .graph_invalidations absent ==="

# Lock release — verify ownership first
LOCK_FILE=".vault-lock"
EXPECTED_TOKEN="<paste-token-captured-from-Step-0.1>"
if [ -f "$LOCK_FILE" ] && grep -q "token: $EXPECTED_TOKEN" "$LOCK_FILE"; then
  rm -f "$LOCK_FILE" && echo "=== LOCK RELEASED ==="
else
  echo "⚠️ Lock ownership check failed at release — skipping rm to avoid stealing another skill's lock."
fi
```

Ordering: `.graph_invalidations` deletion only if validation succeeded; lock release last.

### Step I.11: Report

- **Mode**: `/graph last` from [watermark date] | `/graph [N]` from [N] days ago
- **Update path**: `Path A (surgical Edits: [K] emitted)` | `Path B (full Write — reason: [escalation trigger])`
- **Changed thesis adjacencies re-extracted**: [count] (including [M] pulled from `.graph_invalidations`)
- **Invalidations consumed**: `[N] neighbor theses from .graph_invalidations` or `none (file absent)`
- **Invalidations file deletion**: `deleted` | `skipped (file never existed)` | `⚠️ rm failed — retry on next /graph last`
- **Theses added**: [list, or "none"]
- **Theses removed**: [list, or "none"]
- **Reverse indexes**: rebuilt from scratch (always) — rows modified: [count]
- **Cross-thesis clusters**: [list new/dissolved, or "no structural changes"]
- **Orphan deltas**: [N newly orphaned, M no-longer-orphaned]
- **Edges**: [old → new]
- **Validation**: passed | [list specific failures]
- **No content files modified** — graph update only

## Full Rebuild Path (`/graph` no args, or fallback)

Tool-call budget (§4.2): typical full-rebuild run ~5-6 tool calls vs ~10-12 naïve. Output bit-identical.

### Steps 1-3: Fused Implementation (Single Bash Block)

```bash
echo "=== INVENTORY ==="
for dir in Theses Research Sectors Macro; do
  echo "--- $dir"
  find "$dir" -name '*.md' -type f | sort
done

echo ""
echo "=== THESIS WIKILINKS + STATUS + LOG_TAIL (Steps 2 + 2b input) ==="
for f in Theses/*.md; do
  echo "--- $f"
  echo ">>> WIKILINKS"
  grep -oE '\[\[[^]]+\]\]' "$f" \
    | sed 's|^\[\[||; s|\]\]$||; s|\.md$||; s|\|.*$||; s|#.*$||' \
    | sort -u
  echo ">>> STATUS"
  grep -m1 '^status:' "$f" | sed 's/^status: *//' || echo "unknown"
  echo ">>> LOG_TAIL"
  awk '
    BEGIN { in_log=0; pending_date=""; }
    /^## Log[[:space:]]*$/ { in_log=1; next }
    in_log && /^## / { exit }
    in_log && /^### [0-9]{4}-[0-9]{2}-[0-9]{2}/ { pending_date=$2; next }
    in_log && pending_date != "" && /^- / {
      line=$0; sub(/^- /, "", line);
      if (length(line) > 100) line = substr(line, 1, 100) "…";
      entries[++n] = pending_date " | " line;
      pending_date="";
    }
    END {
      start = (n > 3) ? n - 2 : 1;
      for (i = start; i <= n; i++) print entries[i];
      if (n == 0) print "—";
    }
  ' "$f"
done

echo ""
echo "=== REVERSE INDEXES (Step 3 input) ==="
for dir in Macro Sectors; do
  echo "+++ $dir"
  for f in "$dir"/*.md; do
    [ -f "$f" ] || continue
    echo "--- $(basename "$f" .md)"
    grep -oE '\[\[Theses/[^]|#]+' "$f" \
      | sed 's|\[\[Theses/||; s|\.md$||' \
      | sort -u
  done
done
```

LLM parses output into three top-level sections by `===` markers, sub-buckets per-thesis data by `--- FILE` and `>>>` markers, performs Steps 2-3 categorization (existence validation, bucket by sector/macro/cross-thesis/research) and Step 4 clustering (bidirectional union-find) entirely in reasoning layer. No additional Bash calls for these steps.

**AWK design note** (§7.5): the extraction walks top-to-bottom through `## Log`, pairs each `### YYYY-MM-DD` header with the first `- ` bullet following it (skipping blank lines), keeps last 3 pairs. Bullets >100 chars truncated with `…` (horizontal ellipsis, not `...` — `/lint #42` safe, §7.4).

## Step 1: Inventory Vault

Use the fused block above. `=== INVENTORY ===` section is Step 1 data. Record counts for frontmatter: theses, sectors, macro, research.

## Step 2: Extract Thesis Adjacency

For each thesis in `Theses/`:

1. Extract `[[wikilinks]]` (fused block captures this).
2. Categorize:
   - `Sectors/` → sector
   - `Macro/` → macro
   - `Theses/` → cross-thesis
   - `Research/` → research
   - Other targets → ignore
3. **Validate target existence**: drop dangling references (target file missing — typically archived). Log each drop at `ℹ️` severity in Step 8 report.
4. Build adjacency entry:
   ```
   ### TICKER - Company Name
   - **sectors:** [[Sectors/Sector Name]]
   - **macro:** [[Macro/Note1]], [[Macro/Note2]]
   - **cross-thesis:** [[Theses/OTHER - Company]]
   - **research:** [[Research/2026-01-15 - Topic - Source.md]], ...
   - **status:** active
   - **log_tail:**
     - `2026-04-19 | Stress test: TSM — weakened conviction — [2 more sentences omitted]`
     - `2026-04-18 | Deepened: Industry Context section filled from latest sector research`
     - `2026-04-15 | Status change: conviction medium→high — user reaffirmed after earnings`
   ```

### Step 2b: Extract `status:` and `log_tail:` per thesis (T7.3)

Read-through cache for `/sync` Pass 1 triage and Step 2.5 skill-origin classification. See §7 for design.

**Extraction procedure** (integrated into fused Steps 1-3 Bash block):
- **`status:`** — `grep -m1 '^status:' "$f"` returns YAML frontmatter line. Strip `status: ` prefix. Expected: `draft | active | monitoring | closed`. Missing → `unknown`.
- **`log_tail:`** — last 3 `### YYYY-MM-DD` date headers in document order; first bullet after each. Truncate to 100 chars (word boundary if possible), replace internal newlines with spaces. Format: `YYYY-MM-DD | [bullet text]`. No Log section / <3 entries → emit what's available. Empty Log → `—`.

**Consumer contract**: `/sync` Pass 1 reads 3 prefixes (conviction/status recency, Stress test / Deepened markers, skill-origin); `/sync` Step 2.5 matches most-recent prefix against `_shared/log-prefixes.md` skill-origin list.

**Schema-version signal** (§7.3): `log_tail:` field presence IS the signal. Pre-T7.3 graphs readable; cost consumers an extra round of file reads until `/graph` (full or incremental) upgrades the cache.

## Step 3: Build Reverse Indexes

### Macro → Theses
1. Extract `[[Theses/...]]` wikilinks per `Macro/*.md`.
2. **Validate target existence** (drop dangling, log each).
3. Build reverse mapping (validated only).

### Sector → Theses
Same procedure for `Sectors/*.md`.

Forward and reverse built independently from respective source files. Both apply existence validation. Source-file wikilink wording may still disagree across directions (`/lint #23` catches).

## Step 4: Build Cross-Thesis Clusters

Bidirectional references:
- A lists B in `cross-thesis:` AND B lists A → bidirectional cluster (↔)
- Only one direction → unidirectional (→), note but don't cluster.

Format:
```
| Cluster | Members | Link Type |
|---|---|---|
| AI Compute | [[NVDA]], [[AVGO]], [[MRVL]] | ↔ |
| Memory | [[MU]], [[SNDK]] | ↔ |
```

## Step 5: Identify Orphan Research Notes

Orphan = research note NOT listed in ANY thesis's `research:` field.

**Pure set difference, no additional Bash** (§8): after fused block, LLM holds Research inventory (from `=== INVENTORY ===`) and `linked_research` (from `=== THESIS WIKILINKS ===`). Orphans = `Research inventory − linked_research`, sorted. Emit directly into `## Orphan Research Notes`.

## Step 6: Count Edges

Total unique directional wikilinks from thesis + sector + macro files. Sum deduplicated per source file (same target linked from two different files = two edges). This is the `edges:` frontmatter value.

## Step 7: Write `_graph.md`

**Before overwriting**: if `_graph.md` exists, read and retain old content for Step 8 comparison. Extract: thesis count, edge count, orphan count, adjacency entries, cluster table.

### Step 7.0: No-op Short Circuit (T6.13 — Edit-only when body unchanged)

Compose new graph body in memory, compare to prior body. For no-op full rebuild (common case on quiet vault), body is byte-identical; only frontmatter needs updating.

**Procedure**:
1. Compose full new content (frontmatter + body) in LLM memory.
2. From prior `_graph.md` content, extract everything after second `---` → `prior_body`.
3. Extract same from new composed content → `new_body`.
4. Compare byte-for-byte:
   - **`prior_body == new_body`**: `Edit` tool updates ONLY changed frontmatter fields (`date:`, `last_graph_write:` always advances, `graph_mode:` if differs). Typically 1-3 `Edit` calls. Skip `Write`.
   - **`prior_body != new_body`**: fall through to full `Write`.
5. **Legacy-frontmatter exception**: prior lacks `last_graph_write:` (pre-T6.10) → skip short circuit, full `Write`. Upgrades frontmatter schema in one pass.

Safety + efficiency rationale: §5.

### Step 7.1: Full Write (body changed)

```yaml
---
type: vault-graph
date: YYYY-MM-DD
last_graph_write: YYYY-MM-DDThh:mm:ssZ   # ISO 8601 UTC — T6.10 precision watermark
graph_mode: last | [N] | full            # mode of this write (display only)
theses: [count]
sectors: [count]
macro: [count]
research: [count]
edges: [count]
orphans: [count]
---
```

**`last_graph_write:` population** (§6): reuse `NOW` captured at Step 0.1 lock-acquisition (as `started_at:`). Do NOT issue separate `date -u` call.

**`date:` population**: `YYYY-MM-DD` for display consistency. Same calendar day as `last_graph_write:`.

**`graph_mode:` population**: literal `last`, integer N, or `full`. Read by `/lint #38` for diagnostic messages; not load-bearing.

Sections:
1. `## Thesis Adjacency Index` — all entries from Step 2 (includes T7.3 `status:` + `log_tail:`)
2. `## Reverse Index: Macro → Theses` — from Step 3
3. `## Reverse Index: Sector → Theses` — from Step 3
4. `## Cross-Thesis Clusters` — from Step 4
5. `## Orphan Research Notes` — from Step 5

**After write succeeds**, delete post-write markers (§9):
```bash
rm -f .graph_invalidations
rm -f .sync_all_fresh
```

Failure → both preserved so next `/graph` honors them. Report both delete outcomes in Step 8.

## Step 7.5: Validate Written Graph

Re-read `_graph.md`. Verify:
1. YAML frontmatter parses; all expected fields present (`type`, `date`, `theses`, `sectors`, `macro`, `research`, `edges`, `orphans`)
2. All five section headings exist
3. Every `### TICKER - Name` has at least `sectors:` field
4. **T7.3 cache fields**: every entry carries `status:` and `log_tail:`. Missing either → `⚠️ Adjacency entry [TICKER] missing status: or log_tail: after write — likely extraction glitch; re-run /graph last to refresh.` Non-fatal; continue.
5. All wikilinks valid syntax (no unclosed brackets)
6. Frontmatter counts match content: `theses:` = count of `###` entries; `orphans:` = count of orphan items
7. Every file listed in adjacency exists on disk (spot-check first + last entry + any newly added/changed)

Any fail:
- Checks 1-2 (structural): `❌ Graph rebuild produced a corrupt file — [specific failure]. Re-run /graph.`
- Checks 3-7 (content): `⚠️ Graph rebuilt with minor issues — [specific failure]. Review and re-run /graph if needed.`

Include in Step 8 report.

## Step 8: Report

- **Nodes**: [count] (theses + sectors + macro + research)
- **Edges**: [count]
- **Orphans**: [count]
- **Changes from previous graph** (if captured in Step 7):
  - Theses added/removed: [list]
  - Edges added: [count] | Edges removed: [count]
  - Orphans resolved: [list] | New orphans: [list]
  - Reverse index corrections: [count]
  - Cluster changes: [list new or dissolved clusters]
- **No content files modified** — graph rebuild only
