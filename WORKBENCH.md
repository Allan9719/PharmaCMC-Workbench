# WORKBENCH.md — Architecture & Design Decisions

## 1. Design Philosophy

**Modular orchestration, not monolithic integration.**

The workbench does not merge three projects into one skill. Instead, it defines:

1. **Clear module boundaries** — each project retains its identity and independent git history
2. **Routing logic** — which module handles which signal
3. **Integrated workflows** — multi-module orchestration for complex scenarios
4. **Quality gates** — compliance checkpoints at every handoff

## 2. Module Responsibilities

### CMC Research — Knowledge Layer

| Aspect | Description |
|--------|-------------|
| **Role** | Authoritative CMC knowledge base for Chinese pharma |
| **Input** | User queries about regulations, guidelines, cases, templates |
| **Output** | Factual references, regulatory context, case analogies |
| **Scope** | China NMPA/CDE + global ICH/FDA/EMA frameworks |
| **Does NOT** | Generate drafts, make assessments, or produce deliverables |

### CMC Forge — Execution Layer

| Aspect | Description |
|--------|-------------|
| **Role** | Primary CMC work engine for drafting, assessing, planning, training |
| **Input** | Project context (drug type, stage, region, company posture) + user task |
| **Output** | Structured deliverables (protocols, workplans, assessments, risk registers) |
| **Scope** | Full CMC lifecycle from pre-IND through post-approval |
| **Does NOT** | Produce final GMP-controlled documents or replace SME judgment |

### Scientific Writer — Quality Layer

| Aspect | Description |
|--------|-------------|
| **Role** | Scientific writing quality assurance and language polishing |
| **Input** | Draft text (CMC rationale, FDA-facing summary, manuscript section) |
| **Output** | Revised text with tracked changes, audit report, diagnostic analysis |
| **Scope** | Structure, rhetoric, grammar, clarity, regulatory English quality |
| **Does NOT** | Assess CMC technical content, make regulatory strategy decisions |

## 3. Data Flow

```
User Request
     │
     ▼
┌─────────────┐     Knowledge lookup     ┌──────────────┐
│  CMC Forge  │ ◄─────────────────────── │ CMC Research  │
│  (Executor) │                          │ (Knowledge)   │
└──────┬──────┘                          └──────────────┘
       │
       │ Draft / Assessment / Plan
       ▼
┌──────────────────┐
│ Scientific Writer │  ← Applied when output is English-facing
│ (Quality Gate)    │     or requires publication-quality language
└──────────────────┘
       │
       ▼
   Final Deliverable
   (Draft for controlled review)
```

## 4. Routing Rules

See [routing.md](routing.md) for the complete signal-to-module mapping.

**Priority order for ambiguous requests:**

1. If the request involves drafting, assessing, or planning CMC deliverables → **CMC Forge**
2. If the request involves regulatory knowledge lookup → **CMC Research**
3. If the request involves writing quality, language polishing, or structural diagnosis → **Scientific Writer**
4. If the request spans multiple areas → route via the appropriate integrated workflow

## 5. Integration Patterns

### Pattern A: Knowledge-Grounded Assessment

```
CMC Research → CMC Forge
```
Look up regulatory requirements first, then assess project readiness against them.

### Pattern B: Draft-then-Review

```
CMC Forge → Scientific Writer
```
Generate a CMC draft, then apply 5-pass writing quality audit.

### Pattern C: Full Pipeline

```
CMC Research → CMC Forge → Scientific Writer
```
Knowledge lookup → CMC deliverable → Writing quality polish.

### Pattern D: Standalone Module

Any module can operate independently for requests within its scope.

## 6. Quality Architecture

### Output Classification

| Level | Label | Review Requirement |
|-------|-------|--------------------|
| **L1** | Internal reference | Self-review |
| **L2** | Team discussion draft | Peer review |
| **L3** | Cross-functional review draft | SME + RA review |
| **L4** | Submission-ready draft | QA + QP approval |

All workbench outputs start at L1-L2. No output is L4 without human sign-off.

### Mandatory Compliance Markers

Every deliverable output includes:

```
⚠️ DRAFT — For controlled review. Not a GMP-controlled document.
Module: [CMC Forge / Scientific Writer]
Classification: [L1/L2/L3]
Human review required: [Yes — specify reviewer type]
```

### Regulatory Currency

The bundled CMC Research module is a local snapshot. Treat it as a working reference, not a live regulatory database. Current filing strategy and compliance decisions require verification against official agency and pharmacopoeial sources.

## 7. File Integration Strategy

The workbench contains **full copies** of the three source modules:

```
skills/cmc-forge/           ← copied from E:\Pythonprojects\cmc-forge
skills/scientific-writer/   ← copied from E:\Pythonprojects\scientific-writer-skill
knowledge/CMC_Research/     ← copied from E:\Pythonprojects\CMC_Research
```

**Source projects remain unchanged.** To update a module, re-copy from the source and re-apply any workbench-specific overrides (module READMEs).

**Synchronization note:**
- Source projects: `E:\Pythonprojects\cmc-forge`, `E:\Pythonprojects\CMC_Research`, `E:\Pythonprojects\scientific-writer-skill`
- Workbench copies are snapshots — update periodically from source
- Module-level READMEs in the workbench differ from upstream (workbench-specific)
- Public release packages should exclude private extraction notes and local PDF source files; see `PUBLIC_RELEASE.md`.

## 8. Versioning

| Component | Version | Last Updated |
|-----------|---------|-------------|
| CMC Forge | v2.1 | April 2026 |
| CMC Research | v2.1 | April 2026 |
| Scientific Writer | v1.0 | 2026 |
| Workbench Orchestration | v1.0 | April 2026 |

Version mismatches are tolerated. Each module is self-consistent.
