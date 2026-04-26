> 📖 基于 FDA/EMA/NMPA 官方文件整理，具体参数以各监管机构最新指南为准。

## 24. Biosimilar CMC Pathway

### 24.1 Biosimilar Development is Fundamentally a CMC Exercise

Unlike innovator biologics where clinical efficacy drives the program, biosimilar development is anchored in **analytical similarity**. The entire regulatory pathway (351(k) in US, Article 10(4) in EU) depends on demonstrating that the proposed biosimilar is highly similar to the reference product with no clinically meaningful differences.

### 24.2 Stepwise Development

```
Analytical Similarity (foundation)
    ↓
Functional Similarity (binding, bioassay)
    ↓
Clinical PK/PD (bridging)
    ↓
Clinical Efficacy/Safety (abbreviated, in one indication)
    ↓
Extrapolation to other indications (based on totality of evidence)
```

### 24.3 Reference Product Characterization

- **Sourcing**: Purchase multiple lots of the US-licensed reference product (and EU reference for global filing)
- **Lot-to-lot variability**: Characterize 10-15+ lots to establish the quality range for each CQA
- **Comprehensive analytical characterization**: Primary structure, higher-order structure, glycosylation, charge variants, size variants, potency, process-related impurities

### 24.4 Analytical Similarity Assessment

**Statistical approaches:**

| Tier                   | Attributes                              | Statistical Method                                |
| ---------------------- | --------------------------------------- | ------------------------------------------------- |
| Tier 1 (most critical) | Potency, glycosylation, binding         | Equivalence testing (90% CI within quality range) |
| Tier 2 (major)         | Charge variants, oxidation, aggregation | Quality range comparison                          |
| Tier 3 (minor)         | Visual appearance, pH, osmolality       | Raw data comparison                               |

**FDA Guidance:** "Development of Therapeutic Protein Biosimilars: Comparative Analytical Assessment and Other Quality-Related Considerations" (2019)

### 24.5 Process Development for Biosimilars

- **Reverse engineering**: Develop process to match the target product profile derived from reference product characterization (not from a known originator process)
- **Cell line development**: New cell line producing a product with matching CQA profile
- **Process optimization**: Tune upstream/downstream to achieve desired glycosylation, charge variant, and purity profiles
- **Iterative**: Multiple rounds of process modification to converge on analytical similarity

### 24.6 Interchangeability

- Additional requirement beyond biosimilarity (US only)
- Requires switching studies demonstrating no increased risk from alternating between reference and biosimilar
- Designated as interchangeable by FDA → allows pharmacy-level substitution without prescriber intervention

---

## 25. Combination Products and Fixed-Dose Combinations

### 25.1 Drug-Device Combination Products

**Regulatory framework:** 21 CFR Part 4; jurisdiction determined by primary mode of action (CDER vs. CDRH)

**Common combination products:**

| Product Type                          | Device Component                  | CMC Considerations                                                                                 |
| ------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------- |
| Pre-filled syringes with autoinjector | Autoinjector device               | Human factors, device reliability, extractables/leachables from device                             |
| Metered-dose inhalers (MDI)           | Valve, actuator                   | Delivered dose uniformity, aerodynamic particle size distribution (APSD), propellant compatibility |
| Dry powder inhalers (DPI)             | Inhaler device                    | Device-formulation interaction, moisture sensitivity, device robustness                            |
| Transdermal patches                   | Adhesive system, backing membrane | Adhesion testing, drug release rate, residual drug, skin irritation                                |
| Drug-eluting stents                   | Stent platform                    | Drug loading, elution kinetics, coating integrity, sterile processing                              |
| Intravitreal implants                 | Implant device                    | Biodegradable polymer, drug release over months, sterility                                         |

**Additional CMC requirements for combination products:**
- Design History File (per 21 CFR 820 for device constituent)
- Human factors/usability engineering (FDA guidance)
- Device-specific stability testing (mechanical, functional)
- Biocompatibility testing (ISO 10993 series)

### 25.2 Fixed-Dose Combinations (FDCs)

**CMC challenges unique to FDCs:**
- **Drug-drug compatibility**: Binary/ternary excipient compatibility studies between APIs
- **Dissolution requirements**: Discriminating dissolution conditions for each API individually
- **Content uniformity**: Must meet USP <905> for each API
- **Stability**: Monitor degradation of each API and potential cross-degradation (API A catalyzing degradation of API B)
- **Manufacturing**: May require separate granulations blended together, bilayer tablets, or coated pellets in capsule

