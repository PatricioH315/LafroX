# LafroX — Resumen del Formulario T-15: Programación y recursos

[Índice de resúmenes](README.md) · [Formulario original](../07_PlanDeTrabajo_EDT_Cronograma_Implantaci%C3%B3n/LAFROX-Formulario-T-15.md)

## Para qué sirve

Justifica esfuerzo, equipos, secuencia y reservas del cronograma. Convierte paquetes del T-14 en actividades y compara carga con personas disponibles.

## Cómo está organizado

Las secciones 1–3 explican estimación **PERT**, programación, ruta crítica y ocho frentes. [La sección 4](../07_PlanDeTrabajo_EDT_Cronograma_Implantaci%C3%B3n/LAFROX-Formulario-T-15.md#4-modelo-cuantitativo-de-recursos) contiene supuestos, HH por paquete y curvas mensuales. [La sección 5](../07_PlanDeTrabajo_EDT_Cronograma_Implantaci%C3%B3n/LAFROX-Formulario-T-15.md#5-red-agregada-restricciones-y-escenarios-de-calendario) aplica calendario, revisión y dotación; [la sección 6](../07_PlanDeTrabajo_EDT_Cronograma_Implantaci%C3%B3n/LAFROX-Formulario-T-15.md#6-lista-de-actividades-regla-del-880-y-del-per%C3%ADodo-de-reporte) detalla actividades y esfuerzo continuo.

**HH** significa horas hombre. La curva usa **128 HH efectivas por persona-mes**. La programación diaria usa **6,4 HH efectivas por persona y día**; son supuestos que deberán contrastarse con el equipo.

## Cifras clave

- **222 paquetes**: 163 con entregable y 59 de esfuerzo continuo.
- **163 paquetes con entregable** con fecha; actividades de **8 a 80 HH** y una quincena como máximo, detalladas hasta el H2 y luego por planificación gradual de reporte.
- **216.935 HH** programadas: **204.527** base (incluye el tercer agente de la mesa desde el mes 25), **9.336** de soporte puente y **3.072** protegidas para correcciones E1.
- Máximo mensual: **68 personas equivalentes en mes 15**; hasta **40 desarrolladores** simultáneos en la construcción E1.

No se suma nuevamente la reserva ni se agregan máximos de etapas que ocurren en momentos distintos. Los servicios continuos se controlan por ocurrencia, relevo o quincena; no se simulan como un entregable único.

## Calendario, revisión y capacidad

La red usa **febrero de 2027 como mes 1 supuesto**, días de lunes a viernes, dependencias del Anexo 7.B, nivelación y al menos **diez días hábiles de revisión del CLIENTE** dentro de los hitos. Las reservas dependen de esa red; no sustituyen fechas contractuales ni las cuatro semanas de evidencia.

[La dotación](../07_PlanDeTrabajo_EDT_Cronograma_Implantaci%C3%B3n/LAFROX-Formulario-T-15.md#57-dotaci%C3%B3n-requerida-roles-m%C3%ADnimos-y-dotaci%C3%B3n-declarada) distingue equivalentes mensuales de personas simultáneas. Desarrollo usa hasta **40 personas simultáneas** de las 48 de la división durante la construcción E1 de junio a septiembre de 2027, cuyo último paquete termina el **30-09-2027**; la dotación declarada usa PHP/Laravel y Kotlin, y el Líder de Desarrollo verifica la experiencia de cada persona antes del mes 5. Seguridad, Calidad e Implantación requieren asignación, contratación o servicios externos; Calidad contempla evaluadores hasta **16 por día**. Estos refuerzos son condiciones de planificación, no disponibilidad acreditada.

## Límites y relaciones

Los tamaños por clase, productividad, compras y fecha de inicio deben validarse. La sala sigue la secuencia planos en el mes 1, orden de compra de LafroX en el mes 2, instalación en el mes 3 y recepción en el mes 4, igual que SD6 y T-14. La ruta crítica es la cadena de la Etapa 2 (H8, H9 y H10). La simulación del SD8 usa esta programación y sus supuestos; un percentil no demuestra ejecución.

Consultar [T-14](LAFROX-Formulario-T-14-Resumen.md) para entregables, [T-18](LAFROX-Formulario-T-18-Resumen.md) para activación/reversión y [anexos 7.B/7.F](LAFROX-Subdocumento7-Anexos-Resumen.md) para dependencias y condiciones.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
