# Prioridad 3 y actualización de evidencias

Continuación del 03-11-2026 desde `ef50e4a9`, sobre `LafroX-Prototipo-HTML`. Se completaron las cinco funciones pendientes y se regeneró la trazabilidad. No se modificaron SD3, SD4 ni los otros worktrees.

## Pruebas funcionales

Ejecutadas en Edge sin interfaz, con Playwright y datos del prototipo:

| Función | Caso comprobado | Resultado |
|---|---|---|
| RF-12.29 | Cliente tradicional: temporizador expirado mientras hay un diálogo abierto | Cierra diálogo, invalida sesión simulada y redirige al ingreso |
| RF-12.29 | Cliente moderno: actividad renueva plazo; navegación con sesión vencida | Renueva el plazo y luego impide continuar con la sesión vencida |
| RF-18.01 | Avanzada con certificado vencido o revocado | Bloquea la firma y no guarda evidencia |
| RF-18.01 | Certificado vigente de prueba | Genera evidencia por perfil y descarga JSON; sin desbordamiento a 375 px |
| RF-17.12 | Tabla de 25 filas, búsqueda «Uno», orden descendente y página de 10 | Exporta las 12 coincidencias, ID 23 a ID 1, no solo la página |
| JSON manual | Tabla de picking de Flujo | Exporta las cuatro líneas actuales |
| Borradores | Guardar y recargar Portal y Flujo | Restaura el contenido desde sessionStorage, separado por perfil |
| Atajos | `g s`, preferencia desactivada y escritura en campo | Guarda solo cuando corresponde; no intercepta escritura |
| Navegación | `g i` | Vuelve al inicio del perfil |
| Portal ligero | Cambiar de modo con carrito existente | Conserva carrito, muestra seis productos por página, sin imágenes ni animaciones |

La firma es una **simulación sin validez legal**: certificado de prueba, validación local y sello de tiempo del navegador. La evidencia solo se conserva durante la sesión de la pestaña. El cierre de sesión no revoca tokens de servidor porque el prototipo no tiene servidor.

## Barrido de pantallas

- 49 rutas reales × 5 tamaños = **245 combinaciones**, incluyendo detalles de pedido, cliente, ruta, lote y devolución.
- Tamaños: 375 × 812, 768 × 1024, 1024 × 768, 1366 × 768 y 1920 × 1080.
- Sin errores de JavaScript, pantallas de error ni desbordamiento horizontal de página.
- Los controles HTML visibles y habilitados, contando el área de la etiqueta de los checkbox, alcanzan 44 × 44 px. Los mapas SVG y enlaces dentro de gráficos no entran en esta medición.
- Diez pantallas intervenidas × cinco tamaños × cuatro combinaciones de tema/contraste = **200 revisiones** de texto HTML sólido: claro/normal, oscuro/normal, claro/alto y oscuro/alto. Sin hallazgos por debajo del umbral de texto AA de la comprobación.
- Rutas revisadas en esos modos: `/portal/pedido`, `/portal/cuenta`, `/perfil`, `/flujo`, `/rendicion`, `/canal-moderno`, `/inventario`, `/recepcion`, `/telemetria` y `/admin/parametros`.
- Revisión visual de capturas móviles del portal en claro y oscuro, y de las tres pantallas que inicialmente desbordaban. La planilla se renderizó antes y después de editarla.

Correcciones del barrido: el stepper necesitaba un contenedor posicionado para que sus textos accesibles absolutos no extendieran la página; el OTP de seis dígitos necesitaba reducir campos a 44 px y separación a 2 px en móvil. Se ampliaron enlaces operativos aislados de tablas y fichas.

Esto verifica el estado inicial de las rutas y los casos funcionales enumerados, **no todos los estados de todos los procesos**. La comprobación de contraste excluye SVG, imágenes, fondos degradados, controles deshabilitados, transparencias y estados hover. No constituye un informe de conformidad WCAG ni sustituye NVDA/VoiceOver o pruebas con personas usuarias.

