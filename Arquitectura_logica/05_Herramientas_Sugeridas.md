# 05 — Herramientas Sugeridas (Pie de Inicio Tecnológico · Puelche S.A.)

> **Propósito:** entregar un **punto de partida tecnológico** para la propuesta, herramienta por capa de la maqueta (`04`), con su **justificación ligada a un problema concreto de Puelche** y su alternativa. No es una decisión final de compra: es la **base de arranque** para discutir con el mandante.
>
> **Criterios de selección (del caso y las Bases):** operación **offline** de primera clase · equipo TI de **4 personas** · **híbrido cloud + on-premise** obligatorio · **multi-zona IaC** · **Zero Trust** · sin vendor lock-in · costo de licencias bajo · comunidad y soporte en español.

---

## 1. Stack sugerido de arranque (resumen)

| Capa / Componente | Herramienta sugerida | Alternativa sólida |
|---|---|---|
| **Backend (lógica de negocio, 12 módulos)** | **Django (Python 3.12)** — monolito modular | Laravel (PHP) · Spring Boot (Java) · .NET 8 |
| **Frontend web (portales + consolas)** | **Angular** + Tailwind CSS | React + Next.js |
| **Apps de campo (preventa y reparto, offline)** | **Flutter** (mismo precedente de "Pancho") | PWA Angular · React Native |
| **Base de datos transaccional** | **PostgreSQL + PostGIS** (decidido — ver §5) | MariaDB · MySQL |
| **Cache / sesiones (decidido)** | **Redis** (ver §5.3) | Memcached |
| **Analítica / BI consolidada** | PostgreSQL (OLTP nube: **Aurora**) · analítica pesada en **S3 + Redshift Serverless** | MariaDB para análisis (menos ideal) |
| **Time-series (telemetría, sensores de frío)** | **TimescaleDB** (sobre PostgreSQL) | InfluxDB |
| **Cache y sesiones** | **Redis** | Memcached |
| **Mensajería asíncrona (cola)** | **RabbitMQ** | Kafka (solo si hubiera eventos masivos, no es el caso) — AWS SQS |
| **Búsqueda de catálogo/productos** | **OpenSearch** | Elasticsearch |
| **IAM / Autenticación (Zero Trust)** | **Keycloak** (OIDC/SAML, SSO, MFA) | Azure AD B2C · Auth0 |
| **Contenedores / orquestación** | Docker + Kubernetes (nube) / K3s o Docker Compose en CD | Nomad — EKS/AKS gestionado |
| **Infraestructura como Código** | **Terraform** (multi-zona) + Ansible | Pulumi · CloudFormation |
| **CI/CD** | GitHub Actions o GitLab CI | Jenkins (obsoleto) |
| **Observabilidad** | Prometheus + Grafana + Loki | Datadog (pago) — New Relic |
| **Documentación de API** | OpenAPI / Swagger | Postman Collections |
| **Testing** | pytest (backend) · Playwright (web) | Cypress |

---

## 2. Backend — Django (Python) (decisión 2026-09-03; se valida con el caso)

**Por qué Django para Puelche (y no Laravel):**

