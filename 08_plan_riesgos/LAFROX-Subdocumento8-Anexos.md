# LafroX — Subdocumento 8: Anexos

Los anexos desarrollan el registro de 32 amenazas, la evaluación FMEA, la cuantificación y las respuestas, con matrices de trazabilidad, un modelo reproducible y condiciones de aceptación. Complementan el análisis del cuerpo y el Formulario T-16.

## Anexo 8.A — Registro ampliado de amenazas

Las fichas aplican el proceso de la norma ISO 31000 (International Organization for Standardization [ISO], 2018) que exige el RT-19.04 (Distribuidora Puelche S.A., 2026b), sobre las restricciones del Caso 02 (Distribuidora Puelche S.A., 2026c, Cap. 10) y los temas obligatorios del índice (Distribuidora Puelche S.A., 2026d, sección 11). Cada una se ancla en un subdocumento de la oferta (LafroX, 2026). P, I y D son juicios ordinales iniciales según la sección 8.1.3 del SD8: la causa descrita sustenta P, la consecuencia sustenta I y la forma de detección sustenta D. El cierre de cada ficha exige la evidencia indicada en ella, y los vacíos actuales se distinguen de los eventos inciertos en el Anexo 8.E. Toda ficha se sigue semanalmente y en cada comité, y a diario durante la marcha blanca o la operación afectadas. Tres reglas valen para todas las fichas. El residual hipotético baja P un nivel como supuesto de comparación, no como eficacia medida; sólo la evidencia, el cierre y la autorización ajustan la reserva efectiva (Anexo 8.D). La Tabla C.5 cuenta una sola vez los controles compartidos. Y la contingencia protege la obligación cuando el control falla: retirar alcance obligatorio nunca es una alternativa conforme.

RBS significa estructura de desglose de riesgos y NPR, número de prioridad. G-CAP/G-INT son cargos de efecto compartido definidos en B.2, no riesgos nuevos. Las fichas usan los códigos siguientes.

| Código | Significado | Dónde se define |
| --- | --- | --- |
| R8-01 a R8-32 | Riesgos de este plan | Este anexo |
| E8-01 a E8-14 | Condiciones de evidencia actuales | Anexo 8.E |
| H1 a H12 | Hitos contractuales | SD7, Tabla 7.5 |
| E1, E2 | Etapa 1 y Etapa 2 | Bases Administrativas, Art. 17° |
| F y F−28 días | Fecha de paso a producción de una etapa e inicio de sus cuatro semanas finales de marcha blanca | Bases Administrativas, Art. 17.3 |
| Números x.y.z | Paquetes de trabajo de la EDT | Formulario T-14 |
| M1 a M12 | Módulos de la solución | SD3, Tabla 3.4 |
| INT-01 a INT-15 | Interfaces internas y externas | SD4, Anexos 4-G y 4-H |
| AL-STOCK-01, AL-ACT-01, AL-DR-01 | Protocolos de stock, actualización y recuperación | SD4, Anexo 4-V |
| B-02 | Gateway de borde de los sensores | SD4 y Formulario T-11 |
| D-02, D-03 y siguientes | Dependencias entre paquetes | SD7, Anexo 7.B |
| V-12, V-13 | Consultas al CLIENTE sobre fecha de inicio y evidencia láctea | SD3, Anexo 3.H |
| S-28 | Supuesto del alcance | SD3, Anexo 3.C |
| R18-01 a R18-16 | Resultados del capítulo 18 del caso verificados en la marcha blanca | Formulario T-18 |
| RNG-04 | Regla graduada de excursión térmica | SD3, Anexo 3.G |
| I-01A | Indicador del piloto de INN-01 | SD13 |
| JP, ARQ, SEG, DAT, DES, CAL, SRE, IMP | Roles del equipo | SD8, Tabla 8.1 |
| BA, BTT, Caso | Bases Administrativas, Bases Técnicas Transversales y Caso 02 | Referencias |

### R8-01 — ERP indisponible o guía invalidada

Emisión tributaria concentrada en ERP; si falta una guía o cambia la carga, podría detenerse el despacho por falta de DTE válido.

- Análisis / categoría: Solución / Operación.
- Fuente y EDT: Caso cap. 10; SD4 INT-06/07; T-18 §6.4; 3.3.2, 4.1.2.
- Evaluación inicial: P=4; I=5; D=4; E=20; NPR=80. Horizonte: desde H6 hasta el fin de la operación. P=4 porque toda guía depende del ERP de 2017 y un cambio de carga diario invalida guías preemitidas; D=4 porque la falta de guía válida se aprecia en el andén, cuando ya afecta el despacho.
- Responsable de respuesta: ARQ, con su equipo y contrapartes de su ámbito.
- Disparador: Guía ausente/invalidada o ensayo no termina antes de 05:30.
- Plazo: Antes H6; repetir antes H11.
- Mitigación: Preemisión nocturna, conciliación carga/guía y ensayo de caída ERP con 96 camiones.
- Contingencia: Conservar versión local probada y DTE válidos; Operaciones decide continuidad autorizada con ERP. No emitir documentos alternativos ni reemplazar despacho por papel.
- Evidencia de cierre: Ensayo de 96 salidas sin interrupción, con caída ERP/carga modificada, sin pérdida ni duplicación.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 100,80 HH; residual hipotético con P = 40,00 %: 67,20 HH.
- Riesgo secundario: preemitir guías de noche obliga a reemitirlas si la carga cambia, lo que la conciliación carga–guía debe cubrir.
- Costo-beneficio técnico: control 4.1.2, 80,00 HH del T-15; ahorro hipotético 33,60 HH; retorno 0,42.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-02 — Doble reserva o custodia en la coordinación de reserva

Cortes/reintentos podrían confirmar sin acuse durable o repetir descuentos, alterando stock y trazabilidad.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: SD4, coordinación de reserva y retención de INT-03/04 (apartado 4.1.4.4 y Anexo 4-G); AL-STOCK-01 y AL-ACT-01 (Anexo 4-V); 3.3.6, 3.4.2, 3.4.6, 3.8.1.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: hasta la regresión del H9 y cada cambio de la coordinación de reserva. P=4 porque la reserva se coordina entre sitios que se desconectan y reintentan a diario; D=3 porque la conciliación diaria y AL-STOCK-01 lo detectan, pero después de confirmar.
- Responsable de respuesta: DES, con su equipo y contrapartes de su ámbito.
- Disparador: Confirmación sin acuse, UUID repetido o dos autoridades.
- Plazo: Antes H4; regresión H9.
- Mitigación: Probar concurrencia, UUID, idempotencia, época de autoridad y retención por lote/ubicación.
- Contingencia: Bloquear confirmaciones ambiguas y conciliar colas con un único escritor; continuidad sólo sin degradar despacho.
- Evidencia de cierre: AL-STOCK-01/AL-ACT-01 con cero doble descuento/custodia.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 460,80 HH; residual hipotético con P = 40,00 %: 307,20 HH.
- Riesgo secundario: bloquear las confirmaciones ambiguas puede demorar pedidos durante un corte; se mide en AL-STOCK-01.
- Costo-beneficio técnico: control 3.8.1, 160,00 HH del T-15; ahorro hipotético 153,60 HH; retorno 0,96.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-03 — CD no sostiene 24 horas sin WAN

Dependencias remotas ocultas podrían impedir recibir, preparar o despachar durante desconexión prolongada. El caso describe un solo enlace en Concepción; el SD4 (sección 4.2.5.1) da a cada centro de distribución tres caminos independientes, fibra, LTE y Starlink, y la autonomía de 24 horas cubre la caída simultánea de los tres.

- Análisis / categoría: Solución / Operación.
- Fuente y EDT: Caso cap. 10 y cap. 19; SD4 borde local y sección 4.2.5.1; 6.6.3, 3.8.3, 3.8.5.
- Evaluación inicial: P=3; I=5; D=3; E=15; NPR=45. Horizonte: H5 a H10. P=3 porque el diseño declara 24 horas autónomas, pero una dependencia remota no identificada es plausible; D=3 porque sólo un ensayo de corte completo la revela.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Servicio remoto invocado o cola agotada durante desconexión.
- Plazo: Antes H5; repetir antes H10.
- Mitigación: Ensayar 24 horas sin WAN con procesos completos y reconciliación en Talca y en Concepción, con los tres caminos cortados.
- Contingencia: Mantener autoridad local probada y aislar dependencia; no aprobar corte sin continuidad.
- Evidencia de cierre: 24 horas de operación completa y drenaje sin diferencias inexplicadas.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 96,00 HH; residual hipotético con P = 20,00 %: 48,00 HH.
- Riesgo secundario: ensayar 24 horas sin WAN en un CD real puede afectar la operación del día; se ejecuta en un día permitido y con reversión preparada.
- Costo-beneficio técnico: control 6.6.3, 160,00 HH del T-15; ahorro hipotético 48,00 HH; retorno 0,30.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-04 — Pérdida o duplicación tras 14 horas offline

Dispositivos/reintentos podrían perder pedidos, entregas o cobros al reconectar.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: Caso cap. 10; SD3 operación desconectada; 3.4.6, 3.4.8, 3.4.10, 3.8.3.
- Evaluación inicial: P=4; I=4; D=3; E=16; NPR=48. Horizonte: cada versión móvil hasta el mes 56. P=4 porque 62 preventistas y 96 camiones sincronizan cada día después de tramos sin señal; D=3 porque la diferencia aparece en la conciliación diaria.
- Responsable de respuesta: DES, con su equipo y contrapartes de su ámbito.
- Disparador: Cola no durable, doble acuse o diferencia de cobro.
- Plazo: Antes H5 y cada versión móvil.
- Mitigación: Ensayar 14 horas offline, reinicio, UUID y reconciliación.
- Contingencia: Retener registros durables y bloquear confirmaciones ambiguas sin doble digitación.
- Evidencia de cierre: Registros/cobros completos y únicos al reconectar.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 384,00 HH; residual hipotético con P = 40,00 %: 256,00 HH.
- Riesgo secundario: bloquear las confirmaciones ambiguas al reconectar puede retrasar la rendición del conductor; el retraso se mide en la conciliación diaria.
- Costo-beneficio técnico: control 3.8.3, 320,00 HH del T-15; ahorro hipotético 128,00 HH; retorno 0,40.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-05 — Pérdida del sitio supera RPO

La arquitectura compromete RPO ≤15 min con fibra, LTE y Starlink, a comprobar por escenario. La falla simultánea de los tres caminos seguida de la destrucción del sitio antes de reponer alguno podría eliminar el respaldo local y dejar una copia remota con más de 15 minutos de pérdida. Es el riesgo residual declarado en SD4 4.3.2.4 (RT-02.11).

- Análisis / categoría: Solución / Operación.
- Fuente y EDT: BTT RT-02.11, RT-07.04/07; SD4 4.3.2.4 riesgo residual DR; 3.8.5, 3.9.4, 8.2.7.
- Evaluación inicial: P=3; I=5; D=5; E=15; NPR=75. Horizonte: los 56 meses. P=3 porque exige la falla de los tres caminos de Talca seguida de la destrucción del sitio; D=5 porque la pérdida sólo se reconoce después de ocurrir.
- Responsable de respuesta: ARQ, con su equipo y contrapartes de su ámbito.
- Disparador: Antigüedad remota > 15 minutos o ensayo multisistema fallido.
- Plazo: Ensayar antes H5/H10.
- Mitigación: Aplicar las medidas del SD4 (4.3.2.4): alarmas de retraso de replicación a los 5 y 15 min, reposición del enlace por el proveedor, preemisión de guías al cerrar la carga y conservación local en el NAS WORM de Talca.
- Contingencia: Aplicar DR probado (imagen del WMS de Talca en Fargate de la región activa), recuperar la última copia remota consistente y usar el NAS sólo si sobrevivió al daño, y registrar el incidente con la pérdida efectiva.
- Evidencia de cierre: AL-DR-01 mide RPO ≤ 15 min y RTO ≤ 4 h e identifica la copia remota que sobrevive cuando el NAS se destruye con el sitio; con ella se demuestra la frontera en que se cumple el RPO (RT-07.04) junto con el tratamiento del riesgo residual (RT-02.11). La continuidad del despacho se prueba en un ensayo separado.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 180,48 HH; residual hipotético con P = 20,00 %: 90,24 HH.
- Riesgo secundario: las alarmas de replicación a los 5 minutos pueden dispararse en cortes breves; su umbral se calibra en el ensayo AL-DR-01.
- Costo-beneficio técnico: control 3.8.5, 320,00 HH del T-15; ahorro hipotético 90,24 HH; retorno 0,28.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-06 — Carga y cola de la coordinación de reserva exceden capacidad

La coordinación de reserva y retención del SD4 (apartado 4.1.4.4 y Anexo 4-G) se dimensiona con un máximo de cuatro mensajes por línea de pedido. La retención consumida no se libera, y esa holgura cubre líneas repartidas entre lotes o sitios. Si la multiplicidad medida supera esa cobertura, el tráfico peak podría saturar enlaces o cómputo. La coordinación no se suma al drenaje tras un corte (Anexo 4-W, apartado 4-W.5).

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: SD4, Anexo 4-I, Tabla A.10, y Anexo 4-W, Tablas A.32 y A.33; Caso RT-09.01; AL-STOCK-01; 3.8.4, 3.9.3.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: H5 a H10 y crecimiento anual. P=4 porque las líneas repartidas entre más de un lote o ubicación son habituales; D=3 porque la cola se monitorea, pero su saturación se confirma con prueba de carga.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Más de cuatro mensajes por línea de pedido, cola creciente o latencia incumplida.
- Plazo: Antes H5/H10; vigilancia mensual.
- Mitigación: AL-STOCK-01 mide la proporción de líneas con más de una retención y de retenciones liberadas. Las pruebas 3.8.4 y 3.9.3 verifican 1,5 veces el peak, el crecimiento y el drenaje, sin sumar la coordinación al drenaje tras un corte.
- Contingencia: Priorizar transacciones y limitar tráfico auxiliar; escalar capacidad por arquitectura sin reducir volumen obligatorio.
- Evidencia de cierre: Carga/latencias y drenaje conformes a multiplicidad medida.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 115,20 HH; residual hipotético con P = 40,00 %: 76,80 HH.
- Riesgo secundario: limitar el tráfico auxiliar en el peak retrasa reportes y portales; la prioridad se declara por clase de transacción.
- Costo-beneficio técnico: control 3.8.4, 320,00 HH del T-15; ahorro hipotético 38,40 HH; retorno 0,12.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-07 — Ataque o exposición de datos críticos

Móviles, portales y terceros podrían permitir acceso indebido, ransomware o alteración de lotes/cobros.

