---
name: stress-test
description: Adversarial thesis testing — act as a short seller to find the weakest points in a thesis. Use when user says "stress test", "devil's advocate", "challenge this thesis", or "break [TICKER]".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * defuddle *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, no qualifiers, no softening. Dense, specific, evidence-backed.

Perform an adversarial stress test on a thesis. Your job is to find reasons this investment FAILS. Do not be balanced — be a prosecutor building the strongest possible case against the position.

## Arguments
$ARGUMENTS should be a ticker (e.g., "NVDA") or a thesis name. If empty, ask the user which thesis to stress test.

## Step 0: Pre-flight (MANDATORY — runs before Phase 1)

### 0.1: Acquire vault lock
Acquire a `ticker:TICKER` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 5 minutes. Capture the token, verify ownership (Procedure 1.5) at every subsequent Bash block, release in the final reporting Bash block.

### 0.2: Rename-marker pre-flight
Run `.claude/skills/_shared/preflight.md` Procedure 2. If `.rename_incomplete.TICKER` exists at vault root, hard-block per the contract's 2.3 collision message. Appending a stress-test Log entry and a new research note while inbound wikilinks are split between old and new names would produce audit artifacts keyed to one name while some vault references still point to the other — compounding the split.

Both checks must pass before proceeding to Phase 1.

## Phase 1: Load the Thesis and All Supporting Evidence

**Two-round parallel-batch pattern.** The only serial dependency is that research-note and sector-note paths are resolved from the thesis's `sector:` frontmatter and Related Research wikilinks — so the thesis must be read before the downstream batch can fire. Everything else parallelizes.

### Round 1 — parallel batch (single message, two tool calls)
Issue these two tool calls in ONE message:
1. **Read** `Theses/TICKER - [Name].md` (the thesis).
2. **Grep** the vault for the ticker string across `Theses/ Sectors/ Macro/ Research/` (catches mentions in notes not explicitly linked from the thesis). Use a single multi-path Grep — do not grep each directory separately.

Wait for both to land. Use the thesis content to enumerate: the sector note path (from `sector:` frontmatter), every research wikilink (from `## Related Research` + `## Log`), and referenced macro notes.

### Round 2 — parallel batch (single message, N tool calls)
Issue ALL of these in ONE message as a single parallel tool-call batch:
- **Read** the Sector Note.
- **Read** every research note linked from the thesis (Related Research + Log-mentioned wikilinks).
- **Read** every Macro note referenced by the thesis (from body or Log wikilinks) and any macro note tagged with the same sector.

Do NOT serialize. A well-linked thesis has ~10-20 supporting files; one parallel batch lands in ~one round-trip instead of ~15 sequential rounds. Do not cap the research-note count — read all of them.

After Round 2 lands, proceed to Phase 2.

## Phase 2: Internal Contradiction Scan
Look specifically for:
- Does the Bull Case rely on assumptions that the Bear Case or Risks section already contradicts?
- Do research notes contain data points that undermine the Non-consensus Insights?
- Has the competitive landscape shifted since the thesis was last updated? (Check research note dates vs thesis Log dates)
- Are the Key Metrics internally consistent? (e.g., high revenue growth + high FCF yield is rare — is the company sacrificing one for the other?)
- Does the conviction level match the strength of evidence? (High conviction with thin research = red flag)
- Are Outstanding Questions still unanswered? If yes, how can conviction be high?
- Are existing Conviction Triggers well-defined? Do they cover the actual failure modes, or are the real risks outside the trigger framework? A thesis with vague triggers ("if competition increases") has a hidden vulnerability — it can degrade without ever formally triggering a reassessment.

## Phase 2.4: Cluster-peer stress context (graph primer)

Per `.claude/skills/_shared/graph-primer.md` Mode A.

Read `_graph.md` once. Fire the Read in parallel with Round 2 reads in Phase 1 (same tool-call batch if Phase 2.4 is scheduled at Phase 1 time; otherwise a single standalone Read here).

