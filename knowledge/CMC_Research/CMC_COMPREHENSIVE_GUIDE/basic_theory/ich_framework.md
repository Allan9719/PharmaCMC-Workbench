> 📖 基于 ICH 官方指导原则整理，核心参数已交叉核对。

## 1. What is CMC and Why It Matters

**CMC = Chemistry, Manufacturing, and Controls.** It encompasses all technical information about a drug's composition, how it is made, and how its quality is assured. CMC is the quality backbone of every regulatory submission — without robust CMC data, no drug can receive regulatory approval regardless of how strong the clinical efficacy data may be.

### The Core Proposition

CMC is about **proving your drug is reliably made using a reproducible, scalable process and is safe for patients.** Every tablet, vial, or syringe that reaches a patient must be:
- **Identified** — it is what the label says it is
- **Pure** — free of harmful impurities above qualified thresholds
- **Potent** — it delivers the intended therapeutic effect at the stated strength
- **Stable** — it maintains its quality throughout its shelf life
- **Consistently manufactured** — every batch is equivalent to the batches that proved safe and effective in clinical trials

### Why CMC Matters Strategically

- **CMC deficiencies are a leading cause of FDA Complete Response Letters (CRLs)**, delaying approvals by months or years.
- **CMC timelines often become the critical path** — process validation, stability data generation, and manufacturing site readiness cannot be accelerated beyond physical and regulatory constraints.
- **CMC investment is substantial** — 15-25% of total development costs for small molecules, 30-50% for biologics, and 40-60% for cell/gene therapies.
- **Post-approval CMC changes** (site transfers, process improvements, new formulations) require ongoing regulatory management for the life of the product.

---

## 2. The Four Pillars of CMC

### Pillar 1: Drug Substance (Active Pharmaceutical Ingredient / API)

Everything about the active ingredient before it is formulated:
- **Structure and characterization**: Molecular formula, stereochemistry, solid-state properties
- **Manufacturing process**: Synthetic route (small molecules) or cell culture/fermentation (biologics)
- **Impurity profile**: Process-related impurities, degradation products, elemental impurities, residual solvents, mutagenic impurities
- **Specifications**: Tests and acceptance criteria for identity, assay, purity, physical properties
- **Stability**: Retest period supported by ICH-compliant stability data

### Pillar 2: Drug Product (Finished Dosage Form)

The formulated product as administered to patients:
- **Formulation**: Quantitative composition, excipient selection and justification
- **Manufacturing process**: Unit operations, batch formula, in-process controls
- **Container closure system**: Primary packaging, extractables/leachables
- **Specifications**: Release and stability testing (identity, assay, content uniformity, dissolution, degradation products, microbial limits)
- **Stability**: Shelf life supported by ICH-compliant stability data

### Pillar 3: Analytical Methods

Tools used to measure and ensure quality:
- **Identity tests**: IR, UV, HPLC retention time, mass spectrometry
- **Assay/Potency**: HPLC, UV spectrophotometry, bioassays (biologics)
- **Impurity testing**: HPLC, GC-HS (residual solvents), ICP-MS (elemental impurities)
- **Physical tests**: Dissolution, content uniformity, particle size, hardness
- **Microbiological tests**: Sterility, endotoxins, microbial enumeration
- **Validation**: Per ICH Q2(R2) — specificity, linearity, accuracy, precision, range, LOD/LOQ, robustness

### Pillar 4: Manufacturing Controls

Systems ensuring reproducible, consistent quality:
- **cGMP compliance**: 21 CFR 210/211 (US), EU GMP Annexes, ICH Q7 (APIs)
- **Process validation**: FDA 2011 lifecycle approach (Stages 1-3)
- **In-process controls**: Tests and measurements during manufacturing
- **Environmental controls**: Cleanroom classifications, environmental monitoring
- **Equipment qualification**: IQ/OQ/PQ
- **Cleaning validation**: Product and cleaning agent residue removal
- **Supply chain controls**: Vendor qualification, incoming material testing

---

## 3. Regulatory Framework — ICH Guidelines