- Análisis / categoría: Solución / Seguridad.
- Fuente y EDT: BTT seguridad cap. 13; SD4 seguridad; 3.3.1, 3.8.6, 3.9.5, 8.2.2. El impacto se mide sobre el trabajo de seguridad que un incidente obliga a rehacer: controles construidos, pruebas ofensivas y mantenimiento de ciberseguridad. El monitoreo del SOC (8.1.5) es el control que detecta el evento y no se rehace.
- Evaluación inicial: P=4; I=5; D=4; E=20; NPR=80. Horizonte: los 56 meses. P=4 porque portales, móviles e integraciones con terceros están expuestos de forma permanente; D=4 porque un acceso indebido puede reconocerse recién en la revisión del SIEM.
- Responsable de respuesta: SEG, con su equipo y contrapartes de su ámbito.
- Disparador: Vulnerabilidad crítica/alta o acceso entre clientes.
- Plazo: Antes H5/H10; vigilancia continua.
- Mitigación: Pruebas ofensivas, mínimo privilegio, aislamiento, registro y rotación de credenciales.
- Contingencia: Contener acceso, preservar evidencia y recuperar entorno limpio con continuidad probada.
- Evidencia de cierre: Sin defectos de seguridad críticos/altos abiertos y prueba de recuperación.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 380,16 HH; residual hipotético con P = 40,00 %: 253,44 HH.
- Riesgo secundario: las pruebas ofensivas sobre Preproducción pueden degradar un ambiente compartido; se programan fuera de las ventanas de certificación.
- Costo-beneficio técnico: control 3.8.6, 160,00 HH del T-15; ahorro hipotético 126,72 HH; retorno 0,79.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-08 — Bloqueo por proveedor

Dependencias AWS, mapas, mensajería y ERP podrían impedir sustitución o extracción y comprometer salida y continuidad.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: Aclaraciones §11, 8.2; SD4 híbrida; 2.1, 3.3,3.11, 9.2.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: diseño H2/H8 y salida del mes 56. P=3 porque varias dependencias tienen un solo proveedor; D=3 porque se detecta en el ensayo anual de extracción y restauración.
- Responsable de respuesta: ARQ, con su equipo y contrapartes de su ámbito.
- Disparador: Exportación/restauración falla o restricción contractual.
- Plazo: Diseño en el H2 y el H8; ensayo anual y salida en el mes 56.
- Mitigación: Inventariar dependencias, contratos y formatos; ensayar extracción/restauración.
- Contingencia: Usar copias portables e interfaces desacopladas; alternativa mediante control de cambios.
- Evidencia de cierre: Exportación/restauración reproducibles y documentación CLIENTE.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 352,00 HH; residual hipotético con P = 20,00 %: 176,00 HH.
- Riesgo secundario: mantener formatos portables limita el uso de servicios administrados propios del proveedor; el Comité de Arquitectura decide cada excepción.
- Costo-beneficio técnico: control 1.7.1, 8.1.4, 9.2.1, 448,00 HH del T-15; ahorro hipotético 176,00 HH; retorno 0,39.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-09 — Obsolescencia durante 56 meses

Versiones o dispositivos podrían quedar sin soporte e introducir vulnerabilidades/incompatibilidad.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: Aclaraciones §11, 8.2; SD4; BTT mantenimiento; 8.2.2, 8.2.3, 8.2.4.
- Evaluación inicial: P=4; I=4; D=2; E=16; NPR=32. Horizonte: los 56 meses. P=4 porque varias versiones de la arquitectura terminan su soporte dentro del contrato; D=2 porque esas fechas se conocen y se revisan mensualmente.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Fin de soporte en horizonte o actualización bloqueada.
- Plazo: Inventario H2; revisión mensual operación.
- Mitigación: Inventariar versiones/soporte y ensayar compatibilidad en QA.
- Contingencia: Aislar componente y migrar a versión probada en fechas permitidas.
- Evidencia de cierre: Versiones soportadas y regresión sin degradación E1/E2.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 552,96 HH; residual hipotético con P = 40,00 %: 368,64 HH.
- Riesgo secundario: actualizar versiones durante el contrato puede introducir regresiones; cada actualización pasa la regresión de QA y respeta las fechas prohibidas.
- Costo-beneficio técnico: control 8.2.5, 288,00 HH del T-15; ahorro hipotético 184,32 HH; retorno 0,64.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-10 — Interfaces no documentadas exigen retrabajo

El levantamiento podría descubrir formatos/restricciones no representados en prototipos y atrasar ERP/telemetría.

- Análisis / categoría: Desarrollo / Técnico.
- Fuente y EDT: Caso §17.5; SD7 D-02; 1.2.3, 3.3.2, 3.3.5.
- Evaluación inicial: P=4; I=4; D=3; E=16; NPR=48. Horizonte: hasta el H4. P=4 porque el caso declara interfaces del sistema de gestión sin documentación; D=3 porque se revela en prototipos y pruebas de integración.
- Responsable de respuesta: ARQ, con su equipo y contrapartes de su ámbito.
- Disparador: Contrato incompleto en el mes 3 o conexión fallida.
- Plazo: Antes H2; integración H4.
- Mitigación: Capturar muestras/horarios y probar contratos y errores temprano.
- Contingencia: Priorizar interfaz con capacidad adicional explícita; no usar reserva posterior a H5.
- Evidencia de cierre: Contratos y pruebas positivas/negativas con volumen representativo.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 124,80 HH; residual hipotético con P = 40,00 %: 83,20 HH.
- Riesgo secundario: dar capacidad adicional a una interfaz atrasada desplaza otra; JP registra el traslado contra la reserva del hito.
- Costo-beneficio técnico: control 1.2.3, 80,00 HH del T-15; ahorro hipotético 41,60 HH; retorno 0,52.
- Base cuantitativa: Tabla B.3; cargo compartido G-INT (Tabla B.2).

### R8-11 — Productividad o dotación inferior al modelo

Clases HH/128 HH efectivas no medidas podrían subestimar esfuerzo y especialistas, afectando hitos.

- Análisis / categoría: Desarrollo / Proyecto.
- Fuente y EDT: T-15 §§4/5; SD1 dotación declarada; 162 paquetes con entregable de implementación, enumerados en B.3.1; control 1.3.4.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: hasta el H12; construcción E1, solapamiento y desarrollo E2. P=4 porque los tamaños por clase y las plantillas de actividades aún no se contrastan con la productividad real, el cronograma por actividad usa toda la división de desarrollo entre julio y septiembre de 2027 y la dotación declarada no cubre SEG ni IMP sin contratación (T-15 §5.7); D=3 porque el valor ganado mensual lo detecta con un mes de atraso.
- Responsable de respuesta: JP, con su equipo y contrapartes de su ámbito.
- Disparador: Estimación supera capacidad por rol/subventana o personas no asignadas.
- Plazo: Antes línea base; semanal.
- Mitigación: Refinar con el equipo la estimación por clase, trazada al T-12 y a las cantidades del T-11; asignar competencias y relevos; comprobar el peak de 69 (mes 15), las 48 personas simultáneas de desarrollo y la dotación declarada (T-15 §5.7); vigilar semanalmente la reserva de cada hito (T-15, Tabla 5.2).
- Contingencia: Reordenar dentro de hitos y sustentar capacidad adicional; no prestar E1 a E2.
- Evidencia de cierre: Asignaciones nominales y cero sobreasignación por subventana.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 8.107,20 HH; residual hipotético con P = 40,00 %: 5.404,80 HH.
- Riesgo secundario: reforzar el equipo con personas nuevas reduce la productividad inicial por la inducción; ese efecto se incorpora a la estimación por clase.
- Costo-beneficio técnico: control 1.3.4, 80,00 HH del T-15; ahorro hipotético 2.702,40 HH; retorno 33,78.
- Base cuantitativa: Tabla B.3; cargo compartido G-CAP (Tabla B.2).

### R8-12 — Contrapartes CLIENTE no disponibles

TI de cuatro personas y gerencias podrían no atender decisiones, pruebas o actas a tiempo.

- Análisis / categoría: Desarrollo / Organizacional.
- Fuente y EDT: Caso cap. 10; Aclaraciones §11, 8.2; 1.1.3, 1.8,2.4, 7.3.
- Evaluación inicial: P=4; I=4; D=2; E=16; NPR=32. Horizonte: hasta el H12. P=4 porque el equipo de TI del CLIENTE tiene cuatro personas y atiende la operación; D=2 porque cada revisión tiene fecha registrada y su vencimiento se detecta ese día.
- Responsable de respuesta: JP, con su equipo y contrapartes de su ámbito.
- Disparador: Decisión/revisión no atendida en fecha acordada.
- Plazo: Agenda en el mes 1; cada comité quincenal.
- Mitigación: Reservar agenda, responsable/suplente y material por decisión. En el H1 y el H8, cuya reserva (6 y 4 días hábiles) es menor que los diez días de subsanación del Art. 18.3, el borrador del entregable se revisa con la Contraparte Técnica una semana antes de la entrega formal, para que las observaciones lleguen antes de la revisión de diez días.
- Contingencia: Escalar a patrocinador y avanzar tareas independientes; silencio no es aceptación. Si el H1 o el H8 reciben observaciones formales, el equipo del entregable (2 ARQ en el H1, 5 en el H8) subsana en cinco días hábiles, la mitad del plazo del Art. 18.3, para que el acta quede dentro del mes del Formulario E-25.
- Evidencia de cierre: Decisiones/actas explícitas con responsables y fechas.
- Estrategia: Escalar, porque la decisión depende del CLIENTE y excede la autoridad del JP.
- Efecto esperado y residual: VE individual 486,72 HH; residual hipotético con P = 40,00 %: 324,48 HH.
- Riesgo secundario: escalar decisiones al patrocinador puede tensionar la relación con la Contraparte Técnica; se escala sólo contra la agenda acordada en el mes 1.
- Costo-beneficio técnico: control 1.1.1, 80,00 HH del T-15; ahorro hipotético 162,24 HH; retorno 2,03.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-13 — Conocimiento de ruteo no transferido

Ausencia o jubilación podría ocurrir antes de capturar/validar excepciones operativas.

- Análisis / categoría: Desarrollo / Organizacional.
- Fuente y EDT: Caso cap. 18, resultado 16; SD7 D-03; 1.2.2, 3.4.7.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: hasta las dos semanas sin planificador de la marcha blanca E1 (R18-16). P=3 porque el caso prevé la jubilación del planificador; D=3 porque se detecta en la validación del mes 3 y en la prueba sin planificador.
- Responsable de respuesta: IMP, con su equipo y contrapartes de su ámbito.
- Disparador: Reglas no validadas en el mes 3 o rutas no operables.
- Plazo: Captura meses 1–3; probar antes H7.
- Mitigación: Capturar reglas/excepciones y validar con planificador y suplente.
- Contingencia: Suplente entrenado y reglas versionadas; evitar dependencia permanente de don Hugo.
- Evidencia de cierre: Dos semanas sin planificador y OTIF conforme.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 83,20 HH; residual hipotético con P = 20,00 %: 41,60 HH.
- Riesgo secundario: el suplente capacitado puede no tener la autoridad informal del planificador; IMP valida las reglas con los jefes de despacho.
- Costo-beneficio técnico: control 1.2.2, 80,00 HH del T-15; ahorro hipotético 41,60 HH; retorno 0,52.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-14 — E2 consume capacidad protegida E1

El solapamiento podría reasignar corrección E1, degradarla o retrasar E2.

- Análisis / categoría: Desarrollo / Proyecto.
- Fuente y EDT: BA Art. 17.2; T-15 reserva; 4.2.2, 3.5,3.9.
- Evaluación inicial: P=4; I=5; D=2; E=20; NPR=40. Horizonte: meses 13 a 20. P=4 porque E1 y E2 requieren a los mismos especialistas durante el solapamiento; D=2 porque la imputación separada de horas lo muestra en la semana.
- Responsable de respuesta: DES, con su equipo y contrapartes de su ámbito.
- Disparador: Persona compartida o reserva cargada a E2.
- Plazo: Antes del mes 13; semanal hasta el mes 20.
- Mitigación: Separar equipos y proteger 256 HH de DES y 128 HH de CAL al mes para la Etapa 1.
- Contingencia: Restituir E1 y justificar ampliación E2; no duplicar reserva.
- Evidencia de cierre: Equipos/capacidad independientes y métricas E1 sostenidas.
- Estrategia: Mitigar. Separar y vigilar equipos reduce la reasignación indebida; no elimina toda competencia por especialistas.
- Efecto esperado y residual: VE individual 1.008,00 HH; residual hipotético con P = 40,00 %: 672,00 HH.
- Riesgo secundario: separar los equipos de la Etapa 1 y la Etapa 2 exige más personas a la vez y alimenta R8-11.
- Costo-beneficio técnico: control 1.3.4, 80,00 HH del T-15; ahorro hipotético 336,00 HH; retorno 4,20.
- Base cuantitativa: Tabla B.3; cargo compartido G-CAP (Tabla B.2).

### R8-15 — Perfiles EDI no certificados a tiempo

Dependencia de cadenas podría impedir activar todo el alcance antes de los 28 días finales o de enero de 2029.

- Análisis / categoría: Desarrollo / Proyecto.
- Fuente y EDT: Caso §13.2; SD7 3.6.5/6; T-18 6.2; 3.5.1, 3.6.5, 3.6.6.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: hasta el mes 21. P=4 porque depende de cadenas externas con calendarios propios; D=3 porque el estado de certificación se sigue por perfil.
- Responsable de respuesta: DES, con su equipo y contrapartes de su ámbito.
- Disparador: Perfil sin ambiente/acuse o fecha prevista posterior a F−28 días.
- Plazo: Principal antes H10; todas antes activación/F−28 días.
- Mitigación: Acordar pruebas temprano y registrar todos los perfiles/aprobaciones.
- Contingencia: Carga asistida es contingencia auxiliar, no EDI; recuperar sin excluir cadenas.
- Evidencia de cierre: Aprobaciones por cadena y 100 % del alcance durante cuatro semanas.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 345,60 HH; residual hipotético con P = 40,00 %: 230,40 HH.
- Riesgo secundario: acordar pruebas tempranas con las cadenas exige ambientes EDI antes de terminar los módulos de la Etapa 2; se prueban contra el contrato de la interfaz.
- Costo-beneficio técnico: control 2.1.4, 240,00 HH del T-15; ahorro hipotético 115,20 HH; retorno 0,48.
- Base cuantitativa: Tabla B.3; cargo compartido G-INT (Tabla B.2).

### R8-16 — Migración altera saldos o pierde lotes

Datos WMS/planillas con vacíos podrían trasladar existencias incorrectas e invalidar conciliación/trazabilidad.

- Análisis / categoría: Desarrollo / Técnico.
- Fuente y EDT: SD3 3.4.4; SD7 D-24; 3.7.1–5.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: hasta el corte de migración. P=4 porque el WMS de 2013 y las planillas tienen vacíos de lote; D=3 porque los ensayos de migración lo detectan en la conciliación.
- Responsable de respuesta: DAT, con su equipo y contrapartes de su ámbito.
- Disparador: Lote requerido ausente o diferencia inexplicada.
- Plazo: Dos ensayos antes corte/H6.
- Mitigación: Perfilar/conteo y dos ensayos; reconciliar SKU, lote y ubicación.
- Contingencia: Retener corte y corregir origen; WMS sólo lectura, sin doble escritura.
- Evidencia de cierre: Ensayos/corte con diferencias explicadas y trazabilidad completa.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 432,00 HH; residual hipotético con P = 40,00 %: 288,00 HH.
- Riesgo secundario: retener el corte por diferencias acerca la migración al inicio de la marcha blanca; el corte se programa con margen antes del acta del H6.
- Costo-beneficio técnico: control 3.7.1, 480,00 HH del T-15; ahorro hipotético 144,00 HH; retorno 0,30.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-17 — Fecha efectiva elimina ventanas permitidas

