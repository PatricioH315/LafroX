# Hoja de dependencias del SD13 (uso interno, no se entrega)

Regla de trabajo: **solo se edita el SD13**. Cuando otro subdocumento cambie, se revisa esta hoja, se corrige el SD13 y se avisa al dueño del otro subdocumento lo que no calce.

## Cómo revisar después de cualquier cambio externo

1. `git -C ../sd7-corrigiendo log -1`, `../sd8-revision`, `../sd4-corrigiendo` y `../../LafroX`: comparar con los commits de la columna «Última revisión» de abajo.
2. Si cambió alguno: `python revision/verificar_coherencia_sd13.py` (códigos EDT, paquetes y meses, fechas, R-027, montos, referencias).
3. Revisar a mano lo que el script no cubre (columna «A mano»).
4. Compilar las tres piezas: `latexmk LAFROX-Subdocumento13.tex`, `LAFROX-Subdocumento13-Anexos.tex`, `LAFROX-Formulario-T-19.tex`.
5. Actualizar «Última revisión» en esta hoja.

## Dependencias

| Dato en el SD13 | Fuente de verdad | Dónde aparece en el SD13 | Última revisión | Automático | A mano |
|---|---|---|---|---|---|
| Códigos, nombres y meses de los 23 paquetes de la cuenta 7 (7.1 a 7.5) | SD7 `formulario-t15/tablas/tab_T15_asignacion_partidas.tex` (líneas 135-157) | Cuerpo 13.N.4, tablas de paquetes; T-19 campos 8-9; Anexo 13.B | SD7 `b8bededf` (17-11-2026) | Sí | Texto narrativo que mencione paquetes |
| Fechas de inicio y fin de paquetes y fin temprano/tardío CPM | SD7 `tab_T15_paquetes.tex`, `tab_T15_cpm_detalle.tex` | Cuerpo 13.1.4 y 13.3.4; Anexo 13.B | SD7 `b8bededf` | Sí (toda fecha debe existir en el T-15) | Que la frase use la fecha correcta |
| Fechas de H4, H5 y H10 (entrega, acta, límite) | SD7 `tab_T15_7.tex` | Cuerpo 13.1, 13.3, 13.5; T-19 campos 9-10; Anexo 13.B | SD7 `b8bededf` | Sí | Que no se confunda entrega con acta |
| Mes 1 = febrero de 2027; Operación del mes 21 al 56; etapas | Bases Administrativas Art. 17 y SD7 Anexo 7.A | Todo el SD13 | 17-11-2026 | Parcial (mes de los hitos) | Traspaso a Operación en el mes 21 |
| Horas por paquete y perfil (240 HH clase E; 576, 288 y 528 HH de Operación; sesiones EV-15) | SD7 `tab_T15_asignacion_partidas.tex`, `tab_T15_perfiles_internos.tex` | Anexo 13.B (calendario y horas); T-19 campos 10-11 | SD7 `b8bededf` | No | Sí |
| Riesgo R-027 (p0 40 % / 0,10 Media; residual 25 % / 0,06 Baja) | SD8 `LAFROX-Formulario-T-16.tex` (líneas 64 y 125) | Cuerpo 13.4.7; T-19 ficha 4 campo 15; Anexo 13.C | SD8 `1f2d739e` | Sí | Que el texto diga inicial y residual |
| Controles CT-08 a CT-13 | SD8 `08_plan_riesgos/anexo-e-controles.tex` | Cuerpo 13.N.7; Anexo 13.C | SD8 `1f2d739e` | No | Sí |
| Probabilidad e impacto de INN-01, 02, 03 y 05 | Propios del SD13 (juicio de planificación, Anexo 13.C) | Cuerpo 13.N.7 y Anexo 13.C | 17-11-2026 | No | Que cuerpo y anexo coincidan |
| Módulos, componentes y capas (M2, M3, C-01, N-10, B-01…) | SD4 Anexo 4-N | Cuerpo 13.N.4; Anexo 13.B | SD4 `5485aaf9` | No | Sí |
| Volúmenes de nube (15 DPU-h, 1 y 3 h-tarea, 60/120 RPU-h, 2/4 DPU-h); 30.548 mensajes y 127.848 lecturas por día | SD4 Anexo 4-W | Anexo 13.B; cuerpo 13.3.4 | SD4 `5485aaf9` | No | Sí |
| Hardware ofertado (impresora de cabina, gateways B-02 y B-04) | T-11 (SD4) | Cuerpo 13.3.4 y 13.5.4 | SD4 `5485aaf9` | No | Sí |
| Valorización de las innovaciones | E2 ítem 2.7 en `LafroX/02_analisis_economico_financiero/secciones/2-7_valorizacion_innovaciones.tex` y hoja `INNOVACIONES` del modelo `LafroX_ModeloFinanciero_3_20261113.xlsx` | Solo se remite a E-21 2.7; **el SD13 no lleva montos** | Modelo 13-11-2026 | Sí (busca UF, CLP, USD, $) | Que horas y meses sigan calzando con el T-15 |
| Innovaciones dentro del alcance | SD3 secciones 3.1 y 3.4 | Intro del cuerpo | SD3 — | No | Sí |
| Separación INN-03 / RT-05.30 | T-12 (SD3) y SD5 `A_20.tex` | Cuerpo 13.3 | — | No | Sí |
| Cifras del Caso (1,7 %, 2,9 %, 2.600 entregas, 31.000 pedidos…) y su página impresa | `Bases/Caso_02_Logistica.md` y PDF oficial «Caso 02 - Logística» (páginas impresas «n / 41») | Cuerpo 13.N.1 y escenarios físicos | 17-11-2026 | No | Páginas citadas |
| Nombres y cargos (Líder de Datos, Calidad, Operación/SRE, Jefe de Proyecto, Analista PMO) | SD12 y T-15 `tab_T15_perfiles_internos.tex` | Cuerpo 13.N.4 y 13.N.5; T-19 campo 8 | SD7 `b8bededf` | No | Sí |
| Numeración de otras secciones citadas (Cap. 4 §4.1.3, §4.1.4, §4.2.2; Anexo 7.D; Anexo 8.E; Tabla 23 del T-15) | SD4, SD7, SD8 | Intro del cuerpo y pies de tabla | 17-11-2026 | No | Sí |
| Nombres de componentes iguales entre subdocumentos | SD4 | Todo el SD13 | 17-11-2026 | No | Sí |

