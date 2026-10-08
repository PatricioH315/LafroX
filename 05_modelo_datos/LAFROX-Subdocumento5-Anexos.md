# LAFROX

# Subdocumento 5 — Anexos

**Modelo y gestión de datos**

| | |
| --- | --- |
| Proyecto | TFEP-01/2026 |
| PROPONENTE | LafroX SpA |
| REPRESENTANTE LEGAL | Alex Aravena |
| MANDANTE | Distribuidora Puelche S.A. |

El Subdocumento 5 remite a estos anexos por letra. Contienen diccionario, cardinalidades, dominios/validaciones, retención, sensibilidad, índices, cachés, indicadores, trazabilidad RT-05, protocolos, migración y modelos complementarios; el cuerpo concentra su análisis.

Cada anexo sigue la misma regla de redacción que el capítulo: el texto explica antes de mostrar la tabla, la tabla declara con el número de columnas mínimo que la información exige, y la fuente de cada dato se indica al pie. Ningún dato de estos anexos es una medición. Los valores proceden del dimensionamiento del Subdocumento 4, de los umbrales del capítulo 2 del Subdocumento 2, de los requisitos RT-05 y RT-09 de las Bases Técnicas Transversales (PUCV, 2026d) y del criterio de los casos.

## Índice de anexos

| Anexo | Contenido | Apartado del cuerpo que lo cita |
| --- | --- | --- |
| 5-A | Diccionario de datos atributo por atributo | 5.1.12 |
| 5-B | Cardinalidades exactas e integridad referencial | 5.1.6, 5.1.7 |
| 5-C | Dominios de valores, reglas de validación y causas de rechazo | 5.2.5, 5.3.3 |
| 5-D | Retención por dominio y por atributo | 5.2.7 |
| 5-E | Clasificación por sensibilidad y controles declarados | 5.2.7 |
| 5-F | Índices, columnas y particionado | 5.4.2, 5.4.3 |
| 5-G | Claves de caché e invalidación | 5.4.4 |
| 5-H | Fórmulas de indicador y su linaje | 5.1.6, 5.2.6 |
| 5-I | Matriz de trazabilidad de RT-05 con su evidencia | 5.1, 5.2, 5.3, 5.4 |
| 5-J | Protocolo de aceptación de datos y pruebas propuestas | 5.3.5, 5.4.6 |
| 5-K | Respuesta a la revisión del Informe 1 | 5.1–5.4 |
| 5-L | Mapeo y ventanas de migración | 5.3 |
| 5-M | Modelos lógicos complementarios | 5.1 |
| Referencias | Fuentes documentales | Todo el ítem |

## Lista de tablas de los anexos

Objetos presentes en este documento.

| Número | Contenido |
| --- | --- |
| Tabla A.1 | Leyenda de propietario funcional y de sensibilidad |
| Tabla A.2 | Diccionario de atributos: Entidades maestras e identidad compartida |
| Tabla A.3 | Diccionario de atributos: Recepción, inventario, lote y unidad logística |
| Tabla A.4 | Diccionario de atributos: Trazabilidad sanitaria y cadena de custodia |
| Tabla A.5 | Diccionario de atributos: Preventa, reserva y preparación |
| Tabla A.6 | Diccionario de atributos: Rutas, reparto, entrega, devolución y envases |
| Tabla A.7 | Diccionario de atributos: Cobranza, documentos,envases y objetos |
| Tabla A.8 | Diccionario de atributos: Intercambio electrónico, notificación y gobierno del acceso |
| Tabla A.9 | Diccionario de atributos: Telemetría, caché de lectura y objetos del dispositivo |
| Tabla A.10 | Diccionario de atributos: Modelo dimensional de explotación |
| Tabla A.11 | Módulo, almacén lógico y motor por dominio |
| Tabla A.12 | Dominios de valores cerrados y su validación |
| Tabla A.13 | Causas de rechazo y su tratamiento en operación y en migración |
| Tabla A.14 | Retención declarada por dominio y por atributo |
| Tabla A.15 | Clasificación por sensibilidad y control declarado |
| Tabla A.16 | Índices declarados, columnas, orden y ámbito de unicidad |
| Tabla A.17 | Particionamiento declarado y su relación con la retención |
| Tabla A.18 | Fórmulas exactas, granularidad y linaje documental |
| Tabla A.19 | Catálogo de indicadores por fase, audiencia, latencia y exportación |
| Tabla A.20 | Matriz de trazabilidad de RT-05 con evidencia comprobable |
| Tabla A.21 | Pruebas de aceptación de la migración con umbral numérico |
| Tabla A.22 | Pruebas de aceptación de desempeño con umbral numérico |
| Tabla A.23 | Pruebas de aceptación de trazabilidad, calidad, operación y seguridad |
| Tabla A.24 | Respuesta documental y límites de verificación |
| Tabla A.25 | Mapeo semántico y validación de migración |
| Tabla A.26 | Duración calculada por fase y ola inicial |
| Tabla A.27 | Ventana final, decisión y reserva de rollback |

---

<a id="anexo-5a"></a>

## Anexo 5-A. Diccionario de datos atributo por atributo

Las decisiones de este ítem aplican las Bases Administrativas (Pontificia Universidad Católica de Valparaíso [PUCV], 2026b, arts. 16, 17 y 85), las Bases Técnicas del Caso 02 (PUCV, 2026c, caps. 14–16 y 18) y las Bases Técnicas Transversales (PUCV, 2026d, §§5 y 9); su estructura y presentación siguen las Aclaraciones de licitación (PUCV, 2026a, §§2–6 y 11).

Los antecedentes de empresa, problema, alcance y arquitectura proceden de los Subdocumentos 1, 2, 3 y 4, respectivamente (LafroX SpA, 2026d, 2026c, 2026b, 2026a); sus remisiones señalan el apartado específico utilizado.

El diccionario 5-A contiene una fila por cada uno de los 791 atributos de 111 entidades del esquema lógico, dibujado entre el cuerpo y 5-M. Conserva nombre, significado, tipo, dominio, obligatoriedad, referencia, propietario y sensibilidad/política, conforme RT-05.01.

Las nueve tablas agrupan dominios sin resumir atributos. json representa jsonb en PostgreSQL y datetime timestamp UTC; cachés/documentos no son tablas SQL por aparecer en una vista ER. Las políticas P01 y siguientes evitan repetir retención/control por fila y se desarrollan en la leyenda posterior y 5-D/5-E.

Un obligatorio vacío se rechaza en captura; un derivado lo calcula su proceso. Propietario identifica el dominio dueño, no los consumidores: todos usan el mismo maestro compartido. Retención sigue a la entidad salvo excepción explícita por atributo.

<a id="tab-a1-leyenda"></a>

| Código | Significado | Dueño funcional | Sensibilidad y control exigido |
| :------- | ----------- | -------------------- | ------------------------------- |
| `MAE` | Maestros y configuración; dueño de clientes, proveedores, productos, unidades, sitios, vehículos y parámetros | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `ME` |
| `INV` | Recepción e inventario; dueño de lote, unidad logística, saldo, reserva y conteo | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `ME`, `CR` en la unidad con responsable |
| `CAL` | Calidad y trazabilidad; dueño de sensor, regla térmica, calibración, lectura y custodia | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `ME`, `CR` en el actor del evento |
| `PRE` | Preventa; dueño de tarifa, pedido, línea, promesa y asignación | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `ME`, `AL` en importe y crédito |
| `PREP` | Preparación; dueño de misión y confirmación de picking | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `ME` |
| `RUT` | Rutas; dueño de ruta, viaje, parada y geocerca | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `CR` en la posición y en el conductor |
| `REP` | Reparto y devolución; dueño de entrega, intento, causal, devolución y cuenta de envases | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `ME`, `CR` en el receptor |
| `COB` | Cobranza y finanzas; dueño de saldo, cobro, pos, compensación, rendición, cuadratura y descuadre | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `AL` |
| `DOC` | Documentos y objetos; dueño de documento, referencia, POD, acuse técnico y objeto almacenado | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `AL` en el documento, `ME` en el envoltorio |
| `EDI` | Intercambio electrónico; dueño de perfil de cadena, mensaje, equivalencia y ASN | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `ME` |
| `NOT` | Notificaciones; dueño de plantilla, preferencia, aviso e intento de envío | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `CR` en el contacto del destinatario |
| `TEL` | Telemetría; dueño de lectura cruda, archivo, serie consolidada y posición | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `ME`, `CR` en la posición |
| `GOB` | Gobierno y acceso; dueño de actor, asignación, auditoría y excepción de sincronización | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `AL` en la auditoría |
| `DER` | Proyección derivada; su autoridad es la entidad de origen y ningún proceso escribe salvo el que la publica | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `ME` |
| `ANA` | Explotación; dueño de dimensión y hecho, alimentados desde la fuente transaccional | Responsable funcional del dominio en el CLIENTE; LafroX administra técnicamente | `AL` cuando el atributo es un importe |
| `AL` | Datos de alta sensibilidad: condicion financiera, importe, saldo, documento e identidad tributaria | No aplica: código de sensibilidad | Cifrado a nivel de campo o de servidor, mínimo privilegio y consulta auditada |
| `CR` | Datos críticos o identificadores que permiten reconstruir quién es la persona o dónde está | No aplica: código de sensibilidad | Cifrado a nivel de campo, acceso reforzado y consulta auditada |
| `ME` | Datos de sensibilidad media: medidas de operación, catálogos, estados y referencias técnicas | No aplica: código de sensibilidad | Acceso por rol y cifrado en reposo del almacén |

**Tabla A.1 — Leyenda de propietario funcional y de sensibilidad**

*Fuente: elaboración propia de LafroX a partir de los quince nombres lógicos de persistencia de S4, de RT-05.01 y RT-16 de las Bases Técnicas Transversales (PUCV, 2026d) y de la regla de propietario funcional del Anexo 5-B.*
<a id="tab-a2-dic-maestros"></a>

La Tabla A.2 desarrolla los atributos de maestros e identidades, con sus condiciones y políticas de conservación.

| Entidad | Atributo | Significado | Tipo lógico, tamaño y precisión | Dominio, formato, catálogo o rango | Obligatoriedad y condición | Clave, referencia y unicidad | Propietario funcional | Sensibilidad, retención y control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `mae_cliente` | `cliente_id` | clave interna | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `ME`; `P01` |
| `mae_cliente` | `rut` | RUT normalizado | string(12), RUT sin puntos | RUT chileno de representación de RUT con dígito verificador numérico o K sin puntos ni guiones, con dígito verificador válido | Obligatorio | Valor único | `MAE` | `CR`; `P02` |
| `mae_cliente` | `razon_social` | Razón Social | string(255) | Razón social del interviniente con la grafía del documento oficial | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_cliente` | `canal` | Canal | string(32), catálogo | Catálogo: TRADICIONAL, MODERNO, FOOD_SERVICE, CADENA, HORECA | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_cliente` | `condicion_credito` | Condicion Credito | string(32), catálogo | Catálogo: CREDITO, CONTADO, PREPAGO | Obligatorio | Sin clave | `MAE` | `AL`; `P03` |
| `mae_cliente_punto` | `cliente_punto_id` | Identificador de cliente punto | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `ME`; `P01` |
| `mae_cliente_punto` | `cliente_id` | Identificador de cliente | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_cliente.cliente_id`; integridad según 5-B | `MAE` | `ME`; `P01` |
| `mae_cliente_punto` | `sitio_id` | instalacion que atiende | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_sitio.sitio_id`; integridad según 5-B | `MAE` | `ME`; `P01` |
| `mae_cliente_punto` | `codigo_punto` | identificador del punto de entrega | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_cliente_punto` | `tipo_punto` | Tipo Punto | string(32), catálogo | Catálogo: BODEGA, LOCAL, CENTRO, CANAL | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_cliente_punto` | `activo` | Activo | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `MAE` | `ME`; `P01` |
| `mae_proveedor` | `proveedor_id` | Identificador de proveedor | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `ME`; `P01` |
| `mae_proveedor` | `rut` | Rut | string(12), RUT sin puntos | RUT chileno de representación de RUT con dígito verificador numérico o K sin puntos ni guiones, con dígito verificador válido | Obligatorio | Valor único | `MAE` | `CR`; `P02` |
| `mae_proveedor` | `gln` | Gln | string(13), GLN GS1 | GLN de 13 dígitos | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_proveedor` | `razon_social` | Razón Social | string(255) | Razón social del interviniente con la grafía del documento oficial | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_producto` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `ME`; `P01` |
| `mae_producto` | `gtin` | GTIN canónico del producto; único cuando aplica | string(14), GTIN GS1 | GTIN de 8, 12, 13 o 14 dígitos con dígito verificador válido | Obligatorio | Único para GTIN canónico no nulo; equivalencias alternas controladas | `MAE` | `ME`; `P01` |
| `mae_producto` | `descripcion` | Descripción | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_producto` | `requiere_lote` | obligatoriedad del lote segun producto | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `MAE` | `ME`; `P01` |
| `mae_producto` | `vida_util_dias` | atributo de calculo, no parte de la identidad | integer, 32 bits | Entero dentro del rango del tipo; negativo solo en una diferencia o un descuadre declarado | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_unidad` | `unidad_id` | Identificador de unidad | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `ME`; `P01` |
| `mae_unidad` | `codigo` | Código | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Valor único | `MAE` | `ME`; `P01` |
| `mae_unidad` | `descripcion` | Descripción | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_conversion` | `conversion_id` | Identificador de conversion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `ME`; `P01` |
| `mae_conversion` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `MAE` | `ME`; `P01` |
| `mae_conversion` | `unidad_origen` | Unidad Origen | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_unidad.unidad_id` | `MAE` | `ME`; `P01` |
| `mae_conversion` | `unidad_destino` | Unidad Destino | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_unidad.unidad_id` | `MAE` | `ME`; `P01` |
| `mae_conversion` | `factor` | factor de conversion vigente | decimal(18,6) | Mayor que cero, seis decimales, en la unidad de la regla que lo interpreta | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_conversion` | `vigente_desde` | Vigente Desde | date | Fecha ISO 8601 de inicio del intervalo; admite vigencias futuras; selección histórica según 5-C | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_conversion` | `vigente_hasta` | nulo mientras la version siga vigente | date | Fecha ISO 8601; nula mientras la versión siga vigente | Condicional: nula en la versión vigente y con fecha en las cerradas | Parte de la unicidad con la fecha de inicio de vigencia | `MAE` | `ME`; `P01` |
| `mae_sitio` | `sitio_id` | Identificador de sitio | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `ME`; `P01` |
| `mae_sitio` | `codigo` | Código | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Valor único | `MAE` | `ME`; `P01` |
| `mae_sitio` | `tipo` | Tipo | string(32), catálogo | CENTRO_DISTRIBUCION, CROSS_DOCKING, CASA_MATRIZ, INSTALACION_CLIENTE; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_sitio` | `region` | Region | string(255) | Valor del catálogo territorial aprobado del CLIENTE; hasta 255 caracteres; conservar código/versión de origen y validar equivalencia | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_sitio` | `zona_horaria` | Zona Horaria | string(255) | Identificador de zona horaria IANA del sitio, por ejemplo `America/Santiago` | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_ubicacion` | `ubicacion_id` | Identificador de ubicacion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `ME`; `P01` |
| `mae_ubicacion` | `gln` | Gln | string(13), GLN GS1 | GLN de 13 dígitos | Obligatorio | Valor único | `MAE` | `ME`; `P01` |
| `mae_ubicacion` | `sitio_id` | Identificador de sitio | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_sitio.sitio_id`; integridad según 5-B | `MAE` | `ME`; `P01` |
| `mae_ubicacion` | `gln_padre` | Gln Padre | string(13), GLN GS1 | GLN de 13 dígitos | Condicional: con la condición que declara el dominio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_equivalencia_cliente` | `equivalencia_id` | Identificador de equivalencia | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `AL`; `P03` |
| `mae_equivalencia_cliente` | `cliente_id` | Identificador de cliente | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_cliente.cliente_id`; integridad según 5-B | `MAE` | `ME`; `P01` |
| `mae_equivalencia_cliente` | `sistema` | Sistema | string(255) | Identidad del sistema externo habilitado en contratos S4; hasta 255 caracteres; no admite alta tácita | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_equivalencia_cliente` | `codigo_externo` | Código Externo | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_equivalencia_producto` | `equivalencia_id` | Identificador de equivalencia | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `AL`; `P03` |
| `mae_equivalencia_producto` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `MAE` | `ME`; `P01` |
| `mae_equivalencia_producto` | `sistema` | Sistema | string(32), catálogo | Catálogo: ERP, WMS, EDI, cadena | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_equivalencia_producto` | `codigo_externo` | puede ser un GTIN distinto del de referencia | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_equivalencia_proveedor` | `equivalencia_id` | Identificador de equivalencia | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `AL`; `P03` |
| `mae_equivalencia_proveedor` | `proveedor_id` | Identificador de proveedor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_proveedor.proveedor_id` | `MAE` | `ME`; `P01` |
| `mae_equivalencia_proveedor` | `sistema` | Sistema | string(255) | Identidad del sistema externo habilitado en contratos S4; hasta 255 caracteres; no admite alta tácita | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_equivalencia_proveedor` | `codigo_externo` | Código Externo | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_parametro` | `parametro_id` | Identificador de parametro | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `ME`; `P04` |
| `mae_parametro` | `clave` | identidad del parametro, no de su valor | string(255) | Clave única de la entrada dentro del mbito declarado por su entidad | Obligatorio | Valor único | `MAE` | `ME`; `P04` |
| `mae_parametro_version` | `version_id` | Identificador de version | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `ME`; `P04` |
| `mae_parametro_version` | `parametro_id` | Identificador de parametro | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_parametro.parametro_id` | `MAE` | `ME`; `P04` |
| `mae_parametro_version` | `version` | correlativo de la version | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Parte de la clave de la versión | `MAE` | `ME`; `P04` |
| `mae_parametro_version` | `valor` | Valor del parámetro en esta versión | jsonb | JSON con tipo_valor NUMERO, BOOLEANO, TEXTO, INTERVALO o LISTA y valor validado según 5-C. Ausencia o inaplicabilidad no equivalen a falso: se rechaza una versión sin valor interpretable | Obligatorio | Sin clave | `MAE` | `AL`; `P05` |
| `mae_parametro_version` | `vigente_desde` | Vigente Desde | date | Fecha ISO 8601 de inicio del intervalo; admite vigencias futuras; selección histórica según 5-C | Obligatorio | Sin clave | `MAE` | `ME`; `P04` |
| `mae_parametro_version` | `vigente_hasta` | nulo mientras la version siga vigente | date | Fecha ISO 8601; nula mientras la versión siga vigente | Condicional: nula en la versión vigente y con fecha en las cerradas | Parte de la unicidad con la fecha de inicio de vigencia | `MAE` | `ME`; `P04` |
| `mae_parametro_version` | `cambiado_por` | actor que propone el cambio | string(255) | Texto libre normalizado; actor que propone el cambio | Obligatorio | Sin clave | `MAE` | `ME`; `P04` |
| `mae_parametro_version` | `aprobado_por` | rol funcional que lo aprueba | string(255) | Texto libre normalizado; rol funcional que lo aprueba | Obligatorio | Sin clave | `MAE` | `ME`; `P04` |
| `mae_transportista` | `transportista_id` | Identificador de transportista | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `ME`; `P01` |
| `mae_transportista` | `rut` | Rut | string(12), RUT sin puntos | RUT chileno de representación de RUT con dígito verificador numérico o K sin puntos ni guiones, con dígito verificador válido | Obligatorio | Valor único | `MAE` | `CR`; `P02` |
| `mae_transportista` | `razon_social` | Razón Social | string(255) | Razón social del interviniente con la grafía del documento oficial | Obligatorio | Sin clave | `MAE` | `ME`; `P01` |
| `mae_vehiculo` | `vehiculo_id` | Identificador de vehiculo | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `MAE` | `ME`; `P01` |
| `mae_vehiculo` | `patente` | Patente | string(255) | Patente vigente en Chile, sin guiones ni caracteres especiales | Obligatorio | Valor único | `MAE` | `CR`; `P02` |
| `mae_vehiculo` | `transportista_id` | Identificador de transportista | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_transportista.transportista_id` | `MAE` | `ME`; `P01` |
| `mae_vehiculo` | `refrigerado` | Refrigerado | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `MAE` | `ME`; `P01` |
| `mae_actor` | `actor_id` | Identificador de actor | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `GOB` | `ME`; `P06` |
| `mae_actor` | `tipo` | Tipo | string(32), catálogo | Catálogo: PERSONA, USUARIO, DISPOSITIVO, INTEGRACION | Obligatorio | Sin clave | `GOB` | `ME`; `P06` |
| `mae_actor` | `identificacion` | Identificacion | string(255) | Identificador del actor: RUT, código de empleado o identificador entregado por el canal | Obligatorio | Sin clave | `GOB` | `CR`; `P07` |
| `mae_actor` | `transportista_id` | Transportista al que pertenece el actor | uuid, 128 bits | UUID del registro referenciado | Condicional: obligatorio cuando el actor ejecuta como transportista, ya sea en ruta o en reparto; nula para actores de la propia empresa, del sistema y de los roles de negocio que no pertenecen a un transportista | Clave foránea a `mae_transportista.transportista_id` | `GOB` | `ME`; `P06` |

**Tabla A.2 - Diccionario de atributos: Entidades maestras e identidad compartida**

*Fuente: elaboración propia de LafroX a partir del modelo lógico de la Figura A5.1 del Anexo 5-M, de RT-05.01 de las Bases Técnicas Transversales (PUCV, 2026d) y de la matriz de retención del Anexo 5-D.*

La validación aplica la condición de cada fila al hito indicado; NULL legítimo se distingue de dato obligatorio ausente.

<a id="tab-a3-dic-inventario"></a>

La Tabla A.3 desarrolla los atributos de recepción e inventario, con sus condiciones y políticas de conservación.

| Entidad | Atributo | Significado | Tipo lógico, tamaño y precisión | Dominio, formato, catálogo o rango | Obligatoriedad y condición | Clave, referencia y unicidad | Propietario funcional | Sensibilidad, retención y control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `inv_recepcion` | `recepcion_id` | Identificador de recepcion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `INV` | `ME`; `P08` |
| `inv_recepcion` | `sitio_id` | Identificador de sitio | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_sitio.sitio_id`; integridad según 5-B | `INV` | `ME`; `P08` |
| `inv_recepcion` | `proveedor_id` | Identificador de proveedor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_proveedor.proveedor_id` | `INV` | `ME`; `P08` |
| `inv_recepcion` | `documento_origen` | Documento Origen | string(32), catálogo | Texto libre normalizado, hasta 32 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_recepcion` | `fecha_recepcion` | Fecha Recepción | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_recepcion` | `estado` | Estado | string(32), catálogo | Catálogo: ABIERTA, RECIBIDA, ANULADA | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_recepcion_linea` | `linea_recepcion_id` | Identificador de linea recepcion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `INV` | `ME`; `P08` |
| `inv_recepcion_linea` | `recepcion_id` | Identificador de recepcion | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `inv_recepcion.recepcion_id` | `INV` | `ME`; `P08` |
| `inv_recepcion_linea` | `secuencia_documento` | ordinal de la línea en el documento de origen | integer, 32 bits | Entero positivo asignado por el documento de origen | Condicional: obligatorio cuando el documento de origen numera sus líneas; en documentos que agrupan o no enumeran, la identidad la da el contenido declarado y la repetición legítima no se prohíbe | Único con `recepcion_id` dentro del ámbito de la recepción | `INV` | `ME`; `P08` |
| `inv_recepcion_linea` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `INV` | `ME`; `P08` |
| `inv_recepcion_linea` | `lote_id` | obligatorio cuando el producto lo exige | uuid, 128 bits | UUID del registro referenciado | Obligatorio para producto con lote exigido; NULL si producto exento | Referencia a `inv_lote.lote_id`; integridad según 5-B | `INV` | `ME`; `P08` |
| `inv_recepcion_linea` | `cantidad` | Cantidad | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_recepcion_linea` | `unidad_id` | Identificador de unidad | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_unidad.unidad_id` | `INV` | `ME`; `P08` |
| `inv_recepcion_linea` | `vencimiento_recibido` | Vencimiento Recibido | date | Fecha ISO 8601 declarada por el proveedor; se conserva aunque el lote esté vencido, con control sanitario según 5-C | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_lote` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `INV` | `ME`; `P08` |
| `inv_lote` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `INV` | `ME`; `P08` |
| `inv_lote` | `numero_lote` | Numero Lote | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_lote` | `vencimiento` | Vencimiento | date | Fecha ISO 8601 declarada por el proveedor; se conserva aunque el lote esté vencido, con control sanitario según 5-C | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_lote` | `estado_calidad` | Estado Calidad | string(32), catálogo | PENDIENTE, APTO, BLOQUEADO, LIBERADO, RETIRADO; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_lote` | `gtin` | Gtin | string(14), GTIN GS1 | GTIN de 8, 12, 13 o 14 dígitos con dígito verificador válido | Obligatorio | UK con numero_lote; concordancia con GTIN canónico de producto_id | `INV` | `ME`; `P08` |
| `inv_unidad_logistica` | `unidad_logistica_id` | identificador interno | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `INV` | `ME`; `P08` |
| `inv_unidad_logistica` | `sscc_id` | SSCC estandarizado | string(18), SSCC GS1 | SSCC estandarizado de 18 dígitos, sin guiones | Obligatorio | Valor único | `INV` | `ME`; `P08` |
| `inv_unidad_logistica` | `estado` | Estado | string(32), catálogo | Catálogo: VACIA, ABIERTA, CERRADA, ENTREGADA | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_unidad_logistica` | `tipo` | Tipo | string(32), catálogo | PALLET, CAJA, CONTENEDOR; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_unidad_logistica` | `sitio_id` | Identificador de sitio | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_sitio.sitio_id`; integridad según 5-B | `INV` | `ME`; `P08` |
| `inv_unidad_logistica` | `recepcion_id` | Identificador de recepcion | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `inv_recepcion.recepcion_id` | `INV` | `ME`; `P08` |
| `inv_unidad_logistica` | `fecha_cierre` | nulo mientras la unidad siga vacia o abierta | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Condicional: obligatoria al cerrar la unidad; nula mientras siga vacía o abierta | Sin clave | `INV` | `ME`; `P08` |
| `inv_unidad_contenido` | `contenido_id` | Identificador de contenido | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `INV` | `ME`; `P08` |
| `inv_unidad_contenido` | `unidad_logistica_id` | Identificador de unidad logistica | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_unidad_logistica.unidad_logistica_id`; integridad según 5-B | `INV` | `ME`; `P08` |
| `inv_unidad_contenido` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID del registro referenciado | Obligatorio para producto con lote exigido; NULL si producto exento | Referencia a `inv_lote.lote_id`; integridad según 5-B | `INV` | `ME`; `P08` |
| `inv_unidad_contenido` | `cantidad` | Cantidad | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_unidad_contenido` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `INV` | `ME`; `P08` |
| `inv_unidad_contenido` | `unidad_id` | Identificador de unidad | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_unidad.unidad_id` | `INV` | `ME`; `P08` |
| `inv_saldo` | `saldo_id` | Identificador de saldo | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | PK global; no particionado; UK de grano en 5-F | `INV` | `AL`; `P09` |
| `inv_saldo` | `sitio_id` | Sitio que determina la autoridad del saldo | uuid, 128 bits | UUID de mae_sitio válido | Obligatorio; referencia válida | Referencia a mae_sitio.sitio_id; UK del grano en 5-F | `INV` | `ME`; `P10` |
| `inv_saldo` | `ubicacion_id` | Identificador de ubicacion | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_ubicacion.ubicacion_id` | `INV` | `ME`; `P10` |
| `inv_saldo` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID del registro referenciado | Obligatorio para producto con lote exigido; NULL si producto exento | Referencia a `inv_lote.lote_id`; integridad según 5-B | `INV` | `ME`; `P10` |
| `inv_saldo` | `unidad_id` | Identificador de unidad | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_unidad.unidad_id` | `INV` | `ME`; `P10` |
| `inv_saldo` | `cantidad` | Cantidad | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `INV` | `ME`; `P10` |
| `inv_saldo` | `cantidad_reservada` | Cantidad Reservada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio, admite cero; no puede superar la cantidad de referencia | Sin clave | `INV` | `ME`; `P10` |
| `inv_saldo` | `estado` | Estado | string(32), catálogo | Catálogo: DISPONIBLE, BLOQUEADO, CERRADO | Obligatorio | Sin clave | `INV` | `ME`; `P10` |
| `inv_movimiento` | `movimiento_id` | Identificador de movimiento | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `INV` | `ME`; `P08` |
| `inv_movimiento` | `tipo` | Tipo | string(32), catálogo | Catálogo: RECEPCION, SALIDA, TRASLADO, AJUSTE, ANULACION | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_movimiento` | `sitio_origen_id` | Sitio de origen del movimiento | uuid, 128 bits | UUID del registro referenciado | Condicional: obligatorio en TRASLADO, AJUSTE y ANULACION; en RECEPCION el origen es el proveedor y no hay sitio; SALIDA exige el sitio de origen | Clave foránea a `mae_sitio.sitio_id` | `INV` | `ME`; `P08` |
| `inv_movimiento` | `saldo_origen_id` | Saldo que se descuenta | uuid, 128 bits | UUID del registro referenciado | Condicional según dirección, ajuste con signo y reversión del original; reglas exactas en 5-C | Clave foránea a `inv_saldo.saldo_id` | `INV` | `AL`; `P11` |
| `inv_movimiento` | `sitio_destino_id` | Sitio de destino del movimiento | uuid, 128 bits | UUID del registro referenciado | Condicional: obligatorio en TRASLADO, RECEPCION y AJUSTE; en SALIDA y ANULACION no hay sitio de destino porque el consumo y la anulación no reatribuyen mercadería a otra ubicación | Clave foránea a `mae_sitio.sitio_id` | `INV` | `ME`; `P08` |
| `inv_movimiento` | `saldo_destino_id` | Saldo que se acredita | uuid, 128 bits | UUID del registro referenciado | Condicional según dirección, ajuste con signo y reversión del original; reglas exactas en 5-C | Clave foránea a `inv_saldo.saldo_id` | `INV` | `AL`; `P11` |
| `inv_movimiento` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID del registro referenciado | Obligatorio para producto con lote exigido; NULL si producto exento | Referencia a `inv_lote.lote_id`; integridad según 5-B | `INV` | `ME`; `P08` |
| `inv_movimiento` | `unidad_logistica_id` | Identificador de unidad logistica | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_unidad_logistica.unidad_logistica_id`; integridad según 5-B | `INV` | `ME`; `P08` |
| `inv_movimiento` | `cantidad` | Cantidad | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_movimiento` | `documento_origen_tipo` | Documento Origen Tipo | string(32), catálogo | RECEPCION, PREPARACION, ENTREGA, DEVOLUCION, CONTEO, MOVIMIENTO; catálogo tipado de origen. ANULACION exige MOVIMIENTO | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_movimiento` | `documento_origen_id` | Identificador de documento origen | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia tipada según documento_origen_tipo; ANULACION remite a inv_movimiento.movimiento_id original. FK solo co-residente | `INV` | `ME`; `P08` |
| `inv_movimiento` | `fecha_ocurrencia` | Fecha Ocurrencia | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_movimiento` | `fecha_registro` | Fecha Registro | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `INV` | `ME`; `P08` |
| `inv_reserva` | `reserva_id` | Identificador de reserva | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `INV` | `ME`; `P12` |
| `inv_reserva` | `pedido_id` | Identificador de pedido | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `prv_pedido.pedido_id`; integridad según 5-B | `INV` | `ME`; `P12` |
| `inv_reserva` | `sitio_id` | Identificador de sitio | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_sitio.sitio_id`; integridad según 5-B | `INV` | `ME`; `P12` |
| `inv_reserva` | `estado` | Estado | string(32), catálogo | Catálogo: PROPUESTA, CONFIRMADA, LIBERADA, CANCELADA | Obligatorio | Sin clave | `INV` | `ME`; `P12` |
| `inv_reserva_linea` | `reserva_linea_id` | Identificador de reserva linea | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `INV` | `ME`; `P12` |
| `inv_reserva_linea` | `reserva_id` | Identificador de reserva | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `inv_reserva.reserva_id` | `INV` | `ME`; `P12` |
| `inv_reserva_linea` | `pedido_linea_id` | Identificador de pedido linea | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `prv_pedido_linea.linea_id`; FK física solo si comparte almacén, en otro caso contrato de integridad | `INV` | `ME`; `P12` |
| `inv_reserva_linea` | `saldo_id` | Identificador de saldo | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `inv_saldo.saldo_id` | `INV` | `AL`; `P13` |
| `inv_reserva_linea` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID del registro referenciado | Obligatorio para producto con lote exigido; NULL si producto exento | Referencia a `inv_lote.lote_id`; integridad según 5-B | `INV` | `ME`; `P12` |
| `inv_reserva_linea` | `cantidad_reservada` | Cantidad Reservada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio, admite cero; no puede superar la cantidad de referencia | Sin clave | `INV` | `ME`; `P12` |
| `inv_reserva_linea` | `cantidad_preparada` | Cantidad Preparada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `INV` | `ME`; `P12` |
| `inv_reserva_linea` | `fecha_reserva` | Fecha Reserva | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `INV` | `ME`; `P12` |
| `inv_conteo` | `conteo_id` | Identificador de conteo | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `INV` | `ME`; `P12` |
| `inv_conteo` | `sitio_id` | Identificador de sitio | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_sitio.sitio_id`; integridad según 5-B | `INV` | `ME`; `P12` |
| `inv_conteo` | `ubicacion_id` | Identificador de ubicacion | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_ubicacion.ubicacion_id` | `INV` | `ME`; `P12` |
| `inv_conteo` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `INV` | `ME`; `P12` |
| `inv_conteo` | `estado` | Estado | string(32), catálogo | Catálogo: ABIERTO, CONTABILIZADO, REVERSADO | Obligatorio | Sin clave | `INV` | `ME`; `P12` |
| `inv_conteo_detalle` | `detalle_id` | Identificador de detalle | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `INV` | `ME`; `P12` |
| `inv_conteo_detalle` | `conteo_id` | Identificador de conteo | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `inv_conteo.conteo_id` | `INV` | `ME`; `P12` |
| `inv_conteo_detalle` | `saldo_id` | Identificador de saldo | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `inv_saldo.saldo_id` | `INV` | `AL`; `P13` |
| `inv_conteo_detalle` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `INV` | `ME`; `P12` |
| `inv_conteo_detalle` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID del registro referenciado | Obligatorio para producto con lote exigido; NULL si producto exento | Referencia a `inv_lote.lote_id`; integridad según 5-B | `INV` | `ME`; `P12` |
| `inv_conteo_detalle` | `ubicacion_id` | ubicacion efectivamente contada | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_ubicacion.ubicacion_id` | `INV` | `ME`; `P12` |
| `inv_conteo_detalle` | `cantidad_sistema` | Cantidad Sistema | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `INV` | `ME`; `P12` |
| `inv_conteo_detalle` | `cantidad_contada` | Cantidad Contada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `INV` | `ME`; `P12` |
| `inv_conteo_detalle` | `diferencia` | Diferencia | decimal(18,3) | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `INV` | `ME`; `P12` |
| `inv_conteo_detalle` | `causa` | Causa | string(255) | SIN_DIFERENCIA, CAPTURA, UBICACION, CONVERSION, MERMA, NO_DETERMINADA; requiere decisión para ajustar | Obligatorio | Sin clave | `INV` | `ME`; `P12` |

