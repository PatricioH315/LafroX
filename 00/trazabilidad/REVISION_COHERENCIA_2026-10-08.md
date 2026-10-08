# Revisión exhaustiva del Subdocumento 4 — 2026-10-08

Registro interno (no se entrega). Sin cambios al subdocumento: todo queda para decisión o aprobación.

## Alcance y método

- **Claude:** lectura completa de los tres PDF compilados del commit `d397c30` (cuerpo 151 p., anexos 81 p., T-11 34 p.), contraste con `Bases/*.md`, con el Subdocumento 3 y el 1 (`../LafroX-rama-md`) y con `00/trazabilidad/DECISIONES_COHERENCIA.md`. Chequeos automáticos: cifras recalculadas a mano, capítulo y página de cada cita a las Bases Técnicas Transversales, letra mínima de texto vectorial, legibilidad de figuras, páginas semivacías.
- **ChatGPT (`gpt-6-sol`, esfuerzo alto, solo lectura):** cinco frentes en paralelo. A: 4.1 contra anexos 4-A a 4-V. B: 4.2 y 4.3 contra 4.1 y T-11. C: cifras y cálculo. D: cumplimiento formal. E: fidelidad a las Bases. 51 hallazgos; 44 válidos tras verificar. Descartado, entre otros: «ISO 27001/27002 sin cita en 4-R» (sí se citan en la fuente de la Tabla A.23).
- Nota: los espacios que la extracción de texto muestra pegados («BasesTécnicas», «sinWAN», «elWMS», «4-Vde») **no existen** en el PDF impreso; se verificó visualmente.

## Críticos (indicio de IA o incumplimiento obligatorio)

| # | Hallazgo | Dónde | Corrección propuesta |
|---|---|---|---|
| C1 | **Declaraciones de uso de IA.** Cuerpo: «Revisión final no realizada», «No realizada» en 22 filas, «láminas de Tomás», «conversión entre Markdown y LaTeX», «este archivo de trabajo … no se atribuye al equipo una verificación todavía no realizada», filas 4.2, 4.3, 4-W y T-11 con celdas vacías, niveles «No aplica» y «Alto en vistas asistidas» fuera de la escala. **Anexos: la declaración sigue incluida** (`04/anexos/logica/contenido.tex` → `17_declaracion_de_uso_de_ia`) con «debe consolidarse … antes de presentar la oferta» y la Tabla A.38 copiada de los nombres de archivo («especificaciones tecnologias de software a utilizar», «decisiones del numeral 16 1 del caso»). | `04/partes/cierre/declaracion_de_uso_de_ia.tex`; `04/anexos/logica/partes/17_declaracion_de_uso_de_ia.tex` | Una sola declaración al final del cuerpo, con una fila por sección (4.1, 4.1.1, 4.2, 4.2.1, 4.3, 4.3.1, 4.3.2), por anexo 4-A a 4-W y por T-11; herramienta, finalidad, nivel de la escala y revisor con nombre y qué verificó. Quitar `17_declaracion` del ensamblador de anexos. Necesita los nombres de revisores. |
| C2 | **Rastro del cambio de backend (Django → Laravel).** El Informe 1 evaluó un monolito Django; hoy el texto describe una «transición» desde un backend previo que no existe en el caso: «Sustituye el runtime por Laravel/PHP» (4.1.8); «mantener su runtime junto al nuevo» (4.1.7); «pruebas de paridad de contratos, datos y colas» (Tabla 5); título «Transición al backend Laravel» y «mensajes serializados por un framework de origen … Laravel no puede consumirlos» (4.2.4.1.3); «Implementación compatible del backend» y «Paridad de API» (4-P); «Angular se conserva … por sus componentes existentes» (4-P); «no se presume implementado en PHP por la elección del backend» (4-N). Revela versiones previas de la propuesta. | `09_implantacion_progresiva_del_backend_laravel.tex:6`; `08_detalle…:30`; `14_comparacion…:8`; `11_j_despliegue.tex:256–266`; `19_anexo_4_1_p…:38–48`; `15_anexo_4_1_n…:23` | Reescribir como plan de implantación del sistema nuevo frente al WMS 2013, sin «runtime», «paridad», «framework de origen» ni «se conserva». Título sugerido de 4.2.4.1.3: «Implantación por olas». Django queda solo como alternativa evaluada. |
| C3 | **AS2 fuera de la capa de borde (RT-11.07, obligatorio).** RT-11.07 y Art. 21.2 exigen publicar *todo* servicio por CDN + WAF + anti-DDoS L3/4/7. El canal AS2 entra por un NLB con TLS directo: sin CloudFront ni WAF (WAF no se asocia a NLB). | `02_c_conexiones.tex:67` (Tabla 19); `02_b_servicios_nube.tex` (Tabla 11); T-11 N-04 Transporte AS2; ADR-11 | Opción recomendada: CloudFront + WAF → ALB privado → OpenAS2 (la seguridad de AS2 es S/MIME y MDN, no requiere TLS directo). Alternativa: justificar formalmente la excepción (contrapartes registradas, lista de IP, Shield Advanced en NLB) asumiendo el riesgo. Decisión del equipo (cambia ADR-11). |

