/* Utilidades de interfaz: avisos, modales, validación, carga de archivos,
   menús, pestañas, acordeones, autocompletado, tablas y recorrido guiado. */
(function (L) {
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  L.$ = $;
  L.$$ = $$;

  L.esc = (v) => String(v ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  // Registro de consultas a información sensible, con finalidad (RNF-09.03)
  L.logConsulta = (entidad, detalle, finalidad) => { const me = L.me?.(); if (!me) return; L.store.set('audit.consultas', [{ id: `AU-C${Date.now().toString().slice(-6)}`, fecha: `2026-11-13T${String(new Date().getHours()).padStart(2, '0')}:${String(new Date().getMinutes()).padStart(2, '0')}:00`, persona: me.name, operacion: 'Consulta', entidad, detalle: `${detalle} · finalidad: ${finalidad}`, ip: '10.20.1.15', origen: 'Consola web' }, ...L.store.get('audit.consultas', [])].slice(0, 50)); };
  // Operational events (create, modify, exceptions) go to the same audit log the Auditoría screen reads (RF-17.04)
  L.logAudit = (operacion, entidad, detalle, origen = 'Consola web', antes = null, despues = null) => { const me = L.me?.(); if (!me) return; const now = new Date(); L.store.set('audit.consultas', [{ id: `AU-E${now.getTime().toString().slice(-6)}`, fecha: `2026-11-13T${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}:00`, persona: me.name, operacion, entidad, detalle, antes, despues, ip: '10.20.1.15', origen }, ...L.store.get('audit.consultas', [])].slice(0, 50)); };
  // Business parameter value by id (admin › Parámetros)
  L.param = (id) => L.data?.parametros?.flatMap((g) => g.items).find((x) => x.id === id)?.valor;
  L.uid = (p = 'id') => `${p}-${Math.random().toString(36).slice(2, 8)}`;
  L.sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  // Formatos chilenos
  const nf = new Intl.NumberFormat('es-CL');
  L.fmt = {
    n: (v, d = 0) => new Intl.NumberFormat('es-CL', { minimumFractionDigits: d, maximumFractionDigits: d }).format(v),
    clp: (v) => '$' + nf.format(Math.round(v)),
    pct: (v, d = 1) => new Intl.NumberFormat('es-CL', { minimumFractionDigits: d, maximumFractionDigits: d }).format(v) + ' %',
    date: (d) => new Date(d).toLocaleDateString('es-CL', { day: '2-digit', month: '2-digit', year: 'numeric' }),
    dateShort: (d) => new Date(d).toLocaleDateString('es-CL', { day: '2-digit', month: 'short' }),
    time: (d) => new Date(d).toLocaleTimeString('es-CL', { hour: '2-digit', minute: '2-digit' }),
    dt: (d) => `${L.fmt.date(d)} ${L.fmt.time(d)}`
  };

  // Estado global efímero: lo que se ingresa no persiste (25.6 no lo exige).
  const store = {
    get(k, def) { try { const v = sessionStorage.getItem('lfx.' + k); return v == null ? def : JSON.parse(v); } catch (e) { return def; } },
    set(k, v) { try { sessionStorage.setItem('lfx.' + k, JSON.stringify(v)); } catch (e) { /* almacenamiento no disponible */ } },
    pref(k, def) { try { const v = localStorage.getItem('lfx.pref.' + k); return v == null ? def : v; } catch (e) { return def; } },
    setPref(k, v) { try { localStorage.setItem('lfx.pref.' + k, v); } catch (e) { /* almacenamiento no disponible */ } }
  };
  L.store = store;

  // Limpieza al salir de una vista
  let leaveFns = [];
  L.onLeave = (fn) => leaveFns.push(fn);
  L.runLeave = () => { leaveFns.forEach((f) => { try { f(); } catch (e) { console.error(e); } }); leaveFns = []; };
  L.interval = (fn, ms) => { const id = setInterval(fn, ms); L.onLeave(() => clearInterval(id)); return id; };
  L.timeout = (fn, ms) => { const id = setTimeout(fn, ms); L.onLeave(() => clearTimeout(id)); return id; };

  /* ---------- Avisos emergentes ---------- */
  const ICON_BY = { success: 'check-circle', error: 'alert-circle', warning: 'alert', info: 'info' };
  L.toast = (title, msg = '', type = 'success', opts = {}) => {
    const region = $('#toasts');
    const el = document.createElement('div');
    el.className = `toast toast-${type}`;
    el.setAttribute('role', type === 'error' ? 'alert' : 'status');
    el.innerHTML = `${L.icon(ICON_BY[type])}<div class="t-body"><strong>${L.esc(title)}</strong>${msg ? L.esc(msg) : ''}</div>
      ${opts.action ? `<button type="button" class="t-action">${L.esc(opts.action)}</button>` : ''}
      <button type="button" aria-label="Cerrar aviso">${L.icon('x', 'icon-sm')}</button>`;
    const close = () => { el.classList.add('out'); setTimeout(() => el.remove(), 220); };
    el.querySelector('button[aria-label]').onclick = close;
    if (opts.action) el.querySelector('.t-action').onclick = () => { opts.onAction?.(); close(); };
    region.appendChild(el);
    if (opts.duration || (type !== 'error' && !opts.action)) setTimeout(close, opts.duration || 5200);
  };

  /* ---------- Modales y diálogos ---------- */
  L.modal = ({ title, body, actions = [], size = '', icon = '', onOpen, dismissible = true }) => {
    const opener = document.activeElement;
    const id = L.uid('dlg');
    const back = document.createElement('div');
    back.className = 'modal-backdrop';
    back.innerHTML = `<div class="modal ${size}" role="dialog" aria-modal="true" aria-labelledby="${id}-t">
      <div class="modal-head">
        ${icon ? `<span class="modal-icon ${icon.split(':')[0]}">${L.icon(icon.split(':')[1])}</span>` : ''}
        <h2 id="${id}-t">${L.esc(title)}</h2>
        ${dismissible ? `<button type="button" class="btn btn-tertiary btn-icon" data-close aria-label="Cerrar">${L.icon('x')}</button>` : ''}
      </div>
      <div class="modal-body">${body}</div>
      ${actions.length ? `<div class="modal-foot">${actions.map((a, i) => `<button type="button" class="btn ${a.cls || 'btn-secondary'}" data-act="${i}">${a.icon ? L.icon(a.icon) : ''}${L.esc(a.label)}</button>`).join('')}</div>` : ''}
    </div>`;
    document.body.appendChild(back);
    document.body.style.overflow = 'hidden';
    const dlg = back.firstElementChild;
    const close = (val) => {
      back.remove();
      document.removeEventListener('keydown', onKey, true);
      document.removeEventListener('lfx:session-expired', onExpire);
      if (!$('.modal-backdrop')) document.body.style.overflow = '';
      if (opener && opener.focus) opener.focus();
      api.resolve?.(val);
    };
    const onKey = (e) => {
      if (e.key === 'Escape' && dismissible) { e.stopPropagation(); close(null); }
      if (e.key === 'Tab') trapFocus(e, dlg);
    };
    const onExpire = () => close(null);
    document.addEventListener('lfx:session-expired', onExpire);
    document.addEventListener('keydown', onKey, true);
    back.addEventListener('mousedown', (e) => { if (e.target === back && dismissible) close(null); });
    $$('[data-close]', dlg).forEach((b) => (b.onclick = () => close(null)));
    const api = { el: dlg, close };
    actions.forEach((a, i) => {
      $(`[data-act="${i}"]`, dlg).onclick = async (e) => {
        if (a.onClick) {
          const r = await a.onClick(api, e.currentTarget);
          if (r === false) return;
          close(r === undefined ? a.value ?? i : r);
        } else close(a.value ?? i);
      };
    });
    onOpen?.(dlg, api);
    const first = $('[autofocus]', dlg) || $('input, select, textarea, .modal-foot .btn-primary, .modal-foot .btn-danger, .modal-foot .btn', dlg);
    setTimeout(() => first?.focus(), 30);
    api.promise = new Promise((res) => (api.resolve = res));
    return api;
  };

  function trapFocus(e, root) {
    const f = $$('a[href], button:not([disabled]), input:not([disabled]), select, textarea, [tabindex]:not([tabindex="-1"])', root).filter((x) => x.offsetParent !== null);
    if (!f.length) return;
    const first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }

  // Confirmación de acciones críticas
  L.confirm = ({ title, message, confirmLabel = 'Confirmar', danger = false, requireText = '' }) => {
    const m = L.modal({
      title,
      icon: danger ? 'danger:alert' : 'warning:alert',
      body: `<p>${message}</p>${requireText ? `<div class="field"><label for="cf-txt">Para confirmar, escriba <strong class="mono">${L.esc(requireText)}</strong></label><input id="cf-txt" class="input" autocomplete="off"></div>` : ''}`,
      actions: [
        { label: 'Cancelar', cls: 'btn-secondary', value: false },
        { label: confirmLabel, cls: danger ? 'btn-danger' : 'btn-primary', value: true }
      ],
      onOpen(dlg) {
        if (!requireText) return;
        const btn = $('.modal-foot .btn:last-child', dlg);
        const inp = $('#cf-txt', dlg);
        btn.disabled = true;
        inp.oninput = () => (btn.disabled = inp.value.trim().toUpperCase() !== requireText.toUpperCase());
      }
    });
    return m.promise;
  };

  /* ---------- Validación en tiempo real ---------- */
  L.rut = {
    clean: (r) => String(r).replace(/[^0-9kK]/g, '').toUpperCase(),
    dv(num) {
      let s = 0, m = 2;
      for (let i = num.length - 1; i >= 0; i--) { s += Number(num[i]) * m; m = m === 7 ? 2 : m + 1; }
      const r = 11 - (s % 11);
      return r === 11 ? '0' : r === 10 ? 'K' : String(r);
    },
    valid(r) {
      const c = L.rut.clean(r);
      if (c.length < 8) return false;
      return L.rut.dv(c.slice(0, -1)) === c.slice(-1);
    },
    format(r) {
      const c = L.rut.clean(r);
      if (c.length < 2) return c;
      const body = c.slice(0, -1).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
      return `${body}-${c.slice(-1)}`;
    }
  };

  L.validators = {
    required: (v) => (String(v).trim() ? '' : 'Este campo es obligatorio.'),
    email: (v) => (!v ? 'Ingrese un correo electrónico.' : /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v) ? '' : 'El correo no tiene un formato válido, por ejemplo nombre@empresa.cl.'),
    rut: (v) => (!v ? 'Ingrese el RUT.' : L.rut.valid(v) ? '' : 'El dígito verificador no corresponde. Revise el RUT.'),
    phone: (v) => (/^\+?56\s?9\s?\d{4}\s?\d{4}$/.test(String(v).replace(/[-.]/g, '')) ? '' : 'Use el formato +56 9 1234 5678.'),
    password: (v) => (String(v).length >= 10 && /[A-Z]/.test(v) && /\d/.test(v) ? '' : 'Mínimo 10 caracteres, una mayúscula y un número.'),
    positive: (v) => (Number(v) > 0 ? '' : 'Ingrese un valor mayor que cero.'),
    lot: (v) => (/^[A-Z0-9-]{4,}$/i.test(String(v).trim()) ? '' : 'Lote requerido para SKU con trazabilidad obligatoria.')
  };

  // Enlaza validación a un campo .field. rules: lista de nombres o funciones.
  L.bindField = (input, rules, { okMsg = '', onValid } = {}) => {
    const field = input.closest('.field');
    let msg = field.querySelector('.field-msg.error');
    if (!msg) {
      msg = document.createElement('div');
      msg.className = 'field-msg error';
      msg.id = L.uid('err');
      msg.setAttribute('aria-live', 'polite');
      field.appendChild(msg);
    }
    let ok = field.querySelector('.field-msg.ok');
    if (okMsg && !ok) {
      ok = document.createElement('div');
      ok.className = 'field-msg ok';
      field.appendChild(ok);
    }
    input.setAttribute('aria-describedby', [input.getAttribute('aria-describedby'), msg.id].filter(Boolean).join(' '));
    let touched = false;
    const check = (show = touched) => {
      const v = input.type === 'checkbox' ? (input.checked ? 'x' : '') : input.value;
      let err = '';
      for (const r of rules) { err = typeof r === 'function' ? r(v) : L.validators[r](v); if (err) break; }
      if (show) {
        field.classList.toggle('is-invalid', !!err);
        field.classList.toggle('is-valid', !err && !!okMsg);
        input.setAttribute('aria-invalid', err ? 'true' : 'false');
        msg.innerHTML = err ? `${L.icon('alert-circle', 'icon-sm')}${L.esc(err)}` : '';
        if (ok) ok.innerHTML = !err ? `${L.icon('check', 'icon-sm')}${L.esc(okMsg)}` : '';
      }
      if (!err) onValid?.(v);
      return !err;
    };
    input.addEventListener('blur', () => { touched = true; check(); });
    input.addEventListener('input', () => { if (touched || input.value.length > 3) { touched = true; check(); } });
    input.addEventListener('change', () => { touched = true; check(); });
    input._validate = () => { touched = true; return check(true); };
    return input._validate;
  };

  L.validateAll = (root) => {
    const inputs = $$('input, select, textarea', root).filter((i) => i._validate);
    const results = inputs.map((i) => i._validate());
    const firstBad = inputs[results.indexOf(false)];
    if (firstBad) { firstBad.focus(); return false; }
    return true;
  };

  /* ---------- Carga de archivos con arrastrar y soltar ---------- */
  L.dropzone = (el, { accept = '', multiple = true, maxMB = 10, onChange } = {}) => {
    const input = document.createElement('input');
    input.type = 'file';
    input.hidden = true;
    input.accept = accept;
    input.multiple = multiple;
    input.tabIndex = -1;
    input.setAttribute('aria-label', 'Seleccionar archivos');
    el.after(input);
    let list = el.parentElement.querySelector('.file-list');
    if (!list) { list = document.createElement('ul'); list.className = 'file-list'; el.parentElement.appendChild(list); }
    const files = [];
    el.setAttribute('role', 'button');
    el.setAttribute('tabindex', '0');
    el.addEventListener('click', () => input.click());
    el.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); input.click(); } });
    ['dragenter', 'dragover'].forEach((t) => el.addEventListener(t, (e) => { e.preventDefault(); el.classList.add('is-over'); }));
    ['dragleave', 'drop'].forEach((t) => el.addEventListener(t, (e) => { e.preventDefault(); el.classList.remove('is-over'); }));
    el.addEventListener('drop', (e) => add(e.dataTransfer.files));
    input.addEventListener('change', () => { add(input.files); input.value = ''; });

    function add(fl) {
      Array.from(fl).forEach((f) => {
        if (!multiple) { files.length = 0; list.innerHTML = ''; }
        const tooBig = f.size > maxMB * 1024 * 1024;
        const okType = !accept || accept.split(',').some((a) => (a.trim().endsWith('/*') ? f.type.startsWith(a.trim().slice(0, -1)) : f.name.toLowerCase().endsWith(a.trim()) || f.type === a.trim()));
        const li = document.createElement('li');
        li.className = 'file-item';
        const isImg = f.type.startsWith('image/');
        const url = isImg ? URL.createObjectURL(f) : '';
        li.innerHTML = `${isImg ? `<img class="thumb" src="${url}" alt="Vista previa de ${L.esc(f.name)}">` : `<span class="thumb">${L.icon('file')}</span>`}
          <div style="min-width:0"><div class="name">${L.esc(f.name)}</div>
          <div class="small muted st">${(f.size / 1024).toFixed(0)} KB · <span>Cargando…</span></div>
          <div class="progress" style="margin-top:6px"><span style="width:0%"></span></div></div>
          <button type="button" class="btn btn-tertiary btn-icon" aria-label="Quitar ${L.esc(f.name)}">${L.icon('trash')}</button>`;
        list.appendChild(li);
        const bar = li.querySelector('.progress > span');
        const st = li.querySelector('.st span');
        li.querySelector('button').onclick = () => { li.remove(); const i = files.indexOf(f); if (i > -1) files.splice(i, 1); onChange?.(files); L.toast('Archivo quitado', f.name, 'info'); };
        if (tooBig || !okType) {
          li.querySelector('.progress').classList.add('danger');
          bar.style.width = '100%';
          st.textContent = tooBig ? `Supera ${maxMB} MB` : 'Formato no admitido';
          st.style.color = 'var(--c-danger)';
          L.toast('No se pudo cargar el archivo', tooBig ? `${f.name} supera el máximo de ${maxMB} MB.` : `${f.name} no tiene un formato admitido (${accept}).`, 'error');
          return;
        }
        let p = 0;
        const t = setInterval(() => {
          p = Math.min(100, p + 12 + Math.random() * 22);
          bar.style.width = p + '%';
          if (p >= 100) { clearInterval(t); st.textContent = 'Cargado'; st.style.color = 'var(--c-success)'; files.push(f); onChange?.(files); }
        }, 160);
      });
    }
    return { files, add };
  };

  // Archivo simulado (para demostrar la carga sin que el evaluador tenga archivos a mano)
  L.fakeFile = (name, type = 'image/png', kb = 240) => {
    if (type.startsWith('image/')) {
      const c = document.createElement('canvas');
      c.width = 160; c.height = 120;
      const g = c.getContext('2d');
      g.fillStyle = '#5f5f5f'; g.fillRect(0, 0, 160, 120);
      g.fillStyle = '#e8641b'; g.fillRect(0, 84, 160, 36);
      g.fillStyle = '#fff'; g.font = '600 14px sans-serif'; g.fillText('Evidencia', 12, 108);
      return new Promise((res) => c.toBlob((b) => res(new File([b], name, { type }))));
    }
    return Promise.resolve(new File([new Uint8Array(kb * 1024)], name, { type }));
  };

  /* ---------- Menús desplegables y contextuales ---------- */
  L.menu = (btn, items, { align = 'right' } = {}) => {
    const wrap = btn.closest('.menu-wrap') || btn.parentElement;
    let ul = wrap.querySelector(':scope > .menu');
    if (!ul) {
      ul = document.createElement('ul');
      ul.className = `menu ${align === 'left' ? 'left' : ''}`;
      ul.setAttribute('role', 'menu');
      ul.hidden = true;
      wrap.appendChild(ul);
    }
    btn.setAttribute('aria-haspopup', 'menu');
    btn.setAttribute('aria-expanded', 'false');
    const render = () => {
      const its = typeof items === 'function' ? items() : items;
      ul.innerHTML = its.map((it, i) => (it.sep ? '<li class="sep" role="separator"></li>' : it.title ? `<li class="menu-title" role="presentation">${L.esc(it.title)}</li>` : `<li role="none"><button type="button" role="menuitem" class="${it.danger ? 'danger' : ''}" data-i="${i}" tabindex="-1">${it.icon ? L.icon(it.icon) : ''}${L.esc(it.label)}${it.kbd ? `<span class="kbd">${it.kbd}</span>` : ''}</button></li>`)).join('');
      // Devuelve el foco al disparador antes de la acción, para que un modal lo restaure al cerrarse
      $$('[role=menuitem]', ul).forEach((b) => (b.onclick = () => { close(); btn.focus(); its[b.dataset.i].onClick?.(); }));
    };
    const open = () => {
      render();
      ul.hidden = false;
      btn.setAttribute('aria-expanded', 'true');
      $('[role=menuitem]', ul)?.focus();
      setTimeout(() => document.addEventListener('mousedown', outside), 0);
    };
    const close = () => {
      ul.hidden = true;
      btn.setAttribute('aria-expanded', 'false');
      document.removeEventListener('mousedown', outside);
    };
    const outside = (e) => { if (!wrap.contains(e.target)) close(); };
    btn.addEventListener('click', () => (ul.hidden ? open() : close()));
    ul.addEventListener('keydown', (e) => menuKeys(e, ul, () => { close(); btn.focus(); }));
    btn.addEventListener('keydown', (e) => { if (e.key === 'ArrowDown') { e.preventDefault(); open(); } });
    return { open, close };
  };

  function menuKeys(e, ul, onEsc) {
    const its = $$('[role=menuitem]', ul);
    const i = its.indexOf(document.activeElement);
    if (e.key === 'ArrowDown') { e.preventDefault(); its[(i + 1) % its.length].focus(); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); its[(i - 1 + its.length) % its.length].focus(); }
    else if (e.key === 'Home') { e.preventDefault(); its[0].focus(); }
    else if (e.key === 'End') { e.preventDefault(); its[its.length - 1].focus(); }
    else if (e.key === 'Escape' || e.key === 'Tab') { onEsc(); }
  }

  // Menú contextual (clic derecho o tecla de menú) sobre filas
  L.contextMenu = (root, selector, itemsFor) => {
    const show = (x, y, target) => {
      $('.context-menu')?.remove();
      const its = itemsFor(target);
      const ul = document.createElement('ul');
      ul.className = 'menu context-menu';
      ul.setAttribute('role', 'menu');
      ul.innerHTML = its.map((it, i) => (it.sep ? '<li class="sep" role="separator"></li>' : `<li role="none"><button type="button" role="menuitem" class="${it.danger ? 'danger' : ''}" data-i="${i}" tabindex="-1">${it.icon ? L.icon(it.icon) : ''}${L.esc(it.label)}</button></li>`)).join('');
      document.body.appendChild(ul);
      const r = ul.getBoundingClientRect();
      ul.style.left = Math.min(x, innerWidth - r.width - 8) + 'px';
      ul.style.top = Math.min(y, innerHeight - r.height - 8) + 'px';
      const close = () => { ul.remove(); document.removeEventListener('mousedown', outside); target.focus?.(); };
      const outside = (e) => { if (!ul.contains(e.target)) close(); };
      setTimeout(() => document.addEventListener('mousedown', outside), 0);
      $$('[role=menuitem]', ul).forEach((b) => (b.onclick = () => { close(); its[b.dataset.i].onClick?.(); }));
      ul.addEventListener('keydown', (e) => menuKeys(e, ul, close));
      $('[role=menuitem]', ul)?.focus();
      L.onLeave(() => ul.remove());
    };
    root.addEventListener('contextmenu', (e) => {
      const t = e.target.closest(selector);
      if (!t) return;
      e.preventDefault();
      show(e.clientX, e.clientY, t);
    });
    root.addEventListener('keydown', (e) => {
      const t = e.target.closest(selector);
      if (!t || !(e.key === 'ContextMenu' || (e.shiftKey && e.key === 'F10'))) return;
      e.preventDefault();
      const r = t.getBoundingClientRect();
      show(r.left + 24, r.bottom, t);
    });
  };

  /* ---------- Pestañas ---------- */
  L.tabs = (root, onChange) => {
    const tabs = $$('[role=tab]', root);
    const select = (t, focus = true) => {
      tabs.forEach((x) => {
        const on = x === t;
        x.setAttribute('aria-selected', on);
        x.tabIndex = on ? 0 : -1;
        const p = document.getElementById(x.getAttribute('aria-controls'));
        if (p) p.hidden = !on;
      });
      if (focus) t.focus();
      onChange?.(t.dataset.tab || t.id);
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => select(t));
      t.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') select(tabs[(i + 1) % tabs.length]);
        if (e.key === 'ArrowLeft') select(tabs[(i - 1 + tabs.length) % tabs.length]);
        if (e.key === 'Home') select(tabs[0]);
        if (e.key === 'End') select(tabs[tabs.length - 1]);
      });
    });
    return { select: (id) => select(tabs.find((t) => (t.dataset.tab || t.id) === id), false) };
  };

  L.tabsHtml = (id, items, active) => `<div class="tabs" role="tablist" aria-label="${L.esc(id)}">${items.map((it) => `<button type="button" role="tab" id="${id}-${it.id}" data-tab="${it.id}" aria-controls="${id}-${it.id}-p" aria-selected="${it.id === active}" tabindex="${it.id === active ? 0 : -1}">${L.esc(it.label)}${it.count != null ? ` <span class="badge plain">${it.count}</span>` : ''}</button>`).join('')}</div>`;
  L.panelAttrs = (id, tab, active) => `id="${id}-${tab}-p" role="tabpanel" aria-labelledby="${id}-${tab}" tabindex="0" ${tab !== active ? 'hidden' : ''}`;

  /* ---------- Acordeones ---------- */
  L.accordions = (root) => {
    $$('.accordion-btn', root).forEach((b) => {
      b.addEventListener('click', () => {
        const open = b.getAttribute('aria-expanded') === 'true';
        b.setAttribute('aria-expanded', !open);
        document.getElementById(b.getAttribute('aria-controls')).hidden = open;
      });
    });
  };
  L.accordionHtml = (title, body, open = false, extra = '') => {
    const id = L.uid('acc');
    return `<div class="accordion"><h3><button type="button" class="accordion-btn" aria-expanded="${open}" aria-controls="${id}">${title}${extra}${L.icon('chev-down', 'chev')}</button></h3><div class="accordion-panel" id="${id}" ${open ? '' : 'hidden'}>${body}</div></div>`;
  };

  /* ---------- Autocompletado ---------- */
  L.combobox = (input, source, { onSelect, render, min = 1, max = 8 } = {}) => {
    const wrap = input.closest('.combo');
    const list = document.createElement('ul');
    list.className = 'combo-list';
    list.id = L.uid('lb');
    list.setAttribute('role', 'listbox');
    list.hidden = true;
    wrap.appendChild(list);
    input.setAttribute('role', 'combobox');
    input.setAttribute('aria-autocomplete', 'list');
    input.setAttribute('aria-expanded', 'false');
    input.setAttribute('aria-controls', list.id);
    input.setAttribute('autocomplete', 'off');
    let items = [], idx = -1;
    const hl = (txt, q) => L.esc(txt).replace(new RegExp(`(${q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'ig'), '<mark>$1</mark>');
    const close = () => { list.hidden = true; input.setAttribute('aria-expanded', 'false'); input.removeAttribute('aria-activedescendant'); idx = -1; };
    const update = () => {
      const q = input.value.trim();
      if (q.length < min) { close(); return; }
      const norm = (s) => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
      const lev = (a, b) => { const d = Array.from({ length: a.length + 1 }, (_, i) => [i, ...Array(b.length).fill(0)]); for (let j = 1; j <= b.length; j++) d[0][j] = j; for (let i = 1; i <= a.length; i++) for (let j = 1; j <= b.length; j++) d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)); return d[a.length][b.length]; };
      // Typo tolerance (RF-17.11): substring, ignoring spaces, or every word within 1-2 edits of a word of the text
      const fuzzy = (txt, qn) => { if (txt.includes(qn) || txt.replace(/\s/g, '').includes(qn.replace(/\s/g, ''))) return true; const words = txt.split(/[^a-z0-9]+/).filter(Boolean); return qn.split(/\s+/).filter(Boolean).every((t) => t.length < 3 ? txt.includes(t) : words.some((w) => w.startsWith(t) || lev(t, w.slice(0, t.length + 1)) <= (t.length > 5 ? 2 : 1) || lev(t, w) <= (t.length > 5 ? 2 : 1))); };
      // Result-type filter: «cliente: roble», «pedido: 2648», «ruta:», «lote:», «pantalla:»
      const tm = q.match(/^(cliente|pedido|ruta|lote|pantalla)s?\s*:\s*(.*)$/i);
      const qq = tm ? tm[2] : q;
      items = source().filter((it) => (!tm || norm(it.meta || '').startsWith(norm(tm[1]))) && fuzzy(norm(it.label + ' ' + (it.meta || '')), norm(qq))).slice(0, max);
      list.innerHTML = items.length
        ? items.map((it, i) => `<li role="option" id="${list.id}-${i}" aria-selected="false" data-i="${i}">${render ? render(it, q, hl) : `<span>${hl(it.label, q)}</span>${it.meta ? `<span class="small muted" style="margin-left:auto">${L.esc(it.meta)}</span>` : ''}`}</li>`).join('')
        : `<li role="option" aria-disabled="true" class="muted">Sin coincidencias para «${L.esc(q)}»</li>`;
      list.hidden = false;
      input.setAttribute('aria-expanded', 'true');
      idx = -1;
    };
    const move = (d) => {
      const opts = $$('[role=option][data-i]', list);
      if (!opts.length) return;
      idx = (idx + d + opts.length) % opts.length;
      opts.forEach((o, i) => o.setAttribute('aria-selected', i === idx));
      input.setAttribute('aria-activedescendant', opts[idx].id);
      opts[idx].scrollIntoView({ block: 'nearest' });
    };
    const pick = (i) => { const it = items[i]; if (!it) return; input.value = it.label; close(); onSelect?.(it); };
    input.addEventListener('input', update);
    input.addEventListener('focus', () => input.value && update());
    input.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowDown') { e.preventDefault(); list.hidden ? update() : move(1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
      else if (e.key === 'Enter' && !list.hidden && idx > -1) { e.preventDefault(); pick(idx); }
      else if (e.key === 'Escape') close();
    });
    list.addEventListener('mousedown', (e) => { const li = e.target.closest('[data-i]'); if (li) { e.preventDefault(); pick(+li.dataset.i); } });
    input.addEventListener('blur', () => setTimeout(close, 120));
  };

  /* ---------- Tabla con orden, filtro, paginación y selección ---------- */
  L.dataTable = (host, cfg) => {
    host.dataset.managedTable = 'true';
    const st = { q: '', sort: cfg.sort || null, dir: cfg.dir || 'asc', page: 1, per: cfg.per || 10, sel: new Set(), filters: {} };
    const rowsAll = () => (typeof cfg.rows === 'function' ? cfg.rows() : cfg.rows);
    const norm = (s) => String(s ?? '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
    const filtered = () => {
      let r = rowsAll();
      if (st.q) r = r.filter((x) => norm(cfg.searchKeys.map((k) => x[k]).join(' ')).includes(norm(st.q)));
      Object.entries(st.filters).forEach(([k, v]) => { if (v) r = r.filter((x) => String(x[k]) === v); });
      if (st.sort) {
        const col = cfg.columns.find((c) => c.key === st.sort);
        const val = col.sortVal || ((x) => x[st.sort]);
        r = [...r].sort((a, b) => { const A = val(a), B = val(b); const c = typeof A === 'number' ? A - B : String(A).localeCompare(String(B), 'es'); return st.dir === 'asc' ? c : -c; });
      }
      return r;
    };
    const id = cfg.id || L.uid('tbl');
    host.innerHTML = `
      <div class="toolbar">
        <div class="input-wrap search">${L.icon('search')}<label class="sr-only" for="${id}-q">Buscar</label><input id="${id}-q" class="input" type="search" placeholder="${L.esc(cfg.searchPlaceholder || 'Buscar…')}"></div>
        ${(cfg.filters || []).map((f) => `<label class="sr-only" for="${id}-f-${f.key}">${L.esc(f.label)}</label><select id="${id}-f-${f.key}" class="select" data-filter="${f.key}" style="width:auto;min-width:160px"><option value="">${L.esc(f.label)}: todos</option>${f.options.map((o) => `<option>${L.esc(o)}</option>`).join('')}</select>`).join('')}
        <span class="grow"></span>
        ${cfg.toolbarExtra || ''}
        ${L.me?.()?.all || L.me?.()?.id === 'ti' ? `<button type="button" class="btn btn-secondary btn-sm" data-json-export aria-label="Exportar JSON: ${L.esc(cfg.caption || 'Listado')}">${L.icon('download', 'icon-sm')}Exportar JSON</button>` : ''}
      </div>
      <div class="bulk-slot"></div>
      <div class="table-wrap"><table class="table" aria-describedby="${id}-sum"><caption class="sr-only">${L.esc(cfg.caption || 'Listado')}</caption><thead></thead><tbody></tbody></table></div>
      <div class="pagination"><span id="${id}-sum" aria-live="polite"></span><ul></ul></div>`;
    const thead = $('thead', host), tbody = $('tbody', host), pag = $('.pagination ul', host), sum = $(`#${id}-sum`, host), bulk = $('.bulk-slot', host);
    const draw = () => {
      const all = filtered();
      const pages = Math.max(1, Math.ceil(all.length / st.per));
      st.page = Math.min(st.page, pages);
      const slice = all.slice((st.page - 1) * st.per, st.page * st.per);
      thead.innerHTML = `<tr>${cfg.selectable ? `<th style="width:52px"><label class="check check-cell"><input type="checkbox" data-all aria-label="Seleccionar todos los de esta página"></label></th>` : ''}${cfg.columns.map((c) => `<th class="${c.right ? 'right' : ''}" ${st.sort === c.key ? `aria-sort="${st.dir === 'asc' ? 'ascending' : 'descending'}"` : ''}>${c.sortable === false ? L.esc(c.label) : `<button type="button" class="th-sort" data-sort="${c.key}" ${st.sort === c.key ? `aria-sort="${st.dir}"` : ''}>${L.esc(c.label)}${L.icon(st.sort === c.key ? (st.dir === 'asc' ? 'chev-up' : 'chev-down') : 'arrow-up-down')}</button>`}</th>`).join('')}${cfg.rowActions ? '<th class="right"><span class="sr-only">Acciones</span></th>' : ''}</tr>`;
      tbody.innerHTML = slice.length
        ? slice.map((r) => `<tr data-id="${L.esc(r[cfg.key || 'id'])}" class="${st.sel.has(String(r[cfg.key || 'id'])) ? 'is-selected' : ''}" tabindex="-1">${cfg.selectable ? `<td><label class="check check-cell"><input type="checkbox" data-sel aria-label="Seleccionar ${L.esc(r[cfg.key || 'id'])}" ${st.sel.has(String(r[cfg.key || 'id'])) ? 'checked' : ''}></label></td>` : ''}${cfg.columns.map((c) => `<td class="${c.right ? 'num right' : ''} ${c.wrap ? 'wrap' : ''}">${c.render ? c.render(r) : L.esc(r[c.key])}</td>`).join('')}${cfg.rowActions ? `<td class="right"><div class="menu-wrap"><button type="button" class="btn btn-tertiary btn-icon" data-rowmenu aria-label="Acciones para ${L.esc(r[cfg.key || 'id'])}">${L.icon('more')}<span class="btn-label" aria-hidden="true">Acciones</span></button></div></td>` : ''}</tr>`).join('')
        : `<tr><td colspan="99">${L.empty('search', 'Sin resultados', 'No hay registros que coincidan con la búsqueda o los filtros. Pruebe con otros términos o limpie los filtros.', '<button type="button" class="btn btn-secondary" data-clear>Limpiar filtros</button>')}</td></tr>`;
      sum.textContent = all.length ? `Mostrando ${(st.page - 1) * st.per + 1}–${Math.min(st.page * st.per, all.length)} de ${all.length}` : '0 resultados';
      const nums = [];
      for (let p = 1; p <= pages; p++) if (p === 1 || p === pages || Math.abs(p - st.page) <= 1) nums.push(p); else if (nums[nums.length - 1] !== '…') nums.push('…');
      pag.innerHTML = `<li><button type="button" data-page="${st.page - 1}" ${st.page === 1 ? 'disabled' : ''} aria-label="Página anterior">${L.icon('chev-left')}<span aria-hidden="true">Anterior</span></button></li>${nums.map((p) => (p === '…' ? '<li aria-hidden="true" style="align-self:center;padding:0 4px">…</li>' : `<li><button type="button" data-page="${p}" ${p === st.page ? 'aria-current="page"' : ''} aria-label="Página ${p}">${p}</button></li>`)).join('')}<li><button type="button" data-page="${st.page + 1}" ${st.page === pages ? 'disabled' : ''} aria-label="Página siguiente"><span aria-hidden="true">Siguiente</span>${L.icon('chev-right')}</button></li>`;
      const allBox = $('[data-all]', thead);
      if (allBox) { const ids = slice.map((r) => String(r[cfg.key || 'id'])); allBox.checked = ids.length && ids.every((x) => st.sel.has(x)); allBox.indeterminate = !allBox.checked && ids.some((x) => st.sel.has(x)); }
      bulk.innerHTML = st.sel.size && cfg.bulkActions ? `<div class="bulkbar" role="region" aria-label="Acciones masivas"><strong>${st.sel.size} seleccionado${st.sel.size > 1 ? 's' : ''}</strong>${cfg.bulkActions.map((a, i) => `<button type="button" class="btn btn-sm ${a.cls || 'btn-secondary'}" data-bulk="${i}">${a.icon ? L.icon(a.icon, 'icon-sm') : ''}${L.esc(a.label)}</button>`).join('')}<button type="button" class="btn btn-sm btn-tertiary" style="color:inherit" data-unsel>Quitar selección</button></div>` : '';
      cfg.onDraw?.(host, all);
    };
    host.addEventListener('click', (e) => {
      if (e.target.closest('[data-json-export]')) {
        L.download(`${id}.json`, JSON.stringify(filtered(), null, 2), 'application/json');
        L.toast('JSON exportado', 'Todos los registros filtrados, en el orden aplicado.', 'success');
        return;
      }
      const s = e.target.closest('[data-sort]');
      if (s) { const k = s.dataset.sort; st.dir = st.sort === k && st.dir === 'asc' ? 'desc' : 'asc'; st.sort = k; draw(); $(`[data-sort="${k}"]`, host).focus(); return; }
      const p = e.target.closest('[data-page]');
      if (p && !p.disabled) { st.page = +p.dataset.page; draw(); $('[aria-current="page"]', pag)?.focus(); return; }
      if (e.target.closest('[data-clear]')) { st.q = ''; st.filters = {}; $(`#${id}-q`, host).value = ''; $$('[data-filter]', host).forEach((s) => (s.value = '')); draw(); return; }
      if (e.target.closest('[data-unsel]')) { st.sel.clear(); draw(); return; }
      const b = e.target.closest('[data-bulk]');
      if (b) { cfg.bulkActions[b.dataset.bulk].onClick([...st.sel], () => { st.sel.clear(); draw(); }); return; }
      const rm = e.target.closest('[data-rowmenu]');
      if (rm && !rm._menu) { const tr = rm.closest('tr'); rm._menu = L.menu(rm, () => cfg.rowActions(rowsAll().find((r) => String(r[cfg.key || 'id']) === tr.dataset.id), draw)); rm._menu.open(); }
    });
    host.addEventListener('change', (e) => {
      if (e.target.matches('[data-all]')) { const ids = filtered().slice((st.page - 1) * st.per, st.page * st.per).map((r) => String(r[cfg.key || 'id'])); ids.forEach((x) => (e.target.checked ? st.sel.add(x) : st.sel.delete(x))); draw(); }
      if (e.target.matches('[data-sel]')) { const x = e.target.closest('tr').dataset.id; e.target.checked ? st.sel.add(x) : st.sel.delete(x); draw(); $(`tr[data-id="${CSS.escape(x)}"] [data-sel]`, host)?.focus(); }
      if (e.target.matches('[data-filter]')) { st.filters[e.target.dataset.filter] = e.target.value; st.page = 1; draw(); }
    });
    let t;
    $(`#${id}-q`, host).addEventListener('input', (e) => { clearTimeout(t); t = setTimeout(() => { st.q = e.target.value; st.page = 1; draw(); }, 150); });
    if (cfg.rowActions) L.contextMenu(host, 'tbody tr[data-id]', (tr) => cfg.rowActions(rowsAll().find((r) => String(r[cfg.key || 'id']) === tr.dataset.id), draw));
    draw();
    return { draw, state: st, filtered };
  };

  /* ---------- Estados vacíos ilustrados ---------- */
  L.illus = (kind = 'box') => {
    const shapes = {
      box: '<rect x="44" y="40" width="80" height="56" rx="6" fill="var(--c-surface)" stroke="var(--c-line)" stroke-width="2"/><path d="M44 52h80" stroke="var(--c-line)" stroke-width="2"/><rect x="72" y="46" width="24" height="12" rx="3" fill="var(--c-accent)"/>',
      search: '<circle cx="76" cy="58" r="26" fill="var(--c-surface)" stroke="var(--c-line)" stroke-width="3"/><path d="m95 77 18 18" stroke="var(--c-accent)" stroke-width="6" stroke-linecap="round"/><path d="M66 58h20" stroke="var(--c-line)" stroke-width="3" stroke-linecap="round"/>',
      done: '<circle cx="84" cy="60" r="34" fill="var(--c-surface)" stroke="var(--c-line)" stroke-width="2"/><path d="m68 60 11 11 21-23" fill="none" stroke="var(--c-accent)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>',
      truck: '<rect x="30" y="44" width="64" height="40" rx="4" fill="var(--c-surface)" stroke="var(--c-line)" stroke-width="2"/><path d="M94 56h20l14 14v14H94Z" fill="var(--c-surface)" stroke="var(--c-line)" stroke-width="2"/><circle cx="52" cy="88" r="9" fill="var(--c-accent)"/><circle cx="112" cy="88" r="9" fill="var(--c-accent)"/>',
      offline: '<path d="M44 66a56 56 0 0 1 80 0M58 78a36 36 0 0 1 52 0M72 90a16 16 0 0 1 24 0" fill="none" stroke="var(--c-line)" stroke-width="4" stroke-linecap="round"/><path d="m50 34 68 68" stroke="var(--c-accent)" stroke-width="5" stroke-linecap="round"/>'
    };
    return `<svg class="illus" viewBox="0 0 168 120" aria-hidden="true"><ellipse cx="84" cy="108" rx="60" ry="6" fill="var(--c-line-soft)"/>${shapes[kind] || shapes.box}</svg>`;
  };
  L.empty = (kind, title, text, action = '') => `<div class="empty">${L.illus(kind)}<h3>${L.esc(title)}</h3><p>${L.esc(text)}</p>${action}</div>`;

  L.skeleton = (rows = 4) => `<div aria-hidden="true"><div class="skeleton sk-title"></div>${Array.from({ length: rows }, (_, i) => `<div class="skeleton sk-line" style="width:${90 - (i % 3) * 18}%"></div>`).join('')}</div>`;

  // Simula una carga con esqueleto y luego pinta el contenido
  L.withSkeleton = (el, html, ms = 650, after) => {
    el.setAttribute('aria-busy', 'true');
    el.innerHTML = L.skeleton(5);
    L.timeout(() => { el.innerHTML = html; el.removeAttribute('aria-busy'); after?.(el); }, ms);
  };

  // Mantiene la burbuja de ayuda dentro de la ventana para que no genere desplazamiento horizontal
  const fitTip = (e) => {
    const b = e.target.closest?.('.tip')?.querySelector('.tip-bubble');
    if (!b) return;
    b.style.setProperty('--tip-shift', '0px');
    // Se mide de inmediato: leer el rectángulo fuerza el cálculo con la burbuja ya visible
    const r = b.getBoundingClientRect(), pad = 8, vw = document.documentElement.clientWidth;
    if (!r.width) return;
    const shift = r.right > vw - pad ? vw - pad - r.right : r.left < pad ? pad - r.left : 0;
    b.style.setProperty('--tip-shift', `${Math.round(shift)}px`);
  };
  document.addEventListener('mouseover', fitTip);
  document.addEventListener('focusin', fitTip);
  L.tip = (text) => `<span class="tip"><button type="button" class="tip-btn" aria-label="Más información: ${L.esc(text)}">${L.icon('info', 'icon-sm')}</button><span class="tip-bubble" role="tooltip">${L.esc(text)}</span></span>`;

  L.badge = (text, kind = '') => `<span class="badge ${kind ? 'badge-' + kind : ''}">${L.esc(text)}</span>`;

  L.alert = (kind, title, text = '', actions = '') => `<div class="alert alert-${kind}" role="${kind === 'danger' ? 'alert' : 'status'}">${L.icon({ success: 'check-circle', warning: 'alert', danger: 'alert-circle', info: 'info' }[kind])}<div><strong>${L.esc(title)}</strong>${text ? `<p>${text}</p>` : ''}</div>${actions ? `<div class="alert-actions">${actions}</div>` : ''}</div>`;

  // Botón con estado de carga
  L.busy = async (btn, fn, ms = 900) => {
    btn.classList.add('is-loading');
    btn.setAttribute('aria-busy', 'true');
    btn.disabled = true;
    try { await L.sleep(ms); return await fn(); }
    finally { btn.classList.remove('is-loading'); btn.removeAttribute('aria-busy'); btn.disabled = false; }
  };

  // Exportación de archivos (CSV con BOM para Excel)
  L.download = (name, content, type = 'text/csv;charset=utf-8') => {
    const blob = new Blob([type.startsWith('text/csv') ? '﻿' + content : content], { type });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = name;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(a.href), 1000);
  };
  L.toCSV = (rows, cols) => [cols.map((c) => c.label).join(';'), ...rows.map((r) => cols.map((c) => `"${String(c.val ? c.val(r) : r[c.key]).replace(/"/g, '""')}"`).join(';'))].join('\n');

  /* ---------- Firma en pantalla ---------- */
  L.signaturePad = (canvas, onChange) => {
    const ctx = canvas.getContext('2d');
    const fit = () => { const r = canvas.getBoundingClientRect(); canvas.width = r.width * devicePixelRatio; canvas.height = r.height * devicePixelRatio; ctx.scale(devicePixelRatio, devicePixelRatio); ctx.lineWidth = 2.4; ctx.lineCap = 'round'; ctx.strokeStyle = getComputedStyle(document.documentElement).getPropertyValue('--c-ink'); };
    fit();
    let drawing = false, has = false, last;
    const pos = (e) => { const r = canvas.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; };
    canvas.addEventListener('pointerdown', (e) => { drawing = true; last = pos(e); canvas.setPointerCapture(e.pointerId); });
    canvas.addEventListener('pointermove', (e) => { if (!drawing) return; const p = pos(e); ctx.beginPath(); ctx.moveTo(...last); ctx.lineTo(...p); ctx.stroke(); last = p; if (!has) { has = true; onChange?.(true); } });
    canvas.addEventListener('pointerup', () => (drawing = false));
    // Alternativa por teclado: firma simulada
    canvas.tabIndex = 0;
    canvas.setAttribute('role', 'img');
    canvas.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); api.fake(); } });
    const api = {
      clear() { ctx.clearRect(0, 0, canvas.width, canvas.height); has = false; onChange?.(false); },
      fake() { const w = canvas.getBoundingClientRect().width; ctx.beginPath(); ctx.moveTo(24, 110); for (let x = 24; x < w - 30; x += 12) ctx.lineTo(x, 90 + Math.sin(x / 9) * 22 + Math.cos(x / 23) * 10); ctx.stroke(); has = true; onChange?.(true); },
      get signed() { return has; }
    };
    return api;
  };

  /* ---------- Recorrido guiado ---------- */
  L.tour = (steps, onEnd) => {
    let i = 0;
    const spot = document.createElement('div');
    spot.className = 'tour-spot';
    const card = document.createElement('div');
    card.className = 'tour-card';
    card.setAttribute('role', 'dialog');
    card.setAttribute('aria-modal', 'true');
    card.setAttribute('aria-labelledby', 'tour-t');
    document.body.append(spot, card);
    const end = (done) => { spot.remove(); card.remove(); document.removeEventListener('keydown', key, true); onEnd?.(done); };
    const key = (e) => { if (e.key === 'Escape') end(false); if (e.key === 'Tab') trapFocus(e, card); };
    document.addEventListener('keydown', key, true);
    const show = () => {
      const s = steps[i];
      const target = s.target && $(s.target);
      if (target && target.offsetParent !== null) {
        target.scrollIntoView({ block: 'center', behavior: 'smooth' });
        const r = target.getBoundingClientRect();
        Object.assign(spot.style, { display: 'block', left: r.left - 6 + 'px', top: r.top - 6 + 'px', width: r.width + 12 + 'px', height: r.height + 12 + 'px' });
        const below = r.bottom + 220 < innerHeight;
        const left = Math.max(16, Math.min(r.left, innerWidth - 376));
        Object.assign(card.style, { left: left + 'px', top: (below ? r.bottom + 16 : Math.max(16, r.top - 236)) + 'px', transform: '' });
      } else {
        Object.assign(spot.style, { display: 'block', left: '50%', top: '50%', width: '0px', height: '0px' });
        Object.assign(card.style, { left: '50%', top: '50%', transform: 'translate(-50%, -50%)' });
      }
      card.innerHTML = `<div class="row-between" style="margin-bottom:8px"><span class="small muted">Paso ${i + 1} de ${steps.length}</span><div class="tour-dots" aria-hidden="true">${steps.map((_, j) => `<span class="${j === i ? 'on' : ''}"></span>`).join('')}</div></div>
        <h2 id="tour-t">${L.esc(s.title)}</h2><p>${L.esc(s.text)}</p>
        <div class="row-between" style="margin-top:16px"><button type="button" class="btn btn-tertiary" data-skip>Omitir recorrido</button>
        <div class="btn-group">${i > 0 ? '<button type="button" class="btn btn-secondary" data-prev>Anterior</button>' : ''}<button type="button" class="btn btn-primary" data-next>${i === steps.length - 1 ? 'Comenzar a trabajar' : 'Siguiente'}</button></div></div>`;
      $('[data-skip]', card).onclick = () => end(false);
      $('[data-prev]', card) && ($('[data-prev]', card).onclick = () => { i--; show(); });
      $('[data-next]', card).onclick = () => { if (i === steps.length - 1) end(true); else { i++; show(); } };
      $('[data-next]', card).focus();
    };
    setTimeout(show, 50);
  };

  /* ---------- Varios ---------- */
  L.debounce = (fn, ms = 200) => { let t; return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); }; };
  L.initials = (name) => name.split(' ').filter(Boolean).slice(0, 2).map((p) => p[0]).join('').toUpperCase();
  L.announce = (txt) => { const r = $('#sr-live'); r.textContent = ''; setTimeout(() => (r.textContent = txt), 30); };
})(window.LFX = window.LFX || {});
