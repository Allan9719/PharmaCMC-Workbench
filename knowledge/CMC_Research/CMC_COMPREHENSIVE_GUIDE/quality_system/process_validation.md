> 📖 基于 ICH Q13、FDA/EMA 指南及行业实践整理。

## 18. Emerging Trends in CMC

### 18.1 Continuous Manufacturing (ICH Q13)

| Aspect     | Detail                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------- |
| Definition | Material continuously fed and processed; output collected continuously                            |
| Advantages | 80-90% smaller footprint, hours vs. weeks, real-time quality, flexible batch sizes, reduced waste |
| Challenges | Batch definition, RTD modeling, cleaning/changeover, capital investment                           |
| Regulatory | ICH Q13 provides harmonized guidance; FDA strongly supportive                                     |

**Real-world examples:**
- Vertex (Orkambi/Symdeko): First FDA-approved continuous manufacturing (2015)
- Janssen (Prezista): Batch-to-continuous transition approved 2016
- Pfizer: Portable, continuous, miniature, and modular (PCMM) platform

### 18.2 Real-Time Release Testing (RTRT)

- Uses PAT data to release product without traditional end-product testing
- Example: NIR model predicts tablet content uniformity during compression, replacing HPLC
- Requires robust chemometric model development and validation
- Growing regulatory acceptance

### 18.3 Digital Twins

- Digital replica of manufacturing process using real-time data, simulation, and ML
- Applications: Virtual experiments, scale-up prediction, real-time monitoring, predictive maintenance
- Adopted by large pharma (GSK, Sanofi, Amgen)

### 18.4 AI/ML in CMC

| Application         | Example                                         |
| ------------------- | ----------------------------------------------- |
| Process development | ML models to predict optimal process parameters |
| Process monitoring  | AI-driven anomaly detection in real-time data   |
| Quality prediction  | Predictive CQA models from process parameters   |
| Impurity prediction | Computational degradation pathway prediction    |
| Document authoring  | AI-assisted Module 3 CTD generation             |
| Batch record review | NLP-based automated review                      |

### 18.5 Other Trends

- **Decentralized/Point-of-Care manufacturing** (cell therapies)
- **Modular and portable manufacturing** (pandemic preparedness)
- **3D printing of pharmaceuticals** (Spritam, first FDA-approved 3D-printed drug, 2015)
- **FDA Emerging Technology Program** for novel manufacturing approaches
- **FDA KASA** (Knowledge-Aided Assessment and Structured Application) for structured CMC review

---

## 19. Common CMC Pitfalls and How to Avoid Them

### 19.1 Top Causes of CMC-Related FDA CRLs

| Rank | Cause                                   | Detail                                                                 |
| ---- | --------------------------------------- | ---------------------------------------------------------------------- |
| 1    | **Manufacturing facility deficiencies** | PAI failures, GMP violations, data integrity issues                    |
| 2    | **Insufficient process validation**     | Incomplete PPQ, validation not supporting commercial process           |
| 3    | **Stability failures**                  | OOS results during review, insufficient data for proposed shelf life   |
| 4    | **Specifications issues**               | Unjustified specs, missing critical tests, inadequate impurity control |
| 5    | **Analytical method deficiencies**      | Unvalidated methods, inadequate potency assay precision (biologics)    |
| 6    | **Incomplete Module 3**                 | Missing sections, internal inconsistencies                             |

### 19.2 CMC-Related Clinical Holds

Triggers:
- Safety-related impurities (especially genotoxic per ICH M7)
- Sterility or endotoxin failures (injectables)
- Stability failures affecting safety/efficacy
- Significant GMP deviations
- Inadequate CMC information in IND
- Potency assay issues (biologics — uncertain dosing)
- Container closure integrity failures (sterile products)

Resolution: 30 days for FDA to respond after sponsor addresses all deficiencies.

### 19.3 Top 10 Best Practices

