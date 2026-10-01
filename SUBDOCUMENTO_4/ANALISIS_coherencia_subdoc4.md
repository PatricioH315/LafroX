# Análisis de coherencia del Subdocumento 4 completo (sin ADR)

**Fecha:** 1 de octubre de 2026 · **Revisión doble:** Claude (lectura completa del 4.1 y cruce de cifras) y GPT (cuatro frentes en paralelo: 4.1 interno, 4.2 interno, cruce 4.1↔4.2 y citas a las Bases). Cada hallazgo de GPT que aparece aquí fue verificado contra la fuente; los que no resistieron están en la sección 7.

**Fuentes revisadas**

- **4.1 Arquitectura lógica** (rama `alvaro-md`, commit `fc09a3b`, conversión fiel de `arquitectura-alvaro` `e55133c`): `04_arquitectura/logica 4.1/LAFROX-Subdocumento4.1.md` y `LAFROX-Subdocumento4.1-Anexos.md`.
- **4.2, 4.3, Formulario T-11 y Anexo 4.B** (LaTeX vigente de `Alex_LASECUELA`): `SUBDOCUMENTO_4/Subdocumento_4_MD/Subdocumento_4_completo.md`.
- Reglas: `aclaraciones-licitacion.md`, `Revision_informe.md` y Bases.

**Fuera de alcance:** registros de ADR (4.4, 4.1.11 y Anexo 4.1-O), salvo una nota estructural en la sección 6.

**Leyenda de severidad**

- **Crítica:** indicador de IA según las aclaraciones (deja el subdocumento completo en 0) o contradicción visible en una decisión de diseño entre capítulos.
- **Alta:** dato o cifra que un evaluador detecta.
- **Media / Baja:** forma, trazabilidad o redacción.

**Origen:** C = Claude · G = GPT · C+G = ambos.

---

## 1. Resumen

| Severidad | Cantidad |
|---|---|
| Crítica | 18 |
| Alta | 8 |
| Media | 8 |
| Baja | 5 |

Lo más urgente son dos cosas:

1. **El 4.1 de Álvaro contiene indicadores de IA explícitos** (bloque A). Según la regla 7.1 de las aclaraciones, cualquiera de ellos deja **todo** el Subdocumento 4 en 0, incluido lo que está bien en 4.2.
2. **4.1 y 4.2 calculan distinto lo mismo**: gateways IoT, puntos de temperatura, terminales de bodega y el volumen de las 15 integraciones (bloque B).

---

## 2. Bloque A — Indicadores de IA y notas de trabajo (todo en el 4.1)

