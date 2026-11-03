/* Perfil de terreno: app de reparto y app de preventa (Kotlin en TC58e), versión móvil
   con comportamiento sin conexión simulado (SD4 §4.1.16 y Anexo 4-J; RT-03.10, RT-03.13). */
(function (L) {
  const { esc, icon, $, $$, data: D, fmt } = L;

  const stops = () => L.store.get('field.stops', null) || D.paradas.map((p) => ({ id: p.id, estado: p.estado }));
  const setStop = (id, estado) => { const s = stops(); s.find((x) => x.id === id).estado = estado; L.store.set('field.stops', s); };
  const queue = () => L.store.get('field.queue', []);
  const setQueue = (q) => L.store.set('field.queue', q);
  L.fieldDone = () => stops().filter((s) => s.estado !== 'Pendiente').length;

  const deviceShell = (title, body, { back, tabs, active, fab } = {}) => `
    <div class="device"><div class="device-status" aria-hidden="true"><span>09:42</span><span class="row" style="gap:6px">${icon(L.online() ? 'wifi' : 'wifi-off', 'icon-sm')}<span>87 %</span></span></div>
    <div class="device-screen" id="dev">
      <div class="app-bar">${back ? `<button type="button" class="btn btn-tertiary btn-icon" data-dback="${back}" aria-label="Volver">${icon('arrow-left')}</button>` : `<img src="assets/logo.svg" alt="" width="26" height="28">`}<h2>${esc(title)}</h2><label class="switch" title="Simular conectividad"><input type="checkbox" id="dev-net" ${L.online() ? 'checked' : ''} aria-label="Conectividad del dispositivo (simulación)"></label></div>
      <div class="net-banner ${L.online() ? 'online' : 'offline'}" role="status">${icon(L.online() ? 'wifi' : 'wifi-off', 'icon-sm')}<span class="grow">${L.online() ? 'En línea · todo sincronizado' : `Sin conexión · ${queue().length} evento(s) en cola`}</span>${!L.online() ? '<span class="small">Turno de 14 h</span>' : ''}</div>
      <div class="app-body">${body}</div>
      ${fab || ''}
      ${tabs ? `<nav class="app-tabbar" aria-label="Navegación de la app">${tabs.map(([id, ic, lb]) => `<button type="button" data-dtab="${id}" ${active === id ? 'aria-current="page"' : ''}>${icon(ic)}<span>${lb}</span>${id === 'cola' && queue().length ? `<span class="badge badge-warning plain" style="padding:0 6px;position:absolute;margin-left:28px;margin-top:-30px">${queue().length}</span>` : ''}</button>`).join('')}</nav>` : ''}
    </div></div>`;

  // Sincronización automática al reconectar (RF-06.07, RNG-12)
  const syncQueue = async (onDone) => {
    const q = queue();
    if (!q.length) return onDone?.();
    L.toast('Señal recuperada', `Sincronizando ${q.length} evento(s)…`, 'info', { duration: 2000 });
    await L.sleep(1400);
    setQueue([]);
    L.toast('Sincronización completa', `${q.length} evento(s) enviados sin duplicados ni pérdidas.`, 'success');
    onDone?.();
  };

  /* ---------- App de reparto ---------- */
  L.route('/terreno', {
    title: 'Reparto en terreno', parent: '/inicio', block: 'Perfil de terreno', module: 'M6 Reparto · M7 · M8', rf: ['RF-06.01', 'RF-06.02', 'RF-06.04', 'RF-06.05', 'RF-06.07', 'RF-06.09', 'RF-06.11', 'RF-07.06', 'RF-09.06', 'RF-06.13', 'RF-09.12', 'RNG-12', 'RF-06.10', 'RF-06.12', 'RF-07.10', 'RF-09.07', 'RF-09.13'], actors: ['Conductor propio', 'Conductor externo'],
    render: () => `<div class="page-head hide-sm"><div class="titles"><span class="page-kicker">${icon('phone', 'icon-sm')}Perfil de terreno · app de reparto</span><h1>App de reparto · ruta R-01 Cauquenes</h1><p class="muted" style="margin:0">Vista móvil del conductor. Use el interruptor de la barra superior de la app para simular la pérdida de señal.</p></div><div class="actions"><button type="button" class="btn btn-secondary" id="tr-reset">${icon('sync')}Reiniciar ruta</button></div></div>
      <div class="split"><div id="tr-host"></div><aside class="card hide-sm stack"><h2>Qué funciona sin conexión</h2><p class="small muted" style="margin:0">Según SD4, Anexo 4-J.</p>
        <ul class="list">${[['Entrega y prueba de entrega', 'Captura 14 h · cola cifrada', 'success'], ['Cobro en efectivo', 'Comprobante local', 'success'], ['Devoluciones y envases', 'Se registran en el dispositivo', 'success'], ['Mapas', 'Precargados con la ruta', 'success'], ['Autorización POS', 'No disponible: efectivo o crédito autorizado', 'danger'], ['Recalcular ruta', 'No disponible: secuencia precargada', 'danger']].map(([t, d, k]) => `<li><span class="badge badge-${k} plain" style="padding:4px">${icon(k === 'success' ? 'check' : 'ban', 'icon-sm')}</span><div class="grow"><div class="title">${t}</div><div class="sub">${d}</div></div></li>`).join('')}</ul></aside></div>`,
    mount: (root) => {
      const S = { screen: 'ruta', stop: null };
      const host = $('#tr-host', root);
      const tabs = [['ruta', 'route', 'Ruta'], ['cola', 'sync', 'Cola'], ['frio', 'thermo', 'Frío'], ['mas', 'menu', 'Más']];
      const draw = () => {
        const st = stops();
        let title = 'Mi ruta', body = '', back = '';
        if (S.screen === 'ruta') {
          const done = st.filter((s) => s.estado !== 'Pendiente').length;
          body = `<div class="card" style="padding:var(--sp-4)"><div class="row"><div class="ring" style="--p:${Math.round((done / st.length) * 100)}" data-label="${done}/${st.length}"></div><div><strong>R-01 Cauquenes</strong><div class="small muted">KXTR-21 · con equipo de frío</div><div class="small muted">Credencial válida hasta 21:15</div></div></div></div>
            <ol class="list" aria-label="Entregas de la ruta">${D.paradas.map((p, i) => { const e = st[i].estado; return `<li><button type="button" class="btn btn-tertiary" data-stop="${p.id}" style="width:100%;justify-content:flex-start;text-align:left;min-height:64px;padding:0 4px;font-weight:400"><span class="avatar ${e === 'Pendiente' ? 'dark' : ''}" style="width:36px;height:36px">${e === 'Pendiente' ? i + 1 : icon(e === 'Entregado' ? 'check' : 'alert', 'icon-sm')}</span><span class="grow" style="min-width:0"><strong style="display:block;white-space:normal">${esc(p.nombre)}</strong><span class="small muted">${esc(p.ventana)} · ${p.bultos} bultos${p.frio ? ' · frío' : ''}</span></span>${e !== 'Pendiente' ? L.badge(e, e === 'Entregado' ? 'success' : 'warning') : icon('chev-right')}</button></li>`; }).join('')}</ol>`;
        } else if (S.screen === 'parada') {
          const p = D.paradas.find((x) => x.id === S.stop);
          const e = st.find((x) => x.id === p.id).estado;
          title = p.nombre; back = 'ruta';
          body = `<dl class="desc-list"><dt>Dirección</dt><dd>${esc(p.dir)}</dd><dt>Ventana</dt><dd>${esc(p.ventana)}</dd><dt>Pedido</dt><dd class="mono">${esc(p.pedido)}</dd><dt>Bultos</dt><dd>${p.bultos}${p.frio ? ' · incluye frío' : ''}</dd><dt>Cobro</dt><dd>${p.contado ? 'Contado ' + fmt.clp(p.monto) : 'Crédito 30 días'}</dd></dl>
            ${p.frio ? L.alert('success', 'Cadena de frío vigente', 'Latido del sensor válido · 3,4 °C. Se habilita la bajada del SSCC (RF-09.12).') : ''}
            ${e === 'Pendiente' ? `<button type="button" class="btn btn-secondary btn-block big-btn" data-nav>${icon('pin')}Navegar ${L.online() ? '' : '(mapa precargado)'}</button><button type="button" class="btn btn-primary btn-block big-btn" data-arrive>${icon('check')}Llegué: iniciar entrega</button>` : L.alert(e === 'Entregado' ? 'success' : 'warning', `Parada ${e.toLowerCase()}`, e === 'Entregado' ? 'Prueba de entrega registrada.' : 'Reprogramada a la próxima ventana compatible.')}`;
        } else if (S.screen === 'entrega') {
          const p = D.paradas.find((x) => x.id === S.stop);
          title = 'Entrega · ' + p.nombre; back = 'parada';
          body = '<div id="dv-host"></div>';
        } else if (S.screen === 'cola') {
          const q = queue();
          title = 'Cola de sincronización';
          body = q.length ? `<p class="small muted">Eventos guardados en el dispositivo con identificador único. Se envían solos al recuperar señal o al volver al CD.</p><ul class="list">${q.map((x) => `<li>${icon(x.icon)}<div class="grow"><div class="title">${esc(x.t)}</div><div class="sub mono">${esc(x.uuid)} · ${esc(x.at)}</div></div>${L.badge('En cola', 'warning')}</li>`).join('')}</ul>${L.online() ? `<button type="button" class="btn btn-primary btn-block" data-sync>${icon('sync')}Sincronizar ahora</button>` : L.alert('info', 'Sin señal', 'Nada se pierde: la cola persiste aunque se reinicie el equipo.')}` : L.empty('done', 'Todo sincronizado', 'No hay eventos pendientes de envío.');
        } else if (S.screen === 'frio') {
          title = 'Cadena de frío';
          body = `<div class="card" style="padding:var(--sp-4)"><div class="row-between"><strong>Compartimento refrigerado</strong>${L.badge('Normal', 'success')}</div><div style="font-size:var(--fs-3xl);font-weight:700" class="num">3,4 °C</div><div class="small muted">Consigna 4 °C · sensor independiente 3,6 °C</div></div>
            ${L.charts.line(['07:00', '07:30', '08:00', '08:30', '09:00', '09:30'], [{ name: 'Temperatura', values: [3.8, 3.5, 4.4, 3.9, 3.6, 3.4] }], { w: 340, h: 180, label: 'Temperatura del compartimento en la ruta', min: 0, target: 8 })}
            <p class="small muted">Sin móvil ni satélite, las alarmas locales siguen operando y retienen el SSCC afectado (Anexo 4-J).</p>`;
        } else if (S.screen === 'mas') {
          title = 'Más opciones';
          body = `<ul class="list">
            <li><button type="button" class="btn btn-tertiary" style="width:100%;justify-content:flex-start" data-pos ${L.online() ? '' : 'aria-disabled="true"'}>${icon('cash')}<span class="grow" style="text-align:left">Cobro con tarjeta (POS)<span class="small muted" style="display:block">${L.online() ? 'Terminal emparejado por Bluetooth' : 'No disponible sin conexión'}</span></span></button></li>
            <li><a class="btn btn-tertiary" style="width:100%;justify-content:flex-start" href="#/devoluciones/nueva">${icon('undo')}<span class="grow" style="text-align:left">Registrar devolución</span></a></li>
            <li><a class="btn btn-tertiary" style="width:100%;justify-content:flex-start" href="#/rendicion">${icon('file')}<span class="grow" style="text-align:left">Rendir el turno</span></a></li>
            <li><button type="button" class="btn btn-tertiary" style="width:100%;justify-content:flex-start" data-print>${icon('printer')}<span class="grow" style="text-align:left">Imprimir comprobante (RF-06.13)</span></button></li></ul>`;
        }
        host.innerHTML = deviceShell(title, body, { back, tabs, active: ['parada', 'entrega'].includes(S.screen) ? 'ruta' : S.screen });
        if (S.screen === 'entrega') {
          const p = D.paradas.find((x) => x.id === S.stop);
          const ped = L.findOrder(p.pedido);
          L.delivery($('#dv-host', host), {
            stop: { ...p, ventana: p.ventana }, compact: true,
            lines: ped.lineas.slice(0, 4).map((l) => ({ nombre: l.nombre, cant: l.cant, precio: Math.round(p.monto / ped.lineas.slice(0, 4).reduce((a, x) => a + x.cant, 0)) })),
            onDone: (r) => { setStop(p.id, 'Entregado'); if (!L.online()) setQueue([...queue(), { t: `Entrega ${p.nombre}`, icon: 'check', uuid: 'pod-' + Math.random().toString(16).slice(2, 8), at: '09:4' + queue().length }, ...(r.cash ? [{ t: `Cobro ${fmt.clp(r.cash)}`, icon: 'cash', uuid: 'cob-' + Math.random().toString(16).slice(2, 8), at: '09:4' + queue().length }] : [])]); S.screen = 'ruta'; draw(); },
            onClosed: (r) => { setStop(p.id, 'Reprogramada'); if (!L.online()) setQueue([...queue(), { t: `Local cerrado ${p.nombre}`, icon: 'door', uuid: 'evt-' + Math.random().toString(16).slice(2, 8), at: '09:5' + queue().length }]); S.screen = 'ruta'; draw(); }
          });
        }
        $('#dev-net', host).onchange = (e) => { L.setOnline(e.target.checked); if (e.target.checked) syncQueue(draw); else { L.toast('Sin conexión', 'Siga trabajando: todo queda en el dispositivo.', 'warning'); draw(); } };
        $$('[data-dtab]', host).forEach((b) => (b.onclick = () => { S.screen = b.dataset.dtab; draw(); }));
        $('[data-dback]', host) && ($('[data-dback]', host).onclick = () => { S.screen = $('[data-dback]', host).dataset.dback; draw(); });
        $$('[data-stop]', host).forEach((b) => (b.onclick = () => { S.stop = b.dataset.stop; S.screen = 'parada'; draw(); }));
        $('[data-arrive]', host) && ($('[data-arrive]', host).onclick = () => { S.screen = 'entrega'; draw(); });
        $('[data-nav]', host) && ($('[data-nav]', host).onclick = () => L.toast(L.online() ? 'Navegación iniciada' : 'Mapa precargado', L.online() ? 'ETA 6 min · 2,1 km' : 'Sin recálculo en línea: siga la secuencia precargada.', 'info'));
        $('[data-sync]', host) && ($('[data-sync]', host).onclick = () => syncQueue(draw));
        $('[data-pos]', host) && ($('[data-pos]', host).onclick = () => (L.online() ? L.toast('Terminal POS listo', 'Acerque la tarjeta del cliente.', 'info') : L.modal({ title: 'Cobro con tarjeta no disponible', icon: 'warning:wifi-off', body: '<p>Sin conexión no se puede autorizar un pago con tarjeta. Cobre en efectivo o registre el crédito autorizado del cliente; nunca se presenta una captura POS como pago autorizado (SD4 §4.1.16).</p>', actions: [{ label: 'Entendido', cls: 'btn-primary' }] })));
        $('[data-print]', host) && ($('[data-print]', host).onclick = (e) => L.busy(e.currentTarget, () => L.toast('Comprobante impreso', 'Impresora portátil ZQ220.', 'success'), 900));
        $('#dev', host).scrollTop = 0;
      };
      document.addEventListener('lfx:net', draw);
      L.onLeave(() => document.removeEventListener('lfx:net', draw));
      $('#tr-reset', root) && ($('#tr-reset', root).onclick = () => { L.store.set('field.stops', null); setQueue([]); S.screen = 'ruta'; draw(); L.toast('Ruta reiniciada', '', 'info'); });
      draw();
    }
  });

  /* ---------- App de preventa ---------- */
  L.route('/terreno/preventa', {
    title: 'Preventa en terreno', parent: '/inicio', block: 'Perfil de terreno', module: 'M3 Preventa', rf: ['RF-03.02', 'RF-03.05', 'RF-03.06', 'RF-03.13', 'RF-03.15', 'RF-07.05', 'RF-08.04', 'RF-07.11'], actors: ['Preventista'],
    render: () => `<div class="page-head hide-sm"><div class="titles"><span class="page-kicker">${icon('phone', 'icon-sm')}Perfil de terreno · app de preventa</span><h1>App de preventa · zona Curicó</h1><p class="muted" style="margin:0">Visitas del día, ficha comercial y toma de pedido sin señal.</p></div><div class="actions"><a class="btn btn-secondary" href="#/flujo">Ver el pedido en el flujo completo</a></div></div>
      <div id="pv-host"></div>`,
    mount: (root) => {
      const S = { screen: 'visitas', cli: null, cart: [] };
      const host = $('#pv-host', root);
      const mine = D.clientes.filter((c) => c.preventista === 'Sandra Riffo').slice(0, 7);
      const draw = () => {
        let title = 'Visitas de hoy', body = '', back = '', fab = '';
        if (S.screen === 'visitas') {
          body = `<div class="input-wrap">${icon('search')}<label class="sr-only" for="pv-q">Buscar cliente</label><input id="pv-q" class="input" type="search" placeholder="Buscar cliente"></div>
            <ul class="list" id="pv-list">${mine.map((c, i) => `<li><button type="button" class="btn btn-tertiary" data-cli="${c.id}" style="width:100%;justify-content:flex-start;text-align:left;min-height:60px;padding:0 4px;font-weight:400"><span class="small num" style="width:40px">${9 + i}:${i % 2 ? '30' : '00'}</span><span class="grow"><strong style="display:block">${esc(c.nombre)}</strong><span class="small muted">${esc(c.comuna)} · ${esc(c.canal)}</span></span>${c.vencida ? L.badge('Mora', 'danger') : c.envases.canastillos > 40 ? L.badge('Envases', 'warning') : ''}</button></li>`).join('')}</ul>`;
          fab = `<button type="button" class="fab" style="position:sticky;margin:0 16px 16px auto;bottom:16px;align-self:flex-end" data-fab>${icon('plus')}Pedido</button>`;
        } else if (S.screen === 'cliente') {
          const c = L.findClient(S.cli);
          title = c.nombre; back = 'visitas';
          body = `<div class="grid grid-2" style="gap:8px"><div class="card" style="padding:12px;box-shadow:none"><div class="small muted">Crédito disponible</div><strong class="num">${fmt.clp(c.credito - c.deuda)}</strong></div><div class="card" style="padding:12px;box-shadow:none"><div class="small muted">Deuda vencida</div><strong class="num" style="${c.vencida ? 'color:var(--c-danger)' : ''}">${fmt.clp(c.vencida)}</strong></div></div>
            <p class="small muted" style="margin:0">${L.online() ? 'Datos en línea' : 'Última sincronización: hoy 06:00 (hace 3 h 42 min)'}</p>
            ${c.vencida ? L.alert('danger', 'Cliente con mora', 'Deuda vencida sobre 30 días: el pedido quedará sujeto a autorización (RF-07.05).') + `<button type="button" class="btn btn-secondary btn-block" data-collect style="margin-top:var(--sp-2)">${icon('cash')}Cobrar facturas vencidas</button>` : ''}
            ${c.envases.canastillos > 40 ? L.alert('warning', 'Saldo de envases sobre el umbral', `${c.envases.canastillos} canastillos en poder del cliente (RF-08.04).`) : ''}
            <h3>Compra habitual (RF-03.06)</h3><ul class="list">${D.productos.slice(0, 4).map((p, i) => `<li><span class="grow"><span class="title">${esc(p.nombre)}</span><span class="sub" style="display:block">Cada ${[7, 7, 14, 10][i]} días · última: ${[12, 24, 6, 18][i]} u</span></span><button type="button" class="btn btn-secondary btn-sm" data-add="${p.sku}">${icon('plus', 'icon-sm')}Agregar</button></li>`).join('')}</ul>
            <button type="button" class="btn btn-primary btn-block big-btn" data-order>${icon('cart')}Tomar pedido</button>`;
        } else if (S.screen === 'pedido') {
          const c = L.findClient(S.cli);
          title = 'Pedido · ' + c.nombre; back = 'cliente';
          const tot = S.cart.reduce((a, l) => a + l.cant * l.precio, 0);
          body = `<div class="field combo"><label for="pv-add">Agregar producto</label><input id="pv-add" class="input" placeholder="Nombre o SKU"></div>
            ${S.cart.length ? `<ul class="list">${S.cart.map((l, i) => `<li><span class="grow"><span class="title">${esc(l.nombre)}</span><span class="sub" style="display:block">${fmt.clp(l.precio)} · stock ${L.online() ? '' : '(06:00) '}${fmt.n(l.stock)}</span></span><button type="button" class="btn btn-secondary btn-icon btn-sm" data-cq="${i}" data-d="-1" aria-label="Restar">${icon('minus', 'icon-sm')}</button><strong class="num" style="min-width:28px;text-align:center">${l.cant}</strong><button type="button" class="btn btn-secondary btn-icon btn-sm" data-cq="${i}" data-d="1" aria-label="Sumar">${icon('plus', 'icon-sm')}</button></li>`).join('')}</ul>` : L.empty('box', 'Pedido vacío', 'Busque un producto o agregue desde la compra habitual.')}
            <div class="row-between"><span class="muted">Entrega: sáb 14-11 · ${esc(c.ventana)}</span><strong class="num">${fmt.clp(tot)}</strong></div>
            <button type="button" class="btn btn-primary btn-block big-btn" data-save ${S.cart.length ? '' : 'disabled'}>${icon(L.online() ? 'send' : 'download')}${L.online() ? 'Enviar pedido' : 'Guardar sin conexión'}</button>`;
        }
        host.innerHTML = deviceShell(title, body, { back, fab, tabs: [['visitas', 'list', 'Visitas'], ['cola', 'sync', 'Cola'], ['clientes', 'store', 'Clientes'], ['mas', 'menu', 'Más']], active: 'visitas' });
        $('#dev-net', host).onchange = (e) => { L.setOnline(e.target.checked); if (e.target.checked) syncQueue(draw); else { L.toast('Sin conexión', 'Puede seguir tomando pedidos.', 'warning'); draw(); } };
        $('[data-dback]', host) && ($('[data-dback]', host).onclick = () => { S.screen = $('[data-dback]', host).dataset.dback; draw(); });
        $$('[data-dtab]', host).forEach((b) => (b.onclick = () => { if (b.dataset.dtab === 'clientes') L.go('/clientes'); else if (b.dataset.dtab === 'cola') L.toast(`${queue().length} evento(s) en cola`, queue().length ? 'Se enviarán al reconectar.' : 'Todo sincronizado.', 'info'); else if (b.dataset.dtab === 'mas') L.go('/pedidos'); else { S.screen = 'visitas'; draw(); } }));
        $$('[data-cli]', host).forEach((b) => (b.onclick = () => { S.cli = b.dataset.cli; S.cart = []; S.screen = 'cliente'; draw(); }));
        $('#pv-q', host) && ($('#pv-q', host).oninput = (e) => { const v = e.target.value.toLowerCase(); $$('#pv-list li', host).forEach((li) => (li.hidden = !li.textContent.toLowerCase().includes(v))); });
        $('[data-fab]', host) && ($('[data-fab]', host).onclick = () => { S.cli = mine[0].id; S.cart = []; S.screen = 'pedido'; draw(); });
        $$('[data-add]', host).forEach((b) => (b.onclick = () => { const p = D.productos.find((x) => x.sku === b.dataset.add); S.cart.push({ ...p, cant: 12 }); L.toast('Agregado al pedido', p.nombre, 'success', { duration: 1500 }); b.disabled = true; }));
        $('[data-order]', host) && ($('[data-order]', host).onclick = () => { S.screen = 'pedido'; draw(); });
        // Cobranza en efectivo de facturas vencidas en el local, con recibo provisional y rendición del día (RF-07.11)
        $('[data-collect]', host) && ($('[data-collect]', host).onclick = () => { const c = L.findClient(S.cli); const facts = [['FE-71204', Math.round(c.vencida * 0.6)], ['FE-70988', c.vencida - Math.round(c.vencida * 0.6)]]; L.modal({
          title: 'Cobrar facturas vencidas',
          body: `<ul class="list">${facts.map(([f, m], i) => `<li><label class="check" style="width:100%"><input type="checkbox" data-fc="${m}" checked> <span class="grow mono">${f}</span><span class="num">${fmt.clp(m)}</span></label></li>`).join('')}</ul>
            <div class="field" style="margin-top:var(--sp-3)"><label for="cb-m">Monto recibido en efectivo <span class="req" aria-hidden="true">*</span></label><div class="input-group"><span class="addon">$</span><input id="cb-m" class="input num" inputmode="numeric" value="${c.vencida}"></div></div>
            <p class="hint">Se emite un recibo provisional digital. El efectivo debe rendirse hoy en caja; si no, el turno queda con descuadre.</p>`,
          onOpen: (d) => L.bindField($('#cb-m', d), ['required', (v) => (parseInt(String(v).replace(/\D/g, ''), 10) > 0 ? '' : 'Ingrese el monto recibido.')]),
          actions: [{ label: 'Cancelar' }, { label: 'Emitir recibo provisional', cls: 'btn-primary', onClick: (api) => { if (!L.validateAll(api.el)) return false; const m = parseInt($('#cb-m', api.el).value.replace(/\D/g, ''), 10); const id = 'RP-' + (5120 + queue().length); if (!L.online()) setQueue([...queue(), { t: `Recibo ${id} · ${c.nombre}`, icon: 'cash', uuid: 'rcb-' + Math.random().toString(16).slice(2, 8), at: '09:4' + queue().length }]); L.toast(`Recibo provisional ${id} emitido`, `${fmt.clp(m)} · debe rendirse hoy en caja.`, 'success'); } }]
        }); });
        $$('[data-cq]', host).forEach((b) => (b.onclick = () => { const l = S.cart[b.dataset.cq]; l.cant += Number(b.dataset.d); if (l.cant <= 0) S.cart.splice(b.dataset.cq, 1); draw(); }));
        if ($('#pv-add', host)) L.combobox($('#pv-add', host), () => D.productos.map((p) => ({ label: p.nombre, meta: p.sku, p })), { onSelect: (it) => { S.cart.push({ ...it.p, cant: 6 }); draw(); } });
        $('[data-save]', host) && ($('[data-save]', host).onclick = (e) => L.busy(e.currentTarget, () => {
          const id = 'PV-' + (264830 + queue().length);
          if (!L.online()) { setQueue([...queue(), { t: `Pedido ${id} · ${L.findClient(S.cli).nombre}`, icon: 'cart', uuid: crypto.randomUUID ? crypto.randomUUID().slice(0, 18) : 'uuid-' + Date.now(), at: '09:4' + queue().length }]); L.toast('Pedido guardado sin conexión', `${id} con identificador único; se enviará al reconectar.`, 'success'); }
          else L.toast('Pedido enviado', `${id} pendiente de validación de stock y crédito.`, 'success');
          S.screen = 'visitas'; draw();
        }, 700));
        $('#dev', host).scrollTop = 0;
      };
      draw();
    }
  });
})(window.LFX);
