# SD9: revisión interna y contraste con el repositorio

> Criterio aclarado por el usuario: todos estos hallazgos son errores internos de actualización del SD9. Los otros subdocumentos son las fuentes rectoras y no se modifican para conciliarlos. Este informe conserva la evidencia diagnóstica anterior a la corrección; el estado posterior se registra en ACTUALIZACION_INTERNA_SD9_2026-10-26.md.

**Conclusión de la revisión previa:** los arreglos recientes de fechas, holguras y horas son consistentes con las tablas publicadas del T-15, pero el paquete SD9 todavía contiene una contradicción de alcance por etapa, dos ambigüedades operacionales y cinco desalineaciones o referencias cruzadas que deben resolverse.

Fecha de revisión: 26-10-2026, America/Santiago. Objeto: estado local modificado del SD9, no solo HEAD `30f7bc62`. Los cuatro PDF actuales del SD9 se corresponden con esa versión local. Se actualizaron las referencias remotas con `git fetch origin --prune` antes de comparar. **No se modificó ningún entregable durante esta revisión**; solo se añadió este informe y evidencia temporal de lectura.

## Resumen priorizado

| ID | Naturaleza | Prioridad | Hallazgo |
|---|---|---|---|
| I-01 | Contradicción de alcance por etapa | Alta | H4 exige todas las integraciones y T-13 asigna el portal/EDI a pruebas E1, aunque se construyen en E2. |
| I-02 | Ambigüedad de operación y capacidad | Media | «Regresión completa» significa unas veces 1.316 casos y otras solo los 1.053 automáticos. |
| I-03 | Ambigüedad de gobierno | Media | Se permite interpretar que un acta relaja umbrales, pero las puertas se declaran sin excepciones. |
| I-04 | Desalineación cuantitativa con SD3 | Alta | Requisitos, estados RT y catálogo de casos están desactualizados. |
| I-05 | Referencia cruzada de contenido incorrecto | Alta | SD3/T-10 remiten a una matriz prueba–requisito que no aparece en las secciones indicadas del SD9/T-13. |
| I-06 | Referencia de dotación sin respaldo | Alta | Los 16 evaluadores subcontratados se atribuyen al SD6 actual, que no los declara. |
| I-07 | Inconsistencia de antecedente acreditado | Media | SD9 habla de SCAMPI A y SD1 declara evaluación Benchmark y su renovación. |
| I-08 | Métrica no homogénea entre documentos | Media | SD9/SD1 exigen 80 % global; SD6/T-10 describen 80 % sobre código modificado como si fuera la misma política. |

Las prioridades reflejan impacto en claridad, aceptación o planificación. No son un dictamen de admisibilidad ni prueban por sí mismas incumplimiento real de una solución todavía no ejecutada. Las ambigüedades se distinguen expresamente de las contradicciones comprobadas.

## 1. Coherencia interna del paquete SD9

### I-01. H4 y las pruebas E1 anticipan capacidades que el propio plan deja para E2

**Evidencia local**

- `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/T17/contenido.tex:161`, PDF T-17 p. 10: H4, mes 10, exige **15 de 15 flujos de integración sin error**.
- `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/T13/contenido.tex:164`, PDF T-13 p. 13: fija el mismo criterio genérico para integración, sin subconjunto por etapa.
- `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/T13/contenido.tex:277`, PDF p. 18: AL-CLI-01 prueba pedidos sin señal en el **Portal de Clientes instalado**, y se asigna a **3.8.1 y 3.9.1**.
- `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/T13/contenido.tex:280`, PDF p. 19: AL-STOCK-01 incluye preventa, portal y EDI, también asignado a las dos etapas.
- La tabla de pruebas del cuerpo habla del alcance E2 y de la regresión E1, pero no resuelve la obligación absoluta de 15/15 de H4. El T-13 incluye las actas de sus protocolos en el expediente H5/H10 sin distinguir cuáles existen en cada etapa.

