# Análisis del Subdocumento 3

Fecha de revisión: 1 de octubre de 2026.

## Dictamen

La versión actual resuelve buena parte de las objeciones estructurales de la primera entrega. Explica la solución, incluye tres figuras conceptuales y desarrolla implementación, implantación y operación. Sin embargo, todavía no está cerrada para entrega: la matriz T-12 conserva trazabilidad incompleta, asociaciones incorrectas y referencias insuficientes para acreditar requisitos. La prioridad es corregir esas relaciones y consolidar las cifras, preservando el análisis ya logrado.

## Alcance de esta revisión

Se revisó el cuerpo completo, los archivos fuente activos, la estructura y los registros de los anexos, y la matriz T-12 mediante comprobaciones de identificadores y revisión de asociaciones concretas. Se extrajo el texto de los tres PDF vigentes y se inspeccionó visualmente una muestra de páginas de diagramas, texto y tablas. El contraste utiliza las Bases Administrativas, las Bases Técnicas Transversales, el Caso 02, las aclaraciones y la retroalimentación de la primera entrega disponibles en la carpeta.

No se modificaron los documentos de la oferta. No se certificó individualmente la corrección semántica de las 374 respuestas RT ni se inspeccionaron visualmente las 375 páginas del conjunto. No se encontró el Subdocumento 4 en la carpeta: no se puede confirmar el mapeo del 100 % con su arquitectura lógica. Tampoco se verificaron documentos de planificación o pruebas posteriores no disponibles. El análisis es documental; no constituye una validación normativa externa del mecanismo de acuse tributario.

## Inventario comprobado

| Elemento | Resultado |
|---|---:|
| Cuerpo principal | 26 páginas PDF |
| Anexos | 142 páginas PDF |
| Formulario T-12 | 207 páginas PDF |
| RF ofertados | 175: 134 del caso, 34 BTT, 7 propios |
| RNF ofertados | 86: 24 del caso, 58 BTT, 4 propios |
| Total de requisitos ofertados | 261 |
| Filas RF del T-12, incluidas materias complementarias | 181 |
| Filas RNF del T-12, incluidos alias y materias absorbidas | 90 |
| RT de las BTT incluidos en T-12 | 374 de 374, sin duplicados de código en esas filas |
| Supuestos actuales | 40, S-01 a S-40 |
| Filas con «Paquete por asignar en el plan de trabajo» | 262 |

La cobertura numérica RT está completa; esto no demuestra que cada respuesta acredite su exigencia.

## Qué mejoró respecto de la primera entrega

- La estructura 3.1–3.4 coincide con los títulos de las aclaraciones. El cuerpo dejó de ser principalmente un catálogo de tablas.
- Las figuras 3.1–3.3 muestran el ciclo logístico, la trazabilidad y la continuidad. Tienen fuente y explicación.
- La Tabla 3.1 diferencia desarrollo, marcha blanca y producción: E1 meses 1–12, 13–15 y 16; E2 meses 13–18, 19–20 y 21; operación meses 21–56.
- Se analiza la incompatibilidad de ciertos meses de inicio con septiembre y diciembre, el hito de enero de 2029 y el vencimiento de la suspensión del proveedor de lácteos.
- Se justifica adelantar rutas a E1 por el retiro del planificador y mantener costo de servir en E2. M10 distingue medición de OTIF en E1 de costo de servir en E2.
- La regla térmica separa alerta menor de retención preventiva por excursión crítica; Calidad decide la liberación. Se resuelve la atribución contradictoria al conductor.
- Se declara una promesa diferenciada de 24/48 horas y el precio acordado por el preventista al tomar el pedido, conservado aunque cambie posteriormente la lista de precios.
- Implementación incorpora ambientes, revisión de pares, integración continua y cobertura bloqueante de pruebas. Implantación incorpora papel, olas, migración, acompañamiento nocturno y conductores externos. Operación incorpora horarios, incidentes y objetivos de servicio.
- Los RF tienen los campos del numeral 17.1 y los RNF incluyen umbral y verificación prevista. Los resultados R18 tienen metas y métodos, incluido el ensayo sin el planificador.

