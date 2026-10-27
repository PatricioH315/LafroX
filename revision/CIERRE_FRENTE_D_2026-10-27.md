# LafroX — Frente D: comprobación local del 27 de octubre de 2026

## Alcance

Cambios limitados a SD3 y SD5 con sus anexos y T-12. Las diez ramas solicitadas se actualizaron en la intervención inicial. En esta continuación se corrigió la maquetación de cuatro PDF y se retiraron las notas añadidas de verificación humana, por instrucción expresa del usuario. Las declaraciones obligatorias de IA y las revisiones nominales existentes se conservan. No se inventan validaciones humanas nuevas. Publicación en las ramas LaTeX de SD3 y SD5 autorizada expresamente por el usuario; rama Markdown, documentos ajenos, clases compartidas e imágenes intactos.

## D01–D09

| Ficha | Resultado |
|---|---|
| D01 | K2 reproducible:270 RF/RNF con prioridad (180 RF,90 RNF;64 críticos,163 altos,43 medios). T-12:653 filas, incluidos374 RT y9 identificadores absorbidos/alias. No se alteran IDs de requisitos, prioridades ni estados. |
| D02 | Lote sanitario y SSCC logístico vinculados; retención térmica por unidades/cantidades expuestas y retiro por lote para todas sus unidades/destinos. Calidad dispone; conductor no libera. |
| D03 | Alcance distinguido entre42 camiones propios y54 externos. Fuente existente INT-15 para propios; posición/tiempo del C-02 para externos, con sincronización diferida. RNF-04.01 exige menos de20min por matriz diaria completa. Se mantiene cobertura contractual de seis instalaciones por RT-21.16. |
| D04 | OTIF sobre pedidos completos y a tiempo respecto de la promesa original: registro diario, evaluación mensual; mes15≥90%,mes19≥93%,mes32>95%, sin redondear para aceptar. |
| D05 | C3 febrero2027 y C7 con tres coberturas verificados. Valkey8.1 conservado; M para módulo y mesN para plazos. |
| D06 | Fuentes de figuras SD5 y citas recuperadas selectivamente del historial anterior a2f936555; propias como remisiones. Fuente sanitaria identificada en Referencias SD3. |
| D07 | M9 corregido aSD4§4.1.4.2. Destinos T-13§8.2,T-18§6.4 ySD3§3.4.3–3.4.5/Anexo3.I verificados y mantenidos. |
| D08 | Recuento de121 entidades documentadas y995 atributos, sin atributos repetidos por entidad. Se conservan609 Cumple,22 parciales y22 No cumple; no se encubren brechas con el recuento. |
| D09 | Títulos fuera del minipage exterior, párrafos de frío integrados, Tabla3.2 sintetizada por etapa en una página, fuentes e índices corregidos y Ninguno donde no hay diagramas. Maquetación comprobada en los cuatro PDF. Los dos diagramas indicados por el usuario quedan aceptados sin modificaciones y no se consideran tareas abiertas. |

## Correcciones de esta continuación

- Retirada la frase de verificación añadida y sus marcadores de los documentos finales. La revisión del usuario se comunica fuera del contenido de entrega.
- Cobertura expresada como seis instalaciones según el Caso, con parametrización por sitio. Se retiró la consulta V-01 del entregable por instrucción del usuario, conservando los demás IDs de consulta.
- Ajuste local de longtable: el espacio del pie admite contracción finita de hasta4pt en lugar de contracción infinita. Se evita el diagnóstico de división de cajas sin silenciar mensajes del motor.
- Alineación izquierda flexible en celdas, manteniendo fuente9,5pt, anchuras y estilo de la clase. Referencias del anexo SD5 alineadas a la izquierda para evitar el estiramiento alrededor de URL.
- RF-02.06: resultado esperado redactado de forma más compacta. Conserva sus seis condiciones: estados de stock y hora estimada, exclusión de tránsito del disponible hasta recepción, paso automático a físico, captura local/sincronización, movimiento ERP con reintento y disponibilidad futura diferenciada. Descripción, prioridad, etapa y estado conservados.
- PDF1.7 en el cuerpo SD3 para incorporar los PDF vectoriales originales sin aviso de versión. Los diagramas no se modificaron ni redimensionaron.

Las correcciones resuelven la causa de los avisos. No se elevaron umbrales hbadness/vbadness ni se ocultaron diagnósticos de compilación.

## Compilación e inspección

Cuatro PDF regenerados con LuaLaTeX y auxiliares/índices estabilizados. Todos terminan con salida0 y cero Overfull, Underfull, Infinite glue, referencias indefinidas, caracteres ausentes o avisos de paquetes/versión PDF. El T-12 no necesitó cambios en esta continuación y conserva su compilación previa verificada.

| PDF | Páginas | Pasadas finales | SHA256 |
|---|---:|---:|---|
|LAFROX-Subdocumento3|39|2|`120988965378761e06b2a892a59ffda9d87f36dfff956e189b2de6acde66b293`|
|LAFROX-Subdocumento3-Anexos|183|2|`591e66adae2126caa7c814bcfe090266aa21de27a47482246abb23e487903571`|
|LAFROX-Formulario-T-12|260|2|`0c855f80aca7949b5465494c8fb9a8b3eae2770a55e8d1a10a5ac6d43e86c736`|
|LAFROX-Subdocumento5|46|2|`5327500715fbc02e8987471efc132f4ded626dd33adb497dd6bb21d15e7fbca1`|
|LAFROX-Subdocumento5-Anexos|227|2|`23164995f81eea902a6aedcf2521bcacb56bf9526375b5c55ec77aceae2cca73`|

Se extrajo texto de los cuatro PDF completos y se renderizaron índices, tablas técnicas, declaraciones, fila RF-02.06, registro de cobertura, páginas representativas de los diccionarios y referencias finales. Las imágenes resultantes se inspeccionaron visualmente. No se detectan las notas retiradas ni marcadores de verificación humana en los PDF. No se reabre la revisión de los dos diagramas aceptados por el usuario.

## Reproducción

Ejecutar `python revision/recontar_k2.py` desde SD3 (o pasar rutas SD3 y SD5). El script de solo lectura imprime conteos y alias. K2 incluye fuentes declaradas, estados y ubicación. Los vacíos de procedencia no se rellenan mediante suposiciones. Archivos de control y renders: directorio QA externo `maquetacion-d-20261027`.

La compilación no sustituye las pruebas contractuales ni acredita una nueva revisión humana del contenido.
