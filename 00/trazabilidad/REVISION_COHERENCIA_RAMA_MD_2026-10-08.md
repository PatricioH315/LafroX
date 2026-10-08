# Revisión de coherencia entre subdocumentos — rama `rama-md` — 2026-10-08

Registro interno (no se entrega). **Sin cambios** en `rama-md` (worktree `../LafroX-rama-md`, commit `2648853`).

## Alcance y método

- Lectura completa: SD1 y T-6; SD2 y anexos; SD3 cuerpo y Anexos 3.C–3.K; SD6, T-9 y T-10; SD7, Anexos 7.A–7.F y T-18; SD8, Anexos 8.B–8.F (8.A por muestreo) y T-16.
- SD4 (cuerpo, anexos, T-11), T-12, T-14 y T-15: lectura por secciones y cruce automático (scripts en Python): nombres de módulos, INT, paquetes EDT citados, conteos de la EDT, catálogo RF/RNF, comités, cifras del caso, referencias, declaraciones de IA.
- Criterio: aclaraciones §7.1 c) — un texto que contradice a otro subdocumento en una decisión de diseño (tecnología, etapa, umbral, proveedor, región) anula el subdocumento completo desde el Informe 2; §7.1 d) — notas, «pendiente», referencias inexistentes, revisión «no realizada», etc., también.
- Los 7 frentes de ChatGPT (gpt-6-sol, alto) fallaron: límite de uso de la cuenta Codex. Todo lo que sigue es lectura propia, verificado con cita y línea.
- **Límite:** la rama no contiene SD5, SD9 ni SD13. El Formulario T-22 exige para el Informe 2 los subdocumentos 1–9 y 13; las innovaciones INN-01…05 que usan SD7/SD8 no tienen fuente en la rama.

## Críticos