| Argumento | Vínculo con el caso |
|---|---|
| **GIS de primer nivel (GeoDjango + PostGIS)** | Puelche es **GIS-fuerte**: planificación de rutas, geocercas, cadena de frío (RF-04, RF-14.08, M4/M9/M12). **GeoDjango** es el ORM espacial más maduro (GeoQuerySet, lookups espaciales, serialización GeoJSON/GeoRaster) y además `ADMIN_*` geohashing — **GIS es un requerimiento estelar del caso, no un accesorio**. |
| **Un solo lenguaje Python en todo el backend** | Evita el "problema de los 4 lenguajes" (el físico original proponía Python+Java+Go+Node). Django cubre CRUD + admin interno + GIS + EDI + telemetría + procesamiento de datos **en un solo stack Python**, homogéneo para un equipo de 4. |
| **Admin de Django (gratis e integrado)** | La operación interna (bodega, calidad, cobranza, excepciones EDI) necesita consolas de administración rápidas. El **Django admin** entrega CRUD con permisos, auditoría y filtros **sin escribir UI**, clave para el equipo de 4. |
| **Monolito modular nativo** | La maqueta `04` propone monolito modular; Django separa por **apps/contextos** (pedidos, rutas, bodega) sin la complejidad de microservicios que un equipo pequeño no puede sostener. |
| **Ecosistema para las partes "difíciles" del caso** | EDI/AS2, OCR/Documentos y **pandas/tiempo real** para telemetría: el ecosistema Python (bibliotecas AS2, `django-celery`, `pandas`, `geopandas`) es el más amplio para integración con el ERP legacy y procesamiento de flota/frío. |
| **Offline / sync bien soportada** | **Django REST Framework** + Celery/Redis + jobs idempotentes dan la base para la **sincronización diferida e idempotente** de preventa y reparto (RF-03.16/17, RF-06.07). |
| **Colas nativas** | Las integraciones asíncronas (ERP, cobranzas, EDI, telemetría) se modelan con **Celery + Redis retry + DLQ**, exactamente lo que exigen RF-07.09, RF-05.06 y RF-12.x; en nube se respaldan con **SQS/EventBridge**. |
| **Open source, sin licencias + LTS** | Django LTS (56 meses de soporte) alineado al contrato; costo total de propiedad bajo, sin Oracle ni licencias comerciales. |
| **Coherencia con el físico** | La parte IoT/telemetría/analítica del físico ya estaba pensada en Python; un monolito Django **unifica** el desarrollo y reduce la operación. |

**Alternativa si el mandante prefiere otro ecosistema:** **Laravel (PHP)** — muy productivo para CRUD/portales y comunidad enorme, pero con GIS y EDI/telemetría menos nativos que Django/Python para este caso. **Spring Boot (Java)** — rendimiento y estandarización corporativa, pero equipo más costoso y desarrollo más lento.

> **Recomendación (decidido 2026-09-03):** **Django (Python) monolito modular** como base, con la vía de extraer las **apps** acopladas (EDI, Telemetría, BI) como **servicios contenedorizados independientes** si el volumen lo exige (`04` ya lo prevé).

---

## 3. Frontend web — Angular (propuesto por el usuario)

**Por qué Angular:**

| Argumento | Vínculo con el caso |
|---|---|
| **Framework corporativo completo (TypeScript)** | Portales de clientes, transportistas, proveedores y consolas internas comparten patrones; Angular trae enrutado, seguridad de formularios y **integración OIDC** directa (Keycloak). |
| **Componentes reutilizables** | El portal de clientes (RF-12.15–12.18), de transportistas (RF-12.19–12.21) y de proveedores (RF-12.22–12.24) comparten 90 % de la UI (login, tablas, documentos). |
| **Mantenibilidad a largo plazo (56 meses)** | El contrato exige mantenimiento; Angular tiene soporte LTS de Google y un ecosistema estable. |
| **Tailwind CSS para consistencia** | Misma libreta visual que la referencia "Pancho", acelerando la UI de bodega y tableros BI. |

**Alternativa:** **React/Next.js** — igual de válida y más flexible, pero con más decisiones de arquitectura por cuenta del equipo (que es pequeño).

---

## 4. Apps de campo — Flutter (offline-first)

**Por qué Flutter para preventa y reparto:**

| Argumento | Vínculo con el caso |
|---|---|
| **Offline-first real** | Bases de datos locales (SQLite/Isar), cifrado local y sincronización diferida: requisito **1ª clase** (RF-03.02, RF-03.05, RF-06.12). |
| **Un solo código para Android/iOS** | Los dispositivos de 62 preventistas y conductores variarán; un solo desarrollo cubre ambos. |
| **Impresora térmica, escáner, GPS** | Plugins maduros para comprobante térmico (RF-06.13), escaneo GS1 (RF-05.02), QR (RF-06.11) y geocercas (RF-14.08). |
| **Precedente consistente** | "Pancho" usó **Flutter en móvil + Angular en web**; mantener el mismo patrón reduce riesgo para el evaluador. |

