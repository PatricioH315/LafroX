param(
    [string[]]$TargetDocuments = @('LAFROX-Subdocumento7', 'LAFROX-Subdocumento7-Anexos', 'LAFROX-Formulario-T-14', 'LAFROX-Formulario-T-15', 'LAFROX-Formulario-T-18', 'main'),
    [ValidateRange(1, 99999)][int]$FirstFolio
)
$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $taskRoot
$taskBranch = (git branch --show-current).Trim()
if ($taskBranch -ne 'LafroX-Subdoc7-LateX-CORRIGIENDO') { throw "Rama no autorizada: $taskBranch" }
$buildDirectory = Join-Path $taskRoot 'tmp/pdfs/local-20261105'
$documents = $TargetDocuments
$useFolio = $PSBoundParameters.ContainsKey('FirstFolio')
if ($useFolio) {
    $buildDirectory = Join-Path $buildDirectory "folios-desde-$FirstFolio"
    $documents = @($TargetDocuments | Where-Object { $_ -ne 'main' })
    if ($documents.Count -eq 0) { throw 'Seleccione al menos un entregable para foliar.' }
    $pdfinfo = (Get-Command pdfinfo -CommandType Application | Select-Object -First 1).Source
    $nextFolio = $FirstFolio
}
New-Item -ItemType Directory -Force -Path $buildDirectory | Out-Null
foreach ($document in $documents) {
    $inputTex = "$document.tex"
    if ($useFolio) {
        $inputTex = Join-Path $buildDirectory "$document-wrapper.tex"
        "\def\LFXprimerfolio{$nextFolio}`n\input{$document.tex}" | Set-Content -LiteralPath $inputTex -Encoding utf8
    }
    $latexOptions = @('--interaction=nonstopmode', '--halt-on-error', "--output-directory=$buildDirectory", "--jobname=$document")
    for ($pass = 1; $pass -le 3; $pass++) {
        $passLog = Join-Path $buildDirectory "$document-pass-$pass.txt"
        & lualatex @latexOptions $inputTex 2>&1 | Out-File -LiteralPath $passLog -Encoding utf8
        if ($LASTEXITCODE -ne 0) { throw "Error al compilar $document, pasada $pass. Revisar $passLog" }
        Write-Output "$document - pasada $pass correcta"
    }
    $log = Get-Content -LiteralPath (Join-Path $buildDirectory "$document.log") -Raw
    if ($log -match 'Rerun to get|Label\(s\) may have changed') {
        & lualatex @latexOptions $inputTex 2>&1 | Out-File -LiteralPath (Join-Path $buildDirectory "$document-pass-4.txt") -Encoding utf8
        if ($LASTEXITCODE -ne 0) { throw "Error en pasada final de $document" }
        Write-Output "$document - pasada de estabilización correcta"
    }
    if ($useFolio) {
        $pageCount = & $pdfinfo (Join-Path $buildDirectory "$document.pdf") | Select-String '^Pages:\s+(\d+)\s*$'
        if ($LASTEXITCODE -ne 0 -or !$pageCount) { throw "No se pudo leer la paginación de $document." }
        $lastFolio = $nextFolio + [int]$pageCount.Matches[0].Groups[1].Value - 1
        Write-Output "$document - folios $nextFolio a $lastFolio"
        $nextFolio = $lastFolio + 1
    }
}
Write-Output 'Compilación terminada. Las salidas quedan en tmp hasta su validación.'
