# Prompt de coherencia para el Subdocumento 4 (S4)

**Uso:** copiá este prompt completo y entregalo junto con la versión vigente de S4 y sus fuentes editables. El objetivo es sincronizar los cruces con S8 sin debilitar la coherencia interna, los requisitos de arquitectura ni los compromisos de S4.

## Contexto y límites

- La fuente de referencia vigente de S8 está en `08_plan_riesgos/contenido.tex`, `LAFROX-Subdocumento8-Anexos.tex` (anexos 8.A–8.D) y `LAFROX-Formulario-T-16.tex`.
- El Anexo 8.E fue eliminado. No lo recrees ni lo cites como destino. CI son controles internos, no riesgos transferidos al CLIENTE.
- En este repositorio S4 está disponible como PDF bajo `Datos externos/Informe_2_LafroX/`; no hay fuente LaTeX editable de S4. Los textos extraídos bajo `tmp/` son evidencia histórica/de navegación, no verificación de la versión actual.
- Si sólo tenés el PDF, no lo edites directamente ni fabriques fuente. Pedí la fuente editable o entregá instrucciones de reemplazo acotadas con documento, sección, página y texto.
- Verificá cada número de página, cita, ID y valor en los archivos vigentes. S8 guía la clasificación de los riesgos, pero no autoriza cambiar compromisos ni requisitos propios de S4.
- No edites S8, S7, S9, T-13 ni otros documentos comunes. Informá los cambios que dependan de ellos como pendientes separados.

## Prompt

> Actuá como editor técnico del Subdocumento 4 (arquitectura). Alineá sus cruces con el registro vigente de S8 manteniendo la coherencia interna de los requisitos, diagramas, objetivos, escenarios de falla, pruebas, anexos, T-11 y referencias de S4.
>
> Leé íntegramente el cuerpo, anexos y Formularios de S4, incluido T-11. Contrastá cada cambio con `08_plan_riesgos/contenido.tex`, `LAFROX-Subdocumento8-Anexos.tex` (especialmente 8.D) y `LAFROX-Formulario-T-16.tex`. Revisá el documento completo después de editar: no alcanza con corregir una sola mención.
>
> ### Cruces que tenés que resolver
>
> 1. **Identidad y operación degradada — B-S4-01 / CI-048.** La indisponibilidad de identidad central y la propagación de altas, bajas y revocaciones se clasifican como control interno CI-048, no como riesgo R-048 transferido al CLIENTE. Alineá la arquitectura, responsables y pruebas de operación sin conexión. Conservá responsabilidades SEG (control), ARQ (diseño), SRE (ejecución) y CAL (verificación) cuando correspondan. Comprobá que AL-OFF-01 cubra 24 horas sin WAN, relevos a las 8 y 16 horas, expiración, denegación y reconciliación antes de H5/H10; no describas un permiso inválido como autorizado por defecto.
> 2. **ERP y emisión de guías — B-S4-02 / R-049.** R-049 es una dependencia del ERP del CLIENTE, emisor único de guías, incluida la pérdida de la sala de Talca. No la confundas con R-008 (respuesta del SII), recuperación del WMS, colas locales ni conmutación de la plataforma. Si no existe una guía preemitida todavía válida, una carga modificada o una guía anulada no habilita la salida hasta poder emitir una guía nueva válida. No inventes un segundo emisor ni una excepción al objetivo de recuperación. Conservá separadas las pruebas AL-DTE-01 y AL-DR-01.
> 3. **Autoridad central de escritura y stock — B-S4-03 / CI-050.** La consistencia central y la exclusión del escritor anterior son control interno CI-050, no R-050 transferido al CLIENTE. Verificá que el diseño y AL-STOCK-01/AL-DR-01 cubran conciliación por UUID/sitio, trabajo pendiente no confirmado, promoción controlada y retorno sin doble escritura. Mantené distintos CI-050, R-004 (conciliación inicial) y R-019 (interrupción WAN).
> 4. **POS y SII — CI-009 y R-008.** La falta de respuesta del SII permanece como dependencia externa R-008. Idempotencia, consulta del resultado del POS tras timeout y prevención de doble débito son obligaciones internas CI-009, no riesgos del CLIENTE. Comprobá timeouts antes/después del cargo, consulta con la misma clave y conciliación.
> 5. **Conectividad, energía y cobertura.** Mantené diferenciados WAN por sitio (R-019), corte eléctrico externo (R-020), cobertura RF interior y fallos de diseño/alta disponibilidad. Comprobá rutas de respaldo y tiempos por sitio y componente: una ruta propuesta no prueba instalación ni conmutación. No equipares 3 horas de ventana local en cross-docking con 24 horas de autonomía requerida, ni UPS de gabinete de 30 minutos con generador de Talca de 24 horas. Verificá cobertura en cámaras reales, terminales, puertas y ocupación antes de afirmar que el diseño fue probado.
> 6. **Autorización de promoción y residencia.** Distinguí la decisión operativa de promoción R-018 (titular y suplente delegados, aviso al suplente tras 15 minutos y decisión dentro de 30 minutos) de la aprobación previa de residencia/transferencia de datos R-021. El silencio no autoriza promoción ni redirección de tráfico.
> 7. **Continuidad y recuperación.** Conservá RTO de 4 horas y RPO de 15 minutos. Separá la evidencia de AL-OFF-01, AL-DTE-01, AL-STOCK-01 y AL-DR-01. El retiro sanitario tiene máximo 2 horas; 15+60=75 minutos es un presupuesto objetivo a probar, no un resultado demostrado. No uses 85 minutos ni una prueba genérica para afirmar cobertura conjunta de las 96 salidas, ERP, WMS, identidad y retiro sanitario.
>
> ### Coherencia interna y cierre
>
> Antes de cambiar una pieza, identificá sus dependencias dentro de S4. Actualizá todas las apariciones afectadas sin dejar contradicciones entre requisitos, diagramas, amenazas, tablas, objetivos, pruebas, anexos, T-11 y referencias. Conservá requisitos de seguridad, continuidad, disponibilidad y recuperación. Si un control aún no está implementado, describilo como diseño/compromiso o prueba pendiente, nunca como resultado conseguido. No inventes datos ante discrepancias; documentalas y pedí decisión.
>
> Al finalizar, entregá una matriz `cruce S8 | ubicación en S4 | cambio | efecto en coherencia interna | evidencia verificada | pendiente`. Enumerá las comprobaciones completas de S4 y las dependencias que requieran actualizar S8/S7/S9/T-13. Separá hechos comprobados de pruebas propuestas. No afirmes que editaste un PDF si sólo produjiste instrucciones.

## Criterio de finalización

- Cada cruce aplicable tiene ubicación y tratamiento identificado en S4.
- No quedan referencias internas contradictorias ni se debilitan requisitos/objetivos de S4.
- Las pruebas planificadas están diferenciadas de evidencia de ejecución.
- Los cambios que dependan de otros documentos quedan señalados, no aplicados fuera del alcance.