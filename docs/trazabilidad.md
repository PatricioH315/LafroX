# Trazabilidad del prototipo con SD3 y SD4

Matriz de cada pantalla del prototipo con el bloque del numeral 25.2, el módulo de la arquitectura lógica (SD4) y los requerimientos que demuestra (SD3). Se genera desde el registro de rutas de la aplicación (`js/router.js`), el mismo que alimenta el menú y el mapa del sitio.

## Fuentes

| Documento | Archivo | Uso en el prototipo |
|---|---|---|
| SD3, requerimientos funcionales del caso | `sd3/tablas_anexo/rf_caso.tex` | RF citados por pantalla |
| SD3, requerimientos de las BTT y propios | `sd3/tablas_anexo/rf_btt.tex`, `rf_propios.tex` | Identidad, administración, auditoría, notificaciones |
| SD3, actores del sistema | `sd3/tablas_anexo/actores_sistema.tex` | Un perfil predeterminado por cada uno de los 15 actores, con su menú y permisos |
| SD3, reglas de negocio | `sd3/tablas_anexo/reglas_negocio.tex` | Validaciones y estados (RNG-01 a RNG-17) |
| SD3, glosario | `sd3/tablas_anexo/glosario.tex` | Taxonomía y nomenclatura |
| SD4, matriz de los doce módulos | `sd4/04/anexos/logica/partes/05_anexo_4_1_d_matriz_de_los_doce_modulos.tex` | Menú y mapa del sitio (M1 a M12) |
| SD4, capas de la arquitectura | `sd4/04/partes/4.1_logica/04_capas_de_la_arquitectura.tex` | Canales, tres interacciones, preferencias de tema, texto y densidad |
| SD4, funciones sin conexión | `sd4/04/partes/4.1_logica/16_…sin_conexion.tex` y Anexo 4-J | Comportamiento de las apps de terreno |

## Verificación

- El registro declara 186 códigos RF y RNG en 49 rutas. La declaración localiza la evidencia; no sustituye la prueba de aceptación.
- Los nombres de los 12 módulos coinciden entre SD3 (`contenido.tex`) y SD4 (Anexo 4-D). No se detectaron discrepancias.
- Cada módulo M1 a M12 tiene al menos una pantalla (ver la cobertura más abajo).
- Cada ruta tiene módulo y RF de SD3. Los documentos del prototipo están en `docs/`; no son rutas navegables.

## Cobertura de módulos SD4

| Módulo | Pantallas |
|---|---|
| M1 | `/portal/proveedor`, `/recepcion`, `/recepcion/nueva` |
| M2 | `/flujo`, `/inventario` |
| M3 | `/registro`, `/flujo`, `/terreno/preventa`, `/pedidos`, `/pedidos/:id`, `/clientes`, `/clientes/:id`, `/portal/pedido` |
| M4 | `/flujo`, `/rutas`, `/rutas/:id`, `/portal/transportista` |
| M5 | `/flujo`, `/preparacion` |
| M6 | `/flujo`, `/terreno`, `/pedidos/:id`, `/clientes/:id`, `/portal/entregas`, `/portal/transportista`, `/analitica/:kpi/ruta/:id` |
| M7 | `/flujo`, `/terreno`, `/pedidos/:id`, `/rendicion`, `/clientes`, `/clientes/:id`, `/portal/cuenta` |
| M8 | `/terreno`, `/devoluciones`, `/devoluciones/nueva`, `/devoluciones/:id`, `/clientes/:id` |
| M9 | `/calidad`, `/calidad/lotes/:id`, `/calidad/retiro` |
| M10 | `/tablero`, `/clientes`, `/clientes/:id`, `/analitica`, `/analitica/:kpi`, `/analitica/:kpi/ruta/:id` |
| M11 | `/registro`, `/portal/transportista`, `/portal/proveedor`, `/canal-moderno` |
| M12 | `/rutas/:id`, `/portal/transportista`, `/telemetria` |

## Matriz completa (49 pantallas)

