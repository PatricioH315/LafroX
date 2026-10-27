# Formulario T-14 — Estructura de desglose del trabajo

> Texto extraído del [PDF final](LAFROX-Formulario-T-14.pdf). Las figuras y la composición visual se consultan en el PDF.

LafroX SpA
LICITACIÓN PÚBLICA
Licitación N.° TFEP-01/2026
Proyecto de Plataforma Digital de Misión Crítica
Caso — Logística
Sobre N.° 2 — Oferta Técnica
Propuesta Técnica
Formulario T-14 — Plan de Trabajo, EDT y Carta Gantt
Subdocumento 07 · Formulario T-14
MANDANTE
Distribuidora Puelche S.A.
PROPONENTE
LafroX SpA
RUT 77.418.902-K
Av. Brasil 2241, Valparaíso
REPRESENTANTE LEGAL
Alex Aravena
Jefe de Proyecto y Apoderado
contacto@lafrox.cl
+56 32 250 4100
FECHA DE EMISIÓN
12 de octubre de 2026
FIRMA DEL REPRESENTANTE LEGAL
Alex Aravena
Jefe de Proyecto y Apoderado · LafroX SpA
LAFROX-Formulario-T-14.pdf 1


---

LafroX SpA
Índice general
Índice general 2
Lista de tablas 4
Lista de figuras 6
Formulario T-14: Plan de trabajo, EDT y carta Gantt 7
1 Estructura de descomposición del trabajo 7
2 Diccionario de la EDT 20
2.1 Fase 1. Inicio 21
2.1.1 Cuenta 1.1 — Definición inicial del proyecto 21
2.1.2 Cuenta 1.2 — Alcance del proyecto 21
2.1.3 Cuenta 1.3 — Planificación del proyecto 23
2.1.4 Cuenta 1.4 — Gestión de interesados y comunicaciones 24
2.1.5 Cuenta 1.5 — Gestión de calidad 25
2.1.6 Cuenta 1.6 — Gestión de riesgos 26
2.1.7 Cuenta 1.7 — Plan de Reversibilidad 27
2.1.8 Cuenta 1.8 — Gobierno y control del proyecto 28
2.1.9 Cuenta 1.9 — Cumplimiento normativo y contractual 30
2.2 Fase 2. Elaboración 31
2.2.1 Cuenta 2.1 — Arquitectura de la solución 31
2.2.2 Cuenta 2.2 — Diseño de la seguridad 32
2.2.3 Cuenta 2.3 — Diseño de la sala técnica y de los racks 33
2.2.4 Cuenta 2.4 — Validación de diseños 34
2.2.5 Cuenta 2.5 — Continuidad del negocio 35
2.2.6 Cuenta 2.6 — Experiencia de usuario 36
2.3 Fase 3. Construcción 37
2.3.1 Cuenta 3.1 — Ambientes y cadena de desarrollo 37
2.3.2 Cuenta 3.2 — Servicios de nube de la plataforma 39
2.3.3 Cuenta 3.3 — Base compartida 40
2.3.4 Cuenta 3.4 — Módulos de la Etapa 1 41
2.3.5 Cuenta 3.5 — Módulos de la Etapa 2 44
2.3.6 Cuenta 3.6 — Integraciones externas 45
2.3.7 Cuenta 3.7 — Migración de datos 47
2.3.8 Cuenta 3.8 — Pruebas de la Etapa 1 48
2.3.9 Cuenta 3.9 — Pruebas de la Etapa 2 50
2.3.10 Cuenta 3.10 — Innovaciones 52
2.3.11 Cuenta 3.11 — Documentación técnica 55
2.4 Fase 4. Transición 56
2.4.1 Cuenta 4.1 — Plan de implantación 56
2.4.2 Cuenta 4.2 — Marcha blanca y producción de la Etapa 1 58
2.4.3 Cuenta 4.3 — Marcha blanca y producción de la Etapa 2 60
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
2


---

LafroX SpA
2.5 Fase 5. Adquisiciones y contrataciones 63
2.5.1 Cuenta 5.1 — Hardware e infraestructura 63
2.5.2 Cuenta 5.2 — Servicios de nube y licencias 64
2.5.3 Cuenta 5.3 — Enlaces de comunicaciones 65
2.5.4 Cuenta 5.4 — Acuerdos con terceros 66
2.6 Fase 6. Infraestructura física y sitios 67
2.6.1 Cuenta 6.1 — Adecuación de la sala técnica de Talca 67
2.6.2 Cuenta 6.2 — Cableado estructurado 69
2.6.3 Cuenta 6.3 — Montaje de racks y gabinetes 70
2.6.4 Cuenta 6.4 — Sistemas de seguridad física 71
2.6.5 Cuenta 6.5 — Equipamiento de campo 72
2.6.6 Cuenta 6.6 — Configuración de la infraestructura de los sitios 73
2.7 Fase 7. Capacitación y gestión del cambio 74
2.7.1 Cuenta 7.1 — Capacitación por roles 74
2.7.2 Cuenta 7.2 — Gestión del cambio 76
2.7.3 Cuenta 7.3 — Evaluaciones y certificaciones 77
2.8 Fase 8. Operación y soporte (36 meses) 77
2.8.1 Cuenta 8.1 — Servicios de operación 77
2.8.2 Cuenta 8.2 — Mantenimiento 80
2.8.3 Cuenta 8.3 — Innovaciones en operación 82
2.8.4 Cuenta 8.4 — Informes y obligaciones periódicas 84
2.8.5 Cuenta 8.5 — Capacitación y transferencia en operación 85
2.9 Fase 9. Cierre 86
2.9.1 Cuenta 9.1 — Cierre de la implementación 86
2.9.2 Cuenta 9.2 — Salida al término del contrato 87
3 Carta Gantt 89
4 Criterios vigentes de programación y recursos 102
Referencias 102
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
3


---

LafroX SpA
Lista de tablas
Tabla 1 Cuentas de control y paquetes de trabajo por fase. 7
Tabla 2 Responsables de los paquetes. 20
Tabla 3 Diccionario de la cuenta 1.1. 21
Tabla 4 Diccionario de la cuenta 1.2. 22
Tabla 5 Diccionario de la cuenta 1.3. 23
Tabla 6 Diccionario de la cuenta 1.4. 24
Tabla 7 Diccionario de la cuenta 1.5. 25
Tabla 8 Diccionario de la cuenta 1.6. 27
Tabla 9 Diccionario de la cuenta 1.7. 27
Tabla 10 Diccionario de la cuenta 1.8. 28
Tabla 11 Diccionario de la cuenta 1.9. 30
Tabla 12 Diccionario de la cuenta 2.1. 32
Tabla 13 Diccionario de la cuenta 2.2. 33
Tabla 14 Diccionario de la cuenta 2.3. 34
Tabla 15 Diccionario de la cuenta 2.4. 35
Tabla 16 Diccionario de la cuenta 2.5. 36
Tabla 17 Diccionario de la cuenta 2.6. 37
Tabla 18 Diccionario de la cuenta 3.1. 38
Tabla 19 Diccionario de la cuenta 3.2. 39
Tabla 20 Diccionario de la cuenta 3.3. 40
Tabla 21 Diccionario de la cuenta 3.4. 42
Tabla 22 Diccionario de la cuenta 3.5. 45
Tabla 23 Diccionario de la cuenta 3.6. 46
Tabla 24 Diccionario de la cuenta 3.7. 47
Tabla 25 Diccionario de la cuenta 3.8. 48
Tabla 26 Diccionario de la cuenta 3.9. 50
Tabla 27 Diccionario de la cuenta 3.10. 52
Tabla 28 Diccionario de la cuenta 3.11. 55
Tabla 29 Diccionario de la cuenta 4.1. 57
Tabla 30 Diccionario de la cuenta 4.2. 59
Tabla 31 Diccionario de la cuenta 4.3. 61
Tabla 32 Diccionario de la cuenta 5.1. 63
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
4


---

LafroX SpA
Tabla 33 Diccionario de la cuenta 5.2. 65
Tabla 34 Diccionario de la cuenta 5.3. 66
Tabla 35 Diccionario de la cuenta 5.4. 67
Tabla 36 Diccionario de la cuenta 6.1. 68
Tabla 37 Diccionario de la cuenta 6.2. 69
Tabla 38 Diccionario de la cuenta 6.3. 70
Tabla 39 Diccionario de la cuenta 6.4. 72
Tabla 40 Diccionario de la cuenta 6.5. 72
Tabla 41 Diccionario de la cuenta 6.6. 74
Tabla 42 Diccionario de la cuenta 7.1. 75
Tabla 43 Diccionario de la cuenta 7.2. 76
Tabla 44 Diccionario de la cuenta 7.3. 77
Tabla 45 Diccionario de la cuenta 8.1. 79
Tabla 46 Diccionario de la cuenta 8.2. 81
Tabla 47 Diccionario de la cuenta 8.3. 83
Tabla 48 Diccionario de la cuenta 8.4. 85
Tabla 49 Diccionario de la cuenta 8.5. 86
Tabla 50 Diccionario de la cuenta 9.1. 87
Tabla 51 Diccionario de la cuenta 9.2. 88
Tabla 52 Períodos contractuales e hitos. 90
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
5


---

LafroX SpA
Lista de figuras
Figura 1 Vista panorámica de la EDT completa del proyecto. Para consultar el detalle
por fase, véanse las láminas de la sección «Estructura general» del Subdocumento 7. 19
Figura 2 Carta Gantt de los 56 meses por período contractual, con inicio en febrero de
2027. 91
Figura 3 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 1 de 7
(filas 1 a 23 de 155), con inicio en febrero de 2027. 93
Figura 4 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 2 de 7
(filas 24 a 45 de 155), con inicio en febrero de 2027. 94
Figura 5 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 3 de 7
(filas 46 a 67 de 155), con inicio en febrero de 2027. 95
Figura 6 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 4 de 7
(filas 68 a 89 de 155), con inicio en febrero de 2027. 96
Figura 7 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 5 de 7
(filas 90 a 111 de 155), con inicio en febrero de 2027. 97
Figura 8 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 6 de 7
(filas 112 a 133 de 155), con inicio en febrero de 2027. 98
Figura 9 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 7 de 7
(filas 134 a 155 de 155), con inicio en febrero de 2027. 99
Figura 10 Vista crítica de la carta Gantt: paquetes de la ruta crítica y sus dependencias
hasta H6 y H11. 101
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
6


---

