---
name: xlsx
description: Procesar planillas Excel de requerimientos, volumetría, oferta económica (CLP/UF/USD) y flujo de caja del proyecto TFEP-01/2026. Use cuando haya que leer, consolidar, calcular o generar archivos .xlsx/.csv (catálogos RF/RNF/Bases, planilla de consultas Art. 43.3, flujo de caja mensual). Trigger: "excel", "xlsx", "csv de requerimientos", "flujo de caja", "formulario T", "planilla".
---

# xlsx — Planillas Excel del proyecto

Proceso de lectura y cálculo de los archivos Excel/CSV asociados a la licitación
TFEP-01/2026 (Caso 02 Logística). Aplica a: catálogos de requerimientos
(`Requerimientos/`), planilla de consultas al mandante (Art. 43.3, nomenclatura
de archivos), oferta económica y flujo de caja (Informe 3, Subdoc 3 económico).

## Fuentes y datos esperados

- `Requerimientos/*.csv` — catálogos RF / RNF / Bases (separados por coma, UTF-8,
  con campos entre comillas que pueden contener comas internas).
- Planilla de consultas `.xlsx` — columnas por Art. 43.3.
- Oferta económica y flujo de caja — CLP/UF/USD, gastos de operación/inversión,
  administrativos y de recursos humanos; flujo mensual con total del mes y monto acumulado.

## Lectura robusta de CSV

No usar `-split ','` crudo (rompe campos con comas internas entre comillas). Usar
un parser estado-máquina que respete comillas dobles:

- `"` inicia campo entre comillas; `""` dentro es una comilla escapada.
- `,` fuera de comillas cierra el campo.
- Mantener codificación UTF-8 (los CSV del proyecto llevan BOM y tildes).

Ejemplo PowerShell 5.1:

```powershell
function Split-CsvLine([string]$line) {
  $r = New-Object System.Collections.Generic.List[string]; $f=[System.Text.StringBuilder]::new()
  $q=$false;$i=0
  while($i -lt $line.Length){$c=$line[$i];if($q){if($c -eq '"'){if($i+1 -lt $line.Length -and $line[$i+1] -eq '"'){[void]$f.Append('"');$i+=2;continue}else{$q=$false;$i++}}else{[void]$f.Append($c);$i++}}else{if($c -eq '"'){$q=$true;$i++}elseif($c -eq ','){$r.Add($f.ToString());[void]$f.Clear();$i++}else{[void]$f.Append($c);$i++}}}
  $r.Add($f.ToString()); return $r.ToArray()
}
```

## Catálogos de requerimientos

- **RF** (funcionales) y **RNF** (no funcionales): cada requerimiento trazable a
  su origen (párrafo, entrevista, indicador o restricción).
- **Bases (RT)**: ojo, el CSV puede intercalar RF y RNF en la misma fila física
  (columnas 0–8 y 9–17, separadores vacíos). Deduplicar por ID antes de volcar.
- Salida típica solicitada: tablas `longtable` LaTeX en el capítulo 03, o
  consolidaciones Markdown en `Requerimientos/`.

## Escapes y codificación

- Para volcar a LaTeX (pdflatex + `inputenc`), escapar caracteres no soportados:
  `−`(U+2212)→`$-$`, `≤`→`$\le$`, `≥`→`$\ge$`, `→`→`$\rightarrow$`, `×`→`$\times$`,
  `°`→`\ensuremath{^\circ}`.
- En `.xlsx`, usar formato y tipos correctos (CLP/USD con separadores de miles),
  y preservar la plantilla del CLIENTE cuando se indique.

## Cifras canónicas (usar tal cual)

14.200 clientes · 31.000 pedidos/mes · 260.000 líneas · 2,4 M unidades/mes ·
~34.000 DTE · 62 preventistas · 96 camiones (42 propios + 54 transportistas) ·
~160 conductores externos · ~120 preparadores · 310 personal CD · 68.000
canastillos / 9.400 pallets (14 % pérdida) · 1,7 % merma · OTIF 82,4 % (meta
>95 %) · fill rate 91,3 % (meta >97 %) · retiro sanitario 9 días $31 M ·
ventana 05:30–07:00 · cutover CD 24 h · terreno 14 h sin señal.

## Verificación

- Para la oferta económica: justificar cada ítem presupuestado y que sea coherente
  con el plan de actividades; el flujo debe sumar por mes y estar acumulado.
- Para requerimientos: no perder filas ni duplicar IDs al volcar catálogos.