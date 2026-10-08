# LafroX — Revisión de falencias e incoherencias entre subdocumentos

Fecha de inicio: 6 de octubre de 2026. Estado: revisión en curso; no se declara agotado el universo de falencias.

Objetivo: identificar los puntos de fuga dentro de los documentos y entre ellos, contra las Bases, sin corregir automáticamente la propuesta. Se utiliza el prompt de revisión de la Comisión con la adaptación Markdown que contiene. Una comprobación numérica pasada no acredita conformidad contractual global.

## Alcance y método

El inventario contiene 19 entregables Markdown de SD1, SD2, SD3, SD4, SD6, SD7 y SD8, más el Gantt histórico complementario. SD5 continúa excluido mientras no se consolide, por decisión del usuario. SD9–14 y sus formularios no se recibieron en esta copia: son dependencias futuras, no incumplimientos inferidos. Los documentos internos de Revision, compct y las guías se usan como antecedentes, no como oferta técnica.

Cada observación incluye fuente, ubicación, fragmento literal, requisito/criterio, efecto y condición de cierre. Crítica indica contradicción que afecta requisito bloqueante o estructura obligatoria de la preparación; Alta indica brecha material; Media indica ajuste acotado. La severidad no es un puntaje oficial ni una declaración de inadmisibilidad de PDF ausente.

La regla del prompt que dice que no existen SD4–14 está desactualizada: prevalece el inventario actual. La ausencia de firma/folio/índice paginado, tamaño de letra, calidad de figuras y revisión visual no puede juzgarse a partir de Markdown como si fuese un PDF final. Tampoco se atribuyen revisiones humanas por el solo nombre de un revisor en una tabla.

## Cobertura de la revisión

| Frente | Estado al guardar este registro |
| --- | --- |
| Inventario, títulos, formularios y declaraciones | Primera pasada realizada; quedan cruces finos de referencias/forma |
| SD1/T-6: empresa, capacidades y evidencia | Primera pasada realizada; cotejo habilitantes y declaraciones en curso |
| SD2: diagnóstico, cifras, actores y arbitrajes | Inspección parcial; falta cerrar todos los cálculos y correspondencias |
| SD3/T-12/anexos: alcance y requerimientos | Primera pasada de trazabilidad; falta cotejo completo contra RT/RF/RNF |
| SD4/T-11/anexos: lógica, física y capacidad | Inspección parcial; falta cerrar memoria y emplazamiento por componente |
| SD6: metodologías y gobierno | Primera pasada realizada; falta cruce de herramientas y cadencias con SD4/7 |
| SD7/T-14/T-15/T-18: red, recursos y despliegue | Primera pasada realizada; faltan dependencias restantes y Gantt |
| SD8/T-16: riesgos y reservas | Primera pasada realizada; falta cerrar cobertura frente a todos los hallazgos |
| Correcciones Informe1/T-22 | Fuente completa no recibida; no se calculan porcentajes ficticios |
| Cadena de trazabilidad de procesos críticos | Cierre pendiente: requisito→componente→sitio→EDT→prueba→aceptación→riesgo |

## Hallazgos confirmados hasta esta pasada

### RV-001 — SD6 conserva títulos y numeración ajenos al capítulo obligatorio

- Severidad / tipo: Crítica / Estructura.
- Falencia y condición de cierre: La fuente usa 1.1/1.2 donde las Aclaraciones exigen 6.1/6.2; su nombre Subdocumento_6 no sigue el patrón de preparación final. Debe corregirse antes de exportar; no se califica un PDF ausente como mal presentado.
- Fuente normativa o criterio: Aclaraciones §§1/2/11, capítulo6.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [06_metodologías/Subdocumento_6.md, línea 28](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/06_metodologías/Subdocumento_6.md:28>). Fragmento literal: «## 1.1 Metodología de gestión de proyecto».
- Evidencia: [06_metodologías/Subdocumento_6.md, línea 124](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/06_metodologías/Subdocumento_6.md:124>). Fragmento literal: «## 1.2 Metodología de desarrollo de software».

### RV-002 — T-9/T-10 no están disponibles

- Severidad / tipo: Alta / Dependencia documental.
- Falencia y condición de cierre: El inventario contiene siete formularios:6/11/12/14/15/16/18. No hay T-9/T-10 para concretar las metodologías. Es ausencia en esta copia, no prueba de que no existan en otro lugar.
- Fuente normativa o criterio: Aclaraciones capítulo6.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [06_metodologías/Subdocumento_6.md, línea 124](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/06_metodologías/Subdocumento_6.md:124>). Fragmento literal: «## 1.2 Metodología de desarrollo de software».

### RV-003 — 262 filas T-12 conservan paquetes por asignar

- Severidad / tipo: Alta / Trazabilidad.
- Falencia y condición de cierre: La EDT ya tiene222 paquetes, pero262 de645 filas de cumplimiento no identifican el paquete. La correspondencia por módulo del Anexo7.E no cierra la trazabilidad requerimiento por requerimiento.
- Fuente normativa o criterio: Aclaraciones §3; BA T-12/T-22.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md, línea 30](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md:30>). Fragmento literal: «| RF-01.02 | El sistema debe exigir el número de lote del proveedor en campo estructurado para todo SKU con trazabilidad obligatoria, capturándolo por escaneo GS1… | Sí (E1) | M1 Recepción | Paquete por asignar en el plan de trabajo | Prueba funcional con datos representativos en marcha blanca | Anexo 3.A, Tabla 3.A.1 | R18-02 | Caso, Cap. 4.1, Cap».

### RV-004 — T-12 usa pruebas que no verifican el comportamiento de la fila

- Severidad / tipo: Alta / Pruebas.
- Falencia y condición de cierre: RF-01.07 generación SSCC y RF-01.08 asociación a ubicación remiten a prueba térmica; RF-01.06 decodificación GS1 remite sólo a usabilidad. Se necesitan protocolos funcionales específicos; no basta clasificar una prueba por palabras del requisito.
- Fuente normativa o criterio: BA Art.18.2; BTT aseguramiento de calidad.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md, línea 34](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md:34>). Fragmento literal: «| RF-01.06 | El sistema debe decodificar códigos de barras GS1 interpretando los AIs 01 (GTIN), 10 (lote), 17 (vencimiento) y 00 (SSCC), autocompletando los… | Sí (E1) | M1 Recepción | Paquete por asignar en el plan de trabajo | Prueba de usabilidad con usuarios reales en terreno | Anexo 3.A, Tabla 3.A.1 | R18-02 | Caso, RT-17.06, Cap. 16.2 (GS1) |».
- Evidencia: [03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md, línea 35](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md:35>). Fragmento literal: «| RF-01.07 | Al finalizar el registro de un pallet, el sistema debe generar automáticamente un SSCC bajo estándar GS1-128 vinculado al GTIN, lote, fecha de… | Sí (E1) | M1 Recepción | Paquete por asignar en el plan de trabajo | Prueba en cámara y vehículo con registro térmico | Anexo 3.A, Tabla 3.A.1 | R18-02 | Caso, Cap. 4.2 , Cap 12 (GS1), RT-05.».
- Evidencia: [03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md, línea 36](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md:36>). Fragmento literal: «| RF-01.08 | El sistema debe permitir asociar un SSCC a una dirección de almacenamiento (pasillo-columna-nivel) escaneando ambas etiquetas y validando la… | Sí (E1) | M1 Recepción | Paquete por asignar en el plan de trabajo | Prueba en cámara y vehículo con registro térmico | Anexo 3.A, Tabla 3.A.1 | R18-02 | Caso, Cap. 4.2, Cap. 12 (GS1), RT-05.23».

