param([string]$Motor = 'lualatex', [switch]$SoloMain)
# Compila los tres entregables del Subdocumento 4 (aclaraciones, sección 1):
#   LAFROX-Subdocumento4.pdf          cuerpo 4.1, 4.2 y 4.3 (raíz del proyecto)
#   LAFROX-Subdocumento4-Anexos.pdf   anexos 4-A a 4-W (04/salida)
#   LAFROX-Formulario-T-11.pdf        formulario propio (04/salida)
$ErrorActionPreference = 'Continue'
$projectDirectory = $PSScriptRoot
$outputDirectory = Join-Path $projectDirectory '04/salida'
$sources = @(
    @{ Archivo = 'main.tex'; Nombre = 'LAFROX-Subdocumento4'; Carpeta = '.'; Salida = '.' },
    @{ Archivo = 'anexos_logica.tex'; Nombre = 'LAFROX-Subdocumento4-Anexos'; Carpeta = '04'; Salida = 'salida' },
    @{ Archivo = 'formulario_T11.tex'; Nombre = 'LAFROX-Formulario-T-11'; Carpeta = '04'; Salida = 'salida' }
)
New-Item -ItemType Directory -Path $outputDirectory -Force | Out-Null
Push-Location $projectDirectory
try {
    foreach ($source in $sources) {
        if ($SoloMain -and $source.Carpeta -ne '.') { continue }
        Set-Location -LiteralPath (Join-Path $projectDirectory $source.Carpeta)
        for ($pass = 1; $pass -le 3; $pass++) {
            & $Motor '--interaction=nonstopmode' '--halt-on-error' '--file-line-error' "--output-directory=$($source.Salida)" "--jobname=$($source.Nombre)" $source.Archivo 2>$null | Out-Null
            if ($LASTEXITCODE -ne 0) { throw "Error compilando $($source.Archivo), pasada $pass." }
        }
        Write-Host "OK $($source.Nombre)"
    }
}
finally { Pop-Location }
