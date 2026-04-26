# Process Performance Qualification (PPQ) Protocol Framework

**DRAFT FOR CONTROLLED REVIEW**

> This document provides a framework for structuring a PPQ protocol. It is a scaffold, not a validated document. All process-specific details, acceptance criteria, and sampling plans must be defined by qualified SMEs and approved per the site's document control procedure. No data has been fabricated or assumed; all entries must reflect actual process knowledge.

---

## 1. Protocol Header

| Field | Value | Guidance |
|-------|-------|----------|
| Protocol Number | `[PV-PRO-YYYY-NNN]` | Per site document numbering convention |
| Product Name | `[INN / code name]` | Use INN if available |
| Drug Type | `[mAb / bispecific / ADC / fusion protein / other]` | Determines CQA/CPP framework |
| Dosage Form | `[Solution for injection / Lyophilized powder / PFS]` | Affects DP-specific validation requirements |
| Protocol Title | `[e.g., "Process Performance Qualification Protocol for [Product Name] Drug Substance Manufacturing at [Site]"]` | Be specific and include scope |
| Protocol Version | `[1.0]` | Increment per site SOP |
| Protocol Status | `[Draft / Under Review / Approved / Executed / Superseded]` | Current lifecycle status |
| Manufacturing Site | `[Site name and address]` | Where PPQ will be executed |
| Manufacturing Scale | `[e.g., 2000 L bioreactor / 500 L]` | Must match commercial scale |
| Process Stage | `[Drug Substance / Drug Product / DS + DP]` | Scope of validation |
| Author | `[Name, Title]` | Protocol author |
| Reviewed By | `[Names, Titles]` | Technical review |
| Approved By | `[Name, Title]` | QA or Validation Head |
| Approval Date | `[YYYY-MM-DD]` | Date of formal approval |
| Effective Date | `[YYYY-MM-DD]` | Date protocol becomes effective for execution |

---

## 2. Objective and Scope

### 2.1 Objective

This protocol defines the requirements and acceptance criteria for Process Performance Qualification (PPQ) of `[Product Name]` `[Drug Substance / Drug Product]` manufacturing at `[Site Name]`. The objective is to demonstrate that the commercial manufacturing process, executed under standard operating conditions by trained personnel using qualified equipment, consistently produces product meeting its predetermined specifications and quality attributes.

### 2.2 Scope

| Scope Element | Included | Notes |
|--------------|----------|-------|
| Drug Substance manufacturing | `[Yes / No]` | `[Specify scope if partial]` |
| Drug Product manufacturing | `[Yes / No]` | `[Specify scope if partial]` |
| Process steps validated | `[e.g., All DS steps from cell thaw through DS bulk fill]` | `[List any excluded steps and rationale]` |
| Manufacturing scale | `[Commercial scale: XXX L bioreactor]` | `[PPQ must be at commercial scale per FDA guidance]` |
| Number of PPQ batches | `[Minimum 3; propose [N]]` | `[See Section 5 for statistical justification]` |
| Analytical methods | `[All release and in-process methods as specified]` | `[Methods must be validated per ICH Q2 prior to PPQ]` |
| Equipment | `[List key equipment qualified for this process]` | `[Must be IQ/OQ/PQ complete before PPQ]` |

### 2.3 Prerequisites

| Prerequisite | Status | Verification Document | Verified By | Date |
|-------------|--------|----------------------|-------------|------|
| Facility qualified (HVAC, utilities) | `[ ] Complete` | `[Doc ID]` | `[name]` | `[date]` |
| Equipment IQ/OQ/PQ complete | `[ ] Complete` | `[Doc IDs]` | `[name]` | `[date]` |
| Analytical methods validated | `[ ] Complete` | `[Validation report IDs]` | `[name]` | `[date]` |
| Cleaning validation complete | `[ ] Complete` | `[Doc ID]` | `[name]` | `[date]` |
| Aseptic process simulation complete | `[ ] Complete (DP only)` | `[Doc ID]` | `[name]` | `[date]` |
| Staff training complete | `[ ] Complete` | `[Training records]` | `[name]` | `[date]` |
| Batch records approved | `[ ] Complete` | `[Batch record version]` | `[name]` | `[date]` |
| Raw materials qualified and available | `[ ] Complete` | `[CoA, qualification docs]` | `[name]` | `[date]` |
| Process development data reviewed | `[ ] Complete` | `[Development report ID]` | `[name]` | `[date]` |
| Risk assessment complete (CPP/CQA linkage) | `[ ] Complete` | `[Risk assessment ID]` | `[name]` | `[date]` |
| Quality agreement in place (if contract site) | `[ ] Complete` | `[QA agreement ID]` | `[name]` | `[date]` |

