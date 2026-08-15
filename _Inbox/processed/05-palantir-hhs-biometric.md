---
publish: false
title: HHS plans nationwide biometric sponsor vetting network linked to Palantir
url: "https://www.biometricupdate.com/202608/hhs-plans-nationwide-biometric-sponsor-vetting-network-linked-to-palantir"
source: Biometric Update
date: "2026-08-14"
why_selected: "PLTR High: HHS/ORR draft PWS wires mobile biometrics + FBI NGI through ORR Horizon (ACF instance of Palantir Foundry) for nationwide sponsor vetting."
tags:
  - daily-intel-triage
  - PLTR
  - govtech
---

# HHS plans nationwide biometric sponsor vetting network linked to Palantir

Source: [Biometric Update](https://www.biometricupdate.com/202608/hhs-plans-nationwide-biometric-sponsor-vetting-network-linked-to-palantir)

Draft procurement combines mobile biometrics, FBI identity checks and continuous sponsor monitoring through a Palantir-based platform.

The U.S. Department of Health and Human Services (HHS) is planning a nationwide biometric identity vetting network for people seeking to sponsor unaccompanied children, linking mobile fingerprint collection, FBI background checks, Palantir-powered case management and continuous open-source monitoring. A draft Performance Work Statement describes an integrated architecture that extends from biometric collection through identity verification and ongoing risk monitoring.

The system could also support biometric collection overseas at locations designated by the Department of Homeland Security (DHS).

The HHS sources sought notice's unusually detailed requirements describe an integrated biometric and identity vetting architecture for ORR's Unaccompanied Children Program.

The contemplated contractor would capture FBI-compliant ten-print fingerprints, take passport quality photographs, scan and authenticate identity documents and associate the resulting records with a single person.

Fingerprint transactions would be constructed under the FBI's Electronic Biometric Transmission Specification (EBTS) and transmitted through the Justice Department's Justice Criminal Information Services/Civil Applicant Systems gateway for searches of the FBI's Next Generation Identification system (NGI). Results would then be returned for use in ORR's sponsor vetting process.

ORR wants appointments made available within three business days and requires fingerprints and photographs for adult sponsors, adult household members and adult caregivers. The draft establishes a release gate under which required background check results must be completed and recorded before ORR approves a child's release.

If repeated fingerprint collection fails quality requirements or an NGI submission is rejected, the system would move to an FBI name-check process. Ink fingerprint cards would provide another fallback when required.

The proposed system reaches considerably beyond fingerprinting.

The biometric contractor would generate foundational identity and biometric information for a larger sponsor vetting ecosystem. The contractor would produce biometric and identity records, NGI results, adjudication information and chain-of-custody data for ORR's government systems.

The PWS calls for those outputs to be integrated through ORRbit, ORR's case-management environment, and another system known as ORR Horizon.

## Palantir connects the identity workflow

HHS records say Horizon is the name the Administration for Children and Families (ACF) gives to its version of Palantir Foundry, a software platform used to bring information from different systems together so it can be organized, analyzed and used in agency workflows.

The draft PWS refers specifically to the "ORR Horizon platform built on Palantir Foundry" and says it is integrated with the ORR Sponsor Vetting application.

The HHS's public AI inventory independently identifies Horizon as the "ACF instance of Palantir Foundry" and lists it as the system associated with an Authority to Operate (ATO) for several ACF initiatives, including projects involving ORR data.

The AI use cases identified in those records were still described as under acquisition or development, rather than implemented, when HHS last updated them.

Palantir Foundry is not itself a fingerprint matching system. It is a data integration and operational analytics platform designed to connect information held in different databases and systems, transform and analyze it, apply software models and make the resulting information available through applications and workflows.

A core component, which Palantir calls its Ontology, organizes underlying data into representations of real-world objects, relationships, events and actions.

In practical terms, it can allow information originating in separate databases to be brought into a common operational environment without requiring users to work through each underlying system independently. That distinction is important in the ORR procurement.

The draft does not say Palantir will perform the FBI fingerprint search, nor does it establish that Palantir will persistently store raw fingerprint images.

The biometric contractor and Justice Department systems would perform the collection and criminal history checking, while ORRbit and Horizon would provide the government-controlled infrastructure through which authorized identity and vetting information can be organized and distributed.

The architecture extends beyond initial identity verification. ORR says Horizon and ORRbit would provide confirmed identity information to a separate contractor performing open source intelligence sponsor monitoring and vetting.

The draft PWS describes that companion contract as not yet awarded and says it would conduct open source identity verification, continuous risk monitoring and risk scoring using confirmed identity attributes such as a unique person identifier, name, date of birth and identity document metadata.

The biometric contractor would not be permitted to directly provide the open source contractor with raw fingerprint images, criminal history information, NGI results, identity document images or other protected sponsor case information.

Instead, selected information must pass through government-controlled systems and application programming interfaces. The contractors are also prohibited from independently creating data-sharing or commercial arrangements involving information produced under the biometric contract without government authorization.

HHS says sponsor suitability determinations and decisions about whether a child is released remain the responsibility of ORR personnel.

The biometric contractor's outputs would also be accessible through government systems to authorized ORR and ACF officials and, for specified purposes, outside federal users including DHS, the Justice Department, the HHS inspector general and the Government Accountability Office.

The procurement comes as information collected through the child sponsor program has become increasingly intertwined with immigration enforcement.

Reuters reported in July that ORR had provided Immigration and Customs Enforcement with more than 460,000 investigative leads involving unaccompanied children, sponsors and other household members since January 2025.

More than 12,000 people had been arrested following ORR tips during President Donald Trump's second term, according to internal government information reviewed by Reuters.

DHS told Reuters the information was being used as part of efforts to locate children placed with what the government described as unvetted sponsors, including people with criminal records.

Concerns about weaknesses in sponsor screening predate the current administration. A 2024 HHS inspector general review found that 16 percent of sampled children's case files lacked documentation showing that one or more required sponsor safety checks had been performed.

Among children released while FBI fingerprint or state child abuse checks remained pending, 19 percent of the files were never updated with the results. Thirty-five percent contained sponsor identity documents with legibility problems.

HHS has subsequently moved toward more extensive sponsor vetting. A proposed rule published June 26 would establish additional identity, financial and background check requirements for potential sponsors and adult household members.

ORR said the changes are intended to strengthen sponsor suitability determinations and address fraud and child safety concerns. The biometric procurement shows how those policies could be implemented technologically and at scale.

Every biometric transaction would carry an auditable chain of custody recording information including the collecting device and operator, location and timestamps, quality measurements, submission identifiers and adjudication events.

The PWS calls for immutable audit logs and government access to operational and analytical reporting.

The procurement also contains an optional rapid-DNA component. If ORR activates it, technicians could collect cheek swabs when the government determines that biological kinship needs to be verified.

The draft places explicit restrictions around the DNA. Samples and associated testing material would have to be destroyed after the government receives and accepts the results. Neither the contractor nor its laboratories could upload or cross-reference DNA profiles with the FBI's Combined DNA Index System, other law enforcement databases or commercial genealogy databases.

ORR describes the purpose as administrative kinship verification. The requirements also contemplate possible AI functions for biometric quality assessment, identity matching, fraud detection, EBTS validation and exception detection.

Those capabilities would have to remain disabled by default and could not be activated without prior government approval. Any approved AI function would be subject to requirements involving human review, explainability, documentation and bias monitoring.

Biometric Update reported in 2020 that sponsor fingerprinting itself was not new. Earlier DHS-HHS information sharing arrangements required ORR to fingerprint potential sponsors and certain adult household members so federal agencies could conduct criminal history and other checks.
