# Brief de implementación: cadena de frío en ruta

**Para:** la IA que aplicará los cambios en los subdocumentos de LafroX. **Fecha:** 24‑10‑2026.
**Fuente técnica única:** `00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md` (versión 9.4) en la rama `subdoc-4`. Cada cifra, componente y regla sale de ahí; si algo no está en ese documento, no se inventa.

---

## 1. Reglas obligatorias

1. **Alcance:** solo **SD2, SD3, SD4, SD5, SD6 y SD7**. **No tocar** SD1, SD8 (está en reproceso), SD13, el Informe 3 ni los formularios económicos (E‑21 a E‑26).
2. **No modificar diagramas ni figuras** (`.drawio`, `.png`, `.pdf` de figuras ni figuras TikZ). Si un texto deja una figura desactualizada, anotarlo en la lista de pendientes (§9); no editar la figura.
3. **No crear entidades nuevas en el modelo de datos del SD5.** Solo agregar atributos y valores de catálogo a entidades que ya existen (§5).
4. **EDT del SD7:** los paquetes nuevos van **dentro de la fase y la cuenta que ya les corresponde**, con la numeración correlativa de esa cuenta. No renumerar paquetes existentes ni crear fases nuevas.
5. **No declarar** el riesgo de que un transportista rechace el kit.
6. **No incluir precios** en ningún subdocumento (Bases Administrativas, art. 50.2).
7. **Ficción:** el cliente es «Distribuidora Puelche S.A.» y el proponente «LafroX». Español formal, sin notas al redactor, sin «pendiente», «borrador» ni menciones a IA dentro del texto técnico.
8. **Formato:** respetar `lafrox.cls`, los entornos de tabla existentes (`tablalafrox`), las citas APA y las reglas de las Aclaraciones (tablas del cuerpo breves; detalle en anexos).
9. **Declaración de uso de IA:** actualizar la fila de cada sección o anexo modificado (Aclaraciones §7.2), sin atribuir revisiones humanas que no ocurrieron.
10. **Coherencia de cifras:** usar exactamente las de §3 de este brief en todos los subdocumentos.
11. Trabajar **rama por rama**; no hacer push sin aprobación del usuario.

---

## 2. Resumen de la solución (para entender lo que se escribe)

- Cada uno de los **28 camiones con frío** (18 propios y 10 de transportistas) lleva el **mismo kit, que LafroX provee, instala y mantiene**:
  - **gateway industrial** en la cabina con **AWS IoT Greengrass** (Moxa UC‑8200, misma plataforma que los gateways de cámara B‑02);
  - **3 sondas PT100** leídas por un módulo Moxa ioLogik E1260‑T: 1 de aire y 2 **simuladores de producto** en botellas de glicol;
  - **sensor independiente** Teltonika EYE SENSOR EN12830 en glicol;
  - **termógrafo** EYE SENSOR EN12830 en el aire, cada 1 minuto;
  - **módem satelital Iridium Edge**;
  - sensor de puerta, luz y zumbador, y una UPS.
- **Detectar, alarmar al conductor y bloquear la entrega ocurren en el camión, sin ninguna red:** sondas por cable, luz y zumbador cableados, TC58e por Wi‑Fi local y sensor por Bluetooth.
- **Red móvil (dos operadores) y satélite Iridium transmiten siempre, en paralelo.** No es internet satelital: son mensajes cortos.
  - **Red móvil:** curva cada 1 minuto.
  - **Satélite:** alarmas al instante, curva cada 3 minutos y órdenes de Calidad de bajada.
- **El TC58e es la segunda cadena:** evalúa la misma regla con el sensor independiente y retiene por contradicción.
- **Se mide por compartimento, en el punto más caliente que fija el mapeo térmico.** Cada SSCC hereda la curva de los minutos que estuvo a bordo, más su tiempo fuera de frío en el andén (escaneos de salida de cámara, carga y bajada).
- **Retención por SSCC según la regla de su familia**, nunca del camión completo. Si nadie decide, lo retenido vuelve al CD y decide Calidad (acción por defecto).
- **Ante una ruptura confirmada** (RSA arts. 102, 105 y 192): entrega parcial, ajuste tributario por el ERP, reposición, área de no aptos marcada con X roja y disposición de Calidad (liberar, vender con descuento si es apto, devolver al proveedor, uso no alimentario autorizado o destrucción autorizada).

