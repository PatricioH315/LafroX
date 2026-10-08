# Supuestos que no quedan resueltos por las Bases

Revisión: 1 de octubre de 2026. Alcance: S-01 a S-41 del Anexo 3.C, contrastados con los cuatro documentos de `Bases`.

## Criterio

Un antecedente respalda un supuesto cuando justifica su necesidad, pero no necesariamente fija la solución elegida. Se distingue entre decisiones delegadas al PROPONENTE, datos que requieren levantamiento, estimaciones de ingeniería y obligaciones ya fijadas. «No resuelto por las Bases» no significa que deba dejarse pendiente: el caso exige tomar y fundamentar decisiones y dimensionar la oferta antes de su entrega, con validación posterior cuando corresponda.

## S-01 a S-16: decisiones explícitamente delegadas

El Caso 02, capítulo 16, indica que el CLIENTE no ha tomado esas decisiones y que resolverlas, registrarlas como supuestos y asumir sus efectos en arquitectura, alcance y costo es trabajo del PROPONENTE. El numeral 17.1 exige incluirlas en el registro. Algunas contienen además obligaciones ya resueltas, señaladas abajo.

| ID | Qué no resuelven las Bases | Parte que sí está fijada o respaldada |
|---|---|---|
| S-01 | Fórmula completa de OTIF y tratamiento de entregas parciales. | Se exige una medición única y una meta comprometida; caso 16.1, decisión 1; cap. 18, resultado 4. |
| S-02 | Elegir lote de proveedor como unidad sanitaria y SSCC como unidad logística. | Se exige conservar origen y destino del lote; decisión 2. |
| S-03 | Reagendar a la siguiente ventana y prohibir entrega a terceros. | El caso describe prácticas distintas sin regla; decisión 3. |
| S-04 | Umbral térmico, automatismo del bloqueo y autoridad de liberación. | Se exige registro continuo y control sanitario; decisión 4. |
| S-05 | Mecanismo de confirmación, identificación y cambio de conductor. | Hay diez transportistas, rotación sin aviso y necesidad de acuerdo; decisión 5; sección 13.3. |
| S-06 | Modelo de control, rendición por camión, causales y distribución del riesgo del efectivo. | No se puede imponer medio de pago electrónico al canal tradicional; el efectivo debe poder controlarse y rendirse el mismo día. Restricción 5; decisión 6; resultado 10. |
| S-07 | Método de costeo por actividad y tratamiento de clientes no rentables. | Se exige costo por cliente y entrega construido desde los hechos; decisión 7; resultado 11. |
| S-08 | Reserva central al confirmar y prioridad por llegada al servidor. | El conflicto de asignación de stock está expresamente abierto; decisión 8. |
| S-09 | Conservar el precio acordado por el preventista al tomar el pedido, aunque cambie posteriormente la lista de precios. | El cambio de precio entre pedido y despacho requiere arbitraje; decisión 9. |
| S-10 | Control por saldos, sin serialización de cada envase. | Se conocen cantidades y pérdida estimada; el modelo está abierto; decisión 10. |
| S-11 | Maestro rector y equivalencias con códigos externos. | La inconsistencia de códigos y formatos debe resolverse; decisión 11. |
| S-12 | Flujo, autorizaciones y momento de emisión ante devolución. | El ERP es el único emisor de la nota de crédito y se conserva; decisión 12; cap. 5; restricción 4. |
| S-13 | Excluir cámaras y limitar GPS a vehículo/ruta hasta acuerdo sindical. | Se registra la objeción sindical y se exige hacerse cargo; decisión 13; restricción 10. |
| S-14 | Reemplazar el WMS, en vez de mantenerlo o extenderlo. | El destino del WMS es decisión del PROPONENTE, con justificación técnica y económica; cap. 5; decisión 14. |
| S-15 | Elegir firma, fotografía, nombre o QR y su articulación con el acuse. | Se exige POD digital y cumplimiento tributario; decisión 15; RT-16.14 del caso. |
| S-16 | Captura en E1 mediante talleres meses 1–3 y alternativa ante retiro anticipado. | El retiro se ubica a dos años y se exige preservar conocimiento; no hay fecha exacta ni método impuesto; decisión 16; secciones 4.4 y 13.1; resultado 16. |

