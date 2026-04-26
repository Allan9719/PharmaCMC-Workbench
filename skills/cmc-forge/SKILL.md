---
name: cmc-forge
description: >
  Pharmaceutical CMC work engine for drafting regulated documents, assessing risks and gaps,
  planning stage-gated projects, and building training assets. Triggers when the user asks to
  draft or write a PPQ protocol, validation plan, Module 3 section, comparability strategy,
  tech transfer package, or stage-gate readiness assessment. Also use for CMC gap analysis,
  risk assessment, developability evaluation, analytical lifecycle planning, regulatory meeting
  preparation, change impact assessment, IND/BLA/NDA CMC readiness, post-approval change
  management (PACMP/EC), inspection readiness, or CMC training and FAQ design. Use whenever
  the user mentions CMC, process validation, analytical method, tech transfer, comparability,
  Module 3, CTD, quality package, stage-gate, control strategy, specifications, stability,
  biosimilar, biologic manufacturing, China CDE/NMPA submission, global filing strategy,
  China-to-global CMC bridging, overseas MAH/CDMO transfer, dual-language CMC package,
  or any pharmaceutical quality topic — even informally.
  Do NOT use for statistical analysis, clinical trial design, non-CMC regulatory affairs,
  medical writing (use scientific-writer instead), or reference/bibliography formatting.
---

# CMC Forge

A stage-aware CMC work engine that combines domain playbooks with structured templates to produce fit-for-phase deliverables for regulated pharmaceutical environments.

**Naming rationale**: "Forge" reflects the act of building — forging strategies, documents, risk assessments, and project plans from raw domain knowledge into deliverable assets.

## Core Principles

1. **Stage-appropriate, not one-size-fits-all**: Compliance is a continuum — "just enough" at each phase, not overbuilt early or underbuilt late.
2. **Facts before assumptions**: Separate known evidence from assumptions and unknowns. Never invent data.
3. **Human authority always**: This skill drafts, structures, and synthesizes — it does not approve, release, or sign off.
4. **Fit-for-phase**: Deliverables match the development stage (Pre-IND ≠ Phase III ≠ Post-approval).

## First Move

Before any drafting, collect the minimum context:

```
REQUIRED CONTEXT (ask if missing):
- Drug type: mAb / bispecific / ADC / fusion protein / small molecule / CGT / other
- Development stage: Pre-IND / Phase I / Phase II / Phase III / BLA/NDA / Post-approval
- Specific ask: What document or decision does the user need?
- Target region(s): China NMPA/CDE / US FDA / EU EMA / Japan PMDA / other
- Company posture: China-only / China-first then global / global-first with China bridge / inbound China localization
```

If the user provides a specific document request (PPQ protocol, Module 3 section, etc.), proceed directly to the matching mode. If the request is ambiguous, classify it:

| Signal | Route To |
|--------|----------|
| "起草/写/draft" a document | **DRAFT** mode |
| "评估/分析/assess" risks, gaps, readiness | **ASSESS** mode |
| "规划/搭框架/plan" project or work package | **PLAN** mode |
| "培训/training/FAQ" knowledge assets | **TRAIN** mode |

Default to **ASSESS** if unclear — understanding the situation before drafting is usually the right call.

### China + Global Orientation

When the user is a Chinese pharmaceutical company or the work may support internationalization:

1. Load `references/china-global-cmc-operating-model.md` before drafting region-sensitive strategy.
2. State the target agency and intended use clearly: China IND/NDA/BLA, US IND/BLA/NDA, EU MAA, post-approval variation, or multi-region core package.
3. Produce a **core CMC package + regional delta** structure when possible, rather than writing separate disconnected documents.
4. Use bilingual terminology when helpful: Chinese working term + English regulatory term, especially for Module 3, CQA/CPP, comparability, validation, tech transfer, and post-approval change terms.
5. Flag items that usually need RA confirmation: classification of CMC changes, CDE communication strategy, FDA supplement/reporting category, EU variation type, PACMP/EC positioning, and authority-specific commitments.

---

## MODE: DRAFT — Document Production

Produce a fit-for-phase CMC document draft.

### DRAFT Workflow

**Step 1: CLASSIFY THE DOCUMENT**
Identify document type and load the matching template:

| Document Type | Template |
|--------------|----------|
| PPQ / Process Validation Protocol | `templates/process-validation-protocol-framework.md` |
| Module 3 Authoring Workplan | `templates/module3-workplan-template.md` |
| Stage-Gate Readiness Pack | `templates/stage-gate-readiness-template.md` |
| Technology Transfer Package | `templates/tech-transfer-template.md` |
| Change & Comparability Strategy | `templates/change-comparability-template.md` |

