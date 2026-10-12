# LafroX — Trazabilidad de observaciones del Informe 1: Subdocumento 4

## Publicación en rama-md — 12 de octubre de 2026

Copia del registro de trabajo conservado en `LafroX-rama-latex/04/revision/`, publicada por petición del usuario. Se preservan sus 46 observaciones y 13 pendientes tal como constan en la fuente del 11 de octubre. Es un registro histórico de trazabilidad, no una nueva evaluación del estado actual: los conteos, estados de revisión humana y referencias al T-12 deben leerse según el corte declarado en cada bloque. En particular, sus menciones de 56 celdas humanas pendientes no reemplazan el registro posterior de 132 filas con Álvaro Catalán en `cierre_correcciones_SD4_aclaraciones_2026-10-11.md`.

El cotejo contractual complementario se incluye al final de este mismo archivo. Se adapta el enlace de alineación al nombre existente en esta rama y se identifican las figuras como recursos del checkout LaTeX, sin importar activos no Markdown. No se cambian respuestas, estados, identificadores, entregables ni T-12.


## Alcance y criterio de lectura

Este registro sigue el formato de las tablas de SD1–SD3: observación del Informe 1 → respuesta → sección modificada. Se conserva una fila por cada una de las 46 observaciones ya registradas del SD4, incluidas las positivas, en el orden original: EL-01–EL-21 y EF-01–EF-25. Los identificadores se mantienen para enlazar el seguimiento P-01–P-13.

Fecha de actualización: 11 de octubre de 2026. Fuente de observaciones: `G02-C02-LOGISTICA-LAFROX-Revision Informe 1.pdf`, páginas 9–14, apartados 4.1 y 4.2. Las aclaraciones posteriores gobiernan la estructura consolidada 4.1–4.3. Las observaciones se sintetizan; no son citas literales. Este registro de trabajo no se incorpora al texto de la oferta.

**Borrador de trabajo:** «Documentado» identifica una respuesta presente en el diseño, sin acreditar pruebas, revisión humana ni aceptación contractual. Los cierres pendientes se conservan dentro de la columna «Respuesta» y se desarrollan en la matriz posterior. La tercera columna identifica secciones, anexos, figuras, tablas y formularios de la propuesta; las páginas incluidas en la primera columna pertenecen al Informe 1. No se añaden páginas del PDF actual sin un cotejo nuevo.

## Observaciones del Informe 1

La numeración correlativa facilita comparar esta tabla con las de los otros subdocumentos. Cada respuesta explica el cambio o la evidencia disponible y conserva su condición de cierre.

