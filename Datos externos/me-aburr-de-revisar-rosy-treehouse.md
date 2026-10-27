# Revisión integral LafroX — incoherencias y línea de trabajo priorizada

> **Seguimiento del Frente C y actualización acotada del Frente A — 27-10-2026.** Las marcas «Frente C» califican sólo SD6/SD9 y sus anexos/formularios; las marcas «Frente A» califican únicamente el trabajo realizado o verificado en SD8 y sus documentos asociados. ✅ HECHO = implementación o verificación documental respaldada; ⏳ PENDIENTE = parte restante, incluida revisión final o insumos aún no recibidos. En filas compartidas no se certifica ni se modifica el estado de otros frentes. La revisión humana de los cambios y la revisión general acordada siguen pendientes. No se presentan pruebas previstas como ejecutadas.

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
| 7 | `origin/LafroX-Subdoc7-LateX` | revalidado en `7de6b219` (los 3 commits nuevos sólo tocan la figura del camino del H12 y el T-15; los hallazgos siguen presentes, con números de línea corridos) |
| 8 | `origin/Lafrox_Subdocumento_8_Latex_Nuevo` | **única rama del SD8 en el remoto** (`69d764b5`, auditada). `LafroX-Subdoc8-LateX` ya no existe en GitHub; sólo queda la referencia local vieja (de ahí se puede rescatar la FMEA) |
| 9 | `LafroX-Subdoc9-LateX` | checkout actual |
| 10, 11, 12, 14 | — | **no existen** (ramas 10–12 sólo con README; 14 sin rama) |
| 13 | `origin/LafroX-Subdoc13-LateX` | |

---

## Ola 0 — Congelar el canon (antes de tocar cualquier documento) — ✅ CERRADA (C1–C15 decididas el 27-10-2026)

Sin esto, cada arreglo vuelve a abrirse. Es una tabla de decisiones de una página que todos copian tal cual.

