// Regenera tablas de trazabilidad desde el registro; no marca aceptación funcional.
const fs = require('node:fs');
const path = require('node:path');
const routes = require('./routes.cjs');
const root = path.resolve(__dirname, '..');
const file = path.join(root, 'docs/trazabilidad.md');
let doc = fs.readFileSync(file, 'utf8');
const oldTitles = new Map([...doc.matchAll(/^\| ([^|]+) \| `([^`]+)` \|/gm)].map((m) => [m[2],m[1].trim()]));
const order = new Map([...oldTitles.keys()].map((key,i) => [key,i]));
routes.sort((a,b) => (order.get(a.path) ?? 999) - (order.get(b.path) ?? 999));
const codes = new Set(routes.flatMap((r) => r.rf));
doc = doc.replace(/- (?:Los|El registro declara) \d+ códigos RF[^\n]+/, `- El registro declara ${codes.size} códigos RF, RNG y RNF en ${routes.length} rutas. La declaración localiza la evidencia; no sustituye la prueba de aceptación.`);
doc = doc.replace(/- Cada pantalla tiene[^\n]+/, '- Cada ruta tiene módulo y RF de SD3. Los documentos del prototipo están en `docs/`; no son rutas navegables.');
const modules = ['| Módulo | Pantallas |','|---|---|',...Array.from({length:12},(_,i) => {
  const id='M'+(i+1), re = new RegExp('\\b'+id+'\\b');
  return `| ${id} | ${routes.filter((r) => re.test(r.module)).map((r) => '`'+r.path+'`').join(', ')} |`;
})];
const matrix = ['| Pantalla | Ruta | Bloque 25.2 | Módulo SD4 | RF / RNG de SD3 | Actores (SD3, Anexo 3.A.12a) |','|---|---|---|---|---|',...routes.map((r) => `| ${oldTitles.get(r.path) || r.title} | \`${r.path}\` | ${r.block} | ${r.module} | ${r.rf.join(', ')} | ${r.actors.join(', ')} |`)];
doc = doc.slice(0,doc.indexOf('## Cobertura de módulos SD4')) + '## Cobertura de módulos SD4\n\n' + modules.join('\n') + `\n\n## Matriz completa (${routes.length} pantallas)\n\n` + matrix.join('\n') + '\n';
doc += '\n## Cierre de Prioridad 3 (03-11-2026)\n\n- RF-12.29: temporizador global para ambos perfiles de cliente; 15 min según el parámetro de demostración. «Mi perfil» permite adelantar el reloj de prueba. No se simula un token de servidor.\n- RF-18.01: «Estado de cuenta → Firmar acuerdo». Modos simple y avanzado simulados; certificado vencido/revocado bloquea, vigente genera evidencia JSON y sello de tiempo local. No tiene validez legal.\n- RF-17.12: cada dataTable exporta todos los registros filtrados y ordenados a JSON, no solo la página. Las tablas manuales exportan sus filas actuales; no tienen paginación oculta.\n- Borradores: botón y atajo `g s` en Flujo de pedido y Portal de pedidos; por perfil y pestaña. El atajo se desactiva en Perfil y no opera al escribir ni sobre un diálogo.\n- Portal ligero: seis productos por página, sin imágenes ni animaciones; conserva el carrito al cambiar de modo.\n\nLa planilla tiene 292 filas: 186 RF/RNG con ruta, 10 RT con la evaluación preexistente, 6 RF documentales (RF-13.01 a RF-13.04, RF-16.01 y RF-16.04) y los 90 RNF de SD3 (18 demostrables con ruta, 21 no demostrables en simulación y 51 documentales). Las capas 2–8 se clasifican «No aplica» al prototipo estático. «Sí» significa trazabilidad declarada; no certificación de producción ni validación automática de cada criterio.\n\nPara regenerar: `node revision/update_trace.cjs` y `node revision/update_workbook.mjs` con el runtime de `@oai/artifact-tool`. Ver `revision/verificacion_prioridad3.md` para pruebas y límites.\n';
fs.writeFileSync(file,doc);
console.log(JSON.stringify({routes:routes.length,codes:codes.size}));
