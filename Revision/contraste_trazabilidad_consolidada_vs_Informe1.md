# LafroX — Contraste de la trazabilidad consolidada con la revisión del Informe 1

Nota de trabajo (no entregable). Fecha: 12-10-2026.

- **Fuente contrastada:** `C:\Users\alexa\Downloads\Revision_informe.md`, byte a byte idéntica a [Revision_informe.md](../Revision_informe.md).
- **Tabla contrastada:** [Trazabilidad/LAFROX-Trazabilidad-Informe1-Consolidada.md](../Trazabilidad/LAFROX-Trazabilidad-Informe1-Consolidada.md), 195 filas.
- **Método:** se leyó cada viñeta del informe (identificada por su línea, «L») y se buscó la fila que la responde. Luego se hizo el recorrido inverso: cada fila debe provenir de una viñeta real del informe y reproducirla con fidelidad.
- **Alcance:** se contrastan las observaciones (primera columna). No se auditó si cada respuesta es verdadera en el subdocumento actual.

Leyenda: **✔** coincide · **◐** coincide en parte (falta un elemento de la viñeta) · **✘** ninguna fila la responde.

## Resultado general

- **Recorrido inverso:** las 195 filas provienen de puntos reales del informe. No hay observaciones inventadas ni atribuidas al subdocumento equivocado.
- **Recorrido directo:** de las viñetas del informe, quedan **4 sin ninguna fila** y **10 respondidas solo en parte**; la mayoría pertenece al apartado GENERAL. Además, el SD1 y el SD13 omiten sus valoraciones «OK», que el SD2–SD5 sí conservan.
- **Fidelidad del texto:** **1 fila cambia el sentido** de la viñeta (SD5-06) y **2 filas ponen entre comillas frases que no son literales** (SD3-13 y SD3-36).
- **Páginas del SD4:** las filas SD4 citan páginas («pp. 9–14») de un PDF de revisión que no está en el repositorio. No se pueden cotejar contra el Markdown.

## 1. GENERAL ([L5–L45](../Revision_informe.md))

| L | Punto del informe | Fila(s) | Resultado |
|---|---|---|---|
| 15 | Sin logotipo, plantilla, paleta, encabezado ni pie | SD1-01, SD2-01, SD3-01, SD13-16, SD4-21 | ◐ El SD5 no tiene fila general |
| 16 | 4.2: «LAFROX» no aparece y p. 114 dice «Empresa proponente: Pendiente de definir»; SD3 p. 27 «Razón social… pendiente» | SD3-01 (parte SD3); SD4-23 EF-02 (solo «Cambios v01→v02» de p. 114) | ◐ Ninguna fila del SD4 responde la ausencia de LAFROX ni «Empresa proponente: Pendiente de definir» |
| 17 | Portadas rompen la ficción y se rotulan T-22 | SD1-01, SD2-02, SD3-01, SD13-17; SD4-22 (4.2 sin portada) | ◐ El SD5 no tiene fila |
| 18 | Tres plantillas; Arial y A4 en 1, 2, 3, 5 y 13 | SD1-03, SD2-03, SD3-02, SD13-18, SD4-21 | ◐ El SD5 no tiene fila |
| 19 | Hoja «Página en blanco a propósito» en 3, 4.1, 5 y 13 | SD3-01, SD13-19 | ◐ **4.1 y 5 sin fila** |
| 23 | Sin índice, folio ni firma (Art. 53°) | SD1-02, SD2-04, SD3-02, SD4-22, SD13-20 | ◐ El SD5 no tiene fila |
| 24 | T-6, T-12 y T-19 ausentes; T-11 solo invocado | SD1-07, SD3-18, SD13-12, SD4-37 | ✔ |
| 25 | T-21: el documento resume y el formulario lista; en el 4.2, más de la mitad son tablas de listado | SD1-06, SD2-05, SD3-06 | ◐ **Ninguna fila del SD4 responde lo de «más de la mitad son tablas de listado»** |
| 26 | A4 y cuerpo menor a 11 pt | SD1-03, SD2-03, SD3-02, SD13-18 | ◐ El SD5 no tiene fila |
| 27 | SD2 sin lista de referencias | SD2-30 | ✔ |
| 31 | 4.2 duplicado y título pegado | SD4-22 | ✔ |
| 32 | Seis marcadores «[INSERTAR DIAGRAMA…]» | SD2-31 | ✔ |
| 33 | Diagramas del 4.1 y figura del 4.2 ilegibles (1–2 pt) | SD4-01, SD4-21, SD4-25 | ✔ |
| 34 | Cero figuras en 1, 2, 3, 5 y 13 | SD1-04, SD2-32, SD3-07, SD5-01, SD13-15 | ✔ |
| 35 | Resaltado negro en el SD5 | SD5-17 | ✔ |
| 36 | Columnas angostas que parten palabras, filas cortadas, títulos huérfanos, **páginas semivacías (21 en SD3 y 19 en 4.2)** | SD1-03, SD2-06, SD3-04 | ◐ **Títulos huérfanos y páginas semivacías no tienen fila** (ni en el SD3 ni en el SD4) |
| 37 | Erratas: «próposito», «ventana de 320 minutos» (S3 p. 3), «160 camiones que no son trabajadores» (S3 p. 66), «cinco ambientes» (S1) | SD1-26 (ambientes); SD13-19 («con errata») | ✘ **Las erratas del SD3 (320 minutos y 160 camiones) no tienen fila** |
| 41–45 | Qué se espera (lee y firma, plantilla, diagramas, formularios, sin precios) | SD1-05, SD2-08, SD1-04, SD2-09, SD3-05, SD4-46, SD13-13… | ✔ Repite exigencias ya cubiertas arriba |

