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
| `informe_aplicacion_7RT.md` | Primera aplicación de siete RT y RF-18.02; segunda aplicación: 14 RT y cinco RF; tercera aplicación: cuatro RT y ajuste parcial de RF-18.01. **La tercera aplicación prevalece para sus cinco filas.** |
| `propuestas_SD4_RT.md` | Decisiones actuales para 21 RT: 18 aplicados y tres no aplicados por decisión del usuario. |

## Criterios aplicados

- Parte A: un RF/RNF se acredita con su fila del catálogo (resultado esperado y criterio, Anexo 3.J), el módulo responsable del SD4 (4.1.4.x, Anexos 4-D y 4-E) y el soporte concreto que necesita (dato en SD5, interfaz, dispositivo, regla). Es parcial sólo si falta ese soporte o hay contradicción.
- Parte B: se descompone cada RT en sus elementos exigibles; cumple sólo si la propuesta desarrolla todos, incluido el valor del Caso cap. 15.
- Parciales con «Falta: …»; no cumple con «— (sin componente acreditado). Falta: …». Versiones sólo si la propuesta las declara (SD4-Anexos 4-P, T-11).
- Ajuste posterior de Claude: RT-15.03 a parcial (el T-14 programa informes futuros; la BTT exige la estimación y la metodología en la oferta).

## Resultado

- Parte A: 197 Cumple, 69 parciales y 5 no cumple. Parte B: 215 Cumple, 106 parciales y 53 no cumple.
- Primera aplicación: Parte A 197/69/5; Parte B 222/106/46. Segunda aplicación: Parte A 199/69/3; Parte B 236/106/32. Tercera aplicación vigente: Parte A **199 Cumple, 69 parciales y 3 No cumple**; Parte B **240 Cumple, 106 parciales y 28 No cumple**. Se mantienen 645 filas, cinco columnas, IDs y descripciones intactos.
- Obligatorios o «según caso» en No cumple: 32 antes de la primera aplicación, 25 después, 19 tras la segunda y **17 tras la tercera** (RT-21.02, 21.08, 21.13, 21.16, 23.05, 23.06, 24.01, 24.02, 24.04–24.06, 25.02, 25.04–25.07, 25.09). Los 18 RT aplicados de `propuestas_SD4_RT.md` están en Cumple; RT-05.24, RT-15.05 y RT-16.26 permanecen No cumple por decisión del usuario.
- Las declaraciones faltantes de los informes de lote fueron redactadas antes de la pasada de coherencia; confirmar el estado vigente en el T-12 antes de usarlas.
