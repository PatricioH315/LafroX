# Plantilla LaTeX LafroX

Clase corporativa para los documentos de oferta de la **Licitación N.° TFEP-01/2026**
(Caso 02 — Logística, Distribuidora Puelche S.A.).

Tema **minimalista**: tipografía Inter en todo el documento, sin filetes decorativos,
sin rellenos de color en las tablas y sin filas cebra. La jerarquía se construye con
tamaño, peso y espacio en blanco. La **portada** es la única pieza expresiva y queda
fuera del tema a propósito.

| Archivo | Qué es |
|---|---|
| `lafrox.cls` | La clase. Todo el diseño vive aquí. No se edita para redactar. |
| `lafrox-portada.tex` | La portada, aislada e intercambiable. La carga la clase. |
| `demo.tex` → `demo.pdf` | Muestrario de componentes. No es un entregable. |
| `latexmkrc` | Fija LuaLaTeX y la limpieza. |
| `assets/logo/` | Vacío. Ahí va el logo cuando exista. |

## Compilar

```bash
latexmk demo.tex
```

Requiere **LuaLaTeX** (la clase aborta con cualquier otro motor: usa `fontspec`) y dos
pasadas, que `latexmk` resuelve solo. Para limpiar: `latexmk -c`.

## Tipografía

| Uso | Familia |
|---|---|
| Todo el documento | **Inter** |
| `\texttt` — rutas, opciones, códigos | **IBM Plex Mono** |

Inter es el sustituto abierto (SIL OFL) de la familia **SF de Apple**: mismo esqueleto
geométrico-humanista y altura de x alta. Las SF de Apple no son redistribuibles para
composición de documentos, así que no se usan. IBM Plex Mono cumple el papel de SF
Mono y comparte el esqueleto de Inter, de modo que no desentona como sí desentonaba el
mono de Latin Modern que trae LaTeX por defecto.

Ambas vienen de los paquetes de TeX, no del sistema; MiKTeX las instala en la primera
compilación. El cuerpo va en **11 pt**, que es el mínimo del Art. 40.4: no bajarlo.

## Empezar un documento nuevo

```latex
\documentclass[carta,firma,borrador]{lafrox}

\datoslafrox{
  subtitulo  = {Informe 2},
  alcance    = {Subdocumentos 1--9 y 13},
  formulario = {Formulario T-22},
  fecha      = {05 de octubre de 2026},
  version    = {1.0},
}

\begin{document}
\portadalafrox
\indicelafrox
\chapter{Presentación de la empresa}
...
\end{document}
```

Los metadatos que no se declaran toman el valor por defecto del proyecto, definido en
`lafrox.cls` (sección 6). **Todo valor que contenga una coma debe ir entre llaves**, o
`pgfkeys` lo lee como separador de claves.

### Opciones de clase

| Opción | Efecto |
|---|---|
| `carta` / `oficio` | Tamaño de página (Art. 40.4). `carta` es el valor por defecto. |
| `firma` / `sinfirma` | Zona de media firma en el pie de cada página (Art. 40.2). |
| `borrador` | Marca de agua diagonal `BORRADOR`, al fondo y muy tenue. |
| `final` | Sin marca de agua y **sin notas de orientación**. Es la de entrega. |
| `sinnotas` | Apaga sólo las notas, conservando la marca de agua. |
| `apa` | Carga `biblatex-apa` + `biber` para las citas del Art. 40.4. |

## Cumplimiento formal ya resuelto (Art. 40)

| Art. | Exigencia | Dónde |
|---|---|---|
| 40.1 | Foliación correlativa, sin saltos, inferior derecha | `fancyhdr` en los tres estilos de página, portada incluida, numeración árabe desde el folio 1 |
| 40.2 | Media firma en el extremo inferior derecho de cada página | opción `firma` |
| 40.3 | Hoja resumen con folio inicial por sección | entorno `hojaresumen`, folios vía `\pageref` |
| 40.4 | Carta u oficio, vertical | opciones `carta` / `oficio` |
| 40.4 | Cuerpo no inferior a 11 pt; tablas y figuras, a 9 pt | base `11pt`; tablas a 9,5 pt |
| 40.4 | Índice detallado con folios | `\indicelafrox` |
| 40.4 | Referencias APA 7.ª ed. | opción `apa` |
| 40.4 | Anexos gráficos horizontales | entorno `anexohorizontal` |

> La plantilla retirada (`Productos/plantilla informe/`) usaba `a4paper`, que el
> Art. 40.4 no admite. Esta parte en carta.

## Alcance deliberado

