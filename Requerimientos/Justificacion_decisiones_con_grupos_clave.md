# Justificación de decisiones con grupos clave

> Documento de trabajo del proponente (TFEP-01/2026 — Caso 02 Logística, Distribuidora Puelche S.A.).
> Fuentes: `Requerimientos/decisiones.md` (registro D1–D40) y `TrabajosAnteriores/mapeo_actores.md` (46 actores/grupos).
> Narrativa base: entrevistas del Cap. 8 del caso (tensiones explícitas entre actores) y decisiones deliberadamente no resueltas del numeral 16.1.
> Será consolidado como apoyo del "esquema de solución y alcance" y de la estrategia de gestión del cambio del informe (Subdoc 3/5 del T-22), no como capítulo aparte.

---

## 1. Objetivo y criterio de justificación

Cada decisión del registro (D1–D40) se justifica aquí **no solo frente al catálogo de requerimientos, sino frente a los grupos clave que la viven**. El criterio es:

1. Identificar qué grupo(s) de interés quedan afectados por la decisión (operacionales, gestión y dirección, externos, reguladores o del proyecto).
2. Mostrar cómo la decisión **arbitra la tensión** declarada en las entrevistas (Cap. 8), sin elegir ganadores: distribuye costos y beneficios.
3. Explicitar la **consecuencia si se omite**: cada decisión ausente es un riesgo evaluable por la Comisión (Cap. 19) y un vacío declarable (BTC 17.1).
4. Cerrar con la **estrategia de aceptación** por grupo (sección 4): una decisión técnicamente correcta que el sindicato, el planificador o el turno de bodega rechacen, es una decisión que fracasa en producción (advertencia de la gerenta general, Cap. 1).

Las tensiones del Caso 02 **no se resolverán antes de la adjudicación** (nota del Cap. 8): la propuesta convive con ellas y las arbitra en cada decisión.

---

## 2. Grupos clave y su posición (resumen)

Referencia: mapeo de actores completo de `TrabajosAnteriores/mapeo_actores.md`.

| Grupo clave | Posición declarada (Cap. 8 / restricciones) | Decisiones que más lo afectan |
|---|---|---|
| Preventista (62) | Opera "a ciegas"; queda "mentiroso" ante el cliente; no se capacita deteniendo la venta (R. N.º 11) | D6, D8, D9, D22, D23, D24, D31, D34 |
| Conductor propio (42 + 42 peonetas) | Circula con >$1 M; sin protocolo; dos manos ocupadas; rendición al día siguiente | D3, D4, D5, D6, D12, D13, D15, D39 |
| Conductor de transportista (≈160, 10 empresas) | No es trabajador de Puelche; rota sin aviso; sin correo (R. N.º 6) | D5, D13, D15, D33, D34, D39 |
| Preparador / bodega nocturna (≈120) | Rotación 38 %; −22 °C; sin señal; -40 % productividad con dispositivos nuevos (R. N.º 11) | D14, D19, D25, D36 |
| Recepcionista | Doble digitación; lote en texto libre (41 % sin lote) | D2, D11, D35 |
| Jefa de Bodega (Ximena Bravo) | Slotting mal asignado desde 2013; decide destino de devoluciones sin registro | D12, D14, D23, D24 |
| Planificador de rutas (Hugo Maldonado) | "Que me proponga, no que me imponga"; se jubila en ~2 años | D16, D20, D36 |
| Equipo TI (4 personas, Eduardo Kaufmann) | "Si necesita administrador dedicado, cotícenlo"; prefiere nube | D17, D18, D19, D26–D32 |
| Gerenta General (Amparo Ossa) | "No me cambie al cliente" | D34, D38, D40 |
| Gerente Operaciones (Nelson Quinteros) | "No me toquen el despacho"; 24 h "es imposible" | D1, D3, D4, D14, D21, D26, D30, D36, D39 |
| Gerente Comercial (Rubén Salinas) | Promesa 24 h; mantiene efectivo (38 %); canal moderno 2029 | D1, D6, D9, D22, D40 |
| Gerente Finanzas (Patricio Vergara) | Costo de servir mes a mes; $4,2 M de descuadre | D6, D7, D9, D10, D40 |
| Jefa de Calidad (Katherine Ñanco) | Retiro < 2 h; bloqueo automático ante excursión | D2, D4, D13, D25, D35, D39 |
| Cliente canal tradicional (11.600) | No va a cambiar: sin internet, sin dispositivo, efectivo (R. N.º 5) | D3, D6, D12, D15, D34, D38 |
| Cliente canal moderno (500 puntos; principal = 11 %) | EDI, ventana 30 min, POD digital, penalización; fecha límite ene-2029 | D20, D22, D38 |
| Sindicato de conductores (R. N.º 10) | Objeción formal a cámaras y GPS de jornada | D13, D39 |
| Proveedores (180) y proveedor de lácteos (6 %) | Retiro preventivo: exige trazabilidad certificada | D2, D33, D34 |
| Empresas transportistas (10) | Puelche no controla vehículos ni conductores | D5, D33, D34 |
| Autoridad sanitaria / SII / Agencia de Datos / ANCI | Sumario, DTEs, Ley 21.719, Ley 21.663 | D2, D12, D15, D35, D38 |
| Comisión Evaluadora (Cap. 19) | Juzga comprensión, coherencia, vacíos no listados | D1–D40 (transversal) |

