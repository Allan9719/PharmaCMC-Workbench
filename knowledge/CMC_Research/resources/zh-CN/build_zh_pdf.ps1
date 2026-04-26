# CMC 中文 PDF 编译脚本 (Safe Encoding Version)
# 前置要求：安装 Pandoc + TeX Live/MiKTeX（含 ctex 宏包）

param(
    [string]$InputFile = "CMC_COMPREHENSIVE_GUIDE.md",
    [string]$OutputFile = "CMC_COMPREHENSIVE_GUIDE_zh.pdf",
    [string]$MainFont = "SimSun",
    [string]$SansFont = "Microsoft YaHei",
    [string]$MonoFont = "Consolas"
)

$ErrorActionPreference = "Stop"

# Dependency Check
try {
    $pandocStatus = Get-Command pandoc -ErrorAction SilentlyContinue
    if (-not $pandocStatus) { throw "Pandoc not found" }
    Write-Host "[OK] Pandoc is installed." -ForegroundColor Green
}
catch {
    Write-Host "[ERROR] Please install Pandoc: https://pandoc.org/installing.html" -ForegroundColor Red
    exit 1
}

try {
    $xelatexStatus = Get-Command xelatex -ErrorAction SilentlyContinue
    if (-not $xelatexStatus) { throw "XeLaTeX not found" }
    Write-Host "[OK] XeLaTeX is installed." -ForegroundColor Green
}
catch {
    Write-Host "[ERROR] Please install TeX Live or MiKTeX." -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $InputFile)) {
    Write-Host "[ERROR] Input file not found: $InputFile" -ForegroundColor Red
    exit 1
}

Write-Host "----------------------------------------"
Write-Host "  CMC Guide PDF Build (China Edition)"
Write-Host "----------------------------------------"
Write-Host "Input: $InputFile"
Write-Host "Output: $OutputFile"
Write-Host "Wait..." -ForegroundColor Yellow

# Execute Pandoc
try {
    pandoc $InputFile `
        -o $OutputFile `
        --pdf-engine=xelatex `
        -V mainfont="$MainFont" `
        -V sansfont="$SansFont" `
        -V monofont="$MonoFont" `
        -V geometry:margin=2.5cm `
        -V fontsize=11pt `
        -V documentclass=article `
        -V CJKmainfont="$MainFont" `
        --toc `
        --toc-depth=3 `
        -N

    if (Test-Path $OutputFile) {
        Write-Host "[OK] Build Success!" -ForegroundColor Green
        $size = (Get-Item $OutputFile).Length / 1KB
        Write-Host "File saved to: $OutputFile ($([math]::Round($size, 1)) KB)"
    }
}
catch {
    Write-Host "[ERROR] Build failed. Please check your TeX installation and fonts." -ForegroundColor Red
    Write-Error $_
    exit 1
}
