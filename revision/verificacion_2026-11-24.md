# Verificación del prototipo · 24-11-2026

Versión `20261124fix2`, publicada en https://patricioh315.github.io/LafroX/. Entrada directa con el perfil de evaluación (`#/inicio?perfil=evaluador`), que ve todos los módulos.

## Alcance

- 54 rutas registradas en `js/router.js`; se recorren 51 pantallas: todas las rutas sin parámetros y una instancia real de cada ruta con parámetros (pedido, devolución, cliente, indicador y lote). Queda fuera la ruta de profundización `/analitica/:kpi/ruta/:id`, que se abre desde un gráfico y no tiene enlace directo.
- Tamaños: 1920 × 1080, 1366 × 768, 1024 × 768, 768 × 1024 y 375 × 812 (255 combinaciones).
- Navegadores: Chromium 156 y Microsoft Edge.
- Accesibilidad: axe-core 4.10.3 con las etiquetas `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa` y `wcag22aa`, en las 51 pantallas a 1366 × 768 y a 375 × 812 (102 pasadas).

## Resultado

| Comprobación | Resultado |
|---|---|
| Pantallas que abren con su título, sin caer en «no encontrada» | 51 de 51 en los cinco tamaños |
| Desplazamiento horizontal de página | Ninguno en 255 combinaciones |
| Errores de ejecución o de consola | Ninguno |
| Infracciones axe WCAG 2.2 AA | 0 en 102 pasadas, en ambos navegadores |

## Correcciones de este corte

| Hallazgo | Corrección |
|---|---|
| `/verificacion`: los botones del método de segundo factor tenían `role="radio"` y además `aria-pressed`, atributo no admitido en ese rol. | Se conserva solo `aria-checked`. |
| `/terreno` a 375 px: la barra inferior fija cubría parcialmente la última parada visible (objetivo táctil obstruido). | En teléfono, solo el cuerpo de la app se desplaza entre la barra superior y la barra inferior; la miga de pan se oculta en esa vista. Ningún objetivo queda bajo las barras. |

## Límites

El recorrido es automático y por teclado. No reemplaza una prueba con lector de pantalla ni con personas usuarias, y los servicios externos (ERP, OTP, Transbank, GPS) siguen simulados.
