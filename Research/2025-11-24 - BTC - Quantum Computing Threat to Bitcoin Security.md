---
date: 2025-11-24
tags: [research, crypto, bitcoin, quantum-computing, risk]
status: active
sector: Crypto
source: Grok AI conversation export
---

# Quantum Computing Threat to Bitcoin Security

## Source Content

> [!info] Grok Conversation Export
> Ingested from Grok.zip on 2026-04-14. Original conversation date: 2025-11-24.

**Q:** How long before commercial quantum computers can break bitcoin hashing algorithm.

---

### Understanding the Threat to Bitcoin's Hashing Algorithm

Bitcoin's hashing algorithm, SHA-256 (used for proof-of-work mining and transaction hashing), is a symmetric cryptographic primitive designed to be collision-resistant and preimage-resistant. Classically, breaking it—e.g., finding a preimage (input for a given output) or collision (two inputs with the same output)—requires approximately 2^256 operations, which is computationally infeasible.

Quantum computers don't fully "break" SHA-256 like they can asymmetric cryptography (e.g., via Shor's algorithm on ECDSA signatures). Instead, Grover's algorithm offers a quadratic speedup for unstructured search problems, reducing the complexity to about 2^128 operations for a preimage attack. This effectively halves the security level (from 256 bits to 128 bits), making it comparable to a weakened classical algorithm. However, 2^128 operations remains astronomically large—far beyond practical computation today.

