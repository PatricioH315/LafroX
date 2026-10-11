# Revisión de la Comisión — Informe 2 · Subdocumento 9 (v8, verificación de la v7 y de las correcciones de coherencia)

**LAFROX · GRUPO 2 · INFORME 2 · Caso 2 · Distribuidora Puelche S.A.**

**Archivos recibidos** (`09_plan_calidad/`): `LAFROX-Subdocumento9.md`, `LAFROX-Subdocumento9-Anexos.md`, `LAFROX-Formulario-T-13.md`, `LAFROX-Formulario-T-17.md`. Nomenclatura correcta, un formulario por archivo. Se cotejan con SD1, SD3, SD4, SD5, SD6, SD7, SD13, T-10, T-14 y T-15.

**Alcance.** Aplica `prompt_revision_comision_informe2.md` al estado del SD9 después de corregir las cinco contradicciones con subdocumentos anteriores (fecha habilitada tras el congelamiento, meses de marcha blanca de la Tabla 9.12, severidad de defectos frente al SD4 Tabla 16, escalamiento del Líder de Calidad y regla CMMI del SD1). Las comprobaciones exclusivas del PDF quedan pendientes. El SD8 se está rehaciendo: lo que depende de su registro se marca *No verificable con el material recibido*.

**Diagnóstico.** Puntaje actual **0/100** por indicios de IA (ACL §7.1 d): 16 celdas `[[REVISIÓN HUMANA]]` (SD9 10, Anexos 4, T-13 1, T-17 1) y el marcador literal «borrador» en el SD9, 9.3.2. **Sin esa causal: 40.** Pasa los nodos 1 a 6 del árbol: sin precios, formularios presentes, títulos del índice presentes y sin contradicciones de diseño con subdocumentos anteriores. Queda en el nodo 7 por las figuras sin imagen, el corte de trazabilidad del retiro sanitario en el T-13 y el paquete faltante de la restauración de los meses 13 a 20.

---

## 0. Fuera del puntaje de contenido (igual dejan el ítem en 0)

- **Crítico — 16 celdas `[[REVISIÓN HUMANA]]`.** Sólo un integrante puede completarlas con la revisión que efectivamente hizo.
- **Crítico — marcador «borrador».** SD9 9.3.2: «se presentan primero como borrador» y «su control es el borrador anticipado». El Paso 1.2 lo lista como indicio. También en T-15, sección 5.5.
- **Crítico condicionado — figuras.** Las 10 figuras del SD9 son bloques Mermaid sin imagen enlazada; `Diagramas/` sólo tiene `.drawio` y un `.xlsx`. Si el PDF no trae el dibujo aplica la ACL §7.1 a.

---

## 1. Verificación de las correcciones de coherencia (5)

| Contradicción | Estado | Evidencia |
| --- | --- | --- |
| Corrección diferida al «26 de septiembre» frente al SD4 Tabla 14 y el T-10 | Corregido | SD9 9.3.2 y T-13 §8: primera fecha habilitada 5-10-2028, igual al T-15, 4.1 |
| Marcha blanca 13–16 y 19–21 en la Tabla 9.12 | Corregido | 13–15 antes del H7 (mes 16); 19–20 antes del H12 (mes 21), igual a SD5 5.3.4, SD7 y T-10 |
| Severidad de defectos distinta del SD4 Tabla 16 | Corregido | 9.2.6 clasifica por nivel de servicio; incluye identidad de bodega; seguridad con escala y plazos propios; 9.2.2 alineada |
| Escalamiento al «Comité Ejecutivo» | Corregido | 9.1.1: Comité de Calidad y Procesos y Gerencia General (SD1 1.2) |
| Regla CMMI ausente | Corregido | 9.1.2 incorpora la regla del SD1 1.4 |

## 2. Verificación de la v7 (13 observaciones)

| Estado | Observaciones |
| --- | --- |
| **Parcial** (2) | N7-04 (el SD4 ya declara instancias separadas que se apagan al terminar, pero sin tope simultáneo ni capacidad total), N7-10 (10 de 31 citas a las Bases traen página; 21 sin ella) |
| **No corregido** (10) | N7-01, N7-02, N7-03, N7-06, N7-07, N7-08, N7-09, N7-11, N7-12, N7-13 |
| **No verificable** (1) | N7-05 (depende del SD8) |

---

## Nivel 1 — Contradicción y trazabilidad

**N8-01 (= N7-01). Restauración mensual de los meses 13 a 20 sin paquete.** SD9 9.3.2 y Tabla 9.14 la asignan al 8.1.6; el T-14 define el 8.1.6 como «Mensual, meses 21 a 56» con 36 informes y el T-15 lo programa en 21–56. *Se espera:* paquete o extensión del 8.1.6 en T-14 y T-15 (cambio en el SD7).

**N8-02 (= N7-02). El retiro sanitario en menos de 2 horas no tiene prueba en el T-13.** El T-13 no contiene «retiro» ni «simulacro». La cadena del requisito crítico se corta en S9/T-13, aunque el SD3 Tabla 3.A.13 fija el simulacro en la marcha blanca E1. *Se espera:* tipo de prueba con criterio de entrada, salida, ambiente, paquete y fecha.

## Nivel 2 — Capacidad, fundamento y cierre

**N8-03 (= N7-03).** Tablas 9.12 y 9.13 con seis columnas (máximo cinco en el cuerpo).

**N8-04 (= N7-04, parcial).** Instancias de Preproducción simultáneas sin tope ni capacidad declarada en SD4/T-11.

**N8-05 (= N7-06).** Duplicación ≤ 3 %, inestabilidad ≤ 0,5, utilización ≤ 70 % y regresión ≤ 10 % siguen sin origen citado.

**N8-06 (= N7-07).** La DR del mes 21 no figura en la ficha H12 del T-17. Ahora además el H12 puede esperar una promoción del 5-10-2028 (9.3.2); el T-17 no recoge esa condición.

## Nivel 3 — Forma

**N8-07 (= N7-08).** Tabla 9.5 mezcla puerta y flujo en la fila «G0–G4 y G6».

**N8-08 (= N7-09).** Fuente de la Tabla 9.12 cita «T-15, sección 4.5» para la reserva protegida, que está en la 4.1.

**N8-09 (= N7-10).** 21 de 31 citas a las Bases sin página.

**N8-10 (= N7-11).** 13 filas de la matriz 9.C con «Presentación de la oferta» como hito.

**N8-11 (= N7-13).** Binarios desfasados en `Diagramas/`.

---

## Dependencia del SD8

Sin cambios respecto de la v7, sección 4: re-verificar al cerrar el SD8.

---

## Ruta a 60

1. Cerrar N8-01 (en T-14/T-15) y N8-02 (en T-13).
2. Cerrar N8-03 a N8-06.
3. Limpiar N8-07 a N8-11 y reemplazar «borrador» por «versión preliminar».
4. Fuera del puntaje: 16 celdas de revisión humana e imagen de las 10 figuras.

| Ítem | Peso | Puntaje actual | Ponderado | Sin la causal | Ponderado sin la causal |
| --- | --- | --- | --- | --- | --- |
| 9. Plan de calidad (T-13, T-17) | 8 % | 0 | 0,0 | 40 | 3,2 |
