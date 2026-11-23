# Hoja de dependencias del SD13 (uso interno, no se entrega)

Regla de trabajo: **solo se edita el SD13**. Cuando otro subdocumento cambie, se revisa esta hoja, se corrige el SD13 y se avisa al dueño del otro subdocumento lo que no calce. Cada cambio del SD13 queda en `REGISTRO_CAMBIOS_SD13.md` con su evidencia; esta hoja dice de dónde viene cada dato y qué hay que volver a mirar.

## Cómo revisar después de cualquier cambio externo

1. `git -C ../sd7-corrigiendo log -1`, `../sd8-revision`, `../sd4-corrigiendo`, `../sd3-corrigiendo`, `../sd9-corrigiendo` y `../../LafroX`: comparar con los commits de la tabla «Estado de las fuentes» de abajo.
2. Si cambió alguno: `python revision/verificar_coherencia_sd13.py` (códigos EDT, paquetes y meses, fechas, R-027, montos, referencias, texto de proceso, páginas del Caso, cifras de los escenarios).
3. Revisar a mano lo que el script no cubre (columna «A mano»).
4. Compilar las tres piezas: `latexmk LAFROX-Subdocumento13.tex`, `LAFROX-Subdocumento13-Anexos.tex`, `LAFROX-Formulario-T-19.tex`.
5. Registrar el cambio en `REGISTRO_CAMBIOS_SD13.md` y actualizar esta hoja.

## Estado de las fuentes (última revisión: 22-11-2026)

| Fuente | Commit revisado | Estado respecto de origin |
|---|---|---|
| SD13 `sd13-corrigiendo` | `e03909f9` | al día (incluye INN-04: fórmula en 7.4.1, calibración en 7.4.2; entrega del H4; Anexo 13.B con la carta nivelada). Fecha de emisión 25 de noviembre de 2026 y sin «§», igual que los demás subdocumentos |
| SD3 `sd3-corrigiendo` | `f7ff197d` (origin) | unifica fecha y quita «§»; el T-12 (RT-26.04) pasa R-027 a 3 × 3 (0,10), igual que el SD13; RT-04.14, RT-05.30 y RT-18.08 sin cambios (diferencia abierta) |
| SD4 `sd4-corrigiendo` | `77dca497` (origin) | unifica fecha y redacta la selección del backend; sin efecto en el SD13 |
| SD7 `sd7-corrigiendo` (T-14 y T-15) | `8e71a160` (origin) | 22-11: unifica fecha; en `tab_T15_perfiles_internos.tex` solo cambia el formato de las fórmulas (mismas HH). Antes, `0624f701`, carta nivelada: la tabla CPM de la cuenta 7 iguala la de paquetes (7.1.4, 7.2.4 y 7.3.4 con holgura 0); 6.1.1, 6.7.1 y 6.7.2 terminan el 22-10-2027, 01-12-2027 y 28-06-2028; H3 al 22-06/07-07-2027; H4, H5, H10 y H12 sin cambios. Anexo 13.B corregido (RV-04) |
| SD8 `sd8-revision` (T-16, Anexo 8.E) | `90868f52` (origin) | unifica fecha, quita «§» y ajusta redacción; R-027 sigue 3 / 0,50 × 3 / 0,20 = 0,10 Media y residual 25 % / 0,06 Baja (T-16:64 y 125), igual que el SD13. CT-08 a CT-13 citan SD13 y T-19; umbrales cotejados, coinciden |
| SD9 `sd9-corrigiendo` (T-13, T-17) | `3ec8689e` (origin) | unifica fecha y quita «§» del T-13; la matriz (RT-26.04) pasa R-027 a 3 × 3 (0,10), igual que el SD13; hitos del T-17 al día con el T-15 |
| Modelo financiero | `LafroX_ModeloFinanciero_3_20261113.xlsx` | del 15-11-2026 |
| PDF oficial del Caso, de las Bases Administrativas y de las Técnicas | `trazabilidad-informe2/Bases/pdf/` | páginas impresas «n / N» |

## Dependencias

