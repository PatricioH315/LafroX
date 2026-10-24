# Análisis de coherencia de los 10 subdocumentos (SD1–SD9 y SD13)

Revisión inicial: 23-10-2026. **Última actualización: 23-10-2026 (noche)**, después de publicar las correcciones del SD4 y de las citas al SD4 en SD3, SD7 y SD9.

Cada hallazgo indica su estado: ✅ resuelto, 🟡 parcial, ⬜ abierto.

## 1. Qué se revisó

Se leyó la última versión publicada en cada rama remota (`git fetch` + `git show origin/<rama>`), no los checkouts locales.

| SD | Rama remota | Commit revisado al inicio | Commit actual |
|---|---|---|---|
| SD1 | `LafroX-Subdoc1-LateX` | `938945a` | `938945a` |
| SD2 | `LafroX-Subdoc2-LateX` | `9aaffa7` | `9aaffa7` |
| SD3 | `LafroX-Subdoc3-LateX` | `01e8b60` | `47c8516` |
| SD4 | `subdoc-4` | `5abf4c6` | `7fb3a1f` |
| SD5 | `LafroX-Subdoc5-LateX` | `2f93655` (sin PDF en la rama; se compiló) | `2f93655` |
| SD6 | `LafroX-Subdoc6-LateX` | `d4b8849` | `d4b8849` |
| SD7 | `LafroX-Subdoc7-LateX` | `25002fd` | `246e63f` |
| SD8 | `Lafrox_Subdocumento_8_Latex_Nuevo` | `5934117` (cuerpo compilado desde `main.tex`) | `fb3360f` |
| SD9 | `LafroX-Subdoc9-LateX` | `5cac7ca` | `a4e1c63` |
| SD13 | `LafroX-Subdoc13-LateX` | `83ecc44` | `83ecc44` |

No se revisaron `LafroX-Subdoc4-LateX` (solo README), `Lafrox-Subdoc7-Latex-Tomas` (versión anterior del SD7), `LafroX-Subdoc8-LateX` (SD8 anterior, solo para comparar) ni SD10–SD12 (solo README).

Método: extracción del texto de los 33 PDF, matriz de cifras y nombres clave, verificación automática de cada código, tabla, figura, sección y anexo citado contra el documento dueño, y revisión cruzada independiente con Codex. Cada hallazgo se comprobó con la cita textual en el PDF.

Reglas aplicadas: `aclaraciones-licitacion.md` (§7.1 c: contradicción entre subdocumentos anula el subdocumento; §7.1 d: marcadores, notas, referencias inexistentes o texto que rompe la ficción también lo anulan) y la regla del equipo de que, en una contradicción, gana el subdocumento anterior.

**Decisión tomada:** el SD8 que se entrega es el nuevo (`Lafrox_Subdocumento_8_Latex_Nuevo`, riesgos R-001…R-045) y los demás subdocumentos deben citar sus códigos.

## 2. Correcciones publicadas el 23-10-2026

| Rama | Commits | Qué cambió |
|---|---|---|
| `subdoc-4` | `3d5f1e9`, `7fb3a1f` | Sin PUCV: Bases Técnicas Transversales = Distribuidora Puelche S.A. (2026b) y Caso 02 = (2026c) en cuerpo, anexos y T-11, con sus tres listas de referencias. «M10 Analítica» y «M11 Canal moderno» en el texto. El 41 % sin lote se limita al producto retirado (cuerpo y Anexo 4-W). R8-05 → R-015. Tres PDF de `entrega/` recompilados. |
| `LafroX-Subdoc3-LateX` | `e02fbc0`, `63d1047`, `47c8516` | T-12: 21 citas a tablas y figuras del cuerpo del SD4 y 6 a tablas de sus anexos pasan a la numeración vigente, elegidas por tema. R8-05 → R-015. |
| `LafroX-Subdoc9-LateX` | `a4e1c63` | SD4 Tabla 31 → 21; SD4 Tabla 16 → sección 4.2.4.3; AL-SYNC-01 → AL-ACT-01; Anexo 5-L → 5-K. |
| `LafroX-Subdoc7-LateX` | `c4fbe78`, `246e63f` | T-18: Tabla 14 → Tabla 8 del SD4. R8-05 → R-015 en cuerpo, anexos y T-18. El T-18 se recompiló con sus listas de tablas y figuras. |
| `Lafrox_Subdocumento_8_Latex_Nuevo` | `5d56ba2`, `fb3360f` (tuyos) | Declaración de IA del cuerpo reescrita: sin «en clases», sin «la revisión humana permanece pendiente» ni «podemos saltarnos». |

