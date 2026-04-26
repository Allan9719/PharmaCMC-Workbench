# CMC Forge 项目说明

> 面向中国医药企业的 Claude Code CMC 专项 Skill，覆盖从候选分子、临床阶段、申报准备到上市后变更的结构化 CMC 工作。

## 命名说明

本项目的当前 Skill 名称为 **CMC Forge**，来自根目录 `SKILL.md` 的 front matter：

```yaml
name: cmc-forge
```

`Forge` 表示“锻造、构建、成型”。这个命名更贴近项目当前定位：不是单纯提供 CMC 知识问答，而是把零散的产品信息、工艺数据、法规要求和质量风险，锻造成可审阅、可追踪、可交付的 CMC 工作资产。

目标 GitHub 仓库仍名为 `pharmasee_CMC`，可视为早期项目名称或历史承接仓库。当前内容建议以 **CMC Forge** 作为对外展示名称，以 `pharmasee_CMC` 作为仓库地址和历史索引名称。

## 项目定位

CMC Forge 是一个 Claude Code Skill，服务于制药和生物制药企业的 CMC 工作，尤其适合中国医药企业在以下场景使用：

- CDE/NMPA 申报准备
- 中国先行、后续 FDA/EMA 国际化
- 海外品种转中国本地生产
- CDMO 技术转移和跨实体质量协作
- IND/BLA/NDA/MAA 的 Module 3 工作包规划
- 工艺验证、分析方法生命周期、可比性和上市后变更管理
- CMC 团队培训、FAQ 和知识资产沉淀

## 核心能力

### 1. DRAFT：受监管文档起草

用于起草或搭建：

- PPQ / 工艺验证方案
- Module 3 authoring workplan
- 技术转移工作包
- 变更影响评估和可比性策略
- 阶段门 readiness pack

所有可能进入受监管流程的输出均应标记为 `Draft for controlled review`，并由 CMC、QA、RA 或相关 SME 审阅。

### 2. ASSESS：风险和差距评估

用于评估：

- developability / 成药性风险
- IND 前 CMC readiness
- Phase III 或 BLA 前方法学成熟度
- 变更影响和可比性风险
- GMP/QA 体系、偏差、CAPA 或检查准备差距

评估输出推荐使用红黄绿分级、风险登记表、must-solve-now 与 can-defer 分类。

### 3. PLAN：项目和工作包规划

用于把复杂 CMC 项目拆成可执行工作包：

- 阶段门 CMC 计划
- Module 3 source-to-section map
- 技术转移里程碑和 review gates
- 中国 + 国际化 evidence roadmap
- post-approval change / PACMP / Established Conditions 工作计划

### 4. TRAIN：培训和知识资产

用于把 CMC 专家知识转成：

- 60 分钟培训大纲
- FAQ bank
- quick-reference checklist
- onboarding playbook
- 内部决策树和案例材料

## 中国企业国际化增强

当前版本重点增强了中国医药企业的国际化使用场景。新的工作模型要求把输出拆成：

1. **Global Core Package**  
   产品理解、工艺描述、控制策略、验证策略、稳定性、可比性逻辑和证据地图。

2. **China / NMPA-CDE Delta**  
   中国注册分类、CDE 沟通点、国内生产或进口路径、药典差异、中文术语和 MAH/site 责任。

3. **US / FDA Delta**  
   FDA IND/BLA/NDA 场景、工艺验证生命周期、PQ/CMC structured data、meeting package 和补充申报假设。

4. **EU / EMA Delta**  
   MAA/variation 场景、QP/site 接口、EU variation 分类和区域性质量要求。

5. **Bilingual Terminology Control**  
   对关键术语使用“中文术语 + English regulatory term + abbreviation”的方式统一定义，例如：

| 中文术语 | English Regulatory Term | 缩写 |
|----------|-------------------------|------|
| 关键质量属性 | Critical Quality Attribute | CQA |
| 关键工艺参数 | Critical Process Parameter | CPP |
| 正常操作范围 | Normal Operating Range | NOR |
| 已证明可接受范围 | Proven Acceptable Range | PAR |
| 工艺性能确认 | Process Performance Qualification | PPQ |
| 持续工艺确认 | Continued Process Verification | CPV |
| 批准后变更管理方案 | Post-Approval Change Management Protocol | PACMP |
| 既定条件 | Established Conditions | ECs |

## 项目结构

```text
cmc-forge/
├── SKILL.md
├── README.md
├── CMC_FORGE_PROJECT_NOTE.md
├── playbooks/
│   ├── compliance-continuum.md
│   ├── content-structuring.md
│   ├── druggability-assessment.md
│   ├── early-prioritization.md
│   ├── gmp-qa-principles.md
│   └── risk-comparability.md
├── references/
│   ├── china-global-cmc-operating-model.md
│   ├── deliverable-patterns.md
│   ├── gxp-boundaries.md
│   ├── project-archetypes.md
│   ├── quality-checklist.md
│   ├── regulatory-anchors.md
│   └── routing.md
├── templates/
│   ├── change-comparability-template.md
│   ├── module3-workplan-template.md
│   ├── process-validation-protocol-framework.md
│   ├── stage-gate-readiness-template.md
│   └── tech-transfer-template.md
├── examples/
└── evals/
```

## 典型使用 Prompt

```text
我们是一家中国 Biotech，单抗项目准备先走 CDE IND，同时希望两年后支持 FDA IND/Type C meeting。请帮我搭一个 China-first then global 的 CMC evidence roadmap，要求区分 global core package、CDE delta、FDA delta、双语术语表和未来 90 天行动项。
```

```text
我们准备把一个已在海外上市的生物制品转到中国本地生产，请做一版 CMC localization gap assessment，重点看技术转移、可比性、NMPA/CDE 路径假设、质量体系和数据包差距。
```

```text
请基于 biologics BLA 申报语境，先帮我把 Module 3 authoring workplan 搭起来。不要写正式 CTD 正文，先给 section map、source document inventory、missing content log 和一致性检查清单。
```

## 合规边界

CMC Forge 是起草、评估、规划和培训工具，不是质量系统或最终审批人。

它可以帮助：

- 起草受控审阅前的文档框架
- 识别 CMC 风险、缺口和证据需求
- 建立项目计划、review gates 和责任分工
- 生成培训和知识资产

它不能替代：

- QA/QP 批放行
- 偏差、CAPA 或变更控制最终批准
- GMP 记录签发
- 法规路径的最终法律判断
- SME 对工艺、分析、毒理、临床或质量结论的最终判断

## 建议维护方式

- `SKILL.md` 保持短而强，负责触发、路由和工作流。
- `playbooks/` 存放领域方法论，不写成最终模板。
- `templates/` 存放可直接输出的交付物骨架。
- `references/` 存放法规锚点、边界、路由、质量检查清单和中国/国际化工作模型。
- `evals/` 持续加入真实业务场景，尤其是 CDE/FDA/EMA 并行、技术转移、上市后变更、海外品种本地化和 BD 尽调。

## 当前推荐对外描述

**CMC Forge** is a Claude Code skill for pharmaceutical CMC work, designed to help Chinese and global biopharma teams draft regulated document frameworks, assess CMC risks and gaps, plan stage-gated work packages, and build bilingual China/global CMC evidence roadmaps.
