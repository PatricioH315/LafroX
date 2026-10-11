# Revisión de la Comisión — Informe 2 · Subdocumento 9 (v5)

> **Actualización posterior (11-10-2026).** Tras alinear el SD9 con SD1, T-10, T-14, T-15 y T-18, quedan resueltos C3, C4, A5 y la nota de veto del Comité de Calidad (ver `compct/CONTEXTO_SESION.md`). Siguen abiertos C1, A2, A3 y M4–M7.

**LAFROX · GRUPO 2 · INFORME 2 · Caso 2 · Distribuidora Puelche S.A.**

**Archivos recibidos** (`09_plan_calidad/`): `LAFROX-Subdocumento9.md` (599 líneas), `LAFROX-Subdocumento9-Anexos.md` (881), `LAFROX-Formulario-T-13.md` (199), `LAFROX-Formulario-T-17.md` (256). Nomenclatura conforme (ACL §1); un formulario por archivo.

**Documentos revisados:** Subdocumento 9 (10 figuras Mermaid, 11 tablas numeradas), Anexos 9.A–9.D (29 métricas, 23 reglas, 645 filas de matriz), T-13 y T-17, cotejados con SD1, SD3, SD4, SD6, SD8, T-10, T-12 y T-14.

**Alcance.** Fuente Markdown. Folio, firma, índice paginado, tipografía, legibilidad de figuras y texto seleccionable quedan pendientes del PDF final.

---

## 1. Puntaje

### 9. PLAN DE CALIDAD — Formularios T-13 y T-17 (8 %)

**Revisión: (Puntaje 0)**

**Veredicto.** El subdocumento se tiene por no presentado: hay 16 celdas `[[REVISIÓN HUMANA]]` (SD9 10, AN9 4, T13 1, T17 1), que la ACL §7.1 d trata como indicio de IA y deja el ítem en 0 sin subsanación. Sin esa causal, el diagnóstico de contenido es **20**: el núcleo (umbrales bloqueantes y estrategia 29119 propia) existe, pero el SD9 contradice al T-14 en 11 de 12 pruebas semestrales y las pruebas obligatorias previas a H7 y H12 siguen sin paquete, fecha ni HH.

Ponderado: 0 × 8 % = **0,0**.

---

## 2. Correcciones respecto de v4

| Hallazgo v4 | Estado en v5 | Evidencia |
| --- | --- | --- |
| C1 celdas de revisión humana | **No corregido** | 16 celdas |
| C2 notas de proceso en el cuerpo | Corregido | Cero coincidencias de «esta inspección», «no inventa», «no presenta como ejecutadas», «no modifica sus atribuciones» |
| C3 meses del T-14 | **No corregido** | T-14:1661 («Meses 27, 33, 39, 45, 51 y 54») y T-14:1681 («26, 32, 38, 44, 50 y 55») frente a SD9 Tabla 9.9 |
| C4 certificación de cierre H7/H12 sin planificar | **No corregido** | T-13:157 la exige; la Tabla T13.5 no tiene filas para H7/H12 |
| A1 ambiente del pentest y la resiliencia | Corregido | Fig. 9.4 los ubica en Preproducción; T13.2 y T13.3 coinciden con la Tabla 9.6 |
| A2 cinco campañas en un Preproducción | **No corregido** | T13.5: 3.9.3, 3.9.4, 3.9.5 y 3.9.7 el 19–26-05-2028 |
| A3 holgura sin feriados ni segunda revisión | **No corregido** | Tabla 9.8 igual |
| A4 diciembre | Corregido | 9.3.3 limita la prohibición a pruebas que tocan Producción o el sitio de recuperación |
| A5 alcance de G5 frente a la cadencia quincenal | **No corregido** | — |
| M1 tablas sin número | Corregido | Tablas 9.1, 9.6a y 9.6b con caption y frase introductoria |
| M2 «24 umbrales» en la Fig. 9.1 | Corregido | «5 umbrales bloqueantes · 23 reglas» |
| M3 barra de H1 | Corregido | Termina el 09-03-2027 |
| M5 orden de referencias | Corregido | ISO 9001 antes de las entradas con coautor |
| M4, M6, M7, M5(ii) CMMI SCAMPI como referencia | No corregidos | Ver 3 |

