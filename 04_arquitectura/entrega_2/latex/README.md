# Subdocumento 4.1: arquitectura lógica

El documento LaTeX y el Markdown lógico describen el monolito modular Laravel 13 / PHP 8.5. Los anexos 4.1-A a 4.1-N se entregan en un archivo independiente y se citan desde el cuerpo del apartado. G y H incluyen fichas de las quince interfaces; M define protocolos de aceptación y N la correspondencia lógica.

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

El archivo `../texto/arquitectura_logica.md` está sincronizado con el contenido lógico del LaTeX. Django solo se menciona como alternativa comparada, no como stack elegido. La adaptación de 4.2 es un trabajo separado.

## Estado del cierre de las ocho observaciones

- **Fuentes lógicas:** unificadas; no se modificaron fuentes físicas ni el capítulo 3.
- **Despacho y ERP:** control de estados y ensayo AL-DTE-01 definidos. No hay procedimiento tributario aprobado ni prueba de 96 salidas ejecutada.
- **RPO:** se retira la garantía incondicional sustentada solo en retención local. AL-BR-01 identifica la incompatibilidad del escenario de aislamiento total y pérdida de sitio; AL-DR-01 fija su medición. Registrar la brecha no equivale a enviar una consulta al mandante ni obtener dispensa.
- **Interfaces:** fichas INT-01–15 con modo, volumen, ventana requerida, timeout y respuesta. Los SLA externos y supuestos de carga todavía deben contrastarse con contratos y pruebas.
- **Autonomía:** AL-OFF-01 define corte 24 h, dos relevos, permisos, reinicio y reconciliación. No se presenta como ensayo aprobado.
- **Correspondencia:** Anexo N identifica 12/12 módulos y servicios transversales. Falta el inventario bidireccional del capítulo 3 y el 4.2 integrado; no se afirma cobertura total.
- **Figuras:** siguen abiertos el TTL del IdP, recorrido HHT y etiqueta residual de las láminas importadas, además de acreditar texto de al menos 9 pt impreso. Se conserva la vista de Tomás en primer lugar; no se simula su corrección mediante un cambio de descripción.
- **Entrega:** portada lógica identificada como Entrega 2 y declaración IA añadida. La revisión humana final no se ha realizado. Este fragmento no reemplaza el capítulo 4 integrado exigido para entrega.

`main.pdf` es salida de compilación local. La identificación `LAFROX-Subdocumento4.1.pdf` corresponde únicamente a la copia de trabajo del apartado. Para presentación, integrar 4.1–4.3 y usar `EMPRESA-Subdocumento4.pdf` y `EMPRESA-Subdocumento4-Anexos.pdf`, con la identidad definitiva del proponente y el Formulario A-6 consolidado. No presentar el fragmento 4.1 como si fuera el capítulo completo.
