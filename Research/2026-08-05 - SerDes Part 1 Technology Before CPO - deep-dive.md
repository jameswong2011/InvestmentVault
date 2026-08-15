---
publish: false
date: 2026-08-05
tags: [research, Semiconductors, NVDA, MRVL, SerDes]
sector: Custom Silicon & Networking Semiconductors
ticker: MRVL
propagated_to: [MRVL, NVDA]
source: 'https://nuttycld.substack.com/p/public-serdes-part-1-the-technology'
source_type: deep-dive
updated: 2026-08-14
---

# SerDes Part 1 The Technology You Should Know Before CPO

## Thesis Delta

Consensus prices the CPO / "optics era" as the death of electrical high-speed design, and treats "best SerDes IP" as the investable object → Nutty (analog IC designer) argues a SerDes sits at both ends of every electrical or optical link, LPO/CPO relocate analog/DSP work rather than delete DAC/ADC serializers, and 224G+ (fundamental already ~56 GHz) forces chip-package-board co-design. The money question is who converts that skill into systems, products, or components (Part 2), not who publishes the fastest IP. Hypotheses: [G-13] priced optics-kills-electrical; Semis #8 NRZ→PAM4→PAM6 + CPO remaps the bottleneck; VLM §2 pure SerDes IP fails the layer-owner test.

## Summary

Digital won communication on noise tolerance: a receiver only has to tell 0 from 1, while every analog level carries meaning and must be reconstructed. AI training and inference broke the next constraint. Inside a chip, data already moves in parallel on thousands to tens of thousands of wires; HBM raises bandwidth by adding those lines. Off-chip, matching that parallelism with physical wires and optical cables would occupy more volume than the chips themselves — racks linking tens of thousands of GPUs are already packed. SerDes (serializer / deserializer) is the circuit at the chip boundary that converts parallel on-die data into a fast serial stream on the way out and back into parallel on the way in. The transmission medium — copper or fiber — is a materials question; the method of sending more bits per pin is the same, so SerDes has existed from early electrical links and will remain after optical becomes the rack-internal norm. Lane rates encode that speed-up: 112G/lane is 112 billion bits per second on one path; the industry is crossing to 224G/lane, with 448G/lane under continuous development. The design metric that actually binds is bits per second inside a fixed power budget. NVIDIA's own scale check: in a 100K-server-class datacenter, optical-module transceivers draw 2.3 MW in a traditional cloud and 40 MW in an AI factory — data-movement electricity at power-plant scale. NVIDIA's fiscal 2026 annual report is the revenue proof of the same shift: computing-chip revenue +59%, networking (the business of connecting those chips) +142%.

PAM4 (4-level pulse-amplitude modulation) is how 112G and 224G actually run. NRZ is two levels and one bit per symbol; PAM4 is four levels and two bits, so the pattern `01` is one symbol instead of two NRZ transmissions. Raising the PAM number loads more bits onto each carrier and is therefore attractive on paper — which is why the question "why not PAM6 or PAM8?" is the right one. More levels is digital stepping back toward analog: the margin bands in which a receiver can still recover a distorted symbol shrink as the count rises. OIF, holding error rate fixed, calculates PAM6 needs 3.6 dB more noise margin than PAM4 and PAM8 needs 6.1 dB more; PAM8 requires 4× the SNR of PAM4. Closing that gap means doubling the signal (raise voltage, burn power) or halving noise (physical floors). The industry still probes PAM6 for 448G, and ISSCC publishes higher-level-count papers every year — a door that will have to be passed, not a free lunch. The circuit that builds the multi-level symbol is a DAC-based serializer; the receive side is an ADC-based deserializer. Analog designers own the conversion; digital designers own the reconstruction algorithms that strip attenuation and distortion after the ADC. Receive-side DSP consuming more than 50% of total link power is not rare. The bottleneck is still analog: climbing baud, circuit noise, non-ideal transmission lines, and clock jitter on the converters.

