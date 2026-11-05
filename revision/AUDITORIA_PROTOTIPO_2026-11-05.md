# Auditoría del prototipo contra Bases, Caso 02, SD3 y SD4

Fecha: 05-11-2026. Rama `LafroX-Prototipo-HTML`, commit local `5b727c25`.

## Método

- Se leyó el código de las 51 rutas (`js/app.js`, `js/data.js` y las 12 vistas de `js/views/`) y se contrastó cada requerimiento de `checklist_bases.md` y `checklist_sd3_sd4.md` con lo que la pantalla hace de verdad, no con la etiqueta `rf:` que declara.
- Se hizo un barrido en el navegador de 49 rutas con el perfil de evaluación, en local: **0 errores de JavaScript, 0 pantallas con error y 0 enlaces internos rotos**.
- Se revisó el sitio publicado en GitHub Pages.
- Escala: **Cumple** · **Parcial** (la pantalla existe, pero falta una parte del criterio «Verificar») · **No cumple** (no hay pantalla ni simulación) · **Límite** (exige servidor, dispositivo o personas reales; Bases Técnicas 25.6).

## 1. Hallazgos críticos (corregir antes del 13-11-2026)

| # | Hallazgo | Evidencia | Impacto |
|---|---|---|---|
| C1 | **El commit `5b727c25` no está publicado.** La rama local va 1 commit adelante de `origin`. El sitio en línea no tiene: `/admin/flujos` (RF-17.06), el pago con Transbank (RF-12.30), las alertas de vida útil FEFO (RF-02.09), la merma que descuenta stock (RF-08.05), editar y eliminar geocercas (RF-14.06), la búsqueda global tolerante a errores (RF-17.11) ni la vista previa de documentos (RF-17.08). | `git status`: `ahead 1`. El sitio publicado tiene 50 rutas y la copia local 51. `clients.js` tiene 267 líneas en línea y 291 en local. | La comisión evalúa el enlace (RT-25.06), no la copia local. Varias casillas «✓ corregido» de los checklists **no son verdad en línea**. |
| C2 | **El primer ingreso al sitio publicado falló**: error `L.session is not a function` repetido cada segundo (`features.js:28`) y la aplicación no arrancó. Al recargar funcionó. | Consola del navegador, primera carga. `index.html` carga los scripts sin versión (`?v=`). | Lo más probable es que el navegador haya mezclado archivos en caché de dos versiones tras una publicación. Si le pasa a un evaluador, verá una pantalla en blanco (penalización del Cap. 25.6: pantallas no navegables). |
| C3 | **Los permisos solo filtran el menú, no las acciones.** No existe ningún control por acción. | No hay `L.can` ni comprobaciones del perfil dentro de las vistas. | Infringe SD4 4.1: «un actor relacionado con un módulo no ve todas sus funciones». Ejemplos: la Preventista puede «Bloquear por crédito», ver la cartera vencida y la segmentación en `/clientes`, y en `/pedidos` puede anular y «Asignar a ruta». El Conductor entra a `/devoluciones` y puede aprobar destinos (función de la Jefa de Bodega, RF-08.02). El Preparador registra recepciones sin «autorización funcional». RF-15.04 queda **Parcial**. |
| C4 | **El cliente del canal moderno ve los datos del cliente tradicional.** | `/portal/cuenta` y `/portal/pedido` usan valores fijos: `CL-10021`, «Acuerdo de cuenta · Almacén Doña Rosa» y un crédito de $612.000. | Es una incoherencia visible al cambiar de perfil (Cap. 25.6: inconsistencias evidentes). |
| C5 | **Faltan funciones del portal de clientes que exige el caso.** No hay descarga de la cartola PDF/Excel con detalle de facturas (RF-07.07). No hay listado ni descarga de factura, guía y nota de crédito (RF-12.17). No hay consulta de la historia de temperatura del envío (RF-09.04; Caso, criterio 3: «disponible para el cliente»). | `/portal/cuenta` solo muestra 3 indicadores y un gráfico. Los documentos están en `/clientes/:id`, que el cliente no puede abrir. | Tres RF de etapa 2 y un criterio de aceptación del caso: **No cumple**. |
| C6 | **Criterio 16 del caso (jubilación de Don Hugo) sin pantalla.** El Planificador «registra restricciones» (SD3, actores), pero no existe dónde registrar restricciones o conocimiento de ruta por cliente o zona. | No hay coincidencias de «restricción», «conocimiento» ni «jubil» en `js/`. | El caso dice que el criterio 16 «no es una nota de color». Es el punto más visible frente a la comisión. |

