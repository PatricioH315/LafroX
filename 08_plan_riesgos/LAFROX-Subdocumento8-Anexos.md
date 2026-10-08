# LafroX — Subdocumento 8: Anexos

## Anexo 8.A — Registro ampliado de amenazas

Las fichas aplican el proceso de la norma ISO 31000 (International Organization for Standardization [ISO], 2018) que exige el RT-19.04 (Distribuidora Puelche S.A., 2026b), sobre las restricciones del Caso 02 (Distribuidora Puelche S.A., 2026c, Cap. 10) y los temas obligatorios del índice (Distribuidora Puelche S.A., 2026d, sección 11). Cada una se ancla en un subdocumento de la oferta (LafroX, 2026). P, I y D son juicios ordinales iniciales según la sección 8.1.3 del SD8: la causa descrita sustenta P, la consecuencia sustenta I y la forma de detección sustenta D. El cierre de cada ficha exige la evidencia indicada en ella, y los vacíos actuales se distinguen de los eventos inciertos en el Anexo 8.E. Toda ficha se sigue semanalmente y en cada comité, y a diario durante la marcha blanca o la operación afectadas; su puntuación residual se estima sólo después de verificar sus controles.

Las fichas usan los códigos siguientes.

| Código | Significado | Dónde se define |
| --- | --- | --- |
| R8-01 a R8-32 | Riesgos de este plan | Este anexo |
| E8-01 a E8-12 | Condiciones de evidencia actuales | Anexo 8.E |
| H1 a H12 | Hitos contractuales | SD7, Tabla 7.5 |
| E1, E2 | Etapa 1 y Etapa 2 | Bases Administrativas, Art. 17° |
| F y F−28 días | Fecha de paso a producción de una etapa e inicio de sus cuatro semanas finales de marcha blanca | Bases Administrativas, Art. 17.3 |
| Números x.y.z | Paquetes de trabajo de la EDT | Formulario T-14 |
| M1 a M12 | Módulos de la solución | SD3, Tabla 3.4 |
| INT-01 a INT-15 | Interfaces internas y externas | SD4, Anexos 4-G y 4-H |
| AL-STOCK-01, AL-ACT-01 | Protocolos de aceptación de stock y de actualización | SD4, Anexo 4-V |
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
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 101 HH a 67 HH residuales.
- Riesgo secundario: preemitir guías de noche obliga a reemitirlas si la carga cambia, lo que la conciliación carga–guía debe cubrir.
- Costo-beneficio técnico: el control es el paquete 4.1.2, procedimiento de reversión ensayado, de 80 HH ya incluidas en el T-15. Ahorra 34 HH de valor esperado; retorno 0,4: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

### R8-02 — Doble reserva o custodia en la coordinación de reserva

Cortes/reintentos podrían confirmar sin acuse durable o repetir descuentos, alterando stock y trazabilidad.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: SD4, coordinación de reserva de INT-03/04 (Anexo 4-G); AL-STOCK-01 y AL-ACT-01 (Anexo 4-V); 3.3.6, 3.4.2, 3.4.6, 3.8.1.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: hasta la regresión del H9 y cada cambio de la coordinación de reserva. P=4 porque la reserva se coordina entre sitios que se desconectan y reintentan a diario; D=3 porque la conciliación diaria y AL-STOCK-01 lo detectan, pero después de confirmar.
- Responsable de respuesta: DES, con su equipo y contrapartes de su ámbito.
- Disparador: Confirmación sin acuse, UUID repetido o dos autoridades.
- Plazo: Antes H4; regresión H9.
- Mitigación: Probar concurrencia, UUID, idempotencia, época de autoridad y retención por lote/ubicación.
- Contingencia: Bloquear confirmaciones ambiguas y conciliar colas con un único escritor; continuidad sólo sin degradar despacho.
- Evidencia de cierre: AL-STOCK-01/AL-ACT-01 con cero doble descuento/custodia.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 461 HH a 307 HH residuales.
- Riesgo secundario: bloquear las confirmaciones ambiguas puede demorar pedidos durante un corte; se mide en AL-STOCK-01.
- Costo-beneficio técnico: el control es el paquete 3.8.1, pruebas de integración, regresión e idempotencia, de 160 HH ya incluidas en el T-15. Ahorra 154 HH de valor esperado; retorno 0,96: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

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
- Efecto esperado y residual: al verificar el control, P baja de 3 (40 %) a 2 (20 %); el valor esperado baja de 96 HH a 48 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 6.6.3, prueba de autonomía de 24 horas, de 160 HH ya incluidas en el T-15. Ahorra 48 HH de valor esperado; retorno 0,3: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

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
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 384 HH a 256 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 3.8.3, pruebas del perfil operacional, de 320 HH ya incluidas en el T-15. Ahorra 128 HH de valor esperado; retorno 0,4: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

### R8-05 — Pérdida del sitio supera RPO

Falla simultánea de comunicaciones seguida de destrucción del sitio podría eliminar respaldo local y dejar copia remota con más de 15 minutos de pérdida.

- Análisis / categoría: Solución / Operación.
- Fuente y EDT: BTT RT-02.11, RT-07.04/07; SD4 4.3.2.4 riesgo residual DR; 3.8.5, 3.9.4, 8.2.7.
- Evaluación inicial: P=3; I=5; D=5; E=15; NPR=75. Horizonte: los 56 meses. P=3 porque exige la falla de los tres caminos de Talca seguida de la destrucción del sitio; D=5 porque la pérdida sólo se reconoce después de ocurrir.
- Responsable de respuesta: ARQ, con su equipo y contrapartes de su ámbito.
- Disparador: Antigüedad remota > 15 minutos o ensayo multisistema fallido.
- Plazo: Ensayar antes H5/H10.
- Mitigación: Aplicar las medidas del SD4 (4.3.2.4): alarmas de retraso de replicación a los 5 y 15 min, reposición del enlace por el proveedor, preemisión de guías al cerrar la carga y conservación local en el NAS WORM de Talca.
- Contingencia: Aplicar DR probado (imagen del WMS de Talca en Fargate de la región activa), recuperar los datos del NAS WORM y de la última copia remota, y registrar el incidente con la pérdida efectiva.
- Evidencia de cierre: Conmutación real con RPO ≤ 15 min y RTO ≤ 4 h; continuidad de despacho por ensayo separado.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: al verificar el control, P baja de 3 (40 %) a 2 (20 %); el valor esperado baja de 111 HH a 56 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 3.8.5, prueba de recuperación con conmutación real, de 320 HH ya incluidas en el T-15. Ahorra 56 HH de valor esperado; retorno 0,2: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

### R8-06 — Carga y cola de la coordinación de reserva exceden capacidad

El SD4 (Anexo 4-I) supone cuatro mensajes por línea de pedido. Si muchas líneas se reparten entre lotes o sitios y sus retenciones se liberan, el tráfico supera esa cifra, y el peak y el drenaje podrían saturar enlaces o cómputo.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: SD4, Anexo 4-I y sección 4-W.5; Caso RT-09.01; 3.8.4, 3.9.3.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: H5 a H10 y crecimiento anual. P=4 porque las líneas repartidas entre más de un lote o ubicación son habituales; D=3 porque la cola se monitorea, pero su saturación se confirma con prueba de carga.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Más de cuatro mensajes por línea de pedido, cola creciente o latencia incumplida.
- Plazo: Antes H5/H10; vigilancia mensual.
- Mitigación: Medir la proporción de líneas repartidas y de retenciones liberadas, y probar 1,5 veces el peak, el crecimiento y el drenaje.
- Contingencia: Priorizar transacciones y limitar tráfico auxiliar; escalar capacidad por arquitectura sin reducir volumen obligatorio.
- Evidencia de cierre: Carga/latencias y drenaje conformes a multiplicidad medida.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 115 HH a 77 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 3.8.4, pruebas de carga y resiliencia, de 320 HH ya incluidas en el T-15. Ahorra 38 HH de valor esperado; retorno 0,1: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

