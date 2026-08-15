---
publish: false
date: 2026-08-13
tags: [research, neocloud, ai-compute, NBIS, CRWV]
sector: Neoclouds & GPU-as-a-Service
source: 'https://degentradingdaily.substack.com/p/the-economics-of-a-neocloud-5-jul'
source_type: deep-dive
propagated_to: [NBIS, CRWV, SPCX, NVDA, META, IREN]
---

# Economics of a Neocloud — Unit Model (degentrading)

## Thesis Delta

Consensus reads the neocloud land-grab — xAI–[[Theses/SPCX - SpaceX]]–Google, [[Theses/META - Meta]] selling excess compute, SoftBank's 10GW US plan — as proof the business itself mints cash, and the source's real Google–SpaceX $920M/month deal for ~110k NVDA GB200s (Colossus 2) implies a sub-2-year datacenter payback that appears to confirm it. Re-anchored to wholesale rates, the source's own numbers imply the opposite: the neocloud is a LAYER-RENTER whose payback is set by what [[Theses/NVDA - Nvidia]] charges for the layer below (the author concedes Rubin capex ~2× Blackwell) and rests on a shortage-vintage ~$11.6/GPU-hr rate he himself calls "remarkably generous" — so the durable surplus accrues to the layer owner, not the renter [[Theses/NBIS - Nebius Group]] / [[Theses/CRWV - CoreWeave]].

## Summary

Constructing a datacenter and selling compute is "the best business right now" because compute is severely supply-constrained, paybacks are fast, and hyperscalers prepay for availability. The mechanism, via the Colossus 2 worked example: Google pays SpaceX $920M/month for ~110,000 GB200 NVL72 GPUs plus CPUs and memory — a fully-furnished datacenter — implying ~$11.6/GPU-hour ($920M ÷ 110k ÷ 720 hrs). Dropped onto a fictitious 100MW GB200 buildout (~$5B capex at an assumed ~$50B/GW; ~83,333 GPUs at ~1.2kW each), that rate grosses ~$8.5B/year against only ~$1.29M/MW/year of electricity, maintenance, and staffing — payback under one year. The author immediately discounts the headline: the SpaceX rate was "remarkably generous" (Google faced a shortage; SpaceX had Colossus 1↔2 interconnect problems and retained the right to reclaim the lease), and on a "normal" ~$6/hour the payback stretches to ~2 years. He pegs long-term neocloud→hyperscaler wholesale deals near ~$4/hour while hyperscalers re-monetize at $12+/hour (AWS). The bull kicker is depreciation: A100s (2020 launch) still rent at $1–2/hour, so he endorses Gavin Baker's ~10-year GPU-life view as agentic and inference workloads absorb the older fleet. Conclusion: a neocloud's value equals the NPV of every compute deal it can sign, and the three levers that decide it are financing, the depreciation schedule, and execution.

Scope this appropriately. This is a short (~760-word), informal Substack walkthrough by degentrading — a single-author back-of-envelope built on one anchor deal and round-number capex/opex assumptions ($50B/GW, ~$1.29M/MW/year opex), not an institutional model. Its arithmetic is directional, and the author flags his own headline as an outlier; treat the figures as a sanity-check on magnitude, not as precise inputs. The value it adds to the vault is a clean, self-consistent unit model that the reader can re-anchor to wholesale rates.

## Evidence

| Item | Figure | Provenance |
|---|---|---|
| Google → SpaceX compute deal | $920M/month for compute at xAI datacenters (Colossus 2); announced 5 Jun 2026 | `[web: cnbc]` (author links CNBC) |
| Hardware in deal | ~110,000 NVDA GB200 NVL72 GPUs + CPUs/memory (fully-furnished DC) | `[web: cnbc]` / `[web: degentradingdaily]` |
| Implied rental rate | $920M ÷ 110,000 ÷ 720 hrs ≈ **$11.6/GPU-hour** | `[est.]` (author derivation) |
| Buildout capex | ~$50B/GW (GB200) → 100MW ≈ $5B; GB300 compute +20%; Jensen "$100B/GW realistic" as Rubin compute ~2× Blackwell | `[web: degentradingdaily]` / `[est.]` |
| Power → GPU count | GB200 draws ~1,200W → 100MW ≈ 83,333 GPUs | `[est.]` |
| Fictitious 100MW revenue @ $11.6/hr | 83,333 × 11.6 × 8,760 ≈ **$8,467M/year** | `[est.]` |
| Operating cost | $0.74M/MW/yr electricity + $0.25M/MW/yr maintenance + $0.30M/MW/yr staffing ≈ **$1.29M/MW/yr** | `[1×: degentrading]` |
| Payback (generous $11.6/hr) | **< 1 year** | `[est.]` |
| Payback (normalized ~$6/hr) | **~2 years** | `[est.]` |
| Wholesale vs retail stack | neocloud→hyperscaler ~**$4/hr**; hyperscaler→end-user **$12+/hr** (AWS) | `[1×: degentrading]` / `[est.]` |
| Depreciation evidence | A100 (2020) still rents $1–2/hr (was ~$3 in 2021); hyperscalers rent A100 at $2–3.5/hr | `[web: degentradingdaily]` |
| GPU useful life | ~10 years (Gavin Baker; author concurs, citing agentic/inference demand) | `[1×: degentrading]` (attributed to Baker) |
| Frontier-lab economics | Anthropic >70% gross margin serving inference; labs could turn cash-flow-positive if they chose | `[1×: degentrading]` |

