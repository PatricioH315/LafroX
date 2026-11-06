# Estudio de la documentación del proyecto LafroX

Fecha de revisión: 5 de noviembre de 2026.

## Conclusión

La carpeta contiene principalmente el componente de planificación de la oferta de LafroX para la plataforma logística de Distribuidora Puelche: Subdocumento 7, anexos y formularios T-14, T-15 y T-18. Es una propuesta técnica de ejecución, implantación y operación; no contiene evidencia de que el proyecto ya se haya ejecutado.

La estructura y las cifras centrales son coherentes entre las fuentes revisadas. Reproduje el cálculo CPM existente sin escribir sus resultados sobre los registros anteriores. Sin embargo, la factibilidad integral sigue condicionada por dos asuntos que los propios documentos reconocen: la revisión de las actas previas a producción y la capacidad del equipo de calidad. También queda por confirmar la integración con arquitectura, pruebas, riesgos y aceptación de los otros subdocumentos.

No modifiqué los entregables, las fechas, las estimaciones ni los registros históricos. Este informe y las imágenes de muestra en `tmp/pdfs/estudio-2026-11-05/` son archivos nuevos de esta revisión.

## 1. Mapa documental

| Documento | Páginas actuales | Función |
|---|---:|---|
| LAFROX-Subdocumento7.pdf | 66 | Explica EDT, plan de trabajo, secuencia, hitos e implantación. |
| LAFROX-Subdocumento7-Anexos.pdf | 25 | Detalla calendario, dependencias, resultados, innovaciones, interfaces y supuestos. |
| LAFROX-Formulario-T-14.pdf | 102 | Contiene EDT, diccionario de paquetes y Gantt. |
| LAFROX-Formulario-T-15.pdf | 99 | Contiene estimaciones, HH, recursos, CPM/PERT y programación. |
| LAFROX-Formulario-T-18.pdf | 24 | Define olas, marchas blancas, pruebas, reversión y transferencia. |
| **Total** | **316** | Cinco entregables principales. |

Las fuentes editables son los `.tex` de las carpetas correspondientes y sus tablas. Los `.md` principales se presentan como extracciones de los PDF; sirven para consulta, pero no sustituyen las figuras ni la maquetación. Las imágenes incluyen fuentes draw.io y cartas de GanttProject. La clase `lafrox.cls` y `lafrox-portada.tex` concentran el formato común.

El README explica el uso de la plantilla y las ramas. No debe utilizarse como especificación funcional completa del caso ni como prueba de cumplimiento de las Bases.

## 2. Comprensión del proyecto

La solución busca digitalizar una operación logística que debe seguir vendiendo, preparando y despachando durante la implantación. Abarca recepción, inventario, preparación FEFO, calidad y trazabilidad, temperatura, preventa sin conexión, rutas, reparto, cobros, envases y analítica. Después incorpora canal moderno, portales y costo de servir.

El plan trabaja con doce módulos M1–M12 y quince interfaces. La Etapa 1 incorpora M1–M10 y M12; M10 se amplía en la Etapa 2 con costo de servir, mientras M11 cubre canal moderno. El ERP conserva el papel de registro contable y emisor único de guías. La convivencia exige un escritor autorizado por dato, idempotencia y conciliación, sin doble digitación de los datos compartidos.

Las cantidades del caso que condicionan la implantación incluyen 96 camiones, 62 preventistas, dos centros de distribución y tres plataformas, además de una operación que puede alcanzar unas 2.600 entregas diarias en peak. La cadena de frío agrega banco de pruebas, mapeo por carrocería, compra y contratos, instalación y piloto; no se limita a una función de software.

## 3. Estructura y calendario

La EDT se organiza en nueve fases y 49 cuentas de control. Las fases de Inicio, Elaboración, Construcción y Transición se recorren por etapa; adquisiciones, infraestructura, capacitación, operación y cierre completan el alcance.

| Período | Actividad principal |
|---|---|
| Meses 1–12 | Desarrollo y preparación de la Etapa 1. |
| Meses 13–15 | Marcha blanca E1, en paralelo con desarrollo E2. |
| Mes 16 | Producción E1; aceptación H7 posterior al acta de cierre. |
| Meses 13–18 | Desarrollo y certificación E2. |
| Meses 19–20 | Marcha blanca E2 mientras E1 sigue en producción. |
| Mes 21 | Producción E2 y comienzo de la cobertura contractual de Operación; H12 formaliza aceptación. |
| Meses 21–56 | Operación contractual de ambos alcances durante 36 meses. |