| # | Decisión a fijar | Valores en conflicto hoy | Propuesta | SD afectados |
|---|---|---|---|---|
| C1 ✅ | Prefijo de archivos | `LAFROX-`, `LafroX-`, `Lafrox-`, `LafroX-Subdocumento-8-` | **DECIDIDO** (aclaración §1, ejemplo `VORA-` en mayúsculas; Art. 50.3): `LAFROX-SubdocumentoN`, `LAFROX-SubdocumentoN-Anexos`, `LAFROX-Formulario-T-X`; ZIP `SOBRE2_LAFROX_OFERTA_TECNICA_AAAAMMDD.ZIP` | 7, 8 (y 4 al compilar sin jobname) |
| C2 ✅ | Esquema de IDs de riesgo | SD13 cita `R8-23…R8-29` y `O8-01` (48 citas); SD8 vigente usa `R-001…R-033` y no tiene riesgos de innovación | **DECIDIDO:** se mantiene `R-0xx` del SD8. SD8 agrega los riesgos de adopción de INN-01…05 desde `R-034` (con la P×I de SD13) y define el equivalente de `O8-01` (oportunidad); SD13 reescribe sus 48 citas `R8-xx` a `R-0xx`. El formato de 3 dígitos lo distingue de `R-01…R-12` del SD3 | 8, 13, 7 (T-15 reservas) |
| C3 ✅ | Fecha mes 1 del contrato | SD3: «dic-2026 a mar-2027»; SD7/SD9/SD4: feb-2027 | **DECIDIDO:** mes 1 = febrero 2027 (supuesto, consulta V-12; BA Art. 10 n.º 2: mes 1 = primer mes completo). SD3 reemplaza el rango | 3 |
| C4 ✅ | Orden acta ↔ paso a producción (H7 y H12) | Paso E1 05-05-2028 vs acta H7 29-05; paso E2 05-10-2028 vs acta H12 25-10 (SD7 dice «requiere reprogramar»). BA Art. 17.3 exige acta para cerrar la marcha blanca y habilitar el paso; Art. 17.2 n.º 4: la Operación arranca con el paso | **DECIDIDO: dos actas.** (a) Acta de cierre de marcha blanca (Art. 17.3), firmada al final del mes 15 / mes 20, como entregable explícito de 4.2.1 / 4.3.1; habilita los pasos del 05-05 / 05-10-2028. (b) Acta H7 / H12 de aceptación, se mantiene el 29-05 / 25-10-2028 dentro del mes 16 / 21. Borrar «requiere reprogramar» y «La carta no demuestra por sí sola…». Verificar que la revisión de 10 días hábiles del acta (a) cabe dentro de la marcha blanca sin recortar las 4 últimas semanas de evidencia | 7 (SD7, T-14, T-15, T-17, T-18), 9, 13 |
| C5 ✅ | Dotación de terreno | Preparadores: SD7 «120» vs SD2/T-18 «120 + hasta 60». Conductores: SD7 «cerca de 200» vs SD2 ≈244 | **DECIDIDO (derivado del caso, cap. 1 y 2.4):** preparadores = 120 Talca + 60 Concepción (S-39). Conductores ≈200 (42 propios + ≈160 de transportistas); tripulación ≈244 (84 conductores y peonetas propios + ≈160). SD7 `:308, :506` debe nombrar la métrica que usa en cada caso | 7 |
| C6 ✅ | SOC | SD6: «condicional a subcontratación», RT-11.17 parcial; SD1, SD4 Anexo 4-B y T-15: SOC propio en Valparaíso desde el mes 13 | **DECIDIDO: propio.** SOC de LafroX en el Centro de Operaciones de Valparaíso (Av. Brasil 2241); analistas contratados como personal antes del mes 13, bajo el Encargado de Seguridad; 5 personas por posición (SD4 Anexo 4-B). SD6 corrige `adquisiciones.tex:19` y `contenido.tex:37` (RT-11.17 «Cumple»). El Cap. 12.2 no lo lista como subcontrato | 6, 12 (nuevo) |
| C7 ✅ | Coberturas de prueba | SD1/SD3: lógica ≥70 % y global ≥80 %; T-10: 80 % código modificado; SD6: «80 % global»; SD9: las tres | **DECIDIDO: las tres, con su fuente.** ≥70 % lógica de negocio (RT-04.11, bloqueante en CI); ≥80 % global (política interna SD1 §1.3); ≥80 % del código modificado por cambio (T-10). Completar SD1, SD3, SD6, T-10 `:54`, T-14 1.5.2; SD9 ya cumple | 1, 3, 6, 7, 9 |
| C8 ✅ | RPO ante pérdida del sitio | SD7/T-18: «se cumple» + párrafo sobre «falla de los tres caminos seguida de la destrucción del sitio… no garantizan la recuperación»; SD8 `:200`: «debe demostrarse… se mantiene como pendiente» | **DECIDIDO: no se declara ese escenario como riesgo ni como salvedad.** Afirmación única y positiva: RTO ≤ 4 h y RPO ≤ 15 min (RT-07.04), con tres caminos independientes, alarmas de retraso de replicación a 5 y 15 min y medición en conmutación real (AL-DR-01 antes del H5/H10; semestral, RT-07.07). Eliminar el párrafo de destrucción del sitio en SD8 `:200`, SD7 `subdocumento-07/contenido.tex:551` y T-18 `:237` | 7, 8 |
| C9 ✅ | Ventana de congelamiento | T-10: todo septiembre; SD7/T-18/SD5: 1–25 sept. | **DECIDIDO (Caso, condición 8 y RT-10.05):** 1–25 de septiembre, todo diciembre y los tres primeros días hábiles de cada mes; ventana 05:30–07:00 con indisponibilidad cero. Corregir T-10 `:60` | 6 |
| C10 ✅ | Terminología de componentes | M12 «Telemetría» (SD3/SD4/SD13) vs «posición de flota» (T-18 `tab_T18_olas_alcance`); «Redis» (SD5) vs «ElastiCache Valkey 8.1» (SD4); B-08 «registrador» (SD13) vs «sensor» (T-11); «M» = mes y módulo (SD5) | **DECIDIDO: SD4 + T-11 son el diccionario oficial.** «M12 Telemetría»; «Amazon ElastiCache (Valkey 8.1)»; B-08 con el nombre del T-11; meses siempre «mes N», nunca «MN». Corrigen SD5, SD7 (T-18) y SD13; el glosario del SD3 se alinea | 3, 5, 7, 13 |
| C11 ✅ | Responsables | SD8/T-16 usa 13 roles («Líder de integraciones», «Líder de migración», «Líder funcional de rutas»…); SD1/SD7 usan 8 roles | **DERIVADO:** sólo los 8 roles de SD7 `tab_SD7_3` / SD1 Tabla 1.6 (JP, ARQ, DES, CAL, SRE, SEG, DAT, IMP). El Cap. 12 (nuevo) usa los mismos | 8, 12 |
| C12 ✅ | Títulos oficiales de subdocumentos y formularios en Referencias | «Modelo de datos», «Problema y necesidad», «Inventario de hardware y software», «Fichas de innovación» | **DERIVADO (Bases, T-7 y lista de formularios):** títulos exactos. Ej.: SD5 «Modelo y gestión de datos», T-11 «Especificaciones técnicas ofertadas», T-19 «Cartera de innovaciones» | 2, 4, 5, 13 |
| C13 ✅ | Citas de documentos propios y de las Bases | «LafroX 2026a/b/c» significa cosas distintas en cada SD; autor «LafroX» vs «LafroX SpA.»; misma fuente del caso con 3 títulos («Distribuidora Puelche S.A. 2026c») | **DECIDIDO: remisión interna.** SD y formularios propios se citan en el texto como «(Subdocumento 4, sección 4.2.3)» / «(Formulario T-15, sección 5)» y **se eliminan todas las entradas «LafroX (2026x)» de las listas de Referencias**. **DERIVADO (Aclaración §6):** las Bases se citan «(Bases Técnicas del caso, Cap. 7, p. 12)» / «(Bases Administrativas, Art. 17, p. 13)», con documento, capítulo o artículo y página | todos |
| C14 ✅ | Declaración de IA | «No aplica» (SD1, SD3); «Alto» en todas las filas (SD4, SD5); SD8: «riesgos generados por ia», «contenido academico» | **DECIDIDO:** (a) reemplazar «No aplica» por «Ninguno» (SD1 `contenido.tex:376-383`, SD3 `:580-595`); (b) los «Alto» de SD4 y SD5 se mantienen, porque están revisados por personas y la fila nombra quién verificó qué; (c) la declaración del SD8 la corrige el equipo a mano (fuera de este plan). Ajuste de forma: el nivel en diagramas de SD2 para 2.4, 2.5 y Anexos 2.1–2.3 (sin figuras) pasa a «Ninguno» | 1, 2, 3 |
| C15 ✅ | Numeración de secciones de formularios | T-14/T-15/T-18 (`setcounter{chapter}{6}`) y T-17 (`{8}`) heredan el prefijo del capítulo; T-13 numera a mano desde 1. SD1/SD9 citan «T-15 §7.5.7»; SD7 dice «T-15, sección 5»; SD3 cita «T-13, sección 8.2» (que es «Tamaño estimado del catálogo», no la matriz: **mal apuntada**) y «T-18, sección 6.4» | **DECIDIDO: cada formulario numera desde 1.** Quitar `\setcounter{chapter}` de `LafroX-Formulario-T-14/15/18.tex` y `LAFROX-Formulario-T-17.tex`; citar siempre «Formulario T-X, sección N.M» (sin «§»). Actualizar las citas «§7.x» de SD1 (`:73, :324`), SD9 y TRZ, y revisar el destino real de las citas del SD3 a T-13 y T-18 | 1, 3, 7, 9 |

