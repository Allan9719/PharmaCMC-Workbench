> 📖 基于 ICH Q 系列、CDE 指导原则及行业实践整理。

## 5. Drug Substance (API) — Deep Dive

### 5.1 Synthetic Route Development

**Progression from discovery to commercial:**

| Stage                          | Scale            | Characteristics                                                             |
| ------------------------------ | ---------------- | --------------------------------------------------------------------------- |
| Medicinal Chemistry Route      | mg–g             | 8-15 steps, expensive reagents, column chromatography                       |
| First-Generation Process Route | kg               | 5-10 steps, eliminate chromatography, replace exotic reagents               |
| Commercial Route               | 100 kg–multi-ton | 3-7 steps, crystallization purifications, telescoped steps, optimized yield |

**Key optimization activities:**
- **Reaction screening**: High-throughput experimentation (HTE) platforms, DoE to map parameter space
- **Solvent selection**: Replace Class 1/2 solvents with greener alternatives (2-MeTHF, ethyl acetate, iPrOH)
- **Catalyst optimization**: Reduce Pd loading to <100 ppm; develop ligand systems enabling milder conditions
- **Telescoping**: Combine consecutive steps without intermediate isolation
- **Polymorph-directed crystallization**: Seeding strategy, cooling rate, anti-solvent addition control

### 5.2 Starting Materials (ICH Q11)

Starting materials define the regulatory GMP boundary:
- Must be well-defined substances with established specifications
- Typically 3-5 synthetic steps from final API
- Commercial availability from multiple suppliers preferred
- FDA routinely pushes back on starting materials too close to the API

**Starting material specifications:** Identity (IR, NMR, or MS), assay (>95% by HPLC), specified impurities (>0.10%), residual solvents, chiral purity (if applicable, >99% ee).

### 5.3 Critical Process Parameters (CPPs) and Critical Quality Attributes (CQAs)

**Typical Drug Substance CQAs:**

| CQA                  | Typical Target     | Test Method         |
| -------------------- | ------------------ | ------------------- |
| Assay                | 98.0-102.0%        | HPLC                |
| Specified impurities | Each NMT 0.15%     | HPLC-UV/MS          |
| Total impurities     | NMT 1.0-2.0%       | HPLC                |
| Residual solvents    | Per ICH Q3C        | GC-HS               |
| Water content        | NMT 0.5% (typical) | Karl Fischer        |
| Particle size        | D90 < specified    | Laser diffraction   |
| Polymorphic form     | Confirmed Form I   | XRPD, DSC           |
| Elemental impurities | Per ICH Q3D        | ICP-MS              |
| Residual catalysts   | Pd per ICH Q3D: oral PDE = 10 ug/day (limit depends on daily dose) | ICP-MS              |
| Chiral purity        | >99.5% ee          | Chiral HPLC/SFC     |
| Microbial limits     | Per USP <61>/<62>  | Membrane filtration |

**CPP examples by reaction type:**
- **Coupling reactions**: Temperature, catalyst loading, equivalents, reaction time, inert atmosphere
- **Crystallization**: Cooling rate (°C/hour), seed loading (0.1-1.0% w/w), anti-solvent addition rate, agitation speed
- **Salt formation**: Stoichiometry, addition order, solvent system, temperature profile

### 5.4 Process Characterization

1. **Risk Assessment**: Ishikawa diagrams → FMEA scoring (severity × probability × detectability) → prioritize high-RPN parameters
2. **Screening DoE**: Fractional factorial or Plackett-Burman, 12-20 experiments per unit operation
3. **Optimization DoE**: Full factorial, central composite, or Box-Behnken to build response surface models
4. **Establish ranges**: Proven Acceptable Range (PAR) → Normal Operating Range (NOR, narrower) → Design Space (multidimensional, ICH Q8)

### 5.5 Impurity Profiling

**Classification:**
- **Process-related**: Starting material carryover, reagent/catalyst residues, by-products, intermediates
- **Degradation products**: Hydrolysis, oxidation, photodegradation, thermal degradation
- **Elemental impurities**: Per ICH Q3D class system
- **Mutagenic impurities**: Per ICH M7 — TTC of 1.5 µg/day (lifetime)

