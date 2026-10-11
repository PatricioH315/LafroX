# Revisión de la Comisión Evaluadora — Subdocumento 13 (Informe 2)

Aplicación de `Revision/prompt_revision_comision_informe2.md` al ítem 13 sobre las fuentes Markdown consolidadas. La evidencia se cita por archivo y sección. Las comprobaciones de paginación, folio, firma, tamaño tipográfico, legibilidad y nomenclatura del PDF quedan pendientes de la compilación de los PDF finales.

---

LAFROX · GRUPO 2 · INFORME 2 · Caso 2 · Distribuidora Puelche S.A.

Archivos recibidos: `LAFROX-Subdocumento13.md`, `LAFROX-Subdocumento13-Anexos.md`, `LAFROX-Formulario-T-19.md`. Los tres siguen el patrón de nomenclatura de la Aclaración §1 (en Markdown; la extensión `.pdf` se verifica en la entrega).

Documentos revisados: Subdocumento 13 (805 líneas, 12.435 palabras, 29 tablas, 1 figura), Anexos del Subdocumento 13 (156 líneas, 6 tablas), Formulario T-19 (163 líneas, 5 fichas de 17 campos). El número de páginas no es verificable en Markdown.

## CORRECCIONES DEL INFORME 1

La tabla de trazabilidad existe (Anexos, Anexo 13.D, Tabla 13.D.1) y cubre nueve observaciones. Se muestrearon las nueve contra el texto:

| Observación del Informe 1 (S13) | Estado | Evidencia |
| --- | --- | --- |
| Ningún precio | Corregido | Impacto por rubro, clase y mes, sin montos (13.1.5 a 13.5.5; T-19, campos 10 a 12). |
| Innovación 1 coincidía con un requisito | Corregido | 13.1.2, Tabla 13.2: separa RF-02.09 (alerta en bodega) y la meta de merma; mide «vencimiento posentrega» (I-01B). |
| Innovación 3 coincidía con un requisito | Corregido | 13.3, primer párrafo: «El registro continuo de temperatura en cámaras y vehículos es alcance obligatorio (criterio 3 del caso) y no es la innovación». |
| Innovación 5 debe funcionar sin internet | Corregido | 13.5.2: hoja en pantalla sin señal o impresa en la entrega siguiente, sin dispositivo ni registro. |
| Fichas T-19 con los siete elementos | Corregido | T-19, Fichas 1 a 5, 17 campos en el orden del formulario de las Bases Administrativas. |
| Arquitectura, EDT, flujo de caja, indicador, línea base, meta y mes | Corregido | Subsecciones 13.N.4 a 13.N.6; Anexo 13.B, Tablas 13.B.1 y 13.B.2. |
| Fuentes APA en el texto y vigentes (EPCIS 2.0) | Corregido | 13.3.2: «(GS1 AISBL, 2022)»; correspondencia 1:1 entre 16 citas y 16 referencias. |

Resultado: 7 de 7 puntos de la lista de control del Informe 1 para S13 corregidos; 0 parciales; 0 no corregidos. Sin regresiones detectadas.

## 13. Innovaciones — Formulario T-19 (10 %)

13.1 Innovación 1 (producto o servicio) · 13.2 Innovación 2 (proceso) · 13.3 Innovación 3 (tecnológica o de arquitectura) · 13.4 Innovación 4 (modelo de negocio o de contratación) · 13.5 Innovación 5 (UX, sostenibilidad o impacto social).

**Revisión: (Puntaje 0 en el estado actual; 60 una vez completada la revisión humana)**

**Veredicto:** el subdocumento queda en 0 mientras conserve 13 celdas `[[REVISIÓN HUMANA]]` en sus tres archivos, porque son cuadros de aprobación en blanco (Aclaración §7.1; Paso 1, punto 2). El contenido técnico es sólido: cinco innovaciones, una por tipo, con los siete elementos del Art. 29°, trazadas a módulos y componentes del Capítulo 4 y a 23 paquetes de la EDT (16 en la cuenta 3.10, uno en 5.4.3 y seis en 8.3). Completada la revisión humana, el ítem cae en 60: la única figura es la 13.1, frente a 29 tablas en el cuerpo.

### Introducción