---

### Ejecución de la Ola 0 (alcance aprobado: canon + aplicarlo en los SD)

Las demás olas **no se ejecutan** hasta que el usuario lo indique.

**Mecánica**
- Una worktree por rama en `C:\Users\henri\OneDrive\Documentos\Universidad 2026S2\FEP\Repositorios\Principal\LafroX-worktrees\sdN` (`git worktree add`). No se cambia la rama del checkout actual (SD9).
- `git fetch origin` antes de empezar; trabajar sobre la cabeza del remoto de cada rama.
- Un commit por rama, con conventional commits, en español y sin atribución de IA (regla de CLAUDE.md), por ejemplo `docs(sd7): aplica canon C1, C4, C5, C8, C10, C13 y C15`.
- **No hacer push** sin confirmación del usuario.
- `CANON_LAFROX.md` (tabla C1–C15 final) en la raíz de la rama SD9, como única copia de referencia.

**Orden** (dependencias: SD8 fija los nuevos IDs antes que SD13; el resto es independiente)

| Paso | Rama | Decisiones a aplicar |
|---|---|---|
| 0 | SD9 (actual) | Crear `CANON_LAFROX.md`; C15 (quitar `\setcounter{chapter}{8}` de `LAFROX-Formulario-T-17.tex`, citas «§7.x» → «Formulario T-15, sección N.M»); C13 (remisiones internas, fuera las entradas `LafroX (2026x)`, Bases según §6); C4 (referencias al acta H12) <br>**Frente C — ✅ HECHO: aplicación documental de C4/C13/C15 en SD9; ⏳ PENDIENTE: revisión semántica completa y conciliación final de T-17/calendario con K6.** |
| 1 | SD8 `Lafrox_Subdocumento_8_Latex_Nuevo` | C1 (renombrar `LafroX-Subdocumento-8-Anexos.tex` → `LAFROX-Subdocumento8-Anexos.tex`, `Lafrox-Formulario-T-16.tex` → `LAFROX-Formulario-T-16.tex`, nombres en `\configurarportadalafrox`); C2 (agregar `R-034…` para los riesgos de adopción de INN-01…05 con la P×I del SD13 y el equivalente de `O8-01`); C8 (eliminar el párrafo de destrucción del sitio en `contenido.tex:200`); C11 (T-16 con los 8 roles); C13. **Fuera:** la Declaración de IA (manual, C14) |
| 2 | SD13 | C2 (las 48 citas `R8-xx` → `R-0xx` según el paso 1); C10 (nombre de B-08 según el T-11); C12 (títulos oficiales de T-11 y T-19; agregar «sostenibilidad» al tipo 5 de la Tabla 13.1); C13 |
| 3 | SD7 | C1 (`LafroX-*` → `LAFROX-*` en .tex, portadas y `latexmkrc`/jobname); C4 (acta de cierre de marcha blanca como entregable explícito de 4.2.1 y 4.3.1 en T-14; eliminar «requiere reprogramar» y «La carta no demuestra por sí sola…» en `subdocumento-07/contenido.tex`; alinear T-15, T-17 y T-18); C5 (`:308`, `:495-506`); C8 (`subdocumento-07/contenido.tex:551`, T-18 `:237`); C10 (T-18 «M12 Telemetría»); C13; C15 (quitar `\setcounter{chapter}{6}` de T-14/T-15/T-18 y ajustar referencias internas) |
| 4 | SD6 | C6 (SOC propio: `tablas/adquisiciones.tex:19`, `contenido.tex:37`); C7 (T-10 `:54`, `contenido.tex:66`); C9 (T-10 `:60`); C13 <br>**Frente C — ✅ HECHO: C6/C7/C9/C13 aplicados en SD6 y formularios; compilaciones correctas. ⏳ PENDIENTE: auditoría semántica final de fuentes/citas de nuestro alcance.** |
| 5 | SD5 | C10 (Redis → «Amazon ElastiCache (Valkey 8.1)»; «MN» → «mes N»); C12; C13 (reconstruir la lista; se cruza con 1.5) |
| 6 | SD4 `subdoc-4` | C12 (títulos oficiales en `cierre/referencias.tex`); C13 |
| 7 | SD3 | C3 (`contenido.tex:59`: mes 1 = febrero de 2027); C7; C10 (glosario alineado al SD4); C13 (unificar estilos de cita); C14 («No aplica» → «Ninguno», `:580-595`); C15 (corregir los destinos de «T-13, sección 8.2» y «T-18, sección 6.4») |
| 8 | SD2 | C12/C13 (fuente del caso única, según §6); C14 (nivel en diagramas «Ninguno» donde no hay figuras) |
| 9 | SD1 | C7; C13 (incluye T-6 «2026d»); C14 (`:376-383`); C15 (citas `:73`, `:324`) |

