# LafroX — Subdocumento 8: Anexos

## Anexo 8.A — Registro ampliado de amenazas

P/I/D son juicios ordinales iniciales según SD8 §8.1.3. Las entradas están identificadas, con tratamiento propuesto; no hay evidencia de ensayos ni cierre contractual en esta sesión. La causa descrita sustenta P; la consecuencia sustenta I; la forma y evidencia de detección sustenta D. Los vacíos actuales se distinguen de eventos inciertos en 8.E.

### R8-01 — ERP indisponible o guía invalidada

Emisión tributaria concentrada en ERP; si falta una guía o cambia la carga, podría detenerse el despacho por falta de DTE válido.

- Análisis / categoría: Solución / Operación.
- Fuente y EDT: Caso cap. 10; SD4 INT-06/07; T-18 §6.4; 3.3.2,4.1.2.
- Evaluación inicial: P=4; I=5; D=4; E=20; NPR=80. Horizonte: desde H6 hasta el fin de la operación. P=4 porque toda guía depende del ERP de 2017 y un cambio de carga diario invalida guías preemitidas; D=4 porque la falta de guía válida se aprecia en el andén, cuando ya afecta el despacho.
- Responsable de respuesta: ARQ, con su equipo y contrapartes de su ámbito.
- Disparador: Guía ausente/invalidada o ensayo no termina antes de 05:30.
- Plazo: Antes H6; repetir antes H11.
- Mitigación: Preemisión nocturna, conciliación carga/guía y ensayo de caída ERP con 96 camiones.
- Contingencia: Conservar versión local probada y DTE válidos; Operaciones decide continuidad autorizada con ERP. No emitir documentos alternativos ni reemplazar despacho por papel.
- Evidencia de cierre: Ensayo de 96 salidas sin interrupción, con caída ERP/carga modificada, sin pérdida ni duplicación.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-02 — Doble reserva o custodia CD-05

Cortes/reintentos podrían confirmar sin acuse durable o repetir descuentos, alterando stock y trazabilidad.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: SD4 CD-05; AL-STOCK-01/AL-ACT-01; 3.3.6,3.4.2,3.4.6,3.8.1.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: hasta la regresión del H9 y cada cambio de CD-05. P=4 porque la reserva se coordina entre sitios que se desconectan y reintentan a diario; D=3 porque la conciliación diaria y AL-STOCK-01 lo detectan, pero después de confirmar.
- Responsable de respuesta: DES, con su equipo y contrapartes de su ámbito.
- Disparador: Confirmación sin acuse, UUID repetido o dos autoridades.
- Plazo: Antes H4; regresión H9.
- Mitigación: Probar concurrencia, UUID, idempotencia, época de autoridad y retención por lote/ubicación.
- Contingencia: Bloquear confirmaciones ambiguas y conciliar colas con un único escritor; continuidad sólo sin degradar despacho.
- Evidencia de cierre: AL-STOCK-01/AL-ACT-01 con cero doble descuento/custodia.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-03 — CD no sostiene 24 horas sin WAN

Dependencias remotas ocultas podrían impedir recibir, preparar o despachar durante desconexión prolongada.

- Análisis / categoría: Solución / Operación.
- Fuente y EDT: Caso cap. 10; SD4 borde local; 6.6.3,3.8.3,3.8.5.
- Evaluación inicial: P=3; I=5; D=3; E=15; NPR=45. Horizonte: H5 a H10. P=3 porque el diseño declara 24 horas autónomas, pero una dependencia remota no identificada es plausible; D=3 porque sólo un ensayo de corte completo la revela.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Servicio remoto invocado o cola agotada durante desconexión.
- Plazo: Antes H5; repetir antes H10.
- Mitigación: Ensayar 24 horas sin WAN con procesos completos y reconciliación.
- Contingencia: Mantener autoridad local probada y aislar dependencia; no aprobar corte sin continuidad.
- Evidencia de cierre: 24 horas de operación completa y drenaje sin diferencias inexplicadas.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-04 — Pérdida o duplicación tras 14 horas offline

Dispositivos/reintentos podrían perder pedidos, entregas o cobros al reconectar.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: Caso cap. 10; SD3 operación desconectada; 3.4.6,3.4.8,3.4.10,3.8.3.
- Evaluación inicial: P=4; I=4; D=3; E=16; NPR=48. Horizonte: cada versión móvil hasta el mes 56. P=4 porque 62 preventistas y 96 camiones sincronizan cada día después de tramos sin señal; D=3 porque la diferencia aparece en la conciliación diaria.
- Responsable de respuesta: DES, con su equipo y contrapartes de su ámbito.
- Disparador: Cola no durable, doble acuse o diferencia de cobro.
- Plazo: Antes H5 y cada versión móvil.
- Mitigación: Ensayar 14 horas offline, reinicio, UUID y reconciliación.
- Contingencia: Retener registros durables y bloquear confirmaciones ambiguas sin doble digitación.
- Evidencia de cierre: Registros/cobros completos y únicos al reconectar.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-05 — Pérdida del sitio supera RPO

Falla simultánea de comunicaciones seguida de destrucción del sitio podría eliminar respaldo local y dejar copia remota con más de 15 minutos de pérdida.

- Análisis / categoría: Solución / Operación.
- Fuente y EDT: BTT RT-07.04/07; SD4 límite residual DR; 3.8.5,3.9.4,8.2.7.
- Evaluación inicial: P=3; I=5; D=5; E=15; NPR=75. Horizonte: los 56 meses. P=3 porque exige la falla de los tres caminos de Talca seguida de la destrucción del sitio; D=5 porque la pérdida sólo se reconoce después de ocurrir.
- Responsable de respuesta: ARQ, con su equipo y contrapartes de su ámbito.
- Disparador: Antigüedad remota>15 minutos o ensayo multisistema fallido.
- Plazo: Resolver diseño y ensayar antes H5/H10.
- Mitigación: Evaluar supervivencia remota de datos y resolver brecha mediante gobierno de arquitectura.
- Contingencia: Aplicar DR probado y recuperar datos sobrevivientes; registrar pérdida sin declarar cumplimiento si excede RPO.
- Evidencia de cierre: Conmutación real RPO≤15min/RTO≤4h; continuidad de despacho por ensayo separado.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-06 — Carga y cola CD-05 exceden capacidad

