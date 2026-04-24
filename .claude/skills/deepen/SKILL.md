---
name: deepen
description: Targeted deep research to fill a specific gap in an existing thesis. Use when user says "deepen", "flesh out", "expand on", "fill in", or specifies a thesis section to improve.
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * cp * mkdir * defuddle *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Surgically improve one section of an existing thesis with deep research. This is NOT a full thesis rewrite — it's targeted enhancement of the weakest or most requested part.

## Arguments
$ARGUMENTS should be: `[TICKER] [optional: section name]`
- Examples: `NVDA Outstanding Questions`, `BESI Industry Context`, `LITE`, `APP Bull Case`
- If no section is specified, auto-detect the weakest section (see Phase 2)

## Phase 0: Pre-flight (MANDATORY — runs before Phase 1)

### 0.1: Acquire vault lock
Acquire a `ticker:TICKER` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 10 minutes (deep research may be long-running). Capture the token, verify ownership (Procedure 1.5) at every subsequent Bash block, release in the final reporting Bash block.

### 0.2: Rename-marker pre-flight
Run `.claude/skills/_shared/preflight.md` Procedure 2. If `.rename_incomplete.TICKER` exists at vault root, hard-block per the contract's 2.3 collision message. Rewriting a thesis section while wikilinks are split across old and new names would compound the split — the rewrite would embed wikilinks keyed to the current (new) filename while some inbound references still point to the old name.

Both checks must pass before proceeding to Phase 1.

### 0.3: Section existence probe (only if specific section was specified)

If `$ARGUMENTS` includes a section name (not auto-detect mode), run the refused-section check first, then `.claude/skills/_shared/preflight.md` Procedure 4 (section existence probe) against the thesis file with the target `## [Section Name]` heading.

#### 0.3a: Refused-section check

Certain sections are auto-managed archives or skill-owned artifacts — `/deepen` must never operate on them. If the user-supplied section name (case-insensitive, whitespace-normalized) matches any entry below, hard-abort with the explanation shown:

| Section | Owner | Abort message |
|---|---|---|
| `Legacy Callouts` | `/archive-callouts` | `❌ ## Legacy Callouts is an automated archive of swept addressed callouts, owned exclusively by /archive-callouts. It contains historical audit trail, not deepen-eligible analytical content. To surface insight from legacy callouts, deepen the analytical section they originally belonged to (e.g., Bull Case, Industry Context). To change the archive itself, do NOT use /deepen — either /rollback the last /archive-callouts sweep, or manually edit the plain-bullet entries and accept that /archive-callouts may re-sweep them on the next run.` |

Do NOT proceed to Procedure 4 if the refused-section check fires. Report the abort reason to the user and exit.

#### 0.3b: Section existence probe (standard)

If the section does NOT exist in the thesis:

```
❌ Section "## [requested section]" not found in Theses/TICKER - Name.md.

Sections present in this thesis:
  - ## Summary
  - ## Key Non-consensus Insights
  - ## [list every ## heading found in the thesis]

Sections expected per Templates/Thesis Template.md but missing:
  - ## [missing section 1]
  - ## [missing section 2]
  - ...

Options:
  (a) /deepen TICKER [existing-section]   — deepen a section that exists
  (b) /deepen TICKER                      — auto-detect weakest present section (Phase 2)
  (c) Restore missing section from Templates/Thesis Template.md manually,
      then re-run /deepen TICKER [section]
  (d) /lint TICKER                        — surface all template drift first (check #14)

Aborted — no changes made to the thesis.
```

