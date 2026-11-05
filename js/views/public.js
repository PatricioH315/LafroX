/* Portal público (RF-12.14, RF-17.13): inicio, catálogo sin precios ni stock, cobertura y contacto. */
(function (L) {
  const { esc, icon, data: D } = L;

  L.route('/', {
    title: 'Inicio público', layout: 'public', block: 'Portal principal', module: 'Portal público', rf: ['RF-12.14', 'RF-17.13'], actors: ['Visitante', 'Cliente'],
    render: () => `
      <section class="grid" style="grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);align-items:center;gap:var(--sp-7);padding:var(--sp-6) 0" id="hero">
        <div>
          <span class="page-kicker">${icon('truck', 'icon-sm')}Distribución mayorista del Maule al sur</span>
          <h1 style="font-size:var(--fs-4xl);letter-spacing:-0.01em;margin-bottom:var(--sp-4)">Su almacén abastecido, a la hora que prometimos.</h1>
          <p class="muted" style="font-size:var(--fs-lg);max-width:560px">Más de 8.400 productos para 14.200 almacenes, minimarkets, restaurantes y supermercados entre O'Higgins y La Araucanía. Haga su pedido, siga su entrega y descargue sus documentos desde un solo lugar.</p>
          <div class="btn-group" style="margin-top:var(--sp-5)">
            <a class="btn btn-primary big-btn" href="#/registro">${icon('store')}Quiero ser cliente</a>
            <a class="btn btn-secondary big-btn" href="#/catalogo">Ver catálogo</a>
          </div>
          <dl class="stat-list" style="margin-top:var(--sp-6)">
            <div><dt>Entregas diarias</dt><dd class="num" style="font-size:var(--fs-xl)">1.400</dd></div>
            <div><dt>Productos</dt><dd class="num" style="font-size:var(--fs-xl)">8.400</dd></div>
            <div><dt>Centros y plataformas</dt><dd class="num" style="font-size:var(--fs-xl)">5</dd></div>
          </dl>
        </div>
        <div class="card" style="padding:var(--sp-5);position:relative;overflow:hidden">
          <div class="row-between"><strong>Seguimiento de su entrega</strong>${L.badge('En ruta', 'accent')}</div>
          <p class="small muted" style="margin:4px 0 16px">Pedido PV-264790 · Almacén Doña Rosa</p>
          <ol class="timeline">
            <li class="done"><span class="dot"></span><div class="t-title">Pedido confirmado</div><div class="t-meta">Ayer 16:42 · stock y crédito validados</div></li>
            <li class="done"><span class="dot"></span><div class="t-title">Preparado y cargado</div><div class="t-meta">Hoy 05:10 · guía electrónica 884120</div></li>
            <li class="current"><span class="dot"></span><div class="t-title">Llega entre 09:00 y 09:30</div><div class="t-meta">Camión KXTR-21 · 2 entregas antes</div></li>
            <li><span class="dot"></span><div class="t-title pending">Entregado con firma digital</div></li>
          </ol>
          <div class="alert alert-info" style="margin-top:8px">${icon('phone')}<div>Le avisamos por SMS con una ventana de 30 minutos.</div></div>
        </div>
      </section>
      <section style="margin-top:var(--sp-7)">
        <h2>Lo que puede hacer con Puelche</h2>
        <div class="grid grid-3" style="margin-top:var(--sp-4)">
          ${[['cart', 'Pedir cuando quiera', 'Con su preventista o desde el portal, aun sin señal: el pedido se envía al recuperar conexión.'], ['clock', 'Saber cuándo llega', 'Ventana de 30 minutos por SMS y seguimiento en línea de su camión.'], ['file', 'Sus documentos al día', 'Facturas, guías y notas de crédito descargables, con su estado de cuenta.'], ['crate', 'Control de envases', 'Su saldo de canastillos y pallets actualizado en cada entrega.'], ['snow', 'Cadena de frío demostrable', 'Cada lote refrigerado viaja con su historia de temperatura.'], ['shield', 'Retiro sanitario en horas', 'Si un proveedor retira un lote, le avisamos el mismo día.']].map(([i, t, d]) => `<div class="card"><span class="avatar" style="border-radius:10px">${icon(i)}</span><h3 style="margin-top:12px">${t}</h3><p class="muted" style="margin:0">${d}</p></div>`).join('')}
        </div>
      </section>
      <section class="card card-accent" style="margin-top:var(--sp-7);display:flex;gap:var(--sp-5);align-items:center;flex-wrap:wrap">
        <div style="flex:1 1 320px"><h2 style="margin-bottom:4px">¿Ya es cliente o trabaja en Puelche?</h2><p class="muted" style="margin:0">Use el mismo acceso para el portal de clientes, las consolas y las aplicaciones de terreno.</p></div>
        <a class="btn btn-dark big-btn" href="#/ingresar">${icon('lock')}Ingresar a la plataforma</a>
      </section>`,
    mount: (root) => {
      if (innerWidth < 1024) { const h = root.querySelector('#hero'); if (h) h.style.gridTemplateColumns = 'minmax(0,1fr)'; }
    }
  });

  L.route('/catalogo', {
    title: 'Catálogo', layout: 'public', parent: '/', block: 'Portal principal', module: 'Portal público', rf: ['RF-12.14'], actors: ['Visitante'],
    render: () => {
      const cats = [...new Set(D.productos.map((p) => p.categoria))];
      return `<div class="page-head"><div class="titles"><span class="page-kicker">Catálogo público</span><h1>Nuestros productos</h1><p class="muted" style="margin:0">Catálogo vigente sin precios ni stock. Para comprar, ingrese como cliente.</p></div></div>
        <div class="row" style="margin-bottom:var(--sp-4)" role="group" aria-label="Filtrar por categoría">${['Todas', ...cats].map((c, i) => `<button type="button" class="chip" aria-pressed="${i === 0}" data-cat="${esc(c)}">${esc(c)}</button>`).join('')}</div>
        <div class="grid grid-auto" id="cat-grid"></div>`;
    },
    mount: (root) => {
      const grid = root.querySelector('#cat-grid');
      const draw = (cat) => {
        const list = D.productos.filter((p) => cat === 'Todas' || p.categoria === cat);
        grid.innerHTML = list.map((p) => `<article class="card"><div class="row-between"><span class="badge plain">${esc(p.categoria)}</span>${p.temp !== 'Seco' ? `<span class="badge badge-info">${icon('snow', 'icon-sm')}${esc(p.temp)}</span>` : ''}</div><h3 style="margin:12px 0 4px">${esc(p.nombre)}</h3><p class="small muted mono" style="margin:0">GTIN ${esc(p.gtin)}</p></article>`).join('');
      };
      root.querySelectorAll('[data-cat]').forEach((b) => (b.onclick = () => { root.querySelectorAll('[data-cat]').forEach((x) => x.setAttribute('aria-pressed', x === b)); draw(b.dataset.cat); L.announce(`Mostrando ${b.dataset.cat}`); }));
      draw('Todas');
    }
  });

  L.route('/cobertura', {
    title: 'Cobertura', layout: 'public', parent: '/', block: 'Portal principal', module: 'Portal público', rf: ['RF-17.13'], actors: ['Visitante'],
    render: () => `<div class="page-head"><div class="titles"><span class="page-kicker">Red logística</span><h1>Cobertura y centros</h1></div></div>
      <div class="grid grid-2">${D.sitios.map((s) => `<div class="card"><div class="row-between"><h3 style="margin:0">${esc(s.nombre)}</h3>${L.badge(s.tipo, s.tipo.startsWith('Centro') ? 'dark' : '')}</div><p class="muted" style="margin:8px 0 0">${s.tipo.startsWith('Centro') ? 'Almacenamiento seco, refrigerado y congelado; despacho a su zona.' : 'Transferencia directa desde CD a camiones de reparto local.'}</p></div>`).join('')}</div>`
  });

  L.route('/contacto', {
    title: 'Contacto', layout: 'public', parent: '/', block: 'Portal principal', module: 'Portal público', rf: ['RF-17.13'], actors: ['Visitante'],
    render: () => `<div class="auth-wrap"><form class="card auth-card wide" id="ct" novalidate>
      <h1>Contáctenos</h1><p class="muted">Respondemos dentro de un día hábil.</p>
      <div class="form-grid">
        <div class="field"><label for="ct-n">Nombre <span class="req" aria-hidden="true">*</span></label><input id="ct-n" class="input" autocomplete="name" required></div>
        <div class="field"><label for="ct-e">Correo electrónico <span class="req" aria-hidden="true">*</span></label><input id="ct-e" class="input" type="email" autocomplete="email" required></div>
        <div class="field full"><label for="ct-t">Motivo</label><select id="ct-t" class="select"><option>Quiero ser cliente</option><option>Consulta por una entrega</option><option>Proveedores</option><option>Otro</option></select></div>
        <div class="field full"><label for="ct-m">Mensaje <span class="req" aria-hidden="true">*</span></label><textarea id="ct-m" class="textarea" required></textarea><span class="hint" id="ct-c">0 de 500 caracteres</span></div>
      </div>
      <div class="row" style="margin-top:var(--sp-4)"><button class="btn btn-primary" type="submit">${icon('send')}Enviar mensaje</button></div>
    </form></div>`,
    mount: (root) => {
      const f = root.querySelector('#ct');
      L.bindField(f.querySelector('#ct-n'), ['required']);
      L.bindField(f.querySelector('#ct-e'), ['email']);
      const m = f.querySelector('#ct-m');
      L.bindField(m, ['required', (v) => (v.length > 500 ? 'El mensaje supera los 500 caracteres.' : '')]);
      m.addEventListener('input', () => (f.querySelector('#ct-c').textContent = `${m.value.length} de 500 caracteres`));
      f.onsubmit = (e) => { e.preventDefault(); if (!L.validateAll(f)) { L.toast('Revise el formulario', 'Hay campos con errores.', 'error'); return; } L.busy(f.querySelector('[type=submit]'), () => { f.innerHTML = L.empty('done', 'Mensaje enviado', 'Le responderemos al correo indicado dentro de un día hábil.', '<a class="btn btn-secondary" href="#/">Volver al inicio</a>'); }); };
    }
  });

  L.route('*', {
    title: 'Página no encontrada', layout: 'public', block: 'Transversal', module: 'Transversal', rf: [], actors: ['Todos'],
    render: () => L.empty('search', 'No encontramos esta página', 'Puede que el enlace esté mal escrito o que la pantalla haya cambiado de lugar. Use el menú o vuelva al inicio.', `<div class="btn-group"><a class="btn btn-primary" href="#/${L.session() ? 'inicio' : ''}">Volver al inicio</a></div>`)
  });
})(window.LFX);
