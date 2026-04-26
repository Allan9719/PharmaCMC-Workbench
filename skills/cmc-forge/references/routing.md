# CMC Routing Guide

Use this guide to pick the minimum set of files for the task.

## Route 1: Early Candidate Or Early CMC Decision

Signals:
- candidate selection
- developability
- manufacturability risk
- early Go or no-go
- IND-enabling prioritization

Load:
- `playbooks/druggability-assessment.md`
- `playbooks/early-prioritization.md`

Primary artifact:
- decision memo
- risk matrix
- stage-gate readiness note

## Route 2: Change, Transfer, Or Comparability

Signals:
- process change
- site transfer
- supplier or material change
- comparability
- PACMP
- post-approval change

Load:
- `playbooks/risk-comparability.md`
- `playbooks/compliance-continuum.md`
- `templates/change-comparability-template.md`
- `templates/tech-transfer-template.md` when transfer is involved

Primary artifact:
- change impact package
- comparability plan
- transfer work package

## Route 3: Method, Control Strategy, Or Submission Package

Signals:
- analytical lifecycle
- specifications
- control strategy
- Module 3
- quality package
- evidence map

Load:
- `references/deliverable-patterns.md`
- `templates/module3-workplan-template.md`
- any playbook that matches the product stage or risk type

Primary artifact:
- workplan
- evidence map
- missing-content tracker

## Route 3A: China / Global Filing Or Partner-Facing Package

Signals:
- CDE or NMPA
- 出海 / 国际化 / global filing
- FDA, EMA, PMDA, MAA, BLA, NDA
- bilingual package or English-facing diligence
- imported-to-domestic manufacturing transfer
- overseas MAH, CDMO, licensing, BD due diligence

Load:
- `references/china-global-cmc-operating-model.md`
- `references/regulatory-anchors.md`
- the closest template for the requested artifact

Primary artifact:
- global core package plus regional delta
- bilingual terminology table
- RA confirmation list
- evidence gap tracker

## Route 4: Training Or Knowledge System

Signals:
- onboarding
- FAQ
- curriculum
- workshop
- playbook
- article or training design

Load:
- `playbooks/content-structuring.md`
- `references/deliverable-patterns.md`

Primary artifact:
- training outline
- FAQ bank
- quick-reference guide

## Conflict Rule

If the request hits both risk/comparability and compliance/lifecycle:
1. classify the technical change and quality impact first
2. then decide the regulatory path and evidence burden

If the request hits both early prioritization and content structuring:
1. solve the technical judgment first
2. convert it into training content second

## Minimal-Load Rule

Do not read every playbook. Start with one route. Add a second route only if the first route cannot answer the task safely.
