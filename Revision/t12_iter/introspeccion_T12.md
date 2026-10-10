# Introspección del Formulario T-12 a lo largo de los subdocumentos — 9 de octubre de 2026

Revisión de solo lectura hecha por nueve agentes: ocho tramos del T-12 (A1–A3 y B1–B5) y un cruce inverso con los documentos que la matriz casi no cita (SD2, SD6-Anexos, T-9, T-10, SD7, SD8, T-16, SD9, T-13 y T-17). Ningún entregable se modificó. Se verificaron directamente dos puntos: SD9-Anexos tiene 172 menciones de «Cumple parcialmente», y SD4:1385 dice «no emite firma avanzada».

**Profundidad de la revisión:** todas las filas Parcial y No cumple se leyeron en su tramo. De las filas Cumple se verificó que exista cada sección citada y se leyó a fondo una muestra amplia (≈40 por tramo en B3, las de mayor riesgo en el resto). «Cumple confirmada» significa «sin hallazgo», no «leída línea por línea».

## 1. Estado actual (645 filas)

| Parte | Cumple | Parcial | No cumple |
| --- | --- | --- | --- |
| A — RF/RNF (271) | 237 | 31 | 3 |
| B — RT (374) | 304 | 42 | 28 |
| **Total** | **541** | **73** | **31** |

Documentos que respaldan las filas Cumple: SD4 (416) y SD4-Anexos (245); SD3-Anexos (220); SD5 (174) y SD5-Anexos (164); T-11 (130); T-14 (64); T-18 (21); SD13 (18); SD6 (15). **Nunca se citan:** SD2, SD9, SD9-Anexos, T-9, T-10, T-13 y T-17.

## 2. Hallazgo transversal principal: el SD9 contradice al T-12

La columna «Estado T-12» de la matriz 9.C de `09_plan_calidad/LAFROX-Subdocumento9-Anexos.md` (líneas 138-776) se copió de una versión antigua del T-12. Marca como «Cumple parcialmente» unas **98 filas que hoy son Cumple**: tiene 172 Parciales frente a 73 vigentes. Los 31 No cumple sí coinciden.

Un evaluador vería dos estados distintos para el mismo requisito. **Acción:** regenerar esa columna desde el T-12. Es una tarea mecánica y no cambia contenido.

Otros problemas de la misma matriz:
- Métodos de prueba incoherentes: TLS (RNF-14.01) y EDR (RNF-14.05) se verifican «con carga»; el material de capacitación (RNF-22.02) se verifica «con DR»; RT-10.01 y RT-10.05 se verifican «por inyección de fallas», aunque 9A-16 las mide en Producción.
- 9B-19 (DAST) cita RNF-14.07, que trata de SAST, SCA y contenedores.

## 3. Filas Cumple débiles: el contenido no respalda el estado

### 3.1 Rebajar a Parcial, o completar con 1–2 frases

| ID | Problema | Evidencia | Cierre |
| --- | --- | --- | --- |
| RF-01.04 | No conformidad en la recepción con tipo de lista y fotografía: no está desarrollada | SD4:955 | F (SD4 4.1.4.8) |
| RF-04.02 | No hay reasignación de pedidos entre vehículos ni recálculo de ETA | SD4:913,921 | F |
| RF-05.07 | No hay carga en secuencia inversa a la ruta | SD4:959 | F |
| RF-07.07 | No hay bandeja del cajero para pagos reportados («En Revisión») | SD3-Anexos:89 | F |
| RF-07.09 | Faltan el comprobante digital de abono y el traspaso del saldo insoluto al ERP | SD4:933 | F |
| RF-07.10 | **Contradicción interna:** Cumple, pero RF-07.11 (No cumple) y la Tabla 3.A.3a excluyen el cobro de preventistas | SD3-Anexos:92 vs :230 | **D:** decidir si se ofrece |
| RF-08.02 | No hay destino final seleccionable para la devolución (reingreso, venta con descuento, devolución al proveedor, destrucción) | SD5-Anexos:553 | F (SD5) |
| RF-08.04 | No hay alerta al preventista por umbral de envases | SD4:969 | F |
| RF-11.01 | No hay informes PDF/XLSX por correo; solo CSV/Parquet y aviso con enlace | SD5-Anexos:1508 | F |
| RF-11.02 | Faltan combustible, peajes, tiempo de conducción y prorrateo de indirectos | SD5-Anexos:1496 | F/D |
| RF-11.04 | No existe el índice Perfect Order | SD5-Anexos:1483 | F |
| RF-11.06 | Faltan devoluciones en tránsito y recaudo en efectivo; la latencia es de 2 h | SD5-Anexos:1510 | F |
| RF-11.08 | No se desarrolla la matriz de rentabilidad con sugerencias de frecuencia y pedido mínimo | SD13:448 | F |
| RF-12.07 | No queda escrita la causa de la confirmación o el rechazo comercial (ORDRSP) | SD4-Anexos:345 | F |
| RF-12.09 | `edi_asn` no tiene ETA ni referencia a la guía; SD4 no menciona el ASN | SD5-Anexos:739 | F |
| RF-12.27 | No hay restablecimiento de contraseña por enlace al correo | SD4:279 | F |
| RF-14.03 / 14.04 / 14.06 | Faltan la alerta por desvío >3 km, el tiempo de viaje por entrega y la geocerca del CD con registro de entrada y salida | SD4:977; SD5-Anexos:513 | F |
| RF-17.09 | La salida es solo HTML; no hay DOCX ni XLSX | SD4:1049 | F |
| RNF-14.06 / RT gemela | Dice «semestral», pero para Puelche se compromete una prueba anual | SD1:182 vs :185; SD9:516 | F (corregir la descripción o el SD1) |
| RNF-22.05 / RT-22.06 | Falta «sin costo adicional» en las jornadas de capacitación | T-14:1740 | F |
| RT-06.06 | Cita inexistente (SD6 6.1.3, Tabla 6.3). La obra civil se asigna a LafroX (meses 5-6) en T-9 y SD6-Anexos, y al CLIENTE (mes 3) en T-12 y T-14 | T-9:84; SD6-Anexos:51; T-14:598 | **D**, y alinear |
| RT-10.05 | Las ventanas de cambio se contradicen en la Tabla 14 (05:30–06:00 aparece como «No» y como «Sí») | SD4:2321 | F |
| RT-10.02 | Temperatura, evidencia de entrega y DTE: Alto (8 h) en la Tabla 16 y «críticos» (≤4 h) en las Tablas 17 y 37 | SD4:2379 vs 3197 | F |
| RT-11.07 | Se exige publicar solo por el borde (CloudFront + WAF), pero AS2 (NLB) y Verified Access quedan fuera sin excepción declarada | SD4:2573 | F (declarar la excepción) |
| RT-12.07 | No se renueva la sesión tras autenticarse (fijación de sesión) | SD4:666 | F |
| RT-12.09 | No aparece «no repudio» | SD4:739 | F |