**Verificación de la Ola 0**
- `latexmk` en cada worktree (subdocumento, anexos y formularios): sin `undefined references` ni citas sin entrada en el `.log`.
- `rg` por rama, con 0 resultados esperados en: `No aplica` (tablas de IA), `R8-` (SD13), `LafroX \(2026`, `§7\.`, `Redis` (SD5), `requiere reprogramar`, `destrucción del sitio`, `condicional a subcontratación`.
- `fd` de los .tex de entrega: todos con prefijo `LAFROX-`.
- Resumen final al usuario: lista de commits por rama, sin push.

## Ola 1 — Gravedad crítica: puntaje 0 o «no presentado»

| # | Problema | Evidencia | Arreglo | SD afectados |
|---|---|---|---|---|
| 1.1 | **Faltan los Capítulos 10, 11, 12 y 14** y el Formulario **T-8** (22 % de la ponderación final). Además SD1, SD3 y SD7 ya remiten al Cap. 12 / 12.3 | aclaraciones §11; T-21 | Crear las ramas desde la rama local `rama-formato-Latex-base` (ya no está en el remoto; conviene partir de la clase y la portada estandarizadas del SD9) y redactar con los índices obligatorios. Depende de la Ola 0 (C6, C8, C11) y de los datos de SD1 (dotación, alianzas), SD4 (SLA, observabilidad), SD7 (curva de dotación T-15), SD9 (pruebas DR) | 10, 11, 12, 14 (nuevos); 1, 7 (verificar remisiones) |
| 1.2 | **SD8 con indicios 7.1(d)**: «versión previa», «supuesto heredado», «se deben vincular», «pendientes de estimación», «solapamiento en 70 %, que se conserva», «Corresponde obtener…», «se mantiene como pendiente» | SD8n `contenido.tex:79, 117, 171, 183-190, 196-202` | Reescribir esos pasajes como contenido final del proponente (la Declaración de IA del SD8 la corrige el equipo a mano, C14) | 8 |
| 1.3 | **SD7 reconoce pendientes en el texto**: «requiere reprogramar» (H12), «La carta no demuestra por sí sola…»; archivos huérfanos `tab_T15_contingencia.tex` («pendiente de conciliación») y `tab_T15_11` | SD7 `contenido.tex:350, 429` | Resolver C4 y eliminar los huérfanos | 7, 9, 13 |
| 1.4 | **Nombres de archivo mal formados** (Art. 40.4: no presentado) | SD7 `LafroX-…`; SD8 `LafroX-Subdocumento-8-Anexos`, `Lafrox-Formulario-T-16`, portada T-16 «Lafrox-Subdocumento-T-16.pdf» | Aplicar C1. **Frente A — ✅ HECHO (parte de las portadas):** «Formulario T-7» se corrigió a «Formulario T-16» en las portadas del SD8 y anexos; la fecha ahora usa metadatos y la compilación aislada mostró 27-10-2026. **⏳ PENDIENTE:** renombrar/verificar archivos según C1 y resolver el nombre impreso; el ítem 1.4 no está completo. | 7, 8 |
| 1.5 | **SD5 con Referencias rotas**: entradas sin autor ni año, citas borradas en el texto («las Bases Técnicas del Caso  y …»), citas sin entrada (Puelche 2026d, LafroX SpA 2026a) | SD5 `partes/referencias_ia.tex:5-17`, `contenido.tex:24`, `5_1_modelo.tex:170, 205` | Reconstruir la lista (recuperar de antes del commit 2f936555) y las citas | 5 |
| 1.7 | **Leyendas e indicios textuales de la Aclaración 7.1 a) y d)**: «Fuente: elaboración propia» (7.1 a la nombra literalmente); «borrador» en el contenido<br>**Frente C — ✅ HECHO: fuentes genéricas de SD6 sustituidas por fuentes concretas. ⏳ PENDIENTE: búsqueda y clasificación exhaustiva de marcadores en SD6/SD9 y sus formularios/anexos (C09; transversal 4.7).** | «elaboración propia»: SD8 `contenido.tex:57, 69, 80`, `figuras/rbs.tex:15`, `Lafrox-Formulario-T-16.tex:36`; SD6 `anexos.tex:16`, `tablas/adquisiciones.tex:1`, `comunicaciones.tex:1`, `interesados.tex:2`; SD3 `tablas/sint_epicas.tex:29`; SD7 `formulario-t14/contenido.tex:612`. «Borrador»: SD7 `subdocumento-07-anexos/tablas/tab_7B1.tex:4` (renombrar a «versión preliminar», como hizo SD9). `main.tex` con opción `borrador` en SD1/SD2/SD3 | Reemplazar cada leyenda por la fuente concreta («Fuente: Bases Técnicas del caso, Cap. X, p. Y» o «Fuente: cálculo de la sección N»). Búsqueda final en todas las ramas: `elaboración propia`, `borrador`, `pendiente`, `??`, `[cite`, `académic`, `docente`, `estudiante` | 3, 6, 7, 8 (+1, 2, 3 por `main.tex`) |
| 1.6 | **SD13 cita 48 veces riesgos que no existen** (`R8-23…R8-29`, Anexo 8.F `O8-01`), y SD8 no tiene riesgos de adopción de innovaciones | `git grep R8-` en SD13 vs SD8n | Aplicar C2: agregar a SD8 los riesgos de adopción de INN-01…05 con la P×I que declara SD13, o renumerar SD13. **Frente A — ✅ HECHO (SD8):** el catálogo vigente incluye R-034–R-040 para los riesgos añadidos. **⏳ PENDIENTE:** revalidar contra K0 y alinear/verificar SD13; SD13 se mantuvo en solo lectura, por lo que no se marca completo el ítem compartido. | 8, 13 |

