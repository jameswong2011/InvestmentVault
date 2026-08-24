---
date: 2026-08-23
tags:
  - essay
  - research-process
  - laniakea-partners
  - automation
  - adversarial-research
status: draft
audience: general-investor
source_note:
  - "[[Build documents/n8n Automations]]"
  - "[[Build documents/User Guide]]"
  - "[[Mental Models/Generalist - Overview]]"
  - "[[Theses/LITE - Lumentum]]"
source: internal synthesis
---

# Inside the vault: the system that argues back

*Part three of three on the research system behind Laniakea Partners. Part one covered the structure, a compiled research wiki; part two covered the machinery that lets a language model maintain it safely. This part covers what runs on top: the overnight sensing layer, the feedback loop in the margins of our own notes, and the adversarial procedures whose purpose is to attack the book they maintain.*

**By 07:30 each morning the vault has read about 6,800 news items and kept 226.** One recent brief opens with its own funnel: '6798 fetched → 3635 new → 281 admitted → 226 stories'. The reading is done by five scheduled pipelines that run before the working day, none of which involve the research book's judgement at all:

| Time | Pipeline | What it does |
|---|---|---|
| 07:00 | News sweep | Five channels (a 94-outlet feed registry, per-ticker news, GDELT, Brave, Google News), deduplicated semantically by embeddings, triaged, clustered into a scored morning brief delivered to Telegram |
| 07:30 | Catalyst reminders | Parses the catalyst calendar; alerts at T-2 and T-0; flags the calendar itself once it goes stale |
| 07:35 | Price tripwires | One batch quote call against pre-set levels; an alert cites the thesis trigger block it threatens, so the phone shows the falsifier next to the price |
| 08:00 | X canary | A four-node probe that the harvester's data source is alive before any money is spent on it |
| 08:30 | X harvester | Cashtags derived automatically from thesis frontmatter, engagement-delta detection for what is newly trending, and a sentiment dashboard with a named thesis-divergence section |

The layer is governed by one file of markdown tables listing every feed, watch level, model string and prompt; retuning the entire sensing apparatus is editing a table cell in Obsidian, with no redeploy. Running cost is $20–35 a month at current volume, around $80–145 with the full news sweep on, and the cost has its own war story: the first build spent roughly $10 a run having the strongest model score duplicate stories one at a time, and moving deduplication upstream into embeddings deleted about 95% of the bill.

The design rule for the layer took one revision to learn. The original governance line was 'triage yes, analysis no', on the theory that machine analysis did not belong anywhere near the book. In practice a stack of accurately-sorted headlines is stenography, so the rule was rewritten from a content prohibition into a boundary on write access: the pipelines may analyse as hard as they like, and their output is confined to the daily surfaces, never the book's spine. Nothing enters a thesis except through the ingestion procedure with us choosing the stories. The interesting output is tuned to disagreement: the X dashboard's divergence section names where crowd sentiment contradicts our own positions, flagging in one August case that the crowd's bull case on a memory name rested on a specific corporate out-year commitment our destock framing does not directly engage. An early-August divergence flag on Uber became a full thesis reassessment the same week. Sensing is cheap and constant; judgement is scarce and human-scheduled; the divergence flags are where the first is allowed to summon the second.

## The analyst argues with the machine

Most of the book's text is machine-drafted, and the correction channel runs through the notes themselves. Four typed callouts (question, error, tip, todo), each on a hotkey, can be dropped inline at the exact paragraph they concern: an objection to a claim, a request to test something, a flagged mistake. The instruction 'address fresh callouts' sends the model back through them; it rewrites the relevant body section, then marks the callout addressed, preserving our original wording verbatim with a dated response. From the Lumentum thesis, in full lifecycle:

> **[!question] 2026-04-28 → Addressed 2026-04-28**
> **Prompt:** *What are the equipment suppliers that go into constructing an InP site like Greensboro. Are any of them listed. What is the equivalent exposure to CPO from an equipment vendor perspective.*
> **Response:** The InP fab chokepoint is MOCVD epitaxy — Aixtron and Veeco are the listed duopoly. Full equipment-stack table with ten tool categories and listed suppliers in §Industry Context → Equipment Supply Chain.

The formatting contract encodes a principle: the body is the deliverable and the callout is the ledger. The analysis (here, a ten-row supplier table) lands in the note's spine where every future procedure can see it; the callout keeps a three-sentence record and a pointer. A response longer than three sentences is treated as a smell that the integration did not happen. Addressed callouts are swept to an archive section after 180 days unless pinned as standing revisit slots, and the exchange history has diagnostic value of its own: four error callouts on one name in a month reads as conviction drift, whatever the frontmatter still says.

## The machine argues with itself

