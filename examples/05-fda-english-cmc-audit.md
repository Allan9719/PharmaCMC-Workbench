# Example 05: FDA-Facing English CMC Summary Writing Audit

> **Integrated scenario:** A Chinese biotech company needs to prepare an English CMC summary for FDA IND submission, and wants both CMC content drafting and English writing quality review.
> **Modules invoked:** CMC Forge (DRAFT) + Scientific Writer (REVIEW + WRITE)
> **Workflow:** [05-writing-quality-review.md](../workflows/05-writing-quality-review.md)

---

## Scenario Background

**Company:** SinoBio Innovations (fictional)
**Product:** SB-300, anti-IL-6R IgG1 mAb (biosimilar to tocilizumab)
**Indication:** Rheumatoid arthritis
**Current status:**
- Phase I completed in China
- Analytical similarity to reference product established
- Planning US FDA 351(k) BLA submission
- Internal team has strong CMC expertise but limited English regulatory writing experience
- CMC content available in Chinese; needs English compilation and quality review

**Challenge:** The CMC team can draft technically accurate content but struggles with FDA-style regulatory English — sentence structure, hedging calibration, terminology consistency, and the specific rhetorical patterns expected by FDA reviewers.

---

## Step 1: Content Drafting (CMC Forge DRAFT)

The CMC team provides Chinese-language content. CMC Forge DRAFT mode structures the English CMC summary:

### FDA QS/CMC Summary Structure (simplified)

```
1. Introduction
   - Product description (SB-300, anti-IL-6R IgG1)
   - Biosimilar approach (351(k) pathway)
   - Reference product (tocilizumab, US-licensed Actemra)

2. Manufacturing Process
   - Cell line development
   - Upstream process (CHO-K1, fed-batch, 500L single-use)
   - Downstream process (Protein A → CEX → AEX → VRF)
   - Formulation and fill

3. Characterization and Comparability
   - Analytical similarity assessment
   - Structural characterization (primary, higher-order, PTMs)
   - Functional characterization (binding, bioactivity, Fc function)

4. Control Strategy
   - Drug substance specifications
   - Drug product specifications
   - In-process controls
   - Raw material controls

5. Stability
   - Stability protocol
   - Available data
   - Proposed shelf life

6. Container Closure System
```

CMC Forge populates the structure with provided data, flagging:
- Data placeholders where numbers are needed
- Sections requiring SME review
- Cross-references to Module 3 sections

---

## Step 2: Writing Quality Audit (Scientific Writer REVIEW)

### Original Text Example (before audit):

> "The characterization studies was performed to demonstrate that SB-300 is highly similar to the reference product. The primary structure analysis using peptide mapping and mass spectrometry showed identical sequence. The higher order structure was confirmed by CD spectroscopy, DSC, and HDX-MS which all indicated comparable secondary and tertiary structure. Glycosylation profiles were found to be slightly different but within the range of the reference product lots that was tested. The binding affinity to IL-6R was evaluated and demonstrated to be comparable. Potency was assessed using cell-based assay and showed equivalent biological activity."

### 5-Pass Audit Results

**Pass 1 — Clutter Extraction:**
- "was performed to demonstrate that" → "demonstrated that" (3 words saved)
- "which all indicated" → "indicating" (2 words saved)
- "was evaluated and demonstrated to be" → "demonstrated" (5 words saved)
- "was assessed using cell-based assay and showed" → "Cell-based potency assays showed" (3 words saved)

**Pass 2 — Voice/Verb Vitality:**
- "studies was performed" → grammar error (subject-verb agreement)
- "was found to be slightly different" → passive, weak verb → "differed slightly"
- "was evaluated and demonstrated" → double passive → "binding studies demonstrated"
- "was assessed using...and showed" → passive → "Cell-based potency assays showed"

**Pass 3 — Sentence Architecture:**
- Sentence 3 is 38 words (exceeds 26-word target) → split into two sentences
- Sentence 6 is 33 words → split
- "using peptide mapping and mass spectrometry" creates a 15-word predicate gap in sentence 2

