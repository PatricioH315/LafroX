# Subdocumento 4.2.d-e — Especificaciones Data Center Primario y Secundario
**Propuesta técnica TFEP-01/2026 — Caso 02 Logística — LafroX**
*Referencia: T-21 §4.2 (d) DC Primario · (e) DC Secundario — RT-06 / RT-07 BTT*

---

## Mapa de sitios on-premise

`mermaid
graph TD
    subgraph "SITIO PRINCIPAL — CD TALCA (Sala técnica secundaria)"
        ST["🏢 Sala técnica secundaria\n32 m² sala blanca\n+141 m² recintos apoyo\nTIER II · 99,95%"]
        NOC["👁️ NOC / Monitoreo\n14 m² · DCIM/BMS\n24×7"]
        GEN["⚡ Patio generador\n20 m² · exterior\n12 kVA · 24 h"]
    end

    subgraph "SITIO SECUNDARIO — CD CONCEPCIÓN (Gabinete de borde)"
        GBC["📦 Gabinete de borde\n12U · 600×1200\nActivo autónomo"]
    end

    subgraph "PLATAFORMAS CROSS-DOCKING (×3)"
        XD1["📦 Curicó · 12U"]
        XD2["📦 Chillán · 12U"]
        XD3["📦 Los Ángeles · 12U"]
    end

    subgraph "NUBE (DR / Secundario)"
        AWS["☁️ AWS región Chile/SA\nActivo-pasivo\nRTO ≤4h · RPO ≤15min"]
    end

    ST <-->|"Fibra + LTE + Starlink\n3 caminos, conmutación <30s"| AWS
    ST <-->|"VPN / SD-WAN"| GBC
    ST <-->|"Starlink + LTE dual"| XD1
    ST <-->|"Starlink + LTE dual"| XD2
    ST <-->|"Starlink + LTE dual"| XD3
    NOC --- ST
    GEN --- ST
`

---

## Parte A — Data Center Primario (T-21 §4.2.d)

### A.1 Tipología y justificación

| Sitio | Tipología BTT | Justificación |
|---|---|---|
| **CD Talca** | Sala técnica **secundaria** | Cómputo sustantivo para operación desconectada 24 h (RT-03.10); núcleo de aplicación en nube. |
| **CD Concepción** | **Gabinete de borde** | Continuidad local en ventana de reparto; sin fibra; conectividad exclusiva red móvil. |
| **Cross-docks ×3** | **Gabinete de borde** | Ventana operación 3 h; sin almacenamiento propio; solo WMS reducido. |

---

### A.2 Plano de distribución interna (RT-06.03)

Ver: Diagramas/RT-06_DataCenter/DC01a_Plano_Distribucion.png

**7 zonas separadas por peligro (RT-06.03):**

| Zona | Recinto(s) | m² |
|---|---|---|
| Generadores | Patio exterior | 20 |
| Baterías | Sala UPS + VRLA N+1 | 14 |
| Climatización | 2 CRAC precisión | 12 |
| Servidores | Sala blanca (D) · 4 racks | 32 |
| Comunicaciones | MMR + NOC | 24 |
| Trabajo | Control acceso, reuniones, taller, bodega | 46 |
| Respaldo | Custodia de medios | 10 |

**3 líneas de acceso:**
- 1.ª línea: Recepción/apoyo (tarjeta de proximidad + registro guardia)
- 2.ª línea: Pasillo de servicio técnico (tarjeta + PIN)
- 3.ª línea: Sala blanca (esclusa biométrica facial + antipassback — RT-06.20/23)

---

### A.3 Obra y habilitación (RT-06.01 a RT-06.06)

| RT | Respuesta |
|---|---|
| RT-06.01 | Espacio exclusivo, aislado, acceso independiente del área de bodega |
| RT-06.02 | Blindaje: planchas acero laminado 1,5 mm sobre metalcon (ASTM D1037) |
| RT-06.03 | Plano entregado — ver §A.2 y DC01 |
| RT-06.04 | Piso técnico 40 cm, Cat6A/OM4, certificación Fluke por enlace |
| RT-06.05 | R01 servidores // R02 comunicaciones — independientes |
| RT-06.06 | Obra civil: cargo del CLIENTE. Especificación y coordinación: cargo LafroX |

---

### A.4 Energía (RT-06.07 a RT-06.12)

Ver: Diagramas/RT-06_DataCenter/DC02_Cadena_Electrica.png

**Cadena eléctrica 7 eslabones:** Empalme → Tablero general → ATS/TTA (8-15 s) → UPS 6 kVA N+1 (≥30 min) → PDU rack A/B → Fuente doble equipo → Servidor.

