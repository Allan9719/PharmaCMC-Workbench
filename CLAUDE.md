# PharmaSee CMC Workbench

Unified AI-assisted CMC workbench for Chinese pharmaceutical CMC work.

## Quick Orientation

- **SKILL.md** — Operational instructions (trigger rules, routing, module orchestration)
- **WORKBENCH.md** — Architecture design and module responsibilities
- **routing.md** — Signal-to-module routing (8 routes)

## Module Locations

- `skills/cmc-forge/` — Execution engine (DRAFT/ASSESS/PLAN/TRAIN)
- `skills/scientific-writer/` — Writing quality (WRITE/REVIEW/DIAGNOSE/LEARN)
- `knowledge/CMC_Research/` — Knowledge base (regulations, cases, templates)

## Workflows

Five integrated workflows in `workflows/` cover the most common scenarios:
1. CMC Readiness Assessment
2. Module 3 Authoring
3. China → Global Roadmap
4. Tech Transfer + Comparability
5. Writing Quality Review

## Hard Boundaries

- All outputs are **drafts for controlled review** — never final GMP documents
- Never fabricate batch data, specifications, validation results, or regulatory conclusions
- Never replace QA/QP/RA/SME final judgment
- Every output carries `⚠️ DRAFT` header with classification level and required reviewers
