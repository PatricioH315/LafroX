# Subdocumento 8: Anexos

**Fuente:** `LafroX-Subdocumento-8-Anexos.tex`. Conversión completa de los contenidos de los Anexos 8.A y 8.B del documento fuente.

## Anexo 8.A: Fichas cualitativas y respuestas de riesgo

Las fichas documentan la valoración cualitativa registrada en T-16 y los detalles de respuesta disponibles en el registro vigente. Fuente: elaboración propia a partir del registro vigente; identificación y valoración según T-16, con referencia a Anexo 8.B para cuantificación. Los objetivos residuales son hipótesis condicionadas, no validadas, no acreditan eficacia y no reducen la contingencia adoptada de 2.058,480 HH. Los costos no están aprobados. La etapa indica fase, no plazo.


#### R-001
- **Categoría:** Integración y legado
- **Causa–evento–efecto:** Dado que el ERP no cuenta con documentación de interfaces ni permiso para modificarlo, puede que la interfaz disponible no soporte los contratos necesarios, teniendo como consecuencia retrabajo de la ACL y atraso de integración.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Bastián Trejo.
- **Disparador:** Al cierre del mes 2 no existe intercambio completo en ambiente de prueba.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Probar lectura, escritura autorizada y emisión con el proveedor; cerrar contrato de interfaz. Validar: Contrato firmado, extracción real, rechazo y reintento probados; no basta OpenAPI interno.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Contrato firmado, extracción real, rechazo y reintento probados; no basta OpenAPI interno.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-002
- **Categoría:** Integración y legado
- **Causa–evento–efecto:** Dado que el cliente desconoce condiciones contractuales de acceso a los datos, puede que el tercero limite API, cuotas o historia, teniendo como consecuencia ingesta incompleta de la flota propia.
- **Valoración:** P 3 (0,50); I 1 (0,20); $q_P\times q_I=0,10$; zona Media.
- **Respuesta:** Mitigar; responsable: Bastián Trejo.
- **Disparador:** No hay autorización y muestra válida al final del mes 2.
- **Etapa (no es plazo):** Propuesta.
- **Acción/mitigación y evidencia esperada:** Acordar licencia de datos, cuotas y prueba de extracción; exigir procedimiento de cambio. Validar: Autorización escrita y prueba de posición/historia con límites contratados.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Autorización escrita y prueba de posición/historia con límites contratados.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-003
- **Categoría:** Integración y legado
- **Causa–evento–efecto:** Dado que el WMS de 2013 y los registros físicos conviven durante la transición, puede que el corte deje saldos divergentes o tareas sin dueño, teniendo como consecuencia reversión y extensión de la convivencia.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Leandro Chamorro.
- **Disparador:** Una diferencia de saldo o tarea queda sin explicación al ensayo.
- **Etapa (no es plazo):** Implantación.
- **Acción/mitigación y evidencia esperada:** Ejecutar un ensayo adicional de delta y reversión con pendientes de recepción, picking y retornos. Validar: Conciliación aprobada por bodega y Finanzas; rollback restaura estado sin doble operación.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Conciliación aprobada por bodega y Finanzas; rollback restaura estado sin doble operación.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.



#### R-004
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que los lotes están en texto libre y los registros históricos están incompletos, puede que el saneamiento exceda lo previsto o cargue datos inconsistentes, teniendo como consecuencia rechazo de migración y pérdida de trazabilidad.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Leandro Chamorro.
- **Disparador:** Campos críticos sin correspondencia o lote ausente en la muestra.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Muestrear datos completos por origen y antigüedad, medir defectos y obtener responsables de corrección. Validar: Perfilado reproducible; rechazos aislados; no fabricar lotes faltantes; conciliación por conjunto.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 25 %, condicionado y no validado; condición: Perfilado reproducible; rechazos aislados; no fabricar lotes faltantes; conciliación por conjunto.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-005
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que los sitios y móviles acumulan operaciones desconectadas, puede que reintentos y orden parcial dupliquen cobros o reserven stock ya retenido, teniendo como consecuencia inconsistencia entre sitio, nube y ERP.
- **Valoración:** P 2 (0,30); I 4 (0,80); $q_P\times q_I=0,24$; zona Alta.
- **Respuesta:** Mitigar; responsable: Tomás Pérez.
- **Disparador:** Reintento genera más de un resultado económico o saldo negativo.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Inyectar fallas después de persistir y antes del acuse, con dos sitios y un móvil. Validar: Prueba con UUID repetido, orden invertido y corte de 24 h; invariantes conciliados.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Prueba con UUID repetido, orden invertido y corte de 24 h; invariantes conciliados.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.



