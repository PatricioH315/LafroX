# Revisión de coherencia del Subdocumento 4 — 26-10-2026

## Alcance y método

- **Entregables revisados (lectura completa):** `LAFROX-Subdocumento4.pdf` (193 pp.), `LAFROX-Subdocumento4-Anexos.pdf` (116 pp.) y `LAFROX-Formulario-T-11.pdf` (45 pp.), rama `subdoc-4` en `479807e`.
- **Cruce con los demás subdocumentos (PDF de las ramas remotas):** SD1 y T-6 (`LafroX-Subdoc1-LateX`), SD2 (`LafroX-Subdoc2-LateX`), SD3, anexos y T-12 (`LafroX-Subdoc3-LateX`), SD5 (`LafroX-Subdoc5-LateX`), SD6, T-9 y T-10 (`LafroX-Subdoc6-LateX`), SD7, T-14, T-15 y T-18 (`LafroX-Subdoc7-LateX`), SD8, anexos y T-16 (`Lafrox_Subdocumento_8_Latex_Nuevo`), SD9, T-13 y T-17 (`LafroX-Subdoc9-LateX`), SD13 y T-19 (`LafroX-Subdoc13-LateX`). SD10–SD12 no tienen contenido.
- **Comprobaciones por script:** existencia de cada sección, anexo y tabla del SD4 citada por otros subdocumentos; correspondencia anexo–tabla en el T-12; cifras clave (RTO/RPO, disponibilidad, camiones con frío, terminales, Starlink y operadores, versiones, hitos, códigos S/V/RNG/RF/RNF); citas contra listas de referencias; títulos seguidos de lista o tabla; leyendas «Fuente:» sin tabla ni figura.
- **Reglas aplicadas:** `aclaraciones-licitacion.md` (secciones 2–7) y la retroalimentación del Informe 1.

Estado: **Corregido** (aplicado en esta revisión), **Decisión** (requiere al equipo) o **Fuera del SD4** (vive en otro subdocumento; no se modificó).

## 1. Críticos: indicios de la sección 7.1 de las aclaraciones

| N.º | Hallazgo | Dónde | Estado |
|---|---|---|---|
| C1 | Notas de dibujo dentro de las figuras lógicas: «Actores y canales del definitivo», «Tablet: dispositivo alternativo del general», «Vista funcional de los recorridos del general», «Destinos reproducidos del XML definitivo. Los módulos son contexto», «Monolito modular Laravel/PHP. Los módulos mantienen sus nombres. Las relaciones externas conservan sus destinos», «Mecanismos y dependencias del definitivo», «Persistencia local y central: vista detallada en la página 6», «Las relaciones de módulos con cada mecanismo se conservan. No se asignan nuevas garantías de entrega», «Dominios lógicos y ubicación del definitivo», «Se mantienen los tiempos de retención y el buffer indicados en el definitivo» | Figuras 2, 3, 4, 6, 7, 10 y 12 (`ARQL-21`, `22`, `23`, `24`, `25`, `26`, `28`) | **Decisión** (editar en draw.io; no se tocaron imágenes) |
| C2 | Códigos internos en figuras: «Secrets Manager + SSM (D13)» y «MDM gestionado N-13 (D15)» | Figuras 1 y 11 (`ARQL-01`, `ARQL-27`) | **Decisión** (draw.io) |
| C3 | Marcas de versión: «versión 9.4» en el título de la Tabla A.42 y en la fuente de ADR-24 | Anexo 4-W y Anexo 4-O | Corregido |
| C4 | Alusiones a un diseño anterior: «utilizado en el diseño precedente», «la solución previa agregaba Celery», «El cambio de selección no acredita una migración…», «por su uso en el diseño precedente», «el contraste con el diseño precedente» | 4.1.7.1, Tabla 3, ADR-23, Anexo 4-P | Corregido |
| C5 | Referencias a secciones inexistentes: «matriz de sección 7.4» (V16), «banco 2.4.3», «mapeo 2.4.4» | Anexo 4-W, Tabla A.42 | Corregido |
| C6 | Trece leyendas «Fuente:» bajo listados (tablas convertidas a listas), sin tabla ni figura asociada | 4.2.2.7, 4.2.3.1, 4.2.4.1.1, 4.2.4.3, 4.2.4.5, 4.2.5.3, 4.2.5.4, 4.2.6.3, 4.2.6.6, 4.2.6.10, 4.2.6.11, 4.3.2.3, 4.3.2.5 | Corregido (se eliminaron las leyendas) |
| C7 | Párrafo duplicado palabra por palabra («Los 59,44 W del ARK-1251…») | Anexo 4-W.8, tras la Tabla A.40 | Corregido |