From 224G the analog problem leaves the die. Panasonic Megtron 6, a workhorse high-speed board material, specifies properties only to 10 GHz — above that is RF territory. A 224G signal's fundamental already sits near 56 GHz. Once the fundamental crosses 50 GHz, every package/board trace, via, and connector contact acts as both antenna and filter. A "good SerDes IP" is then insufficient; chip, package, and board have to be designed as one system, and the gap between teams that have done this and teams that have not is described as stark. That is why recruiter demand in the CPO era is for analog designers, and why NVIDIA, Marvell, Intel, and Cadence SerDes postings (viewed 2026-08) cluster at Senior / Staff / Principal with almost no junior seats — a market that poaches rather than trains. Qualcomm buying Alphawave is the corporate version of the same move: acquire the SerDes IP shop, restock the roster overnight.

Copper still occupies the short reach, and that reach is shrinking with frequency. OIF copper-cable objectives are about 2 m at 112G and 1 m at 224G; a server rack is ~2 m tall, so 224G already struggles to span a single rack on copper alone. OIF system power targets put energy per bit at ~0.7 pJ inside a package (a few cm) and ~3.5 pJ over a ~1 m board path. Optical modules fill the ground copper surrenders, in a sequence the market already knows: faceplate pluggables → LPO (module DSP removed) → CPO (optical engine attached beside the switch chip). Two blocks never leave any of those diagrams: the SerDes and the electrical-optical converter — microphones and speakers of the audio analogy. LPO cuts power by deleting the module DSP and handing electrical-path recovery to the host SerDes; the distortion being corrected is not in the fiber (near-lossless at these distances) but in the ~20 cm of board copper from switch ASIC to faceplate. CPO shrinks that stretch to millimetres, so a lighter DSP inside the SerDes can replace the heavy module DSP. NVIDIA materials: of the ~30 W a pluggable draws, ~20 W is the module DSP; CPO does the same job in 9 W. The chip sold as an "optical DSP" is the same family as the host-SerDes DSP — it restores the electrical signal on both sides of the E/O conversion and also corrects laser / modulator / receiver bandwidth limits — which is why firms that are good at SerDes become the optical-DSP names. Host-SerDes DSP survives path-shortening; the module DSP whose job was the chip-to-module copper is the piece that disappears. NVIDIA's published 102.4-terabit-class CPO switch lists 512 lanes: the high-speed electrical lanes moved inside the package, they were not deleted. Ayar Labs' TeraPHY is introduced as "a retimer that cleans up the electrical signal and hands it over to the optical link" — SerDes in front of the optical link as the flagship product. WDM does not retire serialization either: the next-generation IEEE spec carries 800 G on four wavelengths over one fiber, and each wavelength still carries 224G-class serialized data (~200 Gbit/s). Four wavelengths is a cost compromise (a full laser + modulator + receiver set per λ), not a SerDes-off switch. The investor filter this part actually leaves is not "buy the best SerDes company" — engine-blueprint shops rarely capture the car's economics. The question deferred to Part 2 (13 companies) is who converts SerDes skill into money, and how: in systems, in products, in components.

## Framework / Mental Model

Nutty names three devices, not a scoring sheet.

