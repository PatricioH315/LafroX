/* Operación: pedidos (M3), rutas (M4), preparación (M5) y cobranza y rendición (M7). */
(function (L) {
  const { esc, icon, $, $$, data: D, fmt } = L;

  /* ---------- Pedidos ---------- */
  L.route('/pedidos', {
    title: 'Pedidos', parent: '/inicio', block: 'Proceso operacional principal', module: 'M3 Preventa', rf: ['RF-03.03', 'RF-03.16', 'RF-17.12'], actors: ['Preventista', 'Gerente Comercial', 'Gerente de Operaciones', 'Planificador de Rutas'],
    render: () => `<div class="page-head"><div class="titles"><h1>Pedidos</h1><p class="muted" style="margin:0">Preventa, portal de clientes y EDI en un solo listado, con su estado en el proceso.</p></div>
      <div class="actions"><button type="button" class="btn btn-secondary" id="pd-exp">${icon('download')}Exportar CSV</button>${L.allowed('/flujo') ? `<a class="btn btn-primary" href="#/flujo?alta=1">${icon('plus')}Nuevo pedido</a>` : L.allowed('/terreno/preventa') ? `<a class="btn btn-primary" href="#/terreno/preventa">${icon('plus')}Nuevo pedido</a>` : ''}</div></div>
      <div class="grid grid-4" style="margin-bottom:var(--sp-5)" id="pd-kpi"></div>
      <div class="card card-flush" id="pd-t"></div>`,
    mount: (root, p, q) => {
      const counts = (e) => D.pedidos.filter((x) => x.estado === e).length;
      D.pedidos.forEach((x) => (x.precioEstado = L.difPrecio(x) ? 'Con diferencia' : 'Sin diferencia'));
      $('#pd-kpi', root).innerHTML = [['Por validar', counts('Pendiente de validación') + counts('Capturado sin conexión'), 'sync'], ['Retenidos', counts('Retenido'), 'alert'], ['En ruta', counts('En ruta'), 'truck'], ['Entregados hoy', counts('Entregado') + counts('Rendido'), 'check-circle']].map(([t, v, i]) => `<div class="card kpi" style="padding:var(--sp-4)"><span class="label">${icon(i, 'icon-sm')}${t}</span><span class="value" style="font-size:var(--fs-2xl)">${v * 17}</span></div>`).join('');
      const tbl = L.dataTable($('#pd-t', root), {
        id: 'pd', caption: 'Listado de pedidos', rows: D.pedidos, searchKeys: ['id', 'clienteNombre', 'comuna', 'preventista'], searchPlaceholder: 'Buscar por pedido, cliente o comuna',
        filters: [{ key: 'estado', label: 'Estado', options: D.estadosPedido }, { key: 'canal', label: 'Canal', options: ['Tradicional', 'Food service', 'Moderno'] }, { key: 'origen', label: 'Origen', options: ['Preventa', 'Portal', 'EDI'] }, { key: 'precioEstado', label: 'Precio', options: ['Con diferencia', 'Sin diferencia'] }],
        sort: 'id', dir: 'desc', selectable: true,
        columns: [
          { key: 'id', label: 'Pedido', render: (r) => `<a class="row-link mono" href="#/pedidos/${r.id}">${r.id}</a>` },          { key: 'clienteNombre', label: 'Cliente', render: (r) => `${esc(r.clienteNombre)}<div class="small muted">${esc(r.comuna)}</div>` },
          { key: 'canal', label: 'Canal' },
          { key: 'origen', label: 'Origen', render: (r) => L.badge(r.origen, r.origen === 'EDI' ? 'dark' : '') },
          { key: 'entrega', label: 'Entrega', render: (r) => `${fmt.dateShort(r.entrega)}<div class="small muted">${esc(r.ventana)}</div>`, sortVal: (r) => r.entrega },
          { key: 'total', label: 'Total', right: true, render: (r) => fmt.clp(r.total) },
          { key: 'estado', label: 'Estado', render: (r) => L.estadoBadge(r.estado) + (L.difPrecio(r) ? ` ${L.badge('Diferencia de precio', 'warning')}` : '') }
        ],
        rowActions: (r, redraw) => [
          { label: 'Ver detalle', icon: 'eye', onClick: () => L.go('/pedidos/' + r.id) },
          ...(L.allowed('/flujo') ? [{ label: 'Ver en el flujo', icon: 'activity', onClick: () => L.go('/flujo?pedido=' + encodeURIComponent(r.id)) }, { label: 'Duplicar pedido', icon: 'copy', onClick: () => L.go('/flujo?duplicar=' + encodeURIComponent(r.id)) }] : []),
          ...(!L.can('pedido.anular') ? [] : [{ sep: true },
          { label: 'Anular pedido', icon: 'ban', danger: true, onClick: async () => { if (await L.confirm({ title: `¿Anular ${r.id}?`, message: 'Se liberará el stock reservado y se avisará al cliente. Queda registrado en la auditoría.', confirmLabel: 'Anular pedido', danger: true, requireText: 'ANULAR' })) { L.logAudit('Modificación', 'Pedido', `Anulación de ${r.id}`, 'Consola web', r.estado, 'Anulado'); r.estado = 'Fallido'; redraw(); L.toast('Pedido anulado', r.id, 'success'); } } }])
        ],
        bulkActions: [
          ...(!L.can('pedido.asignar') ? [] : [{ label: 'Asignar a ruta', icon: 'route', onClick: (ids, done) => L.modal({ title: `Asignar ${ids.length} pedido(s) a una ruta`, body: `<div class="field"><label for="as-r">Ruta</label><select id="as-r" class="select">${D.rutas.map((r) => `<option>${r.id} · ${esc(r.zona)} (${r.ocupacion} % ocupación)</option>`).join('')}</select></div>`, actions: [{ label: 'Cancelar' }, { label: 'Asignar', cls: 'btn-primary', onClick: () => { done(); L.toast('Pedidos asignados', `${ids.length} pedido(s) quedaron planificados.`, 'success'); } }] }) }]),
          { label: 'Exportar selección', icon: 'download', onClick: (ids) => { L.download('pedidos_seleccion.csv', L.toCSV(D.pedidos.filter((p) => ids.includes(p.id)), [{ label: 'Pedido', key: 'id' }, { label: 'Cliente', key: 'clienteNombre' }, { label: 'Estado', key: 'estado' }, { label: 'Total', key: 'total' }])); L.toast('Exportación lista', `${ids.length} filas en CSV.`, 'success'); } }
        ]
      });
      if (q.estado) { tbl.state.filters.estado = q.estado; $('#pd-f-estado', root).value = q.estado; tbl.draw(); }
      if (q.precio === 'dif') { tbl.state.filters.precioEstado = 'Con diferencia'; $('#pd-f-precioEstado', root).value = 'Con diferencia'; tbl.draw(); }
      $('#pd-exp', root).onclick = (e) => L.busy(e.currentTarget, () => { L.download('pedidos.csv', L.toCSV(tbl.filtered(), [{ label: 'Pedido', key: 'id' }, { label: 'Cliente', key: 'clienteNombre' }, { label: 'Canal', key: 'canal' }, { label: 'Estado', key: 'estado' }, { label: 'Total', key: 'total' }])); L.toast('Exportación lista', 'Se descargó el listado con el filtro aplicado.', 'success'); }, 600);
    }
  });

  L.route('/pedidos/:id', {
    title: (p) => p.id || 'Detalle de pedido', parent: '/pedidos', block: 'Proceso operacional principal', module: 'M3 · M6 · M7', rf: ['RF-03.11', 'RF-06.14', 'RF-12.08', 'RNG-08', 'RF-03.10', 'RF-03.12'], actors: ['Preventista', 'Gerente Comercial', 'Cliente'],
    render: ({ id }) => {
      const o = L.findOrder(id);
      if (!o) return L.empty('search', 'Pedido no encontrado', `No existe el pedido ${id}.`, '<a class="btn btn-primary" href="#/pedidos">Volver a pedidos</a>');
      const idx = ['Capturado sin conexión', 'Pendiente de validación', 'Confirmado', 'Planificado', 'En picking', 'Cargado', 'En ruta', 'Entregado', 'Rendido'];
      const dif = L.difPrecio(o);
      const curI = Math.max(idx.indexOf(o.estado), o.estado === 'Retenido' ? 1 : o.estado === 'Parcial' || o.estado === 'Fallido' || o.estado === 'Reprogramado' ? 6 : -1);
      return `<div class="page-head"><div class="titles"><span class="page-kicker">Pedido · ${esc(o.origen)}</span><h1 class="mono">${esc(o.id)}</h1><p class="muted" style="margin:0"><a href="#/clientes/${o.cliente}">${esc(o.clienteNombre)}</a> · ${esc(o.comuna)} · ${L.estadoBadge(o.estado)}</p></div>
        <div class="actions">${o.estado === 'Retenido' && L.can('pedido.autorizar') ? `<button type="button" class="btn btn-primary" id="od-auth">${icon('check')}Autorizar envío</button>` : ''}<div class="menu-wrap"><button type="button" class="btn btn-secondary" id="od-more">${icon('more')}Acciones</button></div></div></div>
        ${dif ? L.alert('warning', 'Diferencia de precio antes de facturar', `Con la lista vigente, la factura sumaría ${fmt.clp(dif.lista)}; el precio pactado en el pedido es ${fmt.clp(o.total)} (${dif.diferencia > 0 ? '+' : '−'}${fmt.clp(Math.abs(dif.diferencia))}). Cambió el precio de lista de ${dif.lineas.map((l) => esc(l.nombre)).join(', ')} después de tomar el pedido. Alerta enviada a Comercial: corrija antes de facturar; el precio pactado se conserva.`, L.can('pedido.facturar') ? `<button type="button" class="btn btn-secondary btn-sm" id="od-fixp">${icon('check', 'icon-sm')}Facturar con el precio pactado</button>` : '') + '<div style="height:16px"></div>' : ''}
        ${o.estado === 'Retenido' ? L.alert('danger', 'Pedido retenido por crédito', 'Excede el límite en 14 % sobre el umbral de 10 %. Requiere autorización registrada de un supervisor.') + '<div style="height:16px"></div>' : ''}
        <div class="split"><div class="stack-lg">
          <section class="card card-flush"><div class="card-head"><h2>Líneas</h2><span class="small muted">Precio acordado conservado</span></div><div class="table-wrap"><table class="table"><thead><tr><th>Producto</th><th>Lote</th><th class="right">Cantidad</th><th class="right">Precio pactado</th><th class="right">Subtotal</th></tr></thead><tbody>${o.lineas.map((l) => { const pr = D.productos.find((x) => x.sku === l.sku); return `<tr><td class="wrap">${esc(l.nombre)}<div class="small muted mono">${l.sku}</div></td><td class="mono small">${o.estado.match(/picking|Cargado|ruta|Entregado|Rendido|Parcial/) ? l.lote : '—'}</td><td class="num right">${l.cant}</td><td class="num right">${fmt.clp(l.precio)}${pr && pr.precio !== l.precio ? `<div class="small muted">Lista vigente ${fmt.clp(pr.precio)}</div>` : ''}</td><td class="num right">${fmt.clp(l.cant * l.precio)}</td></tr>`; }).join('')}</tbody><tfoot><tr><td colspan="4" class="right"><strong>Total</strong></td><td class="num right"><strong>${fmt.clp(o.total)}</strong></td></tr></tfoot></table></div></section>
          <section class="card"><div class="card-head"><h2>Documentos</h2></div><ul class="list">${[['Nota de venta', 'TXT de ejemplo'], ...(curI >= 5 ? [['Guía de despacho electrónica 884' + o.id.slice(-3), 'TXT de ejemplo']] : []), ...(curI >= 7 ? [['Registro de entrega', 'TXT de ejemplo'], ['Factura electrónica', 'TXT de ejemplo']] : [])].map(([t, f]) => `<li>${icon('file')}<span class="grow">${t}</span><span class="small muted">${f}</span><button type="button" class="btn btn-tertiary btn-sm" data-doc="${esc(t)}">${icon('download', 'icon-sm')}Descargar</button></li>`).join('')}</ul></section>
        </div>
        <aside class="stack-lg"><section class="card"><div class="card-head"><h2>Seguimiento</h2></div><ol class="timeline">${idx.map((s, i) => `<li class="${i < curI ? 'done' : i === curI ? (['Retenido', 'Fallido'].includes(o.estado) ? 'error' : 'current') : ''}"><span class="dot"></span><div class="t-title ${i > curI ? 'pending' : ''}">${i === curI && o.estado !== s ? esc(o.estado) : esc(s)}</div>${i <= curI ? `<div class="t-meta">${fmt.dt(new Date(new Date(o.creado).getTime() + i * 3.1 * 3600e3))}</div>` : ''}</li>`).join('')}</ol></section>
          <section class="card"><dl class="desc-list"><dt>Preventista</dt><dd>${esc(o.preventista)}</dd><dt>Creado</dt><dd>${fmt.dt(o.creado)}</dd><dt>Entrega</dt><dd>${fmt.date(o.entrega)} · ${esc(o.ventana)}</dd><dt>Ruta</dt><dd>${o.ruta ? `<a href="#/rutas/${o.ruta}">${o.ruta}</a>` : 'Sin asignar: entra al próximo plan'}</dd></dl></section></aside></div>`;
    },
    mount: (root, { id }) => {
      const o = L.findOrder(id);
      if (!o) return;
      $$('[data-doc]', root).forEach((b) => (b.onclick = () => L.downloadDemoText(o.id, b.dataset.doc, { Cliente: o.clienteNombre, Estado: o.estado, Total: fmt.clp(o.total), Entrega: fmt.date(o.entrega) })));
      $('#od-fixp', root) && ($('#od-fixp', root).onclick = (e) => L.busy(e.currentTarget, () => { o.precioCorregido = true; L.toast('Diferencia corregida', 'La factura usará el precio pactado; queda registro en la bitácora.', 'success'); L.router.resolve(); }, 700));
      $('#od-auth', root) && ($('#od-auth', root).onclick = () => L.modal({ title: 'Autorizar envío del pedido', body: `<div class="field"><label for="au-m">Motivo <span class="req" aria-hidden="true">*</span></label><select id="au-m" class="select"><option value="">Seleccione…</option><option>Cliente con historial de pago puntual</option><option>Abono comprometido</option><option>Excepción comercial</option></select></div>`, onOpen: (d) => L.bindField($('#au-m', d), ['required']), actions: [{ label: 'Cancelar' }, { label: 'Autorizar', cls: 'btn-primary', onClick: (api) => { if (!L.validateAll(api.el)) return false; L.logAudit('Aprobación', 'Pedido', `Envío de ${o.id} autorizado · motivo: ${$('#au-m', api.el).value}`, 'Consola web', 'Retenido', 'Confirmado'); o.estado = 'Confirmado'; L.toast('Pedido autorizado', 'Queda registrado supervisor, fecha, hora y motivo.', 'success'); L.router.resolve(); } }] }));
      L.menu($('#od-more', root), [{ label: 'Ver cliente', icon: 'store', onClick: () => L.go('/clientes/' + o.cliente) }, ...(o.ruta ? [{ label: 'Ver ruta', icon: 'route', onClick: () => L.go('/rutas/' + o.ruta) }] : []), { label: 'Imprimir', icon: 'printer', onClick: () => window.print() }, ...(L.can('pedido.anular') ? [{ sep: true }, { label: 'Anular pedido', icon: 'ban', danger: true, onClick: async () => { if (await L.confirm({ title: `¿Anular ${o.id}?`, message: 'Se liberará el stock reservado y se avisará al cliente.', confirmLabel: 'Anular', danger: true, requireText: 'ANULAR' })) L.toast('Pedido anulado', o.id, 'success'); } }] : [])]);
    }
  });

  /* ---------- Rutas (M4) ---------- */
  L.route('/rutas', {
    title: 'Rutas', parent: '/inicio', block: 'Proceso operacional principal', module: 'M4 Rutas', rf: ['RF-04.01', 'RF-04.03', 'RF-04.05', 'RF-11.05', 'RNG-14'], actors: ['Planificador de Rutas', 'Gerente de Operaciones'],
    render: () => `<div class="page-head"><div class="titles"><h1>Rutas</h1><p class="muted" style="margin:0">Hoy en ejecución y plan de mañana propuesto por el motor de ruteo.</p></div><div class="actions"><a class="btn btn-secondary" href="#/rutas/restricciones">${icon('sliders')}Restricciones de ruta</a>${L.can('ruta.planificar') ? `<button type="button" class="btn btn-primary" id="rt-gen">${icon('zap')}Generar plan de mañana</button>` : ''}</div></div>
      ${L.tabsHtml('rt', [{ id: 'hoy', label: 'En ejecución hoy', count: D.rutas.length }, { id: 'manana', label: 'Plan de mañana' }], 'hoy')}
      <div ${L.panelAttrs('rt', 'hoy', 'hoy')}><div class="grid grid-auto">${D.rutas.map((r) => `<a class="card card-link" href="#/rutas/${r.id}"><div class="row-between"><strong>${r.id} · ${esc(r.zona)}</strong>${L.badge(r.estado, r.estado === 'Completada' ? 'success' : r.estado === 'En ruta' ? 'accent' : '')}</div><p class="small muted" style="margin:4px 0 12px">${esc(r.conductor)} · ${esc(r.camion)} ${r.frio ? '· frío' : ''}${r.externo ? ' · ' + esc(r.transportista) : ''}</p><div class="row-between small"><span>Entregas</span><span class="num">${r.hechas}/${r.paradas}</span></div><div class="progress"><span style="width:${(r.hechas / r.paradas) * 100}%"></span></div><div class="row-between small" style="margin-top:8px"><span>Ocupación</span><span class="num">${r.ocupacion} %</span></div><div class="progress dark"><span style="width:${r.ocupacion}%"></span></div>${r.desvio ? `<p class="small" style="color:var(--c-danger);margin:8px 0 0">${icon('alert', 'icon-sm')} Desvío de 3,4 km</p>` : ''}</a>`).join('')}</div></div>
      <div ${L.panelAttrs('rt', 'manana', 'hoy')}><div class="card" id="rt-plan">${L.empty('truck', 'El plan de mañana aún no se genera', L.can('ruta.planificar') ? 'Genere la propuesta: el motor asigna los pedidos confirmados respetando capacidad, frío y ventanas, y usted la corrige antes de aprobar.' : 'Lo genera y aprueba el Planificador de Rutas.', L.can('ruta.planificar') ? `<button type="button" class="btn btn-primary" data-gen>${icon('zap')}Generar plan</button>` : '')}</div></div>`,
    mount: (root) => {
      const tabs = L.tabs($('.tabs', root));
      // Plan occupancy: R-10 stays under the 70 % minimum until it is consolidated (RNG-14)
      let consolidatedPlan = false;
      const planOcc = (r, i) => (i === 9 ? (consolidatedPlan ? 82 : 64) : Math.max(72, Math.min(96, r.ocupacion + 8)));
      const gen = async (btn) => {
        tabs.select('manana');
        const host = $('#rt-plan', root);
        host.innerHTML = `<div class="stack"><div class="row"><span class="spinner"></span><strong id="gp-t">Asignando ${fmt.n(D.plan.entregas)} entregas a ${D.plan.rutas} camiones…</strong></div><div class="progress"><span id="gp-b" style="width:5%"></span></div><p class="small muted" id="gp-s">Restricciones: capacidad, frío, ventanas horarias, ocupación mínima 70 % y ${L.restricciones().filter((x) => x.estado === 'Vigente').length} restricciones de ruta registradas.</p></div>`;
        const msgs = ['Agrupando por zona logística…', 'Respetando ventanas de recepción…', 'Asignando carga refrigerada solo a camiones con frío…', 'Secuenciando y calculando ETA…'];
        for (let i = 0; i < 4; i++) { await L.sleep(600); $('#gp-b', root).style.width = 25 * (i + 1) + '%'; $('#gp-t', root).textContent = msgs[i]; }
        host.innerHTML = `${L.alert('success', 'Plan generado en 11 minutos (simulado)', `${D.plan.rutas} rutas, ${fmt.n(D.plan.entregas)} entregas, ocupación promedio ${Math.round(D.rutas.reduce((a, r, i) => a + planOcc(r, i), 0) / D.rutas.length)} %. Se aplicaron ${L.restricciones().filter((x) => x.estado === 'Vigente').length} restricciones de ruta registradas. Revise y corrija antes de aprobar; cada corrección queda registrada.`)}
          <div class="table-wrap" style="margin-top:var(--sp-4)"><table class="table"><thead><tr><th>Ruta</th><th>Zona</th><th>Camión</th><th class="right">Entregas</th><th class="right">Peso</th><th class="right">Ocupación</th><th>Observación</th></tr></thead><tbody>${D.rutas.map((r, i) => `<tr><td class="mono">${r.id}</td><td>${esc(r.zona)}</td><td>${esc(r.camion)}${r.frio ? ' ' + L.badge('Frío', 'info') : ''}</td><td class="num right" data-ent="${i}">${r.paradas + 2}</td><td class="num right" data-peso="${i}">${fmt.n(2800 + i * 97)} kg</td><td class="num right" data-occ="${i}">${planOcc(r, i)} %</td><td data-obs="${i}">${i === 4 ? L.badge('2 entregas fuera de ventana', 'warning') : i === 9 ? L.badge('Bajo 70 %: consolidar', 'danger') : L.badge('Lista', 'success')}</td></tr>`).join('')}</tbody></table></div>
          <div id="gp-cap" style="margin-top:var(--sp-4)">${L.alert('danger', 'Una ruta no puede salir', `${D.rutas[9] ? D.rutas[9].id : 'R-10'} queda bajo la ocupación mínima de 70 %. Ningún camión sale bajo ese umbral ni sobre su peso, volumen o condición térmica.`, '<button type="button" class="btn btn-secondary btn-sm" id="gp-cons">Consolidar con la ruta vecina</button>')}</div>
          <div class="row" style="justify-content:flex-end;margin-top:var(--sp-4)">${L.can('ruta.planificar') ? `<button type="button" class="btn btn-secondary" id="gp-add">${icon('plus')}Agregar pedido a una ruta</button>` : ''}<button type="button" class="btn btn-secondary" id="gp-sms">${icon('send')}Vista previa de avisos</button>${L.can('ruta.aprobar') ? `<button type="button" class="btn btn-primary" id="gp-ok">${icon('check')}Aprobar plan</button>` : '<span class="small muted">La aprobación es del Planificador de Rutas.</span>'}</div>`;
        let consolidated = false;
        $('#gp-cons', root).onclick = (e) => L.busy(e.currentTarget, () => { consolidated = true; consolidatedPlan = true;
          // Moving 6 deliveries (520 kg) from the neighbouring route R-09 to R-10 lifts R-10 to 82 %
          const mv = (a, b, dEnt, dKg) => { $(`[data-ent="${a}"]`, root).textContent = D.rutas[a].paradas + 2 + dEnt; $(`[data-ent="${b}"]`, root).textContent = D.rutas[b].paradas + 2 - dEnt; $(`[data-peso="${a}"]`, root).textContent = fmt.n(2800 + a * 97 + dKg) + ' kg'; $(`[data-peso="${b}"]`, root).textContent = fmt.n(2800 + b * 97 - dKg) + ' kg'; };
          mv(9, 8, 6, 520);
          $('[data-occ="8"]', root).textContent = planOcc(D.rutas[8], 8) - 6 + ' %';
          const avg = Math.round(D.rutas.reduce((a, r, i) => a + planOcc(r, i) - (i === 8 ? 6 : 0), 0) / D.rutas.length);
          const strong = $('#rt-plan .alert', root); if (strong) strong.innerHTML = strong.innerHTML.replace(/ocupación promedio \d+ %/, `ocupación promedio ${avg} %`);
          $('[data-occ="9"]', root).textContent = '82 %'; $('[data-obs="9"]', root).innerHTML = L.badge('Consolidada · 82 %', 'success'); $('#gp-cap', root).innerHTML = L.alert('success', 'Capacidad y carga dentro de los límites', 'Todas las rutas cumplen peso, volumen, frío y ocupación mínima.'); }, 800);
        if ($('#gp-ok', root)) $('#gp-ok', root).onclick = async () => { if (!consolidated) { L.toast('No se puede aprobar todavía', 'Resuelva la ruta bajo la ocupación mínima.', 'error'); $('#gp-cap', root).scrollIntoView({ block: 'center', behavior: 'smooth' }); return; } if (await L.confirm({ title: '¿Aprobar el plan de mañana?', message: `Se publicarán las rutas a los conductores y a los transportistas, y se programarán ${fmt.n(D.plan.entregas)} avisos SMS.`, confirmLabel: 'Aprobar plan' })) L.toast('Plan aprobado', 'Rutas publicadas a conductores y transportistas.', 'success'); };
        $('#gp-add', root) && ($('#gp-add', root).onclick = () => { const cap = 4000, vol = 22; const peds = [{ id: 'PV-264840', d: 'Supermercado La Esquina · 920 kg · 4,1 m³ · seco', kg: 920, m3: 4.1, frio: false }, { id: 'PV-264843', d: 'Hotel Plaza Talca · 310 kg · 1,6 m³ · refrigerado', kg: 310, m3: 1.6, frio: true }, { id: 'PV-264845', d: 'Minimarket Lircay · 180 kg · 0,9 m³ · seco', kg: 180, m3: 0.9, frio: false }]; L.modal({ title: 'Agregar pedido a una ruta', body: `<div class="form-grid"><div class="field"><label for="ga-p">Pedido <span class="req" aria-hidden="true">*</span></label><select id="ga-p" class="select"><option value="">Seleccione…</option>${peds.map((p, i) => `<option value="${i}">${p.id} · ${p.d}</option>`).join('')}</select></div><div class="field"><label for="ga-r">Ruta <span class="req" aria-hidden="true">*</span></label><select id="ga-r" class="select"><option value="">Seleccione…</option>${D.rutas.map((r, i) => `<option value="${i}">${r.id} · ${esc(r.camion)} · ${r.frio ? 'con frío' : 'seco'} · ${fmt.n(+($(`[data-peso="${i}"]`, root)?.textContent.replace(/\D/g, '') || 0))} kg</option>`).join('')}</select></div></div><div id="ga-e" style="margin-top:12px"></div><p class="hint">Capacidad nominal por camión: ${fmt.n(cap)} kg y ${vol} m³.</p>`, onOpen: (d) => { L.bindField($('#ga-p', d), ['required']); L.bindField($('#ga-r', d), ['required']); }, actions: [{ label: 'Cancelar' }, { label: 'Agregar', cls: 'btn-primary', onClick: (api) => { if (!L.validateAll(api.el)) return false; const p = peds[+$('#ga-p', api.el).value], i = +$('#ga-r', api.el).value, r = D.rutas[i]; const kg = +($(`[data-peso="${i}"]`, root).textContent.replace(/\D/g, '')); const m3 = 14 + (i % 5) * 1.3; const err = p.frio && !r.frio ? `${p.id} lleva productos refrigerados y ${r.camion} no tiene equipo de frío.` : kg + p.kg > cap ? `Excede el peso nominal: ${fmt.n(kg)} + ${fmt.n(p.kg)} = ${fmt.n(kg + p.kg)} kg de ${fmt.n(cap)} kg. Reubique el excedente en otra ruta.` : m3 + p.m3 > vol ? `Excede el volumen nominal: ${fmt.n(m3 + p.m3, 1)} de ${vol} m³.` : ''; if (err) { $('#ga-e', api.el).innerHTML = L.alert('danger', 'No se puede agregar', err); return false; } $(`[data-peso="${i}"]`, root).textContent = fmt.n(kg + p.kg) + ' kg'; $(`[data-ent="${i}"]`, root).textContent = +$(`[data-ent="${i}"]`, root).textContent + 1; L.logAudit('Modificación', 'Ruta', `${p.id} agregado a ${r.id} en el plan de mañana (corrección manual)`); L.toast('Pedido agregado', `${p.id} → ${r.id}; la corrección quedó registrada.`, 'success'); } }] }); });
        $('#gp-sms', root).onclick = () => L.modal({ title: 'Aviso al cliente', body: '<div class="card" style="box-shadow:none;background:var(--c-bg);font-family:var(--font-mono);font-size:var(--fs-sm)">Puelche: su pedido llega mañana entre 09:00 y 09:30. Camión KXTR-21.</div>', actions: [{ label: 'Cerrar', cls: 'btn-primary' }] });
      };
      if ($('#rt-gen', root)) $('#rt-gen', root).onclick = (e) => gen(e.currentTarget);
      root.addEventListener('click', (e) => { if (e.target.closest('[data-gen]')) gen(); });
    }
  });

  /* ---------- Route restrictions and planner knowledge (Case 02, acceptance criterion 16; RF-04.04, RF-04.07) ---------- */
  // What today lives only in Don Hugo's head becomes parameters that the routing engine applies to every plan
  const RESTR_BASE = [
    { id: 'RR-001', tipo: 'Acceso vehicular', ambito: 'Calle Prat, Cauquenes (centro)', regla: 'Sin camiones sobre 8 t de 08:00 a 10:00', motivo: 'Restricción municipal en horario escolar', fuente: 'Entrevista a Hugo Maldonado', estado: 'Vigente', usos: 41 },
    { id: 'RR-002', tipo: 'Acceso vehicular', ambito: 'Puente en el camino a Pelluhue', regla: 'No cruzar con el camión grande: usar camión de hasta 8 t o el desvío por Curanipe', motivo: 'El puente no resiste el peso del camión grande', fuente: 'Entrevista a Hugo Maldonado', estado: 'Vigente', usos: 18 },
    { id: 'RR-003', tipo: 'Horario', ambito: 'Minimarket Villa Alegre', regla: 'Entregar antes de las 11:00', motivo: 'Después la dueña sale a buscar a sus nietos y el local queda cerrado', fuente: 'Entrevista a Hugo Maldonado', estado: 'Vigente', usos: 22 },
    { id: 'RR-004', tipo: 'Zona', ambito: 'Feria libre de Linares (martes)', regla: 'Calle Independencia cerrada de 06:00 a 15:00; entrar por Av. León Bustos', motivo: 'Feria semanal', fuente: 'Entrevista a Hugo Maldonado', estado: 'Vigente', usos: 9 },
    { id: 'RR-005', tipo: 'Secuencia', ambito: 'Costa de Constitución y Empedrado', regla: 'En invierno, ir por la ruta del valle y no por la cuesta costera', motivo: 'Neblina y barro; ya hubo dos camiones atascados', fuente: 'Entrevista a Hugo Maldonado', estado: 'Vigente', usos: 6 },
    { id: 'RR-006', tipo: 'Cliente', ambito: 'Cliente de Longaví', regla: 'No asignar conductores con menos de 3 meses en la ruta', motivo: 'No recibe a conductores nuevos desde que le rompieron una caja', fuente: 'Entrevista a Hugo Maldonado', estado: 'Por validar', usos: 0 },
    { id: 'RR-007', tipo: 'Cliente', ambito: 'Supermercado Regional Maule · Local 12', regla: 'Andén 2 reservado para Puelche de 07:00 a 07:30', motivo: 'Acuerdo con la cadena', fuente: 'Gerencia Comercial', estado: 'Vigente', usos: 30 },
    { id: 'RR-008', tipo: 'Zona', ambito: 'Curicó, sector Aguas Negras', regla: 'No programar después de las 17:00', motivo: 'Seguridad del conductor y de la carga', fuente: 'Entrevista a Hugo Maldonado', estado: 'Vigente', usos: 12 }
  ];
  L.restricciones = () => [...L.store.get('rutas.restr', []), ...RESTR_BASE].map((r) => ({ ...r, ...(L.store.get('rutas.restr.mod', {})[r.id] || {}) }));
  const TIPOS_R = ['Acceso vehicular', 'Horario', 'Cliente', 'Zona', 'Secuencia', 'Vehículo'];

  L.route('/rutas/restricciones', {
    title: 'Restricciones de ruta', parent: '/rutas', block: 'Proceso operacional principal', module: 'M4 Rutas', rf: ['RF-04.04', 'RF-04.07', 'RF-04.02'], actors: ['Planificador de Rutas', 'Gerente de Operaciones'],
    render: () => {
      const rs = L.restricciones();
      const vig = rs.filter((r) => r.estado === 'Vigente').length;
      return `<div class="page-head"><div class="titles"><span class="page-kicker">${icon('route', 'icon-sm')}Planificación</span><h1>Restricciones y conocimiento de ruta</h1><p class="muted" style="margin:0">Lo que hoy sabe solo el planificador queda registrado como reglas que el motor de ruteo aplica en cada plan. Así la operación no depende de una persona.</p></div><div class="actions">${L.can('ruta.restricciones') ? `<button type="button" class="btn btn-primary" id="rr-new">${icon('plus')}Nueva restricción</button>` : ''}</div></div>
        <div class="grid grid-4" style="margin-bottom:var(--sp-5)">${[['Restricciones documentadas', rs.length, 'Meta: 100 % antes de la jubilación'], ['Vigentes en el motor', vig, `${rs.length - vig} por validar en terreno`], ['Aplicadas en el último mes', rs.reduce((a, r) => a + (r.usos || 0), 0), 'Veces que cambiaron una ruta'], ['Plan sin corrección manual', '91 %', 'Antes: 3,5 h de una persona']].map(([a, b, c]) => `<div class="card kpi"><span class="label">${a}</span><span class="value" style="font-size:var(--fs-2xl)">${b}</span><span class="meta">${c}</span></div>`).join('')}</div>
        ${L.alert('info', 'Captura del conocimiento antes de la jubilación', 'Registre aquí cada regla que hoy se aplica de memoria: accesos, horarios, clientes y zonas. Las nuevas quedan «Por validar» hasta que un segundo perfil las confirma en terreno; desde ahí el motor las aplica en cada plan.')}
        <div class="card card-flush" style="margin-top:var(--sp-5)" id="rr-t"></div>`;
    },
    mount: (root) => {
      const tbl = L.dataTable($('#rr-t', root), {
        id: 'rr', caption: 'Restricciones de ruta registradas', rows: () => L.restricciones(), searchKeys: ['ambito', 'regla', 'motivo', 'fuente'], searchPlaceholder: 'Buscar por cliente, calle, zona o regla',
        filters: [{ key: 'tipo', label: 'Tipo', options: TIPOS_R }, { key: 'estado', label: 'Estado', options: ['Vigente', 'Por validar', 'Inactiva'] }],
        columns: [{ key: 'id', label: 'Folio', render: (r) => `<span class="mono">${r.id}</span>` }, { key: 'tipo', label: 'Tipo' }, { key: 'ambito', label: 'Ámbito', wrap: true }, { key: 'regla', label: 'Regla', wrap: true, render: (r) => `${esc(r.regla)}<div class="small muted">${esc(r.motivo)}</div>` }, { key: 'fuente', label: 'Fuente', wrap: true }, { key: 'usos', label: 'Aplicada', right: true, render: (r) => `${r.usos || 0} veces` }, { key: 'estado', label: 'Estado', render: (r) => L.badge(r.estado, r.estado === 'Vigente' ? 'success' : r.estado === 'Por validar' ? 'warning' : '') }],
        rowActions: (r, redraw) => (!L.can('ruta.restricciones') ? [] : [
          ...(r.estado === 'Por validar' ? [{ label: 'Validar en terreno', icon: 'check', onClick: () => { if (r.autor && r.autor === L.me().name) { L.toast('Necesita un segundo perfil', 'Quien registró la restricción no puede validarla.', 'warning'); return; } mod(r.id, { estado: 'Vigente' }); redraw(); L.toast('Restricción vigente', `${r.id}: el motor la aplica desde el próximo plan.`, 'success'); } }] : []),
          r.estado === 'Inactiva' ? { label: 'Reactivar', icon: 'sync', onClick: () => { mod(r.id, { estado: 'Vigente' }); redraw(); } } : { label: 'Desactivar', icon: 'ban', onClick: () => { mod(r.id, { estado: 'Inactiva' }); redraw(); L.toast('Restricción desactivada', 'Se conserva en el historial.', 'info'); } }
        ])
      });
      const mod = (id, patch) => L.store.set('rutas.restr.mod', { ...L.store.get('rutas.restr.mod', {}), [id]: { ...(L.store.get('rutas.restr.mod', {})[id] || {}), ...patch } });
      if ($('#rr-new', root)) $('#rr-new', root).onclick = () => L.modal({
        title: 'Nueva restricción de ruta', size: 'lg',
        body: `<div class="form-grid"><div class="field"><label for="nr-t">Tipo <span class="req" aria-hidden="true">*</span></label><select id="nr-t" class="select"><option value="">Seleccione…</option>${TIPOS_R.map((t) => `<option>${t}</option>`).join('')}</select></div>
          <div class="field combo"><label for="nr-a">Ámbito: cliente, calle o zona <span class="req" aria-hidden="true">*</span></label><input id="nr-a" class="input" placeholder="Ej.: Minimarket Lircay o Av. San Miguel, Talca"></div>
          <div class="field full"><label for="nr-r">Regla que debe aplicar el motor <span class="req" aria-hidden="true">*</span></label><input id="nr-r" class="input" placeholder="Ej.: No entregar los viernes después de las 12:00"></div>
          <div class="field full"><label for="nr-m">Motivo <span class="req" aria-hidden="true">*</span></label><input id="nr-m" class="input" placeholder="Por qué existe la regla"></div>
          <div class="field"><label for="nr-f">Fuente</label><select id="nr-f" class="select"><option>Entrevista a Hugo Maldonado</option><option>Conductor</option><option>Cliente</option><option>Corrección manual del plan</option></select></div></div>
          <p class="hint">Queda «Por validar» hasta que otro perfil la confirme en terreno; luego el motor la aplica en cada plan.</p>`,
        onOpen: (d) => { ['#nr-t', '#nr-a', '#nr-r', '#nr-m'].forEach((s) => L.bindField($(s, d), ['required'])); L.combobox($('#nr-a', d), () => D.clientes.map((c) => ({ label: c.nombre, meta: c.comuna }))); },
        actions: [{ label: 'Cancelar' }, { label: 'Registrar restricción', cls: 'btn-primary', onClick: (api) => {
          if (!L.validateAll(api.el)) return false;
          const e = api.el, id = 'RR-' + String(9 + L.store.get('rutas.restr', []).length).padStart(3, '0');
          L.store.set('rutas.restr', [{ id, tipo: $('#nr-t', e).value, ambito: $('#nr-a', e).value.trim(), regla: $('#nr-r', e).value.trim(), motivo: $('#nr-m', e).value.trim(), fuente: $('#nr-f', e).value, estado: 'Por validar', usos: 0, autor: L.me().name }, ...L.store.get('rutas.restr', [])]);
          tbl.draw(); L.toast('Restricción registrada', `${id} queda por validar en terreno.`, 'success');
        } }]
      });
    }
  });

  L.route('/rutas/:id', {
    title: (p) => (p.id ? `Ruta ${p.id}` : 'Detalle de ruta'), parent: '/rutas', block: 'Proceso operacional principal', module: 'M4 Rutas · M12', rf: ['RF-14.05', 'RF-04.08', 'RF-14.04'], actors: ['Planificador de Rutas'],
    render: ({ id }) => {
      const r = D.rutas.find((x) => x.id === id);
      if (!r) return L.empty('search', 'Ruta no encontrada', `No existe la ruta ${id}.`, '<a class="btn btn-primary" href="#/rutas">Volver a rutas</a>');
      const peds = D.pedidos.filter((p) => p.ruta === id && !p.hist);
      return `<div class="page-head"><div class="titles"><span class="page-kicker">${esc(r.transportista)}</span><h1>${r.id} · ${esc(r.zona)}</h1><p class="muted" style="margin:0">${esc(r.conductor)} · ${esc(r.camion)} · salida ${r.salida} · término estimado ${r.eta}</p></div></div>
        <div class="grid grid-4" style="margin-bottom:var(--sp-5)">${[['Entregas', `${r.hechas}/${r.paradas}`], ['Ocupación', r.ocupacion + ' %'], ['Kilómetros', r.km + ' km'], ['OTIF de la ruta', fmt.pct(r.otif)]].map(([a, b]) => `<div class="card kpi" style="padding:var(--sp-4)"><span class="label">${a}</span><span class="value" style="font-size:var(--fs-2xl)">${b}</span></div>`).join('')}</div>
        ${r.desvio ? L.alert('warning', 'Desvío de 3,4 km sobre la ruta planificada', 'Alerta generada por telemetría. Contacte al conductor o registre la causa.', '<a class="btn btn-secondary btn-sm" href="#/telemetria">Ver en el mapa</a>') + '<div style="height:16px"></div>' : ''}
        <section class="card card-flush"><div class="card-head"><h2>Pedidos de la ruta</h2></div><div class="table-wrap"><table class="table"><thead><tr><th>#</th><th>Pedido</th><th>Cliente</th><th>Ventana</th><th>Estado</th></tr></thead><tbody>${peds.map((p, i) => `<tr><td class="num">${i + 1}</td><td><a class="row-link mono" href="#/pedidos/${p.id}">${p.id}</a></td><td>${esc(p.clienteNombre)}</td><td>${esc(p.ventana)}</td><td>${L.estadoBadge(p.estado)}</td></tr>`).join('')}</tbody></table></div></section>
        <section class="card card-flush" style="margin-top:var(--sp-5)"><div class="card-head"><h2>Costo por entrega realizada</h2>${L.tip('Se calcula al cerrar cada entrega con los km y minutos de telemetría imputados a esa parada.')}</div><div class="table-wrap"><table class="table"><caption class="sr-only">Costo de cada entrega de la ruta</caption><thead><tr><th>Pedido</th><th>Cliente</th><th class="right">Km imputados</th><th class="right">Minutos</th><th class="right">Transporte</th><th class="right">Descarga</th><th class="right">Costo total</th></tr></thead><tbody>${peds.slice(0, Math.max(3, r.hechas)).map((p, i) => { const km = +(r.km / r.paradas * (0.7 + (i % 3) * 0.25)).toFixed(1), min = 9 + (i * 7) % 15, tr = Math.round(km * 690), de = 2400 + min * 210; return `<tr><td class="mono">${p.id}</td><td>${esc(p.clienteNombre)}</td><td class="num right">${fmt.n(km, 1)}</td><td class="num right">${min}</td><td class="num right">${fmt.clp(tr)}</td><td class="num right">${fmt.clp(de)}</td><td class="num right"><strong>${fmt.clp(tr + de)}</strong></td></tr>`; }).join('')}</tbody></table></div><p class="small muted" style="padding:0 var(--sp-5) var(--sp-4)">Alimenta el costo de servir por cliente en <a href="#/analitica/costo">Analítica</a>.</p></section>`;
    }
  });

  /* ---------- Preparación (M5) ---------- */

  const baseMissions = [
    { id: 'M-3301', zona: 'Seco', cantidad: 64, hechas: 64, estado: 'Completada' },
    { id: 'M-3302', zona: 'Refrigerado', cantidad: 42, hechas: 26, estado: 'En curso', practicable: true },
    { id: 'M-3303', zona: 'Congelado', cantidad: 18, hechas: 0, estado: 'Pendiente' },
    { id: 'M-3304', zona: 'Seco', cantidad: 71, hechas: 12, estado: 'En curso' },
    { id: 'M-3305', zona: 'Seco', cantidad: 55, hechas: 0, estado: 'Pendiente' },
    { id: 'M-3306', zona: 'Refrigerado', cantidad: 38, hechas: 0, estado: 'Pendiente' }
  ];
  const generatedMissions = () => L.store.get('preparacion.misiones', []);
  L.prepMissions = () => [...baseMissions, ...generatedMissions().flatMap((m) => {
    const pedido = L.findOrder(m.pedidoId);
    if (!pedido) return [];
    const zonas = [...new Set(pedido.lineas.map((l) => l.temp))];
    return [{ ...m, pedido, zona: zonas.join(' / '), cantidad: pedido.lineas.length, hechas: 0, estado: 'Pendiente', practicable: true }];
  })];
  const missionCard = (m) => `<div class="card" data-mission="${esc(m.id)}">
    <div class="row-between"><strong class="mono">${esc(m.id)}</strong>${L.badge(m.estado, m.estado === 'Completada' ? 'success' : m.estado === 'En curso' ? 'accent' : '')}</div>
    <p class="small muted">${esc(m.zona)} · ${m.cantidad} líneas${m.pedido ? ' · Pedido ' + esc(m.pedido.id) : ''}</p>
    <div class="progress"><span style="width:${m.cantidad ? 100 * m.hechas / m.cantidad : 0}%"></span></div>
    <div class="row-between" style="margin-top:12px"><span class="small num">${m.hechas}/${m.cantidad}</span>${m.practicable && L.allowed('/flujo') ?
      `<a class="btn btn-secondary btn-sm" href="#/flujo?escena=preparacion&amp;mision=${encodeURIComponent(m.id)}">${icon('scan', 'icon-sm')}${m.pedido ? 'Iniciar misión' : 'Abrir práctica'}</a>` :
      '<span class="small muted">Solo consulta</span>'}</div></div>`;
  L.route('/preparacion', {
    title: 'Preparación', parent: '/inicio', block: 'Proceso operacional principal', module: 'M5 Preparación',
    rf: ['RF-05.01', 'RF-05.02', 'RF-05.04', 'RF-05.05', 'RF-09.08', 'RF-02.08', 'RNF-02.01', 'RNF-13.01', 'RNF-09.04'], actors: ['Preparador', 'Jefa de Bodega'],
    render: () => `<div class="page-head"><div class="titles"><h1>Preparación de pedidos</h1><p class="muted">Práctica con pedidos confirmados o en preparación. La generación no cambia los pedidos de origen; las tarjetas históricas son de consulta.</p></div><div class="actions">${L.can('prep.misiones') ? `<button type="button" class="btn btn-primary" id="pp-gen">${icon('zap')}Generar misiones</button>` : ''}</div></div>
      ${L.cdBanner()}<div class="grid grid-3" id="prep-missions">${L.prepMissions().map(missionCard).join('')}</div>`,
    mount: (root) => {
      L.cdWire(root, () => L.router.resolve());
      const generate = $('#pp-gen', root);
      if (!generate) return;
      generate.onclick = () => {
        if (!L.can('prep.misiones')) return;
        const previous = generatedMissions();
        const assigned = new Set(previous.map((m) => m.pedidoId));
        const added = D.pedidos.filter((p) => p.lineas.length && ['Confirmado', 'Planificado', 'En picking'].includes(p.estado) && !assigned.has(p.id))
          .map((p, i) => ({ id: 'M-' + (3307 + previous.length + i), pedidoId: p.id }));
        if (!added.length) { L.toast('No hay pedidos nuevos para preparar', 'No se duplicaron misiones.', 'info'); return; }
        L.store.set('preparacion.misiones', [...previous, ...added]);
        L.cdEvent('Generación de ' + added.length + ' misiones');
        $('#prep-missions', root).innerHTML = L.prepMissions().map(missionCard).join('');
        L.toast('Misiones de práctica generadas', added.length + ' pedidos agregados al listado.', 'success');
      };
    }
  });

  /* ---------- Cobranza y rendición (M7) ---------- */
  L.route('/rendicion', {
    title: 'Cobranza y rendición', parent: '/inicio', block: 'Proceso operacional principal', module: 'M7 Cobranza y rendición', rf: ['RF-07.01', 'RF-07.02', 'RF-07.03', 'RF-07.08', 'RF-11.07', 'RF-07.06', 'RF-07.09', 'RF-07.11'], actors: ['Conductores', 'Gerente de Finanzas'],
    render: () => {
      const rows = D.rutas.map((r, i) => { const esp = 900000 + i * 173000; const dif = [0, -12000, 0, 0, -128500, 0, 3000, 0, 0, -45000, 0, 0][i]; return { id: r.id, zona: r.zona, conductor: r.conductor, esperado: esp, rendido: esp + dif, dif, estado: r.estado === 'Completada' ? (dif ? 'Con descuadre' : 'Cuadrada') : 'En ruta' }; });
      L._rend = rows;
      return `<div class="page-head"><div class="titles"><h1>Cobranza y rendición</h1><p class="muted" style="margin:0">Contraste automático entre lo esperado por camión y turno y lo rendido.</p></div></div>
        <div class="grid grid-3" style="margin-bottom:var(--sp-5)"><div class="card kpi"><span class="label">Esperado hoy</span><span class="value" style="font-size:var(--fs-2xl)">${fmt.clp(rows.reduce((a, r) => a + r.esperado, 0))}</span></div><div class="card kpi"><span class="label">Rendido</span><span class="value" style="font-size:var(--fs-2xl)">${fmt.clp(rows.reduce((a, r) => a + r.rendido, 0))}</span></div><div class="card kpi"><span class="label">Descuadres sin tipificar</span><span class="value" style="font-size:var(--fs-2xl);color:var(--c-danger)">3</span></div></div>
        ${L.alert('info', 'Liquidación automática al volver a base', `${rows.filter((r) => r.estado !== 'En ruta').length} de ${rows.length} camiones ya liquidados: el sistema consolidó documentos entregados, devoluciones recibidas, cobranzas en efectivo y saldo de envases sin digitación. Abra «Ver liquidación» en cada fila.`)}<div style="height:16px"></div>
        ${L.tabsHtml('rdt', [{ id: 'rut', label: 'Rendición por ruta' }, { id: 'web', label: 'Pagos web en revisión' }, { id: 'prev', label: 'Recibos de preventa' }, { id: 'pos', label: 'Vouchers POS' }, { id: 'erp', label: 'Envío al ERP' }], 'rut')}
        <div ${L.panelAttrs('rdt', 'rut', 'rut')}><div class="card card-flush" id="rd-t"></div></div>
        <div ${L.panelAttrs('rdt', 'web', 'rut')}><p class="muted" style="margin-top:0">Pagos que los clientes reportan en el portal. Quedan «En revisión» hasta que el cajero verifica el comprobante; recién entonces se envía la rebaja al ERP.</p><div class="card card-flush" id="rd-web"></div></div>
        <div ${L.panelAttrs('rdt', 'prev', 'rut')}><p class="muted" style="margin-top:0">Recibos provisionales que emitieron los preventistas al cobrar facturas vencidas. Se consolidan en el efectivo que cada uno debe rendir hoy.</p><div class="card card-flush" id="rd-prev"></div></div>
        <div ${L.panelAttrs('rdt', 'pos', 'rut')}><p class="muted" style="margin-top:0">Cobros con tarjeta en ruta: el código de autorización del terminal se concilia solo contra la entrega.</p><div class="card card-flush" id="rd-pos"></div></div>
        <div ${L.panelAttrs('rdt', 'erp', 'rut')}><p class="muted" style="margin-top:0">Comprobantes de recaudación y cierres aprobados se transfieren al ERP de forma asíncrona e idempotente: un reenvío con el mismo identificador no duplica el abono.</p><div class="card card-flush" id="rd-erp"></div></div>`;
    },
    mount: (root) => {
      L.tabs($('.tabs', root));
      const web = [{ id: 'PW-3301', cliente: 'Supermercado La Esquina', monto: 412000, banco: 'Banco Estado', fecha: 'Hoy 08:12', estado: 'En revisión' }, { id: 'PW-3302', cliente: 'Minimarket Santa Elena', monto: 96500, banco: 'BCI', fecha: 'Hoy 09:40', estado: 'En revisión' }, { id: 'PW-3298', cliente: 'Almacén Las Rosas', monto: 58300, banco: 'Santander', fecha: 'Ayer 17:05', estado: 'Aprobado' }];
      L.dataTable($('#rd-web', root), { id: 'rdw', caption: 'Pagos reportados en el portal', rows: web, searchKeys: ['id', 'cliente'], filters: [{ key: 'estado', label: 'Estado', options: ['En revisión', 'Aprobado', 'Rechazado'] }],
        columns: [{ key: 'id', label: 'Pago', render: (r) => `<span class="mono">${r.id}</span>` }, { key: 'cliente', label: 'Cliente' }, { key: 'banco', label: 'Banco' }, { key: 'fecha', label: 'Reportado' }, { key: 'monto', label: 'Monto', right: true, render: (r) => fmt.clp(r.monto) }, { key: 'estado', label: 'Estado', render: (r) => L.badge(r.estado, r.estado === 'Aprobado' ? 'success' : r.estado === 'Rechazado' ? 'danger' : 'warning') }],
        rowActions: (r, redraw) => (r.estado !== 'En revisión' || !L.can('rend.gestionar') ? [] : [{ label: 'Verificar comprobante', icon: 'eye', onClick: () => L.modal({ title: `Comprobante ${r.id}`, body: `<dl class="desc-list"><dt>Cliente</dt><dd>${esc(r.cliente)}</dd><dt>Banco</dt><dd>${esc(r.banco)}</dd><dt>Monto</dt><dd class="num">${fmt.clp(r.monto)}</dd><dt>N.º de operación</dt><dd class="mono">${r.id.slice(3)}88412</dd></dl>`, actions: [{ label: 'Rechazar', onClick: () => { r.estado = 'Rechazado'; redraw(); L.toast('Pago rechazado', 'Se avisó al cliente.', 'info'); } }, { label: 'Aprobar y enviar al ERP', cls: 'btn-primary', onClick: () => { r.estado = 'Aprobado'; redraw(); const msg = `MSG-${77120 + L.erpEnvios.length}`; L.erpEnvios.unshift({ id: msg, tipo: `Rebaja por pago web ${r.id} · ${r.cliente} · ${fmt.clp(r.monto)}`, estado: 'En cola' }); erpTbl.draw(); L.toast('Pago aprobado', `Rebaja ${msg} en cola hacia el ERP; véala en «Envío al ERP».`, 'success'); } }] }) }])
      });
      const recibos = () => (L.preventaRecibos ? L.preventaRecibos() : []).map((r) => ({ ...r, preventista: 'Sandra Riffo', estadoR: r.rendido ? 'Rendido' : 'Por rendir' }));
      L.dataTable($('#rd-prev', root), { id: 'rdp', caption: 'Recibos provisionales de preventa', rows: recibos, searchKeys: ['id', 'cliente'],
        columns: [{ key: 'id', label: 'Recibo', render: (r) => `<span class="mono">${r.id}</span>` }, { key: 'preventista', label: 'Preventista' }, { key: 'cliente', label: 'Cliente' }, { key: 'hora', label: 'Hora' }, { key: 'monto', label: 'Monto', right: true, render: (r) => fmt.clp(r.monto) }, { key: 'estadoR', label: 'Estado', render: (r) => L.badge(r.estadoR, r.rendido ? 'success' : 'warning') }],
        rowActions: (r, redraw) => (r.rendido || !L.can('rend.gestionar') ? [] : [{ label: 'Recibir en caja', icon: 'cash', onClick: () => { L.store.set('preventa.recibos', L.preventaRecibos().map((x) => (x.id === r.id ? { ...x, rendido: true } : x))); redraw(); L.toast('Efectivo recibido', `${r.id}: ${fmt.clp(r.monto)} rendido en caja.`, 'success'); } }])
      });
      const vouchers = () => [...L.store.get('pos.vouchers', []), { code: '418832', card: '4417', monto: 126400, cliente: 'Minimarket El Roble' }, { code: '402215', card: '9081', monto: 74900, cliente: 'Botillería Los Aromos' }].map((v) => ({ ...v, conciliado: 'Conciliado' }));
      L.dataTable($('#rd-pos', root), { id: 'rdv', key: 'code', caption: 'Vouchers POS de la ruta', rows: vouchers, searchKeys: ['code', 'cliente'],
        columns: [{ key: 'code', label: 'Autorización', render: (r) => `<span class="mono">${r.code}</span>` }, { key: 'cliente', label: 'Cliente' }, { key: 'card', label: 'Tarjeta', render: (r) => `•••• ${r.card}` }, { key: 'monto', label: 'Monto', right: true, render: (r) => fmt.clp(r.monto) }, { key: 'conciliado', label: 'Conciliación', render: () => L.badge('Conciliado con la entrega', 'success') }]
      });
      L.erpEnvios = L.erpEnvios || [{ id: 'MSG-77120', tipo: 'Cierre comercial R-01', estado: 'Confirmado por el ERP' }, { id: 'MSG-77121', tipo: 'Recaudación R-03', estado: 'Confirmado por el ERP' }, { id: 'MSG-77122', tipo: 'Recaudación R-07', estado: 'En cola' }];
      const erpTbl = L.dataTable($('#rd-erp', root), { id: 'rde', caption: 'Envíos al ERP', rows: () => L.erpEnvios, searchKeys: ['id', 'tipo'],
        columns: [{ key: 'id', label: 'Mensaje', render: (r) => `<span class="mono">${r.id}</span>` }, { key: 'tipo', label: 'Comprobante' }, { key: 'estado', label: 'Estado', render: (r) => L.badge(r.estado, r.estado === 'En cola' ? 'warning' : 'success') }],
        rowActions: (r, redraw) => !L.can('rend.gestionar') ? [] : [{ label: 'Reenviar', icon: 'sync', onClick: () => { if (r.estado === 'En cola') { r.estado = 'Confirmado por el ERP'; redraw(); L.toast('Comprobante transferido', `${r.id} aplicado en cuentas por cobrar.`, 'success'); } else L.toast('Sin duplicado', `${r.id} ya estaba aplicado: el ERP reconoció el identificador y no repitió el abono.`, 'info'); } }]
      });
      L.dataTable($('#rd-t', root), {
        id: 'rd', caption: 'Rendiciones por ruta', rows: L._rend, searchKeys: ['id', 'zona', 'conductor'], filters: [{ key: 'estado', label: 'Estado', options: ['Cuadrada', 'Con descuadre', 'En ruta'] }],
        columns: [{ key: 'id', label: 'Ruta', render: (r) => `<span class="mono">${r.id}</span>` }, { key: 'zona', label: 'Zona' }, { key: 'conductor', label: 'Conductor' }, { key: 'esperado', label: 'Esperado', right: true, render: (r) => fmt.clp(r.esperado) }, { key: 'rendido', label: 'Rendido', right: true, render: (r) => fmt.clp(r.rendido) }, { key: 'dif', label: 'Diferencia', right: true, render: (r) => `<span style="color:${r.dif ? 'var(--c-danger)' : 'inherit'}">${r.dif ? (r.dif > 0 ? '+' : '−') + fmt.clp(Math.abs(r.dif)) : '—'}</span>` }, { key: 'estado', label: 'Estado', render: (r) => L.badge(r.estado, r.estado === 'Cuadrada' ? 'success' : r.estado === 'Con descuadre' ? 'danger' : 'accent') }],
        rowActions: (r, redraw) => [...(L.can('rend.gestionar') && r.dif && r.estado !== 'Cuadrada' ? [{ label: 'Tipificar descuadre', icon: 'edit', onClick: () => L.modal({ title: `Tipificar descuadre ${r.id}`, body: `<p>Diferencia de ${fmt.clp(Math.abs(r.dif))}.</p><div class="field"><label for="tp-c">Causal <span class="req" aria-hidden="true">*</span></label><select id="tp-c" class="select"><option value="">Seleccione…</option><option>Vuelto mal entregado</option><option>Billete rechazado</option><option>Abono parcial no registrado</option></select></div><div class="field" style="margin-top:12px"><label class="check"><input type="checkbox" id="tp-f"> Firmo digitalmente como responsable</label></div>`, onOpen: (d) => { L.bindField($('#tp-c', d), ['required']); L.bindField($('#tp-f', d), [(v) => (v ? '' : 'La firma es obligatoria.')]); }, actions: [{ label: 'Cancelar' }, { label: 'Registrar', cls: 'btn-primary', onClick: (api) => { if (!L.validateAll(api.el)) return false; r.estado = 'Cuadrada'; redraw(); L.toast('Descuadre tipificado', 'Firma y responsable registrados en la bitácora.', 'success'); } }] }) }] : []), { label: 'Ver liquidación', icon: 'file', onClick: () => L.modal({ title: `Liquidación ${r.id} · ${r.conductor}`, body: r.estado === 'En ruta' ? L.alert('info', 'Camión en ruta', 'La liquidación se procesa automáticamente cuando el camión vuelve a base y sincroniza.') : `<p class="small muted" style="margin-top:0">Procesada automáticamente al retornar a base, 18:42.</p><dl class="desc-list"><dt>Documentos tributarios entregados</dt><dd>${14 + r.zona.length % 6} guías · ${12 + r.zona.length % 5} facturas</dd><dt>Devoluciones físicas recibidas</dt><dd>3 líneas · 41 unidades</dd><dt>Cobranza en efectivo</dt><dd>${fmt.clp(r.rendido)} de ${fmt.clp(r.esperado)}</dd><dt>Abonos parciales</dt><dd>1 · saldo a cuenta corriente</dd><dt>Saldo de envases</dt><dd>18 canastillos retornados</dd><dt>Resultado</dt><dd>${r.dif ? L.badge('Descuadre ' + fmt.clp(Math.abs(r.dif)), 'danger') : L.badge('Cuadrada', 'success')}</dd></dl>`, actions: [{ label: 'Cerrar', cls: 'btn-primary' }] }) }, ...(L.allowed('/rutas') ? [{ label: 'Ver ruta', icon: 'route', onClick: () => L.go('/rutas/' + r.id) }] : [])]
      });
    }
  });
})(window.LFX);