---

## 3. Cifras únicas

| Dato | Valor |
|---|---|
| Camiones con frío | 28 (18 propios + 10 de transportistas) |
| Kits con reserva del 10 % | 31 de cada componente unitario; 93 sondas; 93 botellas; 62 SIM M2M |
| Termógrafos (B‑03) | 31 (sin cambio de cantidad); intervalo de 1 min; memoria ≈ 66 h |
| INT‑05 | 30.548 mensajes/día (antes 10.920): 6.048 de cámaras + 24.360 del gateway + 112 eventos + 28 descargas |
| Total de integraciones | 244.280 en régimen / 362.561 en peak (antes 224.652 / 342.933) |
| Total bruto de `calculo.py` | 249.880 / 372.961 (antes 230.252 / 353.333) |
| Lecturas de temperatura | 127.848/día |
| Temperatura en crudo | 6,77 GB/año; 33,83 GB en 5 años; 1,69 GB/año almacenado; DynamoDB 30 días: 0,556 GB |
| Mensajes satelitales | 290 por camión y día; 8.120 por día en la flota |
| Tiempos | Alarma ≤ 2 min por red móvil y ≤ 5 min por satélite; curva en los indicadores ≤ 5 min |

---

## 4. SD3 — Esquema de solución y alcance (rama `LafroX-Subdoc3-LateX`)

**Requerimientos: sí van al anexo donde están todos los requerimientos.** RF nuevos en el Anexo 3.A (`tablas_anexo/rf_propios.tex`) y RNF nuevos en el Anexo 3.B (`tablas_anexo/rnf_propios.tex`), con el mismo formato de columnas de cada tabla. Cada uno debe quedar también en el Formulario T‑12.

