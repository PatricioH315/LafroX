# Aplicación de aclaraciones de IA al SD9

## Objetivo, alcance y restricciones
Aplicar §§7.1 y 7.2 a las fuentes LaTeX actuales de SD9, anexos, T-13 y T-17; conservar mejoras visuales. No inventar autoría, revisión humana, mediciones, certificaciones ni calendario. Markdown, clase y A-6 son solo lectura.

## Ruta y verificaciones
Delegada: preparación y edición de cuatro fuentes no triviales. Previsión 150-250 líneas autoradas; ask-on-risk. Documento pasivo: RED estructural, compilación y verificación visual; no test unitario aplicable. No commit: contenido preexistente no rastreado, sin frontera que permita separar su incorporación. Espejo Engram a cargo del coordinador.

## Tareas
- [x] T1 Contrastar §§7.1/7.2 y fuentes: RED observado, declaraciones Campo/Valor en lugar de una fila por sección; herramienta Codex y recomposición nativa no declaradas; T-17 carece de Referencias. Diez entradas del SD9 cubren introducción, tres secciones, cuatro anexos y dos formularios.
- [x] T2 Corregir declaraciones, ubicación y referencias, sin simular trabajo humano; preservar incertidumbres técnicas identificadas.
- [x] T3 Recompilar cuatro PDF; revisar texto, advertencias y páginas modificadas renderizadas.

## Evidencias y pendientes
Figura 9.9 contradice Tabla 9.9 y T-13. T-15 consultado fija contrato, horas y ventanas de trabajo, pero no resuelve los meses de las pruebas semestrales por nombre; no elegir arbitrariamente. Datos de portada, revisiones humanas y consolidación A-6 siguen faltantes. Afirmaciones ISO/CMMI son atribuciones del SD1, no certificaciones verificadas por esta revisión.

## Cambios aplicados
Cuatro declaraciones en tablas de seis columnas, una fila por entrada, encabezados repetidos, sin partir filas: 10/4/1/1 entradas. Claude Code conservado como historial declarado; Codex añadido por revisión y composición. Nivel Alto en texto conservado; Medio en figuras existentes recompuestas, sin inventar revisión humana. Los 16 marcadores se sustituyen por el estado explícito «Sin responsable ni verificación humana acreditados en esta versión», no por aprobación. T-17 incorpora Referencias antes de la declaración. No se ocultó la declaración ni la consolidación A-6 no acreditada.

## Comprobación parcial
SD9 compilación exit 0, 66 páginas. Declaraciones páginas 65–66 renderizadas e inspeccionadas: completas y legibles, encabezados repetidos, sin filas cortadas. Fuentes: Referencias precede declaración en las cuatro; cero marcadores editoriales de la lista §7.1d en los cuatro cuerpos. No se modificaron los datos de portada sin evidencia. Primer intento restringido MiKTeX falló RegOpenKeyExW; ejecución aprobada en curso para las otras tres raíces.

## Verificación final y siguiente paso
Cuatro latexmk -lualatex -interaction=nonstopmode -halt-on-error <raíz>.tex terminaron exit 0 con aprobación de acceso MiKTeX. PDF finales: SD9 66 páginas, anexos 96, T-13 16 y T-17 16. Cero Overfull, referencias indefinidas y caracteres ausentes en los cuatro logs; SD9 conserva un Underfull preexistente de Figura 9.2, los otros cero. Declaraciones SD9 65–66, anexos 96 y formularios 16 renderizadas e inspeccionadas: seis columnas completas, tablas legibles y sin filas partidas. Texto PDF: 10/4/1/1 estados humanos explícitos; cero [[...]], BORRADOR, INSERTAR DIAGRAMA o Anexo ??. Referencias precede declaración en las cuatro fuentes. La entrega no está certificada: requiere responsable y comprobación humana real por entrada, datos definitivos de portada, A-6, comprobación de las acreditaciones ISO/CMMI y resolución del calendario Figura 9.9 frente a Tabla 9.9/T-13. No se alteró la figura para elegir un calendario sin fundamento. Sin commit ni operación remota.