Inicio distinto del supuesto podría coincidir con congelamientos o impedir la producción de la Etapa 2 antes de enero de 2029.

- Análisis / categoría: Implantación / Proyecto.
- Fuente y EDT: Caso cap. 10/13.2; SD3 V-12; BA Art. 17; 1.1.3, 1.3.1, 4.1.3.
- Evaluación inicial: P=4; I=5; D=2; E=20; NPR=40. Horizonte: hasta el mes 1. P=4 porque la fecha no está confirmada y las ventanas permitidas son estrechas; D=2 porque el calendario se recalcula al confirmar V-12.
- Responsable de respuesta: JP, con su equipo y contrapartes de su ámbito.
- Disparador: Calendario sin días permitidos/28 días de evidencia.
- Plazo: Mes 1, antes del H1; antes del H6 y del H11.
- Mitigación: Convertir meses a fechas con feriados CLIENTE/prohibiciones.
- Contingencia: Reordenar dentro de períodos; escalar incompatibilidad sin presumir prórroga.
- Evidencia de cierre: Calendario compatible con hitos y evidencia completa.
- Estrategia: Escalar, porque la decisión depende del CLIENTE y excede la autoridad del JP.
- Efecto esperado y residual: VE individual 43,20 HH; residual hipotético con P = 40,00 %: 28,80 HH.
- Riesgo secundario: recalcular el calendario al confirmar la fecha puede mover olas a días prohibidos; JP lo revisa en el Comité de Proyecto antes de aprobar la línea base.
- Costo-beneficio técnico: control 1.1.3, 80,00 HH del T-15; ahorro hipotético 14,40 HH; retorno 0,18.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-18 — Marcha blanca no cumple seis condiciones

Defecto alto, volumen incompleto o diferencias podrían persistir en cierre e impedir aceptación. En la Etapa 2, las semanas de cierre caen en el peak de Fiestas Patrias de septiembre de 2028, con cerca de 2.600 entregas diarias y congelamiento del 1 al 25 (SD7, sección 7.3.5).

- Análisis / categoría: Implantación / Operación.
- Fuente y EDT: BA Arts. 17.3 y 18; Caso cap. 19; SD7 7.3.5; T-18; 4.2.1, 4.3.1, 7.3, 3.9.3.
- Evaluación inicial: P=4; I=5; D=2; E=20; NPR=40. Horizonte: cada marcha blanca. P=4 porque las seis condiciones son copulativas y se miden con volumen real; D=2 porque los indicadores son diarios.
- Responsable de respuesta: CAL, con su equipo y contrapartes de su ámbito.
- Disparador: Una condición falla o grupo fuera del alcance.
- Plazo: Diario marcha blanca; H7/H12.
- Mitigación: Activar todo antes de F−28 días y demostrar las seis condiciones simultáneas; en la Etapa 2, habilitar todo en agosto y demostrar la carga a 1,5 veces el peak con ambas etapas activas antes del H11 (3.9.3).
- Contingencia: Extender cuatro semanas el acompañamiento, a costo del adjudicatario y sin mover las fases siguientes, con la opción de hasta 8 personas adicionales del contrato de implantación (E8-14); no firmar cumplimiento ficticio.
- Evidencia de cierre: 28 días completos, cero críticos/altos, conciliación, usuarios certificados y acta.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 2.956,80 HH; residual hipotético con P = 40,00 %: 1.971,20 HH.
- Riesgo secundario: extender una marcha blanca a costo del adjudicatario sin mover las fases siguientes presiona la capacidad del solapamiento (R8-14).
- Costo-beneficio técnico: control 4.1.1, 7.3.1, 7.3.2, 400,00 HH del T-15; ahorro hipotético 985,60 HH; retorno 2,46.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-19 — Suministros o sala fuera de secuencia

LafroX especifica y compra la sala técnica, los racks, los servidores y los gabinetes de borde mediante la orden de compra del mes 2 (5.1.2). La instalación de la sala empieza en el mes 3 y su recepción ocurre en el mes 4. El CLIENTE compra solo el hardware de terreno antes de cada ola. Una compra, recepción o configuración tardía podría bloquear el H3 o una ola pese a HH disponibles.

- Análisis / categoría: Implantación / Proyecto.
- Fuente y EDT: BTT recinto; Caso cap. 11; SD7 D-09–13/26; 5.1.2, 6.1,6.3, 6.6.3, 6.5.
- Evaluación inicial: P=3; I=5; D=3; E=15; NPR=45. Horizonte: hasta el H3. P=3 porque LafroX debe emitir su orden de compra en el mes 2 para iniciar la instalación en el mes 3 y el suministro depende de proveedores externos; D=3 porque las actas de recepción lo revelan.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Orden de compra de LafroX no emitida al cierre del mes 2, suministro posterior al montaje o dispositivo de terreno ausente antes de la ola.
- Plazo: Sala, racks y borde antes H3; terreno antes ola.
- Mitigación: Acordar en el mes 1 el calendario de compra del hardware de terreno del CLIENTE (1.1.3 y 5.1.3). LafroX emite su orden de compra en el mes 2 (5.1.2) y recibe el suministro antes de montar. Las actas 5.1.3 registran la recepción técnica del terreno comprado por el CLIENTE y de la infraestructura provista por LafroX.
- Contingencia: Recuperar suministro/instalación con capacidad específica; no activar equipos inexistentes.
- Evidencia de cierre: Actas y pruebas en secuencia sala, racks, borde y terreno.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 316,80 HH; residual hipotético con P = 20,00 %: 158,40 HH.
- Riesgo secundario: comprar con anticipación hace correr la garantía antes del uso; los plazos de garantía se registran con R8-09.
- Costo-beneficio técnico: control 5.1.2, 5.1.3, 160,00 HH del T-15; ahorro hipotético 158,40 HH; retorno 0,99.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-20 — Rotación y resistencia reducen adopción

Rotación 38 % de preparación y personal antiguo podrían dejar turnos sin usuarios certificados.

- Análisis / categoría: Implantación / Organizacional.
- Fuente y EDT: Caso restricciones; T-18; 7.1.2, 7.2.1, 7.3.1/2.
- Evaluación inicial: P=4; I=4; D=3; E=16; NPR=48. Horizonte: los 56 meses. P=4 porque el turno de noche rota 38 % al año; D=3 porque la certificación por usuario lo detecta antes de cada turno.
- Responsable de respuesta: IMP hasta el mes 21; Guillermo Castillo (SRE) desde el mes 22. IMP conserva la familia de esfuerzo. CAL verifica certificación.
- Disparador: Usuario sin certificar o uso incompleto.
- Plazo: Antes cada ola; mensual.
- Mitigación: Tutor por turno, certificación en puesto y acompañamiento con relevos.
- Contingencia: Retener/restaurar acompañamiento y repetir formación sin detener rutas.
- Evidencia de cierre: Usuarios por perfil/turno certificados y uso sostenido.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 395,52 HH; residual hipotético con P = 40,00 %: 263,68 HH.
- Riesgo secundario: el tutor por turno retira a un preparador experimentado de su puesto; se compensa con relevos del acompañamiento.
- Costo-beneficio técnico: control 7.3.1, 7.3.2, 320,00 HH del T-15; ahorro hipotético 131,84 HH; retorno 0,41.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-21 — Transportistas o sindicato rechazan dispositivos

Vehículos externos y objeciones al GPS podrían impedir sensores o captura en rutas. La solución no instala cámaras en cabina (SD3, sección 3.4.6); el acuerdo con el sindicato cubre los terminales y el uso del GPS para control de jornada.

- Análisis / categoría: Implantación / Organizacional.
- Fuente y EDT: Caso restricciones; SD3 S-28; SD7 acuerdos; 5.4.1, 5.4.2, 6.5.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: hasta la ola de reparto. P=3 porque el caso registra objeciones a GPS y cámaras; D=3 porque el acta exigida antes de la ola lo revela.
- Responsable de respuesta: IMP, con su equipo y contrapartes de su ámbito.
- Disparador: Acuerdo ausente o ruta sin dispositivo requerido.
- Plazo: Antes ola de reparto.
- Mitigación: Acordar instalación, uso, finalidad y acceso con CLIENTE, terceros y sindicato.
- Contingencia: Escalar acuerdos; atención auxiliar no reemplaza registro térmico ni excluye rutas.
- Evidencia de cierre: Acuerdos/pruebas en toda flota y rutas requeridas.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 89,60 HH; residual hipotético con P = 20,00 %: 44,80 HH.
- Riesgo secundario: limitar la finalidad del GPS a la jornada y la ruta puede restringir datos útiles para el ruteo; la finalidad se acuerda con el CLIENTE.
- Costo-beneficio técnico: control 5.4.1, 5.4.2, 160,00 HH del T-15; ahorro hipotético 44,80 HH; retorno 0,28.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-22 — Mesa cubre horario pero no SLA

La mesa base del T-15 (8.1.2) cubre los tres niveles de servicio hasta 2.283 contactos al mes con las posiciones dimensionadas con Erlang C (SD4, Anexo 4-W.7). Esas posiciones podrían no bastar si la demanda o el tiempo de atención superan el supuesto, y el modelo no verifica el abandono ≤ 5 % ni la resolución al primer contacto ≥ 70 %.

- Análisis / categoría: Implantación / Operación.
- Fuente y EDT: BTT RT-21.06/07; Caso RT-21.06; 4.2.2, 8.1.1, 8.1.2.
- Evaluación inicial: P=4; I=4; D=3; E=16; NPR=48. Horizonte: meses 13 a 56. P=4 porque la demanda de 2.000 contactos/mes es una estimación sin medición y la del año 3 queda a 1,1 % del límite de 2.283; D=3 porque la medición por contacto empieza en la marcha blanca.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: >2.200 contactos/mes activa tercer agente valle; >2.391, distinta mezcla/tiempo de atención o falta de relevo exige redimensionamiento por franja.
- Plazo: Antes del H7 (mes 16) y del H12 (mes 21); diario peaks.
- Mitigación: Medir la demanda por intervalo y los agentes y competencias; 04:00–22:00 de lunes a sábado y 24×7 en peaks y críticos.
- Contingencia: tercer agente valle y guardia especialista. Elegir el menor c por franja con A<c y SL(20 s) ≥80 % mediante Erlang C; asignar capacidad y medir abandono ≤5 % y resolución inicial ≥70 % aparte. Escalar incumplimiento inmediatamente.
- Evidencia de cierre: Prueba de demanda/turnos con los tres SLA y horarios.
- Estrategia: Aceptar activamente, porque se dimensiona una primera respuesta condicionada a demanda real; se reserva la contingencia con disparador.
- Efecto esperado y residual: VE individual 11.699,40 HH; la aceptación activa conserva P = 60,00 %, por lo que el residual es igual al inicial.
- Riesgo secundario: un tercer agente en las franjas valle baja la ocupación de la mesa; su permanencia se revisa con la demanda medida.
- Costo-beneficio técnico: control medición dentro de 8.1.2, 0,00 HH del T-15; ahorro hipotético 0,00 HH; retorno no aplicable.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-23 — Frío o sensores no producen evidencia íntegra

−22 °C, falta de señal o deriva podrían dejar lotes sin historial térmico válido.

- Análisis / categoría: Solución / Operación.
- Fuente y EDT: Caso restricciones; SD3 M9/M12; 3.4.5, 6.5,3.8.3.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: los 56 meses. P=4 porque el congelado a −22 °C y los tramos sin señal son recurrentes; D=3 porque las lecturas faltantes aparecen en la conciliación.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Lectura faltante, deriva o dispositivo falla.
- Plazo: Antes de la ola 1 y de la de reparto; continuo.
- Mitigación: Probar autonomía, almacenamiento/calibración y asociación sensor, lote y tiempo.
- Contingencia: Calidad retiene lote sin evidencia y utiliza reemplazo probado.
- Evidencia de cierre: Serie completa y asociada al lote; ensayo a −22 °C y sin señal.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 403,20 HH; residual hipotético con P = 40,00 %: 268,80 HH.
- Riesgo secundario: calibrar los sensores los retira de servicio; se mantiene un stock de reemplazo probado.
- Costo-beneficio técnico: control 6.5.3, 160,00 HH del T-15; ahorro hipotético 134,40 HH; retorno 0,84.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-24 — Filtración en telemetría o reproducción

Datos de ubicación, clientes y cobros podrían circular sin minimización en trazas de incidentes.

- Análisis / categoría: Solución / Seguridad.
- Fuente y EDT: SD4 seguridad; SD7 INN-02; 3.10.2, 3.3.1, 3.8.6.
- Evaluación inicial: P=3; I=5; D=3; E=15; NPR=45. Horizonte: los 56 meses. P=3 porque reproducir un incidente requiere copiar datos de terreno; D=3 porque la minimización se revisa en cada conjunto.
- Responsable de respuesta: SEG, con su equipo y contrapartes de su ámbito.
- Disparador: Datos personales/secretos en conjunto de reproducción.
- Plazo: Antes usar trazas; cada versión.
- Mitigación: Enmascarar, controlar acceso/retención y revisar conjuntos.
- Contingencia: Suspender conjunto afectado, contener y producir muestra protegida.
- Evidencia de cierre: Inspección de datos/permisos sin exposición indebida.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 192,00 HH; residual hipotético con P = 20,00 %: 96,00 HH.
- Riesgo secundario: enmascarar los conjuntos de reproducción puede ocultar la causa de un incidente; CAL valida que el conjunto siga siendo útil (R8-26).
- Costo-beneficio técnico: control 3.8.6, 160,00 HH del T-15; ahorro hipotético 96,00 HH; retorno 0,60.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-25 — INN-01 no logra seguimiento posentrega

Los avisos podrían no confirmarse en la visita, porque el ritmo de reposición del canal tradicional es irregular, o no tener una acción posible si falta el catálogo de canje; la innovación perdería credibilidad ante preventistas y almaceneros.

