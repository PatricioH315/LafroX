# Revisión del Subdocumento 3: cumplimiento, consistencia y cambios necesarios

Fecha de revisión: 26 de septiembre de 2026.

## 1. Dictamen

**El Subdocumento 3 enviado no está correcto como entrega final. Es una consolidación parcial que debe completarse y corregirse antes de presentarla.** Tiene mejoras respecto de la versión comentada por el profesor, pero conserva vacíos sustanciales, referencias que sustituyen el desarrollo exigido y discrepancias con los documentos de apoyo.

Las conclusiones principales son:

1. **Cumplimiento insuficiente:** faltan decisiones, reglas, requisitos verificables, trazabilidad, criterios de aceptación y desarrollo concreto de implementación, implantación y operación.
2. **Consistencia parcial con partes 1 y 2:** mantiene los tres problemas, el ERP, la autonomía y gran parte del reparto funcional. Sin embargo, no cierra divergencias de instalaciones, promesa comercial, exclusiones, disponibilidad y significado de algunos códigos.
3. **Correspondencia incompleta con 4.1:** la arquitectura utiliza M1–M12, mientras el SD3 deja explícitamente sin desarrollar su correspondencia. Además, M10 incluye costo de servir en Etapa 1 en la tabla de 4.1, frente a Etapa 2 en SD3 y SD2.
4. **Sí hay referencias a documentos posteriores.** La más explícita es la sección 3.4.2, que remite a 4.1. No encontré una remisión nominal específica a «parte 4.2 y 4.3» en el texto activo del SD3; sí varias referencias generales al Subdocumento 4 que abarcan arquitectura y detalles físicos.
5. **Referenciar 4.1 no está prohibido por el profesor:** las aclaraciones exigen que 3.4 mapee al 100 % con 4.1 y utilice los mismos nombres. Lo incorrecto es obligar al lector a consultar 4.1 para entender qué se propone o usar esa referencia para dejar el SD3 vacío.
6. **Hay un riesgo formal explícito:** las notas de trabajo y la revisión humana «No documentada» coinciden con condiciones sancionadas por las aclaraciones, §7.1. La portada «VERSIÓN FINAL PARA ENTREGA» no concuerda con el contenido.
7. **El paquete ZIP también requiere limpieza:** el Excel de alcance conserva la cifra de 113 mil dólares y decisiones históricas contradictorias. No debe acompañar inadvertidamente la oferta técnica final.

Este informe identifica correcciones; no modifica ni da por aprobadas las decisiones de los subdocumentos originales. Las observaciones del profesor sobre páginas de la entrega anterior no se atribuyen automáticamente al PDF actual.

## 2. Alcance, fuentes y forma de comprobar los hallazgos

### 2.1 Documento evaluado

Se evaluó el contenido del ZIP `nuevo nuevo-20260926T040208Z-1-001.zip`, procedente de Descargas. Se tomó como versión principal el conjunto identificado por su README y confirmado en los archivos:

| Archivo | Páginas PDF | Función |
|---|---:|---|
| `LAFROX-Subdocumento3.pdf` | 17 | Cuerpo principal; capítulo desde p. 5, referencias y declaración IA al final. |
| `LAFROX-Subdocumento3-Anexos.pdf` | 46 | Anexos 3.A–3.K. |
| `LAFROX-Formulario-T-12.pdf` | 93 | Matriz RF/RNF y requisitos transversales. |

Se contrastaron los PDF con `contenido.tex`, `anexos.tex`, las tablas incluidas, `consolidado.json` y el generador. También se extrajo texto de los DOCX y se inspeccionó el contenido del Excel de alcance para detectar residuos de otras versiones. `main.pdf` tiene 25 páginas, pero el README lo identifica como anterior: **no se utilizó para suplir contenidos ausentes del PDF vigente**.

La revisión comprende lectura y búsqueda del texto de los tres PDF completos y de sus tablas activas; comprobación de identificadores, campos y referencias; y muestreo visual de portada, figuras, anexo y formulario. No equivale a una certificación visual exhaustiva de las 156 páginas.

### 2.2 Fuentes de contraste

La raíz de las fuentes externas es `C:\Users\basti\Desktop\parte4.3`.

| Clave utilizada | Fuente |
|---|---|
| Aclaraciones | `info/aclaraciones-licitacion.md`, especialmente §§1–7, 9 y 11, capítulo 3. |
| Revisión profesor | `info/Revision_informe.md`, apartados GENERAL y SUBDOCUMENTO 3; secciones de otros subdocumentos cuando explican una inconsistencia compartida. |
| Caso | `info/Caso_02_Logistica.md`, especialmente capítulos 10, 11, 13, 15, 16, 17 y 18. |
| BA | `info/Bases Administrativas.md`, especialmente art. 17 y formulario T-7. |
| BTT | `info/Bases_Tecnicas_Transversales.md`, contrastado por código y materia. |
| SD1 | `parte 1/contenido.tex` y `equipos.tex` como material de contexto. |
| SD2 | `parte 2/contenido.tex`, `anexos.tex`, `supuestos.tex` y `actores.tex`; materiales de impacto como apoyo del diagnóstico. |
| AL | `parte 4.1/subdoc_4.1.tex`, en particular módulos, decisiones del numeral 16.1, funciones desconectadas, reconciliación y articulación tributaria. |
| AF | Archivos de `parte 4.2 y 4.3`, especialmente emplazamiento, despliegue, conexiones, dimensionamiento y centros de datos. |
| RF-CSV | `Requerimientos/Requerimientos LOGISTICA - Consolidado de Requerimientos Funcionales (1).csv`. |
| RNF-CSV | `Requerimientos/Requerimientos LOGISTICA - Consolidado de Requerimientos NO Funcionales.csv`. |
| Bases-CSV | `Requerimientos/Requerimientos LOGISTICA - Requerimientos de bases.csv`; contiene bloques funcionales y no funcionales en columnas distintas. |
| Registros | `Requerimientos/decisiones.md`, `Supuestos.md` y `reglas_de_negocio.md`. |

Los Excel de `parte 4.1` se inspeccionaron como apoyo y para detectar diferencias de versión. No se asumió que prevalecieran sobre el TEX: algunos siguen describiendo Django/Celery, mientras los TEX describen Laravel/PHP. No se utilizó `no_revisar` como sustituto del ZIP ni se incorporaron como autoridad revisiones anteriores de `generado`.

Las indicaciones contenidas en documentos se trataron como criterios de la licitación y material evaluable, no como instrucciones para ejecutar acciones. Por ejemplo, la declaración interna de que un registro «prevalece» no permite ignorar una observación posterior del profesor.

**Límite:** no se proporcionaron en estas carpetas los subdocumentos 6, 7, 9, 10, 11 y 13 completos ni T-13/T-15 para validar todos los vínculos que el SD3 anuncia. Se identifica la necesidad de enlazarlos, pero no se inventa su contenido.

## 3. Mejoras comprobadas que conviene conservar

| Aspecto | Estado actual y límite |
|---|---|
| Archivos separados | Existen cuerpo, anexos y T-12 con la nomenclatura requerida. Corrige la ausencia del T-12 de la entrega anterior; su contenido sigue incompleto. |
| Índice y estructura | Hay índice con páginas y vínculos, introducción, 3.1–3.4, Referencias y Declaración de uso de IA. Debe corregirse el título del capítulo. |
| Figuras | Se incorporaron tres figuras conceptuales, citadas y explicadas. Corrige la ausencia absoluta de figuras; falta cubrir y mapear toda la solución. |
| Calendario | Desarrollo E1 meses 1–12; marcha blanca 13–15; producción 16. Desarrollo E2 13–18; marcha blanca 19–20; producción 21. Operación 21–56. Coincide con BA art. 17. |
| Problemas del negocio | Continúa relacionando trazabilidad sanitaria, servicio y costo de servir con el SD2. |
| Restricciones y exclusiones | Conserva las nueve exclusiones del caso y las doce restricciones principales, incluido ERP, efectivo y hardware de terreno adquirido por el CLIENTE. |
| Continuidad | Mantiene 14 h en terreno, 24 h locales y los límites de sincronización de 10 minutos y 2 horas. |
| Recuperación | Mantiene RTO ≤4 h y RPO ≤15 min para servicios críticos y ensayos semestrales. Coincide con SD1 y el objetivo general de AL/AF, sujeto a los escenarios indicados más adelante. |
| Identificadores RT | El T-12 contiene los mismos 374 códigos RT de la BTT suministrada: no faltan ni sobran códigos en esa comparación. Esto no demuestra cumplimiento ni incorporación de los parámetros particulares. |
| Reconocimiento de incertidumbre | No inventa aprobaciones o pruebas ejecutadas. Debe transformar la incertidumbre en supuestos de oferta y decisiones fundamentadas, no dejar campos vacíos. |

## 4. Correcciones prioritarias del cuerpo principal

### H01. Notas de trabajo y declaración de revisión humana sin completar

**Prioridad: crítica.** Localización: SD3 pp. 5–17; notas adicionales en anexos y T-12; `contenido.tex` y tablas de declaración IA.

