---
date: 2026-08-21
tags: [research, quantum, Macro]
sector: 'quantum / Macro'
source: 'https://superpositionv.substack.com/p/beyond-qubits-part-1-qubit-count'
source_type: deep-dive
title: 'Qubit Count Is Not Compute'
publication: Superposition
gmail_id: 1a024125d8a21caf
---

# Qubit Count Is Not Compute

## Thesis Delta

Consensus in listed quantum names still prices the next physical-qubit or logical-qubit headline as if hardware inventory were compute, and as if compute were a cash-flow. Superposition Part 1 implies the market has the wrong unit of analysis: the priced variable is scale; the operating variable that can actually move a return is conversion along a named stack (hardware scale → reliable compute → executable workload → task-level quantum advantage → end-to-end competitive utility → workflow value → commercial capture → provider value capture → economic value), with verification integrity overlaid on every arrow and capital runway constraining the whole map. No vault thesis exists for IONQ, RGTI, QBTS or any other quantum name (grep of `Theses/` and `Macro & Technology/` is empty on those strings); the live Holdings table has none of them. The key question this raises, not a fake ticker: whether we open a Macro quantum watch-file on this conversion stack before any name-level thesis, and whether the moving classical frontier (GPUs, tensor networks, domain solvers) is the competitor the AI-compute book already owns. Conviction and status are untouched because there is no quantum thesis to touch.

Mental-model triggers identified for a later `/sync` (ingest does not write thesis/sector bodies): Generalist [G-4] Perez irruption/pre-chasm (public QC names priced as if the S-curve is secured; this source treats conversion failure as still binary); Generalist [G-10] base rates (DARPA QBI still asking in 2026 whether any architecture reaches utility-scale by 2033 is the outside-view date); Generalist [G-13] expectations investing (price-implied operating variable on listed QC is qubit-count trajectory; Superposition isolates conversion, classical-baseline quality, and financed de-risking); Generalist [G-6]/[G-7] value capture × capital runway (a $10m customer save with $1m captured revenue and $2m delivery cost is the ROIIC failure mode; burn is the time the physics is allowed). Value Layer Monopoly does not fire: quantum compute is not yet a layer anyone must pay to traverse.

## Summary

Superposition's Part 1 of *Beyond Qubits* is a framework essay, not a company report. The load-bearing claim is that qubit count measures one dimension of hardware scale and does not tell you how much reliable computation a machine can complete. Two machines, 10,000 noisy physical qubits versus 500 better-controlled qubits that sustain a deeper and more accurate workload, cannot be ranked by inventory. Even after ranking compute, the investor still has to ask whether the computation beats the best classical alternative, whether the advantage survives the full workflow, whether a customer will pay, whether the provider captures the value, and whether the firm reaches that point before the capital roadmap runs out. The governing structure is conversion, not inventory. Two layers sit across the entire chain rather than at the end of it: verification (whether each claimed conversion is real) and capital (whether the company survives long enough to reach the next layer).

Physical and logical qubits sit on different layers of that conversion. A physical qubit is a hardware resource; in an error-corrected machine many physical resources exist to detect syndromes, route, and protect logical information rather than to hold the user's state. Logical-qubit count is a better milestone than raw physical count, and it is still not utility. Creating a logical qubit, showing that it becomes more reliable as error correction strengthens, performing useful logical operations at low enough error, and executing a large application with those operations are four different facts. The non-interchangeable sequence is physical qubit count ≠ logical qubit demonstration ≠ scalable logical error suppression ≠ useful logical computation. Error correction converts extra physical resources into reliability only if the physical operations sit below the relevant threshold and stronger codes then reduce logical error. A bigger error-corrected system should become more reliable, not merely bigger. Google Quantum AI's Willow surface-code experiments are the worked example: below-threshold logical-memory scaling, a distance-7 memory on 101 physical qubits, lifetime 2.4 ± 0.3 times the best constituent physical qubit. That is the mechanism error correction is supposed to provide. It does not demonstrate a large fault-tolerant application or commercial-scale logical algorithms. The Nature paper itself flags remaining resource requirements and rare correlated error events. The correct read is a piece of the scaling mechanism, not a solved FTQC stack.