### RV-005 — D-05 impide construir antes de terminar los prototipos

- Severidad / tipo: Alta / Cronograma.
- Falencia y condición de cierre: Anexo7.B define FC desde2.6.2 hacia3.4; T-15 termina2.6.2 en mes6 y comienza3.4.1/2/5 en mes5. La red agregada no refleja esta precedencia.
- Fuente normativa o criterio: Anexo7.B D-05; BA Art.17.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 194](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:194>). Fragmento literal: «| 2.6.2 | E | IMP | 3–6 | 180.00 | 240.00 | 300.00 | 240.00 |».
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 213](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:213>). Fragmento literal: «| 3.4.1 | D | DES | 5–7 | 720.00 | 960.00 | 1200.00 | 960.00 |».
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 217](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:217>). Fragmento literal: «| 3.4.5 | D | DES | 5–9 | 720.00 | 960.00 | 1200.00 | 960.00 |».

### RV-006 — D-28 exige terminar estabilización antes de iniciar producción

- Severidad / tipo: Crítica / Cronograma.
- Falencia y condición de cierre: D-28 incluye4.2.2 como predecesor FC de4.2.3. T-15 sitúa4.2.2 meses16–20 y4.2.3 mes16. La dependencia publicada es imposible tal como está escrita; separar cierre de marcha blanca y estabilización posterior.
- Fuente normativa o criterio: Anexo7.B D-28; BA Art.17.2/17.3.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/LAFROX-Subdocumento7-Anexos.md, línea 69](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Subdocumento7-Anexos.md:69>). Fragmento literal: «| D-28 | 4.2.1, 4.2.2 y 7.3.1 Certificación de usuarios | 4.2.3 Paso a producción de la Etapa 1 (H7) | FC | Bases Administrativas, Art. 17.3 y 90.4 |».

### RV-007 — Recepción de sala precede a trabajos necesarios para recibirla

- Severidad / tipo: Alta / Cronograma.
- Falencia y condición de cierre: 6.1.5 está en mes5, pero HVAC/eléctrica/incendio6.1.2–4 continúan hasta mes6. D-10 permite instalar sala desde mes3 mientras especificación5.1.2 cierra mes4. Aclarar entregas parciales y restricciones diarias, sin presentar estas ventanas como FC cumplidas.
- Fuente normativa o criterio: Anexo7.B D-09–13; BTT recinto técnico.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 286](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:286>). Fragmento literal: «| 5.1.2 | G | ARQ | 2–4 | 60.00 | 80.00 | 100.00 | 80.00 |».
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 299](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:299>). Fragmento literal: «| 6.1.2 | T | SRE | 4–6 | 120.00 | 160.00 | 200.00 | 160.00 |».
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 302](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:302>). Fragmento literal: «| 6.1.5 | T | SRE | 5–5 | 120.00 | 160.00 | 200.00 | 160.00 |».

### RV-008 — Identidad se construye mientras su plan de seguridad sigue abierto

- Severidad / tipo: Alta / Cronograma.
- Falencia y condición de cierre: D-06 es FC de2.2.1 a3.3.1; ambas ventanas incluyen mes4. No se demuestra el orden diario de aprobación y construcción. Es una precedencia no acreditada, no imposibilidad si se especifican días/entregas parciales.
- Fuente normativa o criterio: Anexo7.B D-06; BTT seguridad.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 182](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:182>). Fragmento literal: «| 2.2.1 | E | SEG | 2–4 | 180.00 | 240.00 | 300.00 | 240.00 |».
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 207](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:207>). Fragmento literal: «| 3.3.1 | I | SEG | 4–8 | 360.00 | 480.00 | 600.00 | 480.00 |».

### RV-009 — Red de24 bloques no incorpora toda la red D-01–34

- Severidad / tipo: Alta / Cronograma.
- Falencia y condición de cierre: Faltan lags/duración de revisiones, interfaces/certificación externa y garantías. Los ES/EF coherentes del agregado no prueban factibilidad de los222 paquetes. Debe existir una red diaria ejecutable y compatible con HH.
- Fuente normativa o criterio: BA Art.18.3; Aclaraciones7.3.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 486](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:486>). Fragmento literal: «El bloque N04 resume cadenas paralelas de compra, sala, racks y configuración. No sustituye D-07–D-13 ni prueba orden dentro del mes 6. Ningún paquete se entrega en QA antes de H3. El detalle diario y las asignaciones por subventana se verifican antes de aprobar la línea base. Las duraciones agregadas no incluyen separadamente los diez días hábiles».

### RV-010 — No hay Gantt vigente del detalle reconciliado

- Severidad / tipo: Alta / Cronograma.
- Falencia y condición de cierre: El Gantt transcrito del Excel es histórico/sin recálculo; T-14/T-15 se han redistribuido. Las figuras y barras heredadas no materializan la nueva línea detallada con222 paquetes y hitos.
- Fuente normativa o criterio: Aclaraciones7.3; BA T-14/T-15.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/README.md, línea 37](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/README.md:37>). Fragmento literal: «La carta Gantt transcrita del Excel se conserva como fuente histórica complementaria; la programación revisada se lee en T-14/T-15/T-18. No se presenta ese libro como recalculado. Las descripciones históricas de figuras están subordinadas a los criterios vigentes explícitos.».

### RV-011 — PERT de duración vigente no se ha materializado

- Severidad / tipo: Alta / Estimación.
- Falencia y condición de cierre: Hay O/M/P/E de HH por clases, pero se retiró la sensibilidad de duración previa sin recalcularla sobre el calendario nuevo. Las Aclaraciones piden PERT y CPM para ruta/holguras; escenarios deterministas no reemplazan por sí solos el cálculo PERT temporal.
- Fuente normativa o criterio: Aclaraciones7.3.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 497](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:497>). Fragmento literal: «Se retiran los márgenes anteriores de 0,50/0,25 meses y las probabilidades normales por camino: las duraciones y ventanas que los sustentaban no coincidían. N05/N07 conservan 0,50 mes de holgura local por convergencia con N06; no es una reserva adicional de H4. Las marchas blancas y sus cuatro semanas finales tienen reserva utilizable cero.».

### RV-012 — Dotación requerida no está vinculada a competencias disponibles

- Severidad / tipo: Alta / Recursos.
- Falencia y condición de cierre: T-15 pide61 equivalentes en mes9,39DES ese mes y23SRE en mes6; SD1 declara48 desarrolladores Python/Django/móvil y12SRE. Las familias y NOC pueden compartir funciones sólo con matriz explícita. No se demuestra disponibilidad ni habilidades Laravel/PHP o instalación; no se infiere imposibilidad automáticamente.
- Fuente normativa o criterio: BA T-15; BTT equipo; Aclaraciones coherencia.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [01_presentacion_empresa/LAFROX-Subdocumento1.md, línea 149](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/01_presentacion_empresa/LAFROX-Subdocumento1.md:149>). Fragmento literal: «| División de Ingeniería | Desarrollo Software (Python, Django, Móvil) | Sede Central (Santiago) | 48 |».
- Evidencia: [01_presentacion_empresa/LAFROX-Subdocumento1.md, línea 152](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/01_presentacion_empresa/LAFROX-Subdocumento1.md:152>). Fragmento literal: «| División de Infraestructura | Ingeniería de Confiabilidad (SRE) y Cloud | Centro de Operaciones | 12 |».

