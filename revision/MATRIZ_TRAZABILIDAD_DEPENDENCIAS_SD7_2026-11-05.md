# Trazabilidad y dependencias de las correcciones del Subdocumento 7

Fecha: 5 de noviembre de 2026.

Fuente evaluadora: `C:/Users/Leandro/Downloads/G02 - LAFROX - Primera Revisión Informe 2.pdf`. Las páginas indicadas son las del PDF evaluador, no las de los entregables.

Esta matriz conserva los quince puntos propuestos en la conversación. Distingue la observación del evaluador de los hallazgos adicionales y separa tres relaciones que pueden coexistir: entradas de otros documentos, trabajo dentro del S7 y propagación del cambio a documentos que utilizan sus resultados.

## Convenciones y límites

- **Ámbito S7:** cuerpo del Subdocumento 7, anexos 7.A–7.F, T-14, T-15, T-18, fuentes LaTeX, figuras y cálculos correspondientes. Cambiar un formulario de este conjunto sigue siendo un cambio interno del S7.
- **Entrada externa:** información o decisión que S7 utiliza de otro subdocumento. Consultar una fuente existente no obliga a modificarla ni impide avanzar en el S7. Hace falta coordinación cuando la definición está abierta, es contradictoria o se propone cambiarla.
- **Salida hacia otros documentos:** referencias, códigos, fechas, HH o equipos que otros capítulos toman del S7. Los destinatarios se deben contrastar y actualizar si efectivamente contienen la información modificada.
- **Sólo S7:** edición que conserva alcance, compromisos, códigos utilizados externamente, esfuerzo, fechas, recursos y reglas compartidas. Si altera alguno de esos elementos, deja de ser exclusivamente local.
- **Origen R:** observación expresa de la revisión, aunque la acción propuesta agrupe varias observaciones. **Origen A:** añadido del análisis propio. Los métodos concretos para resolver una observación son propuestas de implementación, no nuevas exigencias atribuidas al evaluador.

Los impactos sobre capítulos que no están completos en esta carpeta son una previsión de coordinación basada en sus relaciones documentadas; no una afirmación de que se han inspeccionado y editado todas sus versiones vigentes.

## Matriz principal

