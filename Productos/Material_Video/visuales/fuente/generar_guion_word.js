const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  HeadingLevel, AlignmentType, LevelFormat, BorderStyle, PageBreak, Footer, Header, PageNumber,
  TableOfContents, ExternalHyperlink, ImageRun } = require('docx');

const NEGRO = '0B0D12', NAR = 'FF5A2C', NAR_OSC = 'C2410C', GREY = 'F2F2F2';
const out = process.argv[2];
const VIS = process.argv[3]; // carpeta productos/Video/visuales

const r = (t, o = {}) => new TextRun({ text: t, ...o });
const p = (t, o = {}) => new Paragraph({ spacing: { after: 100 }, ...o, children: Array.isArray(t) ? t : [r(t)] });
const h1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [r(t)] });
const h2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [r(t)] });
const h3 = t => new Paragraph({ heading: HeadingLevel.HEADING_3, children: [r(t)] });
const b = (t, lvl = 0) => new Paragraph({ numbering: { reference: 'bul', level: lvl }, spacing: { after: 60 }, children: Array.isArray(t) ? t : [r(t)] });
const chk = t => new Paragraph({ numbering: { reference: 'chk', level: 0 }, spacing: { after: 60 }, children: [r(t)] });
const kv = (k, v) => b([r(k + ': ', { bold: true }), r(v)]);
const warn = t => new Paragraph({ spacing: { before: 60, after: 120 }, shading: { type: ShadingType.CLEAR, fill: 'FFF1E6' },
  children: [r('⚠ Atención: ', { bold: true, color: NAR_OSC }), r(t)] });
const brk = () => new Paragraph({ children: [new PageBreak()] });
const gap = () => p('');

const cb = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
const borders = { top: cb, bottom: cb, left: cb, right: cb };
const ESTADO = { 'Cumple': 'E3F4E8', 'Corregido v03': 'FFE7D6', 'Corregido v04': 'FFE7D6', 'Pendiente equipo': 'FDECEC' };
function table(widths, rows, headerFill = NEGRO, colorCol = -1) {
  const total = widths.reduce((a, c) => a + c, 0);
  return new Table({
    width: { size: total, type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((row, i) => new TableRow({
      tableHeader: i === 0, cantSplit: true,
      children: row.map((c, j) => {
        let fill = i === 0 ? headerFill : (i % 2 === 0 ? GREY : undefined);
        if (i > 0 && j === colorCol && ESTADO[c]) fill = ESTADO[c];
        return new TableCell({
          width: { size: widths[j], type: WidthType.DXA }, borders,
          margins: { top: 50, bottom: 50, left: 90, right: 90 },
          shading: fill ? { type: ShadingType.CLEAR, fill } : undefined,
          children: String(c).split('|').map(line => new Paragraph({ spacing: { after: 20 },
            children: [r(line, i === 0 ? { bold: true, color: 'FFFFFF', size: 18 } : { size: 18, bold: j === colorCol })] })),
        });
      }),
    })),
  });
}
function img(file, w = 300) {
  const f = path.join(VIS, file);
  if (!fs.existsSync(f)) return p('[falta imagen ' + file + ']');
  return new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 },
    children: [new ImageRun({ type: 'jpg', data: fs.readFileSync(f), transformation: { width: w, height: Math.round(w * 9 / 16) } })] });
}
const noB = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
function gallery(items) { // [file, caption]
  const rows = [];
  for (let i = 0; i < items.length; i += 2) {
    rows.push(new TableRow({ cantSplit: true, children: [0, 1].map(k => {
      const it = items[i + k];
      return new TableCell({ width: { size: 4819, type: WidthType.DXA }, borders: { top: noB, bottom: noB, left: noB, right: noB },
        margins: { top: 60, bottom: 60, left: 60, right: 60 },
        children: it ? [img(it[0], 300), new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 80 },
          children: [r(it[1], { size: 16, color: '555555' })] })] : [p('')] });
    }) }));
  }
  return new Table({ width: { size: 9638, type: WidthType.DXA }, columnWidths: [4819, 4819], rows });
}

