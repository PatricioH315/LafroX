# LafroX — Pendientes para terminar el ítem 3

Este informe identifica los faltantes, contradicciones y correcciones necesarios para terminar el Subdocumento 3, sus anexos y el Formulario T-12. Corresponde a los archivos presentes al 29 de septiembre de 2026. Es un documento interno de revisión, no un entregable de la Oferta Técnica ni una calificación oficial.

## 1. Alcance y fuentes de la revisión

Se revisan exclusivamente estos tres entregables:

- [Subdocumento 3](../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md).
- [Anexos del Subdocumento 3](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md), incluidos los anexos 3.A–3.K y el material complementario conservado dentro del archivo.
- [Formulario T-12](../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md).

La estructura y presentación se contrastan con las [Aclaraciones](../Bases/aclaraciones-licitacion.md), especialmente §§1–7, 9 y el índice obligatorio del capítulo 3. El contenido se contrasta con el apartado **SUBDOCUMENTO 3** del [informe de revisión](../Bases/Revision_informe.md), las [Bases Administrativas](../Bases/Bases_Administrativas.md), las [Bases Técnicas Transversales](../Bases/Bases_Tecnicas_Transversales.md) y el [Caso 02](../Bases/Caso_02_Logistica.md), especialmente capítulos 10–18. Para consistencia se usan los archivos disponibles de los ítems 1 y 2 y los cuatro CSV actuales de `Requerimientos/`.

La retroalimentación del informe describe una entrega anterior. Sus observaciones se comprueban nuevamente: no se asume que sus páginas, cantidades o defectos sigan vigentes. Tampoco se reutilizan como estado actual las revisiones de archivos `v1` descritas en el contexto, porque esas copias no están presentes en la carpeta examinada.

**Disponibilidad documental actualizada:** el usuario incorporó [LAFROX-Subdocumento2-Anexos.md](../02_problema_necesidad/LAFROX-Subdocumento2-Anexos.md) y se revisó completo en este seguimiento del 29 de septiembre de 2026. Sus familias, condiciones rectoras, decisiones e inventario nominal ya se pueden contrastar; queda cerrada la dependencia por ausencia de ese archivo. Los subdocumentos 4–14 siguen sin estar disponibles como evidencia para este encargo. No se modificaron los CSV ni los entregables de los ítems 1–3. La autorización previa de trabajo local en `arquitectura-basti` se mantiene para actualizar este informe y el contexto, sin cambiar de rama, registrar commits ni publicar.

**Resultado del seguimiento:** disponer del Anexo 2 no significa que solo falten subdocumentos posteriores. Ahora hay respaldo para completar y corregir varios pendientes propios de SD3, pero esas correcciones todavía no se ejecutan. Continúan el desarrollo de catálogos, las decisiones y metas de alcance, la aceptación y las respuestas del T-12; además quedan confirmaciones del CLIENTE y revisión humana/formal que no se sustituyen con otro subdocumento.

## 2. Diagnóstico actual comprobado

El cuerpo ya separa los tres problemas, presenta el calendario contractual correcto y contiene apartados de implementación, implantación y operación. El T-12 sí existe como archivo independiente. Las exclusiones del caso, sus doce restricciones y los dieciséis resultados de aceptación están identificados. Esos avances deben conservarse; no corresponde declarar ausentes todos esos elementos como en la revisión anterior.

El Anexo 2 incorporado aporta catorce familias **F-01–F-14**, cinco condiciones rectoras **RNF-DISP, RNF-REND, RNF-RESIL, RNF-SEG y RNF-DR**, las dieciséis decisiones **S-01–S-16**, nueve exclusiones **E-01–E-09**, doce restricciones **R-01–R-12**, 19 actores y cinco sistemas legados. Es una síntesis: declara expresamente que los requerimientos atómicos y su trazabilidad se desarrollan en SD3/T-12. Por tanto, no sustituye el desarrollo pendiente de los 174 RF y 90 RNF de esos archivos. La primera entrada de varias tablas está mezclada con el encabezado y hay restos de formato y celdas adicionales: el contenido se puede contrastar, pero no se declara cerrado el formato del Anexo 2 ni se lo edita en este encargo.

Sin embargo, el ítem 3 todavía no está completo. El cuerpo expresa decisiones que los registros detallados dejan vacías, el T-12 no responde el cumplimiento y la colección complementaria mantiene versiones contradictorias, precios y referencias impropias. Las figuras son transcripciones textuales: sirven como especificación Markdown, pero no acreditan figuras dibujadas ni legibilidad de la presentación final.

Los siguientes conteos proceden de las filas efectivamente presentes, excluyendo encabezados y separadores:

| Registro vigente | Cantidad comprobada | Pendiente comprobado |
|---|---:|---|
| RF, Tabla 3.A.1 | 31 | RF-11.03 no tiene etapa después de `Alta /`; existen descripciones duplicadas y referencias por contrastar. |
| RF, Tabla 3.A.3 | 143 | Las 143 filas tienen descripción, etapa y prioridad vacías; tampoco incorporan actor, precondición, resultado ni origen en ese registro. |
| RNF, Tabla 3.A.4 | 13 | Los 13 métodos de verificación están vacíos. |
| RNF, Tabla 3.A.5 | 77 | Los 77 umbrales y los 77 métodos están vacíos. |
| Supuestos, Tabla 3.A.6 | 25 | 22 sin contenido respaldado ni fuente; ninguna estructura completa de fundamento, impacto e instancia de validación para todas las filas. |
| Aceptación, Tabla 3.A.13 | 16 | Las 16 celdas de meta propia y las 16 de momento/método están vacías. |
| T-12, Parte A | 264: 174 RF + 90 RNF | Cumple, componente, EDT, prueba, sección y criterio vacíos en las 264 filas; origen vacío en 220. |
| T-12, Parte B | 374 RT | Cumple, componente, sección y evidencia vacíos en las 374 filas. |

**Lectura correcta del conteo:** una meta contractual ya escrita en «Resultado exigido» no necesita inventarse otra vez como «meta propia». Sí debe transformarse en un compromiso verificable con momento, procedimiento y evidencia. Los campos vacíos del T-12 son faltantes documentales; no permiten deducir automáticamente cumplimiento ni incumplimiento de una solución aún no acreditada.