| Observación del Informe 1 | Respuesta | Sección modificada |
| --- | --- | --- |
| 1. **EL-01** — Texto y diagramas desconectados, pp. 9–10 | Las figuras de las capas se citan antes de aparecer y se explican inmediatamente después, vinculando el recorrido gráfico con el texto. **Estado y cierre:** Documentado; comprobar legibilidad final. | SD4, §4.1.3; figuras 1–12. |
| 2. **EL-02** — Trece recorridos por actor redundantes y sin explicación, p. 9 | Los trece recorridos por actor se sustituyen por una vista general, ocho vistas por capa, secuencias y una matriz de actores. **Estado y cierre:** Sustitución documentada; cotejar permiso local de Calidad en figuras. | SD4, §4.1.3; Anexo 4-N, matriz de actores. |
| 3. **EL-03** — Actores declarados distintos de los dibujados, p. 9 | Se identifican quince actores y se describen sus perfiles y ámbitos de autorización. La coincidencia con las figuras todavía requiere cotejo gráfico. **Estado y cierre:** Cotejo gráfico final pendiente. | SD4, §§4.1.3.1 y 4.1.18; Anexo 4-N. |
| 4. **EL-04** — Matriz requisito → módulo → capa ausente, p. 9 | El T-12 identifica los requisitos individualmente; 4-E agrupa familias y 4-N relaciona módulos, 37 componentes transversales y realización física. La Tabla 6 y el T-11 completan el emplazamiento y los recursos. **Estado y cierre:** Cadena documentada; cotejo individual de suficiencia en curso (P-01) y referencias externas desactualizadas en 75 filas (P-02). | Formulario T-12; anexos 4-E y 4-N, Tabla A.14; SD4, §4.2.2, Tabla 6; Formulario T-11. |
| 5. **EL-05** — Cinco ambientes solo nombrados, p. 9 | Los cinco ambientes tienen desarrollo por separado y figuras propias. La topología AWS identifica las regiones de producción y recuperación. **Estado y cierre:** Documentado por ambiente. | SD4, §§4.1.9 y 4.2.4.1; figuras 19–23 y Figura 18. |
| 6. **EL-06** — SOLID y patrones sin aplicación, pp. 9–10 | Se desarrolla la aplicación de SOLID mediante contratos de negocio y límites entre módulos, junto con los patrones de diseño y continuidad. **Estado y cierre:** Documentado; pruebas de dependencia/contrato por ejecutar. | SD4, §§4.1.10 y 4.1.10.1. |
| 7. **EL-07** — Seis vistas declaradas sin vista de procesos, p. 10 | Se establece la correspondencia de las cinco vistas exigidas y se incorporan secuencias de procesos. **Estado y cierre:** Corregido documentalmente. | SD4, §4.1.14; figuras 8–9; Anexo 4-S. |
| 8. **EL-08** — Estilo modular pertinente al caso, p. 10 | Se mantiene el estilo modular valorado por el evaluador; Laravel/PHP conserva límites entre los módulos y su elección queda justificada en ADR-01. **Estado y cierre:** Observación positiva conservada; framework actualizado. | SD4, §4.1.13; Anexo 4-O, ADR-01. |
| 9. **EL-09** — Comparación insuficiente y ADR fuera de lógica, p. 10 | Se comparan alternativas arquitectónicas en el cuerpo y se conserva un registro único de 22 ADR en el anexo lógico, sin repetir sus fichas en el cuerpo. **Estado y cierre:** Documentado, sin repetir fichas en cuerpo. | SD4, §4.1.13, Tabla 4; Anexo 4-O. |
| 10. **EL-10** — Doce módulos anunciados sin inventario, p. 10 | Los doce módulos cuentan con inventario de nombre, responsabilidad, contratos, actor y etapa. **Estado y cierre:** Documentado. | Anexo 4-D. |
| 11. **EL-11** — Límites, interfaces, orquestación y coreografía ausentes, p. 10 | Se desarrollan límites de contexto, interfaces internas y externas, y la relación entre orquestación y coreografía mediante contratos y secuencias. **Estado y cierre:** Documentado. | SD4, §4.1.3.5; figuras 8–9; anexos 4-F, 4-G y 4-H. |
| 12. **EL-12** — Marco TOGAF solo citado, p. 10 | La descripción aplica ISO 42010 mediante interesados, preocupaciones y correspondencias entre vistas. No se presenta la mención de TOGAF como evidencia de aplicación. **Estado y cierre:** Se usa el marco desarrollado; no se afirma aplicación de TOGAF por su sola mención. | Anexo 4-S. |
| 13. **EL-13** — Modelo de dominio solo como lista, p. 10 | Se incorpora un modelo conceptual del dominio y se relacionan sus productores con los eventos canónicos. El esquema relacional se remite al SD5. **Estado y cierre:** Documentado; esquema relacional pertenece a SD5. | SD4, §4.1.5, Figura 13; Anexo 4-A. |
| 14. **EL-14** — Caché de 8 h incompatible con 24 h y relevos, p. 10 | El diseño usa caché de 24 horas, manifiesto de 26 horas, credenciales personales y verificador local. AL-OFF-01 incluye relevos a las 8 y 16 horas durante el corte. **Estado y cierre:** Diseño documentado; probar vigencias, permisos, reinicio y reconciliación; una copia vigente no renueva credenciales ni autoriza terceros (P-05). | SD4, §§4.1.3.7 y 4.1.15; anexos 4-J y 4-M, AL-OFF-01. |
| 15. **EL-15** — Gateway solo remoto para HHT, p. 10 | La puerta de API local A-01 se ejecuta en VM-01, VM-C01 y E-01, de modo que el HHT no depende de API Gateway durante un corte de WAN. **Estado y cierre:** Documentado; no depende de API Gateway durante corte. | SD4, §§4.1.3.3 y 4.2.2; Figura 5; Anexo 4-N. |
| 16. **EL-16** — Bloqueo térmico decidido por conductor frente a automático, p. 10 | M9 bloquea preventivamente una excursión crítica y sostenida; la disposición sanitaria corresponde a Calidad con evidencia y permisos. **Estado y cierre:** Bloqueo documentado; cotejar etiquetas gráficas y recorrido local autorizado de Calidad antes de cerrar la autonomía de disposición (P-03/P-06). | SD4, §4.1.4.2; anexos 4-J, 4-M y 4-N. |
| 17. **EL-17** — Etapas discordantes con SD3, p. 10 | Se declaran las etapas por módulo, la implantación progresiva y la remisión al calendario. La consistencia con el SD3 vigente permanece por comprobar. **Estado y cierre:** Contrastar contra SD3 vigente sin editarlo. | SD4, §4.1.8; Anexo 4-D; contraste externo con SD3 y calendario. |
| 18. **EL-18** — Portales externos tratados como intranet/VPN, p. 10 | Se distinguen entradas públicas, privadas y locales. Verified Access se reserva a oficina y consolas, sin exigir VPN para los portales externos públicos. **Estado y cierre:** Documentado; Verified Access reservado a oficina/consolas. | SD4, §§4.1.3 y 4.2.5.2. |
| 19. **EL-19** — Portada promete física pero solo incluye lógica, p. 10 | El cuerpo integrado incluye arquitectura lógica, física y centros de datos bajo la estructura 4.1–4.3. **Estado y cierre:** Corregido en estructura. | SD4, portada y §§4.1–4.3; ensamblador integrado. |
| 20. **EL-20** — Códigos y versiones sin documento entregado, p. 10 | Se identifica el catálogo físico A/B/C/D/E/F/N, el inventario lógico y los contratos internos y externos. Queda comprobar que las imágenes no conserven códigos históricos. **Estado y cierre:** Verificar etiquetas residuales en imágenes; no mezclar códigos históricos. | SD4, §4.2.2; anexos 4-N, 4-G y 4-H; Formulario T-11. |
| 21. **EL-21** — Plantilla distinta e ilegibilidad, p. 10 | Los tres entregables usan plantilla común. El cuerpo conserva 26 tablas técnicas breves y su declaración de IA; la red se presenta mediante tres activos gráficos actuales. **Estado y cierre:** Formato documentado; el registro histórico de rótulos próximos a 5 puntos no describe por sí solo los nuevos activos de red. Revisar su impresión final (P-04). | SD4, cuerpo y figuras; anexos y T-11; registro AUDITORIA_TABLAS_SD4.md. |
| 22. **EF-01** — Documento duplicado y sin portada, p. 11 | Se organiza un cuerpo integrado, con anexos y T-11 como documentos independientes, evitando la duplicación estructural de la entrega preliminar. **Estado y cierre:** Estructura corregida. | SD4, portada y ensamblador; documentos de anexos y Formulario T-11. |
| 23. **EF-02** — Comentarios de IA, versiones y auditorías dentro de la oferta, p. 11 | El barrido previo separó las notas de trabajo de la oferta. Se conserva la declaración obligatoria de IA con sus celdas de revisión humana pendientes. **Estado y cierre:** Revisión humana real pendiente (P-11); comprobar ausencia de notas de proceso en la revisión final, sin retirar la declaración obligatoria. | SD4, declaración de uso de IA; registros de revisión externos al entregable. |
| 24. **EF-03** — Tabla de emplazamiento inexistente/incompleta, p. 11 | El emplazamiento se relaciona con los doce módulos y las 37 capacidades transversales. La matriz de correspondencia, el inventario y el T-11 identifican su realización física. **Estado y cierre:** Doce módulos y 37 transversales inventariados; cotejo individual necesario para confirmar realización física y cobertura de requisitos (P-01). | SD4, §4.2.2, Tabla 6; Anexo 4-N, Tabla A.14; Anexo 4-W, Tabla A.35; T-11. |
| 25. **EF-04** — Figura física ilegible y sin explicación, p. 11 | La vista física general se acompaña de explicaciones y vistas de sitios, emplazamiento, nube y recuperación. Las tres vistas de red detallan la conexión local y regional. **Estado y cierre:** Explicación presente; cotejar correspondencia con recuperación y legibilidad actual (P-03/P-04/P-07). | SD4, §§4.2 y 4.3; Figura 14, figuras 15–18 y 23–26. |
| 26. **EF-05** — Descripciones verbales sustituyen dibujos, pp. 12–13 | Se incorporan dibujos de ambientes, nube, sitios, racks y recinto. Las tres vistas de red forman parte del desarrollo y tienen explicación propia. **Estado y cierre:** Incorporación documental corregida; queda revisión de correspondencia gráfica y legibilidad (P-03/P-04). El borrador de propuestas no es el activo entregado. | SD4, §4.2.4.2, figuras 24–26; §4.3.1.4, figuras 28–29; vistas de ambientes y sitios. |
| 27. **EF-06** — BI ocupa catorce páginas ajenas al ítem, p. 12 | El SD4 conserva la función lógica y el emplazamiento de M10. El modelo analítico detallado se remite al SD5. **Estado y cierre:** Mantener solo justificación y dependencias arquitectónicas. | SD4, §§4.1.4.7 y 4.2.2; remisión a SD5. |
| 28. **EF-07** — Implementos pertinentes, p. 12 | Se mantiene el contenido valorado positivamente: el T-11 identifica modelos de implementos, cantidades y finalidad. **Estado y cierre:** Observación positiva conservada. | Formulario T-11. |
| 29. **EF-08** — Cantidades sin número y ciclo de vida/caídas omitidos, p. 12 | Se explicitan cantidades y criterios de aceptación por tipología, junto con los cálculos del parque y el control de actualizaciones. La aceptación física debe verificarse por ensayo. **Estado y cierre:** Comprobar especificación de aceptación por tipo; cálculos no equivalen a ensayo. | SD4, §4.2.1.2; Anexo 4-W.3; Anexo 4-P; Formulario T-11. |
| 30. **EF-09** — Exceso de equipos congelados/POS/impresoras, p. 12 | El parque se deriva de la dotación por turno y sus reservas: 207 terminales al inicio y 235 en el año 3, incluidos repuestos. La concurrencia nocturna inicial es 186. **Estado y cierre:** Cifras derivadas; 186 es concurrencia nocturna inicial. Precisar el perfil temporal de la campaña de Preproducción que menciona 207 (P-09). | SD4, §§4.2.1 y 4.1.9; Anexo 4-W.3; Formulario T-11. |
| 31. **EF-10** — Frío solo en 18 camiones y alertas al regreso, p. 12 | Se declaran 28 termógrafos: 18 en camiones propios y 10 en camiones externos. La lectura BLE y la alerta local se producen durante la ruta. **Estado y cierre:** Corregido en diseño; ensayo de lectura/alerta por ejecutar. | SD4, §4.1.4.2; Anexo 4-W.4; Formulario T-11, B-03. |
| 32. **EF-11** — Estudio de cobertura inalámbrica insuficiente, p. 12 | Se incluye el estudio de cobertura y la aceptación de las interfaces en cámaras de frío. La propuesta no presenta la estimación como cobertura ya medida. **Estado y cierre:** Estudio y medición necesarios; no inventar cobertura medida. | SD4, §4.2.1.2; criterios de aceptación de interfaces y cámaras. |
| 33. **EF-12** — Sala secundaria sobredimensionada y Tier incoherente, p. 12 | El dimensionamiento usa el equipamiento real del recinto y distingue disponibilidad por componente de disponibilidad de extremo a extremo. **Estado y cierre:** Documentado; ninguna categoría Tier sustituye demostrar disponibilidad. | SD4, §4.3.1.4 y desarrollo de disponibilidad. |
| 34. **EF-13** — Sin cálculo eléctrico/térmico, plano ni racks, p. 12 | Se desarrollan cargas eléctricas y térmicas, memoria de cálculo, distribución de racks y plano del recinto. **Estado y cierre:** Evidencias presentes; verificar correspondencia gráfica final (P-03) y actualizar referencias externas del T-12 (P-02). | SD4, §4.3.1.4, Tablas 23–24 y figuras 28–29; Anexo 4-W.8. |
| 35. **EF-14** — Gabinetes de borde sin energía/clima/acceso, p. 12 | Los gabinetes de borde cuentan con representación gráfica y definición de energía, climatización, acceso y carga/UPS por tipología. **Estado y cierre:** Documentado por tipología. | SD4, §4.2.1.2, figuras 15–16; Anexo 4-W, Tabla A.39; Formulario T-11. |
| 36. **EF-15** — Aprobación de DR podría llevar RTO a 24–72 h, p. 12 | Se declaran las regiones, RTO de hasta 4 horas y aprobación de residencia como hito contractual. La consulta sanitaria regional de solo lectura tiene un presupuesto de 75 minutos, sujeto a prueba. **Estado y cierre:** Diseño documentado; medir restitución por servicio, conectividad de Talca y consulta sanitaria (P-07); residencia y brecha extrema de RPO requieren decisión contractual real (P-08). | SD4, §4.3.2; Anexo 4-M, AL-DR-01; Formulario T-11. |
| 37. **EF-16** — T-11 invocado pero no adjunto, p. 12 | El T-11 existe como Markdown propio y PDF independiente; los registros conservan la compilación efectuada en la ejecución correspondiente. **Estado y cierre:** Presente; verificación de compilación registrada abajo. | Formulario T-11, archivo independiente; registros de compilación. |
| 38. **EF-17** — Zero Trust y SPOF pertinentes, p. 12 | Se mantienen Zero Trust, el análisis de puntos únicos de falla y el respaldo 3-2-1-1-0, con remisión a su desarrollo principal. **Estado y cierre:** Contenido conservado; remitir a sección principal sin repetir controles. | SD4, §§4.1.3.7 y 4.2.5; anexos 4-Q y 4-R; respaldo y continuidad. |
| 39. **EF-18** — Funciones offline y limitaciones omitidas, p. 13 | Se distinguen funciones disponibles y bloqueadas durante un corte: captura local, relevos, guía preemitida y autorizaciones externas condicionadas. **Estado y cierre:** Funciones y límites documentados; probar continuidad completa, no solo captura; completar cotejo del acceso local de Calidad (P-05/P-06). | SD4, §§4.1.15–4.1.16; anexos 4-J, 4-K y 4-M. |
| 40. **EF-19** — Ceph sobre RAID y capacidad contradictoria, p. 13 | Se define Ceph con seis OSD sin RAID, size=3/min_size=2, redundancia N+1 y cálculo de capacidad. **Estado y cierre:** Diseño documentado; fallo y reconstrucción por probar. | SD4, arquitectura física de Talca; Anexo 4-W.8. |
| 41. **EF-20** — DTE diferido contradice único emisor/guía previa, p. 13 | El ERP conserva la emisión previa de la guía. Un cambio de carga invalida la preemisión y requiere otra guía válida; AL-DTE-01 define el ensayo. **Estado y cierre:** Documentado; 96 salidas requieren prueba completa y documentos válidos. | SD4, §4.1.17; anexos 4-M y 4-U, AL-DTE-01. |
| 42. **EF-21** — Dotación incompatible con cuatro TI, p. 13 | El dimensionamiento incorpora dotación propia para NOC/SOC y mesa de servicios, diferenciándola de los cuatro TI del cliente. **Estado y cierre:** Dimensionamiento presente; los cuatro TI del cliente no operan solos toda la plataforma. | SD4, §4.2.6; Anexo 4-W.7. |
| 43. **EF-22** — Sin red, despliegue ni zonas de seguridad, p. 13 | Se desarrollan cinco ambientes, topología AWS, tres vistas de red y direccionamiento con zonas de segmentación. **Estado y cierre:** Red y segmentación incorporadas documentalmente; pendientes legibilidad y cotejo de rutas, zonas y recursos de recuperación (P-03/P-04/P-07). | SD4, §§4.2.4.1–4.2.4.2; figuras 24–26; Tabla 9. |
| 44. **EF-23** — TPS sin sustento y regímenes mezclados, p. 13 | Los cálculos separan operación normal, ventanas horarias y carga de septiembre, con su derivación en la memoria. **Estado y cierre:** Cálculos documentados; prueba no ejecutada. | SD4, §§4.2.6.2–4.2.6.3; Anexo 4-W. |
| 45. **EF-24** — Dieciséis dimensiones ausentes o sin derivación, pp. 13–14 | Las dieciséis dimensiones se sintetizan en el anexo y se justifican mediante derivaciones y cuadros numéricos del cuerpo. **Estado y cierre:** Método documentado; cotejar suficiencia de cada dimensión y validar cotas por medición (P-01/P-09). | SD4, §4.2.6.12; Anexo 4-W, Tabla A.30 y memoria de cálculo. |
| 46. **EF-25** — ADR con precios, p. 13 | El registro único de ADR se presenta mediante decisiones cualitativas y técnicas. La ausencia de precios debe mantenerse en la revisión final de la oferta. **Estado y cierre:** Mantener control de ausencia de precios en toda la oferta técnica. | Anexo 4-O; control final del conjunto de la oferta técnica. |