// ======================= ESCENAS v03 =======================
const scenes = [
 { t: 'ESCENA 1 — Introducción corporativa', time: '0:00 – 0:14 (14 s)', obj: 'Exigido por 24.2-1: logotipo animado, nombre del proyecto, nombre del caso, fecha y nombre del proponente.',
   who: 'Sin personas. Gráfica + voz en off (Alex Aravena).',
   shots: [
    ['0:00–0:04', 'Animación del logo oficial (E1_logo_animado.mp4): aparece el isotipo del zorro, se escribe LAFROX y luego “Ingeniería logística”.', '(Música suave, solo con licencia)', 'Logo oficial animado', 'E1_logo_animado.mp4'],
    ['0:04–0:14', 'Placa de título. Desde aquí entra la capa de marca permanente.', 'LafroX SpA presenta su propuesta técnico-económica para el Caso 02, Logística: una plataforma de trazabilidad, promesa de entrega y costo de servir para Distribuidora Puelche.', 'Proyecto · Caso · Licitación · Proponente · Fecha', '01_E1_placa_titulo'],
   ],
   todo: [
    ['Edición', 'Colocar el MP4 del logo en 0:00 y la placa en 0:04 con fundido de 0,5 s. La capa 00_capa_marca_permanente.png entra en 0:04 y queda hasta el último cuadro.'],
    ['Narrador (Alex)', 'Voz grabada en el mismo set y micrófono que el resto (RT-24.06).'],
    ['Revisión', 'Confirmar los 5 elementos: logo animado, nombre del proyecto, caso, fecha real y proponente.'],
   ] },
 { t: 'ESCENA 2 — Comprensión del problema', time: '0:14 – 1:16 (62 s)', obj: 'Problemática, impacto en las personas, riesgo de no actuar, métricas y comprensión del sector (24.2-2). Se abre con una historia real del caso, no con la empresa.',
   who: 'Alex Aravena (Jefe de Proyecto) y Leandro Chamorro (Líder de Datos).',
   shots: [
    ['0:14–0:29', 'EN CÁMARA Alex, plano medio, mirando al lente. OBJETO: parte con la guía de papel en la mano; al final la arruga y la lanza suave fuera de cuadro por la derecha.', 'Hola, soy Alex Aravena, jefe de proyecto de LafroX. En marzo de 2026, un proveedor pidió a Puelche saber, ese mismo día, a qué clientes llegó un lote de queso. Tardó nueve días… y fue una estimación.', 'Rótulo de Alex', 'rotulo_01_alex_aravena'],
    ['0:29–0:49', 'LÁMINAS de cifras, 5 s cada una, con fundido.', 'Cuarenta y uno por ciento de las recepciones no registraban el lote. Treinta y un millones de pesos perdidos y seis meses fuera de un proveedor clave. El OTIF es de ochenta y dos por ciento y una guía perdida tarda doce días en aparecer. Y un competidor ya entrega en veinticuatro horas.', '41 % · $31 millones · 82,4 % · 7,8 %', '02_E2_cifra_1…4'],
    ['0:49–1:00', 'LÁMINA de personas afectadas.', 'Detrás de cada cifra hay personas: la jefa de calidad buscando en carpetas, el preparador a veintidós bajo cero, el conductor rindiendo efectivo sin respaldo, el almacenero esperando.', 'Impacto en las personas', '02_E2_personas_afectadas'],
    ['1:00–1:16', 'EN CÁMARA Leandro, mismo encuadre y fondo. OBJETO: la guía arrugada entra por la izquierda; la atrapa, mira al lente y habla; al final la pasa por la derecha.', 'Hola, soy Leandro Chamorro, líder de datos. En consumo masivo, el margen se juega en el costo de servir. Puelche lo calcula con un criterio de 2016 y puede estar perdiendo dinero en dos mil clientes sin saberlo.', 'Rótulo de Leandro', 'rotulo_02_leandro_chamorro'],
   ],
   todo: [
    ['Alex', 'Tono serio y cercano; pausa de 1 s después de “nueve días”. Leer del teleprompter bajo el lente.'],
    ['Leandro', 'Énfasis en “consumo masivo” y “sin saberlo”. Quedarse quieto 2 s al final.'],
    ['Edición', 'Rótulo desde el segundo 1 de cada toma, mínimo 6 s. No cortar a láminas antes de 10 s de plano continuo de cada persona.'],
    ['Revisión', 'Todas las cifras salen del Capítulo 7 del caso.'],
   ] },
 { t: 'ESCENA 3 — Solución propuesta', time: '1:16 – 2:24 (68 s)', obj: 'Visión general, beneficios por grupo de interés, diferenciadores clave, innovaciones y resultados esperados con métricas (24.2-3).',
   who: 'Patricio Henríquez (Implantación y Gestión del Cambio) y Maximiliano Miño (Calidad).',
   shots: [
    ['1:16–1:31', 'EN CÁMARA Patricio. OBJETO: recibe la guía por la izquierda; en “aunque no haya señal” la cambia por el TERMINAL con la app y al final lo entrega por la derecha.', 'Hola, soy Patricio Henríquez, líder de implantación. Nuestra visión: que cada caja de Puelche cuente su historia, desde el andén del proveedor hasta la firma del almacenero, aunque no haya señal.', 'Rótulo de Patricio', 'rotulo_03_patricio_henriquez'],
    ['1:31–1:44', 'LÁMINA de beneficios.', 'El almacenero ve el stock y sabe cuándo le llega. El conductor trabaja con una mano y sin señal. Calidad ubica un lote en minutos. Y finanzas conoce el costo real de servir.', '4 grupos de interés', '03_E3_beneficios'],
    ['1:44–1:56', 'LÁMINA de diferenciadores.', '¿Qué nos distingue? Funciona sin señal, la bodega no se detiene si cae internet, la trazabilidad usa estándares GS1 y EPCIS, y el costo se mide por entrega, no por zona.', '4 diferenciadores', '03_E3_diferenciadores'],
    ['1:56–2:10', 'LÁMINA de innovaciones.', 'Cinco innovaciones: seguimiento del vencimiento en el local, reproducción de incidentes de terreno, vida útil del lote según su historia térmica, pago variable ligado al costo de servir y hoja de negocio del almacenero.', 'INN-01 a INN-05 (T-19)', '03_E3_innovaciones'],
    ['2:10–2:24', 'EN CÁMARA Maximiliano. OBJETO: recibe el terminal en la mano desde la izquierda, lo sostiene bajo y al final lo entrega por la derecha. Tras 10 s entra la capa lateral de resultados.', 'Hola, soy Maximiliano Miño, líder de calidad. Cada resultado será medible: OTIF sobre noventa y cinco por ciento, cero guías perdidas y trazabilidad completa del lote. Lo verificaremos en cada hito.', 'Rótulo + metas', 'rotulo_04_maximiliano_mino · 03_E3_resultados_lateral'],
   ],
   todo: [
    ['Patricio / Maximiliano', 'Patricio con tono inspirador; Maximiliano firme, mirando al lente en “lo verificaremos”.'],
    ['Edición', 'El rótulo y la capa lateral no deben estar al mismo tiempo: el rótulo sale antes de que entre la capa lateral.'],
    ['Revisión', 'Innovaciones = T-19 vigente (SD13, 09-11-2026); metas iguales al Subdocumento 3 / T-12.'],
   ] },
 { t: 'ESCENA 4 — Propuesta tecnológica', time: '2:24 – 3:47 (83 s)', obj: 'Conjunto tecnológico completo, arquitectura de alto nivel, servicios de nube, seguridad y cumplimiento normativo (24.2-4).',
   who: 'Bastián Trejo (Arquitecto), Tomás Pérez (Desarrollo), Guillermo Castillo (Operación/SRE) y Álvaro Catalán (Seguridad).',
   shots: [
    ['2:24–2:40', 'EN CÁMARA Bastián. OBJETO: recibe el terminal desde la izquierda; al final lo baja fuera de cuadro.', 'Hola, soy Bastián Trejo, arquitecto de solución. Diseñamos una arquitectura híbrida: la bodega opera en un núcleo local en Talca, con borde en Concepción y en los cross-docking, y la nube AWS aporta escala, analítica y respaldo.', 'Rótulo de Bastián', 'rotulo_05_bastian_trejo'],
    ['2:40–2:55', 'DIAGRAMA en 3 pasos (5 s cada uno): usuarios → nube → on-premise.', 'La bodega y su base de datos viven en Talca, porque una bodega no puede detenerse si se corta internet. En la nube AWS: entrada protegida, servicios administrados, Aurora PostgreSQL, sensores de frío y respaldos inmutables.', 'Arquitectura de alto nivel', '04_E4_arquitectura_paso1/2/3'],
    ['2:55–3:05', 'LÁMINA del stack.', 'El stack: Android nativo en terminales Zebra, Laravel sobre PostgreSQL y Aurora, Keycloak, mensajería con RabbitMQ y SQS, y observabilidad con OpenTelemetry.', 'Stack por capas', '04_E4_stack_tecnologico'],
    ['3:05–3:19', 'EN CÁMARA Tomás. OBJETO: recibe el terminal, muestra 1 s la pantalla de la app a la altura del pecho y al final lo entrega por la derecha.', 'Hola, soy Tomás Pérez, líder de desarrollo. La aplicación del preventista y del conductor funciona sin señal: registra el pedido, la entrega y el lote, y sincroniza sola cuando vuelve la cobertura.', 'Rótulo de Tomás', 'rotulo_06_tomas_perez'],
    ['3:19–3:33', 'EN CÁMARA Guillermo. OBJETO: recibe el terminal desde la izquierda y al final lo entrega por la derecha.', 'Hola, soy Guillermo Castillo, líder de operación. Entre las cinco y media y las siete salen noventa y seis camiones. Esa ventana está protegida: autonomía local, respaldo en la nube y monitoreo continuo.', 'Rótulo de Guillermo', 'rotulo_07_guillermo_castillo'],
    ['3:33–3:47', 'EN CÁMARA Álvaro. OBJETO: recibe el terminal desde la izquierda y lo guarda bajo el brazo. Tras 10 s entra la capa lateral de normas.', 'Hola, soy Álvaro Catalán, encargado de seguridad. Aplicamos un modelo Zero Trust, alineado con ISO/IEC 27001 y con la Ley 21.719 de protección de datos personales. Cada acceso se verifica, cada dato viaja cifrado.', 'Rótulo + normas', 'rotulo_08_alvaro_catalan · 04_E4_seguridad_lateral'],
   ],
   todo: [
    ['Bastián', 'Hablar despacio. Puede grabar también la voz del diagrama y del stack.'],
    ['Tomás / Guillermo / Álvaro', 'Ritmo seguro; mismo encuadre que el resto (marca en el piso).'],
    ['Edición', 'Los 3 pasos del diagrama se encadenan con fundido de 0,5 s, así parece que la arquitectura se construye.'],
    ['Revisión', 'Todo lo nombrado está en el SD4 vigente (09-11-2026): Laravel 13/PHP 8.5, no Django. Kafka y EKS están descartados: no se nombran.'],
   ] },
 { t: 'ESCENA 5 — Ventajas competitivas', time: '3:47 – 4:28 (41 s)', obj: 'Por qué LafroX, experiencia específica, casos de éxito, garantías y compromisos, y valor agregado único (24.2-5).',
   who: 'Mosaico del equipo + Alex Aravena en cámara (segunda aparición, con rótulo).',
   shots: [
    ['3:47–3:59', 'MOSAICO: las tomas de 3 s de cada integrante van bajo las ventanas transparentes.', '¿Por qué LafroX? Porque partimos del andén, la ruta y el almacén, no de la tecnología. Ocho especialistas que cubren cada rol clave, con certificaciones PMP, AWS, CISSP y Kubernetes.', 'Nombre, cargo, años, especialidad y certificación de los 8', '05_E5_mosaico_equipo'],
    ['3:59–4:13', 'LÁMINA de casos de éxito (los 3 casos del sitio web y del T-6).', 'Desde 2012 operamos sistemas como este: el reparto híbrido de LogiNacional, con veintidós mil entregas diarias; la cadena de frío de FarmaRed a veintidós bajo cero; y la preventa sin conexión de Lácteos del Sur.', 'LogiNacional · FarmaRed · Lácteos del Sur', '05_E5_casos_exito'],
    ['4:13–4:28', 'EN CÁMARA Alex (2.ª vez), con rótulo otra vez. OBJETO: recibe el terminal desde la izquierda y lo conserva. Tras 10 s entra la capa de compromisos.', 'Nos comprometemos con los cincuenta y seis meses completos, un despliegue híbrido sin dependencia de un proveedor y niveles de servicio medibles en cada hito. Nuestro valor único: trazabilidad donde ocurre la operación, incluso sin señal.', 'Rótulo + compromisos', 'rotulo_01_alex_aravena · 05_E5_compromisos_lateral'],
   ],
   todo: [
    ['Equipo completo', 'El día de grabación, cada uno graba 3 s mirando a cámara sin hablar, para el mosaico.'],
    ['Edición', 'Las cifras de los casos deben ser idénticas a las del sitio web y el T-6; si cambian allá, se regenera la lámina.'],
    ['Revisión', 'Todo debe poder probarse con el Formulario T-8 y coincidir con el sitio web (Cap. 23).'],
   ] },
 { t: 'ESCENA 6 — Cierre y compromiso', time: '4:28 – 4:47 (19 s)', obj: 'Compromiso, datos de contacto e identidad corporativa final (24.2-6).',
   who: 'Plano grupal de los 8 integrantes (con rótulos) + voz de Alex.',
   shots: [
    ['4:28–4:38', 'PLANO GRUPAL de los 8, mismo fondo, con la capa de rótulos del grupo. Alex, al centro, sostiene el terminal a la altura de la cintura.', 'En LafroX asumimos este proyecto como propio. Porque con nosotros, donde se pierde la señal, no se pierde el dato.', 'Rótulos de los 8', '06_E6_rotulos_plano_grupal'],
    ['4:38–4:47', 'PLACA FINAL. Se mantiene hasta el último cuadro (sin fundido a negro, para que el logo no desaparezca).', '(La música baja hasta silencio)', 'Logo, «Donde se pierde la señal, no se pierde el dato.», lafrox.github.io, contacto@lafrox.cl, +56 32 250 4100', '06_E6_placa_final'],
   ],
   todo: [
    ['Equipo completo', 'Dos filas, de pie, con la misma ropa que en las tomas individuales.'],
    ['Edición', 'Duración final 4:47. Comprobar con ffprobe que no pasa de 300 s.'],
    ['Revisión', 'Contacto igual al del sitio declarado en el T-12 (lafrox.github.io).'],
   ] },
];