| N.º | Corrección y trazabilidad | Entradas o decisiones de otros documentos | Trabajo dentro del ámbito S7 | Documentos que deben contrastarse al cambiar S7 | Clasificación |
|---:|---|---|---|---|---|
| 1 | EDT por productos; etapa como atributo. **R: pp. 27–28 y 32.** | S3/T-12: alcance y trazabilidad. S4: productos/módulos/interfaces. S13/T-19: cartera ofertada. Se pueden usar versiones coherentes ya disponibles; cambios de alcance requieren acuerdo. | Diseñar agrupación, diccionario y equivalencia de códigos; actualizar EDT, anexos, formularios, figuras y scripts internos. | S3/T-12, S9/T-13/T-17 y S13/T-19 por referencias a paquetes; matrices de S4/S5/S6/S8 que citen los códigos afectados. | **Entrada + S7 + salida.** No renumerar sólo el T-14. |
| 2 | Estimación derivada del tamaño por módulo. **R: pp. 28 y 32.** | S3/T-12: requerimientos. S4: complejidad e interfaces. S5: migración. S6: método de trabajo. S9: alcance de pruebas. | Calcular tamaño, productividad, esfuerzo y supuestos; rehacer tablas HH y memoria de estimación del T-15. | S1/capítulo 12 si cambia la demanda de personal; S8 por exposición y reservas; S9 por esfuerzo/costo de calidad; Oferta Económica si cambia la base de esfuerzo o contratación. | **Entrada + S7 + salida.** No fijar por anticipado que el total debe seguir en 220.023 HH. |
| 3 | PERT con O/M/P específicos. **R: pp. 28 y 32.** | Responsables técnicos de los componentes anteriores; S8 para consistencia con riesgos y correlaciones. | Fundamentar escenarios, recalcular incertidumbre de caminos y actualizar límites e interpretación de resultados. | S8 y los textos que reproduzcan probabilidades, holguras o reservas del S7. Si cambia el calendario, aplicar también la propagación del punto 5. | **Entrada + S7 + salida condicional.** La fórmula es local; los escenarios no deben inventarse sin fundamento. |
| 4 | Completar dependencias. **R: pp. 29 y 32.** | S3: secuencia funcional. S4: interfaces/habilitadores. S5: migración. S6: puertas del proceso. S9: pruebas/aceptación. S13: secuencia de innovaciones. | Completar predecesoras/sucesoras, justificar raíces, unificar tabla, anexo, diagrama y código de cálculo. | S5 si cambian ventanas de migración; S9/T-13/T-17 si cambian pruebas/aceptación; S13/T-19 si cambian ventanas de innovaciones; S8 por dependencias y riesgos. | **Entrada + S7 + salida.** El caso específico de 3.6.6 sin sucesor es un hallazgo **A**, dentro de esta corrección R. |
| 5 | CPM desde duraciones y relaciones. **R: pp. 29–30 y 32.** | Estimaciones, vínculos y recursos de los puntos 2, 4 y 7; plazos de aceptación definidos con S9/T-17 y Contraparte. | Generar fechas y caminos críticos; distinguir restricciones contractuales de fechas previamente elegidas; rehacer holguras y Gantt. | S3 donde concrete fechas; S8 por exposición/reservas; S9/T-17 por entregas y revisión; S13/T-19 por hitos de innovaciones; Oferta Económica si cambia la distribución temporal relevante. | **Entrada + S7 + salida.** No propagar cada cálculo provisional como versión definitiva. |
| 6 | Iteraciones, ceremonias y pruebas en Gantt. **R: pp. 25, 29–30, 32 y 40–41.** | S6/T-10: cadencia, incrementos y ceremonias. S9/T-13: pruebas por iteración. S3/S4: secuencia de construcción. | Descomponer construcción en actividades e incrementos con revisión, demostración y prueba; asignar HH dentro de los paquetes sin duplicarlas. | S6/T-10 si se ajusta el proceso o su cadencia; S9/T-13 por campañas y regresiones; S13/T-19 si se mueven incrementos o pilotos. | **Entrada + S7 + salida.** Es una coordinación de método y calendario, no sólo agregar barras. |
| 7 | Nivelar recursos y resolver CAL/IMP/equipos compartidos. **R: pp. 28–30 y 32.** | S1: capacidades corporativas. Capítulo 12/T-8: asignación y roles. S4: posiciones de operación/SOC. S6/S9: dedicación y perfiles. Confirmación de contrataciones/refuerzos cuando corresponda. | Calendario de dedicaciones, relevo y concurrencia; resolver 217,60 HH CAL faltantes y provisión de implantación; recalcular curvas. | S1 y capítulo 12/T-8 por compromisos de personal; S9 por capacidad de pruebas; S8 por riesgos de disponibilidad; Oferta Económica por contrataciones y costos derivados. | **Entrada + S7 + salida.** La planta declarada no equivale a disponibilidad del contrato. |
| 8 | Cerrar actas, revisión, producción y subsanación. **R: pp. 29, 32 y 41.** | S9/T-17: procedimiento y plazos. S3: evidencia y criterios. Contraparte Técnica: decisiones que le corresponden. | Modelar entrega completa, revisión, corrección, nueva revisión, firma y producción; recalcular hitos y estabilización. | S9/T-17, S3 en sus fechas/condiciones de implantación, S8 por riesgo de aceptación y cualquier calendario que replique H7/H12. Oferta Económica si hay efecto temporal o de esfuerzo. | **Entrada + S7 + salida.** No puede resolverse unilateralmente redactando un procedimiento como si estuviera acordado. |
| 9 | Defectos graves durante congelamiento de septiembre. **R: pp. 31 y 33.** | S6: cambios/promoción. S9: severidad, repetición y aceptación. S3/S4: continuidad. S8: tratamiento del riesgo. Autoridad del CLIENTE cuando deba decidir. | Regla en T-18: detección, contención permitida, corrección, prueba y efecto sobre evidencia/cierre. | S6/T-10 y S9/T-13/T-17 por reglas compartidas; S8 por respuesta, residual y contingencia; S3 si cambia la implantación. | **Entrada + S7 + salida.** No asumir excepciones al congelamiento ni reinicios automáticos sin criterio. |
| 10 | Preparación y certificación temprana de cadenas. **R: pp. 29 y 31.** | S3: cadenas/perfiles comprometidos. S4: contratos técnicos. S9: conformidad/aceptación. Disponibilidad del CLIENTE y de cada cadena. | Hitos tempranos de contacto, acceso y pruebas; dependencias de 3.6.5/3.6.6; puerta de habilitación y margen antes de evidencia final. | S3 por alcance/implantación; S4 si cambian requisitos de integración; S9 por pruebas/calendario; S8 por riesgo externo. | **Entrada + S7 + salida.** El vínculo faltante de 3.6.6 fue identificado por el análisis propio. |
| 11 | Evidencia temprana para proveedor de lácteos. **R: p. 31.** | S2/S3: problema, suspensión y compromiso. S4/S5: datos/evidencia técnicamente disponibles. Definición del CLIENTE/proveedor sobre lo aceptable. | Crear o precisar entregable, responsable, destinatario, fecha y criterio, distinguiéndolo del sistema definitivo. | S3/T-12 si se incorpora o precisa alcance; S9 si requiere nueva verificación; S8 si cambia la exposición a la suspensión; S4/S5 si la solución elegida altera diseño o datos. | **Entrada + S7 + salida condicional.** No presentar una propuesta de evidencia como aceptación del proveedor. |
| 12 | Conciliar reservas con S8. **R: pp. 36, 38 y 53.** | S8/T-16: riesgos, respuestas y esfuerzo. Gobierno de autorizaciones y Oferta Económica cuando corresponda. | Ubicar paquetes, perfiles, HH y períodos; distinguir reserva protegida, contingencia y gestión; evitar doble conteo. | S8/T-16 y anexos por uso y disponibilidad de reservas; Oferta Económica por financiación; S1/cap. 12 si exige capacidad adicional; S9 si reserva personal de calidad. | **Entrada + S7 + salida.** Es una conciliación bidireccional. |
| 13 | Gantt legible, agrupaciones claras y Figura 7.20 corregida. **R: pp. 29–30 y 32.** | Ninguna decisión externa nueva para tipografía, leyenda y diagramación. La versión final debe usar la red y el calendario cerrados internamente. | Redibujar/exportar láminas legibles; eliminar llamadas sin destino; mantener códigos y vínculos coherentes con la fuente. | Ninguno por presentación solamente. Si otra pieza reproduce la imagen, sustituir esa copia. Cambios de lógica se gestionan por los puntos 4/5. | **Sólo S7 en su parte gráfica.** Dependencia interna del cierre del modelo. |
| 14 | Depuración de cuerpo, tablas y duplicaciones. **R: pp. 31–33.** | Consultar destinos existentes en S3/S4/S5/S6/S9 para remisiones correctas. No exige editar esos capítulos si el contenido ya está allí. | Reducir celdas extensas, explicar en prosa, resumir reglas y retirar duplicaciones manteniendo los compromisos. | Ninguno si sólo se reorganiza la exposición y se conserva el contenido compartido. Si falta el contenido en su destino, coordinar su incorporación. | **Sólo S7 en la edición.** Deja de ser local si se cambian reglas o se traslada contenido inexistente fuera. |
| 15 | Consistencia editorial y cierre de entrega. **R: pp. 27, 31–32 y 3; además A.** | No requiere cambios externos para aclarar preparación/aprobación manteniendo H1/H8, definir siglas o explicar 10/40 min. Foliación y ficha final requieren consolidación de la propuesta. | Corregir rótulos, leyendas y referencias internas; verificar fuentes/PDF, metadatos y registro de validación. | Ninguno por erratas locales. La foliación global y las remisiones a folios, y la ficha común de entrega, pueden afectar toda la oferta. | **Mixto: separar 15a–15d**, como se detalla abajo. |