**Alternativa:** **PWA Angular** — evita instalar app al cliente (útil para el canal tradicional que "no cambia su forma de operar"), pero con capacidades de impresión/escáner más limitadas. Se puede evaluar **PWA para lectura de avisos** y **Flutter para la app operativa**.

---

## 5. Base de datos — PostgreSQL + PostGIS **y Redis** (decisión 2026-09-02)

> **Decisión final:** la BD transaccional y analítica es **PostgreSQL + PostGIS** (con **TimescaleDB** como extensión para series de tiempo), y el **cache/sesiones/colas ligeras** se hacen con **Redis**. En AWS se consumen gestionados, coherentes con la arquitectura física: **Aurora PostgreSQL** (compatible PostgreSQL; OLTP cloud + réplica/DRP del WMS) + **ElastiCache (Redis)**, con **DynamoDB** para ingesta IoT y **S3 + Redshift Serverless** para el BI pesado. Se cierra el dilema inicial **MariaDB vs PostgreSQL** a favor de PostgreSQL+PostGIS por las necesidades GIS y JSONB del caso.

**Por qué PostgreSQL + PostGIS (y no MariaDB) — decisiones habilitadas por el caso:**

| Necesidad de Puelche | Postgres+PostGIS | Por qué gana |
|---|---|---|
| OLTP transaccional bodega/preventa | ✅ | Tan sólido como MariaDB |
| **Planificación de rutas y geocercas** (RF-04, RF-14.08) | ✅ **PostGIS nativo** | Ruta/geocerca es **eje del caso**; sin depender de capa externa de mapas |
| **JSONB para pedidos offline sincronizados** (RF-03.16/17) y datos EDI | ✅ **JSONB con índices GIN** | El esquema offline y EDI encaja mejor |
| Time-series (camiones, sensores de frío) | ✅ **TimescaleDB** extensión | Telemetría/sensores (M9/M12) |
| Mantenibilidad equipo de 4 | ✅ Gestionado en AWS (RDS) | Menos administración |

**Por qué Redis (cache/sesiones/colas ligeras):**
| Uso en Puelche | Redis |
|---|---|
| Caché de stock disponible, precios, estados (preventa, portales) | ✅ baja latencia |
| Sesiones SSO de portales y consolas | ✅ |
| Colas ligeras / respaldo a RabbitMQ y sincronización diferida | ✅ |

> **Nota:** esta sección reemplaza la postura inicial "MariaDB como pie de inicio". Si el equipo conociera solo MySQL/MariaDB, se documenta el **plan de migración** a PostgreSQL como costo único de arranque (justificado por GIS/JSONB), no como duda de fondo.

### 5.1 Time-series — TimescaleDB (extensión de la BD, no motor aparte)

**TimescaleDB** es una **extensión de PostgreSQL** (no un motor separado) especializada en **datos en serie de tiempo**. Se recomienda sobre la misma BD transaccional/analítica, con un único motor que administrar (clave para un equipo TI de 4 personas).

**Por qué el caso la justifica:**

| Fuente del caso | Dato en serie de tiempo | Volumen/implicancia |
|---|---|---|
| Telemetría de flota (L268, L594) | Posición y velocidad, 42 camiones propios + 54 externos | GPS a 1 lectura/seg × ~96 camiones ≈ **millones de puntos/día**; hoy se consulta a mano en el portal del proveedor (L973) |
| Sensores de frío (RT-17.06, L752) | Temperatura de cámaras y vehículos | **Registros de temperatura por 5 años** (RT-05.10) |
| Rutas planificadas vs reales, geocercas (RF-14) | ETA, kilometraje, desviaciones, costo de servir | Consultas de agregación temporal |

