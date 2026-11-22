# Registro de cambios del SD13 — revisión profunda de coherencia (18-11-2026)

Uso interno, no se entrega. Cada fila es un cambio, con su motivo, su evidencia y su estado. Los ID siguen el plan de la revisión (F1 a F4). Los cambios de texto quedaron en el commit `fe589880` y las figuras en `2a90d102`.

Abreviaturas de archivos: **C** = `13_innovaciones/contenido.tex` (cuerpo), **T** = `T19/contenido.tex` (T-19), **A** = `13_anexos/contenido.tex` (anexos). T-14 y T-15 son los del SD7 (`sd7-corrigiendo`, commit `b8bededf`). Bases: BA = Bases Administrativas, BTT = Bases Técnicas Transversales, Caso = PDF oficial «Caso 02 - Logística» (página impresa).

## Fase 1 — EDT antigua, hitos y texto de proceso

| ID | Dónde | Cambio | Motivo | Evidencia | Commit | Estado |
|---|---|---|---|---|---|---|
| F1-01 | A, 13.B (cotejo de hitos) | Paquetes controlantes de H4, H5 y H10: 3.8.1, 3.8.7 y 3.9.6 pasan a 6.1.1, 6.7.1 y 6.7.2 | Códigos de la EDT antigua | SD7 `tab_T15_7.tex:8,9,14`; `tab_T15_paquetes.tex:90,103,104` | fe589880 | hecho |
| F1-02 | C 13.2.5; A matriz 13.B; T ficha 2 campo 10 | «cuenta 3.8» pasa a «cuentas 6.1 a 6.6» | Las pruebas son del producto 6, no del 3 | SD7 `formulario-t14/tablas/tab_T14_1.tex:6` | fe589880 | hecho |
| F1-03 | C 13.4.4 | Se borra «el primer paquete está en la fase 5»; queda «7.4.1 es un acuerdo con el CLIENTE y no un desarrollo» | Resto del antiguo 5.4.3 | SD7 `dic_7_4.tex:4` | fe589880 | hecho |
| F1-04 | C 13.5.4 | Se borra la justificación de la subcuenta 7.4 sin paquetes de construcción | Justificaba una numeración que ya no existe | SD7 `PROPUESTA_EDT_PAQUETES_2026-11-17.md` | fe589880 | hecho |
| F1-05 | A 13.B | Se quita la «carta editable de 17 paquetes y 7 enlaces»; se remite a la red del T-15; se aclara que el fin temprano CPM no incluye la marcha blanca; la secuencia de 7.4.1 a 7.4.3 es criterio del T-14 | La carta usa códigos 3.10.x y el cuento de paquetes no coincide | `revision/Gantt_Innovaciones_13B.gan`; SD7 `tab_T15_10.tex:28-33` | fe589880 | hecho |
| F1-06 | C tabla 13.8 (7.2.3) | Se agrega «programado hasta el 08-10-2027; fin tardío CPM 30-11-2027» | Los meses «5 a 10» del T-15 y la fecha no calzaban a simple vista | SD7 `tab_T15_paquetes.tex:113`, `tab_T15_cpm_detalle.tex:112` | fe589880 | hecho |
| F1-07 | A 13.C; C declaración de IA | Se elimina la «Pauta de revisión técnica» y el texto «pendiente / no acredita»; la Tabla 13.29 lleva fuente y frase de cierre | Indicio de IA y de proceso interno (ACL 7.1 d) | Aclaración (ACL) 117-155 | fe589880 | hecho; **la revisión técnica humana sigue pendiente de ustedes** |

## Fase 2 — Coherencia interna