| Pantalla | Ruta | Bloque 25.2 | Módulo SD4 | RF / RNG de SD3 | Actores (SD3, Anexo 3.A.12a) |
|---|---|---|---|---|
| Inicio público | `/` | Portal principal | Portal público | RF-12.14, RF-17.13 | Visitante, Cliente |
| Catálogo | `/catalogo` | Portal principal | Portal público | RF-12.14 | Visitante |
| Cobertura | `/cobertura` | Portal principal | Portal público | RF-17.13 | Visitante |
| Contacto | `/contacto` | Portal principal | Portal público | RF-17.13 | Visitante |
| Ingresar | `/ingresar` | Autenticación e incorporación | Base compartida (Keycloak) | RF-15.01, RF-15.02, RF-12.26, RF-06.08 | Todos los perfiles |
| Verificación en dos pasos | `/verificacion` | Autenticación e incorporación | Base compartida (Keycloak) | RF-15.03 | Perfiles administradores y de consola |
| Recuperar acceso | `/recuperar` | Autenticación e incorporación | Base compartida (Keycloak) | RF-12.27 | Todos los perfiles |
| Registro de cliente | `/registro` | Autenticación e incorporación | Portal de clientes (M11 canal, M3) | RF-12.25, RF-18.02, RF-17.08 | Cliente del canal tradicional, Cliente del canal moderno |
| Bienvenida | `/bienvenida` | Autenticación e incorporación | Transversal | RF-17.07, RF-18.02 | Todos los perfiles |
| Inicio | `/inicio` | Portal principal | Transversal | RF-17.07, RF-16.02, RF-17.11, RF-12.28 | Todos los perfiles |
| Tablero | `/tablero` | Portal principal | M10 Analítica (vista operacional) | RF-11.06, RF-16.02 | Gerentes, Jefaturas, Planificador |
| Bandeja de tareas | `/bandeja` | Portal principal | Transversal (flujos RF-17.06) | RF-17.06, RF-17.07 | Todos los perfiles |
| Notificaciones | `/notificaciones` | Portal principal | Transversal | RF-17.10, RF-18.03 | Todos los perfiles |
| Mi perfil y preferencias | `/perfil` | Portal principal | Transversal | RF-18.02, RF-15.03, RF-12.29 | Todos los perfiles |
| Flujo de pedido | `/flujo` | Proceso operacional principal | M3 · M2 · M4 · M5 · M6 · M7 | RF-03.01, RF-03.03, RF-03.09, RF-03.15, RF-03.16, RF-04.01, RF-04.06, RF-05.02, RF-05.05, RF-05.07, RF-06.01, RF-06.02, RF-06.04, RF-07.02, RF-07.03, RF-03.04, RF-03.07, RF-03.08, RF-03.10, RF-03.14, RF-05.03, RF-05.06, RF-06.03, RF-07.09, RF-09.11, RNG-01, RNG-03, RNG-05, RNG-08, RNG-12, RNG-13, RNG-15, RNG-16, RNG-17, RF-02.08, RF-06.10, RF-06.12, RF-07.10, RF-09.07 | Preventista, Planificador de Rutas, Preparador, Jefa de Bodega, Conductor, Gerente de Finanzas |
| Reparto en terreno | `/terreno` | Perfil de terreno | M6 Reparto · M7 · M8 | RF-06.01, RF-06.02, RF-06.04, RF-06.05, RF-06.07, RF-06.09, RF-06.11, RF-07.06, RF-09.06, RF-06.13, RF-09.12, RNG-12, RF-06.10, RF-06.12, RF-07.10, RF-09.07, RF-09.13 | Conductor propio, Conductor externo |
| Preventa en terreno | `/terreno/preventa` | Perfil de terreno | M3 Preventa | RF-03.02, RF-03.05, RF-03.06, RF-03.13, RF-03.15, RF-07.05, RF-08.04, RF-07.11 | Preventista |
| Pedidos | `/pedidos` | Proceso operacional principal | M3 Preventa | RF-03.03, RF-03.16, RF-17.12 | Preventista, Gerente Comercial, Gerente de Operaciones, Planificador de Rutas |
| Detalle de pedido | `/pedidos/:id` | Proceso operacional principal | M3 · M6 · M7 | RF-03.11, RF-06.14, RF-12.08, RNG-08, RF-03.10, RF-03.12 | Preventista, Gerente Comercial, Cliente |
| Rutas | `/rutas` | Proceso operacional principal | M4 Rutas | RF-04.01, RF-04.02, RF-04.03, RF-04.05, RF-11.05, RNG-14 | Planificador de Rutas, Gerente de Operaciones |
| Detalle de ruta | `/rutas/:id` | Proceso operacional principal | M4 Rutas · M12 | RF-04.02, RF-04.04, RF-14.02, RF-14.05, RF-04.08, RF-14.04 | Planificador de Rutas |
| Preparación | `/preparacion` | Proceso operacional principal | M5 Preparación | RF-05.01, RF-05.02, RF-05.04, RF-05.05, RF-09.08, RF-02.08 | Preparador, Jefa de Bodega |
| Cobranza y rendición | `/rendicion` | Proceso operacional principal | M7 Cobranza y rendición | RF-07.01, RF-07.02, RF-07.03, RF-07.08, RF-11.07 | Conductores, Gerente de Finanzas |
| Devoluciones y envases | `/devoluciones` | Proceso operacional secundario | M8 Devoluciones y envases | RF-08.01, RF-08.02, RF-08.03, RF-08.06, RF-17.12, RNG-07 | Conductores, Jefa de Bodega, Gerente de Finanzas |
| Registrar devolución | `/devoluciones/nueva` | Proceso operacional secundario | M8 Devoluciones y envases | RF-08.01, RF-06.09, RNG-06 | Conductores, Jefa de Bodega |
| Detalle de devolución | `/devoluciones/:id` | Proceso operacional secundario | M8 Devoluciones y envases | RF-08.02, RF-17.03, RF-17.06 | Jefa de Bodega, Jefa de Calidad, Gerente de Finanzas |
| Clientes | `/clientes` | Gestión de terceros | M3 · M7 · M10 (cartera) | RF-03.06, RF-07.04, RF-11.08, RF-17.12 | Preventista, Gerente Comercial, Gerente de Finanzas |
| Ficha de cliente | `/clientes/:id` | Gestión de terceros | M3 · M6 · M7 · M8 · M10 | RF-03.06, RF-04.07, RF-07.04, RF-08.03, RF-11.02, RF-17.08, RF-08.07, RNG-03 | Preventista, Gerente Comercial, Gerente de Finanzas |
| Hacer un pedido | `/portal/pedido` | Gestión de terceros | Portal de clientes · M3 | RF-12.15, RF-12.30, RF-12.29 | Cliente del canal tradicional, Cliente del canal moderno |
| Mis entregas | `/portal/entregas` | Gestión de terceros | Portal de clientes · M6 | RF-12.16, RF-06.11 | Clientes |
| Estado de cuenta | `/portal/cuenta` | Gestión de terceros | Portal de clientes · M7 | RF-07.07, RF-12.17, RF-12.18, RF-18.01 | Clientes |
| Portal de transportistas | `/portal/transportista` | Gestión de terceros | Portal de transportistas (canal M11) · M4 · M6 · M12 | RF-12.19, RF-12.20, RF-12.21, RF-06.08, RF-14.05 | Empresa transportista |
| Portal de proveedores | `/portal/proveedor` | Gestión de terceros | Portal de proveedores (canal M11) · M1 | RF-12.22, RF-12.23, RF-12.24, RF-01.01 | Proveedor |
| Canal moderno EDI | `/canal-moderno` | Gestión de terceros | M11 Canal moderno | RF-12.01, RF-12.02, RF-12.03, RF-12.04, RF-12.05, RF-12.06, RF-12.07, RF-12.09, RF-12.10, RF-12.11, RF-12.12, RF-12.13, RNG-11 | Cliente del canal moderno, Gerente Comercial |
| Tablero analítico | `/analitica` | Tablero analítico | M10 Analítica | RF-11.01, RF-11.02, RF-11.03, RF-11.04, RF-11.05, RF-11.06, RF-16.02, RNG-09 | Gerente Comercial, Gerente de Finanzas, Gerente de Operaciones, Jefa de Calidad |
| Detalle del indicador | `/analitica/:kpi` | Tablero analítico | M10 Analítica | RF-11.03, RF-11.06, RF-16.02 | Gerencias |
| Entregas de la ruta | `/analitica/:kpi/ruta/:id` | Tablero analítico | M10 · M6 | RF-11.03, RF-06.06 | Gerencias |
| Personas usuarias | `/admin/usuarios` | Administración | Base compartida (Keycloak) | RF-17.01, RF-15.05, RF-15.03 | Jefe de TI |
| Roles y permisos | `/admin/roles` | Administración | Base compartida (RBAC) | RF-15.04, RF-17.01, RF-17.03 | Jefe de TI |
| Parámetros | `/admin/parametros` | Administración | Registro versionado de parámetros | RF-17.02, RF-17.03, RF-02.01, RF-09.10, RF-17.09, RF-16.03 | Jefe de TI, Gerente de Finanzas, Jefa de Calidad |
| Auditoría | `/admin/auditoria` | Administración | Registro de auditoría inalterable | RF-17.04, RF-17.05 | Jefe de TI, Gerencias |
| Calidad y trazabilidad | `/calidad` | Módulo adicional 1 | M9 Calidad y trazabilidad | RF-02.10, RF-09.01, RF-09.02, RF-09.14 | Jefa de Calidad |
| Detalle de lote | `/calidad/lotes/:id` | Módulo adicional 1 | M9 Calidad y trazabilidad | RF-02.10, RF-09.01, RF-09.02, RF-09.09, RNG-04, RNG-17 | Jefa de Calidad |
| Simulacro de retiro sanitario | `/calidad/retiro` | Módulo adicional 1 | M9 Calidad y trazabilidad | RF-09.01, RF-09.06, RF-17.10 | Jefa de Calidad |
| Telemetría y frío | `/telemetria` | Módulo adicional 2 | M12 Telemetría | RF-09.04, RF-09.05, RF-09.06, RF-14.02, RF-14.03, RF-14.06, RF-09.03, RF-14.01, RNG-04 | Planificador de Rutas, Gerente de Operaciones, Jefa de Calidad |
| Recepción | `/recepcion` | Proceso operacional principal | M1 Recepción | RF-01.01, RF-01.08, RF-01.09, RF-12.23 | Jefa de Bodega, Preparador, Proveedor |
| Registrar recepción | `/recepcion/nueva` | Proceso operacional principal | M1 Recepción | RF-01.01, RF-01.02, RF-01.03, RF-01.04, RF-01.05, RF-01.06, RF-01.07, RF-01.11 | Jefa de Bodega, Preparador |
| Inventario | `/inventario` | Proceso operacional principal | M2 Inventario | RF-02.02, RF-02.04, RF-02.05, RF-02.06, RF-02.07, RF-02.09, RF-10.01, RF-10.02, RF-10.03, RNG-02, RNG-10, RF-01.10, RF-02.03, RF-02.11, RF-08.05, RNG-11 | Jefa de Bodega, Gerente de Operaciones, Preventistas |
| Guía de mi perfil | `/guia` | Portal principal | Transversal | RF-17.07, RF-16.02 | Todos los perfiles |

