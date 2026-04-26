# CMC Forge — Worked Example: Chromatography Resin Supplier Change Impact Assessment & Comparability Strategy

> **Mode**: ASSESS (Route 2: Change, Transfer, Or Comparability)
> **Skill output type**: Comparability / Change Package
> **This is a MOCK output using fictional data. Not a real assessment.**

---

## User Request

> "我们准备更换 Protein A 后面的关键抛光树脂供应商，请先搭一版 change impact assessment 和 comparability strategy。"

---

## 1. Change Summary

### Product Context

| Field | Value |
|-------|-------|
| **Product** | MB-2201 (anti-IL-6R IgG1 mAb) |
| **Development stage** | Commercial (approved, marketed) |
| **Dosage form** | Solution for injection, 100 mg/mL, pre-filled syringe |
| **Manufacturing site** | Site A (internal GMP facility) |
| **Annual batches** | ~40 commercial batches per year |
| **Regulatory jurisdiction** | NMPA (primary), FDA (secondary) |

### Change Description

| Item | Current State | Proposed State |
|------|---------------|----------------|
| **Resin** | Cation exchange (CEX), Brand X, Q HyperD series | Cation exchange (CEX), Brand Y, UnoCipher Plus |
| **Step in process** | Polishing Step 2 (post-Protein A, post-low-pH viral inactivation, post-anion exchange flow-through) | Same step position, same function (aggregate and charge variant clearance) |
| **Supplier** | Supplier A (single source) | Supplier B (establishing second source) |
| **Mode of action** | Bind-elute, cation exchange | Bind-elute, cation exchange (same mode) |
| **Reason for change** | Supplier A announced resin discontinuation (effective 18 months from now); also seeks supply chain resilience through dual sourcing |

### Change Classification

| Dimension | Assessment |
|-----------|-----------|
| **Process step criticality** | Critical polishing step — primary function is HMW aggregate clearance and acidic charge variant control |
| **Change type** | Raw material / consumable supplier change |
| **Change scope** | Same resin class (CEX), same mode (bind-elute), different manufacturer |
| **Preliminary risk level** | **Medium** — same class of resin, same separation mechanism, but different base bead matrix, ligand density, and pore structure may affect selectivity and process performance |

---

## 2. Current vs. Proposed State Table

| Attribute | Current (Brand X, Q HyperD) | Proposed (Brand Y, UnoCipher Plus) | Expected Impact |
|-----------|------------------------------|-------------------------------------|-----------------|
| **Resin class** | CEX, strong (sulfopropyl) | CEX, strong (sulfopropyl) | None — same chemistry |
| **Base matrix** | Polymethacrylate, 5 um | Agarose, 6 um | Possible difference in mass transfer and resolution |
| **Bead size** | 5 um | 6 um | Minor; may affect peak width |
| **Ligand** | Sulfopropyl (SP) | Sulfopropyl (SP) | None — same ligand |
| **Ligand density** | Proprietary (high) | Proprietary (medium-high) | Possible difference in binding capacity and selectivity |
| **Operating pH range** | 2.0-12.0 | 3.0-12.0 | Within operating window (pH 4.5-6.5); no issue |
| **Operating pressure limit** | 100 bar | 70 bar | Must confirm column dimensions and flow rate are compatible; may require flow rate adjustment |
| **Dynamic binding capacity (DBC)** | ~85 mg/mL at 10% breakthrough (model mAb) | ~75 mg/mL at 10% breakthrough (model mAb) | Lower DBC may require reduced load challenge or adjusted loading strategy |
| **Lifetime (cycles)** | Validated 100 cycles | Vendor claim 80+ cycles; to be validated | Must validate cycle lifetime for commercial use |
| **Cleaning/sanitization** | 0.5 M NaOH, 30 min, validated | 0.5 M NaOH, 30 min (vendor recommended) | Compatible; must re-validate cleaning effectiveness |
| **Regulatory filing reference** | Listed in approved BLA Module 3.2.S.2.2 | New resin requires update to Module 3.2.S.2.2 | Regulatory submission required (see Section 7) |
| **Supply security** | Single source, resin discontinued | New second source, long-term supply agreement to be established | Improvement in supply chain resilience |

---

## 3. CQA Impact Hypothesis

Systematic assessment of each product CQA and whether the resin change could affect it:

| CQA | Current Control | Impact Hypothesis | Likelihood | Severity | Rationale |
|-----|----------------|-------------------|------------|----------|-----------|
| **Purity (SEC monomer)** | Controlled at CEX step; targets >= 99.0% monomer post-CEX | Could be affected | Medium | High | Different bead matrix and ligand density may alter aggregate resolution; this is the primary function of this step |
| **Charge variants (acidic/main/basic)** | Controlled at CEX step; targets >= 60% main peak | Could be affected | Medium | Medium | Selectivity differences may shift acidic/main/basic peak distribution; must verify peak profile is maintained |
| **Potency (bioassay)** | Controlled at release; target 80-120% relative to reference | Unlikely to be affected | Low | High | Resin is a purification step; no structural modification expected if purity and charge profile are maintained |
| **Host cell protein (HCP)** | Controlled at Protein A and AEX steps; CEX is secondary | Unlikely to be affected | Low | Low | HCP clearance primarily at Protein A; CEX is not the primary HCP removal step |
| **Residual Protein A** | Controlled at Protein A step; not a function of CEX | Not affected | None | None | Protein A leaching is upstream of this step |
| **Residual DNA** | Controlled at multiple steps | Not affected | None | Low | DNA clearance primarily at nuclease treatment and AEX |
| **Glycosylation profile** | Cell culture controlled; not affected by polishing | Not affected | None | Medium | Glycan pattern established upstream; CEX does not modify glycans |
| **Aggregates (HMW species)** | Primary function of CEX polishing step | Could be affected | Medium | High | Same as purity above; aggregate clearance is the key performance attribute |
| **Endotoxin** | Controlled by manufacturing environment and buffers | Not affected | None | Low | Resin does not introduce endotoxin; buffer preparation controls endotoxin |
| **Subvisible particles** | Controlled by filtration post-chromatography | Unlikely to be affected | Low | Medium | If resin shedding or leachable profile differs, particle formation downstream is possible but unlikely |

**CQAs requiring direct comparability evidence**: Purity (SEC), Charge variants (CEX/iCIEF), HMW aggregates, Potency
**CQAs unlikely to be affected but to be confirmed**: HCP, Residual DNA, Subvisible particles
**CQAs not affected**: Glycosylation, Residual Protein A, Endotoxin

---

## 4. Risk Register

| Risk ID | Risk Description | Category | Severity (S) | Occurrence (O) | Detectability (D) | RPN (S x O x D) | Current Controls | Proposed Mitigation | Owner | Residual Risk |
|---------|-----------------|----------|:---:|:---:|:---:|:---:|-----------------|---------------------|-------|:---:|
| R-001 | New resin fails to achieve target aggregate clearance (>= 99.0% monomer) | Product Quality | 8 | 4 | 2 | **64** | Process characterization data from current resin; design space established | Conduct small-scale resin screening with fractional factorial DOEs; test load challenge, pH, conductivity gradients before implementation | Process Development | Medium |
| R-002 | Different selectivity leads to unacceptable shift in charge variant profile (main peak < 60%) | Product Quality | 7 | 5 | 2 | **70** | Current validated method window; historical batch data | Run head-to-head comparison of charge variant profile using qualified iCIEF method on multiple process intermediate lots | Analytical | Medium |
| R-003 | Lower DBC requires reduced loading, impacting process throughput or yield | Process Performance | 5 | 6 | 3 | **90** | Current process validated at specific load challenge | Determine DBC with actual product; adjust load challenge or increase column volume if needed; confirm yield impact | Process Development | Medium |
| R-004 | New resin introduces unknown leachables not captured by current extractables/leachables (E&L) assessment | Safety / Compliance | 8 | 3 | 4 | **96** | Current E&L study covers existing resin only | Commission E&L study for new resin (per BPSA/BIOSP guidance); compare extractables profile before first GMP use | QA / Process Validation | Low (after mitigation) |
| R-005 | Resin lifetime validation does not achieve target cycles, increasing cost of goods | Manufacturing / Cost | 4 | 4 | 2 | **32** | Current resin validated for 100 cycles | Include lifetime study in validation protocol (target 80+ cycles; if <80, perform cost-benefit analysis) | Process Validation | Low |
| R-006 | Regulatory authority requests additional data or rejects change classification, delaying implementation | Regulatory / Timeline | 7 | 3 | 5 | **105** | Pre-submission meeting planned | Prepare comprehensive comparability package; engage regulatory agency early via pre-submission meeting; classify change conservatively | Regulatory Affairs | Low (after pre-submission) |
| R-007 | Cleaning validation fails due to different resin-matrix interaction with NaOH | GMP Compliance | 6 | 3 | 3 | **54** | Current cleaning validated for existing resin | Include cleaning effectiveness in small-scale study; use TOC, bioburden, and LAL as acceptance criteria | QA / Validation | Low |

