# Checklist del encargado audiovisual — Video LafroX (Caso 02)

**Responsable:** Guillermo Castillo · **Entregable:** video de presentación (BTT Cap. 24), que se entrega **con la Propuesta Final**
**Material base:** `Guion_Video_LafroX_v07.docx` (**solo el guion**, para leer y ensayar) · `Guia_Produccion_Video_LafroX_v07.docx` (explicaciones, reglas, kit, tiempos) · `Guion_Dinamica_Objeto_v01.docx` (detalle de la dinámica) · `Dinamica_vs_Bases_v01.docx` (9 condiciones) · `Checklist_Video_LafroX_v04.docx` (67 verificaciones) · `visuales/` (kit gráfico listo)

> **Dinámica del video:** una **guía de despacho en papel** pasa de mano en mano en el problema (Alex → Leandro → Patricio); Patricio la **cambia por un terminal** con la app y el terminal viaja por Maximiliano, Bastián, Tomás, Guillermo, Álvaro y Alex hasta el plano grupal. **Sale de cuadro por la derecha, entra por la izquierda.**

> **Las 6 reglas que no se pueden romper (cada una descalifica):**
> 1. El video dura **5:00 o menos** (el guion con la dinámica está en 4:47; no agregar nada).
> 2. Aparecen **los 8 integrantes**, cada uno ≥ 10 s seguidos a cámara.
> 3. **1920×1080, MP4 H.264, ≥ 30 fps, ≥ 5 Mbps, ≤ 500 MB**, audio AAC/MP3 ≥ 44,1 kHz.
> 4. **Nada inventado**: cada cifra, certificación y cargo debe coincidir con la propuesta, el T-8 y el sitio web.
> 5. **Nada sin licencia** (música, fotos, íconos, B-roll).
> 6. El video **se entrega junto con la propuesta**.

Marca cada casilla cuando esté hecha. **Obligatorio** = sí o sí; **Recomendado** = mejora la nota.

---

## 0. Antes de todo: datos que me tienen que entregar (bloquean la grabación)

Sin esto no se pueden generar los rótulos finales y el video quedaría con "[__]" o con datos falsos.

- [ ] **Obligatorio** — Años de experiencia de los 8 integrantes. *Pedírselos a Alex (T-8).*
- [ ] **Obligatorio** — Certificaciones definitivas de cada uno. El CSV y el sitio web se contradicen en 6 de 8 personas (ver Checklist v03, sección 4.2). *Que el equipo decida una sola versión y que el sitio web se actualice igual.*
- [ ] **Obligatorio** — Cargos exactos según el T-8. Hoy hay dos versiones: AGENTS.md vs sitio web.
- [ ] **Obligatorio** — Fecha de la Propuesta Final.
- [ ] **Obligatorio** — Nombre oficial del proyecto. Hoy el kit dice "Plataforma de trazabilidad, promesa de entrega y costo de servir"; confirmar que sea el mismo de la portada.
- [ ] **Recomendado** — Que el equipo apruebe el slogan "Donde se pierde la señal, no se pierde el dato." y lo use también en el sitio y la portada.

**Cómo cargarlos:**
1. Abrir `visuales/fuente/generar_visuales.py` y editar la sección `CONFIGURACIÓN` (`FECHA`, `PROYECTO`, lista `EQUIPO`).
2. Ejecutar en esa carpeta:
   ```bash
   python generar_visuales.py
   ```
   (necesita Chrome o Edge; tarda unos 2 minutos y regenera las 29 piezas en `visuales/png/`).
3. Revisar que ningún PNG diga "[__]".

---

## 1. Material y equipo (conseguir 1 semana antes)

