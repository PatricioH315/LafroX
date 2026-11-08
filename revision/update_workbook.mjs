// Actualiza la evidencia del prototipo sin convertir metadatos de ruta en pruebas.
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';

const require = createRequire(import.meta.url);
const runtime = process.env.LFX_NODE_MODULES ? createRequire(path.join(process.env.LFX_NODE_MODULES, '_loader.cjs')) : require;
const { FileBlob, SpreadsheetFile } = await import(pathToFileURL(runtime.resolve('@oai/artifact-tool')).href);
const JSZip = runtime('jszip');
const file = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../docs/cumplimiento_requerimientos_y_arquitectura.xlsx');
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(file));
const previewDir = process.env.LFX_PREVIEW_DIR || os.tmpdir();
const preview = async (sheetName, range, name) => {
  const image = await wb.render({ sheetName, range, scale: 1, format: 'png' });
  await fs.writeFile(path.join(previewDir, name), new Uint8Array(await image.arrayBuffer()));
};
if (process.argv.includes('--inspect')) {
  console.log((await wb.inspect({ kind: 'workbook,sheet,table', maxChars: 2200, tableMaxRows: 2 })).ndjson);
  await preview('Requerimientos', 'A1:E7', 'lafrox-workbook-before.png');
} else {
  const publicURL = 'https://patricioh315.github.io/LafroX/';
  const samples = {
    '/analitica/:kpi': '/analitica/otif',
    '/analitica/:kpi/ruta/:id': '/analitica/otif/ruta/R-01',
    '/clientes/:id': '/clientes/CL-10021',
    '/pedidos/:id': '/pedidos/PV-264821',
    '/rutas/:id': '/rutas/R-01',
    '/calidad/lotes/:id': '/calidad/lotes/L2611-21',
    '/devoluciones/:id': '/devoluciones/DV-5530'
  };
  const resolveURLs = (value) => String(value || '').replace(/index\.html#(\/[^\s]*)/g, (_, route) => publicURL + '#' + (samples[route] || route));
  const status = (value) => value === 'Sí' ? 'Ruta identificada' : value;
  for (const spec of [
    { name: 'Requerimientos', n: 293, status: 'D', evidence: 'E' },
    { name: 'Arquitectura lógica', n: 21, status: 'C', evidence: 'D' }
  ]) {
    const { name, n, status: col, evidence } = spec, sheet = wb.worksheets.getItem(name);
    sheet.getRange(col + '1:' + evidence + '1').values = [['Evidencia', 'Ruta de ejemplo o referencia']];
    sheet.getRange(col + '1:' + col + n).format.columnWidth = 21;
    sheet.getRange(evidence + '1:' + evidence + n).format.columnWidth = 62;
    const rows = sheet.getRange('A2:' + evidence + n).values;
    const i = col === 'D' ? 3 : 2;
    if (col === 'D' && !rows.some((r) => r[0] === 'RT-25.04')) throw new Error('No se localizó RT-25.04');
    sheet.getRange(col + '2:' + evidence + n).values = rows.map((row) => {
      if (row[0] === 'RT-25.04') return ['Probado en Edge', 'revision/verify.cjs · 52 rutas × 5 tamaños; no certifica otros navegadores.'];
      if (row[0] === 'RT-25.03') return ['Parcial', 'Pruebas dirigidas de teclado y semántica. Falta WCAG automatizada + manual y lector.'];
      return [status(row[i]), resolveURLs(row[i + 1])];
    });
    if (col === 'D') {
      const cells = sheet.getRange('D2:D293');
      cells.conditionalFormats.deleteAll();
      cells.format.fill = '#FFFFFF';
      cells.conditionalFormats.addCustom('=$D2="Ruta identificada"', { fill: '#E8F0F8' });
      cells.conditionalFormats.addCustom('=$D2="Documental"', { fill: '#FEF3C7' });
      cells.conditionalFormats.addCustom('=$D2="Probado en Edge"', { fill: '#D6F5DD' });
    }
  }
  wb.worksheets.getItem('Notas').getRange('A1:A5').values = [
    ['Ruta identificada: localiza una pantalla de demostración; no certifica cumplimiento funcional ni aceptación.'],
    ['Las rutas apuntan a ' + publicURL + ' y usan IDs de ejemplo. Algunas requieren ingresar con un perfil autorizado.'],
    ['La hoja incluye RF, RNF, reglas de negocio y RT-25.01–25.10. Ver docs/trazabilidad.md.'],
    ['Solo la capa de presentación se materializa en la demo. Las capas restantes se describen en SD4.'],
    ['Documental: se revisa en la propuesta. No demostrable: requiere pruebas o entorno real. Ver revision/verify.cjs para las pruebas de la demo.']
  ];
  wb.recalculate();
  console.log((await wb.inspect({ kind: 'table', range: 'Requerimientos!A1:E3', include: 'values,formulas' })).ndjson);
  console.log((await wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!', options: { useRegex: true, maxResults: 20 } })).ndjson);
  await preview('Requerimientos', 'A1:E7', 'lafrox-workbook-after.png');
  await preview('Arquitectura lógica', 'A1:D5', 'lafrox-workbook-architecture.png');
  await preview('Notas', 'A1:A5', 'lafrox-workbook-notes.png');
  const original = await JSZip.loadAsync(await fs.readFile(file));
  const workDir = await fs.mkdtemp(path.join(previewDir, 'lafrox-xlsx-'));
  const temporary = path.join(workDir, 'export.xlsx');
  let zip;
  try {
    await (await SpreadsheetFile.exportXlsx(wb)).save(temporary);
    zip = await JSZip.loadAsync(await fs.readFile(temporary));
  } finally {
    await fs.rm(temporary, { force: true });
    await fs.rm(temporary + '.inspect.ndjson', { force: true });
    await fs.rmdir(workDir);
  }
  // La exportación del runtime no conserva los autofiltros. Restaurar solo los metadatos
  // nativos del original (sin editar datos ni estilos fuera de Artifact Tool).
  for (const entry of ['xl/worksheets/sheet1.xml', 'xl/worksheets/sheet2.xml']) {
    const source = await original.file(entry).async('string');
    const filter = source.match(/<(?:\w+:)?autoFilter\b[^>]*\/>/)?.[0];
    let target = await zip.file(entry).async('string');
    const prefix = target.match(/<([\w]+:)?worksheet\b/)[1] || '';
    if (filter && !/<(?:\w+:)?autoFilter\b/.test(target)) target = target.replace(`</${prefix}sheetData>`, `</${prefix}sheetData>` + filter.replace('<autoFilter', '<' + prefix + 'autoFilter'));
    zip.file(entry, target);
  }
  const workbook = 'xl/workbook.xml';
  const originalXML = await original.file(workbook).async('string');
  let xml = await zip.file(workbook).async('string');
  const prefix = xml.match(/<([\w]+:)?workbook\b/)[1] || '';
  const names = originalXML.match(/<definedNames>[\s\S]*?<\/definedNames>/)?.[0];
  if (names && !/<(?:\w+:)?definedNames\b/.test(xml)) xml = xml.replace(`</${prefix}sheets>`, `</${prefix}sheets>` + names.replace(/<(\/?)(definedNames?)/g, '<$1' + prefix + '$2'));
  zip.file(workbook, xml);
  await fs.writeFile(file, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
}