---

## 3. Justificación de decisiones por grupo de tema

Formato: **Decisión adoptada** (resumen del registro) → **Grupos clave** (efecto) → **Tensión arbitrada / riesgo si se omite**.

### 3.1 Servicio, métricas y costo de servir — D1, D7, D21, D22

**D1 — Entrega cumplida y OTIF.** Parcial = no cumplida; OTIF diario por cliente, ruta, zona y consolidado; causal tipificada ante desvíos; Fill Rate y Perfect Order contra la orden original.
- Grupos: Operaciones (sabe al final del día cuántas llegaron, no al siguiente); Comercial (promesa verificable ante el canal moderno); Finanzas (base única para costear); preventistas/conductores (cada desvío queda auditado, no al criterio de cada área).
- Tensión/riesgo: sin métrica unívoca cada área cuenta distinto (la causa raíz del desacuerdo actual); la Comisión mide coherencia del indicador contra el Cap. 18.

**D7 — Costo de servir.** Por entrega y por cliente desde el hecho real (GPS/combustible devengado, peajes, tiempos, indirectos prorrateados, devoluciones/mermas/envases); matriz de rentabilidad neta mensual con sugerencia de ajuste (frecuencia/umbral mínimo), sin eliminar clientes.
- Grupos: Finanzas (obsesión declarada: sabe cuánto cuesta atender cada punto); Comercial (segmenta sin perder clientes); Operaciones (costeo desde dato real, no prorrateo de 2016); preventista (se le sugiere, no se le impone el quiebre del cliente).
- Tensión/riesgo: decisión comercial a ciegas (puede estar perdiendo plata en 2.000 clientes); la pregunta del gerente de finanzas queda sin respuesta si se omite.

**D21 — Metas de los 16 resultados.** Curva de mejora gradual (OTIF 90 % fin Etapa 1 → 93 % mes 12 → 95 % régimen; FR ≥ 97 %; ocupación ≥ 75 %; reentregas ≤ 1 %; envases ≤ 7 %; listado de retiro < 2 h), ancladas en RF de medición con base de cálculo explícita.
- Grupos: Comisión (evaluación del Cap. 18 requiere metas comprometidas, no diagnóstico); Operaciones/Calidad (umbrales de marcha blanca realistas); Finanzas (compromiso alcanzable = oferta creíble).
- Tensión/riesgo: metas planas desde el mes 1 son inauditables o inalcanzables; sin metas no hay marcha blanca definible.

**D22 — Ventana y hora de corte.** Preventista ofrece la ventana comprometible (30 min) desde la ficha y el plan; ETA avisado; hora de corte parametrizable por zona que dispara las misiones de picking.
- Grupos: Cliente moderno (ventana 30 min exigida 2029); Comercial (promesa frente al competidor); Preventista (informa y cumple); bodega nocturna (el corte ordena el ciclo).
- Tensión/riesgo: sin hora de corte el ciclo nocturno se desfasa y la promesa del canal moderno es incumplible.

### 3.2 Pago, cobranza, precio y descuentos — D6, D9, D40