## Altos

| # | Hallazgo | Dónde | Corrección propuesta |
|---|---|---|---|
| A1 | **Guiones visibles «---» y «--».** Portada de los tres PDF («Sobre N.° 2 --- Oferta Técnica»), títulos de los 23 anexos («Anexo 4-R --- Controles…»), fichas INT de 4-G/4-H, títulos 4.2.6.3–4.2.6.7 («dimensiones 1--3») y 4-W.2–4-W.7. Causa: `\LFXsansmedio` y `\LFXsansfuerte` se declaran con `\newfontfamily` sin `Ligatures=TeX`. | `00/plantilla/formato-base/lafrox.cls:129–132` | Agregar `Ligatures=TeX` a ambas `\newfontfamily`. Una línea; corrige todo. |
| A2 | **Nombres de módulos distintos del Subdocumento 3.** SD3 fija «M7 Cobranza y rendición», «M8 Devoluciones y envases», «M9 Calidad y trazabilidad». SD4 usa «M7 Rendición» / «Rendición y cobro», «M8 Devoluciones», «M9 Calidad» / «Trazabilidad y frío», y variantes de M4 («Planificación de rutas», «Ruteo»), M6 («Reparto y entrega», «Entrega y POD») y M10 («Analítica y costo de servir»). | Tabla 8, Anexos 4-D, 4-E, 4-F, 4-N, títulos de 4.1.4 | Usar literalmente los doce nombres de SD3 en títulos, tablas y anexos. |
| A3 | **RF-10 sin representación.** RF-10.01–03 (sugerencia de reposición de compras por SKU y proveedor, E1, M2, traspaso al módulo de compras del ERP) no aparece en SD4; el Anexo 4-E traza RF-01 a 09, 11, 12 y 14 (faltan RF-10 y RF-13). Rompe el mapeo 100 % con SD3. | `05_anexo_4_1_d…`, `06_anexo_4_1_e…`, 4.1.4.3 (M2), INT-06 | Agregar la capacidad a M2 y a INT-06 (ACL hacia compras del ERP), y filas RF-10 y RF-13 en 4-E. |
| A4 | **Pérdida de la sala de Talca (abierto desde 10-07).** El procedimiento conecta los terminales «por VPN», pero firewalls, núcleo y túneles están en la sala perdida; erp-sync y la ACL «se reinstalan desde la misma imagen» sin destino; la guía nueva espera al ERP sin plazo, mientras la Tabla 16 la clasifica crítica con 4 h. | `06_e_sitio_secundario.tex:92`; `11_j_despliegue.tex:324–332` | Declarar un borde de red independiente de la sala (gabinete de comunicaciones fuera de ella o equipo de reposición) y el destino de VM-04; aclarar en la Tabla 16 que el plazo de 4 h excluye la pérdida del ERP del CLIENTE. |
| A5 | **Ansible «desde CD Talca» no tiene ruta.** El Transit Gateway une los sitios solo con la VPC de Producción y D4 eliminó la conexión Talca–Concepción. | `11_j_despliegue.tex:161`; F-02 en 4.2.2 y T-11 | Ejecutar Ansible desde la VPC de Producción (o Systems Manager) hacia cada sitio por su túnel. |
| A6 | **«Ningún sitio depende de otro» es absoluto.** La guía nueva de Concepción y los cross-docking requiere el ERP de Talca. | `02_c_conexiones.tex:15, 54`; `02_a_emplazamiento.tex:141` | Agregar «salvo la emisión de una guía nueva, que requiere el ERP de Talca». |
| A7 | **Gateway IoT de Concepción único, SPOF no declarado.** Talca tiene dos «para evitar un punto único de falla»; Concepción uno, que ejecuta el bloqueo térmico. | 4.1.3.2; Tabla 4; Tabla 20 | Declararlo en la Tabla 4 y la Tabla 20 (conducta segura y reposición desde la reserva de Talca) o agregar un segundo gateway. |
| A8 | **Figura 15 bajo 9 pt.** La vista general física imprime sus rótulos a ≈ 7,4 pt (medido contra una barra de referencia de 9 pt). Nube (Fig. 19) ≈ 9 pt; Talca (Fig. 25) ≈ 8,5–9 pt. | `figuras/fisica/Arquitectura_Fisica_General.png` | Rehacer en draw.io con letra mayor o dividir en dos láminas (no se toca la imagen sin pedido). |
| A9 | **T-11 sin índice.** La portada pasa directo al contenido; aclaraciones §9 exige índice paginado y enlazable en cada documento. | `04/formulario_T11.tex:39–46` | Insertar el índice tras la portada. |
| A10 | **Tablas del cuerpo de más de una página.** Tabla 3 (pp. 50–52), Tabla 20 (pp. 111–113), Tabla 33 (pp. 129–130); además se cortan 1, 4, 7, 8, 11, 13, 21, 22, 23, 27, 29, 30 y 37. | 4.1.11, 4.2.5.3, 4.2.6.13 | Dejar en el cuerpo una síntesis de una página (p. ej., Tabla 3 con los 8–10 ADR críticos) y el detalle en 4-O / 4-W. |
| A11 | **RT-14.08 (obligatorio): retención de trazas no declarada.** Se declaran registros (12 + 24 meses) y métricas (13 meses), no trazas ni su archivo. | 4.1.3.8; 4.1.7 | Declarar plazo de trazas en línea y archivo; el costo va a la Oferta Económica. |
| A12 | **Dotación de año 3.** El propio 4-W agrega un tercer agente sobre 2.200 contactos/mes; el año 3 tiene 2.258. La mesa pasa a 348 h-posición: 19 personas normales y 21 en peak (a 40 h), no 17/19. | `16_anexo_4b…:213–219`; Tabla 30; Tabla 33 dim. 16 | Separar dotación inicial y de año 3, o justificar por qué no se agrega el agente. |
| A13 | **Citas a las Bases sin página (≈ 25).** «conforme al Art. 16», «(Art. 17)», «RT-07.04 exige» (4.1.1); «numeral 2.3 de las Bases Técnicas Transversales» (4.1.2); «Artículo 16 de las Bases Administrativas» (4.1.13); «capítulo 6 del caso» (4.2.2); RT-02.11, RT-02.13, RT-02.14, RT-03.07, RT-03.10/12/13, RT-04.01/02, RT-09.05, RT-10.03/04, RT-11.16, RT-12.07–08, RT-16.10 en 4.1/4.2; 4-K «Art. 16.4»; 4-G «(caso, cap. 14)»; 4-M «RT-07.04»; 4-A «Bases, 1.6». | varios | Completar documento, capítulo/artículo y página. Los capítulos y páginas ya citados pasan el control automático (ninguna incoherencia RT ↔ capítulo). |