## Seguimiento de los pendientes

Los roles siguientes son responsables sugeridos por función, no personas asignadas ni compromisos aceptados. No se inventan fechas ni resultados. Cada punto permanece pendiente hasta registrar la evidencia indicada y su revisión.

| ID | Observaciones relacionadas | Acción y evidencia de cierre | Responsable sugerido / momento | Estado |
| --- | --- | --- | --- | --- |
| P-01 | EL-04, EF-03, EF-24 | Revisar cada requisito aplicable: requisito → capacidad SD3 → módulo/capa → recurso físico → T-11 → verificación. Registrar cobertura completa, parcial o ausente y contradicciones; justificar inaplicabilidad cuando corresponda. | Arquitectura y requisitos / antes de declarar conformidad documental | En curso: control estructural de 499 filas y cotejo semántico dirigido registrados; auditoría semántica total pendiente |
| P-02 | EL-04/20, EF-03/13/24 | Corregir las referencias externas identificadas en el informe de cotejo: 34 formas de cita desactualizadas, 82 menciones y 75 filas distintas. En particular, RT-06.02/03/22/30 deben citar Figura 29 (recinto) y RT-06.05 Figura 28 (racks). Cotejar destinos y temas después de editar T-12. | Responsable SD3/T-12 / coordinación documental | Pendiente externo ampliado; no se edita T-12 en esta actualización |
| P-03 | EL-02/03/16/20, EF-04/05/13/22 | Cotejar figuras con quince actores, permisos, códigos, emplazamientos y rutas de recuperación; dejar registro de cada discrepancia o conformidad. | Arquitectura / revisión gráfica final | Pendiente; incorporación de la red comprobada en fuentes |
| P-04 | EL-01/21, EF-04/05/22 | Revisar PDF actual a tamaño de impresión, incluidas las tres vistas de red; acreditar legibilidad según las Aclaraciones y revisar su nueva paginación. La medición histórica de la red anterior no certifica ni invalida estos activos nuevos. | Diagramación y arquitectura / antes de entregar | Pendiente de comprobación del PDF actual; los controles de tablas no cierran figuras |
| P-05 | EL-06/14/15, EF-18/20 | Ejecutar pruebas de contratos/dependencias y AL-OFF-01/AL-DTE-01 aplicables: 24 h, relevos, expiración, reinicio, reconciliación, guía válida y cambio de carga. Registrar casos, resultados y evidencias; incluir las 96 salidas del escenario DTE. | Desarrollo y QA / etapa de aceptación aplicable | Pendiente de ejecución; no impide registrar el diseño como documentado |
| P-06 | EL-16, EF-18 | Cotejar y concretar el acceso local de Calidad: interfaz, dispositivo, identidad, permisos y auditoría. Probar el recorrido antes de acreditar nueva disposición durante aislamiento. | Arquitectura, seguridad y Calidad / definición y aceptación | Pendiente de cotejo y aceptación; no inferir autorización desde la captura local |
| P-07 | EF-04/15/22 | Concretar y ensayar recuperación por servicio y pérdida completa de Talca incluyendo LAN, firewall y VPN dentro del RTO. Probar consulta sanitaria con región primaria caída, lista completa y evidencia en menos de 2 h; los 75 min son presupuesto de diseño. | SRE, redes, QA y Calidad / aceptación de continuidad | Pendiente de evidencia ejecutada |
| P-08 | EF-15 y límites de cierre | Obtener aprobación de residencia; presentar al mandante aislamiento total seguido de destrucción, desfase recuperable y alternativas. Registrar decisión contractual; R8-05 no equivale a excepción aprobada. | Responsable contractual y mandante / hito y decisión correspondientes | Pendiente contractual; riesgo extremo de RPO abierto |
| P-09 | EL-05, EF-08/09/10/11/12/14/19/21/23/24 | Verificar aceptación por tipología, caídas, frío/alerta en ruta, cobertura inalámbrica, sincronización simultánea, capacidad y disponibilidad; ejecutar fallas/reconstrucción de Ceph. Distinguir 207 terminales iniciales de 235 en año 3 al declarar las campañas de Preproducción. Conservar cálculos y registrar mediciones separadamente. | Infraestructura, redes, operación y QA / aceptación aplicable | Cálculos documentados; precisión temporal de campaña y ensayos pendientes |
| P-10 | EL-17 | Contrastar etapas de 4-D y 4.1.8 con SD3 y calendario vigentes; registrar coincidencias y resolver diferencias por coordinación. | Arquitectura y planificación / revisión documental cruzada | Pendiente; no se modifica SD3 |
| P-11 | EF-02 y declaración de IA | Integrante humano revisa realmente las secciones, anexos y T-11; completar declaración con esa evidencia, sin fabricar revisión. | Integrantes responsables / antes de entrega | Pendiente; la auditoría de tablas conserva 56 celdas sin revisión humana |
| P-12 | EF-06/17/25 | En revisión editorial final, confirmar BI limitado a justificación arquitectónica, remisiones sin duplicación innecesaria y ausencia de precios en oferta técnica. | Revisión técnica/editorial / antes de entrega | Control final pendiente; contenido previamente documentado |
| P-13 | EL-04/11, EF-03/20 | Cotejar RT-16.16/18: enlazar evidencia directa de cifrado, integridad y retención en 4.1.17/4-U/4.2.4.5; comprobar qué mecanismo satisface el sello de tiempo y la verificación después de vencer el certificado. Una marca temporal de registro requiere justificación de suficiencia. | Seguridad, integración documental y QA / definición y aceptación | Pendiente de cotejo específico; no se afirma ausencia de todo el mecanismo |

