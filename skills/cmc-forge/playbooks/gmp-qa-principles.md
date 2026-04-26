# GMP/QA Principles Playbook

> GMP execution fundamentals for drafting deviations, investigations, change controls, batch record reviews, and data integrity documentation. This playbook covers the lifecycle of quality events in a GMP environment.

## Scope and Purpose

This playbook provides the domain knowledge needed to:

- Draft deviation reports, investigation summaries, and CAPA plans
- Structure OOS/OOT investigation documentation
- Design change control packages with risk-based assessments
- Apply ALCOA+ data integrity principles to document drafts
- Prepare batch record review checklists
- Structure supplier qualification documentation

All outputs are drafts. This skill does not approve, sign, or release.

---

## 1. Deviation Management

### 1.1 Deviation Classification

Every deviation must be classified before the investigation proceeds. Classification determines investigation depth, CAPA requirements, and reporting timelines.

| Classification | Definition | Examples | Typical Timeline |
|----------------|-----------|----------|-----------------|
| **Critical** | Directly affects product quality, patient safety, or data integrity. May invalidate validated state. | - Sterility test failure on released batch<br>- Cross-contamination event<br>- Temperature excursion beyond proven acceptable range for cold-chain product<br>- Data integrity finding in GMP records<br>- Use of unqualified equipment for critical process step | Investigation closure: 30 days. CAPA implementation: immediate. QA Head and site leader notification within 24 hours. |
| **Major** | Potential to affect product quality or compliance if unaddressed. Does not directly cause patient risk but indicates a systemic weakness. | - CPP excursion within proven acceptable range but outside normal operating range<br>- Environmental monitoring excursion in Grade A zone<br>- Batch record incomplete at release (missing signature, not missing data)<br>- Calibration overdue on non-critical instrument<br>- SOP revision overdue by >90 days | Investigation closure: 30-60 days. CAPA implementation: risk-based. QA notification within 72 hours. |
| **Minor** | No direct or indirect impact on product quality. Administrative or documentation issue. | - Typo in batch record (corrected, no data impact)<br>- Label formatting inconsistency (correct information)<br>- Training record filed late<br>- Housekeeping observation in non-critical area | Investigation closure: 60-90 days. CAPA: may not be required. Standard QA routing. |

**Escalation rule**: If investigation reveals the deviation is more severe than initially classified, reclassify upward and restart the clock at the higher classification. Reclassification requires QA Head approval.

### 1.2 Investigation Methodology

#### 5 Whys

Use when: the root cause appears straightforward and the scope is narrow (single event, single unit operation).

Process:
1. State the problem precisely (what happened, where, when, how detected).
2. Ask "Why did this happen?" and answer with a factual, evidence-based cause.
3. Repeat on each answer until you reach a root cause that is actionable (i.e., a specific system, process, or control that can be modified).
4. Typically 3-5 layers. If you reach "human error" at Why #2, push further — "human error" is a cause category, not a root cause.
5. Verify the root cause chain by reading it forward: "Because [root cause], then [cause 3], then [cause 2], then [cause 1], therefore [problem]." If the chain does not logically connect, investigate further.

Pitfall: The 5 Whys assumes a single causal chain. If the deviation resulted from multiple contributing factors, use Fishbone or Fault Tree instead.

#### Ishikawa (Fishbone) Diagram

Use when: multiple potential causes exist, or the deviation spans more than one functional area.

Categories (6M framework):

| Category | What to Examine | CMC Examples |
|----------|----------------|-------------|
| **Man (Personnel)** | Training, competency, fatigue, procedures followed | Operator not trained on revised SOP; shift change communication gap; visual inspection failure |
| **Machine (Equipment)** | Qualification state, maintenance, calibration, performance | Pump accuracy drift; filter integrity test failure; HVAC excursion; column lifetime exceeded |
| **Material** | Raw material quality, supplier changes, storage conditions | Buffer pH out of specification upon receipt; resin lot change; container-closure defect |
| **Method** | SOPs, recipes, parameters, sequence | Incorrect pH adjustment target in SOP; sampling method inappropriate for viscosity; hold time exceeded |
| **Measurement** | Analytical method, instrument calibration, sampling | Method not validated for new matrix; sampling point not representative; instrument out of calibration |
| **Milieu (Environment)** | Temperature, humidity, contamination, utilities | Power outage; water system TOC excursion; particulate exceeding limits in fill area |