**D6 — Efectivo.** Se mantiene (38 % del canal tradicional); se reduce con encargo web y POS móvil; riesgo controlado con rendición digital por camión, causales tipificadas con firma y bloqueo del cierre ante saldo sin justificar. Pago anticipado al preventista como alternativa (RF-07.06/RF-07.10).
- Grupos: Finanzas ($4,2 M/mes trazables); Comercial (respeta a los clientes que pagan en efectivo, la mayoría del canal tradicional); conductor (seguridad: menos dinero sin declarar); tesorería (conciliación automática, no "conversada").
- Tensión/riesgo: Finanzas (eliminar) vs. Comercial (mantener) — se arbitra manteniendo y controlando; sin control, el descuadre se perpetúa.

**D9 — Cambio de precio.** Por defecto precio vigente al despacho (RF-03.11); excepción configurable por cliente/cadena (RF-03.12); alerta al cliente (RF-03.13).
- Grupos: Finanzas (facturación consistente); Preventista (credibilidad frente al cliente); cliente (no se entera después de un cobro distinto).
- Tensión/riesgo: cobrar siempre lo ofrecido contradice el RF-03.11; sin regla, facturación y promesa divergen.

**D40 — Descuentos y promociones en terreno.** Solo promociones vigentes del catálogo (RF-03.07); toda diferencia con causal tipificada (RF-07.03); excepción con aprobación registrada de supervisor (RF-03.10).
- Grupos: Conductor (fin del "descuento de buena fe" sin registro); Finanzas ($4,2 M auditables); Comercial (promociones aplicadas de forma controlada); Crédito y cobranza (responsables identificados con firma).
- Tensión/riesgo: sin regla el descuadre de caja se perpetúa y no hay responsable.

### 3.3 Entrega, POD y tributario — D3, D12, D15, D38

**D3 — Local cerrado.** El conductor reporta "local cerrado"; reagenda automática a la próxima ventana del cliente; no decide por su cuenta; si persiste, el producto vuelve al almacén.
- Grupos: Conductor (pierde discrecionalidad, gana protocolo y respaldo); Cliente tradicional (se respeta su ventana); Operaciones (las reentregas dejan de ser la causa índice); Crédito (cobro no perdido en ruta).
- Tensión/riesgo: hoy decide cada conductor (causa principal de reentregas); sin regla, la reentrega sigue arbitraria.

**D12 — Devolución en la entrega.** Registro POD total/parcial con SKU, cantidad y motivo (RF-06.03), offline (RF-08.01); destino decidido en el andén y transmitido al ERP (RF-08.02); nota de crédito la emite el ERP por la cantidad rechazada (RNF-08.02).
- Grupos: Conductor (captura en el punto); Jefa de Bodega (destino estructurado, no "conversado"); Finanzas (nota de crédito sobre la GDE); SII (articulación con documento tributario emitido).
- Tensión/riesgo: sin articulación quedan "dos verdades" entre lo entregado y lo facturado; el sistema no emite DTEs (Restricción N.º 12).

**D15 — Prueba de entrega sin firma.** Firma en pantalla del titular (RF-06.02); alternativas: foto + nombre del receptor (RF-06.12), QR (RF-06.11), térmica Bluetooth (RF-06.13).
- Grupos: Cliente tradicional (no firma en pantalla y no se le exige); Conductor (evidencia válida sin discusión); SII/canal moderno (acuse con respaldo).
- Tensión/riesgo: sin alternativa, la evidencia es inválida y el acuse tributario no se sustenta.

**D38 — POD ↔ GDE/acuse.** Evidencia vinculada a la GDE y a su acuse de recibo digital/tributario (RF-12.12/12.13); acuse al canal moderno ≤ 30 min de la descarga; firma avanzada solo donde el caso la exige (RF-18.01), nunca al receptor tradicional.
- Grupos: SII (articulación tributaria obligatoria; firma RT-16.17/16.18); Cliente moderno (acuse inmediato con su POD digital); Conductor (evidencia y acuse en un solo acto).
- Tensión/riesgo: el receptor habitual es persona natural sin firma avanzada; sin articulación, la exigencia tributaria queda sin resolver.

### 3.4 Stock, productos y envases — D8, D10, D11

