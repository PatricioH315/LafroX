# Prototipo interactivo · Distribuidora Puelche (LafroX)

Prototipo navegable de alta fidelidad de la plataforma logística que LafroX propone para Distribuidora Puelche S.A. (Caso 02 Logística). Responde al capítulo 25 de las Bases Técnicas Transversales y se entrega junto con el Informe 3.

- 51 pantallas que cubren los 9 bloques del numeral 25.2, los componentes del 25.4 y los requisitos RT-25.01 a RT-25.10.
- Cada pantalla declara su módulo de SD4 (M1–M12), sus requerimientos de SD3 y sus actores. Ver [docs/trazabilidad.md](docs/trazabilidad.md) y [docs/cumplimiento.md](docs/cumplimiento.md).
- Datos simulados; nada se envía a un servidor ni se guarda de forma permanente.

## Cómo abrirlo

No requiere instalación ni compilación (RT-25.06). Cualquiera de estas opciones sirve:

```bash
python -m http.server 5173
```

Luego abra `http://localhost:5173`. Para revisión sin conexión (RT-25.10), abra `index.html` directamente en el navegador.

Para recorrerlo, entre por «Ingresar», elija un actor en la lista desplegable y presione «Ingresar como este perfil»: no se piden credenciales. Hay un perfil predeterminado por cada uno de los 15 actores del sistema (SD3, Anexo 3.A.12a) y uno de evaluación que ve todos los módulos. El ingreso con correo y contraseña sigue disponible en «Ingresar con credenciales». Desde el menú de usuario se cambia de perfil en cualquier momento.

## Recorrido sugerido para la evaluación

1. `#/flujo`: el proceso principal de 7 pasos, con la opción de crédito retenido y la excepción «local cerrado».
2. `#/terreno`: la app del conductor; apague el interruptor de señal para ver el modo sin conexión y la cola de sincronización.
3. `#/devoluciones`: el proceso secundario con su flujo de aprobación.
4. `#/analitica`: indicadores, 8 tipos de gráfico, filtros y profundización hasta la entrega.
5. `#/arquitectura` y `#/sistema-diseno`: arquitectura de información (RT-25.09) y sistema de diseño (RT-25.05).
6. `#/cumplimiento`: dónde se demuestra cada exigencia y la matriz de trazabilidad con SD3 y SD4.

## Estructura

```text
index.html            Punto de entrada; carga estilos y scripts en orden
assets/logo.svg       Isotipo LafroX, vectorizado desde logo/lafrox_isotipo_naranja.pdf
css/tokens.css        Paleta, tipografía, espaciado, modo claro y oscuro
css/base.css          Estructura, retícula y puntos de quiebre
css/components.css    Componentes reutilizables
js/icons.js           Iconografía SVG
js/ui.js              Avisos, modales, validación, carga de archivos, menús, tablas, recorrido guiado
js/charts.js          Gráficos SVG sin dependencias
js/data.js            Datos simulados del caso
js/router.js          Enrutador por hash y rastro de navegación
js/app.js             Sesión, perfiles, menú, barra superior y preferencias
js/views/*.js         Una vista por pantalla, con su trazabilidad
docs/                 Trazabilidad y cumplimiento
```

## Publicación (RT-25.06 y RT-25.07)

El sitio es estático, por lo que puede publicarse en GitHub Pages desde la rama `LafroX-Prototipo-HTML` (Settings → Pages → Deploy from a branch → raíz). El enlace no vence mientras exista el repositorio, lo que cubre los seis meses exigidos. Las tipografías se cargan desde Google Fonts; si no están disponibles, la interfaz usa las fuentes del sistema sin perder funciones.