No single number replaces qubit count. Component metrics (gate fidelity, measurement error, gate speed, coherence, physical count) and system metrics (usable width, executable depth, connectivity, throughput, stability, uptime) are inputs. The object of analysis is whether the system completes the required workload at the required accuracy, and at what time-to-solution, which includes compilation, repeated shots, mitigation or correction, classical communication, parameter optimisation, and post-processing. A 50-qubit circuit of depth 100 and a 5-qubit circuit of depth 1,000 place different demands on a machine; connectivity can force the compiler to insert routing, so physical execution is more expensive than the abstract circuit. The measurement hierarchy is component metrics → system benchmarks → application-oriented benchmarks → actual workload → customer workflow. QED-C's application-oriented suite (result quality, total execution time, gate resources; later linear systems, variational simulations, ML classification, with explicit quality-versus-runtime trade-offs) is an improvement over a single component metric and is still not a customer production workload. Microsoft's Quantum Resource Estimator (application model, hardware architecture, QEC assumptions, factory model, error budget → physical-qubit requirement, runtime, accumulated error, Pareto qubit-versus-runtime) is a planning tool under specified assumptions, not a hardware benchmark. resource estimate ≠ hardware demonstration ≠ application advantage. A real fault-tolerant application consumes space, time, error budget, decoding resources, and sometimes expensive logical-operation resources such as magic-state factories; logical-qubit count alone is not enough.

Compute is not advantage. The competitor is the best practical classical stack at the date useful quantum hardware arrives (CPUs, GPUs, supercomputers, tensor networks, specialised numerical methods, AI models, heuristics, domain solvers), not a ten-year-old CPU and not an unoptimised baseline. Candidate application areas (chemistry, materials, many-body simulation, cryptography, certain optimisation problems) are not established commercial quantum-advantage markets. In drug discovery the defensible claim is an improvement to particular molecular or electronic-structure calculations inside a larger discovery workflow, not 'discovering drugs'. DARPA US2QC states that for many proposed applications a rigorous comparison against those classical alternatives for real-world use has not been completed. The classical frontier moves: an algorithm that once looked unreachable can become tractable after a better approximation, solver, GPU implementation, or mathematical technique. Task-level advantage (a kernel, sampling problem, simulation step, subroutine) can be scientifically real and still vanish in the surrounding costs of data preparation, encoding, compilation, repeated execution, measurement, error management, classical optimisation, post-processing, verification, and software integration. A 100× speedup on a portion that is 1% of wall-clock barely moves the workflow. End-to-end competitive utility asks whether the complete quantum-enabled workflow beats the complete classical workflow on an explicitly stated dimension: time-to-solution, cost-to-solution, accuracy, tractable problem size, energy, or access to a previously impractical result.

Workflow utility is still not economic utility. A pharmaceutical buyer wants better decisions about which molecules to test; a materials buyer wants better candidates, fewer failed experiments, shorter development cycles, or properties that were previously too costly to calculate. DARPA's Quantum Benchmarking Initiative defines utility-scale operation as a quantum system whose computational value exceeds its cost, and in 2026 DARPA continues to evaluate whether any architecture can reach that standard by 2033. The latest Stage A FAQ says computational value will generally be measured in dollars. DARPA's machine-cost calculation does not include R&D expenditure, so three statements are not equivalent: (1) customer computational value exceeds machine cost; (2) the provider earns attractive unit economics; (3) shareholders earn attractive returns after R&D, capex, dilution, and time. The first can be true while the third is false. Worked capture failure: a workload that saves the customer $10 million, with the provider capturing $1 million of revenue and spending $2 million to deliver. Business models (hardware sales, cloud access, government contracts, paid PoCs, software/IP licence, vertically integrated service) matter only insofar as experimentation progresses toward repeated economic dependence. The commercial sequence to watch is research relationship → paid proof of concept → repeated usage → production workflow → renewal or expansion. A paid PoC funds experimentation; it does not prove the product belongs permanently in the workflow. Backlog quality is the company's definition, cancellation rights, delivery conditions, timing, and conversion probability, not headline size.