**D8 — Asignación de stock.** Reserva en la confirmación (servidor central), primer llegado; segundo preventista ve quiebre parcial (RF-03.03); offline = indicativo con antigüedad; conflictos resueltos cronológicamente al sincronizar (RF-02.05e).
- Grupos: Preventista (sabe al confirmar; no compromete y falla después); Bodega (preparación con causa de quiebre); Comercial (cero pedidos perdidos/duplicados: criterio del Cap. 18).
- Tensión/riesgo: reserva distribuida en la toma del pedido es inviable; sin regla, el doble compromiso deja stock prometido sin respaldo.

**D10 — Envases retornables.** Control por saldo por cliente (cuenta corriente), no por unidad; alerta de umbral (RF-08.04); reporte diario de pérdida por cliente/tipo/zona (RF-08.06).
- Grupos: Transporte (devolución suma al saldo en ruta); Crédito/comercial (umbral visible al preventista); Finanzas (14 % anual de 68.000 canastillos y 9.400 pallets controlado).
- Tensión/riesgo: el control por unidad identificada es inviable y desproporcionado; sin saldo por cliente, la fuga del 14 % se mantiene.

**D11 — Maestro de productos.** Maestro interno único con historial (RF-01.10); códigos externos resueltos por equivalencias por cadena (RF-12.03); no resueltos a bandeja (RF-12.06).
- Grupos: Abastecimiento (sugerencia de reposición con producto correcto); Recepcionista (captura sin re-digitar); Proveedores (cambios de formato no rompen la operación); Bodega (pedidos sin producto erróneo).
- Tensión/riesgo: con 180 proveedores/8.400 productos el cambio semanal de código, sin maestro, genera duplicados y pedidos incorrectos.

### 3.5 Calidad, cadena de frío y trazabilidad — D2, D4, D35

**D2 — Unidad de trazabilidad sanitaria.** El lote del proveedor (AI 10) es la unidad; el SSCC identifica la unidad logística; retiro y trazabilidades forward/backward por lote (RF-01.02, RF-01.07, RF-02.10, RF-09.01).
- Grupos: Jefa de Calidad (respuesta al retiro en horas, no 9 días); proveedor de lácteos (acredita trazabilidad y restablece la relación); Recepcionista (captura obligatoria, validada); Autoridad sanitaria (sumario respondido); TI (volumen acotado al lote).
- Tensión/riesgo: caja/pallet/SSCC como unidad triplican el esfuerzo sin mejorar el retiro; sin lote obligatorio se repite el retiro masivo de $31 M.

**D4 — Excursión térmica.** Parámetros configurables (tiempo/grados) por tipo de producto definidos por Calidad (RF-09.06); alerta en tiempo real (RF-09.05); bloqueo del despacho NO automático: lo decide el conductor según tipo (RF-09.07).
- Grupos: Calidad (regla escrita, piso D.S. 977/96); Operaciones (no cae la ventana de despacho); Conductor (decide con reglas pre-acordadas); Bodega (disposición final documentada).
- Tensión/riesgo: bloqueo automático arbitrario derriba la ventana 05:30–07:00 (R. N.º 1); sin regla, "monitorear ≠ decidir" y la excursión pasa sin control (HACCP/GDP).

**D35 — Modelo de datos de trazabilidad.** Lotes + eventos de negocio bajo GS1 EPCIS; consulta de afectados ≤ 2 h (RNF-09.01); retención vida útil + 6 meses, piso 5 años (RNF-09.02).
- Grupos: Calidad (retiro < 2 h del Cap. 18); Sanitaria/SII (piso legal de retención); TI (volumen de eventos dimensionado, no infinito).
- Tensión/riesgo: sin modelo eventos–estados, la consulta forward/backward vuelve a tomar días.

### 3.6 Flota, conductores, sindicato y ruteo — D5, D13, D16

**D5 — Identificación del conductor/vehículo.** Confirmación diaria en el portal de transportistas antes de la ventana (RF-12.21); autenticación del conductor real con OTP del jefe de flota (RF-06.08) o PIN/QR al iniciar (RF-14.07); vinculación conductor–camión por viaje.
- Grupos: Transportistas (rotación sin aviso resuelta en la puerta); Conductores externos (sin correo, sin código permanente); Operaciones/Tesorería (quién operó y respondió por cada viaje).
- Tensión/riesgo: 54 camiones y ≈160 personas fuera del control de Puelche; sin identificación, la responsabilidad del viaje es inauditable.

