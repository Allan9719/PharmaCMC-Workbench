# Change Impact Assessment and Comparability Strategy

**DRAFT FOR CONTROLLED REVIEW**

> This document assesses the impact of a proposed manufacturing change and defines the comparability strategy. It is a decision-support tool. Regulatory classification guidance is directional, not definitive — confirm with RA and the applicable regulatory authority. All data must come from verified source documents; no data has been fabricated.

---

## 1. Change Summary

| Field | Value | Guidance |
|-------|-------|----------|
| Change Control Number | `[CC-YYYY-NNN]` | Link to the formal change control in the QMS |
| Product Name | `[INN / code name]` | Use INN if available |
| Drug Type | `[mAb / bispecific / ADC / fusion protein / small molecule / CGT / other]` | Biologics require ICH Q5E comparability |
| Change Title | `[Concise title, e.g., "Change of Protein A chromatography resin from MabSelect SuRe to MabSelect PrismA"]` | Be specific — vague titles create regulatory confusion |
| Change Description | `[Detailed description of what is changing, from what to what]` | Include "from" and "to" states |
| Change Owner | `[Name, Title]` | Person accountable for the change |
| Date Initiated | `[YYYY-MM-DD]` | Change control initiation date |
| Target Implementation Date | `[YYYY-MM-DD]` | When the change should take effect |
| Regulatory Region(s) Affected | `[US / EU / China / Japan / Global]` | Determines which regulations apply |
| Company Filing Posture | `[China-only / China-first then global / Global-first with China bridge / Inbound China localization / Outbound licensing]` | Determines whether to build global core + regional delta logic |
| Application Stage | `[Development / BLA/NDA pending / Post-approval]` | Development changes have different requirements than post-approval |
| Site(s) Affected | `[Manufacturing site(s) where the change applies]` | Multi-site changes may have different impacts per site |

### Change Classification Guidance

Use the following framework to classify the change severity. This classification drives the comparability and regulatory strategy.

| Classification | Definition | Typical Examples | Comparability Required? | Regulatory Filing |
|---------------|-----------|------------------|------------------------|-------------------|
| **Minor** | No impact on product quality, safety, or efficacy. Process parameters remain within validated ranges. | Same raw material, different lot; minor SOP wording change; equipment replacement with identical model. | Not required (routine monitoring sufficient) | Annual Report (FDA) / Type IA (EU) / Record (NMPA) |
| **Major** | Potential impact on product quality attributes. Process parameters may change within or near validated ranges. Some CQAs could be affected but risk is low. | Different chromatography resin (same ligand, different base matrix); scale change within 2-10x; new QC test method (same principle). | Analytical comparability required (Step 1) | CBE-30 or CBE (FDA) / Type IB or Type II (EU) / Notification or Approval (NMPA) |
| **Critical** | Likely impact on product quality, safety, or efficacy. Process parameters change beyond validated ranges. Multiple CQAs potentially affected. | New manufacturing site; new cell line; significant process change (different unit operation); formulation change; container closure change. | Full comparability (Steps 1-3, as triggered) | PAS (FDA) / Type II (EU) / Approval (NMPA) |

### Preliminary Classification

| Field | Value |
|-------|-------|
| Proposed Classification | `[Minor / Major / Critical]` |
| Classification Rationale | `[2-4 sentences explaining why this classification was chosen]` |
| RA Confirmation | `[Confirmed / Pending / Disputed]` |
| RA Confirmed Classification | `[if different from proposed]` |

---

### Regional Filing Path Assumptions

All entries below are preliminary and require RA confirmation.

| Region | Preliminary Path Assumption | Basis / Trigger | Evidence Needed | RA Confirmation Status |
|--------|-----------------------------|-----------------|-----------------|------------------------|
| China NMPA/CDE | `[supplement / notification / record / IND amendment / meeting needed]` | `[change type, stage, product risk]` | `[supporting research data, comparability, site records]` | `[Pending / Confirmed / Disputed]` |
| US FDA | `[PAS / CBE-30 / CBE / annual report / IND amendment / meeting needed]` | `[change type, stage, product risk]` | `[comparability, validation, stability, method data]` | `[Pending / Confirmed / Disputed]` |
| EU EMA | `[Type IA / Type IB / Type II / MAA update / scientific advice]` | `[change type, stage, product risk]` | `[variation support package]` | `[Pending / Confirmed / Disputed]` |

