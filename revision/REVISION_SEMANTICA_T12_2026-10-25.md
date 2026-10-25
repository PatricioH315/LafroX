# Revisión semántica completa del T-12 — 25-10-2026

Se leyeron las **653 filas**: 185 RF, 94 RNF y 374 RT. Las 279 filas de la Parte A representan 270 requerimientos y nueve alias; los alias no se contaron como obligaciones nuevas. Se compararon exigencia, respuesta, responsable, alcance, umbral, excepción, paquete EDT y referencias de la propuesta. También se contrastó el inventario de 98 filas del T-11.

## Resultado

- **595 Cumple, 36 Cumple parcialmente y 22 No cumple.** Son estados documentales de la propuesta, conforme a la introducción del formulario; no resultados de pruebas ejecutadas.
- **62 filas corregidas**, incluidas precisiones de respuesta/trazabilidad y una corrección de puntuación. **27 filas cambiaron de estado** para reconocer cobertura incompleta o evidencia ausente.
- Se conservó literalmente la descripción de las 653 exigencias del T-12. No se eliminaron obligaciones, filas ni alias. Los códigos EDT de todas las respuestas existen en el T-14 vigente y cada fila conserva una observación individual.
- El diccionario SD5 se contó desde sus filas: **121 entidades y 995 atributos**. Se corrigieron tres menciones de 987; no se alteraron entidades ni atributos.
- La fracción de deuda técnica se recalculó sobre las **128.853,67 HH de Operación** de T-15: 2.304 / 128.853,67 × 100 = **1,7881 %**.

## Correcciones de significado

M2 aporta inventario y M5 ejecuta picking; el cierre y la liquidación pertenecen a M7, mientras M10 consulta y calcula indicadores. La respuesta del cierre de misión ahora identifica SKU, cantidad preparada, lote e ID de pedido enviados al ERP. La rendición del preventista no requiere camión ni entrega y sí recibo provisional y cierre diario. La devolución retenida exige disposición de Calidad; un aviso de merma en góndola no descuenta por segunda vez la bodega.

Se corrigieron las precondiciones del alta de conductores: una persona nueva necesita conexión; sin señal actúa un suplente ya enrolado con asignación firmada y PIN. La recuperación de contraseña especifica enlace de un solo uso y hasta 15 minutos. Los indicadores actuales usan las API autorizadas y la analítica histórica queda aislada. El registro ADR vigente llega a ADR-24. La sincronización del terminal de diez minutos se verifica por su protocolo, separado del CD de dos horas.

