# LafroX — plan de cierre de las 29 filas de categoría C

| ID | C1/C2 | Valor propuesto o dato faltante | Destino |
|---|---|---|---|
| RF-08.07 | C1 | Merma atribuible × costo contable del ERP; imputación directa a entrega, sin duplicar devoluciones | SD5 §5.1.11 |
| RF-14.03-BTT | C1 | Cinco nombres bajo `<dominio-del-cliente>`; VPN identificadas por sitio, región y túnel | SD4 §4.2.5.2, Tabla 19 |
| RF-19.03 | C1 | Mismo inventario DNS y VPN de RF-14.03-BTT | SD4 §4.2.5.2, Tabla 19 |
| RNF-21.01 | C1 | NOC propio en Sede Central de LafroX, Santiago; posición y relevos existentes | SD1 §1.1 |
| RNF-21.08 | C1 | 768 HH DES evolutivas/año; otras 768 HH DES/año correctivas | T-14 §2.8, cuenta 8.2 |
| RNF-23.01 | C2 | Cotización unitaria de todos los dispositivos especificados, accesorios y consumibles | T-11 Tabla 1: referencia sin cifras; Oferta Económica: valores |
| RNF-23.02 | C2 | IP y caída de variantes y conjuntos exactos; aplicabilidad para equipos fijos | T-11 Tabla 1 |
| RNF-23.04 | C2 | Marca y modelo de las ocho estaciones; controles se pueden extender ahora | T-11 Tabla 1, Estación de trabajo |
| RT-03.08 | C2 | Compromiso por hora, plazo, pago, cobertura y costo contractual del Savings Plan | SD4 §4.2.3.4: referencia; Oferta Económica: cifras |
| RT-04.13 | C2 | Costo realmente evitable de DEV/QA/PREPROD, costos residuales y excepciones | SD4 §4.2.3.4: método; Oferta Económica: ahorro |
| RT-06.04 | C1 | EN 12825:2001; ANSI/TIA-569-E:2019; ISO/IEC 11801-1:2017; ANSI/TIA-606-D:2021 | T-11 Tabla 1, Piso técnico y cableado; Distribución horizontal |
| RT-06.29 | C1 | Telefonía mediante cliente de software en los puestos y conexión de Internet ya dimensionada | SD4 §4.3.1.4 |
| RT-08.01 | C2 | Configuración completa de estaciones y CPU/interfaces exactas de E-01, con ficha de consumo | T-11 Tabla 1, Estación de trabajo y E-01 |
| RT-08.10 | C2 | Misma cotización que RNF-23.01; hardware de terreno comprado por CLIENTE | T-11 Tabla 1: referencia; Oferta Económica: valores |
| RT-08.11 | C2 | Evidencia ambiental y autonomía de cada modelo en su uso previsto | T-11 Tabla 1 |
| RT-08.12 | C2 | Misma matriz IP/caídas que RNF-23.02 | T-11 Tabla 1 |
| RT-11.13 | C1 | Mismos nombres, servicios, puertos y extremos VPN de RF-14.03-BTT | SD4 §4.2.5.2, Tabla 19 |
| RT-11.17 | C1 | SOC propio en Sede Central de LafroX, Santiago; un puesto desde mes 13 | SD4-Anexos §4-W.7 |
| RT-13.04 | C1 | Umbrales de diseño por los quince actores, con tareas acotadas y cálculo de pasos/tiempos | SD4 §4.1.3.1; tabla de indicadores de T-14 2.6.3 |
| RT-14.08 | C2 | Costos por señal y por almacenamiento en línea/archivo; trazas: propuesta de 30 días en línea | SD4 §4.1.3.8: política; Oferta Económica: desglose |
| RT-15.03 | C2 | Consumos atribuibles y factores publicados para estimación anual completa | SD4 §4.3.1.4 |
| RT-15.04 | C2 | Intensidad de sa-east-1 y tratamiento de us-east-1, año y método de atribución | SD4 §4.3.1.2 |
| RT-15.08 | C2 | Certificados personales vigentes, titular y dedicación efectiva | SD1 §1.5 |
| RT-16.24 | C2 | Proveedor, tarifa y reparto del volumen por CORREO/SMS/WHATSAPP/AVISO_EN_PORTAL | SD4-Anexos 4-H, INT-11; Oferta Económica |
| RT-17.07 | C2 | Consumo de batería medido o estimado con ensayo por modelo durante 14 h | SD4 §4.2.6.7 |
| RT-21.01 | C1 | Mismo NOC y procedimiento de RNF-21.01 | SD1 §1.1 |
| RT-21.03 | C2 | Nombres y dedicaciones de especialistas y relevos operativos por tecnología | SD1 §1.5 |
| RT-21.19 | C1 | Misma bolsa de 768 HH DES/año de RNF-21.08, sin sumar perfiles ni horas | T-14 §2.8, cuenta 8.2 |
| RT-23.01 | C2 | Misión, visión y valores aprobados; inventario de oficinas y direcciones | SD1 §1.1 |

## Alcance, fuentes y reglas de aplicación

Análisis del repositorio `C:\Users\alexa\Desktop\Universidad\FEP\LafroX\LafroX`, en sólo lectura, y de `items.md`. Se investigaron los 27 archivos `LAFROX-*.md` de las carpetas 01_–08_ y 13_, mediante búsquedas cruzadas de requisitos, cifras, personas, oficinas, equipos, costos, normas, autonomía y retenciones, y lectura de los pasajes pertinentes. Se contrastaron las cuatro Bases, `AGENTS.md` y `compct/CONTEXTO_SESION.md`. Los resúmenes e históricos no sustituyen los originales. Los archivos estaban recibiendo cambios concurrentes: este plan refleja el contenido consultado, sin atribuir esos cambios a esta tarea.

Para abreviar destinos y fuentes: SD1 = `01_presentacion_empresa/LAFROX-Subdocumento1.md`; T-6 está en esa misma carpeta. SD2/SD3/SD5/SD6/SD8/SD13 corresponden a `LAFROX-SubdocumentoN.md` y sus anexos dentro de `02_problema_necesidad/`, `03_esquema_solucion_alcance/`, `05_modelo_datos/`, `06_metodologías/`, `08_plan_riesgos/` y `13_innovaciones/`. SD4, SD4-Anexos y T-11 están en `04_arquitectura/`. SD7, sus anexos, T-14, T-15 y T-18 están en `07_PlanDeTrabajo_EDT_Cronograma_Implantación/`, con sus nombres `LAFROX-Subdocumento7*.md` y `LAFROX-Formulario-T-*.md`. BTT = `Bases/Bases_Tecnicas_Transversales.md`; BA = `Bases/Bases_Administrativas.md`; Caso = `Bases/Caso_02_Logistica.md`; Aclaraciones = `Bases/aclaraciones-licitacion.md`. Estas equivalencias identifican el archivo exacto de cada cita siguiente.

**C1 significa propuesta de diseño disponible, no hecho histórico acreditado ni prueba ejecutada.** Sus nuevas decisiones se expresan en futuro y se distinguen de cifras ya documentadas. **C2 significa que la frase completa sigue dependiendo de evidencia o información real.** Una fila mixta se clasifica C2 cuando su parte pendiente impide cerrarla; se indica la decisión que sí podemos tomar.