## 3. Límite frente a los demás subdocumentos

El ítem 3 debe explicar qué se construye, para quién, en qué etapa, bajo qué condiciones y cómo se acepta. El informe de revisión exige desarrollar implementación, implantación y operación; estos contenidos deben ubicarse como subtítulos inferiores dentro de 3.4, preservando el índice obligatorio. No se deben crear títulos 3.5, 3.6 o 3.7 del mismo nivel que los declarados.

| Materia | Lo que corresponde cerrar en el ítem 3 | Desarrollo que corresponde a otro ítem |
|---|---|---|
| Arquitectura | Modelo conceptual, nombres de componentes, responsabilidades de negocio y vínculo por requerimiento. | Capas, interfaces, contratos, versiones tecnológicas, emplazamiento, redes, racks y capacidad detallada: SD4. |
| Datos | Alcance de información, reglas, fuentes y resultados de conciliación/migración. | Modelos conceptual/lógico de datos, diccionario, motor, indexación y plan detallado de migración: SD5. |
| Implementación | Enfoque para convertir alcance en incrementos, control de configuración, integración y promoción verificable. | Metodologías completas y su aplicación detallada: SD6; paquetes, Gantt y nivelación: SD7. |
| Implantación | Convivencia, secuencia de adopción, criterios de avance, contingencias y reversión del alcance. | Plan por sitio, fechas, dotación detallada y cronograma: SD7; formación detallada: SD10. |
| Aceptación | Metas, momento, método previsto y vínculo a evidencia por requisito/resultado. | Casos y protocolos completos, datos, ambientes y calendario de pruebas: SD9/T-13. |
| Operación | Servicio durante 36 meses, objetivos, observabilidad, escalamiento y responsabilidades. | Desarrollo completo del servicio y dimensionamientos en sus capítulos correspondientes, incluidas las dependencias de SD4 y SD10. |
| Innovaciones | Declarar cualquier efecto real sobre alcance y etapas, sin inventar innovaciones. | Cinco fichas completas y T-19: SD13; montos: Oferta Económica. |

La EDT y las pruebas son dependencias reales de la trazabilidad exigida por el Caso §17.1. Su ausencia no se remedia inventando códigos ni dejando espacios inexplicados: se deben registrar como dependencias identificadas hasta disponer del documento responsable. El cierre completo del T-12 requerirá enlazarlas después; este encargo no autoriza producir esos subdocumentos.

## 4. Pendientes del cuerpo del Subdocumento 3

Las acciones siguientes se aplican al cuerpo y deben reflejarse en los anexos y T-12 cuando cambien un compromiso. P0 identifica un problema crítico; P1, contenido necesario para cerrar el alcance; P2, presentación y comprobaciones finales. El orden no reemplaza la obligatoriedad de las Bases.

### C01 — P1: introducción e índice en el orden requerido

**Evidencia:** el documento empieza con el título del capítulo, luego `## Índice` y su lista, y después aparece la introducción. El título del capítulo queda seguido de otro título y el del índice, de una lista sin frase de caída. El índice no indica páginas.

**Acción:** conservar exactamente «Introducción al Alcance de la Solución» y los cuatro títulos 3.1–3.4 con su numeración y orden; disponer el índice inicial y la introducción inmediata bajo el título del capítulo sin infringir las reglas de caída. Revisar todos los títulos. Reservar la paginación para su comprobación final, sin asignar páginas ficticias.

**Cierre:** estructura coincidente con Aclaraciones §§2–3 y 11; ningún título seguido directamente por otro título, tabla o lista sin texto. Índice paginado y enlazado verificado solo en la presentación final.

### C02 — P1: justificar las etapas y los hitos externos

**Evidencia:** §§3.1.2 y 3.2.1 contienen el calendario correcto y la dependencia captura–analítica. Falta hacerse cargo expresamente de la preferencia del comité y de la objeción de la gerenta sobre el planificador; septiembre de 2026 aparece en consultas, pero no integrado al razonamiento del alcance.

**Acción:** explicar qué se adelanta, qué se posterga y por qué, considerando riesgo, dependencias y absorción del CLIENTE. Incorporar septiembre de 2026 y enero de 2029 sin afirmar una fecha contractual de inicio desconocida ni prometer retrospectivamente la habilitación del proveedor. No adoptar como hecho «antes del inicio del contrato» de V-14 sin fuente de esa fecha. Unificar OTIF/fill rate de E1 y costo de servir/canal moderno de E2 en todos los registros.

**Cierre:** cada capacidad tiene etapa y justificación; el cronograma del Art. 17 no cambia. Caso §§13.1–13.3 y 17.3 atendidos explícitamente.

### C03 — P0: promesa comercial consistente con el ítem 2

**Evidencia:** SD2, «Arbitraje de tensiones», fija 24 horas urbanas con corte a las 14:00 y 48 horas rurales/periféricas/cross-docking. En SD3, D-03, RNG-15 y S-21 no trasladan completamente ese compromiso: se habla solo de parametrizar o se deja vacío.

**Acción:** incorporar esa decisión como propuesta LafroX procedente del SD2, definir cobertura, tratamiento de pedidos posteriores al corte y comprobación; llevarla a requerimientos y aceptación. Separar el plazo 24/48 horas de la ventana de 30 minutos del canal moderno. Si se propone cambiarla por capacidad, declarar la discrepancia y el cambio requerido en SD2; no alterar silenciosamente la promesa.

**Cierre:** cuerpo, D-03, S-21, RNG-15, catálogo y T-12 expresan una sola política comprobable.

### C04 — P1: modelo conceptual con componentes reconocibles

**Evidencia:** §3.3 conserva tres figuras como texto. Sus capacidades no muestran todos los doce módulos de §3.1.1/Tabla 3.4 ni una correspondencia explícita por requerimiento. Faltan relaciones claras del cross-docking, el acuse y los canales de E2.

**Acción:** completar las descripciones estructuradas de elementos, entradas, salidas, actores, relaciones y diferencias entre etapas. Relacionar capacidades con M1–M12 y los requisitos que las sostienen, sin dibujar arquitectura física en este encargo. Mantener cita previa, título, fuente y explicación posterior.

**Cierre:** se comprende qué se construye sin leer SD4; cada capacidad comprometida se encuentra en el esquema y en la explicación. El dibujo y la revisión visual final quedan pendientes fuera de esta rama Markdown, conforme a Aclaraciones §4.

