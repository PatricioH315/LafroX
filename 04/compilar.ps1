param([string]$Motor = 'lualatex')
$ErrorActionPreference = 'Stop'
$projectDirectory = $PSScriptRoot
$outputDirectory = Join-Path $projectDirectory 'salida'
$sources = @(
    @{ Archivo = 'main.tex'; Nombre = 'LAFROX-Subdocumento4' },
    @{ Archivo = 'main_logica.tex'; Nombre = 'LAFROX-Subdocumento4.1' },
    @{ Archivo = 'anexos_logica.tex'; Nombre = 'LAFROX-Subdocumento4.1-Anexos' },
    @{ Archivo = 'formulario_T11.tex'; Nombre = 'LAFROX-Formulario-T-11' },
    @{ Archivo = 'anexo_4B.tex'; Nombre = 'LAFROX-Anexo-4B' }
)
New-Item -ItemType Directory -Path $outputDirectory -Force | Out-Null
Push-Location $projectDirectory
try {
    foreach ($source in $sources) {
        for ($pass = 1; $pass -le 3; $pass++) {
            & $Motor '--interaction=nonstopmode' '--halt-on-error' '--file-line-error' '--synctex=1' '--recorder' '--output-directory=salida' "--jobname=$($source.Nombre)" $source.Archivo
            if ($LASTEXITCODE -ne 0) { throw "Error compilando $($source.Archivo), pasada $pass." }
        }
    }
}
finally { Pop-Location }