**Example (Trikafta):** Triple-combination CFTR modulator — three distinct APIs with different physicochemical properties, each requiring its own impurity control and dissolution specification within a single fixed-dose tablet.

### 25.3 Orally Inhaled and Nasal Drug Products (OINDP)

- **Unique CQAs**: Delivered dose uniformity (DDU), aerodynamic particle size distribution (APSD by cascade impaction), moisture content, device actuation force
- **FDA-specific guidance**: "Metered Dose Inhaler (MDI) and Dry Powder Inhaler (DPI) Drug Products" — extensive CMC and bioequivalence guidance
- **Analytical methods**: Andersen Cascade Impactor (ACI), Next Generation Impactor (NGI), dose content uniformity apparatus
- **Device variability**: Must validate across multiple device lots

---

## 26. Nitrosamine Impurity Assessment

### 26.1 Background

In 2018, NDMA (N-nitrosodimethylamine) contamination was discovered in valsartan API from a specific manufacturer, triggering a global crisis. This expanded to multiple sartan drugs and then to ranitidine, metformin, and other products.

### 26.2 Regulatory Response

- **FDA**: "Control of Nitrosamine Impurities in Human Drugs" guidance (2021, updated 2023)
- **EMA**: Article 5(3) referral — mandatory risk assessments for all MAH
- **Health Canada, PMDA, TGA**: Harmonized requirements
- **Scope**: All chemically synthesized drug products, biologics, and OTC products

### 26.3 Risk Assessment Methodology

**Root causes for nitrosamine formation:**
1. Use of nitrite salts or nitrosating agents in API synthesis
2. Presence of secondary/tertiary amines + trace nitrites
3. Contaminated raw materials or solvents
4. Recycled materials/solvents carrying over nitrosating agents
5. Drug substance degradation forming nitrosamine under acidic conditions
6. Interaction between drug and excipients or packaging materials (especially for NDSRIs)

### 26.4 Acceptable Intake (AI) Limits

| Nitrosamine | AI (ng/day) |
| ----------- | ----------- |
| NDMA        | 96          |
| NDEA        | 26.5        |
| NMBA        | 96          |
| NIPEA       | 26.5        |
| NDIPA       | 26.5        |
| NDBA        | 26.5        |

For NDSRIs (Nitrosamine Drug Substance Related Impurities), AI should be determined using the **CPCA (Carcinogenic Potency Categorization Approach)** introduced by FDA in 2024 (Guidance Rev.2). The CPCA method categorizes NDSRIs based on structural features into potency categories with predefined AI limits, rather than requiring compound-specific data for each impurity.

### 26.5 Analytical Methods

- **LC-MS/MS**: Required sensitivity at ng/level (ppb in drug substance, sub-ppm in drug product)
- **GC-MS/MS**: For volatile nitrosamines
- **Method challenges**: Matrix effects, low levels, multiple analytes in single method
- **Confirmatory testing**: Required when risk assessment identifies potential for nitrosamine formation

### 26.6 Regulatory Timelines

- Initial risk assessment: Completed (deadlines passed for most products)
- Confirmatory testing: If risk identified, testing must be completed and results shared with agencies
- **Ongoing obligation**: Any manufacturing change must be re-evaluated for nitrosamine risk

---

## 27. Emerging Modalities — ADCs, Bispecifics, Oligonucleotides

### 27.1 Antibody-Drug Conjugates (ADCs)

**Unique CMC challenges:**

| Aspect                    | Detail                                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| Conjugation chemistry     | Site-specific (engineered cysteine, enzymatic) vs. stochastic (lysine, interchain cysteine)    |
| Drug-Antibody Ratio (DAR) | Critical CQA — target typically 2-4; measured by HIC, RP-HPLC                                  |
| Linker stability          | Cleavable (pH-sensitive, protease) vs. non-cleavable; in vivo stability is key                 |
| Payload potency           | Cytotoxic (auristatins, maytansinoids, camptothecins) — OEB5 containment required              |
| Free drug control         | Unconjugated payload is a critical impurity — must be minimized and controlled                 |
| Aggregate control         | Conjugation can increase aggregation propensity                                                |
| Manufacturing flow        | mAb production → conjugation → purification → fill/finish (multiple CMC dossiers)              |
| Analytical methods        | HIC (DAR distribution), RP-HPLC (drug loading), SEC (aggregates), potency (cytotoxicity assay) |

