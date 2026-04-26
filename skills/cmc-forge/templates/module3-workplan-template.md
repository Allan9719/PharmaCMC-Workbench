# Module 3 Authoring Workplan — Biologics BLA/NDA Submission

**DRAFT FOR CONTROLLED REVIEW**

> This document is a workplan scaffold. All content must be verified against source documents before inclusion in the regulatory submission. No section should be finalized without review by the designated section author and CMC lead.

---

## 1. Submission Context

| Field | Value | Guidance |
|-------|-------|----------|
| Product Name | `[INN / code name]` | Use the planned INN if available; otherwise development code |
| Drug Substance Type | `[mAb / bispecific / ADC / fusion protein / other]` | Determines which ICH Q5 series guidances apply |
| Drug Product Dosage Form | `[solution for injection / lyophilized / pre-filled syringe]` | Affects 3.2.P section structure |
| Regulatory Region | `[US FDA / EMA / NMPA / PMDA / TGA / Health Canada]` | Region-specific formatting expectations differ |
| Company Filing Posture | `[China-only / China-first then global / Global-first with China bridge / Inbound China localization / Outbound licensing]` | Determines whether to build a core package plus regional deltas |
| Application Type | `[BLA / NDA / MAA / J-NDA]` | BLA for biologics (351(a) or 351(k)); NDA for small molecules |
| Submission Pathway | `[Standard 351(a) / 351(k) biosimilar / Accelerated / Breakthrough]` | Accelerated/Breakthrough may affect CMC data requirements |
| Filing Format | `[eCTD 4.0 / NeeS / region-specific]` | Confirm with regulatory operations |
| Target Filing Date | `[YYYY-MM-DD]` | Working backwards from this date determines all downstream milestones |
| Pre-BLA Meeting Date | `[YYYY-MM-DD or N/A]` | If applicable, CMC questions should be pre-agreed |
| CMC Lead | `[Name, Title]` | Single point of accountability for Module 3 content |
| RA CMC Contact | `[Name, Title]` | Interface between CMC team and regulatory publishing |
| eCTD Publishing Lead | `[Name, Title]` | Responsible for hyperlink integrity, file naming, granularity |

### Regional Delta Strategy

Use this section when the dossier may support more than one agency or a partner-facing package.

| Region / Audience | Intended Use | Core Package Reuse | Required Delta | Owner | Status |
|-------------------|--------------|--------------------|----------------|-------|--------|
| China NMPA/CDE | `[IND / NDA / BLA / supplement / meeting package]` | `[High / Medium / Low]` | `[CDE-specific Module 3, local testing, China pharmacopoeia, site/MAH info]` | `[RA CMC]` | `[status]` |
| US FDA | `[IND / BLA / NDA / meeting package]` | `[High / Medium / Low]` | `[FDA-specific validation, PQ/CMC structured data, meeting questions]` | `[RA CMC]` | `[status]` |
| EU EMA | `[MAA / variation / scientific advice]` | `[High / Medium / Low]` | `[EU variation/QP/site-specific expectations]` | `[RA CMC]` | `[status]` |
| Partner / BD | `[due diligence / licensing]` | `[High / Medium / Low]` | `[English executive narrative, risk register, source-evidence tracker]` | `[CMC lead]` | `[status]` |

### Bilingual Terminology Control

| Chinese Term | English Regulatory Term | Abbreviation | Controlled Definition / Usage Note |
|--------------|-------------------------|--------------|------------------------------------|
| 关键质量属性 | Critical Quality Attribute | CQA | `[define once and use consistently]` |
| 关键工艺参数 | Critical Process Parameter | CPP | `[define once and use consistently]` |
| 工艺性能确认 | Process Performance Qualification | PPQ | `[distinguish from broader process validation lifecycle]` |
| 持续工艺确认 | Continued Process Verification | CPV | `[define monitoring period and owner]` |
| `[term]` | `[term]` | `[abbr]` | `[usage note]` |

### Submission Milestone Timeline

