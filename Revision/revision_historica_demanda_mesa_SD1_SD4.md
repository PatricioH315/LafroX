# LafroX — Auditoría histórica de la demanda de mesa

12 de octubre de 2026. Registro de trabajo; revisión de sólo lectura de entregables. No constituye cambio aprobado de cifras, dotación ni HH.

## Conclusión y rectificación

**El usuario tiene razón: había una versión anterior que diferenciaba operación estabilizada, puesta en producción y peak.** La revisión anterior se concentró en SV-06 vigente y omitió recuperar este antecedente. No corresponde presentar la solución como algo que debe inventarse desde cero.

El modelo histórico no desapareció por completo del repositorio: está en objetos Git. Fue reemplazado por otro escenario el 26 de septiembre de 2026, antes de los cambios corporativos del SD1 del 12 de octubre. Por tanto, retirar cifras contractuales de SD1 no originó la sustitución de 620 por 2.000, aunque sí retiró la tabla de capacidad reservada de la presentación empresarial.

Tampoco corresponde declarar restaurable sin validación todo el cálculo viejo: su población, calendario y cobertura tenían defectos. **La separación de escenarios es recuperable; las cifras y la plantilla de siete personas requieren revisión.**

## Alcance y método

- rama-md comprobada; ningún cambio de rama, fetch, compilación, fuente LaTeX, PDF, commit o push.
- Búsqueda del árbol vigente en SD1, SD4, SD7/T-15, SD8, Requerimientos, resúmenes y registros.
- Búsqueda Git de todas las referencias locales disponibles, incluidos objetos de las ramas LaTeX. Se inspeccionaron **50 commits** con cambios en patrones de demanda (620/contactos, 2.000/contactos, 2,5/contactos, SV-06 o S-53) en Markdown/LaTeX, más historia específica del archivo original y cambios de calendario/capacidad. No se afirma acceso a revisiones externas no registradas.
- Se distinguieron las versiones originales de copias, importaciones y regeneraciones; se cotejaron los cambios sustantivos y los documentos vigentes.
- origin/rama-md es una referencia local ya disponible, no una nueva comprobación del servidor. subdoc-4 conserva el modelo de 2.000 en el objeto Git examinado. origin/LafroX-Subdoc4-LateX disponible aquí contiene una plantilla, no el contenido SD4: no se usa como evidencia de dimensionamiento.
- Las antiguas fuentes LaTeX se leyeron desde Git, sin extraerlas al checkout Markdown.

## Cronología comprobada

| Fecha / commit | Antecedente | Qué demuestra |
|---|---|---|
| 17-09, bdfd520 | 04_arquitectura/entrega_2/texto/arquitectura_fisica.md, filas de dimensionamiento; misma tabla en fuente LaTeX original, líneas 102–103 | 620/mes en régimen; aproximadamente 1.500 en marcha blanca; 620 × 1,0 y factor 2,5 durante oleadas; +40 % septiembre; canal tradicional por autoatención. |
| 23-09, c2ac90c | Fuente original, línea 163 y síntesis línea 186 | Desarrollo explícito: 620 en régimen, **1.550** durante oleadas, 25 días, 20 % hora punta, AHT ocho minutos, dos agentes de cola; plantilla de siete distribuida por funciones. |
| 25-09, a5f6865 | Misma fuente y párrafo | Se conserva el modelo; cambios del NOC no lo sustituyen. |
| **26-09, a5e6500** | Diff de fuente original y nuevo anexo de memoria; Requerimientos/Supuestos_Dimensionamiento.md | Se retira el párrafo de 620/1.550. Se adopta (640 + 160) × 2,5 = **2.000**, conservador, AHT diez minutos, 25 % hora cargada y 22,14 días equivalentes. El supuesto S-53 declara ausencia de tasa histórica y futura recalibración. |
| 01-10, 5c5e270 | Registro de supuestos y memoria | S-53 se renombra SV-06; no es una nueva justificación causal de la tasa. |
| 07-10, 738d839 | SD4 anexo y referencias cruzadas | Se corrige límite inicial de 2.391 a 2.283 por cuello de dos agentes; tercer agente se activa con demanda medida >2.200. No se restaura régimen de 620. |
| 09-10, bcbc3b2 / antecedentes 40988a2 | Anexo 4-W.7 y planificación | Refuerzo del tercer agente incorporado desde mes 25; jornada de ese período corregida a 40 horas. |
| 10-10, 0896cae | SD4/T-15 | Aclara límite de Erlang C respecto de abandono/FCR y operación propia; conserva los 2.000 y el refuerzo. |
| 11-10, f4f2ab3 / 8900d67 LaTeX | SD1 capacidad instalada/reservada, Tabla 1.2 | SD1 reproduce capacidad condicionada 2.283/2.391 de SD4/T-15. No origina ni fundamenta la demanda. |
| 12-10, a155da3 / 3ee66ad LaTeX | Separación empresa/proyecto SD1 | Retira tabla contractual del cuerpo corporativo; quedan ocho puestos de mesa/hasta siete activos. **No altera el escenario SD4/T-15.** |