## 2. SUBDOCUMENTO 1 ([L49–L115](../Revision_informe.md#L49))

| L | Punto del informe | Fila | Resultado |
|---|---|---|---|
| 59 | Revisión: sin T-6, sin figuras, rehacer | SD1-04, SD1-07 | ✔ |
| 63 | Crítico: T-6 no entregado | SD1-07 | ✔ |
| 64 | Dos casos; se exigen tres | SD1-08 | ✔ |
| 65 | Faltan 9 de 11 campos | SD1-09 | ✔ |
| 66 | Casos repiten criterios del caso; sin volúmenes | SD1-10 | ✔ |
| 70 | «Más de una década» sin fundación, hitos ni cartera | SD1-11 | ✔ |
| 71 | Sin líneas de negocio ni catálogo | SD1-12 | ✔ |
| 72 | Misión, visión y ESG sobran | SD1-13 | ✔ |
| 73 | Prosa de folleto | SD1-14 | ✔ |
| 74 | **OK** orientación a la industria del caso | — | ✘ Valoración positiva omitida |
| 78 | Sin organigrama | SD1-15 | ✔ |
| 79 | Dotación sin desglose; NOC 24×7 | SD1-16 | ✔ |
| 80 | Tabla de equipo del SD12/T-8; certificaciones ajenas | SD1-17 | ✔ |
| 81 | **OK** responsable único por dominio | — | ✘ Valoración positiva omitida |
| 82 | **OK** 56 meses y 36 de operación | — | ✘ Valoración positiva omitida |
| 86 | «Alineado» frente a «certificado» | SD1-18 | ✔ |
| 87 | AWS sin nivel ni vigencia | SD1-19 | ✔ |
| 88 | Sin alianzas de hardware ni conectividad | SD1-20 | ✔ |
| 89 | Laboratorio con jaulas de Faraday | SD1-21 | ✔ |
| 93 | Lista de normas, no gobierno | SD1-22 | ✔ |
| 94 | Conocimiento orientado al cliente | SD1-23 | ✔ |
| 95 | **OK** riesgo de conocimiento tácito | — | ✘ Valoración positiva omitida |
| 99 | Capacidad instalada = nube contratable | SD1-24 | ✔ |
| 100 | **OK** PREPROD y DR con prueba semestral | — | ✘ Valoración positiva omitida |
| 104 | RTO/RPO contradictorios | SD1-25 | ✔ |
| 105 | Cinco ambientes, seis listados | SD1-26 | ✔ |
| 106 | Microservicios serverless frente a monolito | SD1-27 | ✔ |
| 107 | Evitar centros de datos on-premise | SD1-28 | ✔ |

SD1-01 a SD1-06 responden puntos de GENERAL aplicados al SD1. Las cinco valoraciones «OK» no tienen fila; el SD2, SD3, SD4 y SD5 sí registran las suyas.