| ID | Dónde | Cambio | Motivo | Evidencia | Commit | Estado |
|---|---|---|---|---|---|---|
| F2-01 | C 13.2.4; T ficha 5 campo 8 | Traspaso a Operación en el mes 21 (INN-02: Pérez hasta el mes 20); INN-05: «desde el despliegue por rutas del mes 22» | Mezcla de meses 21 y 22 | SD7 `tab_T15_1.tex:11`; BA Art. 17 | fe589880 | hecho; aviso al SD8 (Tabla 8.1 dice 22) |
| F2-02 | C tabla 13.22 | R-027: «3 × 3 inicial; 2 × 3 residual» | Mezclaba inicial y residual | SD8 `LAFROX-Formulario-T-16.tex:64,125` | fe589880 | hecho; aviso a SD3 (T-12:709) y SD9 |
| F2-03 | C 13.1.7, 13.2.7, 13.3.7, 13.5.7 | Cada exposición muestra el valor del nivel (0,30 o 0,50) y «30 \%» con espacio | 25 % × 0,10 no da 0,03 si no se explica el nivel | Escala del SD8 (tablas 8.2 a 8.4) | fe589880 | hecho |
| F2-04 | C intro; A 13.C; T campos | «13.x.7» → lista de las cinco secciones; «Anexo 13.B.1/13.C.1» → «sección 13.B.1/13.C.1»; 13.B.1 retitulada | Marcador sin resolver y referencia ambigua | — | fe589880 | hecho |
| F2-05 | C 13.3.5; T ficha 3 campo 12; A matriz | Las 150,6 recepciones ponderadas se equiparan a lotes solo para dimensionar y como tope (familias habilitadas una a una) | Contradecía «no contar recepciones como lotes» | A registro de datos INN-03 | fe589880 | hecho |
| F2-06 | C 13.5.5; T ficha 5 campo 12; A | Beneficio de INN-05: creciente entre los meses 22 y 26 y completo desde el 27; 14.200 = clientes activos; «2.600 por día hábil» aclarado | Se contaba el beneficio completo antes del despliegue por rutas | C 13.5.4 (despliegue de 22 a 26) | fe589880 | hecho |
| F2-07 | C, A, T I-04A | «OTIF en la meta vigente (95 % en la evaluación del mes 36)» | La meta de los meses 24-31 es 93 % | C 13.4.2 (90/93/95 %); SD3 R18-04 | fe589880 | hecho |
| F2-08 | C intro; 13.1 a 13.3 | Se agrega la regla de términos: «Calidad» (CLIENTE) y «Calidad y Pruebas» (LafroX); se desambiguan siete menciones | «Calidad» designaba dos áreas | BTT 19.2 (roles) | fe589880 | hecho |
| F2-09 | C 13.1.5, 13.3.4, 13.3.5; T fichas 2 y 3 | Responsables iguales en cuerpo y T-19; parámetros de INN-03 aprobados por Calidad del CLIENTE y validados por el Líder de Calidad y Pruebas; participaciones sin horas propias; se quita «Datos participa en los meses 30 y 48» | El T-15 asigna solo perfiles de datos a 7.1 y 7.3; frase sin respaldo | SD7 `tab_T15_asignacion_partidas.tex:135-157` | fe589880 | hecho; aviso al SD7 (frentes del T-14 frente al T-15) |
| F2-10 | A 13.B | Se quita «un rubro en cada clase»; se borra la descripción del método económico y las 533/154 HH del modelo; perfiles «Ingeniero de Datos y Bases»; EV-15 «derivadas proporcionalmente del T-15» | Riesgo frente al Art. 50.2 y nombres de perfil exactos | BA Art. 50.2; SD7 `tab_T15_perfiles_internos.tex` | fe589880 | hecho |
| F2-11 | A tabla 13.C.1 | Momentos de medición iguales a los del cuerpo (I-02B, I-02C, I-03A, I-03B, I-03C, I-04C) | Anexo y cuerpo se contradecían | C tablas de indicadores | fe589880 | hecho |
| F2-12 | C, A, T | Frase de cierre de la Tabla 13.1; INN-05 «Mes 21 (producción); rutas en 22 a 26»; pies «7.x.1 a 7.x.n»; duplicados; «1.100»; «o 7.3.5»; «CLIENTE»; Subdocumento N en vez de SDn; campo 15 de la ficha 5 con 7.5.1 y 7.5.3; frase sobrante de A reemplazada por un cierre | Redacción y nomenclatura | ACL 37-111 | fe589880 | hecho |
| F2-13 | C 13.N.7 | Títulos uniformes «Riesgo de adopción y controles» | Los cinco títulos eran distintos | REV2 / rúbrica | fe589880 | hecho |
| F2-14 | T campo 1 | «Tipo de innovación (1 a 5)» | Redacción oficial del T-19 | BA T-19 (campo 1) | fe589880 | hecho |

## Fase 3 — Coherencia con otros subdocumentos

