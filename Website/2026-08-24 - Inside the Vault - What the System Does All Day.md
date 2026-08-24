---
date: 2026-08-24
tags:
  - essay
  - research-process
  - laniakea-partners
  - workflows
  - use-cases
status: draft
audience: general-investor
source_note:
  - "[[Website/2026-08-23 - Inside the Vault - Part 1 - Research as a Compiled Artefact]]"
  - "[[Website/2026-08-23 - Inside the Vault - Part 2 - Letting a Language Model Touch the Book]]"
  - "[[Website/2026-08-23 - Inside the Vault - Part 3 - The System That Argues Back]]"
source: internal synthesis
---

# Inside the vault: what the system does all day

**The working morning takes fifteen to forty-five minutes: read what changed overnight, feed in the two or three stories that matter, and let the propagation run.** Behind that sentence sits our in-house research book of 95 theses, 53 sector maps and 11 macro frameworks in plain markdown, maintained by a language model under a fixed schema, with every source immutable and every conviction decision reserved to us. How it is built is a separate story; this piece is about what the setup is for. The uses fall into a handful of families: staying current, feeding it evidence, asking it questions, arguing with it, setting it against our own positions, and letting it police the calendar and the tape.

## Staying current without drowning

Overnight, scheduled pipelines read about 6,800 news items across the open web and X, and compress them into a scored morning brief of a couple hundred stories, clustered by theme. Three features make the brief usable rather than merely shorter. Price tripwires fire against pre-set levels and each alert cites the thesis trigger block it threatens, so the phone shows the falsifier next to the price. Catalyst reminders arrive at T-2 and T-0 for every dated event in the book. And the X dashboard carries a thesis-divergence section that names where crowd sentiment contradicts our own positions, which is the only part of sentiment we care about; one such flag on Uber turned into a full thesis reassessment the same week. Sensing is constant and cheap, judgement stays scheduled and human: we scan the brief in minutes and go deeper only where a flag summons us.

Nothing from this layer enters the book by itself. We hand-pick the one to three stories that matter and ingest them, which is the boundary that keeps the spine curated while the sensing stays wide.

## Feeding it anything

The same intake handles a URL, a PDF, a broker note, a CSV, a video transcript or a full deep-research dump: drop it in the inbox, and it becomes a structured research note that leads with the thesis delta (what this changes for the position, never a business description) and a contradiction check (what in the book this cuts against). Propagation then fans the delta into every affected thesis, sector map and macro note in one pass, appends dated log entries, and refreshes the dependency graph. The practical effect is that reading and filing stop being separate activities; by the time we have read a source, the book already reflects it everywhere it matters.

Earnings get a dedicated version of this. A transcript pull diffs the call against the thesis within the hour: management commentary deltas, hedging shifts, tone of the Q&A, each tested against what the thesis said management would say. The output leads with what moved, and 'nothing moved' is a recorded result.

## Teaching it to think like us

Templates fix the anatomy of an argument. A new thesis arrives with its fifteen sections already asking the hard questions: each non-consensus insight must name the consensus it disputes, the observable that should confirm it and the datapoint that would falsify it; the outstanding questions are drafted as a sceptical investment committee's objections; the conviction triggers demand raise, cut and close conditions written before we hold a settled view. A sector map is born expecting industry history, competitive dynamics, product-level analysis and a section on what consensus believes and where it could be wrong. The machine cannot produce a thesis without a bear case because the bear case is a section, and since the discipline lives in the template rather than in per-note memory, changing a template once changes every note written after it. Structural identity is also what makes the book comparable at all: 95 theses with the same skeleton can be diffed, ranked and swept; 95 bespoke documents cannot.

The mental-models folder does the same for judgement. It holds the strategy's codified lenses: generalist frames such as mean-reversion versus continuation (the most expensive classification call in equity research) and price-implied expectations; industry files such as bottleneck migration and qualification-gate monopolies in semiconductors; cross-sector lenses for value-layer ownership, automation readiness, and management and culture. The model must read the relevant files before any analytical work, so the house edge is applied to every name on every pass rather than when we happen to remember it. The folder is writable in the other direction too: when we learn a new mechanism, we write it in once and it shapes everything analysed thereafter, which makes the folder the place where the strategy itself compounds. Use is governed by a reading protocol: the models are lenses and questions, never conclusions, and agreement across them is a trigger to disconfirm rather than to commit. Each thesis records which lenses fired in a section of its own, held as hypotheses to test, so a position also answers the reflexive question of which of our beliefs the trade depends on.

## Asking the book questions

Because reconciliation happens at write time, cross-sectional questions cost minutes rather than afternoons. Which theses rest on HBM supply; where a single supplier appears across the book; which positions a Taiwan disruption touches first: each is answerable because every note is structurally identical and the graph already links names to sectors, macro exposures, peers and evidence.

