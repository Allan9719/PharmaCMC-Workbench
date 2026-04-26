> 📖 基于 ICH Q5/Q6 系列及行业实践整理，生物类似药对比数据请以实际产品研究为准。

## 10. Process Validation

### 10.1 FDA 2011 Lifecycle Approach — Three Stages

**Stage 1 — Process Design:**
- DoE to characterize CPP–CQA relationships
- Establish PAR (Proven Acceptable Range) and NOR (Normal Operating Range)
- Define design space and control strategy
- Technology transfer package
- Deliverables: Process development report, risk assessments, design space documentation

**Stage 2 — Process Qualification:**

*Equipment Qualification:*

| Phase                           | Purpose                                                                  |
| ------------------------------- | ------------------------------------------------------------------------ |
| DQ (Design Qualification)       | Verify proposed design meets URS                                         |
| IQ (Installation Qualification) | Equipment installed per specs, utilities connected, calibrations current |
| OQ (Operational Qualification)  | Equipment operates correctly across range under no-load conditions       |
| PQ (Performance Qualification)  | Equipment performs reproducibly under production conditions              |

*Process Performance Qualification (PPQ):*
- Typically 3 consecutive successful commercial-scale batches (scientific justification for number)
- Enhanced sampling (more locations, more tests, more in-process data)
- Prospective protocol with pre-defined acceptance criteria
- Statistical analysis: Process capability Ppk ≥ 1.33 for critical attributes
- All batches must meet all criteria; PPQ report with deviations documented

*Cleaning Validation:*
- Demonstrate removal of product residues, cleaning agents, and microorganisms
- Acceptance criteria: (1) 0.1% therapeutic dose carryover, (2) 10 ppm, or (3) visually clean — most conservative applied
- For potent APIs: Health-Based Exposure Limits (HBELs) using PDE values
- Sampling: Swab (preferred, quantitative) + rinse (hard-to-reach areas)
- 3 consecutive successful cycles; dirty/clean hold time studies

**Stage 3 — Continued Process Verification:**
- SPC charts for CPPs and CQAs (X-bar/R, individuals/moving range)
- Ongoing Cpk trending
- Annual Product Quality Review (APQR): batch data, deviations, OOS/OOT, CAPA, complaints, stability
- Revalidation triggers: equipment change, site change, adverse trends

### 10.2 Sterile Product Validation

- **Media fills**: Fill with TSB under production conditions; minimum 3 consecutive successful fills; ≥5,000 units; repeat semi-annually; acceptance: 0 contaminated units for <5,000 units
- **Filter validation**: Bacterial challenge (B. diminuta ≥10⁷ CFU/cm²) for 0.2 µm filters; integrity testing pre- and post-use
- **Environmental monitoring**: Viable and non-viable particles during fills
- **Hold time studies**: Bioburden/endotoxin limits for bulk solution, filtered solution, filled product

---

## 11. Clinical Trial Phases as CMC Triggers

This is the critical section: **how clinical trial data triggers CMC activities throughout the drug development lifecycle.**

### 11.1 Master Trigger Map

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    CLINICAL-TO-CMC TRIGGER TIMELINE                             │
│                                                                                 │
│  DISCOVERY ──► PRE-IND ──► PHASE I ──► PHASE II ──► PHASE III ──► NDA ──► POST │
│                                                                                 │
│  CMC Activities:                                                                │
│  ├── Initial route ─► Process optimization ─► Process lock ─► Validation ─► CPV │
│  ├── Tox batch ──► Clinical supply ──► Scale-up ──► Registration batches ──►    │
│  ├── Pre-form ──► Formulation dev ──► Commercial form ──► Stability ──────►     │
│  ├── Method dev ──► Qualification ──► Validation ──► Transfer ──► Lifecycle     │
│  └── Preliminary specs ──► Refined specs ──► Final specs ──► Justified ────►    │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 11.2 Pre-Clinical / Pre-IND CMC Activities

**Regulatory framework:** 21 CFR 312.23(a)(7), FDA guidance "INDs for Phase 1 Studies" (1995).

**What must be done before any clinical trial begins:**