4L de A31 puede subestimar retenciones múltiples si N≠L; peak y drenaje podrían saturar enlaces o cómputo.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: SD4 A31/A32; Caso RT-09.01; 3.8.4,3.9.3.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: H5 a H10 y crecimiento anual. P=4 porque las retenciones de más de un lote o ubicación (N distinto de L) son habituales; D=3 porque la cola se monitorea, pero su saturación se confirma con prueba de carga.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Mensajes por pedido superiores al supuesto, cola creciente o latencia incumplida.
- Plazo: Antes H5/H10; vigilancia mensual.
- Mitigación: Medir N/L/retenciones y probar 1,5 veces peak, crecimiento y drenaje.
- Contingencia: Priorizar transacciones y limitar tráfico auxiliar; escalar capacidad por arquitectura sin reducir volumen obligatorio.
- Evidencia de cierre: Carga/latencias y drenaje conformes a multiplicidad medida.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-07 — Ataque o exposición de datos críticos

Móviles, portales y terceros podrían permitir acceso indebido, ransomware o alteración de lotes/cobros.

- Análisis / categoría: Solución / Seguridad.
- Fuente y EDT: BTT seguridad cap. 13; SD4 seguridad; 3.3.1,3.8.6,3.9.5,8.1.5.
- Evaluación inicial: P=4; I=5; D=4; E=20; NPR=80. Horizonte: los 56 meses. P=4 porque portales, móviles e integraciones con terceros están expuestos de forma permanente; D=4 porque un acceso indebido puede reconocerse recién en la revisión del SIEM.
- Responsable de respuesta: SEG, con su equipo y contrapartes de su ámbito.
- Disparador: Vulnerabilidad crítica/alta o acceso entre clientes.
- Plazo: Antes H5/H10; vigilancia continua.
- Mitigación: Pruebas ofensivas, mínimo privilegio, aislamiento, registro y rotación de credenciales.
- Contingencia: Contener acceso, preservar evidencia y recuperar entorno limpio con continuidad probada.
- Evidencia de cierre: Sin defectos de seguridad críticos/altos abiertos y prueba de recuperación.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-08 — Bloqueo por proveedor

Dependencias AWS/mapas/mensajería/ERP podrían impedir sustitución o extracción y comprometer salida y continuidad.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: Aclaraciones8.2; SD4 híbrida; 2.1,3.3,3.11,9.2.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: diseño H2/H8 y salida del mes 56. P=3 porque varias dependencias tienen un solo proveedor; D=3 porque se detecta en el ensayo anual de extracción y restauración.
- Responsable de respuesta: ARQ, con su equipo y contrapartes de su ámbito.
- Disparador: Exportación/restauración falla o restricción contractual.
- Plazo: Diseño H2/H8; ensayo anual y salida mes56.
- Mitigación: Inventariar dependencias, contratos y formatos; ensayar extracción/restauración.
- Contingencia: Usar copias portables e interfaces desacopladas; alternativa mediante control de cambios.
- Evidencia de cierre: Exportación/restauración reproducibles y documentación CLIENTE.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-09 — Obsolescencia durante 56 meses

Versiones o dispositivos podrían quedar sin soporte e introducir vulnerabilidades/incompatibilidad.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: Aclaraciones8.2; SD4; BTT mantenimiento; 8.2.2,8.2.3,8.2.4.
- Evaluación inicial: P=4; I=4; D=2; E=16; NPR=32. Horizonte: los 56 meses. P=4 porque varias versiones de la arquitectura terminan su soporte dentro del contrato; D=2 porque esas fechas se conocen y se revisan mensualmente.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Fin de soporte en horizonte o actualización bloqueada.
- Plazo: Inventario H2; revisión mensual operación.
- Mitigación: Inventariar versiones/soporte y ensayar compatibilidad en QA.
- Contingencia: Aislar componente y migrar a versión probada en fechas permitidas.
- Evidencia de cierre: Versiones soportadas y regresión sin degradación E1/E2.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-10 — Interfaces no documentadas exigen retrabajo

El levantamiento podría descubrir formatos/restricciones no representados en prototipos y atrasar ERP/telemetría.

- Análisis / categoría: Desarrollo / Técnico.
- Fuente y EDT: Caso §17.5; SD7 D-02; 1.2.3,3.3.2,3.3.5.
- Evaluación inicial: P=4; I=4; D=3; E=16; NPR=48. Horizonte: hasta el H4. P=4 porque el caso declara interfaces del sistema de gestión sin documentación; D=3 porque se revela en prototipos y pruebas de integración.
- Responsable de respuesta: ARQ, con su equipo y contrapartes de su ámbito.
- Disparador: Contrato incompleto mes3 o conexión fallida.
- Plazo: Antes H2; integración H4.
- Mitigación: Capturar muestras/horarios y probar contratos y errores temprano.
- Contingencia: Priorizar interfaz con capacidad adicional explícita; no usar reserva posterior a H5.
- Evidencia de cierre: Contratos y pruebas positivas/negativas con volumen representativo.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-11 — Productividad o dotación inferior al modelo

Clases HH/128HH efectivas no medidas podrían subestimar esfuerzo y especialistas, afectando hitos.

- Análisis / categoría: Desarrollo / Proyecto.
- Fuente y EDT: T-15 §§4/5; SD1 dotación declarada; 222 paquetes,1.3.4.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: hasta el H5. P=4 porque los tamaños de HH son supuestos, el PERT da 50 % de cumplir cada hito y la dotación declarada no cubre SEG ni IMP sin contratación (T-15 §5.3 y §5.7); D=3 porque el valor ganado mensual lo detecta con un mes de atraso.
- Responsable de respuesta: JP, con su equipo y contrapartes de su ámbito.
- Disparador: Estimación supera capacidad por rol/subventana o personas no asignadas.
- Plazo: Antes línea base; semanal.
- Mitigación: Estimar con equipo/cantidades; asignar competencias y relevos; comprobar el peak de 66 (mes 16), la comparación con la dotación declarada (T-15 §5.7) y las bandas de 15 especialistas; crear la reserva de 0,65/0,67 mes que el PERT exige antes de H4/H5.
- Contingencia: Reordenar dentro de hitos y sustentar capacidad adicional; no prestar E1 a E2.
- Evidencia de cierre: Asignaciones nominales y cero sobreasignación por subventana.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-12 — Contrapartes CLIENTE no disponibles

