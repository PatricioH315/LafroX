# Formulario T-11 — Fila Data Center Primaria y Data Center Secundario (borrador alineado a v5-431 y v6-432)

> **Alcance:** solo las filas de los ítems d) y e) del Subdocumento 4.2. El resto del formulario (cómputo, red, dispositivos de terreno, nube, software) ya vive en `partes/15_anexo_t11.tex` y no se repite aquí.
> Columnas oficiales: Componente | Producto / servicio ofertado | Ubicación / Lugar | Cantidad | Justificación (Formulario T-11 de las Bases Administrativas). Sin precios (Art. 50.2).
> La tabla de sala técnica del anexo actual **debe reemplazarse** por esta (valores alineados al cálculo RT-06.11 de la sección 4.3.1).

---

## Data Center Primaria — infraestructura de la sala técnica secundaria de Talca

| Componente | Producto / servicio ofertado | Ubicación / Lugar | Cantidad | Justificación |
|---|---|---|---|---|
| UPS | Modular de 10 kVA, doble conversión on-line, configuración N+1 y bypass de mantenimiento | Zona de UPS y baterías (plano RT-06.03) | 1 | Dimensionado sobre la carga TI de diseño de 7,0 kW y ≈ 7,4 kVA aparentes (FP 0,95), al 80 % de utilización (resulta ≈ 9,2 kVA → 10 kVA; RT-06.11; Tabla 4.3-1); autonomía ≥ 30 min a plena carga (RT-06.07) |
| Generador | Grupo electrógeno de 15 kVA con estanque para 24 h continuas y contrato de reabastecimiento declarado | Exterior, junto a la acometida (zona de generadores del plano RT-06.03) | 1 | Sostiene la carga total del sitio ≈ 10,4 kW (TI + climatización + apoyo) durante ≥ 24 h (RT-06.08) |
| Transferencia automática | Transferencia red–generador con tablero de protecciones | Acometida, accesible desde el exterior | 1 | Encadena empalme → tablero → transferencia → UPS → PDU → equipo sin interrupción (RT-06.07); se prueba cada mes con carga real y admite termografía (RT-06.10) |
| Climatización | 2 unidades de precisión de 10 kW (≈ 34.000 BTU/h) en configuración N+1 | Zona de climatización, contigua a la sala de servidores y comunicaciones | 2 | Cubren la carga térmica sensible de diseño ≈ 7,6 kW incluso con la pérdida de la unidad mayor, dentro de los rangos del fabricante (RT-06.13; RT-06.11; Tabla 4.3-2) |
| Distribución eléctrica de racks | 2 PDU verticales A/B por gabinete, con medidor | Racks R01 y R02 de la sala | 4 | Dos caminos eléctricos por gabinete (RT-08.04); el medidor es el denominador del PUE (RT-06.10; RT-15.04) |
| Detección de incendio | Detección temprana por aspiración de aire con tecnología láser, tipo AnaLASER o equivalente | Sala de servidores y comunicaciones | 1 | Detecta antes de que exista llama visible (RT-06.16); integrado al monitoreo en línea (RT-06.19) |
| Extinción | Agente limpio tipo FM-200 o equivalente, con aprobación UL, botón de aborto y extintores portátiles habilitados | Sala de servidores y comunicaciones | 1 | Extinción automática sobre equipos energizados conforme a RT-06.17 y extintores con mantención vigente (RT-06.18). No se cita edición específica de norma externa |
| Control de acceso | Biometría facial con AFIS como respaldo, esclusa antipassback con nueva verificación, bitácora electrónica y estación de enrolamiento interna y externa | Acceso del recinto técnico | 1 | RT-06.20 a RT-06.23; bitácora auditable conservada ≥ 5 años (RT-06.21; RT-16.10) |
| Videovigilancia | Cámaras IP con imágenes en línea ≥ 30 días y respaldo recuperable | Recinto y perímetro | Según plano RT-06.03 | Cubre el acceso y el perímetro del recinto, integrada al monitoreo (RT-06.24) |
| Gabinetes | R01 servidores (3 nodos 2U en U18–U23, NAS 2U en U1–U2, KVM 1U en U24, paneles OM4/Cat6A en U40–U42) y R02 comunicaciones (bandeja del operador con ONT de fibra y router LTE, 2U en U31–U32; 2 firewalls 1U en U33–U34; switch de gestión 1U en U35; organizadores 1U en U36 y U39; 2 conmutadores de núcleo 1U en U37–U38; ODF y paneles en U40–U42), 42U | Sala de servidores y comunicaciones | 2 | Racks de servidores independientes de los racks de comunicaciones (RT-06.05); ocupación proyectada R01 y R02 de 12U/42U (29 %) cada uno, con 30U libres por rack para el margen de crecimiento a tres años, coherente con la reserva eléctrica del 20 % de la Tabla 4.3-1 (Figura 4.3-2) |
| Piso técnico y cableado | Cableado Cat6A y fibra OM4 certificados por enlace, sobre piso técnico | Sala | 1 | Cumple la norma por enlace (RT-06.04) con recorridos verificados para 10 GbE |

