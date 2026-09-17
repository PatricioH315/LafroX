# Plantilla LaTeX LafroX

Clase corporativa para los documentos de oferta de la **Licitación N.° TFEP-01/2026**
(Caso 02 — Logística, Distribuidora Puelche S.A.).

Tema **minimalista y monocromo**: tipografía Inter en todo el documento, sin filetes
decorativos, sin rellenos de color en las tablas y sin filas cebra. La jerarquía se
construye con tamaño, peso y espacio en blanco. La **carátula** es la única pieza
expresiva y queda fuera del tema a propósito.

**No hay color en ninguna parte**: negro, grises neutros y blanco. Ni violeta, ni oro,
ni azul, ni colores semánticos de severidad o estado. El único lugar donde la tinta se
invierte es la banda de cabecera de la carátula, donde el texto va en blanco sobre negro.

| Archivo | Qué es |
|---|---|
| `lafrox.cls` | La clase. Todo el diseño vive aquí. No se edita para redactar. |
| `lafrox-portada.tex` | La carátula, aislada e intercambiable. La carga la clase. |
| `main.tex` | **Esqueleto de armado del informe.** Metadatos y orden de los subdocumentos, sin texto. Es el archivo que se compila. |
| `subdocumento-ejemplo/` | Molde de un subdocumento autocontenido. Borrar al montar el informe real. |
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

## Estructura: un subdocumento, una carpeta

El informe se arma desde `main.tex`, que **no contiene texto**: sólo metadatos y el
orden de los subdocumentos. Cada subdocumento del T-7 vive en su carpeta, autocontenido:

```
main.tex
07_plan_trabajo_edt/
  contenido.tex      ← el \chapter y todo el texto
  figuras/           ← imágenes del capítulo
  tablas/            ← fragmentos .tex, si el capítulo se parte
```

En `main.tex` basta una línea por subdocumento:

```latex
\subdocumento{07_plan_trabajo_edt}
```

Dentro de `contenido.tex`, todo se referencia **relativo a la propia carpeta**:

```latex
\parte{tablas/catalogo_rf}                                   % fragmento
\figuralafrox{0.9}{figuras/edt.png}{Estructura...}{fig:edt}  % figura
```

**Mover un subdocumento es mover la carpeta y cambiar la ruta de su llamada.** Nada
dentro del capítulo sabe dónde está montado. El orden de las llamadas en `main.tex` es
el orden del informe, y la numeración de capítulos, figuras y tablas se recalcula sola.

Dos subdocumentos pueden tener cada uno su `figuras/diagrama.png` sin pisarse:
`\subdocumento` añade la carpeta al `graphicspath` sólo mientras dura la importación.

> **No escribas rutas que suban con `../` ni que arranquen desde la raíz del
> repositorio** dentro de un `contenido.tex`. Es lo único que rompe la promesa de poder
> mover la carpeta.

La clase usa `import` y no `\input` precisamente por esto: con `\input`, un `\input`
anidado dentro del capítulo se resuelve desde la carpeta de `main.tex` y no desde la del
capítulo, de modo que mover la carpeta rompe las rutas internas.

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

### Claves de `\datoslafrox`

| Clave | Qué alimenta |
|---|---|
| `empresa`, `rut`, `domicilio` | Bloque **Proponente** de la carátula y pie de página. El Art. 39 exige domicilio en Valparaíso. |
| `representante`, `cargo`, `correo`, `telefono` | Bloque **Representante legal** y rótulo de media firma. Los cuatro los pide el Art. 49.1. |
| `cliente` | Bloque **Mandante**. |
| `licitacion`, `objeto`, `caso` | Identificación del proceso, lo más prominente de la carátula. |
| `sobre` | El sello oscuro bajo el primer filete: de qué pieza de la oferta se trata. |
| `documento`, `subtitulo`, `alcance`, `formulario` | Título de la carátula, encabezados y `pdftitle`. |
| `version`, `fecha`, `nomenclatura` | Bloque de control documental. `nomenclatura` sigue los Arts. 49 a 51: un archivo mal nominado se considera **no presentado**. |
| `logo` | Vacía por omisión (monograma tipográfico). Ver «Marca». |