BA Art. 50.2 y Aclaraciones, consideraciones transversales, prohíben precios, tarifas y valores unitarios en la Oferta Técnica. BTT RT-08.10 pide costos unitarios de dispositivos, lo que crea una tensión documental expresa: se propone referencia técnica sin montos y detalle en la Oferta Económica; no afirmar que esa referencia por sí sola resuelve la interpretación del mandante. El mismo criterio rige Savings Plans, ahorros, observabilidad y canales. Las plantillas económicas de este plan se pegan exclusivamente en la Oferta Económica, aunque `items.md` indique inicialmente T-11 o SD4.

## 1. RF-08.07 — C1

**Fuente:** SD5 §5.1.11; SD5-Anexos 5-A, Tabla A.10 (`hech_actividad_costo`: `importe_costo`, `entrega_sk`, `cliente_sk`, `centro_costo`, `criterio_asignacion`, `importe_devoluciones`); 5-H, costo de servir. SD2-Anexos S-07 y SD3-Anexos 3.C S-07 reservan a Finanzas la validación metodológica. SD13 §13.1.5 valora pérdidas evitadas mediante unidades por costo unitario, sin doble conteo.

**Decisión y cálculo:** proponer como fuente el costo unitario contable del ERP vigente a la fecha del hecho, validado por Finanzas; importe = cantidad mermada × ese costo. No se afirma que su extracción ya esté implementada. Usar asignación directa `ENTREGA` sólo si existe vínculo documentado; la merma general permanece en su centro de costo y no se fuerza sobre un cliente. No hace falta crear `importe_merma` ni cambiar catálogos. La aprobación de Finanzas ya pertenece al alcance de S-07, no es una nueva instancia.

**Destino:** SD5 §5.1.11, al explicar el costo de servir.

**Frase:** «La merma se valorizará como cantidad mermada por costo unitario contable del ERP vigente al ocurrir el hecho y validado por Finanzas; cuando exista atribución documentada a una entrega y cliente se incorporará una sola vez en `importe_costo`, con criterio `ENTREGA` y su centro de costo, sin duplicar `importe_devoluciones`; la merma no atribuible permanecerá en su centro de costo».

## 2. RF-14.03-BTT — C1

**Fuente:** SD4 §4.2.5.2, Tabla 19: cinco clases de entrada y subdominio por entrada; §4.3.2: recuperación en us-east-1; T-11, D-01: dos túneles por cada uno de cinco sitios y región. BTT RT-11.13 exige inventario completo de nombres, puertos y servicios. El dominio del CLIENTE no está acreditado; `contacto@lafrox.cl` pertenece al proponente.

**Decisión:** usar nombres contractuales parametrizados, suficientes para el diseño: `portal.<dominio-del-cliente>`, `api.<dominio-del-cliente>`, `identidad.<dominio-del-cliente>`, `consolas.<dominio-del-cliente>` y `as2.<dominio-del-cliente>`. Portal y API conservan una misma clase de entrada CloudFront. Los mismos nombres se mantienen al recuperar, cambiando el destino, sin nuevos nombres `dr`. La VPN usa IP y no exige inventar DNS de AWS. Inventario lógico: {Talca, Concepción, Curicó, Chillán, Los Ángeles} × {sa-east-1, us-east-1} × {túnel 1, túnel 2} = **20 extremos AWS**, más sus contrapartes públicas D-01 por camino activo. Las IP asignadas se obtienen al provisionar; no son cifras pendientes que el equipo pueda conocer en una oferta ficticia sin infraestructura creada. Esta frase cierra la nomenclatura de diseño; el inventario operativo debe materializar las IP antes de habilitar exposición.

**Destino:** SD4 §4.2.5.2, inmediatamente después de Tabla 19; añadir los nombres a sus filas existentes.

**Frase:** «Las entradas serán `portal.<dominio-del-cliente>` y `api.<dominio-del-cliente>` por CloudFront HTTPS 443, `identidad.<dominio-del-cliente>` para OIDC HTTPS 443, `consolas.<dominio-del-cliente>` por Verified Access HTTPS 443 y `as2.<dominio-del-cliente>` por NLB TCP 443 con TLS 1.3; se conservarán al conmutar a us-east-1, y las VPN IPsec UDP 500/4500 se inventariarán por IP pública asignada, sitio, región y túnel, incluyendo los veinte extremos AWS y las contrapartes D-01, antes de habilitar cada conexión».

## 3. RF-19.03 — C1

**Fuente:** SD3-Anexos, catálogo RF-19.03 y remisión a RT-11.13; SD4 §4.2.5.2, Tabla 19; T-11 D-01; SD4 §4.3.2. Se aplica la misma nomenclatura parametrizada y el mismo cálculo de veinte extremos de la fila 2.

**Destino:** SD4 §4.2.5.2, Tabla 19. **Frase:** la frase de RF-14.03-BTT, íntegra. Es una sola inserción compartida, no tres inventarios diferentes; sus cinco nombres, puertos, recuperación y VPN sirven a las tres filas DNS de este plan. No afirmar que `<dominio-del-cliente>` ya sea un dominio registrado o que las IP operativas estén acreditadas.

## 4. RNF-21.01 — C1

**Fuente:** SD1 §1.1, NOC y escalamiento L1–L3; §1.2, Tabla 1.1: Sede Central de Santiago, 32 profesionales NOC y 12 SRE/Cloud en Centro de Operaciones; SD4-Anexos §4-W.7: puesto permanente y relevos; T-15 §5.7: asignación de la dotación. BA Art. 78.2 y BTT RT-21.01.

**Decisión:** ubicar el servicio propio en la Sede Central de LafroX, Santiago. Es una ubicación propuesta sobre una oficina declarada, no inferencia de dónde funciona hoy el Centro de Operaciones. Las Bases piden ubicación, sin exigir aquí dirección postal. No trasladar el domicilio Av. Brasil 2241 de Valparaíso a Santiago. Mantener un puesto NOC distinto del puesto SOC: 168 ÷ 42 = 4 relevos; techo(168 ÷ 40) = 5 desde 26-04-2028.

**Destino:** SD1 §1.1, viñeta Centro de Operaciones y Mesa de Servicios.

**Frase:** «Para Puelche, LafroX ubicará su NOC propio en la Sede Central de Santiago, con una posición permanente 24×7×365, cuatro relevos por puesto y cinco desde el 26-04-2028; aplicará vigilancia continua, registro y clasificación de alarmas, escalamiento L1–L3, entrega documentada de turno y comprobación de recuperación y cierre conforme a los procedimientos de continuidad».

## 5. RNF-21.08 — C1

**Fuente:** T-14 §2.8, cuenta 8.2, paquete 8.2.1; T-15 §4.2: 4.608 HH DES meses 21–56; §6.2: 72 actividades quincenales de 64 HH; SD6 §§6.1.4 y 6.2, control de cambios, pruebas y aceptación. T-18 §1 y SD4 Tabla 14 preservan congelamientos.

**Decisión y cálculo:** reservar 50 % de la capacidad combinada para evolución. 4.608 ÷ 36 × 12 = 1.536 HH DES/año; 1.536 × 0,5 = **768 evolutivas** y **768 correctivas**. Son 64 HH mensuales para cada uso, sin añadir dotación, HH de seguridad ni las 2.304 HH DES de deuda técnica de 8.2.4. La reserva es para cada período contractual de doce meses de Operación, no para cada año calendario. Su suficiencia se controla con la demanda; no se garantiza correctivo ilimitado a partir de esta división.

**Destino:** T-14 §2.8, cuenta 8.2, después de la fila 8.2.1.

**Frase:** «De las 4.608 HH DES de 8.2.1 se reservarán 768 HH DES de mantención evolutiva por cada doce meses de Operación y 768 HH DES anuales para correctivos; el CLIENTE solicitará el cambio, LafroX estimará su esfuerzo y saldo, el CLIENTE aprobará antes de ejecutarlo y la liquidación registrará las HH efectivas y el saldo de la bolsa, respetando las ventanas de despliegue».

