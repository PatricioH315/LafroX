# T-12 — Matriz de Cumplimiento Técnico y Trazabilidad
## LafroX — Arquitectura Física Híbrida · Caso 02 Logística (Puelche S.A.)

> **Alcance:** requisitos transversales de arquitectura física/híbrida (Cap. 02, 03, 04, 06, 07, 08, 09, 10, 11, 12, 14, 15 de las Bases Técnicas Transversales). Columnas conforme al Formulario T-12 (Bases Administrativas §1704-1716): `ID requerimiento | Descripción | Cumple | Componente que lo satisface | Sección de la propuesta`, más `Hueco / Observación` para la auditoría interna.
>
> **Fuentes de verificación (versiones vigentes):**
> - `Consolidado_Arquitectura_Fis_Log/Propuesta_Arquitectura_Cloud_Caso02_CLAUDE_v2.md` — Cloud v3.6 (en adelante «Cloud §n»)
> - `Consolidado_Arquitectura_Fis_Log/Sala_Servidores_OnPremise_v02.md` — Sala v02 (en adelante «Sala §n»)
> - `Consolidado_Arquitectura_Fis_Log/Dimensionamiento_Infraestructura_OnPremise_v05.md` — Dim v05 (en adelante «Dim §n»)
> - `Consolidado_Arquitectura_Fis_Log/Tabla_Emplazamiento_OnPremise_v06.md` — Tabla v06 (en adelante «Tabla §n»)
> - `Consolidado_Arquitectura_Fis_Log/Arquitectura_Fisica_Hibrida_Consolidada_Caso02_v02.md` — Consolidado v02
> - `Arquitectura_Logica_v6-1.md` v6.2 — arquitectura lógica vigente (D1–D15), en adelante «Lógica v6.2»
> - `Arquitectura_de_Integracion_v01.md` y `Arquitectura_de_Seguridad_v01.md` — vistas de integración y seguridad (Subdoc 4, apartados 3 y 4)
> - La justificación del módulo de BI y analítica vive en Cloud v3.6 §4.3 y en Lógica v6.2 §10.9 (no existe un documento separado)
>
> **Estado:** auditoría exhaustiva (05-09-2026) tras la actualización de la arquitectura on-premise (Sala v02, Dim v05, Tabla v06) e integración del **enlace satelital Starlink (D-06)** en los 5 sitios con cómputo. **Actualizada el 06-09-2026** con el cierre de la auditoría de coherencia del Subdocumento 4: puerta de enlace unificada en Amazon API Gateway (ADR-13), observabilidad de plataforma única (ADR-14), gestión de secretos en servicio administrado (ADR-15), **MDM declarado como componente N-13** (cierra RT-03.18 con emplazamiento, no solo con mención) y retención respondida contra **RT-16.10**.

---

## RESUMEN EJECUTIVO

| Capítulo | Materia | ✅ Cumple | ⚠️ Parcial | ❌ Hueco | Total |
|---:|---|---|---:|---:|---:|
| 02 | Modelo de arquitectura de referencia | 14 | 0 | 0 | 14 |
| 03 | Modelo híbrido: nube y on-premise | 24 | 0 | 0 | 24 |
| 04 | Ambientes, entrega continua y configuración | 10 | 4 | 0 | 14 |
| 06 | Site principal on-premise | 34 | 0 | 0 | 34 |
| 07 | Site secundario y recuperación ante desastres | 14 | 0 | 0 | 14 |
| 08 | Hardware, puestos de trabajo y terreno | 19 | 0 | 0 | 19 |
| 09 | Desempeño, capacidad y escalabilidad | 7 | 1 | 2 | 10 |
| 10 | Disponibilidad, continuidad y resiliencia | 9 | 0 | 0 | 9 |
| 11 | Seguridad de la información | 24 | 4 | 0 | 28 |
| 12 | Identidad, acceso y sesiones | 13 | 0 | 0 | 13 |
| 14 | Observabilidad y gestión del servicio | 9 | 0 | 0 | 9 |
| 15 | Sostenibilidad, eficiencia y certificaciones | 5 | 4 | 0 | 9 |
| | **TOTAL** | **182** | **13** | **2** | **197** |

**Resultado:** 182/197 = **92,4 %** ✅ · 13 ⚠️ (6,6 %) · 2 ❌ (1,0 %).

> En la auditoría anterior (cloud v3.5 + on-premise v01/v04/v05) la solución completa marcaba ~128/172 (≈ 74 %). La actualización de los tres documentos on-premise (Sala v02, Dim v05 con PARTES 5-9, Tabla v06/v06c) cerró la mayor parte de los capítulos 06 (custodia física RT-06.26/27), 07 (DR), 08 (hardware/garantías/pruebas de aceptación), 09 (cuello de botella RT-09.05 y gestión de capacidad RT-09.09), 10 (continuidad), 11 (seguridad), 12 (identidad) y 14 (observabilidad). Los 2 ❌ restantes son artefactos del Plan de Pruebas (T-13), no de arquitectura.

---

# CAPÍTULO 02 — MODELO DE ARQUITECTURA DE REFERENCIA

| ID | Descripción | Cumple | Componente | Sección | Hueco / Observación |
|---|---|---|---|---|---|
| RT-02.01 | Diagrama de arquitectura en las 8 capas | ✅ | Arquitectura Lógica v1 + Consolidado v01 | Consolidado §1; Diseño §2 | — |
| RT-02.02 | Arquitectura modular, límites de contexto y acoplamiento débil | ✅ | Microservicios cloud + módulos on-premise | Cloud §3; Tabla Bloques A-F | — |
| RT-02.03 | Descripción según ISO/IEC/IEEE 42010 con vistas | ✅ | Documento de arquitectura | Cloud §1 (v3.6) | — |
| RT-02.04 | Registro de decisiones de arquitectura (ADR) fechado | ✅ | Decisiones D1-D9 | Arquitectura Lógica v1 / Consolidado | — |
| RT-02.05 | Capa de negocio sin estado; sesión/proceso en almacenes | ✅ | Monolito Django stateless; Redis/BD | Cloud §3.1 | — |
| RT-02.06 | Escrituras idempotentes con clave de idempotencia | ✅ | Broker A-03 + deduplicación RF-03.17 | Tabla A-03; RF-03.16/17 | — |
| RT-02.07 | Flujos de eventos al menos una vez + deduplicación | ✅ | RabbitMQ A-03 | Tabla A-03; Dim §1.2 | — |
| RT-02.08 | Patrones de resiliencia demostrables | ✅ | Fargate/ECS + clúster 3 nodos | Cloud §3.2; Dim §1 | — |
| RT-02.09 | Degradación elegante ante indisponibilidad de no crítico | ✅ | Broker encola + rate limiting | Tabla A-03; Cloud §5.1 | — |
| RT-02.10 | Escalamiento horizontal automático con umbrales | ✅ | ECS Auto Scaling + Ceph | Cloud §3.5; Dim §1.2.5 | — |
| RT-02.11 | SPOF declarados y justificados | ✅ | Declaración SPOF por componente | Tabla §4 (SPOF) | — |
| RT-02.12 | Replicable a nuevas unidades/sitios sin rediseño | ✅ | Nodos edge replicables (Concepción, cross-docking) | Tabla A-01/E-01 | — |
| RT-02.13 | Modelo de dominio del negocio | ✅ | Modelo de dominio Lógica | Arquitectura Lógica v1 | — |
| RT-02.14 | Patrones de arquitectura evolutiva | ✅ | ACL ERP (RT-05.20) | Tabla A-04 | — |