| # | Hecho en conflicto | Lado A | Lado B | Corrección sugerida |
|---|---|---|---|---|
| C1 | **Quién provee la infraestructura on-premise** (sala, UPS, generador, servidores, firewalls, mini-PC) | SD4:1123 «La infraestructura on-premise la provee el adjudicatario dentro del contrato (Bases Administrativas, art. 14.2, p. 10)» | SD6:94 y Tabla 6.3 (101–102) «CLIENTE, según la especificación 5.1.2»; SD7:153 «el CLIENTE compra el hardware de terreno y de la sala»; T-14 5.1.2 «Especificación de compra de la sala técnica, los racks y los gabinetes de borde para el CLIENTE»; 7.B D-10; T-15 §5.2; T-16 R8-19; SD8 C.4 «el H3, de la compra del CLIENTE» | Mantener SD4 (BA 14.2). El CLIENTE compra solo el hardware de terreno (caso cap. 11, E-09). Reescribir SD6 6.1.3, SD7 7.1, T-14 5.1.2/5.1.3, D-10, T-15 §5.2, R8-19 y C.4. Revisar además RT-06.06 (obra civil de separación = cargo del CLIENTE) frente a SD6:103 «LafroX, con instaladores». |
| C2 | **RPO ante pérdida del sitio** | SD4 4.3.2.4 (2706–2725): RPO ≤ 15 min sustentado en tres caminos; el caso extremo «Queda como riesgo residual» con mitigaciones | SD8:7 «brecha residual de RPO»; SD8:154 «El límite residual RPO requiere resolución, no aceptación como sustituto de cumplimiento»; 8.E E8-05 «SD4 describe RPO remoto >15 min … aceptar el riesgo no satisface Bases»; T-16 R8-05 «resolver brecha … plazo: Resolver diseño»; T-18:359 «El límite residual de RPO continúa abierto» | El plan de riesgos declara que la arquitectura no cumple. Alinear SD8, T-16 y T-18 con SD4: riesgo residual declarado (RT-02.11), mitigaciones y verificación AL-DR-01; quitar «brecha», «resolver diseño», «continúa abierto». |
| C3 | **«CD-05» y «A31/A32»** | SD4 no contiene «CD-05» ni «4L»/«2N + 2L». El mecanismo es «Reserva comercial y retención física por sitio» (4.1.4.4) e «INT-03/04 Coordinación de reserva» (Tabla A.32). Tabla A.31 = «Perfil horario por lugar de proceso» | 18 apariciones fuera de SD4: SD7:687 «CD-05 está dimensionado en SD4 A31/A32; falta verificar»; 7.F P7-09/P7-10; T-14:1970; T-18:359; SD8 R8-02, R8-06, C-08, E8-06; T-16 R8-02/R8-06 | Identificador inexistente (§7.1 d) y duda sobre el dimensionamiento de SD4 (§7.1 c). Usar el nombre de SD4, citar Tabla A.32 (fila «Coordinación de reserva») y Tabla A.33 (enlaces). Eliminar la duda «4L vs 2N + 2L» o resolverla en SD4. |
| C4 | **Tecnología del backend** | SD1:101 «La línea trabaja habitualmente con monolitos modulares en Python y Django»; SD1:150 «Desarrollo Software (Python, Django, Móvil) — 48» | SD4: Laravel/PHP, con rastro de una versión Django: 805 «mantener su runtime junto al nuevo»; 817 «Sustituye el runtime por Laravel/PHP»; 943 «pruebas de paridad»; 4.2.4.1.3 «Transición al backend Laravel», «framework de origen». T-15:486 «La división declara Python, Django y móvil; la oferta usa Laravel/PHP» | Declarar en SD1 la competencia PHP/Laravel de la división (o mixta), y quitar de SD4 el relato de «transición» desde un backend previo. Quitar la frase de T-15 o convertirla en plan de asignación sin exponer la contradicción. |
| C5 | **Innovaciones** | SD3 y SD4: cero menciones a INN o innovación. T-12 RT-26.01 (Obligatorio: ubicar cada innovación en la arquitectura) «Sí (E1 y E2) … 3.2.1»; RT-26.08 (validar una en marcha blanca E1) «No ofertado» | SD7/7.D/T-14 3.10 definen INN-01…05 con componentes nuevos (estimador de saldo, lista sin conexión, captura de evidencia, asociación lote–sensor, vista en M9, hoja impresa en cabina). SD7:674 «Tres innovaciones se validan en la marcha blanca de la Etapa 1» | Ubicar cada innovación en SD4 (capa, componente, interfaz). Cambiar RT-26.08 a «Sí (E1)». Corregir la columna Sección de RT-26.xx (SD3 3.2.1 no habla de innovaciones). Traer SD13 a la rama para verificar. |
| C6 | **Declaraciones de IA y notas internas** (incoherentes entre subdocumentos y con indicios §7.1 d) | SD1 y SD2: «Claude / Gemini», nivel Bajo, revisores con nombre | SD3, SD6, SD7, SD8, T-9, T-10, T-12, T-14, T-15, T-16: «Codex; Claude Code», Alto, «No documentada». SD4:2816–2855: «Revisión final no realizada», «láminas de Tomás», «conversión entre Markdown y LaTeX», filas 4.2/4.3/4-W/T-11 vacías. SD4-Anexos:1643 «La revisión humana final se realizará sobre el consolidado». T-11 sin declaración. SD2-Anexos:489 contradice la tabla de SD2:705–708 (Codex Alto vs Claude/Gemini Bajo). T-18:375 «consolidar … en A-6 antes de entrega» | Una sola convención para todas las declaraciones (herramienta, nivel de la escala, revisor con nombre y qué verificó). Quitar fechas, «Actualización del …», «No consta revisión humana». |
| C7 | **Autoría de las Bases en las referencias** | SD4:2798–2802, SD4-Anexos:1625–1629, T-11:122–126: «Pontificia Universidad Católica de Valparaíso. (2026a) Bases técnicas del caso … (2026c) Bases administrativas» | SD1, SD2, SD3, SD6, SD7, SD8: «Distribuidora Puelche S.A. (2026a) Bases Administrativas … (2026c) Caso 02» | Rompe la ficción (§7.1 d) y la misma clave «2026a» designa documentos distintos según el subdocumento. Usar en todos «Distribuidora Puelche S.A.» con las mismas letras. |

### Notas internas visibles (parte de C6)