For target TICKER:
- `entry = adjacency_index[TICKER]`
- `cluster` = first cluster in clusters where TICKER ∈ cluster.members (or null)
- `cluster_peers = cluster.members - {TICKER}` (empty if no cluster)
- Extract `log_tail` entries from `adjacency_index` for each cluster_peer

Scan `cluster_peer` log_tails for entries with prefixes (case-sensitive, exact-match at line start after `YYYY-MM-DD | `): `Stress test`, `Scenario`, `conviction medium→low`, `conviction high→medium`, `Bear case`, `Risk #`, `Deepened: Bear Case`, `Deepened: Risks`.

Surface to Phase 3 as **stress context, not stress substitute**:

```
Cluster-peer stress signals (graph primer):
  [peer TICKER] — cluster: [cluster name]
    [relevant log_tail entry]
    [relevant log_tail entry]
  [peer TICKER] — cluster: [cluster name]
    [relevant log_tail entry]
```

**Phase 3 explicit framing requirement**: "Use cluster-peer stress signals to classify the target thesis's vulnerability as **idiosyncratic** (peers unaffected) or **cluster-wide** (peers showing parallel stress). Primary stress analysis remains target-thesis-driven; peer context validates or contextualizes the target's failure modes, never substitutes for them."

**Anti-pattern enforced** (contract §Anti-patterns): do NOT skip the target thesis's own Risks / Bear Case / Outstanding Questions based on cluster peer signals. The Phase 1 thesis Read + Phase 2 contradiction scan remain mandatory regardless of peer context.

**Confirmation-bias mitigation** (contract §Confirmation-bias mitigations): if cluster peers are all showing parallel stress, explicitly surface the idiosyncratic failure modes FIRST in Phase 3 output, cluster-wide SECOND. This counters the primer's natural bias toward cluster framing.

**Missing-graph fallback**: per `.claude/skills/_shared/graph-primer.md` §Missing-graph fallback. Phase 3 proceeds target-only.

## Phase 2.5: Optional External Evidence (parallel batch)

The short-seller case often benefits from current-market context the vault doesn't have: recent analyst downgrades, short-interest data, pending litigation, fresh bear-case articles. **If any WebSearch / WebFetch calls are issued during the stress test, batch them in parallel** — one message containing up to 25 invocations, mirroring `/catalyst` Phase 2 and `/thesis` Step 3. Do NOT serialize independent external lookups. If the vault already contains sufficient adversarial evidence, skip this phase entirely; `/stress-test` is spec'd to work off vault content alone.

## Phase 3: Build the Short Case
Structure as a short seller would pitch to an investment committee:

1. **Thesis Vulnerability Summary** — One paragraph: the single biggest reason this investment fails
2. **Evidence Against** — 3-5 points, each citing specific data from vault notes:
   - Market structure risks the thesis underweights
   - Competitive threats documented in sector note but not reflected in thesis
   - Macro sensitivities that are unhedged
   - Financial assumptions that don't hold under stress
   - Management or execution risks
3. **Assumption Stress Table**:

| Bull Assumption | What Must Be True | Evidence For | Evidence Against | Fragility |
|---|---|---|---|---|
| [from thesis] | [specific condition] | [cite vault note] | [cite vault note or gap] | 🟢🟡🔴 |

4. **Research Gaps** — What does the thesis NOT know that it needs to? Which Outstanding Questions remain unanswered? What data would a serious short seller have that this vault doesn't?
5. **Kill Trigger** — What single observable event would invalidate the thesis? Be specific and falsifiable (not "competition increases" but "[COMPANY X] launches [PRODUCT Y] at [PRICE Z] by [DATE]")

## Phase 4: Update the Vault

### 4.0: Write manifest skeleton (M1 — skeleton before destructive edits)

