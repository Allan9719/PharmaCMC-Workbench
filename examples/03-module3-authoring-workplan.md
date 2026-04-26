# Example 03: Module 3 Authoring Workplan

> **Integrated scenario:** A Chinese biotech company preparing BLA Module 3 for a bispecific antibody (BsAb).
> **Modules invoked:** CMC Research + CMC Forge (PLAN + DRAFT) + Scientific Writer (REVIEW)
> **Workflow:** [02-module3-authoring.md](../workflows/02-module3-authoring.md)

---

## Scenario Background

**Company:** NovaBio Therapeutics (fictional)
**Product:** NB-101, bispecific antibody (anti-PD-L1 × TGF-β trap)
**Indication:** Hepatocellular carcinoma (HCC), second-line
**Current status:**
- Phase III completed in China (n=320)
- Manufacturing at internal 500L single-use facility
- Analytical methods validated
- 24-month stability data available
- BLA filing target: Q3 2027

**Strategic goal:** Prepare complete Module 3 for NMPA BLA submission.

---

## Step 1: Module 3 Workplan (CMC Forge PLAN)

Using `skills/cmc-forge/templates/module3-workplan-template.md`:

### Section Map and Status

| CTD Section | Content Required | Source Available | Status |
|-------------|-----------------|-----------------|--------|
| 3.2.S.1 General Information | Nomenclature, structure, properties | Complete | Ready to draft |
| 3.2.S.2 Manufacture | Manufacturer info, process description, controls | Partial — process description needs update for Phase III process | Gap: update needed |
| 3.2.S.2.5 Process Validation | Validation reports, PPQ data | Complete (3+ consecutive batches) | Ready to draft |
| 3.2.S.3 Characterisation | Primary/secondary/higher-order structure, purity, impurities | Complete | Ready to draft |
| 3.2.S.4 Control of Drug Substance | Specifications, analytical procedures, validation, batch analyses | Specifications finalized; batch analysis complete | Ready to draft |
| 3.2.S.5 Reference Standards | Reference standard establishment and characterization | Complete | Ready to draft |
| 3.2.S.6 Container Closure | Container closure system description, compatibility | Complete (single-use bags + vials) | Ready to draft |
| 3.2.S.7 Stability | Stability protocol, data summary, shelf life justification | 24-month data available | Ready to draft |
| 3.2.P.1 Description and Composition | Drug product composition | Complete | Ready to draft |
| 3.2.P.2 Pharmaceutical Development | Formulation development, manufacturing process development, container closure | Partial — development history needs compilation | Gap: compile development data |
| 3.2.P.3 Manufacture | Batch formula, process description, process controls, validation | Complete | Ready to draft |
| 3.2.P.4 Control of Excipients | Excipient specifications, compendial status | Complete | Ready to draft |
| 3.2.P.5 Control of Drug Product | Specifications, analytical procedures, validation, batch analyses | Complete | Ready to draft |
| 3.2.P.6 Reference Standards | Drug product reference standard | Complete | Ready to draft |
| 3.2.P.7 Container Closure | Primary packaging description, compatibility | Complete | Ready to draft |
| 3.2.P.8 Stability | Stability protocol, data, shelf life, storage conditions | Complete (24 months + in-use) | Ready to draft |
| 3.2.A.1 Facilities and Equipment | Facility description, equipment qualification | Available | Ready to draft |
| 3.2.A.2 Adventitious Agents Safety Evaluation | Viral safety evaluation, TSE risk | Partial — viral clearance validation complete; needs compilation | Ready to draft |
| 3.2.A.3 Novel Excipients | None (no novel excipients) | N/A | Not applicable |
| 3.2.R Regional Information | China-specific requirements | Partial | Gap: compile regional info |

### Source Document Inventory