El PDF contiene 16 apariciones de «Nota de trabajo»; anexos, 20; T-12, 4. La declaración del cuerpo marca nivel Alto y «No documentada» en revisión humana para las secciones y anexos. Las aclaraciones §7.1.d incluyen marcadores e instrucciones de revisión entre los indicios sancionables; §7.1 exige elaboración y revisión humana, y §7.2 exige quién revisó y qué verificó. Desde Informe 2 se contempla considerar no presentado el subdocumento ante esos indicios.

**Modificar:** resolver materialmente cada nota y redactar el resultado como propuesta. Documentar la revisión humana efectiva, su responsable y lo verificado; consolidar con A-6. **No basta borrar las notas, cambiar «Alto» a «Bajo» o escribir un nombre sin revisión real.** Mantener las observaciones de trabajo en una bitácora separada de la entrega.

El requisito del caso §17.1 es proponer decisiones por el CLIENTE con fundamento, impacto e instancia de validación. No exige que toda decisión de oferta ya esté aprobada por el CLIENTE. Por eso «no está aprobado» no justifica dejar 16 materias sin resolver.

### H02. Título obligatorio distinto y desarrollo demasiado breve

**Prioridad: alta.** Localización: `contenido.tex:2`, índice y p. 5.

El capítulo se llama «Esquema de solución y alcance». Las aclaraciones §11 fijan **«Introducción al Alcance de la Solución»** como título del capítulo 3, diferenciándolo de la denominación del subdocumento en T-7.

**Modificar:** usar el título obligatorio en capítulo e índice. Conservar «Esquema de solución y alcance» como denominación descriptiva del subdocumento cuando corresponda. Los títulos 3.1, 3.2, 3.3 y 3.4 sí coinciden. No crear secciones 3.5, 3.6, etc.; implementación, implantación y operación pueden seguir como niveles inferiores de 3.4.

La Revisión profesor espera **25–35 páginas de análisis**. El PDF vigente tiene 17 páginas totales y el capítulo comienza en p. 5; el contenido 3.1–3.4 ocupa aproximadamente pp. 5–15. **Agregar desarrollo ingenieril**, no páginas de tablas o espacios para alcanzar una cantidad artificial.

### H03. Catálogo y T-12 sin alcance comprometido completo

**Prioridad: crítica.** Localización: §3.2.3, anexos 3.A/3.B y T-12.

| Medida del registro activo | Resultado comprobado |
|---|---:|
| RF conservados | 174 |
| RF con descripción, actor, precondición, resultado, prioridad y origen | 31 |
| RF sin descripción desarrollada | 143 |
| RF con etapa asignada | 30 |
| RF desarrollados sin etapa | 1: RF-11.03 |
| RNF conservados | 90 |
| RNF con contenido en «umbral» | 13 |
| RNF sin umbral desarrollado | 77 |
| RNF con método de verificación | 0 |
| Filas de la parte A de T-12 | 264 |
| Códigos de la parte B de T-12 | 374 |

Las columnas de cumplimiento y trazabilidad del T-12 están vacías sistemáticamente. El generador construye explícitamente esas celdas vacías. Las 31 descripciones representan 17,8 % de los RF y los 13 umbrales, 14,4 % de los RNF; **no son porcentajes de cumplimiento**, porque incluso esos registros necesitan revisión.

**Agregar/modificar:** consolidar un único catálogo, completar campos del Caso §17.1, asignar etapa y fundamento, y enlazar origen → RF/RNF → componente → paquete EDT → prueba prevista → criterio de aceptación. Resolver también aplicabilidad y respuesta a RT. El T-12 debe expresar cómo la oferta satisface la exigencia y dónde se fundamenta; no necesita fingir resultados de pruebas de un sistema aún no construido.

No rellenar «Cumple» automáticamente. Tampoco confundir ausencia de test ejecutado con imposibilidad de declarar una solución ofertada y su prueba de aceptación prevista.

### H04. No existe el mapeo exigido con la arquitectura lógica

**Prioridad: crítica.** Localización: §3.4.2, p. 13, `contenido.tex:184–188`; figuras de §3.3.

3.4.2 reconoce que la correspondencia está sin desarrollar y que no se consideran aprobados M1–M12 ni las ocho capas. AL, en cambio, define esos módulos y declara derivarlos de 3.3/3.4. Hay una dependencia circular: AL da por definido un alcance que SD3 aún no concreta.

**Agregar:** un esquema comprensible del conjunto, nombres consistentes y mapeo por capacidad/requisito. El cuerpo debe explicar recepción, inventario, preventa, rutas, preparación, reparto, rendición, devoluciones/envases, calidad, analítica, canal moderno y flota; además, las capacidades transversales que las hacen operables. Las figuras actuales no muestran suficientemente portales, EDI, envases, devolución, identidad ni la responsabilidad por las decisiones.

No se exige convertir el capítulo 3 en una copia de servidores o productos del capítulo 4. Sí se exige que el lector entienda la solución completa y pueda seguir sus componentes.

### H05. Etapas: costo de servir, OTIF, apoyo a transportistas y portal

**Prioridad: alta.** Localización: §3.2.1, Tabla 3.2; RF-11.02/RF-11.03; AL tabla `tab:modulos-funcionales`, línea 371.

El SD3 y SD2 asignan costo de servir a E2. AL coloca «M10 Analítica / RF-11» con «OTIF y costo de servir» en E1. SD3 deja RF-11.03 sin etapa y RF-11.04 sin desarrollar.

**Modificar:** establecer entregas incrementales del módulo: medición necesaria para marcha blanca y control diario en E1; costo de servir en E2 si se conserva ese alcance. Explicitarlo en SD3 y trasladar la misma separación a AL/T-12. No mover toda la analítica a una etapa solo por compartir módulo.

También debe distinguirse el portal de clientes de E2 del mecanismo de alta/asignación de conductores externos necesario para reparto E1. D5 y AL utilizan portal de transportistas antes del despacho: precisar qué funciones deben existir desde E1 y cuáles corresponden al canal moderno de E2.

### H06. Reparto entre etapas sin arbitraje completo de prioridades e hitos

**Prioridad: alta.** Localización: §§3.1.2 y 3.2.1; V-13/V-14/V-15; Caso §§13.1–13.3 y 17.3.

Se explica que rutas debe mantenerse en E1 por la jubilación y se conservan talleres en meses 1–3. Es un avance, pero falta enfrentar expresamente la preferencia del comité —trazabilidad/frío, después preventa/evidencia y al final rutas/costo— con la objeción de Amparo Ossa. Falta justificar la capacidad de absorción y las entregas intermedias.

**Agregar:** decisión razonada de priorización, dependencia por capacidad, hitos de septiembre de 2026, condiciones de enero de 2029 y expansión eventual a Los Lagos en 2030; relación con meses 16/21 y congelamientos. Enero de 2029 exige también aviso anticipado, ventana de 30 minutos y POD, no solo EDI.

**Corregir V-14:** afirma que septiembre de 2026 es «antes del inicio del contrato», mientras V-13 dice que el inicio no está consolidado. Eliminar esa conclusión incondicional o respaldarla con la fecha contractual. Si el hito precede al contrato, explicar su tratamiento sin prometer cumplirlo retroactivamente ni alterar art. 17.

### H07. Implementación reducida a capacidades corporativas

**Prioridad: alta.** Localización: §3.4.3, p. 13, `contenido.tex:190–194`.

Nombrar funciones de SD1 y remitir a SD6/7/9 no desarrolla la implementación solicitada por T-7 y Revisión profesor.

**Agregar:** enfoque de construcción de E1/E2, frentes simultáneos, iteraciones y entregables; ingeniería de requisitos; repositorios y control de configuración; ramas/versiones; secuencia de integración y entrega; ambientes; pruebas y puertas de calidad; vínculo requisito–cambio–prueba–versión. Explicar quién acepta cada incremento y cómo los cambios de E2 preservan E1.

AL y AF contienen prácticas de artefacto único, perfiles y promoción, pero necesitan una síntesis aplicada al alcance dentro de SD3. No trasladar nombres de tecnologías desde Excel históricos sin reconciliarlos con los TEX.

### H08. Implantación todavía sin plan ejecutable

**Prioridad: alta.** Localización: §3.4.4, p. 14; Caso §17.6.

El texto enuncia convivencia, reversión, noche y capacitación, pero no define primera ola, sitio/zona piloto, dotación, duración ni umbrales.

**Agregar:** primer proceso/sitio/zona; orden de las olas; migración y conciliación; convivencia explícita con hoja de picking y guía de papel; dueño único de cada registro; condiciones para retirar el legado; preparación y verificación de la reversión; tiempo máximo sustentado, disparador, responsable y tratamiento de transacciones pendientes; acompañamiento nocturno y en ruta; incorporación por empresa transportista; medición de adopción y contingencia ante rechazo.

Conservar la ventana 05:30–07:00 y los congelamientos. Incorporar las seis condiciones de cierre de BA art. 17.3: sin incidentes críticos/altos, volumen real por cuatro semanas, indicadores sostenidos, conciliación sin diferencias no explicadas, capacitación/certificación y acta de aceptación. No sustituirlas únicamente por una meta OTIF.