## 6. RNF-23.01 — C2

**Fuente:** T-11 Tabla 1, dispositivos de terreno y operación; SD4 §4.2.1.2; SD6 §6.1.3; Caso cap. 10, compra de terreno por CLIENTE; BTT RT-08.10 y BA Art. 50.2. La búsqueda transversal, incluido T-6, no aporta cotizaciones: montos de contratos históricos no son precios de equipos.

**Dato y obtención:** cotización comercial fechada del distribuidor/fabricante para EC55, TC58e, MC9400 estándar y Freezer, ZQ620 Plus, PAX A920 Pro, ZT411, conjunto Dibal BEV/ME/DMI-610, módulo Ebyte, sondas PT100 y CX450; incluir gateway Moxa de B-02 si integra la compra de sensores. Moneda, impuestos, accesorios y consumibles deben estar separados o claramente incluidos. No mezclar módulo, sonda y caja como si fueran la misma unidad facturable. Cantidades y reservas ya existen en T-11.

**Destino y plantillas:** en T-11, sin precios: «Las estimaciones unitarias fechadas por dispositivo, accesorios y consumibles se individualizan en la Oferta Económica; el CLIENTE adquiere el hardware de terreno según las cantidades de esta tabla». En Oferta Económica, una entrada por unidad facturable: «Para [DATO: modelo y unidad de compra], el costo unitario estimado es [DATO: importe y moneda], según [DATO: proveedor/cotización/fecha], con [DATO: impuestos, accesorios y consumibles incluidos o separados]». La tensión RT-08.10/Art. 50.2 queda expresamente pendiente de interpretación formal, sin insertar cifras en el Sobre 2.

## 7. RNF-23.02 — C2

**Fuente:** T-11 Tabla 1; SD4 §4.2.1.2; BTT RT-08.12. Ya se declaran EC55 IP67, TC58e IP65/68, Freezer IP65/68 y caída de 3 m, ZQ620 Plus IP54 y caja Ebyte IP65; son declaraciones de la propuesta, no fichas incorporadas.

**Dato y obtención:** fichas oficiales de la variante exacta para IP de MC9400 estándar, ZT411, A920 Pro, conjunto de balanza/indicador y CX450, y caídas de los modelos salvo Freezer. Comprobar también alcance del IP de módulo, sonda, caja y ensamblaje. Fabricante o integrador de cada conjunto debe indicar superficie, temperatura, accesorios y condiciones del ensayo; para equipos fijos, instalación protegida y justificación documentada de qué requisito de caída aplica. «No aplica» sin fundamento no cierra la fila.

**Destino:** T-11 Tabla 1, característica de cada dispositivo.

**Plantilla por modelo:** «[DATO: modelo y variante] tendrá protección [DATO: IP y alcance del conjunto] y resistencia a caída [DATO: altura, superficie y condiciones, o condición aplicable documentada para instalación fija], según [DATO: ficha oficial, versión y apartado], en el emplazamiento previsto en esta tabla». Si resulta incompatible y exige sustitución, deja de ser cierre C y debe revisarse como D.

## 8. RNF-23.04 — C2

**Fuente:** T-11 Tabla 1, Estación de trabajo: ocho nuevas (5 Talca, 3 Concepción), dos monitores de 24 pulgadas, ergonomía NCh 2527; controles descritos para las 184 existentes. F-03 ya cuenta **192 estaciones**: extender los controles no suma licencias de estaciones a ese inventario. SD4 §4.2.5, acceso Verified Access.

**Dato y obtención:** marca/modelo seleccionado para las ocho PC, de ficha y cotización del proveedor de cómputo. Compartido con RT-08.01; no puede derivarse de los HPE de servidor o de los Zebra. La extensión de gestión, actualización y cifrado es decisión C1, pero el modelo sigue siendo C2.

**Destino:** T-11 Tabla 1, Estación de trabajo.

**Plantilla:** «Las ocho estaciones [DATO: marca y modelo], cinco en Talca y tres en Concepción, tendrán dos monitores de 24 pulgadas, ergonomía NCh 2527, gestión centralizada, actualización automatizada, cifrado de disco y CrowdStrike Falcon, bajo la misma postura que las 184 estaciones existentes para habilitar Verified Access».

## 9. RT-03.08 — C2

**Fuente:** SD4 §4.2.3.4: Savings Plans para base y peak efímero, montos sólo en Oferta Económica; SD4-Anexos 4-P y 4-W.9, servicios y tareas base. BTT RT-03.08; BA Art. 50.2. No se encontró importe ni partida económica valorizada en los 27 archivos.

**Dato y obtención:** simulación/cotización de AWS con compromiso monetario por hora, tipo de plan, plazo, forma de pago, región/cargas elegibles y subtotal para el período contractual. Responsable financiero y de nube; herramienta comercial de AWS y propuesta económica. No presumir que Aurora, almacenamiento y todos los servicios estén cubiertos por el mismo Savings Plan de cómputo.

**Decisión disponible:** comprometer sólo consumo mínimo permanente elegible; excluir peak y capacidad que se apaga por S-43.

**Destino y plantillas:** SD4 §4.2.3.4: «El compromiso Savings Plans cubrirá exclusivamente el consumo base permanente elegible, excluyendo la capacidad de peak y la apagable, con condiciones y valorización en la partida [DATO: identificador] de la Oferta Económica». Oferta Económica: «El plan [DATO: tipo] compromete [DATO: importe/moneda por hora] durante [DATO: plazo], con pago [DATO: modalidad], para [DATO: cargas elegibles], y costo contractual [DATO: subtotal y moneda]».

## 10. RT-04.13 — C2

**Fuente:** SD4 §4.2.3.4 y SD3-Anexos 3.C S-43: L–V 08:00–20:00; 60 h de 168, meta mínima 60 % de reducción de horas; activaciones excepcionales y críticas. BTT RT-04.13 y BA Art. 50.2.

**Cálculo disponible:** 168 − 60 = **108 h semanales**, 108 ÷ 168 = **64,2857 % potencial de horas**. Para cada ambiente, ahorro semanal = (108 − horas excepcionales equivalentes) × costo horario evitable; usar calendario real para anualizar. Restar del ahorro cualquier costo adicional de arranque; conservar almacenamiento, servicios permanentes y pagos comprometidos. No volver a restar un residual que ya se excluyó del costo evitable.

**Dato y obtención:** costos horarios evitables reales de cada ambiente y costo residual mensual, del presupuesto regional AWS, exportación de estimador o FinOps, con descuentos y compromisos; previsión de excepciones acordada con CLIENTE. Los archivos no permiten obtener dinero a partir de porcentajes de horas.

**Destino y plantillas:** SD4 §4.2.3.4: «La valorización comparará operación continua y horario S-43 con 108 horas semanales potencialmente evitables, descontando activaciones excepcionales y conservando costos residuales y compromisos; el ahorro se declara en [DATO: partida económica]». Oferta Económica: «El ahorro anual de DEV/QA/PREPROD es [DATO: importe y moneda], calculado con [DATO: horas evitadas por ambiente], [DATO: costos horarios evitables], [DATO: excepciones y costos adicionales] y costos residuales [DATO: desglose], frente al escenario continuo».

## 11. RT-06.04 — C1

