# Workflow 01: CMC Readiness Assessment

> **Modules:** CMC Research → CMC Forge (ASSESS)
> **Typical duration:** 30–60 minutes
> **Output level:** L2 (team discussion draft)

---

## When to Use

- Pre-IND CMC readiness check
- Stage-gate readiness assessment (Phase I → II → III → BLA)
- Analytical method maturity evaluation
- Developability risk assessment for candidate molecules
- Change impact assessment (pre- or post-approval)

---

## Step-by-Step Process

### Step 1: Define Assessment Scope

Collect project context using CMC Forge's "First Move" framework:

```
Required information:
- Drug type (mAb, BsAb, ADC, CGT, small molecule, etc.)
- Current development stage (pre-IND, Phase I/II/III, BLA, post-approval)
- Target region(s) (China only, China + global, global)
- Company posture (see: skills/cmc-forge/references/china-global-cmc-operating-model.md)
- Specific assessment focus (if any)
```

### Step 2: Regulatory Context Lookup

Load relevant CMC Research knowledge:

| Assessment Focus | Load From CMC Research |
|-----------------|----------------------|
| IND filing readiness | `declaration_practice/ind_cmc_zh.md` |
| NDA/BLA readiness | `declaration_practice/nda_cmc_zh.md` |
| China regulatory framework | `china_cmc_special/regulatory_framework.md` |
| Process validation | `quality_system/process_validation.md` |
| CDE review expectations | `china_cmc_special/cde_review_trend.md` |
| Pharmacopoeia compliance | `china_cmc_special/pharmacopoeia_2025.md` |
| ATMP-specific | `biologic_drug/atmp_cmc_zh.md` |
| ADC-specific | `biologic_drug/adc_cmc_zh.md` |

### Step 3: Execute Assessment

Invoke **CMC Forge ASSESS mode** with the context gathered.

CMC Forge will produce:
- Red-Yellow-Green scoring across relevant dimensions
- Must-solve-now vs. can-defer prioritization
- Gap register with severity ratings
- Recommended action packages (30/60/90-day)

**Reference playbooks to load (as needed):**
- `skills/cmc-forge/playbooks/druggability-assessment.md` — for candidate developability
- `skills/cmc-forge/playbooks/early-prioritization.md` — for IND-enabling priority
- `skills/cmc-forge/playbooks/risk-comparability.md` — for change/comparability assessment
- `skills/cmc-forge/playbooks/compliance-continuum.md` — for lifecycle compliance

**Template to use:**
- `skills/cmc-forge/templates/stage-gate-readiness-template.md` — structured readiness pack

### Step 4: Review and Refine

- Verify assessment against CMC Research regulatory references
- Ensure red-yellow-green ratings have evidence basis
- Check action packages are stage-appropriate
- Validate terminology consistency (Banana Rule from quality-checklist)

### Step 5: Deliver

Output structure:
```
⚠️ DRAFT — For controlled review. Not a GMP-controlled document.
Module: CMC Forge (ASSESS)
Classification: L2
Human review required: Yes — CMC Lead + QA

[Assessment Deliverable]
- Scope and assumptions
- Dimension scoring (Red/Yellow/Green)
- Gap register
- Priority action packages
- Open questions for team discussion
- Recommended next steps
```

---

## Quality Checkpoints

- [ ] All assumptions and unknowns explicitly stated
- [ ] No fabricated batch data, specifications, or validation results
- [ ] Regulatory citations traceable to CMC Research sources
- [ ] Terminology consistent throughout
- [ ] Stage-appropriate expectations applied
- [ ] DRAFT header and classification level present