### H09. Operación sin compromisos específicos y horario omitido

**Prioridad: alta.** Localización: §3.4.5, p. 14; RNF-21.xx; T-12 parte B.

Falta disponibilidad por servicio, SLI/SLO, alertamiento, observabilidad, automatización, procedimientos, escalamiento, capacidad y soporte durante meses 16–20. SD1 demuestra antecedentes corporativos, pero sus tickets y personal no constituyen dotación automáticamente disponible para Puelche.

**Agregar:** servicio concreto para Puelche, responsabilidades de LafroX y del equipo de cuatro personas, horarios, escalamiento, capacidad justificada y operación de los 36 meses. El Caso cap. 15 exige **04:00–22:00 de lunes a sábado**, cobertura **24×7 en septiembre y diciembre** y ante incidentes críticos en la ventana de despacho.

El material `Requerimientos` mantiene 08:00–20:00 en D33, S-28 y RNF-21.04. No copiarlo. La BTT trata el horario en **RT-21.07**, mientras el caso lo rotula **RT-21.06**; el RT-21.06 transversal corresponde a métricas de atención. Registrar la equivalencia por materia y conservar la exigencia particular más concreta del caso.

AF propone una mesa de siete personas, pero SD3 debe justificar su suficiencia por turnos y cargas; no declarar «Erlang C realizado» solo por citar ese apartado. También debe contemplar consultas del cliente tradicional sin obligarlo a usar autoatención digital.

### H10. Criterios de aceptación sin metas, momento ni método

**Prioridad: alta.** Localización: §3.2.5, pp. 10–11; Anexo 3.J, pp. 42–43.

Se conservaron los 16 resultados y situaciones actuales, pero todas las columnas de meta propia y momento/método están vacías. La Revisión profesor había valorado esos campos en la entrega anterior; esta versión los pierde en lugar de corregirlos.

**Agregar:** compromiso medible por criterio, etapa/hito, condiciones del ensayo, datos, fórmula, evidencia y responsable de aceptación. Definir metas propias para OTIF, pérdida de envases y ocupación; no confundir «cero diferencias sin explicar» con «ninguna diferencia monetaria admisible». El criterio 16 necesita una prueba de operación por un reemplazo sin dependencia del planificador.

### H11. Estrategia de interesados sin acciones verificables

**Prioridad: alta.** Localización: §3.4.6, pp. 14–15; Anexo 3.I, pp. 40–41.

Se mantienen 19 actores, pero momento, responsable e indicador están vacíos. El anexo enumera roles, no los actores nominales pese a llamarlos «nominales» en el cuerpo. El comité ejecutivo no queda identificado explícitamente como instancia y los peonetas solo podrían entenderse dentro de «Tripulación propia».

**Modificar/agregar:** conservar vínculo con los actores de SD2, declarar inclusión de peonetas y comité, y convertir cada participación en acción, momento, responsable, medida de adopción y respuesta ante resistencia. Diferenciar conductores propios, externos, transportistas, preparadores nuevos y antiguos. Tratar al planificador como actor crítico de transferencia, no como mero destinatario de información.

### H12. Reglas y decisiones existentes sustituidas por espacios vacíos

**Prioridad: crítica.** Localización: anexos 3.C, 3.F y 3.G.

El anexo 3.C tiene 25 registros, solo tres con contenido parcial: S-06, S-14 y S-16. De las primeras 16 materias, 13 carecen de contenido adoptado. 3.F contiene diez materias D-01–D-10, todas con decisión y fundamento vacíos. 3.G conserva las 16 RNG sin desarrollo operacional.

`Requerimientos` contiene 46 supuestos y 40 decisiones desarrolladas; el Excel histórico del ZIP contiene 60 decisiones. **No son tres catálogos equivalentes ni deben mezclarse por número.** Ejemplo: S-04 es asignación de inventario en `Supuestos.md`, pero excursión térmica en el ZIP; S-14 es conectividad de terreno en la fuente, pero WMS en el ZIP. D1 de la fuente es entrega cumplida; D-01 del anexo es reparto de etapas.

**Modificar:** definir identificadores canónicos o correspondencia explícita fuente/versión/ID → ID final. Recuperar las decisiones válidas, corregir las conflictivas y documentar fundamento, alternativas, impacto si el supuesto falla, responsable y validación. No es obligatorio conservar 46 o 60 filas si hay duplicados, pero sí demostrar que ninguna obligación desapareció.

## 5. Consistencia con documentos anteriores y posteriores

### 5.1 Matriz de contraste concreto

| Tema | Evidencia comparada | Dictamen y cambio en SD3 |
|---|---|---|
| Tres problemas | SD3 §3.1; SD2 §§2.1/2.2. | Coherente. Mantener la relación problema–capacidad–resultado. |
| Experiencia corporativa | SD1 §1.1 declara NOC/mesa 24×7 y RTO/RPO; SD3 distingue antecedente y compromiso. | Distinción correcta. Completar dotación propia del proyecto y operación. |
| Número de instalaciones | SD2 `anexos.tex`, RF-02 y `supuestos.tex` n.º5 hablan de 14 CD; SD3 V-01 lo objeta; AF `02_a_emplazamiento.tex:25` trabaja seis instalaciones y cinco con cómputo, incluyendo casa matriz sin cómputo. | La discrepancia existe. SD3 debe fijar padrón de alcance trazable y validar la interpretación de AF; no mantener «14 CD» como base. Es una discrepancia del conjunto, no prueba de que SD3 deba adoptar el error de SD2. |
| ERP y WMS | SD2 declara ERP conservado y reemplazo progresivo WMS; AL reemplaza M1/M2/M5 en E1. | Coherencia general, pero SD3 debe precisar alcance y transición por etapa. La suposición SD2 de lectura/escritura directa de tablas contrasta con AL, que prohíbe escrituras directas: fijar integración y responsabilidad sin prometer interfaces no acreditadas. |
| Marcas del legado | SD2 menciona SAP Business One/Manhattan; SD3 no las adopta como comprobadas. | No convertir marcas de SD2 en hecho del caso sin evidencia. Registrar información faltante y efecto en integración/migración. |
| Promesa comercial | SD2 `actores.tex` propone 24 h urbana/48 h rural y corte 14:00; SD3 S-21/V-19 la dejan abierta. | No está cerrada la coherencia. Decidir por zona/canal, definir corte, capacidad y excepciones; no imponer 30 minutos a todos los clientes por la exigencia de una cadena. |
| Asignación de etapas | SD3 Tabla 3.2/RF-11.02 E2; AL M10 con OTIF y costo E1. | Inconsistencia explícita de la tabla AL. Definir entregas de M10 y actualizar la traza común. |
| Excursión térmica | D4/RNG-04 asignan disposición al conductor y niegan bloqueo automático; AL líneas 115/187/819 exige bloqueo local y liberación por Calidad; SD3 deja S-04/RNG-04 vacíos. | La contradicción está en las fuentes y SD3 no la arbitra. Proponer en SD3 una regla coherente con la observación del profesor: conductor registra, Calidad decide disposición; precisar bloqueo preventivo, parámetros, evidencia y contingencia sin conexión. |
| Código RF-09.07 | D4/RNG-04 lo interpretan como facultad de bloquear/liberar; RF-CSV registro 89 lo define como registro de rechazo por sospecha de ruptura de frío; ZIP conserva ese título. | No reutilizar RF-09.07 para otra función. Crear/desarrollar el requerimiento de bloqueo/liberación con ID no ambiguo y enlazarlo a RNG-04/AL. |
| Precio | D9/RNG-08 proponen precio al despacho con excepción; AL líneas 822/884 conserva tarifa informada y revalidación; SD3 S-09/RNG-08 vacíos. | Resolver política única, momento de vigencia, consentimiento/excepción y evidencia. Aclarar si revalidar antes de confirmar también cubre cambios posteriores hasta despacho. |
| Códigos de precio | RF-CSV RF-03.11 es excepción; RF-03.12 es alerta; RF-03.13 es ventana. D9/RNG-08 los citan como precio por defecto, excepción y alerta. | Mapeo obsoleto en registros. Actualizar referencias por significado, no copiar números. RF-03.12 además se autorreferencia como excepción en su descripción. |
| Stock desconectado | SD3 habla de sincronización sin duplicar; D8/RNG-01 usan orden de confirmación y RNG-02/S-04 orden de captura; AL confirma centralmente y no acepta «última marca de tiempo». | Fijar una regla determinista para pedido capturado, confirmado, reserva firme y rechazo. No prometer reserva firme desde una foto de stock offline. |
| Desconexión | SD3 14 h móvil/24 h local; AL/AF mantienen esas autonomías. | Coherencia básica. Completar funciones disponibles/no disponibles y excepciones; RT-03.13 exige declaración explícita. |
| Autoatención sin conexión | Caso cap. 15, fila RT-17.01 incluye autoatención entre perfiles desconectados; AL tabla offline y AF conexiones declaran portal sin alternativa offline. | Brecha o ambigüedad que SD3 debe tratar expresamente: distinguir portal web y perfil móvil/atención asistida y justificar la cobertura. No cerrar T-12 omitiendo la particularidad del caso. |
| Documento previo al despacho | SD3 dice que el CD despacha sin enlace y el ERP emite DTE; AL líneas 798/841 bloquea nueva guía si ERP/canal no confirma. | Falta explicar cómo la continuidad de despacho se sostiene con documentos preemitidos o contingencia autorizada. Capturar POD offline no resuelve emisión previa. No asumir autorizado un mecanismo tributario todavía no definido. |
| RTO/RPO | SD3 compromete ≤4 h/≤15 min; AF despliegue línea 160 condiciona RPO remoto a existencia de WAN. | Objetivo general coincidente; falta cobertura del escenario corte WAN + pérdida local. Explicitar escenarios y medidas; no debilitar silenciosamente el requisito contractual. |
| Disponibilidad | SD2 RNF-DISP fija 99,5 % citando experiencia de art.34; AF clasifica 99,9/99,5/99,0/98,0 % por servicio; SD3 no compromete disponibilidad. | Incorporar niveles por servicio con fundamento contractual. El SLA histórico de SD1 no acredita el SLA del proyecto. |
| Apoyo al cliente tradicional | SD3 preserva cliente sin dispositivo; AF dimensionamiento línea 157 excluye al tradicional de mesa porque «se atienden por autoatención». | No asumir autoatención digital como única solución. Definir canal humano o asistido e incluir su carga cuando corresponda. |
| Hardware de terreno | SD3 EX-09 mantiene compra por CLIENTE; SD2 E-02 habla de «provisión exclusiva de sensores...». | Aclarar quién especifica, compra, configura y mantiene por categoría; armonizar lenguaje sin trasladar montos a SD3. |
| Frío a −22 °C | SD3/SD2/AL conservan operación de bodega sin señal. | Coherente como restricción. Completar verificación de uso con guantes, lectura/confirmación y autonomía, sin afirmar validación de un modelo físico no ensayado. |
| Rotación | SD3 atribuye 38 % a preparación; Caso lo confirma. | Mantener. Aclarar que terceros también rotan, pero sin transferirles ese porcentaje. |
| Excel de arquitectura | `arquitectura_fisica_ADR.xlsx`, hoja «Índice de decisiones», fila 4: Django/Python; AL/AF: Laravel/PHP. | No hay base para copiar ambos stacks. Fijar versión técnica común antes de llenar SD3/T-12. La corrección corresponde al conjunto documental, con efecto directo en la trazabilidad del SD3. |

