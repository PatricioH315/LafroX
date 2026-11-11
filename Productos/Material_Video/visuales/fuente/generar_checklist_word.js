// Genera la checklist verificada del video (Word). Uso: node generar_checklist_word.js salida.docx
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, HeadingLevel,
  AlignmentType, LevelFormat, BorderStyle, PageBreak, Footer, Header, PageNumber, PageOrientation } = require('docx');

const NEGRO = '0B0D12', NAR = 'E8641B', NAR_OSC = 'C2410C', GREY = 'F2F2F2';
const r = (t, o = {}) => new TextRun({ text: t, ...o });
const p = (t, o = {}) => new Paragraph({ spacing: { after: 100 }, ...o, children: Array.isArray(t) ? t : [r(t)] });
const h1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [r(t)] });
const h2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [r(t)] });
const b = t => new Paragraph({ numbering: { reference: 'bul', level: 0 }, spacing: { after: 60 }, children: Array.isArray(t) ? t : [r(t)] });
const n = t => new Paragraph({ numbering: { reference: 'num', level: 0 }, spacing: { after: 60 }, children: Array.isArray(t) ? t : [r(t)] });
const brk = () => new Paragraph({ children: [new PageBreak()] });
const cb = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
const borders = { top: cb, bottom: cb, left: cb, right: cb };
const COL = { 'OK': 'DFF2E3', 'PARCIAL': 'FFF0D6', 'NO': 'FBDADA', 'PENDIENTE': 'E6ECF5' };

