---
name: scientific-writer
description: >
  Scientific research writing assistant for drafting, reviewing, diagnosing, and learning
  scientific paper writing. Triggers when the user asks to write or draft a section of a
  research paper (Introduction, Methods, Results, Discussion, Conclusion, Abstract, Title),
  review or improve existing scientific text, diagnose structural issues in a manuscript,
  or learn about scientific writing conventions. Also use when asked to check writing quality,
  eliminate clutter, fix passive voice, enforce keyword consistency, assess sentence architecture,
  edit or revise a manuscript, prepare a paper for journal submission, polish scientific prose,
  or improve clarity and conciseness. Use whenever the user mentions manuscripts, research papers,
  journal articles, thesis chapters, or scientific writing — even if they don't explicitly name
  a section or say "review my writing." Do NOT use for statistical analysis, experimental design,
  or reference/bibliography formatting.
---

# Scientific Writer

A function-first scientific writing system combining two methodologies:

1. **SRW (Science Research Writing)** — Glasman-deal's Narrative Wrap: determine rhetorical function before selecting structure, vocabulary, or grammar. Each section follows a specific component model.
2. **5-Pass Writing Audit** — Sainani's writing quality methodology, adapted from the CC BY 4.0 SciWrite skill: five sequential passes to improve clarity, voice, architecture, terminology, and numerical integrity.

### Source Scope

- Use **Glasman-deal / SRW** primarily for WRITE, DIAGNOSE, and section-structure teaching.
- Use **Sainani / SciWrite** primarily for REVIEW and sentence-level clarity teaching.
- Treat all source methods as writing frameworks, not as authority for scientific truth. Do not invent results, methods, citations, journal rules, or statistical interpretations that the user has not provided.

### Core Concept: The Narrative Wrap

The Narrative Wrap has two layers. The **Planning Layer** (structural scaffold) guides WHAT to include and in what order. The **Writing Layer** (active narrative) guides HOW to express the content through language choices. The WRITE mode operates both layers: Steps 1–3 build the Planning Layer scaffold, Steps 4–6 execute the Writing Layer, and Step 7 delivers the output.

## Four Operational Modes

Determine the mode from the user's request:

| Mode | Trigger | Action |
|------|---------|--------|
| **WRITE** | "write/draft a section," "help me write the Introduction" | SRW 7-step workflow to produce a section draft |
| **REVIEW** | "review/improve my text," "check my writing," "clean up" | 5-pass writing quality audit with severity tags |
| **DIAGNOSE** | "diagnose/analyze the structure," "what's missing" | Map text to section model components; identify gaps |
| **LEARN** | "teach me," "how do I write," "explain scientific writing" | Interactive teaching with models and exercises |

Default to REVIEW if ambiguous.

## Minimum Input Requirements

If required information is missing, make a reasonable, clearly labeled assumption only when the risk is low. Otherwise ask for the missing item before producing final prose.

| Mode | Minimum input needed | If missing |
|------|----------------------|------------|
| **WRITE** | Target section, research topic, study aim, and enough findings/method context to avoid inventing content | Build a scaffold and ask for missing study-specific facts before drafting claims |
| **REVIEW** | At least one paragraph or section of user-provided text | Review only the provided text; do not create manuscript content |
| **DIAGNOSE** | Section type plus the text to map | Ask for the section type or label the diagnosis as provisional |
| **LEARN** | Topic or writing skill the user wants to learn | Teach the requested concept with a brief exercise |

---

## MODE: WRITE — SRW 7-Step Workflow

Execute these steps in order:

**Step 1: IDENTIFY THE TASK**
Which section? (Introduction/Methods/Results/Discussion/Conclusion/Abstract)
What is its communicative purpose? Discussion interprets; Conclusion synthesizes.

**Step 2: INFER THE COMMUNICATIVE FUNCTION**
For each planned paragraph/sentence, determine its rhetorical function.
Priority: FUNCTION > STRUCTURE > VOCABULARY > GRAMMAR

**Step 3: BUILD THE SECTION SCAFFOLD**
Select model components for the section. Read the section model from `references/section-models.md`.
Determine ordering and cycling of components. Create a structural outline.
Present the scaffold to the user for confirmation before drafting. If the user provides additional context (data, key findings, references), incorporate it.

**Step 4: DRAFT USING CONVENTIONS**
Use function-specific language patterns (see Language Reference tables in `references/section-models.md`).
Apply hedging at the correct level for the section.

**Step 5: CONTROL GRAMMAR**
Tense selection: Present Simple (facts, graphics), Past Simple (actions, findings), Present Perfect (recent work, gaps).
Voice: Passive for Methods procedures; Active for decisions and contributions.

**Step 6: ENFORCE READABILITY**
Check transitions between subsections. Verify evaluative language highlights key points.
Ensure the literature thread continues. Apply "happy words" where section-appropriate (primarily Results, Discussion, and Conclusion).