| Milestone | Target Date | Status | Owner |
|-----------|-------------|--------|-------|
| Pre-submission meeting (if applicable) | `[date]` | `[Not started / Scheduled / Complete]` | `[RA CMC]` |
| Module 3 first draft complete | `[filing date - 12 weeks]` | `[status]` | `[CMC lead]` |
| Internal CMC review round 1 | `[filing date - 10 weeks]` | `[status]` | `[CMC lead]` |
| Cross-functional consistency review | `[filing date - 8 weeks]` | `[status]` | `[RA + CMC lead]` |
| QA review and approval | `[filing date - 6 weeks]` | `[status]` | `[QA Head]` |
| Regulatory publishing (hyperlinks, formatting) | `[filing date - 4 weeks]` | `[status]` | `[eCTD lead]` |
| Final QC read-through | `[filing date - 2 weeks]` | `[status]` | `[CMC lead + RA]` |
| Submission | `[filing date]` | `[status]` | `[RA]` |

**Common Pitfall**: Underestimating the time for hyperlink validation and cross-reference integrity in eCTD. The publishing step routinely takes 3-4 weeks for a biologics BLA with 200+ Module 3 documents. Start the first draft no later than 12 weeks before filing.

---

## 2. Full CTD Module 3 Section Map

The table below covers ALL standard Module 3 sections for a biologic. Mark status as: **N/A** (not applicable), **Draft in progress**, **Internal review**, **Final**, or **Published**.

### 3.2.S — Drug Substance

| Section | Title | Content Description | Status | Author | Due Date |
|---------|-------|---------------------|--------|--------|----------|
| 3.2.S.1 | General Information | Nomenclature, structure, physicochemical and biological properties. Include primary structure (amino acid sequence), higher-order structure summary, molecular weight, extinction coefficient, isoelectric point, glycosylation profile overview. | `[status]` | `[author]` | `[date]` |
| 3.2.S.1.1 | Nomenclature | INN (proposed or granted), company code, USAN, systematic name. Include CAS number if available. | `[status]` | `[author]` | `[date]` |
| 3.2.S.1.2 | Structure | Primary, secondary, tertiary, quaternary structure. Disulfide mapping. Post-translational modifications (glycosylation, deamidation, oxidation sites). Reference structural characterization studies. | `[status]` | `[author]` | `[date]` |
| 3.2.S.1.3 | General Properties | Physicochemical and biological properties relevant to manufacturability and quality: solubility, pI, thermal stability (Tm), forced degradation behavior, biological activity/potency assay overview. | `[status]` | `[author]` | `[date]` |
| 3.2.S.2 | Manufacture | Full manufacturing narrative including cell line history, cell bank system, USP, DSP, process controls, and process validation summary. | `[status]` | `[author]` | `[date]` |
| 3.2.S.2.1 | Manufacturer(s) | Name, address, and responsibilities of each DS manufacturing site. Include contract manufacturers. Must match Module 1 site information. | `[status]` | `[author]` | `[date]` |
| 3.2.S.2.2 | Description of Manufacturing Process and Process Controls | Step-by-step process description with unit operations, process parameters, and in-process controls. Flow diagram required. Include scale information. | `[status]` | `[author]` | `[date]` |
| 3.2.S.2.3 | Control of Materials | Raw materials, starting materials, cell substrate. Cell line development summary, cell bank system (MCB, WCB, EOPC), characterization, and testing. Include TSE/BSE risk assessment for animal-derived materials. | `[status]` | `[author]` | `[date]` |
| 3.2.S.2.4 | Control of Critical Steps and Intermediates | CPPs and their NOR/PAR ranges. In-process controls and acceptance criteria for critical intermediates. Justification linking CPPs to CQAs. | `[status]` | `[author]` | `[date]` |
| 3.2.S.2.5 | Process Validation and/or Evaluation | Process validation strategy and results. PPQ batch summary. Continued process verification plan. May reference Process Validation Protocol/Report in 3.2.R. | `[status]` | `[author]` | `[date]` |
| 3.2.S.2.6 | Manufacturing Process Development | Process development history. Change history with justification. Comparability studies supporting changes. Link to 3.2.R for supporting data. | `[status]` | `[author]` | `[date]` |
| 3.2.S.3 | Characterisation | Elucidation of structure and other characteristics. Comprehensive analytical characterization. | `[status]` | `[author]` | `[date]` |
| 3.2.S.3.1 | Elucidation of Structure and Other Characteristics | Primary structure confirmation, PTM profiling, higher-order structure, charge variants, size variants, glycan profiling, biological activity. Each attribute mapped to a CQA with criticality classification. | `[status]` | `[author]` | `[date]` |
| 3.2.S.3.2 | Impurities | Process-related impurities (HCP, DNA, Protein A, leached metals, host cell proteins) and product-related impurities (aggregates, fragments, charge variants). Include clearance data and justification for specification limits. | `[status]` | `[author]` | `[date]` |
| 3.2.S.4 | Control of Drug Substance | Specification, analytical procedures, validation, batch analyses, and specification justification. | `[status]` | `[author]` | `[date]` |
| 3.2.S.4.1 | Specification | Release and stability specifications with test, acceptance criteria, and reference to analytical procedure. Include pharmacopoeial methods where applicable. | `[status]` | `[author]` | `[date]` |
| 3.2.S.4.2 | Analytical Procedures | Description of each analytical method. Must match methods listed in 3.2.S.4.1. Include system suitability criteria. | `[status]` | `[author]` | `[date]` |
| 3.2.S.4.3 | Validation of Analytical Procedures | Method validation reports per ICH Q2(R2)/Q14. Specificity, accuracy, precision, linearity, range, robustness, LOD/LOQ as applicable. | `[status]` | `[author]` | `[date]` |
| 3.2.S.4.4 | Batch Analyses | Batch results for representative manufacturing batches. Include commercial-scale and PPQ batches. Tabulated results against specification. | `[status]` | `[author]` | `[date]` |
| 3.2.S.4.5 | Justification of Specification | Rationale for each acceptance criterion. Link to clinical batch data, stability data, process capability, and regulatory precedent. Reference ICH Q6B. | `[status]` | `[author]` | `[date]` |
| 3.2.S.5 | Reference Standards or Materials | Primary reference standard (characterization, assignment of potency), working standards (calibration, qualification), system suitability standards. | `[status]` | `[author]` | `[date]` |
| 3.2.S.6 | Container Closure System | Primary container and closure for DS storage and shipping. Materials of construction, compatibility, extractables/leachables summary, closure integrity data. | `[status]` | `[author]` | `[date]` |
| 3.2.S.7 | Stability | Stability protocol, results, and conclusions supporting DS storage and shelf life. | `[status]` | `[author]` | `[date]` |
| 3.2.S.7.1 | Stability Summary and Conclusions | Storage conditions, shelf life, in-use stability, shipping stability. Statistically-derived expiry if applicable. | `[status]` | `[author]` | `[date]` |
| 3.2.S.7.2 | Post-Approval Stability Protocol and Stability Commitment | Ongoing stability protocol. Number of batches per year, test schedule, storage conditions. Commitment batches for commercial manufacturing. | `[status]` | `[author]` | `[date]` |
| 3.2.S.7.3 | Stability Data | Raw and summarized stability data in ICH-compliant tables. Include trend analysis where sufficient data exists. | `[status]` | `[author]` | `[date]` |