## 2. Altos: contradicciones y cifras

| N.º | Hallazgo | Dónde | Estado |
|---|---|---|---|
| A1 | Las portadas declaran «Entrega 2» y emisión el 12-10-2026, pero ADR-23 y ADR-24 se registran el 24-10-2026 (Tabla A.19) y la cadena de frío en ruta es posterior | Portadas de los tres PDF; Tabla A.19 | **Decisión** (fecha y número de entrega) |
| A2 | Tabla A.31, dimensión 9: «0,58 + 3,20 GB/año» y «2,89 + 3,20 GB retenidos», sin la cadena de frío en ruta; la Tabla 16 y 4-W.4 dan 6,77 GB/año y 33,83 GB | Anexo 4-W | Corregido |
| A3 | El T-11 oferta cantidades del año 3 (77 EC55; 121 TC58e, ZQ620 y PAX; 235 MC9400), pero 4.2.6.4 y 4-W.3 llaman «cantidad a proveer» a la inicial (69/106/207) y 4.2.1.1 afirma que «el T-11 distingue las unidades iniciales de la compra del año 3», lo que el T-11 no hace | 4.2.1.1, 4.2.6.4, 4-W.3, T-11 | **Decisión** (qué cantidad se oferta) |
| A4 | El SD4 cita subdocumentos posteriores (SD5 5.2.8 y Anexo 5-A; SD9 Tabla 9.11; SD13), contra la regla de citar solo subdocumentos anteriores | 4.1.3.4, 4.1.3.7, 4.1.4, 4.1.5, 4.2.4.1, 4.2.6, Anexo 4-N | **Decisión** |
| A5 | Título del SD4: las portadas decían «Arquitectura de la solución»; el T-7, el T-11 y los demás subdocumentos usan «Arquitectura lógica y física de la solución» | Portadas, `pdftitle`, entradas LafroX (2026d/e) | Corregido |
| A6 | Cita sin referencia: «(Ministerio de Salud, 1996, arts. 102, 105 y 192)» | 4.1.4.2 | Corregido (se agregó DS N.º 977) |
| A7 | Referencias sin cita: cuerpo (AWS s. f.-j a -n, ISO 2025a y 2026, LafroX 2026e–j, Iridium, Teltonika, Moxa, Subtel); anexos (LafroX 2026d, f, g, h, ISO 2025a y 2026, y los nueve marcos de 4.1.7.1); T-11 (LafroX 2026d, e, g, Fortinet, Iridium, Moxa s. f.-c, Zebra s. f.-f). Además, el anexo citaba «LafroX, 2026» sin letra | Listas de referencias | Corregido (citas agregadas donde ya se usaba la fuente; AWS j–n retiradas del cuerpo y Zebra s. f.-f del T-11) |
| A8 | Término «A2» usado sin definir | 4.1.3.2, 4.1.4.2, 4.2.2.4, Tabla 11, 4.3.2.8; anexos 4-G, 4-N y Tabla A.42 | Corregido (definido en su primera aparición en cuerpo y anexo) |
| A9 | Pruebas V1–V21 citadas en el cuerpo sin indicar dónde se definen | 4.1.12, 4.2.1.4, 4.2.4.7, 4.3.2.8 | Corregido (remiten a la Tabla A.42) |
| A10 | Eventos de frío con productor «TC58e» o «M9 / TC58e», contra la regla de productor único por módulo (4.1.3.5 y CR-02) | Tabla A.2 | Corregido («M9 (TC58e)») |
| A11 | Expresiones de pendiente: «se confirma con Globalsat Chile», «sujeto a confirmación de proveedor», «deben confirmarse con Globalsat Chile» | 4.2.3.1, 4.3.2.8, ADR-24 | **Decisión** (redacción; pueden leerse como «pendiente de validar») |