| ✔ | Elemento | Para qué | Mínimo aceptable |
|---|---|---|---|
| [ ] | Cámara o celular que grabe **1920×1080 (ideal 4K) a 30 fps** | Tomas de personas | Celular reciente en modo video, **no** en modo retrato |
| [ ] | **Trípode** | Mismo encuadre para todos (RT-24.04) | Trípode de celular con adaptador |
| [ ] | **1 micrófono corbatero** (y uno de respaldo) | Mismo sonido para los 8 (RT-24.06) | Corbatero con cable para celular |
| [ ] | **2–3 luces LED 5600 K** o softbox | Iluminación profesional (24.1) | 2 aros/paneles LED + luz ambiente apagada |
| [ ] | **Fondo**: pared gris oscura lisa o roll-up negro con logo naranja | Mismo fondo para todos | Pared lisa sin cuadros ni ventanas |
| [ ] | Tablet o segundo celular con **app de teleprompter** | Que miren al lente y no lean de un papel | Texto impreso grande pegado junto a la cámara |
| [ ] | Cinta adhesiva de color | Marcar en el piso dónde se para cada uno | — |
| [ ] | Audífonos con cable | Escuchar el audio mientras se graba | — |
| [ ] | Baterías cargadas, cargadores y **espacio libre** (≥ 64 GB) | No cortar la sesión | — |
| [ ] | Cronómetro (celular) | Medir los 10 s mínimos por persona | — |
| [ ] | Guion impreso: **Guion_Video_LafroX_v07.docx** (3 páginas: lo que dice, recibe y entrega cada uno) | Que cada uno practique su parte | 1 copia por integrante |
| [ ] | **Guías de despacho de papel** (3–4 copias, una por toma) | Objeto de la dinámica en el problema | Impresas por nosotros: “GUÍA DE DESPACHO N° 000123”, logo LafroX o genérico, **sin RUT ni datos reales** |
| [ ] | **Terminal o tablet** de mano | Objeto de la dinámica en la solución | Pantalla con la app LafroX (captura del prototipo), brillo bajo, **modo avión**, logo del fabricante **tapado** con cinta negra mate |
| [ ] | **Persona de apoyo** fuera de cuadro | Lanzar o entregar el objeto desde la izquierda de la cámara | Que solo se vea su mano, nunca la cara |
| [ ] | **Autorizaciones de uso de imagen** impresas (una por integrante) | Garantizar los derechos del material (24.5) | Hoja simple firmada |
| [ ] | Sala reservada (2–3 horas), silenciosa, sin eco | Audio limpio | Sala con cortinas o muebles blandos |

**Software (gratuito):**
- [ ] **DaVinci Resolve** (edición, pistas, exportación H.264, medidor de volumen) — o el editor que domines.
- [ ] **ffmpeg / ffprobe** para verificar el archivo final:
  ```bash
  winget install Gyan.FFmpeg
  ```

---

## 2. Preparación (D-7 a D-6)

- [ ] **Obligatorio** — Enviar a cada integrante su parte del `Guion_Video_LafroX_v07.docx`: **qué recibe, qué dice y qué entrega**, y su tiempo total de toma (ver tabla 3.3). Cada uno debe decir su texto en ≈ 1 s menos que su toma (ese segundo es para recibir el objeto).
- [ ] **Obligatorio** — Explicar las reglas de la dinámica: recibir **sin moverse de la marca**, objeto **bajo** (pecho o cintura), **primero recibir y después hablar mirando al lente**, el terminal **nunca se lanza**.
- [ ] **Obligatorio** — Avisar la vestimenta: formal o negocio informal; **colores sólidos** gris, blanco o azul oscuro. **No** ropa totalmente negra (se pierde en el fondo), **no** prendas naranjas grandes, **no** rayas finas.
- [ ] **Obligatorio** — Confirmar asistencia de los 8 el mismo día. Si falta Alex, Bastián, Álvaro, Leandro, Maximiliano o yo (Operación), el video queda **descalificado**. Reservar una segunda fecha de respaldo.
- [ ] **Recomendado** — Ensayo con cronómetro (D-6): cada uno lee su parte en voz alta 2 veces.
- [ ] **Obligatorio** — Ensayar los **pasos del objeto** con la persona de apoyo (D-6 y 20 min antes de grabar): primero sin cámara, después con cámara.
- [ ] **Obligatorio** — Designar quién maneja la cámara **cuando yo grabo mi parte** (3:19–3:32).

---

## 3. Día de grabación (D-5) — orden sugerido

### 3.1 Armado del set (primeros 30 min)
- [ ] Fondo listo; nada detrás que distraiga.
- [ ] Luz principal a 45°, relleno al otro lado más suave, contraluz detrás. **Ventanas tapadas** (la luz natural cambia).
- [ ] Cámara en trípode a la **altura de los ojos**, a 1,5–2 m. **Plano medio**: de la cintura a la cabeza, con aire arriba.
- [ ] En la cámara: **1920×1080 o 4K, 30 fps fijos**, exposición, foco y balance de blancos **bloqueados en manual**.
- [ ] Marca de cinta en el piso.
- [ ] Teleprompter justo bajo el lente.

### 3.2 Prueba (15 min)
- [ ] Grabar **15 s de prueba** con alguien y revisarlo con audífonos: sin eco, sin zumbidos, cara bien iluminada.
- [ ] Grabar **10 s de silencio de sala** (sirve para limpiar ruido en la edición).