// ======================= AUDITORÍA =======================
const audit = [
 ['Numeral', 'Qué exige la base', 'Dónde se cumple', 'Estado'],
 ['24.1', 'Duración ≤ 300 s', 'Guion de 287 s (4:47) · control con ffprobe', 'Cumple'],
 ['24.1', 'Full HD 1920×1080, horizontal', 'Todas las piezas en 1920×1080 · exportación', 'Cumple'],
 ['24.1', 'MP4 H.264, ≥ 30 fps, ≥ 5 Mbps, ≤ 500 MB', 'Parámetros de exportación (sección 2)', 'Cumple'],
 ['24.1', 'Audio ≥ 44,1 kHz/16 bit AAC o MP3, normalizado', 'AAC 48 kHz, −16 LUFS', 'Cumple'],
 ['24.1', 'Música opcional con licencia', 'Sin música o con licencia guardada', 'Cumple'],
 ['24.1', 'Iluminación profesional, fondo neutro o corporativo, transiciones suaves', 'Normas de grabación y edición', 'Cumple'],
 ['24.2-1', 'Logotipo animado', 'E1 0:00–0:04: MP4 con el isotipo OFICIAL del sitio web', 'Corregido v04'],
 ['24.2-1', 'Nombre del proyecto', 'Placa de título y locución E1', 'Corregido v03'],
 ['24.2-1', 'Nombre del caso y del proponente', 'Placa de título E1', 'Cumple'],
 ['24.2-1', 'Fecha de la propuesta', 'Placa de título E1: falta el dato real', 'Pendiente equipo'],
 ['24.2-2', 'Análisis de la problemática actual', 'E2: Alex + láminas de cifras', 'Cumple'],
 ['24.2-2', 'Impacto en las personas afectadas', 'E2: lámina de personas afectadas', 'Corregido v03'],
 ['24.2-2', 'Riesgos de no implementar', 'E2: Leandro (decidir a ciegas)', 'Cumple'],
 ['24.2-2', 'Métricas del problema', 'E2: 41 %, $31 M, 82,4 %, 7,8 %', 'Cumple'],
 ['24.2-2', 'Comprensión del sector', 'E2: consumo masivo, cadena de frío, efectivo, competencia', 'Corregido v03'],
 ['24.2-3', 'Visión general', 'E3: Patricio', 'Cumple'],
 ['24.2-3', 'Beneficios para cada grupo de interés', 'E3: lámina de beneficios', 'Cumple'],
 ['24.2-3', 'Diferenciadores clave', 'E3: lámina de diferenciadores', 'Corregido v03'],
 ['24.2-3', 'Innovaciones incluidas', 'E3: INN-01 a INN-05 del T-19 vigente', 'Corregido v04'],
 ['24.2-3', 'Resultados esperados con métricas', 'E3: Maximiliano + capa de metas', 'Cumple'],
 ['24.2-4', 'Conjunto tecnológico completo', 'E4: stack vigente (Laravel 13/PHP 8.5, no Django)', 'Corregido v04'],
 ['24.2-4', 'Arquitectura de alto nivel', 'E4: diagrama en 3 pasos', 'Cumple'],
 ['24.2-4', 'Servicios de nube utilizados', 'E4: diagrama y stack (AWS)', 'Cumple'],
 ['24.2-4', 'Seguridad y cumplimiento normativo', 'E4: Álvaro + capa de normas', 'Cumple'],
 ['24.2-5', 'Por qué el proponente es la mejor opción', 'E5: mosaico + locución', 'Cumple'],
 ['24.2-5', 'Experiencia específica', 'E5: trayectoria desde 2012 (sitio web y SD1)', 'Corregido v04'],
 ['24.2-5', 'Casos de éxito relevantes', 'E5: LogiNacional, FarmaRed y Lácteos del Sur (sitio web y T-6)', 'Corregido v04'],
 ['24.2-5', 'Garantías y compromisos', 'E5: Alex + capa de compromisos', 'Cumple'],
 ['24.2-5', 'Valor agregado único', 'E5: “trazabilidad donde ocurre la operación”', 'Cumple'],
 ['24.2-6', 'Compromiso, contacto e identidad final', 'E6: plano grupal + placa final', 'Cumple'],
 ['24.2', 'Segmentos en el orden indicado', 'E1 → E6 sin intercalar', 'Cumple'],
 ['RT-24.01', '8 integrantes solos, plano medio, a cámara, ≥ 10 s', 'Cada uno 13–15 s y se presenta con su nombre', 'Cumple'],
 ['RT-24.02', 'Rótulo completo CADA VEZ que aparece un integrante', 'Rótulos individuales + mosaico + plano grupal + 2.ª aparición de Alex', 'Corregido v03'],
 ['RT-24.02', 'Años de experiencia en el rótulo', 'Campo “[__] años” en todas las piezas', 'Pendiente equipo'],
 ['RT-24.03', 'Certificaciones (deseable)', 'CSV del equipo y sitio web se contradicen en 6 de 8 personas', 'Pendiente equipo'],
 ['RT-24.04', 'Mismo fondo, iluminación y encuadre', 'Día único de grabación, mismo set', 'Cumple'],
 ['RT-24.05', 'Logo en todas las escenas; contacto en encabezado o pie', 'Logo OFICIAL en la capa de marca desde 0:04; placa final sin fundido a negro', 'Corregido v04'],
 ['RT-24.05', 'Datos de contacto reales', 'lafrox.github.io · contacto@lafrox.cl · +56 32 250 4100 (sitio y T-12)', 'Corregido v04'],
 ['RT-24.06', 'Volumen normalizado y misma calidad de grabación', 'Mismo micrófono, −16 LUFS', 'Cumple'],
 ['24.4', 'Causales de descuento y descalificación', 'Tabla de control (sección 2.3)', 'Cumple'],
 ['24.5', 'USB, respaldo, enlace ≥ 60 días, contraseña aparte, derechos', 'Checklist de entrega (sección 8)', 'Cumple'],
 ['Tabla de entregables', 'Video entregado “con la propuesta final”', 'Cronograma de producción', 'Cumple'],
];

