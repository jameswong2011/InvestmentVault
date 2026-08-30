---
publish: false
title: "NVIDIA NVLink Fusion Expands With NVHBM Custom High-Bandwidth Memory"
url: "https://blogs.nvidia.com/blog/nvlink-fusion-nvhbm-custom-high-bandwidth-memory"
source: NVIDIA Blog
date: "2026-08-27"
why_selected: "Holdings NVDA/000660/AVGO/MRVL: NVHBM moves the memory controller into the HBM base die — claimed +30% BW, -15% HBM power, +25% XPU area vs standard HBM4E; Annapurna first collaborator; Trainium4 on NVLink Fusion."
tags:
  - daily-intel-triage
  - NVDA
  - 000660
  - AVGO
  - MRVL
  - HBM
---

# NVIDIA NVLink Fusion Expands With NVHBM Custom High-Bandwidth Memory

Source: [NVIDIA Blog](https://blogs.nvidia.com/blog/nvlink-fusion-nvhbm-custom-high-bandwidth-memory) — Jesse Clayton, 26 August 2026

Amazon's Annapurna Labs will be the first to collaborate on NVHBM technology alongside NVLink Fusion.

The next wave of AI is placing new demands on infrastructure. As AI agents and trillion-parameter workloads become mainstream, the performance of AI infrastructure depends not only on compute, but on how compute, memory, storage, networking and software are designed together as a unified system.

To help hyperscalers and AI innovators build the next generation of semi-custom AI infrastructure, NVIDIA today expanded NVIDIA NVLink Fusion with NVIDIA NVHBM, a next-generation high-bandwidth memory technology that brings higher memory performance and efficiency to XPUs. It will be validated and offered by leading memory partners, extending this advanced memory capability to NVLink Fusion customers.

Traditional HBM architectures place the memory controller on the XPU die, consuming valuable silicon area that could otherwise be dedicated to compute. NVHBM, built on the same technology that NVIDIA will use for future GPUs, integrates NVIDIA's custom memory controller into the HBM base die. By integrating the memory controller into the 3D HBM stack instead of the XPU, NVHBM delivers up to 30% greater memory bandwidth and 15% lower HBM power consumption, and frees up to 25% more area on XPU compute die compared with standard HBM4E.

NVIDIA is establishing a standard NVHBM implementation, available from multiple memory providers. This reduces the engineering effort required to integrate and qualify memory across multiple suppliers — giving NVLink Fusion customers a faster path for bringing custom AI chips to market.

Amazon's Annapurna Labs will be the first to work on NVHBM as part of its broader collaboration with NVIDIA around NVLink Fusion.

## AWS and NVIDIA Continue NVLink Fusion Collaboration

Amazon's Annapurna Labs will work with NVIDIA on NVHBM technology and the NVLink scale-up architecture to enhance performance and efficiency for AI workloads. This builds on AWS's previously announced support for NVLink Fusion. Annapurna Labs will support NVLink Fusion with its next-generation Trainium chips starting with Trainium4, which would allow Amazon chips and NVIDIA GPUs to work together with common rack-scale architecture.

"NVHBM represents a new architectural approach to advancing high-bandwidth memory performance and efficiency," said Nafea Bshara, vice president of Annapurna Labs at Amazon. "We look forward to this technology collaboration to benefit future AWS infrastructure designs."

## Vertically Integrated and Horizontally Open

NVLink Fusion enables partners to connect custom XPUs and CPUs to NVIDIA's rack-scale platform. Partners can access NVIDIA NVLink chiplets, NVLink-C2C, NVLink Switches and NVIDIA MGX systems and racks, as well as a broad ecosystem of CPU partners, ASIC designers, system manufacturers and technology providers.

Offered with each generation of NVIDIA's rack-scale system architecture, NVLink Fusion allows hyperscalers and AI-native companies to focus engineering resources on XPU innovation while using a proven technology stack for scale-up and scale-out networking, rack-scale systems and software — creating a faster, lower-risk path to deploying semi-custom AI infrastructure.