Los mensajes y diffs no acreditan por qué se decidió convertir el factor 2,5 de oleadas en tasa del escenario inicial. No atribuir esa decisión a una aprobación humana desconocida.

## Comparación de modelos

| Variable | Modelo anterior | Modelo vigente |
|---|---|---|
| Universo | ≈620 usuarios denominados internos, pero incluye transportistas externos | 640 propios + ≈160 conductores externos =800 |
| Régimen | 1 contacto/persona-mes →620 | 2,5 contactos/persona-mes →2.000, escenario conservador |
| Puesta en producción | 2,5 ×620 →1.550 | No distingue esta tasa de la base inicial |
| Septiembre | Aumento supuesto 40 % | Extiende cobertura; no se explicita en 4-W.7 un volumen mensual de contactos peak separado |
| Calendario usado para llegadas | 25 días supuestos | 22,14 días derivados de pedidos/entregas |
| Concentración de hora punta | 20 % | 25 % |
| Atención media | Ocho minutos | Diez minutos |
| Dotación | Siete por funciones: tres diurnos, uno nocturno, supervisor y dos especialistas | Siete simultáneos en punta/dos en valle; plantilla inicial siete, nueve desde mes25; dos adicionales en peaks |
| Control | Recalibración con operación real | Tickets, recalibración mensual/trimestral según texto, medición de abandono/FCR y Erlang A en T-15 |

**Qué se perdió:** la distinción explícita entre régimen y oleadas y la delimitación al menos parcial del canal tradicional. **Qué sí existe hoy:** fórmula, hipótesis de duración/distribución, dotación, capacidad y plan de medición. Por eso «no había nada» sería falso; el pendiente es justificar adecuadamente el escenario y conciliarlo, no volver a desarrollar todo el mecanismo.

## Defectos del antecedente: no restaurarlo a ciegas

1. El párrafo de usuarios antiguo suma 62 preventistas +42 conductores propios +160 externos +310 personas de centro +40 administración/gerencia +4 TI = **618**, redondeado a620. No equivale al personal propio total 640 del Caso §2.4. Usa una población parcial de usuarios, no necesariamente inválida, pero sin justificar exclusiones; llama internos a transportistas externos. Administración/comercial/soporte del Caso son184, no40; conductores propios y peonetas84, no42. No sumar estas categorías otra vez al total640.
2. Las tasas 1,0 y2,5 y aumento40 % eran supuestos. La existencia del texto antiguo no prueba que fueran medidos ni que todas las personas contacten una vez por mes. El Caso §14.2 permite estimación explícita; no obliga a inventar historial real.
3. Los25 días históricos también eran supuestos. Los22,14 actuales pertenecen al despacho, no al calendario real 04:00–22:00 lunes–sábado de la mesa. T-15 sí calcula HH con calendario real; por tanto hay una base mejor ya disponible para conciliar llegadas y cobertura.
4. El cálculo de dos agentes viejo sólo acredita su cola **en régimen bajo esos parámetros**, no oleadas ni septiembre. Reproducción exacta: λ=620÷25×0,20=4.960/h; μ=60÷8=7,5/h; dos agentes producen SL20≈84.46 %. Con oleadas λ=12,4/h, dos agentes producen SL20≈26.25 %, por debajo80 %. Si además se aplica +40 %, λ=17,36/h supera la capacidad bruta de dos agentes (15/h): cola inestable en ese supuesto. No convertir esta sensibilidad en nueva previsión aprobada.
5. Siete personas antiguas incluyen supervisor y especialistas L2; siete posiciones simultáneas actuales son otra cosa. No intercambiar ambos «siete» ni considerar disponibles todos los perfiles a la vez sin cuadrante, relevos y descansos.
6. Autoatención del canal tradicional es mecanismo de reducción, no prueba de demanda cero para todo problema de acceso, seguridad o fallo del portal. Clientes/proveedores/transportistas requieren frontera de soporte explícita; no sumar14.200 automáticamente.

