/* Shell de la aplicación: sesión simulada, perfiles, menú principal, barra superior,
   rastro de navegación, búsqueda global, acciones rápidas y preferencias. */
(function (L) {
  const { $, $$, esc, icon } = L;

  /* ---------- Estructura de menús (fuente del mapa del sitio, RT-25.09) ---------- */
  L.nav = [
    { group: 'Inicio', items: [
      { path: '/inicio', label: 'Inicio', icon: 'home' },
      { path: '/guia', label: 'Guía de mi perfil', icon: 'route' },
      { path: '/tablero', label: 'Tablero', icon: 'grid' },
      { path: '/bandeja', label: 'Bandeja de tareas', icon: 'inbox', badge: 'tareas' }
    ] },
    { group: 'Operación', items: [
      { path: '/pedidos', label: 'Pedidos', icon: 'clipboard', mod: 'M3' },
      { path: '/flujo', label: 'Flujo de pedido', icon: 'activity', mod: 'M3–M7' },
      { path: '/rutas', label: 'Rutas', icon: 'route', mod: 'M4' },
      { path: '/preparacion', label: 'Preparación', icon: 'box', mod: 'M5' },
      { path: '/terreno', label: 'Reparto en terreno', icon: 'truck', mod: 'M6' },
      { path: '/terreno/preventa', label: 'Preventa en terreno', icon: 'cart', mod: 'M3' },
      { path: '/rendicion', label: 'Cobranza y rendición', icon: 'cash', mod: 'M7' }
    ] },
    { group: 'Bodega', items: [
      { path: '/recepcion', label: 'Recepción', icon: 'download', mod: 'M1' },
      { path: '/inventario', label: 'Inventario', icon: 'warehouse', mod: 'M2' },
      { path: '/devoluciones', label: 'Devoluciones y envases', icon: 'undo', mod: 'M8' }
    ] },
    { group: 'Calidad y flota', items: [
      { path: '/calidad', label: 'Calidad y trazabilidad', icon: 'shield', mod: 'M9' },
      { path: '/telemetria', label: 'Telemetría y frío', icon: 'thermo', mod: 'M12' }
    ] },
    { group: 'Clientes y canales', items: [
      { path: '/clientes', label: 'Clientes', icon: 'store', mod: 'Terceros' },
      { path: '/canal-moderno', label: 'Canal moderno EDI', icon: 'link', mod: 'M11' },
      { path: '/portal/pedido', label: 'Hacer un pedido', icon: 'cart', mod: 'Portal' },
      { path: '/portal/entregas', label: 'Mis entregas', icon: 'truck', mod: 'Portal' },
      { path: '/portal/cuenta', label: 'Estado de cuenta', icon: 'file', mod: 'Portal' },
      { path: '/portal/transportista', label: 'Portal de transportistas', icon: 'truck', mod: 'Portal' },
      { path: '/portal/proveedor', label: 'Portal de proveedores', icon: 'box', mod: 'Portal' }
    ] },
    { group: 'Analítica', items: [
      { path: '/analitica', label: 'Tablero analítico', icon: 'chart', mod: 'M10' }
    ] },
    { group: 'Administración', items: [
      { path: '/admin/usuarios', label: 'Personas usuarias', icon: 'users' },
      { path: '/admin/roles', label: 'Roles y permisos', icon: 'key' },
      { path: '/admin/parametros', label: 'Parámetros', icon: 'sliders' },
      { path: '/admin/flujos', label: 'Flujos de aprobación', icon: 'route' },
      { path: '/admin/auditoria', label: 'Auditoría', icon: 'history' }
    ] }
  ];
  const ALWAYS = ['/inicio', '/guia', '/tablero', '/bandeja', '/perfil', '/notificaciones', '/bienvenida'];

  /* ---------- Sesión simulada ---------- */
  L.session = () => L.store.get('session', null);
  L.setSession = (s) => L.store.set('session', s);
  L.me = () => { const s = L.session(); return s && L.profile(s.profile); };
  L.allowed = (path) => {
    const p = L.me();
    if (!p) return false;
    if (p.all) return true;
    const top = '/' + path.split('/').filter(Boolean).slice(0, path.startsWith('/admin') || path.startsWith('/portal') || path.startsWith('/terreno/') ? 2 : 1).join('/');
    return ALWAYS.includes(top) || p.menu.includes(top) || p.menu.includes(path);
  };
  /* Action-level permissions (RF-15.04; SD4 4.1: an actor related to a module does not see all its functions).
     The menu says which screens a profile opens; this matrix says what it may do inside them. */
  const PERM = {
    'cliente.bloquear': ['comercial', 'finanzas'],
    'cliente.cartera': ['comercial', 'finanzas'],
    'cliente.segmentar': ['comercial', 'finanzas'],
    'cliente.crear': ['comercial', 'preventista'],
    'cliente.editar': ['comercial', 'preventista'],
    'cliente.ventana': ['comercial', 'planificador'],
    'precio.excepcion': ['comercial'],
    'pedido.anular': ['comercial', 'gerente-ops'],
    'pedido.asignar': ['planificador', 'gerente-ops'],
    'pedido.autorizar': ['finanzas'],
    'pedido.facturar': ['comercial'],
    'ruta.planificar': ['planificador', 'gerente-ops'],
    'ruta.aprobar': ['planificador'],
    'prep.misiones': ['bodega'],
    'recepcion.registrar': ['bodega'],
    'recepcion.ubicar': ['bodega', 'preparador'],
    'erp.simular': ['bodega'],
    'inv.gestionar': ['bodega'],
    'inv.reposicion': ['bodega', 'gerente-ops'],
    'inv.ficha': ['gerente-ops'],
    'xd.causa': ['bodega', 'gerente-ops'],
    'dev.registrar': ['conductor', 'conductor-ext', 'bodega'],
    'dev.recepcionar': ['bodega'],
    'dev.destino': ['bodega'],
    'dev.nc': ['finanzas', 'bodega'],
    'calidad.disponer': ['calidad'],
    'calidad.retiro': ['calidad'],
    'geocerca.gestionar': ['gerente-ops'],
    'rend.gestionar': ['finanzas'],
    'edi.gestionar': ['comercial']
  };
  L.perm = PERM;
  L.can = (act) => { const p = L.me(); return !!p && (p.all || (PERM[act] || []).includes(p.id)); };
  // Short notice for screens where the profile only consults
  L.readOnly = (txt) => L.alert('info', 'Solo consulta para su perfil', txt || 'Las acciones de esta pantalla las ejecutan los perfiles responsables (RF-15.04).');
  L.signIn = (profileId, { remember = true } = {}) => {
    const first = !L.store.get('seen.' + profileId, false);
    L.setSession({ profile: profileId, at: Date.now(), first });
  };
  L.signOut = () => { L.setSession(null); L.toast('Sesión cerrada', 'Su sesión se cerró en todos los módulos (SSO).', 'info'); L.go('/'); };

  L.myTasks = () => { const p = L.me(); return L.data.tareas.filter((t) => !p || t.perfiles.includes(p.id)); };

  /* ---------- Render principal ---------- */
  const app = () => $('#app');

  L.render = (route, params, query, path) => {
    const s = L.session();
    const layout = route.layout;
    document.title = `${L.titleOf(route, params)} · Puelche · LafroX`;
    if (layout === 'app') {
      if (!$('.app .sidebar')) shell();
      updateShell(path);
      const main = $('#main');
      const denied = !L.allowed(path);
      const crumbs = L.crumbs(route, params, path);
      const bc = route.noCrumb ? '' : `<nav class="breadcrumb" aria-label="Rastro de navegación"><ol>${crumbs.map((c, i) => (i === crumbs.length - 1 ? `<li><span aria-current="page">${esc(c.label)}</span></li>` : `<li><a href="#${c.path}">${i === 0 && c.path === '/inicio' ? icon('home', 'icon-sm') + '<span class="sr-only">' : ''}${esc(c.label)}${i === 0 && c.path === '/inicio' ? '</span>' : ''}</a></li>`)).join('')}</ol></nav>`;
      let html;
      try { html = denied ? deniedView(route) : route.render(params, query); }
      catch (e) { console.error(e); html = L.empty('box', 'No pudimos mostrar esta pantalla', 'Ocurrió un error inesperado al preparar la vista. Vuelva al inicio e intente de nuevo.', '<a class="btn btn-primary" href="#/inicio">Volver al inicio</a>'); }
      main.innerHTML = `<div class="view view-enter">${bc}${html}</div>`;
      if (!denied) { try { route.mount?.(main.firstElementChild, params, query); } catch (e) { console.error(e); L.toast('Algo no funcionó en esta pantalla', 'Recargue la página o vuelva al inicio.', 'error'); } }
      L.accordions(main);
      main.focus({ preventScroll: true });
      window.scrollTo(0, 0);
      L.announce(`${L.titleOf(route, params)} cargado`);
      if (s && s.first && path === '/inicio') L.timeout(() => L.startTour(), 500);
    } else {
      app().className = 'no-shell';
      app().innerHTML = route.layout === 'public' ? publicShell(route.render(params, query), path) : route.render(params, query);
      route.mount?.(app(), params, query);
      L.accordions(app());
      $('#main')?.focus({ preventScroll: true });
      window.scrollTo(0, 0);
    }
  };

  function deniedView(route) {
    const owners = L.data.profiles.filter((p) => !p.all && p.menu?.some((m) => route.path.startsWith(m))).map((p) => p.role.split(' ·')[0]);
    return `${L.empty('box', 'Esta vista no está habilitada para su perfil', `El control de acceso basado en roles (RF-15.04) limita «${L.titleOf(route, {})}» a: ${owners.join(', ') || 'perfiles autorizados'}. Puede cambiar de perfil de demostración para revisarla.`, '<div class="btn-group"><a class="btn btn-secondary" href="#/inicio">Volver al inicio</a><button type="button" class="btn btn-primary" data-switch>Cambiar de perfil</button></div>')}`;
  }

  function publicShell(inner, path) {
    const s = L.session();
    return `<a class="skip-link" href="#main">Saltar al contenido</a>
    <header class="public-top">
      <a class="brand" href="#/" aria-label="Puelche, inicio">${logo()}<span class="brand-name">Puelche<span class="brand-sub">Distribuidora · desde 1974</span></span></a>
      <nav class="public-nav" aria-label="Sitio público">
        ${[['/', 'Inicio'], ['/catalogo', 'Catálogo'], ['/cobertura', 'Cobertura'], ['/contacto', 'Contacto']].map(([p, l]) => `<a href="#${p}" ${p === path ? 'aria-current="page"' : ''}>${l}</a>`).join('')}
      </nav>
      <span style="flex:1"></span>
      <button type="button" class="btn btn-tertiary btn-icon" data-theme-toggle aria-label="Cambiar entre modo claro y oscuro">${themeBtn()}</button>
      ${s ? '<a class="btn btn-primary" href="#/inicio">Ir a mi espacio</a>' : `<a class="btn btn-tertiary hide-sm" href="#/registro">Crear cuenta</a><a class="btn btn-primary" href="#/ingresar">${icon('user')}Ingresar</a>`}
    </header>
    <main id="main" class="public-main" tabindex="-1"><div class="view-enter">${inner}</div></main>
    <footer class="public-foot">Distribuidora Puelche S.A. · Talca, Región del Maule · Prototipo de LafroX para la licitación (Bases, cap. 25). Datos simulados.</footer>`;
  }

  const logo = (cls = 'brand-logo') => `<img class="${cls}" src="assets/logo.svg" alt="" width="32" height="34">`;
  L.logo = logo;

  function shell() {
    app().className = 'app';
    app().innerHTML = `
      <a class="skip-link" href="#main">Saltar al contenido</a>
      <aside class="sidebar" id="sidebar" aria-label="Menú principal">
        <div class="sidebar-head"><a class="brand" href="#/inicio">${logo()}<span class="brand-name">Puelche<span class="brand-sub">Plataforma LafroX</span></span></a><button type="button" class="sidebar-fold" aria-controls="sidebar" aria-expanded="true" aria-label="Plegar menú" title="Plegar menú" data-fold>${icon('chev-left')}</button></div>
        <nav class="nav" id="nav" aria-label="Principal"></nav>
        <div class="sidebar-foot">Prototipo navegable · datos simulados<br>Caso 02 Logística · Informe 3</div>
      </aside>
      <div class="scrim" data-close-nav></div>
      <header class="topbar">
        <button type="button" class="btn btn-tertiary btn-icon menu-toggle" aria-label="Abrir menú" aria-controls="sidebar" aria-expanded="false" data-open-nav>${icon('menu')}</button>
        <div class="combo" style="flex:1 1 auto;max-width:520px">
          <div class="input-wrap">${icon('search')}<label class="sr-only" for="gsearch">Búsqueda global</label><input id="gsearch" class="input" type="search" placeholder="Buscar cliente, pedido, ruta o pantalla…  ( / )" title="Filtre por tipo: cliente:, pedido:, ruta:, lote: o pantalla:"></div>
        </div>
        <span class="grow"></span>
        <span id="net-ind"></span>
        <div class="menu-wrap"><button type="button" class="btn btn-primary hide-sm" id="quick">${icon('plus')}Nuevo</button><button type="button" class="btn btn-primary btn-icon show-sm" id="quick-sm" aria-label="Acciones rápidas">${icon('plus')}</button></div>
        <div class="menu-wrap"><button type="button" class="btn btn-tertiary btn-icon" id="bell" aria-label="Avisos y notificaciones" style="position:relative">${icon('bell')}<span class="btn-label" aria-hidden="true">Avisos</span><span class="badge-dot" style="position:absolute;top:9px;right:9px"></span></button></div>
        <button type="button" class="btn btn-tertiary btn-icon hide-sm" data-theme-toggle aria-label="Cambiar entre modo claro y oscuro">${themeBtn()}</button>
        <div class="menu-wrap"><button type="button" class="btn btn-tertiary" id="usermenu" style="padding:0 6px" aria-label="Menú de usuario"><span class="avatar" id="me-av"></span><span class="hide-md" id="me-name" style="text-align:left;line-height:1.15"></span>${icon('chev-down', 'icon-sm hide-md')}</button></div>
      </header>
      <main id="main" class="main" tabindex="-1"></main>`;

    $('[data-open-nav]').onclick = () => toggleNav(!app().classList.contains('nav-open'));
    // Desktop: fold to an icon rail and back. Phone and tablet: close the drawer.
    $('[data-fold]').onclick = () => (isDesktop() ? setCollapsed(!app().classList.contains('sidebar-collapsed')) : toggleNav(false));
    setCollapsed(L.store.get('nav.collapsed', false), false);
    // The same button swaps between sidebar (desktop) and menu (drawer) icons when the breakpoint changes
    if (!L._bpWatch) {
      L._bpWatch = true;
      let wasDesktop = isDesktop();
      const onBp = () => { const d = isDesktop(); if (d === wasDesktop || !$('[data-fold]')) return; wasDesktop = d; toggleNav(false); setCollapsed(app().classList.contains('sidebar-collapsed'), false); };
      window.matchMedia('(min-width: 1024px)').addEventListener('change', onBp);
      window.addEventListener('resize', onBp);
    }
    $('[data-close-nav]').onclick = () => toggleNav(false);
    $('#nav').addEventListener('click', (e) => { if (e.target.closest('a') && !isDesktop()) toggleNav(false); });

    // Only the quick actions the profile can open and execute (RF-15.04)
    const quickItems = () => {
      const items = [
        { label: 'Nuevo pedido de preventa', icon: 'cart', kbd: 'P', path: '/flujo' },
        { label: 'Registrar devolución', icon: 'undo', kbd: 'D', path: '/devoluciones/nueva', act: 'dev.registrar' },
        { label: 'Simulacro de retiro sanitario', icon: 'shield', path: '/calidad/retiro', act: 'calidad.retiro' },
        { label: 'Registrar recepción', icon: 'download', path: '/recepcion/nueva', act: 'recepcion.registrar' },
        { label: 'Invitar persona usuaria', icon: 'users', path: '/admin/usuarios?nuevo=1' },
        { label: 'Exportar informe del día', icon: 'download', path: '/analitica?exportar=1' }
      ].filter((i) => L.allowed(i.path.split('?')[0]) && (!i.act || L.can(i.act))).map((i) => ({ label: i.label, icon: i.icon, kbd: i.kbd, onClick: () => L.go(i.path) }));
      return [{ title: 'Acciones rápidas' }, ...(items.length ? items : [{ label: 'Sin acciones rápidas para su perfil', icon: 'info', onClick: () => {} }])];
    };
    L.menu($('#quick'), quickItems);
    L.menu($('#quick-sm'), quickItems);

    L.menu($('#bell'), () => [{ title: 'Notificaciones' }, ...L.data.notificaciones.map((n) => ({ label: n.t, icon: n.kind === 'danger' ? 'alert-circle' : n.kind === 'warning' ? 'alert' : n.kind === 'success' ? 'check-circle' : 'info', onClick: () => L.go(n.ruta) })), { sep: true }, { label: 'Ver todas las notificaciones', icon: 'bell', onClick: () => L.go('/notificaciones') }]);

    L.menu($('#usermenu'), () => [
      { title: L.me().name },
      { label: 'Mi perfil y preferencias', icon: 'user', onClick: () => L.go('/perfil') }, { label: 'Atajos de teclado', icon: 'info', kbd: '?', onClick: () => L.showShortcuts() },
      { label: 'Cambiar perfil de demostración', icon: 'users', onClick: () => L.switchProfile() },
      { label: 'Ver recorrido guiado', icon: 'help', onClick: () => { L.go('/inicio'); setTimeout(L.startTour, 400); } },
      { label: isDark() ? 'Modo claro' : 'Modo oscuro', icon: isDark() ? 'sun' : 'moon', onClick: toggleTheme },
      { sep: true },
      { label: 'Cerrar sesión', icon: 'logout', danger: true, onClick: L.signOut }
    ]);

    // Búsqueda global (RF-17.11): clientes, pedidos, rutas y pantallas
    L.combobox($('#gsearch'), () => [
      ...L.nav.flatMap((g) => g.items).filter((i) => L.allowed(i.path)).map((i) => ({ label: i.label, meta: 'Pantalla', path: i.path, icon: i.icon })),
      ...L.data.clientes.map((c) => ({ label: c.nombre, meta: `Cliente · ${c.comuna}`, path: '/clientes/' + c.id, icon: 'store' })),
      ...L.data.pedidos.map((p) => ({ label: p.id, meta: `Pedido · ${p.clienteNombre}`, path: '/pedidos/' + p.id, icon: 'clipboard' })),
      ...L.data.rutas.map((r) => ({ label: `${r.id} ${r.zona}`, meta: `Ruta · ${r.conductor}`, path: '/rutas/' + r.id, icon: 'route' })),
      ...L.data.lotes.map((l) => ({ label: l.id, meta: `Lote · ${l.producto}`, path: '/calidad/lotes/' + l.id, icon: 'shield' }))
    ], {
      onSelect: (it) => { L.go(it.path); $('#gsearch').value = ''; $('#gsearch').blur(); },
      render: (it, q, hl) => `${icon(it.icon)}<span>${hl(it.label, q)}</span><span class="small muted" style="margin-left:auto;text-align:right">${esc(it.meta)}</span>`
    });
  }

  const isDesktop = () => window.matchMedia('(min-width: 1024px)').matches;
  /* Menú completo: en escritorio se pliega hacia la izquierda y se vuelve a desplegar hacia la derecha */
  function setCollapsed(c, save = true) {
    app().classList.toggle('sidebar-collapsed', c);
    if (save) L.store.set('nav.collapsed', c);
    const f = $('[data-fold]');
    const label = isDesktop() ? (c ? 'Desplegar menú' : 'Plegar menú') : 'Cerrar menú';
    f.innerHTML = icon(isDesktop() ? (c ? 'chev-right' : 'chev-left') : 'x');
    f.setAttribute('aria-expanded', isDesktop() ? !c : true);
    f.setAttribute('aria-label', label);
    f.title = label;
    railTitles();
  }

  // In the icon rail each link shows its name as a tooltip; the visible label stays in the DOM for screen readers
  function railTitles() {
    const rail = app().classList.contains('sidebar-collapsed') && isDesktop();
    $$('#nav a').forEach((a) => { const t = a.querySelector('.nav-text')?.textContent || ''; rail ? (a.title = t) : a.removeAttribute('title'); });
  }

  function toggleNav(open) {
    app().classList.toggle('nav-open', open);
    $('[data-open-nav]').setAttribute('aria-expanded', open);
    $('[data-open-nav]').setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    if (open) $('#nav a')?.focus();
  }

  function updateShell(path) {
    const p = L.me();
    const tasks = L.myTasks().length;
    $('#nav').innerHTML = L.nav.map((g) => {
      const items = g.items.filter((i) => L.allowed(i.path));
      if (!items.length) return '';
      return `<div class="nav-group"><span class="nav-label" id="ng-${esc(g.group)}">${esc(g.group)}</span><ul role="list" style="list-style:none;margin:0;padding:0" aria-labelledby="ng-${esc(g.group)}">${items.map((i) => {
        const cur = path === i.path || (i.path !== '/inicio' && path.startsWith(i.path + '/') && !g.items.some((o) => o !== i && path.startsWith(o.path) && o.path.length > i.path.length));
        return `<li><a href="#${i.path}" ${cur ? 'aria-current="page"' : ''}>${icon(i.icon)}<span class="nav-text">${esc(i.label)}</span>${i.badge && tasks ? `<span class="tag" aria-label="${tasks} pendientes">${tasks}</span>` : i.mod && p.all && /^M\d/.test(i.mod) ? `<span class="mod">${esc(i.mod)}</span>` : ''}</a></li>`;
      }).join('')}</ul></div>`;
    }).join('');
    railTitles();
    $('#me-av').textContent = L.initials(p.name);
    $('#me-name').innerHTML = `<strong style="display:block;font-size:var(--fs-sm)">${esc(p.name.split(' ').slice(0, 2).join(' '))}</strong><span class="small muted">${esc(p.role.split(' ·')[0])}</span>`;
    $$('[data-theme-toggle]').forEach((b) => (b.innerHTML = themeBtn()));
    renderNet();
  }

  /* ---------- Conectividad simulada (terreno) ---------- */
  L.online = () => L.store.get('online', true);
  L.setOnline = (v) => { L.store.set('online', v); renderNet(); document.dispatchEvent(new CustomEvent('lfx:net', { detail: v })); };
  function renderNet() {
    const el = $('#net-ind');
    if (!el) return;
    const p = L.me();
    el.innerHTML = p && (p.field || p.all) ? `<span class="badge ${L.online() ? 'badge-success' : 'badge-warning'}" title="Conectividad simulada">${L.online() ? 'En línea' : 'Sin conexión'}</span>` : '';
  }

  /* ---------- Selector de perfiles predeterminados (un perfil por actor de SD3) ---------- */
  const GROUPS = ['Evaluación', 'Terreno', 'Bodega y calidad', 'Oficina y gerencia', 'Externos'];
  L.profileSelectHtml = (id, selected) => `<select id="${id}" class="select">${GROUPS.map((g) => `<optgroup label="${esc(g)}">${L.data.profiles.filter((p) => p.grupo === g).map((p) => `<option value="${p.id}" ${p.id === selected ? 'selected' : ''}>${p.all ? esc(p.actor) : `${esc(p.actor)} — ${esc(p.name)}`}</option>`).join('')}</optgroup>`).join('')}</select>`;
  L.profileCard = (pid) => {
    const p = L.profile(pid);
    const mods = p.all ? 'Todos los módulos' : L.nav.flatMap((g) => g.items).filter((i) => p.menu.includes(i.path) && !['/inicio', '/tablero', '/bandeja'].includes(i.path)).map((i) => i.label).join(' · ');
    return `<div class="row" style="flex-wrap:nowrap;align-items:flex-start"><span class="avatar ${p.all ? 'dark' : ''}">${L.initials(p.name)}</span><div style="min-width:0"><strong>${esc(p.name)}</strong><div class="small muted">${esc(p.role)}</div><div class="small" style="margin-top:4px">${icon('phone', 'icon-sm')} ${esc(p.iface)}</div><div class="small muted" style="margin-top:4px">${esc(mods)}</div></div></div>`;
  };

  // Ingreso directo sin credenciales: queda registrado como sesión de demostración
  L.enterAs = (pid) => {
    L.signIn(pid);
    const next = L.store.get('next', '') || '/inicio';
    L.store.set('next', '');
    // Profiles that require a second factor (RF-15.03) also do so through the shortcut
    if (L.profile(pid).mfa) { L.store.set('pending2fa', next); L.go('/verificacion'); return; }
    L.toast('Sesión iniciada', `${L.profile(pid).actor}: ${L.profile(pid).name}`, 'success');
    L.go(L.session().first ? '/bienvenida' : next);
  };

  /* ---------- Cambio de perfil ---------- */
  L.switchProfile = () => {
    const cur = L.session()?.profile || 'evaluador';
    return L.modal({
      title: 'Cambiar de perfil',
      body: `<p class="muted">Un perfil predeterminado por cada actor del sistema (SD3, Anexo 3.A.12a). Cada uno ve su propio inicio y menú.</p>
        <div class="field"><label for="sw-p">Actor</label>${L.profileSelectHtml('sw-p', cur)}</div>
        <div class="card" id="sw-card" style="box-shadow:none;margin-top:var(--sp-3)">${L.profileCard(cur)}</div>`,
      onOpen(dlg) { const sel = $('#sw-p', dlg); sel.onchange = () => ($('#sw-card', dlg).innerHTML = L.profileCard(sel.value)); },
      actions: [{ label: 'Cancelar' }, { label: 'Cambiar de perfil', cls: 'btn-primary', onClick: (api) => {
        const pid = $('#sw-p', api.el).value;
        L.signIn(pid);
        const s = L.session(); s.first = false; L.setSession(s);
        L.toast('Perfil cambiado', `${L.profile(pid).actor}: ${L.profile(pid).name}`, 'success');
        L.go('/inicio');
        L.router.resolve();
      } }]
    });
  };

  /* ---------- Recorrido guiado de primer ingreso ---------- */
  L.startTour = () => {
    const s = L.session();
    const p = L.me();
    L.tour([
      { title: `Bienvenida, ${p.name.split(' ')[0]}`, text: 'Este recorrido de 5 pasos le muestra cómo moverse por la plataforma. Puede omitirlo y volver a verlo desde su menú de usuario.' },
      { target: '#nav', title: 'Menú principal', text: 'Aquí están solo los módulos de su perfil. Cualquier función principal queda a tres interacciones o menos.' },
      { target: '#gsearch', title: 'Búsqueda global', text: 'Busque clientes, pedidos, rutas, lotes o pantallas. Presione «/» desde cualquier lugar para llegar aquí.' },
      { target: '#quick', title: 'Acciones rápidas', text: 'Cree un pedido, registre una devolución o inicie un simulacro de retiro sin navegar por el menú.' },
      { target: '#widgets', title: 'Su tablero', text: 'Los componentes del inicio son configurables: muéstrelos, ocúltelos o reordénelos desde «Personalizar».' }
    ], () => {
      if (s) { s.first = false; L.setSession(s); L.store.set('seen.' + s.profile, true); }
      L.toast('Recorrido completado', 'Puede repetirlo desde el menú de usuario.', 'success');
    });
  };

  /* ---------- Preferencias: tema, tamaño de texto y densidad ---------- */
  const isDark = () => document.documentElement.dataset.theme === 'dark' || (!document.documentElement.dataset.theme && matchMedia('(prefers-color-scheme: dark)').matches);
  L.isDark = isDark;
  const themeBtn = () => `${icon(isDark() ? 'sun' : 'moon')}<span class="btn-label" aria-hidden="true">${isDark() ? 'Claro' : 'Oscuro'}</span>`;
  const toggleTheme = () => { const t = isDark() ? 'light' : 'dark'; document.documentElement.dataset.theme = t; L.store.setPref('theme', t); $$('[data-theme-toggle]').forEach((b) => (b.innerHTML = themeBtn())); L.toast(t === 'dark' ? 'Modo oscuro activado' : 'Modo claro activado', '', 'info', { duration: 2200 }); };
  L.toggleTheme = toggleTheme;
  L.applyPrefs = () => {
    const d = document.documentElement;
    const t = L.store.pref('theme', '');
    if (t) d.dataset.theme = t;
    d.dataset.text = L.store.pref('text', 'md');
    d.dataset.density = L.store.pref('density', 'normal');
    d.dataset.contrast = L.store.pref('contrast', 'normal');
  };

  /* ---------- Atajos y eventos globales ---------- */
  document.addEventListener('click', (e) => {
    if (e.target.closest('[data-theme-toggle]')) toggleTheme();
    if (e.target.closest('[data-switch]')) L.switchProfile();
  });
  // Atajos de una tecla (RT-13.11): no actúan al escribir ni con modificadores, y se pueden desactivar en «Mi perfil»
  L.shortcuts = [
    ['/', 'Buscar', null],
    ['g i', 'Ir al inicio de mi perfil', '/inicio'],
    ['g b', 'Ir a la bandeja de tareas', '/bandeja'],
    ['g n', 'Ir a las notificaciones', '/notificaciones'],
    ['g p', 'Ir a mi perfil y preferencias', '/perfil'],
    ['g s', 'Guardar borrador del pedido (Flujo o Portal)', null],
    ['?', 'Ver los atajos de teclado', null]
  ];
  L.showShortcuts = () => L.modal({
    title: 'Atajos de teclado',
    body: `<table class="table"><caption class="sr-only">Atajos disponibles</caption><thead><tr><th>Teclas</th><th>Acción</th></tr></thead><tbody>${L.shortcuts.map(([k, l]) => `<tr><td>${k.split(' ').map((x) => `<kbd>${L.esc(x)}</kbd>`).join(' luego ')}</td><td>${L.esc(l)}</td></tr>`).join('')}</tbody></table><p class="hint">Se desactivan en Mi perfil › Accesibilidad. No funcionan mientras escribe en un campo.</p>`,
    actions: [{ label: 'Cerrar', cls: 'btn-primary' }]
  });
  let pendingG = 0;
  document.addEventListener('keydown', (e) => {
    const typing = /INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName) || document.activeElement.isContentEditable;
    if (e.key === 'Escape' && app().classList.contains('nav-open')) toggleNav(false);
    if (typing || e.ctrlKey || e.metaKey || e.altKey || L.store.pref('shortcuts', 'on') === 'off' || !L.me() || document.querySelector('[role="dialog"][aria-modal="true"]')) return;
    if (e.key === '/' && $('#gsearch')) { e.preventDefault(); $('#gsearch').focus(); return; }
    if (e.key === '?') { e.preventDefault(); L.showShortcuts(); return; }
    if (e.key === 'g') { pendingG = Date.now(); return; }
    if (pendingG && Date.now() - pendingG < 1200) {
      pendingG = 0;
      if (e.key.toLowerCase() === 's') {
        e.preventDefault();
        if (L.saveDraft) L.saveDraft();
        else L.toast('Sin borrador en esta pantalla', 'Disponible en Flujo de pedido y Hacer un pedido.', 'info');
        return;
      }
      const hit = L.shortcuts.find(([k]) => k === 'g ' + e.key.toLowerCase());
      if (hit && L.allowed(hit[2])) { e.preventDefault(); L.go(hit[2]); }
    }
  });

  L.boot = () => {
    L.applyPrefs();
    if (!location.hash) location.hash = '/';
    L.router.resolve();
  };
})(window.LFX = window.LFX || {});