Verificación: comparación palabra a palabra de cada PDF antes y después (solo cambiaron las citas previstas y ninguno cambió de cantidad de páginas), compilación sin errores ni referencias rotas, y verificador automático de todas las citas al SD4 en los 10 subdocumentos: hoy todas existen y tratan el tema citado.

## 3. Resumen del estado actual

Lo más grave que queda:

1. **SD8**: las fichas del Anexo 8.A siguen con «Pendiente de definición por responsable» (45 veces en el fuente), el cuerpo conserva «[Fecha de emisión no verificada.]», «pendientes de validación», la nota sobre la «codificación anterior R8» y las remisiones C.5 y E8-xx.
2. **Riesgos y anexos del SD8 citados con la codificación antigua**: SD3, SD7 y SD13 siguen usando R8-xx (salvo R8-05, ya corregido) y los Anexos 8.C–8.F, que no existen en el SD8 nuevo.
3. **SD7 (T-15)** declara que su red, reservas y ruta crítica son un «escenario histórico» «pendiente de recálculo».
4. **SD6** contradice el SOC propio, no tiene figuras y cambió títulos obligatorios.
5. **Figuras del SD4** con notas de elaboración y nombres antiguos de módulos (las corriges tú en draw.io).

Lo que está coherente: tecnologías y versiones, regiones AWS, RTO/RPO, disponibilidad, etapas y meses, hitos H1–H12, volumetría del caso, comités de gobierno, innovaciones SD13↔SD7 y todas las citas al SD4 (sección 9).

### Estado por subdocumento

| SD | Riesgo de anulación | Motivo principal |
|---|---|---|
| SD1 | Bajo | Remite al Capítulo 12 (no entregado); nivel de IA «No aplica» |
| SD2 | Bajo | Sin hallazgos de coherencia relevantes |
| SD3 | Medio | Ya cita bien el SD4. Quedan en el T-12 R8-22, «Tabla T14.xx» y secciones antiguas de T-15 y T-18 |
| SD4 | Medio | Texto corregido. Quedan las notas y nombres antiguos dentro de las figuras |
| SD5 | Bajo | Detalles de forma (referencias incompletas, «No aplica») |
| SD6 | **Alto** | Contradice el SOC propio; sin figuras; títulos obligatorios cambiados; cobertura distinta |
| SD7 | **Alto** | T-15 se declara no recalculado; cita riesgos R8-xx y Anexos 8.C–8.E inexistentes; «T-15, Tabla 5.2» inexistente |
| SD8 | **Alto** | Campos «pendiente» en las fichas, notas de verificación, nombres de archivo, título del capítulo |
| SD9 | Medio | Ya cita bien el SD4. Quedan «Informe 2» en portada, pentest anual vs semestral y el criterio del H4 |
| SD13 | Medio-alto | Cita riesgos R8-xx y Anexo 8.F inexistentes; «Informe 2» en portada |

## 4. Hallazgos críticos (pueden anular el subdocumento)

### C1. 🟡 SD8: marcas de borrador y notas de verificación

Resuelto en `5d56ba2`/`fb3360f`: la declaración de IA del cuerpo ya no dice «en clases», «la revisión humana permanece pendiente» ni «podemos saltarnos algunas partes»; la herramienta figura como «Gentle-Shell y ChatGPT».

