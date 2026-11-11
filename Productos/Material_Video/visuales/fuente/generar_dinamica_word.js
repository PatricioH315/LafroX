// Genera dos Word sobre la dinámica "De la guía de papel al terminal":
//   1) Guion_Dinamica_Objeto_v01.docx  -> escena por escena
//   2) Dinamica_vs_Bases_v01.docx      -> comparación con las exigencias de las Bases (Cap. 24)
// Uso: node generar_dinamica_word.js <carpeta_salida>
const fs = require('fs'), path = require('path');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, HeadingLevel,
  AlignmentType, LevelFormat, BorderStyle, Footer, Header, PageNumber, PageOrientation, TableOfContents } = require('docx');

const OUTDIR = process.argv[2];
const NEGRO = '0B0D12', NAR = 'FF5A2C', NAR_OSC = 'C2410C', GREY = 'F2F2F2';
const WPS = 2.7, CATCH = 1;   // palabras/segundo; segundos para recibir el objeto
const r = (t, o = {}) => new TextRun({ text: t, ...o });
const p = (t, o = {}) => new Paragraph({ spacing: { after: 100 }, ...o, children: Array.isArray(t) ? t : [r(t)] });
const h1 = (t, pb = false) => new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: pb, children: [r(t)] });
const h2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [r(t)] });
const h3 = t => new Paragraph({ heading: HeadingLevel.HEADING_3, children: [r(t)] });
const b = t => new Paragraph({ numbering: { reference: 'bul', level: 0 }, spacing: { after: 60 }, children: Array.isArray(t) ? t : [r(t)] });
const n = t => new Paragraph({ numbering: { reference: 'num', level: 0 }, spacing: { after: 60 }, children: Array.isArray(t) ? t : [r(t)] });
const warn = t => new Paragraph({ spacing: { before: 60, after: 120 }, shading: { type: ShadingType.CLEAR, fill: 'FFF1E6' },
  children: [r('⚠ ', { bold: true, color: NAR_OSC }), r(t)] });
const cb = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
const borders = { top: cb, bottom: cb, left: cb, right: cb };
const COL = { 'Cumple': 'DFF2E3', 'Cumple con condición': 'FFF0D6', 'Riesgo': 'FBDADA', 'Mejora': 'DDEBFF', 'Sin efecto': 'EEEEEE',
  'Bajo': 'DFF2E3', 'Medio': 'FFF0D6', 'Alto': 'FBDADA', 'OK': 'DFF2E3', 'AJUSTADO': 'FFF0D6' };