The International Council for Harmonisation (ICH) develops guidelines accepted by FDA, EMA, PMDA (Japan), Health Canada, Swissmedic, and others. The Quality ("Q") guidelines are the backbone of CMC regulatory science.

### ICH Q1: Stability Testing

| Guideline   | Title                                                 | Key Content                                                                                                                                                          |
| ----------- | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Q1A(R2)** | Stability Testing of New Drug Substances and Products | Core protocol — storage conditions (25°C/60% RH long-term, 40°C/75% RH accelerated), testing frequency, minimum 12 months long-term + 6 months accelerated at filing |
| **Q1B**     | Photostability Testing                                | Minimum 1.2 million lux-hours visible + 200 Wh/m² UV exposure                                                                                                        |
| **Q1C**     | Stability Testing for New Dosage Forms                | Reduced data acceptable for new dosage forms of approved substances                                                                                                  |
| **Q1D**     | Bracketing and Matrixing                              | Statistical designs to reduce stability testing burden                                                                                                               |
| **Q1E**     | Evaluation of Stability Data                          | Statistical analysis, shelf-life extrapolation rules (up to 2× long-term data, max 12 months beyond)                                                                 |

**Stability Storage Conditions:**

| Study Type   | Conditions               | Minimum Duration    | Testing Frequency                 |
| ------------ | ------------------------ | ------------------- | --------------------------------- |
| Long-term    | 25°C ± 2°C / 60% RH ± 5% | 12 months at filing | 0, 3, 6, 9, 12, 18, 24, 36 months |
| Intermediate | 30°C ± 2°C / 65% RH ± 5% | 12 months           | 0, 6, 9, 12 months                |
| Accelerated  | 40°C ± 2°C / 75% RH ± 5% | 6 months            | 0, 3, 6 months                    |

**"Significant Change" Triggers (Drug Product):** ≥5% assay change, degradant exceeding limit, pH outside range, dissolution failure for 12 units, appearance/physical property failure.

### ICH Q2(R2): Validation of Analytical Procedures

All analytical methods used for release and stability must be validated:

| Parameter              | Requirement                                                                                                                      |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Specificity**        | Resolve analyte from all degradants, impurities, and matrix                                                                      |
| **Linearity**          | Minimum 5 concentration levels; demonstrate proportional response                                                                |
| **Range**              | 80-120% (assay), 70-130% (content uniformity), ±20% beyond spec (dissolution)                                                    |
| **Accuracy**           | Minimum 9 determinations across 3 concentrations (3 replicates each)                                                             |
| **Precision**          | Repeatability (min 9 determinations), intermediate precision (different days/analysts/equipment), reproducibility (between labs) |
| **Detection Limit**    | S/N ≥ 3:1 or standard deviation of response/slope                                                                                |
| **Quantitation Limit** | S/N ≥ 10:1 or standard deviation/slope                                                                                           |
| **Robustness**         | Deliberate parameter variation (pH ±0.2, temperature ±5°C, flow rate ±10%)                                                       |

The R2 revision added Analytical Target Profile (ATP), enhanced statistical treatment, and lifecycle management concepts.

### ICH Q3: Impurities

**Q3A(R2) — Drug Substance Impurity Thresholds:**

| Max Daily Dose | Reporting | Identification       | Qualification        |
| -------------- | --------- | -------------------- | -------------------- |
| ≤2 g/day       | ≥0.05%    | ≥0.10% or 1.0 mg/day | ≥0.15% or 1.0 mg/day |
| >2 g/day       | ≥0.03%    | ≥0.05%               | ≥0.05%               |

**Q3B(R2) — Drug Product Degradation Thresholds:**

| Max Daily Dose     | Reporting | Identification              | Qualification               |
| ------------------ | --------- | --------------------------- | --------------------------- |
| <1 mg/day          | ≥0.1%     | 1.0% or 50 ug/day (lower)  | 1.0% or 50 ug/day (lower)  |
| 1 mg – 10 mg/day   | ≥0.1%     | 0.5% or 200 ug/day (lower) | 0.5% or 200 ug/day (lower) |
| >10 mg – 2 g/day   | ≥0.1%     | 0.2% or 2 mg/day (lower)   | 0.2% or 3 mg/day (lower)   |
| >2 g/day           | ≥0.05%    | 0.10%                       | 0.15%                       |