## Cambios de diseño de la ejecución original

1. Sincronización: 43 dispositivos en Talca y 21 en Concepción requieren 5,64/2,75 Mbps útiles. Sumados a 1,87/1,44 de drenaje y con 15 % de margen, dan 8,64/4,82 Mbps. Mínimos de aceptación adoptados: 10/6 Mbps de subida sostenida en LTE y satélite de los CD. Las cifras horarias 5,16/2,14 no representan este escenario. Manteniendo oficina sobre fibra, las cotas simultáneas son 9,87/4,42 Mbps.
2. Consulta sanitaria de emergencia: acceso privado y M9 de solo lectura sobre Aurora/S3 secundarios, sin promover el escritor ni esperar el cambio general de DNS. Presupuesto propuesto de 15 min para acceso y 60 min para consulta/evidencia. Se rechaza acreditar listas incompletas. Se incorpora a ADR-09, T-11 y AL-DR-01.
3. RPO extremo: aislamiento de todos los medios seguido de destrucción queda identificado como brecha a resolver contractualmente. R8-05 no constituye aprobación de una excepción. No existe garantía de transmitir datos nuevos si no queda ningún medio disponible.
4. Concisión: 784 palabras del inventario detallado de tecnologías pasan de 4.1.7 al Anexo 4-P. El cuerpo mantiene la síntesis y los criterios; se conservan encabezados obligatorios, contratos y condiciones de continuidad.
5. Se distingue parque de 207 terminales instalado de concurrencia nocturna de 186; Preproducción cubre el parque y el perfil de carga pertinente.