| ID | Sev. | Dónde | Texto exacto | Por qué es indicador | Origen |
|---|---|---|---|---|---|
| A1 | Crítica | 4.1, Declaración de uso de IA, Tabla 4.6, y Anexos, Tablas A.26 y A.27 | «Revisión final no realizada; se efectuará sobre el consolidado» · «La ausencia actual de esa revisión impide tratar este archivo de trabajo como una entrega final conforme» · 22 filas «No realizada.» | Admite un pendiente, se llama a sí mismo «archivo de trabajo» y declara que no hubo revisión humana. | C+G |
| A2 | Crítica | 4.1, Anexos, Tabla A.27 | «especificaciones tecnologias de software a utilizar», «diseno», «integracion», «conexion» | Títulos sin tildes: son nombres de archivo convertidos en texto. | C |
| A3 | Crítica | 4.1, fuente de las Figuras 4.1, 4.3, 4.4, 4.5, 4.7, 4.8, 4.11, 4.12 y 4.13; y Declaración IA | «Fuente: diagrama general aportado por Tomás Pérez; LafroX.» · «las láminas de Tomás» | Nombra a un integrante del equipo. Rompe la ficción de la licitación (estudiantes). | C |
| A4 | Crítica | 4.1, Referencias (cuerpo y anexos) | «Pontificia Universidad Católica de Valparaíso. (2026c). *Aclaraciones de licitación: índice obligatorio y consistencia de los subdocumentos*.» | Cita el documento de instrucciones del curso. | C |
| A5 | Crítica | 4.1, §4.1.4 | «La correspondencia con los identificadores físicos se detalla en el Anexo 4.A (Formulario T-11) de 4.2» | No existe ningún «Anexo 4.A». En 4.2 el T-11 es un formulario aparte y el único anexo es el 4.B. Es una referencia a un anexo inexistente, regla 7.1 (d). | C+G |
| A6 | Crítica | 4.1, Anexo 4.1-N | «El texto de trabajo disponible del capítulo 3 conserva otra numeración: 3.2.1 contiene alcance funcional…» · «No se declara 100% hasta integrar las versiones aprobadas de los tres apartados.» · «La tabla cubre 12 de 12 módulos, no el 100% de los componentes del capítulo integrado.» | Nota de proceso que además admite que el mapeo 4.1↔4.2 no llega al 100 % que exigen las aclaraciones. | C+G |
| A7 | Crítica | 4.1, Anexo 4.1-M (AL-DTE-01 y AL-BR-01) y Anexo 4.1-V | «Si la única respuesta posible es retener camiones, el ensayo preserva el control tributario, pero falla el criterio de continuidad» · «Con aislamiento total prolongado y sin extracción externa, el diseño descrito no puede demostrar ese RPO» · «La brecha AL-BR-01 queda identificada para decisión de Arquitectura, Infraestructura y CLIENTE: diseñar y presupuestar…» · «el requisito de continuidad no se considera satisfecho» | La propuesta se declara a sí misma en incumplimiento y deja decisiones abiertas. | C+G |
| A8 | Crítica | 4.1, Anexo 4.1-V, Tabla A.25 | «AL-REV-01 · Revisión humana y A-6 · …acta y declaración consolidadas» | Una tarea de revisión interna aparece como condición de aceptación. | C |
| A9 | Crítica | 4.1, unas 20 frases dirigidas a 4.2. Ejemplos: §4.1.3.3 «El recorrido físico y el bloqueo efectivo del acceso directo al origen se deben comprobar en 4.2»; §4.1.3.7 «Su número, sentido de inicio de conexión y reglas de red deben quedar inequívocos en 4.2»; «El inventario de dominios, puertos y rutas de 4.2 debe representar las tres superficies por separado»; Anexo V «la arquitectura física debe realizar la protección que se seleccione» | Se leen como instrucciones al redactor del otro capítulo, no como afirmaciones de la oferta. | C |
| A10 | Crítica | 4.1, §4.1.17.2 | «No se atribuye aprobación a ese procedimiento mientras no exista el acta.» | Pendiente admitido. | C |

**Qué hacer:** reescribir la Declaración de uso de IA con la revisión humana real (quién revisó y qué verificó). Quitar los nombres de personas. Dejar fuera de la oferta las referencias al curso. Convertir AL-MAP, AL-BR, AL-DTE y AL-REV en afirmaciones de diseño con su prueba de aceptación, sin «brecha», «pendiente» ni «no satisfecho». Reescribir las frases «debe… en 4.2» como afirmaciones con referencia a la sección real de 4.2.

---

## 3. Bloque B — Contradicciones entre 4.1 y 4.2/4.3/T-11/4.B