> Los valores por defecto de `empresa`, `rut`, `domicilio`, `correo` y `telefono` son
> **provisionales**: no se ha fijado la identidad del PROPONENTE. Confirmarlos antes de
> cualquier entrega — arrastran a carátula, planilla de consultas, sobres y web.

### Opciones de clase

| Opción | Efecto |
|---|---|
| `carta` / `oficio` | Tamaño de página (Art. 40.4). `carta` es el valor por defecto. |
| `firma` / `sinfirma` | Zona de media firma en el pie de cada página (Art. 40.2). |
| `borrador` | Marca de agua diagonal `BORRADOR`, al fondo y muy tenue. |
| `final` | Sin marca de agua y **sin notas de orientación**. Es la de entrega. |
| `sinnotas` | Apaga sólo las notas, conservando la marca de agua. |
| `apa` | Carga `biblatex-apa` + `biber` para las citas del Art. 40.4. |

## Cumplimiento formal ya resuelto (Arts. 40 y 49 a 51)

| Art. | Exigencia | Dónde |
|---|---|---|
| 40.1 | Foliación correlativa, sin saltos, inferior derecha | `fancyhdr` en los cuatro estilos de página, carátula incluida, numeración árabe desde el folio 1. `oneside,openany` evita versos en blanco sin numerar y no hay ningún `\thispagestyle{empty}` |
| 40.1 | Total de folios declarado | Campo «Total de folios» de la carátula, vía `lastpage` |

El pie imprime **el número solo**. El Art. 40.1 exige que la página esté *numerada*, no
que lleve la palabra «Folio». Para el Sobre N.° 1 —físico, con el índice A-5 declarando
folio de inicio y término por documento— el rótulo ayuda a que el número se lea como
folio; se recupera con `\renewcommand{\LFXfolio}{Folio}`.

> **Ojo con el alcance.** La foliación corrida a lo largo de un sobre, el índice A-5 y la
> firma completa en carátula son exigencias de los **sobres** (Arts. 49 a 51), no de los
> informes preparatorios. Un informe del Art. 45 · T-22 sólo necesita portada, índice,
> páginas numeradas y numeración de figuras y tablas. La clase resuelve las dos cosas,
> pero no confundas una entrega con la otra.
| 40.2 | Media firma en el extremo inferior derecho de cada página | opción `firma` |
| 40.2 | Firma **completa** en la carátula | Bloque de firma de `\portadalafrox`, sobre papel blanco y con nombre, cargo y empresa bajo la línea |
| 49.1 | Bloque de identificación que debe leerse en la carátula | Claves `licitacion`, `objeto`, `caso`, `sobre`, `empresa`, `representante`, `correo`, `telefono` |
| 50.3 | Nomenclatura del archivo | Clave `nomenclatura`, al pie de la carátula |
| 40.3 | Hoja resumen con folio inicial por sección | entorno `hojaresumen`, folios vía `\pageref` |
| 40.4 | Carta u oficio, vertical | opciones `carta` / `oficio` |
| 40.4 | Cuerpo no inferior a 11 pt; tablas y figuras, a 9 pt | base `11pt`; tablas a 9,5 pt |
| 40.4 | Índice detallado con folios | `\indicelafrox`, `tocdepth=3` (hasta subsubsection) |
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

La paleta es enteramente acromática. No hay colores semánticos de severidad o estado: en
un informe de licitación esas distinciones van en palabras y en columnas de tabla, no en
color.

| Color | Valor | Uso |
|---|---|---|
| `lafroxFuerte` | `#000000` | Titulares, numeración de secciones, enlaces |
| `lafroxTinta` | `#111111` | Cuerpo de texto |
| `lafroxGris` | `#5F5F5F` | Texto secundario sobre fondo claro |
| `lafroxLinea` | `#C7C7C7` | Filetes de tabla |
| `lafroxTenue` | `#DCDCDC` | Filetes de encabezado y pie |
| `lafroxBg` | `#F4F4F4` | **Reservado, sin uso desde la v2.2**: la carátula es papel blanco |
| `lafroxBanda` | `#141414` | Banda de cabecera de la carátula |
| `lafroxBandaB` · `lafroxBandaC` | `#3C3C3C` · `#606060` | Diagonales de profundidad |
| `lafroxSobre` | `#9A9A9A` | Texto secundario **sobre** la banda |

