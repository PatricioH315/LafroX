$ErrorActionPreference = 'Stop'
$root = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$file = Join-Path $root 'Presentaciones/Actualizada/LafroX - Informe 2 - numeracion Gantt y EDT ajustadas.pptx'
$app = New-Object -ComObject PowerPoint.Application
$p = $app.Presentations.Open($file, -1, 0, 0)
try {
    if ($p.Slides.Count -ne 51) { throw 'Wrong slide count' }
    foreach ($i in 1..51) {
        $p.Slides.Item($i).Export((Join-Path $PSScriptRoot "after-$i.png"), 'PNG', 1600, 900)
    }
    $transitions = foreach ($i in 22..31) {
        [PSCustomObject]@{ Slide=$i; Effect=$p.Slides.Item($i).SlideShowTransition.EntryEffect; Duration=$p.Slides.Item($i).SlideShowTransition.Duration }
    }
    $transitions | ConvertTo-Json | Set-Content -Encoding utf8 (Join-Path $PSScriptRoot 'powerpoint-transitions.json')
    $preview = Join-Path $PSScriptRoot 'edt-preview.pptx'
    $p.SaveCopyAs($preview)
} finally {
    $p.Close()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($p) | Out-Null
}
$p = $app.Presentations.Open($preview, 0, 0, 0)
try {
    for ($i = $p.Slides.Count; $i -ge 32; $i--) { $p.Slides.Item($i).Delete() }
    for ($i = 21; $i -ge 1; $i--) { $p.Slides.Item($i).Delete() }
    $p.Save()
    $video = Join-Path $PSScriptRoot 'edt-preview.mp4'
    $p.CreateVideo($video, $false, 2, 720, 24, 75)
    $deadline = (Get-Date).AddMinutes(8)
    do {
        Start-Sleep -Seconds 3
        $status = $p.CreateVideoStatus
        if ((Get-Date) -gt $deadline) { throw 'Video rendering timed out' }
    } while ($status -eq 1 -or $status -eq 2)
    if ($status -ne 3) { throw "Video rendering failed: $status" }
    "PowerPoint rendered all 51 slides and EDT Morph preview: $video"
} finally {
    $p.Close()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($p) | Out-Null
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($app) | Out-Null
}