Before any analytical work, the model is required to read a folder of mental models: the accumulated lenses of the strategy, from bottleneck migration in semiconductors (logic wafers in 2021, advanced packaging in 2024, HBM in 2026–27) and qualification-gate monopolies hidden behind share data, to mean-reversion-versus-continuation classification, which our generalist file calls the single most expensive equity research mistake, to reverse-engineering the expectations already embedded in a price. The folder opens with a reading protocol whose first line is the point: a checklist of lenses and questions, never a source of conclusions. Claims are hypotheses to test against current evidence, the outside view runs adversarially against the other models, and the load-bearing rule inverts the natural instinct: agreement across models is a trigger to disconfirm, not to commit. When every lens likes the same name, that is the cue to hunt the bear case and the single falsifying datapoint hardest.

The protocol leaves fingerprints in the book. Every thesis carries a self-populating Mental Models section recording which lenses fired, held as hypotheses rather than verdicts (a health check polices the framing), and the SK Hynix note closes its own section by running the outside view against everything above it: memory names at all-time-high share prices, all-time-high margins and all-time-high capex have never sustained all three through the following 24 months. That sentence sits inside a thesis we hold, put there by the process that maintains the position.

## The machine argues with the book

A set of procedures exists purely to attack. `/stress-test` runs a short-seller pass on a single thesis, and its design details show the intent: it reads our own error callouts first as already-identified weaknesses rather than re-deriving them, caps its evidence reads to the most recent and risk-flagged material so it cannot drown in friendly context, and reports idiosyncratic risk before cluster-wide risk, a rule that exists because a semis-heavy book will otherwise let every stress test collapse into 'the cycle turns'. `/conviction-audit` asks the quieter question: not whether the thesis is wrong, but whether one of its own pre-registered triggers has already fired without being actioned. Between audits, a shared mechanism diffs every new datapoint against the trigger blocks mechanically; most Log entries record no contact, and one August entry reads, in full, '⚡ Trigger hit: none fired. Flag-only.'

Findings that demand action get a register that refuses to forget. The follow-ups file never auto-evicts, a property it owes to a specific failure: a stress-test conclusion recommending a downgrade on Intuit was evicted from the session cache by that file's own compression contract before anyone actioned it. Findings now live in the register until explicitly resolved; six stress-test flags from mid-August currently sit open in it, each naming the conviction change it is waiting on. The catalyst calendar audits the book from another angle. July's run counted 34 thesis earnings dates inside 14 days, 20 of them across four days, and instructed us to treat the window as one correlated portfolio event rather than eight independent reads; the same run found 30 of the book's then-82 theses carried no conviction triggers at all, and named that, in its own words, the book's single largest falsification-machinery gap. The calendar's job is dates; it reported a philosophy violation, because the schema makes the absence countable.

## The book argues with the book

The heaviest artillery is a set of eight portfolio-scale workflows that fan a single-name procedure across every thesis at once: portfolio-wide stress testing, hidden-correlation mapping (which bull cases secretly rest on the same variable), implicit macro-bet aggregation, supply-chain single points of failure, and a coherence audit called vault-contradictions that searches for places where one thesis's bull premise is another thesis's bear premise. The orchestration pattern is the same throughout: read-only analysis agents fan out one per thesis, findings pass through up to three independent verifier agents each prompted to refute them (a majority refutation demotes the finding), and anything that survives is written by a single sequential writer. The workflows run report-only by default, persist only on explicit instruction, and may never touch a conviction field regardless.

The verification stage earns its cost. Plausible-but-wrong is the characteristic output of a capable model, and a finding that survives three attempts at refutation is a different grade of finding from one that merely sounded right. The coherence audit's verifier asks specifically whether a detected clash is a real contradiction or two theses framing the same fact differently, which is most of them. When the sweeps work, they work at a scale no analyst reproduces: one July pass found the same unexamined assumption about EDA-software moats sitting identically in our TSMC, Intel, Broadcom, Nvidia and Arm theses. One finding, five corrections, and a class of groupthink made visible because the book is uniform enough to be diffed against itself.

## What is left for us

The human day this produces is short and concentrated. The pipelines run unattended from 07:00; the morning takes fifteen to forty-five minutes: read the session cache, scan the brief and the divergence flags, ingest the one to three stories that matter, propagate. Earnings days add a transcript pull that diffs management's language against the thesis. Friday is the weekly retrospective, which overlays everything the book did against price action and ranks the gaps between narrative and market reaction. Sunday evening the calendar and the health checks run themselves and file their reports. We choose sources, drop objections in the margins, and take every conviction decision; the machine holds the memory, the reconciliation and the standing instruction to disagree.

Four months in, the ledger reads 115 commits, 95 theses, 543 snapshots and 152 research notes this month, but the number that matters is not in the counts. It is the behaviour the system exhibits under agreement. In *How Laniakea Partners Invests* we wrote that a differentiated view must never become an identity; the vault is that sentence built as infrastructure, down to the closing instruction of the mental-models file the machine reads before every analysis: if every model above agreed, argue the other side once more.