Process:
1. Define the effect (the deviation) at the head of the fish.
2. Assign each 6M category as a major bone.
3. Brainstorm potential causes under each category.
4. Evaluate each potential cause against available evidence.
5. Eliminate causes contradicted by evidence.
6. Confirm the remaining most probable root cause(s).

#### Fault Tree Analysis (FTA)

Use when: the deviation is critical, the root cause is unclear, or you need to demonstrate thoroughness for regulatory purposes (especially for product quality complaints or sterility assurance failures).

Process:
1. Define the top event (the deviation) as the root of the tree.
2. Decompose into contributing conditions using AND/OR logic gates.
3. Continue decomposing each condition until you reach basic events (specific failures that can be independently verified or disproven).
4. Identify the cut sets (combinations of basic events that could cause the top event).
5. Evaluate each basic event against evidence.
6. The confirmed basic events form the root cause set.

FTA is more rigorous than 5 Whys or Fishbone, but requires more time and expertise. Reserve for critical deviations or systemic failures.

### 1.3 Root Cause Categories

When documenting root cause, classify into one of these categories. The category determines the CAPA type:

| Category | Root Cause Description | Typical CAPA Type |
|----------|----------------------|-------------------|
| **Procedure inadequate** | SOP does not cover the scenario, or is ambiguous. | Revise SOP. Add decision tree or flowchart. |
| **Procedure not followed** | SOP exists and is adequate but was not executed as written. | Retraining. Consider WHY the operator deviated (workload, ergonomics, time pressure). |
| **Training insufficient** | Personnel were not trained, or training did not achieve competence. | Retrain with competency assessment. Update training curriculum. |
| **Equipment failure** | Equipment malfunction, calibration drift, or maintenance gap. | Repair/replace. Revise preventive maintenance schedule. |
| **Material issue** | Incoming material out of specification or not tested adequately. | Tighten incoming QC. Evaluate supplier. |
| **Systemic gap** | No system, process, or control exists for the situation that occurred. | New SOP, new control, or new system. |
| **Design deficiency** | Process, facility, or system design does not prevent the failure mode. | Engineering change. May require change control. |

### 1.4 Impact Assessment Scope

After identifying root cause, assess impact across these dimensions:

1. **Affected batch(es)**: Is the batch in question impacted? Can it be released, or must it be rejected? Document the rationale for either decision.
2. **Other batches**: Could the same root cause have affected other batches currently in production, in storage, or already released? Define the lookback window and search criteria.
3. **Validated state**: Does the deviation indicate that the validated state of the process, method, or system is compromised? If yes, a revalidation assessment is required.
4. **Stability program**: Are any ongoing stability studies affected by the deviation (e.g., samples stored under deviated conditions)?
5. **Regulatory submissions**: Does the deviation affect any pending or planned submissions (IND, BLA, variation)?
6. **Registered specifications**: Does the deviation affect the registered specification or filing commitments?

### 1.5 CAPA Design Principles

A well-designed CAPA has these characteristics:

1. **Specific**: The action describes exactly what will be done, by whom, and by when. Not "improve training" but "revise SOP-123 to include pH adjustment decision tree; retrain all operators on Rev 4 by [date]; assess competency via supervised batch execution."
2. **Proportional**: The scope and effort of the CAPA match the severity and likelihood of the risk. A minor documentation error does not require a site-wide SOP overhaul.
3. **Addresses root cause, not symptom**: The CAPA targets the identified root cause. If the root cause is "SOP was ambiguous," the CAPA revises the SOP — it does not just retrain on the ambiguous SOP.
4. **Preventive, not just corrective**: Corrective actions fix the immediate problem. Preventive actions address the systemic condition that allowed the problem to occur. Both are required for major and critical deviations.
5. **Effectiveness check defined**: Every CAPA for major and critical deviations must have an effectiveness check — a measurable criterion that confirms the CAPA worked. This is typically assessed 6-12 months after implementation.

