# Revisión integral LafroX — incoherencias y línea de trabajo priorizada

## Contexto

El equipo pierde tiempo corrigiendo incoherencias sueltas entre subdocumentos que viven en ramas separadas. Se auditaron las ramas vigentes al 27-10-2026 contra `aclaraciones-licitacion.md`, `Bases Administrativas.md`, `Bases_Tecnicas_Transversales.md` y `Caso_02_Logistica.md` (carpeta `Downloads\Bases MarkDown`). Objetivo: un listado único, ordenado de mayor a menor gravedad, donde cada arreglo indique qué subdocumentos toca, para que las correcciones se hagan una sola vez y no se reabran.

Próxima entrega: **Propuesta Final, 25-11-2026** (todos los capítulos 1–14). Desde el Informe 2, un indicio de la Aclaración 7.1(d) o un archivo mal nominado deja el subdocumento completo en 0.

### Ramas vigentes (fuente de verdad)

| SD | Rama vigente | Observación |
|---|---|---|
| 1 | `origin/LafroX-Subdoc1-LateX` | |
| 2 | `origin/LafroX-Subdoc2-LateX` | |
| 3 | `origin/LafroX-Subdoc3-LateX` | |
| 4 | `origin/subdoc-4` | `Guillermo-subdoc4-consistencia` ya integrada; `LafroX-Subdoc4-LateX` vacía |
| 5 | `origin/LafroX-Subdoc5-LateX` | |
| 6 | `origin/LafroX-Subdoc6-LateX` | |
| 7 | `origin/LafroX-Subdoc7-LateX` | local va 1 commit atrás; `Lafrox-Subdoc7-Latex-Tomas` ya integrada |
| 8 | `origin/Lafrox_Subdocumento_8_Latex_Nuevo` | **duplicada** con `LafroX-Subdoc8-LateX` (obsoleta, pero tiene FMEA) |
| 9 | `LafroX-Subdoc9-LateX` | checkout actual |
| 10, 11, 12, 14 | — | **no existen** (ramas 10–12 sólo con README; 14 sin rama) |
| 13 | `origin/LafroX-Subdoc13-LateX` | |

---

## Ola 0 — Congelar el canon (antes de tocar cualquier documento)

Sin esto, cada arreglo vuelve a abrirse. Es una tabla de decisiones de una página que todos copian tal cual.