### 3.2.P — Drug Product

| Section | Title | Content Description | Status | Author | Due Date |
|---------|-------|---------------------|--------|--------|----------|
| 3.2.P.1 | Description and Composition of Drug Product | Qualitative and quantitative composition per unit. Include all excipients with grades and grades rationale. | `[status]` | `[author]` | `[date]` |
| 3.2.P.2 | Pharmaceutical Development | QbD narrative (where applicable). Formulation development, manufacturing process development, container closure development. Design space and control strategy summary. | `[status]` | `[author]` | `[date]` |
| 3.2.P.2.1 | Components of the Drug Product | DS compatibility, excipient characterization and justification, novel excipient data (if applicable). | `[status]` | `[author]` | `[date]` |
| 3.2.P.2.2 | Drug Product | Formulation development rationale. Overfill justification. | `[status]` | `[author]` | `[date]` |
| 3.2.P.2.3 | Manufacturing Process Development | DP process development history, scale-up, process parameter optimization, link to CQAs. | `[status]` | `[author]` | `[date]` |
| 3.2.P.2.4 | Container Closure System | Selection rationale, materials, compatibility, functional testing, device assessment (if combination product). | `[status]` | `[author]` | `[date]` |
| 3.2.P.2.5 | Microbiological Attributes | Preservative efficacy (if multi-dose), sterility assurance strategy, aseptic process simulation, container closure integrity. | `[status]` | `[author]` | `[date]` |
| 3.2.P.2.6 | Compatibility | Diluent compatibility, in-use stability, admixture compatibility, infusion line compatibility. | `[status]` | `[author]` | `[date]` |
| 3.2.P.3 | Manufacture | DP manufacturing narrative. | `[status]` | `[author]` | `[date]` |
| 3.2.P.3.1 | Manufacturer(s) | DP manufacturing site(s), addresses, responsibilities. | `[status]` | `[author]` | `[date]` |
| 3.2.P.3.2 | Batch Formula | Quantitative batch formula for each batch size (if multiple). Overfill calculation. | `[status]` | `[author]` | `[date]` |
| 3.2.P.3.3 | Description of Manufacturing Process and Process Controls | Step-by-step DP process with process parameters and in-process controls. Process flow diagram. | `[status]` | `[author]` | `[date]` |
| 3.2.P.3.4 | Control of Critical Steps and Intermediates | CPPs and IPCs for DP process. Acceptance criteria with justification. | `[status]` | `[author]` | `[date]` |
| 3.2.P.3.5 | Process Validation and/or Evaluation | DP process validation strategy, media fill results, aseptic process simulation. | `[status]` | `[author]` | `[date]` |
| 3.2.P.4 | Control of Excipients | Excipient specifications and compendial status. | `[status]` | `[author]` | `[date]` |
| 3.2.P.4.1 | Specifications | Excipient specifications (compendial or non-compendial). Include supplier CoA acceptance criteria. | `[status]` | `[author]` | `[date]` |
| 3.2.P.4.2 | Analytical Procedures | Non-compendial excipient test methods. | `[status]` | `[author]` | `[date]` |
| 3.2.P.4.3 | Validation of Analytical Procedures | Validation for non-compendial methods. | `[status]` | `[author]` | `[date]` |
| 3.2.P.4.4 | Justification of Specifications | Rationale for non-compendial excipient specifications. | `[status]` | `[author]` | `[date]` |
| 3.2.P.5 | Control of Drug Product | DP specification, methods, validation, batch data, justification. | `[status]` | `[author]` | `[date]` |
| 3.2.P.5.1 | Specification | Release and stability specifications. Include appearance, identity, purity, potency, safety, and general tests. | `[status]` | `[author]` | `[date]` |
| 3.2.P.5.2 | Analytical Procedures | DP-specific methods. Cross-reference DS methods where identical. | `[status]` | `[author]` | `[date]` |
| 3.2.P.5.3 | Validation of Analytical Procedures | DP method validation. Note: matrix effects must be addressed. | `[status]` | `[author]` | `[date]` |
| 3.2.P.5.4 | Batch Analyses | DP batch results from clinical, registration, and PPQ batches. | `[status]` | `[author]` | `[date]` |
| 3.2.P.5.5 | Characterisation of Impurities | Degradation products unique to DP. Leachables from container closure. | `[status]` | `[author]` | `[date]` |
| 3.2.P.5.6 | Justification of Specification | Rationale for DP acceptance criteria. | `[status]` | `[author]` | `[date]` |
| 3.2.P.6 | Reference Standards or Materials | DP reference standards, calibration standards, system suitability standards. | `[status]` | `[author]` | `[date]` |
| 3.2.P.7 | Container Closure System | DP primary container. Materials, drawings, specifications, extractables/leachables, functional testing, child-resistance (if applicable). | `[status]` | `[author]` | `[date]` |
| 3.2.P.8 | Stability | DP stability supporting shelf life and storage conditions. | `[status]` | `[author]` | `[date]` |
| 3.2.P.8.1 | Stability Summary and Conclusions | Proposed shelf life and storage conditions. Statistical shelf-life estimation per ICH Q1E. | `[status]` | `[author]` | `[date]` |
| 3.2.P.8.2 | Post-Approval Stability Protocol and Stability Commitment | Ongoing and commitment stability protocols. | `[status]` | `[author]` | `[date]` |
| 3.2.P.8.3 | Stability Data | Stability data tables and trend analysis. | `[status]` | `[author]` | `[date]` |