**Do NOT silently create the section.** Structural changes to thesis templates must be explicit user action. The thesis's current section inventory is the user's (or a prior skill's) intentional state; `/deepen` deepens existing sections, never authors new ones from nothing.

If auto-detect mode (`$ARGUMENTS` is just TICKER), skip this probe — Phase 2 evaluates only sections that actually exist and scores their weakness. The Phase 2 scoring loop must exclude `## Legacy Callouts` (owned by `/archive-callouts`) and `## Log` (Tier 2 append-only) from weakness candidates regardless of their contents.

## Phase 1: Load Context

**Two-round parallel-batch pattern.** The only serial dependency is that research-note and sector-note paths are resolved from the thesis's `sector:` frontmatter and Related Research wikilinks — so the thesis must be read before the downstream batch can fire. Everything else parallelizes.

### Round 1 — parallel batch (single message, two tool calls)
Issue these two tool calls in ONE message:
1. **Read** `Theses/TICKER - [Name].md` (the thesis).
2. **Grep** the vault for the ticker string across `Theses/ Sectors/ Macro/ Research/` with `glob='*.md'` (catches mentions in notes not yet linked, scoped to markdown). Use a single multi-path Grep — do not grep each directory separately.

Wait for both to land. Use the thesis to enumerate: sector note path (from `sector:` frontmatter), every research wikilink (from `## Related Research` + `## Log`), referenced macro notes.

### Round 2 — parallel batch (single message, N tool calls)
Issue ALL of these in ONE message as a single parallel tool-call batch:
- **Read** the Sector Note.
- **Read** every research note linked from the thesis (Related Research + Log-mentioned wikilinks).
- **Read** every Macro note referenced by the thesis (from body or Log wikilinks) and any macro note tagged with the same sector.

Do NOT serialize. A well-linked thesis has ~10-20 supporting files; one parallel batch lands in ~one round-trip. Do not cap the research-note count — read all of them.

After Round 2 lands, proceed to Phase 2.

## Phase 2: Identify the Target
If a section was specified in $ARGUMENTS, use that. Otherwise, auto-detect:

**Weakness scoring** (check each, flag the worst):
- **Empty or stub sections**: sections with just `-` or `<!-- -->` placeholder comments
- **Key Non-consensus Insights**: if fewer than 3 substantive paragraphs, this is the priority (CLAUDE.md marks this as the most important section)
- **Outstanding Questions**: if fewer than 3 questions, the thesis hasn't been properly challenged
- **Business Model & Product Description**: if under 200 words, the understanding is superficial
- **Industry Context**: if missing value chain analysis or competitive dynamics
- **Key Metrics**: if the table has empty cells or data older than 6 months
- **Bull/Bear Case imbalance**: if one is dramatically shorter than the other (suggests bias)
- **Risks**: if fewer than 3 risks, the thesis is underprotected
- **Catalysts**: if empty or all dates have passed
- **Conviction Triggers**: if missing or vague (not falsifiable)

Tell the user which section you're targeting and why before proceeding.

## Phase 2.5: Graph-primer peer-section cross-read (comparative sections only)

**GATE**: Execute ONLY if the `target_section` resolved in Phase 2 is in the comparative-sections whitelist:
- `Industry Context`
- `Key Non-consensus Insights`
- `Bull Case` (when the deepen framing is comparative — user mentioned peers or competitive dynamics)
- `Bear Case` (same condition as Bull Case)

NOT applicable (SKIP Phase 2.5 entirely if target_section is one of these):
- `Summary`, `Business Model & Product Description`, `Key Metrics`, `Outstanding Questions`, `Catalysts`, `Risks`, `Conviction Triggers`, `Related Research`, `Log`, `Legacy Callouts`

Rationale for gating: peer section content has signal for competitive/comparative framing but becomes noise for idiosyncratic sections (Risks, Catalysts, Outstanding Questions are typically thesis-specific, not cluster-wide).

Per `.claude/skills/_shared/graph-primer.md` Mode A.

Read `_graph.md` once (in parallel with Phase 1 Reads if possible; otherwise as a single Read before Phase 3). Extract:
- `entry = adjacency_index[TICKER]`
- `sector_peers = union over s ∈ entry.sectors of sector_reverse[s] - {TICKER}`
- Rank `sector_peers` by most-recent `log_tail` entry date. Take top 3.

Bash-extract `target_section` from each peer thesis in ONE batch (not per-peer serial Bash):

```bash
TARGET_SECTION="[section name from Phase 2]"
for f in "Theses/[peer1] - Name.md" "Theses/[peer2] - Name.md" "Theses/[peer3] - Name.md"; do
  echo "=== $f ==="
  awk -v sec="## $TARGET_SECTION" '
    $0 == sec { in_sec=1; next }
    in_sec && /^## / { exit }
    in_sec { print }
  ' "$f"
done
```

Inject peer section content as comparative primer for Phase 3 + Phase 5:

```
Peer-section comparative primer (graph primer):
  === [peer TICKER] ## [section]
    [peer content]
  === [peer TICKER] ## [section]
    [peer content]
```

**Phase 3 + Phase 5 explicit framing requirement**: "Use peer sections to identify what's **missing or underdeveloped** in the target thesis's section relative to how peers frame the same analytical dimension. Do NOT replicate peer content verbatim. Peer content identifies gaps; target-specific research fills them."

**Anti-pattern enforced** + **Peer-dominance mitigation**: `.claude/skills/deepen/RATIONALE.md` §5. Summary — the target's divergence from peers is often the thesis itself; do not substitute peer content for target-specific depth.

**Missing-graph fallback**: per `.claude/skills/_shared/graph-primer.md` §Missing-graph fallback. Phase 3 + Phase 5 proceed target-only. Skip peer cross-read silently.

## Phase 3: Deep Research
1. **Vault research first**: Extract every relevant data point from existing research notes, sector notes, and macro notes. Do not duplicate what's already captured.
2. **Web research**: Search for recent developments specific to the target section:
   - For Key Non-consensus Insights: search for sell-side consensus, then find evidence that contradicts it
   - For Outstanding Questions: search for answers to existing questions AND identify new questions a skeptical investor would ask
   - For Business Model: search for revenue breakdowns, segment reporting, product specs, analyst commentary on business model
   - For Industry Context: search for market share data, competitive dynamics, recent M&A, new entrants
   - For Key Metrics: search for latest financial data (quarterly earnings, guidance)
   - For Bull/Bear Case: search for the strongest version of whichever side is underweight
   - For Risks: search for bear cases, short seller reports, regulatory risks, technological disruption
   - For Catalysts: search for upcoming earnings dates, product launches, regulatory decisions, industry events
   - For Conviction Triggers: search for the most likely binary events that would decisively change the thesis
3. **Cross-reference**: Check if new findings affect other theses in the vault

## Phase 4: Pre-Edit Safety — Snapshot

Before rewriting the target section, snapshot the thesis:

1. Create snapshot directory if needed:
   ```bash
   mkdir -p _Archive/Snapshots
   ```
2. Generate `HHMMSS` once at Phase 4 start. Reused by the snapshot (this phase) and the manifest (Phase 4.5):
   ```bash
   HHMMSS=$(date +%H%M%S)
   ```
3. Copy the current thesis note:
   ```bash
   cp "Theses/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (pre-deepen YYYY-MM-DD-HHMMSS).md"
   ```
4. Read the newly created snapshot, then add to its frontmatter:
   ```yaml
   snapshot_of: "[[Theses/TICKER - Company Name]]"
   snapshot_date: YYYY-MM-DD
   snapshot_trigger: deepen
   snapshot_batch: deepen-TICKER-YYYY-MM-DD-HHMMSS
   ```

   **Batch ID format**: `deepen-TICKER-YYYY-MM-DD-HHMMSS`. Rationale in `.claude/skills/deepen/RATIONALE.md` §2.

## Phase 4.5: Write deepen manifest skeleton (M3 — skeleton before destructive edits)

> **Why this manifest exists (M3)**: `.claude/skills/deepen/RATIONALE.md` §1.

Write manifest at `_Archive/Snapshots/_deepen-manifest (deepen-TICKER-YYYY-MM-DD-HHMMSS).md`:

```yaml
---
type: deepen-manifest
batch: deepen-TICKER-YYYY-MM-DD-HHMMSS
status: in-progress
ticker: TICKER
section: [Section Name from Phase 2]
date: YYYY-MM-DD
---

# Deepen Manifest

> **If `status: in-progress`**, `/deepen` crashed between Phase 4.5 (skeleton)
> and Phase 7.5 (flip). Check thesis `## Log` for today's date + `Deepening` prefix
> to see whether the provisional entry has been superseded by the final `Deepened` entry.
> Recovery: `/rollback deepen-TICKER-YYYY-MM-DD-HHMMSS` → Step 2.5g offers:
>   (a) Restore thesis from pre-deepen snapshot (undo section rewrite + Log entry).
>   (b) Full cascade — (a) + delete supporting research note (if Phase 6 created one).
>   (c) Cancel.
>
> **If `status: completed`**, Phase 4-7 all succeeded. `/rollback` Step 2.5g is
> still available within the cascade's per-snapshot age window.

## Thesis snapshot
- [[_Archive/Snapshots/TICKER - Company Name (pre-deepen YYYY-MM-DD-HHMMSS)]]

## Thesis target
- `Theses/TICKER - Company Name.md`
- Section deepened: [Section Name]

## Research note created (if any)
- *(filled in Phase 7.5 flip: wikilink to Research note, or `none — Phase 6 judged new research insubstantial`)*

## Phase 5 Log-append outcome
- *(filled in Phase 7.5 flip: succeeded | provisional-entry-stuck + correction-appended)*
```

Skeleton write failure → hard abort BEFORE Phase 5 destructive edits. Thesis snapshot (Phase 4) exists but is orphan — it falls under standard `/clean` orphan protection (90-day default, opt-in deletion). Report failure to user.

## Phase 5: Rewrite the Target Section

### 5a: Pre-announce Log entry (audit trail before destructive edit)
Append a provisional Log entry to the thesis BEFORE rewriting the section. This ensures an audit trail exists even if the skill fails mid-rewrite:
```
### YYYY-MM-DD
- Deepening [Section Name] — in progress. Snapshot: [[_Archive/Snapshots/...]]
```

### 5b: Rewrite the section
- Rewrite the section in-place, preserving the thesis note's overall structure
- Follow the conventions from CLAUDE.md and the Thesis Template:
  - Non-consensus Insights: 3-5 one-paragraph summaries of what the market is missing
  - Outstanding Questions: 3-10 one-paragraph summaries of what a skeptical IC would ask
  - Business Model: in-depth with analogies, product specs, revenue segmentation
  - Industry Context: competitive dynamics, market share shifts, value chain analysis
  - Conviction Triggers: concrete, falsifiable if/then statements with specific thresholds
- **Integrate, don't append** — the section should read as a coherent whole, not show seams between old and new content
- Bold any genuinely new data points or insights not previously in the vault
- Add wikilinks to any vault notes referenced

### 5c: Finalize Log entry
After the rewrite succeeds, use `Edit` to atomically replace the provisional Log entry with the final version:
```
### YYYY-MM-DD
- Deepened [Section Name]: [key finding] — conviction [unchanged/strengthened/weakened + reason]. Snapshot: [[_Archive/Snapshots/...]]
```
Replace `Deepening [Section Name] — in progress` with `Deepened [Section Name]: [key finding] — conviction [impact + reason]`.

**Verify and retry**: After the Edit, run a single `grep -q` Bash probe to confirm the provisional text (`Deepening [Section Name] — in progress`) is gone. `grep -q` is faster than a Read tool call and returns a clean exit status without injecting the thesis body into context:

```bash
# Exit 0 = provisional text STILL present (Edit failed silently)
# Exit 1 = provisional text absent (Edit succeeded)
if grep -qF "Deepening [Section Name] — in progress" "Theses/TICKER - Company Name.md"; then
  echo "EDIT_FAILED_PROVISIONAL_STUCK"
else
  echo "EDIT_OK"
fi
```

1. **`EDIT_OK`** → provisional text absent → proceed to Phase 6.
2. **`EDIT_FAILED_PROVISIONAL_STUCK`** → retry with broader context:
   - Include the full `### YYYY-MM-DD` date header AND the provisional line as `old_string` to ensure uniqueness.
   - Re-run the same `grep -qF` probe after the retry to confirm.
3. **Retry also failed** (grep still exits 0) → append a corrective entry immediately below the stuck provisional entry:
   ```
   - ↳ CORRECTION: Deepened [Section Name]: [key finding] — conviction [impact + reason]. Supersedes incomplete entry above.
   ```
   This preserves the append-only Log contract while ensuring the audit trail is always complete. `/sync` drift detection recognizes both `"Deepened"` and `"↳ CORRECTION: Deepened"` prefixes.

> **Drift coupling**: `.claude/skills/deepen/RATIONALE.md` §4. Registry entries: `.claude/skills/_shared/log-prefixes.md` §2, §3, §4. `/lint #29` flags drift.

> **Failure states**: If the skill fails after 5a but before 5b → Log shows "Deepening... in progress" but section is unchanged; snapshot is unnecessary (thesis body intact). If it fails after 5b but before 5c → Log shows "Deepening... in progress" with section already rewritten; the verify-and-retry mechanism (above) will correct the Log entry. Both states are recoverable via snapshot. `/lint` #28 (partial write detection) flags the `"Deepening"` prefix as an indicator — if the corrective entry exists alongside it, lint should downgrade to Nice to Have.

## Phase 6: Update the Vault
1. If new research was substantial, also save a supporting research note to Research/:
   `Research/YYYY-MM-DD - [TICKER] - [Section Topic] Deep Dive.md`
   ```yaml
   ---
   date: YYYY-MM-DD
   tags: [research, deep-dive, TICKER]
   sector: [from thesis]
   ticker: TICKER
   source: vault synthesis
   source_type: deep-dive
   propagated_to: [TICKER]
   ---
   ```
2. Add any new wikilinks to the thesis Related Research section

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to register any new research note in the dependency map.

## Phase 7: Update _hot.md

Follow `.claude/skills/_shared/hot-md-contract.md` — compression policy, per-section budgets, truncation-marker avoidance, and cap handling are centralized there. Read `_hot.md` then edit (do NOT touch Latest Sync or Sync Archive — owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: deepened [TICKER] [Section Name], key finding, and the logical next research step. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry if conviction was changed or flagged for reassessment
3. **Open Questions**: Mark resolved any questions this research answered; add new questions raised

**Word cap**: After all `_hot.md` edits, check total word count. If over 4,000 words (soft cap per `_shared/hot-md-contract.md`), prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap. If over 5,000 (hard cap), abort `_hot.md` update per contract.

## Phase 7.5: Flip deepen manifest to completed (M3 — skeleton → populate → flip)

Manifest skeleton was written at Phase 4.5 with `status: in-progress`. Phase 7.5 populates placeholders and flips status.

**Populate body** (Edit Phase 4.5 skeleton, replacing `*(filled in Phase 7.5 flip)*` placeholders):

```markdown
## Research note created (if any)
- [[Research/YYYY-MM-DD - TICKER - [Section Topic] Deep Dive]]
  *(OR `none — Phase 6 judged new research insubstantial`)*

## Phase 5 Log-append outcome
- succeeded: provisional `Deepening [Section Name] — in progress` replaced by final `Deepened [Section Name]: [key finding] — conviction [impact]`.
  *(OR `provisional-entry-stuck + correction-appended: final Log entry written as corrective ↳ CORRECTION block, provisional text preserved`)*
```

**Flip frontmatter**: `status: in-progress` → `status: completed`. Add `completed_date: YYYY-MM-DD`.

Expected frontmatter post-flip:
```yaml
---
type: deepen-manifest
batch: deepen-TICKER-YYYY-MM-DD-HHMMSS
status: completed
ticker: TICKER
section: [Section Name]
date: YYYY-MM-DD
completed_date: YYYY-MM-DD
---
```

**Verify flip landed** (Edit-return inspection — no re-read): inspect the frontmatter-flip Edit's return value. The Edit tool reports success iff the replacement landed; the returned snippet shows the post-edit frontmatter. Confirm `status: completed` present, `status: in-progress` absent, `completed_date:` equals today from the Edit-return content.

**On verification failure** (Edit-return indicates replacement did not produce expected frontmatter, or Edit tool returned error): report `⚠️ Deepen manifest status flip failed — manifest remains status: in-progress despite successful deepen completion. /lint #50 will flag this as Important. Manual fix: edit manifest frontmatter — replace status: in-progress with status: completed (add completed_date: today).` Continue to Phase 8.

## Phase 8: Report
Tell the user:
- Which section was deepened and why it was the priority
- Snapshot saved to: `[[_Archive/Snapshots/...]]`
- The 2-3 most important new findings
- Whether conviction should be reassessed based on what was found
- Theses requiring `/sync`: [list any tickers where cross-references suggest propagation is needed]
- **Run `/sync` to propagate these findings to affected sector notes, macro notes, and cross-thesis references.**