| RT | Valor declarado |
|---|---|
| RT-06.07 | UPS 6 kVA doble conversión N+1, autonomía ≥30 min plena carga |
| RT-06.08 | Generador 12 kVA, estanque 24 h, contrato reabastecimiento |
| RT-06.09 | Empalme exclusivo, puesta a tierra NCh Elec. 2777 |
| RT-06.10 | Revisión semestral con informe (incluido en Subdoc 11) |
| RT-06.11 | Carga TI: 3,1 kW · PUE: 1,7 · FP ≥ 0,95 |
| RT-06.12 (Deseable) | UPS N+1 implementado; doble acometida evaluada en diseño de obra |

---

### A.5 Climatización (RT-06.13 a RT-06.15)

| RT | Respuesta |
|---|---|
| RT-06.13 | 2 CRAC precisión ~12.000 BTU/h c/u, N+1, ASHRAE TC 9.9: 18-27°C, 40-60% HR |
| RT-06.14 | Sensores T/HR/agua integrados a DCIM/BMS del NOC, alertas automáticas |
| RT-06.15 (Deseable) | Pasillo frío confinado 1,2 m (cerramiento + techo + puertas correderas); mejora PUE ~0,15 |

---

### A.6 Detección y extinción (RT-06.16 a RT-06.19)

| RT | Respuesta |
|---|---|
| RT-06.16 | AnaLASER (o equiv.) con tubería aspiración en sala blanca y 2.ª línea |
| RT-06.17 | FM-200 sala dedicada 5 m², cañería corta a sala blanca, NFPA 2001, aprobación UL |
| RT-06.18 | 2 extintores CO₂ en acceso a sala blanca, mantención y certificación vigentes |
| RT-06.19 | Tablero control integrado DCIM/BMS; alertas NOC 24×7 + contraparte CLIENTE |

---

### A.7 Seguridad física y control de acceso (RT-06.20 a RT-06.25)

`mermaid
flowchart LR
    EXT([Exterior]) -->|"Credencial provisional\nRegistro guardia"| L1
    subgraph L1 ["1.ª LÍNEA — Apoyo"]
        CAC["Control acceso\ny custodia"]
        REU["Reuniones"]
        TAL["Taller"]
        BOD["Bodega"]
    end
    L1 -->|"Tarjeta proximidad\nRegistro auditable"| L2
    subgraph L2 ["2.ª LÍNEA — Servicio técnico"]
        direction LR
        ELE["Acometida\neléc."]
        MMR["MMR\nComun."]
        UPS2["UPS+\nBat."]
        EXT2["FM-200"]
        CLI["Clima"]
        MED["Custodia\nmedios"]
    end
    L2 -->|"ESCLUSA: biometría facial\n+ antipassback\n1 persona a la vez\nRT-06.20/23"| L3
    subgraph L3 ["3.ª LÍNEA — Sala blanca + NOC"]
        SB["Sala blanca\n32 m²\n4 racks"]
        NOC2["NOC\nVentana interior"]
    end
    style L3 fill:#E8F5E9,stroke:#1B5E20,stroke-width:2px
`

| RT | Respuesta |
|---|---|
| RT-06.20 | Lector facial 3D + AFIS respaldo en esclusa 3.ª línea |
| RT-06.21 | Log inmutable DCIM/BMS: persona, fecha, hora, motivo; retención 5 años |
| RT-06.22 | Estación de enrolamiento en custodia (1.ª línea), fuera del recinto técnico |
| RT-06.23 | Esclusa doble factor + antipassback + torniquete 1 persona |
| RT-06.24 | 7 cámaras IP; grabación ≥30 días; respaldo secundario auditable |
| RT-06.25 | Acompañamiento obligatorio por personal LafroX; registro previo en agenda NOC |

---

### A.8 Respaldo y custodia de medios (RT-06.26 a RT-06.28)

| RT | Respuesta |
|---|---|
| RT-06.26 | Recinto 10 m² (2.ª línea); medios LTO-9 rotatorios; traslado fuera de sitio a solicitud del CLIENTE |
| RT-06.27 | LED sin UV · HR 40-60% · T 18-27°C · ventilación forzada |
| RT-06.28 | Inventario en DCIM/BMS; verificación legibilidad mensual; registro entrada/salida con responsable |

---

### A.9 Espacio de operación NOC (RT-06.29 a RT-06.31)

| RT | Respuesta |
|---|---|
| RT-06.29 | NOC 14 m²: estaciones de trabajo, pantallas DCIM, telefonía, Internet dedicado |
| RT-06.30 | Separado de sala blanca; acceso por 2.ª línea; ventana interior "ver sin entrar" |
| RT-06.31 | Uso de instalaciones sanitarias, evacuación y áreas exteriores del CD Talca existentes |

---

### A.10 Rutas de comunicaciones (RT-06.32 a RT-06.34)