### 27.2 Bispecific Antibodies

**Diverse formats with different CMC implications:**

| Format                           | CMC Challenge                                                       |
| -------------------------------- | ------------------------------------------------------------------- |
| BiTE (bispecific T-cell engager) | Short half-life → continuous IV infusion or half-life extension     |
| Knobs-into-holes / CrossMAb      | Correct heterodimerization vs. homodimer; analytical discrimination |
| DVD-Ig (dual variable domain)    | Larger molecule, aggregation risk                                   |
| Trispecific and beyond           | Increasing complexity, more mispaired species                       |

**Key CQAs unique to bispecifics:**
- Correct chain pairing (% heterodimer vs. homodimer/mispaired)
- Dual-target binding activity (two potency assays may be needed)
- Charge and size variant analysis distinguishing heterodimer from homodimer

### 27.3 Oligonucleotide Therapeutics (siRNA, ASO)

**Drug substance CMC:**

| Aspect             | Detail                                                                                                                                                     |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Synthesis          | Solid-phase synthesis (phosphoramidite chemistry); 20-25mer typical                                                                                        |
| Purification       | IEX chromatography, RP-HPLC                                                                                                                                |
| Key CQAs           | Sequence identity, full-length purity (n-1 species are key impurities), phosphorothioate content, 2'-modification (2'-OMe, 2'-F, 2'-MOE), counterion (Na⁺) |
| GalNAc conjugation | For hepatocyte targeting; conjugation efficiency, linker integrity                                                                                         |
| Impurities         | n-1/n+1 truncations, depurination products, phosphodiester linkages (in PS backbone), stereoisomers                                                        |
| Analytical         | LC-MS (intact mass, impurity ID), IEX-HPLC (purity), CGE (length), CD (secondary structure)                                                                |

**Drug product CMC:**
- siRNA in lipid nanoparticles: Same LNP challenges as mRNA (particle size, encapsulation, stability)
- ASO subcutaneous injection: Solution formulation, typically simple phosphate buffer

### 27.4 Peptide Therapeutics

- **Manufacturing**: Solid-phase peptide synthesis (SPPS) or recombinant expression
- **Key CQAs**: Sequence identity, disulfide bond formation (correct pairing), diastereomers (D-amino acid impurities), acetylation/truncation impurities, aggregation
- **Analytical**: RP-HPLC, LC-MS/MS (peptide mapping), CE, amino acid analysis
- **Stability**: Peptides can be prone to deamidation, oxidation, and aggregation

### 27.5 Radiopharmaceuticals

- **Unique challenge**: Short half-lives (⁶⁸Ga: 68 min, ¹⁸F: 110 min) require rapid manufacturing and QC
- **Regulatory**: 21 CFR Part 212 (cGMP for PET drugs)
- **Release testing**: Must be completed before radioactive decay renders product unusable → emphasis on rapid methods and parametric release
- **Stability**: Measured in hours, not months

---

## 28. Drug Master Files (DMFs)

### 28.1 What is a DMF?

A Drug Master File is a submission to FDA that may be used to provide confidential detailed information about facilities, processes, or articles used in the manufacturing, processing, packaging, and storing of drugs.

### 28.2 DMF Types

| Type         | Content                                                               | Common Use                                                    |
| ------------ | --------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Type I**   | Manufacturing site, facilities, operating procedures, personnel       | Rarely used; largely obsolete                                 |
| **Type II**  | Drug substance, drug substance intermediate, drug product             | **Most common** — used by API manufacturers                   |
| **Type III** | Packaging material                                                    | Container closure systems, particularly for complex packaging |
| **Type IV**  | Excipient, colorant, flavor, essence, or material used in preparation | Novel excipients                                              |
| **Type V**   | FDA-accepted reference information                                    | Rarely used                                                   |

### 28.3 How DMFs Work

- **DMF holder** (e.g., API manufacturer) files the DMF with FDA
- DMF holder provides a **Letter of Authorization** to the NDA/ANDA/IND applicant
- Applicant references the DMF in their application
- **FDA reviews the DMF only when referenced** — DMFs are not independently reviewed or approved
- DMF holder maintains the DMF with annual updates

### 28.4 DMF vs. ASMF vs. CEP