| # | Archivo:línea | Cambio |
|---|---|---|
| 1 | `tablas_anexo/rf_propios.tex` (después de RF‑09.10) | Agregar **RF‑09.11** Escaneo de salida de cámara y cálculo del tiempo fuera de frío por SSCC, con bloqueo del SSCC que supera el máximo de su familia. **RF‑09.12** Escaneo de bajada de cada SSCC de frío, que lo habilita para entregar solo con un estado vigente. **RF‑09.13** Retención por SSCC en el terminal ante crítica, contradicción o pérdida del enlace con el camión, sin depender de la red. **RF‑09.14** Disposición de Calidad del producto retenido (liberar, vender con descuento si es apto, devolver al proveedor, uso no alimentario autorizado o destrucción autorizada), con área de no aptos (RSA art. 105). Actor: Jefa de Calidad o tripulación, según corresponda; prioridad Crítica / E1; origen: propio LafroX |
| 2 | `tablas_anexo/rnf_propios.tex` (después de RNF‑09.05) | Agregar **RNF‑09.06** Alarma en ruta sin red: detección, alarma al conductor y bloqueo de la entrega sin red móvil ni satélite. Verificación: V6–V9. **RNF‑09.07** Doble camino siempre activo: aviso a Calidad ≤ 2 min por red móvil y ≤ 5 min por satélite en ≥ 95 %. Verificación: V2 y V18. **RNF‑09.08** Decisión térmica con simulador de producto en el punto más caliente del mapeo; registro certificado EN 12830 del aire cada 1 min. Verificación: V3 y V4. **RNF‑09.09** Coherencia de datos: sin pérdidas, sin duplicados, huecos detectados, crítica tardía siempre procesada. Verificación: V11 |
| 3 | `tablas_anexo/supuestos.tex:33` (S‑28) | Reescribir: las empresas transportistas aceptan que se instale el **kit de cadena de frío** (gateway, UPS, sondas, sensor independiente, termógrafo y módem satelital) en sus 10 camiones con frío, y el kit queda funcionando antes de que esas rutas partan con el nuevo proceso de reparto. **LafroX provee, instala y mantiene el kit**, igual que en los camiones propios. (Hoy dice que el CLIENTE compra el equipo: eso cambia) |
| 4 | `tablas_anexo/reglas_negocio.tex:9` (RNG‑04) | Agregar a RNG‑04: acción por defecto (si nadie decide en el plazo de la familia, lo retenido sigue retenido y vuelve al CD; nunca se libera solo); ventana de puerta (con la puerta abierta y hasta 10 min después, el aire no genera advertencias; la crítica nunca se suspende); retención por contradicción entre el gateway y el sensor independiente. Regla nueva **RNG‑17**: tiempo máximo fuera de frío por familia en el andén, que fija Calidad. Verificar antes que RNG‑17 esté libre; si no, usar el siguiente número libre |
| 5 | `tablas_anexo/criterios_aceptacion.tex:8` (R18‑03) | Método: conciliación de las tres series (gateway, sensor independiente y termógrafo) en el 100 % de los camiones con frío |
| 6 | `contenido.tex:11` (3.1.1) | Una frase: registro continuo, alerta y decisión en ruta también sin red móvil, y bloqueo de la entrega del producto afectado |
| 7 | `contenido.tex:152` (3.2.4) | Resumir la ampliación de RNG‑04 y la regla nueva |
| 8 | `contenido.tex:232` y `:249` (3.3.2) | Reemplazar «se vinculan al lote mediante su ubicación o viaje» por la historia térmica por SSCC: cámara → andén → compartimento, con los escaneos de salida de cámara, carga y bajada; se mide el punto más caliente de cada compartimento |
| 9 | `contenido.tex:278` (3.4.1) | Los dos escaneos nuevos y qué ve el conductor (verde, amarillo, rojo) |
| 10 | `contenido.tex:478` (3.4.5) | Plan ante falla del equipo de frío (aviso temprano, minutos restantes por familia, trasbordo o retorno) y protocolo ante ruptura confirmada (md §8.3 y §8.8), en un párrafo |
| 11 | `contenido.tex:522` (3.4.6) | Calidad aprueba las reglas por familia y la lista rotativa de llamada |
| 12 | `LAFROX-Formulario-T-12.tex:120–127, 236, 300–301, 406 y 604` | Columna de componente de RF‑09.03 a 09.10, RNF‑09.05, RNF‑23.01/02, RT‑05.29 y RT‑17.06: gateway del camión con Greengrass, Iridium Edge, sensor independiente y termógrafo EYE EN12830. **Agregar filas** para RF‑09.11 a 09.14 y RNF‑09.06 a 09.09, con paquete EDT del §7 de este brief y sección del SD4 |
| 13 | Anexos 3.A y 3.B (conteos en el texto) | Actualizar los totales de requerimientos si el texto los menciona (hoy 262: 176 RF y 86 RNF → 270: 180 RF y 90 RNF). Buscar «262», «176» y «86» en el SD3 y en los demás subdocumentos que los citen |

---

## 5. SD5 — Modelo y gestión de datos (rama `LafroX-Subdoc5-LateX`, carpeta `05_modelo_datos/`)

**Sin entidades nuevas ni cambios en figuras.** Todo cabe en entidades que ya existen.

