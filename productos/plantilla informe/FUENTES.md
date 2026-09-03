# Fuentes y trazabilidad del Informe 1 (plantilla esqueleto)

Documento de apoyo para el estudiante. Registra, por cada sección de la plantilla, **de dónde provino** el contenido (documento, capítulo/artículo, líneas) y **qué se debe considerar**. Sirve para verificar coherencia y para las referencias en norma APA 7.ª ed. que pide el Subdoc. 2.

Referencias abreviadas usadas abajo:

- **AA** = `Bases/Bases_Administrativas.md` (Licitación N° TFEP-01/2026 — Bases Administrativas)
- **TT** = `Bases/Bases_Tecnicas_Transversales.md` (Bases Técnicas Transversales)
- **C** = `Bases/Caso_02_Logistica.md` (Caso 02 — Logística, Distribuidora Puelche S.A.)

> Regla de precedencia (GG Art. 5°): AA > TT > C. El caso puede endurecer un requisito transversal, nunca rebajarlo.

---

## MAPEO GLOBAL: Informe 1 = Subdocs. 1, 2, 3, 4, 5 y 13

**Fuente:** AA (Formulario T-22, §1832–1844).

Cita textual (AA §1844): *"De la Propuesta Técnica corresponde a los subdocumentos: 1, 2, 3, 4, 5 y 13."*

- El T-22 (Informe y presentación 1, §1836–1842) exige presentar: empresa, problema/necesidad, esquema de solución y alcance, arquitectura lógica y física, y la cartera de cinco innovaciones.
- Los subdocumentos 1–5 y 13 están detallados en AA §1530–1643.
- **Desglose del capítulo de datos (Informe 1, Cap. 6):** el T-22 asigna el Subdoc. 5 (modelo y gestión de datos) al Informe 1 (§1844). El subdoc 4 se desglosó en lógica (4.1) y física (4.2) por coherencia con §1556 que las trata como dos bloques del mismo subdocumento 4.

---

## CAPÍTULO 1 — Presentación de la Empresa (Subdoc. 1)

**Fuente base:** AA §1532–1537 (Subdocumento 1) y AA §1838 (T-22, Informe 1).

Lo que exige el Subdoc. 1:
- Reseña de trayectoria, capacidades instaladas, líneas de negocio, productos y servicios. (AA §1534)
- Estructura organizacional, dotación, certificaciones y alianzas tecnológicas. (AA §1535)
- Experiencia relevante en la industria del caso y en proyectos de complejidad equivalente. (AA §1536)
- Modelo de gobierno interno de calidad, seguridad y gestión del conocimiento. (AA §1537)

### Secciones y su fuente
| Sección plantilla | Fuente directa |
|---|---|
| Identificación y Perfil Corporativo | AA §1534 (¿qué es la empresa, líneas de negocio) |
| Filosofía Estratégica (Misión/Visión/ESG) | AA §1534 (productos y servicios, perfil); transversal/estilístico |
| Trayectoria y Casos de Éxito | AA §1536 (experiencia en la industria y complejidad equivalente) |
| Credenciales y Madurez TI | AA §1535 (certificaciones, alianzas, dotación) |
| Capacidad Instalada | AA §1534 (capacidades instaladas) |
| Estructura del Equipo y Gobernanza | AA §1537 (gobierno interno) + AA §1627 (Subdoc. 12, equipo de trabajo) |

**Nota para los casos de éxito:** deben ser pertinentes a la industria del caso (logística de consumo masivo, trazabilidad, cadena de frío). Véase también el numeral 16.2 del caso (C §788–806, materias a investigar) que sugiere el dominio técnico esperado.

---

## CAPÍTULO 2 — Problema y Necesidad (Subdoc. 2)

**Fuente base:** AA §1539–1545 (Subdocumento 2) y AA §1839 (T-22).

Lo que exige el Subdoc. 2:
- Dimensionamiento realista y con datos cuantitativos. (AA §1541)
- Comprensión del contexto de la industria: operacional, regulatorio y estacional. (AA §1542)
- Actores afectados y grupos de interés, con influencia e interés. (AA §1543)
- Supuestos declarados con fundamento; **no mezclar problema con solución**. (AA §1544)
- Información de apoyo citada en norma APA 7.ª ed. (AA §1545)

**Contenido factual del caso (todo de C):** la narrativa del problema sale íntegramente del caso.

