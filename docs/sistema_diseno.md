# Sistema de diseño del prototipo

Entregable del RT-25.05 (Bases Técnicas Transversales, cap. 25.3) y del RT-13.09. Documenta la paleta, la tipografía, la iconografía, la retícula y los componentes reutilizables del prototipo de Distribuidora Puelche. Según SD4 (capa de presentación), este mismo sistema lo comparten los portales y consolas (Angular con Tailwind CSS) y las apps Kotlin.

La fuente de verdad son los tokens de `css/tokens.css`. Los componentes están en `css/components.css` y sus funciones en `js/ui.js`.

## Resumen

| Exigencia | Cómo se cumple |
|---|---|
| A lo más cinco colores principales | Tinta, gris, fondo, superficie y naranja LafroX |
| A lo más dos familias tipográficas | Source Sans 3 (texto) e IBM Plex Mono (códigos y cifras) |
| Iconografía coherente | 77 íconos de trazo único sobre 24 px, propios del prototipo |
| Retícula y espaciado consistentes | Base de 8 px con 8 pasos de espaciado |
| Componentes reutilizables | Botones, formularios, tablas, gráficos, retroalimentación y navegación, con sus estados |

---

## 1. Color

### 1.1 Paleta principal (cinco colores)

| Token | Nombre | Claro | Oscuro | Uso |
|---|---|---|---|---|
| `--c-ink` | Tinta | `#111111` | `#F4F4F4` | Texto, encabezados, botón oscuro |
| `--c-gray` | Gris | `#5F5F5F` | `#B5B5B5` | Texto secundario e íconos |
| `--c-bg` | Fondo | `#F4F4F4` | `#111111` | Fondo de la aplicación |
| `--c-surface` | Superficie | `#FFFFFF` | `#1B1B1B` | Tarjetas, tablas y modales |
| `--c-accent` | Naranja LafroX | `#E8641B` | `#F29A5E` | Acción principal, foco y serie principal de los gráficos |

Los demás tokens de color (líneas, variantes suaves del naranja) son tonos derivados de estos cinco.

### 1.2 Reglas de contraste (WCAG 2.2 AA)

- El naranja `#E8641B` no se usa como texto sobre blanco. En botones lleva texto en tinta (5,7:1).
- Para texto de acento se usa `--c-accent-strong` `#A8440C` (5,4:1 sobre blanco).
- Los bordes de controles usan `--c-line-strong` `#8A8A8A` (3,4:1 sobre blanco, criterio 1.4.11).
- Todo texto cumple 4,5:1, y el texto grande 3:1, en modo claro y en modo oscuro.

### 1.3 Colores semánticos de estado

No forman parte de la paleta principal; solo comunican estado y siempre van acompañados de texto o ícono.

| Estado | Claro | Oscuro |
|---|---|---|
| Éxito | `#1E7A3C` | `#6FCF8F` |
| Advertencia | `#8A5A00` | `#F0C060` |
| Error | `#B3261E` | `#FF8A80` |
| Información | `#1D5FA8` | `#8AB8F0` |

### 1.4 Modos

| Modo | Cómo se activa |
|---|---|
| Claro u oscuro | Sigue al sistema, o se elige en la barra superior y en Mi perfil |
| Alto contraste | Mi perfil › Accesibilidad. Lleva texto y bordes a negro puro sobre blanco, o a blanco sobre negro |
| Alto contraste del sistema | Se respeta `forced-colors` de Windows |
| Movimiento reducido | Se respeta `prefers-reduced-motion`: se anulan transiciones y animaciones |

---

## 2. Tipografía

| Familia | Token | Uso |
|---|---|---|
| Source Sans 3 | `--font-sans` | Todo el texto de la interfaz |
| IBM Plex Mono | `--font-mono` | Identificadores (PV-264822, SSCC, GDE), códigos y cifras alineadas |

Si las fuentes no cargan, la interfaz usa las del sistema sin perder funciones.

### Escala

| Token | Tamaño | Uso |
|---|---|---|
| `--fs-4xl` | 48 px | Título de portada |
| `--fs-3xl` | 36 px | Cifras destacadas |
| `--fs-2xl` | 28 px | Encabezado de página |
| `--fs-xl` | 22 px | Encabezado de sección |
| `--fs-lg` | 18 px | Encabezado de tarjeta |
| `--fs-md` | 16 px | Texto de lectura |
| `--fs-sm` | 14 px | Texto secundario |
| `--fs-xs` | 13 px | Notas y metadatos (tamaño mínimo) |