### 3.2 Correcciones solo de cita (el estado se mantiene)

- RT-05.17: cambiar SD4-Anexos 4-B por SD4 4.1.10 (SD4:1216).
- RNF-21.05: cambiar 4.2.6.10 por SD4-Anexos 4-W.7.
- RF-03.10: agregar SD3-Anexos 3.G (RNG-03).
- RF-02.09: agregar SD13 (SD13:75).
- RNF-14.04: agregar los casos SIEM de SD4 4.1.3.7.
- **Citas de SD9, T-9, T-13 y T-17 que faltan:**
  - RT-04.03 a 04.05, 04.11 y 04.12: SD9 9.1.4, 9.1.5 y 9.2.2.
  - RT-04.04: SD9 9.2.5.
  - RT-07.07, 07.12, 10.07 y 11.20: SD9 9.3.3 (Tabla 9.9).
  - RT-09.06 y 09.08: SD9 9.2.3.
  - RT-10.09: SD9 9.1.5.
  - RT-13.01: SD9 9.2.2.
  - RT-19.05 y 20.07: T-9.
  - RT-20.08: **T-17**, que la fila exige.
  - RT-20.03 a 20.05 y RT-21.04: SD7 7.3.4 y 7.3.6.

## 4. Cambios de estado posibles con lo que ya está escrito

| ID | Actual | Sugerido | Respaldo |
| --- | --- | --- | --- |
| RNF-23.04 | Parcial | Cumple | T-11:56: gestión central, Falcon y cifrado de las 8 estaciones; la gemela RT-08.07 ya es Cumple |
| RT-25.01 | Parcial | Cumple | SD4:265: ≤3 interacciones por perfil, comprobado en prototipo y aceptación |
| RT-25.05 | No cumple | Cumple con una frase | SD4:267: sistema de diseño; falta solo «espaciado consistente» |
| RT-25.02 | No cumple | Parcial | SD4:283: retroalimentación y errores; faltan carga y transiciones |
| RT-25.04 | No cumple | Parcial | SD4:273: puntos de quiebre de 640–1.536 px; faltan las 5 resoluciones exigidas |
| RT-21.13 | No cumple | Parcial | T-9:124: el Comité de Operación revisa mensualmente la mesa con el CLIENTE |
| RT-13.04 | Parcial | Parcial con «Falta» reducido | T-13:73 y 9A-13: tasa de error ≤5 % |
| RT-02.10, RT-04.13, RT-08.11, RNF-14.05, RT-25.03 | Parcial | Parcial con «Falta» actualizado | Parte de lo faltante ya está escrito (ver los informes de B1, B3, A3 y B5) |

## 5. Otras contradicciones entre subdocumentos

