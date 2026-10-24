import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import { Workbook } from '@oai/artifact-tool';

const root = process.cwd();
const output = path.join(root, 'outputs', 'ganttproject', 'LafroX-Gantt-antes-reestimacion.csv');
const templatePath = 'C:/Users/Leand/Documents/GanttProject/PRUEBA.csv';
const read = relative => fs.readFile(path.join(root, relative), 'utf8');
const clean = text => text
  .replace(/\\allowbreak\{\}/g, '')
  .replace(/\\(?:textbf|textit|ensuremath|mbox|emph)\{([^{}]*)\}/g, '$1')
  .replace(/\\(?:times|rightarrow|geq|leq)/g, match => ({'\\times':'×','\\rightarrow':'→','\\geq':'≥','\\leq':'≤'}[match]))
  .replace(/\\([%&_#])/g, '$1')
  .replace(/[{}]/g, '').replace(/~/g, ' ').replace(/\s+/g, ' ').trim();
const tableRows = text => [...text.matchAll(/^\s*(\d+(?:\.\d+){2,3})\s*&\s*(.*?)\\\\\s*$/gm)]
  .map(match => [match[1], ...match[2].split(/(?<!\\)&/).map(clean)]);
const [edtText, datesText, continuousText, templateText, milestoneText, annexText] = await Promise.all([
  read('formulario-t14/contenido.tex'), read('formulario-t15/tablas/tab_T15_paquetes.tex'),
  read('formulario-t15/tablas/tab_T15_10.tex'), fs.readFile(templatePath, 'utf8'),
  read('subdocumento-07/tablas/tab_SD7_4.tex'), read('subdocumento-07-anexos/tablas/tab_7B1.tex'),
]);
const header = templateText.replace(/^\uFEFF/, '').split(/\r?\n/)[0].split(',');
assert.equal(header.length, 16);
const DAY = 86400000;
const parseDate = text => {
  const [d,m,y] = text.split('-').map(Number);
  return new Date(Date.UTC(y,m-1,d));
};
const iso = date => date.toISOString().slice(0,10);
const fmt = date => `${date.getUTCDate()}/${date.getUTCMonth()+1}/${String(date.getUTCFullYear()).slice(-2)}`;
const workday = date => ![0,6].includes(date.getUTCDay());
const shift = (date,n) => new Date(date.getTime()+n*DAY);
const nextWorkday = date => { let d = new Date(date); while(!workday(d)) d=shift(d,1); return d; };
const previousWorkday = date => { let d=new Date(date); while(!workday(d)) d=shift(d,-1); return d; };
const weekdays = (start,end) => { let n=0; for(let d=start; d<=end; d=shift(d,1)) if(workday(d)) n++; return n; };
const monthStart = month => nextWorkday(new Date(Date.UTC(2027,1+month-1,1)));
const monthEnd = month => previousWorkday(new Date(Date.UTC(2027,1+month,0)));
const sourceBase = 'Escenario nominal histórico anterior a la reestimación. Mes 1: febrero de 2027. Calendario gráfico: lunes a viernes, sin descontar feriados. Duración de la barra: días hábiles de la ventana, no HH de esfuerzo.';
const nodes = [];
const byCode = new Map();
for (const line of edtText.split(/\r?\n/)) {
  const match=line.match(/^\\item\s+(?:\\textbf\{)?(\d+(?:\.\d+)*)(?:\.)?\s+(.+)$/);
  if(!match) continue;
  const code=match[1], label=clean(match[2]);
  assert(!byCode.has(code), `EDT duplicada: ${code}`);
  const node={code,label,kind:'summary',role:'',notes:[],deps:new Map()};
  nodes.push(node); byCode.set(code,node);
}
const scheduled = new Map(tableRows(datesText).map(row=>[row[0],row]));
const continuous = new Map(tableRows(continuousText).map(row=>[row[0],row]));
assert.equal(scheduled.size,163); assert.equal(continuous.size,59);
for(const [code,row] of scheduled){
  const node=byCode.get(code); assert(node, `Falta ${code}`);
  Object.assign(node,{kind:'package',role:row[1],start:nextWorkday(parseDate(row[4])),end:previousWorkday(parseDate(row[5]))});
  node.notes.push(`Fuente de fechas: T-15, tabla Programación de los paquetes con entregable, paquete ${code}. Fechas publicadas: ${row[4]} a ${row[5]}. Predecesoras agregadas publicadas: ${row[6]}.`);
  if(iso(node.start)!==iso(parseDate(row[4])) || iso(node.end)!==iso(parseDate(row[5])))
    node.notes.push('El límite publicado cae en fin de semana; la barra utiliza el día hábil interior de la misma ventana. No se alteró el mes contractual.');
}
for(const [code,row] of continuous){
  assert(!scheduled.has(code)); const node=byCode.get(code); assert(node);
  const months=row[3].split(/[–—-]/).map(Number); assert(months.length===2);
  Object.assign(node,{kind:'package',role:row[2],start:monthStart(months[0]),end:monthEnd(months[1])});
  node.notes.push(`Fuente de ventana: T-15, tabla Actividades de los paquetes de esfuerzo continuo, meses ${row[3]}. Se representa la ventana completa, no dedicación diaria continua. Regla original: ${row[5]}.`);
}
assert.equal(nodes.filter(n=>n.kind==='package').length,222);
assert.equal(nodes.filter(n=>n.kind==='summary'&&n.code.split('.').length===1).length,9);
assert.equal(nodes.filter(n=>n.kind==='summary'&&n.code.split('.').length===2).length,49);
for(const node of nodes.filter(n=>n.kind==='summary')) assert(nodes.some(n=>n.code.startsWith(node.code+'.')),`Resumen vacío: ${node.code}`);

// The publication has aggregate dependencies spanning two stages. Expand only the
// precise links in Annex 7.B instead of interpreting every account as an FS link.
const leaves = code => byCode.get(code)?.kind==='package' ? [byCode.get(code)] : nodes.filter(n=>n.kind==='package'&&n.code.startsWith(code+'.'));
const edgeLog=[];
function relation(predecessor,successor,type,id,comment='') {
  const pred=byCode.get(predecessor), succ=byCode.get(successor); assert(pred&&succ,`${id}: ${predecessor} -> ${successor}`);
  succ.notes.push(`${id}: ${predecessor} → ${successor}, ${type==='FS'?'FC':type==='SS'?'CC':type}. ${comment}`.trim());
  const compatible=type==='FS' ? succ.start >= (pred.kind==='milestone'?pred.start:nextWorkday(shift(pred.end,1)))
    : type==='SS' ? succ.start>=pred.start : type==='FF' ? succ.end>=pred.end : false;
  if(compatible){
    const existing=succ.deps.get(predecessor);
    if(!existing || existing.type===type) succ.deps.set(predecessor,{type,id});
    else succ.notes.push(`${id}: condición adicional del mismo par conservada en notas; el CSV admite una relación por par.`);
  }else{
    succ.notes.push(`${id}: vínculo documental NO activado en Antecesores porque la ventana nominal publicada lo contradice. Se conservan las fechas del escenario histórico; no es una red recalculada.`);
  }
  edgeLog.push({id,predecessor,successor,type,active:compatible});
}
function many(preds,succs,type,id,comment='') {
  for(const p of preds) for(const s of succs) relation(p,s,type,id,comment);
}
const codes = group => leaves(group).map(n=>n.code);
many(['1.2.1'],['2.1.1'],'FS','D-01');
many(['1.2.3'],['3.3.2'],'FS','D-02');
many(['1.2.2'],['3.4.7'],'FS','D-03');
many(['2.4.1'],codes('3.4'),'FS','D-04');
many(['2.6.2'],codes('3.4'),'FS','D-05');
many(['2.2.1'],['3.3.1'],'FS','D-06');
many(['5.2.1'],codes('3.2'),'FS','D-07');
many(['3.2.1','3.2.2','3.2.4','3.2.5'],['3.1.1','3.1.2','3.1.3'],'FS','D-08');
many(['3.2.3'],['3.4.5'],'FS','D-08-IoT');
many(['3.2.6'],['6.5.1'],'FS','D-08-MDM');
many(['2.3.1','2.3.2'],['5.1.2'],'FS','D-09');
many(['5.1.2'],codes('6.1'),'FS','D-10');
many(['6.1.5'],['6.3.1','6.3.2'],'FS','D-11');
many(['6.3.1','6.3.2','6.3.3'],codes('6.6'),'FS','D-12');
many(['6.3.4'],['6.5.1'],'SS','D-12-campo');
// QA availability constrains delivery, not the start of development.
many(['3.1.1','3.1.2','3.1.3'],codes('3.4'),'FF','D-14','La dependencia original condiciona la entrega en QA, no el inicio del desarrollo. Se representa como fin-fin a nivel de paquete.');
many(codes('3.3'),codes('3.4'),'SS','D-15');
for(const [id,preds,succs] of [
  ['D-16',['3.4.1','3.4.2'],['3.4.3','3.4.4']],
  ['D-18',['3.4.3','3.4.6'],['3.4.7','3.4.8']],
  ['D-19',['3.4.8'],['3.4.10']],
]) many(preds,succs,'SS',id,'Relación POR INTERFAZ resumida con CC para conservar el solapamiento. Construcción después del contrato A02 e integración después de la entrega A12: esas puertas internas se conservan como condición documental y no se descomponen en este CSV de paquetes.');
many(['3.4.2'],['3.4.6'],'SS','D-17');
many([...codes('3.4'),'3.6.1','3.6.2','3.6.3','3.6.4'],['3.8.1'],'FS','D-20');
many(['3.8.1'],['3.8.2','3.8.3'],'FS','D-21');
many(['3.8.1'],['3.8.4','3.8.5','3.8.6','3.8.8'],'FS','D-21b');
many(['3.1.3'],['3.8.5'],'FS','D-22');
many(['3.8.2','3.8.3','3.8.4','3.8.5','3.8.6','3.8.8'],['3.8.7'],'FS','D-23');
many(['3.7.1','3.7.2','3.7.3','3.7.4'],['3.7.5'],'FS','D-24','La puerta del corte A06 depende de los ensayos; el detalle interno no se descompone.');
many(['3.8.7','3.7.5','4.1.1','4.1.2'],['4.2.1'],'FS','D-25');
many(codes('6.5'),['4.2.1'],'FS','D-26','La fuente exige equipamiento antes de su ola. Esta vista agregada muestra la disponibilidad del equipamiento antes de la ventana de marcha blanca.');
many(['5.4.1','5.4.2'],['4.2.1'],'FS','D-27');
many(['4.2.1','7.3.1'],['4.2.3'],'FS','D-28');
many(['4.2.3'],['4.2.2'],'FS','D-28-posterior','La estabilización es posterior al acta; la ventana mensual no fija el día de inicio.');
many(['1.2.5','2.4.2'],codes('3.5'),'FS','D-29');
many(codes('3.5'),['3.9.1'],'FS','D-30');
many(['3.9.1'],['3.9.2'],'FS','D-31');
many(['3.9.1'],['3.9.3','3.9.4','3.9.5','3.9.7'],'FS','D-31b');
many(['3.9.2','3.9.3','3.9.4','3.9.5','3.9.7'],['3.9.6'],'FS','D-31c');
many(['3.9.6','3.6.5','4.1.3'],['4.3.1'],'FS','D-32');
many(['4.3.1','7.3.2','7.1.4','4.3.4'],['4.3.3'],'FS','D-33');
many(['4.3.3'],[...codes('8'),...codes('9.1')],'FS','D-34','Inicio contractual por mes 21; la tabla diaria y la ventana mensual se conservan aunque no fijan un corte diario compatible. El SOC 8.1.5 empieza en mes 13 como excepción explícita.');
many(['2.1.1','2.1.2','2.1.3','2.2.1','2.2.3','2.2.4'],['2.4.1'],'FS','Diseño-H2');
many(['1.2.5','2.1.4'],['2.4.2'],'FS','Diseño-H8');

// Contractual milestones are shown at the last working day of the fixed month,
// except H6/H11, whose marker is at the beginning of the white-run window.
const milestoneGroup={code:'10',label:'Hitos contractuales H1–H12',kind:'summary',role:'',notes:[],deps:new Map()};
nodes.push(milestoneGroup); byCode.set('10',milestoneGroup);
const milestones=[...milestoneText.matchAll(/^\s*(H\d+)\s*&\s*(\d+)\s*&\s*(.*?)\s*&\s*(.*?)\\\\/gm)];
assert.equal(milestones.length,12);
for(let i=0;i<milestones.length;i++){
  const [,hito,monthText,label,packageText]=milestones[i], month=Number(monthText), first=['H6','H11'].includes(hito);
  const date=first?monthStart(month):monthEnd(month);
  const node={code:`10.${i+1}`,label:`${hito} — ${clean(label)}`,kind:'milestone',role:'JP',start:date,end:date,notes:[`Formulario E-25 y SD7, tabla de hitos: ${hito}, mes ${month}. Ubicación gráfica convencional: ${first?'primer':'último'} día hábil del mes; no constituye una fecha diaria contractual confirmada. Paquetes: ${clean(packageText)}.`],deps:new Map()};
  nodes.push(node); byCode.set(node.code,node);
  for(const packageCode of packageText.match(/\d+(?:\.\d+){2,3}/g)??[])
    relation(packageCode,node.code,first?'SS':'FS',`Hito-${hito}`);
  if(hito==='H3') relation('6.6.3',node.code,'FS','D-13');
}
for(const node of nodes.filter(n=>n.kind==='summary').reverse()){
  const descendants=nodes.filter(n=>n.kind!=='summary'&&n.code.startsWith(node.code+'.'));
  assert(descendants.length);
  node.start=new Date(Math.min(...descendants.map(n=>n.start.getTime())));
  node.end=new Date(Math.max(...descendants.map(n=>n.end.getTime())));
  node.notes.push('Tarea resumen; fechas derivadas del primer y último paquete o hito descendiente.');
}
const ids=new Map(nodes.map((n,i)=>[n.code,i]));
// DFS over dependency edges: hierarchy and IDs need not be chronological.
const visiting=new Set(),visited=new Set();
function visit(code){
  assert(!visiting.has(code),`Ciclo en ${code}`); if(visited.has(code))return;
  visiting.add(code); for(const p of byCode.get(code).deps.keys())visit(p);
  visiting.delete(code);visited.add(code);
}
for(const node of nodes)visit(node.code);
const colors=['#526D82','#237A69','#D17A32','#8B4C8F','#83822F','#587B39','#B85B74','#387C9C','#666666','#D0A020'];
const rows=nodes.map(node=>{
  assert(node.start<=node.end,`Ventana inválida ${node.code}`);
  const depth=node.code.split('.').length-1;
  const name=`${'  '.repeat(depth)}${node.code==='10'||node.kind==='milestone'?'':node.code+' '}${node.label}`;
  const deps=[...node.deps].map(([code,{type}])=>`${ids.get(code)}-${type}>P0D`).join(';');
  // Rubber dependencies preserve the historical start dates and existing gaps.
  const notes=[sourceBase,...node.notes,node.role?`Responsable del paquete: ${node.role}.`:'',node.deps.size?'Antecesores con restricción mínima (>) para conservar los huecos del escenario nominal; no se agregaron desfases ni reservas calculadas.':''].filter(Boolean).join(' ');
  return [String(ids.get(node.code)),name,fmt(node.start),fmt(node.end),String(node.kind==='milestone'?0:weekdays(node.start,node.end)),'0','0','1','',''+deps,node.code,'','',colors[Number(node.code.split('.')[0])-1],notes,''];
});
assert.equal(rows.length,297);
for(const row of rows)assert.equal(row.length,header.length);
const workbook=Workbook.create(); const sheet=workbook.worksheets.add('Gantt');
sheet.getRange(`A1:P${rows.length+1}`).values=[header,...rows];
const inspection=await workbook.inspect({kind:'region',sheetId:'Gantt',range:'A1:F5',maxChars:1600,tableMaxRows:5,tableMaxCols:6});
const values=sheet.getRange(`A1:P${rows.length+1}`).values;
function csvCell(value){
  const text=value==null?'':String(value);
  return /[",\r\n]/.test(text)||/^\s|\s$/.test(text)?`"${text.replace(/"/g,'""')}"`:text;
}
await fs.mkdir(path.dirname(output),{recursive:true});
await fs.writeFile(output,values.map(row=>row.map(csvCell).join(',')).join('\r\n')+'\r\n','utf8');
const summary={output,rows:rows.length,packages:222,phases:9,accounts:49,innovationGroups:4,milestones:12,scheduledPackages:163,continuousPackages:59,start:iso(monthStart(1)),end:iso(monthEnd(56)),activeEdges:edgeLog.filter(e=>e.active).length,documentedOnlyEdges:edgeLog.filter(e=>!e.active),adjustedWeekendDates:[...scheduled].filter(([code,row])=>iso(byCode.get(code).start)!==iso(parseDate(row[4]))).map(([code])=>code),inspection:inspection.ndjson};
await fs.writeFile(path.join(root,'tmp/ganttproject-historico/validation.json'),JSON.stringify(summary,null,2),'utf8');
console.log(JSON.stringify({...summary,inspection:undefined},null,2));