### R8-07 — Ataque o exposición de datos críticos

Móviles, portales y terceros podrían permitir acceso indebido, ransomware o alteración de lotes/cobros.

- Análisis / categoría: Solución / Seguridad.
- Fuente y EDT: BTT seguridad cap. 13; SD4 seguridad; 3.3.1, 3.8.6, 3.9.5, 8.1.5.
- Evaluación inicial: P=4; I=5; D=4; E=20; NPR=80. Horizonte: los 56 meses. P=4 porque portales, móviles e integraciones con terceros están expuestos de forma permanente; D=4 porque un acceso indebido puede reconocerse recién en la revisión del SIEM.
- Responsable de respuesta: SEG, con su equipo y contrapartes de su ámbito.
- Disparador: Vulnerabilidad crítica/alta o acceso entre clientes.
- Plazo: Antes H5/H10; vigilancia continua.
- Mitigación: Pruebas ofensivas, mínimo privilegio, aislamiento, registro y rotación de credenciales.
- Contingencia: Contener acceso, preservar evidencia y recuperar entorno limpio con continuidad probada.
- Evidencia de cierre: Sin defectos de seguridad críticos/altos abiertos y prueba de recuperación.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 173 HH a 115 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 3.8.6, prueba de seguridad ofensiva de la Etapa 1, de 160 HH ya incluidas en el T-15. Ahorra 58 HH de valor esperado; retorno 0,4: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

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
- Efecto esperado y residual: al verificar el control, P baja de 3 (40 %) a 2 (20 %); el valor esperado baja de 352 HH a 176 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: riesgo de nivel alto, tratado con los paquetes de su EDT ya incluidos en el T-15; su retorno se calcula si sube a nivel crítico (SD8, sección 8.1.3).

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
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 184 HH a 123 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 8.2.5, actualización anual de los componentes de base (un año), de 96 HH ya incluidas en el T-15. Ahorra 61 HH de valor esperado; retorno 0,6: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

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
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 125 HH a 83 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 1.2.3, especificación de las interfaces sin documentación, de 80 HH ya incluidas en el T-15. Ahorra 42 HH de valor esperado; retorno 0,5: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

### R8-11 — Productividad o dotación inferior al modelo

Clases HH/128HH efectivas no medidas podrían subestimar esfuerzo y especialistas, afectando hitos.

- Análisis / categoría: Desarrollo / Proyecto.
- Fuente y EDT: T-15 §§4/5; SD1 dotación declarada; 222 paquetes,1.3.4.
- Evaluación inicial: P=4; I=5; D=3; E=20; NPR=60. Horizonte: hasta el H5. P=4 porque los tamaños por clase y las plantillas de actividades aún no se contrastan con la productividad real, el cronograma por actividad usa toda la división de desarrollo entre julio y septiembre de 2027 y la dotación declarada no cubre SEG ni IMP sin contratación (T-15 §5.7); D=3 porque el valor ganado mensual lo detecta con un mes de atraso.
- Responsable de respuesta: JP, con su equipo y contrapartes de su ámbito.
- Disparador: Estimación supera capacidad por rol/subventana o personas no asignadas.
- Plazo: Antes línea base; semanal.
- Mitigación: Refinar con el equipo la estimación por clase, trazada al T-12 y a las cantidades del T-11; asignar competencias y relevos; comprobar el peak de 69 (mes 15), las 48 personas simultáneas de desarrollo y la dotación declarada (T-15 §5.7); vigilar semanalmente la reserva de cada hito (T-15, Tabla 5.2).
- Contingencia: Reordenar dentro de hitos y sustentar capacidad adicional; no prestar E1 a E2.
- Evidencia de cierre: Asignaciones nominales y cero sobreasignación por subventana.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 4.075 HH a 2.717 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 1.3.4, nivelación de recursos y frentes, de 80 HH ya incluidas en el T-15. Ahorra 1.358 HH de valor esperado; retorno 17,0: el control se justifica por su retorno (Anexo 8.C, Tabla C.5).

### R8-12 — Contrapartes CLIENTE no disponibles

TI de cuatro personas y gerencias podrían no atender decisiones, pruebas o actas a tiempo.

- Análisis / categoría: Desarrollo / Organizacional.
- Fuente y EDT: Caso cap. 10; Aclaraciones §11, 8.2; 1.1.3, 1.8,2.4, 7.3.
- Evaluación inicial: P=4; I=4; D=2; E=16; NPR=32. Horizonte: hasta el H12. P=4 porque el equipo de TI del CLIENTE tiene cuatro personas y atiende la operación; D=2 porque cada revisión tiene fecha registrada y su vencimiento se detecta ese día.
- Responsable de respuesta: JP, con su equipo y contrapartes de su ámbito.
- Disparador: Decisión/revisión no atendida en fecha acordada.
- Plazo: Agenda en el mes 1; cada comité quincenal.
- Mitigación: Reservar agenda, responsable/suplente y material por decisión.
- Contingencia: Escalar a patrocinador y avanzar tareas independientes; silencio no es aceptación.
- Evidencia de cierre: Decisiones/actas explícitas con responsables y fechas.
- Estrategia: Escalar, porque la decisión depende del CLIENTE y excede la autoridad del JP.
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 238 HH a 159 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 1.1.1, acta de constitución con la Contraparte Técnica, de 80 HH ya incluidas en el T-15. Ahorra 79 HH de valor esperado; retorno 0,99: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

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
- Efecto esperado y residual: al verificar el control, P baja de 3 (40 %) a 2 (20 %); el valor esperado baja de 83 HH a 42 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: riesgo de nivel alto, tratado con los paquetes de su EDT ya incluidos en el T-15; su retorno se calcula si sube a nivel crítico (SD8, sección 8.1.3).

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
- Estrategia: Evitar, porque separar los equipos elimina la causa, que es compartir personas entre etapas.
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 1.008 HH a 672 HH residuales.
- Riesgo secundario: separar los equipos de la Etapa 1 y la Etapa 2 exige más personas a la vez y alimenta R8-11.
- Costo-beneficio técnico: el control es el paquete 1.3.4, nivelación de recursos y frentes, de 80 HH ya incluidas en el T-15; el paquete es el mismo de R8-11 y su costo se cuenta una vez. Ahorra 336 HH de valor esperado; retorno 4,2: el control se justifica por su retorno (Anexo 8.C, Tabla C.5).

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
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 346 HH a 230 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 2.1.4, diseño del intercambio con las cadenas, de 240 HH ya incluidas en el T-15. Ahorra 115 HH de valor esperado; retorno 0,5: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

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
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 432 HH a 288 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 3.7.1, perfilamiento y saneamiento de datos, de 480 HH ya incluidas en el T-15. Ahorra 144 HH de valor esperado; retorno 0,3: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

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
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 43 HH a 29 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 1.1.3, acta de fecha de inicio y ventanas de paso a producción, de 80 HH ya incluidas en el T-15. Ahorra 14 HH de valor esperado; retorno 0,2: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

### R8-18 — Marcha blanca no cumple seis condiciones

Defecto alto, volumen incompleto o diferencias podrían persistir en cierre e impedir aceptación. En la Etapa 2, las semanas de cierre caen en el peak de Fiestas Patrias de septiembre de 2028, con cerca de 2.600 entregas diarias y congelamiento del 1 al 25 (SD7, sección 7.3.5).