### Estado de las correcciones (05-11-2026)

- **C1 y C2 corregidos**: se publicó el commit `5b727c25` y los scripts y estilos llevan versión (`?v=`).
- **C3 corregido**: `L.can(acción)` en `js/app.js` define, con la matriz `PERM`, quién ejecuta cada acción. Se aplica en clientes, pedidos, rutas, preparación, rendición, recepción, inventario, devoluciones, calidad, telemetría, canal moderno y acciones rápidas. Los perfiles sin la acción ven solo consulta. La Preventista y el Preparador ahora tienen `/flujo`, porque sus pantallas enlazan a él. Se verificaron 154 pantallas en los 16 perfiles, sin errores.
- **C4 y C5 corregidos**: `L.portalCliente()` asocia cada perfil de cliente a su propia ficha, y `L.portalCuenta()` calcula el saldo, lo vencido, el crédito y las facturas desde ella. Con esto:
  - El estado de cuenta tiene una cartola con facturas pendientes por tramo, descargable en PDF (vista para imprimir) y en Excel (CSV) (RF-07.07).
  - Una pestaña de documentos tributarios descarga facturas, guías y notas de crédito en XML y PDF (RF-12.17).
  - «Mis entregas» muestra los pedidos reales del cliente, con POD y la temperatura del envío refrigerado, descargable (RF-09.04).
  - Al pedir en el portal se valida el stock disponible (RF-12.15).
  - Para que el cliente tradicional tenga algo que mostrar, se agregaron 3 entregas pasadas de Almacén Doña Rosa, marcadas `hist`, que no aparecen en la ruta de hoy.
- **C6 corregido**: nueva pantalla `/rutas/restricciones`, «Restricciones de ruta» en el menú de Operación, para el Planificador y el Gerente de Operaciones.
  - Registra las reglas que hoy se aplican de memoria (accesos, horarios, clientes, zonas, secuencias y vehículos), con su motivo, su fuente (por ejemplo, «Entrevista a Hugo Maldonado») y cuántas veces se aplicaron.
  - Las nuevas quedan «Por validar» hasta que las confirme un segundo perfil, distinto de quien las registró.
  - El plan de rutas declara cuántas restricciones vigentes aplicó.
  - Responde al criterio 16 del caso.
- **Los seis hallazgos críticos están corregidos.** Siguen pendientes los parciales de las secciones 4 a 6.

## 2. Bases Técnicas y Administrativas (Cap. 25, Cap. 13, Art. 26°)

Lo marcado como cumplido en `checklist_bases.md` se confirma, con estas salvedades:

| Exigencia | Estado | Observación |
|---|---|---|
| RT-25.06 Enlace en línea | **Parcial** | Responde, pero publica una versión desactualizada (C1) y falló al primer arranque (C2). |
| RT-25.06 / RT-13.10 Navegadores | **Parcial** | Solo se probó en Chromium. Faltan Firefox y Safari. |
| RT-25.07 Seis meses | Límite | Se acredita con la publicación estable. |
| RT-25.10 Exportación sin conexión (deseable) | **Parcial** | El README dice «abra `index.html` directamente», pero nunca se probó con `file://`. Las fuentes de Google no cargan sin conexión. No hay archivo exportado. |
| 2.7 Filtro por período | **Parcial** | Los botones de 3, 6 y 12 meses funcionan, pero los campos «Desde» y «Hasta» de `/analitica` solo validan el rango y no filtran nada. |
| RT-25.03 / RT-13.01 Informe WCAG | Pendiente (otro entregable) | Sin informe de conformidad ni prueba con lector de pantalla. |
| RT-13.08 Guantes e intemperie | Límite | Botones de 60 px. Se acredita en terreno. |
| 2.2 Recuperación de acceso | Cumple | Usa código de 6 dígitos con vigencia de 15 minutos. RF-12.27 pide «enlace»; la diferencia es menor. |
| Resto del Cap. 25.2, 25.4, 25.8 y 25.9 | Cumple | Confirmado en el código y en el barrido. Hay 9 tipos de gráfico (exigidos: 6). |

