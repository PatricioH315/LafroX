# Iteración de revisión del T-12 — 9 de octubre de 2026

Revisión exhaustiva, fila por fila, de `03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md` (645 filas, 5 columnas de las Bases Administrativas). Ejecutada en seis lotes con gpt-6-luna (esfuerzo xhigh), más una pasada de coherencia entre filas equivalentes; integración y validación por Claude.

## Archivos

| Archivo | Contenido |
| --- | --- |
| `A1_informe.md` | RF-01.01 a RF-14.06: cambios, componentes sin versión, declaraciones faltantes con sección destino y borrador, incoherencias en otros documentos. |
| `A2_informe.md` | RF-14.01-BTT a RNF-23.04: ídem. |
| `B1_informe.md` | RT-02 a RT-07. |
| `B2_informe.md` | RT-08 a RT-12. |
| `B3_informe.md` | RT-13 a RT-17. |
| `B4_informe.md` | RT-18 a RT-26. |
| `informe_coherencia.md` | Pares Parte A / Parte B con la misma materia y su estado final. **Prevalece sobre los informes de lote** cuando el estado de una fila difiere. |
| `informe_aplicacion_7RT.md` | Aplicación posterior de siete RT obligatorios en SD4 y actualización de RF-18.02; verificaciones, dependencias e impactos. **Prevalece para esas ocho filas sobre la revisión anterior.** |
| `propuestas_SD4_RT.md` | 21 propuestas sin aplicar: siete obligatorias, una según caso y trece deseables, con borradores e impactos. |

## Criterios aplicados

- Parte A: un RF/RNF se acredita con su fila del catálogo (resultado esperado y criterio, Anexo 3.J), el módulo responsable del SD4 (4.1.4.x, Anexos 4-D y 4-E) y el soporte concreto que necesita (dato en SD5, interfaz, dispositivo, regla). Es parcial sólo si falta ese soporte o hay contradicción.
- Parte B: se descompone cada RT en sus elementos exigibles; cumple sólo si la propuesta desarrolla todos, incluido el valor del Caso cap. 15.
- Parciales con «Falta: …»; no cumple con «— (sin componente acreditado). Falta: …». Versiones sólo si la propuesta las declara (SD4-Anexos 4-P, T-11).
- Ajuste posterior de Claude: RT-15.03 a parcial (el T-14 programa informes futuros; la BTT exige la estimación y la metodología en la oferta).

## Resultado

- Parte A: 197 Cumple, 69 parciales y 5 no cumple. Parte B: 215 Cumple, 106 parciales y 53 no cumple.
- Tras la aplicación documentada en `informe_aplicacion_7RT.md`: Parte A sin cambio de estados (197/69/5); Parte B 222 Cumple, 106 parciales y 46 no cumple. Los estados de los informes anteriores son antecedentes; las 21 propuestas no alteran el T-12.
- Obligatorios o «según caso» en No cumple: 32 antes de la aplicación; 25 después (RT-13.05, 13.09, 16.04, 16.08, 16.12, 16.18, 16.19, 16.33, 21.02, 21.08, 21.13, 21.16, 23.05, 23.06, 24.01, 24.02, 24.04–24.06, 25.02, 25.04–25.07, 25.09). Los siete aplicados (RT-06.25, 08.17, 08.18, 13.02, 13.10, 13.11, 16.25) quedaron en Cumple.
- Las declaraciones faltantes de los informes de lote fueron redactadas antes de la pasada de coherencia; confirmar el estado vigente en el T-12 antes de usarlas.