TI de cuatro personas y gerencias podrían no atender decisiones, pruebas o actas a tiempo.

- Análisis / categoría: Desarrollo / Organizacional.
- Fuente y EDT: Caso cap. 10; Aclaraciones8.2; 1.1.3,1.8,2.4,7.3.
- Evaluación inicial: P=4; I=4; D=2; E=16; NPR=32. Horizonte: hasta el H12. P=4 porque el equipo de TI del CLIENTE tiene cuatro personas y atiende la operación; D=2 porque cada revisión tiene fecha registrada y su vencimiento se detecta ese día.
- Responsable de respuesta: JP, con su equipo y contrapartes de su ámbito.
- Disparador: Decisión/revisión no atendida en fecha acordada.
- Plazo: Agenda mes1; cada comité quincenal.
- Mitigación: Reservar agenda, responsable/suplente y material por decisión.
- Contingencia: Escalar a patrocinador y avanzar tareas independientes; silencio no es aceptación.
- Evidencia de cierre: Decisiones/actas explícitas con responsables y fechas.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-13 — Conocimiento de ruteo no transferido

Ausencia o jubilación podría ocurrir antes de capturar/validar excepciones operativas.

- Análisis / categoría: Desarrollo / Organizacional.
- Fuente y EDT: Caso resultado16; SD7 D-03; 1.2.2,3.4.7.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: hasta las dos semanas sin planificador de la marcha blanca E1 (R18-16). P=3 porque el caso prevé la jubilación del planificador; D=3 porque se detecta en la validación del mes 3 y en la prueba sin planificador.
- Responsable de respuesta: IMP, con su equipo y contrapartes de su ámbito.
- Disparador: Reglas no validadas mes3 o rutas no operables.
- Plazo: Captura meses 1–3; probar antes H7.
- Mitigación: Capturar reglas/excepciones y validar con planificador y suplente.
- Contingencia: Suplente entrenado y reglas versionadas; evitar dependencia permanente de don Hugo.
- Evidencia de cierre: Dos semanas sin planificador y OTIF conforme.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-14 — E2 consume capacidad protegida E1

El solapamiento podría reasignar corrección E1, degradarla o retrasar E2.

- Análisis / categoría: Desarrollo / Proyecto.
- Fuente y EDT: BA17.2; T-15 reserva; 4.2.2,3.5,3.9.
- Evaluación inicial: P=4; I=5; D=2; E=20; NPR=40. Horizonte: meses 13 a 20. P=4 porque E1 y E2 requieren a los mismos especialistas durante el solapamiento; D=2 porque la imputación separada de horas lo muestra en la semana.
- Responsable de respuesta: DES, con su equipo y contrapartes de su ámbito.
- Disparador: Persona compartida o reserva cargada a E2.
- Plazo: Antes mes13; semanal hasta20.
- Mitigación: Separar equipos y proteger 256DES+128CAL HH/mes E1.
- Contingencia: Restituir E1 y justificar ampliación E2; no duplicar reserva.
- Evidencia de cierre: Equipos/capacidad independientes y métricas E1 sostenidas.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-15 — Perfiles EDI no certificados a tiempo

Dependencia de cadenas podría impedir activar todo el alcance antes de28 días finales o enero2029.

- Análisis / categoría: Desarrollo / Proyecto.
- Fuente y EDT: Caso §13.2; SD7 3.6.5/6; T-18 6.2; 3.5.1,3.6.5,3.6.6.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: hasta el mes 21. P=4 porque depende de cadenas externas con calendarios propios; D=3 porque el estado de certificación se sigue por perfil.
- Responsable de respuesta: DES, con su equipo y contrapartes de su ámbito.
- Disparador: Perfil sin ambiente/acuse o fecha prevista posterior a F−28 días.
- Plazo: Principal antes H10; todas antes activación/F−28 días.
- Mitigación: Acordar pruebas temprano y registrar todos los perfiles/aprobaciones.
- Contingencia: Carga asistida es contingencia auxiliar, no EDI; recuperar sin excluir cadenas.
- Evidencia de cierre: Aprobaciones por cadena y100% de alcance durante cuatro semanas.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-16 — Migración altera saldos o pierde lotes

Datos WMS/planillas con vacíos podrían trasladar existencias incorrectas e invalidar conciliación/trazabilidad.

- Análisis / categoría: Desarrollo / Técnico.
- Fuente y EDT: SD3 3.4.4; SD7 D-24; 3.7.1–5.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: hasta el corte de migración. P=4 porque el WMS de 2013 y las planillas tienen vacíos de lote; D=3 porque los ensayos de migración lo detectan en la conciliación.
- Responsable de respuesta: DAT, con su equipo y contrapartes de su ámbito.
- Disparador: Lote requerido ausente o diferencia inexplicada.
- Plazo: Dos ensayos antes corte/H6.
- Mitigación: Perfilar/conteo y dos ensayos; reconciliar SKU/lote/ubicación.
- Contingencia: Retener corte y corregir origen; WMS sólo lectura, sin doble escritura.
- Evidencia de cierre: Ensayos/corte con diferencias explicadas y trazabilidad completa.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-17 — Fecha efectiva elimina ventanas permitidas

Inicio distinto del supuesto podría coincidir con congelamientos o impedir producción E2 antes enero2029.

- Análisis / categoría: Implantación / Proyecto.
- Fuente y EDT: Caso cap. 10/13.2; SD3 V-12; BA17; 1.1.3,1.3.1,4.1.3.
- Evaluación inicial: P=4; I=5; D=2; E=20; NPR=40. Horizonte: hasta el mes 1. P=4 porque la fecha no está confirmada y las ventanas permitidas son estrechas; D=2 porque el calendario se recalcula al confirmar V-12.
- Responsable de respuesta: JP, con su equipo y contrapartes de su ámbito.
- Disparador: Calendario sin días permitidos/28 días de evidencia.
- Plazo: Mes1 antes H1; antes H6/H11.
- Mitigación: Convertir meses a fechas con feriados CLIENTE/prohibiciones.
- Contingencia: Reordenar dentro de períodos; escalar incompatibilidad sin presumir prórroga.
- Evidencia de cierre: Calendario compatible con hitos y evidencia completa.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-18 — Marcha blanca no cumple seis condiciones