---

## 3. Process Description

### 3.1 Process Overview

`[Provide a narrative description of the manufacturing process. This should match the registered process description in Module 3, Section 3.2.S.2.2 or 3.2.P.3.3.]`

### 3.2 Process Flow Diagram

`[Insert or reference the process flow diagram. Must match the registered flow diagram in Module 3. Each unit operation should be numbered for reference in sampling and testing tables.]`

### 3.3 Unit Operations Summary

| Step # | Unit Operation | Equipment | Scale / Batch Size | Key Parameters |
|--------|---------------|-----------|-------------------|----------------|
| 1 | Cell thaw and expansion | `[e.g., T-flask, shake flask, bioreactor]` | `[scale]` | `[e.g., Temperature, pH, seeding density]` |
| 2 | Seed bioreactor | `[e.g., 50 L single-use bioreactor]` | `[scale]` | `[e.g., Temperature, pH, DO, agitation]` |
| 3 | Production bioreactor | `[e.g., 2000 L single-use bioreactor]` | `[2000 L]` | `[e.g., Temperature, pH, DO, feed strategy]` |
| 4 | Harvest (centrifugation + depth filtration) | `[e.g., Centrifuge, depth filter]` | `[scale]` | `[e.g., Flow rate, pressure]` |
| 5 | Protein A capture chromatography | `[e.g., Chromatography column]` | `[e.g., 30 cm bed height, 45 cm diameter]` | `[e.g., Load challenge, wash volume, elution pH]` |
| 6 | Low-pH viral inactivation | `[e.g., Hold tank]` | `[scale]` | `[e.g., pH 3.5 +/- 0.1, 60 +/- 5 min]` |
| 7 | CEX polishing chromatography | `[e.g., Chromatography column]` | `[scale]` | `[e.g., Load pH, conductivity, gradient]` |
| 8 | AEX flow-through chromatography | `[e.g., Chromatography column]` | `[scale]` | `[e.g., Load pH, conductivity, flow rate]` |
| 9 | Viral filtration | `[e.g., 20 nm filter]` | `[scale]` | `[e.g., Pressure, volume processed]` |
| 10 | UF/DF | `[e.g., TFF system]` | `[scale]` | `[e.g., Concentration factor, diafiltration volumes]` |
| 11 | Bulk fill | `[e.g., Aseptic fill into bags]` | `[scale]` | `[e.g., Fill volume, filter integrity]` |

### 3.4 Critical Process Parameters (CPP) Table

| Parameter | Unit Operation | NOR (Normal Operating Range) | PAR (Proven Acceptable Range) | Classification | Linked CQA(s) | Justification Reference |
|-----------|---------------|------------------------------|-------------------------------|----------------|---------------|------------------------|
| `[e.g., Bioreactor temperature]` | `[e.g., Production bioreactor]` | `[e.g., 36.5-37.5C]` | `[e.g., 35.0-38.0C]` | `[CPP]` | `[e.g., Glycosylation, titer]` | `[e.g., Process characterization study PCS-001]` |
| `[e.g., pH setpoint]` | `[e.g., Production bioreactor]` | `[e.g., 6.90-7.10]` | `[e.g., 6.80-7.20]` | `[CPP]` | `[e.g., Charge variants, glycosylation]` | `[reference]` |
| `[e.g., Feed addition timing]` | `[e.g., Production bioreactor]` | `[e.g., Day 3, 5, 7]` | `[e.g., Day 2-4, 4-6, 6-8]` | `[CPP]` | `[e.g., Titer, glycosylation]` | `[reference]` |
| `[e.g., Protein A load challenge]` | `[Protein A capture]` | `[e.g., 30-40 g/L]` | `[e.g., 25-45 g/L]` | `[CPP]` | `[e.g., HCP clearance, yield]` | `[reference]` |
| `[e.g., Low-pH hold time]` | `[Viral inactivation]` | `[e.g., 55-65 min]` | `[e.g., 50-70 min]` | `[CPP]` | `[e.g., Viral clearance, aggregation]` | `[reference]` |
| `[e.g., Low-pH hold pH]` | `[Viral inactivation]` | `[e.g., 3.4-3.6]` | `[e.g., 3.3-3.7]` | `[CPP]` | `[e.g., Viral clearance, aggregation]` | `[reference]` |
| `[e.g., DF volume (diavolumes)]` | `[UF/DF]` | `[e.g., 8-10 DV]` | `[e.g., 7-12 DV]` | `[CPP]` | `[e.g., Buffer exchange completeness]` | `[reference]` |
| `[parameter]` | `[step]` | `[NOR]` | `[PAR]` | `[classification]` | `[CQAs]` | `[reference]` |