**Forced Degradation (Stress Testing) Protocol:**

| Stress Condition | Parameters                          | Duration     |
| ---------------- | ----------------------------------- | ------------ |
| Acid hydrolysis  | 0.1-1N HCl, 60-80°C                 | 1-7 days     |
| Base hydrolysis  | 0.1-1N NaOH, 60-80°C                | 1-7 days     |
| Oxidation        | 3% H₂O₂, RT-40°C                    | 1-7 days     |
| Thermal          | 60-80°C, solid state                | 1-4 weeks    |
| Photolytic       | ICH Q1B (1.2M lux-hours, 200 Wh/m²) | Per protocol |
| Humidity         | 75% RH, 40°C                        | 1-4 weeks    |

Target: 5-20% degradation to demonstrate method specificity.

### 5.6 Polymorphism and Solid-State Characterization

**Screening campaign:** Crystallization from 20-40 diverse solvents (cooling, anti-solvent, evaporation, slurry conversion), mechanical screening (grinding, ball milling), thermal screening, high-throughput automated platforms.

**Characterization techniques:**

| Technique            | Purpose                                                                |
| -------------------- | ---------------------------------------------------------------------- |
| XRPD                 | Primary polymorph identification (unique diffraction pattern per form) |
| DSC                  | Melting points, polymorphic transitions, Tg (amorphous)                |
| TGA                  | Desolvation/decomposition weight loss                                  |
| DVS                  | Hygroscopicity profiling                                               |
| Single Crystal XRD   | Definitive structure determination                                     |
| Solid-state NMR      | Polymorph distinction, disorder, amorphous content                     |
| Hot Stage Microscopy | Visual phase transition observation                                    |

