# INSTRUCCIONES GLOBALES DE CALIFICACIÓN — RÚBRICAS POR ENTREGABLE

**Licitación:** TFEP-01/2026 · **Caso:** 02 — Logística (Distribuidora Puelche S.A.)
**Uso:** estas instrucciones aplican a **todas** las rúbricas de `rubricas/`. Cada rúbrica por entregable verifica contenido y coherencia contra las Bases, aunque el documento preliminar no esté seccionado: la evaluación es por **contenido**, no por el orden interno del documento.

**Fuente de verdad (precedencia):** `Bases_Administrativas.md` (AA) > `Bases_Tecnicas_Transversales.md` (TT) > `Caso_02_Logistica.md` (C). El caso puede **endurecer** un requisito transversal, nunca **rebajarlo**.

---

## 1 · Inventario de entregables (visión clara del proceso)

| # | Entregable | Rúbrica que lo evalúa | Fecha (T-20) | Sobre/instancia formal |
|---|---|---|---|---|
| 1 | Informe 1 (documento escrito): subdocs. 1, 2, 3, 4.1, 4.2, 5 y 13 | `Rubrica_Informe1.md` | 07-09-2026 | Preparatoria |
| 2 | Presentación preparatoria 1 (PPT) — agenda cerrada del T-22 | `Rubrica_Presentacion1_PPT.md` | 14-09 a 25-09-2026 | Preparatoria |
| 3 | Soporte de requerimientos Cap. 17.1 (catálogos RF/RNF, supuestos y 16 decisiones 16.1, reglas de negocio, matriz de trazabilidad, vacíos/consultas) | Dentro de `Rubrica_Informe1.md` (subdoc. 3 y 5; no capítulos extra) | Íntegro en el informe | Documento |
| 4 | Planilla T-12 Matriz de Cumplimiento (todos los RT) | Referencia: `Rubrica_Informe1.md` + bloqueante G4 | Con la propuesta final | Sobre N° 2 |
| 5 | Página web corporativa activa (verificación durante todo el proceso; declaración jurada en Sobre N° 1) | `Rubrica_PaginaWeb.md` | Desde el registro y toda la evaluación | Sobre N° 1 (final) |
| 6 | Consultas al mandante (Art. 43.3) — acta publicada el 07-09 | Referencia: coherencia con `Rubrica_Informe1.md` (P3.14) | 07-09 | Canal oficial |
| 7 | Diagramas de arquitectura (fuente .md → PNG/SVG/PDF) | Partes 4.1/4.2 del Informe 1 | En el informe | Documento |
| 8 | Video de presentación (Cap. 24 TT) — máxima 5 min, equipo clave completo, 6 segmentos | `Rubrica_Video_y_Prototipo.md` (no es Entrega 1) | Con la propuesta final | Con la propuesta final |
| 9 | Prototipo interactivo + arquitectura de información (Cap. 25 TT) | `Rubrica_Video_y_Prototipo.md` (no es Entrega 1) | Con el Informe 3 | Con el Informe 3 |
| 10 | Tabla de trazabilidad observación→respuesta→sección para el Informe 2 | Referencia: `Rubrica_Presentacion1_PPT.md` §Reglas | Alimenta el Informe 2 | Informe 2 |

**Reglas duras del proceso (aplican a toda la propuesta):**
- La presentación preparatoria es obligatoria: no presentar = quedar fuera del proceso (AA §1834).
- Los tres sobres son simultáneos y copulativos; la falta de cualquiera hace inadmisible la oferta (AA §48.2). Esto aplica a la entrega final, no a ésta.
- Un entregable sometido a aceptación debe incorporar: el artefacto, evidencia de verificación, trazabilidad a los requerimientos y el registro de observaciones previas resueltas (AA §18.2).

---

## 2 · Escala de veredicto (usar en todas las rúbricas)

| Veredicto | Significado | Valor para el cálculo |
|---|---|---|
| **OK** | Cumple el criterio íntegro, con evidencia en el documento | 100 |
| **PARCIAL** | Presente pero débil, incompleto o sin fundamento verificable | 50 |
| **NO** | Ausente, contradictorio o con dato erróneo | 0 |

Siempre anotar la **evidencia de ubicación** (sección/página del preliminar) y, en NO/PARCIAL, el **fundamento normativo** (artículo/numeral) que exige el criterio.

