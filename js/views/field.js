/* Perfil de terreno: app de reparto y app de preventa (Kotlin en TC58e), versión móvil
   con comportamiento sin conexión simulado. */
(function (L) {
  const { esc, icon, $, $$, data: D, fmt } = L;

  const stops = () => L.store.get('field.stops', null) || D.paradas.map((p) => ({ id: p.id, estado: p.estado }));
  const setStop = (id, estado) => { const s = stops(); s.find((x) => x.id === id).estado = estado; L.store.set('field.stops', s); };
  const queue = () => L.store.get('field.queue', []);
  const setQueue = (q) => L.store.set('field.queue', q);
  L.fieldDone = () => stops().filter((s) => s.estado !== 'Pendiente').length;
  // Recibos provisionales del preventista: se consolidan en el efectivo que debe rendir al volver (RF-07.11)
  L.preventaRecibos = () => L.store.get('preventa.recibos', null) || [{ id: 'RP-5114', cliente: 'Minimarket El Roble', monto: 84200, hora: '10:12', rendido: false }, { id: 'RP-5117', cliente: 'Almacén San Expedito', monto: 51900, hora: '11:40', rendido: false }];

  // Field app shown as a real app panel: tabs on top on wide screens, fixed at the bottom on phones
  const deviceShell = (title, body, { back, tabs, active, fab } = {}) => `
    <section class="card field-app" id="dev" aria-label="${esc(title)}">
      <div class="app-bar">${back ? `<button type="button" class="btn btn-tertiary btn-icon" data-dback="${back}" aria-label="Volver">${icon('arrow-left')}</button>` : `<img src="assets/logo.svg" alt="" width="26" height="28">`}<h2>${esc(title)}</h2><label class="switch field-net" title="Simular la señal del equipo"><input type="checkbox" id="dev-net" ${L.online() ? 'checked' : ''}> <span class="small">Señal</span></label></div>
      <div class="net-banner ${L.online() ? 'online' : 'offline'}" role="status">${icon(L.online() ? 'wifi' : 'wifi-off', 'icon-sm')}<span class="grow">${L.online() ? 'En línea · todo sincronizado' : `Sin conexión · ${queue().length} evento(s) en cola`}</span>${!L.online() ? '<span class="small">Turno de 14 h</span>' : ''}</div>
      ${tabs ? `<nav class="app-tabbar" aria-label="Secciones de la app">${tabs.map(([id, ic, lb]) => `<button type="button" data-dtab="${id}" ${active === id ? 'aria-current="page"' : ''}>${icon(ic)}<span>${lb}</span>${id === 'cola' && queue().length ? `<span class="badge badge-warning plain tab-count">${queue().length}</span>` : ''}</button>`).join('')}</nav>` : ''}
      <div class="app-body">${body}</div>
      ${fab || ''}
    </section>`;

  // Sincronización automática al reconectar (RF-06.07, RNG-12)
  const syncQueue = async (onDone) => {
    const q = queue();
    if (!q.length) return onDone?.();
    L.toast('Señal recuperada', `Sincronizando ${q.length} evento(s)…`, 'info', { duration: 2000 });
    await L.sleep(1400);
    setQueue([]);
    L.toast('Sincronización completa', `${q.length} evento(s) enviados sin duplicados ni pérdidas.`, 'success');
    L.cierreTurno();
    onDone?.();
  };

  // RF-06.07: when the device syncs, the central system rebuilds the whole shift and issues the closing report for settlement
  L.cierreTurno = () => {
    if (!/^#\/terreno(\?|$)/.test(location.hash)) return;
    const t = L.store.get('field.times', {}), st = stops();
    const hechas = st.filter((s) => s.estado === 'Entregado').length, rep = st.filter((s) => s.estado === 'Reprogramada').length;
    const cobro = Object.values(t).reduce((a, x) => a + (x.cash || 0), 0), cr = Object.values(t).reduce((a, x) => a + (x.crates || 0), 0), pl = Object.values(t).reduce((a, x) => a + (x.pallets || 0), 0);
    L.modal({ title: 'Reporte de cierre del turno · R-01', body: `<p class="muted" style="margin-top:0">Generado automáticamente al sincronizar: el sistema recuperó todos los despachos registrados en el turno y los consolidó para la rendición.</p><dl class="desc-list"><dt>Entregas confirmadas</dt><dd>${hechas} de ${st.length}</dd><dt>Reprogramadas</dt><dd>${rep}</dd><dt>Cobrado en ruta</dt><dd class="num">${fmt.clp(cobro)}</dd><dt>Envases retornados</dt><dd>${cr} canastillos · ${pl} pallets</dd><dt>Horas por entrega</dt><dd>${Object.entries(t).map(([k, x]) => `${esc(D.paradas.find((p) => p.id === k)?.nombre || k)}: ${x.llegada}–${x.termino}`).join(' · ') || '—'}</dd></dl>`, actions: [{ label: 'Cerrar' }, { label: 'Ir a la rendición', cls: 'btn-primary', onClick: () => L.go('/rendicion') }] });
  };

  /* ---------- App de reparto ---------- */
  L.route('/terreno', {
    title: 'Reparto en terreno', parent: '/inicio', block: 'Perfil de terreno', module: 'M6 Reparto · M7 · M8', rf: ['RF-06.01', 'RF-06.02', 'RF-06.04', 'RF-06.05', 'RF-06.07', 'RF-06.09', 'RF-06.11', 'RF-07.06', 'RF-09.06', 'RF-06.13', 'RF-09.12', 'RNG-12', 'RF-06.10', 'RF-06.12', 'RF-07.10', 'RF-09.07', 'RF-09.13', 'RNF-06.01', 'RNF-09.06', 'RNF-13.02'], actors: ['Conductor propio', 'Conductor externo'],
    render: () => `<div class="page-head hide-sm"><div class="titles"><span class="page-kicker">${icon('truck', 'icon-sm')}App de reparto</span><h1>Ruta R-01 Cauquenes</h1><p class="muted" style="margin:0">${D.paradas.length} entregas · camión KXTR-21 con equipo de frío · salida ${D.rutas[0].salida}</p></div><div class="actions"><button type="button" class="btn btn-secondary" id="tr-reset">${icon('sync')}Reiniciar ruta</button></div></div>
      <div class="split"><div id="tr-host"></div><aside class="card hide-sm stack"><h2>Qué funciona sin conexión</h2>
        <ul class="list">${[['Entrega y prueba de entrega', 'Captura 14 h · cola cifrada', 'success'], ['Cobro en efectivo', 'Comprobante local', 'success'], ['Devoluciones y envases', 'Se registran en el dispositivo', 'success'], ['Mapas', 'Precargados con la ruta', 'success'], ['Autorización POS', 'No disponible: efectivo o crédito autorizado', 'danger'], ['Recalcular ruta', 'No disponible: secuencia precargada', 'danger']].map(([t, d, k]) => `<li><span class="badge badge-${k} plain" style="padding:4px">${icon(k === 'success' ? 'check' : 'ban', 'icon-sm')}</span><div class="grow"><div class="title">${t}</div><div class="sub">${d}</div></div></li>`).join('')}</ul></aside></div>`,
    mount: (root) => {
      const S = { screen: 'ruta', stop: null };
      const coldState = () => L.store.get('field.coldState', 'ok');
      const host = $('#tr-host', root);
      const tabs = [['ruta', 'route', 'Ruta'], ['cola', 'sync', 'Cola'], ['frio', 'thermo', 'Frío'], ['mas', 'menu', 'Más']];
      const draw = () => {
        const st = stops();
        let title = 'Mi ruta', body = '', back = '';
        if (S.screen === 'ruta') {
          const done = st.filter((s) => s.estado !== 'Pendiente').length;
          body = `<div class="card" style="padding:var(--sp-4)"><div class="row"><div class="ring" style="--p:${Math.round((done / st.length) * 100)}" data-label="${done}/${st.length}"></div><div><strong>R-01 Cauquenes</strong><div class="small muted">KXTR-21 · con equipo de frío</div><div class="small muted">Credencial válida hasta 21:15</div>${(() => { const t = L.store.get('field.times', {}); const cash = Object.values(t).reduce((a, x) => a + (x.cash || 0), 0) + 412000; const max = L.param('efectivo-max') || 800000; return `<div class="small" style="margin-top:4px">Efectivo a bordo: <strong class="num" style="${cash > max ? 'color:var(--c-danger)' : ''}">${fmt.clp(cash)}</strong> <span class="muted">de ${fmt.clp(max)} permitidos</span></div>`; })()}</div></div></div>
            <ol class="list" aria-label="Entregas de la ruta">${D.paradas.map((p, i) => { const e = st[i].estado; return `<li><button type="button" class="btn btn-tertiary" data-stop="${p.id}" style="width:100%;justify-content:flex-start;text-align:left;min-height:64px;padding:0 4px;font-weight:400"><span class="avatar ${e === 'Pendiente' ? 'dark' : ''}" style="width:36px;height:36px">${e === 'Pendiente' ? i + 1 : icon(e === 'Entregado' ? 'check' : 'alert', 'icon-sm')}</span><span class="grow" style="min-width:0"><strong style="display:block;white-space:normal">${esc(p.nombre)}</strong><span class="small muted">${esc(p.ventana)} · ${p.bultos} bultos${p.frio ? ' · frío' : ''}</span></span>${e !== 'Pendiente' ? L.badge(e, e === 'Entregado' ? 'success' : 'warning') : icon('chev-right')}</button></li>`; }).join('')}</ol>`;
        } else if (S.screen === 'parada') {
          const p = D.paradas.find((x) => x.id === S.stop);
          const e = st.find((x) => x.id === p.id).estado;
          title = p.nombre; back = 'ruta';
          body = `<dl class="desc-list"><dt>Dirección</dt><dd>${esc(p.dir)}</dd><dt>Ventana</dt><dd>${esc(p.ventana)}</dd><dt>Pedido</dt><dd class="mono">${esc(p.pedido)}</dd><dt>Bultos</dt><dd>${p.bultos}${p.frio ? ' · incluye frío' : ''}</dd><dt>Cobro</dt><dd>${p.contado ? 'Contado ' + fmt.clp(p.monto) : 'Crédito 30 días'}</dd></dl>
            ${p.frio ? (['ok', 'satelite'].includes(coldState()) ? L.alert('success', 'Cadena de frío vigente', 'Señal del equipo de frío del camión hace 4 s · 3,4 °C, carga vigente y sin retención. Se habilita la bajada del SSCC.') : L.alert('danger', coldState() === 'enlace' ? 'Bajada bloqueada: sin latido del camión' : 'Bajada bloqueada: SSCC retenido por excursión', coldState() === 'enlace' ? 'El terminal no recibe señal del equipo de frío del camión hace más de 30 s. Sin estado confiable no se baja producto de frío; el SSCC queda retenido y vuelve al CD si Calidad no decide en plazo.' : 'El SSCC 0078012345000001255 quedó retenido por excursión crítica. Solo Calidad puede liberarlo.')) : ''}
            ${e === 'Pendiente' ? `<button type="button" class="btn btn-secondary btn-block big-btn" data-nav>${icon('pin')}Navegar ${L.online() ? '' : '(mapa precargado)'}</button>${p.frio && !['ok', 'satelite'].includes(coldState()) ? `<button type="button" class="btn btn-primary btn-block big-btn" disabled>${icon('lock')}Entrega de frío bloqueada</button><button type="button" class="btn btn-tertiary btn-block" data-dtab="frio">Ver estado de la cadena de frío</button>` : `<button type="button" class="btn btn-primary btn-block big-btn" data-arrive>${icon('check')}Llegué: iniciar entrega</button>`}` : L.alert(e === 'Entregado' ? 'success' : 'warning', `Parada ${e.toLowerCase()}`, e === 'Entregado' ? `Prueba de entrega registrada. Llegada ${L.store.get('field.times', {})[p.id]?.llegada || '—'} · término ${L.store.get('field.times', {})[p.id]?.termino || '—'}.` : 'Reprogramada a la próxima ventana compatible.')}`;
        } else if (S.screen === 'entrega') {
          const p = D.paradas.find((x) => x.id === S.stop);
          title = 'Entrega · ' + p.nombre; back = 'parada';
          body = '<div id="dv-host"></div>';
        } else if (S.screen === 'cola') {
          const q = queue();
          title = 'Cola de sincronización';
          body = q.length ? `<p class="small muted">Eventos guardados en el dispositivo con identificador único. Se envían solos al recuperar señal o al volver al CD.</p><ul class="list">${q.map((x) => `<li>${icon(x.icon)}<div class="grow"><div class="title">${esc(x.t)}</div><div class="sub">Guardado a las ${esc(x.at)} · no se duplica al enviarse</div></div>${L.badge('En cola', 'warning')}</li>`).join('')}</ul>${L.online() ? `<button type="button" class="btn btn-primary btn-block" data-sync>${icon('sync')}Sincronizar ahora</button>` : L.alert('info', 'Sin señal', 'Nada se pierde: la cola persiste aunque se reinicie el equipo.')}` : L.empty('done', 'Todo sincronizado', 'No hay eventos pendientes de envío.');
        } else if (S.screen === 'frio') {
          title = 'Cadena de frío';
          const cs = coldState(), exc = cs === 'excursion', obs = L.store.get('field.coldObs', []);
          const vals = exc ? [3.8, 3.5, 4.4, 5.6, 6.8, 7.4] : [3.8, 3.5, 4.4, 3.9, 3.6, 3.4];
          body = `${cs === 'satelite' ? L.alert('info', 'Sin red móvil: enlace por satélite', 'Los dos operadores móviles no tienen cobertura. El equipo de frío envía la curva cada 3 min y las alarmas de inmediato por satélite, y Calidad puede bajar órdenes firmadas. Al volver la red se concilia con la serie fina; nada se libera por la sola recuperación.') : cs === 'ok' ? '' : L.alert('danger', exc ? 'Alerta en cabina: excursión crítica' : 'Sin señal del equipo de frío del camión', exc ? '7,4 °C, sobre 6 °C (consigna 4 °C + 2 °C) durante 16 min. El terminal retuvo el SSCC 0078012345000001255 sin depender de red móvil ni satélite. Usted no puede liberarlo: registre lo observado y Calidad decide.' : 'Último latido hace 45 s (máximo 30 s). Las bajadas de frío quedan bloqueadas hasta recuperar el enlace local con el camión.')}
            <div class="card" style="padding:var(--sp-4)"><div class="row-between"><strong>Compartimento refrigerado</strong>${L.badge(exc ? 'Excursión crítica' : cs === 'enlace' ? 'Sin enlace' : cs === 'satelite' ? 'Normal · vía satélite' : 'Normal', cs === 'ok' || cs === 'satelite' ? 'success' : 'danger')}</div><div style="font-size:var(--fs-3xl);font-weight:700" class="num">${exc ? '7,4' : '3,4'} °C</div><div class="small muted">Consigna 4 °C · límite 6 °C sostenido 15 min · sensor independiente ${exc ? '7,6' : '3,6'} °C</div></div>
            ${L.charts.line(['07:00', '07:30', '08:00', '08:30', '09:00', '09:30'], [{ name: 'Temperatura', values: vals }], { w: 340, h: 180, label: 'Temperatura del compartimento en la ruta', min: 0, target: 6, targetLabel: 'Límite' })}
            ${exc ? `<form id="co-f" class="stack" novalidate><div class="field"><label for="co-o">Observaciones del conductor <span class="req" aria-hidden="true">*</span></label><textarea id="co-o" class="textarea" placeholder="Ej.: puerta abierta 10 min en la descarga anterior; el equipo de frío marca falla"></textarea></div><button type="submit" class="btn btn-primary btn-block big-btn">${icon('send')}Enviar a Calidad</button></form>${obs.length ? `<ul class="list">${obs.map((x) => `<li>${icon('check')}<div class="grow"><div class="title small">${esc(x.t)}</div><div class="sub">${x.at} · ${x.cola ? 'en cola' : 'recibida por Calidad'}</div></div></li>`).join('')}</ul>` : ''}` : ''}
            <div class="btn-group" style="margin-top:var(--sp-3)">${cs === 'ok' ? '<button type="button" class="btn btn-secondary btn-sm" data-cold="excursion">Simular excursión</button><button type="button" class="btn btn-secondary btn-sm" data-cold="enlace">Simular pérdida de enlace</button><button type="button" class="btn btn-secondary btn-sm" data-cold="satelite">Simular sin red móvil</button>' : '<button type="button" class="btn btn-tertiary btn-sm" data-cold="ok">Restablecer simulación</button>'}</div>
            <p class="small muted">Con la puerta abierta y hasta 10 min después del cierre se suspenden solo las advertencias del aire; la alarma crítica nunca se suspende. Si Calidad no decide dentro del plazo de la familia, el producto sigue retenido y vuelve al CD. Sin móvil ni satélite, las alarmas locales siguen operando y retienen el SSCC afectado.</p>`;
        } else if (S.screen === 'mas') {
          title = 'Más opciones';
          body = `<ul class="list">
            <li><button type="button" class="btn btn-tertiary" style="width:100%;justify-content:flex-start" data-pos ${L.online() ? '' : 'aria-disabled="true"'}>${icon('cash')}<span class="grow" style="text-align:left">Cobro con tarjeta (POS)<span class="small muted" style="display:block">${L.online() ? 'Terminal emparejado por Bluetooth' : 'No disponible sin conexión'}</span></span></button></li>
            <li><a class="btn btn-tertiary" style="width:100%;justify-content:flex-start" href="#/devoluciones/nueva">${icon('undo')}<span class="grow" style="text-align:left">Registrar devolución</span></a></li>
            <li><a class="btn btn-tertiary" style="width:100%;justify-content:flex-start" href="#/rendicion">${icon('file')}<span class="grow" style="text-align:left">Rendir el turno</span></a></li>
            <li><button type="button" class="btn btn-tertiary" style="width:100%;justify-content:flex-start" data-sun aria-pressed="${L.store.pref('contrast', 'normal') === 'high'}">${icon('sun')}<span class="grow" style="text-align:left">Pantalla para pleno sol<span class="small muted" style="display:block">${L.store.pref('contrast', 'normal') === 'high' ? 'Activada: alto contraste' : 'Más contraste para leer a la intemperie'}</span></span></button></li>
            <li><button type="button" class="btn btn-tertiary" style="width:100%;justify-content:flex-start" data-crew>${icon('users')}<span class="grow" style="text-align:left">Tripulación del turno<span class="small muted" style="display:block">Conductor y peoneta, cada uno con su sesión</span></span></button></li>
            <li><button type="button" class="btn btn-tertiary" style="width:100%;justify-content:flex-start" data-print>${icon('printer')}<span class="grow" style="text-align:left">Imprimir comprobante</span></button></li></ul>`;
        }
        host.innerHTML = deviceShell(title, body, { back, tabs, active: ['parada', 'entrega'].includes(S.screen) ? 'ruta' : S.screen });
        if (S.screen === 'entrega') {
          const p = D.paradas.find((x) => x.id === S.stop);
          const ped = L.findOrder(p.pedido);
          L.delivery($('#dv-host', host), {
            stop: { ...p, ventana: p.ventana }, compact: true,
            lines: ped.lineas.slice(0, 4).map((l) => ({ nombre: l.nombre, cant: l.cant, precio: Math.round(p.monto / ped.lineas.slice(0, 4).reduce((a, x) => a + x.cant, 0)) })),
            onDone: (r) => { const max = L.param('efectivo-max') || 800000, before = Object.values(L.store.get('field.times', {})).reduce((a, x) => a + (x.cash || 0), 0) + 412000; if (before + (r.cash || 0) > max && before <= max) L.toast('Supera el efectivo permitido a bordo', `Lleva ${fmt.clp(before + (r.cash || 0))}. Deposítelo en el próximo punto acordado y regístrelo en «Rendir el turno».`, 'warning'); setStop(p.id, 'Entregado'); L.store.set('field.times', { ...L.store.get('field.times', {}), [p.id]: { llegada: r.llegada, termino: r.termino, cash: r.cash || 0, crates: r.crates, pallets: r.pallets } }); if (!L.online()) setQueue([...queue(), { t: `Entrega ${p.nombre}`, icon: 'check', uuid: 'pod-' + Math.random().toString(16).slice(2, 8), at: '09:4' + queue().length }, ...(r.cash ? [{ t: `Cobro ${fmt.clp(r.cash)}`, icon: 'cash', uuid: 'cob-' + Math.random().toString(16).slice(2, 8), at: '09:4' + queue().length }] : [])]); S.screen = 'ruta'; draw(); },
            onClosed: (r) => { setStop(p.id, 'Reprogramada'); if (!L.online()) setQueue([...queue(), { t: `Local cerrado ${p.nombre}`, icon: 'door', uuid: 'evt-' + Math.random().toString(16).slice(2, 8), at: '09:5' + queue().length }]); S.screen = 'ruta'; draw(); }
          });
        }
        $('#dev-net', host).onchange = (e) => { L.setOnline(e.target.checked); if (e.target.checked) syncQueue(draw); else { L.toast('Sin conexión', 'Siga trabajando: todo queda en el dispositivo.', 'warning'); draw(); } };
        $$('[data-dtab]', host).forEach((b) => (b.onclick = () => { S.screen = b.dataset.dtab; draw(); }));
        $('[data-dback]', host) && ($('[data-dback]', host).onclick = () => { S.screen = $('[data-dback]', host).dataset.dback; draw(); });
        $$('[data-stop]', host).forEach((b) => (b.onclick = () => { S.stop = b.dataset.stop; S.screen = 'parada'; draw(); }));
        $('[data-arrive]', host) && ($('[data-arrive]', host).onclick = () => { S.screen = 'entrega'; draw(); });
        $$('[data-cold]', host).forEach((b) => (b.onclick = () => { const v = b.dataset.cold; L.store.set('field.coldState', v); if (v === 'satelite') L.toast('Sin red móvil', 'Curva y alarmas siguen por satélite.', 'info'); else if (v !== 'ok') { if (navigator.vibrate) navigator.vibrate([300, 150, 300]); L.toast(v === 'excursion' ? 'Alarma de frío en cabina' : 'Sin latido del camión', v === 'excursion' ? 'SSCC retenido. Registre sus observaciones.' : 'Bajadas de frío bloqueadas.', 'error'); } else L.store.set('field.coldObs', []); draw(); }));
        $('#co-f', host) && ($('#co-f', host).onsubmit = (ev) => { ev.preventDefault(); const t = $('#co-o', host).value.trim(); if (!t) { L.toast('Escriba lo que observó', 'La observación es obligatoria para Calidad.', 'error'); $('#co-o', host).focus(); return; } const at = new Date().toLocaleTimeString('es-CL', { hour: '2-digit', minute: '2-digit' }); L.store.set('field.coldObs', [{ t, at, cola: !L.online() }, ...L.store.get('field.coldObs', [])]); if (!L.online()) setQueue([...queue(), { t: 'Observación de frío', icon: 'thermo', uuid: 'obs-' + Math.random().toString(16).slice(2, 8), at }]); L.logAudit('Creación', 'Cadena de frío', `Observación del conductor sobre excursión en SSCC 0078012345000001255: ${t}`, 'App móvil'); L.toast('Observación enviada a Calidad', L.online() ? 'Calidad decide liberar, bloquear o rechazar.' : 'Guardada en el dispositivo; se enviará al reconectar.', 'success'); draw(); });
        $('[data-nav]', host) && ($('[data-nav]', host).onclick = () => L.toast(L.online() ? 'Navegación iniciada' : 'Mapa precargado', L.online() ? 'ETA 6 min · 2,1 km' : 'Sin recálculo en línea: siga la secuencia precargada.', 'info'));
        $('[data-sync]', host) && ($('[data-sync]', host).onclick = () => syncQueue(draw));
        $('[data-pos]', host) && ($('[data-pos]', host).onclick = () => (L.online() ? L.toast('Terminal POS listo', 'Acerque la tarjeta del cliente.', 'info') : L.modal({ title: 'Cobro con tarjeta no disponible', icon: 'warning:wifi-off', body: '<p>Sin conexión no se puede autorizar un pago con tarjeta. Cobre en efectivo o registre el crédito autorizado del cliente; nunca se presenta una captura POS como pago autorizado.</p>', actions: [{ label: 'Entendido', cls: 'btn-primary' }] })));
        $('[data-sun]', host) && ($('[data-sun]', host).onclick = () => { const on = L.store.pref('contrast', 'normal') !== 'high'; L.store.setPref('contrast', on ? 'high' : 'normal'); L.applyPrefs(); L.toast(on ? 'Pantalla para pleno sol activada' : 'Contraste normal', on ? 'Se conserva en este equipo; puede cambiarla en Mi perfil.' : '', 'success', { duration: 2000 }); draw(); });
        $('[data-crew]', host) && ($('[data-crew]', host).onclick = () => L.modal({ title: 'Tripulación del turno · R-01', body: `<ul class="list"><li>${icon('user')}<div class="grow"><div class="title">${esc(L.me().name)}</div><div class="sub">Conductor · sesión en este terminal</div></div>${L.badge('Sesión activa', 'success')}</li><li>${icon('user')}<div class="grow"><div class="title">Luis Mora Fuentes</div><div class="sub">Peoneta · sesión propia en su terminal</div></div>${L.badge(L.store.get('field.peoneta', false) ? 'Sesión activa' : 'Sin iniciar', L.store.get('field.peoneta', false) ? 'success' : 'warning')}</li></ul><p class="hint">El peoneta no usa la sesión del conductor ni hay cuentas genéricas por cargo: cada entrega, cobro o devolución queda a nombre de quien la registra (4.1).</p>`, actions: [{ label: 'Cerrar' }, ...(L.store.get('field.peoneta', false) ? [] : [{ label: 'El peoneta inicia su sesión', cls: 'btn-primary', onClick: () => { L.store.set('field.peoneta', true); L.logAudit('Creación', 'Sesión', 'Luis Mora Fuentes (peoneta) inició sesión propia en su terminal para la ruta R-01', 'App móvil'); L.toast('Sesión del peoneta iniciada', 'En su propio terminal, con su credencial.', 'success'); } }])] }));
        $('[data-print]', host) && ($('[data-print]', host).onclick = (e) => L.busy(e.currentTarget, () => L.toast('Comprobante impreso', 'Impresora portátil ZQ220.', 'success'), 900));
        $('#dev', host).scrollTop = 0;
      };
      document.addEventListener('lfx:net', draw);
      L.onLeave(() => document.removeEventListener('lfx:net', draw));
      $('#tr-reset', root) && ($('#tr-reset', root).onclick = () => { L.store.set('field.stops', null); L.store.set('field.times', {}); L.store.set('field.coldState', 'ok'); setQueue([]); S.screen = 'ruta'; draw(); L.toast('Ruta reiniciada', '', 'info'); });
      draw();
    }
  });

  /* ---------- App de preventa ---------- */
  L.route('/terreno/preventa', {
    title: 'Preventa en terreno', parent: '/inicio', block: 'Perfil de terreno', module: 'M3 Preventa', rf: ['RF-03.02', 'RF-03.05', 'RF-03.06', 'RF-03.13', 'RF-03.15', 'RF-07.05', 'RF-08.04', 'RF-07.11', 'RF-03.08', 'RF-03.09'], actors: ['Preventista'],
    render: () => `<div class="page-head hide-sm"><div class="titles"><span class="page-kicker">${icon('cart', 'icon-sm')}App de preventa</span><h1>Zona Curicó</h1><p class="muted" style="margin:0">Visitas del día, ficha comercial y toma de pedido sin señal.</p></div><div class="actions"><a class="btn btn-secondary" href="#/flujo">Ver el pedido en el flujo completo</a></div></div>
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
            ${c.vencida ? L.alert('danger', 'Cliente bloqueado por mora', 'Deuda vencida sobre 30 días: no se aceptan pedidos a crédito. Solo venta al contado o cobro de la deuda.') + `<button type="button" class="btn btn-secondary btn-block" data-collect style="margin-top:var(--sp-2)">${icon('cash')}Cobrar facturas vencidas</button>` : ''}
            ${c.envases.canastillos > 40 ? L.alert('warning', 'Saldo de envases sobre el umbral', `${c.envases.canastillos} canastillos en poder del cliente.`) : ''}
            <h3>Compra habitual</h3><ul class="list">${D.productos.slice(0, 4).map((p, i) => `<li><span class="grow"><span class="title">${esc(p.nombre)}</span><span class="sub" style="display:block">Cada ${[7, 7, 14, 10][i]} días · última: ${[12, 24, 6, 18][i]} u</span></span><button type="button" class="btn btn-secondary btn-sm" data-add="${p.sku}">${icon('plus', 'icon-sm')}Agregar</button></li>`).join('')}</ul>
            <button type="button" class="btn btn-primary btn-block big-btn" data-order>${icon('cart')}Tomar pedido</button><button type="button" class="btn btn-secondary btn-block" data-gondola>${icon('eye')}Registrar lo que vi en la góndola</button>`;
        } else if (S.screen === 'cola') {
          const q = queue();
          title = 'Cola de sincronización'; back = 'visitas';
          body = q.length ? `<p class="small muted">Pedidos y cobros guardados en el dispositivo con identificador único. Se envían solos al recuperar señal, sin duplicarse.</p><ul class="list">${q.map((x) => `<li>${icon(x.icon)}<div class="grow"><div class="title">${esc(x.t)}</div><div class="sub">Guardado a las ${esc(x.at)} · no se duplica al enviarse</div></div>${L.badge('En cola', 'warning')}</li>`).join('')}</ul>${L.online() ? `<button type="button" class="btn btn-primary btn-block" data-sync>${icon('sync')}Sincronizar ahora</button>` : L.alert('info', 'Sin señal', 'Nada se pierde: la cola persiste aunque se reinicie el equipo.')}` : L.empty('done', 'Todo sincronizado', 'No hay pedidos ni cobros pendientes de envío.');
        } else if (S.screen === 'pedido') {
          const c = L.findClient(S.cli);
          title = 'Pedido · ' + c.nombre; back = 'cliente';
          const tot = S.cart.reduce((a, l) => a + l.cant * l.precio, 0);
          // Crédito: mora bloquea el crédito; el pedido más la deuda vencida sobre el límite alerta, y sobre 110 % bloquea (RF-07.05, RF-03.08, RF-03.09)
          const moroso = c.vencida > 0;
          if (moroso) S.pago = 'contado';
          const pago = S.pago || 'credito';
          const uso = c.credito ? Math.round(((c.vencida + tot) / c.credito) * 100) : 0;
          const sobre = pago === 'credito' && uso > 100, bloqueo = pago === 'credito' && uso > 110;
          body = `<div class="field combo"><label for="pv-add">Agregar producto</label><input id="pv-add" class="input" placeholder="Nombre o SKU"></div>
            ${S.cart.length ? `<ul class="list">${S.cart.map((l, i) => `<li><span class="grow"><span class="title">${esc(l.nombre)}</span><span class="sub" style="display:block">${fmt.clp(l.precio)} · stock ${L.online() ? '' : '(06:00) '}${fmt.n(l.stock)}</span></span><button type="button" class="btn btn-secondary btn-icon btn-sm" data-cq="${i}" data-d="-1" aria-label="Restar">${icon('minus', 'icon-sm')}</button><strong class="num" style="min-width:28px;text-align:center">${l.cant}</strong><button type="button" class="btn btn-secondary btn-icon btn-sm" data-cq="${i}" data-d="1" aria-label="Sumar">${icon('plus', 'icon-sm')}</button></li>`).join('')}</ul>` : L.empty('box', 'Pedido vacío', 'Busque un producto o agregue desde la compra habitual.')}
            <div class="row-between"><span class="muted">Entrega: sáb 14-11 · ${esc(c.ventana)}</span><strong class="num">${fmt.clp(tot)}</strong></div>
            <fieldset><legend>Condición de pago</legend><div class="segmented" role="group" aria-label="Condición de pago"><button type="button" data-pago="credito" aria-pressed="${pago === 'credito'}" ${moroso ? 'disabled' : ''}>Crédito 30 días</button><button type="button" data-pago="contado" aria-pressed="${pago === 'contado'}">Contado</button></div>${moroso ? '<p class="hint">Crédito bloqueado por mora.</p>' : ''}</fieldset>
            ${S.cart.length && bloqueo ? L.alert('danger', 'Pedido bloqueado por crédito', `El pedido más la deuda vencida llega al ${uso} % del límite: sobre 110 % no se puede enviar a crédito. Reduzca el pedido o cámbielo a contado.`) : S.cart.length && sobre ? L.alert('warning', 'El pedido supera el límite de crédito', `El pedido más la deuda vencida llega al ${uso} % del límite de crédito. Puede enviarlo: quedará sujeto a revisión.`) : ''}
            <button type="button" class="btn btn-primary btn-block big-btn" data-save ${S.cart.length && !bloqueo ? '' : 'disabled'}>${icon(L.online() ? 'send' : 'download')}${L.online() ? 'Enviar pedido' : 'Guardar sin conexión'}</button>`;
        }
        host.innerHTML = deviceShell(title, body, { back, fab, tabs: [['visitas', 'list', 'Visitas'], ['cola', 'sync', 'Cola'], ['clientes', 'store', 'Clientes'], ['mas', 'menu', 'Más']], active: S.screen === 'cola' ? 'cola' : 'visitas' });
        $('#dev-net', host).onchange = (e) => { L.setOnline(e.target.checked); if (e.target.checked) syncQueue(draw); else { L.toast('Sin conexión', 'Puede seguir tomando pedidos.', 'warning'); draw(); } };
        $('[data-dback]', host) && ($('[data-dback]', host).onclick = () => { S.screen = $('[data-dback]', host).dataset.dback; draw(); });
        $$('[data-dtab]', host).forEach((b) => (b.onclick = () => { if (b.dataset.dtab === 'clientes') L.go('/clientes'); else if (b.dataset.dtab === 'cola') { S.screen = 'cola'; draw(); } else if (b.dataset.dtab === 'mas') { const rs = L.preventaRecibos().filter((r) => !r.rendido); L.modal({ title: 'Efectivo por rendir hoy', body: rs.length ? `<ul class="list">${rs.map((r) => `<li><span class="mono">${r.id}</span><span class="grow">${esc(r.cliente)} · ${r.hora}</span><span class="num">${fmt.clp(r.monto)}</span></li>`).join('')}</ul><p class="row-between"><strong>Total a rendir</strong><strong class="num">${fmt.clp(rs.reduce((a, r) => a + r.monto, 0))}</strong></p><p class="hint">La rendición es obligatoria al volver a base; Finanzas la ve en Cobranza y rendición.</p>` : L.empty('done', 'Nada por rendir', 'No hay recibos provisionales pendientes.'), actions: [{ label: 'Ver mis pedidos', onClick: () => L.go('/pedidos') }, { label: 'Cerrar', cls: 'btn-primary' }] }); } else { S.screen = 'visitas'; draw(); } }));
        $$('[data-cli]', host).forEach((b) => (b.onclick = () => { S.cli = b.dataset.cli; S.cart = []; S.screen = 'cliente'; draw(); }));
        $('#pv-q', host) && ($('#pv-q', host).oninput = (e) => { const v = e.target.value.toLowerCase(); $$('#pv-list li', host).forEach((li) => (li.hidden = !li.textContent.toLowerCase().includes(v))); });
        $('[data-fab]', host) && ($('[data-fab]', host).onclick = () => { S.cli = mine[0].id; S.cart = []; S.screen = 'pedido'; draw(); });
        $$('[data-add]', host).forEach((b) => (b.onclick = () => { const p = D.productos.find((x) => x.sku === b.dataset.add); S.cart.push({ ...p, cant: 12 }); L.toast('Agregado al pedido', p.nombre, 'success', { duration: 1500 }); b.disabled = true; }));
        $('[data-gondola]', host) && ($('[data-gondola]', host).onclick = () => { const c = L.findClient(S.cli); L.modal({ title: `Góndola · ${c.nombre}`, body: `<p class="muted" style="margin-top:0">Lo que ve en el local queda registrado para Comercial y Calidad, aunque no haya pedido.</p><div class="field"><label for="go-t">Qué vio <span class="req" aria-hidden="true">*</span></label><select id="go-t" class="select"><option value="">Seleccione…</option><option>Producto nuestro vencido</option><option>Exhibidor o promoción de la competencia</option><option>El local está por cerrar</option><option>Falta producto nuestro en la góndola</option><option>Otro</option></select></div><div id="go-x"></div><div class="field" style="margin-top:12px"><label for="go-o">Detalle</label><input id="go-o" class="input" placeholder="Ej.: exhibidor de bebidas de la competencia en la entrada"></div>`, onOpen: (d) => { L.bindField($('#go-t', d), ['required']); $('#go-t', d).onchange = (e) => { $('#go-x', d).innerHTML = e.target.value === 'Producto nuestro vencido' ? `<div class="form-grid" style="margin-top:12px"><div class="field"><label for="go-p">Producto <span class="req" aria-hidden="true">*</span></label><select id="go-p" class="select">${D.productos.filter((p) => p.temp !== 'Seco').slice(0, 6).map((p) => `<option value="${p.sku}">${esc(p.nombre)}</option>`).join('')}</select></div><div class="field"><label for="go-q">Unidades <span class="req" aria-hidden="true">*</span></label><input id="go-q" class="input num" type="number" min="1" value="4"></div></div>` : ''; }; }, actions: [{ label: 'Cancelar' }, { label: 'Registrar', cls: 'btn-primary', onClick: (api) => { if (!L.validateAll(api.el)) return false; const t = $('#go-t', api.el).value; if (t === 'Producto nuestro vencido') { const p = D.productos.find((x) => x.sku === $('#go-p', api.el).value), q = +$('#go-q', api.el).value; D.mermas.push({ id: 'MR-' + (7001 + D.mermas.length), fecha: new Date().toISOString(), sku: p.sku, producto: p.nombre, lote: p.lote, cant: q, origen: 'Góndola del cliente', cliente: c.id, monto: q * p.precio }); } L.logAudit('Creación', 'Visita', `Góndola de ${c.nombre}: ${t}${$('#go-o', api.el).value ? ' · ' + $('#go-o', api.el).value : ''}`, 'App móvil'); if (!L.online()) setQueue([...queue(), { t: `Góndola · ${c.nombre}`, icon: 'eye', uuid: 'gon-' + Math.random().toString(16).slice(2, 8), at: new Date().toLocaleTimeString('es-CL', { hour: '2-digit', minute: '2-digit' }) }]); L.toast('Observación registrada', t === 'Producto nuestro vencido' ? 'Se registró la merma de góndola; no descuenta stock de la bodega.' : 'Comercial la verá en la ficha del cliente.', 'success'); } }] }); });
        $('[data-order]', host) && ($('[data-order]', host).onclick = () => { S.pago = null; S.screen = 'pedido'; draw(); });
        $$('[data-pago]', host).forEach((b) => (b.onclick = () => { S.pago = b.dataset.pago; draw(); }));
        // Cobranza en efectivo de facturas vencidas en el local, con recibo provisional y rendición del día (RF-07.11)
        $('[data-collect]', host) && ($('[data-collect]', host).onclick = () => { const c = L.findClient(S.cli); const facts = [['FE-71204', Math.round(c.vencida * 0.6)], ['FE-70988', c.vencida - Math.round(c.vencida * 0.6)]]; L.modal({
          title: 'Cobrar facturas vencidas',
          body: `<ul class="list">${facts.map(([f, m], i) => `<li><label class="check" style="width:100%"><input type="checkbox" data-fc="${m}" checked> <span class="grow mono">${f}</span><span class="num">${fmt.clp(m)}</span></label></li>`).join('')}</ul>
            <div class="field" style="margin-top:var(--sp-3)"><label for="cb-m">Monto recibido en efectivo <span class="req" aria-hidden="true">*</span></label><div class="input-group"><span class="addon">$</span><input id="cb-m" class="input num" inputmode="numeric" value="${c.vencida}"></div></div>
            <p class="hint">Se emite un recibo provisional digital. El efectivo debe rendirse hoy en caja; si no, el turno queda con descuadre.</p>`,
          onOpen: (d) => L.bindField($('#cb-m', d), ['required', (v) => (parseInt(String(v).replace(/\D/g, ''), 10) > 0 ? '' : 'Ingrese el monto recibido.')]),
          actions: [{ label: 'Cancelar' }, { label: 'Emitir recibo provisional', cls: 'btn-primary', onClick: (api) => { if (!L.validateAll(api.el)) return false; const m = parseInt($('#cb-m', api.el).value.replace(/\D/g, ''), 10); const id = 'RP-' + (5120 + L.preventaRecibos().length); L.store.set('preventa.recibos', [...L.preventaRecibos(), { id, cliente: c.nombre, monto: m, hora: new Date().toLocaleTimeString('es-CL', { hour: '2-digit', minute: '2-digit' }), rendido: false }]); if (!L.online()) setQueue([...queue(), { t: `Recibo ${id} · ${c.nombre}`, icon: 'cash', uuid: 'rcb-' + Math.random().toString(16).slice(2, 8), at: '09:4' + queue().length }]); L.toast(`Recibo provisional ${id} emitido`, `${fmt.clp(m)} · se suma a su efectivo por rendir hoy en caja.`, 'success'); } }]
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