- OK - Texto de introducción bajo el título del capítulo que conecta con arquitectura, EDT, riesgos, flujo de caja, anexos y T-19 (Subdocumento 13, «Introducción a las Innovaciones»).
- OK - Tabla 13.1 de la cartera con tipo, problema y mes de materialización; los meses coinciden con la Tabla 7.D.1 del Anexo 7.D.
- OK - La Figura 13.1 está citada antes, dibujada y explicada después; ubica las cinco innovaciones en las capas 1, 2, 4, 5, 6, 7 y 8 con los nombres del Capítulo 4 (C-01 App de preventa, C-02 App de reparto, C-03 Terminales de bodega, N-10 Plataforma analítica).
- La Figura 13.1 está en Mermaid. El PDF debe llevarla como imagen legible a ≥ 9 pt; hoy no existe un archivo de imagen asociado (Aclaración §4 y §7.1 a).

### 13.1 Innovación 1

- OK - Primer párrafo con tipo y nombre: «Tipo 1, producto o servicio: Seguimiento de vencimiento posentrega en el local (INN-01)».
- OK - Problema dimensionado con el caso: merma de 1,7 % (Caso 02, cap. 4.8) y entrevista a Sandra Riffo (cap. 8).
- OK - Deslinde con lo obligatorio (Tabla 13.2): RF-05.05, RF-02.09, RF-02.08, RF-08.05, RF-03.14, RF-02.10 y RF-01.03 existen en el T-12 con ese contenido.
- OK - Investigación adicional declarada (13.1.3) con paquete y mes: 3.10.1.2 y 3.10.1.4.
- I-01B e I-01C toman su línea base en la marcha blanca; la meta relativa (−25 %, −20 %) se declara como propuesta, sin cálculo que la derive. El grupo debe poder justificarla en la presentación.

### 13.2 Innovación 2

- OK - Separa el circuito de las pruebas obligatorias (RT-10.07, RNF-20.04, RT-14.06) y justifica por qué no es práctica estándar (13.2.2, «Por qué no es práctica estándar»).
- OK - Respeta los cinco ambientes del RT-04.01: «No es un sexto ambiente».
- OK - Verificable antes del mes 16 (I-02A e I-02B en el mes 15), base del RT-26.08 en el T-12.
- La innovación oferta además el RT-04.14 (deseable). Lo propio de la innovación es el cierre por reproducción; el texto lo deja claro, pero el evaluador puede preguntar dónde termina el RT-04.14 y dónde empieza la innovación.

### 13.3 Innovación 3

- OK - Modelo determinista declarado con variables, métrica, línea base y recalibración (Tabla 13.13), coherente con RT-05.30 y RT-18.08 del T-12.
- OK - Volumen reutilizado: 21 × 288 + 28 × 174 = 6.048 + 4.872 = 10.920 mensajes diarios, igual al Anexo del Capítulo 4.
- OK - Regla asimétrica: la estimación puede acortar la vida útil, nunca alargarla más allá de la fecha impresa.
- OK - Revisiones semestrales de los meses 32, 44 y 56, que caen en septiembre con inicio en febrero de 2027, activan parámetros después del día 25, fuera del congelamiento (Caso 02, cap. 10, restricción 8).
- La exposición es 20 (crítica) en R8-27 y R8-23. Está mitigada, pero es la mayor de la cartera y concentra la pregunta sanitaria.

### 13.4 Innovación 4

- OK - Escala TRL aplicada a la práctica contractual con un hito verificable por nivel (Tabla 13.19).
- OK - Sin montos: «Los valores se fijan solo en la Oferta Económica».
- OK - Protección del OTIF con el tramo de 95 % del criterio R18-04 (Capítulo 3, sección 3.2.5).
- La cita «cuarenta y cinco mil pesos» (13.4.1) es dato del caso, no un precio de la oferta; no infringe el Art. 50.2. Se recomienda mantenerla como cita textual atribuida.

### 13.5 Innovación 5

- OK - Funciona sin internet ni dispositivo del cliente (Caso 02, cap. 10, restricción 5).
- OK - Bloque 4 condicionado a dictamen legal bajo la Ley 21.719, con umbral y supresión (Hundepool et al., 2026; Sweeney, 2002).
- OK - I-05C no promete alza: «la meta es estimar el efecto».
- El beneficio comercial se valoriza recién al mes 33; el beneficio social es cualitativo. Es coherente con la evidencia, pero es la innovación con impacto menos cuantificado.