Defecto alto, volumen incompleto o diferencias podrían persistir en cierre e impedir aceptación.

- Análisis / categoría: Implantación / Operación.
- Fuente y EDT: BA17.3/18; T-18; 4.2.1,4.3.1,7.3.
- Evaluación inicial: P=4; I=5; D=2; E=20; NPR=40. Horizonte: cada marcha blanca. P=4 porque las seis condiciones son copulativas y se miden con volumen real; D=2 porque los indicadores son diarios.
- Responsable de respuesta: CAL, con su equipo y contrapartes de su ámbito.
- Disparador: Una condición falla o grupo fuera del alcance.
- Plazo: Diario marcha blanca; H7/H12.
- Mitigación: Activar todo antes F−28 días y demostrar seis condiciones simultáneas.
- Contingencia: Extender a costo adjudicatario sin mover fases siguientes; no firmar cumplimiento ficticio.
- Evidencia de cierre: 28 días completos, cero críticos/altos, conciliación, usuarios certificados y acta.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-19 — Suministros o sala fuera de secuencia

Demoras compra/recepción/configuración podrían bloquear H3 o una ola pese a HH disponibles.

- Análisis / categoría: Implantación / Proyecto.
- Fuente y EDT: BTT recinto; Caso cap. 11; SD7 D-09–13/26; 5.1.2,6.1,6.3,6.6.3,6.5.
- Evaluación inicial: P=3; I=5; D=3; E=15; NPR=45. Horizonte: hasta el H3. P=3 porque compra, recepción e instalación ocurren en dos meses con proveedores externos; D=3 porque las actas de recepción lo revelan.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Suministro posterior a montaje o dispositivo ausente.
- Plazo: Sala/racks/borde antes H3; terreno antes ola.
- Mitigación: Confirmar responsabilidades BTT/SD4 y compra de terreno CLIENTE; recibir antes montar.
- Contingencia: Recuperar suministro/instalación con capacidad específica; no activar equipos inexistentes.
- Evidencia de cierre: Actas y pruebas en secuencia sala/racks/borde/terreno.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-20 — Rotación y resistencia reducen adopción

Rotación 38 % de preparación y personal antiguo podrían dejar turnos sin usuarios certificados.

- Análisis / categoría: Implantación / Organizacional.
- Fuente y EDT: Caso restricciones; T-18; 7.1.2,7.2.1,7.3.1/2.
- Evaluación inicial: P=4; I=4; D=3; E=16; NPR=48. Horizonte: los 56 meses. P=4 porque el turno de noche rota 38 % al año; D=3 porque la certificación por usuario lo detecta antes de cada turno.
- Responsable de respuesta: IMP, con su equipo y contrapartes de su ámbito.
- Disparador: Usuario sin certificar o uso incompleto.
- Plazo: Antes cada ola; mensual.
- Mitigación: Tutor por turno, certificación en puesto y acompañamiento con relevos.
- Contingencia: Retener/restaurar acompañamiento y repetir formación sin detener rutas.
- Evidencia de cierre: Usuarios por perfil/turno certificados y uso sostenido.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-21 — Transportistas o sindicato rechazan dispositivos

Vehículos externos y objeciones GPS/cámara podrían impedir sensores o captura en rutas.

- Análisis / categoría: Implantación / Organizacional.
- Fuente y EDT: Caso restricciones; SD3 S-28; SD7 acuerdos; 5.4.1,5.4.2,6.5.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: hasta la ola de reparto. P=3 porque el caso registra objeciones a GPS y cámaras; D=3 porque el acta exigida antes de la ola lo revela.
- Responsable de respuesta: IMP, con su equipo y contrapartes de su ámbito.
- Disparador: Acuerdo ausente o ruta sin dispositivo requerido.
- Plazo: Antes ola de reparto.
- Mitigación: Acordar instalación/uso/finalidad/acceso con CLIENTE, terceros y sindicato.
- Contingencia: Escalar acuerdos; atención auxiliar no reemplaza registro térmico ni excluye rutas.
- Evidencia de cierre: Acuerdos/pruebas en toda flota y rutas requeridas.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-22 — Mesa cubre horario pero no SLA

Las posiciones de mesa dimensionadas con Erlang C podrían no bastar si la demanda o el tiempo de atención difieren del supuesto, y el modelo no verifica el abandono ≤5 % ni la resolución al primer contacto ≥70 %.

- Análisis / categoría: Implantación / Operación.
- Fuente y EDT: BTT RT-21.06/07; Caso RT-21.06; 4.2.2,8.1.1,8.1.2.
- Evaluación inicial: P=4; I=4; D=3; E=16; NPR=48. Horizonte: meses 13 a 56. P=4 porque la demanda de 2.000 contactos/mes es una estimación sin medición y la del año 3 queda a 1,1 % del límite de 2.283; D=3 porque la medición por contacto empieza en la marcha blanca.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Demanda/tiempos exceden umbral o falta relevo.
- Plazo: Antes H7/mes21; diario peaks.
- Mitigación: Medir demanda por intervalo y agentes/competencias;04–22 lunes–sábado y24×7 peaks/críticos.
- Contingencia: Activar agentes adicionales verificados y guardia especialista.
- Evidencia de cierre: Prueba de demanda/turnos con los tres SLA y horarios.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-23 — Frío o sensores no producen evidencia íntegra

−22°C, falta de señal o deriva podrían dejar lotes sin historial térmico válido.

