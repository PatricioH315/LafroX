param([string]$Motor = 'lualatex', [switch]$SoloMain)
$ErrorActionPreference = 'Stop'
$projectDirectory = $PSScriptRoot
$outputDirectory = Join-Path $projectDirectory '04/salida'
$sources = @(
    @{ Archivo = 'main.tex'; Nombre = 'LAFROX-Subdocumento4'; Carpeta = '.'; Salida = '.' },
    @{ Archivo = 'main_logica.tex'; Nombre = 'LAFROX-Subdocumento4.1'; Carpeta = '.'; Salida = '.' },
    @{ Archivo = 'anexos_logica.tex'; Nombre = 'LAFROX-Subdocumento4.1-Anexos'; Carpeta = '04'; Salida = 'salida' },
    @{ Archivo = 'formulario_T11.tex'; Nombre = 'LAFROX-Formulario-T-11'; Carpeta = '04'; Salida = 'salida' },
    @{ Archivo = 'anexo_4B.tex'; Nombre = 'LAFROX-Anexo-4B'; Carpeta = '04'; Salida = 'salida' }
)
New-Item -ItemType Directory -Path $outputDirectory -Force | Out-Null
Push-Location $projectDirectory
try {
    foreach ($source in $sources) {
        if ($SoloMain -and $source.Carpeta -ne '.') { continue }
        Set-Location -LiteralPath (Join-Path $projectDirectory $source.Carpeta)
        for ($pass = 1; $pass -le 3; $pass++) {
            & $Motor '--interaction=nonstopmode' '--halt-on-error' '--file-line-error' '--synctex=1' '--recorder' "--output-directory=$($source.Salida)" "--jobname=$($source.Nombre)" $source.Archivo
            if ($LASTEXITCODE -ne 0) { throw "Error compilando $($source.Archivo), pasada $pass." }
        }
    }
}
finally { Pop-Location }
