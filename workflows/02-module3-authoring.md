# Workflow 02: Module 3 Authoring

> **Modules:** CMC Research → CMC Forge (DRAFT + PLAN) → Scientific Writer (REVIEW)
> **Typical duration:** Multi-session (Module 3 is a large deliverable)
> **Output level:** L3 (cross-functional review draft)

---

## When to Use

- IND Module 3 CMC preparation
- NDA/BLA Module 3 authoring
- Post-approval variation Module 3 supplements
- Module 3 gap filling for existing submissions

---

## Step-by-Step Process

### Step 1: Scope and Plan

Invoke **CMC Forge PLAN mode** to create the Module 3 workplan.

**Load:**
- `skills/cmc-forge/templates/module3-workplan-template.md` — full CTD section map
- `skills/cmc-forge/references/deliverable-patterns.md` — Module 3 Workplan pattern

**Collect:**
```
- Filing type (IND, NDA/BLA, variation)
- Drug substance type (chemical, biologic, ATMP, etc.)
- Target region(s) and regulatory agency
- Available source documents
- Known gaps in documentation
- Timeline and submission target date
```

**Output:** Module 3 workplan with section map, source document inventory, gap log, and timeline.

### Step 2: Regulatory Framework Alignment

Load relevant CMC Research documents for content grounding:

| Module 3 Section | CMC Research Reference |
|-----------------|----------------------|
| 3.2.S Drug Substance | `small_molecule_drug/api_quality.md` or `biologic_drug/biologic_basic.md` |
| 3.2.P Drug Product | `small_molecule_drug/api_quality.md` (formulation section) |
| 3.2.A Appendices | `quality_system/process_validation.md`, `cross_category/cmc_difference.md` |
| 3.2.R Regional Info | `china_cmc_special/regulatory_framework.md` |
| Stability sections | `basic_theory/ich_framework.md` (ICH Q1A-Q1E) |
| Analytical methods | `basic_theory/ich_framework.md` (ICH Q2, Q14) |

### Step 3: Section-by-Section Drafting

Invoke **CMC Forge DRAFT mode** for each section.

**Process per section:**
1. Review workplan entry for the section
2. Load relevant CMC Research reference content
3. Apply appropriate template structure
4. Draft section with regulatory-anchored content
5. Run internal quality checks (42-point checklist)

**Drafting order (recommended):**
```
3.2.S.2 Manufacturing Process → 3.2.S.3 Characterization → 3.2.S.4 Control
→ 3.2.S.5 Reference Standards → 3.2.S.6 Container Closure → 3.2.S.7 Stability
→ 3.2.P sections (mirror structure)
→ 3.2.A Appendices → 3.2.R Regional
```

### Step 4: Writing Quality Review

For English-facing sections or summaries:

Invoke **Scientific Writer REVIEW mode** (5-pass audit):
1. **Pass 1 — Clutter Extraction:** Remove redundancy, wordiness
2. **Pass 2 — Voice/Verb Vitality:** Strengthen passive constructions, activate verbs
3. **Pass 3 — Sentence Architecture:** Check sentence length, buried predicates
4. **Pass 4 — Keyword Consistency (Banana Rule):** Verify terminology consistency across all sections
5. **Pass 5 — Numerical/Citation Integrity:** Verify numbers, cross-references, and citations against user-provided source material only

**Load:** `skills/scientific-writer/references/writing-quality.md`

### Step 5: Cross-Section Consistency Check

Run the 15-point consistency check from the Module 3 workplan template:
- Terminology consistency across 3.2.S and 3.2.P
- Cross-reference integrity
- Data alignment between sections
- Version control of referenced documents

### Step 6: Deliver

Output structure per section:
```
⚠️ DRAFT — For controlled review. Not a GMP-controlled document.
Module: CMC Forge (DRAFT) + Scientific Writer (REVIEW)
Classification: L3
Human review required: Yes — CMC Lead + RA + QA + SME (per section)

[Section Draft]
- Section heading (CTD numbering)
- Content per template structure
- Embedded data placeholders [DATA: description]
- Cross-references to other sections
- Regulatory citations
- Known gaps and open questions
```

---

## Quality Checkpoints

- [ ] All sections follow CTD numbering and structure
- [ ] No fabricated data — all values are placeholders or from provided sources
- [ ] Terminology consistent across all sections (Banana Rule)
- [ ] Cross-references validated
- [ ] Each section has DRAFT header with reviewer assignments
- [ ] Data cut-off date declared
- [ ] Missing content log maintained and current