### 1.6 Effectiveness Check Design

| CAPA Type | Effectiveness Check Approach | Example |
|-----------|------------------------------|---------|
| SOP revision | Audit compliance with revised SOP for N consecutive executions | "Review 10 consecutive batch records for correct execution of revised pH adjustment step" |
| Training | Competency assessment | "Operator passes supervised execution assessment on first attempt" |
| Equipment change | Monitor performance data | "No pump accuracy excursions in 6 months post-replacement, verified by calibration data" |
| Systemic control addition | Monitor for recurrence | "Zero recurrence of deviation type in 12 months" |

**Effectiveness check failure**: If the effectiveness check reveals the CAPA did not prevent recurrence, the deviation must be reopened or a new deviation initiated. The original root cause analysis is re-evaluated.

### 1.7 The "Never Close with Just 'Human Error'" Rule

**Rule**: A deviation investigation must not close with "human error" (or "operator error," "staff mistake," "inadvertent error") as the sole root cause.

**Why**: "Human error" describes what happened, not why it happened. An operator made an error because something in the system allowed, encouraged, or failed to prevent that error. The investigation must identify the systemic factor:

| If the operator... | The systemic root cause is... |
|---------------------|-------------------------------|
| Didn't know the correct procedure | Training gap |
| Knew but the procedure was hard to follow | Procedure design (usability) |
| Knew but chose to deviate | Cultural or workload issue |
| Knew but made a physical mistake | Engineering control missing (poka-yoke) |
| Was fatigued or rushed | Staffing or scheduling issue |

Closing with "human error" and a CAPA of "retrain" is the most common CAPA effectiveness failure, because retraining does not fix a procedure that is confusing, an environment that is error-prone, or a staffing model that creates fatigue.

**Exception**: If a thorough investigation genuinely concludes that the operator was fully trained, the procedure was clear, engineering controls were in place, and the error was truly random, document this analysis explicitly. State the evidence that rules out each systemic cause. Then the root cause is classified as "procedure not followed — isolated event" with retraining, and the effectiveness check monitors for recurrence.

---

## 2. OOS/OOT Investigation Framework

### 2.1 Phase I: Laboratory Investigation

Trigger: A single test result falls outside its specification limit.

Objective: Determine whether the OOS result is attributable to a laboratory error, before expanding scope to the batch.

Timeline: Typically 3-5 business days.

#### Phase I Assessment Checklist

| Step | Action | Decision |
|------|--------|----------|
| 1 | Analyst reports OOS result immediately to supervisor. Do not retest without documentation. | Proceed to Step 2. |
| 2 | Review the test execution: Was the procedure followed? Check calculations, instrument performance, system suitability, reagent preparation, and environmental conditions. | If a specific laboratory error is identified and documented with evidence, the test is invalidated. Proceed to retest with the same sample preparation. |
| 3 | If no clear lab error is found, evaluate the sample integrity: Was it collected correctly? Stored correctly? Is there visible damage or contamination? | If a sample integrity issue is confirmed, resample (if protocol permits) and retest. |
| 4 | If no lab error and no sample issue is found, proceed to Phase II. The OOS result stands and must be included in the investigation. | Proceed to Phase II. |

**Critical rule for Phase I**: The original OOS result is never discarded. Even if a lab error is found and confirmed, the OOS result and the Phase I investigation are documented in the OOS report. The invalidated result is retained in the record with the invalidation rationale.

### 2.2 Phase II: Full-Scale Investigation

Trigger: Phase I did not identify a laboratory cause.

Objective: Determine whether the OOS result is attributable to the manufacturing process, the product, or is a true outlier.