- Análisis / categoría: Implantación / Operación.
- Fuente y EDT: BA Arts. 17.3 y 18; Caso cap. 19; SD7 7.3.5; T-18; 4.2.1, 4.3.1, 7.3, 3.9.3.
- Evaluación inicial: P=4; I=5; D=2; E=20; NPR=40. Horizonte: cada marcha blanca. P=4 porque las seis condiciones son copulativas y se miden con volumen real; D=2 porque los indicadores son diarios.
- Responsable de respuesta: CAL, con su equipo y contrapartes de su ámbito.
- Disparador: Una condición falla o grupo fuera del alcance.
- Plazo: Diario marcha blanca; H7/H12.
- Mitigación: Activar todo antes de F−28 días y demostrar las seis condiciones simultáneas; en la Etapa 2, habilitar todo en agosto y demostrar la carga a 1,5 veces el peak con ambas etapas activas antes del H11 (3.9.3).
- Contingencia: Extender a costo adjudicatario sin mover fases siguientes; no firmar cumplimiento ficticio.
- Evidencia de cierre: 28 días completos, cero críticos/altos, conciliación, usuarios certificados y acta.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 1.478 HH a 986 HH residuales.
- Riesgo secundario: extender una marcha blanca a costo del adjudicatario sin mover las fases siguientes presiona la capacidad del solapamiento (R8-14).
- Costo-beneficio técnico: el control es el paquete 4.1.1, plan de olas, y 7.3.1, certificación de usuarios, de 240 HH ya incluidas en el T-15. Ahorra 493 HH de valor esperado; retorno 2,1: el control se justifica por su retorno (Anexo 8.C, Tabla C.5).

### R8-19 — Suministros o sala fuera de secuencia

La sala se instala desde el mes 3, por lo que el CLIENTE debe comprar lo especificado dentro del mes siguiente a la aprobación de 5.1.2; una compra, recepción o configuración tardía podría bloquear el H3 o una ola pese a HH disponibles.

- Análisis / categoría: Implantación / Proyecto.
- Fuente y EDT: BTT recinto; Caso cap. 11; SD7 D-09–13/26; 5.1.2, 6.1,6.3, 6.6.3, 6.5.
- Evaluación inicial: P=3; I=5; D=3; E=15; NPR=45. Horizonte: hasta el H3. P=3 porque la compra del CLIENTE debe cerrarse en un mes y la instalación depende de proveedores externos; D=3 porque las actas de recepción lo revelan.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Orden de compra del CLIENTE no emitida al cierre del mes 3, suministro posterior a montaje o dispositivo ausente.
- Plazo: Sala, racks y borde antes H3; terreno antes ola.
- Mitigación: Acordar en el mes 1 el calendario de compra del CLIENTE (1.1.3 y 5.1.3); confirmar responsabilidades BTT/SD4; recibir antes de montar.
- Contingencia: Recuperar suministro/instalación con capacidad específica; no activar equipos inexistentes.
- Evidencia de cierre: Actas y pruebas en secuencia sala, racks, borde y terreno.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: al verificar el control, P baja de 3 (40 %) a 2 (20 %); el valor esperado baja de 317 HH a 158 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 5.1.2, especificación de compra, y 5.1.3, actas de recepción, de 160 HH ya incluidas en el T-15. Ahorra 158 HH de valor esperado; retorno 0,99: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

### R8-20 — Rotación y resistencia reducen adopción

Rotación 38 % de preparación y personal antiguo podrían dejar turnos sin usuarios certificados.

- Análisis / categoría: Implantación / Organizacional.
- Fuente y EDT: Caso restricciones; T-18; 7.1.2, 7.2.1, 7.3.1/2.
- Evaluación inicial: P=4; I=4; D=3; E=16; NPR=48. Horizonte: los 56 meses. P=4 porque el turno de noche rota 38 % al año; D=3 porque la certificación por usuario lo detecta antes de cada turno.
- Responsable de respuesta: IMP, con su equipo y contrapartes de su ámbito.
- Disparador: Usuario sin certificar o uso incompleto.
- Plazo: Antes cada ola; mensual.
- Mitigación: Tutor por turno, certificación en puesto y acompañamiento con relevos.
- Contingencia: Retener/restaurar acompañamiento y repetir formación sin detener rutas.
- Evidencia de cierre: Usuarios por perfil/turno certificados y uso sostenido.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 150 HH a 100 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 7.3.1, certificación de usuarios de la Etapa 1, de 160 HH ya incluidas en el T-15; el paquete es el mismo de R8-18 y su costo se cuenta una vez. Ahorra 50 HH de valor esperado; retorno 0,3: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

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
- Efecto esperado y residual: al verificar el control, P baja de 3 (40 %) a 2 (20 %); el valor esperado baja de 90 HH a 45 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: riesgo de nivel alto, tratado con los paquetes de su EDT ya incluidos en el T-15; su retorno se calcula si sube a nivel crítico (SD8, sección 8.1.3).

### R8-22 — Mesa cubre horario pero no SLA

Las posiciones de mesa dimensionadas con Erlang C podrían no bastar si la demanda o el tiempo de atención difieren del supuesto, y el modelo no verifica el abandono ≤5 % ni la resolución al primer contacto ≥70 %.

- Análisis / categoría: Implantación / Operación.
- Fuente y EDT: BTT RT-21.06/07; Caso RT-21.06; 4.2.2, 8.1.1, 8.1.2.
- Evaluación inicial: P=4; I=4; D=3; E=16; NPR=48. Horizonte: meses 13 a 56. P=4 porque la demanda de 2.000 contactos/mes es una estimación sin medición y la del año 3 queda a 1,1 % del límite de 2.283; D=3 porque la medición por contacto empieza en la marcha blanca.
- Responsable de respuesta: SRE, con su equipo y contrapartes de su ámbito.
- Disparador: Demanda/tiempos exceden umbral o falta relevo.
- Plazo: Antes del H7 (mes 16) y del H12 (mes 21); diario peaks.
- Mitigación: Medir la demanda por intervalo y los agentes y competencias; 04:00–22:00 de lunes a sábado y 24×7 en peaks y críticos.
- Contingencia: Activar agentes adicionales verificados y guardia especialista.
- Evidencia de cierre: Prueba de demanda/turnos con los tres SLA y horarios.
- Estrategia: Aceptar activamente, porque no hay control previo rentable; se reserva la contingencia con disparador.
- Efecto esperado y residual: P se mantiene en 4 (60 %); el valor esperado de 3.182 HH queda como residual, cubierto por la reserva de contingencia y activado por el disparador.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: sin control previo con horas propias; la medición por contacto va dentro de la mesa (8.1.2), y la contingencia, el escenario C-05 de 442 HH al mes, sólo se gasta si la demanda medida supera 2.200 contactos al mes.

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
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 403 HH a 269 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 6.5.3, sensores y gateways instalados y calibrados, de 160 HH ya incluidas en el T-15. Ahorra 134 HH de valor esperado; retorno 0,8: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

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
- Efecto esperado y residual: al verificar el control, P baja de 3 (40 %) a 2 (20 %); el valor esperado baja de 192 HH a 96 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: el control es el paquete 3.8.6, prueba de seguridad ofensiva de la Etapa 1, de 160 HH ya incluidas en el T-15; el paquete es el mismo de R8-07 y su costo se cuenta una vez. Ahorra 96 HH de valor esperado; retorno 0,6: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

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
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 67 HH a 45 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: riesgo de nivel alto, tratado con los paquetes de su EDT ya incluidos en el T-15; su retorno se calcula si sube a nivel crítico (SD8, sección 8.1.3).

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
- Efecto esperado y residual: al verificar el control, P baja de 3 (40 %) a 2 (20 %); el valor esperado baja de 92 HH a 46 HH residuales.
- Riesgo secundario: capturar evidencia de terreno crea el riesgo de filtración R8-24.
- Costo-beneficio técnico: riesgo de nivel alto, tratado con los paquetes de su EDT ya incluidos en el T-15; su retorno se calcula si sube a nivel crítico (SD8, sección 8.1.3).

### R8-27 — INN-03 estima vida remanente insegura

Historia incompleta o mala calibración podría sugerir una vida útil no segura. Causa secundaria: Operaciones podría leer la estimación como permiso para relajar la regla graduada RNG-04.