| Aspect              | DMF (FDA)                              | ASMF (EMA)                                                      | CEP (EDQM)                                 |
| ------------------- | -------------------------------------- | --------------------------------------------------------------- | ------------------------------------------ |
| Structure           | Single confidential document           | Split: Applicant's Part (open) + Restricted Part (confidential) | Certificate referencing Ph. Eur. monograph |
| Review              | Only when referenced in an application | Assessed with each MAA                                          | Assessed independently by EDQM             |
| Approval status     | No standalone approval                 | No standalone approval                                          | Independent certificate issued             |
| Strategic advantage | Flexibility                            | Transparency to applicant                                       | Faster MAA assessment                      |

### 28.5 Strategic Considerations

- DMFs protect API manufacturer's proprietary process information while allowing drug product applicants to reference it
- Due diligence on DMF quality is essential when sourcing APIs from DMF holders
- A poorly maintained DMF can delay NDA/ANDA approval

---

## 29. Data Integrity and Electronic Records

### 29.1 Why Data Integrity Matters in CMC

Data integrity is a **top FDA enforcement priority**. Data integrity failures are a leading cause of Warning Letters, Import Alerts, and PAI failures, particularly at international manufacturing sites.

### 29.2 ALCOA+ Principles

| Principle           | Meaning                                                        |
| ------------------- | -------------------------------------------------------------- |
| **A**ttributable    | Data traceable to the person who generated it                  |
| **L**egible         | Data readable and permanent                                    |
| **C**ontemporaneous | Recorded at the time of the activity                           |
| **O**riginal        | First recording of the data (or a verified true copy)          |
| **A**ccurate        | Data is correct, truthful, and reflects what actually happened |
| + **C**omplete      | All data included, no selective reporting                      |
| + **C**onsistent    | Data follows logical sequence (timestamps, audit trails)       |
| + **E**nduring      | Recorded on durable media, maintained for retention period     |
| + **A**vailable     | Accessible for review throughout retention period              |

### 29.3 21 CFR Part 11 / EU GMP Annex 11

**Electronic records and electronic signatures requirements:**
- System validation (computerized system validation — CSV)
- Audit trail: Secure, computer-generated, time-stamped record of all changes
- Access controls: Unique user IDs, role-based permissions, periodic access reviews
- Electronic signatures: Legally equivalent to handwritten signatures when compliant
- Backup and disaster recovery
- Audit trail review: Must be part of routine batch record review

### 29.4 Common Data Integrity Findings

- Shared login credentials
- Disabled audit trails
- Backdating of records
- Selective reporting (deleting or hiding failing test results)
- Uncontrolled use of standalone systems (e.g., laboratory balances, pH meters without audit trails)
- Insufficient audit trail review during batch release
- Lack of CSV for laboratory instruments

---

## 30. Facility Design, Environmental Controls, and Utilities

### 30.1 Cleanroom Classification

| Standard  | Grade   | Max Particles ≥0.5µm/m³ (at rest) | Max Particles ≥0.5µm/m³ (in operation) | Typical Use                     |
| --------- | ------- | --------------------------------- | -------------------------------------- | ------------------------------- |
| EU GMP    | Grade A | 3,520                             | 3,520                                  | Aseptic filling, stoppering     |
| EU GMP    | Grade B | 3,520                             | 352,000                                | Background for Grade A          |
| EU GMP    | Grade C | 352,000                           | 3,520,000                              | Less critical processing        |
| EU GMP    | Grade D | 3,520,000                         | Not defined                            | Preparation, component washing  |
| ISO 14644 | ISO 5   | 3,520                             | —                                      | Equivalent to Grade A/B at rest |
| ISO 14644 | ISO 7   | 352,000                           | —                                      | Equivalent to Grade C at rest   |
| ISO 14644 | ISO 8   | 3,520,000                         | —                                      | Equivalent to Grade D at rest   |

### 30.2 HVAC Systems

- **Air changes per hour**: Grade A/B: >20 ACPH; Grade C: >20 ACPH; Grade D: >6 ACPH
- **Pressure differentials**: 10-15 Pa between grades; positive pressure in clean areas; negative pressure in potent compound suites
- **HEPA filtration**: 99.97% efficiency for particles ≥0.3µm; terminal HEPA filters in Grade A/B
- **Temperature and humidity**: Typically 20±2°C, 45±10% RH (controlled for product and operator comfort)
- **Qualification**: DQ → IQ → OQ → PQ; HEPA filter integrity testing (DOP/PAO challenge), airflow visualization (smoke studies)