## 3. SUBDOCUMENTO 2 ([L119–L178](../Revision_informe.md#L119))

| L | Punto del informe | Fila | Resultado |
|---|---|---|---|
| 133 | Crítico: no hay resumen ejecutivo | SD2-10 | ✔ |
| 137 | **OK** AS-IS de siete fases | SD2-11 | ✔ |
| 138 | 2.3 y 2.4 duplicadas; paráfrasis del Cap. 4 | SD2-12 | ✔ |
| 139 | 7,8 % en preventa; 588/mes mal calculado | SD2-13 | ✔ |
| 140 | Tres problemas del Cap. 19 sin separar | SD2-14 | ✔ |
| 141 | Sin datos externos; vacío del cross-docking | SD2-15 | ✔ |
| 145 | **OK** marco normativo | SD2-16 | ✔ |
| 146 | Marco legal escrito como solución | SD2-17 | ✔ |
| 147 | Frase de evaluador | SD2-18 | ✔ |
| 148 | Estacionalidad solo como prohibición | SD2-19 | ✔ |
| 149 | Doce materias del 16.2 | SD2-20 | ✔ |
| 150 | 99,95 % «Tier III» frente a Tier II | SD2-21 | ✔ |
| 154 | **OK** mapa de once actores | SD2-22 | ✔ |
| 155 | Faltan ocho actores | SD2-23 | ✔ (los ocho coinciden) |
| 156 | 42 conductores en vez de 84 | SD2-24 | ✔ |
| 157 | Tabla, no matriz | SD2-25 | ✔ |
| 158 | Contradicciones entre entrevistados | SD2-26 | ✔ |
| 159 | Promesa de 24 h sin arbitrar | SD2-27 | ✔ |
| 163 | Supuestos = restricciones copiadas | SD2-28 | ✔ |
| 164 | Sin supuestos propios ni impacto | SD2-29 | ✔ |
| 168 | Citas sin lista de referencias | SD2-30 | ✔ |
| 169 | IA sin supervisión: marcadores | SD2-07, SD2-31 | ✔ |
| 170 | Cero figuras en 23 páginas | SD2-32 | ✔ |

SD2-01 a SD2-09 responden puntos de GENERAL. **Las 23 viñetas del SD2 están cubiertas.**

## 4. SUBDOCUMENTO 3 ([L182–L265](../Revision_informe.md#L182))