#### Phase II Decision Tree

```
Phase I: No lab error found
    |
    v
Assess: Is the product manufactured at this site?
    |
    +-- YES --> Manufacturing investigation
    |               |
    |               +-- Root cause identified?
    |               |       |
    |               |       +-- YES --> CAPA. Evaluate batch disposition.
    |               |       |
    |               |       +-- NO --> Retest (per protocol). Evaluate
    |               |                   trending and batch history.
    |               |
    |               +-- Impact on other batches?
    |                       |
    |                       +-- YES --> Extend investigation. Evaluate
    |                       |           stability samples from affected batches.
    |                       |
    |                       +-- NO --> Limit scope to affected batch.
    |
    +-- NO (contract testing) --> Notify manufacturing site.
                                   Coordinate investigation.
```

#### Retest Strategy

- Retesting must be pre-defined in the OOS SOP (number of retests, who performs them, acceptance criteria).
- Typical approach: 2-3 additional retests from the same sample preparation (if sufficient) or from the original sample (new preparation).
- Retest results do not "average out" the OOS result. Each result is evaluated individually.
- If all retests pass: the original OOS may be attributed to an isolated anomaly, but the investigation must still document why the anomaly occurred if possible.
- If any retest fails: confirms the OOS is not a laboratory anomaly. Proceed to batch disposition evaluation.

#### Batch Disposition Options

| Scenario | Disposition | Documentation |
|----------|------------|---------------|
| Root cause identified, batch is non-conforming | Reject | Deviation + investigation + CAPA. Assess impact on other batches. |
| Root cause identified, batch is marginal but passes re-evaluation | Conditional release (if justified) | Full investigation report. QA Head approval required. Regulatory notification if applicable. |
| Root cause not identified, retests pass, trending shows no pattern | Release with investigation | Investigation report acknowledges inconclusive root cause. Enhanced monitoring plan. |
| Root cause not identified, retests also fail | Reject | Full investigation. CAPA focuses on process investigation. |

### 2.3 OOT (Out of Trend) Framework

Trigger: A result is within specification but deviates from the established trend for that attribute.

#### OOT Trigger Criteria (set in the annual product review or stability protocol)

| Trigger Type | Criteria | Example |
|-------------|---------|---------|
| **Statistical** | Result exceeds 2sigma or 3sigma from the rolling mean of historical data | Purity result is within spec (95.0%) but is 2.5 sigma below the historical mean (98.5%) |
| **Trend-based** | 3 or more consecutive results in the same direction (trending toward specification limit) | 3 consecutive batches showing decreasing assay, each still within spec |
| **Threshold-based** | Result is within X% of specification limit | Degradation product at 2.8% vs. specification of 3.0% |
| **Change-triggered** | Any result after a significant process or material change is evaluated for trend impact | First batch after resin change shows 1% shift in charge variant profile |

#### OOT Response

1. **Alert**: Document the OOT observation. Evaluate against historical data. No immediate action required beyond documentation.
2. **Action level**: OOT with a statistically significant shift. Initiate a focused investigation (not a full deviation, but a documented assessment). May require increased monitoring frequency.
3. **Escalation**: OOT progressing toward OOS. Treat as a deviation. Initiate full investigation and CAPA.

---

## 3. Change Control Lifecycle

### 3.1 Change Classification

| Classification | Definition | Examples | Typical Approval | Timeline |
|----------------|-----------|----------|-----------------|---------|
| **Administrative** | No impact on product quality, process, or validated state. Editorial or organizational changes only. | SOP typo correction; document reformatting; organizational restructuring of document ownership | QA review only | 1-5 days |
| **Minor** | Potential minor impact on process or documentation. No impact on validated state or registered specifications. | In-process control limit tightening; training material update; equipment like-for-like replacement | QA + technical reviewer | 10-30 days |
| **Major** | Impact on process, method, or specifications. May require revalidation, comparability, or regulatory notification. | Analytical method change (different column, different buffer); raw material supplier change; process parameter range expansion | QA + technical + regulatory review. Change control board approval. | 30-90 days |
| **Critical** | Significant impact on product quality, safety, or efficacy. Requires regulatory submission and/or prior approval. | Manufacturing site change; scale change; specification widening; new drug substance process; container-closure change | Full change control board. Regulatory submission required. | 90+ days (including regulatory review) |