### 3.2.A — Appendices

| Section | Title | Content Description | Status | Author | Due Date |
|---------|-------|---------------------|--------|--------|----------|
| 3.2.A.1 | Facilities and Equipment | Facility description, equipment qualification summary, utilities. Multi-product facility cross-contamination controls. HVAC classification. | `[status]` | `[author]` | `[date]` |
| 3.2.A.2 | Adventitious Agents Safety Evaluation | Viral safety evaluation (clearance studies, raw material sourcing). TSE/BSE assessment. Mycoplasma. Per ICH Q5A(R2). | `[status]` | `[author]` | `[date]` |
| 3.2.A.3 | Novel Excipients | Data for excipients not previously used in approved products (or new route of administration). Per ICH M4Q guidance. | `[status]` | `[author]` | `[date]` |

### 3.2.R — Regional Information

| Section | Title | Content Description | Status | Author | Due Date |
|---------|-------|---------------------|--------|--------|----------|
| 3.2.R | Regional Information | Region-specific documents (e.g., environmental assessment for FDA, process validation reports, executed batch records). Content varies by region. | `[status]` | `[author]` | `[date]` |

---

## 3. Source Document Inventory

List every source document that feeds into Module 3. This table drives the content drafting and identifies gaps early.

| Doc ID | Document Title | Version / Date | Module 3 Section(s) Fed | Content Status | Owner | Storage Location |
|--------|---------------|----------------|------------------------|----------------|-------|------------------|
| SRC-001 | Cell Line Development Report | `[vX.X / date]` | 3.2.S.2.3 | `[Final / Draft / Not started]` | `[Process Dev]` | `[SharePoint path / Documentum ID]` |
| SRC-002 | Cell Bank Characterization Report | `[vX.X / date]` | 3.2.S.2.3 | `[status]` | `[Analytical]` | `[location]` |
| SRC-003 | USP Process Development Report | `[vX.X / date]` | 3.2.S.2.2, 3.2.S.2.6 | `[status]` | `[Process Dev]` | `[location]` |
| SRC-004 | DSP Process Development Report | `[vX.X / date]` | 3.2.S.2.2, 3.2.S.2.6 | `[status]` | `[Process Dev]` | `[location]` |
| SRC-005 | Process Characterization Study Report | `[vX.X / date]` | 3.2.S.2.4, 3.2.S.2.6 | `[status]` | `[Process Dev]` | `[location]` |
| SRC-006 | Impurity Clearance Study | `[vX.X / date]` | 3.2.S.3.2 | `[status]` | `[Process Dev]` | `[location]` |
| SRC-007 | Analytical Characterization Package | `[vX.X / date]` | 3.2.S.3.1 | `[status]` | `[Analytical]` | `[location]` |
| SRC-008 | Forced Degradation Study Report | `[vX.X / date]` | 3.2.S.3.1, 3.2.S.7 | `[status]` | `[Analytical]` | `[location]` |
| SRC-009 | Method Validation Reports (all DS methods) | `[vX.X / date]` | 3.2.S.4.3 | `[status]` | `[Analytical]` | `[location]` |
| SRC-010 | DS Specification Justification | `[vX.X / date]` | 3.2.S.4.5 | `[status]` | `[CMC Lead]` | `[location]` |
| SRC-011 | DS Batch Release Data (clinical + PPQ) | `[vX.X / date]` | 3.2.S.4.4 | `[status]` | `[QA]` | `[location]` |
| SRC-012 | DS Stability Report | `[vX.X / date]` | 3.2.S.7 | `[status]` | `[Analytical/Stability]` | `[location]` |
| SRC-013 | Container Closure Qualification (DS) | `[vX.X / date]` | 3.2.S.6 | `[status]` | `[Formulation]` | `[location]` |
| SRC-014 | E&L Study Report (DS container) | `[vX.X / date]` | 3.2.S.6 | `[status]` | `[Analytical]` | `[location]` |
| SRC-015 | Formulation Development Report | `[vX.X / date]` | 3.2.P.2 | `[status]` | `[Formulation]` | `[location]` |
| SRC-016 | DP Process Development Report | `[vX.X / date]` | 3.2.P.2.3, 3.2.P.3 | `[status]` | `[Process Dev]` | `[location]` |
| SRC-017 | DP Method Validation Reports | `[vX.X / date]` | 3.2.P.5.3 | `[status]` | `[Analytical]` | `[location]` |
| SRC-018 | DP Batch Release Data | `[vX.X / date]` | 3.2.P.5.4 | `[status]` | `[QA]` | `[location]` |
| SRC-019 | DP Stability Report | `[vX.X / date]` | 3.2.P.8 | `[status]` | `[Analytical/Stability]` | `[location]` |
| SRC-020 | Viral Clearance Study Report | `[vX.X / date]` | 3.2.A.2 | `[status]` | `[Process Dev]` | `[location]` |
| SRC-021 | Process Validation Protocol | `[vX.X / date]` | 3.2.S.2.5, 3.2.R | `[status]` | `[Validation]` | `[location]` |
| SRC-022 | Process Validation Report (PPQ) | `[vX.X / date]` | 3.2.S.2.5, 3.2.R | `[status]` | `[Validation]` | `[location]` |
| SRC-023 | Comparability Study Report(s) | `[vX.X / date]` | 3.2.S.2.6 | `[status]` | `[CMC Lead]` | `[location]` |
| SRC-024 | Environmental Assessment (FDA) | `[vX.X / date]` | 3.2.R | `[status]` | `[RA]` | `[location]` |