Capital is a constraint across the roadmap, not the last step in the causal stack. Architectures consume different engineering stacks: superconducting (cryogenic infrastructure, fabrication, packaging, control electronics); trapped-ion and neutral-atom (optical, laser, vacuum, and control systems); photonic (sources, switching, detectors, manufacturing, packaging, integration). The investment principle does not change with the modality: a technically plausible roadmap is useful only if the company can finance it. The repeated questions are the next milestone that materially reduces technical risk, the capital required to reach it, and whether the firm can reach it before the next raise. A company that can demonstrate a major de-risking event before its next financing occupies a different position from one that must raise billions before validating its key technical assumption. Cash burn, in this industry, is the time the physics is allowed. Verification is an evidence overlay, not a product layer: for every arrow, what evidence proves the conversion occurred, on real hardware, against a current classical baseline, with disclosed assumptions, uncertainty, and a method that independent parties can audit. DARPA QBI is structured around independent verification and validation of proposed paths to utility-scale quantum computing. Four investor questions collapse the stack: (1) Workload Capability, (2) Competitive Utility, (3) Commercial Conversion, (4) Financed Roadmap, all under a Verification Integrity evidence rule. The largest number in the stack does not determine the value of the system; the weakest conversion can. The first investor question is therefore not how many qubits the machine has. The sequence is: what reliable computation those qubits actually perform; whether that computation retains an advantage against the best classical alternative; whether that advantage matters in a real customer workflow; whether the company can capture the resulting value before the roadmap consumes too much capital. Part 2's hook: a better quantum computer does not prove that a problem needs a quantum computer (the quantum-ML distinction).

## Framework / Mental Model

### Conversion Chain (named): hardware scale → economic value

Superposition names the industry as a conversion chain rather than an inventory problem. Every arrow is a conversion that can fail. Two layers sit *across* the chain rather than as extra steps in it.

| Stage | What converts | What 'done' looks like | Typical false substitute |
|---|---|---|---|
| Hardware scale | Physical devices, control, packaging | Controlled, usable resources | Headline physical-qubit count |
| Reliable compute | Error rates, QEC, calibration, uptime | Work that completes at required accuracy | Logical-qubit count without suppression |
| Executable workload | Width, depth, connectivity, compiler, shots | A specified problem run end-to-end on hardware | Component benchmark or simulator result |
| Task-level quantum advantage | Quantum subroutine vs a classical method | Outperformance on a carefully defined task | Weak or outdated classical baseline |
| End-to-end competitive utility | Full workflow including overhead | Complete quantum-enabled workflow beats complete classical workflow on a stated dimension | Subroutine speedup that is 1% of wall-clock |
| Workflow value | Bottleneck the customer actually pays to remove | Better molecule decisions, better materials candidates, shorter cycles | More gates / larger circuits |
| Commercial capture | Willingness to pay → contracted revenue | Repeated usage, renewal, expansion | Paid PoC; headline backlog |
| Provider value capture | Price, cost-to-serve, mix | Attractive unit economics after delivery cost | Customer value created but not captured |
| Economic value | After R&D, capex, dilution, time | Shareholder returns | DARPA machine-utility (ex-R&D) |

**Cross-cutting layer 1, Evidence overlay → verification integrity.** For every arrow: was the result produced on real hardware; what assumptions; experimental result vs simulation vs resource estimate; uncertainty and methodology disclosed; classical comparison current; independent parties able to reproduce, validate, or audit. DARPA QBI is the external IV&V template.

**Cross-cutting layer 2, Capital constraint → runway to the next de-risking milestone.** Map the technical roadmap onto the financing roadmap. What has to be demonstrated next; equipment, manufacturing, infrastructure, people; cash consumed; next financing date; dilution before the key technical uncertainty is removed. A roadmap that cannot be financed is not an investable roadmap.

