/* Proceso operacional principal (7 pasos, de extremo a extremo):
   preventa sin conexión → sincronización y validación → ruta → picking FEFO →
   carga y guía electrónica → entrega con prueba digital → rendición.
   Incluye la excepción más frecuente: local cerrado (RF-06.04, RNG-05). */
(function (L) {
  const { esc, icon, $, $$, data: D, fmt } = L;

  const STEPS = [
    { t: 'Preventa', who: 'Sandra Riffo · App de preventa', mod: 'M3', rf: 'RF-03.01 a RF-03.15' },
    { t: 'Validación', who: 'Servicio de sincronización · M3, M2, M7', mod: 'M3 · M2 · M7', rf: 'RF-03.03, RF-03.09, RF-03.16' },
    { t: 'Ruta', who: 'Hugo Maldonado · Consola de planificación', mod: 'M4', rf: 'RF-04.01 a RF-04.06' },
    { t: 'Picking FEFO', who: 'Matías Lagos · App de bodega (HHT)', mod: 'M5', rf: 'RF-05.02 a RF-05.05' },
    { t: 'Carga y guía', who: 'Jefa de Bodega · CD Talca', mod: 'M5 · ERP', rf: 'RF-05.06, RF-05.07, RF-09.11' },
    { t: 'Entrega', who: 'Jonathan Curihual · App de reparto', mod: 'M6', rf: 'RF-06.01 a RF-06.12' },
    { t: 'Rendición', who: 'Conductor y Tesorería · M7', mod: 'M7', rf: 'RF-07.01 a RF-07.03' }
  ];
  const STEP_STATES = [['Capturado sin conexión'], ['Pendiente de validación', 'Retenido', 'Confirmado'], ['Planificado'], ['En picking'], ['Cargado', 'En ruta'], ['Entregado', 'Parcial', 'Fallido', 'Reprogramado', 'En ruta'], ['Rendido']];
  const STATES = ['Capturado sin conexión', 'Pendiente de validación', 'Confirmado', 'Planificado', 'En picking', 'Cargado', 'En ruta', 'Entregado', 'Rendido'];

  const newOrder = () => {
    const cli = D.clientes[0];
    return {
      id: 'PV-264822', uuid: '', cli, lines: [
        { ...pick('Leche entera · 1 L'), cant: 24 },
        { ...pick('Arroz grado 1 · 1 kg'), cant: 20 },
        { ...pick('Bebida cola · 3 L'), cant: 12 },
        { ...pick('Helado vainilla · 1 L'), cant: 6 }
      ],
      promo: false, estado: 'Borrador', step: 0, maxStep: 0, offline: true, simCredit: false, held: false,
      route: { pos: 2 }, picked: {}, short: null, loaded: false, guia: '', delivered: null, reprog: null, closedAttempt: false, rendido: false,
      log: []
    };
  };
  const pick = (name) => { const p = D.productos.find((x) => x.nombre === name); return { sku: p.sku, nombre: p.nombre, temp: p.temp, precio: p.precio, stock: p.stock }; };
  const subtotal = (o) => o.lines.reduce((a, l) => a + l.cant * l.precio, 0);
  const extraDisc = (o) => (o.extra ? Math.round((subtotal(o) - (o.promo ? Math.floor(o.lines[2].cant / 3) * o.lines[2].precio : 0)) * o.extra.pct / 100) : 0);
  const discount = (o) => (o.promo ? Math.floor(o.lines[2].cant / 3) * o.lines[2].precio : 0) + extraDisc(o);
  const total = (o) => subtotal(o) - discount(o);

  let O = null;
  const setState = (estado, note) => { O.estado = estado; O.log.unshift({ at: new Date(), estado, note }); L.announce(`Estado del pedido: ${estado}`); };
  const nowTime = () => new Date().toLocaleTimeString('es-CL', { hour: '2-digit', minute: '2-digit', second: '2-digit' });

  L.route('/flujo', {
    title: 'Flujo de pedido', parent: '/pedidos', block: 'Proceso operacional principal', module: 'M3 · M2 · M4 · M5 · M6 · M7', rf: ['RF-03.01', 'RF-03.03', 'RF-03.09', 'RF-03.15', 'RF-03.16', 'RF-04.01', 'RF-04.06', 'RF-05.02', 'RF-05.05', 'RF-05.07', 'RF-06.01', 'RF-06.02', 'RF-06.04', 'RF-07.02', 'RF-07.03', 'RF-03.04', 'RF-03.07', 'RF-03.08', 'RF-03.10', 'RF-03.14', 'RF-05.03', 'RF-05.06', 'RF-06.03', 'RF-07.09', 'RF-09.11', 'RNG-01', 'RNG-03', 'RNG-05', 'RNG-08', 'RNG-12', 'RNG-13', 'RNG-15', 'RNG-16', 'RNG-17', 'RF-02.08', 'RNF-05.02', 'RF-06.10', 'RF-06.12', 'RF-07.10', 'RF-09.07', 'RF-04.02', 'RF-04.04'], actors: ['Preventista', 'Planificador de Rutas', 'Preparador', 'Jefa de Bodega', 'Conductor', 'Gerente de Finanzas'],
    render: () => `<div class="page-head"><div class="titles"><span class="page-kicker">${icon('activity', 'icon-sm')}Proceso principal · de punta a punta</span><h1>Flujo de un pedido: de la preventa a la rendición</h1><p class="muted" style="margin:0">Simule el pedido PV-264822 de Almacén Doña Rosa en los 7 pasos, incluidos los estados intermedios y la excepción «local cerrado».</p></div>
        <div class="actions"><button type="button" class="btn btn-secondary" id="fl-reset">${icon('sync')}Reiniciar simulación</button></div></div>
      <div id="fl-stepper"></div>
      <div class="split"><div id="fl-main" class="stack-lg"></div><aside class="stack-lg" id="fl-side"></aside></div>`,
    mount: (root, params, q) => {
      const draftKey = L.draftKey('flujo');
      O = !q.nuevo ? L.store.get(draftKey, null) || newOrder() : newOrder();
      O.log.forEach((entry) => { entry.at = new Date(entry.at); });
      $('.page-head .actions', root).insertAdjacentHTML('afterbegin', '<button type="button" class="btn btn-secondary" id="fl-draft">Guardar borrador</button>');
      L.registerDraft(() => { L.store.set(draftKey, O); L.toast('Borrador guardado', 'Puede retomarlo en esta pestaña con este perfil. No se envió ninguna transacción.', 'success'); });
      $('#fl-draft', root).onclick = () => L.saveDraft();
      L.onLeave(() => { L.store.set(draftKey, O); });
      const draw = () => {
        $('#fl-stepper', root).innerHTML = `<ol class="stepper" aria-label="Pasos del proceso">${STEPS.map((s, i) => { const cls = O.estado === 'Fallido' && i === 5 ? 'error' : i === O.step && !(i === 6 && O.rendido) ? 'current' : i < O.maxStep || (i === 6 && O.rendido) ? 'done' : ''; const can = i <= O.maxStep && i !== O.step && !(i === 6 && O.rendido && O.step === 6); return `<li class="${cls}"><${can ? 'button type="button"' : 'div'} class="step" ${can ? `data-go="${i}"` : ''} ${i === O.step ? 'aria-current="step"' : ''}><span class="bar"></span><span class="lbl">${esc(s.t)}<span class="sr-only">${cls === 'done' ? ' (completado)' : cls === 'current' ? ' (paso actual)' : ''}</span></span></${can ? 'button' : 'div'}></li>`; }).join('')}</ol>`;
        side();
        const s = STEPS[O.step];
        $('#fl-main', root).innerHTML = `<section class="card" aria-labelledby="fl-h"><div class="card-head"><div><span class="small muted">Paso ${O.step + 1} de 7 · ${esc(s.who)}</span><h2 id="fl-h" tabindex="-1" style="margin-top:4px">${esc(s.t)}</h2></div><div class="row"><span class="badge plain mono">${esc(s.mod)}</span><span class="badge plain">${esc(s.rf)}</span></div></div><div id="fl-body"></div></section>`;
        if (O.step < O.maxStep) {
          const notes = O.log.filter((l) => STEP_STATES[O.step].includes(l.estado)).reverse();
          $('#fl-body', root).innerHTML = `${L.alert('success', 'Paso completado', 'Este paso ya se ejecutó. Su registro queda en la bitácora del pedido.')}<ul class="list" style="margin-top:var(--sp-3)">${notes.map((l) => `<li><span class="mono small">${l.at.toLocaleTimeString('es-CL')}</span><span class="grow">${esc(l.estado)} · ${esc(l.note || '')}</span></li>`).join('')}</ul><div class="row" style="justify-content:flex-end;margin-top:var(--sp-4)"><button type="button" class="btn btn-primary" data-go="${O.maxStep}">Volver al paso actual${icon('arrow-right')}</button></div>`;
          return;
        }
        [preventa, validacion, ruta, picking, carga, entrega, rendicion][O.step]($('#fl-body', root));
      };
      const side = () => {
        const reached = (st) => O.log.some((l) => l.estado === st);
        $('#fl-side', root).innerHTML = `<section class="card"><div class="card-head"><h2>Pedido ${esc(O.id)}</h2>${O.estado === 'Borrador' ? L.badge('Borrador') : L.estadoBadge(O.estado)}</div>
            <dl class="desc-list"><dt>Cliente</dt><dd><a href="#/clientes/${O.cli.id}">${esc(O.cli.nombre)}</a></dd><dt>Comuna</dt><dd>${esc(O.cli.comuna)}</dd><dt>Ventana</dt><dd>${O.reprog ? `<s class="muted">${esc(O.cli.ventana)}</s> ${esc(O.reprog)}` : esc(O.cli.ventana)}</dd><dt>Líneas</dt><dd>${O.lines.length} · ${O.lines.reduce((a, l) => a + l.cant, 0)} u</dd><dt>Total</dt><dd class="num">${fmt.clp(total(O))}</dd>${O.uuid ? `<dt>UUID local</dt><dd class="mono small">${esc(O.uuid)}</dd>` : ''}${O.guia ? `<dt>Guía electrónica</dt><dd class="mono">${esc(O.guia)}</dd>` : ''}</dl></section>
          <section class="card"><div class="card-head"><h2>Estados del pedido</h2></div><ol class="timeline">${STATES.map((st) => {
            const cur = O.estado === st || (st === 'Confirmado' && O.estado === 'Retenido') || (st === 'Entregado' && ['Parcial', 'Fallido', 'Reprogramado'].includes(O.estado));
            const label = st === 'Confirmado' && (O.held || O.estado === 'Retenido') ? 'Retenido → Confirmado' : st === 'Entregado' && O.closedAttempt ? 'Fallido → Reprogramado → Entregado' : st === 'Entregado' && O.estado === 'Parcial' ? 'Entregado parcial' : st;
            const err = cur && ['Retenido', 'Fallido'].includes(O.estado);
            const done = !cur && reached(st);
            const entry = O.log.find((l) => l.estado === st);
            return `<li class="${err ? 'error' : cur ? 'current' : done ? 'done' : ''}"><span class="dot"></span><div class="t-title ${!cur && !done ? 'pending' : ''}">${esc(cur && !['Retenido', 'Fallido', 'Reprogramado', 'Parcial'].includes(O.estado) ? st : cur ? O.estado : label)}</div>${entry ? `<div class="t-meta">${entry.at.toLocaleTimeString('es-CL', { hour: '2-digit', minute: '2-digit' })} · ${esc(entry.note || '')}</div>` : ''}</li>`;
          }).join('')}</ol></section>
          <section class="card"><div class="card-head"><h2>Bitácora auditable</h2>${L.tip('Cada transición queda registrada con persona, fecha y hora (RF-17.04).')}</div>${O.log.length ? `<ul class="list">${O.log.slice(0, 6).map((l) => `<li><span class="mono small">${l.at.toLocaleTimeString('es-CL')}</span><span class="grow small">${esc(l.estado)}${l.note ? ' · ' + esc(l.note) : ''}</span></li>`).join('')}</ul>` : '<p class="small muted">Sin eventos todavía.</p>'}</section>`;
      };
      const next = () => { O.step++; O.maxStep = Math.max(O.maxStep, O.step); draw(); $('#fl-h', root).focus(); window.scrollTo({ top: 0, behavior: 'smooth' }); };

      /* Paso 1 · Preventa sin conexión */
      function preventa(b) {
        const c = O.cli;
        const over = total(O) + c.vencida > c.credito * 0.4;
        b.innerHTML = `
          <div class="net-banner ${O.offline ? 'offline' : 'online'}" style="border-radius:var(--radius-sm);margin-bottom:var(--sp-4)">${icon(O.offline ? 'wifi-off' : 'wifi')}<span class="grow">${O.offline ? 'Sin señal en el local: el pedido se guarda en el dispositivo' : 'En línea: stock y crédito en tiempo real'}</span><label class="switch"><input type="checkbox" id="pv-net" ${O.offline ? '' : 'checked'} aria-label="Simular conectividad"> <span class="small">Señal</span></label></div>
          <div class="grid grid-3" style="margin-bottom:var(--sp-4)">
            <div class="card" style="box-shadow:none;padding:var(--sp-4)"><div class="small muted">Crédito disponible ${L.tip(O.offline ? 'Dato de la última sincronización válida, con su antigüedad visible (RF-03.05).' : 'Dato en línea desde el ERP (RF-03.04).')}</div><div class="num" style="font-size:var(--fs-xl);font-weight:700">${fmt.clp(c.credito - c.deuda)}</div><div class="small muted">${O.offline ? 'Sincronizado hoy 06:00 · hace 3 h 30 min' : 'Actualizado ahora'}</div></div>
            <div class="card" style="box-shadow:none;padding:var(--sp-4)"><div class="small muted">Deuda vencida</div><div class="num" style="font-size:var(--fs-xl);font-weight:700">${fmt.clp(c.vencida)}</div><div class="small muted">Límite ${fmt.clp(c.credito)}</div></div>
            <div class="card" style="box-shadow:none;padding:var(--sp-4)"><div class="small muted">Entrega comprometida ${L.tip('Pedido antes de las 14:00 en zona urbana: promesa 24 h (RNG-15, RF-03.13).')}</div><div style="font-size:var(--fs-lg);font-weight:700">Sáb 14-11</div><div class="small muted">Ventana ${esc(c.ventana)}</div></div>
          </div>
          <div class="field combo" style="margin-bottom:var(--sp-3)"><label for="pv-add">Agregar producto</label><div class="input-wrap">${icon('search')}<input id="pv-add" class="input" placeholder="Escriba nombre o SKU (p. ej. «yogur»)"></div></div>
          <div class="row" style="margin-bottom:var(--sp-3)"><span class="small muted">Sugeridos por historial (RF-03.14):</span>${['Yogur batido frutilla · 125 g', 'Aceite maravilla · 1 L', 'Papel higiénico · 12 rollos'].map((n) => `<button type="button" class="chip" data-sug="${esc(n)}">${icon('plus', 'icon-sm')}${esc(n.split(' ·')[0])}</button>`).join('')}</div>
          <div class="table-wrap" style="border:1px solid var(--c-line-soft)"><table class="table"><caption class="sr-only">Líneas del pedido</caption><thead><tr><th>Producto</th><th class="right">Stock ${O.offline ? '(06:00)' : ''}</th><th class="right">Precio</th><th>Cantidad</th><th class="right">Subtotal</th><th><span class="sr-only">Quitar</span></th></tr></thead>
          <tbody>${O.lines.map((l, i) => `<tr><td class="wrap"><strong>${esc(l.nombre)}</strong><div class="small muted mono">${esc(l.sku)} ${l.temp !== 'Seco' ? '· ' + esc(l.temp) : ''}</div></td><td class="num right">${fmt.n(l.stock)}</td><td class="num right">${fmt.clp(l.precio)}</td><td><div class="row" style="flex-wrap:nowrap;gap:4px"><button type="button" class="btn btn-secondary btn-icon btn-sm" data-q="${i}" data-d="-1" aria-label="Restar una unidad de ${esc(l.nombre)}">${icon('minus', 'icon-sm')}</button><input class="input num" style="width:64px;text-align:center" value="${l.cant}" data-qi="${i}" inputmode="numeric" aria-label="Cantidad de ${esc(l.nombre)}"><button type="button" class="btn btn-secondary btn-icon btn-sm" data-q="${i}" data-d="1" aria-label="Sumar una unidad de ${esc(l.nombre)}">${icon('plus', 'icon-sm')}</button></div></td><td class="num right">${fmt.clp(l.cant * l.precio)}</td><td><button type="button" class="btn btn-tertiary btn-icon" data-rm="${i}" aria-label="Quitar ${esc(l.nombre)}">${icon('trash')}</button></td></tr>`).join('')}</tbody></table></div>
          <div class="row-between" style="margin-top:var(--sp-4)">
            <div class="stack" style="gap:var(--sp-1)"><label class="check"><input type="checkbox" id="pv-promo" ${O.promo ? 'checked' : ''}> Aplicar promoción vigente 3×2 en bebidas (RF-03.07)</label>
            ${O.extra ? `<span class="small">${L.badge(`Descuento excepcional ${O.extra.pct} %`, 'success')} autorizado por ${esc(O.extra.by)} · ${esc(O.extra.why)} (RNG-16)</span>` : `<button type="button" class="btn btn-tertiary btn-sm" id="pv-extra" style="align-self:flex-start">${icon('key', 'icon-sm')}Solicitar descuento excepcional</button>`}</div>
            <div style="text-align:right"><div class="small muted">Subtotal ${fmt.clp(subtotal(O))}${O.promo ? ` · descuento −${fmt.clp(discount(O))}` : ''}</div><div style="font-size:var(--fs-xl);font-weight:700" class="num">Total ${fmt.clp(total(O))}</div></div>
          </div>
          ${over ? `<div style="margin-top:var(--sp-3)">${L.alert('warning', 'El pedido supera el crédito disponible del cliente', 'Puede guardarlo: al sincronizar, el sistema revalida el crédito y, si excede el umbral, lo retiene para autorización (RF-03.08, RNG-03).')}</div>` : ''}
          <div class="row-between" style="margin-top:var(--sp-5)"><span class="small muted">El precio acordado queda fijo en el pedido (RNG-08).</span><button type="button" class="btn btn-primary big-btn" id="pv-save">${icon(O.offline ? 'download' : 'send')}${O.offline ? 'Guardar pedido sin conexión' : 'Enviar pedido'}</button></div>`;
        $('#pv-net', b).onchange = (e) => { O.offline = !e.target.checked; preventa(b); };
        $('#pv-extra', b) && ($('#pv-extra', b).onclick = () => L.modal({
          title: 'Descuento excepcional',
          body: `<p class="muted" style="margin-top:0">Las promociones vigentes las aplica el preventista. Todo descuento fuera de ellas requiere autorización del supervisor comercial antes de confirmar, con pedido, monto y motivo registrados (RNG-16).</p>
            <div class="form-grid"><div class="field"><label for="xd-p">Descuento (%) <span class="req" aria-hidden="true">*</span></label><input id="xd-p" class="input num" inputmode="numeric" value="5"></div>
            <div class="field"><label for="xd-m">Motivo <span class="req" aria-hidden="true">*</span></label><select id="xd-m" class="select"><option value="">Seleccione…</option><option>Igualar precio de la competencia</option><option>Compra por volumen fuera de promoción</option><option>Compensación por entrega fallida</option></select></div></div>`,
          onOpen: (d) => { L.bindField($('#xd-p', d), ['required', (v) => (+v > 0 && +v <= 15 ? '' : 'Ingrese un porcentaje entre 1 y 15.')]); L.bindField($('#xd-m', d), ['required']); },
          actions: [{ label: 'Cancelar' }, { label: 'Enviar al supervisor', cls: 'btn-primary', onClick: async (api) => { if (!L.validateAll(api.el)) return false; const pct = +$('#xd-p', api.el).value, why = $('#xd-m', api.el).value; L.toast('Solicitud enviada', 'Esperando autorización del supervisor comercial…', 'info', { duration: 1800 }); await L.sleep(1500); O.extra = { pct, why, by: 'Rubén Salinas, supervisor comercial' }; setState(O.estado, `Descuento excepcional ${pct} % autorizado · ${why}`); L.toast('Descuento autorizado', `${pct} % · queda registrado quién autorizó, monto y motivo.`, 'success'); preventa(b); } }]
        }));
        $('#pv-promo', b).onchange = (e) => { O.promo = e.target.checked; preventa(b); if (O.promo) L.toast('Promoción aplicada', `3×2 en ${O.lines[2]?.nombre || 'bebidas'}: −${fmt.clp(discount(O))}`, 'success'); };
        $$('[data-q]', b).forEach((x) => (x.onclick = () => { const l = O.lines[x.dataset.q]; l.cant = Math.max(1, l.cant + Number(x.dataset.d)); preventa(b); $(`[data-q="${x.dataset.q}"][data-d="${x.dataset.d}"]`, b).focus(); }));
        $$('[data-qi]', b).forEach((x) => (x.onchange = () => { const v = parseInt(x.value, 10); if (!(v > 0)) { L.toast('Cantidad no válida', 'Ingrese un número entero mayor que cero.', 'error'); x.value = O.lines[x.dataset.qi].cant; return; } O.lines[x.dataset.qi].cant = v; preventa(b); }));
        $$('[data-rm]', b).forEach((x) => (x.onclick = () => { if (O.lines.length === 1) { L.toast('El pedido necesita al menos una línea', '', 'warning'); return; } const [rm] = O.lines.splice(x.dataset.rm, 1); preventa(b); L.toast('Línea quitada', rm.nombre, 'info', { action: 'Deshacer', onAction: () => { O.lines.splice(x.dataset.rm, 0, rm); preventa(b); } }); }));
        const add = (name) => { if (O.lines.some((l) => l.nombre === name)) { L.toast('Ya está en el pedido', 'Ajuste la cantidad en la tabla.', 'info'); return; } O.lines.push({ ...pick(name), cant: 6 }); preventa(b); L.toast('Producto agregado', name, 'success', { duration: 2000 }); };
        $$('[data-sug]', b).forEach((x) => (x.onclick = () => add(x.dataset.sug)));
        L.combobox($('#pv-add', b), () => D.productos.map((p) => ({ label: p.nombre, meta: `${p.sku} · ${p.temp}` })), { onSelect: (it) => add(it.label) });
        $('#pv-save', b).onclick = (e) => L.busy(e.currentTarget, () => {
          O.uuid = 'a3f2c9e1-' + Math.random().toString(16).slice(2, 6) + '-4b7d-9e21';
          if (O.offline) { setState('Capturado sin conexión', 'UUID generado en el dispositivo (RF-03.15)'); L.toast('Pedido guardado en el dispositivo', 'Se enviará al recuperar la señal.', 'success'); }
          else { setState('Capturado sin conexión', 'Captura en línea'); setState('Pendiente de validación', 'Enviado al servidor'); }
          next();
        }, 800);
      }

      /* Paso 2 · Sincronización y validación */
      function validacion(b) {
        b.innerHTML = `
          ${O.estado === 'Capturado sin conexión' ? L.alert('warning', '1 pedido en la cola del dispositivo', `El pedido ${esc(O.id)} espera señal. La sincronización es automática al reconectar o al volver al CD (RF-06.07).`) : ''}
          <label class="check" style="margin-top:var(--sp-3)"><input type="checkbox" id="vl-sim" ${O.simCredit ? 'checked' : ''}> Simular que el cliente excede su crédito en más del 10 % (genera estado «Retenido»)</label>
          <ol class="list" id="vl-steps" style="margin-top:var(--sp-3)">
            ${[['sync', 'Recepción en el servidor central y control de duplicados', 'RF-03.16 · RNG-12'], ['box', 'Reserva firme de stock por orden de llegada', 'RF-03.03 · RNG-01'], ['cash', 'Revalidación de crédito y deuda vencida', 'RF-03.09 · RNG-03'], ['calendar', 'Confirmación de fecha y ventana de entrega', 'RF-03.13 · RNG-15']].map(([i, t, r], k) => `<li data-k="${k}"><span class="avatar" style="border-radius:10px">${icon(i)}</span><div class="grow"><div class="title">${t}</div><div class="sub">${r}</div></div><span class="vl-st small muted">En espera</span></li>`).join('')}
          </ol>
          <div id="vl-out" style="margin-top:var(--sp-4)"></div>
          <div class="row" style="justify-content:flex-end;margin-top:var(--sp-4)"><button type="button" class="btn btn-primary big-btn" id="vl-go">${icon('wifi')}Recuperar señal y sincronizar</button></div>`;
        $('#vl-sim', b).onchange = (e) => (O.simCredit = e.target.checked);
        $('#vl-go', b).onclick = async (e) => {
          const btn = e.currentTarget;
          btn.disabled = true;
          if (O.estado === 'Capturado sin conexión') setState('Pendiente de validación', 'Sincronizado al recuperar señal');
          side();
          const rows = $$('#vl-steps li', b);
          for (let k = 0; k < rows.length; k++) {
            const st = rows[k].querySelector('.vl-st');
            st.innerHTML = '<span class="spinner" aria-hidden="true"></span>';
            await L.sleep(650);
            if (k === 2 && O.simCredit) { st.innerHTML = L.badge('Excede 14 %', 'danger'); break; }
            st.innerHTML = L.badge(k === 1 ? '4 de 4 líneas reservadas' : 'Correcto', 'success');
          }
          if (O.simCredit) {
            setState('Retenido', 'Crédito excedido en 14 % (umbral 10 %)');
            O.held = true;
            side();
            $('#vl-out', b).innerHTML = `${L.alert('danger', 'Pedido retenido por crédito', 'El pedido más la deuda vencida supera el límite en 14 %. Solo un supervisor de crédito puede autorizar el envío (RF-03.10).')}
              <form class="card" style="box-shadow:none;margin-top:var(--sp-3)" id="vl-auth" novalidate><h3>Autorización del supervisor</h3><div class="form-grid">
                <div class="field"><label for="vl-mot">Motivo <span class="req" aria-hidden="true">*</span></label><select id="vl-mot" class="select" required><option value="">Seleccione…</option><option>Cliente con historial de pago puntual</option><option>Abono comprometido esta semana</option><option>Excepción comercial autorizada por gerencia</option></select></div>
                <div class="field"><label for="vl-sup">Supervisor</label><input id="vl-sup" class="input" value="Patricio Vergara U." readonly></div>
                <div class="field full"><label for="vl-com">Comentario</label><textarea id="vl-com" class="textarea" placeholder="Opcional"></textarea></div></div>
                <div class="row" style="justify-content:flex-end;margin-top:var(--sp-3)"><button type="button" class="btn btn-secondary" id="vl-rej">Rechazar pedido</button><button type="submit" class="btn btn-primary">${icon('check')}Autorizar y confirmar</button></div></form>`;
            L.bindField($('#vl-mot', b), ['required']);
            $('#vl-rej', b).onclick = async () => { if (await L.confirm({ title: '¿Rechazar el pedido?', message: 'El cliente y la preventista recibirán el aviso. Esta acción queda registrada en la auditoría.', confirmLabel: 'Rechazar pedido', danger: true })) { L.toast('Pedido rechazado', 'Para continuar la simulación, autorícelo.', 'warning'); } };
            $('#vl-auth', b).onsubmit = (ev) => { ev.preventDefault(); if (!L.validateAll(ev.target)) return; L.busy($('#vl-auth [type=submit]', b), () => { setState('Confirmado', 'Autorizado por supervisor de crédito'); L.toast('Pedido confirmado', 'Autorización registrada con supervisor, monto y motivo.', 'success'); next(); }); };
            btn.remove();
            return;
          }
          setState('Confirmado', 'Stock reservado y crédito validado');
          $('#vl-out', b).innerHTML = L.alert('success', 'Pedido confirmado', 'Se notificó a Almacén Doña Rosa la fecha comprometida: sábado 14-11, ' + esc(O.cli.ventana) + '.');
          btn.outerHTML = `<button type="button" class="btn btn-primary big-btn" id="vl-next">Continuar a planificación${icon('arrow-right')}</button>`;
          $('#vl-next', b).onclick = next;
          $('#vl-next', b).focus();
        };
      }

      /* Paso 3 · Ruta */
      function ruta(b) {
        const others = ['Botillería Los Aromos', 'Almacén El Copihue', 'Panadería La Espiga', 'Almacén Las Camelias', 'Almacén Empedrado Centro'];
        const seq = [...others];
        seq.splice(O.route.pos, 0, '★ ' + O.cli.nombre);
        const eta = (i) => { const m = 8 * 60 + 40 + i * 32; return `${String(Math.floor(m / 60)).padStart(2, '0')}:${String(m % 60).padStart(2, '0')}`; };
        const inWin = (i) => { const [a, bb] = O.cli.ventana.split('–'); return eta(i) >= a && eta(i) <= bb; };
        const pts = seq.map((_, i) => [60 + i * 88 + (i % 2) * 14, 60 + Math.sin(i * 1.3) * 36 + (i % 3) * 18]);
        b.innerHTML = `
          ${L.alert('info', 'Ruta propuesta generada en 11 minutos', 'El motor asignó el pedido a la ruta R-01 Cauquenes respetando capacidad, frío y ventanas (RF-04.01). El planificador puede corregir y cada corrección queda registrada.')}
          <div class="grid grid-2" style="margin-top:var(--sp-4)">
            <div><svg class="map" viewBox="0 0 580 170" role="img" aria-label="Mapa esquemático de la ruta R-01 con ${seq.length} paradas"><rect x="0" y="0" width="580" height="170" fill="var(--c-surface-2)"/><path d="M0 120 Q150 80 300 130 T580 100" stroke="var(--c-line-soft)" stroke-width="18" fill="none"/>
              <polyline points="${pts.map((p) => p.join(',')).join(' ')}" fill="none" stroke="var(--chart-2)" stroke-width="3" stroke-dasharray="6 5"/>
              ${pts.map((p, i) => `<g><circle cx="${p[0]}" cy="${p[1]}" r="${seq[i].startsWith('★') ? 15 : 12}" fill="${seq[i].startsWith('★') ? 'var(--c-accent)' : 'var(--c-surface)'}" stroke="var(--c-ink)" stroke-width="2"/><text x="${p[0]}" y="${p[1] + 4}" text-anchor="middle" style="font-weight:700;fill:var(--c-ink);font-size:12px">${i + 1}</text></g>`).join('')}</svg>
              <div class="stack" style="margin-top:var(--sp-3)"><div><div class="row-between small"><span>Peso</span><span class="num">3.180 de 4.000 kg</span></div><div class="progress dark"><span style="width:79.5%"></span></div></div><div><div class="row-between small"><span>Volumen</span><span class="num">17,4 de 22 m³</span></div><div class="progress dark"><span style="width:79%"></span></div></div>
              <div class="row"><span class="badge badge-success">${icon('snow', 'icon-sm')}Camión con equipo de frío</span><span class="badge badge-success">Ocupación sobre 70 %</span></div></div></div>
            <div><h3>Secuencia de entregas</h3><ol class="list" aria-label="Secuencia de la ruta">${seq.map((n, i) => `<li><span class="avatar ${n.startsWith('★') ? '' : 'dark'}" style="width:32px;height:32px">${i + 1}</span><div class="grow"><div class="title">${esc(n.replace('★ ', ''))}${n.startsWith('★') ? ' ' + L.badge('Este pedido', 'accent') : ''}</div><div class="sub">ETA ${eta(i)}${n.startsWith('★') ? ` · ventana ${esc(O.cli.ventana)} ${inWin(i) ? '✓' : '— fuera de ventana'}` : ''}</div></div>${n.startsWith('★') ? `<button type="button" class="btn btn-secondary btn-icon btn-sm" data-mv="-1" aria-label="Adelantar entrega" ${i === 0 ? 'disabled' : ''}>${icon('chev-up', 'icon-sm')}</button><button type="button" class="btn btn-secondary btn-icon btn-sm" data-mv="1" aria-label="Retrasar entrega" ${i === seq.length - 1 ? 'disabled' : ''}>${icon('chev-down', 'icon-sm')}</button>` : ''}</li>`).join('')}</ol>
              ${!inWin(O.route.pos) ? L.alert('warning', 'La entrega quedaría fuera de la ventana del cliente', 'Muévala para cumplir la ventana pactada (RF-04.04).') : ''}</div>
          </div>
          <div class="row" style="justify-content:flex-end;margin-top:var(--sp-5)"><button type="button" class="btn btn-primary big-btn" id="rt-ok" ${inWin(O.route.pos) ? '' : 'disabled'}>${icon('check')}Aprobar ruta y avisar al cliente</button></div>`;
        $$('[data-mv]', b).forEach((x) => (x.onclick = () => { O.route.pos = Math.max(0, Math.min(5, O.route.pos + Number(x.dataset.mv))); ruta(b); L.announce('ETA recalculada'); L.toast('Secuencia corregida', 'La tabla de ruteo y las ETA se recalcularon (RF-04.02).', 'info', { duration: 2400 }); }));
        $('#rt-ok', b).onclick = () => L.modal({
          title: 'Aviso al cliente', icon: 'info:phone',
          body: `<p class="muted">Vista previa del SMS que se enviará antes de la salida del camión (RF-04.06):</p><div class="card" style="box-shadow:none;background:var(--c-bg);font-family:var(--font-mono);font-size:var(--fs-sm)">Puelche: su pedido ${esc(O.id)} llega el sáb 14-11 entre ${eta(O.route.pos)} y ${eta(O.route.pos).replace(/:(\d\d)/, (m, mm) => ':' + String((+mm + 30) % 60).padStart(2, '0'))}. Camión KXTR-21. Siga su entrega en puelche.cl/e/7Q2</div>`,
          actions: [{ label: 'Volver' }, { label: 'Aprobar y programar aviso', cls: 'btn-primary', onClick: () => { setState('Planificado', `Ruta R-01, parada ${O.route.pos + 1}, ETA ${eta(O.route.pos)}`); L.toast('Ruta aprobada', 'Aviso SMS programado para la salida del camión.', 'success'); next(); } }]
        });
      }

      /* Paso 4 · Picking FEFO */
      function picking(b) {
        const order = { Seco: 0, Refrigerado: 1, Congelado: 2 };
        const lines = [...O.lines].map((l, i) => ({ ...l, i, ubic: `${['A', 'B', 'R', 'C'][order[l.temp] + (l.temp === 'Seco' ? i % 2 : 1)]}-${String(10 + i * 7).padStart(2, '0')}-${(i % 4) + 1}`, lote: `L26${11 - (i % 2)}-${40 + i * 3}`, vence: fmt.date(new Date(2026, 11 + (i % 3), 4 + i * 5)) })).sort((a, z) => order[a.temp] - order[z.temp]);
        if (O.estado === 'Planificado') setState('En picking', 'Misión M-3302 iniciada (FEFO)');
        side();
        const done = lines.filter((l) => O.picked[l.i]).length;
        b.innerHTML = `
          <p class="muted">Recorrido por zonas: seco → refrigerado → congelado (RNG-13). Cada línea exige escanear el código GS1 del lote instruido (RF-05.02).</p>
          <div class="row-between" style="margin-bottom:var(--sp-3)"><div class="grow" style="max-width:420px"><div class="progress"><span style="width:${(done / lines.length) * 100}%"></span></div></div><span class="small num">${done} de ${lines.length} líneas</span></div>
          <p class="small muted">${icon('info', 'icon-sm')} Interfaz para guantes: botones de al menos 15 × 15 mm, sin deslizar, pellizcar ni doble toque (RNF-05.02).</p><div class="table-wrap glove" style="border:1px solid var(--c-line-soft)"><table class="table"><caption class="sr-only">Líneas de la misión de preparación</caption><thead><tr><th>Zona</th><th>Ubicación</th><th>Producto</th><th>Lote FEFO</th><th class="right">Cant.</th><th>Lectura</th></tr></thead><tbody>
          ${lines.map((l) => `<tr class="${O.picked[l.i] ? 'is-selected' : ''}"><td>${L.badge(l.temp, l.temp === 'Seco' ? '' : 'info')}</td><td class="mono">${l.ubic}</td><td class="wrap">${esc(l.nombre)}</td><td><span class="mono">${l.lote}</span><div class="small muted">vence ${l.vence}</div></td><td class="num right">${O.short?.i === l.i ? `<s>${l.cant}</s> ${l.cant - O.short.q}` : l.cant}</td>
            <td>${O.picked[l.i] ? L.badge(O.short?.i === l.i ? 'Con faltante' : 'Confirmada', O.short?.i === l.i ? 'warning' : 'success') : `<div class="row" style="flex-wrap:nowrap;gap:4px"><button type="button" class="btn btn-primary btn-sm" data-scan="${l.i}">${icon('scan', 'icon-sm')}Escanear</button><div class="menu-wrap"><button type="button" class="btn btn-tertiary btn-icon btn-sm" data-pm="${l.i}" aria-label="Más acciones de la línea">${icon('more', 'icon-sm')}</button></div></div>`}</td></tr>`).join('')}</tbody></table></div>
          <div id="pk-msg" style="margin-top:var(--sp-3)" aria-live="assertive"></div>
          <div class="row-between" style="margin-top:var(--sp-4)"><button type="button" class="btn btn-secondary" id="pk-bad">${icon('alert')}Simular lectura incorrecta</button><button type="button" class="btn btn-primary big-btn" id="pk-close" ${done === lines.length ? '' : 'disabled'}>${icon('check')}Cerrar misión</button></div>`;
        const scan = (i, ok = true) => {
          const msg = $('#pk-msg', b);
          if (!ok) { msg.innerHTML = L.alert('danger', 'El código leído no corresponde al lote instruido', 'Se leyó el lote L2610-12 (vence antes en otra posición bloqueada). La confirmación quedó bloqueada; escanee el lote indicado (RF-05.02).'); if (navigator.vibrate) navigator.vibrate(200); return; }
          O.picked[i] = true;
          msg.innerHTML = '';
          L.toast('Línea confirmada', O.lines[i].nombre, 'success', { duration: 1600 });
          picking(b);
          $('[data-scan]', b)?.focus();
        };
        $$('[data-scan]', b).forEach((x) => (x.onclick = () => L.busy(x, () => scan(+x.dataset.scan), 450)));
        $('#pk-bad', b).onclick = () => scan(0, false);
        $$('[data-pm]', b).forEach((x) => L.menu(x, [{ label: 'Reportar faltante', icon: 'alert', onClick: () => shortage(+x.dataset.pm) }, { label: 'Ver ubicación alternativa', icon: 'pin', onClick: () => L.toast('Ubicación alternativa', 'B-22-3 con lote siguiente en FEFO.', 'info') }]));
        const shortage = (i) => L.modal({
          title: 'Reportar faltante', icon: 'warning:alert',
          body: `<p>${esc(O.lines[i].nombre)} · solicitado ${O.lines[i].cant} u</p><div class="form-grid"><div class="field"><label for="sh-q">Unidades faltantes <span class="req" aria-hidden="true">*</span></label><input id="sh-q" class="input num" type="number" min="1" max="${O.lines[i].cant}" value="2"></div><div class="field"><label for="sh-m">Motivo <span class="req" aria-hidden="true">*</span></label><select id="sh-m" class="select"><option value="">Seleccione…</option><option>Sin stock</option><option>Dañado</option><option>Vencido</option><option>Error de ubicación</option><option>Otro</option></select></div></div><p class="hint">El motivo es obligatorio y alimenta el indicador de fill rate (RF-05.03).</p>`,
          onOpen: (dlg) => { L.bindField($('#sh-m', dlg), ['required']); L.bindField($('#sh-q', dlg), [(v) => (v >= 1 && v <= O.lines[i].cant ? '' : `Entre 1 y ${O.lines[i].cant}.`)]); },
          actions: [{ label: 'Cancelar' }, { label: 'Registrar faltante', cls: 'btn-primary', onClick: (api) => { if (!L.validateAll(api.el)) return false; O.short = { i, q: +$('#sh-q', api.el).value, m: $('#sh-m', api.el).value }; O.picked[i] = true; picking(b); L.toast('Faltante registrado', `${O.short.q} u · ${O.short.m}. Comercial fue notificado.`, 'warning'); } }]
        });
        $('#pk-close', b).onclick = (e) => L.busy(e.currentTarget, () => { O.log.unshift({ at: new Date(), estado: 'En picking', note: 'Misión cerrada; detalle enviado al ERP (RF-05.06)' }); L.toast('Misión cerrada', 'Detalle por línea, lote y faltantes enviado al ERP.', 'success'); next(); }, 800);
      }

      /* Paso 5 · Carga y guía electrónica */
      function carga(b) {
        const bultos = [['Bulto 1 · seco', 'SSCC 0078012345000001231'], ['Bulto 2 · seco', 'SSCC 0078012345000001248'], ['Bulto 3 · refrigerado', 'SSCC 0078012345000001255'], ['Bulto 4 · congelado', 'SSCC 0078012345000001262']];
        b.innerHTML = `
          <p class="muted">Carga en secuencia inversa a la ruta: el pedido de la parada ${O.route.pos + 1} va ${O.route.pos < 3 ? 'al fondo' : 'cerca de la puerta'} del camión (RF-05.07).</p>
          <div class="grid grid-2">
            <div><h3>Bultos a cargar</h3><ul class="list">${bultos.map(([t, s], i) => `<li><label class="check grow" style="min-height:var(--target)"><input type="checkbox" data-b="${i}" ${O.loaded ? 'checked disabled' : ''}> <span><strong>${t}</strong><span class="small muted mono" style="display:block">${s}</span></span></label></li>`).join('')}</ul></div>
            <div class="stack"><h3>Exposición fuera de frío</h3><p class="small muted" style="margin:0">Desde la salida de cámara hasta el camión (RF-09.11 · RNG-17). Máximo de la familia: 25 min.</p>
              <div class="row"><div class="ring" id="cg-ring" style="--p:24" data-label="6 min"></div><div><strong id="cg-t">6 de 25 min</strong><div class="small muted">Bultos 3 y 4</div></div></div>
              ${L.alert('info', 'Guía electrónica', 'Al cerrar la carga se solicita la guía de despacho al ERP. Solo sale la carga amparada por una guía vigente.')}</div>
          </div>
          <div id="cg-out" style="margin-top:var(--sp-4)"></div>
          <div class="row" style="justify-content:flex-end;margin-top:var(--sp-4)">${O.guia ? `<button type="button" class="btn btn-primary big-btn" id="cg-go">${icon('truck')}Despachar camión</button>` : `<button type="button" class="btn btn-primary big-btn" id="cg-close" disabled>${icon('file')}Cerrar carga y solicitar guía</button>`}</div>`;
        let mins = 6;
        const t = L.interval(() => { if (O.guia || mins >= 14) return; mins++; $('#cg-ring', b)?.style.setProperty('--p', Math.round((mins / 25) * 100)); $('#cg-ring', b)?.setAttribute('data-label', `${mins} min`); if ($('#cg-t', b)) $('#cg-t', b).textContent = `${mins} de 25 min`; }, 2500);
        const boxes = $$('[data-b]', b);
        boxes.forEach((x) => (x.onchange = () => { const all = boxes.every((y) => y.checked); if ($('#cg-close', b)) $('#cg-close', b).disabled = !all; }));
        if ($('#cg-close', b)) $('#cg-close', b).onclick = (e) => {
          const btn = e.currentTarget;
          $('#cg-out', b).innerHTML = `<div class="card" style="box-shadow:none"><div class="row"><span class="spinner"></span><strong>Solicitando guía electrónica al ERP…</strong></div><div class="progress indeterminate" style="margin-top:12px"><span></span></div></div>`;
          L.busy(btn, () => { clearInterval(t); O.loaded = true; O.guia = 'GDE 884133'; setState('Cargado', 'Guía electrónica 884133 emitida'); $('#cg-out', b).innerHTML = L.alert('success', 'Guía de despacho electrónica 884133 emitida', 'Folio vinculado a los 4 SSCC del pedido. La carga quedó cerrada.'); carga(b); }, 1800);
        };
        if ($('#cg-go', b)) $('#cg-go', b).onclick = () => { setState('En ruta', 'Camión KXTR-21 salió del CD Talca 07:15'); L.toast('Camión despachado', 'El cliente recibió el SMS con su ventana de 30 minutos.', 'success'); next(); };
      }

      /* Paso 6 · Entrega con prueba digital (reutiliza el componente de terreno) */
      function entrega(b) {
        if (O.delivered) { b.innerHTML = `${L.alert('success', O.estado === 'Parcial' ? 'Entrega parcial registrada' : 'Entrega registrada', 'La prueba de entrega se asoció a la guía electrónica y se enviará al ERP (RF-06.14).')}<div class="row" style="justify-content:flex-end;margin-top:var(--sp-4)"><button type="button" class="btn btn-primary big-btn" id="en-next">Continuar a rendición${icon('arrow-right')}</button></div>`; $('#en-next', b).onclick = next; return; }
        const stop = { cliente: O.cli.id, nombre: O.cli.nombre, dir: 'Av. Prat 512, Cauquenes', ventana: O.reprog || O.cli.ventana, contado: true, monto: total(O) - (O.short ? O.short.q * O.lines[O.short.i].precio : 0) };
        const lines = O.lines.map((l, i) => ({ nombre: l.nombre, cant: O.short?.i === i ? l.cant - O.short.q : l.cant, precio: l.precio }));
        b.innerHTML = `${O.reprog ? L.alert('info', 'Segundo intento en la nueva ventana', `Entrega reprogramada a ${esc(O.reprog)} (RNG-05).`) : ''}<div id="en-host" style="margin-top:var(--sp-3)"></div>`;
        L.delivery($('#en-host', b), {
          stop, lines, allowClosed: !O.closedAttempt,
          onDone: (r) => { O.delivered = r; setState(r.partial ? 'Parcial' : 'Entregado', r.partial ? `Rechazo parcial: ${r.rejectReason}` : `Firma digital y foto · cobro ${fmt.clp(r.cash)}`); if (r.partial) O.log[0].note += ' · entregado con rechazo parcial'; entrega(b); side(); },
          onClosed: (r) => { O.closedAttempt = true; setState('Fallido', `Local cerrado ${nowTime()} · ${r.cause}`); O.reprog = 'Lun 16-11, 09:00–09:30'; setState('Reprogramado', 'Próxima ventana compatible con ruta y conservación'); side(); entregaReprog(b); }
        });
      }
      function entregaReprog(b) {
        b.innerHTML = `${L.alert('warning', 'Entrega fallida: local cerrado', 'El intento quedó registrado con hora, causa y foto. El sistema reprogramó la entrega a la próxima ventana compatible con la ruta y la conservación del producto (RNG-05). La mercadería refrigerada vuelve al CD con trazabilidad.')}
          <div class="grid grid-2" style="margin-top:var(--sp-4)"><div class="card" style="box-shadow:none"><div class="small muted">Nueva ventana</div><div style="font-size:var(--fs-xl);font-weight:700">${esc(O.reprog)}</div><div class="small muted">Ruta R-01 · parada 1</div></div><div class="card" style="box-shadow:none"><div class="small muted">Aviso al cliente</div><div style="font-weight:600">SMS enviado ${nowTime()}</div><div class="small muted">«Intentamos entregar su pedido y el local estaba cerrado…»</div></div></div>
          <div class="row" style="justify-content:flex-end;margin-top:var(--sp-5)"><button type="button" class="btn btn-primary big-btn" id="en-retry">${icon('truck')}Simular segundo intento</button></div>`;
        $('#en-retry', b).onclick = () => { setState('En ruta', 'Segundo intento en nueva ventana'); entrega(b); };
      }

      /* Paso 7 · Rendición */
      function rendicion(b) {
        if (O.rendido) {
          b.innerHTML = `${L.empty('done', 'Pedido cerrado de punta a punta', `El pedido ${O.id} pasó por ${O.log.length} eventos auditados, desde la captura sin conexión hasta la rendición.`, `<div class="btn-group"><a class="btn btn-primary" href="#/pedidos">Ver todos los pedidos</a><button type="button" class="btn btn-secondary" id="rd-again">${icon('sync')}Repetir con la excepción</button></div>`)}`;
          $('#rd-again', b).onclick = () => { O = newOrder(); O.simCredit = true; draw(); L.toast('Simulación reiniciada', 'Pruebe «crédito excedido» y luego «local cerrado».', 'info'); };
          return;
        }
        const expected = O.delivered?.cash ?? total(O);
        b.innerHTML = `<p class="muted">Al volver al CD, el sistema calcula lo esperado por camión y turno a partir de las entregas al contado confirmadas (RF-07.01) y lo contrasta con lo declarado (RF-07.02).</p>
          <form id="rd-f" novalidate><div class="grid grid-3">
            <div class="card" style="box-shadow:none"><div class="small muted">Esperado para este pedido</div><div class="num" style="font-size:var(--fs-xl);font-weight:700">${fmt.clp(expected)}</div></div>
            <div class="field"><label for="rd-dec">Efectivo declarado <span class="req" aria-hidden="true">*</span></label><div class="input-group"><span class="addon">$</span><input id="rd-dec" class="input num" inputmode="numeric" value="${expected - 2000}"></div><span class="hint">Pruebe con el monto exacto o con una diferencia.</span></div>
            <div class="card" style="box-shadow:none"><div class="small muted">Diferencia</div><div class="num" id="rd-diff" style="font-size:var(--fs-xl);font-weight:700"></div></div>
          </div>
          <div id="rd-cause" style="margin-top:var(--sp-4)"></div>
          <div class="row" style="justify-content:flex-end;margin-top:var(--sp-4)"><button type="submit" class="btn btn-primary big-btn">${icon('check')}Cerrar rendición</button></div></form>`;
        const dec = $('#rd-dec', b);
        const upd = () => {
          const v = parseInt(dec.value.replace(/\D/g, ''), 10) || 0;
          const d = v - expected;
          $('#rd-diff', b).textContent = (d > 0 ? '+' : d < 0 ? '−' : '') + fmt.clp(Math.abs(d));
          $('#rd-diff', b).style.color = d ? 'var(--c-danger)' : 'var(--c-success)';
          $('#rd-cause', b).innerHTML = d ? `<div class="form-grid"><div class="field"><label for="rd-cat">Causal tipificada <span class="req" aria-hidden="true">*</span></label><select id="rd-cat" class="select" required><option value="">Seleccione…</option><option>Vuelto mal entregado</option><option>Billete rechazado</option><option>Abono parcial no registrado</option><option>Error de digitación</option></select><span class="hint">Toda diferencia exige causal, firma y responsable (RF-07.03).</span></div><div class="field"><label for="rd-resp">Responsable</label><select id="rd-resp" class="select"><option>Conductor</option><option>Peoneta</option><option>Tesorería</option></select></div></div>` : L.alert('success', 'Sin diferencias', 'Lo declarado coincide con lo esperado.');
          if (d) L.bindField($('#rd-cat', b), ['required']);
        };
        dec.addEventListener('input', upd);
        upd();
        $('#rd-f', b).onsubmit = (e) => { e.preventDefault(); if (!L.validateAll(e.target)) { L.toast('Falta tipificar la diferencia', '', 'error'); return; } L.busy($('#rd-f [type=submit]', b), () => { O.rendido = true; setState('Rendido', $('#rd-cat', b) ? `Descuadre tipificado: ${$('#rd-cat', b).value}` : 'Sin diferencias'); L.toast('Rendición cerrada', 'Comprobante transferido al ERP (RF-07.09).', 'success'); draw(); }, 900); };
      }

      root.addEventListener('click', (e) => { const g = e.target.closest('[data-go]'); if (g) { O.step = +g.dataset.go; draw(); } });
      $('#fl-reset', root).onclick = async () => { if (await L.confirm({ title: '¿Reiniciar la simulación?', message: 'Se descartará el avance del pedido PV-264822.', confirmLabel: 'Reiniciar' })) { O = newOrder(); L.store.set(draftKey, O); draw(); L.toast('Simulación reiniciada', '', 'info'); } };
      if (q.paso) { O.step = Math.min(6, +q.paso - 1); O.maxStep = Math.max(O.maxStep, O.step); }
      draw();
    }
  });

  /* ---------- Componente de entrega reutilizable (flujo y app de terreno) ---------- */
  L.delivery = (host, { stop, lines, onDone, onClosed, allowClosed = true, compact = false }) => {
    const st = { qty: lines.map((l) => l.cant), reason: '', signed: false, photo: false, crates: 0, method: 'sign', receiver: '', partialPay: false };
    const cli = stop.cliente ? L.findClient(stop.cliente) : null;
    st.pay = 'cash'; st.pos = null;
    const crateBase = cli ? cli.envases.canastillos : 24;
    host.innerHTML = `
      <div class="row-between" style="margin-bottom:var(--sp-3)"><div><strong style="font-size:var(--fs-lg)">${esc(stop.nombre)}</strong><div class="small muted">${icon('pin', 'icon-sm')} ${esc(stop.dir)} · ventana ${esc(stop.ventana)}</div></div>${allowClosed ? `<button type="button" class="btn btn-secondary" data-closed>${icon('door')}Local cerrado</button>` : ''}</div>
      <h3>1. Confirme lo entregado</h3>
      <ul class="list">${lines.map((l, i) => `<li><div class="grow"><div class="title">${esc(l.nombre)}</div><div class="sub">Pedido: ${l.cant} u</div></div><label class="sr-only" for="dq-${i}">Entregado de ${esc(l.nombre)}</label><input id="dq-${i}" class="input num" data-dq="${i}" type="number" min="0" max="${l.cant}" value="${l.cant}" style="width:${compact ? 72 : 88}px;text-align:center"></li>`).join('')}</ul>
      <div id="dl-rej"></div>
      <h3 style="margin-top:var(--sp-4)">2. Envases retornados (RF-06.09)</h3>
      <div class="row"><span>Canastillos devueltos</span><button type="button" class="btn btn-secondary btn-icon btn-sm" data-cr="-1" aria-label="Restar canastillo">${icon('minus', 'icon-sm')}</button><output id="dl-cr" class="num" style="min-width:24px;text-align:center;font-weight:700">0</output><button type="button" class="btn btn-secondary btn-icon btn-sm" data-cr="1" aria-label="Sumar canastillo">${icon('plus', 'icon-sm')}</button></div>
      <p class="small muted" id="dl-crs" style="margin:6px 0 0" aria-live="polite"></p>
      <h3 style="margin-top:var(--sp-4)">3. Prueba de entrega</h3>
      <div class="segmented" role="tablist" aria-label="Método de confirmación" style="margin-bottom:var(--sp-3)"><button type="button" role="tab" aria-selected="true" data-pm="sign">Firma en pantalla</button><button type="button" role="tab" aria-selected="false" data-pm="qr">Código QR del cliente</button><button type="button" role="tab" aria-selected="false" data-pm="name">Foto y nombre</button></div>
      <div data-pmp="sign"><canvas class="sign-pad" id="dl-sign" aria-label="Área de firma. Firme con el dedo o presione Enter para una firma simulada."></canvas><div class="row-between" style="margin-top:6px"><span class="small muted" id="dl-sign-st">Sin firma</span><div class="btn-group"><button type="button" class="btn btn-tertiary btn-sm" data-sign-fake>Firma de ejemplo</button><button type="button" class="btn btn-tertiary btn-sm" data-sign-clear>Borrar</button></div></div></div>
      <div data-pmp="qr" hidden><div class="row"><svg viewBox="0 0 21 21" width="120" height="120" role="img" aria-label="Código QR de confirmación">${Array.from({ length: 21 * 21 }, (_, k) => ((k * 7919) % 13 < 6 || [0, 1, 2, 3, 4, 5, 6].some((z) => (k % 21 === z && k < 147) || (Math.floor(k / 21) === z && k % 21 < 7))) ? `<rect x="${k % 21}" y="${Math.floor(k / 21)}" width="1" height="1" fill="var(--c-ink)"/>` : '').join('')}</svg><p class="small muted">El cliente escanea este código desde su teléfono para confirmar la recepción (RF-06.11).</p></div><button type="button" class="btn btn-secondary btn-sm" data-qr-ok>Simular escaneo del cliente</button></div>
      <div data-pmp="name" hidden><p class="small muted" style="margin-top:0">Para cuando quien recibe no es el titular, no puede firmar o no tiene teléfono: basta la foto de la mercadería y el nombre de quien recibe (RF-06.12, RF-12.12).</p><div class="field"><label for="dl-rcv">Nombre de quien recibe <span class="req" aria-hidden="true">*</span></label><input id="dl-rcv" class="input" autocomplete="off" placeholder="Ej.: Pedro Muñoz, encargado de bodega"></div></div>
      <div style="margin-top:var(--sp-3)"><div class="dropzone" id="dl-photo" style="min-height:96px">${icon('camera', 'icon-lg')}<div><strong>Foto de la mercadería entregada</strong></div><span class="small">Toque para tomar la foto o arrastre una imagen</span></div><button type="button" class="btn btn-tertiary btn-sm" data-photo-fake style="margin-top:6px">Usar foto de ejemplo</button></div>
      ${stop.contado ? `<h3 style="margin-top:var(--sp-4)">4. Cobro al contado (RF-06.05)</h3><div class="segmented" role="group" aria-label="Medio de pago" style="margin-bottom:var(--sp-3)"><button type="button" data-pay="cash" aria-pressed="true">Efectivo</button><button type="button" data-pay="pos" aria-pressed="false">Tarjeta con POS</button></div><div id="dl-pos" hidden></div><div class="form-grid" id="dl-cashbox"><div class="field"><label for="dl-cash">Monto recibido en efectivo <span class="req" aria-hidden="true">*</span></label><div class="input-group"><span class="addon">$</span><input id="dl-cash" class="input num" inputmode="numeric"></div><span class="hint" id="dl-exp"></span></div></div><div id="dl-pp"></div>` : ''}
      <div class="field" style="margin-top:var(--sp-4)"><label for="dl-acuse">Acuse de la guía de despacho (RF-06.14)</label><select id="dl-acuse" class="select"><option>Recibido conforme</option><option>Recibido con observaciones</option><option>Sin acuse</option></select></div>
      <div id="dl-err" aria-live="assertive" style="margin-top:var(--sp-3)"></div>
      <button type="button" class="btn btn-primary btn-block big-btn" data-confirm style="margin-top:var(--sp-4)">${icon('check')}Confirmar entrega</button>`;
    const $h = (s) => host.querySelector(s);
    const expected = () => lines.reduce((a, l, i) => a + st.qty[i] * l.precio, 0);
    const updExp = () => { if ($h('#dl-exp')) $h('#dl-exp').textContent = `Esperado según lo entregado: ${fmt.clp(expected())}`; if ($h('#dl-cash')) $h('#dl-cash').value = expected(); updPay(); };
    const cashIn = () => ($h('#dl-cash') ? parseInt(($h('#dl-cash').value || '').replace(/\D/g, ''), 10) || 0 : 0);
    // Abono o pago parcial al contado: el saldo insoluto pasa a la cuenta corriente (RF-07.10)
    const updPay = () => {
      const box = $h('#dl-pp'); if (!box) return;
      const c = cashIn(), exp = expected();
      st.partialPay = c > 0 && c < exp;
      box.innerHTML = st.partialPay ? `${L.alert('warning', 'Pago parcial', `Se emitirá un comprobante digital de abono por ${fmt.clp(c)} y el saldo de ${fmt.clp(exp - c)} pasará a la cuenta corriente del cliente (RF-07.10).`)}<label class="check" style="margin-top:6px"><input type="checkbox" id="dl-ppok"> El cliente acepta el abono y el saldo pendiente</label>` : '';
    };
    const updCrates = () => { $h('#dl-crs').textContent = `Saldo de envases del cliente: ${crateBase} → ${Math.max(0, crateBase - st.crates)} canastillos. Se actualiza ${L.online() ? 'en línea' : 'en el dispositivo y se sincroniza al reconectar'} junto con la guía (RF-06.10).`; };
    updExp(); updCrates();
    if ($h('#dl-cash')) $h('#dl-cash').oninput = updPay;
    // Cobro con tarjeta: el terminal Bluetooth entrega el código de autorización que se concilia en la liquidación (RF-07.06)
    const drawPos = () => { const box = $h('#dl-pos'); if (!box) return; box.innerHTML = !L.online() ? L.alert('warning', 'POS no disponible sin conexión', 'Cobre en efectivo o registre el crédito autorizado; nunca se presenta una captura sin autorización como pago.') : st.pos ? L.alert('success', `Pago autorizado · código ${st.pos.code}`, `${fmt.clp(st.pos.monto)} con tarjeta terminada en ${st.pos.card}. El voucher se concilia solo en la liquidación del camión.`) : `<button type="button" class="btn btn-secondary" data-posgo>${icon('cash')}Cobrar ${fmt.clp(expected())} con terminal POS</button><p class="hint">Terminal emparejado por Bluetooth (simulado).</p>`; const go = $h('[data-posgo]'); if (go) go.onclick = (e) => L.busy(e.currentTarget, () => { st.pos = { code: String(400000 + Math.floor(Math.random() * 99999)), card: String(1000 + Math.floor(Math.random() * 8999)), monto: expected() }; drawPos(); }, 1200); };
    host.querySelectorAll('[data-pay]').forEach((x) => (x.onclick = () => { st.pay = x.dataset.pay; host.querySelectorAll('[data-pay]').forEach((y) => y.setAttribute('aria-pressed', y === x)); $h('#dl-pos').hidden = st.pay !== 'pos'; $h('#dl-cashbox').hidden = st.pay === 'pos'; $h('#dl-pp').hidden = st.pay === 'pos'; drawPos(); }));
    host.querySelectorAll('[data-dq]').forEach((x) => (x.oninput = () => {
      const i = +x.dataset.dq;
      const v = Math.max(0, Math.min(lines[i].cant, parseInt(x.value, 10) || 0));
      st.qty[i] = v;
      const partial = st.qty.some((q, k) => q < lines[k].cant);
      $h('#dl-rej').innerHTML = partial ? `<div class="field" style="margin-top:var(--sp-3)"><label for="dl-rr">Motivo del rechazo parcial (RF-06.03) <span class="req" aria-hidden="true">*</span></label><select id="dl-rr" class="select"><option value="">Seleccione…</option><option>Producto dañado</option><option>Vencimiento próximo</option><option>No corresponde a lo pedido</option><option>Sospecha de ruptura de cadena de frío</option></select></div>` : '';
      if (partial) { const sel = $h('#dl-rr'); sel.value = st.reason; const coldInfo = () => { const old = $h('#dl-cold'); if (old) old.remove(); if (st.reason === 'Sospecha de ruptura de cadena de frío') sel.closest('.field').insertAdjacentHTML('afterend', `<div id="dl-cold" style="margin-top:var(--sp-2)">${L.alert('danger', 'Rechazo por cadena de frío', 'El rechazo queda asociado al sensor S-KXTR-21 en el tramo 09:00–09:30 (máx. 8,6 °C, consigna 4 °C). El terminal retiene el SSCC afectado aunque no haya red, y Calidad recibe el caso (RF-09.07, RF-09.13).')}</div>`); }; coldInfo(); sel.onchange = () => { st.reason = sel.value; coldInfo(); }; L.bindField(sel, ['required']); }
      updExp();
    }));
    host.querySelectorAll('[data-cr]').forEach((x) => (x.onclick = () => { st.crates = Math.max(0, st.crates + Number(x.dataset.cr)); $h('#dl-cr').textContent = st.crates; updCrates(); }));
    host.querySelectorAll('[data-pm]').forEach((x) => (x.onclick = () => { st.method = x.dataset.pm; host.querySelectorAll('[data-pm]').forEach((y) => y.setAttribute('aria-selected', y === x)); host.querySelectorAll('[data-pmp]').forEach((p) => (p.hidden = p.dataset.pmp !== x.dataset.pm)); }));
    $h('#dl-rcv').oninput = (e) => (st.receiver = e.target.value.trim());
    const pad = L.signaturePad($h('#dl-sign'), (v) => { st.signed = v; $h('#dl-sign-st').textContent = v ? 'Firma capturada' : 'Sin firma'; $h('#dl-sign-st').style.color = v ? 'var(--c-success)' : ''; });
    $h('[data-sign-fake]').onclick = () => pad.fake();
    $h('[data-sign-clear]').onclick = () => pad.clear();
    $h('[data-qr-ok]').onclick = (e) => L.busy(e.currentTarget, () => { st.signed = true; L.toast('Recepción confirmada por QR', 'El cliente validó desde su teléfono.', 'success'); }, 900);
    const dz = L.dropzone($h('#dl-photo'), { accept: 'image/*', multiple: false, maxMB: 8, onChange: (f) => (st.photo = f.length > 0) });
    $h('[data-photo-fake]').onclick = async () => dz.add([await L.fakeFile('entrega.png')]);
    if (allowClosed) $h('[data-closed]').onclick = () => L.modal({
      title: 'Registrar local cerrado', icon: 'warning:door',
      body: `<p class="muted">Se registra el intento con hora y ubicación. El sistema reprograma a la próxima ventana compatible (RF-06.04 · RNG-05).</p>
        <div class="field"><label for="lc-c">Causa <span class="req" aria-hidden="true">*</span></label><select id="lc-c" class="select"><option value="">Seleccione…</option><option>Local cerrado</option><option>Sin persona para recibir</option><option>Dirección no encontrada</option><option>Cliente rechaza recibir</option></select></div>
        <div class="field" style="margin-top:12px"><span class="label" style="font-weight:600;font-size:var(--fs-sm)">Foto de evidencia <span class="req" aria-hidden="true">*</span></span><div class="dropzone" id="lc-ph" style="min-height:90px">${icon('camera')}<span>Foto de la fachada</span></div><button type="button" class="btn btn-tertiary btn-sm" id="lc-fake">Usar foto de ejemplo</button></div>
        <div class="field" style="margin-top:12px"><label for="lc-o">Observación</label><input id="lc-o" class="input" placeholder="Ej.: cortina abajo, vecino indica que abre a las 11:00"></div>
        <div class="small muted" style="margin-top:12px">${icon('clock', 'icon-sm')} ${nowTime()} · GPS −35,9672, −72,3221</div><div id="lc-err" style="margin-top:8px"></div>`,
      onOpen: (dlg) => { L.bindField($('#lc-c', dlg), ['required']); const z = L.dropzone($('#lc-ph', dlg), { accept: 'image/*', multiple: false }); dlg._z = z; $('#lc-fake', dlg).onclick = async () => z.add([await L.fakeFile('fachada.png')]); },
      actions: [{ label: 'Cancelar' }, { label: 'Registrar intento fallido', cls: 'btn-primary', onClick: async (api) => { const ok = L.validateAll(api.el); if (!api.el._z.files.length) { $('#lc-err', api.el).innerHTML = L.alert('danger', 'Falta la foto de evidencia', 'Tome o adjunte una foto antes de registrar.'); return false; } if (!ok) return false; const cause = $('#lc-c', api.el).value; L.toast('Intento registrado', 'Entrega reprogramada a la próxima ventana compatible.', 'warning'); setTimeout(() => onClosed?.({ cause }), 50); } }]
    });
    $h('[data-confirm]').onclick = (e) => {
      const errs = [];
      const partial = st.qty.some((q, k) => q < lines[k].cant);
      if (partial && !st.reason) { errs.push('Indique el motivo del rechazo parcial.'); $h('#dl-rr')?._validate?.(); }
      if (st.method === 'name' ? !st.receiver : !st.signed) errs.push(st.method === 'name' ? 'Ingrese el nombre de quien recibe.' : 'Falta la firma del receptor o la confirmación por QR.');
      if (!st.photo) errs.push('Falta la foto de la entrega.');
      const byPos = stop.contado && st.pay === 'pos';
      const cash = stop.contado && !byPos ? cashIn() : 0;
      if (byPos && !st.pos) errs.push('Falta la autorización del pago con tarjeta.');
      if (stop.contado && !byPos && cash <= 0) errs.push('Ingrese el monto recibido en efectivo.');
      if (!byPos && st.partialPay && !$h('#dl-ppok')?.checked) errs.push('Confirme que el cliente acepta el abono y el saldo pendiente.');
      $h('#dl-err').innerHTML = errs.length ? L.alert('danger', 'No se puede confirmar todavía', `<ul style="margin:4px 0 0;padding-left:18px">${errs.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>`) : '';
      if (errs.length) { $h('#dl-err').scrollIntoView({ block: 'center', behavior: 'smooth' }); return; }
      const acuse = $h('#dl-acuse')?.value || 'Recibido conforme';
      L.busy(e.currentTarget, () => { L.toast(partial ? 'Entrega parcial registrada' : 'Entrega confirmada', `Acuse de la guía: ${acuse}. ` + (L.online() ? 'Sincronizada con la central.' : 'Guardada en el dispositivo; se enviará al reconectar.'), 'success'); if (acuse === 'Sin acuse') L.toast('Guía sin acuse', 'Se alertó a Finanzas y al jefe de ruta: la guía queda pendiente de acuse.', 'warning'); if (byPos) L.store.set('pos.vouchers', [...L.store.get('pos.vouchers', []), { ...st.pos, cliente: stop.nombre }]);
        if (!byPos && st.partialPay) { L.store.set('cc.movs', [...L.store.get('cc.movs', []), { cliente: stop.cliente || '', nombre: stop.nombre, abono: cash, saldo: expected() - cash, fecha: new Date().toISOString() }]); L.toast('Comprobante de abono emitido', `Saldo ${fmt.clp(expected() - cash)} traspasado a la cuenta corriente del cliente en el ERP.`, 'info'); }
        onDone?.({ partial, rejectReason: st.reason, cash: byPos ? st.pos.monto : cash, pos: byPos ? st.pos : null, crates: st.crates, partialPay: !byPos && st.partialPay, receiver: st.method === 'name' ? st.receiver : '' }); }, 900);
    };
  };
})(window.LFX);