### 30.3 Environmental Monitoring Program

| Parameter                  | Grade A | Grade B | Grade C | Grade D |
| -------------------------- | ------- | ------- | ------- | ------- |
| Viable air (CFU/m³)        | <1      | 10      | 100     | 200     |
| Settle plates (CFU/4h)     | <1      | 5       | 50      | 100     |
| Contact plates (CFU/plate) | <1      | 5       | 25      | 50      |
| Glove prints (CFU/glove)   | <1      | 5       | —       | —       |

- Trending of EM data with alert and action limits
- Identification of recovered organisms to species level for Grade A/B
- Investigation required for any action limit excursion

### 30.4 EU GMP Annex 1 (2022 Revision) — Key Changes

The 2022 revision of Annex 1 is the most significant GMP update for sterile products in decades:
- **Contamination Control Strategy (CCS)**: Required holistic document assessing all contamination risks
- **Expanded scope**: Now covers all sterile products (not just terminally sterilized and aseptically processed)
- **Barrier technology preferred**: RABS (Restricted Access Barrier Systems) and isolators encouraged over conventional cleanrooms
- **Enhanced EM requirements**: More detailed trending, identification requirements
- **APS (Aseptic Process Simulation)**: More prescriptive requirements for media fills
- **Integrity testing**: Enhanced CCI requirements for all sterile products

### 30.5 Water Systems

| Type                      | Generation                                | Quality Standard                                  | Use                                           |
| ------------------------- | ----------------------------------------- | ------------------------------------------------- | --------------------------------------------- |
| Purified Water (PW)       | RO + EDI (or distillation)                | USP <1231>, conductivity ≤1.3 µS/cm, TOC ≤500 ppb | Non-sterile manufacturing, equipment cleaning |
| Water for Injection (WFI) | Distillation or membrane (Ph. Eur. 2017+) | Same as PW + endotoxin ≤0.25 EU/mL                | Parenteral manufacturing, final rinse         |
| Clean Steam               | Clean steam generator                     | Condensate meets WFI specs                        | Autoclave sterilization                       |

### 30.6 Compressed Gas Systems

- Nitrogen, compressed air, CO₂ used in manufacturing
- Must be filtered (0.2µm for sterile applications)
- Qualification: particle count, microbial testing, dew point, oil content
- Monitoring: Periodic requalification per schedule

---

## 31. CMC Due Diligence for Licensing and M&A

### 31.1 When CMC Due Diligence is Needed

- In-licensing a clinical-stage or commercial-stage asset
- Acquiring a company or product line
- Evaluating a CDMO partnership
- Assessing a co-development or co-marketing deal

### 31.2 CMC Due Diligence Assessment Framework

| Area                        | Key Questions                                                                     | Red Flags                                              |
| --------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Process maturity**        | How well-characterized is the process? Is there a design space? Are CPPs defined? | No DoE data, poorly defined process parameters         |
| **Scalability**             | Has the process been run at commercial scale? What scale-up challenges exist?     | Only lab-scale data, untested critical steps at scale  |
| **Manufacturing site**      | GMP-compliant? Recent inspection history? Capacity available?                     | Warning Letters, 483s, capacity constraints            |
| **Supply chain**            | Single-source for critical materials? Starting materials IP-protected?            | Sole-source API, no backup suppliers                   |
| **Analytical methods**      | Validated? Stability-indicating? Transfer-ready?                                  | Unvalidated methods, no forced degradation data        |
| **Stability**               | Adequate data for claimed shelf life? Any adverse trends?                         | Short stability history, unexplained degradation       |
| **IP around manufacturing** | Process patents? Freedom-to-operate?                                              | Originator process patents blocking alternative routes |
| **Regulatory filing**       | Module 3 quality? IND/NDA complete and consistent?                                | Incomplete Module 3, unresolved FDA questions          |
| **Comparability**           | Process changes during development? Bridging data available?                      | Multiple process changes without comparability data    |
| **CMC team**                | Experienced CMC team? Key person dependencies?                                    | CMC knowledge concentrated in 1-2 individuals          |

### 31.3 CMC Risk Scoring