**NOR vs. PAR Note**: NOR is the range used during routine manufacturing. PAR is the wider range within which the process has been shown to produce acceptable product. During PPQ, parameters should be controlled within NOR. Excursions outside NOR but within PAR should be documented and evaluated but do not necessarily invalidate the batch.

---

## 4. Sampling Plan

### 4.1 Sampling Plan Overview

| Unit Operation | Sampling Purpose | Sampling Points | Sample Type | Sample Volume | Frequency |
|---------------|-----------------|----------------|-------------|---------------|-----------|
| Production bioreactor | Process monitoring | `[e.g., Daily from Day 0 to harvest]` | `[e.g., Cell culture supernatant]` | `[e.g., 5 mL]` | `[e.g., Daily]` |
| Harvest | IPC testing | `[e.g., Post-centrifugation, post-depth filtration]` | `[e.g., Clarified harvest]` | `[e.g., 50 mL]` | `[Per batch]` |
| Protein A capture | IPC + yield tracking | `[e.g., Load, flow-through, wash, elution fractions]` | `[e.g., Liquid fractions]` | `[e.g., Per fraction]` | `[Per batch, per column cycle]` |
| Viral inactivation | IPC confirmation | `[e.g., Pre-hold, post-hold]` | `[e.g., Process intermediate]` | `[e.g., 10 mL]` | `[Per batch]` |
| CEX polishing | IPC testing | `[e.g., Load, flow-through, elution fractions]` | `[e.g., Liquid fractions]` | `[e.g., Per fraction]` | `[Per batch]` |
| AEX flow-through | IPC testing | `[e.g., Load, flow-through, wash]` | `[e.g., Liquid fractions]` | `[e.g., Per fraction]` | `[Per batch]` |
| Viral filtration | IPC + filter integrity | `[e.g., Pre-filtration, post-filtration]` | `[e.g., Process intermediate]` | `[e.g., 20 mL]` | `[Per batch]` |
| UF/DF | IPC testing | `[e.g., Pre-concentration, post-concentration, post-DF, final bulk]` | `[e.g., Process intermediate]` | `[e.g., 10 mL per point]` | `[Per batch]` |
| Bulk DS | Release testing | `[e.g., Final bulk container, top/middle/bottom]` | `[e.g., DS bulk]` | `[e.g., Per specification requirements]` | `[Per batch]` |

### 4.2 Detailed Sampling Guidance

**Where to sample**:
- Sample at every process step boundary (entry and exit of each unit operation)
- Sample at every IPC point identified in the batch record
- For bulk containers: sample from top, middle, and bottom for homogeneity verification
- For chromatography: collect fractions across the peak to assess pooling consistency
- For UF/DF: sample before and after concentration, after each diavolume milestone, and at final bulk

**How many sampling points**:
- **Bioreactor**: Daily sampling from inoculation through harvest (typically 12-16 timepoints)
- **Chromatography steps**: At minimum, sample load, flow-through, wash, and elution peak fractions. For PPQ, consider additional in-peak sampling (e.g., early, mid, late peak) to assess peak shape consistency
- **Viral inactivation**: Minimum 2 points (pre-hold, post-hold). Consider midpoint sampling for large volumes
- **UF/DF**: Minimum 4 points (pre-concentration, post-concentration, post-DF, final bulk)
- **Bulk DS**: Minimum 3 points per container (top, middle, bottom) for homogeneity