`mermaid
graph LR
    F["Fibra óptica\n50 Mbps · Camino 1\nDucto Norte"] --> MMR["MMR\n2 ductos\nindependientes"]
    L["LTE 4G/5G\n10 Mbps · Camino 2\nDucto Sur"] --> MMR
    S["Starlink\n~200 Mbps · Camino 3\nDucto Sur"] --> MMR
    MMR --> SW["R02 Switch core\n+ Firewall HA"]
    SW -->|"Direct Connect / VPN"| AWS["☁️ AWS DR"]
    SW --> SB["Sala blanca\nR01 R03 R04"]
`

| RT | Respuesta |
|---|---|
| RT-06.32 | Fibra ingresa por ducto Norte; LTE + Starlink por ducto Sur; puntos físicamente separados |
| RT-06.33 | LafroX provee y gestiona los 3 enlaces, MMR, cableado certificado y ductos |
| RT-06.34 (Deseable) | Starlink + LTE dual con conmutación automática < 30 s supera especificación mínima |

---

### A.11 Elevación de racks R01–R04 (RT-06.05)

Ver: Diagramas/RT-06_DataCenter/DC03_Elevacion_Racks.png

| Rack | Función | 42U · Ocupación | Margen |
|---|---|---|---|
| R01 | Servidores y almacenamiento | ~29% (~12U) | ~20% reserva |
| R02 | Comunicaciones y seguridad | ~19% (~8U) | ~33% reserva |
| R03 | Distribución HDA + respaldo | ~19% (~8U) | ~30% reserva |
| R04 | Crecimiento 3 años | 0% | 100% libre |

---

### A.12 Gabinetes de borde (RT-06.01)

Ver: Diagramas/RT-06_DataCenter/DC04_Gabinetes_Borde.png

| Requisito borde | CD Concepción 12U | Cross-docks ×3 · 12U |
|---|---|---|
| Protección eléctrica | UPS interna ≥30 min + supresor | UPS interna ≥30 min |
| Control de acceso físico | Cerradura biométrica + registro | Cerradura biométrica + registro |
| Monitoreo remoto | T/HR + apertura → NOC Talca | T/HR + apertura → NOC Talca |
| Condiciones ambientales | Ventilación forzada | Ventilación forzada |

---

### A.13 Ficha técnica consolidada

Ver: Diagramas/RT-06_DataCenter/DC05_Ficha_Tecnica.png

| Parámetro | Valor declarado |
|---|---|
| Superficie sala blanca | 32 m² + ~141 m² apoyo |
| Racks | 4 × 42U; ocupación ~29% R01; R04 100% libre |
| Carga TI | 3,1 kW (25% holgura 3 años) |
| PUE | 1,7 diseño; medición continua; desvío >0,2 → plan mejora |
| UPS | 6 kVA doble conversión N+1 |
| Autonomía | ≥30 min; generador toma 8-15 s |
| Generador | 12 kVA · 24 h · contrato reabastecimiento |
| Clima | ~3,6 kW · 2 CRAC N+1 · free cooling |
| T / HR | 18-27°C · 40-60% (ASHRAE TC 9.9) |
| Disponibilidad recinto | TIER II (99,741%) |
| Disponibilidad e2e (contractual) | ≥99,9% (Art. 78°) — gap cubierto por DR en nube |
| Enlaces | Fibra 50 Mbps + LTE 10 Mbps + Starlink · 3 caminos · <30 s conmutación |
| RTO / RPO | ≤4 h / ≤15 min |
| Puertas controladas | 4 líneas (12 puertas); esclusa biométrica 3.ª línea |
| CCTV | 7 cámaras IP; ≥30 días en línea + respaldo secundario |

---

## Parte B — Data Center Secundario / DR (T-21 §4.2.e)

### B.1 Modalidad declarada (RT-07.01)

**Activo-pasivo:** site primario on-premise Talca + site DR en AWS (región Sudamérica/Chile).

| Criterio | Activo-activo | **Activo-pasivo (elegida)** |
|---|---|---|
| Costo | Alto (infraestructura duplicada en caliente) | Bajo (réplica + arranque bajo demanda) |
| RTO | Segundos | ≤4 h (cumple RT-07.04) |
| Complejidad | Alta | Media |
| Adecuación al caso | Excesivo para TIER II secundario | Proporcional |

### B.2 Distancia y análisis de amenazas (RT-07.02)

Site DR: **AWS São Paulo** (>2.800 km de Talca) como región primaria de DR. Amenazas evaluadas: zona sismogénica chilena, falla de ISP local, falla de suministro eléctrico → AWS tiene rutas de tránsito y suministro independientes.

### B.3 Replicación continua (RT-07.03)