**D13 — Cámaras/GPS y jornada.** No se proponen cámaras en cabina; GPS para jornada solo con acuerdo sindical y respeto de privacidad (RF-14.05); telemetría limitada a vehículo/ruta (RF-14.01/04/08); gestión del cambio con el sindicato desde la Etapa 1.
- Grupos: Sindicato (objeción R. N.º 10 atendida); Conductores (privacidad preservada); Operaciones (visibilidad de flota sin control de jornada); Comercial (no se pierde el viaje por conflicto).
- Tensión/riesgo: proponer cámaras/GPS de jornada sin acuerdo es un bloqueo del proyecto predecible; la restricción N.º 10 es explícita.

**D16 — Conocimiento del planificador.** Captura en la Etapa 1: sesiones de transferencia + parametrización de sus reglas en el motor (RF-04.01); modificación manual conservada con recálculo de ETA (RF-04.02/04.04); cada corrección "enseña" al sistema.
- Grupos: Hugo Maldonado ("que proponga, no que imponga"); su ayudante (operar sin perder 6–9 puntos); Operaciones (continuidad con fecha conocida); Comercial (rutas correctas).
- Tensión/riesgo: el conocimiento crítico (puentes, clientes, caminos) se pierde con la jubilación; un motor que impone es rechazado en terreno.

### 3.7 Almacén y operación de bodega — D14, D23, D24, D25

**D14 — WMS de 2013.** Se reemplaza (decisión delegada por el cliente): multi-sitio configurable, consolidación multi-nodo, slotting ABC, conteo ciego, FEFO y offline 24 h.
- Grupos: Jefa de Bodega (slotting desde 2013 arreglado; destinos estructurados); Operaciones (multi-sitio: Concepción y cross-docks); TI (un solo sistema que mantener); Comercial/Calidad (pedidos y trazabilidad desde una fuente).
- Tensión/riesgo: extender el WMS de 2013 mantiene el problema de raíz; es la decisión de alcance más costosa y el cliente la delega expresamente.

**D23 — Planilla de reposición.** Vacío declarado (Cap. 9.10) y resuelto sin requisito a medida: sugerencia desde historial/frecuencia/promociones (RF-03.15) + merma de góndola (RF-08.05).
- Grupos: Jefe de Abastecimiento (dueño de la planilla de 8 semanas + ajuste manual); Preventista (sugerencia en la visita); Comercial (promociones entran al cálculo).
- Tensión/riesgo: dejarlo sin resolver es un vacío evaluable (BTC 17.1); la planilla mensual con ajuste "como siempre" sigue dominando la reposición.

**D24 — Observación de góndola.** Registro estructurado y liviano (merma SKU+lote, alerta de envases); sin fotografías (evita datos personales e imágenes sin utilidad).
- Grupos: Preventista (información que hoy se pierde, capturada sin fricción); Finanzas (mermas registradas); Agencia de Datos (no se crean nuevas categorías sensibles).
- Tensión/riesgo: fotografías de góndolas agregan datos personales sin valor operacional (RNF-16.03, RNF-14.01).

**D25 — Cámara de congelado.** Terminales aptos para −22 °C, con guantes (RNF-05.02), confirmación ≤ 1 s (RNF-05.01), turno completo offline con sincronización 100 % (RNF-09.04); estudio de cobertura Wi-Fi incluye cámaras (RNF-13.09).
- Grupos: Preparador (dispositivo que no falla en el congelado); Jefa de Bodega (no cae la productividad por hardware inadecuado); Calidad (picking trazable en frío).
- Tensión/riesgo: dispositivos convencionales fallan a −22 °C y sin señal; el congelado queda en papel y sin trazabilidad.

### 3.8 Infraestructura, continuidad y datos — D17, D18, D19, D26, D27, D28, D29, D30, D31, D32

**D17 — Híbrido nube/on-premise.** WMS y borde del CD on-premise (offline 24 h, ≤ 1 s); nube para analítica, portales, EDI y servicios elásticos; tabla de emplazamiento por componente como entregable.
- Grupos: TI (4 personas: servicios administrados de nube); Operaciones (funciona con cortes de fibra); requisito habilitante del BA Art. 16.2; Comisión (híbrido obligatorio).
- Tensión/riesgo: solo-nube se cae con el corte de fibra; solo-on-premise incumple las Bases; la tabla de emplazamiento es obligatoria (RF-13.02, RT-03.01).

