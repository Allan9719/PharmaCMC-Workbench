# CMC Document Quality Checklist

> Run this checklist before any DRAFT mode output. Every check must pass or be explicitly waived with a documented reason.

## How to Use This Checklist

- Apply **all** checks to full regulatory submissions (BLA/NDA Module 3, comparability protocols, PPQ protocols).
- Apply **relevant** checks to internal documents (risk assessments, stage-gate packs, training materials) — use judgment on which categories apply.
- A check that fails does not block output — it flags the item for human review. Document the reason for any waiver.
- When a check identifies an issue, mark it in the draft with `[QC: description]` so the reviewer can locate it.

---

## 1. Content Completeness

### 1.1 Required sections present per document type

| Aspect | What to Verify |
|--------|---------------|
| **Check** | All sections required by the document type template are present, or missing sections are explicitly noted as "To be completed" with an owner and deadline. |
| **Why it matters** | Missing sections delay review cycles and signal incomplete thinking, even in drafts. |
| **Common failure** | Sections like "Deviations" or "Change History" are silently omitted because no data exists yet, rather than being present with "None to date." |

### 1.2 Acceptance criteria defined where required

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Every test, study, or validation activity has a pre-defined acceptance criterion. Tentative criteria are labeled as such. |
| **Why it matters** | Acceptance criteria separate objective pass/fail decisions from subjective judgment. Without them, the document cannot be executed. |
| **Common failure** | Protocols list test parameters but leave criteria as "to be determined" or use vague language like "acceptable results." |

### 1.3 Statistical methods and rationale included

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Where data analysis is required, the statistical method (e.g., tolerance interval, %RSD, Cpk) is named, the formula or reference is provided, and the choice is justified for the data type and sample size. |
| **Why it matters** | Regulators challenge statistical methods that appear arbitrary or mismatched to the data structure. |
| **Common failure** | Cpk is calculated without verifying normality, or tolerance intervals are used with sample sizes too small for the chosen confidence level. |

### 1.4 ICH/regulatory references accurate and current

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Every ICH, FDA, or NMPA/CDE guidance cited by number matches the correct version. Outdated guidance is flagged. |
| **Why it matters** | Citing ICH Q1A instead of Q1A(R2), or referencing a withdrawn FDA guidance, undermines credibility. |
| **Common failure** | Copy-paste from earlier documents preserves outdated guidance numbers, especially for ICH Q1A, Q5E, and the FDA Process Validation Guidance (2011 revision). |

### 1.5 Batch/sample sizes justified

| Aspect | What to Verify |
|--------|---------------|
| **Check** | The number of batches, units, or samples is stated and justified (e.g., "3 consecutive PPQ batches per FDA guidance," "n=30 per ICH acceptance criteria"). |
| **Why it matters** | Sample size without justification invites regulator questions about statistical power and representativeness. |
| **Common failure** | PPQ protocols state "3 batches" without linking to the validation lifecycle concept or explaining why 3 is sufficient for the process variability observed. |

### 1.6 Specifications traceable to CQA rationale

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Every specification limit can be traced back to a CQA identification step with a documented rationale (clinical, process, safety, or regulatory source). |
| **Why it matters** | Specifications that appear without rationale look arbitrary and are difficult to defend in submissions or inspections. |
| **Common failure** | Release specifications are copied from a reference product or earlier project without adapting the rationale to the current molecule and indication. |

### 1.7 Control strategy elements linked to process steps

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Each control strategy element (in-process test, CPP monitoring, material attribute, procedural control) is linked to a specific unit operation or process step. |
| **Why it matters** | A control strategy that is a disconnected list of tests does not demonstrate understanding of the process. |
| **Common failure** | Control strategy tables list tests without mapping them to the process flow diagram steps, or CPPs are listed without linking to the CQA they control. |