| Concepto en plantilla | Fuente directa en C |
|---|---|
| El detonante: retiro sanitario marzo 2026 | C §66 (14.200 llamadas, 4.800 kg, $31M), C §182 (41% recepciones sin lote), C §362, C §428 |
| Cadena de frío / rechazo food service | C §250 (rechazo camión, $21M), C §335, C §338 (fiscalización ISP) |
| Modelo AS-IS (recepción, almacenamiento, preventa, rutas, preparación, transporte, devoluciones) | C §176–270 (Título II, proceso actual) |
| Prevención: 62 preventistas, Windows Mobile etc. | C §198–205 |
| Conteo cíclico 3.400 posiciones/mes, 2,3% | C §190 |
| Merma por vencimiento 1,7% | C §242 |
| Envases retornables 68.000 canastillos, 9.400 pallets, 14% | C §244, C §323 |
| OTIF 82,4% → meta sobre 95% | C §301, C §906 |
| Impacto financiero | C §333 ($31M), C §250 ($21M), C §234 (§4,2M/mes rendición) |
| Actores afectados | C §69–79 (Título III, voces de los actores) |
| Marco legal | C §788–806 (materias a investigar) y C §794 (cadena de frío); ver también TT (inconsistencias RT) |
| Supuestos | AA §1544 (exigencia) + C §861–§875 (las 16 decisiones del 16.1) |

**Los criterios de aceptación que cité (retiro <2h, 100% lote, etc.):** C Cap. 18 §897–918 (criterio 1–16).

> Aviso de inconsistencia (ver GG "Inconsistencias"): el caso cita RT-03.13 y RT-05.10 en Cap. 15, pero las Transversales los numeran distinto (RT-03.12 y RT-16.10). En la propuesta debe responder contra el código correcto del documento transversal.

---

## CAPÍTULO 3 — Esquema de Solución y Alcance (Subdoc. 3)

**Fuente base:** AA §1547–1554 (Subdocumento 3) y AA §1840 (T-22) + C Cap. 17.1 §811–835 y §931.

Lo que exige el Subdoc. 3:
- Descripción de la solución y coherencia con el problema. (AA §1549)
- Alcance de Etapa 1 y Etapa 2, con separación explícita. (AA §1550)
- Exclusiones, supuestos y restricciones. (AA §1551)
- Catálogo de requerimientos funcionales/no funcionales, priorizado y trazable. (AA §1552)
- Estrategia para apoyo de grupos de interés clave. (AA §1553)
- Criterios de aceptación del alcance. (AA §1554)

**Correspondencia con los 7 componentes de la plantilla y sus RT (C Cap. 15 y TT):**

| Componente plantilla | RT | Fuente |
|---|---|---|
| Trazabilidad lote-a-lote | RT-03.13 (caso) / correcto transversal? | C §731 (RT-03.13), C §903–904 (retiro <2h, 100% lote), TT Art. 7.1 |
| Gestión de inventario | RT-03.10 (operación desconectada) | C §191 (conteo ciclico), C §731 (RT-03.10 14h/24h) |
| Preventa móvil stock/crédito | --- | C §907 (criterio 5), C §198–205 |
| Planificación de rutas | RT-02.01 (ruta automática <20 min) | C §909 (criterio 7), C §730 (RT-02.12 replicación) |
| Control de rendición/cobro | --- | C §912 (criterio 10), C §234 (§4,2M/mes) |
| Dashboard costo de servir | RT-05.10 (analítica) | C §913 (criterio 11) |
| Gestión de envases | RT-06.01 (control de activos) | C §914 (criterio 12), C §738 (RT-06.01) |

> Ojo: la tabla `Componente → RT` de la plantilla es **de referencia** y debe validarse contra el mapeo definitivo de requerimientos (catálogo RF/RNF del Cap. 17.1, C §815–823). No inventar RT que la solución no cubre.

**Reglas de negocio (dentro del registro de requerimientos 17.1, NO capítulo aparte):** C §822 (registro de reglas de negocio) y GG (sección "Reglas de negocio"). Referencias a decisiones 16.1: C §861+.

---

## CAPÍTULO 4 — Arquitectura Lógica (Subdoc. 4.1)

**Fuente base:** AA §1556–1565 (Subdocumento 4) y AA §1841 (T-22).

Lo que exige (para la parte lógica):
- Capas, módulos, límites de contexto, responsabilidades e interfaces. (AA §1558)
- Arquitectura de integración: servicios, contratos, mensajería, versionado, gobierno. (AA §1560)
- Arquitectura de seguridad: Zero Trust, capa expuesta, identidad, cifrado. (AA §1561)
- Decisiones de arquitectura registradas, alternativas evaluadas y criterio de selección. (AA §1564)
- **Prohibido:** diagramas genéricos; debe ser propia de la solución y del caso. (AA §1565, §1841)