### 3.2 Risk-Based Assessment Approach

Every major and critical change must include a risk assessment. Use this structure:

1. **Change description**: What is changing, from what to what, and why?
2. **Scope of impact**: Which products, processes, methods, specifications, and regulatory filings are affected?
3. **Risk identification**: What could go wrong as a result of this change? Use the 6M framework (Man, Machine, Material, Method, Measurement, Milieu) to ensure comprehensive coverage.
4. **Risk evaluation**: For each identified risk, assess severity (impact on patient/quality), likelihood (probability of occurrence), and detectability (ability to detect the risk before it impacts product). Score as High/Medium/Low or use a quantitative RPN scale.
5. **Risk mitigation**: What controls, tests, or actions will reduce the risk to an acceptable level? Link each mitigation to a specific risk.
6. **Residual risk**: After mitigations, what risk remains? Is it acceptable?
7. **Regulatory impact**: Does this change require a regulatory submission? If yes, what type (PAS, CBE, AR)?

### 3.3 Pre-Approval vs. Post-Implementation Review

| Change Type | Pre-Approval Required | Post-Implementation Review |
|-------------|----------------------|---------------------------|
| **Critical** | Yes. Change cannot be implemented until regulatory approval is received (for PAS) or submission is acknowledged (for CBE). | Effectiveness verification 6-12 months after implementation. First N batches under change reviewed in detail. |
| **Major** | Yes. Internal change control board approval before execution. | Effectiveness verification defined in the change control. May include revalidation, comparability study, or enhanced monitoring. |
| **Minor** | QA approval before execution. | Confirmation of implementation. No formal effectiveness check unless specified. |
| **Administrative** | QA acknowledgment. | None. |

### 3.4 Change Effectiveness Verification

Every major and critical change control must define how effectiveness will be verified:

| Verification Type | When to Use | Example |
|------------------|-------------|---------|
| **Revalidation** | Change affects a validated process or method | 3 consecutive PPQ batches after scale change |
| **Comparability study** | Change could affect product quality attributes | Head-to-head analytical comparison of pre- and post-change batches |
| **Enhanced monitoring** | Change introduces a new risk that requires ongoing assessment | Double-frequency in-process testing for first 10 batches |
| **Stability study** | Change could affect product stability | Concurrent stability study on post-change batches alongside ongoing pre-change stability |
| **Regulatory submission** | Change requires prior approval or notification | PAS, CBE-30, CBE-0, or annual report inclusion per classification |

---

## 4. Data Integrity (ALCOA+)

### 4.1 ALCOA+ Principles

| Principle | Meaning | GMP Application |
|-----------|---------|----------------|
| **A — Attributable** | Every record entry can be traced to the person who made it, with date and time. | Signature (physical or electronic) on batch records, logbooks, and test sheets. Audit trail entries in electronic systems. |
| **L — Legible** | Records can be read and understood by any qualified reviewer, now and in the future. | Indelible ink on paper. No white-out. Single-line-through corrections with initials, date, and reason. Electronic records in readable format. |
| **C — Contemporaneous** | Records are made at the time the activity occurs, not retrospectively. | Real-time batch record entries. No "end-of-day catch-up" on logbooks. Electronic timestamps from instruments, not manual transcription. |
| **O — Original** | The first recording of the data is the original record. Copies are not originals. | Instrument printout is the original (not a handwritten transcription). Electronic raw data file is the original (not a PDF export). |
| **A — Accurate** | Data is correct, truthful, and free from error. No selective recording or reporting. | Record all results, including failed or unexpected results. No "testing into compliance." No deleting unfavorable data. |

