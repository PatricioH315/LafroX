# LafroX — Informe de revisión del T-12, lote B3

## 1. Tabla de cambios

| ID | Estado antes → después | Qué cambió y por qué (evidencia: archivo y sección) |
| --- | --- | --- |
| RT-13.01 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Pruebas de accesibilidad WCAG 2.2 AA en paquetes de aceptación. Falta: herramientas automatizadas, pruebas manuales y el informe de conformidad. Evidencia: LAFROX-Formulario-T-14 cuentas 3.8 y 3.9 (paquetes 3.8.2 y 3.9.2). |
| RT-13.02 | Cumple parcialmente → No cumple | Se ajusta: — (sin componente acreditado). Falta: diseño responsivo, puntos de quiebre y adaptación a escritorio, tableta y teléfono. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.3.1. |
| RT-13.03 | Cumple parcialmente → Cumple | Sube: Investigación por perfil, prototipos y pruebas con participantes del CLIENTE; hallazgos incorporados antes de construir. Evidencia: LAFROX-Formulario-T-14 cuenta 2.6 (paquetes 2.6.1 y 2.6.2). |
| RT-13.04 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Tiempos de transacción y aprendizaje de preparación. Falta: máximos de pasos, tasa de error y aprendizaje por perfil; umbrales a definir por el equipo. Evidencia: LAFROX-Subdocumento3-Anexos 3.B (Tabla 3.A.4); LAFROX-Formulario-T-14 cuenta 2.6 (paquete 2.6.3). |
| RT-13.05 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: máximo tres interacciones para cada función principal y perfil. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.3.1. |
| RT-13.06 | No cumple → Cumple parcialmente | Sube: Modo offline con escrituras pendientes no confirmadas. Falta: retroalimentación visual por acción y errores comprensibles. Evidencia: LAFROX-Subdocumento4 4.1.10; LAFROX-Subdocumento4 4.1.15. |
| RT-13.07 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Objetivos táctiles 15 × 15 mm y sin gestos complejos en picking. Falta: 44 × 44 píxeles, alto contraste, iconos con texto y flujos guiados. Evidencia: LAFROX-Subdocumento3-Anexos 3.B (Tabla 3.A.4). |
| RT-13.08 | Cumple → Cumple parcialmente | Baja: Zebra MC9400 Cold Storage Freezer para frío y guantes, Zebra EC55 legible al sol, Zebra TC58e con protección IP y operación offline. Falta: acreditar conjuntamente −22 °C, lluvia, más de 34 °C, una mano y sol directo. Evidencia: LAFROX-Subdocumento4 4.2.1.2; LAFROX-Subdocumento4 4.1.15; LAFROX-Formulario-T-11 (C-01, C-02 y C-03). |
| RT-13.09 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: sistema de diseño con paleta, tipografía, iconografía, retícula y componentes reutilizables. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.3.1. |
| RT-13.10 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: matriz de navegadores/versiones y política de actualización. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.7. |
| RT-13.11 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: navegación por teclado, foco lógico y atajos. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.3.1. |
| RT-13.12 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: alcance de modo oscuro, personalización e idiomas. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.3.1. |
| RT-14.01 | Cumple → Cumple | Se mantiene: OpenTelemetry para PHP/Laravel y Kotlin, AWS Distro for OpenTelemetry y CloudWatch correlacionados por transaction_id. Evidencia: LAFROX-Subdocumento4 4.1.3.8; LAFROX-Formulario-T-11 (F-01). |
| RT-14.02 | Cumple → Cumple parcialmente | Baja: Tableros operacionales y de negocio de solo lectura con filtros y exportación. Falta: actualización en tiempo real de todos los datos de negocio. Evidencia: LAFROX-Subdocumento4 4.1.3.8; LAFROX-Subdocumento5 5.2.6. |
| RT-14.03 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Disponibilidad por transacción de extremo a extremo. Falta: método de experiencia real y distinción frente a pruebas sintéticas. Evidencia: LAFROX-Subdocumento4 4.2.4.3; LAFROX-Subdocumento4 4.3.2.4. |
| RT-14.04 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Alertas por síntomas, ventanas y criticidad. Falta: supresión/agrupación de ruido, escalamiento automático y turnos. Evidencia: LAFROX-Subdocumento4 4.1.3.8. |
| RT-14.05 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Guías de resolución como artefacto de traspaso. Falta: guías por falla previsible y automatización progresiva. Evidencia: LAFROX-Subdocumento4-Anexos 4-B; LAFROX-Formulario-T-14 fase 8. |
| RT-14.06 | No cumple → Cumple parcialmente | Sube: Post-mortem P1/P2 y causa raíz con informe en cinco días hábiles. Falta: seguimiento de acciones correctivas hasta cierre. Evidencia: LAFROX-Subdocumento1 1.3.3; LAFROX-Subdocumento13 13.2.2. |
| RT-14.07 | No cumple → Cumple parcialmente | Sube: Acceso a registros controlado y auditado. Falta: filtrado de datos sensibles y credenciales en logs. Evidencia: LAFROX-Subdocumento4 4.1.3.7; LAFROX-Subdocumento4 4.1.3.8; LAFROX-Subdocumento4-Anexos 4-R. |
| RT-14.08 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Logs 12 meses en línea y 24 archivados, métricas 13 meses. Falta: retención de trazas y costo asociado; costos a definir por el equipo. Evidencia: LAFROX-Subdocumento4 4.1.3.8. |
| RT-14.09 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: análisis histórico de anomalías con aviso antes del impacto. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.3.8. |
| RT-15.01 | Cumple parcialmente → Cumple | Sube: Utilización por perfil/sitio, escalamiento Fargate y revisión trimestral de capacidad para evitar ociosidad. Evidencia: LAFROX-Subdocumento4 4.2.6.8; LAFROX-Subdocumento4 4.2.6.9; LAFROX-Subdocumento4 4.2.6.10. |
| RT-15.02 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Ambientes no productivos apagados/reducidos y experiencia logística/cadena de frío. Falta: evidencia específica de RSA y normativa DTE. Evidencia: LAFROX-Subdocumento4 4.2.3.4; LAFROX-Subdocumento1 1.4; LAFROX-Formulario-T-6 (Tabla 1). |
| RT-15.03 | No cumple → Cumple | Sube: Tres estimaciones anuales de huella operacional; cada informe incluye metodología y comparación interanual. Evidencia: LAFROX-Formulario-T-14 cuenta 8.4 (paquete 8.4.3). |
| RT-15.04 | Cumple parcialmente → Cumple parcialmente | Se mantiene: PUE estimado de Talca. Falta: intensidad de carbono de la región cloud elegida. Evidencia: LAFROX-Subdocumento4 4.3.1.4. |
| RT-15.05 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: comparación de carbono por región, latencia y regulación. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.2.3.2. |
| RT-15.06 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: metas de reducción de consumo, medición y reporte anual; línea base y meta a definir por el equipo. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Formulario-T-14 cuenta 8.4 (paquete 8.4.3). |
| RT-15.07 | Cumple parcialmente → Cumple parcialmente | Se mantiene: ISO 9001:2015, ISO/IEC 27001:2022, CMMI-DEV nivel 3 e ISO/IEC 20000-1:2018 declaradas. Falta: copias vigentes y códigos de verificación. Evidencia: LAFROX-Subdocumento1 1.3.1; LAFROX-Subdocumento1 1.3.2; LAFROX-Subdocumento1 1.4. |
| RT-15.08 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Equipo con personas, roles y dedicaciones. Falta: identificar personas certificadas asignadas y sus dedicaciones. Evidencia: LAFROX-Subdocumento1 1.5. |
| RT-15.09 | No cumple → Cumple parcialmente | Sube: Compromiso de mantener certificaciones corporativas. Falta: reposición de persona certificada saliente según Art. 76°. Evidencia: LAFROX-Subdocumento1 1.4; LAFROX-Subdocumento1 1.5. |
| RT-16.01 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Consola Angular 22 para usuarios/roles con Keycloak 26.x. Falta: permisos, unidades organizacionales y jerarquías por el CLIENTE. Evidencia: LAFROX-Subdocumento4 4.1.3.7; LAFROX-Subdocumento4-Anexos 4-N (Tabla A.16). |
| RT-16.02 | Cumple parcialmente → Cumple parcialmente | Se mantiene: mae_parametro/mae_parametro_version registra valor, vigencia y actores. Falta: catálogo completo de reglas en interfaz y registro explícito de qué/cuándo cambió. Evidencia: LAFROX-Subdocumento5-Anexos 5-A; LAFROX-Subdocumento4 4.1.4.2. |
| RT-16.03 | Cumple parcialmente → Cumple parcialmente | Se mantiene: mae_parametro_version registra quién cambia/aprueba. Falta: segundo perfil obligatorio y justificación. Evidencia: LAFROX-Subdocumento5-Anexos 5-A. |
| RT-16.04 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: inventario de elementos parametrizables y de los que requieren desarrollo. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.4.2. |
| RT-16.05 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: ambiente de simulación previo a producción. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.4.2. |
| RT-16.06 | Cumple → Cumple | Se mantiene: gob_auditoria registra actor/sistema, hora con zona, origen y valores anteriores/posteriores por operación. Evidencia: LAFROX-Subdocumento5 5.2.2; LAFROX-Subdocumento5-Anexos 5-A; LAFROX-Subdocumento4-Anexos 4-R. |
| RT-16.07 | Cumple → Cumple | Se mantiene: Auditoría inalterable bajo S3 Object Lock, protegida de modificación/eliminación por cualquier perfil. Evidencia: LAFROX-Subdocumento4 4.1.3.7; LAFROX-Subdocumento4 4.1.10; LAFROX-Subdocumento4-Anexos 4-R. |
| RT-16.08 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: interfaz de consulta/exportación y filtros de auditoría para CLIENTE. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.3.7. |
| RT-16.09 | Cumple → Cumple | Se mantiene: Registro de consultas a crédito, pagos y geolocalización, además de modificaciones. Evidencia: LAFROX-Subdocumento4 4.1.3.7; LAFROX-Subdocumento5 5.1.8; LAFROX-Subdocumento4-Anexos 4-C; LAFROX-Subdocumento4-Anexos 4-R. |
| RT-16.10 | Cumple → Cumple | Se mantiene: Auditoría y seguridad retenidas siete años bajo Object Lock. Evidencia: LAFROX-Subdocumento4 4.1.3.7; LAFROX-Subdocumento4 4.1.3.8. |
| RT-16.11 | No cumple → Cumple parcialmente | Sube: Flujos DTE/POD con estados, transiciones y responsables. Falta: plazos, escalamiento automático y delegación. Evidencia: LAFROX-Subdocumento4 4.1.17.1; LAFROX-Subdocumento4 4.1.17.2. |
| RT-16.12 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: configuración CLIENTE de responsables, plazos y aprobaciones sin desarrollo. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.17. |
| RT-16.13 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Bandejas EDI, DTE y sincronización por actor. Falta: bandeja unificada, priorización y alertas. Evidencia: LAFROX-Subdocumento4 4.1.3.5; LAFROX-Subdocumento4-Anexos 4-B. |
| RT-16.14 | Cumple parcialmente → Cumple parcialmente | Se mantiene: POD articulado con guía electrónica/acuse ERP para receptor natural. Falta: motor de reglas sin recompilación y trazabilidad de regla. Evidencia: LAFROX-Subdocumento4 4.1.17; LAFROX-Subdocumento4-Anexos 4-U. |
| RT-16.15 | No cumple → Cumple parcialmente | Sube: Documentos con metadatos, hash y acceso controlado. Falta: búsqueda por contenido/metadatos y previsualización. Evidencia: LAFROX-Subdocumento5 5.1.8; LAFROX-Subdocumento5-Anexos 5-A; LAFROX-Subdocumento4-Anexos 4-N (Tabla A.15). |
| RT-16.16 | Cumple parcialmente → Cumple | Sube: Objetos POD/DTE en Amazon S3 cifrados, con hash y retención por dominio según política del caso. Evidencia: LAFROX-Subdocumento4-Anexos 4-N (Tabla A.15); LAFROX-Subdocumento5 5.2.7; LAFROX-Subdocumento5-Anexos 5-E. |
| RT-16.17 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Evidencia de recepción de persona natural ligada a acuse ERP. Falta: firma avanzada aplicable y validación de certificado conforme Ley 19.799. Evidencia: LAFROX-Subdocumento4 4.1.17; LAFROX-Subdocumento4-Anexos 4-U. |
| RT-16.18 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: sello de tiempo y evidencia verificable tras vencer el certificado. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.17. |
| RT-16.19 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: documentos desde plantillas CLIENTE con datos y formato abierto. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento5 5.1.8. |
| RT-16.20 | Cumple → Cumple | Se mantiene: Trabajador Laravel 13 de notificaciones con Amazon SNS/API de canal; correo, SMS, WhatsApp y aviso en portal. Evidencia: LAFROX-Subdocumento4-Anexos 4-H (INT-11); LAFROX-Subdocumento4-Anexos 4-I (Tabla A.10); LAFROX-Subdocumento5-Anexos 5-A. |
| RT-16.21 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Plantillas versionadas y preferencia por cliente. Falta: administración CLIENTE y variables transaccionales. Evidencia: LAFROX-Subdocumento5-Anexos 5-A; LAFROX-Subdocumento4-Anexos 4-H (INT-11). |
| RT-16.22 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Preferencia por cliente/plantilla. Falta: preferencia por persona, frecuencia y reglas obligatorias. Evidencia: LAFROX-Subdocumento5-Anexos 5-A. |
| RT-16.23 | Cumple → Cumple parcialmente | Baja: Envío asíncrono, reintentos, idempotencia y resultado por intento. Falta: apertura de mensajes. Evidencia: LAFROX-Subdocumento4-Anexos 4-H (INT-11); LAFROX-Subdocumento5-Anexos 5-A. |
| RT-16.24 | No cumple → Cumple parcialmente | Sube: Volumen de INT-11: 2.800 mensajes diarios habituales y 5.200 en peak. Falta: proveedor y costo unitario por canal y tratamiento del costo variable en Oferta Económica; proveedor y costos a definir por el equipo. Evidencia: LAFROX-Subdocumento4-Anexos 4-H (INT-11); LAFROX-Subdocumento4-Anexos 4-I (Tabla A.10). |
| RT-16.25 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: reglas comerciales de comunicaciones y mecanismo de baja. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4-Anexos 4-H (INT-11). |
| RT-16.26 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: canal conversacional para responder/ejecutar acciones. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4-Anexos 4-H (INT-11). |
| RT-16.27 | No cumple → Cumple parcialmente | Sube: Búsqueda asistida por GTIN/lote para identificar productos. Falta: búsqueda global, texto completo, tolerancia a errores, facetas y permisos. Evidencia: LAFROX-Subdocumento5 5.1.7. |
| RT-16.28 | No cumple → Cumple parcialmente | Sube: Filtros y exportación analítica abierta. Falta: ordenamiento, paginación y filtro reflejado en exportación. Evidencia: LAFROX-Subdocumento5 5.2.6; LAFROX-Subdocumento5 5.2.8. |
| RT-16.29 | Cumple → Cumple parcialmente | Baja: Exportación asíncrona abierta con firma/checksum. Falta: aviso de fin y sesión no bloqueada. Evidencia: LAFROX-Subdocumento4-Anexos 4-C; LAFROX-Subdocumento5 5.2.8. |
| RT-16.30 | Cumple → Cumple | Se mantiene: Auditoría de exportaciones sensibles, catálogo público sin precios y portales autenticados para clientes, transportistas y proveedores. Evidencia: LAFROX-Subdocumento4 4.1.3.1; LAFROX-Subdocumento4-Anexos 4-C; LAFROX-Formulario-T-11 (N-01, N-02 y N-03). |
| RT-16.31 | Cumple → Cumple | Se mantiene: Catálogo público sin precios en S3/CloudFront; pruebas de accesibilidad y carga de portales. Evidencia: LAFROX-Subdocumento4 4.1.3.1; LAFROX-Subdocumento4 4.2.5.2; LAFROX-Formulario-T-14 cuentas 3.8 y 3.9 (paquetes 3.8.2, 3.8.4, 3.9.2 y 3.9.3); LAFROX-Formulario-T-11 (N-01). |
| RT-16.32 | Cumple → Cumple | Se mantiene: Portal de clientes para pedido, estado, documentos y saldo; portales transportista/proveedor. Evidencia: LAFROX-Subdocumento4 4.1.3.1; LAFROX-Formulario-T-11 (N-01, N-02 y N-03). |
| RT-16.33 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: estimación e indicador de reducción de atención asistida, con línea base y meta a definir por el equipo. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.3.1; LAFROX-Formulario-T-14 cuenta 8.1. |
| RT-16.34 | Cumple → Cumple | Se mantiene: Portales estáticos S3/CloudFront con caché, aislados de API y límite de tasa. Evidencia: LAFROX-Subdocumento4 4.1.3.2; LAFROX-Subdocumento4 4.2.3.5; LAFROX-Formulario-T-11 (N-01). |
| RT-17.01 | Cumple → Cumple | Se mantiene: Kotlin/Android con Room para preventa/reparto/bodega; PWA Angular 22 para autoatención cliente; todos offline. Evidencia: LAFROX-Subdocumento4 4.1.3.1; LAFROX-Subdocumento4 4.1.15; LAFROX-Formulario-T-11 (N-01). |
| RT-17.02 | Cumple → Cumple parcialmente | Baja: Kotlin nativo justificado por periféricos y offline. Falta: comparar costo de mantención entre alternativas; supuestos a definir por el equipo. Evidencia: LAFROX-Subdocumento4 4.1.7; LAFROX-Subdocumento4 4.1.13; LAFROX-Subdocumento4-Anexos 4-O (ADR-07). |
| RT-17.03 | Cumple parcialmente → Cumple parcialmente | Se mantiene: Matriz OS/SDK/periféricos por modelo y MDM bloquea versiones no soportadas. Falta: declarar vigente, dos anteriores y política. Evidencia: LAFROX-Subdocumento4-Anexos 4-P (Tabla A.19). |
| RT-17.04 | Cumple → Cumple parcialmente | Baja: Distribución Android Enterprise/Zebra DNA e imagen firmada. Falta: firma/integridad verificable del paquete de aplicación. Evidencia: LAFROX-Formulario-T-11 (N-13); LAFROX-Subdocumento4 4.1.7; LAFROX-Subdocumento4-Anexos 4-P (Tabla A.19). |
| RT-17.05 | Cumple → Cumple | Se mantiene: Cola Room/SQLite cifrada, bloqueo/borrado remoto mediante MDM. Evidencia: LAFROX-Subdocumento4-Anexos 4-N (DAT-LOCAL); LAFROX-Formulario-T-11 (N-13); LAFROX-Subdocumento4-Anexos 4-P (Tabla A.19). |
| RT-17.06 | Cumple → Cumple | Se mantiene: Lectores SE4100, SE55 y SE58 integrados en los terminales Zebra EC55, TC58e y MC9400; impresora Zebra ZQ620 Plus; terminal PAX A920 Pro; balanza Dibal BEV con plataforma ME e indicador DMI-610; sensor Ebyte ME31-XDXX0400 y termógrafo Onset InTemp CX450; GPS y captura fotográfica y de firma. Evidencia: LAFROX-Formulario-T-11 (C-01, C-02, C-03, impresora de cabina, terminal de pago, C-05, B-01 y B-03); LAFROX-Subdocumento4 4.2.1.1. |
| RT-17.07 | No cumple → Cumple parcialmente | Sube: Consumo de datos dimensionado en 9,83 MB por turno y sincronización de flota. Falta: optimización de batería y consumo estimado por turno; valor a definir por el equipo. Evidencia: LAFROX-Subdocumento4 4.2.6.7. |
| RT-17.08 | No cumple → No cumple | Se mantiene: — (sin componente acreditado). Falta: interfaz para equipos de bajo costo o generaciones anteriores. Evidencia: no se halló desarrollo acreditable; secciones revisadas/destino: LAFROX-Subdocumento4 4.1.3.1. |

