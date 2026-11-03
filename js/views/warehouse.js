/* Bodega: recepción GS1 (M1) e inventario con FEFO y ocupación (M2). */
(function (L) {
  const { esc, icon, $, $$, data: D, fmt } = L;

  L.route('/recepcion', {
    title: 'Recepción', parent: '/inicio', block: 'Proceso operacional principal', module: 'M1 Recepción', rf: ['RF-01.01', 'RF-01.09', 'RF-12.23'], actors: ['Jefa de Bodega', 'Preparador', 'Proveedor'],
    render: () => `<div class="page-head"><div class="titles"><h1>Recepción de proveedores</h1><p class="muted" style="margin:0">Órdenes de compra programadas por andén. Cada lote queda registrado al ingresar.</p></div><div class="actions"><a class="btn btn-primary" href="#/recepcion/nueva">${icon('scan')}Registrar recepción</a></div></div>
      <div class="card card-flush" id="oc-t"></div>`,
    mount: (root) => L.dataTable($('#oc-t', root), {
      id: 'oc', caption: 'Órdenes de compra', rows: D.ocs, searchKeys: ['id', 'proveedor'], filters: [{ key: 'estado', label: 'Estado', options: ['Programada', 'En recepción', 'Cerrada'] }],
      columns: [{ key: 'id', label: 'Orden', render: (r) => `<span class="mono">${r.id}</span>` }, { key: 'proveedor', label: 'Proveedor' }, { key: 'lineas', label: 'Líneas', right: true }, { key: 'anden', label: 'Andén' }, { key: 'hora', label: 'Hora' }, { key: 'discrepancias', label: 'Discrepancias', right: true, render: (r) => (r.discrepancias ? L.badge(r.discrepancias + ' alertas', 'warning') : '—') }, { key: 'estado', label: 'Estado', render: (r) => L.badge(r.estado, r.estado === 'Cerrada' ? 'success' : r.estado === 'En recepción' ? 'accent' : 'info') }],
      rowActions: (r) => [{ label: r.estado === 'Cerrada' ? 'Ver comparativo' : 'Recepcionar', icon: 'scan', onClick: () => L.go('/recepcion/nueva') }]
    })
  });

  L.route('/recepcion/nueva', {
    title: 'Registrar recepción', parent: '/recepcion', block: 'Proceso operacional principal', module: 'M1 Recepción', rf: ['RF-01.01', 'RF-01.02', 'RF-01.03', 'RF-01.04', 'RF-01.05', 'RF-01.06', 'RF-01.07', 'RF-01.11'], actors: ['Jefa de Bodega', 'Preparador'],
    render: () => `<div class="page-head"><div class="titles"><span class="page-kicker">OC-88412 · Lácteos del Sur S.A. · andén 3</span><h1>Registrar recepción</h1><p class="muted" style="margin:0">Escanee la etiqueta GS1-128: el sistema interpreta GTIN (01), lote (10), vencimiento (17) y SSCC (00).</p></div></div>
      <div class="split"><form class="card stack-lg" id="rc" novalidate>
        <div class="field"><label for="rc-scan">Lectura GS1</label><div class="row" style="flex-wrap:nowrap"><div class="input-wrap" style="flex:1">${icon('scan')}<input id="rc-scan" class="input mono" placeholder="(01)07801234500017(10)L2611-47(17)261211"></div><button type="button" class="btn btn-secondary" id="rc-sim">Simular lectura</button></div><span class="hint">Pruebe también una lectura sin lote para ver la validación.</span></div>
        <div class="form-grid">
          <div class="field"><label for="rc-sku">Producto <span class="req" aria-hidden="true">*</span></label><select id="rc-sku" class="select"><option value="">Seleccione…</option>${D.productos.filter((p) => p.temp !== 'Seco').map((p) => `<option value="${p.sku}">${esc(p.nombre)}</option>`).join('')}</select></div>
          <div class="field"><label for="rc-q">Cantidad recibida <span class="req" aria-hidden="true">*</span></label><input id="rc-q" class="input num" type="number" min="1"><span class="hint" id="rc-oc">Cantidad en la OC: 1.200</span></div>
          <div class="field"><label for="rc-l">Lote del proveedor <span class="req" aria-hidden="true">*</span></label><input id="rc-l" class="input mono"></div>
          <div class="field"><label for="rc-v">Fecha de vencimiento <span class="req" aria-hidden="true">*</span></label><input id="rc-v" class="input" type="date" min="2026-11-13"></div>
          <div class="field"><label for="rc-z">Ubicación destino</label><select id="rc-z" class="select"><option>R-2-14-3 · cámara refrigerada</option><option>C-1-02-1 · cámara congelada</option><option>A-05-11-2 · seco</option></select></div>
          <div class="field"><label for="rc-t">Temperatura al ingreso (°C)</label><input id="rc-t" class="input num" type="number" step="0.1" value="4.2"></div>
        </div>
        <div id="rc-alerts"></div>
        ${L.accordionHtml('Registrar no conformidad', `<div class="form-grid"><div class="field"><label for="nc-t">Tipo</label><select id="nc-t" class="select"><option>Embalaje dañado</option><option>Temperatura fuera de rango</option><option>Etiqueta ilegible</option><option>Producto distinto al pedido</option></select></div><div class="field"><label for="nc-q">Unidades afectadas</label><input id="nc-q" class="input num" type="number" min="0" value="0"></div><div class="full"><div class="dropzone" id="nc-ph" style="min-height:90px">${icon('camera')}<span>Foto de la no conformidad</span></div></div></div><p class="hint">Al confirmar, la cantidad afectada pasa a «Cuarentena» y se notifica a Calidad (RF-01.05).</p>`)}
        <div class="row" style="justify-content:flex-end"><button type="submit" class="btn btn-primary big-btn">${icon('check')}Confirmar pallet y generar SSCC</button></div>
      </form>
      <aside class="card stack"><h2>Comparativo OC vs. recibido</h2><ul class="list" id="rc-cmp">${[['Leche entera · 1 L', 1200, 1200], ['Yogur batido frutilla', 2400, 2304], ['Queso gauda laminado', 600, 0], ['Mantequilla con sal', 480, 0]].map(([n, o, r]) => `<li><span class="grow small">${n}</span><span class="num small">${fmt.n(r)}/${fmt.n(o)}</span>${r && r < o ? L.badge('−' + (o - r), 'warning') : r ? L.badge('OK', 'success') : L.badge('Pendiente')}</li>`).join('')}</ul>${L.alert('info', 'Sin bloquear el cierre', 'Las discrepancias generan alertas pero no impiden cerrar la recepción (RF-01.01).')}</aside></div>`,
    mount: (root) => {
      const f = $('#rc', root);
      const sku = $('#rc-sku', root), lot = $('#rc-l', root), venc = $('#rc-v', root), q = $('#rc-q', root), zone = $('#rc-z', root);
      L.bindField(sku, ['required']);
      L.bindField(q, ['positive']);
      L.bindField(lot, ['lot']);
      L.bindField(venc, [(v) => (!v ? 'Fecha de vencimiento requerida (DD/MM/AAAA).' : v <= '2026-11-13' ? 'El producto ya está vencido: no se puede recibir.' : '')]);
      L.bindField(zone, [(v) => { const p = D.productos.find((x) => x.sku === sku.value); return p && ((p.temp === 'Congelado' && !v.includes('congelada')) || (p.temp === 'Refrigerado' && !v.includes('refrigerada'))) ? `Incompatibilidad térmica: ${p.temp.toLowerCase()} no puede ubicarse en esta zona (RF-01.11).` : ''; }]);
      sku.addEventListener('change', () => zone._validate());
      const parse = (s) => { const m = (k) => (s.match(new RegExp('\\(' + k + '\\)([^(]+)')) || [])[1]; return { gtin: m('01'), lot: m('10'), exp: m('17'), sscc: m('00') }; };
      const apply = (txt) => {
        const g = parse(txt);
        if (!g.gtin) { L.toast('Lectura no reconocida', 'El código no tiene el identificador GTIN (01).', 'error'); return; }
        sku.value = D.productos[9].sku; sku._validate();
        if (g.lot) { lot.value = g.lot; lot._validate(); } else { lot.value = ''; lot._validate(); lot.focus(); }
        if (g.exp) { venc.value = `20${g.exp.slice(0, 2)}-${g.exp.slice(2, 4)}-${g.exp.slice(4, 6)}`; venc._validate(); }
        q.value = q.value || 1200; q._validate();
        L.toast('Etiqueta GS1 interpretada', `GTIN ${g.gtin}${g.lot ? ' · lote ' + g.lot : ' · sin lote'}${g.exp ? ' · vence ' + g.exp : ''}`, g.lot ? 'success' : 'warning');
      };
      let n = 0;
      $('#rc-sim', root).onclick = () => { const s = n++ % 2 === 0 ? '(01)07801234500017(10)L2611-47(17)261211' : '(01)07801234500024(17)261130'; $('#rc-scan', root).value = s; apply(s); };
      $('#rc-scan', root).addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); apply(e.target.value); } });
      q.addEventListener('change', () => { $('#rc-alerts', root).innerHTML = q.value && +q.value !== 1200 ? L.alert('warning', `Discrepancia con la OC: ${q.value > 1200 ? '+' : ''}${q.value - 1200} unidades`, 'Se generará una alerta al cerrar, sin bloquear el cierre.') : ''; });
      L.dropzone($('#nc-ph', root), { accept: 'image/*' });
      f.onsubmit = (e) => {
        e.preventDefault();
        if (!L.validateAll(f)) { L.toast('Revise la recepción', 'Hay datos obligatorios faltantes o incompatibles.', 'error'); return; }
        L.busy($('[type=submit]', f), () => {
          const sscc = '00780123450' + String(Math.floor(Math.random() * 1e8)).padStart(8, '0');
          L.modal({ title: 'Pallet confirmado', icon: 'success:check-circle', body: `<p>SSCC generado bajo GS1-128 y asociado a GTIN, lote, vencimiento y fecha de recepción (RF-01.07).</p><div class="card" style="box-shadow:none;text-align:center"><svg viewBox="0 0 220 60" width="100%" height="60" role="img" aria-label="Código de barras del SSCC">${Array.from({ length: 70 }, (_, i) => `<rect x="${i * 3.1}" y="0" width="${(i * 7) % 3 ? 1.2 : 2.2}" height="60" fill="currentColor"/>`).join('')}</svg><div class="mono" style="margin-top:6px">(00) ${sscc}</div></div>`, actions: [{ label: 'Imprimir etiqueta', cls: 'btn-secondary', icon: 'printer', onClick: () => L.toast('Etiqueta enviada a la impresora del andén', '', 'success') }, { label: 'Siguiente pallet', cls: 'btn-primary', onClick: () => { f.reset(); $$('.field', f).forEach((x) => x.classList.remove('is-invalid', 'is-valid')); } }] });
        }, 900);
      };
    }
  });

  L.route('/inventario', {
    title: 'Inventario', parent: '/inicio', block: 'Proceso operacional principal', module: 'M2 Inventario', rf: ['RF-02.02', 'RF-02.04', 'RF-02.05', 'RF-02.06', 'RF-02.07', 'RF-02.09', 'RF-10.01'], actors: ['Jefa de Bodega', 'Gerente de Operaciones', 'Preventistas'],
    render: () => `<div class="page-head"><div class="titles"><h1>Inventario</h1><p class="muted" style="margin:0">Stock físico, comprometido, disponible y en tránsito por sitio. Disponible = físico habilitado − reservas (RNG-02).</p></div><div class="actions"><button type="button" class="btn btn-secondary" id="iv-cc">${icon('clipboard')}Plan de conteo cíclico</button><button type="button" class="btn btn-primary" id="iv-rep">${icon('cart')}Sugerencia de reposición</button></div></div>
      <div class="grid grid-${D.sitios.length > 4 ? 3 : 4}" style="margin-bottom:var(--sp-5)">${D.sitios.slice(0, 3).map((s) => `<div class="card"><div class="row-between"><strong>${esc(s.nombre)}</strong><span class="num">${s.ocupacion} %</span></div><div class="progress ${s.ocupacion > 80 ? 'danger' : 'dark'}" style="margin:8px 0"><span style="width:${s.ocupacion}%"></span></div>${s.zonas ? `<div class="row small muted">${Object.entries(s.zonas).map(([z, v]) => `<span>${z} ${v} %</span>`).join(' · ')}</div>` : `<span class="small muted">${esc(s.tipo)}</span>`}</div>`).join('')}</div>
      <div class="card card-flush" id="iv-t"></div>`,
    mount: (root) => {
      L.dataTable($('#iv-t', root), {
        id: 'iv', caption: 'Stock por producto', rows: D.productos.map((p) => ({ ...p, disponible: p.stock - p.reservado })), searchKeys: ['sku', 'nombre', 'gtin'], searchPlaceholder: 'Buscar SKU, producto o GTIN', filters: [{ key: 'categoria', label: 'Categoría', options: [...new Set(D.productos.map((p) => p.categoria))] }, { key: 'temp', label: 'Temperatura', options: ['Seco', 'Refrigerado', 'Congelado'] }],
        columns: [{ key: 'sku', label: 'SKU', render: (r) => `<span class="mono">${r.sku}</span>` }, { key: 'nombre', label: 'Producto' }, { key: 'temp', label: 'Zona', render: (r) => L.badge(r.temp, r.temp === 'Seco' ? '' : 'info') }, { key: 'stock', label: 'Físico', right: true, render: (r) => fmt.n(r.stock) }, { key: 'reservado', label: 'Reservado', right: true, render: (r) => fmt.n(r.reservado) }, { key: 'disponible', label: 'Disponible', right: true, render: (r) => `<strong style="color:${r.disponible < 300 ? 'var(--c-danger)' : 'inherit'}">${fmt.n(r.disponible)}</strong>` }, { key: 'transito', label: 'En tránsito', right: true, render: (r) => fmt.n(r.transito) }],
        rowActions: (r) => [{ label: 'Ver lotes FEFO', icon: 'layers', onClick: () => L.modal({ title: `Lotes de ${r.nombre}`, body: `<p class="small muted">Orden de salida FEFO: primero el que vence antes (RNG-10).</p><ol class="list">${[0, 1, 2].map((i) => `<li><span class="avatar dark" style="width:28px;height:28px">${i + 1}</span><span class="grow mono">L26${10 + i}-${30 + i * 7}</span><span class="small">vence ${fmt.date(new Date(2026, 11 + i, 5 + i * 9))}</span><span class="num small">${fmt.n(Math.round(r.stock / (3 - i * 0.5)))} u</span></li>`).join('')}</ol>`, actions: [{ label: 'Cerrar', cls: 'btn-primary' }] }) }, { label: 'Ajuste de inventario', icon: 'edit', onClick: () => L.toast('Ajuste requiere conteo y aprobación', 'Inicie un conteo cíclico de la posición.', 'info') }]
      });
      $('#iv-cc', root).onclick = () => L.modal({ title: 'Plan de conteo cíclico', body: `<p>Noviembre: 1.840 posiciones, priorizando alta rotación y diferencias previas (RF-02.04). Los operarios no ven la cantidad teórica.</p><div class="progress"><span style="width:46%"></span></div><p class="small muted" style="margin-top:6px">46 % completado · diferencia acumulada 0,9 % (línea base 2,3 %)</p>`, actions: [{ label: 'Cerrar' }, { label: 'Asignar conteos de hoy', cls: 'btn-primary', onClick: () => L.toast('Conteos asignados', '62 posiciones a 3 operarios.', 'success') }] });
      $('#iv-rep', root).onclick = () => L.modal({ title: 'Sugerencia de reposición', size: 'lg', body: `<p class="muted">Calculada con historia de venta y promociones comprometidas (RF-10.01, RF-10.02). Revise y apruebe para enviarla al ERP.</p><div class="table-wrap"><table class="table"><thead><tr><th>Producto</th><th>Proveedor</th><th class="right">Sugerido</th><th>Motivo</th></tr></thead><tbody>${D.productos.slice(0, 6).map((p, i) => `<tr><td>${esc(p.nombre)}</td><td>${['Molinos del Maule', 'Bebidas Andinas', 'Lácteos del Sur S.A.'][i % 3]}</td><td class="num right"><input class="input num" style="width:90px;text-align:right" value="${(i + 2) * 120}" aria-label="Cantidad sugerida de ${esc(p.nombre)}"></td><td>${i === 2 ? L.badge('Promoción 3×2 comprometida', 'accent') : 'Cobertura bajo 7 días'}</td></tr>`).join('')}</tbody></table></div>`, actions: [{ label: 'Cancelar' }, { label: 'Aprobar y enviar al ERP', cls: 'btn-primary', onClick: () => L.toast('Sugerencia aprobada', 'Traspasada al módulo de compras del ERP (RF-10.03).', 'success') }] });
    }
  });
})(window.LFX);
