# Frente C: cambios aplicados y entrega K3

**Se aplicó el trabajo respaldado de SD6/SD9. El frente no se declara cerrado:** faltan la ratificación de C03, los contratos finales K2/K5/K6 y la revisión humana de esta actualización. No se crearon capítulos excluidos ni se editaron documentos de otros frentes. Cambios guardados en commits locales por autorización del usuario; sin push. La revisión general se realizará cuando terminen los demás frentes.

## Versiones y aislamiento

| Documento | Rama / versión consultada | Trabajo del frente C |
|---|---|---|
| SD6 | `LafroX-Subdoc6-LateX`, `f20ed720` | Copia gestionada separada, rama `codex/frente-c-sd6`, commit `9b650ede`; original de Claude intacto |
| SD9 | `LafroX-Subdoc9-LateX`, `91a5f7e6` | Checkout existente, sin cambiar de rama |
| SD1 | `0938754e` | Solo lectura: gobierno y dotación |
| SD3 | `8f366246`; matriz heredada desde `33508bb3` | Solo lectura; no se recibió K2 final |
| SD4 | `b0606ac9` | Solo lectura: obra civil, DTE y recuperación |
| SD7 | `93a5e884` | Solo lectura: sala técnica, campañas e hitos; no es recepción de K6 final |

Rutas de trabajo:

- SD6: `C:/Users/henri/.codex/worktrees/frente-c-sd6/LafroX`.
- SD9: `C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva`.
- Fuente del reparto leído: `C:/Users/henri/Downloads/plan/PLAN_PARALELO_LAFROX_2026-10-27.md`.
- Se preservaron los planes no seguidos y los auxiliares que ya estaban modificados en SD9. Las compilaciones nuevas usan `revision/frente-c-build/`, no los PDF antiguos de la raíz.

## Estado por ficha

| Ficha / IDs fuente | Estado y evidencia | Lo que falta |
|---|---|---|
| C01 · 2.2–2.3 | C6 ya aplicado en K0; tabla explicita contratación SOC **antes** del mes 13. Obra civil de separación: CLIENTE; especificación/coordinación, piso y equipos: LafroX. Instalación mes 3 y recepción de sala mes 4, conforme a T-14 6.1.1 y T-15 | Confirmación de B sobre K4/K6 final; no se certifica contratación o recepción efectiva |
| C02 · 2.4 | Aplicado por delegación del usuario. SD6 6.1.3 y T-9 documentan el refuerzo; SD9/T-13 lo consumen sin suponer disponibilidad | B debe nivelar días y concurrencia; proveedor y asignación nominal se acreditarán antes de las sesiones |
| C03 · 2.5–2.6 | C7 conserva las tres coberturas independientes. Definición medible preparada en `PROPUESTA_METRICAS_K3_2026-10-27.md` | Usuario pidió **preparar**, no ratificó. No se añadió una política no aprobada a T-10; sigue abierto el respaldo de duplicación/acoplamiento |
| C04 · 4.4 | Alineados SD6 6.1.6/T-9 y SD9 con gobierno **ya existente** en SD1 1.2/1.3.1: comité interno, presidencia QA y líderes, mensual, escalamiento a Gerencia; no se atribuye al Art. 71 ni acepta por el CLIENTE | E debe confirmar vigencia si modifica SD1; no se creó un nuevo órgano o poder |
| C05 · 4.5, C8 | Hallazgo antiguo parcialmente resuelto antes de esta intervención: T-13 9.1 ya tiene 3.8.5 antes de H5 y 3.9.4 antes de H10. Añadido 7.6: prerrequisitos, alcance real, RTO/RPO, bitácoras, salida y repetición. Mes 21 aclarado como primera conmutación **periódica de Operación**, no primera prueba del proyecto | K6 final y conciliación de periodicidad/ventanas con B; riesgo residual con A. No se inventaron pruebas ejecutadas |
| C06 · 2.9, 4.11 | C9 de K0 conservado y completado con ventana 05:30–07:00 en T-10. RV-012/018/020 revalidados abajo. T-13 agrega escenario de carga modificada/ERP indisponible sin autorizar emisión alternativa | Dotación con E/B; solución y riesgo DTE con E/A/B; reservas con A/B |
| C07 · 2.11–2.12 | Matriz heredada verificada sin regenerarla: 653 filas, 644 requisitos, 9 alias, 15 contratos, 1.352 casos previstos. Remisiones actuales SD3→T-13 8.2 y SD4→T-13 4.1 sí corresponden al contenido; no repetir correcciones del plan antiguo. T-17 localizado en esta copia SD9 | Recibir K2 y regenerar con su SHA; K6 para aceptación. No hay K2 final acreditado por un test del snapshot antiguo |
| C08 · 3.1/3.3/3.9/3.14 | SD6: capítulo «Metodologías»; Referencias y Declaración sin número, introducidas; cita Kruchten enlazada a la entrada existente; frases truncas de T-9 completas; numeración de T-9 desde sección 1 y secciones T-10 sin el prefijo incorrecto 1.0.x; adquisiciones numeradas 6.B.1, con remisión corregida. SD9: cita huérfana 2026c reemplazada y página 15 contrastada en el PDF del Caso | Revisión humana editorial de los cambios; compilación no acredita por sí sola toda la semántica de citas textuales |
| C09 · 1.7/3.11/3.16 | Fuentes genéricas de SD6 sustituidas. Figura 6.1 nativa, con llamada, explicación y declaración veraz. Auditadas las 14 tablas técnicas del cuerpo de SD9; prosa de fases retirada de celdas y conservada antes de las tablas. Las declaraciones IA conservan seis columnas exigidas por Aclaraciones 7.2, no se les aplica mecánicamente el máximo orientativo de cinco de §5 | Revisión humana de la nueva figura y contenido. El detector de frases es heurístico, no certificado automático de cumplimiento |

