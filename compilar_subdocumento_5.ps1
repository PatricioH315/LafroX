param([string]$Motor = 'lualatex', [switch]$SoloCuerpo)
$ErrorActionPreference = 'Stop'
$projectDirectory = $PSScriptRoot
$outputDirectory = Join-Path $projectDirectory '05/salida'
New-Item -ItemType Directory -Path $outputDirectory -Force | Out-Null
$sources = @(
    @{ Archivo = 'main_subdocumento_5.tex'; Nombre = 'LAFROX-Subdocumento5' },
    @{ Archivo = '05/anexos_datos.tex'; Nombre = 'LAFROX-Subdocumento5-Anexos' }
)
Push-Location $projectDirectory
try {
    foreach ($source in $sources) {
        if ($SoloCuerpo -and $source.Nombre.EndsWith('-Anexos')) { continue }
        for ($pass = 1; $pass -le 3; $pass++) {
            & $Motor '--disable-installer' '--interaction=nonstopmode' '--halt-on-error' '--file-line-error' '--recorder' "--output-directory=$outputDirectory" "--jobname=$($source.Nombre)" $source.Archivo
            if ($LASTEXITCODE -ne 0) { throw "Error compilando $($source.Archivo), pasada $pass." }
        }
        Copy-Item -LiteralPath (Join-Path $outputDirectory "$($source.Nombre).pdf") -Destination (Join-Path $projectDirectory "$($source.Nombre).pdf") -Force
    }
}
finally { Pop-Location }
