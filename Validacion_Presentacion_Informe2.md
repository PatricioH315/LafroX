# Validación de la presentación del Informe 2 (v4)

- **Archivo resultante:** `LafroX - Presentación Informe 2 v4.pptx`, con 35 diapositivas. La v3 no se modificó.
- **Fuentes revisadas** (ramas remotas al 19-10-2026; `git fetch` no trajo cambios):
  - SD1 `LafroX-Subdoc1-LateX` 938945a
  - SD2 `LafroX-Subdoc2-LateX` 9aaffa7
  - SD3 `LafroX-Subdoc3-LateX` 01e8b60
  - SD4 `subdoc-4` 5abf4c6
  - SD5 `LafroX-Subdoc5-LateX` 2f93655
  - SD6 `LafroX-Subdoc6-LateX` d4b8849
  - SD7 `LafroX-Subdoc7-LateX` 25002fd
  - SD8 `Lafrox_Subdocumento_8_Latex_Nuevo` 30e2083 (la rama vigente)
  - SD9 `LafroX-Subdoc9-LateX` 5cac7ca
  - SD13 `LafroX-Subdoc13-LateX` 83ecc44
- **Método:** cuatro revisores Codex en solo lectura cubrieron todas las diapos y sus notas. Después, cada observación se comprobó a mano en el `.tex` correspondiente. Solo se corrigieron los errores confirmados; el resto queda abajo como pendiente o descartado.

En las tablas, «Pos.» es la posición de la diapo en la v4 y «N.º» es el número que se ve en pantalla.

## 1. Diapositivas agregadas

| Pos. | N.º | Diapo | Figura y origen |
|---|---|---|---|
| 7 | 06 | Esquema de solución | SD3, Figuras 3.1, 3.2 y 3.3 (`figures/figura 3.{1,2,3}.pdf`). Va antes del Mapa de módulos, en el mismo orden que el SD3. |
| 9 | 08 | Arquitectura lógica | SD4, Figura 1, «Vista general completa de la arquitectura lógica» (`04/figuras/logica/capas/ARQL-01_General_definitivo.pdf`). Junto a la figura se listan las 8 capas con los nombres de las subsecciones de SD4 4.1. |
| 10 | 09 | Arquitectura física | SD4, Figura 14, «Vista general de la arquitectura física híbrida» (`04/figuras/fisica/Arquitectura_Fisica_General.png`). |

- **Mapa de módulos:** se mantiene y pasa a la posición 8 (n.º 07).
- **Diapos siguientes:** se renumeraron con +3. Por ejemplo, Arquitectura híbrida pasa a 10 y el cierre a 32.
- **Notas del orador:** las tres diapos nuevas tienen notas redactadas con el texto del SD3 y del SD4.
- **Imágenes:** van en alta resolución, así que se pueden ampliar al presentar. Las figuras originales no se tocaron.

## 2. Correcciones aplicadas (verificadas en la fuente)

