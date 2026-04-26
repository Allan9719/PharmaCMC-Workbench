# Stage-Gate Readiness Pack

**DRAFT FOR CONTROLLED REVIEW**

> This document assesses CMC readiness at a defined development stage. It is a decision-support tool, not a decision-maker. All Go/No-Go recommendations must be ratified by the designated governance body. No data has been fabricated; all entries must be verified against source documents.

---

## 1. Objective and Scope

| Field | Value | Guidance |
|-------|-------|----------|
| Product Name | `[INN / code name]` | Use INN if available |
| Drug Type | `[mAb / bispecific / ADC / fusion protein / small molecule / CGT / other]` | Determines regulatory pathway and CMC expectations |
| Current Stage | `[Discovery / Pre-IND / Phase I / Phase II / Phase III / Pre-BLA / Post-approval]` | The stage the product is at NOW |
| Target Gate | `[IND filing / Phase I entry / Phase II entry / Phase III entry / BLA filing / Post-approval change]` | The gate being assessed for readiness |
| Target Region(s) | `[China NMPA/CDE / US FDA / EU EMA / Global / Partner diligence]` | Determines whether readiness is local, global, or partner-facing |
| Company Posture | `[China-only / China-first then global / Global-first with China bridge / Inbound China localization / Outbound licensing]` | Determines if regional deltas must be assessed |
| Assessment Date | `[YYYY-MM-DD]` | Snapshot date for evidence |
| Assessment Lead | `[Name, Title]` | Person accountable for the assessment |
| Assessment Team | `[List names and roles]` | Cross-functional team involved |
| Scope Boundaries | `[e.g., Drug Substance only / DS + DP / Full CMC package]` | What is and is not included |

### Gate Readiness Criteria Overview

This assessment uses a three-tier rating for each evidence dimension:

| Rating | Definition | Gate Decision Impact |
|--------|-----------|---------------------|
| **GREEN** | Evidence is sufficient, complete, and meets stage expectations. No action needed before gate. | Supports "Go" |
| **YELLOW** | Evidence is partially complete or has manageable gaps. Remediation plan exists with timeline. | Supports "Conditional Go" if remediation is achievable within the gate window |
| **RED** | Critical evidence is missing, incomplete, or fails to meet minimum stage expectations. No remediation plan or timeline exists. | Triggers "No-Go" or gate delay |

---

### China / Global Readiness Lens

Use this table when the product is intended for China and at least one international path.

| Lens | GREEN | YELLOW | RED | Current Rating | Evidence / Gap |
|------|-------|--------|-----|----------------|----------------|
| Global core CMC story | Product/process/control strategy narrative is source-backed and reusable across regions | Core story exists but has translation, terminology, or evidence gaps | Region-specific narratives conflict or core evidence is not traceable | `[G/Y/R]` | `[source/gap]` |
| CDE/NMPA readiness | CDE-relevant CTD mapping, China site/MAH info, and local requirements are identified | CDE pathway or local evidence needs are partly defined | China pathway assumptions are unknown or unsupported | `[G/Y/R]` | `[source/gap]` |
| FDA/EMA readiness | FDA/EMA expectations are mapped and evidence upgrade plan exists | Major gaps are known but not yet scheduled | Team assumes CDE package can be reused without gap assessment | `[G/Y/R]` | `[source/gap]` |
| Bilingual terminology control | Controlled Chinese-English term table exists and is used consistently | Term table exists but not applied to all documents | Key CMC terms drift across Chinese and English packages | `[G/Y/R]` | `[source/gap]` |
| Cross-entity data and records | System-of-record, ownership, and audit trail boundaries are defined | Boundaries are understood but not documented | Source data crosses sites/entities without clear controls | `[G/Y/R]` | `[source/gap]` |

---

## 2. Full Evidence Snapshot

For each dimension, provide a current-state assessment with supporting evidence and gap identification. The example entries below illustrate a Phase I IND context — adjust expectations for other stages.

### 2.1 Product Understanding

| Evidence Element | Ready (GREEN) Example | Current State | Gap (if any) | Gap Rating | Source Document |
|------------------|----------------------|---------------|--------------|------------|-----------------|
| Primary structure confirmed (amino acid sequence, MW, pI) | Full sequence confirmed by LC-MS peptide mapping, MW by SEC-MALS, pI by cIEF. Results match expected sequence. | `[describe current state]` | `[describe gap or "None"]` | `[G/Y/R]` | `[report ID]` |
| Higher-order structure characterized | Secondary structure by CD, tertiary structure by intrinsic fluorescence, disulfide mapping by non-reducing peptide mapping. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Post-translational modifications profiled | Glycan profiling by HILIC, charge variants by cIEF/CEX, oxidation and deamidation sites identified by peptide mapping. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Biological activity / potency assay established | Cell-based bioassay or binding assay developed and qualified. Potency of representative batches characterized. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Forced degradation completed | Stress conditions (heat, light, pH, oxidation, reduction) tested. Degradation pathways identified and ranked. Methods shown stability-indicating. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| CQA identification and risk ranking | CQAs identified through risk assessment (e.g., using an Ishikawa + risk ranking matrix). Criticality classification for each attribute. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |

### 2.2 Process — Upstream (USP)

| Evidence Element | Ready (GREEN) Example | Current State | Gap (if any) | Gap Rating | Source Document |
|------------------|----------------------|---------------|--------------|------------|-----------------|
| Cell line and cell bank system established | Single-cell cloned, origin and history documented. MCB manufactured and tested per ICH Q5B/Q5D. At minimum, MCB available (WCB may be post-IND). | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Cell bank characterization complete | Identity (sequence confirmation), purity (sterility, mycoplasma, adventitious agents), viability, genetic stability through end-of-production. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| USP process defined at clinical scale | Seed train, bioreactor parameters (media, feed, temperature, pH, DO), harvest method defined. At least 1 run at clinical scale completed. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| In-process controls identified | Key IPCs defined (cell viability, titer, pH, DO, temperature). Preliminary NOR ranges established from development data. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Raw materials qualified | basal media, feeds, and critical raw materials sourced with CoAs. TSE/BSE risk assessed for animal-derived materials. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |

### 2.3 Process — Downstream (DSP)

| Evidence Element | Ready (GREEN) Example | Current State | Gap (if any) | Gap Rating | Source Document |
|------------------|----------------------|---------------|--------------|------------|-----------------|
| DSP process defined at clinical scale | Purification sequence defined (e.g., Protein A capture → low-pH viral inactivation → CEX polishing → AEX flow-through → viral filtration → UF/DF). Clinical scale executed at least once. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Impurity clearance demonstrated | HCP clearance, DNA clearance, Protein A leaching demonstrated. Viral clearance at least planned (may be post-IND for Phase I with justification). | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Preliminary CPPs identified | CPPs from risk assessment and development data. NOR and preliminary PAR ranges established for critical steps. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Process intermediates defined | Hold times, storage conditions for intermediates (if applicable) established. Intermediate stability data available. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |

### 2.4 Analytical

| Evidence Element | Ready (GREEN) Example | Current State | Gap (if any) | Gap Rating | Source Document |
|------------------|----------------------|---------------|--------------|------------|-----------------|
| Release specification established | Specification with tests for identity, purity, potency, safety, and general tests. Phase-appropriate limits set. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Release methods developed and qualified | All specification methods qualified for intended use (Phase I: qualified; Phase III: validated per ICH Q2). System suitability defined. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Characterization methods available | Methods for extended characterization beyond release (e.g., peptide mapping, glycan profiling, SEC-MALS, DSC). Not required for release but expected for characterization section. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Reference standard available | Primary reference standard characterized and assigned potency. Working standard available for routine use. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Stability-indicating methods confirmed | Forced degradation data demonstrates methods can detect degradation. Required for stability study validity. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |

### 2.5 Stability

| Evidence Element | Ready (GREEN) Example | Current State | Gap (if any) | Gap Rating | Source Document |
|------------------|----------------------|---------------|--------------|------------|-----------------|
| DS stability study initiated | Long-term (e.g., -70C or -20C) and accelerated conditions underway. At least 3 months data available for IND. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| DP stability study initiated | Long-term (e.g., 2-8C) and accelerated conditions underway. At least 1-3 months data for IND. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Proposed storage conditions and shelf life | Preliminary storage conditions supported by available data. Proposed retest period or shelf life stated. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| In-use and shipping stability | In-use stability data available (or planned). Shipping qualification complete or planned. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |

### 2.6 Quality System

| Evidence Element | Ready (GREEN) Example | Current State | Gap (if any) | Gap Rating | Source Document |
|------------------|----------------------|---------------|--------------|------------|-----------------|
| GMP manufacturing capability | Clinical manufacturing under GMP. Qualified facility, equipment, and personnel. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Quality agreements in place | Quality agreements with all contract manufacturers and testing laboratories. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Change control system operational | Change control procedure documented and operational. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Deviation/CAPA system operational | Deviation and CAPA procedures documented and operational. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Analytical laboratory qualified | Laboratory equipment qualified. Methods under change control. OOS procedure in place. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |

### 2.7 Supply Chain

| Evidence Element | Ready (GREEN) Example | Current State | Gap (if any) | Gap Rating | Source Document |
|------------------|----------------------|---------------|--------------|------------|-----------------|
| Clinical supply manufactured and released | At least 1 GMP batch manufactured, tested, and released for clinical use. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Drug product available for clinical study | DP manufactured, packaged, labeled, and released. Quantity sufficient for projected clinical demand. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Cold chain capability established | Storage and shipping conditions validated or qualified. Temperature monitoring in place. | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |
| Single-source dependency identified and mitigated | Any single-source critical raw material identified. Risk mitigation plan in place (safety stock, alternate qualification plan). | `[current state]` | `[gap]` | `[rating]` | `[report ID]` |

### Evidence Summary Scorecard

| Dimension | Total Elements | GREEN | YELLOW | RED | Not Assessed |
|-----------|---------------|-------|--------|-----|--------------|
| Product Understanding | 6 | `[n]` | `[n]` | `[n]` | `[n]` |
| Process — USP | 5 | `[n]` | `[n]` | `[n]` | `[n]` |
| Process — DSP | 4 | `[n]` | `[n]` | `[n]` | `[n]` |
| Analytical | 5 | `[n]` | `[n]` | `[n]` | `[n]` |
| Stability | 4 | `[n]` | `[n]` | `[n]` | `[n]` |
| Quality System | 5 | `[n]` | `[n]` | `[n]` | `[n]` |
| Supply Chain | 4 | `[n]` | `[n]` | `[n]` | `[n]` |
| **TOTAL** | **33** | `[n]` | `[n]` | `[n]` | `[n]` |

---

## 3. Critical Gaps Table

Only gaps rated YELLOW or RED that require action before the gate.

| Gap ID | Dimension | Description | Current Rating | Impact on Gate | Required Action | Owner | Target Resolution Date | Blocking? |
|--------|-----------|-------------|----------------|----------------|-----------------|-------|----------------------|-----------|
| CG-001 | `[e.g., Analytical]` | `[e.g., Potency assay qualification not yet complete; only development data available]` | `[Y/R]` | `[e.g., Cannot release clinical batches without qualified potency assay; blocks IND]` | `[e.g., Complete qualification by date; interim: use development data with protocol commitment]` | `[owner]` | `[date]` | `[Yes / No]` |
| CG-002 | `[dimension]` | `[description]` | `[rating]` | `[impact]` | `[action]` | `[owner]` | `[date]` | `[blocking?]` |
| CG-003 | `[dimension]` | `[description]` | `[rating]` | `[impact]` | `[action]` | `[owner]` | `[date]` | `[blocking?]` |
| CG-004 | `[dimension]` | `[description]` | `[rating]` | `[impact]` | `[action]` | `[owner]` | `[date]` | `[blocking?]` |
| CG-005 | `[dimension]` | `[description]` | `[rating]` | `[impact]` | `[action]` | `[owner]` | `[date]` | `[blocking?]` |

**Impact Classification**:
- **Gate-Blocking**: Must resolve before gate can be passed. Any RED item is gate-blocking by default.
- **Gate-Delaying**: Does not block gate passage but delays execution by defined amount. Must have committed resolution timeline.
- **Non-Blocking**: Can be resolved post-gate with documented commitment. YELLOW items with clear remediation plans may qualify.

---

## 4. Risk Register (FMEA-Style)

