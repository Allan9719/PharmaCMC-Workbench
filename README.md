# PharmaCMC Workbench

> Unified AI-assisted CMC workbench for China pharmaceutical companies — covering CDE/NMPA filings, global FDA/EMA readiness, Module 3 authoring, tech transfer, comparability, post-approval changes, scientific writing, and English quality audit.

---

## What Is This?

**PharmaCMC Workbench** integrates three specialized modules into one coherent environment:

| Module | Role | Source Project |
|--------|------|---------------|
| **CMC Forge** | Execution engine — draft, assess, plan, train | `cmc-forge` |
| **CMC Research** | Knowledge base — regulations, cases, templates | `CMC_Research` |
| **Scientific Writer** | Writing quality — SRW methodology + 5-pass audit | `scientific-writer-skill` |

The workbench orchestrates these modules through **5 integrated workflows** covering the most common CMC scenarios Chinese biopharma teams face.

---

## Quick Start

### Prerequisites

- [Claude Code](https://claude.ai/code) installed
- This workbench is self-contained — all three modules are included

### Usage Patterns

**Pattern 1: Use a workflow directly**

```
/workflows/01-cmc-readiness-assessment.md
```

Open a workflow file, follow the step-by-step instructions. Each workflow specifies which modules to invoke and in what order.

**Pattern 2: Invoke a module directly**

```
# CMC drafting, assessment, planning
→ triggers CMC Forge skill

# Scientific writing review
→ triggers Scientific Writer skill

# Knowledge lookup
→ consult CMC Research knowledge base
```

**Pattern 3: Integrated scenario**

```
# Example: China-first then global CMC roadmap
→ CMC Research: regulatory framework lookup
→ CMC Forge: ASSESS mode gap analysis
→ CMC Forge: PLAN mode evidence roadmap
→ Scientific Writer: REVIEW mode on English summary
```

---

## Directory Structure

```
pharmasee-cmc-workbench/
├── README.md                    # This file
├── CLAUDE.md                    # Project-level instructions
├── SKILL.md                     # Skill trigger and orchestration
├── WORKBENCH.md                 # Architecture and design decisions
├── routing.md                   # Signal-to-module routing guide
├── .gitignore                   # Git ignore rules
│
├── skills/                      # Execution modules (full copies)
│   ├── cmc-forge/               # CMC Forge skill (25 files)
│   └── scientific-writer/       # Scientific Writer skill (14 files)
│
├── knowledge/                   # Knowledge base (full copy)
│   └── CMC_Research/            # CMC Research knowledge base (51 files)
│
├── workflows/                   # 5 integrated workflows
│   ├── 01-cmc-readiness-assessment.md
│   ├── 02-module3-authoring.md
│   ├── 03-china-global-roadmap.md
│   ├── 04-tech-transfer-comparability.md
│   └── 05-writing-quality-review.md
│
├── examples/                    # 5 integrated scenario examples
│   ├── 01-china-biotech-global-roadmap.md
│   ├── 02-inbound-localization-gap.md
│   ├── 03-module3-authoring-workplan.md
│   ├── 04-tech-transfer-comparability.md
│   └── 05-fda-english-cmc-audit.md
│
└── evals/                       # Cross-module evaluation scenarios
    └── integrated-workbench-evals.json
```

---

## Integrated Workflows

| # | Workflow | Primary Module | Supporting Modules |
|---|----------|---------------|-------------------|
| 1 | CMC Readiness Assessment | CMC Forge (ASSESS) | CMC Research |
| 2 | Module 3 Authoring | CMC Forge (DRAFT+PLAN) | CMC Research, Scientific Writer |
| 3 | China → Global Roadmap | CMC Forge (ASSESS+PLAN) | CMC Research |
| 4 | Tech Transfer + Comparability | CMC Forge (DRAFT+ASSESS) | CMC Research |
| 5 | Writing Quality Review | Scientific Writer (REVIEW) | CMC Forge |

---

## Compliance Red Lines

This workbench produces **drafts for controlled review only**. It must NOT:

- Replace QA/QP/RA/SME final judgment on any regulated output
- Fabricate batch data, specifications, validation results, or regulatory conclusions
- Make final regulatory classification decisions (Minor/Major/Critical changes)
- Authorize batch release, deviation closure, or change implementation
- Generate GMP-controlled documents without human review and approval

All outputs carry the header: `⚠️ DRAFT — For controlled review. Not a GMP-controlled document.`

---

## Module Details

### CMC Forge (Execution Engine)

- **4 Modes**: DRAFT, ASSESS, PLAN, TRAIN
- **5 Templates**: PPQ protocol, Module 3 workplan, stage-gate readiness, tech transfer, change-comparability
- **6 Playbooks**: Developability, early prioritization, risk-comparability, compliance continuum, GMP/QA, content structuring
- **42-Point Quality Checklist**: Content, terminology, numerical, regulatory, risk, hygiene
- **Bilingual**: Chinese-primary with full English CMC terminology support

### CMC Research (Knowledge Base)

- **18 Sub-documents** covering 42+ sections across small molecules, biologics, ATMP, mRNA, ADC, oligonucleotides
- **China-specific**: NMPA/CDE framework, Chinese Pharmacopoeia 2025, MAH system, DMF
- **3 Case Studies**: Nitrosamine impurity, biosimilar similarity, ADC DAR control
- **3 Practical Templates**: NDA checklist, MAH quality agreement, variation filing form
- **Compliance Infrastructure**: Triple verification gates, update SOP, regulatory tracking

> **Regulatory snapshot note:** CMC Research is a bundled knowledge snapshot. Before using any output for regulated decision-making, verify current requirements against official NMPA/CDE, ICH, FDA, EMA, and pharmacopoeial sources.

For public publishing, see `PUBLIC_RELEASE.md`. Public packages should exclude private extraction notes and local PDF source files.

### Scientific Writer (Writing Quality)

- **4 Modes**: WRITE, REVIEW, DIAGNOSE, LEARN
- **SRW Methodology**: 7-step Narrative Wrap approach for structured scientific writing
- **5-Pass Audit**: Clutter, voice/verb vitality, sentence architecture, keyword consistency, numerical/citation integrity
- **Section Models**: Introduction, Methods, Results, Discussion, Conclusion, Abstract, Title
- **Language Tables**: Reporting verbs, hedging devices, "happy words", tense guides, confidence matrices

---

## Version

**PharmaCMC Workbench v1.0** — April 2026

| Component | Version |
|-----------|---------|
| CMC Forge | v2.1 |
| CMC Research | v2.1 |
| Scientific Writer | v1.0 |

---

## License

This project is licensed under **Apache License 2.0**. The Scientific Writer module's 5-pass writing audit is additionally covered by **CC BY 4.0** (derived from [SciWrite](https://github.com/labarba/sciwrite)).

- See [LICENSE](LICENSE) for the full Apache 2.0 text
- See [NOTICE](NOTICE) for third-party attribution and disclaimer
- See [ATTRIBUTION.md](ATTRIBUTION.md) for module-level attribution details
- See [PUBLIC_RELEASE.md](PUBLIC_RELEASE.md) for release package preparation guide