## Resolución sustentada en lo recuperado, todavía no aplicada

Recuperar **el método anterior de escenarios**, no copiar sus números: régimen estabilizado; oleadas/marcha blanca; septiembre/diciembre; crecimiento. Definir población usuaria de soporte y consultas incluidas, con tasas declaradas por escenario. Puede estudiarse conservar 2.000 como escenario alto de implantación, pero no presentarlo como tasa normal validada ni afirmar que el antecedente lo demuestra.

Usar el calendario y las franjas que T-15 ya contiene. Recalcular por escenario AHT, hora punta y resto; dimensionar puestos simultáneos y plantilla por separado. No imponer reducción de HH ni declarar innecesario el tercer agente sin comprobar cola/servicio/turnos. Alinear cuerpo SD4, tabla de dimensiones, 4-W.7/SV-06, planificación T-15 y riesgo de capacidad SD8 con una decisión autorizada.

La observación24 del SD1 sigue Parcial: separarla en capacidad corporativa (puestos/personas/turnos) y dimensionamiento del contrato. El historial no cierra por sí solo ninguno. No reinsertar el desarrollo contractual completo como presentación de LafroX.

## Evidencias reproducibles

Fuente original: SUBDOCUMENTO_4/Subdocumento_4_LateX/04_arquitectura_fisica/partes/12_k_dimensionamiento.tex. Leer con git show c2ac90c:ruta, git show a5f6865:ruta; comparar git show a5e6500 -- ruta.
SHA-256 del contenido histórico c2ac90c (texto UTF-8 leído): 16f1182486fd6078c9fadad5307ef928a43ab498e8c0d39355f7532ddea0c193.

### Commits con cambios en patrones, todas las referencias locales