**Recuento de 14 hallazgos v4:** 7 corregidos y 7 no corregidos.

**Cambios por contenido (revisión de clases y subdocumentos anteriores).** Se quitaron TMMi, el reparto del costo de la calidad, la complejidad cognitiva, la DRE y los umbrales numéricos de duplicación y deuda. Se restituyeron SLSA nivel 3, la deuda bloqueante = 0 y la duplicación medida sin bloqueo, porque SD3, SD4, T-10 y T-12 ya los declaran. Los conteos quedaron consistentes: Anexo 9.A = 29 filas, Anexo 9.B = 23 filas, Figura 9.1 con los mismos valores.

---

## 3. Hallazgos vigentes

### Críticos

**C1 — 16 celdas `[[REVISIÓN HUMANA]]`.** SD9, 10 filas de la declaración de IA; AN9, 4; T13, 1; T17, 1. Todas declaran nivel «Alto» en texto. Sólo un integrante puede completarlas.

**C3 — El T-14 tiene otras fechas.** SD9 Tabla 9.9, Figura 9.9 y T13.6: recuperación en los meses 24, 30, 36, 42, 48 y 54, resiliencia en 23, 29, 35, 41, 47 y 53. T-14: recuperación en 27, 33, 39, 45, 51 y 54; resiliencia en 26, 32, 38, 44, 50 y 55. Sólo coincide el mes 54. La propagación al T-14 es una decisión pendiente.

**C4 — Certificación de cierre de H7 y H12 sin paquete, fecha ni HH.** T13:157 y SD9 9.3.2 hacen obligatorias, antes de H7 y H12, la intrusión por tercero, la resiliencia, la carga, el DR real y la accesibilidad sobre la versión de cierre. El SD9 admite que la Figura 9.9 «no desglosa fechas ni HH». Una exigencia obligatoria y no planificada contradice la regla de que el plan sea ejecutable.

### Altos

**A2 — Cinco campañas en un solo Preproducción.** T13.5 programa seguridad ofensiva, carga con resiliencia, DR y despliegue entre el 19 y el 26-05-2028 (6 días hábiles) sobre el mismo ambiente. El T13.3 exige «versión congelada» para el pentest, y la resiliencia inyecta fallas en ese ambiente.

**A3 — Holgura de la Tabla 9.8.** Reserva menos 10 días hábiles de subsanación, sin la segunda revisión de la Figura 9.10 ni feriados. H1 (−4) y H8 (−6) quedan negativos.

**A5 — Alcance de G5.** La Tabla 9.5 y la Tabla 9.6 asocian el paso a producción con DR real y pentest; la Tabla 9.4 fija una cadencia quincenal. No se dice qué puerta rige para cada versión quincenal.

### Medios

- **M4 — Figuras.** Diez figuras Mermaid sin imagen enlazada. AGENTS.md exige que cada figura enlace su imagen; los `.drawio` existen en `Diagramas/` pero no se referencian. `Fig_9-1_Marco_Calidad.drawio` no refleja las etiquetas nuevas.
- **M5(ii) — Referencias.** «CMMI Institute (2023)… SCAMPI A Appraisal Report N° 58190» es un informe de evaluación de LafroX, no una fuente publicada. El SD1:204 lo declara emitido en noviembre de 2023; no verificable con el material recibido.
- **M6 — «Terreno» como sexto ambiente.** T13.2 tiene seis filas; el SD4 habla de cinco ambientes.
- **M7 — Capacidad de evaluadores.** SD9 usa 21 días hábiles y 6,4 HH efectivas por persona (2.150,4 HH); el T-15 usa 20 días (según nota de contexto; no re-verificado).
- **M8 — Numeración de tablas.** Las tablas 9.6a y 9.6b quedan entre la 9.6 y la 9.7; la numeración es ascendente pero con sufijo. Aceptable si se mantiene el vínculo con el T-12, que cita las Tablas 9.3, 9.6 y 9.9.