function table(widths, rows, colorCols = [], head = NEGRO) {
  return new Table({ width: { size: widths.reduce((a, c) => a + c, 0), type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((row, i) => new TableRow({ tableHeader: i === 0, cantSplit: true,
      children: row.map((c, j) => {
        let fill = i === 0 ? head : (i % 2 === 0 ? 'FAFAFA' : undefined);
        if (i > 0 && colorCols.includes(j) && COL[c]) fill = COL[c];
        return new TableCell({ width: { size: widths[j], type: WidthType.DXA }, borders,
          margins: { top: 40, bottom: 40, left: 80, right: 80 }, shading: fill ? { type: ShadingType.CLEAR, fill } : undefined,
          children: String(c).split('|').map(line => new Paragraph({ spacing: { after: 20 },
            children: [r(line, i === 0 ? { bold: true, color: 'FFFFFF', size: 17 } : { size: 17, bold: colorCols.includes(j) })] })) });
      }) })) });
}
const sec = (s) => (s < 0 ? '-' : '') + Math.floor(Math.abs(s) / 60) + ':' + String(Math.abs(s) % 60).padStart(2, '0');
const words = t => t.split(/\s+/).filter(Boolean).length;

// ===================== DATOS: ESCENAS CON LA DINÁMICA =====================
// tipo: 'cam' (persona en cámara), 'lam' (lámina con voz en off), 'mud' (sin voz)
// objeto: { recibe, entrega } ; dur en segundos
const E = [
 { t: 'ESCENA 1 — Introducción corporativa', obj: 'Sin objeto. Se presenta la marca.', shots: [
  { tipo: 'mud', quien: '—', dur: 4, accion: 'Animación del logo oficial (E1_logo_animado.mp4).', loc: '', pant: 'Isotipo del zorro + LAFROX + “Ingeniería logística”', pieza: 'E1_logo_animado.mp4' },
  { tipo: 'lam', quien: 'VOZ EN OFF (ALEX)', dur: 10, accion: 'Placa de título. Desde aquí entra la capa de marca permanente.', loc: 'LafroX SpA presenta su propuesta técnico-económica para el Caso 02, Logística: una plataforma de trazabilidad, promesa de entrega y costo de servir para Distribuidora Puelche.', pant: 'Proyecto · Caso · Licitación · Proponente · Fecha', pieza: '01_E1_placa_titulo' },
 ] },
 { t: 'ESCENA 2 — Comprensión del problema', obj: 'Entra la GUÍA DE PAPEL arrugada: es el problema (guías que se pierden, 12 días para encontrarlas).', shots: [
  { tipo: 'cam', quien: 'ALEX', dur: 15, yaTiene: true, recibe: 'Saca la guía de papel del bolsillo / la tiene en la mano al empezar', entrega: 'Al terminar, la arruga y la lanza suave fuera de cuadro por la DERECHA', accion: 'Mira la guía, levanta la vista al lente y habla. Termina arrugándola.', loc: 'Hola, soy Alex Aravena, jefe de proyecto de LafroX. En marzo de 2026, un proveedor pidió a Puelche saber, ese mismo día, a qué clientes llegó un lote de queso. Tardó nueve días… y fue una estimación.', pant: 'Rótulo de Alex (tras 1 s)', pieza: 'rotulo_01_alex_aravena' },
  { tipo: 'lam', quien: 'VOZ EN OFF (ALEX)', dur: 20, accion: 'Cuatro láminas de cifras, 5 s cada una, con fundido.', loc: 'Cuarenta y uno por ciento de las recepciones no registraban el lote. Treinta y un millones de pesos perdidos y seis meses fuera de un proveedor clave. El OTIF es de ochenta y dos por ciento y una guía perdida tarda doce días en aparecer. Y un competidor ya entrega en veinticuatro horas.', pant: '41 % · $31 millones · 82,4 % · 7,8 %', pieza: '02_E2_cifra_1…4' },
  { tipo: 'lam', quien: 'VOZ EN OFF (ALEX)', dur: 11, accion: 'Lámina de personas afectadas.', loc: 'Detrás de cada cifra hay personas: la jefa de calidad buscando en carpetas, el preparador a veintidós bajo cero, el conductor rindiendo efectivo sin respaldo, el almacenero esperando.', pant: 'Impacto en las personas', pieza: '02_E2_personas_afectadas' },
  { tipo: 'cam', quien: 'LEANDRO', dur: 16, recibe: 'La guía arrugada ENTRA por la IZQUIERDA y la atrapa a la altura del pecho', entrega: 'Al terminar, la pasa con la mano fuera de cuadro por la DERECHA', accion: 'Atrapa, la mira con desconfianza, levanta la vista al lente y habla.', loc: 'Hola, soy Leandro Chamorro, líder de datos. En consumo masivo, el margen se juega en el costo de servir. Puelche lo calcula con un criterio de 2016 y puede estar perdiendo dinero en dos mil clientes sin saberlo.', pant: 'Rótulo de Leandro (tras recibir)', pieza: 'rotulo_02_leandro_chamorro' },
 ] },
 { t: 'ESCENA 3 — Solución propuesta', obj: 'EL CAMBIO: Patricio recibe la guía de papel y la cambia por el TERMINAL. Desde aquí viaja el terminal.', shots: [
  { tipo: 'cam', quien: 'PATRICIO', dur: 15, recibe: 'La guía ENTRA por la IZQUIERDA (de mano, no lanzada)', entrega: 'En las últimas palabras deja la guía fuera de cuadro abajo y levanta el TERMINAL con la app; al terminar lo saca por la DERECHA', accion: 'Recibe la guía, habla al lente; en “aunque no haya señal” cambia el papel por el terminal.', loc: 'Hola, soy Patricio Henríquez, líder de implantación. Nuestra visión: que cada caja de Puelche cuente su historia, desde el andén del proveedor hasta la firma del almacenero, aunque no haya señal.', pant: 'Rótulo de Patricio; al final, terminal con pantalla de la app LafroX', pieza: 'rotulo_03_patricio_henriquez' },
  { tipo: 'lam', quien: 'VOZ EN OFF (ALEX)', dur: 13, accion: 'Lámina de beneficios.', loc: 'El almacenero ve el stock y sabe cuándo le llega. El conductor trabaja con una mano y sin señal. Calidad ubica un lote en minutos. Y finanzas conoce el costo real de servir.', pant: '4 grupos de interés', pieza: '03_E3_beneficios' },
  { tipo: 'lam', quien: 'VOZ EN OFF (ALEX)', dur: 12, accion: 'Lámina de diferenciadores.', loc: '¿Qué nos distingue? Funciona sin señal, la bodega no se detiene si cae internet, la trazabilidad usa estándares GS1 y EPCIS, y el costo se mide por entrega, no por zona.', pant: '4 diferenciadores', pieza: '03_E3_diferenciadores' },
  { tipo: 'lam', quien: 'VOZ EN OFF (ALEX)', dur: 14, accion: 'Lámina de innovaciones.', loc: 'Cinco innovaciones: seguimiento del vencimiento en el local, reproducción de incidentes de terreno, vida útil del lote según su historia térmica, pago variable ligado al costo de servir y hoja de negocio del almacenero.', pant: 'INN-01 a INN-05 (T-19)', pieza: '03_E3_innovaciones' },
  { tipo: 'cam', quien: 'MAXIMILIANO', dur: 14, recibe: 'El TERMINAL ENTRA por la IZQUIERDA, entregado en la mano', entrega: 'Lo entrega por la DERECHA', accion: 'Recibe el terminal, lo sostiene bajo (cintura), mira al lente y habla. A los 10 s entra el panel de resultados.', loc: 'Hola, soy Maximiliano Miño, líder de calidad. Cada resultado será medible: OTIF sobre noventa y cinco por ciento, cero guías perdidas y trazabilidad completa del lote. Lo verificaremos en cada hito.', pant: 'Rótulo de Maximiliano → panel “Resultados esperados”', pieza: 'rotulo_04_maximiliano_mino · 03_E3_resultados_lateral' },
 ] },
 { t: 'ESCENA 4 — Propuesta tecnológica', obj: 'El TERMINAL pasa por los 4 líderes técnicos: arquitectura, desarrollo, operación y seguridad.', shots: [
  { tipo: 'cam', quien: 'BASTIÁN', dur: 16, recibe: 'Recibe el TERMINAL desde la IZQUIERDA', entrega: 'Lo deja fuera de cuadro abajo (vuelve en la toma de Tomás)', accion: 'Recibe, mira al lente y habla.', loc: 'Hola, soy Bastián Trejo, arquitecto de solución. Diseñamos una arquitectura híbrida: la bodega opera en un núcleo local en Talca, con borde en Concepción y en los cross-docking, y la nube AWS aporta escala, analítica y respaldo.', pant: 'Rótulo de Bastián', pieza: 'rotulo_05_bastian_trejo' },
  { tipo: 'lam', quien: 'VOZ EN OFF (BASTIÁN)', dur: 15, accion: 'Diagrama en 3 pasos (5 s cada uno).', loc: 'La bodega y su base de datos viven en Talca, porque una bodega no puede detenerse si se corta internet. En la nube AWS: entrada protegida, servicios administrados, Aurora PostgreSQL, sensores de frío y respaldos inmutables.', pant: 'Arquitectura de alto nivel', pieza: '04_E4_arquitectura_paso1/2/3' },
  { tipo: 'lam', quien: 'VOZ EN OFF (BASTIÁN)', dur: 10, accion: 'Lámina del stack.', loc: 'El stack: Android nativo en terminales Zebra, Laravel sobre PostgreSQL y Aurora, Keycloak, mensajería con RabbitMQ y SQS, y observabilidad con OpenTelemetry.', pant: 'Stack por capas', pieza: '04_E4_stack_tecnologico' },
  { tipo: 'cam', quien: 'TOMÁS', dur: 14, recibe: 'Recibe el TERMINAL desde la IZQUIERDA y lo muestra un segundo (pantalla de la app sin señal)', entrega: 'Lo entrega por la DERECHA', accion: 'Recibe, muestra la pantalla brevemente a la altura del pecho, mira al lente y habla.', loc: 'Hola, soy Tomás Pérez, líder de desarrollo. La aplicación del preventista y del conductor funciona sin señal: registra el pedido, la entrega y el lote, y sincroniza sola cuando vuelve la cobertura.', pant: 'Rótulo de Tomás', pieza: 'rotulo_06_tomas_perez' },
  { tipo: 'cam', quien: 'GUILLERMO', dur: 14, recibe: 'Recibe el TERMINAL desde la IZQUIERDA', entrega: 'Lo entrega por la DERECHA', accion: 'Recibe, mira al lente y habla.', loc: 'Hola, soy Guillermo Castillo, líder de operación. Entre las cinco y media y las siete salen noventa y seis camiones. Esa ventana está protegida: autonomía local, respaldo en la nube y monitoreo continuo.', pant: 'Rótulo de Guillermo', pieza: 'rotulo_07_guillermo_castillo' },
  { tipo: 'cam', quien: 'ÁLVARO', dur: 14, recibe: 'Recibe el TERMINAL desde la IZQUIERDA', entrega: 'Lo guarda bajo el brazo (sale del juego hasta la Escena 5)', accion: 'Recibe, mira al lente y habla. A los 10 s entra el panel de seguridad.', loc: 'Hola, soy Álvaro Catalán, encargado de seguridad. Aplicamos un modelo Zero Trust, alineado con ISO/IEC 27001 y con la Ley 21.719 de protección de datos personales. Cada acceso se verifica, cada dato viaja cifrado.', pant: 'Rótulo de Álvaro → panel “Seguridad y cumplimiento”', pieza: 'rotulo_08_alvaro_catalan · 04_E4_seguridad_lateral' },
 ] },
 { t: 'ESCENA 5 — Ventajas competitivas', obj: 'Alex recibe el TERMINAL: el jefe de proyecto se hace cargo de los compromisos.', shots: [
  { tipo: 'lam', quien: 'VOZ EN OFF (ALEX)', dur: 12, accion: 'Mosaico del equipo (tomas de 3 s de cada uno, sin objeto).', loc: '¿Por qué LafroX? Porque partimos del andén, la ruta y el almacén, no de la tecnología. Ocho especialistas que cubren cada rol clave, con certificaciones PMP, AWS, CISSP y Kubernetes.', pant: 'Mosaico con rótulo completo de los 8', pieza: '05_E5_mosaico_equipo' },
  { tipo: 'lam', quien: 'VOZ EN OFF (ALEX)', dur: 14, accion: 'Lámina de casos de éxito.', loc: 'Desde 2012 operamos sistemas como este: el reparto híbrido de LogiNacional, con veintidós mil entregas diarias; la cadena de frío de FarmaRed a veintidós bajo cero; y la preventa sin conexión de Lácteos del Sur.', pant: 'LogiNacional · FarmaRed · Lácteos del Sur', pieza: '05_E5_casos_exito' },
  { tipo: 'cam', quien: 'ALEX', dur: 15, recibe: 'Recibe el TERMINAL desde la IZQUIERDA', entrega: 'Lo mantiene en la mano para el plano grupal', accion: 'Recibe, mira al lente y habla. A los 10 s entra el panel de compromisos.', loc: 'Nos comprometemos con los cincuenta y seis meses completos, un despliegue híbrido sin dependencia de un proveedor y niveles de servicio medibles en cada hito. Nuestro valor único: trazabilidad donde ocurre la operación, incluso sin señal.', pant: 'Rótulo de Alex (otra vez) → panel “Garantías y compromisos”', pieza: 'rotulo_01_alex_aravena · 05_E5_compromisos_lateral' },
 ] },
 { t: 'ESCENA 6 — Cierre y compromiso', obj: 'Remate: el terminal al centro del grupo; nadie sostiene papel.', shots: [
  { tipo: 'lam', quien: 'VOZ EN OFF (ALEX)', dur: 10, accion: 'PLANO GRUPAL de los 8 en dos filas. Alex, al centro, sostiene el terminal a la altura de la cintura.', loc: 'En LafroX asumimos este proyecto como propio. Porque con nosotros, donde se pierde la señal, no se pierde el dato.', pant: 'Rótulos de los 8', pieza: '06_E6_rotulos_plano_grupal' },
  { tipo: 'mud', quien: '—', dur: 9, accion: 'Placa final hasta el último cuadro (sin fundido a negro).', loc: '', pant: 'Logo, slogan, lafrox.github.io, contacto@lafrox.cl, +56 32 250 4100', pieza: '06_E6_placa_final' },
 ] },
];

// Calcular tiempos
let tcur = 0; const checks = [];
E.forEach(s => { s.ini = tcur; s.shots.forEach(sh => { sh.ini = tcur; sh.fin = tcur + sh.dur; tcur = sh.fin;
  const w = words(sh.loc); const need = w / WPS + (sh.tipo === 'cam' && !sh.yaTiene ? CATCH : 0) + (sh.quien === 'PATRICIO' ? 2 : 0);
  sh.w = w; sh.need = need; sh.ok = need <= sh.dur - 0.3 ? 'OK' : (need <= sh.dur ? 'AJUSTADO' : 'LARGO');
  checks.push(sh); }); s.fin = tcur; });
const TOTAL = tcur;
const largos = checks.filter(c => c.ok === 'LARGO');
if (largos.length) { console.error('Tramos largos:', largos.map(c => sec(c.ini))); process.exit(1); }

// ===================== DOCUMENTO 1 =====================
const W = 14570;
const D1 = [];
D1.push(
  new Paragraph({ spacing: { before: 1000, after: 200 }, alignment: AlignmentType.CENTER, children: [r('LafroX SpA', { bold: true, size: 36, color: NAR })] }),
  new Paragraph({ heading: HeadingLevel.TITLE, alignment: AlignmentType.CENTER, children: [r('Dinámica “De la guía de papel al terminal”')] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [r('Guion escena por escena del video de presentación · Licitación TFEP-01/2026 · Caso 02 — Logística', { size: 24 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 300 }, children: [r(`Duración con la dinámica: ${sec(TOTAL)} (${TOTAL} s) · Máximo permitido: 5:00 · Versión v01 · 11-11-2026`, { bold: true, size: 24 })] }),
  new Paragraph({ spacing: { before: 400, after: 160 }, children: [r('Índice', { bold: true, size: 30, color: NEGRO })] }),
  new TableOfContents('Índice', { hyperlink: true, headingStyleRange: '1-2' }),

  h1('1. La idea', true),
  p('Un objeto pasa de mano en mano entre los integrantes y cuenta la historia del caso sin palabras:'),
  b([r('En el problema (Escena 2) pasa una ', {}), r('guía de despacho en papel, arrugada', { bold: true }), r(': es justo lo que hoy se pierde en Puelche (1,1 % de las guías al mes, 12 días para encontrar una).')]),
  b([r('En la solución (Escena 3), ', {}), r('Patricio cambia el papel por un terminal', { bold: true }), r(' con la app LafroX: la transformación digital en un gesto.')]),
  b([r('Desde ahí ', {}), r('viaja el terminal', { bold: true }), r(' por los líderes técnicos, llega a Alex para los compromisos y termina al centro del plano grupal, justo cuando suena el slogan: “Donde se pierde la señal, no se pierde el dato.”')]),
  h2('1.1 Reglas de la dinámica (para cumplir las Bases)'),
  n([r('Cada persona sigue en su toma individual: ', { bold: true }), r('el objeto sale de cuadro por la DERECHA y entra en la toma siguiente por la IZQUIERDA. Nunca hay dos personas en el mismo plano (salvo el grupal).')]),
  n([r('Primero recibe, después habla: ', { bold: true }), r('se recibe el objeto (≈ 1 s), se mira al lente y recién ahí se habla. Los 10 s mínimos y el rótulo cuentan desde que mira a cámara.')]),
  n([r('Nadie se mueve de su marca: ', { bold: true }), r('se recibe sin dar pasos, para mantener el mismo encuadre (RT-24.04).')]),
  n([r('El objeto va bajo, ', { bold: true }), r('a la altura del pecho o de la cintura, y nunca tapa la cara ni la zona del rótulo (abajo a la izquierda).')]),
  n([r('Solo el papel se lanza, y suave. ', { bold: true }), r('El terminal se entrega siempre en la mano.')]),
  n([r('Paso montado con fundido de 0,3–0,5 s ', { bold: true }), r('sobre el movimiento; nada de cortes secos ni efectos.')]),
  n([r('Utilería sin marcas de terceros: ', { bold: true }), r('la guía es inventada (logo LafroX o genérico) y el terminal muestra la app LafroX con la marca del fabricante tapada.')]),
  h2('1.2 Recorrido del objeto'),
  table([2400, 3200, 4600, 4370], [
    ['Momento', 'Objeto', 'De → a', 'Qué cuenta'],
    ['Escena 2 · Alex', 'Guía de papel', 'Aparece en su mano → sale por la derecha', 'El problema: todo depende del papel'],
    ['Escena 2 · Leandro', 'Guía de papel', 'Entra por la izquierda → sale por la derecha', 'Nadie sabe el costo real'],
    ['Escena 3 · Patricio', 'Papel → TERMINAL', 'Entra la guía → la cambia → sale el terminal', 'La transformación digital'],
    ['Escena 3 · Maximiliano', 'Terminal', 'Izquierda → derecha', 'Resultados medibles'],
    ['Escena 4 · Bastián, Tomás, Guillermo, Álvaro', 'Terminal', 'Izquierda → derecha, en cada toma', 'La tecnología lo sostiene'],
    ['Escena 5 · Alex', 'Terminal', 'Lo recibe y lo conserva', 'El jefe de proyecto se compromete'],
    ['Escena 6 · Grupo', 'Terminal al centro', 'En las manos de Alex', 'Remate con el slogan'],
  ]),
  h2('1.3 Utilería que hay que conseguir'),
  table([3000, 5200, 6370], [
    ['Elemento', 'Cómo debe ser', 'Cuidado'],
    ['Guía de despacho en papel (3–4 copias)', 'Impresa por nosotros: “GUÍA DE DESPACHO N° 000123”, logo genérico o LafroX, sin RUT ni datos reales', 'No copiar el formato de una empresa real; se arruga una por toma'],
    ['Terminal o tablet', 'Tamaño de mano; pantalla con la app LafroX (captura del prototipo) y brillo bajo', 'Tapar el logo del fabricante con cinta negra mate; modo avión para que no suenen notificaciones'],
    ['Persona de apoyo fuera de cuadro', 'Lanza o entrega el objeto desde la izquierda de la cámara', 'Que no entre en cuadro más que su mano'],
  ]),
);

E.forEach((s, si) => {
  D1.push(h1(`${si + 2}. ${s.t}`, true),
    new Paragraph({ spacing: { after: 100 }, shading: { type: ShadingType.CLEAR, fill: GREY },
      children: [r('Tiempo: ', { bold: true }), r(`${sec(s.ini)} – ${sec(s.fin)} (${s.fin - s.ini} s)    `), r('Objeto: ', { bold: true }), r(s.obj)] }),
    table([1050, 1500, 3000, 2500, 4150, 2370], [['Tiempo', 'Quién', 'Objeto: recibe / entrega', 'Qué hace', 'Locución (texto exacto)', 'Pantalla · pieza'],
      ...s.shots.map(sh => [`${sec(sh.ini)}–${sec(sh.fin)}|(${sh.dur} s)`, sh.quien,
        sh.tipo === 'cam' ? `RECIBE: ${sh.recibe}|ENTREGA: ${sh.entrega}` : '—', sh.accion, sh.loc || '(sin locución)', `${sh.pant}|${sh.pieza}`])]),
    p(''));
});

// Tiempos
D1.push(h1('8. Control de tiempos', true),
  p(`Cálculo a ${WPS} palabras por segundo. En las tomas a cámara se suma 1 s para recibir el objeto (y 2 s más en la toma de Patricio para cambiar el papel por el terminal). “AJUSTADO” significa que cabe con menos de 0,3 s de holgura: ensayar ese tramo.`),
  table([1500, 2600, 1300, 1300, 1600, 1600, 4670], [['Tramo', 'Quién', 'Duración', 'Palabras', 'Tiempo necesario', 'Estado', 'Nota'],
    ...checks.map(c => [`${sec(c.ini)}–${sec(c.fin)}`, c.quien, `${c.dur} s`, String(c.w), `${c.need.toFixed(1)} s`, c.ok,
      c.tipo === 'cam' ? (c.yaTiene ? 'Ya tiene la guía en la mano: no recibe' : c.quien === 'PATRICIO' ? 'Incluye 1 s para recibir y 2 s para el cambio' : 'Incluye 1 s para recibir el objeto') : ''])], [5]),
  p(''),
  table([3000, 2000, 2000, 7570], [['Escena', 'Inicio', 'Fin', 'Duración'],
    ...E.map(s => [s.t.split(' — ')[0], sec(s.ini), sec(s.fin), `${s.fin - s.ini} s`]), ['TOTAL', '', '', `${TOTAL} s (${sec(TOTAL)}) — margen de ${300 - TOTAL} s bajo el máximo`]]),
  p(''),
  warn('Para hacer espacio a la dinámica se acortaron 7 s de láminas (placa de título, cifras, diagrama y stack) y se resumieron las locuciones de Leandro y del stack respecto del guion v05. No agregar nada más: el margen bajo los 5:00 es de ' + (300 - TOTAL) + ' s.'),
  h2('8.1 Ensayo y grabación'),
  b('Ensayar los pasos 20 minutos antes de grabar, con la persona de apoyo, sin cámara y luego con cámara.'),
  b('Grabar cada toma completa: recepción + habla + entrega. Mínimo 3 tomas buenas por persona.'),
  b('Si una recepción falla, se repite toda la toma; no se “arregla” en la edición.'),
  b('Grabar además 2 s de cada persona sosteniendo el objeto quieta, por si hace falta un plano de apoyo en la edición.'),
);

// Guion por personaje
D1.push(h1('9. Guion por personaje con la dinámica', true),
  p('PERSONAJE: lo que dice. Entre corchetes, la ACCIÓN con el objeto. Entre paréntesis, lo que aparece en PANTALLA.', { spacing: { after: 160 } }));
E.forEach(s => {
  D1.push(new Paragraph({ spacing: { before: 200, after: 80 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: NAR, space: 2 } },
    children: [r(s.t.toUpperCase() + '   ', { bold: true, size: 22 }), r(`${sec(s.ini)} – ${sec(s.fin)}`, { size: 18, color: '777777' })] }));
  s.shots.forEach(sh => {
    const cam = sh.tipo === 'cam';
    if (cam) D1.push(new Paragraph({ indent: { left: 900 }, spacing: { before: 80, after: 20 }, keepNext: true,
      children: [r(`[${sh.quien} ${sh.recibe.charAt(0).toLowerCase() + sh.recibe.slice(1)}]`, { bold: true, size: 18, color: NAR_OSC })] }));
    D1.push(new Paragraph({ spacing: { before: cam ? 20 : 100, after: 20 }, keepNext: true, children: [
      r(`${sec(sh.ini)}–${sec(sh.fin)}   `, { size: 17, color: '888888' }),
      r((sh.quien === '—' ? 'SIN VOZ' : sh.quien) + ': ', { bold: true, color: cam ? NAR_OSC : NEGRO, size: 22 }),
      r(sh.loc, { size: 22 })] }));
    if (cam) D1.push(new Paragraph({ indent: { left: 900 }, spacing: { after: 20 }, keepNext: true,
      children: [r(`[${sh.entrega}]`, { bold: true, size: 18, color: NAR_OSC })] }));
    D1.push(new Paragraph({ indent: { left: 900 }, spacing: { after: 80 }, children: [r(`(PANTALLA: ${sh.accion.replace(/\.$/, '')} — ${sh.pant})`, { italics: true, size: 18, color: '555555' })] }));
  });
});

// ===================== DOCUMENTO 2: COMPARACIÓN =====================
const CMP = [
 ['Numeral', 'Qué exigen las Bases', 'Cómo afecta la dinámica', 'Riesgo', 'Control obligatorio', 'Veredicto'],
 ['24.1 Duración', 'Máximo 5 minutos (300 s); excederlo descalifica.', `Agrega ≈ 11 s de recepciones; se compensa acortando láminas. Total ${sec(TOTAL)}.`, 'Medio', `No agregar nada más (margen ${300 - TOTAL} s). Medir el master con ffprobe.`, 'Cumple con condición'],
 ['24.1 Resolución, formato, fps, bitrate, peso, audio', 'Full HD, MP4 H.264, ≥ 30 fps, ≥ 5 Mbps, ≤ 500 MB, AAC/MP3 ≥ 44,1 kHz.', 'Ninguno: se exporta igual.', 'Bajo', 'Misma exportación y verificación del guion v05.', 'Sin efecto'],
 ['24.1 Aspectos visuales', 'Iluminación profesional, fondo neutro o corporativo, sin efectos que distraigan del mensaje, transiciones suaves.', 'Un objeto en movimiento puede distraer si es exagerado; la pantalla del terminal puede reflejar luz.', 'Medio', 'Gesto breve (≤ 1 s), objeto bajo, fundido 0,3–0,5 s en cada paso, pantalla con brillo bajo y ángulo sin reflejos.', 'Cumple con condición'],
 ['24.1 Música', 'Opcional, con licencia acreditable.', 'Ninguno.', 'Bajo', '—', 'Sin efecto'],
 ['24.2 Orden de los 6 segmentos', 'Introducción → problema → solución → tecnología → ventajas → cierre.', 'No cambia el orden; el objeto acompaña los segmentos.', 'Bajo', '—', 'Cumple'],
 ['24.2-2 Comprensión del problema', 'Problemática, impacto, riesgos, métricas, sector.', 'La guía de papel muestra el problema real del caso (guías perdidas, 12 días).', 'Bajo', 'Usar una guía inventada, sin datos reales.', 'Mejora'],
 ['24.2-3 Solución propuesta', 'Visión, beneficios, diferenciadores, innovaciones, resultados.', 'El cambio papel → terminal muestra la visión en un gesto.', 'Bajo', 'El terminal debe mostrar una pantalla coherente con el prototipo (Cap. 25).', 'Mejora'],
 ['24.2-4 / 24.2-5 / 24.2-6', 'Tecnología, ventajas y cierre.', 'Contenido intacto; las locuciones de Leandro y del stack se resumieron sin perder datos.', 'Bajo', 'Revisar que el stack resumido siga siendo verdadero (SD4).', 'Cumple'],
 ['RT-24.01 Aparición individual', 'Cada integrante solo, en plano medio, mirando a cámara, presentándose, ≥ 10 s.', 'Al recibir el objeto se mira hacia el lado y puede entrar la mano de otra persona.', 'Alto', 'Cada toma es de una sola persona; el objeto entra solo o con una mano mínima; los 10 s se cuentan DESPUÉS de recibir, mirando al lente.', 'Cumple con condición'],
 ['RT-24.02 Rótulo en cada aparición', 'Nombre, cargo, años de experiencia y especialización cada vez que aparece.', 'El objeto podría tapar el rótulo.', 'Medio', 'Rótulo entra cuando la persona ya mira a cámara; objeto a la derecha o al centro bajo, nunca abajo a la izquierda.', 'Cumple con condición'],
 ['RT-24.03 Certificaciones', 'Pueden mostrarse (deseable).', 'Ninguno.', 'Bajo', '—', 'Sin efecto'],
 ['RT-24.04 Mismo fondo, luz y encuadre', 'Fondo, iluminación y encuadre iguales para todos.', 'Si alguien da un paso para atrapar, cambia el encuadre.', 'Medio', 'Recibir sin moverse de la marca del piso; misma mano y misma dirección en todas las tomas.', 'Cumple con condición'],
 ['RT-24.05 Identidad y logo', 'Paleta, tipografía y marca consistentes; logo en todas las escenas; contacto en encabezado o pie.', 'La capa de marca no cambia; un terminal con logo de fabricante o una guía con marca ajena rompería la identidad.', 'Medio', 'Tapar la marca del fabricante; guía con logo LafroX o genérico; pantalla de la app con colores LafroX.', 'Cumple con condición'],
 ['RT-24.06 Audio homogéneo', 'Volumen normalizado, misma calidad, sin cambios bruscos.', 'El papel arrugado y el roce del terminal hacen ruido; puede tapar la primera palabra.', 'Medio', 'Arrugar el papel antes de hablar; silencio de 1 s entre recibir y hablar; normalizar a −16 LUFS.', 'Cumple con condición'],
 ['24.4 Descuento: transiciones bruscas (−5)', 'Transiciones suaves.', 'Un corte seco en el paso se vería brusco.', 'Medio', 'Fundido corto sobre el movimiento; ensayar la continuidad derecha → izquierda.', 'Cumple con condición'],
 ['24.4 Descuento: información poco clara (−5)', 'El mensaje debe entenderse.', 'Si el gesto es largo, quita atención a lo que se dice.', 'Bajo', 'El objeto queda quieto mientras la persona habla.', 'Cumple'],
 ['24.4 Descalificación: información falsa', 'Nada falso o engañoso.', 'Una guía con datos de una empresa real o una pantalla con funciones inexistentes sería engañosa.', 'Medio', 'Guía inventada; pantalla tomada del prototipo de la propuesta.', 'Cumple con condición'],
 ['24.4 Descalificación: material sin licencia', 'Todo con derechos acreditables.', 'Utilería y diseño propios; la marca del terminal no es material con derechos, pero conviene ocultarla.', 'Bajo', 'Incluir la utilería en las autorizaciones y en la carpeta de licencias.', 'Cumple'],
 ['24.4 Descalificación: equipo incompleto', 'Todo el equipo clave aparece.', 'No cambia: aparecen los 8.', 'Bajo', 'Asistencia completa el día de grabación.', 'Cumple'],
 ['24.5 Entrega y derechos', 'USB + respaldo, enlace ≥ 60 días, contraseña aparte, autorización y garantía de derechos.', 'Ninguno.', 'Bajo', 'Igual que en la checklist del encargado audiovisual.', 'Sin efecto'],
 ['Rúbrica interna V4', 'Producción audiovisual comercial; no un zoom leyendo el PPT.', 'La dinámica hace el video más atractivo y menos “cabeza parlante”.', 'Bajo', '—', 'Mejora'],
 ['Rúbrica interna V5', 'Identidad coherente con informe, PPT, web y T-8.', 'El objeto refuerza la historia del caso sin agregar datos nuevos.', 'Bajo', '—', 'Cumple'],
];
const D2 = [];
const cnt = v => CMP.slice(1).filter(x => x[5] === v).length;
D2.push(
  new Paragraph({ spacing: { before: 1000, after: 200 }, alignment: AlignmentType.CENTER, children: [r('LafroX SpA', { bold: true, size: 36, color: NAR })] }),
  new Paragraph({ heading: HeadingLevel.TITLE, alignment: AlignmentType.CENTER, children: [r('La dinámica del objeto frente a las exigencias de las Bases')] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [r('Capítulo 24 de las Bases Técnicas Transversales (24.1–24.5, RT-24.01–RT-24.06) y rúbrica interna · v01 · 11-11-2026', { size: 22 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 300 }, children: [r(`${CMP.length - 1} requisitos revisados: ${cnt('Cumple')} Cumple · ${cnt('Mejora')} Mejora · ${cnt('Cumple con condición')} Cumple con condición · ${cnt('Sin efecto')} Sin efecto · 0 Incumple`, { bold: true, size: 24 })] }),
  h1('1. Conclusión'),
  p([r('La dinámica es compatible con las Bases, siempre que se respeten 9 condiciones. ', { bold: true }), r('Ningún requisito queda incumplido. Mejora la comprensión del problema y de la solución y responde a la rúbrica interna (V4: producción comercial, no “cabeza parlante”). Los riesgos están en la ejecución, no en la idea: tomas individuales, encuadre fijo, rótulo visible, transiciones suaves y audio limpio.')]),
  h2('1.1 Condiciones obligatorias'),
  n('Cada toma tiene a una sola persona; del otro solo puede verse la mano (RT-24.01).'),
  n('Los 10 s mínimos y el rótulo se cuentan desde que la persona mira al lente, después de recibir (RT-24.01, RT-24.02).'),
  n('Se recibe sin moverse de la marca del piso (RT-24.04).'),
  n('El objeto nunca tapa la cara ni la zona del rótulo (RT-24.02).'),
  n('Cada paso se monta con fundido de 0,3–0,5 s; nada de cortes secos ni efectos (24.1, descuento por transiciones bruscas).'),
  n('El papel se arruga antes de hablar y hay 1 s de silencio entre recibir y hablar (RT-24.06).'),
  n('Guía de papel inventada y terminal sin marca del fabricante, con una pantalla del prototipo (RT-24.05, 24.4 información falsa).'),
  n(`No agregar más contenido: la duración queda en ${sec(TOTAL)} (24.1).`),
  n('Ensayar 20 minutos antes de grabar y repetir completa toda toma con una recepción fallida.'),
  h1('2. Comparación requisito por requisito', true),
  table([1900, 2900, 3000, 900, 3870, 2000], CMP, [3, 5]),
  p(''),
  h1('3. Cambios respecto del guion v05', true),
  table([3600, 5200, 5770], [
    ['Elemento', 'Guion v05', 'Con la dinámica'],
    ['Duración total', '4:43 (283 s)', `${sec(TOTAL)} (${TOTAL} s)`],
    ['Tomas a cámara', '13–15 s', '14–16 s (+1 s para recibir; +2 s en Patricio por el cambio)'],
    ['Placa de título', '11 s', '10 s'],
    ['Láminas de cifras', '22 s', '20 s'],
    ['Diagrama de arquitectura', '18 s', '15 s (5 s por paso)'],
    ['Lámina del stack', '11 s', '10 s, con locución resumida'],
    ['Locución de Leandro', '39 palabras', '38 palabras (“el margen se juega en el costo de servir”)'],
    ['Plano grupal', '9 s', '10 s, con el terminal al centro'],
    ['Kit visual', '29 piezas', 'Sin cambios: se usan las mismas piezas'],
  ]),
  h2('3.1 Qué hay que actualizar si se aprueba'),
  b('Guion v05 → v06 con estos tiempos (las piezas gráficas no cambian).'),
  b('Checklist del encargado audiovisual: agregar la utilería, la persona de apoyo y los 20 minutos de ensayo.'),
  b('Checklist del video: volver a medir la duración final con ffprobe.'),
);

function mkDoc(title, children, header) {
  return new Document({ creator: 'LafroX SpA', title,
    styles: { default: { document: { run: { font: 'Calibri', size: 20 } } },
      paragraphStyles: [
        { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: 'Calibri', size: 46, bold: true, color: NEGRO }, paragraph: { spacing: { before: 0, after: 200 }, keepNext: true } },
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', run: { font: 'Calibri', size: 30, bold: true, color: NEGRO }, paragraph: { spacing: { before: 200, after: 120 }, keepNext: true, outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', run: { font: 'Calibri', size: 24, bold: true, color: NAR_OSC }, paragraph: { spacing: { before: 180, after: 90 }, keepNext: true, outlineLevel: 1 } },
        { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', run: { font: 'Calibri', size: 21, bold: true, color: NAR }, paragraph: { spacing: { before: 140, after: 70 }, keepNext: true, outlineLevel: 2 } },
      ] },
    numbering: { config: [
      { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] },
      { reference: 'num', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 300 } } } }] },
    ] },
    sections: [{ properties: { page: { size: { width: 11906, height: 16838, orientation: PageOrientation.LANDSCAPE }, margin: { top: 1000, bottom: 1000, left: 1134, right: 1134 } } },
      headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [r(header, { size: 16, color: '777777' })] })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [r('Página ', { size: 16, color: '777777' }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '777777' })] })] }) },
      children }] });
}
(async () => {
  fs.writeFileSync(path.join(OUTDIR, 'Guion_Dinamica_Objeto_v01.docx'), await Packer.toBuffer(mkDoc('Guion con dinámica del objeto', D1, 'LafroX SpA · Dinámica del objeto · TFEP-01/2026 Caso 02')));
  fs.writeFileSync(path.join(OUTDIR, 'Dinamica_vs_Bases_v01.docx'), await Packer.toBuffer(mkDoc('Dinámica vs Bases', D2, 'LafroX SpA · Dinámica vs Bases (Cap. 24) · TFEP-01/2026 Caso 02')));
  console.log('ok total', TOTAL, sec(TOTAL), '| ajustados:', checks.filter(c => c.ok === 'AJUSTADO').map(c => sec(c.ini) + ' ' + c.quien).join(', ') || 'ninguno');
})();