- Análisis / categoría: Solución / Técnico.
- Fuente y EDT: SD7 INN-03; SD3 M9/M12; BTT RT-26.04; 3.10.3, 8.3.2.
- Evaluación inicial: P=4; I=5; D=4; E=20; NPR=80. Horizonte: los 56 meses. P=4 porque la calibración inicial tiene poca historia térmica; D=4 porque un error de estimación puede reconocerse sólo cuando el producto se reclama.
- Responsable de respuesta: DAT, con su equipo y contrapartes de su ámbito.
- Disparador: Resultado fuera de criterio Calidad o historial faltante.
- Plazo: Antes del uso en los meses 11–15; revisión en los meses 26, 32, 38, 44, 50 y 56.
- Mitigación: Validar con Calidad y regla conservadora; no ampliar vencimiento por inferencia; la regla graduada y el bloqueo de B-02 no cambian.
- Contingencia: Deshabilitar recomendación y mantener vencimiento/control sanitario.
- Evidencia de cierre: Validación Calidad con trazabilidad modelo/datos.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 190 HH a 127 HH residuales.
- Riesgo secundario: Operaciones podría leer la estimación como permiso para relajar la regla RNG-04.
- Costo-beneficio técnico: el control es el paquete 3.10.3.4, validación de INN-03 con Calidad, de 240 HH ya incluidas en el T-15. Ahorra 63 HH de valor esperado; retorno 0,3: el retorno en HH es menor que 1 y el control se aplica por la regla del nivel crítico (SD8, sección 8.1.3) (Anexo 8.C, Tabla C.5).

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
- Efecto esperado y residual: al verificar el control, P baja de 3 (40 %) a 2 (20 %); el valor esperado baja de 28 HH a 14 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: riesgo de nivel alto, tratado con los paquetes de su EDT ya incluidos en el T-15; su retorno se calcula si sube a nivel crítico (SD8, sección 8.1.3).

### R8-29 — INN-05 baja adopción de hoja del almacenero

La hoja podría no ser comprensible o útil y quedar sin uso. Causa secundaria: el bloque 4 comparativo podría permitir inferir las cifras de un local vecino.

- Análisis / categoría: Implantación / Organizacional.
- Fuente y EDT: SD7 INN-05; Caso canal tradicional; BTT RT-26.04; 3.10.4, 8.3.5, 8.3.6.
- Evaluación inicial: P=4; I=3; D=2; E=12; NPR=24. Horizonte: piloto de INN-05. P=4 porque muchos almaceneros no usan herramientas digitales; D=2 porque las métricas de uso se ven cada semana.
- Responsable de respuesta: IMP, con su equipo y contrapartes de su ámbito.
- Disparador: Uso/beneficio menor al objetivo acordado antes piloto.
- Plazo: Piloto en la Etapa 2; evaluar en los meses 24–27.
- Mitigación: Co-diseño/piloto asistido o papel; preservar preventista y efectivo; umbral mínimo de locales y supresión de celdas en el bloque 4, con revisión legal previa.
- Contingencia: Retirar mejora opcional mediante gobierno manteniendo compromisos y canal obligatorio.
- Evidencia de cierre: Utilidad/uso contrastados y decisión documentada.
- Estrategia: Mitigar, porque LafroX controla la causa y el control reduce la probabilidad.
- Efecto esperado y residual: al verificar el control, P baja de 4 (60 %) a 3 (40 %); el valor esperado baja de 67 HH a 45 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: riesgo de nivel alto, tratado con los paquetes de su EDT ya incluidos en el T-15; su retorno se calcula si sube a nivel crítico (SD8, sección 8.1.3).

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
- Efecto esperado y residual: al verificar el control, P baja de 3 (40 %) a 2 (20 %); el valor esperado baja de 133 HH a 67 HH residuales.
- Riesgo secundario: no se identifica.
- Costo-beneficio técnico: riesgo de nivel alto, tratado con los paquetes de su EDT ya incluidos en el T-15; su retorno se calcula si sube a nivel crítico (SD8, sección 8.1.3).

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
- Efecto esperado y residual: al verificar el control, P baja de 3 (40 %) a 2 (20 %); el valor esperado baja de 154 HH a 77 HH residuales.
- Riesgo secundario: ninguno nuevo; R8-31 es a su vez el riesgo secundario de certificar en paralelo a la revisión del CLIENTE.
- Costo-beneficio técnico: riesgo de nivel alto, tratado con los paquetes de su EDT ya incluidos en el T-15; su retorno se calcula si sube a nivel crítico (SD8, sección 8.1.3).

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
- Efecto esperado y residual: al verificar el control, P baja de 3 (40 %) a 2 (20 %); el valor esperado baja de 205 HH a 102 HH residuales.
- Riesgo secundario: ninguno nuevo; R8-32 es a su vez el riesgo secundario de reforzar la calidad con evaluadores subcontratados.
- Costo-beneficio técnico: riesgo de nivel alto, tratado con los paquetes de su EDT ya incluidos en el T-15; su retorno se calcula si sube a nivel crítico (SD8, sección 8.1.3).

## Anexo 8.B — FMEA y exposición inicial

### B.1 Prioridad cualitativa

La tabla reúne la evaluación inicial de las 32 fichas del Anexo 8.A con la escala del SD8, sección 8.1.3, y su justificación individual en cada ficha. El número de prioridad sigue la IEC 60812 (International Electrotechnical Commission [IEC], 2018).

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

Orden dentro del nivel: NPR descendente, impacto y proximidad del plazo. R8-05 tiene NPR 75 e impacto 5 y requiere escalamiento por el riesgo residual que el SD4 declara en 4.3.2.4, registrado en 8.E. R8-01, R8-07 y R8-27 alcanzan NPR 80. No se interpreta NPR como porcentaje ni se estiman puntajes residuales sin evidencia.

### B.2 Cuantificación en horas hombre

La tabla aplica la calibración del SD8, sección 8.1.3. La base son las HH de los paquetes que la ficha nombra (los paquetes recurrentes cuentan doce meses y los de cobertura o acompañamiento no se incluyen); R8-18 y R8-22, cuyos paquetes son de acompañamiento y cobertura, usan los escenarios C-04 y C-05 del Anexo 8.C. Las filas están ordenadas de mayor a menor valor esperado, con su porcentaje acumulado.

**Tabla B.2 — Valor esperado por riesgo. Fuente: elaboración propia a partir del Anexo 8.A y del Formulario T-15.**