| ID | Dónde | Cambio | Motivo | Evidencia | Commit | Estado |
|---|---|---|---|---|---|---|
| F3-01 | A matriz 13.B | INN-03 con capas 1, 2, 4, 5, 6, 7 y 8; INN-05 agrega C-02 | Anexo 4-N | SD4 `15_anexo_4_1_n…tex:64,66` | fe589880 | hecho; aviso al SD4 (INN-05 sin capa 5) |
| F3-02 | C intro | «Capítulo 3, secciones 3.1.1 y 3.4» | La 3.4.2 no trata las innovaciones | SD3 `contenido.tex:17,279` | fe589880 | hecho |
| F3-03 | C tablas 7.5.4; T ficha 5 | Marcha blanca entre el acta del H10 (11-07-2028) y la del H12 (17-10-2028) | 7.5.4 se acepta en el acta del H12 | SD7 `dic_7_5.tex:7`; `tab_T15_7.tex` | fe589880 | hecho; aviso al SD7 (rótulo «18–21») |
| F3-04 | C 13.4.5 | 7.4.1 programado en el mes 17 con fin tardío CPM el 29-09-2028 | Usaba datos de los meses 19 y 20 | SD7 `tab_T15_paquetes.tex:119`, `tab_T15_cpm_detalle.tex:118` | fe589880 | hecho |
| F3-05 | C 13.1.4 y 13.3.4 | Párrafos de H4 reescritos; el fin tardío CPM coincide con el límite del H4 | Eran casi idénticos y negaban la coincidencia | `tab_T15_cpm_detalle.tex:107,108,116` | fe589880 | hecho |
| F3-06 | C 13.3.3 y 13.3.6 | Se explica que en los trimestres sin revisión programada (33 y 45) el corte de I-03B se registra y activa recalibración si marca deriva | El T-15 omite los meses 33 y 45 | SD7 `tab_T15_10.tex:29` | fe589880 | hecho; aviso al SD7 |

## Fase 4 — Bases, Art. 30, RT-26 y fuentes

| ID | Dónde | Cambio | Motivo | Evidencia | Commit | Estado |
|---|---|---|---|---|---|---|
| F4-01 | C, T, A | Páginas del Caso: Riffo p. 17 y p. 16, Ñanco p. 15, cap. 13.2 p. 22, cap. 6 p. 11, sección 14.1 p. 24, anexo B.1 p. 38; páginas agregadas a las citas de T y A | Citas con página equivocada o sin página | PDF oficial «Caso 02 - Logística», páginas impresas | fe589880 | hecho (p. 24 y p. 38 vienen de la auditoría; **revisar a ojo**) |
| F4-02 | C tablas 13.7 y 13.12 y textos de aporte | INN-02: RT-04.14, RT-21.17, RT-14.01, RT-14.07 y RT-04.12 pasan a alcance obligatorio; INN-03: RT-03.10, RT-03.19 y RT-05.30; el aporte se restablece | Art. 30 / REV2 («doble uso») | BTT p. 11, 27, 37 y p. 9 (PDF oficial); T-12 `391`, `372` | fe589880 | hecho; **alinear el T-12 (RT-04.14 «por INN-02»)** |
| F4-03 | C 13.intro, 13.2.5; A; figura 13.3 | RT-26.08: el beneficio medible antes del mes 16 es el de Puelche (aviso a reanudación); I-02A es adicional; rótulo de la figura 13.3 «medición al mes 15» | El beneficio era del proveedor | REV2 (~1351); BTT p. 45 | fe589880 | hecho |
| F4-04 | C 13.2.4 y 13.5.4; T ficha 5 campo 16 | Tablas de modelado de amenazas (RT-26.07) para INN-02 y INN-05 | Solo estaba prometido | BTT p. 45 (RT-26.07), p. 31 (RT-17.05) | fe589880 | hecho |
| F4-05 | C 13.1.2 y 13.3.3; T ficha 3 campo 13 | INN-03: variables, métrica, línea base (fecha impresa como modelo nulo), deriva y rotulado automático (RT-18.07/08); INN-01: estimador declarado | RT-18.08 pide línea base | BTT p. 32 | fe589880 | hecho |
| F4-06 | C, T, A | INN-01: sensibilidad de 0,15 % (900 unidades/mes); INN-02: la frecuencia semanal la da el Caso; INN-04: beneficio en 21.000 km/mes en vez de 20 minutos-persona sin fuente | Supuestos sin respaldo | Caso p. 8, p. 34, p. 5 | fe589880 | hecho |
| F4-07 | C 13.1.6 y 13.3.5; A; T | Contrastes de INN-01 e INN-03 en los mismos meses del año (25 a 27 frente a 13 a 15) y declaración de que no hay control simultáneo | Estacionalidad | — | fe589880 | hecho; **decisión de diseño suya** (no se mantienen rutas de control) |
| F4-08 | A 13.C | Justificación de los tamaños de muestra (100 avisos, 60 lotes, 20 de 24) | ACL: toda cifra se justifica | cálculo del intervalo binomial | fe589880 | hecho |
| F4-09 | C 13.2.2, 13.2.3, 13.3.2, 13.3.3, 13.4.3, 13.5.3 | Fuentes acotadas a lo que respaldan; los TRL se declaran como juicio propio | Sobredeclaración | Fichas de Shahin, DORA, Koutsoumanis, Sweeney, Hundepool, Goo | fe589880 | hecho |
| F4-10 | C, A | «valor mensual ofertado» (no «precio máximo»); «especialista dedicado»; «Puelche registra qué compra…» | Términos no definidos / paráfrasis | CASO restricción 9 | fe589880 | hecho |