| `inv_saldo` | `producto_id` | Producto del saldo, aun cuando no requiere lote | uuid, 128 bits | UUID de mae_producto; si existe lote, su producto_id coincide | Obligatorio | Referencia a mae_producto.producto_id; integridad según 5-B | `INV` | `ME`; `P10` |

**Tabla A.3 - Diccionario de atributos: Recepción, inventario, lote y unidad logística**

*Fuente: elaboración propia de LafroX a partir del modelo lógico de las Figuras 5.2 del Subdocumento 5 y A5.1 del Anexo 5-M, de RT-05.01 de las Bases Técnicas Transversales (PUCV, 2026d) y de la matriz de retención del Anexo 5-D.*

<a id="tab-a4-dic-trazabilidad"></a>

La Tabla A.4 desarrolla los atributos de custodia y frío, con sus condiciones y políticas de conservación.

| Entidad | Atributo | Significado | Tipo lógico, tamaño y precisión | Dominio, formato, catálogo o rango | Obligatoriedad y condición | Clave, referencia y unicidad | Propietario funcional | Sensibilidad, retención y control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `cal_sensor` | `sensor_id` | Identificador de sensor | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `CAL` | `ME`; `P14` |
| `cal_sensor` | `codigo` | Código | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Valor único | `CAL` | `ME`; `P14` |
| `cal_sensor` | `tipo` | Tipo | string(32), catálogo | Catálogo: CAMARA, SONDA, GATEWAY | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_sensor` | `sitio_id` | Sitio de instalación del sensor | uuid, 128 bits | UUID generado; independiente del código comercial | Condicional: obligatorio para sensor fijo, que se instala en un sitio; nula para sensor móvil | Referencia a `mae_sitio.sitio_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_sensor` | `vehiculo_id` | Vehículo en el que se monta el sensor | uuid, 128 bits | UUID del registro referenciado | Condicional: obligatorio para sensor móvil; nula para sensor fijo. La pertenencia es exactamente una de las dos, porque un sensor no puede estar instalado en un sitio y montado en un vehículo al mismo tiempo | Clave foránea a `mae_vehiculo.vehiculo_id` | `CAL` | `ME`; `P14` |
| `cal_sensor` | `gateway_ref` | referencia tecnica al gateway de S4/T-11 | string(255) | Texto libre normalizado; referencia tecnica al gateway de S4/T-11 | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_sensor` | `intervalo_minutos` | Intervalo Minutos | integer, 32 bits | Entero dentro del rango del tipo; negativo solo en una diferencia o un descuadre declarado | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_sensor` | `estado` | Estado | string(32), catálogo | Catálogo: ACTIVO, MANTENIMIENTO, FUERA_DE_SERVICIO | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_regla_termica` | `regla_id` | Identificador de regla | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `CAL` | `ME`; `P14` |
| `cal_regla_termica` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_regla_termica` | `version` | Versión | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Parte de la clave de la versión | `CAL` | `ME`; `P14` |
| `cal_regla_termica` | `umbral_min` | Umbral Min | decimal(18,3) | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_regla_termica` | `umbral_max` | Umbral Max | decimal(18,3) | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_regla_termica` | `duracion_minutos` | Duracion Minutos | integer, 32 bits | Entero dentro del rango del tipo; negativo solo en una diferencia o un descuadre declarado | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_regla_termica` | `severidad` | Severidad | string(32), catálogo | Catálogo: MENOR, CRITICA | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_regla_termica` | `vigente_desde` | Vigente Desde | date | Fecha ISO 8601 de inicio del intervalo; admite vigencias futuras; selección histórica según 5-C | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_regla_termica` | `vigente_hasta` | nulo mientras siga vigente | date | Fecha ISO 8601; nula mientras la versión siga vigente | Condicional: nula en la versión vigente y con fecha en las cerradas | Parte de la unicidad con la fecha de inicio de vigencia | `CAL` | `ME`; `P14` |
| `cal_regla_termica` | `aprobado_por` | rol funcional de Calidad | string(255) | Texto libre normalizado; rol funcional de Calidad | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_calibracion` | `calibracion_id` | Identificador de calibracion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `CAL` | `ME`; `P14` |
| `cal_calibracion` | `sensor_id` | Identificador de sensor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `cal_sensor.sensor_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_calibracion` | `fecha_calibracion` | Fecha Calibración | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_calibracion` | `fecha_vencimiento` | Fecha Vencimiento | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_calibracion` | `incertidumbre` | Incertidumbre | decimal(18,3) | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_calibracion` | `certificado_obj_id` | certificado asociado | string(255) | Texto libre normalizado; certificado asociado | Obligatorio | Sin clave | `CAL` | `AL`; `P14` |
| `cal_calibracion` | `resultado` | Resultado | string(32), catálogo | Catálogo: APROBADO, REPROBADO | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_lectura` | `lectura_id` | Identificador de lectura | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `CAL` | `ME`; `P14` |
| `cal_lectura` | `sensor_id` | Identificador de sensor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `cal_sensor.sensor_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_lectura` | `ts_medicion` | Marca de tiempo de medicion | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_lectura` | `valor` | Valor | decimal(18,3), °C | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `CAL` | `AL`; `P15` |
| `cal_lectura` | `unidad` | Unidad | string(32), catálogo | Unidad de medida registrada en `mae_unidad`; no es texto libre | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_lectura` | `calidad` | Calidad | string(32), catálogo | Catálogo: VALIDA, SOSPECHOSA, INVALIDA | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_lectura` | `hash_evidencia` | Hash Evidencia | string(64), SHA-256 en hexadecimal | Hexadecimal de 64 caracteres; contenido del archivo o del conjunto de objetos | Obligatorio | Sin clave | `CAL` | `AL`; `P14` |
| `cal_asociacion_ventana` | `ventana_id` | Identificador de ventana | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `CAL` | `ME`; `P14` |
| `cal_asociacion_ventana` | `sensor_id` | Identificador de sensor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `cal_sensor.sensor_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_asociacion_ventana` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID del registro referenciado | Obligatorio para producto con lote exigido; NULL si producto exento | Referencia a `inv_lote.lote_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_asociacion_ventana` | `unidad_logistica_id` | Identificador de unidad logistica | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_unidad_logistica.unidad_logistica_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_asociacion_ventana` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_asociacion_ventana` | `desde` | Desde | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_asociacion_ventana` | `hasta` | Instante de cierre de la ventana | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Condicional: nula mientras la ventana siga abierta, que es el estado normal de una ventana en curso; obligatoria en el mismo instante en que la ventana se cierra | Sin clave | `CAL` | `ME`; `P14` |
| `cal_asociacion_lectura` | `asociacion_id` | Identificador de asociacion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `CAL` | `ME`; `P14` |
| `cal_asociacion_lectura` | `ventana_id` | Identificador de ventana | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cal_asociacion_ventana.ventana_id` | `CAL` | `ME`; `P14` |
| `cal_asociacion_lectura` | `lectura_id` | Identificador de lectura | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cal_lectura.lectura_id` | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `evento_id` | Identificador de evento | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `parent_event_id` | causal, no agregación | uuid, 128 bits | UUID del registro referenciado | Condicional: obligatorio en todo evento salvo en la raíz de la cadena | Clave foránea recursiva a `cal_evento_custodia.evento_id`; NULL solo en la raíz | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `ts_ocurrencia` | UTC | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `ts_recepcion` | UTC | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `business_step` | Business Step | string(255) | receiving, transporting, packing, unpacking, shipping, con URI CBV 2.0 y perfil de 5-C | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `event_id_epcis` | identificador canonico GS1 | string(255) | Texto libre normalizado; identificador canonico GS1 | Obligatorio | Valor único, global y no particionado | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `epcis_version` | Versión del estándar EPCIS | string(16), catálogo | Valor 2.0; CBV se declara separadamente en cbv_version | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `cbv_version` | Versión del vocabulario CBV | string(16), catálogo | Valor 2.0; independiente de epcis_version y del perfil de solución | Obligatorio | Sin clave | `CAL` | `ME`; `P16` |
| `cal_evento_custodia` | `perfil_evento` | Perfil versionado de la solución | string(64) | RECEPCION_V1, MOVIMIENTO_V1, AGREGACION_V1, DESPACHO_V1 o ENTREGA_V1; contrato de tipo, acción, paso de negocio y disposición en 5-C | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `tipo_epcis` | Tipo Epcis | string(32), catálogo | ObjectEvent, AggregationEvent; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `accion` | Accion | string(32), catálogo | Catálogo: ADD, OBSERVE, DELETE | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `ubicacion_id` | Identificador de ubicacion | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_ubicacion.ubicacion_id` | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `transaccion_id` | transacciones de negocio del evento | string(255) | Texto libre normalizado; transacciones de negocio del evento | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `actor_id` | Identificador de actor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_actor.actor_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `dispositivo_id` | Identificador de dispositivo | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia lógica al dispositivo, sin FK física: no existe tabla de dispositivos en este esquema (igual que `gob_auditoria.dispositivo_id`) | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `correlacion_id` | Identificador de correlacion | string(64) | Identificador de hasta 64 caracteres generado por el emisor; con el tipo de operación permite reintentar sin duplicar el efecto | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_evento_custodia` | `zona_horaria` | offset local del lugar | string(255) | Identificador de zona horaria IANA del sitio, por ejemplo `America/Santiago` | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_evento_objeto` | `evento_objeto_id` | Identificador de evento objeto | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | PK compuesta con ts_evento; UUID estable de detalle | `CAL` | `ME`; `P14` |
| `cal_evento_objeto` | `evento_id` | Identificador de evento | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | FK compuesta (evento_id,ts_evento) a cal_evento_custodia(evento_id,ts_ocurrencia) | `CAL` | `ME`; `P14` |
| `cal_evento_objeto` | `secuencia_linea` | Identidad ordinal estable del objeto en el evento | integer, 32 bits | Entero positivo. Ordinal del perfil de origen; si no existe, posición del arreglo canónico congelado del evento antes de publicar. Reintentos reutilizan evento y arreglo; no se reordena ni deriva de la hora de recepción | Obligatorio | Único con evento_id y ts_evento; timestamp vinculado a la cabecera por FK compuesta | `CAL` | `ME`; `P14` |
| `cal_evento_objeto` | `ts_evento` | copia mantenida del instante del evento | timestamp with time zone, UTC | Copia de `cal_evento_custodia.ts_ocurrencia`, escrita en la misma transacción que el evento. Existe para que el detalle tenga su propia clave de partición y su propia ventana de retención | Obligatorio | Parte de PK y partición; FK (evento_id, ts_evento) a cabecera (evento_id, ts_ocurrencia) | `CAL` | `ME`; `P14` |
| `cal_evento_objeto` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID del registro referenciado | Obligatorio para producto con lote exigido; NULL si producto exento | Referencia a `inv_lote.lote_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_evento_objeto` | `unidad_logistica_id` | Identificador de unidad logistica | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_unidad_logistica.unidad_logistica_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_evento_objeto` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_evento_objeto` | `unidad_id` | unidad de medida | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_unidad.unidad_id` | `CAL` | `ME`; `P14` |
| `cal_evento_objeto` | `cantidad` | Cantidad | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_evento_objeto` | `epcis_parent_id` | Contenedor de agregación, distinto de causa | string(255) | ID canónico del contenedor según EPCIS; igual en todos los hijos de una agregación | Obligatorio en agregación; NULL cuando no aplica | Sin clave | `CAL` | `ME`; `P14` |
| `cal_documento_evento` | `documento_evento_id` | Identificador de documento evento | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `CAL` | `ME`; `P14` |
| `cal_documento_evento` | `evento_id` | Identificador de evento | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cal_evento_custodia.evento_id` | `CAL` | `ME`; `P14` |
| `cal_documento_evento` | `documento_id` | Identificador de documento | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `doc_documento.documento_id` | `CAL` | `ME`; `P14` |
| `cal_documento_evento` | `hash_evidencia` | Hash Evidencia | string(64), SHA-256 en hexadecimal | Hexadecimal de 64 caracteres; contenido del archivo o del conjunto de objetos | Obligatorio | Sin clave | `CAL` | `AL`; `P14` |
| `cal_excursion` | `excursion_id` | Identificador de excursion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `CAL` | `ME`; `P14` |
| `cal_excursion` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_excursion` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_lote.lote_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_excursion` | `unidad_logistica_id` | Identificador de unidad logistica | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_unidad_logistica.unidad_logistica_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_excursion` | `sensor_id` | Identificador de sensor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `cal_sensor.sensor_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_excursion` | `regla_id` | regla vigente al detectarse | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cal_regla_termica.regla_id` | `CAL` | `ME`; `P14` |
| `cal_excursion` | `inicio` | Inicio | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_excursion` | `fin` | Instante de fin de la excursión | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Condicional: nula mientras la excursión siga abierta, es decir mientras no se haya confirmado ni descartado; obligatoria cuando la excursión se cierra | Sin clave | `CAL` | `ME`; `P14` |
| `cal_excursion` | `magnitud` | Magnitud | decimal(18,6) | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_excursion` | `severidad` | Severidad | string(32), catálogo | MENOR, CRITICA; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_bloqueo` | `bloqueo_id` | Identificador de bloqueo | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `CAL` | `ME`; `P14` |
| `cal_bloqueo` | `excursion_id` | Identificador de excursion | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cal_excursion.excursion_id` | `CAL` | `ME`; `P14` |
| `cal_bloqueo` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_lote.lote_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_bloqueo` | `unidad_logistica_id` | Identificador de unidad logistica | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_unidad_logistica.unidad_logistica_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_bloqueo` | `motivo` | Motivo | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_bloqueo` | `estado` | Estado | string(32), catálogo | Catálogo: VIGENTE, LEVANTADO | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_bloqueo` | `actor_id` | Identificador de actor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_actor.actor_id`; integridad según 5-B | `CAL` | `ME`; `P14` |
| `cal_bloqueo` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_resolucion_calidad` | `resolucion_id` | Identificador de resolucion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `CAL` | `ME`; `P14` |
| `cal_resolucion_calidad` | `bloqueo_id` | Identificador de bloqueo | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cal_bloqueo.bloqueo_id` | `CAL` | `ME`; `P14` |
| `cal_resolucion_calidad` | `responsable_id` | Identificador de responsable | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_actor.actor_id` | `CAL` | `ME`; `P14` |
| `cal_resolucion_calidad` | `decision` | Decision | string(32), catálogo | Catálogo: LIBERAR, RETENER, DESTRUIR | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_resolucion_calidad` | `fundamento` | Fundamento | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |
| `cal_resolucion_calidad` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `CAL` | `ME`; `P14` |

**Tabla A.4 - Diccionario de atributos: Trazabilidad sanitaria y cadena de custodia**

*Fuente: elaboración propia de LafroX a partir del modelo lógico de las Figuras 5.5 y 5.2 del Subdocumento 5 y A5.3 del Anexo 5-M, de RT-05.01 de las Bases Técnicas Transversales (PUCV, 2026d) y de la matriz de retención del Anexo 5-D.*

La validación aplica la condición de cada fila al hito indicado; NULL legítimo se distingue de dato obligatorio ausente.

<a id="tab-a5-dic-preventa"></a>

La Tabla A.5 desarrolla los atributos de pedido y preparación, con sus condiciones y políticas de conservación.