- Análisis / categoría: Implantación / Organizacional.
- Fuente y EDT: SD7 Anexo 7.D INN-01; BTT RT-26.04; 3.10.1, 7.2.1.
- Evaluación inicial: P=4; I=3; D=3; E=12; NPR=36. Horizonte: piloto y validación de INN-01. P=4 porque las compras del canal tradicional son irregulares y el saldo en el local solo se estima; D=3 porque el indicador del piloto (I-01A) lo muestra.
- Responsable de respuesta: IMP, con su equipo y contrapartes de su ámbito.
- Disparador: Avisos con riesgo confirmado bajo el 70 % de los evaluables, o aviso sin acción disponible en el catálogo.
- Plazo: Piloto meses 11–15.
- Mitigación: Piloto asistido; no liberar sin cumplir I-01A; mostrar la confianza de cada aviso y confirmar el saldo en la visita; catálogo aprobado como condición de activación; sin exigir conexión al almacenero.
- Contingencia: Degradar a aviso solo por vida útil remanente del lote, sin estimar el ritmo; mantener trazabilidad lote/entrega y escalar a Comercial.
- Evidencia de cierre: Resultado frente a objetivo previo y decisión de adopción.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 67,20 HH; residual hipotético con P = 40,00 %: 44,80 HH.
- Riesgo secundario: degradar el aviso a sólo vida útil reduce su valor comercial; Comercial decide si mantiene el piloto.
- Costo-beneficio técnico: control 3.10.1.4, 240,00 HH del T-15; ahorro hipotético 22,40 HH; retorno 0,09.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-26 — INN-02 no reproduce fallas relevantes

Registros incompletos podrían impedir reproducir incidentes offline y diagnosticar defectos. Causa secundaria: la captura de evidencia podría consumir batería o datos del terminal.

- Análisis / categoría: Desarrollo / Técnico.
- Fuente y EDT: SD7 Anexo 7.D INN-02; BTT RT-26.04; 3.10.2, 8.3.1.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: meses 11 a 56. P=3 porque registros incompletos de terreno son plausibles; D=3 porque se detecta al intentar reproducir un caso.
- Responsable de respuesta: CAL, con su equipo y contrapartes de su ámbito.
- Disparador: Caso representativo no reproducible.
- Plazo: Validación meses 11–15; operación.
- Mitigación: Ensayar corte, reinicio y reintento con conjuntos protegidos; cupo de tamaño y frecuencia de captura.
- Contingencia: Conservar diagnóstico y regresión base con trazas protegidas.
- Evidencia de cierre: Reproducción y diagnóstico contrastados.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 122,88 HH; residual hipotético con P = 20,00 %: 61,44 HH.
- Riesgo secundario: capturar evidencia de terreno crea el riesgo de filtración R8-24.
- Costo-beneficio técnico: control 3.10.2.4, 240,00 HH del T-15; ahorro hipotético 61,44 HH; retorno 0,26.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-27 — INN-03 estima vida remanente insegura

Historia incompleta o mala calibración podría sugerir una vida útil no segura. Causa secundaria: Operaciones podría leer la estimación como permiso para relajar la regla graduada RNG-04.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: SD7 INN-03; SD3 M9/M12; BTT RT-26.04; 3.10.3, 8.3.2.
- Evaluación inicial: P=4; I=5; D=4; E=20; NPR=80. Horizonte: los 56 meses. P=4 porque la calibración inicial tiene poca historia térmica; D=4 porque un error de estimación puede reconocerse sólo cuando el producto se reclama.
- Responsable de respuesta: DAT hasta el mes 21; Guillermo Castillo (SRE) desde el mes 22. DAT conserva la familia de esfuerzo. Miño/Calidad aprueban parámetros sanitarios.
- Disparador: Resultado fuera de criterio Calidad o historial faltante.
- Plazo: Antes del uso en los meses 11–15; revisión en los meses 26, 32, 38, 44, 50 y 56.
- Mitigación: Validar con Calidad y regla conservadora; no ampliar vencimiento por inferencia; la regla graduada y el bloqueo de B-02 no cambian.
- Contingencia: Deshabilitar recomendación y mantener vencimiento/control sanitario.
- Evidencia de cierre: Validación Calidad con trazabilidad modelo/datos.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 224,64 HH; residual hipotético con P = 40,00 %: 149,76 HH.
- Riesgo secundario: Operaciones podría leer la estimación como permiso para relajar la regla RNG-04.
- Costo-beneficio técnico: control 3.10.3.4, 240,00 HH del T-15; ahorro hipotético 74,88 HH; retorno 0,31.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-28 — INN-04 medición variable genera disputa

Costo de servir incompleto podría distorsionar línea base/liquidación variable.

- Análisis / categoría: Implantación / Proyecto.
- Fuente y EDT: SD7 INN-04; BA Art. 50.2; BTT RT-26.04; 5.4.3, 8.3.3, 8.3.4.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: meses 21 a 56. P=3 porque la atribución de costos admite interpretaciones; D=3 porque las tres liquidaciones sombra la ponen a prueba.
- Responsable de respuesta: JP, con su equipo y contrapartes de su ámbito.
- Disparador: Diferencia inexplicada o liquidaciones sombra no reproducibles.
- Plazo: Modelo en los meses 17–20; liquidaciones sombra en los meses 21–23; antes del mes 24.
- Mitigación: Acordar fórmula, datos y auditoría; valores sólo en Oferta Económica.
- Contingencia: Mecanismo contractual de resolución y corrección; sin modificar SLA ni inventar tarifa.
- Evidencia de cierre: Línea base y tres liquidaciones sombra reconciliadas.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 55,04 HH; residual hipotético con P = 20,00 %: 27,52 HH.
- Riesgo secundario: las liquidaciones sombra exigen datos de costo antes del mes 21; DAT los prepara en el paquete 5.4.3.
- Costo-beneficio técnico: control 5.4.3, 80,00 HH del T-15; ahorro hipotético 27,52 HH; retorno 0,34.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-29 — INN-05 baja adopción de hoja del almacenero

La hoja podría no ser comprensible o útil y quedar sin uso. Causa secundaria: el bloque 4 comparativo podría permitir inferir las cifras de un local vecino.

- Análisis / categoría: Implantación / Organizacional.
- Fuente y EDT: SD7 INN-05; Caso canal tradicional; BTT RT-26.04; 3.10.4, 8.3.5, 8.3.6.
- Evaluación inicial: P=4; I=3; D=2; E=12; NPR=24. Horizonte: piloto de INN-05. P=4 porque muchos almaceneros no usan herramientas digitales; D=2 porque las métricas de uso se ven cada semana.
- Responsable de respuesta: IMP hasta el mes 21; Guillermo Castillo (SRE) desde el mes 22. IMP conserva la familia de esfuerzo. Catalán aprueba privacidad del bloque 4.
- Disparador: Uso/beneficio menor al objetivo acordado antes piloto.
- Plazo: Piloto en la Etapa 2; evaluar en los meses 24–27.
- Mitigación: Co-diseño/piloto asistido o papel; preservar preventista y efectivo; umbral mínimo de locales y supresión de celdas en el bloque 4, con revisión legal previa.
- Contingencia: Retirar mejora opcional mediante gobierno manteniendo compromisos y canal obligatorio.
- Evidencia de cierre: Utilidad/uso contrastados y decisión documentada.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 67,20 HH; residual hipotético con P = 40,00 %: 44,80 HH.
- Riesgo secundario: la alternativa en papel duplica la entrega de la hoja; se limita al piloto.
- Costo-beneficio técnico: control 3.10.4.1, 8.3.6, 320,00 HH del T-15; ahorro hipotético 22,40 HH; retorno 0,07.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-30 — Crecimiento o nuevo CD supera parametrización

CD eventual en 2030 o crecimiento distinto por sitio podría superar capacidades.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: Caso §13.2/14; Aclaraciones §11, 8.2; SD4; 2.1, 3.8.4, 8.2.3.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: los 56 meses. P=3 porque el caso menciona un CD eventual en 2030; D=3 porque la proyección trimestral de capacidad lo revela.
- Responsable de respuesta: ARQ, con su equipo y contrapartes de su ámbito.
- Disparador: Nuevo sitio confirmado o distribución supera escenario.
- Plazo: Antes H5/H10; anual.
- Mitigación: Contrastar distribución real y probar límites de plataforma.
- Contingencia: Preparar ampliación con control de cambios; no declarar sitio incierto contratado.
- Evidencia de cierre: Capacidad ensayada y alcance de nuevo sitio acordado.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 194,56 HH; residual hipotético con P = 20,00 %: 97,28 HH.
- Riesgo secundario: ampliar capacidad por un crecimiento anticipado sobredimensiona la plataforma; la ampliación se decide con la proyección trimestral.
- Costo-beneficio técnico: control 8.2.3, 1.152,00 HH del T-15; ahorro hipotético 97,28 HH; retorno 0,08.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-31 — Observaciones de revisión obligan a repetir certificación paralela

La certificación de cada etapa empieza al terminar la prueba de integración, mientras el CLIENTE revisa el entregable del H4 o del H9; si la revisión formula observaciones sobre el software, parte de la certificación ya ejecutada debe repetirse.

- Análisis / categoría: Desarrollo / Proyecto.
- Fuente y EDT: BA Art. 18.3; SD7 D-21/D-31; T-15 §5.2; 3.8.2, 3.8.3, 3.9.2, 3.9.3, 3.9.4, 3.9.5.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: meses 9 a 18. P=3 porque la revisión del CLIENTE puede observar el software entregado y la certificación ya empezó; D=3 porque las observaciones se conocen al cierre de los diez días hábiles de revisión.
- Responsable de respuesta: CAL, con su equipo y contrapartes de su ámbito.
- Disparador: Observación del CLIENTE sobre un caso o requisito ya certificado.
- Plazo: Revisión del H4 (mes 10) y del H9 (mes 17).
- Mitigación: Entregar por incrementos (T-15 §5.5) para que la revisión final cubra sólo el último; ejecutar primero los casos que no dependen de lo observable en la revisión.
- Contingencia: Repetir sólo los casos afectados, con cargo a la reserva del hito y a la contingencia de calidad.
- Evidencia de cierre: Acta del H4/H9 sin observaciones abiertas sobre casos certificados.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 153,60 HH; residual hipotético con P = 20,00 %: 76,80 HH.
- Riesgo secundario: ninguno nuevo; R8-31 es a su vez el riesgo secundario de certificar en paralelo a la revisión del CLIENTE.
- Costo-beneficio técnico: control 3.8.1, 3.9.1, 320,00 HH del T-15; ahorro hipotético 76,80 HH; retorno 0,24.
- Base cuantitativa: Tabla B.3; cargo propio.

### R8-32 — Evaluadores subcontratados no disponibles para las certificaciones

La reserva ante el H5 y el H10 supone reforzar el equipo de calidad con evaluadores subcontratados hasta 16 personas por día; si no llegan a tiempo o no conocen el dominio, la certificación se alarga.

- Análisis / categoría: Desarrollo / Organizacional.
- Fuente y EDT: SD6 §6.1.3; T-15 §5.2 y §5.7; 3.8.2, 3.8.3, 3.8.4, 3.8.5, 3.8.7, 3.9.2, 3.9.3, 3.9.4, 3.9.6.
- Evaluación inicial: P=3; I=4; D=2; E=12; NPR=24. Horizonte: meses 9 a 12 y 16 a 18. P=3 porque el refuerzo depende de un proveedor externo en dos ventanas precisas; D=2 porque el contrato y la disponibilidad por quincena se verifican antes de cada ventana.
- Responsable de respuesta: CAL, con su equipo y contrapartes de su ámbito.
- Disparador: Contrato no firmado dos meses antes de la ventana o evaluadores sin la inducción del dominio.
- Plazo: Contrato antes del mes 7 y del mes 14.
- Mitigación: Contratar con anticipación, con perfiles y disponibilidad por quincena; inducir a los evaluadores con los casos del T-12 durante la marcha de QA.
- Contingencia: Reasignar evaluadores de la División de Calidad desde otros contratos o priorizar los casos críticos de aceptación.
- Evidencia de cierre: Evaluadores asignados e inducidos al inicio de cada certificación.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: VE individual 204,80 HH; residual hipotético con P = 20,00 %: 102,40 HH.
- Riesgo secundario: ninguno nuevo; R8-32 es a su vez el riesgo secundario de reforzar la calidad con evaluadores subcontratados.
- Costo-beneficio técnico: control 1.5.1, 80,00 HH del T-15; ahorro hipotético 102,40 HH; retorno 1,28.
- Base cuantitativa: Tabla B.3; cargo compartido G-CAP (Tabla B.2).

## Anexo 8.B — FMEA y exposición inicial

Este anexo presenta la prioridad cualitativa y la exposición en horas, separando el valor esperado individual del cargo conjunto. Las matrices permiten comprobar la selección de paquetes, sus ventanas y perfiles.

### B.1 Prioridad cualitativa

La Tabla B.1 reúne la evaluación inicial de las 32 fichas del Anexo 8.A con la escala del SD8, sección 8.1.3, y su justificación individual en cada ficha. El número de prioridad sigue la IEC 60812 (International Electrotechnical Commission [IEC], 2018).

**Tabla B.1 — FMEA inicial. Fuente: Anexo 8.A e IEC (2018).**

| ID | Análisis | P | I | D | E = P×I | NPR = P×I×D | Nivel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R8-01 | Solución | 4 | 5 | 4 | 20 | 80 | Crítica |
| R8-02 | Solución | 4 | 5 | 3 | 20 | 60 | Crítica |
| R8-03 | Solución | 3 | 5 | 3 | 15 | 45 | Crítica |
| R8-04 | Solución | 4 | 4 | 3 | 16 | 48 | Crítica |
| R8-05 | Solución | 3 | 5 | 5 | 15 | 75 | Crítica |
| R8-06 | Solución | 4 | 5 | 3 | 20 | 60 | Crítica |
| R8-07 | Solución | 4 | 5 | 4 | 20 | 80 | Crítica |
| R8-08 | Solución | 3 | 4 | 3 | 12 | 36 | Alta |
| R8-09 | Solución | 4 | 4 | 2 | 16 | 32 | Crítica |
| R8-10 | Desarrollo | 4 | 4 | 3 | 16 | 48 | Crítica |
| R8-11 | Desarrollo | 4 | 5 | 3 | 20 | 60 | Crítica |
| R8-12 | Desarrollo | 4 | 4 | 2 | 16 | 32 | Crítica |
| R8-13 | Desarrollo | 3 | 4 | 3 | 12 | 36 | Alta |
| R8-14 | Desarrollo | 4 | 5 | 2 | 20 | 40 | Crítica |
| R8-15 | Desarrollo | 4 | 5 | 3 | 20 | 60 | Crítica |
| R8-16 | Desarrollo | 4 | 5 | 3 | 20 | 60 | Crítica |
| R8-17 | Implantación | 4 | 5 | 2 | 20 | 40 | Crítica |
| R8-18 | Implantación | 4 | 5 | 2 | 20 | 40 | Crítica |
| R8-19 | Implantación | 3 | 5 | 3 | 15 | 45 | Crítica |
| R8-20 | Implantación | 4 | 4 | 3 | 16 | 48 | Crítica |
| R8-21 | Implantación | 3 | 4 | 3 | 12 | 36 | Alta |
| R8-22 | Implantación | 4 | 4 | 3 | 16 | 48 | Crítica |
| R8-23 | Solución | 4 | 5 | 3 | 20 | 60 | Crítica |
| R8-24 | Solución | 3 | 5 | 3 | 15 | 45 | Crítica |
| R8-25 | Implantación | 4 | 3 | 3 | 12 | 36 | Alta |
| R8-26 | Desarrollo | 3 | 4 | 3 | 12 | 36 | Alta |
| R8-27 | Solución | 4 | 5 | 4 | 20 | 80 | Crítica |
| R8-28 | Implantación | 3 | 4 | 3 | 12 | 36 | Alta |
| R8-29 | Implantación | 4 | 3 | 2 | 12 | 24 | Alta |
| R8-30 | Solución | 3 | 4 | 3 | 12 | 36 | Alta |
| R8-31 | Desarrollo | 3 | 4 | 3 | 12 | 36 | Alta |
| R8-32 | Desarrollo | 3 | 4 | 2 | 12 | 24 | Alta |