- SD7:676 «## Base vigente de planificación»: título de nivel 2 no permitido (aclaraciones §2) y texto de notas: «no acredita productividad ni contratación», «falta verificar su multiplicidad y carga», «INN-03.P5 queda en revisiones semestrales …, no en una supuesta actividad continua nueva».
- Anexo 7.F completo: «validación pendiente», «no acreditados», «no ejecutado», «No se acredita aprobación humana ni formal», «Para entregar una oferta cerrada se requieren…». 7.F declaración: «Se conserva la declaración histórica».
- T-14:1966 «## Criterios vigentes de programación y recursos»: «La estimación es provisional», «sin renumerar T-12 ni inventar nuevos requerimientos».
- T-15:79 «Modelo cuantitativo provisional»; T-15:336 «La versión anterior publicaba 147.328 HH»; T-15:35 «La figura conserva la lectura histórica».
- T-18:65 «La figura conserva la representación histórica»; T-18:349 «Son objetivos de diseño, no tiempos medidos»; T-18:359 «son pruebas planificadas, no ejecutadas».
- SD3:274 «definición coordinada con el redactor del Subdocumento 3»; SD3-Anexos:634 «catálogo coordinado con el redactor del Subdocumento 3 comunicado por el equipo»; SD3:316 «son objetivos no medidos».
- SD4:1047 «El registro de supuestos del capítulo 3 debe conservar…».
- SD8 8.E E8-10 «No usar las declaraciones como disponibilidad demostrada»; SD8:130 «son referencias supuestas, no ensayos ejecutados»; T-16:3 «ningún riesgo tiene cierre acreditado … nominarlos no acredita dotación».

## Altos