| ID | Riesgo | P (probabilidad) | I | Base (HH) | Fracción | Impacto (HH) | Valor esperado (HH) | Acumulado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8-11 | Productividad o dotación inferior al modelo | 4 (60 %) | 5 | 22.640 | 30 % | 6.792 | 4.075 | 27,0 % |
| R8-22 | Mesa cubre horario pero no SLA | 4 (60 %) | 4 | Escenario C-05, 12 meses | — | 5.304 | 3.182 | 48,1 % |
| R8-18 | Marcha blanca no cumple seis condiciones | 4 (60 %) | 5 | Escenario C-04 | — | 2.464 | 1.478 | 57,9 % |
| R8-14 | E2 consume capacidad protegida E1 | 4 (60 %) | 5 | 5.600 | 30 % | 1.680 | 1.008 | 64,6 % |
| R8-02 | Doble reserva o custodia en la coordinación de reserva | 4 (60 %) | 5 | 2.560 | 30 % | 768 | 461 | 67,7 % |
| R8-16 | Migración altera saldos o pierde lotes | 4 (60 %) | 5 | 2.400 | 30 % | 720 | 432 | 70,6 % |
| R8-23 | Frío o sensores no producen evidencia íntegra | 4 (60 %) | 5 | 2.240 | 30 % | 672 | 403 | 73,2 % |
| R8-04 | Pérdida o duplicación tras 14 horas offline | 4 (60 %) | 4 | 3.200 | 20 % | 640 | 384 | 75,8 % |
| R8-08 | Bloqueo por proveedor | 3 (40 %) | 4 | 4.400 | 20 % | 880 | 352 | 78,1 % |
| R8-15 | Perfiles EDI no certificados a tiempo | 4 (60 %) | 5 | 1.920 | 30 % | 576 | 346 | 80,4 % |
| R8-19 | Suministros o sala fuera de secuencia | 3 (40 %) | 5 | 2.640 | 30 % | 792 | 317 | 82,5 % |
| R8-12 | Contrapartes CLIENTE no disponibles | 4 (60 %) | 4 | 1.984 | 20 % | 397 | 238 | 84,1 % |
| R8-32 | Evaluadores subcontratados no disponibles para las certificaciones | 3 (40 %) | 4 | 2.560 | 20 % | 512 | 205 | 85,4 % |
| R8-24 | Filtración en telemetría o reproducción | 3 (40 %) | 5 | 1.600 | 30 % | 480 | 192 | 86,7 % |
| R8-27 | INN-03 estima vida remanente insegura | 4 (60 %) | 5 | 1.056 | 30 % | 317 | 190 | 88,0 % |
| R8-09 | Obsolescencia durante 56 meses | 4 (60 %) | 4 | 1.536 | 20 % | 307 | 184 | 89,2 % |
| R8-07 | Ataque o exposición de datos críticos | 4 (60 %) | 5 | 960 | 30 % | 288 | 173 | 90,3 % |
| R8-31 | Observaciones de revisión obligan a repetir certificación paralela | 3 (40 %) | 4 | 1.920 | 20 % | 384 | 154 | 91,4 % |
| R8-20 | Rotación y resistencia reducen adopción | 4 (60 %) | 4 | 1.248 | 20 % | 250 | 150 | 92,4 % |
| R8-30 | Crecimiento o nuevo CD supera parametrización | 3 (40 %) | 4 | 1.664 | 20 % | 333 | 133 | 93,2 % |
| R8-10 | Interfaces no documentadas exigen retrabajo | 4 (60 %) | 4 | 1.040 | 20 % | 208 | 125 | 94,1 % |
| R8-06 | Carga y cola de la coordinación de reserva exceden capacidad | 4 (60 %) | 5 | 640 | 30 % | 192 | 115 | 94,8 % |
| R8-05 | Pérdida del sitio supera RPO | 3 (40 %) | 5 | 928 | 30 % | 278 | 111 | 95,6 % |
| R8-01 | ERP indisponible o guía invalidada | 4 (60 %) | 5 | 560 | 30 % | 168 | 101 | 96,2 % |
| R8-03 | CD no sostiene 24 horas sin WAN | 3 (40 %) | 5 | 800 | 30 % | 240 | 96 | 96,9 % |
| R8-26 | INN-02 no reproduce fallas relevantes | 3 (40 %) | 4 | 1.152 | 20 % | 230 | 92 | 97,5 % |
| R8-21 | Transportistas o sindicato rechazan dispositivos | 3 (40 %) | 4 | 1.120 | 20 % | 224 | 90 | 98,1 % |
| R8-13 | Conocimiento de ruteo no transferido | 3 (40 %) | 4 | 1.040 | 20 % | 208 | 83 | 98,6 % |
| R8-25 | INN-01 no logra seguimiento posentrega | 4 (60 %) | 3 | 1.120 | 10 % | 112 | 67 | 99,1 % |
| R8-29 | INN-05 baja adopción de hoja del almacenero | 4 (60 %) | 3 | 1.120 | 10 % | 112 | 67 | 99,5 % |
| R8-17 | Fecha efectiva elimina ventanas permitidas | 4 (60 %) | 5 | 240 | 30 % | 72 | 43 | 99,8 % |
| R8-28 | INN-04 medición variable genera disputa | 3 (40 %) | 4 | 352 | 20 % | 70 | 28 | 100,0 % |
| **Total** |  |  |  |  |  |  | **15.076** |  |

Los valores de cada fila se redondean a la hora; el total y los porcentajes acumulados se calculan sin redondear.

El valor esperado no es lo que costará cada riesgo: si ocurre, cuesta su impacto completo, y si no, nada. Sumado sobre todo el registro, estima el esfuerzo que la incertidumbre conocida agregará al proyecto y dimensiona la reserva de contingencia (SD8, sección 8.3.2).

## Anexo 8.C — Escenarios deterministas y costo-beneficio

Este anexo cuantifica en horas hombre y en meses los efectos de los escenarios que usan las fichas, con reglas reproducibles, y presenta la simulación de Monte Carlo del cronograma (C.3).

### C.1 Reglas y unidades

T-15 supone 128 HH efectivas/persona-mes; módulo D = 960 HH, integración I = 480 HH, prueba de integración/certificación = 160 HH y prueba ampliada = 320 HH. Duración por perfil = HH extra / capacidad disponible del perfil. En paralelo se usa el máximo; en secuencia, la suma. No se suman demoras correlacionadas sin modelar el camino.

| Escenario | Cálculo reproducible | Efecto y decisión |
| --- | --- | --- |
| C-01 Corrección E1 meses 13–20 (R8-02/04/14) | 25 % × 960 = 240 HH DES + 160 HH CAL = 400 HH. Máximo(240/256,160/128) = 1,25 meses con reserva mensual | No cabe en un mes por CAL: agregar 32 HH CAL a ese mes o distribuir si la ventana y aceptación lo permiten. Registrar 400 HH una sola vez. Antes de H5 esa reserva no está disponible |
| C-02 Retrabajo EDI previo H10 (R8-10/15) | 50 % × 480 = 240 HH DES + 160 HH CAL = 400 HH. Dos DES y dos CAL adicionales darían máximo(240/256,160/256) = 0,9375 mes en paralelo; si secuencial, 0,9375 + 0,625 = 1,5625 meses | Es una necesidad de escenario, no dotación ni reserva acreditada. El orden real de corrección y prueba determina duración; no prestar reserva E1 a E2 |
| C-03 Demora de construcción o integración (R8-10/11) | La reserva programada es 19 días hábiles antes de la entrega del H4, 35 antes del H5, 21 antes del H9 y 28 antes del H10 (T-15, Tabla 5.2). Una demora de 10 días hábiles en la integración E2 (3.9.1) deja 11 días de reserva antes del H9 | Recuperar con capacidad o secuencia dentro de la reserva; si la demora proyectada supera la mitad de la reserva, replanificar antes del hito. La probabilidad conjunta con los demás riesgos está en C.3. No convertir el pronóstico en fecha contractual |
| C-04 Acompañamiento adicional (R8-18/20) | Cuatro semanas: 12 × 24 × 8 + 160 = 2.464 HH IMP; techo(2464/128) = 20 personas equivalentes | Los 12 puestos simultáneos necesitan relevos. Sólo es aumento de HH si excede el acompañamiento ya incluido; verificar el calendario de esa extensión |
| C-05 Tercer agente de mesa en las franjas valle (R8-22) | 17 horas × 26 días de lunes a sábado = 442 HH/mes; techo(442/128) = 4 personas equivalentes | Se activa si la demanda medida supera 2.200 contactos/mes y eleva el límite de 2.283 a 2.391 contactos/mes (SD4, Anexo 4-W.7). Es capacidad de escenario, no incluida en el T-15; abandono y resolución al primer contacto se miden aparte |
| C-06 Reversión (R8-01) | Máximo(10 min técnicos,30 min preparación operacional) + 10 min validación = 40 min; 04:45 + 40 = 05:25 | Objetivo con cinco minutos hasta 05:30, sin medición. Ensayar 96 despachos y fallos ERP/carga. RTO general de cuatro horas no admite detener despacho |
| C-07 Evidencia completa (R8-17/18) | Activación completa antes de F−28 días. E1 ejemplo: F=01-05-2028 ⇒ 03–30 abril; E2: F=01-10-2028 ⇒ 03–30 septiembre | E1 remanentes semana 8 de marzo; E2 habilitaciones en agosto antes de congelamiento 01–25 septiembre. Aplicar los primeros tres días hábiles y feriados CLIENTE; mantener evidencia hasta acta |
| C-08 Mensajes de la coordinación de reserva (R8-06) | Una línea con una retención usa cuatro mensajes (SD4, Anexo 4-I). Repartida en dos retenciones que se liberan, usa ocho; si ambas se consumen, cuatro. Si 10 % de las líneas se reparten y se liberan, el flujo sube de 46.968 a 46.968 × 1,10 = 51.665 mensajes diarios, antes de descontar la holgura de las retenciones consumidas | No implica el mismo aumento en todo el tráfico. Medir la proporción con AL-STOCK-01 y contrastar el Anexo 4-I con ARQ y SRE; no alterar aquí la memoria física |