| Pos. (n.º) | Antes | Después | Fuente |
|---|---|---|---|
| 1 y 35 (—, 32) | www.lafrox.cl | lafrox.github.io | SD1 `contenido.tex:19`. Es el sitio web declarado. |
| 3 (02), notas | 41 % de recepciones sin lote | … en el producto del retiro | SD2 `contenido.tex:119, 194`: «El 41 % corresponde solo al producto del retiro». |
| 4 (03) | Recepciones sin lote | Sin lote (prod. retirado) | SD2, Tabla 2.1 (`contenido.tex:119`) |
| 4 (03), notas | ninguna recepción sin lote | … en los productos que lo requieren | SD2 `contenido.tex:332`: «Todo producto que lo requiera». |
| 5 (04) | 4 certificaciones: ISO 9001 · 27001 · 20000-1 · CMMI N3 | 4 credenciales: … | SD1 `contenido.tex:225–228`. CMMI-DEV N3 es una *evaluación Benchmark*, no una certificación. |
| 5 (04), notas | certificaciones ISO …, y CMMI nivel 3 (SD1, T-6) | certificaciones ISO 9001, 27001 y 20000-1, y evaluación CMMI-DEV nivel 3 (SD1 y T-6) | Misma fuente. |
| 8 (07) | Sistemas externos: ERP 2017 · GIS y GPS · Cadenas | Sistemas externos: ERP 2017 · Transbank (pagos) · Geolocalización (mapas y posición para rutas); Cadenas (EDI) bajo «Integración · Etapa 2» | SD3 `contenido.tex:304, 388, 412`: los tres sistemas externos son el ERP, Transbank y la geolocalización; las cadenas se integran en la Etapa 2. |
| 8 (07), notas | … y los sistemas externos. | … y los tres sistemas externos: ERP, Transbank y geolocalización; las cadenas se integran por EDI en la Etapa 2. | Misma fuente. |
| 11 (10), notas | Tres caminos: fibra, LTE y Starlink | En los CD, tres caminos; en los cross-docking, Starlink con respaldo LTE | SD4 `4.2_fisica/02_a_emplazamiento.tex:41, 218–219` |
| 12 (11) | Migración: 32 GB | Migración: 16 GB de origen | SD5, Tabla 5.2 (`tablas/volumen_migracion.tex`): 16,05 GB de origen; 32,11 GB es el almacenamiento estimado en destino. |
| 12 (11), notas | Migramos 32 GB con cero diferencias | Migramos unos 16 GB de origen (32 GB estimados en destino) con cero diferencias sin explicar | SD5 `5_3_migracion.tex`: «diferencias no explicadas = cero». |
| 16 (15), notas | Cierra con el H2 en el mes 4 | … y, en la Etapa 2, con el H8 en el mes 14 | SD7 T-14, Tabla del 2.4 (`tab_T14_15.tex`) |
| 21 (20), notas | gestión del cambio con el sindicato y los transportistas | … con las cadenas y los transportistas | SD7 T-14: 7.2.2 «con las cadenas y los transportistas»; el sindicato está en 5.4.2. |
| 27 (25) | 69 personas · peak de dotación · mes 15 | 69 personas · equivalentes · peak del mes 15 | SD7 T-15 `contenido.tex:112, 121`: «69 personas equivalentes»; la curva es de demanda, no de dotación acreditada. |
| 27 (25), notas | con 69 personas | con 69 personas equivalentes | Misma fuente. |
| 29 (27), notas | Los seis riesgos de mayor exposición | Seis de los diez riesgos de mayor exposición | SD8, Tabla 8.4: R-011, R-014 y R-016 (0,24) superan a R-001 (0,20). |
| 30 (28) | p95 ≤ 1 s · ≥ 99,9 % disponible | Preparación p95 ≤ 1 s · ≥ 99,9 % disponible | SD9, Tabla 9.3: el umbral de ≤ 1 s es el de preparación. |
| 30 (28) | ISO/IEC 29119 | ISO/IEC/IEEE 29119 | SD9, Tabla 9.2 |
| 30 (28) | Costo de calidad: 11.136 HH | Conformidad programada: 11.136 HH | SD9 §9.1.6: «La conformidad programada suma 11.136 HH, el 5,1 %». |
| 30 (28), notas | ISO 25010 fija umbrales …; costo de calidad (11.136 HH); (SD9 Tabla 9.2 …) | ISO 25010 ordena las características con su umbral …; 11.136 HH de conformidad programada; (SD9 Tablas 9.2 y 9.3 …) | SD9, Tablas 9.2 y 9.3 y §9.1.6 |
| 31 (29) | 0 incidentes críticos | 0 incidentes críticos o altos | SD9 T-17 (condición 1 del art. 17.3) y SD7 `contenido.tex:443` |
| 31 (29) | G3 · Sin vulnerabilidades altas | Sin vulnerabilidades críticas o altas | SD9, Anexo 9 (`09_anexos/contenido.tex:165`) |
| 32 (30) | Meta: ±15 % en ≥80 % de los casos | … de los lotes | SD13, indicador I-03B (`13_innovaciones/contenido.tex:389–394`) |
| 33 (31) | personas en el peak (mes 15) | personas equivalentes en el peak (mes 15) | SD7 T-15 |
| 33 (31), notas | Peak de 69 personas (SD1 Tabla 1.6) | Peak de 69 personas equivalentes (SD1 Tabla 1.6; SD7 T-15) | El peak está en el T-15, no en el SD1. |