| L | Punto del informe | Fila | Resultado |
|---|---|---|---|
| 192 | Rehacer: 138 pp., 87 % tablas; sin implementación, implantación ni operación | SD3-06 | ✔ |
| 196 | Crítico: sin modelo conceptual ni figuras | SD3-07 | ✔ |
| 197 | Solución en dos páginas; depende del SD4 | SD3-08 | ✔ |
| 198 | Matriz de 19 filas, **sin paquete EDT ni identificador de prueba** | SD3-09 | ◐ **La fila omite «ni identificador de prueba» y la respuesta solo trata la EDT** |
| 199 | **OK** tres problemas separados | SD3-10 | ✔ |
| 203 | **OK** exclusiones fieles; «Lo que no haremos» | SD3-11 | ✔ |
| 204 | Objeción de la gerenta; dependencias; hito de septiembre de 2026 | SD3-12 | ✔ |
| 205 | Marcha blanca de la Etapa 2, meses 13–20 | SD3-13 | ✔ (cita no literal, ver §8) |
| 206 | Etapas no cuadran (OTIF/fill rate; EDI meses 10–16) | SD3-14 | ✔ |
| 207 | Exclusiones y restricciones infladas | SD3-15 | ✔ |
| 208 | Supuestos sin ID ni validación; S-41 | SD3-16 | ✔ |
| 209 | Sin visión de arquitectura empresarial | SD3-17 | ✔ |
| 213 | Crítico: T-12 no entregado | SD3-18 | ✔ |
| 214 | Catálogo funcional = lista de nombres | SD3-19 | ✔ |
| 215 | Prioridad no discrimina (80/90) | SD3-20 | ✔ |
| 216 | Saltos de numeración | SD3-21 | ✔ |
| 217 | RNF sin método de verificación | SD3-22 | ✔ |
| 218 | RF-02.05d/e y RF-15.05 inexistentes | SD3-23 | ✔ |
| 222–223 | Implementación no existe (D54, D49, IaC, 70 %) | SD3-24 | ✔ |
| 227 | Implantación no existe; oleadas y migración en tabla | SD3-25 | ✔ |
| 228 | Reversión sin tiempo para 05:30–07:00 | SD3-26 | ✔ |
| 229 | Sin convivencia con el papel | SD3-27 | ✔ |
| 233 | Operación no existe; SRE una vez | SD3-28 | ✔ |
| 234 | Mesa de ayuda 08:00–20:00 frente a 04:00–22:00 | SD3-29 | ✔ |
| 235 | **OK** RTO/RPO coherentes | SD3-30 | ✔ |
| 239 | **OK** tabla de grupos de interés | SD3-31 | ✔ |
| 240 | Faltan seis actores | SD3-32 | ✔ (los seis coinciden) |
| 241 | Planificador en «C» | SD3-33 | ✔ |
| 245 | **OK** 16 criterios; el N.° 16 sin verificación | SD3-34 | ✔ |
| 246 | **OK** 16 decisiones; WMS por estrangulamiento; **registro de vacíos detecta errores de las Bases**; enterrado en tablas | SD3-35 | ◐ La fila no recoge las valoraciones positivas del estrangulamiento (D14) ni del registro de vacíos |
| 247 | Excursión térmica contradictoria | SD3-36 | ✔ (cita no literal, ver §8) |
| 248 | Precio entre pedido y despacho | SD3-37 | ✔ |
| 249 | Promesa de 24 h «verificable» | SD3-38 | ✔ |
| 250 | Crítico: precio en D45 | SD3-39 | ✔ |
| 254 | Nombres de archivo como fuente | SD3-40 | ✔ |
| 255 | Notas de corrección | SD3-41 | ✔ |
| 256 | Dos voces | SD3-42 | ✔ |
| 257 | Decisiones citadas antes; códigos; párrafo pegado | SD3-43 | ✔ |
| 261–265 | Qué se espera (25–35 pp., T-12, matriz, regla térmica, sin precio) | SD3-06, 09, 18, 36, 39 | ✔ |

SD3-01 a SD3-05 responden puntos de GENERAL. **No hay fila para las erratas del SD3 (L37) ni para sus 21 páginas semivacías (L36).**

## 5. SUBDOCUMENTO 4.1 ([L269–L320](../Revision_informe.md#L269))

| L | Punto del informe | Fila | Resultado |
|---|---|---|---|
| 279 | Sin correlación entre texto y diagramas | SD4-01 | ✔ |
| 283 | 14 diagramas sin leyenda, sin cita, ilegibles | SD4-01, SD4-21 | ✔ |
| 284 | Trece recorridos por actor | SD4-02 | ✔ |
| 285 | 11 actores frente a 13 | SD4-03 | ✔ |
| 286 | Sin matriz requisito → módulo → capa | SD4-04 | ✔ |
| 287 | Ambientes en una línea | SD4-05 | ✔ |
| 288 | SOLID ausente; patrones declarativos | SD4-06 | ✔ |
| 289 | Seis vistas; falta la de procesos | SD4-07 | ✔ |
| 293 | **OK** monolito modular | SD4-08 | ✔ |
| 294 | Comparación de una frase; ADR en 4.2 con precios | SD4-09 (+SD4-46 precios) | ✔ |
| 295 | Doce módulos sin listar | SD4-10 | ✔ |
| 296 | Sin límites, orquestación ni secuencias | SD4-11 | ✔ |
| 297 | TOGAF solo mencionado | SD4-12 | ✔ |
| 298 | Modelo de dominio en viñetas | SD4-13 | ✔ |
| 302 | TTL 8 h frente a 24 h | SD4-14 | ✔ |
| 303 | API Gateway sin respaldo local | SD4-15 | ✔ |
| 304 | Excursión: bloqueo automático frente a conductor | SD4-16 | ✔ |
| 305 | Etapas no coinciden con el SD3 | SD4-17 | ✔ |
| 306 | Portales externos por VPN | SD4-18 | ✔ |
| 310 | Portada «Lógica y Física», solo lógica | SD4-19 | ✔ |
| 311 | Códigos internos sin documento | SD4-20 | ✔ |
| 312 | Plantilla distinta | SD4-21 | ✔ |

**Las 21 viñetas del 4.1 están cubiertas.** Lo único que falta del 4.1 es la hoja «Página en blanco a propósito» del apartado GENERAL (L19).

