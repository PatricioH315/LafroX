# LafroX — Validación de la revisión integral de inconsistencias

Objeto: comprobar, contra el estado actual de los 31 entregables, si `Revision/revision_integral_inconsistencias.md` (RI-01 a RI-19) es correcta, y registrar lo que esa revisión no recoge. Base: rama `rama-md`, commit `0896cae` (10-10-2026 18:05), igual al árbol de trabajo revisado; ningún `.md` cambió durante esta validación (huellas SHA-256 de los 107 Markdown comparadas antes y después). No se modificó ningún entregable ni el informe validado.

## 1. Veredicto

**El método y la evidencia del informe eran correctos a su corte (15:02–15:15), pero hoy está parcialmente desactualizado.** Se redactó antes del cierre de brechas del T-12 y de la decisión NOC/SOC en Valparaíso, ambos registrados en `0896cae`. De las 19 fichas:

| Resultado | Fichas |
|---|---|
| Vigente | RI-02, RI-03, RI-04, RI-05, RI-07, RI-08, RI-10, RI-11, RI-12, RI-14, RI-15, RI-17, RI-18, RI-19 (14) |
| Parcialmente vigente | RI-01, RI-06, RI-13 (3) |
| Superada | RI-09, RI-16 (2) |

Además hay cuatro correcciones de calificación. RI-05, RI-07 y RI-13 no requieren una decisión del equipo: la decisión ya está tomada y documentada, y queda sólo un texto rezagado (corrección documental de complejidad baja). En cambio, la severidad de RI-11 está subestimada, porque una leyenda de figura sin su figura es un indicio del §7.1 a). Hay también un hallazgo nuevo de severidad media (N-01) y no aparecen contradicciones nuevas en los cruces automáticos de la sección 4.

Severidades corregidas: 9 altas (RI-01, 02, 03, 04, 06, 07, 08, 10, 11), 7 medias (RI-05, 12, 13, 14, 15, 17, 19), 1 baja (RI-18) y 2 superadas. Más N-01, de severidad media.

## 2. Validación ficha por ficha

### Parcialmente vigentes

- **RI-01 — Soporte.** Dos de los cuatro RT citados ya están en «Cumple»: RT-21.08 (orientación funcional, [T-12:605][t12], SD3 3.4.5) y RT-21.13 (indicadores abiertos al CLIENTE, [T-12:610][t12], SD4 4.1.3.8). Siguen en «No cumple» RT-21.02, el gerente de servicio ([T-12:599][t12]), y RT-21.16, los traslados N2/N3 ([T-12:613][t12]), junto con sus pares RNF-21.02 y RNF-21.07 ([T-12:264,269][t12]). Para esos dos se mantienen la severidad alta y la solución propuesta. La evidencia y el cierre de la ficha deben reducirse de «cuatro RT» a dos.
- **RI-06 — Matriz 9.C.** Las cifras del informe quedaron obsoletas. Después del informe se sincronizaron 26 estados del 9.C (por ejemplo, RT-23.01/.02 figuran hoy en «Cumple», [SD9-A:766–767][s9a]). Las 12 diferencias que el informe enumera ya no existen. Hoy hay **15 diferencias** sobre los 645 IDs:
  - seis RT-23.05–.10, «Cumple» en el T-12 frente a «No cumple / sin prueba» en el 9.C ([SD9-A:770–775][s9a]);
  - nueve filas que pasaron a «Cumple» en el cierre focal: RNF-12.03, RNF-19.02, RT-02.10, RT-03.08, RT-04.13, RT-14.08 y RT-16.24 (parciales en el 9.C) y RT-21.08 y RT-21.13 (No cumple en el 9.C, [SD9-A:742,747][s9a]).

  El T-12 actual suma RF 162/18/1, RNF 87/1/2 y RT 333/21/20, en total **582/40/23** (el informe decía 561/59/25). Con la regla 9.C.1 sin cambios, sólo los ocho RT que salen de «No cumple» agregan un caso cada uno: RT 346 → 354, total **544 + 302 + 354 + 105 = 1.305 casos** (no 1.303), **613 IDs con prueba propia y 32 sin ella** (23 No cumple + 9 absorbidos). La Tabla 9.C.1 sigue en 346/605/40/1.297 ([SD9-A:137–145][s9a]). El mensaje del commit `0896cae` («SD9 annex 9.C states synced with T-12») tampoco es exacto para esas 15 filas.
