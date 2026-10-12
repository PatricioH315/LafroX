# LafroX — Trazabilidad de la revisión del Informe 1 al Subdocumento 4

Fecha de contraste: 11 de octubre de 2026. Fuente de observaciones: `G02-C02-LOGISTICA-LAFROX-Revision Informe 1.pdf`, páginas 9–14, exclusivamente apartados 4.1 y 4.2. Las aclaraciones posteriores gobiernan la estructura consolidada 4.1–4.3. Este registro de trabajo no se incorpora al texto de la oferta.

## Actualización del estado — 11 de octubre de 2026

Esta actualización revisa el registro a partir de las observaciones identificadas en la conversación, las fuentes locales de SD4 y los registros posteriores [de alineación](ALINEACION_MD_LATEX_2026-10-11.md) y [de auditoría de tablas](AUDITORIA_TABLAS_SD4.md). Conserva las 46 observaciones originales y no ejecuta una nueva auditoría requisito por requisito ni pruebas técnicas. La rama comprobada es `subdoc-4`; se preservan sus modificaciones locales existentes. En esta actualización solo se edita este registro Markdown, sin commit, push, modificación de entregables ni cambios al T-12.

Los conteos, compilaciones y comprobaciones de las ejecuciones anteriores se identifican como antecedentes; no se presentan como controles ejecutados nuevamente. Los pendientes cuentan con condición de cierre en la matriz de seguimiento situada después de la tabla principal. La continuación del cotejo se registra en [COTEJO_TRAZABILIDAD_CONTRACTUAL_SD4.md](COTEJO_TRAZABILIDAD_CONTRACTUAL_SD4.md): se comprueban las referencias estructurales de las 499 filas que citan SD4 y se inicia el cotejo semántico dirigido, sin declarar terminado el análisis individual de todas ellas.

## Versiones y preservación de la ejecución original

- `rama-md`: actualizado desde `baf991d` a `cf43057` mediante fetch y pull fast-forward; mejoras locales de los tres archivos SD4 reaplicadas sin conflictos. Respaldo recuperable: stash `respaldo SD4 antes de pull plan concision 2026-10-11`.
- `subdoc-4`: actualizado de `ca84689` a `292c6e8` mediante fetch y pull fast-forward. Se preserva la carpeta local no versionada `05/`.
- En Markdown se modifican únicamente cuerpo SD4, anexos SD4 y T-11. En LaTeX se sincronizan sus fragmentos y se preparan las propuestas y herramientas de este subdocumento. Sin commit ni push en esta ejecución.

## Cómo leer los estados

«Documentado» significa que existe una respuesta concreta en el diseño; no acredita ejecución, revisión humana ni aprobación contractual. «Parcial» identifica una brecha vigente. «Verificación final» requiere inspección del entregable o medición. «Corregido documentalmente» limita el cierre al contenido o estructura descritos. Las observaciones positivas se conservan sin crear una corrección artificial. La numeración actual no reproduce la del informe preliminar; se actualizan las referencias afectadas por la incorporación de la red y la reorganización de tablas.