## 6. SUBDOCUMENTO 4.2 ([L324–L399](../Revision_informe.md#L324))

| L | Punto del informe | Fila | Resultado |
|---|---|---|---|
| 334 | Duplicado, sin portada, comentarios de IA, una figura, precios | SD4-22, 23, 25, 46 | ✔ |
| 338 | p. 56 ADR-15 «Si se prefiere (B)…» | SD4-23 | ✔ |
| 339 | p. 114 «Cambios v01 → v02» y «Empresa proponente: Pendiente de definir» | SD4-23 | ◐ Ver L16 |
| 340 | p. 32 hallazgo D1 pendiente | SD4-23 | ✔ |
| 341 | Notas de revisión; «3 brokers en 3 AZ» | SD4-23 | ◐ La respuesta es genérica; «3 brokers» no se nombra |
| 342 | Documentos inexistentes (v06, v6.2…) y códigos (L577, S14…) | SD4-20, SD4-23 | ◐ EL-20 corresponde al 4.1; para el 4.2 solo hay una mención en «Qué falta» |
| 346 | Emplazamiento de seis filas; 36 componentes | SD4-24 | ✔ |
| 347 | Figura única ilegible y sin cita | SD4-25 | ✔ |
| 348 | «En texto, la vista…» | SD4-26 | ✔ |
| 349 | BI en catorce páginas | SD4-27 | ✔ |
| 353 | **OK** 27 implementos | SD4-28 | ✔ |
| 354 | Cantidades sin número; caída y ciclo de vida | SD4-29 | ✔ |
| 355 | Sobredimensionamiento de terminales, impresoras y POS | SD4-30 | ✔ |
| 356 | Frío en 18 camiones; alerta al volver | SD4-31 | ✔ |
| 357 | Cobertura inalámbrica en una frase | SD4-32 | ✔ |
| 361 | Sala de 173 m² sobredimensionada | SD4-33 | ✔ |
| 362 | Tier II frente a 99,95 % | SD4-33 | ✔ |
| 363 | Sin cálculo eléctrico/térmico, plano ni racks | SD4-34 | ✔ |
| 364 | Remisión circular a «Seguridad §12» | SD4-47 | ✔ |
| 365 | Gabinetes de borde sin especificación | SD4-35 | ✔ |
| 366 | DR sujeta a aprobación; RTO de 24–72 h | SD4-36 | ✔ |
| 367 | T-11 no adjunto | SD4-37 | ✔ |
| 371 | **OK** seguridad Zero Trust | SD4-38 | ✔ |
| 372 | **OK** SPOF y 3-2-1-1-0 | SD4-38 | ✔ |
| 373 | Identidad sin conexión sin resolver | SD4-39 | ✔ |
| 374 | Sin puerta de enlace local | SD4-39 | ✔ |
| 375 | Funciones no disponibles sin conexión (RT-03.13) | SD4-39 | ✔ |
| 376 | Ceph sobre RAID; 98 % de llenado; **100.000 IOPS para 840** | SD4-40 | ◐ El título de la fila no menciona el sobredimensionamiento de IOPS |
| 377 | DTE diferido | SD4-41 | ✔ |
| 378 | Dotación frente a cuatro TI | SD4-42 | ✔ |
| 379 | Sin red, despliegue ni zonas | SD4-43 | ✔ |
| 383 | **OK** TPS derivados | SD4-48 | ✔ |
| 384 | Salto de 28 a 35 y ×3; tres regímenes | SD4-44 | ✔ |
| 385–386 | Dimensiones sin derivación o ausentes | SD4-45 | ✔ |
| 390 | **OK** quince ADR en formato MADR | SD4-49 | ✔ |
| 391 | Crítico: ADR con precios | SD4-46 | ✔ |
| 395–399 | Qué se espera (un archivo, diagramas, emplazamiento, sala, 28 vehículos) | SD4-22, 26, 24, 33/34, 31 | ✔ |

## 7. SUBDOCUMENTO 5 ([L403–L460](../Revision_informe.md#L403))