- Análisis / categoría: Solución / Operación.
- Fuente y EDT: Caso restricciones; SD3 M9/M12; 3.4.5,6.5,3.8.3.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: los 56 meses. P=4 porque el congelado a −22 °C y los tramos sin señal son recurrentes; D=3 porque las lecturas faltantes aparecen en la conciliación.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Lectura faltante, deriva o dispositivo falla.
- Plazo: Antes ola1/reparto; continuo.
- Mitigación: Probar autonomía, almacenamiento/calibración y asociación sensor/lote/tiempo.
- Contingencia: Calidad retiene lote sin evidencia y utiliza reemplazo probado.
- Evidencia de cierre: Serie completa y asociada al lote; ensayo−22°C/sin señal.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-24 — Filtración en telemetría o reproducción

Datos de ubicación/clientes/cobros podrían circular sin minimización en trazas de incidentes.

- Análisis / categoría: Solución / Seguridad.
- Fuente y EDT: SD4 seguridad; SD7 INN-02; 3.10.2,3.3.1,3.8.6.
- Evaluación inicial: P=3; I=5; D=3; E=15; NPR=45. Horizonte: los 56 meses. P=3 porque reproducir un incidente requiere copiar datos de terreno; D=3 porque la minimización se revisa en cada conjunto.
- Responsable de respuesta: SEG, con su equipo y contrapartes de su ámbito.
- Disparador: Datos personales/secretos en conjunto de reproducción.
- Plazo: Antes usar trazas; cada versión.
- Mitigación: Enmascarar, controlar acceso/retención y revisar conjuntos.
- Contingencia: Suspender conjunto afectado, contener y producir muestra protegida.
- Evidencia de cierre: Inspección de datos/permisos sin exposición indebida.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-25 — INN-01 no logra seguimiento posentrega

Clientes podrían no aportar datos útiles y reducir cobertura de vencimiento en local.

- Análisis / categoría: Implantación / Organizacional.
- Fuente y EDT: SD7 Anexo 7.D INN-01; BTT RT-26.04; 3.10.1,7.2.1.
- Evaluación inicial: P=4; I=3; D=3; E=12; NPR=36. Horizonte: piloto y validación de INN-01. P=4 porque depende de que los clientes aporten datos de forma voluntaria; D=3 porque el indicador del piloto lo muestra.
- Responsable de respuesta: IMP, con su equipo y contrapartes de su ámbito.
- Disparador: Cobertura/uso inferior al objetivo previo del piloto.
- Plazo: Piloto meses 11–15.
- Mitigación: Piloto asistido y comparación con registro base, sin exigir conexión al almacenero.
- Contingencia: Mantener trazabilidad lote/entrega y atención asistida.
- Evidencia de cierre: Resultado frente a objetivo previo y decisión de adopción.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-26 — INN-02 no reproduce fallas relevantes

Registros incompletos podrían impedir reproducir incidentes offline y diagnosticar defectos.

- Análisis / categoría: Desarrollo / Técnico.
- Fuente y EDT: SD7 Anexo 7.D INN-02; BTT RT-26.04; 3.10.2,8.3.1.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: meses 11 a 56. P=3 porque registros incompletos de terreno son plausibles; D=3 porque se detecta al intentar reproducir un caso.
- Responsable de respuesta: CAL, con su equipo y contrapartes de su ámbito.
- Disparador: Caso representativo no reproducible.
- Plazo: Validación meses 11–15; operación.
- Mitigación: Ensayar corte/reinicio/reintento con conjuntos protegidos.
- Contingencia: Conservar diagnóstico y regresión base con trazas protegidas.
- Evidencia de cierre: Reproducción y diagnóstico contrastados.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-27 — INN-03 estima vida remanente insegura

Historia incompleta o mala calibración podría sugerir una vida útil no segura.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: SD7 INN-03; SD3 M9/M12; BTT RT-26.04; 3.10.3,8.3.2.
- Evaluación inicial: P=4; I=5; D=4; E=20; NPR=80. Horizonte: los 56 meses. P=4 porque la calibración inicial tiene poca historia térmica; D=4 porque un error de estimación puede reconocerse sólo cuando el producto se reclama.
- Responsable de respuesta: DAT, con su equipo y contrapartes de su ámbito.
- Disparador: Resultado fuera de criterio Calidad o historial faltante.
- Plazo: Antes uso meses 11–15; revisión26/32/38/44/50/56.
- Mitigación: Validar con Calidad y regla conservadora; no ampliar vencimiento por inferencia.
- Contingencia: Deshabilitar recomendación y mantener vencimiento/control sanitario.
- Evidencia de cierre: Validación Calidad con trazabilidad modelo/datos.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-28 — INN-04 medición variable genera disputa

Costo de servir incompleto podría distorsionar línea base/liquidación variable.

- Análisis / categoría: Implantación / Proyecto.
- Fuente y EDT: SD7 INN-04; BA50.2; BTT RT-26.04; 5.4.3,8.3.3,8.3.4.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: meses 21 a 56. P=3 porque la atribución de costos admite interpretaciones; D=3 porque las tres liquidaciones sombra la ponen a prueba.
- Responsable de respuesta: JP, con su equipo y contrapartes de su ámbito.
- Disparador: Diferencia inexplicada o liquidaciones sombra no reproducibles.
- Plazo: Modelo17–20; sombra21–23; antes mes24.
- Mitigación: Acordar fórmula/datos/auditoría; valores sólo en Oferta Económica.
- Contingencia: Mecanismo contractual de resolución y corrección; sin modificar SLA ni inventar tarifa.
- Evidencia de cierre: Línea base y tres liquidaciones sombra reconciliadas.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-29 — INN-05 baja adopción de hoja del almacenero

La hoja podría no ser comprensible o útil y quedar sin uso.

- Análisis / categoría: Implantación / Organizacional.
- Fuente y EDT: SD7 INN-05; Caso canal tradicional; BTT RT-26.04; 3.10.4,8.3.5,8.3.6.
- Evaluación inicial: P=4; I=3; D=2; E=12; NPR=24. Horizonte: piloto de INN-05. P=4 porque muchos almaceneros no usan herramientas digitales; D=2 porque las métricas de uso se ven cada semana.
- Responsable de respuesta: IMP, con su equipo y contrapartes de su ámbito.
- Disparador: Uso/beneficio menor al objetivo acordado antes piloto.
- Plazo: Piloto E2; evaluar24–27.
- Mitigación: Co-diseño/piloto asistido o papel; preservar preventista y efectivo.
- Contingencia: Retirar mejora opcional mediante gobierno manteniendo compromisos y canal obligatorio.
- Evidencia de cierre: Utilidad/uso contrastados y decisión documentada.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

