# Diagramas — Entrega 2

**Licitación TFEP-01/2026 · Caso 02 — Logística · LafroX**


Todos los diagramas de la Entrega 2 viven aquí, **fuera** de las carpetas de subdocumento.
Cada subdocumento los referencia por nombre de archivo.


## Convención de nombres

| Prefijo | Subdocumento | Materia |
|---|---|---|
| `ARQL-` | 4.1 | Arquitectura lógica |
| `ARQF-` | 4.2 | Arquitectura física y de despliegue |
| `DC-`   | 4.2 (d)(e) | Data center primario y secundario |

## Rescatados del `.docx` de la Entrega 1

Estas 15 imágenes existían **únicamente embebidas** en `productos/Informe 1 Entrega 1.docx`.
No estaban en el repositorio: se extrajeron para que sean editables y versionables por separado.

| Archivo | Contenido |
|---|---|
| `ARQF-01_Modelo_emplazamiento_hibrido.png` | Modelo de emplazamiento híbrido (nube + on-premise) |
| `ARQL-01_Vision_general.png` | Diagrama general de la arquitectura lógica (8 capas) |
| `ARQL-02_Preventista.png` | Recorrido del preventista por la arquitectura lógica |
| `ARQL-03_Conductor_propio.png` | Recorrido del conductor propio |
| `ARQL-04_Conductor_externo.png` | Recorrido del conductor externo |
| `ARQL-05_Cliente_canal_tradicional.png` | Recorrido del cliente del canal tradicional |
| `ARQL-06_Cliente_canal_moderno.png` | Recorrido del cliente del canal moderno (EDI) |
| `ARQL-07_Transportista.png` | Recorrido del transportista |
| `ARQL-08_Proveedor.png` | Recorrido del proveedor |
| `ARQL-09_Preparador.png` | Recorrido del preparador de pedidos |
| `ARQL-10_Jefa_de_calidad.png` | Recorrido de la jefatura de calidad |
| `ARQL-11_Gerente_comercial.png` | Recorrido de la gerencia comercial |
| `ARQL-12_Gerente_finanzas.png` | Recorrido de la gerencia de finanzas |
| `ARQL-13_Planificador_de_rutas.png` | Recorrido del planificador de rutas |
| `ARQL-14_Gerente_TI.png` | Recorrido de la gerencia de TI |

## Diagramas ya versionados en el repositorio

No se copian aquí para no duplicar binarios. Se referencian desde `Diagramas/` en la raíz:

| Ruta | Contenido |
|---|---|
| `Diagramas/RT-06_DataCenter/` | 12 planos del data center (distribución, sala técnica, cadena eléctrica, elevación de racks, gabinetes de borde, ficha técnica) con su propio `README.md` |
| `Diagramas/DC06_Plano_DataCenter_Primario_Blueprint.png` | Blueprint del data center primario |
| `Diagramas/arq_*.png` | 14 diagramas de arquitectura (contexto, capas, integración, seguridad, datos híbrida, dominio/ER, secuencias de preventa, reparto, cadena de frío, EDI y telemetría) |
| `Diagramas/arq_mapa_hibrido.html` | Mapa híbrido interactivo |

## Fuente de los diagramas

Según `AGENTS.md`: la fuente textual vive en los `.md` (Mermaid) o en `.drawio`; los `.png`/`.svg`
exportados son derivados. Al reemplazar un diagrama, actualizar primero la fuente.