| # | Hecho en conflicto | Lado A | Lado B | Corrección sugerida |
|---|---|---|---|---|
| A1 | **Ruta crítica** | SD7:396 «La cadena crítica nace en las interfaces sin documentación … (1.2.3), (3.3.2), (3.4) … (H7, mes 16)»; 7.B:78 | T-15:26 «El camino más crítico llega al H9: la construcción de los módulos de la Etapa 2 (3.5) y su prueba de integración (3.9.1)»; SD8:118 y C.4 (H9 el más expuesto) | Una sola ruta crítica en SD7, 7.B, T-15 y SD8. |
| A2 | **Reserva por hito** | SD7:409 «de 6 a 35 días hábiles»; T-15 Tabla 5.2 (6, 35, 19, 19, 35, 13, 21, 28); SD8 C-03 (19, 35, 21, 28) | 7.F P7-02 «reservas de 3 a 35 días hábiles»; 7.F:213 «T-15 §5 deja reserva de calendario cero antes de H4/H5/H9/H10»; T-15:470 «sin esperar consumo de una holgura inexistente» | Dejar solo la Tabla 5.2. Corregir 7.F y T-15 §5.4. |
| A3 | **Duración de la iteración** | SD6:189 «iteraciones de Construcción de dos semanas» | SD7:681 «El SD6 no fija una duración única de iteración … sin … atribuir a SD6 un sprint obligatorio» | Borrar la frase de SD7 (y la sección completa, ver C6). |
| A4 | **Tiempo de reversión técnica** | SD4:1803 «tiene como objetivo 4 horas» | T-18:349 «nivel técnico ≤10 minutos … total 40 minutos»; SD8 C-06; SD3:316 | Mismo umbral en SD4 y T-18 (distinguir reversión técnica de restauración de incidente del Art. 78.3). |
| A5 | **Starlink en los CD** | SD4 (4.2.5.1, 4.3.2.4) y T-11 D-06: «Talca 1, Concepción 1 y cross-docking 3 — 5» | SD6 Tabla 6.3:109 «Starlink de las tres plataformas»; T-14 5.3.3 «Starlink para las tres plataformas de cross-docking»; T-14 5.3 «un enlace principal y uno de respaldo» | Contratar los 5 Starlink en 5.3.3 y en SD6. |
| A6 | **Fechas de la sala técnica** | T-14 6.1.1–6.1.4 «Mes 3»; T-15:417 «instalación desde el mes 3»; T-14 5.1.2 «Mes 2» | SD6:101 «Mes 5», SD6:103 «Meses 5 y 6»; T-15:89 «la especificación 5.1.2 en el mes 3 y la sala desde el mes 4»; 7.B D-09 «especificación en los meses 2 y 3» | Una sola secuencia (planos, especificación, compra, instalación) en SD6, T-14, T-15 y 7.B. |
| A7 | **Nombres de módulos distintos de SD3** (aclaraciones 3.4: «los componentes tienen el mismo nombre en ambos capítulos») | SD3:25 «M4 Rutas … M7 Cobranza y rendición, M8 Devoluciones y envases, M9 Calidad y trazabilidad, M10 Analítica» | SD4:633 «Módulo de planificación de rutas (M4)»; 647 «rendición y cobro (M7)»; 659 «analítica y costo de servir (M10)»; 681 «M6 Reparto y entrega»; 1274–1276 «M7 Rendición», «M8 Devoluciones», «M9 Calidad»; SD4-Anexos 171–173, 198–200, 225–227 | Usar literalmente los doce nombres de SD3 en todo SD4. |
| A8 | **Reposición (RF-10) y su actor** | SD3:11 y Tabla 3.4 (reposición en M2, E1); T-12 RF-10.01–03 «Sí (E1) M2 Inventario 3.4.2»; D-05 «El Jefe de Abastecimiento la revisa» | SD4: sin reposición de compras ni RF-10. «Jefe de abastecimiento» (actor de RF-10.01–03, S-25, V-09) no está en los 19 actores de SD2 ni en los 15 de SD3/SD4 (SD3:278 «sin crear un decimosexto actor») | Agregar la capacidad a M2 e INT-06 (compras del ERP) en SD4; asignar RF-10 a un actor del catálogo (o declarar la función dentro de un perfil, como SD3-Anexos:636 hace con «catálogo» y «Tesorería»). |
| A9 | **Cinco o seis instalaciones** | SD4:1057 «La lógica adopta seis instalaciones en total, de las cuales cinco son sitios logísticos … y la sexta es la casa matriz de Talca … sin cómputo propio» (decidido) | SD3 S-22, V-01 y SD3:131 (consulta abierta, se confirma en el mes 1); SD2 E-06; SD1 Tabla 1.2 «5 o 6» | Llevar la conclusión de SD4 a SD3 (cerrar V-01 o reformularla) y a SD1. |
| A10 | **Equipo frente a actividades** (lo evalúa el Informe 2, T-22) | SD1:131 «124 especialistas»; Tabla 1.1 (48 desarrollo Python/Django; sin división de implantación) | T-15 §5.7: usa las 48 personas de desarrollo a la vez, SEG e IMP requieren contratación; SD8:120 «la dotación declarada en el SD1 no cubre SEG ni IMP sin contratación»; E8-10 | Declarar en SD1 cómo se cubren SEG (SOC) e implantación, y que la dotación asignada no compromete otros contratos. |
| A11 | **Traslado del servidor del ERP sin paquete EDT** | SD4:2532 y T-11:25 «Traslado del servidor del ERP … desde la sala actual de 25 m² … al rack R01» | T-14: ningún paquete; 6.3.1 «clúster de tres nodos, respaldo local y consola KVM» | Agregar el paquete (regla del 100 %). |
| A12 | **Interfaces en el Anexo 7.E** | SD4-Anexos:249 «INT-04 Detalle de cross-docking a la nube»; anexos «4-G» y «4-H»; INT-12 = réplica DMS del WMS nuevo de Talca | SD7-Anexos:177 «INT-04 Detalle de cross-docking a Talca» (diseño eliminado); 7.E:168 «Anexos 4.1-G y 4.1-H»; INT-12 asignada a 3.3.3 «Convivencia con el WMS de 2013» | Copiar nombres e identificadores de SD4; asignar INT-12 al paquete de replicación (3.2.2/3.2.4). |
| A13 | **Referencias a secciones y tablas de SD4 que no existen** | SD4: azul-verde y *feature flags* en 4.2.4.1.2; tablas con numeración continua (no hay «Tabla 4.1») | SD7:474 y T-18:5, T-18:20 «Capítulo 4, sección 4.1.8 y Tabla 4.1» para azul-verde e «interruptores de funcionalidad» | Citar 4.2.4.1.2 (despliegue) y 4.1.8 (único escritor) con la tabla real; usar el término de SD4. |

