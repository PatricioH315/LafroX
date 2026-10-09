# Limpieza editorial de 4.1 y secuencias

Se aplica el plan autorizado el 9 de octubre de 2026 sobre la rama local `subdoc-4`.

- El cuerpo utiliza nombres funcionales para las rutas de servicios, campos de correlación, perfil local de bodega, integración con ERP y agente de transferencia. El Anexo 4-G conserva rutas y campos exactos; el 4-P, las equivalencias de componentes y herramientas.
- Se conserva la identificación de módulos, requisitos, interfaces, decisiones, eventos canónicos y productos. La simplificación no renombra contratos ni altera las responsabilidades del sistema.
- Se aclaran las referencias al catálogo de interfaces, se eliminan frases repetidas y se describe la implantación Laravel como parte de la propuesta. La comparación con Django permanece en la justificación de alternativas.
- El inventario extenso de AWS se traslada al Anexo 4-P; el cuerpo mantiene la función y justificación de las tecnologías por capa.
- Las figuras 8 y 9 conservan sus participantes, nueve pasos, flechas y geometría. Las etiquetas expresan acciones breves; la explicación posterior conserva deduplicación, conexión iniciada por el sitio, registro transaccional de retención y auditoría, y publicación del evento tras el acuse durable.
- La figura 9 distingue captura sin señal y recuperación de conexión, y mantiene la regla de conservar los eventos hasta recibir confirmación.

El respaldo previo de los fuentes del cuerpo está en `tmp/antes-limpieza-editorial-20261009`, fuera del repositorio. La revisión comprueba referencias automáticas, ausencia de rutas técnicas en el cuerpo y etiquetas de las secuencias, conservación de identificadores trazables y tamaño de letra en el compilado. Las referencias manuales a 4.2.2 y 4.3.2 conservan sus destinos; las referencias a otros subdocumentos no se declaran validadas contra versiones remotas nuevas.

No se alteran fuentes de arquitectura física, centros de datos, formularios ni la rama Markdown. El general y las ocho vistas por capa se conservan. No se realiza commit ni push. El mínimo de 9 puntos comprobado corresponde a las figuras complementarias y no acredita el conjunto de figuras anteriores.