**Common Pitfall**: Source document versions change during Module 3 drafting. Lock the "version used" for each source when a section enters review, and re-verify immediately before publishing. A mismatch between the stability data cited in 3.2.S.7 and the actual stability report version is a common deficiency letter finding.

---

## 4. Missing Content Log

Track content that is not yet available or requires generation. Assign priority based on whether the missing item blocks other sections.

| Log ID | Missing Content | Affected Section(s) | Priority | Impact if Missing | Owner | Target Date | Resolution Status |
|--------|----------------|---------------------|----------|-------------------|-------|-------------|-------------------|
| MC-001 | `[e.g., Final PPQ batch data for Batch 003]` | `[3.2.S.2.5, 3.2.S.4.4]` | `[P0-Critical / P1-High / P2-Medium / P3-Low]` | `[blocks process validation section, delays filing]` | `[owner]` | `[date]` | `[Open / In progress / Resolved]` |
| MC-002 | `[e.g., Glycan characterization for clinical batches]` | `[3.2.S.3.1]` | `[priority]` | `[impact]` | `[owner]` | `[date]` | `[status]` |
| MC-003 | `[e.g., Final DP stability data at 12 months]` | `[3.2.P.8.3]` | `[priority]` | `[impact]` | `[owner]` | `[date]` | `[status]` |
| MC-004 | `[e.g., Updated E&L study for new stopper vendor]` | `[3.2.S.6, 3.2.P.7]` | `[priority]` | `[impact]` | `[owner]` | `[date]` | `[status]` |
| MC-005 | `[e.g., Finalized process validation report]` | `[3.2.S.2.5, 3.2.R]` | `[priority]` | `[impact]` | `[owner]` | `[date]` | `[status]` |