**D18 — Motor de bases de datos.** Relacional ACID (PostgreSQL) para lo transaccional + analítico columnar separado (BI/tablero), desacoplados (RNF-11.02).
- Grupos: Operaciones/SRE (peak de septiembre absorbido sin degradar picking); TI (mantenible por 4 personas); Comisión (declaración por dominio con posición CAP, RT-05.02).
- Tensión/riesgo: OLTP y OLAP compartidos degradan la confirmación de picking (≤ 1 s) y la preventa.

**D19 — Tipo de aplicación.** NATIVA para terreno (preventa, reparto, bodega): offline 14 h, periféricos GS1/térmica/GPS/balanza, guantes a −22 °C, curva ≤ 2 h; web/PWA para autoatención del cliente.
- Grupos: Preventista/Conductor/Preparador (operan sin señal, con guantes, a una mano); Transportistas (dispositivos compartidos); TI (costo de mantención asumido y declarado); Cliente canal tradicional (nada que instalar).
- Tensión/riesgo: PWA/híbrida no alcanza robustez sin señal ni periféricos; el trade-off de costo es declarado (RT-17.01).

**D26 — Enlaces redundantes.** Enlace redundante por sitio on-premise con caminos y proveedores distintos, conmutación ≤ 5 min (RNF-13.07) + operación autónoma 24 h (RNF-13.01) + ancho de banda dimensionado (RNF-13.08).
- Grupos: Operaciones (Concepción hoy sin respaldo; Los Ángeles pierde señal en su ventana); TI (conmutación automática manejable); cross-docks (madrugada cubierta).
- Tensión/riesgo: sin redundancia, un corte de fibra en la madrugada detiene un sitio entero.

**D27 — DR.** Sitio secundario activo-pasivo en región distinta, RTO ≤ 4 h / RPO ≤ 15 min, pruebas 2×/año (RNF-20.06); respaldo 3-2-1-1-0 con restauración mensual (RNF-20.07).
- Grupos: TI (operable por equipo pequeño); Operaciones (objetivos de continuidad); Comisión (RTO/RPO declarados, Art. 20/RT-07.01).
- Tensión/riesgo: activo-activo agrega costo y reconciliación sin beneficio al volumen; sin DR, el caso exige sitio secundario y no lo hay.

**D28 — RAID/redundancia on-premise.** RAID 6 (datos/inventario) y RAID 10 (transaccional), hot-spare; equipos críticos redundantes (RNF-13.03/04/05).
- Grupos: TI (almacenamiento mantenible); Operaciones (tolera falla de al menos un disco, exigencia explícita).
- Tensión/riesgo: un disco fallido = inventario perdido; el nivel RAID debe declararse y justificarse (RT-03.14).

**D29 — Emplazamiento por sitio.** Talca conserva la sala principal y se adecúa (25 m² no cumple); sala secundaria en otro recinto; Concepción y cross-docks con gabinetes de borde; padrón de emplazamiento declarado (RT-06.01).
- Grupos: TI (respaldo físico ubicado); Operaciones (6 sitios, 4 regiones cubiertos); Comisión (tipología por sitio obligatoria: obra civil no declarada = emplazamiento sin resolver).
- Tensión/riesgo: la sala actual no cumple el estándar; sin tipología declarada, la inversión en obra civil es invisible y se evalúa como no resuelto.

**D30 — Peak de septiembre.** Cuello de botella identificado en la persistencia de pedidos y la ingesta de telemetría; escalamiento horizontal automático (RNF-19.02), punto de saturación monitoreado (RNF-19.03), pruebas de carga 1,5× peak y de estrés (RNF-19.04).
- Grupos: SRE/Operaciones (la semana de septiembre no puede caer); TI (escalado configurable); Finanzas (el costo de capacidad queda dimensionado, no sobredimensionado).
- Tensión/riesgo: dimensionar por promedio es el error explícitamente advertido; septiembre duplica el volumen tres semanas.

**D31 — Funciones no disponibles offline.** Declaración obligatoria (RT-03.13): en CD no hay consolidación multi-sitio online (se suple con reporte local); en terreno no hay excepción de crédito del supervisor online (aprobada-diferida con respaldo de llamada).
- Grupos: Preventista (crédito indicativo con respaldo presencial); Bodega (procedimiento manual documentado); conductores (POD sigue operando); Comisión (omitir la lista es observación grave).
- Tensión/riesgo: no declarar qué falla desconectado se evalúa como omisión grave y las expectativas de producción se rompen en el primer corte.