Orden dentro del nivel: NPR descendente, impacto y proximidad del plazo. R8-05 tiene NPR 75 e impacto 5 y requiere escalamiento por el riesgo residual que el SD4 declara en 4.3.2.4, registrado en 8.E. R8-01, R8-07 y R8-27 alcanzan NPR 80. No se interpreta NPR como porcentaje; los residuales hipotéticos de C.5 no son puntuaciones verificadas.

### B.2 Cuantificación individual y conjunta en horas hombre

La Tabla B.2 separa VE individual P×impacto y cargo conjunto sin duplicación. P es juicio para el horizonte de la ficha, no tasa mensual ni frecuencia medida. El impacto representa cota de trabajo adicional bajo el escenario: los paquetes recurrentes incluyen toda su ventana, sin limitarse a un año. No se afirma repetición mensual.

R8-18 cubre cuatro semanas adicionales por cada marcha blanca: 2×(12×24×8+160)=4.928 HH, imputadas contablemente a meses 15 y 20. R8-22 cubre el tercer agente valle entre meses 13–56: 17 horas por cada día real de lunes a sábado. Un indicador incierto por horizonte activa la cota completa; no se inventa tasa de recurrencia. La cota de HH no permite extender hitos.

G-CAP (R8-11/14/32) y G-INT (R8-10/15) representan el mismo retrabajo por paquete, mes y perfil como máximo de sus impactos activos; trabajos distintos se suman. Es un supuesto explícito de comparación, no identidad causal acreditada. El empate se atribuye al ID menor. Se enumeran exactamente los 8/4 estados de ambos grupos con independencia; correlación usa un uniforme común por grupo. Si se demuestra trabajo distinto, se suman cargos y se revisa la reserva.

**Tabla B.2 — Exposición individual y cargo al registro, HH. Fuente: B.3 y T-15 sección 4.2.**

| ID | Riesgo | P del horizonte | Base HH / escenario | Impacto HH | VE individual HH | Cargo conjunto HH |
| --- | --- | --- | --- | --- | --- | --- |
| R8-22 | Mesa cubre horario pero no SLA | 60,00 % | C-05: meses 13–56 | 19.499,00 | 11.699,40 | 11.699,40 |
| R8-11 | Productividad o dotación inferior al modelo | 60,00 % | 45.040,00 | 13.512,00 | 8.107,20 | 8.107,20 |
| R8-18 | Marcha blanca no cumple seis condiciones | 60,00 % | C-04: dos ventanas | 4.928,00 | 2.956,80 | 2.956,80 |
| R8-09 | Obsolescencia durante 56 meses | 60,00 % | 4.608,00 | 921,60 | 552,96 | 552,96 |
| R8-12 | Contrapartes CLIENTE no disponibles | 60,00 % | 4.056,00 | 811,20 | 486,72 | 486,72 |
| R8-02 | Doble reserva o custodia en la coordinación de reserva | 60,00 % | 2.560,00 | 768,00 | 460,80 | 460,80 |
| R8-16 | Migración altera saldos o pierde lotes | 60,00 % | 2.400,00 | 720,00 | 432,00 | 432,00 |
| R8-14 | E2 consume capacidad protegida E1 | 60,00 % | 5.600,00 | 1.680,00 | 1.008,00 | 403,20 |
| R8-23 | Frío o sensores no producen evidencia íntegra | 60,00 % | 2.240,00 | 672,00 | 403,20 | 403,20 |
| R8-20 | Rotación y resistencia reducen adopción | 60,00 % | 3.296,00 | 659,20 | 395,52 | 395,52 |
| R8-04 | Pérdida o duplicación tras 14 horas offline | 60,00 % | 3.200,00 | 640,00 | 384,00 | 384,00 |
| R8-07 | Ataque o exposición de datos críticos | 60,00 % | 2.112,00 | 633,60 | 380,16 | 380,16 |
| R8-08 | Bloqueo por proveedor | 40,00 % | 4.400,00 | 880,00 | 352,00 | 352,00 |
| R8-15 | Perfiles EDI no certificados a tiempo | 60,00 % | 1.920,00 | 576,00 | 345,60 | 345,60 |
| R8-19 | Suministros o sala fuera de secuencia | 40,00 % | 2.640,00 | 792,00 | 316,80 | 316,80 |
| R8-27 | INN-03 estima vida remanente insegura | 60,00 % | 1.248,00 | 374,40 | 224,64 | 224,64 |
| R8-30 | Crecimiento o nuevo CD supera parametrización | 40,00 % | 2.432,00 | 486,40 | 194,56 | 194,56 |
| R8-24 | Filtración en telemetría o reproducción | 40,00 % | 1.600,00 | 480,00 | 192,00 | 192,00 |
| R8-05 | Pérdida del sitio supera RPO | 40,00 % | 1.504,00 | 451,20 | 180,48 | 180,48 |
| R8-31 | Observaciones de revisión obligan a repetir certificación paralela | 40,00 % | 1.920,00 | 384,00 | 153,60 | 153,60 |
| R8-10 | Interfaces no documentadas exigen retrabajo | 60,00 % | 1.040,00 | 208,00 | 124,80 | 124,80 |
| R8-26 | INN-02 no reproduce fallas relevantes | 40,00 % | 1.536,00 | 307,20 | 122,88 | 122,88 |
| R8-06 | Carga y cola de la coordinación de reserva exceden capacidad | 60,00 % | 640,00 | 192,00 | 115,20 | 115,20 |
| R8-01 | ERP indisponible o guía invalidada | 60,00 % | 560,00 | 168,00 | 100,80 | 100,80 |
| R8-03 | CD no sostiene 24 horas sin WAN | 40,00 % | 800,00 | 240,00 | 96,00 | 96,00 |
| R8-21 | Transportistas o sindicato rechazan dispositivos | 40,00 % | 1.120,00 | 224,00 | 89,60 | 89,60 |
| R8-13 | Conocimiento de ruteo no transferido | 40,00 % | 1.040,00 | 208,00 | 83,20 | 83,20 |
| R8-25 | INN-01 no logra seguimiento posentrega | 60,00 % | 1.120,00 | 112,00 | 67,20 | 67,20 |
| R8-29 | INN-05 baja adopción de hoja del almacenero | 60,00 % | 1.120,00 | 112,00 | 67,20 | 67,20 |
| R8-32 | Evaluadores subcontratados no disponibles para las certificaciones | 40,00 % | 2.560,00 | 512,00 | 204,80 | 60,42 |
| R8-28 | INN-04 medición variable genera disputa | 40,00 % | 688,00 | 137,60 | 55,04 | 55,04 |
| R8-17 | Fecha efectiva elimina ventanas permitidas | 60,00 % | 240,00 | 72,00 | 43,20 | 43,20 |

La suma individual es **30.396,36 HH**; el registro independiente, **29.647,18 HH**, y el correlacionado, **29.183,56 HH**. Se adopta el mayor conjunto como contingencia técnica: **29.647,18 HH**. La diferencia de 749,18 HH elimina sólo cargos compartidos según el supuesto. Los controles siguen incluidos en T-15 y no se añaden a la reserva.

### B.3 Matriz de trazabilidad de la cuantificación

La Tabla B.3 expande cuentas a paquetes hoja. Productos: HH por días programados de T-15 Tabla 6.1; continuo: ventana mensual, con acompañamiento/cobertura específicos de C.3. Un perfil de ejecución no sustituye al responsable temporal de la ficha.

**Tabla B.3 — Paquetes, ventanas, perfiles, controles y cargos. Fuente: T-15 secciones 4 y 6 y Anexo 8.A.**

| ID | Paquetes hoja | Meses de impacto | Perfiles | Impacto HH | P | Controles | Cargo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R8-01 | 3.3.2, 4.1.2 | 5, 6, 11 | ARQ, IMP | 168,00 | 60,00 % | 4.1.2 | cargo propio |
| R8-02 | 3.3.6, 3.4.2, 3.4.6, 3.8.1 | 6, 7, 9 | ARQ, DES, CAL | 768,00 | 60,00 % | 3.8.1 | cargo propio |
| R8-03 | 3.8.3, 3.8.5, 6.6.3 | 5, 9, 10 | CAL, SRE | 240,00 | 40,00 % | 6.6.3 | cargo propio |
| R8-04 | 3.4.10, 3.4.6, 3.4.8, 3.8.3 | 6, 7, 8, 9, 10 | DES, CAL | 640,00 | 60,00 % | 3.8.3 | cargo propio |
| R8-05 | 3.8.5, 3.9.4, 8.2.7 | 9, 10, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56 | CAL, SRE | 451,20 | 40,00 % | 3.8.5 | cargo propio |
| R8-06 | 3.8.4, 3.9.3 | 9, 10, 16 | CAL | 192,00 | 60,00 % | 3.8.4 | cargo propio |
| R8-07 | 3.3.1, 3.8.6, 3.9.5, 8.2.2 | 6, 7, 9, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56 | SEG | 633,60 | 60,00 % | 3.8.6 | cargo propio |
| R8-08 | 2.1.1, 2.1.2, 2.1.3, 2.1.4, 3.11.1, 3.11.2, 3.11.3, 3.11.4, 3.11.5, 3.3.1, 3.3.2, 3.3.3, 3.3.4, 3.3.5, 3.3.6, 9.2.1, 9.2.2 | 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 54, 55, 56 | JP, ARQ, SEG, DAT, DES, SRE | 880,00 | 40,00 % | 1.7.1, 8.1.4, 9.2.1 | cargo propio |
| R8-09 | 8.2.2, 8.2.3, 8.2.4 | 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56 | SEG, DES, SRE | 921,60 | 60,00 % | 8.2.5 | cargo propio |
| R8-10 | 1.2.3, 3.3.2, 3.3.5 | 1, 5, 6, 7 | ARQ | 208,00 | 60,00 % | 1.2.3 | G-INT |
| R8-11 | 162 paquetes: B.4 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 | JP, ARQ, SEG, DAT, DES, CAL, SRE, IMP | 13.512,00 | 60,00 % | 1.3.4 | G-CAP |
| R8-12 | 1.1.3, 1.8.1, 1.8.2, 1.8.3, 1.8.4, 1.8.5, 1.8.6, 1.8.7, 1.8.8, 2.4.1, 2.4.2, 7.3.1, 7.3.2 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56 | JP, ARQ, SRE, IMP | 811,20 | 60,00 % | 1.1.1 | cargo propio |
| R8-13 | 1.2.2, 3.4.7 | 1, 2, 3, 7 | DES, IMP | 208,00 | 40,00 % | 1.2.2 | cargo propio |
| R8-14 | 3.5.1, 3.5.2, 3.5.3, 3.5.4, 3.9.1, 3.9.2, 3.9.3, 3.9.4, 3.9.5, 3.9.6, 3.9.7 | 15, 16, 17 | SEG, DAT, DES, CAL, SRE | 1.680,00 | 60,00 % | 1.3.4 | G-CAP |
| R8-15 | 3.5.1, 3.6.5, 3.6.6 | 13, 14, 15, 16, 17, 18, 19 | DES | 576,00 | 60,00 % | 2.1.4 | G-INT |
| R8-16 | 3.7.1, 3.7.2, 3.7.3, 3.7.4, 3.7.5 | 7, 8, 9, 10, 11, 12 | DAT | 720,00 | 60,00 % | 3.7.1 | cargo propio |
| R8-17 | 1.1.3, 1.3.1, 4.1.3 | 1, 17 | JP, IMP | 72,00 | 60,00 % | 1.1.3 | cargo propio |
| R8-18 | 3.9.3, 4.2.1, 4.3.1, 7.3.1, 7.3.2 | 15, 20 | IMP | 4.928,00 | 60,00 % | 4.1.1, 7.3.1, 7.3.2 | cargo propio |
| R8-19 | 5.1.2, 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.3.1, 6.3.2, 6.3.3, 6.3.4, 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5, 6.5.6, 6.6.3 | 2, 3, 4, 5, 9, 10, 11 | ARQ, SRE | 792,00 | 40,00 % | 5.1.2, 5.1.3 | cargo propio |
| R8-20 | 7.1.2, 7.2.1, 7.3.1, 7.3.2 | 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56 | IMP | 659,20 | 60,00 % | 7.3.1, 7.3.2 | cargo propio |
| R8-21 | 5.4.1, 5.4.2, 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5, 6.5.6 | 9, 10, 11 | SRE, IMP | 224,00 | 40,00 % | 5.4.1, 5.4.2 | cargo propio |
| R8-22 | 4.2.2, 8.1.1, 8.1.2 | 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56 | SRE | 19.499,00 | 60,00 % | Medición 8.1.2 | cargo propio |
| R8-23 | 3.4.5, 3.8.3, 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5, 6.5.6 | 6, 7, 9, 10, 11 | DES, CAL, SRE | 672,00 | 60,00 % | 6.5.3 | cargo propio |
| R8-24 | 3.10.2.1, 3.10.2.2, 3.10.2.3, 3.10.2.4, 3.3.1, 3.8.6 | 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14 | SEG, CAL | 480,00 | 40,00 % | 3.8.6 | cargo propio |
| R8-25 | 3.10.1.1, 3.10.1.2, 3.10.1.3, 3.10.1.4, 7.2.1 | 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | DAT, IMP | 112,00 | 60,00 % | 3.10.1.4 | cargo propio |
| R8-26 | 3.10.2.1, 3.10.2.2, 3.10.2.3, 3.10.2.4, 8.3.1 | 2, 3, 4, 5, 7, 8, 9, 11, 12, 14, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56 | CAL | 307,20 | 40,00 % | 3.10.2.4 | cargo propio |
| R8-27 | 3.10.3.1, 3.10.3.2, 3.10.3.3, 3.10.3.4, 8.3.2 | 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56 | DAT | 374,40 | 60,00 % | 3.10.3.4 | cargo propio |
| R8-28 | 5.4.3, 8.3.3, 8.3.4 | 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56 | JP | 137,60 | 40,00 % | 5.4.3 | cargo propio |
| R8-29 | 3.10.4.1, 3.10.4.2, 3.10.4.3, 3.10.4.4, 8.3.5, 8.3.6 | 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27 | IMP | 112,00 | 60,00 % | 3.10.4.1, 8.3.6 | cargo propio |
| R8-30 | 2.1.1, 2.1.2, 2.1.3, 2.1.4, 3.8.4, 8.2.3 | 2, 9, 10, 13, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56 | ARQ, DAT, CAL, SRE | 486,40 | 40,00 % | 8.2.3 | cargo propio |
| R8-31 | 3.8.2, 3.8.3, 3.9.2, 3.9.3, 3.9.4, 3.9.5 | 9, 10, 16 | SEG, CAL | 384,00 | 40,00 % | 3.8.1, 3.9.1 | cargo propio |
| R8-32 | 3.8.2, 3.8.3, 3.8.4, 3.8.5, 3.8.7, 3.9.2, 3.9.3, 3.9.4, 3.9.6 | 9, 10, 16, 17 | CAL | 512,00 | 40,00 % | 1.5.1 | G-CAP |