## Cierre de Prioridad 3 (03-11-2026)

- RF-12.29: temporizador global para ambos perfiles de cliente; 15 min según el parámetro de demostración. «Mi perfil» permite adelantar el reloj de prueba. No se simula un token de servidor.
- RF-18.01: «Estado de cuenta → Firmar acuerdo». Modos simple y avanzado simulados; certificado vencido/revocado bloquea, vigente genera evidencia JSON y sello de tiempo local. No tiene validez legal.
- RF-17.12: cada dataTable exporta todos los registros filtrados y ordenados a JSON, no solo la página. Las tablas manuales exportan sus filas actuales; no tienen paginación oculta.
- Borradores: botón y atajo `g s` en Flujo de pedido y Portal de pedidos; por perfil y pestaña. El atajo se desactiva en Perfil y no opera al escribir ni sobre un diálogo.
- Portal ligero: seis productos por página, sin imágenes ni animaciones; conserva el carrito al cambiar de modo.

La planilla conserva 202 filas: 186 RF/RNG con ruta, 10 RT con la evaluación preexistente y 6 documentales (RF-13.01 a RF-13.04, RF-16.01 y RF-16.04). Las capas 2–8 se clasifican «No aplica» al prototipo estático. «Sí» significa trazabilidad declarada; no certificación de producción ni validación automática de cada criterio.

Para regenerar: `node revision/update_trace.cjs` y `node revision/update_workbook.mjs` con el runtime de `@oai/artifact-tool`. Ver `revision/verificacion_prioridad3.md` para pruebas y límites.