Formulario T-14: Plan de trabajo, EDT y
carta Gantt
Este formulario detalla lo que el Subdocumento 7 resume en sus secciones 7.1 y 7.3, confor-
me al Formulario T-14 de las Bases Administrativas. Contiene la estructura de descomposición
del trabajo (EDT) completa; su diccionario, con el entregable, el criterio de aceptación, el
responsable y el período de cada paquete; y la carta Gantt de los 56 meses del contrato, con
el detalle de las Etapas 1 y 2. El método de estimación y programación, la ruta crítica y los
frentes de trabajo se detallan en el Formulario T-15, y la implantación de cada etapa, en el
Formulario T-18. La EDT termina en el paquete de trabajo; la descomposición de cada paquete
en actividades de 8 a 80 horas hombre que caben en una quincena, con sus fechas, está en el
Formulario T-15, sección 6.
En este formulario, BA, BTT y Caso designan las Bases Administrativas, las Bases Técnicas
Transversales y las Bases Técnicas del caso.
1 Estructura de descomposición del trabajo
La EDT descompone el 100 % del alcance de la Etapa 1, la Etapa 2 y la Operación (BA, art.
15, p. 11) en nueve fases, 49 cuentas de control y 227 paquetes de trabajo. Las fases 1 a 4 son
las del proceso de desarrollo declarado en el Capítulo 6 (Inicio, Elaboración, Construcción
y Transición) y se recorren una vez por etapa. Las fases 5 a 9 agrupan el trabajo que no es
desarrollo de software. Cada paquete es la hoja de su rama, tiene un único responsable y
produce un entregable verificable. En la cuenta 3.10, cada innovación agrupa sus paquetes en
un cuarto nivel. La Tabla 1 resume el tamaño de cada fase.
Tabla 1 Cuentas de control y paquetes de trabajo por fase. Fuente: (Bases Administrativas, arts. 17.2–17.6 y
Formulario T-14, p. 63); (Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Fase Cuentas de control Paquetes de trabajo
1. Inicio 9 35
2. Elaboración 6 20
3. Construcción 11 79
4. Transición 3 11
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
7


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 1 — continuación
Fase Cuentas de control Paquetes de trabajo
5. Adquisiciones y contratacio-
nes
4 15
6. Infraestructura física y sitios 6 24
7. Capacitación y gestión del
cambio
3 13
8. Operación y soporte (36 me-
ses)
5 26
9. Cierre 2 4
Total 49 227
La construcción concentra 79 de los 227 paquetes, y las fases que no son software (5 a 7)
suman 52. Ninguna cuenta de control tiene un solo paquete. La estructura completa es la
siguiente, con la raíz «Plataforma logística de Distribuidora Puelche» y sus nueve fases en el
primer nivel.
• 1. Inicio
• 1.1 Definición inicial del proyecto
• 1.1.1 Acta de constitución del proyecto, firmada con la Contraparte Técnica
• 1.1.2 Documento de validación con el CLIENTE de los problemas y metas del proyecto
• 1.1.3 Acta de confirmación con el CLIENTE de la fecha de inicio, la evidencia para el
proveedor de lácteos, las ventanas de paso a producción y el acuse tributario
• 1.2 Alcance del proyecto
• 1.2.1 Documento de especificación de requerimientos y línea base de alcance de la Etapa 1
(H1)
• 1.2.2 Documento de reglas de ruteo capturadas al planificador de rutas
• 1.2.3 Documento de especificación de las interfaces sin documentación del ERP, del WMS
de 2013 y de la telemetría del tercero
• 1.2.4 Matriz de trazabilidad: requerimiento, módulo, paquete y prueba (H1)
• 1.2.5 Documento de línea base de alcance de la Etapa 2: canal moderno y costo de servir
(H8)
• 1.3 Planificación del proyecto
• 1.3.1 Plan para la dirección del proyecto, con el calendario de congelamientos de septiembre,
diciembre y el cierre mensual
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
8


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
• 1.3.2 EDT y diccionario de la EDT (línea base del alcance)
• 1.3.3 Carta Gantt de 56 meses con los hitos H1 a H12 y la ruta crítica
• 1.3.4 Documento de nivelación de recursos y frentes del solapamiento de los meses 13 a 15
y 19 a 20
• 1.3.5 Reunión semanal de seguimiento con su informe semanal
• 1.4 Gestión de interesados y comunicaciones
• 1.4.1 Registro de interesados con su influencia, interés y estrategia
• 1.4.2 Plan de comunicaciones con calendario y canales por grupo de interés
• 1.4.3 Registro de solicitudes de cambio con análisis de impacto
• 1.5 Gestión de calidad
• 1.5.1 Plan de calidad y plan de pruebas
• 1.5.2 Puertas de calidad automáticas en la cadena de integración (cobertura mínima del
80 %)
• 1.6 Gestión de riesgos
• 1.6.1 Plan de riesgos y registro inicial de riesgos según ISO 31000
• 1.6.2 Registro de riesgos revisado en cada Comité de Proyecto
• 1.7 Plan de Reversibilidad
• 1.7.1 Plan de Reversibilidad inicial (primeros 90 días)
• 1.7.2 Primera actualización anual del Plan de Reversibilidad durante la implementación
• 1.8 Gobierno y control del proyecto
• 1.8.1 Oficina de gestión del proyecto con metodología basada en el PMBOK
• 1.8.2 Actas del Comité Ejecutivo mensual, con la aprobación de los cambios de alcance
• 1.8.3 Actas del Comité de Proyecto quincenal
• 1.8.4 Actas del Comité de Arquitectura mensual
• 1.8.5 Actas del Comité de Operación mensual, desde el mes 13
• 1.8.6 Informe mensual de avance con valor ganado
• 1.8.7 Tablero de estado del proyecto disponible para el CLIENTE
• 1.8.8 Espacio colaborativo con la documentación, los entregables, las actas, los riesgos y
los cambios
• 1.9 Cumplimiento normativo y contractual
• 1.9.1 Matriz de cumplimiento normativo por obligación legal, con su control y su evidencia
• 1.9.2 Acuerdo de tratamiento de datos personales con el CLIENTE
• 1.9.3 Registro de actividades de tratamiento y evaluación de impacto en protección de datos
• 1.9.4 Certificación ISO/IEC 27001 vigente y entrega anual de los informes de certificación
• 1.9.5 Garantía de fiel cumplimiento, seguros y certificados laborales vigentes durante el
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
9


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
contrato
• 2. Elaboración
• 2.1 Arquitectura de la solución
• 2.1.1 Documento de arquitectura lógica: capas, módulos M1 a M12 e interfaces
• 2.1.2 Documento de arquitectura física híbrida: nube, centros de distribución y plataformas
de cross-docking
• 2.1.3 Modelo de datos y diccionario de datos, con la trazabilidad por lote
• 2.1.4 Documento de diseño detallado de M11 y del intercambio con las cadenas
• 2.2 Diseño de la seguridad
• 2.2.1 Plan de seguridad de la información
• 2.2.2 Modelado de amenazas por componente y por integración externa, actualizado ante
cada cambio
• 2.2.3 Plan de respuesta a incidentes de seguridad, con aviso al CLIENTE en dos horas
• 2.2.4 Matriz de clasificación de la información y matriz de controles
• 2.3 Diseño de la sala técnica y de los racks
• 2.3.1 Plano de la sala técnica de Talca, con su cálculo eléctrico y térmico
• 2.3.2 Plano de distribución de los racks R01 de servidores y R02 de comunicaciones
• 2.3.3 Plano de los gabinetes de borde de Concepción y de las plataformas de cross-docking
• 2.4 Validación de diseños
• 2.4.1 Acta de aprobación de la arquitectura, el plan de seguridad y el modelo de datos (H2)
• 2.4.2 Acta de aprobación del diseño detallado de la Etapa 2 (H8)
• 2.4.3 Validación del diseño del kit en banco de pruebas
• 2.4.4 Mapeo térmico por tipo de carrocería
• 2.5 Continuidad del negocio
• 2.5.1 Plan de continuidad del negocio según ISO 22301, con análisis de impacto y procedi-
mientos manuales
• 2.5.2 Plan de continuidad TIC según ISO/IEC 27031 y plan de recuperación ante desastres
• 2.6 Experiencia de usuario
• 2.6.1 Investigación con preparadores, preventistas, conductores y almaceneros
• 2.6.2 Prototipos y pruebas de usabilidad con participantes del CLIENTE
• 2.6.3 Indicadores de usabilidad comprometidos por transacción crítica
• 3. Construcción
• 3.1 Ambientes y cadena de desarrollo
• 3.1.1 Ambientes de Desarrollo y QA en la nube (H3)
• 3.1.2 Ambientes de Preproducción y Producción en la nube (H3)
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
10


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
• 3.1.3 Ambiente de recuperación ante desastres en la región secundaria (H3)
• 3.1.4 Cadena de integración y entrega continua, e infraestructura como código
• 3.1.5 Observabilidad de los doce módulos y de los sitios, con tableros para el CLIENTE (H3)
• 3.2 Servicios de nube de la plataforma
• 3.2.1 Servicio de nube para la aplicación y los portales
• 3.2.2 Servicio de nube de base de datos, caché y mensajería
• 3.2.3 Servicio de nube de ingesta de IoT, telemetría cruda y plataforma analítica
• 3.2.4 Servicio de nube de respaldo inmutable y réplica entre regiones
• 3.2.5 Servicio de nube de seguridad y gobierno, y detección en endpoints
• 3.2.6 Servicio de gestión de dispositivos móviles
• 3.3 Base compartida
• 3.3.1 Identidad y control de acceso, incluidos los conductores externos que rotan sin aviso
• 3.3.2 Integración con el ERP como único emisor de la guía de despacho (INT-06 e INT-07)
• 3.3.3 Convivencia con el WMS de 2013 durante el reemplazo
• 3.3.4 Integración con la telemetría de los 42 camiones propios (INT-15)
• 3.3.5 Registro auditable de stock, lotes y cobros
• 3.3.6 Operación sin conexión: 14 horas en terreno y 24 horas en el CD
• 3.4 Módulos de la Etapa 1
• 3.4.1 Recepción de mercadería con captura de lote y vencimiento (M1 Recepción)
• 3.4.2 Inventario por ubicación y lote, con FEFO y conteo cíclico (M2 Inventario)
• 3.4.3 Preparación de pedidos en el turno de noche y en la cámara de congelado (M5 Prepa-
ración)
• 3.4.4 Cadena de frío, retención por SSCC y retiro sanitario (M9 Calidad y trazabilidad)
• 3.4.5 Ingesta de temperatura (M9) y posición de flota (M12)
• 3.4.6 Aplicación móvil de preventa sin conexión, con stock y crédito (M3 Preventa)
• 3.4.7 Planificación de rutas corregible por el planificador (M4 Rutas)
• 3.4.8 Aplicación móvil de reparto con prueba de entrega digital (M6 Reparto)
• 3.4.9 Devoluciones en terreno y control de envases (M8 Devoluciones y envases)
• 3.4.10 Cobro en ruta, rendición y conciliación (M7 Cobranza y rendición)
• 3.4.11 Indicadores operacionales y OTIF diario (M10 Analítica)
• 3.5 Módulos de la Etapa 2
• 3.5.1 Pedido electrónico y aviso de despacho para las cadenas, y portal de proveedores
(M11 Canal moderno)
• 3.5.2 Portal web de clientes: cuenta, saldo, entregas y documentos
• 3.5.3 Portal web de transportistas: rutas asignadas del día siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
11


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
• 3.5.4 Costo de servir por cliente y por entrega (M10 Analítica)
• 3.6 Integraciones externas
• 3.6.1 Intercambio de lote y trazabilidad con los proveedores
• 3.6.2 Integración con la pasarela de pago para el cobro con tarjeta (INT-09)
• 3.6.3 Integración con el servicio de mapas y geocodificación (INT-10)
• 3.6.4 Integración con el servicio de avisos al cliente (INT-11)
• 3.6.5 Intercambio electrónico con la principal cadena, con sus pruebas aprobadas (INT-08)
• 3.6.6 Incorporación de las demás cadenas al intercambio electrónico (INT-08)
• 3.7 Migración de datos
• 3.7.1 Informe de perfilamiento y datos saneados
• 3.7.2 Datos maestros cargados: 8.400 SKU, clientes e instalaciones
• 3.7.3 Saldos migrados desde el WMS de Talca
• 3.7.4 Saldos cargados en Concepción desde el conteo físico
• 3.7.5 Acta de conciliación y corte fuera de las ventanas de congelamiento
• 3.8 Pruebas de la Etapa 1
• 3.8.1 Pruebas de integración, regresión e idempotencia en QA (H4)
• 3.8.2 Pruebas de aceptación y de accesibilidad con preventistas, conductores y bodega
• 3.8.3 Pruebas del perfil operacional: cinco condiciones físicas y desconexión de 14 horas
• 3.8.4 Pruebas de carga con el peak de septiembre y de resiliencia
• 3.8.5 Prueba de recuperación ante desastres con conmutación real
• 3.8.6 Prueba de seguridad ofensiva de la Etapa 1, por un tercero independiente
• 3.8.7 Acta de certificación de la Etapa 1 (H5)
• 3.8.8 Demostración en Preproducción del despliegue sin interrupción de la Etapa 1
• 3.9 Pruebas de la Etapa 2
• 3.9.1 Pruebas de integración y regresión sin afectar la Etapa 1 en producción (H9)
• 3.9.2 Pruebas de aceptación y de accesibilidad con cadenas, transportistas, Comercial y
Finanzas
• 3.9.3 Pruebas de carga con ambas etapas activas y de resiliencia
• 3.9.4 Prueba de recuperación ante desastres con ambas etapas
• 3.9.5 Prueba de seguridad ofensiva de la Etapa 2, por un tercero independiente
• 3.9.6 Acta de certificación de la Etapa 2 y cierre del desarrollo (H10)
• 3.9.7 Demostración en Preproducción del despliegue sin interrupción de la Etapa 2
• 3.10 Innovaciones
• 3.10.1 Innovación 1: seguimiento de vencimiento posentrega en el local
• 3.10.1.1 Documento de catálogo de acciones y protocolo del piloto (INN-01.P1)
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
12


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
• 3.10.1.2 Estimador de saldo y ritmo de reposición (INN-01.P2)
• 3.10.1.3 Función de lista sin conexión en la aplicación de preventa (INN-01.P3)
• 3.10.1.4 Informe del piloto en marcha blanca y habilitación (INN-01.P4)
• 3.10.2 Innovación 2: reproducción de incidentes de terreno
• 3.10.2.1 Informe de medición inicial y contrato de evidencia (INN-02.P1)
• 3.10.2.2 Circuito mínimo de reproducción en la preventa (INN-02.P2)
• 3.10.2.3 Captura de evidencia en las aplicaciones de preventa, preparación y reparto (INN-
02.P3)
• 3.10.2.4 Informe de validación comparada durante la implementación (INN-02.P4, primera
parte)
• 3.10.3 Innovación 3: vida útil remanente por historia térmica del lote
• 3.10.3.1 Documento de familias priorizadas y parámetros aprobados (INN-03.P1)
• 3.10.3.2 Asociación lote–sensor en el borde y en el camión (INN-03.P2)
• 3.10.3.3 Vista en M9 y orden de salida sugerido (INN-03.P3)
• 3.10.3.4 Informe de validación en marcha blanca con Calidad (INN-03.P4)
• 3.10.4 Innovación 5: hoja de negocio del almacenero
• 3.10.4.1 Prototipo e informe de la prueba de comprensión (INN-05.P1)
• 3.10.4.2 Evaluación de privacidad y diseño de la impresión en cabina (INN-05.P2)
• 3.10.4.3 Cálculo y bloques 1 a 3 de la hoja de negocio (INN-05.P3)
• 3.10.4.4 Hoja certificada, en marcha blanca y en producción (INN-05.P4, primera parte)
• 3.11 Documentación técnica
• 3.11.1 Documentación técnica, funcional, de arquitectura, de operación y de seguridad
• 3.11.2 Base de conocimiento de incidentes y decisiones de diseño
• 3.11.3 Estándares de codificación y documentación de interfaces en OpenAPI y AsyncAPI
• 3.11.4 Inventario de componentes (SBOM) con sus licencias de código abierto
• 3.11.5 Depósito del código fuente en el repositorio del CLIENTE en cada liberación
• 4. Transición
• 4.1 Plan de implantación
• 4.1.1 Plan de olas de la Etapa 1 por sitio y zona: Talca, Concepción y plataformas de cross-
docking
• 4.1.2 Procedimiento de reversión de la Etapa 1 antes de las 05:30, con versión operativa
local y DTE emitidos por el ERP
• 4.1.3 Plan de implantación y reversión de la Etapa 2 fuera de la ventana de 05:30 a 07:00
• 4.1.4 Piloto de cadena de frío en cuatro camiones
• 4.2 Marcha blanca y producción de la Etapa 1
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
13


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
• 4.2.1 Marcha blanca de la Etapa 1 con conciliación diaria (H6)
• 4.2.2 Estabilización de la Etapa 1 en el turno de noche y acompañamiento en ruta
• 4.2.3 Acta de aceptación de la Etapa 1 (H7)
• 4.3 Marcha blanca y producción de la Etapa 2
• 4.3.1 Marcha blanca de la Etapa 2 en convivencia con la Etapa 1 y fuente única de datos
(H11)
• 4.3.2 Estabilización de la Etapa 2 con Comercial, Finanzas, cadenas y transportistas
• 4.3.3 Acta de aceptación final de la implementación (H12)
• 4.3.4 Garantía de correcto funcionamiento constituida, condición de la aceptación final
(H12)
• 5. Adquisiciones y contrataciones
• 5.1 Hardware e infraestructura
• 5.1.1 Especificación de compra de equipos de uso para el CLIENTE
• 5.1.2 Especificación y compra de la sala técnica, los racks, los servidores y los gabinetes de
borde
• 5.1.3 Actas de recepción técnica del equipamiento de terreno comprado por el CLIENTE y
de la infraestructura provista por LafroX
• 5.1.4 Especificación y compra del sistema de cadena de frío
• 5.2 Servicios de nube y licencias
• 5.2.1 Contrato de los servicios de AWS
• 5.2.2 Suscripción del servicio de gestión de dispositivos y de detección en endpoints
• 5.2.3 Licencias de software de terceros constituidas a nombre del CLIENTE
• 5.3 Enlaces de comunicaciones
• 5.3.1 Contrato de fibra óptica de los CD de Talca y Concepción
• 5.3.2 Contrato de planes LTE con dos proveedores (ocho planes)
• 5.3.3 Contrato de Starlink para los cinco sitios: Talca, Concepción y las tres plataformas de
cross-docking
• 5.3.4 Contrato de SIM M2M y servicio satelital de los camiones con frío
• 5.4 Acuerdos con terceros
• 5.4.1 Acuerdos operacionales firmados con los diez transportistas
• 5.4.2 Acta de acuerdo con el sindicato sobre terminales, GPS y cámaras
• 5.4.3 Fórmula aprobada del tramo variable: reglas de atribución, canasta e índices (INN-
04.P1)
• 5.4.4 Contrato de custodia de fuentes con un tercero independiente
• 6. Infraestructura física y sitios
• 6.1 Adecuación de la sala técnica de Talca
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
14


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
• 6.1.1 Coordinación de la obra civil de separación, a cargo del CLIENTE (RT-06.06), y piso
técnico de la sala
• 6.1.2 Hardware de energía instalado: UPS modular N+1, generador con 24 horas de autono-
mía, transferencia automática y PDU A/B
• 6.1.3 Hardware de climatización de precisión N+1 instalado
• 6.1.4 Hardware de detección temprana de incendio y extinción por agente limpio instalado
• 6.1.5 Acta de recepción técnica de la sala
• 6.2 Cableado estructurado
• 6.2.1 Cableado de cobre Cat6A y fibra OM4 tendido, con dos ductos de ingreso independien-
tes
• 6.2.2 Certificación de enlaces, etiquetado y planos as-built
• 6.2.3 Gabinetes de piso y switches de acceso instalados en las bodegas de Talca y Concepción
• 6.3 Montaje de racks y gabinetes
• 6.3.1 Rack R01 de servidores montado: clúster de tres nodos, respaldo local, consola KVM y
traslado del servidor del ERP del CLIENTE a U25–U26, con respaldo completo verificado,
en ventana dominical después del H3 y antes de la marcha blanca de Talca, sin cambios de
software
• 6.3.2 Rack R02 de comunicaciones montado: firewalls, switches de núcleo y de gestión, y
distribución de fibra
• 6.3.3 Gabinete de borde de Concepción montado: servidores activo y en espera, firewalls,
switches, UPS, climatización y monitoreo, con toma del servicio por el de espera si falla el
activo
• 6.3.4 Gabinetes de borde montados en Curicó, Chillán y Los Ángeles, con dos mini-PC
(activo y en espera) por plataforma
• 6.4 Sistemas de seguridad física
• 6.4.1 Hardware de control de acceso biométrico y esclusa instalado
• 6.4.2 Hardware de videovigilancia instalado
• 6.4.3 Recinto de custodia de respaldos habilitado
• 6.5 Equipamiento de campo
• 6.5.1 Terminales de preventa, reparto y bodega configurados y enrolados
• 6.5.2 Terminales de pago configurados, uno por camión
• 6.5.3 Sensores de cámara y gateways IoT instalados en Talca y Concepción
• 6.5.4 Kit de cadena de frío instalado y recibido en los 28 camiones con frío
• 6.5.5 Impresoras de cabina instaladas
• 6.5.6 Impresoras de andén y balanzas de recepción instaladas
• 6.6 Configuración de la infraestructura de los sitios
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
15


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
• 6.6.1 Software de base instalado en los sitios: virtualización, contenedores, PostgreSQL,
RabbitMQ y Keycloak
• 6.6.2 Enlaces de fibra, LTE y Starlink habilitados, con conmutación al respaldo
• 6.6.3 Borde de los CD en servicio, con la prueba de autonomía de 24 horas aprobada
• 7. Capacitación y gestión del cambio
• 7.1 Capacitación por roles
• 7.1.1 Plan de capacitación por perfil: usuarios finales, avanzados, administradores, equipo
técnico y soporte
• 7.1.2 Programa de capacitación continua del turno de noche por la rotación del 38 %
• 7.1.3 Incorporación de conductores de transportistas, escaneos y lectura del rojo
• 7.1.4 Traspaso al equipo de TI de cuatro personas del CLIENTE
• 7.1.5 Materiales de capacitación: manuales por perfil, guías rápidas, preguntas frecuentes
y videos tutoriales
• 7.1.6 Plataforma de autoformación en línea con registro de avance
• 7.2 Gestión del cambio
• 7.2.1 Acompañamiento del personal con 20 o 30 años en la compañía
• 7.2.2 Gestión del cambio con las cadenas y los transportistas
• 7.2.3 Diagnóstico del impacto organizacional por área y perfil, con agentes de cambio
• 7.2.4 Procedimientos operativos rediseñados, contingencia de frío y ruptura confirmada
• 7.2.5 Medición de la adopción y plan de acción correctiva
• 7.3 Evaluaciones y certificaciones
• 7.3.1 Certificación de preventistas, conductores y preparadores (Etapa 1)
• 7.3.2 Certificación de Comercial y Finanzas en costo de servir (Etapa 2)
• 8. Operación y soporte (36 meses)
• 8.1 Servicios de operación
• 8.1.1 Servicio de centro de operaciones 24×7 y mesa de servicio durante los 36 meses de
operación (04:00 a 22:00; 24×7 en septiembre y diciembre)
• 8.1.2 Servicio de gestión de incidentes, problemas y niveles de servicio del artículo 78 de
las Bases Administrativas (p. 40) durante los 36 meses de operación
• 8.1.3 Servicio de continuidad y pruebas semestrales de recuperación ante desastres durante
los 36 meses de operación
• 8.1.4 Actualizaciones anuales del Plan de Reversibilidad durante los 36 meses de operación
• 8.1.5 Servicio de centro de operaciones de seguridad 24×7 con SIEM desde la primera
marcha blanca (mes 13) hasta el mes 56
• 8.1.6 Pruebas mensuales de restauración de respaldos durante los 36 meses de operación
• 8.2 Mantenimiento
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
16


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
• 8.2.1 Mantenimiento correctivo y evolutivo del software durante los 36 meses de operación,
con bolsa anual de horas y fuera de las ventanas de congelamiento
• 8.2.2 Mantenimiento de ciberseguridad durante los 36 meses de operación: vulnerabilida-
des, intrusión anual e inyección de fallas
• 8.2.3 Mantenimiento del hardware durante los 36 meses de operación: sala técnica, racks,
gabinetes de borde y equipamiento de terreno
• 8.2.4 Registro y reducción de la deuda técnica durante los 36 meses de operación
• 8.2.5 Actualizaciones anuales de los componentes de base durante los 36 meses de operación
• 8.2.6 Revisiones semestrales de las instalaciones eléctricas de la sala durante los 36 meses
de operación
• 8.2.7 Ciclo de vida del equipamiento durante los 36 meses de operación: reposición y
disposición final
• 8.3 Innovaciones en operación
• 8.3.1 Innovación 2: mantenimiento de escenarios de regresión (INN-02.P4, segunda parte)
• 8.3.2 Innovación 3: revisión semestral de parámetros durante los 36 meses de operación
(INN-03.P5)
• 8.3.3 Innovación 4: línea base y liquidaciones en sombra (INN-04.P2)
• 8.3.4 Innovación 4: liquidación mensual del tramo variable, meses 24 a 56 (INN-04.P3)
• 8.3.5 Innovación 5: despliegue gradual por rutas (INN-05.P4, segunda parte)
• 8.3.6 Innovación 5: bloque 4 condicionado (INN-05.P5)
• 8.4 Informes y obligaciones periódicas
• 8.4.1 Gestión de la capacidad con proyección trimestral durante los 36 meses de operación
• 8.4.2 Informes mensuales de consumo de nube (FinOps) durante los 36 meses de operación
• 8.4.3 Estimaciones anuales de la huella de carbono de la operación
• 8.4.4 Actualizaciones semestrales del depósito de custodia de fuentes durante los 36 meses
de operación
• 8.5 Capacitación y transferencia en operación
• 8.5.1 Dos jornadas anuales de actualización y capacitación del personal nuevo durante los
36 meses de operación
• 8.5.2 Mentoría al equipo técnico del CLIENTE durante los seis meses posteriores al mes 21
• 8.5.3 Mantenimiento de la base de conocimiento durante los 36 meses de operación, con
métricas de uso
• 9. Cierre
• 9.1 Cierre de la implementación
• 9.1.1 Entrega del código fuente, la infraestructura como código y los procedimientos de
despliegue
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
17


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
• 9.1.2 Informe de lecciones aprendidas y archivo de la implementación
• 9.2 Salida al término del contrato
• 9.2.1 Ejecución del Plan de Reversibilidad y acompañamiento de 90 días
• 9.2.2 Certificado de devolución o eliminación de datos personales
La figura siguiente presenta la EDT completa en una sola vista panorámica. Por su densidad,
se recomienda ampliarla en el PDF; el Subdocumento 7 contiene las láminas separadas por
fase para consultar las cuentas de control y los paquetes con mayor legibilidad.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
18


---

LafroX
SpA
Formulario
T-14:
Plan
de
trabajo,
EDT
y
carta
Gantt
1. Inicio
9 CC · 35 PT
1.1 Definición inicial del
proyecto
1.1.1 Acta de constitución del
proyecto, firmada con la
Contraparte Técnica
1.1.2 Documento de
validación con el CLIENTE
de los problemas y metas del
proyecto
1.1.3 Acta de confirmación
con el CLIENTE de la fecha
de inicio, la evidencia para el
proveedor de lácteos, las
ventanas de paso a
producción y el acuse
tributario
1.2 Alcance del proyecto
1.2.1 Documento de
especificación de
requerimientos y línea base
de alcance de la Etapa 1
(H1)
1.2.2 Documento de reglas
de ruteo capturadas al
planificador de rutas
1.2.3 Documento de
especificación de las
interfaces sin documentación
del ERP, del WMS de 2013 y
de la telemetría del tercero
1.2.4 Matriz de trazabilidad:
requerimiento, módulo,
paquete y prueba (H1)
1.2.5 Documento de línea
base de alcance de la Etapa
2: canal moderno y costo de
servir (H8)
1.3 Planificación del
proyecto
1.3.1 Plan para la dirección
del proyecto, con el
calendario de
congelamientos de
septiembre, diciembre y el
cierre mensual
1.3.2 EDT y diccionario de la
EDT (línea base del alcance)
1.3.3 Carta Gantt de 56
meses con los hitos H1 a
H12 y la ruta crítica
1.3.4 Documento de
nivelación de recursos y
frentes del solapamiento de
los meses 13 a 15 y 19 a 20
1.3.5 Reunión semanal de
seguimiento con su informe
semanal
1.4 Gestión de interesados y
comunicaciones
1.4.1 Registro de interesados
con su influencia, interés y
estrategia
1.4.2 Plan de
comunicaciones con
calendario y canales por
grupo de interés
1.4.3 Registro de solicitudes
de cambio con análisis de
impacto
1.5 Gestión de calidad
1.5.1 Plan de calidad y plan
de pruebas
1.5.2 Puertas de
calidad: lógica 70 %,
global 80 % y código
modificado 80 %
1.6 Gestión de riesgos
1.6.1 Plan de riesgos y
registro inicial de riesgos
según ISO 31000
1.6.2 Registro de riesgos
revisado en cada Comité de
Proyecto
1.7 Plan de Reversibilidad
1.7.1 Plan de Reversibilidad
inicial (primeros 90 días)
1.7.2 Primera actualización
anual del Plan de
Reversibilidad durante la
implementación
1.8 Gobierno y control del
proyecto
1.8.1 Oficina de gestión del
proyecto con metodología
basada en el PMBOK
1.8.2 Actas del Comité
Ejecutivo mensual, con la
aprobación de los cambios
de alcance
1.8.3 Actas del Comité de
Proyecto quincenal
1.8.4 Actas del Comité de
Arquitectura mensual
1.8.5 Actas del Comité de
Operación mensual, desde el
mes 13
1.8.6 Informe mensual de
avance con valor ganado
1.8.7 Tablero de estado del
proyecto disponible para el
CLIENTE
1.8.8 Espacio colaborativo
con la documentación, los
entregables, las actas, los
riesgos y los cambios
1.9 Cumplimiento normativo
y contractual
1.9.1 Matriz de cumplimiento
normativo por obligación
legal, con su control y su
evidencia
1.9.2 Acuerdo de tratamiento
de datos personales con el
CLIENTE
1.9.3 Registro de actividades
de tratamiento y evaluación
de impacto en protección de
datos
1.9.4 Certificación ISO/IEC
27001 vigente y entrega
anual de los informes de
certificación
1.9.5 Garantía de fiel
cumplimiento, seguros y
certificados laborales
vigentes durante el contrato
2. Elaboración
6 CC · 20 PT
2.1 Arquitectura de la
solución
2.1.1 Documento de
arquitectura lógica: capas,
módulos M1 a M12 e
interfaces
2.1.2 Documento de
arquitectura física híbrida:
nube, centros de distribución
y plataformas de cross-
docking
2.1.3 Modelo de datos y
diccionario de datos, con la
trazabilidad por lote
2.1.4 Documento de diseño
detallado de M11 y del
intercambio con las cadenas
2.2 Diseño de la seguridad
2.2.1 Plan de seguridad de la
información
2.2.2 Modelado de
amenazas por componente y
por integración externa,
actualizado ante cada
cambio
2.2.3 Plan de respuesta a
incidentes de seguridad, con
aviso al CLIENTE en dos
horas
2.2.4 Matriz de clasificación
de la información y matriz de
controles
2.3 Diseño de la sala técnica
y de los racks
2.3.1 Plano de la sala técnica
de Talca, con su cálculo
eléctrico y térmico
2.3.2 Plano de distribución
de los racks R01 de
servidores y R02 de
comunicaciones
2.3.3 Plano de los gabinetes
de borde de Concepción y de
las plataformas de cross-
docking
2.4 Validación de diseños
2.4.1 Acta de aprobación de
la arquitectura, el plan de
seguridad y el modelo de
datos (H2)
2.4.2 Acta de aprobación del
diseño detallado de la Etapa
2 (H8)
2.5 Continuidad del negocio
2.5.1 Plan de continuidad del
negocio según ISO 22301,
con análisis de impacto y
procedimientos manuales
2.5.2 Plan de continuidad
TIC según ISO/IEC 27031 y
plan de recuperación ante
desastres
2.6 Experiencia de usuario
2.6.1 Investigación con
preparadores, preventistas,
conductores y almaceneros
2.6.2 Prototipos y pruebas de
usabilidad con participantes
del CLIENTE
2.6.3 Indicadores de
usabilidad comprometidos
por transacción crítica
3. Construcción
11 CC · 79 PT
3.1 Ambientes y cadena de
desarrollo
3.1.1 Ambientes de
Desarrollo y QA en la nube
(H3)
3.1.2 Ambientes de
Preproducción y Producción
en la nube (H3)
3.1.3 Ambiente de
recuperación ante desastres
en la región secundaria (H3)
3.1.4 Cadena de integración
y entrega continua, e
infraestructura como código
3.1.5 Observabilidad de los
doce módulos y de los sitios,
con tableros para el
CLIENTE (H3)
3.2 Servicios de nube de la
plataforma
3.2.1 Servicio de nube para
la aplicación y los portales
3.2.2 Servicio de nube de
base de datos, caché y
mensajería
3.2.3 Servicio de nube de
ingesta de IoT, telemetría
cruda y plataforma analítica
3.2.4 Servicio de nube de
respaldo inmutable y réplica
entre regiones
3.2.5 Servicio de nube de
seguridad y gobierno, y
detección en endpoints
3.2.6 Servicio de gestión de
dispositivos móviles
3.3 Base compartida
3.3.1 Identidad y control de
acceso, incluidos los
conductores externos que
rotan sin aviso
3.3.2 Integración con el ERP
como único emisor de la guía
de despacho (INT-06 e INT-
07)
3.3.3 Convivencia con el
WMS de 2013 durante el
reemplazo
3.3.4 Integración con la
telemetría de los 42
camiones propios (INT-15)
3.3.5 Registro auditable de
stock, lotes y cobros
3.3.6 Operación sin
conexión: 14 horas en
terreno y 24 horas en el CD
3.4 Módulos de la Etapa 1
3.4.1 Recepción de
mercadería con captura de
lote y vencimiento (M1
Recepción)
3.4.2 Inventario por
ubicación y lote, con FEFO y
conteo cíclico (M2 Inventario)
3.4.3 Preparación de pedidos
en el turno de noche y en la
cámara de congelado (M5
Preparación)
3.4.4 Cadena de frío,
retención por SSCC y retiro
sanitario (M9 Calidad y
trazabilidad)
3.4.5 Ingesta de
temperatura (M9) y
posición de flota (M12)
3.4.6 Aplicación móvil de
preventa sin conexión, con
stock y crédito (M3 Preventa)
3.4.7 Planificación de rutas
corregible por el planificador
(M4 Rutas)
3.4.8 Aplicación móvil de
reparto con prueba de
entrega digital (M6 Reparto)
3.4.9 Devoluciones en
terreno y control de envases
(M8 Devoluciones y
envases)
3.4.10 Cobro en ruta,
rendición y conciliación (M7
Cobranza y rendición)
3.4.11 Indicadores
operacionales y OTIF diario
(M10 Analítica)
3.5 Módulos de la Etapa 2
3.5.1 Pedido electrónico y
aviso de despacho para las
cadenas, y portal de
proveedores (M11 Canal
moderno)
3.5.2 Portal web de clientes:
cuenta, saldo, entregas y
documentos
3.5.3 Portal web de
transportistas: rutas
asignadas del día siguiente
3.5.4 Costo de servir por
cliente y por entrega (M10
Analítica)
3.6 Integraciones externas
3.6.1 Intercambio de lote y
trazabilidad con los
proveedores
3.6.2 Integración con la
pasarela de pago para el
cobro con tarjeta (INT-09)
3.6.3 Integración con el
servicio de mapas y
geocodificación (INT-10)
3.6.4 Integración con el
servicio de avisos al cliente
(INT-11)
3.6.5 Intercambio electrónico
con la principal cadena, con
sus pruebas aprobadas (INT-
08)
3.6.6 Incorporación de las
demás cadenas al
intercambio electrónico (INT-
08)
3.7 Migración de datos
3.7.1 Informe de
perfilamiento y datos
saneados
3.7.2 Datos maestros
cargados: 8.400 SKU,
clientes e instalaciones
3.7.3 Saldos migrados desde
el WMS de Talca
3.7.4 Saldos cargados en
Concepción desde el conteo
físico
3.7.5 Acta de conciliación y
corte fuera de las ventanas
de congelamiento
3.8 Pruebas de la Etapa 1
3.8.1 Pruebas de integración,
regresión e idempotencia en
QA (H4)
3.8.2 Pruebas de aceptación
y de accesibilidad con
preventistas, conductores y
bodega
3.8.3 Cinco condiciones
físicas: −22 °C con
guantes, lluvia, calor
superior a 34 °C, sol directo
y uso con una mano;
desconexión separada de
14 horas
3.8.4 Pruebas de carga con
el peak de septiembre y de
resiliencia
3.8.5 Prueba de
recuperación ante desastres
con conmutación real
3.8.6 Prueba de seguridad
ofensiva de la Etapa 1, por
un tercero independiente
3.8.7 Acta de certificación de
la Etapa 1 (H5)
3.8.8 Demostración en
Preproducción del
despliegue sin interrupción
de la Etapa 1
3.9 Pruebas de la Etapa 2
3.9.1 Pruebas de integración
y regresión sin afectar la
Etapa 1 en producción (H9)
3.9.2 Pruebas de aceptación
y de accesibilidad con
cadenas, transportistas,
Comercial y Finanzas
3.9.3 Pruebas de carga con
ambas etapas activas y de
resiliencia
3.9.4 Prueba de
recuperación ante desastres
con ambas etapas
3.9.5 Prueba de seguridad
ofensiva de la Etapa 2, por
un tercero independiente
3.9.6 Acta de certificación de
la Etapa 2 y cierre del
desarrollo (H10)
3.9.7 Demostración en
Preproducción del
despliegue sin interrupción
de la Etapa 2
3.10 Innovaciones
3.10.1 Innovación 1:
seguimiento de
vencimiento posentrega en
el local
3.10.1.1 Innovación 1:
documento de catálogo
de acciones y protocolo
del piloto (INN-01.P1)
3.10.1.2 Innovación 1:
estimador de saldo y
ritmo de reposición
(INN-01.P2)
3.10.1.3 Innovación 1:
función de lista sin
conexión en la
aplicación de preventa
(INN-01.P3)
3.10.1.4 Innovación 1:
informe del piloto en
marcha blanca y
habilitación (INN-01.P4)
3.10.2 Innovación 2:
reproducción de incidentes
de terreno
3.10.2.1 Innovación 2:
informe de medición
inicial y contrato de
evidencia (INN-02.P1)
3.10.2.2 Innovación 2:
circuito mínimo de
reproducción en la
preventa (INN-02.P2)
3.10.2.3 Innovación 2:
captura de evidencia en
las aplicaciones de
preventa, preparación y
reparto (INN-02.P3)
3.10.2.4 Innovación 2:
informe de validación
comparada durante la
implementación (INN-
02.P4, primera parte)
3.10.3 Innovación 3: vida
útil remanente por historia
térmica del lote
3.10.3.1 Innovación 3:
documento de familias
priorizadas y parámetros
aprobados (INN-03.P1)
3.10.3.2 Innovación 3:
asociación lote–sensor
en el borde y en el
camión (INN-03.P2)
3.10.3.3 Innovación 3:
vista en M9 y orden de
salida sugerido (INN-
03.P3)
3.10.3.4 Innovación 3:
informe de validación en
marcha blanca con
Calidad (INN-03.P4)
3.10.4 Innovación 5: hoja
de negocio del almacenero
3.10.4.1 Innovación 5:
prototipo e informe de la
prueba de comprensión
(INN-05.P1)
3.10.4.2 Innovación 5:
evaluación de privacidad
y diseño de la impresión
en cabina (INN-05.P2)
3.10.4.3 Innovación 5:
cálculo y bloques 1 a 3
de la hoja de negocio
(INN-05.P3)
3.10.4.4 Innovación 5:
hoja certificada, en
marcha blanca y en
producción (INN-05.P4,
primera parte)
3.11 Documentación técnica
3.11.1 Documentación
técnica, funcional, de
arquitectura, de operación y
de seguridad
3.11.2 Base de conocimiento
de incidentes y decisiones de
diseño
3.11.3 Estándares de
codificación y documentación
de interfaces en OpenAPI y
AsyncAPI
3.11.4 Inventario de
componentes (SBOM) con
sus licencias de código
abierto
3.11.5 Depósito del código
fuente en el repositorio del
CLIENTE en cada liberación
4. Transición
3 CC · 11 PT
4.1 Plan de implantación
4.1.1 Plan de olas de la
Etapa 1 por sitio y zona:
Talca, Concepción y
plataformas de cross-docking
4.1.2 Procedimiento de
reversión de la Etapa 1
antes de las 05:30, con
versión operativa local y
DTE emitidos por el ERP
4.1.3 Plan de implantación y
reversión de la Etapa 2 fuera
de la ventana de 05:30 a
07:00
4.2 Marcha blanca y
producción de la Etapa 1
4.2.1 Marcha blanca de la
Etapa 1 con conciliación
diaria (H6)
4.2.2 Estabilización de la
Etapa 1, acompañamiento
en ruta y restauraciones de
soporte puente
4.2.3 Acta de
aceptación de la
Etapa 1 (H7)
4.3 Marcha blanca y
producción de la Etapa 2
4.3.1 Marcha blanca de la
Etapa 2 en convivencia con
la Etapa 1 y fuente única de
datos (H11)
4.3.2 Estabilización de la
Etapa 2 con Comercial,
Finanzas, cadenas y
transportistas
4.3.3 Acta de
aceptación final de la
implementación (H12)
4.3.4 Garantía de correcto
funcionamiento constituida,
condición de la aceptación
final (H12)
5. Adquisiciones y contrataciones
4 CC · 15 PT
5.1 Hardware e
infraestructura
5.1.1 Especificación de
compra de equipos de uso
para el CLIENTE
5.1.2 Especificación y
compra de la sala técnica,
los racks, los servidores y
los gabinetes de borde
5.1.3 Actas de recepción
técnica del equipamiento
de terreno comprado por el
CLIENTE y de la
infraestructura provista por
LafroX
5.2 Servicios de nube y
licencias
5.2.1 Contrato de los
servicios de AWS
5.2.2 Suscripción del servicio
de gestión de dispositivos y
de detección en endpoints
5.2.3 Licencias de software
de terceros constituidas a
nombre del CLIENTE
5.3 Enlaces de
comunicaciones
5.3.1 Contrato de fibra óptica
de los CD de Talca y
Concepción
5.3.2 Contrato de planes
LTE con dos proveedores
(ocho planes)
5.3.3 Contrato de Starlink
para los cinco sitios: Talca,
Concepción y las tres
plataformas de cross-
docking
5.4 Acuerdos con terceros
5.4.1 Acuerdos
operacionales firmados con
los diez transportistas
5.4.2 Acta de acuerdo con el
sindicato sobre terminales,
GPS y cámaras
5.4.3 Fórmula aprobada del
tramo variable: reglas de
atribución, canasta e índices
(INN-04.P1)
5.4.4 Contrato de custodia
de fuentes con un tercero
independiente
6. Infraestructura física y sitios
6 CC · 24 PT
6.1 Adecuación de la sala
técnica de Talca
6.1.1 Coordinación de la
obra civil de separación, a
cargo del CLIENTE (RT-
06.06), y piso técnico de la
sala
6.1.2 Hardware de energía
instalado: UPS modular N+1,
generador con 24 horas de
autonomía, transferencia
automática y PDU A/B
6.1.3 Hardware de
climatización de precisión
N+1 instalado
6.1.4 Hardware de detección
temprana de incendio y
extinción por agente limpio
instalado
6.1.5 Acta de recepción
técnica de la sala
6.2 Cableado estructurado
6.2.1 Cableado de cobre
Cat6A y fibra OM4 tendido,
con dos ductos de ingreso
independientes
6.2.2 Certificación de
enlaces, etiquetado y planos
as-built
6.2.3 Gabinetes de piso y
switches de acceso
instalados en las bodegas de
Talca y Concepción
6.3 Montaje de racks y
gabinetes
6.3.1 Rack R01 de
servidores montado: clúster
de tres nodos, respaldo
local, consola KVM y
traslado del servidor del
ERP del CLIENTE
6.3.2 Rack R02 de
comunicaciones montado:
firewalls, switches de núcleo
y de gestión, y distribución
de fibra
6.3.3 Gabinete de borde de
Concepción montado:
servidores activo y en
espera, firewalls, switches,
UPS, climatización y
monitoreo
6.3.4 Gabinetes de borde
montados en Curicó,
Chillán y Los Ángeles, con
dos mini-PC (activo y en
espera) por plataforma
6.4 Sistemas de seguridad
física
6.4.1 Hardware de control de
acceso biométrico y esclusa
instalado
6.4.2 Hardware de
videovigilancia instalado
6.4.3 Recinto de custodia de
respaldos habilitado
6.5 Equipamiento de campo
6.5.1 Terminales de
preventa, reparto y bodega
configurados y enrolados
6.5.2 Terminales de pago
configurados, uno por
camión
6.5.3 Sensores de cámara y
gateways IoT instalados en
Talca y Concepción
6.5.4 Kit de cadena de frío
instalado y recibido en los
28 camiones con frío
6.5.5 Impresoras de cabina
instaladas
6.5.6 Impresoras de andén y
balanzas de recepción
instaladas
6.6 Configuración de la
infraestructura de los sitios
6.6.1 Software de base
instalado en los sitios:
virtualización, contenedores,
PostgreSQL, RabbitMQ y
Keycloak
6.6.2 Enlaces de fibra, LTE y
Starlink habilitados, con
conmutación al respaldo
6.6.3 Borde de los CD en
servicio, con la prueba de
autonomía de 24 horas
aprobada
7. Capacitación y gestión del cambio
3 CC · 13 PT
7.1 Capacitación por roles
7.1.1 Plan de capacitación
por perfil: usuarios finales,
avanzados, administradores,
equipo técnico y soporte
7.1.2 Programa de
capacitación continua del
turno de noche por la
rotación del 38 %
7.1.3 Incorporación de
conductores de
transportistas, escaneos y
lectura del rojo
7.1.4 Traspaso al equipo de
TI de cuatro personas del
CLIENTE
7.1.5 Materiales de
capacitación: manuales por
perfil, guías rápidas,
preguntas frecuentes y
videos tutoriales
7.1.6 Plataforma de
autoformación en línea con
registro de avance
7.2 Gestión del cambio
7.2.1 Acompañamiento del
personal con 20 o 30 años
en la compañía
7.2.2 Gestión del cambio con
las cadenas y los
transportistas
7.2.3 Diagnóstico del
impacto organizacional por
área y perfil, con agentes de
cambio
7.2.4 Procedimientos
operativos rediseñados,
contingencia de frío y
ruptura confirmada
7.2.5 Medición de la
adopción y plan de acción
correctiva
7.3 Evaluaciones y
certificaciones
7.3.1 Certificación de
preventistas, conductores y
preparadores (Etapa 1)
7.3.2 Certificación de
Comercial y Finanzas en
costo de servir (Etapa 2)
8. Operación y soporte (36 meses)
5 CC · 26 PT
8.1 Servicios de operación
8.1.1 Servicio de centro de
operaciones 24×7 y mesa de
servicio durante los 36
meses de operación (04:00 a
22:00; 24×7 en septiembre y
diciembre)
8.1.2 Servicio de gestión de
incidentes, problemas y
niveles de servicio del Art.
78° durante los 36 meses de
operación
8.1.3 Servicio de continuidad
y pruebas semestrales de
recuperación ante desastres
durante los 36 meses de
operación
8.1.4 Actualizaciones
anuales del Plan de
Reversibilidad durante los 36
meses de operación
8.1.5 Servicio de centro de
operaciones de seguridad
24×7 con SIEM desde la
primera marcha blanca
(mes 13) hasta el mes 56
8.1.6 Pruebas mensuales de
restauración de respaldos
durante los 36 meses de
operación
8.2 Mantenimiento
8.2.1 Mantenimiento
correctivo y evolutivo del
software durante los 36
meses de operación, con
bolsa anual de horas y fuera
de las ventanas de
congelamiento
8.2.2 Mantenimiento de
ciberseguridad durante los
36 meses de operación:
vulnerabilidades, intrusión
anual e inyección de fallas
8.2.3 Mantenimiento del
hardware durante los 36
meses de operación: sala
técnica, racks, gabinetes de
borde y equipamiento de
terreno
8.2.4 Registro y reducción de
la deuda técnica durante los
36 meses de operación
8.2.5 Actualizaciones
anuales de los componentes
de base durante los 36
meses de operación
8.2.6 Revisiones semestrales
de las instalaciones
eléctricas de la sala durante
los 36 meses de operación
8.2.7 Ciclo de vida del
equipamiento durante los 36
meses de operación:
reposición y disposición final
8.3 Innovaciones en
operación
8.3.1 Innovación 2:
mantenimiento de escenarios
de regresión (INN-02.P4,
segunda parte)
8.3.2 Innovación 3: revisión
semestral de parámetros
durante los 36 meses de
operación (INN-03.P5)
8.3.3 Innovación 4: línea
base y liquidaciones en
sombra (INN-04.P2)
8.3.4 Innovación 4:
liquidación mensual del
tramo variable, meses 24 a
56 (INN-04.P3)
8.3.5 Innovación 5:
despliegue gradual por rutas
(INN-05.P4, segunda parte)
8.3.6 Innovación 5: bloque 4
condicionado (INN-05.P5)
8.4 Informes y obligaciones
periódicas
8.4.1 Gestión de la
capacidad con proyección
trimestral durante los 36
meses de operación
8.4.2 Informes mensuales de
consumo de nube (FinOps)
durante los 36 meses de
operación
8.4.3 Estimaciones anuales
de la huella de carbono de la
operación
8.4.4 Actualizaciones
semestrales del depósito de
custodia de fuentes durante
los 36 meses de operación
8.5 Capacitación y
transferencia en operación
8.5.1 Dos jornadas anuales
de actualización y
capacitación del personal
nuevo durante los 36 meses
de operación
8.5.2 Mentoría al equipo
técnico del CLIENTE durante
los seis meses posteriores al
mes 21
8.5.3 Mantenimiento de la
base de conocimiento
durante los 36 meses de
operación, con métricas de
uso
9. Cierre
2 CC · 4 PT
9.1 Cierre de la
implementación
9.1.1 Entrega del código
fuente, la infraestructura
como código y los
procedimientos de
despliegue
9.1.2 Informe de lecciones
aprendidas y archivo de la
implementación
9.2 Salida al término del
contrato
9.2.1 Ejecución del Plan de
Reversibilidad y
acompañamiento de 90 días
9.2.2 Certificado de
devolución o eliminación de
datos personales
Plataforma logística de Distribuidora Puelche
49 cuentas de control · 227 paquetes de trabajo
2.4.3 Validación del diseño
del kit en banco de pruebas
2.4.4 Mapeo térmico por
tipo de carrocería
4.1.4 Piloto de cadena de
frío en cuatro camiones
5.1.4 Especificación y
compra del sistema de
cadena de frío
5.3.4 Contrato de SIM M2M
y servicio satelital de los
camiones con frío
Figura 1 Vista panorámica de la EDT completa del proyecto. Para consultar el detalle por fase, véanse las láminas de la sección «Estructura general» del
Subdocumento 7. Fuente: estructura de descomposición del trabajo presentada en la sección 1 de este formulario.
LafroX
SpA
Formulario
T-14
Media
firma:
Alex
Aravena
19


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
La vista reúne las nueve fases, sus 49 cuentas de control y los 227 paquetes de trabajo en
una sola estructura. Las secciones siguientes desarrollan el diccionario y la programación
asociados a esa descomposición.
2 Diccionario de la EDT
El diccionario describe cada paquete con su entregable, su criterio de aceptación, su
responsable y el período del cronograma en que se ejecuta, con el hito del Formulario E-25
que habilita cuando corresponde. Todo entregable se recibe con un acta de la Contraparte
Técnica (BA, art. 18.1, p. 13), que acompaña la evidencia de verificación, la trazabilidad hacia
los requerimientos del Formulario T-12 y las observaciones resueltas (BA, art. 18.2, p. 13). Los
criterios de cada paquete se suman a esa regla común.
Los responsables son los roles de la estructura para el proyecto del Capítulo 1, sección 1.5.
La Tabla 2 presenta las siglas usadas en el diccionario.
Tabla 2 Responsables de los paquetes. Fuente: (Subdocumento 1, sección 1.5).
Sigla Rol Persona
JP Jefe de Proyecto Alex Aravena
ARQ Arquitecto de Solución Bastián Trejo
SEG Encargado de Seguridad de la
Información
Álvaro Catalán
DAT Líder de Datos Leandro Chamorro
DES Líder de Desarrollo Tomás Pérez
CAL Líder de Calidad Maximiliano Miño
SRE Líder de Operación / SRE Guillermo Castillo
IMP Líder de Implantación y Gestión
del Cambio
Patricio Henríquez
Los paquetes de la fase 8 son paquetes de esfuerzo continuo. Cada uno cubre un servicio
durante los 36 meses de operación y se controla con entregables mensuales o anuales, como el
informe de servicio, el informe de pruebas o la actualización de un plan; esos entregables son
sus puntos de verificación.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
20


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
2.1 Fase 1. Inicio
La fase 1 reúne 9 cuentas de control y 35 paquetes de trabajo.
2.1.1 Cuenta 1.1 — Definición inicial del proyecto
Esta cuenta de control reúne los tres documentos con que el proyecto arranca formalmente.
La Tabla 3 presenta sus paquetes.
Tabla 3 Diccionario de la cuenta 1.1. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.1.1 Acta de constitu-
ción del proyecto,
firmada con la Con-
traparte Técnica
Acta firmada por
LafroX y Puelche.
Está firmada en el
mes 1 e identifica
al patrocinador,
a la Contraparte
Técnica, al Jefe
de Proyecto y los
objetivos.
JP Mes 1.
1.1.2 Documento de
validación con el
CLIENTE de los
problemas y metas
del proyecto
Documento de
validación con los
cambios acordados,
si los hay.
Las gerencias del
CLIENTE confir-
man por escrito
los problemas y las
metas.
JP Mes 1.
1.1.3 Acta de confirma-
ción con el CLIEN-
TE de la fecha de
inicio, la evidencia
para el proveedor
de lácteos, las ven-
tanas de paso a
producción y el
acuse tributario
Acta con la respues-
ta del CLIENTE a
cada tema.
Los cuatro temas
tienen una respues-
ta escrita incorpora-
da al plan.
JP Mes 1, antes
del H1.
2.1.2 Cuenta 1.2 — Alcance del proyecto
Esta cuenta de control fija qué se construye y deja todo listo para diseñar. Incluye la captura
del conocimiento del planificador y el levantamiento de las interfaces, porque ambos son
insumos del alcance.
La Tabla 4 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
21


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 4 Diccionario de la cuenta 1.2. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.2.1 Documento de
especificación de
requerimientos
y línea base de
alcance de la Etapa
1 (H1)
Especificación de
requerimientos
aprobada (línea
base de alcance).
El 100 % de los
requerimientos
de la Etapa 1 tiene
módulo y criterio
de aceptación, y
la línea base está
firmada en el mes 2.
ARQ Mes 1 (H1).
1.2.2 Documento de
reglas de ruteo
capturadas al plani-
ficador de rutas
Catálogo de reglas
de ruteo validado
por don Hugo.
Don Hugo firma
que las reglas repre-
sentan su criterio.
Las rutas que el
software genera con
esas reglas resultan
operables cuando
se comparan con
las suyas.
IMP Meses 1 a 3.
1.2.3 Documento de es-
pecificación de las
interfaces sin docu-
mentación del ERP,
del WMS de 2013 y
de la telemetría del
tercero
Especificación
de cada interfaz
(formato, volumen
y horario) y prueba
de conexión.
Cada interfaz tie-
ne contrato y una
prueba de cone-
xión exitosa en el
ambiente de De-
sarrollo antes del
H2.
ARQ Meses 1 a 4.
1.2.4 Matriz de trazabili-
dad: requerimiento,
módulo, paquete y
prueba (H1)
Matriz de trazabili-
dad.
Ningún requeri-
miento ofertado
queda sin paquete
ni sin prueba.
CAL Mes 2 (H1). Se
actualiza con
cada cambio
aprobado.
1.2.5 Documento de línea
base de alcance de
la Etapa 2: canal
moderno y costo de
servir (H8)
Línea base de al-
cance de la Etapa
2.
Está aprobada por
la Contraparte Téc-
nica en el mes 14.
ARQ Mes 13 (H8).
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
22


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
2.1.3 Cuenta 1.3 — Planificación del proyecto
Esta cuenta de control reúne los documentos que dicen cómo y cuándo se hará el trabajo, y
los informes que muestran si se cumple.
La Tabla 5 presenta sus paquetes.
Tabla 5 Diccionario de la cuenta 1.3. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.3.1 Plan para la direc-
ción del proyecto,
con el calendario
de congelamientos
de septiembre, di-
ciembre y el cierre
mensual
Plan para la direc-
ción con el calenda-
rio de congelamien-
tos.
Ningún paso a pro-
ducción, corte de
datos ni desplie-
gue cae en una
fecha prohibida;
los meses 16 y 21
coinciden con el
Art. 17°; el plan está
aprobado.
JP Mes 1 (H1). Se
actualiza con
cada cambio.
1.3.2 EDT y diccionario
de la EDT (línea
base del alcance)
EDT dibujada y dic-
cionario aprobados.
Todo requerimiento
de la matriz (1.2.4)
cae en un paquete,
y ningún paquete
queda sin responsa-
ble.
JP Mes 2 (H1).
1.3.3 Carta Gantt de 56
meses con los hitos
H1 a H12 y la ruta
crítica
Carta Gantt aproba-
da.
Cubre los 56 meses,
respeta el Art. 17° y
nombra la ruta críti-
ca con su cálculo.
JP Mes 2.
1.3.4 Documento de nive-
lación de recursos
y frentes del sola-
pamiento de los
meses 13 a 15 y 19 a
20
Nivelación de recur-
sos por etapa y por
frente.
Ningún mes asigna
a una persona por
sobre su capacidad,
y los dos frentes
del solapamiento
tienen dotación
propia.
JP Mes 2. Se revisa
antes del mes
13.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
23


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 5 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.3.5 Reunión semanal
de seguimiento con
su informe semanal
Una reunión y un
informe por sema-
na.
La reunión se hace
cada semana, y su
informe se publica
con el avance por
paquete y las des-
viaciones frente al
cronograma.
JP Semanal, du-
rante toda la
implementa-
ción.
2.1.4 Cuenta 1.4 — Gestión de interesados y comunicaciones
Esta cuenta de control reúne el trabajo con las personas que pueden apoyar o frenar el
proyecto, y el lugar donde se toman las decisiones.
La Tabla 6 presenta sus paquetes.
Tabla 6 Diccionario de la cuenta 1.4. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.4.1 Registro de intere-
sados con su in-
fluencia, interés y
estrategia
Registro de interesa-
dos.
Están los 17 grupos,
cada uno con un
responsable de
la relación, y el
registro se revisa
antes de cada ola de
implantación.
JP Mes 1.
1.4.2 Plan de comunica-
ciones con calen-
dario y canales por
grupo de interés
Plan de comunica-
ciones.
Cada grupo del
registro tiene su
mensaje, su canal y
su frecuencia.
JP Mes 1.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
24


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 6 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.4.3 Registro de solicitu-
des de cambio con
análisis de impacto
Registro de solici-
tudes de cambio
con su análisis de
impacto.
Cada solicitud tie-
ne su análisis de
impacto y la deci-
sión del Comité
Ejecutivo, y ningún
cambio se ejecuta
sin aprobación.
JP Durante todo el
contrato.
2.1.5 Cuenta 1.5 — Gestión de calidad
Esta cuenta de control reúne las reglas que impiden que algo defectuoso llegue a los usua-
rios.
La Tabla 7 presenta sus paquetes.
Tabla 7 Diccionario de la cuenta 1.5. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.5.1 Plan de calidad y
plan de pruebas
Plan de calidad y
plan de pruebas
aprobados.
Cada tipo de prue-
ba que exigen las
Bases tiene su am-
biente, su calenda-
rio y su criterio de
salida.
CAL Mes 2.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
25


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 7 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.5.2 Puertas de calidad
automáticas: cober-
tura de lógica de
negocio del 70 %,
global del 80 % y del
código modificado
del 80 %
Puertas activas con
informe separado
para cada ámbito.
Se bloquea una
versión si incum-
ple cualquiera de
los tres mínimos:
lógica de negocio
70 % (RT-04.11), glo-
bal 80 % y código
modificado 80 %
(políticas de calidad
de la oferta). Los
denominadores y
resultados se infor-
man por separado;
ninguna versión
llega a Preproduc-
ción con pruebas en
falla.
CAL Desde que exis-
te la cadena
de integración
(3.1.4).
2.1.6 Cuenta 1.6 — Gestión de riesgos
Esta cuenta de control mantiene vivo el registro de riesgos y verifica que cada respuesta se
ejecute.
La Tabla 8 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
26


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 8 Diccionario de la cuenta 1.6. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.6.1 Plan de riesgos y
registro inicial de
riesgos según ISO
31000
Plan de riesgos y
registro inicial.
Cada riesgo tiene
dueño, disparador
y respuesta, y cada
respuesta tiene
un paquete o una
actividad en la EDT.
JP Mes 2.
1.6.2 Registro de riesgos
revisado en cada
Comité de Proyecto
Registro actualizado
con su historial.
El registro se revi-
sa en cada Comi-
té de Proyecto, y
cada cambio de
evaluación queda
registrado.
JP Quincenal, du-
rante toda la
implementa-
ción.
2.1.7 Cuenta 1.7 — Plan de Reversibilidad
Esta cuenta de control asegura que Puelche pueda cambiar de proveedor o asumir la
operación sin interrumpir el servicio. Lo exige el artículo 77 de las Bases Administrativas (p.
39).
La Tabla 9 presenta sus paquetes.
Tabla 9 Diccionario de la cuenta 1.7. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.7.1 Plan de Reversibili-
dad inicial (prime-
ros 90 días)
Plan de Reversibili-
dad.
Se entrega dentro
de los primeros 90
días con sus cuatro
contenidos.
JP Hasta el mes 3.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
27


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 9 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.7.2 Primera actualiza-
ción anual del Plan
de Reversibilidad
durante la imple-
mentación
Plan actualizado. El inventario coinci-
de con lo instalado
a la fecha de la ac-
tualización.
JP Mes 15, al cum-
plirse un año
de la entrega
de 1.7.1; las
actualizaciones
de los meses 27,
39 y 51 son el
paquete 8.1.4
(Art. 77.2).
2.1.8 Cuenta 1.8 — Gobierno y control del proyecto
Esta cuenta de control reúne las instancias de gobierno que el artículo 71 de las Bases
Administrativas (p. 37) hace obligatorias para ambas partes, y los mecanismos de control y
reporte del capítulo 19 de las Bases Técnicas Transversales. Las actas de todos los comités
se levantan dentro de los dos días hábiles siguientes, con acuerdos, responsables y plazos
(RT-19.09).
La Tabla 10 presenta sus paquetes.
Tabla 10 Diccionario de la cuenta 1.8. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.8.1 Oficina de gestión
del proyecto con
metodología basada
en el PMBOK
Oficina constituida,
con su manual de
procedimientos y
sus plantillas.
Los procesos de
alcance, cronogra-
ma, costos, riesgos,
cambios y comu-
nicaciones tienen
procedimiento y
responsable desde
el mes 1.
JP Mes 1, y du-
rante toda la
implementa-
ción.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
28


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 10 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.8.2 Actas del Comité
Ejecutivo mensual,
con la aprobación
de los cambios de
alcance
Un acta por reunión
mensual, con las
decisiones y los
cambios aprobados
o rechazados.
Hay un acta por
mes, levantada
dentro de dos días
hábiles, y todo
cambio ejecutado
tiene su aprobación
previa en un acta.
JP Mensual, du-
rante todo el
contrato.
1.8.3 Actas del Comité de
Proyecto quincenal
Un acta por reunión
quincenal.
Hay un acta cada
quince días, levan-
tada dentro de dos
días hábiles.
JP Quincenal,
durante la im-
plementación.
1.8.4 Actas del Comité
de Arquitectura
mensual
Un acta por reunión
mensual, con las
decisiones de arqui-
tectura registradas.
Hay un acta por
mes, y cada deci-
sión aprobada está
en el registro de
decisiones de arqui-
tectura.
ARQ Mensual, du-
rante todo el
contrato.
1.8.5 Actas del Comité de
Operación mensual,
desde el mes 13
Un acta por reunión
mensual, desde el
mes 13 hasta el mes
56.
Hay un acta por
mes, levantada
dentro de dos días
hábiles.
SRE Mensual, me-
ses 13 a 56.
1.8.6 Informe mensual
de avance con valor
ganado
Un informe por
mes.
Cada informe trae
los índices de valor
ganado, y cada
desviación mayor al
10 % tiene su aviso
y su plan dentro de
cinco días hábiles.
JP Mensual, du-
rante la imple-
mentación.
1.8.7 Tablero de esta-
do del proyecto
disponible para el
CLIENTE
Tablero publicado,
con acceso para el
CLIENTE.
El CLIENTE accede
en todo momento,
y los datos coinci-
den con el último
informe.
JP Desde el mes 2.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
29


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 10 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.8.8 Espacio colabo-
rativo con la do-
cumentación, los
entregables, las ac-
tas, los riesgos y los
cambios
Espacio colabo-
rativo habilitado,
con acceso para el
CLIENTE.
Cada entregable
aceptado y cada
acta están en el es-
pacio, en su versión
vigente.
JP Desde el mes 1.
2.1.9 Cuenta 1.9 — Cumplimiento normativo y contractual
Esta cuenta de control reúne las obligaciones legales y contractuales que no producen
software, pero que el contrato exige mantener y acreditar: cumplimiento normativo, datos
personales, certificación de seguridad, garantías, seguros y obligaciones laborales.
La Tabla 11 presenta sus paquetes.
Tabla 11 Diccionario de la cuenta 1.9. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.9.1 Matriz de cumpli-
miento normativo
por obligación legal,
con su control y su
evidencia
Matriz de cumpli-
miento normativo.
Cada obligación
aplicable tiene su
control y su eviden-
cia, y la matriz está
aprobada por el
CLIENTE.
SEG Mes 1, y ac-
tualizada ante
cada cambio
normativo.
1.9.2 Acuerdo de trata-
miento de datos
personales con el
CLIENTE
Acuerdo firmado. Está firmado antes
de tratar datos
reales; es decir,
antes de cargar el
maestro (3.7.2).
SEG Mes 1.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
30


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 11 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
1.9.3 Registro de activida-
des de tratamiento
y evaluación de im-
pacto en protección
de datos
Registro de trata-
mientos y evaluacio-
nes de impacto.
Cada tratamiento
tiene su registro;
los de alto riesgo
tienen evaluación
de impacto; hay
una contraparte
designada.
SEG Mes 2, y actuali-
zado ante cada
tratamiento
nuevo.
1.9.4 Certificación
ISO/IEC 27001 vi-
gente y entrega
anual de los infor-
mes de certificación
Certificación vi-
gente durante el
contrato e informe
anual de certifica-
ciones.
La certificación
nunca está vencida,
y hay un informe
entregado cada año.
SEG Anual, durante
todo el contra-
to.
1.9.5 Garantía de fiel
cumplimiento, se-
guros y certificados
laborales vigentes
durante el contrato
Garantía constitui-
da, pólizas acredi-
tadas cada año y
certificados labora-
les mensuales.
Ninguna garantía
ni póliza queda
vencida, y hay un
certificado laboral
por mes.
JP Desde la adju-
dicación hasta
el término del
contrato.
2.2 Fase 2. Elaboración
La fase 2 reúne 6 cuentas de control y 20 paquetes de trabajo.
2.2.1 Cuenta 2.1 — Arquitectura de la solución
Esta cuenta de control reúne los planos técnicos del software y de su emplazamiento.
La Tabla 12 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
31


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 12 Diccionario de la cuenta 2.1. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
2.1.1 Documento de
arquitectura lógica:
capas, módulos M1
a M12 e interfaces
Documento de
arquitectura lógica.
Está aprobado en el
H2, y cada requeri-
miento de la línea
base apunta a un
módulo.
ARQ Mes 2 (H2).
2.1.2 Documento de ar-
quitectura física
híbrida: nube, cen-
tros de distribución
y plataformas de
cross-docking
Documento de
arquitectura física.
Está aprobado en el
H2, y cada compo-
nente tiene su lugar
y su razón.
ARQ Mes 2 (H2).
2.1.3 Modelo de datos
y diccionario de
datos, con la traza-
bilidad por lote
Modelo de datos
y diccionario de
datos.
Está aprobado en
el H2, y un retiro
simulado recorre
un lote desde la
recepción hasta sus
clientes.
DAT Mes 2 (H2).
2.1.4 Documento de dise-
ño detallado de M11
y del intercambio
con las cadenas
Documento de
diseño detallado de
la Etapa 2.
Está aprobado en
el H8 y no cambia
ningún contrato de
la Etapa 1.
ARQ Mes 13 (H8).
2.2.2 Cuenta 2.2 — Diseño de la seguridad
Esta cuenta de control define cómo se protegen los datos y los accesos.
La Tabla 13 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
32


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 13 Diccionario de la cuenta 2.2. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
2.2.1 Plan de seguridad
de la información
Plan de seguridad. Está aprobado en el
H2, y cada requisito
de seguridad del T-
12 tiene su control.
SEG Mes 2 (H2).
2.2.2 Modelado de ame-
nazas por compo-
nente y por inte-
gración externa,
actualizado ante
cada cambio
Modelo de amena-
zas con sus contro-
les.
Cada amenaza alta
tiene un control
probado o un riesgo
aceptado por escri-
to por el CLIENTE.
SEG Meses 3 a 10,
y ante cada
cambio de
arquitectura.
2.2.3 Plan de respuesta
a incidentes de
seguridad, con
aviso al CLIENTE
en dos horas
Plan de respuesta
a incidentes de
seguridad.
El plan define la
clasificación, el
escalamiento, los
plazos y los respon-
sables, y se ensaya
una vez antes del
H5.
SEG Mes 3.
2.2.4 Matriz de clasifi-
cación de la infor-
mación y matriz de
controles
Las dos matrices. Cada tipo de dato
tiene su nivel, y ca-
da nivel tiene sus
controles imple-
mentados.
SEG Mes 2 (con el
H2).
2.2.3 Cuenta 2.3 — Diseño de la sala técnica y de los racks
Esta cuenta de control reúne los planos de la infraestructura física que se instala en la fase
6. La sala actual de Talca tiene 25 m², un aire acondicionado de pared y una UPS que dura 10
minutos, y no cumple el estándar exigido (Caso, cap. 5 y 16).
La Tabla 14 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
33


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 14 Diccionario de la cuenta 2.3. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
2.3.1 Plano de la sala téc-
nica de Talca, con
su cálculo eléctrico
y térmico
Plano y memoria de
cálculo.
La potencia y la
climatización cal-
culadas cubren la
carga de diseño con
redundancia N+1.
SRE Meses 1 y 2.
2.3.2 Plano de distribu-
ción de los racks
R01 de servidores
y R02 de comunica-
ciones
Plano de distribu-
ción de los racks.
Los servidores y las
comunicaciones
quedan en racks se-
parados (RT-06.05),
y cada equipo tiene
doble alimentación
(RT-08.04).
SRE Meses 1 y 2.
2.3.3 Plano de los gabi-
netes de borde de
Concepción y de
las plataformas de
cross-docking
Planos de los gabi-
netes.
Cada gabinete sos-
tiene su sitio ope-
rando sin enlace
durante el tiempo
declarado.
SRE Mes 2.
2.2.4 Cuenta 2.4 — Validación de diseños
Esta cuenta de control reúne las dos actas que cierran las fases de Elaboración y dan acceso
a los hitos de pago.
La Tabla 15 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
34


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 15 Diccionario de la cuenta 2.4. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
2.4.1 Acta de aprobación
de la arquitectura,
el plan de seguridad
y el modelo de
datos (H2)
Acta del H2. Está firmada en el
mes 4, sin observa-
ciones abiertas.
ARQ Mes 4 (H2).
2.4.2 Acta de aprobación
del diseño detallado
de la Etapa 2 (H8)
Acta del H8. Está firmada en el
mes 14.
ARQ Mes 13; aproba-
ción en el mes
14 (H8).
2.4.3 Validación del dise-
ño del kit en banco
de pruebas
Kit completo vali-
dado con carga de
ensayo
V1–V3, V5–V8, V11,
V13, V14, V16, V17
y V19 aprobadas
y registradas, sin
alimento comercial.
SRE Mes 3; antes
del mapeo y del
piloto.
2.4.4 Mapeo térmico por
tipo de carrocería
Punto crítico, volu-
men de botellas y
tolerancias por tipo
de caja
V4 compara núcleo
de producto de en-
sayo, simuladores
y aire; Calidad del
CLIENTE valida
punto y tolerancias
con LafroX.
ARQ Mes 4; antes
del piloto.
2.2.5 Cuenta 2.5 — Continuidad del negocio
Esta cuenta de control reúne los planes que dicen cómo sigue operando Puelche si la so-
lución, un sitio o un proveedor fallan. Va más allá de la recuperación técnica (3.1.3): incluye
contingencias auxiliares manuales cuando el proceso las admite. El despacho de 96 camio-
nes entre 05:30 y 07:00 requiere continuidad tecnológica probada, sin sustitución manual ni
interrupción.
La Tabla 16 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
35


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 16 Diccionario de la cuenta 2.5. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
2.5.1 Plan de continuidad
del negocio según
ISO 22301, con
análisis de impacto
y procedimientos
manuales
Plan de continuidad
del negocio con su
análisis de impacto.
Cada proceso iden-
tifica continuidad y
activación aproba-
das por CLIENTE;
sólo admite apo-
yo manual donde
corresponda. El des-
pacho crítico exige
cero interrupción
y flujo tecnológi-
co/DTE probado,
independientemen-
te del RTO general.
SRE Mes 3.
2.5.2 Plan de continuidad
TIC según ISO/IEC
27031 y plan de
recuperación ante
desastres
Plan de continui-
dad TIC y plan de
recuperación ante
desastres.
Los dos planes es-
tán articulados con
el plan de continui-
dad del negocio,
y el RTO y el RPO
coinciden con los
comprometidos.
SRE Mes 3.
2.2.6 Cuenta 2.6 — Experiencia de usuario
Esta cuenta de control reúne el trabajo de diseñar la solución con las personas que la van
a usar, antes de construirla. Lo exige el artículo 26 de las Bases Administrativas (p. 18). En
Puelche es decisivo: preparadores con guantes a −22 °C, preventistas sin señal, conductores
externos que se incorporan en minutos y almaceneros sin internet.
La Tabla 17 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
36


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 17 Diccionario de la cuenta 2.6. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
2.6.1 Investigación con
preparadores, pre-
ventistas, conducto-
res y almaceneros
Informe de investi-
gación de usuarios
por perfil.
Cada perfil opera-
cional tiene sus
tareas críticas y sus
condiciones de uso
documentadas.
IMP Mes 2.
2.6.2 Prototipos y prue-
bas de usabilidad
con participantes
del CLIENTE
Prototipos e infor-
me de las pruebas
de usabilidad.
Cada flujo crítico se
probó con usuarios
de su perfil, y los
hallazgos están
incorporados al
diseño antes de
construir el módulo
(D-05).
IMP Mes 3.
2.6.3 Indicadores de usa-
bilidad comprometi-
dos por transacción
crítica
Tabla de indicado-
res de usabilidad.
Cada transacción
crítica tiene sus
cuatro indicadores,
que se verifican
en las pruebas de
aceptación (3.8.2).
IMP Mes 4.
2.3 Fase 3. Construcción
La fase 3 reúne 11 cuentas de control y 79 paquetes de trabajo.
2.3.1 Cuenta 3.1 — Ambientes y cadena de desarrollo
Esta cuenta de control reúne los lugares donde el software se construye, se prueba y se
ejecuta, y las herramientas que lo mueven entre ellos. Las Bases exigen cinco ambientes:
Desarrollo, QA, Preproducción, Producción y Recuperación ante desastres.
La Tabla 18 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
37


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 18 Diccionario de la cuenta 3.1. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.1.1 Ambientes de De-
sarrollo y QA en la
nube (H3)
Ambientes de Desa-
rrollo y QA operati-
vos.
La cadena de inte-
gración despliega
todos los módulos
en ambos ambien-
tes.
SRE Hasta el mes 5
(H3).
3.1.2 Ambientes de Pre-
producción y Pro-
ducción en la nube
(H3)
Ambientes de Pre-
producción y Pro-
ducción operativos.
La misma versión
del software pasa de
QA a Preproducción
y a Producción sin
volver a compilarse;
toda diferencia
de escala entre
Preproducción y
Producción está
declarada.
SRE Hasta el mes 5
(H3).
3.1.3 Ambiente de re-
cuperación ante
desastres en la re-
gión secundaria
(H3)
Ambiente de recu-
peración habilitado,
con su procedimien-
to de conmutación.
El ambiente está
habilitado en el H3.
La prueba real se
hace en 3.8.5.
SRE Hasta el mes 5
(H3).
3.1.4 Cadena de inte-
gración y entrega
continua, e infra-
estructura como
código
Cadena operativa
y repositorio de
infraestructura
como código.
Un cambio pasa por
la cadena hasta QA
sin intervención
manual; los am-
bientes se pueden
recrear desde el
repositorio.
SRE Mes 4.
3.1.5 Observabilidad de
los doce módulos
y de los sitios, con
tableros para el
CLIENTE (H3)
Tableros y alertas
operativos.
Cada módulo y cada
sitio publica sus
indicadores con
alertas configura-
das.
SRE Hasta el mes
5 (H3: «con
observabilidad
operativa»).
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
38


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
2.3.2 Cuenta 3.2 — Servicios de nube de la plataforma
Esta cuenta de control reúne la puesta en marcha de cada servicio de nube del T-11, antes
de que el software lo use. Contratar el servicio no basta: hay que configurarlo según el plan de
seguridad y conectarlo a la observabilidad.
La Tabla 19 presenta sus paquetes.
Tabla 19 Diccionario de la cuenta 3.2. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.2.1 Servicio de nube
para la aplicación y
los portales
Servicio configura-
do.
El software se des-
pliega en él y cum-
ple el plan de segu-
ridad.
SRE Mes 4.
3.2.2 Servicio de nube
de base de datos,
caché y mensajería
Servicio configura-
do.
La base de datos
replica a la región
secundaria y las
colas entregan
los mensajes sin
duplicarlos.
SRE Mes 4.
3.2.3 Servicio de nube
de ingesta de IoT,
telemetría cruda y
plataforma analítica
Servicio configura-
do.
Las lecturas de un
sensor de prueba
llegan al almacén
analítico.
SRE Mes 4.
3.2.4 Servicio de nube de
respaldo inmutable
y réplica entre
regiones
Servicio configura-
do, con su política
de retención.
Una restauración de
prueba recupera los
datos.
SRE Mes 4.
3.2.5 Servicio de nube
de seguridad y go-
bierno, y detección
en endpoints
Servicio configura-
do.
Los controles del
plan de seguridad
están activos y los
equipos físicos re-
portan a la consola.
SEG Mes 4.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
39


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 19 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.2.6 Servicio de gestión
de dispositivos
móviles
Servicio configura-
do.
Un terminal de
prueba se enrola,
recibe la aplica-
ción y se borra a
distancia.
SRE Antes del en-
rolamiento de
los terminales
(6.5.1).
2.3.3 Cuenta 3.3 — Base compartida
Esta cuenta de control reúne los servicios de software que usan los doce módulos. Se
construyen primero porque, si fallan, fallan todos los módulos a la vez.
La Tabla 20 presenta sus paquetes.
Tabla 20 Diccionario de la cuenta 3.3. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.3.1 Identidad y control
de acceso, incluidos
los conductores
externos que rotan
sin aviso
Identidad y control
de acceso funcio-
nando en QA.
Un conductor ex-
terno nuevo se
habilita en el andén
y pierde el acce-
so al terminar; la
identidad funciona
durante un corte de
24 horas.
SEG Antes del H4.
3.3.2 Integración con el
ERP como único
emisor de la guía de
despacho (INT-06 e
INT-07)
Integración en QA. Toda guía la emite
el ERP; cada entre-
ga se concilia con
su guía el mismo
día; una caída del
ERP no detiene el
despacho.
ARQ Meses 5 y 6;
termina antes
de la prueba de
integración del
H4 (T-15, Tabla
6.1).
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
40


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 20 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.3.3 Convivencia con el
WMS de 2013 duran-
te el reemplazo
Mecanismo de
convivencia y pro-
cedimiento para
apagar el WMS.
No hay doble es-
critura de stock
durante la conviven-
cia.
ARQ Antes del H4.
3.3.4 Integración con la
telemetría de los 42
camiones propios
(INT-15)
Integración en QA. M12 recibe la po-
sición de los 42
camiones.
ARQ Antes del H4.
3.3.5 Registro auditable
de stock, lotes y
cobros
Registro auditable
en QA.
Toda operación de
stock, lote y cobro
queda registrada y
se puede consultar.
ARQ Antes del H4.
3.3.6 Operación sin co-
nexión: 14 horas en
terreno y 24 horas
en el CD
Mecanismo de ope-
ración sin conexión
en QA.
En Preproducción,
una jornada de 14
horas sin señal y un
corte de 24 horas
del CD terminan sin
pedidos perdidos ni
duplicados.
ARQ Antes del H4.
2.3.4 Cuenta 3.4 — Módulos de la Etapa 1
Esta cuenta de control reúne los once programas que la Etapa 1 pone en producción en el
mes 16. Cada uno es un paquete. Se construye por iteraciones de RUP y entra al H4 (mes 10)
con QA superado.
La Tabla 21 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
41


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 21 Diccionario de la cuenta 3.4. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.4.1 Recepción de mer-
cadería con captura
de lote y vencimien-
to (M1 Recepción)
M1 en QA. Los requerimien-
tos del T-12 asig-
nados al módulo
pasan sus pruebas;
además, ningún
producto con traza-
bilidad obligatoria
se recibe sin lote.
DES H4.
3.4.2 Inventario por ubi-
cación y lote, con
FEFO y conteo cícli-
co (M2 Inventario)
M2 en QA. Los requerimientos
del T-12 asignados
al módulo pasan
sus pruebas; ade-
más, cada diferen-
cia de conteo queda
con su causa.
DES H4.
3.4.3 Preparación de pe-
didos en el turno de
noche y en la cáma-
ra de congelado (M5
Preparación)
M5 en QA. Los requerimientos
del T-12 asignados
al módulo pasan
sus pruebas; ade-
más, se opera con
guantes en el termi-
nal de congelado, y
cada faltante queda
con su causa.
DES Meses 5 a 7;
construye des-
pués de los
contratos de
3.4.1/3.4.2 e
integra después
de su entrega
(D-16).
3.4.4 Cadena de frío, re-
tención por SSCC y
retiro sanitario (M9
Calidad y trazabili-
dad)
M9 y doble evalua-
ción del TC58e en
QA.
Reglas por familia,
acción por defecto,
exposición de an-
dén, disposición y
protocolo de rup-
tura; V6–V15 y V21
con retención por
SSCC; retiro en
menos de 2 h.
DES H4, antes del
piloto.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
42


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 21 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.4.5 Ingesta de tempera-
tura (M9) y posición
de flota (M12)
Greengrass de ca-
mión, ingesta móvil
y satelital M9; posi-
ción M12 en QA.
Temperatura a car-
go de M9 con IoT
Core y CloudCon-
nect/SQS; móvil
y satélite siempre
activos, sin pérdi-
das ni duplicados;
M12 conserva solo
posición.
DES H4, antes del
piloto.
3.4.6 Aplicación móvil
de preventa sin co-
nexión, con stock y
crédito (M3 Preven-
ta)
M3 en QA. Los requerimientos
del T-12 asignados
al módulo pasan
sus pruebas; ade-
más, ningún pedido
se pierde ni se du-
plica al recuperar la
señal.
DES H4.
3.4.7 Planificación de
rutas corregible por
el planificador (M4
Rutas)
M4 en QA. Los requerimientos
del T-12 asignados
al módulo pasan
sus pruebas; ade-
más, la ruta se ge-
nera en menos de
20 minutos y don
Hugo la valida.
DES Meses 5 a 8;
construye des-
pués de los
contratos de
3.4.3 y 3.4.6 e
integra después
de su entrega
(D-18); H4.
3.4.8 Aplicación móvil de
reparto con prueba
de entrega digital
(M6 Reparto)
M6 en QA. Los requerimientos
del T-12 asignados
al módulo pasan
sus pruebas; ade-
más, funciona sin
señal, y la prueba
de entrega llega al
ERP el mismo día.
DES Meses 5 a 8;
construye des-
pués de los
contratos de
3.4.3 y 3.4.6 e
integra después
de su entrega
(D-18); H4.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
43


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 21 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.4.9 Devoluciones en
terreno y control
de envases (M8
Devoluciones y
envases)
M8 en QA. Los requerimientos
del T-12 asignados
al módulo pasan
sus pruebas; ade-
más, cada devolu-
ción queda con su
causa.
DES Meses 5 a 8;
H4.
3.4.10 Cobro en ruta, ren-
dición y concilia-
ción (M7 Cobranza
y rendición)
M7 en QA. Los requerimientos
del T-12 asignados
al módulo pasan
sus pruebas; ade-
más, cada cobro
queda unido a su
entrega.
DES Meses 5 a 9;
construye des-
pués de los
contratos de
3.4.8 e integra
después de su
entrega (D-19);
H4.
3.4.11 Indicadores ope-
racionales y OTIF
diario (M10 Analíti-
ca)
Indicadores publica-
dos.
Los requerimien-
tos del T-12 asig-
nados al módulo
pasan sus pruebas;
además, operacio-
nes reproduce el
cálculo sobre una
muestra.
DAT Mes 8; H4.
2.3.5 Cuenta 3.5 — Módulos de la Etapa 2
Esta cuenta de control reúne lo que la Etapa 2 pone en producción en el mes 21. Se construye
entre los meses 13 y 18, mientras la Etapa 1 está en marcha blanca. Entra al H9 (mes 17) con
QA superado.
La Tabla 22 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
44


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 22 Diccionario de la cuenta 3.5. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.5.1 Pedido electrónico
y aviso de despacho
para las cadenas, y
portal de provee-
dores (M11 Canal
moderno)
M11 en QA. Los requerimientos
del T-12 asignados
pasan sus pruebas,
incluido el portal
de proveedores que
consulta en modo
de solo lectura
el estado de sus
órdenes de compra
(RF-12.22).
DES Meses 14 y 15,
tras la entrega
del diseño del
H8; integración
mes 16 (H9).
3.5.2 Portal web de clien-
tes: cuenta, saldo,
entregas y docu-
mentos
Portal en QA. Los requerimientos
del T-12 asignados
pasan sus prue-
bas; además, cada
cliente ve solo sus
datos, y el portal
cumple las normas
de accesibilidad.
DES Meses 14 y 15,
tras la entrega
del diseño del
H8; integración
mes 16 (H9).
3.5.3 Portal web de trans-
portistas: rutas
asignadas del día
siguiente
Portal en QA. Los requerimientos
del T-12 asignados
pasan sus pruebas;
además, cada em-
presa ve solo sus
rutas.
DES Meses 14 y 15,
tras la entrega
del diseño del
H8; integración
mes 16 (H9).
3.5.4 Costo de servir por
cliente y por entre-
ga (M10 Analítica)
Costo de servir
publicado.
Los requerimientos
del T-12 asignados
pasan sus pruebas;
además, finanzas
reproduce el costo
de una muestra de
entregas.
DAT Meses 14 y 15,
tras la entrega
del diseño del
H8; integración
mes 16 (H9).
2.3.6 Cuenta 3.6 — Integraciones externas
Esta cuenta de control reúne las conexiones con terceros que no están en la base compar-
tida. Llevan el código de interfaz de la arquitectura del Capítulo 4 (Subdocumento 4). Cada
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
45


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
integración tiene una conducta definida para cuando el tercero falla, para que una caída
externa no detenga la operación.
La Tabla 23 presenta sus paquetes.
Tabla 23 Diccionario de la cuenta 3.6. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.6.1 Intercambio de lote
y trazabilidad con
los proveedores
Intercambio opera-
tivo con los provee-
dores priorizados.
El proveedor de
lácteos acepta la
evidencia de traza-
bilidad.
DAT Antes del H5.
3.6.2 Integración con la
pasarela de pago
para el cobro con
tarjeta (INT-09)
Integración en QA. Un cobro de prueba
se autoriza, se con-
cilia con su entrega,
y una falla de la
pasarela no lo deja
como aprobado.
DES Antes del H4.
3.6.3 Integración con el
servicio de mapas
y geocodificación
(INT-10)
Integración en QA. Las rutas se gene-
ran con las direc-
ciones georrefe-
renciadas, y la ruta
precargada funcio-
na sin señal.
DES Antes del H4.
3.6.4 Integración con el
servicio de avisos al
cliente (INT-11)
Integración en QA. Un aviso de prueba
llega por el canal
configurado, y los
reintentos quedan
registrados.
DES Antes del H4.
3.6.5 Intercambio electró-
nico con la princi-
pal cadena, con sus
pruebas aprobadas
(INT-08)
Intercambio certifi-
cado por la cadena.
La cadena aprue-
ba por escrito las
pruebas antes del
H10.
DES Meses 13 a 18
(H10).
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
46


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 23 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.6.6 Incorporación de
las demás cadenas
al intercambio
electrónico (INT-08)
Cadenas incorpora-
das.
Cada cadena incor-
porada tiene sus
pruebas aprobadas.
DES Certificación
antes de ca-
da activación;
todo el alcan-
ce habilitado
antes de las
cuatro sema-
nas finales de
marcha blanca
E2.
2.3.7 Cuenta 3.7 — Migración de datos
Esta cuenta de control reúne el traslado de los datos actuales a la nueva solución. Las
Bases exigen dos ensayos antes de la migración definitiva y una conciliación sin diferencias no
explicadas (BTT, num. 20.1, p. 35).
La Tabla 24 presenta sus paquetes.
Tabla 24 Diccionario de la cuenta 3.7. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.7.1 Informe de perfi-
lamiento y datos
saneados
Informe de calidad
de datos y datos
corregidos.
Cada defecto tiene
su corrección o
una aceptación del
dueño del dato.
DAT Antes de 3.7.2.
3.7.2 Datos maestros
cargados: 8.400
SKU, clientes e
instalaciones
Maestro cargado en
Preproducción.
El maestro cuadra
con el origen en los
dos ensayos.
DAT Antes de la
primera ola.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
47


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 24 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.7.3 Saldos migrados
desde el WMS de
Talca
Saldos de Talca
migrados y concilia-
dos.
Los documentos y
los lotes coinciden,
y cada diferencia
de inventario queda
clasificada y explica-
da.
DAT Antes de la ola
de Talca.
3.7.4 Saldos cargados en
Concepción desde
el conteo físico
Saldos de Concep-
ción cargados.
Lo cargado coincide
con el conteo, y
cada diferencia
frente a las planillas
queda clasificada.
DAT Antes de la ola
de Concepción.
3.7.5 Acta de conciliación
y corte fuera de
las ventanas de
congelamiento
Acta de corte por
sitio.
No quedan diferen-
cias sin explicar, y
la fecha no es una
fecha prohibida.
DAT Antes del H6.
2.3.8 Cuenta 3.8 — Pruebas de la Etapa 1
Esta cuenta de control reúne las pruebas que exigen las Bases antes del paso a producción
de la Etapa 1, y el acta que las certifica. Cada prueba tiene su criterio de salida en las Bases
Técnicas Transversales, núm. 20.1, p. 35.
La Tabla 25 presenta sus paquetes.
Tabla 25 Diccionario de la cuenta 3.8. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.8.1 Pruebas de integra-
ción, regresión e
idempotencia en QA
(H4)
Informe de prue-
bas.
Todos los flujos se
ejecutan sin error, y
no hay regresiones.
CAL Ejecución: mes
9. Hito H4: mes
10.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
48


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 25 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.8.2 Pruebas de acepta-
ción y de accesibili-
dad con preventis-
tas, conductores y
bodega
Casos de aceptación
firmados.
Los casos están
firmados por la Con-
traparte Técnica,
y la accesibilidad
cumple WCAG 2.2
AA.
CAL Antes del H5.
3.8.3 Cinco condiciones
físicas: −22 °C con
guantes, lluvia, ca-
lor superior a 34
°C, sol directo y uso
con una mano; des-
conexión separada
de 14 horas
Informe de las
cinco condiciones y
de la desconexión.
Se verifican las cin-
co condiciones, sin
pérdida ni duplica-
ción de registros y
con sincronización
en 10 minutos o
menos.
CAL Antes del H5.
3.8.4 Pruebas de car-
ga con el peak de
septiembre y de
resiliencia
Informe de carga y
resiliencia.
Se cumplen los
tiempos exigidos
a 1,5 veces el peak,
y la solución se
recupera sin inter-
vención.
CAL Antes del H5.
3.8.5 Prueba de recupera-
ción ante desastres
con conmutación
real
Informe AL-DR-01,
mediciones y regis-
tro de correcciones
y repetición.
RTO ≤4 h y RPO
≤15 min medidos
en conmutación
real; tres enlaces,
alarmas 5/15 min,
retorno y concilia-
ción verificados.
Las brechas impi-
den la certificación
hasta su cierre.
CAL Antes del H5;
preparación,
ejecución, co-
rrecciones y
cierre dentro
de la ventana
de T-15.
3.8.6 Prueba de seguri-
dad ofensiva de la
Etapa 1, por un ter-
cero independiente
Informe íntegro del
tercero y evidencia
de las correcciones.
No quedan hallaz-
gos críticos ni altos
abiertos.
SEG Antes del H5.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
49


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 25 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.8.7 Acta de certifica-
ción de la Etapa 1
(H5)
Acta del H5 con
su expediente de
evidencia.
Las pruebas 3.8.2 a
3.8.6 y la demostra-
ción del despliegue
sin interrupción
3.8.8 están aproba-
das, y el acta está
firmada.
CAL Ejecución: me-
ses 10 y 11; el
acta es docu-
mental y no
interviene sis-
temas. Hito H5
del Formulario
E-25: mes 12.
3.8.8 Demostración en
Preproducción
del despliegue sin
interrupción de la
Etapa 1
Informe de la de-
mostración.
La versión se des-
pliega y se revierte
en Preproducción
sin interrupción y
sin intervención
manual.
SRE Antes del H5 y
antes de cada
paso a produc-
ción.
2.3.9 Cuenta 3.9 — Pruebas de la Etapa 2
Esta cuenta de control reúne las mismas pruebas para la Etapa 2, con una exigencia adicio-
nal: demostrar que la Etapa 1, ya en producción, no se degrada.
La Tabla 26 presenta sus paquetes.
Tabla 26 Diccionario de la cuenta 3.9. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.9.1 Pruebas de integra-
ción y regresión sin
afectar la Etapa 1 en
producción (H9)
Informe de prue-
bas.
No hay regresiones
en la Etapa 1.
CAL Ejecución: mes
16. Hito H9 del
Formulario
E-25: mes 17.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
50


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 26 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.9.2 Pruebas de acepta-
ción y de accesibi-
lidad con cadenas,
transportistas, Co-
mercial y Finanzas
Casos firmados. Los casos están
firmados por la
Contraparte Técni-
ca, y los portales
cumplen WCAG 2.2
AA.
CAL Antes del H10.
3.9.3 Pruebas de carga
con ambas etapas
activas y de resilien-
cia
Informe. Se cumplen los
tiempos a 1,5 veces
el peak.
CAL Antes del H10.
3.9.4 Prueba de recupera-
ción ante desastres
con ambas etapas
Informe AL-DR-
01 y correcciones
con ambas etapas
activas.
Conmutación real
con RTO ≤4 h, RPO
≤15 min, alarmas
5/15 min y concilia-
ción de retorno, sin
degradar E1. Se re-
pite lo afectado tras
corregir brechas.
CAL Antes del H10,
dentro de la
ventana de
T-15; prepara-
ción, ensayo
y cierre inclui-
dos.
3.9.5 Prueba de seguri-
dad ofensiva de la
Etapa 2, por un ter-
cero independiente
Informe y correc-
ciones.
No quedan hallaz-
gos críticos ni altos
abiertos.
SEG Antes del H10.
3.9.6 Acta de certifica-
ción de la Etapa 2 y
cierre del desarrollo
(H10)
Acta del H10. Las pruebas 3.9.2 a
3.9.5 y la demostra-
ción del despliegue
sin interrupción
3.9.7 están aproba-
das, y el acta está
firmada.
CAL Ejecución:
meses 16 y 17.
Hito H10 del
Formulario
E-25: mes 18.
3.9.7 Demostración en
Preproducción
del despliegue sin
interrupción de la
Etapa 2
Informe de la de-
mostración.
La versión se des-
pliega y se revierte
sin interrumpir
ninguna de las dos
etapas.
SRE Antes del H10.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
51


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
2.3.10 Cuenta 3.10 — Innovaciones
Esta cuenta de control reúne los paquetes de construcción de las innovaciones 1, 2, 3 y 5.
La parte de la innovación 4 que se hace antes de la Operación está en la fase 5 (5.4.3), porque
es un diseño contractual. Las partes que ocurren durante la Operación están en la fase 8. Las
metas son propuestas de diseño.
La Tabla 27 presenta sus paquetes.
Tabla 27 Diccionario de la cuenta 3.10. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.10.1.1 Innovación 1: docu-
mento de catálogo
de acciones y pro-
tocolo del piloto
(INN-01.P1)
Documento de catá-
logo de acciones y
protocolo del piloto.
Aprobado por Co-
mercial y Calidad.
DAT Meses 7 a 9
3.10.1.2 Innovación 1: esti-
mador de saldo y
ritmo de reposición
(INN-01.P2)
Estimador de saldo
y ritmo de reposi-
ción.
Supera QA y cierra
antes del límite
contractual del H4
(30-11-2027), sin
integrar su entrega
ni su acta.
DAT Meses 9 y 10
(límite del H4)
3.10.1.3 Innovación 1: fun-
ción de lista sin
conexión en la apli-
cación de preventa
(INN-01.P3)
Función de lista
sin conexión en
la aplicación de
preventa.
Funciona sin señal
y cierra antes del lí-
mite contractual del
H4 (30-11-2027), sin
integrar su entrega
ni su acta.
DAT Meses 9 y 10
(límite del H4)
3.10.1.4 Innovación 1: in-
forme del piloto
en marcha blan-
ca y habilitación
(INN-01.P4)
Informe del piloto
en marcha blanca y
habilitación.
Al mes 15, al menos
el 70 % de los avisos
confirma el riesgo,
con al menos 100
avisos.
DAT Meses 11 a 15
(H5 y marcha
blanca)
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
52


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 27 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.10.2.1 Innovación 2: in-
forme de medición
inicial y contrato
de evidencia (INN-
02.P1)
Informe de medi-
ción inicial y contra-
to de evidencia.
Aprobado por el
Encargado de Segu-
ridad.
CAL Meses 2 y 3
3.10.2.2 Innovación 2: cir-
cuito mínimo de
reproducción en
la preventa (INN-
02.P2)
Circuito mínimo de
reproducción en la
preventa.
Un incidente se
reproduce en QA a
partir de su eviden-
cia.
CAL Meses 3 a 5
3.10.2.3 Innovación 2: cap-
tura de evidencia
en las aplicaciones
de preventa, pre-
paración y reparto
(INN-02.P3)
Captura de eviden-
cia en las aplicacio-
nes de preventa,
preparación y repar-
to.
Las tres aplicacio-
nes envían eviden-
cia válida antes del
H4.
CAL Meses 5 a 10
(antes del H4)
3.10.2.4 Innovación 2: infor-
me de validación
comparada durante
la implementación
(INN-02.P4, primera
parte)
Informe de valida-
ción comparada
durante la imple-
mentación.
Al mes 15 se cum-
plen dos metas: el
tiempo de diagnós-
tico baja 30 %, con
al menos 20 casos
comparables, y al
menos el 80 % de
los incidentes se
reproduce.
CAL Meses 11 a 15
(validación en
meses 13 a 15)
3.10.3.1 Innovación 3: docu-
mento de familias
priorizadas y pará-
metros aprobados
(INN-03.P1)
Documento de fa-
milias priorizadas y
parámetros aproba-
dos.
Los parámetros
están aprobados
por Calidad.
DAT Meses 3 a 5
3.10.3.2 Innovación 3: aso-
ciación lote–sensor
en el borde y en el
camión (INN-03.P2)
Asociación lote–sen-
sor en el borde y en
el camión.
Un lote recorre
todo su camino con
historia completa
en QA.
DAT Meses 5 a 9
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
53


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 27 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.10.3.3 Innovación 3: vista
en M9 y orden de
salida sugerido
(INN-03.P3)
Vista en M9 y orden
de salida sugerido.
No cambia la regla
de Calidad y cierra
antes del límite
contractual del H4
(30-11-2027), sin
integrar su entrega
ni su acta.
DAT Meses 9 y 10
(límite del H4)
3.10.3.4 Innovación 3: infor-
me de validación en
marcha blanca con
Calidad (INN-03.P4)
Informe de vali-
dación en marcha
blanca con Calidad.
Al mes 15 se cum-
plen dos metas: al
menos el 95 % de
los lotes tiene his-
toria completa, y al
menos el 80 % de
las estimaciones
queda dentro de
±15 %.
DAT Meses 11 a 15
(H5 y marcha
blanca)
3.10.4.1 Innovación 5: proto-
tipo e informe de la
prueba de compren-
sión (INN-05.P1)
Prototipo e informe
de la prueba de
comprensión.
Al menos el 80 % de
los 24 almaceneros
entiende la hoja.
IMP Meses 13 y 14
3.10.4.2 Innovación 5: eva-
luación de priva-
cidad y diseño de
la impresión en
cabina (INN-05.P2)
Evaluación de pri-
vacidad y diseño
de la impresión en
cabina.
Aprobada por el
Encargado de Segu-
ridad, según la Ley
21.719.
IMP Meses 14 y 15
3.10.4.3 Innovación 5: cálcu-
lo y bloques 1 a 3 de
la hoja de negocio
(INN-05.P3)
Cálculo y bloques
1 a 3 de la hoja de
negocio.
Entra al H9 y fun-
ciona sin señal.
IMP Meses 15 a 17
(H9)
3.10.4.4 Innovación 5: ho-
ja certificada, en
marcha blanca
y en producción
(INN-05.P4, primera
parte)
Hoja certificada, en
marcha blanca y en
producción.
Incluida en el acta
del H12.
IMP Meses 18 a 21
(H10 a H12)
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
54


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
2.3.11 Cuenta 3.11 — Documentación técnica
Esta cuenta de control reúne lo que permite entender, mantener y traspasar la solución. Lo
exige el artículo 77 de las Bases Administrativas (p. 39).
Cada versión liberada se entregará al CLIENTE junto con su SBOM de 3.11.4 en formato
CycloneDX o SPDX, identificando los componentes, sus versiones y licencias (BTT, cap. 11,
RT-11.23, p. 24).
La Tabla 28 presenta sus paquetes.
Tabla 28 Diccionario de la cuenta 3.11. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.11.1 Documentación
técnica, funcional,
de arquitectura,
de operación y de
seguridad
Repositorio docu-
mental con versio-
nes.
Cada versión en
producción tiene su
documentación en
la misma versión.
ARQ Se revisa antes
del H7 y del
H12.
3.11.2 Base de conoci-
miento de inciden-
tes y decisiones de
diseño
Base de conoci-
miento.
Cada incidente
cerrado y cada deci-
sión de arquitectura
tienen su entrada.
Desde la marcha
blanca de la Etapa 1
se miden cada mes
su uso y la utilidad
declarada por los
usuarios; 8.5.3 con-
tinúa la medición
en la Operación.
SRE Desde el H4.
3.11.3 Estándares de codi-
ficación y documen-
tación de interfaces
en OpenAPI y Asyn-
cAPI
Documento de
estándares y do-
cumentación de
interfaces publica-
da.
Cada interfaz tiene
su documentación
generada y versio-
nada, y la cadena de
integración verifica
los estándares.
DES Desde el mes
4, y actuali-
zada en cada
versión.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
55


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 28 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
3.11.4 Inventario de com-
ponentes (SBOM)
con sus licencias de
código abierto
Inventario de com-
ponentes actualiza-
do en cada versión.
Cada componente
tiene su versión
y su licencia, y
ninguna licencia es
incompatible con el
uso del CLIENTE.
DES Desde el mes
4, y en cada
versión.
3.11.5 Depósito del código
fuente en el reposi-
torio del CLIENTE
en cada liberación
Código depositado
en cada liberación.
Cada versión en
producción está en
el repositorio del
CLIENTE, con la
misma etiqueta de
versión.
DES En cada libera-
ción, desde la
primera.
2.4 Fase 4. Transición
La fase 4 reúne 3 cuentas de control y 11 paquetes de trabajo.
2.4.1 Cuenta 4.1 — Plan de implantación
Esta cuenta de control reúne los planes que dicen cómo entra la solución y cómo se vuelve
atrás si algo falla.
La Tabla 29 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
56


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 29 Diccionario de la cuenta 4.1. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
4.1.1 Plan de olas de
la Etapa 1 por si-
tio y zona: Talca,
Concepción y pla-
taformas de cross-
docking
Plan de implan-
tación por sitio y
perfil.
Cada ola tiene su
sitio, su zona, su
criterio de avance
escrito y su registro
oficial.
IMP Antes del H6.
4.1.2 Procedimiento
de reversión de la
Etapa 1 antes de las
05:30, con versión
operativa local y
DTE emitidos por el
ERP
Procedimiento
escrito y ensayado.
Ensayo de reversión
con tiempos medi-
dos, 96 despachos
sin interrupción,
DTE válidos emiti-
dos sólo por ERP,
WMS sólo lectura y
cero pérdida/dupli-
cación; final antes
de 05:30 y fechas
permitidas.
IMP Antes de cada
corte.
4.1.3 Plan de implanta-
ción y reversión de
la Etapa 2 fuera de
la ventana de 05:30
a 07:00
Plan de implanta-
ción de la Etapa
2.
La reversión des-
activa la capacidad
de la Etapa 2 que
falla sin tocar ni
degradar la Etapa 1.
El ensayo se realiza
fuera de la ventana
de 05:30 a 07:00 y
de las fechas prohi-
bidas, con tiempos
medidos y sin pérdi-
da ni duplicación de
datos.
IMP Antes del H11.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
57


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 29 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
4.1.4 Piloto de cadena
de frío en cuatro
camiones
Informe de seis
semanas de piloto
Dos camiones rura-
les, uno urbano y
uno de transportis-
ta; V18, V20 y V21
con evidencia; apro-
bado antes de la ola
de reparto.
IMP Meses 10–11;
seis semanas
antes de la ola
3.
2.4.2 Cuenta 4.2 — Marcha blanca y producción de la Etapa 1
Esta cuenta de control reúne la operación supervisada de la Etapa 1, el acompañamiento
posterior y el acta que la convierte en el registro oficial.
La Tabla 30 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
58


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 30 Diccionario de la cuenta 4.2. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
4.2.1 Marcha blanca
de la Etapa 1 con
conciliación diaria
(H6)
Informes diarios
de indicadores y
de conciliación;
informe mensual
de restauración de
respaldos; acta de
cierre de la marcha
blanca.
Se cumplen las seis
condiciones del
Art. 17.3; cada mes
se restaura una
muestra represen-
tativa sin errores y
se mide el tiempo
efectivo (RT-07.12).
La Contraparte Téc-
nica firma el acta
de cierre al término
del mes 15, lo que
habilita el paso a
producción del mes
16.
IMP Meses 13 a 15.
Empieza con el
H6.
4.2.2 Estabilización de
la Etapa 1, acompa-
ñamiento en ruta y
restauraciones de
soporte puente
Informe de estabili-
zación por ola y tres
informes mensua-
les de restauración,
de los meses 16 a
18.
Cada ruta recibe
al menos un acom-
pañamiento, no
quedan defectos
críticos ni altos
abiertos y cada res-
tauración funciona
sin errores con su
tiempo medido
(RT-07.12).
IMP Meses 16 a 20,
desde el paso
a producción
objetivo del
05-05-2028,
previa acta de
cierre de 4.2.1;
no espera la
aceptación H7
(D-28).
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
59


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 30 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
4.2.3 Acta de aceptación
de la Etapa 1 (H7)
Expediente y acta
de aceptación fir-
mada, distintos del
acta de cierre de
4.2.1.
La Contraparte Téc-
nica acepta en el
mes 16 después del
paso a producción;
entrega objetivo
15-05-2028 y acta
29-05-2028, con
diez días hábiles de
revisión y sin pre-
sumir subsanación
incluida.
JP Mes 16 (H7);
fechas bajo
el supuesto
de inicio en
febrero de
2027.
2.4.3 Cuenta 4.3 — Marcha blanca y producción de la Etapa 2
Esta cuenta de control es igual a la 4.2, aplicada a la Etapa 2. Agrega una condición: convivir
con la Etapa 1 ya en producción, con una sola fuente de verdad para los datos compartidos.
La Tabla 31 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
60


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 31 Diccionario de la cuenta 4.3. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
4.3.1 Marcha blanca de
la Etapa 2 en convi-
vencia con la Etapa
1 y fuente única de
datos (H11)
Informes diarios
de indicadores y
de conciliación;
informe mensual
de restauración de
respaldos; acta de
cierre de la marcha
blanca.
Se cumplen las seis
condiciones del Art.
17.3, no hay doble
digitación y cada
mes se restaura una
muestra represen-
tativa sin errores
con su tiempo me-
dido (RT-07.12). La
Contraparte Técni-
ca firma el acta de
cierre al término
del mes 20, lo que
habilita el paso a
producción del mes
21.
IMP Meses 19 y 20.
Empieza con el
H11.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
61


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 31 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
4.3.2 Estabilización de
la Etapa 2 con Co-
mercial, Finanzas,
cadenas y transpor-
tistas
Informe de estabili-
zación.
No quedan defectos
críticos ni altos
abiertos al cierre
del período.
IMP Desde el paso
a producción
de la Etapa 2
hasta el cierre
del mes 22, con
cuatro sema-
nas reforzadas
posteriores a
la firma del
H12; con inicio
contractual
supuesto en
febrero de 2027,
del 5 de octu-
bre al 30 de
noviembre de
2028, con re-
fuerzo del 26 de
octubre al 22
de noviembre.
4.3.3 Acta de aceptación
final de la imple-
mentación (H12)
Expediente y acta
de aceptación final,
distintos del acta de
cierre de 4.3.1.
La Contraparte
Técnica acepta en el
mes 21 después del
paso a producción,
sin degradación de
E1; entrega objetivo
11-10-2028 y acta
25-10-2028, con
diez días hábiles de
revisión y garantía
constituida.
JP Mes 21 (H12);
fechas bajo
el supuesto
de inicio en
febrero de
2027.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
62


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 31 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
4.3.4 Garantía de correc-
to funcionamiento
constituida, condi-
ción de la acepta-
ción final (H12)
Garantía constitui-
da.
Está entregada
antes de la entrega
del expediente del
H12.
JP Mes 20, en
paralelo con la
marcha blanca
de la Etapa 2;
es un trámite
financiero y
no interviene
sistemas.
2.5 Fase 5. Adquisiciones y contrataciones
La fase 5 reúne 4 cuentas de control y 15 paquetes de trabajo.
2.5.1 Cuenta 5.1 — Hardware e infraestructura
Esta cuenta de control reúne la especificación del equipamiento de terreno que compra el
CLIENTE, la especificación y compra de la infraestructura que provee LafroX y su recepción
técnica. LafroX provee, instala, integra y mantiene la infraestructura dentro del precio con-
tratado (BA, art. 14.2, p. 10); su valorización corresponde a la Oferta Económica conforme al
artículo 51 de las mismas Bases (p. 29).
La Tabla 32 presenta sus paquetes.
Tabla 32 Diccionario de la cuenta 5.1. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
5.1.1 Especificación de
compra de equi-
pos de uso para el
CLIENTE
Especificación de
terminales, impre-
soras, terminales de
pago y balanzas.
Modelos, cantida-
des y necesidad
por ola aprobados
por el CLIENTE;
el sistema de frío
corresponde a 5.1.4.
ARQ Mes 2.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
63


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 32 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
5.1.2 Especificación y
compra de la sala
técnica, los racks,
los servidores y los
gabinetes de borde
Especificación y
orden de compra
emitida por LafroX.
Coincide con los
planos de la fase 2
(2.3) y con el T-11.
LafroX emite la
orden de compra
en el mes 2 para
instalar la sala en el
mes 3.
ARQ Mes 2.
5.1.3 Actas de recepción
técnica del equipa-
miento de terreno
comprado por el
CLIENTE y de la
infraestructura
provista por LafroX
Actas de recepción. El 100 % de lo espe-
cificado se recibe
conforme antes de
su instalación (fase
6).
SRE Según el ca-
lendario de
compra.
5.1.4 Especificación y
compra del sistema
de cadena de frío
Especificación y
órdenes de compra
de LafroX
B-01/B-02 de cáma-
ras y componentes
para 31 kits de ca-
mión; cotización
local y certificación
Subtel aplicable
antes del banco;
compra masiva suje-
ta a aceptación del
prototipo.
ARQ Meses 1–2; an-
tes del banco.
2.5.2 Cuenta 5.2 — Servicios de nube y licencias
Esta cuenta de control reúne los servicios de software que LafroX contrata.
La Tabla 33 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
64


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 33 Diccionario de la cuenta 5.2. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
5.2.1 Contrato de los
servicios de AWS
Servicios contra-
tados y cuentas
habilitadas.
Todos los servicios
de la arquitectura
física del Capítulo 4
están activos antes
de configurar los
ambientes (3.1).
SRE Antes del mes
4.
5.2.2 Suscripción del
servicio de gestión
de dispositivos y
de detección en
endpoints
Suscripciones acti-
vas.
Las licencias cu-
bren todos los equi-
pos del T-11 antes
de su enrolamiento.
SRE Antes del enro-
lamiento de los
terminales.
5.2.3 Licencias de soft-
ware de terceros
constituidas a nom-
bre del CLIENTE
Licencias a nombre
del CLIENTE y su
registro.
Ninguna licencia
de terceros está
a nombre de La-
froX, y todas están
vigentes.
ARQ Antes de usar
cada producto.
2.5.3 Cuenta 5.3 — Enlaces de comunicaciones
Esta cuenta de control reúne los contratos de conexión de los sitios que contrata LafroX. El
caso nombra la dependencia de un solo enlace en Concepción como un riesgo, y Los Ángeles
tiene señal intermitente justo en su ventana de madrugada. Cada CD tiene fibra como enlace
principal, LTE de respaldo y Starlink como tercer camino en espera caliente. Cada plataforma
de cross-docking tiene Starlink como enlace principal y LTE de dos proveedores como respaldo.
La Tabla 34 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
65


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 34 Diccionario de la cuenta 5.3. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
5.3.1 Contrato de fibra
óptica de los CD de
Talca y Concepción
Contrato y fecha de
instalación.
La capacidad con-
tratada coincide
con la del T-11.
SRE Antes del H3.
5.3.2 Contrato de pla-
nes LTE con dos
proveedores (ocho
planes)
Contratos. Los ocho planes
cubren un respaldo
LTE en Talca, uno
en Concepción y
dos de proveedores
distintos en cada
plataforma de cross-
docking.
SRE Antes del H3.
5.3.3 Contrato de Starlink
para los cinco sitios:
Talca, Concepción y
las tres plataformas
de cross-docking
Contratos y equi-
pos.
Cubren los 56 me-
ses del contrato en
los cinco sitios.
SRE Antes del H3.
5.3.4 Contrato de SIM
M2M y servicio
satelital de los ca-
miones con frío
Contratos de dos
operadores móviles
y Globalsat Chile
para Iridium SBD
62 SIM M2M, ser-
vicio bidireccional
y camino de inges-
ta acordado antes
del piloto; sin con-
fundir con SIM
de terminales ni
enlaces de sitio.
SRE Mes 2; servicio
disponible
antes del banco
y del piloto.
2.5.4 Cuenta 5.4 — Acuerdos con terceros
Esta cuenta de control reúne los acuerdos sin los cuales la solución no puede salir a la ruta,
y la fórmula contractual de la innovación 4.
La Tabla 35 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
66


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 35 Diccionario de la cuenta 5.4. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
5.4.1 Acuerdos operacio-
nales firmados con
los diez transportis-
tas
Diez acuerdos fir-
mados.
Los diez acuerdos
están firmados
antes de la ola de
reparto.
IMP Antes del H6.
5.4.2 Acta de acuerdo con
el sindicato sobre
terminales, GPS y
cámaras
Acta firmada por
el sindicato y el
CLIENTE.
Está firmada antes
de la ola de reparto,
y la configuración
respeta lo acordado.
IMP Antes del H6.
5.4.3 Fórmula aprobada
del tramo variable:
reglas de atribución,
canasta e índices
(INN-04.P1)
Fórmula aprobada. Finanzas del CLIEN-
TE aprueba la fór-
mula simulada con
casos antes del mes
21.
JP Meses 17 a 20.
5.4.4 Contrato de custo-
dia de fuentes con
un tercero indepen-
diente
Contrato de cus-
todia firmado y
primer depósito.
El contrato inclu-
ye las cláusulas de
liberación ante in-
solvencia o incum-
plimiento grave, y
el primer depósito
está hecho.
JP Antes del H4.
2.6 Fase 6. Infraestructura física y sitios
La fase 6 reúne 6 cuentas de control y 24 paquetes de trabajo.
2.6.1 Cuenta 6.1 — Adecuación de la sala técnica de Talca
Esta cuenta de control reúne el trabajo de convertir la sala de Talca en una sala técnica que
cumpla las Bases (BTT, capítulo 6). Termina con un acta que habilita el montaje de los racks.
La Tabla 36 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
67


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 36 Diccionario de la cuenta 6.1. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
6.1.1 Coordinación de la
obra civil de sepa-
ración, a cargo del
CLIENTE (RT-06.06),
y piso técnico de la
sala
Sala acondicionada
según el plano, con
obra civil de sepa-
ración especificada
y coordinada por
LafroX y piso téc-
nico provisto por
LafroX.
El recinto coincide
con el plano apro-
bado, incluido el
blindaje perimetral
especificado, y está
listo para recibir los
equipos.
SRE Mes 3, después
de la especi-
ficación 5.1.2
(D-10).
6.1.2 Hardware de ener-
gía instalado: UPS
modular N+1, ge-
nerador con 24
horas de autono-
mía, transferencia
automática y PDU
A/B
Sistema de energía
instalado y proba-
do.
En una prueba con
carga real, el corte
de la red pasa a la
UPS y al generador
sin que se apague
ningún equipo.
SRE Mes 3.
6.1.3 Hardware de clima-
tización de preci-
sión N+1 instalado
Climatización insta-
lada y probada.
Con un equipo
apagado, la sala se
mantiene en el ran-
go de temperatura
del fabricante.
SRE Mes 3.
6.1.4 Hardware de de-
tección temprana
de incendio y ex-
tinción por agente
limpio instalado
Sistema instala-
do y conectado al
monitoreo.
Una prueba de
detección genera
la alarma en el
monitoreo, y la
extinción queda
armada.
SRE Mes 3.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
68


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 36 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
6.1.5 Acta de recepción
técnica de la sala
Acta firmada con
disponibilidad del
recinto.
Obra civil y piso
técnico 6.1.1 recibi-
dos y pruebas 6.1.2
a 6.1.4 aprobadas.
La disponibilidad
del espacio por el
CLIENTE se acredi-
ta, no se presume
por la fecha planifi-
cada.
SRE Mes 4, después
de 6.1.1 a 6.1.4
y antes del
montaje de los
racks (6.3).
2.6.2 Cuenta 6.2 — Cableado estructurado
Esta cuenta de control reúne la red física de cables que conecta los equipos de la sala y de
las bodegas.
La Tabla 37 presenta sus paquetes.
Tabla 37 Diccionario de la cuenta 6.2. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
6.2.1 Cableado de cobre
Cat6A y fibra OM4
tendido, con dos
ductos de ingreso
independientes
Cableado tendido. Los dos ductos de
ingreso están se-
parados (RT-06.32),
y todos los puntos
del diseño están
cableados.
SRE Mes 4.
6.2.2 Certificación de
enlaces, etiquetado
y planos as-built
Informe de certifi-
cación por enlace y
planos as-built.
El 100 % de los enla-
ces está certificado
y etiquetado.
SRE Mes 6.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
69


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 37 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
6.2.3 Gabinetes de piso y
switches de acceso
instalados en las
bodegas de Talca y
Concepción
Gabinetes de piso
instalados y conec-
tados.
Cada punto de la
bodega tiene red, y
el Wi-Fi cubre las
zonas de trabajo de
los terminales.
SRE Antes del H6.
2.6.3 Cuenta 6.3 — Montaje de racks y gabinetes
Esta cuenta de control reúne el montaje de los equipos de cómputo y comunicaciones en
cada uno de los cinco sitios.
La Tabla 38 presenta sus paquetes.
Tabla 38 Diccionario de la cuenta 6.3. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
6.3.1 Rack R01 de ser-
vidores montado:
clúster de tres no-
dos, respaldo local,
consola KVM y tras-
lado del servidor
del ERP del CLIEN-
TE
Rack montado,
energizado por los
dos caminos y co-
nectado. Servidor
del ERP de 2017
trasladado desde
la sala actual de 25
m² a R01 (U25–U26),
con respaldo com-
pleto verificado, en
ventana dominical
y sin cambios de
software.
Cada equipo tiene
doble fuente en cir-
cuitos distintos. El
clúster sigue funcio-
nando con un nodo
apagado. El trasla-
do del ERP a R01
se realiza después
del H3 y antes de la
marcha blanca de
Talca, con respaldo
completo verificado,
en ventana domini-
cal y sin cambios
de software (SD4,
4.3.1.4; T-11).
SRE Montaje antes
del H3. Tras-
lado del ERP
después del H3
y antes de la
marcha blanca
de Talca.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
70


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 38 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
6.3.2 Rack R02 de comu-
nicaciones monta-
do: firewalls, swit-
ches de núcleo y de
gestión, y distribu-
ción de fibra
Rack montado y
conectado.
Al apagar un fire-
wall o un switch,
el tráfico sigue sin
cortarse.
SRE Antes del H3.
6.3.3 Gabinete de bor-
de de Concepción
montado: servi-
dores activo y en
espera, firewalls,
switches, UPS, cli-
matización y moni-
toreo
Gabinete montado
y monitoreado, con
dos servidores HPE
DL20 (activo y en
espera).
El gabinete reporta
su estado al centro
de operaciones, la
falla de un firewall
no corta la red y el
servidor de espera
toma el servicio si
falla el activo.
SRE Antes del H3.
6.3.4 Gabinetes de bor-
de montados en
Curicó, Chillán y
Los Ángeles, con
dos mini-PC (activo
y en espera) por
plataforma
Tres gabinetes
montados, cada uno
con dos mini-PC
industriales E-01
(activo y en espera).
Cada plataforma
opera su ventana de
madrugada con el
enlace cortado y el
mini-PC de espera
toma el servicio si
falla el activo.
SRE Antes de la
ola de cross-
docking.
2.6.4 Cuenta 6.4 — Sistemas de seguridad física
Esta cuenta de control reúne lo que protege físicamente a la sala y a sus respaldos.
La Tabla 39 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
71


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 39 Diccionario de la cuenta 6.4. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
6.4.1 Hardware de con-
trol de acceso bio-
métrico y esclusa
instalado
Control de acceso
instalado y con las
personas autoriza-
das enroladas.
Solo las personas
enroladas entran, y
cada ingreso queda
registrado.
SEG Antes del H3.
6.4.2 Hardware de video-
vigilancia instalado
Cámaras instaladas
y conectadas al
monitoreo.
Se pueden consultar
las imágenes de las
seis zonas de los
últimos 30 días.
SEG Antes del H3.
6.4.3 Recinto de custo-
dia de respaldos
habilitado
Recinto habilitado. El recinto mantiene
entre 18 y 27 °C y
entre 40 y 60 % de
humedad.
SEG Antes del H3.
2.6.5 Cuenta 6.5 — Equipamiento de campo
Esta cuenta de control reúne la puesta en marcha de los equipos que usan las personas en
la bodega y en la ruta. Se instalan por olas, antes de que cada ola empiece.
La Tabla 40 presenta sus paquetes.
Tabla 40 Diccionario de la cuenta 6.5. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
6.5.1 Terminales de pre-
venta, reparto y
bodega configura-
dos y enrolados
Terminales enrola-
dos y asignados.
El 100 % de los
terminales de cada
ola está enrolado y
probado antes de
que la ola empiece.
SRE Antes de cada
ola (H6).
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
72


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 40 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
6.5.2 Terminales de pago
configurados, uno
por camión
Terminales de pago
configurados y
asignados a cada
camión.
Un cobro de prueba
con tarjeta se autori-
za y queda unido a
su entrega.
SRE Antes de la ola
de reparto.
6.5.3 Sensores de cámara
y gateways IoT ins-
talados en Talca y
Concepción
Sensores y gate-
ways instalados y
calibrados.
Los 21 puntos re-
portan a M12 sin
brechas durante
una semana an-
tes de la marcha
blanca.
SRE Antes del H5.
6.5.4 Kit de cadena de
frío instalado y
recibido en los 28
camiones con frío
Acta por camión,
kit instalado y che-
queo completo.
Cuatro actas antes
del piloto y 28 antes
de la ola 3; alarma
simulada, asocia-
ción de registrado-
res y protección
local comprobadas.
SRE Meses 8–12;
antes de la ola
de reparto.
6.5.5 Impresoras de
cabina instaladas
Impresoras instala-
das y vinculadas al
terminal de reparto.
Cada camión impri-
me sin señal.
SRE Antes de la ola
de reparto.
6.5.6 Impresoras de an-
dén y balanzas de
recepción instala-
das
Equipos instalados
y conectados.
La recepción im-
prime etiquetas
y registra el peso
desde M1.
SRE Antes de la ola
de recepción.
2.6.6 Cuenta 6.6 — Configuración de la infraestructura de los sitios
Esta cuenta de control reúne lo necesario para que el hardware instalado funcione como
plataforma: el software de base, los enlaces y la prueba de autonomía.
La Tabla 41 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
73


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 41 Diccionario de la cuenta 6.6. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
6.6.1 Software de base
instalado en los si-
tios: virtualización,
contenedores, Post-
greSQL, RabbitMQ y
Keycloak
Software de base
instalado en los
cinco sitios.
Cada sitio ejecuta la
misma imagen de
la aplicación que la
nube.
SRE Antes del H3.
6.6.2 Enlaces de fibra,
LTE y Starlink habi-
litados, con conmu-
tación al respaldo
Enlaces operativos. Al cortar el enlace
principal, el respal-
do toma el tráfico
en menos de 30
segundos.
SRE Antes del H3.
6.6.3 Borde de los CD
en servicio, con
la prueba de auto-
nomía de 24 horas
aprobada
Informe de la prue-
ba de autonomía
por sitio.
Cada CD opera 24
horas sin enlace y
concilia sin pérdi-
das ni duplicados.
SRE Mes 5, antes
del H3; pruebas
de aceptación
ampliadas
antes del H5.
2.7 Fase 7. Capacitación y gestión del cambio
La fase 7 reúne 3 cuentas de control y 13 paquetes de trabajo.
2.7.1 Cuenta 7.1 — Capacitación por roles
Esta cuenta de control reúne la capacitación de cada grupo según su rol y su situación.
Todo el material de capacitación de 7.1.5, incluidos manuales por perfil, guías rápidas,
preguntas frecuentes y videos tutoriales, y la base de conocimiento consultable de 3.11.2 y
8.5.3 se entregarán en español, en formato editable y serán de propiedad del CLIENTE (BTT,
cap. 22, RT-22.03, p. 38).
El plan de 7.1.1 acordará con el CLIENTE un calendario para todos los perfiles, por turno
y horario, sin afectar la preparación nocturna, el despacho de 05:30 a 07:00 ni las labores en
calle de lunes a sábado, y considerando los peaks de septiembre y diciembre. La capacitación
de conductores externos se acordará con cada transportista mediante 5.4.1, y la inducción
continua de preparadores de 7.1.2 atenderá la rotación anual del 38 % sin detener la operación
(BTT, cap. 22, RT-22.04, p. 38; Caso, cap. 15, pp. 26–27).
La Tabla 42 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
74


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 42 Diccionario de la cuenta 7.1. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
7.1.1 Plan de capaci-
tación por perfil:
usuarios finales,
avanzados, admi-
nistradores, equipo
técnico y soporte
Plan de capacita-
ción aprobado.
Cubre todos los
perfiles de cada ola
y está aprobado por
el CLIENTE.
IMP Antes del H6.
7.1.2 Programa de capaci-
tación continua del
turno de noche por
la rotación del 38 %
Programa de in-
ducción continua y
tutores formados.
Un preparador nue-
vo opera su flujo
después de un máxi-
mo de dos horas de
aprendizaje.
IMP Desde el H6, y
durante toda la
Operación.
7.1.3 Incorporación
de conductores
de transportistas,
escaneos y lectura
del rojo
Inducción y habili-
tación registrada de
cada conductor.
Incluye salida de
cámara, carga y ba-
jada, rojo en TC58e
y prohibición de
liberar; nadie sale a
ruta sin inducción.
IMP Meses 11–20;
antes de la
salida de cada
conductor.
7.1.4 Traspaso al equipo
de TI de cuatro per-
sonas del CLIENTE
Acuerdo de qué fun-
ciones se traspasan
y qué funciones
quedan como servi-
cio, y certificación
de las cuatro perso-
nas.
Las cuatro personas
están certificadas
en sus funciones
antes del cierre
de cada marcha
blanca.
IMP Antes del H7 y
del H12.
7.1.5 Materiales de capa-
citación: manuales
por perfil, guías
rápidas, preguntas
frecuentes y videos
tutoriales
Materiales por
perfil.
Cada perfil tiene su
manual, su guía rá-
pida, sus preguntas
frecuentes y sus vi-
deos, entregados en
formato editable.
IMP Antes del H6,
y actualizados
antes del H11.
7.1.6 Plataforma de au-
toformación en
línea con registro
de avance
Plataforma habili-
tada con los cursos
por perfil.
Cada perfil tiene su
curso, y el avance
de cada persona
queda registrado.
IMP Antes del H6.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
75


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
2.7.2 Cuenta 7.2 — Gestión del cambio
Esta cuenta de control reúne el acompañamiento de quienes no basta con capacitar.
La Tabla 43 presenta sus paquetes.
Tabla 43 Diccionario de la cuenta 7.2. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
7.2.1 Acompañamiento
del personal con
20 o 30 años en la
compañía
Registro del acom-
pañamiento por
persona.
Cada persona iden-
tificada tiene su
plan de acompa-
ñamiento y queda
certificada.
IMP Antes del H6 y
hasta el H7.
7.2.2 Gestión del cambio
con las cadenas y
los transportistas
Plan de comuni-
cación externa
ejecutado.
Cada cadena y cada
transportista recibe
la comunicación y
su acceso antes de
la marcha blanca de
la Etapa 2.
IMP Antes del H11.
7.2.3 Diagnóstico del
impacto organiza-
cional por área y
perfil, con agentes
de cambio
Diagnóstico de im-
pacto y nómina de
agentes de cambio
habilitados.
Cada área tiene su
impacto y sus resis-
tencias previstas,
con una estrategia
para cada una, y
cada sitio tiene al
menos un agente de
cambio.
IMP Meses 2 a 6.
7.2.4 Procedimientos
operativos rediseña-
dos, contingencia
de frío y ruptura
confirmada
Procedimientos
por ruta y proceso
aprobados.
Incluye reparación,
trasbordo o retorno,
entrega parcial,
ajuste ERP, repo-
sición, área de no
aptos y disposición;
procedimiento de
frío antes del piloto.
IMP Meses 8–20;
antes del piloto
y de cada ola.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
76


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 43 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
7.2.5 Medición de la
adopción y plan de
acción correctiva
Informe de adop-
ción por ola y plan
de acción cuando
corresponde.
Cada ola tiene su
medición, y cada
meta no alcanzada
tiene su plan.
IMP Durante cada
marcha blanca
y en la estabili-
zación.
2.7.3 Cuenta 7.3 — Evaluaciones y certificaciones
Esta cuenta de control reúne las pruebas con que se demuestra que cada persona sabe usar
la solución. Es una de las seis condiciones del artículo 17.3 de las Bases Administrativas (p. 13).
La Tabla 44 presenta sus paquetes.
Tabla 44 Diccionario de la cuenta 7.3. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
7.3.1 Certificación de pre-
ventistas, conducto-
res y preparadores
(Etapa 1)
Registro de cer-
tificaciones por
persona.
El 100 % de los
usuarios de la ola
está certificado
antes de su cierre.
IMP H6 y H7.
7.3.2 Certificación de Co-
mercial y Finanzas
en costo de servir
(Etapa 2)
Registro de certifi-
caciones.
El 100 % de los
usuarios definidos
está certificado
antes del mes 19.
IMP Antes del H11.
2.8 Fase 8. Operación y soporte (36 meses)
La fase 8 reúne 5 cuentas de control y 26 paquetes de trabajo.
2.8.1 Cuenta 8.1 — Servicios de operación
Esta cuenta de control reúne los servicios que mantienen la solución funcionando cada
día y la actualización anual del Plan de Reversibilidad, que exige el artículo 77 de las Bases
Administrativas (p. 39).
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
77


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
El SOC de 8.1.5 notificará al CLIENTE toda brecha de seguridad o de datos personales dentro
de las 24 horas de su detección, adjuntando un informe preliminar, y entregará su análisis de
causa raíz dentro de los cinco días hábiles siguientes a la detección (BTT, cap. 11, RT-11.19, p.
24). Durante Operación realizará al menos un ejercicio de simulación de incidente por año
con participación del CLIENTE, conservando el escenario, la bitácora y las acciones de mejora
(RT-11.21).
En 8.1.2, cada incidente crítico tendrá un análisis de causa raíz obligatorio entregado al
CLIENTE dentro de cinco días hábiles desde el incidente, con acciones correctivas, responsa-
bles y plazos; SRE seguirá cada acción hasta su cierre verificado en la gestión de problemas
(BTT, cap. 14, RT-14.06, p. 27). La documentación operativa reunirá el libro de operación y una
guía de resolución para cada escenario de falla previsible, incluidos los de los contratos de in-
tegración y el plan de continuidad; el servicio mantendrá estos procedimientos y automatizará
progresivamente las tareas repetitivas con las herramientas de operación previstas (RT-14.05).
El canal único de la mesa registrará incidentes y solicitudes con número de ticket, clasifica-
ción por severidad y seguimiento de todas sus actuaciones y estados hasta el cierre conforme,
con el escalamiento L1–L3 previsto (BTT, cap. 21, RT-21.15, p. 37). El cierre de cada ticket
requerirá la confirmación de la persona usuaria registrada en él; mientras falte, permanecerá
pendiente de cierre y sujeto al seguimiento de la mesa (RT-21.17).
El servicio conservará un registro histórico de todas las actividades de soporte, vinculadas a
su ticket, con clasificación, actuaciones, responsables y resultado (BTT, cap. 21, RT-21.09, p. 36).
El informe mensual de niveles de servicio de 8.1.2 analizará las tendencias de los principales
requerimientos, detallará el cumplimiento por severidad y analizará cada incumplimiento,
indicando causa, impacto y acción correctiva con responsable y plazo; sus resultados se
revisarán en el Comité de Operación (RT-21.09 y RT-21.18).
Guillermo Castillo, Líder de Operación / SRE, es el gerente de servicio dedicado de la
Operación: con 100 % de dedicación en los meses 21 a 56, es la contraparte permanente del
CLIENTE, representa a LafroX en el Comité de Operación mensual y responde por los niveles
de servicio, los incidentes y el plan de mejora continua (BA, art. 71, p. 37; BTT, cap. 21, RT-21.02,
p. 36; Subdocumento 1, Tabla 1.6).
Los niveles 2 y 3 de la mesa los cubren especialistas distintos de los puestos de mesa de
8.1.2 y del puesto NOC de 8.1.1: en infraestructura y terreno, el equipo SRE de mantenimiento
del hardware de 8.2.3, que ya atiende sala técnica, racks, gabinetes de borde y equipamiento de
terreno; en aplicación, el equipo DES de mantención correctiva de 8.2.1, con apoyo del Líder
de Operación / SRE. El nivel 4 es el soporte del fabricante, que LafroX gestiona sin trasladar su
responsabilidad (BTT, sección 21.3, p. 37). Cuando la resolución de un incidente lo requiere, un
especialista de nivel 2 o 3 se traslada a Curicó, Chillán, Los Ángeles o al sitio que corresponda
por el medio más rápido disponible y permanece en el sitio hasta resolverlo. Como proviene de
8.2.1 o de 8.2.3, los puestos de mesa, NOC y SOC siguen cubiertos y los demás sitios conservan
su atención normal. El traslado no reemplaza la recuperación remota: el restablecimiento
dentro de los plazos del artículo 78 de las Bases Administrativas (p. 40) sigue a cargo del equipo
en espera, la gestión remota y el responsable del sitio (Subdocumento 4, sección 4.2.4.3), y el
traslado se destina a la resolución definitiva. El tiempo del especialista se imputa al paquete
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
78


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
del que proviene; si los traslados exceden esa capacidad, LafroX los cubre sin costo adicional
para el CLIENTE. Pasajes y viáticos se incluyen en la Oferta Económica, porque el CLIENTE no
reembolsa viajes ni traslados (BA, arts. 11.2 y 51, pp. 9 y 29; BTT, cap. 21, RT-21.16, p. 37).
La Tabla 45 presenta sus paquetes.
Tabla 45 Diccionario de la cuenta 8.1. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
8.1.1 Servicio de centro
de operaciones 24×7
y mesa de servicio
durante los 36 me-
ses de operación
(04:00 a 22:00; 24×7
en septiembre y
diciembre)
El servicio prestado
durante los 36 me-
ses, con un informe
mensual de servicio
y un informe anual
por cada año de
operación.
Se cumplen los ho-
rarios de cobertura
en cada uno de los
36 meses.
SRE Meses 21 a 56.
Se paga en el
hito mensual.
8.1.2 Servicio de gestión
de incidentes, pro-
blemas y niveles
de servicio del Art.
78° durante los 36
meses de operación
El servicio prestado
durante los 36 me-
ses, con un informe
mensual de nive-
les de servicio, los
informes de causa
raíz y un informe
anual.
Se cumplen los
tiempos, y cada
incidente crítico
tiene su informe a
tiempo.
SRE Meses 21 a 56.
Las multas se
descuentan del
hito mensual.
8.1.3 Servicio de conti-
nuidad y pruebas
semestrales de re-
cuperación ante
desastres duran-
te los 36 meses de
operación
Siete pruebas de
conmutación en los
36 meses (una al ini-
cio de la Operación
y luego dos por año,
la última en el mes
54), cada una con su
informe.
Cada prueba alcan-
za el RTO y el RPO
comprometidos en
una conmutación
real, programada
fuera de los con-
gelamientos y con
separación máxima
de seis meses.
SRE Meses 21, 27,
33, 39, 45, 51 y
54.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
79


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 45 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
8.1.4 Actualizaciones
anuales del Plan de
Reversibilidad du-
rante los 36 meses
de operación
Tres actualizacio-
nes del plan, una
por año de opera-
ción.
En cada actualiza-
ción, el inventario,
las claves y la ex-
portación están
vigentes.
JP Meses 27, 39
y 51, conti-
nuando la serie
anual que ini-
cia 1.7.2 (Art.
77.2).
8.1.5 Servicio de centro
de operaciones
de seguridad 24×7
con SIEM desde la
primera marcha
blanca (mes 13)
hasta el mes 56
El servicio prestado
desde el mes 13 has-
ta el mes 56, con un
informe mensual de
seguridad.
Cobertura 24×7 to-
dos los meses, cada
incidente crítico
avisado dentro de
dos horas y cada
brecha notificada
dentro de 24 horas.
SEG Meses 13 a 56.
8.1.6 Pruebas mensuales
de restauración de
respaldos durante
los 36 meses de
operación
36 informes de
restauración, uno
por mes.
Cada mes la restau-
ración funciona
sin errores, con su
tiempo medido.
SRE Mensual, me-
ses 21 a 56.
2.8.2 Cuenta 8.2 — Mantenimiento
Esta cuenta de control reúne el trabajo que mantiene la solución sana y actualizada, sepa-
rado por tipo: software, ciberseguridad y hardware.
LafroX destinará las 2.304 HH DES de 8.2.4 a reducir la deuda técnica durante los 36 meses
de Operación, equivalentes al 1,7881 % de las 128.853,67 HH de esa etapa: 2.304 ÷ 128.853,67
× 100 = 1,7881 %. Esa capacidad equivale a 2.304 ÷ 36 = 64 HH mensuales y 64 × 12 = 768
HH anuales, con seguimiento en el registro cuantificado y el informe trimestral existentes;
la fracción corresponde al total del período (BTT, cap. 21, RT-21.21, p. 38; Formulario T-15,
secciones 4.2, 4.3 y 6.2).
El paquete 8.2.1 reparte sus 4.608 HH DES, es decir 4.608 ÷ 3 = 1.536 HH por año de
Operación, en dos partes. La bolsa anual de mantención evolutiva es de 768 HH DES por
año y se reserva para las mejoras funcionales, nuevas características y optimizaciones del
desempeño que solicite el CLIENTE; la mantención correctiva y la normativa no la consumen.
Las otras 768 HH anuales son la capacidad estimada para la mantención correctiva, incluido
el mantenimiento de la Innovación 1 (Formulario T-19), y no son un tope: la corrección de
defectos no tiene costo adicional y la que exceda esa estimación la absorbe LafroX (BTT, sección
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
80


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
21.4, pp. 37–38). La bolsa no utilizada en un año no se pierde y se acumula al año siguiente; en
el tercer año, el Comité de Operación programa el uso del saldo acumulado dentro del período
de Operación. Las horas que excedan la bolsa disponible se liquidan con la tarifa declarada
en la Oferta Económica (BA, art. 51, p. 29). La bolsa se compone del perfil DES, el mismo
que desarrolla la solución, y cada cambio pasa por el pipeline, las pruebas y las puertas de
calidad del desarrollo original (BTT, cap. 21, RT-21.20, p. 38). El procedimiento tiene cuatro
pasos. Solicitud: la Contraparte Técnica registra el cambio en el canal único de la mesa, con su
ticket. Estimación: DES entrega en cinco días hábiles las HH, el alcance y el impacto estimados.
Aprobación: el CLIENTE aprueba por escrito en el Comité de Operación antes de iniciar el
trabajo. Liquidación: el informe mensual de 8.1.1 descuenta las HH reales de cada cambio
desplegado e informa el saldo del año y el saldo acumulado (BTT, cap. 21, RT-21.19, p. 37).
La Tabla 46 presenta sus paquetes.
Tabla 46 Diccionario de la cuenta 8.2. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
8.2.1 Mantenimiento
correctivo y evolu-
tivo del software
durante los 36 me-
ses de operación,
con bolsa anual
de horas y fuera
de las ventanas de
congelamiento
Versiones desple-
gadas, cada una
con su registro: re-
quisito, cambio,
prueba, aprobación
y despliegue.
Ningún despliegue
cae en una fecha
prohibida, y cada
cambio tiene su
registro completo.
DES Meses 21 a 56.
8.2.2 Mantenimiento
de ciberseguridad
durante los 36 me-
ses de operación:
vulnerabilidades,
intrusión anual e
inyección de fallas
En los 36 meses, los
informes periódicos
de vulnerabilida-
des, tres informes
de intrusión (uno
por año) y seis de
resiliencia (dos por
año).
Se cumplen los pla-
zos de corrección;
la prueba anual
termina sin hallaz-
gos críticos ni altos
abiertos; hay dos
pruebas de resilien-
cia por año, con
separación máxima
de seis meses.
SEG Intrusión en
meses 28, 40 y
52; resiliencia
en meses 26,
32, 38, 44, 50 y
55.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
81


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 46 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
8.2.3 Mantenimiento
del hardware du-
rante los 36 meses
de operación: sala
técnica, racks, ga-
binetes de borde y
equipamiento de
terreno
Registro de mante-
nimientos de los 36
meses y un informe
anual por cada año
de operación.
Se cumplen los
mantenimientos
programados, y
ningún equipo
crítico queda sin
repuesto.
SRE Meses 21 a 56.
8.2.4 Registro y reduc-
ción de la deuda
técnica durante
los 36 meses de
operación
Registro de deuda
técnica e informe
trimestral de su
reducción.
El registro está
cuantificado y se
cumple la fracción
de capacidad decla-
rada.
DES Meses 21 a 56.
8.2.5 Actualizaciones
anuales de los com-
ponentes de base
durante los 36 me-
ses de operación
Plan anual de ac-
tualización y su
ejecución.
Cada año hay un
plan aprobado,
ejecutado en su
ventana y con su
reversión ensayada.
SRE Una vez por
año, meses 21 a
56.
8.2.6 Revisiones semes-
trales de las insta-
laciones eléctricas
de la sala durante
los 36 meses de
operación
Seis informes de
revisión eléctrica.
Cada semestre hay
una revisión con
su informe y sus
correcciones.
SRE Semestral,
meses 21 a 56.
8.2.7 Ciclo de vida del
equipamiento du-
rante los 36 meses
de operación: repo-
sición y disposición
final
Plan de ciclo de
vida y registro de
reposiciones y dis-
posiciones.
Cada tipo de equipo
del T-11 tiene su
ciclo de vida, y cada
equipo retirado
tiene su disposición
registrada.
SRE Meses 21 a 56.
2.8.3 Cuenta 8.3 — Innovaciones en operación
Esta cuenta de control reúne la parte de las innovaciones que ocurre después del mes 21.
Las metas son propuestas de diseño.
La Tabla 47 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
82


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 47 Diccionario de la cuenta 8.3. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
8.3.1 Innovación 2: man-
tenimiento de esce-
narios de regresión
(INN-02.P4, segun-
da parte)
Informe trimestral. Ningún incidente
se reabre por la
misma causa, y
ninguna evidencia
contiene datos
personales.
CAL Desde el mes
21.
8.3.2 Innovación 3: revi-
sión semestral de
parámetros durante
los 36 meses de ope-
ración (INN-03.P5)
Parámetros ajusta-
dos con aprobación
del Líder de Calidad
de LafroX y de Cali-
dad del CLIENTE.
Cada revisión se-
mestral queda
documentada y
aprobada por el
Líder de Calidad de
LafroX y Calidad del
CLIENTE. Si la exac-
titud baja del 80 %
dos veces seguidas,
se hace un ajuste
extraordinario.
SRE Meses 26, 32,
38, 44, 50 y 56
del proyecto.
8.3.3 Innovación 4: línea
base y liquidaciones
en sombra (INN-
04.P2)
Línea base y tres
liquidaciones de
prueba.
Finanzas reproduce
las tres sin diferen-
cias.
JP Meses 21 a 23.
8.3.4 Innovación 4: li-
quidación mensual
del tramo varia-
ble, meses 24 a 56
(INN-04.P3)
Las 33 liquidaciones
mensuales (meses
24 a 56) y el registro
de las recomenda-
ciones.
Finanzas reproduce
cada liquidación,
y cada recomen-
dación tiene su
respuesta registra-
da.
JP Mensual, desde
el mes 24.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
83


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 47 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
8.3.5 Innovación 5: des-
pliegue gradual por
rutas (INN-05.P4,
segunda parte)
Hoja disponible en
todas las rutas.
Al mes 27, la hoja
se muestra en al
menos el 90 % de
los locales que
la aceptan, y al
menos el 85 % de
las copias pedidas
se entrega dentro
de dos visitas.
SRE Meses 22 a 26.
8.3.6 Innovación 5: blo-
que 4 condicionado
(INN-05.P5)
Dictamen legal y,
si es favorable, el
bloque activado.
No se activa sin
dictamen legal favo-
rable y aprobación
de privacidad por
el Encargado de
Seguridad; todas
las emisiones cum-
plen el umbral de
agrupación.
SRE Meses 24 a 27.
Desde el mes 22, la responsabilidad de respuesta de los paquetes 8.3.2, 8.3.5 y 8.3.6 pasa al
frente de Operación, bajo el Líder de Operación / SRE, una vez que concluyen las dedicaciones
del Líder de Datos y del Líder de Implantación (SD1, Tabla 1.6). Esta transferencia no cambia
las familias de esfuerzo del T-15: DAT para 8.3.2 e IMP para 8.3.5 y 8.3.6. Cada paquete conserva
el período indicado en su fila.
2.8.4 Cuenta 8.4 — Informes y obligaciones periódicas
Esta cuenta de control reúne los informes y las tareas que las Bases fijan con una periodici-
dad durante la Operación y que no forman parte de los servicios diarios.
Cada propuesta trimestral de ajuste de dimensionamiento de 8.4.1 incluirá su efecto en
el costo de infraestructura, nube, licencias y enlaces respecto de la base contratada, para
decisión del CLIENTE antes de ejecutarla. La comparación empleará los consumos observados
y las condiciones económicas vigentes (BTT, cap. 9, RT-09.09, p. 22).
La Tabla 48 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
84


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 48 Diccionario de la cuenta 8.4. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
8.4.1 Gestión de la capaci-
dad con proyección
trimestral duran-
te los 36 meses de
operación
12 informes trimes-
trales de capacidad.
Cada trimestre hay
una proyección,
con alertas y una
propuesta de ajuste
cuando correspon-
de.
SRE Trimestral,
meses 21 a 56.
8.4.2 Informes mensua-
les de consumo de
nube (FinOps) du-
rante los 36 meses
de operación
36 informes men-
suales de consumo.
Cada informe des-
glosa el consumo, y
toda desviación so-
bre el presupuesto
tiene su alerta y su
explicación.
SRE Mensual, me-
ses 21 a 56.
8.4.3 Estimaciones anua-
les de la huella de
carbono de la opera-
ción
Tres informes anua-
les de huella de
carbono.
Cada informe decla-
ra su metodología y
compara con el año
anterior.
SRE Anual, meses
21 a 56.
8.4.4 Actualizaciones
semestrales del de-
pósito de custodia
de fuentes duran-
te los 36 meses de
operación
Seis actualizaciones
del depósito, con su
constancia.
Cada semestre el
depósito coincide
con la versión en
producción.
JP Semestral,
meses 21 a 56.
2.8.5 Cuenta 8.5 — Capacitación y transferencia en operación
Esta cuenta de control reúne la capacitación y el traspaso de conocimiento que las Bases
exigen después de la implementación.
El centro de soporte revisará los tickets y la retroalimentación de las personas usuarias
para identificar necesidades recurrentes y complejidades de la operación. Incorporará las
soluciones y lecciones validadas en la base de conocimiento de 8.5.3 y revisará trimestralmente
su uso y utilidad para ajustar los procedimientos de atención (BTT, cap. 21, RT-21.10, p. 36).
La Tabla 49 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
85


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 49 Diccionario de la cuenta 8.5. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
8.5.1 Dos jornadas anua-
les de actualización
y capacitación del
personal nuevo du-
rante los 36 meses
de operación
Seis jornadas de
actualización como
mínimo y registro
de la capacitación
del personal nuevo.
Cada año hay al me-
nos dos jornadas, y
cada persona nueva
está capacitada en
su perfil.
IMP Meses 21 a 56.
8.5.2 Mentoría al equipo
técnico del CLIEN-
TE durante los seis
meses posteriores
al mes 21
Plan de mentoría
y registro de las
sesiones.
La mentoría cubre
al menos seis me-
ses, y el equipo de
TI ejecuta solo sus
funciones al final
del período.
IMP Meses 21 a 27.
8.5.3 Mantenimiento de
la base de conoci-
miento durante los
36 meses de opera-
ción, con métricas
de uso
Base de conoci-
miento actualizada
e informe trimes-
tral de uso.
Cada incidente
resuelto con una
solución nueva
tiene su entrada, y
hay métricas de uso
y de utilidad cada
trimestre.
SRE Meses 21 a 56.
2.9 Fase 9. Cierre
La fase 9 reúne 2 cuentas de control y 4 paquetes de trabajo.
2.9.1 Cuenta 9.1 — Cierre de la implementación
Esta cuenta de control reúne lo que se entrega cuando termina la implementación.
La Tabla 50 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
86


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 50 Diccionario de la cuenta 9.1. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
9.1.1 Entrega del código
fuente, la infra-
estructura como
código y los pro-
cedimientos de
despliegue
Repositorios entre-
gados.
El equipo de TI de
Puelche reconstru-
ye y despliega una
versión en un am-
biente de prueba
siguiendo solo lo
entregado.
DES Mes 21 (H12).
9.1.2 Informe de leccio-
nes aprendidas y
archivo de la imple-
mentación
Informe de leccio-
nes aprendidas y
archivo.
El informe cubre
las dos etapas, y el
archivo contiene
todas las actas de
H1 a H12.
JP Después del
H12.
2.9.2 Cuenta 9.2 — Salida al término del contrato
Esta cuenta de control reúne el traspaso final y la eliminación de los datos personales.
La Tabla 51 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
87


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 51 Diccionario de la cuenta 9.2. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63);
(Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
9.2.1 Ejecución del Plan
de Reversibilidad y
acompañamiento
de 90 días
Acta de traspaso. El receptor opera
sin interrupción du-
rante los 90 días de
acompañamiento y
firma la recepción.
JP Meses 54 a 56:
el acompaña-
miento empie-
za al menos
90 días antes
del término
del contrato,
mientras La-
froX mantiene
la operación.
Si el CLIENTE
fija un término
anticipado o
una transición
posterior, el pe-
ríodo se ajusta
para conservar
los 90 días.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
88


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 51 — continuación
Código Paquete de trabajo Entregable Criterio de acepta-
ción
Resp. Período
9.2.2 Certificado de de-
volución o elimi-
nación de datos
personales
Certificado de de-
volución, transfe-
rencia de custodia y
eliminación.
Los datos se de-
vuelven íntegros
en formatos abier-
tos; las copias en
ambientes y respal-
dos de LafroX se
eliminan; los obje-
tos con retención
inmutable (Object
Lock, registro de
auditoría de siete
años) se transfie-
ren en custodia al
CLIENTE sin alte-
rar su retención, y
su eliminación se
certifica al vencer
cada retención. El
certificado identifi-
ca qué se eliminó,
qué se transfirió y
con qué fecha de
vencimiento.
SEG Al término
del contrato,
después de
9.2.1.
3 Carta Gantt
La carta Gantt muestra las ventanas de marcha blanca, los pasos a producción y el inicio
de la fase de Operación, como exige el Formulario T-14. Su estructura contractual la fija el
artículo 17 de las Bases Administrativas (pp. 12–13), y los hitos y sus meses, el Formulario
E-25. La Tabla 52 presenta esa estructura fija de los 56 meses, sobre la cual se programan los
paquetes de la sección 2.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
89


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 52 Períodos contractuales e hitos. Fuente: (Bases Administrativas, art. 17 y Formulario E-25, pp. 12–13,
74–75).
Período contractual Meses Hitos del período
Etapa 1 · Desarrollo 1 a 12 H1 (mes 2), H2 (mes 4), H3 (mes
6), H4 (mes 10), H5 (mes 12)
Etapa 1 · Marcha blanca 13 a 15 H6 (mes 13)
Etapa 1 · Producción Desde el 16 H7 (mes 16)
Etapa 2 · Desarrollo 13 a 18 H8 (mes 14), H9 (mes 17), H10
(mes 18)
Etapa 2 · Marcha blanca 19 y 20 H11 (mes 19)
Etapa 2 · Producción y acepta-
ción final
21 H12 (mes 21)
Operación 21 a 56 Hito mensual (36 pagos)
Se distingue el congelamiento total del 1 al 25 de septiembre, todo diciembre y los primeros
tres días hábiles del mes de la prohibición de paso a producción durante todo septiembre y
diciembre (Caso, secciones 13.2 y 13.3 y RT-10.05). La política de arquitectura también excluye
despliegues durante todo septiembre; su alcance se precisa en T-18, sección 1. Los trámites
documentales sin intervención no equivalen a despliegues. La correspondencia entre meses
contractuales y meses calendario depende de la fecha de inicio del contrato; se analiza en la
sección 7.3.2 del Subdocumento 7 y en su Anexo 7.A, que adoptan como supuesto un inicio en
febrero de 2027.
Las fechas de producción de la carta son objetivos condicionados a contar con actas de
cierre previas. La secuencia de evidencia, revisión y firma, y el conflicto si se necesita el
plazo completo de diez días, se explicitan en T-15, sección 5.5. H7/H12 son aceptaciones
posteriores a producción. La Figura 2 presenta la carta de los 56 meses del contrato, elaborada
en GanttProject: los períodos del artículo 17, las ventanas de marcha blanca, los pasos a
producción del 5 de mayo y del 5 de octubre de 2028 (cuarto día hábil de cada mes), el inicio de
la Operación, simultáneo con el paso a producción de la Etapa 2, y los hitos H1 a H12.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
90


---

LafroX
SpA
Formulario
T-14:
Plan
de
trabajo,
EDT
y
carta
Gantt
Figura 2 Carta Gantt de los 56 meses por período contractual, con inicio en febrero de 2027. Fuente: elaboración en GanttProject a partir de (Bases
Administrativas, art. 17, pp. 12–13 y Formulario E-25) y de las Figuras 3 a 9.
LafroX
SpA
Formulario
T-14
Media
firma:
Alex
Aravena
91


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Las Figuras 3 a 9 detallan, en siete partes, la implementación de las Etapas 1 y 2: 155 filas
ordenadas por fecha de inicio, desde febrero de 2027 hasta la estabilización de la Etapa 2, con
las dependencias entre paquetes visibles. Cada fila es un paquete con entregable, un grupo de
paquetes que comparten fechas («n elementos») o un hito del Formulario E-25, separado en
la entrega del expediente y el acta del CLIENTE. El prefijo RC marca los elementos de la ruta
crítica; PT/H, los demás paquetes y los hitos.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
92


---

LafroX
SpA
Formulario
T-14:
Plan
de
trabajo,
EDT
y
carta
Gantt
Figura 3 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 1 de 7 (filas 1 a 23 de 155), con inicio en febrero de 2027. Fuente: elaboración
en GanttProject a partir de la sección 2 de este formulario.
LafroX
SpA
Formulario
T-14
Media
firma:
Alex
Aravena
93


---

LafroX
SpA
Formulario
T-14:
Plan
de
trabajo,
EDT
y
carta
Gantt
Figura 4 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 2 de 7 (filas 24 a 45 de 155), con inicio en febrero de 2027. Fuente:
elaboración en GanttProject a partir de la sección 2 de este formulario.
LafroX
SpA
Formulario
T-14
Media
firma:
Alex
Aravena
94


---

LafroX
SpA
Formulario
T-14:
Plan
de
trabajo,
EDT
y
carta
Gantt
Figura 5 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 3 de 7 (filas 46 a 67 de 155), con inicio en febrero de 2027. Fuente:
elaboración en GanttProject a partir de la sección 2 de este formulario.
LafroX
SpA
Formulario
T-14
Media
firma:
Alex
Aravena
95


---

LafroX
SpA
Formulario
T-14:
Plan
de
trabajo,
EDT
y
carta
Gantt
Figura 6 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 4 de 7 (filas 68 a 89 de 155), con inicio en febrero de 2027. Fuente:
elaboración en GanttProject a partir de la sección 2 de este formulario.
LafroX
SpA
Formulario
T-14
Media
firma:
Alex
Aravena
96


---

LafroX
SpA
Formulario
T-14:
Plan
de
trabajo,
EDT
y
carta
Gantt
Figura 7 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 5 de 7 (filas 90 a 111 de 155), con inicio en febrero de 2027. Fuente:
elaboración en GanttProject a partir de la sección 2 de este formulario.
LafroX
SpA
Formulario
T-14
Media
firma:
Alex
Aravena
97


---

LafroX
SpA
Formulario
T-14:
Plan
de
trabajo,
EDT
y
carta
Gantt
Figura 8 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 6 de 7 (filas 112 a 133 de 155), con inicio en febrero de 2027. Fuente:
elaboración en GanttProject a partir de la sección 2 de este formulario.
LafroX
SpA
Formulario
T-14
Media
firma:
Alex
Aravena
98


---

LafroX
SpA
Formulario
T-14:
Plan
de
trabajo,
EDT
y
carta
Gantt
Figura 9 Carta Gantt resumida de las Etapas 1 y 2 con dependencias visibles, parte 7 de 7 (filas 134 a 155 de 155), con inicio en febrero de 2027. Fuente:
elaboración en GanttProject a partir de la sección 2 de este formulario.
LafroX
SpA
Formulario
T-14
Media
firma:
Alex
Aravena
99


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
La carta confirma que los períodos fijos del artículo 17 de las Bases Administrativas (pp.
12–13) se cumplen mes a mes y que ningún paso a producción cae en un período de con-
gelamiento. La sala técnica y el borde de los sitios se instalan entre los meses 3 y 5, la base
compartida y los módulos de la Etapa 1 se construyen entre los meses 4 y 8, y las pruebas de
integración y certificación de la Etapa 1 ocupan los meses 9 y 10, antes del H5 del mes 12. Las
cuentas de la Etapa 2 (3.5, 3.9, 4.3 y la segunda parte de 5.4) se ubican entre los meses 13 y
22, con los módulos en los meses 14 y 15 y la integración y certificación en los meses 16 y
17. Las cuentas de capacitación y de gestión del cambio se intensifican desde el mes 10, en
preparación de cada marcha blanca. Las fechas diarias de los paquetes con entregable están
en el Formulario T-15, sección 6.1, y la red con revisiones del CLIENTE y el cálculo de la ruta
crítica, en su sección 5.
La Figura 10 aísla los elementos de la ruta crítica y sus dependencias hasta los inicios de
las marchas blancas, H6 y H11, cuyas fechas son fijas.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
100


---

LafroX
SpA
Formulario
T-14:
Plan
de
trabajo,
EDT
y
carta
Gantt
Figura 10 Vista crítica de la carta Gantt: paquetes de la ruta crítica y sus dependencias hasta H6 y H11. Fuente: elaboración en GanttProject a partir de la
sección 2 de este formulario.
LafroX
SpA
Formulario
T-14
Media
firma:
Alex
Aravena
101


---

LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
4 Criterios vigentes de programación y recursos
Las ventanas mensuales de asignación y las HH por paquete están en el T-15, sección 4. La
preparación del H3 sigue esta secuencia: planos 2.3.1/2.3.2 en el mes 1, especificación y orden
de compra de LafroX 5.1.2 en el mes 2, instalación 6.1.1–6.1.4 en el mes 3 y recepción 6.1.5
en el mes 4. Los racks R01/R02 se montan en los meses 4 y 5, el gabinete de Concepción en
el mes 4 y el borde de los CD entra en servicio mediante 6.6.3 en el mes 5. Los gabinetes de
cross-docking se montan en el mes 9. El CLIENTE compra el equipamiento de terreno antes
de cada ola.
4.2.2 incorpora estabilización y soporte puente E1 en los meses 16–20, desde el paso a
producción previo a H7. La fase contractual de Operación comienza en el mes 21. 4.3.2 abarca
desde el paso a producción de la Etapa 2 hasta el cierre del mes 22, con cuatro semanas
reforzadas posteriores al H12, imputadas a los meses 21 y 22. El T-18, sección 6, declara la
dotación y la regla de decremento. 8.3.2 realiza la revisión INN-03.P5 cada seis meses: meses
26, 32, 38, 44, 50 y 56 del proyecto. El esfuerzo equivalente mensual del T-15 conserva esta
frecuencia. La coordinación de reserva y retención (SD4, apartado 4.1.4.4) y las pruebas AL-
STOCK-01/AL-ACT-01 se incorporan a los paquetes existentes conforme al T-18, sección 6.5.
AL-STOCK-01 mide la proporción de líneas con más de una retención y las pruebas de carga
3.8.4/3.9.3 verifican el drenaje.
## Referencias
Las fuentes citadas en este formulario se listan en formato APA 7.ª edición. Las Bases se
citan en el texto con su documento y el artículo, capítulo, sección o código del requisito.
• Distribuidora Puelche S.A. (2026a). Bases Administrativas, Licitación TFEP-01/2026.
• Distribuidora Puelche S.A. (2026b). Bases Técnicas Transversales, Licitación TFEP-01/2026.
• Distribuidora Puelche S.A. (2026c). Bases Técnicas del Caso Logística.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
102


---