| Dato en el SD13 | Fuente de verdad | Dónde aparece en el SD13 | Automático | A mano |
|---|---|---|---|---|
| Códigos, nombres y meses de los 23 paquetes de la cuenta 7 (7.1 a 7.5) | SD7 `tab_T15_asignacion_partidas.tex` (líneas 135-157) | Cuerpo 13.N.4; T-19 campos 8-9; Anexo 13.B | Sí | Texto narrativo que mencione paquetes |
| Fechas de inicio y fin de paquetes; fin temprano y tardío CPM | SD7 `tab_T15_paquetes.tex`, `tab_T15_cpm_detalle.tex` | Cuerpo 13.1.4, 13.2.4, 13.3.4, 13.4.5; Anexo 13.B | Sí (toda fecha debe existir en el T-15) | Que la frase use la fecha correcta |
| Fechas de H4, H5, H10 y H12 (entrega, acta, corte y límite) | SD7 `tab_T15_7.tex`, `tab_T15_subsanacion.tex` (cotejo con `32bac7fc`) | Cuerpo 13.1, 13.3, 13.5; T-19 campos 9-10; Anexo 13.B | Sí: entregas H4/H5/H10, firma H5 y fechas nominales y de subsanación H12 | Confirmar la secuencia de 6.8.6 y la ventana; no tratar la salida del escenario con subsanación como reprogramación contractual. |
| Paquetes que controlan los hitos (6.1.1, 6.7.1 y 6.7.2) | SD7 `tab_T15_7.tex`, `tab_T15_paquetes.tex:90,103,104` | Anexo 13.B | Sí | — |
| Cuenta 7 «Innovaciones verificadas» y paquetes de pruebas (cuentas 6.1 a 6.6) | SD7 `formulario-t14/tablas/tab_T14_1.tex`, `dic_7_*.tex` | Cuerpo 13.2.5, 13.4.4; T-19 ficha 2 | Sí (no deben quedar «3.8» ni «fase 5») | Que 7.5.4 siga «incluida en el acta del H12» |
| Mes 1 = febrero de 2027; Operación del mes 21 al 56; etapas | Bases Administrativas Art. 17 y SD7 Anexo 7.A | Todo el SD13 | Parcial (mes de los hitos y traspaso en el mes 21) | Que INN-05 despliegue por rutas siga en los meses 22 a 26 |
| Horas por paquete y perfil (240 HH clase E; 576, 288, 528 y 80 HH; sesiones EV-15) | SD7 `tab_T15_asignacion_partidas.tex`, `tab_T15_perfiles_internos.tex` | Anexo 13.B (sesiones EV-15); T-19 campos 10-11 | No | Sí |
| Nombres de perfil (Ingeniero de Datos y Bases Senior/Junior, Analista QA Senior/Junior, Analista PMO) | SD7 `tab_T15_perfiles_internos.tex` | Anexo 13.B; cuerpo 13.4.5 | No | Sí |
| Riesgo R-027 (p0 40 % / 0,10 Media; residual 25 % / 0,06 Baja) | SD8 `LAFROX-Formulario-T-16.tex` (líneas 64 y 125) | Cuerpo 13.4.7; T-19 ficha 4 campo 15; Anexo 13.C | Sí | Que el texto diga inicial y residual |
| Controles CT-08 a CT-13 | SD8 `08_plan_riesgos/anexo-e-controles.tex` | Cuerpo 13.N.7; Anexo 13.C | No | Sí |
| Probabilidad, valor de nivel e impacto de INN-01, 02, 03 y 05 | Propios del SD13 con la escala del SD8 (niveles 2 = 0,30 y 3 = 0,50) | Cuerpo 13.N.7; Anexo 13.C; T-19 campo 15 | Parcial | Que cuerpo, anexo y T-19 coincidan |
| Módulos, componentes y capas (M2, M3, C-01, C-02, N-10, B-01…) | SD4 Anexo 4-N (`15_anexo_4_1_n…tex:59-69`) | Cuerpo 13.N.4; Anexo 13.B (INN-03 con capas 1, 2, 4, 5, 6, 7 y 8) | No | Sí |
| Volúmenes de nube (15 DPU-h, 1 y 3 h-tarea, 60/120 RPU-h, 2/4 DPU-h); 30.548 mensajes y 127.848 lecturas por día | SD4 Anexo 4-W | Anexo 13.B; cuerpo 13.3.4 | No | Sí |
| Hardware ofertado (impresora de cabina, gateways B-02 y B-04, cifrado y borrado remoto del terminal) | T-11 (SD4) y BTT RT-17.05 | Cuerpo 13.3.4, 13.5.4 y tabla de amenazas de INN-05 | No | Sí |
| Valorización de las innovaciones | E2 ítem 2.7 (`LafroX/02_analisis_economico_financiero/secciones/2-7_valorizacion_innovaciones.tex`) y hoja `INNOVACIONES` del modelo | Solo se remite a E-21 2.7; **el SD13 no lleva montos** | Sí (busca UF, CLP, USD, $) | Que horas y meses sigan calzando con el T-15 |
| Innovaciones dentro del alcance | SD3 secciones 3.1.1 y 3.4 | Intro del cuerpo | No | Sí |
| Separación INN-03 / RT-05.30 y alcance obligatorio de INN-02 e INN-03 (RT-04.14, RT-21.17, RT-14.01, RT-04.12, RT-03.10, RT-03.19) | T-12 (SD3) `LAFROX-Formulario-T-12.tex:372,391,665`; SD5 `A_20.tex` | Cuerpo tablas 13.7 y 13.12 | No | Sí |
| Cifras del Caso y su página impresa (Riffo p. 16 y 17, Ñanco p. 15, 4.3 y 4.5 p. 8, 4.8 y 4.9 p. 9, 6 p. 11, 2.2 p. 4-5, 14.1 p. 24, B.1 p. 38, criterio 6 p. 34, restricciones 1 y 5 p. 19, 8 y 9 p. 20) | PDF oficial «Caso 02 - Logística» | Cuerpo 13.N.1 y escenarios físicos; T-19 campos 3, 12 y 14; Anexo 13.C | Sí (entrevistas) | Páginas 24 y 38 sin verificar a ojo |
| Páginas de RT citados (RT-03.x p. 9; RT-04.12 y 04.14 p. 11; RT-05.30 p. 13; RT-14.x p. 27; RT-17.05 p. 31; RT-18.07 y 18.08 p. 32; RT-21.17 p. 37; RT-26.x p. 44-45) | PDF oficial de las Bases Técnicas Transversales | Cuerpo y T-19 | No | Sí |
| Nombres y cargos (Líder de Datos, Calidad y Pruebas, Operación / SRE, Jefe de Proyecto, Analista PMO) | SD12 (no entregado), T-14 `tab_T14_2.tex` y T-15 | Cuerpo 13.N.4 y 13.N.5; T-19 campo 8 | No | Sí |
| Numeración de otras secciones citadas (Cap. 4 §4.1.3, §4.1.4, §4.2.2; Anexo 7.A, 7.B y 7.D; Anexo 8.E; Tabla 23 del T-15; Subdocumento 2, Anexo 2.2) | SD2, SD4, SD7, SD8 | Intro del cuerpo y pies de tabla | No | Sí |
| Nombres de componentes iguales entre subdocumentos | SD4 | Todo el SD13 | No | Sí |