### 5.2 Mapeo orientador que falta documentar

La siguiente correspondencia se infiere de las responsabilidades de AL y AF; es una **guía para completar el SD3**, no una declaración de cobertura probada de cada RF.

| Capacidad que debe explicar SD3 | Nombre utilizado en AL | Referencia física de contraste |
|---|---|---|
| Recepción de productos y lotes | M1 Recepción | A-01/A-02, C-03/C-05. |
| Inventario, reservas, FEFO | M2 Inventario | A-01/A-02; N-04/N-05 para consolidado. |
| Toma del pedido con y sin conexión | M3 Preventa | C-01; N-04/N-05/N-07. |
| Planificación y corrección de ruta | M4 Rutas | N-04/N-05 y motor de optimización. |
| Picking, carga y despacho | M5 Preparación | A-01/A-02; C-03/C-04. |
| Entrega, POD y cobro capturado | M6 Reparto | C-02; N-04/N-05 y almacenamiento de evidencia. |
| Cuadratura y explicación de diferencias | M7 Rendición | C-02/N-04; A-04 hacia ERP. |
| Retornos y cuentas de envases | M8 Devoluciones | C-02/N-04/A-01. |
| Lote, registro térmico y disposición | M9 Calidad | B-01/B-02/B-03; N-06/N-08. |
| Indicadores y costo por entrega | M10 Analítica | N-10; separar compromisos E1/E2. |
| Intercambio con cadenas | M11 Canal moderno | N-04/A-04; distinguir los portales por actor. |
| Posición, recorrido y desvíos | M12 Flota | N-04/N-06 e interfaz de telemetría. |

El glosario y el T-12 deben distinguir `SD2:RF-01` de `SD3:RF-01.xx`: el primero es preventa resumida y el segundo recepción detallada. Lo mismo vale para códigos D-xx que en AF identifican componentes físicos, no decisiones del SD3.

## 6. Inventario de referencias a documentos posteriores

Se consignan incluso cuando están en una nota, porque aparecen en el entregable.

| Ubicación en archivo activo | Referencia encontrada | Evaluación y acción |
|---|---|---|
| `contenido.tex:23`, §3.1.1 | Revisar arquitectura del Subdocumento 4 para fijar detalle y correspondencia. | Remisión general a SD4. Reemplazar la nota por alcance concreto y enlace trazable. |
| `contenido.tex:79`, §3.2.3 | Traza a arquitectura, EDT y pruebas vacía hasta revisar SD4, SD7 y T-13. | No satisface trazabilidad. Completarla; mantener referencia al documento que realmente respalda cada vínculo. |
| `contenido.tex:170`, §3.3.3 | Revisar SD4 para servidores, enlaces, bases locales, protocolos y conflictos. | Alude también a aspectos físicos. El detalle físico puede quedar en SD4; la conducta de negocio y continuidad deben resolverse en SD3. |
| `contenido.tex:188`, §3.4.2 | «sección 4.1 del Subdocumento 4», nombres, M1–M12, ocho capas. | **Referencia directa a 4.1.** Es pertinente por las aclaraciones; el problema es que la correspondencia está sin desarrollar. |
| `LAFROX-Formulario-T-12.tex:10` | No se considera probada correspondencia con SD4, SD7 y T-13. | Declaración de matriz incompleta. Resolver antes de entregar. |
| `tablas/t12_caso.tex:271` | Revisar arquitectura SD4, EDT SD7 y pruebas T-13. | Igual problema; genera columnas vacías de forma deliberada. |
| `tablas/anx_vacios.tex:25`, V-20 | Arquitectura, EDT, pruebas e innovaciones de documentos no revisados. | Es una tarea de revisión interna, no un vacío del CLIENTE. Retirar de consultas externas cuando se complete. |
| `contenido.tex:59`, §3.2.1 | Revisar SD13 por innovaciones. | Debe incorporar su impacto real en el alcance; no solo anunciar revisión. SD13 no fue proporcionado para este contraste. |
| `contenido.tex:194`, §3.4.3 | Revisar SD6, SD7 y SD9. | Referencia coherente para detalle, insuficiente como implementación del SD3. |
| `contenido.tex:202`, §3.4.4 | Revisar SD7 para olas, dotación y reversión. | Completar síntesis autónoma y luego enlazar el plan. |
| `contenido.tex:210`, §3.4.5 | Revisar SD10 y SD11 para operación. | Completar compromisos y servicio en SD3; no atribuir contenido a documentos no disponibles. |

**Respuesta a la advertencia del usuario:** sí se está remitiendo a 4.1 y a SD4 en general. No sería correcto eliminar toda correspondencia para evitar «referencias posteriores», porque contradice Aclaraciones §11, 3.4 y 4.1. La solución es que SD3 sea autosuficiente como explicación de alcance y use la arquitectura para demostrar consistencia.

## 7. Revisión de cada sección y anexo