| # | Decisión a fijar | Valores en conflicto hoy | Propuesta | SD afectados |
|---|---|---|---|---|
| C1 | Prefijo de archivos | `LAFROX-`, `LafroX-`, `Lafrox-`, `LafroX-Subdocumento-8-` | `LAFROX-SubdocumentoN`, `LAFROX-SubdocumentoN-Anexos`, `LAFROX-Formulario-T-X` | 7, 8 (y 4 al compilar sin jobname) |
| C2 | Esquema de IDs de riesgo | SD13 cita `R8-23…R8-29` y `O8-01` (48 citas); SD8 vigente usa `R-001…R-033` y no tiene riesgos de innovación | Un solo esquema (sugerido `R8-xx`, que ya usan SD13 y la rama vieja) | 8, 13, 7 (T-15 reservas) |
| C3 | Fecha mes 1 del contrato | SD3: «dic-2026 a mar-2027»; SD7/SD9/SD4: feb-2027 | feb-2027 | 3 |
| C4 | Fecha del H12 | objetivo 05-10-2028 vs acta calculada 25-10-2028 (SD7 dice «requiere reprogramar») | Reprogramar y dejar una sola fecha | 7 (T-15, T-17), 9, 13 |
| C5 | Dotación de terreno | Preparadores: SD7 «120» vs SD2/T-18 «120 + hasta 60». Conductores: SD7 «cerca de 200» vs SD2 ≈244 | 120 + 60; 84 + ≈160 = ≈244 | 7 |
| C6 | SOC | SD6: «condicional a subcontratación», RT-11.17 parcial; T-15: SOC propio en Valparaíso desde el mes 13 | Una sola postura | 6, 7, 1, 12 (nuevo) |
| C7 | Coberturas de prueba | SD1/SD3: lógica ≥70 % y global ≥80 %; T-10: 80 % código modificado; SD6: «80 % global»; SD9: las tres | Las tres métricas en todos | 1, 3, 6 (T-10), 7 (T-14 1.5.2), 9 |
| C8 | RPO ante pérdida del sitio | SD7/T-18: «se cumple»; SD8: «no demostrado» | Una sola afirmación, con evidencia | 4, 7, 8 |
| C9 | Ventana de congelamiento | T-10: todo septiembre; SD7/T-18/SD5: 1–25 sept. | Una | 5, 6, 7 |
| C10 | Terminología de componentes | M12 «Telemetría» (SD3/SD4) vs «posición de flota» (T-14); «Redis» (SD5) vs «ElastiCache Valkey 8.1» (SD4); B-08 «registrador» vs «sensor»; «M» = mes y módulo (SD5) | Nombres de SD4/T-11 como canon; meses como «mes N» | 5, 7, 13 |
| C11 | Responsables | SD8/T-16 usa 13 roles inventados; SD1/SD7 usan 8 roles | Los 8 roles del SD1 | 8 |
| C12 | Títulos oficiales de subdocumentos y formularios en Referencias | «Modelo de datos», «Problema y necesidad», «Inventario de hardware y software», «Fichas de innovación» | Títulos exactos de las Bases (ej. SD5 «Modelo y gestión de datos», T-11 «Especificaciones técnicas ofertadas», T-19 «Cartera de innovaciones») | 2, 4, 5, 13 |
| C13 | Claves APA de documentos propios | «LafroX 2026a/b/c» significa cosas distintas en cada SD; autor «LafroX» vs «LafroX SpA.»; misma fuente del caso con 3 títulos | Tabla fija clave → documento, compartida | todos |
| C14 | Declaración de IA | «No aplica» (SD1, SD3); «Alto» en todas las filas (SD4, SD5); SD8: «riesgos generados por ia», «contenido academico» | «Ninguno» cuando no hubo uso; niveles reales por sección | 1, 2, 3, 4, 5, 8 |
| C15 | Numeración de secciones de formularios | SD3 cita «T-18 §6.4» y «T-13 §8.2»; SD7 cita T-15 como «sección 5/6» y SD9 como «§7.5.7» | Un solo estilo de cita | 3, 7, 9 |

---

## Ola 1 — Gravedad crítica: puntaje 0 o «no presentado»

| # | Problema | Evidencia | Arreglo | SD afectados |
|---|---|---|---|---|
| 1.1 | **Faltan los Capítulos 10, 11, 12 y 14** y el Formulario **T-8** (22 % de la ponderación final). Además SD1, SD3 y SD7 ya remiten al Cap. 12 / 12.3 | aclaraciones §11; T-21 | Crear las ramas desde `rama-formato-Latex-base` y redactar con los índices obligatorios. Depende de la Ola 0 (C6, C8, C11) y de los datos de SD1 (dotación, alianzas), SD4 (SLA, observabilidad), SD7 (curva de dotación T-15), SD9 (pruebas DR) | 10, 11, 12, 14 (nuevos); 1, 7 (verificar remisiones) |
| 1.2 | **SD8 con indicios 7.1(d)**: «versión previa», «supuesto heredado», «se deben vincular», «pendientes de estimación», «solapamiento en 70 %, que se conserva», declaración de IA | SD8n `contenido.tex:79, 117, 171, 183-190` | Reescribir esos pasajes como contenido final | 8 |
| 1.3 | **SD7 reconoce pendientes en el texto**: «requiere reprogramar» (H12), «La carta no demuestra por sí sola…»; archivos huérfanos `tab_T15_contingencia.tex` («pendiente de conciliación») y `tab_T15_11` | SD7 `contenido.tex:350, 429` | Resolver C4 y eliminar los huérfanos | 7, 9, 13 |
| 1.4 | **Nombres de archivo mal formados** (Art. 40.4: no presentado) | SD7 `LafroX-…`; SD8 `LafroX-Subdocumento-8-Anexos`, `Lafrox-Formulario-T-16`, portada T-16 «Lafrox-Subdocumento-T-16.pdf» | Aplicar C1 | 7, 8 |
| 1.5 | **SD5 con Referencias rotas**: entradas sin autor ni año, citas borradas en el texto («las Bases Técnicas del Caso  y …»), citas sin entrada (Puelche 2026d, LafroX SpA 2026a) | SD5 `partes/referencias_ia.tex:5-17`, `contenido.tex:24`, `5_1_modelo.tex:170, 205` | Reconstruir la lista (recuperar de antes del commit 2f936555) y las citas | 5 |
| 1.6 | **SD13 cita 48 veces riesgos que no existen** (`R8-23…R8-29`, Anexo 8.F `O8-01`), y SD8 no tiene riesgos de adopción de innovaciones | `git grep R8-` en SD13 vs SD8n | Aplicar C2: agregar a SD8 los riesgos de adopción de INN-01…05 con la P×I que declara SD13, o renumerar SD13 | 8, 13 |

