# Revisión de los puntos amplios del Subdocumento 3

Fuentes contrastadas: SD2 `LafroX-Subdoc2-LateX-CORRIGIENDO` (`a72407bc`), SD4 `LafroX-Subdoc4-LateX-corrigiendo` (`82ef4a20`), T-14 en SD7 `LafroX-Subdoc7-LateX-CORRIGIENDO` (`ec054cfb`), SD9 `LafroX-Subdoc9-LateX-corrigiendo` (`7483619d`) y el T-12 de la rama de trabajo. Los identificadores de las ramas son las referencias remotas disponibles en la revisión; esta comprobación no acredita ejecución de pruebas.

## SD3-05 — Prioridades

El recuento de los seis catálogos con prioridad propia produce 58 críticas, 157 altas y 55 medias: 270 requisitos. La Tabla 3.A.2 se cotejó con los techos de las 14 familias del SD2: no aparece ningún RF del caso cuya prioridad exceda los techos de todas sus familias asociadas. No se detectaron RF derivados de BTT con prioridad crítica. La comprobación no determina automáticamente la familia principal cuando hay varias; se examinaron los siete casos múltiples (RF-02.01, RF-02.06, RF-04.08, RF-06.11, RF-08.07, RF-12.13 y RF-14.04), sin cambio de prioridad propuesto. Las prioridades identificables del T-13 coinciden. No se reducen cifras para alcanzar una proporción predeterminada.

## SD3-01 — Figuras

La Figura 3.4 pasa a una vista editable de cuatro bloques; la 3.2 incorpora los datos por etapa del recorrido del lote y la consulta de trazabilidad. La nueva Figura 3.9 muestra los cuatro dominios de emplazamiento, con los límites del enlace y de la emisión tributaria, siguiendo SD4 4.2.2 y Anexo 4-N. Son síntesis: las tablas y diagramas de detalle mantienen la asignación individual y los permisos. Las figuras son propuestas de diseño documental y requieren revisión humana.

## SD3-06 — Componentes del T-12

Se simplificaron cinco patrones de pila repetidos en 40 filas funcionales, conservando módulo o servicio, comportamiento particular y referencias a SD4 y T-11. La introducción indica dónde se conserva la identificación detallada de productos y versiones. Los demás patrones y filas no quedan certificados por esta sustitución: hace falta completar la revisión semántica de la columna entera, especialmente los requisitos transversales donde el nombre o la versión son parte de la acreditación.

## SD3-04 — Cadena T-12 / T-13

El T-12 contiene 653 filas identificadas; la matriz T-13 contiene 644 fichas individuales y una tabla separada con los nueve alias (RF-19.01 a RF-19.05, RNF-06.02, RNF-06.03, RNF-11.03 y RNF-11.04). Para las 644 fichas, una comparación mecánica encontró correspondencia de identificadores, estados y paquetes EDT; también detectó `/Pnn` para las filas ofertadas y cero casos adicionales para los 22 «No cumple». Esta comprobación no determina si un escenario demuestra el criterio, si el paquete existe o si el origen corresponde semánticamente.

Una búsqueda textual adicional encontró todos los números de paquete citados por el T-12 en los archivos del T-14 de SD7. La aparición de una cifra en ese formulario no demuestra por sí sola que sea un paquete aplicable ni que su alcance cubra la exigencia; esa comprobación individual sigue pendiente.

La tabla de alias del T-13 no explicita el identificador absorbente para RF-19.01 a RF-19.05. El T-12 ahora declara respectivamente RT-11.03, RT-11.05, RT-11.13, RT-11.18 y RT-11.19, conforme al Anexo 3.A.3a. Los otros cuatro se remiten a sus filas absorbentes o al plazo del Caso y el protocolo indicados en el Anexo 3.A.5a. Debe reflejarse esa correspondencia en SD9.

El T-13 declara que se generó desde SD3 `3d0eeea7`. Las 40 simplificaciones del T-12 y las dos correcciones previas de origen de RF-09.09 y RF-12.10 no están reflejadas literalmente en esa instantánea. RNF-23.01, RNF-23.02 y RT-08.11 usan en T-13 una síntesis con remisión al T-12, no una copia literal. Se requiere regenerar o conciliar la matriz en la rama corregida de SD9 y revisar sus referencias de fuente, pruebas y criterios contra la versión final del SD3. No se modifica esa otra rama desde este trabajo.

Las fichas `/Pnn` son previstas; el T-13 indica que datos, pasos, ambiente y actas se completan en H1. En particular, RT-16.14 reúne el motor de reglas de BTT y la prueba de entrega del Caso bajo una misma fila: el protocolo debe demostrar ambas exigencias diferenciadas. La revisión semántica individual de los 644 criterios y de su correspondencia con pruebas y paquetes reales sigue pendiente; no debe declararse cerrada por el recuento de filas.