---

## 3 · Verificaciones transversales de coherencia (aplican a todo entregable)

### 3.1 Cifras canónicas (o marca halaga-cero si difieren)

| Métrica | Valor canónico |
|---|---|
| Clientes/puntos de entrega | 14.200 (11.600 trad. / 2.100 food service / ~500 sup.) → 15.500 @3a |
| SKU | 8.400 → 9.500 @3a (de ellos 1.100 → 1.400 refrigerados/congelados) |
| Pedidos / líneas / unidades mensuales | 31.000 → 36.000 · 260.000 → 305.000 · 2,4 M → 2,8 M |
| Entregas día normal / peak sept | ≈ 1.400 / ≈ 2.600 (→ 1.650 / 3.100 @3a) |
| Viajes camión mes / km mes | ≈ 2.100 / ≈ 420.000 |
| Recepciones mes / pallets CD Talca | 1.150 / 14.500 |
| Posiciones de conteo cíclico | 3.400/mes (diferencia 2,3 %) — **no confundir con posiciones de almacén** |
| Documentos tributarios | ≈ 34.000/mes |
| Devoluciones mes | ≈ 900 |
| Envases retornables | 68.000 canastillos + 9.400 pallets (pérdida 14 % anual) |
| Visitas preventa / cobros efectivo | ≈ 62.000 / ≈ 11.800 mensual |
| Preventistas / conductores / personal CD | 62 · ≈200 (42 propios + ~160 terceros) · 310 (todos los turnos) |
| Camiones | 96 (42 propios + 54 transportistas) · **camiones ≠ conductores** |
| Instalaciones a cubrir | **6** + la calle + 14.200 puntos → 7 @3a |
| OTIF / fill rate actuales | 82,4 % (meta > 95 %) · 91,3 % (meta > 97 %) |
| Retiro sanitario | lote 24-0217 · 9 días · $ 31.000.000 · 4.800 kg · suspensión 6 meses (≈ 6 % ventas) |
| Recepciones sin lote | 41 % |
| Ventana despacho | 05:30–07:00 lunes a sábado, indisponibilidad cero |
| Congelamientos | 1–25 sept + todo dic + 3 primeros días hábiles de cada mes |

### 3.2 Innegociables

- **Cronograma (AA Art. 17°):** Etapa 1 = meses 1–15 (desarrollo + marcha blanca; producción mes 16) · Etapa 2 = meses 13–20 (producción mes 21) · Operación = 21–56. Solape meses 13–15 y 19–20. "1–12 como Etapa 1 completa" es error.
- **Híbrido (AA Art. 16.1):** carga principal en nube pública + componentes on-premise. No se admite solo-nube ni solo-on-premise; asignación sin justificar por componente = observación grave (Art. 16.2).
- **5 innovaciones (AA Art. 28):** una por tipo, sin repetir, trazables con arquitectura, EDT y flujo de caja.

### 3.3 Inconsistencias de las Bases (declarar en consultas/supuestos, NO corregir unilateralmente)

| # | Tema | Dato |
|---|---|---|
| A | Nº instalaciones | C §8 dice 5; Tabla 14.1 y RT-21.16 dicen 6 en 4 regiones (Curicó–Los Ángeles, 340 km). Usar 6 + consulta |
| B | Ponderación T-21 | Columna suma 98 % (declarada 100 %) |
| C | Nº ambientes | Art. 24° dice 4; Transversales/RT-04.01 dicen 5 + DR. Usar 5 + DR |
| D | Códigos RT mal mapeados | Red inalámbrica → **RT-03.23** (el caso dice 03.24); sync reconexión → **RT-03.12** (caso dice 03.13); retención → **RT-16.10** (caso dice 05.10); emplazamiento on-premise → **RT-06.01 es "espacio exclusivo/aislado"**, no tipología |
| E | Camiones ≠ conductores | ≈200 vs ≈244 según lectura; aclarar en supuestos |
| F | Fechas calendario | Registro (14–17 ago) antes de publicación (19 ago); Informe 1 = Acta 07-09; Informe 3 + Presentación 3 el mismo día (contra Art. 45). No alterar cronograma |
| G | Desconexión | "2 h" (nominal) vs turno 14 h (contingencia de diseño): documentar ambos |
| H | Nomenclatura | Siempre TFEP-01/2026 (nunca FEP01.26/FEP02.26) |