---

# CAPÍTULO 03 — MODELO HÍBRIDO: NUBE Y ON-PREMISE

| ID | Descripción | Cumple | Componente | Sección | Hueco / Observación |
|---|---|---|---|---|---|
| RT-03.01 | Proveedor, región primaria y secundaria declaradas | ✅ | AWS sa-east-1 + us-east-1; on-premise Talca | Cloud §3.1 | — |
| RT-03.02 | HA en ≥ 2 AZ | ✅ | Aurora Multi-AZ, ECS Multi-AZ | Cloud §3.5 | — |
| RT-03.03 | Infraestructura como código versionada | ✅ | Terraform/CDK en repo del CLIENTE | Cloud §3.3 | — |
| RT-03.04 | Red segmentada por capas, subredes privadas | ✅ | VPC, subredes privadas, DMZ | Cloud §3.4 | — |
| RT-03.05 | Servicios administrados priorizados | ✅ | Aurora, S3, ECS Fargate | Cloud §3.2 | — |
| RT-03.06 | FinOps: etiquetado obligatorio | ✅ | Etiquetado por ambiente/módulo/CC | Cloud §4.5 | — |
| RT-03.07 | Reversibilidad y mitigación de bloqueo por proveedor | ✅ | Patrones abiertos (PostgreSQL, OIDC, OTel), multi-nube opcional | Cloud §3.3 + §4.5 | Formalizar en Consolidado sobre DOCA |
| RT-03.08 | Instancias reservadas / planes de ahorro | ✅ | Savings Plans según perfil | Cloud §4.5 | — |
| RT-03.09 | Cómputo serverless / contenedores administrados valorado | ✅ | Comparativa Fargate vs EC2 permanente | Cloud §3.2 (v3.6) | — |
| RT-03.10 | Autonomía on-premise ante pérdida del enlace | ✅ | WMS local + BD + broker (24 h CD / 14 h terreno) | Tabla A-01/A-02/A-03/A-05; Dim §1.4 | — |
| RT-03.11 | Registro de transacciones críticas en desconectado | ✅ | A-02 PostgreSQL local + A-03 broker | Tabla A-02/A-03 | — |
| RT-03.12 | Sincronización automática y reconciliación determinista | ✅ | Broker con política determinista de reconciliación | Tabla A-03; Dim §5.5 | — |
| RT-03.13 | Funciones NO disponibles en desconectado + procedimiento manual | ✅ | Matriz por función/componente | Tabla §1.1 (v06) | — |
| RT-03.14 | Equipos críticos redundantes; almacenamiento tolerante a disco | ✅ | Clúster 3 nodos + RAID 10 + Ceph; quórum propio | Dim §1.2.2/§1.2.5; Tabla A-02 | — |
| RT-03.15 | Endurecimiento CIS + gestión centralizada de parches | ✅ | Ansible F-02 + CIS Benchmarks | Tabla F-02 | — |
| RT-03.16 | Monitoreo on-premise integrado a la plataforma de nube | ✅ | OTel ADOT + CloudWatch/X-Ray/AMP | Tabla F-01 | — |
| RT-03.17 | Enlace redundante con caminos y proveedores distintos | ✅ | **3 tecnologías por CD: fibra D-03 → satelital Starlink D-06 → LTE D-04 (SD-WAN multi-WAN, < 30 s)**; cross-docks: Starlink principal + LTE dual | Tabla D-03/D-04/**D-06**/E-01; Dim §3.6/§3.7; T-11 C27 | — |
| RT-03.18 | Gestión remota y centralizada de dispositivos de borde | ✅ | **N-13 — MDM gestionado (Android Enterprise / Zebra DNA)** + SSM (servidores) + Greengrass (borde IoT) | Tabla v06 §1.0(b) N-13; Lógica v6.2 §11.7; ADR-15; T-11 B11 | Componente con emplazamiento declarado desde el 06-09-2026 |
| RT-03.19 | Procesamiento en el borde valorado | ✅ | Greengrass B-02 + mini-WMS E-01 | Tabla B-02/E-01 | — |
| RT-03.20 | Ancho de banda dimensionado por sitio | ✅ | Tabla por sitio normal/peak (septiembre) + **camino satelital 1 TB (CDs) / 500 GB (cross-docks)** | Dim §3.7; T-11 C10/C11/C27 | — |
| RT-03.21 | Enlace privado dedicado o VPN para nube | ✅ | AWS Site-to-Site VPN IPsec IKEv2 BGP | Tabla D-01; Dim §3.6 | — |
| RT-03.22 | Acceso remoto con VPN/ZTNA | ✅ | AWS Verified Access + túnel de malla | Cloud §5.1 + §7.5 (v3.6) | — |
| RT-03.23 | Red inalámbrica segmentada por tipo de dispositivo | ✅ | VLANs (IoT, Bodega, Gestión, Servidores) | Tabla D-02 (mapeo verificado) | — |
| RT-03.24 | QoS y priorización de tráfico operacional | ✅ | QoS del firewall + failover WAN | Tabla D-01/D-04 | Deseable (valorado) |

---

# CAPÍTULO 04 — AMBIENTES, ENTREGA CONTINUA Y CONFIGURACIÓN