| Entidad | Atributo | Significado | Tipo lógico, tamaño y precisión | Dominio, formato, catálogo o rango | Obligatoriedad y condición | Clave, referencia y unicidad | Propietario funcional | Sensibilidad, retención y control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `prv_tarifa` | `tarifa_id` | Identificador de tarifa | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `PRE` | `ME`; `P17` |
| `prv_tarifa` | `version` | version de la tarifa | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio, clave primaria | Clave primaria; Parte de la clave de la versión | `PRE` | `ME`; `P17` |
| `prv_tarifa` | `cliente_id` | Identificador de cliente | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_cliente.cliente_id`; integridad según 5-B | `PRE` | `ME`; `P17` |
| `prv_tarifa` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `PRE` | `ME`; `P17` |
| `prv_tarifa` | `canal` | Canal | string(32), catálogo | TRADICIONAL, MODERNO, FOOD_SERVICE, CADENA, HORECA; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `PRE` | `ME`; `P17` |
| `prv_tarifa` | `precio` | Precio | decimal(18,2), CLP | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `PRE` | `AL`; `P18` |
| `prv_tarifa` | `vigente_desde` | Vigente Desde | date | Fecha ISO 8601 de inicio del intervalo; admite vigencias futuras; selección histórica según 5-C | Obligatorio | Sin clave | `PRE` | `ME`; `P17` |
| `prv_tarifa` | `vigente_hasta` | nulo mientras la version siga vigente | date | Fecha ISO 8601; nula mientras la versión siga vigente | Condicional: nula en la versión vigente y con fecha en las cerradas | Parte de la unicidad con la fecha de inicio de vigencia | `PRE` | `ME`; `P17` |
| `prv_pedido` | `pedido_id` | Identificador de pedido | uuid, 128 bits | UUID propio de cada registro ORIGINAL o REVISION | Obligatorio, clave primaria | Clave primaria individual | `PRE` | `ME`; `P19` |
| `prv_pedido` | `cliente_id` | Identificador de cliente | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_cliente.cliente_id`; integridad según 5-B | `PRE` | `ME`; `P19` |
| `prv_pedido` | `canal` | Canal | string(32), catálogo | TRADICIONAL, MODERNO, FOOD_SERVICE, CADENA, HORECA; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `PRE` | `ME`; `P19` |
| `prv_pedido` | `fecha_toma` | Fecha Toma | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `PRE` | `ME`; `P19` |
| `prv_pedido` | `preventista_id` | Preventista que captura el pedido en TERRENO; no es autor genérico de los demás canales | uuid, 128 bits | UUID del registro referenciado | Obligatorio solo en origen_captura=TERRENO; NULL en MOSTRADOR, EDI y PORTAL | Clave foránea a `mae_actor.actor_id` | `PRE` | `ME`; `P19` |
| `prv_pedido` | `sitio_origen_id` | Identificador de sitio origen | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_sitio.sitio_id` | `PRE` | `ME`; `P19` |
| `prv_pedido` | `origen_captura` | Origen Captura | string(32), catálogo | Catálogo: TERRENO, MOSTRADOR, EDI, PORTAL | Obligatorio | Sin clave | `PRE` | `ME`; `P19` |
| `prv_pedido` | `conexion_disponible` | estado de la red, no del pedido | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `PRE` | `ME`; `P19` |
| `prv_pedido` | `estado` | Estado | string(32), catálogo | Catálogo: PENDIENTE, CONFIRMADO, QUIEBRE, CANCELADO | Obligatorio | Sin clave | `PRE` | `ME`; `P19` |
| `prv_pedido_linea` | `linea_id` | Identificador de linea | uuid, 128 bits | UUID propio de cada registro ORIGINAL o REVISION | Obligatorio, clave primaria | Clave primaria individual | `PRE` | `ME`; `P19` |
| `prv_pedido_linea` | `pedido_id` | Identificador de pedido | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `prv_pedido.pedido_id`; integridad según 5-B | `PRE` | `ME`; `P19` |
| `prv_pedido_linea` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `PRE` | `ME`; `P19` |
| `prv_pedido_linea` | `cantidad_solicitada` | Cantidad Solicitada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `PRE` | `ME`; `P19` |
| `prv_pedido_linea` | `unidad_id` | Identificador de unidad | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_unidad.unidad_id` | `PRE` | `ME`; `P19` |
| `prv_pedido_linea` | `precio_unitario` | Precio Unitario | decimal(18,2), CLP | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `PRE` | `AL`; `P20` |
| `prv_pedido_linea` | `moneda` | CLP | string(32), catálogo | CLP; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `PRE` | `ME`; `P19` |
| `prv_pedido_linea` | `tarifa_id` | version de tarifa efectivamente aplicada | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `prv_tarifa.tarifa_id` | `PRE` | `ME`; `P19` |
| `prv_pedido_linea` | `tarifa_version` | Tarifa Versión | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio; referencia válida | Parte de la clave foránea compuesta (`tarifa_id`, `tarifa_version`) a `prv_tarifa(tarifa_id, version)` | `PRE` | `ME`; `P19` |
| `prv_pedido_promesa` | `promesa_id` | Identificador de promesa | uuid, 128 bits | UUID propio de cada registro ORIGINAL o REVISION | Obligatorio, clave primaria | Clave primaria individual | `PRE` | `ME`; `P19` |
| `prv_pedido_promesa` | `pedido_id` | Identificador de pedido | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `prv_pedido.pedido_id`; integridad según 5-B | `PRE` | `ME`; `P19` |
| `prv_pedido_promesa` | `fecha_prometida` | Fecha Prometida | timestamp with time zone, UTC | Instante y ventana comprometidos en UTC; ORIGINAL inmutable; zona de origen conservada en contrato | Obligatorio | Sin clave | `PRE` | `ME`; `P19` |
| `prv_pedido_promesa` | `tipo` | Discriminador único de la promesa | string(32), catálogo | Catálogo: ORIGINAL, REVISION. Es el único atributo que distingue la promesa declarada de su revisión, de modo que no existe un indicador booleano paralelo | Obligatorio | Único parcial con `pedido_id` en el valor `ORIGINAL` | `PRE` | `ME`; `P19` |
| `prv_pedido_promesa` | `version` | Ordinal de promesa dentro del pedido | integer, 32 bits | Entero no negativo; único dentro del pedido | Obligatorio | Unicidad compuesta con `pedido_id`; no integra la PK | `PRE` | `ME`; `P19` |
| `prv_pedido_promesa` | `vigente_desde` | Vigente Desde | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `PRE` | `ME`; `P19` |
| `prv_pedido_promesa` | `vigente_hasta` | nulo en la promesa vigente | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Condicional: nula en la versión vigente y con fecha en las cerradas | Parte de la unicidad con la fecha de inicio de vigencia | `PRE` | `ME`; `P19` |
| `prv_pedido_promesa` | `motivo_cambio` | obligatorio en tipo REVISION | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Condicional: obligatorio cuando el tipo es REVISION; no se admite sin texto | Sin clave | `PRE` | `ME`; `P19` |
| `prv_pedido_promesa` | `actor_id` | Identificador de actor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_actor.actor_id`; integridad según 5-B | `PRE` | `ME`; `P19` |
| `prv_pedido_promesa` | `autorizador_id` | rol funcional que aprueba la reprogramación | string(255) | Identificador del rol de negocio que autoriza la revisión de la promesa | Condicional: obligatorio cuando `tipo` es REVISION, porque reprogramar cambia el compromiso del cliente; nula cuando `tipo` es ORIGINAL | Sin clave | `PRE` | `ME`; `P19` |
| `prv_pedido_promesa` | `fecha_registro` | Fecha Registro | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `PRE` | `ME`; `P19` |
| `prv_linea_asignacion` | `asignacion_id` | Identificador de asignacion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `PRE` | `ME`; `P21` |
| `prv_linea_asignacion` | `linea_id` | Identificador de linea | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `prv_pedido_linea.linea_id`; contrato si otro almacén | `PRE` | `ME`; `P21` |
| `prv_linea_asignacion` | `reserva_linea_id` | Identificador de reserva linea | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_reserva_linea.reserva_linea_id`; integridad según 5-B | `PRE` | `ME`; `P21` |
| `prv_linea_asignacion` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio para producto con lote exigido; NULL si producto exento | Referencia a `inv_lote.lote_id`; integridad según 5-B | `PRE` | `ME`; `P21` |
| `prv_linea_asignacion` | `cantidad_asignada` | Cantidad Asignada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `PRE` | `ME`; `P21` |
| `prv_linea_asignacion` | `cantidad_preparada` | Cantidad Preparada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `PRE` | `ME`; `P21` |
| `prp_mision` | `mision_id` | Identificador de mision | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `PREP` | `ME`; `P19` |
| `prp_mision` | `pedido_id` | Identificador de pedido | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `prv_pedido.pedido_id`; integridad según 5-B | `PREP` | `ME`; `P19` |
| `prp_mision` | `sitio_id` | Identificador de sitio | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_sitio.sitio_id`; integridad según 5-B | `PREP` | `ME`; `P19` |
| `prp_mision` | `ola` | Ola | string(255) | Tiempo objetivo de atención en minutos, contados desde el evento que origina laacción | Obligatorio | Sin clave | `PREP` | `ME`; `P19` |
| `prp_mision` | `estado` | PLANIFICADA, EN CURSO, CERRADA, CANCELADA | string(32), catálogo | PLANIFICADA, EN_CURSO, CERRADA, CANCELADA; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `PREP` | `ME`; `P19` |
| `prp_mision` | `fecha_inicio` | Fecha Inicio | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `PREP` | `ME`; `P19` |
| `prp_mision_linea` | `mision_linea_id` | Identificador de mision linea | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `PREP` | `ME`; `P19` |
| `prp_mision_linea` | `mision_id` | Identificador de mision | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `prp_mision.mision_id` | `PREP` | `ME`; `P19` |
| `prp_mision_linea` | `asignacion_id` | Identificador de asignacion | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `prv_linea_asignacion.asignacion_id` | `PREP` | `ME`; `P19` |
| `prp_mision_linea` | `cantidad_confirmada` | Cantidad Confirmada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `PREP` | `CR`; `P22` |
| `prp_mision_linea` | `cantidad_faltante` | Cantidad Faltante | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `PREP` | `ME`; `P19` |
| `prp_mision_linea` | `cantidad_rechazada` | Cantidad Rechazada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio, admite cero; no puede superar la cantidad de referencia | Sin clave | `PREP` | `ME`; `P19` |
| `prp_picking_confirmacion` | `confirmacion_id` | Identificador de confirmacion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `PREP` | `CR`; `P22` |
| `prp_picking_confirmacion` | `mision_linea_id` | Identificador de mision linea | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `prp_mision_linea.mision_linea_id` | `PREP` | `ME`; `P19` |
| `prp_picking_confirmacion` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID del registro referenciado | Obligatorio para producto con lote exigido; NULL si producto exento | Referencia a `inv_lote.lote_id`; integridad según 5-B | `PREP` | `ME`; `P19` |
| `prp_picking_confirmacion` | `unidad_logistica_id` | Identificador de unidad logistica | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_unidad_logistica.unidad_logistica_id`; integridad según 5-B | `PREP` | `ME`; `P19` |
| `prp_picking_confirmacion` | `actor_id` | Identificador de actor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_actor.actor_id`; integridad según 5-B | `PREP` | `ME`; `P19` |
| `prp_picking_confirmacion` | `dispositivo_id` | Identificador de dispositivo | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia lógica al dispositivo, sin FK física: no existe tabla de dispositivos en este esquema (igual que `gob_auditoria.dispositivo_id`) | `PREP` | `ME`; `P19` |
| `prp_picking_confirmacion` | `cantidad_confirmada` | Cantidad Confirmada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `PREP` | `CR`; `P22` |
| `prp_picking_confirmacion` | `cantidad_rechazada` | Cantidad Rechazada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio, admite cero; no puede superar la cantidad de referencia | Sin clave | `PREP` | `ME`; `P19` |
| `prp_picking_confirmacion` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `PREP` | `ME`; `P19` |

**Tabla A.5 - Diccionario de atributos: Preventa, reserva y preparación**

*Fuente: elaboración propia de LafroX a partir del modelo lógico de las Figuras 5.3 y 5.2 del Subdocumento 5, de RT-05.01 de las Bases Técnicas Transversales (PUCV, 2026d) y de la matriz de retención del Anexo 5-D.*

La validación aplica la condición de cada fila al hito indicado; NULL legítimo se distingue de dato obligatorio ausente.

<a id="tab-a6-dic-reparto"></a>

La Tabla A.6 desarrolla los atributos de ruta, reparto y envases, con sus condiciones y políticas de conservación.

| Entidad | Atributo | Significado | Tipo lógico, tamaño y precisión | Dominio, formato, catálogo o rango | Obligatoriedad y condición | Clave, referencia y unicidad | Propietario funcional | Sensibilidad, retención y control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `rut_ruta` | `ruta_id` | Identificador de ruta | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `RUT` | `ME`; `P23` |
| `rut_ruta` | `planificador_id` | Identificador de planificador | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_actor.actor_id` | `RUT` | `ME`; `P23` |
| `rut_ruta` | `fecha` | Fecha | date | Fecha ISO 8601 programada de la ruta en el calendario del sitio; admite rutas históricas y futuras | Obligatorio | Sin clave | `RUT` | `ME`; `P23` |
| `rut_ruta` | `estado` | PLANIFICADA, EN CURSO, CERRADA | string(32), catálogo | PLANIFICADA, EN_CURSO, CERRADA; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `RUT` | `ME`; `P23` |
| `rut_ruta` | `kilometros` | Kilometros | decimal(18,3) | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `RUT` | `ME`; `P23` |
| `rut_viaje` | `viaje_id` | Identificador de viaje | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `RUT` | `ME`; `P23` |
| `rut_viaje` | `ruta_id` | Identificador de ruta | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `rut_ruta.ruta_id` | `RUT` | `ME`; `P23` |
| `rut_viaje` | `vehiculo_id` | Identificador de vehiculo | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_vehiculo.vehiculo_id` | `RUT` | `ME`; `P23` |
| `rut_viaje` | `conductor_id` | Identificador de conductor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_actor.actor_id` | `RUT` | `CR`; `P24` |
| `rut_viaje` | `salida_prevista` | Salida Prevista | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `RUT` | `ME`; `P23` |
| `rut_viaje` | `llegada_real` | Llegada Real | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `RUT` | `ME`; `P23` |
| `rut_viaje` | `estado` | Estado | string(32), catálogo | PLANIFICADO, EN_CURSO, RETORNADO, CERRADO, CANCELADO; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `RUT` | `ME`; `P23` |
| `rut_parada` | `parada_id` | Identificador de parada | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `RUT` | `ME`; `P23` |
| `rut_parada` | `viaje_id` | Identificador de viaje | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `rut_viaje.viaje_id` | `RUT` | `ME`; `P23` |
| `rut_parada` | `secuencia` | Secuencia | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Sin clave | `RUT` | `ME`; `P23` |
| `rut_parada` | `cliente_id` | Identificador de cliente | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_cliente.cliente_id`; integridad según 5-B | `RUT` | `ME`; `P23` |
| `rut_parada` | `cliente_punto_id` | Identificador de cliente punto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_cliente_punto.cliente_punto_id` | `RUT` | `ME`; `P23` |
| `rut_parada` | `ventana_inicio` | Ventana Inicio | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `RUT` | `ME`; `P23` |
| `rut_parada` | `ventana_fin` | Ventana Fin | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `RUT` | `ME`; `P23` |
| `rut_parada` | `ubicacion` | Ubicación | geometry(Point, 4326) | Punto georreferenciado en WGS 84 (EPSG:4326), en el sistema de referencia declarado por el sitio | Obligatorio | Sin clave | `RUT` | `ME`; `P23` |
| `rut_geocerca` | `geocerca_id` | Identificador de geocerca | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `RUT` | `CR`; `P25` |
| `rut_geocerca` | `parada_id` | Identificador de parada | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `rut_parada.parada_id` | `RUT` | `ME`; `P23` |
| `rut_geocerca` | `tipo` | Tipo | string(32), catálogo | Catálogo: BARRIO, RADIO_DESCARGA, RESTRICCION | Obligatorio | Sin clave | `RUT` | `ME`; `P23` |
| `rut_geocerca` | `poligono` | Poligono | geometry(Polygon, 4326) | Polígono válido SRID 4326, cerrado y sin auto-intersecciones; geocerca de configuración, no posición personal | Obligatorio | Sin clave | `RUT` | `ME`; `P23` |
| `rep_entrega` | `entrega_id` | Identificador de entrega | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `REP` | `ME`; `P27` |
| `rep_entrega` | `pedido_id` | unico: un pedido genera una entrega | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `prv_pedido.pedido_id`; integridad según 5-B | `REP` | `ME`; `P27` |
| `rep_entrega` | `parada_id` | Identificador de parada | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `rut_parada.parada_id` | `REP` | `ME`; `P27` |
| `rep_entrega` | `completa` | Completa | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `REP` | `ME`; `P27` |
| `rep_entrega` | `a_tiempo` | A Tiempo | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `REP` | `ME`; `P27` |
| `rep_entrega` | `promesa_id` | promesa original inmutable | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a la PK individual prv_pedido_promesa.promesa_id, ORIGINAL del mismo pedido; no requiere vigencia actual | `REP` | `ME`; `P27` |
| `rep_entrega` | `estado` | Estado | string(32), catálogo | Catálogo: PENDIENTE, ENTREGADA, PARCIAL, DEVUELTA, NO_ENTREGADA | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `rep_intento` | `intento_id` | Identificador de intento | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `REP` | `ME`; `P27` |
| `rep_intento` | `entrega_id` | Identificador de entrega | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `rep_entrega.entrega_id`; integridad según 5-B | `REP` | `ME`; `P27` |
| `rep_intento` | `numero` | orden del intento en la entrega | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `rep_intento` | `llegada` | Llegada | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `rep_intento` | `salida` | Salida | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `rep_intento` | `resultado` | Resultado | string(32), catálogo | Catálogo: EXITO, RECHAZO_PARCIAL, RECHAZO_TOTAL, NO_ATENDIDO | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `rep_intento` | `causal_id` | Identificador de causal | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `rep_causal.causal_id` | `REP` | `ME`; `P27` |
| `rep_intento` | `receptor_nombre` | Receptor Nombre | string(512) | Texto normalizado del interviniente; es dato personal cuando identifica a una persona natural | Obligatorio cuando existe receptor identificado; NULL en NO_CONTACTO o intento sin receptor | Sin clave | `REP` | `CR`; `P28` |
| `rep_intento` | `receptor_documento` | Receptor Documento | string(255) | Texto normalizado del interviniente; es dato personal cuando identifica a una persona natural | Obligatorio | Sin clave | `REP` | `CR`; `P28` |
| `rep_intento` | `receptor_relacion` | Receptor Relacion | string(32), catálogo | Catálogo: TITULAR, SUSTITUTO, NO_SABE_FIRMAR, RECHAZA | Obligatorio | Sin clave | `REP` | `CR`; `P28` |
| `rep_intento` | `evidencia_obj_id` | Identificador de evidencia obj | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `obj_objeto.objeto_id` | `REP` | `ME`; `P27` |
| `rep_entrega_linea` | `entrega_linea_id` | Identificador de entrega linea | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `REP` | `ME`; `P27` |
| `rep_entrega_linea` | `entrega_id` | Identificador de entrega | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `rep_entrega.entrega_id`; integridad según 5-B | `REP` | `ME`; `P27` |
| `rep_entrega_linea` | `linea_id` | Identificador de linea | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `prv_pedido_linea.linea_id` | `REP` | `ME`; `P27` |
| `rep_entrega_linea` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio para producto con lote exigido; NULL si producto exento | Referencia a `inv_lote.lote_id`; integridad según 5-B | `REP` | `ME`; `P27` |
| `rep_entrega_linea` | `cantidad_aceptada` | Cantidad Aceptada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `rep_entrega_linea` | `cantidad_rechazada` | Cantidad Rechazada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio, admite cero; no puede superar la cantidad de referencia | Sin clave | `REP` | `ME`; `P27` |
| `rep_entrega_linea` | `intento_id` | intento que la entrego | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `rep_intento.intento_id`; integridad según 5-B | `REP` | `ME`; `P27` |
| `rep_entrega_linea` | `asignacion_id` | Identificador de asignacion | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `prv_linea_asignacion.asignacion_id`; contrato si otro almacén | `REP` | `ME`; `P27` |
| `rep_entrega_linea` | `unidad_logistica_id` | Identificador de unidad logistica | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_unidad_logistica.unidad_logistica_id`; integridad según 5-B | `REP` | `ME`; `P27` |
| `rep_entrega_linea` | `unidad_id` | unidad de medida de las cantidades | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_unidad.unidad_id` | `REP` | `ME`; `P27` |
| `rep_causal` | `causal_id` | Identificador de causal | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `REP` | `ME`; `P27` |
| `rep_causal` | `codigo` | Código | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Valor único | `REP` | `ME`; `P27` |
| `rep_causal` | `descripcion` | Descripción | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `rep_causal` | `categoria` | Categoria | string(32), catálogo | Catálogo: PREPARACION, RUTEO, VENTANA, RECEPTION, CLIMA | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `rep_devolucion` | `devolucion_id` | Identificador de devolucion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `REP` | `ME`; `P27` |
| `rep_devolucion` | `entrega_id` | Identificador de entrega | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `rep_entrega.entrega_id`; integridad según 5-B | `REP` | `ME`; `P27` |
| `rep_devolucion` | `causal_id` | Identificador de causal | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `rep_causal.causal_id` | `REP` | `ME`; `P27` |
| `rep_devolucion` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `rep_devolucion` | `estado` | Estado | string(32), catálogo | REGISTRADA, RECIBIDA, EVALUADA, CERRADA, RECHAZADA; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `rep_devolucion_linea` | `devolucion_linea_id` | Identificador de devolucion linea | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `REP` | `ME`; `P27` |
| `rep_devolucion_linea` | `devolucion_id` | Identificador de devolucion | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `rep_devolucion.devolucion_id` | `REP` | `ME`; `P27` |
| `rep_devolucion_linea` | `asignacion_id` | Identificador de asignacion | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `prv_linea_asignacion.asignacion_id` | `REP` | `ME`; `P27` |
| `rep_devolucion_linea` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID del registro referenciado | Obligatorio para producto con lote exigido; NULL si producto exento | Referencia a `inv_lote.lote_id`; integridad según 5-B | `REP` | `ME`; `P27` |
| `rep_devolucion_linea` | `unidad_logistica_id` | Identificador de unidad logistica | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_unidad_logistica.unidad_logistica_id`; integridad según 5-B | `REP` | `ME`; `P27` |
| `rep_devolucion_linea` | `cantidad` | Cantidad | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `rep_devolucion_linea` | `motivo` | Motivo | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `env_cuenta_corriente` | `cuenta_id` | Identificador de cuenta | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `REP` | `ME`; `P27` |
| `env_cuenta_corriente` | `cliente_id` | Identificador de cliente | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_cliente.cliente_id`; integridad según 5-B | `REP` | `ME`; `P27` |
| `env_cuenta_corriente` | `tipo_envase` | unica cuenta por cliente y tipo | string(32), catálogo | Código activo del maestro versionado de tipos de envase del CLIENTE; 1–32 caracteres, sin serialización individual ni alta por defecto; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `env_cuenta_corriente` | `saldo` | Saldo | integer, 32 bits | Entero dentro del rango del tipo; negativo solo en una diferencia o un descuadre declarado | Obligatorio | Sin clave | `REP` | `AL`; `P29` |
| `env_movimiento` | `movimiento_id` | Identificador de movimiento | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `REP` | `ME`; `P27` |
| `env_movimiento` | `cuenta_id` | Identificador de cuenta | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `env_cuenta_corriente.cuenta_id` | `REP` | `ME`; `P27` |
| `env_movimiento` | `entrega_id` | opcional: hay movimientos sin entrega | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `rep_entrega.entrega_id`; integridad según 5-B | `REP` | `ME`; `P27` |
| `env_movimiento` | `tipo` | Tipo | string(32), catálogo | Catálogo: ENTREGA, DEVOLUCION, DEPOSITO_BODEGA, AJUSTE | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `env_movimiento` | `cantidad` | Cantidad | integer, 32 bits | Entero dentro del rango del tipo; negativo solo en una diferencia o un descuadre declarado | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `env_movimiento` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `REP` | `ME`; `P27` |
| `env_movimiento` | `conductor_id` | Identificador de conductor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_actor.actor_id` | `REP` | `CR`; `P28` |
| `env_movimiento` | `evidencia_obj_id` | Identificador de evidencia obj | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `obj_objeto.objeto_id` | `REP` | `ME`; `P27` |

**Tabla A.6 - Diccionario de atributos: Rutas, reparto, entrega, devolución y envases**

*Fuente: elaboración propia de LafroX a partir del modelo lógico de las Figuras 5.4 y 5.6 del Subdocumento 5, de RT-05.01 de las Bases Técnicas Transversales (PUCV, 2026d) y de la matriz de retención del Anexo 5-D.*

La validación aplica la condición de cada fila al hito indicado; NULL legítimo se distingue de dato obligatorio ausente.

<a id="tab-a7-dic-cobranza-documentos"></a>

La Tabla A.7 desarrolla los atributos de cobranza y documentos, con sus condiciones y políticas de conservación.

| Entidad | Atributo | Significado | Tipo lógico, tamaño y precisión | Dominio, formato, catálogo o rango | Obligatoriedad y condición | Clave, referencia y unicidad | Propietario funcional | Sensibilidad, retención y control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `cob_saldo` | `saldo_id` | Identificador de saldo | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `COB` | `AL`; `P30` |
| `cob_saldo` | `cliente_id` | Identificador de cliente | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_cliente.cliente_id`; integridad según 5-B | `COB` | `ME`; `P31` |
| `cob_saldo` | `monto_total` | monto adeudado | decimal(18,2), CLP | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `COB` | `AL`; `P30` |
| `cob_saldo` | `monto_vencido` | Monto Vencido | decimal(18,2), CLP | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `COB` | `AL`; `P30` |
| `cob_saldo` | `fecha_corte` | Fecha Corte | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_cobro` | `cobro_id` | Identificador de cobro | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `COB` | `ME`; `P31` |
| `cob_cobro` | `entrega_id` | Identificador de entrega | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `rep_entrega.entrega_id`; integridad según 5-B | `COB` | `ME`; `P31` |
| `cob_cobro` | `monto` | Monto | decimal(18,2), CLP | Importe monetario en pesos chilenos; precisión 2 decimales | Obligatorio | Sin clave | `COB` | `AL`; `P30` |
| `cob_cobro` | `moneda` | CLP | string(32), catálogo | CLP; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_cobro` | `clave_idempotencia` | Clave Idempotencia | string(255) | Identificador de hasta 64 caracteres generado por el emisor; con el tipo de operación permite reintentar sin duplicar el efecto | Obligatorio | Valor único | `COB` | `ME`; `P31` |
| `cob_cobro` | `estado` | Estado | string(32), catálogo | Catálogo: REGISTRADO, ACEPTADO, ANULADO, PENDIENTE_ALTERNATIVO | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_cobro` | `rendicion_id` | nulo hasta que el conductor lo declara | uuid, 128 bits | UUID del registro referenciado | Nullable al capturar cobro; obligatorio en el hito de rendición/cierre. Referencia a cob_rendicion.rendicion_id | Clave foránea a `cob_rendicion.rendicion_id` | `COB` | `ME`; `P31` |
| `cob_cobro` | `ajuste_redondeo` | Ajuste monetario aplicado al importe del cobro | decimal(18,2), CLP | Diferencia con signo entre importe registrado y monto autorizado externo, exclusivamente para tarjeta con autorización comprobable. Cero si coinciden; NULL para efectivo o crédito sin autorización externa. No modifica por sí solo el saldo | Obligatorio al conciliar tarjeta con importe autorizado disponible; NULL si no existe tal importe | Sin clave | `COB` | `AL`; `P30` |
| `cob_cobro` | `medio` | Medio | string(32), catálogo | Catálogo: EFECTIVO, CREDITO, TARJETA | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_cobro` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_pos_operacion` | `pos_id` | Identificador de pos | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `COB` | `ME`; `P31` |
| `cob_pos_operacion` | `cobro_id` | Identificador de cobro | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cob_cobro.cobro_id` | `COB` | `ME`; `P31` |
| `cob_pos_operacion` | `operacion_id` | mismo id para consulta y compensacion | string(255) | Texto libre normalizado; mismo id para consulta y compensacion | Obligatorio | Valor único | `COB` | `ME`; `P31` |
| `cob_pos_operacion` | `monto` | Monto | decimal(18,2), CLP | Importe monetario en CLP | Obligatorio | Sin clave | `COB` | `AL`; `P30` |
| `cob_pos_operacion` | `medio` | Medio | string(32), catálogo | Catálogo: TARJETA, TRANSFERENCIA | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_pos_operacion` | `estado` | Estado | string(32), catálogo | Catálogo: PENDIENTE, CONFIRMADA, RECHAZADA, COMPENSADA | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_pos_operacion` | `fecha_ultima_consulta` | Fecha Ultima Consulta | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_compensacion` | `compensacion_id` | Identificador de compensacion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `COB` | `ME`; `P31` |
| `cob_compensacion` | `pos_id` | Identificador de pos | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cob_pos_operacion.pos_id` | `COB` | `ME`; `P31` |
| `cob_compensacion` | `cob_cobro_alternativo_id` | Identificador de cob cobro alternativo | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cob_cobro.cobro_id` | `COB` | `ME`; `P31` |
| `cob_compensacion` | `autorizador_id` | Autorizador de la compensación | uuid, 128 bits | UUID de mae_actor.actor_id con rol financiero habilitado y distinto del ejecutor | Obligatorio antes de aprobar todo movimiento o compensación monetaria; NULL mientras esté pendiente. Una consulta no genera autorización financiera | Referencia a mae_actor.actor_id; integridad según 5-B | `COB` | `ME`; `P31` |
| `cob_compensacion` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_compensacion` | `decision` | Decision | string(32), catálogo | Catálogo: COMPENSAR, REINTENTAR, DEVOLVER | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_compensacion` | `fundamento` | Fundamento | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_aplicacion` | `aplicacion_id` | Identificador de aplicacion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `COB` | `ME`; `P31` |
| `cob_aplicacion` | `cobro_id` | Identificador de cobro | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cob_cobro.cobro_id` | `COB` | `ME`; `P31` |
| `cob_aplicacion` | `documento_id` | Identificador de documento | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `doc_documento.documento_id` | `COB` | `ME`; `P31` |
| `cob_aplicacion` | `saldo_id` | Identificador de saldo | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cob_saldo.saldo_id` | `COB` | `AL`; `P30` |
| `cob_aplicacion` | `monto_aplicado` | Monto Aplicado | decimal(18,2), CLP | Importe aplicado en CLP | Obligatorio | Sin clave | `COB` | `AL`; `P30` |
| `cob_aplicacion` | `moneda` | Moneda | string(32), catálogo | CLP; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_rendicion` | `rendicion_id` | Identificador de rendicion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `COB` | `ME`; `P31` |
| `cob_rendicion` | `conductor_id` | Identificador de conductor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_actor.actor_id` | `COB` | `CR`; `P32` |
| `cob_rendicion` | `vehiculo_id` | Identificador de vehiculo | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_vehiculo.vehiculo_id` | `COB` | `ME`; `P31` |
| `cob_rendicion` | `caja_codigo` | Caja Código | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_rendicion` | `turno` | Turno | string(255) | Identidad del turno preinscrito de S4, actor/sitio e inicio; hasta 255 caracteres, referencia verificable | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_rendicion` | `fecha_retorno` | Fecha Retorno | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_rendicion` | `monto_declarado` | Monto Declarado | decimal(18,2), CLP | Monto declarado en rendición (CLP) | Obligatorio | Sin clave | `COB` | `AL`; `P30` |
| `cob_rendicion` | `estado` | Estado | string(32), catálogo | Catálogo: ABIERTA, CERRADA, CON_DESCUADRE | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_cuadratura` | `cuadratura_id` | Identificador de cuadratura | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `COB` | `ME`; `P31` |
| `cob_cuadratura` | `rendicion_id` | Identificador de rendicion | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cob_rendicion.rendicion_id` | `COB` | `ME`; `P31` |
| `cob_cuadratura` | `monto_sistema` | Monto Sistema | decimal(18,2), CLP | Monto según sistema en CLP | Obligatorio | Sin clave | `COB` | `AL`; `P30` |
| `cob_cuadratura` | `diferencia` | Diferencia | decimal(18,3) | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_cuadratura` | `estado` | Estado | string(32), catálogo | PENDIENTE, CUADRADA, CON_DIFERENCIA, APROBADA, CERRADA; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_causal` | `causal_cobro_id` | Identificador de causal cobro | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `COB` | `ME`; `P31` |
| `cob_causal` | `codigo` | Código | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Valor único | `COB` | `ME`; `P31` |
| `cob_causal` | `descripcion` | Descripción | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_causal` | `categoria` | Categoria | string(32), catálogo | Catálogo: FALTANTE, SOBRANTE, ERROR_CAPTURA, TARJETA, DIFERENCIA_FONDO | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_descuadre` | `descuadre_id` | Identificador de descuadre | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `COB` | `ME`; `P31` |
| `cob_descuadre` | `cuadratura_id` | Identificador de cuadratura | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cob_cuadratura.cuadratura_id` | `COB` | `ME`; `P31` |
| `cob_descuadre` | `causal_cobro_id` | Identificador de causal cobro | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cob_causal.causal_cobro_id` | `COB` | `ME`; `P31` |
| `cob_descuadre` | `monto` | Monto | decimal(18,2), CLP | Monto del descuadre en CLP | Obligatorio | Sin clave | `COB` | `AL`; `P30` |
| `cob_descuadre` | `estado` | Estado | string(32), catálogo | ABIERTO, INVESTIGACION, JUSTIFICADO, AUTORIZADO, RESUELTO; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_autorizacion` | `autorizacion_id` | Identificador de autorizacion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `COB` | `ME`; `P31` |
| `cob_autorizacion` | `descuadre_id` | Identificador de descuadre | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cob_descuadre.descuadre_id` | `COB` | `ME`; `P31` |
| `cob_autorizacion` | `autorizador_id` | Autorizador del movimiento de fondos | uuid, 128 bits | UUID de mae_actor.actor_id con rol financiero habilitado y distinto del ejecutor | Obligatorio antes de aprobar todo movimiento o compensación monetaria; NULL mientras esté pendiente. Una consulta no genera autorización financiera | Referencia a mae_actor.actor_id; integridad según 5-B | `COB` | `ME`; `P31` |
| `cob_autorizacion` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `cob_autorizacion` | `decision` | Decision | string(255) | PENDIENTE, APROBADA, RECHAZADA; actor segregado antes de ejecutar | Obligatorio | Sin clave | `COB` | `ME`; `P31` |
| `desp_carga` | `carga_id` | Identificador de carga | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `DOC` | `ME`; `P33` |
| `desp_carga` | `vehiculo_id` | Identificador de vehiculo | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_vehiculo.vehiculo_id` | `DOC` | `ME`; `P33` |
| `desp_carga` | `sitio_id` | Identificador de sitio | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_sitio.sitio_id`; integridad según 5-B | `DOC` | `ME`; `P33` |
| `desp_carga` | `ruta_id` | Identificador de ruta | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `rut_ruta.ruta_id` | `DOC` | `ME`; `P33` |
| `desp_carga` | `version_carga` | version de carga del vehiculo | bigint, 64 bits | Ordinal entero positivo desde 1; aumenta al modificar la carga y se compara numéricamente; aceptación documental según 5-C | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `desp_carga` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `desp_carga` | `estado` | Estado | string(32), catálogo | Catálogo: PREPARADA, DOCUMENTO_EMITIDO, HABILITADA, CERRADA | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `desp_carga` | `documento_habilitador_id` | Identificador de documento habilitador | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `doc_documento.documento_id` | `DOC` | `ME`; `P33` |
| `doc_documento` | `documento_id` | Identificador de documento | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `DOC` | `ME`; `P33` |
| `doc_documento` | `tipo` | Tipo | string(32), catálogo | Catálogo: DTE, GUIA, FACTURA | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_documento` | `folio` | Folio | string(255) | Correlativo del emisor dentro del tipo de documento; se valida junto con tipo y emisor | Obligatorio | Sin clave | `DOC` | `AL`; `P33` |
| `doc_documento` | `emisor` | Emisor | string(255) | Texto normalizado del interviniente; es dato personal cuando identifica a una persona natural | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_documento` | `hash` | Hash | string(64), SHA-256 en hexadecimal | Hexadecimal de 64 caracteres; contenido del archivo o del conjunto de objetos | Obligatorio | Sin clave | `DOC` | `AL`; `P33` |
| `doc_documento` | `receptor` | Receptor | string(255) | Texto normalizado del interviniente; es dato personal cuando identifica a una persona natural | Obligatorio | Sin clave | `DOC` | `CR`; `P34` |
| `doc_documento` | `fecha_emision` | Fecha Emision | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_documento` | `estado` | Estado | string(32), catálogo | Catálogo: EMITIDO, VALIDADO, INCERTO, ANULADO | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_documento` | `version` | version del documento ante reimpresion o anulacion | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Parte de la clave de la versión | `DOC` | `ME`; `P33` |
| `doc_documento` | `carga_id` | Identificador de carga | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `desp_carga.carga_id` | `DOC` | `ME`; `P33` |
| `doc_referencia` | `referencia_id` | Identificador de referencia | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `DOC` | `ME`; `P33` |
| `doc_referencia` | `documento_id` | Identificador de documento | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `doc_documento.documento_id` | `DOC` | `ME`; `P33` |
| `doc_referencia` | `carga_id` | Identificador de carga | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `desp_carga.carga_id` | `DOC` | `ME`; `P33` |
| `doc_referencia` | `tipo_referencia` | Tipo Referencia | string(32), catálogo | Catálogo: CARGA, PEDIDO, ENTREGA, LOTE, UNIDAD | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_referencia` | `entidad_ref_id` | referencia validada, no clave foranea distribuida | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_pod` | `pod_id` | Identificador de pod | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `DOC` | `ME`; `P33` |
| `doc_pod` | `entrega_id` | Identificador de entrega | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `rep_entrega.entrega_id`; integridad según 5-B | `DOC` | `ME`; `P33` |
| `doc_pod` | `receptor_identificacion` | Receptor Identificacion | string(255) | Texto normalizado del interviniente; es dato personal cuando identifica a una persona natural | Obligatorio | Sin clave | `DOC` | `CR`; `P34` |
| `doc_pod` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_pod` | `intento_id` | Identificador de intento | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `rep_intento.intento_id`; integridad según 5-B | `DOC` | `ME`; `P33` |
| `doc_pod` | `numero` | varias evidencias por entrega | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_pod` | `receptor_nombre` | Receptor Nombre | string(512) | Texto normalizado del interviniente; es dato personal cuando identifica a una persona natural | Obligatorio | Sin clave | `DOC` | `CR`; `P34` |
| `doc_pod` | `receptor_relacion` | Receptor Relacion | string(255) | Texto normalizado del interviniente; es dato personal cuando identifica a una persona natural | Obligatorio | Sin clave | `DOC` | `CR`; `P34` |
| `doc_pod` | `lugar` | Lugar | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_pod` | `evidencia_obj_id` | Identificador de evidencia obj | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `obj_objeto.objeto_id` | `DOC` | `ME`; `P33` |
| `doc_acuse_tecnico` | `acuse_id` | Identificador de acuse | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `DOC` | `ME`; `P33` |
| `doc_acuse_tecnico` | `documento_id` | Identificador de documento | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `doc_documento.documento_id` | `DOC` | `ME`; `P33` |
| `doc_acuse_tecnico` | `canal` | Canal | string(32), catálogo | SII, INTERCAMBIO_ERP; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_acuse_tecnico` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_acuse_tecnico` | `estado` | Estado | string(32), catálogo | PENDIENTE, ACEPTADO, RECHAZADO; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_acuse_destinatario` | `acuse_dest_id` | Identificador de acuse dest | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `DOC` | `ME`; `P33` |
| `doc_acuse_destinatario` | `documento_id` | Identificador de documento | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `doc_documento.documento_id` | `DOC` | `ME`; `P33` |
| `doc_acuse_destinatario` | `cliente_id` | Identificador de cliente | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_cliente.cliente_id`; integridad según 5-B | `DOC` | `ME`; `P33` |
| `doc_acuse_destinatario` | `perfil_destinatario` | Perfil Destinatario | string(255) | TITULAR, AUTORIZADO, NO_TITULAR, NO_SABE_FIRMAR, SE_NIEGA; recepción identificada/evidencia según S4 | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_acuse_destinatario` | `firmante` | Firmante | string(255) | Texto normalizado del interviniente; es dato personal cuando identifica a una persona natural | Obligatorio | Sin clave | `DOC` | `CR`; `P34` |
| `doc_acuse_destinatario` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `doc_acuse_destinatario` | `objeto_id` | Identificador de objeto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `obj_objeto.objeto_id` | `DOC` | `ME`; `P33` |
| `doc_acuse_destinatario` | `estado` | Estado | string(32), catálogo | PENDIENTE, RECIBIDO, RECHAZADO; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `obj_objeto` | `objeto_id` | Identificador de objeto | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `DOC` | `ME`; `P33` |
| `obj_objeto` | `clave` | Clave | string(255) | Clave única de la entrada dentro del mbito declarado por su entidad | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `obj_objeto` | `hash` | Hash | string(64), SHA-256 en hexadecimal | Hexadecimal de 64 caracteres; contenido del archivo o del conjunto de objetos | Obligatorio | Sin clave | `DOC` | `AL`; `P33` |
| `obj_objeto` | `clase_retencion` | Clase Retencion | string(32), catálogo | DOCUMENTO_POD, TRAZABILIDAD, TERMICO, GPS_PERSONAL, AUDITORIA, LOG, RESPALDO; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `obj_objeto` | `bytes` | Tamaño del objeto | bigint, unidad byte, rango no negativo | Entero no negativo; tamaño en bytes del objeto almacenado. Corresponde al tamaño efectivo del objeto referenciado. | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `obj_objeto` | `version` | Identificador textual de la versión del objeto | string(255) | Cadena no vacía de hasta 255 caracteres; coincidencia exacta, sin orden numérico ni lexicográfico para determinar vigencia | Obligatorio | Referencia a la versión concreta junto con `clave`; no sustituye la PK `objeto_id` | `DOC` | `ME`; `P33` |
| `obj_objeto` | `cifrado` | Cifrado | boolean | true: cifrado de servidor verificado; false: no cifrado; aceptación según la protección obligatoria de 5-E | Obligatorio; valor explícito, sin asumir true por defecto | Sin clave | `DOC` | `ME`; `P33` |

**Tabla A.7 - Diccionario de atributos: Cobranza, documentos,envases y objetos**

*Fuente: elaboración propia de LafroX a partir del modelo lógico de las Figuras 5.6 y 5.4 del Subdocumento 5 y A5.3 del Anexo 5-M, de RT-05.01 de las Bases Técnicas Transversales (PUCV, 2026d) y de la matriz de retención del Anexo 5-D.*

La validación aplica la condición de cada fila al hito indicado; NULL legítimo se distingue de dato obligatorio ausente.

<a id="tab-a8-dic-intercambio-gobierno"></a>

La Tabla A.8 desarrolla los atributos de EDI, notificaciones y gobierno, con sus condiciones y políticas de conservación.