Los porcentajes 25 % y 50 % son variaciones hipotéticas de esfuerzo, no probabilidades de evento. Los escenarios no constituyen una bolsa adicional sumable: varios pueden describir el mismo defecto.

### C.2 Comparación de prevención y retrabajo

Una respuesta se justifica si reduce el valor esperado más de lo que cuesta (PMI, 2017, pp. 442–443). El ahorro esperado de cada riesgo crítico es la diferencia entre su valor esperado inicial y el residual, con la probabilidad un nivel más baja tras verificar el control (Anexo 8.A). El retorno divide ese ahorro por las HH del paquete que ejecuta el control en el Formulario T-15. Un control incluido en el T-15 no vuelve a cargarse como reserva, y un mismo paquete que controla dos riesgos se cuenta una vez. La Tabla C.5 presenta los 22 riesgos críticos.

**Tabla C.5 — Costo-beneficio del control de cada riesgo crítico. Fuente: elaboración propia a partir de la Tabla B.2 y del Formulario T-15, sección 4.2.**

| ID | Paquete de control | HH del control | VE inicial (HH) | VE residual (HH) | Ahorro esperado (HH) | Retorno |
| --- | --- | --- | --- | --- | --- | --- |
| R8-01 | 4.1.2, procedimiento de reversión ensayado | 80 | 101 | 67 | 34 | 0,4 |
| R8-02 | 3.8.1, pruebas de integración, regresión e idempotencia | 160 | 461 | 307 | 154 | 0,96 |
| R8-03 | 6.6.3, prueba de autonomía de 24 horas | 160 | 96 | 48 | 48 | 0,3 |
| R8-04 | 3.8.3, pruebas del perfil operacional | 320 | 384 | 256 | 128 | 0,4 |
| R8-05 | 3.8.5, prueba de recuperación con conmutación real | 320 | 111 | 56 | 56 | 0,2 |
| R8-06 | 3.8.4, pruebas de carga y resiliencia | 320 | 115 | 77 | 38 | 0,1 |
| R8-07 | 3.8.6, prueba de seguridad ofensiva de la Etapa 1 | 160 | 173 | 115 | 58 | 0,4 |
| R8-09 | 8.2.5, actualización anual de los componentes de base (un año) | 96 | 184 | 123 | 61 | 0,6 |
| R8-10 | 1.2.3, especificación de las interfaces sin documentación | 80 | 125 | 83 | 42 | 0,5 |
| R8-11 | 1.3.4, nivelación de recursos y frentes | 80 | 4.075 | 2.717 | 1.358 | 17,0 |
| R8-12 | 1.1.1, acta de constitución con la Contraparte Técnica | 80 | 238 | 159 | 79 | 0,99 |
| R8-14 | 1.3.4, nivelación de recursos y frentes | 80 | 1.008 | 672 | 336 | 4,2 |
| R8-15 | 2.1.4, diseño del intercambio con las cadenas | 240 | 346 | 230 | 115 | 0,5 |
| R8-16 | 3.7.1, perfilamiento y saneamiento de datos | 480 | 432 | 288 | 144 | 0,3 |
| R8-17 | 1.1.3, acta de fecha de inicio y ventanas de paso a producción | 80 | 43 | 29 | 14 | 0,2 |
| R8-18 | 4.1.1, plan de olas, y 7.3.1, certificación de usuarios | 240 | 1.478 | 986 | 493 | 2,1 |
| R8-19 | 5.1.2, especificación de compra, y 5.1.3, actas de recepción | 160 | 317 | 158 | 158 | 0,99 |
| R8-20 | 7.3.1, certificación de usuarios de la Etapa 1 | 160 | 150 | 100 | 50 | 0,3 |
| R8-22 | Sin control previo; medición dentro de 8.1.2 | — | 3.182 | 3.182 | 0 | — |
| R8-23 | 6.5.3, sensores y gateways instalados y calibrados | 160 | 403 | 269 | 134 | 0,8 |
| R8-24 | 3.8.6, prueba de seguridad ofensiva de la Etapa 1 | 160 | 192 | 96 | 96 | 0,6 |
| R8-27 | 3.10.3.4, validación de INN-03 con Calidad | 240 | 190 | 127 | 63 | 0,3 |

El retorno supera 1 en 3 de los 21 controles: R8-11 (17,0), R8-14 (4,2), R8-18 (2,1). En los otros 18 el ahorro medido sólo en retrabajo es menor que el costo del control, entre 0,1 y 0,99. La razón es que la Tabla B.2 mide el impacto como HH de retrabajo en los paquetes afectados, y no incluye la detención del despacho, la sanción sanitaria, el incumplimiento de un hito ni la pérdida de datos, que son las consecuencias que dan a esos riesgos impacto 4 o 5. Para ellos rige la regla del nivel crítico del SD8, sección 8.1.3: un riesgo crítico se trata aunque su retorno en HH sea menor que 1. Además, la mayoría de esos controles son pruebas, actas o planes que las Bases exigen como entregables. R8-22 se acepta activamente: no gasta horas antes del evento y su contingencia C-05 se activa sólo con la demanda medida.

En despacho, seguridad, sanidad y RPO, la conformidad es obligatoria; las HH ayudan a escoger alternativas conformes. Retirar una innovación que no rinde exige gobierno y preservar compromisos contratados; no elimina funciones obligatorias.

### C.3 Simulación de Monte Carlo del cronograma

El modelo es la red de los 163 paquetes con entregable del Formulario T-15, sección 6.1, con sus dependencias del Anexo 7.B y las fechas de inicio programadas como fechas de liberación. En cada una de las 5.000 iteraciones:

- la duración de cada paquete se toma de una distribución PERT con O = 0,75 d, M = d y P = 1,25 d, que es una beta(3, 3) escalada;
- cada riesgo de la Tabla B.2 ocurre con su probabilidad; si ocurre, la duración de cada paquete afectado crece en la fracción de su impacto, y los efectos de varios riesgos sobre un mismo paquete se suman;
- se recalculan las fechas por las dependencias y se registra la entrega de cada hito.

R8-18 y R8-22 no se simulan porque afectan la duración de las marchas blancas y la operación, que tienen fechas contractuales fijas; se cubren con la reserva de contingencia. La simulación no nivela recursos en cada iteración: supone que el equipo asignado a un paquete se mantiene mientras se alarga.

**Tabla C.3 — Resultado por hito. Fuente: elaboración propia.**

| Hito | Fecha límite de entrega | P50 | P80 | P(entrega a tiempo) |
| --- | --- | --- | --- | --- |
| H1 | 17-03-2027 | 09-03-2027 | 10-03-2027 | > 99,9 % |
| H2 | 17-05-2027 | 06-04-2027 | 09-04-2027 | > 99,9 % |
| H3 | 16-07-2027 | 30-06-2027 | 09-07-2027 | 98,6 % |
| H4 | 16-11-2027 | 28-10-2027 | 03-11-2027 | > 99,9 % |
| H5 | 17-01-2028 | 27-12-2027 | 05-01-2028 | 97,7 % |
| H8 | 17-03-2028 | 06-03-2028 | 09-03-2028 | 99,3 % |
| H9 | 16-06-2028 | 06-06-2028 | 14-06-2028 | 89,9 % |
| H10 | 17-07-2028 | 30-06-2028 | 07-07-2028 | 97,7 % |

