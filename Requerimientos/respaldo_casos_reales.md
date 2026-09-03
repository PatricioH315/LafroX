# Respaldo con casos reales análogos a las decisiones de la licitación

> Documento de evidencia. Para cada decisión de la tabla `decisiones.md` (D1–D40) se indica el caso real, la norma o el benchmark de la industria que la respalda (o la matiza), con fuente verificable y el porqué del respaldo. Uso previsto: argumentación en la defensa técnica y en la justificación de requerimientos (Matriz de Cumplimiento Técnico).

---

## 0. Advertencias transversales (corregir antes de la defensa)

1. **OTIF: no comprometer 95 % plano desde el mes 1.** Walmart partió en 75 % y los mayores CPG (P&G, Unilever) estaban en 10–36 % al lanzarse el KPI; el rango "bueno" actual es 90–95 % (retail) y 88–94 % (cadena de frío). Definir base de cálculo (caja/SKU/orden), ventana horaria y curva gradual (85 %→90 %→95 %). *(Aplicado en D21.)*
2. **Ley 21.719 = protección de datos personales** (crea la Agencia de Datos; vigencia 01-dic-2026). NO es de jornada ni de trazabilidad. El régimen de jornada de conductores es la Ley 21.561 / régimen especial del transporte. Chile no tiene ley propia de trazabilidad electrónica de alimentos; apoyarse en D.S. 977/96 + benchmarks FSMA 204 y Costco como referencia comercial.
3. **FSMA 204 no aplica operativamente hasta 20-jul-2028** (Ley P.L. 119-37). Citarla como benchmark de diseño a 2–3 años, no como exigencia inmediata. Walmart/Costco la exigen comercialmente de todos modos.
4. **Monitoreo ≠ bloqueo automático.** HACCP/GDP exigen decisión documentada por autoridad de calidad tras una excursión, con reglas pre-acordadas. *(Aplicado en D25.)*
5. **FCR 70 % es alcanzable (banda "buena")**; no inflar por encima de ~75 %. Solo 5 % de centros logra world-class (80 %).

---

## A. KPI de servicio, preventa y reparto

### D1 / D21 — OTIF y Fill Rate como KPI contractual
- **Caso:** Walmart (EE. UU., 2017–18) lanzó "On-Time, In-Full": 75 % (ago-2017) → 85 % (abr-2018), meta 95 %, multa 3 % del valor del embarque por tardío/temprano/incompleto. Hoy ~98 %.
  - **Fuente:** Supply Chain Dive — https://www.supplychaindive.com/news/Walmart-OTIF-April-deadline-supplier-effects/515935/ ; DC Velocity — https://www.dcvelocity.com/articles/29022-wal-mart-delivery-mandate-will-push-supply-chain-to-up-its-game
- **Caso (matiz):** Benchmarks 2025-26: retail "bueno" 90–95 %, cadena de frío 88–94 %. Al lanzarse, los 75 mayores proveedores de Walmart tenían OTIF de ~10 % y ninguno llegaba al 95 %.
  - **Fuente:** IndustryWeek/Bloomberg — https://www.industryweek.com/supply-chain/article/22022636/fined-for-arriving-early-wal-mart-puts-its-suppliers-on-notice ; Speed Commerce — https://www.speedcommerce.com/on-time-and-in-full-otif-meaning/
- **Caso (definición):** Encuesta TPA + McKinsey a 24 retailers/manufactureras: 92 % quiere un estándar único; 79 % prefiere "in-full" a nivel caja y "on-time" según fecha solicitada con tolerancia de 1 día de anticipación; falta consenso en el ancho de ventana.
  - **Fuente:** McKinsey — https://www.mckinsey.com/capabilities/operations/our-insights/defining-on-time-in-full-in-the-consumer-sector
- **Por qué respalda:** OTIF/Fill Rate como KPI contractual es práctica líder en retail/CPG con penalización económica. La corrección exigida (ventana + base de cálculo + curva gradual) coincide con el aprendizaje del benchmark.