**Common Pitfall**: Sampling only at the start and end of unit operations. Intermediate sampling during PPQ provides data for future process optimization and troubleshooting, even if not required for release. It is much easier to collect extra samples during PPQ than to repeat the run later.

---

## 5. Statistical Justification for Number of Batches

### 5.1 Batch Number Determination

Per FDA Process Validation Guidance (2011, revised): "The number of batches should be sufficient to provide sufficient statistical confidence in the data." The minimum is typically 3 consecutive batches, but the number should be justified based on process understanding, risk, and statistical requirements.

| Approach | Description | When to Use |
|----------|-------------|-------------|
| **Minimum 3 batches** | Industry standard minimum; 3 consecutive successful batches | Well-characterized process with extensive development data; low process variability |
| **Risk-based determination** | Number based on risk assessment (higher risk = more batches) | New process, limited development data, high CQA criticality |
| **Statistical power approach** | Number determined by desired confidence level and power to detect process drift | Quantitative approach for critical CQAs |
| **Regulatory expectation** | Based on pre-submission discussions or regional guidance | When specific regulatory authority has stated expectations |

### 5.2 Statistical Confidence/Power Framework

| Desired Confidence Level | Desired Power | Expected Process Variability (%CV) | Detectable Shift (multiples of SD) | Minimum Batches Required |
|------------------------|---------------|-----------------------------------|------------------------------------|-------------------------|
| 90% | 80% | 5% (low) | 1.5 SD | 3 |
| 90% | 80% | 10% (moderate) | 1.5 SD | 4 |
| 90% | 80% | 15% (high) | 1.5 SD | 5 |
| 95% | 80% | 5% (low) | 1.0 SD | 5 |
| 95% | 80% | 10% (moderate) | 1.0 SD | 7 |
| 95% | 90% | 10% (moderate) | 1.0 SD | 9 |
| 95% | 80% | 5% (low) | 1.5 SD | 3 |
| 95% | 80% | 10% (moderate) | 1.5 SD | 5 |

**Note**: These are guidelines. Work with your site statistician to determine the appropriate batch number for your specific process and CQA variability. The above table assumes a two-sided tolerance interval approach.

### 5.3 Batch Number Justification for This Protocol

| Field | Value |
|-------|-------|
| Proposed Number of PPQ Batches | `[N]` |
| Justification | `[e.g., "Based on 3 years of development data across 15 pilot-scale and 3 clinical-scale batches showing process %CV <10% for all CQAs, 3 consecutive PPQ batches at commercial scale are sufficient to demonstrate process consistency with 90% confidence."]` |
| Batch Sequence | `[e.g., Consecutive; no more than X weeks between batches]` |
| Batch Size(s) | `[e.g., All at full commercial scale of XXX L]` |
| Statistical Reference | `[e.g., Site validation master plan; statistical analysis report SAR-XXX]` |

---

## 6. Acceptance Criteria

### 6.1 Tiered Acceptance Criteria Framework

The acceptance criteria are organized into three tiers of increasing rigor. All three tiers must be evaluated for a complete PPQ assessment.

---

### Tier 1: Conformance (Specification Compliance)

**Definition**: Each individual PPQ batch must meet all registered release specifications. This is the minimum requirement -- if a batch fails specification, the PPQ fails.

**Example criteria for a monoclonal antibody drug substance**:

| Test | Acceptance Criterion | Specification Reference |
|------|---------------------|----------------------|
| Appearance | Clear to slightly opalescent, colorless to pale yellow, essentially free from visible particulates | `[Spec ID, version]` |
| Identity (peptide mapping) | Matches reference standard | `[Spec ID]` |
| Purity (% monomer by SEC-HPLC) | >= 95.0% | `[Spec ID]` |
| Aggregates (% HMW by SEC-HPLC) | <= 3.0% | `[Spec ID]` |
| Fragments (% LMW by SEC-HPLC) | <= 5.0% | `[Spec ID]` |
| Charge variants -- acidic species | <= 25.0% | `[Spec ID]` |
| Charge variants -- main peak | >= 60.0% | `[Spec ID]` |
| Potency (cell-based bioassay) | 80-120% relative potency | `[Spec ID]` |
| HCP | <= 100 ng/mg | `[Spec ID]` |
| Host cell DNA | <= 10 pg/mg | `[Spec ID]` |
| Protein A leaching | <= 5 ng/mg | `[Spec ID]` |
| Endotoxin | <= 0.5 EU/mg | `[Spec ID]` |
| Sterility | Negative (no growth) | `[Spec ID]` |
| pH | 5.5-6.5 | `[Spec ID]` |
| Concentration (protein content) | `[e.g., 45.0-55.0 mg/mL]` | `[Spec ID]` |
| Osmolality | `[e.g., 280-320 mOsm/kg]` | `[Spec ID]` |
| Subvisible particles >= 10 um | <= 6000 particles/container | `[Spec ID]` |
| Subvisible particles >= 25 um | <= 600 particles/container | `[Spec ID]` |

**Tier 1 Verdict**: `[PASS if all batches meet all specifications. FAIL if any batch fails any specification.]`

---

### Tier 2: Consistency (Inter-Batch Variability)

**Definition**: Evaluates whether the PPQ batches demonstrate consistent process performance by examining inter-batch variability. Consistency means the process is not drifting and is producing comparable results batch-to-batch.

| Metric | Guidance | Acceptance Criterion Template |
|--------|----------|------------------------------|
| %RSD for critical CQAs | Calculate %RSD across all PPQ batches for each critical CQA | `[e.g., %RSD <= 10% for purity; %RSD <= 15% for potency; %RSD <= 20% for HCP]` |
| Range width relative to specification | Compare the observed range across PPQ batches to the specification width | `[e.g., Observed range should be <= 50% of specification width for critical CQAs]` |
| Inter-batch comparison | Visual and statistical comparison of batch profiles (e.g., chromatograms, bioreactor trends) | `[e.g., Overlay plots show consistent profiles; no unexplained batch-to-batch shifts]` |
| Step yield consistency | %RSD for each process step yield and overall yield | `[e.g., Step yield %RSD <= 15%; overall yield %RSD <= 10%]` |
| IPC trend consistency | In-process control results across batches | `[e.g., No adverse trends; all IPCs within acceptance criteria for all batches]` |
| CPP control consistency | Verify all CPPs were maintained within NOR | `[e.g., All CPPs within NOR for all batches; no CPP excursions requiring investigation]` |

**%RSD Guidance by CQA Type**:

| CQA Category | Typical %RSD Expectation (PPQ) | Concerning %RSD | Action if Exceeding |
|-------------|-------------------------------|-----------------|-------------------|
| Potency (bioassay) | <= 10% | > 15% | Investigate method variability and process variability; may need additional batches |
| Purity (SEC monomer) | <= 2% | > 5% | Investigate process consistency for aggregation control |
| Charge variants | <= 10% | > 20% | Evaluate cell culture consistency; check feed strategy |
| Glycosylation (major species) | <= 10% | > 20% | Evaluate cell culture conditions and raw material consistency |
| HCP | <= 25% | > 40% | Investigate chromatography step consistency; evaluate ELISA variability |
| Process yields (overall) | <= 10% | > 20% | Investigate step yield variability; identify root cause of inconsistency |

**Inter-Batch Comparison Methods**:
- **Visual overlay**: Chromatograms, sensor trends, and IPC profiles overlaid across batches
- **Equivalence testing**: If sufficient batches, test whether batch means are statistically equivalent (e.g., using tolerance intervals)
- **Range comparison**: Observed range across PPQ batches should be narrower than development historical range

**Tier 2 Verdict**: `[PASS if all consistency criteria met. CONDITIONAL if minor exceedances with justified root cause. FAIL if significant inconsistency indicating process not in control.]`

---

### Tier 3: Process Capability

**Definition**: Assesses whether the process, based on PPQ data, is capable of consistently meeting specifications long-term. This tier uses process capability indices (Cp, Cpk) and tolerance intervals.