La plantilla estiliza **tipografía, jerarquía, numeración, tabulaciones y tablas**.
Nada más.

La v1.0 traía además una batería de cajas de color, etiquetas de trazabilidad en línea,
fichas de indicadores (`\rt`, `\hito`, `requisito`, `riesgo`, `cifras`…), tres colores
semánticos de severidad y un marcador `\pendiente` con caja. Todo eso se retiró: es
lenguaje de folleto, no de informe de licitación. Si algún elemento hace falta más
adelante, está en el historial de git.

La paleta termina en violeta oscuro, azul, oro, gris y un fondo. El **oro sólo aparece
en la portada**; no hay ni un elemento dorado en las páginas de contenido. Tampoco hay
colores semánticos de severidad o estado: en un informe de licitación esas distinciones
van en palabras y en columnas de tabla, no en color.

## Componentes

### Jerarquía y tabulaciones

Cinco niveles de título: `\chapter`, `\section`, `\subsection`, `\subsubsection`
(numerados hasta el tercero) y `\paragraph`, que corre dentro del párrafo. El número de
capítulo va como rótulo pequeño en mayúsculas con interletraje abierto sobre el título;
no hay filetes en ningún titular. El índice llega al segundo nivel y no lleva guías de
puntos: la alineación del folio a la derecha basta.

Las listas tienen tres niveles con marca y sangría propias, sin configurar nada:
`itemize` usa viñeta, raya y punto; `enumerate` usa `1.`, `a)` y `i.`; y `description`
pone el término en semibold. Los numerales romanos salen en versalitas, que es la
convención española que aplica `babel`.

### Tablas

Una sola: `tablalafrox`, con cuatro argumentos y cuerpo.

```latex
\begin{tablalafrox}{Reparto de alcance}{tab:etapas}%
  {L{2.1cm} Y C{2.4cm}}%
  {\cab{Etapa} & \cab{Alcance} & \cab{Producción}}
  Etapa 1 & Preventa, reparto y trazabilidad sanitaria & Mes 16 \\
\end{tablalafrox}
```

Tres filetes horizontales y espacio: sin relleno de cabecera, sin filas cebra y sin
líneas verticales. Rompe de página sola, repite la cabecera y rotula la continuación.
Las cifras salen de ancho fijo para que las columnas de códigos y de cantidades se
alineen verticalmente.

**La especificación de columnas debe incluir al menos una columna `Y`**: es la elástica,
la que absorbe el ancho restante para que la tabla cierre exactamente en el margen.

| Tipo de columna | Qué hace |
|---|---|
| `Y` | Elástica, alineada a la izquierda. Obligatoria, al menos una. |
| `L{2cm}` `C{2cm}` `R{2cm}` | Ancho fijo: izquierda, centrado, derecha. |
| `F{0.25}` `G{0.25}` `H{0.25}` | Igual, pero en fracción del bloque de texto. |
| `\cab{...}` | Tipografía de celda de cabecera. |

Para las tablas grandes de la Entrega 2, que viven como planillas, va la referencia y
no la tabla volcada a mano. Varias seguidas forman una lista separada por filetes:

```latex
\tablaref{7}{Volumetría de despacho}%
  {Entrega 2/05\_arquitectura\_fisica/tablas/Dimensionamiento.xlsx!Despacho}
```

### Citas y notas de trabajo

```latex
\begin{cita}{Caso 02 --- Logística, Cap. 15}
  Pasaje textual del caso, de las Bases o de una entrevista.
\end{cita}

\nota{Orientación o pendiente. Desaparece con la opción [final] o [sinnotas].}
```

`\nota` es el único andamiaje de redacción de la plantilla, y también donde van los
pendientes. Un solo interruptor apaga todo antes de entregar, así que no hay que cazar
marcas una por una.

### Páginas de control

```latex
\begin{controlversiones}
  \versionfila{1.0}{05-10-2026}{Alex Aravena}{Versión presentada}
\end{controlversiones}

\begin{hojaresumen}
  \resumenfila{Arquitectura lógica}{cap:arqlog}
\end{hojaresumen}
```

`\resumenfila` recibe una **etiqueta**, no un número: el folio se resuelve con
`\pageref` y no hay que mantenerlo a mano.

### Marca

Sin archivo de logo, la clase dibuja un monograma tipográfico (`\lafroxmonograma`,
`\lafroxmarca`). Para usar un logo real, poner el archivo en `assets/logo/` y
declararlo: `\datoslafrox{logo = {assets/logo/lafrox.pdf}}`.

## Retícula y márgenes