## 3. Medios y formales

| N.º | Hallazgo | Estado |
|---|---|---|
| M1 | Guiones visibles «---» en los títulos de los anexos, en los encabezados INT-xx y en la portada («Sobre N.° 2 ---»); «1--3», «4--6»… en los títulos de 4.2.6.3–4.2.6.7 y 4-W.2–4-W.7 (la fuente sans no forma ligaduras) | Corregido en el SD4 (también en la clase de esta rama). Los demás subdocumentos muestran el mismo «---» en su portada |
| M2 | Punto doble en once encabezados de párrafo («Software de cadena de frío en ruta..», «Contraste con Django/Python..», etc.) | Corregido |
| M3 | Erratas: «desdel», «atiendel», «muestral listado» (×2) y comilla de cierre en «”modo offline”» | Corregido |
| M4 | Anexo 4-N: GW-CENT se realizaba en N-03 (Portal de Proveedores); UI-WEB y BOR-PUB omitían N-03 | Corregido (N-04/N-12; N-01 a N-03) |
| M5 | ADR-24 antes de ADR-23 en las Tablas A.18 y A.19; nombres de ADR-23 y ADR-24 distintos entre tabla y ficha | Corregido |
| M6 | La ficha ADR-24 usa otro formato («Decisión:», «Alternativas y criterio:») que las demás | **Decisión** (opcional) |
| M7 | Títulos seguidos directamente de lista o tabla: «Incorporación de las innovaciones del SD13», «Amenazas y pruebas negativas del kit de camión» | Corregido (frase introductoria) |
| M8 | Tablas A.25 y A.42 con «Fuente: …» dentro del título | Corregido (fuente al pie) |
| M9 | T-11: párrafo «Responsabilidad del sistema de frío…» ubicado después de las referencias; nota imperativa «Exigir rango…»; «Contrato LafroX 5.3.4»; RT-13.08 atribuido solo al caso | Corregido |
| M10 | 4.1.6.1: el párrafo de INT-05 aparecía antes de la introducción de la sección | Corregido |
| M11 | Citas a las Bases sin página: RT-14.08, RT-02.10, RT-06.02, RT-11.26, RT-16.23/16.24 | Corregido. Quedan sin página RT-21.13 (4.1.3.8), RT-17.07 (4.2.6.7) y RT-06.29 (T-11): falta verificar la página en el escaneo |
| M12 | Fuentes de las Tablas A.34, A.35, A.37 y A.39 con páginas fijas desactualizadas («pp. 78–104») | Corregido (referencia automática) |
| M13 | Listas de referencias fuera de orden alfabético (entradas agregadas al final) y letras que no parten en «a» (Moxa s. f.-c, Zebra s. f.-f, AWS s. f.-j a -n en el anexo) | **Decisión** (reordenamiento mecánico, sin cambio de contenido) |
| M14 | Declaración de IA: «Alto» en diagramas para 4.1 y 4.2 aunque las figuras de arquitectura son originales del equipo; una sola herramienta y un solo revisor | **Decisión** |
| M15 | Tabla 9: la franja 22:00–06:00 (despliegue permitido) se solapa con 05:30–07:00 (prohibido) | **Decisión** (bajo) |
| M16 | Precisiones menores: «especificación 5.1.1» sin indicar que es un paquete del T-14; «Los únicos elementos con suscripción» sin acotar a software; «Son candidatos de especificación… no se acredita su obtención» | Corregido |

## 4. Cruce con otros subdocumentos (no modificados)