## 2. Componentes sin versión en la propuesta

Las líneas base «estable», «actual» o «compatible» no se convierten en versiones numéricas.

| Producto o componente | Filas afectadas | Sección existente para declarar versión o línea base precisa |
| --- | --- | --- |
| OpenTelemetry y AWS Distro for OpenTelemetry | RT-14.01 | SD4 §4.1.7; SD4-Anexos, Anexo 4-P, Tabla A.19 |
| Amazon CloudWatch y Amazon QuickSight | RT-14.01, RT-14.02 | SD4 §4.1.7; SD4-Anexos, Anexo 4-P, Tabla A.19 |
| AWS Fargate | RT-15.01 | SD4 §4.1.7; SD4-Anexos, Anexo 4-P, Tabla A.19 |
| S3 Object Lock y Amazon S3 | RT-16.07, RT-16.16, RT-16.31, RT-16.34 | SD4 §4.1.7; SD4-Anexos, Anexo 4-P, Tabla A.19 |
| Amazon SNS/API de canal | RT-16.20 | SD4-Anexos, Anexos 4-H (INT-11) y 4-P, Tabla A.19 |
| Kotlin/Android | RT-17.01, RT-17.02 | SD4 §4.1.7; SD4-Anexos, Anexo 4-P, Tabla A.19 |
| Android Enterprise/Zebra DNA | RT-17.04 | SD4-Anexos, Anexo 4-P, Tabla A.19; T-11 N-13 |
| Room/SQLite | RT-17.01, RT-17.05 | SD4 §4.1.7; SD4-Anexos, Anexo 4-P, Tabla A.19 |
| MDM | RT-17.03, RT-17.04, RT-17.05 | SD4-Anexos, Anexo 4-P, Tabla A.19; T-11 N-13 |
| CloudFront | RT-16.31, RT-16.34 | SD4 §4.1.7; SD4-Anexos, Anexo 4-P, Tabla A.19 |