| ID | Descripción | Cumple | Componente | Sección | Hueco / Observación |
|---|---|---|---|---|---|
| RT-04.01 | Cinco ambientes habilitados (hito H3) | ✅ | Dev, QA, PreProd, Prod, DR | Consolidado (5 ambientes + DR); E-25/H3 | Coherencia con Art. 3°/Transversales |
| RT-04.02 | Preproducción equivalente a producción | ✅ | PreProd espejo de Prod | Proceso de desarrollo | — |
| RT-04.03 | Control de versiones con ramas protegidas y revisión por pares | ✅ | Repositorio + ramas protegidas + PR | Proceso de desarrollo §7.6 | — |
| RT-04.04 | Trazabilidad requerimiento→cambio→prueba→despliegue | ⚠️ | Matriz de trazabilidad | Registro de requerimientos (Subdoc 3) | Formalizar vínculo con PR y despliegue en la matriz |
| RT-04.05 | CI con compilación, unit, SAST, composición | ✅ | CodeBuild + SonarQube/CodeGuru + SCA | Cloud §5.6 (RT-11.22); §7.6 | — |
| RT-04.06 | Despliegues automatizados y reproducibles | ✅ | Pipeline CI/CD con rollout/rollback | Cloud §7.6 | — |
| RT-04.07 | Estrategia de despliegue sin interrupción | ✅ | Blue-green/canary + rolling (clúster) | Dim §7.5 (RT-10.06) | — |
| RT-04.08 | Configuración externalizada del artefacto por ambiente | ⚠️ | Variables/SSM Parameter Store | Proceso de desarrollo | Formato y repo del config por ambiente a formalizar |
| RT-04.09 | Secretos en gestor con rotación y auditoría | ✅ | AWS Secrets Manager / KMS; PAM | Cloud §5.2/§5.6; Dim §9.2 | — |
| RT-04.10 | Migraciones de esquema versionadas y reversibles | ✅ | Migraciones BDD versionadas | Proceso de desarrollo / BD | — |
| RT-04.11 | Cobertura de pruebas ≥ 70 % con umbral bloqueante | ✅ | Umbral declarado en CI | Proceso de desarrollo / T-13 | — |
| RT-04.12 | Frecuencia de despliegue y tiempo a producción declarados | ⚠️ | Métricas DORA | Proceso de desarrollo | Declarar valores objetivo |
| RT-04.13 | Ambientes no productivos apagados/reducidos fuera de horario | ✅ | Eco ambientes; RT-15.02 | Cloud §8; RT-04.13 | — |
| RT-04.14 | Ambientes efímeros por rama/incidencia valorados | ⚠️ | Ephemeral environments (optativo) | Proceso de desarrollo | Deseable; decidir alcance |

---

# CAPÍTULO 06 — SITE PRINCIPAL ON-PREMISE

| ID | Descripción | Cumple | Componente | Sección | Hueco / Observación |
|---|---|---|---|---|---|
| RT-06.01 | Espacio de uso exclusivo aislado (tipología) | ✅ | Sala Técnica Secundaria Talca habilitada a nuevo | Sala §8 (RT-06.01); Tabla A-01 (tipología) | Nota mapeo: caso cita RT-06.01 como tipología; transversal lo usa para exclusividad/aislamiento |
| RT-06.02 | Muros no estructurales con blindaje perimetral | ✅ | Recinto de sala (cerramiento perimetral, puertas controladas) | Sala §2/§3 (catch-all §8) | Declarar material/planeamiento en detalle de obra |
| RT-06.03 | Plano de distribución interna con zonas | ✅ | Plano de zonificación (14 recintos, 3 líneas) | Sala §3.2 (RT-06.03) | — |
| RT-06.04 | Piso técnico, canalización y cableado certificado | ✅ | Piso técnico 40 cm, Cat 6A + OM4 certificado | Sala §6.4 | — |
| RT-06.05 | Racks de servidores independientes de comunicaciones | ✅ | R01 vs R02, ocupación/margen por rack | Sala §6.1/§6.2 (RT-06.05) | — |
| RT-06.06 | Obra civil de separación: cargo del CLIENTE, especificación del PROPONENTE | ✅ | Especificación en Sala v02; cargo declarado | Sala §2; Tabla A-01 (TCO) | Declarar plazo de obra civil en Carta Gantt |
| RT-06.07 | UPS ininterrumpido con autonomía ≥ 30 min | ✅ | UPS doble conversión N+1, 6 kVA, ≥ 30 min | Sala §5.1/§5.2/§8 (RT-06.07) | — |
| RT-06.08 | Generación autónoma ≥ 24 h con estanque | ✅ | Generador 12 kVA, estanque 24 h + contrato de reabastecimiento | Sala §5.2/§8 (RT-06.08) | — |
| RT-06.09 | Instalación eléctrica independiente y conforme a norma | ✅ | Acometida/tablero independiente; NCh 2777 (patio generador) | Sala §5.1/§5.2 | Declarar explícitamente norma de baja tensión (NCh 4/2003) |
| RT-06.10 | Medición semestral de instalaciones eléctricas | ✅ | Termografía semestral + informe; sincronizada con DR | Sala §5.1/§8 (RT-06.10) | — |
| RT-06.11 | kW, factor de potencia y eficiencia declarados | ✅ | ≈ 3 kW TI, FP ≥ 0,95, PUE 1,7 | Sala §5.2/§5.4/§8 (RT-06.11) | — |
| RT-06.12 | Redundancia de alimentación 2N o N+1 (valorada) | ✅ | UPS N+1 + ATS + generador | Sala §5.1/§5.2 | Deseable; se valora con N+1 + transferencia automática |
| RT-06.13 | Climatización de precisión N+1 | ✅ | 2 CRAC 12.000 BTU/h en N+1, ASHRAE 18-27 °C | Sala §5.3 | — |
| RT-06.14 | Monitoreo en línea de temperatura/humedad/agua | ✅ | Sensores al DCIM/BMS del NOC + alarmas | Sala §4.2 (RT-06.14) | — |
| RT-06.15 | Estrategia de contención de pasillo frío | ✅ | Pasillo frío confinado (ahorro 15-30 %) | Sala §3.1/§5.3 | — |
| RT-06.16 | Detección temprana por aspiración láser | ✅ | AnaLASER o equivalente | Sala §4.2 (RT-06.16) | — |
| RT-06.17 | Extinción automática con agente limpio | ✅ | FM-200, NFPA 75/2001, botón de aborto | Sala §4.2 (RT-06.17) | — |
| RT-06.18 | Extintores portátiles habilitados y certificados | ✅ | ABC/CO₂ por recinto, recarga anual | Sala §4.2 (RT-06.18) | — |
| RT-06.19 | Detección y extinción integradas al monitoreo y NOC | ✅ | Integración al DCIM/BMS + alarma NOC | Sala §4.2/§4.4 | — |
| RT-06.20 | Ingreso con seguridad física y biometría facial | ✅ | Biometría facial principal + AFIS respaldo | Sala §4.1 (RT-06.20) | — |
| RT-06.21 | Bitácora auditable de ingreso/egreso | ✅ | Bitácora electrónica por persona y puerta | Sala §4.1 (RT-06.21) | — |
| RT-06.22 | Espacio de atención entre acceso principal y pasillo | ✅ | Control de acceso/custodia 10 m² (1ª Línea) | Sala §2/§3.2 | — |
| RT-06.23 | Acceso al término del pasillo, una persona a la vez | ✅ | Esclusa + re-verificación biométrica | Sala §4.1 (RT-06.23) | — |
| RT-06.24 | Videovigilancia IP con retención ≥ 30 días + respaldo | ✅ | 7 cámaras IP, respaldo secundario auditable | Sala §4.3 (RT-06.24) | — |
| RT-06.25 | Procedimiento de acceso de terceros con acompañamiento | ✅ | Recorrido de visita, custodia + acompañamiento | Sala §3.2 | — |
| RT-06.26 | Custodia física de medios de respaldo para sitio primario en otro sitio | ✅ | Servicio de custodia/transporte de medio físico transportable a otro lugar + recinto de custodia; bóveda externa; bitácora RT-06.28; S3 complementaria | Sala v02 §4.5; Tabla v06 D-05 | **CERRADO (v02/v06c)** |
| RT-06.27 | Recinto de custodia con condiciones de luminosidad/humedad/ventilación | ✅ | Recinto 10 m² 2ª línea: LED sin UV ≤300 lux, HR 40–60 %, ventilación forzada, 18–27 °C, monitoreo DCIM/BMS | Sala v02 §4.5 | **CERRADO (v02/v06c)** |
| RT-06.28 | Inventario de medios con rotación y verificación de legibilidad | ✅ | Inventario + rotación + registro de movimientos (bitácora NOC) | Sala §8 (RT-06.28); Dim §6.5 | — |
| RT-06.29 | Espacio físico para personal de operación | ✅ | NOC 14 m² (DCIM/BMS, consola) | Sala §2 | — |
| RT-06.30 | Espacio de operación separado de la sala de equipos | ✅ | NOC separado, «ver sin entrar» | Sala §2/§3.2 | — |
| RT-06.31 | Sanitarias, zonas de emergencia y áreas exteriores existentes | ✅ | Baños existentes del edificio en uso | Sala §8 (RT-06.31) | — |
| RT-06.32 | Rutas físicas distintas con ingreso en extremos distintos | ✅ | MMR con 2 ductos (fibra + LTE) + **antena Starlink en techumbre con canalización protegida (RT-06.32)** | Sala §6.4/§2; Dim §4.1 (D-06) | — |
| RT-06.33 | Conectividad, canalizaciones y ductos provistos | ✅ | Cableado certificado + ductos de operadores | Sala §6.4 | — |
| RT-06.34 | Especificaciones nuevas o mejores valoradas | ✅ | TIER II, PUE 1,7, AnaLASER, CCTV 30 días, **camino satelital Starlink (D-06) en los 5 sitios** | Sala (mejoras declaradas); T-11 C27 | Deseable (valorado) |