### R8-30 — Crecimiento o nuevo CD supera parametrización

CD eventual2030 o crecimiento distinto por sitio podría superar capacidades.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: Caso §13.2/14; Aclaraciones8.2; SD4; 2.1,3.8.4,8.2.3.
- Evaluación inicial: P=3; I=4; D=3; E=12; NPR=36. Horizonte: los 56 meses. P=3 porque el caso menciona un CD eventual en 2030; D=3 porque la proyección trimestral de capacidad lo revela.
- Responsable de respuesta: ARQ, con su equipo y contrapartes de su ámbito.
- Disparador: Nuevo sitio confirmado o distribución supera escenario.
- Plazo: Antes H5/H10; anual.
- Mitigación: Contrastar distribución real y probar límites de plataforma.
- Contingencia: Preparar ampliación con control de cambios; no declarar sitio incierto contratado.
- Evidencia de cierre: Capacidad ensayada y alcance de nuevo sitio acordado.
- Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C. Una ampliación necesita asignación conforme a 8.D; no se presume incluida. Para requisitos obligatorios, el ahorro de HH no sustituye cumplimiento.
- Seguimiento semanal y en cada comité; diario durante marcha blanca/operación afectadas. Puntuación residual sólo tras verificar controles.

## Anexo 8.B — FMEA y exposición inicial

La tabla reúne la evaluación inicial de las 30 fichas del Anexo 8.A con la escala del SD8, sección 8.1.3, y su justificación individual en cada ficha.

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

Orden dentro del nivel: NPR descendente, impacto y proximidad del plazo. R8-05 tiene NPR75 e impacto5 y requiere escalamiento por la brecha conocida registrada en8.E. R8-01/07/27 alcanzan NPR80. No se interpreta NPR como porcentaje ni se estiman puntajes residuales sin evidencia.

## Anexo 8.C — Escenarios deterministas y costo-beneficio

Este anexo cuantifica en horas hombre y en meses los efectos de los escenarios que usan las fichas, con reglas reproducibles.

### C.1 Reglas y unidades

T-15 supone 128 HH efectivas/persona-mes; módulo D = 960 HH, integración I = 480 HH, prueba de integración/certificación = 160 HH y prueba ampliada = 320 HH. Duración por perfil = HH extra / capacidad disponible del perfil. En paralelo se usa el máximo; en secuencia, la suma. No se suman demoras correlacionadas sin modelar el camino.

| Escenario | Cálculo reproducible | Efecto y decisión |
| --- | --- | --- |
| C-01 Corrección E1 meses 13–20 (R8-02/04/14) | 25 % × 960 = 240 HH DES + 160 HH CAL = 400 HH. Máximo(240/256,160/128) = 1,25 meses con reserva mensual | No cabe en un mes por CAL: agregar 32 HH CAL a ese mes o distribuir si la ventana y aceptación lo permiten. Registrar 400 HH una sola vez. Antes de H5 esa reserva no está disponible |
| C-02 Retrabajo EDI previo H10 (R8-10/15) | 50 % × 480 = 240 HH DES + 160 HH CAL = 400 HH. Dos DES y dos CAL adicionales darían máximo(240/256,160/256) = 0,9375 mes en paralelo; si secuencial, 0,9375 + 0,625 = 1,5625 meses | Es una necesidad de escenario, no dotación ni reserva acreditada. El orden real de corrección y prueba determina duración; no prestar reserva E1 a E2 |
| C-03 Demora integración (R8-10/11) | N06/N08 +0,25 mes ⇒ entrega del H4 en t9,75 y revisión del CLIENTE reducida a 0,25 mes; N12/N13 +0,50 ⇒ entrega del H9 en t17,00, sin plazo de revisión. PERT: σ = 0,51 mes al H4 y 0,53 al H5 | Holgura de hito cero y 50 % de cumplir cada hito: recuperar y recalcular antes de comprometer H5/H10. No convertir el pronóstico en fecha contractual |
| C-04 Acompañamiento adicional (R8-18/20) | Cuatro semanas: 12 × 24 × 8 + 160 = 2.464 HH IMP; techo(2464/128) = 20 personas equivalentes | 13 puestos simultáneos necesitan relevos. Sólo es aumento de HH si excede el acompañamiento ya incluido; verificar el calendario de esa extensión |
| C-05 Tercer agente de mesa en las franjas valle (R8-22) | 17 horas × 26 días de lunes a sábado = 442 HH/mes; techo(442/128) = 4 personas equivalentes | Se activa si la demanda medida supera 2.200 contactos/mes y eleva el límite de 2.283 a 2.391 contactos/mes (SD4, Anexo 4-W.7). Es capacidad de escenario, no incluida en el T-15; abandono y resolución al primer contacto se miden aparte |
| C-06 Reversión (R8-01) | Máximo(10 min técnicos,30 min preparación operacional) + 10 min validación = 40 min; 04:45 + 40 = 05:25 | Objetivo con cinco minutos hasta 05:30, sin medición. Ensayar 96 despachos y fallos ERP/carga. RTO general de cuatro horas no admite detener despacho |
| C-07 Evidencia completa (R8-17/18) | Activación completa antes de F−28 días. E1 ejemplo: F=01-05-2028 ⇒ 03–30 abril; E2: F=01-10-2028 ⇒ 03–30 septiembre | E1 remanentes semana 8 de marzo; E2 habilitaciones en agosto antes de congelamiento 01–25 septiembre. Aplicar los primeros tres días hábiles y feriados CLIENTE; mantener evidencia hasta acta |
| C-08 Mensajes CD-05 (R8-06) | 2N + 2L y 4L coinciden sólo si N=L. Si N=2L, tráfico de coordinación = 6L, un 50 % más que 4L | No implica 50 % más de todo el tráfico. Medir retenciones y contrastar A31/A32 con ARQ/SRE; no alterar aquí memoria física |