**Risk scoring key**: S = 1-10 (impact severity), O = 1-10 (likelihood of occurrence), D = 1-10 (difficulty of detection; higher = harder to detect). RPN = S x O x D. Prioritize RPN >= 70 for immediate action.

**Highest-priority risks**: R-006 (regulatory delay, RPN 105), R-004 (leachables, RPN 96), R-003 (DBC/throughput, RPN 90).

---

## 5. Three-Step Comparability Evidence Plan

### Step 1: Analytical Comparability (Required — Always)

**Objective**: Demonstrate that product manufactured with the new resin meets all established specifications and shows no statistically meaningful differences in quality attributes.

**Study design**: Manufacture a minimum of 3 consecutive batches (conformance batches) using the new resin at full commercial scale (or at representative scale if small-scale qualification is accepted). Compare against a reference set of 10+ historical batches manufactured with the current resin.

| Analytical Test | Method | Acceptance Criteria | Rationale |
|----------------|--------|---------------------|-----------|
| Purity (SEC-HPLC) | Qualified SEC method (TSKgel G3000SWxl) | Monomer >= 99.0%; HMW <= 1.0%; within historical range (mean +/- 2 SD) | Primary CQA; aggregate clearance is the key function of this step |
| Charge variants (iCIEF) | Qualified iCIEF method | Main peak >= 60%; acidic peaks and basic peaks within historical range | Selectivity difference is the primary risk for this change |
| Potency (cell-based bioassay) | Qualified cell-based IL-6R binding/inhibition assay | 80-120% relative to reference standard | Confirms biological activity is maintained |
| HCP (ELISA) | Qualified CHO HCP ELISA | <= 100 ng/mg; within historical range | Secondary HCP clearance verification |
| Residual DNA (qPCR) | Qualified qPCR method | <= 10 pg/mg; within historical range | Confirms DNA clearance not affected |
| Glycan profile (HILIC-UPLC) | Qualified HILIC method | G0F, G1F, G2F distribution within historical range; afucosyl <= 5% | Confirms upstream glycan profile not perturbed |
| Subvisible particles (MFI) | Qualified MFI method | Particles >= 2 um and >= 10 um within historical range | Detects any particle formation change |
| Peptide map (LC-MS) | Identity method | Matches reference standard peptide map | Confirms primary structure identity |
| Endotoxin (LAL) | Compendial | <= 0.5 EU/mg | Standard release test |
| Appearance / Color / Clarity | Compendial | Clear to slightly opalescent, colorless to pale yellow, essentially free of visible particulates | Standard release test |
| Concentration (UV A280) | Compendial | 95-105 mg/mL | Standard release test |
| Extractables profile (new) | Vendor E&L certificate + in-house GC-MS/LC-MS confirmation | No new peaks above safety concern threshold (SCT) | Addresses R-004; required for resin change |

**Statistical approach**: Use equivalence testing (TOST) for continuous attributes (SEC purity, charge variant main peak, potency). For qualitative attributes, confirm all results within specification. Reference ICH Q5E for comparability study design principles.

### Step 2: Non-Clinical Bridging (Conditional — Only if Triggered)

**Trigger conditions** — non-clinical bridging is needed ONLY if:
- Analytical comparability shows a statistically meaningful difference in a safety-related CQA (e.g., aggregate level exceeds historical range), OR
- New extractables are identified that cannot be qualified by toxicological risk assessment alone, OR
- Potency falls outside the equivalence margin

**If triggered, the following would be required:**

| Study | Scope | Duration | Rationale |
|-------|-------|----------|-----------|
| Repeat-dose toxicology (rat) | 1-month repeat dose, 2 dose levels + vehicle control, compare pre- and post-change material | ~3-4 months (including reporting) | Standard ICH Q5E non-clinical bridge for biotech products with quality attribute differences |
| Safety pharmacology (core battery) | Cardiovascular (telemetry), CNS (functional observation), respiratory (plethysmography) in rat | Integrated into repeat-dose study | Standard requirement for CMC changes with potential safety impact |
| Immunogenicity assessment (in vivo) | Anti-drug antibody (ADA) monitoring in repeat-dose study | Integrated into repeat-dose study | Detects any change in immunogenicity profile |