## Medios

| # | Hecho en conflicto | Lado A | Lado B |
|---|---|---|---|
| M1 | Alcance E1 descrito distinto | SD3: acuse del receptor vía ERP; retiro sanitario; reposición | SD6:36 «con el acuse de recibo de los conductores; y el manejo de efectivo y los retiros de los pedidos»; SD6:163 «confirmación de recepción por los conductores» |
| M2 | Umbral de cobertura | SD1:169, SD3 D-12, SD4:1751: 80 % de cobertura unitaria (global); SD1 exige SonarQube | SD6:180 «cobertura de líneas … del código modificado inferior al 80 %»; el pipeline de SD4/SD6 no tiene SonarQube |
| M3 | Resultados verificados en la marcha blanca E1 | SD7:658 «Doce de los dieciséis»; T-18:132 lista 12 | 7.C:107 «(14 resultados)»; T-18:30 «catorce de los dieciséis» |
| M4 | Servidores de Concepción | T-11 y SD4: dos DL20 (activo y en espera); dos mini-PC por cross-docking | T-14 6.3.3 «Gabinete de borde de Concepción montado: servidor, …»; 6.3.4 no menciona los mini-PC |
| M5 | Reversión en T-14 | SD3:314 y T-18 §2.5: el papel no sustituye el despacho | T-14 4.1.2 «Procedimiento de reversión … con hoja de picking y guía en papel»; 4.1.3 (E2) copia «96 despachos … final antes de 05:30», mientras SD7/T-18 dicen que la reversión E2 desactiva la capacidad sin tocar E1 |
| M6 | Despliegues en septiembre | SD4 Tabla 14 (1835) y SD6:185: ningún despliegue en todo septiembre | T-18:14 prohíbe solo despliegues «con impacto en la facturación o en el inventario» y congela «1 al 25 de septiembre» |
| M7 | Subsanación de observaciones | T-15 §5.5 «la subsanación de diez días hábiles usa la reserva del hito» | SD8 E8-11 «no tiene holgura: una observación atrasa el hito» |
| M8 | Interesados | SD2 Anexo 2.3 y SD3:370 «mantiene los 19 actores … con sus nombres» | SD6 Tabla 6.1: 17 grupos con otros nombres; omite Food Service y Empresas transportistas |
| M9 | Número de portales | SD3 3.I, SD4 N-01–N-03, T-11 «1 aplicación para 3 portales», T-14 3.5.1 incluye proveedores | SD7:169 «M1 a M12 y dos portales»; T-18 §3.1 omite el portal de proveedores |
| M10 | Trazas del T-12 hacia la evidencia | Lo físico está en SD4 4.3.1.4 | T-12 RT-06.01–06.32 → «3.1.1; 3.3.3» de SD3 (no tratan la sala); RT-06.02 blindaje «Sí» sin material ni resistencia en SD4/T-11 |
| M11 | Capítulo de la arquitectura | Arquitectura = SD4 | SD2:260 «La arquitectura que lo cumple se desarrolla en el Subdocumento 3» |
| M12 | Personas del SOC | SD4-Anexos 4-W.7: una posición = 4 personas (5 desde 26-04-2028) | T-15 §5.7 «El puesto SOC 24×7 exige 6 personas equivalentes» |
| M13 | Cadencia del Comité de Proyecto | SD6 y T-14: quincenal | SD8 C.3:672 «seguimiento semanal en el Comité de Proyecto»; E8-12 «en cada Comité de Proyecto | trimestral» |
| M14 | Probabilidad del H9 | SD8 y T-15: 89,9 % | SD7:409 «en al menos el 90 % de los escenarios» |

## Bajos

