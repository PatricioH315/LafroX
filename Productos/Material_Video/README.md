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

> El kit visual (logo, láminas, rótulos y animación) y la guía de producción con las explicaciones están en la carpeta de trabajo `productos/Video/` del equipo audiovisual.
