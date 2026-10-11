# Formato del Subdocumento 9

## Objetivo y alcance
Integrar fielmente el SD9, anexos y formularios T-13/T-17 en la plantilla común, con sus diez figuras originales. No modificar el Markdown fuente ni corregir contradicciones de contenido pendientes. Conservar clase, portada, logotipos y configuración.

## Ruta y verificación
Ruta delegada: preparación y escritura de múltiples archivos. No hay RED determinista significativo para conversión documental pasiva; se verifican conservación, compilación y PDF. Conversión generada excluida del cálculo de líneas autoradas. Estrategia ask-on-risk; sin PR, push ni commit antes de comprobación del coordinador. RDD on (global); revisión nativa responsabilidad del coordinador. Los commits de cierre están pendientes del coordinador.

## Tareas
- [x] T1 Integrar cuerpo, anexos, T-13 y T-17, metadatos y eliminar dos muestras genéricas. Evidencia: capítulo 9; cuatro fuentes, 41 tablas originales; matriz de 645 filas y siete columnas; 640 identificadores RF/RNF/RT únicos, cero ausentes; cuatro declaraciones IA y marcadores humanos conservados. Commit pendiente.
- [ ] T2 Exportar e incorporar diez diagramas originales. Exportación e incorporación realizadas: diez PDF nativos originales y 83 paneles derivados solapados; geometría original intacta. Vista general pequeña complementada por detalles de etiquetas de aproximadamente 9,7 pt o más. Aceptación de recortes y legibilidad integral pendiente por defectos visuales en algunos paneles.
- [ ] T3 Compilar y revisar visualmente. Compilación final observada exitosa, pero aceptación visual parcial: véanse defectos y siguiente paso.

## Evidencia
- Rama existente LafroX-Subdoc9-LateX; sin operaciones remotas ni commits.
- No había residuos SD8 específicos. Se eliminaron exactamente subdocumento-ejemplo/contenido.tex y subdocumento-ejemplo/tablas/ejemplo_tabla.tex, validando rutas absolutas dentro del proyecto. Las referencias legítimas a riesgos SD8 se conservaron.
- No se modificaron lafrox.cls, lafrox-portada.tex, latexmkrc, logotipos ni .gitignore.
- Primera compilación falló por límite del regex de tablas de la clase (Bad register code 65536). División en bloques de hasta 25 registros resuelta sin cambiar la clase.
- Reflujo inicial campo/valor de la matriz produjo 313 páginas. Corrección a siete columnas reales con ajuste de línea y 9,5 pt produjo 150 páginas antes de ampliar figuras.
- Exportación nativa draw.io por Start-Process oculto y espera: diez resultados exit 0.
- Una compilación obsoleta detenida dejó main.aux truncado; el reinicio falló con File ended while scanning use of @writefile. Se limpiaron sólo seis auxiliares generados con rutas comprobadas, y se recuperó la compilación.
- Último comando: latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex, exit 0; main.pdf de 236 páginas y 5885373 bytes; índices estables.
- Último log: cero advertencias Overfull, referencias indefinidas, etiquetas duplicadas o caracteres ausentes.
- Render e inspección de portada, cuerpo, vistas generales, paneles, tablas anchas, matriz, T-13, T-17 y declaración final. Las imágenes finales están en la carpeta de visualizaciones de esta conversación con prefijo final-qa.

## Defectos observados y siguiente paso
Estado parcial; no certificar PDF limpio. El panel de la página 16 recuperó su leyenda completa tras aislar el recorte en un PDF derivado. En la página 99 todavía falta visualmente el inicio izquierdo de la leyenda nativa, aunque está en la extracción de texto. Algunos encabezados de páginas de paneles están ocultos. Los cortes de bordes del diagrama son intencionales y solapados; falta auditar cobertura completa de etiquetas.

Se detuvieron nuevas correcciones después de la última corrección mecánica autorizada. El verificador independiente debe inspeccionar el PDF final, especialmente páginas 16 y 99, y decidir la corrección siguiente. No se ejecutó el posible enfoque de trasladar contenido de paneles al origen y aplicar clipping explícito equilibrado en sus streams PDF.

Observaciones menores: los metadatos repetidos del comienzo del capítulo quedaron como párrafo compacto, no con los saltos duros del Markdown. Las leyendas originales de tablas se conservan en el texto, pero los bloques de la plantilla tienen títulos genéricos y numeración correlativa adicional. Contacto y nomenclatura de entrega quedan visiblemente pendientes de confirmación. Mantener sin arreglos automáticos los hallazgos sustantivos de la revisión anterior.

## Recuperación acotada posterior
El coordinador autorizó una nueva recuperación única: renderizar los 10 PDF originales y 83 paneles derivados a PNG de 300 ppp con Poppler (-cropbox), preservar todos los PDF y cambiar sólo 93 inclusiones de diagramas en contenido.tex. Ejecutado: 93 PNG, 93 PDF preservados, 0 inclusiones de diagramas PDF. Panel de prueba nativo correcto. Compilación completa y comprobación visual posteriores pendientes. No ejecutar de nuevo convert_sd9.py sin reaplicar aislamiento PNG, pues genera inclusiones PDF. Sin cambios en texto, clase, portada o logotipos.


## Resultado de la recuperación PNG
Comando de rasterización: pdftoppm -f 1 -l 1 -cropbox -r 300 -singlefile -png; 93 resultados correctos y exactamente 93 sustituciones de inclusiones. Último build único latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex: exit 0; 236 páginas, 8553517 bytes. Advertencias comprobadas: Overfull 0, Underfull 0, referencias indefinidas/duplicadas y caracteres ausentes 0.
Se renderizaron e inspeccionaron páginas 15, 16, 17, 98, 99, 100, 149, 150, 151, 222, 223 y 224 con prefijo raster-qa en la carpeta de visualizaciones. Mejoras: página 16 recuperó encabezado y leyenda completa; página 223 recuperó encabezado y título T-17 completo. Persisten: página 99 aún no muestra el prefijo izquierdo de la leyenda; faltan encabezados en páginas 15, 17, 99, 100, 149, 150, 222 y 224. Los paneles rasterizados conservan los cortes intencionales solapados. El resultado sigue PARCIAL; no cerrar T2/T3 ni afirmar PDF limpio. La hipótesis de estado gráfico de diagramas PDF no explica de forma suficiente todos los defectos, porque algunos persisten usando sólo PNG para diagramas. Se detienen nuevas correcciones conforme al límite del coordinador.
Se conserva el intercambio: el PDF principal usa imágenes rasterizadas, no texto vectorial seleccionable de los diagramas; los 93 PDF originales/derivados se preservan para consulta. Texto fuente, clase, portada y logotipos intactos. Sin commits ni revisión nativa.

