# LafroX — formato del Subdocumento 11

Rama local: `LafroX-Subdoc11-LateX-CORRIGIENDO`. La plantilla conserva el formato corporativo y únicamente los títulos obligatorios del comunicado, por instrucción del usuario. No se adelantan subtítulos de tercer nivel ni se deja un esquema provisional de ellos.

## Índice del capítulo

- 11 Introducción a los Planes en operación.
- 11.1 Plan Mantención Preventiva / Evolutiva.
- 11.2 Plan Servicios de Operación.
- Referencias (sin numerar).
- Declaración de uso de IA (sin numerar).

El índice general y la lista de tablas se actualizan automáticamente. La tabla de IA contiene solo las filas 11, 11.1 y 11.2, con revisión humana sin atribuir. No hay anexos ni formularios adicionales asignados a SD11 en el correo.

## Archivos de desarrollo

- `LAFROX-Subdocumento11.tex`: raíz y metadatos.
- `sd11-formato.tex`: firmas, pies, índices y cierres.
- `subdocumento-11/contenido.tex`: introducción y montaje.
- `subdocumento-11/partes/11_1_mantencion.tex`: desarrollo de 11.1.
- `subdocumento-11/partes/11_2_operacion.tex`: desarrollo de 11.2.
- `subdocumento-11/partes/referencias.tex`: fuentes.
- `subdocumento-11/partes/declaracion-ia.tex`: declaración.
- `subdocumento-11/tablas/declaracion-ia.tex`: tabla de IA.

Se mantienen los textos de caída de los apartados obligatorios. El contenido técnico aún debe desarrollarse a partir de las Bases y de la solución; no se han inventado capacidades, SLA, mediciones ni aprobaciones.

## Presentación

Portada común de los capítulos corregidos, adaptada a SD11 y Caso 02. Firma completa en portada; únicamente el folio en su extremo inferior derecho. Las páginas interiores conservan media firma y folio. Papel carta vertical, cuerpo 11 pt y tabla 9,5 pt, con tipografías y márgenes corporativos. Referencias y Declaración de uso de IA son secciones sin numerar.

La imagen de firma es el activo existente de SD12, incorporado por petición del usuario; su presencia no acredita una aprobación nueva. Las notas de revisión no forman parte del PDF.

## Compilación

Ejecutar LuaLaTeX sobre `LAFROX-Subdocumento11.tex` hasta estabilizar índices y referencias. PDF canónico: `LAFROX-Subdocumento11.pdf`.

El ejemplo genérico heredado está fuera de la compilación.