A set of one-command diagnostics turns this into routine practice, each read-only and each answering a question we would otherwise ask only when it was too late:

| Question | Procedure | What comes back |
|---|---|---|
| What must be true for this thesis to work? | assumptions | The load-bearing claims, each with its falsifier, plus places the thesis argues against itself |
| What does the bull case actually rest on? | dependency-map | Key customers, inputs, technology transitions and single points of failure |
| What macro bet are we secretly making? | macro-exposure | The implicit macro variables the position is levered to, with direction and size |
| Where does the company sit in its chain? | value-chain | Who it buys from and sells to, where the bottleneck and pricing power sit, whether it owns a layer |
| Is our stated conviction still earned? | conviction-audit | Whether the evidence matches the label, and whether a pre-registered trigger has fired without being actioned |
| Pitch it in one page | brief | An IC-ready memo distilled from the thesis, working state stripped |

## Arguing in the margins

Most of the book's text is machine-drafted, and the correction channel runs through the notes themselves. A hotkey drops a typed objection (question, error, suggestion, task) at the exact paragraph it concerns; the instruction 'address fresh callouts' sends the model back through them. It rewrites the relevant body section, then marks the callout addressed with our original wording preserved verbatim, a dated response, and a pointer to where the analysis now lives. The rule that keeps this honest is that the body is the deliverable and the callout is the ledger: the new table or scenario lands in the note's spine where every future procedure can see it, and the margin keeps a three-sentence record. Objections we want revisited as new data arrives can be pinned as standing slots. The use case, in short, is delegating revision without losing the argument: every disagreement we have ever had with the machine is preserved next to the claim it concerned.

## Setting it against a position

Three procedures exist to attack single names, and they are the highest-value commands in the set.

A **stress test** runs a short-seller pass over one thesis: it takes our own flagged errors as already-identified weaknesses rather than rediscovering them, and reports the idiosyncratic case against the name before the sector-wide one, so a semis-heavy book cannot let every test collapse into 'the cycle turns'. 

A **scenario** run propagates a hypothetical through the whole portfolio: a 150bp cutting cycle, a Taiwan blockade, an AI-capex pause, each traced through transmission channels to a ranked list of winners, losers and the positions whose theses need a line they currently lack. And the trigger discipline runs continuously underneath: every thesis carries pre-registered raise, cut and close conditions written before the market had an opinion, every new datapoint is mechanically diffed against them, and a finding that demands action lands in a follow-ups register that never auto-forgets; entries leave only by being resolved.

The quiet benefit is what gets written when nothing happens. 'Tested against the triggers, none fired' is logged with a date, which means a position's history is a record of survived falsification attempts rather than an accumulation of supportive clippings.

## Setting it against the whole book

Portfolio-scale sweeps fan the single-name procedures across every thesis at once: **stress-test** everything; map which bull cases secretly rest on the same variable; aggregate the implicit macro bets to find concentration dressed as diversification; stitch the supply-chain positions into one graph and find the shared points of failure; and hunt contradictions, places where one thesis's bull premise is another thesis's bear premise. Findings pass through independent verifier agents prompted to refute them before we ever see the list, so what reaches us has survived attack. One sweep found the same unexamined assumption sitting identically in five of our semiconductor theses; no analyst rereads five theses looking for a shared blind spot, but a uniform book can be diffed against itself.

These runs are report-only by default and may never touch a conviction field. The model recommends with as much force as the evidence supports; every conviction change passes through us.

These portfolio-scale sweeps can be programmed to run automatically every week or every month, surfacing outputs that allow live conviction testing against the daily news and X summaries of thesis delta.

## The calendar and the tape

The catalyst calendar extracts every dated event across the book and reads them jointly, which changes behaviour: when 34 earnings dates fall inside two weeks with 20 in a four-day window, the calendar's instruction is to treat the cluster as one correlated portfolio event rather than a series of independent reads. On Fridays a retrospective overlays everything the book did that week against price action and ranks the gaps between narrative and market reaction into candidate trades, which is where research that felt conclusive but has not been priced gets a second look. Periodically, a surfacing pass asks what we are missing (decayed theses, unanswered questions, under-attended names), and a pruning pass builds the kill list.

## What stays human

We choose the sources, drop the objections, and take every conviction decision. The machinery's job is to make our own standards cheap to obey at all times, on every name, in both directions. The compounding case for the whole setup is a list of things that no longer depend on memory or mood: evidence is filed where it changes a claim, falsifiers are tested on arrival, disagreements are preserved next to the claims they concern, and the cheapest question in the research process is now the one that used to be prohibitive: what, across everything we hold, did this morning's news actually touch?
