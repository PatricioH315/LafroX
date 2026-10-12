# LafroX — Mapeo de requerimientos del T-12 a paquetes de trabajo de la EDT (T-14)

## Propósito y respuesta corta

Documento de trabajo. Comprueba si cada una de las 645 filas del Formulario T-12 tiene un paquete de trabajo en la EDT del Formulario T-14 (49 cuentas de control y 222 paquetes), antes de decidir si se agrega esa columna al T-12. Responde a la observación del Informe 1 sobre la matriz «sin columna de paquete de la EDT» y a la exigencia del caso de relacionar origen, requerimiento, componente, paquete de la EDT, prueba y criterio de aceptación (caso, cap. 17.1, p. 31). No modifica el T-12 ni el T-14.

**Respuesta corta:** la EDT cubre casi todo, pero no todo. De las 645 filas, 390 tienen un paquete que las cubre de forma directa y 193 quedan cubiertas de forma indirecta (por un paquete más amplio o por su cuenta de control). **25 filas no tienen paquete** y 37 no generan trabajo del proyecto. Si hoy se agregara la columna al T-12, esas 25 filas quedarían vacías o apuntando solo a una cuenta, y la Comisión lo vería como faltante. Se cierran con dos paquetes nuevos (ver «Brechas»).

## Criterio

- **Directo:** el nombre, el entregable o el criterio de aceptación del paquete cubre la materia del requerimiento.
- **Indirecto:** la materia cae dentro de un paquete o una cuenta más amplios, pero ninguno la nombra. Basta para la columna del T-12; la observación indica qué conviene precisar en el diccionario.
- **Brecha:** ningún paquete cubre la materia; solo podría remitirse a una cuenta de control completa o a nada.
- **No aplica:** filas «No cumple» (sin trabajo comprometido), declaraciones que se cumplen sin trabajo (por ejemplo, no incorporar IA) y obligaciones del proceso de licitación (sitio web corporativo).

Regla de asignación: los RF y RNF cuyo componente es un módulo van al paquete de construcción de ese módulo (3.4.1 a 3.4.11 en la Etapa 1; 3.5.1 a 3.5.4 en la Etapa 2, según la etapa del Anexo 3.A o 3.B del SD3). Los demás se asignaron uno por uno según la materia. Todo requerimiento pasa además por las pruebas de integración y regresión (3.8.1 en la Etapa 1 y 3.9.1 en la Etapa 2); no se repiten en cada fila.

Validación: los 645 códigos asignados existen en el T-14. De las 83 filas del T-12 que ya citan una cuenta o un paquete del T-14, todas coinciden con este mapeo; en cuatro se agregó el paquete citado como secundario.

## Resumen

| Parte del T-12 | Filas | Directo | Indirecto | Brecha | No aplica |
|---|---:|---:|---:|---:|---:|
| A — RF y RNF | 271 | 227 | 34 | 10 | 0 |
| B — RT | 374 | 163 | 159 | 15 | 37 |
| **Total** | **645** | **390** | **193** | **25** | **37** |

## Brechas y paquetes propuestos

| Brecha | Filas | Paquete que la cerraría |
|---|---|---|
| Servicios comunes de la plataforma: consola de parametrización con aprobación de un segundo perfil, flujos de trabajo y bandeja de tareas, motor de reglas, gestión documental y plantillas, búsqueda global, listados, exportaciones y carga masiva. La cuenta 3.3 dice reunir «los servicios de software que usan los doce módulos», pero sus seis paquetes no los nombran. | 22: RF-17.02, RF-17.03, RF-17.06, RF-17.07, RF-17.08, RF-17.09, RF-17.11, RF-17.12, RNF-17.02, RT-05.22, RT-16.02, RT-16.03, RT-16.04, RT-16.11, RT-16.12, RT-16.13, RT-16.14, RT-16.15, RT-16.19, RT-16.27, RT-16.28, RT-16.29 | Nuevo **3.3.7 Servicios comunes de la plataforma**, en QA antes del H4. |
| Estaciones de trabajo de operación y administración (ocho estaciones con monitores duales, NCh 2527). El T-11 las especifica, pero ningún paquete las especifica, compra ni instala. | 3: RNF-23.04, RT-08.07, RT-08.08 | Ampliar **5.1.2** o crear **5.1.4 Estaciones de trabajo de operación**, con su instalación en 6.5. |

Con esos dos paquetes, las 25 brechas pasan a cobertura directa y la columna de paquete del T-12 queda sin vacíos.

### Revisión una por una de las 25 brechas

Se buscó cada materia en todo el T-14 (paquetes, entregables, criterios y textos de cuenta), en el T-15 y en el SD7: ninguno la nombra. La oferta sí la resuelve técnicamente (SD4 o T-11); lo que falta es el paquete que la construye o la compra. «Firme» significa que ningún paquete existente puede reclamarla; «defendible» significa que un paquete existente la cubre en parte y podría citarse mientras no se cree el nuevo.

| N.° | ID | Qué exige | Dónde la resuelve la oferta | Paquete existente más cercano | Veredicto |
|---:|---|---|---|---|---|
| 1 | RF-17.02 | Parametrizar reglas desde la administración, con versión y autor. | SD4 4.1.3.4: consola Angular y versiones de parámetros. | Ninguno; 3.3.1 solo da roles. | Firme |
| 2 | RT-16.02 | Lo mismo que RF-17.02, como requisito de las Bases. | SD4 4.1.3.4. | Ninguno. | Firme |
| 3 | RT-16.04 | Declarar qué es parametrizable y qué requiere desarrollo. | SD4 4.1.3.4. | Ninguno; la declaración existe, pero no su construcción. | Firme |
| 4 | RF-17.03 | Aprobación de un segundo perfil para cambios de parámetro. | SD4 4.1.3.4. | 3.3.1 (roles), sin el flujo de aprobación. | Firme |
| 5 | RT-16.03 | Lo mismo que RF-17.03. | SD4 4.1.3.4. | 3.3.1, parcial. | Firme |
| 6 | RF-17.06 | Flujos con estados, plazos, escalamiento y delegación, configurables. | SD4 4.1.3.4 y 4.1.3.5. | Ninguno. | Firme |
| 7 | RT-16.11 | Flujos con estados, escalamiento y delegación. | SD4 4.1.3.4 y 4.1.17. | Ninguno. | Firme |
| 8 | RT-16.12 | Flujos configurables sin desarrollo (responsables, plazos, niveles). | SD4 4.1.3.4. | Ninguno. | Firme |
| 9 | RF-17.07 | Bandeja de tareas unificada por persona. | SD4 4.1.3.1 y 4.1.3.5. | Ninguno. | Firme |
| 10 | RT-16.13 | Lo mismo que RF-17.07. | SD4 4.1.3.1 y 4.1.3.5. | Ninguno. | Firme |
| 11 | RT-16.14 | Motor de reglas sin recompilar, con trazabilidad por transacción. | SD4 4.1.3.4 (ExpressionLanguage). | Ninguno. La parte del caso sobre prueba de entrega y guía sí la cubren 3.3.2 y 3.4.8. | Firme |
| 12 | RF-17.08 | Gestión documental: versiones, metadatos, búsqueda y vista previa. | SD4 4.1.6.2 (repositorio S3). | 3.4.8 guarda la evidencia de entrega, pero no la gestión documental general. | Firme |
| 13 | RT-16.15 | Lo mismo que RF-17.08. | SD4 4.1.6.2. | 3.4.8, parcial. | Firme |
| 14 | RF-17.11 | Búsqueda global con texto completo y facetas. | SD4 4.1.3.1. | Ninguno. | Firme |
| 15 | RT-16.27 | Lo mismo que RF-17.11. | SD4 4.1.3.1. | Ninguno. | Firme |
| 16 | RT-05.22 | Carga y descarga masiva con validación y error por registro. | SD4 4.1.3.5 y Anexo 4-C. | 3.7.2 carga maestros una vez en la migración; no es la función permanente. | Firme |
| 17 | RF-17.09 | Documentos desde plantillas administrables. | SD4 4.1.6.2. | 3.6.4: el T-12 dice que reutiliza las plantillas de avisos. | Defendible |
| 18 | RT-16.19 | Lo mismo que RF-17.09. | SD4 4.1.6.2. | 3.6.4. | Defendible |
| 19 | RF-17.12 | Listados ordenables, filtrables y exportables. | SD4 4.1.3.1. | Cada paquete de módulo (3.4.x y 3.5.x) construye sus pantallas. | Defendible |
| 20 | RT-16.28 | Lo mismo que RF-17.12. | SD4 4.1.3.1. | 3.4.x y 3.5.x. | Defendible |
| 21 | RNF-17.02 | Exportaciones grandes asíncronas, con aviso al terminar. | SD4 4.1.4.7 y SD5 5.2.8. | 3.6.4 da el aviso; el trabajo asíncrono no tiene paquete. | Defendible |
| 22 | RT-16.29 | Lo mismo que RNF-17.02. | SD5 5.2.8. | 3.6.4, parcial. | Defendible |
| 23 | RNF-23.04 | Estaciones de operación con monitores duales, NCh 2527 y gestión central. | T-11, fila «Estación de trabajo» (8 nuevas: Talca 5, Concepción 3). | 5.1.1 es solo equipamiento de terreno; 5.1.2 es sala, racks y servidores. | Firme |
| 24 | RT-08.07 | Especificar las estaciones de trabajo con monitores duales. | T-11 y SD4 4.2.1.1 (Tabla 7). | Ninguno. | Firme |
| 25 | RT-08.08 | Ergonomía NCh 2527 y eficiencia energética. | T-11. | Ninguno. | Firme |

Resultado: 19 brechas firmes y 6 defendibles. Las 22 primeras son funciones comunes que SD4 diseña y T-12 declara «Cumple», pero que ningún paquete construye ni estima en HH: es una omisión del T-14 y probablemente también del esfuerzo del T-15. Las tres últimas son un ítem del T-11 sin paquete de compra ni de instalación; el T-11 tampoco dice si las compra LafroX o el CLIENTE.

### Indirectos que conviene precisar en el diccionario

No impiden llenar la columna, pero un evaluador podría preguntar dónde está el trabajo.

| Observación | Filas |
|---|---|
| Retención por dominio: no hay paquete de política de retención; la sostiene el respaldo inmutable. | RNF-01.02, RNF-08.02, RNF-09.02 |
| Ventana de 30 minutos de la cadena; la planifica M4, que no tiene paquete de Etapa 2. | RF-12.10, RF-12.11 |
| Evidencia y acuse al canal moderno; los ejecuta M6, que no tiene paquete de Etapa 2. | RF-12.12, RF-12.13 |
| Registro ADR: no figura como entregable explícito. | RF-13.03, RT-02.04 |
| Superficie de exposición: se declara en la arquitectura física. | RF-14.03-BTT, RF-19.03 |
| 3.3.5 nombra stock, lotes y cobros; el requisito abarca toda operación. | RF-17.04, RF-17.05 |
| Endurecimiento CIS: no figura como entregable explícito. | RNF-13.06, RT-03.15 |
| Cálculo de capacidad: parte del documento de arquitectura física. | RNF-19.01, RNF-19.03 |
| 1.9.4 solo nombra ISO/IEC 27001. | RT-15.07, RT-15.09 |
| Bandeja de pagos del portal (Etapa 2); M7 no tiene paquete de Etapa 2. | RF-07.08 |
| Reportes ejecutivos programados (Etapa 2); 3.5.4 solo nombra el costo de servir. | RF-11.01 |
| Portal público con catálogo: 3.5.2 nombra el portal de clientes, no el público. | RF-12.14 |
| Portal público con catálogo: 3.5.2 nombra el portal de clientes, no el público; el T-12 cita su prueba en 3.8. | RF-17.13 |
| Firma electrónica: la aplica el ERP en la guía y la app en la evidencia. | RF-18.01 |
| Cálculo de ancho de banda: parte del documento de arquitectura física. | RNF-13.08 |
| Los dos ensayos de migración no figuran como entregable. | RT-05.13 |
| Presupuesto de error: no figura como entregable explícito. | RT-10.09 |
| OWASP SAMM: no figura como entregable explícito. | RT-11.28 |
| Portal público: sin paquete de construcción propio; el T-12 cita sus pruebas en 3.8 y 3.9. | RT-16.31 |
| Definición de terminado: no figura como entregable explícito. | RT-20.07 |

## Paquetes sin requerimiento asignado

49 de los 222 paquetes no reciben ninguna fila del T-12. No es un defecto: la EDT contiene el 100 % del trabajo, y la dirección del proyecto, los hitos de aceptación, la gestión del cambio, las innovaciones y el cierre no nacen de un requerimiento técnico. Los paquetes de innovación se trazan a sus fichas del T-19, no al T-12.

