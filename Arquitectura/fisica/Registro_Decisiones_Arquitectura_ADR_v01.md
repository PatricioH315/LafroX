# Registro de Decisiones de Arquitectura (ADR)

> **Actualización 25-09-2026 — backend Laravel.** La arquitectura lógica (4.1) adoptó Laravel 13 sobre PHP 8.5. ADR-01, ADR-05, ADR-11, ADR-12 y ADR-14 se reformularon y quedan en estado *propuesta*; ADR-04, ADR-06, ADR-08 y ADR-13 ajustaron su implementación. El texto vigente es el de `SUBDOCUMENTO_4/Subdocumento_4_LateX/04_arquitectura_fisica/partes/14_m_decisiones_adr.tex`. Las secciones de este archivo que describen Django, workers Celery o una caché de identidad de 8 h quedan como registro histórico de la evaluación anterior y no rigen.

## Distribuidora Puelche S.A. — Licitación TFEP-01/2026 (Caso 02 — Logística)

| Atributo | Valor |
|---|---|
| Documento | ADR-01 … **ADR-15** (formato MADR) |
| Versión | **v02** |
| Estado | En revisión interna — decisiones **Aprobadas** |
| Fecha | 2026-09-05 · **actualizado 2026-09-06** |
| Autor | Arquitecto de Solución (LafroX) |
| Marco de referencia | TOGAF · ISO/IEC/IEEE 42010 (RT-02.03) · Arquitecturas limpias |
| Documentos de origen | **`Arquitectura_Logica_v6-2.md` v6.2 (decisiones D1–D15)**, `Requerimientos/decisiones.md` (40 decisiones), `Tabla_Emplazamiento_OnPremise_v06.md`, `Propuesta_Arquitectura_Cloud_Caso02_CLAUDE_v2.md` (v3.6), `Arquitectura_Fisica_Hibrida_Consolidada_Caso02_v02.md`, `Dimensionamiento_Infraestructura_OnPremise_v05.md` |

> **Cambios v01 → v02 (2026-09-06, cierre de la auditoría del Subdocumento 4).** (1) Se corrigen las cinco menciones a **Kong** en ADR-01, ADR-06 y ADR-11: la puerta de enlace decidida es **Amazon API Gateway** (D8, actualizada el 2026-09-05 para alinearse con la vista física). (2) Se incorporan **ADR-13 (puerta de enlace de servicios)**, **ADR-14 (plataforma de observabilidad)** y **ADR-15 (gestión de secretos)**, que existían como decisiones lógicas sin ADR propio, incumpliendo el apartado 7 del Subdocumento 4 y RT-02.04. (3) Se reapunta el documento de origen a la lógica vigente **v6.2** (antes citaba `Arquitectura_Logica_v2.md`, inexistente).
| Empresa proponente | *Pendiente de definir (nomenclatura Art. 43.3)* |

> **Finalidad.** Cada ADR fundamenta y defiende una elección arquitectónica clave con el mismo rigor que un informe de ingeniería: contexto cuantificado desde el caso, alternativas reales de mercado evaluadas, criterio de selección técnico-económico (TCO, equipo de TI de 4 personas del CLIENTE, latencia, resiliencia), decisión precisa y sus trade-offs con mitigaciones. La **trazabilidad normativa** usa códigos exactos de las Bases Técnicas Transversales (RT-cc.nn), de las Bases Administrativas (BA Art. n°) y de los capítulos del Caso 02, y se enlaza con las decisiones de la Arquitectura Lógica v1 (Dn) y del registro de decisiones del caso (Decisión 16.1 N°).

---

## Índice de decisiones