**Priority Definitions**:
- **P0-Critical**: Blocks 3 or more sections or blocks filing if unresolved. Resolve immediately.
- **P1-High**: Blocks 1-2 sections. Must resolve before internal review.
- **P2-Medium**: Affects completeness but workaround exists. Resolve before publishing.
- **P3-Low**: Nice-to-have, can be deferred to post-approval commitment. Document justification.

---

## 5. Consistency Checks Checklist

Before each review round, verify the following cross-sectional consistencies. Check each item and record the checker and date.

| # | Consistency Check | What to Verify | Status | Checker | Date |
|---|-------------------|----------------|--------|---------|------|
| 1 | **Batch numbers consistency** | Every batch number cited in 3.2.S.4.4 (batch analyses) must also appear in 3.2.S.7 (stability) and 3.2.S.2.5 (validation). No orphan batches. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 2 | **Specification cross-reference** | Tests and acceptance criteria in 3.2.S.4.1 must exactly match the column headers in 3.2.S.4.4 batch tables. Same for 3.2.P.5.1 vs 3.2.P.5.4. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 3 | **Method IDs match** | Analytical procedure IDs in 3.2.S.4.2 must match those referenced in 3.2.S.4.1 specification and 3.2.S.4.3 validation. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 4 | **Process description alignment** | Unit operations listed in 3.2.S.2.2 must match the process flow diagram and the CPPs listed in 3.2.S.2.4. No missing or extra steps. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 5 | **Impurity claim alignment** | Impurities listed in 3.2.S.3.2 must have corresponding limits in 3.2.S.4.1 specification and clearance data in 3.2.S.2.6 (process development). | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 6 | **Stability conditions alignment** | Storage conditions in 3.2.S.7.1 must match those in 3.2.S.7.2 protocol and 3.2.S.7.3 data tables. Test timepoints must align. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 7 | **Container closure consistency** | Container description in 3.2.S.6 must match 3.2.S.1.3 (general properties - storage) and 3.2.S.7.1 (stability storage). Same for 3.2.P.7 vs 3.2.P.1. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 8 | **Manufacturer site addresses** | Addresses in 3.2.S.2.1 and 3.2.P.3.1 must match Module 1 (FDA 356h form) and any site registration information. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 9 | **Excipient quantities** | Quantitative composition in 3.2.P.1 must match 3.2.P.3.2 batch formula (accounting for batch size and overfill). | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 10 | **Comparability references** | Any comparability study cited in 3.2.S.2.6 must have a corresponding study report in 3.2.R or a cross-reference to the relevant section. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 11 | **DS-DP CQA linkage** | CQAs identified in 3.2.S.3.1 characterization should be traceable to the control strategy in 3.2.S.2.4 and specification in 3.2.S.4.1. Uncontrolled CQAs need justification. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 12 | **Terminology consistency** | Product name, drug substance code, dosage form, strength, and route of administration must be identical across all Module 3 sections and match Module 1 and Module 2.3 QOS. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 13 | **Hyperlink integrity** | All internal hyperlinks in eCTD must resolve to the correct leaf document. Every cross-reference (e.g., "see Section 3.2.S.4.3") must be hyperlinked. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 14 | **Data cut-off date** | All data tables must reflect the same data cut-off date. State the cut-off explicitly in each section containing data. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |
| 15 | **Version control** | All source documents referenced must be the latest approved version. No drafts or unapproved versions cited as final. | `[ ] Pass / [ ] Fail` | `[name]` | `[date]` |