**Fuente local:** T-11 Tabla 1, Piso técnico y cableado y Distribución horizontal: piso, Cat6A, OM4, 10 GbE y certificación de enlaces; SD4 §4.3.1.4; T-14 cuentas 2.3 y 6.1; BTT RT-06.04. No hay ediciones específicas en la propuesta: se seleccionan como decisión de diseño, sin afirmar instalación ya certificada.

**Fundamento externo verificado:** [BSI, EN 12825:2001, piso técnico](https://knowledge.bsigroup.com/products/raised-access-floors); [TIA-569, versión E de 2019, canalizaciones y espacios](https://tiaonline.org/standard/tia-569/); [ISO/IEC 11801-1:2017, requisitos generales de cableado](https://www.iso.org/standard/66182.html); [catálogo del TIA Fiber Optics Tech Consortium, ANSI/TIA-606-D de 2021, administración](https://www.tiafotc.org/wp-content/uploads/2023/06/List-of-Current-TIA-Standards-Revisions-6-12-2023.pdf). Se fijan esas ediciones como referencias contractuales concretas; no se afirma que todas sean las últimas revisiones disponibles. No crean obligación de adoptar una nueva topología ni sustituyen requisitos locales de seguridad.

**Destino:** T-11 Tabla 1, ambas filas indicadas; una nota común evita repetición.

**Frase:** «El piso técnico se especificará conforme a EN 12825:2001, las canalizaciones a ANSI/TIA-569-E:2019, el cableado Cat6A y OM4 a ISO/IEC 11801-1:2017 y su identificación y etiquetado a ANSI/TIA-606-D:2021; se entregarán planos, identificadores coincidentes en ambos extremos y documentación de certificación de cada enlace para 10 GbE».

## 12. RT-06.29 — C1

**Fuente:** SD4 §4.3.1.4, zona de trabajo en línea técnica; §4.2.5, Tabla 18, acceso de oficinas mediante Internet; T-11, D-03/D-04/D-06 y estaciones; SD1 §1.1, mesa y escalamiento; BTT RT-06.29 exige habilitar telefonía e Internet.

**Decisión:** LafroX habilita telefonía mediante cliente de software en los puestos operativos, usando la conectividad existente. Es compromiso de provisión, no afirmación de una central telefónica ya instalada en Puelche. No elegir aquí operador, marca, nueva central PBX, ocho líneas públicas independientes ni red adicional; su costo se contempla en la habilitación económica correspondiente. No implica cambiar dotación u horarios de mesa.

**Destino:** SD4 §4.3.1.4, párrafo de zona de trabajo.

**Frase:** «LafroX habilitará en los puestos de operación y administración telefonía mediante cliente de software para llamadas entrantes y salientes, con audio adecuado, y acceso a Internet por los enlaces y caminos de respaldo ya previstos para cada sitio, con su provisión incluida en la habilitación de los puestos».

## 13. RT-08.01 — C2

**Fuente:** T-11 Tabla 1, E-01 y Estación de trabajo; SD4 §§4.2.6.8 y 4.3.1.4; SD4-Anexos 4-W.8, Tabla A.35. E-01 declara i5/i7, 16 GB, dos SSD de 512 GB RAID 1 y máximo 45 W. A 3× necesita 3 vCPU, 5 GB y 50 GB. No hay CPU exacta ni configuración completa de PC.

**Dato y obtención:** configuración/SKU y ficha oficial de las ocho estaciones (CPU exacta, RAM, disco, interfaces y máximo eléctrico; eficiencia energética) y del ARK-2250 o equivalente seleccionado (CPU exacta, interfaces y máximo del conjunto configurado). Cotización de fabricante/integrador y hoja técnica. El consumo de la CPU o de una fuente no demuestra el máximo del equipo.

**Destino:** T-11 Tabla 1, dos filas. **Plantillas:** «Las ocho estaciones serán [DATO: marca/modelo/SKU], con [DATO: CPU exacta], [DATO: RAM], [DATO: disco], [DATO: interfaces] y consumo máximo de [DATO: W y ficha], para consolas web, telefonía y dos monitores de 24 pulgadas». «E-01 usará [DATO: marca/modelo/SKU y CPU exacta], 16 GB, dos SSD industriales de 512 GB en RAID 1, [DATO: interfaces] y máximo de [DATO: W verificados], conforme a [DATO: ficha y configuración]».

**Control:** 16 ≥ 5 GB y 512 ≥ 50 GB verifican memoria/disco; falta comprobar equivalencia de CPU y consumo ≤45 W para conservar Tabla A.35. Si supera esa cota o no admite la alimentación redundante declarada, el cierre requiere revisar diseño, no ocultarlo con una frase.

## 14. RT-08.10 — C2

**Fuente:** T-11 Tabla 1; SD6 §6.1.3; Caso cap. 10; BTT RT-08.10; BA Art. 50.2. **Dato y obtención:** exactamente la cotización por unidad facturable de RNF-23.01, de proveedores reales para los modelos y variantes existentes; no una segunda lista de precios ni precios inferidos de contratos de T-6.

**Destino:** T-11 Tabla 1 para la referencia sin cifras; Oferta Económica para el detalle. **Plantilla técnica:** «El CLIENTE adquirirá los dispositivos de terreno, accesorios y consumibles de esta tabla; sus estimaciones comerciales por unidad facturable se detallan en la Oferta Económica». **Plantilla económica:** «[DATO: modelo y unidad facturable]: [DATO: precio unitario y moneda], referencia [DATO: proveedor y fecha], [DATO: impuestos, accesorios y consumibles]». Reutilizar la ficha económica de RNF-23.01 y preservar sus cantidades. Sigue la tensión normativa ya señalada; no cambiar el responsable de compra para intentar resolverla.

## 15. RT-08.11 — C2

**Fuente:** T-11 Tabla 1; SD4 §4.2.1.2; Caso RT-03.10 (14 h de terreno) y RT-13.08; SD3 supuestos S-33–S-39 y T-18 pruebas de terreno. Existen asignaciones por entorno: MC9400 Freezer entra a −22 °C; estándar atiende seco, refrigerado sobre 0 °C y cross-docking; TC58e atiende reparto. Su mínimo declarado −20 °C no implica por sí solo incumplimiento de una cámara a la que no está asignado.

**Dato y obtención:** matriz de uso/ficha oficial por variante: humedad y condensación, polvo/agua, vibración, temperatura, luminosidad, guantes, una mano cuando aplica, y autonomía por turno con baterías/accesorios previstos. Fabricantes e integrador, completados con prueba representativa de LafroX para autonomía real; la batería de repuesto Freezer ya está prevista. No exigir 14 h de batería individual a un sensor alimentado por fuente, ni confundir continuidad local de bodega 24 h con una sola batería.

**Destino:** T-11 Tabla 1. **Plantilla por uso:** «[DATO: modelo/variante] se utilizará en [DATO: entorno asignado], con aptitud acreditada para [DATO: rangos y condiciones pertinentes] y autonomía de [DATO: horas/recambios y ensayo de turno], según [DATO: ficha/versión y evidencia]; el ingreso a congelado se reserva al MC9400 Cold Storage Freezer». Si hay que usar TC58e dentro de cámara o una ficha no cubre el uso real, revisar como D.

## 16. RT-08.12 — C2

**Fuente:** T-11 Tabla 1 y SD4 §4.2.1.2; BTT RT-08.12. **Dato y obtención:** la misma matriz de fichas IP/caídas de RNF-23.02. Preservar variantes, ensayos, protección de conjuntos e instalación de equipos fijos; no extrapolar caída de 3 m del Freezer al estándar, EC55, TC58e o impresora.

**Destino:** T-11 Tabla 1, cada fila pertinente. **Plantilla:** «[DATO: modelo/variante o conjunto completo] declara [DATO: IP y alcance] y [DATO: resistencia a caídas y condiciones, o justificación de aplicación en instalación fija], acreditados por [DATO: ficha oficial y apartado], coherentes con [DATO: uso previsto]». La misma inserción por modelo cubre RNF-23.02 y RT-08.12; no se requieren dos anexos ni una promesa genérica de robustez.

## 17. RT-11.13 — C1

**Fuente:** SD4 §4.2.5.2, Tabla 19; T-11 D-01; SD4 §4.3.2; BTT RT-11.13. **Decisión y cálculo:** los cinco nombres parametrizados y 5 sitios × 2 regiones × 2 túneles = 20 extremos AWS de RF-14.03-BTT, con IP de sus contrapartes D-01 materializadas al provisionar. Conservar los mismos nombres en recuperación evita nuevos certificados y nombres innecesarios; las dependencias salientes de T-11 no se convierten en nuevas entradas.

**Destino:** SD4 §4.2.5.2, Tabla 19. **Frase:** pegar una sola vez la frase íntegra de RF-14.03-BTT. Cierra el diseño declarado, sin fingir FQDN registrados, IP contratadas o comprobación de exposición ejecutada.

## 18. RT-11.17 — C1

**Fuente:** SD1 §1.2, Tabla 1.1: seguridad en Sede Central de Santiago; SD4-Anexos §4-W.7 y 4-R, Tabla A.23; T-14 8.1.5: puesto SOC desde mes 13; T-15 §§4.1 y 5.7: cuatro/cinco relevos, contratación o subcontratación dentro de las HH existentes. SD6 §6.1.3 presenta subcontratación como condicional, no obligatoria.

**Decisión:** SOC propio en Sede Central de Santiago. El personal de refuerzo ya previsto se contrata dentro de SEG; no atribuir todos los relevos a las siete personas de planta ni compartir el único puesto con NOC. 168/42 = 4; techo(168/40) = 5. La elección no cambia horas ni fechas. En aplicación futura, la referencia condicional de SD6 puede conservarse como alternativa, sin decir que existe subcontrato efectivo.

**Destino:** SD4-Anexos §4-W.7, junto a cobertura NOC/SOC.

**Frase:** «El SOC será propio de LafroX y se ubicará en su Sede Central de Santiago, con una posición permanente 24×7 desde el mes 13, cuatro relevos y cinco desde el 26-04-2028 dentro de la dotación prevista; registrará y clasificará hallazgos del SIEM, escalará a Seguridad, ejecutará la contención autorizada y documentará recuperación, relevo y cierre conforme al Anexo 4-R».

## 19. RT-13.04 — C1

**Fuente:** SD4 §4.1.3.1, interfaces y capacidades; SD3-Anexos 3.I, Tabla 3.A.12a: quince actores; 3.B RNF-05.03: aprendizaje ≤2 h y error ≤5 % en misión de al menos veinte líneas. T-14 2.6.3 compromete cuatro indicadores por transacción y prueba en 3.8.2; T-15 asigna 240 HH a 2.6.3; T-18 §§2.2 y 3.2 ya contienen pruebas. No hay umbrales humanos completos: los siguientes son decisiones de diseño, no resultados medidos.

**Propuesta acotada:** medir tareas de interfaz con sesión iniciada e insumos de negocio disponibles, incluyendo interacción humana y respuesta del sistema; declarar separadamente lo que no forma parte de esa transacción (traslado físico, conducción, resolución sanitaria o adquisición de una aprobación de otro rol). Un paso es una acción intencional: selección, lectura, captura o confirmación. El presupuesto ordinario propuesto es hasta 30 s por paso; confirmar una línea utiliza hasta 10 s por paso. No convertir p95 de API en duración humana. La tabla compromete una transacción representativa por cada perfil existente, sin crear actores.

| Perfil(s) del catálogo | Transacción crítica acotada | Pasos máximos y fundamento propuesto | Tiempo total máximo | Error tolerado | Aprendizaje máximo |
|---|---|---|---|---|---|
| Preventista | Registrar pedido de veinte líneas | Abrir cliente + abrir pedido + 2 acciones/línea + revisar + confirmar = 44 | 44 × 30 s = 22 min | ≤1 línea incorrecta/20 | 2 h |
| Conductor propio; conductor externo | Registrar entrega con POD, envases y cobro ya obtenido | Abrir parada, entrega, evidencia, receptor, envases, medio de cobro, importe, confirmar = 8 | 8 × 30 s = 4 min | ≤1 transacción con error/20 | 2 h |
| Preparador | Confirmar una línea disponible de misión | Ubicación, SKU/lote, cantidad = 3 | 3 × 10 s = 30 s | ≤1 línea con error/20 en la misión | 2 h |
| Cliente tradicional; cliente moderno | Consultar estado/documento/saldo | Abrir consulta, seleccionar registro, mostrar resultado = 3 | 3 × 30 s = 90 s | ≤1 consulta equivocada/20 | 2 h |
| Empresa transportista | Confirmar asignación disponible de conductor/vehículo | Abrir ruta, conductor, vehículo, revisar, confirmar = 5 | 5 × 30 s = 150 s | ≤1 asignación con error/20 | 2 h |
| Proveedor | Consultar orden y recepción vinculada | Abrir órdenes, seleccionar, consultar recepción = 3 | 3 × 30 s = 90 s | ≤1 consulta equivocada/20 | 2 h |
| Jefa de Calidad | Registrar decisión ya evaluada sobre lote | Abrir alerta, lote, evidencia, decisión, motivo, confirmar = 6 | 6 × 30 s = 3 min | ≤1 registro corregible/20; 0 liberaciones indebidas | 2 h |
| Gerente Comercial | Registrar excepción comercial ya evaluada | Abrir caso, datos, decisión, motivo, revisar, confirmar = 6 | 6 × 30 s = 3 min | ≤1 registro corregible/20 | 2 h |
| Gerente de Finanzas | Aprobar rendición conciliada disponible | Abrir rendición, importes, evidencias, decisión, motivo, confirmar = 6 | 6 × 30 s = 3 min | ≤1 registro corregible/20; 0 importes indebidos aprobados | 2 h |
| Planificador de Rutas | Generar y aprobar plan sin excepción externa | Parámetros, generar, revisar, corregir, verificar, aprobar = 6 | 6 × 30 s + 20 min del cálculo máximo previsto = 23 min | ≤1 ajuste de captura/20 planes; 0 planes incompatibles aprobados | 2 h |
| Jefe de TI | Revocar acceso de una cuenta identificada | Abrir cuentas, seleccionar, acción, motivo, confirmar = 5 | 5 × 30 s = 150 s | ≤1 registro corregible/20; 0 revocaciones de otra cuenta | 2 h |
| Gerente de Operaciones | Registrar decisión operacional ya evaluada | Abrir excepción, datos, acción, motivo, revisar, confirmar = 6 | 6 × 30 s = 3 min | ≤1 registro corregible/20 | 2 h |
| Jefa de Bodega | Confirmar ajuste de inventario ya autorizado | Abrir caso, cantidad, causa, evidencia, revisar, confirmar = 6 | 6 × 30 s = 3 min | ≤1 registro corregible/20; 0 ajustes no autorizados | 2 h |

**Cálculo y control:** 1/20 = 5 %; 0/20 = 0 %. Las tareas y presupuestos por paso son hipótesis de diseño explícitas; los 2 h se adoptan como objetivo común a partir del perfil operacional de mayor rotación ya exigido, sin afirmar capacitación de dominio profesional en 2 h. El aprendizaje mide el flujo de interfaz del perfil. El preparador además conserva la misión mínima de veinte líneas y materiales de hasta dos páginas de RNF-05.03. Para rutas, SD4 exige corrida menor de veinte minutos: el presupuesto de 23 min incluye su ejecución y las seis acciones, manteniendo ese requisito más estricto del motor. Ningún valor relaja límites de respuesta de sistema existentes.

**Destino:** insertar la tabla en SD4 §4.1.3.1 como indicadores comprometidos; T-14 2.6.3 y la prueba existente la usan por referencia, sin sumar HH.

**Frase:** «LafroX compromete para cada perfil los tiempos humanos totales, pasos, error tolerado y aprendizaje de la tabla de indicadores, medidos con sesión iniciada e insumos disponibles; los verificará en los prototipos y pruebas de aceptación ya previstos, conservando para preparación el aprendizaje máximo de dos horas y hasta una línea con error en una misión de veinte líneas». Este cierre requiere esa pequeña tabla además de la frase: un máximo universal sin especificar tareas no cubriría el requisito.

## 20. RT-14.08 — C2

**Fuente:** SD4 §4.1.3.8; §4.1.3.7; SD4-Anexos ADR-14 y T-11 F-01: logs 12 meses en línea +24 en archivo, métricas 13 meses, buffer de sitio 24 h, auditoría de seguridad 7 años. No se encontró desglose monetario ni retención numérica de trazas. SD8 R8-24 limita exposición de telemetría; SD13 INN-02 no convierte reproducción de incidencias en conservación ilimitada de trazas.

**Decisión disponible:** proponer trazas técnicas **30 días en línea, sin archivo general**; las evidencias de incidentes/auditoría conservan su política específica existente. Es plazo de diseño propuesto, no atribución de una capacidad gratuita de AWS. Debe comprobarse su implementación en el servicio/configuración elegido.

**Dato y obtención:** presupuesto regional del proveedor para ingesta, métricas, consultas, trazas, logs en línea y archivo, con volumen por mes, muestreo, compresión y tarifa; exportación del estimador AWS/FinOps y decisión técnica de almacenamiento. Buffer 24 h no determina volumen mensual; las cifras de tráfico de integración no equivalen automáticamente a ingesta facturable.

**Destino y plantillas:** SD4 §4.1.3.8: «Los logs técnicos conservarán 12 meses en línea y 24 adicionales archivados, las métricas 13 meses y las trazas técnicas 30 días en línea sin archivo general; la auditoría de seguridad conservará siete años y el costo de cada señal, ingesta y almacenamiento se desglosa en [DATO: partida económica]». Oferta Económica: «El costo de [DATO: señal/rubro] es [DATO: importe/moneda por mes y año], para [DATO: volumen y muestreo], desglosado en ingesta [DATO], línea [DATO], archivo [DATO] y consulta [DATO], según [DATO: región, tarifa y fecha]».

## 21. RT-15.03 — C2

**Fuente:** SD4 §4.3.1.4, carga total Talca ≈13,5 kW y PUE ≈1,5; SD4-Anexos 4-W.8, Tabla A.35, cotas de borde; T-14 8.4.3 y T-15 §4.2: tres informes futuros, 288 HH SRE; SD4 §4.2.3.4 y S-43, horas no productivas. Los informes futuros no son estimación inicial ni factores publicados.

**Cálculo disponible:** cota continua Talca = 13,5 ×24 ×365 = **118.260 kWh/año**. Si F es kgCO₂e/kWh, su componente = 118.260 × F ÷1.000 tCO₂e/año. No multiplicar esta energía total nuevamente por PUE. Las potencias de placa de otros sitios son cotas para UPS, no consumos medidos; nube no expone aquí energía atribuible por servicio. Una cifra completa requiere considerar nube primaria y DR, sitios, puestos, dispositivos y combustible atribuible al generador, sin contar dos veces energía ya incluida.

**Dato y obtención:** consumos anuales atribuibles o estimaciones por carga/horas de todos los componentes; factor eléctrico publicado con territorio/año, factor de combustible y consumo supuesto; reporte/calculadora de carbono de la cuenta AWS o información oficial de atribución. Responsable SRE y sostenibilidad/finanzas del equipo; estadísticas oficiales de energía, fichas y reportes del proveedor. No usar una intensidad de AWS inventada ni declarar electricidad renovable como cero físico.

**Destino:** SD4 §4.3.1.4, nota de huella de toda la solución.

**Plantilla:** «La huella operacional anual estimada es [DATO: tCO₂e/año y desglose nube/sitios/dispositivos/combustible], calculada como suma de energía atribuible por factor territorial de emisión y combustible por su factor, más el reporte atribuible de nube sin duplicaciones, con fuentes y año [DATO]; para Talca se usa la cota de 118.260 kWh/año, que se sustituirá por medición, y los informes de 8.4.3 contrastarán la estimación con la operación».

## 22. RT-15.04 — C2

**Fuente:** SD4 §§4.3.1.2 y 4.3.2.2: sa-east-1 São Paulo, us-east-1 Virginia del Norte; §4.3.1.4: ≈13,4/8,9 ≈1,5 de PUE de sala. El consumo adicional de gateway hasta ≈13,5 kW no pertenece a ese PUE. BTT RT-15.04. No hay intensidad numérica publicada de AWS incorporada.

**Dato y obtención:** intensidad de carbono aplicable a la región sa-east-1 en gCO₂e/kWh, año y método (territorial o de mercado, límites y atribución); dato/tratamiento equivalente para DR. Página o informe oficial de sostenibilidad de AWS y reporte de carbono de la cuenta; si AWS no publica intensidad regional, solicitarla o documentar explícitamente un factor territorial oficial y su diferencia respecto de una intensidad del proveedor. Un reporte de tCO₂e por cuenta no se transforma en g/kWh sin denominador energético.

**Destino:** SD4 §4.3.1.2.

**Plantilla:** «La intensidad declarada para sa-east-1 es [DATO: gCO₂e/kWh, año, fuente y método de atribución]; us-east-1 de recuperación se trata mediante [DATO: intensidad o método documentado y fuente], mientras el PUE de diseño de la sala de Talca es aproximadamente 1,5». No inventar valores Zebra/AWS ni importar un factor chileno a Brasil.

## 23. RT-15.08 — C2

**Fuente:** SD1 §§1.4 y 1.5, Tabla 1.3: certificaciones corporativas y personas/roles/períodos; T-6 Tabla 1: experiencia empresarial; T-15 §5.7: familias y asignación antes de H1. BTT §15.3 exige 2 gestión de proyectos, 5 ITIL, 2 COBIT, 3 arquitectura de nube, 2 seguridad, 2 bases de datos y 2 calidad/pruebas; RT-15.07 exige copia y código cuando exista. La nueva promesa de continuidad de certificados de SD1 §1.5 no acredita certificados personales.

**Dato y obtención:** por cada certificación mínima, titular real, credencial, organismo, código y vigencia, con dedicación/período efectivo de la persona en el proyecto. Expediente de RR. HH., certificado y verificador del emisor; documentación preparada por el equipo para el caso ficticio. Una persona puede cubrir distintos grupos si posee las credenciales, pero no contarse dos veces dentro del mismo grupo. No certificar a Aravena/Castillo/Catalán por sus cargos ni usar certificación corporativa como personal.

**Destino:** SD1 §1.5, junto a Tabla 1.3, relación persona–credencial–dedicación.

**Plantilla por persona:** «[DATO: nombre] acredita [DATO: certificación, emisor, código y vigencia] y participará como [DATO: rol/tecnología] con [DATO: dedicación y meses], dentro de la dotación del T-15». Para líderes existentes reutilizar sus períodos; si faltan titulares suficientes, es problema de competencia/dotación, no frase C.

## 24. RT-16.24 — C2

**Fuente:** SD4-Anexos 4-H INT-11 y 4-I Tabla A.10; 4-W.5: dos avisos por entrega; SD4 §4.1.6.2 y SD5-Anexos 5-A/5-C: dominio común CORREO, SMS, WHATSAPP y AVISO_EN_PORTAL. SNS/API de canal no identifica proveedor comercial ni tarifa de todos esos canales.

**Cálculo disponible:** 1.400 ×2 = **2.800 avisos/día normales**; 2.600 ×2 = **5.200 peak**. Por canal j, volumen = total × proporción j, con suma de proporciones =1 para dos avisos lógicos. Si se reenvía o duplica por otro canal, añadir los intentos facturables y no ocultarlos dentro de esa suma. Una tarifa puede cobrar por segmento SMS, destinatario, conversación o mensaje: aviso lógico y unidad facturable deben distinguirse.

**Dato y obtención:** proveedor y cotización oficial vigente por cada canal, moneda, unidad, tarifa/impuestos, proporciones normal/peak y política de reintentos/excedentes. Equipo de integración y financiero, consola/contrato de proveedor y preferencias proyectadas de CLIENTE. Se puede proponer incluir la carga normal y peak en el precio ofertado, pero se necesita cotización para sostenerla.

**Destino y plantillas:** 4-H INT-11, sin cifras económicas: «Los canales CORREO, SMS, WHATSAPP y AVISO_EN_PORTAL usarán [DATO: proveedor por canal], con volúmenes normal/peak [DATO: por canal y unidad facturable], cuya suma corresponde a 2.800/5.200 avisos lógicos diarios más los reintentos facturables declarados; tarifas y tratamiento variable constan en [DATO: partida económica]». Oferta Económica: «[DATO: canal/proveedor] cobra [DATO: tarifa, moneda, unidad e impuestos] sobre [DATO: volumen facturable]; el precio incluye [DATO: cobertura normal/peak] y los excedentes se liquidan mediante [DATO: regla y responsable]».

## 25. RT-17.07 — C2

**Fuente:** SD4 §4.2.6.7 y SD4-Anexos 4-W.6: reparto 5,36 MB normal, 8,24 septiembre, 9,83 ruta de 34 clientes, descarga por Wi-Fi al retorno; T-11 baterías TC58e 7.000 mAh y MC9400 5.000 mAh; Caso RT-03.10: 14 h. SD13 §13.2 y SD8 R8-26 reconocen consumo de batería como riesgo de reproducción de incidentes.

**Dato y obtención:** estimación por modelo basada en ensayo representativo de 14 h, con escaneos, pantalla/brillo, GPS, red, cámara, Bluetooth/POS, sincronización y eventual captura de incidencias. Equipo móvil e integrador; informe de ensayo o perfil de potencia documentado, además de ficha de batería. No deducir autonomía de mAh nominales ni de megabytes.

**Cálculo válido al obtenerlo:** consumo porcentual = 100 × (carga inicial − final) / capacidad utilizable, o diferencia de porcentajes medidos; declarar desgaste y temperatura del ensayo. Optimización C1: sincronización por lotes, espera creciente y Wi-Fi al retorno, sin reducir GPS, muestreo ni plazos contractuales.

**Destino:** SD4 §4.2.6.7.

**Plantilla:** «La aplicación limitará actividad innecesaria mediante sincronización por lotes, reintentos espaciados y Wi-Fi al retorno, conservando los intervalos y plazos requeridos; el consumo por turno de 14 horas de [DATO: modelo/variante] se estima en [DATO: porcentaje o mAh y capacidad utilizable], bajo [DATO: condiciones y referencia de ensayo], con los consumos de datos ya dimensionados». Repetir por perfiles/modelos relevantes, no extrapolar reparto a todo el parque.

## 26. RT-21.01 — C1

**Fuente:** SD1 §1.1; SD4-Anexos §4-W.7; T-15 §§4.1 y 5.7; BTT RT-21.01. **Decisión y cálculo:** NOC propio en Sede Central de Santiago; una posición permanente, 4 relevos a 42 h y 5 a 40 h desde 26-04-2028, como RNF-21.01. La ubicación propuesta no transforma el domicilio de Valparaíso en una sede de Santiago ni el NOC en sala de servidores del CLIENTE.

**Destino:** SD1 §1.1. **Frase:** la frase íntegra de RNF-21.01; una sola inserción cubre ambas IDs. Conservar mesa 04:00–22:00 L–S y 24×7 en septiembre/diciembre: cobertura del NOC no reemplaza el horario de la mesa ni confunde S-43 con horario de producción.

## 27. RT-21.03 — C2

**Fuente:** SD1 §1.5, Tabla 1.3: Guillermo Castillo y Álvaro Catalán durante Operación; Chamorro y Pérez sólo meses 1–21. T-15 §5.7: familias cuantificadas y asignación nominal antes del H1; §§4.2 y 4.4: capacidad de Operación; SD4-Anexos 4-W.7: relevos NOC/SOC. SD13 §13.1.4 preserva fin de dedicación del líder de Datos y frente operativo de Castillo; SD8 §8.1.2 prevé suplencias sin nominar a todo el equipo técnico.

**Dato y obtención:** nómina aprobada con nombre, tecnología, rol, dedicación/HH y meses, incluidos todos los relevos, suplencias y acumulaciones compatibles. Cubrir AWS/sistemas, PostgreSQL/Aurora, red/borde, Laravel/PHP/Kotlin, RabbitMQ/SQS/SNS y seguridad. Dirección de Operaciones y RR. HH., asignación contractual de T-15 y cartas de compromiso; no generar nombres ficticios adicionales ni prolongar automáticamente a Chamorro/Pérez.

**Destino:** SD1 §1.5.

**Plantilla por asignación:** «[DATO: nombre] cubrirá [DATO: tecnología y funciones operativas], con [DATO: dedicación y período], y tendrá como relevo/suplente a [DATO: nombre y dedicación], dentro de las posiciones y HH existentes del T-15». Las acumulaciones deben caber en la capacidad; liderar SRE o seguridad no acredita por sí solo nominación del equipo completo.

## 28. RT-21.19 — C1

**Fuente:** T-14 §2.8, cuenta 8.2; T-15 §4.2, 8.2.1 =4.608 HH DES y 8.2.4 =2.304 HH DES de deuda técnica; SD6 §§6.1.4 y 6.2; T-18 §1. **Decisión y cálculo:** igual reserva de RNF-21.08: 4.608/3 =1.536 HH DES/año combinadas; mitad =768 HH DES evolutivas/año. **Composición:** 100 % familia DES ya programada, ejecutada por desarrolladores Laravel/PHP o Kotlin según el cambio; no repartir nuevas HH entre ARQ, CAL, SRE o SEG. La ejecución conserva pruebas y aprobación existentes; si una solicitud exige capacidad adicional de otras familias, debe evaluarse antes de aprobarla y no fingirse incluida.

**Destino:** T-14 §2.8, cuenta 8.2, misma inserción que RNF-21.08.

**Frase:** «La bolsa evolutiva será de 768 HH anuales de la familia DES, para desarrollo Laravel/PHP o Kotlin según el cambio, reservadas dentro de las 4.608 HH de 8.2.1 y separadas de las 768 HH correctivas anuales y de las 2.304 HH de deuda técnica de 8.2.4; cada solicitud del CLIENTE se estimará por LafroX, requerirá aprobación previa del CLIENTE y se liquidará por HH efectivas y saldo, respetando las ventanas de despliegue». Integrar con la frase de RNF-21.08 en un único párrafo, sin duplicar bolsa ni modificar T-15.

## 29. RT-23.01 — C2

**Fuente:** SD1 §1.1, giro/historia desde 2012; §1.2 Tabla 1.1, Sede Central Santiago; portada, Av. Brasil 2241 Valparaíso; §§1.3 y 1.4, gobierno y certificaciones; T-6 Tabla 1, experiencia. No consta misión/visión/valores aprobados ni inventario coherente de oficinas. Un domicilio legal no demuestra oficina operativa. Talca y Concepción son instalaciones del CLIENTE.

**Dato y obtención:** declaración institucional aprobada por el equipo que representa a LafroX en este caso ficticio, y relación de oficinas con ciudad, dirección y función, distinguiendo domicilio legal. Responsable: representante legal/Dirección, ficha corporativa y documentos del grupo. No es necesario inventar una política real de una empresa externa; sí obtener aprobación institucional de la empresa ficticia que sólo el equipo puede dar.

**Borrador orientativo disponible, no antecedente acreditado:** misión: diseñar, implantar y operar soluciones de misión crítica para logística, distribución y transporte; visión: consolidar continuidad operacional en entornos distribuidos; valores: calidad, seguridad, trazabilidad y preservación del conocimiento. Se funda en §§1.1 y 1.3 y permite al equipo aprobar o corregir sin redacción extensa.

**Destino:** SD1 §1.1.

**Plantilla:** «La misión de LafroX es [DATO: misión aprobada], su visión es [DATO: visión aprobada] y sus valores son [DATO: valores aprobados]; su presencia geográfica comprende [DATO: oficinas efectivas, ciudad, dirección y función], y su domicilio legal es Av. Brasil 2241, Valparaíso». No presentar el borrador como ya adoptado.

## Comprobación de coherencia y mínimo arrastre

Las **29 IDs** están presentes en la tabla y tienen sección propia: **12 C1 y 17 C2**. Los cierres repetidos se aplican una sola vez: DNS (3 IDs), NOC (2), bolsa evolutiva (2), cotizaciones (2) e IP/caídas (2).

La propuesta no suma HH ni cambia las curvas de T-15, las posiciones de 4-W.7 o los hitos de T-18. NOC/SOC siguen siendo puestos separados; el SOC desde mes 13, relevos 4/5 y mesa con tercer agente valle desde mes 25. La ubicación propuesta en Santiago no acredita por sí sola disponibilidad de instalaciones o nómina, pero es una decisión admisible de oferta sobre sede declarada. Las certificaciones y la nominación del equipo completo permanecen C2. La deuda técnica sigue en 8.2.4 y no se consume como bolsa evolutiva.

Se preservan S-43 (L–V 08:00–20:00 sólo para no productivos), el servicio productivo y sus ventanas críticas, congelamientos y plazos de seguridad existentes. La reserva evolutiva no autoriza desplegar dentro de fechas prohibidas ni decide el asunto contractual pendiente de intervenciones urgentes. No se añade IA: D-09, los procedimientos NOC/SOC y la usabilidad permanecen deterministas; las certificaciones de IA no se vuelven exigibles por estas frases.

El hardware de terreno sigue a cargo del CLIENTE; LafroX conserva habilitación e infraestructura on-premise previstas en SD6/T-14. La extensión de postura a ocho estaciones utiliza el inventario F-03 de 192 y no crea una segunda plataforma. No se cambian modelos, UPS, consumos o asignaciones ambientales sin fichas. Los factores de carbono y prestaciones físicas no se inventan. Toda cifra económica va al Sobre 3; referencias técnicas no equivalen a valores acreditados. Si una C2 muestra incompatibilidad que obliga a sustituir equipo, contratar personal adicional o recalcular capacidad, ese trabajo supera un cierre con frase y debe tratarse aparte.

## Preguntas agrupadas para el equipo — sólo C2

Cada pregunta solicita un conjunto de datos que forma una única ficha de cierre; las filas compartidas reutilizan la respuesta.

1. **RNF-23.01 / RT-08.10:** ¿Cuál es la cotización fechada por cada dispositivo y unidad facturable de T-11, con moneda, impuestos y accesorios/consumibles incluidos o separados, para individualizarla sólo en la Oferta Económica?
2. **RNF-23.02 / RT-08.12:** ¿Qué ficha oficial de cada variante o conjunto acredita su IP y resistencia a caídas, con condiciones de ensayo y justificación de aplicabilidad para equipos fijos?
3. **RNF-23.04 / RT-08.01, estaciones:** ¿Cuál es el SKU/configuración de las ocho estaciones, con CPU, RAM, disco, interfaces, consumo máximo y evidencia de eficiencia energética?
4. **RT-08.01, E-01:** ¿Cuál es la CPU y configuración exacta del mini-PC seleccionado, con interfaces, alimentación redundante y ficha que sostenga el máximo de 45 W?
5. **RT-08.11:** ¿Qué matriz de uso y fichas/ensayos acreditan ambiente y autonomía de cada modelo en su turno, manteniendo la entrada a congelado reservada al Freezer?
6. **RT-03.08:** ¿Cuál es la propuesta Savings Plans, con tipo, compromiso por hora, plazo, pago, cargas elegibles, costo contractual y partida económica?
7. **RT-04.13:** ¿Cuál es el presupuesto comparativo por ambiente que identifica costo evitable, costos residuales, compromisos y horas excepcionales del horario S-43, con su ahorro anual económico?
8. **RT-14.08:** ¿Cuál es el presupuesto de observabilidad por señal, volumen/muestreo y rubro de ingesta, línea, archivo y consulta, con implementación de trazas de 30 días y partida económica?
9. **RT-15.03:** ¿Cuál es la estimación de energía/combustible anual atribuible a nube, sitios, puestos y dispositivos, con factores publicados, límites y método que permita obtener la huella anual completa sin duplicaciones?
10. **RT-15.04:** ¿Qué fuente oficial y año respaldan la intensidad aplicable a sa-east-1 y el tratamiento de us-east-1, en gCO₂e/kWh y con método de atribución explícito?
11. **RT-15.08:** ¿Qué relación persona–credencial vigente–dedicación efectiva cubre las siete cantidades mínimas de BTT §15.3, con copias y códigos verificables?
12. **RT-16.24:** ¿Cuál es la ficha comercial por canal con proveedor, unidad facturable, tarifa, moneda/impuestos, reparto normal/peak, reintentos y liquidación de excedentes?
13. **RT-17.07:** ¿Qué informe de ensayo por modelo estima el consumo de batería durante 14 horas, con carga utilizable, temperatura, pantalla, GPS, escaneo, red y periféricos representativos?
14. **RT-21.03:** ¿Cuál es la nómina operativa por tecnología, con dedicación, meses y todos los relevos y acumulaciones, dentro de las posiciones y HH del T-15?
15. **RT-23.01, identidad:** ¿Qué misión, visión y valores aprueba el equipo para LafroX, tomando como base el borrador de esta sección?
16. **RT-23.01, oficinas:** ¿Qué oficinas efectivas de LafroX existen en Santiago y Valparaíso, con dirección y función, y cuál corresponde sólo a domicilio legal?
