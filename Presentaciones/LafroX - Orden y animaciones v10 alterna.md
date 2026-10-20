# V10 alterna corregida — Secuencias completas

**Esta guía reemplaza el criterio anterior de exposición y respaldo.** Las ampliaciones son pasos de animación intencionales y permanecen dentro del recorrido.

## Reproducción

- Se muestran las **53 diapositivas**, sin ocultas y sin un rango parcial.
- PowerPoint está configurado para **todas las diapositivas**, con animaciones y tiempos activados.
- No hay bloque de respaldo ni presentaciones personalizadas que excluyan contenido.
- La arquitectura lógica y sus ocho ampliaciones, las nueve fases EDT y todas las ramas de riesgos se mantienen consecutivas, en su orden interno original.
- Se mantienen juntos el Gantt de entrada y su continuación, y el par final «9 días → menos de dos horas».

## Qué se corrigió

La versión anterior conservaba físicamente las 53 diapositivas, pero mostraba únicamente 29 por defecto. Esa decisión fue incorrecta para la intención del usuario: los pasos de Morph son parte de la exposición dinámica, no anexos. La versión corregida reorganiza los bloques enteros y presenta todos sus estados.

Se conservaron los 50 efectos Morph, sus duraciones, los IDs y nombres de objetos y los dos avances automáticos (0,1 s en Gantt; 1,5 s en cierre). Al cambiar los límites entre bloques, las transiciones entre bloques pueden tener otra trayectoria; dentro de cada bloque se conserva la adyacencia original.

## Orden completo

| Nueva posición | Folio | Tema / etiqueta original | Posición en v10 original |
|---:|---|---|---:|
| 1 | — | Propuesta | 1 |
| 2 | 01 | 9 días | 2 |
| 3 | 02 | Problemática | 3 |
| 4 | 03 | Datos Clave | 4 |
| 5 | 04 | El Equipo · 8 personas · 10 roles · 7 líderes reportan al Jefe de Proyecto | 51 |
| 6 | 05 | Esquema de solución | 5 |
| 7 | 06 | Datos con una sola verdad | 17 |
| 8 | 07 | Mapa de módulos | 6 |
| 9 | 08 | Arquitectura lógica | 7 |
| 10 | 09 | Capa 1. Presentación | 8 |
| 11 | 10 | Capa 2. Borde y exposición | 9 |
| 12 | 11 | Capa 3. Enlace de servicios | 10 |
| 13 | 12 | Capa 4. Lógica de negocio | 11 |
| 14 | 13 | Capa 5. Integración y eventos | 12 |
| 15 | 14 | Capa 6. Acceso a datos | 13 |
| 16 | 15 | Capa 7. Seguridad transversal | 14 |
| 17 | 16 | Capa 8. Observabilidad transversal | 15 |
| 18 | 17 | Arquitectura física | 16 |
| 19 | 18 | Cómo se divide el proyecto | 30 |
| 20 | 19 | Gantt de implementación | 31 |
| 21 | 19 | Gantt de implementación | 32 |
| 22 | 20 | Metodología | 18 |
| 23 | 21 | Metodología | 19 |
| 24 | 22 | EDT: así se organiza el trabajo | 20 |
| 25 | 23 | EDT: así se organiza el trabajo | 21 |
| 26 | 24 | EDT: así se organiza el trabajo | 22 |
| 27 | 25 | EDT: así se organiza el trabajo | 23 |
| 28 | 26 | EDT: así se organiza el trabajo | 24 |
| 29 | 27 | EDT: así se organiza el trabajo | 25 |
| 30 | 28 | EDT: así se organiza el trabajo | 26 |
| 31 | 29 | EDT: así se organiza el trabajo | 27 |
| 32 | 30 | EDT: así se organiza el trabajo | 28 |
| 33 | 31 | EDT: así se organiza el trabajo | 29 |
| 34 | 32 | Esfuerzo por mes | 33 |
| 35 | 33 | Normas y leyes | 45 |
| 36 | 34 | Calidad del producto | 46 |
| 37 | 35 | Calidad quebloquea | 47 |
| 38 | 36 | Pruebas: del código al terreno | 48 |
| 39 | 37 | Trazabilidad y mejora | 49 |
| 40 | 38 | RBS: de dónde vienen los riesgos | 34 |
| 41 | 39 | RBS: así se clasifican los riesgos | 35 |
| 42 | 40 | RBS: así se clasifican los riesgos | 36 |
| 43 | 41 | RBS: así se clasifican los riesgos | 37 |
| 44 | 42 | RBS: así se clasifican los riesgos | 38 |
| 45 | 43 | RBS: así se clasifican los riesgos | 39 |
| 46 | 44 | RBS: así se clasifican los riesgos | 40 |
| 47 | 45 | RBS: así se clasifican los riesgos | 41 |
| 48 | 46 | RBS: así se clasifican los riesgos | 42 |
| 49 | 47 | Riesgos principales | 43 |
| 50 | 48 | Matriz de exposición | 44 |
| 51 | 49 | 5 innovaciones · Siguiente · Sin hardware nuevo · TRL 2 → 4 → 6 | 50 |
| 52 | 50 | 9 días | 52 |
| 53 | 50 | < 2 horas | 53 |

## Alcance

El contenido técnico y las notas se conservaron. Las discrepancias de contenido de la auditoría siguen pendientes; no se interpretan como resueltas por este reordenamiento. La v10 original no fue modificada. La alterna anterior quedó archivada en Antiguos como «recorrido parcial anterior», para evitar confundirla con esta corrección.

## Key Learnings:

1. Un paso de Morph que parece repetido puede ser necesario para la narrativa visual: no debe apartarse de la exposición sin autorización.
2. Para conservar el dinamismo, hay que reordenar los bloques animados completos, no sus diapositivas por separado.