| Tema | Dónde | Acción |
| --- | --- | --- |
| SOC 24×7: T-12 RT-11.17 lo presenta como propio; SD6 y T-9 dicen «condicional a subcontratación» | SD6:48; SD6-Anexos:61; T-9:94 | Alinear SD6 y T-9 con la decisión NOC/SOC |
| SD2-Anexos compromete disponibilidad ≥99,95 % (T-12: 99,9 %) y cita «BTT §7.2» | SD2-Anexos:34 | Corregir a 99,9 % y BTT cap. 10 |
| SD2-Anexos usa RT-03.12 para la sincronización (corresponde a RT-03.13), rótulos RNF-DISP, REND, RESIL, SEG y DR que no existen, y «Caso cap. 10» | SD2-Anexos:34-38 | Remapear los códigos |
| Tabla 9.9 de SD9: los meses 32, 33, 44 y 45 no coinciden con el Gantt; el mes 32 cae en el congelamiento | SD9:514 vs 440-456 | Corregir la tabla o el Gantt |
| Revisión de riesgos «en cada Comité» frente a «trimestral»; el comité es quincenal | SD8-Anexos:1050 | Corregir la frecuencia |
| SD9 habla de «cinco análisis mínimos»; RT-04.05 enumera seis controles | SD9:227 | Precisar |
| T-14 3.1.1: «hasta el mes 5 (H3)»; el resto: H3 en el mes 6 | T-14:1135 | Revisar la redacción |
| CMMI-DEV vence en noviembre de 2026; la renovación «antes de noviembre» queda casi inmediata | SD1:202-205 | Confirmar con el equipo |

## 6. Pendientes vigentes por tipo de cierre

**F — una o dos frases en el subdocumento dueño (≈30):**
- SD5, modelo de datos: RF-01.08, 01.10, 01.11, 02.01, 02.03, 02.07, 02.08, 04.01, 04.03, 07.04, 07.06, 08.07, 11.05 y RF-18.03.
- SD4: RT-02.10 (umbral de cola), 03.08 y 04.13 (remitir a la Oferta Económica), 06.04 (normas de cableado), 06.29 (telefonía en Talca), 11.08 y RNF-14.01 (TLS: suites, HSTS, vencimiento), 11.13, RF-14.03-BTT y RF-19.03 (FQDN en la Tabla 19), 16.14 (motor de reglas), 16.17 (firma avanzada no aplicable), 16.23 (apertura), 25.02 y 25.03 (carga y alt-text), RNF-12.03, RNF-19.02.
- T-11: RT-08.12 y RNF-23.02 (grado IP y caídas), RT-08.14 (MDM).
- SD1: RT-15.02, 15.07 y 23.01 (misión, visión, valores, URL); RT-23.06 (URL + declaración jurada en el Sobre 1).
- RNF-21.07 (traslado de N2/N3 a Curicó, Chillán y Los Ángeles).

**D — dato o decisión del equipo (≈35):**
- Dominio, NOC/SOC y su ciudad: RT-21.01, RNF-21.01, RT-11.17, RT-23.05.
- Bolsa de 768 HH: RT-21.19, RNF-21.08.
- Baterías: RT-17.07.
- Gerente de servicio: RT-21.02, RNF-21.02.
- Tiempo real: RF-16.02, RT-14.02.
- Firma avanzada: RF-18.01.
- RPO ante triple falla: RT-07.04, RNF-20.06.
- Disparo automático de DR: RT-07.08.
- EDR en el servidor ERP: RT-11.16, RNF-14.05.
- Precios, en conflicto con BA Art. 50.2 (remitir a la Oferta Económica): RT-08.10, RNF-23.01, RT-14.08.
- Fichas técnicas: RT-08.01, 08.04, 08.11.
- Carbono: RT-15.03, 15.04.
- Certificaciones personales: RT-15.08.
- Proveedor de mensajería: RT-16.24.
- Otros:
  - RT-05.10 (catálogo con linaje);
  - RT-06.12 (doble acometida);
  - RT-11.04 (aclaración sobre el congelamiento);
  - RT-13.04 (aprendizaje por perfil);
  - RF-03.12 (precio por línea del ERP);
  - RF-07.03, 07.10 y 07.11 (cobranza);
  - RF-09.05 (termógrafo en línea);
  - RT-18.10 (RPA).
- Por decisión ya tomada: RT-05.24, 15.05 y 16.26.

**S — subdocumento aún no redactado (≈8):**
- SD10 (soporte): RT-21.08, 21.12, 21.13, 21.16.
- SD12 (equipo): RT-21.03, 23.03.
- SD11 (bolsa): RT-21.19, ligado a la decisión de las 768 HH.

**Entregables fuera de los subdocumentos:**
- Video (RT-24.01 a 24.06): ninguna Aclaración le asigna dueño.
- Prototipo con el Informe 3: RT-25.04 y RT-25.06 a 25.10.
- Sitio web: RT-23.02, 23.05 y 23.07 a 23.10. El sitio existe (rama `alex` de lafrox-web), pero falta publicarlo con dominio y declararlo.

## 7. Orden sugerido

1. Regenerar la columna «Estado T-12» de SD9-Anexos 9.C. Es mecánico y elimina la contradicción más visible.
2. Aplicar las correcciones de cita (§3.2) y los cambios de estado respaldados (§4).
3. Decidir RF-07.10 y RF-07.11 (cobro de preventistas) y RT-06.06 (quién ejecuta la obra civil).
4. Redactar las frases F (§3.1 y §6), con mínimo arrastre.
5. Resolver las decisiones D pendientes: dominio, NOC/SOC, 768 HH, baterías y gerente de servicio.