**Regulatory expectation (ICH Q6A Decision Tree #4):** If polymorphism exists, drug substance specification must include polymorph identity test.

### 5.7 Reference Standards

**Primary reference standard** — characterized by:
- Quantitative NMR (qNMR) for absolute purity (traceable to SI units)
- Mass balance: Purity = 100% − impurities − water − residual solvents − inorganic content
- Multiple orthogonal techniques: HPLC, chiral HPLC, elemental analysis, spectroscopic identity
- Storage under controlled conditions (typically −20°C or 2-8°C, desiccated)
- Annual retest with defined criteria

**Working/secondary reference standards** — qualified against primary by HPLC assay, used for routine testing.

---

## 6. Drug Product — Deep Dive

### 6.1 Formulation Development Strategies

**Pre-formulation characterization:**
- Solubility: pH-solubility profile (pH 1-8), biorelevant media (FaSSIF, FeSSIF)
- BCS Classification: Class I (high sol/high perm), II (low sol/high perm), III (high sol/low perm), IV (low sol/low perm)
- pKa, Log P/Log D, intrinsic dissolution rate
- Hygroscopicity (DVS), mechanical properties (compressibility, flowability)
- Excipient compatibility (binary mixtures at 40°C/75% RH, 2-4 weeks)

**Formulation approach by BCS Class:**

| BCS Class | Challenge        | Strategy                                                                                                                               |
| --------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| I         | None major       | Standard IR tablets, direct compression                                                                                                |
| II        | Low solubility   | Amorphous solid dispersions (HME, spray drying), nanocrystals, lipid formulations, salt/cocrystal screening, cyclodextrin complexation |
| III       | Low permeability | Surfactant addition, tight disintegration control                                                                                      |
| IV        | Both             | Combination of solubility + permeability enhancement                                                                                   |

**Key excipient compatibility issues to watch:**
- Amine drugs + lactose = Maillard reaction (browning)
- Acid-sensitive APIs + alkaline excipients
- Oxidation-sensitive APIs + peroxide-containing excipients (PEG, povidone)

### 6.2 Manufacturing Processes — Oral Solids

**Direct Compression** — preferred when API has adequate flow (Carr index <25):
- Blend uniformity is primary challenge
- Stratified sampling: 10 locations × 3 samples, RSD < 5%, individuals within 90-110%

**Wet Granulation:**
- High-shear: Impeller speed, chopper speed, binder addition rate, endpoint by power consumption/torque
- Fluid bed: Inlet air temperature, spray rate, droplet size, air flow rate
- Drying: Fluid bed to LOD 1-3% w/w
- Milling: Comil screen size, impeller speed

**Dry Granulation (Roller Compaction):**
- For moisture/heat-sensitive APIs
- Roll force, gap, speed; target ribbon solid fraction 0.6-0.8

**Tableting (Rotary Press):**
- Parameters: Compression force, pre-compression, press speed (dwell time), tooling
- CQAs: Weight, hardness, thickness, friability (<1.0%), disintegration, dissolution, content uniformity
- Common defects: Capping, lamination, sticking/picking, weight variation

**Film Coating:**
- Pan coating: Inlet air temp, spray rate, pan speed, atomization pressure
- Typical weight gain: 2-4% (aesthetics/moisture), 8-15% (functional coatings)

### 6.3 Injectable Formulations

**Key considerations:**
- Sterility assurance: Terminal sterilization (121°C/15 min, preferred) vs. aseptic processing
- Tonicity: 280-310 mOsm/kg for IV
- pH: Target 3-9 for IV, ideally 5-8
- Viscosity: <20 cP for IV push, <50 cP for SC

**Formulation types:**
- **Solutions**: Co-solvents (PEG 300/400, propylene glycol), cyclodextrin complexation (Captisol, HP-β-CD)
- **Lyophilized**: Bulking agents (mannitol, glycine), cryoprotectants (sucrose, trehalose). Cycle: freezing → primary drying (below collapse temperature) → secondary drying (25-40°C, target residual moisture <1% for proteins)
- **Suspensions**: For poorly soluble IM/SC depots

### 6.4 Biologic Drug Product Formulation

- Buffer selection: Histidine (10-50 mM, preferred for mAbs), phosphate, citrate
- Stabilizers: Sucrose (1-10%), trehalose
- Surfactants: Polysorbate 20/80 (0.01-0.1%)
- High-concentration formulations (>100 mg/mL for SC): Viscosity reduction with arginine, proline
- Stress studies: Thermal, agitation, freeze-thaw, light, oxidative — monitor by SEC, CEX, CE-SDS, turbidity, sub-visible particles

### 6.5 Scale-Up

| Unit Operation         | Scale-Up Parameter             | Guidance                                        |
| ---------------------- | ------------------------------ | ----------------------------------------------- |
| Blending               | Froude number                  | Keep constant; adjust RPM by √(D_small/D_large) |
| High-shear granulation | Impeller tip speed             | Keep constant (5-10 m/s)                        |
| Fluid bed drying       | Air velocity                   | Scale by cross-sectional area                   |
| Roller compaction      | Specific roll force (kN/cm)    | Keep constant                                   |
| Tableting              | Compression force & dwell time | Match dwell time at higher speeds               |
| Film coating           | Spray rate per surface area    | Scale by pan loading                            |
| Lyophilization         | Shelf temp & chamber pressure  | Same parameters; edge/center effects increase   |

**Scale stages:** Lab (0.5-2 kg) → Pilot (10-50 kg) → Commercial (100-500+ kg)

### 6.6 Quality by Design (QbD) Workflow — ICH Q8

1. Define **QTPP** (dosage form, route, strength, pharmacokinetic target, stability)
2. Identify **CQAs** from QTPP (dissolution, assay, CU, degradants)
3. **Risk Assessment** linking material attributes and process parameters to CQAs
4. **DoE** to systematically study impacts
5. Establish **Design Space** (multidimensional region where quality is assured)
6. Define **Control Strategy** (input controls + process controls + testing)
7. **Lifecycle management** per ICH Q10/Q12

### 6.7 Process Analytical Technology (PAT)

| PAT Tool            | Application                                   | What It Measures                 |
| ------------------- | --------------------------------------------- | -------------------------------- |
| NIR spectroscopy    | Blend uniformity, moisture, coating thickness | Chemical and physical attributes |
| Raman spectroscopy  | Polymorph ID, API content                     | Molecular vibrations             |
| In-line HPLC/UPLC   | Reaction monitoring                           | Chemical composition             |
| FBRM                | Crystallization, granulation                  | Chord length distribution        |
| Acoustic emission   | Granulation endpoint                          | Sound energy                     |
| Microwave resonance | Moisture content                              | Dielectric properties            |

---

## 7. Analytical Methods — Deep Dive

### 7.1 Types of Analytical Methods in CMC

| Category               | Purpose                          | Common Methods                                                         |
| ---------------------- | -------------------------------- | ---------------------------------------------------------------------- |
| **Identity**           | Confirm correct molecule         | IR, UV, HPLC retention time, MS, specific rotation                     |
| **Assay (Strength)**   | Quantitate active ingredient     | HPLC (UV, RI), UV spectrophotometry                                    |
| **Purity**             | Detect/quantitate impurities     | HPLC, GC, CE, ICP-MS, LC-MS/MS                                         |
| **Potency**            | Measure biological activity      | Bioassays, cell-based assays (biologics)                               |
| **Physical**           | Characterize physical properties | Dissolution, particle size, hardness, friability                       |
| **Microbiology**       | Ensure microbial quality         | Sterility (USP <71>), endotoxins (USP <85>), bioburden (USP <61>/<62>) |
| **Content Uniformity** | Dose-to-dose consistency         | HPLC per USP <905>                                                     |

### 7.2 Method Development and Validation (ICH Q2(R2))

**Method development phases:**
1. **Method scouting**: Screen columns, mobile phases, detectors
2. **Method optimization**: Systematic optimization of critical method parameters (DoE approach encouraged in Q14)
3. **Method qualification**: Demonstrate fitness for purpose (sufficient for early clinical phases)
4. **Method validation**: Full ICH Q2 validation (required for NDA/BLA)
5. **Method transfer**: Transfer to QC labs at manufacturing sites
6. **Method verification**: Confirm transferred method performs adequately at receiving site

### 7.3 Compendial vs. Non-Compendial Methods

- **Compendial** (USP/Ph.Eur./JP): Standard methods in pharmacopeial monographs. Require verification, not full validation, when used as published.
- **Non-compendial**: Custom methods developed in-house. Require full ICH Q2 validation.
- **Stability-indicating methods** must resolve drug from all degradation products — demonstrated by forced degradation studies and peak purity analysis (PDA).

### 7.4 Specifications Setting (ICH Q6A/Q6B)

Specifications are justified by:
- Pharmacopeial standards
- Batch data (clinical and registration batches)
- Stability data
- Development data (process capability)
- Toxicological qualification of impurities
- Clinical relevance (e.g., dissolution linked to bioavailability)

**Release vs. stability specifications:** Release specifications are typically tighter, allowing for degradation over the shelf life. For example, assay at release might be 98.0-102.0% while the stability (shelf-life) specification is 95.0-105.0%.

### 7.5 Analytical Method Lifecycle Management (ICH Q14)

- Introduces **Analytical QbD**: Define Analytical Target Profile (ATP), identify critical method parameters, establish Analytical Design Space
- **Proven Acceptable Range (PAR)**: Operating range within which method performance is demonstrated
- Supports continuous improvement of methods within the ATP/design space without regulatory filing

### 7.6 Method Transfer and Technology Transfer

**Method transfer approaches:**
1. **Comparative testing**: Sending and receiving labs analyze same samples; statistical comparison (equivalence testing or t-test)
2. **Co-validation**: Both labs validate independently using same protocol
3. **Revalidation**: Receiving lab performs full validation
4. **Transfer waiver**: For compendial methods or simple methods (e.g., pH, KF)

**Documentation**: Transfer protocol, transfer report, acceptance criteria (typically receiving lab within ±2-3% of sending lab mean, or equivalent precision).

---

## 8. Container Closure Systems

### 8.1 Primary Packaging by Dosage Form

| Dosage Form         | Container                                 | Closure                                  | Key Considerations            |
| ------------------- | ----------------------------------------- | ---------------------------------------- | ----------------------------- |
| Oral solids         | HDPE bottles, PVC/Alu or Alu/Alu blisters | Induction-sealed caps, push-through foil | MVTR, child resistance        |
| IV solutions        | Type I borosilicate glass vials, BFS      | Bromobutyl stoppers + Al crimp           | Extractables, delamination    |
| Pre-filled syringes | Type I glass, COP                         | Bromobutyl/chlorobutyl plungers          | Silicone oil, tungsten, glue  |
| Lyophilized         | Type I glass vials                        | Lyophilization stoppers                  | Moisture ingress, CCI         |
| Biologics (mAbs)    | Type I glass, COP vials/PFS               | Fluoropolymer-coated stoppers            | Protein adsorption, particles |

### 8.2 Extractables and Leachables (E&L)

**Extractables studies** (on components under exaggerated conditions):
- Solvents: Water, saline, acidic, basic, organic (IPA, hexane)
- Methods: GC-MS (volatile organics), LC-MS/UV (non-volatiles), ICP-MS (elemental), IC (inorganic), TOC
- Analytical Evaluation Threshold (AET): Based on Safety Concern Threshold — 0.15 µg/day (parenteral), 1.5 µg/day (oral solid)

**Leachables studies** (on drug product in actual container over shelf life):
- Leachables should be a subset of extractables
- Monitored at 0, 3, 6, 12, 18, 24, 36 months on stability

### 8.3 Glass vs. Polymer for Biologics

| Property           | Type I Glass                 | COP/COC                           |
| ------------------ | ---------------------------- | --------------------------------- |
| Breakage           | Risk                         | Resistant                         |
| Delamination       | Possible (FDA advisory 2011) | None                              |
| Protein adsorption | Higher                       | Lower                             |
| Moisture barrier   | Excellent                    | Lower (mitigated by SiOx coating) |
| O₂ permeability    | Very low                     | Higher                            |
| Weight             | Heavy                        | Light                             |
| Cost               | Lower                        | Higher                            |
| Extractables       | Ions                         | Organic compounds                 |

### 8.4 Container Closure Integrity (CCI)

- Critical for sterile products — maintains sterility through shelf life
- **Deterministic methods preferred** (per USP <1207>): Laser-based headspace, HVLD, vacuum decay, pressure decay
- **Probabilistic methods** (dye/microbial ingress): Being phased out
- CCI tested at initial and throughout stability

---

## 9. Stability Studies

### 9.1 Study Design (ICH Q1A-Q1E)

**Batches:** Minimum 3 batches, pilot scale or larger, representative of commercial process.

**Stability-indicating test panel (oral solid example):**

| Test                 | Frequency            |
| -------------------- | -------------------- |
| Appearance           | Every time point     |
| Assay (HPLC)         | Every time point     |
| Degradation products | Every time point     |
| Dissolution          | Every time point     |
| Water content (KF)   | Every time point     |
| Microbial limits     | Selected time points |

**For biologics, additional tests:** SEC (aggregation), CE-SDS (fragmentation), charge variants (CEX/icIEF), potency (bioassay), sub-visible particles (MFI).

### 9.2 Shelf Life Determination

1. **At filing**: 24-36 months proposed based on 12-18 months real-time + accelerated + statistical extrapolation (ICH Q1E)
2. **Extrapolation rules**: Up to 2× long-term data period or 12 months beyond, whichever is shorter — only if accelerated shows no significant change
3. **Post-approval**: Continue stability to cover proposed shelf life; annual batches (≥1/year/strength)

### 9.3 Stability Commitments in Submission

- Complete ongoing studies on registration batches
- Place first 3 commercial batches on stability
- Annual stability: 1 batch/year/strength/pack configuration
- Report confirmed OOS results to agency
- Shelf life extension via supplement with supporting long-term data

---