---

## 6. Cross-Reference Integrity Checks

These checks focus on data integrity across sections. Perform during final QC read-through.

| Cross-Reference Element | Source Section(s) | Target Section(s) | Check Method | Status |
|------------------------|-------------------|-------------------|--------------|--------|
| DS batch numbers in stability | 3.2.S.7.3 | 3.2.S.4.4, 3.2.S.2.5 | Compare batch ID lists | `[ ] Verified` |
| DP batch numbers in stability | 3.2.P.8.3 | 3.2.P.5.4, 3.2.P.3.5 | Compare batch ID lists | `[ ] Verified` |
| DS specification tests and limits | 3.2.S.4.1 | 3.2.S.4.4 (batch table headers) | Column-by-column match | `[ ] Verified` |
| DP specification tests and limits | 3.2.P.5.1 | 3.2.P.5.4 (batch table headers) | Column-by-column match | `[ ] Verified` |
| CPP parameters and ranges | 3.2.S.2.4 | 3.2.S.2.2 (process description) | Parameter names and ranges match | `[ ] Verified` |
| Impurity names and limits | 3.2.S.3.2 | 3.2.S.4.1 (specification table) | Name and limit match | `[ ] Verified` |
| Storage conditions | 3.2.S.7.1, 3.2.P.8.1 | 3.2.S.6, 3.2.P.7, labeling sections | Consistent across all mentions | `[ ] Verified` |
| Reference standard assignments | 3.2.S.5 | 3.2.S.4.2 (methods using standards) | Correct standard cited per method | `[ ] Verified` |
| Glycan/PTM data across sections | 3.2.S.3.1 | 3.2.S.4.4 (release data) | Characterization covers specification attributes | `[ ] Verified` |
| Cell bank testing panel | 3.2.S.2.3 | 3.2.A.2 (adventitious agents) | Tests and results consistent | `[ ] Verified` |

---

## 7. Risks to Submission Readiness

| Risk ID | Risk Description | Likelihood | Impact | Mitigation | Owner | Status |
|---------|------------------|------------|--------|------------|-------|--------|
| RSK-001 | `[e.g., PPQ Batch 003 fails potency specification]` | `[High / Medium / Low]` | `[Blocks filing]` | `[e.g., Have contingency batch scheduled; investigate OOS within 2 weeks]` | `[owner]` | `[Open / Mitigated / Closed]` |
| RSK-002 | `[e.g., Method transfer for host cell protein ELISA not complete]` | `[likelihood]` | `[impact]` | `[mitigation]` | `[owner]` | `[status]` |
| RSK-003 | `[e.g., Stability data at proposed shelf life insufficient for statistical estimation]` | `[likelihood]` | `[impact]` | `[mitigation]` | `[owner]` | `[status]` |
| RSK-004 | `[e.g., Comparability bridge incomplete for manufacturing site change]` | `[likelihood]` | `[impact]` | `[mitigation]` | `[owner]` | `[status]` |
| RSK-005 | `[e.g., Regulatory agency requests additional characterization data during review]` | `[likelihood]` | `[impact]` | `[mitigation]` | `[owner]` | `[status]` |
| RSK-006 | `[e.g., Container closure supplier change mid-submission preparation]` | `[likelihood]` | `[impact]` | `[mitigation]` | `[owner]` | `[status]` |
| RSK-007 | `[e.g., Key author unavailable during drafting window]` | `[likelihood]` | `[impact]` | `[mitigation]` | `[owner]` | `[status]` |

