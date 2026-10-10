# Por qué las 73 filas parciales del T-12 no están en Cumple — 10 de octubre de 2026

Fuente: el «Falta» de cada fila del T-12, contrastado con los nueve informes de la introspección (`introspeccion_T12.md`). Esos informes leyeron todas las filas parciales y confirmaron que el «Falta» sigue vigente, salvo en las filas marcadas con ✱.

| Grupo | Causa | Filas | ¿Se cierra sin decisión del equipo? |
| --- | --- | --- | --- |
| 1 | Al modelo de datos (SD5) le faltan atributos | 13 | Sí: se agregan columnas en SD5-Anexos |
| 2 | Falta una frase técnica simple | 14 | Sí: una frase en el subdocumento dueño |
| 3 | El requisito pide un costo y la oferta técnica no admite precios (BA Art. 50.2) | 8 | Sí: se remite a la Oferta Económica |
| 4 | El diseño se aparta del requisito por decisión propia | 14 | No: hay que cambiar el diseño o aceptar el parcial |
| 5 | Faltan datos externos (fichas de fabricante, carbono, batería) | 8 | Con investigación: datos reales con fuente |
| 6 | Hay una decisión del equipo pendiente | 12 | No |
| 7 | Depende de un entregable fuera de los subdocumentos | 4 | No por ahora |

## Grupo 1 — Faltan atributos en el modelo de datos (SD5-Anexos 5-A)

La funcionalidad está descrita en SD4, pero las tablas de SD5 no tienen los campos que la sostienen. Se cierra agregando columnas, con mínimo arrastre: solo el diccionario de datos y, si corresponde, una línea en SD5 5.1.x.

| ID | Qué agregar |
| --- | --- |
| RF-01.08 | `mae_ubicacion`: pasillo, columna y nivel |
| RF-01.11 | `mae_ubicacion`: zona y rango térmico |
| RF-02.01 | `mae_ubicacion`: zona, rack y posición. Además, una frase sobre la copia offline de la configuración |
| RF-02.07 | `mae_ubicacion`: capacidad configurada (para el % de ocupación) |
| RF-02.03 | `mae_producto`: volumen. `mae_ubicacion`: proximidad al andén. Además, una frase en SD4 4.1.4.3: el jefe de bodega aprueba antes de instruir movimientos |
| RF-01.10 | `mae_producto`: formato, SKU interno, peso, dimensiones, indicadores de trazabilidad y de vencimiento, clasificación sanitaria y RUT del proveedor |
| RF-04.01, RF-04.03, RF-11.05 | `mae_vehiculo`: capacidad nominal de peso y de volumen. `mae_producto`: peso y dimensiones (lo mismo que en RF-01.10) |
| RF-02.08 | `prp_mision_linea`: secuencia de recorrido. `prp_picking_confirmacion`: causal estructurada del faltante |
| RF-07.04, RF-07.06 | Vencimiento por documento y tramos de antigüedad (corriente, 30, 60 y 90+ días) en la cobranza |
| RF-08.07 | `hech_actividad_costo`: importe de merma por entrega y por cliente |

## Grupo 2 — Falta una frase técnica simple

| ID | Frase en | Contenido |
| --- | --- | --- |
| RT-25.01 ✱ | — | Ya está en SD4:265 (máximo de tres interacciones). **Solo hay que citarlo y pasar la fila a Cumple** |
| RNF-23.04 ✱ | — | T-11:56 ya acredita gestión central, Falcon y cifrado en las 8 estaciones. **Pasa a Cumple** |
| RF-18.03, RT-16.23 | SD4-Anexos 4-H INT-11 / SD5 | Se registra la apertura del mensaje cuando el canal la informa (estado `ABIERTO` en `not_intento`) |
| RNF-12.03 | SD4 4.1.17.1 | Acuse comercial dentro de 30 min desde la descarga, vinculado a la misma guía |
| RNF-14.01, RT-11.08 | SD4 4.1.3.7 | Suites TLS modernas, HSTS con precarga, alerta de vencimiento con 30 días de anticipación, TLS 1.3 en todo el tráfico exigido |
| RT-06.04 | SD4 4.3.1.4 | Normas de cableado y canalización: ANSI/TIA-568, TIA-569, TIA-606 y TIA-942 |
| RT-06.29 | SD4 4.3.1.4 | Telefonía e Internet en la zona de trabajo de Talca |
| RT-08.14 | SD4 / T-11 | MDM o gestión centralizada para impresoras, PAX, balanzas y termógrafos (hoy solo Zebra DNA) |
| RT-16.14 | SD4 4.1.3.4 | Reglas parametrizadas que se evalúan sin recompilar, con la regla y su versión registradas en cada transacción |
| RT-15.02 | SD1 1.4 | Conocimiento acreditado de RSA y DTE con los proyectos del T-6 |
| RT-15.07 | SD1 1.4 | Copias vigentes y códigos de verificación de los certificados en el Sobre N° 1 |
| RT-25.03 | SD4 4.1.3.1 | Textos alternativos y etiquetas de accesibilidad (el resto ya está en SD4:269-285) |

## Grupo 3 — El requisito pide un costo y la oferta técnica no lo admite (BA Art. 50.2)