| L | Punto del informe | Fila | Resultado |
|---|---|---|---|
| 415 | Crítico: sin modelo de datos; quince bases | SD5-01 | ✔ |
| 416 | Crítico: sin diccionario | SD5-02 | ✔ |
| 417 | Consulta del proveedor y de la autoridad sanitaria (Cap. 19) | SD5-03 | ✔ |
| 421 | Tabla con palabras partidas; sin análisis en prosa | SD5-04 | ◐ La fila omite las palabras partidas |
| 422 | Decisión 16.1 #18 inexistente | SD5-05 | ✔ |
| 426 | Alcance por migrar con valores del Cap. 15 y casos de saneamiento propios | SD5-06 | ⚠ **Sentido cambiado** (ver §8) |
| 427 | Metodología = RT reescritos; sin volumen, herramientas, tiempos, ventana ni responsables | SD5-07 | ✔ |
| 431 | **OK** índices, partición y orden | SD5-08 | ✔ |
| 432 | «~105 TPS base…» ininteligible | SD5-09 | ✔ |
| 433 | Caché TTL 8 h bodega / 14 h reparto | SD5-10 | ✔ |
| 437 | **OK** separación, latencias, retención, ISO 25012 | SD5-11 | ✔ |
| 438 | **OK** desajuste RT-05.10/RT-16.10 | SD5-12 | ✔ |
| 439 | Sin modelo de explotación; esquema estrella sin dibujar | SD5-13 | ✔ |
| 440 | RT-16.08 frente a RT-16.20 | SD5-14 | ✔ |
| 444 | Timbre diferido; sin guía de papel | SD5-15 | ✔ |
| 445 | **OK** evidencia por receptor; falta acuse legal | SD5-16 | ✔ |
| 449 | Resaltado negro | SD5-17 | ✔ |
| 450 | Línea de metadatos | SD5-18 | ✔ |
| 451 | Doble numeración y códigos internos | SD5-19 | ✔ |
| 452 | Siglas sin definir (FID) | SD5-20 | ✔ |

**Las 20 viñetas del SD5 están cubiertas, una con el sentido cambiado.** El SD5 no tiene filas para los puntos de GENERAL que también lo nombraban (L15, L17, L18, L19, L23, L26), a diferencia del SD1, SD2, SD3 y SD13.

## 8. SUBDOCUMENTO 13 ([L464–L504](../Revision_informe.md#L464))

| L | Punto del informe | Fila | Resultado |
|---|---|---|---|
| 474 | Revisión: tres no superan el Art. 30°; sin siete elementos; sin T-19; precios | SD13-01/02/05, 06–09, 12, 13 | ✔ |
| 478 | **OK** el anexo descarta bien los requisitos | — | ✘ Valoración positiva omitida |
| 479 | Innovación 1 = criterio N.° 1 / RT-05.23 | SD13-01 | ✔ (cita literal) |
| 480 | Innovación 3 = RT-03.10–13 | SD13-02 | ✔ (cita literal) |
| 481 | Innovación 2: olas y FEFO estándar | SD13-03 | ✔ (cita literal) |
| 482 | Innovación 4: restricción N.° 9 y flujo de caja | SD13-04 | ✔ (cita literal) |
| 483 | Innovación 5: WhatsApp sin internet; no está en SD3 ni 4.1 | SD13-05 | ✔ |
| 487 | Cuatro viñetas por innovación | SD13-06 a 09 | ✔ (contexto de las filas siguientes) |
| 488 | Faltan madurez, incorporación, impacto y riesgo | SD13-06, 07, 08, 09 | ✔ |
| 489 | «Investigación adicional: Sí» | SD13-10 | ✔ (cita literal) |
| 490 | Indicadores sin momento ni línea base | SD13-11 | ✔ |
| 494 | Crítico: T-19 no entregado | SD13-12 | ✔ |
| 495 | Crítico: precios en dólares | SD13-13 | ✔ |
| 496 | Fuentes sin cita; EPCIS 1.2 | SD13-14 | ✔ |
| 497 | Siete páginas sin figura | SD13-15 | ✔ (cita literal) |

SD13-16 a SD13-20 citan correctamente L15, L17, L18, L19 y L23. SD13-21 a SD13-23 citan L513, L510 y L511.

## 9. CONSIDERACIONES TRANSVERSALES ([L508–L514](../Revision_informe.md#L508))