#### R-006
- **Categoría:** Operación del cliente
- **Causa–evento–efecto:** Dado que Concepción tiene un solo enlace en la situación actual, puede que la redundancia propuesta no conmute o comparta una falla física, teniendo como consecuencia aislamiento del CD y acumulación de operaciones.
- **Valoración:** P 2 (0,30); I 4 (0,80); $q_P\times q_I=0,24$; zona Alta.
- **Respuesta:** Mitigar; responsable: Guillermo Castillo.
- **Disparador:** Proveedor no demuestra diversidad o BGP no conmuta en prueba.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Inspeccionar rutas físicas y simular caída de fibra y LTE con el satélite activo. Validar: Acta de diversidad y prueba de 24 h con recepción, preparación y despacho reales.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Acta de diversidad y prueba de 24 h con recepción, preparación y despacho reales.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-007
- **Categoría:** Operación del cliente
- **Causa–evento–efecto:** Dado que Los Ángeles presenta señal móvil intermitente en su ventana operacional, puede que el borde o su cola no sostenga la carga de una madrugada sin WAN, teniendo como consecuencia transferencias demoradas y stock desactualizado.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Guillermo Castillo.
- **Disparador:** Una transferencia depende de una llamada central durante el corte.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Medir cobertura nocturna y ensayar las transferencias con corte y reposición de enlace. Validar: Acta nocturna por plataforma, cola durable y conciliación dentro de 2 h.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Acta nocturna por plataforma, cola durable y conciliación dentro de 2 h.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-008
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que existen rutas sin cobertura hasta el regreso y trabajo bajo lluvia y calor, puede que la aplicación o batería no conserve una jornada completa, teniendo como consecuencia pedido, entrega o cobro perdido y repetición de visitas.
- **Valoración:** P 2 (0,30); I 2 (0,40); $q_P\times q_I=0,12$; zona Media.
- **Respuesta:** Mitigar; responsable: Tomás Pérez.
- **Disparador:** Cierre inesperado, dato perdido o batería agotada antes de terminar el turno.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Ensayar 14 h en ruta con periféricos y batería envejecida, más reconexión en 10 min. Validar: Jornada íntegra reproducible y sin duplicados, bajo condiciones de terreno.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Jornada íntegra reproducible y sin duplicados, bajo condiciones de terreno.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-009
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que la operación nocturna requiere relevos mientras la identidad central está inaccesible, puede que el manifiesto venza o admita permisos revocados, teniendo como consecuencia bloqueo de una función válida o acceso indebido.
- **Valoración:** P 2 (0,30); I 2 (0,40); $q_P\times q_I=0,12$; zona Media.
- **Respuesta:** Mitigar; responsable: Álvaro Catalán.
- **Disparador:** Turno válido denegado o manifiesto vencido aceptado.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Probar dos relevos durante un corte, vencimiento y revocación con el verificador local. Validar: Acta de corte con cambios de turno, denegación y bitácora posterior.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Acta de corte con cambios de turno, denegación y bitácora posterior.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-010
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que la cámara de congelado está a −22 °C y sin señal, puede que la batería, pantalla, lector o impresora falle en uso real, teniendo como consecuencia picking lento o registros incompletos.
- **Valoración:** P 2 (0,30); I 2 (0,40); $q_P\times q_I=0,12$; zona Media.
- **Respuesta:** Mitigar; responsable: Bastián Trejo.
- **Disparador:** Modelo o accesorio no tiene rango acreditado o falla en ensayo.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Validar una unidad por tipo en cámara, con guantes, condensación y ciclo entrada/salida. Validar: Ficha exacta y prueba funcional completa antes de compra masiva.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Ficha exacta y prueba funcional completa antes de compra masiva.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-011
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que la regla de excursión no estaba formalizada por producto en el levantamiento, puede que la calibración o parametrización libere un lote no conforme o retenga uno válido, teniendo como consecuencia bloqueo operacional o disposición sanitaria errónea.
- **Valoración:** P 2 (0,30); I 4 (0,80); $q_P\times q_I=0,24$; zona Alta.
- **Respuesta:** Mitigar; responsable: Maximiliano Miño.
- **Disparador:** Ficha sin aprobación, deriva de calibración o alarmas contradictorias.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Validar rangos por familia y contrastar sensor patrón con alarma, desconexión y lectura tardía. Validar: Calidad aprueba reglas; sensor patrón y ensayo de bloqueo; ninguna liberación automática.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Calidad aprueba reglas; sensor patrón y ensayo de bloqueo; ninguna liberación automática.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-012
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que el caso reporta recepciones sin lote y retiro de nueve días, puede que la cadena de custodia nueva quede incompleta en algún sitio o retorno, teniendo como consecuencia identificación tardía de clientes y lote afectado.
- **Valoración:** P 3 (0,50); I 4 (0,80); $q_P\times q_I=0,40$; zona Crítica.
- **Respuesta:** Mitigar; responsable: Maximiliano Miño.
- **Disparador:** Consulta no identifica todos los destinos o supera dos horas.
- **Etapa (no es plazo):** Implantación.
- **Acción/mitigación y evidencia esperada:** Ejecutar retiro simulado extremo a extremo con lote repartido, devolución y sitio desconectado. Validar: Listado reconciliado contra entregas y devoluciones en menos de 2 h; historia incompleta declarada.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Listado reconciliado contra entregas y devoluciones en menos de 2 h; historia incompleta declarada.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-013
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que salen 96 camiones de 05:30 a 07:00 y septiembre casi duplica el volumen, puede que la carga o un componente común degrade el despacho, teniendo como consecuencia día de operación afectado y SLA incumplido.
- **Valoración:** P 2 (0,30); I 4 (0,80); $q_P\times q_I=0,24$; zona Alta.
- **Respuesta:** Mitigar; responsable: Guillermo Castillo.
- **Disparador:** Picking supera 1 s o la cola no drena antes del despacho.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Probar carga con un nodo fuera, backlog y periféricos reales en ventana de despacho. Validar: Prueba a peak de caso y margen declarado; 96 despachos completos con falla inyectada.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Prueba a peak de caso y margen declarado; 96 despachos completos con falla inyectada.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-014
- **Categoría:** Operación del cliente
- **Causa–evento–efecto:** Dado que la sala actual tiene split, UPS de diez minutos y acceso por llave, puede que la habilitación o redundancia eléctrica falle ante un corte prolongado, teniendo como consecuencia caída de los nodos locales críticos.
- **Valoración:** P 2 (0,30); I 4 (0,80); $q_P\times q_I=0,24$; zona Alta.
- **Respuesta:** Mitigar; responsable: Guillermo Castillo.
- **Disparador:** Autonomía o temperatura fuera del diseño en aceptación.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Recepcionar energía, autonomía y climatización con carga, corte y alarma. Validar: Ensayo de energía y carga térmica, PDU/circuitos comprobados y acta de recepción.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Ensayo de energía y carga térmica, PDU/circuitos comprobados y acta de recepción.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-015
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que la operación híbrida produce datos en varios sitios y medios, puede que la restauración o promoción pierda datos o supere los límites, teniendo como consecuencia interrupción prolongada y conciliación extraordinaria.
- **Valoración:** P 3 (0,50); I 4 (0,80); $q_P\times q_I=0,40$; zona Crítica.
- **Respuesta:** Mitigar; responsable: Guillermo Castillo.
- **Disparador:** RPO supera 15 min, RTO supera 4 h o dos escritores aceptan operaciones.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Ensayar desastre total con escritura en curso, exclusión del escritor y retorno. Validar: Informe medido de conmutación y retorno; incluir pérdida simultánea de WAN y nodo.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Informe medido de conmutación y retorno; incluir pérdida simultánea de WAN y nodo.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-016
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que hay portales externos, flota móvil y datos comerciales sensibles, puede que una vulnerabilidad o cuenta privilegiada comprometa servicio o evidencia, teniendo como consecuencia indisponibilidad, fuga y recuperación forense.
- **Valoración:** P 2 (0,30); I 4 (0,80); $q_P\times q_I=0,24$; zona Alta.
- **Respuesta:** Mitigar; responsable: Álvaro Catalán.
- **Disparador:** Hallazgo explotable, acceso anómalo o registro de auditoría alterado.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Revisar superficie y privilegios; probar restauración aislada y respuesta a credencial comprometida. Validar: Pentest sin hallazgos bloqueantes y ejercicio de contención/recuperación.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Pentest sin hallazgos bloqueantes y ejercicio de contención/recuperación.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-017
- **Categoría:** Personas y adopción
- **Causa–evento–efecto:** Dado que el sindicato objetó cámaras en cabina y control de jornada por GPS, puede que el uso de ubicación sea rechazado aunque no se instalen cámaras, teniendo como consecuencia adopción suspendida y rediseño de finalidades.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Patricio Henríquez.
- **Disparador:** No existe acuerdo antes del piloto o se detecta finalidad distinta.
- **Etapa (no es plazo):** Propuesta.
- **Acción/mitigación y evidencia esperada:** Acordar finalidades, retención y acceso con sindicato y dirección; demostrar uso sin control de jornada. Validar: Acta de participación, revisión de privacidad y prueba de permisos/retención.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Acta de participación, revisión de privacidad y prueba de permisos/retención.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-018
- **Categoría:** Personas y adopción
- **Causa–evento–efecto:** Dado que 54 camiones pertenecen a diez empresas y sus conductores cambian sin aviso, puede que el acuerdo o enrolamiento no cubra reemplazos, teniendo como consecuencia entregas sin evidencia y trabajo paralelo en papel.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Patricio Henríquez.
- **Disparador:** Conductor de reemplazo llega sin autorización o capacitación.
- **Etapa (no es plazo):** Implantación.
- **Acción/mitigación y evidencia esperada:** Probar alta, baja y conductor suplente por cada empresa; pactar obligación de informar reemplazos. Validar: Diez acuerdos y prueba de enrolamiento/soporte que no detenga reparto.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 25 %, condicionado y no validado; condición: Diez acuerdos y prueba de enrolamiento/soporte que no detenga reparto.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-019
- **Categoría:** Personas y adopción
- **Causa–evento–efecto:** Dado que la rotación anual es del 38 % y el turno nocturno es crítico, puede que el personal nuevo no alcance autonomía de preparación, teniendo como consecuencia baja productividad y errores de picking.
- **Valoración:** P 3 (0,50); I 1 (0,20); $q_P\times q_I=0,10$; zona Media.
- **Respuesta:** Mitigar; responsable: Patricio Henríquez.
- **Disparador:** Errores superan el criterio aprobado o novato requiere apoyo continuo.
- **Etapa (no es plazo):** Implantación.
- **Acción/mitigación y evidencia esperada:** Validar incorporación de personal nuevo con tareas reales y guías breves de turno. Validar: Medir tiempo, pasos y errores según 3.A.4a con novatos en turno nocturno.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 25 %, condicionado y no validado; condición: Medir tiempo, pasos y errores según 3.A.4a con novatos en turno nocturno.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-020
- **Categoría:** Personas y adopción
- **Causa–evento–efecto:** Dado que preventistas y conductores están en ruta de lunes a sábado, puede que la convocatoria no libere tiempo sin afectar operación, teniendo como consecuencia usuarios no certificados al paso a producción.
- **Valoración:** P 3 (0,50); I 1 (0,20); $q_P\times q_I=0,10$; zona Media.
- **Respuesta:** Mitigar; responsable: Patricio Henríquez.
- **Disparador:** Cobertura de certificación incompleta dos semanas antes de cierre.
- **Etapa (no es plazo):** Implantación.
- **Acción/mitigación y evidencia esperada:** Acordar microturnos de entrenamiento y recuperar ausencias por ruta y perfil. Validar: Agenda aprobada, asistencia y prueba práctica individual por perfil.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Agenda aprobada, asistencia y prueba práctica individual por perfil.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-021
- **Categoría:** Personas y adopción
- **Causa–evento–efecto:** Dado que las reglas residen en Hugo Maldonado, que se jubila en dos años, puede que se retire antes de transferir y validar todas las excepciones, teniendo como consecuencia rutas inseguras o promesas incumplidas.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Patricio Henríquez.
- **Disparador:** Zona sin reglas y suplente sin ejecutar una planificación independiente.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Capturar y validar reglas por zona con Hugo y un suplente, usando rutas y restricciones reales. Validar: Repositorio aprobado y suplente planifica rutas sin ayuda, sin violar peso/puentes/ventanas.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Repositorio aprobado y suplente planifica rutas sin ayuda, sin violar peso/puentes/ventanas.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-022
- **Categoría:** Operación del cliente
- **Causa–evento–efecto:** Dado que TI del cliente tiene cuatro personas y la operación no puede detenerse, puede que las validaciones o decisiones no lleguen a la fecha requerida, teniendo como consecuencia cadenas de aprobación retrasadas.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Alex Aravena.
- **Disparador:** Validación pendiente cinco días hábiles o sin suplente.
- **Etapa (no es plazo):** Propuesta.
- **Acción/mitigación y evidencia esperada:** Pactar titulares y suplentes, agenda y SLA de decisiones por hito. Validar: Agenda y acuerdos escritos; ninguna aprobación tácita de aceptación contractual.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 25 %, condicionado y no validado; condición: Agenda y acuerdos escritos; ninguna aprobación tácita de aceptación contractual.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-023
- **Categoría:** Operación del cliente
- **Causa–evento–efecto:** Dado que septiembre, diciembre y cierres mensuales restringen cambios, puede que una demora desplace un corte o parche a una ventana prohibida, teniendo como consecuencia reprogramación y multa por atraso.
- **Valoración:** P 2 (0,30); I 2 (0,40); $q_P\times q_I=0,12$; zona Media.
- **Respuesta:** Mitigar; responsable: Alex Aravena.
- **Disparador:** Fecha propuesta cae en congelamiento o cierre mensual.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Revalidar calendario por fecha efectiva y reservar alternativa permitida para cada corte. Validar: Calendario validado por contraparte y plan alternativo; emergencia requiere definición contractual.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Calendario validado por contraparte y plan alternativo; emergencia requiere definición contractual.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-024
- **Categoría:** Operación del cliente
- **Causa–evento–efecto:** Dado que el cliente compra dispositivos de terreno y LafroX habilita la infraestructura, puede que una compra, entrega o recepción exceda la ventana de la ola, teniendo como consecuencia piloto sin equipos completos o marcha blanca insuficiente.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Bastián Trejo.
- **Disparador:** Orden sin fecha comprometida o muestra no aceptada un mes antes de ola.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Confirmar orden, stock y plazo por ola; homologar alternativa antes de la compra. Validar: Orden y acta de muestra; préstamo o alternativa homologada no reduce población de prueba.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Orden y acta de muestra; préstamo o alternativa homologada no reduce población de prueba.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-025
- **Categoría:** Empresa proveedora
- **Causa–evento–efecto:** Dado que construcción E2 coincide con marcha blanca E1 y hay líderes con varios roles, puede que la dotación real no sostenga los frentes simultáneos, teniendo como consecuencia atraso de E2 o deterioro de E1.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Alex Aravena.
- **Disparador:** Capacidad disponible por rol menor que carga dos semanas seguidas.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Nominar equipos separados y suplentes; verificar capacidad semanal y contrato de refuerzo. Validar: Cartas y calendario nominal; no sumar las HH de mitigación a capacidad inexistente.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Cartas y calendario nominal; no sumar las HH de mitigación a capacidad inexistente.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-026
- **Categoría:** Contrato y licitación
- **Causa–evento–efecto:** Dado que hay seis condiciones copulativas de cierre y revisión contractual, puede que observaciones, capacitación o indicadores sigan abiertos al cierre, teniendo como consecuencia extensión a cargo de LafroX sin mover fases.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Maximiliano Miño.
- **Disparador:** Incidente alto abierto, diferencia sin explicar o acta pendiente.
- **Etapa (no es plazo):** Implantación.
- **Acción/mitigación y evidencia esperada:** Revisar evidencia con contraparte antes del hito y ejecutar ensayo de go/no-go. Validar: Checklist de seis condiciones con evidencia; ninguna firma ni prueba se presume.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 25 %, condicionado y no validado; condición: Checklist de seis condiciones con evidencia; ninguna firma ni prueba se presume.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-027
- **Categoría:** Contrato y licitación
- **Causa–evento–efecto:** Dado que el caso contiene decisiones de diseño y sistemas excluidos con dependencias, puede que una solicitud introduzca trabajo no previsto o duplique sistemas de registro, teniendo como consecuencia sobrecosto y retraso.
- **Valoración:** P 3 (0,50); I 1 (0,20); $q_P\times q_I=0,10$; zona Media.
- **Respuesta:** Mitigar; responsable: Alex Aravena.
- **Disparador:** Nueva función sin requisito o decisión aprobada.
- **Etapa (no es plazo):** Propuesta.
- **Acción/mitigación y evidencia esperada:** Trazar solicitudes a requisitos, impacto y aprobación antes de construcción. Validar: Registro de cambios, estimación y aprobación; exclusiones no eliminan integración obligatoria.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Registro de cambios, estimación y aprobación; exclusiones no eliminan integración obligatoria.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-028
- **Categoría:** Operación del cliente
- **Causa–evento–efecto:** Dado que 38 % del canal tradicional paga en efectivo y hay diferencias mensuales, puede que el circuito de custodia no explique toda diferencia al retorno, teniendo como consecuencia reproceso financiero y exposición del conductor.
- **Valoración:** P 2 (0,30); I 2 (0,40); $q_P\times q_I=0,12$; zona Media.
- **Respuesta:** Mitigar; responsable: Leandro Chamorro.
- **Disparador:** Diferencia al cierre sin evidencia ni responsable.
- **Etapa (no es plazo):** Implantación.
- **Acción/mitigación y evidencia esperada:** Simular caja de turno, faltante, devolución y pago parcial; acordar custodia física con Finanzas. Validar: Cuadre por camión y turno el mismo día; importe externo no se incorpora como costo del proyecto.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 15 %, condicionado y no validado; condición: Cuadre por camión y turno el mismo día; importe externo no se incorpora como costo del proyecto.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-029
- **Categoría:** Regulatorio y externo
- **Causa–evento–efecto:** Dado que el ERP es único emisor y el receptor suele carecer de firma avanzada, puede que la prueba de entrega no se vincule o verifique conforme al acto, teniendo como consecuencia rechazo de evidencia y disputa de entrega.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Bastián Trejo.
- **Disparador:** Guía, identidad o certificado no coincide con el expediente.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Validar flujo por acto con experto tributario y probar certificado vencido, POD offline y acuse. Validar: Dictamen sobre el flujo y AL-DTE-01 aprobado; no equiparar firma simple y avanzada.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Dictamen sobre el flujo y AL-DTE-01 aprobado; no equiparar firma simple y avanzada.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-030
- **Categoría:** Integración y legado
- **Causa–evento–efecto:** Dado que la cadena exige pedido electrónico, ASN, ventana y POD antes de enero de 2029, puede que su formato, ambiente o certificación no estén disponibles a tiempo, teniendo como consecuencia integración no habilitada y pérdida de capacidad comercial.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Bastián Trejo.
- **Disparador:** No hay ventana de certificación acordada al mes 4.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Obtener especificación, sandbox, fechas y responsable de certificación; ensayar el flujo completo. Validar: Confirmación escrita de cadena y certificación completa antes del H12; dependencia externa mantiene zona alta.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 35 %, condicionado y no validado; condición: Confirmación escrita de cadena y certificación completa antes del H12; dependencia externa mantiene zona alta.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