## 3. Actores y capa de presentación (SD3 3.A.12a; SD4 Capa 1)

| Punto | Estado | Observación |
|---|---|---|
| Los 15 actores tienen perfil y menú propio | Cumple | 15 perfiles más el de evaluación. Ningún interesado sin cuenta aparece como perfil. |
| Permisos acotados por rol dentro de los módulos | **No cumple** | Ver C3. |
| El peoneta no comparte la sesión del conductor | **No cumple** | No hay ninguna mención ni pantalla. |
| Jefe de TI: «interfaces, observabilidad» | **Parcial** | Solo tiene administración. No hay pantalla de estado de interfaces (ERP, EDI, telemetría) ni de observabilidad (RF-16.01). |
| Búsqueda global (RF-17.11) | **Parcial** | Tolera errores y filtra por tipo, pero solo las pantallas respetan el perfil. Clientes, pedidos, rutas y lotes aparecen para cualquier perfil. |
| Preferencias (RT-13.12) | Cumple | El aviso «se aplican en todos sus dispositivos» contradice SD4 («conservadas en el dispositivo») y el almacenamiento local. |
| RF-12.25: «RUT no habilitado → contactar al ejecutivo comercial» | **No cumple** | El registro en 5 pasos acepta cualquier RUT válido. |
| Canal tradicional: activación asistida por SMS opcional y compra asistida sin cuenta | **No cumple** | No se muestra. |

## 4. Funciones sin conexión (SD4, Anexo 4-J)

| Función | Estado |
|---|---|
| Pedido de preventa, entrega y POD, cobro en efectivo, POS no disponible, mapas precargados | Cumple (simulado) |
| Recepción y preparación con el CD sin enlace | Cumple (`cdBanner`) |
| Pedido de autoatención en cola con UUID | **No cumple**: el portal no tiene modo sin conexión. |
| Nueva guía electrónica sin conexión (Talca o guía preemitida) | **No cumple**: no se muestra. |
| EDI sin conexión, tablero central con alarmas locales | **No cumple**: no se muestra. |
| Cadena de frío del camión y curva por Iridium | **Parcial**: la lista de camiones dice «Iridium ✓», pero no se simula la pérdida de móvil. La pestaña «Frío» del conductor siempre muestra «Normal». |
| Liberación sanitaria local | **No cumple**: no se muestra. |

## 5. Módulos funcionales: lo que no cumple el criterio «Verificar»

Solo se listan los parciales y los incumplimientos. El resto de los RF del checklist **cumple** como simulación creíble.

### M1 Recepción
- **RF-01.04 Parcial**: la foto de la no conformidad no es obligatoria.
- **RF-01.05 Parcial**: al confirmar no pasa nada visible. No aparece la cuarentena ni el aviso a Calidad; solo hay un texto de ayuda.
- **RF-01.06 Parcial**: no existe el caso «Producto no encontrado». Cualquier GTIN se resuelve al mismo producto.
- **RF-01.10 Parcial**: a la ficha le faltan «clasificación sanitaria» y «RUT del proveedor». No se pueden crear fichas, solo editarlas. No se ve el historial de cambios de GTIN y SKU.

