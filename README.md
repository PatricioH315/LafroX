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
| `build_template.js` | Generador de la plantilla (láminas de ejemplo). |
| `lib/lafrox.js` | Biblioteca compartida: tema, layouts, helpers, figuras `deco()`, estilo de gráficos y post-proceso (SVG, transiciones Morph/fade por lámina, corrección de gráficos combinados). |
| `lib/format.js` | Formato numérico chileno (miles con punto, decimales con coma). |
| `build_final.js`, `slides/*.js` | Generador de la presentación final (una función por bloque). |
| `tools/extract_final_data.py` | Lee el modelo financiero SD7 y escribe `data/final.json`. |
| `data/final.json` | Cifras de la presentación final (única fuente de números de `build_final.js`). |
| `assets/final/` | Diagramas de arquitectura (vista general y 8 capas), figuras 3.1 a 3.3 y arquitectura física, extraídos de la presentación Informe 2 v4. |
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

## Presentación final

`LafroX - Presentación Final.pptx`: exposición de LafroX SpA ante la Comisión Evaluadora de Distribuidora Puelche (Licitación TFEP-01/2026, 27-11-2026; 15 min de exposición y 15 de preguntas). 47 láminas: 41 de exposición y 6 de anexo. Todas llevan notas del orador (presentador, hora objetivo acumulada y guion).

Regenerar:

```bash
python -I tools/extract_final_data.py   # lee el modelo SD7 y escribe data/final.json
node build_final.js                     # genera "LafroX - Presentación Final.pptx"
```

Fuente de los números: `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX-worktrees/sd7-corrigiendo/outputs/sd7-ajuste-20261122/LafroX_ModeloFinanciero_3_SD7.xlsx` (se puede pasar otra ruta como argumento del extractor). Las celdas se ubican por etiqueta. Los datos que no vienen del modelo (EDT, RBS, matriz y top-10 de riesgos, metas de innovaciones, criterios de calidad) están en el bloque `documentos` del extractor y provienen de los subdocumentos. `build_final.js` no contiene cifras escritas a mano.

Transiciones: Morph de 1,2 s en todas las láminas, salvo la 1 y la 40 (desvanecer; la 40 avanza sola a los 1,5 s) y la 20 (Morph de 1,4 s con avance automático a los 0,1 s). Los objetos con el mismo nombre `!!` en láminas consecutivas se animan (título `!!title`, `!!reloj`, `!!thumb`, `!!capahl`, `!!gv_*`, `!!precio`, `!!inn_*`, `!!kpi_*`, etc.).

| N° | Lámina | Presentador | Hora |
| --- | --- | --- | --- |
| 1 | Portada | Alex Aravena | 0:20 |
| 2 | El equipo | Alex Aravena | 0:50 |
| 3 | Agenda de la exposición | Alex Aravena | 1:20 |
| 4 | 9 días | Alex Aravena | 1:50 |
| 5 | Problemática | Alex Aravena | 3:00 |
| 6 | Mapa de módulos | Bastián Trejo | 3:50 |
| 7 | Arquitectura lógica en ocho capas | Bastián Trejo | 4:15 |
| 8 a 15 | Capas 1 a 8 | Bastián Trejo / Tomás Pérez | 4:27 a 5:51 |
| 16 | Trazabilidad y continuidad | Tomás Pérez | 6:30 |
| 17 | Metodología | Alex Aravena | 6:50 |
| 18 | RUP y DevSecOps | Alex Aravena | 7:05 |
| 19 | Cómo se divide el proyecto | Alex Aravena | 7:20 |
| 20 y 21 | Gantt (colapsado y desplegado) | Alex Aravena | 7:22 y 7:45 |
| 22 a 24 | EDT (base, Construcción, Operación y soporte) | Alex Aravena / Guillermo Castillo | 8:00 a 8:30 |
| 25 | Calidad: criterios clave | Maximiliano Miño | 9:00 |
| 26 a 29 | RBS, rama 1 y matriz de exposición | Alex Aravena / Guillermo Castillo | 9:10 a 10:00 |
| 30 | Cinco innovaciones | Patricio Henríquez | 11:00 |
| 31 | Nuestra oferta (divisor) | Leandro Chamorro | 11:05 |
| 32 | Precio total | Leandro Chamorro | 11:35 |
| 33 | Del precio a la estructura de costo | Leandro Chamorro | 12:05 |
| 34 | Forma de pago | Leandro Chamorro | 12:35 |
| 35 | Innovaciones en el flujo | Leandro Chamorro | 13:00 |
| 36 | Curva S | Leandro Chamorro | 13:25 |
| 37 | Rentabilidad | Leandro Chamorro | 13:50 |
| 38 | Sensibilidad | Leandro Chamorro | 14:15 |
| 39 | Compromisos medibles | Alex Aravena | 14:35 |
| 40 | 9 días (desvanecer, avance automático) | Alex Aravena | 14:38 |
| 41 | De 9 días a < 2 horas y contacto | Alex Aravena | 15:00 |
| 42 a 47 | Anexo: divisor, supuestos, proveedores, adquisiciones, flujo mensual, top-10 de riesgos | solo para preguntas | |