**D32 — Migración de datos.** Por dominio en ventanas sin operación (RT-05.11–05.14): maestros completos, ventas 3 años, inventario 2, trazabilidad 5, cuentas por cobrar abiertas; piso legal 5/6 años (RNF-01.02/08.02/09.02); ERP fuente durante cohabitación con capa anticorrupción (RT-05.20).
- Grupos: TI (convivencia con el ERP 2017 sin documentación); Finanzas (cartera abierta conservada); Calidad (trazabilidad nunca se pierde); SII (documentos 6 años).
- Tensión/riesgo: migrar mal rompe la relación con el ERP; no migrar el piso legal es incumplimiento normativo.

### 3.9 Soporte, identidad, personas y monitoreo — D33, D34, D39

**D33 — Mesa de ayuda y soporte en terreno.** 08:00–20:00 ampliado a 24×7 para críticos y ventana de despacho (RNF-21.04); umbrales de atención (RNF-21.03); dotación con Erlang C (RNF-21.05); traslado de niveles 2–3 a sitios alejados (RNF-21.07).
- Grupos: TI (4 personas: sin administradores dedicados, el soporte se costea); Operaciones (turno nocturno y 05:30–07:00 amparados); Transportistas (error de su conductores se resuelve de madrugada).
- Tensión/riesgo: la operación es nocturna y alejada; sin 24×7, un corte nocturno en bodega pasa inadvertido hasta la mañana.

**D34 — Registro/recuperación de credenciales sin correo.** SSO/directorio (RF-15.01/02); canal moderno por correo (RF-12.25–27); usuarios sin correo con factor presencial —OTP del jefe de flota (RF-06.08) y credencial en dotación—; MFA en acceso externo y privilegiado (RF-15.03).
- Grupos: Conductores externos (rotación sin aviso resuelta); Canal tradicional/proveedores (sin correo); TI (identidad centralizada con MFA); Agencia de Datos (acceso auditado).
- Tensión/riesgo: exigir correo a quien no lo tiene bloquea la operación del día; el alta por flujo de correo asumido (RT-12.12) no sirve a estos usuarios.

**D39 — Monitoreo continuo.** NOC 24×7×365 (RNF-21.01) con observabilidad unificada (RF-16.01) y alertas por síntomas de negocio (RF-16.03); objeto = sistema/operación, NO el conductor: sin cámaras ni GPS de jornada (D13, R. N.º 10).
- Grupos: Operaciones (despacho sin plan B: la ventana no puede estar sin monitoreo); TI (observabilidad administrada); Sindicato (se monitorea la plataforma, no la persona).
- Tensión/riesgo: la preparación es nocturna y la ventana 05:30–07:00 no tiene plan manual; un corte sin detectar llegaría a la mañana con 96 camiones detenidos.

### 3.10 Alcance, despliegue y crecimiento — D20, D36, D37

**D20 — Reparto Etapas 1 y 2.** Etapa 1: trazabilidad/frío, abastecimiento/recepción, WMS/inventario y captura temprana del planificador; Etapa 2: canal moderno (EDI + portal), analítica y ruteo restante; canal moderno en producción antes de ene-2029 (RNF-12.01).
- Grupos: Comité ejecutivo (su preferencia respetada como orden, no como alcance); Operaciones/Calidad (trazabilidad-frío primero, urgencia declarada); TI (planificador capturado antes de la jubilación); canal moderno (fecha límite innegociable).
- Tensión/riesgo: un reparto que difiera sin justificar las 6 dependencias (técnica, riesgo, preferencia, hitos, absorción, criterio) se evalúa como debilidad; el planificador se jubila en ~2 años.

**D36 — Puesta en producción por oleadas.** 1) bodega; 2) preventa por zona; 3) reparto por transportista; 4) facturación/ERP; avance con umbrales OTIF/FR y certificación (RNF-22.04); capacitación sin detener la operación (RNF-22.03).
- Grupos: Operaciones (despacho de la mañana nunca se cae por un paso único); Bodega (arranque con curva de aprendizaje ≤ 2 h, no -40 %); Transportistas (incorporación por empresa); Comercial (preventa por zona sin interrumpir la venta).
- Tensión/riesgo: un único paso afectaría simultáneamente bodega, preventa, reparto y facturación sin reversión.