| CMC Area           | Pre-IND Requirement                                                                                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Drug Substance     | Defined reproducible process (not necessarily optimized), structural characterization (NMR, MS, IR, UV, XRPD), preliminary impurity profile qualified against tox batch |
| Drug Product       | Simple preliminary formulation (powder-in-capsule, simple solution), adequate for intended route                                                                        |
| Analytical         | Fit-for-purpose methods — suitable but not fully validated; identity, purity, potency, key safety impurities                                                            |
| Specifications     | Wide, preliminary, justified based on tox batch data                                                                                                                    |
| Stability          | 1-3 months accelerated + any available real-time data — enough to cover planned Phase I duration                                                                        |
| Reference Standard | Characterized sufficiently to serve as reference for release/stability                                                                                                  |

**The Tox Batch Bridge:** Clinical material must be comparable to (or higher purity than) the GLP toxicology batch. Key comparability: impurity profiles, potency, physical form.

**Timeline:** 12-24 months from candidate selection to IND filing.

### 11.3 Phase I → CMC Triggers

**GMP requirements (FDA guidance "CGMP for Phase 1 Investigational Drugs," 2008):**
- Risk-proportionate, reduced GMP vs. commercial
- Process need not be validated; must be defined, documented, and controlled
- Methods need not be fully validated — "scientifically sound and suitable"
- Quality unit must be in place; personnel trained
- Batch records required; deviation management, though less formal

**Phase I clinical data triggers:**

| Clinical Data                 | CMC Action Triggered                                                                                                 |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Unexpected toxicity**       | Reformulation (excipient switch, pH adjustment, salt form change), reassess impurity profile                         |
| **Injection site reactions**  | Modify DP formulation (buffer, tonicity, surfactant)                                                                 |
| **Poor oral bioavailability** | Enable formulation: particle size reduction, amorphous solid dispersion, lipid formulation, salt/cocrystal screening |
| **High PK variability**       | Evaluate food effects → may trigger enteric coating or modified-release                                              |
| **Half-life data**            | Decision on immediate-release vs. modified-release                                                                   |
| **Dose-proportionality**      | Determines range of dosage strengths needed                                                                          |
| **Dose range for Phase II**   | Determines batch size requirements and number of strengths                                                           |
| **Narrow therapeutic window** | Tighter DP specifications (content uniformity, dissolution)                                                          |

**Concurrent CMC activities during Phase I:**
- Drug substance process optimization (yield improvement, problematic reagent removal)
- Salt/polymorph screening and selection
- Pre-formulation studies (excipient compatibility)
- Analytical method development and initial validation
- Initiation of long-term stability studies

### 11.4 Phase II → CMC Triggers (The Pivotal Investment Decision)

**Phase IIa (Proof of Concept) — the single most important CMC trigger:**

Positive proof-of-concept triggers massive CMC investment:
- Scale-up from lab/pilot (1-10 kg) to intermediate/commercial scale (10-100+ kg)
- Technology transfer from development to commercial manufacturing site
- Investment in dedicated manufacturing equipment
- Process characterization studies initiated
- Commercial site selection and qualification begins

**Phase IIb (Dose Optimization) — the most critical clinical-to-CMC trigger:**

| Clinical Data                         | CMC Action Triggered                                                                  |
| ------------------------------------- | ------------------------------------------------------------------------------------- |
| **Final dose selection**              | Determines commercial dosage strength(s) — arguably the most impactful single trigger |
| **Dose-response data**                | Single vs. multiple strengths decision                                                |
| **Dosing regimen** (QD, BID, weekly)  | Drives formulation strategy (IR, CR, depot)                                           |
| **Route of administration confirmed** | Locks in formulation approach                                                         |

**Process development triggered by Phase II:**
- Drug substance: Final route selection, starting material selection, CPP identification
- Scale-up: Often from 1-10 kg to 10-100 kg (new unit operations may be introduced)
- QbD/DoE: Design space mapping per ICH Q8(R2)
- PAT evaluation initiated
- Formulation transitions from "fit-for-purpose" to "intended commercial formulation"
- Bioequivalence bridging may be needed if formulation changed significantly from Phase I

**Regulatory considerations:**
- IND amendments (21 CFR 312.31) required for significant CMC changes
- FDA guidance "IND Applications — Preparing for Phase 2/3 Studies" (2003) sets expectations: more complete characterization, updated impurity profiles, preliminary method validation, expanded stability

**Timeline:** Phase II CMC activities typically span 2-3 years — the most intensive period of CMC development.

### 11.5 Phase III → CMC Triggers (Commercial Readiness)