En RF-01.07, el resultado esperado del catálogo confundía AI 11 con recepción. **GS1 define AI 11 como fecha de producción** y AI 00 como SSCC. La recepción se conserva como dato interno y texto legible, sin reutilizar AI 11. Fuente primaria: [GS1 Application Identifiers](https://ref.gs1.org/ai/).

## Brechas reconocidas

Estas brechas permanecen expresas en el T-12; no se construyeron funcionalidades ni acreditaciones para ocultarlas:

- RF-03.09: «superar el límite en más de 110 %» no fija inequívocamente si la base es 1,10 o 2,10 veces el cupo; Finanzas debe validar la fórmula.
- RF-15.03 / RT-12.03: la política de segundo factor no está desarrollada uniformemente para todas las entradas externas, más allá de administradores/consolas y el PIN del terminal enrolado.
- RNF-14.01 / RT-11.08: admitir TLS 1.2 en un legado no satisface una exigencia literal TLS 1.3 para todos los enlaces.
- RT-11.07: el acceso AS2 por NLB no acredita la misma cobertura de CDN/WAF/protección L7 declarada para toda publicación.
- RT-11.04: la excepción de remediación durante congelamientos puede exceder 7/15/30 días. RNF-14.06: el calendario del proyecto no concreta la práctica propia semestral de intrusión.
- RF-17.09: HTML y el guardado PDF del navegador no acreditan un generador integrado PDF/DOCX/XLSX. RF-18.03 / RT-16.23: NO_SOPORTADA para apertura de SMS es una limitación real, no una apertura medida.
- RNF-23.01/.02 / RT-08.10/.12: el kit conserva accesorios con especificación funcional y prestaciones que requieren ficha, modelo o prueba. RT-03.18 / RT-08.14: inventario/mantenimiento no acreditan bloqueo, borrado y actualización remotos en todas las familias de sensores/registradores.
- RT-22.08: 3.11.2 comienza en H4 y 8.5.3 cubre Operación; no está desarrollado todo el intervalo desde el inicio del contrato.
- RT-26.01: SD13 conserva la arquitectura térmica anterior y no está conciliado con el kit B-04–B-15 y los dos caminos vigentes de SD4.

Las restantes brechas previas se conservan: linaje automatizado, doble acometida, disparo regional automático, huella/intensidad de carbono, acreditaciones, nominación operativa completa, espacio de experiencias, video y prototipo, entre otras. Todas aparecen individualizadas en la tabla y en el CSV/JSON.

## Evidencia institucional

Se recuperaron por HTTPS con respuesta 200 el [sitio institucional](https://lafrox.github.io/) y su JavaScript el 25-10-2026. Se verificó que el script no construyera los elementos ausentes del HTML. Las copias y sus SHA-256 están en `semantica_t12_2026-10-25/evidencia_web` y `fuentes.json`.

La página publica historia, capacidades y casos, pero no los testimonios declarados en la matriz ni el centro de recursos, recorrido virtual, calculadora y tablero de métricas en vivo. RT-23.01/.02/.04/.05 quedan parciales por evidencia incompleta; RT-23.07–23.10 quedan «No cumple». Un certificado mencionado en la página o en la bibliografía no se equiparó a una copia validada; no se llamó a contrapartes ni se contactó a terceros.

## Condiciones que no deben perderse

La frecuencia, los plazos y las capacidades de la propuesta son compromisos que se aceptarán con pruebas; esta revisión no las ejecuta. El registro de apertura no se inventa cuando el canal no lo informa. Una fotografía/QR de entrega no se presenta automáticamente como acuse tributario. RTO/RPO se leen con los escenarios y el residual declarados. La posición de flota procede de los 42 camiones propios; no se interpretó como GPS continuo disponible para todos los transportistas. Los nuevos formatos/transportes EDI requieren distinguir configuración de un mapeo soportado frente a desarrollo de un adaptador.

En T-11 se revisaron 98 recursos. La base de 28 kits supone un compartimento y una puerta por vehículo; mapeo y levantamiento deben confirmar esa base y ajustar cantidades si hay más zonas/puertas. Quedan por precisar la especificación de las ocho PC nuevas y el inventario de entrada SBD respecto de las 13 colas de aplicaciones. El registro T-11 identifica esas condiciones sin inventar modelos, cantidades o resultados de ensayos.

## Trazabilidad y alcance de la comprobación

El CSV/JSON conserva la exigencia completa, respuesta final, estado anterior/final, observación individual, hallazgo, paquetes con nombre, fuente de la obligación con archivo/línea y secciones de respaldo declaradas. Se leyeron las respuestas; los scripts verifican cardinalidad, conservación de exigencias, referencias e integridad y serializan los dictámenes. Una coincidencia de palabras o un código existente no se utilizó como decisión automática de cumplimiento.

Las ramas SD1, SD8, SD9 y SD13 se consultaron como fuentes; no se editaron. SD10–SD12 conservan árboles de plantilla en las referencias remotas consultadas y no se usaron como acreditación de planes completos. Los compromisos operacionales se contrastaron con SD3/SD4 y los entregables/criterios concretos del T-14. Se corrigieron SD3, T-11 de SD4 y los totales textuales de SD5. No se alteraron figuras, modelos de datos, formulación económica ni ramas excluidas. `fuentes.json` conserva las revisiones Git consultadas.

Esta es una revisión documental asistida de todas las filas, **no una aceptación del CLIENTE, una revisión humana registrada ni una certificación de cumplimiento contractual o legal**. Los dictámenes «Cumple» no convierten entregables futuros en pruebas ya realizadas; las ausencias que deben acreditarse en la oferta se mantienen como brechas.

## Registro individual de las 653 filas

Archivos completos: [CSV](semantica_t12_2026-10-25/matriz_revision.csv), [JSON](semantica_t12_2026-10-25/matriz_revision.json), [fuentes y método](semantica_t12_2026-10-25/fuentes.json).

| ID | Estado final | Resultado de la lectura semántica |
| --- | --- | --- |
| RF-01.01 | Cumple | Comparación de OC sin bloquear cierre |
| RF-01.02 | Cumple | Lote obligatorio y bloqueo de avance |
| RF-01.03 | Cumple | Vencimiento vinculado a lote y ubicación |
| RF-01.04 | Cumple | Lista de no conformidad y fotografía obligatoria |
| RF-01.05 | Cumple | Cuarentena por cantidad y aviso a Calidad |
| RF-01.06 | Cumple | AI GS1 y contingencia manual auditada |
| RF-01.07 | Cumple | SSCC y fecha de recepción diferenciada de producción |
| RF-01.08 | Cumple | Doble escaneo y compatibilidad de ubicación |
| RF-01.09 | Cumple | Recepción al ERP con cola y reintento |
| RF-01.10 | Cumple | Ficha completa, obligatorios y validación |
| RF-01.11 | Cumple | Putaway rechaza incompatibilidad térmica |
| RF-02.01 | Cumple | Topología y copia offline con zona obligatoria |
| RF-02.02 | Cumple | Consolidación distingue sitio de origen |
| RF-02.03 | Cumple | Slotting propuesto requiere aprobación de Bodega |
| RF-02.04 | Cumple | Conteo ciego mensual y diferencias tipificadas |
| RF-02.05 | Cumple | Disponible excluye bloqueados y reserva firme; copia fechada |
| RF-02.06 | Cumple | Tránsito delimitado por carga y recepción, con integración ERP |
| RF-02.07 | Cumple | Ocupación cuenta posiciones, no unidades ni lotes |
| RF-02.08 | Cumple | M2 aporta stock y M5 ejecuta la preparación |
| RF-02.09 | Cumple | FEFO por vencimiento y alerta configurable |
| RF-02.10 | Cumple | Ciclo de lote debe incluir estados, ubicaciones y excepciones |
| RF-02.11 | Cumple | Lecturas y excepciones en ambos extremos del cross-docking |
| RF-03.01 | Cumple | Consulta conectada por SKU |
| RF-03.02 | Cumple | Copia sin señal con antigüedad visible |
| RF-03.03 | Cumple | Reserva por recepción central y acuse local, sin ERP |
| RF-03.04 | Cumple | Crédito y mora conectados |
| RF-03.05 | Cumple | Crédito y mora de copia fechada |
| RF-03.06 | Cumple | Historial con productos y frecuencia |
| RF-03.07 | Cumple | Promoción vigente calculada por línea |
| RF-03.08 | Cumple | Alerta de exceso antes de enviar |
| RF-03.09 | Cumple parcialmente | Umbral 110 % ambiguo respecto de la base de comparación |
| RF-03.10 | Cumple | Excepción del supervisor auditada |
| RF-03.11 | Cumple | Precio pactado no cambia con la lista posterior |
| RF-03.12 | Cumple | Diferencia ERP bloquea facturación y avisa a Comercial |
| RF-03.13 | Cumple | Promesa incluye stock, capacidad y franja |
| RF-03.14 | Cumple | Sugerencias por historial y promociones |
| RF-03.15 | Cumple | UUID se origina en el dispositivo |
| RF-03.16 | Cumple | Reenvíos del mismo UUID no crean otro pedido |
| RF-04.01 | Cumple | Ruteo con peso, volumen y zona |
| RF-04.02 | Cumple | Planificador reasigna y recalcula |
| RF-04.03 | Cumple | Exceso de peso o volumen bloquea cierre |
| RF-04.04 | Cumple | Secuencia considera ventana del cliente |
| RF-04.05 | Cumple | Frío no se asigna a camión seco |
| RF-04.06 | Cumple | ETA y ventana de 30 min por canal INT-11 |
| RF-04.07 | Cumple | Franja de cliente versionada |
| RF-04.08 | Cumple | M4 aporta datos; M10 calcula costo desde E2 |
| RF-05.01 | Cumple | Misiones manuales o programadas por pedido/ruta |
| RF-05.02 | Cumple | GS1 confirma SKU y lote, contingencia auditada |
| RF-05.03 | Cumple | Faltante exige causa antes de confirmar |
| RF-05.04 | Cumple | Secuencia seco, refrigerado, congelado |
| RF-05.05 | Cumple | FEFO entre lotes habilitados; excepción con causa |
| RF-05.06 | Cumple | Cierre de misión transmite líneas y pedido al ERP |
| RF-05.07 | Cumple | Carga inversa de ruta y control de SSCC faltante |
| RF-06.01 | Cumple | Confirmación por línea o guía completa |
| RF-06.02 | Cumple | Firma capturada es evidencia POD, no acuse tributario automático |
| RF-06.03 | Cumple | Rechazo registra cantidades y causa |
| RF-06.04 | Cumple | Local cerrado conserva intento y dirección |
| RF-06.05 | Cumple | Efectivo exacto asociado a entrega |
| RF-06.06 | Cumple | Llegada y fin son instantes separados |
| RF-06.07 | Cumple | Sincronización termina en acuse y alimenta cierre |
| RF-06.08 | Cumple | Alta conectada, autoridad de identidad y suplentes enrolados |
| RF-06.09 | Cumple | Cantidad, tipo y estado de envase retornado |
| RF-06.10 | Cumple | Saldos por cliente/parque con sincronización diferida |
| RF-06.11 | Cumple | QR único generado por conductor, confirmación opcional |
| RF-06.12 | Cumple | Firma/foto offline conserva vínculo documental |
| RF-06.13 | Cumple | Impresión Bluetooth cuando se necesita respaldo físico |
| RF-06.14 | Cumple | Evidencia al ERP y retorno del estado de acuse |
| RF-07.01 | Cumple | Monto esperado por camión y turno |
| RF-07.02 | Cumple | Rendición compara esperado y declarado |
| RF-07.03 | Cumple | Saldo sin causal impide cierre |
| RF-07.04 | Cumple | Cartera a 30 días con ejecutivo y recontactos |
| RF-07.05 | Cumple | Bloqueo de crédito mantiene contado y cobro |
| RF-07.06 | Cumple | Autorización POS y conciliación sin digitación |
| RF-07.07 | Cumple | Cartola por antigüedad y formatos PDF/XLSX |
| RF-07.08 | Cumple | Tesorería aprueba pago informado por portal |
| RF-07.09 | Cumple | ERP recibe aprobados de forma idempotente |
| RF-07.10 | Cumple | Abono parcial con recibo y saldo al ERP |
| RF-07.11 | Cumple | Cobro PREVENTA sin exigir camión ni entrega |
| RF-08.01 | Cumple | Devolución offline con causa |
| RF-08.02 | Cumple | Calidad habilita disposición de mercadería retenida |
| RF-08.03 | Cumple | Saldo de envases por cliente y tipo |
| RF-08.04 | Cumple | Umbral de envases avisa al preventista |
| RF-08.05 | Cumple | Origen de merma y custodia evitan doble descuento |
| RF-08.06 | Cumple | Pérdida de envases diaria por cliente/tipo/zona |
| RF-08.07 | Cumple | Devoluciones y merma se imputan una vez al costo |
| RF-09.01 | Cumple | Trazabilidad de lote a clientes y guías |
| RF-09.02 | Cumple | Recepción y proveedor reconstruyen origen |
| RF-09.03 | Cumple | Cámaras separadas de kits de camión |
| RF-09.04 | Cumple | 28 kits completos y series durante el trayecto |
| RF-09.05 | Cumple | Regla por familia, alarma local y aviso por dos caminos |
| RF-09.06 | Cumple | Retención por SSCC; Calidad dispone |
| RF-09.07 | Cumple | Rechazo vinculado al sensor, compartimento y tramo |
| RF-09.08 | Cumple | Lote tomado en picking, no atribuido al gateway |
| RF-09.09 | Cumple | Expediente por envío y conciliación de tres series |
| RF-09.10 | Cumple | Parámetros versionados, segundo aprobador y regla preventiva |
| RF-09.11 | Cumple | Salida/carga delimitan exposición de andén |
| RF-09.12 | Cumple | Bajada habilitada con manifiesto y latido vigentes |
| RF-09.13 | Cumple | Pérdida de latido impide nueva bajada; POD autorizado puede terminar |
| RF-09.14 | Cumple | Disposición sanitaria y efectos ERP separados |
| RF-10.01 | Cumple | Reposición revisable por SKU/proveedor |
| RF-10.02 | Cumple | Promociones comprometidas entran al cálculo |
| RF-10.03 | Cumple | Sugerencia aprobada pasa al ERP |
| RF-11.01 | Cumple | Reportes semanales/mensuales y cuatro indicadores |
| RF-11.02 | Cumple | Costo directo e indirecto por entrega/cliente |
| RF-11.03 | Cumple | OTIF exige fecha, franja y todas las unidades |
| RF-11.04 | Cumple | Fill rate y perfect order parten del pedido original |
| RF-11.05 | Cumple | Ocupación se mide en peso y volumen |
| RF-11.06 | Cumple | Tablero actual usa API; BI conserva históricos |
| RF-11.07 | Cumple | Liquidación la realiza M7 y M10 la consulta |
| RF-11.08 | Cumple | Rentabilidad mensual sugiere acciones, no elimina clientes |
| RF-12.01 | Cumple | Pedido EDI por estándar/perfil de cadena |
| RF-12.02 | Cumple | Validación antes de registrar pedido |
| RF-12.03 | Cumple | Equivalencias por cadena a identidad canónica |
| RF-12.04 | Cumple | Pedido válido deriva al ERP por ACL |
| RF-12.05 | Cumple | Pedido normalizado disponible a M3/planificación |
| RF-12.06 | Cumple | Bandeja permite corregir, rechazar y reprocesar |
| RF-12.07 | Cumple | Respuesta de negocio distinta del MDN |
| RF-12.08 | Cumple | Historia de recepción a POD |
| RF-12.09 | Cumple | ASN posterior a carga y referido a guía emitida |
| RF-12.10 | Cumple | Ruta respeta ventana de 30 min |
| RF-12.11 | Cumple | M6 registra cumplimiento de ventana de entrega |
| RF-12.12 | Cumple | POD con receptor; acuse tributario es otro hecho |
| RF-12.13 | Cumple | Acuse comercial por INT-08 y referencia a guía/ASN |
| RF-12.14 | Cumple | Catálogo público sin precios ni stock |
| RF-12.15 | Cumple | Autoservicio valida el mismo stock/crédito |
| RF-12.16 | Cumple | Portal muestra estado y promesa de entrega |
| RF-12.17 | Cumple | Solo documentos de la cuenta autenticada |
| RF-12.18 | Cumple | Saldo desde sistema de gestión |
| RF-12.19 | Cumple | Rutas de empresa transportista para día siguiente |
| RF-12.20 | Cumple | Documentos de sus rutas asignadas |
| RF-12.21 | Cumple | Conductor/vehículo confirmados antes de despacho |
| RF-12.22 | Cumple | Proveedor consulta sus OC, sin escribirlas |
| RF-12.23 | Cumple | Proveedor consulta recepciones de sus órdenes |
| RF-12.24 | Cumple | Proveedor consulta devoluciones y notas ERP |
| RF-12.25 | Cumple | Alta exige vínculo con cliente activo y correo |
| RF-12.26 | Cumple | Autenticación del portal centralizada |
| RF-12.27 | Cumple | Enlace de recuperación de un uso y hasta 15 min |
| RF-12.28 | Cumple | Cierre explícito invalida sesión |
| RF-12.29 | Cumple | Caducidad de sesión por inactividad |
| RF-12.30 | Cumple | Pago Transbank vinculado a pedido y resultado comprobado |
| RF-13.01 | Cumple | Ocho capas con responsabilidades declaradas |
| RF-13.02 | Cumple | Emplazamiento justificado por criterios |
| RF-13.03 | Cumple | Registro ADR vigente alcanza 24 decisiones |
| RF-13.04 | Cumple | Dominio con entidades, relaciones y eventos |
| RF-14.01 | Cumple | INT-15 solo consume fuente de los 42 propios |
| RF-14.02 | Cumple | Ruta planificada frente a real de flota propia |
| RF-14.03 | Cumple | Desvío superior a 3 km alerta al control |
| RF-14.04 | Cumple | Kilómetros y tiempos imputados a entrega/cliente |
| RF-14.05 | Cumple | Identidad personal asociada a vehículo/turno |
| RF-14.06 | Cumple | Geocercas con entrada y salida fechadas |
| RF-14.01-BTT | Cumple | Clasificación por cuatro sensibilidades |
| RF-14.02-BTT | Cumple | Controles ISO con implementación/evidencia |
| RF-14.03-BTT | Cumple | Inventario de entradas, puertos y servicios |
| RF-14.04-BTT | Cumple | Respuesta a críticos en dos horas |
| RF-14.05-BTT | Cumple | Brecha notificada en 24 h y causa en cinco días hábiles |
| RF-15.01 | Cumple | Identidad federada y directorio corporativo |
| RF-15.02 | Cumple | SSO con propagación de cierre |
| RF-15.03 | Cumple parcialmente | MFA de todo acceso externo no queda especificada de forma uniforme |
| RF-15.04 | Cumple | Roles y atributos con segregación |
| RF-15.05 | Cumple | Baja automatizada antes de 24 horas |
| RF-16.01 | Cumple | OTel correlaciona nube y sitios |
| RF-16.02 | Cumple | Acceso del CLIENTE y exportación con latencias diferenciadas |
| RF-16.03 | Cumple | Síntomas de negocio, ruido y escalamiento |
| RF-16.04 | Cumple | Causa de cada crítico con seguimiento hasta cierre |
| RF-17.01 | Cumple | CLIENTE administra identidades y jerarquías |
| RF-17.02 | Cumple | Parámetros de reglas implementadas, no algoritmos nuevos |
| RF-17.03 | Cumple | Segundo aprobador para impacto operacional |
| RF-17.04 | Cumple | Auditoría durable e inmutable con antes/después |
| RF-17.05 | Cumple | Consulta/exportación de auditoría sin SQL |
| RF-17.06 | Cumple | Responsables/plazos/niveles configurables, estados nuevos requieren desarrollo |
| RF-17.07 | Cumple | Bandeja común por responsable y vencimiento |
| RF-17.08 | Cumple | Objetos versionados/cifrados con búsqueda y previsualización |
| RF-17.09 | Cumple parcialmente | HTML/impresión del navegador no acredita generador integrado |
| RF-17.10 | Cumple | Tres canales como mínimo y plantillas administrables |
| RF-17.11 | Cumple | Texto completo con errores, facetas y permisos |
| RF-17.12 | Cumple | Exportación mantiene filtro y orden |
| RF-17.13 | Cumple | Portal público comparte aceptación de accesibilidad |
| RF-18.01 | Cumple | Firma por acto, certificado y evidencia; V-18 sigue como validación |
| RF-18.02 | Cumple | Preferencias no anulan notificaciones obligatorias |
| RF-18.03 | Cumple parcialmente | Entrega/error y reintentos cubiertos; apertura SMS no observable |
| RF-19.01 | Cumple | Clasificación por cuatro sensibilidades; alias del requisito BTT, no obligación nueva |
| RF-19.02 | Cumple | Controles ISO con implementación/evidencia; alias del requisito BTT, no obligación nueva |
| RF-19.03 | Cumple | Inventario de entradas, puertos y servicios; alias del requisito BTT, no obligación nueva |
| RF-19.04 | Cumple | Respuesta a críticos en dos horas; alias del requisito BTT, no obligación nueva |
| RF-19.05 | Cumple | Brecha notificada en 24 h y causa en cinco días hábiles; alias del requisito BTT, no obligación nueva |
| RNF-01.01 | Cumple | Registro de recepción medido desde confirmación hasta pantalla, máximo 2 s |
| RNF-01.02 | Cumple | Retención distingue sanitario cinco años y tributario seis |
| RNF-01.03 | Cumple | Recepción local 24 h y drenaje al ERP hasta dos horas |
| RNF-02.01 | Cumple | CD autónomo 24 h, sincronización hasta dos horas y conflicto determinista |
| RNF-03.01 | Cumple | Registro de línea local hasta 1,5 s con o sin señal |
| RNF-03.02 | Cumple | Consulta conectada de stock/crédito hasta 2 s |
| RNF-03.03 | Cumple | Historial conectado hasta 2 s |
| RNF-04.01 | Cumple | Corrida de ruteo comprometida en menos de veinte minutos |
| RNF-05.01 | Cumple | Confirmación incluye almacenamiento local; no depende de Wi-Fi |
| RNF-05.02 | Cumple | Controles 15 por 15 mm y 30 min a menos 22 grados |
| RNF-05.03 | Cumple | Veinte líneas, error máximo 5 %, entrenamiento hasta dos horas |
| RNF-06.01 | Cumple | Jornada íntegra cifrada durante 14 h |
| RNF-06.02 | Cumple | Alias de autonomía por perfil, no requisito adicional |
| RNF-06.03 | Cumple | Plazo móvil de diez minutos; RNF-02.01 corresponde al CD |
| RNF-07.01 | Cumple | Cobros sincronizan en diez minutos hasta su aceptación |
| RNF-07.02 | Cumple | Cifrado por campo de dominios sensibles; PAN permanece tokenizado |
| RNF-08.01 | Cumple | Registro de retorno completo hasta treinta segundos por ítem |
| RNF-08.02 | Cumple | Sanitario cinco años y efectos tributarios seis |
| RNF-09.01 | Cumple | Lista sanitaria exportable en menos de dos horas |
| RNF-09.02 | Cumple | Vida útil más seis meses con piso de cinco años |
| RNF-09.03 | Cumple | Consultas, modificaciones y exportaciones sensibles auditadas |
| RNF-09.04 | Cumple | Room conserva lectura dentro de cámara sin señal |
| RNF-09.05 | Cumple | Frecuencias separadas por origen y huecos explícitos |
| RNF-09.06 | Cumple | Protección local sin redes externas, retención por latido inválido |
| RNF-09.07 | Cumple | Ambos caminos activos y metas por camino en 95 % de ensayos |
| RNF-09.08 | Cumple | Simulador decide; registro EN12830 conserva aire |
| RNF-09.09 | Cumple | Identidad productor/arranque/secuencia, crítica tardía no se ignora |
| RNF-11.01 | Cumple | Indicadores actuales hasta cinco minutos desde backend conectado |
| RNF-11.02 | Cumple | BI aislado de OLTP para proteger confirmaciones |
| RNF-11.03 | Cumple | Alias del cierre comercial hasta dos horas |
| RNF-11.04 | Cumple | Alias de gestión hasta cuatro horas |
| RNF-12.01 | Cumple | Producción E2 mes 21 antes de enero de 2029 |
| RNF-12.02 | Cumple | Mapeos/perfiles configurables dentro de contratos soportados; transportes nuevos requieren desarrollo |
| RNF-12.03 | Cumple | Acuse comercial hasta treinta minutos, distinto del MDN y tributario |
| RNF-13.01 | Cumple | Sitio conserva escrituras críticas por 24 h sin WAN |
| RNF-13.02 | Cumple | Funciones excluidas y suplencia declaradas |
| RNF-13.03 | Cumple | Talca N+1 y pares activo/espera por cada otro sitio |
| RNF-13.04 | Cumple | Disco tolerado por réplica/RAID según emplazamiento |
| RNF-13.05 | Cumple | Ceph sin RAID hardware, niveles declarados por sitio |
| RNF-13.06 | Cumple | CIS/Ansible y ventana acordada de parcheo |
| RNF-13.07 | Cumple | Tres caminos con topología distinta para CD y cross-docking |
| RNF-13.08 | Cumple | Normal/peak y perfil de drenaje dimensionados |
| RNF-13.09 | Cumple | Cobertura de cámaras es criterio de aceptación, cantidad AP preliminar |
| RNF-14.01 | Cumple parcialmente | Excepción TLS1.2 impide declarar TLS1.3 universal |
| RNF-14.02 | Cumple | KMS con custodio separado y cifrado de todos los almacenes |
| RNF-14.03 | Cumple | Datos y aplicación privados; borde limita publicación |
| RNF-14.04 | Cumple | SIEM necesita correlación de negocio además de retención |
| RNF-14.05 | Cumple | Falcon y Guard Duty por clase de carga, SOC24x 7 |
| RNF-14.06 | Cumple parcialmente | No queda calendarizada la campaña semestral propia |
| RNF-14.07 | Cumple | Pipeline bloquea hallazgos críticos con SAST/SCA/DAST/imágenes |
| RNF-14.08 | Cumple | Cada liberación incluye SBOM |
| RNF-14.09 | Cumple | Procedencia SLSA3 y firma son obligaciones de pipeline |
| RNF-14.10 | Cumple | Datos sintéticos/anonimizados; no productivos reales sin protección |
| RNF-14.11 | Cumple | Posición por vehículo/ruta, finalidad y acuerdo sindical |
| RNF-14.12 | Cumple | Campos personales categorizados y sensibles cifrados/auditados |
| RNF-15.01 | Cumple | Vigencias distintas de token, refresco, sesión y asignación offline |
| RNF-15.02 | Cumple | Firma y rotación sin identificadores en URL |
| RNF-15.03 | Cumple | Ciclo de identidad y siete años de evidencia inmutable |
| RNF-16.01 | Cumple | p 95 de experiencia real; sintéticas solo complementan |
| RNF-16.02 | Cumple | Runbooks por escenario, con automatización progresiva |
| RNF-16.03 | Cumple | Se excluyen secretos y datos sensibles de los logs |
| RNF-17.01 | Cumple | Retención de auditoría de siete años supera el piso |
| RNF-17.02 | Cumple | Exportación grande no bloquea sesión y avisa al terminar |
| RNF-17.03 | Cumple | Portal estático aislado y con caché |
| RNF-19.01 | Cumple | 14,66 TPS peak operacional no equivale a mensajes Io T diarios |
| RNF-19.02 | Cumple | Escala por perfil con umbrales y techo explícitos |
| RNF-19.03 | Cumple | ERP/ACL es candidato a cuello; se explica detección |
| RNF-19.04 | Cumple | 1,5 veces peak una sola vez y estrés hasta quiebre |
| RNF-20.01 | Cumple | 99,9 % mensual de transacción extremo a extremo |
| RNF-20.02 | Cumple | Cuatro criticidades por impacto y Art 78 |
| RNF-20.03 | Cumple | Continuidad BIA/manual/activación como entregable comprometido |
| RNF-20.04 | Cumple | Fallos inyectados antes de producción y semestral |
| RNF-20.05 | Cumple | Falla/latencia/error de cada dependencia documentados |
| RNF-20.06 | Cumple | RTO4h/RPO15min como objetivo de diseño, ensayo regional semestral |
| RNF-20.07 | Cumple | 3-2-1-1-0 incluye restauración verificada |
| RNF-21.01 | Cumple | NOC permanente, dotación por turnos declarada |
| RNF-21.02 | Cumple | SRE nominado dedicado como gerente de servicio |
| RNF-21.03 | Cumple | 80/20, primer contacto 70 y abandono máximo 5 |
| RNF-21.04 | Cumple | Horario general y críticos 24x 7 no se confunden |
| RNF-21.05 | Cumple | Erlang C usa demanda proyectada, no llamadas observadas |
| RNF-21.06 | Cumple | Ticket único y cierre conforme |
| RNF-21.07 | Cumple | Traslado no retira cobertura permanente |
| RNF-21.08 | Cumple | Bolsa evolutiva separada del correctivo sin tope |
| RNF-21.09 | Cumple | Actualizaciones de base anuales con ventana/reversión |
| RNF-22.01 | Cumple | Plan cubre cinco perfiles incluyendo soporte |
| RNF-22.02 | Cumple | Materiales editables y propiedad del CLIENTE |
| RNF-22.03 | Cumple | Turnos y peaks no interrumpen operación |
| RNF-22.04 | Cumple | 7.1.4 certifica a TI antes de H7 y H12 |
| RNF-22.05 | Cumple | Dos jornadas anuales y nuevas personas sin cargo |
| RNF-22.06 | Cumple | Mentoría seis meses desde producción E2 |
| RNF-23.01 | Cumple parcialmente | Especificación del kit aún no fija todos los modelos/mínimos |
| RNF-23.02 | Cumple parcialmente | Resguardo de cabina no acredita IP/caída de todos los modelos |
| RNF-23.03 | Cumple | Cinco años y reserva con mantenimiento; baterías no duran cinco años sin recambio |
| RNF-23.04 | Cumple | Ocho estaciones duales con cifrado, EDR y ergonomía |
| RT-02.01 | Cumple | Ocho capas, componentes e interfaces de la vista lógica |
| RT-02.02 | Cumple | Monolito modular permite perfiles críticos separados; no monolito inseparable |
| RT-02.03 | Cumple | Vistas de lógica, procesos, despliegue, datos y seguridad |
| RT-02.04 | Cumple | Registro de decisiones actualizado hasta ADR24 |
| RT-02.05 | Cumple | Negocio sin estado; sesión y proceso en almacenes externos |
| RT-02.06 | Cumple | UUID del cliente y ventana durable de treinta días |
| RT-02.07 | Cumple | Al menos una vez y orden por agregado; deduplicación de consumidor |
| RT-02.08 | Cumple | Timeout por llamada y resiliencia con retroceso/jitter y mamparos |
| RT-02.09 | Cumple | Modo reducido informado, sin pérdida silenciosa |
| RT-02.10 | Cumple | Umbrales y límites de escala por perfil; valores económicos fuera de oferta técnica |
| RT-02.11 | Cumple | SPOF y riesgos residuales explícitos, no eliminados por un estado Cumple |
| RT-02.12 | Cumple | Sitio nuevo parametriza bodega, rutas y cartera; reservas IP |
| RT-02.13 | Cumple | Dominio con entidades, relaciones y eventos |
| RT-02.14 | Cumple | ACL y reemplazo progresivo aíslan legado y proveedores |
| RT-03.01 | Cumple | AWS primaria en Sudamérica y secundaria declarada |
| RT-03.02 | Cumple | Componentes HA distribuidos en dos zonas; tarea de ruteo se relanza |
| RT-03.03 | Cumple | Terraform/Ansible reproducibles en repositorio del CLIENTE |
| RT-03.04 | Cumple | Subredes de datos privadas; borde limita exposición |
| RT-03.05 | Cumple | Servicios administrados con excepciones justificadas por ADR |
| RT-03.06 | Cumple | Etiquetas, presupuesto y reporte mensual por centro de costo |
| RT-03.07 | Cumple | Portabilidad y esfuerzo de salida declarados como estrategia |
| RT-03.08 | Cumple | Capacidad base comprometida, costos en la oferta correspondiente |
| RT-03.09 | Cumple | Fargate/Lambda justificados para variabilidad; análisis técnico de modalidades |
| RT-03.10 | Cumple | Autonomía CD24h y terreno 14h son alcances distintos |
| RT-03.11 | Cumple | Escritura durable cifrada en terminal y sitio |
| RT-03.12 | Cumple | Conflictos se resuelven por regla, no última fecha |
| RT-03.13 | Cumple | Funciones indisponibles, CD2h y terminal 10min se declaran por separado |
| RT-03.14 | Cumple | Redundancia cubre Talca, Concepción y los tres cross-docking |
| RT-03.15 | Cumple | CIS y parches centralizados con ventana/reversión |
| RT-03.16 | Cumple | Misma observabilidad nube/sitio mediante OTel |
| RT-03.17 | Cumple | CD: fibra/LTE/Starlink; cross-docking: Starlink/dos LTE |
| RT-03.18 | Cumple parcialmente | No todas las familias acreditan el conjunto completo de gestión remota |
| RT-03.19 | Cumple | Greengrass filtra/agrega y decide localmente en cámaras y camión |
| RT-03.20 | Cumple | Volumen y ventanas de sincronización sustentan ancho de banda |
| RT-03.21 | Cumple | VPN IPsec/IKEv 2 por sitio; no exposición directa de base |
| RT-03.22 | Cumple | Verified Access con identidad y postura de equipos |
| RT-03.23 | Cumple | VLAN, autenticación empresarial y estudio de cobertura como aceptación |
| RT-03.24 | Cumple | Qo S prioriza operación; estudio incluye cámaras y congelado |
| RT-04.01 | Cumple | Cinco ambientes operativos como condición de H3 |
| RT-04.02 | Cumple | Equivalencia de preproducción con tres diferencias explicitadas |
| RT-04.03 | Cumple | Ramas protegidas y pares sin escritura directa a principal |
| RT-04.04 | Cumple | Cadena de trazabilidad incluye prueba y despliegue; ejecución futura no simulada por este informe |
| RT-04.05 | Cumple | Pipeline con compilación/unitarias/análisis y bloqueo |
| RT-04.06 | Cumple | Automatización con reversión; aprobación de hito no equivale a paso manual |
| RT-04.07 | Cumple | Azul-verde/canario y demostración antes de cada producción |
| RT-04.08 | Cumple | Un artefacto y configuración por ambiente |
| RT-04.09 | Cumple | Secretos fuera del artefacto, rotación y auditoría |
| RT-04.10 | Cumple | Esquema expandir/contraer permite convivir versiones |
| RT-04.11 | Cumple | 70 % lógica de negocio es distinto del 80 % global de unitarias |
| RT-04.12 | Cumple | Metas de cadencia/lead time/fallos/restauración y medición futura |
| RT-04.13 | Cumple | No productivo se reduce, ahorro económico se remite fuera |
| RT-04.14 | Cumple | INN02 crea/destruye entorno efímero aun ante fallo |
| RT-05.01 | Cumple | Diccionario contado: 121 entidades y 995 atributos, con propietario y sensibilidad Referencia de modelos corregida a 5-L. |
| RT-05.02 | Cumple | Motor y posición CAP diferenciados por dominio |
| RT-05.03 | Cumple | Auditoría y outbox en transacción preservan trazabilidad |
| RT-05.04 | Cumple | ISO25012, validación de captura y tablero de calidad |
| RT-05.05 | Cumple | BI separado de OLTP, sin consulta pesada directa |
| RT-05.06 | Cumple | Exportación íntegra autónoma con manifiesto/huella/conteo |
| RT-05.07 | Cumple | Retención y eliminación segura por dominio |
| RT-05.08 | Cumple | Categorías sensibles con cifrado de campo y custodia separada |
| RT-05.09 | Cumple | Maestros canónicos, dueño y equivalencias evitan duplicados |
| RT-05.10 | Cumple parcialmente | Retención del caso cubierta; falta catálogo de linaje automatizado |
| RT-05.11 | Cumple | Migración con origen, volumen, transformaciones, criterios y reversión |
| RT-05.12 | Cumple | Perfilado/saneamiento con decisión por defecto detectado |
| RT-05.13 | Cumple | Dos ensayos completos, no dos pruebas parciales |
| RT-05.14 | Cumple | Conciliación cuantitativa exige explicación de diferencias |
| RT-05.15 | Cumple | Historia no migrada permanece consultable por retención |
| RT-05.16 | Cumple | Open API3.1 y Async API2.6 desde código |
| RT-05.17 | Cumple | Versionado semántico con preaviso seis meses |
| RT-05.18 | Cumple | m TLS entre servicios y sin claves en URL; contratos externos se levantan |
| RT-05.19 | Cumple | Correlación de entrada/salida común a la operación |
| RT-05.20 | Cumple | Legados y terceros detrás de ACL/adaptadores |
| RT-05.21 | Cumple | Catálogo por interfaz incluye modo/volumen/ventana y falla |
| RT-05.22 | Cumple | Carga/descarga masiva con errores por registro y procesamiento parcial |
| RT-05.23 | Cumple | GS1, EPCIS/CBV, EDI por cadena y formato SII |
| RT-05.24 | No cumple | No se acredita portal de desarrolladores ni credenciales autoservidas |
| RT-05.25 | Cumple | Tableros construidos sobre indicadores del caso |
| RT-05.26 | Cumple | Filtro por dimensión y profundización hasta transacción origen |
| RT-05.27 | Cumple | Autoría Quick Sight y modelo semántico para CLIENTE |
| RT-05.28 | Cumple | Formatos abiertos y calendario de envío |
| RT-05.29 | Cumple | Latencias 5min/2h/4h; antigüedad visible cuando ambos caminos fallan Validación citada en 4.2.6.12; 4.2.11 no existe. |
| RT-05.30 | Cumple | Modelo cinético determinista sí es analítica predictiva; variables/métrica/recalibración declaradas |
| RT-06.01 | Cumple | Tipología separa sala Talca y gabinetes de borde |
| RT-06.02 | Cumple | Blindaje material y resistencia especificados en vista de sala |
| RT-06.03 | Cumple | Plano contiene zonas y recorrido de acceso |
| RT-06.04 | Cumple | Normas de piso/canalización/cableado/etiquetado y certificación por enlace |
| RT-06.05 | Cumple | Racks independientes: ocupación 15U y 12U con margen |
| RT-06.06 | Cumple | CLIENTE ejecuta separación; Lafro X especifica/coordina |
| RT-06.07 | Cumple | UPS15k VA N+1 y al menos 30min a plena carga |
| RT-06.08 | Cumple | Generador 25k VA, estanque 24h y reabastecimiento |
| RT-06.09 | Cumple | Instalación eléctrica independiente y puesta a tierra declarada |
| RT-06.10 | Cumple | Revisión eléctrica semestral con informe |
| RT-06.11 | Cumple | Carga 8,9k W TI, factor 0,95 y PUEaprox 1,5 |
| RT-06.12 | Cumple parcialmente | No está acreditada doble acometida; UPSN+1 no la sustituye |
| RT-06.13 | Cumple | Dos unidades 10k W N+1 y control de rangos |
| RT-06.14 | Cumple | Temperatura/humedad/agua integradas al monitoreo |
| RT-06.15 | Cumple | Paneles ciegos y orientación reducen recirculación |
| RT-06.16 | Cumple | Aspiración láser de detección temprana |
| RT-06.17 | Cumple | Agente limpio automático con aprobación UL/NFPA |
| RT-06.18 | Cumple | Extintores portátiles y certificación/mantención vigentes |
| RT-06.19 | Cumple | Detección/extinción avisan a NOC y CLIENTE |
| RT-06.20 | Cumple | Facial principal con AFIS de respaldo |
| RT-06.21 | Cumple | Identidad, fechas y motivo de acceso en bitácora retenida |
| RT-06.22 | Cumple | Enrolamiento interno y estación externa |
| RT-06.23 | Cumple | Esclusa de una persona con segunda verificación |
| RT-06.24 | Cumple | Seis cámaras, treinta días en línea y archivo recuperable |
| RT-06.25 | Cumple | Terceros autorizados, acompañados y registrados |
| RT-06.26 | Cumple | Medio físico rotativo cifrado y custodia externa |
| RT-06.27 | Cumple | Control de luz, humedad, ventilación y temperatura de custodia |
| RT-06.28 | Cumple | Inventario/movimientos/rotación y prueba semanal de legibilidad |
| RT-06.29 | Cumple | Puestos con telefonía e Internet fuera de zona restringida |
| RT-06.30 | Cumple | Operación habitual no necesita entrar a sala |
| RT-06.31 | Cumple | Uso de sanitarios/zonas existentes explícito |
| RT-06.32 | Cumple | Ingresos y ductos separados; satélite adicional |
| RT-06.33 | Cumple | Lafro X provee conectividad, seguridad y canalizaciones |
| RT-06.34 | Cumple | Esquema de copias inmutables mejora el mínimo |
| RT-07.01 | Cumple | Activo-pasivo caliente justificado por costo/RTO/complejidad |
| RT-07.02 | Cumple | Distancias y amenazas comunes entre dominios |
| RT-07.03 | Cumple | Réplica continua con alertas de retraso |
| RT-07.04 | Cumple | RTO4h/RPO15min se verifican por escenario; residual declarado |
| RT-07.05 | Cumple | Conmutación automatizada bajo autorización del CLIENTE |
| RT-07.06 | Cumple | Retorno con conciliación ensayado semestral |
| RT-07.07 | Cumple | Dos ensayos reales al año con medición e informe |
| RT-07.08 | Cumple parcialmente | Autorización humana impide acreditar disparo automático |
| RT-07.09 | Cumple | 3-2-1-1-0 cubre los componentes del esquema requerido |
| RT-07.10 | Cumple | Custodia de claves independiente de producción |
| RT-07.11 | Cumple | Object Lock/Vault Lock Compliance protege frente a administrador |
| RT-07.12 | Cumple | Restauración mensual medida, distinta de conmutación regional |
| RT-07.13 | Cumple | Frecuencia/retención/tiempo por dominio |
| RT-07.14 | Cumple | PITR temporal permite selección granular; no escritura directa sobre original |
| RT-08.01 | Cumple | Marca/modelo/configuración/consumo y memoria de cálculo por sitio |
| RT-08.02 | Cumple | Réplica/RAID con integridad y monitoreo predictivo |
| RT-08.03 | Cumple | Núcleo/firewall/balanceador con HA |
| RT-08.04 | Cumple | Dos fuentes/circuitos y transferencia para equipos de fuente única |
| RT-08.05 | Cumple | Márgenes sobre carga de año 3, no rendimiento observado |
| RT-08.06 | Cumple | Compra nueva y garantía desde recepción conforme |
| RT-08.07 | Cumple | Ocho estaciones con dos monitores |
| RT-08.08 | Cumple | Ergonomía y eficiencia energética son condiciones de compra |
| RT-08.09 | Cumple | 192 estaciones con cifrado/EDR/extraíbles y actualización |
| RT-08.10 | Cumple parcialmente | Kit aún tiene especificaciones funcionales sin modelo por accesorio |
| RT-08.11 | Cumple | Condiciones reales y baterías; prueba previa no equivale a prueba ejecutada |
| RT-08.12 | Cumple parcialmente | Prestaciones IP/caída incompletas no se sustituyen por uso bajo resguardo |
| RT-08.13 | Cumple | Vida útil con recambio de baterías, calibración y reserva |
| RT-08.14 | Cumple parcialmente | Inventario común no acredita todas las funciones remotas |
| RT-08.15 | Cumple | Unidad de cada variante antes de compra masiva |
| RT-08.16 | Cumple | Ciclo de recepción a disposición y reposición |
| RT-08.17 | Cumple | Sanitización verificable con certificado de todo medio retirado |
| RT-08.18 | Cumple | Gestor autorizado y certificado de disposición |
| RT-08.19 | Cumple | Extensión cuantificada al menos 60meses con mantenimiento |
| RT-09.01 | Cumple | Capacidad deriva de caso y cuatro umbrales por transacción |
| RT-09.02 | Cumple | Concurrencia y perfil horario se derivan, no solo suma diaria |
| RT-09.03 | Cumple | Crecimiento 3x en tres años sin rediseño |
| RT-09.04 | Cumple | Escala con métricas 1min, reacción 3min y drenaje |
| RT-09.05 | Cumple | ERP/ACL candidato a cuello con detección y medidas |
| RT-09.06 | Cumple | 1,5xpeak y estrés a quiebre en preproducción |
| RT-09.07 | Cumple | Informe debe incluir curva, saturación, recursos y recuperación |
| RT-09.08 | Cumple | Encolamiento/tasa/mensaje explícito sin pérdida |
| RT-09.09 | Cumple | Proyección trimestral y propuesta de ajuste con impacto económico |
| RT-09.10 | Cumple | Regresión de desempeño semanal y por candidata con bloqueo |
| RT-10.01 | Cumple | Disponibilidad 99,9mensual medida extremo a extremo |
| RT-10.02 | Cumple | Cuatro criticidades justificadas por impacto |
| RT-10.03 | Cumple | BIA, manuales y activación alineados a ISO22301 |
| RT-10.04 | Cumple | Continuidad TIC ISO27031 articulada con DR |
| RT-10.05 | Cumple | Ventanas operativas y congelamientos con aviso 10díashábiles |
| RT-10.06 | Cumple | Sin interrupción; indisponibilidad excepcional justificada |
| RT-10.07 | Cumple | Inyección de cinco clases de fallas antes de producción y semestral |
| RT-10.08 | Cumple | Comportamiento ante dependencia ausente/errónea/lenta |
| RT-10.09 | Cumple | Presupuesto de error vinculado a suspender cambios no correctivos |
| RT-11.01 | Cumple | Zero Trust por solicitud y mínimo privilegio |
| RT-11.02 | Cumple | STRIDE por componente/integración con actualización |
| RT-11.03 | Cumple | Clasificación por sensibilidad y matriz de control |
| RT-11.04 | Cumple parcialmente | Excepción de remediación en congelamiento puede superar 7/15/30días |
| RT-11.05 | Cumple | Controles ISO27001/27002 con evidencia |
| RT-11.06 | Cumple | Controles de nube 27017 y privacidad 27018 |
| RT-11.07 | Cumple parcialmente | AS2 directo por NLB no acredita el mismo conjunto CDN/WAF/L7 |
| RT-11.08 | Cumple parcialmente | TLS1.2 documentado sigue por debajo del mínimo literal TLS1.3 |
| RT-11.09 | Cumple | KMS y separación de funciones en reposo |
| RT-11.10 | Cumple | Cifrado de campo de categorías del caso, sin guardar PAN |
| RT-11.11 | Cumple | Puerta API controla permisos/esquema/cuota y carga |
| RT-11.12 | Cumple | Reto de bots con alternativa accesible y falsos bloqueos |
| RT-11.13 | Cumple | Entradas de dominio/puerto/servicio, VPN por IP |
| RT-11.14 | Cumple | 12mesesenlínea y 24archivo; seguridad siete años |
| RT-11.15 | Cumple | SIEM correlaciona casos del negocio |
| RT-11.16 | Cumple | Falcon/Guard Duty cubren plataformas del alcance; ERP del CLIENTE se aísla |
| RT-11.17 | Cumple | SOC permanente con ubicación/dotación/procedimiento |
| RT-11.18 | Cumple | Clasificación/escalamiento y aviso crítico 2h |
| RT-11.19 | Cumple | Notificación 24h y causa en cinco días hábiles |
| RT-11.20 | Cumple | Tercero independiente al menos anual y antes de producción |
| RT-11.21 | Cumple | Simulación anual de incidente con CLIENTE |
| RT-11.22 | Cumple | SAST/SCA/DAST e imágenes bloqueantes |
| RT-11.23 | Cumple | SBOM Cyclone DX/SPDX entregado por versión |
| RT-11.24 | Cumple | Firma y procedencia SLSA3 |
| RT-11.25 | Cumple | No productivos usan sintéticos/anonimizados |
| RT-11.26 | Cumple | Dependencias se aprueban por licencia/mantención/vulnerabilidades |
| RT-11.27 | Cumple | Producción sin acceso directo de desarrollo; excepción temporal grabada |
| RT-11.28 | Cumple | OWASPSAMM inicial y reevaluaciónanual |
| RT-12.01 | Cumple | OIDC/OAuth/SAML y directorio con autoridadcentral |
| RT-12.02 | Cumple | SSO y cierre propagado |
| RT-12.03 | Cumple parcialmente | MFA externa no detallada uniformemente para todos los portales |
| RT-12.04 | Cumple | FIDO2/claves de acceso al menos paraadministradores |
| RT-12.05 | Cumple | RBAC con atributos y segregación |
| RT-12.06 | Cumple | Elevación temporal aprobada y sesión registrada |
| RT-12.07 | Cumple | Token/refresco/sesión/asignación offline tienen vigencias distintas |
| RT-12.08 | Cumple | Credenciales firmadas/rotatorias fuera de URL |
| RT-12.09 | Cumple | Identidad completa auditada con retenciónsiete años |
| RT-12.10 | Cumple | Baja automatizada en menos de 24h |
| RT-12.11 | Cumple | PIN en terminal enrolado, relevo y suplente con guantes/sin correo |
| RT-12.12 | Cumple | Autoservicio de alta/recuperación valida vínculo y factor previo |
| RT-12.13 | Cumple | Último recurso con doblecustodia y rotaciónposterior |
| RT-13.01 | Cumple | WCAG2.2AA es aceptación con pruebas automáticas/manuales e informe |
| RT-13.02 | Cumple | Web responsiva y aplicación nativa por terminal, sin simple reducción |
| RT-13.03 | Cumple | Investigación/prototipos antes de construcción definitiva |
| RT-13.04 | Cumple | Umbral/pasos/error/aprendizaje por perfil verificables |
| RT-13.05 | Cumple | Acceso a función principal desdeinicio entres interacciones; distinto de pasos internos |
| RT-13.06 | Cumple | Acciones tienen resultado visible y error comprensible |
| RT-13.07 | Cumple | 44px general y 15mm en picking con guía |
| RT-13.08 | Cumple | Pruebas reales en frío/lluvia/calor/sol/una mano/sin señal |
| RT-13.09 | Cumple | Paleta/tipografía/iconografía/retícula/componentes comunes |
| RT-13.10 | Cumple | Versiones de navegadores y actualización por liberación |
| RT-13.11 | Cumple | Teclado completo, foco y atajos con aceptación manual |
| RT-13.12 | Cumple | Personalización y oscuro declarados; multidioma no justificado por caso |
| RT-14.01 | Cumple | Métricas/logs/trazas y correlación por transacción |
| RT-14.02 | Cumple | CLIENTE accede/exporta con latencias diferenciadas |
| RT-14.03 | Cumple | Mide experiencia real y no solo sintéticas |
| RT-14.04 | Cumple | Síntomas con ruido/agrupación/escalamiento/turnos |
| RT-14.05 | Cumple | Libro y guía por escenario previsible |
| RT-14.06 | Cumple | Causa por crítico, cinco días hábiles y seguimiento |
| RT-14.07 | Cumple | Se excluyen datos sensibles y credenciales de logs |
| RT-14.08 | Cumple | Retención diferenciada de logs/métricas/trazas; costo fuera |
| RT-14.09 | Cumple | Estadística determinista compara franjas históricas y alerta temprana |
| RT-15.01 | Cumple | Utilización por sitio/perfil y revisión para evitar ociosidad |
| RT-15.02 | Cumple parcialmente | Apagado cubierto; acreditación RSA/DTE no aportada |
| RT-15.03 | Cumple parcialmente | Informes futuros no sustituyen la estimación/metodología en oferta |
| RT-15.04 | Cumple parcialmente | PUE declarado, intensidad de carbono regional no aportada |
| RT-15.05 | No cumple | No hay comparación de regiones por carbono |
| RT-15.06 | Cumple | Meta 60 % con horario 60/168 y reporte de consumo |
| RT-15.07 | Cumple parcialmente | Certificados declarados no equivalen a copias/códigosverificados |
| RT-15.08 | Cumple parcialmente | Nómina no identifica todas las certificaciones individuales |
| RT-15.09 | Cumple | Obligación de vigencia/reemplazo y traslape no equivale a acreditar actuales |
| RT-16.01 | Cumple | CLIENTE administra personas/roles/permisos/unidades |
| RT-16.02 | Cumple | Valores de reglas implementadas, con versión y antes/después |
| RT-16.03 | Cumple | Impacto operacional exige segundo perfil |
| RT-16.04 | Cumple | Nuevoalgoritmo/estado/contrato requiere desarrollo; valores existentes configurables |
| RT-16.05 | Cumple | QA simula efecto de parámetro antes de producción |
| RT-16.06 | Cumple | Cada escritura conserva actor/sistema,zona,origen,antes/después |
| RT-16.07 | Cumple | Object Lock protege incluso frente al administrador |
| RT-16.08 | Cumple | Auditoría consultable/exportable con filtros sin SQL |
| RT-16.09 | Cumple | Consulta sensible se registra además de modificación |
| RT-16.10 | Cumple | Siete años superan piso de cinco |
| RT-16.11 | Cumple | Estados/transiciones y delegación/plazos definidos |
| RT-16.12 | Cumple | CLIENTE configuraresponsables/plazos/niveles de flujos existentes |
| RT-16.13 | Cumple | Bandeja por responsable y vencimiento |
| RT-16.14 | Cumple | Expresiones versionadas sin recompilar en puntos implementados; POD/acuse separados |
| RT-16.15 | Cumple | Objetosversionados,búsqueda y previsualización bajo control de acceso |
| RT-16.16 | Cumple | Cifrado/hash/retención por dominio documental |
| RT-16.17 | Cumple | Firma por acto, validación certificado y V18 del receptor |
| RT-16.18 | Cumple | Marca de tiempo y cadena de verificación conservadas seis años |
| RT-16.19 | Cumple | Salida HTML satisface formato abierto de esta fila, distinta de RF17.09 |
| RT-16.20 | Cumple | Correo/app/SMS cumplen tres canales |
| RT-16.21 | Cumple | Plantillas versionadas y canal por cliente tradicional |
| RT-16.22 | Cumple | Preferencia no desactiva avisoobligatorio |
| RT-16.23 | Cumple parcialmente | No se acredita apertura medida en SMS |
| RT-16.24 | Cumple | Proveedor por canal y volumenconjunto; valores en Oferta Económica |
| RT-16.25 | Cumple | Baja comercial suprime cola/reintentos sin impedir avisos operativos |
| RT-16.26 | No cumple | No se ofrece canal conversacional ejecutor deacciones |
| RT-16.27 | Cumple | Búsqueda global con errores/facetas y permisos |
| RT-16.28 | Cumple | Listados exportan el mismo conjuntofiltrado |
| RT-16.29 | Cumple | Exportaciónasíncrona mantiene sesión y avisa al completarse |
| RT-16.30 | Cumple | Auditoría de exportación y portalesporperfil |
| RT-16.31 | Cumple | Portalpúblico comparte accesibilidad y pruebas de carga |
| RT-16.32 | Cumple | Autoatención para pedido/estado/documentos/saldo |
| RT-16.33 | Cumple | Meta 15 % de reducción con línea base y reporte; no es resultado observado |
| RT-16.34 | Cumple | Caché/borde separan portal de APItransaccional |
| RT-17.01 | Cumple | Recepción/preparación/preventa/reparto nativos y cliente PWA; paquetes de todos los perfiles |
| RT-17.02 | Cumple | Kotlin frente a alternativas justificado por offline/periféricos/mantención |
| RT-17.03 | Cumple | Android vigente ydosanteriores con política por tandas |
| RT-17.04 | Cumple | Paquete firmado por MDM yverificación antes deinstalar |
| RT-17.05 | Cumple | Cifrado local; borrado requiere que el equipo recupere red |
| RT-17.06 | Cumple | Periféricos de temperatura y GPS son fuentes y recorridos separados |
| RT-17.07 | Cumple | 9,83MB peor ruta y criterio de batería se validan con unidad de prueba |
| RT-17.08 | Cumple | Vista ligera de portalcon aceptación en dispositivos de bajo costo |
| RT-18.01 | Cumple | Ausencia declarada de componentes de IA es una decisión de alcance |
| RT-18.02 | Cumple | No entrenamiento de terceros es obligación aun sin componente de IA propio |
| RT-18.03 | Cumple | Límites/supervisión de resultado IA noaplican al alcance declarado |
| RT-18.04 | Cumple | Sin modelos aprendidos no se presume evaluación de riesgos de resultados de IA |
| RT-18.05 | Cumple | Sin interacciones de IA que deban registrarse |
| RT-18.06 | Cumple | No hay componente de IA que desactivar |
| RT-18.07 | Cumple | No se presentan resultados de IA |
| RT-18.08 | Cumple | INN03 cinético declara variables/métrica/base/recalibración/deriva |
| RT-18.09 | Cumple | Responsabilidad de resultados de IA no aplica al alcance sin componentes de IA |
| RT-18.10 | No cumple | No se acredita RPA/agentes con ahorro cuantificado |
| RT-19.01 | Cumple | PMO basada en PMBOK con Kanban subordinado al controlformal |
| RT-19.02 | Cumple | Jefe nominado exclusivo y facultado, sujeto aaprobaciones del CLIENTE |
| RT-19.03 | Cumple | Control de cambios registraimpacto y exige aprobación previa |
| RT-19.04 | Cumple | ISO31000, registro vivo porcomité y mitigacionescon disparador |
| RT-19.05 | Cumple | Espacio colaborativo con registros y entregablesactualizados |
| RT-19.06 | Cumple | Informe mensual con físico/financiero/desviaciones/compromisos |
| RT-19.07 | Cumple | Valor ganado con SPI/CPI, no porcentajecualitativo |
| RT-19.08 | Cumple | Tablero accesible en todomomento con estado actualizado |
| RT-19.09 | Cumple | Actas dedosdíashábiles conacuerdos,responsables yplazos |
| RT-19.10 | Cumple | Desviaciónmayor 10 % comunicada encincodíascon recuperación |
| RT-20.01 | Cumple | Implantación por sitio/perfil y calendario contractual |
| RT-20.02 | Cumple | Olas con criterio de avance yreversión con tiempo |
| RT-20.03 | Cumple | Convivencia y conciliacióndiaria sin digitación doble oculta |
| RT-20.04 | Cumple | Indicadores diarios y umbrales de marchablanca |
| RT-20.05 | Cumple | Acompañamiento porola con dotación decreciente |
| RT-20.06 | Cumple | Estabilizacióncuatrosemanas porola y sin cargo adicional |
| RT-20.07 | Cumple | Definición de terminado incluye código/pruebas/docs/seguridad/despliegue |
| RT-20.08 | Cumple | Aceptación por T-17 y Contraparte Técnica, no por compilación |
| RT-21.01 | Cumple | NOC24x 7 con ubicación,dotación y procedimientos |
| RT-21.02 | Cumple | Gerente dedicado nominado durante Operación |
| RT-21.03 | Cumple parcialmente | Falta nómina por tecnología del equipo operativo completo |
| RT-21.04 | Cumple | Documentación transferible y ensayada por personal CLIENTE |
| RT-21.05 | Cumple | Mesapropia L1/L2/L3 y certificacióndeclarada |
| RT-21.06 | Cumple | 80/20,FCR70,abandono 5 yhorariodelcaso |
| RT-21.07 | Cumple | Horario general distinto de coberturacríticos 24x 7 |
| RT-21.08 | Cumple | Orientación detoda complejidad y preguntas frecuentes |
| RT-21.09 | Cumple | Histórico de soporte con tendencia mensual |
| RT-21.10 | Cumple | Aprendizaje detickets y utilidad de conocimiento |
| RT-21.11 | Cumple | Autoformación porperfil yregistro de avance |
| RT-21.12 | No cumple | No se acredita espacio deintercambio deexperiencias |
| RT-21.13 | Cumple | Indicadoresclave del soporte abiertos al CLIENTE |
| RT-21.14 | Cumple | Erlang C usa demanda 2000contactos/mes proyectada |
| RT-21.15 | Cumple | Canalúnico con cicloy clasificación hasta cierre |
| RT-21.16 | Cumple | Traslado L2/L3 no reducepuestosde mesa/NOC/SOC |
| RT-21.17 | Cumple | Sin confirmación ticketno se cierra automáticamente |
| RT-21.18 | Cumple | Reporte mensual por severidad yaccionescorrectivas |
| RT-21.19 | Cumple | Evolutivo 768HH/año separado del correctivo ysaldoacumulable |
| RT-21.20 | Cumple | Mismo estándar de desarrollo para mantenimientoevolutivo |
| RT-21.21 | Cumple | Fracción recalculada 1,7881 % sobre 128853,67HH de Operación |
| RT-21.22 | Cumple | Actualizacionesanuales conventana/reversión |
| RT-22.01 | Cumple | Capacitación porroles incluye administrador/técnico/soporte |
| RT-22.02 | Cumple | Modalidades presencial/online/autoformación/puesto |
| RT-22.03 | Cumple | Materiales español/editables/propiedad CLIENTE |
| RT-22.04 | Cumple | Turnos yacuerdo transportistas, rotación 38 % ypeaks |
| RT-22.05 | Cumple | 7.1.4 certifica TIantesde H7/H12 |
| RT-22.06 | Cumple | Dos jornadasanuales ypersonalnuevo sincargo |
| RT-22.07 | Cumple | Mentoríaseismeses post E2 |
| RT-22.08 | Cumple parcialmente | Base desde H4 y Operación no cubre todo el contrato |
| RT-22.09 | Cumple | Ambiente QA ficticio disponible en horario S43; nooperaciónininterrumpida |
| RT-23.01 | Cumple parcialmente | Historia, sedes y certificaciones publicadas; falta acreditación verificable de antigüedad y certificados. |
| RT-23.02 | Cumple parcialmente | Casos publicados sin testimonios de las contrapartes ni autorización para publicarlos. |
| RT-23.03 | Cumple parcialmente | Directivos y equipo publicados, sin todos los currículos y certificados individuales. |
| RT-23.04 | Cumple parcialmente | Capacidades declaradas, sin acreditación de alianzas ni metodologías certificadas en la evidencia examinada. |
| RT-23.05 | Cumple parcialmente | HTTPS y elementos adaptables no acreditan por sí solos todos los criterios WCAG 2.2 AA. |
| RT-23.06 | Cumple | Compromiso de disponibilidad futura del sitio; esta revisión no prueba disponibilidad continua. |
| RT-23.07 | No cumple | No aparece un centro de recursos en el HTML ni en el JavaScript publicados. |
| RT-23.08 | No cumple | No aparece una demostración, recorrido virtual o portal de soporte en los recursos publicados. |
| RT-23.09 | No cumple | Los niveles de servicio históricos de casos no son métricas de operación en tiempo real. |
| RT-23.10 | No cumple | No aparece una calculadora operativa en el HTML ni en el JavaScript publicados. |
| RT-24.01 | No cumple | No se aportó el video individual con aparición mínima de diez segundos por integrante. |
| RT-24.02 | No cumple | No se aportaron las sobreimpresiones de nombre, cargo, experiencia y especialización. |
| RT-24.03 | No cumple | No se aportó video con certificaciones en pantalla; se conserva la ausencia de este elemento valorado. |
| RT-24.04 | No cumple | Fondo, iluminación y encuadre uniformes no son verificables sin el video. |
| RT-24.05 | No cumple | No se aportó la identidad visual del video. |
| RT-24.06 | No cumple | La normalización del sonido no es verificable sin el video. |
| RT-25.01 | Cumple parcialmente | Los prototipos previstos no acreditan la navegación completa de un prototipo entregado. |
| RT-25.02 | No cumple | No hay evidencia de estados e interacciones del prototipo entregado. |
| RT-25.03 | Cumple parcialmente | La aceptación WCAG general no sustituye la evidencia del prototipo. |
| RT-25.04 | No cumple | Faltan pruebas del prototipo en las resoluciones explícitas de escritorio, tableta y teléfono. |
| RT-25.05 | No cumple | No se entregó el sistema de diseño correspondiente al prototipo. |
| RT-25.06 | No cumple | No se acredita un enlace navegable al prototipo. |
| RT-25.07 | No cumple | No se acredita garantía de acceso al prototipo durante seis meses. |
| RT-25.08 | Cumple parcialmente | Los flujos previstos no demuestran las interacciones del prototipo requerido. |
| RT-25.09 | No cumple | No se entregaron mapa, taxonomía y menús del prototipo. |
| RT-25.10 | No cumple | No se acredita una exportación interactiva del prototipo para revisión sin conexión. |
| RT-26.01 | Cumple parcialmente | El SD13 conserva la arquitectura térmica anterior; el SD4 vigente usa el kit completo. |
| RT-26.02 | Cumple | La validación al mes 15 se distingue de la habilitación al 16; se detallan los paquetes y meses de cada innovación. |
| RT-26.03 | Cumple | Cada innovación tecnológica declara su madurez TRL y sus fuentes APA. |
| RT-26.04 | Cumple | Cada ficha declara probabilidad, impacto, mitigación y contingencia de adopción. |
| RT-26.05 | Cumple | Los indicadores tienen línea base, meta y momento; los beneficios e impactos son estimaciones. |
| RT-26.06 | Cumple | El modelo cinético determinista no incorpora un modelo aprendido. |
| RT-26.07 | Cumple | INN-02 e INN-05 modifican seguridad y cuentan con modelado propio declarado. |
| RT-26.08 | Cumple | INN-02 mide su beneficio al mes 15, antes del mes 16. |

## Verificación de las salidas

Siete raíces afectadas recompiladas con tres pasadas de LuaLaTeX; T-12 final de 264 páginas y T-11 de 45. Se comprobó la presencia de los 653 identificadores en el PDF del T-12 y se revisaron visualmente 23 páginas seleccionadas de las siete salidas. Se corrigió el espaciado del bloque de fuente/nota del T-11 y se verificó el PDF final. Sin caracteres faltantes ni referencias LaTeX indefinidas; T-11 y T-12 sin desbordes. Se conservan dos advertencias inferiores a 1 pt en la declaración IA de SD3 y advertencias de pegamento en tablas inalteradas de SD5. Figuras y bloques TikZ/figure íntegros respecto de la línea base. Las huellas SHA-256 finales quedan en el JSON de verificación.