| Entidad | Atributo | Significado | Tipo lógico, tamaño y precisión | Dominio, formato, catálogo o rango | Obligatoriedad y condición | Clave, referencia y unicidad | Propietario funcional | Sensibilidad, retención y control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `edi_perfil_cadena` | `perfil_id` | Identificador de perfil | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `EDI` | `ME`; `P35` |
| `edi_perfil_cadena` | `cliente_id` | Identificador de cliente | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_cliente.cliente_id`; integridad según 5-B | `EDI` | `ME`; `P35` |
| `edi_perfil_cadena` | `version` | Versión | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Parte de la clave de la versión | `EDI` | `ME`; `P35` |
| `edi_perfil_cadena` | `transporte` | Transporte | string(255) | Modo de transporte del perfil de cadena | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_perfil_cadena` | `formato` | Formato | string(255) | Formato habilitado por contrato de cadena de S4 y versión de esquema; original preservado, sin integración adicional | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_perfil_cadena` | `ventana` | Ventana | string(255) | HH:MM/HH:MM en zona del perfil; hora válida, intervalo positivo; fin anterior implica día siguiente | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_perfil_cadena` | `vigente_desde` | Vigente Desde | date | Fecha ISO 8601 de inicio del intervalo; admite vigencias futuras; selección histórica según 5-C | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_perfil_cadena` | `vigente_hasta` | nulo mientras siga vigente | date | Fecha ISO 8601; nula mientras la versión siga vigente | Condicional: nula en la versión vigente y con fecha en las cerradas | Parte de la unicidad con la fecha de inicio de vigencia | `EDI` | `ME`; `P35` |
| `edi_mensaje` | `mensaje_id` | Identificador de mensaje | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `EDI` | `ME`; `P35` |
| `edi_mensaje` | `perfil_id` | Identificador de perfil | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `edi_perfil_cadena.perfil_id` | `EDI` | `ME`; `P35` |
| `edi_mensaje` | `direccion` | Direccion | string(32), catálogo | Catálogo: ENTRADA, SALIDA | Obligatorio | Sin clave | `EDI` | `CR`; `P36` |
| `edi_mensaje` | `tipo` | Tipo | string(32), catálogo | ORDERS, ORDRSP, DESADV, INVOIC, RECADV, APERAK; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_mensaje` | `identificador` | identificador del intercambio | string(255) | Texto libre normalizado; identificador del intercambio | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_mensaje` | `clave_idempotencia` | Clave Idempotencia | string(255) | Identificador de hasta 64 caracteres generado por el emisor; con el tipo de operación permite reintentar sin duplicar el efecto | Obligatorio | Valor único | `EDI` | `ME`; `P35` |
| `edi_mensaje` | `correlacion_id` | agrupa los mensajes de una operacion | string(64) | Identificador de hasta 64 caracteres generado por el emisor; con el tipo de operación permite reintentar sin duplicar el efecto | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_mensaje` | `version` | version del esquema o del payload | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Parte de la clave de la versión | `EDI` | `ME`; `P35` |
| `edi_mensaje` | `ts_recepcion` | Marca de tiempo de recepcion | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_mensaje` | `ts_procesamiento` | Marca de tiempo de procesamiento | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_mensaje` | `estado` | Estado | string(32), catálogo | Catálogo: RECIBIDO, PROCESADO, RECHAZADO, REINTENTO | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_mensaje` | `payload_ref` | Payload Ref | string(512) | Clave del objeto íntegro original en S3_DOCS; hasta 512 caracteres, referencia verificada por hash | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_mensaje` | `payload_hash` | Payload Hash | string(64) | SHA-256 hexadecimal de 64 caracteres del mensaje original; no contenido JSON | Obligatorio | Sin clave | `EDI` | `AL`; `P35` |
| `edi_equivalencia` | `equivalencia_id` | Identificador de equivalencia | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `EDI` | `AL`; `P37` |
| `edi_equivalencia` | `perfil_id` | Identificador de perfil | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `edi_perfil_cadena.perfil_id` | `EDI` | `ME`; `P38` |
| `edi_equivalencia` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `EDI` | `ME`; `P38` |
| `edi_equivalencia` | `codigo_cadena` | Código Cadena | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Sin clave | `EDI` | `ME`; `P38` |
| `edi_asn` | `asn_id` | Identificador de asn | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `EDI` | `ME`; `P35` |
| `edi_asn` | `mensaje_id` | Identificador de mensaje | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `edi_mensaje.mensaje_id` | `EDI` | `ME`; `P35` |
| `edi_asn` | `fecha_envio` | Fecha Envio | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_asn` | `acuse` | estado del acuse del socio | string(255) | Texto libre normalizado; estado del acuse del socio | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_asn_linea` | `asn_linea_id` | Identificador de asn linea | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `EDI` | `ME`; `P35` |
| `edi_asn_linea` | `asn_id` | Identificador de asn | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `edi_asn.asn_id` | `EDI` | `ME`; `P35` |
| `edi_asn_linea` | `unidad_logistica_id` | Identificador de unidad logistica | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_unidad_logistica.unidad_logistica_id`; integridad según 5-B | `EDI` | `ME`; `P35` |
| `edi_asn_linea` | `lote_id` | Identificador de lote | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `inv_lote.lote_id`; integridad según 5-B | `EDI` | `ME`; `P35` |
| `edi_asn_linea` | `cantidad` | Cantidad | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `EDI` | `ME`; `P35` |
| `edi_asn_linea` | `unidad_id` | Identificador de unidad | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_unidad.unidad_id` | `EDI` | `ME`; `P35` |
| `not_plantilla` | `plantilla_id` | Identificador de plantilla | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `NOT` | `ME`; `P39` |
| `not_plantilla` | `tipo_aviso` | Tipo Aviso | string(32), catálogo | PEDIDO, PREPARACION, DESPACHO, ENTREGA, INCIDENCIA, COBRANZA, RETIRO; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `NOT` | `ME`; `P39` |
| `not_plantilla` | `canal` | Canal | string(32), catálogo | Catálogo: CORREO, SMS, WHATSAPP, AVISO_EN_PORTAAL | Obligatorio | Sin clave | `NOT` | `ME`; `P39` |
| `not_plantilla` | `version` | Versión | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Parte de la clave de la versión | `NOT` | `ME`; `P39` |
| `not_plantilla` | `cuerpo_ref` | contenido versionado | string(512) | Referencia versionada al cuerpo de plantilla; hasta 512 caracteres; no texto del mensaje ni contenido JSON | Obligatorio | Sin clave | `NOT` | `ME`; `P39` |
| `not_plantilla` | `vigente_desde` | Vigente Desde | date | Fecha ISO 8601 de inicio del intervalo; admite vigencias futuras; selección histórica según 5-C | Obligatorio | Sin clave | `NOT` | `ME`; `P39` |
| `not_plantilla` | `vigente_hasta` | nulo mientras siga vigente | date | Fecha ISO 8601; nula mientras la versión siga vigente | Condicional: nula en la versión vigente y con fecha en las cerradas | Parte de la unicidad con la fecha de inicio de vigencia | `NOT` | `ME`; `P39` |
| `not_preferencia` | `preferencia_id` | Identificador de preferencia | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `NOT` | `ME`; `P39` |
| `not_preferencia` | `cliente_id` | Identificador de cliente | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_cliente.cliente_id`; integridad según 5-B | `NOT` | `ME`; `P39` |
| `not_preferencia` | `plantilla_id` | Identificador de plantilla | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `not_plantilla.plantilla_id` | `NOT` | `ME`; `P39` |
| `not_preferencia` | `plantilla_version` | Plantilla Versión | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Sin clave | `NOT` | `ME`; `P39` |
| `not_preferencia` | `activa` | Activa | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `NOT` | `AL`; `P40` |
| `not_aviso` | `aviso_id` | Identificador de aviso | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `NOT` | `ME`; `P39` |
| `not_aviso` | `cliente_id` | Identificador de cliente | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_cliente.cliente_id`; integridad según 5-B | `NOT` | `ME`; `P39` |
| `not_aviso` | `entrega_id` | Identificador de entrega | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `rep_entrega.entrega_id`; integridad según 5-B | `NOT` | `ME`; `P39` |
| `not_aviso` | `plantilla_id` | Identificador de plantilla | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `not_plantilla.plantilla_id` | `NOT` | `ME`; `P39` |
| `not_aviso` | `plantilla_version` | Plantilla Versión | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Sin clave | `NOT` | `ME`; `P39` |
| `not_aviso` | `tipo` | Tipo | string(32), catálogo | PEDIDO, PREPARACION, DESPACHO, ENTREGA, INCIDENCIA, COBRANZA, RETIRO; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `NOT` | `ME`; `P39` |
| `not_aviso` | `estado` | Estado | string(32), catálogo | Catálogo: PENDIENTE, ENVIADO, CONFIRMADO, FALLIDO | Obligatorio | Sin clave | `NOT` | `ME`; `P39` |
| `not_aviso` | `clave_idempotencia` | Clave Idempotencia | string(255) | Identificador de hasta 64 caracteres generado por el emisor; con el tipo de operación permite reintentar sin duplicar el efecto | Obligatorio | Valor único | `NOT` | `ME`; `P39` |
| `not_intento` | `intento_id` | Identificador de intento | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `NOT` | `ME`; `P39` |
| `not_intento` | `aviso_id` | Identificador de aviso | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `not_aviso.aviso_id` | `NOT` | `ME`; `P39` |
| `not_intento` | `canal` | Canal | string(32), catálogo | EMAIL, SMS, PUSH; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `NOT` | `ME`; `P39` |
| `not_intento` | `fecha` | Fecha | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `NOT` | `ME`; `P39` |
| `not_intento` | `resultado` | Resultado | string(32), catálogo | PENDIENTE, ENVIADO, CONFIRMADO, FALLIDO; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `NOT` | `ME`; `P39` |
| `gob_auditoria` | `auditoria_id` | Identificador de auditoria | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `GOB` | `ME`; `P41` |
| `gob_auditoria` | `actor_id` | Identificador de actor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_actor.actor_id`; integridad según 5-B | `GOB` | `ME`; `P41` |
| `gob_auditoria` | `entidad` | Entidad | string(255) | Nombre de la entidad agregada auditada, del catálogo del modelo | Obligatorio | Sin clave | `GOB` | `ME`; `P41` |
| `gob_auditoria` | `entidad_id` | Identificador de entidad | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio | Sin clave | `GOB` | `ME`; `P41` |
| `gob_auditoria` | `operacion` | Operacion | string(32), catálogo | Catálogo: CREAR, MODIFICAR, ANULAR, CONSULTAR, EXPORTAR | Obligatorio | Sin clave | `GOB` | `ME`; `P41` |
| `gob_auditoria` | `valores_anteriores` | Valores Anteriores | jsonb | Snapshot estructurado previo, campos mínimos y datos personales según retención 5-D; excluir claves, secretos y posición vencida | Obligatorio | Sin clave | `GOB` | `CR`; `P42` |
| `gob_auditoria` | `valores_posteriores` | Valores Posteriores | jsonb | Snapshot estructurado posterior con regla/versión y resultado; campos mínimos y datos personales según 5-D | Obligatorio | Sin clave | `GOB` | `CR`; `P42` |
| `gob_auditoria` | `resultado` | Resultado | string(32), catálogo | Catálogo: OK, RECHAZADO, ERROR | Obligatorio | Sin clave | `GOB` | `ME`; `P41` |
| `gob_auditoria` | `fecha_ocurrencia` | Fecha Ocurrencia | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `GOB` | `ME`; `P41` |
| `gob_auditoria` | `fecha_registro` | Fecha Registro | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `GOB` | `ME`; `P41` |
| `gob_auditoria` | `dispositivo_id` | Identificador de dispositivo | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio | Sin clave | `GOB` | `ME`; `P41` |
| `gob_auditoria` | `transaction_id` | Identificador de transaction | string(64) | Identificador de hasta 64 caracteres generado por el emisor; con el tipo de operación permite reintentar sin duplicar el efecto | Obligatorio | Sin clave | `GOB` | `ME`; `P41` |
| `gob_auditoria` | `correlacion_id` | Identificador de correlacion | string(64) | Identificador de hasta 64 caracteres generado por el emisor; con el tipo de operación permite reintentar sin duplicar el efecto | Obligatorio | Sin clave | `GOB` | `ME`; `P41` |
| `gob_auditoria` | `consulta_sensible` | consultas y exportaciones sensibles | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `GOB` | `ME`; `P41` |
| `gob_asignacion` | `asignacion_id` | Identificador de asignacion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `GOB` | `ME`; `P26` |
| `gob_asignacion` | `actor_id` | Identificador de actor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_actor.actor_id`; integridad según 5-B | `GOB` | `ME`; `P26` |
| `gob_asignacion` | `rol` | Rol | string(255) | Rol funcional del responsable asignado, del catálogo de roles de S4 | Obligatorio | Sin clave | `GOB` | `ME`; `P26` |
| `gob_asignacion` | `sitio_id` | Identificador de sitio | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_sitio.sitio_id`; integridad según 5-B | `GOB` | `ME`; `P26` |
| `gob_asignacion` | `vigente_desde` | Vigente Desde | date | Fecha ISO 8601 de inicio del intervalo; admite vigencias futuras; selección histórica según 5-C | Obligatorio | Sin clave | `GOB` | `ME`; `P26` |
| `gob_asignacion` | `vigente_hasta` | nulo mientras siga vigente | date | Fecha ISO 8601; nula mientras la versión siga vigente | Condicional: nula en la versión vigente y con fecha en las cerradas | Parte de la unicidad con la fecha de inicio de vigencia | `GOB` | `ME`; `P26` |
| `gob_excepcion_sync` | `excepcion_id` | Identificador de excepcion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `GOB` | `ME`; `P43` |
| `gob_excepcion_sync` | `tipo` | Tipo | string(32), catálogo | DUPLICADO, CONFLICTO_VERSION, GAP_VERSION, REFERENCIA_AUSENTE, VALIDACION, PAGO_INCIERTO; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `GOB` | `ME`; `P43` |
| `gob_excepcion_sync` | `clave` | Clave | string(255) | Clave única de la entrada dentro del mbito declarado por su entidad | Obligatorio | Sin clave | `GOB` | `ME`; `P43` |
| `gob_excepcion_sync` | `correlacion_id` | Identificador de correlacion | string(64) | Identificador de hasta 64 caracteres generado por el emisor; con el tipo de operación permite reintentar sin duplicar el efecto | Obligatorio | Sin clave | `GOB` | `ME`; `P43` |
| `gob_excepcion_sync` | `payload` | Contenido que provocó la decisión | jsonb | JSON histórico de entrada, actor/dispositivo, valores previos pertinentes, decisión, regla y versión; máximo 256 KiB serializado como límite de diseño. Exceso: rechazo tipificado y referencia a objeto íntegro con hash, misma retención; no se sustituye por estado mutable actual | Condicional: obligatorio cuando la excepción se origina en un conflicto de datos; puede ser nulo cuando la decisión se funda solo en el estado de las entidades, y en ese caso la regla aplicada y su versión bastan para reconstruirla | Sin clave | `GOB` | `ME`; `P43` |
| `gob_excepcion_sync` | `version` | Versión | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Parte de la clave de la versión | `GOB` | `ME`; `P43` |
| `gob_excepcion_sync` | `regla_aplicada` | Regla Aplicada | string(255) | Código de regla versionada de 5-C/mae_parametro_version; debe existir en la versión del snapshot, no solo en estado actual | Obligatorio | Sin clave | `GOB` | `ME`; `P43` |
| `gob_excepcion_sync` | `regla_version` | Versión de la regla aplicada | integer, 32 bits | Entero desde 1. El tipo es entero porque el número de versión de una regla es un correlativo, y el dominio coincide con el tipo | Obligatorio | Sin clave | `GOB` | `ME`; `P43` |
| `gob_excepcion_sync` | `decision` | Decision | string(255) | RETENER, REINTENTAR, RECHAZAR, ACEPTAR_IDEMPOTENTE, CONCILIAR; regla/versionado y snapshot obligatorios | Obligatorio | Sin clave | `GOB` | `ME`; `P43` |
| `gob_excepcion_sync` | `estado` | Estado | string(32), catálogo | Catálogo: ABIERTA, RESUELTA, RECHAZADA | Obligatorio | Sin clave | `GOB` | `ME`; `P43` |
| `gob_excepcion_sync` | `responsable` | Responsable | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `GOB` | `ME`; `P43` |
| `gob_excepcion_sync` | `fecha` | Fecha de registro de la excepción | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `GOB` | `ME`; `P43` |
| `gob_excepcion_sync` | `fecha_cierre` | Instante de resolución de la excepción | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Condicional: obligatoria cuando la excepción pasa a RESUELTA o RECHAZADA, porque en esos dos estados la decisión está tomada; nula mientras la excepción siga ABIERTA | Sin clave | `GOB` | `ME`; `P43` |

**Tabla A.8 - Diccionario de atributos: Intercambio electrónico, notificación y gobierno del acceso**

*Fuente: elaboración propia de LafroX a partir del modelo lógico de la Figura A5.2 del Anexo 5-M, de RT-05.01 de las Bases Técnicas Transversales (PUCV, 2026d) y de la matriz de retención del Anexo 5-D.*

La validación aplica la condición de cada fila al hito indicado; NULL legítimo se distingue de dato obligatorio ausente.

<a id="tab-a9-dic-telemetria-cache"></a>

La Tabla A.9 desarrolla los atributos de telemetría y copias de consulta, con sus condiciones y políticas de conservación.

| Entidad | Atributo | Significado | Tipo lógico, tamaño y precisión | Dominio, formato, catálogo o rango | Obligatoriedad y condición | Clave, referencia y unicidad | Propietario funcional | Sensibilidad, retención y control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `tel_lectura_cruda` | `sensor_id` | Identificador de sensor | uuid, 128 bits | UUID del sensor registrado en `cal_sensor`; debe existir y estar vigente al escribir la lectura | Obligatorio, clave primaria | Clave primaria; además referencia a `cal_sensor.sensor_id` (contrato entre almacenes) | `TEL` | `ME`; `P44` |
| `tel_lectura_cruda` | `ts_medicion` | Marca de tiempo de medicion | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio, clave primaria | Clave primaria | `TEL` | `ME`; `P44` |
| `tel_lectura_cruda` | `valor` | Valor | decimal(18,3), °C | Valor de temperatura de lectura cruda; precisión definida por sensor y calibración vigentes | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `TEL` | `ME`; `P45` |
| `tel_lectura_cruda` | `unidad` | Unidad | string(32), catálogo | Unidad de medida registrada en `mae_unidad`; no es texto libre | Obligatorio | Sin clave | `TEL` | `ME`; `P44` |
| `tel_lectura_cruda` | `expira_en` | treinta dias | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `TEL` | `ME`; `P44` |
| `tel_lectura_cruda` | `origen` | Origen | string(32), catálogo | CAMARA, TERMOGRAFO_VEHICULO; procedencia real, sensor y tiempo | Obligatorio | Sin clave | `TEL` | `ME`; `P44` |
| `tel_archivo_termino` | `archivo_id` | Identificador de archivo | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `TEL` | `ME`; `P46` |
| `tel_archivo_termino` | `sensor_id` | Identificador de sensor | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `cal_sensor.sensor_id`; integridad según 5-B | `TEL` | `ME`; `P46` |
| `tel_archivo_termino` | `ventana_id` | ventana de exposicion asociada | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cal_asociacion_ventana.ventana_id` | `TEL` | `ME`; `P46` |
| `tel_archivo_termino` | `calibracion_id` | Identificador de calibracion | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cal_calibracion.calibracion_id` | `TEL` | `ME`; `P46` |
| `tel_archivo_termino` | `regla_id` | regla vigente al medir | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `cal_regla_termica.regla_id` | `TEL` | `ME`; `P46` |
| `tel_archivo_termino` | `ts_medicion` | Marca de tiempo de medicion | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `TEL` | `ME`; `P46` |
| `tel_archivo_termino` | `valor` | Valor | decimal(18,3), °C | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `TEL` | `AL`; `P47` |
| `tel_archivo_termino` | `unidad` | Unidad | string(32), catálogo | Unidad de medida registrada en `mae_unidad`; no es texto libre | Obligatorio | Sin clave | `TEL` | `ME`; `P46` |
| `tel_archivo_termino` | `hash_evidencia` | Hash Evidencia | string(64), SHA-256 en hexadecimal | Hexadecimal de 64 caracteres; contenido del archivo o del conjunto de objetos | Obligatorio | Sin clave | `TEL` | `AL`; `P46` |
| `tel_archivo_termino` | `desde_retencion` | cinco anos | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `TEL` | `ME`; `P46` |
| `tel_serie_consolidada` | `sensor_id` | Identificador de sensor | uuid, 128 bits | UUID del sensor registrado en `cal_sensor`; debe existir y estar vigente al escribir la lectura | Obligatorio, clave primaria | Clave primaria; además referencia a `cal_sensor.sensor_id` (contrato entre almacenes) | `TEL` | `ME`; `P46` |
| `tel_serie_consolidada` | `fecha` | Fecha | date | Fecha ISO 8601 del día local consolidado, derivada de las mediciones en la zona IANA del sitio | Obligatorio, clave primaria | Clave primaria | `TEL` | `ME`; `P46` |
| `tel_serie_consolidada` | `producto_id` | Identificador de producto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Referencia a `mae_producto.producto_id`; integridad según 5-B | `TEL` | `ME`; `P46` |
| `tel_serie_consolidada` | `valor_min` | Valor Min | decimal(18,3), °C | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `TEL` | `AL`; `P47` |
| `tel_serie_consolidada` | `valor_max` | Valor Max | decimal(18,3), °C | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `TEL` | `AL`; `P47` |
| `tel_serie_consolidada` | `valor_promedio` | Valor Promedio | decimal(18,3), °C | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `TEL` | `AL`; `P47` |
| `tel_serie_consolidada` | `lecturas` | Lecturas | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Sin clave | `TEL` | `ME`; `P46` |
| `tel_posicion_gps` | `posicion_id` | Identificador de posicion | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `TEL` | `CR`; `P48` |
| `tel_posicion_gps` | `vehiculo_id` | Identificador de vehiculo | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `mae_vehiculo.vehiculo_id` | `TEL` | `ME`; `P48` |
| `tel_posicion_gps` | `ts_posicion` | Marca de tiempo de posicion | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `TEL` | `CR`; `P48` |
| `tel_posicion_gps` | `punto` | Punto | geometry(Point, 4326) | Punto georreferenciado en WGS 84 (EPSG:4326), en el sistema de referencia declarado por el sitio | Obligatorio | Sin clave | `TEL` | `ME`; `P48` |
| `tel_posicion_gps` | `fuente` | Fuente | string(32), catálogo | Catálogo: GPS, CELULAR | Obligatorio | Sin clave | `TEL` | `ME`; `P48` |
| `tel_posicion_gps` | `sensibilidad` | Sensibilidad | string(255) | Precisión estimada del punto, del catálogo de la fuente de posicionamiento | Obligatorio | Sin clave | `TEL` | `CR`; `P49` |
| `tel_posicion_gps` | `region_residencia` | residencia de referencia | string(255) | Texto libre normalizado; residencia de referencia | Obligatorio | Sin clave | `TEL` | `CR`; `P49` |
| `cache_stock` | `clave` | Clave | string(255) | Clave de stock: sitio+ubicación+producto+lote+unidad de medida+versión; lote NULL se representa explícitamente sin omitir producto | Obligatorio, clave primaria | Clave primaria | `DER` | `ME`; `P50` |
| `cache_stock` | `valor` | Valor | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad o moneda declarada por la clave | Obligatorio | Sin clave | `DER` | `ME`; `P51` |
| `cache_stock` | `version` | Versión | integer, 32 bits | Entero creciente desde 1; la mayor es la versión vigente | Obligatorio | Parte de la clave de la versión | `DER` | `ME`; `P50` |
| `cache_stock` | `vigente_desde` | Vigente Desde | timestamp with time zone, UTC | Instante ISO 8601 en UTC en que la versión.cache se publicó | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_stock` | `expira_en` | Expira En | timestamp with time zone, UTC | Instante ISO 8601 en UTC; la entrada deja de ser válida en ese instante | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_stock` | `invalida_por` | Invalida Por | string(32), catálogo | Catálogo de motivos: SALDO, TARIFA, CREDITO, MANIFIESTO | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_stock` | `origen` | Origen | string(32), catálogo | Texto o número normalizado definido por la entrada | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_precio` | `clave` | Clave | string(255) | Identificador de la entrada; tabla e identidad se declaran en el Anexo 5-G | Obligatorio, clave primaria | Clave primaria | `DER` | `ME`; `P50` |
| `cache_precio` | `valor` | Valor | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad o moneda declarada por la clave | Obligatorio | Sin clave | `DER` | `ME`; `P51` |
| `cache_precio` | `version` | Versión | integer, 32 bits | Entero creciente desde 1; la mayor es la versión vigente | Obligatorio | Parte de la clave de la versión | `DER` | `ME`; `P50` |
| `cache_precio` | `vigente_desde` | Vigente Desde | timestamp with time zone, UTC | Instante ISO 8601 en UTC en que la versión.cache se publicó | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_precio` | `expira_en` | Expira En | timestamp with time zone, UTC | Instante ISO 8601 en UTC; la entrada deja de ser válida en ese instante | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_precio` | `invalida_por` | Invalida Por | string(32), catálogo | Catálogo de motivos: SALDO, TARIFA, CREDITO, MANIFIESTO | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_precio` | `origen` | Origen | string(32), catálogo | Texto o número normalizado definido por la entrada | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_credito` | `clave` | Clave | string(255) | Identificador de la entrada; tabla e identidad se declaran en el Anexo 5-G | Obligatorio, clave primaria | Clave primaria | `DER` | `AL`; `P50` |
| `cache_credito` | `valor` | Valor | decimal(18,2), CLP | Saldo de crédito indicativo en CLP; versión de autoridad, sin validar cobro desde caché | Obligatorio | Sin clave | `DER` | `AL`; `P51` |
| `cache_credito` | `version` | Versión | integer, 32 bits | Entero creciente desde 1; la mayor es la versión vigente | Obligatorio | Parte de la clave de la versión | `DER` | `AL`; `P50` |
| `cache_credito` | `vigente_desde` | Vigente Desde | timestamp with time zone, UTC | Instante ISO 8601 en UTC en que la versión.cache se publicó | Obligatorio | Sin clave | `DER` | `AL`; `P50` |
| `cache_credito` | `expira_en` | Expira En | timestamp with time zone, UTC | Instante ISO 8601 en UTC; la entrada deja de ser válida en ese instante | Obligatorio | Sin clave | `DER` | `AL`; `P50` |
| `cache_credito` | `invalida_por` | Invalida Por | string(32), catálogo | Catálogo de motivos: SALDO, TARIFA, CREDITO, MANIFIESTO | Obligatorio | Sin clave | `DER` | `AL`; `P50` |
| `cache_credito` | `origen` | Origen | string(32), catálogo | Texto o número normalizado definido por la entrada | Obligatorio | Sin clave | `DER` | `AL`; `P50` |
| `cache_identidad` | `actor_id` | Identificador de actor | uuid, 128 bits | Texto o número normalizado definido por la entrada | Obligatorio, clave primaria | Clave primaria | `DER` | `ME`; `P50` |
| `cache_identidad` | `rol` | Rol | string(255) | Texto o número normalizado definido por la entrada | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_identidad` | `permisos` | Permisos | JSON, documento de consulta | Permisos preemitidos por Keycloak con versión, vigencia y firma; solo lectura, sin crear autorización offline | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_identidad` | `manifiesto_version` | Manifiesto Versión | integer, 32 bits | Texto o número normalizado definido por la entrada | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_identidad` | `expira_en` | Expira En | timestamp with time zone, UTC | Instante ISO 8601 en UTC; la entrada deja de ser válida en ese instante | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_identidad` | `ultima_sync` | Ultima sincronización | timestamp with time zone, UTC | Texto o número normalizado definido por la entrada | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_manifiesto` | `clave` | manifiesto y version | string(255) | Identificador de la entrada; tabla e identidad se declaran en el Anexo 5-G | Obligatorio, clave primaria | Clave primaria | `DER` | `ME`; `P50` |
| `cache_manifiesto` | `version` | Versión | integer, 32 bits | Entero creciente desde 1; la mayor es la versión vigente | Obligatorio | Parte de la clave de la versión | `DER` | `ME`; `P50` |
| `cache_manifiesto` | `hash_firma` | firma del manifiesto | string(64), SHA-256 en hexadecimal | Texto o número normalizado definido por la entrada | Obligatorio | Sin clave | `DER` | `ME`; `P52` |
| `cache_manifiesto` | `firmante` | Firmante | string(255) | Texto o número normalizado definido por la entrada | Obligatorio | Sin clave | `DER` | `ME`; `P52` |
| `cache_manifiesto` | `emitido_en` | Emitido En | timestamp with time zone, UTC | Texto o número normalizado definido por la entrada | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_manifiesto` | `expira_en` | Expira En | timestamp with time zone, UTC | Instante ISO 8601 en UTC; la entrada deja de ser válida en ese instante | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `cache_manifiesto` | `estado` | Estado | string(32), catálogo | Texto o número normalizado definido por la entrada | Obligatorio | Sin clave | `DER` | `ME`; `P50` |
| `obj_manifiesto` | `manifiesto_id` | Identificador de manifiesto | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `DOC` | `ME`; `P33` |
| `obj_manifiesto` | `tipo` | Tipo | string(32), catálogo | Catálogo: EVIDENCIA, RETIRO, EXPORTACION, DOCUMENTO | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `obj_manifiesto` | `hash_manifiesto` | Hash Manifiesto | string(64), SHA-256 en hexadecimal | Hexadecimal de 64 caracteres; contenido del archivo o del conjunto de objetos | Obligatorio | Sin clave | `DOC` | `AL`; `P33` |
| `obj_manifiesto` | `registros` | Registros | integer, 32 bits | Entero dentro del rango del tipo; negativo solo en una diferencia o un descuadre declarado | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `obj_manifiesto` | `generado_en` | Generado En | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `obj_manifiesto_linea` | `linea_id` | Identificador de linea | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `DOC` | `ME`; `P33` |
| `obj_manifiesto_linea` | `manifiesto_id` | Identificador de manifiesto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `obj_manifiesto.manifiesto_id` | `DOC` | `ME`; `P33` |
| `obj_manifiesto_linea` | `objeto_id` | Identificador de objeto | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `obj_objeto.objeto_id` | `DOC` | `ME`; `P33` |
| `obj_manifiesto_linea` | `hash_linea` | Hash Línea | string(64), SHA-256 en hexadecimal | Hexadecimal de 64 caracteres; contenido del archivo o del conjunto de objetos | Obligatorio | Sin clave | `DOC` | `AL`; `P33` |
| `obj_manifiesto_linea` | `bytes` | Tamaño del objeto en línea | bigint, unidad byte, rango no negativo | Entero no negativo; tamaño en bytes correspondiente al objeto asociado a la línea del manifiesto | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |
| `obj_manifiesto_linea` | `orden` | Orden | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Sin clave | `DOC` | `ME`; `P33` |

**Tabla A.9 - Diccionario de atributos: Telemetría, caché de lectura y objetos del dispositivo**

*Fuente: elaboración propia de LafroX a partir del modelo lógico de la Figura A5.3 del Anexo 5-M, de RT-05.01 de las Bases Técnicas Transversales (PUCV, 2026d) y de la matriz de retención del Anexo 5-D.*

La validación aplica la condición de cada fila al hito indicado; NULL legítimo se distingue de dato obligatorio ausente.

<a id="tab-a10-dic-analitico"></a>

La Tabla A.10 desarrolla los atributos de hechos y dimensiones analíticas, con sus condiciones y políticas de conservación.

| Entidad | Atributo | Significado | Tipo lógico, tamaño y precisión | Dominio, formato, catálogo o rango | Obligatoriedad y condición | Clave, referencia y unicidad | Propietario funcional | Sensibilidad, retención y control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `dim_fecha` | `fecha_key` | Fecha Key | date | Fecha ISO 8601 del calendario de negocio; admite días pasados, presentes y futuros | Obligatorio, clave primaria | Clave primaria | `ANA` | `ME`; `P53` |
| `dim_fecha` | `anio` | Anio | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_fecha` | `mes` | Mes | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_fecha` | `dia_semana` | Dia Semana | integer, 32 bits | Entero dentro del rango del tipo; negativo solo en una diferencia o un descuadre declarado | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_fecha` | `festivo` | Festivo | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `ANA` | `ME`; `P53` |
| `dim_fecha` | `estacion` | Estacion | string(255) | VERANO, OTONO, INVIERNO, PRIMAVERA; derivación calendárica austral documentada | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_cliente` | `cliente_sk` | Cliente Sk | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `ANA` | `ME`; `P53` |
| `dim_cliente` | `cliente_id` | clave de negocio; admite varias versiones | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_cliente` | `version` | Versión | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Parte de la clave de la versión | `ANA` | `ME`; `P53` |
| `dim_cliente` | `vigente_desde` | Vigente Desde | date | Fecha ISO 8601 de inicio del intervalo; admite vigencias futuras; selección histórica según 5-C | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_cliente` | `vigente_hasta` | nulo en la version vigente | date | Fecha ISO 8601; nula mientras la versión siga vigente | Condicional: nula en la versión vigente y con fecha en las cerradas | Parte de la unicidad con la fecha de inicio de vigencia | `ANA` | `ME`; `P53` |
| `dim_cliente` | `vigente` | Vigente | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Condicional: con la condición que declara el dominio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_cliente` | `razon_social` | Razón Social | string(255) | Razón social del interviniente con la grafía del documento oficial | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_cliente` | `canal` | Canal | string(32), catálogo | TRADICIONAL, MODERNO, FOOD_SERVICE, CADENA, HORECA; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_cliente` | `comuna` | Comuna | string(255) | Valor del catálogo territorial aprobado del CLIENTE; hasta 255 caracteres; conservar código/versión de origen y validar equivalencia | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_cliente` | `region` | Region | string(255) | Valor del catálogo territorial aprobado del CLIENTE; hasta 255 caracteres; conservar código/versión de origen y validar equivalencia | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_producto` | `producto_sk` | Producto Sk | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `ANA` | `ME`; `P53` |
| `dim_producto` | `producto_id` | clave de negocio; admite varias versiones | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_producto` | `version` | Versión | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Parte de la clave de la versión | `ANA` | `ME`; `P53` |
| `dim_producto` | `vigente_desde` | Vigente Desde | date | Fecha ISO 8601 de inicio del intervalo; admite vigencias futuras; selección histórica según 5-C | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_producto` | `vigente_hasta` | nulo en la version vigente | date | Fecha ISO 8601; nula mientras la versión siga vigente | Condicional: nula en la versión vigente y con fecha en las cerradas | Parte de la unicidad con la fecha de inicio de vigencia | `ANA` | `ME`; `P53` |
| `dim_producto` | `gtin` | Gtin | string(14), GTIN GS1 | GTIN de 8, 12, 13 o 14 dígitos con dígito verificador válido | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_producto` | `descripcion` | Descripción | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_producto` | `familia` | Familia | string(255) | Familia aprobada del maestro de producto; versión de origen, sin clasificación inventada | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_producto` | `rango_termico` | Rango Termico | string(255) | Representación del mínimo/máximo/unidad de la regla térmica vigente al hecho; mínimo < máximo | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_sitio` | `sitio_sk` | Sitio Sk | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `ANA` | `ME`; `P53` |
| `dim_sitio` | `sitio_id` | clave de negocio; admite varias versiones | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_sitio` | `version` | Versión | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Parte de la clave de la versión | `ANA` | `ME`; `P53` |
| `dim_sitio` | `vigente_desde` | Vigente Desde | date | Fecha ISO 8601 de inicio del intervalo; admite vigencias futuras; selección histórica según 5-C | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_sitio` | `vigente_hasta` | nulo en la version vigente | date | Fecha ISO 8601; nula mientras la versión siga vigente | Condicional: nula en la versión vigente y con fecha en las cerradas | Parte de la unicidad con la fecha de inicio de vigencia | `ANA` | `ME`; `P53` |
| `dim_sitio` | `codigo` | Código | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_sitio` | `tipo` | Tipo | string(32), catálogo | CENTRO_DISTRIBUCION, CROSS_DOCKING, CASA_MATRIZ, INSTALACION_CLIENTE; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_sitio` | `region` | Region | string(255) | Valor del catálogo territorial aprobado del CLIENTE; hasta 255 caracteres; conservar código/versión de origen y validar equivalencia | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_ruta` | `ruta_sk` | Ruta Sk | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `ANA` | `ME`; `P53` |
| `dim_ruta` | `version` | Versión | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Parte de la clave de la versión | `ANA` | `ME`; `P53` |
| `dim_ruta` | `vigente_desde` | Vigente Desde | date | Fecha ISO 8601 de inicio del intervalo; admite vigencias futuras; selección histórica según 5-C | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_ruta` | `vigente_hasta` | nulo en la version vigente | date | Fecha ISO 8601; nula mientras la versión siga vigente | Condicional: nula en la versión vigente y con fecha en las cerradas | Parte de la unicidad con la fecha de inicio de vigencia | `ANA` | `ME`; `P53` |
| `dim_ruta` | `fecha` | Fecha | date | Fecha ISO 8601 programada de la ruta en el calendario del sitio; admite rutas históricas y futuras | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_ruta` | `conductor_nombre` | Conductor Nombre | string(512) | Nombre del conductor asignado, del maestro `mae_actor`; es dato personal | Obligatorio | Sin clave | `ANA` | `CR`; `P54` |
| `dim_ruta` | `vehiculo_patente` | Vehículo Patente | string(255) | Patente vigente en Chile, sin guiones ni caracteres especiales | Obligatorio | Sin clave | `ANA` | `CR`; `P54` |
| `dim_ruta` | `tipo_servicio` | Tipo Servicio | string(32), catálogo | URBANO, RURAL, PERIFERICO, CROSS_DOCKING; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `dim_canal` | `canal_sk` | Canal Sk | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `ANA` | `ME`; `P53` |
| `dim_canal` | `codigo` | Código | string(64) | Texto normalizado, sin espacios iniciales o finales ni duplicados | Obligatorio | Valor único | `ANA` | `ME`; `P53` |
| `dim_canal` | `descripcion` | Descripción | string(512) | Texto libre normalizado, hasta 512 caracteres, con el detalle que exige el registro | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega` | `entrega_sk` | Entrega Sk | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `ANA` | `ME`; `P53` |
| `hech_entrega` | `entrega_id` | clave de origen: una entrega, una fila | uuid, 128 bits | UUID de rep_entrega cuando existe; no se genera una entrega ficticia | Condicional: NULL mientras el pedido no tenga entrega operativa | Valor único cuando existe | `ANA` | `ME`; `P53` |
| `hech_entrega` | `pedido_id` | un pedido comprometido, una fila | uuid, 128 bits | UUID del pedido comprometido de origen, preservado en la carga | Obligatorio | Valor único; una fila por pedido comprometido | `ANA` | `ME`; `P53` |
| `hech_entrega` | `cliente_sk` | Cliente Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `dim_cliente.cliente_sk` | `ANA` | `ME`; `P53` |
| `hech_entrega` | `sitio_sk` | Sitio Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `dim_sitio.sitio_sk` | `ANA` | `ME`; `P53` |
| `hech_entrega` | `ruta_sk` | Ruta Sk | uuid, 128 bits | UUID del registro referenciado | Condicional: NULL mientras no exista ruta asignada; válida cuando se informa | Clave foránea a `dim_ruta.ruta_sk` | `ANA` | `ME`; `P53` |
| `hech_entrega` | `fecha_key` | Fecha Key | date | Fecha ISO 8601 de negocio del hecho; derivación del origen y zona del sitio según 5-H; no es la fecha de carga ETL | Obligatorio; referencia válida | Clave foránea a `dim_fecha.fecha_key` | `ANA` | `ME`; `P53` |
| `hech_entrega` | `fecha_promesa_original` | Fecha Promesa Original | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio para el pedido comprometido; ORIGINAL inmutable, disponible aun sin entrega | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega` | `fecha_entrega_real` | nula si no hubo entrega | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Condicional: nula cuando el hecho aún no se ha producido o el dato no existe | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega` | `minutos_promesa` | Minutos Promesa | integer, 32 bits | Entero dentro del rango del tipo; negativo solo en una diferencia o un descuadre declarado | Condicional: NULL si faltan los instantes de origen necesarios para calcular el plazo | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega` | `minutos_retraso` | Minutos Retraso | integer, 32 bits | Entero dentro del rango del tipo; negativo solo en una diferencia o un descuadre declarado | Condicional: NULL sin entrega real; no se imputa retraso cero | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega` | `completa` | Completa | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega` | `a_tiempo` | A Tiempo | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega` | `con_devolucion` | Con Devolución | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega` | `estado_entrega` | Estado Entrega | string(32), catálogo | Catálogo: ENTREGADA, PARCIAL, DEVUELTA, NO_ENTREGADA | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega` | `importe` | Importe | decimal(18,2), CLP | Importe monetario en CLP | Obligatorio | Sin clave | `ANA` | `AL`; `P55` |
| `hech_entrega` | `moneda` | Moneda | string(32), catálogo | CLP; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega_intento` | `intento_sk` | Intento Sk | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `ANA` | `ME`; `P53` |
| `hech_entrega_intento` | `intento_id` | clave de origen | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio | Valor único | `ANA` | `ME`; `P53` |
| `hech_entrega_intento` | `entrega_sk` | Entrega Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `hech_entrega.entrega_sk` | `ANA` | `ME`; `P53` |
| `hech_entrega_intento` | `numero_intento` | Numero Intento | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega_intento` | `cliente_sk` | Cliente Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `dim_cliente.cliente_sk` | `ANA` | `ME`; `P53` |
| `hech_entrega_intento` | `fecha_key` | Fecha Key | date | Fecha ISO 8601 de negocio del hecho; derivación del origen y zona del sitio según 5-H; no es la fecha de carga ETL | Obligatorio; referencia válida | Clave foránea a `dim_fecha.fecha_key` | `ANA` | `ME`; `P53` |
| `hech_entrega_intento` | `fecha_intento` | Fecha Intento | timestamp with time zone, UTC | Instante ISO 8601 en UTC, con zona horaria explícita | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega_intento` | `resultado` | Resultado | string(32), catálogo | ENTREGADO, ENTREGA_PARCIAL, NO_CONTACTO, RECHAZADO_POR_CLIENTE, NO_ENTREGADO_POR_CAUSAL; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_entrega_intento` | `minutos_desde_promesa` | Minutos Desde Promesa | integer, 32 bits | Entero dentro del rango del tipo; negativo solo en una diferencia o un descuadre declarado | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_linea_venta` | `linea_venta_sk` | Línea Venta Sk | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `ANA` | `ME`; `P53` |
| `hech_linea_venta` | `linea_id` | clave de origen | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio | Valor único | `ANA` | `ME`; `P53` |
| `hech_linea_venta` | `pedido_id` | Identificador de pedido | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_linea_venta` | `cliente_sk` | Cliente Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `dim_cliente.cliente_sk` | `ANA` | `ME`; `P53` |
| `hech_linea_venta` | `producto_sk` | Producto Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `dim_producto.producto_sk` | `ANA` | `ME`; `P53` |
| `hech_linea_venta` | `canal_sk` | Canal Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `dim_canal.canal_sk` | `ANA` | `ME`; `P53` |
| `hech_linea_venta` | `fecha_key` | Fecha Key | date | Fecha ISO 8601 de negocio del hecho; derivación del origen y zona del sitio según 5-H; no es la fecha de carga ETL | Obligatorio; referencia válida | Clave foránea a `dim_fecha.fecha_key` | `ANA` | `ME`; `P53` |
| `hech_linea_venta` | `cantidad_solicitada` | Cantidad Solicitada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_linea_venta` | `cantidad_entregada` | Cantidad Entregada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio, admite cero; no puede superar la cantidad de referencia | Sin clave | `ANA` | `ME`; `P53` |
| `hech_linea_venta` | `cantidad_rechazada` | Cantidad Rechazada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio, admite cero; no puede superar la cantidad de referencia | Sin clave | `ANA` | `ME`; `P53` |
| `hech_linea_venta` | `importe` | Importe | decimal(18,2), CLP | Importe monetario en CLP | Obligatorio | Sin clave | `ANA` | `AL`; `P55` |
| `hech_linea_venta` | `moneda` | Moneda | string(32), catálogo | CLP; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_movimiento_stock` | `movimiento_sk` | Movimiento Sk | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `ANA` | `ME`; `P53` |
| `hech_movimiento_stock` | `movimiento_id` | clave de origen | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio | Valor único | `ANA` | `ME`; `P53` |
| `hech_movimiento_stock` | `sitio_sk` | Sitio Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `dim_sitio.sitio_sk` | `ANA` | `ME`; `P53` |
| `hech_movimiento_stock` | `producto_sk` | Producto Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `dim_producto.producto_sk` | `ANA` | `ME`; `P53` |
| `hech_movimiento_stock` | `fecha_key` | Fecha Key | date | Fecha ISO 8601 de negocio del hecho; derivación del origen y zona del sitio según 5-H; no es la fecha de carga ETL | Obligatorio; referencia válida | Clave foránea a `dim_fecha.fecha_key` | `ANA` | `ME`; `P53` |
| `hech_movimiento_stock` | `tipo_movimiento` | Tipo Movimiento | string(32), catálogo | RECEPCION, SALIDA, TRASLADO, AJUSTE, ANULACION; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_movimiento_stock` | `cantidad` | Cantidad | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_movimiento_stock` | `unidad_medida` | Unidad Medida | string(255) | Unidad de medida registrada en `mae_unidad`; no es texto libre | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_actividad_costo` | `actividad_costo_sk` | Actividad Costo Sk | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `ANA` | `AL`; `P55` |
| `hech_actividad_costo` | `entrega_id` | clave de origen del coste asignado | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_actividad_costo` | `entrega_sk` | Entrega Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `hech_entrega.entrega_sk` | `ANA` | `ME`; `P53` |
| `hech_actividad_costo` | `cliente_sk` | Cliente Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `dim_cliente.cliente_sk` | `ANA` | `ME`; `P53` |
| `hech_actividad_costo` | `ruta_sk` | Ruta Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `dim_ruta.ruta_sk` | `ANA` | `ME`; `P53` |
| `hech_actividad_costo` | `sitio_sk` | Sitio Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `dim_sitio.sitio_sk` | `ANA` | `ME`; `P53` |
| `hech_actividad_costo` | `fecha_key` | Fecha Key | date | Fecha ISO 8601 de negocio del hecho; derivación del origen y zona del sitio según 5-H; no es la fecha de carga ETL | Obligatorio; referencia válida | Clave foránea a `dim_fecha.fecha_key` | `ANA` | `ME`; `P53` |
| `hech_actividad_costo` | `centro_costo` | Centro Costo | string(64) | Código de centro de costo proveniente de maestro. No es un importe monetario. | Obligatorio | Sin clave | `ANA` | `AL`; `P55` |
| `hech_actividad_costo` | `criterio_asignacion` | Criterio Asignación | string(32), catálogo | Catálogo: KILOMETRAJE, TIEMPO, ENTREGA, PESO | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_actividad_costo` | `importe_costo` | Importe Costo | decimal(18,2), CLP | Importe monetario en CLP | Obligatorio | Sin clave | `ANA` | `AL`; `P55` |
| `hech_actividad_costo` | `km_recorridos` | Km Recorridos | decimal(18,6) | Numérico no negativo en kilómetros, tres decimales | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_actividad_costo` | `minutos_ruta` | Minutos Ruta | integer, 32 bits | Entero dentro del rango del tipo; negativo solo en una diferencia o un descuadre declarado | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_actividad_costo` | `cantidad_entregada` | Cantidad Entregada | decimal(18,3) | Numérico no negativo, tres decimales, en la unidad de medida declarada | Obligatorio, admite cero; no puede superar la cantidad de referencia | Sin clave | `ANA` | `ME`; `P53` |
| `hech_actividad_costo` | `envases_retornados` | Envases Retornados | integer, 32 bits | Entero no negativo; cero admitido en un conteo, una cantidad o una secuencia | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_actividad_costo` | `importe_devoluciones` | Importe Devoluciones | decimal(18,2), CLP | Importe monetario en CLP | Obligatorio | Sin clave | `ANA` | `AL`; `P55` |
| `hech_excursion` | `excursion_sk` | Excursión Sk | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio, clave primaria | Clave primaria | `ANA` | `ME`; `P53` |
| `hech_excursion` | `excursion_id` | clave de origen | uuid, 128 bits | UUID generado; independiente del código comercial | Obligatorio | Valor único | `ANA` | `ME`; `P53` |
| `hech_excursion` | `producto_sk` | Producto Sk | uuid, 128 bits | UUID del registro referenciado | Obligatorio; referencia válida | Clave foránea a `dim_producto.producto_sk` | `ANA` | `ME`; `P53` |
| `hech_excursion` | `fecha_key` | Fecha Key | date | Fecha ISO 8601 de negocio del hecho; derivación del origen y zona del sitio según 5-H; no es la fecha de carga ETL | Obligatorio; referencia válida | Clave foránea a `dim_fecha.fecha_key` | `ANA` | `ME`; `P53` |
| `hech_excursion` | `magnitud` | Magnitud | decimal(18,6) | Numérico con la precisión declarada en la columna de tipo; no admite dígitos no significativos | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_excursion` | `duracion_minutos` | Duracion Minutos | integer, 32 bits | Entero dentro del rango del tipo; negativo solo en una diferencia o un descuadre declarado | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_excursion` | `severidad` | Severidad | string(32), catálogo | MENOR, CRITICA; validación y rechazo DOMINIO_NO_ADMITIDO según 5-C | Obligatorio | Sin clave | `ANA` | `ME`; `P53` |
| `hech_excursion` | `con_bloqueo` | Con Bloqueo | boolean | Verdadero o falso explícito y validado; sin convertir desconocido en falso | Obligatorio; valor explícito sin default de dato desconocido | Sin clave | `ANA` | `ME`; `P53` |