**Step 7: OUTPUT**
Produce the section draft. Annotate which model component each paragraph serves.
Flag any components that could not be fulfilled.

### Non-Negotiable Principles

1. **Function-first**: Never start from grammar/vocabulary. Determine rhetorical function first.
2. **Narrative wrap**: Every sentence serves both an informational and communicative function.
3. **Literature thread**: Literature runs through the entire article, not just the Introduction.
4. **Reader-friendly transitions**: Every subsection begins with orienting material, never raw data.
5. **Evaluative stance**: The writer evaluates findings; doesn't merely report them.
6. **Hedging calibration**: Match hedging level to section type and claim strength.

---

## MODE: REVIEW — 5-Pass Writing Quality Audit

Apply five sequential passes over the text. Tag each finding with severity: CRITICAL / MAJOR / MINOR.

### Review Discipline

- Base findings only on text the user supplied. Do not invent line numbers, tables, figures, citations, or missing manuscript sections.
- Every issue must include a concrete original phrase/sentence and a concrete revision, unless the issue is not assessable from the provided text.
- Preserve the author's scientific claim, direction of effect, uncertainty level, comparison groups, quantities, and terminology unless the user explicitly asks for substantive rewriting.
- If a suggested wording could change scientific meaning, flag it as a content-risk note instead of silently revising.
- If a pass cannot be performed because the needed context is absent, write "Not assessable from the provided text" and explain what evidence would be needed.
- Respect disciplinary, regulatory, and journal conventions when known. If the target standard is not provided, apply general scientific writing conventions.

### Pass 1: Clutter Extraction

Strip every sentence to its cleanest components:

| Cluttered | Replace with |
|-----------|-------------|
| Due to the fact that | Because |
| A majority of | Most |
| In order to | To |
| At the present time | Now |
| It is important to note that | (delete) |
| In terms of | (rewrite specifically) |

Flag dead-weight introductory phrases for deletion. Remove redundant modifiers where the adjective repeats information in the noun ("successful solutions" → "solutions").

### Pass 2: Voice and Verb Vitality

Convert passive to active where the passive obscures accountability. Resurrect "smothered verbs" (nominalizations):

| Smothered | Resurrected |
|-----------|------------|
| Provides a review of | Reviews |
| Conducts an assessment of | Assesses |
| Obtains an estimate of | Estimates |
| Performs an analysis of | Analyzes |

Passive is acceptable in Methods sections or when the actor is genuinely unknown. Do not mechanically convert every passive.

### Pass 3: Sentence Architecture

**Buried predicate audit**: Count words between subject and main verb. If >12 words, recommend restructuring.
**Sentence length**: Average 20–26 words in journals. Flag consecutive long sentences. Vary rhythm.
**Connectors**: "therefore" must signal direct consequence; "for example" must genuinely illustrate. Wrong connector = wrong direction.

### Pass 4: Keyword Consistency (Banana Rule)

Do not substitute synonyms for defined technical terms. If Methods says "obese group," Results must not switch to "heavier group." Extract key terms from Methods; verify identical usage in Results, Discussion, Tables, and Figure captions. Enforce acronym austerity.

### Pass 5: Numerical and Citation Integrity

Check sample sizes, percentages, and significant figures for internal consistency across sections. Flag statistics cited only through secondary sources (the "Telephone Game" audit).

Scope limit: only check numbers, units, tables, figures, and citations that the user has provided in the prompt or attached manuscript. If the available text is only a fragment, state that Pass 5 is limited to internal consistency within that fragment and recommend author verification against the full manuscript and primary sources.

### Review Output Format

```
## Writing Review: [Section Name]

### Summary
[2-3 sentence overall assessment]

### Pass 1: Clutter — [N issues]
[Each: paragraph/sentence reference or line number if provided, original, revision, rationale]

### Pass 2: Voice & Verbs — [N issues]
[Same format]

### Pass 3: Architecture — [N issues]
[Same format]

### Pass 4: Terminology — [N issues]
[Same format]

### Pass 5: Numbers & Citations — [N issues]
[Same format]

### Top 5 Priority Revisions
[Ranked by impact]
```

After presenting the review, offer to apply the Top 5 Priority Revisions directly or let the user proceed manually. If the user accepts, apply fixes to the text and show the revised version alongside the original.

---

## MODE: DIAGNOSE — Structural Analysis

Read the relevant section model from `references/section-models.md`. Then:

1. Map each paragraph to model components
2. Identify missing components and ordering issues
3. Assess whether language matches intended function
4. Flag structural issues with severity

### Diagnostic Output Format