| Metric | Target | Calculation Approach | Minimum Data Requirement |
|--------|--------|---------------------|-------------------------|
| **Cpk (Process Capability Index)** | Cpk >= 1.0 (minimum); Cpk >= 1.33 (target) | Cpk = min[(USL - mean) / (3 x SD), (mean - LSL) / (3 x SD)] | Minimum 3 batches; more reliable with 5+ |
| **Cp (Process Capability)** | Cp >= 1.0 (minimum); Cp >= 1.33 (target) | Cp = (USL - LSL) / (6 x SD) | Same as Cpk |
| **Tolerance interval coverage** | 95% confidence / 99% coverage (typical) | Calculate tolerance interval that covers 99% of the population with 95% confidence | Minimum 3 batches; interval width decreases with more batches |
| **Specification utilization** | Observed mean should be near center of specification | Distance from mean to nearest specification limit as % of specification width | Any number of batches |

**Cpk Interpretation**:

| Cpk Value | Interpretation | PPQ Assessment |
|-----------|---------------|----------------|
| Cpk < 1.0 | Process is not capable; significant risk of out-of-specification results | FAIL -- Process needs improvement before routine manufacturing |
| 1.0 <= Cpk < 1.33 | Process is marginally capable; some risk of OOS results | CONDITIONAL -- Acceptable with enhanced monitoring; process improvement recommended |
| 1.33 <= Cpk < 1.67 | Process is capable; low risk of OOS results | PASS -- Proceed with routine manufacturing and standard monitoring |
| Cpk >= 1.67 | Process is highly capable; very low risk of OOS results | PASS -- Excellent process control |

**Important Note on Sample Size**: Cpk calculated from 3 batches has very wide confidence intervals. A Cpk of 1.33 from 3 batches could have a true Cpk as low as 0.6 or as high as 3.0. Report Cpk with confidence intervals and state that it will be refined during continued process verification (Stage 3). Do not make definitive capability claims from 3-batch PPQ data alone.

**Cpk Calculation Template** (for each critical CQA):

| CQA | USL | LSL | Mean (PPQ batches) | SD (PPQ batches) | Cp | Cpk | 95% CI for Cpk | Assessment |
|-----|-----|-----|--------------------|--------------------|----|----|----------------|------------|
| Purity (% monomer) | `[e.g., 100%]` | `[e.g., 95.0%]` | `[e.g., 97.2%]` | `[e.g., 0.5%]` | `[calc]` | `[calc]` | `[calc]` | `[Pass / Conditional / Fail]` |
| Potency (%) | `[e.g., 120%]` | `[e.g., 80%]` | `[e.g., 101%]` | `[e.g., 5%]` | `[calc]` | `[calc]` | `[calc]` | `[assessment]` |
| HCP (ng/mg) | `[e.g., 100]` | `[e.g., 0]` | `[e.g., 25]` | `[e.g., 8]` | `[calc]` | `[calc]` | `[calc]` | `[assessment]` |
| Aggregates (%) | `[e.g., 3.0%]` | `[e.g., 0%]` | `[e.g., 1.2%]` | `[e.g., 0.3%]` | `[calc]` | `[calc]` | `[calc]` | `[assessment]` |

**Tier 3 Verdict**: `[PASS if all Cpk >= 1.0 and tolerance intervals within specification. CONDITIONAL if Cpk 1.0-1.33 with enhanced monitoring plan. FAIL if any Cpk < 1.0.]`

---

### 6.2 Overall PPQ Acceptance Decision

| Criterion | Required Outcome | Actual | Pass/Fail |
|-----------|-----------------|--------|-----------|
| Tier 1: All batches meet specification | All PPQ batches pass all specification tests | `[result]` | `[ ] Pass / [ ] Fail` |
| Tier 2: Inter-batch consistency | %RSD within targets; no adverse trends | `[result]` | `[ ] Pass / [ ] Conditional / [ ] Fail` |
| Tier 3: Process capability | Cpk >= 1.0 for all critical CQAs | `[result]` | `[ ] Pass / [ ] Conditional / [ ] Fail` |
| CPP control | All CPPs within NOR for all batches | `[result]` | `[ ] Pass / [ ] Fail` |
| IPC compliance | All IPCs within acceptance criteria | `[result]` | `[ ] Pass / [ ] Fail` |
| No critical deviations | No unresolved critical deviations | `[result]` | `[ ] Pass / [ ] Fail` |
| Batch records complete | All batch records reviewed and approved | `[result]` | `[ ] Pass / [ ] Fail` |

