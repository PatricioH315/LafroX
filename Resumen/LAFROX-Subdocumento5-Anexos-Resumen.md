# LafroX — Resumen de los anexos del Subdocumento 5

[Índice de resúmenes](README.md) · [Documento original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md)

## Para qué sirve

Los anexos 5-A–5-C definen rango/ficha térmica versionados, reglas preventivas sin aprobador y distribución local con acuse. El catálogo común CORREO/SMS/WHATSAPP/AVISO_EN_PORTAL se aplica a plantillas, preferencias e intentos; la baja se identifica por cliente, finalidad, categoría y canal. La retención conserva la decisión mientras el cliente pueda ser destinatario, sin habilitar publicidad por borrar registros.

Esta guía explica los 13 anexos del capítulo 5 por separado. Permite elegir el listado, protocolo o cálculo que se necesita sin recorrer todas sus tablas. Los identificadores conservan la nomenclatura del original.

## Anexo 5-A. Diccionario de datos atributo por atributo

Diccionario completo de 111 entidades y 791 atributos: tipo, dominio, obligatoriedad, dueño y sensibilidad. Explica qué significa cada dato y cuándo puede estar ausente legítimamente. Las abreviaturas de dominio y controles complementan las vistas del cuerpo; no sustituyen las restricciones de integridad.

**Cuándo consultarlo:** para implementar campos, interpretar columnas o verificar que una captura tiene significado y dueño.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-a-diccionario-de-datos-atributo-por-atributo)

## Anexo 5-B. Cardinalidades exactas, módulo y integridad referencial

Precisa relaciones, motores, módulos y autoridad de escritura. Las referencias entre almacenes se distinguen de claves físicas; ruta es central y bodega conserva autoridad local. Ante partición de red se mantiene consistencia dentro del perímetro autorizado, sin dos escritores concurrentes del mismo agregado.

**Cuándo consultarlo:** para revisar relaciones o decidir dónde puede confirmarse una modificación.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-b-cardinalidades-exactas-m%C3%B3dulo-y-integridad-referencial)

## Anexo 5-C. Dominios de valores, reglas de validación y causas de rechazo

Declara formatos, valores y rechazos de captura/integración. Valida identificadores de producto, lotes, unidades y estados, preservando nulos legítimos. Las excepciones quedan aisladas con contexto; no se crea un lote ficticio para llenar un campo. También desarrolla contratos de eventos y sus reglas.

**Cuándo consultarlo:** para reglas de validación, mensajes de rechazo o saneamiento del legado.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-c-dominios-de-valores-reglas-de-validaci%C3%B3n-y-causas-de-rechazo)

## Anexo 5-D. Retención por dominio y por atributo

Fija retención por dominio/atributo y copia: documentos/POD seis años, térmico detallado cinco, posición personal doce meses y auditoría siete. Los registros interpretativos permanecen con sus expedientes. La purga considera versiones, réplicas y conservación legal; estar en almacenamiento de objetos no determina por sí solo un plazo.

**Cuándo consultarlo:** antes de archivar, replicar o eliminar datos.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-d-retenci%C3%B3n-por-dominio-y-por-atributo)

## Anexo 5-E. Clasificación por sensibilidad y controles declarados

Asigna sensibilidad y controles de almacén, campo y acceso. Distingue cifrado en reposo de protección específica de columnas, y declara excepciones justificadas. GPS requiere protección de campo; documentos se consultan por roles. El acceso queda registrado y las decisiones de protección son verificables.

**Cuándo consultarlo:** para diseñar acceso y cifrado o revisar exposición de información personal.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-e-clasificaci%C3%B3n-por-sensibilidad-y-controles-declarados)

## Anexo 5-F. Índices, columnas y particionado

Define índices, orden de columnas, unicidad y particionado. Preserva coherencia de producto/lote y grano de saldos; las tablas particionadas deben conservar claves compatibles con sus referencias. Evita anunciar una unicidad global que el esquema físico no puede imponer.

**Cuándo consultarlo:** al construir consultas críticas, restricciones o mantenimiento por períodos.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-f-%C3%ADndices-columnas-y-particionado)

## Anexo 5-G. Claves de caché, vigencia e invalidación