**Qué resuelve TimescaleDB que una tabla normal no:**

| Capacidad | Por qué la necesita Puelche |
|---|---|
| **Hipertablas** (particiona por tiempo automático) | Ingesta continua de GPS/sensores sin gestionar particiones a mano |
| **Compresión columnar** | Reduce espacio de los 5 años de temperatura + 12 meses de geolocalización |
| **`time_bucket` / interpolación** | Agregar "velocidad promedio por ruta", "excursiones térmicas por hora" |
| **Políticas de retención automatizadas** | Cumple **RT-05.10**: temperatura 5 años, geolocalización 12 meses (los datos se borran solos al vencer) |

**Vs InfluxDB:** ambas sirven, pero TimescaleDB **reutiliza SQL y el mismo PostgreSQL** (una sola BD con OLTP + series + GIS vía PostGIS). InfluxDB gana en ingesta pura pero **añade un motor, un lenguaje y un operador nuevo** que el equipo pequeño tendría que sostener durante 56 meses.

> **Criterio de adopción declarado en la propuesta (recomendado):** "Se parte con **PostgreSQL transaccional**; si el dimensionamiento (Cap. 8 de las Bases) indica frecuencias de muestreo altas (p. ej. GPS ≥ 1 punto/min por camión o sensores cada ≤ 15 min), se adopta **TimescaleDB** como extensión por compresión y partición por tiempo". Declararlo así demuestra que se pensó el **volumen**, no que se sigue moda. Es una **decisión de diseño condicionada a dimensionamiento**, no un requisito del caso.

### 5.2 Telemetría integrada — usos permitidos vs objeción sindical

Decisión de diseño confirmada en sesión (trazada a `Caso` L268, L577, L594, L973):

| Uso de la telemetría | ¿Se propone? | Justificación |
|---|---|---|
| **Integrar posición/velocidad** de los 42 camiones propios (y ampliar a los 54 externos) | ✅ **Sí** | El caso la da como fuente a integrar (L268, L594, RT-17.06); hoy se consulta a mano (L973) |
| Visibilidad de rutas **planificadas vs reales**, ETA, geocercas, kilometraje/costo de servir | ✅ **Sí** | Módulo M12 (RF-14) |
| Apoyo a **cadena de frío** (ubicación + sensores) | ✅ **Sí** | Coherente con M9 |
| **Cámaras en cabina** | ❌ **No** | Objetada por el sindicato (L577) |
| **Control de jornada por posicionamiento satelital** | ❌ **No** | Objetada por el sindicato (L577); usarla para esto invalida la propuesta o exige plan de gestión del cambio |
| Geolocalización de personas (derivada del GPS) | ⚠️ **Con resguardos** | Ley 21.719 · RT-05.10 (12 meses) · RT-11.10 (cifrado) · RT-16.09 (registro de consultas) |

> **Planteamiento de la empresa (considerando AWS):**
>
> *"Como empresa entendemos la objeción del sindicato. Por esto comunicamos desde ya que la telemetría se usará **únicamente como dato operacional y no de control**: para rutas planificadas vs reales, geocercas, ETA, costo de servir y apoyo a la cadena de frío. Damos de antemano el conocimiento de que este uso puede generar **fricción con el sindicato**, y lo declaramos como **riesgo a futuro** con plan de gestión del cambio. El alcance explícito queda como registro ante cualquier inconveniente."*
>
> **Cómo lo materializa AWS (resguardos, no intromisión):**
> - **No se usará** para control de jornada ni cámaras en cabina (objeción L577). La visibilidad de flota es operativa (búsqueda de excepción/incidencia), no vigilancia de personas.
> - **Menor privilegio y alcance acotado** sobre la geolocalización de personas vía **AWS IAM + VPC privada** y roles con permiso mínimo (solo el personal operativo autorizado).
> - **Cifrado en reposo** de posiciones con **AWS KMS** (cumple RT-11.10).
> - **Retención acotada (12 meses)** con **AWS S3 Lifecycle / Glue + TimescaleDB** (cumple RT-05.10).
> - **Registro de consultas** a datos sensibles con **AWS CloudTrail** (cumple RT-16.09) y **Ley 21.719**.
> - **Auditoría de acceso** con **AWS CloudTrail + Security Hub**; segmentación Zero Trust en la red (WAF/mTLS).

