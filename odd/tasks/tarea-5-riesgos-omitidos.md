# Tarea 5: omisiones incorporadas

Se agregan once riesgos R-041–R-051 y se conservan los cuarenta IDs anteriores. R-016 explicita jubilación y caída de 6–9 puntos y revalora I=4; R-019 explicita el enlace único inicial de Concepción y revisa p0 de 5 % a 25 %, manteniendo sus HH condicionales.

## Asunciones y cuantificación

Las probabilidades nuevas son hipótesis de planificación, no estadísticas del caso ni riesgos residuales demostrados. Fuente, ventana, episodios y bases de esfuerzo en 8.B.2; impacto máximo en 8.C.1. Se excluyen tareas ordinarias, pérdidas de bienes y reconstrucción del ERP del CLIENTE. El 38 % de rotación y las 2.600 entregas no se usan como p0.

Total ampliado: 1594,93 HH esperadas. Diez mayores: 739,40 HH (46,4 %). Se suman VE por riesgo redondeados a dos decimales; cada VE usa PERT sin redondear. Base anterior 1.100,60 HH; incremento R-019 de 12 HH y nuevos riesgos de 482,33 HH. No se deriva ni asigna una reserva aprobada, ni se modifica T-15, presupuesto o cronograma.

## Correspondencia para sincronización final

| ID | Omisión / fuente |
|---|---|
| R-041 | Desacuerdo sobre telemetría impide incorporación; Caso, caps. 10 (restricción 10), 16.1 y 19; S3, S-13; S7, acuerdo 5.4.2. |
| R-042 | Rotación nocturna supera inducción disponible; Caso, caps. 7.2, 10 (restricción 11) y 19; S7, pp. 21--22 y 32; T-14, 7.1.2; T-15, meses 13--56. |
| R-043 | Interfaces ERP/WMS no verificables a tiempo; Caso, cap. 5 y cap. 19; S3, S-18, S-14 y V-16; S7, 1.2.3 y 3.3.2. |
| R-044 | Peak y congelamiento impiden cierre de fase; Caso, caps. 10 (restricción 8), 17.5 y 19; S7, 7.3.1 y 7.3.5, pp. 37 y 58; T-18. |
| R-045 | Cambio de soporte exige adecuación extraordinaria; Revisión del Informe 2, S8, análisis 8.2; S4, plataforma declarada; S7, 8.2.5. |
| R-046 | Dependencia de proveedor limita salida o sustitución; Revisión del Informe 2, S8, análisis 8.2; S4, servicios gestionados; S7, 8.1.4 y fase 9. |
| R-047 | Capacidad efectiva insuficiente bajo carga peak; Caso, caps. 14, 17.4 y 19; S4, 4.2.6, pp. 153--167; S7, 7.3.5. |
| R-048 | Indisponibilidad de identidad afecta relevo; Brecha B-S4-01; S4, Tabla 4, p. 78; pp. 26--27, 46--47 y 81. |
| R-049 | ERP indisponible impide nueva guía válida; Brecha B-S4-02; Caso, cap. 10, restricciones 1 y 4; S4, pp. 78, 84 y 183. |
| R-050 | Consolidación central no confirma reservas; Brecha B-S4-03; S4, Tabla 4, p. 78; 4.1.15--4.1.16 y 4.3.2.5--4.3.2.6. |
| R-051 | Conductor externo rechaza uso de la solución; Caso, caps. 10 (restricción 6), 15, RT-22.04 y 19; S7, 5.4.1 y 7.1.3. |

Brechas de tarea 4: B-S4-01→R-048; B-S4-02→R-049; B-S4-03→R-050; B-S7-01→R-042. Estados actualizados en Anexo 8.D.

S4: enlazar riesgos R-043 y R-045–R-050 con contratos, capacidad, dependencia de AWS, identidad, ERP y stock. No atribuir a controles no ensayados eficacia demostrada. S7: vincular R-041 con 5.4.2, R-042 con 7.1.2 (13–56, IMP hasta 21/SRE desde 22), R-043 con 1.2.3/3.3.2, R-044 con cierre E2 y R-051 con 7.1.3. S3: conservar exclusión de cámaras en cabina, ERP único no modificable y WMS sustituido progresivamente.

S6/T9: integrar contrapartes y objetivos de coordinación de los once nuevos riesgos sin transferir responsabilidad de diseño. S13: conservar sincronizaciones pendientes de tarea 2 y R-034 según tarea 4.

R-044 y R-047 no son duplicados: coordinación/cierre frente a saturación técnica. R-013/R-031/R-051 separan firma, habilitación de reemplazo y rechazo individual. R-017/R-042 separan inasistencia y sobrecarga de inducción por rotación. R-008/R-049 separan SII y ERP. R-004/R-019/R-050 separan conciliación inicial, WAN y consolidación central.

## Pendientes siguientes

Tarea 6 revisa los trece internos originales y la ubicación de controles técnicos añadidos (R-045–R-048/R-050), preservando su trazabilidad según naturaleza; no se adelanta su reubicación. Tarea 7 completa costo-beneficio, esfuerzo de respuesta y riesgo residual. Tarea 8 concilia la nueva exposición de esfuerzo con reservas y cronograma. Tarea 9 aplica la técnica requerida.

## Verificación final

Tarea 5 completada. Se comprobaron los 51 registros provisionales, 31 coordinaciones y 11 hipótesis nuevas; bandas, factores, productos, zonas, PERT/VE, justificaciones y selecciones de diez riesgos son consistentes. El esfuerzo esperado es 1.594,93 HH, sin aprobar ni recalcular reservas de planificación.

Los tres entregables se compilaron con LuaLaTeX: Subdocumento 8 (25 páginas), anexos (55 páginas) y formulario T-16 (23 páginas). Se revisaron visualmente las páginas, incluidas tablas nuevas, hipótesis, matriz de cobertura, RBS, folios y firmas. La comprobación automática y `git diff --check` finalizaron correctamente. Las citas protegidas y las huellas de los documentos fuente permanecen intactas; no se modificaron otros subdocumentos, T-15 ni el cronograma. Las tareas 6–9 siguen pendientes.
