# Análisis profundo del Subdocumento 1

Fecha de revisión: 30 de septiembre de 2026.

## 1. Alcance y criterio de análisis

La revisión se limita a `01_presentacion_empresa`: documento principal, anexos, formulario T-6, fuentes LaTeX, plantilla local, logos, README, retroalimentación de la primera entrega y registros de compilación. Se extrajo texto y se revisaron visualmente las 30 páginas de los tres PDF: 17 del documento principal, 5 de anexos y 8 del T-6. Las páginas con organigrama, declaración de IA, contactos y escasa ocupación se inspeccionaron también individualmente.

No se revisaron las Bases, los otros subdocumentos, los requerimientos generales ni análisis anteriores del proyecto. Por eso, las referencias al Art. 34, Art. 40, arquitectura, Sobre 1 y Subdocumento 3 se evalúan como declaraciones del material revisado. No constituyen comprobaciones independientes de cumplimiento. Tampoco se verificaron en internet las certificaciones, programas comerciales o entidades mencionadas.

La retroalimentación es el criterio local de contraste. Su instrucción de utilizar proyectos ficticios y verosímiles establece el contexto académico; no se interpreta la falta de existencia real de esos proyectos como una falta por sí misma. Sí se evalúa que la ficción sea coherente, esté bien identificada y tenga evidencia simulada trazable cuando el texto la promete.

Se distinguen tres clases de resultado: defecto comprobado en estos archivos; debilidad de demostración; y asunto que requiere validación fuera del alcance. No se asigna una nota ni se presume el resultado de una evaluación oficial.

## 2. Dictamen

La versión actual corrige una parte sustancial de las deficiencias de la primera entrega. Tiene identidad corporativa, trayectoria fechada, tres líneas de negocio, catálogo, organigrama, dotación que suma correctamente 124 personas, gobierno interno y un T-6 independiente con tres proyectos y sus once campos.

Sin embargo, todavía presenta una distancia entre lo que declara y lo que demuestra. Las principales brechas son la ausencia de credenciales financieras, el dimensionamiento incompleto de la capacidad operacional y el respaldo pendiente de certificaciones y alianzas. A ellas se suman un RUT con dígito verificador incorrecto, un PDF de anexos desactualizado respecto de la plantilla actual y problemas de paginación.

No corresponde rehacer todo desde cero. Conviene conservar la estructura y corregir las brechas de evidencia, precisión y presentación. Tampoco resulta defendible considerar cerradas todas las observaciones de la primera entrega.

## 3. Mapa de archivos y función efectiva

| Archivo o grupo | Función | Resultado de la revisión |
|---|---|---|
| `LAFROX-Subdocumento1.tex` | Entrada del documento principal | Importa `contenido.tex`; portada con T-7; comentario de compilación todavía apunta a `main.tex`. |
| `contenido.tex` | Fuente sustantiva | Seis secciones, referencias y declaración de IA. Contiene la mayoría de las mejoras y brechas. |
| `LAFROX-Subdocumento1.pdf` | Documento principal entregable | 17 páginas; tres tablas y una figura; una página casi vacía en el folio 9. |
| `LAFROX-Formulario-T-6.tex/.pdf` | Experiencia similar | Tres proyectos y once campos; 8 páginas, las tres últimas horizontales. |
| `LAFROX-Subdocumento1-Anexos.tex` y `anexos.tex` | Archivo de anexos | Declara que no existen anexos complementarios y remite al T-6 y al Sobre 1. |
| `LAFROX-Subdocumento1-Anexos.pdf` | Anexos renderizados | 5 páginas para una breve declaración; diseño anterior, con monograma LX y sin el acento naranja de los PDF actuales. |
| `tablas/equipo.tex` | Tabla nominal heredada | No está incorporada en la compilación actual del principal. Conserva certificaciones cuestionadas en la retroalimentación. |
| `lafrox.cls`, `lafrox-portada.tex`, `logo/` | Plantilla e identidad | Buena base visual; algunos comentarios prometen controles que no aparecen implementados o invocados. |
| `latexmkrc` | Construcción | Por defecto compila principal y T-6; no incluye anexos. |
| `README.md` | Documentación de trabajo | Describe `entrega_1/`, `entrega_2/` y un registro de observaciones que no están en la carpeta revisada. |
| `retroalimentación entrega 1.md` | Criterio local | Permite evaluar cierre de observaciones, sin sustituir la rúbrica completa. |
| `.log`, `.aux`, `.toc`, `.lot`, `.lof`, `.fls`, `.fdb_latexmk`, `.synctex.gz` | Productos auxiliares | Los registros actuales informan compilación de los tres PDF; hay residuos `main.*` de una versión anterior. |