#### R-031
- **Categoría:** Integración y legado
- **Causa–evento–efecto:** Dado que el canal tradicional no usa siempre correo y proveedores no acreditan toda apertura, puede que el aviso de llegada no se reciba antes de la salida, teniendo como consecuencia cliente ausente y entrega fallida.
- **Valoración:** P 3 (0,50); I 1 (0,20); $q_P\times q_I=0,10$; zona Media.
- **Respuesta:** Mitigar; responsable: Tomás Pérez.
- **Disparador:** Mensaje fallido o contacto inválido antes de partida.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Validar contactos y probar fallback por canal con confirmación de entrega; medir apertura por separado. Validar: Prueba de recepción antes de salida; SMS sin lectura informable no cuenta como abierto.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Prueba de recepción antes de salida; SMS sin lectura informable no cuenta como abierto.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-032
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que la solución usa servicios administrados y APIs con contratos propios, puede que la reversibilidad no preserve funcionalidad y evidencia en una salida, teniendo como consecuencia migración costosa y dependencia prolongada.
- **Valoración:** P 2 (0,30); I 2 (0,40); $q_P\times q_I=0,12$; zona Media.
- **Respuesta:** Mitigar; responsable: Bastián Trejo.
- **Disparador:** Componente sin alternativa o exportación sin semántica.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Ensayar exportación e importación de un flujo representativo y medir sustitución del servicio no portable. Validar: Ensayo reproducible, licencias y formatos declarados; costo de salida separado de EOL.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 15 %, condicionado y no validado; condición: Ensayo reproducible, licencias y formatos declarados; costo de salida separado de EOL.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-033
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que el contrato dura 56 meses y versiones/equipos tienen ciclos de soporte, puede que un componente quede sin parche o repuesto antes del cierre, teniendo como consecuencia actualización no prevista o vulnerabilidad persistente.
- **Valoración:** P 3 (0,50); I 1 (0,20); $q_P\times q_I=0,10$; zona Media.
- **Respuesta:** Mitigar; responsable: Bastián Trejo.
- **Disparador:** Soporte restante menor a doce meses y sin reemplazo homologado.
- **Etapa (no es plazo):** Operación.
- **Acción/mitigación y evidencia esperada:** Consolidar fechas EOL/EOS comprobadas y ensayar actualización o sustitución antes del fin de soporte. Validar: Ficha/versiones y calendario anual; presupuesto de reposición pendiente de tarifas.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Ficha/versiones y calendario anual; presupuesto de reposición pendiente de tarifas.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-034
- **Categoría:** Empresa proveedora
- **Causa–evento–efecto:** Dado que se requieren madrugada, peaks, seis sitios y traslados de hasta 340 km, puede que ausencia, demanda o traslado impidan atención dentro del SLA, teniendo como consecuencia interrupción más larga y abandono.
- **Valoración:** P 2 (0,30); I 2 (0,40); $q_P\times q_I=0,12$; zona Media.
- **Respuesta:** Mitigar; responsable: Guillermo Castillo.
- **Disparador:** Demanda supera capacidad del turno o especialista no puede llegar.
- **Etapa (no es plazo):** Operación.
- **Acción/mitigación y evidencia esperada:** Simular ausencia y peak de llamadas con traslado; pactar cobertura de suplentes por tecnología. Validar: Prueba de cola con 80 % antes de 20 s, abandono ≤5 % y guardia acreditada.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 15 %, condicionado y no validado; condición: Prueba de cola con 80 % antes de 20 s, abandono ≤5 % y guardia acreditada.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-035
- **Categoría:** Empresa proveedora
- **Causa–evento–efecto:** Dado que nube, mensajes, licencias y reposiciones tienen consumo y pago durante 56 meses, puede que el consumo o los pagos superen la previsión financiera, teniendo como consecuencia recorte de servicio o necesidad de financiamiento.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Alex Aravena.
- **Disparador:** No hay precio/volumen contractual o desvío sin cobertura de caja.
- **Etapa (no es plazo):** Propuesta.
- **Acción/mitigación y evidencia esperada:** Construir presupuesto por unidad, peak, divisa y calendario de cobro; probar alertas de consumo. Validar: Oferta económica y flujo de caja revisados; sin tarifas, severidad monetaria sigue pendiente.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 25 %, condicionado y no validado; condición: Oferta económica y flujo de caja revisados; sin tarifas, severidad monetaria sigue pendiente.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-036
- **Categoría:** Personas y adopción
- **Causa–evento–efecto:** Dado que el inventario de góndola no pertenece al sistema de registro de Puelche, puede que datos inferidos generen avisos de vencimiento sin confirmación, teniendo como consecuencia visitas improductivas y beneficio no demostrable.
- **Valoración:** P 3 (0,50); I 1 (0,20); $q_P\times q_I=0,10$; zona Media.
- **Respuesta:** Mitigar; responsable: Patricio Henríquez.
- **Disparador:** Avisos sin lote confirmado o rechazo reiterado del local.
- **Etapa (no es plazo):** Implantación.
- **Acción/mitigación y evidencia esperada:** Pilotear por locales voluntarios y separar saldo inferido de observado; validar avisos antes de acción. Validar: Muestra de avisos confirmados, intervención autorizada e indicador INN-01 medido.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Muestra de avisos confirmados, intervención autorizada e indicador INN-01 medido.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-037
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que los fallos aparecen en condiciones de terreno difíciles de replicar, puede que captura y reproducción no conserven el orden causal del incidente, teniendo como consecuencia corrección ineficaz y reapertura de tickets.
- **Valoración:** P 3 (0,50); I 1 (0,20); $q_P\times q_I=0,10$; zona Media.
- **Respuesta:** Mitigar; responsable: Tomás Pérez.
- **Disparador:** Ticket se cierra sin reproducción o reaparece por la misma causa.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Seleccionar incidentes de prueba y verificar reproducción con datos minimizados y versión exacta. Validar: Escenario reproduce fallo, corrección lo elimina y datos sensibles están protegidos.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Escenario reproduce fallo, corrección lo elimina y datos sensibles están protegidos.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-038
- **Categoría:** Solución y tecnología
- **Causa–evento–efecto:** Dado que el modelo cinético depende de familia de producto e historia térmica completa, puede que la estimación sea inválida o exceda el uso permitido, teniendo como consecuencia decisión de disposición errónea.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Maximiliano Miño.
- **Disparador:** Modelo sin parámetros aprobados o serie térmica incompleta.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Validar por familia contra evidencia del proveedor; mantener modo informativo hasta aceptación. Validar: Validación de Calidad/proveedor; innovación nunca libera ni amplía vencimiento automáticamente.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Validación de Calidad/proveedor; innovación nunca libera ni amplía vencimiento automáticamente.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-039
- **Categoría:** Contrato y licitación
- **Causa–evento–efecto:** Dado que la mejora puede deberse a combustible, malla o mezcla de clientes y no al servicio, puede que la línea base o canasta atribuya un ahorro espurio, teniendo como consecuencia disputa del tramo variable o sacrificio del OTIF.
- **Valoración:** P 3 (0,50); I 1 (0,20); $q_P\times q_I=0,10$; zona Media.
- **Respuesta:** Mitigar; responsable: Alex Aravena.
- **Disparador:** Una variación externa modifica el incentivo sin ajuste o OTIF bajo genera pago.
- **Etapa (no es plazo):** Propuesta.
- **Acción/mitigación y evidencia esperada:** Acordar canasta y fórmula; recalcular casos de estacionalidad y OTIF bajo sin pago variable. Validar: Contrato y cálculo auditables por Finanzas; tarifas y techo monetario pendientes.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Contrato y cálculo auditables por Finanzas; tarifas y techo monetario pendientes.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-040
- **Categoría:** Personas y adopción
- **Causa–evento–efecto:** Dado que hay baja alfabetización y agregados de negocios comparables, puede que la hoja no se entienda o permita identificar otro local, teniendo como consecuencia rechazo del servicio y divulgación comercial.
- **Valoración:** P 3 (0,50); I 1 (0,20); $q_P\times q_I=0,10$; zona Media.
- **Respuesta:** Mitigar; responsable: Patricio Henríquez.
- **Disparador:** Local no puede explicar la hoja o agregado permite reidentificar.
- **Etapa (no es plazo):** Implantación.
- **Acción/mitigación y evidencia esperada:** Probar comprensión con locales y revisión de divulgación; desactivar comparativos hasta autorización. Validar: Prueba de comprensión; revisión de privacidad y separación de copias pedidas/entregadas.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Prueba de comprensión; revisión de privacidad y separación de copias pedidas/entregadas.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-041
- **Categoría:** Contrato y licitación
- **Causa–evento–efecto:** Dado que el cliente tiene cuatro personas de TI y debe sostener o transferir el servicio, puede que documentación, cuentas o exportación no permitan una entrega efectiva, teniendo como consecuencia dependencia al cierre y operación no sostenible.
- **Valoración:** P 2 (0,30); I 2 (0,40); $q_P\times q_I=0,12$; zona Media.
- **Respuesta:** Mitigar; responsable: Guillermo Castillo.
- **Disparador:** Tarea esencial solo puede ejecutarla el equipo saliente.
- **Etapa (no es plazo):** Operación.
- **Acción/mitigación y evidencia esperada:** Ensayar una entrega parcial a operadores del cliente y corregir runbooks antes del cierre. Validar: Operador receptor ejecuta procedimiento con cuentas propias y exportación reconciliada.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 15 %, condicionado y no validado; condición: Operador receptor ejecuta procedimiento con cuentas propias y exportación reconciliada.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-042
- **Categoría:** Regulatorio y externo
- **Causa–evento–efecto:** Dado que el contrato conserva documentos, ubicación y evidencia durante varios años, puede que un cambio o interpretación exija adaptar controles y purga, teniendo como consecuencia retrabajo, conservación indebida o incumplimiento.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Álvaro Catalán.
- **Disparador:** Nueva exigencia afecta dato tratado o purga elimina evidencia vigente.
- **Etapa (no es plazo):** Operación.
- **Acción/mitigación y evidencia esperada:** Revisar normativa aplicable con asesor competente y ensayar purga con expediente retenido. Validar: Matriz legal actualizada y ensayo de supresión sin reconstrucción; no se certifica legalidad con esta planilla.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 20 %, condicionado y no validado; condición: Matriz legal actualizada y ensayo de supresión sin reconstrucción; no se certifica legalidad con esta planilla.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-043
- **Categoría:** Integración y legado
- **Causa–evento–efecto:** Dado que el POS depende de un tercero y el timeout no equivale a rechazo, puede que el reintento o pago alternativo duplique la obligación, teniendo como consecuencia conciliación, devolución y reclamo del cliente.
- **Valoración:** P 2 (0,30); I 2 (0,40); $q_P\times q_I=0,12$; zona Media.
- **Respuesta:** Mitigar; responsable: Leandro Chamorro.
- **Disparador:** Existe pago incierto y se intenta cobrar otra vez sin consulta.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Inyectar timeout después del cargo y probar consulta, cancelación y autorización de alternativa. Validar: Contrato POS y prueba de un solo cargo económico con correlación y devolución.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Contrato POS y prueba de un solo cargo económico con correlación y devolución.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-044
- **Categoría:** Operación del cliente
- **Causa–evento–efecto:** Dado que retornos en terreno y recepción local atraviesan varios registros, puede que una devolución se contabilice dos veces o quede sin vínculo al lote, teniendo como consecuencia saldo, cuenta de envases y trazabilidad incorrectos.
- **Valoración:** P 2 (0,30); I 1 (0,20); $q_P\times q_I=0,06$; zona Baja.
- **Respuesta:** Mitigar; responsable: Leandro Chamorro.
- **Disparador:** Dos movimientos para una recepción o saldo sin vínculo a entrega.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Probar retorno parcial, sitio offline y reintento con lote retenido y envase recuperado. Validar: Conciliación por cliente/tipo y lote; MERMA/DESTRUCCION no duplica costo.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 10 %, condicionado y no validado; condición: Conciliación por cliente/tipo y lote; MERMA/DESTRUCCION no duplica costo.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.