### C05 — P0: retirar la afirmación de arquitectura revisada y corregir atribuciones

**Evidencia:** la introducción declara haber contrastado arquitecturas disponibles; Tabla 3.4 se atribuye a «Arquitectura Lógica v6-2» y las Referencias la incluyen. Ese documento no está presente. El SD2 y su anexo incorporado no indican «14 CD», marcas SAP/Manhattan ni talleres meses 1–3 y cooperación durante cuatro meses; R-11 del Anexo 2 atribuye la rotación del 38 % a preparación. El reemplazo del WMS sí está respaldado ahora por S-14 del Anexo 2.2 y el inventario del Anexo 2.3.

**Acción:** presentar el padrón M1–M12 como definición conceptual de este alcance y su mapeo a SD4 como dependencia futura. Corregir §§3.2.1–3.2.4 y V-01/V-15/V-17/V-18/V-21 según la evidencia real. Los talleres y cuatro meses de cooperación pueden proponerse como supuesto propio, pero no como texto del SD2: S-16 solo fija captura en E1 antes de la jubilación. Conservar el reemplazo progresivo del WMS con localizadores correctos. El Anexo 2.1 distingue 99,95 % de infraestructura y 99,9 % de transacción crítica: V-18 no debe atribuirle 99,5 % como compromiso actual.

**Cierre:** ninguna fuente ausente aparece como consultada; toda afirmación sobre SD1/SD2 tiene localizador verificable o se identifica como dependencia.

### C06 — P1: desarrollar implementación

**Evidencia:** §3.4.3 es un párrafo de enfoque general. No describe suficientemente el recorrido del incremento, configuración, ramas/versiones, controles de integración ni condiciones para desplegarlo. El detalle útil está disperso en la colección complementaria.

**Acción:** explicar cómo se construye un incremento de recepción, preventa o reparto, cómo se vincula a requisitos, cómo se revisa y versiona, qué validaciones bloquean su promoción y cómo se preserva E1 mientras se desarrolla E2. Adoptar la política corporativa de cobertura del 80 % declarada en SD1, o explicar y resolver cualquier excepción; el 70 % de RT-04.11 es un piso, no prueba de consistencia con esa política.

**Cierre:** enfoque propio del caso que cubre software, configuración, integración continua y despliegue, según «c) Implementación» del informe. La metodología completa permanece en SD6.

### C07 — P1: completar implantación y reversión

**Evidencia:** §3.4.4 ya menciona olas, conciliación, capacitación y autorización de reversión. No fija disparadores concretos, secuencia de vuelta, tiempo máximo propuesto ni manejo completo de operaciones capturadas durante el cambio; tampoco explicita la convivencia de hoja de picking y guía en papel.

**Acción:** describir convivencia y registro oficial por fase, corte/conciliación, decisiones de avanzar o volver, tratamiento de datos capturados, comprobación posterior y escalamiento. Expresar el presupuesto de tiempo de reversión con fundamento compatible con 05:30–07:00, sin confundirlo con RTO. Precisar la estabilización y su cobertura de bodega nocturna y acompañamiento en ruta; vincular su dotación/duración detallada a SD7.

**Cierre:** procedimiento resumido ejecutable y criterios de avance que recogen todas las condiciones del Art. 17.3, incluidas **las cuatro últimas semanas** a volumen real y el acta de la Contraparte Técnica. Caso §§13.3 y 17.6 e informe «d) Implantación» atendidos.

### C08 — P1: objetivos y mecanismos de operación

**Evidencia:** §3.4.5 ya compromete 36 meses, horario correcto, RTO/RPO y escalamiento, pero deja medición/evidencia por completar y no desarrolla objetivos por servicio, procedimientos ni automatización operacional.

**Acción:** identificar servicios, indicador, objetivo, ventana de medida, responsable, frecuencia y respuesta ante desvío. Separar disponibilidad 99,95 % por componentes exigidos en BTT §7.2, 99,9 % mensual de transacción crítica y cero indisponibilidad de despacho. Explicar alertas por sincronización/colas, recuperación, capacidad y procedimientos de incidentes y tareas automatizadas; distinguir NOC 24×7 de la mesa 04:00–22:00 L–S con ampliaciones del caso.

**Cierre:** alcance operacional medible coherente con BA Arts. 20 y 78, BTT §§7.2 y 21, Caso cap. 15 e informe «e) Operación». No basta una lista de términos SRE.

## 5. Pendientes del Anexo 3

Las acciones de este apartado conciernen a los registros vigentes y a la coexistencia con el material complementario. Ese material debe conservarse separado, conforme al AGENTS.md; sus decisiones no se pueden adoptar automáticamente ni usar para completar vacíos sin contraste.

### A01 — P0: controlar el material complementario y el precio

**Evidencia:** la colección `tablas_anexo` está físicamente dentro del archivo entregable aunque su nota diga que no está incluida por el anexo vigente. La decisión 45 contiene «113 mil dólares antes de reservas». Otras tablas presentan montos de garantías y obligaciones administrativas; no son lo mismo que un precio propio de la oferta y requieren clasificación, no eliminación indiscriminada de todas las cifras.

**Acción:** para la futura entrega, resolver qué archivo conserva la colección histórica y cuál constituye el Anexo 3 vigente, con autorización para cualquier traslado o modificación. Mantener el material original separado y conservado; no reconciliarlo automáticamente. La oferta que se presente no puede contener el precio ni cifras que permitan inferir su monto. Revisar además las referencias a compra de dispositivos por el proponente frente a EX-09: el CLIENTE compra, LafroX especifica.

**Cierre:** un único registro vigente por materia; material histórico conservado e inequívocamente fuera de la oferta; cero precios propios de oferta en cuerpo, anexo y T-12. Aclaraciones §3, BA Art. 50.2 e informe «Eliminar el precio».

### A02 — P1: completar los 143 RF pendientes

**Evidencia:** Tabla 3.A.3 contiene 143 materias sin desarrollo adoptado. Tabla 3.A.1 desarrolla solo 31. Hay materia disponible en CSV, pero no está incorporada de forma trazable en esos registros.

