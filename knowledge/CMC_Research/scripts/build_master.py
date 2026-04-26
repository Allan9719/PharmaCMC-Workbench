#!/usr/bin/env python3
"""
从子文档汇编 CMC_COMPREHENSIVE_GUIDE.md 主文档。

Plan B 架构：子文档为单一事实来源，主文档为自动生成的导航+概览版。

用法：
    python scripts/build_master.py          # 生成主文档
    python scripts/build_master.py --check  # 检查主文档是否与子文档同步
"""

import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDE_DIR = ROOT / "CMC_COMPREHENSIVE_GUIDE"
MASTER_FILE = ROOT / "CMC_COMPREHENSIVE_GUIDE.md"

SECTIONS = [
    {
        "title": "基础理论",
        "dir": "basic_theory",
        "files": ["ich_framework.md"],
    },
    {
        "title": "化学药 CMC",
        "dir": "small_molecule_drug",
        "files": ["api_quality.md"],
    },
    {
        "title": "生物药 CMC",
        "dir": "biologic_drug",
        "files": ["biologic_basic.md", "atmp_cmc_zh.md", "mrna_cmc_zh.md", "adc_cmc_zh.md", "oligonucleotide_cmc_zh.md"],
    },
    {
        "title": "中国 CMC 专项",
        "dir": "china_cmc_special",
        "files": ["regulatory_framework.md", "pharmacopoeia_2025.md", "cde_review_trend.md"],
    },
    {
        "title": "申报实务",
        "dir": "declaration_practice",
        "files": ["ind_cmc_zh.md", "nda_cmc_zh.md", "variation_report.md"],
    },
    {
        "title": "质量体系",
        "dir": "quality_system",
        "files": ["process_validation.md", "mah_management.md", "audit_risk.md"],
    },
    {
        "title": "跨品类专题",
        "dir": "cross_category",
        "files": ["cmc_difference.md", "frontier_checklist.md"],
    },
]


def extract_summary(content: str, max_lines: int = 30) -> str:
    """从子文档提取摘要：取第一个 H1 标题后的内容直到 H2，限制行数。"""
    lines = content.split("\n")
    result = []
    found_h1 = False
    for line in lines:
        if line.startswith("# ") and not found_h1:
            found_h1 = True
            continue
        if found_h1 and line.startswith("## "):
            break
        if found_h1:
            result.append(line)
            if len(result) >= max_lines:
                result.append("_...（详见完整文档）_\n")
                break
    return "\n".join(result).strip()


def get_word_count(content: str) -> int:
    """估算中文字数。"""
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", content))
    english_words = len(re.findall(r"[a-zA-Z]+", content))
    return chinese_chars + english_words


def build_master() -> str:
    """从子文档汇编主文档。"""
    parts = []
    total_lines = 0
    total_words = 0
    file_count = 0

    # 头部
    parts.append("# CMC 综合知识指南\n")
    parts.append(f"> 本文档由 `scripts/build_master.py` 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}。")
    parts.append("> 子文档为单一事实来源（Plan B 架构），本文档为导航概览版。\n")

    # 目录
    parts.append("## 目录\n")
    for idx, section in enumerate(SECTIONS, 1):
        dir_path = GUIDE_DIR / section["dir"]
        parts.append(f"{idx}. **{section['title']}** — `{section['dir']}/`")
        for f in section["files"]:
            file_path = dir_path / f
            if file_path.exists():
                parts.append(f"   - [{f}]({section['dir']}/{f})")
    parts.append("")

    # 各章节摘要
    for idx, section in enumerate(SECTIONS, 1):
        dir_path = GUIDE_DIR / section["dir"]
        parts.append(f"---\n")
        parts.append(f"## {idx}. {section['title']}\n")
        parts.append(f"> 来源目录：[{section['dir']}/]({section['dir']}/)\n")

        for f in section["files"]:
            file_path = dir_path / f
            if not file_path.exists():
                parts.append(f"### {f}\n")
                parts.append(f"_文件不存在：{file_path}_\n")
                continue

            content = file_path.read_text(encoding="utf-8")
            lines = content.count("\n")
            words = get_word_count(content)
            total_lines += lines
            total_words += words
            file_count += 1

            # 提取标题
            title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
            title = title_match.group(1) if title_match else f

            parts.append(f"### {title}\n")
            parts.append(f"📄 完整文档：[{f}]({section['dir']}/{f})（{lines} 行，约 {words} 字）\n")

            summary = extract_summary(content)
            if summary:
                parts.append(summary)
            parts.append("")

    # 统计
    parts.append("---\n")
    parts.append("## 文档统计\n")
    parts.append(f"| 指标 | 数值 |")
    parts.append(f"|------|------|")
    parts.append(f"| 子文档数量 | {file_count} |")
    parts.append(f"| 总行数 | {total_lines} |")
    parts.append(f"| 总字数（估算） | {total_words} |")
    parts.append(f"| 生成时间 | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} |")

    return "\n".join(parts) + "\n"


def check_sync() -> bool:
    """检查主文档是否与子文档同步。"""
    if not MASTER_FILE.exists():
        print("主文档不存在，需要构建。")
        return False

    current = MASTER_FILE.read_text(encoding="utf-8")
    fresh = build_master()

    # 提取正文（跳过时间戳）
    ts_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}(:\d{2})?"
    current_body = re.sub(ts_pattern, "", current)
    fresh_body = re.sub(ts_pattern, "", fresh)

    if current_body.strip() == fresh_body.strip():
        print("[SYNC] 主文档与子文档已同步。")
        return True
    else:
        print("[OUT-OF-SYNC] 主文档与子文档不同步，需要重新构建。")
        # 显示差异统计
        current_lines = current_body.split("\n")
        fresh_lines = fresh_body.split("\n")
        print(f"   当前主文档：{len(current_lines)} 行")
        print(f"   预期主文档：{len(fresh_lines)} 行")
        return False


def main():
    if "--check" in sys.argv:
        synced = check_sync()
        sys.exit(0 if synced else 1)
    else:
        print("正在从子文档汇编主文档...")
        master_content = build_master()
        MASTER_FILE.write_text(master_content, encoding="utf-8")
        lines = master_content.count("\n")
        print(f"[OK] 主文档已生成：{MASTER_FILE} ({lines} 行)")


if __name__ == "__main__":
    main()