| N.º | Hallazgo | Dónde corregir |
|---|---|---|
| X1 | Numeración de tablas del SD4 desplazada por la nueva Tabla 3 (cuerpo) y la nueva Tabla A.25 (anexo). El T-12 cita «Anexo 4-R (Tabla A.25)» en 21 filas (es A.26) y «Anexo 4-T (Tabla A.27)» en 5 filas (es A.28). SD9A y T-13 citan «SD4, Tabla 21» para los umbrales p95 (es la Tabla 22). SD5 cita «Anexo 4-W.10, Tabla A.40» (es A.41). SD7, SD7A, SD8 y T-18 citan «Anexo 4-W, Tablas A.32 y A.33» para la coordinación de reserva (el volumen está en las Tablas A.10 y A.37) | T-12, SD9A, T-13, SD5, SD7, SD7A, SD8, T-18 |
| X2 | SD9, SD9A y T-13 atribuyen a 4.2.4.1.4 el bloqueo por regresión de desempeño; está en 4.2.4.1.1 | SD9, SD9A, T-13 |
| X3 | SD8 ubica el RPO ≤15 min en §4.2.5.1; está en 4.2.4.4 y 4.3.2.4 | SD8 |
| X4 | R-015 significa «Recuperación y retorno exceden RTO/RPO» en el SD8 (como lo usa el SD4), pero en el T-16 R-015 es un riesgo de adopción de usuarios | T-16 |
| X5 | SD8 contiene «[Fecha de emisión no verificada.]» en sus referencias y SD8A «Costo: Pendiente» en R-015 | SD8, SD8A |
| X6 | SD13 y T-19 nombran el T-11 «Inventario de hardware y software»; el SD4 y el T-11 lo titulan «Especificaciones técnicas ofertadas» | SD13, T-19 |
| X7 | «V-18» es una consulta al CLIENTE (SD3 y SD4 4.1.17) y «V18» una prueba de frío (SD3 y SD4 4.2.4.7) | SD3 y SD4 (cambiar uno de los dos prefijos) |
| X8 | SD9 y T-13 afirman que, si cae un gateway de Talca, «el otro lee ambas cámaras»; el SD4 no declara esa conmutación | SD9, T-13 o SD4 |
| X9 | Portada con «Sobre N.° 2 ---» visible | Clase de cada subdocumento |

**Verificado sin diferencias:** nombres M1–M12 (SD3), quince actores, Laravel 13/PHP 8.5/PostgreSQL 16 (T-12, SD5), RTO ≤4 h y RPO ≤15 min, 99,9 % y 99,95 % y los cuatro niveles de servicio (SD1, SD2, SD3, SD9, T-12, T-17), 28 camiones con frío (18 + 10), Starlink en cinco sitios con Telsur, Entel y Claro (SD6, SD7, T-14), coberturas de 70 % y 80 % (SD1, SD6, SD7, SD9), H3 en el mes 6, canal moderno antes de enero de 2029, Bastián Trejo como Arquitecto de Solución, supuestos S-19 a S-44, mesa 7/2 agentes con límites 2.283 y 2.391 (T-15) y SOC en Valparaíso.

**Cálculos del SD4 verificados:** TPS por hora y por lugar (Tablas 14 y A.35), concurrencia (Tabla 15), volúmenes y retenciones (Tabla 16), mensajes por integración (Tablas 17, A.10 y A.37: 244.280 y 362.561), anchos de banda y drenaje (Tablas 18 y A.38), capacidad por sitio (Tablas 19 y A.39), tareas Fargate (Tabla 20), plan de capacidad (Tablas 21 y A.41), tiempo por guía (9,47/4,42/1,89 s), carga eléctrica y térmica (Tablas 24, 25 y A.40), ocupación de racks y conmutación regional (135 min). Todos cuadran.

## 5. Decisiones pendientes para el equipo

