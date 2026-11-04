# Prototipo interactivo · Distribuidora Puelche (LafroX)

Prototipo navegable de alta fidelidad de la plataforma logística que LafroX propone para Distribuidora Puelche S.A. (Caso 02 Logística). Responde al capítulo 25 de las Bases Técnicas Transversales y se entrega junto con el Informe 3.

- 49 pantallas que cubren los 9 bloques del numeral 25.2, los componentes del 25.4 y los requisitos RT-25.01 a RT-25.10.
- Cada pantalla declara su módulo de SD4 (M1–M12), sus requerimientos de SD3 y sus actores. La documentación de cumplimiento está en `docs/` y no se publica en el sitio.
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
5. Trazabilidad con SD3 y SD4: ver [docs/trazabilidad.md](docs/trazabilidad.md) y [docs/cumplimiento.md](docs/cumplimiento.md) (no forman parte del sitio).
6. Arquitectura de información (RT-25.09) y sistema de diseño (RT-25.05): ver [docs/arquitectura_informacion.md](docs/arquitectura_informacion.md) y [docs/sistema_diseno.md](docs/sistema_diseno.md).

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

Enlace en línea: https://patricioh315.github.io/LafroX/ (GitHub Pages, publicado el 04-11-2026).

El sitio es estático, por lo que puede publicarse en GitHub Pages desde la rama `LafroX-Prototipo-HTML` (Settings → Pages → Deploy from a branch → raíz). El enlace no vence mientras exista el repositorio, lo que cubre los seis meses exigidos. Las tipografías se cargan desde Google Fonts; si no están disponibles, la interfaz usa las fuentes del sistema sin perder funciones.

## Funciones de demostración (Prioridad 3)

- En **Perfil**, un cliente puede probar el cierre tras 15 minutos de inactividad adelantando el reloj de prueba. El temporizador también funciona sin ese botón.
- En **Estado de cuenta → Firmar acuerdo**, se simulan firma simple y avanzada, certificados vigentes/vencidos/revocados y evidencia descargable. Sin validez legal.
- Todas las tablas ofrecen **Exportar JSON**. Las tablas con filtros incluyen todos los registros filtrados y ordenados, no solo la página.
- **Guardar borrador** o `g s` en Flujo de pedido y Portal de pedidos. Los borradores duran la pestaña y están separados por perfil; no envían el pedido.
- **Activar vista ligera** en Portal de pedidos: seis productos por página, sin imágenes ni animaciones.

Pruebas reproducibles y límites: [revision/verificacion_prioridad3.md](revision/verificacion_prioridad3.md).