---

## Ola 2 — Gravedad alta: contradicciones y remisiones rotas entre subdocumentos

Ejecutar en el orden indicado: primero el documento «dueño» del dato, después los que lo citan.

| # | Incoherencia | Dueño → corregir en |
|---|---|---|
| 2.1 | Supuestos P7-01…P7-11: el Anexo 7.F dice que el Cap. 8 los evalúa; SD8 no menciona ningún P7. Reservas: T-15 y SD8 se remiten la conciliación mutuamente y nadie la hace | SD8 (evaluar P7 y conciliar reservas) → SD7 (T-15 refleja reservas en el cronograma) |
| 2.2 | SOC (C6) | SD6 `tablas/adquisiciones.tex:19`, `contenido.tex:37` ↔ T-15 `contenido.tex:98` |
| 2.3 | Sala técnica: SD6 dice obra civil meses 5–6 a cargo de LafroX; T-14 6.1.1 dice a cargo del CLIENTE (RT-06.06) e instalación en el mes 3 | T-14 (dueño) → SD6 `adquisiciones.tex:8` |
| 2.4 | «Hasta 16 evaluadores subcontratados por día» atribuido a SD6 §6.1.3, que no lo dice | SD6 (agregar o no) → T-15 `tab_T15_8`, SD9 `:291, 303, 324` |
| 2.5 | Umbrales «duplicación ≤3 %» y «acoplamiento ≤20» atribuidos al T-10, que no los declara | T-10 (agregar) → SD9 `:104-105`, Anexo 9.A `:123` |
| 2.6 | Coberturas (C7) | T-10 `:54`, SD6 `:66`, T-14 1.5.2 |
| 2.7 | RPO (C8) | SD4 → SD7 `:562`, T-18 `:237`, SD8 `:200` |
| 2.8 | Preparadores y conductores (C5) | SD2 → SD7 `:308, 506` |
| 2.9 | Congelamiento (C9) | T-10 `:60` ↔ SD7 `:514`, T-18 `:41` |
| 2.10 | Reversión técnica: SD7 `tab_SD7_7` la asigna al SRE; SD4 la declara automática | SD4 → SD7 |
| 2.11 | Remisiones mal apuntadas: T-11 `:115` cita 4.1.3.5 para M9 (es Integración); SD5 §5.1.7 cita «SD4 4.1.4.8» (M9 está en 4.1.4.2); SD3 cita «T-18 §6.4» y «T-13 §8.2»; SD4 `11_j:63` cita «T-13 §4.1» | Verificar cada destino y corregir |
| 2.12 | Remisiones no verificadas aún: SD7/SD8 → SD4 §4.1.4.4, 4.2.4.1.2, 4.3.2.4, Anexo 4-W.7; SD3 §3.4.3–3.4.5, Anexo 3.I; SD13 «transferencia desde el mes 22»; TRZ → SD4 4.1.1, 4.3.2.4, 4.2.6, 4.1.3.5 | Verificar en la Ola 5 con el script de remisiones |
| 2.13 | Terminología (C10) | SD5, T-14, SD13 |
| 2.14 | Responsables del T-16 (C11) | SD8 |
| 2.15 | Retención por lote vs por SSCC | SD3 l.12, 153, RNG-04 vs SD2 S-04, SD3 l.120, 295 |
| 2.16 | Fecha de inicio (C3) | SD3 l.59 |

---

## Ola 3 — Gravedad media: incumplimiento formal del índice y de la redacción (ítem Transversal + ítem del SD)

