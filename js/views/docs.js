/* Documentación del prototipo:
   arquitectura de información (RT-25.09), sistema de diseño (RT-25.05) y
   cumplimiento de las Bases con trazabilidad a SD3 (requerimientos) y SD4 (módulos). */
(function (L) {
  const { esc, icon, $, $$, data: D } = L;
  const lay = () => (L.session() ? 'app' : 'public');

  const routeLabel = (r) => (typeof r.title === 'function' ? r.title({}) : r.title);
  const ZONES = [
    { name: 'Sitio público', test: (r) => r.layout === 'public' && !['Autenticación e incorporación'].includes(r.block) && r.path !== '*' },
    { name: 'Autenticación e incorporación', test: (r) => r.block === 'Autenticación e incorporación' }
  ];

  /* ---------- Arquitectura de información ---------- */
  L.route('/arquitectura', {
    title: 'Arquitectura de información', parent: '/inicio', layout: 'app', block: 'Documentación (RT-25.09)', module: 'Prototipo', rf: ['RT-25.09', 'RT-25.01'], actors: ['Comisión evaluadora'],
    render: () => {
      const app = L.routes.filter((r) => r.layout === 'app' && !['/bienvenida'].includes(r.path));
      const byPath = (p) => L.routes.find((r) => r.path === p);
      const children = (p) => L.routes.filter((r) => r.path !== p && (typeof r.parent === 'string' ? r.parent === p : r.parent && r.parent({}) === p) && r.layout === 'app' && !L.nav.flatMap((g) => g.items).some((i) => i.path === r.path));
      const tree = (path, depth = 0) => { const kids = children(path); return kids.length && depth < 3 ? `<ul>${kids.map((k) => `<li><a href="#${k.path.includes(':') ? path : k.path}">${esc(routeLabel(k))}</a> <code class="small muted">${esc(k.path)}</code>${tree(k.path, depth + 1)}</li>`).join('')}</ul>` : ''; };
      const total = L.routes.filter((r) => r.path !== '*').length;
      return `<div class="page-head"><div class="titles"><span class="page-kicker">RT-25.09 · arquitectura de información</span><h1>Arquitectura de información del prototipo</h1><p class="muted" style="margin:0">${total} pantallas navegables. Todo se genera desde el mismo registro de rutas que usa la aplicación, por lo que el mapa siempre coincide con lo implementado.</p></div><div class="actions"><button type="button" class="btn btn-secondary" id="ia-print">${icon('printer')}Imprimir</button></div></div>
        <nav class="row" aria-label="Secciones de la página" style="margin-bottom:var(--sp-5)">${[['ia-mapa', 'Mapa del sitio'], ['ia-nav', 'Diagrama de navegación'], ['ia-tax', 'Taxonomía y nomenclatura'], ['ia-menu', 'Estructura de menús'], ['ia-jer', 'Jerarquía de la información'], ['ia-3', 'Regla de tres interacciones']].map(([a, b]) => `<a class="chip" href="javascript:void(0)" data-jump="${a}">${b}</a>`).join('')}</nav>

        <section class="card" id="ia-mapa" style="margin-bottom:var(--sp-5)"><div class="card-head"><h2>1. Mapa del sitio completo</h2><span class="badge plain">${total} pantallas</span></div>
          <div class="grid grid-3 sitemap">
            ${ZONES.map((z) => `<div><h3>${z.name}</h3><ul>${L.routes.filter(z.test).map((r) => `<li><a href="#${r.path}">${esc(routeLabel(r))}</a> <code class="small muted">${esc(r.path)}</code></li>`).join('')}</ul></div>`).join('')}
            ${L.nav.map((g) => `<div><h3>${esc(g.group)}</h3><ul>${g.items.map((i) => `<li><a href="#${i.path}">${esc(i.label)}</a>${i.mod ? ` <span class="badge plain mono">${esc(i.mod)}</span>` : ''}${tree(i.path)}</li>`).join('')}</ul></div>`).join('')}
            <div><h3>Utilidades globales</h3><ul><li><a href="#/perfil">Mi perfil y preferencias</a></li><li><a href="#/notificaciones">Notificaciones</a></li><li><a href="#/bienvenida">Bienvenida de primer ingreso</a></li><li>Búsqueda global (atajo «/»)</li><li>Acciones rápidas («Nuevo»)</li><li>Página no encontrada (404)</li></ul></div>
          </div></section>

        <section class="card" id="ia-nav" style="margin-bottom:var(--sp-5)"><div class="card-head"><h2>2. Diagrama de navegación</h2></div>
          <div class="table-wrap">${navDiagram()}</div>
          <p class="small muted">Las flechas continuas son el camino principal; las discontinuas, desvíos y excepciones (credenciales incorrectas, segundo factor, local cerrado). Desde cualquier pantalla con sesión se accede al menú principal, la búsqueda global, las acciones rápidas, las notificaciones y el menú de usuario.</p></section>

        <section class="card" id="ia-tax" style="margin-bottom:var(--sp-5)"><div class="card-head"><h2>3. Taxonomía y nomenclatura</h2></div>
          <div class="grid grid-2"><div><h3>Identificadores visibles</h3><div class="table-wrap"><table class="table"><thead><tr><th>Prefijo</th><th>Objeto</th><th>Ejemplo</th></tr></thead><tbody>${[['PV-', 'Pedido de venta', 'PV-264822'], ['R-', 'Ruta de reparto', 'R-01'], ['M-', 'Misión de preparación', 'M-3302'], ['DV-', 'Devolución', 'DV-5527'], ['L', 'Lote del proveedor', 'L2611-47'], ['OC-', 'Orden de compra', 'OC-88412'], ['EDI-', 'Mensaje del canal moderno', 'EDI-77121'], ['CL-', 'Cliente', 'CL-10021'], ['U-', 'Persona usuaria', 'U-1001'], ['AU-', 'Evento de auditoría', 'AU-90412'], ['SSCC', 'Unidad logística GS1', '(00) 0780…'], ['GDE', 'Guía de despacho electrónica', 'GDE 884133']].map((r) => `<tr>${r.map((c, i) => `<td class="${i !== 1 ? 'mono' : ''}">${esc(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div></div>
          <div><h3>Estados del pedido (proceso principal)</h3><ol class="timeline">${D.estadosPedido.map((e) => `<li class="done"><span class="dot"></span><div class="t-title">${L.estadoBadge(e)}</div></li>`).join('')}</ol></div></div>
          <h3 style="margin-top:var(--sp-5)">Términos del dominio (glosario de SD3, Anexo 3.A.14)</h3><dl class="desc-list">${[['OTIF', 'Pedidos completos y a tiempo sobre comprometidos (RNG-09).'], ['FEFO', 'Primero en vencer, primero en salir.'], ['POD', 'Prueba de entrega: firma, QR o foto.'], ['Fill rate', 'Unidades entregadas sobre unidades pedidas.'], ['Costo de servir', 'Costo logístico por entrega y por cliente.'], ['Local cerrado', 'Excepción más frecuente de la entrega (RNG-05).'], ['Retenido', 'Pedido o lote bloqueado hasta una decisión autorizada.'], ['Cross-docking', 'Transferencia directa sin almacenamiento.']].map(([a, b]) => `<dt>${a}</dt><dd>${b}</dd>`).join('')}</dl>
          <h3 style="margin-top:var(--sp-5)">Convenciones de nombres</h3><ul><li>Menús con sustantivos del negocio («Pedidos», «Rutas»); botones con verbo en infinitivo («Registrar devolución», «Aprobar ruta»).</li><li>Rutas en minúscula y en español, sin tildes: <code>/devoluciones/nueva</code>, <code>/clientes/:id</code>.</li><li>Cada módulo muestra su código de SD4 (M1–M12) para el perfil de evaluación.</li><li>Los estados usan siempre el mismo color: éxito verde, advertencia ámbar, error rojo, en curso naranja.</li></ul></section>

        <section class="card" id="ia-menu" style="margin-bottom:var(--sp-5)"><div class="card-head"><h2>4. Estructura de menús por perfil</h2></div>
          <p class="muted">Menú principal lateral (agrupado en ${L.nav.length} secciones), barra superior global y menús contextuales en filas de tablas (clic derecho, tecla de menú o botón «⋯»). Cada perfil ve solo lo que su rol permite (RF-15.04).</p>
          <div class="table-wrap"><table class="table"><caption class="sr-only">Menú visible por perfil</caption><thead><tr><th>Perfil</th><th>Interfaz</th>${L.nav.slice(1, 7).map((g) => `<th>${esc(g.group)}</th>`).join('')}</tr></thead><tbody>${D.profiles.map((p) => `<tr><td><strong>${esc(p.name.split(' ').slice(0, 2).join(' '))}</strong><div class="small muted">${esc(p.role.split(' ·')[0])}</div></td><td class="wrap small">${esc(p.iface)}</td>${L.nav.slice(1, 7).map((g) => { const its = g.items.filter((i) => p.all || p.menu.includes(i.path)); return `<td class="wrap small">${its.length ? its.map((i) => esc(i.label)).join('<br>') : '<span class="muted">—</span>'}</td>`; }).join('')}</tr>`).join('')}</tbody></table></div>
          <h3 style="margin-top:var(--sp-5)">Barra superior (todas las pantallas con sesión)</h3><div class="row">${['Menú (móvil)', 'Búsqueda global', 'Indicador de conectividad', 'Nuevo: acciones rápidas', 'Notificaciones', 'Modo claro u oscuro', 'Menú de usuario'].map((t) => `<span class="chip">${t}</span>`).join('')}</div></section>

        <section class="card" id="ia-jer" style="margin-bottom:var(--sp-5)"><div class="card-head"><h2>5. Jerarquía de la información</h2></div>
          <div class="grid grid-2"><div><h3>Niveles de navegación</h3><ol class="timeline">${[['Nivel 0 · Sitio público', 'Inicio público, catálogo, cobertura, contacto, ingreso y registro'], ['Nivel 1 · Inicio por perfil', 'Accesos principales, tablero configurable y tareas'], ['Nivel 2 · Módulo', 'Listado con indicadores, filtros, búsqueda y acciones masivas'], ['Nivel 3 · Detalle', 'Ficha, línea de tiempo, pestañas y acciones del registro'], ['Nivel 4 · Acción', 'Formulario, flujo de pasos, modal o confirmación']].map(([t, d], i) => `<li class="${i === 4 ? 'current' : 'done'}"><span class="dot"></span><div class="t-title">${t}</div><div class="t-meta">${d}</div></li>`).join('')}</ol></div>
          <div><h3>Orden dentro de cada pantalla</h3><ol class="list" style="counter-reset:a">${['Rastro de navegación (dónde estoy)', 'Título, contexto y acciones principales de la página', 'Alertas que exigen decisión', 'Indicadores resumen', 'Filtros y búsqueda', 'Contenido principal: tabla, ficha o flujo', 'Panel lateral: estado, línea de tiempo, bitácora'].map((t, i) => `<li><span class="avatar dark" style="width:28px;height:28px">${i + 1}</span><span class="grow">${t}</span></li>`).join('')}</ol></div></div></section>

        <section class="card" id="ia-3"><div class="card-head"><h2>6. Regla de tres interacciones (RT-25.01)</h2></div>
          <p class="muted">Funciones principales por perfil y su camino más corto desde el inicio.</p>
          <div class="table-wrap"><table class="table"><thead><tr><th>Perfil</th><th>Función principal</th><th>Camino</th><th class="right">Interacciones</th></tr></thead><tbody>${[['Preventista', 'Tomar un pedido sin señal', 'Inicio → «Tomar un pedido» → «Guardar sin conexión»', 2], ['Conductor', 'Registrar local cerrado', 'Inicio → «Iniciar mi ruta» → parada → «Local cerrado»', 3], ['Planificador', 'Aprobar el plan de mañana', 'Inicio → «Revisar ruta propuesta» → «Aprobar plan»', 3], ['Jefa de Calidad', 'Iniciar retiro sanitario', 'Inicio → «Simulacro de retiro» → «Iniciar retiro»', 2], ['Jefa de Bodega', 'Registrar recepción', '«Nuevo» → «Registrar recepción»', 2], ['Gerencia', 'Ver OTIF por ruta', 'Inicio → tarjeta OTIF', 1], ['Finanzas', 'Tipificar descuadre', 'Menú → Rendición → «⋯» de la fila', 3], ['Jefe de TI', 'Invitar persona', '«Nuevo» → «Invitar persona usuaria»', 2], ['Cliente', 'Hacer un pedido', 'Inicio → «Hacer un pedido»', 1], ['Empresa transportista', 'Confirmar conductor y vehículo', 'Inicio → «Asignar conductor y vehículo» → «Asignar» → «Confirmar»', 3], ['Proveedor', 'Ver la recepción de una orden', 'Inicio → «Órdenes y recepciones» → pestaña «Recepciones»', 2], ['Cualquier actor', 'Ingresar sin credenciales', 'Ingresar → elegir actor → «Ingresar como este perfil»', 2],['Todos', 'Encontrar cualquier registro', '«/» → escribir → Enter', 2]].map(([a, b, c, n]) => `<tr><td>${a}</td><td>${b}</td><td class="wrap small">${c}</td><td class="num right">${L.badge(String(n), n <= 3 ? 'success' : 'danger')}</td></tr>`).join('')}</tbody></table></div></section>`;
    },
    mount: (root) => {
      $('#ia-print', root).onclick = () => window.print();
      $$('[data-jump]', root).forEach((a) => (a.onclick = (e) => { e.preventDefault(); const t = document.getElementById(a.dataset.jump); t.scrollIntoView({ behavior: 'smooth' }); t.setAttribute('tabindex', '-1'); t.focus({ preventScroll: true }); }));
    }
  });

  function navDiagram() {
    const N = {
      pub: [40, 40, 'Inicio público'], cat: [40, 130, 'Catálogo'], reg: [40, 220, 'Registro (5 pasos)'], login: [250, 40, 'Ingresar (SSO)'], rec: [250, 130, 'Recuperar acceso'], mfa: [460, 40, 'Segundo factor'], wel: [460, 130, 'Bienvenida + recorrido'],
      home: [670, 85, 'Inicio por perfil'], board: [880, 20, 'Tablero'], flow: [880, 100, 'Flujo de pedido'], field: [880, 180, 'Terreno móvil'], mods: [880, 260, 'Módulos (M1–M12)'], list: [1090, 220, 'Listado'], det: [1090, 300, 'Detalle'], act: [880, 340, 'Acción / modal'], ia: [670, 300, 'Arquitectura y cumplimiento']
    };
    const E = [['pub', 'login'], ['pub', 'cat'], ['pub', 'reg'], ['login', 'mfa'], ['login', 'rec', 1], ['mfa', 'wel'], ['wel', 'home'], ['mfa', 'home'], ['login', 'home', 1], ['home', 'board'], ['home', 'flow'], ['home', 'field'], ['home', 'mods'], ['mods', 'list'], ['list', 'det'], ['det', 'act'], ['home', 'ia', 1], ['reg', 'login', 1]];
    const w = 170, h = 44;
    const box = ([x, y, t], k) => `<g><rect x="${x}" y="${y}" width="${w}" height="${h}" rx="10" fill="${k === 'home' ? 'var(--c-accent)' : 'var(--c-surface)'}" stroke="var(--c-ink)" stroke-width="1.5"/><text x="${x + w / 2}" y="${y + h / 2 + 5}" text-anchor="middle" style="font-size:13px;font-weight:600;fill:var(--c-ink)">${esc(t)}</text></g>`;
    const edge = ([a, b, dash]) => { const A = N[a], B = N[b]; const x1 = A[0] + w / 2, y1 = A[1] + h / 2, x2 = B[0] + w / 2, y2 = B[1] + h / 2; const dx = x2 - x1, dy = y2 - y1; const sx = Math.abs(dx) * h > Math.abs(dy) * w ? (w / 2) / Math.abs(dx) : (h / 2) / Math.abs(dy || 1); const ex = x2 - dx * sx, ey = y2 - dy * sx; return `<line x1="${x1 + dx * sx}" y1="${y1 + dy * sx}" x2="${ex}" y2="${ey}" stroke="var(--c-gray)" stroke-width="1.5" ${dash ? 'stroke-dasharray="5 4"' : ''} marker-end="url(#arr)"/>`; };
    return `<svg viewBox="0 0 1280 400" style="min-width:900px;width:100%;height:auto" role="img" aria-label="Diagrama de navegación: del inicio público al ingreso, segundo factor, bienvenida e inicio por perfil, y desde allí a tablero, flujo, terreno y módulos con listado, detalle y acción"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 10 5 0 10z" fill="var(--c-gray)"/></marker></defs>${E.map(edge).join('')}${Object.entries(N).map(([k, v]) => box(v, k)).join('')}</svg>`;
  }

  /* ---------- Sistema de diseño ---------- */
  const lum = (hex) => { const c = hex.replace('#', '').match(/../g).map((x) => parseInt(x, 16) / 255).map((v) => (v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4))); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; };
  const ratio = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((m, n) => n - m); return (x + 0.05) / (y + 0.05); };

  L.route('/sistema-diseno', {
    title: 'Sistema de diseño', parent: '/inicio', block: 'Documentación (RT-25.05)', module: 'Prototipo', rf: ['RT-25.05', 'RT-25.03', 'RT-25.04'], actors: ['Comisión evaluadora'],
    render: () => {
      const pal = [['Tinta', '#111111', 'Texto, encabezados, botón oscuro'], ['Gris', '#5F5F5F', 'Texto secundario, iconos'], ['Fondo', '#F4F4F4', 'Fondo de la aplicación'], ['Superficie', '#FFFFFF', 'Tarjetas, tablas, modales'], ['Naranja LafroX', '#E8641B', 'Acción principal, foco, serie principal']];
      const sem = [['Éxito', '#1E7A3C'], ['Advertencia', '#8A5A00'], ['Error', '#B3261E'], ['Información', '#1D5FA8']];
      return `<div class="page-head"><div class="titles"><span class="page-kicker">RT-25.05 · sistema de diseño</span><h1>Sistema de diseño LafroX</h1><p class="muted" style="margin:0">Tokens y componentes reutilizables, compartidos por portales y consolas (Angular/Tailwind) y apps Kotlin, según SD4 §4.1.4.</p></div></div>
        <section class="card" style="margin-bottom:var(--sp-5)"><div class="card-head"><h2>Paleta: cinco colores principales</h2><span class="small muted">Tomada de lafrox.cls</span></div>
          <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(170px,1fr))">${pal.map(([n, h, u]) => `<div><div style="height:88px;border-radius:10px;background:${h};border:1px solid var(--c-line-soft)"></div><strong style="display:block;margin-top:8px">${n}</strong><code>${h}</code><div class="small muted">${u}</div><div class="small">Sobre blanco ${ratio(h, '#FFFFFF').toFixed(1)}:1 · sobre tinta ${ratio(h, '#111111').toFixed(1)}:1</div></div>`).join('')}</div>
          ${L.alert('info', 'Regla de contraste', `El naranja (${ratio('#E8641B', '#FFFFFF').toFixed(1)}:1 sobre blanco) no se usa como texto; en botones lleva texto tinta (${ratio('#E8641B', '#111111').toFixed(1)}:1). Para texto de acento se usa la variante #A8440C (${ratio('#A8440C', '#FFFFFF').toFixed(1)}:1). Todo texto cumple WCAG 2.2 AA (4,5:1).`)}
          <h3 style="margin-top:var(--sp-5)">Colores semánticos de estado (no forman parte de la paleta principal)</h3><div class="row">${sem.map(([n, h]) => `<span class="badge" style="background:${h};color:#fff;border:0;padding:6px 12px">${n} · ${h} · ${ratio(h, '#FFFFFF').toFixed(1)}:1</span>`).join('')}</div></section>

        <div class="grid grid-2" style="margin-bottom:var(--sp-5)">
          <section class="card"><div class="card-head"><h2>Tipografía: dos familias</h2></div>
            <p style="font-size:var(--fs-4xl);font-weight:700;margin:0;line-height:1.1">Título 48</p><p style="font-size:var(--fs-2xl);font-weight:600;margin:0">Encabezado de página 28</p><p style="font-size:var(--fs-xl);font-weight:600;margin:0">Encabezado de sección 22</p><p style="font-size:var(--fs-lg);font-weight:600;margin:0">Encabezado de tarjeta 18</p><p style="margin:0">Texto de lectura 16 · Source Sans 3</p><p class="small muted" style="margin:0">Texto secundario 14</p><p class="mono" style="margin:8px 0 0">PV-264822 · SSCC 00780123 · IBM Plex Mono</p>
            <p class="small muted" style="margin-top:12px">Tamaño mínimo de texto 13 px; el usuario puede ampliarlo a 18 o 20 px base desde sus preferencias.</p></section>
          <section class="card"><div class="card-head"><h2>Retícula y espaciado</h2></div><p class="muted">Base de 8 px. Objetivos táctiles mínimos de 44 × 44 px.</p>${[4, 8, 12, 16, 24, 32, 48, 64].map((s) => `<div class="row" style="margin-bottom:6px"><code style="width:48px">${s}px</code><span style="display:inline-block;height:14px;width:${s * 3}px;background:var(--c-accent);border-radius:3px"></span></div>`).join('')}
            <h3>Puntos de quiebre</h3><div class="table-wrap"><table class="table"><tbody>${[['Teléfono', '375 × 812', 'Una columna, menú desplegable, modales desde abajo'], ['Tableta vertical', '768 × 1024', 'Dos columnas, menú desplegable'], ['Tableta horizontal', '1024 × 768', 'Menú lateral fijo'], ['Escritorio', '1366 × 768', 'Menú lateral de 240 px'], ['Escritorio amplio', '1920 × 1080', 'Contenido hasta 1.680 px']].map((r) => `<tr>${r.map((c) => `<td class="wrap">${c}</td>`).join('')}</tr>`).join('')}</tbody></table></div></section></div>

        <section class="card" style="margin-bottom:var(--sp-5)"><div class="card-head"><h2>Iconografía</h2><span class="small muted">${L.iconNames.length} iconos de trazo único sobre 24 px</span></div><div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(92px,1fr));gap:8px">${L.iconNames.map((n) => `<div style="text-align:center;padding:10px 4px;border:1px solid var(--c-line-soft);border-radius:8px">${icon(n, 'icon-lg')}<div class="small muted" style="font-size:11px;overflow-wrap:anywhere">${n}</div></div>`).join('')}</div></section>

        <section class="card" style="margin-bottom:var(--sp-5)"><div class="card-head"><h2>Botones y estados</h2></div>
          <div class="stack"><div class="btn-group"><button class="btn btn-primary">Primario</button><button class="btn btn-secondary">Secundario</button><button class="btn btn-tertiary">Terciario</button><button class="btn btn-dark">Oscuro</button><button class="btn btn-danger">Destructivo</button><button class="btn btn-primary" disabled>Deshabilitado</button><button class="btn btn-primary" id="ds-load">Con carga</button><button class="btn btn-secondary btn-icon" aria-label="Solo icono">${icon('edit')}</button></div>
          <p class="small muted" style="margin:0">Pase el puntero (posado) y presione (activo) sobre cada botón; con Tab se ve el foco.</p>
          <button class="fab" style="position:static;align-self:flex-start" type="button">${icon('plus')}Botón flotante</button></div></section>

        <div class="grid grid-2" style="margin-bottom:var(--sp-5)">
          <section class="card stack"><h2>Formularios</h2><div class="field"><label for="ds-1">Campo con validación (RUT)</label><input id="ds-1" class="input" placeholder="12.345.678-5"></div><div class="field combo"><label for="ds-2">Autocompletado</label><input id="ds-2" class="input" placeholder="Escriba «alm»"></div><div class="field"><label for="ds-3">Selector</label><select id="ds-3" class="select"><option>Opción 1</option><option>Opción 2</option></select></div><div class="field"><label for="ds-4">Fecha y hora</label><input id="ds-4" type="datetime-local" class="input" value="2026-11-14T09:00"></div><div class="options-row"><label class="check"><input type="checkbox" checked> Casilla</label><label class="radio"><input type="radio" name="ds-r" checked> Opción A</label><label class="radio"><input type="radio" name="ds-r"> Opción B</label><label class="switch"><input type="checkbox" checked> Interruptor</label></div><div class="dropzone" id="ds-dz">${icon('upload')}<span>Arrastrar y soltar archivos</span></div></section>
          <section class="card stack"><h2>Retroalimentación</h2>${L.alert('success', 'Éxito', 'La acción se completó.')}${L.alert('warning', 'Advertencia', 'Revise antes de continuar.')}${L.alert('danger', 'Error', 'No se pudo completar la acción.')}${L.alert('info', 'Información', 'Dato útil para la tarea.')}
            <div class="btn-group">${['success', 'error', 'warning', 'info'].map((t) => `<button class="btn btn-secondary btn-sm" data-toast="${t}">Aviso ${t === 'success' ? 'de éxito' : t === 'error' ? 'de error' : t === 'warning' ? 'de advertencia' : 'informativo'}</button>`).join('')}<button class="btn btn-secondary btn-sm" id="ds-modal">Modal</button><button class="btn btn-secondary btn-sm" id="ds-confirm">Confirmación crítica</button></div>
            <div class="card" style="box-shadow:none">${L.skeleton(3)}</div><div class="progress"><span style="width:62%"></span></div><div class="progress indeterminate"><span></span></div></section></div>

        <section class="card" style="margin-bottom:var(--sp-5)"><div class="card-head"><h2>Navegación y datos</h2></div>
          ${L.tabsHtml('dst', [{ id: 'a', label: 'Pestaña activa' }, { id: 'b', label: 'Otra pestaña', count: 3 }], 'a')}<div ${L.panelAttrs('dst', 'a', 'a')}><p>Contenido de la pestaña activa.</p></div><div ${L.panelAttrs('dst', 'b', 'a')}><p>Contenido de otra pestaña.</p></div>
          ${L.accordionHtml('Acordeón', '<p>Contenido plegable.</p>')}
          <div style="margin-top:var(--sp-4)">${L.stepperHtml(['Hecho', 'Actual', 'Pendiente'], 1)}</div>
          <div class="row"><span class="badge badge-success">Éxito</span><span class="badge badge-warning">Advertencia</span><span class="badge badge-danger">Error</span><span class="badge badge-info">Información</span><span class="badge badge-accent">En curso</span><span class="badge badge-dark">Oscuro</span><span class="chip" aria-pressed="true">Filtro activo</span>${L.tip('Información contextual emergente')}<div class="menu-wrap"><button type="button" class="btn btn-secondary btn-sm" id="ds-menu">Menú desplegable ${icon('chev-down', 'icon-sm')}</button></div></div></section>
        <section class="card">${L.empty('box', 'Estado vacío ilustrado', 'Cada listado sin datos explica por qué y ofrece la siguiente acción.', '<button class="btn btn-primary btn-sm" type="button">Acción sugerida</button>')}</section>`;
    },
    mount: (root) => {
      L.bindField($('#ds-1', root), ['rut'], { okMsg: 'RUT válido' });
      L.combobox($('#ds-2', root), () => D.clientes.map((c) => ({ label: c.nombre, meta: c.comuna })));
      L.dropzone($('#ds-dz', root), {});
      L.tabs($('.tabs', root));
      $$('[data-toast]', root).forEach((b) => (b.onclick = () => L.toast(b.textContent, 'Ejemplo de notificación emergente.', b.dataset.toast)));
      $('#ds-load', root).onclick = (e) => L.busy(e.currentTarget, () => L.toast('Acción completada', '', 'success'), 1200);
      $('#ds-modal', root).onclick = () => L.modal({ title: 'Ventana modal', body: '<p>El foco queda atrapado dentro, Esc la cierra y el foco vuelve al botón de origen.</p>', actions: [{ label: 'Cancelar' }, { label: 'Aceptar', cls: 'btn-primary' }] });
      $('#ds-confirm', root).onclick = () => L.confirm({ title: '¿Eliminar el registro?', message: 'Esta acción no se puede deshacer.', confirmLabel: 'Eliminar', danger: true, requireText: 'ELIMINAR' });
      L.menu($('#ds-menu', root), [{ label: 'Editar', icon: 'edit', onClick: () => {} }, { label: 'Duplicar', icon: 'copy', onClick: () => {} }, { sep: true }, { label: 'Eliminar', icon: 'trash', danger: true, onClick: () => {} }], { align: 'left' });
    }
  });

  /* ---------- Cumplimiento y trazabilidad ---------- */
  const COMPONENTS = [
    ['Navegación', 'Menú principal', '/inicio'], ['Navegación', 'Menú secundario contextual', '/pedidos'], ['Navegación', 'Rastro de navegación', '/clientes'], ['Navegación', 'Paginación', '/clientes'], ['Navegación', 'Pestañas', '/clientes/CL-10021'], ['Navegación', 'Acordeones', '/admin/parametros'], ['Navegación', 'Navegación por pasos', '/registro'], ['Navegación', 'Menú de acciones rápidas', '/inicio'],
    ['Formularios', 'Validación en tiempo real', '/registro'], ['Formularios', 'Selectores y desplegables', '/devoluciones/nueva'], ['Formularios', 'Casillas y botones de opción', '/devoluciones/nueva'], ['Formularios', 'Fecha y hora', '/admin/auditoria'], ['Formularios', 'Carga de archivos con arrastrar y soltar', '/registro'], ['Formularios', 'Autocompletado', '/devoluciones/nueva'], ['Formularios', 'Formularios de varios pasos', '/registro'],
    ['Visualización', 'Tablas con orden y filtro', '/pedidos'], ['Visualización', 'Barras, líneas y circular', '/analitica'], ['Visualización', 'Tarjetas de información', '/inicio'], ['Visualización', 'Líneas de tiempo', '/flujo'], ['Visualización', 'Indicadores de progreso', '/rutas'], ['Visualización', 'Distintivos y etiquetas', '/pedidos'], ['Visualización', 'Información contextual emergente', '/analitica'],
    ['Retroalimentación', 'Éxito, error, advertencia e información', '/sistema-diseno'], ['Retroalimentación', 'Modales y diálogos', '/admin/usuarios'], ['Retroalimentación', 'Notificaciones emergentes', '/flujo'], ['Retroalimentación', 'Esqueletos de carga', '/analitica'], ['Retroalimentación', 'Indicadores de progreso', '/calidad/retiro'], ['Retroalimentación', 'Estados vacíos ilustrados', '/rutas'],
    ['Acción', 'Botones primarios, secundarios y terciarios', '/sistema-diseno'], ['Acción', 'Botón de acción flotante', '/terreno/preventa'], ['Acción', 'Acciones en línea', '/flujo'], ['Acción', 'Menús contextuales', '/pedidos'], ['Acción', 'Acciones masivas', '/devoluciones'], ['Acción', 'Confirmación de acciones críticas', '/admin/usuarios']
  ];
  const RT = [
    ['RT-25.01', 'Navegación intuitiva, máximo tres interacciones', '/arquitectura', 'Tabla de caminos por perfil, accesos principales en el inicio, búsqueda global y acciones rápidas.'],
    ['RT-25.02', 'Retroalimentación, carga y errores', '/sistema-diseno', 'Avisos, esqueletos, botones con carga, validación en línea y errores con instrucciones.'],
    ['RT-25.03', 'WCAG 2.2 AA', '/sistema-diseno', 'Contraste verificado, 44 × 44 px, teclado completo, foco visible, saltar al contenido, etiquetas ARIA y textos alternativos.'],
    ['RT-25.04', 'Diseño responsivo', '/sistema-diseno', 'Puntos de quiebre 375 / 768 / 1024 / 1366 / 1920; menú desplegable bajo 1024 px.'],
    ['RT-25.05', 'Sistema de diseño documentado', '/sistema-diseno', '5 colores, 2 familias, iconografía, retícula de 8 px y componentes vivos.'],
    ['RT-25.06', 'Enlace navegable sin instalación', '/', 'HTML, CSS y JavaScript estáticos, sin complementos ni compilación.'],
    ['RT-25.07', 'Acceso por seis meses', '/', 'Publicación estática sin dependencias externas de ejecución (solo tipografías con respaldo del sistema).'],
    ['RT-25.08', 'Navegación completa e interactividad', '/flujo', 'Ingreso de datos, transiciones, posado y activo, carga de archivos, desplegables y validaciones simuladas.'],
    ['RT-25.09', 'Arquitectura de información', '/arquitectura', 'Mapa del sitio, diagrama de navegación, taxonomía, menús y jerarquía.'],
    ['RT-25.10', 'Exportación para revisión sin conexión (deseable)', '/cumplimiento', 'La carpeta funciona abriendo index.html sin servidor; se entrega en .zip.']
  ];
  L.compliance = { COMPONENTS, RT };

  L.route('/cumplimiento', {
    title: 'Cumplimiento y trazabilidad', parent: '/inicio', block: 'Documentación', module: 'Prototipo', rf: ['RT-25.01', 'RT-25.10'], actors: ['Comisión evaluadora'],
    render: () => {
      const blocks = ['Portal principal', 'Autenticación e incorporación', 'Proceso operacional principal', 'Proceso operacional secundario', 'Perfil de terreno', 'Gestión de terceros', 'Tablero analítico', 'Administración', 'Módulo adicional 1', 'Módulo adicional 2'];
      const routes = L.routes.filter((r) => r.path !== '*');
      const mods = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12'];
      return `<div class="page-head"><div class="titles"><span class="page-kicker">Bases cap. 25 · SD3 · SD4</span><h1>Cumplimiento y trazabilidad</h1><p class="muted" style="margin:0">Dónde se demuestra cada exigencia del capítulo 25 y a qué requerimiento (SD3) y módulo (SD4) responde cada pantalla.</p></div><div class="actions"><button type="button" class="btn btn-primary" id="cm-exp">${icon('download')}Exportar matriz CSV</button></div></div>
        ${L.tabsHtml('cm', [{ id: 'alc', label: 'Alcance 25.2' }, { id: 'rt', label: 'RT-25.01 a 25.10' }, { id: 'comp', label: 'Componentes 25.4' }, { id: 'traz', label: 'Trazabilidad SD3 / SD4', count: routes.length }], 'alc')}
        <div ${L.panelAttrs('cm', 'alc', 'alc')}><div class="card card-flush"><div class="table-wrap"><table class="table"><thead><tr><th>Bloque del numeral 25.2</th><th>Pantallas que lo demuestran</th><th>Estado</th></tr></thead><tbody>${blocks.map((b) => { const rs = routes.filter((r) => r.block === b); return `<tr><td class="wrap"><strong>${b === 'Módulo adicional 1' ? 'Módulo adicional 1: M9 Calidad y trazabilidad' : b === 'Módulo adicional 2' ? 'Módulo adicional 2: M12 Telemetría y frío' : b}</strong></td><td class="wrap">${rs.map((r) => `<a href="#${r.path.includes(':') ? (r.path.startsWith('/clientes') ? '/clientes/CL-10021' : r.path.startsWith('/pedidos') ? '/pedidos/' + D.pedidos[3].id : r.path.startsWith('/devoluciones') ? '/devoluciones/' + D.devoluciones[2].id : r.path.startsWith('/rutas') ? '/rutas/R-01' : r.path.startsWith('/calidad') ? '/calidad/lotes/L2611-52' : r.path.startsWith('/analitica/:kpi/') ? '/analitica/otif/ruta/R-01' : '/analitica/otif') : r.path}">${esc(routeLabel(r))}</a>`).join(' · ')}</td><td>${L.badge(rs.length ? 'Cubierto' : 'Pendiente', rs.length ? 'success' : 'danger')}</td></tr>`; }).join('')}</tbody></table></div></div></div>
        <div ${L.panelAttrs('cm', 'rt', 'alc')}><div class="card card-flush"><div class="table-wrap"><table class="table"><thead><tr><th>Código</th><th>Requisito</th><th>Evidencia</th><th>Dónde</th></tr></thead><tbody>${RT.map(([c, t, p, e]) => `<tr><td class="mono">${c}</td><td class="wrap">${t}</td><td class="wrap small">${e}</td><td><a class="btn btn-tertiary btn-sm" href="#${p}">Ver${icon('chev-right', 'icon-sm')}</a></td></tr>`).join('')}</tbody></table></div></div></div>
        <div ${L.panelAttrs('cm', 'comp', 'alc')}><div class="card card-flush"><div class="table-wrap"><table class="table"><thead><tr><th>Categoría</th><th>Componente</th><th>Dónde se ve</th></tr></thead><tbody>${COMPONENTS.map(([a, b, p]) => `<tr><td>${a}</td><td>${b}</td><td><a href="#${p}">${esc(p)}</a></td></tr>`).join('')}</tbody></table></div></div></div>
        <div ${L.panelAttrs('cm', 'traz', 'alc')}>
          <div class="card" style="margin-bottom:var(--sp-4)"><h2>Cobertura de los 12 módulos de SD4</h2><div class="row">${mods.map((m) => { const n = routes.filter((r) => new RegExp(m + '(?!\\d)').test(r.module)).length; return `<span class="badge ${n ? 'badge-success' : 'badge-danger'}">${m} · ${n} pantalla${n === 1 ? '' : 's'}</span>`; }).join('')}</div><p class="small muted" style="margin-top:8px">Fuentes: SD3 Anexo 3.A (RF del caso, BTT y propios; actores 3.A.12a; reglas 3.A.10) y SD4 Anexo 4-D (matriz de los doce módulos) y Anexo 4-J (funciones sin conexión).</p></div>
          <div class="card card-flush"><div class="table-wrap"><table class="table"><caption class="sr-only">Matriz pantalla, módulo, requerimientos y actores</caption><thead><tr><th>Pantalla</th><th>Ruta</th><th>Bloque 25.2</th><th>Módulo SD4</th><th>RF / RNF SD3</th><th>Actores</th></tr></thead><tbody>${routes.map((r) => `<tr><td class="wrap"><strong>${esc(routeLabel(r))}</strong></td><td class="mono small">${esc(r.path)}</td><td class="wrap small">${esc(r.block || '')}</td><td class="wrap small">${esc(r.module || '')}</td><td class="wrap small mono">${esc((r.rf || []).join(', '))}</td><td class="wrap small">${esc((r.actors || []).join(', '))}</td></tr>`).join('')}</tbody></table></div></div></div>`;
    },
    mount: (root) => {
      L.tabs($('.tabs', root));
      $('#cm-exp', root).onclick = () => { L.download('trazabilidad_prototipo.csv', L.toCSV(L.routes.filter((r) => r.path !== '*'), [{ label: 'Pantalla', val: routeLabel }, { label: 'Ruta', key: 'path' }, { label: 'Bloque 25.2', key: 'block' }, { label: 'Módulo SD4', key: 'module' }, { label: 'RF/RNF SD3', val: (r) => (r.rf || []).join(', ') }, { label: 'Actores', val: (r) => (r.actors || []).join(', ') }])); L.toast('Matriz exportada', '', 'success'); };
    }
  });

  // Las páginas de documentación son públicas cuando no hay sesión
  ['/arquitectura', '/sistema-diseno', '/cumplimiento'].forEach((p) => {
    const r = L.routes.find((x) => x.path === p);
    Object.defineProperty(r, 'layout', { get: lay, configurable: true });
  });
})(window.LFX);