| L | Punto del informe | Fila(s) | Resultado |
|---|---|---|---|
| 510 | Contradicciones entre subdocumentos (RTO/RPO, serverless, Tier, excursión, caché 8 h) | SD1-25, SD1-27, SD2-21, SD3-36, SD4-14, SD4-16, SD5-10, SD13-22 | ✔ Repartida en cada subdocumento |
| 511 | No se puede seguir un requerimiento hasta un componente | SD3-09, SD4-04, SD4-24, SD5-01, SD13-23 | ✔ |
| 512 | Fundamentación ingenieril: decisiones correctas, pero enterradas en tablas; sin diagramas explicados, cálculos a la vista ni análisis en prosa | — | ✘ **Ninguna fila la recoge como tal**; se responde solo de forma indirecta (SD3-06, SD3-35, SD4-44/45…) |
| 513 | Cuatro indicios de IA; desde el Informe 2, puntaje 0 | SD2-07, SD3-03, SD4-23, SD13-21 | ◐ El SD1 y el SD5 no tienen fila de indicios de IA |
| 514 | Compliance: precios en la Oferta Técnica | SD1-06, SD2-09, SD3-05, SD3-39, SD4-46, SD13-13 | ✔ |

## 10. Fidelidad del texto de las observaciones

| Fila | Problema | Informe (literal) | Tabla |
|---|---|---|---|
| **SD5-06** | **Sentido cambiado.** El informe constata (sin «OK», pero sin reparo) que el alcance de migración y los casos de saneamiento están presentes. La fila lo convierte en una exigencia («Incorporar…»). | L426: «Alcance por migrar con los valores del Cap. 15 y casos de saneamiento propios del caso (lotes en texto libre, duplicados de cliente, saldos de envases).» | «Incorporar alcance histórico y saneamiento: lotes libres, clientes duplicados y saldos de envases.» |
| SD3-13 | Las comillas no contienen una cita literal. | L205: «Marcha blanca de la Etapa 2… Meses 13–20» | «marcha blanca Etapa 2, meses 13–20» |
| SD3-36 | Las comillas no contienen una cita literal. | L247: «lo decide el conductor» / «la adopta la autoridad de calidad» | «la decide el conductor» / «la adopta Calidad» |
| SD4-01 a SD4-49 | Las páginas («pp. 9–14») remiten a un PDF de revisión que no está en el repositorio; no son cotejables aquí. El texto de cada observación sí coincide con su viñeta. | — | — |

Todas las demás filas parafrasean fielmente su viñeta. Las comillas de SD2-10, SD2-18, SD2-21, SD2-24, SD2-31, SD3-01, SD3-33, SD3-37, SD3-39, SD3-40, SD3-41, SD13-01 a 04, SD13-10 y SD13-15 coinciden con el informe.

## 11. Lista de brechas (decisión pendiente del equipo)

Ninguna se corrigió en la tabla, porque añadir filas exige redactar respuestas nuevas y corregir SD5-06 modifica una fuente.

1. **SD3 — erratas** «ventana de 320 minutos» (p. 3) y «160 camiones que no son trabajadores» (p. 66) (L37): sin fila.
2. **SD3 y SD4 — títulos huérfanos y páginas semivacías** (21 en SD3 y 19 en 4.2) (L36): sin fila.
3. **SD4 (4.1) y SD5 — hoja «Página en blanco a propósito»** (L19): sin fila.
4. **SD4 (4.2) — «LAFROX no aparece» y «Empresa proponente: Pendiente de definir»** (L16, L339): sin respuesta explícita.
5. **SD4 (4.2) — más de la mitad son tablas de listado (T-21)** (L25): sin fila.
6. **SD5 — puntos GENERAL** (identidad, portada T-22, A4/11 pt, índice/folio/firma, indicios de IA): sin filas.
7. **SD1 — indicios de IA** (L513): sin fila (SD1-05 trata solo de leer y firmar).
8. **SD1 (5) y SD13 (1) — valoraciones «OK»** omitidas (L74, L81, L82, L95, L100, L478).
9. **Transversal — fundamentación ingenieril** (L512): sin fila propia.
10. **Parciales:** SD3-09 (identificador de prueba), SD3-35 (valoraciones positivas), SD4-40 (IOPS), SD4-23 (3 brokers, referencias del 4.2), SD5-04 (palabras partidas).
11. **Fidelidad:** reformular SD5-06 y ajustar las comillas de SD3-13 y SD3-36.

