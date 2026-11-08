/* Ejecutar con Node y Playwright. LFX_NODE_MODULES permite usar el runtime del host.
   LFX_BROWSER permite señalar Chrome/Edge; no instala dependencias en el prototipo. */
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const assert = require('node:assert/strict');
const { chromium } = require(process.env.LFX_NODE_MODULES ? path.join(process.env.LFX_NODE_MODULES, 'playwright') : 'playwright');
const root = path.resolve(__dirname, '..');
const server = http.createServer((req, res) => {
  const file = path.resolve(root, '.' + decodeURI(req.url.split('?')[0] === '/' ? '/index.html' : req.url.split('?')[0]));
  if (!file.startsWith(root + path.sep)) { res.writeHead(403).end(); return; }
  fs.readFile(file, (err, data) => { if (err) { res.writeHead(404).end(); return; } res.setHeader('Content-Type', ({ '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml' })[path.extname(file)] || 'application/octet-stream'); res.end(data); });
});
const report = { functional: [], screens: [], consoleErrors: [] };
// Comprobación de contraste de texto HTML sólido; no certifica SVG, imágenes ni estados hover.
function auditContrast() {
  const canvas = document.createElement('canvas'); canvas.width=canvas.height=1;
  const ctx=canvas.getContext('2d',{willReadFrequently:true}), cache=new Map();
  const rgba=(color)=>{ if(cache.has(color))return cache.get(color); ctx.clearRect(0,0,1,1);ctx.fillStyle=color;ctx.fillRect(0,0,1,1);const p=[...ctx.getImageData(0,0,1,1).data];p[3]/=255;cache.set(color,p);return p; };
  const blend=(a,b)=>[0,1,2].map((i)=>a[i]*a[3]+b[i]*(1-a[3])).concat(1);
  const luminance=(c)=>c.slice(0,3).map((v)=>{v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4;}).reduce((s,v,i)=>s+v*[.2126,.7152,.0722][i],0);
  const bad=[];
  for(const el of document.querySelectorAll('body *')) {
    if(el.namespaceURI!=='http://www.w3.org/1999/xhtml'||!el.getClientRects().length||el.closest('.sr-only,[disabled],.toast-region'))continue;
    const text=[...el.childNodes].filter((n)=>n.nodeType===3).map((n)=>n.textContent.trim()).join(' '); if(!text)continue;
    const style=getComputedStyle(el);if(style.visibility!=='visible'||Number(style.opacity)<1)continue;
    let bg=[255,255,255,1], parents=[], parent=el, skip=false;
    while(parent){const st=getComputedStyle(parent);if(st.backgroundImage!=='none'||Number(st.opacity)<1)skip=true;parents.push(st.backgroundColor);parent=parent.parentElement;}
    if(skip)continue;
    for(const color of parents.reverse())bg=blend(rgba(color),bg);
    const fg=blend(rgba(style.color),bg),a=luminance(fg),b=luminance(bg),ratio=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);
    const large=parseFloat(style.fontSize)>=24||(parseFloat(style.fontSize)>=18.66&&parseInt(style.fontWeight)>=700),min=large?3:4.5;
    if(ratio<min-.03)bad.push({text:text.slice(0,80),ratio:+ratio.toFixed(2),min,color:style.color,bg:parents[parents.length-1]});
  }
  return bad.slice(0,20);
}
(async () => {
  await new Promise((r) => server.listen(0, '127.0.0.1', r));
  const browser = await chromium.launch({ headless: true, ...(process.env.LFX_BROWSER ? { executablePath: process.env.LFX_BROWSER } : {}) });
  try {
    const page = await browser.newPage();
    page.on('pageerror', (e) => report.consoleErrors.push(e.message));
    page.on('console', (m) => { if (m.type() === 'error' && !m.text().includes('net::ERR')) report.consoleErrors.push(m.text()); });
    await page.route('https://**/*', (r) => r.abort());
    await page.goto(`http://127.0.0.1:${server.address().port}`);
    const login = async (profile = 'evaluador') => page.evaluate((profile) => { LFX.signIn(profile); LFX.store.set('seen.' + profile, true); LFX.session().first && LFX.setSession({ ...LFX.session(), first: false }); }, profile);
    const go = async (route) => { await page.evaluate((route) => LFX.go(route), route); await page.waitForTimeout(750); };
    await login('cliente'); await go('/portal/pedido');
    await page.locator('[data-add]').first().click();
    await page.locator('#pp-draft').click();
    assert.ok(await page.evaluate(() => Object.keys(LFX.store.get(LFX.draftKey('portal'), {})).length));
    await page.reload(); await page.waitForTimeout(200);
    assert.ok(await page.locator('#pp-send').count());
    await page.locator('#pp-light').click(); await page.waitForTimeout(100);
    assert.equal(await page.locator('[data-add]').count(), 6);
    assert.equal(await page.locator('#pp-grid img').count(), 0);
    assert.ok(await page.locator('#pp-send').count(), 'Cambiar a ligero conserva el carrito');
    report.functional.push('Borrador de portal restaurado tras recarga; vista ligera paginada conserva el carrito y no carga imágenes');
    await go('/portal/cuenta');
    await page.setViewportSize({width:375,height:812});
    assert.equal(await page.evaluate(() => document.documentElement.dataset.portalLight), 'on');
    await page.locator('#pc-sign').click();
    await page.locator('#sig-mode').selectOption('advanced');
    await page.locator('#sig-cert').selectOption('expired');
    await page.locator('#sig-consent').check();
    await page.getByRole('button', { name: 'Firmar', exact: true }).click();
    assert.match(await page.locator('#sig-error').innerText(), /bloqueada/);
    assert.equal(await page.evaluate(() => LFX.store.get('signatures.cliente', []).length), 0);
    await page.locator('#sig-cert').selectOption('revoked');
    await page.getByRole('button', { name: 'Firmar', exact: true }).click();
    assert.match(await page.locator('#sig-error').innerText(), /bloqueada/);
    await page.locator('#sig-cert').selectOption('valid');
    await page.getByRole('button', { name: 'Firmar', exact: true }).click();
    await page.waitForTimeout(100);
    assert.equal(await page.evaluate(() => LFX.store.get('signatures.cliente', [])[0].certificado), 'DEMO-001');
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth+1),false,'Firma sin desbordamiento móvil');
    const dl = page.waitForEvent('download');
    await page.getByRole('button', { name: 'Descargar evidencia JSON' }).click();
    assert.equal((await dl).suggestedFilename(), 'firma-simulada.json');
    report.functional.push('Firma avanzada: certificados vencido/revocado bloqueados, vigente genera evidencia y descarga JSON');
    await page.locator('#pc-sign').click();
    assert.equal(await page.locator('[role=dialog]').count(),1);
    await page.evaluate(() => { LFX.setSession({ ...LFX.session(), lastActivity: Date.now() - LFX.idleLimit() - 1000 }); });
    await page.waitForTimeout(1300);
    assert.equal(await page.evaluate(() => LFX.session()), null);
    assert.equal(await page.locator('[role=dialog]').count(), 0);
    assert.match(page.url(), /ingresar/);
    await login('cliente-moderno'); await go('/portal/cuenta');
    const previous = await page.evaluate(() => { const t=Date.now()-5000;LFX.setSession({...LFX.session(),lastActivity:t});return t; });
    await page.locator('#pc-pay').click();
    assert.ok(await page.evaluate((t)=>LFX.session().lastActivity>t,previous));
    await page.evaluate(() => { LFX.setSession({...LFX.session(),lastActivity:Date.now()-LFX.idleLimit()-1000}); LFX.go('/portal/pedido'); });
    await page.waitForTimeout(150);
    assert.equal(await page.evaluate(()=>LFX.session()),null);
    report.functional.push('Inactividad en ambos clientes: actividad renueva plazo; temporizador y navegación expiran sesión y cierran diálogos');
    await login(); await go('/pedidos');
    await page.evaluate(() => {
      const host = document.createElement('div'); document.getElementById('main').append(host);
      window.testTable = LFX.dataTable(host, { id: 'test-json', rows: Array.from({length:25}, (_,i) => ({id:i, nombre: i % 2 ? 'Uno' : 'Dos'})), searchKeys: ['nombre'], columns: [{key:'id',label:'ID'}, {key:'nombre',label:'Nombre'}] });
      testTable.state.q = 'Uno'; testTable.state.sort = 'id'; testTable.state.dir = 'desc'; testTable.draw();
      window.originalDownload = LFX.download; LFX.download = (name, data) => { window.exported = {name,data}; };
    });
    await page.locator('#test-json-q').locator('..').locator('..').getByRole('button', {name:'Exportar JSON: Listado'}).click();
    const exported = await page.evaluate(() => JSON.parse(window.exported.data));
    assert.equal(exported.length, 12); assert.equal(exported[0].id, 23); assert.equal(exported[11].id, 1);
    await page.evaluate(() => { LFX.download = window.originalDownload; });
    report.functional.push('JSON de dataTable respeta búsqueda, orden descendente y todas las páginas');
    await go('/flujo');
    await page.evaluate(()=>{window.originalDownload=LFX.download;LFX.download=(name,data)=>{window.exported={name,data};};});
    await page.locator('.table-json').first().click();
    assert.equal(await page.evaluate(()=>JSON.parse(window.exported.data).filas.length),4);
    await page.evaluate(()=>{LFX.download=window.originalDownload;});
    report.functional.push('Tabla manual de picking exporta sus cuatro líneas a JSON');
    await page.locator('#fl-draft').click();
    assert.ok(await page.evaluate(() => LFX.store.get(LFX.draftKey('flujo'), null)));
    await page.evaluate(() => LFX.store.set(LFX.draftKey('flujo'), null));
    await page.locator('#fl-h').focus();
    await page.keyboard.press('g'); await page.keyboard.press('s');
    assert.ok(await page.evaluate(() => LFX.store.get(LFX.draftKey('flujo'), null)));
    await page.reload(); await page.waitForTimeout(150);
    assert.ok(await page.locator('#fl-h').count());
    await page.evaluate(() => { LFX.store.set(LFX.draftKey('flujo'), null); LFX.store.setPref('shortcuts', 'off'); });
    await page.locator('#fl-h').focus(); await page.keyboard.press('g'); await page.keyboard.press('s');
    assert.equal(await page.evaluate(() => LFX.store.get(LFX.draftKey('flujo'), null)), null);
    await page.evaluate(() => LFX.store.setPref('shortcuts', 'on'));
    await page.locator('#pv-add').focus();await page.keyboard.type('gs');
    assert.equal(await page.evaluate(() => LFX.store.get(LFX.draftKey('flujo'), null)), null);
    await page.locator('#pv-add').fill('');await page.locator('#fl-h').focus();
    await page.keyboard.press('g');await page.keyboard.press('i');await page.waitForTimeout(100);
    assert.match(page.url(), /inicio/);
    report.functional.push('Borrador de flujo y atajo g s; preferencia de desactivación respetada');

    await login('preventista'); await go('/flujo?nuevo=1&paso=7');
    assert.equal(await page.locator('#rd-f').count(), 0, 'No se puede rendir un borrador mediante URL');
    await page.locator('#pv-promo').check();
    const promo = await page.locator('#pv-discount').innerText();
    await page.getByRole('button', {name:/Quitar Leche entera/}).click();
    await page.getByRole('button', {name:/Quitar Arroz/}).click();
    assert.equal(await page.locator('#pv-discount').innerText(), promo, 'La promoción no depende del orden ni del número de líneas');
    await page.getByRole('button', {name:/Quitar Bebida cola/}).click();
    assert.equal(await page.locator('#pv-discount').innerText(), 'Sin descuento');
    assert.ok(await page.locator('#pv-promo').isDisabled());
    report.functional.push('Promoción 3×2 por SKU y bloqueo del salto a rendición en borrador');
    await page.locator('#pv-save').click();
    await page.locator('#vl-sim').check();
    await page.locator('#vl-go').click();
    await page.locator('#vl-refresh').waitFor();
    assert.equal(await page.locator('#vl-demo-finance').count(), 0);
    await login('finanzas'); await go('/flujo');
    await page.getByRole('button', {name:'Revisar solicitud'}).click();
    await page.locator('#credit-reason').fill('Excepción de demostración verificada');
    await page.getByRole('button', {name:'Autorizar pedido'}).click();
    await login('preventista'); await go('/flujo');
    assert.match(await page.locator('#fl-body').innerText(), /Crédito autorizado/);
    await login('preparador'); await go('/recepcion/nueva');
    assert.match(page.url(), /#\/inicio$/);
    await go('/flujo?escena=preparacion');
    assert.match(await page.locator('#fl-h').innerText(), /Picking/);
    assert.match(await page.locator('main').innerText(), /Escenario de práctica/);
    await login('gerente-ops'); await go('/calidad/retiro');
    assert.match(page.url(), /#\/inicio$/);
    await login('ti'); await go('/admin/roles');
    await page.locator('#ro-profile').selectOption('preparador');
    await page.locator('[data-permission="recepcion.registrar"]').check();
    await page.locator('#ro-save').click();
    await page.getByRole('button', {name:'Enviar a aprobación', exact:true}).last().click();
    assert.equal(await page.evaluate(() => LFX.profileCan('preparador','recepcion.registrar')), false);
    assert.equal(await page.locator('[data-review]').count(), 0);
    await login('gerente-ops'); await go('/admin/roles');
    await page.getByRole('button', {name:'Aprobar',exact:true}).click();
    await login('preparador'); await go('/recepcion/nueva');
    assert.match(page.url(), /#\/recepcion\/nueva$/);
    report.functional.push('URLs por permiso, traspaso a Finanzas y cambios de permiso efectivos tras aprobación de otro perfil');
    await login(); await go('/analitica');
    assert.equal(await page.locator('.kpi a button, a.kpi button').count(), 0);
    await page.locator('.skip-link').focus(); await page.keyboard.press('Enter');
    assert.equal(await page.evaluate(() => document.activeElement.id), 'main');
    assert.match(page.url(), /#\/analitica$/);
    await go('/pedidos');
    await page.locator('button[data-sort]').first().focus(); await page.keyboard.press('Enter');
    assert.equal(await page.locator('button[aria-sort]').count(), 0);
    assert.equal(await page.locator('th[aria-sort]').count(), 1);
    assert.ok(await page.evaluate(() => document.activeElement.hasAttribute('data-sort')));
    report.functional.push('Teclado: salto a contenido sin cambiar ruta, orden de tabla y controles KPI no anidados');

    await login('conductor'); await go('/terreno');
    assert.match(await page.locator('#tr-host').innerText(), /R-01 Cauquenes/);
    await page.locator('#dev-net').uncheck();
    await page.locator('[data-dtab=mas]').click();
    await page.locator('[data-crew]').click();
    assert.match(await page.getByRole('dialog').innerText(), /sin sesión compartida/);
    assert.equal(await page.getByRole('button', {name:/inicia su sesión/}).count(), 0);
    await page.keyboard.press('Escape');
    await login('conductor-ext'); await go('/terreno');
    assert.match(await page.locator('#tr-host').innerText(), /R-09 Parral/);
    assert.ok(await page.locator('#dev-net').isChecked());
    assert.equal(await page.locator('[data-stop^="E-"]').count(), 0);
    report.functional.push('Tripulación sin sesión ficticia y ruta/señal aisladas por perfil');
    await login(); await go('/analitica');
    assert.ok((await page.locator('#an-summary').innerText()).includes('pedidos'));
    const initial = parseInt(await page.locator('#an-summary').innerText());
    await page.locator('#an-canal').selectOption('Tradicional');
    await page.locator('#an-apply').click();
    await page.waitForURL(/canal=Tradicional/);
    const selected = parseInt(await page.locator('#an-summary').innerText());
    assert.ok(selected > 0 && selected < initial, 'Filtrar el canal selecciona pedidos, no escala porcentajes');
    assert.ok(await page.locator('a.kpi[href*="canal=Tradicional"]').count());
    await page.evaluate(() => { window.originalDownload=LFX.download; LFX.download=(name,data)=>{window.exported={name,data};}; });
    await page.locator('#an-exp').click();
    await page.locator('[name=an-section][value=kpis]').uncheck();
    await page.locator('[name=an-section][value=charts]').uncheck();
    await page.getByRole('button', {name:'Descargar CSV'}).click();
    const csvReport = await page.evaluate(() => window.exported.data);
    assert.match(csvReport, /Detalle por ruta/);
    assert.doesNotMatch(csvReport, /Indicadores principales|Resultado por canal|Food service|Moderno/);
    assert.equal((csvReport.match(/"Canal";"Tradicional"/g) || []).length, selected);
    await page.locator('a.kpi').first().click();
    await page.waitForURL(/analitica\/otif\?.*canal=Tradicional/);
    await page.locator('#dk-exp').click();
    const detailReport = await page.evaluate(() => window.exported.data);
    assert.equal(detailReport.trim().split('\n').length - 1, selected);
    assert.doesNotMatch(detailReport, /Food service|Moderno/);
    await page.evaluate(() => { LFX.download = window.originalDownload; });
    report.functional.push('Analítica: filtros viajan al detalle; el CSV contiene la misma muestra y solo las secciones solicitadas');
    const routes = await page.evaluate(() => LFX.routes.filter((r) => r.path !== '*').map((r) => r.path.replace(':kpi', LFX.data.kpis[0].id).replace(':id', r.path.includes('/pedidos') ? LFX.data.pedidos[0].id : r.path.includes('/clientes') ? LFX.data.clientes[0].id : r.path.includes('/rutas') ? LFX.data.rutas[0].id : r.path.includes('/devoluciones') ? LFX.data.devoluciones[0].id : r.path.includes('/lotes') ? LFX.data.lotes[0].id : LFX.data.rutas[0].id)));
    for (const mode of (process.env.LFX_THEMES || 'light:normal').split(',')) {
    const [theme,contrastMode] = mode.split(':');
    await page.evaluate(({theme,contrastMode})=>{LFX.store.setPref('theme',theme);LFX.store.setPref('contrast',contrastMode);LFX.applyPrefs();},{theme,contrastMode});
    for (const [width,height] of [[375,812],[768,1024],[1024,768],[1366,768],[1920,1080]]) {
      await page.setViewportSize({width,height});
      for (const route of routes) {
        if (process.env.LFX_ROUTES && !process.env.LFX_ROUTES.split(',').includes(route)) continue;
        await go(route);
        const state = await page.evaluate(() => {
          const visible = (el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 && getComputedStyle(el).visibility !== 'hidden'; };
          return { overflow: document.documentElement.scrollWidth > innerWidth + 1, offenders: [...document.querySelectorAll('#app *')].filter(visible).filter((el) => el.getBoundingClientRect().right > innerWidth+1 && !el.closest('.table-wrap,.tabs,.sidebar')).slice(-12).map((el)=>({tag:el.tagName,cls:el.className,id:el.id,right:Math.round(el.getBoundingClientRect().right)})), error: document.body.innerText.includes('No pudimos mostrar esta pantalla'), tiny: [...document.querySelectorAll('button,a[href],input,select,textarea')].filter(visible).filter((el) => !el.disabled).map((el) => { const target = el.closest('label') || el; const r = target.getBoundingClientRect(); return {label:el.getAttribute('aria-label') || el.textContent.trim().slice(0,55),width:Math.round(r.width),height:Math.round(r.height)}; }).filter((r) => r.width < 44 || r.height < 44) };
        });
        report.screens.push({theme,contrastMode,width,height,route,...state});
        if(process.env.LFX_CONTRAST) report.screens[report.screens.length-1].contrast = await page.evaluate(auditContrast);
        if (process.env.LFX_SCREENSHOTS && width === 375) await page.screenshot({path:path.join(process.env.LFX_SCREENSHOTS,`${route.replaceAll('/','_') || 'inicio'}-${theme}-${contrastMode}.png`),fullPage:true});
      }
    }
    }
    assert.equal(report.consoleErrors.length, 0, report.consoleErrors.join('\n'));
    assert.equal(report.screens.filter((s) => s.error).length, 0, 'Pantallas con fallback');
    assert.equal(report.screens.filter((s) => s.overflow).length, 0, 'Desbordamiento horizontal');
    assert.equal(report.screens.filter((s) => s.tiny.length).length, 0, 'Objetivos HTML menores de 44 px');
    assert.equal(report.screens.filter((s) => s.contrast?.length).length, 0, 'Contraste de texto HTML');
  } finally { await browser.close(); }
})().catch((e) => { report.failure = e.stack; process.exitCode = 1; }).finally(() => {
  const output = process.env.LFX_QA_REPORT || path.join(require('node:os').tmpdir(), 'lafrox-qa.json');
  fs.writeFileSync(output, JSON.stringify(report,null,2)); server.close();
  console.log(JSON.stringify({ functional: report.functional, screens: report.screens.length, overflow:report.screens.filter((s)=>s.overflow).length, tiny:report.screens.filter((s)=>s.tiny?.length).length, errors:report.consoleErrors, failure:report.failure, output },null,2));
});