- **RI-13 — TLS.** La cita del cuerpo ya no existe: [SD4:725][s4] exige ahora TLS 1.3 en las entradas externas y entre componentes. Queda un residuo en [SD4-A:1179][s4a]: tras acotar la excepción TLS 1.2 al ERP de 2017, agrega «La misma regla rige para un tercero con limitación de protocolo». Esa extensión contradice la decisión vigente (la única excepción es el ERP) y el «Cumple» de RNF-14.01 y RT-11.08 ([T-12:231,464][t12]). Corrección: suprimir esa frase. Es documental (D), de complejidad baja, no una decisión del equipo.

### Superadas

- **RI-09 — SOC.** [SD6:48][s6], [T-9:94][t9] y [SD6-A:61][s6a] declaran hoy un SOC 24×7 propio en el Centro de Operaciones de Valparaíso, con analistas contratados antes del mes 13. RT-11.17 está en «Cumple» con ubicación, dotación y procedimientos ([T-12:473][t12]). No quedan frases de cobertura condicionada a una subcontratación.
- **RI-16 — Acuse comercial.** [SD4:1409][s4] (4.1.17.1) compromete el acuse comercial dentro de 30 minutos desde la descarga, por INT-08/OpenAS2 junto con el ASN de la misma guía, y lo distingue del MDN y del acuse tributario. RNF-12.03 está en «Cumple» ([T-12:221][t12]). El único residuo es el estado parcial de esa fila en el 9.C ([SD9-A:365][s9a]), ya contado en RI-06. No se verificó si el SD5 modela el acuse comercial como objeto propio; existe `edi_asn`.

### Vigentes, con precisiones