**D37 — Nuevo CD Los Lagos (2030).** Multi-nodo configurable (RF-02.01) con consolidación multi-sitio (RF-02.02): el CD nuevo se replica por configuración, sin desarrollo a medida.
- Grupos: Operaciones (escalar la red sin rediseño); TI (mantenible por parametrización); Comisión (RT-02.12 exige multi-tenencia o parametrización).
- Tensión/riesgo: sin replicabilidad, el crecimiento del cliente a 2030 exige un rediseño y la decisión del RT-02.12 queda sin responder.

---

## 4. Estrategia de aceptación por grupo (plan de gestión del cambio)

Cada decisión que afecta a un grupo se acompaña de un mecanismo que lo incorpora, para que la adopción no hunda el proyecto (advertencia de la gerenta general).

| Grupo clave | Decisiones que lo afectan | Mecanismo de aceptación |
|---|---|---|
| Preventista | D6, D8, D9, D22, D23, D24, D31, D34 | Capacitación en terreno sin detener la venta (R. N.º 11, RT-22.04); curva de aprendizaje ≤ 2 h (RNF-05.03); crédito/stock visibles (deja de ser "mentiroso"); sugerencias que antes ya hacía en planilla. |
| Conductor propio / peoneta | D3, D4, D5, D6, D12, D13, D15, D39 | POD digital reemplaza la guía mojada; protocolo para local cerrado (menos reentregas); rendición el mismo día (no "conversada"); a una mano y sin red (RT-13.08). |
| Conductor de transportista | D5, D13, D15, D33, D34, D39 | Onboarding simplificado (OTP del jefe de flota); acuerdo de capacitación con cada empresa (R. N.º 6, RT-22.04); soporte y credenciales cubiertos por la oferta. |
| Bodega nocturna / preparadores | D14, D19, D25, D36 | Onboarding por rotación simplificado (R. N.º 11); dispositivo que no falla a −22 °C; capacitación en turno nocturno sin detener la operación (RT-22.04); arranque por oleada con curva ≤ 2 h. |
| Planificador (Hugo) y ayudante | D16, D20, D36 | "El sistema propone, él corrige" (RF-04.02/04.04); sus reglas se parametrizan, no se ignoran; transferencia en sesiones antes de la jubilación. |
| Sindicato | D13, D39 | Comunicación desde la Etapa 1; sin cámaras ni GPS de jornada; la telemetría usa datos del vehículo y la ruta. |
| TI del cliente (4 personas) | D17–D19, D26–D32, D33, D34 | Todo rol de especialista dedicado se ofrece como servicio costeado (Restricción N.º 9); documentación de interfaces del ERP levantada por el adjudicatario. |
| Cliente canal tradicional | D3, D6, D12, D15, D34, D38 | No se le exige nada (R. N.º 5): sigue en efectivo, sin firma forzada y con su ventana respetada; el sistema se adapta a él. |
| Cliente canal moderno | D20, D22, D38 | EDI con formato por cadena (16.2 N.º 2), ventana de 30 min y POD/acuse digital antes de ene-2029 (RNF-12.01). |
| Comisión evaluadora | D1–D40 | Coherencia total: decisión → RF/RNF → RT → párrafo del caso; vacíos declarados (no ocultados) y consultas Art. 43.3 separadas de supuestos. |

---

## 5. Notas resueltas y pendientes del registro

| Nota | Estado | Resumen |
|---|---|---|
| ¿Pago anticipado al preventista? | Resuelto (D6/D40) | Sí, como alternativa al efectivo: POS móvil (RF-07.06) y abonos parciales (RF-07.10), con causales tipificadas (RF-07.03). |
| ¿Más de una propuesta/alternativa? | Pendiente (sección 1 del registro) | Definir antes del cierre de sobres; si se presenta variante, evaluar efecto en puntaje económico (BA Art. 60°–61°) y su declaración en formularios. |
| ¿Monitoreo constante necesario? | Resuelto (D39) | Sí, 24×7×365 (NOC, RNF-21.01): preparación nocturna y ventana de despacho sin plan B (Restricción N.º 1). |