| Score  | Level         | Implication                                                                                          |
| ------ | ------------- | ---------------------------------------------------------------------------------------------------- |
| Green  | Low risk      | Standard development, no major concerns                                                              |
| Yellow | Moderate risk | Addressable with investment and time; factor into deal terms                                         |
| Red    | High risk     | Potential deal-breaker; may require process redesign, site change, or significant timeline extension |

### 31.4 CMC-Related Deal Terms

- **Tech transfer timeline and milestones** with acceptance criteria
- **Manufacturing supply agreements** with defined quality standards
- **CMC milestone payments** tied to IND filing, process validation, NDA submission
- **Representations and warranties** on GMP compliance, data integrity, and regulatory standing
- **Indemnification** for CMC-related regulatory actions

---

## 32. Generic Drug (ANDA) CMC Requirements

### 32.1 How ANDA CMC Differs from NDA CMC

ANDAs (Abbreviated New Drug Applications) rely on bioequivalence to the Reference Listed Drug (RLD) rather than independent safety and efficacy data. CMC requirements are adapted accordingly.

### 32.2 Key ANDA CMC Requirements

| Requirement            | Detail                                                                                                                                  |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Q1/Q2 Sameness**     | Qualitatively (Q1) and quantitatively (Q2) same inactive ingredients as RLD (for oral solids — other dosage forms have different rules) |
| **Dissolution**        | Comparative dissolution profiles in multiple media; f₂ similarity factor ≥50 (or biowaiver per BCS)                                     |
| **Bioequivalence**     | In vivo PK study demonstrating 90% CI of Cmax and AUC within 80-125% of RLD                                                             |
| **BCS Biowaivers**     | ICH M9 / FDA guidance: BCS Class I drugs may qualify for biowaiver based on in vitro dissolution data                                   |
| **Stability**          | At least 3 batches, 6 months accelerated + 6 months long-term at time of filing; shelf life based on available data                     |
| **Process validation** | Required at time of ANDA approval (on-site verification batch) or committed before commercial distribution                              |
| **Specifications**     | Generally aligned with RLD product; compendial where available                                                                          |

### 32.3 Paragraph IV Certifications and CMC

When a generic applicant files a Paragraph IV certification challenging an Orange Book-listed patent:
- **Polymorph patents**: CMC must demonstrate the generic product uses a non-infringing polymorph (or that the patent is invalid/not infringed)
- **Formulation patents**: Must design around patented excipient combinations or ratios
- **Process patents**: Must use a non-infringing manufacturing process
- CMC strategy directly impacts patent litigation risk and market exclusivity timing

---

## 33. Master Reference Table

### ICH Quality Guidelines

| Guideline | Title                               | CMC Relevance                                       |
| --------- | ----------------------------------- | --------------------------------------------------- |
| Q1A-Q1E   | Stability Testing                   | Core stability study design and evaluation          |
| Q2(R2)    | Validation of Analytical Procedures | Method validation requirements                      |
| Q3A(R2)   | Impurities in New Drug Substances   | DS impurity thresholds                              |
| Q3B(R2)   | Impurities in New Drug Products     | DP degradant thresholds                             |
| Q3C(R8)   | Residual Solvents                   | Solvent classification and limits                   |
| Q3D(R2)   | Elemental Impurities                | Metal impurity risk assessment                      |
| Q3E       | Extractables and Leachables         | E&L assessment framework                            |
| Q5A(R2)   | Viral Safety                        | Viral clearance requirements for biologics          |
| Q5B       | Expression Construct Analysis       | Genetic characterization of cell lines              |
| Q5C       | Stability of Biotech Products       | Biologics-specific stability considerations         |
| Q5D       | Cell Substrate Characterisation     | Cell bank testing requirements                      |
| Q5E       | Comparability                       | Pre/post-change comparability for biologics         |
| Q6A       | Specifications: Chemical Substances | Test requirements and acceptance criteria           |
| Q6B       | Specifications: Biotech Products    | Biologic-specific test requirements                 |
| Q7        | GMP for APIs                        | API manufacturing GMP standard                      |
| Q8(R2)    | Pharmaceutical Development          | QbD, design space, QTPP, CQAs                       |
| Q9(R1)    | Quality Risk Management             | Risk assessment tools and process                   |
| Q10       | Pharmaceutical Quality System       | PQS model, CAPA, change management                  |
| Q11       | Drug Substance Development          | Extends QbD to API, starting material justification |
| Q12       | Lifecycle Management                | Established conditions, PACMPs                      |
| Q13       | Continuous Manufacturing            | CM guidance for DS and DP                           |
| Q14       | Analytical Procedure Development    | Analytical QbD, ATP, PAR                            |
| M4Q(R1)   | CTD — Quality                       | Module 3 structure and content                      |
| M7(R2)    | Mutagenic Impurities                | Assessment and control of genotoxic impurities      |