- **RI-02 — Capacidad en ventanas de prueba.** Confirmada con exactitud. Un barrido de los 163 paquetes de la Tabla 6.1 comparó HH con máximo de personas × días hábiles × 6,4 HH ([T-15:542][t15]). Sólo los ocho paquetes que cita el informe son infactibles: 3.8.4, 3.8.5 y 3.8.8 (179,2 HH de capacidad para 320 HH); 3.9.2 (96 para 320); 3.9.3, 3.9.4 y 3.9.5 (115,2 para 320); 3.9.7 (76,8 para 160) ([T-15:654–665][t15]). No hay otros casos.
- **RI-03 — H12.** Vigente. El reparto supone el H12 firmado el 05-10-2028 ([T-15:86][t15]). Sin embargo, 4.3.3 «Aceptación final (H12)» corre del 11 al 19-10 y 9.1.2 (archivo de las actas H1–H12, «después del H12») del 02 al 10-10 ([T-15:686,732][t15]; [T-14:1761][t14]), contra D-34 ([SD7-A:78][s7a]).
- **RI-04 — Innovaciones y gates.** Vigente. T-14 y SD13 fijan los meses 9 y 10 «(H4)» ([T-14:1311–1312,1320][t14]; [SD13:112–113,369][s13]). Los paquetes terminan el 19-11-2027, después de la entrega del H4 (20-10) y de su límite (16-11) ([T-15:495,667–668,676][t15]). INN-05.P4 «Certificación del H10» empieza el 03-07-2028, después del H10 del 12-06 ([T-15:681][t15]; [SD13:609][s13]).
- **RI-05 — Predecesoras de las pruebas no funcionales.** La contradicción es real, pero no requiere decisión. El equipo ya decidió que las pruebas de carga, recuperación, seguridad y despliegue empiezan después de la integración: así lo dicen [T-15:476][t15], la Tabla 6.1, el T-13 y el SD9 9.3.2 (decisión del 9-10, registrada en el contexto). Sólo están rezagadas las notas de D-21b y D-31b ([SD7-A:63,74][s7a]), que aún dicen «no dependen del resultado funcional» y nombran 3.4/3.5 como predecesoras. Pasa a corrección documental de complejidad baja.
- **RI-07 — Regla térmica.** La contradicción es real, pero no hace falta pedir una decisión a Calidad. El SD2 (Anexo 2.2, S-04), el SD3 ([SD3-A:405,534][s3a]) y siete pasajes del SD4 ([SD4:343,485,839][s4]; [SD4-A:447,470][s4a]) dicen «crítica **y** sostenida». Sólo el SD5 usa «o» ([SD5:141,227][s5]). Por la regla del equipo manda el subdocumento anterior, así que se alinean dos frases del SD5, que mantiene otra persona. Las líneas que cita el informe se corrieron (RNG-04 está en 534, el SD4 en 839 y el SD4-A en 447).
- **RI-08 — Cobranza de preventistas.** Vigente. RF-07.10 está en «Cumple» con M3/M7 ([T-12:87][t12]) y RF-07.11 en «No cumple», con M7 limitado al reparto ([T-12:88][t12]). Ambas filas citan como respaldo las mismas secciones (SD4 4.1.4.6, SD5 5.1.8). [SD3-A:230][s3a] reserva la cobranza a crédito al CLIENTE.
- **RI-10 — Réplica de las series térmicas.** Vigente. Las líneas del SD4 se corrieron: la copia diferida de cinco años de temperatura a us-east-1 está en [SD4:1994,3205][s4] y [SD5-A:1306][s5a] dice «sin réplica fuera de la región declarada». La severidad alta se sostiene por la afectación potencial de datos sanitarios; con la evidencia actual es una ambigüedad.
- **RI-11 — Figuras sin objeto. Severidad subestimada.** [SD1:142][s1] contiene «**Figura 1.1** … Fuente: Elaboración propia» sin imagen, sólo con una descripción textual ([SD1:140][s1]). Los seis destinos de figura del SD2 y los ocho del SD3 no existen en el repositorio. Las Aclaraciones dicen expresamente que «una leyenda sin su figura es indicio de generación por IA (sección 7.1, letra a)» ([ACL:71][acl]). Desde el Informe 2, ese indicio declara no presentado el subdocumento completo ([ACL:131][acl]). La frase del informe «Esto no es una acusación de IA» minimiza el riesgo. Debe pasar a **alta**, con riesgo de puntaje 0 en SD1, SD2 y SD3 si el PDF final no inserta las imágenes.
- **RI-12 — Reconexión en cámara.** Vigente ([SD3-A:282][s3a]; [SD3:207][s3]; [T-12:213][t12]). Se lee mejor como redacción ambigua que como un compromiso adicional; se mantiene en media.
- **RI-14 — Capacitación en Concepción.** Vigente. La estrategia está ahora en [SD3-A:603][s3a] (antes 602) y S-39 en [SD3-A:440][s3a].
- **RI-15 — Descuento excepcional.** Vigente. Además, la frase «La autorización de descuentos necesita un requerimiento propio» ([SD3-A:546][s3a]) se lee como una nota pendiente dentro de un entregable (riesgo del §7.1 d). Conviene reformularla aunque no se cree el requisito.
- **RI-17 — Mes 3 en el T-9.** Vigente. [T-9:75][t9] atribuye al T-14 la «instalación en mes 3» de racks, servidores y borde. El T-14 5.1.2 sólo instala la sala en el mes 3 ([T-14:1417][t14]) y la propia tabla del T-9 sitúa los racks en los meses 4–5 ([T-9:82–83][t9]).
- **RI-18 — Formulario del SD6-A.** Vigente: dice «Formulario: Formulario T-6» ([SD6-A:5][s6a]).
- **RI-19 — Cota por cross-docking.** Vigente. Las líneas se corrieron a [SD4:2729][s4] y [SD4-A:1475][s4a].