---

## 2. Current vs. Proposed State Comparison

| Element | Current State (Pre-Change) | Proposed State (Post-Change) | Impact Hypothesis | Impact Rating |
|---------|---------------------------|------------------------------|-------------------|---------------|
| `[e.g., Chromatography resin]` | `[e.g., MabSelect SuRe, 5 cm bed height, 6 cycle lifetime]` | `[e.g., MabSelect PrismA, 5 cm bed height, estimated 30+ cycle lifetime]` | `[e.g., Different base matrix may affect HCP clearance and leachables profile; higher ligand density may improve capacity]` | `[High / Medium / Low / None]` |
| `[e.g., Load challenge]` | `[e.g., 35 g/L at current resin]` | `[e.g., Up to 45 g/L at new resin (higher capacity)]` | `[e.g., Higher load may affect impurity clearance; needs characterization]` | `[rating]` |
| `[e.g., Wash volume]` | `[e.g., 10 CV]` | `[e.g., 10 CV (unchanged)]` | `[e.g., No change expected]` | `[None]` |
| `[e.g., Elution pH]` | `[e.g., pH 3.5]` | `[e.g., pH 3.5 (unchanged)]` | `[e.g., No change expected]` | `[None]` |
| `[e.g., Resin lifetime]` | `[e.g., Validated to 6 cycles]` | `[e.g., Target 30+ cycles; requires lifetime validation]` | `[e.g., Extended lifetime may affect cleaning; need to demonstrate consistent clearance over lifetime]` | `[rating]` |
| `[element]` | `[current]` | `[proposed]` | `[hypothesis]` | `[rating]` |
| `[element]` | `[current]` | `[proposed]` | `[hypothesis]` | `[rating]` |

**Common Pitfall**: Listing "no impact" for elements that are indirectly affected. For example, changing a chromatography resin may not change the elution buffer, but it may change the impurity profile of the eluate, which then affects downstream steps. Always trace the impact through the entire process.

---

## 3. CQA Impact Assessment Matrix

| CQA | Specification Limit | Directly Affected? | Indirectly Affected? | Risk of Change | Impact Rationale | Monitoring Approach |
|-----|---------------------|--------------------|--------------------|-----------------|------------------|---------------------|
| Potency (bioassay) | `[e.g., 80-120% relative potency]` | `[Yes / No]` | `[Yes / No]` | `[High / Medium / Low]` | `[e.g., Unlikely to change — resin change does not affect molecular structure]` | `[e.g., Release testing + stability]` |
| Purity (% monomer by SEC) | `[e.g., >= 95.0%]` | `[Yes / No]` | `[Yes / No]` | `[rating]` | `[rationale]` | `[approach]` |
| Aggregates (% HMW by SEC) | `[e.g., <= 3.0%]` | `[Yes / No]` | `[Yes / No]` | `[rating]` | `[rationale]` | `[approach]` |
| Charge variants (cIEF or CEX) | `[e.g., Acidic <= X%, Main >= Y%, Basic <= Z%]` | `[Yes / No]` | `[Yes / No]` | `[rating]` | `[rationale]` | `[approach]` |
| Glycosylation (major glycans) | `[e.g., G0F: X-Y%, G1F: X-Y%, G2F: X-Y%]` | `[Yes / No]` | `[Yes / No]` | `[rating]` | `[rationale]` | `[approach]` |
| HCP (ng/mg) | `[e.g., <= 100 ng/mg]` | `[Yes / No]` | `[Yes / No]` | `[rating]` | `[e.g., Potential impact — different base matrix may change HCP clearance profile]` | `[approach]` |
| DNA (pg/mg) | `[e.g., <= 10 pg/mg]` | `[Yes / No]` | `[Yes / No]` | `[rating]` | `[rationale]` | `[approach]` |
| Protein A leaching (ng/mg) | `[e.g., <= 5 ng/mg]` | `[Yes / No]` | `[Yes / No]` | `[rating]` | `[e.g., Directly affected — different resin has different leaching profile]` | `[approach]` |
| Endotoxin (EU/mg) | `[e.g., <= 0.5 EU/mg]` | `[Yes / No]` | `[Yes / No]` | `[rating]` | `[rationale]` | `[approach]` |
| Sterility | `[Negative]` | `[Yes / No]` | `[Yes / No]` | `[rating]` | `[rationale]` | `[approach]` |
| Identity (peptide mapping) | `[Matches reference]` | `[Yes / No]` | `[Yes / No]` | `[rating]` | `[rationale]` | `[approach]` |
| Appearance | `[Clear to slightly opalescent, colorless to pale yellow]` | `[Yes / No]` | `[Yes / No]` | `[rating]` | `[rationale]` | `[approach]` |
| pH | `[e.g., 5.5-6.5]` | `[Yes / No]` | `[Yes / No]` | `[rating]` | `[rationale]` | `[approach]` |
| `[additional CQA]` | `[limit]` | `[affected?]` | `[affected?]` | `[rating]` | `[rationale]` | `[approach]` |