## Hallazgos prioritarios

### 1. Alta: la trazabilidad sigue incompleta

En la Parte A del T-12 aparecen 262 filas con el paquete EDT por asignar. Hay columnas de prueba y criterio, pero muchas pruebas son descripciones generales y no referencias inequívocas a un protocolo. El numeral 17.1 del caso exige correspondencia entre origen, requerimiento, componente, paquete EDT, prueba y criterio de aceptación. Remitir al futuro plan de trabajo no completa esa correspondencia.

Corrección: enlazar cada requisito ofertado con un paquete existente y una prueba identificada, usando los documentos de planificación y calidad. Separar expresamente los alias y materias absorbidas. No inventar identificadores de paquetes para aparentar cierre.

### 2. Alta: existen asociaciones semánticas incorrectas

Ejemplos comprobados en el T-12:

| Código | Exigencia | Asociación actual | Problema |
|---|---|---|---|
| RT-16.14 de BTT | Motor de reglas sin recompilación y trazabilidad de la regla aplicada | M6 Reparto; RF-06.01, RF-06.02 y RF-12.17 | Recibir bultos, capturar firma y consultar documentos no acreditan un motor de reglas. El caso usa RT-16.14 para firma electrónica: la coincidencia de código entre fuentes requiere distinguir su significado. |
| RF-01.07 | Generar SSCC y vincularlo a los datos del pallet | Prueba en cámara y vehículo con registro térmico | No comprueba generación, unicidad ni asociación del SSCC. |
| RF-01.08 | Asociar SSCC con dirección de almacenamiento | Prueba en cámara y vehículo con registro térmico | No verifica el vínculo ni las validaciones de ubicación. |
| RF-02.10 | Consultar ciclo de vida de un lote | R18-15, causa de faltantes | No acredita por sí mismo el resultado sanitario R18-01. |

Corrección: revisar las relaciones por contenido, distinguiendo origen y código; admitir varios criterios de aceptación cuando corresponda. Las pruebas complementarias de usabilidad o desempeño no sustituyen la prueba funcional del resultado.

### 3. Alta: varios «Sí» transversales no tienen respaldo localizado suficiente

Las BTT, numeral 1.5, piden componente, servicio, producto o práctica concreta individualizada, sección y página, y evidencia. Varias filas usan «Base compartida» o «Innovaciones de la oferta» y una sección amplia, sin página ni desarrollo específico verificable.

RT-26.01 y RT-26.02 remiten a 3.2.1. Esa sección distribuye capacidades por etapa; no individualiza la arquitectura de cada innovación ni sus paquetes y meses. La evidencia propuesta para RT-26.02 es una verificación de configuración en marcha blanca, que no reemplaza la identificación de paquetes y meses en la oferta.

Corrección: señalar el artefacto concreto y su ubicación verificable. El compromiso futuro puede declararse, pero debe distinguirse de la evidencia documental que ya corresponde presentar.

### 4. Media: cifras y documentación de mantenimiento desactualizadas

- El cuerpo, sección 3.2.2, dice 29 supuestos; el anexo llega a S-40.
- El texto resume 250 requisitos y 54 críticos, 157 altos y 39 medios. Esa cuenta corresponde a los catálogos sin los once requisitos propios. El total ofertado es 261 y la distribución conjunta comprobada es 56 críticos, 162 altos y 43 medios. Conviene expresar ambos universos y evitar presentar 250 como total general.
- El README todavía declara 174 RF y solo 31 desarrollados, y describe un T-12 sin cumplimiento completo. Esa descripción no corresponde a las fuentes activas revisadas.
- El generador documentado produce fragmentos de la estructura anterior; el T-12 actual contiene sus tablas directamente y los anexos incluyen `tablas_anexo`. El flujo de mantenimiento debe aclararse antes de regenerar.