#### Resources Required
- **Qubits Needed**: Implementing Grover's algorithm for SHA-256 requires implementing a reversible quantum circuit for the hash function, plus workspace for the search space. Estimates vary:
  - At minimum, around 5,000–10,000 **logical qubits** for the basic circuit, but scaling to run the full 2^128 iterations demands **hundreds of millions to billions of physical qubits** (due to error correction overhead, where 1 logical qubit might need 1,000+ physical qubits).
  - For context, current commercial quantum computers (e.g., IBM's ~1,000-qubit systems as of late 2025) are noisy and offer only a handful of reliable logical qubits. Achieving fault-tolerant, scalable systems at this level is a massive engineering challenge.
- **Time and Operations**: Even with sufficient qubits, running 2^128 Grover iterations could take centuries to millennia on optimistic hardware assumptions, unless massive parallelism is achieved.

#### Timeline for Commercial Quantum Computers
Expert consensus from recent analyses (as of November 2025) points to **no practical threat to SHA-256 from commercial quantum computers for at least 20–30 years**, likely not before 2045–2055. Here's why:
- **Short-Term (5–10 Years)**: Progress will focus on noisy intermediate-scale quantum (NISQ) devices with <10,000 physical qubits. These can't run Grover's at scale for SHA-256; they're more suited to small proofs-of-concept. The nearer-term risk (10–15 years) is to Bitcoin's ECDSA signatures via Shor's algorithm, which needs "only" ~2,000–4,000 logical qubits.
- **Mid-Term (10–20 Years)**: Fault-tolerant quantum computers with 100,000–1 million physical qubits may emerge commercially (e.g., from IBM, Google, or IonQ roadmaps). This could threaten weaker symmetric crypto (e.g., AES-128), but SHA-256's effective 128-bit post-quantum security holds.
- **Long-Term (20+ Years)**: Only then might we see systems with the millions/billions of qubits needed for Grover-scale attacks on SHA-256. Some optimistic projections (e.g., from Chainalysis) warn of broader crypto threats by 2040, but this primarily targets signatures, not hashing.

Bitcoin's community is proactive: Satoshi Nakamoto anticipated quantum risks and suggested forking to quantum-resistant hashes (e.g., SHA-3 or lattice-based alternatives) if needed. Upgrades like BIP-340 (Schnorr signatures) and potential post-quantum standards from NIST could mitigate risks well before they materialize.

In summary, while quantum computing is advancing rapidly, SHA-256's robustness means commercial systems won't break it anytime soon—think generational horizon, not next decade. For Bitcoin holders, the hashing layer is safer than the signing layer in the quantum era.

---

**Q:** Shor's algorithm on ECDSA

---

### Shor's Algorithm and Its Threat to ECDSA

Shor's algorithm, developed by Peter Shor in 1994, is a quantum algorithm that efficiently solves two fundamental problems in number theory: integer factorization and the discrete logarithm problem. These are the mathematical foundations of many public-key cryptosystems. Classically, solving them requires exponential time (e.g., brute-force search), making them secure for practical purposes. Quantumly, Shor's reduces the complexity to polynomial time, enabling a "practical" break with sufficient hardware.

#### How Shor's Algorithm Targets ECDSA
Bitcoin (and many blockchains) uses the Elliptic Curve Digital Signature Algorithm (ECDSA) over the secp256k1 curve for transaction signing. ECDSA's security relies on the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**: given a public key point \( Q = d \cdot G \) (where \( G \) is the base point and \( d \) is the private key), finding \( d \) is computationally infeasible classically.

- **Shor's Application**: The algorithm computes the discrete log in an elliptic curve group using quantum Fourier transforms and period-finding. For secp256k1 (a 256-bit curve), it can recover the private key from the public key in \( O(n^3) \) time, where \( n \approx 256 \) is the bit length—vastly faster than classical attacks (which need ~2^{128} operations).
- **Attack Vector on Bitcoin**: An attacker with a public key (exposed via a spent transaction or reused address) could derive the private key and forge signatures to steal funds. Unspent outputs with hidden public keys (e.g., pay-to-script-hash addresses) are safer until spent.

This doesn't affect Bitcoin's SHA-256 hashing (which resists Grover's algorithm, needing ~2^{128} operations), but it endangers the signing layer.

#### Hardware Requirements
Running Shor's on secp256k1 demands a fault-tolerant quantum computer:
- **Logical Qubits**: Estimates range from 523  to 2,330–2,619 , depending on optimizations like windowed arithmetic or fault-tolerant gates. A conservative lower bound is ~2,000 logical qubits for a full run.
- **Physical Qubits**: Error correction (e.g., surface codes) inflates this: 1 logical qubit may require 1,000–10,000 physical qubits, leading to 1–10 million physical qubits total .
- **Runtime**: With ~1 GHz clock speeds and parallelization, cracking one key might take hours to days , but scaling to multiple attacks adds overhead.

Current systems (e.g., Google's Willow chip with 105 qubits as of late 2025) are noisy and far short—advances like error reduction help, but not enough for ECDLP yet [post:3][post:11][post:13].

#### Timeline for a Practical Break
Expert views vary due to uncertainties in scaling (e.g., qubit fidelity, manufacturing). As of November 2025:
- **Near-Term Optimism/Pessimism**: A "Quantum Doomsday Clock" projects a cryptographically relevant quantum computer (CRQC) by March 2028 (2.3 years from now) . Vitalik Buterin estimates a 20% chance of quantum-breaking crypto by 2030, urging Ethereum upgrades by 2028 [post:1]. Aggressive forecasts: 4–5 years .
- **Consensus Mid-Range**: 5–15 years (mid-2030s to 2040) per Chainalysis and others . ChatGPT-5 models 45–60% likelihood in 2035–2039 .
- **Longer-Term Skepticism**: Blockstream CEO Adam Back sees 20–40 years [post:0]. The threat has been known since ~2010, giving ample upgrade time [post:0].

Geopolitical shocks or breakthroughs (e.g., in logical qubit density) could accelerate this, but Bitcoin's community has anticipated it since Satoshi's era .

#### Implications and Mitigations for Bitcoin
- **Risks**: ~20% of BTC (3–4 million coins, including Satoshi's) in vulnerable exposed-key addresses could be targeted first [post:8]. Market panic, theft, and forks are possible if unprepared.
- **Defenses**:
  - **Soft Forks**: Migrate to post-quantum signatures (e.g., NIST's Dilithium, Falcon, or XMSS) via Taproot upgrades [post:5][post:9]. Bitcoin can "upgrade like everything else" [post:9].
  - **Best Practices**: Use fresh addresses (hides public keys); avoid reuse. zk-SNARKs (deployed since 2016) add privacy layers [post:0].
  - **Ecosystem Response**: Ethereum targets quantum-readiness by 2028 [post:1]; Bitcoin discussions favor backward-compatible shifts [post:8].

In essence, Shor’s poses an existential but addressable threat to ECDSA—more urgent than to hashing, but with a 10–20 year runway for action. Quantum-resistant Bitcoin is feasible; the real challenge is consensus.
