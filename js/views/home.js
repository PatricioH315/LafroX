/* Portal principal con sesión: inicio personalizado por perfil, tablero con componentes
   configurables, bandeja de tareas, notificaciones y preferencias. */
(function (L) {
  const { esc, icon, $, $$, data: D, fmt } = L;
  const C = L.charts;

  const kind = (e) => D.estadoKind[e] || '';
  L.estadoBadge = (e) => L.badge(e, kind(e));

  /* ---------- Catálogo de componentes del tablero ---------- */
  const W = {
    kpis: { title: 'Indicadores clave', span: 'span-all', render: () => `<div class="grid grid-4">${D.kpis.slice(0, 4).map((k) => kpiCard(k)).join('')}</div>` },
    flujo: { title: 'Pedidos de hoy por estado', render: () => { const cnt = {}; D.pedidos.forEach((p) => (cnt[p.estado] = (cnt[p.estado] || 0) + 1)); const items = ['Capturado sin conexión', 'Confirmado', 'Retenido', 'En picking', 'En ruta', 'Entregado', 'Fallido'].map((e) => ({ label: e, value: (cnt[e] || 0) * 23, drill: '/pedidos?estado=' + encodeURIComponent(e), color: e === 'Retenido' || e === 'Fallido' ? 'var(--c-danger)' : e === 'Entregado' ? 'var(--chart-2)' : undefined })); return C.hbar(items, { label: 'Pedidos por estado' }); } },
    alertas: { title: 'Alertas', render: () => `<ul class="list">${D.notificaciones.slice(0, 4).map((n) => `<li><span class="badge badge-${n.kind === 'danger' ? 'danger' : n.kind === 'warning' ? 'warning' : n.kind === 'success' ? 'success' : 'info'} plain" style="padding:6px">${icon(n.kind === 'danger' ? 'alert-circle' : n.kind === 'warning' ? 'alert' : 'info', 'icon-sm')}</span><a class="grow item-link" href="#${n.ruta}" style="display:block;min-height:0"><div class="title">${esc(n.t)}</div><div class="sub">${esc(n.d)} · ${esc(n.hace)}</div></a></li>`).join('')}</ul>` },
    rutas: { title: 'Rutas en curso', render: () => `<ul class="list">${D.rutas.slice(0, 5).map((r) => `<li><a class="item-link" href="#/rutas/${r.id}"><span class="avatar dark" style="border-radius:8px;font-size:12px">${r.id}</span><div class="grow"><div class="title">${esc(r.zona)} · ${esc(r.conductor)}</div><div class="progress" style="margin-top:6px"><span style="width:${(r.hechas / r.paradas) * 100}%"></span></div></div><span class="small num">${r.hechas}/${r.paradas}</span></a></li>`).join('')}</ul><a class="btn btn-tertiary btn-sm" href="#/rutas">Ver las 12 rutas${icon('arrow-right', 'icon-sm')}</a>` },
    tareas: { title: 'Mis tareas', render: () => { const t = L.myTasks(); return t.length ? `<ul class="list">${t.slice(0, 4).map((x) => `<li><a class="item-link" href="#${x.ruta}"><span class="badge ${x.prioridad === 'Crítica' ? 'badge-danger' : x.prioridad === 'Alta' ? 'badge-warning' : ''} plain">${esc(x.tipo)}</span><div class="grow"><div class="title">${esc(x.titulo)}</div><div class="sub">${esc(x.ref)} · vence ${esc(x.plazo)}</div></div>${icon('chev-right')}</a></li>`).join('')}</ul><a class="btn btn-tertiary btn-sm" href="#/bandeja">Abrir bandeja${icon('arrow-right', 'icon-sm')}</a>` : L.empty('done', 'Sin tareas pendientes', 'Cuando algo requiera su acción aparecerá aquí.'); } },
    calidad: { title: 'Lotes bajo control de Calidad', render: () => `<ul class="list">${D.lotes.slice(0, 4).map((l) => `<li><a class="item-link" href="#/calidad/lotes/${l.id}"><span class="mono small">${l.id}</span><div class="grow"><div class="title">${esc(l.producto)}</div><div class="sub">${esc(l.proveedor)}</div></div>${L.badge(l.estado, l.estado === 'Retenido' ? 'danger' : l.estado === 'En evaluación' ? 'warning' : 'success')}</a></li>`).join('')}</ul><a class="btn btn-secondary btn-sm" href="#/calidad/retiro">${icon('shield', 'icon-sm')}Simulacro de retiro</a>` },
    ocupacion: { title: 'Ocupación de bodegas', render: () => C.hbar(D.sitios.map((s) => ({ label: s.nombre, value: s.ocupacion, color: s.ocupacion > 80 ? 'var(--c-danger)' : undefined, drill: '/inventario' })), { unit: '%', max: 100, label: 'Ocupación por sitio' }) },
    telemetria: { title: 'Cadena de frío en ruta', render: () => `<ul class="list">${D.camiones.map((c) => `<li><a class="item-link" href="#/telemetria">${icon(c.temp < 0 ? 'snow' : 'thermo')}<div class="grow"><div class="title">${esc(c.camion)} · ${esc(c.ruta)}</div><div class="sub">Consigna ${c.setpoint} °C · ${esc(c.señal)}</div></div><strong class="num">${fmt.n(c.temp, 1)} °C</strong>${L.badge(c.estado, c.estado === 'Normal' ? 'success' : c.estado === 'Advertencia' ? 'warning' : 'danger')}</a></li>`).join('')}</ul>` },
    agenda: { title: 'Mi agenda de visitas', render: () => `<ul class="list">${D.clientes.filter((c) => c.preventista === 'Sandra Riffo').slice(0, 5).map((c, i) => `<li><span class="small num" style="width:44px">${9 + i}:${i % 2 ? '30' : '00'}</span><a class="grow item-link" href="#/clientes/${c.id}" style="display:block;min-height:0"><div class="title">${esc(c.nombre)}</div><div class="sub">${esc(c.comuna)} · ${c.vencida ? 'deuda vencida' : 'al día'}</div></a>${c.vencida ? L.badge('Mora', 'danger') : ''}</li>`).join('')}</ul><a class="btn btn-primary btn-sm" href="#/terreno/preventa">${icon('cart', 'icon-sm')}Abrir app de preventa</a>` },
    'ruta-dia': { title: 'Mi ruta de hoy · R-01 Cauquenes', render: () => `<div class="row" style="gap:var(--sp-5)"><div class="ring" style="--p:${Math.round((L.fieldDone() / D.paradas.length) * 100)}" data-label="${L.fieldDone()}/${D.paradas.length}"></div><div><strong>${D.paradas.length - L.fieldDone()} entregas pendientes</strong><p class="small muted" style="margin:0">Camión KXTR-21 · salida 07:15 · ${L.online() ? 'en línea' : 'sin conexión'}</p></div></div><a class="btn btn-primary" style="margin-top:var(--sp-4)" href="#/terreno">${icon('truck')}Abrir app de reparto</a>` },
    mision: { title: 'Misión de preparación M-3302', render: () => `<p class="small muted">Zona refrigerada · 42 líneas · FEFO</p><div class="progress"><span style="width:62%"></span></div><p class="small" style="margin-top:6px">26 de 42 líneas confirmadas</p><a class="btn btn-primary" href="#/preparacion">${icon('scan')}Continuar misión</a>` },
    clientes: { title: 'Clientes con riesgo', render: () => `<ul class="list">${D.clientes.filter((c) => c.vencida || c.otif < 82).slice(0, 5).map((c) => `<li><a class="item-link" href="#/clientes/${c.id}"><span class="avatar">${L.initials(c.nombre)}</span><div class="grow"><div class="title">${esc(c.nombre)}</div><div class="sub">OTIF ${fmt.pct(c.otif)} · ${c.vencida ? 'vencido ' + fmt.clp(c.vencida) : 'al día'}</div></div></a></li>`).join('')}</ul>` },
    rendicion: { title: 'Rendición del día', render: () => `<dl class="stat-list"><div><dt>Esperado</dt><dd class="num">${fmt.clp(18420000)}</dd></div><div><dt>Rendido</dt><dd class="num">${fmt.clp(18291500)}</dd></div><div><dt>Diferencia</dt><dd class="num" style="color:var(--c-danger)">−${fmt.clp(128500)}</dd></div></dl><a class="btn btn-secondary btn-sm" style="margin-top:12px" href="#/rendicion">Revisar descuadres</a>` },
    admin: { title: 'Administración', render: () => `<dl class="stat-list"><div><dt>Personas activas</dt><dd class="num">${D.usuarios.filter((u) => u.estado === 'Activo').length * 11}</dd></div><div><dt>Cambios por aprobar</dt><dd class="num">1</dd></div><div><dt>Eventos de auditoría hoy</dt><dd class="num">1.284</dd></div></dl><div class="btn-group" style="margin-top:12px"><a class="btn btn-secondary btn-sm" href="#/admin/usuarios">Personas</a><a class="btn btn-secondary btn-sm" href="#/admin/auditoria">Auditoría</a></div>` },
    'mis-pedidos': { title: 'Mis pedidos', render: () => `<ol class="timeline"><li class="done"><span class="dot"></span><div class="t-title">PV-264790 entregado</div><div class="t-meta">Ayer 09:14 · firma digital</div></li><li class="current"><span class="dot"></span><div class="t-title">PV-264821 llega mañana 09:00–09:30</div><div class="t-meta">Confirmado · $186.400</div></li></ol><a class="btn btn-primary btn-sm" href="#/portal/pedido">${icon('cart', 'icon-sm')}Hacer un pedido</a>` },
    transp: { title: 'Rutas asignadas para mañana', render: () => `<dl class="stat-list"><div><dt>Rutas asignadas</dt><dd class="num">${D.rutas.filter((r) => r.externo).length}</dd></div><div><dt>Por confirmar</dt><dd class="num" style="color:var(--c-warning)">${D.rutas.filter((r) => r.externo).length - 1}</dd></div><div><dt>Plazo</dt><dd>Hoy 18:00</dd></div></dl><a class="btn btn-primary btn-sm" style="margin-top:12px" href="#/portal/transportista">${icon('truck', 'icon-sm')}Asignar conductores</a>` },
    prov: { title: 'Mis órdenes de compra', render: () => `<dl class="stat-list"><div><dt>Abiertas</dt><dd class="num">${D.ocs.filter((o) => o.estado !== 'Cerrada').length}</dd></div><div><dt>En recepción</dt><dd class="num">1</dd></div><div><dt>Discrepancias</dt><dd class="num" style="color:var(--c-warning)">2</dd></div></dl><a class="btn btn-secondary btn-sm" style="margin-top:12px" href="#/portal/proveedor">Ver órdenes y recepciones</a>` },
    cuenta: { title: 'Mi cuenta', render: () => `<dl class="stat-list"><div><dt>Crédito disponible</dt><dd class="num">${fmt.clp(612000)}</dd></div><div><dt>Saldo por pagar</dt><dd class="num">${fmt.clp(188000)}</dd></div><div><dt>Canastillos en su poder</dt><dd class="num">38</dd></div></dl><a class="btn btn-secondary btn-sm" style="margin-top:12px" href="#/portal/cuenta">Ver estado de cuenta</a>` },
    entregas: { title: 'Entregas de la semana', render: () => C.stacked(['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'], [{ name: 'A tiempo', values: [1180, 1210, 1260, 1195, 1288, 690] }, { name: 'Tarde', values: [130, 118, 104, 122, 99, 61] }, { name: 'Fallidas', values: [58, 51, 49, 55, 44, 30], color: 'var(--c-danger)' }], { label: 'Entregas por día y resultado' }) + C.legend([{ label: 'A tiempo' }, { label: 'Tarde' }, { label: 'Fallidas', color: 'var(--c-danger)' }]) }
  };
  L.widgets = W;

  function kpiCard(k) {
    const improving = k.good === 'up' ? k.value > k.base : k.value < k.base;
    const delta = k.value - k.base;
    return `<a class="card card-link kpi" href="#/analitica/${k.id}"><span class="label">${esc(k.label)} ${L.tip(k.desc)}</span><span class="value">${k.unit === '%' ? fmt.pct(k.value) : fmt.n(k.value, 1) + ' ' + k.unit}</span>
      <span class="meta"><span class="${improving ? 'delta-up' : 'delta-down'}">${delta > 0 ? '▲' : '▼'} ${fmt.n(Math.abs(delta), 1)} pts</span> vs. 2025 · meta ${k.unit === '%' ? fmt.pct(k.meta, 0) : k.meta + ' ' + k.unit}</span>
      <span class="spark">${C.spark(D.serie[k.id], { color: improving ? 'var(--chart-1)' : 'var(--c-danger)' })}</span></a>`;
  }
  L.kpiCard = kpiCard;

  const widgetHtml = (id, editing) => {
    const w = W[id];
    return `<section class="card widget ${w.span || ''}" data-w="${id}" aria-labelledby="w-${id}" ${editing ? 'draggable="true"' : ''}>
      <div class="card-head"><h2 id="w-${id}">${esc(w.title)}</h2>${editing ? `<div class="widget-tools"><button type="button" class="btn btn-tertiary btn-icon btn-sm" data-wmove="-1" aria-label="Mover ${esc(w.title)} antes">${icon('chev-up', 'icon-sm')}</button><button type="button" class="btn btn-tertiary btn-icon btn-sm" data-wmove="1" aria-label="Mover ${esc(w.title)} después">${icon('chev-down', 'icon-sm')}</button><button type="button" class="btn btn-tertiary btn-icon btn-sm" data-wrm aria-label="Ocultar ${esc(w.title)}">${icon('eye-off', 'icon-sm')}</button><span class="drag-handle" aria-hidden="true">${icon('grip')}</span></div>` : ''}</div>
      <div class="w-body">${L.skeleton(3)}</div></section>`;
  };

  // Componente de tablero configurable reutilizado por inicio y tablero
  function mountWidgets(root, key, defaults, all = Object.keys(W)) {
    let list = L.store.get(key, defaults).filter((x) => W[x]);
    let editing = false;
    const host = $('#widgets', root);
    const bar = $('#w-bar', root);
    const draw = (fast) => {
      host.classList.toggle('editing', editing);
      host.innerHTML = list.length ? list.map((id) => widgetHtml(id, editing)).join('') : `<div class="span-all card">${L.empty('box', 'Su tablero está vacío', 'Agregue componentes para ver aquí la información que más usa.', '<button type="button" class="btn btn-primary" data-wadd>Agregar componentes</button>')}</div>`;
      $$('.widget', host).forEach((el, i) => { const fill = () => { el.querySelector('.w-body').innerHTML = W[el.dataset.w].render(); L.accordions(el); }; fast ? fill() : L.timeout(fill, 250 + i * 90); });
      bar.innerHTML = editing
        ? `<button type="button" class="btn btn-secondary" data-wadd>${icon('plus')}Agregar componente</button><button type="button" class="btn btn-tertiary" data-wreset>Restablecer</button><button type="button" class="btn btn-primary" data-wdone>${icon('check')}Guardar diseño</button>`
        : `<button type="button" class="btn btn-secondary" data-wedit>${icon('sliders')}Personalizar</button>`;
    };
    const save = () => L.store.set(key, list);
    root.addEventListener('click', (e) => {
      if (e.target.closest('[data-wedit]')) { editing = true; draw(true); L.announce('Modo de personalización activado'); }
      else if (e.target.closest('[data-wdone]')) { editing = false; save(); draw(true); L.toast('Diseño guardado', 'Su tablero se verá así en este equipo.', 'success'); }
      else if (e.target.closest('[data-wreset]')) { list = [...defaults]; draw(true); }
      else if (e.target.closest('[data-wrm]')) { const id = e.target.closest('.widget').dataset.w; list = list.filter((x) => x !== id); draw(true); L.toast('Componente oculto', W[id].title, 'info', { action: 'Deshacer', onAction: () => { list.push(id); draw(true); } }); }
      else if (e.target.closest('[data-wmove]')) { const b = e.target.closest('[data-wmove]'); const id = b.closest('.widget').dataset.w; const i = list.indexOf(id), j = i + Number(b.dataset.wmove); if (j < 0 || j >= list.length) return; [list[i], list[j]] = [list[j], list[i]]; draw(true); $(`.widget[data-w="${id}"] [data-wmove="${b.dataset.wmove}"]`, host)?.focus(); }
      else if (e.target.closest('[data-wadd]')) {
        const avail = all.filter((x) => !list.includes(x));
        L.modal({ title: 'Agregar componentes', body: avail.length ? `<p class="muted">Elija los componentes que quiere ver en su tablero.</p>${avail.map((id) => `<label class="check"><input type="checkbox" value="${id}"> ${esc(W[id].title)}</label>`).join('')}` : '<p>Ya tiene todos los componentes disponibles.</p>', actions: [{ label: 'Cancelar' }, { label: 'Agregar', cls: 'btn-primary', onClick: (api) => { const sel = $$('input:checked', api.el).map((i) => i.value); list.push(...sel); editing = true; draw(true); if (sel.length) L.toast(`${sel.length} componente(s) agregado(s)`, '', 'success'); } }] });
      }
    });
    // Reordenar arrastrando
    let dragId = null;
    host.addEventListener('dragstart', (e) => { const w = e.target.closest('.widget'); if (!w) return; dragId = w.dataset.w; w.classList.add('dragging'); e.dataTransfer.effectAllowed = 'move'; });
    host.addEventListener('dragend', (e) => { e.target.closest('.widget')?.classList.remove('dragging'); $$('.drop-target', host).forEach((x) => x.classList.remove('drop-target')); });
    host.addEventListener('dragover', (e) => { const w = e.target.closest('.widget'); if (!w || !dragId) return; e.preventDefault(); $$('.drop-target', host).forEach((x) => x.classList.remove('drop-target')); w.classList.add('drop-target'); });
    host.addEventListener('drop', (e) => { const w = e.target.closest('.widget'); if (!w || !dragId) return; e.preventDefault(); const i = list.indexOf(dragId), j = list.indexOf(w.dataset.w); list.splice(i, 1); list.splice(j, 0, dragId); dragId = null; draw(true); });
    draw();
  }

  /* ---------- Acciones principales por perfil (RT-25.01: máx. 3 interacciones) ---------- */
  const QUICK = {
    evaluador: [['activity', 'Recorrer el flujo de un pedido', '7 pasos de punta a punta', '/flujo'], ['truck', 'Ver la app de reparto', 'Perfil de terreno sin conexión', '/terreno'], ['chart', 'Abrir el tablero analítico', '7 tipos de gráfico', '/analitica']],
    'gerente-ops': [['route', 'Revisar rutas del día', '12 rutas en curso', '/rutas'], ['chart', 'OTIF de hoy', 'Profundizar hasta la entrega', '/analitica/otif'], ['alert', 'Excepciones abiertas', '3 requieren decisión', '/bandeja']],
    planificador: [['route', 'Revisar ruta propuesta', 'Plan de mañana, 84 rutas', '/rutas'], ['thermo', 'Ver recorridos reales', 'Desvíos y telemetría', '/telemetria'], ['clipboard', 'Pedidos por planificar', 'Confirmados sin ruta', '/pedidos?estado=Confirmado']],
    preventista: [['cart', 'Tomar un pedido', 'Funciona sin señal', '/terreno/preventa'], ['store', 'Mis clientes', 'Crédito, deuda e historial', '/clientes'], ['clipboard', 'Mis pedidos', 'Estado de sincronización', '/pedidos']],
    conductor: [['truck', 'Iniciar mi ruta', '6 entregas · R-01', '/terreno'], ['undo', 'Registrar devolución', 'Producto y envases', '/devoluciones/nueva'], ['cash', 'Rendir mi turno', 'Efectivo y documentos', '/rendicion']],
    preparador: [['scan', 'Continuar misión', 'M-3302 · 16 líneas', '/preparacion'], ['download', 'Recepción en andén', 'OC-88412 en curso', '/recepcion/nueva']],
    bodega: [['download', 'Recepciones del día', '3 programadas', '/recepcion'], ['warehouse', 'Inventario y FEFO', 'Ocupación por zona', '/inventario'], ['undo', 'Devoluciones por evaluar', 'Aprobar destino', '/devoluciones']],
    calidad: [['shield', 'Simulacro de retiro', 'Lote → clientes en < 2 h', '/calidad/retiro'], ['thermo', 'Excursiones térmicas', '1 crítica abierta', '/telemetria'], ['box', 'Lotes retenidos', 'Disposición sanitaria', '/calidad']],
    comercial: [['store', 'Cartera de clientes', 'Rentabilidad y riesgo', '/clientes'], ['link', 'Pedidos EDI', '3 en excepción', '/canal-moderno'], ['chart', 'Indicadores comerciales', 'OTIF y fill rate', '/analitica']],
    finanzas: [['cash', 'Rendiciones del día', 'Descuadres por tipificar', '/rendicion'], ['chart', 'Costo de servir', 'Por cliente y canal', '/analitica/costo'], ['store', 'Crédito y cobranza', 'Clientes en mora', '/clientes']],
    ti: [['users', 'Personas usuarias', 'Altas, bajas y roles', '/admin/usuarios'], ['sliders', 'Parámetros', '1 cambio por aprobar', '/admin/parametros'], ['history', 'Auditoría', 'Consultar y exportar', '/admin/auditoria']],
    cliente: [['cart', 'Hacer un pedido', 'Con su crédito disponible', '/portal/pedido'], ['truck', 'Seguir mi entrega', 'Ventana de 30 minutos', '/portal/entregas'], ['file', 'Descargar documentos', 'Facturas y guías', '/portal/cuenta']],
    'cliente-moderno': [['cart', 'Pedido manual', 'Además del EDI de la cadena', '/portal/pedido'], ['truck', 'Entregas por local', 'Ventana de 30 minutos', '/portal/entregas'], ['file', 'Documentos y acuses', 'Facturas, guías y ASN', '/portal/cuenta']],
    'conductor-ext': [['truck', 'Iniciar mi ruta', 'Credencial de turno de 14 h', '/terreno'], ['undo', 'Registrar devolución', 'Producto y envases', '/devoluciones/nueva'], ['cash', 'Rendir mi turno', 'Efectivo y documentos', '/rendicion']],
    transportista: [['truck', 'Asignar conductor y vehículo', 'Rutas de mañana', '/portal/transportista'], ['inbox', 'Mis tareas', 'Plazo hoy 18:00', '/bandeja']],
    proveedor: [['box', 'Órdenes y recepciones', 'Solo lectura', '/portal/proveedor'], ['inbox', 'Mis tareas', 'Discrepancias por revisar', '/bandeja']]
  };

  L.route('/inicio', {
    title: 'Inicio', noCrumb: true, block: 'Portal principal', module: 'Transversal', rf: ['RF-17.07', 'RF-16.02'], actors: ['Todos los perfiles'],
    render: () => {
      const p = L.me();
      const h = D.today.getHours();
      return `<div class="page-head"><div class="titles"><span class="page-kicker">${esc(p.iface)}</span><h1>${h < 12 ? 'Buenos días' : h < 20 ? 'Buenas tardes' : 'Buenas noches'}, ${esc(p.name.split(' ')[0])}</h1><p class="muted" style="margin:0">${esc(p.role)} · viernes 13 de noviembre de 2026</p></div><div class="actions" id="w-bar"></div></div>
        ${p.id === 'evaluador' ? L.alert('info', 'Perfil de evaluación', 'Este perfil ve todos los módulos. Use «Cambiar perfil de demostración» en el menú de usuario para ver el inicio, el menú y los permisos de cada actor.', '<button type="button" class="btn btn-secondary btn-sm" data-switch>Cambiar perfil</button>') + '<div style="height:16px"></div>' : ''}
        <section aria-labelledby="qa-t" style="margin-bottom:var(--sp-5)"><h2 id="qa-t" class="sr-only">Accesos principales</h2><div class="grid grid-4">${(QUICK[p.id] || []).map(([i, t, s, r]) => `<a class="card card-link" href="#${r}" style="display:flex;gap:12px;align-items:center;padding:var(--sp-4)"><span class="avatar" style="border-radius:10px">${icon(i)}</span><span style="min-width:0"><strong style="display:block">${esc(t)}</strong><span class="small muted">${esc(s)}</span></span></a>`).join('')}</div></section>
        <div class="grid grid-2" id="widgets"></div>`;
    },
    mount: (root) => mountWidgets(root, 'w.home.' + L.me().id, L.me().home)
  });

  L.route('/tablero', {
    title: 'Tablero', parent: '/inicio', block: 'Portal principal', module: 'M10 Analítica (vista operacional)', rf: ['RF-11.06', 'RF-16.02'], actors: ['Gerentes', 'Jefaturas', 'Planificador'],
    render: () => `<div class="page-head"><div class="titles"><h1>Tablero principal</h1><p class="muted" style="margin:0">Componentes configurables: agréguelos, ocúltelos o reordénelos (arrastrando o con las flechas).</p></div><div class="actions" id="w-bar"></div></div>
      <div class="grid grid-2" id="widgets"></div>`,
    mount: (root) => mountWidgets(root, 'w.board.' + L.me().id, ['kpis', 'entregas', 'flujo', 'rutas', 'alertas', 'ocupacion'])
  });

  /* ---------- Bandeja de tareas unificada (RF-17.07) ---------- */
  L.route('/bandeja', {
    title: 'Bandeja de tareas', parent: '/inicio', block: 'Portal principal', module: 'Transversal (flujos RF-17.06)', rf: ['RF-17.06', 'RF-17.07'], actors: ['Todos los perfiles'],
    render: () => {
      const t = L.myTasks();
      const tipos = [...new Set(t.map((x) => x.tipo))];
      return `<div class="page-head"><div class="titles"><h1>Bandeja de tareas</h1><p class="muted" style="margin:0">Aprobaciones, revisiones y excepciones que esperan su acción.</p></div></div>
        ${L.tabsHtml('bt', [{ id: 'todas', label: 'Todas', count: t.length }, ...tipos.map((x) => ({ id: x, label: x, count: t.filter((y) => y.tipo === x).length }))], 'todas')}
        <div class="card card-flush" id="bt-list"></div>`;
    },
    mount: (root) => {
      const draw = (tipo) => {
        const t = L.myTasks().filter((x) => tipo === 'todas' || x.tipo === tipo);
        $('#bt-list', root).innerHTML = t.length ? `<ul class="list" style="padding:0 var(--sp-5)">${t.map((x) => `<li data-t="${x.id}" tabindex="-1"><span class="badge ${x.prioridad === 'Crítica' ? 'badge-danger' : x.prioridad === 'Alta' ? 'badge-warning' : 'badge-info'}">${esc(x.prioridad)}</span><div class="grow"><div class="title">${esc(x.titulo)}</div><div class="sub">${esc(x.tipo)} · ${esc(x.ref)} · vence ${esc(x.plazo)}</div></div><a class="btn btn-primary btn-sm" href="#${x.ruta}">Atender</a><div class="menu-wrap"><button type="button" class="btn btn-tertiary btn-icon" data-tm="${x.id}" aria-label="Más acciones para ${esc(x.titulo)}">${icon('more')}</button></div></li>`).join('')}</ul>` : L.empty('done', 'Bandeja al día', 'No tiene tareas de este tipo.');
        $$('[data-tm]', root).forEach((b) => L.menu(b, [{ label: 'Delegar a otra persona', icon: 'users', onClick: () => L.toast('Tarea delegada', 'Quedó registrada la delegación (RF-17.06).', 'success') }, { label: 'Posponer 1 hora', icon: 'clock', onClick: () => L.toast('Tarea pospuesta', '', 'info') }, { sep: true }, { label: 'Marcar como resuelta', icon: 'check', onClick: () => { b.closest('li').remove(); L.toast('Tarea resuelta', '', 'success'); } }]));
      };
      L.tabs(root.querySelector('.tabs'), draw);
      draw('todas');
    }
  });

  L.route('/notificaciones', {
    title: 'Notificaciones', parent: '/inicio', block: 'Portal principal', module: 'Transversal', rf: ['RF-17.10', 'RF-18.03'], actors: ['Todos los perfiles'],
    render: () => `<div class="page-head"><div class="titles"><h1>Notificaciones</h1></div><div class="actions"><button type="button" class="btn btn-secondary" id="nt-read">${icon('check')}Marcar todas como leídas</button></div></div>
      <div class="card"><ul class="list" id="nt">${D.notificaciones.map((n) => `<li><span class="badge-dot" style="background:var(--c-accent)"></span><a class="grow item-link" href="#${n.ruta}" style="display:block;min-height:0"><div class="title">${esc(n.t)}</div><div class="sub">${esc(n.d)} · ${esc(n.hace)}</div></a>${L.badge(n.kind === 'danger' ? 'Crítica' : n.kind === 'warning' ? 'Advertencia' : n.kind === 'success' ? 'Éxito' : 'Información', n.kind)}</li>`).join('')}</ul></div>`,
    mount: (root) => { $('#nt-read', root).onclick = () => { $$('.badge-dot', root).forEach((d) => (d.style.background = 'var(--c-line)')); L.toast('Notificaciones leídas', '', 'success'); }; }
  });

  /* ---------- Perfil y preferencias (RT-13.12 de SD4, RF-18.02) ---------- */
  L.route('/perfil', {
    title: 'Mi perfil y preferencias', parent: '/inicio', block: 'Portal principal', module: 'Transversal', rf: ['RF-18.02', 'RF-15.03'], actors: ['Todos los perfiles'],
    render: () => {
      const p = L.me();
      const pref = (k, d) => L.store.pref(k, d);
      return `<div class="page-head"><div class="titles"><h1>Mi perfil y preferencias</h1></div></div>
      <div class="split"><div class="stack-lg">
        <section class="card"><div class="card-head"><h2>Apariencia y lectura</h2></div>
          <div class="stack">
            <div><span class="label" id="pf-th" style="font-weight:600;display:block;margin-bottom:6px">Tema</span><div class="segmented" role="group" aria-labelledby="pf-th">${[['light', 'Claro'], ['dark', 'Oscuro'], ['', 'Según el sistema']].map(([v, l]) => `<button type="button" data-pref="theme" data-v="${v}" aria-pressed="${pref('theme', '') === v}">${l}</button>`).join('')}</div></div>
            <div><span id="pf-tx" style="font-weight:600;display:block;margin-bottom:6px">Tamaño del texto</span><div class="segmented" role="group" aria-labelledby="pf-tx">${[['md', 'Normal'], ['lg', 'Grande'], ['xl', 'Muy grande']].map(([v, l]) => `<button type="button" data-pref="text" data-v="${v}" aria-pressed="${pref('text', 'md') === v}">${l}</button>`).join('')}</div></div>
            <div><span id="pf-dn" style="font-weight:600;display:block;margin-bottom:6px">Densidad de los listados</span><div class="segmented" role="group" aria-labelledby="pf-dn">${[['compact', 'Compacta'], ['normal', 'Normal'], ['comfortable', 'Amplia']].map(([v, l]) => `<button type="button" data-pref="density" data-v="${v}" aria-pressed="${pref('density', 'normal') === v}">${l}</button>`).join('')}</div></div>
          </div></section>
        <section class="card"><div class="card-head"><h2>Notificaciones</h2></div>
          <div class="table-wrap"><table class="table"><caption class="sr-only">Canales por tipo de aviso</caption><thead><tr><th>Aviso</th><th>App</th><th>Correo</th><th>SMS</th></tr></thead><tbody>${['Tareas asignadas', 'Alertas críticas', 'Resumen diario'].map((t, i) => `<tr><td>${t}</td>${[1, i !== 1, i === 1].map((on, j) => `<td><label class="switch"><input type="checkbox" ${on ? 'checked' : ''} aria-label="${t} por ${['app', 'correo', 'SMS'][j]}"></label></td>`).join('')}</tr>`).join('')}</tbody></table></div>
          <button type="button" class="btn btn-primary" style="margin-top:var(--sp-4)" id="pf-save">Guardar preferencias</button></section>
      </div>
      <aside class="card stack"><div class="row"><span class="avatar lg">${L.initials(p.name)}</span><div><strong>${esc(p.name)}</strong><div class="small muted">${esc(p.role)}</div></div></div>
        <dl class="desc-list"><dt>Interfaz</dt><dd>${esc(p.iface)}</dd><dt>Segundo factor</dt><dd>${p.mfa ? L.badge('Activo', 'success') : L.badge('No exigido', '')}</dd><dt>Sesión</dt><dd>Única para todos los módulos (SSO)</dd></dl>
        <button type="button" class="btn btn-secondary" data-switch>${icon('users')}Cambiar perfil de demostración</button>
        <button type="button" class="btn btn-tertiary" onclick="LFX.signOut()">${icon('logout')}Cerrar sesión</button></aside></div>`;
    },
    mount: (root) => {
      $$('[data-pref]', root).forEach((b) => (b.onclick = () => {
        const k = b.dataset.pref, v = b.dataset.v;
        $$(`[data-pref="${k}"]`, root).forEach((x) => x.setAttribute('aria-pressed', x === b));
        L.store.setPref(k, v);
        if (k === 'theme') { if (v) document.documentElement.dataset.theme = v; else delete document.documentElement.dataset.theme; }
        else L.applyPrefs();
        L.toast('Preferencia aplicada', b.textContent, 'success', { duration: 2000 });
      }));
      $('#pf-save', root).onclick = (e) => L.busy(e.currentTarget, () => L.toast('Preferencias guardadas', 'Se aplican en todos sus dispositivos.', 'success'), 700);
    }
  });
})(window.LFX);