## 4. Contraste con la primera entrega

| Observación original | Estado en la versión actual | Qué queda pendiente |
|---|---|---|
| T-6 ausente y solo dos casos | Resuelta en contenido | Existe T-6 independiente con tres proyectos. Mejorar su presentación. |
| Faltaban nueve de once campos | Resuelta en contenido | Los once campos están en los tres proyectos; los años podrían precisarse con mes si fuera necesario. |
| No había figuras | Resuelta | Ahora hay un organigrama explicado; la mejora visual sigue siendo limitada. |
| Trayectoria sin año ni hitos | Resuelta en descripción | Fundación en 2012 e hitos en 2015, 2018, 2021 y 2024. Falta detalle de respaldo del hito de acreditación de 2018. |
| Sin líneas de negocio ni catálogo | Resuelta en cobertura temática | Tres líneas y catálogo en tres categorías; sigue siendo principalmente una enumeración en prosa. |
| Sin organigrama ni desglose de dotación | Parcialmente resuelta | Organigrama y 124 técnicos por área/ubicación; faltan total corporativo, antigüedad y cobertura de turnos. |
| Certificaciones solo como alineación | Mejorada, no acreditada dentro del alcance | Ahora se declaran organismo, número, alcance y vencimiento; los respaldos se remiten al Sobre 1. |
| Única alianza AWS | Mejorada | Hay alianzas de nube, equipos, redes y satélite; faltan precisión comercial y cobertura explícita de servidores/IoT. |
| Gobierno como lista de normas | Mejorada | Hay responsables, comités y frecuencias; faltan indicadores completos y evidencia de funcionamiento. |
| Capacidad instalada genérica | Parcialmente resuelta | Se declaran dos centros de datos y personal; no se identifican sedes, equipamiento o capacidad libre. |
| RTO/RPO contradictorios | Resuelta dentro del documento | Ambos lugares usan RTO ≤ 4 horas y RPO ≤ 15 minutos. No se contrastó con el resto de la oferta. |
| Cinco ambientes anunciados, seis listados | Resuelta dentro del documento | DEV, QA, PREPROD, PROD y DR. Capacitación se explica como espacio aislado. |
| Perfil serverless incompatible con solución Django | Mejorada en el perfil | Ahora se declara Python/Django/PostgreSQL. Persiste ambigüedad sobre despliegue independiente. |
| Tabla del equipo mal ubicada y con credenciales dudosas | Corregida en el PDF activo, pendiente en archivos | La tabla antigua no se utiliza, pero permanece. La sección 1.5 sigue detallando ocho personas del proyecto. |
| Credenciales financieras insuficientes | Pendiente | No se incorporan datos financieros ni una remisión específica a antecedentes financieros. |

## 5. Hallazgos prioritarios

### H01. Las credenciales financieras no están desarrolladas — prioridad alta

**Evidencia:** la retroalimentación exige credenciales técnicas, organizacionales y financieras. `contenido.tex` describe recursos y contratos anteriores, pero no presenta patrimonio, ingresos, liquidez, endeudamiento, capital de trabajo, financiamiento ni capacidad para sostener obligaciones prolongadas.

Los montos del T-6 —25.000 a 35.000 UF, 18.000 a 25.000 UF y 12.000 a 18.000 UF— describen el tamaño de contratos. No demuestran solvencia, margen, caja disponible o exposición actual.

**Corrección propuesta:** incorporar una síntesis financiera académica coherente con los 124 técnicos y la escala de los proyectos, o remitir de forma identificable a los documentos financieros pertinentes, con nombre, período y contenido acreditado. No inventar valores aislados sin conciliación con la historia de empresa.

### H02. El RUT impreso tiene un dígito verificador incorrecto — prioridad alta