| ID | Observación y página del evaluador | Evidencia actual | Estado / cierre necesario |
| --- | --- | --- | --- |
| EL-01 | Texto y diagramas desconectados, pp. 9–10 | 4.1.3: figuras 1–12 precedidas de cita y seguidas de explicación | Documentado; comprobar legibilidad final |
| EL-02 | Trece recorridos por actor redundantes y sin explicación, p. 9 | General, ocho vistas preparadas por capa, secuencias y matriz de actores 4-N | Sustitución documentada; cotejar permiso local de Calidad en figuras |
| EL-03 | Actores declarados distintos de los dibujados, p. 9 | Quince actores en 4-N; perfiles y ámbitos en 4.1.3.1/4.1.18 | Cotejo gráfico final pendiente |
| EL-04 | Matriz requisito → módulo → capa ausente, p. 9 | T-12 individual; 4-E familias; 4-N módulos y 37 componentes, Tabla A.14; distribución en Tabla 6 y recursos en T-11 | Cadena documentada; cotejo individual de suficiencia en curso (P-01) y referencias externas desactualizadas en 75 filas (P-02) |
| EL-05 | Cinco ambientes solo nombrados, p. 9 | 4.1.9, 4.2.4.1 y figuras 19–23; topología AWS en Figura 18 | Documentado por ambiente |
| EL-06 | SOLID y patrones sin aplicación, pp. 9–10 | 4.1.10.1: contratos de negocio y límites; patrones en 4.1.10 | Documentado; pruebas de dependencia/contrato por ejecutar |
| EL-07 | Seis vistas declaradas sin vista de procesos, p. 10 | 4.1.14 y 4-S: cinco vistas exigidas; procesos en figuras 8–9 | Corregido documentalmente |
| EL-08 | Estilo modular pertinente al caso, p. 10 | ADR-01, 4.1.13, Laravel/PHP con límites de módulos | Observación positiva conservada; framework actualizado |
| EL-09 | Comparación insuficiente y ADR fuera de lógica, p. 10 | Tabla 4, «Alternativas lógicas y criterio de selección»; registro único de 22 ADR en 4-O | Documentado, sin repetir fichas en cuerpo |
| EL-10 | Doce módulos anunciados sin inventario, p. 10 | 4-D: nombre, responsabilidad, contratos, actor y etapa | Documentado |
| EL-11 | Límites, interfaces, orquestación y coreografía ausentes, p. 10 | 4.1.3.5; 4-F/G/H; figuras 8–9 | Documentado |
| EL-12 | Marco TOGAF solo citado, p. 10 | ISO 42010 aplicado en 4-S con interesados, preocupaciones y correspondencias | Se usa el marco desarrollado; no se afirma aplicación de TOGAF por su sola mención |
| EL-13 | Modelo de dominio solo como lista, p. 10 | Figura 13, 4.1.5; productores y eventos en 4-A | Documentado; esquema relacional pertenece a SD5 |
| EL-14 | Caché de 8 h incompatible con 24 h y relevos, p. 10 | Caché 24 h; manifiesto 26 h; credenciales personales y verificador local; AL-OFF-01 incluye relevos a las 8 y 16 h | Diseño documentado; probar vigencias, permisos, reinicio y reconciliación; una copia vigente no renueva credenciales ni autoriza terceros (P-05) |
| EL-15 | Gateway solo remoto para HHT, p. 10 | API local A-01 en VM-01/VM-C01/E-01 y figura 5 | Documentado; no depende de API Gateway durante corte |
| EL-16 | Bloqueo térmico decidido por conductor frente a automático, p. 10 | M9 bloquea excursión crítica/sostenida; solo Calidad dispone con evidencia | Bloqueo documentado; cotejar etiquetas gráficas y recorrido local autorizado de Calidad antes de cerrar la autonomía de disposición (P-03/P-06) |
| EL-17 | Etapas discordantes con SD3, p. 10 | 4-D etapas, 4.1.8 implantación y referencia al calendario | Contrastar contra SD3 vigente sin editarlo |
| EL-18 | Portales externos tratados como intranet/VPN, p. 10 | Entradas pública, privada y local en 4.1.3/4.2.5.2 | Documentado; Verified Access reservado a oficina/consolas |
| EL-19 | Portada promete física pero solo incluye lógica, p. 10 | Cuerpo consolidado 4.1–4.3 y main integrado | Corregido en estructura |
| EL-20 | Códigos y versiones sin documento entregado, p. 10 | Catálogo físico A/B/C/D/E/F/N, inventario 4-N y contratos 4-G/H | Verificar etiquetas residuales en imágenes; no mezclar códigos históricos |
| EL-21 | Plantilla distinta e ilegibilidad, p. 10 | Plantilla común; vistas por capa; auditoría de tablas: 26 tablas técnicas breves y declaración de IA en cuerpo; tres activos de red actuales | Formato documentado; el registro histórico de rótulos próximos a 5 puntos no describe por sí solo los nuevos activos de red. Revisar su impresión final (P-04) |
| EF-01 | Documento duplicado y sin portada, p. 11 | Main único, anexos y T-11 independientes | Estructura corregida |
| EF-02 | Comentarios de IA, versiones y auditorías dentro de la oferta, p. 11 | Barrido previo de texto; notas de trabajo en este registro; declaración obligatoria conserva sus celdas pendientes | Revisión humana real pendiente (P-11); comprobar ausencia de notas de proceso en la revisión final, sin retirar la declaración obligatoria |
| EF-03 | Tabla de emplazamiento inexistente/incompleta, p. 11 | 4.2.2, Tabla 6; correspondencia en 4-N/A.14; inventario en 4-W/A.35 y T-11 | Doce módulos y 37 transversales inventariados; cotejo individual necesario para confirmar realización física y cobertura de requisitos (P-01) |
| EF-04 | Figura física ilegible y sin explicación, p. 11 | Figura 14 y vistas de sitios, emplazamiento, nube y recuperación 15–18/23; red en figuras 24–26 | Explicación presente; cotejar correspondencia con recuperación y legibilidad actual (P-03/P-04/P-07) |
| EF-05 | Descripciones verbales sustituyen dibujos, pp. 12–13 | Diagramas de ambientes, nube, sitios, racks y recinto; tres vistas de red incorporadas como figuras 24–26 en 4.2.4.2 | Incorporación documental corregida; queda revisión de correspondencia gráfica y legibilidad (P-03/P-04). El borrador de propuestas no es el activo entregado |
| EF-06 | BI ocupa catorce páginas ajenas al ítem, p. 12 | M10: función lógica y emplazamiento; modelo detallado remitido a SD5 | Mantener solo justificación y dependencias arquitectónicas |
| EF-07 | Implementos pertinentes, p. 12 | T-11 con modelos, cantidades y finalidad | Observación positiva conservada |
| EF-08 | Cantidades sin número y ciclo de vida/caídas omitidos, p. 12 | 4.2.1.2, 4-W.3, T-11, actualizaciones 4-P | Comprobar especificación de aceptación por tipo; cálculos no equivalen a ensayo |
| EF-09 | Exceso de equipos congelados/POS/impresoras, p. 12 | Dotación por turno, parque y reservas en 4-W/T-11; 207 terminales al inicio y 235 en año 3, incluidos repuestos | Cifras derivadas; 186 es concurrencia nocturna inicial. Precisar el perfil temporal de la campaña de Preproducción que menciona 207 (P-09) |
| EF-10 | Frío solo en 18 camiones y alertas al regreso, p. 12 | 28 termógrafos, 18 propios + 10 externos; BLE y alerta local en ruta | Corregido en diseño; ensayo de lectura/alerta por ejecutar |
| EF-11 | Estudio de cobertura inalámbrica insuficiente, p. 12 | 4.2.1.2 y aceptación de interfaces/cámaras | Estudio y medición necesarios; no inventar cobertura medida |
| EF-12 | Sala secundaria sobredimensionada y Tier incoherente, p. 12 | 4.3.1.4 dimensiona equipamiento real; disponibilidad por componente separada de E2E | Documentado; ninguna categoría Tier sustituye demostrar disponibilidad |
| EF-13 | Sin cálculo eléctrico/térmico, plano ni racks, p. 12 | Tablas 23–24, carga eléctrica y térmica; figuras 28 (racks) y 29 (recinto); memoria 4-W.8 | Evidencias presentes; verificar correspondencia gráfica final (P-03) y actualizar referencias externas del T-12 (P-02) |
| EF-14 | Gabinetes de borde sin energía/clima/acceso, p. 12 | Figuras 15–16, 4.2.1.2, Tabla A.39 de carga/UPS y T-11 | Documentado por tipología |
| EF-15 | Aprobación de DR podría llevar RTO a 24–72 h, p. 12 | 4.3.2 declara regiones y RTO ≤ 4 h; aprobación de residencia como hito; consulta sanitaria regional de solo lectura con presupuesto de 75 min | Diseño documentado; medir restitución por servicio, conectividad de Talca y consulta sanitaria (P-07); residencia y brecha extrema de RPO requieren decisión contractual real (P-08) |
| EF-16 | T-11 invocado pero no adjunto, p. 12 | Archivo propio MD y PDF independiente | Presente; verificación de compilación registrada abajo |
| EF-17 | Zero Trust y SPOF pertinentes, p. 12 | 4.1.3.7, 4-Q/R; 4.2.5; respaldo 3-2-1-1-0 | Contenido conservado; remitir a sección principal sin repetir controles |
| EF-18 | Funciones offline y limitaciones omitidas, p. 13 | 4.1.15–16, 4-J/K/M; captura local, relevos, guía preemitida y autorizaciones externas condicionadas | Funciones y límites documentados; probar continuidad completa, no solo captura; completar cotejo del acceso local de Calidad (P-05/P-06) |
| EF-19 | Ceph sobre RAID y capacidad contradictoria, p. 13 | Seis OSD sin RAID, size=3/min_size=2, N+1 y cálculo de 4-W.8 | Diseño documentado; fallo y reconstrucción por probar |
| EF-20 | DTE diferido contradice único emisor/guía previa, p. 13 | Preemisión ERP, invalidación por cambio, AL-DTE-01 y 4-U | Documentado; 96 salidas requieren prueba completa y documentos válidos |
| EF-21 | Dotación incompatible con cuatro TI, p. 13 | Dotación propia de NOC/SOC y mesa en 4.2.6/4-W.7 | Dimensionamiento presente; los cuatro TI del cliente no operan solos toda la plataforma |
| EF-22 | Sin red, despliegue ni zonas de seguridad, p. 13 | Cinco ambientes y topología AWS; figuras 24–26 de red en 4.2.4.2 y Tabla 9, «Direccionamiento y segmentación» | Red y segmentación incorporadas documentalmente; pendientes legibilidad y cotejo de rutas, zonas y recursos de recuperación (P-03/P-04/P-07) |
| EF-23 | TPS sin sustento y regímenes mezclados, p. 13 | 4.2.6.2–3 y 4-W separan normal, ventana y septiembre | Cálculos documentados; prueba no ejecutada |
| EF-24 | Dieciséis dimensiones ausentes o sin derivación, pp. 13–14 | Síntesis trasladada a 4-W/Tabla A.30; derivaciones en la memoria y cuadros numéricos del cuerpo | Método documentado; cotejar suficiencia de cada dimensión y validar cotas por medición (P-01/P-09) |
| EF-25 | ADR con precios, p. 13 | ADR únicos en 4-O, decisiones cualitativas y técnicas | Mantener control de ausencia de precios en toda la oferta técnica |

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

