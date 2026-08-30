---
publish: false
date: 2026-08-29
tags: [research, daily-intel-triage, news, NVDA, NBIS]
sector: Compute Accelerators
ticker: NVDA
source: 'https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-denies-pausing-ai-cloud-commitments-initiative-after-reported-partner-backlash-report-claims-company-told-cloud-providers-it-could-only-lease-its-gpus-to-nvidia-approved-customers'
propagated_to: [NVDA, NBIS, CRWV]
source_type: news
---

# Nvidia Denies Pausing AI Cloud Commitments Initiative After Reported Partner Backlash Report Claims Company Told Cloud Providers It Could Only Lease GPUs to Nvidia-Approved Customers

## Thesis Delta
Consensus, working off the Wall Street Journal, briefly priced a pause in some Nvidia 'take or pay' AI Compute Partnership transactions less than two months after the early-July launch, on partner irritation at tenant steering and internal antitrust worry. Nvidia's on-record reply to Tom's Hardware is that the July model 'is still in place and continues to evolve due to high demand', so the take-or-pay / revenue-share structure and the $36B of typically six-year commitments as of 26 Jul 2026 remain the operating fact; tenant-approval optics stay a governance risk for neoclouds ([[Theses/NBIS - Nebius Group]], [[Theses/CRWV - CoreWeave]]) without changing conviction.

## Summary
Nvidia on Friday denied a WSJ report that it had put some transactions under the recently introduced 'take or pay' AI Compute Partnership on hold, less than two months after unveiling the initiative in early July and days before detailing it on the earnings call, with the pause attributed to partners irritated at Nvidia's attempts to influence their operations and to internal concern about potential antitrust scrutiny. A spokesperson told Tom's Hardware that 'the new business model we introduced in July that opens up compute access to the fast-growing AI ecosystem is still in place and continues to evolve due to high demand'; Tom's itself records that the underlying report does not establish abandonment of the programme (Nvidia committed to rent capacity of newly built AI data centres and their minimum revenue) and only claims that some deals were placed on hold, while the denial is that the programme continues to exist but is evolving, which means changing. Per the WSJ account as relayed, Nvidia told some participating cloud providers they could lease its GPUs only to Nvidia-approved customers and preferred to spread available capacity across multiple smaller AI companies instead of letting a single large customer take most or all of it; some operators pushed back, arguing they should retain control over which customers they serve, and that friction is the alleged reason some deals were paused. Nvidia does not lend money or directly finance data-centre buildouts (the circular-financing reading the article explicitly rejects), it provides demand commitments and guaranteed revenue levels, and those guarantees, not cash advances, are what Tom's says may have raised internal antitrust worry and could lead Nvidia to revise terms it inks with partners.