### 3.3 Tomas individuales (≈ 75 min) — mismo encuadre, misma luz, mismo micrófono
| ✔ | Orden | Quién | Escena | Duración de la toma | Objeto: recibe → entrega |
|---|---|---|---|---|---|
| [ ] | 1 | Alex (presentación) | E2 · 0:14 | 15 s | Ya tiene la **guía** en la mano → la arruga y la lanza suave por la derecha |
| [ ] | 2 | Leandro | E2 · 1:00 | 16 s | Atrapa la **guía** por la izquierda → la pasa por la derecha |
| [ ] | 3 | Patricio | E3 · 1:16 | 15 s | Recibe la **guía** → en “aunque no haya señal” la cambia por el **terminal** → lo entrega por la derecha |
| [ ] | 4 | Maximiliano | E3 · 2:10 | 14 s | Recibe el **terminal** en la mano → lo entrega por la derecha |
| [ ] | 5 | Bastián | E4 · 2:24 | 16 s | Recibe el **terminal** → lo baja fuera de cuadro |
| [ ] | 6 | Tomás | E4 · 3:05 | 14 s | Recibe el **terminal**, muestra 1 s la pantalla → lo entrega por la derecha |
| [ ] | 7 | Guillermo (yo) | E4 · 3:19 | 14 s | Recibe el **terminal** → lo entrega por la derecha |
| [ ] | 8 | Álvaro | E4 · 3:33 | 14 s | Recibe el **terminal** → lo guarda bajo el brazo |
| [ ] | 9 | Alex (compromisos, 2.ª vez) | E5 · 4:13 | 15 s | Recibe el **terminal** → lo conserva para el plano grupal |

Para cada toma:
- [ ] Mínimo **3 tomas buenas** por persona, cada una **completa**: recibir + hablar + entregar. Si la recepción falla, se repite toda la toma.
- [ ] **Recibir sin dar pasos**: la persona no se mueve de su marca del piso.
- [ ] **Primero recibe (≈ 1 s), después mira al lente y habla.** Los 10 s mínimos se cuentan desde que mira a cámara.
- [ ] El objeto **bajo** (pecho o cintura), nunca delante de la cara ni abajo a la izquierda (ahí va el rótulo).
- [ ] Del que entrega **solo se ve la mano**; nunca dos personas en la misma toma.
- [ ] El papel se arruga **antes** de hablar; 1 s de silencio entre recibir y hablar.
- [ ] Mirar **al lente**, no a la pantalla.
- [ ] Cronometrar: **nunca menos de 10 s** mirando a cámara.
- [ ] **Recomendado**: grabar 2 s extra de cada persona sosteniendo el objeto quieta (plano de apoyo para la edición).

### 3.4 Tomas extra (30 min)
- [ ] **Mosaico (E5):** cada integrante 3–5 s mirando a cámara, **sin hablar**, mismo encuadre.
- [ ] **Plano grupal (E6):** los 8 en dos filas, misma ropa, mismo fondo, 10 s. **Alex al centro con el terminal** a la altura de la cintura; nadie con papel.
- [ ] **Voces en off** (todas las líneas "VOZ EN OFF" del guion v07): Alex, y Bastián en el diagrama y el stack. Mismo micrófono.
- [ ] **B-roll propio** (solo si queda tiempo): manos usando una tablet, guantes, documentos de la propuesta, equipo trabajando. **No** filmar marcas ni logos de terceros.

### 3.5 Antes de irse
- [ ] Copiar todo a **2 lugares** (computador + disco/Drive).
- [ ] **Firmas de las autorizaciones de uso de imagen** de los 8.
- [ ] Lista de asistencia firmada.

---

## 4. Edición (D-4)

**Proyecto:** 1920×1080, **30 fps**. Usar el orden y los tiempos del guion v07 y, de la guía de producción v07, la sección 7 (tiempos) y la sección 6 (kit visual).

**Pistas:**
- [ ] **V1** — tomas de cámara, láminas de fondo completo (`visuales/png/0x_...`) y `visuales/video/E1_logo_animado.mp4` en 0:00.
- [ ] **V2** — rótulos (`rotulo_01…08`) y paneles laterales (`..._lateral.png`, mosaico, rótulos del grupo).
- [ ] **V3 (arriba de todo)** — `00_capa_marca_permanente.png` desde **0:04 hasta el último cuadro** (logo + pie de contacto, RT-24.05).
- [ ] **A1** — voces. **A2** — música (solo si tiene licencia).