1. Editar en draw.io las figuras `ARQL-01`, `21`, `22`, `23`, `24`, `25`, `26`, `27` y `28` (C1 y C2).
2. Fecha de emisión y número de entrega de las portadas frente a ADR-23 y ADR-24 (A1).
3. Cantidades ofertadas: año 3 (T-11) o iniciales (cuerpo) (A3).
4. Mantener o retirar las citas a SD5, SD9 y SD13 (A4).
5. Redacción de las confirmaciones con Globalsat Chile (A11).
6. Corregir las citas desplazadas en T-12, SD5, SD7, SD8, SD9, T-13 y T-18 (X1–X3), y R-015 del T-16 (X4).

## 6. Seguimiento del 26-10-2026 (decisiones del equipo)

- **A1, fechas:** ADR-23 y ADR-24 quedan registrados el 12 de octubre de 2026, igual que la fecha de emisión de las portadas. No quedan otras fechas posteriores a la emisión en el SD4.
- **A3, cantidades:** la fuente de verdad son los supuestos S-31 y S-32 del SD3 («la compra inicial no varía»; el crecimiento cambia la compra del año 3), calculados en 4-W.3. El T-11 ahora declara ambas cifras por fila (por ejemplo, «62 + 7 = 69 al inicio; 70 + 7 = 77 en el año 3»; N-13: 382 al inicio y 433 en el año 3). En 4.2.6.4 se habla de la cantidad inicial y se remite al T-11 para el crecimiento; en 4-W.3 se habla del «parque inicial».
- **A4, citas a SD5, SD9 y SD13:** se mantienen y se verificó su destino. SD5 5.2.8 (exportación asíncrona) y Anexo 5-A (`mae_parametro`, `not_plantilla`) corresponden; la separación reserva/retención se precisó a SD5 5.2.3. La cita «Subdocumento 9, Tabla 9.11» era incorrecta (esa tabla es el calendario de calidad): ahora cita el Formulario T-13, sección 4.1 (instancias de Preproducción por campaña). Las cinco innovaciones del SD13 coinciden.
- **A11, Globalsat:** las frases se reescribieron como compromiso contractual (paquete 5.3.4 del T-14) con su alternativa de diseño (receptor SBD en ECS), sin «se confirma» ni «sujeto a confirmación».
- **X1 y X2, citas de otros subdocumentos:** se reemplazó la cita a tablas del SD4 por la cita al anexo o a la sección, con commits locales sin publicar:
  - `LafroX-Subdoc3-LateX` `db47447`: T-12, 323 citas «SD4-Anexos 4-X (Tabla A.n)» → «SD4-Anexos 4-X»; 4-W.8 → «4-W.5 y 4-W.8» (T-12 pasa de 264 a 258 páginas; nadie lo cita por página).
  - `LafroX-Subdoc5-LateX` `7957389`: «Tabla A.40» → «sección 4-W.10».
  - `LafroX-Subdoc7-LateX` `ef3d196`: T-18 y Anexo 7.F, «Tablas A.32 y A.33» → «sección 4-W.5».
  - `LafroX-Subdoc9-LateX` `beb7e9d`: SD9A y T-13, «Tabla 21» → «sección 4.2.6.11»; regresión de desempeño 4.2.4.1.4 → 4.2.4.1.1.
- **SD8:** no se modificó (pendiente de su actualización por el equipo); conserva «Tablas A.32 y A.33», R-015 distinto del T-16 y las marcas de pendiente.

## 7. Cruce en profundidad entre el SD4 y el Formulario T-11 (26-10-2026)

**Método.** Se revisaron las 91 frases del cuerpo y de los anexos que remiten al T-11, y cada fila del T-11 (producto, ubicación, cantidad, potencia y justificación) contra el cuerpo (4.2.1, 4.2.2, 4.2.3, 4.3.1, Tablas 19 y 24, Figuras 17 y 28) y el Anexo 4-W (Tablas A.36, A.39 y A.40). También se cruzó cada servicio de nube nombrado en el SD4 con el catálogo 4.2.3.1, el inventario del Anexo 4-P y el T-11.

