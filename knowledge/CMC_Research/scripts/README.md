# scripts/ — 工具脚本

## build_master.py

**用途：** 从 `CMC_COMPREHENSIVE_GUIDE/` 下的子文档自动生成主文档 `CMC_COMPREHENSIVE_GUIDE.md`。

Plan B 架构下，各子文档是单一事实来源，主文档是自动生成的导航+概览版。

**运行：**

```bash
# 生成主文档
python scripts/build_master.py

# 检查主文档是否与子文档同步（退出码 0=同步, 1=不同步）
python scripts/build_master.py --check
```

**输出：** 覆盖 `CMC_COMPREHENSIVE_GUIDE.md`，包含：
- 目录索引（链接到各子文档）
- 各章节摘要（从子文档自动提取前 30 行）
- 文档统计（子文档数量、总行数、总字数）

**配置：** 脚本顶部的 `SECTIONS` 列表定义了子文档的加载顺序。新增子文档后需在此列表中添加条目。

**依赖：** Python 3.6+，无第三方依赖。