**Critical principle:** Sponsors aim to lock the commercial process BEFORE pivotal Phase III trials begin, because any significant post-Phase III process change may require bridging studies.

**Phase III triggers:**

| Activity                                | Trigger                         | Deliverable                             |
| --------------------------------------- | ------------------------------- | --------------------------------------- |
| Process Design completion (Stage 1)     | Phase II data + risk assessment | Design space, CPP/CQA linkage           |
| Equipment/Facility qualification        | Commercial site selected        | Full IQ/OQ/PQ                           |
| Process Performance Qualification (PPQ) | Process locked                  | ≥3 consecutive commercial-scale batches |
| Registration batches                    | PPQ complete                    | Batches for NDA Module 3 + stability    |
| Full method validation                  | Commercial methods ready        | ICH Q2 validation reports               |
| Cleaning validation                     | Multi-product facility          | 3 consecutive cleaning cycles           |
| Stability program                       | Registration batches            | ICH Q1A protocol initiated              |
| Supply chain                            | Commercial scale confirmed      | Multi-source vendor qualification       |
| Commercial specifications               | Batch data + development data   | Justified per ICH Q6A/Q6B               |

**Registration batch requirements:**
- Minimum 1, typically 3 batches at proposed commercial scale (or justified pilot ≥1/10th commercial)
- Final commercial process, final site, commercial-grade materials, final container closure
- Stability initiated per ICH Q1A(R2): 25°C/60% RH and 40°C/75% RH minimum

**Stability data at NDA filing:** 6 months accelerated + 12 months long-term (minimum from 3 batches).

### 11.6 NDA/BLA Submission — CMC Requirements

The complete CMC package in CTD Module 3 includes:
- Full process description with validation data
- Full analytical method descriptions with validation
- Batch analyses for clinical, registration, and any commercial batches
- Complete stability data with shelf-life proposal
- Specifications with scientific justification
- Container closure system with E&L data
- Post-approval stability commitment
- For biologics: cell bank characterization, viral safety package, comparability data

### 11.7 Post-Approval — CMC Activities Triggered by Market Data

| Market Data/Event                              | CMC Activity Triggered                                 |
| ---------------------------------------------- | ------------------------------------------------------ |
| Commercial manufacturing experience (CPV data) | SPC trending, process improvements, APQR               |
| Stability failures/OOS                         | Investigation, potential recall, reformulation         |
| Patient feedback (e.g., swallowing difficulty) | New dosage form development (pediatric, ODT)           |
| Supply chain disruption                        | Alternate supplier qualification, site transfer        |
| Cost optimization                              | Process improvements, yield optimization, site changes |
| New indication (different dose/route)          | New formulation development, new stability studies     |
| Patent expiry preparation                      | Technology transfer to new sites                       |
| Regulatory requirement changes                 | Nitrosamine assessment, elemental impurity testing     |

---

## 12. CMC Strategy and Planning

### 12.1 CMC Development Plan — Phase-Aligned

| Gate                 | Key CMC Decision                                                                     | Go/No-Go Criteria                                                          |
| -------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Pre-IND              | Synthetic route feasible? Formulation viable? GLP material available?                | Process produces quality material; tox batch acceptable                    |
| Phase I Start        | GMP material manufactured? IND CMC complete?                                         | Release specs met; stability supports trial duration                       |
| Phase I → Phase II   | Process scalable? Formulation suitable?                                              | No showstopper impurities; bioavailability adequate                        |
| Phase II → Phase III | Process locked? Commercial form selected? Methods validation-ready? Site identified? | Process characterized; design space defined; commercial formulation stable |
| Pre-NDA/BLA          | Process validated? Stability supports shelf life? Module 3 complete?                 | PPQ successful; ≥12 months stability; specs justified                      |

### 12.2 CMC Investment and Cost

| Development Phase                 | Small Molecule CMC Cost | Biologic CMC Cost |
| --------------------------------- | ----------------------- | ----------------- |
| IND-enabling (Pre-Phase I)        | $2-5M                   | $5-15M            |
| Phase I-II                        | $5-15M                  | $15-50M           |
| Phase III to NDA                  | $10-30M                 | $50-200M          |
| Commercial facility               | $50-200M                | $200M-$2B         |
| **Total CMC as % of development** | **15-25%**              | **30-50%**        |