## Dos trazabilidades distintas

La tabla de este registro sigue observación → evidencia → acción → cierre. La trazabilidad contractual sigue RF/RNF/RT → capacidad SD3 → módulo/capa → recurso físico → T-11 → verificación. No se sustituye la segunda por este registro.

La continuación recalculó 645 filas del T-12, incluidas las variantes con sufijo `-BTT`: 499 citan SD4 o sus anexos, y otras seis citan T-11 sin SD4. Se resolvieron 752 menciones explícitas a secciones del cuerpo en 83 encabezados distintos de sus 108 encabezados numerados. Este control no acredita que cada referencia sea suficiente para todo el requisito. Se encontraron 34 formas de cita numérica desactualizadas en 75 filas distintas. El Anexo 4-E agrupa familias y enlaza el T-12; 4-N/Tabla A.14, Tabla 6 y T-11 completan la realización física. El análisis semántico dirigido y el inventario de correcciones están en [el informe de cotejo](#cotejo-contractual-complementario); la auditoría semántica completa permanece en curso (P-01). No se editó T-12 ni otro subdocumento.

## Red actual, activo anterior y borradores conservados

La fuente local actual incorpora tres activos en 4.2.4.2: red general (archivo del checkout LaTeX: `04/figuras/fisica/Red_01_general_legible.pdf`), red local (archivo del checkout LaTeX: `04/figuras/fisica/Red_02_sitios_legible.pdf`) y conectividad regional (archivo del checkout LaTeX: `04/figuras/fisica/Red_03_regiones_legible.pdf`), como figuras 24, 25 y 26. Se acompañan de explicación y de la Tabla 9 de direccionamiento y segmentación. El cierre gráfico sigue condicionado a P-03/P-04; esta continuación no mide tipografía ni inspecciona nuevamente el PDF.

Se conserva el activo anterior Red_general_sitios_regiones.pdf (archivo del checkout LaTeX: `04/figuras/fisica/Red_general_sitios_regiones.pdf`), con fuente Red_general_sitios_regiones.drawio (archivo del checkout LaTeX: `04/figuras/fuentes/fisica/Red_general_sitios_regiones.drawio`). El registro de alineación identifica ese XML corregido por el usuario y su SHA-256 `912bf7b551a9bd005b9e8f00b39d265faa7ff34221b6934f33cf4ee33b841aac`. Esa huella y sus observaciones de impresión no se atribuyen automáticamente a los tres activos actuales.

Los archivos siguientes se conservan como borradores históricos, no como evidencia de la figura entregada:

Archivo editable: Red_integral_SD4.drawio (archivo del checkout LaTeX: `04/figuras/propuestas/Red_integral_SD4.drawio`), dos páginas preparadas para explicación independiente. Preliminares: sitios y regiones (archivo del checkout LaTeX: `04/figuras/propuestas/Red_integral_SD4.png`) y segmentación (archivo del checkout LaTeX: `04/figuras/propuestas/Segmentacion_SD4.png`).

El borrador reutiliza iconos AWS, grupos de región/VPC y cajas del vocabulario gráfico de los ambientes existentes. Los mínimos de ancho de banda son decisiones de diseño, no capacidades medidas. La incorporación posterior corresponde al activo aprobado identificado arriba, no a la aprobación automática de estos borradores.

## Verificación de la ejecución original — antecedente histórico

- Se registran 46 observaciones (EL-01–EL-21 y EF-01–EF-25), incluidas las positivas y las de forma, con la página de origen y la evidencia actual.
- Se comprobaron 340 enlaces Markdown locales, sus destinos y anclas, sin errores; el cuerpo conserva 25 figuras y 40 tablas. No se insertó la propuesta como figura aprobada.
- El contraste automatizado de 184 líneas de contenido añadidas o modificadas encuentra su texto en los fragmentos LaTeX. El encabezado de la tabla transversal requiere lectura manual porque el fuente lo agrupa con título y especificación de columnas; su texto se comprobó directamente. Este cotejo cubre las modificaciones, no certifica todas las versiones históricas de las figuras.
- Los tres PDF se compilaron con LuaLaTeX y pasadas para estabilizar referencias. Registros finales sin referencias indefinidas, destinos repetidos, caracteres faltantes ni desbordamientos. Cuerpo: 188 páginas; anexos: 91; T-11: 46. Son conteos de la salida, no un criterio de aprobación.
- Se inspeccionaron muestras de capacidad y de la tabla T-11, y las dos vistas de la propuesta. El T-11 usa orientación horizontal y ancho real de página; el detalle extenso de administración por familia se conserva en 4-P y su fila queda como síntesis. No se redujo la tipografía para acomodarlo.
- `git diff --check` pasó en ambas ramas. Los cambios Markdown versionables se limitan a los tres entregables SD4; la carpeta `md para drive/`, los stashes y `05/` permanecen preservados. No se actualizaron copias de Drive ni otros subdocumentos.

## Controles posteriores registrados

- El registro de alineación informa cero diferencias normalizadas en 1.579 bloques del cuerpo, 948 de anexos y 110 de T-11; 27 figuras con activos y 342 enlaces internos. Su compilación registró 191 páginas de cuerpo, 91 de anexos y 46 de T-11. Son resultados de esa ejecución, no una nueva compilación realizada para actualizar esta tabla.
- La auditoría posterior de tablas reemplaza esos conteos de contenido y enlaces: cero diferencias en 1.568 bloques de cuerpo, 1.050 de anexos y 110 de T-11; 343 enlaces internos y 27 figuras conservadas. Registra 26 tablas técnicas más la declaración de IA en cuerpo, 40 tablas en anexos y la tabla oficial de T-11. Su mapa sustenta las referencias numéricas actualizadas aquí.
- La actualización de este registro conserva los 46 ID y añade doce pendientes con evidencia de cierre y responsables sugeridos. No acredita una nueva revisión visual, cotejo contractual completo, medición, compilación ni revisión humana.
- La continuación agrega P-13, actualiza el universo de referencias y coteja las fuentes efectivas: 29 figuras, 27 tablas de cuerpo y 40 de anexos. Racks y recinto son figuras 28 y 29. Los conteos de 27 figuras de los registros previos se conservan solo como antecedentes históricos. Se registra el cotejo estructural completo y el análisis semántico dirigido sin declarar conformidad global.

## Límites del cierre

Pruebas de autonomía, recuperación, consulta sanitaria y caudal siguen siendo criterios de aceptación por ejecutar. La revisión humana de IA se conserva pendiente. Las figuras heredadas necesitan comprobar etiquetas y modelos con el texto actual; el límite extremo de RPO requiere resolución del mandante. No se declara conformidad total por la sincronización ni por compilar.

## Registro de actualización y preservación

La homologación de formato conserva las 46 observaciones, sus identificadores, las condiciones de cierre y los 13 pendientes. Se separa la explicación de la respuesta de la ubicación de su evidencia. No constituye una nueva comprobación técnica ni actualiza los estados por los cambios locales de otras tareas. Solo se modifica este registro, sin editar entregables ni T-12, y sin commit o push.

## Actualización del estado — 11 de octubre de 2026

Esta actualización revisa el registro a partir de las observaciones identificadas en la conversación, las fuentes locales de SD4 y los registros posteriores [de alineación](ALINEACION_MD_LATEX_SD4_2026-10-11.md) y [de auditoría de tablas](AUDITORIA_TABLAS_SD4.md). Conserva las 46 observaciones originales y no ejecuta una nueva auditoría requisito por requisito ni pruebas técnicas. La rama comprobada es `subdoc-4`; se preservan sus modificaciones locales existentes. En esta actualización solo se editó este registro Markdown, entonces sin commit ni push, modificación de entregables ni cambios al T-12.

Los conteos, compilaciones y comprobaciones de las ejecuciones anteriores se identifican como antecedentes; no se presentan como controles ejecutados nuevamente. Los pendientes cuentan con condición de cierre en la matriz de seguimiento situada después de la tabla principal. La continuación del cotejo se registra en [el cotejo contractual complementario](#cotejo-contractual-complementario): se comprueban las referencias estructurales de las 499 filas que citan SD4 y se inicia el cotejo semántico dirigido, sin declarar terminado el análisis individual de todas ellas.

## Versiones y preservación de la ejecución original

- `rama-md`: actualizado desde `baf991d` a `cf43057` mediante fetch y pull fast-forward; mejoras locales de los tres archivos SD4 reaplicadas sin conflictos. Respaldo recuperable: stash `respaldo SD4 antes de pull plan concision 2026-10-11`.
- `subdoc-4`: actualizado de `ca84689` a `292c6e8` mediante fetch y pull fast-forward. Se preserva la carpeta local no versionada `05/`.
- En Markdown se modifican únicamente cuerpo SD4, anexos SD4 y T-11. En LaTeX se sincronizan sus fragmentos y se preparan las propuestas y herramientas de este subdocumento. Sin commit ni push en esta ejecución.


## Cotejo contractual complementario

Copia publicada en `rama-md` el 12 de octubre de 2026. Se conserva el corte de revisión del 11 de octubre de la fuente en `subdoc-4`; los conteos y pendientes siguientes no constituyen un recálculo sobre el T-12 actualizado después de ese corte.

Fecha: 11 de octubre de 2026. Registro de trabajo en `subdoc-4`. Se conserva el estado local de ambos checkouts. Se revisan fuentes Markdown y fragmentos LaTeX actuales; no se modifica T-12 ni el contenido de los entregables.

### Alcance y resultado

- T-12 leído: 645 filas, incluidas las variantes con sufijo `-BTT`; 499 citan SD4. Otras seis citan T-11 sin citar SD4, por lo que el universo ampliado es 505 filas.
- Las 752 menciones explícitas a secciones del cuerpo SD4 se resuelven en 83 encabezados distintos, dentro de sus 108 encabezados numerados. No se encontraron secciones inexistentes en esas menciones.
- Se confirmaron 34 formas de referencia desactualizadas a tablas/figuras, repetidas en 82 citas de 75 filas distintas. La existencia de la sección no subsana el rótulo numérico equivocado.
- El cuerpo efectivo contiene 29 figuras: red general 24, red local 25, conectividad regional 26, arquitectura Talca 27, racks 28 y recinto 29. La numeración de 27 figuras de los registros anteriores es histórica.
- El control estructural cubre todas las filas que citan SD4; el cotejo semántico es dirigido a los casos documentados abajo. No se declara concluida la auditoría semántica de las 499 filas ni se cambian sus estados de cumplimiento.

### Referencias externas que requieren corrección

Los destinos se proponen a partir del título y del tema actual. Si una matriz se convirtió en punteos o se trasladó a anexos, se indica ese destino; no se realiza sustitución aritmética de números. Los casos condicionados requieren leer el requisito antes de editar T-12.

| Cita actual del T-12 | Filas afectadas | Destino vigente / revisión necesaria |
| --- | --- | --- |
| SD4-Anexos 4-O (Tabla A.17) | RF-13.03, RT-02.04 | 4-O, Tabla A.18 (resumen ADR); A.19 para fecha y estado. |
| SD4-Anexos 4-R (Tabla A.23) | RF-14.01-BTT, RF-14.02-BTT, RF-19.01, RF-19.02, RNF-14.04, RNF-14.05, RNF-14.07, RNF-14.09, RNF-15.03, RNF-16.03, RT-11.03, RT-11.05, RT-11.16, RT-11.17, RT-12.09, RT-14.07 | 4-R, Tabla A.25 (controles). A.23 corresponde ahora a amenazas de módulos. |
| SD4 4.2.5.2 (Tabla 19) | RF-14.03-BTT, RF-19.03, RT-11.13 | 4.2.5.2, Tabla 11 (superficie de exposición). |
| SD4-Anexos 4-R (Tabla A.23, controles 5.24 y 5.26) | RF-14.04-BTT, RF-19.04, RT-11.18 | 4-R, Tabla A.25, controles 5.24 y 5.26. |
| SD4-Anexos 4-P (Tabla A.19) y 4-R (Tabla A.23) | RF-15.03 | 4-P, Tablas A.20–A.21 según tecnología y soporte; 4-R, Tabla A.25. |
| SD4 4.2.6.11 (Tabla 31) | RF-17.11, RT-09.01, RT-09.02, RT-09.05, RT-16.27 | 4.2.6.11, Tabla 22 (pruebas de dimensionamiento). |
| SD4-Anexos 4-P (Tabla A.19) | RF-17.13, RNF-21.09, RT-13.10, RT-17.03, RT-17.04, RT-17.05, RT-17.08 | 4-P, Tablas A.20–A.21 según el componente y la vigencia exigidos; verificar el detalle de cada fila. |
| SD4 4.1.17 y 4.2.4.5 (Tabla 17) | RF-18.01, RT-16.18 | 4.1.17 y listado de retención por dominio de 4.2.4.5; completar con 4-U para evidencia documental. |
| SD4 4.2.4.2 (Tabla 15) y 4.2.5.2 (Tabla 19) | RNF-14.03, RT-03.04 | 4.2.4.2, clasificación de servicios en punteos y Tabla 9 de segmentación según requisito; 4.2.5.2, Tabla 11. |
| SD4-Anexos 4-R (Tabla A.23, controles 8.10 y 8.11) | RNF-14.10, RT-11.25 | 4-R, Tabla A.25, controles 8.10 y 8.11. |
| SD4-Anexos 4-T (Tabla A.25) | RNF-16.01, RT-09.01, RT-09.06, RT-09.07, RT-14.03 | 4-T, Tabla A.27 (objetivos y escenarios de desempeño). |
| SD4 4.3.2.4 (Tabla 38) y 4.2.4.3 | RNF-20.01 | 4.3.2.4, Tabla 26 (objetivos de continuidad); conservar 4.2.4.3. |
| SD4 4.1.10 y 4.2.4.3 (Tabla 16) | RNF-20.02 | 4.1.10 y listado de respaldo/restauración por dominio en 4.2.4.3. |
| SD4 4.3.2.4 (Tabla 38) | RNF-20.06, RT-07.04 | 4.3.2.4, Tabla 26 (objetivos de continuidad). |
| SD4 4.2.4.2 (Tabla 15) | RT-02.12 | 4.2.4.2, clasificación de servicios en punteos; Tabla 9 si se busca segmentación. Confirmar intención de cada requisito. |
| SD4 4.2.4.5 (Tabla 17) | RT-05.10 | 4.2.4.5, listado de retención por dominio; ya no es Tabla 17. |
| SD4-Anexos 4-P (Tabla A.20) | RT-05.16 | 4-P, Tabla A.22 si la remisión busca la implementación lógica Laravel; A.20 es ahora el ciclo de soporte. |
| SD4 4.3.1.4 (Figura 25) | RT-06.02, RT-06.03, RT-06.22, RT-06.30 | 4.3.1.4, Figura 29 (recinto). |
| SD4 4.3.1.4 (Figura 24) | RT-06.05 | 4.3.1.4, Figura 28 (racks). |
| SD4 4.3.1.4 (Tabla 34) | RT-06.11, RT-08.01 | 4.3.1.4, Tabla 23 (carga eléctrica). |
| SD4 4.3.1.4 (Tabla 35) | RT-06.13 | 4.3.1.4, Tabla 24 (carga térmica). |
| SD4 4.3.2.2 (Tabla 36) | RT-07.02 | 4.3.2.2, Tabla 25 (distancias y amenazas comunes). |
| SD4 4.3.2.3 (Tabla 37) | RT-07.03 | 4.3.2.3, listado de replicación/RPO por dominio. |
| SD4 4.3.2.5 (Tabla 39) | RT-07.05 | 4.3.2.5, secuencia de conmutación en punteos. |
| SD4-Anexos 4-W.8 (Tablas A.34 y A.35) | RT-08.01 | 4-W.8, Tablas A.38 (VM) y A.39 (carga/UPS); comprobar cuál respalda cada magnitud. |
| SD4 4.2.4.3 (Tabla 16) | RT-08.03, RT-10.01, RT-10.02 | 4.2.4.3, listado de respaldo/restauración por dominio. |
| SD4 4.2.6.10 (Tabla 30) | RT-08.05, RT-09.02, RT-09.03 | 4.2.6.10, Tabla 21 (umbrales en percentil 95). |
| SD4 4.2.1.1 (Tabla 7) | RT-08.07 | Inventario trasladado a 4-W/Tabla A.35; conservar justificación de 4.2.1.1 y T-11. |
| SD4 4.2.4.1.1 (Tabla 13) | RT-09.04 | 4.2.4.1.1, Tabla 8 (ventanas de despliegue). |
| SD4 4.2.6.9 (Tabla 29) | RT-09.04 | 4.2.6.9, Tabla 20 (proyección y crecimiento). |
| SD4 4.1.19 (Tabla 6) | RT-09.05 | 4.1.19, Tabla 5 (primer cuello de botella). |
| SD4 4.2.6.12 (Tabla 32) | RT-09.06, RT-09.07, RT-09.08 | Síntesis trasladada a 4-W/Tabla A.30; conservar remisión de 4.2.6.12. |
| SD4 4.2.4.1.4 (Tabla 14) | RT-10.05 | 4.2.4.1.4 y Tabla 9 (direccionamiento/segmentación). |
| SD4-Anexos 4-R (Tabla A.23, controles 8.29, 8.31 y 8.32) | RT-11.27 | 4-R, Tabla A.25, controles 8.29, 8.31 y 8.32. |

### Cotejo semántico dirigido y condiciones de cierre

| Requisito / tema | Evidencia localizada en SD4 y T-11 | Resultado del cotejo / cierre necesario |
| --- | --- | --- |
| RF-01.04, fotografía de no conformidad | 4.1.4.8 y T-11 C-03 estándar premium con cámara trasera de 16 MP. | La configuración antes omitida está declarada. Mantener prueba de captura; no se verificó aquí la ficha externa del fabricante. |
| RF-09.04, frío en 28 camiones | 4.1.4.2, 4-W.4 y T-11 B-03: 18 propios más 10 externos. | Cobertura del parque documentada; lectura, asociación al camión y continuidad durante ruta requieren ensayo. |
| RF-09.05, alerta en cabina y plataforma | T-12 declara BLE al TC58e y reenvío inmediato con cobertura o al recuperarla. | La alerta local tiene recorrido; la plataforma depende de cobertura. Registrar esa limitación al cotejar la exigencia de tiempo real; no afirmar recepción remota durante un aislamiento. |
| RF-09.06, bloqueo y disposición sanitaria | 4.1.4.2 y 4-N identifican A-01/A-02/C-03 y permisos de Calidad; M9 conserva bloqueo preventivo. | Hay realización local declarada, pero falta evidencia de aceptación del recorrido de identidad, permiso, disposición y auditoría; no atribuir la decisión al conductor. |
| RT-03.10, 24 h local y 14 h de terreno | 4.1.15, 4.2.2.7, 4-J/4-M y AL-OFF-01. | Captura y relevo documentados. Despacho depende de guía válida preemitida; cambio de carga exige ERP/servicio tributario. El ensayo debe incluir esa condición. |
| RT-03.13, sincronización y funciones no disponibles | 4.1.15–16, 4-J/4-K y 4-W.6; caudal por simultaneidad y acuse durable. | Cubre ambos significados del código. Los plazos de 10 min/2 h siguen sujetos a medición y reconciliación; el promedio horario no basta. |
| RT-03.24, QoS y estudio de cámaras | 4.2.5.1 desarrolla prioridades; 4.2.1.2 y supuestos S-36 describen estimación y estudio inalámbrico. | El T-12 cita 4.2.4.2 y 4.3.1.4, que no son las referencias más precisas para ambos mecanismos. Añadir los apartados específicos y evidencia de estudio/aceptación; no tratar la estimación de AP como cobertura medida. |
| RT-04.02, equivalencia de Preproducción | 4.1.9 usa 207 terminales; 4.2.4.1 declara diferencias; T-11 y 4-W distinguen 207 al inicio y 235 en año 3. | El parque inicial tiene respaldo y el crecimiento está derivado. Aclarar qué campaña prueba cada parque; no confundir diferencia temporal con concurrencia nocturna de 186. |
| RT-06.02/03/05/22/30, recinto y racks | Los objetos están presentes en 4.3.1.4, figuras 28 y 29. | Error de referencia confirmado en T-12; no equivale a ausencia de los objetos. La revisión gráfica de requisitos materiales sigue pendiente. |
| RT-06.11/13, carga eléctrica y climatización | 4.3.1.4, Tablas 23–24 y memoria 4-W.8. | Hay cálculo/diseño; referencias de T-12 desactualizadas. No acredita medición real ni aceptación de equipos. |
| RNF-20.06 y RT-07.04, RTO/RPO | 4.3.2.3–4, AL-DR-01, exclusión del escritor y restitución de conectividad de Talca. | Brecha contractual real ante aislamiento total seguido de destrucción; su registro en R8-05 no autoriza la excepción. Los estados Cumple del T-12 requieren decisión y justificación antes de acreditar conformidad incondicional. |
| RT-07.05/07, conmutación y pruebas | 4.3.2.5–7 y protocolos AL-DR-01; consulta sanitaria regional prevista en 75 min. | Procedimiento y objetivos documentados; falta evidencia de conmutación real, RTO/RPO y consulta sanitaria completa en menos de 2 h. |
| RT-05.10, linaje y retención | 4.2.4.5 conserva retención por dominio; T-12 declara falta de catálogo con linaje automatizado. | Mantener separación: retención documentada no cierra el linaje faltante. No elevar la fila parcial por actualizar su referencia. |
| RT-16.16, cifrado e integridad de documentos | La cita A.15 de 4-N lleva a una matriz de módulos, no al detalle de custodia. 4.1.17, 4-U y retención 4.2.4.5 desarrollan la evidencia. | Cita existente pero insuficientemente específica. Añadir evidencia directa de cifrado, integridad y retención, además del recurso físico. |
| RT-16.18, conservación tras vencer certificado | 4.1.17 y 4-U; T-12 menciona XML, acuse, hash, marca temporal y cadena de verificación. | El respaldo documental está descrito; la simple marca temporal de un registro no demuestra por sí sola el sello exigido. Cotejar protocolo/autoridad temporal y prueba de verificación posterior antes de cerrar. |

### Preservación y reproducibilidad

Las huellas siguientes identifican los archivos leídos para este corte. Si otra tarea modifica sus fuentes, recalcular los conteos y destinos antes de cerrar un pendiente.

| Fuente leída | SHA-256 |
| --- | --- |
| T-12 | `569d66f0745a264e61a3453df7c4f814cd6144d007ab924b20967db9890cc21c` |
| SD4 | `0198286485d3fbc4737cd31f9b139904f0a80f4ddb2c5f278ee148bb44ffc3cb` |
| SD4-Anexos | `255a3f999aa4fc4dde5f0a452ff6cd60f41f72d16ef6a44323ac853e222d898a` |
| T-11 | `0b5e92d68c7f00ee8e654ae21386820d57538bf25c75bf24d25fd5b3f4ba83c0` |

Filas distintas con referencias desactualizadas: RF-13.03, RF-14.01-BTT, RF-14.02-BTT, RF-14.03-BTT, RF-14.04-BTT, RF-15.03, RF-17.11, RF-17.13, RF-18.01, RF-19.01, RF-19.02, RF-19.03, RF-19.04, RNF-14.03, RNF-14.04, RNF-14.05, RNF-14.07, RNF-14.09, RNF-14.10, RNF-15.03, RNF-16.01, RNF-16.03, RNF-20.01, RNF-20.02, RNF-20.06, RNF-21.09, RT-02.04, RT-02.12, RT-03.04, RT-05.10, RT-05.16, RT-06.02, RT-06.03, RT-06.05, RT-06.11, RT-06.13, RT-06.22, RT-06.30, RT-07.02, RT-07.03, RT-07.04, RT-07.05, RT-08.01, RT-08.03, RT-08.05, RT-08.07, RT-09.01, RT-09.02, RT-09.03, RT-09.04, RT-09.05, RT-09.06, RT-09.07, RT-09.08, RT-10.01, RT-10.02, RT-10.05, RT-11.03, RT-11.05, RT-11.13, RT-11.16, RT-11.17, RT-11.18, RT-11.25, RT-11.27, RT-12.09, RT-13.10, RT-14.03, RT-14.07, RT-16.18, RT-16.27, RT-17.03, RT-17.04, RT-17.05, RT-17.08.

No se ejecutaron ensayos, compilación ni revisión visual nueva del PDF. El estado semántico completo de las 499 filas sigue pendiente; este registro permite priorizar y revisar las correcciones externas de T-12.
