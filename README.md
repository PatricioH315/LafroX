# LafroX — Subdocumento 10

Servicios de operación y niveles de servicio. Corrección local del 23 de noviembre de 2026 sobre la versión corporativa 1.0. Rama hija `LafroX-Subdoc10-LateX-corrigiendo`, creada desde `origin/LafroX-Subdoc10-LateX` en `3faaec7ac6ab05a2bb7c0b7187584ad59b0b81e4`.

## Entregables

- `LAFROX-Subdocumento10.pdf`: capítulo 10, servicios, dimensionamiento y niveles de servicio.
- `LAFROX-Subdocumento10-Anexos.pdf`: memoria de cálculo, indicadores, recuperación, brechas y matriz de requisitos.
- `trazabilidad/SD10_fuentes_y_brechas.md`: registro auxiliar de fuentes, versiones, localizaciones y decisiones. No sustituye un subdocumento LaTeX.
- `trazabilidad/fuentes_sd10.json`: versiones y huellas de las fuentes consultadas.
- `trazabilidad/calculos_sd10.json`: reproducción del modelo y resultados.

## Compilación y verificación

La revisión 0.5 alinea los sitios con el SD4 y amplía el dimensionamiento de soporte, los acuerdos propuestos y la medición. La trazabilidad conserva los cortes anteriores y los respaldos de la nueva revisión.

Se usa la clase corporativa heredada, sin modificaciones, y LuaLaTeX con sus fuentes y paquetes. Desde esta carpeta:

```powershell
python verificacion/comprobar_calculos.py
latexmk -lualatex -interaction=nonstopmode -halt-on-error -jobname=LAFROX-Subdocumento10 main.tex
latexmk -lualatex -interaction=nonstopmode -halt-on-error -jobname=LAFROX-Subdocumento10-Anexos anexos.tex
```

Después de compilar, ejecutar python verificacion/comprobar_entrega.py (requiere pypdf).

Revisar log, referencias, índices, folios, tablas y diagramas, y renderizar todas las páginas antes de publicar. Las bases y aclaraciones pueden consultarse en Markdown; las fuentes de subdocumentos y formularios usadas son LaTeX y sus PDF correspondientes.

## Alcance y limitaciones

La redacción reúne lo respaldado por las fuentes publicadas y reproduce las hipótesis de SD4 y T-15. El modelo no acredita abandono, resolución al primer contacto, turnos asignados ni ensayos realizados. Las brechas B-01 a B-11 requieren datos o conciliación documental; N/A indica falta de respaldo específico, no un valor cero. SD11 y SD12 son dependencias documentales del plan de operación y dotación. No se incluyen precios, firmas ni revisiones humanas no acreditadas. Este trabajo no modifica el modelo financiero ni otros subdocumentos.

## Verificación de continuidad y mesa (23-11-2026)

Se integró el trabajo local pendiente con `origin/LafroX-Subdoc10-LateX-corrigiendo`, preservando la portada y la declaración existente. El modelo compara cotas por franja y alternativas A/B/C de 13/14/15 plazas, sin atribuir su contratación. La base de 36 meses reproduce 38.246 HH de mesa del T-15. La calibración, los turnos nominales, los acuerdos y las actas de ejecución siguen requiriendo evidencia real.

Si `latexmk` no dispone de Perl, ejecutar LuaLaTeX tres veces para cada raíz, conservando sus nombres de trabajo. `verificacion/comprobar_calculos.py --sd4-audit RUTA/cobertura.json` contrasta los calendarios y las cotas calculados independientemente en SD4. La verificación de entrega actualiza las huellas de los PDF compilados; no acredita revisión humana ni ensayos en una instalación.


## Control de coherencia entre subdocumentos

Ejecutar `python verificacion/verificar_coherencia_interdocumental.py --workspace RUTA_PROYECTO --output RUTA_RESULTADO.json` con los checkouts LaTeX vigentes de SD4 y SD5 disponibles. Comprueba el motor de la Figura 1 y su XML editable, la vigencia de reparto, las citas, el alcance de restauraciones y los casos de medición del SLA. El registro `trazabilidad/cierres_interdocumentales.json` distingue criterios adoptados, límites residuales y verificación por etapa; no exige consultas al CLIENTE para decidir el diseño. Se adopta calendario SLA íntegro y reloj corrido, TLS 1.3 sin excepción automática y reserva C de mesa en los seis peaks (2.010 HH mesa y 308 HH NOC adicionales, a cargo de LafroX). La compatibilidad real, el cuadrante, la conciliación económica y los ensayos requieren su evidencia; el registro no acredita contrataciones, aprobación humana ni pruebas ejecutadas. La limitación física de RPO y la dependencia del emisor tributario se conservan explícitas.


El contraste posterior al pull de las trece ramas LaTeX está registrado en `trazabilidad/contraste_bases_subdocumentos_20261123.json`, con los commits, las bases aplicables y los efectos internos para T-12, T-15/SD12 y la oferta económica. Las decisiones se toman dentro de LafroX; no se iniciaron consultas al CLIENTE. Los PDF finales se verifican mediante los tres programas de `verificacion/`, sin atribuir pruebas en Producción ni revisión humana adicional.


Pull previo a publicación (23 de noviembre de 2026): se integró 6a037715, conservando las tablas nuevas de coordinación/guardias y distinguiendo la base T-15 de la reserva C en el relevo NOC. Se regeneró el anexo desde las fuentes combinadas para resolver el conflicto del PDF.