---

## Ola 2 — Gravedad alta: contradicciones y remisiones rotas entre subdocumentos

Ejecutar en el orden indicado: primero el documento «dueño» del dato, después los que lo citan.

| # | Incoherencia | Dueño → corregir en |
|---|---|---|
| 2.1 | Supuestos P7-01…P7-11: el Anexo 7.F dice que el Cap. 8 los evalúa; SD8 no menciona ningún P7. Reservas: T-15 y SD8 se remiten la conciliación mutuamente y nadie la hace | SD8 (evaluar P7 y conciliar reservas) → SD7 (T-15 refleja reservas en el cronograma). **Frente A — ⏳ PENDIENTE:** se localizó la fuente del Anexo 7.F (`subdocumento-07-anexos/tablas/tab_7F1.tex`, rama SD7, `93a5e884`, con P7-01…P7-11); aún no se evaluó/propagó en SD8 ni se concilian reservas. Hace falta validar K0 y recibir K4/K5. |
| 2.2 | SOC (C6)<br>**Frente C — ✅ HECHO en SD6/T-9: SOC propio, ubicación/dirección y contratación de analistas antes del mes 13, sin subcontratación del SOC (C01).** | SD6 `tablas/adquisiciones.tex:19`, `contenido.tex:37` ↔ T-15 `contenido.tex:98` |
| 2.3 | Sala técnica: SD6 dice obra civil meses 5–6 a cargo de LafroX; T-14 6.1.1 dice a cargo del CLIENTE (RT-06.06) e instalación en el mes 3<br>**Frente C — ✅ HECHO en SD6/T-9/Anexo 6.B: obra civil de separación a cargo del CLIENTE; LafroX especifica/coordina y provee piso/equipos; instalación mes 3 y recepción de sala mes 4. ⏳ PENDIENTE: revalidar nuestros textos contra K6 final (C01).** | T-14 (dueño) → SD6 `adquisiciones.tex:8` |
| 2.4 | «Hasta 16 evaluadores subcontratados por día» atribuido a SD6 §6.1.3, que no lo dice<br>**Frente C — ✅ HECHO: política documentada en SD6/T-9 y consumida en SD9/T-13: hasta 16 externos/día por demanda; meses 9–12 y 16–18; hipótesis 8 h nominales y 6,4 HH netas/persona-día. ⏳ PENDIENTE: cuadrante de días/concurrencias y comprobación de capacidad con la programación final; no se acredita contratación ni disponibilidad real (C02).** | SD6 (agregar o no) → T-15 `tab_T15_8`, SD9 `:291, 303, 324` |
| 2.5 | Umbrales «duplicación ≤3 %» y «acoplamiento ≤20» atribuidos al T-10, que no los declara<br>**Frente C — ✅ HECHO: propuesta de definición medible preparada. ⏳ PENDIENTE: ratificar duplicación ≤3 % y acoplamiento ≤20; fijar/configurar/calibrar herramientas por lenguaje y propagar de forma consistente a T-10, SD6, SD9, Anexo 9.A/9.B y T-13. No se han presentado como política nueva aprobada (C03).** | T-10 (agregar) → SD9 `:104-105`, Anexo 9.A `:123` |
| 2.6 | Coberturas (C7)<br>**Frente C — ✅ HECHO en SD6/T-10/SD9: tres coberturas diferenciadas y exigibles conjuntamente: ≥70 % lógica de negocio, ≥80 % global y ≥80 % código modificado. No se certifica aquí la parte de T-14 (C03).** | T-10 `:54`, SD6 `:66`, T-14 1.5.2 |
| 2.7 | RPO (C8) | SD4 → SD7 `:562`, T-18 `:237`, SD8 `:200` |
| 2.8 | Preparadores y conductores (C5) | SD2 → SD7 `:308, 506` |
| 2.9 | Congelamiento (C9)<br>**Frente C — ✅ HECHO en T-10: períodos C9 y ventana 05:30–07:00 sin indisponibilidad. ⏳ PENDIENTE: contrastar y resolver en SD6/SD9 la aparente diferencia entre prohibición de despliegues y excepción de emergencia descrita en SD9, según fuente autorizada; cerrar ventanas de pruebas con K6 (C06).** | T-10 `:60` ↔ SD7 `:514`, T-18 `:41` |
| 2.10 | Reversión técnica: SD7 `tab_SD7_7` la asigna al SRE; SD4 la declara automática | SD4 → SD7 |
| 2.11 | Remisiones mal apuntadas: T-11 `:115` cita 4.1.3.5 para M9 (es Integración); SD5 §5.1.7 cita «SD4 4.1.4.8» (M9 está en 4.1.4.2); SD3 cita «T-18 §6.4» y «T-13 §8.2»; SD4 `11_j:63` cita «T-13 §4.1»<br>**Frente C — ✅ HECHO: verificados los destinos actuales T-13, sección 8.2 (catálogo y matriz individual), y T-13, sección 4.1 (instancias de Preproducción); ambas remisiones sí tienen respaldo en la versión revisada. No se modifican ni califican las otras remisiones de esta fila (C07).** | Verificar cada destino y corregir |
| 2.12 | Remisiones no verificadas aún: SD7/SD8 → SD4 §4.1.4.4, 4.2.4.1.2, 4.3.2.4, Anexo 4-W.7; SD3 §3.4.3–3.4.5, Anexo 3.I; SD13 «transferencia desde el mes 22»; TRZ → SD4 4.1.1, 4.3.2.4, 4.2.6, 4.1.3.5<br>**Frente C — ⏳ PENDIENTE únicamente para C: completar inventario y verificación semántica de las remisiones que salen de SD6/SD9 y sus anexos/formularios, y revalidarlas contra los commits finales recibidos. No se califica el trabajo de TRZ ni de otros SD (C07; transversal 4.7).** | Verificar en la Ola 5 con el script de remisiones |
| 2.13 | Terminología (C10) | SD5, T-14, SD13 |
| 2.14 | Responsables del T-16 (C11) | SD8 |
| 2.15 | Retención por lote vs por SSCC | SD3 l.12, 153, RNG-04 vs SD2 S-04, SD3 l.120, 295 |
| 2.16 | Fecha de inicio (C3) | SD3 l.59 |

