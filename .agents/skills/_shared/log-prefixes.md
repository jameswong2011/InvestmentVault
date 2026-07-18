---
type: shared-contract
purpose: Single source of truth for Log-entry prefixes that carry cross-skill semantic weight.
last_reviewed: 2026-07-12
---

<!--
Editing note (2026-04-19): `$sync Step 2.5 skill-origin classification` added as a consumer to every "skill-origin" prefix (entries #5, #6, #7, #8, #9, #11, #12, #13, #14, #15). These prefixes signal that the originating skill already handled sector/macro propagation — `$sync` uses the list to skip redundant Step 4/5 re-propagation for thesis-only changes. See `$sync` Step 2.5 for consumer logic; `$lint #29` enforces alignment.

Editing note (2026-05-22): `Numbers refresh:` (entry §18) added as a skill-origin prefix when `$numbers` was introduced. A numeric refresh of the Key Metrics table is hygiene, not analysis — `$sync` skips downstream propagation. Both `$sync` Step 2.5 enumeration (line ~311) and this registry updated atomically per the editing protocol below.

Editing note (2026-07-12): `Metrics synced:` (entry §20) added as a skill-origin prefix when `$deepen --sync-metrics` mode was introduced. A metric-sync pass reconciles a note's own stale prose figures (across Summary/Insights/Questions/Risks/Key-Metrics-Notes-cells) against fresh data — already-refreshed by `$numbers` where available, or fetched fresh via the same FMP-first/web-search-fallback waterfall otherwise. This is hygiene/consistency maintenance, not new analysis — same rationale as `Numbers refresh:` — so `$sync` skips downstream propagation. Both `$sync` Step 2.5 enumeration and Step 3e drift-exclusion list, and this registry, updated atomically per the editing protocol below.
-->


# Log Prefix Registry

> **This file is a load-bearing contract.** Every prefix listed here is produced by at least one skill and interpreted by at least one consumer skill (or `$lint` check). Editing any prefix requires updating every producer and consumer simultaneously.
>
> **Before editing**: grep all SKILL.md files for the current prefix string and the "Drift coupling" warnings to identify every touch-point.
>
> **After editing**: run `$lint` — check #29 verifies producer/consumer alignment against this file.

## How to read this file

Each entry has the form:

```yaml
- prefix: "[exact string match at start of Log bullet]"
  case_sensitive: true | false
  match_anchor: "line-prefix" | "contains"          # how consumers search for it
  producer:
    skill: /skill-name
    step: "Step/Phase reference"
    emits_when: "[condition]"
  consumers:
    - skill: $sync
      step: "Step 3e | Step 3f | Rule 8"
      role: "drift-anchor | drift-exclusion | dedup-key | audit-only"
    - skill: $lint
      check: "#28 | #12 | etc."
      role: "signal | classifier"
  example: "### 2026-04-17\n- [literal example line]"
  breakage_if_changed: "[one-sentence description of what silently breaks]"
```

---

## Registry

### 1. Stress test

```yaml
prefix: "Stress test"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $stress-test
  step: Phase 4 step 2
  emits_when: always (one per stress test run)
consumers:
  - skill: $sync
    step: Step 3e drift detection
    role: drift-exclusion
example: |
  ### 2026-04-17
  - Stress test [[Research/2026-04-17 - NVDA - Stress Test]]: top vulnerability China risk, 3/7 assumptions rated 🔴 — conviction weakened: reassess
breakage_if_changed: "$sync drift detection no longer excludes stress-test entries → every stress test inflates drift signal by one, producing false ⚠️ Conviction drift warnings on healthy theses."
```

### 2. Deepening (provisional pre-announcement)

```yaml
prefix: "Deepening"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $deepen
  step: Phase 5a
  emits_when: always (pre-rewrite audit trail)
consumers:
  - skill: $lint
    check: "#28 partial-write detection"
    role: signal (indicates $deepen may have failed mid-rewrite)
  - skill: $sync
    step: Step 3e drift detection
    role: drift-exclusion (unconditional) — provisional entries carry no conviction sentiment and stuck "Deepening" entries (no matching "Deepened" or "↳ CORRECTION: Deepened") must not bias the drift window
example: |
  ### 2026-04-17
  - Deepening Outstanding Questions — in progress. Snapshot: [[_Archive/Snapshots/NVDA - Nvidia (pre-deepen 2026-04-17-1530)]]
breakage_if_changed: "$lint #28 partial-write detection misses failed deepen operations → truncated sections persist undetected. $sync drift detection regresses: stuck Deepening entries consume slots in the last-5 window, potentially suppressing true drift signals by accident or producing biased windows on failed-$deepen states."
```

### 3. Deepened (finalized)

```yaml
prefix: "Deepened"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $deepen
  step: Phase 5c (atomic replacement of Deepening entry)
  emits_when: rewrite completed successfully
consumers:
  - skill: $sync
    step: Step 3e drift detection
    role: drift-exclusion (when chain-linked to $stress-test or within 14 days of one — `deepened_exclusion_days` in `.drift-config.md`, default 14; matches $sync Step 3e)
  - skill: $lint
    check: "#28 partial-write detection"
    role: classifier (presence downgrades Deepening match to Nice to Have)
example: |
  ### 2026-04-17
  - Deepened Outstanding Questions: 3 new questions on hybrid bonding yield data — conviction strengthened, design wins accelerating. Snapshot: [[_Archive/Snapshots/...]]
breakage_if_changed: "$sync drift detection stops excluding deepen entries → gap-filling research falsely counts as deterioration evidence."
```

### 4. ↳ CORRECTION: Deepened (retry corrective)

```yaml
prefix: "↳ CORRECTION: Deepened"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $deepen
  step: Phase 5c retry-and-append fallback
  emits_when: Edit retry failed — corrective entry appended below stuck provisional entry
consumers:
  - skill: $sync
    step: Step 3e drift detection
    role: drift-exclusion (same as "Deepened")
  - skill: $lint
    check: "#28 partial-write detection"
    role: classifier (presence alongside a "Deepening" entry downgrades lint severity to Nice to Have)
example: |
  ### 2026-04-17
  - Deepening Outstanding Questions — in progress. Snapshot: [[_Archive/Snapshots/...]]
  - ↳ CORRECTION: Deepened Outstanding Questions: [findings] — conviction strengthened. Supersedes incomplete entry above.
breakage_if_changed: "$deepen's retry-and-append mechanism becomes silently broken — retries leave the audit trail with stuck Deepening entries that $lint elevates to Important severity."
```

### 5. Conviction reaffirmed

```yaml
prefix: "Conviction reaffirmed"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $status
  step: Step 2R (Reaffirm Flow)
  emits_when: user runs `$status TICKER reaffirm [rationale]`
consumers:
  - skill: $sync
    step: Step 3e drift detection
    role: drift-window-anchor (resets the drift-detection window — only entries after this anchor are counted)
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier (thesis-only reaffirm carries no propagatable research delta — Step 4.-1 / 5.-1 skip sector and macro re-propagation)
example: |
  ### 2026-04-17
  - Conviction reaffirmed at high after drift review — earnings miss was one-time, competitive position unchanged
breakage_if_changed: "$sync drift detection no longer anchors — reaffirmed theses keep firing drift warnings because the anchor isn't recognized."
```

### 6. Status change: conviction

```yaml
prefix: "Status change: conviction"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $status
  step: Step 4 (conviction change branch)
  emits_when: conviction change applied via `$status TICKER conviction old→new`
consumers:
  - skill: $sync
    step: Step 3e drift detection
    role: drift-window-anchor (resets the drift-detection window)
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier ($status Step 5 already updated sector — Step 4.-1 skips re-propagation to avoid duplicate analytical edits)
example: |
  ### 2026-04-17
  - Status change: conviction medium → low — China risk unhedgeable. Snapshot: [[_Archive/Snapshots/...]]
breakage_if_changed: "$sync drift detection cannot find the anchor post-conviction-change → drift signal may re-fire immediately on the same evidence."
```

### 7. Status change: (non-conviction)

```yaml
prefix: "Status change:"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $status
  step: Step 4 (non-closure status change branch)
  emits_when: status change applied via `$status TICKER status old→new` (excluding closures)
consumers:
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier ($status Step 5 already updated sector Active Theses — Step 4.-1 skips re-propagation)
example: |
  ### 2026-04-17
  - Status change: active → monitoring — awaiting Q3 earnings catalyst. Snapshot: [[_Archive/Snapshots/...]]
breakage_if_changed: "Audit trail readability only — no automated consumer breaks."
```

### 8. CLOSED

```yaml
prefix: "CLOSED"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $status, $prune
  step: $status Step 4 closure branch; $prune Stage 2
  emits_when: thesis transitions to status: closed (archival)
consumers:
  - skill: $sync
    step: Step 1 Missing-file-resilience, Step 7 Rule 9
    role: implicit (archived theses are detected by file absence, but CLOSED Log entry is the final audit marker)
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier (closure is handled by producer skill's own sector + graph invalidation writes — Step 4.-1 skips re-propagation for the closed thesis if still in Theses/ pending mv)
  # NOTE: $lint #33 detects the same partial-closure state (status: closed AND still
  # in Theses/) via FRONTMATTER — it does not match the "CLOSED" Log literal, so it is
  # not a `- skill:` consumer here. (Listing it as one produced a false #29 consumer-
  # drift CRITICAL once the literal left lint's text during the 2026-07 skills cleanup.)
example: |
  ### 2026-04-17
  - CLOSED: thesis invalidated by margin compression. Archived.
breakage_if_changed: "Closure audit trail is broken; lint cannot distinguish pending-archive from stuck-open theses."
```

### 9. Prune upgrade

```yaml
prefix: "Prune upgrade"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $prune
  step: Stage 3
  emits_when: approved upgrade in prune batch
consumers:
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier ($prune Stage 4 already updated sector conviction display — Step 4.-1 skips re-propagation)
example: |
  ### 2026-04-17
  - Prune upgrade low → medium: 3 new research notes since creation, competitive position strengthened — conviction strengthened, design wins accelerating
breakage_if_changed: "Audit trail readability only."
```

### 10. Scenario

```yaml
prefix: "Scenario "
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $scenario
  step: Phase 6 (per affected thesis log append)
  emits_when: thesis rated Major impact in scenario Phase 3 table
consumers:
  - skill: audit-only
example: |
  ### 2026-04-17
  - Scenario [[Research/2026-04-17 - Scenario - China Taiwan]]: negative via supply chain disruption — conviction weakened, TSMC capex at risk
breakage_if_changed: "Audit trail readability only. Note the trailing space is significant — it distinguishes the prefix from a Log entry that happens to mention 'scenarios' in prose."
```

### 11. Initial thesis created

```yaml
prefix: "Initial thesis created"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $thesis
  step: Step 4 (initial Log entry)
  emits_when: new thesis created
consumers:
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier ($thesis Step 5 already added to sector Active Theses — Step 4.-1 skips redundant sector re-propagation when no co-changed research note drives the change)
  # NOTE: $prune's draft-limbo flag keys on the Log-entry COUNT (exactly 1 entry), not
  # on the "Initial thesis created" literal — so it is not a `- skill:` consumer here.
  # (Listing it as one produced a false #29 consumer-drift CRITICAL after the literal
  # left prune's text during the 2026-07 skills cleanup.)
example: |
  ### 2026-04-17
  - Initial thesis created. Conviction: medium — non-consensus view on CPO attach rate
breakage_if_changed: "$prune's draft-limbo flag may misclassify theses with edited initial entries."
```

### 12. ROLLBACK to snapshot

```yaml
prefix: "ROLLBACK to snapshot"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $rollback
  step: Step 5.4
  emits_when: every successful rollback
consumers:
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier ($rollback Step 6 already handled sector note restoration — Step 4.-1 skips re-propagation; the thesis body reverted to snapshot state carries no new research delta)
example: |
  ### 2026-04-17
  - ROLLBACK to snapshot (2026-04-16, pre-sync). 2 log entries from 2026-04-16 lost. Safety snapshot: [[_Archive/Snapshots/...]]
breakage_if_changed: "Audit trail readability only."
```

### 14. Scenario REVERSED

```yaml
prefix: "Scenario REVERSED"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $scenario
  step: Reverse Mode Flow R4
  emits_when: user runs `$scenario reverse [scenario-research-note]`; one entry appended per previously-affected thesis
consumers:
  - skill: $sync
    step: Step 3e drift detection
    role: drift-exclusion (this entry signals a withdrawn prior propagation, not deterioration of the thesis's own conviction — it must not count toward drift)
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier (reverse mode is an append-only corrective signal with no propagatable research delta — Step 4.-1 / 5.-1 skip sector and macro re-propagation)
  - skill: audit-only (downstream readers see this as the corrective signal pairing with the original "Scenario " entry on a prior date)
example: |
  ### 2026-04-19
  - Scenario REVERSED [[Research/2026-04-17 - Scenario - China Taiwan]]: original propagation withdrawn — geopolitical signal proved transient, supply chain fears unrealized. Original "Scenario" entry on 2026-04-17 remains as historical record per Tier 2.
breakage_if_changed: "$sync drift detection would wrongly count Scenario REVERSED entries as a fresh drift signal (since they read as 'something happened to this thesis recently'), producing false ⚠️ Conviction drift warnings on theses that just had a scenario withdrawn. The whole point of reverse mode is to preserve audit trail without inflating drift; failing to exclude breaks that contract."
```

### 13. Cross-thesis closure / Cross-thesis closures

```yaml
prefix_singular: "Cross-thesis closure:"
prefix_plural: "Cross-thesis closures:"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $prune
  step: Stage 4.2b
  emits_when: a prune closure affected this thesis's cross-thesis wikilinks (appended once per neighbor thesis per prune run)
consumers:
  - skill: audit-only
  - skill: $sync
    step: Step 3e drift detection
    role: drift-exclusion (this entry does not reflect deterioration of the thesis's own conviction — it reflects an upstream neighbor's closure — so it must not count toward drift)
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier (notification-only entry about a DIFFERENT thesis's closure — the neighbor's own sector/macro state is unchanged by this Log append, so Step 4.-1 / 5.-1 skip re-propagation)
example: |
  ### 2026-04-17
  - Cross-thesis closure: [[_Archive/FOO - Foobar Inc]] archived — no catalyst identified, thin research base. Cross-thesis and Related Research wikilinks retained; review body prose if thesis impact has changed.
  - Cross-thesis closures: [[_Archive/FOO - Foobar]], [[_Archive/BAR - Barbaz]] archived this run — see $prune output. Cross-thesis wikilinks retained.
breakage_if_changed: "$sync drift detection would wrongly count $prune-triggered cross-thesis notifications as evidence against the unchanged thesis, producing false ⚠️ Conviction drift warnings on healthy theses. Plural and singular forms must both be recognized — the singular covers single-closure runs; the plural is emitted when one thesis is referenced by multiple closures in the same prune batch."
```

### 15. Renamed file:

```yaml
prefix: "Renamed file:"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $rename
  step: Step 10 (append Log entry to renamed thesis)
  emits_when: every successful $rename run (and repair re-runs that complete the outstanding wikilink edits)
consumers:
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier (rename is a filename + wikilink operation with no analytical delta — Step 4.-1 / 5.-1 skip sector and macro re-propagation for a self-modified thesis whose only recent entry is a rename record)
  - skill: $sync
    step: Step 3e drift detection
    role: drift-exclusion (rename carries no conviction sentiment; counting it would consume a drift-window slot without adding signal)
  - skill: audit-only (human-readable record of the filename evolution)
example: |
  ### 2026-04-19
  - Renamed file: "SQ - Square" → "SQ - Block". 7 inbound wikilinks rewritten across 5 files. Snapshot: [[_Archive/Snapshots/SQ - Square (pre-rename 2026-04-19-143055)]]
breakage_if_changed: "$sync Step 2.5 stops classifying post-rename theses as skill-origin → Step 4 fires on the next default sync and rewrites sector analytical text citing no actual research delta. $sync Step 3e stops excluding rename entries → drift-detection window fills with non-sentiment rename records, biasing drift signal on recently renamed theses."
```

### 16. Comparison

```yaml
prefix: "Comparison "
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $compare
  step: Phase 5.2 (per affected thesis log append)
  emits_when: $compare successfully appends Log entry to thesis
consumers:
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier ($compare Phase 5.5 already updated sector competitive-dynamics / value-chain sections and added the comparison research note to the sector's Related Research + Log — Step 4.-1 / 4.0 idempotency skip prevents silently overwriting $compare's analysis with $sync's generic re-synthesis)
  - skill: audit-only (human-readable record of cross-thesis competitive work)
example: |
  ### 2026-04-21
  - Comparison [[Research/2026-04-21 - BESI vs AMAT - Competitive Comparison]]: BESI's hybrid-bonding moat widening vs AMAT's bevel-etch position — conviction strengthened, design-win momentum confirmed
breakage_if_changed: "$sync Step 2.5 stops classifying post-$compare theses as skill-origin. Combined with $compare's sector Related Research + sector Log idempotency markers (Phase 5.5), losing this prefix causes $sync Step 4 to re-propagate the comparison research note to the same sector sections $compare just edited — silently overwriting $compare's nuanced competitive analysis with $sync's generic synthesis. The trailing space is significant — it distinguishes the prefix from prose mentions of 'comparison' and mirrors the 'Scenario ' (#10) pattern."
```

### 17. Callout sweep

```yaml
prefix: "Callout sweep:"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $archive-callouts
  step: Phase 4 (write phase — one Log entry per thesis swept per run)
  emits_when: $archive-callouts moves one or more addressed callouts into ## Legacy Callouts for a target note
consumers:
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier (sweep is a pure body-restructuring operation — addressed callouts relocate from their source sections into ## Legacy Callouts with no new analytical content. Step 4.-1 / 5.-1 skip sector and macro re-propagation to prevent $sync from rewriting downstream notes with formatting noise that carries no research delta.)
  - skill: $sync
    step: Step 3e drift detection
    role: drift-exclusion (sweep carries no conviction sentiment — counting it in the last-5-entry drift window would pollute signal on theses whose only recent activity is hygiene sweeps, producing false ⚠️ Conviction drift warnings on healthy theses)
  - skill: audit-only (human-readable record of callout archival batches — Log entry format captures sweep date, section breakdown, and safety snapshot path)
example: |
  ### 2026-04-24
  - Callout sweep: 14 addressed callouts ≥180d swept to ## Legacy Callouts. Sections touched: Bull Case (6), Catalysts (4), Industry Context (3), Risks (1). Safety snapshot: [[_Archive/Snapshots/NVDA - Nvidia (pre-callout-sweep 2026-04-24-143055)]]
breakage_if_changed: "$sync Step 2.5 stops classifying post-sweep theses as skill-origin → the first default $sync after every $archive-callouts run rewrites sector and macro notes citing no actual research delta, duplicating text already captured in the target thesis. $sync Step 3e drift detection stops excluding sweep entries → the drift window fills with hygiene-sweep bookkeeping on actively-maintained theses, biasing drift signal toward false positives on heavy callout users."
```

### 18. Numbers refresh

```yaml
prefix: "Numbers refresh:"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $numbers
  step: Step 9 (Append Log entry — runs unconditionally per refresh, including zero-material-delta runs)
  emits_when: $numbers successfully refreshes ≥1 row of the thesis ## Key Metrics table (covers single-ticker mode AND --all / --all-active batch modes — one entry per refreshed thesis)
consumers:
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier (a Key Metrics refresh is FMP-sourced numeric hygiene — no qualitative claim, no research note, no thesis-level analytical delta. Step 4.-1 / 5.-1 skip sector and macro re-propagation to prevent $sync from emitting "TICKER market cap updated" noise into sector and macro notes. Material deltas surface to the user as advisories in $numbers Step 10 — the user runs $deepen, $stress-test, or $sync manually if a metric shift warrants downstream action.)
  - skill: $sync
    step: Step 3e drift detection
    role: drift-exclusion (refresh carries no conviction sentiment — counting it in the last-5-entry drift window would pollute drift signal on actively-maintained theses where $numbers runs monthly per the recommended cadence. Without exclusion, every refresh would consume one of the five drift-window slots without adding research signal.)
  - skill: audit-only (human-readable record of refresh batches — Log entry captures count refreshed, count material, single most-significant Δ, and safety snapshot path. Snapshot enables $rollback for the rare case where a notes-column-preservation invariant trips post-write.)
example: |
  ### 2026-05-22
  - Numbers refresh: 7 metrics updated, 2 material. Revenue growth decel +65%→+42% YoY. Snapshot: [[_Archive/Snapshots/NVDA - Nvidia (pre-numbers 2026-05-22-143055)]]
breakage_if_changed: "$sync Step 2.5 stops classifying post-refresh theses as skill-origin → every $numbers run (recommended monthly cadence per $numbers SKILL.md §Recommended frequency) triggers full $sync propagation citing no actual research delta. Sector and macro notes accumulate analytical noise about market cap and EV/Revenue changes that carry no investment signal. $sync Step 3e drift detection stops excluding refresh entries → the drift window fills with monthly hygiene bookkeeping, biasing drift signal toward false positives on heavily-refreshed theses."
```

### 19. Cross-thesis signal

```yaml
prefix: "Cross-thesis signal via"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $sync
  step: Step 4b cross-thesis contradiction sweep (2026-07-09)
  emits_when: the sweep finds a peer Active Thesis whose named assumption is CONTRADICTED by the source research — $sync appends a Tier B Log-only entry on the peer pointing at §Risks/§Bear Case
consumers:
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier (the entry is machine-written propagation output, already fully handled in the run that wrote it — without this classification the NEXT $sync would read the peer's entry as manual research and re-propagate, creating a feedback loop between sector peers)
  - skill: $retro
    step: §2.3 Log classification
    role: skill-origin (machine propagation, not user conviction activity — excluded from VAULT_DIRECTION manual-signal weighting)
example: |
  ### 2026-07-09
  - Cross-thesis signal via [[Research/2026-07-09 - AMD MI400 ramp - deep-dive]]: "NVDA rack-scale monopoly through 2027" contradicted by AMD evidence — MI400 rack systems shipping to two hyperscalers in Q4. Review §Risks/§Bear Case.
breakage_if_changed: "Peer theses receiving contradiction signals get re-propagated on every subsequent $sync (feedback loop), and $retro counts machine-written bear-side appends as manual conviction activity, corrupting the alpha/reflection split."
```

### 20. Metrics synced

```yaml
prefix: "Metrics synced:"
case_sensitive: true
match_anchor: line-prefix
producer:
  skill: $deepen
  step: "MS-7.5 (Metric-Sync mode finalize — atomic replacement of 'Metrics syncing — in progress' entry)"
  emits_when: "$deepen --sync-metrics successfully applies ≥1 confirmed cluster to the thesis body"
consumers:
  - skill: $sync
    step: Step 2.5 skill-origin classification
    role: skill-origin classifier (a metric-sync pass reconciles the note's own stale figures against fresh Key Metrics data — no new qualitative claim, no research note, no thesis-level analytical delta. Same rationale as §18 Numbers refresh:.)
  - skill: $sync
    step: Step 3e drift detection
    role: drift-exclusion (reconciliation carries no conviction sentiment — counting it in the last-5-entry drift window would pollute drift signal exactly as an unexcluded Numbers refresh: would)
  - skill: audit-only (human-readable record: cluster count, location count, section count, data-source mix across Key Metrics table / FMP direct / web search, single most-significant cluster, safety snapshot path)
example: |
  ### 2026-07-15
  - Metrics synced: 1 cluster updated across 4 locations in 4 sections (0 via Key Metrics table, 4 via FMP direct). Forward P/E 30x→22x, reconciled across Summary/Insights/Questions/Risks. Snapshot: [[_Archive/Snapshots/NVDA - Nvidia (pre-deepen-metrics-sync-2026-07-15-101500)]]
breakage_if_changed: "$sync Step 2.5 stops classifying post-sync theses as skill-origin → every $deepen --sync-metrics run triggers full $sync propagation citing no actual research delta, flooding sector/macro notes with reconciliation noise carrying no investment signal. $sync Step 3e drift detection stops excluding sync entries → the drift window fills with mechanical reconciliation bookkeeping, biasing drift signal toward false positives on frequently-synced theses."
```

---

## Editing protocol

1. **Before any edit**: grep `.agents/skills/` for the prefix string. Note every occurrence in producer SKILL.md Log-append blocks AND every occurrence in consumer SKILL.md search/filter logic.
2. **Edit the prefix here first** — this file is the source of truth.
3. **Update every producer** to emit the new string.
4. **Update every consumer** to search for the new string.
5. **Run `$lint`** — check #29 verifies:
   - Every prefix in this registry appears in at least one producer SKILL.md.
   - Every prefix in this registry is found in at least one Log entry within `Theses/` (confirming producers are firing).
   - No SKILL.md contains a legacy prefix that has been renamed here.
6. **Update `last_reviewed:` frontmatter** to today's date.

## Intentionally not in this registry

These prefixes appear in vault content but are NOT contracts:
- `Deepened [Section Name]: [findings]` — the `[Section Name]` part is freeform and NOT load-bearing. Only the `Deepened` prefix matters.
- `Transcript ingested:` — **produced by `$transcript`** but deliberately **NON-skill-origin**: a transcript delta IS a research finding that must reach sector/macro notes, so `$sync` treats it like manual research and propagates normally. Do NOT add it to the skill-origin classification list (that would silently suppress transcript-driven propagation). Listed here so its omission from the skill-origin set reads as intentional, not drift.
- Any text produced by manual edits — users can write arbitrary Log entries. Consumers must tolerate unknown prefixes (treat as audit-only, not anchors/exclusions).