| Device | Components | How it is applied |
|---|---|---|
| **Analog–digital sliding scale** | NRZ (2 levels, 1 bit) → PAM4 (4 / 2) → PAM6 → PAM8 | More levels raise bits/symbol and shrink recoverable margin. OIF noise-margin deltas (PAM6 +3.6 dB, PAM8 +6.1 dB vs PAM4; PAM8 = 4× SNR) are the quantitative test of whether a next-gen lane rate can leave PAM4. |
| **Architecture stack with two persistent blocks** | Faceplate pluggable → LPO → CPO → optical I/O (Ayar-class) | At every generation, SerDes + E/O converter remain. What *moves* is where the heavy DSP sits and how long the electrical stub is (~20 cm board → millimetres). Forecast a vendor by matching its focus (module DSP vs host SerDes vs retimer vs laser) to which of those pieces shrinks. |
| **Monetization typology (engine vs car)** | Systems / products / components | "Best SerDes IP" is the engine blueprint. The investable object is who converts the skill into a finished system (switch / GPU rack), a product (optical DSP, CPO switch), or a component — the question Part 2 applies to 13 companies. |

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Lane rates | 112G/lane in service; crossing to 224G/lane; 448G/lane in development | [1×: Nutty / industry] |
| 112G definition | 1 lane = 112 billion bits/s | [1×: Nutty] |
| Modulation in service | 112G and 224G links all PAM4 (2 bits/symbol vs NRZ 1 bit) | [1×: Nutty] |
| Next-gen modulation | PAM6 probed for 448G; ISSCC papers on higher level counts yearly | [1×: Nutty / ISSCC] |
| PAM6 vs PAM4 noise margin | +3.6 dB at same error rate | [1×: OIF via Nutty] |
| PAM8 vs PAM4 noise margin | +6.1 dB at same error rate | [1×: OIF via Nutty] |
| PAM8 vs PAM4 SNR | 4× SNR (double signal or halve noise) | [1×: OIF via Nutty] |
| Converter topology | DAC-based serializer; ADC-based deserializer | [1×: Nutty] |
| RX DSP power share | Often >50% of total link power | [1×: Nutty] |
| Board-material spec ceiling | Panasonic Megtron 6 datasheet properties only to 10 GHz | [1×: Panasonic via Nutty] |
| 224G fundamental | ~56 GHz (already past the 50 GHz "antenna/filter" line) | [1×: Nutty] |
| Copper reach (OIF) | ~2 m @ 112G; ~1 m @ 224G | [1×: OIF via Nutty] |
| Rack height vs copper | Server rack ~2 m → 224G copper struggles to span one rack | [1×: OIF / Nutty] |
| Energy/bit (OIF system targets) | ~0.7 pJ in-package (few cm); ~3.5 pJ over ~1 m board | [1×: OIF via Nutty] |
| Faceplate copper stub | ~20 cm switch-ASIC-to-module; CPO shrinks to millimetres | [1×: Nutty] |
| Pluggable vs CPO module power | ~30 W pluggable, of which ~20 W is module DSP; CPO ~9 W | [1×: NVIDIA via Nutty] |
| 100K-server transceiver draw | 2.3 MW traditional cloud vs 40 MW AI factory | [1×: NVIDIA via Nutty] |
| NVIDIA FY26 mix | Compute-chip revenue +59%; networking +142% | [1×: NVIDIA FY26 AR via Nutty] |
| NVIDIA 102.4T CPO switch | Spec lists 512 electrical lanes (moved inside the package) | [1×: NVIDIA via Nutty] |
| IEEE next-gen WDM | 800 G on 4 wavelengths / fiber; each λ is 224G-class (~200 Gbit/s) serialized | [1×: IEEE 802.3 via Nutty] |
| Optical I/O framing | Ayar Labs TeraPHY = retimer that cleans the electrical signal into the optical link | [1×: Ayar via Nutty] |
| Talent market (2026-08) | NVDA / MRVL / INTC / CDNS SerDes postings almost all Senior / Staff / Principal | [1×: company career boards via Nutty, viewed 2026-08] |
| Roster M&A | Qualcomm acquired Alphawave (SerDes IP) to restock analog/SerDes designers | [1×: QCOM / Nutty] |
| Part 2 scope | 13 companies mapped on systems / products / components | [1×: Nutty] |

## Contradiction Check

Supports [[Theses/NVDA - Nvidia]] §Networking and the Spectrum-X/Quantum-X CPO catalyst: FY26 networking +142% vs compute +59% is the source's exhibit that interconnection, not just FLOPs, is the growth vector, and the 102.4T / 512-lane CPO spec is the same "lanes moved inside the package" claim. Challenges the naive reading of Risk #10 (SerDes plateau / copper ~2 m reach wall) as "CPO deletes electrical content." Nutty's 1 m @ 224G OIF reach and 56 GHz fundamental *agree* that copper scale-up is hitting a wall; they disagree that the wall retires SerDes — CPO relocates 512 lanes onto the package and still needs DAC/ADC + a lighter SerDes DSP. 448G + PAM6 remaining "under continuous development / keep knocking" is consistent with Risk #10's "true 448G uni-directional uncertain" hedge; it is not a resolution. [G-14] hypothesis: 30 W → 9 W per module is interconnect-energy deflation that *raises* bits moved, not a demand shrink.