### 1.8 Stability protocol covers ICH conditions

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Stability protocols include all required ICH conditions (long-term, accelerated, and where applicable, intermediate, photostability, in-use) with correct temperatures, humidities, and timepoints. |
| **Why it matters** | Incomplete stability design delays filing and may require repeat studies. |
| **Common failure** | Photostability is omitted for proteins that are photosensitive, or in-use stability is missing for multi-dose presentations. |

### 1.9 Regulatory submission context provided

| Aspect | What to Verify |
|--------|---------------|
| **Check** | The document states which regulatory submission it supports (IND, BLA, variation/supplement, annual report) and the target agency. |
| **Why it matters** | Content depth and formatting requirements differ by submission type and agency. |
| **Common failure** | A document drafted for IND-level content is later used for BLA filing without upgrading evidence depth. |

### 1.10 China/global regional delta identified

| Aspect | What to Verify |
|--------|---------------|
| **Check** | For China, US, EU, or multi-region work, the output states the primary target agency and separates the global core CMC story from regional deltas. |
| **Why it matters** | Chinese companies often reuse one evidence package across CDE, FDA, EMA, partners, and CDMOs. Silent regional differences create rework and regulatory risk. |
| **Common failure** | A CDE-oriented Chinese draft is translated into English but never upgraded for FDA/EMA expectations, or an FDA-style package omits China-specific registration and site considerations. |

### 1.11 Bilingual terminology controlled when needed

| Aspect | What to Verify |
|--------|---------------|
| **Check** | If the output is bilingual or partner-facing, key CMC terms are defined as Chinese term + English regulatory term + abbreviation, and the same term is used consistently. |
| **Why it matters** | Terminology drift between Chinese internal documents and English partner/regulatory packages can obscure CQA, CPP, specification, and comparability commitments. |
| **Common failure** | "工艺验证", "工艺确认", "process validation", and "PPQ" are mixed without clarifying whether the text means lifecycle validation, Stage 2 PPQ, or legacy validation. |

---

## 2. Terminology and Consistency ("Banana Rule")

> The "Banana Rule": once you call it a banana, call it a banana everywhere. Switching between "banana," "fruit," and "yellow crescent" in the same document destroys clarity.

### 2.1 CQA terms used consistently

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Each CQA is identified by one canonical name and that name is used in every occurrence — across the CQA table, control strategy, specifications, and protocol sections. |
| **Why it matters** | Regulators and reviewers cross-reference sections. "Purity" in one section and "main peak by SE-HPLC" in another for the same attribute create confusion about whether they refer to the same thing. |
| **Common failure** | Early sections use the scientific term ("charge variant distribution") while later sections abbreviate to "CVA" or switch to "acidic variants" without establishing the relationship. |

### 2.2 CPP names identical across all documents

| Aspect | What to Verify |
|--------|---------------|
| **Check** | CPP names match exactly across the process description, batch records, control strategy, and validation protocols. Parameters, units, and ranges are identical. |
| **Why it matters** | A CPP called "pH of buffer A" in one place and "equilibration buffer pH" in another may or may not be the same parameter. Ambiguity in CPP identity undermines the entire control strategy. |
| **Common failure** | Different authors working on different sections independently name parameters, resulting in the same CPP appearing under different names. |

### 2.3 Batch numbering consistent

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Every batch identifier (number, code) used in data tables, summary text, figure labels, and appendices is identical and traceable. |
| **Why it matters** | A batch called "PPQ-001" in the body and "Batch 2024-001" in the appendix may be the same batch — or may not. The reviewer cannot tell. |
| **Common failure** | Manufacturing batch numbers differ from analytical batch codes, and the mapping between them is never documented. |

### 2.4 Analytical method names match validation reports

| Aspect | What to Verify |
|--------|---------------|
| **Check** | The analytical method names and version numbers in specifications, validation protocols, and control strategy exactly match those in the method validation reports. |
| **Why it matters** | Method identity must be unambiguous to ensure the validated method is the one used for release and stability. |
| **Common failure** | A method is called "SE-HPLC for purity" in the specification but "Size-exclusion chromatography Method A v2.1" in the validation report, with no cross-reference table. |