**Acción:** por cada RF, completar descripción verificable, actor, precondición, resultado, prioridad, origen localizado y etapa. Mostrar qué toma de los CSV y qué deriva directamente de una Base. Revisar duplicados como RF-07.02/RF-07.03 y RF-02.08/RF-05.05: actualmente sus descripciones no diferencian funciones; justificar su distinción o relación sin renumerar las fuentes por iniciativa propia.

**Cierre:** cada requerimiento ofertado tiene todos los campos del Caso §17.1 y una clasificación clara; toda materia no adoptada tiene disposición fundada, sin usar «materia sin desarrollar» como respuesta final.

### A03 — P0: reconciliar por fuente los códigos y la cobertura

**Evidencia:** los CSV contienen 134 RF del caso y 34 RF de Bases, pero hay cinco colisiones: RF-14.01–RF-14.05. En el primero son telemetría; en el segundo, seguridad. Su unión por código da 163 códigos distintos, no 168 requerimientos equivalentes. El T-12 contiene esos códigos, pero un código común no prueba cobertura de ambas obligaciones.

**Acción:** identificar por documento de origen cada requisito y crear una correspondencia explícita; conservar los CSV. Auditar además colisiones semánticas entre catálogos y tablas complementarias: RF-02.08/02.09, RF-09.06/09.07, RNF-14.01 y RNF-16.03 son puntos de control. El RF-14.07 citado en el material complementario no existe en los CSV actuales ni como fila del T-12.

**Cierre:** ninguna obligación de seguridad queda sustituida por telemetría ni viceversa; cada referencia se resuelve por fuente y significado, no solo por número.

### A04 — P1: explicar diferencias de inventarios

**Evidencia:** T-12 tiene 11 RF sin ID homólogo en los CSV: RF-06.06, RF-07.11, RF-09.10, RF-10.01–10.03 y RF-19.01–19.05. Los CSV RNF suman 24 + 58 = 82 códigos; T-12 tiene 90. Hay tres diferencias de grafía (`RNF-03-01/02/03` en CSV frente a `RNF-03.01/02/03`) y ocho RNF adicionales: RNF-06.02/06.03, RNF-09.05, RNF-11.03/11.04, RNF-12.03 y RNF-14.11/14.12.

**Acción:** registrar alias y justificación de cada adicional con su fuente, sin concluir que deban borrarse ni alterar los CSV. Separar cobertura por fuente, identificadores únicos y obligaciones reales.

**Cierre:** los conteos 174/90 pueden reconstruirse; toda diferencia tiene disposición documentada y ningún alias crea un requerimiento ficticio.

### A05 — P1: correspondencia con SD2 y capacidades faltantes

**Evidencia:** Tabla 3.A.2 deja vacías las filas de cross-docking y acuse tributario y denomina RF-01–RF-14 a las familias del SD2. El Anexo 2.1 incorporado confirma que sus códigos son **F-01–F-14**, en particular **F-05 Cross-Docking Controlado** y **F-09 Acuse de Recibo Legal de GDE**, ambos de E1. También confirma F-12/F-13/F-14 en E2. Los cinco RNF rectores tienen códigos propios que requieren correspondencia con los RNF detallados.

**Acción:** corregir las referencias a familias del SD2 en cuerpo, tablas, glosario y T-12 a **F-01–F-14**, sin renumerar los RF atómicos de SD3/CSV. Completar el mapeo de las catorce familias y de los cinco RNF rectores. Descomponer cross-docking, POD y acuse con etapa, actor, resultado y origen en el caso. Diferenciar acuse legal asociado a la GDE de mensajes del intercambio EDI y asegurar la capacidad requerida en E1 sin depender indebidamente del canal moderno de E2.

**Cierre:** las catorce familias y las cinco condiciones rectoras del Anexo 2.1 tienen correspondencia semántica verificable; F-05 y F-09 dejan de ser vacíos. La fuente ya está disponible: ejecutar esta corrección corresponde al ítem 3, no a un subdocumento posterior.

### A06 — P1: RNF con umbral, origen y método

**Evidencia:** 77 RNF carecen de umbral y los 90 carecen de método en Tablas 3.A.4/3.A.5. Algunas materias de cumplimiento son categóricas; no se resuelven inventando una cifra.

**Acción:** completar cada RNF con el umbral de la Base o un objetivo propuesto y fundamentado, condición de medición, método, evidencia y etapa aplicable. Para requisitos categóricos, formular un criterio binario verificable. Cotejar latencias, retenciones, disponibilidad, seguridad, usabilidad, mantenibilidad y operación. Identificar valores propios como 2 horas de aprendizaje o 15×15 mm como propuestas si no hay fuente contractual que los establezca.

**Cierre:** ningún «umbral por definir» ni método vacío para el alcance ofertado; se distingue exigencia contractual de decisión propia. Caso §§15 y 17.1.

### A07 — P0: resolver las dieciséis decisiones y nueve supuestos adicionales

**Evidencia:** de 25 filas de Tabla 3.A.6, solo S-06, S-14 y S-16 tienen contenido y fuente. El cuerpo y tablas históricas ya toman otras decisiones, pero no hay registro vigente completo de consecuencias e instancia.

**Acción:** usar S-01–S-16 del Anexo 2.2 incorporado como decisiones de formulación ya documentadas, cotejándolas con el Caso §16.1 y desarrollándolas en el registro de SD3; completar también S-17–S-25. No presentar las dieciséis como inexistentes ni como aprobadas por el CLIENTE. Añadir fundamento, impacto si falla, instancia/responsable de validación y requerimientos relacionados, que la síntesis del Anexo 2 no completa para todas las filas. Separar restricciones e hipótesis; precisar custodia del efectivo, interfaces, telemetría, hardware, retiro del planificador, sitios, turnos e historia de reposición.

**Cierre:** las dieciséis decisiones tienen respuesta razonada y los nueve supuestos adicionales tienen tratamiento. «Validación futura» describe un procedimiento concreto y no reemplaza decidir la oferta.

### A08 — P1: exclusiones y restricciones sin filas vacías ni relleno

**Evidencia:** Tabla 3.A.7 deja EX-10/11 vacíos y Tabla 3.A.8 deja R-13–R-22 vacíos. La colección agrega video, web, sobres, garantías y otras condiciones de licitación como si fueran alcance de la solución.