### Nested non-equivalence ladders

These are the category errors the chain is built to prevent. They are not interchangeable progress markers.

| Ladder | Sequence |
|---|---|
| Logical-layer | physical qubit count ≠ logical qubit demonstration ≠ scalable logical error suppression ≠ useful logical computation |
| Measurement hierarchy | component metrics → system benchmarks → application-oriented benchmarks → actual workload → customer workflow |
| Gate-to-customer | gate metric → system capability → application-oriented benchmark → end-to-end workload → customer workflow |
| Estimate vs evidence | resource estimate ≠ hardware demonstration ≠ application advantage |
| Commercial | research relationship → paid PoC → repeated usage → production workflow → renewal or expansion |
| Capture | workflow utility → willingness to pay → commercial conversion → provider value capture → economic value |
| DARPA vs shareholders | customer computational value > machine cost ≠ provider unit economics ≠ shareholder returns after R&D / capex / dilution / time |

### Four investor questions (evaluation protocol)

Methodology: score a company on the four questions, then haircut every score by the Evidence Rule. Do not start with total qubit count.

| # | Question | What to look for | What not to start with |
|---|---|---|---|
| 1 | **Workload Capability.** Can the system complete harder and more valuable workloads on real hardware at the required accuracy? | Rising executable capability; more of the system used effectively; greater width and depth sustained; improving error rates; if pursuing FT, stronger QEC actually reducing logical error | Total qubit count |
| 2 | **Competitive Utility.** Does the advantage survive the best classical alternative and the full workflow? | Current classical method; preprocessing, sampling, post-processing, error management included; advantage stated in time-to-solution, cost-to-solution, accuracy, or another explicit dimension | 'The quantum algorithm works' |
| 3 | **Commercial Conversion.** Does technical utility become repeated customer use and provider value capture? | Renewals, expansion, repeated hardware purchases, sustained cloud usage; contractual quality of backlog; profitable capture | Research collaborations as demand; paid PoCs as production; headline backlog as revenue |
| 4 | **Financed Roadmap.** Can the company reach the next major de-risking milestone with the capital available to it? | Milestone, capex, burn, next raise, dilution before the key uncertainty is removed | An unfunded technical story |

**Evidence Rule (Verification Integrity), applied to all four:** How strong is the evidence? Real hardware? Assumptions? Experiment vs simulation vs resource estimate? Uncertainty and methodology disclosed? Classical comparison credible? Independent reproduce / validate / audit possible? Evidence quality determines how much weight the headline deserves.

### Architecture-neutral economic core vs gate-model examples (appendix scope)

The economic framework is intended to be architecture-neutral: resource → reliable execution → workload → competitive utility → value capture. Several technical examples are drawn primarily from gate-model and fault-tolerant quantum computing. Gate fidelity, circuit width and depth, surface-code distance, logical operations, and magic-state production do not map directly onto every paradigm. Analog quantum simulation, annealing, and other architectures require workload-native equivalents. Raw qubit counts should not be compared casually across modalities.

QEC threshold is not a universal hardware constant. It depends on the error-correcting code, decoder, syndrome-extraction circuit, physical operations, and the structure of the underlying noise. Correlated errors and leakage become more important as systems scale. Willow demonstrates below-threshold logical-memory performance for its specific surface-code implementation; it is not proof that all components required for large-scale FT computation have reached the same maturity.

Width ≈ how many qubits participate. Depth ≈ how many sequential layers must be sustained. Neither is a complete performance metric. Connectivity matters because a compiler inserts extra operations when two qubits that must interact are not directly connected. The practical question is whether the hardware can execute the required combination of width, depth, connectivity, and accuracy for the workload.

Average fidelity is useful and incomplete. Distinguish single-qubit errors, two-qubit errors, measurement errors, leakage, crosstalk, correlated errors, calibration stability, and system-level circuit performance. A strong component benchmark does not automatically guarantee strong long-workload performance.