**Current assessment**: Step 2 is **unlikely to be triggered** given that (a) the resin is the same class and mode of action, (b) no structural modification of the product is expected, and (c) the change is limited to a polishing purification step. However, this determination is conditional on Step 1 results.

### Step 3: Clinical Bridge (Not Required — With Justification)

**Assessment**: A clinical bridging study is **not required** for this change. Justification:

1. **Resin function**: The CEX polishing step is a purification operation that removes process-related impurities (aggregates, charge variants, HCP). It does not covalently modify the product.
2. **Same resin class**: Both resins are strong cation exchangers with sulfopropyl ligands. The mode of separation (charge-based) is identical.
3. **Downstream controls**: Post-chromatography steps (viral filtration, UF/DF, sterile filtration, fill-finish) remain unchanged, providing additional assurance that the final product is equivalent.
4. **ICH Q5E guidance**: For manufacturing process changes that do not affect the product's structural or functional properties, and where analytical comparability demonstrates equivalence, clinical bridging is not expected.
5. **Regulatory precedent**: Multiple approved post-approval changes for chromatography resin replacement in mAb manufacturing have been classified without clinical bridge requirements (e.g., FDA CBE-30 supplements for similar changes).

**Contingency**: If Step 2 is triggered (i.e., analytical comparability fails and non-clinical differences are observed), then Step 3 clinical bridge (PK bridging study, single dose, crossover in healthy volunteers) would be evaluated. This is considered highly unlikely.

---

## 6. Regulatory Path Analysis

### NMPA Classification

| Factor | Assessment |
|--------|-----------|
| **Change category** | Raw material (chromatography resin) supplier change for a critical process step |
| **Relevant NMPA guidance** | "Technical Guideline for Post-approval Change Management of Biological Products" (2021) |
| **Preliminary classification** | **Moderate change (中等变更)** — change of critical raw material supplier for a critical process step, same type and function |
| **Reporting pathway** | **Filing (备案)** — submit change notification to NMPA with comparability data package; no prior approval required, but notification must be filed before implementation |
| **Expected review time** | 15-30 working days for acknowledgment |
| **Required submission content** | Change description, comparability protocol, analytical comparability data, risk assessment, updated Module 3.2.S.2.2 sections |

### FDA Classification (if applicable)

| Factor | Assessment |
|--------|-----------|
| **Change category** | Manufacturing process change — change to reagent (chromatography resin) |
| **Relevant guidance** | FDA Guidance "Changes to an Approved Application: Biological Products" (1997, updated) |
| **Preliminary classification** | **CBE-30 (Changes Being Effected in 30 days)** — change in a manufacturing site or process for a purification step where the change is not expected to adversely affect product quality |
| **Reporting pathway** | Submit supplement (CBE-30) to BLA; implement change 30 days after submission unless FDA notifies otherwise |
| **Required submission content** | Comparability data, updated process description, validation summary |

### Pre-Submission Recommendation

Given that MB-2201 is marketed in both China and the US, and the change affects a critical process step:
- **NMPA**: Recommend pre-submission communication with CDE Review Division 4 to confirm filing classification and data expectations.
- **FDA**: Consider a Type IA meeting or written response request to confirm CBE-30 classification, particularly regarding the E&L study requirements.
- **Timeline impact**: Allow 2-3 months for pre-submission interaction before filing.

---

## 7. Timeline

### Estimated Implementation Plan (5 months total)

| Phase | Activities | Duration | Start | End |
|-------|-----------|----------|-------|-----|
| **Phase 1: Small-Scale Evaluation** | Resin screening (small-scale column, 1 mL), process parameter DOE (load challenge, pH, conductivity, gradient), selectivity comparison, E&L vendor data review | 6 weeks | Month 1 | Month 2.5 |
| **Phase 2: Process Development & Optimization** | Optimize operating parameters for new resin, define new NOR/PAR ranges, confirm DBC with product, conduct preliminary lifetime study (accelerated cycling at small scale) | 4 weeks | Month 2.5 | Month 3.5 |
| **Phase 3: Pre-Submission & Validation Prep** | Compile comparability protocol, draft updated Module 3 sections, submit pre-submission inquiry to NMPA/FDA, prepare validation master plan | 3 weeks | Month 3.5 | Month 4 |
| **Phase 4: Conformance Batches & Comparability** | Execute 3 consecutive conformance batches at manufacturing scale, collect all analytical comparability data, statistical analysis (TOST), compile comparability report | 6 weeks | Month 4 | Month 5.5 |
| **Phase 5: Regulatory Filing** | Finalize comparability package, submit filing to NMPA (and CBE-30 to FDA if applicable), update batch records and SOPs | 2 weeks | Month 5.5 | Month 6 |