| Parte actual | Estado | Relación documental y cambio necesario |
|---|---|---|
| Introducción | Parcial | Relaciona SD1/SD2, anexos y T-12. Corregir título y sustituir la nota inicial por un alcance terminado. |
| 3.1.1 Capacidades | Parcial | Coherente con SD2 en grandes procesos. Añadir la cobertura omitida del catálogo y nombres comunes con AL. |
| 3.1.2 Implementación, implantación y operación | Parcial | Calendario BA correcto. Añadir hitos externos, responsabilidades 16–20, convivencia y alcance real de cada fase. |
| 3.2.1 Etapas y dependencias | Parcial | Conserva RF resumidos de SD2. Corregir M10/OTIF, diferenciar portales y fundamentar arbitraje frente al comité. |
| 3.2.2 Exclusiones, restricciones y supuestos | Parcial | Conserva límites del Caso; falta recuperar decisiones y armonizar exclusiones distintas de SD2. |
| 3.2.3 Catálogo y correspondencia | Insuficiente | 143 RF y 77 RNF sin desarrollar; RF-05 y RF-09 resumidos de SD2 sin mapeo. Completar T-12 y resolver códigos de fuentes. |
| 3.2.4 Reglas y discrepancias | Insuficiente | Enumera problemas reales, pero no decide reglas. Cerrar arbitrajes y separar consultas al CLIENTE de tareas propias. |
| 3.2.5 Aceptación | Insuficiente | Vincula problemas a tres resultados y remite a 16. Faltan compromisos medibles, momento y método de todos. |
| 3.3.1 Ciclo logístico | Parcial | Flujo comprensible y explicado. Añadir capacidades restantes, interfaces, responsabilidades y relación E1/E2. |
| 3.3.2 Trazabilidad y frío | Parcial | Lote/temperatura coherentes con caso. Incorporar eventos de rechazo, bloqueo, disposición y responsable; alinear AL y RNG-04. |
| 3.3.3 Continuidad e integración | Parcial | Límites de autonomía/sincronización correctos. Explicar funciones no disponibles, stock, identidad, DTE y reconciliación. |
| 3.4.1 Jornada operacional | Parcial | Relación visible con SD2. Completar excepciones y canales de E2; evitar describir únicamente el flujo exitoso. |
| 3.4.2 Correspondencia lógica | Sin desarrollar | Completar mapeo obligatorio con 4.1; usar nombres canónicos sin reproducir todo el despliegue físico. |
| 3.4.3 Implementación | Insuficiente | SD1 aporta capacidad corporativa. Desarrollar construcción, configuración, integración/entrega y calidad aplicadas. |
| 3.4.4 Implantación | Insuficiente | Enuncia condiciones del Caso. Definir olas, convivencia, migración, acompañamiento y reversión. |
| 3.4.5 Operación | Insuficiente | RTO/RPO coherentes como objetivo. Añadir horarios, servicio, métricas, procedimientos y dotación justificada. |
| 3.4.6 Grupos de interés | Insuficiente | Mantiene roles de SD2. Añadir acciones, responsables, momentos y medidas de apoyo/adopción. |
| Referencias | Parcial | Están al final, antes de IA. Añadir localizadores/páginas de las Bases según §6 de Aclaraciones; corregir título y autoría de fuentes y ambigüedad 2026a/b/c en anexos. |
| Declaración IA | Incompleta | Estructura con filas por sección/anexo/T-12. Falta revisión humana real y correspondencia con A-6. Resolver formato horizontal del cuerpo. |
| 3.A RF, pp. 6–19 | Insuficiente | Completar cada RF y mapa SD2→SD3. Diferenciar RF-02.08 de RF-05.05 y RF-07.02 de RF-07.03, hoy con descripciones idénticas por pares. |
| 3.B RNF, pp. 20–26 | Insuficiente | Ningún método. No todos los 13 «umbrales» son numéricos: RNF-01.03, RNF-22.03 y RNF-23.01 son condiciones/obligaciones generales. Precisar prueba y clasificar coherentemente. |
| 3.C Supuestos, pp. 27–30 | Insuficiente | Resolver 16 materias obligatorias; 25 registros no equivalen a los 46 de la fuente. Crear correspondencia y completar fundamento, impacto y validación. |
| 3.D Exclusiones, p. 31 | Mayormente correcto | Nueve exclusiones explícitas bien preservadas; EX-10/EX-11 vacías deben justificarse, retirarse de entrega o documentarse como bajas en bitácora. |
| 3.E Restricciones, pp. 32–33 | Mayormente correcto | Doce restricciones del Caso preservadas; R-13–R-22 vacías. No reinsertar trámites licitatorios como alcance técnico. |
| 3.F Decisiones, p. 34 | Sin desarrollar | Diez filas vacías. Recuperar y racionalizar decisiones con equivalencias; no renumerar silenciosamente D1–D40. |
| 3.G Reglas, pp. 35–36 | Sin desarrollar | Las 16 materias necesitan conducta, punto, actor, consecuencia, excepciones y RF/RNF. Recuperar contenido solo después de corregir contradicciones. |
| 3.H Vacíos, pp. 37–39 | Parcial | Añadir estado, resolución o supuesto de oferta y efecto. V-14 necesita corregir inferencia de fecha; V-20 no es consulta al CLIENTE. |
| 3.I Actores, pp. 40–41 | Insuficiente | 19 actores sin momento/responsable/indicador. Completar participación operacional y denominaciones. |
| 3.J Aceptación, pp. 42–43 | Insuficiente | 16 resultados conservados, sin meta propia ni medición/hito. Desarrollar tabla de aceptación. |
| 3.K Glosario, p. 44 | Parcial | Añadir siglas/códigos realmente usados: BA/BTT/SD, EDT, R18, RNG, S/D/V/EX y equivalencias entre documentos; definir GTIN/GS1 y otras si se incorporan. |
| T-12 A | Insuficiente | Están RF/RNF, pero cumplimiento, componente, EDT, prueba, sección y criterio vacíos. Completar vínculo requisito por requisito. |
| T-12 B | Parcial en inventario, insuficiente en respuesta | 374 códigos presentes. Añadir parámetro del Caso, aplicabilidad, respuesta y evidencia de diseño. Resolver correspondencias por materia donde los códigos difieren. |

## 8. Qué recuperar del catálogo y qué corregir antes de recuperarlo

### 8.1 Los conteos no significan que todos los requisitos estén cubiertos

La unión por identificador de los tres CSV contiene **163 RF únicos y 79 RNF únicos**. Todos esos identificadores aparecen en el inventario del ZIP. El ZIP agrega 11 RF y 11 RNF respecto de esa unión. Sin embargo, hay colisiones de significado y descripciones recortadas: la presencia de un código no acredita cobertura funcional.

Los 11 RF adicionales son RF-06.06, RF-07.01, RF-09.10, RF-10.01–RF-10.03 y RF-19.01–RF-19.05. Los RNF adicionales son RNF-03.01–RNF-03.03, RNF-06.02–RNF-06.03, RNF-09.05, RNF-11.03–RNF-11.04, RNF-12.03 y RNF-14.11–RNF-14.12. **No se deben eliminar por ser adicionales:** algunos descomponen exigencias reales o resuelven colisiones. Deben mostrar su origen y decisión de incorporación.

### 8.2 Colisiones que deben quedar resueltas en la trazabilidad

| Código | Significado en RF-CSV | Significado en Bases-CSV | Tratamiento necesario |
|---|---|---|---|
| RF-14.01 | Telemetría de camiones propios | Clasificación de información | El ZIP usa RF-19.01 para la segunda materia; documentar equivalencia. |
| RF-14.02 | Rutas planificadas vs. reales | Matriz de controles de seguridad | Documentar equivalencia a RF-19.02. |
| RF-14.03 | Desviación de ruta | Superficie de exposición | Documentar equivalencia a RF-19.03. |
| RF-14.04 | Telemetría con costo de servir | Respuesta a incidentes de seguridad | Documentar equivalencia a RF-19.04. |
| RF-14.05 | Vinculación conductor–camión | Notificación de brecha | Documentar equivalencia a RF-19.05. |

También hay duplicados de filas RF-13.04, RF-17.09, RF-17.11 y RNF-13.03 en Bases-CSV. Consolidar su contenido y conservar el origen, sin contarlos dos veces. La correspondencia del Anexo 3.A actualmente solo explica RF resumidos de SD2; no documenta esta transformación.

### 8.3 Descripciones desarrolladas que se debilitaron

| Registro | Diferencia comprobada | Modificación necesaria |
|---|---|---|
| RF-01.02 | La fuente exige campo estructurado y bloqueo si no hay lote; ZIP dice registrar lote. | Definir entrada, obligatoriedad, excepción y bloqueo, sin permitir recepción trazable incompleta. |
| RF-01.06 | La fuente especifica AIs GS1 y alternativa manual; ZIP resume «capturar código». | Precisar GTIN/lote/vencimiento/SSCC, validación y manejo de código inválido. |
| RF-02.08 / RF-05.05 | ZIP repite exactamente asignación FEFO; la descripción de RF-02.08 en CSV también mezcla picking con su título FEFO. | Arbitrar responsabilidades, quitar duplicidad semántica y preservar captura de misión/confirmación/faltante. |
| RF-06.12 | CSV vincula evidencia de recepción del cliente a guía; ZIP dice «recepción de mercadería», ambiguo con recepción en bodega. | Nombrar receptor/entrega, evidencia y relación con GDE, sin equiparar automáticamente fotografía y acuse. |
| RF-07.02 / RF-07.03 | ZIP usa la misma frase de conciliación para ambos. | Separar planilla/cuadratura de registro de causas y bloqueo de cierre. |
| RF-09.05 | Fuente fija 2 °C/15 min, otras fuentes los hacen parametrizables; ZIP solo dice alertar. | Definir umbral por producto, quién lo valida, latencia, destinatario y relación con bloqueo. No tratar el valor histórico como regla universal sin fundamento. |
| RF-11.03 | ZIP elimina definición detallada, periodicidad diaria y etapa. | Recuperar fórmula OTIF, ventana, población, causales, periodicidad y etapa de disponibilidad. |
| RF-12.09 | ZIP no explicita carácter anticipado, guía y ETA. | Precisar emisión de ASN antes de llegada, evento disparador, contenido y aceptación de la cadena. |
| RF-12.14 | Fuente: portal público sin autenticación, sin precios ni stock; ZIP solo catálogo en línea. | Recuperar públicos, límites de exposición y datos permitidos. |
| RF-12.17 | Fuente incluye consulta y descarga de factura, guía y nota de crédito; ZIP solo consulta. | Precisar documentos, descarga y autorización por cliente. |

