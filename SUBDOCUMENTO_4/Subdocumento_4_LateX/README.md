# Subdocumento 4.2 en LaTeX — Arquitectura física y de despliegue

**Licitación TFEP-01/2026 · Caso 02 — Logística (Distribuidora Puelche S.A.) · LafroX**

Proyecto LaTeX del Subdocumento 4.2, armado sobre la clase `lafrox` con la estructura de carpetas que la propia clase define: un subdocumento por carpeta, autocontenido, llamado desde `main.tex` con una línea.

---

## Compilar

```bash
latexmk main.tex
```

`latexmkrc` fuerza **LuaLaTeX** (`$pdf_mode = 4`), que es lo que la clase necesita para la portada. Para limpiar los auxiliares:

```bash
latexmk -c
```

> **No compilado aquí.** Este proyecto se generó en una máquina sin distribución de TeX, de modo que el fuente está verificado pero el PDF no se ha producido todavía. La primera compilación puede arrojar avisos de caja (`Overfull \hbox`) en las tablas más anchas: son de ajuste fino, no de estructura. La sección «Qué revisar en la primera compilación» lista qué mirar.

---

## Estructura

```
Subdocumento_4_LateX/
├── main.tex                     metadatos de la oferta y orden de los subdocumentos
├── lafrox.cls                   clase institucional (sin modificar)
├── lafrox-portada.tex           carátula (la carga la clase automáticamente)
├── latexmkrc                    LuaLaTeX + biber
└── 04_arquitectura_fisica/      el subdocumento, autocontenido
    ├── contenido.tex            el \chapter y las llamadas \parte{}
    ├── figuras/                 5 imágenes
    └── partes/                  16 fragmentos, uno por apartado
```

Nada dentro de `04_arquitectura_fisica/` conoce dónde está montado: no hay rutas con `../` ni desde la raíz del repositorio. Para reubicar el capítulo basta mover la carpeta y cambiar la ruta en `main.tex`.

### Los dieciséis fragmentos

| Archivo | Apartado | Tablas |
|---|---|---|
| `00_como_leer.tex` | Cómo leer esta parte | 1 |
| `01_vision_general.tex` | Visión general de la arquitectura física | — |
| `02_a_emplazamiento.tex` | (a) Modelo de emplazamiento híbrido | 1 |
| `03_b_tecnologias.tex` | (b) Tecnologías de software ofertadas | 1 |
| `04_c_implementos.tex` | (c) Implementos a proveer | 4 |
| `05_d_sitio_principal.tex` | (d) Sitio principal on-premise (CD Talca) | 1 |
| `06_e_sitio_secundario.tex` | (e) Sitio secundario y recuperación ante desastres | 1 |
| `07_f_niveles_servicio.tex` | (f) Niveles de servicio de infraestructura | — |
| `08_g_operacion_desconectada.tex` | (g) Operación desconectada | 1 |
| `09_h_integracion.tex` | (h) Arquitectura de integración | 9 |
| `10_i_seguridad.tex` | (i) Arquitectura de seguridad | 14 |
| `11_j_despliegue.tex` | (j) Arquitectura de despliegue | 8 |
| `12_k_dimensionamiento.tex` | (k) Dimensionamiento y plan de capacidad | 16 |
| `13_l_capa_analitica.tex` | (l) Capa analítica | 15 |
| `14_m_decisiones_adr.tex` | (m) Registro de decisiones de arquitectura | 32 |
| `15_n_trazabilidad.tex` | (n) Trazabilidad normativa consolidada | 8 |

**112 tablas** en total, todas compuestas en el documento.

---

## Qué cambió respecto del Markdown

El origen es `04_arquitectura/entrega_2/texto/arquitectura_fisica.md` del repositorio, con tres diferencias deliberadas.

**Las tablas están dentro del documento.** En el Markdown, las 115 tablas eran punteros del tipo «*ver planilla del subdocumento*» y el contenido vivía en siete archivos `.xlsx`. Un documento con 115 remisiones a una planilla no se puede leer, y en un sobre de licitación tampoco se puede evaluar. Aquí cada tabla se compone con el entorno `tablalafrox` de la clase, que rompe de página sola, repite la cabecera y rotula la continuación. Las planillas siguen siendo la fuente de los datos y el lugar donde editarlos.

**Seis tablas de dos columnas se convirtieron en viñetas.** Para mejorar la lectura se transformaron seis tablas etiqueta→definición en listas: Contratos (t33) y Versionado (t37) en (h), y Autorización (t47), Gestión de dispositivos (t49), En tránsito (t50) y Cifrado a nivel de campo (t52) en (i). En el Markdown se conservan los punteros `> **Tabla N** — …` hacia la planilla y el contenido se repite como viñetas; en LaTeX, `itemize`. Las matrices con datos (multi-columna) se mantienen como tablas.