**Evidencia:** `lafrox.cls:336` define `77.418.902-K`, visible en las portadas de los tres PDF.

La comprobación aritmética por módulo 11 produce suma ponderada 149, resto 6 y dígito verificador 5. Para el cuerpo numérico 77.418.902 corresponde **77.418.902-5**.

**Corrección propuesta:** confirmar la identidad ficticia acordada. Si se conserva ese cuerpo numérico, usar el dígito 5 y regenerar los tres entregables. Esto comprueba coherencia aritmética, no inscripción ni existencia de la empresa.

### H03. El NOC está contado, pero no dimensionado — prioridad alta

**Evidencia:** `contenido.tex:110` y `:120` declaran 32 personas de NOC y cobertura 24×7, mientras la programación de turnos queda diferida a cada contrato.

El desglose es una mejora, pero no permite determinar puestos simultáneos, turnos, respaldo por ausencias, capacidad L1/L2/L3 o carga de contratos activos. Una plaza continua requiere 168 horas de cobertura por semana antes de ausencias y otras tareas; conocer el total de personas no basta para saber cuántas plazas continuas se sostienen. No se concluye que 32 sean insuficientes.

**Corrección propuesta:** presentar un cuadro de capacidad corporativa con puestos concurrentes, organización de turnos, reserva, escalamiento y carga disponible. Separar claramente la operación del NOC, la atención a usuarios y las guardias de especialistas. Explicar cómo se reserva capacidad para Puelche sin asignar toda la dotación corporativa al nuevo contrato.

### H04. Certificaciones y referencias: afirmación versus evidencia — prioridad alta

**Evidencia:** `contenido.tex:152` remite certificados y cartas al Sobre 1. Después utiliza expresiones como «está validada», «acredita» y «experiencia verificable». En estos archivos no se incluyen certificados ni cartas.

La remisión puede ser correcta para la oferta completa, pero su entrega efectiva no se puede comprobar con el alcance solicitado. Las entradas bibliográficas con números de certificado no sustituyen esos respaldos.

La retroalimentación autoriza proyectos ficticios; el problema no es esa ficción, sino presentar antecedentes simulados como verificados sin identificar su carácter ni el documento que los sostiene. El propio texto reconoce que son declaraciones, pero cambia luego a lenguaje de acreditación.

**Corrección propuesta:** identificar el carácter académico de los antecedentes según el formato autorizado y crear una trazabilidad precisa hacia los respaldos simulados correspondientes. Evitar afirmar validación efectiva cuando solo se está declarando información.

### H05. El PDF de anexos no corresponde a la identidad visual actual — prioridad alta

**Evidencia:** compilación registrada el 27 de septiembre; plantilla local modificada el 29. Principal y T-6 fueron compilados el 30. La inspección visual confirma que anexos usa LX y diagonales grises, mientras principal y T-6 usan el isotipo del zorro y acento naranja.

El contenido sustantivo de la declaración de anexos coincide con `anexos.tex`; la divergencia comprobada es de presentación y dependencia de plantilla.

**Causa probable:** `latexmkrc` solo incluye principal y T-6 en `@default_files`. Una compilación por defecto no actualiza anexos.

**Corrección propuesta:** incluir anexos en el procedimiento de generación de entregables y recompilar cuando cambie la plantilla. No confundir un log sin errores con un PDF actualizado respecto de todas sus dependencias.

### H06. La disponibilidad de referencia no es directamente comparable — prioridad media-alta

**Evidencia:** Tabla 1.2, folio 12 del principal; fila de SLA del T-6, folio 7. Los proyectos 1 y 2 usan disponibilidad anual de 99,5 % y 99,9 %, respectivamente. El proyecto 3 usa 99,5 % mensual del servicio central. La tabla compara esas cifras con 99,95 % de infraestructura.

Es positivo reconocer que la exigencia de Puelche supera la experiencia. Sin embargo, también cambian el objeto medido y el período. Disponibilidad de infraestructura y de un servicio aplicativo no son intercambiables; un promedio anual puede admitir un mes con disponibilidad inferior al objetivo mensual.