---

## 6. Infraestructura — híbrido multi-zona (obligación de licitación)

> **Decisión 2026-09-02:** nube en **AWS** (multi-región/multi-AZ). La lista de servicios es el §6.1. El stack open source del resto (Django, Angular, Flutter, PostgreSQL, Redis, Keycloak) **no cambia**: AWS aporta la capa de infraestructura y servicios gestionados sobre los que corre.

| Componente | Herramienta | Justificación |
|---|---|---|
| Contenedores | Docker | Estandariza apps de campo y back-office |
| Orquestación nube | **Kubernetes gestionado (Amazon EKS)** — multi-AZ | Multi-zona exigida; autoscaling; decisión AWS |
| Orquestación CD (on-prem) | **K3s / Docker Compose con réplicas** | 3 CDs con personal TI mínimo; K3s liviano y administrable |
| IaC | **Terraform** (multi-zona) + Ansible | Define zonas, redes y segmentación Zero Trust **por código**; multi-proveedor (AWS + on-prem) |
| Gestión de config/secrets | Ansible + HashiCorp Vault | Rotación de credenciales, zero-trust en colas (mTLS) |
| CI/CD | GitHub Actions / GitLab CI | Entrega de los 12 módulos con pruebas automáticas |
| Monitor | Prometheus + Grafana + Loki | Observabilidad de 3 CDs + nube con stack open source (o Amazon CloudWatch como respaldo) |

### 6.1 Servicios de AWS útiles para Puelche (mapeados al stack)

> Leídos contra la maqueta `04` y el stack `05`: se aprovecha lo **gestionado** de AWS para reducir carga del equipo TI de 4 personas, manteniendo el stack de aplicación multi-nube y on-prem (sin lock-in total).