### Partes del informe que también quedaron desactualizadas

- La tabla de huellas del §1 ya no coincide: T-12, T-11 y SD9-A cambiaron después del corte.
- La decisión D-05 del §5 («modalidad SOC y tratamiento de terceros TLS») está resuelta en la parte SOC y decidida en la parte TLS.
- El «Orden de resolución» del §5 debe retirar RI-09 y RI-16, y pasar RI-05, RI-07 y RI-13 a correcciones directas.

## 3. Hallazgo nuevo

### N-01 — Predecesoras por cuenta en la Tabla 6.1 del T-15 incompatibles con sus fechas

**Severidad media · complejidad baja · corrección documental.** La nota de la tabla dice que las predecesoras van «agrupadas por cuenta del Anexo 7.B cuando dependen de toda la cuenta» ([T-15:548][t15]). En al menos once celdas, la cuenta citada contiene paquetes que terminan después del inicio del sucesor; leída literalmente, la red es infactible:

| Sucesor (inicio) | Predecesora | Paquete de la cuenta que termina después |
|---|---|---|
| 2.1.1 (01-03-2027) | 1.2 | 1.2.5 (09-02-2028) |
| 2.4.1 (19-04-2027) | 2.1, 2.2 | 2.1.4 (16-02-2028); 2.2.2 (meses 3–10) |
| 3.1.1–3.1.3 (01-06-2027) | 3.2 | 3.2.6 (29-06-2027) |
| 3.2.1–3.2.6 (03-05-2027) | 5.2 | 5.2.2/5.2.3 (11-05-2027) |
| 3.3.2, 3.4.7 (junio 2027) | 1.2 | 1.2.5 (09-02-2028) |
| 3.4.1–3.4.11 (junio–septiembre 2027) | 2.4 | 2.4.2 (13-03-2028) |
| 3.8.1 (01-10-2027) | 3.6 | 3.6.5/3.6.6 (julio–agosto 2028) |
| 4.2.3 (05-05-2028) | 7.3 | 7.3.2 (25-07-2028) |
| 5.1.2 (02-03-2027) | 2.3 | 2.3.3 (29-03-2027) |
| 6.1.1–6.1.5 (abril–mayo 2027) | 5.1 | 5.1.3 (09-06-2027) |
| 6.6.1–6.6.3 (10-06-2027) | 6.3 | 6.3.4 (20-10-2027) |

El Anexo 7.B sí declara las dependencias precisas: D-01 (1.2.1 → 2.1.1), D-04, D-07 (5.2.1), D-08 (3.2.1/2/4/5), D-09 (2.3.1/2.3.2), D-10, D-12 (6.3.1–6.3.3) y D-20 (3.6.1–3.6.4) ([SD7-A:42–61][s7a]). Con ellas, las fechas cumplen fin-comienzo. **Solución:** en la columna de predecesoras, reemplazar la cuenta por el rango de paquetes del Anexo 7.B (por ejemplo, «3.4, 3.6.1–3.6.4»), sin mover fechas ni HH. Las relaciones CC o «por interfaz» de D-15 a D-19 (dentro de 3.4) ya están explicadas y no se incluyen aquí.

### Observación técnica (no interdocumental)

[SD4:773,1093][s4] dicen que CloudWatch «conserva las métricas 13 meses». CloudWatch retiene las métricas estándar hasta 15 meses, con resolución decreciente, y ese plazo no se configura. La cifra no contradice a otro documento, pero conviene expresarla como «al menos 13 meses» o «15 meses».

## 4. Cruces automáticos sin hallazgos

