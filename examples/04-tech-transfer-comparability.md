# Example 04: Tech Transfer + Comparability Strategy

> **Integrated scenario:** An ADC drug tech transfer from originator site to CDMO, with comparability strategy for multi-regional filing.
> **Modules invoked:** CMC Research + CMC Forge (ASSESS + DRAFT)
> **Workflow:** [04-tech-transfer-comparability.md](../workflows/04-tech-transfer-comparability.md)

---

## Scenario Background

**Company:** OncoLink Biopharma (fictional)
**Product:** OL-200, anti-HER2 ADC (IgG1 mAb, cleavable linker, MMAE payload)
**Indication:** HER2+ breast cancer, second-line
**Current status:**
- Phase II ongoing in China and US simultaneously
- Manufactured at internal R&D facility (50L/200L single-use)
- DAR (Drug-to-Antibody Ratio) control is critical CQA
- Target: transfer to CDMO 500L single-use for Phase III and commercial

**Strategic goal:**
1. Tech transfer to CDMO by Q2 2027
2. Generate comparability data for NMPA and FDA simultaneously
3. Support Phase III manufacturing at CDMO

---

## Step 1: Change Classification

**Transfer type:** Manufacturing site change + scale change (200L → 500L)

**Regulatory classification (preliminary):**

| Region | Likely Classification | Basis |
|--------|----------------------|-------|
| China (NMPA) | Major change (重大变更) | Site change + scale change for biologic |
| US (FDA) | PAS (Prior Approval Supplement) | Manufacturing site change for licensed biologic (if post-approval); CBE for IND-stage |
| EU (EMA) | Type II variation | Manufacturing site change |

---

## Step 2: CQA Impact Assessment

| CQA | Impact Hypothesis | Risk Level | Justification |
|-----|-------------------|------------|---------------|
| Primary structure | No impact | LOW | Same cell line, same genetic construct |
| Higher-order structure | No impact expected | LOW | Process does not affect primary sequence |
| Charge variants | Possible impact | MEDIUM | Scale-up may affect harvest conditions, affecting deamidation |
| Glycosylation | Possible impact | MEDIUM | Culture conditions (pH, feed, temperature) change with scale |
| Aggregate content | Possible impact | HIGH | Scale-up affects mixing, shear, UF/DF loading |
| DAR distribution | Possible impact | HIGH | Conjugation reaction scale-up is critical; DAR distribution is safety-relevant |
| Free drug (MMAE) | Possible impact | MEDIUM | Conjugation/quench scale-up may affect free drug removal |
| Potency (binding) | No impact expected | LOW | Primary structure unchanged |
| Potency (cytotoxicity) | Possible impact | MEDIUM | DAR shift may affect cytotoxicity |
| Process-related impurities | Possible impact | MEDIUM | Scale-up affects impurity clearance |

---

## Step 3: FMEA Risk Register

| # | Risk | S | O | D | RPN | Mitigation |
|---|------|---|---|---|-----|-----------|
| 1 | DAR distribution shift due to conjugation scale-up | 9 | 5 | 3 | 135 | Develop scale-down model at CDMO; DoE on conjugation parameters |
| 2 | Aggregate increase due to UF/DF scale-up | 7 | 4 | 3 | 84 | Optimize UF/DF loading and cross-flow rate at new scale |
| 3 | Glycosylation pattern shift | 6 | 4 | 3 | 72 | Control culture pH and feed strategy; monitor closely in PPQ |
| 4 | Free drug increase due to quench scale-up | 8 | 3 | 2 | 48 | Validate quench step; include free drug as PPQ critical parameter |
| 5 | Viral clearance different at new scale | 8 | 2 | 2 | 32 | Viral clearance validation at new scale required |
| 6 | Raw material lot-to-lot variability at CDMO | 5 | 4 | 4 | 80 | Qualify alternative raw materials; establish incoming testing |

---

