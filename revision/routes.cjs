// Lee únicamente metadatos de rutas; no confunde declarar un RF con probarlo.
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const listeners = () => {};
const context = { console, window: { addEventListener: listeners, LFX: { store: { get: (_, def) => def }, esc: (s) => s, icon: () => '' } }, document: { addEventListener: listeners }, setInterval, setTimeout, clearTimeout, clearInterval, Intl, URLSearchParams };
context.window.window = context.window;
vm.createContext(context);
for (const file of ['ui.js', 'data.js', 'router.js', ...fs.readdirSync(path.join(root, 'js/views')).filter((f) => f.endsWith('.js')).map((f) => 'views/' + f)]) {
  vm.runInContext(fs.readFileSync(path.join(root, 'js', file), 'utf8'), context, { filename: file });
}
const routes = context.window.LFX.routes.filter((r) => r.path !== '*').map((r) => ({ path: r.path, title: typeof r.title === 'string' ? r.title : r.title.toString(), block: r.block, module: r.module, rf: r.rf, actors: r.actors }));
if (require.main === module) console.log(JSON.stringify(routes, null, 2));
module.exports = routes;