---

## Ola 3 — Gravedad media: incumplimiento formal del índice y de la redacción (ítem Transversal + ítem del SD)

| # | Problema | SD |
|---|---|---|
| 3.1 | Título de capítulo distinto al obligatorio: «Introducción a las metodologías» (debe ir «Metodologías»)<br>**Frente C — ✅ HECHO: título del capítulo de SD6 corregido a «Metodologías», compilado y comprobado en PDF (C08).** | 6 |
| 3.2 | Título de capítulo «Introducción de riesgos» (debe ser «Introducción a los Riesgos»). **Frente A — ✅ HECHO:** título corregido en `08_plan_riesgos/contenido.tex`, compilado y comprobado en la salida aislada de SD8. | 8 |
| 3.3 | Referencias y Declaración de IA numeradas como 6.3 y 6.4 (deben ir sin número); «Referencias» seguido de lista<br>**Frente C — ✅ HECHO: Referencias y Declaración de IA de SD6 sin numeración, incluidas en índice y con texto de entrada; cierre aclaratorio de la actualización añadido (C08).** | 6 |
| 3.4 | Diez `\paragraph*` seguidos de `itemize` sin frase de entrada; «La tabla distingue…» sobre una lista | 4 (`02_b:25, 46`; `02_a:263`; `11_j:225, 376, 459`; `12_k:72, 163, 243, 291`; `06_e:38, 80`) |
| 3.5 | Tablas consecutivas sin texto (2.A.1 → 2.A.2) | 2 `anexos.tex:30-33` |
| 3.6 | Títulos 3.3.2 y 3.3.3 dentro de `minipage`; párrafos de cadena de frío pegados antes de la introducción de 3.1.1, 3.4.1, 3.4.5, 3.4.6 | 3 |
| 3.7 | Mezcla de problema y solución en el Cap. 2 («Decisión que requiere la necesidad», «Decisión del proponente») | 2 `contenido.tex:66-67`, `anexos.tex:163` |
| 3.8 | RBS en página A3 (Bases exigen carta u oficio); numeración de tablas forzada a mano y duplicada («8.4»). **Frente A — ✅ HECHO (RBS):** rediseñada en dos páginas oficio apaisadas; se comprobaron los 40 IDs y la salida aislada. **⏳ PENDIENTE:** revisar la numeración de tablas; el borrador sigue provisional hasta revalidarlo contra K0. | 8 |
| 3.9 | Citas sin entrada / entradas sin cita: SD1 «2026c», T-6 «2026d», SD3 «Ministerio de Salud, 1996», SD6 Kruchten, SD8 «2026c», «2026-a», SD13 «LafroX, 2026» sin letra; estilos mezclados en SD3<br>**Frente C — ✅ HECHO en nuestro alcance: Kruchten citado en SD6 y cita huérfana «2026c» de SD9 reemplazada por el Caso, capítulo 8, página impresa 15 verificada. ⏳ PENDIENTE: auditoría semántica completa de citas/entradas, fuentes y páginas en SD6/SD9 y formularios. Los casos de otros SD quedan sin calificar (C08; transversal 4.7).** | 1, 3, 6, 8, 13 (tras C13) |
| 3.10 | Declaración de IA (C14) + tabla sin texto de cierre en SD1; niveles «Medio» en diagramas para secciones sin figuras en SD2 | 1, 2, 3, 4, 5, 8 |
| 3.11 | Figuras: SD6 no tiene ninguna; SD7 con 17 láminas EDT sin `\ref` previo y lámina que «amplía» la 3.10 (§4)<br>**Frente C — ✅ HECHO en SD6: Figura 6.1 del proceso de control, con llamada previa, fuente, explicación y declaración de asistencia IA; PDF revisado por muestreo. ⏳ PENDIENTE: revisión humana de la nueva figura y revisión visual integral de las figuras de nuestro alcance. No se califica SD7 (C09).** | 6, 7 |
| 3.12 | T-6 con campos renombrados («Experiencia del Proponente», «Período de implementación / operación»); T-15 `tab_T15_3` sin la columna «N° de personas (peak)»; T-19 titulado «Fichas de innovación»; tipo 5 sin «sostenibilidad» en Tabla 13.1 | 1, 7, 13 |
| 3.13 | Numeración 4.1 como `\section` y 4.2/4.3 como `\chapter` (registrado en `00/trazabilidad/PENDIENTES.md`) | 4 |
| 3.14 | Erratas: SD8 «riegos, debemos de definir» (`:53`); T-9 «…Siendo la tabla 6.A.1» sin cierre; tabla de adquisiciones numerada 6.A.2 dentro del Anexo 6.B<br>**Frente C — ✅ HECHO en SD6/T-9: frases inconclusas completadas, adquisiciones numeradas 6.B.1 y remisiones corregidas. No se califica la errata del SD8 (C08).**<br>**Frente A — ✅ HECHO en SD8:** la errata se reemplazó por «Para analizar los riesgos, se definen…» en `08_plan_riesgos/contenido.tex`; se compiló y verificó la salida aislada. | 6, 8 |
| 3.15 | Numeración de anexos sin estilo común (2.1–2.3 / 3.A–3.K con tablas 3.A.x / 4-W) | 2, 3 (decidir y unificar) |
| 3.16 | **Tablas del cuerpo vs Aclaración §5 (no auditado sistemáticamente):** prohibidas las tablas «Concepto \| Descripción», las celdas con más de una frase, más de 5 columnas o más de 1 página; cada tabla debe tener fuente, cita previa en el texto y análisis posterior. Caso ya detectado: SD7 `tab_SD7_7` (M8). Revisar todas las tablas del cuerpo de cada SD y mover los listados al anexo/formulario con tabla de síntesis<br>**Frente C — ✅ HECHO en nuestro alcance: auditoría heurística de tablas del cuerpo, comprobaciones de las 14 tablas técnicas de SD9 y traslado de las descripciones de fases a prosa; seis columnas de la declaración IA conservadas por exigencia específica de Aclaraciones 7.2. ⏳ PENDIENTE: inventario completo con título/extensión PDF, revisión semántica de celdas/fuentes/análisis posterior e inspección visual integral de SD6/SD9. El verificador no acredita por sí solo cumplimiento integral (C09; transversal 4.7).** | todos |

