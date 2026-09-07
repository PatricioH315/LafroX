---
name: datacenter-diagrams
description: Diagramas de datacenter para la propuesta Puelche (TFEP-01/2026) usando las librerias nativas de draw.io (mxgraph.rackGeneral.rackCabinet3, plate, horCableDuct, shelf, neatPatch) y cabinets. Use al elaborar, renderizar o auditar cualquier plano de sala tecnica, elevacion de rack, gabinete de borde o topologia fisica del DC (on-premise Talca + borde Concepción/cross-docks). Triggers: "elevacion de rack", "diagrama de rack", "plano de sala", "gabinete de borde", "data center", "RT-06.05", "RT-06.01".
---

# datacenter-diagrams — Diagramas de datacenter (elevación de rack y plano de sala)

Especializado en los artefactos físicos del DC que exigen RT-06.03 (plano de
distribución interna), RT-06.05 (racks independientes + ocupación proyectada por
rack) y §6.1 (gabinete o borde operacional con 4 requisitos). Se apoya en la
app **draw.io desktop** (ya instalada, v31+) para rendizado local a PNG/PDF, con
la fuente `.drawio` versionable en `Diagramas/`.

## Herramienta y librerías (regla de AGENTS.md)

| Artefacto | Librería draw.io | Shapes clave |
|---|---|---|
| Elevación de rack (vista frontal, U numeradas) | **Rack** (`More Shapes → Networking → Rack`) | `mxgraph.rackGeneral.rackCabinet3` (gabinete 42U con numeración automática), `rackCabinet2`, `rackNumbering`, `plate`, `horCableDuct1U/2U`, `horRoutingBank1U/2U`, `neatPatch2U`, `shelf1U/2U/4U`, `channelBase`, `cabinetLeg` |
| Gabinete eléctrico / borde | **Cabinets** (`Other → Cabinets`) | `mxgraph.cabinets.cabinet` (con `hasStand`), `coverPlate`, `dimension`, `dimensionBottom` |
| Plano de sala / zonificación | General (rectángulos) + leyenda de zonas | Coordenadas con escala indicativa, cotas en m², 7 zonas de RT-06.03 |

### Geometría del gabinete `rackCabinet3` (regla crítica)

Es el shape oficial con **numeración de U automática**. Al usarlo:

- El número de U se deriva de la altura: `unitNum = round((height − 42) / rackUnitSize)`.
- Ajustes recomendados: `rackUnitSize=10`, `textSize=8`, `numDisp=descend`,
  `startUnit=1`, `rackUnitDirLeft=1`. Con `rackUnitSize=10`, un rack 42U mide
  **height = 42·10 + 42 = 462 px** y el número **1 queda abajo** (U1), **42 arriba**.
- El eje interior disponible tras la columna de números es
  `x = cabinetX + 24 + 9`, `width = cabinetW − 24 − 18`.
- Posición de la U *N* (N = 1..42) dentro del gabinete en `cabinetY`:
  - Fila ocupa `y = cabinetY + (height − 21 − unitH·N)`, alto `= unidad_U · unitH`.
- PDU vertical **A y B en lados opuestos** (RT-08.04 / caminos eléctricos distintos):
  rotular como franjas laterales (`plate` estrechas) o anotación fuera de la geometría.

## Vistas por entregable

| Vista | Contenido mínimo | RT que responde |
|---|---|---|
| **Plano de distribución interna** | 14 recintos reales (Sala v02 §2), 3 líneas de acceso, esclusa antipassback, 7 zonas coloreadas (generadores, baterías, climatización, servidores, comunicaciones, trabajo, respaldo), leyenda, escala indicativa | RT-06.03 |
| **Elevación de rack** | Gabinete 42U numerado; por equipo: nombre real (T-11), U ocupadas, margen por rack; PDU A/B laterales; paneles/organizadores | RT-06.05 |
| **Bandas de ocupación** (racks sin elevación U-por-U) | Rango de U ocupadas, reserva 20–30 %, gabinete de crecimiento al 100 % libre | RT-06.05 |
| **Gabinete de borde** (Concepción / cross-docks) | 4 requisitos §6.1: protección eléctrica, control de acceso físico, monitoreo remoto, condiciones ambientales + equipo real (T-11 C3/C5/C6/C13/C14, mini-PC, D-06 Starlink) | §6.1 · RT-06.01 · T-21 4.2.e |
| Topología física / red | (opcional, usar `mermaid-diagrams`/`plantuml-diagrams`) | — |