1. **Engage CMC early** — CMC scientists at the table from candidate selection
2. **Plan manufacturing site readiness** — begin site qualification 12-18 months before NDA filing
3. **Start stability studies early** — cannot accelerate time; lock commercial formulation early
4. **De-risk supply chain** — qualify multiple suppliers for critical materials
5. **Invest in analytical development** — under-resourcing is a common cause of delays
6. **Robust change management** — track all process changes and their impact
7. **Use platform approaches** where possible — saves 1-2 years for established modalities
8. **Conduct mock PAI audits** — before filing, identify and remediate gaps
9. **Prepare for information requests** — have CMC team ready for rapid FDA response
10. **Align globally** — if multi-region filing, harmonize CMC strategy across FDA/EMA/PMDA from the start

### 19.4 Real-World Cautionary Examples

- **Dendreon (Provenge):** Manufacturing delays and cost overruns for autologous cell therapy → bankruptcy
- **Emergent BioSolutions (COVID):** Cross-contamination between AstraZeneca and J&J vaccine substances → millions of doses destroyed, FDA facility shutdown
- **Sarepta (Elevidys):** Gene therapy manufacturing consistency and potency assay variability → initial CMC challenges
- **Multiple gene therapy programs:** Delays from insufficient viral vector manufacturing capacity

---

## 20. FDA vs. EMA — CMC Comparison

| Aspect                  | FDA (US)                                            | EMA (EU)                                                       |
| ----------------------- | --------------------------------------------------- | -------------------------------------------------------------- |
| Filing format           | CTD Module 3 (identical)                            | CTD Module 3 (identical)                                       |
| API documentation       | DMF (Drug Master File)                              | ASMF or CEP (Certificate of Suitability from EDQM)             |
| Post-approval changes   | SUPAC framework (PAS, CBE-30, CBE-0, Annual Report) | Variations Regulation (Type IA, IAIN, IB, Type II, Extensions) |
| GMP inspections         | FDA ORA directly inspects                           | National competent authorities (MHRA, ANSM, etc.)              |
| Batch release           | QC release by manufacturer                          | Qualified Person (QP) certification legally required           |
| Compendial standard     | USP-NF                                              | European Pharmacopoeia (Ph. Eur.)                              |
| Sterile manufacturing   | FDA Aseptic Processing Guidance (2004)              | EU GMP Annex 1 (2022 — significantly more detailed)            |
| Assessment transparency | FDA review documents                                | EPAR with detailed quality assessment                          |
| Assessment process      | Single FDA division review                          | Rapporteur + Co-Rapporteur from 2 member states                |
| Biosimilar CMC          | FDA framework (2012+)                               | EMA pathway (established earlier, more extensive guidelines)   |
| ATMPs                   | FDA gene/cell therapy guidances                     | Regulation (EC) 1394/2007, CAT committee                       |
| TSE/BSE risk            | Adventitious agent assessment                       | Specific formalized TSE guidance (EMA/410/01 Rev.3)            |

**EMA Variation Types:**

| Type      | Description                   | Timing                                          |
| --------- | ----------------------------- | ----------------------------------------------- |
| Type IA   | Minor, "do and tell"          | Implement immediately, notify within 12 months  |
| Type IAIN | Minor, immediate notification | Implement and notify immediately                |
| Type IB   | Minor, "tell, wait, and do"   | Notify; implement after 30 days if no objection |
| Type II   | Major                         | Requires prior approval (standard 60-day review, may extend to ~90 days with clock-stop) |
| Extension | Fundamental change            | New application-level review                    |

---

## 21. Technology Transfer

### 21.1 What Technology Transfer Means in CMC

Technology transfer is the systematic, documented process of transferring process knowledge, analytical methods, and manufacturing procedures from one site (the "sending unit") to another (the "receiving unit"). It is one of the most practically important and frequently encountered CMC activities.

**Common transfer scenarios:**
- Development lab → pilot plant
- Pilot plant → commercial manufacturing site
- CDMO → in-house manufacturing (or reverse)
- Site A → Site B (commercial to commercial, for capacity, cost, or risk mitigation)
- Originator → licensee (in-licensing/out-licensing deals)

### 21.2 Technology Transfer Package

A complete technology transfer includes:

| Component                  | Contents                                                                          |
| -------------------------- | --------------------------------------------------------------------------------- |
| **Process description**    | Detailed process flow, unit operations, CPPs, CQAs, design space                  |
| **Master batch record**    | Step-by-step manufacturing instructions, IPCs, sampling plans                     |
| **Analytical methods**     | Method descriptions, validation reports, reference standards                      |
| **Raw material specs**     | Specifications for all starting materials, intermediates, excipients              |
| **Equipment requirements** | Equipment specifications, capacity, materials of construction, scale-up rationale |
| **Cleaning procedures**    | Validated cleaning methods, acceptance criteria, MACO/HBEL calculations           |
| **Stability data**         | Historical stability data, protocol for new-site batches                          |
| **Regulatory history**     | IND/NDA amendments, process change history, prior regulatory commitments          |
| **Risk assessment**        | Site-specific risk assessment, equipment mapping, gap analysis                    |

### 21.3 Transfer Execution

**Transfer batches:**
- Typically 1-3 batches at receiving site (prior to formal PPQ)
- Comparison to sending site batch data on all CQAs
- Acceptance criteria defined in transfer protocol (e.g., CQAs within ±X% of sending site mean)
- Enhanced sampling (similar to PPQ)

**Equipment mapping:**
- Different equipment brands/models at sending vs. receiving site require parameter translation
- Dimensional analysis, geometric similarity, scale-up parameters (tip speed, Froude number, Reynolds number)
- Example: Different granulator → match impeller tip speed, not RPM

**Common transfer failures and root causes:**
- Dissolution shift (different granulator design, compression profile)
- Yield drop (material handling losses at different scale)
- Impurity profile changes (different heating/cooling rates, hold times)
- Content uniformity issues (different blender geometry)

### 21.4 Analytical Method Transfer

**Approaches (per USP <1224>):**

| Approach            | When Used                                                           |
| ------------------- | ------------------------------------------------------------------- |
| Comparative testing | Most common; both labs analyze same samples; statistical acceptance |
| Co-validation       | Both labs validate independently with same protocol                 |
| Revalidation        | Receiving lab performs full validation                              |
| Transfer waiver     | Simple methods (pH, KF) or compendial methods                       |

**Acceptance criteria:** Receiving lab typically within ±2-3% of sending lab mean, equivalent precision (F-test for variances, t-test for means).

### 21.5 Regulatory Implications

- **New commercial manufacturing site** = PAS (Prior Approval Supplement) in US; Type II Variation in EU
- PAI at the receiving site typically required
- New stability data from receiving site batches required
- If transfer occurs during development, IND amendment required for significant site changes

---

## 22. CMO/CDMO Management and Quality Agreements

### 22.1 Why CDMO Management Matters

The majority of small and mid-size pharma companies use CDMOs (Contract Development and Manufacturing Organizations) for some or all manufacturing. The marketing authorization holder retains full regulatory responsibility regardless of outsourcing.

### 22.2 CDMO Selection Criteria

| Criterion                 | Assessment                                                                 |
| ------------------------- | -------------------------------------------------------------------------- |
| Technical capability      | Equipment, scale, dosage form expertise, modality experience               |
| Regulatory track record   | FDA/EMA inspection history, 483s, Warning Letters                          |
| Capacity and availability | Current utilization, ability to meet timeline, dedicated vs. shared suites |
| Quality systems maturity  | QMS, deviation rate, CAPA effectiveness, change control                    |
| Geographic location       | Proximity to sponsor, regulatory risk (Import Alerts), logistics           |
| Financial stability       | Solvency, long-term viability                                              |
| IP protection             | Confidentiality practices, data security, non-compete clauses              |
| References                | Track record with similar molecules/products                               |

### 22.3 Quality Agreements

**Required by:** 21 CFR 211.22 (US), EU GMP Chapter 7, ICH Q7 Section 16

**Essential content:**