## 12. Resolución aplicada (12-10-2026, autorizada por el usuario)

Se actualizaron las tablas de origen y se regeneró la consolidada: 213 filas (212 de los subdocumentos y TR-01). Verificación: 212/212 filas idénticas a su fuente, 0 líneas de notas perdidas, identificadores únicos y enlaces correctos.

| Brecha (§11) | Resolución | Fila(s) |
|---|---|---|
| 1. Erratas del SD3 | Documentado: ninguna aparece en los PDF vigentes (cuerpo, anexos y T-12) | SD3-44 |
| 2. Títulos huérfanos y páginas semivacías | Revisión página por página de los PDF vigentes. SD3: **Parcial**, 5 páginas con espacio sin uso (cuerpo p. 20; anexos pp. 83 y 131; T-12 pp. 4 y 128) y una frase introductoria separada de su lista (p. 22). SD4: **Pendiente**, 15 páginas semivacías en el cuerpo antes de figuras o tablas en hoja horizontal. Ningún título queda al pie de página. | SD3-45, SD4-53 |
| 3. Hoja en blanco en 4.1 y SD5 | Corregido (SD4: PDF vigente; SD5: Markdown) | SD4-50, SD5-22 |
| 4. LAFROX y «Pendiente de definir» en el 4.2 | Corregido en los PDF vigentes | SD4-51 |
| 5. T-21: tablas de listado en el 4.2 | Documentado | SD4-52 |
| 6. SD5: puntos de GENERAL | Identidad, portada, hoja en blanco e IA documentados; formato de página, tipografía, folio y firma **por cotejar en el PDF del SD5** | SD5-21 a SD5-24 |
| 7. SD1: indicios de IA | Documentado (PDF del cuerpo y del T-6) | SD1-34 |
| 8. Valoraciones «OK» | SD1: 3 «Se mantiene», 1 «Parcial» (faltan los 36 meses de operación) y 1 «Trasladado» al SD3; SD13: se mantiene el criterio | SD1-29 a SD1-33, SD13-16 |
| 9. Fundamentación ingenieril | Documentado como fila transversal | TR-01 |
| 10. Parciales | SD3-09 se omite por decisión del usuario; SD3-35, SD4-40 (IOPS, con frase nueva en el ADR-10), SD4-23 y SD5-04 completados | — |
| 11. Fidelidad | SD5-06 vuelve al sentido del informe; SD3-13 y SD3-36 usan las citas literales | — |

Hallazgos nuevos de la revisión de los PDF:

- El PDF vigente del SD4 (`origin/subdoc-4`, 7ba8608) **no lleva media firma en ninguna página** y la línea de firma de su portada está vacía; SD1, SD2 y SD3 sí la tienen. Se registró en SD4-22 (EF-01).
- Las portadas del SD4 (PDF) y del SD5 (Markdown) tienen fecha de emisión 05-10-2026; las del SD2 y el SD3, 12-10-2026.
- El checkout local `../LafroX-subdoc4` (rama `subdoc-4`, 292c6e8) está desactualizado respecto de `origin/subdoc-4`. Para la revisión se extrajeron los PDF del remoto al directorio temporal, sin tocar el checkout.
- El PDF del SD4 no incluye todavía la frase nueva del ADR-10, que solo está en el Markdown.

### Ajuste posterior (12-10-2026, decisión del usuario)

- Se retiró la fila EF-31 (páginas semivacías del SD4) y la nota sobre la media firma del SD4 en EF-01; el usuario resuelve la firma.
- SD3-45 pasa a «Documentado», con la reducción verificada de 21 a menos de diez páginas semivacías y sin títulos al pie de página.
- Los PDF se volvieron a verificar contra las ramas remotas (`origin/LafroX-Subdoc1-LateX` 05fe9c9, `origin/LafroX-Subdoc3-LateX` e55ca51, `origin/subdoc-4` 5899782). El SD3 commiteado tiene 35, 168 y 261 páginas; el Anexo 3.H está en la p. 145.
- Tras el commit 50dd1f7, la tabla del SD13 vive en `13_innovaciones/LAFROX-SD13-Matriz-cambios-Informe1-Informe2.md`; ahí se reincorporó la fila «OK». La consolidada tiene 212 filas de datos (211 filas de las matrices fuente y la transversal TR-01), más el encabezado: 213 filas físicas en la tabla.
