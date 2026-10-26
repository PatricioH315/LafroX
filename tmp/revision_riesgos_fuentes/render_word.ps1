$ErrorActionPreference = 'Stop'
$source = (Resolve-Path -LiteralPath 'Datos externos\riesgos_conservados.docx').Path
$targetDir = Join-Path (Get-Location).Path 'tmp\revision_riesgos_fuentes\rendered'
New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
$target = Join-Path $targetDir 'riesgos_conservados.pdf'
$word = $null
$document = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $document = $word.Documents.Open($source, $false, $true)
    $document.ExportAsFixedFormat($target, 17)
    Write-Output $target
}
finally {
    if ($document -ne $null) { $document.Close(0) }
    if ($word -ne $null) { $word.Quit() }
}