| ID | Sev. | Tema | 4.1 dice | 4.2 / T-11 / 4.B dice | Qué debería prevalecer | Origen |
|---|---|---|---|---|---|---|
| B1 | Crítica | Gateways IoT | §4.1.3.2, §4.1.4.2 y §4.1.7 (tres veces): «Corre solo en dos gateways IoT industriales…, uno en el CD Talca y otro en el CD Concepción» | Tabla 1 de 4.2.1: Talca 2, Concepción 1. T-11 (B-02): «3 + 1 de reserva = 4». T-11 (N-08): «3 gateways». | El inventario físico (3 + 1). Corregir el 4.1. | C+G |
| B2 | Crítica | Puntos de temperatura en cámaras | §4.1.4.2: «28 puntos de cámara y 28 termógrafos». Anexo H (INT-05): «(28+28)×288 = 16.128 muestras/día». | Tabla 1 de 4.2.1: 15 + 6 = **21** puntos. 4.B: 21 × 288 + 28 × 162 = **10.584** lecturas/día. | 21 (inventario cotizado). El caso no fija la cantidad de puntos de cámara. Corregir el 4.1 y el Anexo I. | C+G |
| B3 | Crítica | Volumen de mensajes por integración (dimensión 11 del 14.2) | Anexos G, H e I: base de 25 días/mes y peak ×2. Pedidos 1.240/día. | Tablas 20 y 33: base de 22,14 «días equivalentes» y peak ×1,857. Pedidos 1.400/día. 4.2 afirma contar «INT-01 a INT-15 del catálogo del apartado 4.1». | Una sola base de cálculo. La de 4.B (SV-01, 22,14 días) está justificada; recalcular el Anexo 4.1-I con ella. | C+G |
| B4 | Crítica | Terminales de bodega | §4.1.3.3 «Los 120 terminales…»; §4.1.9 «se prueban los 120 terminales»; Anexo T «120 preparadores concurrentes» | 4.2.1: 120 en Talca + 60 en Concepción + 2 por cross-docking = **186** (205 con reserva). | 186. En el 4.1, 120 es solo Talca. | C+G |
| B5 | Crítica | RPO durante un corte | §4.1.16 y Anexo M: «el RPO de 15 minutos sigue siendo un requisito exigible»; «la arquitectura física debe realizar la protección que se seleccione» | 4.2.4.4 y 4.3.2: «el RPO remoto de 15 minutos rige solo con enlace y no se promete durante un corte que lo impide» | Hay que alinear: o 4.2 diseña la protección externa, o ambos declaran lo mismo con el mismo fundamento. Hoy 4.2 relaja lo que 4.1 dice que no se puede relajar. | C+G |
| B6 | Crítica | Mapeo al 100 % | Anexo N: 49 unidades lógicas (12 módulos + 37 transversales) con la columna «Obligación en 4.2». | 4.2.2: 36 componentes (13 nube pura + 11 on-premise + 12 híbridos), y la Tabla 2 mapea módulos y capas, no las 49 unidades. | Una tabla puente 49 ↔ 36 en ambos sentidos. | C+G |
| B7 | Alta | Captura en cámara a −22 °C (tema evaluado en el cap. 19 del caso) | §4.1.3.1: los terminales «descargan las misiones de preparación al inicio del turno y registran su ejecución localmente, incluso en cámaras a -22 °C sin señal». Pero §4.1.4.8 dice: «El preparador confirma cada lectura en el servicio local». | 4.2.1 y 4.2.2 (C-03): Wi-Fi 6E con mayor densidad dentro de las cámaras; los MC9400 trabajan «contra el WMS del sitio por la red inalámbrica». El caso (RT-03.24) exige un estudio de cobertura del interior de las cámaras. | El mecanismo de 4.2 (Wi-Fi en cámara + WMS local, con la memoria del terminal como respaldo). Corregir §4.1.3.1. | C |
| B8 | Alta | Servicios de nube nombrados | §4.1.7 «Los servicios AWS consumidos incluyen…»: omite DMS (que el propio 4.1 usa en INT-12), Lambda (que el propio 4.1 cita como autorizador), Verified Access, NLB, Glue, QuickSight, Security Lake, Inspector, Macie, Config, Control Tower y Systems Manager. | 4.2.3 y T-11 los contratan. | Completar la lista del 4.1. | C+G |
| B9 | Alta | Herramienta de BI | El 4.1 no nombra la herramienta de los tableros de M10 (solo Redshift). | 4.2.2 (N-10), 4.2.3 y T-11: «QuickSight embebido». | Nombrar QuickSight en §4.1.4.7 y §4.1.7. | C |
| B10 | Alta | Referencias bibliográficas | Autor PUCV (2026a/2026b) y cita «(PUCV, 2026b, cap. 2, p. 6)». | Sin autor: «*Bases técnicas transversales* (versión 1.0) [Licitación N.° TFEP-01/2026]. (2026).» y cita «(Bases Técnicas Transversales, Cap. 2, p. 6)». | Un solo estilo y una sola lista de Referencias para todo el Subdocumento 4. | C+G |
| B11 | Alta | Declaración de uso de IA | El 4.1 tiene la suya (ver A1). | 4.2/4.3 no tienen ninguna (las aclaraciones la exigen al final de cada subdocumento). | Una sola declaración al final del Subdocumento 4 que cubra 4.1, 4.2, 4.3, T-11 y los anexos. | G |
| B12 | Media | Dueño del paso M11 → ERP | §4.1.3.5: «El hub… entrega al ERP, exclusivamente mediante la ACL, la información necesaria para sus documentos, incluida la guía». | Anexo H: INT-07 pertenece a ACL/M5; M11 solo a INT-08. 4.2 sigue al Anexo H. | Nombrar el contrato INT del paso M11 → ERP o eliminar la frase. | G |
| B13 | Media | Retención para deduplicación | §4.1.16: «el resultado se retiene para deduplicación durante 30 días». | 4.2.5 y T-11 solo declaran colas y buffers de 24 h, sin un almacén de 30 días. | Declarar en 4.2 dónde vive esa clave durante 30 días. | G |
| B14 | Media | Referencia a una tabla sin número | §4.1.10: «conforme a la Tabla de 4.2» | Es la Tabla 10 de 4.2.4.3 (el contenido coincide). | Citar «Tabla 10». | C |