Explica claves de caché, vigencia e invalidación. Redis se reconstruye desde la autoridad; permisos y manifiestos firmados tienen plazos diferentes. Un manifiesto de 26 h no extiende credenciales de 8 h en bodega o 14 h en terreno. La lectura desconectada permanece fechada o indicativa.

**Cuándo consultarlo:** para entender por qué una copia local puede leerse sin autorizar una nueva transacción.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-g-claves-de-cach%C3%A9-vigencia-e-invalidaci%C3%B3n)

## Anexo 5-H. Fórmulas de indicador, linaje documental y catálogo por fase

Define indicadores, granularidad, linaje, audiencia y latencia. OTIF usa la promesa ORIGINAL e incluye pedidos no entregados; cantidades se homologan y los casos sin base se declaran. La fecha analítica procede del hecho de negocio, no del día de carga. Costo de servir empieza en E2.

**Cuándo consultarlo:** para fórmulas, tableros y conciliación entre un indicador y sus documentos de origen.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-h-f%C3%B3rmulas-de-indicador-linaje-documental-y-cat%C3%A1logo-por-fase)

## Anexo 5-I. Matriz de trazabilidad de RT-05 con su evidencia

Relaciona RT-05 con sección y evidencia. RT-05.10 y RT-05.24 siguen como deseables no ofertados; RT-05.30 se atiende por INN-03. Las funciones técnicas del SD4 se remiten a sus contratos sin atribuirlas al diccionario. La matriz distingue contenido disponible de pruebas por ejecutar.

**Cuándo consultarlo:** para revisar cumplimiento de gestión de datos junto al T-12.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-i-matriz-de-trazabilidad-de-rt-05-con-su-evidencia)

## Anexo 5-J. Protocolo de aceptación de datos y pruebas propuestas

Propone pruebas de perfilado, conciliación, integridad, desempeño, exportación y recuperación. La carga normal es **12,34 TPS**, coherente con SD4, Anexo 4-W. El retiro en menos de dos horas contempla sedes y hechos pendientes, identificando exposición potencial. Su presupuesto de 85 min es una estimación de diseño; una lista parcial sin cubrir el universo no demuestra aceptación.

**Cuándo consultarlo:** para preparar ensayos y precisar qué evidencia debe producir cada uno.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-j-protocolo-de-aceptaci%C3%B3n-de-datos-y-pruebas-propuestas)

## Anexo 5-K. Resolución de observaciones de la instancia anterior

Responde observaciones previas con cambio documental, sección y evidencia. Incluye modelo/diccionario, autoridad, continuidad y otros aspectos del capítulo. El estado describe diseño documentado y pruebas programadas, sin convertir una respuesta escrita en validación técnica ya realizada.

**Cuándo consultarlo:** para seguir la resolución de observaciones y comprobar su evidencia.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-k-resoluci%C3%B3n-de-observaciones-de-la-instancia-anterior)

## Anexo 5-L. Mapeo, cálculo de olas y ventana de corte

Define migración por origen semántico, clave destino, transformación, rechazo, responsable y conciliación. Calcula olas y ventana de corte con deltas y reversión. Los nombres físicos reales del legado quedan sujetos al perfilado; el mapeo no finge conocer un esquema aún no inspeccionado.

**Cuándo consultarlo:** para planificar extracción, saneamiento, ensayos completos y autorización del corte.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-l-mapeo-c%C3%A1lculo-de-olas-y-ventana-de-corte)

## Anexo 5-M. Modelos lógicos complementarios

Complementa el modelo general con maestros/identidades, EDI/gobierno y telemetría/caché/objetos. Las vistas de inventario, preparación, reparto, custodia, documentos y analítica permanecen en el cuerpo. Las referencias complementan relaciones; el diccionario 5-A conserva todos los atributos.

**Cuándo consultarlo:** para visualizar dominios que no se desarrollan por completo en las figuras del cuerpo.

[Ver este anexo en el original](../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md#anexo-5-m-modelos-l%C3%B3gicos-complementarios)

## Lectura relacionada

El [resumen del Subdocumento 5](LAFROX-Subdocumento5-Resumen.md) explica las decisiones que estos anexos respaldan. Las matrices y protocolos describen compromisos y verificaciones previstas; una prueba solo se considera ejecutada cuando exista su evidencia.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