### CQA Impact Summary

| Impact Category | CQAs Affected | Action Required |
|----------------|---------------|-----------------|
| **Directly affected (High risk)** | `[list CQAs]` | Must include in comparability protocol with predefined acceptance criteria |
| **Indirectly affected (Medium risk)** | `[list CQAs]` | Include in comparability protocol; may use trending rather than strict limits |
| **Not affected (Low risk)** | `[list CQAs]` | Routine release testing sufficient; no additional comparability testing needed |

---

## 4. Three-Step Comparability Evidence Plan

### Step 1: Analytical / Quality Comparison

**Objective**: Demonstrate that the post-change product is highly similar to the pre-change product using a comprehensive analytical comparison. This is ALWAYS required for major and critical changes. Per ICH Q5E.

| Test | Method | Pre-Change Data (Reference) | Post-Change Data Required | Acceptance Criteria | Number of Batches | Rationale |
|------|--------|----------------------------|--------------------------|---------------------|-------------------|-----------|
| Identity (peptide mapping) | LC-MS peptide mapping | `[Historical range: matches reference]` | `[Min. 3 post-change batches]` | `[Matches reference]` | `[3+]` | Confirms primary structure unchanged |
| Purity / Aggregates (SEC-HPLC) | SEC-UV | `[Historical mean: 97.5%, range 96.0-98.5%]` | `[Min. 3 batches]` | `[Individual values within pre-change historical range; no statistically significant shift (p > 0.05)]` | `[3+]` | Key CQA for safety |
| Charge variants (CEX-HPLC or cIEF) | CEX-UV or cIEF | `[Historical range]` | `[Min. 3 batches]` | `[Acidic, main, basic peaks within pre-change historical range]` | `[3+]` | PTM-related CQA |
| Glycosylation (HILIC or LC-MS) | HILIC-FLR or LC-MS | `[Historical range]` | `[Min. 3 batches]` | `[Major glycan species within pre-change historical range]` | `[3+]` | Critical for biological activity |
| Potency (cell-based bioassay) | Cell-based or binding | `[Historical mean: 100%, range 85-115%]` | `[Min. 3 batches]` | `[Individual values within 80-125% relative to reference]` | `[3+]` | Confirms biological activity preserved |
| HCP | ELISA | `[Historical range]` | `[Min. 3 batches]` | `[Within pre-change historical range; no upward trend]` | `[3+]` | Process performance |
| Protein A leaching | ELISA | `[Historical range]` | `[Min. 3 batches]` | `[Within specification; no upward trend]` | `[3+]` | Directly affected by resin change |
| DSQ (disulfide bond mapping) | Non-reducing peptide mapping | `[Matches expected pattern]` | `[Min. 1 batch]` | `[Matches expected pattern]` | `[1+]` | Higher-order structure confirmation |
| Thermal stability (DSC) | DSC | `[Historical Tm values]` | `[Min. 1 batch]` | `[Tm values within 1C of pre-change mean]` | `[1+]` | Conformational stability |
| Biological activity (binding) | SPR or ELISA | `[Historical range]` | `[Min. 3 batches]` | `[KD or EC50 within pre-change range]` | `[3+]` | Orthogonal potency confirmation |
| Subvisible particles | MFI or HIAC | `[Historical range]` | `[Min. 3 batches]` | `[No statistically significant increase]` | `[3+]` | Particle safety |