If no template fits, adapt the nearest one. Read the template for structure guidance.

**Step 2: COLLECT FACTS**
Gather from the user:
- Product and process details
- Available data (batch results, stability, analytical)
- Applicable regulations (ICH, FDA, NMPA/CDE)
- Target market and filing posture (China-only, global core, or region-specific delta)
- Stage-specific constraints

Separate: FACTS (user-provided) | ASSUMPTIONS (stated, not verified) | UNKNOWNS (flagged for later).

**Step 3: SELECT PLAYBOOK**
Load domain playbook for content depth:

| Document Domain | Playbook |
|----------------|----------|
| Candidate evaluation, IND-enabling | `playbooks/druggability-assessment.md` + `playbooks/early-prioritization.md` |
| Process change, comparability | `playbooks/risk-comparability.md` + `playbooks/compliance-continuum.md` |
| GMP execution, QA, deviations | `playbooks/gmp-qa-principles.md` |
| China/global filing, transfer, or dual-region strategy | `references/china-global-cmc-operating-model.md` + relevant template |

Read only the files needed. Do not load everything.

**Step 4: PRODUCE DRAFT**
Fill the template with stage-appropriate content. Follow these rules:

- Use precise CMC terminology (CQA, CPP, NOR, PAR, Cpk, etc.)
- Include acceptance criteria where applicable — even if tentative
- Reference specific ICH/FDA guidance by number
- Add `Draft for controlled review` label on any regulated document
- Write in the language the user used (Chinese or English)

**Step 5: QUALITY CHECK**
Before output, verify against the CMC Quality Checklist in `references/quality-checklist.md`.

**Step 6: OUTPUT**
Present the draft with:
1. Document type and stage context
2. Known facts / Assumptions / Unknowns summary
3. The draft document
4. Flagged decision points requiring human input
5. List of missing evidence that blocks finalization
6. Required reviewers by role

---

## MODE: ASSESS — Risk and Gap Analysis

Evaluate CMC readiness, risks, or gaps.

### ASSESS Workflow

**Step 1: DEFINE SCOPE**
What is being assessed? Common types:
- Developability / candidate risk
- IND-enabling CMC readiness
- Pre-PPQ readiness
- Change impact
- Analytical method maturity
- Comparability strategy soundness

**Step 2: LOAD ASSESSMENT FRAMEWORK**
Read the relevant playbook:
- Candidate risk → `playbooks/druggability-assessment.md`
- Stage readiness → `playbooks/early-prioritization.md` + `playbooks/compliance-continuum.md`
- Change/comparability → `playbooks/risk-comparability.md`
- GMP/QA compliance → `playbooks/gmp-qa-principles.md`

**Step 3: APPLY RED-YELLOW-GREEN SCORING**
For each assessment dimension, use the playbook's indicator tables:

| Rating | Meaning | Action |
|--------|---------|--------|
| RED | Blocks progress, must resolve now | Immediate action required |
| YELLOW | Controllable risk, plan resolution | Resolve before next stage gate |
| GREEN | Acceptable, proceed | Monitor only |

**Step 4: PRODUCE ASSESSMENT**
Output structure:
1. Assessment scope and stage
2. Dimension-by-dimension scoring with rationale
3. Risk register (if applicable): Risk | Severity | Likelihood | Detectability | RPN | Action | Owner
4. Must-solve-now vs. can-defer classification
5. Recommended action package (prioritized, time-bound)
6. Human review required (by role)

---

## MODE: PLAN — Project and Work Package Planning

Structure a CMC project into manageable work packages.

### PLAN Workflow

**Step 1: IDENTIFY PROJECT ARCHETYPE**
Read `references/project-archetypes.md`. Match the request to one of the 7 best-fit archetypes:
1. Stage-gated CMC readiness
2. Developability and early prioritization
3. Analytical lifecycle and control strategy
4. Technology transfer / site transfer
5. Change control and comparability
6. Module 3 and quality-package structuring
7. CMC training / FAQ / knowledge systems

**Step 2: SELECT DELIVERABLE PATTERN**
Read `references/deliverable-patterns.md`. Choose the output pattern that fits:
- Readiness Pack | Risk Register | Comparability Package | Tech Transfer Package | Module 3 Workplan | Training Pack

**Step 3: BUILD PROJECT PACKAGE**
Output structure:
1. Project framing (archetype, stage, objective)
2. Workstream breakdown
3. Deliverables by phase with evidence owners
4. Review gates and checkpoint logic
5. Key risks and dependencies
6. Open questions
7. Meeting cadence (if relevant)
8. Human review required