## Pendientes abiertos del SD13

- **Revisión técnica humana (SD13-12):** registrar revisor, fecha, versión, evidencia y resultado en la declaración de IA. Después se elimina la «Pauta de revisión técnica» del Anexo 13.C y el texto «pendiente» de la declaración.
- **Portada de la propuesta final:** subtítulo y fecha en las tres raíces `.tex` (hoy dicen «Informe 2» y 12 de octubre de 2026).
- **Cadencia de INN-03:** el T-15 lista revisiones en los meses 24, 27, 30, 36, 39, 42, 48, 51 y 54, y el indicador I-03B dice «trimestral». Aclarar con el dueño del SD7.
- **Carta editable `Gantt_Innovaciones_13B.gan`:** sigue con los códigos antiguos y el script `verificar_cotejo_sd13.py` está fijado a commits viejos. Decidir si se actualiza o se archiva.
- **Archivos del Informe 2 ya obsoletos:** `AJUSTES-LOCALES-INFORME2.md` y `validacion-ajustes-locales.json`.

## Diferencias detectadas en otros documentos (para avisar a sus dueños; no se editan desde el SD13)

- E2 2.7: usa los códigos antiguos de paquetes (líneas 5 y 46) y no menciona el ingreso contingente de INN-04.
- Modelo financiero: perfil de INN-04 (todo a Jefe de Proyecto; el T-15 reparte con el Analista PMO), reparto de horas de INN-05 (893,4 + 226,6 contra 960 + 160 del T-15) y meses de operación de INN-02 (22-55 contra 21-56 del T-15).
- SD8: «5.4.3» en el T-16 y en el Anexo F; R-035 «dentro de 7.1.3» choca con INN-01.P3.
- SD9 y T-12 (RT-26.01 y RT-26.02): siguen con los códigos antiguos. `CANON_LAFROX.md:8` dice que los riesgos de innovación parten en R-034.