**Acceptance Criteria Template**:

For each test, define criteria using one of these approaches:
- **Specification-based**: Post-change results must meet the current registered specification. Minimum standard.
- **Historical range-based**: Post-change results must fall within the pre-change historical manufacturing range (e.g., mean +/- 2SD). Stronger standard, demonstrates similarity not just compliance.
- **Statistical equivalence**: Pre-defined equivalence margin (e.g., +/- 2SD or delta based on clinical relevance). Strongest standard, used for critical CQAs.

| Tier | When to Use | Example |
|------|-----------|---------|
| Specification-based | Low-risk CQAs, specification is wide relative to process variability | Endotoxin: post-change <= limit |
| Historical range | Medium-risk CQAs, demonstrates comparable process performance | HCP: post-change within pre-change 95% reference interval |
| Statistical equivalence | High-risk CQAs directly affected by the change | Potency: equivalence margin +/- 10% (predefined) |

### Step 2: Non-Clinical Comparison

**When Triggered**: When analytical comparability (Step 1) shows differences that could affect safety or when the change affects a CQA with known safety impact (e.g., aggregate increase, new impurity, significant glycan shift).

| Trigger | Assessment Needed | Typical Tests | Acceptance |
|---------|------------------|---------------|------------|
| Aggregate increase >2x pre-change level | Immunogenicity risk assessment | In vitro cytokine release assay; T-cell epitope analysis | No increase in immunogenicity signals |
| New impurity identified | Toxicological assessment | Impurity qualification study (if > ICH Q3A/B threshold) | Impurity qualified at expected level |
| Significant glycan shift (e.g., >5% change in afucosylation) | Fc effector function assessment | ADCC assay, CDC assay, FcRn binding | Functional activity comparable |
| Charge variant shift >5% | Degradation product assessment | Forced degradation to characterize new peak | New peak characterized and qualified |
| Potency shift outside 80-125% | Pharmacological relevance assessment | Dose-response comparison, broader bioassay panel | Dose-response curves comparable |

**Non-Clinical Protocol Template**:

| Field | Value |
|-------|-------|
| Trigger Met? | `[Yes / No / N/A]` |
| Trigger Description | `[which specific trigger was met]` |
| Study Design | `[e.g., Side-by-side testing of pre- and post-change material in [assay name]]` |
| Number of Lots (Pre-Change) | `[n]` |
| Number of Lots (Post-Change) | `[n]` |
| Duration | `[weeks]` |
| Acceptance Criteria | `[criteria]` |
| Status | `[Not required / Planned / In progress / Complete]` |

### Step 3: Clinical Bridge

**When Triggered**: When Steps 1 and 2 do not provide sufficient evidence that the change has no adverse impact on safety or efficacy. This is rare for most manufacturing changes but may be required for:
- Changes to the drug substance that affect PK/PD
- Formulation changes that affect bioavailability
- Cell line changes
- Significant impurity profile changes

| Consideration | Guidance |
|--------------|---------|
| Study type | `[PK bridging study / PD comparison / Full clinical efficacy study]` |
| Study design | `[Crossover / Parallel / Single-dose PK / Multiple-dose PK]` |
| Population | `[Healthy volunteers / Patient population — match approved indication]` |
| Sample size | `[Based on PK equivalence margin, typically 80-125% for AUC and Cmax]` |
| Endpoints | `[AUC0-inf, AUC0-t, Cmax, Tmax, half-life, clearance, volume of distribution]` |
| Equivalence margins | `[Typically 80.00-125.00% for AUC and Cmax (standard bioequivalence)]` |
| Reference product | `[Pre-change product batch(es)]` |
| Test product | `[Post-change product batch(es)]` |
| Status | `[Not required / Under discussion with RA / Protocol development / Planned / Complete]` |