---

## Ola 4 — Gravedad media-baja: brechas de contenido que bajan puntaje

| # | Brecha | SD |
|---|---|---|
| 4.1 | Riesgos ausentes: obsolescencia tecnológica, bloqueo por proveedor, escalabilidad | 8 |
| 4.2 | Sin técnica de análisis (FMEA / árbol de fallas / simulación); recuperar la FMEA de `LafroX-Subdoc8-LateX` `partes/cuerpo.tex:138` | 8 |
| 4.3 | Sin costo-beneficio de las respuestas ni plazos; T-16 sin columna de plazo; riesgos sin paquetes de la EDT ni hitos | 8 (citar T-14) |
| 4.4 | «Comité de Calidad y Procesos» con poder de veto que no figura en SD6/T-9 ni en el Art. 71<br>**Frente C — ✅ HECHO: gobierno de SD6/T-9 y SD9 alineado con SD1, secciones 1.2/1.3.1; comité interno QA/líderes, reunión mensual y escalamiento a Gerencia; no se atribuye al Art. 71 ni sustituye aceptación del CLIENTE (C04).** | 6 o 9 |
| 4.5 | Primera prueba real de DR en el mes 21, junto al paso a producción E2, sin análisis de riesgo<br>**Frente C — ✅ HECHO en SD9/T-13: revalidado que 3.8.5/3.9.4 ya preceden H5/H10; añadido protocolo 7.6 con prerrequisitos, ambiente, medición RTO/RPO, evidencia y salida; mes 21 aclarado como primera conmutación periódica de Operación, no primera prueba del proyecto. ⏳ PENDIENTE: periodicidad entre campañas, recursos/ventanas contra K6 y tratamiento del riesgo residual que afecta nuestras pruebas. No se califica SD8 ni se inventan ejecuciones (C05).** | 9, 8 |
| 4.6 | Certificaciones que vencen al inicio del contrato (CMMI nov-2026, ISO 27001 ene-2027, AWS mar-2027) sin plan de renovación | 1, 12 |
| 4.7 | Meta OTIF «95 %» vs caso «sobre 95 %» | 3, 13 (I-04A) |
| 4.8 | RF-14.01 cubre sólo 42 camiones propios (falta fuente para los 54 de terceros); RNF-04.01 «tiempo acotado»; S-22 (5 vs 6 sitios); choque RF-14.01–05 entre caso y Bases | 3 (T-12) |
| 4.9 | 4.3.1 «Data Center Primaria» incluye la «sala técnica secundaria» de Talca sin frase aclaratoria | 4 |
| 4.10 | SD5: pendientes declarados en `revision/` (ampliación sin revisión humana acreditada, 36 «Cumple parcialmente» y 22 «No cumple» en T-12); conteo 139 vs 121 entidades en notas | 5, 3 |
| 4.11 | SD6 RV-012 (40 vs 48 desarrolladores), RV-018 (contingencia DTE), RV-020 (reserva 1.600 HH)<br>**Frente C — ✅ HECHO: RV-012/018/020 revalidados y respuestas/entradas requeridas documentadas; T-13 contempla carga modificada/ERP indisponible sin emisor alternativo. ⏳ PENDIENTE en nuestros SD: cerrar coherencia con asignación efectiva, solución DTE y K5/K6; distinguir reserva de evaluación E2 y demostrar capacidad sin doble conteo. No reemplazar a ciegas 40/48 ni presentar las 1.600 HH de evaluación como reserva disponible (C06).** | 6, 1, 7 |