### RV-013 — Techos mensuales no prueban capacidad de subventanas

- Severidad / tipo: Alta / Recursos.
- Falencia y condición de cierre: M6 y M7 exigen960HH en media mensual,15 personas equivalentes por banda; otras tareas se concentran antes de t9,5. La curva mensual no muestra asignaciones simultáneas, roles especializados ni relevos diarios.
- Fuente normativa o criterio: T-15 §5.2; Aclaraciones7.2.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 480](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:480>). Fragmento literal: «La preparación 3.4.3 completa sus 960 HH en mes 8, después de recepción/inventario; preventa 3.4.6 termina mes 8. Rutas 3.4.7 y reparto 3.4.8 se ejecutan en mes 9. Dentro de ese mes, reparto entrega su base aceptada en la primera mitad y cobranza 3.4.10 ejecuta sus 960 HH en la segunda; devoluciones 3.4.9 e indicadores 3.4.11 terminan en mes 9. Est».

### RV-014 — Cobertura horaria no demuestra SLA de atención

- Severidad / tipo: Alta / Operación.
- Falencia y condición de cierre: Un puesto simultáneo y HH promedio no prueban los tres SLA. SD4 sí propone demanda y Erlang C; falta validar sus supuestos y reconciliar ese cálculo con T-15. RV-052/RV-053/RV-054 precisan la discrepancia de cobertura, límite y abandono, sin afirmar que no exista modelo.
- Fuente normativa o criterio: BTT RT-21.06/07; Caso RT-21.06.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md, línea 545](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md:545>). Fragmento literal: «| E8-07 | Puesto de mesa/cobertura no demuestra SLA. Medir demanda y servicio, turnos y competencias. BTT RT-21.06 y Caso RT-21.06 tienen contenido distinto | SRE; antes H7/mes 21 | R8-22 |».

### RV-015 — Horas de cobertura mensuales son promedios

- Severidad / tipo: Media / Recursos.
- Falencia y condición de cierre: 730HH NOC y468HH mesa provienen de promedios; un mes de31 días exige744HH por puesto24×7. El techo de6 relevos puede cubrirlo, pero las HH mensuales publicadas deben ajustarse al calendario real; no es una prueba de incapacidad de esos seis agentes.
- Fuente normativa o criterio: BTT horarios; T-15 modelo de cobertura.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 132](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:132>). Fragmento literal: «- C identifica cobertura mínima de un puesto simultáneo: NOC = 365 × 24 / 12 = 730 HH/mes; mesa = 18 × 6 × 52 / 12 = 468 HH/mes, ampliada a 730 en septiembre/diciembre bajo el calendario supuesto. Un puesto no es una persona ni acredita capacidad ante el volumen de tickets. La curva dimensiona relevos con 128 HH efectivas.».

### RV-016 — Cuatro semanas de acompañamiento aún no tienen reparto real entre meses

- Severidad / tipo: Alta / Implantación.
- Falencia y condición de cierre: 4.3.2 imputa2464HH sólo en mes21. Si H12 se autoriza después de primeros tres días hábiles, cuatro semanas pueden cruzar mes22. El documento admite redistribuir luego pero no la ha ejecutado; no retirar cobertura para conservar una celda.
- Fuente normativa o criterio: Caso RT-20.05/06; BA Art.17.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 282](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:282>). Fragmento literal: «| 4.3.2 | A | IMP | 21–21 | 2464.00 | 2464.00 | 2464.00 | 2464.00 |».

### RV-017 — RPO residual contradice objetivo obligatorio en un escenario declarado

- Severidad / tipo: Crítica / Continuidad.
- Falencia y condición de cierre: SD4 admite que la última copia remota puede exceder15 minutos si se pierden tres enlaces y después el sitio. NAS local no sobrevive al sitio destruido. SD8 lo reconoce, pero no resuelve la brecha; no basta aceptar el riesgo.
- Fuente normativa o criterio: BTT RT-07.04; SD8 E8-05.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4.md, línea 2616](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4.md:2616>). Fragmento literal: «Queda como riesgo residual la falla simultánea de los tres caminos seguida de la destrucción del sitio antes de reponer alguno: en esa secuencia, la última copia remota podría exceder 15 min. Se mitiga con alarmas de retraso de replicación a los 5 y 15 min, reposición del enlace por el proveedor, preemisión de guías al cerrar la carga y conservació».

### RV-018 — Despacho depende de DTE nuevo cuando cambia la carga

- Severidad / tipo: Crítica / Continuidad.
- Falencia y condición de cierre: Preemisión no cubre una guía invalidada ni destrucción del ERP Talca. Se declara bloqueo sin guía válida; el objetivo40min carece de ensayo/capacidad demostrada. Hace falta una vía tributaria conforme que sostenga96 despachos sin interrupción; no habilitar emisión por otro sistema.
- Fuente normativa o criterio: Caso RT-10.05; ERP intocable; BA aceptación.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4.md, línea 931](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4.md:931>). Fragmento literal: «El ERP permanece como único emisor ante el SII mediante fibra, LTE y satélite de Talca; un cambio de carga invalida la guía preemitida y exige una nueva. El riesgo de identidad local tampoco se declara cerrado antes de probar cada relevo de turno durante un corte de 24 horas. El emplazamiento y la redundancia física se verifican en 4.2.».

### RV-019 — CD-05 tiene volumen supuesto pendiente de multiplicidad

- Severidad / tipo: Alta / Capacidad.
- Falencia y condición de cierre: 2N+2L coincide con4L sólo si N=L. Retenciones por más de un lote/ubicación modifican tráfico, almacenamiento y drenaje; A31/A32 deben contrastarse con escenarios medidos sin declarar dimensionamiento ausente.
- Fuente normativa o criterio: BTT capacidad; SD4A31/A32; SD8C-08.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md, línea 509](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md:509>). Fragmento literal: «| C-08 Mensajes CD-05 (R8-06) | 2N + 2L y 4L coinciden sólo si N=L. Si N=2L, tráfico de coordinación = 6L, un 50 % más que 4L | No implica 50 % más de todo el tráfico. Medir retenciones y contrastar A31/A32 con ARQ/SRE; no alterar aquí memoria física |».

### RV-020 — Reserva de gestión no está dimensionada ni disponible

- Severidad / tipo: Alta / Riesgos.
- Falencia y condición de cierre: SD8 presenta mecanismo de solicitud pero ninguna bolsa técnica o cobertura de necesidades adicionales. Los escenarios400HH/2464HH no tienen asignación financiada ni cronograma neto. No sumar escenarios ni transferir E1 aE2.
- Fuente normativa o criterio: Aclaraciones8.3; BA50.2.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md, línea 529](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md:529>). Fragmento literal: «| Reserva de gestión | Sin bolsa adicional cuantificada/asignada | JP solicita caso; Comité Ejecutivo autoriza con capacidad/plazo explícitos; actualización T-15/calendario. Monto en Oferta Económica |».

### RV-021 — FMEA ordinal no se calibra por evento y horizonte concreto