### B.3.1 Desglose de R8-11

Los 162 paquetes con entregable cuya ventana termina a más tardar en mes 21 constituyen la exposición de implementación. Se excluye 9.2.2, de salida en mes 56, y los 59 paquetes de esfuerzo continuo. La selección explícita sustituye una base agregada sin listado.

**Tabla B.4 — Base de R8-11 por perfil y ventana. Fuente: T-15 secciones 4.2 y 6.1.**

| Perfil | Paquetes | Cantidad | Meses 1–12 HH | Meses 13–21 HH | Total HH |
| --- | --- | --- | --- | --- | --- |
| JP | 1.1.1, 1.1.2, 1.1.3, 1.3.1, 1.3.2, 1.3.3, 1.3.4, 1.4.1, 1.4.2, 1.6.1, 1.7.1, 1.7.2, 4.2.3, 4.3.3, 4.3.4, 5.4.3, 5.4.4, 9.1.2 | 18 | 960,00 | 480,00 | 1.440,00 |
| ARQ | 1.2.1, 1.2.3, 1.2.5, 2.1.1, 2.1.2, 2.1.4, 2.4.1, 2.4.2, 3.3.2, 3.3.3, 3.3.4, 3.3.5, 3.3.6, 5.1.1, 5.1.2, 5.2.3 | 16 | 3.520,00 | 560,00 | 4.080,00 |
| SEG | 1.9.1, 1.9.2, 1.9.3, 2.2.1, 2.2.3, 2.2.4, 3.2.5, 3.3.1, 3.8.6, 3.9.5, 6.4.1, 6.4.2, 6.4.3 | 13 | 2.320,00 | 320,00 | 2.640,00 |
| DAT | 2.1.3, 3.10.1.1, 3.10.1.2, 3.10.1.3, 3.10.1.4, 3.10.3.1, 3.10.3.2, 3.10.3.3, 3.10.3.4, 3.4.11, 3.5.4, 3.6.1, 3.7.1, 3.7.2, 3.7.3, 3.7.4, 3.7.5 | 17 | 5.840,00 | 1.120,00 | 6.960,00 |
| DES | 3.4.1, 3.4.10, 3.4.2, 3.4.3, 3.4.4, 3.4.5, 3.4.6, 3.4.7, 3.4.8, 3.4.9, 3.5.1, 3.5.2, 3.5.3, 3.6.2, 3.6.3, 3.6.4, 3.6.5, 3.6.6, 9.1.1 | 19 | 11.040,00 | 3.920,00 | 14.960,00 |
| CAL | 1.2.4, 1.5.1, 3.10.2.1, 3.10.2.2, 3.10.2.3, 3.10.2.4, 3.8.1, 3.8.2, 3.8.3, 3.8.4, 3.8.5, 3.8.7, 3.9.1, 3.9.2, 3.9.3, 3.9.4, 3.9.6 | 17 | 2.640,00 | 1.360,00 | 4.000,00 |
| SRE | 2.3.1, 2.3.2, 2.3.3, 2.5.1, 2.5.2, 3.1.1, 3.1.2, 3.1.3, 3.1.4, 3.1.5, 3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.6, 3.8.8, 3.9.7, 5.1.3, 5.2.1, 5.2.2, 5.3.1, 5.3.2, 5.3.3, 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.2.1, 6.2.2, 6.2.3, 6.3.1, 6.3.2, 6.3.3, 6.3.4, 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5, 6.5.6, 6.6.1, 6.6.2, 6.6.3 | 44 | 7.760,00 | 160,00 | 7.920,00 |
| IMP | 2.6.1, 2.6.2, 2.6.3, 3.10.4.1, 3.10.4.2, 3.10.4.3, 3.10.4.4, 4.1.1, 4.1.2, 4.1.3, 5.4.1, 5.4.2, 7.1.1, 7.1.6, 7.2.2, 7.2.3, 7.3.1, 7.3.2 | 18 | 1.520,00 | 1.520,00 | 3.040,00 |

Base **45.040,00 HH**; impacto=base×30 %=13.512,00 HH; VE individual=impacto×60 %=8.107,20 HH. Distinto del esfuerzo de todos los paquetes de T-15.

## Anexo 8.C — Escenarios deterministas y costo-beneficio

Este anexo cuantifica en horas hombre y en meses los efectos de los escenarios que usan las fichas, con reglas reproducibles, y presenta la simulación de Monte Carlo del cronograma (C.3).

### C.1 Reglas y unidades

T-15 supone 128 HH efectivas/persona-mes; módulo D = 960 HH, integración I = 480 HH, prueba de integración/certificación = 160 HH y prueba ampliada = 320 HH. Duración por perfil = HH extra / capacidad disponible del perfil. En paralelo se usa el máximo; en secuencia, la suma. No se suman demoras correlacionadas sin modelar el camino.

**Tabla C.1 — Escenarios deterministas. Fuente: T-15 y 8.A.**

| Escenario | Cálculo reproducible | Efecto y decisión |
| --- | --- | --- |
| C-01 Corrección E1 meses 13–20 (R8-02/04/14) | 25 % × 960 = 240 HH DES + 160 HH CAL = 400 HH. Máximo(240/256,160/128) = 1,25 meses con reserva mensual | No cabe en un mes por CAL: agregar 32 HH CAL a ese mes o distribuir si la ventana y aceptación lo permiten. Registrar 400 HH una sola vez. Antes de H5 esa reserva no está disponible |
| C-02 Retrabajo EDI previo H10 (R8-10/15) | 50 % × 480 = 240 HH DES + 160 HH CAL = 400 HH. Dos DES y dos CAL adicionales darían máximo(240/256,160/256) = 0,9375 mes en paralelo; si secuencial, 0,9375 + 0,625 = 1,5625 meses | Es una necesidad de escenario, no dotación ni reserva acreditada. El orden real de corrección y prueba determina duración; no prestar reserva E1 a E2 |
| C-03 Demora de construcción o integración (R8-10/11) | La reserva programada es 19 días hábiles antes de la entrega del H4, 35 antes del H5, 21 antes del H9 y 25 antes del H10 (T-15, Tabla 5.2). Una demora de 10 días hábiles en la integración E2 (3.9.1) deja 11 días de reserva antes del H9 | Recuperar con capacidad o secuencia dentro de la reserva; si la demora proyectada supera la mitad de la reserva, replanificar antes del hito. La probabilidad conjunta con los demás riesgos está en C.3. No convertir el pronóstico en fecha contractual |
| C-04 Acompañamiento adicional (R8-18/20) | Cuatro semanas: 12 × 24 × 8 + 160 = 2.464 HH IMP; techo(2464/128) = 20 personas equivalentes | Los 12 puestos simultáneos necesitan relevos. Sólo es aumento de HH si excede el acompañamiento ya incluido; verificar el calendario de esa extensión |
| C-05 Tercer agente de mesa en las franjas valle (R8-22) | 17 horas × 26 días de lunes a sábado = 442 HH/mes; techo(442/128) = 4 personas equivalentes | Se activa si la demanda medida supera 2.200 contactos/mes y eleva el límite de 2.283 a 2.391 contactos/mes (SD4, Anexo 4-W.7). Cota meses 13–56 con días reales L–S. No incluida en T-15; >2.391 obliga a recalcular por franja y asignar capacidad. Abandono/resolución inicial se miden aparte |
| C-06 Reversión (R8-01) | Máximo(10 min técnicos, 30 min preparación operacional) + 10 min validación = 40 min; 04:45 + 40 = 05:25 | Objetivo con cinco minutos hasta 05:30, sin medición. Ensayar 96 despachos y fallos ERP/carga. RTO general de cuatro horas no admite detener despacho |
| C-07 Evidencia completa (R8-17/18) | Activación completa antes de F−28 días. E1 ejemplo: F=05-05-2028 ⇒ 07 abril–04 mayo (el 1 de mayo es feriado, por lo que el 2, el 3 y el 4 son los tres primeros días hábiles); E2: F=05-10-2028 ⇒ 07 septiembre–04 octubre | E1 remanentes semana 8 de marzo; E2 habilitaciones en agosto antes de congelamiento 01–25 septiembre. Fechas posteriores a tres primeros hábiles; confirmar feriados CLIENTE. La evidencia continúa hasta acta; habilitaciones E2 concluyen en agosto |
| C-08 Mensajes de la coordinación de reserva (R8-06) | Una línea con una retención usa cuatro mensajes (SD4, Anexo 4-I). Repartida en dos retenciones que se liberan, usa ocho; si ambas se consumen, cuatro. Si 10 % de las líneas se reparten y se liberan, el flujo sube de 46.968 a 46.968 × 1,10 = 51.665 mensajes diarios, antes de descontar la holgura de las retenciones consumidas | No implica el mismo aumento en todo el tráfico. Medir la proporción con AL-STOCK-01 y contrastar el Anexo 4-I con ARQ y SRE; no alterar aquí la memoria física |

Los porcentajes 25 % y 50 % son variaciones hipotéticas de esfuerzo, no probabilidades de evento. Los escenarios no constituyen una bolsa adicional sumable: varios pueden describir el mismo defecto.


### C.2 Costo-beneficio de las respuestas

La Tabla C.5 compara las 32 amenazas (PMI, 2017, pp. 442–443). Residual hipotético: P un nivel menor, salvo aceptación activa R8-22, impacto constante. No es eficacia medida. El costo del control es el paquete programado; no se vuelve a cargar a contingencia.

**Tabla C.5 — Controles y comparación individual, HH. Fuente: B.2, B.3 y T-15 sección 4.2.**

| ID | Control EDT | HH control | VE inicial HH | Residual hipotético HH | Ahorro hipotético HH | Retorno |
| --- | --- | --- | --- | --- | --- | --- |
| R8-01 | 4.1.2 | 80,00 | 100,80 | 67,20 | 33,60 | 0,42 |
| R8-02 | 3.8.1 | 160,00 | 460,80 | 307,20 | 153,60 | 0,96 |
| R8-03 | 6.6.3 | 160,00 | 96,00 | 48,00 | 48,00 | 0,30 |
| R8-04 | 3.8.3 | 320,00 | 384,00 | 256,00 | 128,00 | 0,40 |
| R8-05 | 3.8.5 | 320,00 | 180,48 | 90,24 | 90,24 | 0,28 |
| R8-06 | 3.8.4 | 320,00 | 115,20 | 76,80 | 38,40 | 0,12 |
| R8-07 | 3.8.6 | 160,00 | 380,16 | 253,44 | 126,72 | 0,79 |
| R8-08 | 1.7.1, 8.1.4, 9.2.1 | 448,00 | 352,00 | 176,00 | 176,00 | 0,39 |
| R8-09 | 8.2.5 | 288,00 | 552,96 | 368,64 | 184,32 | 0,64 |
| R8-10 | 1.2.3 | 80,00 | 124,80 | 83,20 | 41,60 | 0,52 |
| R8-11 | 1.3.4 | 80,00 | 8.107,20 | 5.404,80 | 2.702,40 | 33,78 |
| R8-12 | 1.1.1 | 80,00 | 486,72 | 324,48 | 162,24 | 2,03 |
| R8-13 | 1.2.2 | 80,00 | 83,20 | 41,60 | 41,60 | 0,52 |
| R8-14 | 1.3.4 | 80,00 | 1.008,00 | 672,00 | 336,00 | 4,20 |
| R8-15 | 2.1.4 | 240,00 | 345,60 | 230,40 | 115,20 | 0,48 |
| R8-16 | 3.7.1 | 480,00 | 432,00 | 288,00 | 144,00 | 0,30 |
| R8-17 | 1.1.3 | 80,00 | 43,20 | 28,80 | 14,40 | 0,18 |
| R8-18 | 4.1.1, 7.3.1, 7.3.2 | 400,00 | 2.956,80 | 1.971,20 | 985,60 | 2,46 |
| R8-19 | 5.1.2, 5.1.3 | 160,00 | 316,80 | 158,40 | 158,40 | 0,99 |
| R8-20 | 7.3.1, 7.3.2 | 320,00 | 395,52 | 263,68 | 131,84 | 0,41 |
| R8-21 | 5.4.1, 5.4.2 | 160,00 | 89,60 | 44,80 | 44,80 | 0,28 |
| R8-22 | Medición dentro de 8.1.2 | 0,00 | 11.699,40 | 11.699,40 | 0,00 | No aplica |
| R8-23 | 6.5.3 | 160,00 | 403,20 | 268,80 | 134,40 | 0,84 |
| R8-24 | 3.8.6 | 160,00 | 192,00 | 96,00 | 96,00 | 0,60 |
| R8-25 | 3.10.1.4 | 240,00 | 67,20 | 44,80 | 22,40 | 0,09 |
| R8-26 | 3.10.2.4 | 240,00 | 122,88 | 61,44 | 61,44 | 0,26 |
| R8-27 | 3.10.3.4 | 240,00 | 224,64 | 149,76 | 74,88 | 0,31 |
| R8-28 | 5.4.3 | 80,00 | 55,04 | 27,52 | 27,52 | 0,34 |
| R8-29 | 3.10.4.1, 8.3.6 | 320,00 | 67,20 | 44,80 | 22,40 | 0,07 |
| R8-30 | 8.2.3 | 1.152,00 | 194,56 | 97,28 | 97,28 | 0,08 |
| R8-31 | 3.8.1, 3.9.1 | 320,00 | 153,60 | 76,80 | 76,80 | 0,24 |
| R8-32 | 1.5.1 | 80,00 | 204,80 | 102,40 | 102,40 | 1,28 |

Los **35 controles únicos suman 6.768,00 HH ya incluidas en T-15**. No se suman retornos individuales ni se repite el costo de un mismo control. La Tabla C.7 identifica cargos compartidos.

**Tabla C.7 — Controles compartidos. Fuente: Tabla C.5.**

| Paquete | Riesgos | HH de cargo único |
| --- | --- | --- |
| 3.8.1 | R8-02, R8-31 | 160,00 |
| 3.8.6 | R8-07, R8-24 | 160,00 |
| 1.3.4 | R8-11, R8-14 | 80,00 |
| 7.3.1 | R8-18, R8-20 | 160,00 |
| 7.3.2 | R8-18, R8-20 | 160,00 |

El conjunto residual hipotético sería **23.503,37 HH**, diferencia **6.143,81 HH**. No se libera automáticamente: CAL mide eficacia y JP solicita actualización con remanente/ventana; autoriza el comité competente.

