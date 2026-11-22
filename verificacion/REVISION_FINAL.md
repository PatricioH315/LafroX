# LafroX — Verificación del SD10

## Versión 0.5 · 21 de noviembre de 2026

La revisión conserva el SD4 `0dc50b3d` como corte técnico y coteja responsabilidades y mantención con T-8, T-14, T-15, T-18, SD11 `f92a6a99` y SD12 `a33dea8e`. Se registran 16 observaciones con fuente y estado en la trazabilidad.

| Comprobación | Resultado |
|---|---|
| Inventario y citas | Cinco sitios logísticos con cómputo local y casa matriz de Talca en nube, sujeta a confirmación en M1. Despliegue y plantillas cotejados en pp. 113 y 64 del SD4. |
| Escenario por perfil | Los 197 contactos adicionales de la sensibilidad se reproducen desde población y tasa. El escenario SD4 de 2.000 se conserva. Se verifica el porcentaje antes de 20 s con la dotación de cada escenario. |
| Peak y relevo | El verificador recalcula las filas nocturna, dominical y NOC. Septiembre de 2029 tiene cinco domingos. La alternativa suma 1.690 HH de mesa, 14 plazas por carga y 50 HH adicionales de NOC. La planilla de turnos y los datos de demanda siguen por acreditar. |
| Acuerdos internos | Las cuatro filas LaTeX se comparan con sus tramos calculados. Primera actuación y resolución quedan dentro de BA 78.2 en el diseño propuesto. |
| Continuidad y métricas | GU-02/03/08 conserva el emisor ERP; 10.B separa escenarios RPO y añade mediciones analíticas, de aviso remoto y de latido. Se conservan ambos denominadores de disponibilidad para la conciliación. |
| Conciliación | SD11 confirma bolsa, asignación por perfiles y control de tareas manuales. SD12 respalda titulares y procedencia de apoyos. El total de Operación frente a E2 y la fila del gerente conservan sus diferencias documentadas. |

Se compilaron y renderizaron 50 páginas, 20 de cuerpo y 30 de anexos. Se revisaron visualmente índices, portadas, tablas, figuras y páginas modificadas. Ambos PDF pasaron la validación de formato, foliación, texto seleccionable, referencias, tabla de IA y exclusión de importes. El verificador numérico pasó y comprobó la correspondencia con tres tablas LaTeX.

La entrega se mantiene como borrador revisado. Siguen abiertas la validación de sitio, dotación, apoyos, continuidad del emisor, RPO combinado, calendario y conciliación económica, además de la revisión humana, el A-6 y las firmas.


## Versión 0.4 · 21 de noviembre de 2026

Estado de entrega: borrador revisado para el Sobre 2. Se conserva la verificación histórica de 0.3. El registro de 0.4 incorpora trece hallazgos y cruces puntuales, con decisión, fuente y responsable del respaldo pendiente.

| Verificación documental | Resultado |
|---|---|
| Reconexión escalonada | Dos dispositivos que vuelven en momentos distintos tienen relojes independientes de diez minutos. El centro de distribución usa su propio plazo de dos horas tras un corte de 24 horas. GU-01 exige conciliar stock y verificar aplicación única por UUID. |
| Mantenimiento aprobado y exceso | En el ejemplo de 24 horas, dos caídas solapadas cubren 100 minutos y la ventana aprobada cubre 60. Computan 40 minutos de indisponibilidad. Ambos resultados se reproducen con 1.440 y 1.380 minutos de tiempo de referencia. |
| Carga modificada con ERP caído | GU-08 retiene el despacho hasta tener guía aplicable. La ruta para una carga intacta con guía válida está descrita. B-07 conserva como requisito previo a oferta respaldar continuidad del emisor para cumplir la ventana protegida. |
| Conmutación con pendientes | La tabla y el texto de 10.C sitúan el reenvío en el paso 6 y la verificación por UUID en el paso 7, antes de mover tráfico. El caso de aislamiento total seguido de pérdida física se registra en B-11. |
| Peak y capacidad | Los cálculos mantienen 2.283 contactos con dos puestos en valle. Con 2.391, dos puestos consiguen 78,33 % y tres 95,26 %. El escenario condicionado permanece explícito y se exige cuadrante o perfil de demanda que lo sustente. |
| Respaldo puntual | Se cotejaron T-8, T-14, T-15, T-18 y E2. Se verifican 9.336 HH de soporte puente y la coincidencia de 86.274,20 HH dedicadas. Se registran la diferencia total de 631,12 HH y las 12 HH del gerente para conciliación. |

