# Material del video de presentación — LafroX (Caso 02)

Todo lo necesario para producir y entregar el video de presentación de la propuesta
(Bases Técnicas Transversales, Capítulo 24). Responsable: Guillermo Castillo (encargado audiovisual).

| Archivo | Qué es | ¿Se entrega al profesor? |
|---|---|---|
| `Guion_Video_LafroX_v07.docx` | **Guion** del video (4:47): lo que dice cada integrante, qué recibe y entrega en la dinámica del objeto, y lo que aparece en pantalla | No (uso interno) |
| `Checklist_Encargado_Audiovisual.md` | **Checklist del encargado**: datos pendientes, material, preparación, grabación, edición, exportación y entrega | No (uso interno) |
| `Checklist_Video_LafroX_v04.docx` | **Checklist de verificación** del video contra las Bases (67 puntos; columna "Video final") | No (uso interno) |
| `declaracion/LAFROX-Declaracion-Derechos-Video.pdf` | **Declaración** de titularidad de derechos y autorización de uso del video (BTT 24.5). La firma **Alex Aravena** (Jefe de Proyecto y Apoderado) | **Sí**, firmada |
| `declaracion/LAFROX-Autorizacion-Imagen-Equipo.pdf` | **Autorización** de uso de imagen y voz de los 8 integrantes (respaldo interno de la declaración; las Bases no la exigen) | Opcional (puede ir en la USB) |
| `Guia_Produccion_Video_LafroX_v07.docx` | **Guía de producción**: auditoría del Cap. 24, reglas de la dinámica, escenas en tablas, kit visual, tiempos, plan de grabación y verificaciones | No (uso interno) |
| `Guion_Dinamica_Objeto_v01.docx` | Detalle de la dinámica "de la guía de papel al terminal" escena por escena y utilería | No (uso interno) |
| `Dinamica_vs_Bases_v01.docx` | La dinámica comparada con las exigencias de las Bases (9 condiciones) | No (uso interno) |
| `visuales/` | **Kit visual** para la edición (ver abajo) | No (se usa para editar) |

## Qué se entrega al profesor (BTT 24.5)

1. El video `LAFROX_Video_TFEP-01-2026_Caso02.mp4` (MP4 H.264, 1920×1080, ≥ 30 fps, ≥ 5 Mbps, ≤ 500 MB, ≤ 5 min).
2. Unidad USB etiquetada "LafroX SpA — Propuesta TFEP-01/2026 — Caso 02 Logística Distribuidora Puelche", con el video **y una copia de respaldo**.
3. Enlace de descarga sin restricciones y vigencia ≥ 60 días; **contraseña en un documento separado**.
4. La declaración firmada por Alex (`declaracion/LAFROX-Declaracion-Derechos-Video.pdf`).
5. En la propuesta: filas RT-24.01 a RT-24.06 del Formulario T-12 actualizadas a "Cumple".

## Firmas

- **Declaración:** solo Alex Aravena, como representante del PROPONENTE (BTT 24.5 y Art. 40.2 de las Bases Administrativas): firma completa en el espacio inferior y media firma en el pie. Completar a mano fecha, cédula y duración del video.
- **Autorización de imagen:** los 8 integrantes, el día de grabación.

## Compilar la declaración y la autorización

Formato oficial LafroX (`lafrox.cls`, tomado de `00/plantilla/formato-base`). Requiere LuaLaTeX (MiKTeX o TeX Live):

```bash
cd declaracion
latexmk LAFROX-Declaracion-Derechos-Video.tex
latexmk LAFROX-Autorizacion-Imagen-Equipo.tex
```

La declaración redefine el pie para dejar **la línea de media firma vacía** (sin firma escaneada).

## Kit visual (`visuales/`)

Identidad tomada del sitio oficial `lafrox.github.io`: isotipo del zorro, paleta `#0B0D12` / `#FF5A2C` / `#E8641B` y tipografías Archivo e IBM Plex Mono (licencia SIL OFL 1.1).

| Archivo o carpeta | Contenido | Uso en la edición |
|---|---|---|
| `visuales/video/E1_logo_animado.mp4` | Animación del logo (4 s, 1920×1080, 30 fps) | Pista V1, 0:00–0:04 |
| `visuales/png/00_capa_marca_permanente.png` | Logo, encabezado y pie de contacto (transparente) | Pista V3, desde 0:04 hasta el final |
| `visuales/png/0x_E*_*.png` | Láminas de fondo completo (cifras, beneficios, innovaciones, arquitectura, stack, casos, placas) | Pista V1 |
| `visuales/png/*_lateral.png`, `05_E5_mosaico_equipo.png`, `06_E6_rotulos_plano_grupal.png` | Paneles y capas transparentes | Pista V2 |
| `visuales/png/rotulo_01…08_*.png` | Rótulo de cada integrante (RT-24.02) | Pista V2, desde que la persona mira a cámara |
| `visuales/logo/` | Isotipo oficial (`oficial/lafrox-isotipo.svg`) y logotipo horizontal en PNG | Otros usos |
| `visuales/previews/` | Miniaturas de cada pieza con la capa de marca encima | Revisión |
| `visuales/fuente/` | Generadores (Python y Node) y tipografías | Regenerar piezas y documentos |

### Regenerar las piezas (cuando lleguen los datos pendientes)

Editar la sección `CONFIGURACIÓN` de `visuales/fuente/generar_visuales.py` (fecha, nombre del proyecto, años de experiencia y certificaciones de cada integrante) y ejecutar:

```bash
cd visuales/fuente
python generar_visuales.py
```

Requiere Python 3 y Chrome o Edge. Para regenerar solo algunas piezas: `python generar_visuales.py rotulo`. La animación del logo se regenera con `python logo_animado.py` (requiere Pillow y ffmpeg).

> **Pendiente del equipo antes de grabar:** años de experiencia, certificaciones según el T-8 (el CSV y el sitio web se contradicen en 6 de 8 personas), cargos exactos, fecha y nombre oficial del proyecto. Hoy las piezas muestran "[__]" donde faltan datos.
