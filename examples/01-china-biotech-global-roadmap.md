# Example 01: China Biotech mAb — China-First then Global CMC Roadmap

> **Integrated scenario:** A Chinese biotech company developing a novel anti-PD-1 IgG4 mAb, currently in Phase II in China, planning for global expansion (US + EU).
> **Modules invoked:** CMC Research + CMC Forge (ASSESS + PLAN)
> **Workflow:** [03-china-global-roadmap.md](../workflows/03-china-global-roadmap.md)

---

## Scenario Background

**Company:** BioGenesis Therapeutics (fictional)
**Product:** BG-001, anti-PD-1 IgG4 (S228P) monoclonal antibody
**Indication:** Non-small cell lung cancer (NSCLC), second-line
**Current status:**
- Phase I completed in China (CDE IND: CXL2024001)
- Phase II ongoing at 3 sites in China
- Manufacturing at internal 200L/500L facility (USP + DSP + formulation/fill)
- Analytical methods developed and qualified, not yet validated
- Stability data: 6 months accelerated, 12 months long-term (2°C–8°C)

**Strategic goal:** File US FDA IND by Q4 2027, EU EMA clinical trial application by Q1 2028.

---

## Step 1: Company Posture Identification

**Posture: China-first then global**

From `skills/cmc-forge/references/china-global-cmc-operating-model.md`:
- Build one coherent CMC narrative, then express regional deltas
- Strategy: Complete Phase II/III in China while building global-ready CMC package

---

## Step 2: Regulatory Context (from CMC Research)

### China (Current — Phase II)
- `declaration_practice/ind_cmc_zh.md`: CDE IND requirements met
- `china_cmc_special/regulatory_framework.md`: MAH system compliance established
- `china_cmc_special/cde_review_trend.md`: CDE increasing scrutiny on CQA control strategy

### US (Target — IND)
- `basic_theory/ich_framework.md`: ICH M4Q CTD format required
- `cross_category/cmc_difference.md`: FDA expects process characterization data, comparability protocol if scaling
- `skills/cmc-forge/references/regulatory-anchors.md`: FDA PQ/CMC guidance

### EU (Target — CTA)
- `basic_theory/ich_framework.md`: EMA CTD format, largely harmonized with FDA
- Key delta: EMA may require additional stability data for EU climatic zones

---

## Step 3: Gap Assessment (CMC Forge ASSESS)

### Dimension Scoring

| Dimension | Status | Score | Key Gap |
|-----------|--------|-------|---------|
| Drug substance characterization | Partially complete | YELLOW | Higher-order structure not fully characterized; charge variant heterogeneity needs deeper analysis |
| Manufacturing process | Defined at clinical scale | YELLOW | Process characterization incomplete; no design space established |
| Analytical methods | Qualified, not validated | RED | Methods need full ICH Q2(R2) validation; some methods missing for global requirements |
| Stability | 12 months ongoing | YELLOW | Need ICH Q1A(R2) full stability protocol; in-use stability missing |
| Reference standards | Working standards only | YELLOW | Need primary reference standard establishment and characterization |
| Container closure | Vial (clinical) | YELLOW | Need commercial container closure selection and compatibility studies |
| Process validation | Not started | RED | Clinical-scale only; no PPQ plan |
| Quality system | Established (China GMP) | YELLOW | Need to demonstrate equivalence to FDA cGMP |

### Must-Solve-Now vs. Can-Defer

**Must-solve-now (before FDA IND):**
1. Analytical method validation (ICH Q2(R2))
2. Process characterization critical parameters
3. Reference standard establishment
4. Stability protocol redesign for global

**Can-defer (post-IND, pre-BLA):**
1. Commercial-scale process validation (PPQ)
2. Container closure commercial selection
3. Process analytical technology (PAT) implementation
4. Full design space establishment

---

## Step 4: Phased Evidence Roadmap (CMC Forge PLAN)

### Phase 1: Foundation Building (Q3 2026 – Q1 2027)

| Activity | Deliverable | Timeline |
|----------|------------|----------|
| Analytical method validation (ICH Q2(R2)/Q14) | Validation reports for 8 core methods | 4 months |
| Reference standard establishment | Primary reference standard characterization report | 2 months |
| Process characterization (DoE) | Critical process parameters identified, preliminary control strategy | 3 months |
| Stability protocol redesign | Global stability protocol per ICH Q1A(R2) | 1 month |

### Phase 2: China Phase III + Global Preparation (Q2 2027 – Q3 2027)

| Activity | Deliverable | Timeline |
|----------|------------|----------|
| Module 3 CTD authoring (FDA format) | Draft Module 3 for FDA IND | 3 months |
| CMC summary (QS/CMC) | FDA CMC summary section | 1 month |
| Regional delta analysis (China → US) | Gap assessment and bridge strategy | 1 month |
| English writing quality review | 5-pass audit on all English sections | 1 month |

### Phase 3: US FDA IND Filing (Q4 2027)

| Activity | Deliverable | Timeline |
|----------|------------|----------|
| Final Module 3 compilation | Complete Module 3 package | 1 month |
| Cross-reference integrity check | Consistency verification report | 2 weeks |
| FDA pre-IND meeting (optional) | Meeting package and minutes | 1 month |
| IND submission | eCTD submission to FDA | — |

### Phase 4: EU CTA + Ongoing (Q1 2028+)

| Activity | Deliverable | Timeline |
|----------|------------|----------|
| EU regional delta (Module 1 + 2) | Regional-specific sections | 2 months |
| EU stability climatic zone data | Additional stability data if required | Ongoing |
| Commercial-scale process development | Scale-up and PPQ readiness | 6–9 months |

---

## Step 5: Key Risks

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Analytical method validation reveals gaps | Delays IND 2–3 months | Start with risk-ranked methods; validate highest-priority first |
| Process characterization shows unexpected sensitivity | Control strategy revision needed | Build characterization plan with worst-case ranges |
| FDA requests additional stability data | Delays IND review | Include rolling stability update strategy in IND cover letter |
| Scale-up introduces CQA shifts | Comparability study needed | Plan scale-up with concurrent comparability protocol |

---

## Output Classification

```
⚠️ DRAFT — For controlled review. Not a GMP-controlled document.
Module: CMC Forge (ASSESS + PLAN) + CMC Research
Classification: L2
Human review required: Yes — CMC VP + Head of RA (China + US)
```

---

## Notes

- All data, timelines, and assessments in this example are fictional and for illustration only.
- Company posture "China-first then global" follows the operating model in `skills/cmc-forge/references/china-global-cmc-operating-model.md`.
- Gap dimensions follow the stage-gate readiness template from `skills/cmc-forge/templates/stage-gate-readiness-template.md`.