| # | Problema | SD |
|---|---|---|
| 3.1 | Título de capítulo distinto al obligatorio: «Introducción a las metodologías» (debe ir «Metodologías») | 6 |
| 3.2 | Título de capítulo «Introducción de riesgos» (debe ser «Introducción a los Riesgos») | 8 |
| 3.3 | Referencias y Declaración de IA numeradas como 6.3 y 6.4 (deben ir sin número); «Referencias» seguido de lista | 6 |
| 3.4 | Diez `\paragraph*` seguidos de `itemize` sin frase de entrada; «La tabla distingue…» sobre una lista | 4 (`02_b:25, 46`; `02_a:263`; `11_j:225, 376, 459`; `12_k:72, 163, 243, 291`; `06_e:38, 80`) |
| 3.5 | Tablas consecutivas sin texto (2.A.1 → 2.A.2) | 2 `anexos.tex:30-33` |
| 3.6 | Títulos 3.3.2 y 3.3.3 dentro de `minipage`; párrafos de cadena de frío pegados antes de la introducción de 3.1.1, 3.4.1, 3.4.5, 3.4.6 | 3 |
| 3.7 | Mezcla de problema y solución en el Cap. 2 («Decisión que requiere la necesidad», «Decisión del proponente») | 2 `contenido.tex:66-67`, `anexos.tex:163` |
| 3.8 | RBS en página A3 (Bases exigen carta u oficio); numeración de tablas forzada a mano y duplicada («8.4») | 8 |
| 3.9 | Citas sin entrada / entradas sin cita: SD1 «2026c», T-6 «2026d», SD3 «Ministerio de Salud, 1996», SD6 Kruchten, SD8 «2026c», «2026-a», SD13 «LafroX, 2026» sin letra; estilos mezclados en SD3 | 1, 3, 6, 8, 13 (tras C13) |
| 3.10 | Declaración de IA (C14) + tabla sin texto de cierre en SD1; niveles «Medio» en diagramas para secciones sin figuras en SD2 | 1, 2, 3, 4, 5, 8 |
| 3.11 | Figuras: SD6 no tiene ninguna; SD7 con 17 láminas EDT sin `\ref` previo y lámina que «amplía» la 3.10 (§4) | 6, 7 |
| 3.12 | T-6 con campos renombrados («Experiencia del Proponente», «Período de implementación / operación»); T-15 `tab_T15_3` sin la columna «N° de personas (peak)»; T-19 titulado «Fichas de innovación»; tipo 5 sin «sostenibilidad» en Tabla 13.1 | 1, 7, 13 |
| 3.13 | Numeración 4.1 como `\section` y 4.2/4.3 como `\chapter` (registrado en `00/trazabilidad/PENDIENTES.md`) | 4 |
| 3.14 | Erratas: SD8 «riegos, debemos de definir» (`:53`); T-9 «…Siendo la tabla 6.A.1» sin cierre; tabla de adquisiciones numerada 6.A.2 dentro del Anexo 6.B | 6, 8 |
| 3.15 | Numeración de anexos sin estilo común (2.1–2.3 / 3.A–3.K con tablas 3.A.x / 4-W) | 2, 3 (decidir y unificar) |

---

## Ola 4 — Gravedad media-baja: brechas de contenido que bajan puntaje

| # | Brecha | SD |
|---|---|---|
| 4.1 | Riesgos ausentes: obsolescencia tecnológica, bloqueo por proveedor, escalabilidad | 8 |
| 4.2 | Sin técnica de análisis (FMEA / árbol de fallas / simulación); recuperar la FMEA de `LafroX-Subdoc8-LateX` `partes/cuerpo.tex:138` | 8 |
| 4.3 | Sin costo-beneficio de las respuestas ni plazos; T-16 sin columna de plazo; riesgos sin paquetes de la EDT ni hitos | 8 (citar T-14) |
| 4.4 | «Comité de Calidad y Procesos» con poder de veto que no figura en SD6/T-9 ni en el Art. 71 | 6 o 9 |
| 4.5 | Primera prueba real de DR en el mes 21, junto al paso a producción E2, sin análisis de riesgo | 9, 8 |
| 4.6 | Certificaciones que vencen al inicio del contrato (CMMI nov-2026, ISO 27001 ene-2027, AWS mar-2027) sin plan de renovación | 1, 12 |
| 4.7 | Meta OTIF «95 %» vs caso «sobre 95 %» | 3, 13 (I-04A) |
| 4.8 | RF-14.01 cubre sólo 42 camiones propios (falta fuente para los 54 de terceros); RNF-04.01 «tiempo acotado»; S-22 (5 vs 6 sitios); choque RF-14.01–05 entre caso y Bases | 3 (T-12) |
| 4.9 | 4.3.1 «Data Center Primaria» incluye la «sala técnica secundaria» de Talca sin frase aclaratoria | 4 |
| 4.10 | SD5: pendientes declarados en `revision/` (ampliación sin revisión humana acreditada, 36 «Cumple parcialmente» y 22 «No cumple» en T-12); conteo 139 vs 121 entidades en notas | 5, 3 |
| 4.11 | SD6 RV-012 (40 vs 48 desarrolladores), RV-018 (contingencia DTE), RV-020 (reserva 1.600 HH) | 6, 1, 7 |