### 3.4 Mapa de coherencia (validar en cada entrega)

| Regla | Fuente | Qué validar |
|---|---|---|
| Lógica ↔ Física | AGENTS política fuente de verdad | Mismo stack/capas en lógica, física y diagramas |
| Arquitectura ↔ Costos | AA Art. 16 nota | Cada componente físico con costo; sin arquitectura que lo sustente = incoherencia grave |
| Alcance ↔ Catálogo ↔ Arquitectura | C §931–933 | El alcance sale del catálogo; la arquitectura sostiene el alcance |
| Requerimientos ↔ EDT ↔ Pruebas | C §823 | Matriz de trazabilidad: origen→RF→componente→EDT→prueba→aceptación |
| Criterios Cap. 18 ↔ metas | C §899–920 | Meta comprometida (o propuesta), mes en que se alcanza, cómo se mide |

### 3.5 Checklist de coherencia del caso

- [ ] Distingue los **3 problemas**: habilitación sanitaria/comercial, competitividad del servicio, costo. (C §930)
- [ ] Arquitectura resuelve **verificablemente**: despacho durante corte, turno 14 h sin señal, captura a −22 °C, integración ERP+DTE, peak septiembre. (C §932)
- [ ] Modelo de datos **soporta la pregunta del proveedor y de la autoridad** y declara las **16 decisiones 16.1**. (C §933)
- [ ] Decisión sobre el **WMS de 2013** tomada y fundada. (C §931, D14)
- [ ] **Exclusiones explícitas** (excluir ≠ ignorar). (C §931, §597)
- [ ] NO supone un **cliente digital que no existe** (almacenero sin internet, pago en efectivo). (C §940–942)
- [ ] Hace cargo del **sindicato** (cámaras en cabina / GPS jornada) con plan de gestión del cambio. (C §10.10, D13)
- [ ] **Planificador** (D16 / criterio 16): captura del conocimiento antes de la jubilación. (C §920)
- [ ] **Conductores de terceros** (D5): identidad y capacitación propias. (C §17.6.6)
- [ ] **Efectivo** (D6): camino propuesto (eliminar/reducir/controlar) con consecuencias. (C §546, §772)
- [ ] **Costo de servir** (D7) construido desde el hecho. (C §913, §550)
- [ ] **GS1 / DTE / RSA / cadena de frío** usados con propiedad técnica. (C §788–806)

---

## 4 · Método de calificación

1. Aplicar la escala (§2) criterio por criterio de la rúbrica correspondiente, con nota de evidencia.
2. **Puntaje de ítem** (0–100) = promedio de sus criterios (en Informe 1, los ítems son los subdocs. 1–13 del T-21; en los demás entregables, los bloques de la rúbrica).
3. **Puntaje Informe 1** = Σ (puntaje ítem × ponderación columna "Informe 1" del T-21): Transversal 4 % · Subdoc 1 → 4 % · Subdoc 2 → 11 % · Subdoc 3 → 21 % · Subdoc 4.1 → 16 % · Subdoc 4.2 → 16 % · Subdoc 5 → 11 % · Subdoc 13 → 17 % (**suma 100 %**; consultar inconsistencia B).
4. **Bloqueantes** (bajan nota dura o anulan el criterio donde aparecen):

| Id | Bloqueante | Origen |
|---|---|---|
| G1 | Cifra canónica errónea (Tabla §3.1) | AUDITORIA §2.3 |
| G2 | Cronograma fuera del Art. 17° | AA Art. 17° |
| G3 | Propuesta solo-nube o solo-on-premise | AA Art. 16.1 |
| G4 | RT respondido contra código mal mapeado del caso (no del transversal) | AGENTS inconsistencia #4 |
| G5 | Diagrama genérico (no reconocible como Puelche) | AA §1565, §1841 |
| G6 | Innovaciones repetidas o fuera de tipo obligatorio | AA Art. 28.1 |
| G7 | Celdas del 14.2 vacías o sin método/supuestos | C §668, §699–720 |
| G8 | Código, sección o cohorte con "celdas vacías" en los formularios | T-12 / T-11 |

5. **Cierre:** para cada NO/PARCIAL indicar el lugar exacto de corrección en el preliminar y el artículo/numeral que exige el criterio.