**Acción:** cerrar la disposición de las filas vacías, sin inventar exclusiones. Conservar las nueve exclusiones y doce restricciones del caso. Si se adoptan otras exclusiones técnicas, justificar su Base y efecto concreto; no trasladar automáticamente las históricas. Separar condiciones administrativas de restricciones del producto/servicio.

**Cierre:** no hay filas vacías ni ampliaciones de exclusión que rebajen una obligación de las Bases. Informe «b) Definición del alcance».

### A09 — P0: arbitrar el tratamiento térmico

**Evidencia:** cuerpo §§3.2.2, 3.2.4 y 3.3.2 y RNG-04 vigente disponen retención preventiva del sistema y decisión de Calidad. S-04 del Anexo 2.2 incorporado indica que el sistema alerta y habilita el bloqueo y que Calidad decide liberar, bloquear o rechazar: no acredita retención automática como decisión común ya adoptada. La decisión complementaria 4 y RNG-04 complementaria asignan decisión al conductor; decisión 25 habla de Calidad. Tabla 3.A.26 añade el umbral `> 2 °C por más de 15 minutos` sin sustento localizado.

**Acción:** alinear SD3 con S-04 del Anexo 2.2: precisar qué detecta el sistema, qué bloqueo habilita, cuándo interviene Calidad, cómo se registra y cómo se preserva ante desconexión. Diferenciar bloqueo preventivo de invalidación sanitaria; si se propone un bloqueo automático, justificarlo como modificación de la decisión común y registrar la actualización requerida en SD2, sin aplicarla silenciosamente. No adoptar el umbral genérico como hecho de las Bases: establecer parámetros por producto con fundamento y validación sanitaria competente.

**Cierre:** S-04, reglas, RF/RNF, esquema y aceptación son coherentes; ninguna liberación sanitaria depende de la discreción del conductor. La investigación normativa de detalle es pendiente, no asesoría jurídica acreditada por este informe.

### A10 — P1: reglas de negocio precisas

**Evidencia:** RNG-01 no determina por completo el desempate entre orden de confirmación central y orden de captura offline. RNG-07 dice que entregar descuenta y devolver suma sin definir qué representa el saldo. Precio vigente al despacho del cuerpo/RNG-08 contradice «precio ofrecido» de Tabla 3.A.26. Reagendamiento automático histórico contradice la propuesta con decisión del planificador. La colección agrega 110 % de crédito y 30 días de vida útil sin fuente exacta.

**Acción:** definir los estados del pedido y la reserva firme, la antigüedad de stock/crédito y las consecuencias de conflictos; fijar la semántica del saldo de envases con un ejemplo calculado de entrega/devolución. Usar S-03, S-08, S-09, S-10 y S-12 del Anexo 2.2 para unificar reintento, reserva, precio, retornables y devolución. S-03 ya adopta reagendamiento del sistema y no entrega a terceros; no atribuirle autoridad decisoria exclusiva del planificador sin explicar el cambio. Distinguir captura operacional de efectos tributarios del ERP y revisar los RF relacionados.

**Cierre:** reglas deterministas y ejemplos reproducibles; cero contradicciones con supuestos y catálogos; parámetros adicionales declarados como propuestas, no exigencias inventadas.

### A11 — P1: aceptación de los dieciséis resultados

**Evidencia:** Tabla 3.A.13 deja meta propia y momento/método vacíos en las 16 filas. La complementaria 3.A.23 propone 90/93/95 % OTIF, 7 % de envases y 75/65 % de ocupación, pero no constituye una adopción vigente ni una fundamentación suficiente. «93 % al mes 12» carece de origen temporal claro tras una E1 que produce al mes 16. Una alerta bajo el umbral de ocupación no demuestra que ningún camión salga bajo ese umbral.

**Acción:** por R18-01–R18-16 fijar compromiso, línea base y su alcance, fórmula/unidad, población, umbral, etapa/momento, método, evidencia y autoridad de aceptación. Fundamentar metas propias de OTIF, envases y ocupación; resolver la condición de salida de camiones y la factibilidad de rutas. Definir R18-16 mediante prueba de operación con reemplazo y comparación controlada, no únicamente sesiones de transferencia.

**Cierre:** las 16 filas son comprobables; no se hacen pasar metas propias por Bases ni se deja su elección íntegra al futuro. SD9 desarrolla los protocolos completos.

### A12 — P1: estrategia de apoyo diferenciada por actor

**Evidencia:** Tabla 3.A.12 enumera 19 actores, pero repite «Inicio, piloto y seguimiento» y «Participación y adopción registradas» en todas las filas. El Anexo 2.3 incorporado confirma los 19 y nombra expresamente «Tripulación propia y peoneta (84 personas)»; SD3 abrevia nombres y debe mantener la correspondencia, no tratar a los peonetas como ausentes del SD2. El comité ejecutivo requiere participación explícita como instancia, sin inventar un vigésimo actor nominal. El planificador tiene influencia Alta e interés Muy Alto en ese anexo, incompatible con el tratamiento histórico de «mantener informado» meses 13–16.

**Acción:** precisar actividad, resistencia, influencia/interés, momento, responsable, indicador y respuesta ante falta de cooperación por actor, usando los nombres del Anexo 2.3 y explicitando cualquier abreviación. Incluir participación de comité, gerenta, comercial, almaceneros, autoridad y peonetas sin alterar el universo nominal de 19. Dar al planificador participación acorde con su influencia Alta, interés Muy Alto y riesgo R18-16; distinguir objeciones de gerenta y sindicato. No incorporar como alcance contractual el texto de «liquidación transparente» del actor Empresas Transp. si supone administrar pagos: E-05 del propio Anexo 2.2 y el Caso excluyen esa función.

**Cierre:** estrategia accionable para todos los grupos clave del informe, coherente con SD2 §Actores; los responsables propuestos se corresponden con la estructura de SD1 o están identificados como contraparte del CLIENTE.

### A13 — P1: consultas útiles y sin cierres ficticios

**Evidencia:** V-01–V-21 repiten en gran parte «contrastar el planteamiento original», sin pregunta/responsable/efecto. La colección tiene otra serie V-01–V-12 con significados distintos y varios «Resuelto» sin constancia de respuesta. V-12 histórico dice que la razón social está por definir, pese a la identidad LafroX del encargo.