Los porcentajes 25 % y 50 % son variaciones hipotéticas de esfuerzo, no probabilidades de evento. Los escenarios no constituyen una bolsa adicional sumable: varios pueden describir el mismo defecto.

### C.2 Comparación de prevención y retrabajo

Una verificación de 160 HH frente a retrabajo supuesto de 400 HH da 400/160 = 2,5. Con prueba ampliada de 320 HH, 400/320 = 1,25. Son cocientes de esfuerzo, sin frecuencia del evento, ahorro esperado ni retorno monetario. Un control incluido en T-15 no vuelve a cargarse como reserva. Los valores específicos requieren estimación del equipo.

En despacho, seguridad, sanidad y RPO, la conformidad es obligatoria; las HH ayudan a escoger alternativas conformes. Retirar una innovación que no rinde exige gobierno y preservar compromisos contratados; no elimina funciones obligatorias.

## Anexo 8.D — Reservas, autorización y programación

| Componente | HH / ventana | Inclusión y regla |
| --- | --- | --- |
| Corrección protegida E1 | 8 × (256 DES + 128 CAL) = 3.072 HH; meses 13–20 | Ya incluida en 202.774 HH. Remanente inicial de planificación 3.072; consumo real no informado. No prestar a E2 ni usar antes del mes 13 |
| Soporte puente E1 | 9.336 HH SRE; meses 16–20 | Servicio base ya incluido; no reserva de desarrollo |
| Cierre/estabilización implementación meses 21–22 | 2.834,54 HH | Separado de operación en T-15; no añadir de nuevo |
| Calendario H4/H5/H9/H10 | 0 meses de reserva de hito; el PERT exige 0,65 y 0,67 mes antes de H4/H5 para 90 % | Brecha que debe cerrarse antes de aprobar la línea base (T-15 §5.3) |
| Últimas cuatro semanas de marcha blanca | 0 días disponibles como reserva | Evidencia obligatoria, no tiempo para completar alcance |
| Contingencia de integración E1 | 400 HH (240 DES + 160 CAL), dimensionada con C-02; disponible meses 7 a 11 | Cubre el mayor escenario individual de retrabajo de integración antes del H5, cuando la reserva protegida aún no existe. Fuera del total del T-15; su uso exige autorización y actualiza la curva |
| Contingencia de integración E2 | 400 HH (240 DES + 160 CAL), dimensionada con C-02; disponible meses 15 a 18 | Separada de la E1; no se presta entre etapas ni se suma con la anterior |
| Contingencia de atención | 442 HH/mes desde el mes en que se active C-05 | Sólo si la demanda medida supera 2.200 contactos/mes |
| Extensión de marcha blanca | 2.464 HH por cada cuatro semanas (C-04) | Sólo ante extensión del Art. 17.3, a costo del adjudicatario y sin mover fases siguientes |
| Reserva de gestión | Para riesgos no identificados; sin horas preasignadas | JP solicita caso; Comité Ejecutivo autoriza con capacidad/plazo explícitos; actualización T-15/calendario. Su monto, y el de las contingencias anteriores, corresponde a la Oferta Económica (Art. 50.2) |

Por evento se registra ID relacionado, mes/subventana, perfil, HH autorizadas/consumidas, remanente y efecto en hitos. Si R8-02 y R8-04 representan el mismo defecto, comparten cargo. Redactar esta planificación no demuestra consumo de HH. La ampliación de marcha blanca se rige por Art. 17.3 a costo del adjudicatario y sin mover fases siguientes; ninguna reserva lo deroga.

## Anexo 8.E — Problemas, dependencias y condiciones de evidencia

Estas entradas son estados documentales actuales, no probabilidades FMEA. El riesgo asociado describe un evento futuro distinto del vacío ya identificado.

| ID | Estado y condición de cierre | Responsable / límite | Riesgos asociados |
| --- | --- | --- | --- |
| E8-01 | T-15 usa tamaños y productividad supuestos; peak 66 en el mes 16, brechas de dotación en SEG e IMP (T-15 §5.7) y capacidad por subventana sin asignación. Estimar con equipo y comprobar personas, competencias, relevos y cero sobreasignación | JP/DES/CAL; antes línea base | R8-11/14 |
| E8-02 | CPM agregado de 24 bloques con revisiones Art. 18.3 y PERT calculados; cada hito tiene 50 % de cumplirse y faltan 0,65/0,67 mes de reserva antes de H4/H5; detalle diario y sala/racks/configuración no demostrado. Desagregar D-01–D-34 y comprobar secuencias y capacidad | JP/ARQ/SRE; antes línea base/H3 | R8-10/11/19 |
| E8-03 | V-12 no confirma fecha/calendario hábil. Febrero 2027 es ejemplo; comprobar E2 antes enero 2029, congelamientos y 28 días | JP/CLIENTE; mes 1 antes H1 | R8-15/17/18 |
| E8-04 | Objetivo 40 minutos/96 camiones sin ensayo. Demostrar versión operativa, DTE válidos y flujo sin interrupción; papel no acredita despacho | ARQ/SRE/Operaciones; antes H6/H11 | R8-01 |
| E8-05 | SD4 describe RPO remoto >15 min ante pérdida del sitio/respaldo. Resolver arquitectura y medir RPO/RTO; aceptar el riesgo no satisface Bases | ARQ/SRE; antes H5/H10 | R8-05 |
| E8-06 | CD-05 ya incluido en A31/A32; 4L depende de multiplicidad. Medir 2N+2L, retenciones, carga y drenaje, incluido enlace de respaldo Talca | ARQ/SRE; antes H5/H10 | R8-02/06 |
| E8-07 | T-15 ya imputa las posiciones de mesa del SD4 y el SOC 24×7, pero el Erlang C no verifica abandono ni resolución al primer contacto, y el límite es 2.283 contactos/mes. Medir por contacto desde la marcha blanca y calibrar Erlang A (T-15 §5.6). BTT RT-21.06 y Caso RT-21.06 tienen contenido distinto | SRE; antes H7/mes 21 | R8-22 |
| E8-08 | Suspensión láctea septiembre 2026 es antecedente anterior; V-13 sin restitución documentada. Confirmar condiciones/evidencia con CLIENTE/proveedor sin atribuir solución retroactiva | JP/DAT/Calidad CLIENTE; mes 1 y antes aceptación trazabilidad | R8-16/23 |
| E8-09 | AL-STOCK-01/AL-ACT-01, carga, offline y conmutación descritos, no ejecutados. Aportar resultados reproducibles y resolver defectos críticos/altos | CAL/líderes; H5/H10/cierre aplicable | R8-02–07/16/18 |
| E8-10 | Antecedentes/dotación SD1 sin acreditación externa en esta copia. No usar declaraciones como disponibilidad/certificación demostradas | JP; antes presentación correspondiente | R8-11 |
| E8-11 | Sin revisión humana final/A-6 consolidado ni actas de aceptación en esta sesión. Documentar revisores, alcance, pruebas y actas; Markdown no acredita presentación visual final | JP/CAL; antes entrega y cada aceptación | R8-18 |
| E8-13 | La red agregada incorpora medio mes de revisión del CLIENTE antes de cada hito y presentación por incrementos (T-15 §5.1 y §5.5), pero la subsanación de diez días hábiles no tiene holgura: una observación atrasa el hito. Acordar con la Contraparte Técnica el calendario de presentaciones | JP/CAL/CLIENTE; antes aprobar línea base | R8-12/17/18 |
| E8-12 | SD5 sin consolidar, excluido. Datos necesarios no disponibles en SD3/4 son dependencias futuras; no presumir disponibilidad | DAT/ARQ; al consolidarse | R8-16 |

