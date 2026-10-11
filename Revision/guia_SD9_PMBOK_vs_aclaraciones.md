# Guía de trabajo SD9 — PMBOK cap. 8 frente a la estructura de las Aclaraciones

Nota de trabajo (no entregable). Contrasta tres fuentes: el PMBOK 6, cap. 8 (`clases + pmbok/PMBOK6_Cap08_Gestion_de_la_Calidad_transcripcion.md`), la estructura obligatoria del Capítulo 9 (`Bases/aclaraciones-licitacion.md`, §11) y el estado actual de `09_plan_calidad/LAFROX-Subdocumento9.md`.

Precedencia: las Aclaraciones fijan los títulos y el contenido obligatorio. El PMBOK orienta el método y no crea requisitos. En la oferta se cita como Project Management Institute (2017), nunca con el nombre del archivo local. Las clases FEP01–FEP05 no tienen una clase dedicada a calidad; lo único pertinente es FEP01, diapositivas 13–15 (atributos ISO/IEC 25010), y FEP02, diapositiva 44 (validar el alcance frente a controlar la calidad).

## 1. Estructura obligatoria del Capítulo 9 frente al SD9

| Título obligatorio | Contenido exigido | Estado en el SD9 |
|---|---|---|
| Introducción | Resumen y conexión con capítulos, anexos y formularios | Cumple. Cita SD3–SD8, SD13, T-13 y T-17 |
| 9.1 Plan de Calidad | ISO/IEC 25010, modelos de madurez, métricas de código, cobertura, complejidad y acoplamiento con umbrales bloqueantes | Cumple: 9.1.1 a 9.1.5, Tablas 9.2–9.4 |
| 9.2 Estrategia de Aseguramiento de Calidad | Puertas, revisión por pares, análisis estático y dinámico; ISO/IEC/IEEE 29119 (niveles, tipos, ambientes, datos, automatización); V&V y trazabilidad requisito → diseño → código → prueba → despliegue | Cumple: 9.2.1 a 9.2.6, Figuras 9.3–9.8 |
| 9.3 Alineación con Plan de Trabajo | Actividades de calidad en la EDT y el cronograma del Cap. 7 | Cumple: 9.3.1 a 9.3.3, Tablas 9.10–9.14 |
| Referencias / Declaración de uso de IA | Sin numerar, en ese orden | Cumple la forma; la declaración tiene celdas `[[REVISIÓN HUMANA]]` abiertas (bloqueante, §7.1 d) |

## 2. Componentes del PMBOK frente al SD9

### 2.1 Planificar la gestión de la calidad (PMBOK pp. 277–287)

| Elemento del PMBOK | Página | Dónde está en el SD9 | Estado |
|---|---|---|---|
| Estándares de calidad | 286 | 9.1.1, Figura 9.1 | Cubierto |
| Objetivos de calidad del proyecto | 286 | Implícitos en los umbrales (Tabla 9.2) | Falta enunciarlos |
| Roles y responsabilidades | 286 | 9.1.1, Tabla 9.1 | Cubierto |
| Entregables y procesos sujetos a revisión | 286 | Tabla 9.8, T-17 | Cubierto |
| Actividades de gestión y control | 286 | 9.2 completa | Cubierto |
| Herramientas de calidad | 286 | 9.1.4, 9.2.2 | Cubierto |
| No conformidad, acción correctiva, mejora continua | 286 | 9.2.6, Tabla 9.9 | Cubierto |
| Métricas de calidad | 287 | 9.1.4, 9.1.5 | Cubierto |
| Prevención frente a inspección | 274 | 9.2.1 («el control es más barato cuanto antes ocurre») | Implícito; falta nombrarlo |
| Costo de la calidad (COQ) | 274, 282–283 | — | Ausente |
| Análisis costo-beneficio de las actividades de calidad | 282 | — | Ausente |
| Planificación de pruebas e inspección | 285 | 9.2.3, T-13 | Cubierto |

### 2.2 Gestionar la calidad / aseguramiento (PMBOK pp. 288–297)

| Elemento del PMBOK | Página | Dónde está en el SD9 | Estado |
|---|---|---|---|
| Aseguramiento frente a control | 290 | 9.1.1 (lo cita expresamente) | Cubierto |
| Listas de verificación | 292 | Tabla 9.8 | Cubierto |
| Análisis de causa raíz | 292 | 9.2.6 | Cubierto, sin técnica nombrada |
| Diagramas de causa y efecto (Ishikawa) | 293–294 | — | Ausente |
| Auditorías de calidad | 294 | 9.1.2 (trimestrales de trazabilidad) | Cubierto |
| Métodos de mejora (PDCA) | 296 | Tabla 9.9 sigue un ciclo de cinco pasos | Implícito; falta nombrar PDCA |
| Informes de calidad | 296 | «Informes y matriz 9.C» (Figura 9.1) | Parcial: no dice contenido, frecuencia ni destinatario |
| Solicitudes de cambio → control integrado de cambios | 296 | — (está en T-9, sección 5) | Falta el vínculo |
| Registro de lecciones aprendidas | 297 | — (tampoco en SD6 ni T-9) | Ausente |