### Correcciones del Informe 1

- OK - Las siete observaciones de S13 están corregidas y la Tabla 13.D.1 apunta a secciones que existen y dicen lo que la tabla afirma.

### Consistencia

- OK - Nombres y códigos INN-01 a INN-05 idénticos en T-12, SD5, SD7 y Anexo 7.D, T-14, SD8, Anexo 8.A, T-16, SD9 y T-13.
- OK - Paquetes y meses idénticos al T-14 y al Anexo 7.D; riesgos R8-23 a R8-29 con la misma probabilidad e impacto que el Anexo 8.A y el T-16.
- OK - Responsables y dedicaciones iguales a la Tabla 1.3 del Capítulo 1.
- OK - Herramientas (GitLab CI, Terraform, PHPUnit, PHPStan, OpenTelemetry, CloudWatch, Greengrass) presentes en el Capítulo 4 y en el Formulario T-10.
- Diferencias de redacción sin contradicción: INN-05.P4 «18 a 21 y 22 a 26» (SD13) frente a «18 a 26» (Anexo 7.D); INN-03.P5 «26, 32 … 56» frente a «cada seis meses, 21 a 56».

### Forma e indicios de uso de IA

- Crítico: 13 celdas `[[REVISIÓN HUMANA]]` (8 en el cuerpo, 4 en los anexos, 1 en el T-19). En el régimen del Informe 2 dejan el subdocumento en 0 hasta que un integrante registre qué verificó (Aclaración §7.1).
- OK - Sin marcadores, notas de versión, nombres de archivo como fuente ni referencias a documentos inexistentes.
- OK - Ningún título seguido directamente de tabla, lista o figura; índice enlazado en los tres archivos.
- OK - Cierre con «Referencias» y «Declaración de uso de IA» en los tres archivos; 16 citas y 16 referencias con correspondencia 1:1 en el cuerpo.
- Una figura frente a 29 tablas en el cuerpo. Un capítulo técnico sin diagramas por innovación queda expuesto a la observación de la Aclaración §4.

### Qué se espera en el Informe 3

- Completar las 13 celdas de revisión humana con el nombre del integrante y lo verificado.
- Exportar la Figura 13.1 como imagen para el PDF, legible a ≥ 9 pt.
- Agregar al menos un diagrama de recorrido por innovación (por ejemplo, el circuito de INN-02 o el flujo de datos de INN-03).
- Valorizar las cinco innovaciones en el flujo de caja de la Oferta Económica (T-22, Informe 3), con los mismos rubros, clases y meses de las Tablas 13.4, 13.9, 13.15, 13.21 y 13.26.
- Justificar las metas relativas de I-01B, I-01C, I-02A e I-03D con un cálculo o una fuente.

## CONSIDERACIONES TRANSVERSALES

- **Consistencia técnica:** sin contradicciones de decisión entre el SD13 y los Subdocumentos 1, 3, 4, 5, 7, 8 y 9 ni sus formularios.
- **Trazabilidad:** INN-03 se sigue de punta a punta: problema (Caso 02, cap. 4.9) → requerimientos base (RF-09.03 a RF-09.10) → componentes (B-01, B-02, B-03, N-06, N-08, N-10, M9) → dato (Capítulo 5, sección 5.1.7) → paquetes 3.10.3.1 a 3.10.3.4 y 8.3.2 → riesgo R8-27 → indicador I-03B. No se corta.
- **Fundamentación ingenieril:** el deslinde con lo obligatorio en cada innovación y la regla asimétrica de INN-03 son las decisiones más defendibles.
- **Uso de IA:** el único indicio es la revisión humana sin completar.
- **Compliance:** sin precios, sin plazos distintos del Art. 17°; folio y firma se verifican en el PDF.

| Ítem | Peso | Puntaje | Ponderado |
| --- | --- | --- | --- |
| 13. Innovaciones — Formulario T-19 (estado actual) | 10 % | 0 | 0,0 |
| 13. Innovaciones — Formulario T-19 (con revisión humana completa) | 10 % | 60 | 6,0 |