> 注：Identification 和 Qualification 取百分比与质量阈值中的较低值（whichever is lower）。

**Q3C(R8) — Residual Solvents:**
- **Class 1** (avoid): Benzene (2 ppm), carbon tetrachloride (4 ppm), 1,2-dichloroethane (5 ppm)
- **Class 2** (limit): Methylene chloride (600 ppm), chloroform (60 ppm), acetonitrile (410 ppm), DMF (880 ppm), toluene (890 ppm)
- **Class 3** (low toxicity): Acetone, ethanol, ethyl acetate, isopropanol — limit 5000 ppm

**Q3D(R2) — Elemental Impurities:**
- **Class 1** (highest toxicity): As, Cd, Hg, Pb — controlled in all drug products
- **Class 2A**: Co, Ni, V — evaluated across all routes
- **Class 2B**: Ag, Au, Ir, Os, Pd, Pt, Rh, Ru, Se, Tl — evaluated if intentionally added
- **Class 3**: Ba, Cr, Cu, Li, Mo, Sb, Sn, W — significant only for inhalation

**Q3E — Extractables and Leachables:** Risk-based approach using Safety Concern Threshold (SCT) and Qualification Threshold (QT).

**ICH M7(R2) — Mutagenic Impurities:**
- Threshold of Toxicological Concern (TTC): 1.5 µg/day for lifetime exposure
- Less-than-lifetime (LTL) adjustments allow higher limits for shorter clinical durations
- In silico assessment (Derek Nexus, Sarah Nexus) for all synthetic intermediates and plausible by-products

### ICH Q5: Quality of Biotechnological Products

| Guideline   | Title                            | Key Content                                                                                                 |
| ----------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Q5A(R2)** | Viral Safety Evaluation          | Three-pronged approach: cell line testing, viral clearance validation (≥4 log₁₀ reduction), product testing |
| **Q5B**     | Analysis of Expression Construct | Characterize vector, host cell, genetic stability through production culture                                |
| **Q5C**     | Stability of Biotech Products    | Potency is primary stability indicator; accelerated data are supportive only                                |
| **Q5D**     | Cell Substrate Characterisation  | MCB/WCB testing: identity, purity, stability, adventitious agents                                           |
| **Q5E**     | Comparability                    | Tiered approach: analytical → functional → nonclinical → clinical (if needed)                               |

### ICH Q6: Specifications

**Q6A (Chemical Substances):**
- Universal drug substance tests: appearance, identity, assay, impurities
- Universal drug product tests: appearance, identity, assay, degradation products
- Specific tests as appropriate: dissolution, content uniformity, water content, residual solvents, microbial limits, pH, sterility/endotoxins (parenterals)
- Decision trees for polymorphism, dissolution, microbial testing

**Q6B (Biotechnological Products):**
- Identity: immunochemical, peptide mapping, electrophoretic
- Purity: SEC, IEX, CE-SDS, rp-HPLC
- Potency: biological activity assay (mechanism-based)
- Process-related impurities: HCP, host cell DNA, Protein A, media components
- Product-related impurities: aggregates, fragments, charge variants, deamidated/oxidized variants

### ICH Q7: GMP for APIs

The definitive GMP guidance for API manufacturing:
- Applies from the "regulatory starting material" onward
- Covers: quality management, personnel, facilities, equipment, documentation, materials management, production controls, packaging, storage, lab controls, validation, change control, complaints/recalls
- Section 18: APIs by cell culture/fermentation (biotech)
- Section 19: APIs for clinical trials (reduced requirements)

### ICH Q8(R2): Pharmaceutical Development (Quality by Design)