function table(widths, rows, estadoCol = -1, head = NEGRO) {
  return new Table({
    width: { size: widths.reduce((a, c) => a + c, 0), type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((row, i) => new TableRow({ tableHeader: i === 0, cantSplit: true,
      children: row.map((c, j) => {
        let fill = i === 0 ? head : undefined;
        if (i > 0 && j === estadoCol) fill = COL[c];
        return new TableCell({ width: { size: widths[j], type: WidthType.DXA }, borders,
          margins: { top: 40, bottom: 40, left: 80, right: 80 },
          shading: fill ? { type: ShadingType.CLEAR, fill } : undefined,
          children: String(c).split('|').map(line => new Paragraph({ spacing: { after: 20 },
            alignment: (j === estadoCol || (i > 0 && j === row.length - 1 && c === '☐')) ? AlignmentType.CENTER : AlignmentType.LEFT,
            children: [r(line, i === 0 ? { bold: true, color: 'FFFFFF', size: 17 } : { size: 17, bold: j === estadoCol || j === 0 })] })) });
      }) })),
  });
}

// ---------------- CHECKLIST ----------------
// [ID, verificación, fuente, estado, evidencia/hallazgo, acción]
const H = ['ID', 'Qué se verifica', 'Fuente', 'Estado hoy', 'Evidencia / hallazgo', 'Acción', 'Video final'];
const W = [620, 2600, 1900, 1050, 4300, 3300, 800];
const G = {
 A: ['A. Especificaciones técnicas (24.1)', [
  ['A-01', 'Duración ≤ 300 s (más es descalificación)', 'BTT 24.1 · Rúbrica V1/V7', 'OK', 'Guion v06 cronometrado en 287 s (4:47), con la dinámica del objeto; locuciones medidas a 2,7 palabras/s.', 'Medir el master final con ffprobe y guardar la captura.'],
  ['A-02', 'Full HD 1920×1080, horizontal', 'BTT 24.1', 'OK', 'Las 28 piezas del kit y el MP4 del logo miden 1920×1080 (verificado con Pillow y ffprobe).', 'Proyecto de edición en 1920×1080.'],
  ['A-03', 'MP4 con códec H.264', 'BTT 24.1', 'OK', 'E1_logo_animado.mp4: h264 High, yuv420p.', 'Exportar el master en MP4/H.264.'],
  ['A-04', '≥ 30 cuadros por segundo', 'BTT 24.1', 'OK', 'Logo animado a 30 fps constantes.', 'Grabar y exportar a 30 fps constantes.'],
  ['A-05', 'Tasa de bits ≥ 5 Mbps', 'BTT 24.1', 'OK', 'Logo animado a 11,4 Mbps (CBR).', 'Exportar el master a 12 Mbps.'],
  ['A-06', 'Peso ≤ 500 MB', 'BTT 24.1', 'PARCIAL', 'Estimación: 12 Mbps × 287 s ≈ 430 MB. Aún no hay master.', 'Verificar el tamaño del archivo final.'],
  ['A-07', 'Audio ≥ 44,1 kHz/16 bit, AAC o MP3, normalizado, sin ruido', 'BTT 24.1 · RT-24.06', 'PARCIAL', 'Definido en el guion (AAC 48 kHz, −16 LUFS, mismo corbatero). Aún no se ha grabado.', 'Probar 15 s en la sala real y normalizar en la edición.'],
  ['A-08', 'Música solo con licencia acreditable', 'BTT 24.1 / 24.4', 'OK', 'El guion indica sin música o con licencia guardada.', 'Si se usa música, guardar el PDF de la licencia en la USB.'],
  ['A-09', 'Iluminación profesional, fondo neutro/corporativo, transiciones suaves, sin efectos', 'BTT 24.1 / 24.4', 'PARCIAL', 'Plan: tres puntos, fondo único, fundidos de 0,5 s y de 0,3–0,5 s en los pasos del objeto (ver Dinamica_vs_Bases_v01). Falta grabar.', 'Revisar los primeros clips antes de grabar a todos.'],
 ]],
 B: ['B. Contenido y orden obligatorio (24.2)', [
  ['B-01', 'Seis segmentos en el orden de 24.2', 'BTT 24.2', 'OK', 'Guion v06: E1 → E6 sin intercalar; la dinámica no cambia el orden.', '—'],
  ['B-02', 'Logotipo animado', 'BTT 24.2-1', 'OK', 'Corregido: E1_logo_animado.mp4 usa el isotipo OFICIAL del sitio (zorro) + “LAFROX” en Archivo 900. 1920×1080, 30 fps, 11,4 Mbps.', '—'],
  ['B-03', 'Nombre del proyecto', 'BTT 24.2-1', 'PARCIAL', 'Guion: “Plataforma de trazabilidad, promesa de entrega y costo de servir”. Las portadas usan la plantilla “Proyecto de Plataforma Digital de Misión Crítica — Caso [N. y nombre]”.', 'Fijar UN nombre oficial y usarlo igual en portada, T-12 y video.'],
  ['B-04', 'Nombre del caso y del proponente', 'BTT 24.2-1', 'OK', 'Placa de título: Caso 02 — Logística · Distribuidora Puelche S.A. · LafroX SpA.', '—'],
  ['B-05', 'Fecha de la propuesta', 'BTT 24.2-1', 'NO', 'La placa dice “[fecha de la propuesta]”.', 'Poner la fecha real de entrega de la Propuesta Final.'],
  ['B-06', 'Análisis de la problemática actual', 'BTT 24.2-2', 'OK', 'E2: historia del retiro (lote, 9 días) + cifras.', '—'],
  ['B-07', 'Impacto en las personas afectadas', 'BTT 24.2-2', 'OK', 'Lámina 02_E2_personas_afectadas (calidad, preparador, conductor, almacenero).', '—'],
  ['B-08', 'Riesgos de no implementar', 'BTT 24.2-2', 'OK', 'E2, Leandro: decidir a ciegas, pérdida en 2.000 clientes.', '—'],
  ['B-09', 'Métricas del problema', 'BTT 24.2-2 · Rúbrica V6', 'OK', 'Coinciden con la tabla canónica (INSTRUCCIONES_GLOBALES §3.1): OTIF 82,4 % (> 95 %), fill rate 91,3 % (> 97 %), 41 % sin lote, 9 días, $31 M, 6 meses ≈ 6 %, 96 camiones, ventana 05:30–07:00.', '—'],
  ['B-10', 'Demostración de comprensión del sector', 'BTT 24.2-2', 'OK', 'Consumo masivo, cadena de frío −22 °C, efectivo 38 %, competidor con entrega en 24 h.', '—'],
  ['B-11', 'Visión general', 'BTT 24.2-3', 'OK', 'E3, Patricio.', '—'],
  ['B-12', 'Beneficios por grupo de interés', 'BTT 24.2-3', 'OK', 'Lámina 03_E3_beneficios (4 grupos).', '—'],
  ['B-13', 'Diferenciadores clave', 'BTT 24.2-3', 'OK', 'Lámina 03_E3_diferenciadores. Coincide con “Por qué LafroX” del sitio web.', '—'],
  ['B-14', 'Innovaciones incluidas', 'BTT 24.2-3 · BA Art. 28', 'OK', 'Corregido: lámina y locución con INN-01 a INN-05 del T-19 vigente (SD13, 09-11-2026).', 'Si el T-19 cambia otra vez, regenerar la lámina.'],
  ['B-15', 'Resultados esperados con métricas', 'BTT 24.2-3', 'OK', 'OTIF > 95 %, fill rate > 97 %, guías perdidas 0, reentregas < 1 % (referencias del caso).', 'Confirmar que son las metas comprometidas en SD3.'],
  ['B-16', 'Conjunto tecnológico completo', 'BTT 24.2-4', 'OK', 'Corregido: Laravel 13 (PHP 8.5), Horizon y Redis, Kotlin/Zebra, PostgreSQL/PostGIS, Aurora, DynamoDB, Keycloak, RabbitMQ/SQS, GS1/EPCIS 2.0, OpenTelemetry, CloudWatch, Terraform (SD4 del 9-11).', '—'],
  ['B-17', 'Arquitectura de alto nivel', 'BTT 24.2-4', 'OK', 'Corregido: bloque Fargate dice “Laravel 13 · Horizon”. EKS y Kafka no se nombran (descartados en SD4).', '—'],
  ['B-18', 'Servicios de nube utilizados', 'BTT 24.2-4', 'OK', 'AWS: CloudFront, WAF, API Gateway, ECS Fargate, Aurora, DynamoDB, S3, Redshift, QuickSight (presentes en SD4).', '—'],
  ['B-19', 'Seguridad y cumplimiento normativo', 'BTT 24.2-4', 'OK', 'Zero Trust, ISO/IEC 27001, Ley 21.719, Ley 19.799. El sitio declara ISO/IEC 27001:2022 certificada (AENOR).', 'Opcional: agregar “ISO/IEC 27001:2022 certificada”.'],
  ['B-20', 'Por qué el proponente es la mejor opción', 'BTT 24.2-5', 'OK', 'E5: mosaico + “partimos del andén, la ruta y el almacén”.', '—'],
  ['B-21', 'Experiencia específica', 'BTT 24.2-5', 'OK', 'Corregido: “Desde 2012 operamos sistemas como este…” (sitio web y SD1).', '—'],
  ['B-22', 'Casos de éxito relevantes', 'BTT 24.2-5 · BTT 23.2', 'OK', 'Corregido: lámina 05_E5_casos_exito y locución con LogiNacional, FarmaRed y Lácteos del Sur, con las cifras del sitio y el T-6.', 'Mantener idénticos al sitio y al T-6.'],
  ['B-23', 'Garantías y compromisos', 'BTT 24.2-5', 'OK', 'E5: 56 meses, híbrido, sin dependencia de un proveedor, SLA por hito.', 'Opcional: certificaciones corporativas ISO 9001, 20000-1, CMMI-DEV 3.'],
  ['B-24', 'Valor agregado único', 'BTT 24.2-5', 'OK', '“Trazabilidad donde ocurre la operación, incluso sin señal”.', '—'],
  ['B-25', 'Cierre: compromiso, contacto e identidad final', 'BTT 24.2-6', 'OK', 'Placa final con logo oficial, lafrox.github.io, contacto@lafrox.cl y +56 32 250 4100.', 'Slogan: ver F-04.'],
 ]],
 C: ['C. Participación del equipo e identidad (24.3)', [
  ['C-01', 'RT-24.01: cada integrante solo, plano medio, a cámara, ropa formal, ≥ 10 s', 'BTT 24.3', 'OK', 'Guion v06: los 8 integrantes, cada uno 14–16 s en plano continuo (≥ 10 s mirando a cámara después de recibir el objeto), se presentan con su nombre.', 'Cronometrar cada toma en la edición.'],
  ['C-02', 'Equipo clave crítico completo (si falta uno: descalificación)', 'BA criterio “Capacidad de equipo” · BTT 24.4', 'OK', 'Jefe de Proyecto, Arquitecto, Seguridad, Datos, Calidad y Operación aparecen; también Desarrollo e Implantación.', 'Lista de asistencia el día de grabación.'],
  ['C-03', 'RT-24.02: rótulo en CADA aparición', 'BTT 24.3', 'OK', 'Rótulo individual + mosaico + plano grupal + segunda aparición de Alex.', '—'],
  ['C-04', 'RT-24.02: años de experiencia de cada uno', 'BTT 24.3', 'NO', 'No existe el dato individual en ningún documento del repo: el T-8/SD12 está vacío y el SD1 solo trae rangos de antigüedad por área.', 'Definir los años en el T-8 y cargarlos en generar_visuales.py.'],
  ['C-05', 'RT-24.02: cargo en el proyecto', 'BTT 24.3 · SD12 (traslado)', 'PARCIAL', 'Los cargos del video coinciden con AGENTS.md y el traslado SD12. El sitio web usa otros nombres (p. ej. “Liderazgo Funcional e Implantación”, “Arquitectura de Solución e Integración”). Trejo y Henríquez tienen doble rol.', 'Usar exactamente los cargos del T-8 en rótulos, sitio y video.'],
  ['C-06', 'RT-24.03: certificaciones', 'BTT 24.3 (deseable)', 'NO', 'Hay contradicción en 6 de 8 personas entre el CSV del equipo y el sitio web (ver tabla de la sección 4). Mostrar una certificación no acreditada es información falsa.', 'El equipo define la versión correcta en el T-8 y se regeneran los rótulos.'],
  ['C-07', 'RT-24.04: mismo fondo, iluminación y encuadre', 'BTT 24.3', 'PARCIAL', 'Plan: día único, mismo set, marcas en el piso.', 'Verificar en la grabación.'],
  ['C-08', 'RT-24.05: logotipo visible en todas las escenas', 'BTT 24.3', 'OK', 'Corregido: capa de marca permanente con el logo oficial desde 0:04 hasta el último cuadro; 0:00–0:04 es la animación del logo.', '—'],
  ['C-09', 'RT-24.05: paleta y tipografía corporativa consistentes', 'BTT 24.3 · Rúbrica V5', 'OK', 'Corregido: paleta del sitio (#0B0D12, #FF5A2C, #E8641B, #C2410C) y tipografías Archivo + IBM Plex Mono en las 29 piezas.', '—'],
  ['C-10', 'RT-24.05: datos de contacto en encabezado o pie', 'BTT 24.3', 'OK', 'Corregido: pie fijo con lafrox.github.io · contacto@lafrox.cl · +56 32 250 4100.', '—'],
  ['C-11', 'RT-24.06: volumen normalizado y misma calidad', 'BTT 24.3', 'PARCIAL', 'Plan: un solo corbatero y −16 LUFS.', 'Verificar en la edición.'],
 ]],
 D: ['D. Evaluación, descalificación y entrega (24.4–24.5)', [
  ['D-01', 'Sin material con derechos de autor sin licencia', 'BTT 24.4', 'PARCIAL', 'Logo oficial de la empresa; gráficos propios; Archivo e IBM Plex Mono con licencia OFL (incluida en fuente/fonts). Falta el B-roll y una posible música.', 'Carpeta licencias/ en la USB (incluir los OFL).'],
  ['D-02', 'Sin información falsa o engañosa', 'BTT 24.4 · BTT 23.2', 'PARCIAL', 'Corregidos: Django, innovaciones antiguas, web y contacto. Queda: certificaciones en conflicto (C-06) y años de experiencia (C-04).', 'Resolver C-04 y C-06 antes de grabar.'],
  ['D-03', 'USB etiquetada con empresa y proyecto, más archivo de respaldo', 'BTT 24.5', 'PENDIENTE', 'Checklist de entrega en el guion v03.', 'Preparar al final.'],
  ['D-04', 'Enlace de descarga ≥ 60 días, sin restricciones; contraseña en documento aparte', 'BTT 24.5', 'PENDIENTE', '—', 'Configurar 90 días.'],
  ['D-05', 'Declaración de derechos y autorización de proyección', 'BTT 24.5', 'PENDIENTE', '—', 'Incluir en la carta de la propuesta.'],
  ['D-06', 'Video entregado con la Propuesta Final', 'BTT tabla de entregables N° 26 · Rúbrica', 'PENDIENTE', '—', 'Incluir en el índice de la Propuesta Final.'],
 ]],
 E: ['E. Rúbrica interna del equipo (Rúbricas/Rúbrica Entrega 1/Rubrica_Video_y_Prototipo.md)', [
  ['E-01', 'V1 · Máximo 5 minutos', 'Rúbrica V1', 'OK', '287 s (4:47) con la dinámica.', '—'],
  ['E-02', 'V2 · Equipo clave completo presente y hablando', 'Rúbrica V2', 'OK', 'Los 8 hablan a cámara.', '—'],
  ['E-03', 'V3 · 6 segmentos en orden', 'Rúbrica V3', 'PARCIAL', 'La rúbrica trae un orden que NO es el de las Bases (empresa → problema → solución → arquitectura → innovaciones → plan de implementación) y cita mal el §24.1. Las Bases (24.2) mandan: introducción → problema → solución → tecnología → ventajas → cierre. El guion sigue las Bases.', 'Corregir V3 en la rúbrica para que no induzca a error.'],
  ['E-04', 'V4 · Producción comercial; no un zoom leyendo el PPT', 'Rúbrica V4', 'OK', 'Personas a cámara + láminas diseñadas para video.', '—'],
  ['E-05', 'V5 · Identidad coherente con informe, PPT, web y T-8/T-9', 'Rúbrica V5', 'PARCIAL', 'Logo, paleta, tipografía, web y contacto ya coinciden con el sitio. Faltan las certificaciones y los cargos según el T-8.', 'Ver C-05 y C-06.'],
  ['E-06', 'V6 · Cifras iguales a la tabla canónica', 'Rúbrica V6 · INSTRUCCIONES_GLOBALES §3.1', 'OK', 'Revisadas una por una (ver B-09).', '—'],
  ['E-07', 'V7 · Duración verificable', 'Rúbrica V7', 'OK', 'Control con ffprobe en el guion.', '—'],
 ]],
 F: ['F. Coherencia con el resto de la propuesta en GitHub', [
  ['F-01', 'Sitio web oficial', 'T-12 RT-23.05/23.06 (SD3, 9-nov) · BTT 23.3', 'OK', 'Corregido: el video muestra lafrox.github.io, igual que el T-12 y la declaración jurada.', '—'],
  ['F-02', 'Correo y teléfono oficiales', 'Sitio web (sección Contacto)', 'OK', 'Corregido: contacto@lafrox.cl · +56 32 250 4100.', '—'],
  ['F-03', 'Dotación de la empresa', 'Sitio web vs SD1', 'OK', 'Hay contradicción: el sitio dice 124 especialistas y el SD1 vigente 133. El video no menciona la cifra, por eso queda OK.', 'Si se menciona, alinear primero sitio y SD1.'],
  ['F-04', 'Slogan único', 'Presentación 1 · sitio web', 'OK', 'Slogan único del video: “Donde se pierde la señal, no se pierde el dato.” (placa final y cierre de Alex).', 'Llevarlo también al sitio web, la portada y la presentación.'],
  ['F-05', 'T-12 filas RT-24.01–24.06', 'SD3 LAFROX-Formulario-T-12.tex (9-nov)', 'PENDIENTE', 'Hoy dicen “No cumple — Se entrega con la Propuesta Final”.', 'Cuando exista el video, cambiar a “Cumple” con el archivo y el minuto como evidencia.'],
  ['F-06', 'Decisión pendiente “Guion, casting y producción del video”', 'Requerimientos/decisiones.md (main), ítem 2', 'PARCIAL', 'El guion v03 responde quién aparece, en qué orden y con qué mensaje.', 'Registrar la decisión como cerrada cuando el equipo apruebe el guion.'],
  ['F-07', 'No usar el video como “relleno” de alcance', 'retroalimentacion_entrega_1.md (SD3)', 'OK', 'El profesor criticó listar el video como exclusión o restricción. El SD3 vigente ya no lo hace.', 'Mantener.'],
  ['F-08', 'Cronograma 56 meses e híbrido', 'BA Art. 16–17 · INSTRUCCIONES_GLOBALES §3.2', 'OK', 'E5 menciona 56 meses e híbrido nube + on-premise.', '—'],
  ['F-09', 'Nombres de las personas iguales en todos los documentos', 'AGENTS.md · SD12 · sitio', 'OK', 'Los 8 nombres coinciden. Ojo con las tildes: “Bastián”, “Álvaro”, “Tomás”, “Miño”, “Henríquez”.', '—'],
 ]],
};

// Conteo
const all = Object.values(G).flatMap(g => g[1]);
const cnt = s => all.filter(x => x[3] === s).length;

const C = [];
C.push(
  new Paragraph({ spacing: { before: 1400, after: 200 }, alignment: AlignmentType.CENTER, children: [r('LafroX SpA', { bold: true, size: 36, color: NAR })] }),
  new Paragraph({ heading: HeadingLevel.TITLE, alignment: AlignmentType.CENTER, children: [r('Checklist verificada del video de presentación')] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [r('Licitación TFEP-01/2026 · Caso 02 — Logística · Capítulo 24 de las Bases Técnicas Transversales', { size: 24 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [r('Revisión del repositorio GitHub PatricioH315/LafroX (43 ramas) y del sitio oficial lafrox.github.io · v04: correcciones 1–5, slogan único y dinámica del objeto · 10-11-2026', { size: 20, color: '555555' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 400 }, children: [r(`${all.length} puntos verificados: ${cnt('OK')} OK · ${cnt('PARCIAL')} PARCIAL · ${cnt('NO')} NO · ${cnt('PENDIENTE')} PENDIENTE`, { bold: true, size: 26 })] }),
  brk(),
  h1('1. Resumen'),
  p('Versión v02: incluye las correcciones 1 a 5 ya aplicadas al guion v06 y al kit visual. Esta checklist reúne todo lo que el repositorio dice sobre el video y verifica cada punto contra lo producido hasta hoy: el guion v06 (con la dinámica del objeto) y el kit visual en productos/Video/visuales. Usa la escala del equipo (INSTRUCCIONES_GLOBALES §2): OK = cumple con evidencia; PARCIAL = presente pero incompleto o sin verificar; NO = ausente, contradictorio o con dato erróneo. Se agrega PENDIENTE para lo que todavía no corresponde hacer (por ejemplo, la entrega en USB). La última columna, “Video final”, sirve para marcar a mano cada punto sobre el video ya editado.'),
  h2('1.1 Corregido en esta versión'),
  n([r('Logo, paleta y tipografía oficiales ', { bold: true }), r('del sitio lafrox.github.io (isotipo del zorro, Archivo, IBM Plex Mono) en las 29 piezas y la animación.')]),
  n([r('Web y contacto: ', { bold: true }), r('lafrox.github.io · contacto@lafrox.cl · +56 32 250 4100.')]),
  n([r('Stack vigente: ', { bold: true }), r('Laravel 13/PHP 8.5 en vez de Django.')]),
  n([r('Innovaciones: ', { bold: true }), r('INN-01 a INN-05 del T-19 del 9-11-2026.')]),
  n([r('Experiencia y casos de éxito: ', { bold: true }), r('nueva lámina y locución con LogiNacional, FarmaRed y Lácteos del Sur.')]),
  h2('1.2 Lo que sigue pendiente (decisión del equipo)'),
  b('Certificaciones por persona (C-06): el CSV y el sitio se contradicen en 6 de 8 personas.'),
  b('Años de experiencia de cada integrante (C-04): no existen en ningún documento; definirlos en el T-8.'),
  b('Cargos exactos según el T-8 (C-05), fecha (B-05) y nombre oficial del proyecto (B-03).'),
  b('Corregir el orden de segmentos de la rúbrica interna V3 (E-03).'),
);

// Checklist
C.push(brk(), h1('2. Checklist verificada'));
for (const k of Object.keys(G)) {
  const [title, rows] = G[k];
  C.push(h2(title), table(W, [H, ...rows.map(x => [...x, '☐'])], 3), p(''));
}

// Correcciones
C.push(brk(), h1('3. Correcciones (✔ = aplicada en esta versión)'),
  table([600, 4200, 5470, 2400, 1900], [
    ['N°', 'Corrección', 'Detalle', 'Puntos', 'Quién'],
    ['1 ✔', 'Logo, paleta y tipografía oficiales', 'Isotipo del sitio (img/lafrox-isotipo.svg) + “LAFROX” en Archivo 900; paleta #0B0D12 / #FF5A2C / #E8641B / #FFC20E; regenerar las 28 piezas y la animación.', 'B-02, C-08, C-09, E-05', 'Kit (automatizable)'],
    ['2 ✔', 'Web y contacto', 'https://lafrox.github.io/ · contacto@lafrox.cl · +56 32 250 4100 en la capa de marca y la placa final.', 'B-25, C-10, F-01, F-02', 'Kit (automatizable)'],
    ['3 ✔', 'Stack Laravel', 'Lámina del stack, bloque Fargate del diagrama y locución de E4: PHP/Laravel + Horizon + Redis en vez de Django/Celery.', 'B-16, B-17, D-02', 'Kit + guion'],
    ['4 ✔', 'Innovaciones del T-19 vigente', 'Lámina de innovaciones y locución de E3 con INN-01…INN-05.', 'B-14, D-02', 'Kit + guion'],
    ['5 ✔', 'Experiencia y casos de éxito', 'Lámina nueva en E5 con los 3 casos del sitio/T-6 y la trayectoria desde 2012; locución “Versión A”.', 'B-21, B-22', 'Kit + guion'],
    ['6', 'Certificaciones y cargos', 'Resolver el conflicto CSV vs sitio en el T-8; luego regenerar rótulos y mosaico.', 'C-05, C-06', 'Equipo (decisión)'],
    ['7', 'Años de experiencia', 'Definirlos en el T-8 para los 8 integrantes.', 'C-04', 'Equipo (decisión)'],
    ['8', 'Fecha y nombre del proyecto (slogan ✔)', 'Fijar los tres y usarlos igual en todos los documentos.', 'B-03, B-05, F-04', 'Equipo (decisión)'],
    ['9', 'Rúbrica interna', 'Corregir el orden de segmentos de V3 según BTT 24.2.', 'E-03', 'Equipo'],
    ['10', 'Cierre administrativo', 'Actualizar T-12 RT-24.01–06 y decisiones.md cuando el video exista.', 'F-05, F-06', 'Equipo'],
  ], -1, NAR_OSC),
);

// Datos oficiales
C.push(brk(), h1('4. Datos oficiales encontrados en GitHub'),
  h2('4.1 Identidad y contacto (sitio lafrox.github.io, commit del 09-10-2026 “incorporar el logo”)'),
  table([3500, 7070, 4000], [
    ['Dato', 'Valor', 'Archivo'],
    ['Sitio web declarado', 'https://lafrox.github.io/', 'T-12 RT-23.05/23.06 (SD3)'],
    ['Correo / teléfono', 'contacto@lafrox.cl · +56 32 250 4100', 'index.html, sección Contacto'],
    ['Sede / domicilio', 'Santiago de Chile · Av. Brasil 2241, Valparaíso', 'index.html'],
    ['Logo', 'Isotipo (zorro) naranja #E8641B, SVG 432×432', 'img/lafrox-isotipo.svg'],
    ['Paleta', 'Negro #0B0D12 · naranja #FF5A2C · naranja oscuro #C2410C · amarillo #FFC20E · hueso #F6F7F9', 'css/styles.css'],
    ['Tipografía', 'Archivo (títulos y texto) · IBM Plex Mono (datos)', 'css/styles.css · Google Fonts'],
    ['Trayectoria', 'Fundada en 2012 (14 años); certificaciones ISO 9001:2015, ISO/IEC 27001:2022, ISO/IEC 20000-1:2018, CMMI-DEV 3', 'index.html · SD1'],
    ['Casos de éxito', 'LogiNacional S.A. (2021–22) · FarmaRed S.A. (2022–23) · Comercializadora Lácteos del Sur S.A. (2023–24)', 'index.html · T-6 (SD1)'],
  ], -1),
  p(''),
  h2('4.2 Certificaciones por persona: dos fuentes contradictorias'),
  table([2600, 3200, 4200, 4570], [
    ['Integrante', 'CSV del equipo (AGENTS.md)', 'Sitio web oficial', 'Usado hoy en el kit'],
    ['Alex Aravena', 'PMP (PMI); CSM', 'PMP (PMI); CSM', 'PMP, CSM (coincide)'],
    ['Bastián Trejo', 'AWS SA Professional', 'CKAD', 'AWS SA Professional'],
    ['Álvaro Catalán', 'CISSP; CEH', 'AWS SA Professional', 'CISSP, CEH'],
    ['Leandro Chamorro', 'CKAD', 'CKAD', 'CKAD (coincide)'],
    ['Tomás Pérez', 'CKAD', 'AWS SA Professional', 'CKAD'],
    ['Maximiliano Miño', '—', 'Mobile UI/UX Design Specialist (IDF)', '—'],
    ['Guillermo Castillo', '—', 'Mobile UI/UX Design Specialist (IDF)', '—'],
    ['Patricio Henríquez', '—', 'CISSP; CEH', '—'],
  ], -1),
  p('Nota: la combinación del CSV (seguridad con CISSP/CEH, arquitecto con AWS SA Pro) es más coherente con los roles, pero la que está publicada en el sitio es la que la Comisión verá. El T-8 debe definir una sola versión y el sitio debe actualizarse para coincidir.', { spacing: { before: 80 } }),
  h2('4.3 Stack vigente (SD3/SD4 del 9-nov)'),
  p('PHP/Laravel (monolito modular) con Horizon y Redis · Kotlin/Android en terminales Zebra · PostgreSQL + PostGIS on-premise · Aurora PostgreSQL · DynamoDB · S3 + Redshift + QuickSight · Keycloak · RabbitMQ local + SQS · API Gateway, CloudFront, WAF · ECS Fargate · OpenTelemetry · Starlink. EKS y Kafka quedan descartados explícitamente.'),
  h2('4.4 Innovaciones vigentes (T-19, SD13 del 9-nov)'),
  table([1300, 3600, 9670], [
    ['ID', 'Tipo', 'Nombre'],
    ['INN-01', 'Producto o servicio', 'Seguimiento de vencimiento posentrega en el local'],
    ['INN-02', 'Proceso', 'Reproducción de incidentes de terreno'],
    ['INN-03', 'Tecnológica o de arquitectura', 'Vida útil remanente por historia térmica del lote'],
    ['INN-04', 'Modelo de negocio o de contratación', 'Tramo variable de la Operación ligado al costo de servir'],
    ['INN-05', 'Experiencia de usuario, sostenibilidad o impacto social', 'Hoja de negocio del almacenero'],
  ], -1),
);

// Fuentes revisadas
C.push(brk(), h1('5. Fuentes revisadas en GitHub'),
  table([5600, 3400, 1300, 4270], [
    ['Archivo', 'Rama', 'Último commit', 'Qué aporta'],
    ['Bases/Bases_Tecnicas_Transversales.md (Título VII, Cap. 23–24)', 'main (idéntico en las 5 ramas que lo tienen)', '—', 'Requisitos 24.1–24.5 y entregable N° 26'],
    ['Bases/Bases_Administrativas.md', 'main', '—', 'Equipo clave crítico, T-8, Art. 76'],
    ['Rúbricas/Rúbrica Entrega 1/Rubrica_Video_y_Prototipo.md', 'main', '—', 'Verificaciones V1–V7 del equipo'],
    ['Rúbricas/Rúbrica Entrega 1/INSTRUCCIONES_GLOBALES.md', 'main', '—', 'Escala OK/PARCIAL/NO y cifras canónicas'],
    ['Requerimientos/decisiones.md', 'main', '—', 'Decisión pendiente: guion y casting del video'],
    ['LAFROX-Formulario-T-12.tex', 'LafroX-Subdoc3-LateX-CORRIGIENDO', '09-11-2026', 'RT-23 (web) y RT-24 (video: “No cumple”)'],
    ['retroalimentacion_entrega_1.md', 'LafroX-Subdoc3-LateX-CORRIGIENDO', '09-11-2026', 'Crítica del profesor al “relleno” de alcance'],
    ['Stack (Laravel, EKS descartado)', 'LafroX-Subdoc4-LateX-corrigiendo', '09-11-2026', 'Stack vigente'],
    ['SD13_v_nueva/T19 (Formulario T-19)', 'LafroX-Subdoc13-LateX-corrigiendo', '09-11-2026', 'Innovaciones vigentes'],
    ['contenido.tex · trazabilidad/TRASLADO-SD12 · ANTECEDENTES-SIMULADOS', 'LafroX-Subdoc1-LateX-CORRIGIENDO', '09-11-2026', 'Empresa, casos (T-6), roles y dedicación'],
    ['G02 - LAFROX - Primera Revisión Informe 2.md', 'Lafrox_Subdocumento_8_Latex_Revision', '08-11-2026', 'RT-24 aceptado como “se entrega con la Propuesta Final”'],
    ['Productos/Presentacion_1_LafroX.pdf', 'main', '—', 'Slogan y www.lafrox.cl'],
    ['Repositorio lafrox/lafrox.github.io', 'main', '09-10-2026', 'Logo, paleta, tipografía, contacto, equipo, casos'],
  ], -1),
);

const doc = new Document({
  creator: 'LafroX SpA', title: 'Checklist verificada del video',
  styles: {
    default: { document: { run: { font: 'Calibri', size: 20 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: 'Calibri', size: 48, bold: true, color: NEGRO }, paragraph: { spacing: { before: 0, after: 200 }, keepNext: true } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', run: { font: 'Calibri', size: 32, bold: true, color: NEGRO }, paragraph: { spacing: { before: 200, after: 140 }, keepNext: true, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', run: { font: 'Calibri', size: 25, bold: true, color: NAR_OSC }, paragraph: { spacing: { before: 200, after: 100 }, keepNext: true, outlineLevel: 1 } },
    ],
  },
  numbering: { config: [
    { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] },
    { reference: 'num', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 300 } } } }] },
  ] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838, orientation: PageOrientation.LANDSCAPE }, margin: { top: 1000, bottom: 1000, left: 1134, right: 1134 } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [r('LafroX SpA · Checklist del video · TFEP-01/2026 Caso 02', { size: 16, color: '777777' })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [r('Página ', { size: 16, color: '777777' }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '777777' })] })] }) },
    children: C,
  }],
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(process.argv[2], buf); console.log('ok', process.argv[2], `${all.length} items: OK ${cnt('OK')} PARCIAL ${cnt('PARCIAL')} NO ${cnt('NO')} PENDIENTE ${cnt('PENDIENTE')}`); });
