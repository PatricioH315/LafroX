# Revisión de incoherencias del Subdocumento 4 — 2026-10-03

Documento interno (no se entrega). Revisión conjunta: lectura completa de Claude (LAFROX-Subdocumento4.pdf, 162 pp.; LAFROX-Subdocumento4-Anexos.pdf, 93 pp.; LAFROX-Formulario-T-11.pdf, 31 pp.) y tres revisiones de GPT-6 Luna (esfuerzo alto) en paralelo: frente A = 4.1 y anexos lógicos, frente B = 4.2, 4.3, T-11 y 4-W, frente C = cumplimiento de bases y forma. Contraste con `Bases/` (caso, BTT, BA, aclaraciones, revisión del Informe 1) y con las decisiones D1–D30. Páginas = folio impreso. No se modificó ningún archivo del subdocumento ni ninguna figura.

Origen: **C** = Claude, **G** = GPT (ID de su informe), **C+G** = ambos.

## Críticas (pueden anular el subdocumento completo, aclaraciones §7.1)

| # | Ubicación | Problema | Origen |
|---|---|---|---|
| 1 | Cuerpo p. 162, Declaración de uso de IA | Dice «Revisión final no realizada», «la tabla no atribuye autoría exclusiva de IA a las láminas de Tomás», «conversión entre Markdown y LaTeX» y «La ausencia actual de esa revisión impide tratar este archivo de trabajo como una entrega final conforme». Son indicios literales de borrador (§7.1 d). | C+G (B-01, C-01) |
| 2 | Anexos pp. 90–93, Tablas A.34 y A.35 | Todas las filas dicen «No realizada»; la fuente dice «debe consolidarse … antes de presentar la oferta». A.35 usa títulos en minúscula y sin tildes sacados de nombres de archivo («decisiones del numeral 16 1 del caso», «implantacion progresiva del backend laravel») y desfasados respecto de la numeración real (p. ej. 4.1.3 = «principios de integracion»). | C+G (C-01, C-03) |
| 3 | Declaración IA (cuerpo y anexos) | Faltan filas para 4.2, 4.3, Anexo 4-W y Formulario T-11 (§7.2 exige una fila por sección y por anexo/formulario). El cuerpo anuncia «22 anexos», pero el catálogo A.1 declara 23 (4-A … 4-W). | C+G (B-02, C-02) |
| 4 | Réplica de analítica y geolocalización | 4.1.3.7 (p. 36), 4.2.3.2 (p. 89–90: «copia de los buckets de S3 salvo el de geolocalización»; «quedan fuera de la región secundaria»), 4.2.4.4.2 (p. 115: «excluidas de us-east-1 por diseño») y ADR-19 (Anexo 4-O) dicen que **no** se replican. 4.3.2.2 (p. 154), Tabla 37 (p. 156) y AL-DR-01 (Anexo 4-M) dicen que **sí** se copian de forma diferida con RPO ≤ 24 h. T-11 N-06: posiciones de flota «solo en sa-east-1». Es una contradicción de decisión de diseño/región (§7.1 c). | C |

## Altas