## Planilla y checklist

- Se conservaron las tres hojas y las 202 filas de requerimientos; IDs, tipos y títulos sin cambios. Se comprobaron por XML los encabezados congelados y los autofiltros originales; el generador restituye estos últimos tras una omisión del exportador, usando JSZip del mismo runtime.
- Resultado: **186 RF/RNG con ruta**, **10 RT con evaluación preexistente** y **6 documentales**. Cero «No» antiguos por falta de etiquetado. «Sí» expresa trazabilidad declarada, no aceptación funcional.
- Los seis documentales son RF-13.01 a RF-13.04, RF-16.01 y RF-16.04. Las capas 2–8 se clasifican «No aplica» al prototipo estático.
- La matriz Markdown ahora coincide con las **49 rutas**; se retiraron rutas documentales antiguas que ya no existen.
- Se marcaron únicamente las casillas comprobadas de Prioridad 3. No se marcaron automáticamente los demás criterios al encontrar un RF en el registro.

## Reproducir

El sitio sigue sin requerir instalación. Solo los verificadores requieren Node y Playwright; el actualizador de planilla requiere `@oai/artifact-tool`.

Desde la raíz del prototipo, en PowerShell:

```powershell
# Apuntar a los paquetes del runtime del host si no están en la resolución normal de Node.
$env:LFX_NODE_MODULES = '<ruta a node_modules del runtime>'
$env:LFX_BROWSER = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
$env:LFX_QA_REPORT = Join-Path (Get-Location) 'revision/qa_resultado.json'
node revision/verify.cjs

$env:LFX_ROUTES = '/portal/pedido,/portal/cuenta,/perfil,/flujo,/rendicion,/canal-moderno,/inventario,/recepcion,/telemetria,/admin/parametros'
$env:LFX_THEMES = 'light:normal,dark:normal,light:high,dark:high'
$env:LFX_CONTRAST = '1'
$env:LFX_QA_REPORT = Join-Path (Get-Location) 'revision/qa_contraste.json'
node revision/verify.cjs
```

Resultados observados: ejecución funcional exitosa, barrido 245/245, revisión de modos 200/200; cero errores, desbordamientos y hallazgos de contraste HTML. Los JSON y capturas son evidencia local generada, no fuentes del sitio. `node --check` sobre todos los JavaScript y `git diff --check` también pasan.

Regeneración documental: `node revision/update_trace.cjs`; planilla: `node revision/update_workbook.mjs` con el runtime indicado. Antes de autoría de planillas, ejecutar el marcador de operación del skill de spreadsheets. El script admite `--inspect` para renderizar sin editar y `LFX_PREVIEW_DIR` para guardar vistas previas.

## Límites y reversión

Continúan pendientes la aceptación detallada de casillas no verificadas, informe formal de accesibilidad, lector de pantalla y matriz de navegadores. No se afirma haber publicado el sitio ni probado servicios reales.

La unidad de comportamiento comprende `js/features.js`, su carga en `index.html`, integración en `js/app.js`, `js/ui.js`, vistas `clients.js`, `flow.js`, `home.js` y estilos táctiles/responsive. La unidad documental comprende generadores en `revision/`, checklist, README y los archivos de `docs/`. Revertir estos cambios contra `ef50e4a9` no requiere revertir Prioridades 1–2. No hay migraciones ni dependencias añadidas al sitio.

## Revisión final (03-11-2026)

Revisión independiente en el navegador integrado (Chromium), sin Playwright, sobre el estado completo de las tres prioridades.