**Por qué es una contradicción de alcance:** no basta con que un simulador de contrato esté disponible. AL-CLI-01 exige operar un portal instalado. El propio cronograma del T-13 está orientado a certificar E1 antes de construir E2, por lo que la obligación queda anticipada. Los datos del SD7 y la arquitectura confirman el desfase:

- SD7, T-14, diccionario 3.5: portales en meses 14–15, integración en mes 16.
- SD7, tabla de paquetes: 3.5.2 del 15-03 al 28-04-2028; 3.6.5 del 01-02 al 04-07-2028; 3.6.6 del 01-06 al 23-08-2028.
- SD4, apartado 4.1.4: M11, portales y canal moderno pertenecen a E2.

**Corrección propuesta:** declarar flujos y protocolos aplicables por etapa. En E1 probar las capacidades realmente construidas y, si se desea, los contratos futuros con simuladores identificados como tales; no presentarlos como aceptación del portal real. En E2 exigir el alcance completo y la regresión de E1. Mantener la cobertura final de las quince interfaces, sin eliminar obligaciones por cambiar su momento.

### I-02. La regresión completa nocturna solo dimensiona explícitamente el componente automático

**Dónde:** cuerpo `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/09_plan_calidad/contenido.tex:165,222`; `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/T13/contenido.tex:302–320`; `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/T17/contenido.tex:102`; Anexo 9.C.2 `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/09_anexos/contenido.tex:218`.

El catálogo declarado tiene 1.316 casos: 1.053 automáticos y 263 manuales. Sin embargo, cuerpo y T-13 llaman «regresión completa» al cálculo de 1.053 casos, 8,8 horas en un ejecutor o 4,4 en dos, y afirman que cabe por la noche antes de cada promoción. El T-17 exige regresión completa aprobada; el cuerpo la pide también para correcciones durante marcha blanca. Los 263 manuales se presupuestan por separado como 65,8 HH por ciclo y se ubican en los meses de certificación.

**Problema:** no queda definido si una promoción ordinaria o correctiva requiere los 263 manuales, qué subconjunto permite una selección por impacto y quién autoriza esa selección. Las horas de ejecutor no prueban cobertura ni disponibilidad del equipo manual.

**Matiz:** no se afirma que sea imposible hacer ambas partes en paralelo durante una noche; podría ser viable con personas y ventanas asignadas. Lo que falta es una regla y capacidad demostrada para el alcance realmente obligatorio.

**Corrección propuesta:** diferenciar regresión automática, selección manual por impacto y campaña completa de aceptación; fijar la evidencia requerida por tipo de promoción y el criterio de selección sin relajar los resultados obligatorios. Recalcular las cantidades después de I-04.

### I-03. No se distingue cambiar una línea base de levantar una puerta fallida

**Dónde:** cuerpo `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/09_plan_calidad/contenido.tex:110,156–165`; Anexo 9.B, `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/09_anexos/contenido.tex:164–170`.

- La sección 9.1.5 dice que el Comité de Calidad no puede relajar los umbrales **sin acta del Comité de Arquitectura**.
- Las tablas de puertas dicen que **nadie** puede levantar esos bloqueos; el texto añade que ninguna puerta admite excepciones.

**Problema:** un lector puede interpretar que el acta habilita la relajación de cualquier umbral, incluidos los exigidos contractualmente. Otra lectura es que se refiere solo al cambio formal de un umbral adicional de LafroX para versiones futuras; esa distinción no está escrita.

**Corrección propuesta:** separar el cambio formal y prospectivo de un compromiso adicional de la autorización para promover una versión fallida. Una decisión interna no sustituye una exigencia contractual ni debe convertir una prueba en falla en evidencia aprobada.

## 2. Errores internos de actualización respecto de las fuentes rectoras

### I-04. El catálogo del SD9 no coincide con el SD3/T-12 vigente

**Dónde en SD9:** cuerpo `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/09_plan_calidad/contenido.tex:222` (PDF p. 20), `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/T13/contenido.tex:302–320` (PDF p. 20), Anexo 9.C.2. La declaración IA de la sección 9.2 conserva la referencia al cálculo anterior.

