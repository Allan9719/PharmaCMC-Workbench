# Public Release Guide

This document governs what is included in and excluded from public release packages of PharmaSee CMC Workbench.

## Licensing

| Scope | License |
|-------|---------|
| Workbench overall (code, workflows, examples, evals, orchestration) | **Apache 2.0** — see [LICENSE](LICENSE) |
| Scientific Writer 5-pass audit (derived from SciWrite) | **CC BY 4.0** — see [NOTICE](NOTICE) |
| Glasman-Deal section models (summarized guidance) | **Fair use** — no redistribution of book excerpts |

## Include in Public Release

```
pharmasee-cmc-workbench/
├── LICENSE, NOTICE, ATTRIBUTION.md, PUBLIC_RELEASE.md
├── README.md, CLAUDE.md, SKILL.md, WORKBENCH.md, routing.md, .gitignore
│
├── skills/
│   ├── cmc-forge/                   Full CMC Forge skill
│   └── scientific-writer/           Public subset only (see Exclude below)
│       ├── SKILL.md, README.md, ATTRIBUTION.md
│       └── references/             (section-models.md, writing-quality.md)
│
├── knowledge/
│   └── CMC_Research/               Knowledge base (markdown only, no PDFs)
│
├── workflows/                       5 integrated workflows
├── examples/                        5 scenario examples
└── evals/                           integrated-workbench-evals.json
```

## Exclude from Public Release

| Item | Location | Reason |
|------|----------|--------|
| Private extraction notes | `skills/scientific-writer/extracted-models/` | Summarized excerpts from Glasman-Deal's copyrighted book. Excluded to respect source material rights. |
| PDF build artifacts | `knowledge/**/*.pdf` | Generated artifacts, not source. Rebuild from markdown if needed. |
| Pre-built PDF guide | `knowledge/CMC_Research/CMC_COMPREHENSIVE_GUIDE_zh.pdf` | Same as above. |
| Temporary scripts | `patch_file*.py`, `replace_lines.py` | Local editing artifacts. |
| Editor / OS files | `.vscode/`, `.idea/`, `.DS_Store`, `Thumbs.db` | Standard gitignore items. |

## How to Prepare a Release Package

```bash
# 1. Copy the repo
cp -r pharmasee-cmc-workbench/ release-package/

# 2. Remove excluded items
rm -rf release-package/skills/scientific-writer/extracted-models/
find release-package/knowledge/ -name "*.pdf" -delete

# 3. Verify no excluded items remain
find release-package/ -name "extracted-models" -type d   # should return nothing
find release-package/ -name "*.pdf"                       # should return nothing

# 4. Verify attribution files present
ls release-package/LICENSE release-package/NOTICE release-package/ATTRIBUTION.md

# 5. Archive
tar czf pharmasee-cmc-workbench-v1.0.tar.gz -C release-package/ .
```

## Attribution Requirements

When distributing a public release:

1. **Retain LICENSE** — Apache 2.0 full text must accompany the package
2. **Retain NOTICE** — Third-party attribution must be included verbatim
3. **Retain ATTRIBUTION.md** — Module-level attribution for Scientific Writer
4. **SciWrite credit** — When distributing the Scientific Writer module:
   - Original: https://github.com/labarba/sciwrite (CC BY 4.0)
   - Fork source: https://github.com/Allan9719/sci_write
   - State that changes were made
5. **Do not redistribute** Glasman-Deal book excerpts or the `extracted-models/` directory

## Regulatory Currency

Before publishing or using outputs in regulated work, review all regulatory references against official current sources:

- NMPA / CDE
- ICH
- FDA
- EMA
- Chinese Pharmacopoeia 2025 and other applicable pharmacopoeias

The bundled CMC Research module is a **local knowledge snapshot**, not a live regulatory database.

## Final Safety Check

- [ ] No private extraction notes in package
- [ ] No PDF files in package
- [ ] No temporary scripts or editor files
- [ ] LICENSE, NOTICE, ATTRIBUTION.md all present
- [ ] Workflows do not imply the model can verify data the user has not supplied
- [ ] All regulated outputs remain draft-only and require human QA/QP/RA/SME review