### Key FDA Regulations

| Regulation     | Title                                                                          |
| -------------- | ------------------------------------------------------------------------------ |
| 21 CFR 210/211 | cGMP for Finished Pharmaceuticals                                              |
| 21 CFR 312     | IND Regulations (312.23 = CMC content)                                         |
| 21 CFR 314     | NDA Regulations (314.50 = application content; 314.70 = post-approval changes) |
| 21 CFR 601     | BLA Regulations                                                                |
| 21 CFR 600-680 | Biologics-specific Regulations                                                 |

### Key FDA Guidance Documents

| Guidance                                             | Year      | Topic                                             |
| ---------------------------------------------------- | --------- | ------------------------------------------------- |
| CGMP for Phase 1 Investigational Drugs               | 2008      | Reduced GMP for Phase 1                           |
| Process Validation: General Principles and Practices | 2011      | Three-stage lifecycle validation                  |
| PAT Framework                                        | 2004      | Real-time monitoring and control                  |
| Pharmaceutical cGMPs for the 21st Century            | 2004      | Risk-based quality framework                      |
| SUPAC-IR                                             | 1995      | Post-approval changes for IR oral solids          |
| SUPAC-MR                                             | 1997      | Post-approval changes for MR oral solids          |
| SUPAC-SS                                             | 1997      | Post-approval changes for semisolids              |
| ANDAs: Stability Testing                             | Various   | Stability testing guidance                        |
| Container Closure Systems                            | Various   | Packaging requirements                            |
| Analytical Procedures and Methods Validation         | 2015      | Complementing ICH Q2                              |
| CMC Information for Human Gene Therapy INDs          | 2020      | Gene therapy CMC requirements                     |
| Control of Nitrosamine Impurities in Human Drugs     | 2021/2023 | Nitrosamine risk assessment and control           |
| Development of Therapeutic Protein Biosimilars       | 2019      | Comparative analytical assessment for biosimilars |
| ANDA Submissions — Content and Format                | Various   | Generic drug CMC requirements                     |
| Data Integrity and Compliance with Drug CGMP         | 2018      | ALCOA+ principles, electronic records             |
| Combination Products — cGMP Requirements             | Various   | 21 CFR Part 4, device constituent GMP             |
| Metered Dose Inhaler and DPI Drug Products           | 1998/2018 | OINDP CMC and bioequivalence                      |

---

## 34. Glossary of Key CMC Terms

