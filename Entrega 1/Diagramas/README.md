# Diagramas — Entrega 1

**Licitación TFEP-01/2026 · Caso 02 — Logística · LafroX**


> **Registro congelado.** Estas son **todas** las imágenes que contiene
> `productos/Informe 1 Entrega 1.docx`, el documento efectivamente entregado el 07-09-2026.


## Inventario (15 imágenes)

| Archivo | Contenido | Subdoc. |
|---|---|---|
| `ARQF-01_Modelo_emplazamiento_hibrido.png` | Modelo de emplazamiento híbrido (nube + on-premise) | 4.2 |
| `ARQL-01_Vision_general.png` | Diagrama general de la arquitectura lógica (8 capas) | 4.1 |
| `ARQL-02_Preventista.png` | Recorrido del preventista | 4.1 |
| `ARQL-03_Conductor_propio.png` | Recorrido del conductor propio | 4.1 |
| `ARQL-04_Conductor_externo.png` | Recorrido del conductor externo | 4.1 |
| `ARQL-05_Cliente_canal_tradicional.png` | Recorrido del cliente del canal tradicional | 4.1 |
| `ARQL-06_Cliente_canal_moderno.png` | Recorrido del cliente del canal moderno (EDI) | 4.1 |
| `ARQL-07_Transportista.png` | Recorrido del transportista | 4.1 |
| `ARQL-08_Proveedor.png` | Recorrido del proveedor | 4.1 |
| `ARQL-09_Preparador.png` | Recorrido del preparador de pedidos | 4.1 |
| `ARQL-10_Jefa_de_calidad.png` | Recorrido de la jefatura de calidad | 4.1 |
| `ARQL-11_Gerente_comercial.png` | Recorrido de la gerencia comercial | 4.1 |
| `ARQL-12_Gerente_finanzas.png` | Recorrido de la gerencia de finanzas | 4.1 |
| `ARQL-13_Planificador_de_rutas.png` | Recorrido del planificador de rutas | 4.1 |
| `ARQL-14_Gerente_TI.png` | Recorrido de la gerencia de TI | 4.1 |

## Qué **no** contiene el Informe 1 entregado

Verificado por hash: **ninguna** de las 29 piezas de `Diagramas/` en la raíz del repositorio
aparece dentro del `.docx`. Es decir, quedaron **fuera del entregable**:

| Material | Estado |
|---|---|
| `Diagramas/RT-06_DataCenter/` — 12 planos del data center | material de trabajo, no llegó al Informe 1 |
| `Diagramas/DC06_Plano_DataCenter_Primario_Blueprint.png` | material de trabajo, no llegó al Informe 1 |
| `Diagramas/arq_*.png` — 14 diagramas de arquitectura | material de trabajo, no llegó al Informe 1 |

Es un hallazgo relevante para la Entrega 2: los subdocumentos 4.2 (d) y (e) —
**Especificaciones Data Center primario y secundario, 12 % de la ponderación del Informe 2** —
se sustentaron sin incorporar ninguno de los planos ya elaborados.


## Sobre el proyecto LaTeX (retirado)

`productos/Informe1/informe latex/` **no reflejaba este entregable** y fue **retirado del
repositorio por obsoleto**: sus macros `\diagrama{}` invocaban 8 archivos, de los cuales 5 no
existen (`as_is_preventa_reparto.png`, `as_is_preparacion_despacho.png`,
`arq_fisica_emplazamiento.png`, `modelo_datos_er.png`, `DC06_Plano_DataCenter_Primario_Blueprint.svg`)
y se renderizaban como `[PENDIENTE]`.

La **fuente de verdad de lo entregado es el `.docx`**, no el LaTeX. Queda en el historial de git
(commit `6a4a00d` y tag `respaldo/pre-consolidacion-2026-09-08/datacenter`) por si hiciera falta.