**Contraste:** SD3 `33508bb3`, `contenido.tex:126–140`, y conteo directo de filas únicas del T-12:

| Magnitud | SD9/T-13 | SD3/T-12 actual |
|---|---:|---:|
| RF/RNF con prioridad propia | 262 | 270 |
| Críticos | 56 | 64 |
| Altos | 163 | 163 |
| Medios | 43 | 43 |
| Filas RF/RNF del T-12, incluidos 9 alias/absorbidos | 271 | 279 |
| RT «Cumple» | No desglosado en la tabla de casos | 324 |
| RT «Cumple parcialmente» | No desglosado en la tabla de casos | 28 |
| RT ofertados para el cálculo de casos | 356 | 352 |
| RT «No cumple» | 18 | 22 |

Se comprobaron **374 identificadores RT únicos**, sin duplicados, con suma 324 + 28 + 22. Los 279 RF/RNF del T-12 no se deben contar como 279 obligaciones independientes: el propio SD3 distingue 270 requisitos y nueve filas absorbidas/alias.

Manteniendo exactamente la regla propuesta por SD9 —5/3/2 casos según prioridad, uno por RT ofertado y siete por cada una de quince integraciones— se obtiene:

**64×5 + 163×3 + 43×2 + 352 + 15×7 = 1.352 casos**, no 1.316.

Con el mismo redondeo del reparto 80/20: aproximadamente **1.082 automáticos y 270 manuales**; unas **9,02 horas de ejecutor** automático y **67,5 HH** por ciclo manual. Son consecuencias de la regla de estimación, no casos ya diseñados ni pruebas ejecutadas. Aplicadas al escenario actual de fallas, cambian también sus 93,8/109,8 HH por evento: con 67,5 HH manuales y el resto de componentes sin cambios, serían 95,5/111,5 HH.

**Corrección propuesta:** regenerar el catálogo desde identificadores y estados vigentes; recalcular tiempos y escenarios de fallas, incluyendo trazabilidad de las nuevas capacidades de frío. No aumentar automáticamente las HH globales del proyecto ni tomar la regla 5/3/2 como un diseño exhaustivo de pruebas.

### I-05. SD3 y T-10 remiten a una matriz de pruebas que no está donde indican

**Referencias de origen**

- SD3 `contenido.tex:144` y `anexos.tex:181`: indican que las pruebas generales están en **T-13 §8.2** y en una matriz del **SD9 §9.2.5**.
- SD6/T-10 `LAFROX-Formulario-T-10.tex:35`: afirma que la matriz T-12 vincula los requisitos con su prueba.

**Contenido real del destino**

- T-13 §8.2 contiene un **conteo agregado**, no una relación identificador RF/RNF/RT → caso de prueba → criterio.
- SD9 §9.2.5 describe el método de trazabilidad, muestra un ejemplo y dice que la matriz se genera desde el repositorio; no publica la matriz requisito por requisito.
- Anexo 9.D cubre **los dieciséis resultados del caso**, no los 270 requisitos ni los 374 RT.
- El T-12 actual tiene seis columnas (ID, descripción, cumplimiento, componente, paquete EDT y sección), sin columna de caso de prueba.
- SD7 sí sitúa la matriz detallada como entregable 1.2.4/H1; esa declaración futura no es por sí sola incoherente.

**Problema:** las secciones existen, pero la remisión atribuye un contenido que no contienen. No es un error de número de sección ni prueba de que no se haya previsto trabajar la trazabilidad; es una referencia de contenido incorrecto y una cobertura que no puede auditarse individualmente con esos destinos.

**Corrección propuesta:** publicar la matriz individual si se ofrece como disponible, o corregir las remisiones para reconocer qué existe en la oferta y qué se entregará en H1. La regla de cómputo de casos no sustituye la prueba prevista de cada requisito.

### I-06. El refuerzo de 16 evaluadores diarios se atribuye a un SD6 que no lo declara

**Dónde en SD9:** cuerpo `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/09_plan_calidad/contenido.tex:288` (PDF p. 25); `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/T13/contenido.tex:430` en la tabla de roles.