---

## Ola 5 — Higiene del repositorio y consolidación

| # | Tarea | SD |
|---|---|---|
| 5.1 | Archivar `Guillermo-subdoc4-consistencia` y `LafroX-Subdoc4-LateX` vacía (`LafroX-Subdoc8-LateX`, `Lafrox-Subdoc7-Latex-Tomas`, `LafroX-Revision-Trazabilidad-Informe1-LateX` y `rama-formato-Latex-base` ya no existen en el remoto; rescatar la FMEA del SD8 desde la referencia local antes de `git fetch --prune`) | 4, 8 |
| 5.2 | Quitar restos de plantilla: `main.tex` en modo `borrador` con `EJEMPLO_LAFROX_NO_ENTREGAR.ZIP`, `subdocumento-ejemplo/`, encabezados «Compilar: latexmk main.tex», `tablas/` sin usar, `tmp/`, `PROMPT-PORTADAS.md`, `main.pdf` antiguo del SD4, ~120 PNG de revisión del SD1, README obsoleto | 1, 2, 3, 4, 13 |
| 5.3 | `\datoslafrox`: fecha «12 de octubre de 2026» en todas; sin `version`; subtítulo de SD2 no oficial; SD3 «Subdocumento 3» vs «03»; `lafrox.cls` del SD3 distinta<br>**Frente C — ⏳ PENDIENTE sólo para SD6/SD9: aplicar y comprobar fecha/versión/formato comunes cuando exista acuerdo aprobado; no se cambia el canon ni la clase compartida desde este frente. Los demás SD quedan sin calificar.** | todos |
| 5.4 | Rama de trazabilidad: actualizar a Propuesta Final (hoy dice «Informe 1») y verificar sus remisiones al SD4 | TRZ |
| 5.5 | Pasada final de remisiones: script que extraiga todas las citas «§x.y», «Tabla», «paquete», «H\d», «R8-», «S-», «RF-» de cada rama y las compruebe contra los `\label`/IDs del destino (reutilizar `revision/audit_sd7_refs.py` de SD7 como base)<br>**Frente C — ✅ HECHO en C: verificadores locales de matriz/alineación y destinos puntuales de T-13 comprobados. ⏳ PENDIENTE: pasada semántica completa de nuestras remisiones sobre las versiones finales y resolución de los hallazgos propios del verificador común; no se declara ejecutada la auditoría global de otros frentes.** | todos |

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