La incoherencia de precio quedó corregida en SD2 S-09 y RF activos 03.11/12 del SD3/T-12: todos conservan el precio capturado. La integración requiere prueba. Catálogos originales y material complementario histórico se conservan sin reemplazar la línea activa.

Infraestructura 99,95 %, transacción crítica 99,9 % y cero interrupción de despacho son obligaciones distintas. RTO ≤4 h/RPO ≤15 min no rebajan la ventana crítica.

## Anexo 8.F — Adopción de innovaciones y oportunidad

| Innovación SD7 vigente | Riesgo de adopción | P / I | Mitigación y contingencia |
| --- | --- | --- | --- |
| INN-01 Seguimiento de vencimiento posentrega | R8-25 | 4 / 3 | Piloto asistido y objetivo previo; conservar trazabilidad base si no rinde |
| INN-02 Reproducción de incidentes | R8-26; seguridad R8-24 | 3 / 4 | Casos protegidos de corte/reintento; mantener diagnóstico/regresión base |
| INN-03 Vida remanente por historia térmica | R8-27 | 4 / 5 | Validación Calidad/revisión semestral; retirar recomendación y mantener vencimiento/control sanitario |
| INN-04 Tramo variable por costo de servir | R8-28 | 3 / 4 | Línea base y tres liquidaciones sombra; resolución contractual sin tarifas técnicas |
| INN-05 Hoja de negocio del almacenero | R8-29 | 4 / 3 | Co-diseño/piloto asistido sin exigir conexión; conservar preventista y efectivo |

La oportunidad se evalúa con una escala de beneficio simétrica a la de impacto del SD8, sección 8.1.3, en el horizonte de los meses 11 a 56:

| Valor | Beneficio ordinal |
| --- | --- |
| 1 | Mejora local sin efecto medible en retrabajo ni servicio |
| 2 | Reduce retrabajo que ya cabe en la capacidad asignada |
| 3 | Reduce retrabajo que consumiría contingencia o acorta la resolución de un servicio auxiliar |
| 4 | Protege un hito, un SLA o un alcance obligatorio |
| 5 | Evita detener el despacho crítico o comprometer seguridad, datos o sanidad |

O8-01 — Oportunidad de diagnóstico: si los casos protegidos INN-02 representan incidentes reales, podrían permitir resolver fallas equivalentes con menos retrabajo. P ordinal 3, porque los casos protegidos cubren sólo los incidentes de corte y reintento; beneficio ordinal 3, porque un caso reproducible reduce el retrabajo de diagnóstico que hoy consumiría contingencia; puntuación de oportunidad 9, separada de exposición de amenazas. La evidencia de comparación son las HH de diagnóstico de incidentes equivalentes antes y después de usar los casos. CAL compara HH antes/después de casos equivalentes durante validación meses 11–15 y operación. Disparador: incidente equivalente con reproducción disponible. Acción: reutilizar casos dentro de 3.10.2/8.3.1. Si no se verifica ahorro, mantener diagnóstico base sin descontar HH del T-15. No se suma esta oportunidad como reserva.

## Referencias

- Distribuidora Puelche S.A. (2026). Bases Administrativas TFEP-01/2026, artículos 17, 18, 50.2 y formularios T-16/T-22.
- Distribuidora Puelche S.A. (2026). Bases Técnicas Transversales, RT-07.04/07, RT-19.04, RT-21.06/07 y RT-26.04.
- Distribuidora Puelche S.A. (2026). Caso 02 — Logística, capítulos 10–14 y requisitos específicos citados.
- Aclaraciones de licitación (2026), capítulo 8 y reglas de presentación.
- LafroX. SD1–4, SD6 y SD7, con anexos y formularios citados. SD5 no utilizado.
- International Electrotechnical Commission. (2018). *IEC 60812:2018 Failure modes and effects analysis (FMEA and FMECA)*. IEC.
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. ISO.
- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.), capítulo 11. Project Management Institute.

## Declaración de uso de IA

La tabla declara el uso de IA en estos anexos; se consolida en la declaración del SD8 y en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Anexos 8.A y 8.B | Codex; Claude Code | Fichas y FMEA (6 de octubre de 2026); justificación individual de P y D con horizonte (7 de octubre de 2026) | Alto | Ninguno | No documentada |
| Anexos 8.C y 8.D | Codex; Claude Code | Escenarios deterministas; contingencias dimensionadas y PERT (7 de octubre de 2026) | Alto | Ninguno | No documentada |
| Anexos 8.E y 8.F | Codex; Claude Code | Condiciones de evidencia; escala de beneficio de la oportunidad (7 de octubre de 2026) | Alto | Ninguno | No documentada |