**Corrección propuesta:** agregar objeto del SLA, ventana de medición, exclusiones y resultado observado. Explicar por separado qué experiencia sirve para volumen, continuidad, aplicaciones y soporte. Sustituir «verifica cifra por cifra» por una formulación que reconozca las diferencias de comparabilidad.

### H07. La complejidad de los proyectos todavía depende demasiado de cifras brutas — prioridad media

**Evidencia:** T-6, folios 6–7; síntesis en `contenido.tex:164` en adelante.

Los tres proyectos están mejor diferenciados: logística e integración, telemetría de frío y preventa desconectada. Sus fechas de término —2022, 2023 y 2024— son compatibles con una ventana de cinco años respecto de 2026.

No obstante, faltan explicaciones operacionales de las cifras:

- Proyecto 1: 22.000 entregas para 420 camiones representan unas 52,4 entregas por camión y día, si todos participan. No es prueba de imposibilidad; exige definir qué se cuenta, tamaño de ruta y distribución de carga. El principal añade ERP y facturación electrónica, mientras el alcance del T-6 no identifica explícitamente el ERP ni las integraciones.
- Proyecto 2: 12 millones de mediciones mensuales equivalen a unas 4,63 por segundo como promedio de un mes de 30 días. La complejidad puede estar en sensores, ráfagas, continuidad, alarmas y retención, pero el total mensual por sí solo no la demuestra. Faltan cantidad de sensores, frecuencia y política ante desconexión.
- Proyecto 3: 18.000 transacciones para 280 preventistas representan unas 64,3 por persona y día. Debe definirse si son pedidos, operaciones internas o eventos. Faltan máximo de usuarios concurrentes, duración de desconexión y resultados de conciliación.

Además, se declaran SLA comprometidos, pero no resultados efectivamente alcanzados. Los proyectos narrados muestran alcance y tamaño; todavía no prueban desempeño de operación.

**Corrección propuesta:** incorporar una breve ficha de complejidad por proyecto: integraciones, usuarios/sitios, picos, dificultad afrontada y resultado medido. Conciliar unidades entre principal y T-6 sin sumar entregas y transacciones, algo que el texto ya evita correctamente.

### H08. Alianzas pertinentes, pero insuficientemente delimitadas — prioridad media-alta

**Evidencia:** sección 1.6, `contenido.tex:230` en adelante.

La cobertura de nube, terminales, redes y satélite es mucho mejor que una alianza AWS aislada. Persisten cuatro debilidades:

1. «Fortinet / Cisco (Select Partner)» reúne dos fabricantes en una única denominación y vigencia, sin separar acuerdos ni beneficios.
2. El nivel de socio AWS se presenta como garantía de soporte empresarial directo L3. En los archivos no se identifica el contrato de soporte que habilita ese beneficio.
3. La resistencia a −25 °C se atribuye de manera general a productos Zebra, sin familias/modelos ni alcance de la condición ambiental. Una alianza no acredita por sí misma las condiciones de todos los equipos suministrados.
4. No se identifica de forma explícita al proveedor de servidores físicos, gateways/termógrafos, equipamiento de centros de datos o mantenimiento presencial. Las alianzas existentes no demuestran automáticamente esa cobertura.

**Corrección propuesta:** convertir la sección en una matriz: proveedor, programa/acuerdo, estado, vigencia, beneficio documentado, componente cubierto y respaldo. Tratar las fechas y denominaciones comerciales como pendientes de validación, sin afirmar que son falsas.

### H09. CMMI requiere una validación técnica específica — prioridad media-alta

**Evidencia:** `contenido.tex:158`, `:162` y `:247` relacionan CMMI-DEV, versión 2.0, SCAMPI A, evaluación de 2023 y una renovación SCAMPI A en 2026.

Estos archivos no explican la correspondencia entre versión del modelo, método de evaluación, unidad organizacional y mecanismo de renovación. Tampoco identifican al evaluador; solo lo describen como acreditado.

No se determina aquí cuál nomenclatura externa es válida: esa comprobación excede la revisión limitada a archivos. Sí se identifica un punto de validación necesario antes de conservar una referencia tan específica.

**Corrección propuesta:** validar conjuntamente versión, método aplicable, fecha, alcance organizacional y datos del evaluador. Evitar reemplazar una sigla por otra sin comprobar la ficha completa del antecedente simulado.

