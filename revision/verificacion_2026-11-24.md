# Verificación del prototipo · 24-11-2026

Versión `20261124fix3`, publicada en https://patricioh315.github.io/LafroX/. Entrada directa con el perfil de evaluación (`#/inicio?perfil=evaluador`), que ve todos los módulos.

## Alcance

- 54 rutas registradas en `js/router.js`; se recorren 52 pantallas: todas las rutas sin parámetros y una instancia real de cada ruta con parámetros (pedido, devolución, cliente, indicador, detalle de indicador por ruta y lote).
- Tamaños: 1920 × 1080, 1366 × 768, 1024 × 768, 768 × 1024 y 375 × 812 (260 combinaciones).
- Navegadores: Chromium 156 y Microsoft Edge.
- Accesibilidad: axe-core 4.10.3 con las etiquetas `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa` y `wcag22aa`, en las 52 pantallas a 1366 × 768 y a 375 × 812 (104 pasadas).
- Objetivos táctiles: medición de cada botón, campo, selector, enlace fuera de texto corrido y elemento interactivo de gráficos en los cinco tamaños, con un mínimo de 44 × 44 px. En los gráficos se mide el área de toque real; cuando el gráfico no admite 44 px, se exige un control equivalente de 44 px que lleve al mismo destino.

## Resultado

| Comprobación | Resultado |
|---|---|
| Pantallas que abren con su título, sin caer en «no encontrada» | 52 de 52 en los cinco tamaños |
| Desplazamiento horizontal de página | Ninguno en 260 combinaciones |
| Errores de ejecución o de consola | Ninguno |
| Infracciones axe WCAG 2.2 AA | 0 en 104 pasadas, en ambos navegadores |
| Objetivos interactivos menores de 44 × 44 px sin equivalente | Ninguno en los cinco tamaños |

## Correcciones de este corte

| Hallazgo | Corrección |
|---|---|
| `/verificacion`: los botones del método de segundo factor tenían `role="radio"` y además `aria-pressed`, atributo no admitido en ese rol. | Se conserva solo `aria-checked`. |
| `/terreno` a 375 px: la barra inferior fija cubría parcialmente la última parada visible. | En teléfono, solo el cuerpo de la app se desplaza entre la barra superior y la barra inferior; la miga de pan se oculta en esa vista. |
| Encabezado público a 375 px: el logotipo enlazado medía 34 px de alto. | Altura mínima de 44 px. |
| `/analitica`, OTIF por ruta: las barras con detalle medían menos de 44 px de ancho en pantallas medianas. | Cada barra tiene un área de toque de la altura del gráfico, y la tabla «Ver datos en tabla» enlaza cada ruta a su detalle con un objetivo de 44 px. |
| `/telemetria`: en teléfono, las rutas del mapa esquemático medían 21 px. | Bajo el mapa, una fila de botones de 44 px por ruta abre la misma ficha del camión. |

## Límites

El recorrido es automático y por teclado. No reemplaza una prueba con lector de pantalla ni con personas usuarias, y los servicios externos (ERP, OTP, Transbank, GPS) siguen simulados.