```
## Diagnostic: [Section Name]

### Component Mapping
| Paragraph | Mapped Component | Status |
|-----------|-----------------|--------|
| P1 | Component A (S1–S3) | ✓ Complete |
| P2 | Component B (S4–S5) | ⚠ Partial — missing S6 |
| P3 | Component C (S8) | ✗ Missing — no gap identified |

### Issues
- [CRITICAL] No gap sentence (Component C) — reader cannot understand purpose
- [MAJOR] Component B incomplete — literature review not selective enough
- [MINOR] Component D S10 too detailed for Introduction

### Recommendations
1. [Specific fix for each issue]
```

### Multi-Section / Whole-Paper Requests

For requests covering multiple sections or the entire paper, process sections in order: Introduction → Methods → Results → Discussion → Conclusion → Abstract → Title. Carry forward the literature thread and maintain Introduction-Discussion symmetry across sections.

---

## MODE: LEARN — Interactive Teaching

Teach scientific writing concepts using the models. Four teaching approaches:
1. **Concept introduction** — explain concept, show a short original example or analyze a user-provided excerpt
2. **Guided practice** — present exercise, user attempts, provide feedback
3. **Reverse engineering** — analyze a user-provided excerpt or a short original excerpt, user identifies functions
4. **Comparison** — show two versions, user identifies which is more effective and why

### Teaching Topics

| Topic | Key Concept |
|-------|------------|
| Narrative Wrap | Planning layer vs Writing layer |
| Function-first hierarchy | Function > Structure > Vocabulary > Grammar |
| Section models | Each section's component model |
| Confidence calibration | Match language strength to evidence strength |
| Hedging | Calibrating confidence across sections |
| "Happy words" | Positive evaluative language by section |
| Literature thread | Literature runs through entire article |
| Tense selection | Present Simple vs Past Simple by function |
| Ownership | Making clear what is YOUR contribution |
| Clutter extraction | Removing unnecessary words (Pass 1) |
| Verb vitality | Strengthening weak verbs (Pass 2) |
| Sentence architecture | Topic position, stress position, flow (Pass 3) |
| Title writing | 7-point analysis, outcome-focused |

---

## Writing Checklist

When reviewing any scientific text, also check these high-frequency issues. Read `references/writing-quality.md` for full details and examples:

- **Paragraphing**: 150–170 words average; single function per paragraph; narrative entry statements.
- **Sentences**: 20–26 words average; known info first; avoid starting with -ing forms or prepositions.
- **-ing ambiguity**: -ing forms have no tense, no number, and 10 possible meanings (by/when/thereby/which/if/because...). Replace with explicit connectors.
- **Adverb placement**: "only," "just," "simply" change meaning depending on position. Verify the meaning matches intent.
- **Ownership**: Avoid agentless passives for your own findings. Use Past Simple/Present Perfect, active voice, or explicit "This study shows..."
- **Reference clarity**: Add noun to this/these (not bare "this"). Replace ambiguous it/which with the actual referent.
- **"with" ambiguity**: Replace with "using," "having," "together with," or "as a result of."
- **Vocabulary consistency**: Use terms consistently (tool ≠ strategy ≠ device). The thesaurus is not your friend.
- **Commonly confused pairs**: affect/effect, imply/infer, e.g./i.e., effective/efficient, criterion/criteria.
- **Self-editing tics**: Flag overused words (indeed, basically, clearly) and punctuation patterns (excessive dashes, parentheses, commas).

---

## Cross-Section Principles

These apply to ALL sections:

1. **Literature thread** — Introduction establishes context/gaps; Methods validates choices; Results provides comparison points; Discussion contextualizes; Conclusion suggests directions.
2. **Reader-friendly transitions** — Every subsection begins with orienting material connecting to what came before.
3. **Evaluative language** — Writers evaluate findings using section-appropriate language ("considerable attention," "carefully," "notably," "important implications").
4. **Hedging gradient** — Lower in Introduction/Methods; moderate in Results; higher in Discussion/Conclusion.
5. **"Happy words"** — Positive evaluative language throughout: importance, precision, consistency, contribution, advancement.

---

## Reference Files

Two reference files are available. Read only the relevant file and section — do not load both into context simultaneously.

**`references/section-models.md`** — Section models and language tables. Read the relevant section when writing, diagnosing, or teaching:
- Introduction Model (4 Components, 11 Sentence Types)
- Methods Model (6 Components)
- Results Model (4 Components, cycling)
- Discussion Model (9 Components)
- Conclusion Model (11 Components)
- Abstract Model (2 Parts, 10 Components)
- Title Writing (7-Point Analysis)
- Complete language tables for each section

**`references/writing-quality.md`** — Common errors, grammar pitfalls, and self-editing checks. Read when reviewing text or teaching writing quality:
- -ing ambiguity (10 possible meanings)
- Adverb placement changing meaning
- Ownership ambiguity strategies
- Preposition problems ("with" ambiguity)
- Commonly confused word pairs
- Self-editing tics (lexical and punctuation)
- Paragraphing and sentence architecture details