**Datos que debe respetar (C):** híbrido obligatorio exigido en AA Art. 16° y §1841; operación desconectada 14h/24h (C RT-03.10); 350 SKUs, 14.200 clientes, 31.000 pedidos-mes (C Tabla 14.1); técnicas de preparación/picking por oleadas y zonas (C §158? — numeral 16.2 #8).

---

## CAPÍTULO 5 — Arquitectura Física (Subdoc. 4.2)

**Fuente base:** AA §1556–1565 (Subdocumento 4), AA Art. 16° (híbrido) y AA §1841 (T-22).

Lo que exige (parte física):
- Emplazamiento de cada componente en nube y on-premise, con justificación por componente conforme al Art. 16°. (AA §1559)
- Arquitectura de despliegue: ambientes, redes, alta disponibilidad, DR, respaldos. (AA §1562)
- Dimensionamiento y plan de capacidad, con supuestos de volumen, concurrencia, crecimiento. (AA §1563)

**Datos y restricciones del caso:**
- Híbrido obligatorio: **AA Art. 16°** (y TT §4.1).
- Emplazamiento on-premise: C §738 (RT-06.01: sala técnica secundaria en CD Talca 25 m², gabinetes de borde en CD Concepción y 3 plataformas cross-docking).
- Operación desconectada: C §731 (RT-03.10: CD 24h sin enlace, dispositivos 14h).
- Ambientes: AA Art. 24° / TT RT-04.01 (5 ambientes + DR — ver GG inconsistencia #3).
- DR semestral: AA Art. 20° (prueba de DR) y TT RT-07.07 (2 veces/año).
- Despacho peak sept: C (perfil no plano, ~2.600 despachos/día, véase GG "Reglas que condicionan el diseño").

---

## CAPÍTULO 6 — Modelo y Gestión de Datos (Subdoc. 5)

**Fuente base:** AA §1567–1574 (Subdocumento 5), AA §1844 (asignación al Informe 1), y C Cap. 17.1 + datos del caso.

Lo que exige el Subdoc. 5:
- Dominio de información. (AA §1569)
- Selección del motor/paradigma de persistencia, justificado (teorema CAP). (AA §1570)
- Estrategia de migración, saneamiento, validación, conciliación. (AA §1571)
- Estrategia de desempeño: indexación, particionamiento, caché. (AA §1572)
- Separación transaccional/analítico. (AA §1573)
- Calidad de datos, retención, archivado, eliminación segura. (AA §1574)

**Datos de retención citados en plantilla:** C §734 (RT-05.10 / correcto RT-16.10 — retención: doc tributarios 6 años, trazabilidad vida útil+6 meses mín 5 años, temperatura 5 años, evidencia entrega 6 años, geolocalización 12 meses).

**Volumen de datos (C Tabla 14.1, §688–689):** ~34.000 documentos tributarios/mes, 3.400 posiciones conteo/mes, 14.200 clientes, 260.000 líneas / 2,4M unidades-mes.

**Planillas/cuadernos deben desaparecer:** C §269 (planillas y cuadernos como sistema de registro).

---

## CAPÍTULO 7 — Innovaciones (Subdoc. 13)

**Fuente base:** AA Art. 28° §469–481 (cartera de cinco innovaciones) y AA §1636–1641 (Subdoc. 13), AA Art. 29° §485+ (documentación por innovación).

Lo que exige:
- Cinco innovaciones, **una por cada tipo obligatorio**, sin repetir tipo. (AA §28.1, §475–481)
- Pertinencia al caso y trazables con arquitectura, EDT y flujo de caja. (AA §28.2)
- Cada innovación en el **Formulario T-19** con: problema concreto del caso que resuelve, tecnología que la sustenta, etc. (AA Art. 29° §487+).
- Valorización económica en el flujo de caja (AA §1864, Informe 3).

**Tipos obligatorios (AA §475–481):**
1. Producto o servicio — funcionalidad o servicio nuevo/mejorado.
2. Proceso — cambio en ejecución del proceso o en desarrollo/operación.
3. Tecnológica o de arquitectura — adopción de tecnología/patrón vigente, con APA 7.ª.
4. Modelo de negocio o de contratación — licenciamiento, pago por uso, etc., reflejado en costos.
5. Experiencia de usuario, sostenibilidad o impacto social.

> Nota GG: en innovación tipo 3 la AA §479 exige justificación con estándares y fuentes citadas en APA 7.ª — mismo requisito que el Subdoc. 2 (AA §1545).

---

## Notas transversales importantes

- **No crear capítulos extra:** registros de supuestos, reglas de negocio y matriz de trazabilidad NO son capítulos aparte del informe; viven dentro del registro de requerimientos del Cap. 17.1 (C §815–823) y se reflejan como apoyo en el Subdoc. 3 (esquema) y Subdoc. 5 (modelo de datos).
- **Cronograma de 56 meses** (AA Art. 17°): no lo toques.
- **Despliegue híbrido** (AA Art. 16°): no aceptes solo-nube ni solo-on-premise.
- **Inconsistencias documentadas** (AGENTS.md): número de instalaciones 5 vs 6; códigos RT mal mapeados (RT-03.24→03.23, RT-03.13→03.12, RT-05.10→16.10, RT-06.01 tipología); ambientes 4 vs 5; camiones vs conductores. Resolver por consulta, no unilateralmente.