Sigue abierto:
- Anexo 8.A: «Plazo/hito: Pendiente de definición por responsable» y «Contingencia: Pendiente de definición por responsable» en las fichas (45 líneas en el fuente).
- Cuerpo p.5: «señala como pendientes de definición por responsable los plazos, las contingencias»; p.13: «estimaciones de planificación pendientes de validación por los responsables»; p.15: «quedan pendientes de evidencia y planificación actualizadas».
- Referencias: «[Fecha de emisión no verificada.]» tres veces; SD3, SD4 y SD13 citados como «s. f.» aunque tienen fecha (12-10-2026). El SD8 se cita a sí mismo.
- p.11: «Los análisis y anexos que conservan la codificación anterior R8 corresponden a una versión previa del registro» (nota de versión).
- p.9 «C.5 sólo compara hipótesis» y p.16 «E8-05», «E8-13», «E8-14»: no existen en el SD8 nuevo.
- Portada «VERSIÓN FINAL PARA ENTREGA»; pie «Media firma: representante» (el resto dice «Alex Aravena»).
- 8.3 no entrega responsable, plazo y disparador por respuesta (aclaraciones §11, 8.3).
- La tabla de IA dice «Ver declaración propia de ese anexo / del formulario» para los Anexos 8.A y 8.B y el T-16, pero ni los anexos ni el T-16 tienen declaración de IA, aunque su índice la anuncia.
- Dos tablas distintas numeradas «Tabla 8.4» (p.8 y p.12).
- p.7: «Para poder realizar un buen análisis de riegos, debemos de definir…» (errata y registro informal); p.8: la tabla reconoce «un solapamiento en 70 %» entre los niveles 4 y 5 de probabilidad.

**Corrección (SD8):** completar plazos y contingencias o quitar esos campos; poner fecha en las referencias; quitar la nota de versión, C.5 y E8-xx; agregar la declaración de IA de anexos y T-16; renumerar tablas; corregir la banda 5 a «q > 70 %».

### C2. 🟡 Citas a riesgos y anexos del SD8 con la codificación antigua

Resuelto: R8-05 → R-015 en SD3 (T-12), SD4 y SD7 (cuerpo, anexos y T-18).

Sigue abierto:
- **Riesgos R8-xx**: SD3 T-12 (R8-22), SD7 cuerpo p.56 (R8-02), T-14 p.93 (R8-27, R8-29), T-15 pp.44–48 (R8-12, R8-17, R8-18, R8-19), T-18 p.23 (R8-01), SD13 cuerpo, anexos y T-19 (R8-23 a R8-29). No hay equivalencia directa: el SD8 dice «No existe crosswalk verificable entre los códigos R8 […] y el registro vigente». Hay que elegir cada código a mano (por ejemplo, R8-02 «doble reserva o custodia» ↔ R-005 «conflictos y duplicados tras reconexión»).
- **Valoraciones distintas**: SD13 p.33 «R8-27 […] probabilidad 4 e impacto 5 (exposición 20, nivel crítico)» ↔ SD8 R-038 «P 3 (0,50); I 2 (0,40) […] 0,20; zona Alta».
- **Escala distinta**: SD13-Anexos p.10 atribuye al SD8 «la probabilidad 3 equivale a un 40 % y la 4 a un 60 %, y el impacto se mide como fracción del esfuerzo afectado». El SD8 usa bandas 31–50 % y 51–70 % y dice que las ponderaciones no son fracciones de esfuerzo (T-16 p.5).
- **Anexos inexistentes**: T-15 p.42 «SD8, Anexo 8.C, agrega una simulación de Monte Carlo» (el SD8 dice «No se presentan simulaciones»); T-15 p.38 «SD8, Anexo 8.D»; SD7 p.56 «conforme al Anexo 8.E»; SD13 p.24 «Anexo 8.F, oportunidad O8-01».
- **Reservas**: el SD8 fija 2.058,48 HH de contingencia y 1.600 HH de gestión, «no una asignación por mes, perfil o paquete»; el T-15 p.38 dice que las reservas del SD8 «deben conciliarse con la nueva línea base». El reflejo de las reservas en el cronograma (exigido en 8.3) no existe en ninguno de los dos.

