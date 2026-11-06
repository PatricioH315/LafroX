# Prompt de coherencia para el Subdocumento 13 (S13)

**Uso:** copiá este prompt completo y entregalo junto con la versión vigente de S13 y sus fuentes editables. El objetivo es alinear las referencias de riesgos con S8 sin alterar la coherencia interna, el alcance, los indicadores, etapas, dueños ni criterios de habilitación de las innovaciones.

## Contexto y límites

- La fuente de referencia vigente de S8 está en `08_plan_riesgos/contenido.tex`, `LAFROX-Subdocumento8-Anexos.tex` (anexos 8.A–8.D) y `LAFROX-Formulario-T-16.tex`.
- El Anexo 8.E fue eliminado. No lo recrees ni lo cites como destino. Los controles CI son internos; no son riesgos transferidos al CLIENTE.
- En este repositorio S13 está disponible como PDF bajo `Datos externos/Informe_2_LafroX/`; no hay fuente LaTeX editable de S13. Los extractos bajo `tmp/` son evidencia histórica/de navegación, no verificación de la versión actual.
- Si sólo tenés PDFs, no los edites ni fabriques fuente. Pedí la fuente editable o entregá instrucciones de reemplazo acotadas, con documento, sección, página y texto.
- Verificá directamente en las versiones vigentes las citas, ID, páginas, valores e indicadores. S8 es la referencia actual para la clasificación de riesgo, pero no permite debilitar compromisos o puertas de habilitación de S13.
- No edites S8, S4, S7, S9 ni otros documentos. Reportá cambios dependientes de ellos como tareas separadas.

## Prompt

> Actuá como editor técnico del Subdocumento 13 (innovaciones). Alineá sus referencias al registro de riesgos con la clasificación vigente de S8 sin alterar la lógica, alcance, etapas, indicadores, responsables, criterios de habilitación ni compromisos propios de cada innovación.
>
> Leé íntegramente S13, sus anexos y el Formulario T-19. Contrastá todas las menciones de riesgos, matrices, ID, probabilidades, impactos, responsables y criterios de habilitación con `08_plan_riesgos/contenido.tex`, `LAFROX-Subdocumento8-Anexos.tex` (8.A–8.D) y `LAFROX-Formulario-T-16.tex`. Verificá directamente las páginas y referencias actuales; los extractos de `tmp/` no son prueba de la versión vigente.
>
> ### Cruces que tenés que resolver
>
> 1. **Reclasificación de riesgos de diseño.** En T-16 los asuntos de diseño y construcción se retiraron de los riesgos transferidos al CLIENTE. Alineá en todo S13 estos seis ID: R-034→CI-034, R-035→CI-035, R-036→CI-036, R-037→CI-037, R-038→CI-038 y R-040→CI-040. Revisá cuerpo, tablas, anexos, formularios, referencias cruzadas y menciones a RBS/T-16; no dejes ID anteriores como riesgos vigentes del CLIENTE. Conservá controles, dueños, indicadores y puertas de decisión como trabajo interno de diseño/verificación. No cites el eliminado Anexo 8.E ni inventes otro destino. Si S13 necesita indicar un artefacto de seguimiento interno y no existe uno confirmado, reportá el vacío en vez de inventarlo.
> 2. **INN-01 / CI-034 y piloto.** Conservá el paquete 3.10.1.4 en meses 11–15, certificación H5 en 11–12 y piloto real con locales en 13–15. Alineá coordinación del piloto (IMP), dirección de INN-01 (DAT) y validación del catálogo (Comercial/Calidad) en meses 7–9 si siguen vigentes en S13. I-01A exige al menos 70 % de aciertos con al menos 100 avisos evaluables al mes 15; no amplíes a otras rutas sin cumplirlo. Revisá la referencia antigua del tipo R8-25: cambiála sólo después de verificar qué riesgo/documento cita y confirmar que el destino vigente es CI-034. No elimines ni debilites el piloto al cambiar la clasificación.
> 3. **INN-02, INN-03 e INN-05.** Alineá las referencias de diseño/verificación con CI-035–CI-038 y CI-040, preservando indicadores, responsables y condiciones para habilitar cada función. La reclasificación a CI no significa aceptación del diseño, cierre del control ni reducción automática de valoraciones históricas.
> 4. **Mantener R-039 como riesgo del CLIENTE.** No reclasifiques la liquidación contractual de INN-04: S8 la conserva como R-039, impacto 3 y exposición 0,10 (Media). Cotejá en fuentes vigentes probabilidad 40 %, PERT 61,33 HH y VE 24,53 HH. Alineá su tratamiento con mes 20, tres liquidaciones sombra en meses 21–23 y pagos variables desde mes 24; una disputa puede suspender el devengo afectado, pero no el servicio. Si S13 muestra valores distintos, identifica la fuente que gobierna y presenta la discrepancia; no los sobrescribas sin resolverla.
>
> ### Coherencia interna y cierre
>
> Tras cada cambio, revisá de extremo a extremo la innovación: descripción, alcance obligatorio/opcional, calendario, etapas, indicador, fuente de datos, responsable, costo/horas, habilitación, riesgo y referencias. Mantené consistencia entre cuerpo, tablas, anexos y T-19. No cambies indicadores ni puertas de seguridad para ajustarlos a una puntuación de riesgo. No sustituyas términos del contrato ni conviertas validaciones pendientes en hechos cumplidos. Ante datos contradictorios, no inventes: documentá y pedí decisión.
>
> Al finalizar, entregá una matriz `innovación/ID anterior | ID vigente | ubicaciones revisadas | cambio | indicador/puerta preservados | coherencia interna verificada | pendiente`. Indicá cuántas referencias obsoletas quedaron (objetivo: cero) o justificá cada excepción. Si sólo tenés PDFs, no los edites: pedí fuentes editables o entregá instrucciones de reemplazo acotadas y verificables.

## Criterio de finalización

- Todas las referencias internas de S13 usan la clasificación/ID vigente, sin referencias contradictorias entre cuerpo, anexos y T-19.
- I-01A y las ventanas del piloto se conservan sin presentar resultados no verificados.
- R-039 permanece como riesgo cliente con la valoración vigente cotejada.
- Los cambios mantienen alcance e indicadores y las dependencias externas quedan explícitas.