**Acción:** indicar pregunta específica, fuente del vacío, supuesto de oferta, efecto sobre alcance/etapa, responsable, momento límite y estado comprobado. Distinguir decisión propia de respuesta del CLIENTE. Corregir atribuciones falsas a SD2 y retirar la consulta por ausencia de su anexo, ya disponible; conservar las dependencias de arquitectura, EDT/pruebas. Mantener la serie histórica separada. Registrar para armonización con SD2 el alcance de recepción de F-02 en «seis instalaciones»: no demostrar recepción en un sitio que sea solo oficina sin precisar el universo operacional. El OTIF ≥95 % atribuido al canal moderno en su tabla de actores no debe asumirse como condición expresa de la carta 2029 sin fuente localizada; el Caso §7.1 presenta una meta de referencia sobre 95 %, lo que exige distinguir referencia, propuesta y obligación comercial.

**Cierre:** cada vacío afecta una decisión reconocible y tiene tratamiento; ninguna fila afirma consulta enviada, aprobada o resuelta por tercero sin evidencia.

### A14 — P1: cronograma, soporte, ambientes y continuidad consistentes

**Evidencia:** Tabla 3.A.20 conserva «marcha blanca E2 meses 13–20», mientras el cuerpo usa correctamente desarrollo 13–18 y marcha blanca 19–20. Decisión 33/Tabla 3.A.26 mantienen mesa 08:00–20:00. V-04 complementario interpreta «cinco ambientes más DR», pero SD1 declara cinco en total, incluido DR. La sesión offline de bodega de 8 h no demuestra por sí sola autonomía de CD de 24 h.

**Acción:** mantener BA Art. 17 como calendario rector; adoptar el horario del Caso cap. 15 distinguiendo su RT-21.06 del RT-21.07 transversal por materia. Adoptar cinco ambientes totales (DEV, QA, PREPROD, PROD y DR) coherentes con SD1, conservando la eventual inconsistencia de Bases como consulta. Expresar el requisito de renovar acceso por turnos durante el corte de 24 h, dejando mecanismo técnico a SD4. No confundir RTO/RPO con permiso de interrupción en despacho.

**Cierre:** una sola declaración vigente de calendario, horario, ambientes y continuidad; ningún dato histórico rebaja el caso.

### A15 — P1: cifras y migración con alcance correcto

**Evidencia:** decisión 60 declara 9,6 GB de origen y 20 GB de destino sin mostrar el cálculo en estos archivos; también usa 5,76 TB como capacidad no acreditada. Decisión 32 y el supuesto de migración hablan de cuentas abiertas, omitiendo «más 2 años» del Caso cap. 15. Decisión 58 excluye del cálculo de cobertura registros sin lote, lo que puede ocultar la brecha.

**Acción:** sustentar cualquier cifra propia que permanezca con cantidades, profundidad, tamaños unitarios, fórmula y unidades; o limitar el cuerpo al alcance y remitir el cálculo a SD4/SD5 como dependencia. Incluir maestros completos, ventas/pedidos 3 años, inventario **y movimientos** 2 años, trazabilidad 5 años y cuentas por cobrar saldos vivos **más 2 años**. No inventar lotes: mostrar cobertura total histórica y subconjunto trazable por separado, con sus denominadores.

**Cierre:** cifras reproducibles y límites explícitos; no se exige completar en SD3 toda la volumetría del Caso §14.2, que alimenta dimensionamiento de SD4 y detalle de SD5.

### A16 — P2: rótulos, glosario y referencias

**Evidencia:** rótulos complementarios anuncian 61 decisiones, 15 exclusiones, 44 restricciones, 91 RF, 41 RNF y 47 supuestos; hay respectivamente 60, 14, 43, 90, 40 y 46 filas. Existen citas a RF-02.05d/e y S-41 sin registro correspondiente, fuentes como `reglas_de_negocio.md` y rutas de tablas `.tex`, y códigos no explicados.

**Acción:** conservar las discrepancias como información del material histórico separado, sin corregirlo silenciosamente; cualquier catálogo vigente deberá tener rótulos exactos. Eliminar en la futura oferta las atribuciones a archivos de trabajo y reemplazarlas por fuentes documentales reales. Resolver referencias inexistentes, extender glosario para SD, BA/BTT/BTC, R18, RNG, S/EX/R/V, UUID, SRE, CI/CD y M1–M12, y comprobar enlaces/citas.

**Cierre:** títulos y conteos vigentes exactos, ninguna referencia interna inexistente y cada código interpretado sin ambigüedad. La integridad de columnas de las tablas Markdown actuales sí pasó el control estructural: no se detectaron filas divergentes en los tres archivos.

## 6. Pendientes del Formulario T-12

El formulario ya está separado y conserva todas las filas RT. El problema actual es responder y acreditar, no crear un archivo inexistente. BA Formulario T-12, BTT §1.5 y Caso §17.1 determinan los campos y la cadena requerida.

### T01 — P0: respuesta expresa en todas las filas

**Evidencia:** Cumple está vacío en 264 filas de Parte A y 374 de Parte B.

**Acción:** declarar cumple, cumple parcialmente o no cumple con fundamento de oferta; definir una convención que separe compromiso de resultado de prueba ejecutada. Mantener Obligatorio/Deseable/Según caso como carácter del RT, nunca como respuesta. «Según caso» no equivale a opcional. Cualquier no aplicabilidad debe justificarse contra el caso; la ausencia de prueba ejecutada durante esta fase no autoriza por sí sola declarar no aplicabilidad.

**Cierre:** cero respuestas vacías y ningún «cumple» sin componente y localizador. El criterio de BTT §1.5 exige esa individualización; responder solo «Comprometido» requiere explicar cómo representa la respuesta de cumplimiento, no sustituirla sin definición.

### T02 — P1: Parte A por requerimiento y fuente

**Evidencia:** seis columnas de cumplimiento/trazabilidad están vacías en las 264 filas; 220 orígenes también. «Materia sin desarrollar» no es una descripción verificable.

**Acción:** sincronizar con el catálogo adoptado; por fila, identificar componente conceptual, sección exacta de SD3/anexo, etapa, criterio pertinente y verificación prevista. Asociar obligaciones técnicas sin resultado R18 directo con su criterio transversal, en vez de forzar vínculos semánticos. Resolver las diferencias y colisiones de A03/A04. Indicar EDT y pruebas como dependencias del documento responsable mientras no estén disponibles, con responsable de cierre.