**Corrección:** tabla de equivalencia R8-xx → R-0xx aprobada por quien lleva el SD8, aplicada en SD3, SD7 y SD13; reemplazar las remisiones a 8.C–8.F por fichas o secciones que existan.

### C3. ✅ SD4 revelaba el origen académico de las Bases

Resuelto en `3d5f1e9`. Se quitó «Las Bases Técnicas Transversales y del caso proceden de la Pontificia Universidad Católica de Valparaíso (PUCV)» del cuerpo, los anexos y el T-11. Las 78 citas «PUCV (2026a/b)» pasan a «Distribuidora Puelche S.A. (2026b/c)» y las listas de referencias quedan como en los demás subdocumentos, sin «Escuela de Informática».

### C4. 🟡 SD4: notas de elaboración dentro de las figuras

Abierto (son imágenes: las corriges tú en `04/figuras/fuentes/Arquitectura-logica-general-y-8-capas.drawio.xml`, recuadro de subtítulo de cada página):

| Figura | Página del PDF | Texto a quitar |
|---|---|---|
| 2 (capa 1, Presentación) | 14 | «Actores y canales del definitivo.» |
| 3 (capa 2, Borde) | 20 | «Vista funcional de los recorridos del general.» |
| 4 (capa 3, Puertas de servicio) | 22 | «Destinos reproducidos del XML definitivo. Los módulos son contexto.» |
| 6 (capa 4, Negocio) | 26 | «Los módulos mantienen sus nombres. Las relaciones externas conservan sus destinos.» |
| 7 (capa 5, Integración) | 29 | «Mecanismos y dependencias del definitivo.» y «Persistencia local y central: vista detallada en la página 6. Las relaciones de módulos con cada mecanismo se conservan. No se asignan nuevas garantías de entrega.» (si se deja la remisión, debe decir «Figura 10») |
| 10 (capa 6, Datos) | 39 | «Dominios lógicos y ubicación del definitivo.» |
| 12 (capa 8, Observabilidad) | 49 | «Se mantienen los tiempos de retención y el buffer indicados en el definitivo.» |

### C5. ⬜ SD7: el T-15 se declara a sí mismo sin recalcular

- T-15 p.6: «las fechas, reservas y probabilidades de la Tabla 7.8 corresponden exclusivamente a ese escenario histórico y no acreditan la ruta crítica ni la factibilidad».
- T-15 p.38: «Sus fechas, reservas, probabilidades y afirmaciones de nivelación no están reconciliadas con la línea base vigente de 217.543 HH […] Antes de usarlos para decidir se recalculará la red».
- T-15 p.43, título de la Tabla 7.8: «Escenario nominal histórico: entrega, reserva y probabilidad por hito; pendiente de recálculo».
- SD7 p.38: «La Tabla 5.2 del Formulario T-15 conserva sus antiguas reservas y probabilidades como referencia histórica»; p.40: «una hipótesis de hasta 40 desarrolladores simultáneos, todavía pendiente de asignación nominal».
- SD9 T-13 p.11 lo arrastra: «no se presume suficiencia del escenario histórico del T-15».
- T-14 p.24 dice que el T-15 «nombra la ruta crítica con su cálculo», pero el T-15 dice que ese cálculo no la acredita.

**Corrección (SD7):** recalcular red, holguras y reservas con las 217.543 HH, o quitar las frases de «histórico/pendiente» y presentar el cálculo como vigente. Luego quitar la frase del T-13.

### C6. 🟡 Referencias a tablas, secciones y anexos que no existen

Resuelto (todas las citas al SD4):