**The "+" (Additional Principles)**:

| Principle | Meaning |
|-----------|---------|
| **Complete** | All data is recorded, including repeat or redundant tests. No data is omitted. Audit trails show all activities. |
| **Consistent** | Data entries follow a logical sequence. Timestamps are chronological. No backdating. |
| **Enduring** | Records are durable and available for their required retention period. Paper records are protected from degradation. Electronic records are backed up and migrated as systems change. |
| **Available** | Records are accessible for review throughout their retention period. Not locked in obsolete systems or lost in archived boxes without an index. |

### 4.2 Common Data Integrity Gaps in CMC

| Gap | Description | Detection Method |
|-----|-------------|-----------------|
| **Shared login credentials** | Multiple users share one login for an instrument or LIMS system. Audit trail cannot attribute actions to individuals. | Review user account management. Check for unique credentials per user. |
| **Trial injections deleted** | Analyst runs "practice" injections and deletes them before running "official" samples. | Audit trail review. Compare total injections per sequence vs. reported results. |
| **Reprocessing without documentation** | Chromatography data is reprocessed (integrated differently) without documenting the reason or preserving the original integration. | Audit trail for reprocessing events. Require electronic signature for reprocessing. |
| **Backdated entries** | Records are completed after the fact but dated as if contemporaneous. | Cross-reference timestamps from independent sources (instrument logs, building access, electronic timestamps). |
| **Selective reporting** | Only passing results are recorded; failing results are discarded without investigation. | Compare sample receipt logs to reported results. Check for gaps in sequence numbers. |
| **Uncontrolled spreadsheets** | GMP calculations performed in Excel without validation, version control, or cell protection. | Inventory all spreadsheets used in GMP activities. Validate and control those used for release decisions. |
| **Post-it note records** | Temporary paper records (sticky notes, scratch pads) used for initial data capture, then transcribed to official records with the temporary record discarded. | Observe laboratory practices. Require all GMP data to be recorded directly in controlled documents. |

### 4.3 Electronic Record Requirements

#### 21 CFR Part 11 (US FDA) / EU Annex 11

Key requirements for electronic records and signatures:

1. **Validated systems**: Computer systems used for GMP purposes must be validated for their intended use. Validation scope matches risk.
2. **Audit trail**: Electronic systems must maintain an audit trail that records the date, time, previous value, new value, and the identity of the person making each change. Audit trails cannot be disabled.
3. **Electronic signatures**: Must be unique to one individual, not shared, and must include the signer's name, date/time, and meaning (e.g., "reviewed by," "approved by," "recorded by").
4. **System access controls**: Role-based access. Users can only perform actions appropriate to their role. System administrator role is separate from data generation/review roles.
5. **Record retention and retrieval**: Electronic records must be available for the full retention period. System migration or retirement must preserve record integrity.

#### Audit Trail Expectations

| What to Look For | Acceptable | Unacceptable |
|------------------|-----------|-------------|
| Modification reason | Reason code or free-text explanation for every change | Modifications with no reason documented |
| Original value preserved | Audit trail shows previous value and new value | Audit trail overwritten or only shows final value |
| Chronological order | Entries are time-stamped and sequential | Gaps in timestamp sequence without explanation |
| User identity | Each entry attributable to a unique user | Shared accounts or generic logins |
| Tamper evidence | Audit trail cannot be edited by end users | Administrator can modify or delete audit trail entries |

---

## 5. Batch Record Review

### 5.1 What to Review

Batch record review covers these areas, in this order:

1. **Completeness**: All fields are filled. No blanks without explanation. All required signatures present.
2. **In-process controls**: Every in-process test result is within the specified range. Any excursion is documented with a deviation reference.
3. **Yield**: Step yields and overall yield are within the expected range. Unexpectedly high or low yields are investigated.
4. **Specifications**: Final release testing results meet registered specifications. OOS results are investigated.
5. **Deviations**: All deviations that occurred during the batch are closed or have an approved investigation plan. Open deviations do not prevent batch release unless they are critical and uninvestigated.
6. **Material reconciliation**: All materials are accounted for. Line clearance is documented. No unaccounted discrepancies.
7. **Equipment and facility**: Equipment used was qualified and within calibration. Room classification and environmental monitoring data are within limits.
8. **Labeling**: Product labels match the batch record and specification. Expiry date and batch number are correct.
9. **Attachments**: All required attachments (printouts, charts, labels, samples) are present and traceable to the batch.

