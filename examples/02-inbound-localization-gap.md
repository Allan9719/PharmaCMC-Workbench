# Example 02: Overseas Biologic → China Local Manufacturing CMC Localization Gap Assessment

> **Integrated scenario:** A global pharma company bringing an approved EU/US biologic to China, planning local manufacturing at a Chinese CDMO.
> **Modules invoked:** CMC Research + CMC Forge (ASSESS + DRAFT)
> **Workflow:** [03-china-global-roadmap.md](../workflows/03-china-global-roadmap.md) + [04-tech-transfer-comparability.md](../workflows/04-tech-transfer-comparability.md)

---

## Scenario Background

**Company:** GlobalBio Pharma (fictional)
**Product:** GB-500, anti-TNFα IgG1 mAb (approved in EU since 2020, US since 2021)
**Indication:** Rheumatoid arthritis, ankylosing spondylitis
**Current status:**
- Approved in 50+ countries (EU, US, Japan, etc.)
- Manufactured at EU site (2000L stainless steel, 4 batches/year)
- Full Module 3 available in eCTD format (EU/US)
- China import license held; sold as imported drug since 2022
- MAH license holder: GlobalBio China subsidiary

**Strategic goal:** Transfer manufacturing to Chinese CDMO by 2028 for cost reduction and supply chain resilience. File NMPA variation (major change) for manufacturing site addition.

---

## Step 1: Company Posture

**Posture: Inbound localization**

From `skills/cmc-forge/references/china-global-cmc-operating-model.md`:
- Overseas product with established global CMC package
- Need to demonstrate local manufacturing produces comparable product
- Must meet NMPA/CDE expectations for manufacturing site addition

---

## Step 2: Regulatory Context (from CMC Research)

### China Requirements
- `declaration_practice/variation_report.md`: Major change category — manufacturing site addition requires full comparability + on-site inspection
- `china_cmc_special/regulatory_framework.md`: NMPA requires comprehensive CMC dossier for site change
- `quality_system/process_validation.md`: Process validation per Chinese GMP expectations
- `quality_system/mah_management.md`: MAH responsibilities for CDMO oversight
- `quality_system/audit_risk.md`: Inspection risk management for new site

### Global Reference
- `cross_category/cmc_difference.md`: EU/US vs. China regulatory differences
- ICH Q5E: Comparability of biotechnological/biological products

---

## Step 3: Gap Assessment (CMC Forge ASSESS)

### Gap Categories

| Category | Gap Description | Severity |
|----------|----------------|----------|
| **Process knowledge transfer** | EU site uses stainless steel 2000L; CDMO has single-use 500L/1000L | CRITICAL — process format change |
| **Cell bank** | Need Chinese cell bank establishment from MCB/WCB transfer | HIGH — requires NIFDC testing |
| **Analytical methods** | Methods established at EU site; need transfer and validation at CDMO + China lab | HIGH |
| **Reference standards** | Need China-deposited reference standards | MEDIUM |
| **Raw materials** | Some EU-sourced raw materials may not have China DMF; need alternatives | HIGH |
| **Stability** | Need China-manufactured stability data per ICH Q1A(R2) and NMPA expectations | HIGH |
| **Comparability** | EU-origin vs. China-origin full analytical comparability required | CRITICAL |
| **Quality system** | CDMO quality system must meet Chinese GMP + MAH oversight requirements | HIGH |
| **Container closure** | Current EU vial + pre-filled syringe; CDMO may have different platform | MEDIUM |
| **Regulatory pathway** | NMPA major change variation + potential on-site inspection | HIGH |

### Must-Solve-Now
1. CDMO qualification and quality agreement (MAH template from CMC Research)
2. Cell bank transfer protocol (ICH Q5A(R2) + NIFDC requirements)
3. Process transfer and scale-down model development
4. Analytical method transfer protocol
5. Comparability study design and acceptance criteria

---

## Step 4: Tech Transfer Plan (CMC Forge DRAFT)

### Using Template: `skills/cmc-forge/templates/tech-transfer-template.md`

**Transfer objective:** Transfer manufacturing process for GB-500 from EU origin site to Chinese CDMO site, enabling local commercial supply.

**Knowledge transfer checklist:**

| Category | Items | Status |
|----------|-------|--------|
| Process knowledge | USP parameters, DSP chromatography conditions, formulation recipe, fill parameters | To transfer |
| Analytical methods | 12 release methods, 6 characterization methods, stability-indicating methods | To transfer |
| Materials | Cell bank, reference standard, critical raw materials | To transfer |
| Equipment | Bioreactor, chromatography columns, UF/DF system, fill/finish line | CDMO to qualify |
| Quality systems | Deviation management, CAPA, change control, batch release | To align |

**Phase sequence:**
1. Project kickoff and CDMO qualification (Month 1–2)
2. Knowledge transfer and training (Month 2–4)
3. Process development at CDMO (scale-down model + optimization) (Month 3–6)
4. Analytical method transfer and co-validation (Month 4–7)
5. Process performance qualification (PPQ) — 3+ consecutive batches (Month 7–10)
6. Comparability study execution (Month 8–11)
7. Stability study initiation (Month 9)
8. NMPA variation submission (Month 12)
9. NMPA on-site inspection readiness (Month 12–14)

---

## Step 5: Comparability Strategy (from risk-comparability playbook)

**Three-step comparability:**

**Step 1: Quality/Analytical Comparability (mandatory)**
- Full side-by-side characterization: primary structure, higher-order structure, charge variants, glycosylation, size variants, bioactivity, binding affinity
- CQA-by-CQA comparison with pre-defined acceptance criteria
- Statistical analysis (equivalence testing where applicable)

**Step 2: Non-Clinical Bridge (likely needed)**
- In vitro bioactivity comparison
- Fc effector function comparison (ADCC, CDC if applicable)
- Tissue cross-reactivity (if required by NMPA)

**Step 3: Clinical Bridge (unlikely but contingent)**
- PK bridging study if Steps 1 + 2 show significant differences
- NMPA may request based on comparability results

---

## Step 6: Regulatory Path (China)

**NMPA Classification:** Major change (重大变更) — manufacturing site addition
**Required submissions:**
1. Variation application form
2. Updated Module 3 (new manufacturing site)
3. Comparability study report
4. Process validation report (PPQ)
5. Stability data (at least 6 months)
6. Quality agreement between MAH and CDMO
7. CDMO GMP compliance evidence

**Expected timeline:** 12–18 months from submission to approval (including inspection).

---

## Output Classification

```
⚠️ DRAFT — For controlled review. Not a GMP-controlled document.
Module: CMC Forge (ASSESS + DRAFT) + CMC Research
Classification: L2
Human review required: Yes — China RA Lead + CMC VP + QA Director + CDMO PM
```

---

## Notes

- All data, timelines, and company/product names are fictional.
- Gap categories follow stage-gate readiness template dimensions.
- Comparability framework from `skills/cmc-forge/playbooks/risk-comparability.md`.
- Tech transfer structure from `skills/cmc-forge/templates/tech-transfer-template.md`.
- MAH quality agreement template available at `knowledge/CMC_Research/resources/zh-CN/templates/practice/mah_quality_agreement_template.md`.