**Los planos del recinto están incorporados.** RT-06.03 exige el plano de distribución interna con separación de zonas y RT-06.05 la elevación de gabinetes. Estaban elaborados en `Diagramas/RT-06_DataCenter/` del repositorio pero nunca entraron al entregable. Se incorporan cuatro: distribución interna, cadena eléctrica, elevación de gabinetes y gabinete de borde.

**La numeración automática está apagada bajo el nivel de capítulo.** Esta parte trae su propia rotulación —apartados (a) a (n), subsecciones numeradas a mano— y el texto se refiere a ella en decenas de lugares («el apartado (j)», «§4.4 de este apartado»). Si se dejara activa la numeración de LaTeX, el lector vería dos numeraciones superpuestas y las referencias internas dejarían de coincidir con lo impreso. El índice sigue recogiendo los tres niveles. La decisión está comentada en `contenido.tex`.

---

## Correcciones aplicadas durante la conversión

Al componer las planillas afloraron defectos que en el Markdown quedaban invisibles, porque el dato estaba dentro del `.xlsx` y no en el texto. Se corrigieron en el LaTeX; **las planillas del repositorio siguen teniendo el error y hay que arreglarlas ahí también**:

| Dónde | Qué decía la planilla | Qué dice ahora |
|---|---|---|
| Tabla 101, apartado (l) | «Art. 5° Capacidad Analítica», «Cap. 5° Innovación — 1 innovación obligatoria (análisis predictivo)», «Art. 39° Acceso a datos» | Tabla reescrita contra los artículos correctos (Art. 23° y 25°). Los tres artículos citados regulaban otra materia: el 5° es el orden de precedencia de los documentos y el 39° la documentación administrativa |
| Tabla 101, apartado (l) | Prometía «análisis predictivo de demanda (Redshift ML o SageMaker)» | Contradecía la Decisión N° 52, que declina analítica predictiva de forma fundada. Ahora la renuncia se declara como tal, conforme a RT-18.01 |
| Tabla 101, apartado (l) | Citaba RF-17.12 y RF-16.02 | Ninguno de los dos existe en el catálogo del subdocumento 3 |
| Tabla 21, apartado (a) | «CD Talca (Sala Técnica Secundaria)» | «sala técnica principal»: Talca aloja el núcleo, así que le corresponde esa tipología del numeral 6.1 |
| Tabla 62, apartado (j) | «TIER II objetivo (99,741 %)» | «disponibilidad de infraestructura de 99,95 % por componente»: el numeral 6.1 exige ese valor y el texto ya lo compromete |
| 7 celdas en 6 apartados | «3-2-1-1-0» | «3-2-1-0», que es como RT-07.09 nombra el esquema |

---

## Qué revisar en la primera compilación

1. **Cajas desbordadas en tablas.** Los anchos de columna se calcularon por el largo del contenido, pero sin componer no hay certeza. Si alguna tabla desborda, el ajuste es la tercera línea de su entorno: la especificación de columnas. `F{0.24}` es una columna fija del 24 % del bloque de texto, `G{}` la misma centrada y `Y` la columna elástica que cuadra la tabla. **Toda tabla necesita al menos una `Y`.**
2. **Las cinco figuras.** Están a `0.86`–`0.94` del ancho de texto. Los planos del recinto son densos: si alguno queda ilegible, conviene subirlo a `1.0` o pasarlo a `anexohorizontal`, que la clase provee para eso.
3. **La carátula.** `main.tex` trae los metadatos del subdocumento, pero la razón social, el RUT y el domicilio del proponente siguen siendo los valores por defecto de la clase. Hay que confirmarlos antes de entregar (Art. 39° y 43.3).
4. **Las notas de trabajo.** `contenido.tex` abre con una `\nota{}` y la clase las apaga todas con la opción `final` de `\documentclass`. Para la versión a entregar: `\documentclass[carta,firma,final]{lafrox}`, que además quita la marca de agua de borrador.

---

## Lo que sigue pendiente de contenido

Del análisis del subdocumento (`04_arquitectura/ANALISIS_arquitectura_fisica_4-2.md` en el repositorio):

- **La tabla de emplazamiento de 36 componentes.** El apartado (a) la cita —11 on-premise puros, 12 híbridos, 13 servicios de nube— y entrega una de seis filas. El documento completo existe en `Arquitectura/fisica/Tabla_Emplazamiento_OnPremise_v06.md`. El Art. 16.2 califica de observación grave la asignación sin justificar por componente, así que es la incorporación más urgente.
- **Nueve requisitos obligatorios** de este subdocumento sin respuesta: RT-07.13, RT-06.02, RT-06.06, RT-06.19, RT-06.31, RT-08.06, RT-08.07, RT-08.09 y RT-08.16.
- **Veintiséis requisitos** resueltos en el texto pero sin el código citado. Como el Formulario T-12 se responde código por código, un requisito bien resuelto y mal citado puntúa igual que uno ausente.