---

## Ola 5 — Higiene del repositorio y consolidación

| # | Tarea | SD |
|---|---|---|
| 5.1 | Archivar `LafroX-Subdoc8-LateX` (tras rescatar FMEA), `Guillermo-subdoc4-consistencia`, `Lafrox-Subdoc7-Latex-Tomas`, `LafroX-Subdoc4-LateX` vacía | 4, 7, 8 |
| 5.2 | Quitar restos de plantilla: `main.tex` en modo `borrador` con `EJEMPLO_LAFROX_NO_ENTREGAR.ZIP`, `subdocumento-ejemplo/`, encabezados «Compilar: latexmk main.tex», `tablas/` sin usar, `tmp/`, `PROMPT-PORTADAS.md`, `main.pdf` antiguo del SD4, ~120 PNG de revisión del SD1, README obsoleto | 1, 2, 3, 4, 13 |
| 5.3 | `\datoslafrox`: fecha «12 de octubre de 2026» en todas; sin `version`; subtítulo de SD2 no oficial; SD3 «Subdocumento 3» vs «03»; `lafrox.cls` del SD3 distinta | todos |
| 5.4 | Rama de trazabilidad: actualizar a Propuesta Final (hoy dice «Informe 1») y verificar sus remisiones al SD4 | TRZ |
| 5.5 | Pasada final de remisiones: script que extraiga todas las citas «§x.y», «Tabla», «paquete», «H\d», «R8-», «S-», «RF-» de cada rama y las compruebe contra los `\label`/IDs del destino (reutilizar `revision/audit_sd7_refs.py` de SD7 como base) | todos |

---

## Orden de ejecución (línea de trabajo)

1. **Ola 0** completa, en una reunión corta, documentada en una sola tabla compartida.
2. **Ola 1** en paralelo por responsable de SD (1.2–1.6 son independientes). **1.1** (Caps. 10, 11, 12, 14) empieza en paralelo, pero toma los datos ya canonizados.
3. **Ola 2** en el orden dueño → citante indicado.
4. **Olas 3 y 4** por subdocumento (cada responsable cierra su SD completo).
5. **Ola 5** al final, seguida de una recompilación de todos los PDF.

Fuera de alcance de este listado: contenido económico del Informe 3 (proveedores clave, curva S, costos, VAN/TIR, valorización de innovaciones), salvo que el Cap. 12 y el Cap. 14 deban citarlo.

## Verificación

- Recompilar cada SD con su `latexmkrc` y revisar el `.log`: cero `undefined references` y cero citas sin entrada.
- Revisar el índice de cada PDF contra el índice obligatorio de `aclaraciones-licitacion.md` §11 (títulos, orden, Referencias y Declaración sin número).
- Correr el script de la tarea 5.5 sobre todas las ramas: cero remisiones a destinos inexistentes.
- Búsqueda global de marcadores 7.1(d): `rg -i "pendiente|versión previa|heredado|se deben|requiere reprogramar|borrador|TODO"`.
- Nombres de los PDF generados con el patrón `LAFROX-SubdocumentoN(-Anexos).pdf` / `LAFROX-Formulario-T-X.pdf`.

## Entregable al aprobar

Copiar este plan como `REVISION_INTEGRAL_2026-10-27.md` en la raíz del repositorio (sin commit) para que el equipo lo use como checklist.