### H10. El gobierno interno describe actividades, pero no cierra el ciclo de control — prioridad media

**Evidencia:** sección 1.3, folios 10–11.

Hay comités mensuales, auditorías trimestrales, pruebas externas y simulacros semestrales; cobertura de pruebas mínima de 80 % y rechazo de deuda bloqueante. La gestión del conocimiento es ahora corporativa y contempla post-mortem y talleres.

Falta convertir las actividades en un modelo de gestión verificable: indicador, meta, fuente, dueño, frecuencia de medición, tratamiento del desvío y registro. Cobertura de pruebas no demuestra por sí sola corrección funcional. SAST/SCA tampoco explican qué vulnerabilidades bloquean un despliegue ni sus plazos de resolución.

El texto introduce un veto de QA y escalamiento a Gerencia, pero el organigrama no muestra esa relación de escalamiento. La estructura se denomina matricial aunque la figura representa principalmente una jerarquía funcional, sin relaciones de asignación a proyectos.

**Corrección propuesta:** una matriz breve de calidad, seguridad y conocimiento, acompañada de una regla explícita de aprobación y tratamiento de excepciones. Mostrar en la figura o en su leyenda las líneas funcionales y de escalamiento.

### H11. Capacidad instalada y dotación global incompletas — prioridad media

**Evidencia:** `contenido.tex:27`, `:61`, `:97` y Tabla 1.1.

La suma 48 + 15 + 32 + 12 + 10 + 7 = 124 es correcta. El texto reconoce que excluye Gerencia, Operaciones, gestión, comercial y administración, lo que evita presentar 124 como total absoluto de la empresa.

No obstante, falta el total corporativo; «Centro de Operaciones» no identifica una sede; no hay distribución de antigüedad ni datos sobre disponibilidad real de personal. Se declaran dos centros de datos sin localización, modalidad de propiedad/arrendamiento, capacidad de cómputo, almacenamiento, redundancia o responsabilidades de mantenimiento.

La cartera incorpora ocho clientes activos, pero cinco no tienen alcance, antigüedad de relación o capacidad contratada. La lista no demuestra por sí sola que se sostengan operaciones simultáneas de esa escala.

**Corrección propuesta:** ficha de sedes y recursos instalados, dotación corporativa total y capacidad ocupada/disponible. Para clientes adicionales, una tabla breve de relación y servicio, sin extender innecesariamente la narrativa.

### H12. «Monolito modular» y «despliegue independiente» quedan ambiguos — prioridad media

**Evidencia:** `contenido.tex:23` y `:222`.

El perfil de empresa ahora es coherente internamente con Python/Django/PostgreSQL. Pero el despliegue independiente de componentes críticos puede referirse a procesos de trabajo, componentes móviles, borde o servicios separados. El texto no los identifica.

No se afirma que sea técnicamente imposible. La debilidad es que una expresión puede sugerir separación de despliegue de módulos que forman una misma unidad de aplicación.

**Corrección propuesta:** distinguir núcleo modular y unidad de despliegue de los componentes que realmente se despliegan aparte. Conservar el detalle arquitectónico extenso en su documento correspondiente.

### H13. Persisten afirmaciones absolutas o excesivamente concluyentes — prioridad media

**Evidencia:** `contenido.tex:21` afirma que el diseño elimina el riesgo de pérdida transaccional; la sección de alianzas utiliza «garantiza» para beneficios y continuidad; la cartera concluye capacidad de operación simultánea a partir de una enumeración.

El almacenamiento cifrado y la sincronización reducen determinados riesgos, pero el texto no trata pérdida física del dispositivo, corrupción, conflictos o fallos antes de replicación. La solución técnica descrita no demuestra eliminación de todo riesgo.

**Corrección propuesta:** expresar capacidades y condiciones concretas: persistencia local, reintentos, idempotencia, respaldo, reconciliación y límites. Reducir lenguaje promocional y vincular cada conclusión a un dato que realmente la sostenga.

## 6. Calidad editorial y presentación

### H14. Paginación innecesariamente dispersa — prioridad media