**Overall PPQ Verdict**: `[PASS / CONDITIONAL PASS / FAIL]`

**Conditions (if Conditional Pass)**:
- `[List specific conditions that must be met, e.g., enhanced monitoring for X CQA for first N commercial batches]`

---

## 7. Deviation Classification and Escalation Matrix

| Deviation Category | Definition | Impact on PPQ Batch | Escalation | Resolution Required Before |
|-------------------|-----------|---------------------|------------|---------------------------|
| **Critical** | Deviation that directly affects product quality, safety, or efficacy. Examples: CPP outside PAR, sterility failure, specification failure, unauthorized process change. | Batch may be rejected. PPQ may fail. | Immediate notification to QA Head, Validation Lead, CMC Lead. Investigation initiated within 24 hours. | Batch disposition. PPQ report cannot be finalized. |
| **Major** | Deviation that may affect product quality. CPP within PAR but outside NOR. IPC excursion. Unplanned hold time extension within validated range. | Batch is investigational. Quality impact assessment required. | Notification to QA within 24 hours. Investigation within 5 business days. | Batch disposition. May be resolved concurrent with PPQ execution if non-blocking. |
| **Minor** | Deviation with no expected quality impact. Documentation error corrected. Observation that does not affect process or product. | Batch is acceptable with documentation. | Notification to QA within batch record review cycle. Documented in batch record. | Batch release. |

### Escalation Path

```
Minor deviation
    --> Documented in batch record
    --> Reviewed during batch record review
    --> No impact on PPQ outcome

Major deviation
    --> QA notified within 24 hours
    --> Quality impact assessment within 5 business days
    --> If quality impact confirmed: escalate to Critical
    --> If no quality impact: document resolution, proceed with PPQ
    --> Include in PPQ report

Critical deviation
    --> QA Head and Validation Lead notified immediately
    --> Formal investigation initiated within 24 hours
    --> CMC Lead informed
    --> Batch disposition decision by QA Head
    --> PPQ batch may be invalidated
    --> If PPQ batch invalidated: replacement batch required
    --> Regulatory notification assessment by RA
```

---

## 8. Protocol Amendment Procedure

| Condition | Action | Approval Required | Documentation |
|-----------|--------|-------------------|---------------|
| Typographical or formatting error with no technical impact | Minor amendment | QA reviewer approval | Amendment log entry |
| Change to sampling points (additional sampling) | Amendment with justification | Validation Lead + QA | Amendment form, risk assessment |
| Change to acceptance criteria (tightening) | Amendment with justification | Validation Lead + QA + CMC Lead | Amendment form, rationale document |
| Change to acceptance criteria (widening) | NOT permitted during PPQ execution. Requires new protocol. | N/A -- write new protocol | New protocol version |
| Change to number of batches (increase) | Amendment with justification | Validation Lead + QA | Amendment form, updated statistical justification |
| Change to number of batches (decrease) | NOT permitted. Minimum 3 batches required. | N/A | N/A |
| Unplanned process change during PPQ | Deviation + impact assessment + possible protocol amendment | QA Head + Validation Lead + CMC Lead | Deviation report, amendment if needed |
| Equipment failure during PPQ batch | Deviation + repair/requalification + impact assessment | QA Head | Deviation report; batch disposition decision |

**Amendment Log**:

| Amendment # | Date | Description | Rationale | Approved By | Approval Date |
|-------------|------|-------------|-----------|-------------|---------------|
| 001 | `[date]` | `[description]` | `[rationale]` | `[name]` | `[date]` |
| 002 | `[date]` | `[description]` | `[rationale]` | `[name]` | `[date]` |

---

## 9. Continued Process Verification (Stage 3) Plan Summary

While detailed Stage 3 planning is outside the scope of this PPQ protocol, the following elements should be addressed to ensure a smooth transition:

| Element | Description | Status |
|---------|-------------|--------|
| Statistical monitoring plan | Control charts, trending, alert/action limits for CPPs and CQAs | `[ ] Planned / [ ] Documented in separate CPV protocol]` |
| Number of batches for enhanced monitoring | `[e.g., First 10 commercial batches or first 12 months]` | `[defined or to be defined]` |
| Annual product quality review integration | How PPQ and CPV data feed into APQR | `[planned]` |
| Process capability reassessment | When and how Cpk will be recalculated with accumulated data | `[planned]` |
| Change control threshold | Criteria for when CPV data triggers a change control | `[planned]` |