**Coincide sin cambios:** especificaciones y potencias de nodos, NAS, firewalls, switches, KVM, ERP y conmutadores (Tabla 24 = T-11); servidores de Concepción (16 hilos, 32 GB, 3,84 TB en RAID 10, 2 × 500 W) y mini-PC E-01 (59,44 W, 6 + 1); UPS de 15 kVA, generador de 25 kVA, climatización de 2 × 10 kW y sala de UPS de 3,5 kW; UPS de gabinetes (1,5, 5 y 0,75 kVA, con 59, 68 y 61 %); ocupación de R01 y R02 (15U y 12U, posiciones U); enlaces (fibra de 20/10 Mbps, LTE con mínimos de 10/6 Mbps, ocho planes, cinco Starlink); puntos de acceso (39/20/6 + 7); kit de camión (28 + 3, 93 sondas, 93 botellas, 62 SIM); B-01 (21 puntos, 7 módulos); terminales, impresoras, terminales de pago y balanzas (reservas del 10 % redondeadas hacia arriba); cuentas, colas, instancias de Aurora, tareas Fargate, cachés, verificadores y colectores; siete dependencias de salida; 217 endpoints con EDR.

**Corregido:**

| Incoherencia | Corrección |
|---|---|
| 4.2.1.1 dice que los servidores tienen repuestos por componente «declarados en el T-11»; el T-11 no los declaraba | T-11: clúster de Talca (un NVMe de 960 GB, un M.2 de 480 GB y una fuente de 800 W), Concepción (un SSD de 1,92 TB y una fuente de 500 W) y NAS (un disco de 4 TB), con la regla del 10 % redondeado hacia arriba |
| 4.2.4.1.1 fija las métricas de escalamiento «conforme a N-04 del T-11»; la fila N-04 no las tenía | T-11 N-04: consumidor por edad del mensaje más antiguo sobre 60 s y trabajos por más de 100 mensajes, con métricas de un minuto |
| 4.2.1.2 dice que se entrega una unidad de prueba de cada tipo y variante «especificado en el T-11»; el T-11 no lo mencionaba | T-11, introducción: unidades de prueba incluidas en las cantidades declaradas (RT-08.15) |
| Amazon SES y AWS End User Messaging Social (INT-11), AWS Certificate Manager (Anexo 4-R) y AWS Fault Injection Service (pruebas de resiliencia) se usan en el SD4, pero no estaban en el catálogo 4.2.3.1, en el inventario del Anexo 4-P ni como servicio en el T-11 | Agregados a 4.2.3.1 (fila Notificaciones; ACM en identidad; FIS en operación), al inventario del Anexo 4-P y al T-11 (fila «N-04 — Notificaciones»; ACM y FIS en N-12) |
| Termógrafo: el cuerpo exige calibración según EN 13486; el T-11 decía «calibración ISO 17025» | T-11 B-03: certificado de calibración según EN 13486 emitido por laboratorio ISO/IEC 17025 |
| Aplicación de terreno: el cuerpo define los perfiles de preventa, reparto y bodega (más Calidad); el T-11 decía «recepción, preparación» | T-11: «preventa, reparto, bodega y Calidad» |
| Keycloak se restituye en us-east-1 (4.2.3.5 y 4.3.2.5); la fila A-05 del T-11 solo lo ubicaba en sa-east-1 | T-11 A-05: «Fargate, con restitución en us-east-1» |

El T-11 pasa de 45 a 46 páginas; ningún documento lo cita por página.

## 8. Cruce en profundidad entre el SD4 y el Formulario T-12 (26-10-2026)

**Método.** Se leyeron las 648 filas del T-12 (`origin/LafroX-Subdoc3-LateX`, 590 «Cumple», 36 «Cumple parcialmente» y 22 «No cumple»); 505 citan el SD4 o el T-11. Se validaron por script:

- las 1.296 citas a secciones del cuerpo y a anexos del SD4, contra el índice compilado;
- los códigos del T-11 citados, contra sus filas;
- la presencia del código RT/RF en la sección citada (211 filas coinciden; las 8 restantes tratan el tema sin repetir el código);
- unos 110 datos que el T-12 afirma (versiones, cantidades, plazos, retenciones, márgenes, potencias, distancias y dotación), contra el texto del cuerpo, los anexos y el T-11.