**Tabla A.10 - Diccionario de atributos: Modelo dimensional de explotación**

*Fuente: elaboración propia de LafroX a partir del modelo lógico de la Figura 5.7 del Subdocumento 5, de RT-05.01 de las Bases Técnicas Transversales (PUCV, 2026d) y de la matriz de retención del Anexo 5-D.*

La validación aplica la condición de cada fila al hito indicado; NULL legítimo se distingue de dato obligatorio ausente.

---
### Políticas referidas por el diccionario

Cada fila conserva sensibilidad y código de política. Los códigos siguientes reproducen su plazo/control; 5-D define inicio, ubicación y eliminación y prevalece en excepciones de conservación. AL/CR/ME se interpretan con la leyenda A.1 y 5-E. Las referencias de UUID se validan según 5-B; no son UUID nuevos del receptor. La política por fila no permite eliminar maestros interpretativos ni evidencia de un expediente vigente.

- `P01`: Vigente con historial de versiones; Acceso por rol; cifrado en reposo del almacén.
- `P02`: Vigente con historial de versiones; Cifrado a nivel de campo, acceso reforzado y consulta auditada.
- `P03`: Vigente con historial de versiones; Cifrado a nivel de campo.
- `P04`: Vigente más 5 años de historial; Acceso por rol; cifrado en reposo del almacén.
- `P05`: Vigente más 5 años de historial; Cifrado a nivel de campo.
- `P06`: 7 años (auditoría y seguridad); Acceso por rol; cifrado en reposo del almacén.
- `P07`: 7 años (auditoría y seguridad); Cifrado a nivel de campo, acceso reforzado y consulta auditada.
- `P08`: Máx(vida útil + 6 meses, 5 años); Acceso por rol; cifrado en reposo del almacén.
- `P09`: 5 años por trazabilidad; se reconstruye del movimiento; Cifrado a nivel de campo.
- `P10`: 5 años por trazabilidad; se reconstruye del movimiento; Acceso por rol; cifrado en reposo del almacén.
- `P11`: Máx(vida útil + 6 meses, 5 años); Cifrado a nivel de campo.
- `P12`: 6 años por respaldo del documento y del corte; Acceso por rol; cifrado en reposo del almacén.
- `P13`: 6 años por respaldo del documento y del corte; Cifrado a nivel de campo.
- `P14`: 5 años, incluida la versión de regla y calibración que la interpreta; Acceso por rol; cifrado en reposo del almacén.
- `P15`: 5 años, incluida la versión de regla y calibración que la interpreta; Cifrado a nivel de campo.
- `P16`: conservar con el expediente sanitario y sus versiones interpretativas.
- `P17`: 5 años como evidencia del precio aplicado; Acceso por rol; cifrado en reposo del almacén.
- `P18`: 5 años como evidencia del precio aplicado; Cifrado a nivel de campo.
- `P19`: 6 años por el compromiso con el cliente; Acceso por rol; cifrado en reposo del almacén.
- `P20`: 6 años por el compromiso con el cliente; Cifrado a nivel de campo.
- `P21`: 6 años por compromiso/evidencia; Acceso por rol; cifrado en reposo del almacén.
- `P22`: 6 años por el compromiso con el cliente; Cifrado a nivel de campo, acceso reforzado y consulta auditada.
- `P23`: 12 meses la posición; 6 años el plan y la secuencia; Acceso por rol; cifrado en reposo del almacén.
- `P24`: 12 meses la posición; 6 años el plan y la secuencia; Cifrado a nivel de campo, acceso reforzado y consulta auditada.
- `P25`: 12 meses la posición; 6 años el plan y la secuencia; Cifrado en reposo y en tránsito.
- `P26`: Historial interpretativo de auditoría 7 años; datos personales según 5-D; Acceso por rol; cifrado en reposo del almacén.
- `P27`: 6 años por evidencia de servicio; Acceso por rol; cifrado en reposo del almacén.
- `P28`: 6 años por evidencia de servicio; Cifrado a nivel de campo, acceso reforzado y consulta auditada.
- `P29`: 6 años por evidencia de servicio; Cifrado a nivel de campo.
- `P30`: 6 años de dossier financiero; Cifrado a nivel de campo.
- `P31`: 6 años de dossier financiero; Acceso por rol; cifrado en reposo del almacén.
- `P32`: 6 años de dossier financiero; Cifrado a nivel de campo, acceso reforzado y consulta auditada.
- `P33`: 6 años con bloqueo de versión; Acceso por rol; cifrado en reposo del almacén.
- `P34`: 6 años con bloqueo de versión; Cifrado a nivel de campo, acceso reforzado y consulta auditada.
- `P35`: 6 años deintercambio; Acceso por rol; cifrado en reposo del almacén.
- `P36`: 6 años deintercambio; Cifrado a nivel de campo, acceso reforzado y consulta auditada.
- `P37`: Vigente con historial; Cifrado a nivel de campo.
- `P38`: Vigente con historial; Acceso por rol; cifrado en reposo del almacén.
- `P39`: 12 meses de registro; 6 años la evidencia de notificación al cliente; Acceso por rol; cifrado en reposo del almacén.
- `P40`: 12 meses de registro; 6 años la evidencia de notificación al cliente; Cifrado a nivel de campo.
- `P41`: 7 años (auditoría y seguridad); Solo escritura; la consulta se audita.
- `P42`: 7 años (auditoría y seguridad); Cifrado a nivel de campo; Solo escritura; la consulta se audita.
- `P43`: 7 años, alineada con la retención de la auditoría porque la decisión forma parte del expediente que la sustenta; Acceso por rol; cifrado en reposo del almacén.
- `P44`: 30 días en el almacén de ingesta; Retención de 30 días; no es evidencia sanitaria.
- `P45`: 30 días en el almacén de ingesta; Cifrado a nivel de campo; Retención de 30 días; no es evidencia sanitaria.
- `P46`: 5 años, con asociación, regla y calibración; Acceso por rol; cifrado en reposo del almacén.
- `P47`: 5 años, con asociación, regla y calibración; Cifrado a nivel de campo.
- `P48`: 12 meses totales, incluidos los derivados; Cifrado en reposo y en tránsito; Uso limitado a la finalidad declarada; eliminación total verificada a los 12 meses.
- `P49`: 12 meses totales, incluidos los derivados; Cifrado en reposo y en tránsito; Cifrado a nivel de campo, acceso reforzado y consulta auditada; Uso limitado a la finalidad declarada; eliminación total verificada a los 12 meses.
- `P50`: Sin retención: es derivada y se reconstruye; Proyección derivada: no es fuente y no confirma una reserva.
- `P51`: Sin retención: es derivada y se reconstruye; Cifrado a nivel de campo; Proyección derivada: no es fuente y no confirma una reserva.
- `P52`: Sin retención: es derivada y se reconstruye; Cifrado a nivel de campo, acceso reforzado y consulta auditada; Proyección derivada: no es fuente y no confirma una reserva.
- `P53`: Alineada a la retención de su fuente transaccional; Se publica al warehouse sin dato crítico ni sin cifrar.
- `P54`: Alineada a la retención de su fuente transaccional; Cifrado a nivel de campo, acceso reforzado y consulta auditada; Se publica al warehouse sin dato crítico ni sin cifrar.
- `P55`: Alineada a la retención de su fuente transaccional; Cifrado a nivel de campo; Se publica al warehouse sin dato crítico ni sin cifrar.

<a id="anexo-5b"></a>

## Anexo 5-B. Cardinalidades exactas, módulo y integridad referencial

Cada dominio relacional confirma en su autoridad, sin escritor alternativo durante particiones: BD_RUTAS central con copias lectoras; inventario/preparación local. Ingesta térmica durable acepta consistencia eventual; BI es diferido y Redis reconstruible. S3 aporta durabilidad/versionado, sin transacción distribuida con su referencia. CAP se aplica por perímetro, no solo por motor.


Las cardinalidades se leen en las vistas de 5.1/5-M y la nulabilidad en 5-A/5-C; las restricciones físicas e índices están en 5-F. La matriz siguiente identifica almacén, motor y autoridad, sin repetir todos los conectores.

Los extremos opcionales representan estados iniciales o excepciones, no omisión de controles: TERRENO exige preventista; producto con lote exigido exige lote; raíz causal es el único evento sin padre; un sensor fijo exige sitio y uno móvil vehículo. La unidad VACIA/ABIERTA puede no tener contenido; al cerrarse exige contenido y SSCC según el hito. Una misión puede no tener confirmación antes del picking, pero no cierra sin validar sus líneas. Pedido PENDIENTE no tiene promesa confirmada; al confirmarse mantiene exactamente una ORIGINAL y las revisiones autorizadas. Cada pedido admite cero o una entrega y varios intentos vinculados a esa entrega. Cada promesa tiene promesa_id como PK individual y ordinal único por pedido; entrega referencia la ORIGINAL del mismo pedido.

Lote y unidad logística se relacionan muchos a muchos mediante inv_unidad_contenido; unidad y evento se relacionan mediante cal_evento_objeto. No existe una FK directa lote→unidad ni unidad→cabecera del evento. El SSCC identifica la unidad, no el lote; GTIN+número del proveedor identifica el lote. La reserva detalla líneas vinculadas al pedido; las confirmaciones referencian su línea de misión. Un pedido EDI sin cliente resuelto queda en staging, sin crear un pedido canónico inválido.

Movimientos conservan saldo origen/destino según dirección, ajuste y reversión de 5-C. Cobro puede preceder a rendición, obligatoria al cierre; aplicación conecta deuda/documento y pago. POD/acuses son objetos distintos del DTE. El expediente conserva entidades/versiones bajo 5-D, sin borrado en cascada de evidencia; referencias entre almacenes se validan por contrato, no por FK distribuida. Los hechos analíticos conservan grano/identidad de origen y las cachés son proyecciones reconstruibles.

<a id="tab-a12-modulo-almacen"></a>

| Dominio | Módulo y almacén lógico | Motor que lo sostiene | Participantes y ubicación | Naturaleza de la referencia |
| --- | --- | --- | --- | --- |
| Maestros y configuración | `BD_MAESTROS_CONF` | PostgreSQL 16 con Aurora central como distribución y copia local de lectura | Autoridad en Maestro; copias de solo lectura en cada sitio | Réplica por publicación de eventos, sin escritura local |
| Actores, roles y permisos | `BD_GOBIERNO_ACCESO` e identidad federada de S4 | PostgreSQL 16 y Keycloak como proveedor de identidad | Central | El token se valida contra el emisor; no se almacenan contraseñas |
| Recepción, lote, saldo y unidad logística | BD_INVENTARIO | PostgreSQL 16/PostGIS por sitio; Aurora copia/consolidado | Cada sitio confirma en su perímetro | DMS solo Talca lector; consolidación por eventos |
| Trazabilidad, custodia y calidad | `BD_CALIDAD_TRAZABILIDAD` | PostgreSQL 16 local y DynamoDB para ingesta de eventos | Central Aurora para el expediente consolidado | El evento local es el que prueba; el central consolida |
| Preventa, tarifa y promesa | BD_PREVENTA | Aurora PostgreSQL central | M3, dueño del pedido en los tres canales | Pedido/tarifa centrales; reserva validada por inventario del sitio |
| Preparación y picking | `BD_PREPARACION` | PostgreSQL 16 local | Por sitio | Escritura local con evento al bus y confirmación idempotente |
| Rutas, viajes y paradas | BD_RUTAS | PostgreSQL/PostGIS central | Autoridad central; copias en sitio/dispositivo | Itinerario descargado/versionado; sin otro escritor |
| Reparto, entrega y devolución | BD_REPARTO | PostgreSQL central; Room/SQLite en terreno | Central consolida capturas autorizadas | Acuse durable local; consolidación posterior sin exigir WAN |
| Cobranza y finanzas | BD_COBRANZA_FINANZAS | PostgreSQL central; captura durable móvil | Autoridad financiera central | Captura offline permitida, rendición y conciliación; POS incierto no es aprobación |
| Documentos y objetos | `S3_DOCS` | Almacenamiento de objetos con bloqueo de versión | Central y copia por región | La referencia es por clave lógica y huella, nunca por ruta física |
| Intercambio con canal moderno | `BD_EDI_CANALMODERNO` | PostgreSQL 16 central | Central | Contrato versionado y mensajes idempotentes |
| Notificaciones al cliente | BD_MAILS_NOTIF | PostgreSQL central | Central | Plantillas/preferencias versionadas; tres canales |
| Telemetría y caché de lectura | BD_TELEMETRIA / REDIS_SESIONES_CACHE | DynamoDB raw; S3 Parquet/Glue/Redshift series; Redis caché | M12 ingiere; central consolida; metadatos/calibraciones en Calidad | Caché reconstruible, sin confirmar reservas/pagos |
| Analítica de explotación | `BD_BI_GERENCIA` | Amazon S3, AWS Glue, Amazon Redshift Serverless y QuickSight embebido | Región `sa-east-1` | Consulta sin escritura en el almacén transaccional |
| Bus de eventos | Cola administrada de brokerage de S4 | Broker de mensajería | Central y por sitio | Publicación con reintento y confirmación durable |
| Copia local del dispositivo | Persistencia local de captura/consulta | Room/SQLite nativo; IndexedDB en PWA | Dispositivo/cuenta | UUID, payload pendiente y acuse durable; sin autoridad comercial autónoma |

**Tabla A.11 - Módulo, almacén lógico y motor por dominio**

*Fuente: elaboración propia de LafroX a partir de los quince nombres lógicos de persistencia de S4 4.1.5, del Subdocumento 4 y de T-11; el Formulario T-12 no añade motores.*

Las relaciones de negocio no usan borrado en cascada de evidencia. Se cierran estados y se elimina solo bajo retención elegible. UUID relaciona filas y clave natural protege negocio; entre almacenes/sedes se valida identidad y versión por contrato, no mediante FK distribuida.

En PostgreSQL 16 la UK particionada incluye toda la clave de partición; unicidad local no equivale a identidad global. 5-F fija ámbito y restricciones. Una FK hacia tabla particionada requiere clave referenciada válida; entre motores se valida el contrato de identidad.


<a id="anexo-5c"></a>

## Anexo 5-C. Dominios de valores, reglas de validación y causas de rechazo

Se conservan sin partición las entidades con UUID global referenciado por FK simple: saldo, movimiento, excursión/bloqueo, POD y auditoría. Su grano se controla con UK y mantenimiento por lotes; no se anuncia PK global incompatible con una partición mensual. El detalle sanitario conserva la partición y FK compuestas ya declaradas. El saldo incluye producto_id y lote nullable solo para producto exento; UK sitio/ubicación/producto/lote/unidad usa NULLS NOT DISTINCT. Contenido/reserva/conteo conservan la misma condición, sin crear lote ficticio. Si existe lote, se verifica que corresponde al producto.

Los catálogos abiertos de territorio, sistema, turno y familia remiten a versiones aprobadas y contratos concretos, no a un catálogo cerrado sin definición. En 5-A se enumeran dominio de decisión/causa/perfil de receptor y procedencia térmica. Desconocido se aísla como DOMINIO_NO_ADMITIDO con original y dueño; la dimensión hereda versión y no fabrica clasificación. La ventana EDI valida hora/zona y cruce a día siguiente según el perfil.

Las reglas de este anexo se sustentan en las vistas lógicas del cuerpo y Anexo 5-M y el diccionario 5-A. Dentro del mismo PostgreSQL se aplican FK; entre almacenes, sedes o S3 se valida identidad/versión mediante contratos, conciliación y excepciones, sin anunciar FK distribuida.

**Parámetros tipados.** valor es JSON/jsonb con tipo_valor y valor: NUMERO exige número, unidad y rango aprobados; BOOLEANO solo true/false; TEXTO límite declarado por parámetro, máximo inicial 512 caracteres; INTERVALO exige cantidad positiva y unidad del catálogo SEGUNDO/MINUTO/HORA/DIA; LISTA exige elementos del catálogo aprobado, sin duplicados. Tipo desconocido, ausencia de valor, rango o unidad inválidos producen PARAMETRO_INVALIDO y aislamiento en migración. No se convierte ausencia en falso.

**Perfiles sanitarios.** epcis_version=2.0 y cbv_version=2.0 son independientes; perfil_evento es versión de contrato de solución: RECEPCION_V1 (ObjectEvent, OBSERVE, receiving), MOVIMIENTO_V1 (ObjectEvent, OBSERVE, transporting), AGREGACION_V1 (AggregationEvent, ADD/DELETE para composición/descomposición, packing/unpacking), DESPACHO_V1 (ObjectEvent, OBSERVE, shipping), ENTREGA_V1 (ObjectEvent, OBSERVE, receiving en destino). Los términos CBV se serializan con sus identificadores de vocabulario; ubicación, instante, objetos, disposición y procedencia se validan en el contrato. Un perfil desconocido se aísla con EVENTO_FUERA_DE_SUBCONJUNTO, conservando mensaje original. ObjectEvent/AggregationEvent son tipos EPCIS, no versiones de CBV. El arreglo de objetos se congela con ordinal estable antes de publicar; la falta de ordinal externo no inventa un hecho de negocio.

**Movimientos y cantidades.** cantidad es positiva con unidad; RECEPCION exige destino, SALIDA exige origen, TRASLADO exige ambos distintos y misma conversión validada. AJUSTE positivo exige destino y causa; negativo exige origen y causa. ANULACION exige documento_origen_tipo=MOVIMIENTO y documento_origen_id del movimiento original, invierte sus efectos origen/destino y conserva cantidad/unidad y vínculo idempotente; nunca sobrescribe ni elimina el original. Los saldos no se vuelven negativos por una reversión sin control. Importes cobrados no negativos; ajuste_redondeo y diferencias pueden tener signo con su fórmula, justificación y autorización. ajuste_redondeo = importe registrado − importe autorizado externo solo para tarjeta comprobada; efectivo/crédito no fabrican autorización externa.

**Identidad de promesa.** Cada ORIGINAL o REVISION recibe un promesa_id distinto como PK individual. UNIQUE(pedido_id, version) ordena la historia sin repetir ordinal; el único parcial de ORIGINAL garantiza una por pedido. La entrega referencia esa PK y valida pedido coincidente y tipo ORIGINAL en el contrato/transacción de aceptación, sin filtrar su vigencia.