---

## 4. Verificación (OK)

- **OK — Estructura.** 9.1, 9.2 y 9.3 con el texto exacto del índice obligatorio; «Referencias» y «Declaración de uso de IA» al final.
- **OK — Sin precios** (`USD`, `CLP`, `UF`, `$`, CAPEX, OPEX, TCO: cero coincidencias).
- **OK — Sin notas de proceso, marcadores clásicos de IA ni referencias a documentos inexistentes.**
- **OK — Cálculos.** 849 + 354 + 105 = 1.308 casos; 1.046 automatizados; 8,7 h y 4,36 h; 65,5 HH. 21,99 TPS, 1.163 usuarios, 237 dispositivos, 43,98 y 10,41 TPS. Presupuesto de error 43,2 / 40,32 / 41,76 / 44,64 min. Tabla 9.7: 10.848 HH (5,0 % de 216.935).
- **OK — Coherencia con subdocumentos anteriores.** SLSA nivel 3, deuda bloqueante y duplicación con PHPCPD/jscpd coinciden con SD3, SD4, T-10 y T-12. 32,11 GB coincide con SD4 y SD5. R8-31, R8-32 y R8-18 coinciden con el SD8.
- **OK — Ambientes y pruebas.** Pentest y resiliencia en Preproducción en la Figura 9.4, la Tabla 9.6 y el T-13.
- **OK — Hitos.** H6/H11 como condiciones de entrada y H7/H12 como pasos a producción (meses 16 y 21), coherentes con T-17 y con el Art. 17.
- **OK — Figuras y tablas.** Las 10 figuras y las 11 tablas se citan antes y se explican después; ningún título queda sin frase introductoria.

## 5. Pendientes del PDF final

Nomenclatura efectiva, portada, firma y foliación; índice con número de página y enlaces; tamaño ≥ 9 pt en figuras; tablas largas (T13.3 con celdas de párrafo); páginas de las citas a las Bases; páginas en blanco.

## 6. Qué se espera en el Informe 3

1. Completar las 16 celdas de revisión humana con la revisión efectivamente realizada.
2. Propagar al T-14 (8.1.3 y 8.2.2) los meses del SD9 y del T-13, o a la inversa.
3. Crear paquete, fechas, HH y responsables para la certificación de cierre de H7 y H12 (T-14, T-15 y Tabla T13.5).
4. Escalonar las campañas de 3.8 y 3.9 para no compartir Preproducción.
5. Rehacer la Tabla 9.8 con feriados y segunda revisión, o justificar por escrito por qué H1 y H8 quedan negativos.
6. Definir el alcance de G5 frente a la cadencia quincenal y enlazar las imágenes de las figuras.

## CONSIDERACIONES TRANSVERSALES

- **Consistencia técnica.** La única contradicción de fondo entre subdocumentos es la de fechas con el T-14 (C3).
- **Trazabilidad.** El requisito «retiro de lote < 2 h» recorre origen, requisito, componente, paquete 3.4.4, prueba, cambio, despliegue y acta R18-01; el eslabón de EDT no se refleja en la Tabla 9.7, que agrupa por cuenta.
- **Uso de IA.** Un indicio vigente (C1). Consecuencia: 0 sin subsanación.
- **Compliance.** Sin precios y sin plazos fuera del Art. 17°. Folio y firma, pendientes del PDF.
- **Correcciones.** De 14 hallazgos de v4: 7 corregidos y 7 no corregidos.

| Ítem | Peso | Puntaje | Ponderado |
| --- | --- | --- | --- |
| 9. Plan de calidad (T-13, T-17) | 8 % | 0 | 0,0 |