## Cambios previos de la sesión (ya con commit)

Renumeración EDT, hitos y R-027, riesgo de adopción en cada 13.N.7, fuentes y APA 7, figura 13.4, portada del 25 de noviembre de 2026: ver `git log` de la rama (commits `da451d9b` a `3164b2da`).

## No hecho o pendiente de ustedes

| ID | Tema | Qué falta |
|---|---|---|
| P-01 | Revisión técnica humana (SD13-12) | Revisor, fecha, versión, evidencia y resultado por innovación y para la figura 13.1; recién ahí se actualiza la declaración de IA |
| P-02 | Títulos de las referencias 2026a y 2026c | Compararlos con la portada de cada PDF oficial («Bases para la preparación de la propuesta…», «Bases Técnicas del Caso 02 — Logística») |
| P-03 | Multas (C 13.4.2) | Citar el artículo de las Bases Administrativas con su página; no se verificó el Art. 80° |
| P-04 | Carta Gantt `Gantt_Innovaciones_13B.gan` y `verificar_cotejo_sd13.py` | Siguen con los códigos antiguos y commits fijados; el verificador nuevo los reemplaza; decidir si se archivan |
| P-05 | Páginas 24 y 38 del Caso | Confirmar a ojo en el PDF oficial (vienen de la auditoría, no de una lectura directa) |

## Auditoría de regresiones (18-11-2026) — corregido y pendiente

Corregido, sin commit: duplicado y «minutos-persona» de INN-04 (C 13.4.5, A registro de datos); calendario de 7.4.1 (C 13.4.5, T ficha 4); T-19 ficha 3 (aporte sin el borde, TRL por juicio propio, «Calidad y Pruebas», sin horas de Calidad); aprobación de parámetros de INN-03; OTIF «más de 95 %»; fila RT-03.10/03.19 de la tabla 13.12; predecesoras en A; aclaración del 30 % de INN-02; deriva del estimador de INN-01; citas del Caso sin autor; minúsculos (puntuación, «Operación / SRE», impacto 0,20 de R-027, RT-21.17, cap. 18 criterio 11, ventana 7.1.4).

Pendiente (no hecho): M4 frases que introducen o cierran tablas (13.20, 13.25, 13.C, fichas 1 a 4) y \ref de `tab:sd13-B-calendario` y `tab:sd13-C-datos`; M5 celdas con varias oraciones; M10 declaración de IA (nombres de revisores y «Se comprobó la aritmética»; depende de P-01); m3, m5, m6, m8, m10, m11, m13 de redacción; m14 figura 13.6 («I-05B antes del mes 19» debe decir mes 14) y figura 13.1 sin el gateway B-04; revisar los «Overfull hbox» tras recompilar; la numeración de tablas citada arriba cambió al insertar las tablas de amenazas.

## Auditoría de errores descalificantes (18-11-2026) — sin corregir