- Severidad / tipo: Alta / Riesgos.
- Falencia y condición de cierre: Las fichas repiten queD refleja ausencia de prueba en esta sesión; P3/4 carece de justificación individual de bandas, horizonte y juicio responsable. El producto está calculado, pero puntuar no demuestra la validación ni cuantifica una probabilidad estadística.
- Fuente normativa o criterio: Aclaraciones8.1/8.2; BTT RT-19.04.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md, línea 12](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md:12>). Fragmento literal: «- Evaluación inicial: P=4; I=5; D=4; E=20; NPR=80. D refleja la modalidad de detección propuesta y la ausencia de prueba del control en esta sesión.».
- Evidencia: [08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md, línea 27](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md:27>). Fragmento literal: «- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. D refleja la modalidad de detección propuesta y la ausencia de prueba del control en esta sesión.».
- Evidencia: [08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md, línea 42](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md:42>). Fragmento literal: «- Evaluación inicial: P=3; I=5; D=3; E=15; NPR=45. D refleja la modalidad de detección propuesta y la ausencia de prueba del control en esta sesión.».

### RV-022 — Horizonte y oportunidad no tienen escala de beneficio desarrollada

- Severidad / tipo: Alta / Riesgos.
- Falencia y condición de cierre: O8-01 asigna beneficio ordinal3 y puntuación9 sin escala de beneficio equivalente a la escala de impacto de amenazas. Explicitar beneficio, horizonte y evidencia de comparación; no descontar HH sin medición.
- Fuente normativa o criterio: Plan de riesgos y método declarado.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md, línea 567](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md:567>). Fragmento literal: «O8-01 — Oportunidad de diagnóstico: si los casos protegidos INN-02 representan incidentes reales, podrían permitir resolver fallas equivalentes con menos retrabajo. P ordinal 3, beneficio ordinal 3, puntuación de oportunidad 9, separada de exposición de amenazas. CAL compara HH antes/después de casos equivalentes durante validación meses 11–15 y op».

### RV-023 — Declaración IA incompleta por secciones/anexos/formularios

- Severidad / tipo: Alta / Forma.
- Falencia y condición de cierre: SD6 y SD8 cierran con un párrafo, sin la tabla obligatoria de seis campos y filas por cada sección/anexo/formulario. SD7 y otros documentos tienen declaraciones históricas que deben cotejarse con el uso actual. No inventar revisores.
- Fuente normativa o criterio: Aclaraciones7.2; BA A-6.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [08_plan_riesgos/LAFROX-Subdocumento8.md, línea 101](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/08_plan_riesgos/LAFROX-Subdocumento8.md:101>). Fragmento literal: «Codex apoyó la redacción, organización, análisis ordinal FMEA y cálculos deterministas el 6 de octubre de 2026, con participación alta en texto y datos calculados. No se generaron imágenes; la RBS se representa textualmente. La revisión humana no consta en el material de esta sesión. Esta declaración no acredita ensayos ejecutados, aprobación del C».

### RV-024 — Títulos de SD8 sin texto de caída

- Severidad / tipo: Alta / Forma.
- Falencia y condición de cierre: 8.1/8.2/8.3 pasan directamente a subtítulos;8.1.2 pasa a tabla; las fichas de anexos pasan a listas sin frase introductoria. La regla exige texto bajo cada título; no aplica un conteo automático de anclas como si fueran contenido.
- Fuente normativa o criterio: Aclaraciones §3.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [08_plan_riesgos/LAFROX-Subdocumento8.md, línea 9](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/08_plan_riesgos/LAFROX-Subdocumento8.md:9>). Fragmento literal: «## 8.1 Plan de riesgos».
- Evidencia: [08_plan_riesgos/LAFROX-Subdocumento8.md, línea 50](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/08_plan_riesgos/LAFROX-Subdocumento8.md:50>). Fragmento literal: «## 8.2 Identificación y Análisis de Riesgos».
- Evidencia: [08_plan_riesgos/LAFROX-Subdocumento8.md, línea 70](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/08_plan_riesgos/LAFROX-Subdocumento8.md:70>). Fragmento literal: «## 8.3 Plan de Acción a Riesgos».

### RV-025 — SD1–3/SD7 conservan descripciones; la conformidad visual final no está acreditada

- Severidad / tipo: Alta / Presentación.
- Falencia y condición de cierre: La conservación Markdown es correcta para este espacio, pero las descripciones de SD1–3/SD7 no prueban diagramas de entrega. SD4 sí enlaza 26 figuras reales, parcialmente inspeccionadas en navegador; no se afirma que carezca de imágenes. No se generan LaTeX/PDF en esta rama ni se sanciona un PDF no recibido. La preparación final requiere su flujo visual independiente.
- Fuente normativa o criterio: Aclaraciones §4; regla local Markdown.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 29](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:29>). Fragmento literal: «  **Descripción textual de figura.** No sustituye la revisión visual del PDF.».
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 65](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:65>). Fragmento literal: «  **Descripción textual de figura.** No sustituye la revisión visual del PDF.».

### RV-026 — Restos de conversión y notas internas dentro de entregables

- Severidad / tipo: Alta / Forma.
- Falencia y condición de cierre: Hay Datos complementarios de figuras transcritas, nombres de macros y notas históricas/actualizaciones al redactor. Separarlos de oferta; mantener supuestos técnicos sin ocultar pendientes reales ni eliminar declaración IA obligatoria.
- Fuente normativa o criterio: Aclaraciones7.1d.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/LAFROX-Subdocumento7.md, línea 674](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Subdocumento7.md:674>). Fragmento literal: «## Datos complementarios de las figuras transcritas».

### RV-027 — Certificados, experiencia y alianzas son declaraciones sin acreditación recibida

- Severidad / tipo: Alta / Evidencia.
- Falencia y condición de cierre: SD1 contiene identificadores/vigencias/contactos y atribuye acreditación a Sobre1. No hay certificados/cartas en esta copia. No presentar esas afirmaciones como comprobadas por revisarMarkdown.
- Fuente normativa o criterio: BA Art.34; Aclaraciones1.4.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [01_presentacion_empresa/LAFROX-Subdocumento1.md, línea 188](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/01_presentacion_empresa/LAFROX-Subdocumento1.md:188>). Fragmento literal: «Los proyectos, volúmenes, números de certificado y alianzas de este capítulo son declarados por LafroX; su acreditación documental (certificados y cartas de referencia del Art. 34°) se entrega en el Sobre N° 1.».

### RV-028 — No está la revisión completa del Informe1 ni tabla exhaustiva T-22

- Severidad / tipo: Alta / Trazabilidad de revisión.
- Falencia y condición de cierre: El único archivo revision_informe_1 resume controles transversales y dice queSD7 no fue evaluado. El registro SD8 traza17 cambios propios, no todas las observaciones de SD1–5/13. No se puede calcular porcentaje de correcciones ni adoptar puntajes originales sin fuente.
- Fuente normativa o criterio: BA T-22; protocolo del prompt.
- Estado: Confirmado en las fuentes disponibles.
- Evidencia: [07_plan_trabajo_edt/retroalimentacion/revision_informe_1.md, línea 3](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/retroalimentacion/revision_informe_1.md:3>). Fragmento literal: «El Subdocumento 7 **no fue evaluado explícitamente** en el Informe 1.».

## Distinciones para evitar falsos positivos

