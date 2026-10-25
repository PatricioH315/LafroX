# Cadena de frío — SD3, 25-10-2026

Rama: `LafroX-Subdoc3-LateX`.

RF-09.11–09.14, RNF-09.06–09.09, RNG-17, S-28, R18-03 y T-12. Catálogo 270; 279 filas con alias. Historia y retención por SSCC, disposición y compra coherentes.

Fuente técnica: brief del 24-10-2026 y solución de cadena de frío v9.4, en la rama `subdoc-4`, `00/trazabilidad/`.

Verificado: compilación LuaLaTeX de las raíces de este subdocumento, texto de PDF, revisión de páginas seleccionadas y diferencias de fuentes. Ninguna figura ni bloque figure/TikZ modificado. La declaración conserva las revisiones anteriores y registra que la ampliación no tiene revisión humana acreditada. Las pruebas físicas no se presentan como ejecutadas.

El informe interdocumental completo y su lista de figuras/pendientes están en la rama `subdoc-4`: `00/trazabilidad/IMPLEMENTACION_CADENA_FRIO_2026-10-25.md`. SD9/SD13 e Informe 3 conservan las referencias fuera de alcance documentadas allí.

## Archivos editados en esta sesión

- `.gitignore`
- `LAFROX-Formulario-T-12.pdf`
- `LAFROX-Formulario-T-12.tex`
- `LAFROX-Subdocumento3-Anexos.pdf`
- `LAFROX-Subdocumento3.pdf`
- `anexos.tex`
- `contenido.tex`
- `tablas/generador/consolidado.json`
- `tablas_anexo/criterios_aceptacion.tex`
- `tablas_anexo/exclusiones.tex`
- `tablas_anexo/reglas_negocio.tex`
- `tablas_anexo/rf_propios.tex`
- `tablas_anexo/rnf_propios.tex`
- `tablas_anexo/supuestos.tex`

## Compilaciones verificadas

- `LAFROX-Formulario-T-12`: tres pasadas correctas.
- `LAFROX-Subdocumento3-Anexos`: tres pasadas correctas.
- `LAFROX-Subdocumento3`: tres pasadas correctas.

## Cotejo correctivo T-12/T-11 — 25-10-2026

Se detectó y corrigió la atribución de compra de sensores al CLIENTE que permanecía en la introducción del T-11. En el T-12 se sustituyeron las descripciones genéricas del kit por componentes y paquetes específicos para registro de cámaras, picking, rechazo, parametrización, evidencia y disposición; se distinguió M5 Preparación de M9 y se corrigió la referencia del tiempo de andén a 3.4.3. Se actualizaron ciclo de vida, autonomía, gestión de dispositivos y referencias B-04–B-15. Se retiraron del T-11 las dos referencias bibliográficas del registrador ELA sustituido.

Este cotejo corrige la alineación documental de la ampliación. No equivale a certificar cumplimiento integral de cada fila de toda la matriz ni a acreditar cotizaciones, certificaciones o ensayos físicos.

## Revisión semántica posterior — 25-10-2026

Se completó la revisión semántica de las 653 filas del T-12 y la correspondencia de 98 recursos del T-11. El registro posterior corrige 62 filas y 27 estados: 595 Cumple, 36 Cumple parcialmente y 22 No cumple. La descripción de ninguna exigencia se alteró. El informe canónico, observación individual y CSV/JSON están en `revision/REVISION_SEMANTICA_T12_2026-10-25.md` y `revision/semantica_t12_2026-10-25/` de la rama SD3. El resumen SD4 es `00/trazabilidad/REVISION_SEMANTICA_FORMULARIOS_2026-10-25.md`. Esta revisión reconoce brechas; la compilación no acredita cumplimiento total. El diccionario contado tiene 121 entidades y 995 atributos.