## Contradiction Check

Read `Theses/NBIS - Nebius Group.md` and `Theses/CRWV - CoreWeave.md`. The "neocloud = layer-renter to NVDA" framing **supports** both theses; it does not challenge them — and this source is already inside the vault's audit trail.

- **NBIS Insight #6 + §Mental Models (VLM layer-renter / [G-7] ROIIC):** NBIS is explicitly "the **layer-renter** [that] carries the depreciation" while "NVIDIA, the layer owner, harvests the Rubin value gap through its memory markup." The source's own concession that "Rubin will be twice as much as Blackwell" is the exact mechanism by which the layer owner resets the capex base and re-captures surplus — corroborating, not contradicting, Insight #6's perceived-vs-real-ROIC decoupling. This maps to **Value-Layer-Monopoly §2** (margin hostage to the layer below; the owner of the scarce complementary asset captures the surplus) and to **Generalist [G-7]**: the source's payback is a cash proxy for ROIIC, but whether the incremental GW clears the ~15% hurdle is hostage to the rental multiple, exactly as NBIS's rate-sensitivity model quantifies (~14% at 1.5× → ~39% at 3.0×; [[Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive]]).
- **Already reconciled — this note formalizes an existing citation.** NBIS Log 2026-08-05 (Addendum 5) audited *this exact source*: the 1–2.5yr payback "reconciles fully" with the bearish arithmetic because the bull headline anchors on the $11.6/hr "retail outlier the note itself calls remarkably generous" (plus an unbuildable 83K-GPU/100MW TDP density) at Blackwell-vintage capex on a cash metric; the note's **own** ~$4/hr wholesale + **own** Rubin-2× concession reproduce the bear case, and NBIS's guided ~$2–3.15/hr wholesale sits in the vault's held band. So this is an **additional worked example / audit-trail record**, not a new thesis — it overlaps [[Research/2026-06-03 - Neoclouds NBIS vs CRWV - deep-dive]] and [[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]].
- **CRWV §Mental Models + Insight #2:** the thesis already carries the identical verdict — "CRWV rents the layer below (NVIDIA allocation + silicon)… the durable layers in this stack are NVIDIA's and the grid's." The source's closing frame — value = NPV of compute deals; levers = **financing, depreciation, execution** — maps precisely onto the vault's split: CRWV = the credit/financing bet (Insight #2 DDTL, Outstanding Q#7), NBIS = the execution bet, both hostage to the depreciation schedule (CRWV Outstanding Q#6). The source agrees these three levers dominate.
- **Automation & AI-Readiness Lens B:** the neocloud is the compute infrastructure others rent to run automation — the "indirect exposure" adjacency. Per Lens B, durable value accrues to whoever owns the scarce complementary asset (NVIDIA silicon, grid power), not to the thin reseller that owns no semantic/execution layer — reinforcing why the neocloud sits a rung below the layer owner.
- **The one genuine tension (emphasis, not arithmetic):** the source's headline — "current compute markets are pricing a severe shortage… anyone that tells you otherwise is covering their eyes" — cuts against the vault's cyclically-aware caution (H100 spot already −50–70% from peaks per CRWV Insight #2; [[Macro & Technology/Sustainability of AI Capex]] places CRWV in the fragile leveraged-merchant tranche; miner-pivots like [[Theses/IREN - IREN Limited]] compete the rate down). But the disagreement is over shortage-*permanence*, not the unit math — the author's own normalized $4–6/hr already lands inside the vault's held band. Net: this source raises no new contradiction and adds a clean unit model for [[Sectors/Neoclouds & GPU-as-a-Service]].

## Source Excerpts

> "Again, a neocloud's valuation should be the summation of the NPV of all the compute deals that it can do. **Hence the ability to obtain financing, the exact depreciation schedule and the ability to execute are the 3 most important levers impacting it.**"

> "This is where i would come in and say that the Space X deal was **remarkably generous.** Was Google facing a massive compute shortage?"
