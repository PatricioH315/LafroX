# Cumplimiento del capítulo 25 de las Bases

Dónde se demuestra cada exigencia del capítulo 25 (Bases Técnicas Transversales) en el prototipo. Las rutas se abren agregando el fragmento a la URL publicada, por ejemplo `…/index.html#/flujo`. El sistema de diseño y la arquitectura de información se documentan en `docs/sistema_diseno.md` y `docs/arquitectura_informacion.md`; ya no forman parte del sitio.

## Alcance mínimo (numeral 25.2)

| Bloque 25.2 | Pantallas |
|---|---|
| Portal principal | `/`, `/catalogo`, `/cobertura`, `/contacto`, `/inicio`, `/tablero`, `/bandeja`, `/notificaciones`, `/perfil` |
| Autenticación e incorporación | `/ingresar`, `/verificacion`, `/recuperar`, `/registro`, `/bienvenida` |
| Proceso operacional principal | `/flujo`, `/pedidos`, `/pedidos/:id`, `/rutas`, `/rutas/:id`, `/preparacion`, `/rendicion`, `/recepcion`, `/recepcion/nueva`, `/inventario` |
| Proceso operacional secundario | `/devoluciones`, `/devoluciones/nueva`, `/devoluciones/:id` |
| Perfil de terreno | `/terreno`, `/terreno/preventa` |
| Gestión de terceros | `/clientes`, `/clientes/:id`, `/portal/pedido`, `/portal/entregas`, `/portal/cuenta`, `/portal/transportista`, `/portal/proveedor`, `/canal-moderno` |
| Tablero analítico | `/analitica`, `/analitica/:kpi`, `/analitica/:kpi/ruta/:id` |
| Administración | `/admin/usuarios`, `/admin/roles`, `/admin/parametros`, `/admin/auditoria` |
| Módulo adicional 1: M9 Calidad y trazabilidad | `/calidad`, `/calidad/lotes/:id`, `/calidad/retiro` |
| Módulo adicional 2: M12 Telemetría y frío | `/telemetria` |

Detalle de los mínimos exigidos:

- **Portal principal:** inicio público; inicio con sesión distinto para cada uno de los 15 actores de SD3 más un perfil de evaluación; tablero con componentes que se agregan, ocultan y reordenan (arrastrando o con flechas); menú completo; rastro de navegación; menús contextuales.
- **Autenticación:** ingreso directo sin credenciales eligiendo el actor en una lista desplegable; además, ingreso con credenciales (correo o credencial de turno), registro de cliente en 5 pasos, recuperación de acceso en 3 pasos, segundo factor de 6 dígitos y bienvenida con recorrido guiado de 5 pasos.
- **Proceso principal (7 pasos):** preventa sin conexión → validación de stock y crédito → ruta → picking FEFO → carga y guía electrónica → entrega con prueba digital → rendición. Incluye los estados intermedios (Capturado sin conexión, Pendiente de validación, Retenido, Confirmado, Planificado, En picking, Cargado, En ruta, Entregado, Parcial, Fallido, Reprogramado, Rendido) y la excepción más frecuente: **local cerrado** (RF-06.04, RNG-05).
- **Proceso secundario:** devoluciones y envases (M8) con listado, detalle, creación y flujo de aprobación visual en 5 etapas.
- **Perfil de terreno:** apps de reparto y preventa en vista móvil, con modo sin conexión, cola de sincronización y funciones no disponibles sin señal, según SD4 Anexo 4-J.
- **Terceros:** directorio de clientes (tabla y tarjetas, paginación, filtros por canal), ficha con pestañas, evaluación, historial, documentos y envases; portal de transportistas (asignación de conductor y vehículo) y portal de proveedores (solo lectura).
- **Tablero analítico:** 6 indicadores del caso y 8 tipos de gráfico (líneas, barras, circular, barras apiladas, área, aguja, mapa de calor y dispersión); filtros por período, canal, zona y fechas; profundización en 3 niveles (indicador → ruta → entrega); exportación CSV, impresión y envío programado.
- **Administración:** personas usuarias (invitar, cambiar rol, suspender, importar CSV), matriz de roles y permisos con aviso de segregación de funciones, parámetros con aprobación de un segundo perfil y auditoría con filtros y exportación CSV o JSON.

## Componentes de interfaz (numeral 25.4)

| Categoría | Componente | Dónde se ve |
|---|---|---|
| Navegación | Menú principal | `#/inicio` |
| Navegación | Menú secundario contextual | `#/pedidos` |
| Navegación | Rastro de navegación | `#/clientes` |
| Navegación | Paginación | `#/clientes` |
| Navegación | Pestañas | `#/clientes/CL-10021` |
| Navegación | Acordeones | `#/admin/parametros` |
| Navegación | Navegación por pasos | `#/registro` |
| Navegación | Menú de acciones rápidas | `#/inicio` |
| Formularios | Validación en tiempo real | `#/registro` |
| Formularios | Selectores y desplegables | `#/devoluciones/nueva` |
| Formularios | Casillas y botones de opción | `#/devoluciones/nueva` |
| Formularios | Fecha y hora | `#/admin/auditoria` |
| Formularios | Carga de archivos con arrastrar y soltar | `#/registro` |
| Formularios | Autocompletado | `#/devoluciones/nueva` |
| Formularios | Formularios de varios pasos | `#/registro` |
| Visualización | Tablas con orden y filtro | `#/pedidos` |
| Visualización | Barras, líneas y circular | `#/analitica` |
| Visualización | Tarjetas de información | `#/inicio` |
| Visualización | Líneas de tiempo | `#/flujo` |
| Visualización | Indicadores de progreso | `#/rutas` |
| Visualización | Distintivos y etiquetas | `#/pedidos` |
| Visualización | Información contextual emergente | `#/analitica` |
| Retroalimentación | Éxito, error, advertencia e información | `docs/sistema_diseno.md` |
| Retroalimentación | Modales y diálogos | `#/admin/usuarios` |
| Retroalimentación | Notificaciones emergentes | `#/flujo` |
| Retroalimentación | Esqueletos de carga | `#/analitica` |
| Retroalimentación | Indicadores de progreso | `#/calidad/retiro` |
| Retroalimentación | Estados vacíos ilustrados | `#/rutas` |
| Acción | Botones primarios, secundarios y terciarios | `docs/sistema_diseno.md` |
| Acción | Botón de acción flotante | `#/terreno/preventa` |
| Acción | Acciones en línea | `#/flujo` |
| Acción | Menús contextuales | `#/pedidos` |
| Acción | Acciones masivas | `#/devoluciones` |
| Acción | Confirmación de acciones críticas | `#/admin/usuarios` |