#### R-045
- **Categoría:** Integración y legado
- **Causa–evento–efecto:** Dado que direcciones, pesos y puentes no están plenamente formalizados, puede que geocodificación o propuesta asigne camión/ruta incompatible, teniendo como consecuencia entrega fallida y reproceso de planificación.
- **Valoración:** P 3 (0,50); I 2 (0,40); $q_P\times q_I=0,20$; zona Alta.
- **Respuesta:** Mitigar; responsable: Bastián Trejo.
- **Disparador:** Dirección no ubicable o restricción de peso/volumen violada.
- **Etapa (no es plazo):** Implementación.
- **Acción/mitigación y evidencia esperada:** Validar rutas por zona y atributos físicos; comparar proveedor GIS y ruta conocida con conductor. Validar: Catálogo de restricciones aprobado y planificación con corrección auditada, incluso sin señal.
- **Plazo/hito:** Pendiente de definición por responsable.
- **Residual:** objetivo 15 %, condicionado y no validado; condición: Catálogo de restricciones aprobado y planificación con corrección auditada, incluso sin señal.
- **Contingencia:** Pendiente de definición por responsable.
- **Riesgo secundario:** Pendiente de definición por responsable.
- **Costo:** Pendiente.


## Anexo 8.B: Valor esperado y contingencia adoptada

