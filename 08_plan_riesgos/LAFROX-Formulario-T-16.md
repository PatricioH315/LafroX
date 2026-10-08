# LafroX — Formulario T-16: Plan de riesgos

Prob. e Impacto usan escalas ordinales 1–5 de SD8 §8.1.3. Expos. = Prob. × Impacto. Evaluación inicial, sin porcentajes estadísticos ni cierre acreditado. Detalle y NPR en Anexos 8.A/8.B; el valor esperado en HH de cada riesgo está en el Anexo 8.B, Tabla B.2. Los responsables dirigen equipos; nominarlos no acredita dotación.

| ID | Riesgo | Categoría | Prob. | Impacto | Expos. | Mitigación | Responsable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R8-01 | ERP indisponible o guía invalidada | Operación | 4 | 5 | 20 | Preemisión nocturna, conciliación carga/guía y ensayo de caída ERP con 96 camiones; plazo: Antes H6; repetir antes H11. Disparador y contingencia: Anexo 8.A R8-01 | ARQ |
| R8-02 | Doble reserva o custodia CD-05 | Técnico | 4 | 5 | 20 | Probar concurrencia, UUID, idempotencia, época de autoridad y retención por lote/ubicación; plazo: Antes H4; regresión H9. Disparador y contingencia: Anexo 8.A R8-02 | DES |
| R8-03 | CD no sostiene 24 horas sin WAN | Operación | 3 | 5 | 15 | Ensayar 24 horas sin WAN con procesos completos y reconciliación; plazo: Antes H5; repetir antes H10. Disparador y contingencia: Anexo 8.A R8-03 | SRE |
| R8-04 | Pérdida o duplicación tras 14 horas offline | Técnico | 4 | 4 | 16 | Ensayar 14 horas offline, reinicio, UUID y reconciliación; plazo: Antes H5 y cada versión móvil. Disparador y contingencia: Anexo 8.A R8-04 | DES |
| R8-05 | Pérdida del sitio supera RPO | Operación | 3 | 5 | 15 | Evaluar supervivencia remota de datos y resolver brecha mediante gobierno de arquitectura; plazo: Resolver diseño y ensayar antes H5/H10. Disparador y contingencia: Anexo 8.A R8-05 | ARQ |
| R8-06 | Carga y cola CD-05 exceden capacidad | Técnico | 4 | 5 | 20 | Medir N/L/retenciones y probar 1,5 veces peak, crecimiento y drenaje; plazo: Antes H5/H10; vigilancia mensual. Disparador y contingencia: Anexo 8.A R8-06 | SRE |
| R8-07 | Ataque o exposición de datos críticos | Seguridad | 4 | 5 | 20 | Pruebas ofensivas, mínimo privilegio, aislamiento, registro y rotación de credenciales; plazo: Antes H5/H10; vigilancia continua. Disparador y contingencia: Anexo 8.A R8-07 | SEG |
| R8-08 | Bloqueo por proveedor | Técnico | 3 | 4 | 12 | Inventariar dependencias, contratos y formatos; ensayar extracción/restauración; plazo: Diseño H2/H8; ensayo anual y salida mes56. Disparador y contingencia: Anexo 8.A R8-08 | ARQ |
| R8-09 | Obsolescencia durante 56 meses | Técnico | 4 | 4 | 16 | Inventariar versiones/soporte y ensayar compatibilidad en QA; plazo: Inventario H2; revisión mensual operación. Disparador y contingencia: Anexo 8.A R8-09 | SRE |
| R8-10 | Interfaces no documentadas exigen retrabajo | Técnico | 4 | 4 | 16 | Capturar muestras/horarios y probar contratos y errores temprano; plazo: Antes H2; integración H4. Disparador y contingencia: Anexo 8.A R8-10 | ARQ |
| R8-11 | Productividad o dotación inferior al modelo | Proyecto | 4 | 5 | 20 | Estimar con equipo/cantidades; asignar competencias y relevos; comprobar el peak de 69 (mes 15), las 48 personas simultáneas de desarrollo y la dotación declarada (T-15 §5.7); vigilar la reserva de cada hito; plazo: Antes línea base; semanal. Disparador y contingencia: Anexo 8.A R8-11 | JP |
| R8-12 | Contrapartes CLIENTE no disponibles | Organizacional | 4 | 4 | 16 | Reservar agenda, responsable/suplente y material por decisión; plazo: Agenda mes1; cada comité quincenal. Disparador y contingencia: Anexo 8.A R8-12 | JP |
| R8-13 | Conocimiento de ruteo no transferido | Organizacional | 3 | 4 | 12 | Capturar reglas/excepciones y validar con planificador y suplente; plazo: Captura meses1–3; probar antes H7. Disparador y contingencia: Anexo 8.A R8-13 | IMP |
| R8-14 | E2 consume capacidad protegida E1 | Proyecto | 4 | 5 | 20 | Separar equipos y proteger 256DES+128CAL HH/mes E1; plazo: Antes mes13; semanal hasta20. Disparador y contingencia: Anexo 8.A R8-14 | DES |
| R8-15 | Perfiles EDI no certificados a tiempo | Proyecto | 4 | 5 | 20 | Acordar pruebas temprano y registrar todos los perfiles/aprobaciones; plazo: Principal antes H10; todas antes activación/F−28 días. Disparador y contingencia: Anexo 8.A R8-15 | DES |
| R8-16 | Migración altera saldos o pierde lotes | Técnico | 4 | 5 | 20 | Perfilar/conteo y dos ensayos; reconciliar SKU/lote/ubicación; plazo: Dos ensayos antes corte/H6. Disparador y contingencia: Anexo 8.A R8-16 | DAT |
| R8-17 | Fecha efectiva elimina ventanas permitidas | Proyecto | 4 | 5 | 20 | Convertir meses a fechas con feriados CLIENTE/prohibiciones; plazo: Mes1 antes H1; antes H6/H11. Disparador y contingencia: Anexo 8.A R8-17 | JP |
| R8-18 | Marcha blanca no cumple seis condiciones | Operación | 4 | 5 | 20 | Activar todo antes F−28 días y demostrar seis condiciones simultáneas; plazo: Diario marcha blanca; H7/H12. Disparador y contingencia: Anexo 8.A R8-18 | CAL |
| R8-19 | Suministros o sala fuera de secuencia | Proyecto | 3 | 5 | 15 | Confirmar responsabilidades BTT/SD4 y compra de terreno CLIENTE; recibir antes montar; plazo: Sala/racks/borde antes H3; terreno antes ola. Disparador y contingencia: Anexo 8.A R8-19 | SRE |
| R8-20 | Rotación y resistencia reducen adopción | Organizacional | 4 | 4 | 16 | Tutor por turno, certificación en puesto y acompañamiento con relevos; plazo: Antes cada ola; mensual. Disparador y contingencia: Anexo 8.A R8-20 | IMP |
| R8-21 | Transportistas o sindicato rechazan dispositivos | Organizacional | 3 | 4 | 12 | Acordar instalación/uso/finalidad/acceso con CLIENTE, terceros y sindicato; plazo: Antes ola de reparto. Disparador y contingencia: Anexo 8.A R8-21 | IMP |
| R8-22 | Mesa cubre horario pero no SLA | Operación | 4 | 4 | 16 | Medir demanda por intervalo y agentes/competencias;04–22 lunes–sábado y24×7 peaks/críticos; plazo: Antes H7/mes21; diario peaks. Disparador y contingencia: Anexo 8.A R8-22 | SRE |
| R8-23 | Frío o sensores no producen evidencia íntegra | Operación | 4 | 5 | 20 | Probar autonomía, almacenamiento/calibración y asociación sensor/lote/tiempo; plazo: Antes ola1/reparto; continuo. Disparador y contingencia: Anexo 8.A R8-23 | SRE |
| R8-24 | Filtración en telemetría o reproducción | Seguridad | 3 | 5 | 15 | Enmascarar, controlar acceso/retención y revisar conjuntos; plazo: Antes usar trazas; cada versión. Disparador y contingencia: Anexo 8.A R8-24 | SEG |
| R8-25 | INN-01 no logra seguimiento posentrega | Organizacional | 4 | 3 | 12 | Piloto asistido y comparación con registro base, sin exigir conexión al almacenero; plazo: Piloto meses11–15. Disparador y contingencia: Anexo 8.A R8-25 | IMP |
| R8-26 | INN-02 no reproduce fallas relevantes | Técnico | 3 | 4 | 12 | Ensayar corte/reinicio/reintento con conjuntos protegidos; plazo: Validación meses11–15; operación. Disparador y contingencia: Anexo 8.A R8-26 | CAL |
| R8-27 | INN-03 estima vida remanente insegura | Técnico | 4 | 5 | 20 | Validar con Calidad y regla conservadora; no ampliar vencimiento por inferencia; plazo: Antes uso meses11–15; revisión26/32/38/44/50/56. Disparador y contingencia: Anexo 8.A R8-27 | DAT |
| R8-28 | INN-04 medición variable genera disputa | Proyecto | 3 | 4 | 12 | Acordar fórmula/datos/auditoría; valores sólo en Oferta Económica; plazo: Modelo17–20; sombra21–23; antes mes24. Disparador y contingencia: Anexo 8.A R8-28 | JP |
| R8-29 | INN-05 baja adopción de hoja del almacenero | Organizacional | 4 | 3 | 12 | Co-diseño/piloto asistido o papel; preservar preventista y efectivo; plazo: Piloto E2; evaluar24–27. Disparador y contingencia: Anexo 8.A R8-29 | IMP |
| R8-30 | Crecimiento o nuevo CD supera parametrización | Técnico | 3 | 4 | 12 | Contrastar distribución real y probar límites de plataforma; plazo: Antes H5/H10; anual. Disparador y contingencia: Anexo 8.A R8-30 | ARQ |
| R8-31 | Observaciones de revisión obligan a repetir certificación paralela | Proyecto | 3 | 4 | 12 | Entregar por incrementos y ejecutar primero los casos independientes de la revisión; repetir sólo los casos afectados con cargo a la reserva del hito; plazo: revisión del H4 y del H9. Disparador: observación sobre un caso ya certificado | CAL |
| R8-32 | Evaluadores subcontratados no disponibles para las certificaciones | Organizacional | 3 | 4 | 12 | Contratar antes de los meses 7 y 14 con disponibilidad por quincena e inducción con casos del T-12; contingencia: reasignación interna y priorización de casos críticos. Disparador: contrato no firmado dos meses antes | CAL |

## Referencias

- Distribuidora Puelche S.A. (2026). Bases Administrativas TFEP-01/2026, artículos 17, 18, 50.2 y formularios T-16/T-22.
- Distribuidora Puelche S.A. (2026). Bases Técnicas Transversales, RT-07.04/07, RT-19.04, RT-21.06/07 y RT-26.04.
- Distribuidora Puelche S.A. (2026). Caso 02 — Logística, capítulos 10–14 y requisitos específicos citados.
- Aclaraciones de licitación (2026), capítulo 8 y reglas de presentación.
- LafroX. SD1–4, SD6 y SD7, con anexos y formularios citados. SD5 no utilizado.
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. ISO.
- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.), capítulo 11. Project Management Institute.

## Declaración de uso de IA

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Formulario T-16 | Codex; Claude Code | Tabla de riesgos desde las fichas del Anexo 8.A (6 de octubre de 2026); actualización de R8-11 y referencias (7 de octubre de 2026) | Alto | Ninguno | No documentada |