Febrero de 2027 es un supuesto de inicio, no una fecha confirmada. Bajo ese supuesto, producción E1 tiene objetivo 5 de mayo de 2028 y H7, 29 de mayo; producción E2 tiene objetivo 5 de octubre y H12, 25 de octubre de 2028.

Los congelamientos y las ventanas de despacho condicionan las activaciones. Los documentos distinguen el congelamiento del 1 al 25 de septiembre, todo diciembre y los tres primeros días hábiles mensuales de la prohibición de paso a producción en septiembre y diciembre. También identifican una política adicional de arquitectura que excluye despliegues durante todo septiembre.

## 4. Comprobaciones realizadas

Recalculé directamente desde las tablas fuente:

- 227 paquetes en el diccionario T-14 y en la estimación T-15, con los mismos códigos.
- 168 paquetes con fechas y 59 de esfuerzo continuo.
- 207.487 HH de paquetes.
- 220.023 HH en las 56 filas mensuales; todas las sumas de filas de horas y personas cuadran.
- Máximo mensual conjunto de 64 personas equivalentes, únicamente en el mes 16.
- Coincidencia de los hashes de las cuatro fuentes numéricas con la captura K4.

La composición del esfuerzo evita duplicar componentes:

**207.487 + 128 de restauraciones previas + 9.336 de soporte puente + 3.072 de reserva protegida = 220.023 HH.**

Ejecuté en memoria el modelo `revision/recalcular_cpm_20261025.py`, deteniéndolo antes de la escritura de archivos. Los 168 paquetes calculados coinciden con sus fechas publicadas y el modelo no registra violaciones de sus precedencias. Las holguras reproducidas son H1: 5; H2: 11; H3: 17; H4: 16; H5: 20; H7: 2; H8: 14; H9: 19; H10: 13; H12: 3 días hábiles. H6 y H11 son inicios fijos.

Esto reproduce el modelo existente, no valida independientemente cada hipótesis de productividad ni demuestra disponibilidad nominal. Las probabilidades PERT publicadas son condicionales al camino y sus supuestos; no representan una probabilidad integral de éxito del proyecto.

Leí el texto de los cinco PDF y comprobé su número de páginas. No aparecieron marcadores literales `??` en el texto extraído. Rendericé e inspeccioné una muestra de ocho páginas, incluidas la secuencia de actas, capacidad CAL, resumen de recursos, EDT y pruebas DR. La muestra no mostró recortes evidentes; no constituye una nueva auditoría visual exhaustiva de las 316 páginas. No recompilé LaTeX ni certifiqué la sincronización exacta de todos los Markdown.

## 5. Hallazgos prioritarios

### A. El cierre previo a producción no tiene encajado el plazo completo de revisión

El T-15, sección 5.5 y tabla de secuencia de actas en la página 58 del PDF, distingue correctamente dos actos: cierre de marcha blanca previo a producción y aceptación H7/H12 posterior.

Con el calendario interno del modelo, reproduje estos resultados:

| Etapa | Evidencia final | Entrega completa supuesta | Revisión de diez días hábiles | Producción objetivo |
|---|---|---|---|---|
| E1 | 3–30 abril 2028 | 2 mayo | 3–16 mayo | 5 mayo |
| E2 | 3–30 septiembre 2028 | 2 octubre | 3–17 octubre | 5 octubre |

Sólo hay dos días de revisión anteriores a producción en ambos casos. La holgura positiva de H7/H12 no resuelve esa condición previa. Hace falta confirmar el procedimiento aplicable con la Contraparte Técnica; si requiere el plazo completo, deberán evaluarse alternativas de programación. No corresponde presentar estas fechas como aprobadas ni asumir evidencia futura.

### B. Diez personas CAL no cubren las ventanas de certificación publicadas

Recalculé la condición necesaria de capacidad entre el 25 de octubre y el 11 de noviembre de 2027 para 3.8.2–3.8.5:

- Trabajo mínimo dentro del intervalo: 204,80 + 204,80 + 320 + 320 = 1.049,60 HH.
- Capacidad de diez personas en trece días hábiles a 6,4 HH efectivas: 832 HH.
- Brecha: **217,60 HH**.
- Se necesitan al menos **13 personas CAL en algún momento**, manteniendo las ventanas y máximos del modelo.