| Term         | Definition                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| **API**      | Active Pharmaceutical Ingredient — the drug substance                                                  |
| **APQR**     | Annual Product Quality Review                                                                          |
| **ASD**      | Amorphous Solid Dispersion                                                                             |
| **ASMF**     | Active Substance Master File (EU equivalent of DMF)                                                    |
| **ATP**      | Analytical Target Profile                                                                              |
| **BCS**      | Biopharmaceutics Classification System                                                                 |
| **BLA**      | Biologics License Application                                                                          |
| **CAPA**     | Corrective Action and Preventive Action                                                                |
| **CBE**      | Changes Being Effected (supplement type)                                                               |
| **CCI**      | Container Closure Integrity                                                                            |
| **CEP**      | Certificate of Suitability (EDQM)                                                                      |
| **CPP**      | Critical Process Parameter                                                                             |
| **CPV**      | Continued Process Verification                                                                         |
| **CQA**      | Critical Quality Attribute                                                                             |
| **CRL**      | Complete Response Letter                                                                               |
| **CTD**      | Common Technical Document                                                                              |
| **DMF**      | Drug Master File                                                                                       |
| **DoE**      | Design of Experiments                                                                                  |
| **DP**       | Drug Product                                                                                           |
| **DS**       | Drug Substance                                                                                         |
| **DSC**      | Differential Scanning Calorimetry                                                                      |
| **E&L**      | Extractables and Leachables                                                                            |
| **EC**       | Established Conditions (ICH Q12)                                                                       |
| **EMA**      | European Medicines Agency                                                                              |
| **FMEA**     | Failure Mode and Effects Analysis                                                                      |
| **GMP/cGMP** | (current) Good Manufacturing Practice                                                                  |
| **HBEL**     | Health-Based Exposure Limit                                                                            |
| **HCP**      | Host Cell Protein                                                                                      |
| **HME**      | Hot Melt Extrusion                                                                                     |
| **HVLD**     | High-Voltage Leak Detection                                                                            |
| **ICH**      | International Council for Harmonisation                                                                |
| **IND**      | Investigational New Drug Application                                                                   |
| **IPC**      | In-Process Control                                                                                     |
| **IQ/OQ/PQ** | Installation/Operational/Performance Qualification                                                     |
| **LNP**      | Lipid Nanoparticle                                                                                     |
| **MCB/WCB**  | Master Cell Bank / Working Cell Bank                                                                   |
| **MVTR**     | Moisture Vapor Transmission Rate                                                                       |
| **NDA**      | New Drug Application                                                                                   |
| **NOR**      | Normal Operating Range                                                                                 |
| **OOS/OOT**  | Out of Specification / Out of Trend                                                                    |
| **PACMP**    | Post-Approval Change Management Protocol                                                               |
| **PAI**      | Pre-Approval Inspection                                                                                |
| **PAR**      | Proven Acceptable Range                                                                                |
| **PAS**      | Prior Approval Supplement                                                                              |
| **PAT**      | Process Analytical Technology                                                                          |
| **PDE**      | Permitted Daily Exposure                                                                               |
| **PPQ**      | Process Performance Qualification                                                                      |
| **PQS**      | Pharmaceutical Quality System                                                                          |
| **QbD**      | Quality by Design                                                                                      |
| **QP**       | Qualified Person (EU)                                                                                  |
| **QTPP**     | Quality Target Product Profile                                                                         |
| **RTRT**     | Real-Time Release Testing                                                                              |
| **SCT**      | Safety Concern Threshold                                                                               |
| **SPC**      | Statistical Process Control                                                                            |
| **SUPAC**    | Scale-Up and Post-Approval Changes                                                                     |
| **TTC**      | Threshold of Toxicological Concern                                                                     |
| **XRPD**     | X-Ray Powder Diffraction                                                                               |
| **ADC**      | Antibody-Drug Conjugate                                                                                |
| **ALCOA+**   | Attributable, Legible, Contemporaneous, Original, Accurate + Complete, Consistent, Enduring, Available |
| **ANDA**     | Abbreviated New Drug Application                                                                       |
| **APSD**     | Aerodynamic Particle Size Distribution                                                                 |
| **ASO**      | Antisense Oligonucleotide                                                                              |
| **CDMO**     | Contract Development and Manufacturing Organization                                                    |
| **CCS**      | Contamination Control Strategy (EU GMP Annex 1)                                                        |
| **CMO**      | Contract Manufacturing Organization                                                                    |
| **CSV**      | Computerized System Validation                                                                         |
| **DAR**      | Drug-Antibody Ratio                                                                                    |
| **DDU**      | Delivered Dose Uniformity                                                                              |
| **FDC**      | Fixed-Dose Combination                                                                                 |
| **GDP**      | Good Distribution Practice                                                                             |
| **NDMA**     | N-Nitrosodimethylamine                                                                                 |
| **NDSRI**    | Nitrosamine Drug Substance Related Impurity                                                            |
| **RABS**     | Restricted Access Barrier System                                                                       |
| **RLD**      | Reference Listed Drug                                                                                  |
| **siRNA**    | Small Interfering RNA                                                                                  |
| **WFI**      | Water for Injection                                                                                    |

---

## Part 2: China-Specific CMC Topics

35. [China CMC Regulatory Framework](#35-china-cmc-regulatory-framework)
36. [China-US-EU CMC Comparison](#36-china-us-eu-cmc-comparison)
37. [Bilingual CMC Glossary](#37-bilingual-cmc-glossary)
38. [China Drug Development CMC Milestones](#38-china-drug-development-cmc-milestones)
39. [China DMF and Associated Review](#39-china-dmf-and-associated-review)
40. [CMC Management under MAH System](#40-cmc-management-under-mah-system)
41. [Common CMC Deficiency Cases in China](#41-common-cmc-deficiency-cases-in-china)
42. [Major China CMC Regulatory Updates 2024-2026](#42-major-china-cmc-regulatory-updates-2024-2026)

***