| # | Ubicación | Problema | Origen |
|---|---|---|---|
| 5 | 4.1.17.2 (p. 62), 4.2 intro (p. 67), Tabla 21 y texto (p. 125), ADR-17 | «La nueva guía se emite por cualquiera de los tres caminos de Talca **o Concepción**». `erp-sync`, la ACL y el ERP están solo en VM-04 de Talca; los sitios no se conectan entre sí. Si Talca queda aislado, los caminos de Concepción no llegan al ERP. | G (A-01), verificado |
| 6 | 4.1.1 (p. 13: «ADR fechados») vs Anexo 4-O | RT-02.04 exige un registro de ADR **fechado**; ninguna ficha ADR-01 … ADR-22 tiene fecha. | C |
| 7 | 4.2.3.4 (p. 90–91), Tabla 11 | RT-03.06 (obligatorio) exige etiquetado por ambiente, módulo y centro de costo; presupuestos con alertas; y un reporte mensual al CLIENTE. Solo se mencionan Savings Plans, Cost Explorer y Budgets; no hay etiquetado ni reporte. | G (C-04), verificado |
| 8 | 4.1.7 (p. 51: «el esfuerzo de migración exigido por RT-03.07») y 4.2.3.4 | RT-03.07 pide el esfuerzo estimado de migración y qué componentes son portables o no. Se afirma que se documenta, pero no hay estimación. | G (C-05), verificado |
| 9 | T-11 (servidor de Concepción, E-01 mini-PC); 4.3.1.4 Tabla 34 | RT-08.01 exige declarar el **consumo** de cada equipo de cómputo. Solo se declara para Talca; Concepción indica fuentes de 500 W y el mini-PC «fuentes DIN 24 VDC». La UPS de 3 kVA del gabinete de Concepción y las UPS de 1,5 kVA de los gabinetes de piso no tienen cálculo. | G (B-03) + C |
| 10 | Cola SQS de `erp-sync` | T-11 N-09 la trata como cola de **trabajos** («solicitudes de erp-sync»). Los Anexos 4-J, 4-M (AL-DTE-01) y 4-U dicen que viaja por shipper → **SQS FIFO**. La Tabla 13 dice que el shipper solo escribe en «su cola FIFO» (la de reconciliación, que consume el consumidor de Fargate) y que los trabajos son solo notificaciones y EDI. El cuerpo dice solo «SQS». No queda definido qué cola lee `erp-sync`. | C |
| 11 | Referencias a otros subdocumentos | Los supuestos S-28 y S-30–S-41 se declaran «registrados en el Subdocumento 3» (4.2.1.1, 4-W.1, 4-W.3, T-11). Según las aclaraciones, el listado de supuestos va en 2.5 / Subdocumento2-Anexos (o en 3.2). El BIA, los procedimientos manuales y «el plan de recuperación ante desastres del Subdocumento 11» (4.1.10) no calzan con el índice de 11, que solo pide el plan de pruebas de DR; además 4.2.4.6 dice que el DRP es «de esta sección». Si el destino no existe, es indicio §7.1 d. | C |

## Medias

| # | Ubicación | Problema | Origen |
|---|---|---|---|
| 12 | 4.1.3.1 (p. 20), 4.1.4.4 (p. 41) | Se cita «(RT-16.30)» sin «del caso». En las BTT, RT-16.30 es el registro de exportaciones sensibles; el portal es RT-16.30 **del caso**. Lo mismo pasa con RT-16.14 (BTT = motor de reglas; caso = firma/acuse) en algunas citas. | C |
| 13 | 4.1.3.7 (p. 34: «RT-12.01–12.06 y RT-12.09–12.12»); T-11 (RT-15.04) | Se dan por cubiertos RT-12.04 (FIDO2/claves de acceso para administradores) y RT-12.10 (baja efectiva ≤ 24 h), que no aparecen en el texto. RT-15.04 exige además la intensidad de carbono de la región de nube, que tampoco se declara. RT-09.04 pide declarar el tiempo de reacción del escalamiento, que no se declara (solo está incluido en «RT-09.01–08» del Anexo 4-T). | C |
| 14 | Figura 24, paso 4 (p. 102) | «La réplica reducida … recibe cada versión … **desde el ECR de sa-east-1**». Contradice 4.2.4.1.1 y D17 (ECR replica a us-east-1 «sin depender del registro primario»). **Solo reportar; no tocar la figura.** | C |
| 15 | Figura 19 (p. 92) | No muestra la réplica de ECR ni las colas SQS/SNS vacías de us-east-1 que describe el texto (D17). **Solo reportar.** | C |
| 16 | Anexo 4-N, Tabla A.15, fila INT-JOBS | «Trabajadores Laravel → erp-sync en VM-04». En el cuerpo, los trabajos Laravel corren en Fargate (N-04) y `erp-sync` es un perfil aparte en VM-04. | C |
| 17 | 4-W.5 (ventana dominical) y 4.2.6.6 | Talca cuenta 238 equipos = 132 de bodega + **los 106** de reparto, y Concepción solo sus 66 de bodega. Contradice SV-03 (camiones repartidos 2/3–1/3, que se usa para la sincronización: 43/21). Los 69 terminales de preventa no aparecen en ninguna ronda. | C |
| 18 | 4.2.6.3 (p. 129) vs 4-W.2 | El cuerpo presenta las 2.600 sesiones del portal como dato del caso («pertenecen a food service y cadenas (PUCV, 2026a, cap. 2, p. 4)»). La memoria dice que son un parámetro de diseño (2.100 + 500). | C |
| 19 | Figuras 3–13 (capas de 4.1.3) | Las figuras de capas 4.1.3 siguen siendo recortes (crops) de la vista general, que las aclaraciones §4 prohíben. Es un pendiente conocido; no se tocan las figuras. | C (pendiente previo) |

