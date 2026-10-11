# LafroX — Diferencias Markdown vs LaTeX, Subdocumentos 1 a 3

Revisión del 10 de octubre de 2026. Se compara el árbol de trabajo de `rama-md` (incluye los cambios sin commit del T-12 y del SD3-Anexos) con las ramas `origin/LafroX-Subdoc1-LateX` (17995de, 08-10 22:26), `origin/LafroX-Subdoc2-LateX` (8c693bc, 08-10 23:13) y `origin/LafroX-Subdoc3-LateX` (35a8262, 09-10 17:19). Solo lectura con `git show`: no se hizo checkout ni se creó o editó ningún archivo LaTeX.

**Método.** Ambos lados se normalizaron a texto plano: párrafos, ítems y filas de tabla, con `\input` resueltos. Luego se alinearon con difflib y se compararon palabra a palabra. Se descartaron como ruido el espacio fino en porcentajes (`80%` frente a `80 %`), `\,°C`, las referencias `\ref` y los artefactos de maquetación (longtable, colspec, encabezados de continuación). Los únicos insumos LaTeX activos son `contenido.tex`, `anexos.tex` (con `tablas_anexo/*`) y los `LAFROX-Formulario-*.tex`. Las carpetas `tablas/` de SD1, SD2 y SD3 no se incluyen en ningún documento y son restos.

## Resumen

| Documento | Estado | Diferencias de contenido |
|---|---|---|
| SD1 cuerpo | MD más nuevo | 9 cambios de texto, 3 párrafos solo en MD, Referencias y declaración de IA |
| SD1 anexos | **Solo existe en LaTeX** | El MD no tiene `LAFROX-Subdocumento1-Anexos.md` |
| T-6 | Equivalentes | Solo maquetación (`<br>` en contactos, espacio en %) |
| SD2 cuerpo | Casi iguales | 4 diferencias menores, 1 cita sin autor en MD y orden de Referencias |
| SD2 anexos | Equivalentes | Solo formato |
| SD3 cuerpo | MD más nuevo | 4 párrafos con cambios o agregados (conteo 259/261, S-41→S-44, mesa de servicio) |
| SD3 anexos | MD más nuevo | 36 filas RNF con otra «Verificación prevista», Tabla 3.A.4a y S-42 a S-44 solo en MD |
| **T-12** | **LaTeX obsoleto y con otra estructura** | 645 IDs en ambos, pero otro formato de columnas, otra escala de cumplimiento y 94 filas con compromiso distinto (más RT-26.06) |

Conclusión: el LaTeX de SD1–SD3 refleja el estado del 8 y 9 de octubre. Todo lo que cambió después en `rama-md` (commits `c74b783` en adelante: cierre de brechas del T-12, SOC propio, RT-13.04 y supuestos S-42 a S-44) no llegó al LaTeX. La brecha mayor es el T-12.

---

## Subdocumento 1

### Cuerpo (`contenido.tex` frente a `LAFROX-Subdocumento1.md`)

Contenido que solo está en el MD o que el MD amplía:

1. **Sitio web corporativo** (párrafo después de los hitos de la trayectoria, RT-23.01 a RT-23.10, `https://lafrox.github.io/`). Solo MD.
2. **Centro de Operaciones** (ítem de capacidad instalada): el MD agrega «Centro de Operaciones de Seguridad (SOC)» y la ubicación «en el Centro de Operaciones de LafroX en Valparaíso (Av. Brasil 2241)».
3. **Tabla 1.1**: el MD agrega «(Valparaíso)» en la ubicación de las filas NOC (32) y SRE/Cloud (12). En LaTeX dicen solo «Centro de Operaciones».
4. **Párrafo tras la Tabla 1.1**: el MD agrega que el centro aloja el puesto SOC 24×7 propio, bajo el Encargado de Seguridad de la Información.
5. **1.3.1 Calidad**: párrafo nuevo solo en MD («Los métodos de diseño… RUP y DevSecOps… RT-23.04»).
6. **DevSecOps**: el MD agrega la frase sobre la cadencia semestral frente al mínimo de RT-11.20.
7. **1.3.2 Seguridad**: párrafo nuevo solo en MD sobre pruebas de intrusión por tercero independiente (RT-11.20).
8. **Certificaciones con vencimiento**: el MD agrega la renovación ante la Contraparte Técnica en H1 y la remisión a SD9 9.1.2. También cambia `art. 34` por `Art. 34°`.
9. **1.5 Estructura para Proyecto**: dos párrafos solo en MD, uno sobre las facultades del JP (RT-19.02) y otro sobre la continuidad de certificaciones y el reemplazo (RT-15.09, BA Art. 76°).
10. **Tabla 1.2**: `secciones 2.2-2.4` (LaTeX) frente a `secciones 2.2 a 2.4` (MD).
11. **Declaración de IA (Tabla 1.4)**: en las filas 1.3 y 1.5 el MD agrega «OpenAI Codex» y nuevas finalidades.
12. **Referencias**: el MD agrega «LafroX. (2026). Subdocumento 6: Metodologías». **Falta en ambos** la entrada del SD9, que el MD ahora cita («LafroX, 2026, Subdocumento 9, sección 9.1.2»). Además, con dos obras LafroX del mismo año, el MD debería distinguir 2026a y 2026b.