### Graves (prioridad)
- **A1 Declaración de IA:** «Se comprobó la aritmética» sin responsable; filas solo con revisión editorial; 13.1-13.5 declaradas «Medio». Obs. vinculante del Informe 2 abierta. Depende de P-01 (revisión técnica real).
- **A2 INN-03:** el modelo se oferta como RT-05.30 (T-12:421 «Cumple») y el borde como RT-03.19; lo que queda como aporte (decisión de Calidad y orden de salida) no es tecnología de tipo 3. Contradicción interna: I-03D mide central frente a borde. SD3:17 y SD5 5_1_modelo:262 dicen que el aporte es el cálculo sin enlace. Elegir: (a) retirar el «Cumple» de RT-05.30 en T-12 y devolver modelo, EPCIS y borde a INN-03; (b) mantener RT-05.30 y redefinir INN-03 e I-03D.
- **A3 INN-02:** RT-04.14 (deseable) figura como obligatorio y la propia INN-02 lo implementa (T-12:391 lo cumple «por INN-02»); el beneficio de Puelche usado para RT-26.08 no tiene indicador formal (falta I-02E con base, regla de asignación del brazo «sin circuito», meta y mes 15); T-12:713 dice que RT-26.08 lo cumple I-02A.
- **A4 Códigos EDT antiguos en otros formularios:** T-12 (SD3) líneas 391, 421, 628, 707, 713; T-16 (SD8):64 y anexo F:48 («5.4.3»); T-13 (SD9) 386, 426, 673, 767, 770, 773. Dueños de SD3, SD8 y SD9.
- **A5 INN-04 redactada como oferta condicionada:** «el contrato vuelve a la estructura de las Bases» (C 13.4.7, T ficha 4 campo 17, Fig. 13.5) y «si no se aprueban las reglas, no se activa el tramo». Riesgo Art. 53. Reescribir dentro de E-25 y E-21 1.2; coordinar con la Oferta Económica.
- **A6 Portada sin media firma abajo a la derecha** (Art. 40.2 y Art. 53). Plantilla compartida `lafrox-portada.tex`.
- **A7 Figuras contradicen el texto:** 13.1 sin B-04/B-08; 13.4 «B-03: camión» y C-02 como alarma (el texto dice B-04); 13.6 «I-05B antes del mes 19» (texto: mes 14); 13.3 «Calidad admite» (debe ser Calidad y Pruebas).

### Medios (anotados, no prioritarios)
- Cuerpo a 10,9 pt (Art. 40.4 pide 11); clase compartida.
- Metadatos del PDF con título «Propuesta Técnica — Informe 2».
- 7.4.1 en 7 días del mes 17 frente a datos de los meses 19-20 (SD7).
- A:52 reconoce que la red del T-15 está incompleta para INN-04.
- RT deseables (04.14, 03.19, 05.30) bajo «Ya es alcance obligatorio».
- Papel térmico de INN-05 asignado a Puelche sin respaldo en el T-11.
- Dedicación del Líder de Datos «meses 1 a 20» frente a 57,6 HH del perfil 23 en 7.3.5.
- R-027 2×3 en T-12:709 frente a 3×3 inicial en SD13 (SD3).
- Familia de esfuerzo de 7.3.5, 7.5.5 y 7.5.6: SRE en T-14, DAT/IMP en T-15 y SD13 (SD7).
- Capa 5 de INN-05 ausente del Anexo 4-N (SD4).
- «Kit B-03 a B-15» frente a T-11 (B-03 a B-14; B-15 es la SIM).
- HH por perfil en las sesiones EV-15 (riesgo bajo de inferir costos).
- Conciliación de hitos del Anexo 13.B densa: el equipo debe poder explicarla.

### Menores (anotados)
- Título del índice de 13.B.1 distinto del encabezado; `tab:sd13-B-calendario` y `tab:sd13-C-datos` sin \ref; tipografía pequeña (nombre de contrato 9,2 pt, subíndice p₀, cabeceras 7,5 pt); «Caso — Logística» sin número frente a los metadatos; títulos de 2026a y 2026c; 7.3.2 «5 a 9» (termina en el mes 8); redacción de aprobación de 7.3.1 frente al T-14; E-21 citado en p. 70 y p. 71; escenarios de INN-02 e INN-03 pequeños.

## Decisión A2 (18-11-2026): INN-03 deja de responder al RT-05.30