## K3 para B/E y coordinación

### Evaluadores

- **Modalidad:** subcontratación de refuerzo bajo CAL; no confundir con SOC propio.
- **Techo:** hasta 16 externos por día, adicionales a la plantilla corporativa, sin sumar automáticamente sus diez especialistas como disponibilidad de este contrato.
- **Períodos de planificación:** meses 9–12 y 16–18, solo días de sesiones efectivas; no disponibilidad continua contratada.
- **Hipótesis de jornada:** 8 h nominales de planificación, 80 % programable = 6,4 HH netas/persona-día; máximo diario externo 102,4 HH. No es una jornada laboral contractual.
- **Días y capacidad:** para cada sesión, registrar fecha, personas, rol, paquete, horas, indisponibilidades y otras asignaciones. La capacidad neta es la suma de horas realmente asignables, no `16 × todos los días del período`.
- **Control:** JP confirma proveedor, competencias, confidencialidad y contratación/asignación antes de reservar; CAL comprueba suficiencia. No se autoriza una sesión sin respaldo.
- **Cálculo reproducible:** 270 casos manuales × 15/60 = 67,5 HH; `ceil(67,5/6,4)=11` evaluadores-día antes de coordinación/incidencias. Con 16 simultáneos se requieren 17 tandas de 15 min = 4,25 h mínimas. HH y tiempo transcurrido no son intercambiables.
- **Autoridad:** usuario delegó la elección contextual en este chat el 27-10-2026. La delegación no acredita contratos firmados ni un calendario nivelado.

### Métricas y gobierno

- Coberturas C7: ≥70 % lógica de negocio; ≥80 % global; ≥80 % código modificado. Deben cumplirse conjuntamente.
- Duplicación/acoplamiento: límites heredados de SD9, definición propuesta aparte; ratificación y calibración pendientes. No se asegura que ESLint genérico mida acoplamiento eferente.
- Comité interno: fuente SD1 1.2/1.3.1 (`0938754e`), Jefe de QA y líderes de proyecto, mensual; observaciones y desacuerdos a Gerencia. No dispensa umbrales ni reemplaza aceptación del CLIENTE. Explicitado en SD6/T-9 y SD9.