## 3. Pendientes que requieren decisión (no se tocaron)

1. **OTIF «> 95 %» (pos. 4).** Coincide con la Tabla 2.1 del SD2 (referencia del caso). El SD3 (`contenido.tex:189`) compromete un 95 % en el mes 32. Las dos cifras están en los subdocumentos.
2. **RTO ≤ 4 h · RPO ≤ 15 min · ≥ 99,9 % (pos. 11).** En el SD4 aplican a los *servicios críticos* y a la *transacción crítica*. Como titular está bien, pero conviene decirlo al presentar.
3. **«Pallet o canastillo con su lote» (pos. 12).** El SD3 menciona «canastillo/pallet», pero el SD5 tipifica las unidades como pallet, caja o contenedor, y los canastillos se controlan por saldo.
4. **Gantt «Sep/Dic» (pos. 25–26).** La ubicación supone un inicio en febrero de 2027 (SD7, anexos). Se recalcula cuando se confirme la fecha de inicio.
5. **129.879 HH de Operación (pos. 14 y 22).** Es la suma de los paquetes de la fase 8 de la EDT, y es correcta en ese contexto. El bloque contractual de Operación (m21–56) programa 128.854 HH.
6. **Citas de las notas en las pos. 28–29 (riesgos).** Las probabilidades 35/30/25/45 % están en el Anexo 8.B y las reservas en el §8.6. La Tabla 8.4 solo tiene la exposición cualitativa.
7. **Paráfrasis aceptables que podrían precisarse:**
   - «−30 % horas de diagnóstico» se refiere a la *mediana* (SD13, I-02A).
   - «4 semanas de volumen real» corresponde al 100 % del volumen real en las últimas cuatro semanas.
   - «trazable de punta a punta, aun sin señal» (notas del cierre): la trazabilidad central se completa al reconectar.

## 4. Observaciones descartadas

- **«24×7 · NOC, SOC y Mesa» (pos. 5):** es correcto según el SD1 (NOC 24×7 en la Tabla de dotación y mesa 24×7 en el alcance de la ISO 20000-1). El horario 04:00–22:00 del T-15 se refiere al contrato con Puelche, no a LafroX.
- **Merma 1,7 % → ≤ 1,0 %:** coincide con la Tabla 2.1 del SD2.
- **RBS (pos. 28):** «45 riesgos · 7 ramas · 2/23/19/1» coincide con la rama vigente del SD8. La rama antigua `LafroX-Subdoc8-LateX`, con 32 riesgos en 3 ramas, ya no aplica.
- **«Cada rama tiene un color…» (notas):** describe el diseño de la presentación, no es un dato de los subdocumentos.

## 5. Verificado sin observaciones

Las demás cifras y códigos coinciden con los subdocumentos:

- **Retiro y diagnóstico (SD2):** 9 días, 4.800 kg, 6 meses, 6 % de las ventas, OTIF 82,4 %, 4,2 % y $4,2 M/mes.
- **LafroX y referencias (SD1):** 124 especialistas, y 420/96 camiones, 22.000/≈1.400 entregas y 280/62 preventistas.
- **Solución y arquitectura (SD3, SD4, SD5):**
  - etapas con producción en los meses 16 y 21;
  - 7 interfaces y M1–M12;
  - AWS São Paulo en 2 zonas con recuperación en Virginia, y 14 h / 24 h sin conexión;
  - 8 capas y 22 ADR;
  - 15 dominios y EPCIS 2.0.
- **Gestión, EDT y plan (SD6, SD7):**
  - SPI/CPI < 0,90 y el ritmo de gobierno;
  - EDT con 9 fases, 49 cuentas de control y 222 paquetes, con las HH de cada fase;
  - bloques y frentes F1–F8, y los hitos H1–H12;
  - riesgos por mes;
  - 8.106 HH en el mes 15 y 217.543 HH en total.
- **Riesgos, calidad e innovaciones (SD8, SD9, SD13):**
  - responsables y probabilidades de los seis riesgos, y 2.058 + 1.600 HH;
  - normas y leyes;
  - G0–G6, 1.316 casos y −22 °C;
  - las 5 innovaciones con sus metas.