**B3 en detalle: volumen por integración, valor normal / peak**

| INT | 4.1 (Anexos G/H/I) | 4.2 (Tabla 33) |
|---|---|---|
| INT-01 Preventa | 1.240 / 2.480 pedidos (más 4.960 / 9.920 consultas) | 1.400 / 2.600 |
| INT-02 Entrega, POD y cobro | hasta 4.200 / 7.800 (3 sobres por entrega) | 7.000 / 13.000 (5 por entrega) |
| INT-03 Eventos de bodega | 52.000 / 104.000 | 58.710 / 109.032 |
| INT-04 Cross-docking → Talca | ≤ 52.000 / 104.000 | 5.600 / 10.400 |
| INT-05 Temperatura | 16.128 (o 12.600) | 10.584 |
| INT-06 ERP | 4.686 / 9.372 | 2.025 / 3.762 |
| INT-07 DTE/SII | 2.720 / 5.440 | 3.071 / 5.703 |
| INT-08 EDI | 544 / 1.088 | 0 / 1.144 |
| INT-09 Pagos | 500 / 1.000 | 533 / 990 |
| INT-10 Mapas | 200 / 400 | 96 / 96 |
| INT-11 Avisos | 2.800 / 5.200 | 2.800 / 5.200 ✓ |
| INT-12 Réplica DMS | 0,50 / 0,99 GiB por día | 12.602 / 23.404 cambios |
| INT-13 Identidad | 120 manifiestos + 1.144 autenticaciones | 760 (380 dispositivos × 2) |
| INT-14 Observabilidad | 144.000 muestras + 5.200 trazas + 104.000 registros | 10.000 (10 nodos × 1.000) |
| INT-15 Flota | 60.480 / 70.560 | 60.480 / 60.480 |

---

## 4. Bloque C — Incoherencias internas de 4.2/4.3/T-11/4.B