| Comprobación | Alcance | Resultado |
|---|---|---|
| Trazabilidad | 192 RF y RNG de SD3 contra los `rf` de las rutas | 186 en alguna ruta y 6 documentales; ningún código ajeno a SD3 |
| Planilla | 329 URL de las tres hojas | 8 apuntaban a pantallas retiradas (`#/arquitectura`, `#/sistema-diseno`, `#/cumplimiento`); corregidas hacia `docs/` y `abrir-prototipo.bat` |
| Rutas | 49 rutas × 375, 768, 1024, 1366 y 1920 px | Sin errores, sin desplazamiento horizontal, sin enlaces rotos y controles de 44 × 44 px |
| Perfiles | 16 perfiles: cada entrada de su menú y su guía | Ninguna pantalla bloqueada ni con error |
| Contraste | 49 rutas × claro, oscuro, alto contraste claro y oscuro | 2 hallazgos en `/clientes`, corregidos: número del chip seleccionado y estrella vacía de la valoración |
| Nombres accesibles | Controles visibles de las 49 rutas | Sin controles sin nombre; sin `id` duplicados |
| Prioridad 3 | Inactividad, firma, JSON, borradores con `g s` y vista ligera | Funcionan; el borrador de Flujo se restaura tras recargar |

Corrección adicional: una sesión de cliente sin marca de tiempo se cerraba de inmediato por inactividad; ahora empieza a contar desde ese momento.

## Correcciones por análisis externo (03-11-2026)

Un análisis externo marcó 32 puntos. Verificados contra el texto de SD3 y el código:

| Resultado | Puntos |
|---|---|
| Faltaban y se construyeron | RF-07.05 y RF-03.09 (bloqueo de crédito en preventa), RF-07.06 (POS con código de autorización y voucher conciliado), RF-07.11 (recibos del preventista consolidados en lo que rinde), RF-07.08 (bandeja de pagos web «En revisión»), RF-07.09 (envío idempotente al ERP), RF-11.04 (Perfect Order por causa raíz), RF-11.08 (segmentación por rentabilidad con simulación), RF-14.06 (geocercas con entradas y salidas), RF-01.09 (cola y reintento al ERP), RNF-02.01 (CD sin enlace 24 h), RNF-05.02 (picking de 60 px, ≥ 15 mm), RNF-09.03 (auditoría de consultas con finalidad), RNF-12.02 (configurar una cadena EDI nueva) |
| Existían débiles y se reforzaron | RF-07.10 (abono visible en la ficha), RF-04.07 (ventana editable), RF-08.07 (devoluciones y mermas en el costo de servir), RF-03.08 (se usa la deuda vencida, como dice SD3) |
| Incorrectos en el análisis | RF-03.12 (SD3 alerta al responsable comercial, no al cliente; ya estaba) y RF-03.11 (SD3 pide conservar el precio pactado, no excepciones por cliente) |
| No demostrables en simulación | RNF-05.03, RNF-08.01 y RNF-12.01, más la retención real de RNF-01.02, 08.02 y 09.02 (se muestra la política y una restauración simulada) |
| Acción externa | RT-25.06 y RT-25.07: publicar en GitHub Pages |

Además:

- **RNF incorporados.** Los 90 RNF de SD3 no estaban en la planilla ni en el checklist. Ahora están: 18 demostrables con ruta, 21 no demostrables en simulación y 51 documentales. La planilla pasa a 292 filas.
- **Etiquetas auditadas.** Se revisó cada código declarado contra lo que muestra su pantalla. Se quitaron o movieron etiquetas sin respaldo (RF-04.02, RF-04.04, RF-14.02, RF-17.03, RF-12.23, RF-03.06 y las de `/guia`) y se construyó la evidencia que faltaba para RF-07.04 (cartera vencida con promesas de pago) y RF-18.03 (registro de envíos por canal). Las URL de la planilla se regeneraron desde las rutas.
- **Barrido final.** 49 rutas × 5 tamaños, pestañas nuevas a 375 px, 13 pantallas intervenidas en 4 modos de contraste y 16 perfiles: sin errores, desbordes, enlaces rotos ni controles bajo 44 px. La estrella vacía de la valoración es un gráfico y cumple 3:1.