- Los rangos UF del T-6 son montos de proyectos históricos en un campo que exige el propio formulario BA; no son por sí solos precios de esta oferta. Las pérdidas de $4,2 millones son un dato de negocio del Caso, no una tarifa de LafroX. Cualquier monto de la oferta sigue prohibido por Art.50.2.
- SD4 ya dimensiona CD-05 en A31/A32. La falencia es la hipótesis de multiplicidad y su verificación, no la ausencia de CD-05.
- OTIF 95 % en mes32 no se rechaza sólo por ser posterior a H12: el Caso capítulo18 permite al proponente fijar meta/momento. Se requiere consistencia y medición, no inventar un hito contractual diferente.
- El modelo de HH con supuestos está autorizado; la falta de validación se registra como brecha de evidencia. No se afirma contratación ni inviabilidad sólo porque una familia de rol exceda una categoría corporativa.
- La conservación de los catálogos históricos está autorizada; no se los modifica para ocultar diferencias ni se confunden con la línea activa.
- Un objetivo de reversión de40 minutos no es un tiempo medido; un puntaje FMEA no es probabilidad estadística; un registro de riesgos no resuelve una brecha técnica.

## Segunda pasada — Arquitectura, capacidad, identidad y operación

### RV-029 — SD4 utiliza recortes con conexiones cortadas

- Severidad / tipo: Alta / Figuras.
- Falencia y condición de cierre: Las figuras ARQL-21…28 se enlazan desde capas_recortes; en ARQL-24 se observan conexiones que entran/salen cortadas en el borde. La prohibición de recortar una imagen general para detalle está explícita. No se juzga tamaño impreso desde la captura del navegador.
- Fuente normativa o criterio: Aclaraciones §4.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4.md, línea 319](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4.md:319>). Fragmento literal: «![Negocio: monolito modular Laravel y sus doce módulos](https://raw.githubusercontent.com/PatricioH315/LafroX/a422d30baeaf69a3cce14909bf38e549f4f6d5fd/04/figuras/logica/capas_recortes/ARQL-24_Recorte_Negocio.png)».
- Comprobación adicional: Inspección visual del navegador: ARQL-24, imagen3061×344, conexiones cortadas; Talca también visible..

### RV-030 — Reinicio de VM-02 no demuestra indisponibilidad cero

- Severidad / tipo: Crítica / Continuidad.
- Falencia y condición de cierre: La única instancia de escritura se reinicia en otro nodo; D-05 la restaura hasta en4h. N+1 de hosts yCeph no mantiene un servicio SQL activo durante reinicio. Se necesita demostrar cómo el flujo de despacho continúa durante falla de instancia/host en05:30–07:00.
- Fuente normativa o criterio: Caso restricción1/RT-10.05; SD4 continuidad.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4.md, línea 1980](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4.md:1980>). Fragmento literal: «| Instancia de escritura VM-02 | Se reinicia en otro nodo del clúster. | D-05 restaura la base en hasta 4 h sin enlace. |».

### RV-031 — Reposición física de Concepción/plataformas no tiene plazo de recuperación demostrado

- Severidad / tipo: Alta / Continuidad.
- Falencia y condición de cierre: Un servidor en Concepción y un mini-PC por plataforma carecen de segundo cómputo local activo; la contingencia es reposición desdeTalca y reconstrucción central. Faltan transporte, detección, restauración y autonomía simultánea siWAN está caído. Fuentes/discos redundantes no cubren falla del equipo completo.
- Fuente normativa o criterio: Caso cap.10; BTT RTO/continuidad.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4.md, línea 1983](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4.md:1983>). Fragmento literal: «| Servidor de borde de Concepción | RAID 10 y fuentes redundantes. | Reposición del equipo y reconstrucción de su base desde el estado central. |».
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4.md, línea 1984](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4.md:1984>). Fragmento literal: «| Mini-PC de un cross-docking | Dos fuentes, dos SSD en RAID 1 y dos switches. | Reposición desde Talca y reconstrucción desde el estado central y SQS FIFO. |».

### RV-032 — Pasarela dimensionada con cantidad de cobros en efectivo

- Severidad / tipo: Alta / Volumetría.
- Falencia y condición de cierre: INT-09 usa11.800/22,14; ese volumen corresponde a cobros en efectivo del Caso, no pagos electrónicos. Hace falta volumen o supuesto explícito de pagos por tarjeta y comportamiento de solicitudes/respuestas/reintentos.
- Fuente normativa o criterio: Caso14.1; BTT dimensionamiento.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4-Anexos.md, línea 380](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4-Anexos.md:380>). Fragmento literal: «| INT-09 Pasarela de pago | 533 msg/día | 990 | 11.800 ÷ 22,14; peak × 1,857 |».
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4-Anexos.md, línea 1410](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4-Anexos.md:1410>). Fragmento literal: «| INT-09 Pasarela de pago | 533 | 990 | 11.800 ÷ 22,14; peak × 1,857 |».

### RV-033 — Régimen normal EDI usa cero del AS-IS en una tabla de solución futura

- Severidad / tipo: Media / Volumetría.
- Falencia y condición de cierre: INT-08 normal=0 actual, peak=1144 del escenarioE2. Para comparación normal/peak deE2, con la misma hipótesis11% y4mensajes, normal sería1400×0,11×4=616. Distinguir AS-IS, E1 yE2 y recalcular totales que dependan de ello.
- Fuente normativa o criterio: BTT/caso capacidad; SD3 alcanceE2.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4-Anexos.md, línea 1409](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4-Anexos.md:1409>). Fragmento literal: «| INT-08 Cadenas modernas EDI | 0 | 1.144 | 0 actual; 2.600 × 11 % × 4 |».

### RV-034 — Reserva agregada de terminales no coincide con reserva por plataforma

- Severidad / tipo: Media / Inventario.
- Falencia y condición de cierre: La memoria actual suma132+66+7=205 bodega, pero declara queT-11 mantiene un repuesto en cada una de tres plataformas:6 activos+3=9, total207. La corrección+2 sólo se explica en año3; armonizar también estado inicial, licencias/identidad y parque por fecha.
- Fuente normativa o criterio: BTT repuestos; T-11; SD4W.3.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4-Anexos.md, línea 1363](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4-Anexos.md:1363>). Fragmento literal: «- Terminales de bodega: se comparten entre turnos (RT-12.11; Bases Técnicas del caso, cap. 15, p. 27), sin personal de carga adicional (S-33), de modo que los fija el turno nocturno: 120 preparadores en Talca y 60 en Concepción (S-39). En Talca, 20 son de la cuadrilla de congelado (S-34): los productos de frío son 1.100 ÷ 8.400 = 13,1 % del surtido».

### RV-035 — Ventana de registro térmico vehicular no abarca todo retorno declarado

- Severidad / tipo: Alta / Volumetría.
- Falencia y condición de cierre: Se presupuestan162 lecturas por vehículo entre05:30 y19:00, mientras la propia memoria coloca retorno/sincronización entre17:00 y20:00. Para vehículo que retorna20:00, registrar hasta19:00 no materializa registro continuo. Definir inicio/fin por ruta y frío, incluyendo extensión y casos nocturnos, y recalcular.
- Fuente normativa o criterio: Caso criterio3; registro continuo.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4-Anexos.md, línea 287](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4-Anexos.md:287>). Fragmento literal: «Modo asíncrono para muestras y alarma local inmediata. Volumen: 10.584 lecturas/día en régimen y peak, por 21 puntos de cámara × 288 lecturas más 28 termógrafos × 162 lecturas entre 05:30 y 19:00 (6.048 + 4.536). Contraparte: IoT Core/ingesta central, requerida 24×7; el bloqueo M9–M5 permanece local y no espera a nube. Acuse remoto máximo de 30 seg».
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4-Anexos.md, línea 1373](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4-Anexos.md:1373>). Fragmento literal: «La temperatura separa cámaras y camiones: 21 puntos instalados × 288 lecturas/día = 6.048 lecturas de cámara, con la cámara de Concepción estimada por S-37, y 28 termógrafos × 162 lecturas/día entre 05:30 y 19:00 = 4.536 lecturas de camión; el total es 10.584 mensajes/día. Con 145 bytes por lectura, son 0,56 GB/año crudos, 0,14 GB/año almacenados c».