Corrección: consolidar un inventario único y documentar qué archivos gobiernan realmente cada salida.

### 5. Alta: la reversión carece de una duración y una alternativa durante el despacho

La sección 3.4.4 dispone que la reversión termine antes de las 05:30, pero incluye como disparador un defecto crítico dentro de la ventana 05:30–07:00. En ese escenario ya no es posible cumplir el plazo escrito. Tampoco se expresa cuánto demora la vuelta al procedimiento manual ni la última hora segura para decidirla.

Corrección: fijar duración máxima ensayada, hora límite de decisión, responsable y procedimiento para incidentes después de las 05:30. Distinguir reversión de una ola y continuidad de una operación que ya está despachando.

### 6. Media: los criterios para avanzar de ola deben ser aplicables a esa ola

La sección 3.4.4 exige indicadores del Anexo 3.J sostenidos cuatro semanas. El anexo incluye resultados de E2, una meta anual de envases y el OTIF del mes 32. Aunque el documento distingue aceptaciones provisionales, la regla general de avance no delimita qué resultados aplican a cada ola.

Corrección: asignar a cada ola su subconjunto de R18, umbral, período, evidencia y aceptación provisional o definitiva. Así se evita exigir resultados posteriores para habilitar una ola anterior.

### 7. Media: la tolerancia de migración necesita separar errores de origen y de transferencia

S-29 propone una tolerancia del 2,3 % para saldos valorizados a partir de la discrepancia actual del conteo cíclico. Esa cifra describe una debilidad de la operación de origen; no demuestra que sea una tolerancia apropiada para migración. El texto sí exige exactitud en documentos y lotes, lo que es positivo.

Corrección: exigir que la migración reproduzca exactamente los saldos aprobados, y gestionar por separado las diferencias entre inventario físico y registros antiguos, con ajustes autorizados. Si se mantiene tolerancia, justificar su alcance y el tratamiento de cada diferencia.

### 8. Media: presentación, volumen y cierre editorial

El cuerpo tiene 26 páginas y entra en la extensión de 25–35 solicitada por la retroalimentación, aunque esa cuenta incluye portada e índices. No conviene aumentar texto para llenar páginas.

Los anexos y T-12 suman 349 páginas. El detalle está correctamente separado del cuerpo, pero las páginas examinadas muestran columnas estrechas, palabras muy partidas y tablas que ocupan muchas páginas. En la Figura 3.3, página 16 del cuerpo, la etiqueta «Reconexión» queda demasiado próxima y parcialmente superpuesta a los bordes de los nodos.

Las portadas dicen «VERSIÓN FINAL PARA ENTREGA», mientras el T-12 mantiene paquetes por asignar y la revisión humana figura como «No documentada». La aclaración 7.1.d sanciona marcadores de trabajo pendientes. Esto requiere cierre real y revisión humana registrada; no basta eliminar las expresiones ni afirmar una revisión que no ocurrió.

Corrección: ajustar anchos y orientación de tablas, corregir la etiqueta del diagrama y revisar las referencias finales. La revisión visual realizada fue una muestra, no una garantía sobre todas las páginas.

## Orden de trabajo recomendado

1. Corregir las correspondencias erróneas del T-12 y distinguir códigos iguales de fuentes distintas.
2. Completar enlaces con arquitectura, EDT y pruebas reales; ubicar evidencia por sección y página.
3. Resolver la reversión durante despacho y los criterios específicos de cada ola.
4. Unificar cifras, supuestos, prioridades y flujo de generación.
5. Revisar migración, presentación y registro de revisión humana.

La solución ya se entiende. Lo pendiente es demostrar, con relaciones correctas y evidencia localizada, que cada compromiso se construye, se prueba y se acepta de forma consistente.
