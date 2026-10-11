# LafroX — Verificación del espejo del Subdocumento 4

## Alcance y fuentes

Petición explícita del usuario: hacer commit y push y asegurar igualdad de contenido entre Markdown y LaTeX. Se conserva la separación de ramas: `rama-md` solo versiona Markdown; `subdoc-4` conserva fuentes, figuras y PDF. No se editan otros subdocumentos, catálogos ni Bases.

Antes de publicar se actualizaron las referencias de origin. Bases de trabajo: `subdoc-4` en `292c6e8` y `rama-md` en `d8bc438`, esta última después de avance rápido desde `cf43057`. Se preservó y reaplicó sin conflictos el trabajo SD4 local; el stash `respaldo SD4 antes de sincronizar y publicar 2026-10-11` sigue disponible. Las carpetas locales `05/`, `md para drive/` y los borradores gráficos no forman parte de los commits.

## Correspondencia comprobada

| Entregable | Bloques de contenido cotejados | Diferencias normalizadas |
| --- | --- | --- |
| Cuerpo 4.1–4.3 | 1.579 | 0 |
| Anexos 4-A–4-W | 948 | 0 |
| Formulario T-11 | 110 | 0 |

El control compara secuencialmente párrafos, viñetas, títulos y filas de tabla del Markdown contra las entradas LaTeX realmente ensambladas. Normaliza sintaxis de énfasis, espacios, símbolos, enlaces y macros de presentación; no reemplaza auditoría contractual ni revisión humana. Se excluyen navegación y procedencia de figura de esta comparación textual y se comprueban aparte. Los residuos conocidos del conversor —declaraciones de capítulo, medidas de estilo y alineación de multicolumn— no son contenido de los entregables.

Los 27 títulos de figura y su numeración coinciden con la lista compilada. Se comprobaron sus 27 activos reales y las referencias numéricas a sus anclas. Los 342 enlaces internos entre los tres Markdown tienen destino y ancla válidos.

## Contenido sincronizado

- De Markdown a LaTeX: detalles vigentes de recepción, inventario, consulta comercial, rutas, cobranza, devoluciones, EDI y telemetría; AES-256/KMS; ASN al cargar distinto del acuse comercial tras descarga; Preproducción por campaña; bloqueo de duplicación sobre 3 % y herramientas Playwright, Pact, Spectral y MobSF; MC9400 premium con cámara de 16 MP.
- De LaTeX a Markdown: explicación, ancla y activo del diagrama de red corregido por el usuario; figura de emplazamiento ya existente como TikZ, exportada a PDF sin cambiar su dibujo; numeración correlativa y referencias actualizadas.
- Cuerpo, anexos y T-11 mantienen las mejoras previas de continuidad, dimensionamiento y consulta sanitaria. Los resúmenes SD4 se actualizan en Markdown.

## Conservación del diagrama aprobado

Fuente: [Red_general_sitios_regiones.drawio](../figuras/fuentes/fisica/Red_general_sitios_regiones.drawio).

SHA-256: `912bf7b551a9bd005b9e8f00b39d265faa7ff34221b6934f33cf4ee33b841aac`. Coincide con el XML corregido que el usuario envió desde Descargas. No se movieron objetos ni se alteraron sus conexiones.

Su exportación vectorial es [Red_general_sitios_regiones.pdf](../figuras/fisica/Red_general_sitios_regiones.pdf). Queda como Figura 24 en 4.2.4.2, página 132 del cuerpo compilado en esta ejecución. Los rótulos menores quedan próximos a 5 puntos al encajar el conjunto en carta: su legibilidad impresa sigue pendiente; no se declara satisfecho un mínimo de 9 puntos ni se modifica el diseño aprobado sin instrucción.

## Compilación y límites

Compilación con LuaLaTeX y tres pasadas por entregable: cuerpo 191 páginas, anexos 91 y T-11 46. Logs finales sin referencias indefinidas, desbordamientos ni caracteres faltantes. Se conserva el aviso preexistente de nombre de clase frente a su ruta. Se inspeccionan las páginas afectadas de cobranza, tecnologías, MC9400 y red.

La igualdad documental no acredita ensayos de autonomía, capacidad o recuperación ni aprobación del mandante. La revisión humana de IA y el riesgo de destrucción después del aislamiento de todos los enlaces mantienen su estado.

La renumeración afecta cinco referencias externas del T-12, fuera del alcance autorizado: RT-06.02, RT-06.03, RT-06.22 y RT-06.30 deben apuntar a Figura 27 (recinto), y RT-06.05 a Figura 26 (racks). No se modifica el Subdocumento 3 ni su matriz en esta tarea.

Los controles reproducibles están en [auditar_espejo.py](../herramientas/auditar_espejo.py) y [verificar_espejo.py](../herramientas/verificar_espejo.py). La ejecución requiere el checkout hermano Markdown y los auxiliares de los tres PDF; no escribe en las fuentes.