| Servicio AWS | Qué cubre en Puelche | Mapeo al stack / módulo |
|---|---|---|
| **Amazon Aurora PostgreSQL** (compatible PostgreSQL; sustituye a RDS estándar) | OLTP cloud (preventa/reparto/BI) + **réplica/DRP del WMS on-prem** vía WAL; multi-AZ | **PostgreSQL** (Capa 5 · M1–M10, DRP) |
| **Amazon ElastiCache (Redis)** | Cache, sesiones y colas de sincronización — misma primitiva que Redis local | **Redis** (Capa 4 · M3 preventa, sesiones) |
| **Amazon DynamoDB** | Ingesta serverless low-latency de sensores de frío / IoT (deviceId+timestamp), retención 5 años | **M9 calidad (frío)** · raw edge |
| **TimescaleDB (por AWS Marketplace)** | Time-series de telemetría operacional sobre PostgreSQL | **M12 telemetría** (según §5.1) |
| **Amazon S3** (+ Intelligent-Tiering) | Objetos: POD firmados, DTE, adjuntos, evidencia QR + **data lake raw** (Parquet) | **Capa 5 docs** · M6/M7 · data lake |
| **Amazon Redshift Serverless** | OLAP/BI histórico: cadena de frío, OTIF, costo de servir, tableros (alimentado desde S3 vía Glue; no accede directo a Aurora) | **M10 BI / M12** · analítica nube |
| **Amazon EKS** | Kubernetes gestionado multi-AZ para el monolito modular Django y portales | **Capa 3** (orquestación nube) |
| **Amazon Route 53** | DNS y routing multi-zona, failover | Capa transversal |
| **AWS WAF + Shield** | Filtro y protección DDoS frente a internet (portales públicos/clientes) | **Seguridad** (Zero Trust perimetral) |
| **AWS Secrets Manager / SSM Parameter Store** | Secretos y parámetros (alternativa/complemento a Vault) | **Seguridad** (Zero Trust) |
| **AWS KMS** | Cifrado de datos en reposo, incl. geolocalización de personas (RT-11.10) | **Seguridad / privacidad Ley 21.719** |
| **AWS IAM + AWS Organizations** | Cuentas, roles y políticas; límite de permisos (menor privilegio) | **Seguridad** |
| **Amazon CloudWatch / X-Ray** | Métricas, logs centralizados y trazabilidad de solicitudes (respaldo a Grafana/Prometheus/Loki) | **Observabilidad** |
| **AWS Transit Gateway / VPC Peering** | Conectividad cifrada cloud ↔ 3 CDs on-prem (site-to-site VPN / Direct Connect) | **Híbrido rel. on-prem** (Capa 5) |
| **AWS SQS** | Cola gestionada como opción de respaldo/subsidio a RabbitMQ en nube | **Capa 4 mensajería** (si se evita administrar RabbitMQ) |
| **AWS Backup** | Backups centralizados y política de retención (RT-05.10: 12 meses geo-personas, 5 años temperatura…) | **Respaldo/RT** |
| **Amazon GuardDuty / Security Hub** | Detección de amenazas y postura de seguridad (Zero Trust) | **Seguridad** |
| **AWS CloudTrail** | Auditoría de acciones (registro de consultas a datos sensibles — RT-16.09) | **Auditoría / seguridad** |
| **SES / SNS / SQS** | Notificaciones por email/SMS/push (alternativa gestionada a notificaciones) | **M6/M12 avisos** (11.600 clientes trad.) |

> **Nota sobre la BD (decisión 2026-09-02):** la base queda en **PostgreSQL + PostGIS** (transaccional y analítica) y **Redis** (cache/sesiones/colas ligeras), como pediste. En AWS se consumen gestionados y coherentes con la arquitectura física (`markdownsarquitecturafisica/`): **Aurora PostgreSQL** (OLTP cloud + réplica/DRP del WMS) y **ElastiCache (Redis)** — multi-AZ. TimescaleDB se monta sobre el PostgreSQL (extensión) y no como motor aparte; la ingesta IoT en frío va a **DynamoDB** y el BI pesado a **S3 + Redshift Serverless**.

---

## 7. Seguridad — Keycloak (coherente con "Pancho")

- **OIDC/SAML, SSO, MFA** para todos los portales y consolas (mismo estándar que la referencia → coherencia de propuesta).
- **Perfiles por actor** del catálogo `02`: los **11 actores canónicos** → roles en Keycloak (preventista, conductor-propio, conductor-externo, preparador, planificador, calidad, gerente comercial, gerente de finanzas, jefe de TI, cliente-trad, cliente-mod). Los roles de portal de entidad externa (transportista, proveedor) se modelan por rol de portal gestionado por la operación, no como actores internos adicionales.
- **OTP de un solo uso** para conductores externos (RF-06.08) sin alta corporativa.
- **Apps offline:** token de corta vida + datos cifrados en dispositivo + borrado remoto.

---

## 8. Mapa herramientas ↔ módulos de la maqueta (`04`)