---

## 5. Regulatory Path Classification

### FDA Pathway Decision Guidance

| Change Classification | Reporting Category | Typical Examples | Estimated Review Time | Data Package |
|----------------------|-------------------|------------------|----------------------|-------------|
| **Minor** | Annual Report (21 CFR 314.70(d)) | Raw material vendor change (same grade), equipment replacement (equivalent), specification tightening | No review (filed annually) | Updated batch record, CoAs |
| **Moderate** | Changes Being Effected in 30 days (CBE-30, 21 CFR 314.70(c)) | New analytical method (different principle), process parameter range widening, in-process limit change | 30 days (auto-effective if no FDA action) | Comparability data, updated specifications, batch data |
| **Moderate** | Changes Being Effected (CBE, 21 CFR 314.70(c)) | Equipment change (different but equivalent function), scale change within validated range | 0 days (effective on submission) | Comparability data, equipment qualification |
| **Major** | Prior Approval Supplement (PAS, 21 CFR 314.70(b)) | New manufacturing site, new drug substance process, formulation change, container closure change, cell line change | ~4-6 months (standard review) | Full comparability package, validation data, stability data |

### EMA Pathway (for reference)

| Change Type | Classification | Filing | Timeline |
|------------|---------------|--------|----------|
| Minor | Type IA (notification) | Post-implementation | Immediate or 12-month batch |
| Moderate | Type IB (notification) | Pre-implementation | 30 days |
| Major | Type II (approval) | Pre-implementation | ~90 days |
| Any change to terms of MA | Article 61(3) notification | Pre-implementation | As applicable |

### NMPA (China) Pathway (for reference)

| Change Type | Classification | Filing | Timeline |
|------------|---------------|--------|----------|
| Minor | Record (备案) | Post-implementation at provincial level | As specified |
| Moderate | Notification (报告) | Pre-implementation at NMPA | ~60 days |
| Major | Approval (审批) | Pre-implementation at NMPA | ~90-120 days |

### Confirmed Regulatory Path

| Region | Filing Category | Target Submission Date | Review Timeline Expected | Regulatory Contact |
|--------|----------------|----------------------|-------------------------|-------------------|
| `[US]` | `[PAS / CBE-30 / CBE / AR]` | `[date]` | `[duration]` | `[name]` |
| `[EU]` | `[Type IA / IB / II]` | `[date]` | `[duration]` | `[name]` |
| `[China]` | `[Record / Notification / Approval]` | `[date]` | `[duration]` | `[name]` |

---

## 6. PACMP Discussion Framework

If the change is being considered under a Post-Approval Change Management Protocol (ICH Q12) or Established Conditions (EC) framework, address the following:

| PACMP Element | Assessment |
|--------------|------------|
| Is there an existing PACMP for this type of change? | `[Yes / No / Under development]` |
| If yes, does this change fall within the PACMP scope? | `[Yes / No]` |
| What are the predefined acceptance criteria in the PACMP? | `[criteria]` |
| Does the change data meet PACMP criteria? | `[Yes / No / Not yet assessed]` |
| If no PACMP exists, should one be developed? | `[Yes / No — rationale]` |
| Would an EC framework reduce future reporting burden for similar changes? | `[Assessment]` |
| Regulatory authority engagement planned? | `[Pre-submission meeting / Written inquiry / None]` |

---

## 7. Post-Implementation Monitoring Plan