Cell/gene therapy CMC can be 40-60% of total development cost.

### 12.3 Parallel vs. Sequential Activities

**Parallel (higher cost, faster):**
- Formulation development simultaneous with API process optimization
- Long-term stability while continuing process characterization
- Building commercial suites during Phase II (high-risk, done for breakthrough therapies)
- Qualifying backup manufacturing sites during pivotal trials

**Sequential (lower cost, slower):**
- Wait for final API process before formulation development
- Complete process validation only after Phase III feedback
- Single-site development → then technology transfer

**COVID-19 example:** Moderna and Pfizer/BioNTech ran CMC development almost entirely in parallel with clinical trials — manufacturing at-risk at commercial scale during Phase III. Operation Warp Speed funded this parallel approach, compressing the typical 10+ year timeline to under 1 year.

### 12.4 Platform Approaches

For well-established modalities (monoclonal antibodies, ADCs), platform manufacturing processes and analytical methods can save 1-2 years of development time:
- Standardized cell culture conditions
- Standard purification trains (Protein A → low pH viral inactivation → CEX/AEX → viral filtration → UF/DF)
- Pre-validated analytical method suites
- Pre-qualified container closure systems

---

## 13. Regulatory Interactions for CMC

### 13.1 FDA Meeting Types

| Meeting Type | Purpose                                 | Response Timeline | Meeting Timeline |
| ------------ | --------------------------------------- | ----------------- | ---------------- |
| Type A       | CRL resolution, clinical holds          | 30 days           | 60 days          |
| Type B       | Pre-IND, EOP2, Pre-Phase 3, Pre-NDA/BLA | 60 days           | 75 days          |
| Type C       | All other meetings                      | 60 days           | 75 days          |
| Type D       | Written response only                   | Variable          | No meeting       |

### 13.2 Key CMC Topics by Meeting

**Pre-IND Meeting:**
- Synthetic route acceptability, impurity control strategy
- Formulation suitability for FIH
- Specifications adequacy
- Stability data requirements
- For biologics: cell bank characterization, viral clearance strategy

**End-of-Phase 2 Meeting (most important CMC regulatory interaction):**
- Process development status — ready for registration batches?
- Commercial formulation acceptability; bridging studies needed?
- Commercial specifications justified?
- Process validation approach
- Facility readiness
- Comparability for process changes (Phase I/II → Phase III)

**Pre-NDA/BLA Meeting:**
- Module 3 completeness and format
- Outstanding CMC deficiencies
- Process validation status
- Pre-approval inspection (PAI) timing
- Comparability protocols for anticipated post-approval changes

### 13.3 Accelerated Pathways — CMC Implications

| Designation              | CMC Impact                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Breakthrough Therapy** | More frequent CMC meetings, rolling submission, concurrent validation may be accepted, less stability data at filing with commitments |
| **Accelerated Approval** | CMC requirements generally not reduced; some flexibility on stability data                                                            |
| **Priority Review**      | 6-month review clock; PAI must complete within shorter window; CMC readiness critical at filing                                       |
| **Fast Track**           | Rolling review; more CMC interactions                                                                                                 |

---

## 14. Post-Approval CMC Changes and Lifecycle Management

### 14.1 FDA Post-Approval Change Framework

**SUPAC (Scale-Up and Post-Approval Changes) — Change Levels:**

| Level       | Impact                             | Reporting                           | Examples                                                                                                                          |
| ----------- | ---------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Level 1** | Unlikely to affect quality         | **Annual Report**                   | ≤10× batch size (non-sterile), same-design equipment, editorial batch record changes                                              |
| **Level 2** | Could have significant impact      | **CBE-30**                          | Moderate process changes, moderate batch size changes, equipment changes (different operating principle), same-campus site change |
| **Level 3** | Likely to adversely affect quality | **PAS (Prior Approval Supplement)** | New site, new synthetic route, new container closure material, qualitative excipient changes, widening specifications             |

### 14.2 Supplement Types

| Type              | Timing                                                 | Examples                                                               |
| ----------------- | ------------------------------------------------------ | ---------------------------------------------------------------------- |
| **PAS**           | Cannot implement until FDA approves (4-6 month review) | New manufacturing site, major process change, specification widening   |
| **CBE-30**        | Implement 30 days after FDA receipt (unless objection) | Moderate process changes, tightening specs, moderate container changes |
| **CBE-0**         | Implement immediately upon filing                      | Strengthening warnings, compendial compliance changes                  |
| **Annual Report** | Within 60 days of NDA anniversary                      | Minor changes (Level 1), ongoing stability data                        |