### 2.5 Site and facility names consistent

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Manufacturing site, testing site, and any contract facility names are used consistently — using either the registered name or the site code, but not mixing both. |
| **Why it matters** | Different names for the same site raise questions about whether activities were performed at one site or two. |
| **Common failure** | The manufacturing narrative uses "Site A" while the batch records reference the facility registration number, and stability sections use the city name. |

### 2.6 Abbreviations defined at first use

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Every abbreviation is spelled out at its first occurrence in the document. A consolidated abbreviation table is present if the document exceeds 5 pages. |
| **Why it matters** | Readers from different disciplines (regulatory, manufacturing, analytical) may not share all abbreviations. |
| **Common failure** | Abbreviations are defined in a table at the end but used without definition in the body, or the table is missing entirely for longer documents. |

### 2.7 No synonym drift for defined terms

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Once a term is defined with a specific meaning (e.g., "drug substance" vs. "drug product" vs. "in-process material"), that definition is maintained throughout. |
| **Why it matters** | "Drug substance" and "active pharmaceutical ingredient" may be interchangeable in some contexts but not in Module 3 where each has a specific section. |
| **Common failure** | A document switches between "drug substance" and "API" mid-text, or uses "formulation" when referring specifically to the "drug product manufacturing process." |

### 2.8 Dosage form and presentation terms consistent

| Aspect | What to Verify |
|--------|---------------|
| **Check** | The dosage form description (e.g., "solution for injection," "lyophilized powder for reconstitution") is used identically in the product description, labeling, and specification sections. |
| **Why it matters** | Regulatory submissions require precise dosage form terminology per the relevant pharmacopoeia or NDA/BLA conventions. |
| **Common failure** | The product is described as a "liquid formulation" in process sections but "solution for injection" in the specification header. |

---

## 3. Numerical Integrity

### 3.1 Percentages sum correctly

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Any set of values expressed as percentages that should total 100% (or a defined total) does so, within rounding tolerance. Composition tables, charge variant distributions, and impurity profiles are checked. |
| **Why it matters** | Percentage tables that sum to 98.5% or 101.3% suggest either a calculation error or a missing/extra component. |
| **Common failure** | Charge variant tables where acidic variants + main peak + basic variants do not sum to 100% due to independent rounding of each value. |

### 3.2 Batch sizes consistent across sections

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Batch size (in mass, volume, or unit count) is identical wherever it appears: process description, batch records, yield calculations, material balance tables. |
| **Why it matters** | A batch size of 10 L in the process description and 10,000 mL in the batch record is the same — but 100 L in the yield section is a different batch. |
| **Common failure** | Target batch size is stated correctly but the actual batch sizes in the data tables reference different scales without explanation (e.g., clinical scale vs. commercial scale batches mixed in the same summary). |

### 3.3 Specification ranges do not contradict data tables

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Proposed specification ranges are consistent with the data presented. No data point in the summary tables falls outside the proposed range without explanation (e.g., an outlier with documented investigation). |
| **Why it matters** | Data outside the proposed specification without explanation suggests either the specification is wrong or the data is wrong — either way, a reviewer will ask. |
| **Common failure** | Historical batch data is presented to justify specifications, but 1-2 batches exceed the proposed range, and no justification or discussion is provided. |

### 3.4 Statistical calculations verified

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Recalculate mean, standard deviation, %RSD, and Cpk from the raw data tables. Verify that reported values match. Confirm the correct formula was used (e.g., sample SD vs. population SD). |
| **Why it matters** | A single incorrect Cpk can change a process from "capable" to "not capable," altering the entire validation conclusion. |
| **Common failure** | %RSD is calculated as (SD/mean)*100 but the mean used in the calculation is from a different data set than the SD, or n is wrong because a deleted data point was not documented. |

