<!-- Fuente: Subdocumento_4_LateX/04_arquitectura_fisica/partes/02_c_conexiones.tex — conversión fiel; editar el .tex y regenerar -->

<a id="sec:conexiones"></a>
## 4.2.5 Conexiones, puntos de falla y contingencia

Esta sección describe cómo se conectan los sitios, el terreno y la nube, identifica cada punto donde esa conexión o su infraestructura puede fallar, y declara cómo se resuelve cada falla o, cuando no se resuelve de forma automática, cuál es la contingencia. Su punto de partida es el caso: la conectividad actual de Puelche se corta con frecuencia y en algunos lugares no existe, por lo que la solución no puede suponer un enlace disponible y debe decir, para cada conexión, qué pasa cuando no lo está.

### 4.2.5.1 Conexiones entre sitios, terreno y nube

Los dos dominios fijos, la nube y el on-premise, se conectan por túneles VPN IPsec que terminan en el par de firewalls de cada sitio (D-01) y en el Transit Gateway de AWS en sa-east-1, con enrutamiento dinámico BGP. El mismo Transit Gateway enruta entre los sitios, de modo que Concepción y los cross-docking alcanzan Talca sin exponerla a Internet. Los caminos de acceso se distribuyen así:

- Cada centro de distribución tiene dos caminos físicamente independientes: fibra y LTE.
- Cada cross-docking tiene dos caminos físicamente independientes: Starlink y LTE de dos proveedores.

Los terminales EC55 y TC58e acceden por red celular a CloudFront, cuyas rutas `/v1` y `/sync/v1` llegan a la API REST pública.