| ID | Sev. | Cita A | Cita B | Problema | Origen |
|---|---|---|---|---|---|
| C1 | Crítica | 4.2.1, criterios: «Concepción: el servidor se dimensiona a su propia bodega, sin sobrecompra» | 4.3.2: «Ante una contingencia que afecte solo a la bodega de Talca, asume la carga de esa bodega mediante la promoción controlada del motor de almacenes.» 4.2.6.8 (Tabla 22): Concepción 10 vCPU, 15 GB y 140 GB. | Concepción asume Talca en el DRP local, pero no está dimensionado para hacerlo. Ya estaba en la lista de pendientes y sigue sin resolverse. | G (verificado) |
| C2 | Crítica | 4.2.2 (A-04): «corre en VM-04 junto al ERP de 2017» | El Formulario T-11 no tiene ninguna fila para A-04 ni para la capa anticorrupción, y la fila de Aplicación no incluye VM-04. | Un componente del catálogo no aparece en el formulario de implementos, aunque 4.2 dice que el T-11 detalla todo elemento por elemento. | G (verificado) |
| C3 | Alta | 4.2.6.3, Tabla 17, columna «Ventana de despacho»: WMS de Talca 1,11 TPS y total «1,68 / 3,05 TPS» | Anexo 4.B, perfil horario: a las 05:00, 1,64 / 3,02; a las 06:00, 1,11 / 2,00 y nube 0,68 / 1,26 | La ventana de 05:30 a 07:00 toma solo el valor de las 06:00, y el total no suma: 1,11 + 0,68 = 1,79 (no 1,68) y 2,00 + 1,26 = 3,26 (no 3,05). | G (verificado) |
| C4 | Alta | 4.3.1, cálculo del PUE: «las pérdidas de conversión del UPS de ≈ 0,55 kW» | 4.3.1, tabla de carga térmica: «Pérdidas de conversión del UPS (eficiencia ≈ 0,92) ≈ 610 W» | 7,0 × (1/0,92 − 1) = 0,61 kW. La suma del recinto da ≈ 10,5 kW, no 10,4. | G (verificado) |
| C5 | Media | 4.3.1: «ISO/IEC 27017 (nube) e ISO/IEC 27018»; 4.2.1 y T-11: «calibración contra patrón NIST» | Las Referencias de 4.2 solo traen las tres Bases. | Normas citadas sin referencia. | G (verificado) |
| C6 | Media | Anexo 4.B, aportes de Talca: «observabilidad = 5 × 0,25 = 1,25 GB/día» | Talca tiene 3 nodos físicos y 6 máquinas virtuales. INT-14 cuenta «10 nodos». | El «nodo» de observabilidad no está definido (Talca 5, Concepción 2, 1 por cross-docking). Hay que definirlo. GPT lo leyó como 5 colectores; eso es incorrecto (ver la sección 7). | C (corrige a G) |
| C7 | Baja | 4.2.2 (N-07): «ElastiCache mantiene en memoria el stock, el crédito y las sesiones» | 4.2.3: «ElastiCache solo actúa como caché» | Las sesiones también son caché, pero la segunda frase se lee como si solo guardara stock y crédito. | C |
| C8 | Baja | 4.2.2 (F-02): «Gestión de parches: Ansible…» | T-11: «Configuración · Ansible y Terraform con CDK» sin el código F-02 | Se pierde la traza del componente al formulario. | G |
| C9 | Baja | 4.3.1: «…sin el cálculo que los respalde.La consola KVM…» (`05_d_sitio_principal.tex`, línea 110) | — | Falta un espacio después del punto. | C |

---

## 5. Bloque D — Citas a las Bases y datos del caso

| ID | Sev. | Dónde | Problema | Origen |
|---|---|---|---|---|
| D1 | Alta | 4.1, §4.1.2: «…120 preparadores nocturnos y 310 personas de centro de distribución (PUCV, 2026a, cap. 14, pp. 24–25)» | El caso no da 120 preparadores (el 14.1 solo da 310 personas). En 4.2 es el supuesto S-39. Se cita como dato del caso algo que es un supuesto propio. | C+G |
| D2 | Media | 4.1, §4.1.21: «Los cortes frecuentes de dos horas descritos en la operación» | El caso habla de tramos de ruta sin cobertura de hasta 2 h; la fibra se corta 4 veces al año. Mezcla las dos cosas. | C |
| D3 | Media | 4.1, §4.1.15 vs. Anexo M | RT-03.13 se usa con dos sentidos: el del documento transversal (declarar qué funciones no operan sin conexión) y el del cap. 15 del caso (tiempo de sincronización). Hay que decir cuál y citar RT-03.12 para la reconciliación. | G (matizado) |
| D4 | Media | 4.2.2: «el Artículo 21 de las Bases Administrativas (p. 15) impide exponer los sitios a Internet y separa los públicos externos en la DMZ» | El Art. 21.2 exige publicar solo a través de la capa de borde. La DMZ es una decisión propia y debería apoyarse en RT-03.04. | G |
| D5 | Baja | T-11: «RT-12.11; Bases Técnicas del caso, Cap. 15, p. 27» y RT-13.08 | Citar también el RT de las Bases Técnicas Transversales, además del parámetro del caso. | G |
| D6 | Baja | 4.1, §4.1.2: «8.400 SKU (que pasan a aproximadamente 9.500)» | 9.500 es la proyección a 3 años del caso; falta decirlo. | G |