**Vigencias.** Parámetro, regla térmica, calibración, tarifa y revisiones de promesa no tienen intervalos históricos superpuestos para su clave natural. Intervalos semiabiertos [desde,hasta), extremo abierto solo para versión final, fin > inicio. La escritura bloquea la clave natural y comprueba todos los intervalos en la misma transacción; donde son co-residentes se añade exclusión por rango PostgreSQL con soporte btree_gist. El único parcial de fila abierta es adicional y no sustituye la exclusión. La promesa ORIGINAL permanece inmutable aun cuando haya revisión; el indicador la busca por tipo=ORIGINAL y no por vigencia actual.

**Selección temporal.** El dominio de vigente_desde identifica el inicio, no obliga a que sea posterior al hecho. Para usar una versión, desde ≤ fecha de negocio < hasta, o sin límite final cuando hasta es NULL; una versión futura no se aplica antes de su inicio. Se conservan intervalos y versiones históricas, incluidos los de dimensiones analíticas. Un vencimiento se registra tal como lo declara el proveedor; su estado sanitario se valida sin desplazar la fecha para aceptar el lote.

**Carga y cifrado.** version_carga es un ordinal bigint positivo, aumenta con cada revisión y se compara numéricamente. La autorización de salida exige que carga y documento ERP correspondan a esa versión; un ordinal mayor no acredita emisión válida. obj_objeto.cifrado es booleano comprobado en el almacenamiento; si 5-E exige cifrado, false o la falta de verificación impiden aceptar el objeto, conservando original y causa de rechazo.

**Origen de captura.** En TERRENO, preventista_id identifica al capturador autorizado; MOSTRADOR, EDI y PORTAL mantienen NULL sin inventar un preventista. La identidad de quien captura o integra se registra en gob_auditoria.actor_id con UUID/correlación y origen_captura: persona autorizada, cuenta de autoatención o actor técnico autenticado, respectivamente. El responsable comercial no se infiere de ese campo. M3 valida cuenta/permisos al confirmar; un pedido pendiente no crea reserva ni promesa de entrega confirmada.

**Ciclo de vida.** parent_event_id admite NULL exclusivamente en raíz causal; unidad VACIA/ABIERTA admite ausencia de contenido y SSCC hasta el hito de cierre que lo exige. Producto sin lote obligatorio admite lote NULL. Las líneas permiten varias asignaciones/lotes/unidades e intentos; no se deduplican por mera igualdad de producto/cantidad. Actor autorizador financiero referencia mae_actor.actor_id y tiene rol habilitado distinto del ejecutor, antes de aprobar un movimiento; no se confunde con nombre de rol. payload de excepción conserva snapshot de decisión y regla/versionado con límite de 256 KiB de diseño; el exceso conserva objeto íntegro con hash y retención equivalente, sin truncamiento silencioso.

La recepción conserva lecturas térmicas físicamente inválidas con valor original, sensor, hora, unidad y alerta; se excluyen del cálculo de cumplimiento con causa visible, sin destruir evidencia. Defecto de sensor, excursión válida y pérdida de cobertura son incidentes distintos. Cada rechazo adicional usa código de causa, original preservado, responsable y decisión antes de publicar; los catálogos de identidad y causales externos se versionan según S4, no se sustituyen por un default local.


Cada regla de calidad declara dominio, punto de aplicación y causa tipificada. Los rechazos alimentan el tablero RT-05.04; original y decisión se conservan antes de publicar.
<a id="tab-a13-dominios"></a>

| Atributo o familia | Valores o formato admitidos | Regla de validación en el punto de captura | Causa de rechazo |
| --- | --- | --- | --- |
| `mae_producto.gtin` | 8, 12, 13 o 14 dígitos | Longitud declarada y dígito verificador válido; más de un GTIN por producto se modela como equivalencia y no como duplicado | `GTIN_INVALIDO`, `GTIN_DUPLICADO` |
| `inv_lote.numero_lote` | Texto normalizado de 1 a 28 caracteres | Se eliminan espacios sobrantes; no se admite solo espacio; el vencimiento es atributo y no forma parte de la identidad | `LOTE_VACIO` |
| `inv_unidad_logistica.sscc_id` | 18 dígitos | Estructura GS1 válida, con dígito verificador y no repetida entre unidades vivas | `SSCC_INVALIDO`, `SSCC_DUPLICADO` |
| `inv_unidad_logistica.unidad_logistica_id` | Identificador interno generado por el sistema | Nunca se deriva del SSCC ni del código de negocio; identifica la unidad aunque el SSCC se reetiquete | `IDENTIDAD_LOGISTICA_INVALIDA` |
| `inv_lote.fecha_vencimiento` | Fecha en formato ISO 8601 | Obligatoria cuando el producto la exige y posterior o igual a la fecha de recepción | `VENCIMIENTO_ANTERIOR`, `VENCIMIENTO_AUSENTE` |
| Cantidades con unidad | Decimal de tres lugares y unidad declarada | Mayor o igual a cero; la cantidad reservada no supera la disponible menos la bloqueada | `CANTIDAD_NEGATIVA`, `RESERVA_EXCESIVA`, `UNIDAD_SIN_CONVERSION` |
| `mae_sitio.codigo` | Código alfanumérico de 3 a 10 caracteres | Debe existir en el maestro de sitios y estar activo en el momento de la captura | `SITIO_DESCONOCIDO` |
| `mae_unidad.codigo` | Código del maestro de unidades | Debe existir y tener conversión vigente hacia la unidad de la línea | `UNIDAD_SIN_CONVERSION` |
| `mae_cliente.canal` | `TRADICIONAL`, `MODERNO`, `FOOD_SERVICE`, `CADENA`, `HORECA` | Debe existir en la ficha del cliente; el canal y el perfil de atención son atributos distintos y ninguno se deduce del otro | `CANAL_NO_DECLARADO` |
| `mae_actor.rol` | Roles del catálogo de identidad de S4 | Debe existir el actor con rol activo y sitio asignado; no todo actor pertenece a un transportista | `ACTOR_SIN_ROL` |
| `prv_pedido_promesa.tipo` | `ORIGINAL`, `REVISION` | La primera promesa del pedido es `ORIGINAL` y no se modifica; toda revisión declara motivo, autor e instante | `PROMESA_NO_INMUTABLE`, `MOTIVO_REVISION_AUSENTE` |
| `rep_intento.resultado` | `ENTREGADO`, `ENTREGA_PARCIAL`, `NO_CONTACTO`, `RECHAZADO_POR_CLIENTE`, `NO_ENTREGADO_POR_CAUSAL` | Obligatorio; el dominio cerrado admite el no contacto sin inventar causa | `RESULTADO_NO_CATALOGADO` |
| `rep_intento.causal_codigo` | Código del catálogo de causales de reparto | Obligatorio cuando el resultado no es exitoso | `CAUSAL_OBLIGATORIA` |
| `cal_evento_custodia.tipo_evento` | Subconjunto EPCIS declarado en 5.1.7 | Cada tipo declara acción, paso de negocio y momento; un tipo fuera del subconjunto se rechaza | `EVENTO_FUERA_DE_SUBCONJUNTO` |
| `cal_evento_custodia.parent_event_id` | Clave del evento causal | Obligatorio en todo evento salvo en la raíz; la agregación logística usa su propio identificador de contenedor | `CADENA_CUSTODIA_ROTA` |
| `cal_regla_termica.ventana` | Minutos de inicio y fin dentro del rango declarado | La ventana no puede cruzar una regla de producto distinta sin asociación explícita | `VENTANA_TERMICA_INVALIDA` |
| Huella de objeto y documento | SHA-256 en hexadecimal de 64 caracteres | Debe coincidir con la del archivo recibido en la ingesta y en cada verificación posterior | `HASH_NO_COINCIDE` |
| `obj_objeto.clase_retencion` | Clases de la política de retención del Anexo 5-D | Obliga a declarar plazo y efecto al vencer antes de aceptar el objeto | `CLASE_RETENCION_DESCONOCIDA` |
| Versión de carga | Identificador de versión de la carga | Obligatorio en toda carga de historia y en todo ensayo; la carga sin versión se rechaza completa | `VERSION_DE_CARGA_AUSENTE` |
| `mae_sitio.zona_horaria` | Identificador IANA válido | Debe existir en la base de zonas horarias y coincidir con la del sitio declarado | `ZONA_HORARIA_INVALIDA` |
| Temperatura leída | Decimal en grados Celsius con su unidad | Dentro del rango físico admitido por el tipo de sensor; una lectura inválida se conserva marcada y aislada del indicador | `TEMPERATURA_FUERA_DE_RANGO`, `UNIDAD_TEMPERATURA_AUSENTE` |
| `mae_parametro_version.vigente_hasta` | Fecha nula en la versión vigente | No solapamiento de intervalos históricos, bloqueo de clave natural y único parcial de versión abierta | `VERSION_VIGENTE_DUPLICADA` |
| Importes | Decimal de dos lugares con moneda | Importe no negativo con moneda; ajustes y diferencias con signo según el contrato financiero de este anexo | `IMPORTE_NEGATIVO`, `MONEDA_AUSENTE` |
| `gob_auditoria.resultado` | `ACEPTADO`, `RECHAZADO`, `PARCIAL`, `DIFIERIDO` | Obligatorio en toda operación registrada; una auditoría sin resultado es una auditoría incompleta | `AUDITORIA_INCOMPLETA` |

| `mae_sitio.tipo` | CENTRO_DISTRIBUCION, CROSS_DOCKING, CASA_MATRIZ, INSTALACION_CLIENTE | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `inv_lote.estado_calidad` | PENDIENTE, APTO, BLOQUEADO, LIBERADO, RETIRADO | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `inv_unidad_logistica.tipo` | PALLET, CAJA, CONTENEDOR | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `cal_evento_custodia.tipo_epcis` | ObjectEvent, AggregationEvent | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `cal_excursion.severidad` | MENOR, CRITICA | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `prv_tarifa.canal` | TRADICIONAL, MODERNO, FOOD_SERVICE, CADENA, HORECA | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `prv_pedido.canal` | TRADICIONAL, MODERNO, FOOD_SERVICE, CADENA, HORECA | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `prv_pedido_linea.moneda` | CLP | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `prp_mision.estado` | PLANIFICADA, EN_CURSO, CERRADA, CANCELADA | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `rut_ruta.estado` | PLANIFICADA, EN_CURSO, CERRADA | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `rut_viaje.estado` | PLANIFICADO, EN_CURSO, RETORNADO, CERRADO, CANCELADO | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `rep_devolucion.estado` | REGISTRADA, RECIBIDA, EVALUADA, CERRADA, RECHAZADA | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `env_cuenta_corriente.tipo_envase` | Código activo del maestro versionado de tipos de envase del CLIENTE; 1–32 caracteres, sin serialización individual ni alta por defecto | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `cob_cobro.moneda` | CLP | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `cob_aplicacion.moneda` | CLP | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `cob_cuadratura.estado` | PENDIENTE, CUADRADA, CON_DIFERENCIA, APROBADA, CERRADA | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `cob_descuadre.estado` | ABIERTO, INVESTIGACION, JUSTIFICADO, AUTORIZADO, RESUELTO | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `doc_acuse_tecnico.canal` | SII, INTERCAMBIO_ERP | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `doc_acuse_tecnico.estado` | PENDIENTE, ACEPTADO, RECHAZADO | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `doc_acuse_destinatario.estado` | PENDIENTE, RECIBIDO, RECHAZADO | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `obj_objeto.clase_retencion` | DOCUMENTO_POD, TRAZABILIDAD, TERMICO, GPS_PERSONAL, AUDITORIA, LOG, RESPALDO | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `edi_mensaje.tipo` | ORDERS, ORDRSP, DESADV, INVOIC, RECADV, APERAK | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `not_plantilla.tipo_aviso` | PEDIDO, PREPARACION, DESPACHO, ENTREGA, INCIDENCIA, COBRANZA, RETIRO | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `not_aviso.tipo` | PEDIDO, PREPARACION, DESPACHO, ENTREGA, INCIDENCIA, COBRANZA, RETIRO | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `not_intento.canal` | EMAIL, SMS, PUSH | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `not_intento.resultado` | PENDIENTE, ENVIADO, CONFIRMADO, FALLIDO | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `gob_excepcion_sync.tipo` | DUPLICADO, CONFLICTO_VERSION, GAP_VERSION, REFERENCIA_AUSENTE, VALIDACION, PAGO_INCIERTO | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `dim_cliente.canal` | TRADICIONAL, MODERNO, FOOD_SERVICE, CADENA, HORECA | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `dim_sitio.tipo` | CENTRO_DISTRIBUCION, CROSS_DOCKING, CASA_MATRIZ, INSTALACION_CLIENTE | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `dim_ruta.tipo_servicio` | URBANO, RURAL, PERIFERICO, CROSS_DOCKING | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `hech_entrega.moneda` | CLP | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `hech_entrega_intento.resultado` | ENTREGADO, ENTREGA_PARCIAL, NO_CONTACTO, RECHAZADO_POR_CLIENTE, NO_ENTREGADO_POR_CAUSAL | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `hech_linea_venta.moneda` | CLP | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `hech_movimiento_stock.tipo_movimiento` | RECEPCION, SALIDA, TRASLADO, AJUSTE, ANULACION | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |
| `hech_excursion.severidad` | MENOR, CRITICA | Validación al capturar/transformar; versión del dueño | `DOMINIO_NO_ADMITIDO`: aislar original y resolver antes de publicar |

**Tabla A.12 - Dominios de valores cerrados y su validación**

*Fuente: elaboración propia de LafroX a partir del Anexo 5-A, de los perfiles de evento declarados en 5.1.7 y de RT-05.04 de las Bases Técnicas Transversales (PUCV, 2026d).*

<a id="tab-a14-causas-rechazo"></a>

| Causa | Dónde se detecta | Tratamiento en operación | Tratamiento en migración |
| --- | --- | --- | --- |
| `GTIN_INVALIDO` | Captura de recepción y de producto | Rechazo con mensaje al operador | Cuarentena con el valor original preservado |
| `GTIN_DUPLICADO` | Resolución de equivalencia de producto | Rechazo; se registra la referencia existente | Alta de equivalencia con decisión registrada, no reemplazo silencioso |
| `LOTE_VACIO` | Captura de recepción | Rechazo; no se acepta línea de producto que exige lote sin él | Cuarentena con el valor original y la regla que exige el lote |
| `VENCIMIENTO_ANTERIOR` | Captura de recepción | Rechazo con la fecha correcta en el mensaje | Cuarentena; no se deriva vencimiento desde una vida útil genérica |
| `VENCIMIENTO_AUSENTE` | Captura de recepción de producto que exige vencimiento | Rechazo | Cuarentena hasta obtener el dato de origen o la decisión de Calidad |
| `SSCC_INVALIDO` | Captura de unidad logística | Rechazo de la unidad | Cuarentena con la etiqueta original disponible |
| `IDENTIDAD_LOGISTICA_INVALIDA` | Captura de unidad logística | Rechazo; la identidad interna la genera el sistema | Cuarentena; nunca se deriva un identificador del código de negocio |
| `CANTIDAD_NEGATIVA` | Captura de movimiento | Rechazo | Cuarentena con el signo original preservado |
| `RESERVA_EXCESIVA` | Confirmación de preparación | Rechazo; el saldo no permite la reserva | No se ajusta el saldo para coincidir: la diferencia se explica y se autoriza |
| `UNIDAD_SIN_CONVERSION` | Captura de línea | Rechazo | Cuarentena hasta declarar el factor y su versión |
| `SITIO_DESCONOCIDO` | Captura con sitio | Rechazo | Alta del sitio en el maestro con decisión registrada o aislamiento |
| `CANAL_NO_DECLARADO` | Captura de pedido | Rechazo | Cuarentena; el canal no se deduce del nombre del cliente |
| `ACTOR_SIN_ROL` | Identificación de la operación | Rechazo; no hay operación sin actor | Cuarentena; no se inventa un actor |
| `RESULTADO_NO_CATALOGADO` | Cierre de intento | Rechazo del cierre | Cuarentena; el resultado histórico se conserva sin reinterpretar |
| `CAUSAL_OBLIGATORIA` | Cierre de intento no exitoso | Rechazo del cierre | Cuarentena con el resultado original y la observación de la fuente |
| `EVENTO_FUERA_DE_SUBCONJUNTO` | Ingesta de evento de custodia | Rechazo del evento con alerta | No se fabrica historia: el evento no migrado queda declarado |
| `CADENA_CUSTODIA_ROTA` | Ingesta de evento sin padre resoluble | Rechazo del evento enlazado y registro de la interrupción | Cuarentena del evento huérfano sin inventar el padre |
| `VENTANA_TERMICA_INVALIDA` | Asociación de ventana a producto | Rechazo de la asociación | Cuarentena de la asociación |
| `HASH_NO_COINCIDE` | Ingesta de documento u objeto | Rechazo del documento y alerta | Aislamiento con el archivo original disponible para verificación |
| `CLASE_RETENCION_DESCONOCIDA` | Aceptación de objeto almacenado | Rechazo del objeto | No se acepta objeto sin clase; se corrige la política, no el objeto |
| `VERSION_DE_CARGA_AUSENTE` | Carga masiva | Rechazo del lote completo | Rechazo; la versión es obligatoria y ordena la reejecución |
| `ZONA_HORARIA_INVALIDA` | Captura de sitio | Rechazo del alta de sitio | Cuarentena del sitio |
| `TEMPERATURA_FUERA_DE_RANGO` | Ingesta de lectura | Rechazo de la lectura con alerta | Cuarentena de la serie; no se corrige la lectura histórica |
| `UNIDAD_TEMPERATURA_AUSENTE` | Ingesta de lectura | Rechazo de la lectura | Cuarentena de la serie |
| `VERSION_VIGENTE_DUPLICADA` | Publicación de versión de parámetro | Rechazo de la publicación | Cuarentena de la versión duplicada |
| `IMPORTE_NEGATIVO`, `MONEDA_AUSENTE` | Captura de importe | Rechazo | Cuarentena con el importe original |
| `AUDITORIA_INCOMPLETA` | Cierre de la operación | Rechazo del registro de auditoría | La operación no se carga sin su auditoría |

**Tabla A.13 - Causas de rechazo y su tratamiento en operación y en migración**

*Fuente: elaboración propia de LafroX a partir de RT-05.04 y RT-05.12 de las Bases Técnicas Transversales (PUCV, 2026d), del caso de estudio y de las reglas de saneamiento declaradas en 5.3.*

A.13 distingue rechazo (sin carga y con causa accionable), cuarentena (original íntegro consultable, defecto y resolución posterior) y decisión registrada (corrección/equivalencia aprobada con regla/versión en perfilado). Se prohíbe carga corregida silenciosa o historia inferida: resultado/causa ausentes permanecen aislados con original visible.


<a id="anexo-5d"></a>

## Anexo 5-D. Retención por dominio y por atributo

La retención se determina por clase, no por estar en S3: documentos/POD seis años; trazabilidad máximo entre vida útil más seis meses y cinco años; térmico detallado cinco años; GPS y datos personales de posición doce meses totales (raw treinta días en sa-east-1, sin réplica internacional); auditoría siete años; logs doce meses online más veinticuatro de archivo y respaldos treinta y cinco días según S4. Las copias personales y versiones temporales se incluyen en purga/inventario. Geocercas de configuración no son posición personal. Maestros, reglas y calibraciones sobreviven mientras permitan interpretar cualquier expediente retenido.

Un objeto bloqueado o bajo conservación legal no se destruye antes de vencimiento: se programa eliminación elegible, se comprueban versiones, réplicas y respaldos conforme S4 y se registra resultado. No se promete eludir Object Lock ni borrar evidencia financiera como si fuera caché.

La Tabla A.14 detalla inicio, ubicación y eliminación por dominio/atributo. Los doce meses de posición personal incluyen derivados y coordenadas recuperables de respaldos: retirar el identificador no basta para anonimizar. Los siete años de auditoría/seguridad son un compromiso de S4, no un plazo impuesto por el caso.

<a id="tab-a15-retencion"></a>

| Dominio o atributo | Inicio del plazo | Retención en línea | Archivo adicional | Ubicación y réplica | Efecto al vencer y evidencia |
| --- | --- | --- | --- | --- | --- |
| `doc_documento`, `doc_pod` y acuses | Emisión del documento | 6 años | Ninguno | Central con copia por región; bloqueo de versión activo | Eliminación por clase con conteo de filas, clave de objeto y registro de la ejecución |
| Expediente del lote: `cal_evento_custodia`, `cal_evento_objeto`, `cal_documento_evento`, `inv_lote`, `inv_unidad_logistica`, `inv_unidad_contenido` | Cierre del lote | Mayor entre vida útil más seis meses y cinco años | Ninguno | PostgreSQL local y expediente consolidado en el central | Eliminación por partición o por lote cerrado, con el conteo de eventos y su hash |
| `cal_regla_termica` con sus versiones, `cal_calibracion` y `cal_asociacion_ventana` | Vigencia de la versión | 5 años contados desde que deja de estar vigente | Ninguno | Central y copia local de lectura | Eliminación solo cuando ninguna serie retenida la necesita para interpretarse |
| `cal_excursion` y `cal_bloqueo` con su resolución | Cierre de la resolución de Calidad | 5 años | Ninguno | Central | Eliminación por partición con el identificador de la resolución conservado en el conteo |
| `tel_lectura_cruda` | Instante de la lectura | 30 días | Ninguno | DynamoDB con tablas y punto de acceso temporal | Expiración automática por clave de tiempo; no es evidencia sanitaria |
| `tel_archivo_termino` con la serie detallada | Cierre del archivo diario | 5 años | Compresión por mes a partir del segundo año | Almacenamiento de objetos, sin réplica fuera de la región declarada | Eliminación por objeto con manifiesto de borrado y conteo de lecturas asociadas |
| `tel_serie_consolidada` | Cierre del día del sitio | 5 años | Ninguno | Almacenamiento de series | Eliminación por mes al vencer el plazo |
| `tel_posicion_gps` y derivados personales | Instante del punto | 12 meses totales | Ninguno | Solo `sa-east-1`, sin réplica internacional adicional | Borrado del punto y de sus derivados, con verificación de que la auditoría conservada no permite reconstruir la posición |
| `cob_*`, `env_*` y su dossier financiero | Cierre del período | 6 años | Ninguno | Central | Eliminación por clase con respaldo previo verificado |
| `prv_pedido`, `prv_pedido_linea`, `prv_pedido_promesa` y `prp_*` | Cierre del pedido | 6 años por el compromiso con el cliente | Ninguno | Central con copia de lectura | Eliminación por ejercicio después de cumplir el plazo documental |
| `mae_*` con su historial de versiones | Fecha de inicio de vigencia | Vigente más cinco años de historial | Ninguno | Maestro central y copias locales | Ninguna versión se elimina mientras una entidad viva la referencie |
| `edi_mensaje`, `edi_asn`, `edi_perfil_cadena` | Recepción del mensaje | 6 años | Ninguno | Central | Eliminación por clase con el conteo de mensajes y su correlativo |
| `not_aviso`, `not_intento`, `not_plantilla` y `not_preferencia` | Envío del aviso | 12 meses de registro; 6 años la evidencia de notificación al cliente | Ninguno | Central | Eliminación del registro de intento con el aviso conservado |
| `gob_auditoria` y `gob_excepcion_sync` | Registro de la operación | 7 años | Compresión por año | Central | Eliminación con autorización de dos perfiles y registro de la ejecución |
| Registros técnicos de aplicación y de acceso | Emisión del registro | 12 meses | 24 meses de archivo | Central | Eliminación por clase, distinta de la retención de auditoría y seguridad |
| Respaldo transaccional y de identidad | Cada copia | 35 días | Ninguno | Copia por sitio | Rotación automática verificada por conteo y fecha |
| `cache_*` y copias locales de lectura | Publicación de la entrada | Sin retención: es derivada y se reconstruye | Ninguno | Memoria caché del proceso y almacenamiento del dispositivo | Expiración por vigencia; purga verificable y auditada al vencer la entrada, cerrar sesión o retirar autorización |
| `hech_*` y `dim_*` | Cierre del hecho o de la versión | Alineada a la retención de su fuente transaccional | Ninguno | Redshift Serverless | Compactación por partición; la agregación no extiende el plazo de la fuente |

**Tabla A.14 - Retención declarada por dominio y por atributo**

*Fuente: elaboración propia de LafroX a partir de RT-05.07 de las Bases Técnicas Transversales (PUCV, 2026d), de los plazos de retención del Subdocumento 4 y del Artículo 85 de las Bases Administrativas (PUCV, 2026b).*

El respaldo y la salida de contrato se coordinan con S4: la eliminación comprueba clase, versiones, réplicas y plazo. Un bloqueo de conservación activo no se elude; se elimina al hacerse elegible y se audita la excepción. La evidencia vigente no pierde su clave compartida y las copias personales deben quedar ilegibles según el procedimiento aprobado, sin afirmar que una clave global pueda destruirse selectivamente.


<a id="anexo-5e"></a>

## Anexo 5-E. Clasificación por sensibilidad y controles declarados

RT-05.08 y Art. 85 exigen seudonimización/cifrado de campo para datos personales sensibles. A.15 distingue protección del almacén y de columnas según sensibilidad; toda clase AL exige cifrado en reposo y justificación del control de campo (PUCV, 2026d, §5; 2026b, art. 85).
<a id="tab-a16-sensibilidad"></a>

| Clase de dato | Sensibilidad | Cifrado en reposo | Cifrado a nivel de campo | Control de acceso declarado |
| --- | --- | --- | --- | --- |
| Documentos tributarios, POD y acuses | `AL` | Sí, con cifrado de servidor y rotación de clave | No, por decisión declarada: la emisión es única y el acceso está restringido por rol | Solo el ERP emite; lectura por rol de documentos y registro de consulta |
| Ubicación de personas y vehículos | `CR` | Sí | Sí | Acceso por rol de operación, uso limitado a la finalidad declarada y registro de auditoría |
| Identificación de personas, licencias y datos de contacto | `CR` | Sí | Sí | Credenciales cifradas de transporte sin clave estática; nunca se almacenan contraseñas del proveedor de identidad |
| Condición de crédito, saldo y cobro | `AL` | Sí | Sí | Acceso por rol de cobranza, con consulta auditada y segregación entre quien cobra y quien autoriza |
| Expediente sanitario por lote y unidad | `AL` | Sí | Sí en el identificador del responsable y en la firma | Acceso por rol de calidad y de trazabilidad; el acceso del conductor no libera el lote por sí solo |
| Series de temperatura, reglas y calibraciones | `ME` | Sí | No | Acceso por rol de calidad |
| Inventario, saldos y conteos | `ME` | Sí | No | Acceso por sitio asignado |
| Datos de clientes y maestro comercial | `ME` con `CR` en RUT y representante | Sí | Sí en RUT y representante | Acceso por rol de maestro, con auditoría de modificación |
| Objetos almacenados de evidencia | `ME` con `AL` en el documento que contienen | Sí, con bloqueo de versión | No | Acceso por referencia de clave lógica y huella verificada, nunca por ruta física |
| Registros de auditoría y de seguridad | `AL` | Sí | Sí en los valores anterior y posterior | Consulta por perfil de auditoría, con registro de la propia consulta |
| Registros técnicos de aplicación y de acceso | `ME` | Sí | No | Acceso por rol de seguridad, con retención de doce meses distinta de la auditoría |
| Parámetros, catálogos y equivalencias | `ME` | Sí | No | Acceso por rol de configuración, con versión y responsable del cambio |
| Credenciales de turno y manifiesto firmado del dispositivo | `AL` | Sí | No | Vida de 8 horas en bodega y 14 en terreno, con manifiesto de 26 horas renovado cada hora |
| Copias locales de identidad, precio, crédito y saldo | `CR` | Sí en el almacén del dispositivo | Sí | Copia de identidad de solo lectura por 24 horas; la copia local no confirma reservas ni precios |
| Lectura cruda de telemetría | `ME` | Sí | No | Acceso al proceso de ingesta; retención de 30 días |
| Hechos y dimensiones analíticas | `ME` con `AL` en importes | Sí en el almacén analítico | Sí en importes | Publicación sin dato crudo y con el mismo criterio de acceso que la fuente |

**Tabla A.15 - Clasificación por sensibilidad y control declarado**

*Fuente: elaboración propia de LafroX a partir de RT-05.08 y RT-16 de las Bases Técnicas Transversales (PUCV, 2026d), del Artículo 85 de las Bases Administrativas (PUCV, 2026b) y de la clasificación por atributo del Anexo 5-A.*

GPS se cifra por campo y desaparece a doce meses totales; la evidencia de operación puede subsistir, pero auditoría/respaldo no deben reconstruir la coordenada. DTE conserva acceso por rol y emisión única, justificando su control sin cifrado de campo. La copia de identidad de 24 h permite consulta, no autoriza reservas/precios ni reemplaza el control de acceso.


<a id="anexo-5f"></a>

## Anexo 5-F. Índices, columnas y particionado

La PK de cal_evento_objeto es (evento_objeto_id, ts_evento); la UK es (evento_id, secuencia_linea, ts_evento). La cabecera no particionada tiene UK (evento_id, ts_ocurrencia) y el detalle FK (evento_id, ts_evento) hacia esa pareja. Se prohíbe cambiar ts_ocurrencia y ts_evento tras aceptar el evento. Así un mismo evento no puede ingresar en otro mes con timestamp divergente. Si cabecera y detalle no son co-residentes, se mantienen en el mismo almacén sanitario de S4 para este contrato; otras referencias son contratos entre dominios.

mae_producto.gtin es único para el GTIN canónico no nulo; las equivalencias alternas no comparten identidad entre productos. inv_lote conserva UK (gtin, numero_lote) y valida concordancia con producto_id; vencimiento es atributo. gob_excepcion_sync usa UK (correlacion_id, clave), construida de identidad de operación y versión de decisión, sin depender de la hora de recepción.

rep_entrega y rep_entrega_linea no se particionan; una entrega por pedido tiene varios intentos y sus fragmentos. La identidad del fragmento y su asignación de origen se fijan antes de reintentar; la combinación con lote/unidad NULL legítimos aplica NULLS NOT DISTINCT, y no se eliminan líneas legítimas de asignaciones distintas por una coincidencia de atributos. Se verificará en PREPROD el esquema físico y las restricciones; no se afirma que se hayan ejecutado las restricciones antes de los ensayos.

5.4.2 justifica las consultas; A.16 declara columnas/orden y ámbito físico. El predicado de igualdad abre el índice y el de rango lo acota. Partición permite poda temporal, pero no crea índice ni garantiza unicidad entre meses.

En PostgreSQL 16, una unicidad particionada incluye la clave de partición; un índice local no acredita identidad global (PostgreSQL Global Development Group, 2023). Las identidades globales se conservan en tablas sin partición; el detalle sanitario usa FK/PK/UK compuestas y fecha inmutable.