Fault-tolerant space-time resources: a real application may depend on logical operation count, target logical error, code distance, error-correction cycle time, decoder performance, physical-qubit overhead, and resources for expensive logical operations (including large magic-state factories). Space-time trade-off: more physical resources may reduce runtime; conserving qubits may increase time. Modern resource-estimation frameworks examine qubits and runtime together within an error budget. Resource estimation tells us what a computation may require under assumptions; it does not prove current hardware meets those assumptions.

## Evidence

All figures below are Superposition's recounting of named third-party results unless tagged otherwise. Treat as `[1×: Superposition]` at note level; secondary citations are named in the row.

**Willow / surface-code (Google Quantum AI, as cited)** `[1×: Superposition]` `[web: superpositionv.substack.com]`

| Claim | Figure | What it is / is not |
|---|---|---|
| Code | distance-7 surface-code memory | Logical *memory*, not a large FT application |
| Physical resources | 101 physical qubits | Encoding + overhead for that distance, not 101 logical qubits |
| Lifetime vs best constituent physical qubit | 2.4 ± 0.3 | Below-threshold scaling: increasing code distance reduced logical error |
| Mechanism shown | below-threshold logical-memory scaling | Additional redundancy made encoded information *more reliable*, not merely bigger |
| Remaining issues named in the Nature paper (per Superposition) | resource requirements; rare correlated error events | Scaling challenges, not a solved stack |
| Correct interpretation | piece of the FT scaling mechanism | Not 'Google has solved fault-tolerant quantum computing' |
| Appendix qualifier | specific surface-code implementation | Do not generalise to all FT components at equal maturity |

**QED-C application-oriented benchmarking** `[1×: Superposition]`

| Item | Content |
|---|---|
| Unit of analysis Superposition prefers | the *workload*, not the qubit |
| Suite design | varies problem sizes and inputs |
| Measured dimensions | result quality; total execution time; quantum gate resources |
| Later extension | linear systems; variational simulations; machine-learning classification |
| Explicit trade-off examined | result quality vs runtime |
| What it is | movement from component performance toward application performance |
| What it is not | a real customer production workload; commercial utility |

**Microsoft Quantum Resource Estimator** `[1×: Superposition]`

| Input | Output / use |
|---|---|
| Application model | Physical-qubit requirements |
| Hardware architecture | Runtime |
| Error-correction assumptions | Accumulated error |
| Factory model | (incl. magic-state factories as expensive logical-operation resources) |
| Error budget | Pareto-optimal trade-offs between qubit count and runtime |
| Category | Resource estimate under specified assumptions |
| Not | A hardware benchmark; proof current hardware meets those assumptions |

**DARPA US2QC and QBI (2026 / 2033)** `[1×: Superposition]`

| Program | Load-bearing statement |
|---|---|
| US2QC | For many proposed quantum applications, rigorous comparison against the best classical alternatives for real-world use has **not yet been completed** |
| QBI definition of utility-scale | Computational value exceeds cost |
| 2026 status | DARPA continues to evaluate whether **any architecture** can reach that standard **by 2033** |
| Stage A FAQ | Computational value will generally be measured in **dollars** |
| QBI Q&A on machine cost | Does **not** include R&D expenditure |
| QBI structure | Independent verification and validation of proposed paths to utility-scale QC |
| Implication Superposition draws | Machine utility ≠ attractive corporate economics ≠ shareholder returns after R&D, capex, dilution, and time |

**Worked numerical examples (illustrative, author-constructed)** `[1×: Superposition]` `[est.]`

| Example | Arithmetic Superposition uses | Point |
|---|---|---|
| Inventory vs compute | 10,000 physical qubits, shallow, error-overwhelmed vs 500 qubits, deeper and more accurate | Qubit count cannot rank the machines |
| Scale intuition | 100 vs 1,000 vs 1 million qubits | Ranking looks intuitive; it is not compute |
| Depth vs width | 50-qubit circuit, depth 100 vs 5-qubit circuit, depth 1,000 | Different machine demands; neither number is capability |
| Amdahl-style workflow | Quantum portion 100× faster, but 1% of customer total processing time | End-to-end barely moves |
| Capture failure | Customer saves $10m; provider revenue $1m; delivery cost $2m | Customer value created; provider value destroyed |