Los grises son neutros de verdad (R=G=B). El gris anterior tiraba a azul y se leía como
color, no como tinta rebajada.

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

Para las tablas grandes, que viven como planillas dentro de cada subdocumento, va la
referencia y no la tabla volcada a mano. Varias seguidas forman una lista separada por
filetes:

```latex
\tablaref{7}{Volumetría de despacho}%
  {04\_arquitectura/entrega\_2/tablas/arquitectura\_fisica\_Dimensionamiento.xlsx!Despacho}
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

### Carátula

Una banda negra de cabecera con el borde inferior en diagonal —más baja a la derecha—,
acompañada de dos escalones de gris que le dan profundidad. Dentro van la marca en
negativo y el estado del documento. **El resto del papel queda blanco.**

La carátula es un **instrumento de identificación**, no una tapa de marca: su trabajo es
que un evaluador con ocho ofertas sobre el escritorio sepa en dos segundos qué
licitación, qué sobre, qué documento, de quién, de qué fecha y en qué versión. Por eso
la jerarquía tipográfica la encabeza el identificador del proceso, no el rótulo genérico
«Propuesta Técnica». De arriba abajo:

1. Licitación, objeto del proyecto y caso.
2. Sello del sobre y título del documento (de la clave `documento`), subtítulo y alcance.
3. Mandante · Proponente · Representante legal, los tres rotulados.
4. Control documental: versión, fecha de emisión, estado y total de folios.
5. Firma completa del representante, con sus datos bajo la línea.
6. Al pie, nomenclatura del archivo a la izquierda y folio a la derecha.

**No lleva pie académico** —asignatura, unidad, profesor— porque el documento se
presenta como una oferta real, no como un trabajo de asignatura.

Para abrir o cerrar la diagonal, los dos únicos parámetros están al inicio de
`lafrox-portada.tex`:

```latex
\def\LFXbandaIzqY{0.150}   % altura de la banda en el borde izquierdo
\def\LFXbandaDerY{0.088}   % altura de la banda en el borde derecho
```

> **El tercio inferior no admite arte.** Ahí van la firma y el folio: el Art. 40.2 pide
> firma completa en la carátula y el Sobre N.° 1 se entrega físico, foliado y firmado.
> Sobre tinta casi negra no se puede firmar con lápiz, y un folio en blanco sobre gris
> no sobrevive a una fotocopia — y la falta de foliación es causal de **exclusión**
> (Art. 40.1). No subir `\LFXbandaIzqY` por encima de ~0,19: el bloque de
> identificación empieza en 0,228 y se montaría sobre los escalones de gris.

#### Qué cambió en la v2.2

Hasta la v2.1 la carátula era una cuña a sangre que recorría la página completa, con
**todo** el texto en negativo encima. Se cambió por tres motivos, los tres de fondo y no
de gusto: la jerarquía estaba invertida (38 pt para «Propuesta Técnica», 9,5 pt grises
para el número de licitación); no se podía firmar sobre la cuña; y el folio iba en
blanco confiando en que la diagonal exterior alcanzara el margen derecho, cosa que hacía
por 0,02 de ancho de papel. Además faltaban cuatro de los seis elementos que el
Art. 49.1 exige leer en la carátula, y el título estaba cableado a mano: la portada
decía «PROPUESTA TÉCNICA» aunque la clave `documento` dijera otra cosa.

## Retícula y márgenes

Todo cae sobre los mismos dos márgenes verticales: bloque de texto, filete del
encabezado, ambos bloques del pie y también el título y los datos de la **carátula**.
Sólo la banda diagonal se sale, porque es arte a sangre y va de borde a borde a
propósito.

La carátula no lleva esas fracciones escritas a mano: las calcula de `\geometry` con
`\LFXcalcularmargenes`, así que si mañana se cambian los márgenes, la carátula los sigue.

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

Once decisiones que no son evidentes y conviene no deshacer:

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
5. **La carátula lleva folio, pero no media firma.** El Art. 40.2 pide media firma en
   cada página y firma **completa** en la carátula, y esa la aporta el bloque de firma
   de la propia carátula.
6. **El estilo `plain` anula `\headrule` explícitamente**, no sólo `\headrulewidth`. El
   `\headrule` del estilo `lafrox` dibuja el filete por su cuenta, y las páginas de
   apertura de capítulo quedaban con una línea suelta sobre el título.
7. **No se usa `\needspace` antes de una tabla.** Fuerza un corte y `longtable` abre la
   tabla con un tramo sin filas, dejando el rótulo de continuación huérfano. El paquete
   ya no se carga: no reintroducirlo.
8. **El folio de la carátula y el de la contraportada van los dos en tinta.** Desde la
   v2.2 ambas tapas tintan sólo la cabecera y dejan el pie sobre papel blanco, que es la
   única forma de que el folio sobreviva a una fotocopia. `\LFXpiefolioen{color}`
   conserva el parámetro por si una pieza futura necesita el pie en negativo, pero hoy
   nadie lo usa: si vuelves a poner arte en el pie, el folio es lo primero que revisar.
9. **En la carátula, las coordenadas de TikZ se escriben `{(a+b)*\paperwidth}`.** Sin
   paréntesis ni `*`, una expresión como `0.15+0.013\paperwidth` se lee como «0,15 pt
   más 0,013 anchos de papel» y las franjas se desarman. Lo mismo vale para el
   monograma, que usa `<factor><longitud>` y no expresiones pgfmath.
10. **Un `\\` dentro de un nodo TikZ reinicia tamaño de fuente Y color.** Por eso el
    titular de la carátula y el bloque de la contraportada usan **un nodo por línea** en
    vez de uno solo con salto. Con un único nodo, la segunda línea volvía a
    `lafroxTinta` y quedaba negro sobre negro, ilegible. Dentro de una `minipage` el
    salto sí conserva los ajustes, y por eso los bloques de identificación sí los usan.
11. **La marca de agua de `[borrador]` se salta el folio 1.** Mientras la carátula fue
    oscura la diagonal era invisible ahí; ahora cruzaría justo el bloque del Art. 49.1,
    que es el que tiene que leerse sin estorbo. El estado ya se declara dos veces en la
    propia carátula, así que no se pierde el aviso.

## Relación con el resto del repositorio

- El repositorio se organiza por los 14 subdocumentos del Formulario T-7 (`01_.../`
  … `14_.../`), cada uno con `entrega_1/` (congelada) y `entrega_2/` (trabajo). Esta
  plantilla es **forma**, no fuente de contenido: toma el texto de `entrega_2/` de cada
  subdocumento y, cuando no existe aún, de su línea base en `entrega_1/`.
- No es el proyecto LaTeX retirado. De aquél sólo se conservó la paleta, y ya
  oscurecida. Ver `AGENTS.md`.
- Los diagramas se toman de la biblioteca única en `Diagramas/` (raíz del repositorio),
  con `\figuralafrox`.

## Nomenclatura de archivos al entregar (Art. 50.3)

`latexmk` genera `demo.pdf` (o el nombre del `.tex` compilado), pero el Art. 50.3 exige
que el respaldo digital del Sobre N.° 2 se nombre
`SOBRE2_[EMPRESA]_OFERTA_TECNICA_AAAAMMDD.ZIP`. **Renombrar el PDF final antes de
empaquetar**: la clase no puede resolver esto por sí sola. Ver Artículos 49° a 51° para
la nomenclatura de cada sobre.

## Firma completa en documentos principales (Art. 40.2, segunda frase)

El Art. 40.2 exige firma completa en la carátula **y en los documentos principales**,
no sólo media firma por página. La portada (`\portadalafrox`) resuelve la carátula. Para
"documentos principales" —a definir si es cada subdocumento del T-7 o el documento
consolidado— falta un bloque de firma completa reutilizable. Pendiente de decisión de
diseño: no se resuelve unilateralmente en la clase.