| Índice sobre | Columnas en orden | Tipo | Ámbito de la unicidad | Consulta o contrato que lo justifica |
| --- | --- | --- | --- | --- |
| `inv_saldo` | `sitio_id`, `ubicacion_id`, `producto_id`, `lote_id`, `unidad_id` | Único NULLS NOT DISTINCT | Sin partición; sitio en grano | Saldo disponible de un lote en una ubicación y en su unidad de medida: la unidad forma parte del grano porque un mismo lote puede estar almacenado en dos unidades y sus cantidades no son comparables sin conversión |
| `inv_lote` | `producto_id`, `numero_lote` | Único | Sin partición | Identidad sanitaria garantizada del lote: producto interno más número declarado. La unicidad es estructural porque `producto_id` es clave primaria del maestro, y por eso esta es la clave que se controla en la captura |
| `inv_lote` | `gtin`, `numero_lote` | Único | Sin partición | Búsqueda por la clave que declara el proveedor. El GTIN canónico del maestro identifica un producto y tiene unicidad global; los GTIN alternativos se resuelven mediante equivalencias verificadas, la asignación de un GTIN ya usado a otro producto se rechaza en la captura y se reporta en la conciliación |
| `inv_lote` | `numero_lote` | No único | Sin partición | Búsqueda asistida por lote cuando no se conoce el producto |
| `inv_unidad_logistica` | `sscc_id` | Único | Con alcance de unidad viva | Resolución de la unidad por SSCC reetiquetado |
| `inv_unidad_contenido` | `unidad_logistica_id`, `lote_id` | No único | Por sitio | Recorrido de unidades de un lote: el lote no es un atributo de la unidad y se resuelve por su contenido |
| `inv_unidad_contenido` | `unidad_logistica_id`, `producto_id` | No único | Por sitio | Composición vigente de una unidad con producto y cantidad |
| `inv_reserva_linea` | `pedido_linea_id`, `reserva_id` | No único | Por sitio | Reserva efectiva de una línea de pedido concreta |
| `inv_movimiento` | `saldo_origen_id`, `fecha_ocurrencia` | No único | Sin partición; filtro temporal cuando aplica | Reconstrucción del saldo desde el movimiento, en orden del instante en que ocurrió |
| `inv_movimiento` | `saldo_origen_id`, `fecha_registro` | No único | Sin partición; filtro temporal cuando aplica | Reconstrucción en orden de registro, que ordena hechos acaídos con el mismo instante de ocurrencia |
| `inv_recepcion_linea` | `recepcion_id`, `secuencia_documento` | Único parcial con `secuencia_documento` no nula | Con la recepción en el ámbito | Identidad de línea cuando el documento de origen numera sus líneas: el ordinal del documento es la autoridad y su repetición dentro de la misma recepción sí es un duplicado |
| `inv_recepcion_linea` | `recepcion_id`, `producto_id`, `lote_id`, `unidad_id` | No único | Con la recepción en el ámbito | Consulta del detalle recibido. No es identidad: dos líneas legítimas pueden compartir producto, lote y unidad con distinta cantidad o posición de origen, y `lote_id` es nulo en los productos que no lo exigen, por lo que la combinación no se declara única |
| `cal_evento_custodia` | `event_id_epcis` | Único | Global, con independencia de la partición | Identificador canónico del evento en el intercambio. La tabla no se particiona precisamente para que esta unicidad sea una restricción real: una clave única sobre una tabla particionada por mes tendría que incluir la columna de partición y solo protegería dentro del mes |
| `cal_evento_custodia` | `ubicacion_id`, `ts_ocurrencia` | No único | Sin partición; filtro temporal de consulta | Eventos ocurridos en una ubicación dentro de un rango de fechas |
| `cal_evento_custodia` | `parent_event_id` | No único | Sin partición; filtro temporal de consulta | Verificación de continuidad de la cadena causal; la raíz del recorrido es el evento sin padre declarado |
| `cal_evento_objeto` | `evento_id`, `secuencia_linea`, `ts_evento` | Único | Mensual por el mes de `ts_evento` | Identidad de la línea de objetos: el ordinal estable del arreglo canónico del perfil, conservado en cada reintento. Dos objetos del mismo evento con el mismo lote y distinta unidad de medida o distinta cantidad son líneas legítimas y quedan admitidas; la clave no contiene columnas nulas, de modo que la unicidad no depende de ningún tratamiento de nulos |
| `cal_evento_objeto` | `lote_id`, `evento_id` | No único | Mensual por el mes de `ts_evento` | Reconstrucción de custodia de un lote: el lote no es atributo de la cabecera y se resuelve recorriendo los objetos, que regresan a la cabecera por `evento_id`. El orden pone primero `lote_id`, que es el predicado que acota el conjunto, y después el evento |
| `cal_evento_objeto` | `unidad_logistica_id`, `evento_id` | No único | Mensual por el mes de `ts_evento` | Historial de una unidad logística; el SSCC se resuelve en `inv_unidad_logistica` y no se almacena en el evento |
| `cal_excursion` | `lote_id`, `inicio` | No único | Sin partición; filtro temporal cuando aplica | Excursiones de un lote; la tensión por producto se obtiene por la asociación declarada, no por una columna de producto inexistente |
| `cal_calibracion` | `sensor_id`, `fecha_calibracion` | No único | Sin partición | Búsqueda de las calibraciones de un sensor en orden de fecha. La vigencia no la resuelve este índice, sino la restricción de no solapamiento entre `fecha_calibracion` y `fecha_vencimiento`, que se declara aparte |
| `cal_regla_termica` | `producto_id`, `version` | Único | Sin partición | Versiones interpretables durante cinco años |
| `cal_regla_termica` | `producto_id` | Único parcial con `vigente_hasta` nula | Sin partición | Una sola versión vigente por producto. Predicado vigente_hasta IS NULL. Adicionalmente, exclusión por producto e intervalo para impedir todo solapamiento histórico; reglas distintas |
| `doc_documento` | `tipo`, `emisor`, `folio`, `version` | Único | Global, con independencia del mes de emisión | Identidad fiscal del documento: la huella no sustituye tipo, emisor, folio y versión. La versión integra la clave porque un documento puede reemitirse o anularse sin cambiar su folio, y la fiscalidad exige que esa identidad sea única en todo el horizonte retenido |
| `doc_documento` | `hash` | No único | Sin partición; filtro por emisión | Detección de contenido repetido; la unicidad real es la fiscal, no la de la huella |
| `doc_pod` | `entrega_id` | No único | Sin partición; filtro temporal cuando aplica | Varias evidencias y varios objetos POD de una misma entrega |
| `doc_pod` | `evidencia_obj_id` | No único | Sin partición; filtro temporal cuando aplica | Resolución de los objetos que componen el POD; la evidencia referenciada es la unificada y no una segunda referencia por objeto |
| `prv_pedido_promesa` | `promesa_id` | Clave primaria individual | Sin partición | Identifica cada ORIGINAL o REVISION y permite la referencia de entrega por UUID |
| `prv_pedido_promesa` | `pedido_id`, `version` | Único | Sin partición | Un ordinal por pedido; conserva todas las revisiones con UUID distintos |
| `prv_pedido_promesa` | `pedido_id`, `vigente_desde` | No único | Sin partición; filtro por vigencia | Lectura de la promesa original y de sus revisiones con la vigencia que las ordena |
| `prv_pedido_promesa` | `pedido_id`, `tipo` | Único parcial con `tipo` igual a `ORIGINAL` | Global, con independencia del mes de captura | Una sola promesa original por pedido sin impedir el historial ilimitado de revisiones. La tabla no se particiona, de modo que la unicidad es real y no una protección limitada al mes |
| `prv_pedido` | `pedido_id` | Único | Sin partición | Clave de negocio del pedido comprometido |
| `rep_entrega` | `pedido_id` | Único | Sin partición | Una entrega por pedido, varios intentos; entrega_id conserva identidad |
| `rep_entrega_linea` | `entrega_id`, `intento_id`, `linea_id`, `asignacion_id`, `unidad_logistica_id` | Único NULLS NOT DISTINCT | Sin partición | Grano fragmento de asignación por intento y unidad; NULL legítimos se comparan iguales. entrega_linea_id conserva identidad idempotente; varias asignaciones se distinguen por asignacion_id |
| `cob_cobro` | `clave_idempotencia` | Único | Global, con independencia del mes de registro | Reintento del cobro sin duplicar el efecto. La restricción es global y se evalúa dentro de la misma transacción que inscribe el cobro y su imputación, de modo que dos intentos concurrentes de la misma operación no pueden pasar ambos |
| `edi_mensaje` | `clave_idempotencia` | Único | Global, con independencia del mes de recepción | Mensaje recibido dos veces con el mismo efecto. La unicidad se comprueba en la ingesta, antes de que el mensaje produzca hechos, y la rechaza completa si ya existe |
| `edi_asn_linea` | `asn_id`, `unidad_logistica_id` | Único | Con el mes de recepción en el ámbito | Varias unidades en un aviso, una línea por unidad; el SSCC se resuelve en `inv_unidad_logistica` y no se almacena en la línea del aviso |
| `gob_auditoria` | `transaction_id` | No único | Sin partición; filtro temporal cuando aplica | Reintento idempotente de una escritura y reconstrucción de su antes y después |
| `gob_excepcion_sync` | `correlacion_id`, `clave` | Único | Sin partición | Idempotencia de la decisión: `clave` es la identidad de la operación que provocó la excepción dentro del ámbito declarado por `correlacion_id`, y su unicidad impide que un reintento registre dos decisiones. No se agrupa por dispositivo porque la entidad no tiene atributo de dispositivo: el origen de la captura viaja en `payload` |
| `gob_excepcion_sync` | `estado`, `fecha` | No único | Sin partición | Seguimiento de excepciones abiertas por antigüedad. `fecha` es el instante en que se registró la excepción y es la columna que da el orden, sin necesidad de una columna de orden adicional |
| `mae_proveedor` | `rut` | Único | Sin partición | Resolución de proveedor por RUT |
| `mae_cliente` | `rut` | Único | Sin partición | Resolución de cliente por RUT |
| `obj_objeto` | `clave` | Único | Sin partición | Resolución de evidencia por clave lógica |
| `cache_stock`, `cache_precio`, `cache_credito`, `cache_identidad`, `cache_manifiesto` | No aplica | No aplica | No aplica | La caché en memoria no admite índice SQL: la versión viaja en el valor y la invalidación la publica el proceso que escribe la fuente |
| `inv_unidad_contenido` | `lote_id`, `unidad_logistica_id` | No único | Por sitio | Recorrido sanitario inverso: localizar todas las unidades de un lote |
| `cal_evento_custodia` | `evento_id`, `ts_ocurrencia` | Único | Sin partición | Destino de FK compuesta de detalle; fuerza timestamp único por identidad de cabecera |

**Tabla A.16 - Índices declarados, columnas, orden y ámbito de unicidad**

*Fuente: elaboración propia de LafroX a partir de los atributos reales del Anexo 5-A, de los accesos declarados en 5.1 y de PostgreSQL 16 como motor de referencia.*

Documento usa identidad fiscal, no hash único. Lote se relaciona con unidad por contenido e índices en ambos sentidos. ORIGINAL tiene unicidad parcial global y evento/cobro/mensaje no se particionan. Caché no admite índice SQL; 5-G define versión/invalidación. Los planes y restricciones se comprobarán en PREPROD.

<a id="tab-a18-particionamiento"></a>

| Tabla o familia | Clave de partición | Motivo declarado | Relación con la política de retención |
| --- | --- | --- | --- |
| `cal_evento_objeto` | Mes de `ts_evento` | Es la única tabla de custodia particionada, y usa una copia mantenida del instante del evento porque no tiene fecha propia | Permite retirar meses completos al vencer el plazo del expediente del lote |
| `cal_excursion` | Sin partición | UUID global referenciado; índices selectivos y mantenimiento acotado | Archivo/borrado por lotes elegibles, conservando expediente vigente |
| `cal_bloqueo` | Sin partición | UUID global referenciado; índices selectivos y mantenimiento acotado | Archivo/borrado por lotes elegibles, conservando expediente vigente |
| `tel_serie_consolidada` | Mes del día local del sitio | Se consulta por día y por sensor | Permite eliminar por mes al cumplir cinco años |
| `gob_auditoria` | Sin partición | UUID global referenciado; índices selectivos y mantenimiento acotado | Archivo/borrado por lotes elegibles, conservando expediente vigente |
| `inv_saldo` | Sin partición | UUID global referenciado; índices selectivos y mantenimiento acotado | Archivo/borrado por lotes elegibles, conservando expediente vigente |
| `inv_movimiento` | Sin partición | UUID global referenciado; índices selectivos y mantenimiento acotado | Archivo/borrado por lotes elegibles, conservando expediente vigente |
| `doc_pod` | Sin partición | UUID global referenciado; índices selectivos y mantenimiento acotado | Archivo/borrado por lotes elegibles, conservando expediente vigente |
| `hech_entrega`, `hech_entrega_intento`, `hech_linea_venta` y `hech_actividad_costo` | Mes del hecho | Hechos inmutables de alta escritura | La retención sigue a la fuente transaccional del hecho |

**Tabla A.17 - Particionamiento declarado y su relación con la retención**

*Fuente: elaboración propia de LafroX a partir de PostgreSQL 16 Table Partitioning y de la matriz de retención del Anexo 5-D.*

El detalle sanitario mantiene ts_evento=ts_ocurrencia y no admite cambios posteriores. Mes es ámbito físico; filtro por mes no implica partición. Se retira una partición completa solo si todo su contenido es elegible y ningún expediente sigue vigente; en otro caso se aplica eliminación por filas verificadas.


<a id="anexo-5g"></a>


## Anexo 5-G. Claves de caché, vigencia e invalidación

Las claves/versiones siguen cache_* de 5-A y S4 §§4.1.3.6–7, Anexo 4-O, ADR-06. La autoridad incrementa versión e invalida por outbox; Redis se reconstruye desde ella. Sin enlace, lectura fechada/indicativa; reserva, cobro y precio requieren al escritor competente.

- **Permisos:** actor/sitio/versión; credencial 8 h bodega o 14 h terreno. Cambio de rol/sitio invalida; vencimiento bloquea el turno. Relevos preinscritos se verifican con PIN.
- **Manifiesto:** versión/huella/objetos, firmado por Keycloak, 26 h; renovación horaria con enlace o cambio de turno. Verificador comprueba firma/vigencia y avisa antes de vencer; no es Redis ni extiende la credencial.
- **Identidad de consulta:** cliente/sitio/versión, 24 h; cambio de maestro/manifiesto refresca, sin autorizar operaciones.
- **Saldo:** sitio/ubicación/producto/lote/unidad/versión, 5 min en pantalla; movimiento invalida y refresca o marca dato indicativo.
- **Precio:** GTIN/canal/versión hasta vigente_hasta; nueva tarifa invalida, con vigencia pendiente hasta validación.
- **Crédito:** cliente/versión hasta cambio de condición o 8 h de credencial; cambio de saldo/condición invalida, con restricción visible.
- **Maestros:** familia/clave/versión hasta nueva publicación; reemplazo refresca sitios, productos y unidades.
- **Evidencia:** clave lógica/huella/versión; captura/intercambio refresca objetos y exige hash antes de aceptar.
- **Consulta local:** objeto/versión de manifiesto, 24 h; actualización refresca stock/precio/crédito. PWA conserva catálogo/precios fechados, validación definitiva en M3.
- **Pendientes:** dispositivo o cuenta/UUID/versión de cola, sin TTL antes de resolución. Room/SQLite o IndexedDB conserva payload/evidencia/resultado; UUID vincula al pedido central tras acuse. Resolución publica estado; purga sigue 5-D, sin tratar evidencia como caché.

<a id="anexo-5h"></a>

## Anexo 5-H. Fórmulas de indicador, linaje documental y catálogo por fase

5.2.6 desarrolla fórmulas y casos sin base: OTIF sobre ORIGINAL, exactitud por cantidades homologadas y desviación monetaria ≤0,3 %. A.18–A.19 detallan el catálogo con linaje, audiencias y latencias; SSCC/lote se exigen según hito y producto, admitiendo VACIA/ABIERTA y exentos. Costo de servir inicia E2.

Las claves fecha_key se derivan del origen y se convierten al calendario de la zona IANA del sitio, conservando el instante UTC; no se sustituyen por el día de carga ETL. hech_entrega usa la fecha de la promesa ORIGINAL, incluidos pedidos no entregados; hech_entrega_intento, la fecha_intento; hech_linea_venta, la fecha de negocio de la venta en origen; hech_movimiento_stock, la fecha_ocurrencia del movimiento; hech_actividad_costo, la fecha de negocio de la actividad trazada; hech_excursion, su inicio. Al medir relleno o intentos sobre pedidos comprometidos, el período y denominador se obtienen de la ORIGINAL del pedido, aunque sus hechos se ejecuten en otra fecha. Las versiones de dimensiones se seleccionan por la fecha del hecho dentro de su intervalo, no por la versión vigente al cargar. Un origen sin fecha válida se aísla y se informa; no se inventa una fecha ni se asigna una futura arbitraria.

La Tabla A.18 define fórmula, grano, período, casos sin dato y linaje de cada indicador; A.19 fija fase, audiencia y latencia. El linaje documental registra origen, transformación, fórmula, versión y responsable; la automatización deseable no ofertada en T-12 queda fuera del alcance.
<a id="tab-a20-formulas"></a>

| Indicador | Fórmula exacta y granularidad | Linaje documental | Periodo | Regla para el caso sin dato |
| --- | --- | --- | --- | --- |
| Entrega completa y a tiempo | 100 × pedidos completos en ventana ORIGINAL / todos los comprometidos, una vez; sin filtro de vigencia | `prv_pedido`, `prv_pedido_linea`, `prv_pedido_promesa`, `rep_entrega`, `rep_entrega_linea`, `hech_entrega`, `hech_entrega_intento` | Cierre diario | El pedido comprometido sin entrega cuenta en el denominador y no en el numerador; su número se reporta aparte |
| Intento de entrega | Por día y por cliente: cociente entre pedidos con al menos un intento de entrega y pedidos comprometidos | `prv_pedido`, `rep_intento`, `hech_entrega_intento` | Cierre diario | Un intento en estado desconocido no se convierte en entrega ni en ausencia de visita |
| Relleno de pedido | Por día, cliente y línea: cien por el cociente entre la cantidad entregada y la cantidad pedida, en la unidad de la línea | `prv_pedido_linea`, `rep_entrega_linea`, `hech_linea_venta` | Cierre diario | Una línea sin cantidad pedida válida se excluye del denominador y se reporta como no evaluable |
| Exactitud de inventario | 100 × max(0,1−Σ diferencias absolutas / Σ cantidades contadas homologadas); base cero N/A | `inv_conteo`, `inv_conteo_detalle`, `inv_saldo` | Cierre de cada conteo | Un conteo con cantidad contada declarada en cero y diferencia declarada se reporta como no evaluable |
| Trazabilidad reconstruible | Cien por el cociente entre las consultas de trazabilidad respondidas completas y las consultas solicitadas, por lote y por tipo | `cal_evento_custodia`, `doc_pod`, `obj_objeto`, `obj_manifiesto` | Inmediata en línea | Una consulta respondida parcialmente se cuenta como no respondida y se informa el evento faltante |
| Integridad de lote en recepción | 100 × líneas completas / líneas que requieren lote al cierre; SSCC según hito | `inv_recepcion`, `inv_recepcion_linea`, `inv_lote`, `inv_unidad_logistica` | Captura y cierre diario | Una recepción con líneas sin lote no cuenta en el numerador |
| Tensión térmica por producto | Número de excursiones sobre el total de ventanas evaluadas, por producto y por período | `cal_excursion`, `cal_regla_termica`, `cal_asociacion_ventana`, `cal_lectura` | Cierre mensual | Una ventana sin ninguna lectura se excluye del denominador y se reporta como pérdida de cobertura |
| Exposición térmica consolidada | Promedio ponderado por número de lecturas de la temperatura consolidada dentro y fuera de rango | `tel_serie_consolidada`, `cal_regla_termica` | Cierre mensual | Una serie sin lecturas no se promedia y se reporta como sin dato |
| Vencimientos y riesgo de caducidad | Conteo de lotes por ventana de vencimiento y por sitio, con la cantidad asociada | `inv_lote`, `inv_saldo`, `dim_producto` | Cierre diario | Un lote sin fecha de vencimiento exigida se reporta aparte y no se imputa a ninguna ventana |
| Cobertura de frío y disponibilidad de cadena de frío | Por sitio y por día: porcentaje de tiempo con cámara o vehículo con lectura dentro de la ventana térmica vigente | `cal_sensor`, `cal_asociacion_lectura`, `cal_lectura`, `tel_serie_consolidada` | Cierre diario | Un sensor sin lectura se cuenta como no disponible, nunca como disponible |
| Reparto, causales y reentrega | Por día y por zona: cociente entre pedidos entregados y pedidos con intento, con distribución por causal de resultado | `rep_intento`, `rep_causal`, `rut_viaje`, `rut_parada` | Cierre diario | Una causal no catalogada se reporta como categoría propia y no se reparte en las demás |
| Devoluciones y su causa | Por mes, cliente y causa: cantidad e importe devueltos sobre cantidad e importe entregados | `rep_devolucion`, `rep_devolucion_linea`, `rep_entrega_linea` | Cierre mensual | Una devolución sin causa catalogada se mantiene con la causa sin declarar y se excluye del indicador por causa |
| Rendición y diferencia de turno | Por turno, sitio y responsable: diferencia entre efectivo declarado y efectivo contado, en moneda | `cob_rendicion`, `cob_cuadratura`, `cob_descuadre` | Cierre de turno | Un turno sin conteo declarado se reporta como no evaluable |
| Cobranza y aplicación | Por mes y cliente: importe aplicado sobre importe facturado del período | `cob_cobro`, `cob_aplicacion`, `cob_saldo`, `cob_compensacion` | Cierre mensual | Un cobro sin aplicación se informa como pendiente con su antigüedad, no como aplicado |
| Disponibilidad de la explotación analítica | Marca de última consolidación expuesta y vigente, por ambiente y por tablero | `hech_entrega_intento` y marca de consolidación | Cinco minutos en el día, dos horas en el cierre, cuatro horas en la gestión | Un tablero sin marca vigente se declara no disponible y no publica un valor antiguo como actual |
| Costo por cliente y entrega | Suma del costo asignado por entrega y por cliente según el criterio declarado, sobre el número de entregas completas | `hech_actividad_costo`, `hech_entrega`, `dim_cliente` | Cierre mensual, a partir de E2 | Una entrega sin actividad de costo se informa como sin dato de costo, no como costo cero |

**Tabla A.18 - Fórmulas exactas, granularidad y linaje documental**

*Fuente: elaboración propia de LafroX a partir de RT-05.25 a RT-05.29 de las Bases Técnicas Transversales (PUCV, 2026d), de S3 sobre indicadores y de los atributos del Anexo 5-A.*

OTIF usa todos los pedidos comprometidos del período una vez, incluidos no entregados, y exige completar todas sus líneas dentro de la ventana ORIGINAL inmutable. La fila analítica se identifica por pedido_id y conserva la ORIGINAL; entrega_id y ruta_sk pueden ser NULL hasta que existan sus hechos operativos. No se crean entregas ni rutas ficticias para cargar el denominador. Las duraciones sin instantes suficientes son NULL, no cero; la ausencia de entrega no retira al pedido comprometido del cálculo. No filtra por vigencia actual ni por existencia de entrega. La exactitud por cantidades homologa unidades y declara base cero; la desviación monetaria usa valor contable del sitio y el umbral ≤0,3 %, sin confundir ambos indicadores.

<a id="tab-a21-catalogo-indicadores"></a>

| Fase | Audiencia | Objetivo | Indicadores y KPI | Dimensiones y filtros | Profundización | Frecuencia y latencia máxima | Exportación |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Recepción y bodega | Supervisor de bodega y calidad | Trazabilidad e integridad del ingreso | Integridad de lote, cobertura de lectura, cobertura de frío y disponibilidad de cadena de frío, vencimientos | Sitio, fecha, producto, canal, tipo de evento | Hasta línea de recepción y lectura | Diaria y continua; cinco minutos | CSV y Parquet programado |
| Preparación y despacho | Supervisor de preparación | Cumplimiento del compromiso de salida | Relleno de pedido, tiempo de preparación, picking sin incidencia | Sitio, fecha, cliente, zona, misión | Hasta línea y asignación | Continua; cinco minutos | CSV y Parquet programado |
| Reparto | Supervisor de reparto y operación | Servicio entregado y causa del no cumplimiento | Entrega completa y a tiempo, intento de entrega, causales, reentrega | Día, zona, ruta, conductor, resultado | Hasta intento y línea de entrega | Continua; cinco minutos | CSV y Parquet programado |
| Calidad y sanitario | Calidad y responsable sanitario | Exposición térmica y disposición de lote | Tensión térmica por producto, excursiones, bloqueos y resoluciones, cobertura de frío y disponibilidad de cadena de frío | Producto, lote, sitio, ventana, severidad | Hasta lectura y regla aplicada | Diaria y mensual; cinco minutos y cierre mensual | CSV y Parquet programado |
| Cobranza y finanzas | Cobranza y tesorería | Recuperación y control de caja | Cobranza y aplicación, rendición y diferencia de turno, cuentas de envases | Mes, cliente, turno, responsable, causal | Hasta cobro, pago y documento | Diaria y de cierre de turno; dos horas | CSV y Parquet programado |
| Gestión | Gerencia | Cumplimiento del contrato y del caso | OTIF consolidado, cobertura del plan, costo por cliente y entrega en E2, calidad de datos | Mes, cliente, sitio, producto, canal | Hasta pedido, entrega y documento | Cierre diario; cuatro horas | Exportación integral con manifiesto |
| Plataforma | Responsable de datos de LAFROX | Salud de la plataforma | Latencia de consolidación, cobertura de datos, excepciones de sincronización, incidentes | Ambiente, módulo, dispositivo, periodo | Hasta tablero, consulta y excepción | Continua; cinco minutos | CSV y Parquet programado |

**Tabla A.19 - Catálogo de indicadores por fase, audiencia, latencia y exportación**

*Fuente: elaboración propia de LafroX a partir de S3 3.4, de RT-05.25 a RT-05.29 de las Bases Técnicas Transversales (PUCV, 2026d) y de las fases del Artículo 17 de las Bases Administrativas (PUCV, 2026b).*

Consulta operativa puntual usa API/caché válida; BI pesado usa Redshift. Latencias: ≤5 min operativo, ≤2 h desde último retorno para cierre y ≤4 h gerencial. Cada tablero muestra consolidación y pendientes; la exportación programada conserva alcance/manifest/hash/conteo según 5.2.8.


<a id="anexo-5i"></a>

## Anexo 5-I. Matriz de trazabilidad de RT-05 con su evidencia

A.20 vincula cada RT-05 con desarrollo verificable en cuerpo/anexo. RT-05.10/.24/.30 siguen siendo deseables no ofertados según T-12; diccionario, linaje documental y fórmulas no se presentan como esas capacidades automatizadas.
<a id="tab-a22-rt05"></a>

| Requisito | Apartado que lo atiende | Evidencia comprobable en la fuente | Anexo que lo desarrolla |
| --- | --- | --- | --- |
| RT-05.01 Modelo y diccionario | 5.1.1 a 5.1.11 | Nueve vistas lógicas distribuidas entre cuerpo y 5-M, sin duplicaciones; diccionario de 111 entidades y 791 atributos con tipo, dominio, obligatoriedad, propietario y sensibilidad | 5-A y 5-B |
| RT-05.02 Paradigma y motor por dominio | 5.1.1 y 5.2.1 | Tabla de índices y almacenes; posición declarada entre consistencia y disponibilidad por dominio; sin credenciales contadas como tecnología de persistencia | 5-B |
| RT-05.03 Trazabilidad de la operación | 5.2.2 | el contrato de escritura de 5.2.2 con cambio, auditoría y outbox en la misma transacción del motor dueño; `gob_auditoria` con actor, dispositivo, instante, resultado y valores anterior y posterior | 5-A y 5-J |
| RT-05.04 Calidad de datos | 5.2.5 | Perfil por población, regla, umbral, dueño, resolución y tablero con profundización; ISO/IEC 25012 (International Organization for Standardization, 2008) como referencia de dimensiones, no de cifras propias | 5-C y 5-H |
| RT-05.05 Separación transaccional y analítica | 5.1.1 y 5.2.6 | Consumo en S3, Glue, Redshift Serverless y QuickSight; el almacén transaccional no ejecuta analítica pesada | 5-B |
| RT-05.06 Exportación íntegra sin costo adicional | 5.2.8 | Operación autónoma con tablas, series y objetos, formatos abiertos, relaciones y diccionario, manifiesto con huella y conteo, permiso, seguimiento, reintento, validación y descarga | 5-H |
| RT-05.07 Retención, archivado y eliminación | 5.2.7 | Matriz por dominio con inicio de plazo, en línea y archivo, ubicación y réplica, bloqueo legal, eliminación de derivados y evidencia | 5-D y 5-F |
| RT-05.08 Datos personales conforme al Art. 85 | 5.2.7 y 5.1.10 | Clasificación `AL`, `CR` y `ME` por atributo con cifrado en reposo, cifrado a nivel de campo, mínimo privilegio y consulta auditada | 5-E |
| RT-05.09 Gestión de datos maestros | 5.1.3 | Maestro con dueño y aprobador por familia, vigencia, equivalencias entre ERP, WMS y EDI, propagación, conflicto y conciliación; la identidad del lote no se fusiona por semejanza | 5-A y 5-C |
| RT-05.10 Catálogo con linaje automatizado, deseable | 5.2.6 y Anexo 5-H | No ofertado como capacidad automatizada; se entrega trazabilidad documental de origen, transformación, fórmula, versión y responsable | 5-H |
| RT-05.11 Plan de migración | 5.3.1 a 5.3.6 | Alcance, volumen `32,11 GB` con rango `30,73` a `33,49 GB`, origen, reglas, criterios de calidad, oleadas, reversión y responsables | 5-J |
| RT-05.12 Perfilado y saneamiento previos | 5.3.2 | Perfilado por conjunto, categoría excluyente, original preservado, causa tipificada y decisión del responsable | 5-C y 5-J |
| RT-05.13 Dos ensayos completos en preproducción | 5.3.4 y 5-L | Dos ensayos completos e independientes antes del corte, con extracción, transformación, carga, conciliación, delta y reversión | 5-J |
| RT-05.14 Conciliación cuantitativa | 5.3.5 | Conciliación del universo de origen/destino por claves, recuentos y sumas; muestreo dirigido complementario; cero diferencias no explicadas | 5-J |
| RT-05.15 No migrados accesibles en consulta | 5.3.3 | Repositorio de consulta con inventario, formato, localización, búsqueda, dueño, plazo, permisos y prueba de consulta | 5-D y 5-J |
| RT-05.16 Servicios síncronos y flujos por evento | 5.2.2 y 5.2.4 | Contratos en OpenAPI 3.1 y AsyncAPI 2.6 o superior generados desde el código, con versión semántica | Subdocumento 4 |
| RT-05.17 Obsolescencia y preaviso | 5.2.4 | Política de versiones con preaviso mínimo de seis meses y tabla de equivalencias entre sistemas | 5-C |
| RT-05.18 Autenticación entre sistemas | 5.2.4; S4 4.1.3.5 y 4.1.3.7 | Autenticación de servicios mediante mTLS y credenciales rotadas; las credenciales de turno de personas son un control distinto | S4; 5-E |
| RT-05.19 Registro de entrada y salida con correlativo | 5.2.2 | `transaction_id` y `correlacion_id` en auditoría, evento, excepción de sincronización y mensaje; instantes de ocurrencia y de registro diferenciados | 5-A y 5-J |
| RT-05.20 Capa anticorrupción | 5.2.4 | Traducción de integraciones heredadas y de terceros con equivalencias tipadas y validación de versión antes del efecto | 5-B |
| RT-05.21 Declaración por integración | 5.2.4; S4 Anexos 4-G/4-H/4-I | Catálogo INT con modo, volumen, ventana de contraparte y comportamiento sin respuesta; no sustituido por una prueba genérica | S4 |
| RT-05.22 Carga y descarga masiva | 5.2.8 | Carga operativa por rol CLIENTE, validación previa, aceptación parcial por registro independiente, informe de errores y reintento idempotente; descarga abierta | 5-C y 5-J; S4 Anexo 4-C |
| RT-05.23 Estándares sectoriales | 5.1.7 y 5.1.9 | Subconjunto declarado de EPCIS 2.0 y CBV 2.0 (GS1, 2022a, 2022b) con identificadores canónicos y etiquetas españolas separadas; equivalencias GS1 en EDI | 5-A |
| RT-05.24 Portal de desarrolladores, deseable | 5.4.6 | No ofertado; no hay compromiso de portal y no se describe ninguno | No aplica |
| RT-05.25 Capa analítica con tableros | 5.2.6 | Catálogo de indicadores por fase con audiencia, objetivo, fórmula, dimensiones, filtros, profundización, frecuencia y latencia | 5-H |
| RT-05.26 Filtros y profundización | 5.2.6 | Filtros por período, unidad organizacional y dimensión, con profundización hasta pedido, entrega, línea y documento | 5-H |
| RT-05.27 Autoservicio y modelo semántico | 5.2.6; S4 4.1.4.7 y 4.2.2.4, N-10 | Autoría QuickSight autónoma con permisos separados; grano, relaciones, fórmulas y casos límite documentados en el modelo semántico | 5-H; S4 |
| RT-05.28 Exportación de informes | 5.2.6 y 5.2.8 | Informes exportables y envío por calendario bajo permisos CLIENTE; exportación íntegra con manifiesto, huella y conteo | 5-H |
| RT-05.29 Latencia máxima de disponibilidad analítica | 5.2.6 y 5.4.1 | Operativa de hasta cinco minutos desde el hecho, cierre de hasta dos horas desde el último retorno y gerencial de hasta cuatro horas | 5-H y 5-J |
| RT-05.30 Analítica predictiva, deseable | 5.2.6 | No ofertado; no se promete predicción ni se la describe como capacidad disponible | No aplica |