| Paquete | Nombre |
|---|---|
| 1.1.1 | Acta de constitución del proyecto, firmada con la Contraparte Técnica |
| 1.1.2 | Documento de validación con el CLIENTE de los problemas y metas del proyecto |
| 1.1.3 | Acta de confirmación con el CLIENTE de la fecha de inicio, la evidencia para el proveedor de lácteos, las… |
| 1.2.1 | Documento de especificación de requerimientos y línea base de alcance de la Etapa 1 (H1) |
| 1.2.2 | Documento de reglas de ruteo capturadas al planificador de rutas |
| 1.2.3 | Documento de especificación de las interfaces sin documentación del ERP, del WMS de 2013 y de la telemetría… |
| 1.2.5 | Documento de línea base de alcance de la Etapa 2: canal moderno y costo de servir (H8) |
| 1.3.2 | EDT y diccionario de la EDT (línea base del alcance) |
| 1.3.3 | Carta Gantt de 56 meses con los hitos H1 a H12 y la ruta crítica |
| 1.3.4 | Documento de nivelación de recursos y frentes del solapamiento de los meses 13 a 15 y 19 a 20 |
| 1.3.5 | Reunión semanal de seguimiento con su informe semanal |
| 1.4.1 | Registro de interesados con su influencia, interés y estrategia |
| 1.4.2 | Plan de comunicaciones con calendario y canales por grupo de interés |
| 1.7.2 | Primera actualización anual del Plan de Reversibilidad durante la implementación |
| 1.9.5 | Garantía de fiel cumplimiento, seguros y certificados laborales vigentes durante el contrato |
| 2.3.3 | Plano de los gabinetes de borde de Concepción y de las plataformas de cross-docking |
| 2.4.1 | Acta de aprobación de la arquitectura, el plan de seguridad y el modelo de datos (H2) |
| 2.4.2 | Acta de aprobación del diseño detallado de la Etapa 2 (H8) |
| 3.8.1 | Pruebas de integración, regresión e idempotencia en QA (H4) |
| 3.9.1 | Pruebas de integración y regresión sin afectar la Etapa 1 en producción (H9) |
| 3.10.1.1 | Innovación 1: documento de catálogo de acciones y protocolo del piloto (INN-01.P1) |
| 3.10.1.2 | Innovación 1: estimador de saldo y ritmo de reposición (INN-01.P2) |
| 3.10.1.3 | Innovación 1: función de lista sin conexión en la aplicación de preventa (INN-01.P3) |
| 3.10.2.1 | Innovación 2: informe de medición inicial y contrato de evidencia (INN-02.P1) |
| 3.10.2.3 | Innovación 2: captura de evidencia en las aplicaciones de preventa, preparación y reparto (INN-02.P3) |
| 3.10.4.1 | Innovación 5: prototipo e informe de la prueba de comprensión (INN-05.P1) |
| 3.10.4.2 | Innovación 5: evaluación de privacidad y diseño de la impresión en cabina (INN-05.P2) |
| 3.10.4.3 | Innovación 5: cálculo y bloques 1 a 3 de la hoja de negocio (INN-05.P3) |
| 3.11.2 | Base de conocimiento de incidentes y decisiones de diseño |
| 3.11.5 | Depósito del código fuente en el repositorio del CLIENTE en cada liberación |
| 4.3.4 | Garantía de correcto funcionamiento constituida, condición de la aceptación final (H12) |
| 5.2.3 | Licencias de software de terceros constituidas a nombre del CLIENTE |
| 5.4.1 | Acuerdos operacionales firmados con los diez transportistas |
| 5.4.4 | Contrato de custodia de fuentes con un tercero independiente |
| 6.1.5 | Acta de recepción técnica de la sala |
| 7.2.1 | Acompañamiento del personal con 20 o 30 años en la compañía |
| 7.2.2 | Gestión del cambio con las cadenas y los transportistas |
| 7.2.3 | Diagnóstico del impacto organizacional por área y perfil, con agentes de cambio |
| 7.2.4 | Procedimientos operativos afectados, rediseñados y documentados |
| 7.2.5 | Medición de la adopción y plan de acción correctiva |
| 7.3.2 | Certificación de Comercial y Finanzas en costo de servir (Etapa 2) |
| 8.1.4 | Actualizaciones anuales del Plan de Reversibilidad durante los 36 meses de operación |
| 8.3.1 | Innovación 2: mantenimiento de escenarios de regresión (INN-02.P4, segunda parte) |
| 8.3.3 | Innovación 4: línea base y liquidaciones en sombra (INN-04.P2) |
| 8.3.4 | Innovación 4: liquidación mensual del tramo variable, meses 24 a 56 (INN-04.P3) |
| 8.3.5 | Innovación 5: despliegue gradual por rutas (INN-05.P4, segunda parte) |
| 8.3.6 | Innovación 5: bloque 4 condicionado (INN-05.P5) |
| 8.4.4 | Actualizaciones semestrales del depósito de custodia de fuentes durante los 36 meses de operación |
| 9.1.2 | Informe de lecciones aprendidas y archivo de la implementación |

## Cobertura por cuenta de control

| Cuenta | Paquetes | Con filas del T-12 | Filas asignadas |
|---|---:|---:|---:|
| 1.1 | 3 | 0 | 0 |
| 1.2 | 5 | 1 | 1 |
| 1.3 | 5 | 1 | 1 |
| 1.4 | 3 | 1 | 1 |
| 1.5 | 2 | 2 | 3 |
| 1.6 | 2 | 2 | 2 |
| 1.7 | 2 | 1 | 1 |
| 1.8 | 8 | 8 | 12 |
| 1.9 | 5 | 4 | 6 |
| 2.1 | 4 | 4 | 42 |
| 2.2 | 4 | 4 | 21 |
| 2.3 | 3 | 2 | 8 |
| 2.4 | 2 | 0 | 0 |
| 2.5 | 2 | 2 | 13 |
| 2.6 | 3 | 3 | 11 |
| 3.1 | 5 | 5 | 44 |
| 3.2 | 6 | 6 | 52 |
| 3.3 | 6 | 6 | 65 |
| 3.4 | 11 | 11 | 135 |
| 3.5 | 4 | 4 | 47 |
| 3.6 | 6 | 6 | 30 |
| 3.7 | 5 | 5 | 8 |
| 3.8 | 8 | 7 | 19 |
| 3.9 | 7 | 6 | 13 |
| 3.10 | 16 | 8 | 5 |
| 3.11 | 5 | 3 | 8 |
| 4.1 | 3 | 3 | 2 |
| 4.2 | 3 | 3 | 5 |
| 4.3 | 4 | 3 | 5 |
| 5.1 | 3 | 3 | 11 |
| 5.2 | 3 | 2 | 5 |
| 5.3 | 3 | 3 | 1 |
| 5.4 | 4 | 2 | 2 |
| 6.1 | 5 | 4 | 16 |
| 6.2 | 3 | 3 | 5 |
| 6.3 | 4 | 4 | 8 |
| 6.4 | 3 | 3 | 10 |
| 6.5 | 6 | 6 | 4 |
| 6.6 | 3 | 3 | 9 |
| 7.1 | 6 | 6 | 14 |
| 7.2 | 5 | 0 | 0 |
| 7.3 | 2 | 1 | 2 |
| 8.1 | 6 | 5 | 36 |
| 8.2 | 7 | 7 | 23 |
| 8.3 | 6 | 1 | 2 |
| 8.4 | 4 | 3 | 11 |
| 8.5 | 3 | 3 | 7 |
| 9.1 | 2 | 1 | 1 |
| 9.2 | 2 | 2 | 3 |

## Mapeo completo — Parte A (RF y RNF)