El principal dedica el folio 9 a un solo párrafo de NOC. La fuente tiene `\newpage` antes y después de ese párrafo (`contenido.tex:119–122`). Es un defecto visible y de causa identificable.

En el T-6, cinco páginas preceden a la tabla, incluyendo una lista de figuras vacía. La tabla ocupa tres páginas horizontales y la tercera contiene únicamente la fila de contactos. En anexos, cinco páginas conducen a un párrafo que declara que no existen anexos; las listas de tablas y figuras están vacías.

**Corrección propuesta:** retirar saltos innecesarios, usar preliminares pertinentes al tamaño del archivo y reorganizar las fichas de experiencia para evitar una página residual. Mantener las exigencias formales que correspondan; no eliminar índices obligatorios sin contrastar previamente el formato aplicable.

### H15. Controles formales declarados en la plantilla no demostrados — prioridad por validar

Los comentarios de `lafrox.cls` dicen que el formato contempla zona de media firma por página, hoja resumen y orientación vertical. La inspección muestra folios correlativos, pero en páginas interiores no aparece un bloque específico de media firma; `LFXpiederecho` imprime únicamente el folio. Existe el entorno `hojaresumen`, pero ninguna entrada de estos documentos lo utiliza. Las páginas 6–8 del T-6 están rotadas 90 grados.

Esto prueba diferencias entre intención documentada y ejecución. No permite concluir rechazo normativo: no se leyeron las Bases y puede haber tratamiento especial para formularios o informes preparatorios. El índice general tampoco debe confundirse automáticamente con una hoja resumen de sobre.

**Corrección propuesta:** contrastar estos tres puntos con las reglas aplicables antes de la entrega. La portada presenta espacio de firma, pero los PDF revisados no están firmados; ese estado debe resolverse en el proceso de emisión que corresponda.

### H16. Referencias y navegación mejorables — prioridad baja-media

Las referencias y declaración de IA aparecen como secciones sin numeración y no figuran en el índice general del principal. Las listas de tablas y figuras incorporan la frase completa de fuente en sus entradas, lo que añade longitud innecesaria.

La tabla de IA, folio 17, es legible, pero la columna «Herramienta» se parte como «Herramien-ta» y algunas celdas tienen muchas líneas. La tabla declara «síntesis de turnos NOC» y «validación de organigrama y turnos», aunque el documento no contiene el esquema de turnos. Puede describir trabajo previo, pero el resultado no permite revisarlo.

**Corrección propuesta:** incorporar las secciones finales a la navegación si el formato lo permite, usar títulos breves de figuras/tablas en índices y ajustar las columnas de IA. Alinear la declaración con el contenido efectivamente presentado y el registro real del equipo. Este análisis no modifica ni valida retrospectivamente esas declaraciones.

## 7. Mantenibilidad y control de versiones

### H17. Documentación y fragmentos heredados no describen el estado actual — prioridad media

El README remite a carpetas `entrega_1/` y `entrega_2/` ausentes. La referencia al registro `00_trazabilidad_observaciones/` no tiene un respaldo dentro de la carpeta revisada. No se determina si existe fuera de este alcance.

`LAFROX-Subdocumento1.tex` conserva la instrucción `latexmk main.tex`, pero no hay `main.tex` en la carpeta. Los archivos `main.*` son residuos de una compilación anterior; el log registra 10 páginas frente a las 17 del PDF vigente.

`tablas/equipo.tex` afirma ser importado desde `contenido.tex`, pero no existe esa llamada ni aparece en las dependencias actuales. Conserva CKAD para el líder de datos y «administrador de bases de datos certificado» sin fabricante, exactamente el tipo de observación señalada en la primera entrega.

**Corrección propuesta:** actualizar README y comandos de compilación, identificar la versión vigente, y retirar o marcar expresamente el fragmento heredado. No reintroducir la tabla antigua como si estuviera validada. Registrar el cierre de observaciones con evidencia y versión concreta.

### H18. Identificación de formularios y representación legal requieren precisión — prioridad por validar

El principal y anexos se identifican como T-7; el T-6 se presenta correctamente como formulario independiente. La retroalimentación denomina el ítem «Presentación de la empresa — Formulario T-6», mientras README y fuente hablan de T-7. Puede tratarse del documento contenedor versus el formulario de experiencia; con este alcance no corresponde cambiar todos los T-7 a T-6.