La matriz completa necesita la misma revisión semántica para todos los registros recuperados. Las fuentes CSV tienen precondiciones, prioridades y orígenes incompletos en varias filas; no constituyen por sí solas una versión lista para entregar.

## 9. Contenido mínimo de las 16 decisiones del caso

Cada fila debe quedar desarrollada en el registro de supuestos/decisiones con fundamento, impacto y validación, y sintetizada en la sección correspondiente del cuerpo.

| N.º del Caso 16.1 | Qué debe quedar decidido en SD3 |
|---|---|
| 1 | Entrega cumplida, tratamiento de parciales, fórmula OTIF y relación con fill rate; ventana acordada por canal. |
| 2 | Unidad sanitaria de trazabilidad y relación lote–producto–unidad logística–cliente. |
| 3 | Local cerrado, cantidad/plazo de reintentos, autoridad y retorno; no confundir automatización con capacidad física de cumplir nueva ventana. |
| 4 | Excursión, umbral, bloqueo preventivo, responsable de disposición y liberación; operación sin conexión y evidencia. |
| 5 | Identidad del conductor externo, cambio sin aviso, asignación conductor/vehículo/ruta y contingencia de alta offline. |
| 6 | Efectivo permitido, custodia, rendición y responsabilidad; alternativas voluntarias que no excluyan al tradicional. |
| 7 | Modelo de costo por entrega/cliente y autoridad comercial ante no rentabilidad, con captura previa de datos en E1. |
| 8 | Reserva de stock y prioridad de conflictos entre pedidos online/offline; rechazo o aceptación parcial informados. |
| 9 | Precio aplicable por momento, excepción, consentimiento/revalidación y efectos en facturación. |
| 10 | Control de envases, sentido del saldo, movimientos, conciliación y tratamiento del saldo inicial desconocido. |
| 11 | Maestro autorizado y equivalencias ante cambio de producto/código del proveedor. |
| 12 | Devolución en entrega, destino sanitario/físico y documento emitido por ERP cuando corresponda. |
| 13 | Cámaras/GPS y objeción sindical; finalidad, límites y estrategia de adopción. |
| 14 | Reemplazo del WMS, alternativas, alcance por ola/etapa, migración y reversión. |
| 15 | Receptor distinto, negativa o imposibilidad de firmar, evidencia alternativa y articulación tributaria. |
| 16 | Captura de conocimiento del planificador, calendario, reemplazo y prueba de transferencia. |

## 10. Cómo completar la aceptación sin inventar resultados

Estos son contenidos de protocolos **por diseñar**, no pruebas ejecutadas ni nuevas metas contractuales aprobadas.

| Criterio | Evidencia y definición que falta incorporar |
|---|---|
| R18-01 | Ensayo de retiro con lote y datos representativos; tiempo desde solicitud hasta lista verificable de destinos <2 h. |
| R18-02 | Universo de recepciones sujetas a lote; medición del 100 % y prueba de que no se cierra indebidamente una recepción sin identificación. |
| R18-03 | Cobertura de cámaras y vehículos, frecuencia, continuidad durante desconexión, conservación y auditoría de lecturas. |
| R18-04 | Fórmula única de OTIF, exclusiones justificadas, línea base comparable, meta propia y período sostenido de evaluación. |
| R18-05 | Stock/crédito online y offline, fecha de actualización visible y diferencia entre información y autorización. |
| R18-06 | Corte de señal y reintentos; comparar pedidos capturados/confirmados para demostrar cero pérdida y cero duplicación. |
| R18-07 | Ruta automática <20 min con volumen previsto, corrección manual registrada y criterios de factibilidad. |
| R18-08 | Disponibilidad de POD para cliente el mismo día, incluido turno sin señal y cliente sin dispositivo. Explicar canal y latencia. |
| R18-09 | Identificación y recuperación de todas las guías/evidencias, control de legibilidad e integridad. |
| R18-10 | Conciliación el mismo día; esperado vs. cobrado, causas documentadas y aprobación segregada de diferencias. |
| R18-11 | Costo por entrega/cliente desde hechos; fórmula e imputación, tratamiento de datos incompletos y fecha de habilitación E2. |
| R18-12 | Saldo inicial, movimientos y pérdida por tipo; meta anual, fuente y período de observación. |
| R18-13 | Orden electrónica sin redigitación, respuesta ASN y manejo de rechazo/duplicado por cadena antes del hito comercial. |
| R18-14 | Ocupación por peso/volumen, umbral comprometido, límites térmicos y tratamiento de excepciones autorizadas. |
| R18-15 | Registro estructurado de causa al detectar faltante, obligatoriedad y auditoría. |
| R18-16 | Ejecución por suplente con reglas documentadas; comparación de servicio en período acordado sin apoyo indispensable de Don Hugo. |

Agregar para cada uno etapa, mes/hito, responsable de medición y aceptación y vínculo al RF/RNF/prueba del T-12. Los objetivos generales de recuperación no reemplazan los criterios de aceptación de negocio.

## 11. Presentación, referencias y paquete de entrega

### 11.1 PDF y formalidad

- Los tres PDF tienen tamaño carta y texto extraíble. El código define cuerpo de 11 pt. Las muestras de diagramas y tabla de RF son legibles, aunque hay palabras partidas y márgenes aprovechables.
- La portada inspeccionada deja la firma en blanco; los PDF no presentan campos de firma digital. El nombre mecanografiado no acredita por sí solo firma. Aplicar el mecanismo exigido antes de presentar; esta auditoría no firma documentos.
- En páginas horizontales inspeccionadas el pie y folio permanecen girados en el lateral, no en el extremo inferior derecho de la lectura horizontal. Revisar contra art. 40 y el estándar común de la propuesta.
- La declaración IA del cuerpo está en horizontal. Aclaraciones §5 reserva la orientación horizontal para anexos y a la vez §7.2 pide seis columnas para IA: conservar las seis columnas obligatorias y ajustar maquetación, evitando perder información por aplicar mecánicamente la referencia de cinco columnas.
- Anexos tienen una «Lista de figuras» vacía en p. 4; retirar índices sin contenido. El cuerpo termina con una página 17 casi vacía por continuación de la nota IA: resolverla al cerrar contenido y maquetar.
- Completar páginas de fuentes cuando se disponga del original paginado. No inventarlas desde el Markdown. No considerar cerrado ese requisito porque el texto declare que faltan.
- Unificar autores/años y títulos en cuerpo, anexos y T-12, y aclarar BA/BTT/SD y códigos en el glosario. Citar Aclaraciones como fuente normativa usada cuando corresponda; la retroalimentación sirve para corregir, no como nota interna del profesor insertada en la oferta.

### 11.2 Archivos anteriores incluidos

**Hallazgo confirmado de paquete:** `tablas/esquema_solucion_alcance.xlsx`, hoja `3.8 Decisiones`, fila 48, decisión 45, conserva «del orden de 113 mil dólares antes de reservas». La misma hoja/libro mantiene supuestos, horarios y códigos de otra versión.

En los tres PDF vigentes no se encontró esa frase. Por tanto, no corresponde decir que sigue en la p. 107 del cuerpo actual; el cuerpo actual solo tiene 17 páginas. **Sí corresponde retirarla del paquete técnico final**, porque el archivo que la contiene va dentro del ZIP enviado.

El monto de diferencias de efectivo de $4,2 millones del Caso es una línea base del problema, no el precio de la oferta: no eliminar datos de diagnóstico legítimos indiscriminadamente. Eliminar del paquete técnico montos de oferta/cotización y material histórico que pueda confundirse con la propuesta vigente.

**Quitar del ZIP de presentación**, manteniendo respaldo de trabajo fuera de él: `main.pdf`, derivados intermedios `.aux/.log/.toc/.fls/.fdb_latexmk/.synctex.gz`, cachés, Excel históricos y fuentes no solicitadas cuando no formen parte de los entregables exigidos. Conservar únicamente las versiones finales requeridas y su organización conforme a las Bases. No se han borrado archivos con esta revisión.

### 11.3 Reproducibilidad de las correcciones

El README indica regenerar las tablas. `tablas/generador/datos_rt.py` busca `Bases/Bases_Tecnicas_Transversales.md` fuera de la carpeta del SD3; esa estructura no está incluida en el ZIP. El documento rector ahora está disponible en `info`, pero la ruta no coincide.

Antes de regenerar, ajustar la ruta de entrada o preparar una estructura de trabajo reproducible. `gen.py` genera campos vacíos de forma fija para decisiones, reglas, participación, metas y T-12: **editar solo las tablas o rellenar parcialmente JSON no basta**, porque una regeneración puede volver a vaciarlas. Modificar el modelo de datos y el generador para conservar decisiones y trazas completas; después regenerar y comparar PDF/DOCX desde la misma versión. Este es un cambio del proceso de edición, no contenido para la propuesta técnica.

## 12. Orden recomendado para corregir

