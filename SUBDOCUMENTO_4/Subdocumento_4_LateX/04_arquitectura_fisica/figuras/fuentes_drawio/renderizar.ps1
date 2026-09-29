# Exportación pendiente de ejecutar en un equipo con acceso a draw.io desktop.
$ErrorActionPreference = 'Stop'
$drawio = 'C:\Users\alexa\AppData\Local\Programs\draw.io\draw.io.exe'
$destino = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not (Test-Path -LiteralPath $drawio)) {
    throw "No se encuentra draw.io: $drawio"
}
foreach ($nombre in @('Arquitectura_Fisica_General_v2', 'Arquitectura_Fisica_Nube')) {
    $origen = Join-Path $destino "$nombre.drawio"
    $png = Join-Path $destino "$nombre.png"
    $pdf = Join-Path $destino "$nombre.pdf"
    & $drawio -x -f png -s 2 -o $png $origen
    if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $png)) {
        throw "Falló la exportación PNG: $nombre"
    }
    & $drawio -x -f pdf --crop -o $pdf $origen
    if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $pdf)) {
        throw "Falló la exportación PDF: $nombre"
    }
    Write-Output "Exportado: $nombre (PNG 2×, PDF recortado)"
}