## Step 4: Three-Step Comparability Evidence Plan

### Step 1: Quality/Analytical Comparability

**Design:**
- 3 PPQ batches at CDMO (500L) vs. 3 clinical batches at originator (200L)
- Side-by-side characterization of all CQAs

**Acceptance criteria framework:**

| CQA | Acceptance Criterion | Method |
|-----|---------------------|--------|
| Primary structure | Identical (peptide mapping, MS) | LC-MS/MS |
| Charge variants | Within historical range ± 2SD | cIEF |
| Glycosylation (G0f, G1f, G2f, afucosylated) | Within historical range ± 2SD | HILIC |
| Aggregate (HMW) | ≤ 2.0% | SE-HPLC |
| DAR (average) | 3.5–4.0 | HIC-HPLC |
| DAR distribution (D0, D2, D4, D6, D8) | Within historical range | HIC-HPLC |
| Free MMAE | ≤ 0.5% | RP-HPLC |
| Binding affinity (HER2) | 80–120% relative to reference | ELISA/SPR |
| Potency (cell-based) | 80–120% relative to reference | Cytotoxicity assay |

**Statistical approach:** Equivalence testing (TOST) where applicable; range comparison for qualitative attributes.

### Step 2: Non-Clinical Bridge

**Design:**
- In vitro cytotoxicity comparison (5 cell lines)
- HER2 binding affinity comparison
- Fc effector function comparison (ADCC, CDC)
- Tissue cross-reactivity (if requested by NMPA)

**Trigger for Step 3:** If any CQA falls outside acceptance criteria AND Step 2 shows functional impact.

### Step 3: Clinical Bridge (contingent)

**Design (if triggered):**
- Single-dose PK study (cross-over or parallel)
- Immunogenicity monitoring (ADA, NAb)
- Safety assessment

---

## Step 5: Knowledge Grounding (CMC Research)

| Topic | Reference |
|-------|-----------|
| ADC CMC considerations | `biologic_drug/adc_cmc_zh.md` |
| Process validation | `quality_system/process_validation.md` |
| CDMO management | `quality_system/process_validation.md` (CDMO section) |
| MAH responsibilities | `quality_system/mah_management.md` |
| Post-market variation (China) | `declaration_practice/variation_report.md` |
| Variation filing template | `knowledge/CMC_Research/resources/zh-CN/templates/compliance/variation_filing_template.md` |
| ADC DAR control case study | `knowledge/CMC_Research/resources/zh-CN/cases/frontier_drug/adc_dar_control_case.md` |

---

## Step 6: Tech Transfer Work Package

Using `skills/cmc-forge/templates/tech-transfer-template.md`:

**Phase sequence:**
```
Month 1-2:  CDMO qualification + knowledge transfer
Month 2-4:  Scale-down model development (conjugation critical)
Month 3-5:  Analytical method transfer + co-validation
Month 4-6:  Process development at CDMO (500L engineering runs)
Month 6-8:  PPQ (3 consecutive batches)
Month 7-9:  Comparability data analysis + report
Month 8:    Stability initiation (CDMO batches)
Month 9-10: Regulatory submission preparation
Month 10-12: Submission + inspection readiness
```

---

## Output Classification

```
⚠️ DRAFT — For controlled review. Not a GMP-controlled document.
Module: CMC Forge (ASSESS + DRAFT) + CMC Research
Classification: L3
Human review required: Yes — CMC Director + QA VP + RA (China + US) + CDMO PM
```

---

## Notes

- All data, company names, product names, and timelines are fictional.
- ADC-specific risks (DAR control, free drug) highlighted per `knowledge/CMC_Research/CMC_COMPREHENSIVE_GUIDE/biologic_drug/adc_cmc_zh.md`.
- Risk register format from `skills/cmc-forge/playbooks/risk-comparability.md`.
- Comparability framework follows ICH Q5E and NMPA biosimilar/complex biologics guidance.