The foundation of modern CMC development:
- **Quality Target Product Profile (QTPP)**: Prospective summary of desired quality characteristics
- **Critical Quality Attributes (CQAs)**: Properties within appropriate limits for desired quality
- **Design Space**: Multidimensional combination of input variables demonstrated to assure quality — working within design space is NOT a regulatory change
- **Control Strategy**: Planned controls ensuring process performance and product quality
- **Process Analytical Technology (PAT)**: Real-time monitoring and control
- **Traditional vs. Enhanced approach**: Enhanced (QbD) enables greater regulatory flexibility

### ICH Q9(R1): Quality Risk Management

- **Process**: Risk Assessment → Risk Control → Risk Review → Risk Communication
- **Tools**: FMEA/FMECA, Fault Tree Analysis, HACCP, HAZOP, Risk Ranking and Filtering
- **R1 revision** (2023): Emphasis on avoiding subjectivity and bias, promoting formality

### ICH Q10: Pharmaceutical Quality System

- **Four PQS elements**: (1) Process Performance and Product Quality Monitoring, (2) CAPA System, (3) Change Management, (4) Management Review
- **Enablers**: Knowledge Management, Quality Risk Management
- The "ICH Q-Trio" (Q8+Q9+Q10) represents the modern pharmaceutical quality paradigm

### ICH Q11: Drug Substance Development and Manufacture

- Extends Q8 QbD principles to API development
- Starting material justification criteria: well-defined, sufficient steps to final API, full GMP from starting material onward
- Manufacturing process development approaches: traditional vs. enhanced
- Control strategy for drug substance

### ICH Q12: Lifecycle Management

- **Established Conditions (ECs)**: Legally binding commitments — only changes to ECs require regulatory notification
- **Post-Approval Change Management Protocols (PACMPs)**: Pre-agreed change management for anticipated changes
- **Reporting categories**: Prior approval, notify-and-wait, annual report — harmonized globally
- The regulatory payoff for investment in process understanding

### ICH Q13: Continuous Manufacturing

- Harmonized guidance for continuous manufacturing of drug substances and drug products
- Addresses batch definition, process monitoring, control strategy, startup/shutdown
- Covers both small molecules and biologics

### ICH Q14: Analytical Procedure Development

- Complements Q2(R2) on validation
- Introduces Analytical QbD, Analytical Design Space, and Proven Acceptable Range (PAR)
- Supports lifecycle management of analytical procedures

---

## 4. The Common Technical Document (CTD) Module 3

Module 3 (Quality) is the CMC section of every regulatory submission worldwide. Structured per ICH M4Q(R1).

### Module 3 Structure

```
Module 3: Quality
├── 3.2.S — Drug Substance (repeated per substance)
│   ├── 3.2.S.1  General Information (nomenclature, structure, properties)
│   ├── 3.2.S.2  Manufacture (process, controls, validation)
│   ├── 3.2.S.3  Characterisation (structure elucidation, impurities)
│   ├── 3.2.S.4  Control of Drug Substance (specs, methods, validation, batch analyses)
│   ├── 3.2.S.5  Reference Standards
│   ├── 3.2.S.6  Container Closure System
│   └── 3.2.S.7  Stability
│
├── 3.2.P — Drug Product (repeated per product/dosage form)
│   ├── 3.2.P.1  Description and Composition
│   ├── 3.2.P.2  Pharmaceutical Development (QbD, design space)
│   ├── 3.2.P.3  Manufacture (batch formula, process, validation)
│   ├── 3.2.P.4  Control of Excipients
│   ├── 3.2.P.5  Control of Drug Product (specs, methods, validation, batch analyses)
│   ├── 3.2.P.6  Reference Standards
│   ├── 3.2.P.7  Container Closure System (E&L data)
│   └── 3.2.P.8  Stability
│
├── 3.2.A — Appendices
│   ├── 3.2.A.1  Facilities and Equipment (esp. biologics)
│   ├── 3.2.A.2  Adventitious Agents Safety Evaluation (biologics)
│   └── 3.2.A.3  Novel Excipients (if applicable)
│
└── 3.2.R — Regional Information
    └── 3.2.R.1-R.6  Region-specific (e.g., executed batch records for FDA)
```

---