### 3.5 Units consistent throughout

| Aspect | What to Verify |
|--------|---------------|
| **Check** | No section mixes unit systems for the same measurement. Convert and compare: if concentration is in mg/mL in one table and ug/mL in another, confirm the values are consistent. |
| **Why it matters** | A specification stated as "0.5 mg/mL" in one section and "500 ug/mL" in another is the same — but "0.5 ug/mL" is a 1000x error. |
| **Common failure** | Protein concentration is in mg/mL in process sections but ug/mL in analytical sections because method sensitivity discussions use the smaller unit, and the value is transcribed without conversion. |

### 3.6 Significant figures appropriate

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Reported values use appropriate significant figures. Analytical results should not have more decimal places than the method precision supports. Specification limits should not imply false precision. |
| **Why it matters** | Reporting a purity as "99.234%" when the method precision is +/- 0.5% is misleading. Reporting a specification as "95.000-105.000%" implies the method can distinguish at the third decimal. |
| **Common failure** | Copy-pasting spreadsheet output into documents preserves full calculator precision (e.g., "mean = 98.723456%") rather than rounding to the appropriate precision. |

### 3.7 Stability timepoints align with protocol

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Every stability timepoint reported in data tables matches a timepoint defined in the stability protocol. No extra or missing timepoints without explanation. |
| **Why it matters** | Reporting data at an unapproved timepoint, or omitting data from a required timepoint, raises data integrity questions. |
| **Common failure** | A 6-month timepoint is reported as "6M" but was actually tested at day 178 (not exactly 6 months), and no explanation is given for the deviation from the protocol-specified window. |

### 3.8 Yield and material balance calculations correct

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Step yields multiply correctly to produce the overall yield. Material balance inputs and outputs reconcile. |
| **Why it matters** | A step yield of 95% followed by 90% followed by 85% should produce an overall yield of approximately 72.7%, not the 80% stated. |
| **Common failure** | Overall yield is calculated independently rather than as the product of step yields, leading to inconsistency. |

---

## 4. Regulatory Compliance

### 4.1 ICH guidance numbers and versions accurate

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Every ICH guidance referenced in the document is cited with the correct code, revision, and step number. Verify that the guidance was actually adopted by the target regulatory agency. |
| **Why it matters** | ICH Q1A(R2) and ICH Q1A are different documents. ICH Q12 is at Step 5 but agency implementation varies. |
| **Common failure** | Documents cite ICH Q8, Q9, Q10 as if they are binding requirements rather than guidelines, or reference ICH guidances that the target agency has not formally adopted. |

### 4.2 Regulatory commitments match submission text

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Any commitment made in the document (e.g., "additional stability data will be submitted in the annual report," "method validation will be completed prior to BLA submission") is consistent with the regulatory strategy and does not contradict commitments made elsewhere. |
| **Why it matters** | Regulatory commitments are binding. Contradicting them between documents creates compliance gaps. |
| **Common failure** | A comparability protocol commits to reporting under a CBE-30 category, but the regulatory strategy document classifies the same change as a PAS. |

### 4.3 Post-approval change reporting category correct

| Aspect | What to Verify |
|--------|---------------|
| **Check** | The proposed reporting category (PAS, CBE-30, CBE-0, Annual Report, or NMPA classification) is correct for the type and impact of the change, and is justified with reference to the relevant guidance or regulation. |
| **Why it matters** | Under-reporting a change (e.g., filing as CBE when it should be PAS) can result in regulatory action. Over-reporting wastes resources and time. |
| **Common failure** | Change reporting category is selected based on precedent from a different product or different agency without verifying that the same classification applies to the current situation. |