### RV-036 — Portal excluye adopción del canal tradicional en su cota

- Severidad / tipo: Alta / Capacidad.
- Falencia y condición de cierre: La memoria usa2600 sesiones por food service+cadenas, y su extremo también2600; SD3/4 ofrece portal opcional a11600 tradicionales. Faltan adopción/visitas/concurrencia por ese canal o una cota justificable. No se exige que todos lo usen, pero tampoco se puede denominar cota global sin ese supuesto.
- Fuente normativa o criterio: SD3alcance; BTT/caso capacidad.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4-Anexos.md, línea 1304](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4-Anexos.md:1304>). Fragmento literal: «La nube suma preventa, reparto, recepción, trazabilidad, guías, sincronización y el escenario EDI. Los aproximadamente 2.852 documentos/día peak son el total de DTE (34.000 ÷ 22,14 × 1,857), no sólo guías; tomarlos todos como guías a emitir antes de la salida es una cota conservadora. El portal queda separado: 2.600 ÷ 9 × 2 por SV-04 = 578 sesiones».

### RV-037 — Revocación inmediata comprometida y autorización offline prolongada requieren compatibilización

- Severidad / tipo: Alta / Seguridad.
- Falencia y condición de cierre: RNF-15.01/RT-12.07 promete revocación inmediata; SD4 reconoce que no puede prometerla mientras el equipo permanece sin señal. Precisar alcance, controles locales y decisión delCLIENTE sin rebajar unilateralmente requisito; no presentar14h de exposición como revocación cumplida.
- Fuente normativa o criterio: BTT RT-12.07; Caso autonomía.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4.md, línea 1019](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4.md:1019>). Fragmento literal: «Al finalizar el turno expiran la asignación y sus permisos. Si se denuncia pérdida de dispositivo o baja anticipada, Keycloak revoca el acceso conectado y el equipo borra los datos al recuperar conexión. Mientras permanezca sin señal no puede prometerse revocación remota inmediata: la duración de la asignación limita la exposición y la incidencia s».

### RV-038 — Conductor nuevo durante corte no puede darse de alta

- Severidad / tipo: Alta / Identidad.
- Falencia y condición de cierre: Ante rotación sin aviso, SD4 exigeOTP conectado y propone otro conductor ya habilitado. No acredita que el transportista tenga un suplente válido disponible para la misma ruta, por lo que un reemplazo no enrolado puede bloquear salida durante24h sinWAN. Ensayar ese caso y acordar contingencia válida sin cuentas compartidas.
- Fuente normativa o criterio: Caso restricciones2/6/9; SD3actores.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4.md, línea 1017](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4.md:1017>). Fragmento literal: «La aplicación conserva localmente una asignación firmada para el turno de hasta 14 horas y permite capturar eventos mientras no exista red. La caché local de identidad, de solo lectura y TTL de 24 horas, no acorta por sí sola la vigencia de esa asignación de terreno; tampoco la renueva. Una persona reemplazante que no fue dada de alta no obtiene un».

### RV-039 — M12 tiene nombres diferentes entre alcance y arquitectura

- Severidad / tipo: Media / Terminología.
- Falencia y condición de cierre: SD3 usaM12 Telemetría ySD4 general Flota/Activos; la EDT lo llamaM12 Frío. Definir nombre canónico y alcance en la matriz; evitar que mantenimiento mecánico excluido se incorpore por leerActivos como nueva función.
- Fuente normativa o criterio: Aclaraciones §3 nombres idénticos; Caso exclusiones.
- Evidencia: [03_esquema_solucion_alcance/LAFROX-Subdocumento3.md, línea 25](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/03_esquema_solucion_alcance/LAFROX-Subdocumento3.md:25>). Fragmento literal: «La solución organiza estas capacidades en doce módulos de negocio: M1 Recepción, M2 Inventario, M3 Preventa, M4 Rutas, M5 Preparación, M6 Reparto, M7 Cobranza y rendición, M8 Devoluciones y envases, M9 Calidad y trazabilidad, M10 Analítica, M11 Canal moderno y M12 Telemetría. Una base compartida provee identidad, integración, registro auditable, op».
- Evidencia: [03_esquema_solucion_alcance/LAFROX-Subdocumento3.md, línea 265](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/03_esquema_solucion_alcance/LAFROX-Subdocumento3.md:265>). Fragmento literal: «| Calidad, evidencia y flota | M9 Calidad y trazabilidad; M12 Telemetría | Retiro sanitario y control de cadena de frío. | 1 |».

### RV-040 — Pedido urbano después de las14:00 no tiene política cerrada

- Severidad / tipo: Alta / Alcance.
- Falencia y condición de cierre: RNG-15 da24h a urbanos antes14:00 y48h a otros; el registro reconoce tratamiento posterior aún sin definir. Faltan promesa mostrada, fecha límite, efecto enOTIF y prueba. La regla debe ser explícita antes de aceptar preventa.
- Fuente normativa o criterio: Caso decisiónpromesa; SD2arbitraje; SD3RNG-15.
- Evidencia: [03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md, línea 543](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md:543>). Fragmento literal: «Las reglas RNG-01, RNG-04, RNG-05 y RNG-07 recogen las decisiones adoptadas en el SD2, Anexo 2.2, S-08, S-04, S-03 y S-10, respectivamente. RNG-15 conserva la promesa del arbitraje 1 del SD2; permanece pendiente definir el tratamiento de pedidos urbanos posteriores a las 14:00. Los parámetros se configuran sin desarrollo (RF-17.02), conservando los».

### RV-041 — Excursión térmica depende de parámetros por producto aún no disponibles

- Severidad / tipo: Alta / Sanidad.
- Falencia y condición de cierre: RNG-04 describe menor/transitoria ycrítica/sostenida, peroV-11 no fija desviación/duración. Sin catálogo validado porCalidad no se verifican alertas, retención o vida remanente. Es dependencia de evidencia, no permiso para inventar umbrales sanitarios.
- Fuente normativa o criterio: Caso decisiones/criterio3; SD3S-04/V-11.
- Evidencia: [03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md, línea 565](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md:565>). Fragmento literal: «| V-11 | ¿Qué umbrales y duraciones de excursión térmica aplica cada tipo de producto? | Parámetros pendientes de RNG-04. | SD2, S-04, y RNG-04 ya definen alerta para excursión menor y transitoria, y bloqueo preventivo para crítica y sostenida; Calidad decide liberar, bloquear o rechazar. Los valores por producto siguen pendientes. | Jefa de Calida».

### RV-042 — Fin comunitario RabbitMQ publicado en SD4 no coincide con fuente oficial actual

- Severidad / tipo: Media / Tecnologías.
- Falencia y condición de cierre: A17 dice30-11-2026 para4.3; la tabla oficial consultada ahora indica31-01-2027. Es una fecha documental incorrecta, conservadora respecto de la actual; no prueba por sí sola software sin soporte. Actualizar referencia y programar la rama de liberación antes del inicioFeb2027.
- Fuente normativa o criterio: BTT vigencia tecnológica; fuente fabricante.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4-Anexos.md, línea 972](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4-Anexos.md:972>). Fragmento literal: «| RabbitMQ | 4.3.x | Comunidad: 30-11-2026. | Actualizar antes de esa fecha a rama soportada; no se presume licencia comercial. |».
- Comprobación adicional: Fuente primaria: https://www.rabbitmq.com/release-information.