### D6 / D40 — DSD / preventa-conductor, rendición de caja, control de descuentos en terreno
- **Caso:** Coca-Cola Hellenic (bottler en 28 países) digitalizó DSD/last-mile con osapiens HUB: POD digital, cashless, tracking en tiempo real y settlement automatizado con SAP; +30 % eficiencia, ~8,5 M entregas/año.
  - **Fuente:** osapiens (2025) — https://osapiens.com/wp-content/uploads/2025/01/osapiens-Case-Study-CocaCola-Hellenic-EN-2.pdf
- **Caso:** Swire Coca-Cola (bottler #5 global) desplegó SFA + DMS + DSD + TPM (gestión de promociones) con eBest, integrando preventa, reparto y control de promociones.
  - **Fuente:** eBest — https://www.ebestmobile.com/client-success/swire-coca-cola-case-beverage-industry-best-practice/
- **Caso (LatAm):** Bimbo y Nestlé (Chile/Perú) con TMS móvil (Descartes + Drivin) digitalizan la conciliación de caja en ruta, recalculando montos ante entregas parciales/rechazos; reduce el cierre de ruta hasta 60 %.
  - **Fuente:** Drivin — https://driv.in/en/blog/collections-settlements-fmcg-logistics
- **Caso (Chile):** Coca-Cola Andina con DispatchTrack/SimpliRoute redujo 40 % la dispersión de rutas y su app "Mi Ruta" registra entregas, firmas digitales y stock desde el celular.
  - **Fuente:** Beetrack/DispatchTrack — https://www.beetrack.com/es/historias-de-clientes/chile/optimiza-tus-rutas-de-entrega-como-coca-cola-andina ; Coca-Cola Andina — https://www.koandina.com/nuestra-compania/ecosistemami/mi-ruta/
- **Por qué respalda:** el modelo preventa-conductor con rendición de efectivo y control de promociones en terreno es el estándar de embotelladoras globales y está disponible/validado en LatAm y Chile.

### D15 / D38 — POD digital y articulación con GDE / acuse de recibo
- **Caso:** ePOD con firma + foto + QR + GPS ya se comercializa en Chile (Webfleet/ePOD, Claro, Formidável); en roofing (RouteMagic) redujo disputas 18 % y aceleró la facturación.
  - **Fuente:** Webfleet CL — https://www.webfleet.com/es_cl/webfleet/fleet-management/workflow-management/electronic-proof-of-delivery/ ; Claro — https://www.clarocloud.cl/portal/ar/cld/productos/iot/gestion-de-logistica-claro/ ; RouteMagic — https://www.routemagic.app/customers/case-studies/about-roofing/
- **Caso (norma Chile):** La Guía de Despacho Electrónica (GDE) es obligatoria desde 17-ene-2020 (Ley 21.131) y debe incluir identificación del transportista y del conductor (nombre y RUT); la Ley 19.983 regula el acuse de recibo electrónico (firma digital) y su mérito ejecutivo; la Res. Ex. 91/2026 del SII refuerza la fiscalización al transporte (nuevos datos de traslado, vigencia 01/11/2026).
  - **Fuente:** SII — https://www.sii.cl/destacados/factura_electronica/guia_despacho.html ; Ley 19.983 — https://www.sii.cl/factura_electronica/desc_19983.pdf ; Facele — https://facele.cl/guias-de-despacho-en-chile-el-sii-refuerza-la-fiscalizacion-al-transporte-con-la-resolucion-exenta-n-91-de-2026/
- **Por qué respalda:** digitalizar el POD y vincularlo a la GDE/acuse es obligación vigente y evolutiva en Chile; el requisito de RUT de conductor refuerza además D20/D5 (confirmación diaria de conductor).

### D22 — Promesa de entrega en ventana horaria y hora de corte
- **Caso:** Guías de ruteo (DispatchTrack, Optivo, Routella, Locus) tratan la ventana horaria (2–4 h típica en última milla) y el "depot cut-off time" como restricciones de primera clase que el optimizador resuelve junto con capacidad y tráfico; prometer solo lo cumplible preserva densidad de ruta.
  - **Fuente:** Optivo — https://www.optivologistics.com/en/blog/delivery-time-windows-how-to-manage/ ; DispatchTrack — https://www.dispatchtrack.com/blog/delivery-route-planner-best-practices/ ; Locus — https://locus.sh/blogs/delivery-route-optimization/
- **Por qué respalda:** la ventana comprometible (RF-03.14) + respeto de la ventana (RF-04.07, RF-12.10) + ETA (RF-04.06) + corte que dispara picking (RF-05.01) es el diseño estándar del ruteo en última milla.

### D24 — Observación de góndola y temp-check por el preventista
- **Caso:** La observación de góndola en retail execution es práctica consagrada (Ag Barr/Ava, Mondelez/EasyPicky, Wall's/eBest, Clobotics): detectan stock/planograma y corrigen en terreno reduciendo quiebres. Para congelados/refrigerados, el temp-check es estándar: Plumsense redujo -88 % de spoilage en 180 camiones (merma anual US$1,1M → <US$200k); DPD Fresh garantiza temperatura 100 % con trackers.
  - **Fuente:** Clobotics — https://clobotics.com/case-studies/retail/ ; Plumsense — https://www.plumsense.com/case-study/protecting-cold-chain-integrity-for-a-national-food-distributor/
- **Por qué respalda:** registrar merma en góndola con SKU/lote (RF-08.05) y alertas de envases (RF-08.04) es la práctica de ejecución de retail; el temp-check de frío queda cubierto por la cadena de frío (D4/D25).

### D10 — Control del parque de envases/pallets retornables y pérdidas
- **Caso:** CHEP (pooling, 500 M activos) invirtió +US$20 M en RFID (PLUS ID) para rastrear y reducir pérdidas; ~10 M de pallets "fugados" del circuito cerrado con costo de reemplazo hasta US$21/pallet (caso académico Emory). CHEP Brazil y Tanimura & Antle (IFCO) usan tracking IoT/RFID y VMI para controlar pérdidas por cliente.
  - **Fuente:** Beontag — https://www.beontag.com/en-GB/cases/chep-achieves-real-time-rti-container-tracking-with-rfid/ ; Emory/ICIS 2007 — https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1158&context=icis2007
- **Por qué respalda:** controlar por saldo por cliente (cuenta corriente, RF-08.03/RF-08.06) y alertar ante umbrales (RF-08.04) es la estrategia aceptada (pooling + trazabilidad) para la pérdida del 14 % anual del caso; el caso académico confirma que sin control se filtra >10 % del pool.

---

## B. Trazabilidad y cadena de frío

### D2 / D35 — Trazabilidad por LOTE, modelo de eventos EPCIS, retiro forward/backward
- **Caso (regla):** FSMA 204 (FDA), 21 CFR §1.1300–1.1400, define el **Traceability Lot Code (TLC)** como unidad de control sanitario y un modelo **CTE/KDE** tipo EPCIS; respuesta en 24 h (o plazo acordado). EPCIS es formato interoperable recomendado.
  - **Fuente:** FDA — https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods ; CRS R48925
  - **Matiz:** cumplimiento postergado a 20-jul-2028 (P.L. 119-37). Usar como benchmark.
- **Caso (técnica):** GS1 US publicó el mapeo de cada CTE/KDE de FSMA 204 como **EPCIS 2.0 JSON** (GTIN+Batch/Lot, GLN como TLC Source Reference).
  - **Fuente:** GS1 US — "EPCIS Recommendations for FSMA 204 Critical Tracking Events"
- **Caso (prueba):** Walmart/IBM Food Trust: la trazabilidad de una caja de mangos pasó de ~7 días a **2,2 segundos**; Walmart luego exigió a proveedores de hojas verdes ingresar a la red (2018).
  - **Fuente:** IBM PR (prnewswire) ; Computerworld 15-oct-2018
- **Caso (retiros reales donde el lote grueso falló):**
  - Romero E. coli 2018 (Yuma): registros manuscritos y conmingling impidieron identificar la finca en 6/7 ramas; se pidió evitar TODA la romana. → FDA/CDC investigation summaries.
  - ConAgra 2007 (mantequilla de maní): identificada solo por código de producto "2111"; retiro ampliado a todo el producto desde oct-2004; 212 pacientes enfermos tras el retiro. → Sheth et al., *Clin Infect Dis* 2011 (doi 10.1093/cid/cir407).
  - Rose Acre 2018 (huevos): identificación solo por planta P-1065 + fecha juliana; retiro de 206,7 M huevos con confusión en la distribución. → CDC archive.
- **Por qué respalda:** el lote (y no caja/pallet) como unidad sanitaria con eventos EPCIS y trazado forward/backward es exactamente el modelo regulatorio y de mejor práctica al que converge la industria; D2/D35 lo implementan.

### D35 (retiro < 2 h) — Benchmark de plazos
- **Caso:** Costco (Addendum V3.0, cláusula 3.1.5) exige trazar un paso atrás/adelante **dentro de 2 horas, 100 % del lote**, con mock recall anual y aviso en 24 h ante retiro real. Walmart/Sam's (ago-2025) exigen FSMA 204 con hold/rechazo de carga y penalidades por trazabilidad insuficiente.
  - **Fuente:** one.walmart.com / enablement.walmart.com ; Azzule "Costco Food Safety & Quality Audit V3" ; fsma204hub.com
- **Por qué respalda:** el < 2 h de la licitación coincide con el estándar comercial de Costco y supera el 24 h de FSMA 204 y el 1 día hábil (guía FSAI) de la UE. Defendible como estándar comercial duro.

### D4 / D25 — Excursión térmica configurable y decisión de bloqueo (no automático)
- **Caso (norma alimentos):** Código **SQF Storage & Distribution** y guía **GCCA Cold Chain Best Practices**: límites UCL/LCL por producto, tiempo excedido acumulado sobre UCL como criterio, alarmas y **procedimiento de desviación con disposición documentada** (liberar/bloquear/mover/rechazar); "una desviación no es rechazo automático, pero la decisión debe ser demostrable y documentada".
  - **Fuente:** sqfi.com ; gcca.org
- **Caso (norma farma extrapolable GDP):** UE GDP 2013/C 343/01: ante excursión → reporte, cuarentena del stock, evaluación contra estabilidad y **disposición por persona autorizada**, permitiendo tolerancias pre-acordadas; el bloqueo previo a la evaluación es innegociable, pero lo decide la autoridad de calidad.
  - **Fuente:** health.ec.europa.eu
- **Caso (IoT):** CD de alimentos con 48 sensores IoT y umbrales por zona configurados vs HACCP/FDA logró 0 rupturas tras eliminar controles manuales cada 4 h. (Caso vendor, usar como evidencia de práctica.)
  - **Fuente:** ifactoryapp.com ; iot-works.com UK cold-chain
- **Por qué respalda:** la excursión se define por tiempo×grados configurables (RF-09.06) con alerta en tiempo real (RF-09.05) y **bloqueo decidido por autoridad de calidad, no automático** — exactamente el patrón HACCP/GDP. *(Matiz aplicado en D25.)*

### D25 (hardware a −22 °C operable con guantes)
- **Caso:** Zebra MC9400/MC9450 Freezer (rango −30 °C a +50 °C, caída 7 ft a −30 °C MIL-STD-810H, pantalla táctil y ventana de escáner con calefacción, teclado operable con guantes); Honeywell CK65/CK67 Cold Storage (teclado grande para guantes, IP65/IP68, batería 7.000 mAh, Android 14).
  - **Fuente:** spec sheets Zebra (MC9400/MC9450) ; automation.honeywell.com (CK65) ; poscentral.co.uk (CK67)
- **Por qué respalda:** existen dispositivos de grado congelado masivos que cubren −22 °C con UI para guantes; exigir RNF-05.01/02/09.04 y cubrir W-Fi en cámaras (RNF-13.09) es auditable y disponible en el mercado.

### D35 (marco normativo chileno)
- **Caso (norma):** **D.S. 977/96 (RSA)** art. 1, 67 (temperatura/humedad en almacenamiento/transporte), art. 68 (perecibles en vehículos cerrados con termómetro de lectura exterior), art. 107 (rotulado incluye lote). **D.S. 297/1992** define "lote" y exige identificación indeleble del lote y de fábrica. **Ley 20.606** es etiquetado nutricional (NO trazabilidad). Chile **no tiene** reglamento de trazabilidad electrónica de alimentos comparable a FSMA 204.
  - **Fuente:** minsal.cl (RSA actualizado 06-mar-2026, Manual MINSAL) ; D.S. 297 — faolex
- **Por qué respalda:** hay obligación de lote en el rótulo y de control de temperatura (refuerza D4), pero no mandato de trazabilidad electrónica → fundamentar la trazabilidad en benchmarks FSMA/Costco + D.S. 977/96, no en una ley chilena que no existe.

### Verificación Ley 21.719 (transversal)
- **Caso (norma):** La **Ley 21.719** (prom. 25-nov-2024, vigencia diferida 01-dic-2026) "Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales", reformando la Ley 19.628. NO es ley de jornada ni de trazabilidad (la de jornada es la Ley 21.561).
  - **Fuente:** Diario Oficial 13-dic-2024 ; BCN Ley Chile #1209272 ; LLM UC (2025)
- **Por qué respalda:** D6/D34/RNF-07.02 y `Informe.md` ya la usan como protección de datos personales (correcto). No citarla como jornada ni trazabilidad. *(Precisión añadida en lista de normativa.)*

---

## C. Arquitectura y tecnología

### D14 — Reemplazar el WMS legado (no extenderlo)
- **Caso:** SAP dejó de dar soporte mainstream a SAP WM el 31/12/2025; cientos de almacenes migran a SAP EWM como reemplazo completo por deuda técnica. Caso Manhattan WMoS documenta migración de WMS legacy + interfaces + soporte post-go-live.
  - **Fuente:** Swisslog — https://www.swisslog.com/en-us/blog/2026/05/upgrade-legacy-warehouse-software-with-sap-ewm ; BONbLOC — https://www.bonbloc.com/case-study/manhattan-wms-migration-support.html
- **Por qué respalda:** sustituir (no extender) un WMS con brecha funcional y deuda técnica acumulada es el patrón estándar de la industria.

### D17 / D29 — Híbrida nube/on-premise + borde operacional
- **Caso:** En bodegas de alta velocidad, la nube pura tiene latencia de round-trip de 8–15 s vs 200–500 ms en borde; 15 s consumen 17 % de la ventana de reacción de 90 s. Datex y proveedores WMS usan lógica de automatización crítica on-premise con sincronización asíncrona a la nube. Panduit clasifica los entornos de bodega como "Harsh Indoor" (gabinetes rugged sin TI dedicado).
  - **Fuente:** iFactory AI — https://ifactoryapp.com/industries/delivery-operations-management/ ; Inbound Logistics (oct-2025) — https://www.inboundlogistics.com/articles/wms-2025-boosting-operations-beyond-the-warehouse/ ; Panduit — https://www.panduit.com/.../edge-computing.pdf
- **Por qué respalda:** borde/almacén on-premise por latencia/criticidad (RNF-02.01, RNF-05.01) y nube para analítica es la arquitectura correcta y validada; gabinetes de borde rugged en bodega (D29) es estándar.

### D18 — PostgreSQL transaccional + motor analítico separado
- **Caso:** Tinybird: "no ejecutes consultas analíticas en tu OLTP primaria — es supervivencia"; una consulta analítica masiva puede detener la aplicación. Reintech confirma que PostgreSQL es robusto para OLTP logístico pero OLAP requiere instancia/configuración separada (los parámetros de tuning son contradictorios).
  - **Fuente:** Tinybird — https://www.tinybird.co/blog/2025-02-27-outgrowing-postgres-how-to-optimize-and-integrate-an-oltp-olap-stack ; Reintech — https://reintech.io/blog/postgresql-database-tuning-olap-vs-oltp
- **Por qué respalda:** desacoplar OLTP (PostgreSQL) de OLAP (RF-11.06, RNF-11.02) es best practice; sin separación se degrada picking/preventa.

### D19 — Apps nativas de terreno (no PWA/híbrida)
- **Caso:** El ecosistema logístico profesional usa Android rugged nativo (Zebra, Honeywell), no PWAs: acceso a escáner físico, impresora térmica ZPL/CPCL, GPS, base de datos embebida y sub-segundo sin red. Las PWAs tienen acceso limitado/inconsistente a periféricos, push y segundo plano (especialmente iOS).
  - **Fuente:** Cleverence — https://www.cleverence.com/articles/wms-warehouse-apps/10-barcode-apps-emphasizing-offline-first-4821 ; TekRevol — https://www.tekrevol.com/blogs/native-vs-pwa
- **Por qué respalda:** la operación offline 14 h, periféricos y guantes (RNF-05.02/06.01) exigen nativo; PWA no cubre de forma robusta esos casos.

### D26 / D27 — Enlace redundante, DR activo-pasivo, RTO/RPO
- **Caso:** Benchmarks retail: RTO 1–4 h, RPO 15–30 min. Active-active para RTO ~0; warm standby activo-pasivo para RTO de horas; cold backup para días. VMware Cloud on AWS logra RTO ~15 min y RPO <10 min con warm standby automatizado.
  - **Fuente:** DataCamp — https://www.datacamp.com/blog/rto-vs-rpo ; PeerSpot VMware Cloud on AWS
- **Por qué respalda:** RTO≤4 h y RPO≤15 min del caso está alineado con retail crítico; activo-pasivo es el tier correcto (no sobre-ingeniería activo-activo a ese RTO).

### D28 — RAID (RAID 10 para transaccional)
- **Caso:** RAID 10 supera a RAID 6 en IOPS de escritura y velocidad de rebuild; recomendado para bases de datos transaccionales y VMs (WMS). RAID 6 para datos fríos/archivado donde mide la capacidad.
  - **Fuente:** WunderTech — https://www.wundertech.net/raid-6-vs-raid-10
- **Por qué respalda:** RAID 10 para el transaccional (picking) y RAID 6 para datos fríos es la configuración indicada; justifica la elección frente a alternativas (RNF-13.03/04/05).

### D30 — Cuello de botella y pruebas de carga 1.5× peak
- **Caso:** Load testing de retail antes de Black Friday simula **150–200 %** del pico para encontrar breakpoints; el peak genera 20–30× el tráfico normal. SCAYLE recomienda duplicar el tráfico esperado y probar app + infra + DB + red.
  - **Fuente:** Aqua-Cloud — https://aqua-cloud.io/load-testing-before-peak-season/ ; SCAYLE — https://www.scayle.com/library/blog/black-friday
- **Por qué respalda:** probar al 1.5× del peak de septiembre (RNF-19.04) y declarar el cuello de botella (RNF-19.03) es práctica estándar de retail estacional.

### D31 — Degradación elegante / funciones no disponibles en offline
- **Caso:** Google Cloud Well-Architected define "graceful degradation" como principio de confiabilidad (continuar con rendimiento/alcance reducido en vez de fallar completo). En flotas logísticas heterogéneas: suspender funciones no esenciales, mantener la ruta crítica, usar fallbacks.
  - **Fuente:** Google Cloud — https://docs.cloud.google.com/architecture/framework/reliability/graceful-degradation ; Inferensys
- **Por qué respalda:** declarar qué funciones no están disponibles offline y su procedimiento manual (RNF-13.02) es el patrón estándar de degradación elegante.

### D36 — Go-live por oleadas (no big-bang)
- **Caso:** Hershey 1999 (SAP R/3 + Manugistics + Siebel big-bang en temporada pico): >US$100 M en órdenes sin procesar, ganancias -19 %. Panorama Consulting: el big-bang solo aplica a 1–2 áreas funcionales; el rollout por fases (módulo/unidad/geografía) reduce el radio de explosión de cada fallo.
  - **Fuente:** MeltingSpot — https://meltingspot.io/en/blog/hersheys-sap-erp-failure-112-million-dollar-halloween-disaster ; Panorama — https://www.panorama-consulting.com/big-bang-implementation/
- **Por qué respalda:** puesta en producción por oleadas (RT-20.02) con indicadores de marcha blanca es la recomendación de la industria; nunca go-live en temporada pico (septiembre).

---

## D. Soporte, datos, identidad e integraciones

### D33 — Mesa de ayuda con Erlang C, 80/20, FCR 70 %, traslados a sitios alejados
- **Caso (método):** La fórmula de Erlang C (Erlang, 1917) es la base del WFM de contact centers; el SLA "80 % < 20 s" es el default de la industria desde los sist. Bell/ICMI y lo usan ACD, COPC y outsourcers.
  - **Fuente:** DialPhone — https://www.dialphone.com/tools/erlang-calculator
- **Caso (FCR):** SQM Group benchmark 2024 (500+ centros): FCR promedio **69 %**, banda "buena" 70–79 %, world-class 80 % (solo 5 %); retail 73–75 %; soporte técnico 60 %; órdenes 71 %.
  - **Fuente:** SQM Group — https://www.sqmgroup.com/resources/library/blog/call-center-fcr-benchmark-2024-results-by-industry
- **Caso (soporte en terreno/frío):** Distribuidor de alimentos con monitoreo IoT en tránsito: -71 % reclamos, merma US$1,1M → <US$200k/año; telemetría que convierte desviaciones en alertas en 2 min.
  - **Fuente:** Plumsense — https://www.plumsense.com/case-study/protecting-cold-chain-integrity-for-a-national-food-distributor/
- **Por qué respalda:** 70 % FCR es realista (banda "buena"); Erlang C + 80/20 es el estándar; considerar shrinkage 25–35 % y ocupación objetivo <85 % al dimensionar (RNF-21.05).

### D39 — NOC 24×7×365 + alertamiento por síntomas de negocio
- **Caso:** INOC (NOCaaS) con AIOps: correlación de alarmas a ticket único; AT&T redujo onboarding de 6 a 1 semana; SHI 10× reducción de MTTR. ServiceNow ITOM AIOps alerta por síntomas de negocio (transacciones/APIs que exceden SLA), no solo métricas crudas. GEODIS Control Tower y Locus marcan pedidos en riesgo antes de impactar SLA y miden OTIF.
  - **Fuente:** INOC — https://www.inoc.com/lp/noc-monitoring ; ServiceNow — https://www.servicenow.com/docs/r/it-operations-management/noc-operator-aiops-use-case.html ; GEODIS — https://geodis.com/us-en/resources/blog/... ; Locus — https://locus.sh/blogs/supply-chain-control-tower/
- **Por qué respalda:** NOC 24×7×365 (RNF-21.01) + observabilidad unificada (RF-16.01) + alertas por OTIF/síntomas (RF-16.03) es el modelo maduro de operaciones logísticas, no solo de TI.

### D34 — Autogestión de registro/recuperación para usuarios externos sin correo corporativo
- **Caso:** Microsoft Entra External ID ofrece self-service sign-up B2B: el socio se registra con el correo que quiera, la app recopila atributos (RUT/teléfono), sin correo corporativo ni intervención manual de TI; se complementa con self-service password reset/recovery.
  - **Fuente:** Microsoft Learn — https://learn.microsoft.com/en-us/entra/external-id/self-service-sign-up-overview ; https://learn.microsoft.com/en-us/entra/external-id/self-service-portal
- **Por qué respalda:** el alta/recuperación de credenciales de transportistas/proveedores sin correo corporativo (RF-06.08, RF-15.xx, RT-12.12) es best practice de un proveedor identitario líder.

### D20 / D5 — Portal de transportistas con confirmación diaria de conductor/vehículo
- **Caso:** Walmart estandarizó el carrier onboarding self-service (wls.walmart.com) y los carriers confirman cita/vehículo-conductor por ventana horaria en Retail Link; llegar fuera de ventana = penalidad (3 % del costo) y baja en compliance scorecard (target ~98 % on-time). En Chile, Walmart/SMU/Cencosud/Tottus operan cita previa por CD en ventanas de 30–60 min y exigen etiquetado SSCC + **EDI DESADV** antes de partir + INVOIC, con multas por fill rate.
  - **Fuente:** Walmart — https://wls.walmart.com/ ; Logistok — https://logistok.cl/logistica-b2b-supermercados/ ; GS1 Chile — https://gs1chile.org/Estandares/comparte
- **Por qué respalda:** confirmación diaria de conductor/vehículo con penalización es práctica vigente que las cadenas imponen; desmiente que el EDI retail esté obsoleto (sigue mandatorio en Chile).

### D37 — Parámetros multi-sitio para replicar a un nuevo CD sin rediseño
- **Caso:** SAP Activate documenta Template Project + Rollout Projects con categorías de proceso (global no cambiable / standard / local) y Solution Standardization Board; casos LeverX (global SAP EWM template en 3 regiones) y Bayer/Blue Yonder (procesos estándar en 350+ locaciones).
  - **Fuente:** SAP Community — https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/... ; LeverX — https://leverx.com/case-studies/global-sap-ewm-template-implementation ; Supply Chain 24/7 (Bayer/Blue Yonder)
- **Por qué respalda:** un WMS único parametrizado por sitio (RF-02.01/RF-02.02) para un futuro CD Los Lagos es el patrón "template + rollout" sancionado (RT-02.12).

### D32 — Migración de datos históricos
- **Caso:** Los fallos famosos de ERP (Hershey US$100M+, Nike US$100M, Revlon US$64M, FoxMeyer quiebra, Lidl €500M, Target Canada por master data) indican que la calidad/migración de datos es la causa técnica #1 de desvíos (~50–75 % de proyectos). Las prácticas que respaldan D32 (limpieza previa, transformación en staging, validación con saldos control, dry-run, reversión) provienen de mejores prácticas de implantación; el caso Credencys (retail multi-sitio) reporta -82 % errores de migración y 99,4 % exactitud validada.
  - **Fuente:** Panorama/ERP Research (causa #1) ; topdynamicspartners (prácticas) ; Credencys (retail multi-sitio)
- **Por qué respalda:** el plan por dominio con transformación, calidad, validación y reversión (RT-05.11–15) es la práctica correcta; la migración es la mayor fuente de riesgo técnico.

---

## Notas de rigor
- **Sesgo de vendor:** casos como iFactory, IoT-WorkS, osapiens, eBest, Cleverence, Drivin, SQM (referencial para FCR) son *case studies de proveedores*; usarlos como evidencia de práctica dominante, no como dato regulatorio o precio.
- **Fuentes regulatorias primarias:** FDA, CDC, EUR-Lex, GS1 US, SII, Diario Oficial/BCN, minsal.cl deben preferirse cuando se cita una norma.
- **Fechas a vigilar:** vigencia Ley 21.719 (01-dic-2026), postergación FSMA 204 (20-jul-2028), Res. Ex. 91/2026 SII (01/11/2026), fin soporte SAP WM (31-12-2025).

## Matriz de cobertura
| Decisión | Respaldo |
|---|---|
| D1/D21 | OTIF Walmart + McKinsey + benchmarks |
| D2/D35 | FSMA 204 + EPCIS GS1 + retiros reales + Costco/Ley |
| D4/D25 | SQF/GCCA + GDP + IoT + hardware Freezer |
| D5/D20 | Walmart carrier + cita previa retail chileno + EDI |
| D6/D40 | Coca-Cola Hellenic/Swire + Bimbo/Nestlé Drivin + Andina |
| D10 | CHEP + RFID/pooling |
| D14 | SAP WM→EWM + Manhattan |
| D15/D38 | ePOD Chile + GDE/19.983/Res 91 |
| D17/D29 | Edge iFactory + Datex + Panduit |
| D18 | Tinybird + Reintech |
| D19 | Cleverence + TekRevol |
| D22 | Optivo/DispatchTrack/Locus |
| D24 | Clobotics + Plumsense |
| D26/D27 | DataCamp + VMware Cloud on AWS |
| D28 | WunderTech (RAID) |
| D30 | Aqua-Cloud + SCAYLE |
| D31 | Google Cloud graceful degradation |
| D32 | Panorama/ERP Research + Credencys |
| D33 | Erlang C + SQM FCR + Plumsense |
| D34 | Microsoft Entra External ID |
| D36 | Hershey + Panorama |
| D37 | SAP Activate + LeverX + Bayer/Blue Yonder |
| D39 | INOC + ServiceNow + GEODIS/Locus |