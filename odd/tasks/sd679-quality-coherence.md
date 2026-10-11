# Corrección coordinada SD6–SD7–SD9

## Objetivo y alcance
Resolver los trece hallazgos del plan de calidad en Markdown, con propagación mínima a cronograma y capacidad. SD8, SD1, SD4 y fuentes quedan fuera de edición; preservar cambios previos del usuario.

## Estrategia
Dos unidades locales; delivery_strategy: exception-ok autorizado por el usuario. Pronóstico: 430–520 líneas authored. Ruta delegada por preparación analítica y múltiples archivos; un solo escritor. RDD OFF, sin activación ni publicación. Commits pendientes del coordinador.

## Tareas
- [ ] Q1: Reconciliar puertas, aceptación, doce pruebas, métricas y calendario contractual. Commit pendiente.
  - [x] Implementación documental y comprobaciones locales.
  - [x] Verificación independiente, incluido rechecado de corrección acotada.
- [ ] Q2: Completar restauraciones puente, desglosar H1 y reestimar campañas con trazabilidad y conciliación de capacidad. Commit pendiente.
  - [x] Implementación, aritmética y coherencia documental verificadas.
  - [x] Condiciones de capacidad nominal y PERT efectivo conservadas como pendientes, sin acreditar factibilidad.

## Restricciones y aceptación
Bases prevalecen. No cambiar hitos contractuales; G5 permanece H7/H12 y control técnico previo H6/H11. Sin dependencia numérica de SD8. No acreditar pruebas ejecutadas ni revisión humana. SD6 sólo cambia por capacidad real afectada. Cifras nuevas derivadas de supuestos explícitos; no garantía de factibilidad sin evidencia nominal.

## Comprobaciones
Sin RED aplicable a documentación pasiva. git diff --check; conteos 12 pruebas, cinco condiciones físicas y desconexión separada; 44 informes mensuales; aritmética HH y curvas; días hábiles/feriados y ventanas invasivas; evaluación nativa read-only. Comparar archivos protegidos con estado previo.

## Estado
Exploración y autorización de exceso concluidas. Q1/Q2 implementados documentalmente y con comprobaciones locales; las casillas principales permanecen abiertas hasta los commits; la verificación independiente fue conforme. No se atribuye aprobación de la oferta.

## Evidencia de Q1
Doce filas en Tabla 9.8; cinco condiciones físicas más desconexión separada en T-13. G5 contractual H7/H12 y preparación técnica previa H6/H11; aceptación doce E1/dos E2 más OTIF por tramos y envases diferidos. Calendario efectivo: reservas H1=5, H2=11, H3=16 (recepción22-06), H4=18, H5=34, H8=4, H9=19 y H10=23. El escenario nominal T-15 permanece identificado; no se acredita simulación efectiva. Fuentes legales BCN y solsticios NOAA/USNO citadas en T-17. Ventana invasiva DR E1:26–29-10-2027; preparación/análisis fuera de ella no modifica sitio.

## Evidencia de Q2
T-15:205.135 HH base/componentes +9.336 cobertura puente +3.072 protegidas =217.543. Cambio neto608: DR operacional+480 y restauraciones13–20+128; intrusiónE1+160/E2−160 neto0. Calidad11.136=4.224 prevención+6.912 evaluación. Curva56meses: cada totalHH y totalpersonas conciliado; sumas etapas38.141,17/12.347,17/11.406,54/7.307,91/16.712/128.853,67/2.774,54; máximo69 mes15. Costos/eventos esperados SD8 retirados sin presentar fallas como0HH.

## Comprobaciones observadas
- Python por entrada estándar: sumasHH/rol/fila/etapa y 222 paquetes con componentes; salida0. Doce pruebas y44 informes conciliados.
- Python calendario: límites calculados desde cierre de mes, excluyendo recepción e incluyendo límite; diez días de revisión efectivos dentro del mes; salida0. No implica acta con observaciones ni segunda revisión.
- git diff --check: salida0; advertencias CRLF, sin errores de whitespace.
- gentle-ai review assess --cwd . --json: salida1 high/unassessable por inventario untracked. Reejecución con inventario y selección de esta tarea: salida0 medium/executable_change por AGENTS.md previo;14rutas638líneas globales en ese momento, incluyendo cambios previos. RDD OFF; no se ejecutaron transiciones.

## Pendientes y entrega
Asignación nominal por especialidad, concurrencia diaria, disponibilidad del tercero y recalcular PERT/red efectiva no demostradas: explicitadas como condiciones, no PASS. Confirmar hashes protegidos contra instantánea del coordinador; no se editaron SD8/SD1/SD4 ni Revision. Dos unidades locales autorizadas exception-ok; sin publicación. Revisión independiente y commits pendientes; identificar cambios previos antes de staging. Notificar al responsable SD8 línea base217.543 HH, sin editar su documento.

## Corrección acotada tras verificación independiente
El verificador confirmó aritmética/calendario/contenido salvo un bloqueo: T-15,4.5 conservaba reservas copiadas del SD8 y una garantía de capacidad movilizable. Se sustituyó únicamente esa sección por estimación de contingencias por evento/rol/mes, validación de capacidad nominal y autorización previa. Se retiraron el total238.733,98HH, sus importes derivados y el salto68→89,2. Se califican5.1–5.4 como escenarios históricos nominales no reconciliados con217.543HH/calendario vigente, sin prueba de factibilidad actual. Gobierno usa reserva efectiva T-17. No se editó SD8 ni otros entregables durante esta corrección.

Comprobaciones posteriores: ausencia de importes/garantías antiguas y lectura dirigida conforme; Python56filas/217.543total/205.135base/11.136calidad/44informes salida0; git diff --check salida0, sóloCRLF. Pendiente rechecado independiente y commits; no declarar cierre definitivo antes de ellos.

## Cierre documental y límite de procedencia
El verificador independiente confirmó la corrección acotada; el coordinador confirmó git diff --check. Q1/Q2 tienen implementación y comprobaciones completas, sin atribuir dotación nominal ni PERT efectivo. Los dos commits de unidad permanecen pendientes: no se retuvieron bytes de la instantánea anterior a los cambios propios y el diff de HEAD mezcla importación SD9 previa, hunks del usuario en T-14 y cambios de AGENTS/contexto. Sin procedencia demostrable no se preparó index ni commit; se conservó todo el estado. No es fallo de permisos ni falta de autorización. No se afirman hashes protegidos comprobados ni conteo exclusivo baseline-to-final del escritor. La puerta de cierre por commit sigue sin cumplir; no hubo push, PR, cambio de rama, stash ni reset.
