# routing.md — Signal-to-Module Routing Guide

## How to Use This Guide

When a user request arrives, match it against the signal patterns below to determine which module(s) to invoke. If a request matches multiple signals, use the workflow files in `workflows/` for orchestrated execution.

---

## Route Matrix

### Route 1: CMC Knowledge Lookup → CMC Research

**Signals:**
- Regulations, guidelines, guidance documents
- "What does NMPA/CDE/FDA/EMA require for..."
- Pharmacopoeia, ICH Q-series
- Case studies, deficiency letter analysis
- China-specific regulatory framework questions
- Templates and checklists (NDA checklist, MAH agreement, variation filing)

**Action:** Load relevant `knowledge/CMC_Research/CMC_COMPREHENSIVE_GUIDE/` sub-document or `resources/zh-CN/` resource file.

Path note: workflow references such as `declaration_practice/ind_cmc_zh.md` are relative to `knowledge/CMC_Research/CMC_COMPREHENSIVE_GUIDE/` unless another base path is specified.

**Output type:** Factual reference with source attribution.

---

### Route 2: CMC Drafting → CMC Forge (DRAFT mode)

**Signals:**
- Draft, write, generate CMC documents
- PPQ protocol, comparability strategy, tech transfer package
- Module 3 section drafting
- Stage-gate readiness pack
- Change control documentation

**Action:** Activate CMC Forge DRAFT mode. Load appropriate template from `skills/cmc-forge/templates/`.

**Output type:** Structured draft document with `⚠️ DRAFT` header.

---

### Route 3: CMC Assessment → CMC Forge (ASSESS mode)

**Signals:**
- Assess, evaluate, gap analysis, readiness check
- Developability, IND readiness, change impact, analytical maturity
- Risk assessment, FMEA, red-yellow-green scoring
- Comparability assessment

**Action:** Activate CMC Forge ASSESS mode. Load relevant playbook (developability, risk-comparability, compliance-continuum, early-prioritization).

**Output type:** Structured assessment with risk ratings and action packages.

---

### Route 4: CMC Planning → CMC Forge (PLAN mode)

**Signals:**
- Plan, roadmap, work package, timeline
- Stage-gate work plan, evidence roadmap, deliverable decomposition
- China-first-then-global strategy
- Module 3 authoring workplan

**Action:** Activate CMC Forge PLAN mode. Load relevant template and reference (china-global-cmc-operating-model, project-archetypes, deliverable-patterns).

**Output type:** Structured plan with milestones, dependencies, and human review gates.

---

### Route 5: Scientific Writing → Scientific Writer

**Signals:**
- Write, draft scientific/academic text
- Review, polish, improve writing quality
- Diagnose structural issues in text
- Learn scientific writing methodology
- English quality for FDA/EMA-facing documents
- CMC rationale language, manuscript sections

**Action:** Activate Scientific Writer in appropriate mode (WRITE/REVIEW/DIAGNOSE/LEARN). Load relevant section model from `skills/scientific-writer/references/section-models.md` or `skills/scientific-writer/references/writing-quality.md`.

**Output type:** Revised text with quality audit, or structural diagnostic report.

---

### Route 6: Knowledge-Grounded Execution → CMC Research + CMC Forge

**Signals:**
- "Based on NMPA requirements, assess our IND readiness"
- "Check CDE guidelines and draft a comparability strategy"
- Any request that combines regulatory context with CMC execution

**Action:**
1. CMC Research: Look up relevant regulatory requirements
2. CMC Forge: Execute assessment/drafting against those requirements

**Output type:** Contextualized CMC deliverable with regulatory citations.

---

### Route 7: Full Pipeline → CMC Research + CMC Forge + Scientific Writer

**Signals:**
- "Draft an FDA-facing CMC summary and review the English quality"
- "Write Module 3 rationale sections with publication-quality language"
- Any request requiring knowledge lookup + CMC execution + writing quality

**Action:**
1. CMC Research: Regulatory context
2. CMC Forge: Generate CMC draft
3. Scientific Writer: 5-pass writing quality audit

**Output type:** Polished, compliance-annotated CMC deliverable.

---

### Route 8: Training & Knowledge Building → CMC Forge (TRAIN mode) + CMC Research

**Signals:**
- Train, teach, learning materials
- Quick-reference, FAQ, knowledge base
- Onboarding materials for new team members

**Action:**
1. CMC Forge TRAIN mode: Generate training content
2. CMC Research: Provide reference materials and case studies

**Output type:** Structured training package with references.

---

## Conflict Resolution

When a request matches multiple routes:

1. **Specific beats general:** "Draft an NMPA-compliant PPQ protocol" → Route 2 (not Route 1)
2. **Execution beats knowledge:** If both knowledge lookup and execution are possible, default to execution with embedded knowledge references
3. **Chinese-language regulatory questions** → always route through CMC Research first
4. **English-language deliverables** → always include Scientific Writer in pipeline

## Minimal Load Rule

Only load the reference files needed for the current task. Do not load all module files simultaneously. Each workflow specifies the minimum required files.