Interlineado: 1,2 en títulos y 1,5 en texto. La persona usuaria puede ampliar el texto base a 18 o 20 px desde Mi perfil.

---

## 3. Iconografía

- 77 íconos SVG propios, de trazo único de 1,8 px sobre una cuadrícula de 24 px, con extremos redondeados (`js/icons.js`).
- Tamaños: 16 px (`icon-sm`), 20 px (por defecto) y 28 px (`icon-lg`).
- Heredan el color del texto (`currentColor`).
- Los íconos decorativos se ocultan a lectores de pantalla. Los botones que solo muestran un ícono tienen nombre accesible, y en escritorio amplio los de la barra superior muestran también su texto.

---

## 4. Retícula y espaciado

### 4.1 Espaciado (base de 8 px)

| Token | Valor |
|---|---|
| `--sp-1` | 4 px |
| `--sp-2` | 8 px |
| `--sp-3` | 12 px |
| `--sp-4` | 16 px |
| `--sp-5` | 24 px |
| `--sp-6` | 32 px |
| `--sp-7` | 48 px |
| `--sp-8` | 64 px |

### 4.2 Medidas fijas

| Token | Valor | Uso |
|---|---|---|
| `--target` | 44 px | Objetivo táctil mínimo de todo control (RT-25.03) |
| `--row-h` | 52 px (44 compacta, 60 amplia) | Alto de fila según la densidad elegida |
| `--sidebar-w` | 280 px | Menú lateral; ancho en que ninguna etiqueta se parte en dos líneas |
| `--topbar-h` | 64 px | Barra superior |
| `--radius-sm`, `--radius`, `--radius-lg` | 6, 10 y 16 px | Esquinas de controles, tarjetas y modales |

### 4.3 Puntos de quiebre

| Tamaño | Referencia | Comportamiento |
|---|---|---|
| Teléfono | 375 × 812 | Una columna, menú como panel, formularios en una columna |
| Tableta vertical | 768 × 1024 | Dos columnas donde cabe, menú como panel |
| Tableta horizontal | 1024 × 768 | Menú lateral fijo y plegable |
| Escritorio | 1366 × 768 | Menú lateral, paneles laterales en detalle |
| Escritorio amplio | 1920 × 1080 | Contenido con más márgenes y texto en los botones de la barra superior |

---

## 5. Componentes reutilizables

Cada componente tiene estados de reposo, posado, foco visible, activo y deshabilitado.

| Categoría | Componentes | Dónde verlos |
|---|---|---|
| Acción | Botón primario, secundario y terciario; botón de ícono; botón de acción flotante; menú contextual; acciones masivas; confirmación de acciones críticas | `/pedidos`, `/terreno`, `/admin/usuarios` |
| Formularios | Campo con validación en tiempo real, selector, casilla, opción, interruptor, fecha y hora, carga con arrastrar y soltar, autocompletado, formulario de pasos | `/registro`, `/devoluciones/nueva`, `/recepcion/nueva` |
| Navegación | Menú lateral plegable, rastro de navegación, pestañas, acordeón, paginación, indicador de pasos, acciones rápidas | Todas las pantallas con sesión |
| Datos | Tabla ordenable y filtrable, tarjeta de indicador, línea de tiempo, distintivo, ayuda emergente, 8 tipos de gráfico (líneas, barras en vertical, horizontal y apiladas, circular, área, aguja, mapa de calor y dispersión) | `/analitica`, `/tablero`, `/pedidos/:id` |
| Retroalimentación | Alertas de éxito, error, advertencia e información; modales; notificaciones emergentes; esqueletos de carga; estados vacíos ilustrados | `/flujo`, `/pedidos` con filtros sin resultados |

### Reglas de uso

- Una sola acción primaria por zona de la pantalla.
- Las acciones destructivas piden confirmación y usan color de error.
- Los errores dicen qué pasó y qué hacer, sin mensajes técnicos.
- Toda acción muestra respuesta: estado de carga en el botón y notificación al terminar.