| Módulo | Herramientas que lo soportan |
|---|---|
| M1–M2 Recepción / Inventario | Django + PostgreSQL (+ escáner GS1) + colas RabbitMQ |
| M3 Preventa | Flutter + Redis (stock/crédito cache) + sync Django |
| M4 Planificación rutas | Django + **PostGIS/GeoDjango** + mapas (OSRM/Google/Here) |
| M5 Preparación | Django + HHT + colas RabbitMQ |
| M6 Reparto | Flutter + impresora térmica + QR + notificaciones |
| M7 Cobranza | Django + POS/Transbank + ERP vía colas |
| M8 Devoluciones/Envases | Django + BD |
| M9 Calidad/Trazabilidad | Django + TimescaleDB + sensores |
| M10 BI | Angular (tableros) + PostgreSQL analítico (S3/Redshift) + Grafana |
| M11 EDI | Django + adaptador AS2 (Python) + RabbitMQ + OpenSearch (historial) |
| M12 Telemetría | Django + TimescaleDB (según dimensionamiento §5.1) + API GPS + PostGIS + monitoreo operativo (Jefa de calidad/operaciones) |

---

## 9. Cumplimiento de la licitación (checklist rápido)

| Exigencia | Cómo la cumple este stack |
|---|---|---|
| Híbrido cloud + on-premise obligatorio | BD on-prem por CD (§6) + analítica/objetos en nube AWS (Capa 5, §6.1) |
| Multi-zona e IaC | Amazon EKS multi-AZ + Terraform (AWS y on-prem) |
| Zero Trust | Keycloak OIDC/MFA + mTLS + Vault + AWS WAF/IAM/KMS + segmentación por IaC |
| Sin vendor lock-in | App open source (Django, Angular, Flutter, PostgreSQL, Redis, RabbitMQ, Keycloak) portables; la nube AWS aporta servicios gestionados sin amarrar la aplicación |
| Mantenible 56 meses por equipo pequeño | Monolito modular + LTS + documentación OpenAPI + servicios AWS gestionados |
| Operación offline 1ª clase | Flutter offline-first + sync idempotente (+ Redis/colas en servidor) |

---

## 10. Próximo paso con este documento

1. ✅ **Base de datos decidida (2026-09-02): PostgreSQL + PostGIS** (transaccional y analítica) **y Redis** (cache/sesiones/colas ligeras). En AWS: **Aurora PostgreSQL** (compatible, OLTP nube + réplica/DRP del WMS) + **ElastiCache (Redis)**, más **DynamoDB** (ingesta IoT/frío) y **S3 + Redshift Serverless** (BI pesado). **Se cierra el dilema MariaDB vs PostgreSQL** a favor de PostgreSQL+PostGIS (GIS para rutas/geocercas/frío, ver §5 y §5.1).
2. ✅ **Nube decidida (2026-09-02): AWS** (multi-AZ). Lista de servicios en §6.1.
3. ✅ **Backend decidido (2026-09-03): Django (Python) monolito modular** — por GIS/GeoDjango, un solo lenguaje Python, admin integrado y EDI/telemetría (ver §2). La capa de cómputo nube del físico se ajusta a monolito Django en ECS Fargate.
4. Confirmar app de campo: **Flutter** (operativa) + **PWA/Avisos** (clientes).
5. ✅ **Modelo de actores sobre los 11 canónicos** (`02` §1) — **CONFIRMADO (2026-09-01)**. La maqueta `04` se construye con los 11 canónicos; los A1–A16 del `02` §3 quedan documentados pero fuera de la maqueta.
6. **Telemetría (confirmado en sesión):** integrar para uso operativo; **no** para control de jornada; con plan de gestión del cambio y resguardos Ley 21.719 (RT-05.10/11.10/16.09). **RF-14.02→supuesto, RF-14.05→exclusión, RF-14.09→eliminado.**
7. **TimescaleDB (criterio definido):** adoptar como extensión de PostgreSQL **según dimensionamiento** de muestreo del Cap. 8 de las Bases; declararlo en la propuesta.
8. Alimentar la **matriz de trazabilidad** y el **plan de 56 meses**: cada herramienta genera una línea de esfuerzo y de soporte.
9. Si el equipo quiere bajar riesgo, hacer un **piloto de 60 días**: preventa offline + reparto + rendición con un CD.