SD9 afirma disponer de refuerzo de **hasta 16 evaluadores subcontratados por día**, en meses 9–12 y 16–18, y lo atribuye a **SD6 §6.1.3**. El SD6 vigente `ecc85f0b`, `subdocumento_6/contenido.tex:35–37`, trata allí adquisiciones y la condición del SOC; no declara esa dotación ni su disponibilidad o calendario. Tampoco aparece el compromiso en T-9/T-10 ni en la tabla de adquisiciones examinada. El T-15 repite la remisión a SD6, por lo que no constituye una acreditación independiente.

**Matiz:** SD9 puede proponer un refuerzo; la ausencia en SD6 no prueba que sea imposible contratarlo. Sí impide dar por respaldado el calendario mediante la cita actual.

**Corrección propuesta:** acordar el compromiso real, su responsable, horas, especialidades, fechas y forma de contratación; incluirlo en el documento correspondiente y conciliarlo con la curva T-15. Corregir la cita aun si se mantiene como supuesto pendiente.

### I-07. El antecedente CMMI no coincide con el del SD1

**Dónde:** cuerpo SD9 `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/09_plan_calidad/contenido.tex:87`, PDF p. 11.

SD9 dice que LafroX renueva una evaluación **SCAMPI A** de nivel 3. SD1 vigente `d03bf324`, `contenido.tex:227,231,351`, identifica una evaluación **Benchmark n.º 58190**, emitida en noviembre de 2023, y exige renovación mediante una nueva **Benchmark** antes de noviembre de 2026, presentada en H1.

**Problema:** la evidencia corporativa invocada no tiene la misma denominación y mecanismo de renovación. No se cuestiona aquí la autenticidad ni la validez externa del antecedente; se constata la inconsistencia entre lo que los capítulos dicen acreditar.

**Corrección propuesta:** usar el antecedente y la renovación realmente declarados por SD1, manteniendo su condición de acreditación y la presentación en H1.

### I-08. El 80 % de cobertura usa denominadores distintos

**Contraste**

- SD9, Tabla 9.4 y Anexo 9.A, 9A-31: **cobertura unitaria global ≥80 %**.
- SD1 `contenido.tex:198`: declara esa misma cobertura global como política corporativa.
- SD6 `subdocumento_6/contenido.tex:66` y T-10 `LAFROX-Formulario-T-10.tex:54`: describen **cobertura de líneas del código modificado ≥80 %**, también como política de LafroX.

**Problema:** cobertura global y cobertura de líneas modificadas no son la misma medida. Una puede cumplir y la otra fallar. No son requisitos mutuamente excluyentes —se pueden exigir ambos—, pero no se debe presentar uno como evidencia del otro o como la misma política sin distinguirlos.

**Corrección propuesta:** fijar un denominador por métrica y, si se mantienen ambos compromisos, definir dos controles independientes en las compuertas, informes y criterios de aceptación. Conservar además el control distinto de 70 % de lógica de negocio.

## 3. Lo que no reporto como error nuevo