### DR y aceptación

- T-13 7.6 fija el protocolo; 9.1 conserva las campañas 3.8.5 y 3.9.4 del snapshot de B, antes de H5/H10.
- Contrastar K6 con estas ventanas: E1 25-10 a 11-11-2027, intervención 26–29 de octubre; E2 19-05 a 01-06-2028. Preparación/informe no equivale a intervención. Revisar además intervalos entre campañas, inicio de servicio y periodicidad semestral; no inferirla solo de los meses de Operación.
- Certificación, cierre de marcha blanca y aceptación H7/H12 son distintos; corregida una frase residual del Anexo 9.B que los confundía.
- A recibe: riesgo de repetición por falla de DR, consumo por rol y afectación del expediente; no se imputa una reserva sin K5.

## RV-012 / RV-018 / RV-020: entrega a sus dueños

| Hallazgo vigente | Evidencia consultada | Acción del dueño |
|---|---|---|
| Dotación corporativa no equivale a disponibilidad de proyecto | SD1 `contenido.tex`: 48 desarrollo, 12 SRE; SD7 T-15 distingue curva de demanda y asignación nominal. En las fuentes TeX vigentes de SD6 no aparece un compromiso propio de 40 desarrolladores que deba reemplazarse a ciegas | E/B: matriz de personas/competencias/dedicaciones y concurrencias. No se inventó contratación ni se confundió plantilla con asignación |
| La guía preemitida no cubre una carga modificada; con ERP perdido una guía nueva espera su restitución | SD4 `04/partes/4.1_logica/04_capas_de_la_arquitectura.tex`, integración tributaria; `04/partes/4.3_centros_de_datos/06_e_sitio_secundario.tex`, recuperación de Talca | E/A/B: demostrar continuidad de 96 salidas y procedimiento conforme. C prueba bloqueo, idempotencia y recuperación; **no** ofrece otro emisor ni presenta bloqueo correcto como continuidad acreditada |
| No hay una bolsa de gestión de 1.600 HH disponible acreditada en las fuentes vigentes de SD6 | SD6/T-9 controlan reservas por separado; 1.600 HH en SD9 corresponde a evaluación E2, no a reserva. SD7 distingue reserva protegida y HH de paquetes | A/B: K5/K6 con naturaleza, monto, autorización, roles y consumo; no sumar escenarios, evaluación y reserva como capacidad adicional |

## Destinos que pueden consumir D/E

- T-13 **4.1**, «Instancias de Preproducción por campaña»: respalda la remisión actual de SD4 sobre instancias simultáneas.
- T-13 **8.2**, «Tamaño estimado del catálogo»: contiene dimensionamiento y matriz individual generada; respalda la remisión actual SD3. No redirigir a 4.1 para hablar de trazabilidad.
- SD9 **9.2.5**, trazabilidad; T-13 **7.5**, protocolos híbridos; nuevo **7.6**, DR; T-17 **3.1**, expediente y **4**, criterios de hitos.
- `git ls-tree -r --name-only 93a5e884` no identifica un T-17 separado en la versión SD7 consultada. Si B incorpora otro, debe acordarse cuál se entrega antes de integrar.

## Verificación y entrega técnica

Ejecutar desde la raíz del checkout SD9:

```powershell
python SD9_v_nueva/revision/verificar_matriz_pruebas.py
python SD9_v_nueva/revision/verificar_alineacion_sd7.py 93a5e884
python SD9_v_nueva/revision/verificar_frente_c.py --sd6 'C:/Users/henri/.codex/worktrees/frente-c-sd6/LafroX' --output SD9_v_nueva/revision/AUDITORIA_TABLAS_FRENTE_C_2026-10-27.json
```