## Desglose del punto 15

| Subpunto | Procedencia | Cambio | Dependencia/propagación |
|---|---|---|---|
| 15a | **R:** p. 27 para 1.2.1/H1; pp. 31–32 para tiempos y siglas. | Aclarar elaboración frente a aprobación, leyendas y relación entre reversión técnica y total. | **Sólo S7**, si no cambia fechas contractuales ni reglas compartidas. |
| 15b | **A.** | Revisar también 1.2.5/H8, cuyo rótulo mezcla mes de elaboración y mes de aprobación. | **Sólo S7** como aclaración. Si se cambian fechas, aplicar puntos 5/8 y su propagación. |
| 15c | **A.** | Reconciliar los PDF finales con sus hashes y registro de QA; comprobar sincronización y salidas auxiliares. | **Sólo S7** para sus cinco entregables; el manifiesto general, si existe, recibe los hashes finales. |
| 15d | **R:** p. 3 para foliación integrada; **A** para reconciliar fecha/versión con revisiones posteriores. | Foliación correlativa de oferta y metadatos comunes de entrega. | **Consolidación transversal**. No asignar folios finales ni una nueva ficha común sólo desde S7. |

## Cómo distribuir el trabajo

### Trabajo local que puede adelantarse

Se pueden corregir rótulos y explicaciones sin cambiar compromisos; definir siglas; simplificar tablas; retirar duplicaciones que ya tienen destino; preparar formatos legibles y generar el inventario de referencias. Esto corresponde a 13, 14 y 15a–15c, con los límites anteriores.