---

# CAPÍTULO 07 — SITE SECUNDARIO Y RECUPERACIÓN ANTE DESASTRES

| ID | Descripción | Cumple | Componente | Sección | Hueco / Observación |
|---|---|---|---|---|---|
| RT-07.01 | Modalidad activo/pasivo(activo) declarada y justificada | ✅ | Talca activo · Aurora pasiva promueble · Concepción activa autónoma | Dim §5.1 | — |
| RT-07.02 | Distancia del sitio secundario + amenazas comunes | ✅ | ~2.300 km (nube) y ~250-400 km (Concepción); análisis de amenazas | Dim §5.2; Cloud §7 | — |
| RT-07.03 | Replicación continua con medición y alerta de retraso | ✅ | DMS CDC (WAL lógico) → Aurora; alarmas lag 5/15 min | Dim §5.3 | — |
| RT-07.04 | RTO ≤ 4 h y RPO ≤ 15 min | ✅ | DRP documentado | Dim §5.6; Cloud §7 | — |
| RT-07.05 | Procedimiento de conmutación documentado y automatizado | ✅ | Runbook de conmutación (6 pasos, semiautomático) | Dim §5.4 | — |
| RT-07.06 | Procedimiento de retorno con reconciliación | ✅ | Failback con ventanilla de escritura única + reconciliación | Dim §5.5; Cloud §7 | — |
| RT-07.07 | Prueba DR 2×/año con informe | ✅ | Prueba semestral con RTO/RPO medidos + plan de corrección | Dim §5.6 | Coherencia Art. 20 |
| RT-07.08 | Conmutación automática ante indisponibilidad (valorada) | ✅ | Detección + verificación + promoción (semi-automática); Cloud automatización | Dim §5.4; Cloud §7.5 (v3.6) | Deseable (valorado) |
| RT-07.09 | Política de respaldo 3-2-1-1-0 | ✅ | Datos + snapshot + S3; 2 medios; fuera de sitio; inmutable; 0 errores | Tabla D-05; Dim §1.2.4 | — |
| RT-07.10 | Respaldos cifrados en reposo y tránsito, clave independiente | ✅ | NAS WORM cifrado + S3 SSE-KMS + TLS/VPN | Dim §5.7 | — |
| RT-07.11 | Copias inmutables contra borrado/modificación | ✅ | S3 Object Lock + Backup Vault Lock | Tabla D-05; Dim §5.7 | — |
| RT-07.12 | Prueba de restauración mensual documentada | ✅ | Verificación mensual «0 errores» | Dim §5.7/§5.9 | — |
| RT-07.13 | Frecuencia, retención y tiempo de restauración por dominio | ✅ | Tabla por dominio de datos | Dim §5.8 | — |
| RT-07.14 | Restauración granular (valorada) | ✅ | PITR PostgreSQL + archivo/snapshot | Dim §5.9 | Deseable (valorado) |

---

# CAPÍTULO 08 — HARDWARE, PUESTOS DE TRABAJO Y TERRENO