- **Títulos obligatorios:** los 38 títulos de las Aclaraciones §11 que corresponden a los diez cuerpos existen con su redacción exacta.
- **Referencias internas:** las 1.167 referencias «SDn x.y» apuntan a encabezados existentes. Los 69 anexos referidos existen, igual que las Tablas A.n del SD4 (36) y del SD5 (27).
- **Identificadores:** S-01..S-44, E-01..E-09, RNG-01..16, V-01..18, R8-01..32, E8-01..14, INT-01..15 y D-01..D-34 (37 con sufijos) están definidos, sin referencias huérfanas.
- **Hitos H1–H10:** entrega, límite y P80 coinciden entre la Tabla 5.2 del T-15, la Tabla 8.5 y el Anexo 8.C del SD8 y las ventanas del T-13. El SD8 agrega P50, que es una magnitud distinta.
- **Innovaciones:** los meses de INN-01..05 coinciden entre SD13, T-14 y la sección 4 del T-15, y las fechas de la Tabla 6.1 caen dentro de esas ventanas. La única excepción de gate es RI-04.
- **Riesgos:** la probabilidad y el impacto de los 32 riesgos coinciden entre el FMEA del SD8-A y el T-16, y E = P × I. Las columnas «Análisis» y «Categoría» son dimensiones distintas, no contradicciones.
- **Conteos del catálogo:** 261/271/259/645 concilian entre SD3, SD9 y el T-12 (Parte A con 3 «No cumple»).
- **Filas del T-12 cerradas hoy:** RT-02.10/RNF-19.02, RT-03.08, RT-04.13, RT-14.08 y RT-16.24 coinciden con el texto del SD4 y del T-11: de 2 a 4 tareas con techo de 8; registros 12 + 24 meses, métricas 13 y trazas 30 días; 2.800/5.200 avisos diarios.
- **Cálculos del §2.1 del informe:** 21 × 288 + 28 × 174 = 10.920; 16,05478 × 2 = 32,10956; 7.450 × 1,2 = 8.940; 5 + 30 + 20 + 30 + 15 + 15 + 5 + 15 = 135 min; 20.948,16 frente a 20.198,98 HH en el SD8. Todos correctos.
- **Cifras obsoletas:** 218.720, 206.312, 202.774, 190.366, 56.024, 130.158,67, 19.448,58, 15.076, 13.223, 12.004, 29.647, 1.282, 1.288 y «43 supuestos» no aparecen en ningún entregable. Django/Python sólo aparece como alternativa descartada en las decisiones de arquitectura del SD4.

## 5. Límites

Esta validación no es una relectura semántica línea a línea de los 2,6 MB de entregables. Combina tres cosas: la verificación de las 19 fichas contra el texto actual, los barridos automáticos de la sección 4 y lecturas focales. Los seis frentes de lectura completa encargados a Codex (alcance, arquitectura, datos, plan, riesgos/calidad/innovación y T-12) no se ejecutaron porque se agotó su cuota de uso; las instrucciones quedaron listas para correrlos. No se acreditan ensayos, PDF, figuras finales ni revisión humana.

[s1]: ../01_presentacion_empresa/LAFROX-Subdocumento1.md
[s3]: ../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md
[s3a]: ../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md
[t12]: ../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md
[s4]: ../04_arquitectura/LAFROX-Subdocumento4.md
[s4a]: ../04_arquitectura/LAFROX-Subdocumento4-Anexos.md
[s5]: ../05_modelo_datos/LAFROX-Subdocumento5.md
[s5a]: ../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md
[s6]: ../06_metodologías/LAFROX-Subdocumento6.md
[s6a]: ../06_metodologías/LAFROX-Subdocumento6-Anexos.md
[t9]: ../06_metodologías/LAFROX-Formulario-T-9.md
[s7a]: ../07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Subdocumento7-Anexos.md
[t14]: ../07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-14.md
[t15]: ../07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-15.md
[s9a]: ../09_plan_calidad/LAFROX-Subdocumento9-Anexos.md
[s13]: ../13_innovaciones/LAFROX-Subdocumento13.md
[acl]: ../Bases/aclaraciones-licitacion.md
