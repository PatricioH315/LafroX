# SD9: alineación metodológica y contractual con las Bases

## Objetivo y problema

Corregir el cuerpo del plan de calidad frente a las Bases vigentes: medición contractual de restauración y disponibilidad, exclusiones de trazabilidad, clasificación del esfuerzo de calidad y afirmaciones sobre pruebas, aceptación y capacidad. El contraste con clases, PMBOK 6 y el extracto de calidad del compañero orienta el método; las Bases prevalecen.

## Alcance autorizado y restricciones

- Rama comprobada: `rama-md`; conservarla y trabajar únicamente en Markdown.
- Fuente editable: `09_plan_calidad/LAFROX-Subdocumento9.md`.
- Seguimiento: este archivo y `compct/CONTEXTO_SESION.md`.
- No editar SD7, SD4, anexos, T-13, T-17, figuras, planillas, Bases ni archivos históricos.
- Conservar títulos obligatorios, figuras Mermaid, umbrales existentes, marcadores de revisión humana y cifras verificadas. No atribuir pruebas, acreditaciones o aceptación sin evidencia.
- No inventar fechas, HH, disponibilidad de especialistas ni divisiones de paquetes mixtos. No publicar ni cambiar de rama.
- El commit local se resolverá según la política vigente y la instrucción del coordinador; nunca hacer push.

## Tarea y aceptación

- [x] **SD9-01 — Corregir y verificar el cuerpo de SD9 contra las Bases.** Cierre local; las dependencias externas siguen abiertas.
  - Ruta: **delegada**; disparador: investigación previa y redacción no mecánica sobre varias afirmaciones contractuales relacionadas.
  - MTTR: media mensual desde detección hasta restitución verificada, ≤4 h (BA 78.3); distinguir máximos individuales de resolución (BA 78.2).
  - Presupuesto de error: minutos del mes real, indisponibilidad computable y exclusión de mantenimiento aprobado (BA 79.4); mantener indisponibilidad cero en despacho (Caso RT-10.05).
  - DRE: delimitar defectos conocidos de una misma cohorte/versión y corte mensual; denominador cero no acredita un resultado favorable.
  - Trazabilidad: 22 ID No cumple y nueve absorbidos/alias explican 31 sin prueba propia; preservar 645 ID, 614 con prueba propia y 1.308 casos.
  - Costo: preservar 10.848 HH = 4.224 + 6.624 y aproximadamente 5,0 %; identificar grupos de paquetes mixtos, no categorías puras sin desglose. El valor esperado de tres riesgos no es todo el costo de no conformidad ni demuestra eficiencia por su cociente.
  - Pruebas: retirar garantías absolutas sobre caminos y recurrencia; distinguir certificación inicial y aceptación contractual de la verificación/validación que continúan durante el proyecto.
  - Certificación de cierre: contemplar las pruebas aplicables de BTT 20.1 y RT-11.20 sobre la versión de cierre, incluida recuperación real y accesibilidad; sin inventar una programación ya aprobada.
  - Capacidad: distinguir techo aritmético de disponibilidad demostrada por especialidad, tercero, ambiente y ventana. Preservar los compromisos contractuales y explicar condiciones de habilitación sin notas de asistente en el entregable.
  - Actualizar el contexto compacto y registrar evidencia observada y límites; no marcar cerradas las dependencias externas.

## Verificación

Documentación pasiva: no existe un RED/GREEN funcional significativo ni una frontera de ejecución que probar. Aplican lectura contractual, comprobaciones deterministas y revisión estructural; no se ejecutan ensayos de la solución ni se acredita revisión humana.

- `git diff --check`: requerido tras las ediciones finales.
- Script de lectura sin archivos versionados: comprobar 645 = 614 + 31; 31 = 22 + 9; 1.308 = 849 + 354 + 105; 10.848 = 4.224 + 6.624; capacidad 16 × 21 × 6,4 = 2.150,4; presupuestos críticos de meses de 28/29/30/31 días.
- Comparar antes/después: lista de encabezados, marcadores de revisión humana y bloques Mermaid conservados; ausencia de frases falsas identificadas, sin eliminar los criterios exigibles.
- Releer BA 78.2/78.3/79.4, BTT 20.1 y RT-11.20, Caso RT-10.05 y Aclaraciones §11/§7.1 antes de cerrar.
- Confirmar diff limitado a las tres superficies autorizadas y exclusivamente Markdown.

## Límites y dependencias externas

- Fechas, HH y nivelación de las recertificaciones H7/H12 en SD7/T-13 no se pueden cerrar con el cuerpo de SD9 solamente. Requieren una intervención posterior autorizada; no acreditar disponibilidad completa ni calendario inexistente.
- SD4 necesita armonización posterior de mediana/media y presupuesto fijo/mes real; no se modifica en esta unidad.
- Anexos, T-13/T-17, figuras y planillas pueden mantener diferencias fuera de alcance. No se declara coherencia documental total ni conformidad final.

## Progreso, entrega y siguiente paso

- Estado: correcciones locales de SD9-01 aplicadas, verificadas y cerradas por el coordinador. No se acredita resolución de las dependencias externas.
- Espejo Engram: versión inicial completa confirmada por el coordinador en observación #116 antes de las ediciones de fuente; esta actualización requiere nueva sincronización y lectura.
- Estrategia: `ask-on-risk`; previsión máxima de 170 líneas authored (adiciones + eliminaciones), incluidos registros; no se prevé PR ni publicación.
- Commit de unidad autorizado por el coordinador: `docs(quality): align SD9 with tender requirements`, exclusivamente las tres superficies de esta tarea en `rama-md`; ejecución sujeta al permiso de escritura de Git. No hacer push ni cambiar de rama. El coordinador conservará el resultado y la identidad observada en el espejo.
- Revisión nativa: RDD efectivo ON global; evaluación del coordinador con inventario explícito de la tarea: `passive`, `non_executable_only`, tres rutas y 95 líneas; `review_due: false`, motivo `passive`. No requiere revisor ni ceremonia de consentimiento. La lectura estructural y el spot-check `git diff --check` del coordinador pasaron; no se fabrica aprobación de ensayos ni conformidad global.
- Evidencia observada: script de lectura, salida 0: T-12 y 9.C con 645 ID y 22 No cumple; 614 pruebas propias; 1.308 casos; 10.848 HH; techo 2.150,4 HH; presupuestos críticos 40,32/41,76/43,2/44,64 min para 28/29/30/31 días. Cláusulas BA 78.2/78.3/79.4, BTT 20.1, Caso RT-10.05 y estructura de Aclaraciones verificadas contra el texto.
- Evidencia estructural: 25 encabezados, 10 bloques Mermaid y 10 marcadores humanos conservados frente a la instantánea original en memoria; expresiones falsas identificadas ausentes. `git diff --check`: salida 0 tras editar SD9.
- Conteo de fuente observado: 17 adiciones + 11 eliminaciones = 28 líneas authored; el conteo final incluirá el contexto y este registro.
- Siguiente paso: comprobación final y commit local si Git permite escribir; el coordinador sincroniza el espejo con el resultado. Las fechas/HH de SD7/T-13 y la armonización de SD4 siguen fuera de alcance.