- El verificador de alineación dejó de rechazar las secciones 4/5/6 válidas tras C15; ahora detecta el prefijo antiguo 7.4/7.5/7.6. Se eliminaron exigencias textuales de revisión humana histórica: un test no puede exigir afirmar una revisión no realizada.
- `latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=revision/frente-c-build DOCUMENTO.tex`, desde cada raíz documental, para cuerpo/anexos/T-9/T-10 y cuerpo/anexos/T-13/T-17.
- Los resultados finales, hashes y advertencias se registran en `VERIFICACION_PDF_FRENTE_C_2026-10-27.json`. La revisión visual es por muestreo; no reemplaza revisión humana integral de los PDF.
- N/A: pruebas de aplicación o runtime de negocio; los cambios son fuentes LaTeX, documentación y verificadores documentales.
- SD6 se entrega además como `SD6_FRENTE_C_2026-10-27.patch`, limitado a siete fuentes. Aplicar solo sobre la versión correspondiente y después de comprobar el estado local; no se ejecutó su aplicación en la rama original.
- Límite de reversión: siete fuentes del patch SD6 y fuentes/verificadores/informes de esta actualización en SD9; no incluye canon, clase, portadas, fuentes de otros frentes ni los auxiliares preexistentes. No usar `reset/clean` global para revertir.

## Para cerrar el frente

1. Ratificar la definición C03 y calibrar sus herramientas antes de propagar a T-10.
2. Recibir K2 final de D y regenerar/verificar la matriz con ese commit.
3. Recibir K5/K6 de A/B, nivelar refuerzo y cerrar periodicidad, ventanas y aceptación.
4. Confirmar con E dotación, gobierno vigente y tratamiento del escenario DTE.
5. Revisar humanamente los cambios y actualizar su declaración con nombres/evidencia reales; luego integrar las fuentes y PDF autorizados.

## PDF verificados de esta copia de revisión

8/8 compilaciones con salida 0; cero referencias/citas indefinidas, etiquetas duplicadas, errores LaTeX y cajas overfull en sus logs finales. Se inspeccionó visualmente una página representativa de cada PDF. Esto no acredita revisión humana del equipo ni ejecución de pruebas del sistema.

- [LAFROX-Formulario-T-10](C:/Users/henri/.codex/worktrees/frente-c-sd6/LafroX/revision/frente-c-build/LAFROX-Formulario-T-10.pdf) — 5 páginas.
- [LAFROX-Formulario-T-9](C:/Users/henri/.codex/worktrees/frente-c-sd6/LafroX/revision/frente-c-build/LAFROX-Formulario-T-9.pdf) — 9 páginas.
- [LAFROX-Subdocumento6-Anexos](C:/Users/henri/.codex/worktrees/frente-c-sd6/LafroX/revision/frente-c-build/LAFROX-Subdocumento6-Anexos.pdf) — 8 páginas.
- [LAFROX-Subdocumento6](C:/Users/henri/.codex/worktrees/frente-c-sd6/LafroX/revision/frente-c-build/LAFROX-Subdocumento6.pdf) — 13 páginas.
- [LAFROX-Formulario-T-13](C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/revision/frente-c-build/LAFROX-Formulario-T-13.pdf) — 76 páginas.
- [LAFROX-Formulario-T-17](C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/revision/frente-c-build/LAFROX-Formulario-T-17.pdf) — 16 páginas.
- [LAFROX-Subdocumento9-Anexos](C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/revision/frente-c-build/LAFROX-Subdocumento9-Anexos.pdf) — 20 páginas.
- [LAFROX-Subdocumento9](C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX/SD9_v_nueva/revision/frente-c-build/LAFROX-Subdocumento9.pdf) — 34 páginas.

## Commits locales de esta entrega

- SD6: `9b650edebe0c5a139462df4c41fbf84f048cdcd4`, rama `codex/frente-c-sd6`.
- SD9, fuentes y verificadores: `db5c59cf01d5a6804286842c40de0e76e93d05b9`, rama `LafroX-Subdoc9-LateX`.
- El registro de entrega y sus evidencias se guarda en un commit documental posterior, identificable en el historial de SD9.
- Se excluyen PDF de compilación, logs, auxiliares y planes preexistentes ajenos a estos cambios.
- Por indicación del usuario, los pendientes se retomarán en la revisión general cuando los demás frentes estén listos. No se presentan como resueltos.