### 5.2 Common Batch Record Deficiencies

| Deficiency | Description | Prevention |
|-----------|-------------|-----------|
| **Missing signatures** | Fields completed but not signed, or signed by unauthorized person | Pre-review checklist before QA submission |
| **Incorrect date/time** | Entries with wrong date, future date, or out-of-sequence timestamps | Real-time entry enforcement. Supervisory check during execution. |
| **Unjustified corrections** | Corrections without reason code, or reason code does not match the correction | Training on correction procedure. Periodic audits of correction patterns. |
| **Missing attachments** | Instrument printouts or chromatograms referenced but not attached | Batch record assembly checklist at end of manufacturing. |
| **Parameter recording errors** | Value recorded does not match what was set or measured | Dual verification for critical parameters. Automated data capture where feasible. |
| **Calculation errors** | Yield calculations, dilution factors, or conversions are incorrect | Automated calculations in validated systems. Independent verification for manual calculations. |
| **Incomplete line clearance** | Previous product materials not fully cleared before start | Line clearance checklist with independent verification. |
| **Ambiguous entries** | "OK," "N/A," or "as expected" used where a specific value or observation is required | SOP specifies what constitutes an acceptable entry for each field. |

### 5.3 Release Decision Framework

```
Batch Record Review Complete
    |
    v
All specifications met? -- NO --> Reject or hold pending investigation
    | YES
    v
All in-process controls met? -- NO --> Deviation investigation required.
    | YES                              Assess impact on batch quality.
    v
All deviations closed/resolved? -- NO --> QA Head decision:
    | YES                                  Hold until resolved, or
    |                                      Release with approved plan
    v
All documentation complete? -- NO --> Return for completion.
    | YES                            Cannot release incomplete record.
    v
Yield within expected range? -- NO --> Investigation required.
    | YES
    v
RELEASE by authorized person (QP or designee)
```

---

## 6. Supplier and Material Management

### 6.1 Risk-Based Supplier Classification

| Risk Tier | Definition | Examples | Qualification Requirements |
|-----------|-----------|----------|---------------------------|
| **Critical** | Material or service directly impacts product quality, safety, or efficacy. Failure is not detectable by routine incoming QC alone. | Drug substance manufacturer; sterile filters; container-closure systems; chromatography resins; GMP contract testing labs | Full audit (on-site or detailed remote). Quality agreement. Approved supplier list entry. Annual review. Change notification agreement. |
| **Major** | Material or service impacts process performance or quality attributes but failure is detectable by routine controls. | Buffer components; growth media; single-use bags; non-sterile filters; calibration services | Questionnaire-based qualification. May require on-site audit for new suppliers. Quality agreement for GMP materials. Periodic review. |
| **Minor** | Material or service has no direct quality impact. Failure has no patient safety consequence. | Office supplies; non-GMP cleaning materials; packaging for non-sterile intermediates | Approved supplier list. No formal qualification required beyond purchasing controls. |

### 6.2 Qualification Requirements by Risk Tier

#### Critical Supplier Qualification

1. **Initial assessment**: Supplier questionnaire + regulatory status review (FDA warning letters, inspection history, certifications).
2. **On-site audit**: GMP compliance assessment covering facilities, equipment, quality system, data integrity, and change control.
3. **Quality agreement**: Document defining responsibilities for change notification, deviation reporting, OOS investigation, and batch release.
4. **Material qualification**: Minimum 3 lots tested against specification before routine use. Comparability assessment for critical materials.
5. **Ongoing monitoring**: Annual supplier review. Re-audit cycle (typically every 2-3 years, or after significant change or regulatory finding).

