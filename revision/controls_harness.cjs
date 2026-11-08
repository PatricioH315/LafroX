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
/* Pruebas de los controles auditados. Configuración de Playwright igual a verify.cjs.
   LFX_QA_URL permite ejecutar las mismas pruebas contra GitHub Pages. */
const { expect } = require(process.env.LFX_NODE_MODULES ? path.join(process.env.LFX_NODE_MODULES, 'playwright/test') : 'playwright/test');
async function startControls(page, base) {
  page.setDefaultTimeout(6500);
  await page.goto(base);
  await page.evaluate(() => { LFX.signIn('evaluador'); LFX.setSession({ ...LFX.session(), first: false }); });
  const go = async (route) => { await page.evaluate((r) => LFX.go(r), route); await expect.poll(() => new URL(page.url()).hash).toBe('#' + route); };
  const button = (name) => page.getByRole('button', { name, exact: true });
  const row = (id) => page.locator('tr[data-id="' + id + '"]');
  const action = async (id, name) => { await row(id).locator('[data-rowmenu]').click(); await page.getByRole('menuitem', { name, exact: true }).click(); };
  return { go, button, row, action };
}

async function runControls(check, label) {
  const remote = process.env.LFX_QA_URL;
  if (!remote) await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  let browser;
  const errors = [];
  try {
    browser = await chromium.launch({ headless: true, ...(process.env.LFX_BROWSER ? { executablePath: process.env.LFX_BROWSER } : {}) });
    const page = await browser.newPage({ viewport: { width: 1366, height: 768 }, acceptDownloads: true });
    page.on('pageerror', (error) => { errors.push(error.message); console.error(error); });
    await page.route('https://**/*', (r) => remote && new URL(r.request().url()).origin === new URL(remote).origin ? r.continue() : r.abort());
    await check(page, remote || 'http://127.0.0.1:' + server.address().port);
    assert.deepEqual(errors, []);
    console.log(label + ': pruebas aprobadas.');
  } finally {
    if (browser) await browser.close();
    if (!remote) server.close();
  }
}

module.exports = { runControls, startControls, expect, assert };