Angular 22, Laravel 13, PHP 8.5 y Keycloak 26.x sí tienen versión declarada. La Tabla A.19 usa líneas estables/compatibles para algunas tecnologías, sin número.

## 3. Declaraciones faltantes

Cada destino corresponde a una sección existente. El borrador formula la carencia explícita; las cifras no disponibles quedan para definición del equipo.

- **RT-13.01 — T-14 cuentas 3.8 y 3.9 (paquetes 3.8.2 y 3.9.2)**: «La propuesta incorporará herramientas automatizadas, pruebas manuales y el informe de conformidad.»
- **RT-13.02 — SD4 4.1.3.1**: «La interfaz se adaptará a escritorio, tableta y teléfono con puntos de quiebre declarados y reorganización del contenido.»
- **RT-13.04 — SD3-Anexos 3.B (Tabla 3.A.4); T-14 cuenta 2.6 (paquete 2.6.3)**: «La propuesta incorporará máximos de pasos, tasa de error y aprendizaje por perfil; umbrales a definir por el equipo.»
- **RT-13.05 — SD4 4.1.3.1**: «Las funciones principales de cada perfil se completarán en no más de tres interacciones desde su pantalla de inicio.»
- **RT-13.06 — SD4 4.1.10; SD4 4.1.15**: «La propuesta incorporará retroalimentación visual por acción y errores comprensibles.»
- **RT-13.07 — SD3-Anexos 3.B (Tabla 3.A.4)**: «Las interfaces de terreno incorporarán objetivos táctiles de 44 × 44 píxeles, alto contraste, iconos acompañados de texto y flujos guiados.»
- **RT-13.08 — SD4 4.2.1.2; SD4 4.1.15; T-11 (C-01, C-02 y C-03)**: «La matriz de dispositivos precisará qué equipos cubren −22 °C, lluvia, más de 34 °C, uso a una mano, sol directo y operación desconectada durante el turno. El equipo definirá cualquier modelo faltante.»
- **RT-13.09 — SD4 4.1.3.1**: «Se documentará el sistema de diseño con paleta acotada, hasta dos familias tipográficas, iconografía coherente, retícula y componentes reutilizables.»
- **RT-13.10 — SD4 4.1.7**: «La propuesta declarará la matriz de navegadores y versiones soportadas y su política de actualización.»
- **RT-13.11 — SD4 4.1.3.1**: «Las interfaces permitirán completar todas las tareas por teclado, con foco lógico y atajos para las operaciones frecuentes.»
- **RT-13.12 — SD4 4.1.3.1**: «La propuesta declarará el alcance de modo oscuro, personalización por persona e idiomas adicionales.»
- **RT-14.02 — SD4 4.1.3.8; SD5 5.2.6**: «El CLIENTE tendrá acceso permanente a tableros exportables y con actualización en tiempo real para los datos de negocio requeridos. El equipo definirá el intervalo de actualización comprometido.»
- **RT-14.03 — SD4 4.2.4.3; SD4 4.3.2.4**: «Los indicadores se calcularán sobre eventos de uso real con método y ventana declarados; las pruebas sintéticas se reportarán por separado.»
- **RT-14.04 — SD4 4.1.3.8**: «Las alertas agruparán eventos relacionados, suprimirán duplicados y escalarán automáticamente; se declararán responsables y turnos.»
- **RT-14.05 — SD4-Anexos 4-B; T-14 fase 8**: «Se entregará un procedimiento operativo y una guía de resolución por cada falla previsible, indicando las tareas automatizadas y las que seguirán manuales.»
- **RT-14.06 — SD1 1.3.3; SD13 13.2.2**: «Las acciones correctivas de cada incidente crítico quedarán asignadas y se seguirán hasta verificar su cierre.»
- **RT-14.07 — SD4 4.1.3.7; SD4 4.1.3.8; SD4-Anexos 4-R**: «Los registros técnicos filtrarán credenciales y datos personales sensibles antes de persistirlos; el acceso seguirá controlado y auditado.»
- **RT-14.08 — SD4 4.1.3.8**: «La política declarará retención en línea y archivada de métricas, logs y trazas, junto con sus costos. Los costos se definirán por el equipo.»
- **RT-14.09 — SD4 4.1.3.8**: «La observabilidad comparará el comportamiento actual con históricos y alertará anomalías antes de su impacto.»
- **RT-15.02 — SD4 4.2.3.4; SD1 1.4; T-6 (Tabla 1)**: «Se incorporará evidencia específica de conocimiento RSA y normativa DTE, junto con la experiencia logística acreditada.»
- **RT-15.04 — SD4 4.3.1.4**: «La propuesta declarará la intensidad de carbono de la región de nube escogida y su fuente, además del PUE del recinto.»
- **RT-15.05 — SD4 4.2.3.2**: «La selección de región comparará intensidad de carbono, latencia y restricciones regulatorias.»
- **RT-15.06 — T-14 cuenta 8.4 (paquete 8.4.3)**: «Se definirá y reportará anualmente una meta de reducción de consumo frente a una línea base. La línea base y la meta quedan por definir por el equipo.»
- **RT-15.07 — SD1 1.3.1; SD1 1.3.2; SD1 1.4**: «Se adjuntará copia vigente de cada certificado y el código verificable del emisor cuando exista.»
- **RT-15.08 — SD1 1.5**: «La nómina del proyecto identificará a cada persona certificada asignada y declarará su dedicación.»
- **RT-15.09 — SD1 1.4; SD1 1.5**: «Las certificaciones se mantendrán vigentes durante el contrato y la salida de una persona certificada activará su reemplazo conforme al Artículo 76°.»
- **RT-16.01 — SD4 4.1.3.7; SD4-Anexos 4-N (Tabla A.16)**: «La consola permitirá al CLIENTE administrar permisos, unidades organizacionales y jerarquías además de personas usuarias y roles.»
- **RT-16.02 — SD5-Anexos 5-A; SD4 4.1.4.2**: «Se enumerarán las reglas parametrizables y su edición versionada desde la interfaz, registrando actor, valor anterior y nuevo e instante.»
- **RT-16.03 — SD5-Anexos 5-A**: «Cada cambio operacional requerirá aprobación de un segundo perfil y conservará su justificación, actores, valores e instante.»
- **RT-16.04 — SD4 4.1.4.2**: «La propuesta distinguirá expresamente los elementos parametrizables de los que requieren desarrollo.»
- **RT-16.05 — SD4 4.1.4.2**: «Un ambiente aislado permitirá simular cambios de parámetros antes de aplicarlos en producción.»
- **RT-16.08 — SD4 4.1.3.7**: «El CLIENTE consultará y exportará auditoría desde una interfaz con filtros por persona, período, entidad y tipo de operación.»
- **RT-16.11 — SD4 4.1.17.1; SD4 4.1.17.2**: «Cada flujo declarará estados, transiciones, responsables y plazos, con escalamiento automático y delegación por ausencia.»
- **RT-16.12 — SD4 4.1.17**: «El CLIENTE configurará responsables, plazos y niveles de aprobación de los flujos sin desarrollo.»
- **RT-16.13 — SD4 4.1.3.5; SD4-Anexos 4-B**: «Una bandeja unificada mostrará solicitudes pendientes por responsable con priorización y alertas de vencimiento.»
- **RT-16.14 — SD4 4.1.17; SD4-Anexos 4-U**: «El diseño explicará la recepción del destinatario persona natural y conservará la regla aplicada; las reglas configurables no requerirán recompilación.»
- **RT-16.15 — SD5 5.1.8; SD5-Anexos 5-A; SD4-Anexos 4-N (Tabla A.15)**: «Los documentos permitirán búsqueda por contenido y metadatos y previsualización sin descarga, respetando permisos.»
- **RT-16.17 — SD4 4.1.17; SD4-Anexos 4-U**: «Se definirán los actos que requieren firma avanzada y se verificará la validez del certificado al firmar, junto con el mecanismo aplicable al receptor habitual persona natural.»
- **RT-16.18 — SD4 4.1.17**: «Se conservarán sello de tiempo y evidencia para verificar la firma después del vencimiento del certificado.»
- **RT-16.19 — SD5 5.1.8**: «El CLIENTE generará documentos desde plantillas administrables con datos transaccionales y salida en formato abierto.»
- **RT-16.21 — SD5-Anexos 5-A; SD4-Anexos 4-H (INT-11)**: «El CLIENTE administrará plantillas versionadas con variables de transacción y selección de canal por cliente.»
- **RT-16.22 — SD5-Anexos 5-A**: «Cada persona podrá configurar canal y frecuencia, respetando las notificaciones obligatorias definidas por el CLIENTE.»
- **RT-16.23 — SD4-Anexos 4-H (INT-11); SD5-Anexos 5-A**: «Cada intento registrará entrega, apertura o error, manteniendo reintentos e idempotencia.»
- **RT-16.24 — SD4-Anexos 4-H (INT-11); SD4-Anexos 4-I (Tabla A.10)**: «Se declarará el proveedor y costo unitario por canal y volumen esperado; la Oferta Económica expondrá el costo variable. Proveedores y costos unitarios quedan por definir por el equipo.»
- **RT-16.25 — SD4-Anexos 4-H (INT-11)**: «Las notificaciones cumplirán las reglas de comunicaciones comerciales y ofrecerán baja cuando corresponda.»
- **RT-16.26 — SD4-Anexos 4-H (INT-11)**: «Se propondrá un canal conversacional para responder mensajes y ejecutar acciones desde el propio canal.»
- **RT-16.27 — SD5 5.1.7**: «La búsqueda global indexará texto completo, tolerará errores de escritura, ofrecerá filtros facetados y respetará los permisos de quien consulta.»
- **RT-16.28 — SD5 5.2.6; SD5 5.2.8**: «Los listados se podrán ordenar, filtrar, paginar y exportar; cada exportación conservará el filtro aplicado.»
- **RT-16.29 — SD4-Anexos 4-C; SD5 5.2.8**: «Las exportaciones extensas se ejecutarán en segundo plano, avisarán al completarse y permitirán continuar usando la sesión.»
- **RT-16.33 — SD4 4.1.3.1; T-14 cuenta 8.1**: «Se fijará un indicador de reducción de atención asistida con línea base y meta. Los valores quedan por definir por el equipo.»
- **RT-17.02 — SD4 4.1.7; SD4 4.1.13; SD4-Anexos 4-O (ADR-07)**: «La justificación de Kotlin nativo comparará el costo de mantención frente a las alternativas. El equipo definirá los supuestos de costo.»
- **RT-17.03 — SD4-Anexos 4-P (Tabla A.19)**: «La matriz declarará Android vigente y las dos versiones anteriores por modelo, junto con la política de actualización.»
- **RT-17.04 — T-11 (N-13); SD4 4.1.7; SD4-Anexos 4-P (Tabla A.19)**: «La distribución gestionada instalará el paquete firmado y comprobará su integridad antes de actualizar.»
- **RT-17.07 — SD4 4.2.6.7**: «Se optimizará el consumo de datos y batería y se declarará el consumo de batería por turno. El valor queda por definir por el equipo.»
- **RT-17.08 — SD4 4.1.3.1**: «La propuesta declarará una interfaz para equipos de bajo costo o generaciones anteriores, con su alcance funcional.»