Diferencias de forma:

- El MD tiene portada, índice con números de página y listas de tablas y figuras escritos a mano. La fecha de emisión dice «05 de octubre de 2026» y los números de página no se pueden verificar. LaTeX los genera.
- **Figura 1.1**: el LaTeX incluye `figuras/Figura 1.1.pdf`. El MD tiene la leyenda y la «Descripción de imagen» **sin la imagen enlazada**, ubicada además antes de la leyenda. Es el hallazgo RI-11 vigente (Aclaraciones §7.1 a).

### Anexos

- LaTeX: `LAFROX-Subdocumento1-Anexos.tex` declara que el SD1 no tiene anexos, remite al T-6 y a las cartas del art. 34, e incluye Referencias.
- MD: **no existe** `01_presentacion_empresa/LAFROX-Subdocumento1-Anexos.md`. Falta decidir si el entregable de anexos del SD1 se emite. Si se emite, el MD queda incompleto.

### Formulario T-6

Contenido equivalente. Solo cambian los saltos `<br>` en la fila de contactos y la portada o índice manual del MD.

## Subdocumento 2

### Cuerpo

1. **Cita sin autor (defecto del MD)**: el MD dice «(2026c, anexo B.2)» y el LaTeX «(Distribuidora Puelche S.A., 2026c, anexo B.2)». Hay que corregir el MD.
2. **Entrevistas**: LaTeX dice «entrevistas a los actores clave descritas en el caso» y el MD «entrevistas del caso».
3. **Cross-docking**: LaTeX dice «cap. 6» y el MD «capítulo 6». En el resto del documento se usa «cap.».
4. **Referencias**: en el MD, «Ministerio de Salud (1996)» queda antes de «Ley N.º 21.719». El orden alfabético APA es el del LaTeX (Ley, luego Ministerio).
5. **Figuras 2.1–2.6**: el LaTeX las incluye. El MD usa enlaces `[Ver Figura 2.x](<figuras/figura 2.x.pdf>)` hacia una carpeta `figuras/` **que no existe** en `02_problema_necesidad/` (enlaces rotos, RI-11). Solo el LaTeX trae la nota «Fuente: elaboración propia. Transcripción textual de la figura original.» después de cada transcripción.
6. **Tabla 2.4 (IA)**: los encabezados son «Texto / Diag. / Revisión humana» en LaTeX y «Nivel en texto / Nivel en diagramas / Revisión humana (quién y qué verificó)» en el MD.
7. El ítem «Pérdida de competitividad» está partido en dos párrafos en el MD. El texto es idéntico.

### Anexos

Las nueve tablas (2.A.1 a 2.A.9) tienen las mismas filas y el mismo texto. Solo difiere el formato de porcentajes.

## Subdocumento 3

### Cuerpo

1. **Supuestos**: el LaTeX dice «El Anexo 3.C registra 41 supuestos» y el MD «44».
2. **Catálogo y correspondencia** (sección del catálogo): el MD agrega un párrafo completo sobre las 271 filas de la Parte A, que son 261 + 10 alias o absorbidas, y la conciliación 259 con prueba, 9 absorbidas y 3 «No cumple» (RF-07.11, RNF-21.02, RNF-21.07). El LaTeX habla de «catálogo ofertado».
3. **Prioridades**: el MD agrega la distribución de los 259 ofertados (56/160/43) y redefine qué registra el T-12. Las cinco columnas se mantienen. La prueba queda en SD9 9.C y el criterio en el T-17. El LaTeX dice que el T-12 responde «con componente, sección, prueba prevista y criterio de aceptación», lo que contradice el T-12 MD.
4. **3.4.5 Servicio**: dos párrafos solo en MD (canal único RT-21.15/RNF-21.06 y mesa N1/N2/N3 RT-21.08), antes de la Tabla 3.5.
5. **Tabla 3.6 (IA)**: en la fila 3.4 el MD agrega «registro de solicitudes en el canal único de servicio».
6. **Figuras 3.1–3.8**: el LaTeX incluye las ocho, incluida «Diagrama de la solución.pdf». El MD tiene las ocho leyendas **sin imagen enlazada** (RI-11).