### Key Milestones

| Milestone | Target Date |
|-----------|-------------|
| Small-scale screening complete, go/no-go decision | Month 2 |
| Process parameters defined for new resin | Month 3.5 |
| Pre-submission inquiry submitted to regulatory | Month 4 |
| Conformance batches complete | Month 5.5 |
| Regulatory filing submitted | Month 6 |
| Implementation (first commercial batch with new resin) | Month 7-8 (subject to regulatory review) |

### Dependencies

| Dependency | Impact if Delayed |
|------------|-------------------|
| Resin delivery from Supplier B (lead time 8-10 weeks for first commercial-scale order) | Delays Phase 4; order resin at Phase 1 start to buffer lead time |
| E&L vendor study completion | Required before conformance batch release; commission at Phase 1 |
| Pre-submission regulatory feedback | May change data requirements; build in 4-week response time buffer |
| Qualified analytical lab capacity | Comparability testing requires prioritized lab time; reserve in advance |

---

## 8. Open Questions

The following questions must be answered before finalizing the change control and comparability strategy:

| # | Question | Owner | Target Resolution | Impact if Unresolved |
|---|----------|-------|-------------------|---------------------|
| 1 | **What is the confirmed discontinuation timeline from Supplier A?** Is the 18-month timeline firm, or is there a possibility of extension? | Procurement / Supply Chain | Week 2 | If timeline is shorter, implementation plan must be accelerated; if longer, there may be more flexibility |
| 2 | **Has Supplier B provided a complete extractables data package per BPSA/BIOSP protocols?** If not, what is the timeline for receiving it? | QA / Supplier Quality | Week 4 | E&L data is required before conformance batches; absence delays the entire program |
| 3 | **Are there any pending process changes (e.g., cell culture media change, scale-up) that could confound the comparability assessment?** If so, should those changes be sequenced before or after the resin change? | CMC Lead / Process Development | Week 2 | Concurrent process changes would complicate root-cause attribution if comparability fails; must isolate this change |
| 4 | **What is the minimum acceptable resin lifetime for commercial viability?** If the new resin achieves only 60-70 cycles (vs. current 100), is this acceptable from a cost-of-goods perspective? | Manufacturing / Finance | Month 3 | If short lifetime is unacceptable, a different resin candidate or larger column may be needed |
| 5 | **Does the clinical or medical affairs team anticipate any upcoming changes to the dosing regimen, indication expansion, or combination therapy studies** that would require additional regulatory submissions? If so, the resin change should be sequenced to avoid concurrent submissions. | Clinical / Regulatory Affairs | Week 4 | Overlapping submissions could strain regulatory review resources and create confusion about change attribution |

---

## 9. Human Review Required

This assessment is an AI-drafted working document. The following roles must review and approve before proceeding with the change implementation plan:

| Role | Review Scope | Decision Required |
|------|-------------|-------------------|
| **Process Development Lead** | Small-scale study design, process parameter ranges, DBC and lifetime study plan | Approve technical approach and study design |
| **Analytical Lead** | Comparability test plan, acceptance criteria, statistical approach (TOST design) | Confirm analytical methods are adequate for comparability assessment |
| **QA Head** | Change control classification, E&L study requirements, cleaning validation approach | Approve change control initiation and classification |
| **Regulatory Affairs Lead** | Regulatory pathway (NMPA filing / FDA CBE-30), pre-submission strategy, Module 3 update scope | Confirm regulatory classification and submission strategy |
| **Manufacturing Head** | Manufacturing timeline, conformance batch scheduling, supply chain impact, throughput/yield considerations | Confirm manufacturing capacity and timeline feasibility |
| **Supply Chain / Procurement** | Resin lead time, supply agreement terms, dual-source strategy, cost impact assessment | Confirm resin availability and commercial terms |
| **Medical / Clinical Lead** | Confirm no concurrent clinical activities that would conflict with the change timeline | Provide go/no-go for sequencing |
| **Quality Control (QC) Lab Manager** | Lab capacity for comparability testing, method availability, prioritization | Confirm QC lab can support the comparability study timeline |

---

> **Disclaimer**: This is a fictional example produced by the CMC Forge skill to demonstrate output format and content depth. All data, product names, resin brands, and timelines are invented. Do not use this document as a template for real regulatory or manufacturing decisions without review by qualified SMEs.
