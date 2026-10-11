# Revisión cruzada del Formulario T-12 — 11 de octubre de 2026

Revisión fila a fila de las 645 filas del T-12 (271 de la Parte A y 374 de la Parte B) contra las Bases y contra los subdocumentos citados. Documento de trabajo; no es entregable.

## Método

1. **Correspondencia con las Bases (mecánica, 645 filas).** Cada RT de las BTT tiene exactamente una fila en la Parte B y su descripción contiene literalmente el texto de las BTT; los 26 valores del Caso 02, cap. 15, aparecen en la fila de su código. Cada RF/RNF de la Parte A coincide por ID con los Anexos 3.A y 3.B del SD3 y con los catálogos consolidados.
2. **Descripción de la Parte A frente al SD3.** Se comparó el texto de cada fila con la tabla de origen del SD3.
3. **Secciones citadas.** Se resolvió cada cita (sección, tabla, anexo, paquete o ficha) contra los encabezados y tablas de los 31 documentos.
4. **Evidencia semántica.** Parte B: por cada RT se leyeron las frases que lo citan en SD1, SD4, SD4-Anexos, SD5, SD5-Anexos, SD6, SD9, SD13, T-9, T-11, T-13, T-14, T-15 y T-18, y se contrastaron con la descripción y con la columna «Componente». Parte A: lectura completa de SD4 4.1.4 y SD5 5.1, y búsqueda dirigida en SD4/SD5 y sus anexos de cada mecanismo exigido por la descripción.
5. **Sentido inverso.** Las 31 filas parciales o «No cumple» se contrastaron con los subdocumentos para detectar cobertura no reconocida.

Codex no participó: los 14 frentes de lectura fallaron por límite de uso.

## Resultado

Ninguna fila cambia de estado. Conteo vigente: 614 Cumple, 13 parciales, 18 No cumple (Parte A 271/0/0; Parte B 343/13/18). El Anexo 9.C del SD9 sigue sincronizado (0 diferencias), por lo que no hay arrastre a SD3 3.2, SD9 9.2.3, T-13 ni la planilla.

### Hallazgos corregidos

| Tipo | Filas | Corrección |
| --- | --- | --- |
| Descripción distinta del SD3 | RF-03.11, RF-03.12, RF-09.06, RF-18.01 | Texto del T-12 igualado al de la Tabla 3.A.1/3.A.3. RF-18.01 exigía firma avanzada en el acuse, contradiciendo la firma simple del receptor persona natural (SD4 4.1.17). |
| Tabla citada inexistente | RT-06.06, RT-19.09 | SD6 no tiene Tablas 6.3 ni 6.5: se citan SD6-Anexos 6.B (Tabla 6.B.1) y T-9 sección 3, que contienen la evidencia. |
| Cifra del componente errónea | RT-05.01 | 111 entidades / 791 atributos → 121 / 987, como declara SD5-Anexos 5-A; resúmenes del SD5 corregidos. |
| Contradicción de catálogo | RF-08.02 | SD5-Anexos sólo admitía REINGRESO, MERMA y DESTRUCCION; se agregan VENTA_DESCUENTO y DEVOLUCION_PROVEEDOR (5-A y 5-C). |
| Contradicción de oportunidad | RF-12.09, RF-12.13, RNF-12.03 | El SD4 enviaba el ASN «junto con» el acuse tras la descarga; RF-12.09 lo exige al cargar el camión. SD4 4.1.17.1, RNF-12.03 (SD3-Anexos 3.A.5b y T-12) y sus componentes separan ambos envíos. |
| Componente que no responde la exigencia | RF-07.08 (describía Transbank), RF-12.07 (MDN de transporte), RT-21.07 y RNF-21.04 (24×7 sólo «en la ventana de despacho», cuando D-10 atiende críticos y altos 24×7×365) | Componente reescrito con el mecanismo correcto. |
| Mecanismo exigido sin desarrollo en ningún subdocumento | RF-01.01, 01.03–01.06; RF-02.04, 02.09, 02.11; RF-03.04–03.10, 03.13, 03.14; RF-04.02, 04.05; RF-05.01, 05.02, 05.05, 05.07; RF-06.01, 06.14; RF-07.03, 07.06, 07.08, 07.10; RF-08.01, 08.02, 08.04, 08.06; RF-09.07; RF-11.01, 11.02, 11.04, 11.08; RF-12.07, 12.08, 12.10, 12.11; RF-14.02, 14.03, 14.06; RNF-01.01, 03.03, 07.02, 08.01 | Una o dos frases por módulo en SD4 4.1.3.7, 4.1.4.3–4.1.4.8 y 4.1.17.1 (y evento de desvío en SD4-Anexos 4-A), reutilizando módulos, terminales e integraciones existentes; componente y sección del T-12 actualizados. |
| Respuesta incompleta a código de doble significado | RT-03.13, RT-03.24, RT-05.15 | El componente declara ahora también el valor del Caso 02 (10 min / 2 h; estudio de cobertura dentro de cámaras; alcance de migración). |
| Coherencia entre RF del catálogo | RF-03.09 frente a RF-07.05 | Se distingue el cliente ya bloqueado (mora > 30 días o deuda sobre el cupo, RF-07.05) del pedido que lleva la deuda sobre el límite (alerta) o sobre 110 % (bloqueo con aprobación de supervisor). |
| Referencias del T-12 | — | «Subdocumentos 1–8 y 13» → «1–9 y 13», porque la matriz cita SD9, T-13 y T-17. |

### Filas no «Cumple» (sentido inverso)

Las 31 filas mantienen su estado. Ninguna tiene cobertura completa no reconocida: video (RT-24) y prototipo (RT-25) quedan para la propuesta final; huella de carbono, certificaciones y datos corporativos esperan datos reales; los Deseables RT-05.24, RT-15.05, RT-16.26, RT-18.10 y RT-21.12 no están ofertados en ningún subdocumento (SD5-Anexos declara expresamente RT-05.24 «No ofertado»).

## Pendientes que no son cambios simples

1. **Cámara del MC9400 (RF-01.04).** La no conformidad exige una fotografía capturada con el terminal de recepción; el T-11 (C-03) no declara la configuración de cámara del MC9400. Confirmar la variante con cámara trasera en la ficha del fabricante antes de afirmarlo en el T-11.
2. **Modelo de datos del SD5.** El estado «En revisión» de los pagos informados en el portal (RF-07.08), el umbral de envases por cliente (RF-08.04) y la tarifa de peajes por ruta (RF-11.02) están comprometidos en SD4 pero no tienen atributo propio en el diccionario 5-A.
3. **LaTeX.** El T-12, SD4 (4.1.3.7, 4.1.4.x, 4.1.17.1), SD4-Anexos 4-A, SD5-Anexos 5-A/5-C y SD3-Anexos (RNF-12.03) cambiaron después de la sincronización LaTeX de esta madrugada.
4. **Declaración de IA del SD3.** La columna de revisión humana dice «No documentada.»; la regla del equipo usa `[[REVISIÓN HUMANA]]` mientras falte la revisión.