const kit = [
 ['Archivo', 'Uso en el video', 'Pista'],
 ['video/E1_logo_animado.mp4', 'E1 · 0:00–0:04', 'V1'],
 ['png/00_capa_marca_permanente.png', 'Todo el video desde 0:04 hasta el final (logo, encabezado, pie de contacto)', 'V3 (arriba de todo)'],
 ['png/01_E1_placa_titulo.png', 'E1 · 0:04–0:14', 'V1'],
 ['png/02_E2_cifra_1_lote … cifra_4_competencia.png', 'E2 · 0:29–0:49 (5 s cada una)', 'V1'],
 ['png/02_E2_personas_afectadas.png', 'E2 · 0:49–1:00', 'V1'],
 ['png/03_E3_beneficios.png', 'E3 · 1:31–1:44', 'V1'],
 ['png/03_E3_diferenciadores.png', 'E3 · 1:44–1:56', 'V1'],
 ['png/03_E3_innovaciones.png', 'E3 · 1:56–2:10', 'V1'],
 ['png/03_E3_resultados_lateral.png', 'E3 · sobre Maximiliano, desde 2:21', 'V2'],
 ['png/04_E4_arquitectura_paso1/2/3.png', 'E4 · 2:40–2:55 (5 s cada paso)', 'V1'],
 ['png/04_E4_stack_tecnologico.png', 'E4 · 2:55–3:05', 'V1'],
 ['png/04_E4_seguridad_lateral.png', 'E4 · sobre Álvaro, desde 3:44', 'V2'],
 ['png/05_E5_mosaico_equipo.png', 'E5 · 3:47–3:59 (las tomas van debajo, en V1)', 'V2'],
 ['png/05_E5_casos_exito.png', 'E5 · 3:59–4:13', 'V1'],
 ['png/05_E5_compromisos_lateral.png', 'E5 · sobre Alex, desde 4:24', 'V2'],
 ['png/06_E6_rotulos_plano_grupal.png', 'E6 · 4:28–4:38 sobre el plano grupal', 'V2'],
 ['png/06_E6_placa_final.png', 'E6 · 4:38–4:47', 'V1'],
 ['png/rotulo_01 … rotulo_08_*.png', 'Sobre cada integrante, desde el segundo 1 y por lo menos 6 s', 'V2'],
 ['logo/oficial/lafrox-isotipo.svg y logo/*.png', 'Isotipo oficial y logotipo horizontal (fondo claro u oscuro)', '—'],
 ['fuente/*.py', 'Generadores: editar textos y volver a crear las piezas', '—'],
];

const team = [
 ['Integrante', 'Cargo', 'Crítico', 'Escena', 'Seg.', 'Especialización · certificaciones'],
 ['Alex Aravena', 'Jefe de Proyecto', 'Sí', '2, 5, 6', '14 + 16', 'Dirección de proyectos TI · PMP, CSM'],
 ['Leandro Chamorro', 'Líder de Datos', 'Sí', '2', '15', 'Analítica y costo de servir · CKAD'],
 ['Patricio Henríquez', 'Líder de Implantación y Gestión del Cambio', 'No', '3', '13', 'Adopción en terreno · [__]'],
 ['Maximiliano Miño', 'Líder de Calidad', 'Sí', '3', '13', 'Aseguramiento de calidad · [__]'],
 ['Bastián Trejo', 'Arquitecto de Solución', 'Sí', '4', '15', 'Arquitectura híbrida · AWS SA Professional'],
 ['Tomás Pérez', 'Líder de Desarrollo', 'No', '4', '13', 'Desarrollo móvil offline-first · CKAD'],
 ['Guillermo Castillo', 'Líder de Operación / SRE', 'Sí', '4', '13', 'Alta disponibilidad y continuidad · [__]'],
 ['Álvaro Catalán', 'Encargado de Seguridad de la Información', 'Sí', '4', '13', 'Zero Trust y cumplimiento · CISSP, CEH'],
];

