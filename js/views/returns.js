/* Proceso operacional secundario: devoluciones y envases retornables (M8).
   Listado, detalle, creación y flujo de aprobación visual. */
(function (L) {
  const { esc, icon, $, $$, data: D, fmt } = L;
  const FLOW = ['Registrada en ruta', 'Recepcionada en andén', 'En evaluación', 'Aprobada', 'Nota de crédito emitida'];
  const kind = (e) => ({ 'Registrada en ruta': 'info', 'Recepcionada en andén': 'info', 'En evaluación': 'warning', Aprobada: 'success', Rechazada: 'danger', 'Nota de crédito emitida': 'success' }[e]);

  L.route('/devoluciones', {
    title: 'Devoluciones y envases', parent: '/inicio', block: 'Proceso operacional secundario', module: 'M8 Devoluciones y envases', rf: ['RF-08.01', 'RF-08.02', 'RF-08.03', 'RF-08.06', 'RF-17.12', 'RNG-07'], actors: ['Conductores', 'Jefa de Bodega', 'Gerente de Finanzas'],
    render: () => `<div class="page-head"><div class="titles"><h1>Devoluciones y envases</h1><p class="muted" style="margin:0">Desde el registro en ruta hasta la nota de crédito, con decisión de destino aprobada.</p></div><div class="actions">${L.can('dev.registrar') ? `<a class="btn btn-primary" href="#/devoluciones/nueva">${icon('plus')}Registrar devolución</a>` : ''}</div></div>
      ${L.tabsHtml('dv', [{ id: 'dev', label: 'Devoluciones', count: D.devoluciones.length }, { id: 'env', label: 'Envases retornables' }], 'dev')}
      <div ${L.panelAttrs('dv', 'dev', 'dev')}>
        <div class="grid grid-4" style="margin-bottom:var(--sp-5)">${FLOW.slice(0, 4).map((e) => `<button type="button" class="card card-link kpi" data-fe="${esc(e)}" style="text-align:left;font:inherit;color:inherit;cursor:pointer"><span class="label">${esc(e)}</span><span class="value" style="font-size:var(--fs-2xl)">${D.devoluciones.filter((d) => d.estado === e).length}</span></button>`).join('')}</div>
        <div class="card card-flush" id="dv-t"></div></div>
      <div ${L.panelAttrs('dv', 'env', 'dev')}>
        <div class="grid grid-3" style="margin-bottom:var(--sp-5)"><div class="card kpi"><span class="label">Canastillos en clientes</span><span class="value">68.000</span><span class="meta">Parque total controlado por tipo</span></div><div class="card kpi"><span class="label">Pallets en clientes</span><span class="value">9.400</span></div><div class="card kpi"><span class="label">Pérdida anual estimada</span><span class="value" style="color:var(--c-danger)">14 %</span><span class="meta">Línea base 2025 del caso</span></div></div>
        <div class="grid grid-2"><section class="card"><div class="card-head"><h2>Saldo de envases por cliente</h2>${L.tip('Saldo = inicial conciliado + entregados − devueltos ± ajustes autorizados.')}</div>${L.charts.hbar(D.clientes.slice().sort((a, b) => b.envases.canastillos - a.envases.canastillos).slice(0, 7).map((c) => ({ label: c.nombre.slice(0, 20), value: c.envases.canastillos, color: c.envases.canastillos > 40 ? 'var(--c-danger)' : undefined, drill: '/clientes/' + c.id })), { label: 'Canastillos por cliente' })}<p class="small muted">En rojo: sobre el umbral de 40 canastillos (alerta al preventista).</p></section>
        <section class="card"><div class="card-head"><h2>Pérdida por zona y tipo</h2></div>${L.charts.stacked(['Talca', 'Curicó', 'Linares', 'Cauquenes', 'Chillán'], [{ name: 'Canastillos', values: [420, 310, 280, 190, 350] }, { name: 'Pallets', values: [38, 22, 19, 12, 30] }], { label: 'Envases perdidos por zona' })}${L.charts.legend([{ label: 'Canastillos' }, { label: 'Pallets' }])}</section></div></div>`,
    mount: (root) => {
      L.tabs($('.tabs', root));
      const tbl = L.dataTable($('#dv-t', root), {
        id: 'dvl', caption: 'Devoluciones', rows: ['conductor', 'conductor-ext'].includes(L.me()?.id) ? D.devoluciones.filter((d) => D.pedidos.find((p) => p.id === d.pedido)?.ruta === L.fieldRoute().id) : D.devoluciones, searchKeys: ['id', 'clienteNombre', 'producto', 'pedido', 'lote'], searchPlaceholder: 'Buscar por folio, cliente, producto o lote',
        filters: [{ key: 'estado', label: 'Estado', options: [...FLOW, 'Rechazada'] }, { key: 'motivo', label: 'Motivo', options: D.motivosDevolucion }],
        sort: 'id', dir: 'desc', selectable: true,
        columns: [
          { key: 'id', label: 'Folio', render: (r) => `<a class="row-link mono" href="#/devoluciones/${r.id}">${r.id}</a>` },
          { key: 'clienteNombre', label: 'Cliente' },
          { key: 'producto', label: 'Producto', render: (r) => `${esc(r.producto)}<div class="small muted mono">Lote ${r.lote}</div>` },
          { key: 'cant', label: 'Cant.', right: true },
          { key: 'motivo', label: 'Motivo', wrap: true },
          { key: 'fecha', label: 'Fecha', render: (r) => fmt.dateShort(r.fecha) },
          { key: 'estado', label: 'Estado', render: (r) => L.badge(r.estado, kind(r.estado)) }
        ],
        rowActions: (r, redraw) => [{ label: 'Ver detalle', icon: 'eye', onClick: () => L.go('/devoluciones/' + r.id) }, ...(r.estado === 'En evaluación' && L.can('dev.destino') ? [{ label: 'Aprobar destino', icon: 'check', onClick: () => L.go('/devoluciones/' + r.id) }] : []), ...(L.allowed('/pedidos') ? [{ label: 'Ver pedido de origen', icon: 'clipboard', onClick: () => L.go('/pedidos/' + r.pedido) }] : [])],
        bulkActions: [...(!L.can('dev.destino') ? [] : [{ label: 'Aprobar seleccionadas', icon: 'check', onClick: async (ids, done) => { const ev = D.devoluciones.filter((d) => ids.includes(d.id) && d.estado === 'En evaluación'); if (!ev.length) { L.toast('Nada que aprobar', 'Solo se aprueban devoluciones «En evaluación».', 'warning'); return; } if (await L.confirm({ title: `¿Aprobar ${ev.length} devolución(es)?`, message: 'Se asignará el destino «Reingreso a stock» y se enviará la transacción al ERP.', confirmLabel: 'Aprobar' })) { ev.forEach((d) => { d.estado = 'Aprobada'; d.destino = 'Reingreso a stock'; }); done(); L.toast('Devoluciones aprobadas', `${ev.length} folio(s) actualizados.`, 'success'); } } }]), { label: 'Exportar', icon: 'download', onClick: (ids) => { L.download('devoluciones.csv', L.toCSV(D.devoluciones.filter((d) => ids.includes(d.id)), [{ label: 'Folio', key: 'id' }, { label: 'Cliente', key: 'clienteNombre' }, { label: 'Producto', key: 'producto' }, { label: 'Estado', key: 'estado' }])); } }]
      });
      $$('[data-fe]', root).forEach((b) => (b.onclick = () => { tbl.state.filters.estado = b.dataset.fe; $('#dvl-f-estado', root).value = b.dataset.fe; tbl.draw(); L.announce(`Filtrado por ${b.dataset.fe}`); }));
    }
  });

  L.route('/devoluciones/nueva', {
    permission: 'dev.registrar',
    title: 'Registrar devolución', parent: '/devoluciones', block: 'Proceso operacional secundario', module: 'M8 Devoluciones y envases', rf: ['RF-08.01', 'RF-06.09', 'RNG-06'], actors: ['Conductores', 'Jefa de Bodega'],
    render: () => `<div class="page-head"><div class="titles"><h1>Registrar devolución</h1><p class="muted" style="margin:0">Se captura en la entrega, aun sin señal; el producto se evalúa antes de habilitarlo para la venta.</p></div></div>
      <form class="split" id="nd" novalidate><div class="card stack-lg">
        <div class="form-grid">
          <div class="field combo full"><label for="nd-cli">Cliente <span class="req" aria-hidden="true">*</span></label><div class="input-wrap">${icon('store')}<input id="nd-cli" class="input" placeholder="Escriba el nombre del cliente" required></div></div>
          <div class="field"><label for="nd-ped">Pedido de origen <span class="req" aria-hidden="true">*</span></label><select id="nd-ped" class="select" required disabled><option value="">Primero elija el cliente</option></select></div>
          <div class="field"><label for="nd-fecha">Fecha y hora</label><input id="nd-fecha" class="input" type="datetime-local" value="2026-11-13T09:45"></div>
          <div class="field combo full"><label for="nd-sku">Producto <span class="req" aria-hidden="true">*</span></label><div class="input-wrap">${icon('box')}<input id="nd-sku" class="input" placeholder="Nombre o SKU" required></div></div>
          <div class="field"><label for="nd-cant">Cantidad <span class="req" aria-hidden="true">*</span></label><input id="nd-cant" class="input num" type="number" min="1" required></div>
          <div class="field"><label for="nd-lote">Lote <span id="nd-lote-req" class="req" aria-hidden="true" hidden>*</span></label><input id="nd-lote" class="input mono" placeholder="L2611-47"><span class="hint" id="nd-lote-h">Obligatorio para productos con trazabilidad.</span></div>
          <fieldset class="full"><legend>Motivo <span class="req" aria-hidden="true">*</span></legend><div class="options-row" id="nd-mot">${D.motivosDevolucion.map((m, i) => `<label class="radio"><input type="radio" name="nd-mot" value="${esc(m)}" ${i === 0 ? 'checked' : ''}> ${esc(m)}</label>`).join('')}</div></fieldset>
          <div class="field full"><label for="nd-obs">Observación</label><textarea id="nd-obs" class="textarea" maxlength="300" placeholder="Describa el estado del producto"></textarea></div>
        </div>
        <div><span style="font-weight:600;font-size:var(--fs-sm)">Fotos del producto</span><div class="dropzone" id="nd-drop" style="margin-top:6px">${icon('camera', 'icon-lg')}<div><strong>Arrastre las fotos aquí</strong> o haga clic para adjuntarlas</div><span class="small">JPG o PNG · máx. 8 MB</span></div><button type="button" class="btn btn-tertiary btn-sm" id="nd-fake" style="margin-top:6px">Usar foto de ejemplo</button></div>
        <fieldset><legend>Envases retornados en la misma visita</legend><div class="form-grid"><div class="field"><label for="nd-can">Canastillos</label><input id="nd-can" class="input num" type="number" min="0" value="0"></div><div class="field"><label for="nd-pal">Pallets</label><input id="nd-pal" class="input num" type="number" min="0" value="0"></div></div></fieldset>
      </div>
      <aside class="card stack"><h2>Resumen</h2><dl class="desc-list" id="nd-sum"><dt>Cliente</dt><dd>—</dd><dt>Producto</dt><dd>—</dd><dt>Monto estimado</dt><dd>—</dd></dl>${L.alert('info', 'Qué pasa después', 'Bodega recepciona en andén, Calidad evalúa y Bodega decide el destino. Si corresponde, el ERP emite la nota de crédito.')}<button type="submit" class="btn btn-primary big-btn">${icon('check')}Registrar devolución</button><a class="btn btn-tertiary" href="#/devoluciones">Cancelar</a></aside></form>`,
    mount: (root) => {
      const f = $('#nd', root);
      let cli = null, prod = null;
      const cliIn = $('#nd-cli', root), ped = $('#nd-ped', root), sku = $('#nd-sku', root), lote = $('#nd-lote', root), cant = $('#nd-cant', root);
      const sum = () => { $('#nd-sum', root).innerHTML = `<dt>Cliente</dt><dd>${esc(cli?.nombre || '—')}</dd><dt>Pedido</dt><dd class="mono">${esc(ped.value || '—')}</dd><dt>Producto</dt><dd>${esc(prod?.nombre || '—')}</dd><dt>Cantidad</dt><dd>${esc(cant.value || '—')}</dd><dt>Monto estimado</dt><dd class="num">${prod && cant.value ? fmt.clp(prod.precio * cant.value) : '—'}</dd>`; };
      L.bindField(cliIn, [(v) => (cli && cli.nombre === v ? '' : 'Elija un cliente de la lista.')]);
      L.combobox(cliIn, () => D.clientes.map((c) => ({ label: c.nombre, meta: c.comuna, c })), { onSelect: (it) => { cli = it.c; ped.disabled = false; ped.innerHTML = `<option value="">Seleccione…</option>${D.pedidos.filter((p) => p.cliente === cli.id).concat(D.pedidos.slice(0, 2)).slice(0, 4).map((p) => `<option>${p.id}</option>`).join('')}`; cliIn._validate(); sum(); } });
      L.bindField(ped, ['required']);
      ped.onchange = sum;
      L.bindField(sku, [(v) => (prod && prod.nombre === v ? '' : 'Elija un producto de la lista.')]);
      L.combobox(sku, () => D.productos.map((p) => ({ label: p.nombre, meta: `${p.sku} · ${p.temp}`, p })), { onSelect: (it) => { prod = it.p; sku._validate(); $('#nd-lote-req', root).hidden = !prod.trazable; $('#nd-lote-h', root).textContent = prod.trazable ? 'Este producto exige lote (trazabilidad obligatoria).' : 'Opcional para este producto.'; sum(); } });
      L.bindField(cant, ['positive']);
      cant.oninput = sum;
      L.bindField(lote, [(v) => (prod?.trazable ? L.validators.lot(v) : '')]);
      const dz = L.dropzone($('#nd-drop', root), { accept: 'image/*', maxMB: 8 });
      $('#nd-fake', root).onclick = async () => dz.add([await L.fakeFile('devolucion.png')]);
      f.onsubmit = (e) => {
        e.preventDefault();
        if (!L.can('dev.registrar')) return;
        if (!L.validateAll(f)) { L.toast('Revise el formulario', 'Hay campos obligatorios sin completar o con errores.', 'error'); return; }
        L.busy($('[type=submit]', f), () => {
          const id = 'DV-' + (5531 + Math.floor(Math.random() * 40));
          D.devoluciones.unshift({ id, pedido: ped.value, cliente: cli.id, clienteNombre: cli.nombre, sku: prod.sku, producto: prod.nombre, temp: prod.temp, cant: +cant.value, lote: lote.value || '—', motivo: $('[name=nd-mot]:checked', root).value, estado: 'Registrada en ruta', fecha: new Date().toISOString(), conductor: 'Jonathan Curihual', monto: prod.precio * cant.value, destino: '' });
          L.toast('Devolución registrada', `${id}${L.online() ? '' : ' · guardada en el dispositivo'}`, 'success', { action: 'Ver', onAction: () => L.go('/devoluciones/' + id) });
          L.go('/devoluciones/' + id);
        }, 900);
      };
    }
  });

  L.route('/devoluciones/:id', {
    title: (p) => p.id || 'Detalle de devolución', parent: '/devoluciones', block: 'Proceso operacional secundario', module: 'M8 Devoluciones y envases', rf: ['RF-08.02', 'RF-17.06'], actors: ['Jefa de Bodega', 'Jefa de Calidad', 'Gerente de Finanzas'],
    render: ({ id }) => {
      const d = D.devoluciones.find((x) => x.id === id);
      if (!d) return L.empty('search', 'Devolución no encontrada', `No existe el folio ${id}.`, '<a class="btn btn-primary" href="#/devoluciones">Volver</a>');
      const cur = d.estado === 'Rechazada' ? 3 : FLOW.indexOf(d.estado);
      const who = ['Conductor · ' + d.conductor, 'Jefa de Bodega · andén CD Talca', 'Jefa de Calidad · evaluación sanitaria', 'Jefa de Bodega · decide destino', 'ERP · nota de crédito'];
      return `<div class="page-head"><div class="titles"><span class="page-kicker">Devolución</span><h1 class="mono">${esc(d.id)}</h1><p class="muted" style="margin:0">${esc(d.clienteNombre)} · pedido <a href="#/pedidos/${d.pedido}">${esc(d.pedido)}</a> · ${L.badge(d.estado, kind(d.estado))}</p></div></div>
        <section class="card" style="margin-bottom:var(--sp-5)"><div class="card-head"><h2>Flujo de aprobación</h2><span class="small muted">Responsables y plazos configurables</span></div>
          <ol class="stepper" aria-label="Flujo de aprobación">${FLOW.map((s, i) => `<li class="${d.estado === 'Rechazada' && i === 3 ? 'error' : i < cur || (i === cur && d.estado === 'Nota de crédito emitida') ? 'done' : i === cur ? 'current' : ''}"><div class="step" ${i === cur ? 'aria-current="step"' : ''}><span class="bar"></span><span class="lbl">${esc(d.estado === 'Rechazada' && i === 3 ? 'Rechazada' : s)}</span><span class="small muted">${esc(who[i])}</span></div></li>`).join('')}</ol>
          <div id="dv-act"></div></section>
        <div class="split"><section class="card"><div class="card-head"><h2>Detalle</h2></div><dl class="desc-list"><dt>Producto</dt><dd>${esc(d.producto)} <span class="mono small muted">${d.sku}</span></dd><dt>Lote</dt><dd class="mono"><a href="#/calidad">${esc(d.lote)}</a></dd><dt>Cantidad</dt><dd>${d.cant} u</dd><dt>Motivo</dt><dd>${esc(d.motivo)}</dd><dt>Monto</dt><dd class="num">${fmt.clp(d.monto)}</dd><dt>Registrada</dt><dd>${fmt.dt(d.fecha)} por ${esc(d.conductor)}</dd>${d.destino ? `<dt>Destino</dt><dd>${esc(d.destino)}</dd>` : ''}</dl></section>
          <section class="card"><div class="card-head"><h2>Evidencia</h2></div><div class="row"><div class="skeleton" style="width:120px;height:90px;border-radius:8px" aria-label="Foto de la devolución" role="img"></div><div class="skeleton" style="width:120px;height:90px;border-radius:8px" role="img" aria-label="Foto del lote"></div></div><p class="small muted" style="margin-top:8px">2 fotos capturadas en la entrega.</p></section></div>`;
    },
    mount: (root, { id }) => {
      const d = D.devoluciones.find((x) => x.id === id);
      if (!d) return;
      const host = $('#dv-act', root);
      const advance = (to, msg) => { d.estado = to; L.toast(msg, d.id, 'success'); L.router.resolve(); };
      const act = { 'Registrada en ruta': 'dev.recepcionar', 'Recepcionada en andén': 'dev.recepcionar', 'En evaluación': 'dev.destino', Aprobada: 'dev.nc' }[d.estado];
      if (act && !L.can(act)) host.innerHTML = L.readOnly(`El siguiente paso lo ejecuta ${act === 'dev.nc' ? 'Finanzas, que solicita la nota de crédito al ERP' : 'la Jefa de Bodega'}.`);
      else if (d.estado === 'Registrada en ruta') host.innerHTML = `<div class="row" style="justify-content:flex-end"><button type="button" class="btn btn-primary" id="a1">${icon('download')}Recepcionar en andén</button></div>`;
      else if (d.estado === 'Recepcionada en andén') host.innerHTML = `<div class="row" style="justify-content:flex-end"><button type="button" class="btn btn-primary" id="a2">${icon('shield')}Enviar a evaluación de Calidad</button></div>`;
      else if (d.estado === 'En evaluación') host.innerHTML = `<form id="a3" class="stack" novalidate style="border-top:1px solid var(--c-line-soft);padding-top:var(--sp-4)"><h3>Decisión de destino</h3><fieldset><legend class="sr-only">Destino</legend><div class="options-row">${['Reingreso a stock', 'Merma', 'Devolución a proveedor', 'Venta con descuento'].map((x, i) => `<label class="radio"><input type="radio" name="dest" value="${x}" ${i === 0 ? 'checked' : ''}> ${x}</label>`).join('')}</div></fieldset><div class="field"><label for="a3-c">Justificación <span class="req" aria-hidden="true">*</span></label><textarea id="a3-c" class="textarea" required placeholder="Estado del producto y criterio aplicado"></textarea></div><div class="row" style="justify-content:flex-end"><button type="button" class="btn btn-secondary" id="a3-rej">${icon('x')}Rechazar devolución</button><button type="submit" class="btn btn-primary">${icon('check')}Aprobar destino</button></div></form>`;
      else if (d.estado === 'Aprobada') host.innerHTML = `<div class="row" style="justify-content:flex-end"><button type="button" class="btn btn-primary" id="a4">${icon('file')}Solicitar nota de crédito al ERP</button></div>`;
      else host.innerHTML = L.alert(d.estado === 'Rechazada' ? 'danger' : 'success', d.estado === 'Rechazada' ? 'Devolución rechazada' : 'Flujo cerrado', d.estado === 'Rechazada' ? 'Se informó al cliente y al conductor.' : `Nota de crédito NC-${d.id.slice(3)} emitida y transferida al ERP.`);
      $('#a1', root) && ($('#a1', root).onclick = (e) => L.busy(e.currentTarget, () => advance('Recepcionada en andén', 'Recepcionada en andén')));
      $('#a2', root) && ($('#a2', root).onclick = (e) => L.busy(e.currentTarget, () => advance('En evaluación', 'Enviada a Calidad')));
      if ($('#a3', root)) {
        L.bindField($('#a3-c', root), ['required']);
        $('#a3', root).onsubmit = (e) => { e.preventDefault(); if (!L.validateAll(e.target)) return; d.destino = $('[name=dest]:checked', root).value; const cl = L.findClient(d.cliente); L.busy($('#a3 [type=submit]', root), () => advance('Aprobada', cl ? `Destino «${d.destino}» aprobado · costo de servir de ${cl.nombre}: ${fmt.pct(cl.costoServir)}` : 'Destino aprobado')); };
        $('#a3-rej', root).onclick = async () => { if (await L.confirm({ title: '¿Rechazar la devolución?', message: 'El producto vuelve al cliente o se gestiona como merma del transporte. Esta decisión queda auditada.', confirmLabel: 'Rechazar', danger: true })) advance('Rechazada', 'Devolución rechazada'); };
      }
      $('#a4', root) && ($('#a4', root).onclick = (e) => L.busy(e.currentTarget, () => advance('Nota de crédito emitida', 'Nota de crédito emitida'), 1400));
    }
  });
})(window.LFX);
