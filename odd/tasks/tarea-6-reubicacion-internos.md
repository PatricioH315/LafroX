# Tarea 6: reubicación de asuntos internos del proveedor

Se retiran de T-16, 8.A, 8.B, 8.C y RBS los trece riesgos de diseño identificados expresamente en la revisión (p. 34): R-009, R-010, R-023–R-027, R-034–R-038 y R-040. Se aplica el mismo criterio a tres incorporaciones de tarea 5: R-047, R-048 y R-050. El registro vigente conserva 35 riesgos, con ID originales discontinuos, sin reutilizar los retirados.

El Anexo 8.E mantiene los 16 asuntos como CI con el mismo sufijo. Cada ficha conserva evento, dueño, destino documental propuesto, control, evidencia requerida, momento de verificación y bloqueo/corrección ante incumplimiento. Su estado es «reubicado; verificación pendiente»; no se declaran controles implementados ni defectos cerrados. Se preservan valoraciones, PERT/VE y las hipótesis previas, distinguidas del registro vigente. Las tres coordinaciones retiradas de 8.A.2 se conservan en 8.E.5; quedan 28 coordinaciones activas y 3 internas.

## Clasificación de las incorporaciones de tarea 5

- CI-047: dimensionamiento y escalabilidad ofertada; S4, 4.1.19 y 4.2.6.10–12; S9/T-13. La coordinación del cierre en septiembre continúa en R-044.
- CI-048: continuidad de identidad central/local y relevos; S4, 4.1.12/4.1.15, AL-OFF-01; S9/T-13. Conserva B-S4-01.
- CI-050: consistencia de consolidación, reserva y autoridad de escritura; S4, 4.1.15–16 y 4.3.2.5–6; S9/T-13. Conserva B-S4-03.
- R-045 se mantiene por cambio excepcional externo de soporte/compatibilidad, excluyendo mantenimiento ordinario y elección inicial sin soporte.
- R-046 se mantiene por restricción efectiva externa de salida/sustitución, excluyendo portabilidad omitida por diseño o falta de plan de salida.
- R-049 se mantiene por disponibilidad del ERP del CLIENTE, emisor único que LafroX no modifica. Recuperar el WMS no acredita recuperar el ERP. Conserva B-S4-02.

## Conciliación de perímetro

1.594,93 HH anteriores = 1.183,11 HH de los 35 riesgos vigentes + 411,82 HH históricas de los 16 asuntos internos. No es ahorro demostrado, reserva liberada ni costo de calidad aprobado. Se mantienen p0, O/M/P, PERT, VE e impactos individuales; sólo cambia el conjunto sumado y priorizado.

Distribución vigente: 1 Crítica, 14 Alta, 15 Media, 5 Baja. Ramas: Solución 3, Integración 6, Operación 13, Personas 8, Contrato 3, Regulatorio 2. Diez mayores VE: R-002, R-042, R-015, R-043, R-003, R-004, R-006, R-005, R-001, R-045; subtotal 689,67 HH (58,3 %). La reserva de gestión de 1.600 HH se mantiene separada, sin modificar su importe ni autorización. T-15, cronograma y presupuesto no se editan.

## Insumo para sincronización independiente posterior

| Destino a modificar después | Cambio requerido |
|---|---|
| S4, 4.1.2/4.1.6.2 y módulos M4/M7 | Integrar CI-009 (idempotencia POS) y CI-010 (dependencia del servicio de mapas elegido), con contratos y pruebas negativas/de caída. |
| S4, seguridad transversal 4.1.3.7, dispositivos/identidad y borde | Integrar CI-023–CI-027 con revocación, protección local, autenticidad EDI, defensa de canales y recuperación de evidencia. No declararlos como riesgo del CLIENTE en T-16. |
| S4, capacidad, identidad y reconciliación | Integrar CI-047/048/050 con las pruebas de 8.E.1; conservar brechas B-S4-01/03 como controles internos pendientes de evidencia. Mantener R-049 y su diferencia frente a CI-050. |
| S13, INN-01 | Sustituir referencia a R-034/T-16 por CI-034; mantener paquete 3.10.1.4 meses 11–15, H5 en 11–12, piloto real 13–15, I-01A en mes 15 ≥70 % y ≥100 avisos evaluables. DAT dirige, IMP coordina piloto, Comercial/Calidad validan catálogo 7–9. |
| S13, INN-02 | CI-035 y CI-036 deben quedar en diseño y validación de reproducción/captura, con diagnóstico base y sanitización previa a salida del terminal. |
| S13, INN-03 | CI-037 y CI-038 deben quedar como criterios de validación por familia y consistencia lote–sensor. Mantener RNG-04, fecha impresa y bloqueo de inferencia con historia incompleta. |
| S13, INN-04 e INN-05 | R-039 permanece riesgo contractual vigente (I3, E0,10 Media); CI-040 pasa al diseño y validación de comprensión/privacidad de la hoja. No conservar referencias de CI al registro vigente T-16. |
| S9, 9.2.1/9.2.3/9.2.5/9.2.6 y T-13 | Registrar pruebas/casos de los 16 CI, su vínculo a requisitos, versiones, resultados y defectos. Conservar G4/G5 bloqueantes, certificación H5/H10 y verificación periódica aplicable. La matriz prevista no acredita pruebas ejecutadas. |
| S7, EDT/T-14/T-15 y costo de calidad | Identificar controles compartidos y paquetes existentes antes de estimar cualquier diferencia. No cargar 411,82 HH como trabajo ordinario cierto ni trasladarlas a reserva del CLIENTE. Conciliar en tarea 8. |
| S6 y matrices transversales | Actualizar referencias retiradas por CI y destinos vigentes; mantener obligaciones de LafroX y coordinaciones de 8.E.5. Los ID R retirados no se reutilizan. |

Los destinos son propuestas de sincronización basadas en las secciones consultadas. Ningún archivo fuera de S8 y sus entregables se modifica. Las tareas 7 (respuestas/residual), 8 (reservas/cronograma) y 9 (técnica de análisis) siguen pendientes.

## Comprobaciones

`tmp/verificar_tarea6.py` verifica conservación individual, 35 registros activos, 16 CI, coordinaciones, hipótesis, bandas y límites, factores, impacto, exposición, zona, RBS, rankings, sumas y conciliación histórica. Comprueba las citas protegidas y las huellas SHA-256 de los PDF fuente consultables en las carpetas oficiales de la propuesta técnica. La base completa anterior queda en `tmp/tarea6-baseline.json` para auditoría; no se renumera ni pierde el ID de ningún evento.

Verificación final completada: cálculos y conservación por ID correctos; `git diff --check` sin incidencias. Los tres entregables compilan con LuaLaTeX y referencias estabilizadas: cuerpo de 24 páginas, anexos de 71 páginas y T-16 de 18 páginas. Se revisaron visualmente tablas, RBS en dos páginas, portada actualizada, folios, firmas y matrices internas. La revisión detectó y eliminó tres filas de hipótesis que se habían repetido bajo el encabezado de coordinación interna; la comprobación automática ahora exige exactamente tres filas de coordinación en 8.E.5. Persisten los mensajes preexistentes del motor sobre contracción de pegamento en la tabla 8.C, sin desbordamientos visibles ni referencias indefinidas. No se alteraron archivos de otros subdocumentos.