## Pendientes abiertos del SD13

- **P-04 Carta `Gantt_Innovaciones_13B.gan` y `verificar_cotejo_sd13.py`:** siguen con los códigos antiguos y commits fijados; el verificador de coherencia los reemplaza (el de cotejo falla en `physical_examples`). Decidir si se archivan.

Cerrados (22-11-2026):

- **P-01 Declaración de revisión humana:** la Tabla 13.29 identifica quién revisó la redacción y la claridad por pieza. La revisión técnica efectiva de modelos, umbrales y cálculos no queda acreditada por esa tabla y debe registrarse por sus responsables antes de darla por cerrada.
- **P-02 Títulos de las referencias 2026a y 2026c:** la portada de los PDF es genérica («Bases Administrativas / Técnicas para la preparación de la propuesta»); el SD13 usa el mismo título que el SD3 y el SD8, así que se mantiene por coherencia del grupo.
- **P-03 Multas (cuerpo 13.4.2):** citadas como Bases Administrativas, Formulario E-25, p. 74.
- **P-05 Páginas 24 y 38 del Caso:** verificadas en «Caso 02 - Logística.pdf» (página impresa = índice del PDF − 1). P. 24, sección 14.1: 2,4 millones de unidades despachadas y ≈ 62.000 visitas de preventa al mes; p. 38, B.1: 62 personas, unas 2.600 visitas diarias.