**Cierre:** origen → requisito → componente → etapa → aceptación recorrible por fila. No se declara trazabilidad completa a EDT/pruebas hasta disponer de códigos reales.

### T03 — P1: Parte B con valores del caso y evidencia propia

**Evidencia:** 374 RT carecen de componente, sección y evidencia. La reproducción de la Base no acredita cómo LafroX cumple.

**Acción:** individualizar componente, servicio, producto o práctica y su versión cuando corresponda, localizador de la oferta y entregable/prueba/informe/certificado previsto. Una cita a la Base es origen, no evidencia de la solución. Cotejar todos los parámetros del Caso cap. 15 por **materia**, documentando desajustes de códigos de sincronización, cobertura, retención, firma y soporte; conservar el código transversal y el endurecimiento del caso.

**Cierre:** 374 respuestas localizables y con evidencia pertinente; los valores particulares no quedan invisibles en la reproducción del requisito general. Los localizadores de SD4–SD14 se completan cuando existan, sin exigir su desarrollo dentro de SD3.

### T04 — P1: respuesta coherente sobre IA y requisitos deseables

**Evidencia:** D-09 y decisión complementaria 52 declaran ruteo determinístico y ausencia de IA; Parte B incluye RT-18, RT-05.30 y RT-26.06 sin respuesta. Tabla 3.A.17 complementaria todavía alude a «componentes de inteligencia artificial declarados».

**Acción:** distinguir IA integrada en la solución de IA usada para redactar. Responder por requisito la decisión de no incorporar modelos; justificar los condicionados y señalar deseables no ofertados sin simular cumplimiento. No extrapolar esa decisión a innovaciones de SD13 aún no revisadas: RT-26.06 necesita su condición y futura comprobación.

**Cierre:** D-09, RNF/RF asociados y T-12 son compatibles; no hay una declaración global de «cumple» para una capacidad no propuesta.

## 7. Pendientes transversales y de entrega

Estas acciones afectan los tres archivos. No habilitan creación de PDF ni trabajo en LaTeX dentro de esta rama; se distinguen correcciones Markdown de comprobaciones posteriores del entregable final.

### F01 — P0: retirar notas editoriales de la futura oferta

**Evidencia:** hay numerosas «Nota de trabajo», «Nota de conversión», «esta versión», instrucciones para completar y rutas de tablas originales. Algunas notas están después de Declaración de uso de IA, por lo que el documento tampoco termina estrictamente en esa sección.

**Acción:** llevar los pendientes a este informe interno y redactar el alcance como oferta, sin borrar silenciosamente vacíos ni presentar decisiones no tomadas como resueltas. Diferenciar consultas contractuales legítimas, que sí tienen un registro, de instrucciones del revisor. Retirar las notas de conversión en la futura entrega. Conservar el historial por separado conforme a A01.

**Cierre:** texto sin instrucciones al asistente, notas de versiones ni afirmaciones de conversión. Aclaraciones §7.1(d) e informe «Indicios de uso de IA»; no se infiere automáticamente la autoría humana o artificial del texto.

### F02 — P1: referencias completas y localizadas

**Evidencia:** hay páginas atribuidas a las Bases sin PDF disponible para contrastarlas, referencias que agrupan Caso/BTT en una sola entrada, y la arquitectura ausente en la bibliografía del cuerpo. La declaración de páginas futuras no satisface la exigencia final de página.

**Acción:** distinguir cada documento, agregar Aclaraciones donde sustenten estructura, usar autor/año consistentes y enlazar toda cita con su referencia. Precisar capítulo/artículo/registro en el Markdown; verificar páginas con la edición final disponible, sin fabricar números. Las fuentes externas de cumplimiento requieren investigación y localizadores reales cuando se desarrolle el mecanismo, no una URL malformada o una lista decorativa.

**Cierre:** correspondencia completa cita–bibliografía, sin fuente ausente presentada como consultada; Referencias y Declaración de uso de IA sin numerar y en ese orden al final.

### F03 — P1: revisión humana y declaración de IA veraces

**Evidencia:** el cuerpo tiene 17 filas de declaración, los anexos 11 y T-12 dos: 30 filas con «No documentada». Hay uso Alto declarado, pero eso no acredita revisión. Las figuras textuales tampoco demuestran que el grupo pueda explicar los modelos.

**Acción:** el equipo debe revisar realmente contenido, cálculos, decisiones, trazas y figuras, y consignar quién verificó qué. Actualizar la granularidad de secciones/subsecciones y anexos/formulario conforme a Aclaraciones §7.2; consolidar en A-6 cuando corresponda. No atribuir revisores, firmas o verificaciones ficticias ni reemplazar automáticamente los niveles de uso.

**Cierre:** declaración fiel al trabajo efectivamente realizado y capacidad de defensa del contenido. A-6 es dependencia administrativa; no se exige crearlo como parte del ítem 3.

### F04 — P2: comprobación formal posterior

**Evidencia:** los tres archivos tienen nombres base y separación correctos, pero son Markdown; no se verificaron portada, firma, folio, páginas, tipografía o legibilidad impresa.

**Acción:** después de completar contenido, verificar en el formato final autorizado índice paginado/enlazado, texto seleccionable, carta/oficio, cuerpo ≥11 puntos, tablas/figuras ≥9 puntos, firma y foliación. Revisar estilo LafroX uniforme, orientación y continuidad de tablas; evitar listados largos en el cuerpo. Usar las 25–35 páginas sugeridas por el informe como orientación de análisis, no afirmar que el Markdown ya cumple ese rango. Mantener archivos independientes y nomenclatura/ZIP exigidos.

**Cierre:** revisión visual y documental efectivamente realizada. Nada de esto se da por aprobado en este informe ni autoriza conversión o generación de PDF aquí.

## 8. Secuencia de trabajo y criterio de término

Para ejecutar las correcciones sin trasladar obligaciones de otros capítulos al ítem 3, se propone esta secuencia:

1. Fijar la versión entregable y la conservación del complemento; resolver precio y atribuciones de fuentes inexistentes (A01, C05, F01).
2. Construir la correspondencia por fuente y disponer adicionales/alias, conservando los CSV (A02–A05).
3. Adoptar las decisiones de alcance, etapas, reglas y metas; completar RNF, supuestos, consultas y aceptación (C02–C03, A06–A15).
4. Desarrollar el análisis del cuerpo, modelo conceptual, implementación, implantación, operación y apoyo de actores (C04, C06–C08, A12).
5. Responder T-12 con evidencia propia y dependencias honestas (T01–T04).
6. Corregir estructura, referencias, rótulos y declaración humana real; comprobar luego presentación final (C01, A16, F02–F04).

El ítem 3 queda cerrado en contenido cuando los tres documentos dicen lo mismo y cada capacidad comprometida puede recorrerse desde su fuente hasta su etapa y aceptación, sin campos inexplicados, precios de oferta, referencias ficticias ni decisiones incompatibles. Quedará **cierre condicionado por dependencias** mientras falten los documentos necesarios para el mapeo definitivo a arquitectura, EDT/pruebas. El Anexo 2 ya fue incorporado y contrastado, por lo que su ausencia deja de ser una condición de cierre. Registrar dependencias no equivale a haber presentado una trazabilidad completa.

**Qué falta después de incorporar el Anexo 2:** se distinguen tres grupos, que no deben confundirse:

| Grupo | Pendiente real | Dónde se resuelve |
|---|---|---|
| Trabajo propio del ítem 3, con insumos disponibles | Desarrollar RF/RNF, trasladar F-01–F-14 y decisiones S-01–S-16, fundamentar metas, completar reglas/aceptación, corregir contradicciones y responder la parte sustentable del T-12. | Cuerpo de SD3, Anexo 3 y T-12: las acciones de este informe siguen pendientes de ejecución. |
| Vínculos dependientes de documentos posteriores | Componentes definitivos y localizadores de arquitectura; paquetes EDT; identificadores/protocolos de prueba. | Principalmente SD4, SD7 y SD9/T-13. |
| Otras acreditaciones y validaciones | Detalle de datos/migración, metodología, formación/operación e innovaciones cuando un requisito remita a ellas; confirmaciones del CLIENTE; revisión humana y presentación final. | SD5, SD6, SD10 y SD13 según requisito; CLIENTE/equipo para las validaciones. No todos son nuevos contenidos de SD3. |

Solo **después de ejecutar las correcciones propias del ítem 3** podrá afirmarse que su trazabilidad técnica pendiente se limita a enlaces con subdocumentos posteriores. Incluso entonces, cualquier consulta o revisión humana/formal no realizada conserva su estado real. Actualizar este informe no constituye ejecución ni cierre de esas acciones.

No se han aplicado estas acciones a los entregables. Este informe reúne **32 acciones**: 8 del cuerpo, 16 de anexos, 4 del T-12 y 4 transversales. Los cálculos de inventario y vacíos se realizaron sobre los archivos presentes; no representan aceptación del CLIENTE ni evaluación oficial.

## Referencias

Estas fuentes sostienen el diagnóstico por documento y apartado; los enlaces de revisión son localizadores internos y no sustituyen la bibliografía APA del futuro entregable.

- Distribuidora Puelche S.A. (2026a). [Bases Administrativas de Licitación TFEP-01/2026](../Bases/Bases_Administrativas.md). Arts. 16–17, 20, 40, 50 y 78; Formulario T-12.
- Distribuidora Puelche S.A. (2026b). [Bases Técnicas Transversales](../Bases/Bases_Tecnicas_Transversales.md). §1.5, §7.2, capítulos 3–5, 9–12, 18–22 y RT citados en las acciones.
- Distribuidora Puelche S.A. (2026c). [Caso 02 — Logística](../Bases/Caso_02_Logistica.md). Capítulos 10–18, especialmente §§13.1–13.3, 14.1–14.2, 16.1 y 17.1–17.3.
- Distribuidora Puelche S.A. (2026d). [Aclaraciones de la Licitación](../Bases/aclaraciones-licitacion.md). §§1–7, 9 y 11, índice de capítulos 3–7.
- Comisión revisora. (s. f.). [Revision_informe](../Bases/Revision_informe.md). Apartado SUBDOCUMENTO 3 y consideraciones transversales. Autoría institucional consignada de manera descriptiva; fecha no verificable con este archivo.
- LafroX. (2026). [Subdocumento 1](../01_presentacion_empresa/LAFROX-Subdocumento1.md), [anexos](../01_presentacion_empresa/LAFROX-Subdocumento1-Anexos.md) y [T-6](../01_presentacion_empresa/LAFROX-Formulario-T-6.md). Política de calidad, continuidad, organización y distinción de experiencia corporativa.
- LafroX. (2026). [Subdocumento 2](../02_problema_necesidad/LAFROX-Subdocumento2.md) y [Anexos del Subdocumento 2](../02_problema_necesidad/LAFROX-Subdocumento2-Anexos.md). Arbitraje y problemas; Anexo 2.1: F-01–F-14 y cinco RNF rectores; Anexo 2.2: dieciséis decisiones, nueve exclusiones y doce restricciones; Anexo 2.3: 19 actores y cinco sistemas legados. Anexo incorporado y revisado en este seguimiento.
- LafroX. (2026). [Subdocumento 3](../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md), [anexos](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md) y [T-12](../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md). Archivos actuales revisados.
- LafroX. (s. f.). Catálogos actuales de [Requerimientos](../Requerimientos/): «Consolidado de Requerimientos Funcionales» (134), «Consolidado de Requerimientos NO Funcionales» (24), «Requerimeintos NO funcionales de bases» (58) y «Requerimientos de bases» (34), todos en CSV. Insumos de contraste, no Bases ni aprobación de la Comisión.

## Declaración de uso de IA

Este informe interno fue elaborado con asistencia de Codex para contrastar fuentes, contar registros e identificar pendientes. No se atribuye una revisión humana ya realizada ni se declara cumplimiento oficial de los entregables. Esta declaración se refiere al informe; no reemplaza las declaraciones del ítem 3 ni el Formulario A-6.

| Sección | Herramienta | Finalidad | Nivel en texto | Nivel en diagramas | Revisión humana |
|---|---|---|---|---|---|
| Informe de pendientes, §§1–8 | Codex | Contraste documental, conteos y propuesta de acciones de cierre. | Alto | Ninguno | No documentada al momento de elaboración. |
