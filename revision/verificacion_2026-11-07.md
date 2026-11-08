# Verificación del prototipo · 07-11-2026

Estas correcciones viven solo en la rama `LafroX-Prototipo-HTML`. Se mantienen los servicios, actores y datos como **simulación local**. Los hallazgos de cobertura del Caso Logística no se reabren en este corte.

| Auditoría | Qué cambió | Cómo comprobarlo |
|---|---|---|
| B-01 | El encabezado público ya no comprime su botón de entrada. La lista de camiones de frío puede envolver sus textos. | Abrir las rutas públicas y de autenticación a 375×812 y Telemetría a 1024×768. |
| B-02, B-05 | La promoción se aplica por SKU; el acceso directo no cambia el avance del pedido. Preparación abre una escena de práctica con un borrador separado. | Como Preventista, activar el 3×2 y quitar otras líneas; quitar la cola elimina el descuento. Abrir `#/flujo?nuevo=1&paso=7` no permite rendir. |
| B-03 | Tablero, gráficos, detalle y CSV seleccionan la misma muestra. Las fechas, el canal y la zona viajan en el enlace de detalle. | Aplicar «Tradicional», abrir OTIF y exportar. Coinciden el universo del tablero y el CSV. |
| B-04 | Botón de ayuda fuera del enlace KPI, orden anunciado en el encabezado y enlace «Saltar al contenido» compatible con el router. | Activar los controles con teclado y comprobar que no cambia el fragmento al saltar. No es una certificación WCAG. |
| S-01 | Las altas críticas y el retiro verifican permiso aunque se abra su URL. Finanzas resuelve la solicitud de crédito y un segundo perfil debe aprobar el cambio de permisos. | Solicitar crédito como Preventista, resolver como Finanzas, volver al pedido. TI propone permisos; Operaciones decide. |
| S-02 | La planilla distingue ruta identificada de prueba y usa IDs de muestra en el sitio. | Abrir una ruta de la matriz con el perfil correspondiente; un enlace no cuenta como aprobación. |
| S-03 | Conductor propio y externo tienen rutas distintas; se conserva el estado por perfil. El peoneta no simula una sesión ni un segundo terminal. | Cambiar señal del conductor propio y abrir el perfil externo; no hereda su estado. |

## Repetir las pruebas

`node revision/verify.cjs` con Playwright disponible (o configurar `LFX_NODE_MODULES` y `LFX_BROWSER`). El script abre un servidor local, no escribe transacciones reales y registra resultados en `LFX_QA_REPORT` o el directorio temporal.

En Edge, el barrido general en claro cubrió 52 rutas × 5 tamaños (260 combinaciones) sin desbordamientos de página, controles HTML menores de 44 px ni errores de ejecución. El corte final también pasó las 11 comprobaciones funcionales y 120 combinaciones dirigidas de las pantallas modificadas en oscuro y alto contraste.

La prueba de responsividad no acredita conformidad WCAG, lector de pantalla, uso en hardware real, otros navegadores ni cumplimiento productivo de los requisitos del Caso.
