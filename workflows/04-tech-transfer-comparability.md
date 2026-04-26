# Workflow 04: Tech Transfer + Comparability Strategy

> **Modules:** CMC Research → CMC Forge (DRAFT + ASSESS)
> **Typical duration:** Multi-session
> **Output level:** L3 (cross-functional review draft)

---

## When to Use

- Technology transfer to CDMO or internal site
- Manufacturing site change
- Process change requiring comparability assessment
- Post-approval change management (China NMPA, US FDA, EU EMA)
- Scale-up from clinical to commercial manufacturing

---

## Step-by-Step Process

### Step 1: Define Transfer/Change Context

Collect:
```
- Transfer type: site change, scale change, process change, equipment change, raw material change
- Drug type and current stage
- Source site vs. destination site
- Regions affected (China, US, EU)
- Regulatory classification pre-assessment (if known)
- Available characterization and process data
```

### Step 2: Knowledge Grounding

Load CMC Research references:

| Topic | Load From CMC Research |
|-------|----------------------|
| Process validation expectations | `quality_system/process_validation.md` |
| Post-market variation filing (China) | `declaration_practice/variation_report.md` |
| China regulatory framework | `china_cmc_special/regulatory_framework.md` |
| CDMO management | `quality_system/process_validation.md` (CDMO section) |
| MAH responsibilities | `quality_system/mah_management.md` |
| Inspection risk | `quality_system/audit_risk.md` |

Load CMC Forge playbooks:
- `skills/cmc-forge/playbooks/risk-comparability.md` — comprehensive comparability framework
- `skills/cmc-forge/playbooks/gmp-qa-principles.md` — GMP execution fundamentals

### Step 3: Risk Assessment

Invoke **CMC Forge ASSESS mode**:

**Produce:**
- Current vs. proposed state comparison
- CQA impact hypothesis matrix
- FMEA risk register with RPN scoring
- Risk heat map classification

**Use template:** `skills/cmc-forge/templates/change-comparability-template.md`

### Step 4: Comparability Strategy

Based on risk assessment, design the three-step comparability evidence plan:

```
Step 1: Quality/Analytical Comparability
- Side-by-side analytical characterization
- CQA-by-CQA comparison with pre-defined acceptance criteria
- Statistical analysis plan

Step 2: Non-Clinical Bridge (if needed)
- In vitro bioactivity comparison
- PK/PD bridging (if applicable)
- Safety assessment (if applicable)

Step 3: Clinical Bridge (if needed)
- PK bridging study design
- Clinical endpoints (if applicable)
- Immunogenicity assessment (for biologics)
```

**Decision logic:** Risk level determines comparability depth.
- Low risk → Step 1 only
- Medium risk → Steps 1 + 2
- High risk → Steps 1 + 2 + 3

### Step 5: Tech Transfer Work Package (if applicable)

If the scenario involves technology transfer:

Invoke **CMC Forge DRAFT mode** with:
- `skills/cmc-forge/templates/tech-transfer-template.md`

**Produce:**
- Knowledge transfer checklist (process, analytical, materials, equipment)
- Critical knowledge preservation table
- Workstream breakdown (process, analytical, quality, supply chain, validation)
- Phase sequence with milestones
- Acceptance criteria framework
- Communication and governance structure

### Step 6: Regulatory Path Analysis

Determine regulatory classification across affected regions:

| Region | Classification Framework |
|--------|------------------------|
| **China (NMPA)** | Record / Notification / Approval (变更管理办法) |
| **US (FDA)** | CBE-30 / CBE-0 / PAS (21 CFR 601.12 / 314.70) |
| **EU (EMA)** | Type IA / Type IB / Type II (Regulation 1234/2008) |

Reference: `skills/cmc-forge/references/regulatory-anchors.md`

### Step 7: Deliver

Output structure:
```
⚠️ DRAFT — For controlled review. Not a GMP-controlled document.
Module: CMC Forge (DRAFT + ASSESS)
Classification: L3
Human review required: Yes — CMC Lead + QA + RA + SME

[Tech Transfer / Comparability Package]
1. Transfer/change summary and classification
2. Current vs. proposed state comparison
3. CQA impact assessment matrix
4. FMEA risk register
5. Comparability evidence plan (3-step)
6. Tech transfer work package (if applicable)
7. Regulatory path analysis (by region)
8. Implementation timeline with dependencies
9. Post-implementation monitoring plan
10. Open questions register
```

---

## Quality Checkpoints

- [ ] Risk register has RPN scores, not just qualitative descriptions
- [ ] Comparability acceptance criteria are pre-defined and justified
- [ ] No fabricated process data or batch results
- [ ] Regulatory classification is advisory, not final determination
- [ ] Timeline accounts for validation batch scheduling and testing turnaround
- [ ] MAH/quality agreement considerations addressed (for CDMO transfers)
- [ ] GMP compliance expectations stated for receiving site