---

## 8. Typical Timeline Mapping

Estimates for a biologics BLA Module 3. Actual time depends on team size, data maturity, and number of changes.

| Section Category | Estimated Authoring Time | Complexity Driver | Longest Lead Items |
|------------------|-------------------------|-------------------|---------------------|
| 3.2.S.2 (Manufacture) | 4-6 weeks | Process development narrative, change history, validation summary | Process validation report must be final before 3.2.S.2.5 can be completed |
| 3.2.S.3 (Characterization) | 3-4 weeks | Breadth of analytical characterization, PTM profiling | Forced degradation and characterization studies must be complete |
| 3.2.S.4 (Control of DS) | 3-5 weeks | Specification justification requires cross-referencing all data sources | Specification justification (3.2.S.4.5) is often the hardest section to write well |
| 3.2.S.7 (Stability) | 2-3 weeks | Data compilation and statistical analysis | Shelf-life estimation requires sufficient long-term data |
| 3.2.P.2 (Pharm Dev) | 4-6 weeks | Most narrative-heavy section; requires integration of all development data | Often underestimated; needs strong QbD story |
| 3.2.P.3-5 (DP Manufacture + Control) | 3-4 weeks | DP process validation, method validation | Similar dependencies to DS counterparts |
| 3.2.P.8 (DP Stability) | 2-3 weeks | Data compilation | Same as DS stability |
| 3.2.A (Appendices) | 2-3 weeks | Viral safety evaluation requires separate expert input | Viral clearance study timeline |
| Cross-section consistency review | 2 weeks | Entire Module 3 must be reviewed as a whole | Requires all sections in near-final state |
| Regulatory publishing | 3-4 weeks | Hyperlinking, file sizing, granularity, validation | Cannot start until all sections are final |

---

## 9. Human Review Gate Structure

| Review Gate | Trigger | Participants | Scope | Decision Criteria | Min. Duration |
|-------------|---------|-------------|-------|-------------------|---------------|
| **Gate 1: Section-Level Review** | Individual section first draft complete | Section author + 1 peer SME | Technical accuracy, completeness, fit-for-phase | Section passes internal technical review | 3-5 business days |
| **Gate 2: CMC Cross-Functional Review** | All sections in first draft | CMC Lead, RA CMC, QA, Analytical Lead, Process Dev Lead | Cross-references, consistency, regulatory strategy alignment | No unresolved cross-reference errors; consistency checks pass | 5-7 business days |
| **Gate 3: QA Compliance Review** | Post Gate 2 revisions complete | QA Head or designee | GMP compliance, data integrity, audit trail | QA sign-off on each section | 3-5 business days |
| **Gate 4: Regulatory Publishing Review** | Post Gate 3 final content | eCTD Publishing Lead, RA CMC | Hyperlink integrity, formatting, file sizing, eCTD compliance | Zero broken hyperlinks; all files pass eCTD validation | 5-10 business days |
| **Gate 5: Final QC Read-Through** | Post publishing | CMC Lead + RA CMC | End-to-end narrative review, last check for errors | No critical or major findings | 2-3 business days |

**Escalation Path**: Any reviewer can escalate to CMC Lead. CMC Lead escalates to Head of Regulatory Affairs for issues that may affect filing strategy or timeline.

---

## 10. Appendix: Data Cut-Off Declaration

| Field | Value |
|-------|-------|
| Data Cut-Off Date | `[YYYY-MM-DD]` |
| Declared By | `[Name, Title]` |
| Approved By | `[Name, Title]` |
| Date Declared | `[YYYY-MM-DD]` |
| Sections Affected | All sections containing batch data, stability data, or analytical results |

> All data included in this Module 3 submission reflects results available as of the data cut-off date stated above. Any results generated after this date are not included unless explicitly noted.

---

*Document generated from cmc-forge Module 3 Workplan Template. All content requires human verification before regulatory submission.*