### 4.4 Established Conditions properly identified

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Where ICH Q12 Established Conditions (EC) are claimed, each EC is explicitly identified, justified, and distinguished from non-EC process parameters. The regulatory impact of changing each EC is described. |
| **Why it matters** | Improperly designating a parameter as an EC may restrict post-approval flexibility, while failing to designate a true EC may lead to inadequate change control. |
| **Common failure** | EC lists are copied from precedent without evaluating whether the current process knowledge supports the same EC designations. |

### 4.5 Draft labeling present where required

| Aspect | What to Verify |
|--------|---------------|
| **Check** | If the document affects product labeling (storage conditions, specifications that translate to labeling claims, administration instructions), draft labeling language is included or referenced. |
| **Why it matters** | Labeling changes have their own regulatory pathway and must be consistent with the CMC data. |
| **Common failure** | A stability study supports a revised storage condition (e.g., from -20C to -70C), but the labeling section is not updated to reflect this. |

### 4.6 Pharmacopoeial compliance stated where applicable

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Where methods or specifications reference a pharmacopoeia (USP, EP, JP, ChP), the specific monograph or general chapter is cited by number and current version. |
| **Why it matters** | Pharmacopoeial methods may be harmonized or may differ between regions. Citing the wrong pharmacopoeia creates a compliance gap. |
| **Common failure** | Documents reference "USP <788>" for particulate matter when the current applicable chapter is USP <787> for protein therapeutics, or fail to specify which pharmacopoeia applies for multi-region filings. |

---

## 5. Risk and Evidence

### 5.1 Facts vs. assumptions clearly separated

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Every claim in the document is traceable to either a fact (cited data, reference document, validated result) or an assumption (labeled as such with rationale). No fact-like statements rest on unstated assumptions. |
| **Why it matters** | Regulatory reviewers and internal decision-makers need to know the evidence basis for each conclusion. An unstated assumption treated as fact is a hidden risk. |
| **Common failure** | A specification range is justified by "clinical experience" without citing the specific clinical data, batch history, or literature that supports the range. |

### 5.2 Missing evidence flagged, not hidden

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Where evidence is incomplete, pending, or not yet generated, this is explicitly stated in the document with a plan and timeline for completion. No gaps are filled with placeholder text that could be mistaken for final content. |
| **Why it matters** | Missing evidence is a normal part of development. Hiding it is not. Reviewers who discover undisclosed gaps lose trust in the entire document. |
| **Common failure** | A section states "data supports the proposed range" when the data is from a different product, scale, or condition, without disclosing the surrogate nature of the evidence. |

### 5.3 Risk mitigations linked to identified risks

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Every risk mitigation action in the document is traceable to a specific identified risk. No mitigations exist without a corresponding risk, and no identified risk lacks a mitigation (or an explicit acceptance rationale). |
| **Why it matters** | Orphaned mitigations (no risk) waste resources. Orphaned risks (no mitigation) are uncontrolled hazards. |
| **Common failure** | A FMEA or risk assessment table includes mitigations like "ongoing process verification" for every risk without explaining how OPV specifically addresses each risk. |

### 5.4 Comparability acceptance criteria justified

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Where comparability is assessed, acceptance criteria are justified by reference to clinical experience, process capability data, lot history, and/or relevant guidance (ICH Q5E). Criteria are not arbitrary. |
| **Why it matters** | Unjustified acceptance criteria are the most common deficiency in comparability protocols. If the criteria cannot be traced to a rationale, the comparability conclusion cannot be defended. |
| **Common failure** | Acceptance criteria are set as "within historical range" without defining what the historical range is, which batches it includes, or whether it accounts for expected process variability. |

### 5.5 No unsupported claims or conclusions

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Every conclusion statement is supported by data or logical argument presented in the document. No conclusion leaps beyond the evidence. |
| **Why it matters** | "The process is validated" is a conclusion that requires specific evidence. Stating it without the supporting evidence is a compliance risk. |
| **Common failure** | Executive summaries or conclusion sections make definitive claims ("no impact on product quality") that are not fully supported by the data presented in the body. |