## Data Center Secundario — gabinete de borde del CD Concepción

| Componente | Producto / servicio ofertado | Ubicación / Lugar | Cantidad | Justificación |
|---|---|---|---|---|
| Gabinete de borde | Gabinete industrializado con alimentación protegida (UPS + respaldo) para la autonomía declarada | CD Concepción | 1 | Sitio de recuperación del dominio on-premise, a ≈ 250–400 km de Talca (RT-07.02); opera de forma autónoma todos los días (RT-06.01 del caso; numeral 6.1 de las Transversales) |
| Climatización del borde | Climatización de precisión acorde al equipamiento del borde | CD Concepción, gabinete de borde | 1 | Dimensionada al equipamiento real del borde conforme a la tipología del numeral 6.1 |
| Control de acceso y monitoreo | Acceso controlado y monitoreo remoto integrado al NOC del sitio | CD Concepción, gabinete de borde | 1 | Aplica la tipología de borde operacional del numeral 6.1 con supervisión remota del sitio |
| Servidor de borde | Dell R250 o HPE DL20 Gen11, 32 GB, RAID 10 sobre las 4 bahías (sin repuesto en caliente) | CD Concepción, gabinete de borde | 1 | Sostiene el WMS con 24 h de operación autónoma; promoción controlada ante contingencia de Talca (RNF-02.01; RT-07.02). Fuente única declarada como punto único de falla aceptado (RT-02.11) |
| Perímetro del borde — firewall | Par activo/pasivo de firewalls de borde de grado empresarial | CD Concepción, gabinete de borde | 2 | Sin punto único de falla (RT-08.03); es el Customer Gateway del túnel hacia AWS y conmuta entre fibra y LTE en menos de 30 s (RT-03.17) |
| Perímetro del borde — switch | Par de switches de núcleo en stack, con doble fuente | CD Concepción, gabinete de borde | 2 | Sin punto único de falla (RT-08.03); sostiene la red de bodega del sitio secundario durante 24 h de autonomía, sin depender del principal |

> Los componentes de la **réplica en nube** (`us-east-1`) ya están declarados en el anexo actual: N-04 (réplica reducida ECS), N-05 (Aurora Global Database), N-06 (Global Tables), N-11 (AWS Backup + S3 Object Lock + replicación de S3) y D-01 (VPC/Route 53) — no requieren cambios.

---

## Qué corregir en `partes/15_anexo_t11.tex` (tabla de sala técnica)

- **D1 UPS:** 6 kVA → **10 kVA modular N+1** (cálculo RT-06.11).
- **D2 Generador:** 12 kVA → **15 kVA** (sostiene ≈ 10,4 kW del sitio, RT-06.08).
- **D4 Climatización:** 12.000 BTU/h → **10 kW (≈ 34.000 BTU/h) por unidad, N+1** (carga térmica ≈ 7,6 kW, RT-06.13). Retirar la cita ASHRAE (norma externa).
- **D7 Extinción:** retirar la edición de NFPA ("NFPA 75 y 2001") → solo RT-06.17.
- **D11 Gabinetes:** 4 racks (R01–R04) → **2 racks: R01 servidores, R02 comunicaciones**, con margen de crecimiento del 20 % dentro de los racks (RT-06.05, Figura 4.3-2).
- **D5 PDU:** 4 gabinetes / 8 PDU → **2 racks / 4 PDU**.
- **C7 Switch de gestión:** la consola KVM se declara en "gabinete R02" → **R01** (la Figura 4.3-2 la ubica en R01, U24). El switch de gestión permanece en R02.
- **C8 Distribución horizontal:** "gabinete R03" → **racks R01 y R02** (los paneles de fibra OM4 y cobre Cat6A están en ambos gabinetes según la Figura 4.3-2; R03 no existe en el diseño vigente).
- Verificar D8/D9/D10 coherentes con el plano RT-06.03 (Figura 4.3-1).