| Concepto nuevo | Entidad existente que lo recibe | Cambio en el diccionario (Anexo 5‑A) |
|---|---|---|
| Tipos de sonda | `cal_sensor` (A_4) | Atributo o valores de catálogo `tipo`: SONDA_AIRE, SIMULADOR, SENSOR_INDEPENDIENTE, TERMOGRAFO_EN12830; atributo `compartimento` |
| Origen de la lectura | `tel_lectura_cruda` (A_9) | Catálogo `origen`: hoy CAMARA y TERMOGRAFO_VEHICULO; agregar SONDA_AIRE, SIMULADOR, SENSOR_INDEPENDIENTE. Atributos `secuencia`, `arranque` y `camino` (RED_MOVIL o SATELITE) |
| Historia térmica por SSCC | `cal_asociacion_ventana` (A_4) | Usarla para asociar el SSCC con su compartimento entre la carga y la bajada; atributo `compartimento` si falta |
| Retención por SSCC | `cal_bloqueo` (A_4) | Catálogo de motivos: CRITICA, CONTRADICCION, NO_CONFIABLE, EXPOSICION_ANDEN |
| Disposición de Calidad | `cal_resolucion_calidad` (A_4) | Catálogo: LIBERAR, VENTA_DESCUENTO, DEVOLVER_PROVEEDOR, USO_NO_ALIMENTARIO, DESTRUIR |
| Escaneos nuevos | `cal_evento_custodia` (A_4) | Tipos de evento: SALIDA_CAMARA y BAJADA_CAMION |
| Archivo de los registradores | `tel_archivo_termino` (A_9) | Indicar que incluye el termógrafo y el sensor independiente |
| Manifiesto del viaje | `obj_manifiesto` y `obj_manifiesto_linea` (A_9) | Atributo `compartimento` en la línea |

| Archivo:línea | Cambio de texto |
|---|---|
| `partes/5_1_modelo.tex:135` (5.1.7) | Un párrafo: historia térmica por SSCC con `cal_asociacion_ventana`, retención en `cal_bloqueo` y disposición en `cal_resolucion_calidad`, sin entidades nuevas |
| `partes/5_1_modelo.tex:223` (5.1.10) | «21 puntos × 288 y 28 termógrafos × 174 = 10.920 muestras/día» → 127.848 lecturas y 30.548 mensajes al día (cifras de §3) |
| `partes/5_2_gestion.tex:17` (5.2.2) | Secuencia y arranque por productor; procesamiento único; huecos; crítica tardía siempre procesada |
| `partes/5_2_gestion.tex:72` (5.2.7) | Temperatura 5 años; archivo original de los registradores en S3 con bloqueo; el registro de temperatura no guarda GPS |
| `partes/5_4_desempeno.tex:17` (5.4.2) y Anexo 5‑F (`anexos/contenido.tex:272`) | Índice de consulta por SSCC, compartimento e intervalo |
| Anexo 5‑C (`anexos/contenido.tex:185`) | Los catálogos de la tabla anterior |

---

## 6. SD6 — Metodologías (rama `LafroX-Subdoc6-LateX`)

| Archivo:línea | Cambio |
|---|---|
| `subdocumento_6/contenido.tex:35` (6.1.3 Gestión de adquisiciones) | Regla: ningún equipo se compra sin cotización de un proveedor con domicilio en Chile y certificación Subtel; el plazo de certificación entra al cronograma |
| `subdocumento_6/tablas/adquisiciones.tex:4` (Anexo 6.B) | **Dividir** la fila de equipamiento de terreno en dos. (a) «Equipos de uso: terminales de preventa, reparto y bodega, impresoras, terminales de pago y balanzas»: CLIENTE, según la especificación 5.1.1, como hoy. (b) Fila nueva «Sistema de cadena de frío: gateways y sensores de cámara (B‑01 y B‑02) y kit de los 28 camiones con frío (gateway, UPS, módulo de sondas, sondas y simuladores, sensor independiente, termógrafo e Iridium Edge)»: **LafroX**, según la especificación 5.1.x; Arquitecto (especificación), SRE (instalación y recepción); compra antes del banco de pruebas; paquetes 2.4, 4.1 y 6.5 |
| `subdocumento_6/contenido.tex:37` (texto de 6.1.3) | Si el texto dice que el CLIENTE compra el equipamiento de terreno, precisar que el sistema de cadena de frío lo compra LafroX, porque es infraestructura que LafroX opera y de la que dependen sus niveles de servicio |
| `subdocumento_6/tablas/adquisiciones.tex`, después de la fila «Starlink de las tres plataformas» (`:13`) | Fila nueva: «SIM M2M de dos operadores y servicio satelital Iridium de los camiones con frío» · Necesidad: «Aviso y curva de temperatura en ruta» · Responsable: «LafroX (5.3.x). SRE. Antes del piloto de cadena de frío. Paquete 6.6. Contratos». Usa la misma regla del SD6, que deja todos los servicios de conectividad a cargo de LafroX (fibra, LTE y Starlink). Numerar 5.3.x con el siguiente número libre de la cuenta 5.3 del T‑14 |
| `subdocumento_6/contenido.tex:64` (6.2.2 DevSecOps) | Una frase: el software de los camiones se despliega por etapas con Greengrass, con reversión |