## Medios

| # | Hallazgo | Dónde |
|---|---|---|
| M1 | «La tabla siguiente detalla los medios…» introduce una lista, no una tabla. | `02_c_conexiones.tex:26` |
| M2 | «Los costos, el emplazamiento y la redundancia se comprueban en 4.2»: 4.2 no tiene costos. | `08_detalle…:30` |
| M3 | Frases que suenan a pendiente o a nota interna: «se deben comprobar en 4.2» (4.1.3.3); «El registro de supuestos del capítulo 3 debe conservar…» (4.1.20); catálogo de anexos: «Las referencias desde el cuerpo deben usar la letra del anexo» y «El identificador se conserva aunque cambie la paginación»; 4-W/4-P: «Fechas consultadas … el 07-10-2026» (posterior a la fecha de emisión 05-10-2026 de las portadas). | `04_capas…:117`; `21_decisiones…:4`; `00_catalogo_anexos.tex:4`; `19_anexo_4_1_p…:16` |
| M4 | QuickSight figura en 4.2.3, N-10 y T-11, pero no en 4.1.7 (Analítica/BI), M10 ni Fig. 1. | 4.1.7; 4.1.4.7 |
| M5 | El motor de optimización de rutas nunca se nombra (4.1.1 exige productos; T-11 dice «contenedor propio»). | `04_c_implementos.tex:79`; T-11 N-04 |
| M6 | SV-01…SV-07 se usan en 4.2.6 sin definirse en el cuerpo. | `12_k_dimensionamiento.tex` |
| M7 | Anexo 4-J: «M2 valida reserva y crédito»; el crédito lo valida M3 (fila de autoatención y 4.1.4.4). | `11_anexo_4_1_j…:8` |
| M8 | Decisiones 16.1 N° 6, 7 y 11 delegan al CLIENTE sin regla propuesta («Puelche define custodia», «Comercial decide», «Dueño del maestro»). | `13_anexo_4_1_l…:13–18` |
| M9 | Ancho de banda de Concepción sin tráfico de oficina: `calculo.py` asigna los 184 usuarios a Talca; el caso los sitúa en Talca y Concepción (cap. 2, p. 5). El supuesto de 5 MB/usuario-hora solo está en el script. | `calculo.py:165, 559–569`; Tabla 27 |
| M10 | Tamaño de tarea Fargate no declarado: «14 solicitudes/s por tarea» supone 1 vCPU. | 4-W.9; T-11 N-04 |
| M11 | Autonomía de UPS (30 min) y generador (24 h) sin cálculo de baterías ni combustible; consumos auxiliares (2,7 kW clima, 0,6 kW apoyo, 0,78 kW pérdidas) sin base declarada. UPS «modular N+1» sin tamaño de módulos. | 4.3.1.4; T-11 |
| M12 | 4-W.11: «Talca 333,73×, Concepción 166,87×» usa la CPU total de los nodos, no la de VM-01/VM-C01 (3 vCPU): ≈ 15,6× y 31,3×. | `16_anexo_4b…:296` |
| M13 | 3-2-1-1-0 en Concepción y cross-docking: Tabla 17 dice «reconstrucción desde el estado central»; no hay copia restaurable propia. | Tabla 17 |
| M14 | Preproducción: 4.1.9 dice que «se prueban los 186 terminales» y «la emisión de guía por el ERP»; 4.2.4 usa sitio emulado y ERP simulado (abierto #6). | `10_ambientes…:3` |
| M15 | «El cumplimiento de los estándares del Art. 4.3 … se acredita en la fila 5.23»: esa fila solo cubre ISO 27017/27018. | `05_d_sitio_principal.tex:24` |
| M16 | Mapa 4-F omite consumidores que 4-A declara (M10 y ACL de EntregaRegistrada, M10 de DevolucionRegistrada, M9 de DesviacionDeRuta). | `07_anexo_4_1_f…` |
| M17 | 4-N afirma que la Tabla 8 realiza físicamente los 37 identificadores transversales; la Tabla 8 solo tiene M1–M12 y capas (INT-OPT, SEC-SIEM, DEV-PIPE sin fila). | `15_anexo_4_1_n…:27`; `22_anexo_4_1_s…:19` |
| M18 | Anexo 4-C extiende «turno completo ≤ 10 min» a todo terreno; el caso lo fija para reparto. | `04_anexo_4_1_c…:10` |
| M19 | Anexo 4-P sin Proxmox, Ceph ni GitLab en el ciclo de soporte. | `19_anexo_4_1_p…` |
| M20 | Proveedor de notificaciones (SMS/WhatsApp/correo) no identificado. | T-11 dependencias; 4.2.3 |
| M21 | Páginas semivacías: cuerpo pp. 12 y 14 (antes de Figs. 1 y 2), 69 y 91; anexos p. 4 (solo la apertura); T-11 p. 34 con una línea. | — |
| M22 | Letra bajo 9 pt: Fig. 18 (TikZ) una línea a 8,9 pt; `\texttt` en tablas a 8,7 pt (Tablas 3, 13, 21, 39). Figs. 26 y 27 a ≈ 117 ppp (se pixelan al imprimir). | `02_a_emplazamiento.tex` (TikZ); `lafrox.cls:134` |
| M23 | Ubicación del servidor ERP en la sala de 25 m² y su formato 2U se presentan como hechos; son supuestos. | `05_d_sitio_principal.tex:49`; T-11 |
| M24 | T-11, dudas de ficha: MC9400 estándar con 5.000 mAh (la estándar es 7.000); TC58e 7.000 mAh es batería extendida opcional; «PAX A920 Pro» sin variante. Verificar en fichas oficiales. | T-11 C-02, C-03, terminal de pago |

## Bajos (redacción y forma)

- Comillas inglesas: «”modo offline”» (`11_patrones…:19`) y “…” en 4.3.1.4 (`05_d…:38`); el resto usa «».
- «sólo» con tilde en 8 lugares (4.2.6 y 4-W); el resto usa «solo».
- Fig. 14: «Fuente: elaboración propia de LafroX.» (las demás: «elaboración propia.»).
- «exigida por la Base» (4.1.14); «(ejemplo un nivel TIER» y «Para la disponibilidad y la redundancia la disponibilidad…» (4.3.1.4); «imponemos» (4.2.6.1); «Cap. 13» con mayúscula y paréntesis anidados (4.2.4.1.4); «§ 4.1.6» (4.1.3.5 y 4.1.4.1).
- «Tabla de ancho de banda de 4.2.6» → «Tabla 27» (`11_j_despliegue.tex:314`).
- «2,2 Mbps, un 15 % sobre el drenaje»: son 17,6 %; decir «al menos 15 %».
- RF-07.02 citado para dos funciones distintas en M7; RF-01 / RF-11 con formato distinto de RF-xx.yy.
- Tabla 35 trivial (dos filas con el mismo valor): puede ir en texto.
- «Desarrollo, QA y Preproducción se reducen o apagan» tres veces en la misma página (4.2.4.1); «datos sintéticos … cuya anonimización se verifica con Macie» es incongruente.
- APA: sufijos s. f.-a…e de AWS y SII no siguen el orden alfabético de títulos; «SII» sin expandir en la primera cita del cuerpo; AWS se expande como «[AWS]» y luego se escribe completo.
- Anexo 4-Q usa IDs abreviados («SHIPPER», «CDC»); los IDs de componentes «INT-BROKER», «INT-GIS»… comparten prefijo con las interfaces INT-01…15; la columna «Correspondencia 4.2.2» de la Tabla A.15 contiene criterios, no componentes.
- 4-W: la telemetría de Talca usa 10.920 ÷ 2 (incluye termógrafos); solo cambia en el redondeo.

## Fuera del Subdocumento 4 (avisar al equipo)

- SD1 (`01_presentacion_empresa/LAFROX-Subdocumento1.md:150`) presenta la División de Ingeniería como «Desarrollo Software (Python, Django, Móvil)» mientras la solución es Laravel/PHP. Con C2 resuelto, igual conviene alinear SD1 (agregar PHP/Laravel).

## Verificado sin diferencias

Mensajes 230.252 / 353.333 y sus quince subtotales; TPS 12,34 / 3,76–6,94 / 14,66 y el perfil horario; 21,99 TPS de prueba; terminales 207 → 235, 433 MDM, 217 EDR, 65 + 7 AP; racks 15U / 12U y posiciones; carga TI 7.450 → 8.940 W, UPS 15 kVA, PUE 1,5, generador 25 kVA (68 %); UPS de borde 3,42 / 0,88 / 0,42 kVA; Ceph 1,92 TB y utilizaciones; Aurora db.r6g.2xlarge y 111,70 sol/s; secuencia de 135 min; almacenamiento (50,75 / 87,72 / 0,58 / 3,20 / 32,11 GB); drenajes y Tabla 27; ventana dominical; Erlang 7 + 2 agentes y límite 2.283; 36 componentes 13 + 11 + 12 y la Tabla 9; CIDR sin solapes; solo sa-east-1 y us-east-1; sin componentes retirados ni subdocumentos posteriores; índice obligatorio 4.1 → 4.3.2 correcto; ningún título seguido de tabla, figura o lista; cada RT citado con capítulo coincide con su capítulo y página verificados; hechos del caso (sitios, flota 42 + 54 con 18 + 10 de frío, 184 de oficina, H2 mes 4, H3 mes 6, proyección a tres años con 7 instalaciones, planilla de 11 hojas, jubilación en 2 años, 68.000 canastillos, 2,3 %, retiro de 9 días).

## Recomendación de orden

1. C1, C2 y A1 (sin decisión de diseño, salvo los nombres de revisores).
2. A2, A3, A6, A9, A13 y M1–M7 (correcciones de texto).
3. Decisiones del equipo: C3 (AS2), A4 (sala de Talca), A5 (Ansible), A7 (gateway), A10 (tablas largas), A12 (dotación), M9–M13.
4. Figuras (el equipo las edita): A8, M22.