| ID | Requerimiento (resumen) | Paquete(s) del T-14 | Cobertura | Observación |
|---|---|---|---|---|
| RF-01.01 | El sistema debe registrar la recepción física de un proveedor validando las cantidades… | 3.4.1 | Directo |  |
| RF-01.02 | El sistema debe exigir el número de lote del proveedor en campo estructurado para todo… | 3.4.1 | Directo |  |
| RF-01.03 | El sistema debe registrar la fecha de vencimiento en formato DD/MM/AAAA para todo SKU con… | 3.4.1 | Directo |  |
| RF-01.04 | El sistema debe permitir registrar una no conformidad durante la recepción seleccionando… | 3.4.1 | Directo |  |
| RF-01.05 | Al confirmar una no conformidad, el sistema debe cambiar automáticamente a estado… | 3.4.1 | Directo |  |
| RF-01.06 | El sistema debe decodificar códigos de barras GS1 interpretando los AIs 01 (GTIN), 10… | 3.4.1 | Directo |  |
| RF-01.07 | Al finalizar el registro de un pallet, el sistema debe generar automáticamente un SSCC… | 3.4.1 | Directo |  |
| RF-01.08 | El sistema debe permitir asociar un SSCC a una dirección de almacenamiento… | 3.4.1 | Directo |  |
| RF-01.09 | Al cerrar una recepción, el sistema debe enviar automáticamente la transacción de ingreso… | 3.4.1 | Directo |  |
| RF-01.10 | El sistema debe permitir crear y mantener fichas de producto con atributos obligatorios… | 3.4.1, 3.7.2 | Directo |  |
| RF-01.11 | El sistema debe validar la compatibilidad térmica entre el tipo de almacenamiento del SKU… | 3.4.2 | Directo |  |
| RF-02.01 | El sistema debe permitir registrar y configurar cada instalación de la red logística… | 3.4.2 | Directo |  |
| RF-02.02 | El sistema debe consolidar el stock físico en unidades de cada SKU en todos los nodos de… | 3.4.2 | Directo |  |
| RF-02.03 | El sistema debe calcular periódicamente una propuesta de reasignación de ubicaciones… | 3.4.2 | Directo |  |
| RF-02.04 | El sistema debe generar un plan de conteo cíclico mensual que cubra una cantidad de… | 3.4.2 | Directo |  |
| RF-02.05 | El sistema debe calcular el stock disponible para venta por SKU y por centro de… | 3.4.2 | Directo |  |
| RF-02.06 | El sistema debe registrar como «en tránsito» todo inventario despachado desde un nodo de… | 3.4.2 | Directo |  |
| RF-02.07 | El sistema debe permitir consultar el nivel de ocupación de cada centro de distribución… | 3.4.2 | Directo |  |
| RF-02.08 | El sistema debe dirigir la preparación de pedidos (picking) asignando tareas de… | 3.4.2 | Directo |  |
| RF-02.09 | El sistema debe gestionar el almacenamiento de productos con fecha de vencimiento… | 3.4.2 | Directo |  |
| RF-02.10 | El sistema debe proveer una interfaz de trazabilidad que permita buscar y detallar el… | 3.4.4 | Directo |  |
| RF-02.11 | El sistema debe registrar en cada plataforma de cross-docking la lectura de las unidades… | 3.4.2 | Directo |  |
| RF-03.01 | La app debe mostrar, con conectividad, el stock disponible en tiempo real para cada SKU… | 3.4.6 | Directo |  |
| RF-03.02 | La app debe mostrar, sin conectividad, el stock según la última sincronización válida… | 3.4.6 | Directo |  |
| RF-03.03 | El sistema debe reservar el stock comprometido en el momento de la confirmación del… | 3.4.6 | Directo |  |
| RF-03.04 | La app debe mostrar, con conectividad, el crédito disponible y la deuda vencida del… | 3.4.6 | Directo |  |
| RF-03.05 | La app debe mostrar, sin conectividad, el crédito y la deuda según la última… | 3.4.6 | Directo |  |
| RF-03.06 | La app debe mostrar el historial de compra del cliente (productos y frecuencia). | 3.4.6 | Directo |  |
| RF-03.07 | La app debe permitir aplicar una promoción vigente (3x2, descuento por volumen) a una… | 3.4.6 | Directo |  |
| RF-03.08 | El sistema debe alertar al preventista cuando el pedido, sumado a la deuda vencida… | 3.4.6 | Directo |  |
| RF-03.09 | El sistema debe bloquear el envío del pedido cuando este, sumado a la deuda vencida… | 3.4.6 | Directo |  |
| RF-03.10 | El sistema debe permitir que un supervisor autorice, de forma registrada, el envío de un… | 3.4.6 | Directo |  |
| RF-03.11 | El sistema debe registrar y conservar en cada pedido de preventa el precio acordado por… | 3.4.6 | Directo |  |
| RF-03.12 | El sistema debe generar una alerta al responsable comercial cuando el importe calculado… | 3.4.6 | Directo |  |
| RF-03.13 | El sistema debe informar al preventista la fecha y ventana horaria de entrega que puede… | 3.4.6 | Directo |  |
| RF-03.14 | El sistema debe generar sugerencias de productos usando historial de compra, frecuencia… | 3.4.6 | Directo |  |
| RF-03.15 | La app debe generar un identificador único en el dispositivo al crear un pedido sin… | 3.4.6 | Directo |  |
| RF-03.16 | El sistema debe detectar y descartar automáticamente los reenvíos duplicados de un pedido… | 3.4.6 | Directo |  |
| RF-04.01 | El sistema debe asignar pedidos a la flota, secuenciando la ruta en función de la… | 3.4.7, 3.6.3 | Directo |  |
| RF-04.02 | El sistema debe permitir modificar manualmente la secuencia de ruta y reasignar pedidos… | 3.4.7, 3.6.3 | Directo |  |
| RF-04.03 | El sistema debe bloquear la adición de líneas de pedido a una ruta si la sumatoria excede… | 3.4.7, 3.6.3 | Directo |  |
| RF-04.04 | El sistema debe permitir la configuración de ventanas horarias específicas por cliente y… | 3.4.7, 3.6.3 | Directo |  |
| RF-04.05 | El sistema debe restringir la asignación de pedidos refrigerados o congelados… | 3.4.7, 3.6.3 | Directo |  |
| RF-04.06 | El sistema debe crear un aviso al contacto del cliente con la hora estimada de llegada… | 3.4.7 | Directo |  |
| RF-04.07 | El sistema debe permitir parametrizar franjas horarias de recepción en la ficha maestra… | 3.4.7 | Directo |  |
| RF-04.08 | El sistema debe calcular el costo de cada entrega tras haber sido realizada. | 3.5.4, 3.4.7 | Directo | Costo de cada entrega (Etapa 2). |
| RF-05.01 | El jefe de bodega debe poder iniciar la generación manualmente o configurar la generación… | 3.4.3 | Directo |  |
| RF-05.02 | El sistema debe exigir la validación de cada línea recolectada escaneando el código GS1.… | 3.4.3 | Directo |  |
| RF-05.03 | El sistema debe exigir la selección obligatoria de un motivo parametrizable de una lista… | 3.4.3 | Directo |  |
| RF-05.04 | El sistema debe secuenciar las líneas de la misión de preparación priorizando las zonas… | 3.4.3 | Directo |  |
| RF-05.05 | El sistema debe asignar el inventario para la preparación de pedidos aplicando… | 3.4.3 | Directo |  |
| RF-05.06 | El sistema debe enviar al ERP, al cerrar una misión de preparación, el detalle… | 3.4.3 | Directo |  |
| RF-05.07 | El sistema debe dirigir la carga de pedidos preparados en el camión siguiendo la… | 3.4.3 | Directo |  |
| RF-06.01 | El sistema debe permitir marcar la recepción conforme de bultos mediante validación por… | 3.4.8 | Directo |  |
| RF-06.02 | El sistema debe permitir capturar la firma digital del receptor como evidencia de… | 3.4.8 | Directo |  |
| RF-06.03 | El sistema debe permitir reportar un rechazo total o parcial seleccionando la cantidad y… | 3.4.8 | Directo |  |
| RF-06.04 | El sistema debe permitir reportar un local cerrado, indicando la dirección del cliente. | 3.4.8 | Directo |  |
| RF-06.05 | El sistema debe permitir digitar el monto exacto recaudado en pagos realizados en efectivo | 3.4.10 | Directo |  |
| RF-06.06 | El sistema debe registrar la hora real de llegada y de término de cada entrega. | 3.4.8 | Directo |  |
| RF-06.07 | El sistema debe sincronizarse automaticamente, al detectar la reconexión de señal o el… | 3.4.8 | Directo |  |
| RF-06.08 | El sistema debe permitir al conductor de una empresa externa iniciar su jornada usando… | 3.4.8, 7.1.3 | Directo |  |
| RF-06.09 | Al registrar una entrega, el sistema debe permitir al conductor capturar la cantidad de… | 3.4.9 | Directo |  |
| RF-06.10 | El sistema debe actualizar el saldo del cliente y del parque retornable en línea o en… | 3.4.9 | Directo |  |
| RF-06.11 | El sistema debe ofrecer al cliente la opción de confirmar la recepción mediante un código… | 3.4.8 | Directo |  |
| RF-06.12 | El sistema debe permitir confirmar la recepción del cliente aun si este no dispone de… | 3.4.8 | Directo |  |
| RF-06.13 | La app de reparto debe permitir imprimir en terreno un comprobante térmico de entrega… | 3.4.8 | Directo |  |
| RF-06.14 | El sistema debe enviar al ERP, para cada guía de despacho electrónica, la evidencia de… | 3.4.8 | Directo |  |
| RF-07.01 | El sistema debe calcular para cada camión y turno el monto esperado de rendición a partir… | 3.4.10 | Directo |  |
| RF-07.02 | El sistema debe generar la planilla digital de rendición individual al retorno del… | 3.4.10 | Directo |  |
| RF-07.03 | El sistema debe obligar al registro estructurado y categorizado de causales para… | 3.4.10 | Directo |  |
| RF-07.04 | El sistema debe proveer una consola de gestión para la cartera de crédito a 30 días… | 3.4.10 | Directo |  |
| RF-07.05 | El sistema debe notificar en la aplicación móvil de preventa el estado de bloqueo o mora… | 3.4.6 | Directo |  |
| RF-07.06 | El sistema debe integrarse vía Bluetooth con terminales de pago portátil (POS) en la… | 3.4.10, 3.6.2 | Directo |  |
| RF-07.07 | El sistema debe disponer en el portal web de autoatención el estado de cuenta y la… | 3.5.2 | Directo |  |
| RF-07.08 | El sistema debe proveer una bandeja de validación para pagos reportados en el portal web… | 3.5.2, 3.4.10 | Indirecto | Bandeja de pagos del portal (Etapa 2); M7 no tiene paquete de Etapa 2. |
| RF-07.09 | El sistema debe transferir de forma estructurada, asíncrona e idempotente los… | 3.4.10 | Directo |  |
| RF-07.10 | El sistema debe permitir el registro de anticipos o pagos parciales en entregas al… | 3.4.10 | Directo |  |
| RF-07.11 | El sistema debe permitir al preventista registrar la cobranza en efectivo de facturas… | 3.4.6 | Directo |  |
| RF-08.01 | El sistema debe permitir al conductor registrar la devolución de productos en el momento… | 3.4.9 | Directo |  |
| RF-08.02 | Al recepcionar una devolución en el andén del CD, el sistema debe permitir seleccionar el… | 3.4.9 | Directo |  |
| RF-08.03 | El sistema debe mantener una cuenta corriente de envases retornables por cliente… | 3.4.9 | Directo |  |
| RF-08.04 | El sistema debe generar una alerta al preventista cuando el saldo de envases retornables… | 3.4.9 | Directo |  |
| RF-08.05 | El sistema debe permitir registrar mermas por vencimiento detectadas en conteo cíclico… | 3.4.2 | Directo |  |
| RF-08.06 | El sistema debe reportar la pérdida de envases retornables desglosada por cliente, tipo… | 3.4.9 | Directo |  |
| RF-08.07 | El sistema debe incluir el costo de devoluciones y mermas por cliente como componente del… | 3.5.4, 3.4.9 | Directo | Costo de devoluciones y mermas en el costo de servir. |
| RF-09.01 | El sistema debe permitir la trazabilidad 'hacia adelante' (forward tracing): dado un lote… | 3.4.4 | Directo |  |
| RF-09.02 | El sistema debe permitir la trazabilidad 'hacia atrás' (backward tracing): dado un… | 3.4.4 | Directo |  |
| RF-09.03 | El sistema debe registrar de forma automática y continua la temperatura de las cámaras de… | 3.4.4 | Directo |  |
| RF-09.04 | El sistema debe registrar de forma automática y continua la temperatura en los camiones… | 3.4.4 | Directo |  |
| RF-09.05 | El sistema debe generar una alerta en tiempo real (notificación en cabina y en plataforma… | 3.4.4 | Directo |  |
| RF-09.06 | Ante una excursión térmica crítica y sostenida, el sistema debe bloquear preventivamente… | 3.4.4 | Directo |  |
| RF-09.07 | El sistema debe permitir al conductor registrar el rechazo de un producto entregado por… | 3.4.4 | Directo |  |
| RF-09.08 | El sistema debe registrar, en el momento de la preparación (picking), el lote específico… | 3.4.3 | Directo |  |
| RF-09.09 | El sistema debe generar la evidencia de cumplimiento de cadena de frío exigible ante la… | 3.4.4 | Directo |  |
| RF-09.10 | El sistema debe permitir parametrizar por tipo de producto la regla de excursión térmica… | 3.4.4 | Directo |  |
| RF-10.01 | El sistema debe sugerir la reposición de compras por SKU y proveedor a partir de la… | 3.4.2 | Directo |  |
| RF-10.02 | El sistema debe incorporar al cálculo de reposición las promociones comprometidas. | 3.4.2 | Directo |  |
| RF-10.03 | El sistema debe traspasar la sugerencia aprobada al módulo de compras del ERP. | 3.4.2, 3.3.2 | Directo |  |
| RF-11.01 | El sistema debe programar y distribuir vía correo electrónico reportes ejecutivos… | 3.5.4, 3.4.11 | Indirecto | Reportes ejecutivos programados (Etapa 2); 3.5.4 solo nombra el costo de servir. |
| RF-11.02 | El sistema debe calcular el Costo de Servir real por entrega y por cliente, imputando los… | 3.5.4 | Directo |  |
| RF-11.03 | El sistema debe calcular diariamente el indicador OTIF por cliente, ruta, zona y total… | 3.4.11 | Directo |  |
| RF-11.04 | El sistema debe calcular automáticamente el Fill Rate (unidades entregadas vs. pedidas) y… | 3.4.11 | Directo |  |
| RF-11.05 | El sistema debe calcular diariamente la utilización de capacidad volumétrica (m^3) y de… | 3.4.11 | Directo |  |
| RF-11.06 | El sistema debe proveer un Tablero de Control Operacional en tiempo real que consolide el… | 3.4.11 | Directo |  |
| RF-11.07 | El sistema debe procesar automáticamente la liquidación y cierre comercial individual por… | 3.4.11 | Directo |  |
| RF-11.08 | El sistema debe segmentar mensualmente la cartera de clientes en matrices de rentabilidad… | 3.5.4 | Directo |  |
| RF-12.01 | El sistema debe recibir el mensaje de pedido electrónico estructurado (EDI/EDIFACT/XML… | 3.5.1, 3.6.5, 2.1.4 | Directo |  |
| RF-12.02 | El sistema debe validar automáticamente el pedido EDI recibido, verificando estructura… | 3.5.1, 3.6.5, 2.1.4 | Directo |  |
| RF-12.03 | El sistema debe resolver el código de producto informado por la cadena contra el maestro… | 3.5.1, 3.6.5, 2.1.4 | Directo |  |
| RF-12.04 | El sistema debe registrar automáticamente, sin digitación manual, el pedido EDI válido… | 3.5.1, 3.6.5, 2.1.4 | Directo |  |
| RF-12.05 | El sistema debe poner a disposición del proceso de planificación de rutas todo pedido… | 3.5.1, 3.6.5, 2.1.4 | Directo |  |
| RF-12.06 | El sistema debe permitir gestionar, mediante una bandeja de excepciones, los pedidos que… | 3.5.1, 3.6.5, 2.1.4 | Directo |  |
| RF-12.07 | El sistema debe enviar a la cadena de origen una confirmación o rechazo del pedido… | 3.5.1, 3.6.5, 2.1.4 | Directo |  |
| RF-12.08 | El sistema debe mantener el historial de estados de cada pedido electrónico (recepción… | 3.5.1, 3.6.5, 2.1.4 | Directo |  |
| RF-12.09 | El sistema debe generar y enviar al cliente del canal moderno un ASN cuando su pedido… | 3.5.1, 3.6.5, 2.1.4 | Directo |  |
| RF-12.10 | El sistema debe planificar la llegada del camión al cliente del canal moderno dentro de… | 3.5.1, 3.4.7 | Indirecto | Ventana de 30 minutos de la cadena; la planifica M4, que no tiene paquete de Etapa 2. |
| RF-12.11 | El sistema debe registrar el cumplimiento o incumplimiento de la ventana de 30 minutos… | 3.5.1, 3.4.7 | Indirecto | Ventana de 30 minutos de la cadena; la planifica M4, que no tiene paquete de Etapa 2. |
| RF-12.12 | El sistema debe capturar evidencia de entrega en el local del cliente: firma en pantalla… | 3.5.1, 3.4.8 | Indirecto | Evidencia y acuse al canal moderno; los ejecuta M6, que no tiene paquete de Etapa 2. |
| RF-12.13 | El sistema debe enviar al cliente del canal moderno un acuse de recibo digital de la… | 3.5.1, 3.4.8 | Indirecto | Evidencia y acuse al canal moderno; los ejecuta M6, que no tiene paquete de Etapa 2. |
| RF-12.14 | El sistema debe publicar un portal web público, sin autenticación, con el catálogo… | 3.5.2 | Indirecto | Portal público con catálogo: 3.5.2 nombra el portal de clientes, no el público. |
| RF-12.15 | El portal autenticado de clientes debe permitir generar un pedido en autoservicio… | 3.5.2 | Directo |  |
| RF-12.16 | El portal de clientes debe permitir consultar el estado de sus entregas y la ventana de… | 3.5.2 | Directo |  |
| RF-12.17 | El portal de clientes debe permitir consultar y descargar sus documentos tributarios… | 3.5.2 | Directo |  |
| RF-12.18 | El portal de clientes debe permitir consultar el saldo y estado de cuenta del cliente… | 3.5.2 | Directo |  |
| RF-12.19 | El portal de transportistas debe permitir consultar las rutas asignadas a la empresa para… | 3.5.3 | Directo |  |
| RF-12.20 | El portal de transportistas debe permitir descargar la documentación de despacho de cada… | 3.5.3 | Directo |  |
| RF-12.21 | El portal debe permitir confirmar, antes de la ventana de despacho, qué conductor y… | 3.5.3 | Directo |  |
| RF-12.22 | El portal de proveedores debe permitir consultar, en modo de solo lectura, el estado de… | 3.5.1 | Directo | El paquete incluye el portal de proveedores. |
| RF-12.23 | El portal de proveedores debe permitir consultar, en modo de solo lectura, las… | 3.5.1 | Directo | El paquete incluye el portal de proveedores. |
| RF-12.24 | El portal de proveedores debe permitir consultar, en modo de solo lectura, sus… | 3.5.1 | Directo | El paquete incluye el portal de proveedores. |
| RF-12.25 | El portal debe permitir al cliente del canal moderno registrarse con su RUT de empresa… | 3.5.2, 3.3.1 | Directo |  |
| RF-12.26 | El portal debe permitir al cliente autenticarse con su correo y contraseña registrados. | 3.5.2, 3.3.1 | Directo |  |
| RF-12.27 | El portal debe permitir al cliente solicitar un enlace de restablecimiento de contraseña… | 3.5.2, 3.3.1 | Directo |  |
| RF-12.28 | El portal debe permitir al cliente cerrar su sesión de forma explícita, invalidando el… | 3.5.2, 3.3.1 | Directo |  |
| RF-12.29 | El portal debe cerrar automáticamente la sesión del cliente tras un período de… | 3.5.2, 3.3.1 | Directo |  |
| RF-12.30 | El portal debe permitir al cliente pagar los pedidos generados en autoservicio (RF-12.15)… | 3.5.2, 3.6.2 | Directo |  |
| RF-13.01 | El PROPONENTE debe declarar la arquitectura lógica de la solución organizada en las 8… | 2.1.1 | Directo |  |
| RF-13.02 | El PROPONENTE debe presentar una tabla de emplazamiento que asigne cada componente de la… | 2.1.2 | Directo |  |
| RF-13.03 | El PROPONENTE debe mantener un registro de decisiones de arquitectura (ADR) fechado, con… | 2.1.1, 1.8.4 | Indirecto | Registro ADR: no figura como entregable explícito. |
| RF-13.04 | El PROPONENTE debe presentar un modelo de dominio del negocio del caso, con las entidades… | 2.1.3 | Directo |  |
| RF-14.01 | El sistema debe integrarse con la plataforma de telemetría de terceros existente que… | 3.3.4 | Directo |  |
| RF-14.02 | El sistema debe mostrar en el mapa las rutas planificadas vs las rutas reales recorridas… | 3.4.5, 3.6.3 | Directo |  |
| RF-14.03 | El sistema debe generar una alerta cuando el camión se desvíe más de 3 km de la ruta… | 3.4.5 | Directo |  |
| RF-14.04 | El sistema debe integrar los datos de telemetría con el módulo de costo de servir… | 3.5.4, 3.4.5 | Directo |  |
| RF-14.05 | El sistema debe registrar qué conductor propio o de transportista externo está asociado a… | 3.4.5, 3.3.1 | Directo |  |
| RF-14.06 | El sistema debe permitir la gestión de geocercas zonas geográficas, para identificar… | 3.4.5 | Directo |  |
| RF-14.01-BTT | El sistema debe permitir clasificar la información del CLIENTE por nivel de sensibilidad… | 2.2.4 | Directo |  |
| RF-14.02-BTT | El PROPONENTE debe mantener una matriz de controles de seguridad trazable a ISO/IEC 27001… | 2.2.4 | Directo |  |
| RF-14.03-BTT | El PROPONENTE debe declarar la superficie de exposición completa de la solución: cada… | 2.1.2, 2.2.2 | Indirecto | Superficie de exposición: se declara en la arquitectura física. |
| RF-14.04-BTT | El PROPONENTE debe disponer de un plan de respuesta a incidentes de seguridad que defina… | 2.2.3 | Directo |  |
| RF-14.05-BTT | El sistema (o el equipo de seguridad del ADJUDICATARIO) debe notificar al CLIENTE… | 8.1.5, 2.2.3 | Directo |  |
| RF-15.01 | El sistema debe contar con una gestión de identidad centralizada, con federación mediante… | 3.3.1 | Directo |  |
| RF-15.02 | El sistema debe implementar inicio de sesión único para todos los módulos de la solución… | 3.3.1 | Directo |  |
| RF-15.03 | El sistema debe exigir autenticación multifactor para personas usuarias administradoras… | 3.3.1 | Directo |  |
| RF-15.04 | El sistema debe implementar control de acceso basado en roles, complementado con control… | 3.3.1 | Directo |  |
| RF-15.05 | El sistema debe automatizar el aprovisionamiento y desaprovisionamiento de cuentas… | 3.3.1 | Directo |  |
| RF-16.01 | El sistema debe implementar observabilidad unificada para nube y on-premise, con… | 3.1.5 | Directo |  |
| RF-16.02 | El CLIENTE debe disponer de acceso propio y permanente a los tableros operacionales y de… | 3.1.5 | Directo |  |
| RF-16.03 | El sistema debe implementar alertamiento basado en síntomas de negocio y no sólo en… | 3.1.5 | Directo |  |
| RF-16.04 | El sistema (o el equipo del ADJUDICATARIO) debe ejecutar un análisis de causa raíz… | 8.1.2 | Directo |  |
| RF-17.01 | El sistema debe disponer de un módulo de administración que permita al CLIENTE, sin… | 3.3.1 | Directo |  |
| RF-17.02 | El sistema debe permitir parametrizar reglas de negocio (umbrales, plazos, montos… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RF-17.03 | El sistema debe requerir aprobación de un segundo perfil para todo cambio de parámetro… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RF-17.04 | El sistema debe registrar toda operación que cree, modifique o elimine información, con… | 3.3.5 | Indirecto | 3.3.5 nombra stock, lotes y cobros; el requisito abarca toda operación. |
| RF-17.05 | El CLIENTE debe poder consultar y exportar la auditoría desde la interfaz, con filtros… | 3.3.5 | Indirecto | 3.3.5 nombra stock, lotes y cobros; el requisito abarca toda operación. |
| RF-17.06 | El sistema debe soportar flujos de trabajo con estados, transiciones, responsables… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RF-17.07 | El sistema debe proveer una bandeja de tareas unificada para cada persona usuaria, donde… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RF-17.08 | El sistema debe gestionar documentos con versionado, metadatos, control de acceso… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RF-17.09 | El sistema debe generar documentos a partir de plantillas administrables por el CLIENTE… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RF-17.10 | El sistema debe enviar notificaciones por al menos tres canales: correo electrónico… | 3.6.4 | Directo |  |
| RF-17.11 | El sistema debe disponer de búsqueda global con indexación de texto completo con… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RF-17.12 | El sistema debe presentar listados ordenables, filtrables, paginados y exportables en… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RF-17.13 | El sistema debe disponer de un portal público con la información que el caso determine… | 3.5.2, 3.8.2 | Indirecto | Portal público con catálogo: 3.5.2 nombra el portal de clientes, no el público; el T-12 cita su prueba en 3.8. |
| RF-18.01 | El sistema debe soportar firma electrónica conforme a la Ley N.º 19.799 (2002, art. 2… | 3.3.2, 3.4.8 | Indirecto | Firma electrónica: la aplica el ERP en la guía y la app en la evidencia. |
| RF-18.02 | Cada persona usuaria debe poder configurar sus preferencias de canal (correo, SMS… | 3.6.4 | Indirecto |  |
| RF-18.03 | El sistema debe enviar notificaciones de forma asíncrona, con reintento ante falla… | 3.6.4 | Directo |  |
| RF-19.01 | Clasificación de información por nivel de sensibilidad | 2.2.4 | Directo |  |
| RF-19.02 | Matriz de controles de seguridad trazable a ISO 27001/27002 | 2.2.4 | Directo |  |
| RF-19.03 | Declaración de superficie de exposición | 2.1.2, 2.2.2 | Indirecto | Superficie de exposición: se declara en la arquitectura física. |
| RF-19.04 | Plan de respuesta a incidentes de seguridad | 2.2.3 | Directo |  |
| RF-19.05 | Notificación de brecha de seguridad al CLIENTE | 8.1.5, 2.2.3 | Directo |  |
| RNF-01.01 | Tiempo de respuesta de registro de ítem en recepción. El tiempo de procesamiento para el… | 3.4.1, 3.3.6 | Directo |  |
| RNF-01.02 | Retención de registros de recepción. El sistema debe conservar los registros de recepción… | 3.2.4 | Indirecto | Retención por dominio: no hay paquete de política de retención; la sostiene el respaldo inmutable. |
| RNF-01.03 | Operación offline de recepción (24 horas). El sistema debe operar en modo desconectado… | 3.3.6 | Directo |  |
| RNF-02.01 | Operación offline del CD (24 horas). El sistema de gestión de almacén (inventario… | 3.3.6 | Directo |  |
| RNF-03.01 | Tiempo de respuesta de registro de línea de pedido. El tiempo para registrar una línea de… | 3.4.6 | Directo |  |
| RNF-03.02 | Tiempo de respuesta de consulta de stock y crédito con conectividad. El tiempo para… | 3.4.6, 3.2.2 | Directo |  |
| RNF-03.03 | Tiempo de respuesta de consulta de historial de compra. El tiempo para consultar el… | 3.4.6 | Directo |  |
| RNF-04.01 | Tiempo de generación de rutas diarias. El motor de ruteo debe procesar la asignación y… | 3.4.7 | Directo |  |
| RNF-05.01 | Latencia de confirmación de picking (≤ 1s). La confirmación de una línea de picking… | 3.4.3 | Directo |  |
| RNF-05.02 | Operabilidad con guantes a -22 °C. La interfaz de picking debe ser operable sin precisión… | 3.4.3, 3.8.3 | Directo |  |
| RNF-05.03 | Curva de aprendizaje (≤ 2 horas). Un nuevo operario de preparación, sin experiencia… | 7.1.2 | Directo |  |
| RNF-06.01 | Autonomía de reparto sin cobertura. El sistema debe persistir el 100% de los datos… | 3.3.6 | Directo |  |
| RNF-06.02 | Duración del acceso sin conexión por perfil | 3.3.6 | Directo |  |
| RNF-06.03 | Sincronización del dispositivo tras un turno sin señal en no más de 10 minutos. | 3.3.6 | Directo |  |
| RNF-07.01 | Tiempo de sincronización de cobranzas tras reconexión. El sistema debe sincronizar la… | 3.4.10 | Directo |  |
| RNF-07.02 | Cifrado de datos de pagos y comportamiento comercial. El sistema debe cifrar a nivel de… | 2.2.4, 3.6.2 | Indirecto |  |
| RNF-08.01 | Tiempo de registro de devoluciones en el andén. El registro de una devolución en el andén… | 3.4.9 | Directo |  |
| RNF-08.02 | Retención de registros de devoluciones y mermas. Los registros de devoluciones y mermas… | 3.2.4 | Indirecto | Retención por dominio: no hay paquete de política de retención; la sostiene el respaldo inmutable. |
| RNF-09.01 | Tiempo de obtención de clientes afectados por lote. El sistema tiene un tiempo de… | 3.4.4 | Directo |  |
| RNF-09.02 | Retención de registros sanitarios y de trazabilidad. El sistema debe conservar los… | 3.2.4 | Indirecto | Retención por dominio: no hay paquete de política de retención; la sostiene el respaldo inmutable. |
| RNF-09.03 | Auditoría de consultas y modificaciones de trazabilidad. El sistema debe registrar todas… | 3.3.5 | Directo |  |
| RNF-09.04 | Operación sin cobertura y sincronización en cámara de frío. El sistema debe funcionar Sin… | 3.3.6, 3.4.3 | Directo |  |
| RNF-09.05 | Frecuencia de registro de temperatura. Cada cámara y cada vehículo con frío registra… | 3.4.4, 6.5.3, 6.5.4 | Directo |  |
| RNF-11.01 | Latencia de indicadores operacionales del día. El sistema debe desplegar los indicadores… | 3.4.11, 3.2.3 | Directo |  |
| RNF-11.02 | Aislamiento del procesamiento analítico y transaccional. El sistema debe desacoplar el… | 3.4.11, 3.2.3 | Directo |  |
| RNF-11.03 | Cierre comercial del día | 3.4.11, 3.2.3 | Directo |  |
| RNF-11.04 | Latencia de los indicadores de gestión | 3.4.11, 3.2.3 | Directo |  |
| RNF-12.01 | Hito de producción del canal moderno. El portal de autoatención de clientes (RF-12.15 a… | 3.5.1, 3.5.2, 4.3.3 | Directo |  |
| RNF-12.02 | Configurabilidad de integración EDI para nuevas cadenas. El mecanismo de recepción EDI… | 3.6.6 | Directo |  |
| RNF-12.03 | Envío del acuse de recibo al canal moderno. El acuse de recibo digital de cada entrega a… | 3.5.1, 3.6.5 | Directo |  |
| RNF-13.01 | Disponibilidad del sitio on-premise durante corte de enlace (24h). El componente… | 3.3.6, 6.6.3 | Directo |  |
| RNF-13.02 | Declaración de funciones no disponibles en modo desconectado. El PROPONENTE debe declarar… | 3.3.6, 6.6.3 | Directo |  |
| RNF-13.03 | Redundancia de equipos on-premise críticos. Los equipos on-premise críticos deben ser… | 6.3.1, 6.3.3, 6.3.4 | Directo |  |
| RNF-13.04 | Tolerancia del almacenamiento local a la falla de un disco. El almacenamiento local debe… | 6.3.1, 6.3.3, 6.3.4 | Directo |  |
| RNF-13.05 | Declaración y justificación del nivel RAID. el PROPONENTE debe declarar el nivel RAID… | 6.3.1, 6.3.3, 6.3.4 | Directo |  |
| RNF-13.06 | Endurecimiento de sistemas on-premise según CIS Benchmarks. Los sistemas on-premise deben… | 6.6.1, 8.2.5 | Indirecto | Endurecimiento CIS: no figura como entregable explícito. |
| RNF-13.07 | Enlace redundante entre on-premise y nube. El enlace entre el sitio on-premise y la nube… | 6.6.2, 5.3.1, 5.3.2, 5.3.3 | Directo |  |
| RNF-13.08 | Dimensionamiento de ancho de banda por sitio. El PROPONENTE debe dimensionar el ancho de… | 2.1.2 | Indirecto | Cálculo de ancho de banda: parte del documento de arquitectura física. |
| RNF-13.09 | Estudio de cobertura de red inalámbrica en sitios operacionales (incluye cámaras de… | 6.2.3 | Directo |  |
| RNF-14.01 | Cifrado en tránsito con TLS 1.3. Todo el tráfico en tránsito debe emplear TLS 1.3, con… | 3.2.1, 3.2.5 | Indirecto |  |
| RNF-14.02 | Cifrado en reposo de todos los datos. La totalidad de los datos en reposo debe estar… | 3.2.5 | Indirecto |  |
| RNF-14.03 | Segregación de red en la nube (subredes privadas). En la nube, la red debe segmentarse… | 3.1.2 | Indirecto |  |
| RNF-14.04 | SIEM con casos de uso de detección específicos del negocio. Los eventos de seguridad… | 8.1.5, 3.2.5 | Directo |  |
| RNF-14.05 | Detección y respuesta en puntos finales (EDR). Se debe implementar detección y respuesta… | 3.2.5, 5.2.2 | Directo |  |
| RNF-14.06 | Pruebas de intrusión anuales por tercero independiente. Se deben ejecutar pruebas de… | 3.8.6, 3.9.5, 8.2.2 | Directo |  |
| RNF-14.07 | Análisis estático de código, SCA y escaneo de contenedores en CI/CD. El flujo de… | 3.1.4, 1.5.2 | Directo |  |
| RNF-14.08 | Inventario de componentes de software (SBOM) en formato CycloneDX/SPDX. Cada versión… | 3.11.4 | Directo |  |
| RNF-14.09 | Verificación de procedencia de artefactos según SLSA nivel 3. Los artefactos deben… | 3.1.4 | Indirecto |  |
| RNF-14.10 | Prohibición de datos productivos en ambientes no productivos. Queda prohibido el uso de… | 3.1.1 | Indirecto |  |
| RNF-14.11 | Privacidad de la geolocalización de personas. Hasta el acuerdo con el sindicato, la… | 5.4.2, 1.9.3 | Directo |  |
| RNF-14.12 | Categorías de datos personales en terreno. El 100 % de los campos con datos personales… | 1.9.3, 2.2.4 | Directo |  |
| RNF-15.01 | Política de sesión: duración, inactividad, renovación, revocación. El sistema debe… | 3.3.1 | Directo |  |
| RNF-15.02 | Credenciales de sesión firmadas y de vida breve. Las credenciales de sesión deben ser… | 3.3.1 | Directo |  |
| RNF-15.03 | Registro completo del ciclo de vida de la identidad (auditoría). El sistema debe… | 3.3.1 | Directo |  |
| RNF-16.01 | Indicadores de nivel de servicio medidos sobre experiencia real del usuario. Los… | 3.1.5 | Directo |  |
| RNF-16.02 | Libro de operación y guía de resolución documentados. El PROPONENTE debe documentar un… | 3.11.1, 8.1.1 | Directo |  |
| RNF-16.03 | Registros sin datos personales sensibles ni credenciales. Los registros (logs) de la… | 3.1.5 | Indirecto |  |
| RNF-17.01 | Retención de auditoría mínima de 5 años. El período de retención de la auditoría debe ser… | 3.3.5, 3.2.4 | Directo |  |
| RNF-17.02 | Exportaciones de gran volumen procesadas de forma asíncrona. Las exportaciones de gran… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RNF-17.03 | Portal público resistente a picos de tráfico. El portal público debe resistir picos de… | 3.2.1 | Directo |  |
| RNF-19.01 | Cálculo de capacidad con supuestos de usuarios concurrentes y TPS. El PROPONENTE debe… | 2.1.2, 8.4.1 | Indirecto | Cálculo de capacidad: parte del documento de arquitectura física. |
| RNF-19.02 | Escalamiento horizontal automático de capas de aplicación e integración. Las capas de… | 3.2.1 | Directo |  |
| RNF-19.03 | Identificación del cuello de botella al crecer la carga. El PROPONENTE debe identificar… | 2.1.2, 8.4.1 | Indirecto | Cálculo de capacidad: parte del documento de arquitectura física. |
| RNF-19.04 | Pruebas de carga en Preproducción con 1.5× peak y pruebas de estrés. Se deben ejecutar… | 3.8.4, 3.9.3 | Directo |  |
| RNF-20.01 | Disponibilidad mensual mínima del 99.9% para servicios críticos. La solución debe… | 8.1.2 | Directo |  |
| RNF-20.02 | Clasificación de servicios por criticidad (crítico, alto, medio, bajo). El PROPONENTE… | 2.5.1 | Indirecto |  |
| RNF-20.03 | Plan de continuidad del negocio conforme a ISO 22301. El PROPONENTE debe elaborar un plan… | 2.5.1 | Directo |  |
| RNF-20.04 | Pruebas de resiliencia con inyección de fallas. Se deben ejecutar pruebas de resiliencia… | 3.8.4, 3.9.3, 8.2.2 | Directo |  |
| RNF-20.05 | Documentación de comportamiento ante falla de dependencias externas. El PROPONENTE debe… | 2.5.2 | Indirecto |  |
| RNF-20.06 | Site secundario para DR: RTO ≤ 4h, RPO ≤ 15 min. El PROPONENTE debe habilitar un sitio… | 3.1.3, 2.5.2 | Directo |  |
| RNF-20.07 | Política de respaldo 3-2-1-1-0 (3 copias, 2 medios, 1 fuera de sitio, 1 inmutable, 0… | 3.2.4, 6.4.3 | Directo |  |
| RNF-21.01 | Centro de operaciones de red (NOC) 24×7×365. El ADJUDICATARIO debe disponer de un centro… | 8.1.1 | Directo |  |
| RNF-21.02 | Gerente de servicio dedicado para el CLIENTE. El ADJUDICATARIO debe designar un gerente… | 8.1.1 | Indirecto |  |
| RNF-21.03 | Centro de atención telefónica: 80% en 20 segundos, 70% resolución primer contacto. El… | 8.1.1 | Directo |  |
| RNF-21.04 | Horario de atención ampliado a 24×7 para incidentes críticos y ventana de despacho… | 8.1.1 | Directo |  |
| RNF-21.05 | Dimensionamiento de la dotación del centro de atención con teoría de colas o Erlang C. El… | 8.1.1 | Indirecto |  |
| RNF-21.06 | Canal único de registro de incidentes con ticket y seguimiento. Debe existir un canal… | 8.1.2 | Directo |  |
| RNF-21.07 | Traslado a sitios alejados (Curicó, Chillán, Los Ángeles) para resolución de incidentes.… | 8.2.3 | Directo |  |
| RNF-21.08 | Bolsa anual de horas de mantención evolutiva. El PROPONENTE debe declarar el tamaño de la… | 8.2.1 | Directo |  |
| RNF-21.09 | Planificación anual de actualizaciones de versiones de componentes. Las actualizaciones… | 8.2.5, 8.1.1 | Directo |  |
| RNF-22.01 | Plan de capacitación estructurado por perfil (usuarios, administradores, técnicos). El… | 7.1.1 | Directo |  |
| RNF-22.02 | Material de capacitación en español, editable y de propiedad del CLIENTE. Todo el… | 7.1.5 | Directo |  |
| RNF-22.03 | Capacitación sin afectar la operación: programación por turnos y horarios acordados. La… | 7.1.1, 7.1.2 | Directo |  |
| RNF-22.04 | Evaluación y certificación de usuarios administradores y equipo técnico. Las personas… | 7.1.4, 7.3.1 | Indirecto |  |
| RNF-22.05 | Capacitación de personal nuevo del CLIENTE sin costo adicional durante la Operación.… | 8.5.1 | Directo |  |
| RNF-22.06 | Acompañamiento y mentoría al equipo técnico del CLIENTE durante 6 meses post producción.… | 8.5.2 | Directo |  |
| RNF-23.01 | Especificación de hardware de terreno con marca, modelo, cantidad y características. El… | 5.1.1 | Directo |  |
| RNF-23.02 | Dispositivos con grado de protección IP y resistencia a caídas coherentes con el entorno.… | 5.1.1 | Directo |  |
| RNF-23.03 | Ciclo de vida esperado de cada dispositivo y plan de reposición durante 56 meses. El… | 5.1.1, 8.2.7 | Directo |  |
| RNF-23.04 | Estaciones de trabajo para operación y administración con monitores duales. El PROPONENTE… | — | Brecha | Estaciones de trabajo de operación: ningún paquete las especifica ni instala. |

## Mapeo completo — Parte B (RT)

| ID | Requerimiento (resumen) | Paquete(s) del T-14 | Cobertura | Observación |
|---|---|---|---|---|
| RT-02.01 | La solución se organizará en las ocho capas del numeral 2.1. El PROPONENTE presentará el… | 2.1.1 | Directo |  |
| RT-02.02 | La arquitectura será modular, con límites de contexto explícitos y acoplamiento débil. Se… | 2.1.1 | Directo |  |
| RT-02.03 | La descripción de la arquitectura se ajustará a ISO/IEC/IEEE 42010, con vistas lógica, de… | 2.1.1, 2.1.2 | Directo |  |
| RT-02.04 | El PROPONENTE mantendrá un registro de decisiones de arquitectura (ADR) fechado, con la… | 2.1.1, 1.8.4 | Indirecto | Registro ADR: no figura como entregable explícito. |
| RT-02.05 | La capa de servicios de negocio será sin estado. El estado de sesión y el estado de… | 2.1.1 | Indirecto |  |
| RT-02.06 | Toda operación de escritura expuesta a reintentos será idempotente, con clave de… | 3.3.6 | Indirecto |  |
| RT-02.07 | Los flujos de eventos garantizarán entrega al menos una vez, con deduplicación en el… | 3.2.2 | Indirecto |  |
| RT-02.08 | La solución implementará patrones de resiliencia demostrables: reintento con retroceso… | 2.1.1 | Indirecto |  |
| RT-02.09 | La solución degradará de forma elegante: ante la indisponibilidad de un componente no… | 3.3.6 | Indirecto |  |
| RT-02.10 | Las capas de aplicación e integración escalarán horizontalmente de forma automática, con… | 3.2.1 | Directo |  |
| RT-02.11 | El PROPONENTE declarará explícitamente los puntos únicos de falla que subsistan en su… | 2.1.2 | Indirecto |  |
| RT-02.12 | La solución admitirá su replicación a nuevas unidades, sitios, sucursales o filiales del… | 2.1.1 | Indirecto |  |
| RT-02.13 | El PROPONENTE presentará un modelo de dominio del negocio del caso, con las entidades… | 2.1.3 | Directo |  |
| RT-02.14 | Se valorará la aplicación documentada de patrones de arquitectura evolutiva que permitan… | 3.3.2, 3.3.3 | Directo |  |
| RT-03.01 | El PROPONENTE declarará el proveedor de nube pública, la región primaria y la región… | 5.2.1, 2.1.2 | Directo |  |
| RT-03.02 | Todos los componentes con requisito de alta disponibilidad se desplegarán en al menos dos… | 3.1.2 | Directo |  |
| RT-03.03 | La totalidad de la infraestructura se definirá como código, versionada en el repositorio… | 3.1.4 | Directo |  |
| RT-03.04 | La red se segmentará por capas, con subredes privadas para aplicación y datos, y… | 3.1.2 | Indirecto |  |
| RT-03.05 | El PROPONENTE privilegiará servicios administrados por sobre servicios autoadministrados… | 2.1.2 | Indirecto |  |
| RT-03.06 | Se aplicarán prácticas FinOps: etiquetado obligatorio de todos los recursos por ambiente… | 8.4.2 | Directo |  |
| RT-03.07 | El PROPONENTE declarará su estrategia de reversibilidad y de mitigación del bloqueo por… | 1.7.1 | Directo |  |
| RT-03.08 | La solución empleará instancias reservadas, planes de ahorro o capacidad comprometida… | 5.2.1 | Indirecto |  |
| RT-03.09 | Se valorará el uso de cómputo sin servidor o de contenedores administrados para las… | 3.2.1 | Indirecto |  |
| RT-03.10 | El componente on-premise operará de forma autónoma y degradada ante la pérdida total del… | 3.3.6, 6.6.3 | Directo |  |
| RT-03.11 | Durante la operación desconectada, la solución continuará registrando las transacciones… | 3.3.6 | Directo |  |
| RT-03.12 | Restablecido el enlace, la sincronización será automática, con reconciliación… | 3.3.6 | Directo |  |
| RT-03.13 | El PROPONENTE declarará qué funciones NO estarán disponibles en modo desconectado y qué… | 3.3.6 | Directo |  |
| RT-03.14 | Los equipos on-premise críticos serán redundantes. El almacenamiento local tolerará la… | 6.3.1, 6.3.3 | Directo |  |
| RT-03.15 | Los sistemas on-premise se endurecerán conforme a los CIS Benchmarks aplicables, con… | 6.6.1, 8.2.5 | Indirecto | Endurecimiento CIS: no figura como entregable explícito. |
| RT-03.16 | El monitoreo del componente on-premise se integrará a la misma plataforma de… | 3.1.5 | Directo |  |
| RT-03.17 | El enlace entre el sitio on-premise y la nube será redundante, con caminos físicos y… | 6.6.2 | Directo |  |
| RT-03.18 | Los dispositivos de borde y de terreno se administrarán de forma remota y centralizada… | 3.2.6 | Directo |  |
| RT-03.19 | Se valorará el procesamiento en el borde de las cargas que lo admitan —filtrado… | 6.5.3, 3.2.3 | Indirecto |  |
| RT-03.20 | El PROPONENTE dimensionará el ancho de banda requerido por sitio, en régimen normal y en… | 2.1.2 | Indirecto |  |
| RT-03.21 | La conexión entre la red del CLIENTE y la nube se establecerá mediante enlace privado… | 6.6.2 | Indirecto |  |
| RT-03.22 | El acceso remoto de las personas trabajadoras del CLIENTE, incluido el trabajo desde el… | 3.2.5, 3.3.1 | Indirecto |  |
| RT-03.23 | La red inalámbrica de los sitios operacionales, cuando el caso la requiera, contará con… | 6.2.3 | Directo |  |
| RT-03.24 | El PROPONENTE declarará la calidad de servicio y la priorización de tráfico aplicada a… | 6.6.2 | Indirecto |  |
| RT-04.01 | Los cinco ambientes del numeral 4.1 estarán habilitados y operativos como condición del… | 3.1.1, 3.1.2, 3.1.3 | Directo |  |
| RT-04.02 | Preproducción será equivalente a producción en topología, versiones de componentes y… | 3.1.2 | Directo |  |
| RT-04.03 | El código residirá en un sistema de control de versiones con ramas protegidas, revisión… | 3.1.4 | Directo |  |
| RT-04.04 | Existirá trazabilidad completa entre requerimiento, incidencia, cambio de código, prueba… | 1.2.4, 3.1.4 | Directo |  |
| RT-04.05 | El flujo de integración continua ejecutará, como mínimo: compilación, pruebas unitarias… | 3.1.4 | Directo |  |
| RT-04.06 | Los despliegues serán automatizados y reproducibles, con reversión automatizada y sin… | 3.1.4 | Directo |  |
| RT-04.07 | La estrategia de despliegue permitirá liberar sin interrupción del servicio: azul-verde… | 3.8.8, 3.9.7 | Directo |  |
| RT-04.08 | Toda configuración estará externalizada del artefacto y gestionada por ambiente. Un mismo… | 3.1.4 | Indirecto |  |
| RT-04.09 | Los secretos residirán en un gestor de secretos con rotación automática y auditoría de… | 3.2.5 | Indirecto |  |
| RT-04.10 | Las migraciones de esquema de base de datos serán versionadas, reversibles y ejecutadas… | 3.1.4 | Indirecto |  |
| RT-04.11 | La cobertura de pruebas automatizadas del código de lógica de negocio será de al menos 70… | 1.5.2 | Directo |  |
| RT-04.12 | El PROPONENTE declarará su frecuencia de despliegue objetivo, su tiempo desde el… | 3.1.4 | Indirecto |  |
| RT-04.13 | Los ambientes no productivos se apagarán o reducirán fuera del horario de uso, con el… | 3.1.1, 8.4.2 | Indirecto |  |
| RT-04.14 | Se valorará la existencia de ambientes efímeros por rama o por incidencia, creados y… | 3.10.2.2 | Indirecto |  |
| RT-05.01 | El PROPONENTE entregará el modelo de datos documentado y un diccionario de datos con el… | 2.1.3 | Directo |  |
| RT-05.02 | El PROPONENTE justificará la selección del paradigma y del motor de persistencia… | 2.1.3 | Indirecto |  |
| RT-05.03 | Toda operación de negocio será trazable: la solución permitirá reconstruir quién, qué… | 3.3.5 | Directo |  |
| RT-05.04 | La calidad de datos se gestionará conforme a ISO/IEC 25012, con validación en el punto de… | 3.7.1 | Indirecto |  |
| RT-05.05 | El almacenamiento transaccional y el analítico estarán separados. Ninguna consulta… | 3.2.3 | Directo |  |
| RT-05.06 | La solución permitirá exportar la totalidad de la información del CLIENTE en formatos… | 9.1.1, 9.2.1 | Indirecto |  |
| RT-05.07 | El PROPONENTE declarará la política de retención, archivado y eliminación por cada… | 2.1.3, 9.2.2 | Indirecto |  |
| RT-05.08 | Los datos personales se tratarán conforme al Artículo 85° de las Bases Administrativas… | 1.9.2, 1.9.3 | Directo |  |
| RT-05.09 | El PROPONENTE presentará una estrategia de gestión de datos maestros que evite la… | 3.7.2 | Indirecto |  |
| RT-05.10 | Se valorará la implementación de un catálogo de datos con linaje automatizado, que… | 2.1.3 | Indirecto |  |
| RT-05.11 | El PROPONENTE presentará un plan de migración con alcance, origen, volumen, reglas de… | 3.7.1, 3.7.2, 3.7.3, 3.7.4, 3.7.5 | Directo |  |
| RT-05.12 | La migración incluirá una etapa de perfilado y saneamiento previo, con informe de los… | 3.7.1 | Directo |  |
| RT-05.13 | Se ejecutarán al menos dos ensayos completos de migración sobre Preproducción antes de la… | 3.7.5 | Indirecto | Los dos ensayos de migración no figuran como entregable. |
| RT-05.14 | La conciliación posterior a la migración será cuantitativa y verificable: recuentos… | 3.7.5 | Directo |  |
| RT-05.15 | Los datos históricos que no se migren quedarán accesibles en un repositorio de consulta… | 3.7.3 | Indirecto |  |
| RT-05.16 | Los servicios síncronos se documentarán en OpenAPI 3.1 y los flujos dirigidos por eventos… | 3.11.3 | Directo |  |
| RT-05.17 | Los contratos de interfaz se versionarán semánticamente, con compatibilidad hacia atrás y… | 3.11.3 | Indirecto |  |
| RT-05.18 | La autenticación entre sistemas empleará OAuth 2.1 con credenciales de cliente o… | 3.3.1 | Indirecto |  |
| RT-05.19 | Toda integración registrará la transacción de entrada y de salida, con identificador de… | 3.3.5 | Indirecto |  |
| RT-05.20 | Las integraciones con sistemas heredados o de terceros se aislarán mediante una capa… | 3.3.2 | Directo |  |
| RT-05.21 | El PROPONENTE declarará, por cada integración, el modo (síncrono o asíncrono), el volumen… | 2.1.1 | Indirecto |  |
| RT-05.22 | La solución soportará la carga y descarga masiva de información en formatos abiertos, con… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-05.23 | Se emplearán los estándares sectoriales de intercambio que las Bases Técnicas del caso… | 3.6.1, 3.6.5 | Indirecto |  |
| RT-05.24 | Se valorará la publicación de un portal de servicios para desarrolladores con… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-05.25 | La solución proveerá una capa analítica con tableros operacionales y de gestión… | 3.4.11, 3.2.3 | Directo |  |
| RT-05.26 | Los tableros permitirán filtrar por período, unidad organizacional y dimensiones propias… | 3.4.11, 3.2.3 | Directo |  |
| RT-05.27 | El CLIENTE podrá construir sus propios informes sin intervención del ADJUDICATARIO… | 3.2.3 | Indirecto |  |
| RT-05.28 | Todo informe será exportable en formatos abiertos y programable para envío automático por… | 3.4.11 | Indirecto |  |
| RT-05.29 | La latencia máxima entre la ocurrencia de una transacción y su disponibilidad en la capa… | 3.4.11, 3.2.3 | Directo |  |
| RT-05.30 | Se valorará la incorporación de analítica predictiva pertinente al proceso del caso, con… | 3.10.3.1, 3.10.3.2, 3.10.3.3, 8.3.2 | Directo |  |
| RT-06.01 | El espacio asignado será de uso exclusivo de la solución y estará aislado de otras… | 2.3.1, 6.1.1 | Directo |  |
| RT-06.02 | Los muros no estructurales del recinto contarán con blindaje perimetral; el PROPONENTE… | 6.1.1 | Indirecto |  |
| RT-06.03 | El PROPONENTE entregará el plano de distribución interna del recinto, con la separación… | 2.3.1, 6.1.1 | Directo |  |
| RT-06.04 | El piso técnico, la canalización, el cableado estructurado y el etiquetado se ejecutarán… | 6.1.1, 6.2.1, 6.2.2 | Directo |  |
| RT-06.05 | Los racks de servidores serán independientes de los racks de equipos de comunicación. Se… | 2.3.2, 6.3.1, 6.3.2 | Directo |  |
| RT-06.06 | La obra civil de separación de las instalaciones es de cargo del CLIENTE; su… | 6.1.1 | Directo |  |
| RT-06.07 | El suministro eléctrico de los equipos será ininterrumpido, con sistema de alimentación… | 6.1.2 | Directo |  |
| RT-06.08 | La capacidad de generación autónoma asegurará un rango mínimo de 24 horas continuas de… | 6.1.2 | Directo |  |
| RT-06.09 | La instalación eléctrica del recinto será independiente de la del resto del edificio y… | 6.1.2 | Indirecto |  |
| RT-06.10 | Se efectuará revisión y medición semestral de las instalaciones eléctricas del recinto… | 8.2.6 | Directo |  |
| RT-06.11 | El PROPONENTE declarará la carga eléctrica proyectada en kW, el factor de potencia y la… | 2.3.1, 6.1.1 | Directo |  |
| RT-06.12 | Se valorará la redundancia de alimentación en configuración 2N o N+1 con doble acometida… | 6.1.2 | Directo |  |
| RT-06.13 | El recinto contará con climatización de precisión para operación continua, redundante en… | 6.1.3 | Directo |  |
| RT-06.14 | Se monitorearán en línea la temperatura, la humedad y la presencia de agua, con… | 6.1.3, 3.1.5 | Indirecto |  |
| RT-06.15 | El PROPONENTE declarará la estrategia de contención de pasillo frío o caliente y su… | 2.3.2 | Indirecto |  |
| RT-06.16 | El recinto contará con detección temprana por aspiración de aire con tecnología láser… | 6.1.4 | Directo |  |
| RT-06.17 | La extinción será automática mediante agente limpio tipo FM-200 o equivalente, con… | 6.1.4 | Directo |  |
| RT-06.18 | Se proveerá un sistema secundario de extintores portátiles habilitados, con mantención y… | 6.1.4 | Indirecto |  |
| RT-06.19 | El sistema de detección y extinción se integrará al monitoreo en línea y notificará al… | 6.1.4 | Indirecto |  |
| RT-06.20 | El ingreso al recinto se controlará mediante seguridad física y control de acceso… | 6.4.1 | Directo |  |
| RT-06.21 | Todo ingreso y egreso quedará registrado en una bitácora auditable, con identificación de… | 6.4.1 | Indirecto |  |
| RT-06.22 | Entre el acceso principal y el término del pasillo de la zona de control se dispondrá un… | 6.4.1 | Indirecto |  |
| RT-06.23 | Al término del pasillo se instalará un acceso que impida el paso de más de una persona a… | 6.4.1 | Directo |  |
| RT-06.24 | El recinto contará con videovigilancia y monitoreo IP, con imágenes en línea y… | 6.4.2 | Directo |  |
| RT-06.25 | El PROPONENTE declarará el procedimiento de acceso de terceros —fabricantes… | 6.4.1 | Indirecto |  |
| RT-06.26 | Se habilitará un servicio de custodia de medios de respaldo para el sitio primario, en un… | 6.4.3 | Directo |  |
| RT-06.27 | El recinto de custodia cumplirá exigencias de luminosidad, humedad, ventilación y… | 6.4.3 | Directo |  |
| RT-06.28 | Se llevará un inventario de medios con rotación, verificación periódica de legibilidad y… | 6.4.3 | Indirecto |  |
| RT-06.29 | El PROPONENTE habilitará el espacio físico necesario para el personal encargado de la… | 2.3.1 | Indirecto |  |
| RT-06.30 | El espacio de operación estará separado de la sala de equipos y no requerirá el ingreso… | 2.3.1 | Indirecto |  |
| RT-06.31 | Las instalaciones sanitarias, las zonas de seguridad ante emergencia y las áreas… | 2.3.1 | Indirecto |  |
| RT-06.32 | El acceso a las redes de comunicaciones estará provisto a través de rutas físicas… | 6.2.1 | Directo |  |
| RT-06.33 | El PROPONENTE proveerá toda la conectividad, la seguridad y las canalizaciones, cañerías… | 6.2.1 | Indirecto |  |
| RT-06.34 | Se privilegiará al PROPONENTE que ofrezca o provea especificaciones nuevas o mejores que… | 3.2.4 | Indirecto |  |
| RT-07.01 | El PROPONENTE declarará la modalidad escogida —activo-activo o activo-pasivo— y la… | 2.5.2, 3.1.3 | Indirecto |  |
| RT-07.02 | El sitio secundario estará emplazado a una distancia suficiente del principal para no… | 3.1.3 | Directo |  |
| RT-07.03 | La replicación de datos será continua, con medición y alertamiento del retraso de… | 3.2.4 | Indirecto |  |
| RT-07.04 | El objetivo de tiempo de recuperación (RTO) no superará 4 horas y el objetivo de punto de… | 3.1.3, 2.5.2 | Directo |  |
| RT-07.05 | El procedimiento de conmutación estará documentado, automatizado en la mayor medida… | 2.5.2 | Directo |  |
| RT-07.06 | Existirá un procedimiento de retorno al sitio principal igualmente documentado y probado… | 2.5.2, 3.1.3 | Indirecto |  |
| RT-07.07 | El plan de recuperación ante desastres se probará al menos dos veces al año mediante… | 3.8.5, 3.9.4, 8.1.3 | Directo |  |
| RT-07.08 | Se valorará que la conmutación sea automática ante la detección de indisponibilidad, con… | 2.5.2, 3.1.3 | Indirecto |  |
| RT-07.09 | La política de respaldo seguirá el esquema 3-2-1-0: tres copias, en dos medios distintos… | 3.2.4 | Directo |  |
| RT-07.10 | Los respaldos estarán cifrados en reposo y en tránsito, con clave gestionada de forma… | 3.2.4 | Indirecto |  |
| RT-07.11 | Las copias inmutables estarán protegidas contra borrado y contra modificación durante su… | 3.2.4 | Directo |  |
| RT-07.12 | Se ejecutará y documentará una prueba de restauración al menos mensual, sobre una muestra… | 8.1.6 | Directo |  |
| RT-07.13 | El PROPONENTE declarará, por cada dominio de datos, la frecuencia de respaldo, el período… | 3.2.4 | Indirecto |  |
| RT-07.14 | Los respaldos permitirán la restauración granular: un registro, una tabla, un módulo o el… | 3.2.4 | Indirecto |  |
| RT-08.01 | El PROPONENTE especificará el equipamiento de cómputo con su marca, modelo de referencia… | 5.1.2 | Directo |  |
| RT-08.02 | El almacenamiento será redundante, con tolerancia declarada a la falla de discos, control… | 6.3.1 | Indirecto |  |
| RT-08.03 | Los conmutadores de núcleo, los cortafuegos y los balanceadores de carga estarán en… | 6.3.2 | Directo |  |
| RT-08.04 | Todo el equipamiento contará con fuentes de poder redundantes y conexión a circuitos… | 6.3.1 | Indirecto |  |
| RT-08.05 | El PROPONENTE declarará el margen de crecimiento del dimensionamiento propuesto… | 8.4.1 | Directo |  |
| RT-08.06 | El equipamiento será nuevo, sin uso previo, con garantía de fábrica vigente desde la… | 5.1.2 | Indirecto |  |
| RT-08.07 | El PROPONENTE especificará las estaciones de trabajo requeridas para la operación y la… | — | Brecha | Estaciones de trabajo de operación: ningún paquete las especifica ni instala. |
| RT-08.08 | Los puestos de trabajo cumplirán las condiciones ergonómicas de la NCh 2527 y los equipos… | — | Brecha | Estaciones de trabajo de operación: ningún paquete las especifica ni instala. |
| RT-08.09 | Las estaciones estarán gestionadas de forma centralizada, con cifrado de disco, control… | 3.2.5, 5.2.2 | Indirecto |  |
| RT-08.10 | El PROPONENTE especificará cada dispositivo de terreno con marca, modelo de referencia… | 5.1.1 | Directo |  |
| RT-08.11 | La especificación considerará las condiciones reales de uso del caso: intemperie… | 5.1.1 | Directo |  |
| RT-08.12 | Los dispositivos declararán su grado de protección contra polvo y agua y su resistencia a… | 5.1.1 | Directo |  |
| RT-08.13 | El PROPONENTE indicará el ciclo de vida esperado de cada dispositivo, la disponibilidad… | 5.1.1, 8.2.7 | Directo |  |
| RT-08.14 | Los dispositivos se integrarán a la gestión centralizada de flota exigida en RT-03.18. | 3.2.6 | Directo |  |
| RT-08.15 | El PROPONENTE proveerá una unidad de cada tipo de dispositivo especificado para pruebas… | 5.1.1 | Indirecto |  |
| RT-08.16 | El PROPONENTE presentará el plan de ciclo de vida del equipamiento: recepción, puesta en… | 5.1.3, 6.5.1, 8.2.7 | Directo |  |
| RT-08.17 | Todo medio de almacenamiento que salga de servicio será borrado de forma segura y… | 8.2.7, 9.2.2 | Indirecto |  |
| RT-08.18 | La disposición final de equipamiento electrónico se realizará con gestor autorizado… | 8.2.7 | Directo |  |
| RT-08.19 | Se valorará una estrategia de reacondicionamiento o de extensión de vida útil que reduzca… | 8.2.7 | Indirecto |  |
| RT-09.01 | El PROPONENTE presentará el cálculo de capacidad que sustenta su dimensionamiento, con… | 2.1.2 | Indirecto |  |
| RT-09.02 | La solución soportará la concurrencia y el volumen de transacciones que fije el caso, y… | 3.8.4 | Indirecto |  |
| RT-09.03 | La solución soportará, sin rediseño, un crecimiento de al menos tres veces la volumetría… | 2.1.2 | Indirecto |  |
| RT-09.04 | El escalamiento de las capas de aplicación e integración será horizontal y automático… | 3.2.1 | Directo |  |
| RT-09.05 | El PROPONENTE identificará el componente que primero se convertirá en cuello de botella… | 2.1.2 | Indirecto |  |
| RT-09.06 | Se ejecutarán pruebas de carga sobre Preproducción con un volumen equivalente a 1,5 veces… | 3.8.4, 3.9.3 | Directo |  |
| RT-09.07 | El informe de pruebas de carga incluirá la curva de tiempo de respuesta frente a carga… | 3.8.4, 3.9.3 | Directo |  |
| RT-09.08 | La solución degradará de forma controlada al superarse la capacidad: encolamiento… | 2.1.1 | Indirecto |  |
| RT-09.09 | Se gestionará la capacidad durante la Operación con proyección trimestral de crecimiento… | 8.4.1 | Directo |  |
| RT-09.10 | Se valorará la existencia de pruebas de carga automatizadas ejecutadas de forma periódica… | 3.1.4 | Indirecto |  |
| RT-10.01 | La solución alcanzará una disponibilidad mensual mínima de 99,9 % para los servicios… | 8.1.2 | Directo |  |
| RT-10.02 | El PROPONENTE clasificará cada servicio de la solución en crítico, alto, medio o bajo… | 2.5.1 | Indirecto |  |
| RT-10.03 | El plan de continuidad del negocio se elaborará conforme a ISO 22301, con análisis de… | 2.5.1 | Directo |  |
| RT-10.04 | La continuidad TIC se estructurará conforme a ISO/IEC 27031, articulada con el plan de… | 2.5.2 | Directo |  |
| RT-10.05 | Los mantenimientos programados se ejecutarán fuera de la ventana operacional crítica que… | 1.3.1, 8.2.1 | Indirecto |  |
| RT-10.06 | La solución permitirá desplegar cambios sin interrupción del servicio. Las ventanas de… | 3.8.8, 3.9.7 | Directo |  |
| RT-10.07 | Se ejecutarán pruebas de resiliencia mediante inyección controlada de fallas —caída de… | 3.8.4, 3.9.3, 8.2.2 | Directo |  |
| RT-10.08 | El PROPONENTE documentará, por cada dependencia externa, el comportamiento de la solución… | 2.5.2 | Indirecto |  |
| RT-10.09 | Se declarará un presupuesto de error por servicio crítico y su vinculación con el ritmo… | 8.1.2 | Indirecto | Presupuesto de error: no figura como entregable explícito. |
| RT-11.01 | La arquitectura de seguridad se basará en el modelo Zero Trust conforme a NIST SP… | 2.2.1 | Directo |  |
| RT-11.02 | El PROPONENTE entregará un modelado de amenazas documentado por cada componente y por… | 2.2.2 | Directo |  |
| RT-11.03 | La información del CLIENTE se clasificará por nivel de sensibilidad, con controles… | 2.2.4 | Directo |  |
| RT-11.04 | Existirá un programa de gestión de vulnerabilidades con escaneo continuo y plazos máximos… | 8.2.2 | Directo |  |
| RT-11.05 | El PROPONENTE mantendrá una matriz de controles de seguridad trazable a ISO/IEC 27001 e… | 2.2.4 | Directo |  |
| RT-11.06 | Se aplicarán los controles de ISO/IEC 27017 para los servicios en nube y de ISO/IEC 27018… | 2.2.1, 1.9.1 | Indirecto |  |
| RT-11.07 | La publicación de servicios se realizará exclusivamente a través de la capa de borde, con… | 3.2.1 | Indirecto |  |
| RT-11.08 | El cifrado en tránsito empleará TLS 1.3, con prohibición expresa de TLS 1.0 y 1.1… | 3.2.1 | Indirecto |  |
| RT-11.09 | La totalidad de los datos en reposo estará cifrada, con claves gestionadas en un servicio… | 3.2.5 | Indirecto |  |
| RT-11.10 | Los datos de categoría sensible que el caso identifique se cifrarán adicionalmente a… | 2.2.4 | Indirecto |  |
| RT-11.11 | La puerta de enlace de servicios aplicará autenticación, autorización, cuotas, límites de… | 3.2.1 | Indirecto |  |
| RT-11.12 | Los puntos de entrada públicos contarán con protección contra bots y abuso automatizado… | 3.2.1 | Indirecto |  |
| RT-11.13 | El PROPONENTE declarará la superficie de exposición completa de la solución: cada nombre… | 2.1.2 | Indirecto |  |
| RT-11.14 | Los eventos de seguridad se registrarán de forma centralizada e inalterable, con… | 8.1.5, 3.2.5 | Indirecto |  |
| RT-11.15 | Los eventos se correlacionarán en una plataforma SIEM, con casos de uso de detección… | 8.1.5 | Directo |  |
| RT-11.16 | Se implementará detección y respuesta en puntos finales y en cargas de trabajo, tanto en… | 3.2.5, 5.2.2 | Directo |  |
| RT-11.17 | El PROPONENTE dispondrá de un centro de operaciones de seguridad con cobertura 24×7… | 8.1.5 | Directo |  |
| RT-11.18 | El plan de respuesta a incidentes de seguridad definirá clasificación, cadena de… | 2.2.3 | Directo |  |
| RT-11.19 | Toda brecha de seguridad o de datos personales se notificará al CLIENTE dentro de las 24… | 8.1.5 | Directo |  |
| RT-11.20 | Se ejecutarán pruebas de intrusión por un tercero independiente del ADJUDICATARIO… | 3.8.6, 3.9.5, 8.2.2 | Directo |  |
| RT-11.21 | Se realizarán ejercicios de simulación de incidente con participación del CLIENTE al… | 8.1.5 | Directo |  |
| RT-11.22 | El flujo de integración continua incorporará análisis estático de código, análisis de… | 3.1.4 | Directo |  |
| RT-11.23 | Cada versión liberada se acompañará de su inventario de componentes de software en… | 3.11.4 | Directo |  |
| RT-11.24 | Los artefactos se firmarán y su procedencia se verificará conforme a SLSA nivel 3 o… | 3.1.4 | Indirecto |  |
| RT-11.25 | Queda prohibido el uso de datos productivos reales en ambientes no productivos sin… | 3.1.1 | Indirecto |  |
| RT-11.26 | El PROPONENTE declarará el proceso de aprobación de nuevas dependencias de terceros… | 3.11.4 | Indirecto |  |
| RT-11.27 | Las personas desarrolladoras no tendrán acceso interactivo directo al ambiente de… | 3.3.1 | Indirecto |  |
| RT-11.28 | Se aplicará el marco OWASP SAMM o equivalente para medir y mejorar la madurez del proceso… | 2.2.1 | Indirecto | OWASP SAMM: no figura como entregable explícito. |
| RT-12.01 | La gestión de identidad será centralizada, con federación mediante OpenID Connect y OAuth… | 3.3.1 | Directo |  |
| RT-12.02 | Existirá inicio de sesión único para todos los módulos de la solución, con cierre de… | 3.3.1 | Directo |  |
| RT-12.03 | La autenticación multifactor será obligatoria para personas usuarias administradoras… | 3.3.1 | Directo |  |
| RT-12.04 | Se soportarán factores resistentes a la suplantación de identidad, tipo FIDO2 o claves de… | 3.3.1 | Directo |  |
| RT-12.05 | El control de acceso será basado en roles, complementado con control basado en atributos… | 3.3.1 | Directo |  |
| RT-12.06 | Los accesos privilegiados se gestionarán con elevación temporal a demanda, aprobación… | 3.3.1 | Indirecto |  |
| RT-12.07 | La política de sesión declarará duración máxima, caducidad por inactividad, renovación de… | 3.3.1 | Directo |  |
| RT-12.08 | Las credenciales de sesión serán firmadas y de vida breve, con credencial de refresco… | 3.3.1 | Directo |  |
| RT-12.09 | Se registrará auditoría completa del ciclo de vida de la identidad: creación… | 3.3.1 | Directo |  |
| RT-12.10 | El aprovisionamiento y el desaprovisionamiento estarán automatizados y ligados al ciclo… | 3.3.1 | Directo |  |
| RT-12.11 | El mecanismo de autenticación se adecuará al perfil operacional real descrito en el caso… | 3.3.1 | Directo |  |
| RT-12.12 | Las personas usuarias externas del CLIENTE —clientes, proveedores, pacientes… | 3.5.2, 3.3.1 | Directo |  |
| RT-12.13 | El PROPONENTE declarará el procedimiento de acceso de emergencia (cuenta de último… | 3.3.1 | Indirecto |  |
| RT-13.01 | Todas las interfaces destinadas a personas usuarias cumplirán WCAG 2.2 nivel AA… | 3.8.2, 3.9.2 | Directo |  |
| RT-13.02 | El diseño será responsivo y funcionará correctamente en escritorio, tableta y teléfono… | 3.5.2, 2.6.2 | Indirecto |  |
| RT-13.03 | El PROPONENTE ejecutará investigación con personas usuarias reales del CLIENTE… | 2.6.1, 2.6.2 | Directo |  |
| RT-13.04 | Se comprometerán indicadores de usabilidad medibles: tiempo máximo de la transacción… | 2.6.3 | Directo |  |
| RT-13.05 | Ninguna funcionalidad principal requerirá más de tres interacciones desde la pantalla de… | 2.6.2 | Indirecto |  |
| RT-13.06 | La solución entregará retroalimentación visual clara ante cada acción, manejará los… | 2.6.2 | Indirecto |  |
| RT-13.07 | La solución soportará a personas usuarias con baja alfabetización digital: alto… | 2.6.2 | Indirecto |  |
| RT-13.08 | Cuando el caso lo requiera, las interfaces de terreno operarán con guantes, a la… | 3.8.3 | Directo |  |
| RT-13.09 | Existirá un sistema de diseño documentado con paleta de colores acotada, jerarquía… | 2.6.2 | Indirecto |  |
| RT-13.10 | El PROPONENTE declarará la matriz de navegadores y de versiones soportadas y su política… | 3.8.2 | Indirecto |  |
| RT-13.11 | La solución será navegable íntegramente por teclado, con orden de foco lógico y atajos… | 3.8.2 | Indirecto |  |
| RT-13.12 | Se valorará el soporte de modo oscuro, de personalización de la interfaz por persona… | 2.6.2 | Indirecto |  |
| RT-14.01 | La observabilidad será unificada para nube y on-premise, con métricas, registros y trazas… | 3.1.5 | Directo |  |
| RT-14.02 | El CLIENTE dispondrá de acceso propio y permanente a los tableros operacionales y de… | 3.1.5 | Directo |  |
| RT-14.03 | Los indicadores de nivel de servicio se medirán sobre la experiencia real de la persona… | 3.1.5 | Indirecto |  |
| RT-14.04 | El alertamiento se basará en síntomas de negocio y no sólo en umbrales de… | 3.1.5 | Indirecto |  |
| RT-14.05 | Existirá un libro de operación y una guía de resolución documentados para cada escenario… | 3.11.1 | Directo |  |
| RT-14.06 | Todo incidente crítico dará lugar a un análisis de causa raíz obligatorio, con informe… | 8.1.2 | Directo |  |
| RT-14.07 | Los registros de la solución no contendrán datos personales sensibles ni credenciales, y… | 3.1.5 | Indirecto |  |
| RT-14.08 | El PROPONENTE declarará la retención de métricas, registros y trazas, y su costo… | 3.1.5 | Indirecto |  |
| RT-14.09 | Se valorará la detección proactiva de anomalías mediante análisis del comportamiento… | 3.1.5 | Indirecto |  |
| RT-15.01 | El PROPONENTE dimensionará la infraestructura ajustada a la demanda real, evitando… | 8.4.1 | Indirecto |  |
| RT-15.02 | Los ambientes no productivos se apagarán o reducirán fuera del horario de uso. Caso, cap.… | 3.1.1, 8.4.2 | Indirecto |  |
| RT-15.03 | El PROPONENTE estimará la huella de carbono anual de la operación de la solución y… | 8.4.3 | Directo |  |
| RT-15.04 | Se declarará la eficiencia en el uso de la energía (PUE) del recinto on-premise y la… | 8.4.3 | Indirecto |  |
| RT-15.05 | Se valorará la elección de regiones de nube con menor intensidad de carbono cuando la… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-15.06 | Se valorará la definición de metas de reducción del consumo durante la Operación, con… | 8.4.3 | Directo |  |
| RT-15.07 | Las certificaciones se acreditarán con copia del certificado vigente y con el código de… | 1.9.4 | Indirecto | 1.9.4 solo nombra ISO/IEC 27001. |
| RT-15.08 | Las personas certificadas formarán parte del equipo efectivamente asignado al PROYECTO… | 1.8.1 | Indirecto |  |
| RT-15.09 | El ADJUDICATARIO mantendrá vigentes estas certificaciones durante todo el período… | 1.9.4 | Indirecto | 1.9.4 solo nombra ISO/IEC 27001. |
| RT-16.01 | La solución dispondrá de un módulo de administración que permita al CLIENTE, sin… | 3.3.1 | Indirecto |  |
| RT-16.02 | Las reglas de negocio parametrizables —umbrales, plazos, montos, tolerancias, catálogos… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-16.03 | Todo cambio de parámetro con impacto operacional requerirá aprobación de un segundo… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-16.04 | El PROPONENTE declarará expresamente qué elementos son parametrizables y cuáles requieren… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-16.05 | Existirá un ambiente de simulación que permita probar el efecto de un cambio de parámetro… | 3.1.1 | Indirecto |  |
| RT-16.06 | Toda operación que cree, modifique o elimine información quedará registrada con… | 3.3.5 | Indirecto |  |
| RT-16.07 | El registro de auditoría será inalterable y no podrá ser modificado ni eliminado por… | 3.3.5, 3.2.4 | Indirecto |  |
| RT-16.08 | El CLIENTE podrá consultar y exportar la auditoría desde la interfaz, con filtros por… | 3.3.5 | Indirecto |  |
| RT-16.09 | Las consultas a información sensible quedarán registradas, no sólo las modificaciones.… | 3.3.5 | Indirecto |  |
| RT-16.10 | El período de retención de la auditoría será el que fije el caso y, en su defecto, no… | 3.2.4 | Indirecto |  |
| RT-16.11 | La solución soportará flujos de trabajo con estados, transiciones, responsables, plazos… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-16.12 | Los flujos serán configurables por el CLIENTE sin desarrollo, al menos en lo relativo a… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-16.13 | Toda solicitud pendiente será visible para su responsable en una bandeja de tareas… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-16.14 | El motor de reglas permitirá definir condiciones de negocio evaluables sin recompilación… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-16.15 | La solución gestionará documentos con versionado, metadatos, control de acceso, búsqueda… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-16.16 | Los documentos se almacenarán cifrados, con verificación de integridad y retención… | 3.4.8, 3.2.4 | Indirecto |  |
| RT-16.17 | La solución soportará firma electrónica conforme a la Ley N° 19.799, con firma avanzada… | 3.3.2 | Indirecto |  |
| RT-16.18 | Se generará el sello de tiempo y se conservará la evidencia de firma que permita… | 3.3.2 | Indirecto |  |
| RT-16.19 | La solución generará documentos a partir de plantillas administrables por el CLIENTE, con… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-16.20 | La solución enviará notificaciones por al menos tres canales: correo electrónico… | 3.6.4 | Directo |  |
| RT-16.21 | Las plantillas de notificación serán administrables por el CLIENTE, con variables de la… | 3.6.4 | Indirecto |  |
| RT-16.22 | Cada persona usuaria podrá configurar sus preferencias de canal y de frecuencia… | 3.6.4 | Indirecto |  |
| RT-16.23 | El envío será asíncrono, con reintento ante falla, control de duplicados y registro de… | 3.6.4 | Directo |  |
| RT-16.24 | El PROPONENTE declarará el proveedor de cada canal, su costo unitario, su volumen… | 3.6.4 | Indirecto |  |
| RT-16.25 | Las notificaciones respetarán la normativa de comunicaciones comerciales y permitirán la… | 3.6.4 | Indirecto |  |
| RT-16.26 | Se valorará la integración con canales conversacionales que permitan a la persona usuaria… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-16.27 | La solución dispondrá de búsqueda global con indexación de texto completo, tolerancia a… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-16.28 | Los listados serán ordenables, filtrables, paginados y exportables en formatos abiertos… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-16.29 | Las exportaciones de gran volumen se procesarán de forma asíncrona, con notificación al… | 3.3 (cuenta) | Brecha | Sin paquete propio: servicio común de la plataforma (propuesta 3.3.7). |
| RT-16.30 | Toda exportación de información sensible quedará registrada en la auditoría, con… | 3.3.5 | Indirecto |  |
| RT-16.31 | La solución dispondrá de un portal público con la información que el caso determine… | 3.5.2, 3.8.2, 3.8.4, 3.9.2, 3.9.3 | Indirecto | Portal público: sin paquete de construcción propio; el T-12 cita sus pruebas en 3.8 y 3.9. |
| RT-16.32 | Las personas usuarias externas dispondrán de autoatención para las consultas de mayor… | 3.5.2 | Directo |  |
| RT-16.33 | El PROPONENTE estimará la reducción esperada del volumen de atención asistida por efecto… | 3.5.2 | Indirecto |  |
| RT-16.34 | El portal público resistirá picos de tráfico sin degradar los servicios transaccionales… | 3.2.1 | Indirecto |  |
| RT-17.01 | La solución proveerá una aplicación móvil para los perfiles operacionales que el caso… | 3.4.6, 3.4.8, 3.4.3 | Directo |  |
| RT-17.02 | El PROPONENTE declarará si la aplicación es nativa, híbrida o web progresiva, y… | 2.1.1 | Indirecto |  |
| RT-17.03 | La aplicación soportará las versiones de sistema operativo móvil vigentes y las dos… | 3.2.6 | Indirecto |  |
| RT-17.04 | La aplicación se distribuirá por las tiendas oficiales o mediante gestión de flota… | 3.2.6 | Directo |  |
| RT-17.05 | La información almacenada en el dispositivo estará cifrada, con borrado remoto y bloqueo… | 3.2.6 | Indirecto |  |
| RT-17.06 | La aplicación integrará los periféricos que el caso requiera: cámara, lector de códigos… | 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5, 6.5.6 | Directo |  |
| RT-17.07 | El consumo de datos móviles y de batería se optimizará y se declarará el consumo estimado… | 2.1.2 | Indirecto |  |
| RT-17.08 | Se valorará la disponibilidad de una versión de la interfaz para dispositivos de bajo… | 3.5.2 | Indirecto |  |
| RT-18.01 | El PROPONENTE declarará cada componente de inteligencia artificial: propósito, modelo o… | — | No aplica | Se cumple declarando que la solución no incorpora IA (D-09); no genera trabajo. |
| RT-18.02 | Se garantizará contractualmente que los datos del CLIENTE no serán utilizados para… | — | No aplica | Se cumple declarando que la solución no incorpora IA (D-09); no genera trabajo. |
| RT-18.03 | Se documentarán los límites de uso, los casos en que el resultado requiere validación… | — | No aplica | Se cumple declarando que la solución no incorpora IA (D-09); no genera trabajo. |
| RT-18.04 | Los riesgos de sesgo, alucinación, fuga de información y uso indebido se evaluarán y… | — | No aplica | Se cumple declarando que la solución no incorpora IA (D-09); no genera trabajo. |
| RT-18.05 | Toda interacción relevante con un componente de inteligencia artificial quedará… | — | No aplica | Se cumple declarando que la solución no incorpora IA (D-09); no genera trabajo. |
| RT-18.06 | El componente podrá desactivarse sin comprometer la operación del resto de la solución, y… | — | No aplica | Se cumple declarando que la solución no incorpora IA (D-09); no genera trabajo. |
| RT-18.07 | Cuando el resultado se presente a una persona usuaria, se indicará expresamente que fue… | — | No aplica | Se cumple declarando que la solución no incorpora IA (D-09); no genera trabajo. |
| RT-18.08 | Los modelos predictivos declararán sus variables de entrada, su métrica de desempeño, su… | 3.10.3.1, 8.3.2 | Directo |  |
| RT-18.09 | La responsabilidad por los resultados de los componentes de inteligencia artificial recae… | — | No aplica | Se cumple declarando que la solución no incorpora IA (D-09); no genera trabajo. |
| RT-18.10 | Se valorará el uso de automatización robótica de procesos o de agentes para tareas… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-19.01 | El ADJUDICATARIO constituirá una oficina de gestión del proyecto con metodología… | 1.8.1 | Directo |  |
| RT-19.02 | El Jefe de Proyecto tendrá dedicación exclusiva durante toda la fase de implementación y… | 1.8.1 | Indirecto |  |
| RT-19.03 | Existirá un procedimiento formal de control de cambios conforme al Artículo 72° de las… | 1.4.3, 1.8.2 | Directo |  |
| RT-19.04 | La gestión del riesgo seguirá la norma ISO 31000, con registro de riesgos vivo, revisión… | 1.6.1, 1.6.2 | Directo |  |
| RT-19.05 | El ADJUDICATARIO habilitará un espacio colaborativo accesible al CLIENTE, con la… | 1.8.8 | Directo |  |
| RT-19.06 | El ADJUDICATARIO entregará un informe mensual de avance con estado del cronograma, avance… | 1.8.6 | Directo |  |
| RT-19.07 | El avance se medirá con valor ganado, reportando el índice de desempeño del cronograma y… | 1.8.6 | Directo |  |
| RT-19.08 | El CLIENTE dispondrá de un tablero de estado del proyecto actualizado, accesible en… | 1.8.7 | Directo |  |
| RT-19.09 | Las actas de todos los comités del Artículo 71° de las Bases Administrativas se… | 1.8.2, 1.8.3, 1.8.4, 1.8.5 | Directo |  |
| RT-19.10 | Toda desviación superior al 10 % en un hito se comunicará dentro de los cinco días… | 1.8.6 | Indirecto |  |
| RT-20.01 | El PROPONENTE presentará un plan de implantación por sitio y por perfil, coherente con el… | 4.1.1 | Directo |  |
| RT-20.02 | La estrategia de paso a producción será gradual y reversible. Se declarará el criterio de… | 4.1.1, 4.1.2, 4.1.3 | Directo |  |
| RT-20.03 | Durante la marcha blanca, la solución convivirá con la operación vigente del CLIENTE, con… | 4.2.1, 4.3.1 | Directo |  |
| RT-20.04 | El PROPONENTE definirá los indicadores diarios que se medirán durante la marcha blanca y… | 4.2.1, 4.3.1 | Indirecto |  |
| RT-20.05 | Se dispondrá de acompañamiento en terreno durante las primeras semanas de cada ola, con… | 4.2.2 | Directo |  |
| RT-20.06 | Se establecerá un período de estabilización con atención reforzada tras cada paso a… | 4.2.2, 4.3.2 | Directo |  |
| RT-20.07 | Existirá una definición de terminado acordada con el CLIENTE, aplicable a cada… | 1.5.1 | Indirecto | Definición de terminado: no figura como entregable explícito. |
| RT-20.08 | El protocolo de aceptación de cada hito se formalizará conforme al Formulario T-17, con… | 3.8.7, 3.9.6, 4.2.3, 4.3.3 | Directo |  |
| RT-21.01 | El ADJUDICATARIO dispondrá de un centro de operaciones de red con cobertura 24×7×365… | 8.1.1 | Directo |  |
| RT-21.02 | Se designará un gerente de servicio dedicado como contraparte permanente del CLIENTE… | 8.1.1 | Indirecto |  |
| RT-21.03 | El equipo de operación contará con especialistas por tecnología, nominados y con… | 8.1.1 | Indirecto |  |
| RT-21.04 | Los procedimientos de operación estarán documentados y serán ejecutables por el personal… | 3.11.1, 7.1.4 | Directo |  |
| RT-21.05 | El PROPONENTE dispondrá de un centro de atención adecuado para soportar integralmente las… | 8.1.1 | Directo |  |
| RT-21.06 | El centro de atención cumplirá un tiempo de atención al usuario final de 80 % antes de 20… | 8.1.1 | Indirecto |  |
| RT-21.07 | El horario mínimo de atención será de 8:00 a 20:00 en días hábiles, ampliado a 24×7 para… | 8.1.1 | Directo |  |
| RT-21.08 | La atención cubrirá orientación funcional de distintos grados de complejidad, desde… | 8.1.1, 8.5.3 | Indirecto |  |
| RT-21.09 | Se mantendrá un registro histórico de las actividades de soporte que permita monitorear y… | 8.1.2 | Indirecto |  |
| RT-21.10 | Existirá un proceso de aprendizaje del centro de soporte que acumule conocimiento sobre… | 8.5.3 | Directo |  |
| RT-21.11 | Se proveerán servicios de capacitación en línea en modalidad de autoformación, con… | 7.1.6 | Directo |  |
| RT-21.12 | Se habilitarán espacios de interacción entre las entidades y personas usuarias del… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-21.13 | Los indicadores clave del proceso de soporte estarán abiertos al CLIENTE, y los… | 3.1.5, 8.1.2 | Indirecto |  |
| RT-21.14 | El PROPONENTE dimensionará la dotación del centro de atención con fundamento… | 8.1.1 | Indirecto |  |
| RT-21.15 | Existirá un canal único de registro de incidentes y solicitudes, con número de ticket… | 8.1.2 | Indirecto |  |
| RT-21.16 | Cuando el caso comprenda sitios alejados, los especialistas de niveles 2 y 3 deberán… | 8.2.3 | Indirecto |  |
| RT-21.17 | El cierre de un ticket requerirá confirmación de la persona usuaria o transcurso del… | 8.1.2 | Indirecto |  |
| RT-21.18 | El ADJUDICATARIO reportará mensualmente el cumplimiento de los niveles de servicio de… | 8.1.2 | Directo |  |
| RT-21.19 | El PROPONENTE declarará el tamaño de la bolsa anual de horas de mantención evolutiva, su… | 8.2.1 | Directo |  |
| RT-21.20 | La mantención evolutiva se someterá al mismo estándar de calidad, pruebas y seguridad que… | 8.2.1 | Directo |  |
| RT-21.21 | El PROPONENTE mantendrá un registro de deuda técnica cuantificado y destinará una… | 8.2.4 | Directo |  |
| RT-21.22 | Las actualizaciones de versión de los componentes de base se planificarán anualmente, con… | 8.2.5 | Directo |  |
| RT-22.01 | El plan de capacitación se estructurará por perfil: personas usuarias finales, usuarias… | 7.1.1, 7.1.2 | Directo |  |
| RT-22.02 | Las modalidades incluirán capacitación presencial en cada sitio de operación, sesiones en… | 7.1.1 | Indirecto |  |
| RT-22.03 | Todo el material de capacitación se entregará en español, en formato editable y de… | 7.1.5 | Directo |  |
| RT-22.04 | La capacitación no podrá afectar la operación del CLIENTE: se programará por turnos y en… | 7.1.1, 7.1.2 | Directo |  |
| RT-22.05 | Las personas usuarias administradoras y el equipo técnico del CLIENTE serán evaluados y… | 7.1.4, 7.3.1 | Indirecto |  |
| RT-22.06 | Durante la Operación se ejecutarán al menos dos jornadas anuales de actualización y se… | 8.5.1 | Directo |  |
| RT-22.07 | El ADJUDICATARIO proveerá acompañamiento y mentoría al equipo técnico del CLIENTE durante… | 8.5.2 | Directo |  |
| RT-22.08 | La base de conocimiento será mantenida y actualizada durante todo el Contrato, con… | 8.5.3 | Directo |  |
| RT-22.09 | Se valorará la existencia de un ambiente permanente de entrenamiento, con datos… | 7.1.6 | Indirecto |  |
| RT-23.01 | Información institucional: descripción detallada del giro principal, historia y… | — | No aplica | Sitio web corporativo de LafroX durante la licitación; no es trabajo del proyecto. |
| RT-23.02 | Experiencia y casos de éxito: portafolio de proyectos similares de los últimos cinco… | — | No aplica | Sitio web corporativo de LafroX durante la licitación; no es trabajo del proyecto. |
| RT-23.03 | Equipo profesional: organigrama del equipo directivo, perfiles de socios y directores… | — | No aplica | Sitio web corporativo de LafroX durante la licitación; no es trabajo del proyecto. |
| RT-23.04 | Capacidades técnicas: servicios y soluciones ofrecidas, conjunto tecnológico dominado… | — | No aplica | Sitio web corporativo de LafroX durante la licitación; no es trabajo del proyecto. |
| RT-23.05 | El sitio será accesible conforme a WCAG 2.2 nivel AA, responsivo y con certificado TLS… | — | No aplica | Sitio web corporativo de LafroX durante la licitación; no es trabajo del proyecto. |
| RT-23.06 | El sitio se mantendrá activo y disponible durante todo el proceso de licitación, desde el… | — | No aplica | Sitio web corporativo de LafroX durante la licitación; no es trabajo del proyecto. |
| RT-23.07 | Material educativo digital: seminarios en línea, artículos técnicos o centro de recursos… | — | No aplica | Sitio web corporativo de LafroX durante la licitación; no es trabajo del proyecto. |
| RT-23.08 | Demostración en línea, recorrido virtual de la solución o portal de soporte para clientes. | — | No aplica | Sitio web corporativo de LafroX durante la licitación; no es trabajo del proyecto. |
| RT-23.09 | Métricas de disponibilidad y desempeño de los servicios del proponente publicadas en… | — | No aplica | Sitio web corporativo de LafroX durante la licitación; no es trabajo del proyecto. |
| RT-23.10 | Calculadora de retorno de la inversión o herramienta de estimación pertinente a la… | — | No aplica | Sitio web corporativo de LafroX durante la licitación; no es trabajo del proyecto. |
| RT-24.01 | Todos los integrantes clave del equipo deberán aparecer individualmente presentándose, en… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-24.02 | Cada vez que aparezca un integrante deberá mostrarse en pantalla su nombre completo, su… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-24.03 | Las certificaciones principales de cada integrante podrán mostrarse en pantalla. | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-24.04 | El fondo será el mismo para todas las tomas de personas, con iluminación consistente y… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-24.05 | La paleta de colores corporativa, la tipografía y el uso de la marca serán consistentes… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-24.06 | Los niveles de volumen estarán normalizados, con la misma calidad de grabación y sin… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-25.01 | Navegación intuitiva sin necesidad de manual, con un máximo de tres interacciones para… | 2.6.2 | Indirecto |  |
| RT-25.02 | Retroalimentación visual clara ante cada acción, estados de carga y transición fluidos, y… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-25.03 | Cumplimiento de WCAG 2.2 nivel AA: contraste adecuado, tamaños de fuente legibles… | 2.6.2 | Indirecto |  |
| RT-25.04 | Diseño responsivo demostrado en escritorio (1920 × 1080 y 1366 × 768), tableta (768 ×… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-25.05 | Sistema de diseño documentado: paleta de a lo más cinco colores principales, a lo más dos… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-25.06 | El prototipo se entregará como enlace navegable en línea, sin instalación ni… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-25.07 | El acceso al prototipo estará garantizado por un mínimo de seis meses desde su entrega. | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-25.08 | El prototipo permitirá navegación completa entre pantallas, simulación de ingreso de… | 2.6.2 | Directo |  |
| RT-25.09 | Se entregará la arquitectura de información del prototipo: mapa del sitio completo… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-25.10 | Se valorará la posibilidad de exportar el prototipo a un documento interactivo para… | — | No aplica | No cumple: sin trabajo comprometido. |
| RT-26.01 | Cada innovación se ubicará explícitamente en la arquitectura: qué capa la contiene, qué… | 3.10 (cuenta) | Indirecto |  |
| RT-26.02 | Cada innovación identificará los paquetes de la estructura de descomposición del trabajo… | 3.10 (cuenta), 5.4.3, 8.3 (cuenta) | Directo |  |
| RT-26.03 | Las innovaciones de base tecnológica declararán el nivel de madurez de la tecnología con… | 3.10 (cuenta) | Indirecto |  |
| RT-26.04 | Cada innovación declarará su riesgo de adopción, su probabilidad, su impacto, la… | 1.6.1 | Indirecto |  |
| RT-26.05 | Cada innovación declarará su indicador de verificación con línea base, meta y momento de… | 3.10.1.4, 3.10.2.4, 3.10.3.4, 3.10.4.4 | Indirecto |  |
| RT-26.06 | Las innovaciones que incorporen inteligencia artificial cumplirán íntegramente el… | — | No aplica | Ninguna innovación incorpora IA; no genera trabajo. |
| RT-26.07 | Las innovaciones que modifiquen la arquitectura de seguridad requerirán su propio… | 2.2.2 | Directo |  |
| RT-26.08 | Se valorará que al menos una innovación sea verificable durante la marcha blanca de la… | 3.10.2.4 | Directo |  |

## Fuentes

- [Formulario T-12](../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md): 645 filas (Parte A, 271; Parte B, 374).
- [Formulario T-14](../07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-14.md): diccionario de la EDT, 222 paquetes.
- [Anexos del SD3](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md): etapa de cada RF y RNF.
- Caso, cap. 17.1, p. 31: contenido exigido a la matriz de trazabilidad.