Además, cada brecha declarada («Falta: …») se contrastó con el SD4 vigente.

**Coincide sin cambios.** Todas las citas existen y los datos concuerdan:

- versiones: Laravel 13, PHP 8.5, PostgreSQL 16, Angular 22, Keycloak 26 y RabbitMQ 4.x del Anexo 4-P;
- capacidad y márgenes: 14,66 y 21,99 TPS; márgenes de 155,6, 151,9 y 158,3 %; 8,9 kW, factor 0,95 y PUE;
- centro de datos: R01 15U (36 %) y R02 12U (29 %); seis cámaras IP; 7.700 y 2.700 km;
- retenciones y respaldo: auditoría por 7 años con Object Lock; registros 12 + 24 meses, métricas 13 meses y trazas 30 días; PITR de 35 días;
- tiempos: ventana de deduplicación de 30 días (4.1.16); alarmas de réplica a 60 s, 5 y 15 min; presupuesto de error de 43 min;
- dotación: NOC y SOC en Valparaíso con 4 personas por posición, 5 desde el 26-04-2028;
- terreno: 9,83 MB por turno, 81 baterías y 40 cunas;
- clasificación de servicios: la de 4.1.10 y la de 4.2.4.3 son idénticas.

Las brechas declaradas siguen vigentes en el SD4: doble acometida, intensidad de carbono, conmutación con autorización del CLIENTE, AS2 por NLB sin CDN/WAF, excepción TLS 1.2 del ERP, segundo factor de portales externos y familias sin borrado remoto. La nota de RT-26.01 sigue siendo cierta: el SD13 aún no incorpora el kit B-04 a B-15.

**Corregido:**

| Incoherencia | Corrección |
|---|---|
| El equipo retiró del cuerpo del SD4 la mención explícita a R-015 (06_e, «limitación técnica de recuperación»); el T-12 (RNF-20.06, RT-07.04 y RT-02.11) y el ADR del Anexo 4-O la conservaban | T-12: «es una limitación técnica de recuperación que se presenta al mandante», sin las citas a R-015 del SD8. Anexo 4-O: «Su registro como limitación técnica de recuperación no constituye aceptación del mandante» |
| RT-08.01 citaba «4-W.5 y 4-W.8»: en la conversión anterior se tradujo mal «Tablas A.38 y A.39» (numeración previa = capacidad por VM y UPS de borde, ambas en 4-W.8; 4-W.5 trata enlaces) | T-12 RT-08.01: «SD4-Anexos 4-W.8» |
| RT-03.18 hablaba de «433 terminales»; el T-11 (N-13) declara 382 al inicio y 433 en el año 3 | «382 terminales al inicio y 433 en el año 3» |
| RT-16.20 nombraba solo «Amazon SNS/API de canal»; el SD4 y el T-11 (N-04 — Notificaciones) fijan SES, SNS y End User Messaging Social | Componente con los tres servicios y cita al T-11 (N-04 — Notificaciones) |

Commits: T-12 en `LafroX-Subdoc3-LateX` `6818ecb` (259 páginas, sin referencias indefinidas; nadie lo cita por página); Anexo 4-O en `subdoc-4` (anexos de 116 páginas).

## 9. Cruce del SD4 con el SD8 actualizado (26-10-2026)

**Fuente.** `origin/Lafrox_Subdocumento_8_Latex_Nuevo` (`bfbd7323`, 26-10-2026 20:40): cuerpo (`08_plan_riesgos/contenido.tex`), Anexos 8.A–8.B y Formulario T-16, con 33 riesgos R-001 a R-033. La rama antigua `LafroX-Subdoc8-LateX` (10-10) no se usó. En la rama nueva no hay PDF del cuerpo; solo están los PDF de los anexos y del T-16.