const C = [];
// Portada
C.push(
  new Paragraph({ spacing: { before: 1800, after: 300 }, alignment: AlignmentType.CENTER,
    children: [new ImageRun({ type: 'png', data: fs.readFileSync(path.join(VIS, 'logo', 'logo_lafrox_fondo_claro.png')), transformation: { width: 450, height: 90 } })] }),
  new Paragraph({ heading: HeadingLevel.TITLE, alignment: AlignmentType.CENTER, children: [r('Guía de producción y kit visual del video de presentación')] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [r('Licitación TFEP-01/2026 · Caso 02 — Logística · Distribuidora Puelche S.A.', { size: 26 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [r('Capítulo 24 de las Bases Técnicas Transversales (RT-24.01 a RT-24.06)', { size: 22, color: '555555' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 500 }, children: [r('Duración del guion: 4:47 (287 s) · Máximo permitido: 5:00', { bold: true, size: 24 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, children: [r('Versión v07 · Noviembre 2026 · El guion para leer está en Guion_Video_LafroX_v07.docx', { size: 22, color: '555555' })] }),
  brk(),
  new Paragraph({ spacing: { after: 160 }, children: [r('Índice', { bold: true, size: 34, color: NEGRO })] }),
  new TableOfContents('Índice', { hyperlink: true, headingStyleRange: '1-2' }),
  brk(),
);

// 1. Auditoría
C.push(h1('1. Auditoría de cumplimiento del Capítulo 24'),
  p('Revisión punto por punto del guion contra el texto de las Bases Técnicas Transversales (Capítulo 24, numerales 24.1 a 24.5, y la tabla de entregables del Título VII). La v03 corrigió las brechas de contenido; la v04 alinea el video con el sitio oficial y los documentos vigentes del 9-11-2026 (logo, contacto, stack, innovaciones y casos de éxito). Lo que queda en rojo depende de datos que solo el equipo puede aportar. El detalle de las 67 verificaciones está en Checklist_Video_LafroX.'),
  table([1200, 3200, 3638, 1600], audit, NEGRO, 3),
  gap(),
  h2('1.1 Brechas que tenía la versión anterior'),
  b([r('Rótulos incompletos (RT-24.02). ', { bold: true }), r('La base exige el rótulo “cada vez que aparezca un integrante”. El mosaico, el plano grupal y la segunda aparición de Alex no lo tenían. Ahora sí.')]),
  b([r('Logo ausente al final (RT-24.05). ', { bold: true }), r('El cierre terminaba con un fundido a negro y el logo desaparecía. Ahora la placa final se mantiene hasta el último cuadro.')]),
  b([r('Contenido de 24.2 sin cubrir. ', { bold: true }), r('Faltaban el nombre del proyecto, el impacto en las personas, la comprensión del sector, los diferenciadores clave y el conjunto tecnológico completo. Se agregaron láminas y locución para cada uno.')]),
  b([r('Logo animado. ', { bold: true }), r('Ahora existe como archivo MP4 listo para usar.')]),
  h2('1.2 Riesgos que el equipo debe resolver'),
  warn('Certificaciones (RT-24.03): el CSV del equipo y el sitio web se contradicen en 6 de 8 personas (por ejemplo, Álvaro: CISSP/CEH en el CSV y AWS SA Professional en el sitio). Mostrar una certificación no acreditada es información falsa. El T-8 debe fijar una sola versión y el sitio debe coincidir.'),
  warn('Cargos distintos entre documentos: en la Presentación 1 (GitHub) los roles son otros. Por ejemplo, Patricio aparece en “Ciberseguridad, QA e Infraestructura” y Guillermo en “Desarrollo Frontend y Movilidad”. Este guion usa los roles de AGENTS.md. El video debe coincidir exactamente con el Formulario T-8.'),
  warn('Sitio web (Cap. 23): el video muestra lafrox.github.io, el sitio declarado en el T-12. Debe estar activo durante todo el proceso (RT-23.06) y sus casos de éxito y currículos deben coincidir con el video. No usar www.lafrox.cl (solo aparece en la Presentación 1).'),
);

// 2. Buenas prácticas + requisitos
C.push(brk(), h1('2. Buenas prácticas y requisitos técnicos'),
  h2('2.1 Buenas prácticas aplicadas'),
  b([r('Problema del cliente antes que la empresa: ', { bold: true }), r('la Escena 1 dura 15 s y la Escena 2 abre con el retiro sanitario.')]),
  b([r('Estructura problema → solución → llamado a la acción, ', { bold: true }), r('que coincide con el orden obligatorio de 24.2.')]),
  b([r('Una idea por pantalla, ', { bold: true }), r('con cifras grandes y al menos 3 s de lectura.')]),
  b([r('Autenticidad: ', { bold: true }), r('personas reales del equipo y solo afirmaciones respaldadas por la propuesta.')]),
  b([r('Alternar cámara y láminas ', { bold: true }), r('para evitar el exceso de “cabeza parlante”, respetando los 10 s continuos de cada integrante.')]),
  b([r('Frente a cámara: ', { bold: true }), r('ensayar, hablar a 2,6–2,8 palabras por segundo, mirar al lente (lo exige RT-24.01) y usar teleprompter.')]),
  b([r('Imagen: ', { bold: true }), r('iluminación de tres puntos, exposición y balance de blancos en manual, cámara en trípode a la altura de los ojos.')]),
  b([r('Audio: ', { bold: true }), r('importa más que la imagen. Usar el mismo corbatero para todos, hacer una prueba de 15 s en la sala real y normalizar a −16 LUFS.')]),
  b([r('Edición: ', { bold: true }), r('solo fundidos de 0,5 s y una única plantilla gráfica.')]),
  h2('2.2 Especificaciones técnicas (24.1)'),
  table([2600, 3000, 4038], [
    ['Aspecto', 'Mínimo de las bases', 'Lo que configuramos'],
    ['Duración', '≤ 300 s', '287 s'],
    ['Resolución', '1920 × 1080, horizontal', '1920 × 1080, 16:9'],
    ['Formato', 'MP4 · H.264', 'MP4 · H.264 High Profile'],
    ['Cuadros por segundo', '≥ 30 fps', '30 fps constantes'],
    ['Tasa de bits', '≥ 5 Mbps', '12 Mbps (≈ 420 MB)'],
    ['Peso', '≤ 500 MB', '≈ 420–440 MB'],
    ['Audio', '≥ 44,1 kHz · 16 bit · AAC/MP3', 'AAC 48 kHz · 192 kbps · −16 LUFS'],
    ['Música', 'Opcional, con licencia', 'Con licencia guardada o sin música'],
  ]),
  gap(),
  h2('2.3 Descuentos y descalificación (24.4)'),
  table([4200, 1800, 3638], [
    ['Situación', 'Efecto', 'Cómo lo evitamos'],
    ['Duración > 5 minutos', 'Descalificación', 'Guion de 287 s y control con ffprobe'],
    ['Falta un integrante del equipo clave', 'Descalificación', 'Aparecen los 8'],
    ['Calidad inferior a 24.1', 'Descalificación', 'Parámetros de exportación'],
    ['Información falsa o engañosa', 'Descalificación', 'Cifras con fuente; cruce con T-8, T-11, T-12, T-19'],
    ['Material sin licencia', 'Descalificación', 'Logo oficial de la empresa; gráficos propios; Archivo e IBM Plex Mono (OFL)'],
    ['No entregar el video', 'Descalificación', 'Checklist de entrega'],
    ['Audio, iluminación, transiciones, claridad, rol no crítico', '−5 puntos c/u', 'Normas de grabación y edición'],
  ]),
);

// 3. Identidad + equipo
C.push(brk(), h1('3. Identidad visual y equipo'),
  h2('3.1 Logotipo LafroX'),
  p('El logo oficial está en el sitio web de la empresa (repositorio lafrox/lafrox.github.io, archivo img/lafrox-isotipo.svg, incorporado el 09-10-2026): un isotipo de zorro naranja. El logotipo del video replica el encabezado del sitio: isotipo + “LAFROX” en Archivo 900 + “INGENIERÍA LOGÍSTICA” en IBM Plex Mono. El isotipo se usa sin modificar.'),
  img('previews/../logo/logo_preview.jpg', 520),
  kv('Archivos', 'logo/oficial/lafrox-isotipo.svg (original), logo/logo_lafrox_fondo_oscuro.png, logo/logo_lafrox_fondo_claro.png, logo/isotipo_lafrox.png.'),
  kv('Paleta (css del sitio)', 'negro #0B0D12, panel #14181F, naranja #FF5A2C, naranja oscuro #C2410C, isotipo #E8641B, amarillo #FFC20E, texto suave #CBD2DC.'),
  kv('Tipografía', 'Archivo (títulos y texto) e IBM Plex Mono (rótulos técnicos), igual que el sitio. Ambas con licencia SIL OFL 1.1, incluidas en fuente/fonts.'),
  kv('Slogan único', '“Donde se pierde la señal, no se pierde el dato.” Resume la promesa de la propuesta: la operación sigue registrando pedidos, entregas, lotes y temperaturas aunque no haya conectividad (offline-first + trazabilidad). Reemplaza a las dos frases anteriores (Presentación 1 y sitio web).'),
  warn('Para mantener la coherencia (Rúbrica V5), conviene usar el mismo slogan en el sitio web, la portada de la propuesta y la presentación.'),
  h2('3.2 Quién aparece, dónde y cuánto'),
  table([1500, 2000, 800, 900, 900, 3538], team),
  gap(),
  warn('Completar “[__] años” en fuente/generar_visuales.py (lista EQUIPO) y volver a ejecutar el generador. Los datos deben coincidir con el Formulario T-8.'),
  h2('3.3 Set de grabación'),
  b('Fondo: pared gris carbón o roll-up negro con el logo naranja, igual para los 8.'),
  b('Vestimenta: gris, blanco o azul oscuro; sin ropa totalmente negra (se pierde en el fondo) ni prendas naranjas grandes.'),
  b('Iluminación de tres puntos con LED de 5600 K, sin luz de ventana; balance de blancos manual.'),
  b('Trípode a la altura de los ojos; plano medio; marcas en el piso; un solo corbatero para todos.'),
);

// 4. Guion
C.push(brk(), h1('4. Dinámica del objeto: de la guía de papel al terminal'),
  p('Para hacer el video más dinámico, un objeto pasa de mano en mano y cuenta la historia del caso: en el problema pasa una guía de despacho en papel arrugada (lo que hoy se pierde en Puelche); Patricio la cambia por un terminal con la app LafroX (la solución), y el terminal viaja por los líderes técnicos hasta Alex y termina al centro del plano grupal, justo cuando suena el slogan. El detalle completo está en Guion_Dinamica_Objeto_v01 y su revisión frente a las Bases en Dinamica_vs_Bases_v01 (ningún requisito incumplido, 9 condiciones).'),
  h2('4.1 Reglas que no se pueden romper'),
  b('Cada toma tiene a una sola persona; del que entrega solo puede verse la mano (RT-24.01).'),
  b('Primero se recibe (≈ 1 s), después se mira al lente y se habla. Los 10 s y el rótulo cuentan desde que mira a cámara.'),
  b('El objeto sale de cuadro por la DERECHA y entra en la toma siguiente por la IZQUIERDA; se recibe sin moverse de la marca del piso (RT-24.04).'),
  b('El objeto va bajo (pecho o cintura) y nunca tapa la cara ni la zona del rótulo, abajo a la izquierda (RT-24.02).'),
  b('Solo el papel se lanza, y suave. El terminal se entrega siempre en la mano.'),
  b('Cada paso se monta con un fundido de 0,3–0,5 s sobre el movimiento; nada de cortes secos ni efectos (24.1 y descuento por transiciones bruscas).'),
  b('El papel se arruga antes de hablar y hay 1 s de silencio entre recibir y hablar (RT-24.06).'),
  b('Guía inventada (logo LafroX o genérico, sin datos reales) y terminal con la marca del fabricante tapada, mostrando una pantalla del prototipo (RT-24.05 y 24.4).'),
  b('No agregar más contenido: con la dinámica el video dura 4:47 (287 s).'),
  h2('4.2 Recorrido del objeto'),
  table([2600, 2200, 4838], [
    ['Toma', 'Objeto', 'Acción'],
    ['Alex (E2)', 'Guía de papel', 'La tiene en la mano; al final la arruga y la lanza por la derecha'],
    ['Leandro (E2)', 'Guía de papel', 'La atrapa por la izquierda; al final la pasa por la derecha'],
    ['Patricio (E3)', 'Papel → terminal', 'Recibe la guía y la cambia por el terminal; lo entrega por la derecha'],
    ['Maximiliano (E3)', 'Terminal', 'Lo recibe en la mano y lo entrega por la derecha'],
    ['Bastián, Tomás, Guillermo, Álvaro (E4)', 'Terminal', 'Izquierda → derecha en cada toma; Álvaro lo guarda bajo el brazo'],
    ['Alex (E5)', 'Terminal', 'Lo recibe y lo conserva'],
    ['Plano grupal (E6)', 'Terminal', 'Alex al centro, a la altura de la cintura'],
  ]),
);

C.push(brk(), h1('5. Guion escena por escena'),
  p('Para cada escena: objetivo, quién aparece, tabla de tomas (tiempo, qué se ve, locución exacta, texto en pantalla y pieza del kit visual) y tareas por responsable. EN CÁMARA significa que la persona habla al lente en plano continuo.'));
scenes.forEach((s, i) => {
  if (i > 0) C.push(brk());
  C.push(h2(s.t),
    new Paragraph({ spacing: { after: 100 }, shading: { type: ShadingType.CLEAR, fill: GREY },
      children: [r('Tiempo: ', { bold: true }), r(s.time + '    '), r('Quién aparece: ', { bold: true }), r(s.who)] }),
    p([r('Objetivo: ', { bold: true }), r(s.obj)]),
    h3('Tomas y locución'),
    table([950, 2000, 3500, 1500, 1688], [['Tiempo', 'Qué se ve / qué se hace', 'Locución (texto exacto)', 'En pantalla', 'Pieza del kit'], ...s.shots]),
    gap(), h3('Qué debe hacer cada responsable'),
    table([2300, 7338], [['Responsable', 'Tarea'], ...s.todo], NAR_OSC), gap());
});

// 5. Kit visual
const prev = n => 'previews/' + n + '.jpg';
C.push(brk(), h1('6. Kit visual del video'),
  p('Todas las piezas están en productos/Video/visuales/. Las láminas de fondo completo van en la pista V1. Las capas transparentes (rótulos y paneles laterales) van en V2. La capa de marca permanente va en V3, arriba de todo, desde 0:04 hasta el final. Las miniaturas muestran cómo se ve cada pieza con la capa de marca encima (sobre una silueta gris que representa la toma de cámara).'),
  h2('6.1 Lista de archivos y dónde se usan'),
  table([3700, 4338, 1600], kit),
  gap(),
  h2('6.2 Vista previa'),
  gallery([
    [prev('E1_logo_animado'), 'E1 · logo animado (último cuadro)'], [prev('01_E1_placa_titulo'), 'E1 · placa de título'],
    [prev('02_E2_cifra_1_lote'), 'E2 · cifra 1'], [prev('02_E2_cifra_2_perdida'), 'E2 · cifra 2'],
    [prev('02_E2_cifra_3_otif'), 'E2 · cifra 3'], [prev('02_E2_cifra_4_competencia'), 'E2 · cifra 4'],
    [prev('02_E2_personas_afectadas'), 'E2 · personas afectadas'], [prev('rotulo_01_alex_aravena'), 'Rótulo individual (ejemplo)'],
    [prev('03_E3_beneficios'), 'E3 · beneficios'], [prev('03_E3_diferenciadores'), 'E3 · diferenciadores'],
    [prev('03_E3_innovaciones'), 'E3 · innovaciones'], [prev('03_E3_resultados_lateral'), 'E3 · capa de resultados'],
    [prev('04_E4_arquitectura_paso1'), 'E4 · arquitectura paso 1'], [prev('04_E4_arquitectura_paso2'), 'E4 · arquitectura paso 2'],
    [prev('04_E4_arquitectura_paso3'), 'E4 · arquitectura paso 3'], [prev('04_E4_stack_tecnologico'), 'E4 · stack tecnológico'],
    [prev('04_E4_seguridad_lateral'), 'E4 · capa de seguridad'], [prev('05_E5_mosaico_equipo'), 'E5 · mosaico del equipo'],
    [prev('05_E5_casos_exito'), 'E5 · casos de éxito'], [prev('05_E5_compromisos_lateral'), 'E5 · capa de compromisos'], [prev('06_E6_rotulos_plano_grupal'), 'E6 · rótulos del plano grupal'],
    [prev('06_E6_placa_final'), 'E6 · placa final'], [prev('00_capa_marca_permanente'), 'Capa de marca permanente'],
  ]),
  h2('6.3 Cómo modificar las piezas'),
  b('Editar la sección CONFIGURACIÓN de fuente/generar_visuales.py: fecha, nombre del proyecto, slogan, años de experiencia y certificaciones de cada integrante.'),
  b('Ejecutar: python generar_visuales.py (necesita Chrome o Edge; las tipografías están en fuente/fonts).'),
  b('Para regenerar solo algunas piezas: python generar_visuales.py rotulo (genera solo las que contienen “rotulo” en el nombre).'),
  b('La animación del logo se regenera con python logo_animado.py (necesita ffmpeg).'),
);

// 6. Tiempos y plan
C.push(brk(), h1('7. Tiempos y plan de producción'),
  table([2600, 1300, 1300, 1300, 3138], [
    ['Escena', 'Inicio', 'Fin', 'Duración', 'Personas (s en cámara)'],
    ['1 Introducción', '0:00', '0:14', '14 s', '—'],
    ['2 Problema', '0:14', '1:16', '62 s', 'Alex 15 · Leandro 16'],
    ['3 Solución', '1:16', '2:24', '68 s', 'Patricio 15 · Maximiliano 14'],
    ['4 Tecnología', '2:24', '3:47', '83 s', 'Bastián 16 · Tomás 14 · Guillermo 14 · Álvaro 14'],
    ['5 Ventajas', '3:47', '4:28', '41 s', 'Mosaico 12 · casos 14 · Alex 15'],
    ['6 Cierre', '4:28', '4:47', '19 s', 'Grupo 10'],
    ['Total', '', '', '287 s', '8 de 8 integrantes'],
  ]),
  gap(),
  h2('7.1 Día de grabación'),
  table([1300, 5500, 2838], [
    ['Hora', 'Actividad', 'Responsable'],
    ['00:00', 'Armar set, luces, trípode, marcas en el piso, balance de blancos', 'Guillermo Castillo'],
    ['00:30', 'Prueba de 15 s de audio e imagen; 10 s de silencio de sala', 'Guillermo Castillo'],
    ['00:45', 'Tomas individuales en orden del guion (3 tomas buenas por persona)', 'Todos; dirige Alex'],
    ['02:00', 'Tomas de 3 s mirando a cámara, para el mosaico', 'Todos'],
    ['02:15', 'Plano grupal y locuciones en off', 'Todos'],
    ['02:30', 'B-roll propio: tablet, guantes, documentos, equipo trabajando', 'Patricio Henríquez'],
  ]),
  gap(),
  h2('7.2 Cronograma'),
  table([1300, 5500, 2838], [
    ['Día', 'Actividad', 'Responsable'],
    ['D-10', 'Definir en el T-8 años y certificaciones; fijar fecha, nombre del proyecto y slogan; regenerar piezas', 'Alex Aravena'],
    ['D-7', 'Revisar el kit visual y ajustar textos', 'Bastián Trejo'],
    ['D-6', 'Ensayo con cronómetro', 'Todo el equipo'],
    ['D-5', 'Día de grabación único', 'Guillermo Castillo'],
    ['D-4', 'Edición con el kit visual y normalización de audio', '[responsable de edición]'],
    ['D-3', 'Revisión cruzada con T-8, T-11, T-12, T-19 y el sitio web', 'Maximiliano Miño'],
    ['D-2', 'Exportación, ffprobe, respaldo y enlace', 'Guillermo Castillo'],
    ['D-1', 'Prueba de USB y enlace en otro equipo', 'Alex Aravena'],
  ]),
);

// 7. Checklists
C.push(brk(), h1('8. Listas de verificación'),
  h2('8.1 Antes de exportar'),
  ...['Los 6 segmentos están en el orden de 24.2.', 'Los 8 integrantes aparecen ≥ 10 s en plano continuo.',
    'Hay rótulo completo cada vez que aparece un integrante (incluye mosaico, plano grupal y segunda aparición de Alex).',
    'El logo es visible en todas las escenas, también en el último cuadro.', 'Fecha y años reales (no quedan “[__]”); certificaciones según el T-8.',
    'Cifras, metas, servicios y cargos coinciden con T-8, T-11, T-12, T-19 y el sitio web.', 'No hay material sin licencia; solo fundidos.'].map(chk),
  h2('8.2 Exportación y control técnico'),
  new Paragraph({ shading: { type: ShadingType.CLEAR, fill: GREY }, spacing: { after: 100 }, children: [r('ffmpeg -i master.mov -c:v libx264 -profile:v high -pix_fmt yuv420p -r 30 -b:v 12M -maxrate 14M -bufsize 24M -c:a aac -ar 48000 -b:a 192k -af loudnorm=I=-16:TP=-1:LRA=11 -movflags +faststart LAFROX_Video_TFEP-01-2026_Caso02.mp4', { font: 'Consolas', size: 17 })] }),
  new Paragraph({ shading: { type: ShadingType.CLEAR, fill: GREY }, spacing: { after: 100 }, children: [r('ffprobe -v error -show_entries format=duration,size,bit_rate:stream=codec_name,width,height,r_frame_rate,sample_rate -of default=nw=1 LAFROX_Video_TFEP-01-2026_Caso02.mp4', { font: 'Consolas', size: 17 })] }),
  h2('8.3 Entrega (24.5)'),
  ...['USB etiquetada: “LafroX SpA — Propuesta TFEP-01/2026 — Caso 02 Logística Distribuidora Puelche”.',
    'En la USB: video, copia de respaldo, carpeta de licencias y captura del ffprobe.',
    'Enlace sin límite de descargas y con vigencia de al menos 60 días (configurar 90).',
    'Contraseña del enlace en un documento separado.', 'Declaración de derechos y autorización de proyección.',
    'Video entregado junto con la propuesta final.'].map(chk),
);

// 8. Fuentes
const src = [
  ['Bases Técnicas Transversales, Título VII y Capítulos 23–24 (repositorio LafroX)', null],
  ['Bases Administrativas, Art. 28° y criterio “Capacidad de equipo”', null],
  ['Caso 02 — Logística, Capítulos 5 y 7', null],
  ['Registro de Decisiones de Arquitectura (ADR) y Arquitectura de Seguridad de la propuesta', null],
  ['Presentación 1 LafroX (GitHub, Productos/Presentacion_1_LafroX.pdf): slogan', null],
  ['Sitio oficial lafrox.github.io (repositorio lafrox/lafrox.github.io): logo, paleta, tipografía, contacto, equipo y casos de éxito', null],
  ['Subdocumento 4 (stack, 09-11-2026), Formulario T-19 (SD13, 09-11-2026), Formulario T-12 (SD3) y T-6 (SD1)', null],
  ['Better Proposals — The right way to use videos in your proposals', 'https://betterproposals.io/blog/the-right-way-to-use-videos-in-your-proposals/'],
  ['Teleprompter.com — How to make a pitch video that stands out', 'https://www.teleprompter.com/blog/how-to-make-a-pitch-video-that-stands-out'],
  ['MV Marketing — Corporate video production tips', 'https://mv-marketing.pages.dev/blog/corporate-video-production-tips'],
  ['Bonomotion — How to create effective corporate videos', 'https://bonomotion.com/how-to-create-effective-corporate-videos/'],
  ['Vidpros — Talking head video setup: essential guide', 'https://vidpros.com/talking-head-video-setup-essential-guide/'],
  ['Universidad de Toronto — Lighting, audio and camera settings for talking head video', 'https://edtech.engineering.utoronto.ca/how-lighting-audio-camera-settings-impact-talking-head-video-quality/'],
  ['University of Waterloo — Shooting video tips', 'https://uwaterloo.ca/keep-learning/sites/default/files/uploads/documents/shooting_video_tips_final.pdf'],
  ['Clipchamp — Ideas y ejemplos de videos corporativos', 'https://clipchamp.com/es/blog/corporate-video-ideas-examples/'],
  ['Prezi — Consejos de presentación', 'https://prezi.com/es/learn/presenter-tips/'],
];
C.push(h1('9. Fuentes'), ...src.map(([t, u]) => b(u ? [new ExternalHyperlink({ link: u, children: [r(t, { style: 'Hyperlink' })] })] : [r(t)])));

// 9. Guion por personaje (formato de lectura)
const ROT = {
  'ALEX': 'ALEX ARAVENA · Jefe de Proyecto · [__] años de experiencia · Dirección de proyectos TI · PMP, CSM',
  'LEANDRO': 'LEANDRO CHAMORRO · Líder de Datos · [__] años de experiencia · Modelo de datos y costo de servir · CKAD',
  'PATRICIO': 'PATRICIO HENRÍQUEZ · Líder de Implantación y Gestión del Cambio · [__] años de experiencia · Adopción en terreno y capacitación',
  'MAXIMILIANO': 'MAXIMILIANO MIÑO · Líder de Calidad · [__] años de experiencia · Aseguramiento de calidad y pruebas',
  'BASTIÁN': 'BASTIÁN TREJO · Arquitecto de Solución · [__] años de experiencia · Arquitectura híbrida e integración · AWS Solutions Architect – Professional',
  'TOMÁS': 'TOMÁS PÉREZ · Líder de Desarrollo · [__] años de experiencia · Laravel y móvil Kotlin offline-first · CKAD',
  'GUILLERMO': 'GUILLERMO CASTILLO · Líder de Operación / SRE · [__] años de experiencia · Alta disponibilidad, NOC y niveles de servicio',
  'ÁLVARO': 'ÁLVARO CATALÁN · Encargado de Seguridad de la Información · [__] años de experiencia · Seguridad Zero Trust y cumplimiento · CISSP, CEH',
};
const EXTRA = {
  '03_E3_resultados_lateral': 'a los 10 s entra a la derecha el panel “Resultados esperados”: OTIF 82,4 % → > 95 % · Fill rate 91,3 % → > 97 % · Guías perdidas 1,1 % → 0 · Reentregas 4,2 % → < 1 %',
  '04_E4_seguridad_lateral': 'a los 10 s entra a la derecha el panel “Seguridad y cumplimiento”: Zero Trust · ISO/IEC 27001:2022 · Ley 21.719 · Ley 19.799 · Cifrado en reposo y en tránsito',
  '05_E5_compromisos_lateral': 'a los 10 s entra a la derecha el panel “Garantías y compromisos”: 56 meses · Híbrido nube + on-premise · Sin dependencia de un proveedor · SLA por hito · ISO 9001 · ISO/IEC 20000-1 · CMMI-DEV 3',
};
const MODE = process.argv[4] || 'guia';   // 'solo' = solo el guion; 'guia' = documento explicativo
const T = [
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [r('GUION — VIDEO DE PRESENTACIÓN LAFROX', { bold: true, size: 32, color: NEGRO })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 }, children: [r('Licitación TFEP-01/2026 · Caso 02 — Logística · Distribuidora Puelche S.A. · Duración 4:47', { size: 20, color: '777777' })] }),
];
scenes.forEach(s => {
  T.push(new Paragraph({ spacing: { before: 200, after: 80 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: NAR, space: 2 } },
    children: [r(s.t.toUpperCase() + '   ', { bold: true, size: 22, color: NEGRO }), r(s.time, { size: 18, color: '777777' })] }));
  s.shots.forEach(sh => {
    const m = sh[1].match(/EN CÁMARA ([A-Za-zÁÉÍÓÚáéíóúÑñ]+)/);
    const who = m ? m[1].toUpperCase() : null;
    const silent = sh[2].startsWith('(');
    const speaker = who ? who : (silent ? 'SIN VOZ' : (sh[4].includes('04_E4') ? 'VOZ EN OFF (BASTIÁN)' : 'VOZ EN OFF (ALEX)'));
    const texto = sh[2].replace(/^Versión B: /, '');
    let pantalla;
    if (who) {
      pantalla = 'Plano medio de ' + (who.charAt(0) + who.slice(1).toLowerCase()) + ' mirando a cámara. Rótulo: «' + ROT[who] + '»';
      const ex = Object.keys(EXTRA).find(k => sh[4].includes(k)); if (ex) pantalla += '; ' + EXTRA[ex];
    } else {
      pantalla = sh[1].replace(/\.$/, '') + ' — ' + sh[3];
    }
    T.push(new Paragraph({ spacing: { before: 100, after: 20 }, keepNext: true, children: [
      r(sh[0] + '   ', { size: 17, color: '888888' }),
      r(speaker + ': ', { bold: true, color: who ? NAR_OSC : NEGRO, size: 22 }),
      r(silent ? '' : texto, { size: 22 }) ] }));
    const objm = sh[1].includes('OBJETO: ') ? [null, sh[1].split('OBJETO: ')[1].split('. Tras')[0].replace(/\.$/, '')] : null;
    if (who && objm) T.push(new Paragraph({ indent: { left: 900 }, spacing: { after: 20 }, keepNext: true, children: [
      r('[' + objm[1] + ']', { bold: true, size: 18, color: NAR_OSC }) ] }));
    T.push(new Paragraph({ indent: { left: 900 }, spacing: { after: 80 }, children: [
      r('(PANTALLA: ' + pantalla + ')', { italics: true, size: 18, color: '555555' }) ] }));
  });
});

const doc = new Document({
  creator: 'LafroX SpA', title: MODE === 'solo' ? 'Guion — Video LafroX' : 'Guía de producción del video — Caso 02 (v07)',
  styles: {
    default: { document: { run: { font: 'Calibri', size: 21 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: 'Calibri', size: 48, bold: true, color: NEGRO }, paragraph: { spacing: { before: 0, after: 240 }, keepNext: true } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', run: { font: 'Calibri', size: 34, bold: true, color: NEGRO }, paragraph: { spacing: { before: 240, after: 160 }, keepNext: true, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', run: { font: 'Calibri', size: 27, bold: true, color: NAR_OSC }, paragraph: { spacing: { before: 220, after: 100 }, keepNext: true, outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', run: { font: 'Calibri', size: 23, bold: true, color: NAR }, paragraph: { spacing: { before: 160, after: 80 }, keepNext: true, outlineLevel: 2 } },
    ],
  },
  numbering: { config: [
    { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] },
    { reference: 'chk', levels: [{ level: 0, format: LevelFormat.BULLET, text: '☐', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 300 } } } }] },
  ] },
  sections: [{
    properties: { page: { margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [r('LafroX SpA · Video de presentación · TFEP-01/2026 Caso 02', { size: 16, color: '777777' })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [r('Página ', { size: 16, color: '777777' }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '777777' })] })] }) },
    children: MODE === 'solo' ? T : C,
  }],
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(out, buf); console.log('ok', out); });