Tecnologías verificadas sin discrepancia en la fecha declarada: Laravel13 seguridad17-03-2028 ([fabricante](https://laravel.com/framework/docs/13.x/releases)); PHP8.5 seguridad31-12-2029 ([fabricante](https://www.php.net/supported-versions.php)); PostgreSQL16 fin09-11-2028 ([fabricante](https://www.postgresql.org/support/versioning/)); Angular22 LTSjunio2028 orientativo ([fabricante](https://angular.dev/reference/releases)). La coherencia de estas fechas no demuestra compatibilidad integral ni vigencia por56 meses sin actualizaciones.


## Tercera pasada — Equipo, metodología y cobertura de alcance

### RV-043 — Roles mínimos funcional e integración no tienen correspondencia explícita

- Severidad / tipo: Alta / Equipo.
- Falencia y condición de cierre: BTT19.2 exige Líder Funcional100% en implementación y Líder de Integración permanente. SD1/SD8/T-14 nominan ocho líderes sin esos roles. No basta atribuir integración al arquitecto o funcionalidad a implantación sin matriz de responsabilidades/dedicación y competencias; la compatibilidad no se presume.
- Fuente normativa o criterio: BTT19.2; SD1estructura; T-15.
- Evidencia: [Bases/Bases_Tecnicas_Transversales.md, línea 867](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/Bases/Bases_Tecnicas_Transversales.md:867>). Fragmento literal: «| **Líder Funcional** | 100 % en implementación | Experiencia en la industria del caso. |».
- Evidencia: [Bases/Bases_Tecnicas_Transversales.md, línea 869](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/Bases/Bases_Tecnicas_Transversales.md:869>). Fragmento literal: «| **Líder de Integración** | Permanente en implementación | Experiencia en integración de sistemas heredados. |».

### RV-044 — Liderazgo de desarrollo100% no aparece en primeras ventanas

- Severidad / tipo: Alta / Recursos.
- Falencia y condición de cierre: T-15 tiene cero equivalentes DES meses1–3 y su curva estima ejecución por familias, mientras BTT pide Líder de Desarrollo100% en toda implementación. Explicitar esfuerzo/financiación/dedicación del líder y su mapeo a trabajos iniciales, sin añadir dos veces HH ya incluidas.
- Fuente normativa o criterio: BTT19.2; T-15curva; SD1nomina.
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 386](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:386>). Fragmento literal: «| 1 | 709.34 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 709.34 | 5 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 8 |».
- Evidencia: [07_plan_trabajo_edt/LAFROX-Formulario-T-15.md, línea 387](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/07_plan_trabajo_edt/LAFROX-Formulario-T-15.md:387>). Fragmento literal: «| 2 | 1736.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1736.00 | 4 | 3 | 2 | 1 | 0 | 2 | 3 | 2 | 17 |».

### RV-045 — Gestión del SD6 no materializa PMBOK adaptado

- Severidad / tipo: Alta / Metodologías.
- Falencia y condición de cierre: SD6 describe coordinación/Kanban pero no identifica PMBOK ni desarrolla cómo controla valor ganado, alcance, reservas yfrentes concretos. SD7/T-14 sí lo exigen en1.8.1. Un nombre enEDT no suple metodología desarrollada en6.1.
- Fuente normativa o criterio: Aclaraciones6.1; BTT RT-19.01/07.
- Evidencia: [06_metodologías/Subdocumento_6.md, línea 28](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/06_metodologías/Subdocumento_6.md:28>). Fragmento literal: «## 1.1 Metodología de gestión de proyecto».

### RV-046 — DevSecOps aparece opcional y sin criterios bloqueantes del proyecto

- Severidad / tipo: Alta / Metodologías.
- Falencia y condición de cierre: SD6 usa podrán integrarse/podrá describirse para pruebas eIaC; no nombra las herramientas concretas SD4 ni umbrales de puerta. BTT RT-04.05/06 impone pipeline y despliegue reproducible. Distinguir políticas corporativas delSD1 de compuertas efectivas del proyecto y concretarlas enT-10/calidad.
- Fuente normativa o criterio: BTT RT-04.03–09; Aclaraciones6.2.
- Evidencia: [06_metodologías/Subdocumento_6.md, línea 149](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/06_metodologías/Subdocumento_6.md:149>). Fragmento literal: «Durante las iteraciones de Construcción, los cambios podrán integrarse con frecuencia y someterse a pruebas automatizadas y verificaciones de seguridad, con el propósito de detectar problemas tempranamente. La infraestructura de los ambientes podrá describirse mediante archivos versionados para facilitar su revisión y reproducción. Estas prácticas ».

### RV-047 — La matriz SD6 que dice todas sólo contiene tres adquisiciones

- Severidad / tipo: Alta / Adquisiciones.
- Falencia y condición de cierre: Enumera sensores, pistola de barras yAWS; omite sala/racks/servidores, conectividad, software/soporte, equipos de terreno yservicios externos delT-11/SD7. Falta responsable, disponibilidad y dependencia por adquisición; el texto nuevo no completa la matriz.
- Fuente normativa o criterio: Aclaraciones6.1; BTT/caso provisión; T-14F5.
- Evidencia: [06_metodologías/Subdocumento_6.md, línea 100](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/06_metodologías/Subdocumento_6.md:100>). Fragmento literal: «Todas las adquisiciones se explicitan en la siguiente tabla.».

### RV-048 — ADR no cumplen fecha/estado/responsables verificables

- Severidad / tipo: Alta / Arquitectura.
- Falencia y condición de cierre: El Anexo4-O reúne ADR-01–22 con decisión/alternativas/criterio/evidencia, pero las fichas no muestran fecha efectiva ni estado de aprobación yresponsable de aprobación. La Base exige registro fechado; no confundir fecha de consulta de tecnología con fecha de decisión.
- Fuente normativa o criterio: BA Art.19; BTT RT-02.04.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4-Anexos.md, línea 625](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4-Anexos.md:625>). Fragmento literal: «**ADR-01. Estilo arquitectónico**».

### RV-049 — Portal de proveedores ofertado sin paquete específico identificado

- Severidad / tipo: Alta / Alcance.
- Falencia y condición de cierre: RF-12.22 yel SD4 incluyen portal de proveedores; los desarrollosE2 describen cadena/clientes/transportistas/costo. No hay en la EDT un paquete o criterio de portal proveedor, niT-12 asignado para eseRF. Un vínculo genérico M11→3.5.1 no demuestra cobertura de consultaOC por proveedor.
- Fuente normativa o criterio: T-12RF-12.22; SD4N-01–03; SD7cobertura100%.
- Evidencia: [03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md, línea 148](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md:148>). Fragmento literal: «| RF-12.22 | El portal de proveedores debe permitir consultar, en modo de solo lectura, el estado de sus órdenes de compra. | Sí (E2) | M11 Canal moderno | Paquete por asignar en el plan de trabajo | Prueba funcional con datos representativos en marcha blanca | Anexo 3.A, Tabla 3.A.1 | R18-13 | Caso, RT-16.30 |».


