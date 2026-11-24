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
| 1 | Portada | Alex Aravena | 0:20 |
| 2 | El equipo | Alex Aravena | 0:45 |
| 3 | Agenda de la exposición | Alex Aravena | 1:10 |
| 4 | 9 días | Alex Aravena | 1:40 |
| 5 | Problemática | Alex Aravena | 2:35 |
| 6 | Mapa de módulos | Bastián Trejo | 3:15 |
| 7 | Arquitectura lógica en ocho capas | Bastián Trejo | 3:40 |
| 8 a 15 | Capas 1 a 8 | Bastián Trejo / Tomás Pérez | 3:48 a 4:44 |
| 16 | Trazabilidad y continuidad | Tomás Pérez | 5:14 |
| 17 | Metodología | Alex Aravena | 5:29 |
| 18 | RUP y DevSecOps | Alex Aravena | 5:41 |
| 19 | Cómo se divide el proyecto | Alex Aravena | 5:53 |
| 20 y 21 | Gantt (colapsado y desplegado) | Alex Aravena | 5:55 y 6:13 |
| 22 | EDT: base | Alex Aravena | 6:25 |
| 23 a 32 | EDT: productos 1 a 10 (1 a 7 Alex, 8 a 10 Guillermo Castillo) | Alex Aravena / Guillermo Castillo | 6:34 a 7:55 (9 s c/u) |
| 33 | Calidad: criterios clave | Maximiliano Miño | 8:20 |
| 34 | RBS: ramas | Alex Aravena | 8:30 |
| 35 | RBS: base | Alex Aravena | 8:40 |
| 36 a 41 | RBS: ramas 1 a 6 | Guillermo Castillo | 8:49 a 9:34 (9 s c/u) |
| 42 | Diez riesgos de mayor exposición | Guillermo Castillo | 9:47 |
| 43 | Matriz de exposición | Alex Aravena | 10:00 |
| 44 | Cinco innovaciones | Patricio Henríquez | 11:00 |
| 45 | Nuestra oferta (divisor) | Leandro Chamorro | 11:05 |
| 46 | Precio total | Leandro Chamorro | 11:35 |
| 47 | Del precio a la estructura de costo | Leandro Chamorro | 12:05 |
| 48 | Forma de pago | Leandro Chamorro | 12:35 |
| 49 | Innovaciones en el flujo | Leandro Chamorro | 13:00 |
| 50 | Curva S | Leandro Chamorro | 13:25 |
| 51 | Rentabilidad | Leandro Chamorro | 13:50 |
| 52 | Sensibilidad | Leandro Chamorro | 14:15 |
| 53 | Compromisos medibles | Alex Aravena | 14:35 |
| 54 | 9 días (desvanecer, avance automático) | Alex Aravena | 14:38 |
| 55 | De 9 días a < 2 horas y contacto | Alex Aravena | 15:00 |
| 56 a 60 | Anexo: divisor, supuestos, proveedores, adquisiciones, flujo mensual | solo para preguntas | |