| Subdocumento | Antes | Ahora |
|---|---|---|
| SD3 (T-12) | Tablas 29–39 del SD4 y otras con numeración antigua; Figuras 24 y 25 | Tablas y figuras vigentes por tema (p. ej. 4.3.2.4 → Tabla 26, 4.2.6.11 → Tabla 21, 4.3.1.4 → Figuras 28 y 29) |
| SD3 (T-12) | Anexos del SD4: 4-O A.17, 4-R A.23, 4-T A.25, 4-P A.19, 4-W.8 A.34/A.35 | 4-O A.19, 4-R A.25, 4-T A.27, 4-P A.21 (A.20 en RNF-21.09), 4-W.8 A.38/A.39 |
| SD7 (T-18 p.5) | «Capítulo 4, Tabla 14» | Tabla 8 (Ventanas de despliegue) |
| SD9 (T-13, Anexos) | «SD4, Tabla 31» | Tabla 21 |
| SD9 (cuerpo, Anexos, T-13) | «SD4, Tabla 16» | sección 4.2.4.3 |
| SD9 (T-13 p.19) | «AL-DTE-01 a AL-SYNC-01» | «AL-DTE-01 a AL-ACT-01» |
| SD9 (T-13 p.14) | «SD5, Anexo 5-L» | Anexo 5-K |

Sigue abierto:

| Subdocumento | Cita | Realidad |
|---|---|---|
| SD3 (T-12) | «Tabla T14.42», «T14.45», «T14.46» (43 citas) | El T-14 numera sus tablas «Tabla 7.xx» |
| SD3 (T-12) | «T-15 5.7» (p.117), «T-18 2.7» y «2.6» (pp.91, 122) | Son 7.5.7, 7.2.7 y 7.2.6 |
| SD7 (cuerpo pp.38, 40, 44) y SD8 (p.15) | «T-15, Tabla 5.2» | La tabla de reservas es la 7.8 |
| SD7 / SD13 / SD8 | Anexos 8.C–8.F, C.5, E8-xx | Ver C1 y C2 |

### C7. ⬜ SD6 contradice el SOC propio

- SD6 p.5: «El servicio SOC 24x7 es condicional a su subcontratación; RT-11.17 presenta cumplimiento parcial porque la ubicación del SOC no está declarada».
- T-15 p.12: «El SOC es propio de LafroX y opera desde su Centro de Operaciones en Valparaíso (RT-11.17…)». T-12 p.195 lo da por «Cumple», en Valparaíso desde el mes 13. SD1 p.6 ubica el SOC en Valparaíso.

**Corrección (SD6, posterior):** decir que el SOC es de LafroX, opera desde Valparaíso desde el mes 13 y cumple RT-11.17.

### C8. ⬜ SD6 sin figuras ni análisis en el cuerpo

El cuerpo (10 pp.) no tiene ninguna figura ni tabla de análisis: solo la tabla de IA. Cada sección remite al T-9 o T-10. Aclaraciones §7.1 a) lo trata como indicio de capítulo generado por IA, y §3 pide que el subdocumento resuma y analice.

**Corrección (SD6):** al menos una figura propia en 6.1 (gobierno y cadencias) y otra en 6.2 (fases RUP / cadena DevSecOps), explicadas en el texto.

### C9. ⬜ Nombres de archivo fuera del patrón (Art. 40.4: archivo mal nominado = no presentado)

- SD8: `LafroX-Subdocumento-8-Anexos.pdf` (guion antes del número) y `Lafrox-Subdocumento-T-16.pdf` (el formulario se llama «Subdocumento»). El cuerpo no tiene PDF en la rama.
- SD7: prefijo `LafroX-` en vez de `LAFROX-`, y un duplicado `LafroX-Formulario-T-14-revisado.pdf`.
- Deben ser `LAFROX-Subdocumento8.pdf`, `LAFROX-Subdocumento8-Anexos.pdf`, `LAFROX-Formulario-T-16.pdf`, igual que SD1–SD6, SD9 y SD13.

## 5. Hallazgos altos