**Step 4: MAP ROUTING**
If the plan spans multiple areas, read `references/routing.md` to identify which playbooks and templates apply to each workstream.

---

## MODE: TRAIN — Knowledge Asset Creation

Convert CMC expertise into structured training materials.

### TRAIN Workflow

**Step 1: DEFINE AUDIENCE AND OBJECTIVE**
Who is learning? What should they be able to do after?
Common audiences: new CMC team members, cross-functional partners, CMC leads from other therapeutic areas.

**Step 2: LOAD CONTENT STRUCTURING GUIDE**
Read `playbooks/content-structuring.md` for the 5-module training design framework:
1. Meta (audience, duration, difficulty, objectives)
2. Core Concepts (definition + "one-sentence understanding" + "why it matters")
3. Deep Dive (framework, red-yellow-green indicators, decision matrices)
4. Application (real cases, common mistakes, replicable workflows)
5. Reinforcement (FAQ, self-test questions, "3 sentences to remember")

**Step 3: SELECT SOURCE CONTENT**
Choose the domain playbook(s) to convert into training. Use the 5-module framework to restructure.

**Step 4: PRODUCE TRAINING ASSET**
Output the training material with:
1. Clear learning objectives
2. Progressive structure (concept → framework → application → test)
3. Red-yellow-green indicator tables
4. Real or realistic case studies
5. FAQ bank
6. Quick-reference checklist

---

## Hard Boundaries

Do NOT let this skill:

| Boundary | Reason |
|----------|--------|
| Approve or release batches | QP/QA authority only |
| Sign off on deviations, CAPA, change controls | Requires authorized human role |
| Generate GMP batch records for validated systems | Must go through controlled document process |
| Invent specifications, validation outcomes, stability data | All data must come from user or source documents |
| Declare regulatory compliance as legal fact | Skill provides analysis, not legal opinion |
| Replace SME judgment on clinical or toxicological decisions | Skill supports, does not decide |

If the user asks for any of the above, produce a decision package or review checklist instead.

---

## Regulatory Anchors

Use these as orientation when structuring work. Full list with links in `references/regulatory-anchors.md`.

| Anchor | When to Reference |
|--------|-------------------|
| ICH Q10 | Lifecycle quality system |
| ICH Q12 | Post-approval change management, EC, PACMP |
| ICH Q14 | Analytical procedure lifecycle |
| ICH Q2(R2) | Analytical procedure validation |
| ICH Q5A(R2) | Viral safety evaluation for biotech products |
| ICH Q5E | Comparability for biotech products |
| ICH M4Q | Module 3 structure |
| ICH Q1A(R2) | Stability testing |
| FDA Process Validation Guidance | Stage 1-2-3 lifecycle |
| FDA PQ/CMC | Structured data expectations |

---

## Reference Files

Read only the files needed for the task. Do not load all files simultaneously.

### Playbooks (domain knowledge)
- `playbooks/druggability-assessment.md` — Candidate risk evaluation (4 dimensions, red-yellow-green)
- `playbooks/early-prioritization.md` — IND-enabling module priority (P0-P4 framework)
- `playbooks/risk-comparability.md` — Risk management + comparability 3-step method + PACMP/EC
- `playbooks/compliance-continuum.md` — Full lifecycle compliance (Phase I → Post-approval)
- `playbooks/gmp-qa-principles.md` — GMP/QA fundamentals, deviation/CAPA/OOS lifecycle
- `playbooks/content-structuring.md` — Training content design methodology

### References (operational guidance)
- `references/routing.md` — Signal-to-route mapping (5 routes)
- `references/project-archetypes.md` — 7 best-fit + 2 medium + 2 off-limits archetypes
- `references/deliverable-patterns.md` — 6 reusable output patterns
- `references/gxp-boundaries.md` — Safe-use, caution, off-limits boundaries
- `references/regulatory-anchors.md` — ICH/FDA/NMPA guidance links and reading order
- `references/china-global-cmc-operating-model.md` — China-first/global CMC package design, bilingual terminology, regional deltas
- `references/quality-checklist.md` — CMC document quality checks before output

### Templates (document scaffolds)
- `templates/process-validation-protocol-framework.md` — PPQ protocol (8 sections)
- `templates/module3-workplan-template.md` — Module 3 authoring workplan
- `templates/stage-gate-readiness-template.md` — Stage-gate readiness pack
- `templates/tech-transfer-template.md` — Technology transfer work package
- `templates/change-comparability-template.md` — Change impact + comparability strategy

### Examples (worked outputs)
- `examples/candidate-assessment-example.md` — Full mock output: bispecific candidate assessment
- `examples/process-change-example.md` — Full mock output: chromatography resin change
