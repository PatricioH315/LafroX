# LafroX — Auditoría y reorganización de tablas del SD4

Fecha: 11 de octubre de 2026. Registro de trabajo; no forma parte del texto entregable.

## Alcance y criterio

Se revisaron las 39 tablas originales del cuerpo (38 técnicas y declaración de IA), las matrices asociadas de anexos y T-11. Solo se modificó SD4 y su espejo Markdown/LaTeX, preservando los cambios locales anteriores. Sin commit ni push.

La sección 5 de las [Aclaraciones](../../../LafroX-alvaro-md/Bases/aclaraciones-licitacion.md) reserva las tablas del cuerpo para comparaciones; excluye explicaciones en celdas, pide no superar una página como referencia, mínimo 9 puntos, orientación vertical, fuente y análisis. Esa sección excluye anexos y formularios, sujetos a legibilidad. La sección 7.2 exige la declaración de IA al final del subdocumento con seis columnas y filas por sección, anexo y formulario; no se puede trasladar íntegramente a anexos ni sustituirla por texto.

## Resultado

- Nueve tablas explicativas convertidas en punteos: originales 9, 10, 12, 15, 16, 19, 20, 36 y 38.
- Tres matrices trasladadas: original 6 (inventario) a 4-W/A.35; original 7 (correspondencia) a 4-N/A.14; original 32 (dieciséis dimensiones) a 4-W/A.30.
- Cuatro cuadros numéricos aligerados: original 22 separa derivaciones; original 26 separa escenarios; original 29 separa acciones; original 30 separa las fuentes y conserva su asociación con cada operación.
- Se eliminaron dos columnas de valor constante: estrategia y reversión del WMS (original 1) y techo de Fargate (original 28). Su valor común permanece explícito junto a cada cuadro.
- La original 8 (distribución por dominio y criterio) se mantiene como Tabla 6: siete filas, cinco columnas y valores comparables, no un listado explicativo.
- La original 16 pasa a punteos por dominio con frecuencia, retención y restauración intactas.
- Quedan 26 tablas técnicas breves y una declaración de IA. Ninguna tabla técnica se divide entre páginas. Todas permanecen en vertical, con tipografía institucional de 9,5 puntos para los datos y sin partición automática de palabras.
- La declaración conserva sus 56 filas y 56 celdas pendientes de revisión humana. Diecisiete finalidades extensas se desarrollan en punteos de la propia declaración; las celdas quedan breves. La tabla obligatoria sigue varias páginas, repite encabezado y permanece en vertical.
- Los anexos contienen 40 tablas y T-11 su tabla oficial. No se altera el formato técnico de T-11; se actualizan las referencias afectadas.

## Decisión por tabla original

La numeración de esta primera columna corresponde al estado anterior a esta reorganización. Los identificadores originales se conservan para mantener trazabilidad, incluso cuando el destino es un listado.