| ADR | Título | Estado | Decisión relacionada |
|---|---|---|---|
| [ADR-01](#adr-01--estilo-arquitectónico-monolito-modular-vs-microservicios) | Estilo arquitectónico: monolito modular (Laravel 13 / PHP 8.5; Django queda como alternativa descartada) | Propuesta | D5 (AL v1) |
| [ADR-02](#adr-02--conectividad-y-redundancia-wan-starlink-leo--sd-wan) | Conectividad y redundancia WAN: Starlink LEO + SD-WAN | Aprobado | Decisión 16.1 N° 26 |
| [ADR-03](#adr-03--modelo-de-despliegue-híbrido-borde-operacional-on-premise--nube-aws) | Modelo de despliegue híbrido (Art. 16) | Aprobado | D7 (AL v1) · Decisión 16.1 N° 17 |
| [ADR-04](#adr-04--persistencia-políglota-por-dominio) | Persistencia políglota por dominio (CAP) | Aprobado | D2/D4 (AL v1) · Decisión 16.1 N° 18 |
| [ADR-05](#adr-05--mensajería-asíncrona-broker-local--colas-nube) | Mensajería asíncrona: RabbitMQ local + SQS FIFO con sobre JSON y colas separadas para trabajos Laravel | Propuesta | D4 (AL v1) |
| [ADR-06](#adr-06--identidad-y-autenticación-híbrida-modelo-b) | Identidad híbrida (Modelo B): Keycloak | Aprobado | D6 (AL v1) · Decisión 16.1 N° 34 |
| [ADR-07](#adr-07--estrategia-de-movilidad-de-terreno-nativa-android) | Movilidad de terreno: nativa Android (Kotlin) | Aprobado | decisiones.md N° 19 |
| [ADR-08](#adr-08--destino-del-wms-legado-de-2013) | Destino del WMS legado de 2013 | Aprobado | Decisión 16.1 N° 14 |
| [ADR-09](#adr-09--estrategia-de-recuperación-ante-desastres-dr) | DR: activo-pasivo warm standby multi-región | Aprobado | Decisión 16.1 N° 27 |
| [ADR-10](#adr-10--almacenamiento-on-premise-y-niveles-raid) | Almacenamiento on-premise y niveles RAID | Aprobado | Decisión 16.1 N° 28 |
| [ADR-11](#adr-11--integración-b2b--edi-con-supermercados) | Integración B2B/EDI: hub GS1 con capa anticorrupción y AS2 en AWS Transfer Family | Propuesta | RF-12 · RF-01.10 |
| [ADR-12](#adr-12--absorción-del-peak-de-septiembre-y-perfil-no-plano) | Absorción del peak de septiembre (cómputo elástico por perfil PHP) | Propuesta | Decisión 16.1 N° 30 |
| [ADR-13](#adr-13--puerta-de-enlace-de-servicios-amazon-api-gateway) | Puerta de enlace de servicios: Amazon API Gateway | Aprobado | D8 (AL v6.2) |
| [ADR-14](#adr-14--plataforma-de-observabilidad-única-otel--amp--cloudwatch--x-ray) | Observabilidad: plataforma única con emisión on-premise (OpenTelemetry PHP) | Propuesta | D14 (AL v6.2) |
| [ADR-15](#adr-15--gestión-de-secretos-servicio-administrado-en-lugar-de-gestor-autoalojado) | Gestión de secretos: servicio administrado | Aprobado | D13 (AL v6.2) · SEC-01 |

---

# ADR-01 — Estilo Arquitectónico: Monolito Modular vs. Microservicios

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisiones relacionadas:** D5 (Arquitectura Lógica, 2026-09-03, confirmada 09-04); **D8 (Amazon API Gateway, actualizada 2026-09-05 — ver ADR-13)**; **D14 (observabilidad de plataforma única, 2026-09-06 — ver ADR-14)**.
- **Trazabilidad normativa:** BTT **RT-02.02** (arquitectura modular, fronteras explícitas, despliegue independiente de componentes críticos) · BTT **§2.3** (la **sofisticación no reemplaza la pertinencia**: microservicios sin volumen que los justifique = error de ingeniería) · **RT-02.01** (8 capas) · **RT-02.03** (ISO/IEC/IEEE 42010) · **RT-09.05** (cuello de botella) · **BA Art. 16** (híbrido) · Caso 02 Cap. 14.2/15 (volumetría) · **RNF-19.01–04** (capacidad, escalado, cuello de botella, pruebas 1,5×).

### 1. Contexto y Problema
La carga del caso es transaccional y concentrada, pero **no plana**: ~31.000 pedidos/mes y 260.000 líneas/mes sobre 14.200 clientes y 8.400 productos, con un **peak de ~105 TPS** en la ventana de despacho (dimensionamiento: ~20 TPS confirmación de picking con 120 terminales, ~8 TPS preventa, ~35 TPS movimientos + sincronización, burst ×3). Pérdidas operacionales traducibles a dinero: conteo cíclico con 2,3 % de diferencia, merma por vencimiento 1,7 % del inventario, OTIF 82,4 % contra meta 95 % y $4,2 millones/mes de descuadre de caja. El equipo de TI del CLIENTE tiene **4 personas** para operar la solución completa durante 36 meses de Operación.

### 2. Alternativas Evaluadas
| Alternativa | Descripción | Soporte a escala (~105 TPS) | Equipo de 4 TI | Complejidad de operación | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Monolito modular (Django 5.x LTS, Python 3.12)** | Único despliegue de proceso con módulos internos (apps Django por dominio: WMS, preventa, distribución, trazabilidad, portal), **Amazon API Gateway** en la frontera (ADR-13), workers Celery para asincronía | Suficiente: 6 tareas Fargate en peak absorben 105 TPS con headroom ×1,5 | 1 framework, 1 lenguaje, 1 artefacto CI/CD; curva de reposición corta | Baja: un despliegue por ambiente, rollback simple, observabilidad OTel única | **Ganadora** |
| **B. Microservicios en Kubernetes (EKS)** | 20+ servicios acoplados a lo operacional (bodega, reparto, preventa, telemetría, facturación), mesh Istio, 3+ nodos por AZ | Sobra capacidad operativa para 105 TPS | Inviable: cluster operado por 4 personas (9–13 planos de control, versionado de contratos, backing services por dominio) | Alta: 2-3 SRE dedicados, curva de despliegue semanal, lock-in de operadores | Rechazada (BTT §2.3: volumen no la justifica) |
| **C. Monolito "clásico" sin límites de módulos (refactor del WMS 2013)** | Continuidad sobre el monolito actual sin fronteras de contexto ni despliegue independiente | Cumple hoy, no escala a multi-sitio | N/D (proveedor desaparecido, sin soporte) | Alta (deuda estructural) | Rechazada (viola RT-02.02) |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **Escala real (BTT §2.3):** para 31.000 pedidos/mes y **105 TPS de diseño**, el costo de coordinación de 20 servicios supera cualquier ganancia. El umbral donde los microservicios se justifican (típicamente >10³–10⁴ TPS, equipos de 5+ por dominio) está **dos órdenes de magnitud** por encima del caso.
- **Equipo de 4 personas (RT-02.02/RT-02.03):** un monolito modular tiene **1 artefacto, 1 pipeline, 1 proceso**: la reposición de personal y la mantención son lineales. EKS exige 9–13 componentes de plano de control (Kube-apiserver, etcd, Ingress, autoscaler, RBAC, CNI, mesh…) más 20 servicios; el costo fijo de operarlo supera al de la nube usada.
- **Despliegue independiente (RT-02.02):** la modularidad del monolito se materializa en **procesos y tareas separables** —tarea `portal` (canal moderno, hito enero 2029), workers Celery (`celery-reconciliation`, `celery-erp-sync`), shipper de colas— que escalan y se despliegan de forma independiente sin particionar el dominio.
- **TCO (56 meses):** A y B convergen en cómputo AWS, pero B agrega ~3 nodos EKS dedicados (≈ USD 1.200–1.600/mes) + SRE; A escala con Fargate (2→6 tareas) solo en septiembre (ADr-12). El diferencial B−A se estima en **USD 40.000–70.000 en 56 meses** por infraestructura y soporte, sin beneficio funcional neto.
- **Latencia/resiliencia:** el monolito modular en nube + borde local (ADR-03) cumple RNF-05.01 (≤1 s) y RNF-02.01 (24 h) porque lo que corre local es el mismo kernel WMS; particionar en servicios no aporta resiliencia adicional y añade saltos de red.

### 4. Decisión Adoptada
**Monolito modular en **Django 5.x LTS** sobre **Python 3.12**, con apps Django por dominio y límites de contexto explícitos (fundamentos de DDD y módulos de la Arquitectura Lógica v1), desplegado en **ECS Fargate** (tarea `web` + tarea `portal` + workers Celery), con **Amazon API Gateway** (D8 · ADR-13), observabilidad **OpenTelemetry sobre plataforma única en nube** (D14 · ADR-14) y borde local por sitio (ADR-03). Los módulos **críticos** (WMS offline, shipper de reconciliación, workers ERp-sync, tarea portal) se despliegan **de forma independiente** en procesos separados, satisfaciendo RT-02.02 sin adoptar microservicios.

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Riesgo de acoplamiento entre apps si no se respetan los límites | Deuda estructural intrínseca al monolito | Architecture Fitness Functions (ArchUnit/Django: contratos de módulo) en CI; revisión por módulo (RT-02.01) |
| Un fallo de proceso puede amplificarse a todo el despliegue | Golpe de blast radius mayor que en microservicios | Separación en tareas/workers; health checks ALB; retry/backoff; observabilidad por `transaction_id` (D9) |
| Escalado vertical limitado del monolito | El peak se absorbe con más réplicas de la misma imagen | Auto-scaling predictivo+reactivo del peak de septiembre (ADR-12, 2→6 tareas) |
| Menor "trendiness" frente a la evaluación técnica | La BTT §2.3 **penaliza** microservicios injustificados | Documentación explícita del análisis de escala/TCO (este ADR) como evidencia de pertinencia |

---

# ADR-02 — Conectividad y Redundancia WAN: Starlink LEO + SD-WAN

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** Decisión 16.1 N° 26 (redundancia de enlace de cada sitio).
- **Trazabilidad normativa:** BTT **RT-03.17** (enlace redundante con caminos y proveedores distintos, conmutación ≤ 5 min) · **RT-03.10** (autonomía 24 h) · **RT-03.19** (edge) · **RNF-13.01** (autonomía 24 h CD / 14 h terreno) · **RNF-13.07** (enlace redundante ≤ 5 min) · **RNF-13.08** (ancho de banda dimensionado) · **RT-10.05** (ventana crítica 05:30–07:00, indisponibilidad cero) · Caso 02 §6.12/§8 (cortes de fibra, Concepción sin respaldo, Los Ángeles sin señal en madrugada) · BA Art. 16.

### 1. Contexto y Problema
La operación depende del enlace de datos en horarios en que no existe plan manual (Restricción N° 1: **indisponibilidad cero 05:30–07:00**). Verificado en el caso:
- **Talca:** fibra se corta **4 veces al año** sin enlace de respaldo; la bodega debe aguantar 24 h sin enlace.
- **Concepción:** no tiene respaldo alguno.
- **Cross-docks (Curicó, Chillán, Los Ángeles):** conectividad exclusivamente por red móvil; **Los Ángeles pierde señal intermitentemente entre las 03:00–05:00**, exactamente su ventana de operación de 3 h.
- Impacto económico: un día sin despacho de la mañana = operación caída (96 camiones).

### 2. Alternativas Evaluadas
| Alternativa | Descripción | Cobertura Los Ángeles 03:00–05:00 | Cumple RT-03.17 (≤5 min, caminos distintos) | Costo 56 meses (referencial) | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Fibra + LTE + Starlink LEO con SD-WAN (tri-camino)** | Starlink como principal en cross-docks y respaldo en CDs; LTE dual (2 proveedores); SD-WAN con conmutación automática y BGP | Cobertura confirmada por constelación LEO (independiente de torres 4G) | Sí: 3 caminos, 2 proveedores LTE distintos + satelital | CAPEX $2.012.500 CLP + OPEX $50.400.000 CLP (56 m) = **$52.412.500 CLP (~USD 58.236)** (cotización 5 sitios) | **Ganadora** |
| **B. Fibra + LTE 4G puro** | Redundancia solo terrestre (fibra + 4G/Cat-12 femto backhaul) | No: en Los Ángeles la torre 4G falla justo en la ventana | Parcial: dos caminos pero el radio comparte tecnología física de torres | Sin CAPEX satelital; LTE puro ~USD 20–30 K en 56 m | Rechazada (no cierra el caso Los Ángeles ni el "sin red de respaldo" de Concepción) |
| **C. Satélite GEO tradicional (VSAT)** | Enlace de órbita geoestacionaria | Latencia 500–700 ms de ida y vuelta; débil en lluvia | Sí en camino, pero RTT penaliza RT-03.11/RNF-05.01 | Superior a LEO (equipos terminales GEO) | Rechazada (latencia y costo) |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **Riesgo funcional:** el único escenario que B no resuelve —señal móvil intermitente en Los Ángeles 03:00–05:00— es el que el caso declara crítico. La alternativa A aporta un **camino físicamente independiente de las torres 4G** (constelación LEO) y de las trincheras de fibra.
- **RT-03.17/RNF-13.07:** conmutación automática ≤ 5 min por diseño SD-WAN (detección de pérdida < 5 s, failover < 30 s según práctica de diseño del sitio); la redundancia de caminos es de física distinta (fibra → satelital → LTE), no solo de proveedor.
- **Ventana crítica (RT-10.05):** el despacho 05:30–07:00 no depende de un único medio; el tri-camino convive con la autonomía local de 24 h (RNF-13.01) para el caso de pérdida total (RT-03.10).
- **TCO:** la oferta Starlink (5 sitios, 56 meses) es **USD ~58.236**; frente a LTE puro que **no cumple el requisito**, el costo se justifica como prima de resiliencia del servicio crítico (costo de un día sin despacho >> costo del enlace). FinOps: CAPEX unitario bajo ($350.000 CLP/kit), reposición 15 % por ciclo de vida (RT-08.13).
- **Equipo de 4 TI:** Starlink Enterprise gestionado (cero mantención de infraestructura de radio), SD-WAN con políticas centralizadas; sin ingeniería de redes satelitales in-house.

### 4. Decisión Adoptada
**Tri-camino WAN por sitio con SD-WAN:** (1) fibra (enlace principal en Talca y Concepción), (2) **Starlink Enterprise LEO** —principal en los 3 cross-docks (Curicó, Chillán, Los Ángeles) y respaldo automático en los 2 CD— y (3) **LTE dual** (2 proveedores) con módulo 4G Cat-12. Conmutación automática < 30 s entre caminos, documentada en `Tabla_Emplazamiento_OnPremise_v06 §D-03/D-04/D-06` y con planes/precios **declarados en la oferta** (T-11 C27 · T-12 RT-08.13). Los cross-docks salen por Starlink directo a SQS/IoT/SSM (configuración crítica) y sincronizan detalle a Talca por AMQPS entre brokers (RT-03.11).

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Costo recurrente de planes Starlink | La prima de conectividad satelital es el mayor gasto de red | Planes tier por sitio (1 TB CDs / 500 GB cross-docks); revisión trimestral FinOps (RT-03.06) |
| Skyline/interferencia puntual en cielos despejados (lluvia fuerte) | Degradación momentánea de throughput | SD-WAN con conmutación por política; LTE como tercer camino independiente |
| Dependencia de tarifas/dólar en 56 meses (TCM USD 900 CLP) | Variación cambiaria en OPEX | Cotización con supuesto de reposición y cláusula de revisión de tarifas; registro en supuestos |
| Sostenimiento de 5 kits (RT-08.13) | Gestión de repuestos | 15 % de reposición cotizado; ciclo de vida en Sección 4.1 de la Tabla v06 |

---

# ADR-03 — Modelo de Despliegue Híbrido: Borde Operacional On-Premise vs. Nube AWS

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisiones relacionadas:** D7 (AL v1: híbrido + multi-zona + IaC + Zero Trust); Decisión 16.1 N° 17 (asignación de componentes).
- **Trazabilidad normativa:** **BA Art. 16.1–16.4** (híbrido obligatorio, carga principal en nube, criterios 16.2, exigencias 16.3/16.4) · **RT-03.01** (región primaria/secundaria) · **RT-03.02** (multi-AZ) · **RT-03.10** (autonomía) · **RT-03.19** (edge) · **RNF-02.01** (24 h) · **RNF-05.01** (≤ 1 s en cámara) · **RNF-05.02** (guantes −22 °C) · Caso 02 Cap. 6 (cámara sin cobertura) y Cap. 16.1.

### 1. Contexto y Problema
Tres hechos confluyen: (a) el Art. 16 exige **carga principal en nube pública + componentes on-premise** (inadmisible solo-nube o solo-on-prem); (b) la cámara de congelado a **−22 °C no tiene cobertura de señal** y el picking exige **≤ 1 s** de confirmación (RNF-05.01), inviable con RTT de 40–80 ms hacia la nube más procesamiento remoto; (c) la bodega debe operar **24 h sin enlace** (RNF-02.01/RT-03.10). El perfil de carga es nocturno (22:00–06:00) y de madrugada (05:30–07:00).

### 2. Alternativas Evaluadas
| Alternativa | Descripción | RT-03.10 (24 h) | RNF-05.01 (≤1 s) | Art. 16.1 (carga en nube) | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Híbrido: WMS maestro on-prem + borde por sitio + nube AWS (carga principal)** | WMS y BD transaccional en Talca (maestro), borde edge en Concepción y cross-docks, nube para OLTP cloud, canal moderno, analítica, IoT, respaldo inmutable | Sí (autonomía local 24 h CD / 14 h terreno) | Sí (confirmación en el dispositivo local) | Sí | **Ganadora** |
| **B. Solo nube (WMS en AWS)** | Toda la operación en la nube | No: sin enlace, bodega muere en minutos | No: RTT + procesamiento no sostiene ≤1 s en cámara | No (no es híbrida) | **Inadmisible** (BA Art. 16) |
| **C. Solo on-premise (WMS maestro + todo local)** | Centro de datos propio con todo el cómputo | Sí | Sí | No (no es híbrida) | **Inadmisible** (BA Art. 16) |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **Cumplimiento normativo:** solo A satisface Art. 16 en sus cuatro numerales (16.1 híbrido, 16.2 justificación por componente, 16.3 exigencias de nube, 16.4 exigencias on-premise). Tabla maestra de emplazamiento en `Tabla_Emplazamiento_OnPremise_v06 §1.0` (36 componentes).
- **Latencia (RNF-05.01):** el borde local ejecuta la confirmación de picking en el propio sitio; la alternativa nube añade ≥40–80 ms RTT y procesamiento remoto, por encima del umbral de 1 s en la cámara.
- **Autonomía (RNF-02.01/RT-03.10):** el diseño del caso exige supervivencia sin enlace; el maestro local con réplica cloud (DMS CDC, RPO ≤ 15 min) da continuidad (ADR-09) sin depender de la WAN durante el corte.
- **TCO/equipo:** el cómputo local se acota a lo imprescindible (23 componentes on-premise/híbrido), el resto se delega a servicios administrados AWS (ADR-12) — menor costo fijo que un DC propio y menor riesgo que una operación 100 % nube.
- **Carga principal en nube (Art. 16.1):** canal moderno (portales), OLTP cloud, ingesta IoT, analítica/BI, respaldo inmutable y DRP viven en AWS (sa-east-1, DRP us-east-1 — RT-03.01).

### 4. Decisión Adoptada
**Arquitectura híbrida obligatoria con borde operacional on-premise:** WMS maestro + BD transaccional en Talca (VM-01/VM-02), edge autónomo en Concepción (VM-C01/VM-C02), mini-WMS en cross-docks (E-01), y máxima utilización de AWS administrado (ECS Fargate, Aurora, DynamoDB, IoT Core, S3, Redshift/QuickSight) para la carga principal. Detalle por componente en `Tabla_Emplazamiento_OnPremise_v06 §1.0` y `Cloud v3.6`.

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Dos dominios operativos que mantener (on-prem + nube) | Mayor superficie que la nube pura | IaC total (RT-03.03), SSM Agent (gestión sin puertos entrantes), Zero Trust (D7) |
| El maestro local exige administración de BD/hardware | Costo de operación on-premise | Dimensionamiento con headroom ×1,5 y RAID 10 (ADR-10); NOC 24×7 (RNF-21.01) |
| La identidad debe sobrevivir offline | Despliegue de caché local de solo lectura | Modelo B (ADR-06), sin maestro local a promover |
| La réplica cloud aumenta costos de AWS | DRP por réplica continua | Aurora replicada solo para lo crítico (A-01/A-02); respaldos 3-2-1-1-0 (ADR-09) |

---

# ADR-04 — Persistencia Políglota por Dominio

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisiones relacionadas:** D2 (series de tiempo condicionadas al muestreo, consolidado en OLAP); D4 (nube AWS + PostgreSQL/Redis/Aurora/DynamoDB/S3+Redshift); Decisión 16.1 N° 18 (motor por dominio, RT-05.02).
- **Trazabilidad normativa:** BTT **RT-05.02** (paradigma, garantías transaccionales y posición CAP por dominio) · **RT-05.01** (diccionario de datos) · **RT-05.11–05.15** (migración/volúmenes) · **RNF-09.01** (retiro < 2 h) · **RNF-09.02** (retención 5 años) · **RNF-11.02** (OLAP desacoplado del OLTP) · RSA **D.S. 977/96** (retención legal de trazabilidad) · Caso 02 Cap. 16.1/16.2 y Cap. 4.9.

### 1. Contexto y Problema
Cada dominio tiene exigencias distintas de consistencia, volumen y retención: pedidos/inventario/trazabilidad demandan **ACID** y reconciliación determinista tras cortes; la ingesta de sensores y telemetría es **escritura masiva de baja latencia**; las series de tiempo (temperatura de cámara y camión) requieren compresión y consulta por rango; la analítica exige columnar separado para no degradar picking; y la retención sanitaria impone **5 años de trazabilidad** (piso legal) con 6 meses adicionales por vida útil. Un único motor no puede cumplir las cuatro posiciones CAP sin sacrificar desempeño.

### 2. Alternativas Evaluadas
| Dominio | Alternativa A | Alternativa B | Alternativa C | Ganador |
|---|---|---|---|---|
| Transaccional (pedidos, inventario, trazabilidad, facturación) | PostgreSQL ACID (CP) | MySQL | MongoDB (AP) | **A — PostgreSQL** (CP: consistencia inmediata exigida por operación offline y reconciliación) |
| OLTP cloud + réplica DRP WMS | Aurora PostgreSQL | RDS MySQL | DocumentDB | **Aurora** (administrado, failover <30 s, PITR 35 días, réplica WAL) |
| IoT raw (senores, telemetría) | DynamoDB (AP) | PostgreSQL puro | Kafka+Elasticsearch | **DynamoDB** (escritura serverless <10 ms p99, TTL 30 días) |
| Series de tiempo (frío) | **Capa OLAP: S3 Parquet + Redshift Serverless (columna)** | InfluxDB | Particionado manual | **OLAP (S3+Redshift)** (adoptado según muestreo — D2; sin segundo motor; consolidado 5 años) |
| Analítica / BI / lake 5 años | S3 + Redshift Serverless + QuickSight | Snowflake | Athena sobre S3 puro | **S3+Redshift+QuickSight** (columnar desacoplado, RNF-11.02) |
| Retención legal / respaldo inmutable | S3 Object Lock / Glacier + Backup Vault | Cinta/tape local | NAS local puro | **S3 Object Lock/Glacier** (inmutabilidad WORM, custodia RT-06.26+27) |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **RT-05.02 y CAP:** la posición se declara por dominio: transaccional **CP** (consistencia inmediata; la operación offline y la reconciliación vuelta a línea lo exigen), IoT raw **AP** (eventual, TTL corto), series de tiempo **AP columnar en la capa OLAP**, analítica **AP columnar**. Declarar la posición evita el error de elegir un motor "para todo".
- **Volumen (RT-05.15):** ~31.000 pedidos/mes, 260.000 líneas, 2,4 M unidades y telemetría de 28 sensores + 18 termógrafos → persistencia manejable en PostgreSQL (índices + PostGIS para georreferencia de rutas) con DynamoDB absorbiendo el pico de IoT sin saturar el transaccional (RNF-11.02).
- **Trazabilidad (RNF-09.01/09.02, D.S. 977/96):** el registro de eventos por lote (EPCIS GS1, decisión 16.1 N° 35) se conserva en PostgreSQL (5 años) y su respaldo inmutable replica el piso legal; la réplica Aurora da RPO ≤15 min.
- **Equipo de 4 TI:** tres motores administrados o de bajo mantenimiento (PostgreSQL/Aurora, DynamoDB, Redshift Serverless) — sin motores dedicados exóticos (InfluxDB descartado: segundo motor a operar, D2). La serie de tiempo consolidada no requiere un motor adicional: vive en la capa OLAP (S3 Parquet → Redshift).

### 4. Decisión Adoptada
**Persistencia políglota por dominio:** PostgreSQL+PostGIS (transaccional WMS on-premise, CP), Aurora PostgreSQL (OLTP cloud + réplica DRP, failover <30 s), DynamoDB (IoT raw, TTL 30 días, AP), S3 (lake analítico 5 años) con Redshift Serverless y QuickSight (OLAP, incluye la serie de tiempo consolidada de temperatura), y S3 Object Lock/Glacier + Backup Vault para retención legal inmutable (RSA D.S. 977/96). Matriz CAP declarada y trazada a RT-05.02 en `Cloud v3.6 §4` y `decisiones.md N° 18/35`.

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Consistencia fuerte en el transaccional limita escalado horizontal de escritura | El volumen (~105 TPS) no lo justifica | Réplicas de lectura (2 Aurora readers) y partición lógica por instalación (RF-02.01/02.02) |
| DynamoDB eventual abre ventanas de lectura inconsistente cortas | Telemetría no es crítico de negocio | TTL 30 días + consolidado en la capa OLAP (S3 Parquet/Redshift, 5 años) con validación de rango |
| Amazonas de datos (S3) requiere gobierno | Costo y gobernanza del lake | Glue + catálogo y QuickSight con modelos aprobados; FinOps (RT-03.06) |
| Integración entre motores exige ETL | Latencia de analítica != OLTP | Batch nocturno y distribución de datos por dominio (RT-05.01) |

---

# ADR-05 — Mensajería Asíncrona: Broker Local (RabbitMQ) + Colas Nube (SQS FIFO / EventBridge)

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** D4 (AL v1, capa de mensajería); shipper en VM-03 (D-AL-03).
- **Trazabilidad normativa:** BTT **RT-02.06** (idempotencia) · **RT-02.07** (deduplicación) · **RT-03.12** (sincronización/reconciliación tras reconexión) · **RT-03.10** (autonomía) · **RNF-07.01** (sincro < 10 min) · **RNF-13.01** (24 h) · Zero Trust (BA Art. 21) · Caso 02 Cap. 16.1 (reglas de reintento/devolución).

### 1. Contexto y Problema
El caso exige **orden estricto y sin pérdida** en la cadena pedido→despacho→cobranza (una línea de preventa fuera de orden rompe la reconciliación determinista), pero la operación transcurre **offline**: bodega 24 h, terreno 14 h. Además, todo el tráfico debe ser **outbound** (Zero Trust: sin conexiones entrantes al on-premise). REST síncrono no sobrevive a un corte a mitad de ventana; Kafka aporta orden y durabilidad pero exige operación y no resuelve el broker local por sitio.

### 2. Alternativas Evaluadas
| Alternativa | Orden estricto | Buffer offline 24 h | Zero Trust (outbound) | Equipo de 4 TI | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. RabbitMQ local + SQS FIFO/EventBridge (nube), shipper** | SQS FIFO por `group_id` (pedido/entidad) garantiza orden | RabbitMQ 24 h (~3 M mensajes) en cada sitio | Shippper VM-03 publica por HTTPS/443 (VPC Endpoint SQS), sin entrantes | RabbitMQ es maduro y liviano; SQS/EventBridge administrados | **Ganadora** |
| **B. Kafka (clúster local + MSK nube)** | Orden por partición | Posible local, pero requiere clúster mínimo 3 brokers por sitio | Requiere conectividad zookeeper/plano de control | Elevada: 3+ brokers por sitio + MSK; operación de retención y rebalances | Rechazada (escala y operación no la justifican) |
| **C. REST síncrono puro** | N/D | No: cae con la WAN | Parcial | Baja | Rechazada (viola RT-03.10/RNF-13.01) |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **Resiliencia (RT-03.10/RNF-13.01):** el broker local retiene transacciones y telemetría durante el corte y las reproduce al reconectar; el shipper publica en **orden cronológico e idempotente** (idempotency keys, RT-02.06/02.07) a la cola FIFO.
- **Reconciliación determinista (RT-03.12):** `celery-reconciliation` procesa la cola al recuperar el enlace; claves de idempotencia evitan duplicados (RT-02.07) y el orden de publicación por entidad garantiza consistencia en el maestro.
- **Zero Trust (BA Art. 21):** SQS FIFO se consume via VPC Endpoint SQS/PrivateLink (HTTPS/443); AMQPS 5671 queda solo entre brokers on-premise (cross-dock → Talca). No se abren puertos entrantes.
- **TCO/equipo:** RabbitMQ (este) + SQS/EventBridge (administrados) > Kafka (+MSK) para 105 TPS; el costo operativo de operar clústeres Kafka en 5 sitios es desproporcionado para 4 personas.

### 4. Decisión Adoptada
**Capa de mensajería híbrida:** RabbitMQ (A-03) como broker de colas offline en cada sitio (buffers 24 h), con **shipper en VM-03 (modo `wms_only`)** que publica el buffer hacia **SQS FIFO** (VPC Endpoint / HTTPS 443) con idempotencia; **EventBridge** como bus de eventos de negocio (eventos que disparan ERP-sync, alertas, auditoría) y **AWS IoT Core (MQTT)** para la ingesta edge (ADR-04/ADR-12). Workers `celery-reconciliation` y `celery-erp-sync` procesan en nube. Registrado en `Cloud v3.6 §3.1/§7.9` y `Consolidado §3.4/D-AL-03`.

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Dos brokers (local/nube) con estrategias distintas | Más superficie que un solo bus | Contratos de eventos versionados (AsyncAPI, RT-05.16/17); matriz de integración (Consolidado §3.5) |
| Posible duplicado en el flujo local→nube | Garantías "at-least-once" | Idempotency keys + procesamiento deduplicado (RT-02.06/07); buffer con ACK solo tras commit exitoso |
| Volume de mensajes en septiembre (2×) | Crecimiento de cola | SQS y broker dimensionados; auto-escalado de workers (ADR-12) |
| Kafka descartado | Menor capacidad de reprocesamiento histórico | S3 como foso de eventos (reproceso por replays controlados, ADR-04) |

---

# ADR-06 — Identidad y Autenticación Híbrida (Modelo B): Keycloak IdP Maestro en Nube + Caché Local de Solo Lectura

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisiones relacionadas:** D6 (AL v1, 2026-09-04: Keycloak IdP maestro, Modelo B); Decisión 16.1 N° 34 (credenciales de usuarios externos sin correo).
- **Trazabilidad normativa:** BTT **RT-12.10** (aprovisionamiento ≤ 24 h) · **RT-12.11** (autenticación en perfil operacional: guantes, rotación 38 %, dispositivos compartidos) · **RT-12.12** (credenciales de externos sin correo) · **RT-03.10**/RNF-13.01 (offline 24 h CD / 14 h terreno) · **BA Art. 22** (MFA para acceso externo) · **RF-15.01–15.05** (identidad centralizada) · **RF-06.08** (OTP conductores externos ≤ 2 min) · Caso 02 Cap. 16.1 N° 34.

### 1. Contexto y Problema
La operación exige autenticación **incluso sin enlace**: la bodega trabaja 24 h y el terreno 14 h desconectados, con 62 preventistas y ~200 conductores (de 10 transportistas externos) **sin correo corporativo**, dispositivos compartidos entre turnos y rotación de personal de preparación de 38 % anual. Un IdP solo-nube paraliza la bodega ante un corte; un maestro local tradicional (AD) duplica la administración de identidad y crea un maestro a promover.

### 2. Alternativas Evaluadas
| Alternativa | Offline 24 h/14 h | Externos sin correo (OTP) | Un solo maestro (sin promoción) | Rechazo/Aceptación |
|---|---|---|---|---|
| **A. Keycloak IdP maestro en nube (ECS Fargate) + caché local de solo lectura TTL 8 h + offline tokens (8 h/14 h)** | Sí (validación local de firma OIDC) | Sí (OTP emitido por jefe de flota, RF-06.08) | Sí (Modelo B, D6) | **Ganadora** |
| **B. IdP nube puro (ej. Cognito-only)** | No: sin red, sin autenticación | Parcial (depende de conectividad) | Sí | Rechazada (paraliza CD/terreno, RT-03.10) |
| **C. Active Directory tradicional on-premise** | Sí | Parcial (sin flujo OTP para externos sin dominio) | No: maestro local a promover en DR | Rechazada (complejidad de federación + DR de identidad) |
| **D. Cognito como dependencia** | No | Parcial | — | Rechazada (D6: Cognito solo alternativa; descendencia de dependencia) |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **Autonomía (RT-03.10/RNF-13.01):** la caché local (A-05: VM-05 Talca, VM-C03 Concepción) valida localmente la **firma OIDC** y mantiene sesiones hasta 24 h CD / 14 h terreno; el token offline se renueva al inicio del turno en cobertura, de modo que la ventana offline siempre cubre la jornada (8 h bodega / 14 h reparto-preventa) **sin autenticación en ruta**.
- **Autoridad única (D6):** todas las escrituras viven en el IdP maestro de la nube; los cambios de alta/baja/roles se propagan por **export/import del Realm cifrado vía S3 (outbound)** con Δ ≤ 8 h (TTL) y baja efectiva SCIM ≤ 24 h (RT-12.10). No existe maestro local a promover ⇒ **DR de identidad = misma autoridad en nube** (no depende de switchover).
- **Externos (RT-12.11/12.12):** OTP de un solo uso para conductores (RF-06.08, ≤ 2 min, sin correo) y credencial inicial en sesión de dotación; MFA para todo acceso externo y privilegiado (Art. 22).
- **Equipo de 4 TI:** Keycloak administrado (Fargate) + federación OIDC con **Amazon API Gateway** (ADR-13); sin sincronización de directorio propietario.

### 4. Decisión Adoptada
**Modelo B de identidad (D6):** **Keycloak IdP maestro en AWS (ECS Fargate, 2 tareas Multi-AZ, backend Aurora)** con **caché local de solo lectura TTL 8 h** en VM-05/VM-C03 y **offline access tokens por perfil** (8 h bodega, 14 h reparto/preventa). Sincronización del Realm cifrado por S3 (outbound, Zero Trust); MFA OIDC para externos; OTP para conductores externos. Reconciliado en `Cloud v3.6 §3.3/§5.4/§7.3` y `Consolidado §5/D-AL-01/02`.

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Revocación no es inmediata en el borde (Δ ≤ 8 h TTL) | Ventana de revocación por TTL | SCIM ≤ 24 h; baja reforzada por matrícula de activos y MDM (bloqueo de terminal) |
| El Realm viaja por S3 (outbound) | Exposición del cifrado durante el traslado | Cifrado KMS del objeto; solo lectura de cachés; sin claves privadas locales |
| OTP para externos depende del jefe de flota | Fricción en cambio sin aviso | Emisión previa a la ventana; listado de contingencia; rotación diaria (RF-12.21) |
| Falla del IdP maestro deja sin altas/bajas | Degradación administrativa | Identidad en nube multi-AZ + us-east-1 DRP (ADR-09); las evaluaciones locales siguen operando |

---

# ADR-07 — Estrategia de Movilidad de Terreno: Aplicación Nativa Android (Kotlin)

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** decisiones.md N° 19 (nativa vs. híbrida vs. PWA).
- **Trazabilidad normativa:** BTT **RT-12.11** (autenticación en perfil operacional) · **RT-13.08** (interfaz de terreno: guantes térmicos, −22 °C, lluvia, 34 °C, una mano, turno sin conexión) · **RT-03.19** (edge) · **RNF-05.02** (guantes −22 °C) · **RNF-05.03** (curva de aprendizaje ≤ 2 h) · **RNF-06.01** (14 h sin señal) · **RF-03.02** (stock offline) · **RF-06.11/06.12/06.13** (QR/foto/impresora térmica) · Caso 02 Cap. 6 (cámara sin cobertura, turnos de 30 min).

### 1. Contexto y Problema
El terreno es el corazón de la operación: 62 preventistas, ~200 conductores y 120 terminales de bodega operando con **guantes térmicos a −22 °C**, **a una mano durante la descarga**, bajo lluvia, sol directo y **14 h sin señal**. Requiere escáner GS1, impresora térmica Bluetooth y POS móvil (PAX), y curva de aprendizaje ≤ 2 h. Una PWA no controla el SDK de escáner Zebra de forma confiable ni persiste un turno completo sin capa nativa; una híbrida (Flutter) agrega un runtime intermedio que degrada la interacción con periféricos industriales.

### 2. Alternativas Evaluadas
| Alternativa | Periféricos Zebra (DataWedge)/BT | Offline 14 h | UX guantes/1 mano/−22 °C | Curva ≤ 2 h | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Nativa Android (Kotlin), SQLite/Room + SDK Zebra DataWedge + scanner API** | Total (intent `com.symbol.datawedge`) | SQLite con sync deduplicada (RF-03.17) | Full control de la UI (botones grandes, táctil frente a guantes) | SÍ (flujos guiados) | **Ganadora** |
| **B. PWA (canal web)** | Limitado (Web Bluetooth parcial, sin DataWedge nativo) | Solo Service Worker con cuotas y poca fiabilidad para cámara/escáner | Media | Parcial | Rechazada para terreno; **adoptada para autoatención** del cliente (portal) |
| **C. Híbrida Flutter/React Native** | Puentes parciales, mantención de capa nativa | Posible pero con runtime intermedio | Media | Media | Rechazada (complejidad y rendimiento de periféricos) |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **Periféricos (RT-13.08/RF-06.13):** DataWedge (intents) entrega disparo de escáner GS1, CW (camera wedge) para QR (RF-06.11) y salidas a impresora BW Zebra — integraciones nativas estables que un runtime híbrido/PWA no garantiza.
- **Offline total (RNF-06.01/RT-03.19):** SQLite/Room persiste el turno completo (pedidos, POD con foto/firma, cobros, devoluciones) y sincroniza con deduplicación e idempotencia al reconectar (< 10 min, RNF-07.01); STock indicativo con antigüedad visible (RF-02.05) y resolución cronológica de conflictos (RF-02.05e).
- **Condiciones extremas (RNF-05.02/RT-12.11):** la UI nativa permite contraste alto, botones grandes, entrada por guantes (toque grueso), sin gestos complejos; dispositivos Rugged Zebra (EC55, TC58e, MC9400 Cold Storage) con Android 13+ y baterías de cámara/5G.
- **TCO:** una misma app nativa cubre preventa, reparto y bodega (parque de terreno de la Sección 4 de la Tabla v06); el costo de mantención de la plataforma nativa se asume como trade-off frente a las exigencias RNF (decisiones.md N° 19 documenta este trade-off).

### 4. Decisión Adoptada
**Aplicación nativa Android (Kotlin)** para preventa, reparto/cobranza y picking/recepción de bodega, con persistencia local **SQLite/Room**, SDK **Zebra DataWedge** (escáner GS1 + CW QR) y módulo de impresión Bluetooth (ZQ620) y POS (PAX). PWA (web) solo para la **autoatención del canal moderno** (portal, ADR-11). Dispositivos Rugged: EC55 (preventa), TC58e (reparto), MC9400 Cold Storage (cámara −22 °C), DS2208 (andén), penalizados por guantes/una mano (RNF-05.02).

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Dos stacks de UI (nativa Android + portal web) | Mayor mantención que una sola tecnología | Automatización de CI/tests (Appium), contratos API compartidos; la web cubre el canal sin offline |
| Versionado de app en parque de ~270 dispositivos (62 EC55 preventa + ~200 TC58e reparto + reservas; 174 MC9400 bodega) | Coordinación de despliegues de terreno | MDM (Gestión de Endpoints, F-03) con controles de distribución; actualizaciones en ventana sin operación |
| SQLite frente a sincronización concurrente | Conflictos de stock | Claves de idempotencia + reconciliación cronológica (ADR-05) |
| Dependencia de kits Android fabricantes (Zebra) | Ciclo de vida OS | Dispositivos con Android 13→18 Garage/Zebra; política de intercambio RT-08.13 |

---

# ADR-08 — Destino del WMS Legado de 2013

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** Decisión 16.1 N° 14 (reemplazar el WMS de 2013).
- **Trazabilidad normativa:** **RT-05.11–RT-05.15** (plan de migración por dominio, volúmenes y reversión) · **RT-03.10**/RNF-02.01 (24 h) · **RNF-05.01** (≤1 s) · Caso 02 Cap. 16.1 N° 14 (el CLIENTE delega expresamente la decisión) y Cap. 9 (dolores: conteo 2,3 %, merma 1,7 %, rasgos de WMS 2013) · estrategia azul-verde y reversión.

### 1. Contexto y Problema
El WMS de 2013 corre en Talca con **proveedor desaparecido** (sin soporte, sin roadmap), planillas impresas (conteo cíclico con 2,3 % de diferencia y ajustes sin investigación de causa), y no soporta multi-sitio ni operación de 24 h sin enlace. El CLIENTE **delega expresamente** en el proponente la decisión (Cap. 16.1 N° 14). Extenderlo arrastra el riesgo de fecha conocida: sin soporte, un incidente en la ventana crítica (05:30–07:00) no tendría plan B.

### 2. Alternativas Evaluadas
| Alternativa | Multi-sitio (RF-02.01/02.02) | Offline 24 h | Soporte y riesgo | Costo | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Reemplazo total en la Etapa 1** | Sí (topología configurable, consolidación multi-nodo) | Sí (RNF-02.01) | Proveedor nuevo con soporte contractual; conversión controlada | Mayor CAPEX, menor riesgo de operación | **Ganadora** |
| **B. Mantener/extender el WMS 2013** | No (arquitectura monocliente sin multi-sitio) | No | Proveedor desaparecido: sin parches ni soporte, un fallo = cero plan B en ventana crítica | Bajo CAPEX, riesgo operacional alto e ilimitado | Rechazada |
| **C. Coexistencia temporal (WMS 2013 + nuevo en un sitio)** | Parcial (solo mientras dure el puente) | — | Migración en olas reduce el riesgo | Medio | Complemento de la estrategia de despliegue (azul-verde), no fin último |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **Requisitos (RF-02.x):** slotting ABC, conteo cíclico ciego, picking FEFO dirigido, SSCC GS1, trazabilidad por lote — el WMS 2013 no los contempla ni los puede incorporar sin proveedor.
- **Riesgo operacional:** un sistema sin soporte expuesto a la ventana de indisponibilidad cero (RT-10.05) es un riesgo con fecha de impacto indefinido; el análisis de riesgos del caso lo califica como inaceptable frente al CAPEX del reemplazo.
- **Migración (RT-05.11–15):** por dominio y en ventanas sin operación: maestros completos, ventas/pedidos 3 años, inventario 2 años, trazabilidad 5 años, CxC abierta; convivencia con el ERP/GDE (que no se reemplaza) vía capa anticorrupción (ADR-11).
- **Reversión y despliegue:** estrategia **azul-verde** por ola y sitio, con umbrales de marcha blanca por oleada (RT-20.02/20.04) y plan de reversión para volver al WMS 2013 sin pérdida en caso de no superar los indicadores.
- **TCO 56 meses:** el costo de reemplazo se paga en la Etapa 1 y se amortiza con la reducción de 2,3 %→~0,3 % de diferencia de conteo y 1,7 %→<1 % de merma (objetivos de RF/planilla del Cap. 18) y con OTIF 82,4 %→95 %.

### 4. Decisión Adoptada
**Reemplazo total del WMS 2013 en la Etapa 1** por el **módulo WMS del monolito modular (ADR-01)** desplegado en Talca (maestro), Concepción (edge) y cross-docks (mini-WMS E-01), con migración por dominio (RT-05.11–15), oleadas por sitio y plan de reversión azul-verde documentado. El ERP administrativo/GDE **no se reemplaza** y se integra por la capa anticorrupción (ADR-11).

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Conversión de datos en ventanas sin operación | Ventana de corte por dominio | Migración nocturna por dominio con verificación de conciliación (RT-05.12/05.14) |
| Curva de aprendizaje del personal de bodega | Riesgo operacional en cutover | Marcha blanca por ola con certificación (RT-20.02/20.04); curva ≤ 2 h (RNF-05.03) |
| El ERP sigue existiendo | Dualidad de maestros durante la cohabitación | Capa anticorrupción (ADR-11) y catálogo de equivalencias (RF-12.03) |
| Costo de migración y reversiones | CAPEX de transición | Plan de reversión por ola; pruebas de restauración mensuales (RNF-20.07) |

---

# ADR-09 — Estrategia de Recuperación ante Desastres (DR): Warm Standby Activo-Pasivo Multi-Región

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** Decisión 16.1 N° 27 (modalidad activo-pasivo, RTO/RPO, cadencia de pruebas).
- **Trazabilidad normativa:** **RT-07.01** (declarar y justificar modalidad activo-activo vs. activo-pasivo) · **RT-07.07** (pruebas reales ≥ 2 veces/año con informe y medición de RTO/RPO) · **RNF-20.06** (RTO ≤ 4 h, RPO ≤ 15 min) · **RNF-20.07** (3-2-1-1-0) · **BA Art. 20** (continuidad y pruebas semestrales) · DRP local Talca→Concepción (RTO +1–2 h) · Caso 02 Cap. 16.1 N° 27.

### 1. Contexto y Problema
La ventana de despacho (05:30–07:00) no admite plan manual; una falla mayor del sitio primario debe recuperar el servicio con **RTO ≤ 4 h y RPO ≤ 15 min** (RNF-20.06) y probarse con conmutación real **al menos 2 veces al año** (RT-07.07/Art. 20). El sitio primario es Talca (WMS maestro on-premise); el respaldo secundario se apoya en la nube (replicación AWS) y en el borde autónomo de Concepción como DRP local.

### 2. Alternativas Evaluadas
| Alternativa | RTO/RPO | Complejidad operativa | Costo | Cumple RT-07.01 (justificación) | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Activo-pasivo warm standby multi-región (Aurora réplica DRP + DMS CDC)** | RTO ≤ 4 h / RPO ≤ 15 min | Media: promote documentado, pruebas semestrales | Réplica + DRP regional (us-east-1) | Sí | **Ganadora** |
| **B. Activo-activo (multi-maestro)** | RPO ~0 | Alta: conflictos de escritura y reconciliación continua entre nodos | 2× infraestructura transaccional + reconciliación | Justificable pero no necesario al volumen | Rechazada (costo/complejidad desproporcionados, RT-07.01) |
| **C. Backup en frío (bajo demanda)** | RTO > 24 h (restauración completa) | Baja | Baja | No cumple RTO ≤ 4 h | Rechazada |
| **D. Continuidad intrarregional en sa-east-1 (sin us-east-1)** | Falla de AZ o corrupción: RTO ≤ 4 h / RPO ≤ 15 min (multi-AZ + CDC) · **caída de toda la región sa-east-1: RTO 24–72 h** desde respaldo inmutable (S3 Object Lock/Backup Vault) | Media: restauración y rehidratación; cada 6–12 meses requiere prueba real | Réplica y respaldo solo dentro de sa-east-1; menor costo de salida que A | No cumple RTO ≤ 4 h ante falla regional (RNF-20.06) | **Contingencia condicionada**: solo si el CLIENTE rechaza la transferencia internacional (Art. 23) — no sustituye a A como plan base |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **RTO/RPO (RNF-20.06):** la réplica continua (DMS CDC) y la réplica de Aurora (WAL) mantienen RPO ≤ 15 min; el promote a la región DRP (us-east-1) más el DRP local Talca→Concepción (procedimiento documentado de 5 pasos, RTO +1–2 h) cumplen los cuatros horas.
- **RT-07.01:** activo-activo duplicaría la infraestructura transaccional y exigiría reconciliación de doble escritura (~105 TPS peak) sin beneficio medible frente al RTO comprometido; la modalidad activo-pasiva es proporcional al volumen (CAP consistente, ADR-04).
- **Pruebas (RT-07.07/Art. 20):** conmutación real semestral con informe de RTO/RPO efectivos y plan de corrección de brechas; consistente con la retención sanitaria y la operación continua.
- **Identidad (ADR-06):** el DR de identidad no exige conmutación local (el maestro está en la nube y las cachés A-05 siguen validando firmas): se elimina una clase entera de riesgos de DR.
- **Respaldo 3-2-1-1-0 (RNF-20.07):** copia primaria on-premise + réplica local (Concepción) + pierna cloud (S3 Object Lock/Backup Vault, inmutable) + offsite + prueba mensual de restauración y retención legal (ADR-04).
- **Falla de AZ vs. caída de región (alternativa D):** si el CLIENTE no aprueba la transferencia a us-east-1 (Art. 23, `Arquitectura_de_Seguridad_v01.md` §10), la postura mínima es la continuidad intrarregional en sa-east-1: uso de la tercera AZ (sa-east-1a/1b/1c) y respaldo inmutable regional, que mantiene RTO ≤ 4 h / RPO ≤ 15 min ante **falla de una zona de disponibilidad o corrupción de datos** — lo que el multi-AZ ya brinda —, pero **no ante una caída de toda la región sa-east-1**, escenario en que la reconstrucción desde el respaldo inmutable toma **24–72 h** e incumple RNF-20.06. Esta alternativa **no usa los sitios on-premise del CLIENTE** para la carga cloud (Talca/Concepción alojan solo el dominio on-premise, con su DRP local RTO +1–2 h); y es precisamente esta degradación la que motiva solicitar la aprobación de us-east-1 con resguardos, conforme al Art. 23.

### 4. Decisión Adoptada
**DR activo-pasivo warm standby multi-región:** replicación continua del WMS (VM-02) hacia **Aurora (ACM us-east-1 global replica)** con DMS CDC, RPO ≤ 15 min y RTO ≤ 4 h; **DRP local** Talca→Concepción (VM-C01/VM-C02) con RTO +1–2 h para la bodega; pruebas reales **2×/año** (RT-07.07) y respaldo **3-2-1-1-0** admitido por S3 Object Lock. Documentado en `Cloud v3.6 §6` y `Consolidado §8`. **Si el CLIENTE no aprueba la transferencia internacional (Art. 23), rige la alternativa D** (§2): continuidad intrarregional en sa-east-1 con tercera AZ y respaldo inmutable, aceptando el RTO de 24–72 h ante caída de toda la región, que es el impacto evaluado en §3.

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Capacidad de cómputo ociosa en la región DRP | Costo de la réplica caliente | Aurora multi-AZ compartida con OLTP cloud; DRP us-east-1 solo componentes críticos |
| Ventana de pérdida ≤ 15 min | No cero-datos | RPO ≤ 15 min aceptado (RNF-20.06); reconciliación de vuelta (RT-03.12) |
| Pruebas de conmutación real | Riesgo de fallo durante la prueba | Ventanas de prueba con plan de reversión; indicadores medidos y corrección de brechas (RT-07.07) |
| Replicación CDC sobre enlaces WAN | Costo de ancho de banda | WAL/DMS comprimido; ventana de replicación nocturna junto a sync batch |

---

# ADR-10 — Almacenamiento On-Premise y Niveles RAID

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** Decisión 16.1 N° 28 (declarar y justificar nivel RAID frente a alternativas).
- **Trazabilidad normativa:** BTT **RT-03.14** (tolerancia a falla de disco y nivel RAID declarado) · **RNF-13.03** (equipos críticos redundantes) · **RNF-13.04** (tolerancia a falla de al menos 1 disco) · **RNF-13.05** (justificación del nivel RAID) · Caso 02 Cap. 16.1 N° 28 y Cap. 10 (ventana crítica sin falla).

### 1. Contexto y Problema
La BD transaccional del WMS (VM-02) concentra ~105 TPS de diseño con escritura fuerte de sincronización y trazabilidad; la evidencia fotográfica del POD, los logs y el contenido de cámara suman datos de escritura secuencial menos críticos. Una falla de disco en la ventana de despacho (05:30–07:00) no puede detener la operación. El nivel RAID debe tolerar el fallo de al menos un disco (RNF-13.04) y justificarse (RNF-13.05/RT-03.14).

### 2. Alternativas Evaluadas
| Nivel | Tolerancia | Reescritura/desempeño | Rebuild frente a URE | Costo (utilizable) | Aplicación | Rechazo/Aceptación |
|---|---|---|---|---|---|---|
| **RAID 10** | N-1 discos por espejo (≥ 1, hasta N/2) | Excelente para IOPS de escritura | Rápido y acotado | 50 % (4–8 NVMe) | BD transaccional y réplica (VM-02, VM-C02, PMe VM-01) | **Ganadora (transaccional)** |
| **RAID 6 (doble paridad + hot-spare)** | Hasta 2 discos simultáneos | Bueno para secuencial | Rebuild más largo, pero seguro ante segundo fallo | 2/N (p.ej. 2 de 8) | Evidencia POD (fotos/firmas), logs, rollups de cámara y mini-WMS de cross-dock | **Ganadora (datos/evidencia)** |
| **RAID 5** | 1 disco | Medio | Riesgo USB de URE en rebuild a gran capacidad + sin doble redundancia | 1/N (económico) | No aplica | Rechazada (no cumple RNF-13.04 robustamente en discos grandes y rebuild) |
| **JBOD/Sin RAID** | 0 | N/D | N/D | — | — | Inadmisible (viola RNF-13.04) |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **Transaccional (RNF-13.04, RT-03.14):** RAID 10 sobre NVMe Superdome/Kioxia (Dimensionamiento v05 §1.2.4) entrega >100.000 IOPS frente a ~840 IOPS necesarias (105 TPS × 8 E/S), con latencia de escritura determinista y reparación acotada — crítico en la ventana de despacho.
- **Evidencia/logs:** RAID 6 (doble paridad + hot-spare) para fotografías POD, logs y rollups; tolera el segundo fallo durante el rebuild, relevante en discos de alta capacidad y baja rotación de escritura.
- **Rechazo de RAID 5:** en discos modernos de 8–16 TB, la probabilidad de URE (uncorrectable read error) durante un rebuild extenso no es despreciable; el caso exige tolerancia a fallo de al menos un disco en operación competitiva (RNF-13.04/05) y RAID 5 solo cubre uno.
- **Coherencia con Ceph (hipervisor):** el pool Ceph N+1 de los nodos de cómputo complementa los niveles RAID de las VMs (redundancia de infraestructura, RNF-13.03); la pieza cross-dock usa contenedores con disco local del mini-PC recubierto por el respaldo nocturno (RNF-20.07).
- **TCO:** el sobre-costo del 50 % de RAID 10 solo se aplica a la BD crítica; el grueso del almacenamiento (evidencia, logs, telemetría) usa RAID 6 con solo 2 de 8 discos de paridad, manteniendo el costo de almacenamiento total contenidamente respecto de RAID 1/0 puro.

### 4. Decisión Adoptada
**RAID 10** para los servicios transaccionales del WMS (VM-02/VM-C02 y núcleo del maestro) con NVMe, y **RAID 6 con hot-spare** para evidencia fotográfica/POD, logs y rollups de cámara; **RAID 5 descartado** y justificado frente a alternativas (RNF-13.05/RT-03.14), con redundancia de equipos críticos por hipervisor Ceph N+1 (RNF-13.03). Registrado en `Dimensionamiento v05 §1.2.4` y `Tabla v06 §A-02`.

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| 50 % de pérdida útil en la BD | Mayor costo de almacenamiento crítico | Solo en la capa transaccional; resto en RAID 6 |
| Rebuild de RAID 6 durante fallas | Ventana de vulnerabilidad al segundo fallo | Hot-spare + alertas NOC 24×7 (RNF-21.01) y monitoreo SMART |
| Complejidad de niveles mixtos | Operación de dos políticas | Política única de respaldo 3-2-1-1-0 (RNF-20.07) sobre ambas capas |
| Dependencia del proveedor de hardware | Reposición de discos | SLA de reemplazo ≤ 4 h para componente crítico (Sección 4.2 Tabla v06); stock ≥ 10 % parque |

---

# ADR-11 — Integración B2B/EDI con Supermercados: Hub GS1 Centralizado con Capa Anticorrupción

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisiones relacionadas:** RF-12 (mensajería electrónica EDI); RF-01.10 (maestro interno de productos, tabla de equivalencias por cadena); A-04 (Capa Anticorrupción del ERP).
- **Trazabilidad normativa:** BTT **RT-05.23** (estándares sectoriales de intercambio — EDI) · **RT-16.16** (documentos cifrados con integridad y retención) · **RT-16.17** (firma electrónica Ley N° 19.799) · **RNF-12.01** (canal moderno en producción antes de enero 2029) · **RF-12.03** (equivalencias GTIN por cadena) · **RF-12.06** (bandeja de excepciones) · **RF-01.10** — estándares GS1 (EANCOM/GS1 XML, EPCIS) invocados por el Caso 02 Cap. 16.2 · Caso 02 Cap. 9 (cadenas del canal moderno).

### 1. Contexto y Problema
Los supermercados del canal moderno (p.ej. Walmart, Cencosud, SMU) exigen intercambio electrónico EDI dentro de sus ventanas de taking (pedidos, envío de guías/facturas, acuse de recibo). Hoy el caso lo resuelve por correo/telefono y con diferencias de maestro por cadena (decisión 16.1 N° 11). Conectores punto-a-punto por cadena multiplican los adaptadores, duplican la lógica de mapeo y disparan el mantenimiento ante cada cambio de especificación de la cadena; además, el ERP (que no se reemplaza) expone una frontera frágil.

### 2. Alternativas Evaluadas
| Alternativa | Estandarización GS1 | Esfuerzo por cadena nueva | Aislamiento del ERP | Madurez del ecosistema | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Hub EDI centralizado (GS1) + Capa Anticorrupción (ACL)** | Mapeo único a GS1 EANCOM/GS1 XML; EPCIS para trazabilidad | Conector configurado (perfiles por cadena), sin desarrollo a medida | El ERP solo habla con la ACL (nunca escritura directa) | Estándar de la industria; validación de esquemas | **Ganadora** |
| **B. Conectores punto-a-punto por cadena** | Modelado ad-hoc por cadena | Desarrollo y pruebas por cada cadena | Frontera expuesta directamente al ERP | Baja | Rechazada (esfuerzo × cadenas y acoplamiento) |
| **C. Portal manual de documentos** | No es EDI | Descarga/upload manual | N/D | Baja | Solo complemento (bandeja e impresos de respaldo) |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **Estandarización (Cap. 16.2):** el caso exige estándares GS1; el hub declara un modelo canónico (EANCOM D.01B/GS1 XML para pedidos/despachos/facturas, EPCIS para eventos de trazabilidad) y mapea cada cadena contra el modelo, no contra el ERP.
- **Esfuerzo marginal:** una cadena nueva se agrega por **configuración de perfil** (equivalencias GTIN, RF-12.03) y pruebas de conexión, no por código; el hub centraliza la validación, el retry y la auditoría.
- **Aislamiento del ERP (ACL A-04):** el ERP (que no se reemplaza, ADR-08) queda detrás de la capa anticorrupción: `celery-erp-sync` lee contratos OpenAPI del ERP y publica notificaciones por SQS; **nunca hay escritura directa** desde una cadena al ERP (Zero Trust, BA Art. 21).
- **Plazo contractual:** el canal moderno (incluido EDI) entra en producción antes del **hito enero 2029** (RNF-12.01), por lo que la Etapa 2 concentra portal y EDI detrás de la misma puerta de enlace (**Amazon API Gateway**, ADR-13) y del hub.
- **Equipo de 4 TI:** el hub EDI se aloja como módulo del monolito (ADR-01) en la DMZ de AWS (N-01…N-03) con servicios administrados (API Gateway, SQS, EventBridge), sin adaptadores propietarios por cadena.

### 4. Decisión Adoptada
**Hub EDI centralizado basado en GS1** (EANCOM/GS1 XML para textos, EPCIS para trazabilidad) en la nube (DMZ, `modulo integraciones` del monolito), con **conector configurable por cadena**, **tabla de equivalencias GTIN/cadena** (RF-12.03), **bandeja de excepciones** (RF-12.06) y **Capa Anticorrupción (ACL, A-04)** hacia el ERP/GDE. Canal moderno operativo ≤ enero 2029 (RNF-12.01). La evidencia POD se articula con la GDE y el acuse de recibo electrónico (RF-12.12/12.13, RT-16.17/16.18).

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Dependencia de especificaciones por cadena | Cambios en el perfil de cada cadena | Versionado de contratos (AsyncAPI, RT-05.16/17) y pruebas de integración contínua contra los bancos de pruebas de cada cadena |
| El ERP sigue siendo el emisor tributario | Latencia de la GDE/factura | Acuse dentro de los 30 min de la descarga (RF-12.13); la ACL abstrae el ERP |
| Equivocaciones de GTIN por cadena | Diferencias de maestro | Equivalencias por cadena (RF-12.03) + bandeja de excepciones visible (RF-12.06) |
| Costo de la infraestructura DMZ H2 | Recursos del hub | Servicios administrados y FinOps (RT-03.06); el hub comparte la tarea `portal` (ADR-01) |

---

# ADR-12 — Absorción del Peak de Septiembre y Perfil de Carga No Plano

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** Decisión 16.1 N° 30 (cuello de botella del peak de septiembre y estrategia).
- **Trazabilidad normativa:** BTT **RT-09.05** (identificar el cuello de botella y cómo se detecta/resuelve) · **RT-03.06** (FinOps) · **RT-03.08** (instancias reservadas/ahorro) · **RT-03.09** (cómputo serverless para carga variable) · **RNF-19.01–04** (capacidad, escalado horizontal automático, cuello de botella, pruebas 1,5×) · Caso 02 Cap. 14.2/15 (perfil no plano; congelamiento 1–25 sept) · **RT-10.05** (congelamiento de cambios en septiembre/diciembre).

### 1. Contexto y Problema
El perfil de carga no es plano: preventa 09:00–18:00, preparación 22:00–06:00, despacho 05:30–07:00 (96 camiones), sincronización de flota 17:00–20:00, y **septiembre casi duplica el volumen durante 3 semanas** (1.400 → 2.600 entregas/día). Sobredimensionar para el promedio diario es un error declarado por el propio caso; sobredimensionar estático para el peak paga 12 meses la capacidad de 3 semanas.

### 2. Alternativas Evaluadas
| Alternativa | Costo en régimen | Comportamiento en peak | Detección de cuello de botella | Rechazo/Aceptación |
|---|---|---|---|---|
| **A. Cómputo elástico serverless/contenedores (Fargate 2→6, Celery 2→4, Lambda, Aurora escalada)** | Pago por uso; escala solo cuando sube la carga | Auto-escalado predictivo (calendario sept/diciembre) + reactivo (CPU/cola) | Amazon CloudWatch / Prometheus; umbrales de cola y TPS visibles (RT-09.05) | **Ganadora** |
| **B. Sobredimensionamiento estático (12×2 vCPU fijo + Aurora 2×)** | Pago fijo del 100 % los 56 meses | Nunca degrada, pero se paga todo el año | Requiere monitoreo manual | Rechazada (costo: ~40–60 % más OPEX por el peak inactivo, contra FinOps RT-03.06) |
| **C. Overprovision moderado + colas más largas (sin escala automática)** | Intermedio | Los workers cuelan y la reconciliación se desplaza a horario no crítico | Parcial | Complementa a A para cargas cola (reconciliación) |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **Perfil no plano (Cap. 14.2/15):** la capacidad se calcula al **peak ×1,5** (RNF-19.04) = **3.900 entregas/día**, con ~105 TPS de diseño de despacho y pruebas de carga de **1,5×peak ≈ 160 TPS / 5.850 entregas** (RNF-19.04). Fargate 2→6 tareas (Django), Celery 2→4 y Lambda 100→500 cubren la ratio de las 3 semanas sin pago residual.
- **Cuello de botella identificado (RT-09.05):** confirmación/persistencia transaccional de pedidos e ingesta de telemetría de la flota. Se declara el punto de saturación y se vigila con métricas de negocio (OTIF, pedidos no preparados) y de infraestructura (cola SQS, CPU, TPS) — RNF-19.03.
- **FinOps (RT-03.06) y RT-03.08/03.09:** la base reservada (RI/Savings Plan) cubre la capacidad de régimen; el crecimiento del peak se paga con cómputo efímero (Fargate/Lambda). Ampliar Aurora a `xlarge` + 2 readers y DynamoDB con autoscaling absorbe el pico sin compra fija.
- **Congelamiento (RT-10.05):** del 1 al 25 de septiembre y en diciembre no se despliegan cambios; la escala predictiva se programa por calendario (calendario de eventos) y se valida en la marcha blanca de septiembre del año 1.
- **Equipo de 4 TI:** la operación es declarativa (IaC, RT-03.03): el mismo despliegue escala y decrece sin intervención manual; las políticas de alerta de desviación de presupuesto (RT-03.06) sustituyen el control manual del costo.

### 4. Decisión Adoptada
**Cómputo elástico con auto-escalado horizontal** (Fargate Django 2→6, Celery 2→4, Lambda 100→500, Aurora `db.r6g.large→xlarge` +2 readers, DynamoDB on-demand) con **escala predictiva por calendario** (septiembre/diciembre) y **reactiva** (CPU, profundidad de cola, TPS); base de capacidad con Savings Plan/instancias reservadas de la carga de régimen (RT-03.08) y la diferencia del peak como cómputo efímero (RT-03.09). Monitoreo del cuello de botella declarado (RT-09.05/RNF-19.03) y pruebas 1,5×peak (RNF-19.04).

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Costo de proveer la parte efímera | Dependencia del autoscaler | 0 riesgo de pay-what-you-use: presupuestos y alarmas (RT-03.06); base RI para régimen |
| La cola puede crecer en el burst | Latencia de reconciliación | Vúmenes dimensionados (SQS × 24 h buffer); workers autoescalados; congelamiento de cambios (RT-10.05) |
| Complejidad del autoscaler predictivo | Configuración de calendario | Configuración IaC por evento (EventBridge); ensayo en marcha blanca de sept; aumentos conservadores ×1,5 |
| Surgimiento de cuello de botella nuevo tras el peak | Identificación tardía | Monitoreo de síntomas de negocio (RF-16.03) + pruebas de estrés al punto de quiebre (RNF-19.04) |

---

# ADR-13 — Puerta de Enlace de Servicios: Amazon API Gateway

- **Estado:** Aprobado
- **Fecha:** 2026-09-05 (formalizado como ADR el 2026-09-06)
- **Decisión relacionada:** D8 (Arquitectura Lógica v6.2, Capa 3).
- **Trazabilidad normativa:** **BA Art. 21.2** (puerta de enlace con autenticación, autorización, cuotas, límites de tasa, validación de esquema e inspección de carga útil) · **RT-02.01** (capa 3 del modelo de referencia) · **RT-11.11** · **RT-05.16/05.18** (contratos y OAuth 2.1/mTLS) · **RT-02.02** (contratos versionados retro-compatibles) · Art. 16.3 (preferencia por servicios administrados).

### 1. Contexto y Problema
La Capa 3 es el punto por donde entra **todo**: las APIs de negocio, la sincronización diferida de preventa y reparto —que es tráfico de primera clase, no un anexo— y los tres portales de la DMZ. El Art. 21.2 no pide «un gateway»: pide autenticación, autorización, cuotas, límites de tasa, validación de esquema e inspección de carga útil, todo en el borde. Y el CLIENTE opera con **4 personas de TI**: cualquier componente que haya que parchar, dimensionar y sostener 24×7 compite con la operación.

### 2. Alternativas Evaluadas
| Alternativa | Operación | Integración con el borde | Cuotas y esquema | Costo para un equipo de 4 | Veredicto |
|---|---|---|---|---|---|
| **A. Amazon API Gateway (administrado)** | Cero nodos que operar; escala con la carga | Nativa con CloudFront, WAF, Shield y ALB; autorizador OIDC contra Keycloak | Validación de esquema OpenAPI, cuotas y límites por cliente y por ruta, trazabilidad por transacción | Nulo en operación; costo por invocación declarado en FinOps | **Ganadora** |
| **B. Kong Gateway (open source, autoalojado)** | Nodos propios con alta disponibilidad, parches y versiones a cargo del equipo | Requiere integrar manualmente con WAF/ALB | Equivalente vía plugins | Alto: un componente crítico más en la ruta de la venta, operado por 4 personas | Rechazada |
| **C. Sin puerta de enlace, exponiendo el ALB directo a los módulos** | Mínima | — | No cumple Art. 21.2 (sin cuotas ni validación de esquema en el borde) | — | Rechazada (incumplimiento normativo) |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **Cumplimiento literal del Art. 21.2** sin desarrollo propio: autenticación OIDC, autorización por rol, cuotas y límites de tasa por cliente, validación de esquema e inspección de carga útil son capacidades nativas.
- **Equipo de 4 personas (Cap. 2.4 del caso):** la alternativa B agrega un componente crítico en la ruta de la venta que hay que dimensionar, parchar y recuperar. En la ventana de despacho 05:30–07:00, con indisponibilidad cero comprometida, ese es exactamente el riesgo que no conviene asumir.
- **Coherencia con la vista física:** el documento de nube, el consolidado híbrido, la tabla de emplazamiento y el de despliegue ya declaran Amazon API Gateway; mantener Kong en el registro de decisiones habría dejado una contradicción entre la arquitectura lógica, la física y el costo, que el **Art. 16.4 in fine** califica de incoherencia grave.
- **Reversibilidad (Art. 16.3):** los contratos son **OpenAPI 3.1 y AsyncAPI 2.6**, estándares abiertos; la lógica de negocio vive en Django, no en el gateway. Migrar a Kong u otro gateway no exige reescribir servicios, solo reconfigurar rutas y autorizadores. La dependencia es de configuración, no de código, y así queda declarada en la matriz de reversibilidad.

### 4. Decisión Adoptada
**Amazon API Gateway** como Capa 3 única, con autorizador OIDC contra el Keycloak maestro, validación de esquema OpenAPI, cuotas y límites de tasa por actor y por ruta, versionado `/v{major}` y asignación de `transaction_id` propagado a la Capa 8. **Kong Gateway queda declarado como alternativa open source evaluada y no adoptada.**

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Dependencia de un servicio del proveedor de nube | Menor portabilidad del borde | Contratos en estándares abiertos; la lógica no vive en el gateway (§4.6 de reversibilidad) |
| Costo por invocación en el peak de septiembre | Gasto variable | Cuotas por actor y límites declarados; modelado en FinOps con el peak de 105 TPS |
| Los portales entran en enero de 2029 | La configuración crece en la Etapa 2 | Mismo gateway, rutas nuevas por configuración; sin componente adicional |

---

# ADR-14 — Plataforma de Observabilidad Única: OTel + AMP + CloudWatch + X-Ray

- **Estado:** Aprobado
- **Fecha:** 2026-09-06
- **Decisión relacionada:** D14 (Arquitectura Lógica v6.2, Capa 8); reemplaza la parte de plataforma de D9.
- **Trazabilidad normativa:** **BA Art. 16.4** («monitoreo del componente on-premise integrado a la misma plataforma de observabilidad que la nube, sin puntos ciegos») · **RT-03.16** (idéntica exigencia) · **RT-14.01 a RT-14.09** · **RT-09.01** (medición p95) · Art. 16.3 (servicios administrados).

### 1. Contexto y Problema
La observabilidad tiene que cubrir dos dominios muy distintos —una nube elástica y cinco sitios que pueden quedar 24 h sin enlace— y hacerlo **sin puntos ciegos**. La versión anterior de la arquitectura lógica declaraba un conjunto **Prometheus + Grafana + Loki autoadministrado en cada centro de distribución**, además de la plataforma en nube. Al contrastarlo con la vista física aparecieron dos problemas: ese conjunto **no tenía máquina virtual dimensionada** —VM-06 es de 2 vCPU, 4 GB y 50 GB, insuficiente para sostener Prometheus, Loki y Grafana con 13 meses de métricas— y, más de fondo, **constituye una segunda plataforma de observabilidad**, que es justamente lo que el Art. 16.4 y RT-03.16 prohíben al exigir «la misma».

### 2. Alternativas Evaluadas
| Alternativa | ¿Una sola plataforma? | Qué se ve durante un corte de 24 h | Operación | Veredicto |
|---|---|---|---|---|
| **A. Emisión on-premise (ADOT, buffer 24 h) → plataforma única en nube (AMP, CloudWatch, X-Ray, Grafana OSS)** | **Sí** | Sin tableros centralizados; alarmas locales del equipamiento y bloqueo de frío 100 % local; **cero pérdida de telemetría** gracias al buffer | Nula on-premise | **Ganadora** |
| **B. Prometheus + Grafana + Loki autoalojado por sitio, además de la nube** | No: dos plataformas | Tableros locales completos | Dos plataformas que parchar, dimensionar y correlacionar, sobre un equipo de 4; requiere VM adicional no dimensionada | Rechazada (incumple RT-03.16 y Art. 16.4; sin emplazamiento) |
| **C. Datadog o New Relic** | Sí | Depende del enlace igual que A | Menor, pero con lock-in y costo por host y por volumen | Rechazada (lock-in y costo) |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **La norma pide una plataforma, no dos.** Es el criterio decisivo: el Art. 16.4 y RT-03.16 usan la palabra «misma».
- **«Sin puntos ciegos» se resuelve con el buffer, no con una segunda plataforma.** El colector ADOT retiene 24 h en disco —exactamente la autonomía comprometida del centro de distribución— de modo que un corte no produce un hueco en la serie: produce un retraso que se cierra al reconectar.
- **Ninguna decisión crítica depende de un tablero.** El bloqueo de despacho por excursión térmica es local (decisión 16.1 N° 4), la alarma de cámara es acústica y luminosa, y los sensores de sala reportan al DCIM/BMS (RT-06.14). Lo que se pierde durante el corte es visibilidad agregada, no capacidad de operar.
- **Sin lock-in real:** **AMP es compatible con Prometheus y PromQL**, de modo que las reglas de alerta y las consultas son portables; la instrumentación es **OpenTelemetry**, estándar neutral; y Grafana es **OSS**. Se conserva el ecosistema Prometheus/Grafana sin operar sus servidores.
- **Equipo de 4 personas:** no se le entrega al CLIENTE una plataforma de observabilidad que mantener además del negocio.

### 4. Decisión Adoptada
**Instrumentación OpenTelemetry** en todos los componentes; **colectores ADOT on-premise (F-01: VM-06 Talca, VM-C04 Concepción, contenedor en cross-docking) con buffer en disco de 24 h**; **plataforma única en nube**: métricas en **AMP** (13 meses), registros en **CloudWatch Logs** (12 meses en línea + 24 en archivo), trazas en **X-Ray** (30 días), tableros en **Grafana OSS** autoadministrado en sa-east-1 y alertas por AMP/Alertmanager y CloudWatch hacia SNS y PagerDuty. **Se declara expresamente qué no está disponible durante un corte** (RT-03.13), y se declara que ninguna decisión de la ventana 05:30–07:00 depende de ello.

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Sin tableros centralizados durante un corte de enlace | Menor visibilidad agregada en contingencia | Buffer de 24 h sin pérdida; alarmas locales del equipamiento; bloqueo de frío local; declaración formal en la matriz RT-03.13 |
| Dependencia de servicios del proveedor de nube | Portabilidad | AMP compatible con Prometheus/PromQL, OTel como instrumentación y Grafana OSS: el ecosistema es portable |
| El buffer de 24 h consume disco en VM-06 y VM-C04 | Capacidad local | Dimensionado en el plan de capacidad; el corte de referencia es de 24 h (RT-03.10) |

---

# ADR-15 — Gestión de Secretos: Servicio Administrado en lugar de Gestor Autoalojado

- **Estado:** Aprobado
- **Fecha:** 2026-09-06
- **Decisión relacionada:** D13 (Arquitectura Lógica v6.2, Capa 7); resolución **SEC-01** de `Arquitectura_de_Seguridad_v01.md` §5.3.
- **Trazabilidad normativa:** **BA Art. 21.4** («prohibición absoluta de credenciales, claves o secretos embebidos… uso obligatorio de un gestor de secretos con rotación automática») · **Art. 21.2** (gestión de claves con separación de funciones) · **Art. 16.2** (justificación de emplazamiento componente por componente) · **Art. 16.3** (servicios administrados) · **Art. 21** (Zero Trust) · RT-04.09 · RT-11.09.

### 1. Contexto y Problema
La solución necesita custodiar secretos de peso: credenciales del ERP de 2017, certificados AS2 y EDI de cada cadena de supermercados, credenciales del SII y de Transbank, y las credenciales de servicio entre módulos. El Art. 21.4 exige un gestor con rotación automática. La arquitectura lógica declaraba **HashiCorp Vault on-premise**, pero al contrastarla con la vista física apareció el problema real: **Vault no existía en ninguna vista física** —no tenía máquina virtual entre las diez del dimensionamiento, no figuraba en el inventario del consolidado, ni en la tabla de emplazamiento, ni en el T-11—. Un componente de seguridad sin emplazamiento justificado **incumple el Art. 16.2** y, al no estar costeado, cae en la incoherencia grave del Art. 16.4 in fine.

### 2. Alternativas Evaluadas
| Alternativa | Emplazamiento y costo | Operación para 4 personas | Zero Trust | Rotación automática | Veredicto |
|---|---|---|---|---|---|
| **A. AWS Secrets Manager + SSM Parameter Store** | Servicio administrado, sin VM ni licencia; costo por secreto declarable en FinOps | Nula: no se parcha ni se sella | Consumo **saliente** desde on-premise por VPC Endpoint; ningún puerto entrante | Nativa | **Ganadora** |
| **B. HashiCorp Vault autoalojado en Talca** | VM adicional con alta disponibilidad, respaldo, procedimiento de sellado y desellado, y licencia empresarial si se requiere alta disponibilidad | Alta: el desellado tras un reinicio es un procedimiento manual crítico que puede caer a las 3 de la mañana | Equivalente | Sí, con configuración propia | Rechazada |
| **C. Secretos en variables de entorno o en la configuración del despliegue** | — | — | — | — | Rechazada: **prohibición absoluta** del Art. 21.4 |

### 3. Criterio de Selección y Justificación Técnica-Económica
- **El componente debe existir en la vista física.** Es la razón inmediata: lo declarado no estaba emplazado ni costeado. Cualquiera de las dos salidas corregía el defecto, pero solo una lo hacía sin agregar infraestructura.
- **Equipo de 4 personas (Cap. 2.4):** el modo sellado de Vault tras un reinicio exige intervención humana con custodios. En una operación cuya ventana crítica es de 05:30 a 07:00 y cuyo turno de preparación es nocturno, introducir un componente que puede requerir desellado manual de madrugada es un riesgo operacional que no compra nada.
- **Zero Trust intacto:** los nodos on-premise consumen secretos por **VPC Endpoint saliente**, coherente con la regla de que no se abren puertos entrantes salvo las dos excepciones D-AL-05.
- **La contingencia no depende de la nube.** El secreto de la **cuenta de emergencia** queda deliberadamente **fuera de línea**, en sobre sellado con doble firma en el recinto de custodia de la sala (RT-06.26/06.27): es la única credencial que debe seguir siendo utilizable cuando no hay ni IdP ni enlace, y por eso no vive en ningún sistema.
- **Separación de funciones (Art. 21.2):** quien administra la plataforma no administra las claves maestras; la política se expresa en IAM y queda auditada en CloudTrail.

### 4. Decisión Adoptada
**AWS Secrets Manager** para secretos con rotación (credenciales del ERP, SII, Transbank y certificados AS2/EDI) y **SSM Parameter Store** para parámetros de configuración no sensibles, con consumo **saliente** desde los nodos on-premise por VPC Endpoint, rotación automática, y **cifrado con CMK de KMS bajo separación de funciones**. **HashiCorp Vault queda declarado como alternativa evaluada y no adoptada.** La cuenta de emergencia se custodia fuera de línea.

### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Los nodos on-premise requieren enlace para obtener un secreto nuevo | Dependencia de la nube para la rotación | Los secretos en uso se cachean en memoria por el proceso durante la autonomía de 24 h; ninguna rotación se programa dentro de la ventana crítica ni de un corte |
| Dependencia de un servicio del proveedor de nube | Portabilidad | Los secretos son datos, no lógica; la exportación está cubierta por la declaración de reversibilidad (Art. 16.3) |
| Costo por secreto y por rotación | Gasto variable | Volumen acotado (integraciones del catálogo, 15 entradas) y declarado en FinOps |

---

## Matriz de trazabilidad (ADR → normativa → decisión → documento)

| ADR | RT / RNF clave | BA / Caso | Decisión relacionada | Documento que la materializa |
|---|---|---|---|---|
| ADR-01 | RT-02.02 · §2.3 · RT-09.05 · RNF-19.01–04 | Art. 16 | D5 | Arquitectura_Logica_v6-1 (v6.2) · Cloud v3.6 §1.1/§3.5 |
| ADR-02 | RT-03.17 · RT-03.10 · RNF-13.01/13.07/13.08 · RT-10.05 | §6.12/§8 (caso) | Decisión 16.1 N° 26 | Tabla v06 §D-03/D-04/D-06 · T-11 C27 |
| ADR-03 | Art. 16.1–16.4 · RT-03.01/03.02/03.10 · RNF-02.01/05.01/05.02 | Art. 16 BA | D7 · Decisión 16.1 N° 17 | Tabla v06 §1.0 · Cloud v3.6 §1 |
| ADR-04 | RT-05.02 · RT-05.15 · RNF-09.01/09.02/11.02 | Cap. 16.1 N° 18/35 · D.S. 977/96 | D2/D4 | Cloud v3.6 §4 · decisiones.md N° 18/35 |
| ADR-05 | RT-02.06/02.07 · RT-03.10/03.12 · RNF-07.01/13.01 | Art. 21 (Zero Trust) | D4 · D-AL-03 | Cloud v3.6 §3.1/§7.9 · Consolidado §3.4 |
| ADR-06 | RT-12.10/12.11/12.12 · RT-03.10 · RNF-13.01 | Art. 22 (MFA) | D6 · Decisión 16.1 N° 34 | Cloud v3.6 §3.3/§5.4 · Consolidado §5 |
| ADR-07 | RT-13.08 · RT-12.11 · RT-03.19 · RNF-05.02/05.03/06.01 | Cap. 6/13.8 (caso) | Decisión 16.1 N° 19 | Tabla v06 §4 · decisiones.md N° 19 |
| ADR-08 | RT-05.11–05.15 · RT-03.10 · RNF-02.01 | Cap. 16.1 N° 14 | Decisión 16.1 N° 14 | decisiones.md N° 14 · Informe 1 |
| ADR-09 | RT-07.01/07.07 · RNF-20.06/20.07 | Art. 20 BA | Decisión 16.1 N° 27 | Cloud v3.6 §6 · Consolidado §8 |
| ADR-10 | RT-03.14 · RNF-13.03/13.04/13.05 | Cap. 16.1 N° 28 | Decisión 16.1 N° 28 | Dimensionamiento v05 §1.2.4 · Tabla v06 §A-02 |
| ADR-11 | RT-05.23 · RT-16.16/16.17 · RNF-12.01 · RF-12.03/12.06/12.13 | Cap. 16.2 GS1 | RF-12 · RF-01.10 | Arquitectura_Logica_v6-1 (v6.2, M11) · Arquitectura_de_Integracion_v01 §7 |
| ADR-12 | RT-09.05 · RT-03.06/03.08/03.09 · RNF-19.01–04 | Cap. 14.2/15 · RT-10.05 | Decisión 16.1 N° 30 | Cloud v3.6 §3.5 · Dimensionamiento v05 §1 |
| **ADR-13** | RT-02.01 · RT-11.11 · RT-05.16/05.18 · RT-02.02 | Art. 21.2 · Art. 16.3 | D8 (AL v6.2) | Arquitectura_Logica_v6-1 §7 · Arquitectura_de_Integracion_v01 §4 · Cloud v3.6 §2.3 |
| **ADR-14** | RT-03.16 · RT-14.01–14.09 · RT-09.01 | **Art. 16.4** · Art. 16.3 | D14 (AL v6.2, reemplaza D9) | Arquitectura_Logica_v6-1 §12 · Consolidado §9 · Tabla v06 F-01 |
| **ADR-15** | RT-04.09 · RT-11.09 · RT-03.15 | **Art. 21.4** · Art. 21.2 · **Art. 16.2** · Art. 16.3 | D13 (AL v6.2) · SEC-01 | Arquitectura_de_Seguridad_v01 §5.3 · Arquitectura_Logica_v6-1 §11 |

---

## Referencias
1. Bases Administrativas (TFEP-01/2026) — Art. 16 (híbrido), Art. 20 (DR), Art. 21–22 (seguridad/MFA).
2. Bases Técnicas Transversales — RT-02.xx, RT-03.xx, RT-05.xx, RT-07.xx, RT-09.xx, RT-10.xx, RT-12.xx, RT-13.xx, RT-16.xx.
3. Caso 02 Logística — Cap. 6, 9, 10, 14.2, 15, 16.1 (40 decisiones), 16.2 (materias a investigar), 17, 18.
4. `Arquitectura_Logica_v6-2.md` **v6.2** — decisiones **D1–D15** (vigentes 2026-09-06).
5. `Requerimientos/decisiones.md` — Registro de decisiones del caso (N° 1–40).
6. `Tabla_Emplazamiento_OnPremise_v06.md` (v07) — Sección 1.0 tabla maestra, Bloques A–F y N, Sección 4 dispositivos.
7. `Propuesta_Arquitectura_Cloud_Caso02_CLAUDE_v2.md` (v3.6) — dimensionamiento, costos, justificaciones Art. 16 (matriz §7.1).
8. `Arquitectura_Fisica_Hibrida_Consolidada_Caso02_v02.md` — fuente única consolidada.
9. `Dimensionamiento_Infraestructura_OnPremise_v05.md` — TPS, RAID, capacidad.
10. `T-11` C27 — kit Starlink D-06: planes (1 TB CD / 500 GB cross-dock) y reposición 15 %/56 meses declarados en la oferta.