`mermaid
flowchart LR
    DB_P["MariaDB/PostgreSQL\non-premise Talca"] -->|"AWS DMS / CDC\nDirect Connect 50 Mbps"| RDS_P["Aurora multi-AZ\nRegión primaria"]
    RDS_P -->|"Réplica asíncrona\nlag < 5 min · alerta si >5 min"| RDS_S["Aurora Replica\nRegión DR (São Paulo)"]
    RDS_P --> S3["S3 Object Lock\nCross-Region"]
    style RDS_S fill:#FFF9C4
    style S3 fill:#C8E6C9
`

Alerta NOC si lag >5 min; escalamiento a JP si lag >15 min (umbral RPO).

### B.4 RTO y RPO (RT-07.04)

| Métrica | Comprometido | Cómo se cumple |
|---|---|---|
| RPO | ≤15 min | Replicación lag <5 min normal; alerta a 5 min |
| RTO | ≤4 h | Arranque ECS desde ECR + promoción Aurora + Route 53 failover |

### B.5–B.6 Conmutación y retorno (RT-07.05 / RT-07.06)

`mermaid
sequenceDiagram
    participant NOC as NOC Talca
    participant AUTO as Terraform/Ansible
    participant DR as AWS DR Region
    participant CLI as Contraparte CLIENTE

    NOC->>CLI: Notificación T+0 (≤5 min)
    NOC->>AUTO: Aprobación conmutación
    AUTO->>DR: Promoción Aurora → primaria
    AUTO->>DR: Arranque ECS desde ECR
    AUTO->>DR: Route 53 failover
    DR-->>NOC: Servicio activo (RTO ≤4 h)
    Note over NOC,DR: --- Operación en DR ---
    AUTO->>DR: Sincronización inversa (reconciliación)
    AUTO->>NOC: Retorno a site primario
    NOC->>CLI: Confirmación retorno
`

### B.7 Respaldos 3-2-1-0 (RT-07.09 a RT-07.14)

`mermaid
graph TD
    SRC["Datos producción"] -->|"Copia 1 · inmutable"| S3I["S3 Object Lock WORM\nAES-256 KMS · retención RT-05.10\nProtegida vs credenciales admin"]
    SRC -->|"Copia 2 · cross-region"| S3CR["S3 Cross-Region Replication\nRegión DR"]
    SRC -->|"Copia 3 · local"| NAS["NAS on-premise R01\nLTO-9 rotatorio · cifrado"]
    NAS -->|"Traslado mensual"| CUST["Custodia física\nfuera del recinto"]
    S3I --> VER["Verificación restauración\nmensual · TRE medido\n0 errores"]
    S3CR --> VER
    NAS --> VER
    style S3I fill:#FFF9C4
    style S3CR fill:#C8E6C9
    style NAS fill:#BBDEFB
`

**Política de retención por dominio:**

| Dominio | Frecuencia | Retención | TRE est. |
|---|---|---|---|
| Base transaccional | Continua (PITR) + diario | 3 años online; 6 archivo | <4 h completo |
| Documentos tributarios | Diario incremental | 6 años | <1 h |
| Registros sanitarios / trazabilidad lote | Por evento | Vida útil + 6 m; mín. 5 años | <2 h |
| Registros temperatura | Cada 5 min (IoT) | 5 años | <4 h |
| Evidencia de entrega | Por entrega | 6 años | <2 h |
| Geolocalización personas | Por evento | 12 meses | <1 h |
| Logs auditoría y acceso | Por evento | 5 años | <1 h |

---

## Trazabilidad RT-06 / RT-07

| RT | Carácter | Sección |
|---|---|---|
| RT-06.01 | Oblig. | A.1 |
| RT-06.02 | Oblig. | A.3 |
| RT-06.03 | **Oblig.** | **A.2** |
| RT-06.04 | Oblig. | A.3 |
| RT-06.05 | Oblig. | A.3 / A.11 |
| RT-06.06 | Oblig. | A.3 |
| RT-06.07–08 | Oblig. | A.4 |
| RT-06.09–11 | Oblig. | A.4 |
| RT-06.12 | Deseable | A.4 |
| RT-06.13–14 | Oblig. | A.5 |
| RT-06.15 | Deseable | A.5 |
| RT-06.16–19 | Oblig. | A.6 |
| RT-06.20–25 | Oblig. | A.7 |
| RT-06.26–28 | Oblig. | A.8 |
| RT-06.29–31 | Oblig. | A.9 |
| RT-06.32–33 | Oblig. | A.10 |
| RT-06.34 | Deseable | A.10 |
| RT-07.01–07 | Oblig. | B.1–B.5 |
| RT-07.08 | Deseable | B.5 |
| RT-07.09–13 | Oblig. | B.7 |
| RT-07.14 | Deseable | B.7 |

---
*Fuente: BTT §6-7 · Caso_02 §15 · Diagramas en Diagramas/RT-06_DataCenter/*
*Este Markdown es fuente de verdad del §4.2.d-e. El LaTeX rquitectura_fisica.tex lo referencia, no lo reemplaza.*
