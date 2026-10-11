# Ajustar la tabla T-16 a las Bases Administrativas

## Objetivo
Alinear la tabla del Formulario T-16 con su estructura real en las Bases Administrativas y mantener actualizadas sus mitigaciones según las fuentes vigentes.

## Autoridad y decisiones
- Destino: `Lafrox-Subdocumento-T-16.tex` (el archivo ya tenía cambios locales; se preservó todo lo ajeno a esta tarea).
- Estructura: `ID | Riesgo | Categoría | Prob. | Impacto | Expos. | Mitigación | Responsable`.
- Categoría: rama RBS de nivel 1, según el punto 2 del CSV actualizado, determinada por el primer dígito del código RBS de cada riesgo.
- Probabilidad e impacto: las ponderaciones decimales del registro se mapean a bandas: 0–20 %→1, >20–40 %→2, >40–60 %→3, >60–80 %→4, >80–100 %→5. Exposición = P ordinal × I ordinal; no mezclar valores de impacto en HH.
- Escala local: en esta rama no está el SD6 mencionado por el usuario; el usuario autorizó usar la escala visible en `08_plan_riesgos/contenido.tex` (SD8).
- Mitigaciones: del punto 6 de `Datos externos/Tablas_tiesgos/(Nueva)LafroX-Riesgos-actualizadosr.xlsx - Riesgos LafroX.csv`, unión por ID y `Estrategia — Acción concreta` (incluida `Validar:`). No se duplican responsable, disparador, costo ni etapa.
- No se modificaron los CSV ni otros documentos. No se creó commit.

## Tareas
1. [x] Alinear estructura T-16, escala y categorías RBS de nivel 1 con las fuentes acordadas.
2. [x] Mejorar legibilidad de la tabla y validar el formato paginado.
3. [x] Integrar las 45 mitigaciones del punto 6 del CSV nuevo por ID.
4. [x] Actualizar la columna Categoría para usar rama RBS de nivel 1.
5. [x] Compilar y verificar estructura, mapeo y presentación.

## Evidencia final
- Bases Administrativas, líneas 1743–1752: orden de las ocho columnas.
- Punto 2 del CSV actualizado, líneas 56–65: siete ramas RBS; todos los códigos de R-001–R-045 usan un primer dígito entre 1 y 7 que identifica su rama.
- Punto 6 del CSV nuevo: Tabla 9 contiene respuestas por ID; Tabla 10 es otra vista de las mismas respuestas.
- T-16 incluye los 45 IDs en secuencia y ocho columnas por fila. Categoría corresponde a una de las siete ramas: Solución y tecnología; Integración y legado; Operación del cliente; Personas y adopción; Contrato y licitación; Regulatorio y externo; Empresa proveedora.
- Mitigación toma `Estrategia — Acción concreta` de Tabla 9, incluida `Validar:`; responsable no se duplica dentro de la acción.
- Columnas elásticas `Y` y campos fijos `F/G` conforme a `lafrox.cls` evitan que la tabla se comprima.
- Compilación final LuaLaTeX/latexmk: exit 0, PDF de 21 páginas en carpeta temporal; warnings no bloqueantes `\\@parboxrestore` y orden `fvextra`/`csquotes`.
- Verificación estructural previa: 45 IDs consecutivos, ocho celdas por fila, mitigaciones pobladas; el último cambio solo modificó la Categoría por primer dígito RBS y se comprobó visualmente en página 16.
- `git diff --check` sin errores de whitespace. Git avisa LF→CRLF en el próximo toque.
- No se creó commit ni se sustituyó el PDF local preexistente.