**Architecture capital stacks (qualitative, still evidence of the constraint layer)** `[1×: Superposition]`

| Modality | Engineering stack Superposition names |
|---|---|
| Superconducting | Cryogenic infrastructure, fabrication, packaging, control electronics |
| Trapped-ion / neutral-atom | Optical, laser, vacuum, and control systems |
| Photonic | Sources, switching, detectors, manufacturing, packaging, integration |

**Appendix failure modes (named checklist)** `[1×: Superposition]`

| Failure mode | Definition |
|---|---|
| Qubit inflation | Larger hardware count without corresponding improvement in executable workloads |
| Logical-qubit inflation | Logical-qubit number without error suppression, logical-operation quality, or scaling evidence |
| Simulator substitution | Simulated result discussed as current hardware capability |
| Estimator substitution | Future resource estimate treated as evidence the required hardware already exists |
| Weak classical baseline | Quantum method compared against an outdated or poorly optimised classical alternative |
| Subroutine advantage | Quantum component improves while the complete end-to-end workflow remains slower, more expensive, or less useful |
| PoC inflation | Experimental customer projects treated as durable production demand |
| Backlog inflation | Headline backlog treated as high-quality recurring revenue without cancellation rights, delivery conditions, timing, or conversion |
| Value-capture failure | System creates customer value; provider cannot capture enough for attractive unit economics |
| Roadmap-capital mismatch | Key technical proof point lies beyond the company's practical financing horizon |

**Variables Superposition lists for company-level verification** `[1×: Superposition]`

Physical and usable qubit counts; logical qubits where applicable; logical error rates; evidence of below-threshold scaling; operation quality; measurement errors; executable width and depth; architecture-specific connectivity or interaction constraints; system throughput; uptime; time-to-solution; benchmark methodology; classical baseline quality; hardware versus simulator execution; customer renewals; backlog quality and conversion; provider gross economics; cash burn; capex requirements; runway to the next major de-risking milestone. No single variable determines the answer; the interaction among them does.

**Open questions (Part 1 → Part 2)** `[1×: Superposition]`

| Question | Status |
|---|---|
| Can we build a better quantum computer? | No longer the hardest question |
| For which workloads does improving the quantum computer create an advantage the classical frontier cannot erase? | The hard question of Part 1 |
| Which of those advantages become large enough, repeatable enough, and economical enough to support durable businesses? | Beyond that |
| A better quantum computer does not prove that a problem needs a quantum computer | Hook for Part 2 (quantum machine learning) |

## Contradiction Check

There is no quantum thesis to support or challenge. `Theses/` has no IONQ, RGTI, QBTS or other quantum-name file. `Macro & Technology/` has no quantum note. `Sectors/` has no quantum sector note. The live Holdings table (not the JS `HOLDINGS` array) contains SK Hynix, Palantir, TSMC, SpaceX, Nvidia, Cloudflare, Broadcom, Nebius, Marvell, Sandisk, Kioxia, Advantest, Lam Research, Applied Materials, KLA, ASM International, and BE Semiconductor: none are quantum hardware or quantum-software names. Wikilink targets: none. Conviction and status: unchanged, because there is nothing to change.

The honest read is a low-signal ingest against the existing book and a high-signal ingest as a pre-thesis filter. If we later open a quantum name, Superposition's chain is the screen that would have to be passed before a qubit-count roadmap is allowed to set conviction. The only adjacent live-book contact is the classical-frontier claim (CPUs, GPUs, supercomputers, tensor networks, AI models, domain solvers as the moving competitor). That is consistent with the AI-compute sleeve remaining the default stack until an end-to-end utility result is shown; it does not touch a named §Conviction Trigger, §Key Non-consensus Insight, or Bull/Bear paragraph on NVDA or any other holding. A source that only supplies a screen we do not yet have a name to apply it to is exactly the 'confirms priors on nothing, challenges nothing on the book' case; say so.