En todas estas filas la parte técnica está cubierta. El «Falta» es un monto, y la oferta técnica no puede llevar montos. Se cierran con una frase que remita el costo a la Oferta Económica (Formulario E-21), igual que SD4:1995.

| ID | Parte técnica que falta además del costo |
| --- | --- |
| RT-03.08 (Savings Plans) | Ninguna |
| RT-04.13 (ahorro ≥60 % de horas, S-43) | Ninguna; el ahorro ya está cuantificado en horas |
| RT-02.10, RNF-19.02 | El umbral numérico de edad y profundidad de cola para escalar la integración (2 a 4 tareas ya declaradas) |
| RT-14.08 | El plazo de retención de las trazas (los registros y las métricas ya lo tienen) |
| RNF-23.01, RT-08.10 | Ninguna |
| RT-16.24 | El proveedor por canal (correo, SMS, WhatsApp); hoy no se nombra ninguno |

## Grupo 4 — El diseño se aparta del requisito por decisión propia

Aquí la propuesta dice explícitamente que hace otra cosa. Para llegar a Cumple hay que cambiar el diseño. Si no, el parcial es honesto.

| ID | Qué hace la propuesta | Qué exige el requisito |
| --- | --- | --- |
| RF-16.02, RT-14.02 | Operación ≤5 min, cierre comercial en 2 h, gestión en 4 h | Tiempo real |
| RF-18.01, RT-16.17 | «La solución no emite firma avanzada»; el ERP firma la guía (SD4:1385) | Firma avanzada cuando corresponda y verificar el certificado. **Se puede cerrar** declarando que ningún acto del caso exige firma avanzada y que el certificado se verifica al firmar |
| RNF-20.06, RT-07.04 | El RPO puede superar 15 min si fallan los tres enlaces y se pierde el sitio | RPO ≤15 min sin salvedad |
| RT-07.08 | La conmutación a DR la autoriza el CLIENTE (SD4:3251) | Disparo automático con salvaguardas |
| RNF-14.05, RT-11.16 | El servidor ERP del CLIENTE queda fuera del EDR | EDR 24×7 en todos los servidores |
| RT-05.10 | Linaje documental; el catálogo automatizado «no se oferta» | Catálogo con linaje automatizado |
| RF-07.03 | La cobranza a crédito la gestiona el CLIENTE (SD3-Anexos:230) | Consola de cartera |
| RF-09.05 | El termógrafo registra offline y descarga al volver (T-11 B-03) | Alerta de temperatura en tiempo real en la plataforma |
| RF-03.12 | No hay precio por línea desde el ERP | Comparar el precio facturado por línea |
| RT-11.04 | Pendiente de aclaración del CLIENTE sobre el congelamiento | Remediación en plazo |

## Grupo 5 — Faltan datos externos reales

No se pueden inventar. Hay que sacarlos de las fichas del fabricante o de fuentes publicadas.

- **RT-08.12 y RNF-23.02:** grado IP y resistencia a caídas de MC9400, ZT411, PAX A920 Pro, Dibal BEV y Onset CX450 (fichas del fabricante).
- **RT-08.11:** humedad, polvo, vibración, luminosidad y autonomía por dispositivo (fichas).
- **RT-08.01:** marca, modelo y ficha de las 8 estaciones, y CPU del mini-PC.
- **RT-08.04:** fuente redundante en impresoras, balanzas y estaciones (ficha o decisión de compra).
- **RT-17.07:** consumo de batería por turno (estimación a partir de la ficha).
- **RT-15.03 y RT-15.04:** huella de carbono anual e intensidad de carbono de sa-east-1 (fuente publicada por AWS).

## Grupo 6 — Decisiones del equipo pendientes

- **Ciudad del NOC:** RNF-21.01, RT-21.01.
- **Ciudad del SOC:** RT-11.17. Además hay que alinear SD6 y T-9, que lo dejan condicionado a subcontratación.
- **Bolsa de 768 HH:** RNF-21.08, RT-21.19 (tamaño, perfiles y procedimiento).
- **Dominio del sistema:** RF-14.03-BTT, RF-19.03, RT-11.13 (FQDN de cada entrada de la Tabla 19).
- **Equipo de operación nominado por tecnología:** RT-21.03 (o SD12).
- **Personas certificadas y su dedicación:** RT-15.08.
- **Umbrales de usabilidad por perfil:** RT-13.04. Ya existe la tasa de error ≤5 % (T-13:73) para preparación.
- **Doble acometida eléctrica en Talca:** RT-06.12.

## Grupo 7 — Fuera de los subdocumentos

- **RT-23.02:** testimonios autorizados por clientes.
- **RT-23.03:** CV y certificaciones personales en la web (dependen de SD12).
- **RT-23.09:** métricas en vivo de los servicios operados para clientes; hoy solo se mide el sitio.
- **RT-25.08:** interactividad simulada del prototipo (Informe 3).

## Resultado posible

Si se aplican los grupos 1, 2 y 3, más el cierre de RF-18.01/RT-16.17 del grupo 4, pasan a Cumple **unas 37 filas** de 73: 13 + 14 + 8 + 2. Quedarían 36 parciales, y todas tendrían una causa legítima: diseño propio, datos externos, decisiones del equipo o entregables externos.