| ID | Dónde | Cambio | Motivo | Evidencia | Commit | Estado |
|---|---|---|---|---|---|---|
| A2-01 | C tabla 13.12 | Se quita la fila RT-05.30 del alcance obligatorio y de la fuente; la fila RT-03.10/03.19 se acota a «filtrado y agregación genéricos en el gateway» | Decisión de ustedes: retirar el «Cumple» de RT-05.30 del T-12 | Obs. del Informe 2 (doble uso); BTT RT-05.30 deseable, p. 13 | fe589880 | hecho |
| A2-02 | C 13.3.2 («Modelo analítico y alcance propio») | El modelo cinético, la acumulación de carga térmica por lote en el gateway, la proyección por lote en EPCIS 2.0 y la decisión de Calidad del CLIENTE son la tecnología de INN-03 | Art. 28 tipo 3 | SD3 `contenido.tex:17`; SD5 `5_1_modelo.tex:262` (ahora coherentes) | fe589880 | hecho |
| A2-03 | T ficha 3 campo 4 | Misma redacción que el cuerpo | Coherencia cuerpo / T-19 | — | fe589880 | hecho |
| A2-04 | SD3 T-12 | **Aviso al dueño del SD3:** en `LAFROX-Formulario-T-12.tex:421` (RT-05.30) retirar el «Cumple» por INN-03; revisar `:628` (RT-18.08) para que no dependa de INN-03 como respuesta a RT-05.30 | Doble uso | — | — | aviso |

## Graves A3, A5 y A7 (18-11-2026)

| ID | Dónde | Cambio | Motivo | Evidencia | Commit | Estado |
|---|---|---|---|---|---|---|
| A3-01 | C 13.2.6, A 13.C.1, T ficha 2 campos 13-14 | Nuevo indicador **I-02E** (mediana de minutos aviso→reanudación; base: incidentes sin circuito de los meses 13 a 15; meta −30 % con ≥ 20 pares; mes 15) y regla de asignación al brazo con o sin circuito por orden de llegada | El beneficio de RT-26.08 no tenía indicador formal | REV2 ~1351; BTT p. 45 | fe589880 | hecho |
| A3-02 | C tabla 13.7 | RT-04.14 rotulado «requisito deseable ofertado como alcance base» | No es obligatorio | BTT p. 11 | fe589880 | hecho; **aviso al SD3: T-12:391 no debe atribuir RT-04.14 a INN-02; T-12:713 debe citar I-02E para RT-26.08** |
| A5-01 | C 13.4.7 y 13.4.8; T ficha 4 campo 17; Fig. 13.5 | Se elimina «el contrato vuelve a la estructura de las Bases» y «no se activa el tramo»; ahora el pago sigue la estructura de valor mensual fijo más variables de servicio de E-25 y E-21 1.2 | Riesgo de oferta condicionada (Art. 53) | BA E-25 p. 74, E-21 1.2 p. 70 | fe589880 | hecho; coordinar con la Oferta Económica |
| A7-01 | Figuras 13.1, 13.3, 13.4, 13.5, 13.6 | 13.1 y 13.4: B-04 en el camión con B-03 y B-08 de respaldo; 13.3: «Calidad y Pruebas»; 13.6: «I-05B en el mes 14»; 13.5: texto de contingencia | Contradecían el texto | `gen_diagramas.py`, `gen_recorridos.py`, drawio | 2a90d102 | hecho; **revisar a ojo la figura 13.1 (caja más larga)** |

## Formato (18-11-2026)

| ID | Dónde | Cambio | Motivo | Evidencia | Commit | Estado |
|---|---|---|---|---|---|---|
| A6-01 | `sd13-comun.tex` (`\LFXpiefolioen`) | La portada de los tres documentos lleva media firma en el extremo inferior derecho, además de la firma completa | Art. 40.2: media firma en cada página y firma completa en la carátula | BA Art. 40.2 (línea 664) | ver `git log` | hecho |
| FM-01 | `sd13-comun.tex` (`\normalsize`) | Cuerpo a 11,1 pt de TeX (11,06 pt de Word) | Art. 40.4: no inferior a 11 pt; la opción 11pt compone a 10,91 pt | BA Art. 40.4 | ver `git log` | hecho; el cuerpo pasó de 60 a 61 páginas |
| FM-02 | `sd13-comun.tex` (`\LFXcuerpofigura`) | Cuerpo de figura a 9,2 pt de TeX | 9 pt de TeX son 8,97 pt de Word | BA Art. 40.4 | ver `git log` | hecho |
| FM-03 | `sd13-comun.tex` (`\hypersetup`) | Título del PDF «Propuesta Técnica — Subdocumento 13 — Innovaciones — Propuesta final» | Decía «Informe 2» | metadatos del PDF | ver `git log` | hecho |