## S-17 a S-41: información o hipótesis no determinadas completamente

| ID | Qué queda sin resolver | Qué dicen efectivamente las Bases | Cómo se resuelve |
|---|---|---|---|
| S-17 | Fecha de inicio y calendario efectivo compatible con congelamientos e hitos. | BA, arts. 7 y 17: meses relativos y cronograma obligatorio. Caso 13.3: restricciones de paso a producción. El calendario de licitación no fija la fecha exacta de inicio contractual. | Aclaración/calendario contractual y validación de escenarios. |
| S-18 | Interfaces concretas, operaciones, formatos, permisos y suficiencia sin modificar ERP. | La entrevista del Jefe de TI dice expresamente que existen y se usan; se desconoce cuáles y cómo. El cap. 5 declara falta de documentación. | Levantamiento y prueba de integración. No hace falta suponer su existencia genérica. |
| S-19 | Derecho contractual de acceso y disponibilidad técnica de datos de telemetría. | Cap. 5: se mantiene como fuente y debe integrarse; el CLIENTE no tiene claridad sobre las condiciones de acceso. | Revisión contractual con proveedor y validación técnica. |
| S-20 | Fecha real de disponibilidad del hardware antes de cada ola y posibilidad de absorber demoras. | Compra por CLIENTE y especificación por PROPONENTE están resueltas en E-09 y BTT 8.3. | Plan de compras, responsables y fechas límite; analizar efecto en hitos. |
| S-21 | Promesa segmentada de 24/48 horas y corte a las 14:00. | Las entrevistas describen tensión Comercial/Operaciones; no imponen esos plazos ni el corte. La solución del SD2 es decisión de LafroX, no una respuesta de las Bases. | Modelar capacidad y calendario; comprometer regla viable y validarla con Comercial/Operaciones. |
| S-22 | Número y detalle de instalaciones actuales que deben cubrirse. | Sección 2.3 enumera cinco; entrevista TI dice cinco; 14.1 y RT-21.16 del caso dicen seis. | Consulta al mandante e inventario de sitios. Parametrizar no resuelve la discrepancia de alcance. |
| S-23 | Relación entre personas, dispositivos y concurrencia; interpretación para dimensionamiento. | Sección 2.4: 84 conductores/peonetas propios y aproximadamente 160 externos, aproximadamente 244 personas. El «≈200 conductores» de 14.1 excluye peonetas: no es necesariamente una cifra contradictoria. | Separar roles, personas, turnos y equipos compartidos; inventario operacional. |
| S-24 | No hay hipótesis pendiente en el mínimo de autonomía. | Caso cap. 15, RT-03.10: CD 24 horas y terreno 14 horas. | Tratar como restricción/requisito y demostrar cumplimiento. |
| S-25 | Disponibilidad efectiva, calidad, granularidad y extracción de historia/promociones para reposición. | Sección 4.1 usa ocho semanas de ventas y ajuste manual; cap. 15, RT-05.15, exige migrar tres años de ventas/pedidos. Eso no describe calidad o interfaz de acceso. | Perfilado de datos y levantamiento con abastecimiento/TI. |
| S-26 | Meta de pérdida de envases del 7 % y reducción a la mitad. | El 14 % es pérdida actual estimada; cap. 18, resultado 12, deja la meta al PROPONENTE. | Comprometer meta fundada, establecer fórmula y validar línea base. |
| S-27 | Umbral de ocupación de 60 % y política de excepciones. | 68 % es promedio actual y 41 % un día observado; resultado 14 deja el umbral al PROPONENTE. | Cálculo por rutas, regla de autorización y compromiso de meta. |
| S-28 | Aceptación de transportistas para instalar termógrafos y fecha de instalación. | Sección 2.3 informa diez camiones de terceros con frío; resultado 3 exige registro continuo. No entrega autorización contractual. | Acuerdo con cada transportista y calendario de instalación/certificación. |
| S-29 | Usar 2,3 % como tolerancia de migración. | El 2,3 % es discrepancia actual del conteo, no tolerancia autorizada de transferencia; sección 4.2 y tabla 7.1. | Separar saneamiento y exactitud de transferencia; aprobar saldos y criterios de corte. |
| S-30 | Compartir terminal, impresora y POS por camión en lugar de por conductor. | Se conocen 96 camiones y rotación; no se fija política de asignación de cada periférico. | Decisión de dimensionamiento validada con Operaciones y transportistas. |
| S-31 | Crecimiento de camiones proporcional a viajes. | Tabla 14.1 proyecta viajes de ≈2.100 a ≈2.400, pero no cantidad de camiones. | Escenarios de capacidad: más utilización, más viajes o más vehículos. |
| S-32 | Crecimiento de terminales proporcional a dotación. | Se proyectan preventistas y personal de CD, no terminales simultáneos. El caso menciona equipos compartidos por turno. | Dimensionar concurrencia y política de asignación por perfil. |
| S-33 | Mismos preparadores realizan carga, sin personal adicional con terminal. | Sección 4.5 describe preparación y carga y menciona al cargador; no determina que sea la misma cuadrilla. | Levantamiento de funciones y turnos. |
| S-34 | Distribución proporcional de líneas de congelado según productos y superficie. | Se conoce el total conjunto de SKU fríos y superficies, no líneas de picking por régimen térmico. | Medición o estimación de mezcla y concurrencia, con validación. |
| S-35 | Dos personas simultáneas por cross-docking. | Cap. 3 describe personal reducido, sin cifra. | Levantamiento por plataforma y franja horaria. |
| S-36 | Cobertura de 500 m² por punto Wi-Fi y densidad en cámaras. | Se exige estudio de cobertura: RT-03.24 del caso y RT-03.23 BTT. No se fija superficie por punto. | Estimación radioeléctrica y estudio de sitio. |
| S-37 | Cámara refrigerada de Concepción de 450 m². | Sección 2.3 informa 9.000 m² de instalación y existencia de refrigerado, sin superficie de esa cámara. | Planos o medición física. |
| S-38 | Mantener fija la flota refrigerada durante el horizonte. | Se conocen 18 propios y 10 de terceros con frío; no se proyecta la flota fría. | Plan de flota y escenarios de crecimiento. |
| S-39 | 60 preparadores nocturnos en Concepción. | Se conocen 120 en la entrevista de bodega de Talca y menor escala en Concepción; no se da dotación nocturna del segundo sitio. | Nómina/turnos y carga operacional por sitio. |
| S-40 | Tipología del séptimo sitio y tratamiento de equipamiento/cotización. | 14.1 proyecta siete instalaciones y 13.2 menciona apertura eventual en Los Lagos hacia 2030, sin ubicación ni tamaño. | Consulta de alcance, escenarios replicables y tratamiento comercial explícito. |
| S-41 | Un computador por cada una de las 184 personas y uso de CrowdStrike. | Sección 2.4 da 184 personas; RT-08.09 exige gestión, cifrado, control de extraíbles, antivirus con detección/respuesta y actualización, sin imponer marca ni número de computadores. | Inventario TI; decisión justificada del producto y alcance de licencias/equipos. |

## Implicaciones para el anexo

- S-24 está enteramente fijado en su contenido obligatorio; conviene ubicarlo en restricciones, conservando una referencia si se requiere mantener numeración.
- En S-06, S-12, S-16, S-18, S-20, S-23 y S-41, separar el hecho u obligación conocido de la decisión o dato aún no confirmado.
- Mantener las decisiones delegadas como decisiones fundamentadas de la oferta, sujetas a la instancia de validación correspondiente. No dejarlas sin propuesta esperando que el CLIENTE las decida por el PROPONENTE.
- No usar el levantamiento futuro para omitir el dimensionamiento inicial: el capítulo 14 pide estimar, mostrar método y declarar supuestos en la propuesta.
- Las referencias al SD2 respaldan coherencia interna de LafroX, pero no convierten una decisión de la empresa en una instrucción de las Bases.

No se modificó el anexo en esta revisión.