#### Major Supplier Qualification

1. **Initial assessment**: Supplier questionnaire + reference checks.
2. **Audit decision**: Risk-based. On-site audit if supplier provides GMP materials or if questionnaire reveals concerns.
3. **Quality agreement**: Required for GMP materials.
4. **Material qualification**: Minimum 1-3 lots tested. Reduced scope compared to critical.
5. **Ongoing monitoring**: Periodic review (annual or biennial).

#### Minor Supplier Qualification

1. **Initial assessment**: Basic vendor verification (business license, reputation).
2. **No formal audit requirement**.
3. **No quality agreement required**.
4. **Purchasing controls**: Purchase orders specify requirements. Receipt inspection confirms delivery.

### 6.3 Change Notification Management

#### Incoming Change Notification Process

When a supplier notifies the site of a change to a qualified material or service:

1. **Log the notification**: Record in the supplier change log with date, supplier, material, change description, and proposed implementation date.
2. **Classify the impact**: Assess whether the change could affect product quality, process performance, or regulatory filings. Use the risk-based approach from Section 3.2.
3. **Determine response**: Accept the change, request additional data, request a delay for internal assessment, or reject the change and source alternative material.
4. **Internal change control**: If the supplier change is accepted, open an internal change control to document the assessment and any required actions (retesting, revalidation, regulatory notification).
5. **Monitor**: Track the first batches manufactured with the changed material for any impact on quality attributes.

**Critical rule**: Never implement a supplier change for a critical material without a documented impact assessment, even if the supplier says the change is "minor." The supplier's definition of "minor" may not align with yours.

---

## 7. Claude's Boundaries

This skill operates within strict boundaries. These are non-negotiable.

### What This Skill CAN Do

- Draft deviation reports, investigation summaries, and CAPA plans for human review
- Structure OOS investigation documentation using the Phase I/Phase II framework
- Design change control risk assessments and effectiveness verification plans
- Prepare batch record review checklists and deficiency tracking tables
- Draft supplier qualification documentation
- Apply ALCOA+ principles to evaluate data integrity gaps in document drafts
- Produce training materials on GMP/QA topics

### What This Skill CANNOT Do

| Boundary | Reason |
|----------|--------|
| **Approve or release batches** | Batch disposition requires authorized QP or QA designee judgment. |
| **Sign off on deviations, CAPA, or change controls** | Approval requires a named, trained individual in the quality system. |
| **Declare root cause as confirmed without human verification** | Root cause determination requires SME judgment and evidence review by qualified personnel. |
| **Generate GMP batch records for use in production** | Controlled documents must go through the document control system. |
| **Invent investigation outcomes or analytical data** | All data must come from actual test results or user-provided information. |
| **Determine regulatory reporting category as final** | Regulatory classification requires regulatory affairs review. Skill provides analysis only. |
| **Replace QP or QA Head judgment** | Skill supports decision-making; it does not make final quality decisions. |

### Mandatory Label

Every document produced by this skill must carry:

> **Draft for controlled review** — This document was generated with AI assistance and has not been reviewed or approved by authorized quality personnel. It must not be used for GMP-regulated activities until reviewed, approved, and released through the site quality system.

---

## Quick Reference: Investigation Method Selection

| Situation | Method | Why |
|-----------|--------|-----|
| Single, straightforward deviation | 5 Whys | Efficient for simple causal chains |
| Multiple potential cause areas | Ishikawa (Fishbone) | Ensures broad coverage of cause categories |
| Critical deviation, unclear cause, or regulatory scrutiny | Fault Tree Analysis | Most rigorous, demonstrates thoroughness |
| OOS with no lab error | Phase I/Phase II framework | Structured regulatory expectation |
| Trending quality attribute shift | OOT trigger criteria + trending analysis | Early detection before OOS |
| Supplier material change | Risk assessment + comparability | Risk-based approach per ICH Q9/Q10 |