Pendiente de formato (menor): el asunto de los metadatos sigue diciendo «Caso 02 — Logística» (la portada dice «Caso — Logística»); los subíndices de p₀ se componen a 6,6-7,6 pt por ser subíndices; las cabeceras y pies están a 7,5 pt (no son cuerpo ni tabla).

## Revisión de ramas actualizadas (19-11-2026)

| ID | Dónde | Cambio | Motivo | Evidencia | Commit | Estado |
|---|---|---|---|---|---|---|
| RV-01 | C, A y T | Sin cambios de contenido. Se revisan los commits nuevos de SD3 (`3ee615a9`), SD4 (`0dc50b3d`), SD7 (`315e89b5`), SD8 (`530d5224`) y SD9 (`84c12443`) | EDT por productos, cascada y recodificación de citas en los otros subdocumentos | `verificar_coherencia_sd13.py`: OK; fechas de hitos, CPM de 6.1.1 y de la cuenta 7, perfiles y Tabla 23 del T-15 sin cambios; el T-14 de 7.4.1 coincide con el SD13 | — | hecho |
| RV-02 | PDF y auxiliares de las tres piezas | Se recompilan con LuaLaTeX; el índice y la lista de tablas del cuerpo corrigen páginas desde 13.4.5 | El commit `51d750cf` dejó el índice de una pasada anterior | `LAFROX-Subdocumento13.toc` | — | hecho |
| RV-03 | Hoja de dependencias | Commits al 19-11-2026, SD9 agregado, diferencias resueltas separadas de las abiertas y nueva diferencia del SD8 en R-027 (mes 20 contra mes 17) | Mantener la hoja al día | `HOJA_DEPENDENCIAS_SD13.md` | — | hecho |

## Revisión de ramas actualizadas (22-11-2026)

| ID | Dónde | Cambio | Motivo | Evidencia | Commit | Estado |
|---|---|---|---|---|---|---|
| RV-04 | A, sección previa a 13.B.1 | 7.1.4, 7.2.4 y 7.3.4: se reemplaza «fin temprano CPM 28-12-2027» por la carta nivelada del T-15 (01-12-2027 a 28-04-2028, fin igual al tardío, holgura cero) | El T-15 de SD7 `0624f701` publica fechas niveladas; el 28-12-2027 ya no figura | `tab_T15_cpm_detalle.tex` y `tab_T15_paquetes.tex` en origin; `verificar_coherencia_sd13.py` marcaba anexos:56 | — | hecho |
| RV-05 | A 13.B.1 | Se reemplaza «las entregas de H4, H5 y H10 coinciden con el fin temprano de sus paquetes de control» por «preceden el fin de 6.1.1 (22-10-2027), 6.7.1 (01-12-2027) y 6.7.2 (28-06-2028)» | La carta nivelada mueve esos fines; la frase contradecía los párrafos siguientes del anexo | `tab_T15_cpm_detalle.tex` y `tab_T15_7.tex` en origin | — | hecho |
| RV-06 | Hoja de dependencias | Commits de SD7, SD8 y SD9 al 22-11-2026; alineación de CT-08 a CT-13 del SD8 como resuelta; nueva diferencia menor en el texto CPM del T-15 | Mantener la hoja al día | `HOJA_DEPENDENCIAS_SD13.md`; verificador OK con las fuentes de origin; Anexos recompilados con LuaLaTeX sin errores | — | hecho |
| RV-07 | C, A y T | Sin cambios de contenido. Se revisan los commits de la tarde de SD3 (`f7ff197d`), SD4 (`77dca497`), SD7 (`8e71a160`), SD8 (`90868f52`) y SD9 (`3ec8689e`): fecha de emisión unificada al 25-11-2026, sin «§», R-027 a 3 × 3 (0,10) en T-12 y SD9 | Cierre para la entrega final | `verificar_coherencia_sd13.py`: OK; el SD13 ya tenía la fecha y no usa «§»; T-16:64 y 125 coinciden con el Anexo 13.C y el T-19; PDF de las tres piezas compilados desde `e03909f9` sin referencias indefinidas | — | hecho |
| RV-08 | Hoja de dependencias | Commits al 22-11-2026 (tarde); P-01, P-02, P-03 y P-05 cerrados con su evidencia; queda abierto P-04 | Mantener la hoja al día | `HOJA_DEPENDENCIAS_SD13.md`; PDF oficial del Caso, pp. 24 y 38 | — | hecho |
