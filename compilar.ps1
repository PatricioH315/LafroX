param([string]$Motor = 'lualatex', [switch]$SoloMain)
# Compila los tres entregables del Subdocumento 4 (aclaraciones, sección 1) en la carpeta entrega/:
#   LAFROX-Subdocumento4.pdf          cuerpo 4.1, 4.2 y 4.3
#   LAFROX-Subdocumento4-Anexos.pdf   anexos 4-A a 4-W
#   LAFROX-Formulario-T-11.pdf        formulario propio
$ErrorActionPreference = 'Continue'
$projectDirectory = $PSScriptRoot
$outputDirectory = Join-Path $projectDirectory 'entrega'
$buildDirectory = Join-Path $projectDirectory 'entrega/_build'
$sources = @(
    @{ Archivo = 'main.tex'; Nombre = 'LAFROX-Subdocumento4'; Carpeta = '.'; Salida = 'entrega/_build' },
    @{ Archivo = 'anexos_logica.tex'; Nombre = 'LAFROX-Subdocumento4-Anexos'; Carpeta = '04'; Salida = '../entrega/_build' },
    @{ Archivo = 'formulario_T11.tex'; Nombre = 'LAFROX-Formulario-T-11'; Carpeta = '04'; Salida = '../entrega/_build' }
)
New-Item -ItemType Directory -Path $buildDirectory -Force | Out-Null
Push-Location $projectDirectory
try {
    foreach ($source in $sources) {
        if ($SoloMain -and $source.Carpeta -ne '.') { continue }
        Set-Location -LiteralPath (Join-Path $projectDirectory $source.Carpeta)
        for ($pass = 1; $pass -le 3; $pass++) {
            & $Motor '--interaction=nonstopmode' '--halt-on-error' '--file-line-error' "--output-directory=$($source.Salida)" "--jobname=$($source.Nombre)" $source.Archivo 2>$null | Out-Null
            if ($LASTEXITCODE -ne 0) { throw "Error compilando $($source.Archivo), pasada $pass." }
        }
        # Se compila en entrega/_build y se copia el PDF al final, para que un visor abierto no bloquee las pasadas.
        $pdf = Join-Path $buildDirectory "$($source.Nombre).pdf"
        # Un antivirus o indexador puede retener el PDF recién escrito unos segundos: se reintenta hasta 60 s.
        $copiado = $false; $motivo = ''
        for ($try = 1; $try -le 20; $try++) {
            try { Copy-Item -LiteralPath $pdf -Destination $outputDirectory -Force -ErrorAction Stop; $copiado = $true; break }
            catch { $motivo = $_.Exception.Message; Start-Sleep -Seconds 3 }
        }
        if ($copiado) { Write-Host "OK $($source.Nombre)" }
        else { Write-Warning "$($source.Nombre): compilado en entrega/_build, pero no se pudo copiar a entrega/: $motivo" }
    }
}
finally { Pop-Location }