La Figura [10](02_c_conexiones.md#fig:conexiones) muestra estas conexiones.

<a id="fig:conexiones"></a>
**Figura 10.** Conexiones entre los sitios, el terreno y la nube

> Figura compuesta en TikZ en el LaTeX; ver main.pdf, página 57.

- Usuarios externos: clientes, transportistas y proveedores
- AWS sa-east-1
- Transit Gateway
- VPC Endpoints
- API REST pública
- CloudFront y WAF
- AWS us-east-1<br>recuperación<br>y réplica
- CD Talca<br> D-01 en par
- CD Concepción<br> D-01 de borde
- Cross-docking<br> E-01, tres sitios
- Terreno<br> C-01 y C-02
- Camiones<br> B-03

La figura distingue las entradas públicas, los túneles de sitio y las sincronizaciones locales en cuatro flujos:

- Sitios–Talca: Concepción y los cross-docking sincronizan con Talca por la VPN.
- Termógrafo–terminal: los termógrafos descargan por Bluetooth al terminal del conductor.
- Nube–VM: AWS DMS accede a VM-02 y `erp-sync` a VM-04 únicamente por el túnel IPsec autenticado.
- Cross-docking–SQS: los eventos críticos llegan a SQS FIFO sin depender de Talca.

Los 184 usuarios de administración, comercial y soporte de Talca y Concepción acceden a las consolas y a la administración de Keycloak solo por Verified Access. La consola Angular corre en Fargate tras un ALB privado y reenvía las llamadas a la API REST privada por el endpoint de interfaz execute-api. CloudFront publica únicamente los endpoints OIDC necesarios para autenticación y renovación de sesión por la API REST pública sin autorizador hacia Keycloak tras el ALB privado; el verificador local de relevos permanece en cada sitio. Las cadenas usan el canal AS2 descrito en la sección [4.4.11](14_m_decisiones_adr.md#sub:adr-11).

La Tabla [12](#tab:conexiones) resume cada conexión con su medio, su camino alternativo y el tiempo de conmutación entre ambos.

<a id="tab:conexiones"></a>
**Tabla 12.** Conexiones de la solución y su camino alternativo
| Conexión | Medio y protocolo | Camino alternativo | Conmutación |
| --- | --- | --- | --- |
| CD Talca con la nube | Fibra D-03, túneles IPsec con BGP | LTE D-04 | Menos de 30 s |
| CD Concepción con la nube | Fibra D-03, túneles IPsec con BGP | LTE D-04 | Menos de 30 s |
| Cross-docking con la nube | Starlink D-06, túneles IPsec con BGP | LTE D-04 de dos proveedores | Menos de 30 s |
| Concepción con Talca | TCP 8080 y 5432 con TLS sobre la VPN | Operación autónoma | No aplica |
| Cross-docking con Talca | AMQPS 5671 entre brokers, por la VPN | Envío diferido | No aplica |
| Terreno con la nube | Red celular, CloudFront, API REST pública | Almacén local del dispositivo | No aplica |
| Termógrafos con el terminal del conductor | BLE con el terminal del conductor, en ruta y al regresar | Registro interno del termógrafo | No aplica |
| Usuarios externos con los portales | Internet, HTTPS por CloudFront | Ninguno: el autoservicio requiere conexión | No aplica |
| Oficinas y trabajo remoto con las consolas | Internet, HTTPS por Verified Access | Otra conexión a Internet | No aplica |
| Cadenas con el canal AS2 | Internet, TLS 1.3 al Network Load Balancer | Reenvío AS2 hasta el acuse MDN | No aplica |
| Región primaria con la secundaria | Replicación nativa de Aurora, DynamoDB y S3 | Respaldo inmutable | Promoción autorizada |

Los cinco sitios tienen un camino alternativo hacia la nube. Concepción también opera sin los sistemas de Talca, el terreno sin señal y los termógrafos con registro interno. El autoservicio de los portales requiere conexión.

<a id="sub:superficie"></a>
### 4.2.5.2 Superficie de exposición

La Tabla [13](#tab:superficie) delimita las únicas entradas desde redes externas. Cada entrada usa un subdominio propio del dominio del CLIENTE gestionado en Route 53.

<a id="tab:superficie"></a>
**Tabla 13.** Superficie de exposición
| Entrada | Servicio y puerto | Quién accede | Control |
| --- | --- | --- | --- |
| Portales y API | CloudFront, HTTPS 443 | Clientes, transportistas, proveedores y terminales de terreno | WAF, protección contra bots, Shield Advanced y autorizador |
| Identidad | OIDC de Keycloak por CloudFront, HTTPS 443 | Personas usuarias | WAF y límites de tasa |
| Consolas | Verified Access, HTTPS 443 | Oficina y trabajo remoto | Identidad, MFA y postura |
| Canal AS2 | Network Load Balancer, TCP 443 con TLS 1.3 | Cadenas registradas | Lista de IP, certificados, firma y MDN |
| Túneles de sitio | VPN del Transit Gateway, IPsec UDP 500 y 4500 | Firewalls D-01 de los cinco sitios | Autenticación IKE y cifrado IPsec |

La tabla excluye toda otra entrada desde fuera de la red del CLIENTE. En recuperación ante desastres se activan las mismas entradas en us-east-1. MDM, EDR, SII, Transbank, GIS, notificaciones y telemetría de flota son dependencias de salida, detalladas en el Formulario T-11.

### 4.2.5.3 Puntos de falla en los sitios y en los enlaces

Cada conexión se apoya en equipos del sitio que también pueden fallar. La Tabla [14](#tab:fallas-sitios) recorre esos puntos de falla, desde el enlace hasta la energía del recinto, e indica para cada uno el mecanismo que la resuelve y la contingencia si ese mecanismo no basta.

<a id="tab:fallas-sitios"></a>
**Tabla 14.** Puntos de falla en los sitios y en los enlaces
| Punto de falla | Resolución | Contingencia |
| --- | --- | --- |
| Fibra de un centro de distribución | BGP conmuta los túneles al LTE en menos de 30 s. | Si cae también el LTE, operación local 24 h. |
| Caída del enlace de Talca para la oficina | Verified Access admite otra conexión a Internet con los mismos controles. | Plan de rutas y manifiesto aprobados en el WMS antes de las 22:00; tableros y costo de servir esperan el retorno. |
| Starlink de un cross-docking | El LTE de dos proveedores toma el tráfico en menos de 30 s. | La ventana de 3 h opera 100 % local y sincroniza al reconectar. |
| Enlace de Los Ángeles en la madrugada | Starlink queda como camino único, porque la red móvil falla a esa hora. | La ventana de madrugada opera íntegramente local. |
| Firewall de Talca | La unidad pasiva asume las direcciones y los túneles en menos de 30 s. | Operación local 24 h sin enlace. |
| Firewall de Concepción | La unidad pasiva asume el túnel y la conmutación de enlace en menos de 30 s. | La unidad dañada se reemplaza con la de reserva de Talca. |
| Nodo del clúster de Talca | Las VM se reinician en los nodos restantes, con sus datos replicados por Ceph. | Ante un segundo nodo, el DRP local promueve el WMS de Concepción en 1 a 2 h. |
| Instancia de escritura VM-02 | Se reinicia en otro nodo del clúster. | D-05 restaura la base en hasta 4 h sin enlace. |
| Disco de un nodo de Talca | El RAID 10 reconstruye sobre el repuesto en caliente. | Ceph conserva una segunda copia en otro nodo. |
| Miembro del stack de switches de Talca o de Concepción | El otro miembro mantiene el tráfico. | Reposición sin corte con la unidad de reserva de Talca. |
| Servidor de borde de Concepción | El RAID 10 tolera la falla de un disco; el equipo tiene fuente única y, ante su falla, se repone. | La pila se reinstala con la misma imagen y la base local se reconstruye desde el estado central, que ya recibió los eventos del sitio por las colas. |
| Mini-PC de un cross-docking | Equipo único; se repone con la unidad de reserva, que viaja desde Talca en el camión de línea nocturno. | El nuevo equipo se resincroniza desde Talca y SQS FIFO. |
| Firewall de un cross-docking | La unidad pasiva del par asume el túnel en menos de 30 s. | La ventana de 3 h opera 100 % local y sincroniza al reconectar. |
| Periféricos de andén | Sin redundancia por equipo. | La etiqueta se emite en otra de las impresoras del centro de distribución. |
| Energía de la sala de Talca | UPS N+1 de 30 min y generador que toma carga en 8 a 15 s. | Estanque de 24 h y contrato de reabastecimiento. |
| Climatización de la sala de Talca | Segunda unidad de precisión en N+1. | Alerta del monitoreo de los sensores ambientales. |

La tabla muestra que los firewalls van en par en los cinco sitios, porque RT-08.03 (Bases Técnicas Transversales, Cap. 8, p. 18) no admite cortafuegos en punto único de falla, y que los puntos únicos de falla que permanecen son el servidor de Concepción y el mini-PC y el switch de cada cross-docking, donde la redundancia no compensa su costo: la pérdida de sus enlaces se cubre con la autonomía local, y la falla de sus propios equipos, con la reposición y la resincronización indicadas en la tabla. Por el mismo fundamento, ese servidor, el mini-PC y el switch de los cross-docking operan con fuente única, excepción declarada a la exigencia de fuente redundante. La liberación sanitaria y el despacho no dependen de la nube. En la ventana de Talca, VM-02 se reinicia en otro nodo y otra impresora emite la etiqueta si falla la del andén. Los mecanismos de alta disponibilidad se detallan en la sección [4.2.4.3](11_j_despliegue.md#sub:3-alta-disponibilidad).

### 4.2.5.4 Puntos de falla en la nube, el terreno y las integraciones

La Tabla [15](#tab:fallas-nube) completa el recorrido con los puntos de falla que están fuera de los sitios: la nube, el terreno y los sistemas de terceros.

<a id="tab:fallas-nube"></a>
**Tabla 15.** Puntos de falla en la nube, el terreno y las integraciones
| Punto de falla | Resolución | Contingencia |
| --- | --- | --- |
| Zona de disponibilidad de sa-east-1 | Aurora conmuta en menos de 30 s, ElastiCache en menos de 60 s y Fargate reprograma las tareas. | La operación continúa en las zonas restantes. |
| Región sa-east-1 completa | Route 53 redirige el tráfico y, con autorización del CLIENTE, se promueve la réplica en us-east-1. | RTO de 4 h y RPO de 15 min; la bodega y el terreno operan en local, y los terminales de bodega trabajan contra la puerta de API local del WMS. |
| Túnel VPN de Talca durante la replicación | VM-02 retiene los cambios en su registro de escritura mientras DMS no puede leerlos. | DMS reanuda la réplica al reconectar; la copia en Aurora queda desactualizada durante el corte. |
| IdP maestro o enlace de identidad | La caché de solo lectura, de 24 h, conserva los datos de identidad recibidos, y el verificador local habilita los relevos de turno con el manifiesto firmado y el PIN personal. | La credencial de turno dura hasta 8 h en bodega y 14 h en terreno; no hay revocación remota mientras dure el corte; cuenta de último recurso (sección [4.4.15](14_m_decisiones_adr.md#sub:adr-15)). |
| Señal móvil en ruta | La aplicación opera contra el almacén local del dispositivo. | Sincroniza al reconectar dentro de los 10 min de la Tabla [4](#tab:t29). |
| ERP legado | El trabajador `erp-sync` retiene las operaciones en su cola SQS hasta 24 h y reintenta con la misma clave idempotente, de modo que un reintento no emite otro documento. | El camión no se libera sin guía confirmada o contingencia tributaria aprobada por el CLIENTE. |
| Perfil de API saturado | El balanceador reparte entre tareas y el escalado agrega tareas cuando los procesos PHP-FPM ocupados superan el 70 %. | Limitación de tasa en API Gateway con mensaje explícito al usuario. |
| Mensaje de reconciliación inválido o que falla | El consumidor rechaza el sobre de versión desconocida sin aplicarlo; tras cinco intentos pasa a la cola de mensajes fallidos. | Alarma inmediata y reproceso manual trazable; el grupo afectado no bloquea a los demás. |
| Excursión térmica sin enlace | El gateway bloquea el despacho en menos de 5 s en el borde. | Buffer de 24 h y alerta al reconectar. |
| SII, cadenas o notificaciones | Reintento con espera creciente y cola de mensajes fallidos. | Reproceso desde la cola al recuperarse el tercero. |
| Carga del peak de septiembre | Escalado automático e independiente de los perfiles de API y de trabajadores en Fargate, y de Aurora. | Limitación de tasa en API Gateway. |

Ninguna de estas fallas detiene la bodega ni el terreno. La peor de ellas, la pérdida de toda la región primaria, deja sin servicio a los portales y a la analítica hasta la promoción de la réplica, pero la preparación, el despacho y la entrega siguen operando contra sus bases locales y sus dispositivos, porque ninguna de esas transacciones depende de la nube para confirmarse.