### Anexos

1. **Totales**: el MD agrega «De ellos se ofertan 259…» (3.A) y «se ofertan 84» (3.B).
2. **Tabla 3.A.4a** (indicadores de usabilidad por perfil, RT-13.04) y su párrafo introductorio: **solo MD**.
3. **«Verificación prevista» distinta en 36 filas RNF**. El LaTeX conserva textos genéricos («Prueba funcional con datos representativos en marcha blanca», «Ejercicio de recuperación con medición de RTO/RPO», «Prueba de desempeño con volumen de peak»). El MD tiene la verificación específica de cada requisito. Filas: RNF-12.01, 03.01, 05.01, 07.01, 04.01, 11.02, 13.03, 13.04, 13.06, 13.07, 14.01, 14.03, 14.05, 14.07–14.10, 15.03, 16.01, 17.02, 17.03, 19.04, 20.01, 20.04, 20.06, 20.07, 21.02–21.04, 21.07, 22.02–22.06 y 12.03. En el LaTeX hay incoherencias evidentes: RNF-21.02 (gerente de servicio) aparece con «prueba funcional» y RNF-22.02 (material de capacitación) con «ejercicio de recuperación RTO/RPO».
4. **Supuestos S-42, S-43 y S-44**: solo MD. El párrafo del Anexo 3.C dice «S-17 a S-41» en LaTeX y «S-17 a S-44» en el MD.
5. **Anexo 3.J**: el MD agrega que el T-12 no registra pruebas ni criterios.
6. **Tabla 3.A.15 (IA)**: en la fila 3.C el MD agrega S-42 y S-43.
7. Las demás tablas (3.A.1, 3.A.2, 3.A.3, 3.A.3a/b, 3.A.5, 3.A.5a/b, 3.A.6 a 3.A.14, 3.A.12a y 3.A.13) coinciden fila por fila.

### Formulario T-12 (diferencia mayor)

| Aspecto | LaTeX (35a8262) | MD (árbol de trabajo) |
|---|---|---|
| Columnas Parte A | 9: ID, Requerimiento (truncado con «…» en 165 filas), Cumple, Componente, EDT, Prueba, Sección, Criterio, Origen | 5: ID requerimiento, Descripción completa, Cumple, Componente que lo satisface, Sección de la propuesta |
| Columnas Parte B | 7, una tabla por capítulo: Código, Exigencia, Carácter, Cumple, Componente, Sección, Evidencia | Una tabla con las mismas 5 columnas |
| Escala | Sí (E1), Sí (E2), Sí (E1 y E2), Sí (licitación), Sí (alias), Absorbido por…, No aplica, No ofertado, Sí, condicionado | Cumple, Cumple parcialmente, No cumple |
| Totales | RF Sí 175 + 6 no ofertadas o absorbidas; RNF 86 Sí o alias + 3 absorbidas; RT 326 Sí, 38 No ofertado, 9 No aplica, 1 condicionado | 588 Cumple, 34 parciales, 23 No cumple |
| EDT | «Paquete por asignar en el plan de trabajo» en 262 filas | No existe la columna |
| Caso cap. 15 | No incorporado | 26 filas RT con el alcance del caso en la descripción (por ejemplo RT-21.06 con el horario 04:00–22:00) |
| Convenciones, Referencias, IA | Sección «Convenciones», 6 referencias (LafroX 2026a/b/c), tabla de IA T12.27 | Párrafo de escala, 4 referencias, declaración de IA en prosa con `[[REVISIÓN HUMANA]]` |

Mismos 645 IDs en ambos, sin faltantes ni duplicados. **94 filas cambian de compromiso** (más RT-26.06, que cambia de etiqueta):

