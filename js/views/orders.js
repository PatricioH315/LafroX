/* Operación: pedidos (M3), rutas (M4), preparación (M5) y cobranza y rendición (M7). */
(function (L) {
  const { esc, icon, $, $$, data: D, fmt } = L;

  /* ---------- Pedidos ---------- */
  L.route('/pedidos', {
    title: 'Pedidos', parent: '/inicio', block: 'Proceso operacional principal', module: 'M3 Preventa', rf: ['RF-03.03', 'RF-03.16', 'RF-17.12'], actors: ['Preventista', 'Gerente Comercial', 'Gerente de Operaciones', 'Planificador de Rutas'],
    render: () => `<div class="page-head"><div class="titles"><h1>Pedidos</h1><p class="muted" style="margin:0">Preventa, portal de clientes y EDI en un solo listado, con su estado en el proceso.</p></div>
      <div class="actions"><button type="button" class="btn btn-secondary" id="pd-exp">${icon('download')}Exportar CSV</button><a class="btn btn-primary" href="#/flujo">${icon('plus')}Nuevo pedido</a></div></div>
      <div class="grid grid-4" style="margin-bottom:var(--sp-5)" id="pd-kpi"></div>
      <div class="card card-flush" id="pd-t"></div>`,
    mount: (root, p, q) => {
      const counts = (e) => D.pedidos.filter((x) => x.estado === e).length;
      $('#pd-kpi', root).innerHTML = [['Por validar', counts('Pendiente de validación') + counts('Capturado sin conexión'), 'sync'], ['Retenidos', counts('Retenido'), 'alert'], ['En ruta', counts('En ruta'), 'truck'], ['Entregados hoy', counts('Entregado') + counts('Rendido'), 'check-circle']].map(([t, v, i]) => `<div class="card kpi" style="padding:var(--sp-4)"><span class="label">${icon(i, 'icon-sm')}${t}</span><span class="value" style="font-size:var(--fs-2xl)">${v * 17}</span></div>`).join('');
      const tbl = L.dataTable($('#pd-t', root), {
        id: 'pd', caption: 'Listado de pedidos', rows: D.pedidos, searchKeys: ['id', 'clienteNombre', 'comuna', 'preventista'], searchPlaceholder: 'Buscar por pedido, cliente o comuna',
        filters: [{ key: 'estado', label: 'Estado', options: D.estadosPedido }, { key: 'canal', label: 'Canal', options: ['Tradicional', 'Food service', 'Moderno'] }, { key: 'origen', label: 'Origen', options: ['Preventa', 'Portal', 'EDI'] }],
        sort: 'id', dir: 'desc', selectable: true,
        columns: [
          { key: 'id', label: 'Pedido', render: (r) => `<a class="row-link mono" href="#/pedidos/${r.id}">${r.id}</a>` },
          { key: 'clienteNombre', label: 'Cliente', render: (r) => `${esc(r.clienteNombre)}<div class="small muted">${esc(r.comuna)}</div>` },
          { key: 'canal', label: 'Canal' },
          { key: 'origen', label: 'Origen', render: (r) => L.badge(r.origen, r.origen === 'EDI' ? 'dark' : '') },
          { key: 'entrega', label: 'Entrega', render: (r) => `${fmt.dateShort(r.entrega)}<div class="small muted">${esc(r.ventana)}</div>`, sortVal: (r) => r.entrega },
          { key: 'total', label: 'Total', right: true, render: (r) => fmt.clp(r.total) },
          { key: 'estado', label: 'Estado', render: (r) => L.estadoBadge(r.estado) }
        ],
        rowActions: (r, redraw) => [
          { label: 'Ver detalle', icon: 'eye', onClick: () => L.go('/pedidos/' + r.id) },
          { label: 'Ver en el flujo', icon: 'activity', onClick: () => L.go('/flujo') },
          { label: 'Duplicar pedido', icon: 'copy', onClick: () => L.toast('Pedido duplicado', `Borrador creado a partir de ${r.id}.`, 'success') },
          { sep: true },
          { label: 'Anular pedido', icon: 'ban', danger: true, onClick: async () => { if (await L.confirm({ title: `¿Anular ${r.id}?`, message: 'Se liberará el stock reservado y se avisará al cliente. Queda registrado en la auditoría.', confirmLabel: 'Anular pedido', danger: true, requireText: 'ANULAR' })) { r.estado = 'Fallido'; redraw(); L.toast('Pedido anulado', r.id, 'success'); } } }
        ],
        bulkActions: [
          { label: 'Asignar a ruta', icon: 'route', onClick: (ids, done) => L.modal({ title: `Asignar ${ids.length} pedido(s) a una ruta`, body: `<div class="field"><label for="as-r">Ruta</label><select id="as-r" class="select">${D.rutas.map((r) => `<option>${r.id} · ${esc(r.zona)} (${r.ocupacion} % ocupación)</option>`).join('')}</select></div>`, actions: [{ label: 'Cancelar' }, { label: 'Asignar', cls: 'btn-primary', onClick: () => { done(); L.toast('Pedidos asignados', `${ids.length} pedido(s) quedaron planificados.`, 'success'); } }] }) },
          { label: 'Exportar selección', icon: 'download', onClick: (ids) => { L.download('pedidos_seleccion.csv', L.toCSV(D.pedidos.filter((p) => ids.includes(p.id)), [{ label: 'Pedido', key: 'id' }, { label: 'Cliente', key: 'clienteNombre' }, { label: 'Estado', key: 'estado' }, { label: 'Total', key: 'total' }])); L.toast('Exportación lista', `${ids.length} filas en CSV.`, 'success'); } }
        ]
      });
      if (q.estado) { tbl.state.filters.estado = q.estado; $('#pd-f-estado', root).value = q.estado; tbl.draw(); }
      $('#pd-exp', root).onclick = (e) => L.busy(e.currentTarget, () => { L.download('pedidos.csv', L.toCSV(tbl.filtered(), [{ label: 'Pedido', key: 'id' }, { label: 'Cliente', key: 'clienteNombre' }, { label: 'Canal', key: 'canal' }, { label: 'Estado', key: 'estado' }, { label: 'Total', key: 'total' }])); L.toast('Exportación lista', 'Se descargó el listado con el filtro aplicado.', 'success'); }, 600);
    }
  });

  L.route('/pedidos/:id', {
    title: (p) => p.id || 'Detalle de pedido', parent: '/pedidos', block: 'Proceso operacional principal', module: 'M3 · M6 · M7', rf: ['RF-03.11', 'RF-06.14', 'RF-12.08', 'RNG-08', 'RF-03.10', 'RF-03.12'], actors: ['Preventista', 'Gerente Comercial', 'Cliente'],
    render: ({ id }) => {
      const o = L.findOrder(id);
      if (!o) return L.empty('search', 'Pedido no encontrado', `No existe el pedido ${id}.`, '<a class="btn btn-primary" href="#/pedidos">Volver a pedidos</a>');
      const idx = ['Capturado sin conexión', 'Pendiente de validación', 'Confirmado', 'Planificado', 'En picking', 'Cargado', 'En ruta', 'Entregado', 'Rendido'];
      const curI = Math.max(idx.indexOf(o.estado), o.estado === 'Retenido' ? 1 : o.estado === 'Parcial' || o.estado === 'Fallido' || o.estado === 'Reprogramado' ? 6 : -1);
      return `<div class="page-head"><div class="titles"><span class="page-kicker">Pedido · ${esc(o.origen)}</span><h1 class="mono">${esc(o.id)}</h1><p class="muted" style="margin:0"><a href="#/clientes/${o.cliente}">${esc(o.clienteNombre)}</a> · ${esc(o.comuna)} · ${L.estadoBadge(o.estado)}</p></div>
        <div class="actions">${o.estado === 'Retenido' ? `<button type="button" class="btn btn-primary" id="od-auth">${icon('check')}Autorizar envío</button>` : ''}<div class="menu-wrap"><button type="button" class="btn btn-secondary" id="od-more">${icon('more')}Acciones</button></div></div></div>
        ${o.id === D.pedidoDifPrecio && !o.precioCorregido ? L.alert('warning', 'Diferencia de precio antes de facturar', `El importe calculado para la factura (${fmt.clp(Math.round(o.total * 1.032))}) difiere del precio pactado en el pedido (${fmt.clp(o.total)}). Corrija antes de facturar: el precio pactado se conserva (RF-03.12, RNG-08).`, `<button type="button" class="btn btn-secondary btn-sm" id="od-fixp">${icon('check', 'icon-sm')}Facturar con el precio pactado</button>`) + '<div style="height:16px"></div>' : ''}
        ${o.estado === 'Retenido' ? L.alert('danger', 'Pedido retenido por crédito', 'Excede el límite en 14 % sobre el umbral de 10 %. Requiere autorización registrada de un supervisor (RF-03.10).') + '<div style="height:16px"></div>' : ''}
        <div class="split"><div class="stack-lg">
          <section class="card card-flush"><div class="card-head"><h2>Líneas</h2><span class="small muted">Precio acordado conservado (RNG-08)</span></div><div class="table-wrap"><table class="table"><thead><tr><th>Producto</th><th>Lote</th><th class="right">Cantidad</th><th class="right">Precio</th><th class="right">Subtotal</th></tr></thead><tbody>${o.lineas.map((l) => `<tr><td class="wrap">${esc(l.nombre)}<div class="small muted mono">${l.sku}</div></td><td class="mono small">${o.estado.match(/picking|Cargado|ruta|Entregado|Rendido|Parcial/) ? l.lote : '—'}</td><td class="num right">${l.cant}</td><td class="num right">${fmt.clp(l.precio)}</td><td class="num right">${fmt.clp(l.cant * l.precio)}</td></tr>`).join('')}</tbody><tfoot><tr><td colspan="4" class="right"><strong>Total</strong></td><td class="num right"><strong>${fmt.clp(o.total)}</strong></td></tr></tfoot></table></div></section>
          <section class="card"><div class="card-head"><h2>Documentos</h2></div><ul class="list">${[['Nota de venta', 'PDF'], ...(curI >= 5 ? [['Guía de despacho electrónica 884' + o.id.slice(-3), 'PDF · XML']] : []), ...(curI >= 7 ? [['Prueba de entrega (firma y foto)', 'PDF'], ['Factura electrónica', 'PDF · XML']] : [])].map(([t, f]) => `<li>${icon('file')}<span class="grow">${t}</span><span class="small muted">${f}</span><button type="button" class="btn btn-tertiary btn-sm" data-doc="${esc(t)}">${icon('download', 'icon-sm')}Descargar</button></li>`).join('')}</ul></section>
        </div>
        <aside class="stack-lg"><section class="card"><div class="card-head"><h2>Seguimiento</h2></div><ol class="timeline">${idx.map((s, i) => `<li class="${i < curI ? 'done' : i === curI ? (['Retenido', 'Fallido'].includes(o.estado) ? 'error' : 'current') : ''}"><span class="dot"></span><div class="t-title ${i > curI ? 'pending' : ''}">${i === curI && o.estado !== s ? esc(o.estado) : esc(s)}</div>${i <= curI ? `<div class="t-meta">${fmt.dt(new Date(new Date(o.creado).getTime() + i * 3.1 * 3600e3))}</div>` : ''}</li>`).join('')}</ol></section>
          <section class="card"><dl class="desc-list"><dt>Preventista</dt><dd>${esc(o.preventista)}</dd><dt>Creado</dt><dd>${fmt.dt(o.creado)}</dd><dt>Entrega</dt><dd>${fmt.date(o.entrega)} · ${esc(o.ventana)}</dd><dt>Ruta</dt><dd><a href="#/rutas/${o.ruta}">${o.ruta}</a></dd></dl></section></aside></div>`;
    },
    mount: (root, { id }) => {
      const o = L.findOrder(id);
      if (!o) return;
      $$('[data-doc]', root).forEach((b) => (b.onclick = () => L.busy(b, () => L.toast('Documento descargado', b.dataset.doc, 'success'), 600)));
      $('#od-fixp', root) && ($('#od-fixp', root).onclick = (e) => L.busy(e.currentTarget, () => { o.precioCorregido = true; L.toast('Diferencia corregida', 'La factura usará el precio pactado; queda registro en la bitácora.', 'success'); L.router.resolve(); }, 700));
      $('#od-auth', root) && ($('#od-auth', root).onclick = () => L.modal({ title: 'Autorizar envío del pedido', body: `<div class="field"><label for="au-m">Motivo <span class="req" aria-hidden="true">*</span></label><select id="au-m" class="select"><option value="">Seleccione…</option><option>Cliente con historial de pago puntual</option><option>Abono comprometido</option><option>Excepción comercial</option></select></div>`, onOpen: (d) => L.bindField($('#au-m', d), ['required']), actions: [{ label: 'Cancelar' }, { label: 'Autorizar', cls: 'btn-primary', onClick: (api) => { if (!L.validateAll(api.el)) return false; o.estado = 'Confirmado'; L.toast('Pedido autorizado', 'Queda registrado supervisor, fecha, hora y motivo.', 'success'); L.router.resolve(); } }] }));
      L.menu($('#od-more', root), [{ label: 'Ver cliente', icon: 'store', onClick: () => L.go('/clientes/' + o.cliente) }, { label: 'Ver ruta', icon: 'route', onClick: () => L.go('/rutas/' + o.ruta) }, { label: 'Imprimir', icon: 'printer', onClick: () => window.print() }, { sep: true }, { label: 'Anular pedido', icon: 'ban', danger: true, onClick: async () => { if (await L.confirm({ title: `¿Anular ${o.id}?`, message: 'Se liberará el stock reservado y se avisará al cliente.', confirmLabel: 'Anular', danger: true, requireText: 'ANULAR' })) L.toast('Pedido anulado', o.id, 'success'); } }]);
    }
  });

  /* ---------- Rutas (M4) ---------- */
  L.route('/rutas', {
    title: 'Rutas', parent: '/inicio', block: 'Proceso operacional principal', module: 'M4 Rutas', rf: ['RF-04.01', 'RF-04.02', 'RF-04.03', 'RF-04.05', 'RF-11.05', 'RNG-14'], actors: ['Planificador de Rutas', 'Gerente de Operaciones'],
    render: () => `<div class="page-head"><div class="titles"><h1>Rutas</h1><p class="muted" style="margin:0">Hoy en ejecución y plan de mañana propuesto por el motor de ruteo.</p></div><div class="actions"><button type="button" class="btn btn-primary" id="rt-gen">${icon('zap')}Generar plan de mañana</button></div></div>
      ${L.tabsHtml('rt', [{ id: 'hoy', label: 'En ejecución hoy', count: D.rutas.length }, { id: 'manana', label: 'Plan de mañana' }], 'hoy')}
      <div ${L.panelAttrs('rt', 'hoy', 'hoy')}><div class="grid grid-auto">${D.rutas.map((r) => `<a class="card card-link" href="#/rutas/${r.id}"><div class="row-between"><strong>${r.id} · ${esc(r.zona)}</strong>${L.badge(r.estado, r.estado === 'Completada' ? 'success' : r.estado === 'En ruta' ? 'accent' : '')}</div><p class="small muted" style="margin:4px 0 12px">${esc(r.conductor)} · ${esc(r.camion)} ${r.frio ? '· frío' : ''}${r.externo ? ' · ' + esc(r.transportista) : ''}</p><div class="row-between small"><span>Entregas</span><span class="num">${r.hechas}/${r.paradas}</span></div><div class="progress"><span style="width:${(r.hechas / r.paradas) * 100}%"></span></div><div class="row-between small" style="margin-top:8px"><span>Ocupación</span><span class="num">${r.ocupacion} %</span></div><div class="progress dark"><span style="width:${r.ocupacion}%"></span></div>${r.desvio ? `<p class="small" style="color:var(--c-danger);margin:8px 0 0">${icon('alert', 'icon-sm')} Desvío de 3,4 km</p>` : ''}</a>`).join('')}</div></div>
      <div ${L.panelAttrs('rt', 'manana', 'hoy')}><div class="card" id="rt-plan">${L.empty('truck', 'El plan de mañana aún no se genera', 'Genere la propuesta: el motor asigna los pedidos confirmados respetando capacidad, frío y ventanas, y usted la corrige antes de aprobar.', `<button type="button" class="btn btn-primary" data-gen>${icon('zap')}Generar plan</button>`)}</div></div>`,
    mount: (root) => {
      const tabs = L.tabs($('.tabs', root));
      const gen = async (btn) => {
        tabs.select('manana');
        const host = $('#rt-plan', root);
        host.innerHTML = `<div class="stack"><div class="row"><span class="spinner"></span><strong id="gp-t">Asignando 1.432 entregas a 84 camiones…</strong></div><div class="progress"><span id="gp-b" style="width:5%"></span></div><p class="small muted" id="gp-s">Restricciones: capacidad, frío, ventanas horarias, ocupación mínima 70 %.</p></div>`;
        const msgs = ['Agrupando por zona logística…', 'Respetando ventanas de recepción…', 'Asignando carga refrigerada solo a camiones con frío…', 'Secuenciando y calculando ETA…'];
        for (let i = 0; i < 4; i++) { await L.sleep(600); $('#gp-b', root).style.width = 25 * (i + 1) + '%'; $('#gp-t', root).textContent = msgs[i]; }
        host.innerHTML = `${L.alert('success', 'Plan generado en 11 minutos (simulado)', '84 rutas, 1.432 entregas, ocupación promedio 79 %. Revise y corrija antes de aprobar; cada corrección queda registrada.')}
          <div class="table-wrap" style="margin-top:var(--sp-4)"><table class="table"><thead><tr><th>Ruta</th><th>Zona</th><th>Camión</th><th class="right">Entregas</th><th class="right">Peso</th><th class="right">Ocupación</th><th>Observación</th></tr></thead><tbody>${D.rutas.map((r, i) => `<tr><td class="mono">${r.id}</td><td>${esc(r.zona)}</td><td>${esc(r.camion)}${r.frio ? ' ' + L.badge('Frío', 'info') : ''}</td><td class="num right">${r.paradas + 2}</td><td class="num right">${fmt.n(2800 + i * 97)} kg</td><td class="num right">${Math.min(96, r.ocupacion + 8)} %</td><td data-obs="${i}">${i === 4 ? L.badge('2 entregas fuera de ventana', 'warning') : i === 9 ? L.badge('Bajo 70 %: consolidar', 'danger') : L.badge('Lista', 'success')}</td></tr>`).join('')}</tbody></table></div>
          <div id="gp-cap" style="margin-top:var(--sp-4)">${L.alert('danger', 'Una ruta no puede salir', `${D.rutas[9] ? D.rutas[9].id : 'R-10'} queda bajo la ocupación mínima de 70 %. Ningún camión sale bajo ese umbral ni sobre su peso, volumen o condición térmica (RNG-14).`, '<button type="button" class="btn btn-secondary btn-sm" id="gp-cons">Consolidar con la ruta vecina</button>')}</div>
          <div class="row" style="justify-content:flex-end;margin-top:var(--sp-4)"><button type="button" class="btn btn-secondary" id="gp-sms">${icon('send')}Vista previa de avisos</button><button type="button" class="btn btn-primary" id="gp-ok">${icon('check')}Aprobar plan</button></div>`;
        let consolidated = false;
        $('#gp-cons', root).onclick = (e) => L.busy(e.currentTarget, () => { consolidated = true; $('[data-obs="9"]', root).innerHTML = L.badge('Consolidada · 82 %', 'success'); $('#gp-cap', root).innerHTML = L.alert('success', 'Capacidad y carga dentro de los límites', 'Todas las rutas cumplen peso, volumen, frío y ocupación mínima (RNG-14).'); }, 800);
        $('#gp-ok', root).onclick = async () => { if (!consolidated) { L.toast('No se puede aprobar todavía', 'Resuelva la ruta bajo la ocupación mínima (RNG-14).', 'error'); $('#gp-cap', root).scrollIntoView({ block: 'center', behavior: 'smooth' }); return; } if (await L.confirm({ title: '¿Aprobar el plan de mañana?', message: 'Se publicarán las rutas a M6 y a los transportistas, y se programarán 1.432 avisos SMS.', confirmLabel: 'Aprobar plan' })) L.toast('Plan aprobado', 'Rutas publicadas a conductores y transportistas.', 'success'); };
        $('#gp-sms', root).onclick = () => L.modal({ title: 'Aviso al cliente (RF-04.06)', body: '<div class="card" style="box-shadow:none;background:var(--c-bg);font-family:var(--font-mono);font-size:var(--fs-sm)">Puelche: su pedido llega mañana entre 09:00 y 09:30. Camión KXTR-21.</div>', actions: [{ label: 'Cerrar', cls: 'btn-primary' }] });
      };
      $('#rt-gen', root).onclick = (e) => gen(e.currentTarget);
      root.addEventListener('click', (e) => { if (e.target.closest('[data-gen]')) gen(); });
    }
  });

  L.route('/rutas/:id', {
    title: (p) => (p.id ? `Ruta ${p.id}` : 'Detalle de ruta'), parent: '/rutas', block: 'Proceso operacional principal', module: 'M4 Rutas · M12', rf: ['RF-04.02', 'RF-04.04', 'RF-14.02', 'RF-14.05', 'RF-04.08', 'RF-14.04'], actors: ['Planificador de Rutas'],
    render: ({ id }) => {
      const r = D.rutas.find((x) => x.id === id);
      if (!r) return L.empty('search', 'Ruta no encontrada', `No existe la ruta ${id}.`, '<a class="btn btn-primary" href="#/rutas">Volver a rutas</a>');
      const peds = D.pedidos.filter((p) => p.ruta === id);
      return `<div class="page-head"><div class="titles"><span class="page-kicker">${esc(r.transportista)}</span><h1>${r.id} · ${esc(r.zona)}</h1><p class="muted" style="margin:0">${esc(r.conductor)} · ${esc(r.camion)} · salida ${r.salida} · término estimado ${r.eta}</p></div></div>
        <div class="grid grid-4" style="margin-bottom:var(--sp-5)">${[['Entregas', `${r.hechas}/${r.paradas}`], ['Ocupación', r.ocupacion + ' %'], ['Kilómetros', r.km + ' km'], ['OTIF de la ruta', fmt.pct(r.otif)]].map(([a, b]) => `<div class="card kpi" style="padding:var(--sp-4)"><span class="label">${a}</span><span class="value" style="font-size:var(--fs-2xl)">${b}</span></div>`).join('')}</div>
        ${r.desvio ? L.alert('warning', 'Desvío de 3,4 km sobre la ruta planificada', 'Alerta generada por telemetría (RF-14.03). Contacte al conductor o registre la causa.', '<a class="btn btn-secondary btn-sm" href="#/telemetria">Ver en el mapa</a>') + '<div style="height:16px"></div>' : ''}
        <section class="card card-flush"><div class="card-head"><h2>Pedidos de la ruta</h2></div><div class="table-wrap"><table class="table"><thead><tr><th>#</th><th>Pedido</th><th>Cliente</th><th>Ventana</th><th>Estado</th></tr></thead><tbody>${peds.map((p, i) => `<tr><td class="num">${i + 1}</td><td><a class="row-link mono" href="#/pedidos/${p.id}">${p.id}</a></td><td>${esc(p.clienteNombre)}</td><td>${esc(p.ventana)}</td><td>${L.estadoBadge(p.estado)}</td></tr>`).join('')}</tbody></table></div></section>
        <section class="card card-flush" style="margin-top:var(--sp-5)"><div class="card-head"><h2>Costo por entrega realizada</h2>${L.tip('Se calcula al cerrar cada entrega con los km y minutos de telemetría imputados a esa parada (RF-04.08, RF-14.04).')}</div><div class="table-wrap"><table class="table"><caption class="sr-only">Costo de cada entrega de la ruta</caption><thead><tr><th>Pedido</th><th>Cliente</th><th class="right">Km imputados</th><th class="right">Minutos</th><th class="right">Transporte</th><th class="right">Descarga</th><th class="right">Costo total</th></tr></thead><tbody>${peds.slice(0, Math.max(3, r.hechas)).map((p, i) => { const km = +(r.km / r.paradas * (0.7 + (i % 3) * 0.25)).toFixed(1), min = 9 + (i * 7) % 15, tr = Math.round(km * 690), de = 2400 + min * 210; return `<tr><td class="mono">${p.id}</td><td>${esc(p.clienteNombre)}</td><td class="num right">${fmt.n(km, 1)}</td><td class="num right">${min}</td><td class="num right">${fmt.clp(tr)}</td><td class="num right">${fmt.clp(de)}</td><td class="num right"><strong>${fmt.clp(tr + de)}</strong></td></tr>`; }).join('')}</tbody></table></div><p class="small muted" style="padding:0 var(--sp-5) var(--sp-4)">Alimenta el costo de servir por cliente en <a href="#/analitica/costo">Analítica</a>.</p></section>`;
    }
  });

  /* ---------- Preparación (M5) ---------- */
  L.route('/preparacion', {
    title: 'Preparación', parent: '/inicio', block: 'Proceso operacional principal', module: 'M5 Preparación', rf: ['RF-05.01', 'RF-05.02', 'RF-05.04', 'RF-05.05', 'RF-09.08'], actors: ['Preparador', 'Jefa de Bodega'],
    render: () => `<div class="page-head"><div class="titles"><h1>Preparación de pedidos</h1><p class="muted" style="margin:0">Misiones del turno noche en CD Talca, con secuencia térmica y FEFO.</p></div><div class="actions"><button type="button" class="btn btn-primary" id="pp-gen">${icon('zap')}Generar misiones</button></div></div>
      <div class="grid grid-3">${[['M-3301', 'Seco', 64, 64, 'Completada'], ['M-3302', 'Refrigerado', 42, 26, 'En curso'], ['M-3303', 'Congelado', 18, 0, 'Pendiente'], ['M-3304', 'Seco', 71, 12, 'En curso'], ['M-3305', 'Seco', 55, 0, 'Pendiente'], ['M-3306', 'Refrigerado', 38, 0, 'Pendiente']].map(([id, z, n, d, e]) => `<div class="card"><div class="row-between"><strong class="mono">${id}</strong>${L.badge(e, e === 'Completada' ? 'success' : e === 'En curso' ? 'accent' : '')}</div><p class="small muted" style="margin:4px 0 12px">Zona ${z} · ${n} líneas · ${d ? 'Matías Lagos' : 'sin asignar'}</p><div class="progress"><span style="width:${(d / n) * 100}%"></span></div><div class="row-between" style="margin-top:12px"><span class="small num">${d}/${n}</span>${e === 'Completada' ? '' : `<a class="btn btn-secondary btn-sm" href="#/flujo?paso=4">${icon('scan', 'icon-sm')}${e === 'En curso' ? 'Continuar' : 'Iniciar'}</a>`}</div></div>`).join('')}</div>`,
    mount: (root) => { $('#pp-gen', root).onclick = (e) => L.busy(e.currentTarget, () => L.toast('Misiones generadas', '6 misiones agrupadas por pasillo y zona térmica.', 'success'), 1200); }
  });

  /* ---------- Cobranza y rendición (M7) ---------- */
  L.route('/rendicion', {
    title: 'Cobranza y rendición', parent: '/inicio', block: 'Proceso operacional principal', module: 'M7 Cobranza y rendición', rf: ['RF-07.01', 'RF-07.02', 'RF-07.03', 'RF-07.08', 'RF-11.07'], actors: ['Conductores', 'Gerente de Finanzas'],
    render: () => {
      const rows = D.rutas.map((r, i) => { const esp = 900000 + i * 173000; const dif = [0, -12000, 0, 0, -128500, 0, 3000, 0, 0, -45000, 0, 0][i]; return { id: r.id, zona: r.zona, conductor: r.conductor, esperado: esp, rendido: esp + dif, dif, estado: r.estado === 'Completada' ? (dif ? 'Con descuadre' : 'Cuadrada') : 'En ruta' }; });
      L._rend = rows;
      return `<div class="page-head"><div class="titles"><h1>Cobranza y rendición</h1><p class="muted" style="margin:0">Contraste automático entre lo esperado por camión y turno y lo rendido.</p></div></div>
        <div class="grid grid-3" style="margin-bottom:var(--sp-5)"><div class="card kpi"><span class="label">Esperado hoy</span><span class="value" style="font-size:var(--fs-2xl)">${fmt.clp(rows.reduce((a, r) => a + r.esperado, 0))}</span></div><div class="card kpi"><span class="label">Rendido</span><span class="value" style="font-size:var(--fs-2xl)">${fmt.clp(rows.reduce((a, r) => a + r.rendido, 0))}</span></div><div class="card kpi"><span class="label">Descuadres sin tipificar</span><span class="value" style="font-size:var(--fs-2xl);color:var(--c-danger)">3</span></div></div>
        ${L.alert('info', 'Liquidación automática al volver a base', `${rows.filter((r) => r.estado !== 'En ruta').length} de ${rows.length} camiones ya liquidados: el sistema consolidó documentos entregados, devoluciones recibidas, cobranzas en efectivo y saldo de envases sin digitación (RF-11.07). Abra «Ver liquidación» en cada fila.`)}<div style="height:16px"></div>
        <div class="card card-flush" id="rd-t"></div>`;
    },
    mount: (root) => {
      L.dataTable($('#rd-t', root), {
        id: 'rd', caption: 'Rendiciones por ruta', rows: L._rend, searchKeys: ['id', 'zona', 'conductor'], filters: [{ key: 'estado', label: 'Estado', options: ['Cuadrada', 'Con descuadre', 'En ruta'] }],
        columns: [{ key: 'id', label: 'Ruta', render: (r) => `<span class="mono">${r.id}</span>` }, { key: 'zona', label: 'Zona' }, { key: 'conductor', label: 'Conductor' }, { key: 'esperado', label: 'Esperado', right: true, render: (r) => fmt.clp(r.esperado) }, { key: 'rendido', label: 'Rendido', right: true, render: (r) => fmt.clp(r.rendido) }, { key: 'dif', label: 'Diferencia', right: true, render: (r) => `<span style="color:${r.dif ? 'var(--c-danger)' : 'inherit'}">${r.dif ? (r.dif > 0 ? '+' : '−') + fmt.clp(Math.abs(r.dif)) : '—'}</span>` }, { key: 'estado', label: 'Estado', render: (r) => L.badge(r.estado, r.estado === 'Cuadrada' ? 'success' : r.estado === 'Con descuadre' ? 'danger' : 'accent') }],
        rowActions: (r, redraw) => [{ label: 'Tipificar descuadre', icon: 'edit', onClick: () => L.modal({ title: `Tipificar descuadre ${r.id}`, body: `<p>Diferencia de ${fmt.clp(Math.abs(r.dif))}.</p><div class="field"><label for="tp-c">Causal <span class="req" aria-hidden="true">*</span></label><select id="tp-c" class="select"><option value="">Seleccione…</option><option>Vuelto mal entregado</option><option>Billete rechazado</option><option>Abono parcial no registrado</option></select></div><div class="field" style="margin-top:12px"><label class="check"><input type="checkbox" id="tp-f"> Firmo digitalmente como responsable</label></div>`, onOpen: (d) => { L.bindField($('#tp-c', d), ['required']); L.bindField($('#tp-f', d), [(v) => (v ? '' : 'La firma es obligatoria (RF-07.03).')]); }, actions: [{ label: 'Cancelar' }, { label: 'Registrar', cls: 'btn-primary', onClick: (api) => { if (!L.validateAll(api.el)) return false; r.estado = 'Cuadrada'; redraw(); L.toast('Descuadre tipificado', 'Firma y responsable registrados en la bitácora.', 'success'); } }] }) }, { label: 'Ver liquidación', icon: 'file', onClick: () => L.modal({ title: `Liquidación ${r.id} · ${r.conductor}`, body: r.estado === 'En ruta' ? L.alert('info', 'Camión en ruta', 'La liquidación se procesa automáticamente cuando el camión vuelve a base y sincroniza.') : `<p class="small muted" style="margin-top:0">Procesada automáticamente al retornar a base, 18:42 (RF-11.07).</p><dl class="desc-list"><dt>Documentos tributarios entregados</dt><dd>${14 + r.zona.length % 6} guías · ${12 + r.zona.length % 5} facturas</dd><dt>Devoluciones físicas recibidas</dt><dd>3 líneas · 41 unidades</dd><dt>Cobranza en efectivo</dt><dd>${fmt.clp(r.rendido)} de ${fmt.clp(r.esperado)}</dd><dt>Abonos parciales</dt><dd>1 · saldo a cuenta corriente</dd><dt>Saldo de envases</dt><dd>18 canastillos retornados</dd><dt>Resultado</dt><dd>${r.dif ? L.badge('Descuadre ' + fmt.clp(Math.abs(r.dif)), 'danger') : L.badge('Cuadrada', 'success')}</dd></dl>`, actions: [{ label: 'Cerrar', cls: 'btn-primary' }] }) }, { label: 'Ver ruta', icon: 'route', onClick: () => L.go('/rutas/' + r.id) }]
      });
    }
  });
})(window.LFX);