- d2f100e 2026-10-12 subdoc 1,2,3
- 4214540 2026-10-12 docs(sd3): synchronize LaTeX deliverables and add signature
- 58fa636 2026-10-12 fix(sd4): revierte cambios fuera de 04_arquitectura
- a798317 2026-10-12 docs(sd4): publica espejo Markdown y registros de revision
- ae4fa5a 2026-10-12 docs(sd4): publica revision de puntuacion y nomenclatura con PDF
- a155da3 2026-10-12 docs(sd1): separa presentacion corporativa y preserva trazabilidad
- 2b213df 2026-10-12 docs(sd1): separa presentacion corporativa y preserva trazabilidad
- 60b96f4 2026-10-12 index on rama-md: 2b213df docs(sd1): separa presentacion corporativa y preserva trazabilidad
- 3ee66ad 2026-10-12 docs(sd1): separa presentacion corporativa y corrige organigrama
- 8bb34f0 2026-10-11 act sub 7
- d42c58a 2026-10-11 docs(sd4): aplica aclaraciones y conserva espejo con rama-md
- a1b3b8a 2026-10-11 docs(sd4): aplica aclaraciones y alinea espejo Markdown con LaTeX
- 146f3f6 2026-10-11 psuh subdoc 1 terminado
- fd771d2 2026-10-11 docs(sd1): consolidate AI declaration and T-6
- 8900d67 2026-10-11 docs(sd1): dimensiona equipamiento y capacidad reservada de mesa
- f4f2ab3 2026-10-11 subdoc2 intentando terminarlo, terminado 1
- e3f635f 2026-10-11 Update SD7
- cf43057 2026-10-11 arreglos
- 783752c 2026-10-11 Actualizacion en proceso de subdoc 7
- 0baf246 2026-10-10 se actualizo el latex acorde a md actualizado
- 230c2bd 2026-10-10 docs: alinea Subdocumento 3 LaTeX con rama-md y rehace el T-12
- 8c3913b 2026-10-10 docs: alinea Subdocumento 4 LaTeX con rama-md (df021b9)
- bcbc3b2 2026-10-09 Alinea Subdocumento 4 Markdown con LaTeX y avance del T-12
- e151405 2026-10-09 Alinea Subdocumento 4 LaTeX con la rama Markdown
- 3ae483a 2026-10-09 Subdoc 4 para completar T-12
- 34372ee 2026-10-09 se actualizo la informacion de los latexs
- 40988a2 2026-10-09 Actualización subdoc 7 y 8
- a2f9701 2026-10-09 Intento de T-12
- 1c9788c 2026-10-08 aa
- d397c30 2026-10-07 actualización
- 78bc620 2026-10-07 docs: alinear Subdocumento 4 Markdown con LaTeX vigente
- 2ae97a7 2026-10-07 docs: regenerar Subdocumento 4 Markdown desde LaTeX (subdoc-4)
- c1f0874 2026-10-07 figuras de ambiente arregladas
- 738d839 2026-10-07 Corrige falencias interdocumentales SD1, SD3, SD4, SD6, SD7 y SD8
- 7225fe8 2026-10-06 docs: regenerar Subdocumento 4 Markdown desde LaTeX (rama-latex a422d30)
- 284048e 2026-10-05 limpieza de archivos
- 7edd6d2 2026-10-03 docs: alinear Subdocumento 4 Markdown con rama-latex
- 732a9d6 2026-10-03 correccion de coherencia
- e377a58 2026-10-01 docs: incorporar Markdown fisico y centros de datos en alvaro-md
- 76e3fd7 2026-10-01 docs: retirar Markdown fisico de rama-latex tras copiarlo a alvaro-md
- 95ed2c9 2026-10-01 MDs insertados
- 5f72650 2026-10-01 docs: consolidar arquitectura latex 4.1 4.2 y 4.3 sin cambios de contenido
- 1c6fb43 2026-10-01 creacion de mds
- 5c5e270 2026-10-01 dimensionamiento
- 09c72fa 2026-09-29 Coherencia con 4.1
- 8cb0efd 2026-09-26 Subdoc 4: copia de la última versión de Álex (Alex_LASECUELA, 3ffb1b0)
- a5e6500 2026-09-26 Actualziación dimensionamiento
- a5f6865 2026-09-25 Subdoc 4: corrige inconsistencias internas; prevalece el 4.3
- c2ac90c 2026-09-23 Actualizacion
- bdfd520 2026-09-17 comit

### Fuentes vigentes revisadas y hashes

- Bases/Caso_02_Logistica.md: 2a1ed88f764873d200b75e05bb4eed72f7e145bf46f4a545ee0619b1c7b76b88.
- 04_arquitectura/LAFROX-Subdocumento4-Anexos.md: e1bc515b3dfbed3e6e7f2393e2d435a06cef88764d39f76997937625c9f19b08.
- 04_arquitectura/LAFROX-Subdocumento4.md: 318ff780372f19b9023dd5ed8ed4945e7adfd8f3eb75a00546157083387e10ba.
- 07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-15.md: 2c709410da376ac9515a94602956a3d1f93964d27b5ccfb5015959c684bf0ab1.
- 01_presentacion_empresa/LAFROX-Subdocumento1.md: 7001f26cb939645ed5a2cf3fe0a349453acab4e4cfb9e16853fe2443c4a372ce.
