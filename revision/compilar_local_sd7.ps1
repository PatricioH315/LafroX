param([string[]]$TargetDocuments = @('LAFROX-Subdocumento7', 'LAFROX-Subdocumento7-Anexos', 'LAFROX-Formulario-T-14', 'LAFROX-Formulario-T-15', 'LAFROX-Formulario-T-18', 'main'))
$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $taskRoot
$taskBranch = (git branch --show-current).Trim()
if ($taskBranch -ne 'LafroX-Subdoc7-LateX-CORRIGIENDO') { throw "Rama no autorizada: $taskBranch" }
$buildDirectory = Join-Path $taskRoot 'tmp/pdfs/local-20261105'
New-Item -ItemType Directory -Force -Path $buildDirectory | Out-Null
$documents = $TargetDocuments
foreach ($document in $documents) {
    for ($pass = 1; $pass -le 3; $pass++) {
        $passLog = Join-Path $buildDirectory "$document-pass-$pass.txt"
        & lualatex --interaction=nonstopmode --halt-on-error "--output-directory=$buildDirectory" "$document.tex" 2>&1 | Out-File -LiteralPath $passLog -Encoding utf8
        if ($LASTEXITCODE -ne 0) { throw "Error al compilar $document, pasada $pass. Revisar $passLog" }
        Write-Output "$document - pasada $pass correcta"
    }
    $log = Get-Content -LiteralPath (Join-Path $buildDirectory "$document.log") -Raw
    if ($log -match 'Rerun to get|Label\(s\) may have changed') {
        & lualatex --interaction=nonstopmode --halt-on-error "--output-directory=$buildDirectory" "$document.tex" 2>&1 | Out-File -LiteralPath (Join-Path $buildDirectory "$document-pass-4.txt") -Encoding utf8
        if ($LASTEXITCODE -ne 0) { throw "Error en pasada final de $document" }
        Write-Output "$document - pasada de estabilización correcta"
    }
}
Write-Output 'Compilación terminada. Las salidas quedan en tmp hasta su validación.'