Modern AI data centres cost billions on premises, infrastructure, and compute hardware well before an operator has enough customer contracts to finance the buildout, and banks or infrastructure investors want confidence that enough future facility capacity will actually be rented; under the programme Nvidia uses its own demand commitment on a portion of the facility's capacity in exchange for a percentage of the facility's revenue if demand is strong, so from the lender's perspective part of the project's revenue stream is supported by Nvidia rather than depending entirely on the operator finding customers. Colette Kress, Nvidia's CFO, described the mechanism on the earnings call as a take-or-pay commitment on a portion of capacity, a minimum revenue guarantee that gives lenders confidence to underwrite the project, and in exchange a share of the NeoCloud's revenue earned above that floor, so Nvidia 'get[s] paid twice, once on the hardware sale, and again through the share of rental revenue, a highly recurring stream layered on top of a one-time equipment purchase.' Actual percentages and economic terms remain undisclosed; Tom's walks a stylised six-year case in which Nvidia commits to rent, say, 30% of a new facility: if the site rents 80% and clears the floor, Nvidia does not absorb the guaranteed capacity and instead takes a percentage of excess revenue, and if the site rents only 20%, the take-or-pay obligation requires Nvidia to cover the difference between actual and contracted minimum per the agreement, or to rent back unused compute for its own needs and cover that same gap. As of late July, weeks after the formal announcement, Nvidia had committed $36B in these new six-year agreements; the SEC filing language is that commitments, typically six years in duration, totalled $36B as of 26 Jul 2026, and because Nvidia has not disclosed which portions of monetizable capacity it typically commits, the hardware value sitting under that $36B cannot be reverse-engineered.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Report date / claim | Friday denial of WSJ: some ACP 'take or pay' transactions on hold, <2 months after early-July launch | [web: tomshardware.com / WSJ] |
| Nvidia response | July model 'still in place and continues to evolve due to high demand' | [web: tomshardware.com] |
| Programme status per Tom's | WSJ does not establish abandonment; denial = exists but evolving | [web: tomshardware.com] |
| Tenant-control claim | Lease GPUs only to Nvidia-approved customers; prefer spread across smaller AI firms vs one large offtaker | [1×: WSJ via Tom's] |
| Partner response | Some operators pushed back, want control of who they serve | [1×: WSJ via Tom's] |
| Financing form | Demand commitments + guaranteed revenue; not cash lending / not circular financing | [web: tomshardware.com] |
| Antitrust / terms | Internal antitrust worry; Nvidia may revise partner terms | [1×: WSJ via Tom's] |
| Mechanism (Kress) | Take-or-pay on a portion of capacity + min revenue guarantee; share of NeoCloud revenue above floor; paid twice (hardware + rental share) | [web: tomshardware.com / transcript] |
| Stylised economics | Example: 30% committed, 6-year tenor; 80% utilisation = no absorb + upside share; 20% utilisation = cover floor gap or rent-back | [web: tomshardware.com] |
| Commitments | $36B as of 26 Jul 2026; typically six-year tenor | [1×: Nvidia SEC via Tom's] |
| Undisclosed | % of monetizable capacity committed; cannot back out hardware value under $36B | [web: tomshardware.com] |

## Contradiction Check
**Supports** [[Theses/NVDA - Nvidia]] §Risks #11 (third-party AI infrastructure financing cycle) and the demand-commitment flywheel if the Friday denial holds: $36B of typically six-year take-or-pay / revenue-share commitments remain outstanding, and Kress's 'paid twice' structure is still the stated model rather than a shelved experiment. **Raises a risk flag, does not change conviction**, for [[Theses/NBIS - Nebius Group]] insight #5 (funding quality vs [[Theses/CRWV - CoreWeave]] GPU-collateralized debt) and [[Theses/CRWV - CoreWeave]] insight #3 (NVIDIA vendor financing dressed as strategic validation): even with the programme intact, a tenant-approval clause that lets Nvidia steer who can rent the GPUs limits independent offtake and extends CUDA/channel control (Industry Semiconductors #2(iii) design lock-in; #10 second-order anchor) into the neocloud's customer book. Generalist [G-4] reads the take-or-pay floor as financial capital underwriting the frenzy build, so a real pause would have been a Perez turning-point signal; the denial keeps the frenzy-funding read in place until a named-deal halt or a 10-Q cut to the $36B stock. [[Theses/NVDA - Nvidia]] has no `## Conviction Triggers` to touch; [[Theses/NBIS - Nebius Group]] `→ CLOSE if` (capex gap funded primarily via GPU-collateralized debt) is not fired by a denied pause. Pair with same-day tape [[Research/2026-08-29 - NBIS CRWV IREN - Neocloud Tape on Nvidia ACP Pause Report - news]]. No conviction or status change.

## Source Excerpts
> "The new business model we introduced in July that opens up compute access to the fast-growing AI ecosystem is still in place and continues to evolve due to high demand." — Nvidia spokesperson [web: tomshardware.com]

> "Nvidia provides a take-or-pay commitment on a portion of the facility's capacity, a minimum revenue guarantee that gives lenders the confidence to underwrite the project, and in exchange, we share in a portion of the NeoCloud's revenue earned above that floor." — Colette Kress, Nvidia CFO [web: tomshardware.com / transcript]

> "In this model, we get paid twice, once on the hardware sale, and again through the share of rental revenue, a highly recurring stream layered on top of a one-time equipment purchase." — Colette Kress [web: tomshardware.com / transcript]

> "Our commitments, which are typically six years in duration, totaled $36 billion as of July 26, 2026." [1×: Nvidia SEC via Tom's]