**Tabla C.4 — Sensibilidad: probabilidad de entrega a tiempo si el riesgo no existiera (3.000 iteraciones). Fuente: elaboración propia.**

| Riesgo | H3 | H5 | H9 | H10 |
| --- | --- | --- | --- | --- |
| Con todos los riesgos | 98,6 % | 97,9 % | 90,5 % | 97,8 % |
| Sin R8-11 Productividad o dotación | 99,2 % | 99,2 % | 99,2 % | 97,7 % |
| Sin R8-14 Capacidad E1 usada por E2 | 99,2 % | 97,6 % | 100,0 % | 100,0 % |
| Sin R8-15 Perfiles EDI | 99,2 % | 97,6 % | 97,4 % | 97,9 % |
| Sin R8-19 Suministros o sala | 100,0 % | 97,6 % | 89,9 % | 97,8 % |
| Sin R8-23 Evidencia de frío | 98,9 % | 99,3 % | 89,9 % | 97,8 % |
| Sin R8-31 Certificación repetida | 98,9 % | 98,7 % | 89,9 % | 99,5 % |
| Sin R8-32 Evaluadores subcontratados | 98,9 % | 99,1 % | 89,9 % | 99,9 % |
| Sin R8-06 Carga de la coordinación de reserva | 99,2 % | 97,6 % | 90,0 % | 98,8 % |

La lectura es la del diagrama de tornado (PMI, 2017, p. 434): el H9 depende sobre todo de mantener separada la capacidad de la Etapa 1 (R8-14), de la productividad (R8-11) y de la certificación de las cadenas (R8-15); el H10, de R8-14 y del refuerzo de calidad (R8-32, R8-31); el H5, de la evidencia de frío (R8-23), la productividad y el refuerzo de calidad; el H3, de la compra del CLIENTE (R8-19). Esos riesgos tienen seguimiento semanal en el Comité de Proyecto. La Tabla C.4 se compara contra su propia fila «Con todos los riesgos», calculada con 3.000 iteraciones; por eso difiere en décimas de la Tabla C.3, de 5.000. Las diferencias menores a un punto, incluidas las que dejan una fila bajo esa base, están dentro del error de muestreo.

## Anexo 8.D — Reservas, autorización y programación

La tabla siguiente fija las reservas, quién autoriza su uso y cuándo se programan.

| Componente | HH / ventana | Inclusión y regla |
| --- | --- | --- |
| Corrección protegida E1 | 8 × (256 DES + 128 CAL) = 3.072 HH; meses 13–20 | Ya incluida en 202.774 HH. Remanente inicial de planificación 3.072; consumo real no informado. No prestar a E2 ni usar antes del mes 13 |
| Soporte puente E1 | 9.336 HH SRE; meses 16–20 | Servicio base ya incluido; no reserva de desarrollo |
| Cierre/estabilización implementación meses 21–22 | 2.774,54 HH | Separado de operación en T-15; no añadir de nuevo |
| Reserva de cronograma | Reserva entre la entrega y la fecha límite de cada hito (T-15, Tabla 5.2), dimensionada para que la fecha P80 simulada quede antes de la fecha límite (Tabla C.3) | Se consume sólo por desviaciones registradas; no se presta entre hitos |
| Últimas cuatro semanas de marcha blanca | 0 días disponibles como reserva | Evidencia obligatoria, no tiempo para completar alcance |
| Reserva de contingencia | 15.076 HH, suma de los valores esperados de la Tabla B.2, repartidas por período en el SD8, sección 8.3.2. La capacidad protegida E1 absorbe sólo R8-02, R8-04 y R8-14 (1.853 HH); la contingencia adicional es de 13.223 HH | Cubre riesgos identificados y forma parte de la línea base. La usa el JP con el riesgo declarado, y se libera cuando el riesgo se cierra sin ocurrir o cuando la verificación de su control baja el valor esperado al residual; si todos los controles se verifican, se liberan 4.273 HH y quedan 10.803 HH. Los escenarios C-01 a C-05 son usos típicos: corrección E1 (400 HH), retrabajo EDI (400 HH), extensión de marcha blanca (2.464 HH por cuatro semanas) y tercer agente de mesa (442 HH/mes). Cada uso se registra contra el riesgo que lo origina; no se presta entre etapas |
| Reserva de gestión | Riesgos no identificados; no se expresa en HH en esta oferta técnica | No forma parte de la línea base; la autoriza el Comité Ejecutivo y usarla exige actualizar la línea base; su monto se define en la Oferta Económica (Art. 50.2) |

Por evento se registra ID relacionado, mes/subventana, perfil, HH autorizadas/consumidas, remanente y efecto en hitos. Si R8-02 y R8-04 representan el mismo defecto, comparten cargo. La ampliación de marcha blanca se rige por el Art. 17.3 (Distribuidora Puelche S.A., 2026a) a costo del adjudicatario y sin mover fases siguientes; ninguna reserva lo deroga.

## Anexo 8.E — Problemas, dependencias y condiciones de evidencia

Estas entradas son estados documentales actuales, no probabilidades FMEA. El riesgo asociado describe un evento futuro distinto del vacío ya identificado.

| ID | Estado y condición de cierre | Responsable / límite | Riesgos asociados |
| --- | --- | --- | --- |
| E8-01 | T-15 estima por clases de tamaño fundadas en los requerimientos del T-12 y las cantidades del T-11 (SD7, sección 7.2.2), con tríada de ±25 %; la productividad de 128 HH efectivas por persona y mes aún no se contrasta con el avance real; peak 69 en el mes 15, 48 personas simultáneas de desarrollo entre julio y septiembre de 2027, brechas de dotación en SEG e IMP (T-15 §5.7) y capacidad por subventana sin asignación. Refinar la estimación con el equipo y comprobar personas, competencias, relevos y cero sobreasignación | JP/DES/CAL; antes línea base | R8-11/14 |
| E8-02 | Cronograma de 564 actividades calculado con dependencias, revisión Art. 18.3 y nivelación (T-15 §5–§6); sus plantillas, equipos y compras del CLIENTE no están validados. Reestimar con el equipo, confirmar plazos de compra y repetir el cálculo | JP/ARQ/SRE; antes línea base/H3 | R8-10/11/19 |
| E8-03 | V-12 no confirma fecha/calendario hábil. Febrero 2027 es ejemplo; comprobar E2 antes enero 2029, congelamientos y 28 días | JP/CLIENTE; mes 1 antes H1 | R8-15/17/18 |
| E8-04 | Objetivo 40 minutos/96 camiones sin ensayo. Demostrar versión operativa, DTE válidos y flujo sin interrupción; papel no acredita despacho | ARQ/SRE/Operaciones; antes H6/H11 | R8-01 |
| E8-05 | SD4 cumple RPO ≤15 min con tres caminos independientes y declara como riesgo residual la falla simultánea de los tres seguida de la destrucción del sitio (4.3.2.4; RT-02.11). Verificar las alarmas de replicación de 5 y 15 min y medir RPO/RTO en conmutación real | ARQ/SRE; antes H5/H10 | R8-05 |
| E8-06 | La coordinación de reserva de INT-03/04 está dimensionada en el SD4 (Anexo 4-I y sección 4-W.5) con cuatro mensajes por línea de pedido. Medir la proporción de líneas repartidas entre lotes o sitios, la carga y el drenaje de la cola, incluido el enlace de respaldo de Talca | ARQ/SRE; antes H5/H10 | R8-02/06 |
| E8-07 | T-15 ya imputa las posiciones de mesa del SD4 y el SOC 24×7, pero el Erlang C no verifica abandono ni resolución al primer contacto, y el límite es 2.283 contactos/mes. Medir por contacto desde la marcha blanca y calibrar Erlang A (T-15 §5.6). BTT RT-21.06 y Caso RT-21.06 tienen contenido distinto | SRE; antes del H7 (mes 16) y del H12 (mes 21) | R8-22 |
| E8-08 | La suspensión del proveedor de lácteos, de marzo a septiembre de 2026, es antecedente anterior; V-13 sin restitución documentada. Confirmar condiciones/evidencia con CLIENTE/proveedor sin atribuir solución retroactiva | JP/DAT/Calidad CLIENTE; mes 1 y antes aceptación trazabilidad | R8-16/23 |
| E8-09 | AL-STOCK-01/AL-ACT-01, carga, offline y conmutación descritos, no ejecutados. Aportar resultados reproducibles y resolver defectos críticos/altos | CAL/líderes; H5/H10/cierre aplicable | R8-02–07/16/18 |
| E8-10 | Antecedentes, certificaciones y dotación del SD1 son declarados; su acreditación documental se entrega en el Sobre N.° 1 (SD1, sección 1.4). No usar las declaraciones como disponibilidad demostrada antes de asignar personas | JP; antes presentación correspondiente | R8-11 |
| E8-11 | La red agregada incorpora medio mes de revisión del CLIENTE antes de cada hito y presentación por incrementos (T-15 §5.1 y §5.5), y la subsanación de diez días hábiles consume la reserva del hito (SD7, sección 7.3.1; T-15 §5.5 y Tabla 5.2). Las reservas de H2 a H10 (13 a 35 días hábiles) la absorben; la del H1 (6 días hábiles) no, por lo que una observación al H1 atrasa su acta. Acordar con la Contraparte Técnica el calendario de presentaciones | JP/CAL/CLIENTE; antes aprobar línea base | R8-12/17/18 |
| E8-12 | La calibración de probabilidades e impactos de la sección 8.1.3 y la simulación usan juicio del equipo, no frecuencias medidas. Contrastar con los datos de avance y de incidentes desde el mes 3 y recalcular el valor esperado y la simulación en cada Comité de Proyecto | JP/CAL; trimestral desde el mes 3 | Todos |

