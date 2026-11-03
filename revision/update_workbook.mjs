// Runtime: @oai/artifact-tool (LFX_NODE_MODULES puede apuntar al paquete del host).
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';
const require = createRequire(import.meta.url);
const runtime = process.env.LFX_NODE_MODULES ? createRequire(path.join(process.env.LFX_NODE_MODULES, '_loader.cjs')) : require;
const { FileBlob, SpreadsheetFile } = await import(pathToFileURL(runtime.resolve('@oai/artifact-tool')).href);
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const file = path.join(root, 'docs/cumplimiento_requerimientos_y_arquitectura.xlsx');
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(file));
const previewDir = process.env.LFX_PREVIEW_DIR || os.tmpdir();
console.log((await wb.inspect({kind:'workbook,sheet,table',maxChars:2200,tableMaxRows:2,tableMaxCols:5})).ndjson);
if (process.argv.includes('--inspect')) {
  const blob = await wb.render({sheetName:'Requerimientos',range:'A1:E7',scale:1,format:'png'});
  await fs.writeFile(path.join(previewDir,'lafrox-workbook-before.png'), new Uint8Array(await blob.arrayBuffer()));
  console.log('Preview:',path.join(previewDir,'lafrox-workbook-before.png'));
} else {
  const routes = require('./routes.cjs');
  const documentary = new Set(['RF-13.01','RF-13.02','RF-13.03','RF-13.04','RF-16.01','RF-16.04']);
  const sheet = wb.worksheets.getItem('Requerimientos');
  const rows = sheet.getRange('A2:E203').values;
  const counts = {};
  for (const row of rows) {
    const urls = routes.filter((r) => r.rf.includes(row[0])).map((r) => 'index.html#' + r.path);
    if (urls.length) { row[3] = 'Sí'; row[4] = urls.join('\n'); }
    else if (documentary.has(row[0])) { row[3] = 'Documental'; row[4] = 'Fuera de la demostración funcional; consultar SD4 y checklist_sd3_sd4.md'; }
    else if (/^RT-25\./.test(row[0])) { /* Conservar evaluación independiente de las bases. */ }
    else { row[3] = 'No'; row[4] = ''; }
    counts[row[3]] = (counts[row[3]] || 0) + 1;
  }
  sheet.getRange('D2:E203').values = rows.map((r) => r.slice(3));
  sheet.getRange('D1:D203').format.columnWidth = 14;
  const status = sheet.getRange('D2:D203');
  status.conditionalFormats.deleteAll();
  status.format.fill = '#FFFFFF';
  status.conditionalFormats.addCustom('=$D2="Sí"',{fill:'#D6F5DD'});
  status.conditionalFormats.addCustom('=$D2="No"',{fill:'#FEE2E2'});
  status.conditionalFormats.addCustom('=$D2="Documental"',{fill:'#FEF3C7'});
  // Extender las alturas solo donde aumentó la cantidad de rutas del registro.
  rows.forEach((r,i) => { const lines = String(r[4]).split('\n').length; if (lines > 1) sheet.getRange(`D${i+2}:E${i+2}`).format.rowHeight = Math.max(72,lines*15); });
  const arch = wb.worksheets.getItem('Arquitectura lógica');
  arch.getRange('C1:C21').format.columnWidth = 14;
  const architecture = arch.getRange('A2:D21').values;
  architecture.forEach((row,i) => {
    if (/^M\d+$/.test(row[0])) {
      const re = new RegExp('\\b' + row[0] + '\\b');
      const urls = routes.filter((r) => re.test(r.module)).map((r) => 'index.html#' + r.path);
      arch.getRange(`C${i+2}:D${i+2}`).values = [[urls.length ? 'Sí' : 'No',urls.join('\n')]];
      arch.getRange(`D${i+2}`).format.rowHeight = Math.max(42,urls.length*15);
    } else if (row[0] !== 'Capa 1') { arch.getRange(`C${i+2}:D${i+2}`).values = [['No aplica','No materializada: prototipo estático, sin servidor. Arquitectura propuesta en SD4.']]; arch.getRange(`C${i+2}`).format.fill = '#F3F4F6'; }
  });
  const notes = wb.worksheets.getItem('Notas');
  notes.getRange('A1').values = [['«Cumple» indica trazabilidad declarada, no aceptación de producción. «Documental» se verifica en SD4; «No aplica» identifica capas no materializadas en el prototipo.']];
  wb.recalculate();
  console.log('Counts:',JSON.stringify(counts));
  console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!',options:{useRegex:true,maxResults:20},summary:'Errores de fórmula'})).ndjson);
  for (const [name,range] of [['Requerimientos','A124:E130'],['Arquitectura lógica','A1:D5'],['Notas','A1:A4']]) {
    const image = await wb.render({sheetName:name,range,scale:1,format:'png'});
    const output = path.join(previewDir,`lafrox-${name.replaceAll(' ','-')}.png`);
    await fs.writeFile(output,new Uint8Array(await image.arrayBuffer())); console.log('Preview:',output);
  }
  await (await SpreadsheetFile.exportXlsx(wb)).save(file);
  // La exportación del runtime omite autoFilter y no expone worksheet.autoFilter.
  // Restituir únicamente esta capacidad faltante, sin reautorizar celdas ni estilos.
  const JSZip = runtime('jszip');
  const zip = await JSZip.loadAsync(await fs.readFile(file));
  const filters = [['xl/worksheets/sheet1.xml','A1:E203'],['xl/worksheets/sheet2.xml','A1:D21']];
  for (const [entry,ref] of filters) {
    let xml = await zip.file(entry).async('string');
    const prefix = xml.match(/<([\w]+:)?worksheet\b/)[1] || '';
    if (!/<(?:\w+:)?autoFilter\b/.test(xml)) xml = xml.replace(`</${prefix}sheetData>`,`</${prefix}sheetData><${prefix}autoFilter ref="${ref}"/>`);
    zip.file(entry,xml);
  }
  let xml = await zip.file('xl/workbook.xml').async('string');
  const prefix = xml.match(/<([\w]+:)?workbook\b/)[1] || '';
  const definedNames = `<${prefix}definedNames><${prefix}definedName name="_xlnm._FilterDatabase" localSheetId="0" hidden="1">'Requerimientos'!$A$1:$E$203</${prefix}definedName><${prefix}definedName name="_xlnm._FilterDatabase" localSheetId="1" hidden="1">'Arquitectura lógica'!$A$1:$D$21</${prefix}definedName></${prefix}definedNames>`;
  if (!/<(?:\w+:)?definedNames\b/.test(xml)) xml=xml.replace(`</${prefix}sheets>`,`</${prefix}sheets>${definedNames}`);
  zip.file('xl/workbook.xml',xml);
  await fs.writeFile(file,await zip.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
}