Los controles con retorno menor a uno se aplican por sanidad, continuidad, datos o aceptación obligatoria. Para los diez riesgos altos también se compara control contra contingencia de impacto completo de B.2; preservar una alternativa conforme exige menor exposición residual demostrable. Retirar función obligatoria es alternativa inadmisible. Los riesgos de obsolescencia/portabilidad incluyen controles durante toda operación y salida. Valorización sólo en Oferta Económica.

### C.3 Simulación de Monte Carlo sobre actividades

El modelo usa las 564 actividades de los 163 paquetes con entregable del Formulario T-15, Tabla 6.1, con las precedencias de esa tabla y las del Anexo 7.B (FC, CC y por interfaz). Los 59 paquetes de esfuerzo continuo cargan capacidad con su distribución mensual y no se convierten en productos. Las fechas programadas son fechas mínimas de inicio: ninguna actividad se adelanta para mejorar el resultado.

Cada escenario tiene 5.000 iteraciones con una semilla fija, de modo que la corrida se repite con el mismo resultado. La duración de cada paquete se multiplica por un factor PERT 0,75 + 0,50 × beta(3, 3), común a sus actividades, que reproduce la tríada O = 0,75 M y P = 1,25 M del T-15. Cada riesgo ocurre con la probabilidad de su ficha y, si ocurre, alarga los paquetes de la Tabla B.3 en la fracción de impacto de la Tabla 8.3. Los riesgos de los grupos G-CAP y G-INT toman el máximo del mismo efecto; trabajos distintos se suman. El escenario independiente sortea cada riesgo por separado; el correlacionado usa un mismo número aleatorio para los riesgos de cada grupo. Ninguna de las dos correlaciones es medida: son los dos extremos razonables del juicio del equipo.

El calendario usa días hábiles de lunes a viernes, 6,4 HH por persona y día, y el 1 de febrero de 2027 como inicio supuesto (V-12). El corte de la migración (3.7.5.A06) y la instalación de terreno (6.5) no ocurren del 1 al 25 de septiembre, en diciembre ni en los tres primeros días hábiles del mes; el desarrollo en DEV y QA, la documentación y la capacitación no son intervenciones productivas. Cada iteración nivela los recursos por día y por rol: desarrollo 48, arquitectura y datos 15 en conjunto, seguridad 7 sin el SOC, SRE y NOC 44, calidad 10 (16 durante las certificaciones de los meses 9 a 12 y 16 a 18) e implantación 30. El esfuerzo continuo, el soporte puente y la capacidad protegida E1 se descuentan antes de asignar productos. Cada actividad toma la primera fecha en que caben sus personas, con prioridad por la fecha límite del hito que alimenta.

La fecha límite de entrega de cada hito es el último día hábil del mes del Formulario E-25 menos los diez días hábiles de revisión del CLIENTE (BA Art. 18.3). Los intervalos de confianza son de Wilson al 95 % y miden sólo el error de muestreo del modelo; no cubren el error de los tamaños, la disponibilidad real ni la eficacia de los controles.

**Tabla C.3 — Entrega por hito y escenario correlacionado. Fuente: elaboración propia, simulación descrita en esta sección sobre el T-15 y el Anexo 7.B.**

| Hito | Límite | P50 independiente | P80 independiente | P a tiempo | IC 95 % | P correlacionado |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | 17-03-2027 | 10-03-2027 | 11-03-2027 | 100,00 % | 99,92 %–100,00 % | 100,00 % |
| H2 | 17-05-2027 | 05-05-2027 | 10-05-2027 | 97,36 % | 96,88 %–97,77 % | 97,36 % |
| H3 | 16-07-2027 | 07-07-2027 | 13-07-2027 | 88,32 % | 87,40 %–89,18 % | 88,32 % |
| H4 | 16-11-2027 | 29-10-2027 | 05-11-2027 | 99,92 % | 99,79 %–99,97 % | 99,92 % |
| H5 | 17-01-2028 | 24-12-2027 | 04-01-2028 | 97,76 % | 97,31 %–98,13 % | 97,76 % |
| H8 | 17-03-2028 | 16-03-2028 | 16-03-2028 | 91,08 % | 90,26 %–91,84 % | 91,08 % |
| H9 | 16-06-2028 | 24-05-2028 | 29-05-2028 | 100,00 % | 99,92 %–100,00 % | 100,00 % |
| H10 | 17-07-2028 | 27-06-2028 | 29-06-2028 | 100,00 % | 99,92 %–100,00 % | 100,00 % |

Sin riesgos y con el factor PERT igual a 1, todos los hitos se entregan en la fecha programada del T-15, Tabla 5.2. Con riesgos, la fecha P80 de cada hito queda antes de su límite. Las ocho entregas se cumplen juntas en el 78,04 % de las iteraciones (IC 95 %: 76,87 %–79,17 %) en ambos escenarios. La correlación no cambia la probabilidad de los hitos porque los riesgos agrupados ya comparten el mismo efecto máximo en la Tabla B.2; sólo adelanta algunas fechas P50 del H9 y del H10.

### C.3.1 Preparación de marchas blancas

El H6 y el H11 exigen que los prerrequisitos de la marcha blanca (D-25 y D-32) terminen a tiempo para el acta del mes 13 y del mes 19, con la misma regla de entrega de los demás hitos. El H7 y el H12 exigen además el alcance completo, los equipos y los usuarios antes de F−28 días; con un inicio el 1 de febrero de 2027, F1 es el 5 de mayo de 2028, primer día permitido después del feriado del 1 de mayo y de los tres primeros días hábiles, y F2 el 5 de octubre de 2028, sujetos al calendario del CLIENTE. La Etapa 2 se habilita en agosto, antes del congelamiento de septiembre.

**Tabla C.6 — Preparación condicionada, no aceptación contractual. Fuente: elaboración propia, simulación de la sección C.3.**

| Comprobación | Independencia | IC 95 % | Correlación común |
| --- | --- | --- | --- |
| H6 prerrequisitos | 96,50 % | 95,95 %–96,97 % | 96,50 % |
| H7 alcance antes de F−28 días | 100,00 % | 99,92 %–100,00 % | 100,00 % |
| H11 prerrequisitos | 100,00 % | 99,92 %–100,00 % | 100,00 % |
| H12 alcance antes de F−28 días | 100,00 % | 99,92 %–100,00 % | 100,00 % |
| Ocho entregas juntas | 78,04 % | 76,87 %–79,17 % | 78,04 % |
| Entregas y preparación juntas | 75,82 % | 74,61 %–76,99 % | 75,82 % |

La preparación no es la aceptación. Las seis condiciones del Art. 17.3 son copulativas: cero incidentes críticos o altos, volumen real durante cuatro semanas, disponibilidad y tiempos de respuesta sostenidos, conciliación sin diferencias inexplicadas, personas capacitadas y certificadas, y acta. Se miden durante la marcha blanca, y el riesgo de no cumplirlas es R8-18, con su contingencia de cuatro semanas adicionales de acompañamiento en cada etapa. Esa contingencia no mueve el paso a producción: la observación continúa hasta el acta y no autoriza desplegar durante los congelamientos.

### C.3.2 Sensibilidad con muestras comunes

La Tabla C.4 usa las mismas 5.000 muestras de la corrida independiente y desactiva sólo el riesgo indicado, conservando calendario, dependencias y nivelación. Muestra los hitos que no llegan al 100 % en la corrida base.

**Tabla C.4 — Sensibilidad con 5.000 muestras comunes. Fuente: elaboración propia, simulación de la sección C.3.**

| Escenario | H2 | H3 | H5 | H8 | Ocho juntas |
| --- | --- | --- | --- | --- | --- |
| Todos | 97,36 % | 88,32 % | 97,76 % | 91,08 % | 78,04 % |
| Sin R8-11 | 100,00 % | 100,00 % | 100,00 % | 100,00 % | 100,00 % |
| Sin R8-19 | 97,36 % | 100,00 % | 97,76 % | 91,08 % | 87,26 % |
| Sin R8-23 | 97,36 % | 88,32 % | 99,70 % | 91,08 % | 79,24 % |
| Sin R8-31 | 97,36 % | 88,32 % | 98,92 % | 91,08 % | 78,74 % |
| Sin R8-14, R8-15, R8-32 o R8-06 | 97,36 % | 88,32 % | 97,76 % | 91,08 % | 78,04 % |

R8-11 es el riesgo que gobierna el plazo: sin él, todas las entregas se cumplen. R8-19 explica la exposición del H3, y R8-23 y R8-31 la del H5. Quitar R8-14, R8-15, R8-32 o R8-06 no cambia los hitos medidos, aunque sí cambia su consumo de horas en la Tabla B.2. Una diferencia en la tabla no prueba la eficacia de un control: sólo indica dónde concentrar el seguimiento.

### C.3.3 Entradas y reproducción

La simulación usa como entradas el Formulario T-15 (Tablas 4.2 y 6.1), las dependencias del Anexo 7.B, la Tabla B.1 (P e I de cada riesgo) y las Tablas B.3 y C.5 (paquetes afectados y controles). Los parámetros son los de esta sección: 5.000 iteraciones por escenario, semilla fija, factor PERT por paquete, nivelación diaria por rol y regla de entrega de los hitos. Antes de cada ejecución se comprueba que las 564 actividades sumen las HH de sus 163 paquetes, que los 222 paquetes sumen 190.366 HH y que ninguna precedencia del T-15 quede incumplida. JP conserva el modelo y sus resultados en el repositorio del proyecto, y CAL repite la corrida cuando cambia la línea base y en cada Comité de Proyecto con los datos de avance (E8-12).

## Anexo 8.D — Reservas, autorización y programación

La Tabla D.1 distingue la programación vigente de las reservas de contingencia y de gestión (PMI, 2017, pp. 202 y 443). La valorización monetaria pertenece a la Oferta Económica.

**Tabla D.1 — Componentes de capacidad. Fuente: T-15 y Tabla B.2.**

| Componente | HH / ventana | Regla/autoridad |
| --- | --- | --- |
| Base de paquetes | 190.366,00 | T-15, sección 4.2; programada |
| Soporte puente | 9.336,00; meses 16–20 | Incluido; servicio, no corrección |
| Protección E1 | 3.072,00; meses 13–20 | Incluida; 256 DES + 128 CAL por mes; exclusiva de la Etapa 1 |
| Programación vigente | 202.774,00 | Suma de las tres filas anteriores |
| Cierre y estabilización, meses 21–22 | 2.774,54 | Incluido en la programación; no se suma otra vez |
| Contingencia del registro | 29.647,18 | JP solicita el cargo por evento, mes y perfil; T-15, sección 4.5 |
| Absorción por la protección E1 | 0,00 | Ningún riesgo coincide con meses 13–20, Etapa 1 y perfiles DES/CAL |
| Gestión | 1.600,00 | Fuera de la línea base; Comité Ejecutivo |
| Cuatro semanas finales de cada marcha blanca | 0 días de reserva | Evidencia obligatoria |

Con ambas reservas, la capacidad que la oferta debe poder movilizar es de **234.021,18 HH**. El T-15, sección 4.5, compara su peak mensual con la dotación declarada.

R8-02 y R8-04 recaen en productos y pruebas anteriores al mes 13, y R8-14 es trabajo de la Etapa 2; por eso el descuento por capacidad protegida es **0,00 HH**. Las 3.072 HH siguen protegidas para correcciones futuras de la Etapa 1: si una ocurrencia concreta coincide con la ventana y el perfil, su cargo autorizado se descuenta de la contingencia, nunca de nuevo del total base.

La Tabla D.2 reparte la contingencia por mes y perfil. Arquitectura y datos comparten capacidad, con columnas separadas de imputación. El reparto ubica la necesidad; los recursos de cada ventana se verifican en el T-15, sección 4.5.

**Tabla D.2 — Contingencia por mes y perfil, HH. Fuente: Tablas B.2 y B.3.**

| Mes | JP | ARQ | SEG | DAT | DES | CAL | SRE | IMP | Total HH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 132,96 | 39,36 | 28,80 | 0,00 | 0,00 | 0,00 | 82,29 | 2,13 | 285,54 |
| 2 | 66,72 | 202,56 | 100,80 | 81,60 | 0,00 | 89,60 | 61,71 | 59,73 | 662,73 |
| 3 | 23,52 | 72,96 | 43,20 | 28,80 | 0,00 | 60,80 | 278,40 | 45,33 | 553,01 |
| 4 | 9,12 | 15,36 | 43,20 | 28,80 | 0,75 | 30,40 | 446,40 | 57,60 | 631,63 |
| 5 | 9,12 | 461,36 | 74,06 | 57,60 | 0,75 | 60,80 | 403,20 | 0,00 | 1.066,89 |
| 6 | 9,12 | 419,76 | 236,34 | 28,80 | 1.226,55 | 0,00 | 28,80 | 0,00 | 1.949,37 |
| 7 | 23,52 | 33,76 | 44,80 | 184,80 | 984,84 | 30,40 | 28,80 | 0,00 | 1.330,92 |
| 8 | 9,12 | 0,96 | 0,00 | 230,74 | 720,15 | 4,34 | 0,00 | 0,00 | 965,32 |
| 9 | 9,12 | 0,96 | 76,80 | 366,86 | 1,18 | 417,87 | 225,60 | 41,60 | 1.139,98 |
| 10 | 9,12 | 0,96 | 0,00 | 110,40 | 1,18 | 316,67 | 194,18 | 47,31 | 679,83 |
| 11 | 9,12 | 0,96 | 0,00 | 393,60 | 1,18 | 30,40 | 224,58 | 61,71 | 721,56 |
| 12 | 9,12 | 0,96 | 0,00 | 220,80 | 1,18 | 30,40 | 0,58 | 4,11 | 267,16 |
| 13 | 9,12 | 96,96 | 0,00 | 0,00 | 29,98 | 0,00 | 256,54 | 81,05 | 473,65 |
| 14 | 9,12 | 72,96 | 0,00 | 48,00 | 29,98 | 30,40 | 276,94 | 105,74 | 573,14 |
| 15 | 23,52 | 1,87 | 0,00 | 241,92 | 957,34 | 0,00 | 256,54 | 1.528,59 | 3.009,79 |
| 16 | 23,52 | 1,87 | 163,84 | 0,00 | 29,98 | 467,33 | 317,26 | 45,39 | 1.049,20 |
| 17 | 29,92 | 1,87 | 0,00 | 0,00 | 79,35 | 42,37 | 266,74 | 70,08 | 490,34 |
| 18 | 9,12 | 1,87 | 0,00 | 0,00 | 79,35 | 0,00 | 266,74 | 94,08 | 451,17 |
| 19 | 9,12 | 1,87 | 0,00 | 0,00 | 46,44 | 0,00 | 276,94 | 26,88 | 361,25 |
| 20 | 9,12 | 1,87 | 0,00 | 0,00 | 1,18 | 0,00 | 266,74 | 1.505,28 | 1.784,20 |
| 21 | 48,21 | 1,87 | 9,60 | 1,44 | 22,08 | 1,28 | 275,44 | 7,68 | 367,61 |
| 22 | 5,01 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 8,64 | 310,05 |
| 23 | 5,01 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 8,64 | 310,05 |
| 24 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 9,84 | 320,60 |
| 25 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 255,04 | 9,84 | 290,00 |
| 26 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 9,84 | 320,60 |
| 27 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 265,24 | 8,88 | 299,24 |
| 28 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 7,68 | 318,44 |
| 29 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 7,68 | 308,24 |
| 30 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 7,68 | 308,24 |
| 31 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 7,68 | 318,44 |
| 32 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 265,24 | 7,68 | 298,04 |
| 33 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 7,68 | 318,44 |
| 34 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 7,68 | 308,24 |
| 35 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 7,68 | 308,24 |
| 36 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 7,68 | 318,44 |
| 37 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 255,04 | 7,68 | 287,84 |
| 38 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 7,68 | 308,24 |
| 39 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 7,68 | 308,24 |
| 40 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 7,68 | 318,44 |
| 41 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 265,24 | 7,68 | 298,04 |
| 42 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 7,68 | 318,44 |
| 43 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 7,68 | 318,44 |
| 44 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 265,24 | 7,68 | 298,04 |
| 45 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 7,68 | 318,44 |
| 46 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 7,68 | 308,24 |
| 47 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 7,68 | 308,24 |
| 48 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 7,68 | 318,44 |
| 49 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 255,04 | 7,68 | 287,84 |
| 50 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 7,68 | 308,24 |
| 51 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 7,68 | 308,24 |
| 52 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 7,68 | 318,44 |
| 53 | 4,16 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 265,24 | 7,68 | 298,04 |
| 54 | 6,29 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 285,64 | 7,68 | 320,57 |
| 55 | 6,29 | 0,96 | 9,60 | 1,44 | 7,68 | 1,28 | 275,44 | 7,68 | 310,37 |
| 56 | 6,29 | 0,96 | 16,00 | 1,44 | 7,68 | 1,28 | 275,44 | 7,68 | 316,77 |
| Total | 644,16 | 1.466,56 | 1.163,84 | 2.074,56 | 4.482,24 | 1.657,86 | 14.095,24 | 4.062,72 | 29.647,18 |

