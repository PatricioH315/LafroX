# Plantilla de presentación LafroX

Plantilla PowerPoint de 21 láminas (formato 20 × 11,25 in) generada por código. Incluye layouts, gráficos editables, tablas, figuras decorativas y transiciones Morph.

## Regenerar la plantilla

Requisitos:

- Node.js.
- `pptxgenjs` y `jszip` (en `C:/Users/henri/node_modules` o con `npm i pptxgenjs jszip`).
- Fuente **Inter** (Regular, SemiBold y Light) instalada en el equipo.

```bash
node build_template.js   # genera "LafroX - Plantilla.pptx"
```

No edite el `.pptx` a mano si piensa regenerarlo: los cambios se pierden. Modifique `build_template.js` y vuelva a ejecutarlo. Los textos de las láminas son de ejemplo.

## Estructura del repositorio

| Ruta | Contenido |
| --- | --- |
| `build_template.js` | Generador: layouts, láminas, figuras, post-proceso (SVG, Morph, gráficos) y tema. |
| `assets/` | Fondo oscuro e isotipos de la marca. |
| `assets/decor/` | Figuras decorativas en SVG (13 archivos). |
| `assets/decor/png/` | Versión PNG (2400 px) de cada figura, usada como respaldo para Google Slides. |
| `tools/rasterize_decor.py` | Regenera los PNG desde los SVG (`python -I tools/rasterize_decor.py`, requiere PyMuPDF). |
| `LafroX - Plantilla.pptx` | Resultado del build. |

## Catálogo de láminas

| N° | Nombre | Layout | Cuándo usarla |
| --- | --- | --- | --- |
| 1 | Portada | PORTADA | Abrir la presentación. |
| 2 | Agenda | CONTENIDO | Anticipar la estructura (seis ítems). |
| 3 | Divisor de sección | SECCION | Separar bloques temáticos. |
| 4 | Equipo de trabajo | CONTENIDO | Presentar roles y personas. |
| 5 | KPIs | CONTENIDO_OSCURO | Destacar cuatro cifras clave y una meta. |
| 6 | Síntomas y causa raíz | CONTENIDO | Pasar del síntoma al origen. |
| 7 | Tabla estándar | CONTENIDO | Datos tabulares con total. |
| 8 | Tabla antes / después | CONTENIDO | Comparar situación actual y propuesta con estado. |
| 9 | Barras horizontales | CONTENIDO | Ranking de una serie con barra destacada. |
| 10 | Columnas apiladas | CONTENIDO | Composición por período. |
| 11 | Líneas | CONTENIDO | Evolución frente a una meta. |
| 12 | Dona | CONTENIDO | Distribución porcentual con total central. |
| 13 | Combo Pareto | CONTENIDO | Frecuencia y acumulado (eje secundario). |
| 14 | Gantt | CONTENIDO | Plan por etapas con hitos. |
| 15 | Proceso en pasos | CONTENIDO | Flujo de cinco pasos y resultado esperado. |
| 16 | Texto + imagen | CONTENIDO | Argumento con apoyo visual. |
| 17 | Matriz 2×2 | CONTENIDO | Riesgos por probabilidad e impacto. |
| 18 | Cita | CONTENIDO | Mensaje clave previo al cierre. |
| 19 | Cierre | CIERRE | Preguntas y datos de contacto. |
| 20 | Guía de estilo | CONTENIDO | Referencia de paleta, tipografía y reglas (no se presenta). |
| 21 | Biblioteca de figuras | CONTENIDO | Copiar figuras decorativas y conocer su nombre (no se presenta). |

## Uso en PowerPoint