### 14.3 Comparability Protocols (21 CFR 314.70(a))

Pre-agreed protocols describing:
- Specific tests and acceptance criteria for anticipated changes
- If results meet criteria → change reported at lower category (PAS → CBE-30)
- ICH Q12 expands this concept via PACMPs (Post-Approval Change Management Protocols)

### 14.4 ICH Q12 — Established Conditions (ECs)

- **ECs are the legally binding commitments** in the marketing authorization
- Only changes to ECs require regulatory notification
- Non-EC parameters managed within the quality system (no filing required)
- Promotes risk-based post-approval change management
- Categorizes Module 3 information by regulatory impact

### 14.5 Continued Process Verification (Stage 3)

- Statistical Process Control (SPC) charts for CPPs and CQAs
- Annual Product Quality Review (APQR): all batches, deviations, OOS/OOT, complaints, stability
- Identifies adverse trends early → triggers investigation or revalidation

### 14.6 Post-Approval Commitments (PACs)

Common CMC post-approval commitments:
- Complete process validation (if concurrent)
- Additional stability studies (shelf-life extension)
- Method validation for new methods
- Pediatric formulation development
- Enhanced process controls based on CPV data

---

## 15. Biologics-Specific CMC

### 15.1 "The Process IS the Product"

Unlike small molecules (fully characterized by structure), biologics are defined by their manufacturing process. Even small process changes can alter the product's:
- Glycosylation pattern (affects efficacy, immunogenicity)
- Charge variant profile
- Aggregation propensity (affects safety)
- Higher-order structure (affects potency)

### 15.2 Cell Line and Cell Bank System

**Development:** Transfection → single-cell cloning → clone screening → lead clone selection → cell bank generation

**Cell Bank System:**
- **Master Cell Bank (MCB)**: Generated from lead clone; extensively characterized; stored in liquid nitrogen; limited use (generates WCBs)
- **Working Cell Bank (WCB)**: Generated from MCB; used for production; characterized with confirmatory testing
- **End-of-Production Cells (EPC)**: Cells harvested at the limit of in vitro cell age; tested for genetic stability

**Characterization testing (ICH Q5A, Q5B, Q5D):**

| Test Category        | Examples                                                                                 |
| -------------------- | ---------------------------------------------------------------------------------------- |
| Identity             | Isoenzyme analysis, DNA fingerprinting, gene sequencing                                  |
| Purity               | Sterility, mycoplasma, adventitious viruses (in vitro/in vivo), species-specific viruses |
| Genetic stability    | Gene copy number, restriction enzyme mapping, sequencing at MCB and EPC                  |
| Tumorigenicity       | Soft agar cloning, nude mouse studies (for some cell lines)                              |
| Retroviral particles | TEM, reverse transcriptase activity, infectivity assays                                  |

### 15.3 Viral Safety (ICH Q5A(R2))

Three complementary approaches:
1. **Cell line and raw material testing** for adventitious agents
2. **Viral clearance validation**: Demonstrate ≥4 log₁₀ reduction through orthogonal steps (low pH inactivation, nanofiltration, chromatography)
3. **Product testing** at appropriate manufacturing steps

### 15.4 Biologic Characterization

| Attribute                  | Methods                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------- |
| Primary structure          | Peptide mapping (LC-MS/MS), intact mass, amino acid analysis, N/C-terminal sequencing |
| Higher-order structure     | CD, DSC, FTIR, HDX-MS, cryo-EM                                                        |
| Glycosylation              | HILIC, CE-LIF, LC-MS, MALDI-TOF                                                       |
| Charge variants            | CEX-HPLC, icIEF, CZE                                                                  |
| Size variants              | SEC-HPLC, CE-SDS (reduced/non-reduced), AUC, SEC-MALS                                 |
| Potency                    | Cell-based bioassay, binding assay (SPR, ELISA), ADCC/CDC assays                      |
| Process-related impurities | HCP (ELISA), host cell DNA (qPCR), Protein A (ELISA), residual media                  |

### 15.5 Comparability (ICH Q5E)