## Bajas

| # | Ubicación | Problema | Origen |
|---|---|---|---|
| 20 | Anexo 4-G (INT-03) | «260,000/22,14 × 5 = 58,710»: usa separador de miles en inglés, y con 22,14 el resultado da 58.717 (el 58.710 sale de 22,142857). | G (A-02) + C |
| 21 | Figuras 15 y 28 | Muestran un solo gateway IoT en Talca; el texto dice dos. Figura 29 y T-11: la bandeja del operador tiene solo ONT y router LTE, mientras el texto (p. 150) incluye el terminal Starlink. **Solo reportar.** | C |
| 22 | 4.1.3.2 vs 4.2 | «AWS WAF + Shield» frente a «Shield Advanced»: las aclaraciones exigen nombres idénticos. | C |
| 23 | 4.1.3.1 | Es el único título de capa sin «(Capa 1)»; 4.1.3.2 a 4.1.3.8 sí llevan el número. | C |
| 24 | Archivo de anexos, pp. 87–93 | El encabezado corrido dice «Anexo 4-W. Memoria de cálculo» en Referencias y en la Declaración de IA. En la referencia SII (s. f.-c), la URL partida queda antes del autor (p. 89). | C |
| 25 | 4.2.6.8 / 4-W.8 | «Con un nodo caído, Talca conserva … 1,92 TB útiles»: con un nodo caído quedan 4 NVMe y Ceph opera degradado con 2 réplicas. La frase es imprecisa. | C |

## Verificado sin incoherencias

- Índice y títulos obligatorios del capítulo 4 (aclaraciones §11); cierre con Referencias y Declaración de IA; índice de anexos (las páginas del catálogo A.1 calzan con el PDF).
- Cantidades 4.2.1.1 ↔ Fig. 18 ↔ 4.2.6.4 ↔ T-11 ↔ 4-W: 205 terminales de bodega (22 de congelado + 183 estándar), 69/106/31, 72 puntos de acceso, 7 módulos y 24 sondas, 4 gateways, reservas del 10 %, 380 equipos en MDM, 209 agentes EDR, 8 planes LTE, 20 túneles VPN.
- Tabla 9 (36 componentes; suma 37 por N-10) y listas 4.2.2.4–4.2.2.6.
- Mensajes: 178.661 / 260.155 por día (Tablas 26, A.10 y A.30), subtotales por grupo.
- VMs: Talca 14 vCPU / 23→25 GB / 210→221 GB / 136→359 IOPS; total 26 vCPU / 59→61 GB; Concepción 12 vCPU / 17→18 GB; utilizaciones porcentuales.
- Enlaces: Tabla 27 = A.31; drenajes de 1,68 / 1,09 / 0,27 GB → 1,87 / 1,21 / 0,30 Mbps.
- Electricidad y clima: 5.850 W + 20 % = 7.020 W; UPS 9,2 → 10 kVA; PUE 10,7/7,0 ≈ 1,5; generador 13,5 → 20 kVA; racks de 12U (R01 5,2/6,2 kW; R02 0,65/0,8 kW).
- Conmutación: 5 + 30 + 20 + 30 + 15 + 15 + 5 + 15 = 135 min ≤ 4 h. Tabla 16 = BA Art. 78.2. Tabla 17 = RT-05.10 del caso. Etapas = BA Art. 17.1. H3 en el mes 6 = Formulario E-25.
- Dotación 15/17 (42 h) y 17/19 (40 h); mesa de ayuda con 2.000 contactos y 7 agentes; cobertura 04:00–22:00 = RT-21.06 del caso.
- Sin precios ni tarifas de la oferta (GPT frente C).