---

## 7. SD7 — EDT, plan y cronograma (rama `LafroX-Subdoc7-LateX`)

**Los paquetes nuevos van en la cuenta que ya les corresponde.** Antes de numerar, leer la cuenta completa en `formulario-t14/contenido.tex` y su tabla en `formulario-t14/tablas/`, y usar el siguiente número libre de esa misma cuenta. Cada paquete nuevo lleva entregable, criterio de aceptación, responsable y mes, como los demás, y suma sus horas al T‑15.

| Paquete | Dónde va | Cambio |
|---|---|---|
| 2.4.x Validación del diseño del kit en banco de pruebas | Cuenta 2.4 «Validación de diseños» (`contenido.tex:147`) | **Nuevo.** Entregable: kit completo validado en laboratorio (pruebas V1–V3, V5–V8, V11, V13, V14, V16, V17 y V19). Responsable: Arquitecto o SRE |
| 2.4.x Mapeo térmico por tipo de carrocería | Cuenta 2.4 | **Nuevo.** Entregable: punto crítico, volumen de las botellas y tolerancias por tipo de caja (V4). Responsable: Calidad del CLIENTE con LafroX |
| 3.4.4 Cadena de frío, retención de lotes y retiro sanitario (M9) | `contenido.tex:217` y `tablas/tab_T14_21.tex:7` | **Cambiar** la descripción: reglas por familia, retención por SSCC, acción por defecto, disposición, doble evaluación en el TC58e y protocolo ante ruptura |
| 3.4.5 Ingesta de temperatura y posición de la flota | `contenido.tex:219` y `tablas/tab_T14_21.tex:8` | **Cambiar:** separar la temperatura, que es de **M9** (como dice el SD4): componentes de Greengrass del camión, red móvil y satélite. La posición sigue en M12. Corregir la misma asignación en el T‑18 |
| 5.1.1 Especificación de compra del equipamiento de terreno para el CLIENTE | `contenido.tex:389` | **Cambiar:** queda solo para los equipos de uso (terminales, impresoras, terminales de pago y balanzas); los sensores, termógrafos y gateways salen de este paquete |
| 5.1.x Especificación y compra del sistema de cadena de frío | Cuenta 5.1, junto a 5.1.2 (compra de sala, servidores y gabinetes de borde, a cargo de LafroX) | **Nuevo.** LafroX especifica y compra los gateways y sensores de cámara (B‑01 y B‑02) y los 31 kits de camión, con certificación Subtel y cotización local. Antes del banco de pruebas |
| 5.3.x Contrato de SIM M2M y servicio satelital de los camiones con frío | Cuenta 5.3, junto a los contratos de LTE y Starlink | **Nuevo.** Entregable: contratos con dos operadores móviles y con Globalsat Chile (Iridium SBD). Responsable: SRE. Antes del piloto |
| 6.5.4 Termógrafos instalados en los 28 camiones | `contenido.tex:469` y `tablas/tab_T14_40.tex:7` | **Cambiar:** «Kit de cadena de frío instalado y recibido en los 28 camiones con frío». Criterio: acta por camión, chequeo completo y prueba de alarma |
| 4.1.x Piloto de cadena de frío en 4 camiones | Cuenta 4.1, junto al plan de olas de la Etapa 1 (`contenido.tex:361`) | **Nuevo.** 6 semanas en 4 camiones (2 rurales, 1 urbano, 1 de transportista), antes de la ola de reparto; incluye V18, V20 y V21 |
| 7.1.3 Incorporación de los conductores de los transportistas | `contenido.tex:491` | **Agregar** al alcance: escaneos de salida y bajada, y lectura del rojo en el TC58e |
| 7.2.4 Procedimientos operativos rediseñados | `contenido.tex:507` | **Agregar:** procedimiento de contingencia por ruta ante falla del equipo de frío y procedimiento ante ruptura confirmada |