Generate `HHMMSS` once at the start of Phase 4. Reused by all per-file writes and the manifest. Write the manifest skeleton BEFORE any destructive edits (§3 invariant: skeleton → populate → flip).

```bash
HHMMSS=$(date +%H%M%S)
mkdir -p _Archive/Snapshots
```

Manifest path: `_Archive/Snapshots/_stress-test-manifest (stress-test-TICKER-YYYY-MM-DD-HHMMSS).md`. Write initial state:

```yaml
---
type: stress-test-manifest
batch: stress-test-TICKER-YYYY-MM-DD-HHMMSS
status: in-progress
ticker: TICKER
date: YYYY-MM-DD
---

# Stress Test Manifest

> **If `status: in-progress`**, `/stress-test` crashed between Phase 4.0 (skeleton)
> and Phase 4.6 (flip). The Log entry on `Theses/TICKER - Name.md` may or may not
> have landed; check the thesis `## Log` for today's date + `Stress test` prefix.
> Recovery: manually complete or strike through the entry, then flip this
> manifest's `status:` to `completed` or `rm` the manifest.
>
> **If `status: completed`**, Phase 4 finished cleanly. `/rollback` Step 2.5d
> can surface the recorded Log entry for strikethrough review.

## Research note created
- [[Research/YYYY-MM-DD - TICKER - Stress Test]]  *(filled in Phase 4.6 flip)*

## Thesis Log entry appended (Tier B — no snapshot)
- Target: `Theses/TICKER - Name.md`
- Entry date: YYYY-MM-DD
- Entry text: *(filled in Phase 4.6 flip with actual text)*
- Log append outcome: *(filled in Phase 4.6 flip: succeeded | failed reason)*
```

Skeleton write failure → hard abort Phase 4 before any destructive edits. Report the failure and the current state (none of 4.1-4.5 have run yet).

### 4.1: Write the research note (without `propagated_to:`)

Save the stress test to `Research/YYYY-MM-DD - [TICKER] - Stress Test.md` with:
```yaml
---
date: YYYY-MM-DD
tags: [research, stress-test, TICKER]
sector: [from thesis]
ticker: TICKER
source: vault synthesis
source_type: stress-test
# propagated_to: omitted intentionally — set in Phase 4.4 only after Log append succeeds
---
```

> **Why omitted at write time**: mirrors `/scenario` Phase 6.1 + 6.3 atomicity. If the Log append in Phase 4.2 fails (file lock, missing `## Log` section, malformed frontmatter), writing `propagated_to: [TICKER]` here would falsely claim propagation succeeded. Future `/sync` Case 2b would then skip TICKER as already-propagated, never retrying the failed append — permanent audit gap. The all-or-nothing rule trades a single trivial frontmatter Edit at Phase 4.4 for guaranteed eventual consistency.

### 4.2: Append Log entry to thesis (track outcome)

Append a Log entry to the thesis note (max 2 lines):
```
### YYYY-MM-DD
- Stress test [[Research/YYYY-MM-DD - TICKER - Stress Test]]: [top vulnerability], X/Y assumptions rated 🔴 — conviction [unchanged/weakened: reassess + reason]
```
> **Drift coupling**: `/sync` Step 3e excludes entries starting with `"Stress test"` from drift detection. **Registry entry**: `.claude/skills/_shared/log-prefixes.md` §1. Do not change this prefix without updating the registry, `/sync`, and `/lint` check #29 will flag any drift.

Use "weakened" (not "unchanged") when any assumption is rated 🔴 — this ensures `/sync` conviction drift detection counts the entry correctly. The conviction level itself is not changed; the log wording reflects that evidence weakened the case even if the user hasn't acted yet.

**Track outcome**: capture the Edit result as `log_append_succeeded: true | false`. On success, proceed to 4.3 normally. On failure (Edit error, missing `## Log` section), do NOT abort — proceed to 4.3, but skip 4.4's `propagated_to:` write per the atomicity rule below.