Es una cota inferior: no demuestra suficiencia de trece ni incluye todos los servicios continuos. El T-15 ya reconoce esta brecha en su sección 5.7, página 62 del PDF. Se debe resolver mediante asignación/refuerzo o nivelación compatible con los hitos, sin confundir el promedio mensual con concurrencia diaria.

### C. La integración con otros subdocumentos sigue abierta

La reconciliación K6 identifica pendientes de referencias/arquitectura (K1), pruebas (K3) y riesgos/reservas (K5). Se deben confirmar especialmente el protocolo T-17, el traspaso de supuestos P7 al SD8, las reservas aprobadas, turnos SOC y apoyos SRE/SEG en pruebas.

En esta revisión no inspeccioné las versiones actuales completas de las otras ramas ni las Bases originales. Las afirmaciones sobre esos documentos son dependencias declaradas por el material local, no un nuevo dictamen de cumplimiento contractual. El informe del 25 de octubre tiene valor histórico, pero sus hallazgos no deben trasladarse como pendientes actuales sin volver a contrastarlos.

### D. La evidencia de validación de PDF requiere actualización

Los cinco PDF conservan los números de páginas registrados en `K6_QA_PDF.json`, pero **ninguno coincide con su SHA-256 almacenado**. En cambio, las cuatro fuentes numéricas sí coinciden con K4.

Esto demuestra que el registro no identifica exactamente los binarios actuales. No demuestra por sí solo un cambio sustantivo ni un defecto visual: una recompilación también cambia bytes. Conviene actualizar la evidencia de QA para la entrega definitiva después de contrastar las fuentes, registrar el entorno y revisar los binarios finales.

### E. `main.pdf` es una salida anterior

El `main.tex` actual remite a `LAFROX-Subdocumento7.tex`, pero `main.pdf` tiene cinco páginas, frente a las 66 del entregable principal. Por tanto, el PDF auxiliar no representa la salida actual esperada de esa entrada. Debe identificarse como antiguo o regenerarse en la próxima compilación para evitar confusiones.

### F. Metadatos y revisión humana deben reconciliarse al cierre

Los envoltorios conservan fecha de emisión de 12 de octubre de 2026 y versión 1.0, pese a revisiones posteriores. El registro K6 explica que esa ficha se mantuvo a la espera de coordinación; no la cambié. La depuración editorial también deja pendiente contrastar la declaración de IA con sus responsables antes de consolidar A-6. No debe atribuirse una revisión humana nueva por el solo hecho de esta revisión automatizada.

## 6. Fortalezas y orden de trabajo sugerido

El conjunto ofrece buena trazabilidad entre alcance, paquetes, módulos, interfaces, pruebas y resultados de aceptación. Son especialmente útiles la separación entre soporte puente y operación, la reserva E1 protegida, las condiciones de evidencia de 28 días, la distinción entre reversión técnica y operacional, y la separación de restauración de respaldo y conmutación DR real.

El siguiente trabajo debería resolver, en este orden:

1. Procedimiento de actas previo a producción y coherencia con T-17.
2. Capacidad CAL y asignación nominal de equipos y turnos.
3. Cruces con las versiones vigentes de arquitectura, pruebas y riesgos/reservas.
4. Consolidación de metadatos y declaración de revisión humana.
5. Compilación final y actualización de hashes y evidencia visual para los PDF exactos de entrega.

## Fuentes locales principales

- Los cinco PDF y sus fuentes `.tex`, incluidos diccionarios y tablas de estimación, programación y recursos.
- `README.md`.
- `revision/REVISION_SD7_2026-10-25.md` e `IMPLEMENTACION_CADENA_FRIO_2026-10-25.md`, como antecedentes históricos.
- `revision/frente-b/K4_BASE_PROGRAMACION.md`, `K4_MANIFIESTO.json` y tablas de captura.
- `revision/frente-b/K6_RECONCILIACION.md`, `K6_VERIFICACION.json`, `K6_INTERVALOS_CAPACIDAD.csv`.
- `revision/frente-b/VALIDACION_FINAL.md`, `K6_QA_PDF.json` y `DEPURACION_EDITORIAL.md`.
- `revision/recalcular_cpm_20261025.py` y lógica de capacidad de `revision/frente-b/verificar_frente_b.py`.