| Risk ID | Risk Description | Potential Effect | Severity (S) 1-10 | Likelihood (O) 1-10 | Detectability (D) 1-10 | RPN (SxOxD) | Risk Level | Mitigation Action | Owner | Status |
|---------|-----------------|-------------------|--------------------|---------------------|------------------------|-------------|------------|-------------------|-------|--------|
| FMR-001 | `[e.g., Glycosylation profile drift across manufacturing campaigns]` | `[e.g., Potency variation, immunogenicity risk]` | `[7]` | `[4]` | `[3]` | `[84]` | `[Medium: 1-30 Low, 31-80 Medium, 81-200 High, >200 Critical]` | `[e.g., Implement at-line glycan monitoring; establish alert limits from existing data]` | `[owner]` | `[Open / Mitigated / Accepted]` |
| FMR-002 | `[e.g., Single-source dependency for Protein A resin]` | `[e.g., Supply disruption halts manufacturing]` | `[9]` | `[3]` | `[7]` | `[189]` | `[rating]` | `[e.g., Qualify alternate resin; maintain 6-month safety stock]` | `[owner]` | `[status]` |
| FMR-003 | `[e.g., Stability data insufficient at proposed shelf life]` | `[e.g., Regulatory request for additional data; shortened shelf life]` | `[6]` | `[5]` | `[4]` | `[120]` | `[rating]` | `[e.g., Place additional batches on stability; use accelerated data for preliminary shelf life with commitment]` | `[owner]` | `[status]` |
| FMR-004 | `[e.g., HCP assay coverage not fully characterized]` | `[e.g., Regulatory question on immunogenicity risk from residual HCP]` | `[6]` | `[5]` | `[5]` | `[150]` | `[rating]` | `[e.g., Complete 2D gel/Mass spec coverage study; prepare response strategy]` | `[owner]` | `[status]` |
| FMR-005 | `[e.g., Analytical method transfer to QC lab not complete]` | `[e.g., Cannot release clinical batches at manufacturing site]` | `[8]` | `[3]` | `[3]` | `[72]` | `[rating]` | `[e.g., Prioritize method transfer; interim testing at development lab under GMP]` | `[owner]` | `[status]` |
| FMR-006 | `[description]` | `[effect]` | `[S]` | `[O]` | `[D]` | `[RPN]` | `[rating]` | `[mitigation]` | `[owner]` | `[status]` |
| FMR-007 | `[description]` | `[effect]` | `[S]` | `[O]` | `[D]` | `[RPN]` | `[rating]` | `[mitigation]` | `[owner]` | `[status]` |
| FMR-008 | `[description]` | `[effect]` | `[S]` | `[O]` | `[D]` | `[RPN]` | `[rating]` | `[mitigation]` | `[owner]` | `[status]` |

**Severity Scale (S)**: 1-2 Negligible | 3-4 Minor | 5-6 Moderate | 7-8 Major | 9-10 Critical/Hazardous
**Occurrence Scale (O)**: 1-2 Remote | 3-4 Low | 5-6 Moderate | 7-8 High | 9-10 Very High
**Detectability Scale (D)**: 1-2 Very easily detected | 3-4 Easily detected | 5-6 Moderately detectable | 7-8 Hardly detectable | 9-10 Undetectable
**RPN Thresholds**: 1-30 = Low (monitor) | 31-80 = Medium (plan mitigation) | 81-200 = High (mitigate before gate) | >200 = Critical (must resolve)

---

## 5. Priority Action Package

### Next 30 Days

| Action ID | Action | Linked Gap/Risk | Owner | Deliverable | Due Date | Status |
|-----------|--------|-----------------|-------|-------------|----------|--------|
| ACT-001 | `[e.g., Complete potency assay qualification]` | `[CG-001]` | `[owner]` | `[e.g., Qualified method report]` | `[date]` | `[Not started / In progress / Complete]` |
| ACT-002 | `[e.g., Manufacture and release clinical DS batch]` | `[CG-xxx]` | `[owner]` | `[e.g., Batch release documentation]` | `[date]` | `[status]` |
| ACT-003 | `[action]` | `[linked item]` | `[owner]` | `[deliverable]` | `[date]` | `[status]` |

### Next 60 Days

| Action ID | Action | Linked Gap/Risk | Owner | Deliverable | Due Date | Status |
|-----------|--------|-----------------|-------|-------------|----------|--------|
| ACT-004 | `[e.g., Complete DP formulation and fill]` | `[CG-xxx]` | `[owner]` | `[deliverable]` | `[date]` | `[status]` |
| ACT-005 | `[e.g., Initiate formal stability studies]` | `[CG-xxx]` | `[owner]` | `[deliverable]` | `[date]` | `[status]` |
| ACT-006 | `[action]` | `[linked item]` | `[owner]` | `[deliverable]` | `[date]` | `[status]` |

### Next 90 Days

| Action ID | Action | Linked Gap/Risk | Owner | Deliverable | Due Date | Status |
|-----------|--------|-----------------|-------|-------------|----------|--------|
| ACT-007 | `[e.g., Compile Module 3 draft for IND filing]` | `[CG-xxx]` | `[owner]` | `[deliverable]` | `[date]` | `[status]` |
| ACT-008 | `[e.g., Complete viral clearance study (if deferred from IND)]` | `[CG-xxx]` | `[owner]` | `[deliverable]` | `[date]` | `[status]` |
| ACT-009 | `[action]` | `[linked item]` | `[owner]` | `[deliverable]` | `[date]` | `[status]` |

---

## 6. Decision Recommendation

### Gate Decision Criteria