La portada rotula «Representante legal» a Alex Aravena, con cargo «Jefe de Proyecto y Apoderado». Ser apoderado puede explicar una representación autorizada, pero no se adjunta aquí el fundamento del poder ni se distingue representación legal de firma por mandato.

**Corrección propuesta:** comprobar la relación T-7/T-6 en la nomenclatura aplicable y el carácter en que firma la persona designada. Ajustar etiquetas y referencias de manera coherente, sin asumir que la diferencia es un error automático.

## 8. Aspectos que conviene conservar

1. Fundación en 2012 y trayectoria coherente con 2026; las fechas exactas de aniversario no se documentan, por lo que «catorce años» funciona como síntesis por años calendario.
2. Tres líneas de negocio pertinentes a operación desconectada, frío y arquitectura híbrida.
3. Separación explícita entre volumen corporativo y compromiso contractual con el cliente.
4. Cinco ambientes consistentes y un único par RTO/RPO dentro del principal.
5. Organigrama legible, CISO con reporte a Gerencia y explicación del veto de QA.
6. Tabla de dotación conciliada aritméticamente y aclaración de su perímetro técnico.
7. Gobierno del conocimiento corporativo, con responsables y conservación de post-mortem.
8. Tres proyectos distintos; reconocimiento explícito de que el proyecto 3 no tiene componentes on-premise.
9. Reconocimiento honesto de la brecha de disponibilidad y de que entregas y transacciones no se deben sumar.
10. Declaración de IA con revisión humana nominada, cuya precisión puede mejorarse.

## 9. Orden de corrección recomendado

| Orden | Acción | Evidencia de cierre |
|---|---|---|
| 1 | Confirmar identidad y corregir RUT | Portadas con dígito coherente y metadatos conciliados. |
| 2 | Desarrollar credenciales financieras y su respaldo | Síntesis o remisión específica, con datos coherentes. |
| 3 | Completar capacidad corporativa/NOC | Turnos, puestos simultáneos, reserva y capacidad disponible. |
| 4 | Alinear declaraciones con evidencias académicas | Matriz de certificados, alianzas y cartas referenciadas. |
| 5 | Validar CMMI, programas de socios y nomenclaturas | Fichas completas y denominaciones verificadas. |
| 6 | Precisar SLA y complejidad de experiencias | Unidad, período, pico, integración y resultado por proyecto. |
| 7 | Ajustar gobierno y ambigüedad arquitectónica | Indicadores, decisiones y unidades de despliegue explícitas. |
| 8 | Resolver paginación y anexos desactualizados | PDF visualmente consistentes, sin páginas residuales injustificadas. |
| 9 | Actualizar documentación y trazabilidad | README vigente, entradas de compilación correctas y fragmentos identificados. |
| 10 | Revisar reglas formales fuera de este alcance | Confirmación documentada de firma, hoja resumen y orientación del T-6. |

## 10. Verificación realizada y límites

Se verificaron los once campos del T-6, las tres fechas de término, la conciliación de dotación, la repetición de RTO/RPO, las cinco denominaciones de ambientes, los folios y las referencias visuales principales. La suma de personal y el dígito del RUT se calcularon independientemente.

Los logs actuales de principal, anexos y T-6 registran generación de 17, 5 y 8 páginas y no contienen las advertencias buscadas de referencias indefinidas o cajas desbordadas. El log heredado `main.log` sí contiene advertencias de cajas, pero no se atribuyen a los PDF vigentes. No se recompilaron ni editaron las fuentes originales.

Un log correcto no acredita cumplimiento normativo, veracidad de antecedentes, madurez operacional o calidad de contenido. La revisión tampoco prueba consistencia con otros subdocumentos ni entrega efectiva de documentos remitidos al Sobre 1.

**Conclusión:** el Subdocumento 1 tiene una base recuperada y considerablemente mejor que la descrita en la primera retroalimentación. Para completar esa recuperación debe pasar de una descripción detallada a una demostración trazable de capacidad, corregir su identidad aritmética y asegurar que todos los entregables correspondan a la misma versión.
