---
name: pharmasee-cmc-workbench
description: >
  Unified CMC workbench for Chinese pharmaceutical companies. Orchestrates three modules:
  CMC Forge (execution), CMC Research (knowledge), and Scientific Writer (writing quality).
  Triggers when the user asks about any integrated CMC workflow that spans multiple modules,
  such as: China-first then global CMC roadmap, inbound localization gap assessment,
  Module 3 authoring with writing quality review, tech transfer + comparability strategy,
  FDA/EMA-facing English CMC summary audit, or any request that explicitly mentions
  "PharmaSee", "CMC workbench", "integrated CMC", or asks for a multi-step CMC workflow
  that goes beyond a single module's scope.
  Also triggers when the user's request clearly requires knowledge lookup + CMC execution + writing quality,
  or when the user asks for a workflow rather than a single task.
  Do NOT trigger for requests that fall cleanly within a single module's scope — route those
  to CMC Forge, CMC Research, or Scientific Writer directly.
---

# PharmaSee CMC Workbench

A unified AI-assisted CMC workbench integrating three specialized modules for Chinese pharmaceutical CMC work — from CDE/NMPA filings through global FDA/EMA readiness.

## Module Architecture

```
pharmasee-cmc-workbench/
├── SKILL.md                          ← You are here
├── README.md                         Quick-start guide
├── WORKBENCH.md                      Architecture & design decisions
├── routing.md                        Signal-to-module routing (8 routes)
│
├── skills/
│   ├── cmc-forge/                    Execution engine (DRAFT/ASSESS/PLAN/TRAIN)
│   └── scientific-writer/            Writing quality (WRITE/REVIEW/DIAGNOSE/LEARN)
│
├── knowledge/
│   └── CMC_Research/                 Knowledge base (18 sub-documents + resources)
│
├── workflows/                        5 integrated workflows
├── examples/                         5 integrated scenario examples
└── evals/                            8 cross-module evaluation scenarios
```

## Core Principle: Module Orchestration

This skill does NOT replace its three modules. It **orchestrates** them:

| Module | Role | When Active |
|--------|------|------------|
| **CMC Research** | Knowledge layer | Regulatory lookup, case reference, template retrieval |
| **CMC Forge** | Execution layer | Drafting, assessing, planning CMC deliverables |
| **Scientific Writer** | Quality layer | Writing quality audit, language polish, structural diagnosis |

## Integration Patterns

### Pattern A: Knowledge-Grounded Assessment
```
CMC Research → CMC Forge
```
Look up regulatory requirements, then assess project readiness.

### Pattern B: Draft-then-Review
```
CMC Forge → Scientific Writer
```
Generate CMC draft, then apply 5-pass writing quality audit.

### Pattern C: Full Pipeline
```
CMC Research → CMC Forge → Scientific Writer
```
Knowledge lookup → CMC deliverable → Writing quality polish.

### Pattern D: Standalone Module
Any module operates independently for requests within its scope.

## Routing Logic

When a request arrives, match against these rules (priority order):

1. **Single-module request** → Route to the appropriate module directly. Do NOT activate the workbench orchestrator.
   - CMC drafting/assessment/planning/training → `skills/cmc-forge/SKILL.md`
   - Scientific writing/review/diagnosis → `skills/scientific-writer/SKILL.md`
   - Regulatory knowledge lookup → `knowledge/CMC_Research/` (read relevant sub-document)

2. **Multi-module request** → Activate this workbench skill. Choose the appropriate workflow:

| User Signal | Workflow | Modules |
|-------------|----------|---------|
| Readiness assessment, gap analysis, IND readiness | `workflows/01-cmc-readiness-assessment.md` | CMC Research → CMC Forge (ASSESS) |
| Module 3 drafting, CTD authoring | `workflows/02-module3-authoring.md` | CMC Research → CMC Forge (DRAFT+PLAN) → Scientific Writer |
| China → global strategy, cross-regional roadmap | `workflows/03-china-global-roadmap.md` | CMC Research → CMC Forge (ASSESS+PLAN) |
| Tech transfer, comparability, site change | `workflows/04-tech-transfer-comparability.md` | CMC Research → CMC Forge (DRAFT+ASSESS) |
| Writing quality review, English audit | `workflows/05-writing-quality-review.md` | CMC Forge → Scientific Writer (REVIEW) |

3. **Ambiguous request** → Default to the routing rules in `routing.md`. If still unclear, ask the user to clarify scope.

## Operational Procedure

When the workbench is activated:

### Step 1: Classify the Request
- Determine which modules are needed
- Select the matching workflow from `workflows/`
- If no workflow matches, use the routing rules in `routing.md`

### Step 2: Load Minimum Required Files
- Only load the reference files specified in the workflow
- Do NOT load all module files simultaneously
- Each workflow specifies the minimum required files