- Referencias a subdocumentos posteriores (regla que fijaste para SD4): SD1 → SD3 3.4.5, SD4, T-15; SD2 → SD3; SD2-Anexos:485 → «SD3 y SD7»; SD3 → SD4 4.1.3.1/4-N y T-18 §6.4.
- SD7:255 «los ocho roles» frente a los diez roles mínimos de SD1 Tabla 1.3.
- SD3 3.4.3: tres frentes de construcción E1 por dominio; SD7/T-15: un frente F3.
- Estilo de cita distinto: SD4 «Bases Técnicas del caso, cap. X, p. Y» (aclaraciones §6); SD1/SD2 «(2026c, tabla 7.1)»; SD3 «Caso, cap.»; SD7 «Caso 02, sección». Solo SD4 indica página.
- Ley 21.719: SD2 «Ministerio del Interior y Seguridad Pública. (2024)»; SD4 «Ley N.° 21.719. (2024)».
- SD6:8 fecha de emisión «7 de octubre de 2026»; portadas de SD1, SD2 y T-6 «05 de octubre de 2026».
- SD6 Tabla 6.3 y T-14 5.4.2: acta con el sindicato sobre «terminales, GPS y cámaras», cuando SD2/SD3 excluyen las cámaras.
- SD3:113 «El paquete de trabajo de cada uno se asigna en el plan de trabajo», pero T-12 ya trae la columna EDT.
- Residuos de conversión en el Markdown: SD4:1066–1072 («fisica.chapter», «[block] 25pt28ptlafroxFuerte»), SD3-Anexos:433 «-22 ^°C», SD7 «$→$», «[-1pt]».

## Verificado coherente (no repetir)

- Cifras del caso: 96 camiones (42 + 54), 28 con frío (18 + 10), 62 preventistas, 84 tripulantes propios, ≈ 160 externos (≈ 200 conductores en caso 14.1), 120 preparadores, 14.200 puntos (11.600 + 2.100 + 500), 180 proveedores, 1.400/2.600 entregas, 31.000 pedidos, 260.000 líneas, 1.150 recepciones, 34.000 DTE, 11.800 cobros, 900 devoluciones, 8.400 SKU / 1.100 de frío, 68.000 canastillos y 9.400 pallets, 21 puntos de cámara y 3 gateways IoT.
- Calendario: E1 1–12 / 13–15 / 16; E2 13–18 / 19–20 / 21; operación 21–56 (SD3, SD4, SD6, SD7, T-14, T-18). Aritmética del Anexo 7.A. Fechas límite de hitos SD8 = T-15.
- RTO ≤ 4 h, RPO ≤ 15 min, 99,95 % / 99,9 %, mesa 04:00–22:00 L–S y 24×7 en septiembre y diciembre, incidentes 15 min/4 h y 1 h/8 h, 14 h sin señal y 24 h sin enlace, sincronización 10 min / 2 h.
- Regla de precio (S-09, RNG-08, RF-03.11/12, SD4 M3, 8.E). OTIF 90/93/95 % en los meses 15/19/32. Regla térmica graduada con decisión de Calidad. ERP único emisor. WMS 2013 en solo lectura hasta el cierre de la marcha blanca.
- Equipo nominado: mismos ocho nombres y siglas en SD1 y SD8.
- EDT: 49 cuentas, 222 paquetes, por fase y por responsable (58/34/33/24/19/18/18/18) — contado sobre el diccionario de T-14. Paquetes citados en SD3/SD6/SD7/SD8/T-12 existen.
- HH: 202.774 = 190.366 + 9.336 + 3.072; contingencia 15.076 (suma de la Tabla B.2), 1.853 y 13.223; 32 riesgos, 22 críticos, RBS 13/10/9.
- Catálogo SD3 = T-12: 134 + 34 + 7 = 175 RF; 24 + 58 + 4 = 86 RNF; 181 y 90 filas; 54/157/39 = 250.
- Comités y cadencias SD6 = T-14 = T-15 = SD7. Cinco ambientes y herramientas del pipeline SD6 = SD4. Erlang de la mesa (2.200 / 2.283 / 2.391) SD8 C-05 = SD4 4-W.7. Quince actores de sistema SD3 = SD4. Alianzas de SD1 (Zebra, Fortinet, Starlink, AWS) = productos de T-11.