## 4. Incoherencias detectadas en otros documentos

- **Dotación NOC/SOC.** Fuera del lote, RT-11.17 y RT-21.01 atribuyen «8 a 10 personas» a un puesto. SD4-Anexos §4-W.7 establece ocho personas totales para una posición NOC y otra SOC (cuatro por puesto), y diez totales desde 26-04-2028 (cinco por puesto). No se modificaron esas filas.
- **Frío de C-02.** T-11 C-02 declara −20 a +50 °C frente a −22 °C exigidos por Caso 02 cap. 15. C-03 Cold Storage cubre −30 °C, pero no se aclara si sustituye a C-02.
- **Canales de notificación.** SD4-Anexos 4-H INT-11 ofrece correo, SMS, WhatsApp y aviso en portal. SD5-Anexos 5-A usa CORREO/SMS/WHATSAPP/AVISO_EN_PORTAAL en not_plantilla y EMAIL/SMS/PUSH en not_intento; hay errata y catálogos incompatibles.
- **Aperturas.** RT-16.23 queda parcial por falta de evento de apertura; RF-18.03 fuera del lote permanece Cumple con alcance equivalente y debe revisarse.
- **Exportaciones.** RT-16.29 queda parcial por falta de aviso final y sesión no bloqueada; RNF-17.02 fuera del lote permanece Cumple con alcance equivalente y debe revisarse.
- **Flujos y búsqueda.** RT-16.11 acredita estados/transiciones, mientras RF-17.06 añade configuración por CLIENTE y permanece No cumple. RT-16.27 solo acredita búsqueda por lote/GTIN; RF-17.11 exige alcance global y sigue No cumple.
- **Documentos.** RT-16.16 cumple cifrado, hash y retención; RF-17.08 permanece No cumple por búsqueda, previsualización y gestión documental más amplia.
- **Logs.** RT-14.07 queda parcial por acceso controlado sin sanitización; RNF-16.03 sigue No cumple al exigir exclusión de datos sensibles y credenciales.
- **Notificaciones.** RT-16.20 cumple canales, RT-16.21 queda parcial por administración de plantillas, y RF-17.10 también permanece parcial.
- **Utilización.** RT-15.01 se marca Cumple por utilización proyectada, elasticidad y revisión trimestral en SD4 §§4.2.6.8–4.2.6.10; mantener consistencia con las tablas de infraestructura.