**Pass 4 — Keyword Consistency (Banana Rule):**
- "reference product" used 2x, "reference product lots" used 1x → standardize to "reference product"
- "comparable" used 3x, "highly similar" used 1x → standardize: "highly similar" for overall conclusion, "comparable" for individual attributes
- "cell-based assay" vs. "cell-based potency assay" → standardize to "cell-based potency assay"

**Pass 5 — Numerical/Citation Integrity:**
- No numerical data provided in sample — flag as gap
- No cross-references to Module 3 sections — flag as gap
- "slightly different" lacks quantitative context — flag for data inclusion

### Revised Text (after audit):

> "Characterization studies demonstrated that SB-300 is highly similar to the reference product. Peptide mapping and mass spectrometry confirmed an identical primary amino acid sequence. Higher-order structure analysis by circular dichroism, differential scanning calorimetry, and hydrogen-deuterium exchange mass spectrometry indicated comparable secondary and tertiary structures.
>
> Glycosylation profiles differed slightly from the reference product [data: see Module 3.2.S.3, Table X] but fell within the established quality range of the reference product lots analyzed (n=10). Binding affinity to IL-6R was highly similar [KD: X.X nM vs. X.X nM for reference]. Cell-based potency assays demonstrated equivalent biological activity [relative potency: XX.X%, 95% CI: XX–XX%]."

### Top 5 Priority Revisions

1. **CRITICAL:** Fix subject-verb agreement ("studies was" → "studies demonstrated")
2. **CRITICAL:** Add quantitative data to all comparative statements
3. **MAJOR:** Reduce sentence length — split sentences exceeding 26 words
4. **MAJOR:** Standardize terminology per Banana Rule (comparable/highly similar)
5. **MAJOR:** Add Module 3 cross-references for all data claims

---

## Step 3: Language Pattern Recommendations

From `skills/scientific-writer/references/section-models.md`:

### Hedging Calibration for FDA CMC Summary

| Section | Recommended Hedging Level | Examples |
|---------|--------------------------|---------|
| Manufacturing Process | Low (descriptive) | "Manufacturing employs..." "The process consists of..." |
| Characterization Results | Moderate | "Data indicate..." "Results demonstrate..." "Profiles are comparable..." |
| Comparability Conclusion | Moderate-High | "SB-300 is highly similar to..." "No clinically meaningful differences were identified..." |
| Stability Claims | Moderate | "Available data support a shelf life of..." "Ongoing studies will confirm..." |

### Key Language Patterns

**For comparative statements:**
- "Comparable to the reference product" (when within acceptance criteria)
- "Highly similar to the reference product" (for overall conclusion)
- "Fell within the quality range established by the reference product" (for range-based comparisons)
- "No clinically meaningful differences were identified in..." (for summary conclusions)

**Avoid in FDA submissions:**
- "Identical" (overclaims — use "highly similar" or "comparable")
- "Exactly the same" (unscientific)
- "Prove" (use "demonstrate" or "support")
- Absolute claims without quantitative backing

---

## Step 4: Cross-Check with CMC Forge Quality Checklist

From `skills/cmc-forge/references/quality-checklist.md`, key items for English CMC summary:

- [ ] Content completeness: All required sections present
- [ ] Banana Rule: "reference product" used consistently (not "originator", "innovator", "brand")
- [ ] Numerical integrity: All data values match source documents
- [ ] Regulatory compliance: ICH Q5E terminology used correctly
- [ ] Document hygiene: No DRAFT watermark in final, no internal project codes visible

---

## Output Classification

```
⚠️ DRAFT — For controlled review. Not a GMP-controlled document.
Module: CMC Forge (DRAFT) + Scientific Writer (REVIEW)
Classification: L2
Human review required: Yes — RA Lead + Native English Speaker + CMC SME
```

---

## Notes

- All text examples, company names, and product names are fictional.
- Writing quality methodology from Scientific Writer SKILL.md (5-pass audit).
- Language patterns from `skills/scientific-writer/references/section-models.md`.
- FDA biosimilar terminology follows ICH Q5E and FDA biosimilar guidance conventions.
- This example demonstrates the "Draft-then-Review" integration pattern (Pattern B).