## Fuente de datos (no inventar cifras)

- Recintos, plano, energía, clima, racks: `Sala_Servidores_OnPremise_v02.md` (§2, §3.2, §5, §6.2/6.3).
- Equipos e inventario: `T-11_Especificaciones_Tecnicas_Ofertadas.md` (C1–C8 racks Talca; C3 borde Concepción; C13/C14; A5 SD-WAN; D-06 Starlink; B-02 Gateway IoT).
- Volumetría/supuestos: `Dimensionamiento_Infraestructura_OnPremise_v05.md`, `Dimensionamiento_y_Plan_de_Capacidad_v01.md`, `Tabla_Emplazamiento_OnPremise_v06.md`.
- R01 (elevación obligatoria, profe §6): Sala v02 §6.3 — patch fibra OM4/cobre Cat6A, NODO-1/2/3 (1U), Gateway IoT, NAS D-05 (2U), consola KVM, reserva 20 %.

## Renderizado

```powershell
$exe = "C:\Users\henri\AppData\Local\Programs\draw.io\draw.io.exe"
& $exe --export --format png --scale 2 --border 12 --output "Diagramas\out.png" --page-index 1 "fuente.drawio"
```

- Páginas numeradas desde **1** (en v27+). `--page-index 1` = primera página.
- **Quirk Windows:** si hay una instancia de draw.io abierta, el CLI no exporta y no devuelve salida.
  Cerrarla antes: `Get-Process -Name draw.io -ErrorAction SilentlyContinue | Stop-Process -Force`.
- Guardar PNG/SVG/PDF de salida en `Diagramas/` (protocolo AGENTS.md).
- Validar XML antes de entregar (se permite script de verificación local: `[xml]$x = Get-Content -Raw ...`).

## Entregables actuales (2026-09-06)

- `Diagramas/DB_Diagrama_Datacenter_RT0603.drawio` — **5 páginas** en un solo archivo: P1 plano RT-06.03
  (14 recintos, 3 líneas, esclusa, rampa, ventana NOC, 7 zonas + leyenda + escala), P2 cadena eléctrica de
  7 eslabones, P3 elevaciones R01–R04 (orden canónico del profesor), P4 gabinete de borde + 4 requisitos §6.1,
  P5 ficha técnica. PNGs exportados `DB_Diagrama_Datacenter_RT0603_p1..p5.png`.
- R01 v05 (Sala v02 §6.3): patch U42–U40, reserva U39–U31, NODO-1/2/3 U29–27, Gateway U25, NAS U24–23, KVM
  U22, reserva U21–U1; PDU A/B en lados opuestos. Elevación previa parcial: `DB_Elevacion_Racks_RT0605.drawio`.

## Auditoría

Al auditar un diagrama de DC entrante, verificar contra AGENTS.md (fuente de
verdad tecnológica):

1. **Híbrido**: site primario on-premise Talca + site secundario (AWS sa-east-1
   primaria / us-east-1 DR) + gabinete de borde.
2. **RT-06.05**: racks de servidores **independientes** de los de comunicación (R01 vs R02).
3. **§6.1 gabinete de borde**: los 4 requisitos explicitados (no solo el servidor).
4. **Ocupación proyectada** de cada rack con margen (RT-06.05).
5. Plano con **cotas/escala** y las 7 zonas separadas (RT-06.03).
6. Registrar veredicto/hallazgos en `AUDITORIA.md`.