## Cuarta pasada — Coherencia visual y dimensionamiento de atención

### RV-050 — TTL de identidad8h en figura contra24h en diseño vigente

- Severidad / tipo: Alta / Figura/texto.
- Falencia y condición de cierre: La figuraARQL-27 dice caché localTTL8h; el texto4.1.18 yel catálogo actual declaran24h, yARQL-17 representa relevo24h. Redibujar/armonizar la versión de la figura; una tabla correcta no elimina esa contradicción interna.
- Fuente normativa o criterio: Aclaraciones §§3/4/7.1c; Caso autonomía.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4.md, línea 483](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4.md:483>). Fragmento literal: «![Seguridad: identidad y autorización transversal](https://raw.githubusercontent.com/PatricioH315/LafroX/a422d30baeaf69a3cce14909bf38e549f4f6d5fd/04/figuras/logica/capas_recortes/ARQL-27_Recorte_Seguridad.png)».
- Comprobación adicional: Captura en navegador: etiqueta Keycloak—IdP maestro+caché localTTL8h; texto línea1017:TTL24h..

### RV-051 — Observabilidad dibujaAMP/X-Ray/Grafana pero texto eligeCloudWatch único

- Severidad / tipo: Alta / Figura/texto.
- Falencia y condición de cierre: ARQL-28 muestraAMP, X-Ray yGrafanaOSS; el texto4.1.3.8/ADR-14 y4.2.3.3 eligen CloudWatch como única plataforma y descartan servicios separados. Armonizar diagramas, contratos, retenciones yoperación.
- Fuente normativa o criterio: Aclaraciones §§3/4/7.1c; BTT RT-03.16.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4.md, línea 552](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4.md:552>). Fragmento literal: «En on-premise, los colectores ADOT, con buffer en disco de 24 horas, recolectan la telemetría local y la exportan a la plataforma única en Amazon CloudWatch: Logs conserva los registros técnicos 12 meses en línea y 24 meses en archivo; Metrics conserva las métricas 13 meses; las trazas y los tableros operacionales también se alojan en CloudWatch (A».
- Comprobación adicional: Captura ARQL-28: AMP métricas13meses; X-Ray trazas30días; GrafanaOSS tableros..

### RV-052 — T-15 no financia en HH la mesa ySOC dimensionados enSD4

- Severidad / tipo: Crítica / Recursos/operación.
- Falencia y condición de cierre: SD4W.7 calcula7 puestos de mesa en hora cargada,2enotras17h yNOC/SOC24×7. T-15 declara un puesto de mesa468HH/mes y32HH/mes deSOC. En la misma base promedio, mesa necesita(7+17×2)×6×52/12=1066HH: diferencia598HH/mes. Un SOC24×7 requiere730HH/mes promedio, no32, salvo servicio externo explícitamente contratado/capacidad separada. Con128HH efectivos, las coberturas normales exigen techo1066/128=9mesa y6NOC+6SOC=21 equivalentes, antes de otras funciones;SD4usa17personas por horas nominales. Reconciliar productividad, turnos, contratos ycurvas antes de mantener147.328HH como presupuesto completo.
- Fuente normativa o criterio: BTT RT-11.17/21.06; SD4W.7; T-14/T-15.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4-Anexos.md, línea 1464](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4-Anexos.md:1464>). Fragmento literal: «- Dotación simultánea: (7 + 17 × 2) × 6 = 246 horas-posición semanales; 246 ÷ 42 = 5,86, pero la dotación no puede ser menor que las 7 posiciones simultáneas, por lo que la mesa requiere **7 personas**.».
- Comprobación adicional: Cálculo independiente:mesa1066contra468HH,598debrecha; el encuadre deSOCrequiere definir propio/subcontratado ysu imputación..

### RV-053 — Límite2391contactos incumple SLA de la franja valle

- Severidad / tipo: Media / Cálculo.
- Falencia y condición de cierre: A2391contactos/mes la memoria da4,99llegadas/hora en franja valle. Con2agentes y10min de atención, ErlangC daSL20s=76,51%, inferior80%. El límite por esa franja es aproximadamente2283,46contactos/mes, no2391. El escenario base2000sí pasa; año3 2258queda cerca del límite.
- Fuente normativa o criterio: BTT RT-21.06; SD4W.7.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4-Anexos.md, línea 1466](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4-Anexos.md:1466>). Fragmento literal: «- Capacidad máxima de siete agentes: Al resolver el mismo cálculo, el límite es 2.391 contactos/mes; 2.391 × 25 % ÷ 22,14 = 27,00 contactos/hora cargada y 2.391 × 75 % ÷ 22,14 ÷ 17 = 4,99 contactos/hora en las demás franjas.».
- Comprobación adicional: Reproducción M/M/c: A=λ/μ, μ=6/h; C=[A^c/c!×c/(c−A)]/[Σ(k=0…c−1)A^k/k!+A^c/c!×c/(c−A)]; SL(t)=1−C×exp[−(cμ−λ)t], t=20/3600h..

### RV-054 — ErlangC no verifica abandono ni resolución al primer contacto

- Severidad / tipo: Alta / Método de atención.
- Falencia y condición de cierre: La memoria afirma cálculo con abandono≤5%, pero ErlangC supone cola sin abandono. No presenta distribución de paciencia ni datos que demuestren70% de primera resolución. Dimensionamiento puedeprobar espera bajo supuestos; los otros dosSLA requieren modelos/datos yprocedimiento distintos.
- Fuente normativa o criterio: BTT RT-21.06.
- Evidencia: [04_arquitectura/LAFROX-Subdocumento4-Anexos.md, línea 1462](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/04_arquitectura/LAFROX-Subdocumento4-Anexos.md:1462>). Fragmento literal: «- Resultado Erlang C: con 10 minutos de atención media, 80 % de respuestas antes de 20 segundos y abandono ≤5 %, exige 7 agentes en la hora cargada y 2 en las demás.».
- Comprobación adicional: El modelo reproducido tiene infinitapaciencia; no se ejecutó ErlangA ni se midieron tickets..

### RV-055 — CadenciasSD6/SD8 omiten Comité de Operación mensual desde13

- Severidad / tipo: Media / Gobierno.
- Falencia y condición de cierre: Los textos nuevos describen Proyecto/Ejecutivo/Arquitectura pero no desarrollan el Comité de Operación desde mes13. T-14 sí tiene1.8.5 yBA71loimpone. Incorporar ciclo, participantes, métricas yactas; no basta haber nombrado sólo tres comités.
- Fuente normativa o criterio: BA Art.71; BTT RT-19.09.
- Evidencia: [06_metodologías/Subdocumento_6.md, línea 110](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/LafroX_Markdown/06_metodologías/Subdocumento_6.md:110>). Fragmento literal: «El Comité Ejecutivo y el Comité de Arquitectura se reúnen mensualmente; el Comité de Proyecto, quincenalmente, revisa avance y registro vivo de riesgos (BTT RT-19.04 y gobierno de SD7). La reunión semanal de seguimiento prepara los datos y no reemplaza estos comités.».
- Comprobación adicional: BA71yT-14paquete1.8.5están disponibles; falta desarrollo en el gobierno deSD6/8..


## Estado de cierre

La revisión sigue activa. Este registro conserva resultados comprobados y la cobertura que falta; no autoriza publicar la propuesta ni contiene cambios de diseño. No se crearon archivos distintos de Markdown, no se cambió checkout y no hubo commit/push. La copia sigue sin Git.