Compilaron el cuerpo de 20 páginas y los anexos de 26. Se renderizaron las 46 páginas y se inspeccionaron las secciones modificadas, las tablas, los índices y la declaración de IA. Pasaron 17 controles de cálculo, el verificador de entrega y la revisión de diferencias de Git. El verificador conserva huellas SHA-256, texto seleccionable, formato carta, foliación, enlaces de índice, referencias resueltas y comprobación de ausencia de cifras monetarias en ambos PDF. Los casos de la tabla son ejercicios documentales de aceptación.

Antes de liberar el Sobre 2 se requieren los respaldos de ERP, RPO, cobertura de la sexta instalación, dotación por turno, acuerdos de apoyo y conciliación económica, según su alcance. La revisión humana, el A-6 y las firmas deben constar en los documentos de entrega. Las pruebas de habilitación se mantienen en la fase contractual correspondiente.


## Versión 0.3 · 21 de noviembre de 2026

**Estado:** Borrador revisado. La revisión asistida comprende el contraste técnico con el SD4 `0dc50b3d19990513daeae37fdb3c9d7a9595d334`, sus anexos y T-11, más las bases y aclaraciones. Los 32 hallazgos y conformidades tienen un registro en `trazabilidad/SD10_fuentes_y_brechas.md`. El manifiesto identifica y conserva las huellas del corte.

| Escenario cotejado | Criterio comprobado en la redacción | Evidencia fuera del borrador |
|---|---|---|
| Jornada ordinaria y nocturna | M6 habilita los cinco ambientes. El horario reducido aplica a los tres no productivos. Producción y Recuperación conservan sus compromisos, igual que la guardia para críticos y altos. | Calendario de servicio por canal y turno y detalle de costo por recurso. |
| Peak | La extensión nocturna y dominical queda bajo 60 horas-posición de diseño. El límite de 2.391 contactos requiere tres en el valle modelado o demanda compatible con el NOC de dos puestos. | Cuadrante nominal y registros para calibración. |
| Congelamiento | Se conserva el despacho protegido, el aviso planificado con diez días hábiles y el registro de contención y decisión escrita ante urgencia. | Autorización específica y acuerdos de reporte y medición. |
| Pérdida de WAN y ERP | GU-01 comprueba resincronización por tipo de operación. GU-08 libera la carga intacta ya amparada y retiene cambios o cargas sin guía aplicable. | Actas y coordinación del ERP. |
| Pérdida de cómputo, sala o región | GU-02, GU-03 y GU-06 separan la validación funcional, escritor único, ruta sanitaria y aviso remoto. El aislamiento total con posterior pérdida de sitio conserva su propio ensayo de RPO. | Actas de conmutación, retorno, V17 y falla combinada. |

Los dos PDF se recompilaron con LuaLaTeX. El cuerpo tiene 20 páginas y los anexos 24. Se renderizaron las 44 páginas y se comprobaron portadas, índices, folios, tablas, diagramas, referencias y declaración de IA. El verificador confirma formato carta, foliación correlativa, texto seleccionable, tablas completas y referencias resueltas. El resultado con la huella SHA-256 de cada PDF queda en `verificacion/resultado_entrega.json`.

La reproducción de capacidad pasó 11 controles. La mesa conserva 90,6 % en hora cargada y 84,2 % en valle para 2.000 contactos. Se comprobaron los límites 2.283 con dos agentes en valle y 2.391 cuando el valle deja de limitar. Se verifican además 135 min para la secuencia regional y 64,3 % de reducción teórica de horas de cómputo de ambientes no productivos.

La sexta instalación, las dotaciones y acuerdos, la conciliación económica, los ensayos y la revisión humana, A-6 y firma quedan sujetos a evidencia. La regeneración de los PDF de SD4 y T-11 se registra como dependencia del equipo responsable de esa fuente. Los cambios del SD10 se limitan al checkout de su rama de corrección.

## Registro histórico · versión 0.2

Fecha: 17 de noviembre de 2026. Estado: borrador revisado. La revisión automática y visual asistida por Codex no acredita revisión humana ni aceptación del CLIENTE.

## Cambios verificados frente al contraste