Todo cae sobre los mismos dos márgenes verticales: bloque de texto, filete del
encabezado, ambos bloques del pie y —desde la v2.1— también el título, la retícula de
datos y el pie académico de la **portada**. Sólo la banda diagonal se sale, porque es
arte a sangre y va de borde a borde a propósito.

La portada no lleva esas fracciones escritas a mano: las calcula de `\geometry` con
`\LFXcalcularmargenes`, así que si mañana se cambian los márgenes, la portada los sigue.

| Medida | Valor | Por qué |
|---|---|---|
| Márgenes | 3,1 cm izq. · 2,7 cm der. · 2,9 cm sup. · 3,0 cm inf. | Medida de línea corta; en un tema minimalista el aire es el recurso |
| `headheight` | 27 pt | Tiene que caber el texto del encabezado **más** el filete y su separación |
| `headsep` | 16 pt | Separación visible entre el filete y la primera línea |
| `footskip` | 52 pt | Tiene que caber las tres filas del pie derecho: filete de firma, rótulo y folio |

**Si cambias `\LFXchico`, `\headrule` o el pie, revisa el log**: `fancyhdr` dice el
mínimo exacto que necesita para `headheight` y `footskip`. Con valores por debajo, la
caja del encabezado se desborda hacia el cuerpo y todo el bloque queda corrido —
exactamente el síntoma que hacía ver los encabezados «desalineados».

Para verificarlo a ojo, compila una copia con `\usepackage{showframe}` después de la
clase: dibuja las cajas de encabezado, cuerpo y pie, y cualquier desajuste salta.

## Notas de implementación

Nueve decisiones que no son evidentes y conviene no deshacer:

1. **Las tablas usan `xltabular` con el cuerpo capturado como argumento** (`+b`).
   `tabularx` y sus derivados leen su contenido de una sola vez, así que no sobreviven a
   un `\newenvironment` partido entre código de apertura y de cierre.
2. **Los rótulos de continuación van en `\makebox[0pt]`.** Si midieran su texto real,
   `longtable` ensancharía la primera columna de toda la tabla para caberlos.
3. **El pie de página reinicia el color de fila y `\arraystretch`.** La salida de página
   puede ocurrir mientras una tabla está abierta, y sin eso el pie hereda su fondo y el
   interlineado de 1,42 de las tablas de datos, que no tiene nada que hacer en un pie de
   dos líneas a 7,5 pt.
4. **Los dos bloques del pie llevan `\begin{tabular}[b]`.** Así comparten la línea base
   de su **última** fila y el folio queda a la misma altura que la segunda línea del
   bloque izquierdo. Con la alineación por omisión cada bloque se apoya en su **primera**
   fila, y el de la derecha —que tiene una fila más— cuelga por debajo del otro.
5. **La portada lleva folio, pero no media firma.** El Art. 40.2 pide media firma en
   cada página y firma **completa** en la carátula, y esa la aporta la línea «Firma del
   representante» de la propia portada. Repetir la media firma, además, chocaba con el
   pie académico.
6. **El estilo `plain` anula `\headrule` explícitamente**, no sólo `\headrulewidth`. El
   `\headrule` del estilo `lafrox` dibuja el filete por su cuenta, y las páginas de
   apertura de capítulo quedaban con una línea suelta sobre el título.
7. **No se usa `\needspace` antes de una tabla.** Fuerza un corte y `longtable` abre la
   tabla con un tramo sin filas, dejando el rótulo de continuación huérfano. El paquete
   ya no se carga: no reintroducirlo.
8. **Las columnas de la retícula de portada se miden en `\textwidth`, no en
   `\paperwidth`.** Eran 0,375 del ancho de papel cada una, y sumadas se salían del
   margen derecho.
9. **En la portada, las coordenadas de TikZ se escriben `{(a+b)*\paperwidth}`.** Sin
   paréntesis ni `*`, una expresión como `0.34+0.095\paperwidth` se lee como «0,34 pt
   más 0,095 anchos de papel» y las franjas se desarman. Lo mismo vale para el
   monograma, que usa `<factor><longitud>` y no expresiones pgfmath.

## Relación con el resto del repositorio

- El contenido se toma de `Entrega 2/` (y su línea base, `Entrega 1/`). Esta plantilla
  es **forma**, no fuente de contenido.
- No es el proyecto LaTeX retirado. De aquél sólo se conservó la paleta, y ya
  oscurecida. Ver `AGENTS.md`.
- Los diagramas se toman de `Entrega 2/Diagramas/`, con `\figuralafrox`.