### A1. 🟡 Nombres M10 y M11 en el SD4
Resuelto en el texto (`3d5f1e9`): «M10 Analítica» y «M11 Canal moderno», incluido el título 4.1.4.7 y los Anexos 4-D, 4-E, 4-F y 4-N.
Abierto: las Figuras 1, 4, 6 y 7 (pp. 12, 22, 26 y 29) siguen diciendo «M10 · BI Gerencia» y «M11 · EDI Canal Moderno» dentro de la imagen.

### A2. ⬜ Cobertura de pruebas: global vs código modificado
SD1 p.11 «cobertura unitaria global de al menos 80 %»; SD4 p.118, SD9 y T-14 p.27, igual. SD6 p.6 «al menos 80 % de cobertura de líneas para el código modificado» y T-10 p.4 igual.
**Corrección (SD6 y T-10):** «cobertura unitaria global ≥80 %» y, aparte, «lógica de negocio ≥70 %».

### A3. ⬜ Pruebas de intrusión: semestrales vs anuales
T-12 p.105 y SD3-Anexos p.99: «LafroX ejecuta estas pruebas de forma semestral, por sobre el mínimo anual». SD9 p.30 programa «tres intrusiones» con separación de doce meses (meses 28, 40 y 52).
**Corrección (SD9):** seis campañas semestrales en Operación.

### A4. ⬜ SD6 Anexo 6.B: obra civil en otros meses y a otro cargo
SD6-Anexos p.6: «Obra civil, piso técnico e instalación de energía, climatización e incendio — Habilitación del recinto LafroX […] Meses 5 y 6». SD6 cuerpo p.5 y T-14: orden de compra mes 2, instalación mes 3, recepción mes 4. T-12 p.161 y T-14: la obra civil de separación es de cargo del CLIENTE (RT-06.06).
**Corrección (SD6 anexo):** meses 2/3/4 y obra civil a cargo del CLIENTE con coordinación de LafroX.

### A5. ⬜ Sincronización del CD: 10 minutos vs 2 horas
SD3 p.18: dispositivo ≤10 min; centro ≤2 h tras 24 h de corte. T-18 p.9 y T-14 p.55: «14 horas sin señal en terreno y 24 horas sin enlace en el CD, […] con sincronización en 10 minutos o menos».
**Corrección (SD7):** separar «terreno ≤10 min» y «CD ≤2 h».

### A6. ⬜ Mesa de servicio cubierta con personal del NOC
SD1 p.7: los agentes de mesa se cuentan aparte de los 124 especialistas. T-15 p.46: «NOC y mesa se cubren con personal del NOC con turnos asignados».
**Corrección (T-15):** mesa con sus agentes propios (SD4 Anexo 4-W.7), separada del NOC.

### A7. ⬜ Preparadores: 120 vs 180
SD3-Anexos p.154: «120 personas Talca; 60 personas Concepción, según S-39»; T-18 p.15 incluye Concepción. SD7 p.50: «son 120 preparadores».
**Corrección (SD7):** «120 en Talca y hasta 60 en Concepción (supuesto S-39)».

### A8. ⬜ Títulos obligatorios cambiados (aclaraciones §2 y §10)
- SD6: «Introducción a las metodologías del proyecto y software» (debe ser «Introducción a las Metodologías»), «6.1 Metodología de gestión de proyecto» («…de Gestión de Proyectos»), «6.2 Metodología de desarrollo de software» («…de Desarrollo Software»). La portada corta el título: «…y desarrollo de softwa».
- SD8: «Introducción a la gestión de riesgos» (debe ser «Introducción a los Riesgos»).

### A9. ⬜ Portadas distintas entre subdocumentos
- «VERSIÓN FINAL PARA ENTREGA» en SD5, SD6, SD7, SD8, SD9 y SD13, pero no en SD1–SD4.
- «Informe 2 · Cuerpo del subdocumento / Anexos / Formulario…» en todas las portadas de SD9 y SD13.
**Corrección:** dejar las portadas como SD1–SD4.