If a future `/sync` were run against a still-absent quantum thesis, the correct action is still 'do not create a ticker'. The outstanding question is whether to stand up `Macro & Technology/` (or a sector note) for this conversion chain so that Part 2 and subsequent Superposition pieces have a home.

## Source Excerpts

> "A useful way to think about the industry is as a chain: hardware scale → reliable compute → executable workload → task-level quantum advantage → end-to-end competitive utility → workflow value → commercial capture → provider value capture → economic value. Every arrow is a conversion problem. And two additional layers sit across the entire chain. Verification determines whether we should believe each claim. Capital determines whether the company can survive long enough to reach the next layer."

> "physical qubit count ≠ logical qubit demonstration ≠ scalable logical error suppression ≠ useful logical computation. Each is evidence of progress. They are not interchangeable."

> "Its surface-code experiments demonstrated below-threshold logical-memory scaling: increasing the code distance reduced logical error. The distance-7 surface-code memory used 101 physical qubits, and its lifetime exceeded that of its best constituent physical qubit by a factor of 2.4 ± 0.3."

> "The Nature paper itself discusses substantial scaling challenges that remain, including resource requirements and rare correlated error events. So the correct interpretation is not: Google has solved fault-tolerant quantum computing. It is: Google demonstrated an important piece of the scaling mechanism required for fault-tolerant quantum computing."

> "Its benchmark suite varies problem sizes and inputs while measuring dimensions including result quality, total execution time, and quantum gate resources. Later work extended the framework across problems such as linear systems, variational simulations, and machine-learning classification while explicitly examining trade-offs between result quality and runtime."

> "Microsoft's current Quantum Resource Estimator illustrates what resource estimation is designed to do. Given an application model, hardware architecture, error-correction assumptions, factory model, and error budget, it evaluates combinations of design choices and estimates physical-qubit requirements, runtime, and accumulated error. It can then identify Pareto-optimal trade-offs between qubit count and runtime."

> "DARPA's US2QC program makes this problem explicit: for many proposed quantum applications, rigorous comparison against the best classical alternatives for real-world use has not yet been completed."

> "Suppose the quantum portion of a workflow becomes 100 times faster. That sounds enormous. But if that quantum portion accounts for only 1% of the customer's total processing time, the overall workflow barely changes."

> "QBI defines utility-scale operation as a quantum system whose computational value exceeds its cost, and in 2026 DARPA continues to evaluate whether any architecture can reach that standard by 2033. The latest Stage A FAQ also says that computational value will generally be measured in dollars. … In a QBI Q&A, DARPA clarified that its machine-cost calculation does not include R&D expenditure."

> "Suppose a quantum workload saves a customer $10 million. … imagine the quantum provider captures only $1 million in revenue and spends $2 million delivering the service. The technology creates customer value. The business destroys provider value."

> "A useful progression to watch is: research relationship → paid proof of concept → repeated usage → production workflow → renewal or expansion."

> "Superconducting systems may depend heavily on cryogenic infrastructure, fabrication, packaging, and control electronics. Trapped-ion and neutral-atom architectures may depend on demanding optical, laser, vacuum, and control systems. Photonic approaches face their own challenges in sources, switching, detectors, manufacturing, packaging, and integration."

> "There are four core questions. 1. Workload Capability … 2. Competitive Utility … 3. Commercial Conversion … 4. Financed Roadmap … Evidence Rule: Verification Integrity"

> "Failure Modes. Qubit inflation … Logical-qubit inflation … Simulator substitution … Estimator substitution … Weak classical baseline … Subroutine advantage … PoC inflation … Backlog inflation … Value-capture failure … Roadmap-capital mismatch."

> "The hardest question is no longer simply: Can we build a better quantum computer? It is: For which workloads does improving the quantum computer create an advantage that the classical frontier cannot erase? And beyond that: Which of those advantages become large enough, repeatable enough, and economical enough to support durable businesses? The first question leads directly to Part 2."