| Otros archivos del SD7 | Cambio |
|---|---|
| `subdocumento-07/contenido.tex:382` (7.3.3) | Piloto antes de la ola de reparto; los 28 kits instalados antes de que esa ola parta |
| `formulario-t18/tablas/tab_T18_olas_alcance.tex:4` y `:6` | Olas 1 y 3: la temperatura queda a cargo de M9 (no M12); kit instalado antes de la ola 3 |
| `formulario-t15/contenido.tex:72` y `tablas/tab_T15_1.tex` | Horas de los paquetes nuevos y de los cambiados, coherentes con los totales del T‑15 y del SD7 |
| `subdocumento-07-anexos/tablas/tab_7C1.tex:6` | R18‑03: agregar los paquetes nuevos |
| `subdocumento-07-anexos/tablas/tab_7E2.tex:8` | INT‑05: paquetes y volumen nuevos |
| `subdocumento-07-anexos/contenido.tex:57` (Anexo 7.F) | Supuestos de planificación: plazo de Subtel (unas 8 semanas para equipos de red móvil) y cotizaciones locales |
| Totales de la EDT | Si el SD7 cita «222 paquetes» o «217.543 HH», recalcular y actualizar esos totales en todos los subdocumentos que los citen |

---

## 8. SD2 y SD4

**SD2 (rama `LafroX-Subdoc2-LateX`).** Solo normativa, sin párrafos nuevos sobre aire y producto:

| Archivo:línea | Cambio |
|---|---|
| `contenido.tex:53` (2.2.2) | Completar la cita del RSA: arts. 68, 190, 191, 303, 102, 105 y 192, en la misma frase o lista que ya existe |
| `contenido.tex:80` (2.2.4) | Corregir: la tolerancia de −15 °C en transporte interurbano es del art. 190, y la de −12 °C, de los arts. 191 y 192 |

**SD4 (rama `subdoc-4`).** Aplicar la tabla §16.4 del documento técnico, archivo por archivo. En 4.2.1 (`04/partes/4.2_fisica/04_c_implementos.tex`) y en el T‑11, indicar que el sistema de cadena de frío (B‑01, B‑02, B‑03 y el kit de camión) lo provee, instala y mantiene LafroX, y que los equipos de uso los compra el CLIENTE según la especificación. Excepción: **no editar figuras** (por ejemplo, la figura de `02_a_emplazamiento.tex:132` y ARQL‑01); anotarlas en §9. Actualizar `Dimensionamiento/dimensionamiento/calculo.py` y regenerar `resultados.md` con las cifras de §3.

---

## 9. Lista de pendientes que la IA debe entregar al terminar

1. Figuras que quedaron desactualizadas: archivo y qué dato cambió.
2. Cifras que otros subdocumentos fuera del alcance citan y quedaron distintas (por ejemplo, SD13 con 10.920 mensajes, o los totales de la EDT y de los requerimientos).
3. Números nuevos que se usaron (RF, RNF, RNG y paquetes) y dónde quedaron.
4. Filas de la declaración de uso de IA modificadas.
5. **Para el Informe 3 (no se edita ahora):** el sistema de cadena de frío pasa a ser inversión de LafroX (sensores y gateways de cámara, y 31 kits de camión), más las 62 SIM M2M y el servicio satelital como costo de operación de LafroX.

---

## 10. Verificación final

- `grep` de «10.920», «224.652», «342.933», «230.252», «0,58 GB» y «28 termógrafos» en las ramas del alcance: no deben quedar en texto vigente.
- Cada requerimiento nuevo aparece en su anexo **y** en el T‑12.
- Cada paquete nuevo aparece en el T‑14, en el T‑15 y, si corresponde, en el T‑18 y en el Anexo 7.C.
- Ninguna figura modificada; ninguna entidad nueva en el SD5; nada en SD1, SD8, SD13 ni en el Informe 3.
- Compilar cada subdocumento sin errores.