## Diferencias detectadas en otros documentos (para avisar a sus dueños; no se editan desde el SD13)

Abiertas (revisadas el 22-11-2026 contra SD3 `f7ff197d`, SD7 `8e71a160`, SD8 `90868f52` y SD9 `3ec8689e`; ninguna se cerró con esos commits):

- **E2 2.7** (F1-01): usa los códigos antiguos de paquetes (líneas 5 y 46) y no menciona el ingreso contingente de INN-04. Sin commits nuevos en origin.
- **Modelo financiero:** perfil de INN-04 (todo a Jefe de Proyecto; el T-15 reparte con el Analista PMO), reparto de horas de INN-05 (893,4 + 226,6 contra 960 + 160 del T-15) y meses de operación de INN-02 (22-55 contra 21-56 del T-15).
- **SD8 R-027** (nueva): el Anexo F (`anexo-f-respuestas.tex:48`) y los Anexos del SD8 piden «reglas de 7.4.1 aprobadas al cierre del mes 20»; el T-14 (`dic_7_4.tex`) y el SD13 dicen que Finanzas aprueba la fórmula inicial al cierre de 7.4.1 (1 al 9 de junio de 2028, mes 17) y que la calibración es de 7.4.2 (meses 21 a 23). No es contradicción (el mes 20 sirve de plazo máximo), pero conviene alinear la redacción.
- **SD9** (F2-02): `CANON_LAFROX.md:8` dice que los riesgos de innovación parten en R-034 (el SD13 usa R-027 y siguientes del SD8).
- **SD4** (F3-01): el Anexo 4-N no incluye la capa 5 (cola de sincronización) para INN-05.

Resueltas en el SD13 sin modificar las fuentes (23-11-2026):

- **SD3/T-12 y SD9/T-13** (cotejo del 23-11): RT-05.30 y RT-18.08 remiten al modelo determinista; el SD13 ya no contradice esa respuesta y reconoce una sola capacidad predictiva. RT-04.14 se ejecuta en los paquetes de INN-02, pero los entornos efímeros no son su mérito diferencial. RT-26.08 conserva I-02A en ambos formularios; el SD13 separa de esa validación el beneficio de terreno I-02E.

- **SD7** (F2-09, F3-03, F3-06; cotejo del 23-11): el SD13 conserva la ventana de 7.5.4 y remite el acta H12 a 9.4.2. Para 7.3.5, 21–56 es la ventana de asignación y 24–54 abarca las nueve revisiones programadas, no dos calendarios alternativos. Para 7.3.2, 5–9 es la asignación y 07-06 a 20-09-2027 la ejecución nivelada. El SD13 distingue estas capas sin alterar el T-15.

Resueltas en origin (19-11-2026 y 22-11-2026):

- **SD8** (22-11): el Anexo 8.E vincula CT-08 a CT-13 con las secciones 13.N.6–13.N.7, el Anexo 13.B y las fichas del T-19, con los mismos umbrales del SD13.

- **SD8** (F2-01, F2-02): «5.4.3» pasó a 7.4.1 en el T-16, el Anexo F y los Anexos; R-029 y R-035 citan 9.5.2 y 9.5.3, ya no 7.1.2 y 7.1.3; la Tabla 8.1 y el Anexo 8.E ponen a SRE desde el mes 21 para INN-03 y desde el 22 para el despliegue por rutas de INN-05, igual que el SD13.
- **SD3 y T-12** (F2-02, F4-02): RT-26.01 y RT-26.02 con los códigos 7.x; ya no aparece «2 × 3 (0,06)» para R-027.
- **SD9** (F2-02): 3.10.x, 8.3.x y 5.4.3 de INN-02 pasaron a 7.2.1 a 7.2.5; ya no aparece «2 × 3 (0,06)».