**Reglas:**
- [ ] **Obligatorio** — Rótulo de cada integrante **cada vez que aparece**: rótulo individual, mosaico, plano grupal y la 2.ª aparición de Alex. Entra 1 s después de que la persona aparece y dura ≥ 6 s.
- [ ] **Obligatorio** — No cortar a una lámina antes de que la persona lleve 10 s en cámara.
- [ ] **Obligatorio** — Rótulo y panel lateral **nunca al mismo tiempo** (primero sale el rótulo, después entra el panel).
- [ ] **Obligatorio** — Solo **fundidos cruzados de 0,5 s**. Nada de barridos, giros, zooms ni efectos.
- [ ] **Obligatorio** — **Pasos del objeto**: cortar en el movimiento (sale por la derecha → entra por la izquierda) con un **fundido de 0,3–0,5 s**. Revisar que la dirección sea siempre la misma y que no se vea un salto.
- [ ] **Obligatorio** — El rótulo entra **cuando la persona ya mira a cámara** (después de recibir), no mientras atrapa el objeto.
- [ ] **Obligatorio** — El video termina en la **placa final**, **sin fundido a negro** (el logo debe verse hasta el final).
- [ ] **Obligatorio** — Audio: mismo nivel para todos, normalizado a **−16 LUFS** (DaVinci: Fairlight › Loudness). Sin saltos de volumen entre personas.
- [ ] **Recomendado** — Música suave a −20 dB bajo las voces, con fundido de entrada y salida. Si no hay licencia, **sin música**.
- [ ] Duración total **4:47** (máximo absoluto 4:55).

---

## 5. Exportación y control técnico (D-2)

**En DaVinci Resolve (Deliver):** MP4 · H.264 · 1920×1080 · 30 fps · tasa de bits **12 000 kb/s** · audio AAC 48 kHz 192 kb/s.
**Nombre:** `LAFROX_Video_TFEP-01-2026_Caso02.mp4`

**O con ffmpeg** (desde un master exportado en alta calidad):
```bash
ffmpeg -i master.mov -c:v libx264 -profile:v high -pix_fmt yuv420p -r 30 -b:v 12M -maxrate 14M -bufsize 24M -c:a aac -ar 48000 -b:a 192k -af loudnorm=I=-16:TP=-1:LRA=11 -movflags +faststart LAFROX_Video_TFEP-01-2026_Caso02.mp4
```

**Verificar** (y guardar una captura de pantalla del resultado como evidencia):
```bash
ffprobe -v error -show_entries format=duration,size,bit_rate:stream=codec_name,width,height,r_frame_rate,sample_rate -of default=nw=1 LAFROX_Video_TFEP-01-2026_Caso02.mp4
```

| ✔ | Qué debe decir ffprobe | Mínimo exigido |
|---|---|---|
| [ ] | `duration` | **≤ 300** (esperado ≈ 287) |
| [ ] | `width` / `height` | **1920 / 1080** |
| [ ] | `codec_name` (video) | **h264** |
| [ ] | `r_frame_rate` | **30/1** |
| [ ] | `bit_rate` | **≥ 5 000 000** |
| [ ] | `size` | **≤ 524 288 000** (500 MB) |
| [ ] | `codec_name` (audio) / `sample_rate` | **aac** / **≥ 44100** |

**Revisión humana** (verlo completo 2 veces, una con audífonos):
- [ ] Los 6 segmentos en orden: introducción → problema → solución → tecnología → ventajas → cierre.
- [ ] Logo visible en **todas** las escenas; contacto siempre en el pie.
- [ ] No queda ningún "[__]" ni dato de relleno.
- [ ] Cifras iguales a la propuesta (OTIF 82,4 %, 41 %, 9 días, $31 M…).
- [ ] La dinámica cumple las **9 condiciones** de `Dinamica_vs_Bases_v01.docx` (sección 1.1): una persona por toma, 10 s mirando a cámara, encuadre fijo, rótulo visible, fundidos suaves, audio limpio, utilería sin marcas ajenas.
- [ ] Revisión cruzada con **Maximiliano** (D-3) usando `Checklist_Video_LafroX_v04.docx`: marcar la columna "Video final".

---

## 6. Qué le llevo al profesor (entrega con la Propuesta Final)