También pueden adelantarse borradores de EDT, conteos de tamaño, auditorías de vínculos y escenarios de calendario. Son trabajos internos útiles aunque su cierre necesite entradas externas. No es necesario esperar a que otros capítulos estén completamente terminados para empezar.

### Definiciones que S7 debe recibir o acordar

- S3/T-12: alcance, requisitos, etapas y criterios comunes.
- S4/S5: arquitectura, interfaces, infraestructura y migración.
- S6/T-10: cadencia de desarrollo y política de cambios.
- S1/capítulo 12/T-8: personas y disponibilidad.
- S8/T-16: respuestas y reservas.
- S9/T-13/T-17: pruebas y aceptación.
- S13/T-19: alcance y secuencia de innovaciones.
- CLIENTE y terceros: decisiones de aceptación, disponibilidad y evidencia que les correspondan.

### Cambios que S7 debe comunicar tras estabilizar su base

| Si cambia en S7… | Debe comunicarse a… | Para actualizar o contrastar… |
|---|---|---|
| Códigos o estructura de paquetes | S3/T-12, S9/T-13/T-17, S13/T-19 y cualquier matriz que cite EDT | Referencias y trazabilidad. |
| Fechas, hitos y ventanas | S3, S5, S8, S9/T-17, S13/T-19; Oferta Económica si corresponde | Implantación, migración, exposición, aceptación, innovaciones y distribución temporal. |
| HH y dotación | S1/cap. 12, S8, S9 y Oferta Económica | Asignaciones, capacidad, reservas, esfuerzo de calidad y contratación. |
| Iteraciones, pruebas o reglas de cambio | S6/T-10, S9/T-13/T-17, S8 | Método de trabajo, campañas, aceptación y riesgos. |
| Reserva y su período de uso | S8/T-16 y Oferta Económica; responsables del personal afectado | Riesgo, autorización, capacidad y financiación. |
| Sólo tipografía o redacción | Responsables de copias de esas figuras, si las hay | Sustitución de la pieza, sin reabrir el alcance. |

La comunicación de cambios no equivale a modificar automáticamente los demás capítulos. Primero se identifica la referencia afectada y después se aplica la actualización correspondiente, preservando una tabla de equivalencias y una única versión de la base de planificación.
