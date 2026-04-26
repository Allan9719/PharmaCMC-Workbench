# Workflow 05: Writing Quality Review

> **Modules:** Scientific Writer (REVIEW/DIAGNOSE) + CMC Forge (DRAFT)
> **Typical duration:** 20–45 minutes per document section
> **Output level:** L2 (team discussion draft)

---

## When to Use

- FDA-facing CMC summary English quality review
- EMA-facing English dossier sections
- CMC rationale writing for Module 3
- Scientific manuscript sections (Introduction through Conclusion)
- Regulatory response letters in English
- Any English-language CMC document requiring quality assurance

---

## Step-by-Step Process

### Step 1: Identify Document Type and Audience

Determine the document type to select the appropriate review standard:

| Document Type | Primary Audience | Quality Standard |
|--------------|-----------------|-----------------|
| FDA CMC summary (QS/CMC) | FDA reviewers | Clear, concise, regulatory English |
| EMA Module 3 English sections | EMA assessors | EU regulatory English conventions |
| CMC rationale (change justification) | Multi-regional RA | Technical + regulatory language |
| Scientific manuscript | Peer reviewers | Academic scientific English |
| Regulatory response (deficiency letter reply) | CDE/FDA/EMA | Precise, evidence-based language |

### Step 2: Structural Diagnosis (if needed)

If the document structure is unclear or problematic:

Invoke **Scientific Writer DIAGNOSE mode**:
- Map text paragraphs to section model components
- Identify missing rhetorical elements
- Flag structural issues with severity ratings
- Compare against the appropriate section model

**Load:** `skills/scientific-writer/references/section-models.md` (relevant section model)

### Step 3: 5-Pass Writing Quality Audit

Invoke **Scientific Writer REVIEW mode**:

**Pass 1 — Clutter Extraction:**
- Identify and remove redundancy, wordiness, unnecessary qualifiers
- Flag sentences that can be shortened by 30%+ without losing meaning

**Pass 2 — Voice/Verb Vitality:**
- Check passive/active voice balance (regulatory docs tolerate more passive)
- Identify weak verbs (is, are, was, were, has, have) that could be strengthened
- Verify verb tense consistency within sections

**Pass 3 — Sentence Architecture:**
- Check sentence length (target 20–26 words average for scientific prose)
- Identify buried predicates (>12 words between subject and verb)
- Verify paragraph function (one function per paragraph, 150–170 words average)

**Pass 4 — Keyword Consistency (Banana Rule):**
- Verify the same term is used consistently for the same concept throughout
- Flag synonym variation (e.g., "batch" vs. "lot", "drug product" vs. "formulation")
- Cross-check terminology against CMC Forge quality checklist

**Pass 5 — Numerical/Citation Integrity:**
- Verify numbers against user-provided source data only
- Check cross-reference integrity within the provided text
- Verify citation format consistency when citations are provided
- Flag claims whose evidence is absent from the provided material

**Load:** `skills/scientific-writer/references/writing-quality.md`

### Step 4: CMC Content Coherence Check

Optionally, cross-reference with CMC Forge quality checklist for CMC-specific issues:

**Load:** `skills/cmc-forge/references/quality-checklist.md`

Check:
- Content completeness (11 items)
- Terminology & Banana Rule (8 items)
- Numerical integrity (8 items)
- Regulatory compliance (6 items)
- Risk & evidence (6 items)
- Document hygiene (5 items)

### Step 5: Targeted Revision (if requested)

If revision is needed:

Invoke **Scientific Writer WRITE mode** for specific sections:
- Apply SRW 7-step workflow to restructure problematic sections
- Use section model conventions for rhetorical function
- Apply appropriate language patterns from reference tables

### Step 6: Deliver

Output structure:
```
⚠️ DRAFT — For controlled review. Not a GMP-controlled document.
Module: Scientific Writer (REVIEW) + CMC Forge (Quality Checklist)
Classification: L2
Human review required: Yes — RA Lead + Native English Speaker

[Writing Quality Audit Report]
1. Overall quality score and summary
2. Pass-by-pass findings (CRITICAL/MAJOR/MINOR)
3. Top 5 Priority Revisions (ranked by impact)
4. Specific paragraph/sentence-level suggestions, or line-by-line suggestions if line numbers are provided
5. Structural recommendations (if applicable)
6. Terminology consistency report (Banana Rule violations)

[Or: Revised Section Draft]
- Clean revised text with tracked changes noted
- Summary of changes made
- Remaining open items for author review
```

---

## Quality Checkpoints

- [ ] All 5 passes completed and documented
- [ ] Severity ratings applied consistently (CRITICAL/MAJOR/MINOR)
- [ ] Banana Rule checked across the entire document
- [ ] No changes to technical content or data — only language quality
- [ ] Regulatory terminology preserved (not "improved" to non-standard terms)
- [ ] Revision suggestions are actionable and specific
