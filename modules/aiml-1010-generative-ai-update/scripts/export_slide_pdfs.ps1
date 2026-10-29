# Export slide decks with speaker notes to PDF using Microsoft Print to PDF
$ErrorActionPreference = "Stop"

$moduleDefs = @(
    @{
        Key = "module_01_agentic_ai"
        Pattern = "*Agentic AI*"
        PdfName = "[Slides] Module 01 - Agentic AI Notes.pdf"
    },
    @{
        Key = "week_03_prompt_engineering_i"
        Pattern = "*Week 03*"
        PdfName = "[Slides] Week 3 - GAI Prompt 1.pdf"
    },
    @{
        Key = "week_04_prompt_engineering_ii"
        Pattern = "*Week 04*"
        PdfName = "[Slides] Week 4 - GAI Prompt 2.pdf"
    },
    @{
        Key = "week_10_transformers_llm_evolution"
        Pattern = "*Week 10*"
        PdfName = "[Slides] Week 10 - GAI Notes.pdf"
    },
    @{
        Key = "week_11_diffusion_models_text_to_image"
        Pattern = "*Week 11*"
        PdfName = "[Slides] Week 11 - GAI Notes.pdf"
    },
    @{
        Key = "week_12_pretraining_generative_ai"
        Pattern = "*Week 12*"
        PdfName = "[Slides] Week 12 - GAI Notes.pdf"
    },
    @{
        Key = "week_13_finetuning_generative_ai"
        Pattern = "*Week 13*"
        PdfName = "[Slides] Week 13 - GAI Notes.pdf"
    },
    @{
        Key = "week_15_prototyping_genai_apps"
        Pattern = "*Week 15*"
        PdfName = "[Slides] Week 15 - GAI Notes.pdf"
    },
    @{
        Key = "week_16_llm_alignment_responsible_ai"
        Pattern = "*Week 16*"
        PdfName = "[Slides] Week 16 - GAI Notes.pdf"
    }
)

$baseDir = "modules\aiml-1010-generative-ai-update\units"

# 1. Process each module
$ppt = $null
try {
    foreach ($m in $moduleDefs) {
        $folder = Get-ChildItem "ref\AIML 1010 Update\New Modules" -Directory | Where-Object { $_.Name -like $m.Pattern }
        if (-not $folder) { throw "Folder for $($m.Pattern) not found!" }

        $unitDir = Join-Path $baseDir $m.Key
        $slidesDir = Join-Path $unitDir "slides"
        if (-not (Test-Path $slidesDir)) {
            New-Item -ItemType Directory -Path $slidesDir -Force | Out-Null
        }

        $destPdf = Join-Path $slidesDir $m.PdfName

        # Check if already rendered and non-empty
        if ((Test-Path -LiteralPath $destPdf) -and (Get-Item -LiteralPath $destPdf).Length -gt 100000) {
            Write-Host "[Already Present] $destPdf ($((Get-Item -LiteralPath $destPdf).Length) bytes)"
            continue
        }

        # Check if pre-existing PDF in source folder
        $srcPdf = Get-ChildItem -LiteralPath $folder.FullName -Filter "*.pdf" | Select-Object -First 1
        if ($srcPdf) {
            Copy-Item -LiteralPath $srcPdf.FullName -Destination $destPdf -Force
            Write-Host "[Copied Source PDF] $destPdf ($((Get-Item -LiteralPath $destPdf).Length) bytes)"
            continue
        }

        # Otherwise render via PowerPoint COM
        $srcPptx = Get-ChildItem -LiteralPath $folder.FullName -Filter "*[Slides]*.pptx" | Select-Object -First 1
        if (-not $srcPptx) { throw "No slides PPTX found in $($folder.FullName)" }

        if (-not $ppt) {
            Write-Host "[PowerPoint COM] Initializing PowerPoint application..."
            $ppt = New-Object -ComObject PowerPoint.Application
        }

        $tempPptx = [System.IO.Path]::GetFullPath("temp_$($m.Key).pptx")
        Copy-Item -LiteralPath $srcPptx.FullName -Destination $tempPptx -Force

        Write-Host "[Rendering Notes PDF] $($m.Key) via PowerPoint..."
        $pres = $ppt.Presentations.Open($tempPptx, -1, 0, -1)
        try {
            $pres.PrintOptions.ActivePrinter = "Microsoft Print to PDF"
            $pres.PrintOptions.OutputType = 5 # ppPrintOutputNotesPages
            $pres.PrintOptions.PrintInBackground = $false
            $absDestPdf = [System.IO.Path]::GetFullPath($destPdf)
            $pres.PrintOut(1, $pres.Slides.Count, $absDestPdf, 1, $false)
            Write-Host "[Generated] $absDestPdf ($((Get-Item -LiteralPath $absDestPdf).Length) bytes)"
        } finally {
            $pres.Close()
            [System.Runtime.Interopservices.Marshal]::ReleaseComObject($pres) | Out-Null
            Remove-Item $tempPptx -Force -ErrorAction SilentlyContinue
        }
    }
} finally {
    if ($ppt) {
        $ppt.Quit()
        [System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
        [System.GC]::Collect()
        [System.GC]::WaitForPendingFinalizers()
    }
}

# 2. Final Verification
Write-Host "`n=== Verification: All 9 Slide Notes PDFs ==="
$allPassed = $true
foreach ($m in $moduleDefs) {
    $pdfPath = Join-Path (Join-Path $baseDir $m.Key) "slides\$($m.PdfName)"
    if (Test-Path -LiteralPath $pdfPath) {
        $len = (Get-Item -LiteralPath $pdfPath).Length
        Write-Host "PASS: $($m.Key) -> $($m.PdfName) ($len bytes)"
    } else {
        Write-Host "FAIL: Missing $pdfPath"
        $allPassed = $false
    }
}

if (-not $allPassed) {
    throw "Verification failed: not all PDFs exist."
}
Write-Host "Task 1 complete: All 9 PDFs verified!"