Cada celda se muestra con dos decimales, por lo que las sumas visibles pueden diferir en centésimas de los totales.

La reserva de gestión cubre un evento que el registro no identifica: rehacer un módulo de clase D (960 HH DES), su integración (480 HH) y una certificación (160 HH CAL), 1.600 HH en total. Con 8 desarrolladores y 4 evaluadores adicionales, el desarrollo toma 960 / (8 × 128) = 0,94 meses y la integración y certificación 640 / (4 × 128) = 1,25 meses, unos 2,2 meses en secuencia. No usa la protección E1. El Comité Ejecutivo la autoriza y actualiza la línea base sin ampliar hitos. Un riesgo identificado, como los escenarios C-01 y C-02, consume contingencia y nunca gestión.

La reserva de cronograma se compara con el pronóstico de cada hito en el seguimiento semanal. Cada consumo registra el identificador del evento, el paquete, la etapa, el mes, el perfil, las HH y la evidencia; sólo una misma corrección comparte cargo. El residual hipotético no se libera sin eficacia, cierre y autorización. Ninguna reserva deroga el Art. 17.3 ni sus multas.

## Anexo 8.E — Problemas, dependencias y condiciones de evidencia

Estas entradas son estados documentales actuales, no probabilidades FMEA. Tabla E.1 fija condiciones de línea base y aceptación. El riesgo asociado describe un evento futuro distinto del vacío ya identificado.

**Tabla E.1 — Condiciones de evidencia y compatibilidad. Fuente: oferta y Bases citadas.**

| ID | Estado y condición de cierre | Responsable / límite | Riesgos asociados |
| --- | --- | --- | --- |
| E8-01 | T-15 estima por clases de tamaño fundadas en los requerimientos del T-12 y las cantidades del T-11 (SD7, sección 7.2.2), con tríada de ±25 %; la productividad de 128 HH efectivas por persona y mes aún no se contrasta con el avance real; peak 69 en el mes 15, 48 personas simultáneas de desarrollo entre julio y septiembre de 2027, brechas de dotación en SEG e IMP (T-15 §5.7) y capacidad por subventana sin asignación. Refinar la estimación con el equipo y comprobar personas, competencias, relevos y cero sobreasignación | JP/DES/CAL; antes línea base | R8-11/14 |
| E8-02 | El cronograma de 564 actividades incluye dependencias, revisión Art. 18.3 y nivelación (T-15, secciones 5 y 6). El equipo valida plantillas, dotación y plazos en la línea base y repite el cálculo. LafroX emite la orden de compra de infraestructura en el mes 2 para instalar la sala desde el mes 3. El calendario de compra de hardware de terreno del CLIENTE se acuerda en el mes 1 y asegura disponibilidad antes de cada ola | JP/ARQ/SRE; antes línea base/H3 | R8-10/11/19 |
| E8-03 | V-12 no confirma fecha/calendario hábil. Febrero 2027 es ejemplo; comprobar E2 antes enero 2029, congelamientos y 28 días | JP/CLIENTE; mes 1 antes H1 | R8-15/17/18 |
| E8-04 | Objetivo 40 minutos/96 camiones sin ensayo. Demostrar versión operativa, DTE válidos y flujo sin interrupción; papel no acredita despacho | ARQ/SRE/Operaciones; antes H6/H11 | R8-01 |
| E8-05 | RPO crítico ≤ 15 min y RTO ≤ 4 h por escenario. Si el sitio se destruye con los tres caminos caídos, el ensayo AL-DR-01 identifica la copia remota que sobrevive y la frontera en que se cumple el RPO; el NAS local destruido no aporta datos. El tratamiento del SD4 4.3.2.4 (RT-02.11) se demuestra junto con RT-07.04. AL-DR-01 y la continuidad del despacho se ensayan por separado | ARQ/SRE; H5/H10 y operación | R8-05 |
| E8-06 | La coordinación de reserva y retención de INT-03/04 (SD4, apartado 4.1.4.4 y Anexo 4-G) está dimensionada en el Anexo 4-I, Tabla A.10, y Anexo 4-W, Tablas A.32 y A.33, con un máximo de cuatro mensajes por línea. La retención consumida no se libera y la holgura cubre líneas repartidas. AL-STOCK-01 mide la proporción de líneas con más de una retención. 3.8.4/3.9.3 verifican carga y drenaje, incluido el enlace de respaldo de Talca, sin sumar la coordinación al drenaje | ARQ/SRE; antes H5/H10 | R8-02/06 |
| E8-07 | La mesa base cubre los tres niveles de servicio hasta 2.283 contactos al mes (SD4, Anexo 4-W.7). Sobre 2.200 se activa el tercer agente valle; sobre 2.391, o con otra mezcla o tiempos, se recalcula por franja y se asigna capacidad. Se miden 80 % antes de 20 s, abandono ≤ 5 % y resolución inicial ≥ 70 %. La cota del tercer agente está en la contingencia (T-15, sección 4.5) | SRE; H7 mes 16/H12 mes 21; diario | R8-22 |
| E8-08 | La suspensión del proveedor de lácteos, de marzo a septiembre de 2026, es antecedente anterior; V-13 sin restitución documentada. Confirmar condiciones/evidencia con CLIENTE/proveedor sin atribuir solución retroactiva | JP/DAT/Calidad CLIENTE; mes 1 y antes aceptación trazabilidad | R8-16/23 |
| E8-09 | AL-STOCK-01/AL-ACT-01, carga, offline y conmutación descritos, no ejecutados. Aportar resultados reproducibles y resolver defectos críticos/altos | CAL/líderes; H5/H10/cierre aplicable | R8-02–07/16/18 |
| E8-10 | Antecedentes, certificaciones y dotación del SD1 son declarados; su acreditación documental se entrega en el Sobre N.° 1 (SD1, sección 1.4). No usar las declaraciones como disponibilidad demostrada antes de asignar personas | JP; antes presentación correspondiente | R8-11 |
| E8-11 | Separar los diez días hábiles de revisión del CLIENTE de los diez de subsanación; reconocer el hito sólo con acta. La reserva de cada hito va de 4 a 35 días hábiles (T-15, Tabla 5.2). En el H1 y el H8, menores que el plazo de subsanación, el borrador se revisa una semana antes de la entrega y toda observación formal se subsana en cinco días hábiles (R8-12) | JP/CAL/CLIENTE; antes de la línea base | R8-12/17/18/31 |
| E8-12 | La calibración de probabilidades e impactos de la sección 8.1.3 y la simulación usan juicio del equipo, no frecuencias medidas. Contrastar con los datos de avance y de incidentes desde el mes 3 y recalcular el valor esperado y la simulación en cada Comité de Proyecto | JP/CAL; trimestral desde el mes 3 | Todos |
| E8-13 | La programación supone el inicio el 1 de febrero de 2027 y días hábiles de lunes a viernes, sin feriados del CLIENTE. Al confirmar V-12 se convierten los meses a fechas, se repite la nivelación y la simulación del Anexo 8.C, y se verifica que cada fecha P80 siga antes de su límite | JP/CAL; mes 1, antes de la línea base | R8-11/17 |
| E8-14 | La carga de desarrollo llega a 48,10 personas equivalentes frente a 48 en un día de julio a septiembre de 2027. Si R8-18 se materializa, implantación llega a 34,9 y 36,8 equivalentes en los meses 15 y 20, frente a 30: el contrato del personal de implantación incluye una opción de hasta 8 personas adicionales por cuatro semanas, activable con cinco días hábiles de aviso. Asignar personas con nombre y firmar ese contrato antes del mes 11 | JP/DES/IMP; antes de asignar y antes del mes 11 | R8-11/14/18 |

La regla de precio es única en la oferta: el SD2 (Anexo 2.2, S-09), el SD3 (Anexo 3.G, RNG-08) y el Formulario T-12 (RF-03.11 y RF-03.12) conservan el precio acordado al capturar el pedido. Su transmisión al ERP sin alteración se verifica en las pruebas de integración.

Infraestructura 99,95 %, transacción crítica 99,9 % y cero interrupción de despacho son obligaciones distintas. RTO ≤4 h/RPO ≤15 min no rebajan la ventana crítica.


Las seis condiciones de aceptación requieren evidencia separada. Retiro sanitario: clientes con evidencia en menos de dos horas; 85 minutos de diseño del SD5 orientan el ensayo, no lo acreditan.

## Anexo 8.F — Adopción de innovaciones y oportunidad

La Tabla F.1 vincula cada innovación con su riesgo de adopción, su evaluación y su respuesta.

**Tabla F.1 — Riesgos de innovaciones. Fuente: SD13 y Anexo 8.A.**

| Innovación SD7 vigente | Riesgo de adopción | P / I | Mitigación y contingencia |
| --- | --- | --- | --- |
| INN-01 Seguimiento de vencimiento posentrega en el local | R8-25 | 4 / 3 | Piloto asistido, I-01A y confirmación en la visita; aviso solo por vida útil y trazabilidad base si no rinde |
| INN-02 Reproducción de incidentes de terreno | R8-26; seguridad R8-24 | 3 / 4 | Casos protegidos de corte/reintento; mantener diagnóstico/regresión base |
| INN-03 Vida útil remanente por historia térmica del lote | R8-27 | 4 / 5 | Validación Calidad/revisión semestral; retirar recomendación y mantener vencimiento/control sanitario |
| INN-04 Tramo variable de la Operación ligado al costo de servir | R8-28 | 3 / 4 | Línea base y tres liquidaciones sombra; resolución contractual sin tarifas técnicas |
| INN-05 Hoja de negocio del almacenero | R8-29 | 4 / 3 | Co-diseño/piloto asistido sin exigir conexión; conservar preventista y efectivo |

La oportunidad se evalúa con una escala de beneficio simétrica a la de impacto del SD8, sección 8.1.3, en el horizonte de los meses 11 a 56:

**Tabla F.2 — Escala de beneficio. Fuente: escala del SD8.**

| Valor | Beneficio ordinal |
| --- | --- |
| 1 | Mejora local sin efecto medible en retrabajo ni servicio |
| 2 | Reduce retrabajo que ya cabe en la capacidad asignada |
| 3 | Reduce retrabajo que consumiría contingencia o acorta la resolución de un servicio auxiliar |
| 4 | Protege un hito, un SLA o un alcance obligatorio |
| 5 | Evita detener el despacho crítico o comprometer seguridad, datos o sanidad |

O8-01 — Oportunidad de diagnóstico: si los casos protegidos INN-02 representan incidentes reales, podrían permitir resolver fallas equivalentes con menos retrabajo. P ordinal 3, porque los casos protegidos cubren sólo los incidentes de corte y reintento; beneficio ordinal 3, porque un caso reproducible reduce el retrabajo de diagnóstico que hoy consumiría contingencia; puntuación de oportunidad 9, separada de exposición de amenazas. Estrategia: mejorar, porque la reutilización de los casos protegidos aumenta su probabilidad de ocurrir (PMI, 2017, p. 444). La evidencia de comparación son las HH de diagnóstico de incidentes equivalentes antes y después de usar los casos. CAL compara HH antes/después de casos equivalentes durante validación meses 11–15 y operación. Disparador: incidente equivalente con reproducción disponible. Acción: reutilizar casos dentro de 3.10.2/8.3.1. Si no se verifica ahorro, mantener diagnóstico base sin descontar HH del T-15. No se suma esta oportunidad como reserva.


DAT/IMP conservan perfiles de esfuerzo; responsabilidad desde mes 22 pasa a Operación, con aprobaciones Calidad/Seguridad de Tabla 8.1 y SD13.

## Referencias

Las fuentes citadas en este documento se listan en formato APA 7.ª edición. Las Bases se citan en el texto con su documento y el artículo, capítulo, sección o código del requisito.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.*
- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N.º TFEP-01/2026*.
- LafroX. (2026). Subdocumentos 1 a 7 y 13, con los anexos y formularios citados.
- International Electrotechnical Commission. (2018). *IEC 60812:2018 Failure modes and effects analysis (FMEA and FMECA)*. IEC.
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. ISO.
- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.), capítulo 11. Project Management Institute.


## Declaración de uso de IA

La tabla declara apoyo de IA conforme a las Aclaraciones §7.2. La revisión humana identifica quién efectivamente verificó cada parte y se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Anexo 8.A | Codex; Claude Code | Registro, horizonte y responsables temporales | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 8.B | Codex; Claude Code | FMEA y matrices de exposición/paquetes | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 8.C | Codex; Claude Code | Costo-beneficio, ejecución y modelo reproducible | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 8.D | Codex; Claude Code | Contingencia, gestión y curva por mes/perfil | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 8.E | Codex; Claude Code | Compatibilidad y condiciones de evidencia | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 8.F | Codex; Claude Code | Adopción de innovaciones y oportunidad | Alto | Ninguno | [[REVISIÓN HUMANA]] |