Supports [[Theses/AVGO - Broadcom]] Key Non-consensus Insight #3 (in-sourcing overstated because hyperscalers still rent 224G SerDes, memory controllers, packaging). The 224G+ "chip + package + board as one system" claim and the senior-only talent market are the mechanism under that insight: the scarce layer is analog/SerDes *plus* RF-frequency physical design, not a downloadable IP block. VLM §1 talent-gravity and Semis #2 qualification-gate (teams that have shipped 224G co-design vs those that have not) fire as hypotheses, not as a Broadcom monopoly verdict — Nutty explicitly refuses the "buy the best SerDes company" collapse and defers winner-picking to Part 2.

Challenges the *duration* of [[Theses/MRVL - Marvell Technology]] Insight #4 / Outstanding Question #5 / → LOW if OFC 2027 shows >35% 1.6T short-reach share loss from DSP to LPO. Nutty's stack says LPO hands recovery to the *host* SerDes and CPO deletes the module DSP whose job was the 20 cm stub — the exact piece Marvell monetises as "optical DSP" (80%+ 800G, Nova/Ara 1.6T). That is supportive of the thesis's own cannibalisation math (module-DSP GM ~65% → LPO-blend ~55%) and of Semis #14 as a reclassification risk on the owned electro-optics layer. It does **not** kill long-reach / coherent DSP (fiber + device bandwidth still need reconstruction) and does **not** pick Photonic Fabric vs switch-CPO. Falsifier Nutty himself plants: if optical I/O (Ayar-class retimer-in-front-of-fiber) eliminates the *host* SerDes earlier than the "microphones and speakers remain" analogy allows, the persistence claim is wrong.

Orthogonal to [[Theses/LITE - Lumentum]] Insight #3 (SiPh/CPO raises InP laser demand) and directly relevant to Outstanding Question "How does Lumentum's role change under CPO" / Risk #3 (CW/SHP narrower than EML). Nutty's persistent block on the optical side is the E/O converter, not the SerDes; LITE sells the light source that converter consumes. The source does not discuss EML vs CW ASP, so it cannot resolve whether CPO volume offsets LITE's module-margin loss. No ALAB thesis exists in `/Theses` — Astera-style AEC/retimer is the product analog of Ayar's "SerDes in front of the link," left as an open mapping for Part 2.

Models agreed on SerDes persistence + interconnect as an infrastructure toll → disconfirm: (i) 448G slips or freezes on PAM4, stalling the lane-rate treadmill that funds analog scarcity; (ii) module-DSP disappearance prints in MRVL OFC 2027 share/GM before host-SerDes content offsets it; (iii) optical I/O collapses the host SerDes the source says never leaves. Base rate: engine-blueprint businesses are acquired (Alphawave) rather than compounded as public layer monopolies — that is the outside view [G-10] against any "own SerDes, own the stack" read.

## Source Excerpts

> "by an NVIDIA ($NVDA) estimate, in the same 100K-server-class datacenter, the transceivers (optical modules) draw 2.3 MW in a traditional cloud and 40 MW in an AI factory."

> "The standards body OIF calculates that, holding the same error rate, PAM6 requires 3.6 dB more noise margin than PAM4, and PAM8 requires 6.1 dB more. PAM8 needs 4x the SNR (Signal-to-Noise Ratio) of PAM4."

> "The copper-cable reach objectives OIF has set by speed generation run about 2 m at 112G and 1 m at 224G. … By OIF’s system power targets, the energy to send one bit is about 0.7 pJ inside a package (a few cm) but climbs steeply to about 3.5 pJ over a board path of about 1 m."

> "Per NVIDIA’s materials, of the 30W that one pluggable draws, 20W is the module DSP’s share, while CPO does the same job in 9W."

> "NVIDIA’s published spec for its 102.4-terabit-class CPO switch explicitly lists 512 lanes. The high-speed electrical lanes did not disappear; they only moved from outside the package to inside."

> "We need to sharpen the question beyond ‘who is best at SerDes.’ ‘Who is converting SerDes skill into money, and how: in systems, in products, in components?’"
