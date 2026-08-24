---
date: 2026-08-21
publication: Superposition
title: '[Beyond Qubits] Part 1. Qubit Count Is Not Compute'
source: 'https://superpositionv.substack.com/p/beyond-qubits-part-1-qubit-count'
gmail_id: 1a024125d8a21caf
sender: superpositionv@substack.com
received: 2026-08-21T11:25:58Z
tags: [clippings, quantum]
source_type: inbox-clip
extracted_from: Gmail PLAIN_TEXT
thread_id: 1a024125d8a21caf
---

# [Beyond Qubits] Part 1. Qubit Count Is Not Compute

View this post on the web at https://superpositionv.substack.com/p/beyond-qubits-part-1-qubit-count

How investors should trace the conversion from hardware scale to reliable computation, competitive utility, and economic value

When a quantum computing company announces a new machine, qubit count often gets the headline. But qubit count is not compute. It measures one dimension of hardware scale; it does not tell us how much reliable computation the system can actually complete.
That distinction sounds simple, but it changes how a quantum company should be evaluated.
Imagine two machines. One has 10,000 physical qubits but can execute only shallow computations before errors overwhelm the result. Another has 500 qubits, but better control allows it to sustain a smaller but much deeper and more accurate workload. Which machine has more computing power?
The qubit count alone cannot answer the question.
And even if we determine which machine can perform the more difficult computation, an investor still has several questions left. Does that computation beat the best classical alternative? Does the advantage survive the full workflow? Does a customer care enough to pay for it? Can the quantum company capture that value? And can it reach that point before the capital roadmap runs out?
This is the deeper structure behind quantum computing investment.
The governing structure is conversion, not inventory.
A useful way to think about the industry is as a chain:
hardware scale
→ reliable compute
→ executable workload
→ task-level quantum advantage
→ end-to-end competitive utility
→ workflow value
→ commercial capture
→ provider value capture
→ economic value
Every arrow is a conversion problem.
And two additional layers sit across the entire chain.
Verification determines whether we should believe each claim.
Capital determines whether the company can survive long enough to reach the next layer.
This is why the largest number in a quantum computing presentation is rarely enough.
1. A Qubit Count Measures Scale, Not Useful Compute
The appeal of qubit count is obvious.
It is simple.
One machine has 100 qubits. Another has 1,000. A third promises one million.
The ranking seems intuitive.
But quantum systems do not work like storage capacity, where twice the number of bits roughly means twice the room to store information.
More qubits create more potential computational resources, but they also create a larger system that must be controlled.
Quantum information is fragile. Operations can introduce errors. Qubits can lose information through decoherence. Measurements can be imperfect. Control signals can drift. Unwanted interactions can affect nearby qubits.
So increasing the number of qubits does not automatically increase the amount of useful computation.
A loose analogy is transistor count.
A chip with more transistors may be more capable, but transistor count alone does not tell you the performance of the computer. Architecture, memory, power, software, manufacturing quality, and cooling all matter.
Quantum computing adds another difficulty: the information being manipulated is itself unusually sensitive to noise.
A larger machine therefore matters only if the company can turn that additional hardware into controlled, reliable execution.
That is the first conversion.
Hardware scale → reliable compute
2. Physical Qubits and Logical Qubits Are Different Layers
This brings us to one of the most important distinctions in quantum computing: physical qubits versus logical qubits.
A physical qubit is a hardware-level quantum resource.
But in an error-corrected machine, not every physical qubit directly represents the information that the user wants to compute with. Some physical resources may support error detection, syndrome measurement, routing, or other functions required to protect the logical information.
The long-term goal of fault-tolerant quantum computing is to encode quantum information so that errors can be detected and corrected faster than they destroy the computation.
In many error-correction architectures, multiple physical qubits are used to encode a logical qubit.
This is why logical qubits are often treated as a more meaningful milestone than raw physical-qubit count.
But investors should be careful not to replace one simplistic metric with another.
Logical qubit count is not utility either.
Creating a logical qubit is one milestone.
Showing that it becomes more reliable as error correction becomes stronger is another.
Performing useful logical operations at sufficiently low error rates is another.
Executing a large application with those operations is another step again.
The distinction can be summarized this way:
physical qubit count
≠ logical qubit demonstration
≠ scalable logical error suppression
≠ useful logical computation
Each is evidence of progress.
They are not interchangeable.
3. Error Correction Has to Improve With Scale
Quantum error correction illustrates why conversion matters more than inventory.
Adding more physical resources to an error-correction code is useful only if the additional redundancy makes the encoded quantum information more reliable.
That does not happen automatically.
The physical operations must first be good enough for the chosen error-correction system to operate below the relevant error threshold. Once that condition is met, strengthening the code can reduce the logical error rate.
For investors, the technical intuition is more important than the mathematics:
A bigger error-corrected system should become more reliable, not merely bigger.
Google Quantum AI’s Willow work provides a useful example.
Its surface-code experiments demonstrated below-threshold logical-memory scaling: increasing the code distance reduced logical error. The distance-7 surface-code memory used 101 physical qubits, and its lifetime exceeded that of its best constituent physical qubit by a factor of 2.4 ± 0.3.
That is a meaningful result because it demonstrates the mechanism that error correction is supposed to provide.
But it is equally important to say what it does not prove.
It does not demonstrate a large fault-tolerant application.
It does not prove that useful logical algorithms can already run at commercial scale.
The Nature paper itself discusses substantial scaling challenges that remain, including resource requirements and rare correlated error events.
So the correct interpretation is not:
Google has solved fault-tolerant quantum computing.
It is:
Google demonstrated an important piece of the scaling mechanism required for fault-tolerant quantum computing.
That distinction is exactly the kind investors need to preserve.
4. There Is No Single Number That Replaces Qubit Count
If qubit count is insufficient, what should replace it?
There is no universal answer.
That is uncomfortable, but important.
Quantum compute is multidimensional.
At the component level, investors may encounter numbers such as gate fidelity, measurement error, gate speed, coherence time, and physical-qubit count.
At the system level, other variables become important: usable width, executable depth, connectivity, throughput, stability, and uptime.
But none of those alone is the final object we care about.
The real question sits one layer higher:
Can the system complete the required workload at the required accuracy?
And then:
How much time and resource does it require to produce that trustworthy result?
This is why raw gate speed can also be misleading.
A fast quantum operation does not guarantee a fast application.
A real computation may require circuit preparation, compilation, repeated execution, measurements, error mitigation or correction, communication with classical processors, parameter optimization, and classical post-processing.
The relevant quantity is therefore closer to time-to-solution than gate time.
The same principle applies to circuit depth.
Depth matters, but depth alone does not define computational capability.
A 50-qubit circuit with depth 100 and a five-qubit circuit with depth 1,000 place different demands on a machine. Hardware connectivity can also force a compiler to insert additional routing operations, making the physical execution more expensive than the abstract circuit suggests.
So there is no single magic number.
There is a hierarchy of measurements.
Component metrics
→ system benchmarks
→ application-oriented benchmarks
→ actual workload
→ customer workflow
The higher we move, the closer we get to economic relevance.
5. The Better Unit of Analysis Is the Workload
This is why the better unit of analysis is not the qubit.
It is the workload.
The Quantum Economic Development Consortium’s application-oriented benchmarking work is useful here.
Its benchmark suite varies problem sizes and inputs while measuring dimensions including result quality, total execution time, and quantum gate resources. Later work extended the framework across problems such as linear systems, variational simulations, and machine-learning classification while explicitly examining trade-offs between result quality and runtime.
That is an improvement over judging a machine through a single component metric.
But another distinction matters.
An application-oriented benchmark is not necessarily a real customer production workload.
Benchmarks can include algorithms, subroutines, simplified problems, or workloads chosen because they expose useful properties of a quantum system.
They help move us from component performance toward application performance.
They do not, by themselves, demonstrate commercial utility.
This is why the hierarchy matters:
gate metric
→ system capability
→ application-oriented benchmark
→ end-to-end workload
→ customer workflow
Each layer removes another abstraction.
The closer we get to the customer workflow, the harder it becomes to hide behind a single impressive hardware number.
6. Resource Estimates Are Not Hardware Benchmarks
A related category error appears when investors encounter fault-tolerant resource estimates.
Suppose a paper estimates that a future quantum algorithm will require a certain number of physical qubits and a certain runtime.
That information can be extremely useful.
But it does not mean an existing machine can perform the computation.
Microsoft’s current Quantum Resource Estimator illustrates what resource estimation is designed to do. Given an application model, hardware architecture, error-correction assumptions, factory model, and error budget, it evaluates combinations of design choices and estimates physical-qubit requirements, runtime, and accumulated error. It can then identify Pareto-optimal trade-offs between qubit count and runtime.
This is precisely why logical-qubit count alone is not enough for fault-tolerant computing.
A real application consumes a combination of space, time, error budget, decoding resources, and sometimes expensive logical-operation resources such as magic-state factories.
But the category must remain clear:
A resource estimate is not a hardware benchmark.
It tells us what a fault-tolerant computation may require under specified assumptions.
It does not demonstrate that a company has already achieved those hardware assumptions.
So investors should distinguish:
resource estimate
≠ hardware demonstration
≠ application advantage
All three are useful.
They answer different questions.
7. Compute Is Not Quantum Advantage
Suppose we now have a machine that can reliably execute a difficult workload.
Have we demonstrated useful quantum computing?
Not yet.
We have demonstrated compute.
The next conversion is competitive.
Potential quantum applications are often discussed in chemistry, materials science, quantum many-body simulation, cryptography, and certain optimization problems.
In drug discovery, for example, the relevant claim is not that a quantum computer will somehow “discover drugs.” The more defensible question is whether quantum computation can improve particular molecular or electronic-structure calculations inside a much larger discovery workflow.
These are candidate areas.
They are not all established commercial quantum-advantage markets.
To establish advantage, we need a competitor.
That competitor is classical computing.
And not the classical computer of ten years ago.
Not an intentionally weak algorithm.
Not an unoptimized baseline.
The relevant competitor is the best practical classical stack available when the comparison matters.
That stack may include CPUs, GPUs, supercomputers, tensor networks, specialized numerical methods, AI models, heuristics, and domain-specific solvers.
DARPA’s US2QC program makes this problem explicit: for many proposed quantum applications, rigorous comparison against the best classical alternatives for real-world use has not yet been completed.
This matters because the classical frontier moves.
An algorithm that once looked unreachable may become tractable after a better approximation, solver, GPU implementation, or mathematical technique appears.
So quantum computing is not racing against a stationary target.
It is racing against the classical frontier at the time useful quantum hardware arrives.
8. Task-Level Advantage Is Not End-to-End Utility
This gives us another distinction.
A quantum system may show an advantage on a particular computational task without producing an advantage for the entire workflow.
Call the first one task-level quantum advantage.
A quantum kernel, sampling problem, simulation step, or subroutine may outperform known classical methods on a carefully defined task.
That can be scientifically and technically important.
But a customer does not purchase an isolated subroutine.
The full process may also require:
data preparation,
encoding,
compilation,
repeated quantum execution,
measurement,
error management,
classical optimization,
post-processing,
verification,
and integration with existing software.
The advantage has to survive those surrounding costs.
This leads to a more demanding standard:
End-to-end competitive utility
Suppose the quantum portion of a workflow becomes 100 times faster.
That sounds enormous.
But if that quantum portion accounts for only 1% of the customer’s total processing time, the overall workflow barely changes.
Likewise, a computational advantage may disappear if the quantum system requires too many repeated measurements, too much preprocessing, or expensive error correction.
This is why a genuine quantum advantage should eventually be evaluated at the level of the entire task.
Not just:
Is the quantum circuit faster?
But:
Does the complete quantum-enabled workflow produce a better outcome than the best complete classical workflow?
And “better” may mean different things.
It could mean lower time-to-solution.
Lower cost-to-solution.
Higher accuracy.
A larger tractable problem.
Lower energy consumption.
Or access to a useful result that was previously impractical.
The dimension of advantage has to be stated explicitly.
9. Workflow Utility Is Still Not Economic Utility
Even an end-to-end computational advantage does not automatically create an economically useful product.
The computation has to remove a real bottleneck.
A pharmaceutical company does not ultimately want more quantum gates.
It wants better decisions about which molecules to test.
A materials company does not want a larger circuit.
It wants better candidates, fewer failed experiments, shorter development cycles, or access to properties that were previously too costly to calculate.
This is the transition from computational utility to workflow value.
Then comes another transition.
How much is that workflow improvement worth?
DARPA’s Quantum Benchmarking Initiative offers a useful external reference point. QBI defines utility-scale operation as a quantum system whose computational value exceeds its cost, and in 2026 DARPA continues to evaluate whether any architecture can reach that standard by 2033.
The latest Stage A FAQ also says that computational value will generally be measured in dollars.
That is a useful discipline.
A difficult calculation is not automatically valuable.
A valuable calculation is not automatically economical.
But an investor needs one more distinction.
DARPA’s definition of machine utility is not the same thing as attractive corporate economics.
In a QBI Q&A, DARPA clarified that its machine-cost calculation does not include R&D expenditure.
So these three statements are not equivalent:
customer computational value exceeds machine cost
the provider earns attractive unit economics
shareholders earn attractive returns after R&D, capex, dilution, and time
The first can be true while the third is false.
This is where technical utility becomes investment analysis.
10. Customer Value Must Become Provider Value Capture
Suppose a quantum workload saves a customer $10 million.
That sounds valuable.
But imagine the quantum provider captures only $1 million in revenue and spends $2 million delivering the service.
The technology creates customer value.
The business destroys provider value.
That distinction matters enormously in deep tech.
The commercial chain is therefore more accurately written as:
workflow utility
→ willingness to pay
→ commercial conversion
→ provider value capture
→ economic value
The specific business model can differ.
A quantum company may sell hardware.
It may charge for cloud access.
It may earn revenue through government contracts.
It may run paid proof-of-concept projects.
It may license software or intellectual property.
It may operate a vertically integrated service.
What matters is whether experimentation progresses toward repeated economic dependence on the product.
A useful progression to watch is:
research relationship
→ paid proof of concept
→ repeated usage
→ production workflow
→ renewal or expansion
Not every business will follow those exact steps.
But the direction matters.
A paid proof of concept tells us that someone is willing to fund experimentation.
It does not prove that quantum computing belongs permanently in the customer’s workflow.
The same caution applies to backlog.
Backlog can indicate contracted commitments, but its quality depends on the company’s definition, cancellation rights, delivery conditions, timing, and the probability that those commitments convert into recognized revenue.
So the investor should ask:
Is customer interest becoming recurring usage?
And then:
Can the company capture enough of the value it creates to build a good business?
11. Capital Is a Constraint Across the Entire Roadmap
There is another reason quantum company analysis cannot stop at technical capability.
Time costs money.
Quantum computing is a capital-intensive deep-tech industry, and different architectures require different engineering stacks.
Superconducting systems may depend heavily on cryogenic infrastructure, fabrication, packaging, and control electronics.
Trapped-ion and neutral-atom architectures may depend on demanding optical, laser, vacuum, and control systems.
Photonic approaches face their own challenges in sources, switching, detectors, manufacturing, packaging, and integration.
The details differ.
The investment principle does not.
A technically plausible roadmap is useful only if the company can finance it.
This is why capital should not be treated as the final step in the causal stack.
It is better understood as a constraint across the roadmap.
At every stage, investors should ask:
What is the next milestone that materially reduces technical risk?
Then:
How much capital is required to reach it?
Then:
Can the company reach that milestone before it needs to raise money again?
A company that can demonstrate a major de-risking event before its next financing occupies a very different position from one that must raise billions before validating its key technical assumption.
Cash burn is therefore not merely an accounting variable.
In deep tech, it determines how much time the physics has to work.
12. Verification Is an Evidence Layer, Not a Product Layer
The same structural distinction applies to verification.
Verification is not another step through which quantum resources physically transform into economic value.
It is the evidence layer that tells us whether each claimed transformation is real.
For every arrow in the stack, investors should ask:
What evidence proves that this conversion occurred?
For hardware scale → reliable compute:
Did error rates actually improve? Was the result produced on real hardware?
For reliable compute → workload:
Was a meaningful workload executed, or only a component benchmark?
For workload → competitive utility:
Was the best available classical baseline used?
For utility → commercialization:
Are customers repeatedly using the system, or merely testing it?
For commercial conversion → economic value:
Is the company capturing value after the cost of delivering the product?
Verification therefore sits across the causal stack.
This distinction also explains why third-party validation matters.
Not every proprietary system can be perfectly reproduced by outside researchers.
But the methodology, assumptions, benchmark conditions, uncertainty, and comparison methods should be disclosed well enough for credible independent verification or audit.
DARPA’s QBI is explicitly structured around independent verification and validation of proposed paths to utility-scale quantum computing.
The principle extends beyond DARPA.
A quantum claim becomes more valuable when the evidence becomes harder to manipulate.
13. Four Questions for Evaluating a Quantum Computing Company
With the causal chain, evidence layer, and capital constraint separated, the investor framework becomes simpler.
There are four core questions.
1. Workload Capability
Can the system complete harder and more valuable workloads on real hardware at the required accuracy?
Do not begin with total qubit count.
Look for evidence that executable capability is increasing.
Can the company use more of its system effectively?
Can it sustain greater width and depth?
Are error rates improving?
If it is pursuing fault tolerance, does stronger error correction actually reduce logical error?
The key is movement from hardware inventory toward reliable execution.
2. Competitive Utility
Does the advantage survive the best classical alternative and the full workflow?
Do not ask only whether the quantum algorithm works.
Ask what classical method it is being compared against.
Is the baseline current?
Are preprocessing, sampling, post-processing, error management, and other overhead included?
Does the advantage survive when measured in time-to-solution, cost-to-solution, accuracy, or another explicitly stated dimension?
Quantum advantage matters only if enough of it survives the moving classical frontier.
3. Commercial Conversion
Does technical utility become repeated customer use and provider value capture?
Separate research collaborations from recurring production demand.
Separate paid PoCs from long-term workloads.
Treat backlog according to its actual contractual quality, not merely its headline size.
Look for renewals, expansion, repeated hardware purchases, sustained cloud usage, or other evidence that the customer continues paying after the experiment ends.
And then ask whether the provider can capture the value profitably.
Technology value and company value are not the same thing.
4. Financed Roadmap
Can the company reach the next major de-risking milestone with the capital available to it?
Map the technical roadmap onto the financing roadmap.
What has to be demonstrated next?
What equipment, manufacturing capacity, infrastructure, and people are required?
How much cash will be consumed?
When is another financing likely?
What dilution might be required before the key technical uncertainty is removed?
A roadmap that cannot be financed is not an investable roadmap.
Evidence Rule: Verification Integrity
The four questions above should all be evaluated through the same rule:
How strong is the evidence?
Was the result produced on real hardware?
What assumptions were used?
Is it an experimental result, a simulation, or a resource estimate?
Are uncertainty and methodology disclosed?
Was the classical comparison credible?
Can independent parties reproduce, validate, or audit the claim?
The quality of the evidence determines how much weight the headline deserves.
What Matters / What Does Not
What matters is not which company announces the largest qubit count.
What matters is whether additional hardware scale converts into reliable workload capability.
What matters is not whether a company can produce an impressive quantum demonstration.
What matters is whether the advantage survives the best classical alternative and the full end-to-end workflow.
What matters is not whether customers are willing to pay for experiments.
What matters is whether experiments become repeated usage and commercial dependence.
And what matters to an investor is not merely whether the technology creates customer value.
What matters is whether the company can capture enough of that value before the capital roadmap runs out.
From Qubits to Economic Value
The core causal stack is therefore:
hardware scale
→ reliable compute
→ executable workload
→ task-level quantum advantage
→ end-to-end competitive utility
→ workflow value
→ commercial capture
→ provider value capture
→ economic value
Across that entire chain sits:
Evidence overlay → verification integrity
And across the roadmap sits:
Capital constraint → runway to the next de-risking milestone
This structure matters because every conversion can fail.
More physical qubits may fail to produce better reliable computation.
Better error correction may fail to produce useful logical operations.
A useful workload may fail to beat a new classical algorithm.
A task-level quantum advantage may disappear when the full workflow is counted.
A workflow improvement may create too little customer value to justify its cost.
A valuable product may fail to produce attractive provider economics.
And a technically promising company may run out of capital before it reaches the milestone that proves the thesis.
The largest number in the stack therefore does not determine the value of the system.
The weakest conversion can.
This is why the first investor question should not be:
How many qubits does it have?
A better sequence is:
What reliable computation can those qubits actually perform?
Then:
Does that computation retain an advantage against the best classical alternative?
Then:
Does that advantage matter in a real customer workflow?
Then:
Can the company capture the resulting value before the roadmap consumes too much capital?
Once these questions are separated, quantum computing becomes somewhat less mysterious.
It becomes a problem of converting one layer of capability into the next.
And that leads directly to the next question in this series:
A better quantum computer does not prove that a problem needs a quantum computer.
That distinction becomes especially important when we turn to quantum machine learning.
Appendix
Assumptions and Scope
The economic framework in this essay is intended to be architecture-neutral:
resource → reliable execution → workload → competitive utility → value capture
Several of the technical examples, however, are drawn primarily from gate-model and fault-tolerant quantum computing.
Metrics such as gate fidelity, circuit width and depth, surface-code distance, logical operations, and magic-state production do not map directly onto every quantum computing paradigm.
Analog quantum simulation, annealing, and other architectures require workload-native equivalents.
This is another reason raw qubit counts should not be compared too casually across different modalities.
QEC Thresholds Are Architecture-Dependent
The QEC threshold discussed in the main text should not be understood as a universal hardware constant.
It depends on the error-correcting code, decoder, syndrome-extraction circuit, physical operations, and the structure of the underlying noise.
Correlated errors and leakage can be particularly important when systems scale.
Google’s Willow result demonstrates below-threshold logical-memory performance for its specific surface-code implementation. It should not be generalized into proof that all components required for large-scale fault-tolerant computation have already reached the same maturity.
Width, Depth, and Connectivity
Circuit width roughly describes how many qubits participate in a computation.
Depth describes how many sequential layers of operations must be sustained.
Neither is a complete performance metric.
Connectivity also matters because a compiler may need to insert additional operations when two qubits that must interact are not directly connected.
The practical question is therefore whether the hardware can execute the required combination of width, depth, connectivity, and accuracy for the workload.
Fidelity Is Not One Number
Average fidelity is useful but incomplete.
Depending on the architecture and workload, investors may need to distinguish among:
single-qubit errors,
two-qubit errors,
measurement errors,
leakage,
crosstalk,
correlated errors,
calibration stability,
and system-level circuit performance.
A strong component benchmark does not automatically guarantee strong long-workload performance.
Fault-Tolerant Space-Time Resources
For fault-tolerant computation, logical-qubit count is only one part of the resource requirement.
A real application may depend on:
logical operation count,
target logical error,
code distance,
error-correction cycle time,
decoder performance,
physical-qubit overhead,
and the resources required for expensive logical operations.
Some algorithms may also require large magic-state factories.
This creates a space-time trade-off.
Using more physical resources may reduce runtime. Conserving qubits may increase time.
This is why modern resource-estimation frameworks examine qubits and runtime together within an error budget rather than reducing the entire computation to one headline number.
Again:
Resource estimation tells us what a computation may require under assumptions. It does not prove that current hardware meets those assumptions.
Failure Modes
Qubit inflation: A larger hardware count is presented without corresponding improvement in executable workloads.
Logical-qubit inflation: A logical-qubit number is presented without error suppression, logical-operation quality, or scaling evidence.
Simulator substitution: A simulated result is discussed as though it demonstrates current hardware capability.
Estimator substitution: A future resource estimate is interpreted as evidence that the required hardware already exists.
Weak classical baseline: A quantum method is compared against an outdated or poorly optimized classical alternative.
Subroutine advantage: A quantum component improves while the complete end-to-end workflow remains slower, more expensive, or less useful.
PoC inflation: Experimental customer projects are interpreted as evidence of durable production demand.
Backlog inflation: Headline backlog is treated as equivalent to high-quality recurring revenue without examining cancellation rights, delivery conditions, timing, or conversion.
Value-capture failure: A system creates customer value but the provider cannot capture enough of it to support attractive unit economics.
Roadmap-capital mismatch: The key technical proof point lies beyond the company’s practical financing horizon.
Variables to Verify
For deeper company analysis, useful variables may include physical and usable qubit counts; logical qubits where applicable; logical error rates; evidence of below-threshold scaling; operation quality; measurement errors; executable width and depth; architecture-specific connectivity or interaction constraints; system throughput; uptime; time-to-solution; benchmark methodology; classical baseline quality; hardware versus simulator execution; customer renewals; backlog quality and conversion; provider gross economics; cash burn; capital expenditure requirements; and runway to the next major de-risking milestone.
No single variable determines the answer.
The interaction among them does.
Open Questions
The hardest question is no longer simply:
Can we build a better quantum computer?
It is:
For which workloads does improving the quantum computer create an advantage that the classical frontier cannot erase?
And beyond that:
Which of those advantages become large enough, repeatable enough, and economical enough to support durable businesses?
The first question leads directly to Part 2.

Thanks for reading! Subscribe for free to receive new posts and support my work.