### 4.3: Add to Related Research (independent of Log append outcome)

Add the stress test to the thesis's `## Related Research` section (if not already present):
```
- [[Research/YYYY-MM-DD - TICKER - Stress Test]]
```

This is a wikilink registration, not a propagation claim — runs regardless of Phase 4.2 outcome. The Related Research listing is a presence record; `propagated_to:` is the propagation contract.

### 4.4: Atomicity rule for `propagated_to:` update

**Update the research note's `propagated_to:` frontmatter only if Phase 4.2 Log append succeeded.** Mirrors the `/scenario` Phase 6.3 atomicity rule.

- **Log append succeeded** (`log_append_succeeded: true`): edit the research note's frontmatter to add `propagated_to: [TICKER]`. Insertion point: immediately before the closing `---` of frontmatter. This signals to subsequent `/sync` runs that producer-side propagation is complete; `/sync` Case 2b will skip TICKER as already-propagated.
- **Log append failed** (`log_append_succeeded: false`): do **NOT** write `propagated_to:` at all. Leave the frontmatter without the field. The next `/sync` (default mode) will detect TICKER via the file-direct fallback (research note's `ticker: TICKER` frontmatter), apply the per-thesis idempotency check (today's date entry referencing this note? no), and retry the Log append.

> **Why never partial**: matches `/scenario` Phase 6.3 rationale — a partial `propagated_to:` would create a permanent audit gap that future `/sync` runs silently skip because the dedup hint says "already done." For single-ticker `/stress-test`, the partial case is binary (either present-with-TICKER or absent), but the rule is the same: omit on failure, write only on success.

### 4.5: Conviction unchanged (manual decision)

Do NOT change the conviction level — flag it for the user to decide via `/status TICKER conviction old→new [rationale]`.

### 4.6: Flip manifest to completed (M1 — skeleton → populate → flip)

Manifest skeleton was written at Phase 4.0 with `status: in-progress`. Phase 4.6 populates the body with the actual Log entry text and Phase 4.2 outcome, then flips status to `completed`.

> **Batch ID format (C4 fix)**: Ticker-scoped skills include TICKER in the batch ID to prevent collisions when two concurrent `/stress-test` runs on different tickers hit the same HHMMSS. Prior format `stress-test-YYYY-MM-DD-HHMMSS` could collide between simultaneous `/stress-test NVDA` and `/stress-test AMAT`; new format `stress-test-NVDA-YYYY-MM-DD-HHMMSS` and `stress-test-AMAT-YYYY-MM-DD-HHMMSS` are distinct. `/rollback` Step 2.5d cascade detection matches by the `stress-test-` prefix AND the `ticker:` frontmatter field of the manifest.

**Why this exists**: `/stress-test` writes a Log entry to the tested thesis (Tier B — no pre-edit snapshot because the Log is append-only) and a research note. If the user later decides the stress test was invalid (wrong input, stale vault state, experimental run), there's no `/rollback` cascade path to restore the pre-stress-test thesis state. Manual strikethrough of the Log entry is the only remedy. The manifest provides `/rollback` cascade-detection with the Log entry text so the user can choose per-entry annotation (same pattern as `/sync` Tier B sidecar and `/compare` manifest).

**Consolidated flip** (one parallel tool-call block — mirrors `/status` Step 7.9 pattern):

Issue BOTH Edits in ONE message as a single parallel tool-call batch (body populate + frontmatter flip have no ordering dependency — the body section and frontmatter are disjoint regions of the same file):

1. **Body Edit** — populate placeholders with actual values:
   - `## Thesis Log entry appended` — Entry text: the actual Log entry written in Phase 4.2 (including the filled-in vulnerability and ratings).
   - Log append outcome: `succeeded` or `failed (reason)` per Phase 4.2's `log_append_succeeded` tracking.