## Requisitos RT-25.01 a RT-25.10

| Código | Requisito | Evidencia | Dónde |
|---|---|---|---|
| RT-25.01 | Navegación intuitiva, máximo tres interacciones | Tabla de caminos por perfil, accesos principales en el inicio, búsqueda global y acciones rápidas. | `docs/arquitectura_informacion.md` |
| RT-25.02 | Retroalimentación, carga y errores | Avisos, esqueletos, botones con carga, validación en línea y errores con instrucciones. | `docs/sistema_diseno.md` |
| RT-25.03 | WCAG 2.2 AA | Contraste verificado, 44 × 44 px, teclado completo, foco visible, saltar al contenido, etiquetas ARIA y textos alternativos. | `docs/sistema_diseno.md` |
| RT-25.04 | Diseño responsivo | Puntos de quiebre 375 / 768 / 1024 / 1366 / 1920; menú desplegable bajo 1024 px. | `docs/sistema_diseno.md` |
| RT-25.05 | Sistema de diseño documentado | 5 colores, 2 familias, iconografía, retícula de 8 px y componentes vivos. | `docs/sistema_diseno.md` |
| RT-25.06 | Enlace navegable sin instalación | HTML, CSS y JavaScript estáticos, sin complementos ni compilación. | `#/` |
| RT-25.07 | Acceso por seis meses | Publicación estática sin dependencias externas de ejecución (solo tipografías, con respaldo del sistema). | `#/` |
| RT-25.08 | Navegación completa e interactividad | Ingreso de datos, transiciones, posado y activo, carga de archivos, desplegables y validaciones simuladas. | `#/flujo` |
| RT-25.09 | Arquitectura de información | Mapa del sitio, diagrama de navegación, taxonomía, menús y jerarquía. | `docs/arquitectura_informacion.md` |
| RT-25.10 | Exportación para revisión sin conexión (deseable) | La carpeta funciona abriendo `index.html` sin servidor; se entrega en .zip. | `abrir-prototipo.bat` |

## Pruebas realizadas

- Ingreso directo con los 16 perfiles predeterminados, sin errores.
- Recorrido automático de las 49 rutas con el perfil de evaluación: ninguna con error de ejecución y todas con su título.
- Revisión de los 144 enlaces internos distintos y de los destinos de profundización de los gráficos: ninguno roto.
- Sin desplazamiento horizontal de página a 375 px en ninguna pantalla; revisión visual a 768, 1366 y 1920 px.
- Revisión automática de nombres accesibles: todos los botones, enlaces y campos tienen nombre o etiqueta.
- Flujo principal completo, con crédito retenido y con local cerrado; registro en 5 pasos con errores; ingreso con credenciales incorrectas y segundo factor; modo sin conexión con cola de sincronización.

## Pendiente antes de la entrega

- Publicar el enlace definitivo (RT-25.06) y registrarlo en el Informe 3. Hoy responde 404. Los seis meses de RT-25.07 no se pueden demostrar en la entrega: se acreditan con la publicación estable.
- ✓ Hecho el 04-11-2026: se corrigió en el prototipo todo lo que la revisión externa marcó como corregible: 8 requerimientos (RF-03.11, RF-03.12, RF-06.08, RF-07.08, RF-08.07, RF-14.06, RNF-05.02 y los botones de 38 px de RT-25.03) y 10 incoherencias de datos. Detalle en `revision/checklist_sd3_sd4.md`, sección 10.
- Títulos de RF-02.09 y RF-12.30 en el catálogo de main: agregados en la rama `fix/rf-catalog-titles`; falta fusionarla.
- No corregibles en el prototipo, por ser simulación: RNF-05.03, RNF-08.01, RNF-12.01, la revisión con lector de pantalla y la parte real (ERP, OTP, Transbank, GPS) de los requerimientos anteriores.
- Revisión con lector de pantalla (NVDA o VoiceOver): no se ha hecho; la revisión de accesibilidad fue automática y por teclado.
- Apertura sin servidor (RT-25.10): el código no usa módulos ES, `fetch` ni rutas absolutas, pero falta abrir `index.html` con doble clic en Chrome, Edge y Firefox para confirmarlo.

## Continuación verificada el 03-11-2026

Prioridad 3 completada: inactividad, firma avanzada simulada, JSON transversal, borradores con atajo y portal ligero. Barrido de 49 rutas en cinco tamaños (245 combinaciones); revisión de las diez pantallas intervenidas en cuatro modos de tema/contraste (200 combinaciones). Sin errores de JavaScript ni desbordamiento de página en los estados probados.

La planilla y la matriz se regeneraron; las casillas verificadas de Prioridad 3 quedaron marcadas. No se certifica el cumplimiento integral de los criterios no recorridos. Véase [evidencia, reproducción y límites](../revision/verificacion_prioridad3.md).