**Citas entre documentos.** El SD4 ya no cita al SD8, al T-16 ni ningún código R-xxx. El SD8 nombra al Subdocumento 4 en su introducción, sin cita, y mantiene una entrada propia en su lista de referencias.

**Datos de los riesgos frente al SD4: todo coincide.**

| Riesgo o afirmación del SD8 | SD4 |
|---|---|
| R-009: ante un timeout se consulta el cargo con la misma clave antes de reintentar | Anexo 4-H, INT-09: «se consulta por la misma clave antes de volver a cobrar» |
| R-010: ruta aprobada y cartografía precargada | Anexo 4-H (INT-10) y Anexo 4-J |
| R-012: el CLIENTE compra el equipamiento de terreno según la especificación de LafroX | 4.2.1 y T-11: los equipos de uso los compra el CLIENTE (paquete 5.1.1 del T-14) |
| R-014: el termógrafo en camiones de terceros requiere autorización del propietario | 4.2.1.4: se instala con el acuerdo de cada transportista (S-28) |
| R-019: los sitios dependen de fibra, LTE o satélite | 4.2.5.1 y T-11 (D-03, D-04 y D-06) |
| R-021: las regiones de Brasil y Estados Unidos requieren aprobación del CLIENTE | ADR-19: «sujetas a aprobación del CLIENTE»; 4.2.3.2 y 4.3.2.2 |
| R-022: un cambio urgente en congelamiento requiere autorización | 4.2.4.1.4 (RT-11.04) |
| R-024, R-025, R-026 y R-027: validación EDI, MDM, WAF/Shield y copias inmutables | OpenAS2 (firma y MDN), Android Enterprise/Zebra DNA, Shield Advanced, Vault Lock y Object Lock |
| 8.3.3: RTO 4 h, RPO 15 min, NAS destruido junto con el sitio, 96 despachos, retiro sanitario en menos de 2 h y AL-DR-01 | 4.2.4.4, 4.3.2.4 (limitación técnica), 4.1.8, 4.1.4.2 y Anexo 4-V |
| Tabla 8.1: Bastián Trejo (ARQ) y Encargado de Seguridad | Anexo 4-O (Bastián Trejo, Arquitecto de Solución) y Anexo 4-W.7 |

**Observaciones para el equipo del SD8 (no se modificó):**

1. La referencia «LafroX. (s. f.-b). *Subdocumento 4…*, §§4.1.4.4, 4.2.5.1 y 4.3.2.4; Anexos 4-G, 4-I y 4-W. [Fecha de emisión no verificada.]» tiene tres problemas:
   - ninguna cita del texto la usa;
   - el SD4 tiene fecha (12 de octubre de 2026), así que no corresponde «s. f.»;
   - la nota entre corchetes es una marca de borrador, que la sección 7.1 de las aclaraciones cuenta como indicio de IA. Lo mismo ocurre con las entradas del SD3 y del SD13.
2. En 8.3.3, «AL-DR-01/E8-05»: E8-05 solo se define en la versión antigua del SD8. AL-DR-01 sí existe en el SD4.
3. Los 85 minutos del retiro sanitario provienen del SD5 (Anexo 5, Tabla A.23), no del SD4.

**Riesgos residuales del SD4 sin riesgo equivalente en el T-16** (no es una contradicción: RT-02.11 se responde en el SD4):

- la identidad central;
- el ERP como único emisor de DTE en Talca;
- las fallas del kit de frío de 4.1.12;
- la limitación de recuperación ante la caída de los tres caminos seguida de la destrucción del sitio (4.3.2.4).

El SD8 trata este último escenario en 8.3.3 como condición de prueba, sin código de riesgo, igual que el SD4.

**Conflicto que queda: R-015 en el SD7.** En el SD8 y el T-16, R-015 es un riesgo de adopción. El T-18 (`formulario-t18/contenido.tex`, línea 237) y el Anexo 7.F (`tab_7F1.tex`, fila P7-10) lo siguen usando para el escenario de recuperación del SD4.

No requiere cambios en el SD4.
