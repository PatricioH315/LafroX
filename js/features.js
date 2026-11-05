/* Prioridad 3: comportamiento transversal del prototipo, sin servicios externos. */
(function (L) {
  const { $, $$, esc } = L;
  const clients = ['cliente', 'cliente-moderno'];
  const clientSession = () => clients.includes(L.session()?.profile);
  L.idleLimit = () => Number(L.data.parametros.flatMap((g) => g.items).find((p) => p.id === 'inact').valor) * 60000;
  L.checkInactivity = (now = Date.now()) => {
    const s = L.session();
    if (!clientSession()) return false;
    const last = s.lastActivity ?? s.at;
    // Una sesión sin marca de tiempo empieza a contar ahora, en vez de cerrarse de inmediato
    if (last == null) { L.setSession({ ...s, lastActivity: now }); return false; }
    if (now - last < L.idleLimit()) return false;
    // Cierra también diálogos para que no quede contenido del cliente sobre el acceso.
    document.dispatchEvent(new Event('lfx:session-expired'));
    document.body.style.overflow = '';
    L.setSession(null);
    L.go('/ingresar');
    L.toast('Sesión cerrada por inactividad', 'Vuelva a ingresar para continuar.', 'warning');
    return true;
  };
  const activity = () => {
    if (L.checkInactivity() || !clientSession()) return;
    L.setSession({ ...L.session(), lastActivity: Date.now() });
  };
  ['pointerdown', 'keydown', 'scroll'].forEach((ev) => document.addEventListener(ev, activity, { passive: true, capture: true }));
  document.addEventListener('visibilitychange', () => { if (!document.hidden) L.checkInactivity(); });
  setInterval(() => L.checkInactivity(), 1000);
  const resolve = L.router.resolve.bind(L.router);
  L.router.resolve = () => { if (!L.checkInactivity()) resolve(); };

  // Un borrador por perfil y flujo; nunca dispara el envío de la transacción.
  L.draftKey = (flow) => `draft.${L.session()?.profile}.${flow}`;
  L.registerDraft = (save) => { L.saveDraft = save; L.onLeave(() => { L.saveDraft = null; }); };
  const render = L.render;
  L.render = (route, params, query, path) => {
    document.documentElement.dataset.portalLight = path.startsWith('/portal/') && L.store.pref('portalLight', 'off') === 'on' ? 'on' : 'off';
    return render(route, params, query, path);
  };

  // Tablas manuales: exporta filas actuales; dataTable usa todos los datos filtrados.
  L.enableTableExports = (root = document) => {
    $$('table.table', root).forEach((table) => {
      if (table.dataset.jsonExport || table.closest('[data-managed-table]')) return;
      table.dataset.jsonExport = 'true';
      const btn = document.createElement('button');
      btn.type = 'button'; btn.className = 'btn btn-secondary btn-sm table-json';
      const caption = $('caption', table)?.textContent || 'Tabla';
      btn.textContent = 'Exportar JSON'; btn.setAttribute('aria-label', `Exportar JSON: ${caption}`);
      (table.closest('.table-wrap') || table).before(btn);
      btn.onclick = () => {
        const headings = $$('thead th', table).map((th, i) => th.textContent.trim() || `Columna ${i + 1}`);
        const rows = $$('tbody tr', table).map((tr) => Object.fromEntries($$('td', tr).map((td, i) => {
          const input = $('input,select,textarea', td);
          const value = input ? input.type === 'checkbox' ? input.checked : input.value : td.textContent.trim();
          return [`${i + 1}. ${headings[i] || 'Valor'}`, value];
        })));
        L.download('tabla.json', JSON.stringify({ tabla: caption, filas: rows }, null, 2), 'application/json');
      };
    });
  };
  const observeTables = new MutationObserver(() => L.enableTableExports());
  observeTables.observe(document.getElementById('app'), { childList: true, subtree: true });

  L.signDocument = (doc) => {
    L.modal({
      title: 'Firma electrónica · demostración',
      body: `<p>Documento: <strong>${esc(doc)}</strong></p>${L.alert('info', 'Simulación sin validez legal', 'No se contacta a un prestador ni se usa un certificado real. El sello de tiempo es local y la evidencia dura solo esta sesión.')}
        <div class="field"><label for="sig-mode">Modalidad</label><select class="select" id="sig-mode"><option value="simple">Firma electrónica simple</option><option value="advanced">Firma electrónica avanzada simulada</option></select></div>
        <div class="field"><label for="sig-cert">Certificado de prueba (modalidad avanzada)</label><select class="select" id="sig-cert"><option value="valid">DEMO-001 · vigente</option><option value="expired">DEMO-002 · vencido</option><option value="revoked">DEMO-003 · revocado</option></select></div>
        <label class="check"><input type="checkbox" id="sig-consent"> He leído el documento y acepto firmarlo en esta demostración.</label><p id="sig-error" class="field-error" role="alert"></p>`,
      actions: [{ label: 'Cancelar' }, { label: 'Firmar', cls: 'btn-primary', onClick: (api) => {
        const advanced = $('#sig-mode', api.el).value === 'advanced', cert = $('#sig-cert', api.el).value;
        const error = !$('#sig-consent', api.el).checked ? 'Debe aceptar el documento antes de firmar.' : advanced && cert !== 'valid' ? 'Certificado no válido: firma bloqueada. Seleccione uno vigente.' : '';
        if (error) { $('#sig-error', api.el).textContent = error; return false; }
        const evidence = { simulacion: true, documento: doc, firmante: L.me().name, modalidad: advanced ? 'Avanzada simulada' : 'Simple simulada', certificado: advanced ? 'DEMO-001' : null, validacion: advanced ? 'Vigente (simulada)' : 'No requiere certificado en esta demostración', selloTiempoLocal: new Date().toISOString(), id: L.uid('firma') };
        const key = `signatures.${L.session().profile}`;
        L.store.set(key, [...L.store.get(key, []), evidence]);
        api.close();
        L.showSignature(evidence);
        return false;
      } }]
    });
  };
  L.showSignature = (evidence) => L.modal({ title: 'Evidencia de firma simulada', body: `<dl class="desc-list">${Object.entries(evidence).map(([k, v]) => `<dt>${esc(k)}</dt><dd class="wrap">${esc(v ?? 'No aplica')}</dd>`).join('')}</dl><p class="hint">Sin validez legal. No constituye una firma avanzada real ni un sello de tiempo de un tercero.</p>`, actions: [{ label: 'Descargar evidencia JSON', cls: 'btn-primary', onClick: () => L.download('firma-simulada.json', JSON.stringify(evidence, null, 2), 'application/json') }, { label: 'Cerrar' }] });
})(window.LFX);
