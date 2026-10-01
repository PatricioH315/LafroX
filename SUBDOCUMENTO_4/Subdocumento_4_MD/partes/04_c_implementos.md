<!-- Fuente: Subdocumento_4_LateX/04_arquitectura_fisica/partes/04_c_implementos.tex — conversión fiel; editar el .tex y regenerar -->

<a id="sec:implementos"></a>
## 4.2.1 Especificaciones Implementos a proveer (Hardware y Software)

Esta sección resume y analiza el equipamiento y el software que la solución requiere en las instalaciones del CLIENTE, en el terreno y en la plataforma de nube. El detalle de cada elemento, con su producto ofertado, su ubicación, su cantidad y su justificación, se entrega en el Formulario T-11. El equipamiento físico lo adquiere el CLIENTE, y el adjudicatario lo especifica, instala, integra y mantiene durante el contrato.

### 4.2.1.1 Síntesis del equipamiento por familia

La Tabla [1](#tab:t26) cruza cada familia de equipamiento con el sitio donde se instala. Las cifras son las unidades en operación; la reserva se analiza a continuación de la tabla.

<a id="tab:t26"></a>
**Tabla 1.** Equipamiento en operación por familia y por sitio
| Familia | Talca | Concepción | Cada cross-docking | Terreno |
| --- | --- | --- | --- | --- |
| Servidores y nodos de cómputo | 3 | 1 | 1 | – |
| Respaldo local (NAS WORM) | 1 | – | – | – |
| Firewalls | 2 | 2 | 2 | – |
| Switches de núcleo, de gestión y de sitio | 3 | 2 | 1 | – |
| Switches de acceso en las bodegas | 4 | 2 | – | – |
| Puntos de acceso Wi-Fi 6E | 39 | 20 | 2 | – |
| Terminales de bodega | 120 | 60 | 2 | – |
| Impresoras de andén | 4 | 2 | – | – |
| Balanzas de recepción | 2 | 1 | – | – |
| Puntos de temperatura en cámaras | 15 | 6 | – | – |
| Gateways IoT | 2 | 1 | – | – |
| Estaciones de trabajo | 5 | 3 | – | – |
| Terminales de preventa | – | – | – | 62 |
| Equipos de reparto por camión | – | – | – | 96 |
| Termógrafos de camión | – | – | – | 28 |

La tabla muestra que la operación se concentra en el terreno y en las bodegas, no en la sala técnica. Solo en la calle trabajan 62 terminales de preventa y 96 camiones equipados, cada uno con un terminal de conductor, una impresora de cabina y un terminal de pago; en las bodegas y en los cross-docking, 186 terminales y los puntos de acceso que los conectan. Frente a eso, el cómputo y el almacenamiento suman 8 equipos: 3 servidores en Talca, 1 en Concepción, 3 mini-PC y la NAS. Esa proporción refleja el caso, donde la operación ocurre en la calle, en la cámara y en el andén, y explica por qué la gestión de dispositivos (N-13) es un componente con emplazamiento propio y no un accesorio.

Los equipos de reparto se cuentan por camión y no por conductor, porque los conductores de los transportistas rotan sin aviso y el equipo queda en el vehículo (S-30). Los terminales de bodega se comparten entre turnos, como contempla el perfil operacional del caso (RT-12.11; Bases Técnicas del caso, Cap. 15, p. 27), por lo que su cantidad la fija el turno con más personas trabajando a la vez: los 120 preparadores nocturnos de Talca y los 60 de Concepción (S-39); la carga de los camiones la hace esa misma cuadrilla (S-33). Los puntos de acceso son una estimación preliminar por superficie, con mayor densidad dentro de las cámaras, que el estudio de cobertura confirma (S-36).

A las unidades en operación se suma la reserva del numeral 8.4 de las Bases Técnicas Transversales (Cap. 8, p. 19): el 10 % del parque de cada tipo de dispositivo y de componente crítico, redondeado hacia arriba. Con ella se cotizan 69 terminales de preventa, 106 de cada equipo de reparto, 205 terminales de bodega, 72 puntos de acceso, 7 impresoras de andén, 4 balanzas, 7 módulos y 24 sondas de temperatura, 31 termógrafos y 4 gateways IoT, además de una unidad de reserva por cada modelo de equipo de red y para el mini-PC: una para los firewalls de los centros de distribución, una para los de los cross-docking, una para los switches de núcleo, una para los de acceso, una para los de los cross-docking y una para el mini-PC. El switch de gestión no lleva reserva, porque su falla no detiene la operación. Los servidores no llevan una unidad entera de reserva: se cubren con repuestos por componente, como discos y fuentes. A tres años, el crecimiento de los viajes y de la dotación que proyecta el caso agrega 15 unidades de cada equipo de reparto, 8 terminales de preventa y 28 terminales de bodega (S-31, S-32); los termógrafos no crecen, porque el caso no proyecta más camiones con equipo de frío (S-38). El detalle elemento por elemento está en el Formulario T-11, el cálculo de cada cantidad en el Anexo 4.B y los supuestos en el registro del Subdocumento 3.

Se proveen ocho estaciones nuevas para despacho, administración, planificación, calidad y TI. Los equipos existentes de los usuarios de oficina se incorporan a la gestión central con CrowdStrike Falcon, cifrado de disco, parches y control de extraíbles como condición de acceso por Verified Access (sección [4.4.16](14_m_decisiones_adr.md#sub:adr-16)).

### 4.2.1.2 Criterios de selección

Cada familia se especifica contra una condición del caso que el equipamiento de oficina no resiste:

- Los 22 terminales de la cuadrilla de congelado están certificados para trabajar a -30 °C con guantes gruesos y batería de recambio en caliente, porque la preparación de congelados ocurre a -22 °C. Los 183 restantes atienden la bodega seca, la cámara de refrigerado sobre 0 °C y los cross-docking, y son el modelo estándar, porque esas condiciones no exigen la versión para congelado (S-34).
- Los terminales de terreno operan un turno completo sin señal, a una mano y bajo sol directo.
- Los mini-PC de los cross-docking son de rango industrial, porque las naves no tienen climatización y el supuesto de diseño es de hasta 50 °C bajo la techumbre en verano.
- Los 28 termógrafos en operación cubren los 18 camiones propios y los 10 refrigerados de los transportistas que declara el caso, porque el instrumento viaja con la carga y su registro ampara la cadena de frío aun cuando el vehículo no sea del CLIENTE; en los camiones de terceros se instala con el acuerdo de cada transportista (S-28). Están calibrados contra un patrón NIST en dos puntos, porque su registro es la prueba de la cadena de frío ante un cliente o ante la autoridad sanitaria.

En la sala técnica se aplica redundancia sin sobrecompra:

- Talca: los tres servidores del clúster son idénticos, de modo que la pérdida de cualquiera deja capacidad para todas las máquinas virtuales; el crecimiento de 3 veces se absorbe agregando discos y memoria en los mismos nodos, dentro del margen de crecimiento de los racks, y los firewalls van en par.
- Concepción: el servidor se dimensiona a su propia bodega, sin sobrecompra, y sus switches de núcleo van en par porque es el sitio de recuperación on-premise.
- Los cinco sitios: los firewalls van en par activo/pasivo, porque RT-08.03 (Bases Técnicas Transversales, Cap. 8, p. 18) no admite cortafuegos en punto único de falla. El servidor de Concepción, y el mini-PC y el switch de cada cross-docking, quedan como puntos únicos de falla aceptados, cubiertos por la operación autónoma del sitio y por la unidad de reserva que viaja en el camión de línea nocturno desde Talca.

### 4.2.1.3 Software y licenciamiento

El software de base que opera el adjudicatario es de código abierto y se organiza así:

- PostgreSQL con PostGIS, RabbitMQ, Keycloak, Proxmox VE, Ceph y Docker sostienen la plataforma, junto con el motor de optimización de rutas.
- La aplicación está escrita en PHP 8.5 con Laravel 13 y sus dependencias fijadas por Composer. Las dependencias de PHP se revisan en cada construcción con `composer audit` y su licencia se verifica contra una lista de licencias admitidas antes de incorporarlas.
- Los portales usan Angular y TypeScript; las aplicaciones de terreno usan Kotlin.

Los únicos elementos con suscripción son los servicios de la plataforma de nube, descritos en la sección [4.2.3](02_b_servicios_nube.md#sec:servicios-nube), la gestión de dispositivos, los agentes de detección en endpoints y el orquestador de integración continua GitLab CI. Esta composición mantiene la reversibilidad de la solución y evita que el CLIENTE quede atado a un licenciamiento propietario.