### M2 Inventario
- **RF-02.01 Parcial**: solo tiene zonas; faltan pasillos, racks, niveles y posiciones. El rango refrigerado es **0–8 °C** y SD3 dice **2–8 °C** (incoherencia).
- **RF-02.02 Parcial**: falta el desglose del stock por instalación y por zona para cada SKU.
- **RF-02.03 Parcial**: solo se aprueba todo junto; no se puede aprobar, rechazar o modificar cada movimiento.
- **RF-02.04 Parcial**: no hay pantalla de conteo ciego ni flujo de umbral → «Pendiente de autorización».
- **RF-02.06 Parcial**: falta la hora estimada de llegada y la confirmación tránsito → físico.
- **RF-02.07 Parcial**: falta el histórico de 12 meses y la exportación.
- **RF-02.10 Parcial**: falta la ubicación por pasillo y posición, las salidas con guía y cantidad, las excepciones del lote y la exportación de su ficha.

### M3 Preventa
- **RF-03.03 Parcial**: no se muestra el quiebre parcial entre dos preventistas; el flujo siempre dice «4 de 4 líneas reservadas».
- **RF-03.08 Defecto**: en `/flujo` la alerta salta al superar el **40 %** del límite (`credito * 0.4`), no el 100 % que pide el RF. En `/terreno/preventa` está bien.
- **RF-03.14 Parcial**: las sugerencias son fijas y no hay «criterios configurados por comercial».
- **RF-03.16 Parcial**: no se ve un reenvío duplicado descartado ni que quede auditado.
- Trazabilidad mal citada: la cola de la preventa cita RF-03.13; debería citar RF-03.15 y RNG-12.

### M4 Rutas
- **RF-04.03 Parcial**: no se puede intentar agregar una línea que exceda el peso o el volumen para ver el bloqueo; solo hay un texto.
- **RF-04.05 Parcial**: el bloqueo de carga de frío en un camión seco solo existe en el portal de transportistas, no en la consola del planificador.

### M5 Preparación
- **RF-05.01 Parcial**: falta la generación automática al cierre de turno y la agrupación por pedido o por ruta.
- **RF-05.02 No cumple**: no existe el ingreso manual de contingencia registrado como «Ingreso Manual».
- **RF-05.04 No cumple**: se pueden escanear las líneas de frío antes de terminar las de seco; no hay bloqueo.
- **RF-05.05 Parcial**: falta el mensaje «Lote X con vencimiento anterior disponible en [ubicación]» y la excepción FEFO con motivo.
- **RF-05.07 Parcial**: se usan casillas en vez de escanear el SSCC. No hay alerta por bulto fuera de secuencia ni aviso a la Jefa de Bodega si falta un bulto.

### M6 Reparto
- **RF-06.01 Parcial**: no hay marcado masivo por guía.
- **RF-06.06 Parcial**: no se registra la hora de llegada ni la de término. Analítica muestra solo la llegada.
- **RF-06.07 Parcial**: al sincronizar no se genera el reporte de cierre o rendición.
- **RF-06.09 Parcial**: en la entrega solo se registran canastillos; faltan los pallets, el tipo y el estado.

### M7 Cobranza
- Cumple en lo simulable.

### M8 Devoluciones
- **RF-08.02 Parcial**: el destino lo decide cualquier perfil con acceso (C3).

### M9 Calidad
- **RF-09.01 Defecto de datos**: los clientes afectados son siempre los primeros 12 del maestro, no los que recibieron el lote. Falta la columna de guía. El título dice «N clientes» y la tabla muestra otra cantidad.
- **RF-09.03 Parcial**: no hay exportación del registro para la autoridad sanitaria.
- **RF-09.05 y RF-09.06 Parcial**: no hay alerta en cabina ni registro de observaciones del conductor.
- **Incoherencia de la regla térmica**: RF-09.05 dice «desviación de 2 °C por 15 min». La alerta de telemetría usa un valor absoluto de 8 °C por 20 min. La tabla de parámetros por familia dice 2 °C por 20 min en lácteos.
- **RF-09.09 Parcial**: el expediente de evidencia de frío no se descarga; solo aparece un aviso.
- **RF-09.12 y RF-09.13 Parcial**: no se simula un latido vencido que bloquee la bajada del SSCC.
- **RF-09.14 Parcial**: en `/calidad` falta «uso no alimentario» (en `/telemetria` sí está) y no hay marca del área de no aptos.