Esta matriz presenta, para los 45 riesgos vigentes, las estimaciones iniciales de probabilidad de ocurrencia, los impactos condicionales en horas-hombre (HH) y el valor esperado por riesgo. Son estimaciones de planificación, no frecuencias históricas demostradas; su validación corresponde a los responsables de cada riesgo. Por decisión adoptada, la suma de $p_0\times HH$ se utiliza como estimación de contingencia en esfuerzo de 2.058,480 HH; no es una simulación ni una asignación mensual o por perfil. La estimación inicial porcentual $p_0$ se usa para calcular el valor esperado, mientras que la exposición cualitativa de T-16 ($q_P\times q_I$) usa escalas separadas. El objetivo residual sigue condicionado y no está disponible para recalcular la contingencia hasta validar la eficacia de las respuestas.

| ID | $p_0$ inicial (%) | Objetivo residual* (%) | Impacto condicional (HH) | Valor esperado (HH) | Mes estimado |
|---|---:|---:|---:|---:|---:|
| R-001 | 45% | 20% | 152,0 | 68,400 | 2 |
| R-002 | 40% | 20% | 67,2 | 26,880 | 2 |
| R-003 | 40% | 20% | 201,6 | 80,640 | 11 |
| R-004 | 45% | 25% | 224,0 | 100,800 | 3 |
| R-005 | 30% | 10% | 128,0 | 38,400 | 8 |
| R-006 | 25% | 10% | 70,4 | 17,600 | 6 |
| R-007 | 40% | 20% | 80,0 | 32,000 | 9 |
| R-008 | 30% | 10% | 80,0 | 24,000 | 10 |
| R-009 | 25% | 10% | 67,2 | 16,800 | 8 |
| R-010 | 25% | 10% | 88,0 | 22,000 | 3 |
| R-011 | 30% | 10% | 96,0 | 28,800 | 8 |
| R-012 | 35% | 10% | 201,6 | 70,560 | 12 |
| R-013 | 30% | 10% | 105,6 | 31,680 | 11 |
| R-014 | 20% | 10% | 96,0 | 19,200 | 4 |
| R-015 | 35% | 10% | 201,6 | 70,560 | 11 |
| R-016 | 30% | 10% | 144,0 | 43,200 | 11 |
| R-017 | 40% | 20% | 126,4 | 50,560 | 3 |
| R-018 | 45% | 25% | 150,4 | 67,680 | 11 |
| R-019 | 45% | 25% | 148,8 | 66,960 | 12 |
| R-020 | 35% | 20% | 112,0 | 39,200 | 12 |
| R-021 | 45% | 20% | 152,0 | 68,400 | 3 |
| R-022 | 50% | 25% | 118,4 | 59,200 | 1 |
| R-023 | 30% | 10% | 88,0 | 26,400 | 4 |
| R-024 | 40% | 20% | 126,4 | 50,560 | 3 |
| R-025 | 35% | 20% | 177,6 | 62,160 | 4 |
| R-026 | 40% | 25% | 201,6 | 80,640 | 11 |
| R-027 | 35% | 20% | 80,0 | 28,000 | 1 |
| R-028 | 30% | 15% | 108,8 | 32,640 | 12 |
| R-029 | 35% | 20% | 126,4 | 44,240 | 8 |
| R-030 | 50% | 35% | 232,0 | 116,000 | 4 |
| R-031 | 35% | 20% | 80,0 | 28,000 | 8 |
| R-032 | 30% | 15% | 152,0 | 45,600 | 3 |
| R-033 | 40% | 20% | 126,4 | 50,560 | 6 |
| R-034 | 30% | 15% | 136,0 | 40,800 | 21 |
| R-035 | 40% | 25% | 88,0 | 35,200 | 1 |
| R-036 | 40% | 20% | 80,0 | 32,000 | 14 |
| R-037 | 35% | 20% | 80,0 | 28,000 | 10 |
| R-038 | 45% | 20% | 152,0 | 68,400 | 12 |
| R-039 | 35% | 20% | 67,2 | 23,520 | 4 |
| R-040 | 40% | 20% | 92,8 | 37,120 | 18 |
| R-041 | 30% | 15% | 176,0 | 52,800 | 53 |
| R-042 | 35% | 20% | 126,4 | 44,240 | 21 |
| R-043 | 30% | 10% | 88,0 | 26,400 | 8 |
| R-044 | 30% | 10% | 88,0 | 26,400 | 8 |
| R-045 | 35% | 15% | 100,8 | 35,280 | 8 |