### Step 3: Execute the Workflow
- Follow the workflow's step-by-step process
- Hand off between modules at defined points
- Maintain context across module transitions

### Step 4: Apply Quality Gates
- All outputs carry: `⚠️ DRAFT — For controlled review. Not a GMP-controlled document.`
- Include classification level (L1–L4)
- Specify required human reviewers

### Step 5: Deliver
- Present output in the workflow's specified structure
- Include all compliance markers
- List assumptions and unknowns

## Hard Boundaries

This workbench MUST NOT:

1. **Fabricate data** — No invented batch data, specifications, validation results, stability data, or regulatory conclusions
2. **Replace human authority** — All outputs require QA/QP/RA/SME review and approval
3. **Make final regulatory classifications** — Change classifications (Minor/Major/Critical) are advisory only
4. **Authorize GMP actions** — No batch release, deviation closure, or change implementation
5. **Generate final submission documents** — All outputs are drafts for controlled review

## Regulatory Currency Boundary

The bundled CMC Research materials are a local knowledge snapshot, not a live regulatory database. For any current filing strategy, compliance decision, or health-authority response, verify requirements against official NMPA/CDE, ICH, FDA, EMA, and pharmacopoeial sources before relying on the output.

## Company Posture Framework

From `skills/cmc-forge/references/china-global-cmc-operating-model.md`, identify the user's posture:

| Posture | Description |
|---------|-------------|
| China-only | Domestic market focus |
| China-first then global | Start in China, expand outward |
| Global-first with China bridge | Global product, adding China |
| Inbound localization | Overseas product → China manufacturing |
| Outbound licensing | China product → global partner |

Apply the posture when routing China/global CMC requests.

## Bilingual Terminology

When working across Chinese and English CMC contexts:

- Use consistent bilingual terms (see `skills/cmc-forge/CMC_FORGE_PROJECT_NOTE.md`)
- Maintain terminology consistency (Banana Rule) within each output language
- Chinese regulatory terms reference CMC Research sources
- English regulatory terms follow ICH/FDA conventions

## First Move

When the workbench is activated, collect context before executing:

```
Required context (if not provided):
1. Drug type (mAb, BsAb, ADC, CGT, small molecule, etc.)
2. Development stage (pre-IND, Phase I/II/III, BLA, post-approval)
3. Target region(s) (China, US, EU, multi-regional)
4. Company posture (China-only, China-first then global, etc.)
5. Specific task or question
```

If context is partially missing, proceed with reasonable defaults and state assumptions explicitly.

## Reference File Index

### CMC Forge (skills/cmc-forge/)
- `SKILL.md` — Skill definition and trigger rules
- `references/routing.md` — Internal 5-route routing
- `references/project-archetypes.md` — 7 best-fit project types
- `references/deliverable-patterns.md` — 6 reusable output patterns
- `references/china-global-cmc-operating-model.md` — China/global strategy
- `references/gxp-boundaries.md` — Safe-use boundaries
- `references/quality-checklist.md` — 42-point quality checklist
- `references/regulatory-anchors.md` — ICH/FDA/NMPA guidance links
- `templates/` — 5 document scaffolds (PPQ, Module 3, stage-gate, tech transfer, change-comparability)
- `playbooks/` — 6 domain scripts (developability, risk-comparability, compliance-continuum, GMP/QA, early-prioritization, content-structuring)
- `examples/` — 2 worked mock outputs
- `evals/evals.json` — 10 single-module evaluation scenarios

### Scientific Writer (skills/scientific-writer/)
- `SKILL.md` — Skill definition and trigger rules
- `references/section-models.md` — Consolidated section models + language tables
- `references/writing-quality.md` — Grammar, self-editing, common errors
- `extracted-models/` — private extraction notes; exclude from public release packages

### CMC Research (knowledge/CMC_Research/)
- `CMC_COMPREHENSIVE_GUIDE/` — 18 sub-documents (42+ sections)
- `resources/zh-CN/` — Case studies, templates, regulation links
- `COMPLIANCE_FRAMEWORK.md` — Compliance assurance framework
- `SUMMARY.md` — Navigation table of contents

Workflow references such as `declaration_practice/ind_cmc_zh.md` are relative to `knowledge/CMC_Research/CMC_COMPREHENSIVE_GUIDE/` unless another base path is specified.

## Conflict Resolution

When CMC Forge and CMC Research provide conflicting information:
- **CMC Research is authoritative** for regulatory facts and requirements
- **CMC Forge provides frameworks and templates** for structuring work
- When in doubt, cite both and flag for human review

When Scientific Writer suggestions conflict with CMC regulatory terminology:
- **Regulatory terminology is preserved** — do not "improve" standard terms
- Language quality improvements apply to sentence structure and clarity, not domain vocabulary