### 5.6 Uncertainty quantified where relevant

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Where data is limited, variable, or from small sample sizes, the uncertainty is acknowledged and its impact on conclusions is discussed. |
| **Why it matters** | Drawing firm conclusions from 2 batches of data is fundamentally different from drawing them from 20 batches. The document must reflect this. |
| **Common failure** | Conclusions from development-scale batches (n=1-3) are stated with the same confidence as conclusions from commercial-scale batches (n=10+). |

---

## 6. Document Hygiene

### 6.1 "Draft for controlled review" label present

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Every document produced by this skill carries the label "Draft for controlled review" on the first page or header. |
| **Why it matters** | This label prevents any draft from being mistaken for an approved, released document. It is a core boundary of this skill. |
| **Common failure** | The label is present on the cover page but lost when sections are copy-pasted into other documents or emails. |

### 6.2 Version control header with date and author

| Aspect | What to Verify |
|--------|---------------|
| **Check** | The document header includes: document title, version number, date, and author (role, not just name). If there are prior versions, a revision history table is present. |
| **Why it matters** | Without version control, reviewers cannot confirm they are reviewing the latest draft, and edits to superseded versions are lost. |
| **Common failure** | Documents have a version number but no date, making it impossible to distinguish between "v2.0" created in January and "v2.0" created in March. |

### 6.3 Reviewer roles identified

| Aspect | What to Verify |
|--------|---------------|
| **Check** | The document lists the required reviewer roles (not just names) — e.g., "QA Review," "Technical Review (Process Science)," "Regulatory Review," "QP Review" as applicable. |
| **Why it matters** | Different reviewers evaluate different aspects. A QA reviewer checks compliance; a technical reviewer checks accuracy. Both are needed. |
| **Common failure** | Reviewer names are listed without roles, or the review signature block is missing entirely. |

### 6.4 Cross-references valid

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Every cross-reference to a section number, table, figure, or appendix resolves to the correct target. If the document was restructured, all references are updated. |
| **Why it matters** | A reference to "Section 4.2" that should be "Section 5.2" after restructuring forces the reviewer to hunt for information and undermines confidence. |
| **Common failure** | Section numbering changes during drafting but cross-references are updated manually and some are missed, especially in large documents. |

### 6.5 Table and figure numbering sequential

| Aspect | What to Verify |
|--------|---------------|
| **Check** | Tables and figures are numbered sequentially without gaps or duplicates. Each is referenced in the text at least once. |
| **Why it matters** | An unreferenced table may contain critical data that no reviewer notices. A duplicated number creates ambiguity. |
| **Common failure** | A table is deleted during drafting but the numbering is not re-sequenced, leaving a gap (Table 3, Table 4, Table 6...). |

---

## Checklist Summary

| Category | Count | Check IDs |
|----------|-------|-----------|
| Content Completeness | 9 | 1.1 - 1.9 |
| Terminology and Consistency | 8 | 2.1 - 2.8 |
| Numerical Integrity | 8 | 3.1 - 3.8 |
| Regulatory Compliance | 6 | 4.1 - 4.6 |
| Risk and Evidence | 6 | 5.1 - 5.6 |
| Document Hygiene | 5 | 6.1 - 6.5 |
| **Total** | **42** | |

## Quick-Reference: What to Check First

When time is limited, run these checks in order of impact:

1. **Draft label present** (6.1) — prevents misuse
2. **No unsupported conclusions** (5.5) — highest regulatory risk
3. **Facts vs. assumptions separated** (5.1) — highest integrity risk
4. **Specification ranges vs. data** (3.3) — most commonly challenged
5. **Acceptance criteria defined** (1.2) — blocks execution if missing
6. **CQA terms consistent** (2.1) — most visible to reviewers
7. **Statistical calculations verified** (3.4) — most likely to contain errors
8. **Cross-references valid** (6.4) — most tedious but most disruptive when wrong