*La probabilidad residual es un objetivo condicionado; no se incorpora al escenario inicial mientras no se acrediten sus condiciones de validación. Las probabilidades iniciales son estimaciones de planificación y deben validarse con los responsables.*

**Totales condicionales y esperados**

| Impacto condicional total (HH) | Valor esperado total/adoptado (HH) |
|---:|---:|
| 5.585,6 | 2.058,480 |

**Disponibilidad y condiciones pendientes para la cuantificación.** Fuente: elaboración propia.

| Parámetro | Información disponible | Estado | Qué falta |
|---|---|---|---|
| Probabilidad inicial | Estimación porcentual inicial por riesgo | Juicio de planificación; sin frecuencia histórica comprobada | Validar horizonte, fundamento y responsable de cada estimación |
| Impacto condicional en HH | Estimación puntual del esfuerzo si ocurre el riesgo | Punto estimado; sin distribución | Sustentar rangos o distribuciones y evitar doble conteo |
| Mes previsto | Mes de referencia para el evento | Estimación puntual; no es distribución temporal | Vincular con actividades e hitos y estimar variabilidad temporal |
| Probabilidad residual | Objetivo sujeto a respuesta y condición de validación | Condicionada; eficacia pendiente | Acreditar la condición antes de usarla en un escenario residual |
| Dependencias | Las relaciones entre riesgos no están cuantificadas | Pendiente | Analizar causas comunes y documentar dependencias |
| Cronograma | No hay duración incierta ni relación riesgo--actividad completa | Sin red simulable | Incorporar tareas, distribuciones de duración, precedencias y recursos |
| Impacto económico | Las consecuencias monetarias y costos de respuesta requieren validación | Incompleto | Valorar los costos antes de una simulación económica |

La suma de los valores esperados individuales, adoptada como contingencia de esfuerzo, es 2.058,480 HH. El registro no permite una asignación actual por período o perfil: no se dispone de crosswalk entre los códigos R8 de análisis previos y los 45 riesgos vigentes. Los objetivos residuales son condicionales y no modifican esta estimación hasta que se valide la eficacia de las respuestas. Este anexo no presenta resultados de simulación, percentiles ni probabilidades de cumplimiento del cronograma.