| Section                        | Key Elements                                                                             |
| ------------------------------ | ---------------------------------------------------------------------------------------- |
| **Roles and responsibilities** | Who approves batch records, who investigates deviations, who releases batches            |
| **Change control**             | Mutual notification requirements, approval process for changes affecting product quality |
| **Deviation management**       | Notification timelines, investigation responsibilities, CAPA requirements                |
| **Batch release**              | Release criteria, documentation required, QP responsibilities (EU)                       |
| **Audit rights**               | Frequency, scope, notice period, regulatory inspection support                           |
| **Regulatory obligations**     | Filing responsibilities, inspection support, annual report contributions                 |
| **Specifications and testing** | Who performs release testing, who holds reference standards                              |
| **Stability**                  | Who conducts stability studies, data sharing                                             |
| **Complaints and recalls**     | Investigation responsibilities, communication protocols                                  |
| **Material management**        | Raw material sourcing, approved suppliers, incoming testing                              |
| **Subcontracting**             | Approval requirements for further outsourcing                                            |

### 22.4 Sponsor Oversight of CDMOs

- **Regular audits**: Initial qualification audit, annual/biannual surveillance audits, for-cause audits
- **Batch record review**: Real-time or retrospective review of all batch production records
- **Deviation trending**: Monitor CDMO deviation rates and types over time
- **KPI tracking**: Right-first-time rate, batch cycle time, deviation closure time, OOS rate
- **On-site presence**: Embedded quality representative for critical programs
- **Remote monitoring**: Digital batch record systems enabling real-time visibility

### 22.5 Multi-CDMO Strategy

- Dual-source critical manufacturing steps for supply chain resilience
- Regulatory implications: each site requires its own supplement/variation
- Tech transfer between CDMOs requires full transfer package
- Comparability data between sites required

---

## 23. Supply Chain and Vendor Qualification

### 23.1 Vendor Qualification Program

**Risk-based tiering:**

| Tier     | Material Type                                                  | Qualification Level                                                |
| -------- | -------------------------------------------------------------- | ------------------------------------------------------------------ |
| Critical | API starting materials, key intermediates, critical excipients | Full on-site audit, qualification testing, annual review           |
| Major    | Excipients, processing aids, primary packaging                 | Desktop audit + questionnaire, CoA verification + periodic testing |
| Minor    | Secondary packaging, non-product contact materials             | Questionnaire, CoA review                                          |

### 23.2 Supplier Qualification Activities

- **Audit program**: Initial qualification audit, routine surveillance (every 2-3 years for critical), for-cause audits
- **Qualification testing**: Compare supplier CoA results to in-house testing (minimum 3 lots)
- **Change notification agreements**: Supplier must notify of any changes to manufacturing process, specifications, or site
- **Approved supplier list**: Maintained by quality unit; changes require formal change control

### 23.3 Incoming Material Testing

- **Full testing**: Per specification for each lot received (required for APIs)
- **Reduced testing**: Identity + CoA verification after qualification (permitted for excipients under risk-based justification, per 21 CFR 211.84)
- **Skip-lot testing**: Testing every Nth lot after extensive qualification and trending (requires scientific justification)

### 23.4 Supply Chain Risk Management

| Risk                                             | Mitigation                                                               |
| ------------------------------------------------ | ------------------------------------------------------------------------ |
| Single-source dependency                         | Qualify ≥2 suppliers for critical materials                              |
| Geographic concentration                         | Diversify supplier locations; avoid sole reliance on one country         |
| Regulatory action (Import Alert, Warning Letter) | Monitoring of FDA enforcement actions against suppliers                  |
| Geopolitical disruption                          | Safety stock policy (3-6 months for critical materials)                  |
| Quality drift                                    | Trending of incoming material test results; annual quality review        |
| Raw material discontinuation                     | Early notification agreements; contingency qualification of alternatives |

### 23.5 Water Systems

- **Purified Water (PW)**: USP requirements, for non-sterile manufacturing
- **Water for Injection (WFI)**: By distillation (traditional) or membrane-based (now accepted by Ph. Eur. since 2017); required for parenteral products
- **System qualification**: IQ/OQ/PQ, microbial and chemical monitoring, action/alert limits
- **Continuous monitoring**: TOC, conductivity at point-of-use, microbial sampling per schedule

---