| ID | Descripción | Cumple | Componente | Sección | Hueco / Observación |
|---|---|---|---|---|---|
| RT-08.01 | Equipamiento de cómputo especificado (marca, modelo, CPU, RAM) | ✅ | Clúster 3 × Dell R6615/DL325 + NAS + red | Dim §4.1 | — |
| RT-08.02 | Almacenamiento redundante con monitoreo predictivo | ✅ | RAID 10 + Hot-Spare + Ceph; S.M.A.R.T./NVMe | Dim §1.2.2 + §6.1 | — |
| RT-08.03 | Conmutadores, firewalls y balanceadores en HA | ✅ | Stack/MLAG + clúster A/P sin SPOF; **SD-WAN multi-WAN (D-01) sobre 3 enlaces (D-03/D-06/D-04)** | Dim §3.8 | — |
| RT-08.04 | Fuentes redundantes y circuitos eléctricos distintos | ✅ | Doble fuente + PDU A/B por rack | Sala §6.2; Dim §3.8 | — |
| RT-08.05 | Margen de crecimiento declarado y procedimiento de ampliación | ✅ | 47 % vCPU / 73 % RAM / 68 % Ceph + procedimiento | Dim §6.2 | — |
| RT-08.06 | Equipamiento nuevo, sin uso previo, garantía de fábrica | ✅ | Declaración + garantías (server 5 años, OneCare) incluye **5 kits Starlink nuevos** | Dim §6.3; Tabla §4.2; T-11 C27 | — |
| RT-08.07 | Estaciones de trabajo especificadas | ✅ | 5 Talca + 3 Concepción (PC + 2×24") | Dim §4.2 | — |
| RT-08.08 | Ergonomía NCh 2527 y equipos certificados | ✅ | Ergonomía + Energy Star + 80 Plus Gold | Dim §6.4 | Declarar informe NCh 2527 junto al mobiliario |
| RT-08.09 | Estaciones gestionadas con cifrado y control de extraíbles | ✅ | EDR + Ansible, whitelist USB, MAM | Dim §6.5 (RT-08.09) | — |
| RT-08.10 | Dispositivos de terreno con marca, modelo, cantidad, costo | ✅ | Parque completo + USD referencial + accesorios/consumibles | Tabla §4 (RT-08.10) | — |
| RT-08.11 | Especificación según condiciones reales de uso | ✅ | Freezer, IP, caídas, batería, 5G | Tabla §4 (MC9400/TC58e/EC55) | — |
| RT-08.12 | Grado de protección IP y resistencia a caídas declarados | ✅ | IP65/68, IP67, 2,4 m, −30 °C | Tabla §4 | — |
| RT-08.13 | Ciclo de vida, repuestos y reposición en 56 meses | ✅ | Plan por dispositivo + stock seco 10 % + **reposición Starlink 15 %/56 meses** | Tabla §4.1 (RT-08.13); T-11 C27 | — |
| RT-08.14 | Integración a la gestión centralizada de flota | ✅ | MDM/MAM + RT-03.18 en terminales | Tabla §4 (C-01/C-02/C-03) | — |
| RT-08.15 | Unidad de cada tipo para pruebas de aceptación | ✅ | Sección 4.3: 1 unidad por tipo, sin cargo, antes de la compra masiva (Etapa 1 mes 16 / Etapa 2 mes 21), acta Art. 18 | Tabla v06 §4.3 | **CERRADO (v06c)** — Deseable cumplido |
| RT-08.16 | Plan de ciclo de vida del equipamiento | ✅ | Plan por etapas (recepción → disposición) | Dim §6.7 | — |
| RT-08.17 | Borrado seguro y verificable de medios | ✅ | NIST 800-88/DoD 5220.22-M + certificado | Dim §6.8 | — |
| RT-08.18 | Disposición final con gestor autorizado | ✅ | REP Ley 20.920 + certificado | Dim §6.9 | — |
| RT-08.19 | Reacondicionamiento/extensión de vida útil (valorado) | ✅ | Reutilización interna cuantificada | Dim §6.10 | Deseable (valorado) |

---

# CAPÍTULO 09 — DESEMPEÑO, CAPACIDAD Y ESCALABILIDAD

| ID | Descripción | Cumple | Componente | Sección | Hueco / Observación |
|---|---|---|---|---|---|
| RT-09.01 | Cálculo de capacidad con supuestos de la volumetría del caso | ✅ | Dimensionamiento por volumetría real | Dim §1.5/§1.3; Cloud §3.5 | — |
| RT-09.02 | Soportar concurrencia y umbrales del 9.1 | ✅ | P95 2 s preventa; 260.000 líneas/mes | Cloud §3.5; Dim §1 | — |
| RT-09.03 | Crecimiento 3× en 3 años sin rediseño | ✅ | Margen y escala a 3 años (nodo/RAM/Ceph) | Dim §6.2 | — |
| RT-09.04 | Escalamiento horizontal automático | ✅ | ECS Auto Scaling + Ceph + aplicación | Cloud §3.5 | — |
| RT-09.05 | Componente cuello de botella identificado | ✅ | Escritura transaccional VM-02 PostgreSQL (05:30–07:00) + drenaje broker; detección OTel/Prometheus; PgBouncer+particionado+réplica lectura+4º nodo | Dim v05 §10.5 | **CERRADO (v05)** |
| RT-09.06 | Pruebas de carga 1,5× peak en PreProducción | ❌ | Plan de Pruebas (T-13) | Subdoc 9 | Comprometer en T-13 con volumetría del caso |
| RT-09.07 | Informe de pruebas de carga con curva y punto de saturación | ❌ | Plan de Pruebas (T-13) | Subdoc 9 | Ídem |
| RT-09.08 | Degradación controlada al superar capacidad | ✅ | Encolamiento + rate limit + mensaje explícito | Cloud §5.1; Tabla A-03 | — |
| RT-09.09 | Gestión de capacidad en Operación (proyección trimestral) | ✅ | Alerta 70 %/2 semanas + proyección trimestral + procedimiento de ampliación | Dim v05 §10.8; Dim §6.2 | **CERRADO (v05)** |
| RT-09.10 | Pruebas de carga periódicas en CI (valorado) | ⚠️ | CI/CD | Proceso de desarrollo | Deseable; valorar incorporar smoke de performance |

---

# CAPÍTULO 10 — DISPONIBILIDAD, CONTINUIDAD Y RESILIENCIA

| ID | Descripción | Cumple | Componente | Sección | Hueco / Observación |
|---|---|---|---|---|---|
| RT-10.01 | Disponibilidad mensual ≥ 99,9 % e2e sobre transacción crítica | ✅ | SLO e2e ≠ TIER II; clúster + WAN + UPS/gen + DRP | Sala §7/§8 (RT-10.01); Dim §7.1 | — |
| RT-10.02 | Clasificación de servicios y nivel del Art. 78° | ✅ | Crítico/alto/medio/bajo por impacto | Cloud §6.1 (v3.6) | — |
| RT-10.03 | BCP conforme ISO 22301 | ✅ | BCP del consolidado con ALC por servicio | Dim §7.2 | Formalizar BCP completo en Consolidado |
| RT-10.04 | Continuidad TIC conforme ISO/IEC 27031 | ✅ | Continuidad TIC con estructura de eventos | Dim §7.3 | Ídem |
| RT-10.05 | Mantenimientos fuera de ventana crítica con aviso ≥ 10 días | ✅ | Ventana 00:00-04:00 + aviso 10 días hábiles | Dim §7.4 | — |
| RT-10.06 | Despliegue sin interrupción | ✅ | Rolling/blue-green/canary; N+1 | Dim §7.5 | — |
| RT-10.07 | Pruebas de resiliencia por inyección de fallas | ✅ | Chaos semestral + pre-producción | Dim §7.6 | — |
| RT-10.08 | Comportamiento por dependencia externa documentado | ✅ | Matriz de dependencias (fallo/error/lentitud) | Dim §7.7 | — |
| RT-10.09 | Presupuesto de error por servicio crítico (valorado) | ✅ | ≤ 0,1 % (≈ 43 min/mes) desglosado | Dim §7.8 | Deseable (valorado) |

---

# CAPÍTULO 11 — SEGURIDAD DE LA INFORMACIÓN

| ID | Descripción | Cumple | Componente | Sección | Hueco / Observación |
|---|---|---|---|---|---|
| RT-11.01 | Arquitectura Zero Trust (NIST SP 800-207) | ✅ | Zero Trust por capas, microsegmentación | Cloud §5.1 (+§7.4) | — |
| RT-11.02 | Modelado de amenazas por componente (STRIDE) | ✅ | STRIDE por componente/integración | Dim §8.1 (v05) | — |
| RT-11.03 | Clasificación de la información con controles por nivel | ✅ | Público/Interno/Confidencial/Restringido | Dim §8.2 | — |
| RT-11.04 | Programa de vulnerabilidades con plazos 7/15/30 | ✅ | Escaneo semanal automatizado + plazos | Dim §8.3 | — |
| RT-11.05 | Matriz de controles trazable a ISO 27001/27002 | ⚠️ | Referencia única en doc. seguridad del consolidado | Dim §8.4 | Materializar la matriz completa de controles en el consolidado |
| RT-11.06 | Controles ISO 27017/27018 en nube | ✅ | AWS programas de conformidad + aplicación | Cloud §5.6 | — |
| RT-11.07 | Publicación por capa de borde (CDN/WAF/DDoS L3-4-7) | ✅ | CloudFront + WAF v2 + Shield | Cloud §5.1/§5.2 | — |
| RT-11.08 | TLS 1.3 con HSTS + gestión automatizada de certificados | ✅ | ACM + TLS 1.3 + HSTS preload | Cloud §5.6; Dim §8.5 | — |
| RT-11.09 | Cifrado en reposo con KMS y separación de funciones | ✅ | CMK por dato + dual control | Cloud §5.6; Dim §8.6 | — |
| RT-11.10 | Cifrado a nivel de campo de datos sensibles | ✅ | pgcrypto + KMS; tokenización PAN | Cloud §5.4 (v3.6); Dim §8.7 | — |
| RT-11.11 | Puerta de enlace con auth, cuotas, tasas, validación de esquema | ✅ | AWS API Gateway + Lambda authorizers | Cloud §5.1 (RT-11.11) | — |
| RT-11.12 | Protección contra bots con reto progresivo | ✅ | WAF + Challenge/CAPTCHA | Cloud §5.2/§5.4 (RT-11.12) | — |
| RT-11.13 | Superficie de exposición completa declarada | ✅ | Tabla dominios/puertos/servicios | Cloud §5.6 (RT-11.13); Dim §8.8 | — |
| RT-11.14 | Eventos centralizados, inalterables, con retención 12+24 meses | ✅ | SIEM WORM + S3 Object Lock; 12+24 meses | Dim §8.9; Cloud §5.6 | — |
| RT-11.15 | SIEM con casos de uso del proceso de negocio | ✅ | Casos logísticos (frío, fraude reparto, inventario) | Dim §8.10 | — |
| RT-11.16 | Detección y respuesta en endpoints y cargas de trabajo | ✅ | EDR F-03 + GuardDuty + Inspección | Tabla F-03; Cloud §5.2/§5.5 | — |
| RT-11.17 | SOC 24×7 con ubicación, dotación y procedimientos | ⚠️ | SOC declarado (L1 por turno + L2 on-call) | Dim §8.10 | Formalizar ubicación/dotación/procedimientos en doc. seguridad del consolidado |
| RT-11.18 | Plan de respuesta a incidentes con comunicación ≤ 2 h | ✅ | Fases + roles + comunicación ≤ 2 h | Dim §8.11 | — |
| RT-11.19 | Notificación de brechas ≤ 24 h y RCA ≤ 5 días hábiles | ✅ | Protocolo + plantillas | Dim §8.12 | — |
| RT-11.20 | Pentest por tercero independiente anual + pre-producción | ✅ | Pentest anual + pre-go-live | Dim §8.13 | — |
| RT-11.21 | Simulacros con el CLIENTE (valorado) | ✅ | Simulacro anual (ransomware/disponibilidad/frío) | Dim §8.14 | Deseable (valorado) |
| RT-11.22 | CI con SAST/SCA/DAST/imágenes + bloqueo ante críticos | ✅ | CodeBuild + Sonar/CodeGuru + ZAP + Inspector | Cloud §5.6 (RT-11.22) | — |
| RT-11.23 | SBOM CycloneDX/SPDX por versión | ✅ | Syft/Trivy + entrega al CLIENTE | Cloud §5.6 (RT-11.23) | — |
| RT-11.24 | Artefactos firmados y SLSA nivel 3 | ✅ | Sigstore/cosign + provenance SLSA 3 | Cloud §5.6 (RT-11.24) | — |
| RT-11.25 | Prohibición de datos productivos reales en no productivos | ✅ | Datos sintéticos + Macie | Cloud §5.6 (RT-11.25) | — |
| RT-11.26 | Proceso de aprobación de dependencias de terceros | ⚠️ | (CI/CD) | Proceso de desarrollo | Declarar criterios de licencia/mantenimiento/vulnerabilidades |
| RT-11.27 | Sin acceso interactivo directo a producción | ✅ | SSM Session Manager JIT + auditoría | Cloud §5.6 (RT-11.27) | — |
| RT-11.28 | Madurez OWASP SAMM (valorado) | ⚠️ | (Proceso de desarrollo) | Proceso de desarrollo | Deseable; evaluar SAMM inicial y reevaluación anual |

---

# CAPÍTULO 12 — IDENTIDAD, ACCESO Y GESTIÓN DE SESIONES

| ID | Descripción | Cumple | Componente | Sección | Hueco / Observación |
|---|---|---|---|---|---|
| RT-12.01 | Identidad centralizada con OIDC/OAuth 2.1 + LDAP | ✅ | Keycloak (Modelo B: autoridad en nube, caché local TTL 8 h) | Cloud §5.4 (RT-12.01) y §3.3 (v3.6); Tabla A-05 | Alineado: Cloud v3.6 + Tabla v06 (maestro en nube, caché local A-05 TTL 8 h, D6) |
| RT-12.02 | SSO con cierre de sesión propagado | ✅ | Keycloak back-channel logout | Cloud §5.4 (RT-12.02) | — |
| RT-12.03 | MFA obligatoria (admins, acceso remoto, privilegiado) | ✅ | TOTP/FIDO2 + OTP externos | Cloud §5.4; Dim §9.2 | — |
| RT-12.04 | Factores resistentes a suplantación tipo FIDO2/passkeys | ✅ | WebAuthn/passkeys para administradores | Cloud §5.4 (v3.6) | Deseable |
| RT-12.05 | RBAC (+ABAC) con matriz de segregación SoD | ✅ | RBAC/ABAC + matriz SoD | Cloud §5.4; Dim §9.1 | — |
| RT-12.06 | PAM con elevación temporal y grabación de sesión | ✅ | IAM Identity Center + SSM JM + bóveda | Cloud §5.6 (RT-12.06); Dim §9.2 | — |
| RT-12.07 | Política de sesión (duración, inactividad, revocación, concurrencia) | ✅ | Tabla de política de sesión | Cloud §5.4 (v3.6); Dim §9.3 | — |
| RT-12.08 | Credenciales firmadas de vida breve con refresco rotatorio | ✅ | JWT corta vida + refresh con rotación | Cloud §5.4 (RT-12.08); Dim §9.4 | — |
| RT-12.09 | Auditoría del ciclo de vida de la identidad con no repudio | ✅ | SIEM + CloudTrail + Keycloak events | Cloud §5.4 (RT-12.09); Dim §9.5 | — |
| RT-12.10 | Aprovisionamiento/desaprovisionamiento SCIM ≤ 24 h | ✅ | SCIM + MDM + baja ≤ 24 h | Dim §9.6 | — |
| RT-12.11 | Autenticación adaptada al perfil de terreno (guantes, compartidos, sin correo) | ✅ | TTL 8 h + OTP offline + terminales con guantes | Tabla A-05; C-01/C-02; Dim §9.3 | — |
| RT-12.12 | Usuarios externos con registro/verificación/recuperación autoservidos | ✅ | Portal autoservido (OTP + verificación) | Cloud §5.4 (v3.6) | — |
| RT-12.13 | Cuenta de emergencia (break-glass) con custodia, control y auditoría | ✅ | Custodia compartida + rotación + auditoría | Cloud §5.4 (v3.6); Dim §9.7 | — |

---

# CAPÍTULO 14 — OBSERVABILIDAD Y GESTIÓN DEL SERVICIO

| ID | Descripción | Cumple | Componente | Sección | Hueco / Observación |
|---|---|---|---|---|---|
| RT-14.01 | Observabilidad unificada nube + on-premise (OTel, correlación por ID) | ✅ | **Plataforma única**: ADOT on-premise (buffer 24 h) → AMP + CloudWatch Logs + X-Ray + Grafana OSS (ADR-14) | Tabla F-01; Cloud §8 | — |
| RT-14.02 | Acceso del CLIENTE a tableros con datos reales y exportación | ✅ | Grafana + cuentas federadas Keycloak | Cloud §8; Dim §9.8 | — |
| RT-14.03 | SLI sobre experiencia real (no solo sintética) | ✅ | P95 e2e, sync, serialización, DAT/RUM | Dim §9.9 | — |
| RT-14.04 | Alertamiento por síntomas de negocio | ✅ | OTIF/bloqueos/colas/devoluciones/discrepancias | Dim §9.10 | — |
| RT-14.05 | Libro de operación y guías de resolución | ✅ | Runbooks por escenario | Dim §9.11 | — |
| RT-14.06 | RCA obligatorio en incidentes críticos (≤ 5 días hábiles) | ✅ | RCA con 5 Why + seguimiento | Dim §9.12; Cloud §5.4 | — |
| RT-14.07 | Logs sin datos sensibles ni credenciales, acceso auditado | ✅ | Masking/seudonimización + acceso por rol | Dim §9.13 | — |
| RT-14.08 | Retención de métricas/logs/trazas y costo asociado | ✅ | Tabla on-line/archivo + costo | Dim §9.14 | — |
| RT-14.09 | Detección proactiva de anomalías (valorado) | ✅ | Baselines estadísticos sobre series de tiempo (ingesta IoT, TPS, latencias, OTIF) — Prometheus/PromQL + Grafana, **sin modelos de IA/ML** | Dim §9.15 | Deseable (valorado) |

---

# CAPÍTULO 15 — SOSTENIBILIDAD, EFICIENCIA Y CERTIFICACIONES

| ID | Descripción | Cumple | Componente | Sección | Hueco / Observación |
|---|---|---|---|---|---|
| RT-15.01 | Dimensionamiento ajustado a demanda real con factor de utilización | ✅ | P95/perfil de carga; utilización declarada | Dim §1.5; Cloud §3.5/§4.5 | — |
| RT-15.02 | Ambientes no productivos apagados/reducidos | ✅ | Eco ambientes (RT-04.13) | Cloud §8 | — |
| RT-15.03 | Huella de carbono anual con metodología | ✅ | Métrica de huella + metodología | Cloud §4.5 (v3.6) | — |
| RT-15.04 | PUE del recinto e intensidad de carbono de la región | ✅ | PUE 1,7 + intensidad de carbono sa-east-1 | Sala §5.4; Cloud §4.5 (v3.6) | — |
| RT-15.05 | Regiones con menor intensidad de carbono (valorado) | ✅ | Análisis comparativo regional | Cloud §4.5 (v3.6) | Deseable (valorado) |
| RT-15.06 | Metas de reducción de consumo en Operación (valorado) | ⚠️ | (Operación/Sostenibilidad) | Subdoc 8/Operación | Deseable; definir meta y reporte anual |
| RT-15.07 | Certificaciones con copia vigente y código de verificación | ⚠️ | Empresa proponente (por definir) | Oferta corporativa | Acreditar certificados vigentes (27001/9001) |
| RT-15.08 | Personal certificado efectivamente asignado con dedicación | ⚠️ | Equipo LafroX (roles definidos) | T-15 / oferta | Completar certificaciones y dedicación por rol |
| RT-15.09 | Mantener vigentes las certificaciones durante 56 meses | ⚠️ | Compromiso contractual | Oferta | Declarar plan de reposición conforme Art. 76° |

---

## HALLAZGOS DE LA AUDITORÍA (05-09-2026)

**Mejoras cerradas por la actualización on-premise (Sala v02 · Dim v05 · Tabla v06 · v06c):**
- Cap. 6: RT-06.07 (UPS ≥ 30 min), RT-06.08 (generador 24 h + contrato), RT-06.11 (FP ≥ 0,95 + PUE medido), RT-06.14 (sensores en línea), RT-06.18 (extintores por recinto), RT-06.23 (una persona + re-verificación), RT-06.26 y RT-06.27 (custodia física de medios: servicio de custodia/transporte de medio transportable + recinto 10 m² con condiciones ambientales — Sala v02 §4.5 / Tabla v06 D-05), RT-06.28 (inventario de medios), RT-06.31 (sanitarias existentes).
- Cap. 7: RT-07.01 a RT-07.14 completos en Dim PARTE 5 (modalidad, distancia, replicación, conmutación, retorno, prueba 2×/año, respaldos 3-2-1-1-0, cifrado, inmutabilidad, restauración mensual y granular).
- Cap. 8: RT-08.02 (S.M.A.R.T.), RT-08.05 (ampliación), RT-08.06 (equipo nuevo — incluye 5 kits Starlink), RT-08.08 (eficiencia), RT-08.09 (extraíbles), RT-08.10/08.13/§8.4 (Tabla v06 §4-4.2 — incluye kit Starlink con reposición 15 %), RT-08.15 (unidad por tipo para pruebas de aceptación — Tabla v06 §4.3), RT-08.16-08.19 en Dim §6.7-6.10.
- Cap. 9: RT-09.05 (cuello de botella = escritura VM-02 + drenaje broker, detección y resolución — Dim v05 §10.5), RT-09.09 (gestión trimestral de capacidad con alerta 70 % — Dim v05 §10.8).
- Cap. 10: RT-10.01 (SLO e2e ≠ TIER II), RT-10.03 (ISO 22301), RT-10.04 (ISO 27031), RT-10.05/10.06/10.07/10.09.
- Cap. 11: RT-11.02 (STRIDE), RT-11.03, RT-11.04, RT-11.08/11.09/11.10, RT-11.13, RT-11.14/11.15, RT-11.18/11.19/11.20.
- Cap. 12/14: RT-12.05-12.13, RT-14.02-14.09.

**Resultado global T-12:** **182 ✅/197 = 92,4 %** · ⚠️ 13 · ❌ 2.

**Huecos pendientes:**
- **❌ (2):** RT-09.06 y RT-09.07 (pruebas de carga 1,5× peak con informe y curva de saturación) → se cierran en el **T-13 (Plan de Pruebas, Subdoc 9)**.
- **⚠️ (13):** 04.04/04.08/04.12/04.14 (proceso de desarrollo); 09.10 (Deseable: carga en CI); 11.05/11.17/11.26/11.28 (matriz ISO/SOC/dependencias/SAMM); 15.06-15.09 (metas de reducción y certificaciones de la empresa proponente).
- **Reconciliación pendiente:** ~~Cloud §3.3/§5.4 aún declara Keycloak maestro en VM-05 (on-premise)~~ **RESUELTO**: el documento cloud pasó a Modelo B en su **v3.6** (§3.3, §3.5, §5.4, §7.3, §7.10, L-02, Apéndice C) — Keycloak maestro en nube (ECS/Fargate), caché local A-05 de solo lectura TTL 8 h (VM-05/VM-C03), sin maestro on-premise ni promoción local. Queda consolidado en `Arquitectura_Fisica_Hibrida_Consolidada_Caso02_v02.md` (**D-AL-18**, redactada el 06-09-2026 — el registro saltaba de D-AL-17 a D-AL-19 y esta referencia quedaba rota).

**Cierre de la auditoría de coherencia del Subdocumento 4 (06-09-2026).** Se resolvieron las divergencias entre la arquitectura lógica y la física que afectaban a esta matriz:

| Hallazgo | Resolución | Efecto en el T-12 |
|---|---|---|
| Puerta de enlace declarada como Kong en tres ADR | **Amazon API Gateway** (D8 · **ADR-13**) | RT-11.11, RT-05.16/05.18 quedan sustentados por un único componente coherente en lógica, física y costo |
| Prometheus/Grafana/Loki on-premise sin VM dimensionada | **Plataforma única**: ADOT con buffer de 24 h → AMP, CloudWatch, X-Ray, Grafana OSS (**ADR-14**) | RT-03.16 y RT-14.01–14.09 se responden con «la misma plataforma que la nube», como exige el Art. 16.4 |
| HashiCorp Vault sin emplazamiento físico | **Secrets Manager + SSM** en N-12 (**ADR-15**) | Art. 21.4 y RT-04.09 sustentados por un componente emplazado y costeado (Art. 16.2) |
| MDM mencionado sin componente | **N-13** en la tabla de emplazamiento y en el T-11 B11 | RT-03.18 y RT-08.14 dejan de apoyarse en una mención genérica |
| Retención citada contra RT-05.10 | Se responde contra **RT-16.10** | Corrige el mapeo del Cap. 15 del caso; el desajuste se eleva como consulta (Art. 43.3) |
| «Flutter» en el dimensionamiento on-premise | **Kotlin (Android nativo)**, conforme a ADR-07 | RT-13.08 y RT-17.01 quedan sustentados por un solo marco de desarrollo |

*Documento T-12_ArqFisica · v05-09-2026 · LafroX — Caso 02 Logística.*