### M10 Analítica
- **RF-11.03 Parcial**: falta el OTIF por zona.
- **RF-11.05 Parcial**: no hay bitácora de viajes subutilizados en la ventana 05:30–07:00.

### M11 Canal moderno
- **RF-12.08 Parcial**: no hay historial de estados del pedido EDI con ASN y POD.
- **RF-12.09 Parcial**: el ASN es solo un aviso, sin su contenido.
- **RF-12.15 Parcial**: el portal no valida stock y el crédito está fijo.
- **RF-12.21 Incoherente con SD3**: SD3 dice que una ruta sin confirmar «mantiene la asignación planificada como supuesto no verificado»; el prototipo dice que «vuelven a despacho para reasignación».

### M12 Telemetría
- **RF-14.01 Parcial**: el mapa muestra 12 rutas, no los 42 camiones propios.

### Transversales
- **RF-15.03 Parcial**: el segundo factor ofrece solo app y SMS; faltan FIDO2 y claves de acceso.
- **RF-15.05 Parcial**: no hay vínculo con el ciclo laboral (baja automática ≤ 24 h).
- **RF-17.01 Parcial**: faltan las unidades organizacionales y sus jerarquías.
- **RF-17.04 Parcial**: la auditoría no muestra valores anteriores y posteriores. Las acciones hechas en el prototipo (bloquear, anular, aprobar) **no generan registros**; solo se guardan las consultas. Los avisos dicen «queda en la auditoría».
- **RF-17.06 Parcial**: falta la delegación por ausencia (y en línea la pantalla no existe, C1).
- **RF-18.02 Parcial**: no se configura la frecuencia y no hay canales obligatorios bloqueados.

## 6. Reglas de negocio (RNG)

- **Cumplen**: RNG-01, 02, 03, 05, 06, 07, 08, 09, 11, 12, 14, 15, 16 y 17.
- **RNG-10 Parcial**: no se muestra que, a igual vencimiento, se prioriza la recepción más antigua.
- **RNG-13 No cumple**: es la secuencia térmica obligatoria (ver RF-05.04).
- **RNG-04 Parcial**: falta la suspensión durante la puerta abierta y el regreso al CD si nadie decide.

## 7. Errores de los checklists existentes

- `checklist_bases.md` marca RT-25.06 como cumplido, pero el sitio en línea no tiene el último commit (C1).
- `checklist_sd3_sd4.md`, sección 10, dice «todo lo corregible quedó corregido y verificado». Eso fue en local; en línea falta parte (C1).
- Casi todas las casillas de RF de `checklist_sd3_sd4.md` siguen sin marcar (`[ ]`). Esta auditoría sirve para marcarlas, salvo las de las secciones 5 y 6.

## 8. Prioridad sugerida

1. **Publicar** `5b727c25` y versionar los scripts (`?v=` en `index.html`). Resuelve C1 y C2.
2. **Corregir permisos por acción** en `/clientes`, `/pedidos` y `/devoluciones` (C3).
3. **Agregar al portal de clientes** los documentos tributarios, la cartola descargable y la temperatura del envío, y usar los datos del cliente con sesión (C4, C5).
4. **Agregar una pantalla de restricciones de ruta** para el Planificador (C6, criterio 16).
5. **Bloqueos de M5**: secuencia térmica, ingreso manual auditado y SSCC fuera de secuencia (RF-05.02, 05.04, 05.07).
6. **Coherencia de datos**: umbral del 40 % en `/flujo`, clientes afectados en el retiro sanitario, rango 2–8 °C, regla térmica y RF-12.21.
7. **El resto de los parciales** de la sección 5, según el tiempo disponible.