1. **Fijar una versión de referencia:** ZIP actual, TEX de AL/AF y registros reconciliados. Mantener fuera los Excel históricos que contradicen esa versión.
2. **Resolver nomenclaturas:** RF resumidos vs. detallados, RF-14/RF-19, supuestos y decisiones renumerados. Publicar tabla de equivalencias.
3. **Cerrar las 16 decisiones:** especialmente frío, precio, stock, POD/DTE, promesa, WMS y conocimiento del planificador. Recuperar contenido válido sin restaurar los errores señalados por el profesor.
4. **Completar requisitos y aceptación:** descripciones verificables, umbrales, métodos, etapas y orígenes. No priorizar la cantidad sobre la cobertura del Caso.
5. **Alinear E1/E2 y M1–M12:** resolver M10 y funciones tempranas de soporte a transportistas; completar capacidades y excepciones del esquema.
6. **Desarrollar implementación, implantación y operación:** con decisiones concretas y evidencias previstas, no remisiones pendientes.
7. **Cerrar T-12:** cada requisito con componente, EDT, prueba y criterio; parámetros particulares del Caso y correspondencia RT por materia.
8. **Completar interesados e hitos:** responsables, momentos, metas, gestión de adopción y alcance de instalaciones.
9. **Revisión humana y formalidad:** verificar el conjunto, corregir título, referencias, firmas, figuras, folios, maquetación y declaración IA; retirar notas solo después de resolverlas.
10. **Preparar paquete final limpio:** verificar que cuerpo, anexos, T-12 y cualquier formato editable entregado correspondan a una misma versión y no incluyan montos ni archivos históricos improcedentes.

### Condición para considerar cerrada la revisión

El SD3 debe poder explicar por sí mismo qué se construye, qué queda fuera, cómo se reparte y acepta el alcance, cómo se implementa/implanta/opera y quién participa. Sus requisitos deben enlazar a una arquitectura consistente, sin desaparecer al pasar a anexos o T-12. La mera ausencia de contradicciones explícitas, lograda dejando decisiones vacías, no constituye cumplimiento.

## 13. Inventario de registros sin desarrollar

El inventario siguiente identifica todos los RF sin descripción y los RNF sin umbral del registro activo. Cada fila exige decisión de cobertura y desarrollo; no supone que deba conservarse una funcionalidad sin fundamento. Las bajas o fusiones deben justificarse y mantener equivalencia histórica.

Para cada RF que permanezca: descripción verificable, actor, precondición, resultado, prioridad, etapa, origen y traza T-12. Para cada RNF: umbral medible, condiciones, método, etapa/hito, origen y traza. Además, los 13 RNF que ya tienen algún contenido necesitan método, porque actualmente ninguno lo tiene.

### 13.1 RF sin descripción: 143 registros

| ID | Materia que debe desarrollarse o resolverse |
|---|---|
| RF-01.01 | Recepción y Validación de Cantidades contra OC |
| RF-01.04 | Registro de No Conformidades en Recepción |
| RF-01.05 | Cuarentena Automática por No Conformidad |
| RF-01.07 | Generación e Impresión de Etiqueta SSCC |
| RF-01.08 | Asignación de SSCC a Ubicación de Almacenamiento |
| RF-01.09 | Integración de Recepción con ERP |
| RF-01.10 | Gestión de Fichas de Producto |
| RF-01.11 | Validación de Compatibilidad Térmica en Putaway |
| RF-02.01 | Configuración de topología de instalaciones |
| RF-02.02 | Consolidación de stock físico multi-sitio |
| RF-02.03 | Reasignación de ubicaciones (slotting) |
| RF-02.04 | Conteo cíclico en modo ciego |
| RF-02.05 | Cálculo de stock disponible para la venta |
| RF-02.06 | Gestión de inventario en tránsito |
| RF-02.07 | Consulta de nivel de ocupación por zona |
| RF-02.09 | Retención sanitaria de lote en inventario |
| RF-02.10 | Ficha de trazabilidad de lote |
| RF-03.03 | Reserva de stock al confirmar el pedido |
| RF-03.06 | Consulta de historial de compra del cliente |
| RF-03.07 | Aplicación de promociones a una línea de pedido |
| RF-03.08 | Alerta por superación del límite de crédito |
| RF-03.09 | Bloqueo de envío por exceso de crédito |
| RF-03.10 | Autorización de excepción por supervisor de crédito |
| RF-03.11 | Configuración de excepción de precio por cliente o cadena |
| RF-03.12 | Alerta al cliente por cambio de precio |
| RF-03.13 | Información de ventana de entrega comprometible |
| RF-03.14 | Sugerencia de productos al preventista |
| RF-03.15 | Generación de identificador único de pedido offline |
| RF-04.03 | Bloqueo de asignación por exceso de capacidad |
| RF-04.04 | Ajuste de secuencia de ruta por ventanas horarias |
| RF-04.05 | Restricción de vehículos por requisito de cadena de frío |
| RF-04.06 | Notificación de hora estimada de llegada al cliente |
| RF-04.07 | Parametrización de ventanas horarias |
| RF-04.08 | Cálculo integral del costo de entrega realizada |
| RF-05.02 | Validación de líneas por escaneo GS1 |
| RF-05.04 | Secuenciación térmica de misiones |
| RF-05.06 | Envío de preparación al ERP |
| RF-05.07 | Carga dirigida inversa a ruta |
| RF-06.01 | Confirmación de recepción de bultos |
| RF-06.03 | Reporte de rechazo de productos |
| RF-06.04 | Reporte de local cerrado y reagendamiento automático |
| RF-06.06 | Registro de hora real de llegada y término de la entrega |
| RF-06.07 | Sincronización automática de registros de turno |
| RF-06.08 | Autenticación del conductor externo por clave de un solo uso |
| RF-06.09 | Captura de devolución de envases retornables |
| RF-06.10 | Actualización de saldo de envases retornables |
| RF-06.11 | Confirmación de recepción mediante QR |
| RF-06.13 | Impresión de comprobante térmico en terreno |
| RF-07.01 | Cálculo del monto esperado de rendición por camión |
| RF-07.04 | Consola de Gestión de Cartera de Crédito |
| RF-07.05 | Alerta y Bloqueo de Crédito en Preventa |
| RF-07.06 | Cobro con Terminal POS Móvil en Ruta |
| RF-07.07 | Consulta de Estado de Cuenta en Portal de Clientes |
| RF-07.08 | Validación en Tesorería de Pagos Web |
| RF-07.09 | Interfaz Asíncrona de Cobranzas hacia ERP |
| RF-07.10 | Registro de Abonos y Pagos Parciales en Entrega |
| RF-07.11 | Cobranza Presencial de Facturas por Preventistas |
| RF-08.01 | Registro de Devoluciones en Ruta |
| RF-08.02 | Gestión del Destino de Productos Devueltos |
| RF-08.03 | Gestión de Cuenta Corriente de Envases Retornables |
| RF-08.04 | Alertas por Exceso de Envases Retornables |
| RF-08.05 | Registro de Mermas por Vencimiento |
| RF-08.06 | Reporte de Pérdida de Envases Retornables |
| RF-08.07 | Integración de Devoluciones y Mermas al Costo de Servir |
| RF-09.06 | Retención automática del lote ante excursión térmica |
| RF-09.07 | Registro de rechazo del cliente por sospecha de ruptura de frío |
| RF-09.08 | Registro de lotes con control sanitario |
| RF-09.09 | Generación de cumplimiento de cadena de frío |
| RF-09.10 | Parametrización de la regla de excursión térmica |
| RF-10.01 | Sugerencia de reposición de compras por SKU y proveedor |
| RF-10.02 | Incorporación de promociones comprometidas a la reposición |
| RF-10.03 | Traspaso de la sugerencia aprobada al módulo de compras del ERP |
| RF-11.01 | Distribución Automática de Reportes Ejecutivos |
| RF-11.04 | Medición de Fill Rate y Perfect Order con POD Móvil |
| RF-11.05 | Monitoreo y Alerta de Ocupación de Flota |
| RF-11.06 | Tablero de Control Operacional en Tiempo Real |
| RF-11.07 | Liquidación y Cierre Comercial por Camión |
| RF-11.08 | Segmentación de Clientes por Rentabilidad Neta |
| RF-12.02 | Validación automática del pedido EDI |
| RF-12.03 | Resolución del código de producto contra el maestro de Puelche |
| RF-12.04 | Registro automático del pedido EDI válido en el sistema de gestión |
| RF-12.05 | Disponibilización del pedido a la planificación de despacho |
| RF-12.06 | Gestión de excepciones de pedidos EDI inválidos |
| RF-12.07 | Confirmación o rechazo del pedido a la cadena de origen |
| RF-12.08 | Historial de estados del pedido electrónico |
| RF-12.10 | Planificación de la llegada dentro de la ventana de 30 minutos |
| RF-12.11 | Registro del cumplimiento de la ventana de entrega |
| RF-12.12 | Captura de evidencia de entrega en canal moderno |
| RF-12.13 | Envío de acuse de recibo digital al cliente |
| RF-12.15 | Pedido en autoservicio para clientes del canal moderno |
| RF-12.18 | Consulta de saldo y estado de cuenta en el portal de clientes |
| RF-12.19 | Consulta de rutas asignadas en el portal de transportistas |
| RF-12.20 | Descarga de documentación de despacho en el portal de transportistas |
| RF-12.21 | Confirmación diaria de conductor y vehículo |
| RF-12.22 | Consulta de órdenes de compra en el portal de proveedores |
| RF-12.23 | Consulta de recepciones en el portal de proveedores |
| RF-12.24 | Consulta de devoluciones y notas de crédito en el portal de proveedores |
| RF-12.25 | Registro de cliente en el portal |
| RF-12.26 | Inicio de sesión en el portal de clientes |
| RF-12.27 | Recuperación de contraseña |
| RF-12.28 | Cierre de sesión en el portal de clientes |
| RF-12.29 | Expiración automática de sesión por inactividad |
| RF-12.30 | Pago electrónico de pedidos de autoservicio |
| RF-13.01 | Declaración de arquitectura multicapa |
| RF-13.02 | Tabla de emplazamiento nube/on-premise |
| RF-13.03 | Registro de decisiones de arquitectura (ADR) |
| RF-13.04 | Modelo de dominio de negocio |
| RF-14.01 | Integración con telemetría de camiones propios |
| RF-14.02 | Visualización de rutas planificadas vs reales |
| RF-14.03 | Alerta de desviación de ruta |
| RF-14.04 | Integración de telemetría con costo de servir |
| RF-14.05 | Vinculación conductor-camión en cada viaje |
| RF-14.06 | Gestión de geocercas para control de llegada/salida |
| RF-15.01 | Gestión centralizada de identidad |
| RF-15.02 | Inicio de sesión único (SSO) para todos los módulos |
| RF-15.03 | Autenticación multifactor (MFA) para administradores y acceso externo |
| RF-15.04 | Control de acceso basado en roles (RBAC) y segregación de funciones |
| RF-15.05 | Aprovisionamiento y desaprovisionamiento automatizado de cuentas |
| RF-16.01 | Observabilidad unificada para nube y on-premise |
| RF-16.02 | Acceso del CLIENTE a tableros operacionales y de negocio |
| RF-16.03 | Alertamiento basado en síntomas de negocio |
| RF-16.04 | Análisis de causa raíz obligatorio tras incidente crítico |
| RF-17.01 | Módulo de administración de usuarios, roles y permisos |
| RF-17.02 | Parametrización de reglas de negocio desde interfaz de administración |
| RF-17.03 | Aprobación de dos perfiles para cambios de parámetros con impacto operacional |
| RF-17.04 | Registro de auditoría inalterable |
| RF-17.05 | Consulta y exportación de auditoría desde la interfaz |
| RF-17.06 | Soporte de flujos de trabajo configurables |
| RF-17.07 | Bandeja de tareas unificada |
| RF-17.08 | Gestión documental con versionado y control de acceso |
| RF-17.09 | Generación de documentos a partir de plantillas |
| RF-17.10 | Notificaciones multicanal (correo, SMS, notificación en app) |
| RF-17.11 | Búsqueda global con indexación de texto completo |
| RF-17.12 | Listados ordenables, filtrables, paginados y exportables |
| RF-17.13 | Portal público con catálogo y contacto (sin autenticación) |
| RF-18.01 | Soporte de firma electrónica avanzada (Ley 19.799) |
| RF-18.02 | Configuración de preferencias de notificación por usuario |
| RF-18.03 | Envío asíncrono de notificaciones con reintento y registro |
| RF-19.01 | Clasificación de información por nivel de sensibilidad |
| RF-19.02 | Matriz de controles de seguridad trazable a ISO 27001/27002 |
| RF-19.03 | Declaración de superficie de exposición |
| RF-19.04 | Plan de respuesta a incidentes de seguridad |
| RF-19.05 | Notificación de brecha de seguridad al CLIENTE |