---

## 10. References

| Reference | Document ID / Version | Relevance |
|-----------|----------------------|-----------|
| FDA Process Validation Guidance | January 2011, revised | Defines Stage 1-3 lifecycle approach |
| ICH Q8(R2) | Pharmaceutical Development | QbD, design space, CQAs, CPPs |
| ICH Q9 | Quality Risk Management | Risk assessment tools and methodology |
| ICH Q10 | Pharmaceutical Quality System | Knowledge management, continuous improvement |
| ICH Q11 | Development and Manufacture of Drug Substances | DS-specific guidance |
| ICH Q6B | Specifications: Test Procedures for Biotechnological/Biological Products | Specification setting |
| EU Annex 15 | Qualification and Validation | EU expectations for PV |
| ISPE GAMP 5 | A Risk-Based Approach to Compliant GxP Computerized Systems | Computer system validation |
| Site Validation Master Plan | `[VMP document ID]` | Site-specific validation requirements |
| Process Development Report | `[report ID]` | Process characterization and CPP/CQA linkage |
| Risk Assessment Report | `[report ID]` | CPP/CQA risk ranking |
| Cleaning Validation Protocol/Report | `[document ID]` | Cleaning validation status |
| Aseptic Process Simulation Report | `[document ID]` | Media fill results (DP only) |

---

## 11. Human Review Checklist

Before finalizing the PPQ protocol, verify the following:

| # | Review Item | Verified | Reviewer | Date |
|---|-------------|----------|----------|------|
| 1 | Process description matches registered process (Module 3, Section 3.2.S.2.2) | `[ ] Yes` | `[name]` | `[date]` |
| 2 | All CPPs from risk assessment are included with correct NOR/PAR ranges | `[ ] Yes` | `[name]` | `[date]` |
| 3 | Acceptance criteria match or are tighter than registered specifications | `[ ] Yes` | `[name]` | `[date]` |
| 4 | Sampling plan covers all process steps and IPC points | `[ ] Yes` | `[name]` | `[date]` |
| 5 | Number of PPQ batches is statistically justified | `[ ] Yes` | `[name]` | `[date]` |
| 6 | All analytical methods are validated | `[ ] Yes` | `[name]` | `[date]` |
| 7 | All equipment is qualified (IQ/OQ/PQ) | `[ ] Yes` | `[name]` | `[date]` |
| 8 | Batch records are approved and controlled | `[ ] Yes` | `[name]` | `[date]` |
| 9 | Staff training is documented and complete | `[ ] Yes` | `[name]` | `[date]` |
| 10 | Deviation and escalation procedures are defined | `[ ] Yes` | `[name]` | `[date]` |
| 11 | Protocol amendment procedure is defined | `[ ] Yes` | `[name]` | `[date]` |
| 12 | Prerequisites are verified and documented | `[ ] Yes` | `[name]` | `[date]` |
| 13 | Regulatory authority expectations are addressed (pre-submission meeting commitments) | `[ ] Yes` | `[name]` | `[date]` |
| 14 | Protocol is consistent with site Validation Master Plan | `[ ] Yes` | `[name]` | `[date]` |
| 15 | Protocol has been reviewed by: Process Development, Analytical, QA, Validation, Regulatory (as applicable) | `[ ] Yes` | `[names]` | `[date]` |

---

## 12. Approval Signatures

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Protocol Author | `[Name]` | __________ | `[date]` |
| Process Development Review | `[Name]` | __________ | `[date]` |
| Analytical Review | `[Name]` | __________ | `[date]` |
| Quality Assurance Review | `[Name]` | __________ | `[date]` |
| Validation Lead | `[Name]` | __________ | `[date]` |
| QA Head (Final Approval) | `[Name]` | __________ | `[date]` |

---

*Document generated from cmc-forge Process Validation Protocol Framework. This is a scaffold -- all process-specific details, acceptance criteria, and sampling plans must be defined and approved by qualified SMEs. No data has been fabricated or assumed.*