---

## 6. Nota estructural sobre los ADR (fuera de alcance, pero afecta la coherencia)

- **Dos registros de decisiones en el mismo subdocumento.** El 4.1 dice: «Las decisiones lógicas utilizan los identificadores del registro del Subdocumento 4. El Anexo O contiene sus fichas fechadas». Las fichas del Anexo 4.1-O (ADR-01, 04–08 y 11–14, **fechadas**, más ADR-L01 y L02) usan los mismos números que los 16 ADR de 4.4 (**sin fecha**). Si el texto difiere, son dos versiones del mismo ADR. Hay que dejar un solo registro.
- **Conteo cíclico.** §4.1.4.3 dice «a menos del 1%» y ADR-08 dice «2,3 %→0,3 %».

---

## 7. Descartados tras verificar

| Hallazgo | Por qué se descarta |
|---|---|
| G: «observabilidad 5 × 0,25 imputa los cinco colectores a Talca; Talca daría 0,435 GB, no 1,43» | El 5 son nodos de Talca, no colectores: cuadra con los «10 nodos» de INT-14 y con los 0,59 GB de Concepción y 0,27 GB por cross-docking. Queda solo C6 (definir qué es un nodo). |
| G: T-11 «Tabla 28» vs. «Tabla 1» | Error de la conversión a Markdown (mezcló la numeración del PDF principal con la del T-11 por separado). En el PDF no existe. |
| G: 4.2.5.1 sin número | Error de la conversión a Markdown. En el PDF sí está numerada. **Corregido**, junto con otras 34 subsecciones sin número y el símbolo ÷. |
| G: enlaces a `MANIFIESTO.md` y figuras como enlace en el 4.1 | Existen solo en la versión Markdown de Álvaro, no en su LaTeX/PDF. |
| G: «RT-06.01 del caso» citado mal (Crítica) | El RT-06.01 del caso es la tipología de emplazamiento, que es justo lo que se cita. Como mucho, ajuste menor. |
| G: «el objetivo de sincronización del CD (≤ 2 h) aparece solo en físico» | Falso: está en §4.1.4.4 y en la Tabla A.23 del 4.1. |
| C (análisis de ADR anterior): «4.1 dice que los portales se acceden por intranet o VPN» y «DMS por sitio» | Era del 4.1 viejo (`entrega_2/texto/arquitectura_logica.md`). El 4.1 de Álvaro ya está alineado en ambos puntos. |

**Pendientes conocidos que quedaron resueltos dentro de 4.2:** <30 s vs. ≤60 s (son componentes distintos), TC58e −20 vs. −30 °C, terminales de Talca 132/150 vs. 144, y 12.600 vs. 16.100 mensajes IoT. Siguen abiertos: Concepción (C1) y la diferencia de 21 vs. 28 puntos y de 3 vs. 2 gateways **frente al 4.1** (B1 y B2).

**Coincidencias verificadas (no requieren cambio):** Laravel 13/PHP 8.5, Kotlin, PostgreSQL 16, RabbitMQ local + SQS FIFO + SNS, CloudFront/WAF/Shield, Verified Access para consolas, puerta de API local en VM-01/VM-C01/E-01, caché de identidad en VM-05/VM-C03/E-01, credenciales de 8 h/14 h, manifiesto de 26 h, DMS solo desde Talca, DynamoDB con TTL de 30 días, OpenAS2, ERP como único emisor de DTE, conmutación <30 s, cinco ambientes (H3, mes 6), seis instalaciones con cinco de cómputo, autonomía de 24 h/14 h, sincronización de 10 min/2 h, umbrales p95 (Tabla 25 = Tabla A.23), clasificación de servicios (Tabla 10), 96 camiones (42 + 54), 1.400/2.600 entregas, 28 termógrafos (18 + 10), 160 conductores de 10 empresas, títulos obligatorios del índice del cap. 4.