### 2.3 Controlar la calidad (PMBOK pp. 298–306)

| Elemento del PMBOK | Página | Dónde está en el SD9 | Estado |
|---|---|---|---|
| Inspección y pruebas | 303–304 | 9.2.3, Tabla 9.6 | Cubierto en profundidad |
| Muestreo estadístico | 303 | 9.2.4 (muestra de reidentificación) | Cubierto |
| Hojas de verificación | 302 | — | Ausente |
| Diagramas de control; tolerancias frente a límites de control | 274, 304 | — | Ausente |
| Histogramas / Pareto | 293, 304 | — | Ausente |
| Revisiones del desempeño | 303 | Comité de Calidad mensual (9.1.1, 9.1.5) | Cubierto |
| Retrospectivas | 276, 305 | — | Ausente |
| Entregables verificados → Validar el alcance | 305 | Acta T-17 (9.3.2, Figura 9.10) | Cubierto sin nombrar el vínculo |

## 3. Qué agregar, dónde y con qué cifra

Ninguna adición crea títulos del mismo nivel (§2 de las Aclaraciones). Todo entra como texto o subtítulo de menor nivel bajo un título existente.

1. **COQ sin montos (9.1.1 o 9.3.1).** Reclasificar las 10.848 HH de la Tabla 9.10 en prevención (1.2/1.5, 2.6, 3.10.2), evaluación (3.8, 3.9, 4.1/7.3, 8.1–8.3) y costo de fallas (reservas R8-18 y las 153,6 HH esperadas de R8-31). Se expresa en HH, no en dinero (Art. 50.2). Responde al PMBOK pp. 274 y 282–283 con cifras que ya existen.
2. **Objetivos de calidad (9.1.1).** Tres o cuatro objetivos medibles que agrupen la Tabla 9.2 (por ejemplo, 0 defectos críticos o altos al cierre de marcha blanca, 100 % de requisitos ofertados con prueba aprobada).
3. **Tolerancia frente a límite de control (9.1.5).** La regresión de p95 de G3 (10 %) es una tolerancia; agregar límites de control estadísticos para el p95 semanal y la densidad de defectos, con un diagrama de control como figura explicada. Agregar un Pareto de causas de defectos como insumo del Comité.
4. **Lecciones aprendidas y retrospectivas (9.2.6).** Registro de lecciones aprendidas alimentado por la Tabla 9.9 y por una retrospectiva al cierre de cada certificación (H5, H10) y de cada marcha blanca (H7, H12). Coordinar con SD6 6.2.3, que hoy no las menciona.
5. **Solicitudes de cambio (9.2.6).** Una frase que derive al control integrado de cambios del T-9, sección 5, cuando una acción de mejora toque la línea base.
6. **Informes de calidad (9.1.1 o 9.2.6).** Contenido, frecuencia (mensual, al Comité y a la Contraparte Técnica) y relación con la matriz 9.C.
7. **Validar el alcance (9.3.2).** Declarar que el acta del T-17 es la validación del alcance que recibe los entregables verificados por el control de calidad (PMBOK p. 305; FEP02, diapositiva 44).
8. **Nombrar las técnicas que ya se usan.** «Prevención antes que inspección» en 9.2.1; PDCA en la Tabla 9.9; Ishikawa como técnica del análisis de causa raíz en 9.2.6.

## 4. Defectos formales detectados de paso

- **Viñetas duplicadas en 9.2.3** (líneas 313–317): los ítems «855 casos…» y «356 casos…» aparecen dos veces, con una línea en blanco entre ellos. Eliminar la repetición.
- **Tablas 9.12 y 9.13 con seis columnas**: la §5 fija cinco como referencia. Fusionar «Responsable» con «Financiamiento» en la 9.12; en la 9.13, quitar «Entrega programada» o llevarla al T-17.
- **«Guía de control y evidencia» y «Mejora continua…» como `####` sin número**: se aceptan como subtítulos de menor nivel, pero conviene numerarlos (9.1.1.1, 9.2.6.1) para que el índice sea uniforme.
- **«se presentan primero como borrador» (9.3.2)**: el uso es legítimo, pero la palabra «borrador» figura en la lista de indicios de la §7.1 d. Conviene reemplazarla por «versión preliminar».
- **Figuras en Mermaid**: la regla del proyecto exige que la figura del Markdown enlace la imagen real; los `.drawio` de `09_plan_calidad/Diagramas/` deben ser la fuente del PDF.
- **Declaración de uso de IA**: las celdas `[[REVISIÓN HUMANA]]` siguen abiertas; a partir del Informe 2 eso significa SD no presentado.