La continuación recalculó 645 filas del T-12, incluidas las variantes con sufijo `-BTT`: 499 citan SD4 o sus anexos, y otras seis citan T-11 sin SD4. Se resolvieron 752 menciones explícitas a secciones del cuerpo en 83 encabezados distintos de sus 108 encabezados numerados. Este control no acredita que cada referencia sea suficiente para todo el requisito. Se encontraron 34 formas de cita numérica desactualizadas en 75 filas distintas. El Anexo 4-E agrupa familias y enlaza el T-12; 4-N/Tabla A.14, Tabla 6 y T-11 completan la realización física. El análisis semántico dirigido y el inventario de correcciones están en [el informe de cotejo](COTEJO_TRAZABILIDAD_CONTRACTUAL_SD4.md); la auditoría semántica completa permanece en curso (P-01). No se editó T-12 ni otro subdocumento.

## Red actual, activo anterior y borradores conservados

La fuente local actual incorpora tres activos en 4.2.4.2: [red general](../figuras/fisica/Red_01_general_legible.pdf), [red local](../figuras/fisica/Red_02_sitios_legible.pdf) y [conectividad regional](../figuras/fisica/Red_03_regiones_legible.pdf), como figuras 24, 25 y 26. Se acompañan de explicación y de la Tabla 9 de direccionamiento y segmentación. El cierre gráfico sigue condicionado a P-03/P-04; esta continuación no mide tipografía ni inspecciona nuevamente el PDF.

Se conserva el activo anterior [Red_general_sitios_regiones.pdf](../figuras/fisica/Red_general_sitios_regiones.pdf), con fuente [Red_general_sitios_regiones.drawio](../figuras/fuentes/fisica/Red_general_sitios_regiones.drawio). El registro de alineación identifica ese XML corregido por el usuario y su SHA-256 `912bf7b551a9bd005b9e8f00b39d265faa7ff34221b6934f33cf4ee33b841aac`. Esa huella y sus observaciones de impresión no se atribuyen automáticamente a los tres activos actuales.

Los archivos siguientes se conservan como borradores históricos, no como evidencia de la figura entregada:

Archivo editable: [Red_integral_SD4.drawio](../figuras/propuestas/Red_integral_SD4.drawio), dos páginas preparadas para explicación independiente. Preliminares: [sitios y regiones](../figuras/propuestas/Red_integral_SD4.png) y [segmentación](../figuras/propuestas/Segmentacion_SD4.png).

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