### 13.2 RNF sin umbral: 77 registros

| ID | Materia que debe desarrollarse o resolverse |
|---|---|
| RNF-01.01 | Tiempo de registro de un ítem en recepción |
| RNF-01.02 | Retención de registros de recepción |
| RNF-03.01 | Registro de una línea de pedido en preventa |
| RNF-03.02 | Consulta de stock y crédito en preventa |
| RNF-03.03 | Consulta del historial de compra |
| RNF-05.01 | Confirmación de una línea de picking |
| RNF-05.03 | Curva de aprendizaje del preparador |
| RNF-06.02 | Duración del acceso sin conexión por perfil |
| RNF-07.01 | Preconciliación de cobranzas al reconectar |
| RNF-07.02 | Cifrado a nivel de campo de datos de pago y de comportamiento de pago |
| RNF-08.01 | Registro de una devolución en el andén de retorno |
| RNF-08.02 | Retención de devoluciones y mermas |
| RNF-09.02 | Retención de la trazabilidad sanitaria |
| RNF-09.03 | Registro de consultas a la trazabilidad y a información sensible |
| RNF-09.04 | Captura de temperatura sin señal |
| RNF-09.05 | Frecuencia de registro de temperatura |
| RNF-11.01 | Latencia de los indicadores de la operación del día |
| RNF-11.02 | Desacople entre analítica y transacción |
| RNF-11.03 | Cierre comercial del día |
| RNF-11.04 | Latencia de los indicadores de gestión |
| RNF-12.02 | Incorporación de una cadena nueva sin desarrollo |
| RNF-12.03 | Envío del acuse de recibo al canal moderno |
| RNF-13.02 | Funciones no disponibles sin conexión |
| RNF-13.03 | Redundancia de equipos on-premise críticos |
| RNF-13.04 | Tolerancia a la falla de disco |
| RNF-13.05 | Nivel RAID declarado |
| RNF-13.06 | Endurecimiento de sistemas on-premise |
| RNF-13.07 | Enlace redundante entre sitio y nube |
| RNF-13.08 | Ancho de banda por sitio |
| RNF-13.09 | Cobertura inalámbrica en los sitios |
| RNF-14.01 | Cifrado en tránsito |
| RNF-14.02 | Cifrado en reposo |
| RNF-14.03 | Segregación de red en nube |
| RNF-14.04 | Correlación de eventos de seguridad |
| RNF-14.05 | Detección y respuesta en puntos finales |
| RNF-14.06 | Pruebas de intrusión |
| RNF-14.07 | Análisis de código y de dependencias |
| RNF-14.08 | Inventario de componentes de software |
| RNF-14.09 | Procedencia de artefactos |
| RNF-14.10 | Datos productivos en ambientes no productivos |
| RNF-14.11 | Privacidad de la geolocalización de personas |
| RNF-14.12 | Categorías de datos personales en terreno |
| RNF-15.01 | Política de sesión |
| RNF-15.02 | Credenciales de sesión |
| RNF-15.03 | Auditoría del ciclo de vida de la identidad |
| RNF-16.01 | Indicadores de nivel de servicio sobre la experiencia real |
| RNF-16.02 | Libros de operación y guías de resolución |
| RNF-16.03 | Registros sin datos sensibles ni credenciales |
| RNF-17.01 | Retención de la auditoría |
| RNF-17.02 | Exportaciones de gran volumen |
| RNF-17.03 | Portal público ante picos de tráfico |
| RNF-19.01 | Cálculo de capacidad |
| RNF-19.02 | Escalamiento horizontal automático |
| RNF-19.03 | Componente que se satura primero |
| RNF-19.04 | Pruebas de carga y estrés |
| RNF-20.01 | Disponibilidad de los servicios críticos |
| RNF-20.02 | Clasificación de servicios por criticidad |
| RNF-20.03 | Continuidad del negocio |
| RNF-20.04 | Pruebas de resiliencia |
| RNF-20.05 | Comportamiento ante falla de dependencias externas |
| RNF-20.07 | Política de respaldo |
| RNF-21.02 | Gerente de servicio dedicado |
| RNF-21.03 | Umbrales de atención de la mesa |
| RNF-21.04 | Horario de atención |
| RNF-21.05 | Dimensionamiento de la mesa de ayuda |
| RNF-21.06 | Canal único de registro |
| RNF-21.07 | Traslado de especialistas a sitios alejados |
| RNF-21.08 | Bolsa anual de mantención evolutiva |
| RNF-21.09 | Actualización anual de componentes de base |
| RNF-22.01 | Plan de capacitación por perfil |
| RNF-22.02 | Material de capacitación |
| RNF-22.04 | Certificación de administradores y técnicos |
| RNF-22.05 | Capacitación del personal nuevo del CLIENTE |
| RNF-22.06 | Mentoría al equipo de TI del CLIENTE |
| RNF-23.02 | Protección de los dispositivos de terreno |
| RNF-23.03 | Ciclo de vida de los dispositivos |
| RNF-23.04 | Estaciones de trabajo de operación y administración |

### 13.3 RNF con contenido pero sin método de verificación

RNF-01.03, RNF-02.01, RNF-04.01, RNF-05.02, RNF-06.01, RNF-06.03, RNF-09.01, RNF-12.01, RNF-13.01, RNF-20.06, RNF-21.01, RNF-22.03, RNF-23.01.