### A10. ⬜ H4 (mes 10) exige integraciones de la Etapa 2
SD9 T-17 p.9, criterio del H4: «15 de 15 flujos de integración sin error». INT-08 (intercambio con las cadenas) se construye en los meses 13 a 18 (T-14, paquetes 3.6.5 y 3.6.6).
**Corrección (SD9):** en H4, solo las integraciones de la Etapa 1; las 15 en el H10.

## 6. Hallazgos medios

| # | Estado | Dónde | Problema | Corrección |
|---|---|---|---|---|
| M1 | ✅ | SD4 pp.53, 59 y Anexo 4-W | El 41 % sin lote se generalizaba a todas las recepciones | Corregido: «del producto retirado» |
| M2 | ⬜ | SD7 p.33 | «cerca de 200 conductores»; SD2/SD3: 84 propios + ≈160 externos (244) | Usar las cifras de SD2 |
| M3 | ⬜ | T-14 pp.40–41 y 50–51 | «Hasta el mes 5 (H3)» e «integración mes 16 (H9)», pero H3 = mes 6 y H9 = mes 17 | «antes del H3 (mes 6)», «antes del H9 (mes 17)» |
| M4 | ⬜ | T-14 p.88 ↔ T-15 p.28 | Operación 128.373,67 HH vs 128.853,67 HH | Unificar el total |
| M5 | ⬜ | T-15 p.8 ↔ T-14 p.84 | Frente F7 «meses 9 a 21», pero su paquete 7.2.3 es de los meses 2 a 6 | Ampliar la ventana de F7 |
| M6 | ⬜ | T-15 p.59 ↔ T-14 p.65 | Ensayo de reversión 4.1.2 «antes de cada corte», programado una sola vez (80 HH) | Una ocurrencia por corte |
| M7 | ⬜ | T-15 p.11 ↔ p.31 | 102,67 HH de cierre en el mes 22, pero la curva muestra 0 | Corregir la curva |
| M8 | ⬜ | SD1 pp.5 y 17 | Remite al «Capítulo 12» y a «12.3» (SD12 no entregado) | Dejar SD1 autosuficiente |
| M9 | ⬜ | Declaraciones de IA | Filas agrupadas («Anexos 7.A a 7.F», «Anexos 9.A a 9.D», «Subdocumento 6 Anexos»); «No aplica» como nivel en SD1, SD3 y SD5 | Una fila por anexo; «Ninguno» |
| M10 | ⬜ | SD6 tabla de IA | «adaptación a Markdown» como finalidad | Redactar sin el formato de origen |
| M11 | 🟡 | Citas a las Bases | SD4 ya usa «Distribuidora Puelche S.A. (2026b/c)» como el resto. Queda SD9 (y parte de SD7) con «(BA, p. 13; BTT, p. 26)», y SD1/SD8 con RT sin página | Un solo estilo con página |

## 7. Hallazgos bajos

- ⬜ Nombres sin tilde: «Bastian Trejo» (SD5), «Tomas Perez» (SD6), «Patricio Henriquez» (SD13).
- ⬜ SD8: fecha «12 de Octubre de 2026» con mayúscula.
- ⬜ SD1: pentest corporativo «semestral» y para Puelche «al menos anual»; coherente, pero conviene alinear la frase con T-12 (semestral).
- ⬜ SD9 p.21: «Datos históricos del CLIENTE 32,11 GB»; SD5 p.35 aclara que 32,11 GB es almacenamiento estimado de destino y 16,05 GB el volumen de origen.
- ⬜ SD5: algunas referencias sin autor o año (cuerpo p.42; Anexos p.215).
- ⬜ T-11 (SD4): cita las Bases por título («Bases Técnicas Transversales, cap. X, p. Y») y su lista trae las entradas por autor; es el estilo previo del SD4 y no se tocó.

## 8. Orden sugerido para lo que queda