Required when manufacturing process changes occur during development or post-approval:
- **Tiered approach**: Analytical (most extensive) → functional/biological → nonclinical/clinical (if needed)
- Analytical comparability is usually sufficient if comprehensive and well-designed
- Critical for biosimilar development (entire pathway depends on analytical similarity)

---

## 16. Small Molecule vs. Biologics CMC — Key Differences

| Aspect                  | Small Molecule         | Biologic                                  |
| ----------------------- | ---------------------- | ----------------------------------------- |
| Molecular weight        | <1,000 Da              | 10,000-150,000+ Da                        |
| Structure               | Fully characterized    | Complex; defined by process               |
| Manufacturing           | Chemical synthesis     | Cell culture/fermentation                 |
| Impurity control        | ICH Q3A/B thresholds   | Process-specific; HCP, DNA, aggregates    |
| Analytical methods      | HPLC, GC, titration    | Bioassays, SEC, CEX, peptide mapping      |
| Specifications          | ICH Q6A                | ICH Q6B                                   |
| Process changes         | Generally lower impact | Can fundamentally alter product           |
| Stability testing       | Standard ICH Q1A       | ICH Q5C; potency is primary indicator     |
| Stability extrapolation | Allowed per Q1E        | Generally not accepted for biologics      |
| Comparability           | Rarely needed          | Required for any significant change (Q5E) |
| GMP standard            | 21 CFR 210/211, ICH Q7 | 21 CFR 210/211 + 600-680, ICH Q7          |
| Typical CMC cost        | 15-25% of development  | 30-50% of development                     |

---

## 17. Advanced Therapies — Cell, Gene, and mRNA CMC

### 17.1 Cell Therapy (CAR-T) CMC Challenges

| Challenge                     | Detail                                                                        |
| ----------------------------- | ----------------------------------------------------------------------------- |
| Autologous manufacturing      | Each batch = one patient; no traditional batch statistics                     |
| Starting material variability | Patient cells vary in quality and quantity                                    |
| Short shelf life              | Some products must be administered within hours                               |
| Chain of identity             | Patient-specific material tracking throughout manufacturing                   |
| Potency assays                | Functional assays with high variability (cytotoxicity, cytokine release)      |
| Sterility testing             | 14-day test vs. short shelf life — release before completion may be necessary |
| Scale-out (not scale-up)      | Each batch is small; scale = more parallel batches                            |

**Example:** Kymriah (tisagenlecleucel, Novartis) — initial manufacturing failure rates were high (~8%); decentralized model posed quality assurance challenges.

### 17.2 Gene Therapy (AAV Vectors) CMC Challenges

| Challenge               | Detail                                                              |
| ----------------------- | ------------------------------------------------------------------- |
| Scalability             | Transitioning from adherent to suspension cell culture              |
| Full/empty capsids      | Ratio is a CQA; separation by ultracentrifugation or chromatography |
| Vector characterization | Genome integrity, capsid identity, potency (transgene expression)   |
| Impurity profile        | Host cell DNA, HCP, residual plasmid DNA                            |
| Lot-to-lot variability  | Greater than traditional biologics                                  |
| Manufacturing capacity  | Enormous quantities needed; limited global capacity                 |

**Example:** Zolgensma (onasemnogene abeparvovec, Novartis) — manufacturing at scale was extremely challenging; $2.1M per dose reflects manufacturing complexity.

### 17.3 mRNA Therapeutics CMC

**Drug substance (mRNA):**
- In vitro transcription (IVT) optimization
- Purification to remove dsRNA (immune activation trigger)
- CQAs: Capping efficiency, poly(A) tail length, sequence integrity, truncated species, template DNA removal

**Drug product (LNP formulation):**
- Lipid nanoparticle composition: ionizable lipid, PEGylated lipid, DSPC, cholesterol
- CQAs: Particle size, polydispersity, encapsulation efficiency, mRNA integrity within LNP
- Cold chain challenges: Original Comirnaty required −70°C; industry working toward 2-8°C stability through lyophilization

### 17.4 Regulatory Framework for Advanced Therapies

- FDA: "CMC Information for Human Gene Therapy INDs" (2020), potency guidance for cell/gene therapy
- EMA: ATMP Regulation (EC) No 1394/2007; Committee for Advanced Therapies (CAT)
- ICH: Guidelines for gene therapy and cell therapy vectors under development

---