- **LaTeX «Sí» → MD «Cumple parcialmente»** (31): RF-01.08, 01.10, 01.11, 02.01, 02.03, 02.07, 02.08, 03.12, 04.01, 04.03, 07.03, 07.04, 07.06, 08.07, 11.05, 18.03; RNF-21.08; RT-08.04, 15.02, 15.03, 15.04, 15.07, 15.08, 16.14, 16.23, 21.03, 21.19, 23.03, 25.01, 25.03 y 25.08.
- **LaTeX «Sí» → MD «No cumple»** (15): RNF-21.02, RNF-21.07, RT-21.02, RT-21.16, RT-24.01, 24.02, 24.04, 24.05, 24.06, RT-25.02, 25.04, 25.05, 25.06, 25.07 y 25.09.
- **LaTeX «No ofertado» → MD «Cumple»** (28): RT-02.14, 03.08, 03.09, 03.19, 03.24, 04.13, 04.14, 05.30, 06.15, 06.34, 07.14, 08.15, 08.19, 09.10, 10.09, 11.21, 11.28, 12.04, 13.12, 14.09, 15.06, 16.05, 17.08, 23.07–23.10 y 26.08.
- **LaTeX «No ofertado» → MD «Cumple parcialmente»** (3): RT-05.10, 06.12 y 07.08.
- **LaTeX «No ofertado» → MD «No cumple»** (8, sin cambio de fondo): RF-07.11, RT-05.24, 15.05, 16.26, 18.10, 21.12, 24.03 y 25.10, con RF-07.11 como «No ofertado como función independiente».
- **LaTeX «No aplica» → MD «Cumple»** (9): RT-18.01 a RT-18.09. El fondo es el mismo (D-09, sin componentes de IA), pero el LaTeX lo marca «No aplica» y el MD «Cumple».
- **RT-26.06**: «Sí, condicionado» en LaTeX y «Cumple» en el MD.

Descripciones que difieren:

- **RF-03.03 y RF-09.04**: el T-12 LaTeX conserva la versión antigua («sistema de gestión, por orden de llegada»; «propios + de transportistas que cuenten…»). Su propio Anexo LaTeX y el MD ya tienen la versión vigente (servidor central, S-08 y RNG-01; 18 propios y 10 de transportistas, S-28). Es una incoherencia interna del LaTeX.
- **RF-03.11 y RF-03.12**: el **T-12 MD** tiene una redacción distinta de su propio catálogo (SD3-Anexos MD, Tabla 3.A.1) y del LaTeX. El T-12 dice «conservar para todos los pedidos… y transmitirlo al ERP» y «bloquear su confirmación y notificar a Comercial». El catálogo dice «registrar y conservar en cada pedido de preventa… sin modificarlo» y «generar una alerta al responsable comercial». Es una incoherencia interna del MD.
- **RF-13.01 a RF-18.03 y RF-19.0x (BTT)**: el T-12 LaTeX usa solo el título corto. El MD usa la descripción completa.
- **RNF-05.02**: el LaTeX dice solo «Operabilidad con guantes a -22 °C». El MD agrega el umbral (≥ 15×15 mm, sin gestos complejos).

---

## Restos en las ramas LaTeX (no son contenido, pero se publican)

- PDFs compilados versionados en las tres ramas.
- Notas de trabajo `.md` en la raíz: SD1 (`ANALISIS_SUBDOCUMENTO_1.md`, `retroalimentación entrega 1.md`), SD2 (`ESTUDIO_SUBDOCUMENTO_2.md`, `main.zip`, `cropped21-test.png`) y SD3 (9 notas, `_staging_sd3_p13.png`).
- `main.tex` de plantilla con «EJEMPLO_LAFROX_NO_ENTREGAR» y la carpeta `subdocumento-ejemplo/`.
- El encabezado de `LAFROX-Subdocumento3.tex` dice «esta revisión incluye notas de trabajo». Es un comentario y no se imprime.
- SD2 `contenido.tex` define estilos TikZ que no se usan, porque las figuras son PDF.

## Qué queda por decidir

1. **T-12**: el MD es la versión vigente. Hay que decidir si se regenera el T-12 LaTeX desde el MD (5 columnas y escala Cumple/Parcial/No cumple) o si alguna convención del LaTeX (por ejemplo «No aplica» para RT-18) debe volver al MD.
2. **Anexos del SD1**: decidir si se crea el MD equivalente o si se retira el PDF LaTeX.
3. **Corregir en el MD**: la cita «(2026c, anexo B.2)» del SD2, el orden de Referencias del SD2, la referencia SD9 que falta en el SD1 y las descripciones de RF-03.11 y RF-03.12 en el T-12 MD.
4. **Imágenes (RI-11)**: SD1, SD2 y SD3 en Markdown no enlazan imágenes existentes.