| # | Source Document | Version | CTD Sections Supported |
|---|----------------|---------|----------------------|
| 1 | Drug Substance Process Description | v3.2 | 3.2.S.2 |
| 2 | Process Validation Report (PPQ) | v1.0 | 3.2.S.2.5 |
| 3 | Characterization Report (primary/secondary/HS) | v2.1 | 3.2.S.3 |
| 4 | DS Specifications | v4.0 | 3.2.S.4.1 |
| 5 | Analytical Method Validation Package (12 methods) | v1.0 | 3.2.S.4.2–4.3 |
| 6 | Batch Analysis Summary (10 batches) | v1.1 | 3.2.S.4.4 |
| 7 | Reference Standard Report | v1.0 | 3.2.S.5 |
| 8 | Container Closure Qualification | v1.0 | 3.2.S.6 |
| 9 | Stability Study Report (24 months) | v1.0 | 3.2.S.7 |
| 10 | Formulation Development Report | v2.0 | 3.2.P.2.1 |
| 11 | Manufacturing Process Development Report | v1.0 | 3.2.P.2.2 |
| 12 | DP Process Description | v2.1 | 3.2.P.3 |
| 13 | DP Specifications | v3.0 | 3.2.P.5.1 |
| 14 | DP Batch Analysis (8 batches) | v1.0 | 3.2.P.5.4 |
| 15 | DP Stability Report (24 months) | v1.0 | 3.2.P.8 |
| 16 | Facility Description | v1.0 | 3.2.A.1 |
| 17 | Viral Clearance Validation Report | v1.0 | 3.2.A.2 |
| 18 | Quality Agreement (MAH vs. internal) | v1.2 | 3.2.R |

### Timeline

```
Month 1-2:  Compile source documents → Draft 3.2.S sections
Month 2-3:  Draft 3.2.P sections
Month 3:    Draft 3.2.A + 3.2.R sections
Month 3-4:  Cross-section consistency check (15-point)
Month 4:    Writing quality review (English summary sections)
Month 4-5:  Internal review (CMC Lead + RA + QA)
Month 5:    Final compilation and eCTD formatting
```

---

## Step 2: Knowledge Grounding (CMC Research)

| Section Being Drafted | CMC Research Reference |
|-----------------------|----------------------|
| 3.2.S (Biologic DS) | `biologic_drug/biologic_basic.md` |
| 3.2.S.3 (Characterization) | `basic_theory/ich_framework.md` (ICH Q6B) |
| 3.2.S.7 (Stability) | `basic_theory/ich_framework.md` (ICH Q1A-Q1E, Q5C) |
| 3.2.P (DP) | `small_molecule_drug/api_quality.md` (formulation principles) |
| 3.2.A (Adventitious agents) | `cross_category/cmc_difference.md` |
| 3.2.R (China-specific) | `china_cmc_special/regulatory_framework.md` |
| BsAb-specific considerations | `cross_category/cmc_difference.md` (bispecific section) |
| NDA filing requirements | `declaration_practice/nda_cmc_zh.md` |
| CDE review expectations | `china_cmc_special/cde_review_trend.md` |

---

## Step 3: Drafting Process (CMC Forge DRAFT)

For each section:
1. Open the section template from `module3-workplan-template.md`
2. Load relevant CMC Research reference for content grounding
3. Populate with data from source documents
4. Mark data placeholders for remaining gaps
5. Run self-check against 42-point quality checklist

---

## Step 4: Writing Quality Review (Scientific Writer)

For the executive summary and any English-facing sections:
- Apply 5-pass audit
- Focus on Banana Rule (terminology consistency) across all sections
- Verify numerical integrity (batch data, stability data, specifications)

---

## Output Classification

```
⚠️ DRAFT — For controlled review. Not a GMP-controlled document.
Module: CMC Forge (PLAN + DRAFT) + CMC Research + Scientific Writer
Classification: L3
Human review required: Yes — CMC Lead + RA Director + QA + SME (per section)
Data cut-off date: [To be declared at compilation]
```

---

## Notes

- All data, company names, and product names are fictional.
- Section map follows `skills/cmc-forge/templates/module3-workplan-template.md`.
- Quality checklist from `skills/cmc-forge/references/quality-checklist.md` (42 items).
- BsAb-specific considerations may require additional characterization beyond standard mAb (dual-binding, forced pairing confirmation).