2. **Frontmatter Edit** — flip `status: in-progress` → `status: completed`. Add `completed_date: YYYY-MM-DD`.

Both Edits land in one round-trip instead of two. If either fails, proceed to the post-flip verification below — the verify step catches partial state.

Expected frontmatter post-flip:
```yaml
---
type: stress-test-manifest
batch: stress-test-TICKER-YYYY-MM-DD-HHMMSS
status: completed
ticker: TICKER
date: YYYY-MM-DD
completed_date: YYYY-MM-DD
---
```

**Verify flip landed**: re-read the manifest frontmatter. Confirm `status: completed` present, `status: in-progress` absent, `completed_date:` equals today.

**On verification failure** (flip Edit silently missed): do NOT retry aggressively. Report `⚠️ Stress-test manifest status flip failed — manifest at [path] remains status: in-progress despite successful stress-test completion. /lint #47 will flag this as Important until manually resolved. Manual fix: edit the manifest and replace status: in-progress with status: completed (add completed_date: today).` Continue to Phase 5.

### Recovery guidance (in manifest body)

The flipped manifest's body includes:

```
## Recovery guidance

To undo this stress test's Log entry (e.g., the stress test was based on wrong
input and the Log entry misrepresents current conviction state):

  /rollback stress-test-TICKER-YYYY-MM-DD-HHMMSS
  → Step 2.5d matches this manifest by batch ID
  → Presents the Log entry above for strikethrough annotation
  → User can choose: (1) leave as historical audit (Tier 2 append-only respected)
                     (2) strikethrough with `~~entry~~ → Reverted YYYY-MM-DD:
                        stress test was invalid because...`
                     (3) manually delete (violates Tier 2 — only for clearly
                        erroneous entries)

The research note at `Research/YYYY-MM-DD - TICKER - Stress Test.md` is NOT
deleted by rollback — it persists as historical record (same rule as scenario
research notes).
```

### 4.6a: Manifest write failure handling

If the manifest write fails (rare — filesystem issue), log the failure but do NOT abort the stress test result. The Log entry and research note are already in place; the missing manifest means future rollback cascade can't surface the Log entry for strikethrough, but manual strikethrough is still possible. Report `⚠️ Stress-test manifest write failed at [path]: [reason]. Rollback cascade recovery will not find this run; manual strikethrough is the fallback path.`

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to register the stress test research note in the dependency map.

## Phase 5: Update _hot.md

Follow `.claude/skills/_shared/hot-md-contract.md` for all _hot.md writes. Read `_hot.md` then edit (do NOT touch Latest Sync or Sync Archive — owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: stress tested [TICKER], top vulnerability found, and whether conviction reassessment was flagged. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry if conviction reassessment was flagged (note: conviction not changed, flagged for user)
3. **Open Questions**: Add any critical research gaps or unanswered questions the stress test exposed

**Word cap**: After all `_hot.md` edits, check total word count. If over 4,000 words (soft cap per `_shared/hot-md-contract.md`), prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap. If over 5,000 (hard cap), abort `_hot.md` update per contract.

## Phase 6: Report
Present findings directly to the user. Lead with the scariest finding. End with a clear verdict: "This thesis survives stress testing" or "This thesis has N critical vulnerabilities that need resolution before conviction can be maintained."

Include in the report:
- **Research note**: `[[Research/YYYY-MM-DD - TICKER - Stress Test]]`
- **Log append**: `succeeded` | `failed (reason — next /sync will retry via file-direct fallback)`
- **`propagated_to:` frontmatter**: `set ([TICKER])` | `omitted (Log append failed — next /sync will retry)`

**Run `/sync` to propagate stress test findings to affected sector notes and cross-thesis references.** If the Log append failed, `/sync` will additionally retry the append via file-direct fallback (research note's `ticker: TICKER` resolves to the thesis, today's-date idempotency check passes since no entry was written, and the Log entry lands on retry).
