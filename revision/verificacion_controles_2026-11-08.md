# Verificación de controles · 8 de noviembre de 2026

Alcance: perfil **Comisión evaluadora**, en el prototipo estático. No se modificaron asignaciones de perfiles ni permisos. Las altas, configuraciones y transacciones de práctica quedan en la sesión de la pestaña; no se envían a sistemas externos.

| Hallazgo | Resultado esperado y verificado |
|---|---|
| E-01 · Ver en el flujo | Muestra el estado del pedido seleccionado en solo lectura. |
| E-02 · Nuevo y duplicar pedido | Abren borradores distintos. La copia conserva el cliente y las líneas del pedido de origen sin modificarlo. Desde la ficha se conserva el cliente seleccionado. |
| E-03 · Comparativo de recepción | Abre la OC seleccionada. Una OC cerrada es de solo lectura; el pallet de una OC abierta queda asociado a esa OC. |
| E-04 · Descargar documentos | Pedidos, portal proveedor y portal transportista descargan un TXT con la referencia correcta y una advertencia de simulación. |
| E-05 · Importar personas | Lee el CSV, informa errores y duplicados, y agrega las filas válidas como altas pendientes. |
| E-06 · Alta de cliente y cadena EDI | El folio de alta y la configuración EDI se pueden consultar. El formulario no afirma haber validado ni conectado un sistema externo. |
| E-07 · Ver traza | Un ID inexistente devuelve «Sin resultados»; un pedido conocido devuelve una traza ilustrativa. |
| E-08 · Generar misiones | Agrega misiones de práctica para pedidos elegibles sin duplicarlas; cada enlace conserva el pedido y la misión. |
| E-09 · Acciones por fila | Las filas sin acciones aplicables no muestran un menú vacío. |

La revisión adicional de contraste en Clientes corrigió las estrellas de valoración: ahora se distinguen por su forma, no por un gris de bajo contraste.

## Repetir las pruebas

Desde la raíz del prototipo, con Node y Playwright instalados:

```sh
node revision/verify_admin_controls.cjs
node revision/verify_controls.cjs
node revision/verify.cjs
```

Las dos primeras pruebas pueden ejecutarse contra GitHub Pages con `LFX_QA_URL`. Las tres aceptan `LFX_NODE_MODULES` para localizar Playwright y `LFX_BROWSER` para usar un Chrome o Edge instalado.