| Criterion | Go | Conditional Go | No-Go |
|-----------|-----|---------------|-------|
| RED items | Zero RED items | Zero RED items that are gate-blocking; non-blocking REDs have committed remediation plan | Any gate-blocking RED item with no remediation plan |
| YELLOW items | Zero YELLOW items | YELLOW items have documented remediation plan with timeline achievable before next gate | YELLOW items exceed 50% of total with no prioritized plan |
| Clinical supply | Available and released | Available with minor labeling or packaging actions remaining | Not manufactured or not released |
| Regulatory submission readiness | Module 3 skeleton complete; source docs identified | Module 3 in progress; key source docs identified; missing items tracked | Module 3 not started or major source docs missing |
| Risk posture | All High/Critical risks mitigated | High risks mitigated; Critical risks have active mitigation with committed timeline | Critical risks unmitigated |

### Recommendation

| Field | Value |
|-------|-------|
| Overall Recommendation | `[GO / CONDITIONAL GO / NO-GO]` |
| Rationale | `[2-4 sentence summary of why this recommendation is made]` |
| Conditions (if Conditional Go) | `[List specific conditions that must be met, with dates]` |
| Key Risks to Monitor Post-Gate | `[List top 3 risks to track]` |
| Recommended By | `[Name, Title, Date]` |
| Approved By | `[Name, Title, Date]` |

---

## 7. Human Review Matrix

| Role | Review Scope | Review Type | Required Before | Sign-Off Required |
|------|-------------|-------------|-----------------|-------------------|
| **CMC Lead** | Full assessment accuracy, gap prioritization, gate recommendation | Technical + strategic | Gate decision meeting | Yes — accountable for recommendation |
| **QA Head or Designee** | GMP compliance gaps, quality system readiness, deviation/CAPA posture | Compliance | Gate decision meeting | Yes — must confirm quality system acceptable for stage |
| **Regulatory Affairs (RA) CMC** | Regulatory strategy alignment, Module 3 readiness, pre-submission meeting readiness | Regulatory | Gate decision meeting | Yes — must confirm regulatory package on track |
| **Analytical Lead** | Method readiness, specification soundness, stability data adequacy | Technical | Gate decision meeting | Yes — must confirm analytical package supports stage |
| **Process Development Lead** | Process understanding, scale-up readiness, CPP/CQA linkage | Technical | Gate decision meeting | Advisory — informs CMC Lead decision |
| **Supply Chain Lead** | Raw material availability, manufacturing slot, cold chain | Operational | Gate decision meeting | Advisory — informs Go/No-Go on supply readiness |
| **Toxicology / Nonclinical (if applicable)** | Any CMC data supporting nonclinical study (e.g., test article characterization) | Cross-functional | IND filing (if applicable) | Advisory — confirms CMC-nonclinical alignment |
| **Clinical Operations (if applicable)** | Clinical supply availability and labeling | Operational | IND filing / clinical study start | Advisory — confirms clinical supply readiness |

**Review Process**:
1. Assessment lead distributes draft pack to all reviewers minimum 5 business days before gate meeting.
2. Each reviewer returns comments within 3 business days.
3. Assessment lead incorporates comments and resolves conflicts.
4. Final pack distributed 2 business days before gate meeting.
5. Gate meeting: present recommendation, discuss open issues, ratify decision.
6. Decision documented and distributed within 2 business days of meeting.

---

## 8. Appendix: Stage-Specific Expectations Quick Reference

| Evidence Dimension | Phase I IND (Minimum) | Phase III / Pre-BLA (Expected) | Post-Approval Change |
|--------------------|-----------------------|-------------------------------|---------------------|
| Product characterization | Primary structure + key PTMs + forced degradation | Full characterization suite + clinical correlation | Affected attributes + comparability |
| Process definition | Clinical-scale process defined; preliminary CPPs | Commercial-scale validated; design space (if QbD); PPQ complete | Changed steps characterized; comparability demonstrated |
| Analytical methods | Qualified for intended use | Validated per ICH Q2; lifecycle management per Q14 | Validated for changed product; method comparability |
| Stability | 3-6 months long-term + accelerated initiated | Full shelf-life data; statistical estimation per Q1E | Affected conditions; comparability stability |
| Specifications | Phase-appropriate; clinically justified | Comprehensive; justified by manufacturing experience + clinical data | Affected tests; comparability criteria |
| Process validation | Not required at IND | Stage 1 (design) + Stage 2 (PPQ, min 3 batches) complete | Affected steps re-validated |
| Viral safety | Strategy defined; clearance planned | Full viral clearance data; ICH Q5A(R2) compliant | Re-evaluation if process change affects clearance steps |

---

*Document generated from cmc-forge Stage-Gate Readiness Template. All content requires human verification and sign-off before gate decision.*
