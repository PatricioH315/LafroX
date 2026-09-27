# Subdocumento 4.1: arquitectura lógica

El documento LaTeX vigente describe el monolito modular Laravel 13 / PHP 8.5. Los anexos 4.1-A a 4.1-L se entregan en un archivo independiente y se citan desde el cuerpo del apartado.

## Abrir y compilar

- Abre la raíz del repositorio como proyecto de VS Code y usa `main.tex` para el subdocumento. Compila desde esa raíz con `lualatex --interaction=nonstopmode --halt-on-error main.tex` dos veces. El resultado es `main.pdf`.
- Abre `04_arquitectura/entrega_2/latex/anexos_4.1.tex` como documento independiente. Desde su propia carpeta, ejecuta `lualatex --interaction=nonstopmode --halt-on-error anexos_4.1.tex` dos veces. El resultado queda al lado del fuente como `anexos_4.1.pdf`.
- La ruta de búsqueda de `lafrox.cls` admite ambas formas de compilación. La segunda pasada resuelve el índice, el folio final y las referencias de las tablas.

## Diagramas generales

- La Figura 4.1 presenta primero la vista completa de Tomás: `Diagramas/arquitectura_logica_actual/cambios laravel/ARQL-01_Vision_general.png`.
- La Figura 4.2 presenta después la síntesis `Diagramas/arquitectura_logica_actual/ARQL-19_Vista_general_legible.pdf`. Su fuente editable es el archivo `.dot` del mismo nombre. Las dos figuras se complementan y se muestran en páginas independientes.
- La lámina detallada `ARQL-20_Arquitectura_logica_Laravel.pdf` muestra actores, M1–M12, integración, datos, seguridad y observabilidad. Se conserva también en SVG y PNG; su fuente editable es `ARQL-20_Arquitectura_logica_Laravel.dot`.

## Consistencia pendiente de consolidación

Se incorporó el commit `b08b623` de `tomas-ajustes-logica`, con las catorce láminas y el TXT de `Diagramas/arquitectura_logica_actual/cambios laravel/`, además de `capas/04_negocio.png`. `LECTURA_DIAGRAMAS.md`, en esa carpeta, contiene las descripciones precisadas por actor y las diferencias visuales pendientes (TTL del IdP, acceso local HHT y etiqueta residual). Las figuras ARQL-19 y ARQL-20 se conservan: los originales importados no sustituyen automáticamente esas vistas consolidadas.

El apartado «Patrones de diseño y continuidad» vincula expresamente el diseño con RT-10.03 (ISO 22301) y RT-10.04 (ISO/IEC 27031), delimita las responsabilidades del Subdocumento 11 y especifica evidencia de aceptación sin afirmar certificación.

El archivo `../texto/arquitectura_logica.md` todavía contiene referencias a Django, Python y Celery. No representa la versión Laravel del `subdoc_4.1.tex` hasta que se armonice expresamente. La adaptación de la arquitectura física 4.2 es un trabajo separado.