**Tabla A.20 - Matriz de trazabilidad de RT-05 con evidencia comprobable**

*Fuente: elaboración propia de LafroX a partir del bloque RT-05 de las Bases Técnicas Transversales (PUCV, 2026d), del Formulario T-12 sobre capacidades ofertadas y no ofertadas y del contenido de los apartados citados del Subdocumento 5.*

RT-05.16/.17/.20 se desarrollan en S4: contratos desde código, versiones y capa anticorrupción. S5 conserva el vínculo y las reglas de datos, sin duplicar esa arquitectura.


<a id="anexo-5j"></a>

## Anexo 5-J. Protocolo de aceptación de datos y pruebas propuestas

La prueba de retiro ≤2 h sigue el recorrido de 5.1.7 y contrasta todas las autoridades con carga/ruta/despacho previos. Calidad y cada sede verifican existencias/destinatarios, conductores aportan pendientes y Finanzas valida documentos. Clientes planificados con el lote offline se contactan/bloquean como potenciales, sin declararlos entregas confirmadas. Tras 30 min sin respuesta se escala a Operaciones manteniendo cobertura preventiva.

El presupuesto de 85 min es estimación de diseño, no resultado medido. La prueba ≤2 h debe demostrar cobertura del universo expuesto/potencial, lista de contactos, bloqueos, evidencias pendientes y escalamiento; un resultado parcial sin identificar el universo potencial falla aceptación. Casos offline y restauración forman parte del ensayo.

Las Tablas A.21–A.23 especifican pruebas propuestas de migración, desempeño y trazabilidad/calidad/seguridad, con precondición, datos/carga, acción, umbral, período, evidencia y responsable. Su aceptación requiere registrar los resultados; no se presentan como pruebas ejecutadas.

Las pruebas son propuestas sin resultados ni aceptación del CLIENTE acreditados.
<a id="tab-a23-pruebas-migracion"></a>

| Prueba | Precondición y conjunto de datos | Carga y acción | Umbral numérico de aceptación | Evidencia y responsable |
| --- | --- | --- | --- | --- |
| Perfilado de origen | Extracción de solo lectura del ERP y del WMS de Talca y de las planillas de las demás sedes | Perfilado por conjunto con el catálogo declarado | Informe con el cien por ciento de los conjuntos previstos y conteo, distribución y versión del código por conjunto | Informe de perfilado; responsable de datos LAFROX |
| Reconciliación de conteos | Conjunto cargado y su contraparte en origen | Conteo por producto, lote, unidad y sitio | Diferencia cero o diferencia explicada y aprobada por regla declarada; toda diferencia sin regla se rechaza | Registro de conciliación con su aprobación; responsable de migración y CLIENTE |
| Reconciliación de agregados | Saldos, importes y cantidades ya conciliados por clave | Suma agregada por producto, cliente y corte | Diferencia cero al redondeo declarado, con el redondeo publicado en el informe | Informe de agregados; responsable de datos LAFROX |
| Integridad referencial en destino | Destino cargado | Recorrido del grafo de claves foráneas buscando filas huérfanas | Cero huérfanos en claves foráneas dentro del mismo motor | Reporte de huérfanos; responsable técnico |
| Explicación de diferencias | Diferencias detectadas en la conciliación | Cada diferencia se explica, se autoriza y se registra con su evidencia | Cero diferencias explicadas sin registro; cero diferencias aceptadas sin responsable identificable | Registro de decisiones; responsable de negocio del CLIENTE por rol |
| Muestra de trazabilidad | Lotes con más de una recepción, unidades reetiquetadas y devoluciones | Seguimiento completo desde recepción hasta entrega con su evidencia | Conciliación completa del universo migrado y trazabilidad verificable; diferencias no explicadas cero. Muestra dirigida complementaria, sin sustituir controles completos | Evidencia de la muestra con su veredicto; calidad |
| Ensayo completo en preproducción | Entorno PREPROD con componentes y conjunto completos | Ensayo completo con extracción, transformación, carga, índices, delta, conciliación y reversión, midiendo su duración total | Dos ensayos completos e independientes antes del corte, con duración total registrada y diferencia de conciliación cero en ambos | Acta de ensayo con su duración y su resultado; responsable de migración y CLIENTE |
| Reversión | Punto de control y respaldo declarados | Se detiene el escritor nuevo, se identifican las operaciones posteriores al corte, se aplica el delta conciliado y se restaura el destino | Destino consistente con el punto de control en el cien por ciento de las claves verificadas y cero operaciones posteriores no identificadas | Evidencia de reversión con conteos; responsable de migración |
| Idempotencia de carga | Conjunto de entrada con su versión de carga | Se carga dos veces el mismo conjunto | Estado resultante idéntico y cero duplicados en claves naturales | Comparación de conteos y huellas; responsable técnico |
| Eventos fuera de orden y duplicados | Conjunto de mensajes con clave de idempotencia, versiones y tiempos de ocurrencia fuera de secuencia | Se reproducen mensajes duplicados, tardíos y desordenados dentro y fuera de la ventana de deduplicación | Cero efectos duplicados y cero eventos aplicados fuera de versión | Registro de inbox y de efectos; responsable técnico |
| Cartera viva y no migrados | Cartera con saldos vivos más dos años de historia | Se carga la cartera viva y se habilita el repositorio de consulta de lo no migrado | Cien por ciento de los saldos vivos cargados con su saldo; acceso de consulta probado con evidencia de una búsqueda real | Acta de cierre de cartera; finanzas del CLIENTE |

**Tabla A.21 - Pruebas de aceptación de la migración con umbral numérico**

*Fuente: elaboración propia de LafroX a partir de RT-05.11 a RT-05.15 de las Bases Técnicas Transversales (PUCV, 2026d), del Artículo 17 de las Bases Administrativas (PUCV, 2026b) y de la estrategia de migración de 5.3.*

En las pruebas de A.22, p95 se mide desde la acción de la persona usuaria, con el perfil completo de 5.4.1 y resultados por operación, no solo la media global. Máximos: consulta simple API 500 ms; escritura API 800 ms; preparación 1 s; entrega/acuse durable local 2 s; línea de preventa 1,5 s; consulta stock/crédito extremo a extremo 2 s; búsqueda compuesta 3 s; informe estándar 30 s. Son umbrales de las Bases Técnicas Transversales (PUCV, 2026d) §9.1 y del caso §15; el acuse local no implica consolidación central, que mantiene 10 min móvil/2 h sitio desde reconexión. Cada ensayo dura al menos quince minutos por nivel de carga; estrés continúa hasta saturación y la recuperación debe volver a esos umbrales en ≤5 min tras retirar el exceso.

<a id="tab-a24-pruebas-desempeno"></a>

| Prueba | Precondición y carga | Acción | Umbral numérico de aceptación | Periodo y responsable |
| --- | --- | --- | --- | --- |
| Carga normal | 12,30 TPS sostenidos, con el reparto de contribución declarado entre componentes | Ejecución de la mezcla de operaciones declarada | Cero pérdida y cero duplicado; p95 por operación dentro de los máximos numéricos precedentes | Medido por quince minutos; arquitectura |
| Carga de pico | 14,66 TPS sostenidos | misma mezcla | Cero pérdida; p95 por operación dentro de los máximos numéricos precedentes | Medido por quince minutos; arquitectura |
| Carga de holgura | 21,99 TPS sostenidos, que es 1,5 veces el pico | misma mezcla | Cero pérdida y cero duplicado; p95 por operación dentro de los máximos precedentes; retraso de consolidación ≤10 min móvil/≤2 h sitio desde reconexión | Medido por quince minutos; arquitectura |
| Crecimiento esperado | 17,03 TPS en nube/portal y 3,15 TPS en Talca | misma mezcla | Cero pérdida dentro del reparto declarado de capacidad | Medido por quince minutos; arquitectura |
| Capacidad independiente | 43,98 TPS en nube/portal y 8,05 TPS en Talca | misma mezcla | Cero pérdida y cero duplicado | Medido por quince minutos; arquitectura |
| Estrés y recuperación | Carga por encima del pico sostenido hasta el límite declarado y retirada | Se sostiene el estrés y se deja el sistema volver a la carga normal | Recuperación a los máximos p95 precedentes en ≤5 min después de retirar el estrés | Medido; arquitectura |
| Latencia de lectura con caché | Repetición sobre la misma clave dentro de su vigencia | Lectura repetida | p95 consulta API ≤500 ms y stock/crédito extremo a extremo ≤2 s; cero consultas al origen en el camino cacheado | Medido por quince minutos; arquitectura |
| Latencia de escritura transaccional | Confirmación de una operación con escritura, auditoría y publicación de evento | Confirmación de la operación | p95 escritura API ≤800 ms; confirmación local preparación ≤1 s, preventa ≤1,5 s y entrega ≤2 s; consolidación según 5.2.3 | Medido; responsable funcional del dominio |
| Idempotencia de escritura | Reintento de la misma clave de operación | Reintento | Exactamente una operación efectiva por clave, con el inbox y el efecto confirmados en la misma transacción | Medido; responsable técnico |
| Retención y eliminación | Clase de datos vencida con su procedimiento declarado | Ejecución del procedimiento | Filas eliminadas, conteo registrado, clave destruida con granularidad compatible y respaldo verificado | Por clase; seguridad |
| Reconstrucción de caché | Pérdida total de la caché de lectura | Reconstrucción desde la autoridad | Cien por ciento de las claves reconstruidas sin pérdida de dato y ninguna reserva o cobro confirmado por la caché | Medido; arquitectura |
| Caída de red de área amplia | Registro en terreno sin conexión durante catorce horas y reconexión posterior | Captura, sincronización y conciliación | Cero pérdidas y cero duplicados; sincronización de dispositivo dentro de diez minutos y del centro dentro de dos horas tras la reconexión | Medido; operación |

**Tabla A.22 - Pruebas de aceptación de desempeño con umbral numérico**

*Fuente: elaboración propia de LafroX a partir de RT-05.29 de las Bases Técnicas Transversales (PUCV, 2026d), de los escenarios de carga de S4 declarados en 5.4.1 y de la matriz de retención del Anexo 5-D.*

<a id="tab-a25-pruebas-operacion"></a>

| Prueba | Conjunto de datos | Acción | Umbral numérico de aceptación | Evidencia y responsable |
| --- | --- | --- | --- | --- |
| Cadena de custodia completa | Lotes con unidades, contenido y eventos encadenados | Seguimiento de recepción a entrega verificando eslabones y su relación causal | Todos los eslabones presentes, encadenados y con la clave de origen declarada; cero evento raíz con padre | Evidencia de la cadena; calidad |
| Búsqueda exacta y asistida | GTIN y lote conocidos, y lote homónimo de otro producto | Búsqueda exacta y búsqueda asistida por lote | La búsqueda exacta entrega un único lote; la asistida entrega los homónimos y exige confirmación del producto antes de mostrar trazabilidad | Registro de ambas consultas; calidad |
| Varias recepciones del mismo lote | Lote recibido en dos recepciones con unidades distintas | Recorrido de retiro del lote | El recorrido distingue lo determinable por unidad de lo que solo se determina por evidencia agregada; no se inventa una recepción única | Informe del recorrido con su clasificación; calidad |
| Mezcla, reempaque y devolución | Unidad con contenido modificado y devolución posterior | Seguimiento de la composición y del saldo | Composición vigente y saldo consistentes antes y después del reempaque; la devolución figura en el saldo del cliente y en la rendición de envases | Evidencia de composición; inventario |
| Retiro con terreno desconectado | Operación de terreno durante catorce horas sin WAN | Retiro, consulta local y escalamiento | El retiro identifica universo confirmado/potencial en ≤2 h; presupuesto de diseño 85 min a validar, con última sincronización, pendientes y escalamiento registrados; el estado de trazabilidad local se declara con su fecha | Registro de la operación con su bitácora; operación |
| Restauración por clase | Respaldo y punto de control declarados | Restauración de trazabilidad, de documentos y de geo | Trazabilidad restaurada en menos de dos horas; documentos y temperatura en menos de ocho; geo y auditoría en menos de veinticuatro | Acta de restauración con tiempo medido; arquitectura |
| Integridad referencial en destino | Destino cargado | Recorrido del grafo de claves foráneas buscando filas huérfanas | Cero filas huérfanas en claves foráneas dentro del mismo motor | Reporte de huérfanos; responsable técnico |
| Conflicto de cantidad | Reserva sobre saldo insuficiente | Intento de reserva | Rechazo con causa `RESERVA_EXCESIVA` y saldo inalterado | Registro del rechazo; inventario |
| Duplicado de clave de negocio | Dos intentos con el mismo GTIN y lote | Segundo intento | Rechazo por unicidad con causa tipificada | Registro del rechazo; inventario |
| Integridad de documento | Archivo almacenado con huella registrada | Alteración del archivo y verificación | Rechazo por huella no coincidente, alerta y preservación del original | Registro de verificación; documentos |
| Terminal de pago tardío | Cobro con POS pendiente y segundo pago alternativo | Consulta de la operación y aplicación del segundo pago | El pago se mantiene pendiente hasta que la compensación autorizada lo resuelva; cero efecto duplicado interno; posible cargo externo tardío detectado, conciliado y compensado según contrato | Registro de la compensación; cobranza |
| DTE previo al movimiento | Emisión fiscal, carga de vehículo y POD | Secuencia de emisión, habilitación de traslado y evidencias | Cero movimiento sin documento emitido previamente; acuse técnico del SII y recibo de mercaderías presentes y distinguidos | Expediente del caso; documentos |
| Representación en papel | Receptor no habilitado para el documento electrónico | Emisión y representación | El expediente contiene el documento electrónico y su representación en papel conforme a S4; cero timbre móvil posterior | Expediente del caso; documentos |
| Regla de retención por atributo | Atributo con plazo menor que el de su entidad | Vencimiento del atributo | El atributo se elimina y el resto de la entidad se conserva; la auditoría no permite reconstruir el dato vencido | Registro de la eliminación; seguridad |
| Exportación íntegra | Conjunto con tablas, series, objetos y metadatos | Exportación del CLIENTE sin costo adicional | Un conjunto con relaciones y diccionario, manifiesto con huella y conteo, validación previa y descarga; una auditoría de posición vencida no se incluye | Manifiesto de exportación; responsable de datos LAFROX |
| Serie térmica de cinco años | Serie detallada y sus asociaciones, regla y calibración | Consulta e interpretación de una serie de hace más de un año | La serie detallada sigue disponible e interpretable con la versión de regla y la calibración vigentes a la fecha de la lectura | Evidencia de la serie; calidad |
| Eliminación de ubicación vencida | Punto con más de doce meses y su respaldo | Verificación de la eliminación y de la imposibilidad de reconstruir la posición | Cero punto, cero derivado y cero copia legible del punto vencido; la auditoría conservada no permite reconstruirlo | Registro de la eliminación y su verificación; seguridad |
| Carga masiva operativa parcial | Rol CLIENTE y lote con registros válidos, inválidos, dependencias y duplicados | Carga, consulta de informe y reenvío de rechazados corregidos | Aceptados+rechazados=100 % del lote; cero rechazos sin causa/clave; cero agregados parcialmente inconsistentes; cero efectos duplicados al reenviar | Informe por registro, conteos y auditoría; responsable del módulo y CLIENTE |

**Tabla A.23 - Pruebas de aceptación de trazabilidad, calidad, operación y seguridad**

*Fuente: elaboración propia de LafroX a partir de RT-05.08, RT-05.14 y RT-05.29 de las Bases Técnicas Transversales (PUCV, 2026d), de los recorridos de 5.1.7 y de la matriz de retención del Anexo 5-D.*

S4, Anexo 4-M, define ensayos complementarios. AL-DTE-01 comprueba 96 salidas con guía vigente, reintentos y cambios de carga en ambas rutas ERP; sin comunicación, conserva carga amparada y difiere ajustes. AL-CLI-01 reinicia el portal Android/iOS sin red, recupera catálogo/pedido y reenvía UUID: cero pérdida/duplicación, reserva tras validación M3; sesión vencida/cuenta bloqueada se rechazan. Rechazo esperado conserva causa/auditoría/mensaje; no es fallo de integridad.

AL-DR-01 se ensaya semestralmente: corte individual/por pares de fibra, LTE y Starlink, retraso externo y pérdida de sitio con un camino activo. Se mide RPO=t_incidente−t_último_punto_consistente recuperable mediante UUID/secuencia, y RTO≤4 h; transacciones de nube/WMS Talca, mensajes críticos, documentos/evidencias y temperatura ≤15 min; analítica/mensajes no críticos ≤24 h y GPS ≤24 h solo en sa-east-1. Talca detiene DMS, habilita su copia Aurora para escritura y levanta wms_only en Fargate de la región activa; Concepción reconstruye su operación desde eventos, sin carga de Talca. Cambio regional crea colas vacías y reenvía outbox sin duplicados; retorno conserva un escritor. S3 RTC verifica 99,99 % en 15 min y pendientes/recopia; DynamoDB verifica alarma ReplicationLatency a 60 s. Autonomía 24 h sin los tres caminos se prueba aparte: buffer local no protege ante su caída simultánea seguida de destrucción del sitio, límite residual de S4 §4.3.2. Restauración por clase de A.23 no sustituye RTO crítico. Se registran estados sanitarios/evidencias, tiempos, pérdidas y duplicados. Versiones/incidentes/crecimiento repiten protocolos y revisión trimestral de capacidad; son ensayos por ejecutar.


<a id="anexo-5k"></a>

## Anexo 5-K. Respuesta al Informe 1 - Subdocumento 5

La Tabla A.24 indica respuesta documental y verificación pendiente. La coincidencia de campos no certifica reglas ni pruebas ejecutadas; firma, folio, paginación y legibilidad requieren el PDF final.

| Observación | Respuesta documental | Evidencia | Estado |
| --- | --- | --- | --- |
| Modelo, relaciones y diccionario insuficientes | Conceptual y vistas críticas en cuerpo; modelos del cuerpo y complementos 5-M y diccionario exacto | 5.1, 5-A, 5-B, 5-C | Diseño y diccionario documentados; prueba en PREPROD |
| CAP, motor y autoridad no justificados | Autoridad por perímetro; DMS solo Talca lector; eventos centrales deduplicados | 5.2.1–3 y 5-B | Diseño documentado; ensayo offline pendiente |
| Migración sin volumen, herramientas, responsables ni ventana | Fuente 16,05478 GB base, destino estimado 32,10956; mapeo, cálculo por fase, dos ensayos, marcha blanca y corte | 5.3, 5-L, 5-J | Propuesta documentada; perfilado/actas y tiempos reales futuros |
| Desempeño y autonomía inconsistentes | Índices reales, globales sin partición, timestamp compuesto, vigencias 24/8–14/26 h | 5.4, 5-F, 5-G | Cotejo documental; DDL/planes y pruebas PREPROD pendientes |
| Modelo analítico e indicadores ausentes | Granos y claves; original inmutable, base completa, latencias y audiencia | 5.1.11, 5.2.6, 5-H | Diseño documentado; cálculo sobre datos reales futuro |
| Documento/guía/POD confundidos | ERP único emisor previo al traslado; POD y acuses diferenciados | 5.1.8, 5-J | Diseño documentado; validaciones externas S4 abiertas |
| Formato, referencias y metadatos | Reducción de cuadros narrativos y figuras redundantes; índices reconstruidos | Fuente S5/A5 y Referencias | Control de fuente; presentación final bajo procedimiento de entrega |

**Tabla A.24 — Respuesta documental y límites de verificación**

*Fuente: Informe 1, revisión del ítem 5; evidencia de la fuente de este ítem.*

Las pruebas descritas se ejecutarán durante el proyecto. Este estado no atribuye aprobación humana ni conformidad de producción.

<a id="anexo-5l"></a>

## Anexo 5-L. Mapeo, cálculo de olas y ventana de corte

Este anexo define el contrato de migración de 5.3. Los nombres físicos del legado se comprobarán durante el perfilado y se versionarán en el contrato de extracción. No se presentan nombres hipotéticos como esquema constatado.

La Tabla A.25 relaciona conjuntos y campos críticos con las entidades reales de destino y el responsable que valida la conversión.

| Origen semántico / alcance | Destino y clave | Transformación versionada | Rechazo / conciliación | Responsable |
| --- | --- | --- | --- | --- |
| ERP: clientes/proveedores/productos/unidades/sitios completos; RUT, código, GTIN | mae_cliente, mae_proveedor, mae_producto, mae_unidad, mae_sitio; UUID interno y equivalencia de código | Normalizar códigos/RUT/GTIN sin cambiar identidad; equivalencias aprobadas | Duplicado ambiguo o código ausente a staging; recuento y claves completas | Leandro Chamorro + maestros CLIENTE |
| ERP: ventas/pedidos tres años; pedido/línea, fecha, cantidad, precio, moneda, cliente | prv_pedido/pedido_linea, tarifa y promesa si existe compromiso comprobado; clave origen+pedido+línea | UTC según zona de origen, unidades homologadas, decimal exacto; no fabricar promesa histórica | Claves/importe por mes y moneda; promesa no disponible declarada y consultable | Datos + Comercial/Finanzas CLIENTE |
| WMS/ERP: recepción y trace hasta cinco años disponibles; producto/lote/GTIN, cantidad, unidad, fecha, documento | inv_recepcion/linea, inv_lote, cal_evento_custodia/objeto solo con hecho comprobado | Preservar ordinal externo cuando existe y equivalencias aprobadas; conservar originales | Lote/fecha/actor ausentes no se inventan; cobertura, claves y cantidades conciliadas | Datos + Calidad/bodega CLIENTE |
| WMS/conteos: inventario dos años; sitio/ubicación/producto/lote/unidad/saldo | inv_saldo, inv_movimiento y conteo según hecho de origen; clave de saldo completa | Conversión de unidad versionada y saldo original; ajuste solo con aprobación | Ubicación desconocida aislada; totales por grano, conteo físico y desviación CLP ≤0,3 % | Datos + bodega/Finanzas CLIENTE |
| ERP: toda cartera viva + dos años; cliente/documento/vencimiento/saldo y pagos | cob_saldo y cob_cobro según evidencia; clave externa de documento/pago | Preservar deuda anterior, moneda y relación fiscal; no convertir timeout en pago | Saldos por cliente/documento, identidad y sumas; deuda ausente impide corte | Datos + Finanzas CLIENTE |
| ERP/archivos: copias fiscales/POD y conjuntos no migrados | doc_documento, doc_pod, obj_objeto o archivo de consulta; tipo/emisor/folio/versión, hash | Original inmutable, sin reemisión; referencias y permisos según clase | Hash/conteo/consulta de originales y retención comprobables | Datos + Finanzas/Calidad CLIENTE |

**Tabla A.25 — Mapeo semántico y validación de migración**

*Fuente: RT-05.11–15, alcance S3/S4 y esquema lógico de S5.*

Cada campo transformado conserva valor de origen, regla/versión, clave y decisión. Un campo sin correspondencia no se omite silenciosamente: responsable decide migrar, corregir o conservar consulta con explicación aprobada.

La Tabla A.26 calcula fases de carga inicial. Para volumen V en GB de fuente decimal y base ventas 10,476, cada fase es max(mínimo, techo(tiempo ventas × V/10,476)); mínimos 10/10/10/10/10/10/20 min. Son reservas de planificación, no tiempos medidos. Extracción usa bytes de fuente; transferencia bytes serializados reales, aquí provisionalmente iguales. Transformación/carga/índices usan la base medida en ensayo, no el factor 2 como tasa de red.

| Ola / fuente GB | Extracción / transferencia min | Transformación / carga / índices min | Delta / conciliación min | Total min |
| --- | --- | --- | --- | ---: |
| 1 Maestros / 0.03418 | 10 / 10 | 10 / 10 / 10 | 10 / 20 | 80 |
| 2 Ventas / 10.47600 | 45 / 30 | 40 / 60 / 35 | 30 / 45 | 285 |
| 3 Recepciones / 1.38000 | 10 / 10 | 10 / 10 / 10 | 10 / 20 | 80 |
| 4 Inventario / 3.34860 | 15 / 10 | 13 / 20 / 12 | 10 / 20 | 100 |
| 5 Cartera base / 0.81600 | 10 / 10 | 10 / 10 / 10 | 10 / 20 | 80 |

**Tabla A.26 — Duración calculada por fase y ola inicial**

*Fuente: volúmenes de S4 y fórmula de planificación de LafroX; sin medición ejecutada.*

La suma secuencial se distribuye en noches previas. La mayor ola, 285 min, cabe en 22:00–02:45; reserva de preparación 30 min y rollback 60 min da 375 min, 22:00–04:15. No equivale a detener la operación esas noches: origen sigue siendo escritor y el destino está en staging. Cartera viva adicional y trace perfilada obligan a recalcular cada fase y ampliar noches de carga inicial antes de aceptación.

La Tabla A.27 fija la ventana relativa final propuesta; los dos ensayos deben demostrar que el delta real cabe. No se transfiere el escritor si el tiempo medido más rollback supera la ventana disponible.

| Hito | Horario relativo propuesto | Control | Responsable |
| --- | --- | --- | --- |
| Punto de control y frontera | 22:00–22:15 | Snapshot/marcas de agua; suspender nuevas escrituras en perímetro | Datos + responsable operativo CLIENTE |
| Delta final | 22:15–22:45 | Drenar, aplicar y deduplicar bajo autoridad vigente | Leandro Chamorro |
| Conciliación completa | 22:45–23:30 | Claves, cantidades/importes, cobertura, cero diferencias no explicadas | Bodega/Calidad/Finanzas CLIENTE |
| Validación y go/no-go | 23:30–00:00 | Prueba operativa y aprobación segregada; no-go al exceder | Responsable CLIENTE + datos |
| Cambio y observación, si go | 00:00–00:30 | Un escritor, ERP emisor único | Operación + datos |
| Reserva rollback | 00:30–01:30 | Restaurar punto de control, conciliar delta, devolver autoridad previa del sitio | Datos + operación CLIENTE |

**Tabla A.27 — Ventana final, decisión y reserva de rollback**

*Fuente: ventanas y congelamientos de las Bases/S3/S4; propuesta relativa, sin fecha de inicio contractual inventada.*

Se preserva despacho 05:30–07:00 y congelamientos septiembre/diciembre/cierre mensual. Si no-go ocurre antes, rollback comienza inmediatamente y usa la reserva; se registran tiempos, resultado y frontera recuperada. E1 M16 y E2 M21 requieren marcha blanca previa y últimas cuatro semanas con volumen real. RTO/RPO de S4 continúan siendo condiciones contractuales; esta reserva es hipótesis a demostrar, no resultado de recuperación.


<a id="anexo-5m"></a>

## Anexo 5-M. Modelos lógicos complementarios

Los modelos específicos complementan el MR general de 5.1. El diccionario 5-A conserva todos los atributos, tipos y restricciones.

El esquema lógico se distribuye sin duplicaciones: inventario, pedido/preparación, reparto, custodia, cobranza/documentos y analítica se dibujan en las Figuras 5.2–5.7 del cuerpo. Aquí se desarrollan maestros, EDI/gobierno y telemetría. El diccionario 5-A define tipos, dominio, obligatoriedad, propietario y sensibilidad de todos los atributos.

La Figura A5.1 desarrolla maestros e identidades compartidas; se relaciona con 5.1.3 del cuerpo y se valida con 5-A/5-C.

**Insertar figura A5.1 — Maestros e identidades compartidas.**

*Fuente: modelo de LafroX a partir de S3/S4 y RT-05.01.*

Las equivalencias traducen claves externas a UUID canónicos y no crean identidades paralelas. La vigencia conserva historia y la copia local mantiene versión/fecha de consulta.

La Figura A5.2 desarrolla edi, notificaciones y gobierno; se relaciona con 5.1.9 del cuerpo y se valida con 5-A/5-C.

**Insertar figura A5.2 — EDI, notificaciones y gobierno.**

*Fuente: modelo de LafroX a partir de S3/S4 y RT-05.01.*

Mensaje y aviso conservan identidad/resultado; auditoría y excepción preservan actor, contexto y versión. El acuse de integración no sustituye aceptación fiscal ni recepción física.

La Figura A5.3 desarrolla telemetría, copias de consulta y objetos; se relaciona con 5.1.10 del cuerpo y se valida con 5-A/5-C.

**Insertar figura A5.3 — Telemetría, copias de consulta y objetos.**

*Fuente: modelo de LafroX a partir de S3/S4 y RT-05.01.*

Raw, detalle, agregado, GPS y evidencia tienen plazos y permisos distintos. Las proyecciones se reconstruyen desde su autoridad; la evidencia durable pendiente no se trata como caché descartable.

## Referencias

Estas fuentes sostienen las reglas y decisiones citadas en este ítem. Las fuentes locales son documentos de la licitación o de la propuesta; EPCIS/CBV y PostgreSQL respaldan exclusivamente sus contratos técnicos.

- Pontificia Universidad Católica de Valparaíso. (2026a). *Aclaraciones de licitación*. [Documento](../Bases/aclaraciones-licitacion.md).
- Pontificia Universidad Católica de Valparaíso. (2026b). *Bases Administrativas TFEP-01/2026*. [Documento](../Bases/Bases_Administrativas.md).
- Pontificia Universidad Católica de Valparaíso. (2026c). *Bases Técnicas del Caso 02 — Logística*. [Documento](../Bases/Caso_02_Logistica.md).
- Pontificia Universidad Católica de Valparaíso. (2026d). *Bases Técnicas Transversales*, versión 1.0. [Documento](../Bases/Bases_Tecnicas_Transversales.md).
- LafroX SpA. (2026d). *Presentación de la empresa*, Subdocumento 1. [Documento](../01_presentacion_empresa/LAFROX-Subdocumento1.md).
- LafroX SpA. (2026c). *Problema y necesidad*, Subdocumento 2. [Documento](../02_problema_necesidad/LAFROX-Subdocumento2.md).
- LafroX SpA. (2026b). *Esquema de solución y alcance*, Subdocumento 3 y anexos. [Documento](../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md).
- LafroX SpA. (2026a). *Arquitectura*, Subdocumento 4, anexos y formularios T-11/T-12. [Documento](../04_arquitectura/LAFROX-Subdocumento4.md).
- International Organization for Standardization. (2008). *ISO/IEC 25012:2008, Software engineering — SQuaRE — Data quality model*. Dimensiones de calidad citadas en 5.2.5; no es fuente de umbrales numéricos.
- GS1. (2022a). *EPCIS Standard*, release 2.0, junio de 2022. [Estándar](https://ref.gs1.org/standards/epcis/2.0.1/).
- GS1. (2022b). *Core Business Vocabulary Standard*, release 2.0. [Estándar](https://ref.gs1.org/standards/cbv/2.0.0/).
- PostgreSQL Global Development Group. (2023). *PostgreSQL 16 Documentation: Constraints; Table Partitioning*. [Restricciones](https://www.postgresql.org/docs/16/ddl-constraints.html), [particionado](https://www.postgresql.org/docs/16/ddl-partitioning.html). Aplicación: 5-F.

<a id="sec-ia"></a>

## Declaración de uso de IA

<a id="tab-a27-declaracion-ia"></a>

**Texto de caída:** La declaración responde al requisito §7.2 de Bases/aclaraciones-licitacion.md. Se indica herramienta utilizada, finalidad, nivel de asistencia y verificación humana realizada. No se completan datos de revisión humana ni aprobación del CLIENTE.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
|---|---|---|---|---|---|
| S5 - Capítulo completo | Modelo de asistencia interna | Revisión estructural, coherencia con guía y verificación de contradicciones | Medio | Bajo | Ninguno (revisión técnica automatizada interna). No se atribuye revisor humano. |
| A5 - 5-A (Diccionario) | Modelo de asistencia interna | Conciliación modelo-diccionario, corrección de tipos/dominios/referencias | Medio | Ninguno | Ninguno (verificación por conteo 111/792). No se atribuye revisor humano. |
| A5 - 5-B a 5-F | Modelo de asistencia interna | Matrices, índices, retención, sensibilidad, particionado | Medio | Ninguno | Ninguno. No se atribuye revisor humano. |
| A5 - 5-G a 5-J | Modelo de asistencia interna | Cachés, fórmulas/indicadores, RT-05, pruebas | Medio | Ninguno | Ninguno. No se atribuye revisor humano. |
| A5 - 5-K (Respuesta Informe 1) | Modelo de asistencia interna | Registro de respuestas con evidencia | Medio | Ninguno | Ninguno. No se atribuye revisor humano. |