1. SD8: limpiar los marcadores de C1 y definir la equivalencia R8-xx → R-0xx (C2).
2. Aplicar esa equivalencia en SD3, SD7 y SD13, y reemplazar las remisiones a 8.C–8.F.
3. SD4: figuras en draw.io (C4 y A1).
4. SD7: T-15 (C5), «Tabla 5.2», A5, A6, A7 y medios M2–M7.
5. SD6: SOC (C7), figuras (C8), títulos (A8), cobertura (A2) y Anexo 6.B (A4).
6. SD3 (T-12): citas «T14.xx», «T-15 5.7», «T-18 2.x».
7. SD9 y SD13: pentest (A3), portadas (A9) y H4 (A10).
8. Nombres de archivo (C9) y bajos.

## 9. Verificado coherente

- **Empresa y portada**: LafroX SpA, RUT 77.418.902-K, Alex Aravena, 12-10-2026 en los 10.
- **Plazos**: 56 meses; Etapa 1 desarrollo 1–12, marcha blanca 13–15, producción mes 16; Etapa 2 desarrollo 13–18, marcha blanca 19–20, producción mes 21; Operación 21–56.
- **Hitos**: H1 m2, H2 m4, H3 m6, H4 m10, H5 m12, H6 m13, H7 m16, H8 m14, H9 m17, H10 m18, H11 m19, H12 m21 (salvo M3).
- **Tecnología**: Laravel 13 / PHP 8.5, Angular 22, PostgreSQL 16, Aurora PostgreSQL, RabbitMQ local + SQS/SNS (sin EventBridge ni Kafka), Keycloak 26, Kotlin/Android, GitLab CI + CodeBuild, Terraform + Ansible, OpenTelemetry + CloudWatch, DynamoDB para telemetría, S3/Glue/Redshift para analítica.
- **Regiones**: sa-east-1 primaria y us-east-1 DR.
- **Continuidad**: RTO ≤4 h y RPO ≤15 min en servicios críticos; RPO ≤24 h en dominios no críticos; autonomía 24 h en CD y 14 h en terreno; reversión técnica ≤10 min distinta del objetivo operacional de 40 min (decisión 04:45, término 05:25).
- **Disponibilidad**: infraestructura 99,95 %, crítico 99,9 %, alto 99,5 %, medio 99,0 %.
- **Ambientes**: DEV, QA, PREPROD, PROD y DR.
- **Volumetría**: 96 camiones (42 propios, 54 externos), 28 con frío (18 + 10), 62 preventistas, 14.200 clientes (11.600 + 2.100 + 500), 8.400 SKU (→ ≈9.500), 31.000 pedidos/mes, ≈1.400 entregas/día y 2.600 en peak, 19 actores/grupos de interés y 15 actores con acceso.
- **Requerimientos**: 262 (176 RF + 86 RNF) y 271 filas en T-12. Todos los RF/RNF, S-, RNG-, V-, INT-, ADR- y N- citados fuera de su dueño existen en él.
- **Citas al SD4**: todas las secciones, tablas, figuras, anexos y tablas de anexo del SD4 citadas por los otros nueve subdocumentos existen y tratan el tema citado (verificado el 23-10 noche).
- **Nombres de módulos**: «M10 Analítica» y «M11 Canal moderno» en el texto de SD3, SD4, SD7, SD13 y T-12 (las figuras del SD4 quedan pendientes).
- **Gobierno**: reunión semanal, Comité de Proyecto quincenal, Ejecutivo y Arquitectura mensuales, Operación mensual desde el mes 13.
- **Equipo**: los 8 nombres y roles de SD1 Tabla 1.6 se repiten en SD7, SD8, SD9 y SD13.
- **Innovaciones**: paquetes y meses de INN-01, -02, -03 y -05 idénticos en SD13 y SD7; INN-04 en 5.4.3; revisión de INN-03 en meses 26, 32, 38, 44, 50 y 56.
- **Despliegue**: azul-verde con canario en SD3, SD4, SD7 y SD9.
- **Calidad**: lógica de negocio ≥70 % en todos; global ≥80 % en todos salvo SD6 (A2).
- **Migración**: 32,11 GB (30,73–33,49) en SD3, SD4, SD5 y SD9.