La regla de precio es única en la oferta: el SD2 (Anexo 2.2, S-09), el SD3 (Anexo 3.G, RNG-08) y el Formulario T-12 (RF-03.11 y RF-03.12) conservan el precio acordado al capturar el pedido. Su transmisión al ERP sin alteración se verifica en las pruebas de integración.

Infraestructura 99,95 %, transacción crítica 99,9 % y cero interrupción de despacho son obligaciones distintas. RTO ≤4 h/RPO ≤15 min no rebajan la ventana crítica.

## Anexo 8.F — Adopción de innovaciones y oportunidad

La tabla siguiente vincula cada innovación con su riesgo de adopción, su evaluación y su respuesta.

| Innovación SD7 vigente | Riesgo de adopción | P / I | Mitigación y contingencia |
| --- | --- | --- | --- |
| INN-01 Seguimiento de vencimiento posentrega en el local | R8-25 | 4 / 3 | Piloto asistido, I-01A y confirmación en la visita; aviso solo por vida útil y trazabilidad base si no rinde |
| INN-02 Reproducción de incidentes de terreno | R8-26; seguridad R8-24 | 3 / 4 | Casos protegidos de corte/reintento; mantener diagnóstico/regresión base |
| INN-03 Vida útil remanente por historia térmica del lote | R8-27 | 4 / 5 | Validación Calidad/revisión semestral; retirar recomendación y mantener vencimiento/control sanitario |
| INN-04 Tramo variable de la Operación ligado al costo de servir | R8-28 | 3 / 4 | Línea base y tres liquidaciones sombra; resolución contractual sin tarifas técnicas |
| INN-05 Hoja de negocio del almacenero | R8-29 | 4 / 3 | Co-diseño/piloto asistido sin exigir conexión; conservar preventista y efectivo |

La oportunidad se evalúa con una escala de beneficio simétrica a la de impacto del SD8, sección 8.1.3, en el horizonte de los meses 11 a 56:

| Valor | Beneficio ordinal |
| --- | --- |
| 1 | Mejora local sin efecto medible en retrabajo ni servicio |
| 2 | Reduce retrabajo que ya cabe en la capacidad asignada |
| 3 | Reduce retrabajo que consumiría contingencia o acorta la resolución de un servicio auxiliar |
| 4 | Protege un hito, un SLA o un alcance obligatorio |
| 5 | Evita detener el despacho crítico o comprometer seguridad, datos o sanidad |

O8-01 — Oportunidad de diagnóstico: si los casos protegidos INN-02 representan incidentes reales, podrían permitir resolver fallas equivalentes con menos retrabajo. P ordinal 3, porque los casos protegidos cubren sólo los incidentes de corte y reintento; beneficio ordinal 3, porque un caso reproducible reduce el retrabajo de diagnóstico que hoy consumiría contingencia; puntuación de oportunidad 9, separada de exposición de amenazas. Estrategia: mejorar, porque la reutilización de los casos protegidos aumenta su probabilidad de ocurrir (PMI, 2017, p. 444). La evidencia de comparación son las HH de diagnóstico de incidentes equivalentes antes y después de usar los casos. CAL compara HH antes/después de casos equivalentes durante validación meses 11–15 y operación. Disparador: incidente equivalente con reproducción disponible. Acción: reutilizar casos dentro de 3.10.2/8.3.1. Si no se verifica ahorro, mantener diagnóstico base sin descontar HH del T-15. No se suma esta oportunidad como reserva.

## Referencias

Las fuentes citadas en este documento se listan a continuación en formato APA 7.ª edición.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026*, artículos 17, 18 y 50.2, y Formularios T-16 y T-22.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*, RT-07.04, RT-07.07, RT-19.04, RT-21.06, RT-21.07 y RT-26.04.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística*, capítulos 10 a 14 y requisitos específicos citados.
- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N.º TFEP-01/2026*, secciones 2, 4, 6, 7 y 11 (Capítulo 8).
- LafroX. (2026). Subdocumentos 1 a 4, 6 y 7, con los anexos y formularios citados.
- International Electrotechnical Commission. (2018). *IEC 60812:2018 Failure modes and effects analysis (FMEA and FMECA)*. IEC.
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. ISO.
- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.), capítulo 11. Project Management Institute.

## Declaración de uso de IA

En cumplimiento de la sección 7.2 de las Aclaraciones de la licitación, la tabla siguiente declara el uso de herramientas de inteligencia artificial en estos anexos, con la revisión humana de cada parte. La declaración se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Anexos 8.A y 8.B | Codex; Claude Code | Fichas y FMEA; justificación individual de P y D con horizonte | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexos 8.B y 8.C: cuantificación y simulación | Claude Code | Valor esperado en HH, simulación de Monte Carlo y sensibilidad sobre el cronograma por actividad | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexos 8.C y 8.D | Codex; Claude Code | Escenarios deterministas; reserva de contingencia por valor esperado | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexos 8.E y 8.F | Codex; Claude Code | Condiciones de evidencia; escala de beneficio de la oportunidad | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexos 8.A–8.E: correcciones de coherencia | Claude Code | Fuentes de las fichas, notas de redondeo y de muestreo, contingencia adicional elegible, condiciones E8 (base de estimación, RPO residual, plazos H7/H12, subsanación y suspensión láctea), fichas R8-05, R8-11 y R8-22, y referencias | Medio | Ninguno | [[REVISIÓN HUMANA]] |
| Anexos 8.A–8.D: alineación con el PMBOK | Claude Code | Estrategia, efecto esperado, residual y riesgo secundario en cada ficha; Tabla C.5 con ahorro esperado y retorno; reglas de reserva | Medio | Ninguno | [[REVISIÓN HUMANA]] |
| Anexos 8.A–8.D: revisión de la Comisión | Claude Code | Glosario de códigos, costo-beneficio por riesgo (Tabla C.5), riesgos del Caso 19 en R8-03 y R8-18, coordinación de reserva según el SD4, redacción de las fichas y citas | Medio | Ninguno | [[REVISIÓN HUMANA]] |