- **Duplicar una lámina:** clic derecho sobre la miniatura > *Duplicar diapositiva*. Cada lámina trae notas del orador con indicaciones de uso.
- **Textos de título y subtítulo:** se editan en los marcadores de la lámina (portada, divisor, cierre y título de contenido).
- **Gráficos:** clic derecho sobre el gráfico > *Editar datos*. Los colores por punto (barra naranjo destacada, Pareto) se ajustan en *Formato de punto de datos*.
- **Tablas:** seleccione la tabla y use *Disposición* para agregar filas o columnas; mantenga el alto de fila para conservar el ritmo.
- **Marcas ✓/✗ de la tabla comparativa:** son formas sobre la tabla; si cambia el alto de las filas, muévalas junto con ellas.

## Morph y figuras decorativas

Todas las láminas, salvo la portada, tienen transición **Morph** (Transiciones > Morph, opción *Objetos*; 1,2 s). PowerPoint anima los objetos que tienen **el mismo nombre** en dos láminas consecutivas: la figura se desplaza, escala o rota de una posición a otra.

Regla de nombres `!!`:

- Las figuras decorativas se llaman `!!deco_<tipo>_<n>` (por ejemplo `!!deco_anillos_1`). Para que una figura se anime, debe tener **exactamente el mismo nombre** en láminas consecutivas.
- Para renombrar: *Inicio > Organizar > Panel de selección*, doble clic sobre el nombre.
- Para animar: en la lámina siguiente, mueva, escale o rote la figura; no cambie el nombre.
- Una figura que aparece solo en una lámina entra y sale con desvanecimiento.
- Algunas tarjetas recurrentes también usan nombres `!!` (`!!tarjeta_1`, `!!panel_oscuro`), por lo que se desplazan entre láminas consecutivas.

Para **desactivar** Morph: seleccione las láminas > Transiciones > *Ninguna*. En el generador, ajuste la constante `MORPH` (`enabled`, `skip`, `durMs`).

**Google Slides no soporta Morph:** la transición cae a *desvanecer*. Las figuras se ven con su PNG de respaldo.

Las figuras se insertan como SVG con PNG de respaldo: se mantienen nítidas en PowerPoint. Guía de uso:

- Láminas claras: figuras sutiles (`anillos` al 5 % de opacidad, `cuarto-circulo`, `mosaico`).
- Láminas oscuras y naranjas: ondas (`onda-naranjo`, `onda-naranjo-claro`).
- Mantenga las figuras detrás del contenido y saliendo por los bordes; no deben cubrir texto.

## Paleta, tipografía y reglas de diseño

| Color | HEX | Color | HEX |
| --- | --- | --- | --- |
| Negro | `111111` | Gris claro | `C7C7C7` |
| Carbón | `141414` | Humo | `F4F4F4` |
| Grafito | `3C3C3C` | Blanco | `FFFFFF` |
| Gris oscuro | `606060` | **Naranjo** | `E8641B` |
| Gris | `9A9A9A` | Durazno | `F29A5E` |

- **Tipografía:** Inter SemiBold para títulos; Inter para texto. Escala: título 44 pt, subtítulo 28 pt, cuerpo 18 pt, notas 13 pt.
- **Márgenes:** 1,61 in a cada lado (contenido de 16,8 in de ancho); el contenido comienza en y = 3,1 in y termina en y = 10,2 in.
- **Tamaños mínimos:** cuerpo desde 16 pt; notas de fuente 13 pt.
- **Un solo título** por lámina; sin líneas bajo los títulos.
- **Naranjo solo como acento** para destacar (cifras, barra principal, encabezados de tabla).
- Una idea por lámina; cifras con coma decimal (82,4 %).

## Limitaciones conocidas

- El número de lámina se muestra sin cero a la izquierda (2, no 02).
- Las marcas ✓/✗ de la tabla comparativa son formas superpuestas, no parte de la tabla.
- Requiere la fuente Inter instalada; sin ella, PowerPoint sustituye la tipografía y cambian los anchos de texto.
- Morph solo funciona en PowerPoint 2019 o posterior y Microsoft 365.
- La figura `figura.svg` está en la biblioteca, pero no se usa en ninguna lámina de ejemplo.
