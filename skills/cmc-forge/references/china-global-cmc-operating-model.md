# China + Global CMC Operating Model

Use this file when the requester is a Chinese pharmaceutical company, when the package supports NMPA/CDE, or when the product is being prepared for internationalization.

## Core Rule

Build one scientifically coherent CMC story, then express regional deltas explicitly. Avoid writing China, US, and EU packages as unrelated narratives.

Output should separate:
- **Global core package**: product understanding, process description, control strategy, validation strategy, stability strategy, comparability logic, and evidence map.
- **China / NMPA-CDE delta**: China registration category, CDE communication points, domestic site or imported product pathway, China pharmacopoeia considerations, Chinese-language controlled terminology.
- **US / FDA delta**: IND/BLA/NDA context, supplement or annual-report assumptions, FDA process validation lifecycle, PQ/CMC structured data readiness where relevant.
- **EU / EMA delta**: MAA or variation context, QP and batch certification interfaces, EU variation classification assumptions, ASMF/PMF where applicable.
- **Other market delta**: PMDA/TGA/Health Canada or partner-specific requirements, only if requested or clearly relevant.

## Company Postures

| Posture | Typical Need | Skill Behavior |
|---------|--------------|----------------|
| China-only | CDE/NMPA filing or domestic change | Use Chinese regulatory terms and NMPA/CDE anchors first; keep ICH as scientific backbone. |
| China-first then global | Domestic IND/NDA first, later US/EU | Create a China-ready package that does not block later global reuse; track evidence gaps against FDA/EMA expectations. |
| Global-first with China bridge | US/EU package exists, China filing follows | Map existing global CTD content to CDE expectations; identify translation, local testing, site, and pharmacopeial deltas. |
| Inbound localization | Overseas marketed product moves to China manufacturing or China supply | Focus on transfer-to-domestic-production evidence, comparability, site readiness, and change-registration path assumptions. |
| Outbound licensing or BD | Chinese asset reviewed by global partner | Produce an English-facing diligence package plus source-evidence tracker and risk register. |

## Bilingual Terminology Pattern

When writing for Chinese teams that interact with global partners, define terms once using:

`中文术语 (English regulatory term; abbreviation)`

Examples:
- 关键质量属性 (Critical Quality Attribute; CQA)
- 关键工艺参数 (Critical Process Parameter; CPP)
- 正常操作范围 (Normal Operating Range; NOR)
- 已证明可接受范围 (Proven Acceptable Range; PAR)
- 可比性研究 (comparability exercise)
- 既定条件 (Established Conditions; ECs)
- 批准后变更管理方案 (Post-Approval Change Management Protocol; PACMP)
- 工艺性能确认 (Process Performance Qualification; PPQ)
- 持续工艺确认 (Continued Process Verification; CPV)

## Regional Delta Checklist

Before output, answer or flag as unknown:

| Question | Why It Matters |
|----------|----------------|
| Which agency is the primary audience: CDE, FDA, EMA, or partner due diligence? | Determines depth, terminology, and evidence burden. |
| Is the product domestic, imported, or transferring overseas manufacture into China? | Changes site and dossier expectations. |
| Is this clinical-stage, registration-stage, or post-approval? | Controls whether evidence is fit-for-phase or must support commercial commitments. |
| Are China Pharmacopoeia, USP, EP, or JP methods/specifications relevant? | Prevents silent method/specification mismatch. |
| Are there multi-site or CDMO responsibilities? | Requires quality agreement, data ownership, and tech-transfer governance. |
| Will controlled records or source data cross legal entities or borders? | Requires data integrity, confidentiality, and system-of-record boundaries. |
| Does the package need Chinese, English, or bilingual output? | Prevents inconsistent terminology across translated documents. |

## China-Focused Evidence Hotspots

For NMPA/CDE-oriented work, pay special attention to:
- source-to-CTD traceability for Module 3 sections
- local site responsibilities and MAH responsibilities
- imported-to-domestic manufacturing transfer evidence, when relevant
- post-approval change classification assumptions and supporting research data
- biological product comparability for process/site/material changes
- pharmacopeial method alignment and justification for non-compendial methods
- Chinese terminology consistency across CTD, internal reports, and translated appendices

## Internationalization Hotspots

For Chinese companies going global, explicitly assess:
- whether early CMC data can support FDA/EMA interactions, not only CDE review
- whether method qualification plans are upgradeable to ICH Q2(R2) validation
- whether Q14 analytical procedure development rationale is documented
- whether Q5A(R2) viral safety expectations are covered for biologics and CGT-relevant materials
- whether control strategy is described as linked CQA-CPP-IPC-specification logic
- whether PPQ/CPV plans are lifecycle-based and statistically defensible
- whether the English dossier reads as source-backed regulatory writing, not a literal translation

## Output Pattern

For China/global tasks, add this section to the normal output:

1. **Target Region and Use**
2. **Global Core CMC Package**
3. **China / CDE-NMPA Delta**
4. **US/EU/Other Delta** if applicable
5. **Bilingual Terminology Table** if the output is bilingual or partner-facing
6. **RA Confirmation Items**
7. **Evidence Gaps Blocking Finalization**

## Hard Boundary

Do not make final legal or regulatory classification claims. Say "preliminary regulatory-path assumption" and require RA confirmation for agency-specific filing categories, variation types, and authority commitments.
