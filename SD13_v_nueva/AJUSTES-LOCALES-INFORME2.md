# Ajustes locales del SD13 — Informe 2

Fecha: 11 de octubre de 2026. Registro interno de edición, no parte del cuerpo de la oferta.

## Alcance aplicado

Se modificaron únicamente el cuerpo, anexos y T-19 existentes del paquete SD13 en LaTeX. No se editaron otros subdocumentos, fuentes Markdown, diagramas, componentes, paquetes EDT, fechas, hardware ni metas numéricas.

- RT-26.08 se fundamenta en el beneficio temprano I-02A de INN-02. La habilitación de INN-01/03 no se presenta como ahorro demostrado.
- Las metas de reducción se identifican como propuestas de diseño y se explica el mecanismo esperado y su contraste futuro, sin inventar mediciones.
- I-05B exige interpretar correctamente las tres preguntas: al menos 20 de 24 participantes. Se armonizaron cuerpo, Anexo 13.C y T-19.
- La reutilización de hardware no se presenta como prueba de suficiencia de cómputo o almacenamiento.
- Se distingue el modelo cinético que sustenta RT-05.30 de la incorporación distribuida de INN-03. No se declara cerrado el filtro del Art. 30° ni su consistencia externa.
- La antigua Tabla 13.13 se convirtió en prosa en 13.3.2. Las tablas posteriores se renumeran automáticamente; sus etiquetas internas estables permiten resolver las referencias LaTeX locales.
- La respuesta del Anexo 13.D ya no equivale a una certificación de cierre integral del filtro de innovación.
- Se preserva el desarrollo adelantado del T-19 sin tratar su completitud final ni la valorización económica como exigencias nuevas del Informe 2. No se agregaron costos o precios.
- Se declara la intervención de Codex; se conservan las 13 celdas de revisión humana sin atribuir verificaciones ficticias.

## Dependencias aplazadas por instrucción del usuario

No se desarrolla todavía el plan transversal. Cuando estén consolidados los demás subdocumentos en LaTeX, habrá que comprobar:

1. Referencias de T-12 a la antigua Tabla 13.13 (ahora prosa en 13.3.2), a la antigua Tabla 13.16 (indicadores de INN-03, ahora 13.15) y a otras tablas posteriores. Las etiquetas internas no protegen referencias numéricas escritas manualmente en documentos externos.
2. Correspondencia SD4 ↔ responsabilidades de las innovaciones y capacidad adicional.
3. Delimitación INN-03/RT-05.30 en T-12 y SD5, incluyendo RT-18.08. El ajuste local no acredita por sí solo que el agregado cumpla el filtro de innovación.
4. Revisión humana real y firma de entrega.

El informe de revisión anterior en la carpeta `Subdoc/Revision` conserva evidencia histórica de la versión previa; sus citas literales, conteos de tablas y observaciones locales deben leerse con este registro de cambios. No se recalcula aquí una nota global ni se certifica conformidad integral.

## Verificación

Se recompilan los tres PDF del paquete y se inspecciona su representación final. El resultado automatizado queda en `validacion-ajustes-locales.json`; las imágenes de control se guardan fuera del paquete, en `Subdoc/tmp/sd13/qa-local/`.

Resultado final: cuerpo de 45 paginas, anexos de 12 y T-19 de 13. Se mantienen 6 figuras y 28 tablas en el cuerpo. Sin referencias indefinidas, desbordes horizontales ni figuras demasiado grandes. Revision visual final realizada; tipografia minima en figuras: 9,193 pt. Permanecen 13 marcadores de revision humana real.

## Precision posterior de RT-18.08

Se explicita la senal de deriva I-03B inferior al 80 % en dos cortes consecutivos de una misma familia. La referencia inicial se medira por familia durante la validacion de meses 11 a 15, con al menos 60 lotes. Periodicidad y muestra de cortes operacionales pendientes de protocolo previo a habilitacion. Armonizados cuerpo, anexo C y ficha 3 en LaTeX y Markdown. RT-18.08 externo no editado. PDFs 45/12/13 paginas; QA sin desbordes ni referencias indefinidas.


## Actualización final — bases PDF, 2026-10-11

Este estado sustituye los conteos y marcadores anteriores: cuerpo 50 páginas, anexos 12 y T-19 14; 28 tablas y 6 figuras en el cuerpo. Compilación sin desbordes, referencias indefinidas ni flotantes demasiado grandes. Contactos de todas las páginas inspeccionados.

Se incorporaron páginas impresas verificadas de Bases Administrativas y Técnicas Transversales; el Caso se cita por capítulo/entrevista, sin exigir páginas. Se normalizó Caso 2/02 a Caso o Caso Logística. Se simplificaron cinco tablas EDT, se precisó el diferencial de INN04 y se corrigió la declaración IA, con revisión humana No acreditada. No se modificaron RT-18.08, otros subdocumentos ni fuentes de diagramas. Los PNG del Markdown son renders de figuras existentes.

Mapa verificable: ../Revision/mapa_paginas_bases_SD13_2026-10-11.json. La revisión humana sigue pendiente; no se afirma admisibilidad definitiva.