## Decisiones y correcciones aplicadas el 2026-10-03

- **D31 Réplica.** La analítica se copia en diferido a us-east-1 (RPO ≤ 24 h), porque guarda los 5 años de temperatura y trazabilidad (RT-05.10). La geolocalización de personas y las posiciones de flota quedan solo en sa-east-1, con copia inmutable en otra cuenta de esa región; riesgo residual declarado. No se agrega ninguna región. Se aplicó en 4.1.3.7, 4.2.3.2, 4.2.4.4.2, 4.3.2.2, Tabla 37, AL-DR-01 y ADR-19.
- **D32 Nueva guía.** La emite el ERP de Talca por sus tres caminos; Concepción y los cross-docking necesitan además un camino propio. Sin camino hasta el ERP, rige D15. Se aplicó en 4.1.17.2, 4.2 intro, 4.2.5.4, ADR-17, 4-J, 4-M y 4-U.
- **D33 Colas del ERP.** Hay una SQS FIFO de solicitudes al ERP, leída solo por `erp-sync`, y una SQS FIFO de respuesta por sitio (Concepción y cada cross-docking) que lee el shipper. Las colas de trabajos quedan en 2 (notificaciones y EDI). Se aplicó en 4.1.3.5, M7, 4.1.7, 4.2.2 (N-09, A-04), Tabla 11, Tabla 13 e IAM, T-11 N-09, ADR-17, 4-J, 4-M y 4-U.
- **D34 ADR.** Se borró «fechados» de 4.1.1. RT-02.04 sigue sin fecha por decisión del usuario.
- **D35 FinOps (RT-03.06).** Se omite por ahora, por decisión del usuario.
- **D36 RT-03.07.** Se agregó en 4.2.3.4 un esfuerzo acotado en tres grupos: 4 servicios por configuración, 4 por adaptador y 5 por rediseño.
- **D37 Energía (RT-08.01).** Nueva tabla A.33 en 4-W.8: Concepción 2,16 kVA (UPS de 3 kVA, 72 %), gabinete de piso 0,88 kVA (1,5 kVA, 59 %), cross-docking 0,37 kVA (nueva UPS de 0,75 kVA, 49 %). El T-11 declara el consumo del servidor de Concepción (1.000 W de placa) y del mini-PC (45 W).
- **D38 Subdocumento 11.** Se eliminaron sus menciones (4.1.10 y Anexo 4-R), porque ese subdocumento no está hecho.
- **D39 Citas RT del caso.** Formato «RT-xx.yy del caso (PUCV, 2026a, cap. 15, p. 27)», con p. 26 para RT-03.13. Se agregaron RT-12.04 (FIDO2) y RT-12.10 (baja ≤ 24 h) en 4.1.3.7 y RT-09.04 (reacción < 3 min) en 4.2.6.9. Se quitó RT-15.04 del T-11; la intensidad de carbono sigue pendiente.
- **D40 Menores.**
  - Ventana dominical recalculada con calculo.py (SV-03 para reparto; preventa por red móvil): Talca 203 equipos, tandas de 18 y 12 domingos; Concepción 101 equipos, tandas de 9 y 12 domingos.
  - 2.600 sesiones del portal declaradas como parámetro de diseño.
  - Formato 58.710.
  - Fila INT-JOBS corregida a Fargate.
  - Nombre «AWS Shield Advanced».
  - Título «Capa de presentación (Capa 1)».
  - Frase de Ceph precisada.
  - Encabezados de Referencias e IA en los anexos.