### 6.1 Unidad USB (física)
- [ ] **Obligatorio** — Etiqueta en la USB: **"LafroX SpA — Propuesta TFEP-01/2026 — Caso 02 Logística Distribuidora Puelche"**.
- [ ] **Obligatorio** — Dentro de la USB:
  - [ ] `LAFROX_Video_TFEP-01-2026_Caso02.mp4` (el video)
  - [ ] `LAFROX_Video_TFEP-01-2026_Caso02_RESPALDO.mp4` (**copia de respaldo**, exigida)
  - [ ] Carpeta `licencias/`: licencias de música (si hay), de imágenes de banco (si hay) y de tipografías (`visuales/fuente/fonts/OFL-*.txt`)
  - [ ] Captura del `ffprobe` (evidencia de calidad técnica)
- [ ] **Recomendado** — Probar la USB en **otro computador** el día anterior (D-1).

### 6.2 Enlace de descarga (digital)
- [ ] **Obligatorio** — Subir el video a Drive / OneDrive con enlace **sin límite de descargas** y vigencia **≥ 60 días** (configurar 90).
- [ ] **Obligatorio** — Proteger con contraseña y entregar la **contraseña en un documento separado** (no en la misma hoja del enlace).
- [ ] **Recomendado** — Probar el enlace desde una sesión de incógnito.

### 6.3 Documentos
- [ ] **Obligatorio** — Declaración de que LafroX **posee los derechos** de todo el material y **autoriza** la proyección del video en la evaluación (en la carta de la propuesta; coordinar con Alex).
  - Archivo: `declaracion/LAFROX-Declaracion-Derechos-Video.pdf` (formato oficial LafroX). Completar a mano fecha, cédula de Alex y duración del video; **firma Alex** (firma completa abajo y media firma en el pie).
- [ ] **Recomendado** — Autorización de uso de imagen y voz firmada por los 8 integrantes (respaldo de la declaración anterior): `declaracion/LAFROX-Autorizacion-Imagen-Equipo.pdf`. Hacerla firmar **el día de grabación**.
- [ ] **Obligatorio** — Pedir a quien lleva el **T-12** que cambie las filas **RT-24.01 a RT-24.06** de "No cumple — se entrega con la Propuesta Final" a **"Cumple"**, con el nombre del archivo y el minuto como evidencia (ej.: RT-24.01 → rótulos en 0:15, 1:02, 1:17…).
- [ ] **Recomendado** — Avisar a Alex para cerrar la decisión pendiente "Guion, casting y producción del video" en `Requerimientos/decisiones.md`.

---

## 7. Calendario resumido

| Día | Qué hago yo |
|---|---|
| **D-10** | Conseguir los datos de la sección 0 y regenerar el kit |
| **D-8** | Reservar sala y equipo; imprimir las guías de papel y preparar el terminal; enviar guion y código de vestimenta |
| **D-6** | Ensayo con cronómetro y **ensayo de los pasos del objeto** |
| **D-5** | **Día de grabación** (set, pruebas, 20 min de ensayo de la dinámica, 9 tomas con objeto, mosaico, grupo, voces, firmas) |
| **D-4** | Edición completa |
| **D-3** | Revisión cruzada con Maximiliano (Checklist v03) |
| **D-2** | Exportación, ffprobe, respaldo, subir enlace |
| **D-1** | Probar USB y enlace en otro equipo; preparar documento de la contraseña |
| **Entrega** | USB + enlace + contraseña aparte + declaración de derechos + T-12 actualizado |

---

### Archivos que voy a usar

| Archivo | Para qué |
|---|---|
| `Guion_Video_LafroX_v07.docx` | **Solo el guion**: lo que dice, recibe y entrega cada uno, y lo que aparece en pantalla |
| `Guia_Produccion_Video_LafroX_v07.docx` | Explicaciones: auditoría, reglas de la dinámica (sección 4), escenas en tablas, kit visual, tiempos, verificaciones |
| `Guion_Dinamica_Objeto_v01.docx` | Detalle de la dinámica escena por escena y utilería |
| `Dinamica_vs_Bases_v01.docx` | Las 9 condiciones para que la dinámica cumpla las Bases |
| `Checklist_Video_LafroX_v04.docx` | Verificación final punto por punto (columna "Video final") |
| `visuales/png/` | 29 piezas gráficas listas para la edición |
| `visuales/video/E1_logo_animado.mp4` | Animación del logo (0:00–0:04) |
| `visuales/logo/` | Logo oficial (isotipo) y logotipo horizontal |
| `visuales/fuente/generar_visuales.py` | Para regenerar las piezas cuando lleguen los datos pendientes |