- **Fechas y HH corregidas:** la comprobación `verificar_alineacion_sd7.py origin/LafroX-Subdoc7-LateX` pasa contra `c193bfe4`: 25 filas de campañas, diez hitos, 12.016 HH de conformidad y sus proporciones. No han reaparecido las 217.543 HH ni las fechas anteriores del T-17.
- **CPM/H12:** el SD9 ya explicita que la sincronización con el T-15 publicado no valida su reproducción ni resuelve la diferencia entre fecha objetivo E2, acta H12 y cobertura desde el primer día del mes 21. Sigue siendo un pendiente de integración con SD7, no una incoherencia oculta nueva.
- **Aritmética de conformidad:** 4.224 + 7.792 = 12.016 HH y 12.016 / 220.023 ≈ 5,5 %. Las 880 HH de frío no se suman dos veces a la base del proyecto. I-04 obliga a revisar el modelo de pruebas, no prueba automáticamente que esa suma sea incorrecta.
- **Referencias internas:** la comprobación de etiquetas de tablas y figuras del cuerpo no encontró destinos ausentes; reconoce las etiquetas generadas por el macro de figuras.
- **Métricas:** se comprobaron 42 identificadores 9A únicos.
- **Herramientas:** las herramientas específicas buscadas en T-13/Anexo 9.B sí aparecen en SD4. Que SD6 no enumere todas no demuestra que SD9 incorpore herramientas nuevas.
- **Volumetría:** los principales números de prueba contrastados conservan correspondencia con SD4: 14,66 TPS, 6,94 TPS de despacho, 775,33 concurrentes y 32,11 GB de migración. Esto no sustituye ensayos de capacidad.
- **Gateway de frío:** SD9 exige que un gateway de Talca sustituya al otro y atienda ambas cámaras. SD4 declara dos gateways y ensayos de falla, pero su ADR-22 no detalla por sí solo la conmutación cruzada. Es evidencia de diseño/ensayo por completar, no una contradicción demostrada que permita afirmar que el reemplazo no funciona.
- En las relaciones verificadas con **SD2, SD5, SD8 y SD13** no se confirmó una contradicción adicional de la misma claridad. Esto no certifica cumplimiento exhaustivo de esos documentos ni resuelve sus problemas propios.

## 4. Orden de corrección sugerido

1. Separar integración y protocolos por etapa; asegurar que H4/H5 no dependan de portales/EDI todavía no construidos.
2. Regenerar el catálogo con el SD3/T-12 vigente y revisar regresión, pruebas manuales y escenarios de fallas.
3. Acordar la matriz individual de trazabilidad y reparar las remisiones que la dan por existente.
4. Acreditar o reformular el refuerzo de evaluadores; distinguir capacidades presupuestadas de personas asignadas.
5. Unificar el antecedente CMMI, los denominadores de cobertura y las reglas de gobierno de umbrales.
6. Volver a compilar/verificar el paquete solo después de aplicar las correcciones autorizadas.

## Alcance técnico y versiones

Se leyeron las fuentes locales de cuerpo, Anexos 9.A–9.D, T-13 y T-17, y se extrajo el texto de sus cuatro PDF y de las figuras PDF. Se buscaron referencias entrantes al SD9/T-13/T-17 en las demás ramas y se contrastaron alcance por etapa, requisitos, conteos, criterios, recursos, antecedentes y magnitudes principales.

| SD | Referencia Git | Commit |
|---|---|---|
| 1 | origin/LafroX-Subdoc1-LateX | d03bf324 |
| 2 | origin/LafroX-Subdoc2-LateX | ed9f7bd5 |
| 3 | origin/LafroX-Subdoc3-LateX | 33508bb3 |
| 4 | origin/subdoc-4 | d9b1b1ba |
| 5 | origin/LafroX-Subdoc5-LateX | 77b20f91 |
| 6 | origin/LafroX-Subdoc6-LateX | ecc85f0b |
| 7 | origin/LafroX-Subdoc7-LateX | c193bfe4 |
| 8 | origin/Lafrox_Subdocumento_8_Latex_Nuevo | 37ba6c86 |
| 9 | checkout local modificado sobre LafroX-Subdoc9-LateX | 30f7bc62 + cambios locales |
| 13 | origin/LafroX-Subdoc13-LateX | 68501694 |

SD10–SD12 siguen sin contenido técnico propio desarrollado en sus ramas nominales: no permiten una comparación sustantiva. Se usaron las ramas activas SD4/SD8 y no sus variantes antiguas. Las rutas de otros SD son rutas lógicas dentro de la referencia Git indicada, no fuentes existentes en el checkout SD9. Las copias y el conteo verificable de los 374 RT se conservan bajo `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/tmp/auditoria_sd9_actual/`; no forman parte de los entregables.

La revisión no ejecuta pruebas del sistema, no acredita certificados ni turnos, y no comprueba contra información externa la vigencia de estándares o leyes. Es una auditoría de coherencia de la documentación disponible. No se corrige ni publica nada en este turno.