| Tabla original | Título | Decisión | Referencia actual | Motivo |
| --- | --- | --- | --- | --- |
| 1 | Capacidad absorbida del WMS 2013 por ola | Tabla breve + dato común | 1 | Columna constante trasladada a texto común; valor conservado. |
| 2 | Clasificación lógica y protección de la información | Conservar tabla breve | 2 | Comparación breve con datos o decisiones en varias dimensiones. |
| 3 | Dependencias singulares y riesgo residual | Conservar tabla breve | 3 | Comparación breve con datos o decisiones en varias dimensiones. |
| 4 | Alternativas lógicas y criterio de selección | Conservar tabla breve | 4 | Comparación breve con datos o decisiones en varias dimensiones. |
| 5 | Detección del primer cuello de botella | Conservar tabla breve | 5 | Comparación breve con datos o decisiones en varias dimensiones. |
| 6 | Equipamiento en operación por familia y por sitio | Anexo 4-W | A.35 | Inventario o síntesis extensa; conservar matriz y valores en la memoria. |
| 7 | Correspondencia entre la arquitectura lógica y la física | Anexo 4-N | A.14 | Matriz completa de trazabilidad; conservar sus cuatro dimensiones. |
| 8 | Distribución de los componentes por dominio y criterio de emplazamiento | Conservar tabla breve | 6 | Comparación breve con datos o decisiones en varias dimensiones. |
| 9 | Autonomía por ámbito ante la pérdida del enlace | Punteos | Listado en el mismo apartado | Explica procesos, reglas o respuesta ante fallas; no requiere cuadrícula. |
| 10 | Servicios contratados en la plataforma de nube, por función | Punteos | Listado en el mismo apartado | Explica procesos, reglas o respuesta ante fallas; no requiere cuadrícula. |
| 11 | Ambientes de despliegue | Conservar tabla breve | 7 | Comparación breve con datos o decisiones en varias dimensiones. |
| 12 | Perfiles de ejecución del artefacto Laravel | Punteos | Listado en el mismo apartado | Explica procesos, reglas o respuesta ante fallas; no requiere cuadrícula. |
| 13 | Ventanas de despliegue | Conservar tabla breve | 8 | Comparación breve con datos o decisiones en varias dimensiones. |
| 14 | Direccionamiento y segmentación | Conservar tabla breve | 9 | Comparación breve con datos o decisiones en varias dimensiones. |
| 15 | Clasificación de servicios por nivel de servicio | Punteos | Listado en el mismo apartado | Explica procesos, reglas o respuesta ante fallas; no requiere cuadrícula. |
| 16 | Respaldo y restauración por dominio de datos | Punteos | Listado en el mismo apartado | Explica procesos, reglas o respuesta ante fallas; no requiere cuadrícula. |
| 17 | Conexiones de la solución y su camino alternativo | Conservar tabla breve | 10 | Comparación breve con datos o decisiones en varias dimensiones. |
| 18 | Superficie de exposición | Conservar tabla breve | 11 | Comparación breve con datos o decisiones en varias dimensiones. |
| 19 | Puntos de falla en los sitios y en los enlaces | Punteos | Listado en el mismo apartado | Explica procesos, reglas o respuesta ante fallas; no requiere cuadrícula. |
| 20 | Puntos de falla en la nube, el terreno y las integraciones | Punteos | Listado en el mismo apartado | Explica procesos, reglas o respuesta ante fallas; no requiere cuadrícula. |
| 21 | Calendario y factores de diseño | Conservar tabla breve | 12 | Comparación breve con datos o decisiones en varias dimensiones. |
| 22 | Transacciones por segundo por lugar de proceso | Tabla breve + punteos | 13 | Comparación numérica; explicación o citas fuera de las celdas. |
| 23 | Concurrencia por ventana | Conservar tabla breve | 14 | Comparación breve con datos o decisiones en varias dimensiones. |
| 24 | Volumen, retención y destino de los datos | Conservar tabla breve | 15 | Comparación breve con datos o decisiones en varias dimensiones. |
| 25 | Mensajes de integración por grupo | Conservar tabla breve | 16 | Comparación breve con datos o decisiones en varias dimensiones. |
| 26 | Ancho de banda por sitio y camino | Tabla breve + punteos | 17 | Comparación numérica; explicación o citas fuera de las celdas. |
| 27 | Capacidad requerida por sitio | Conservar tabla breve | 18 | Comparación breve con datos o decisiones en varias dimensiones. |
| 28 | Procesos Fargate por perfil | Tabla breve + dato común | 19 | Columna constante trasladada a texto común; valor conservado. |
| 29 | Proyección y crecimiento de capacidad | Tabla breve + punteos | 20 | Comparación numérica; explicación o citas fuera de las celdas. |
| 30 | Umbrales de respuesta en percentil 95 | Tabla breve + punteos | 21 | Comparación numérica; explicación o citas fuera de las celdas. |
| 31 | Pruebas que confirman el dimensionamiento | Conservar tabla breve | 22 | Comparación breve con datos o decisiones en varias dimensiones. |
| 32 | Síntesis de las dieciséis dimensiones | Anexo 4-W | A.30 | Inventario o síntesis extensa; conservar matriz y valores en la memoria. |
| 33 | Carga eléctrica de TI proyectada del recinto | Conservar tabla breve | 23 | Comparación breve con datos o decisiones en varias dimensiones. |
| 34 | Carga térmica sensible proyectada del recinto | Conservar tabla breve | 24 | Comparación breve con datos o decisiones en varias dimensiones. |
| 35 | Destinos de recuperación: distancia y amenazas comunes | Conservar tabla breve | 25 | Comparación breve con datos o decisiones en varias dimensiones. |
| 36 | Replicación y RPO por dominio de datos | Punteos | Listado en el mismo apartado | Explica procesos, reglas o respuesta ante fallas; no requiere cuadrícula. |
| 37 | Objetivos de continuidad | Conservar tabla breve | 26 | Comparación breve con datos o decisiones en varias dimensiones. |
| 38 | Secuencia de conmutación de región | Punteos | Listado en el mismo apartado | Explica procesos, reglas o respuesta ante fallas; no requiere cuadrícula. |
| 39 | Uso de IA en el Subdocumento 4 | Tabla obligatoria | 27 | La sección 7.2 exige la tabla final con seis columnas y todas las filas. |

## Verificación y límites

Cotejo secuencial: cero diferencias de contenido entre Markdown y LaTeX en 1568 bloques del cuerpo, 1050 de anexos y 110 de T-11; 343 enlaces internos válidos. Se conservan las 27 figuras y el diagrama aprobado, SHA256 912bf7b551a9bd005b9e8f00b39d265faa7ff34221b6934f33cf4ee33b841aac. Se mantiene una única copia de cada matriz trasladada y se conservan los valores, plazos y condiciones de sus celdas.

Compilación LuaLaTeX: cuerpo 183 páginas, anexos 99, T-11 46. Sin referencias indefinidas, caracteres faltantes ni cajas desbordadas. La comprobación de continuidad detecta exclusivamente la declaración obligatoria (Tabla 27) en varias páginas. La revisión visual cubre las tablas técnicas conservadas, los punteos principales, las matrices trasladadas y el formato final de IA.

Esta es una verificación editorial, de referencias y maquetación; no demuestra ejecución de pruebas de carga, aprobación del CLIENTE ni revisión humana del equipo. Esas dependencias previas permanecen en su estado real. Fuentes y derivados PDF permanecen en el checkout LaTeX; la rama Markdown conserva únicamente sus tres consolidados en 04_arquitectura.
