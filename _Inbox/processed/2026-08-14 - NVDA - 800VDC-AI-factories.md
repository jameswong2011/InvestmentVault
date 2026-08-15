---
publish: false
title: 'NVIDIA Ditches AC Power For 800 VDC AI Factories, Backed By Microsoft, Google and 80 Firms For 2H 2026'
source: 'https://wccftech.com/nvidia-800-vdc-platforms-break-past-traditional-power-distros-to-scale-up-performance/'
date: 2026-08-14
article_date: 2026-08-13
tags: [daily-intel-triage, news]
holdings: [NVDA]
---

# NVIDIA Ditches AC Power For 800 VDC AI Factories, Backed By Microsoft, Google and 80 Firms For 2H 2026

Source: https://wccftech.com/nvidia-800-vdc-platforms-break-past-traditional-power-distros-to-scale-up-performance/

Why it matters: NVDA: 800 VDC OCP architecture with MSFT/GOOGL + 80 firms; Rubin MGX racks already in production for 2H26; 2027 row-power / Kyber path.

## Extracted body

# NVIDIA Ditches AC Power For 800 VDC AI Factories To Scale Up Compute

**Source:** [Wccftech](https://wccftech.com/nvidia-800-vdc-platforms-break-past-traditional-power-distros-to-scale-up-performance/) — Hassan Mujtaba

NVIDIA is spearheading the race to roll out its first 800 VDC platforms with the backing of Google & Microsoft in the second half of this year.

As Datacenters continue to outstrip electricity generation, the need for more power-efficient & versatile solutions has become essential. This is why major companies like NVIDIA, Microsoft & Google have invested heavily in 800V DC or HVDC (High-Voltage Direct Current) infrastructure to power their upcoming AI platforms.

The push towards DC over AC power is plain and simple. AC power presents various overheads as the current is converted multiple times, which adds to the complexity of denser AI platforms. As next-generation AI factories continue to grow in power demand, these inefficiencies compound & lead to huge bottlenecks in performance scaling.

800 VDC, on the other hand, uses a higher voltage through DC power, requiring fewer conversion stages between the grid and the GPUs. This means that more power can reach the accelerator & in return, that offers higher performance. For this, NVIDIA has laid out its DSX reference designs that offer AI factories to transition from AC to "fully native 800 VDC" setups.

As a result, NVIDIA has partnered with Google and Microsoft to develop the industry's first 800 VDC architecture through the Open Compute Project (OCP) platform, and is backed by a tally of 80 equipment/infrastructure companies who are already building products based on the new specifications and have laid out a trajectory to roll out the first platforms in the second half of 2026.

“800 VDC unlocks the compute performance and power density required for AI at scale,” said Vladimir Troy, vice president of data center infrastructure at NVIDIA. “Through OCP, NVIDIA is working with more than 80 ecosystem companies to give AI factories a practical path forward — not just a future vision.”

Shifting to DC infrastructure is also important to address the growing power bottleneck. As per the latest IEA report, data center electricity consumption grew 17% in 2025, with AI facilities gobbling up 50%. Global consumption is estimated to double to almost 950 TWh by 2030, and to meet that demand, an infrastructure investment of almost $9 trillion will be required through 2040.

Wood Mackenzie projects $9 trillion in global AI and data infrastructure investment through 2040. The facilities that can absorb that investment will be the ones that resolved their power architecture before compute demand outran what their infrastructure could deliver. NVIDIA, Google and Microsoft are working with the broader ecosystem to make sure 800 VDC is ready when operators need it — and that existing facilities have a path to get there now.

According to the latest reports from Taiwan's industry sources, NVIDIA's Rubin MGX platforms based on the 800 VDC power architecture are already in production and will be rolling out in the second half of 2026.

The biggest benefit of the 800 VDC MGX racks is that customers don't need to invest in any major changes to their existing setups, and the DC platforms can be integrated directly into AC platforms. Some salient features of this approach include:

- Leverage existing AC infrastructure and investments
- Avoid disruption to established supply chains and operational practices
- Adopt 800 VDC incrementally, based on application needs and deployment timelines, while aligning future infrastructure with next-generation AI compute requirements

| Topic | AC System Behavior | DC System Behavior | Key Consideration |
| --- | --- | --- | --- |
| Fault Current | Alternating current fault current is limited by system impedance and naturally oscillates. | Direct current fault current can be very high and sustained due to lack of zero crossing. | DC faults can be more severe and harder to interrupt. |
| Fault Energy | Energy dissipates over cycles; fault clearing benefits from current zero crossings. | Energy is continuous; no natural zero crossing to aid interruption. | DC systems require faster and more robust interruption methods. |
| Shock Hazard | AC shocks can cause muscle contraction and fibrillation; severity depends on frequency. | DC shocks cause continuous muscle contraction; can be harder to let go. | DC shock hazards may be more dangerous due to sustained current flow. |
| Protection Devices | Circuit breakers and fuses are widely available and standardized for AC. | DC protection devices are specialized and more complex. | DC protection requires advanced technology and design. |
| Ground Fault Detection | Easier to detect due to alternating nature of current. | More difficult to detect; requires sensitive monitoring. | DC systems need advanced ground fault detection schemes. |
| Series Arcing | AC arcs extinguish naturally at zero crossings. | DC arcs can persist without zero crossings. | DC systems are more prone to sustained series arcing. |
| Parallel Arcing / Arc Flash | AC arc flashes are intense but self-extinguish more readily. | DC arc flashes can be more sustained and harder to extinguish. | DC arc flash hazards are more severe and require stronger mitigation strategies. |

NVIDIA is also accelerating its DC roadmap with a dedicated solution for AI factories. This solution is called a "row power center" and is essentially a centralized power station for a full rack row that uses an overhead 800 VDC busway to scale power distribution across multiple rack rows and supports up to 2 MW of power per row. This solution is expected in 2027. This architecture will also scale to next-gen Rubin Ultra and Feynman platforms on the Kyber racks, which are scheduled for next year.

By cutting AC conversion losses, 800 VDC delivers more power directly to the GPUs, breaks through the “power wall,” and enables higher density and performance. The first platforms—including NVIDIA’s Rubin MGX systems, are already in production and set to roll out in the second half of 2026, with a practical path that lets operators leverage existing AC infrastructure and adopt DC incrementally.