| Punto | Resultado documental |
|---|---|
| Índice obligatorio | Capítulo «Introducción a los Servicios», con 10.1 y 10.2 conservados. |
| Declaración de IA | Tabla de seis columnas y siete filas: secciones 10.1/10.2 y anexos 10.A–10.E. No se atribuye revisión humana. |
| Redacción y fuentes | Retirada la frase «El usuario autorizó…» y la referencia técnica a la plantilla. Citas de bases con páginas; notas de preparación sustituidas por condiciones del servicio. |
| Atención y escalamiento | Recepción telefónica y alertas vinculadas al ticket; clasificación, transferencia, primera atención, restitución, confirmación de cierre y relevo definidos. |
| Acuerdos operacionales | Funciones, disparadores, evidencia y coordinación desarrollados. La derivación no reinicia relojes ni suma tiempo al máximo externo. Presupuestos numéricos internos y formalización siguen sin acreditarse. |
| Hardware | Mínimos BTT 8.4 incorporados: crítico 24×7/4h, no crítico 24 h, reemplazo crítico 4 h desde diagnóstico, fabricante y reserva mínima 10 %. No se añaden compras ni precios. |
| Retención | Política técnica incorporada desde SD4/SD5: registros 12 meses en línea + 24 meses de archivo, métricas 13 meses, trazas 30 días sin archivo adicional, auditoría/seguridad 7 años; ADOT 24 h temporal. |
| Procedimientos | Nueve guías GU-01–GU-09 con responsables, acciones, escalamiento, precauciones y comprobación. Recuperación regional y retorno controlado desarrollados. |
| Indicadores | Causa raíz media a solicitud y baja no exigida; fórmulas operacionales y tratamiento de denominador cero. Se distinguen contacto, ticket, restauración y cierre. |
| Calendario | Ventanas y congelamientos explícitos; prohibición de paso en septiembre completo de SD4 conservada sin presumir excepciones. |
| Detección proactiva | Mecanismo determinista de comparación histórica y prueba de degradación gradual recogido desde SD4. |
| Matriz y trazabilidad | Estados diferenciados entre diseño documentado, formalización, ensayo y conciliación económica; doce cambios V02-01–V02-12 trazados. |

## Comprobaciones realizadas

Se conserva el conjunto de fuentes congelado para la versión 0.1. Las incorporaciones se cotejan con fuentes LaTeX y sus PDF, sin espejos Markdown de subdocumentos. Bases y aclaraciones se consultan en sus archivos de origen.

El desglose de retención sí estaba en SD4, fuente lógica líneas 582 y 623–625, y en SD5, gestión línea 85. Se corrige la omisión del contraste previo. En los PDF del mismo commit se localizan los pasajes de SD4 en páginas de archivo 47–49 y el de SD5 en página 35. La política de archivo adicional de métricas no se inventa ni se generaliza desde los registros técnicos.

Se cotejan visualmente los folios impresos 6 de BA (artículo 5),19 de BTT (soporte de hardware) y 26–27 del Caso (p95 y ventanas). En esos PDF de imagen, la posición de archivo es el folio+1. Las huellas se añaden al manifiesto de fuentes.

El script comprobar_calculos.py reproduce diez controles: Erlang C 90,6%/84,2%; límites enteros de contactos; sensibilidad 6.000; DR 135 min; reducción teórica de horas 64,3%; plazas 8/13 y fracción de deuda técnica 2,0985%. No acredita abandono real, demanda observada ni ensayo ejecutado.

El script comprobar_entrega.py verifica PDF legible y sin páginas vacías, título, declaración de IA completa en una página, nueve guías, retención, causa raíz media, ausencia de notas del usuario, referencias resueltas, ausencia de glifos faltantes, desbordes horizontales y tablas partidas. Conserva páginas y SHA-256 en resultado_entrega.json.

Se renderizan todas las páginas de ambos PDF para inspeccionar portada, índices, folios, contenido, tablas y diagramas. Se ajusta el ancho de la declaración de IA y se evita la separación automática de palabras en tablas, conservando tipografía y clase corporativas.

## Dependencias conservadas y límites

La versión desarrolla lo respaldado, sin asignar nombres, contactos, productos, contratos, mediciones, firmas o aprobaciones inexistentes. B-04 ya no identifica ausencia de política técnica; mantiene la comprobación del costo asociado en E2 fuera de este alcance. Las condiciones B-01–B-10 conservan las dependencias de sitio adicional, habilitación, acuerdos específicos, relojes, ERP, cuadrante/calibración, SD11/12 y conciliación técnica-económica.

No se requiere fingir contratos ya suscritos para declarar cobertura propuesta. Sí se requiere formalizar y habilitar el servicio, y someter sus procedimientos a las pruebas indicadas. Los nuevos campos de registro y las fórmulas se identifican como elaboración procedimental y metodológica, no como citas literales ni decisiones aprobadas.

Sólo se modifica la rama de corrección de SD10. El Excel, E2 y los demás subdocumentos no se editan. El resultado continúa siendo borrador hasta contar con revisión humana real.