| Monitoring Element | Description | Duration | Frequency | Acceptance Trigger | Owner |
|-------------------|-------------|----------|-----------|-------------------|-------|
| Enhanced stability monitoring | Place first 3 post-change batches on stability alongside pre-change batches | `[12-24 months]` | `[per stability protocol]` | `[No adverse trends relative to pre-change batches]` | `[Stability Lead]` |
| Process performance trending | Monitor key process parameters and yields for post-change batches | `[First 10 batches or 12 months, whichever is longer]` | `[per batch]` | `[No adverse trends; parameters within NOR]` | `[Process Lead]` |
| Impurity trending | Track HCP, DNA, Protein A, and other impurities | `[First 10 batches]` | `[per batch]` | `[No upward trend; all within specification]` | `[Analytical Lead]` |
| CPP monitoring | Verify CPPs remain within NOR/PAR post-change | `[First 10 batches]` | `[per batch]` | `[All CPPs within NOR]` | `[Process Lead]` |
| Customer complaint monitoring | Monitor for any new complaint types post-change | `[12 months]` | `[monthly review]` | `[No new complaint types related to change]` | `[QA]` |
| Annual Product Quality Review (APQR) | Include post-change data in next APQR with comparison to pre-change | `[Annual]` | `[Annual]` | `[APQR includes comparability summary]` | `[QA]` |

---

## 8. Open Questions Register

| Question ID | Question | Impact on Strategy | Owner | Target Resolution Date | Status | Resolution |
|-------------|----------|-------------------|-------|----------------------|--------|-----------|
| OQ-001 | `[e.g., Does the new resin require a change in registered cleaning validation?]` | `[e.g., If yes, cleaning revalidation adds 4-6 weeks to timeline]` | `[owner]` | `[date]` | `[Open / Resolved]` | `[resolution or N/A]` |
| OQ-002 | `[e.g., Can we use retrospective data from SU engineering runs as pre-change reference, or do we need dedicated pre-change batches?]` | `[e.g., Affects number of pre-change batches in comparability]` | `[owner]` | `[date]` | `[status]` | `[resolution]` |
| OQ-003 | `[e.g., What is the minimum number of post-change batches required by [regulatory authority]?]` | `[e.g., Affects scale of comparability study]` | `[owner]` | `[date]` | `[status]` | `[resolution]` |
| OQ-004 | `[e.g., Is the post-change resin considered the same "type" for regulatory purposes, or does it constitute a new raw material?]` | `[e.g., Classification affects regulatory pathway]` | `[owner]` | `[date]` | `[status]` | `[resolution]` |
| OQ-005 | `[question]` | `[impact]` | `[owner]` | `[date]` | `[status]` | `[resolution]` |

---

## 9. Human Review Required

| Reviewer | Role | Review Scope | Decision Authority | Sign-Off Required |
|----------|------|-------------|-------------------|-------------------|
| **CMC Lead** | Technical leadership | Change classification, CQA impact, comparability strategy | Confirms technical strategy | Yes |
| **QA Head or Designee** | Quality oversight | GMP compliance, change control procedure, specification impact | Approves change control | Yes |
| **Regulatory Affairs CMC** | Regulatory strategy | Regulatory classification, filing pathway, data package adequacy | Confirms regulatory pathway | Yes |
| **Analytical Lead** | Analytical science | Method suitability for comparability, acceptance criteria feasibility | Confirms analytical strategy | Yes |
| **Process Development Lead** | Process knowledge | Impact hypothesis accuracy, process parameter assessment | Confirms process assessment | Yes |
| **Toxicology / Nonclinical** (if Step 2 triggered) | Safety assessment | Non-clinical study design and interpretation | Confirms safety assessment | Yes (if triggered) |
| **Clinical / Medical** (if Step 3 triggered) | Clinical strategy | Clinical bridge study design and interpretation | Confirms clinical assessment | Yes (if triggered) |
| **Qualified Person / QP** (EU, if applicable) | Batch release authority | Confirms change does not compromise product release | Release authority | Yes (for EU) |

**Review Process**:
1. Draft assessment distributed to all reviewers.
2. Reviewers provide comments within 5 business days.
3. Change owner resolves comments and updates assessment.
4. Final version circulated for sign-off.
5. Change control approved per QMS procedure.
6. Implementation proceeds per approved plan.

---

*Document generated from cmc-forge Change & Comparability Template. All content requires human verification. Regulatory classification is advisory and must be confirmed by Regulatory Affairs. Comparability conclusions require sign-off by designated reviewers.*
