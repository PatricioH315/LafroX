/* Administración: personas usuarias, roles y permisos (RBAC), parametrización con
   aprobación de un segundo perfil y consulta de auditoría (RF-15.04, RF-17.01 a RF-17.05). */
(function (L) {
  const { esc, icon, $, $$, data: D, fmt } = L;
  const roleName = (id) => D.roles.find((r) => r.id === id)?.nombre || id;

  L.route('/admin/usuarios', {
    title: 'Personas usuarias', parent: '/inicio', block: 'Administración', module: 'Base compartida (Keycloak)', rf: ['RF-17.01', 'RF-15.05', 'RF-15.03'], actors: ['Jefe de TI'],
    render: () => `<div class="page-head"><div class="titles"><h1>Personas usuarias</h1><p class="muted" style="margin:0">Altas, bajas, roles y segundo factor, sin intervención del proveedor (RF-17.01).</p></div><div class="actions"><button type="button" class="btn btn-secondary" id="us-imp">${icon('upload')}Importar CSV</button><button type="button" class="btn btn-primary" id="us-new">${icon('plus')}Invitar persona</button></div></div>
      <div class="card card-flush" id="us-t"></div>`,
    mount: (root, p, q) => {
      const tbl = L.dataTable($('#us-t', root), {
        id: 'us', caption: 'Personas usuarias', rows: D.usuarios, searchKeys: ['nombre', 'correo', 'sitio'], searchPlaceholder: 'Buscar por nombre o correo',
        filters: [{ key: 'rol', label: 'Rol', options: D.roles.map((r) => r.id) }, { key: 'estado', label: 'Estado', options: ['Activo', 'Suspendido', 'Pendiente'] }],
        sort: 'nombre', selectable: true,
        columns: [
          { key: 'nombre', label: 'Persona', render: (r) => `<div class="row" style="flex-wrap:nowrap"><span class="avatar" style="width:36px;height:36px">${L.initials(r.nombre)}</span><div>${esc(r.nombre)}<div class="small muted">${esc(r.correo)}</div></div></div>` },
          { key: 'rol', label: 'Rol', render: (r) => esc(roleName(r.rol)) }, { key: 'sitio', label: 'Sitio' },
          { key: 'mfa', label: 'Segundo factor', render: (r) => (r.mfa ? L.badge('Exigido', 'success') : L.badge('No exigido', '')) },
          { key: 'ultimo', label: 'Último acceso', render: (r) => fmt.dt(r.ultimo), sortVal: (r) => r.ultimo },
          { key: 'estado', label: 'Estado', render: (r) => L.badge(r.estado, r.estado === 'Activo' ? 'success' : r.estado === 'Suspendido' ? 'danger' : 'warning') }
        ],
        rowActions: (r, redraw) => [
          { label: 'Cambiar rol', icon: 'key', onClick: () => roleModal(r, redraw) },
          { label: 'Restablecer segundo factor', icon: 'fingerprint', onClick: () => L.toast('Segundo factor restablecido', `${r.nombre} deberá enrolarlo en su próximo ingreso.`, 'success') },
          { sep: true },
          r.estado === 'Suspendido' ? { label: 'Reactivar', icon: 'check', onClick: () => { r.estado = 'Activo'; redraw(); L.toast('Cuenta reactivada', r.nombre, 'success'); } } : { label: 'Suspender acceso', icon: 'ban', danger: true, onClick: async () => { if (await L.confirm({ title: `¿Suspender a ${r.nombre}?`, message: 'Se cerrarán sus sesiones en todos los módulos de inmediato (baja efectiva, RF-15.05).', confirmLabel: 'Suspender', danger: true })) { r.estado = 'Suspendido'; redraw(); L.toast('Acceso suspendido', 'Sesiones cerradas en todos los módulos.', 'success'); } } }
        ],
        bulkActions: [{ label: 'Exigir segundo factor', icon: 'fingerprint', onClick: (ids, done) => { D.usuarios.filter((u) => ids.includes(u.id)).forEach((u) => (u.mfa = true)); done(); L.toast('Segundo factor exigido', `${ids.length} persona(s).`, 'success'); } }, { label: 'Suspender', icon: 'ban', onClick: async (ids, done) => { if (await L.confirm({ title: `¿Suspender ${ids.length} cuenta(s)?`, message: 'Se cerrarán sus sesiones en todos los módulos.', confirmLabel: 'Suspender', danger: true, requireText: 'SUSPENDER' })) { D.usuarios.filter((u) => ids.includes(u.id)).forEach((u) => (u.estado = 'Suspendido')); done(); L.toast('Cuentas suspendidas', '', 'success'); } } }]
      });
      const roleModal = (u, redraw) => L.modal({ title: `Cambiar rol de ${u.nombre}`, body: `<div class="field"><label for="rl">Rol</label><select id="rl" class="select">${D.roles.map((r) => `<option value="${r.id}" ${r.id === u.rol ? 'selected' : ''}>${esc(r.nombre)}</option>`).join('')}</select></div><p class="hint">El cambio de rol requiere confirmación y queda en la auditoría.</p>`, actions: [{ label: 'Cancelar' }, { label: 'Guardar', cls: 'btn-primary', onClick: async (api) => { const v = $('#rl', api.el).value; if (v === u.rol) return; api.close(); if (await L.confirm({ title: 'Confirmar cambio de rol', message: `${esc(u.nombre)} pasará de «${esc(roleName(u.rol))}» a «${esc(roleName(v))}» y verá otro menú.`, confirmLabel: 'Confirmar cambio' })) { u.rol = v; redraw(); L.toast('Rol actualizado', u.nombre, 'success'); } return false; } }] });
      const invite = () => L.modal({
        title: 'Invitar persona usuaria', size: 'lg',
        body: `<div class="form-grid"><div class="field"><label for="iv-n">Nombre completo <span class="req" aria-hidden="true">*</span></label><input id="iv-n" class="input" autocomplete="off"></div><div class="field"><label for="iv-e">Correo corporativo <span class="req" aria-hidden="true">*</span></label><input id="iv-e" class="input" type="email" placeholder="nombre@puelche.cl"></div>
          <div class="field"><label for="iv-r">Rol <span class="req" aria-hidden="true">*</span></label><select id="iv-r" class="select"><option value="">Seleccione…</option>${D.roles.map((r) => `<option value="${r.id}">${esc(r.nombre)}</option>`).join('')}</select></div><div class="field"><label for="iv-s">Sitio</label><select id="iv-s" class="select">${D.sitios.map((s) => `<option>${esc(s.nombre)}</option>`).join('')}</select></div>
          <div class="field"><label for="iv-d">Fecha de inicio</label><input id="iv-d" class="input" type="date" value="2026-11-16"></div><div class="field"><label for="iv-h">Vigencia hasta (opcional)</label><input id="iv-h" class="input" type="date"></div>
          <div class="full"><label class="check"><input type="checkbox" id="iv-m" checked> Exigir segundo factor desde el primer ingreso</label></div></div>`,
        onOpen: (d) => { L.bindField($('#iv-n', d), ['required']); L.bindField($('#iv-e', d), ['email', (v) => (v.endsWith('@puelche.cl') ? '' : 'Use un correo del dominio @puelche.cl.'), (v) => (D.usuarios.some((u) => u.correo === v) ? 'Ya existe una persona con ese correo.' : '')]); L.bindField($('#iv-r', d), ['required']); L.bindField($('#iv-h', d), [(v) => (!v || v > $('#iv-d', d).value ? '' : 'La vigencia debe terminar después del inicio.')]); },
        actions: [{ label: 'Cancelar' }, { label: 'Enviar invitación', cls: 'btn-primary', icon: 'send', onClick: async (api, btn) => { if (!L.validateAll(api.el)) return false; await L.busy(btn, () => {}, 800); D.usuarios.unshift({ id: 'U-' + (2000 + D.usuarios.length), nombre: $('#iv-n', api.el).value, correo: $('#iv-e', api.el).value, rol: $('#iv-r', api.el).value, sitio: $('#iv-s', api.el).value, estado: 'Pendiente', mfa: $('#iv-m', api.el).checked, ultimo: new Date().toISOString() }); tbl.draw(); L.toast('Invitación enviada', 'La persona recibirá un enlace de activación.', 'success'); } }]
      });
      $('#us-new', root).onclick = invite;
      $('#us-imp', root).onclick = () => L.modal({ title: 'Importar personas desde CSV', body: `<div class="dropzone" id="imp-dz">${icon('upload', 'icon-lg')}<div><strong>Arrastre el archivo CSV</strong> o haga clic</div><span class="small">Columnas: nombre; correo; rol; sitio</span></div><button type="button" class="btn btn-tertiary btn-sm" id="imp-f" style="margin-top:6px">Usar archivo de ejemplo</button>`, onOpen: (d) => { const z = L.dropzone($('#imp-dz', d), { accept: '.csv,text/csv', multiple: false, maxMB: 2 }); $('#imp-f', d).onclick = async () => z.add([await L.fakeFile('personas.csv', 'text/csv', 4)]); d._z = z; }, actions: [{ label: 'Cancelar' }, { label: 'Validar e importar', cls: 'btn-primary', onClick: (api) => { if (!api.el._z.files.length) { L.toast('Adjunte un archivo CSV', '', 'error'); return false; } L.toast('Importación validada', '12 filas válidas · 1 con correo duplicado (omitida).', 'warning'); } }] });
      if (q.nuevo) invite();
    }
  });

  L.route('/admin/roles', {
    title: 'Roles y permisos', parent: '/inicio', block: 'Administración', module: 'Base compartida (RBAC)', rf: ['RF-15.04', 'RF-17.01', 'RF-17.03'], actors: ['Jefe de TI'],
    render: () => `<div class="page-head"><div class="titles"><h1>Roles y permisos</h1><p class="muted" style="margin:0">Control de acceso basado en roles, con mínimo privilegio y segregación de funciones.</p></div><div class="actions"><button type="button" class="btn btn-secondary" id="ro-new">${icon('plus')}Nuevo rol</button><button type="button" class="btn btn-primary" id="ro-save" disabled>${icon('check')}Guardar cambios</button></div></div>
      <section class="card card-flush"><div class="table-wrap"><table class="table"><caption class="sr-only">Matriz de roles y permisos</caption><thead><tr><th>Rol</th><th>Módulos</th><th class="right">Personas</th>${D.permisos.map((p) => `<th style="text-align:center">${p}</th>`).join('')}</tr></thead><tbody>${D.roles.map((r) => `<tr><td><strong>${esc(r.nombre)}</strong><div class="small muted">${esc(r.desc)}</div></td><td>${r.modulos.map((m) => `<span class="badge plain mono">${m}</span>`).join(' ')}</td><td class="num right">${r.usuarios}</td>${D.permisos.map((p, i) => `<td style="text-align:center"><label class="check check-cell"><input type="checkbox" data-r="${r.id}" data-i="${i}" ${D.matriz[r.id][i] ? 'checked' : ''} ${r.id === 'admin' && i === 5 ? 'disabled' : ''} aria-label="${p} para ${esc(r.nombre)}"></label></td>`).join('')}</tr>`).join('')}</tbody></table></div></section>
      <div id="ro-sod" style="margin-top:var(--sp-4)"></div>`,
    mount: (root) => {
      const changes = new Set();
      $$('[data-r]', root).forEach((c) => (c.onchange = () => {
        const k = c.dataset.r + c.dataset.i;
        changes.has(k) ? changes.delete(k) : changes.add(k);
        $('#ro-save', root).disabled = !changes.size;
        $('#ro-save', root).innerHTML = `${icon('check')}Guardar cambios${changes.size ? ` (${changes.size})` : ''}`;
        const conflict = $(`[data-r="conductor"][data-i="3"]`, root).checked || $(`[data-r="finanzas"][data-i="1"]`, root).checked && $(`[data-r="finanzas"][data-i="3"]`, root).checked;
        $('#ro-sod', root).innerHTML = conflict ? L.alert('warning', 'Posible conflicto de segregación de funciones', 'Un mismo rol podría crear y aprobar la misma transacción. Revise antes de guardar.') : '';
      }));
      $('#ro-save', root).onclick = async () => { if (await L.confirm({ title: `¿Guardar ${changes.size} cambio(s) de permisos?`, message: 'Los cambios con impacto operacional quedan pendientes de aprobación por un segundo perfil (RF-17.03).', confirmLabel: 'Enviar a aprobación' })) { changes.clear(); $('#ro-save', root).disabled = true; $('#ro-save', root).innerHTML = `${icon('check')}Guardar cambios`; L.toast('Cambios enviados a aprobación', 'Gerencia de Operaciones debe aprobarlos.', 'success'); } };
      $('#ro-new', root).onclick = () => L.modal({ title: 'Nuevo rol', body: `<div class="field"><label for="nr-n">Nombre del rol</label><input id="nr-n" class="input"></div><div class="field" style="margin-top:12px"><label for="nr-b">Basado en</label><select id="nr-b" class="select">${D.roles.map((r) => `<option>${esc(r.nombre)}</option>`).join('')}</select></div>`, onOpen: (d) => L.bindField($('#nr-n', d), ['required', (v) => (D.roles.some((r) => r.nombre.toLowerCase() === v.toLowerCase()) ? 'Ya existe un rol con ese nombre.' : '')]), actions: [{ label: 'Cancelar' }, { label: 'Crear rol', cls: 'btn-primary', onClick: (api) => { if (!L.validateAll(api.el)) return false; L.toast('Rol creado', $('#nr-n', api.el).value, 'success'); } }] });
    }
  });

  L.route('/admin/parametros', {
    title: 'Parámetros', parent: '/inicio', block: 'Administración', module: 'Registro versionado de parámetros', rf: ['RF-17.02', 'RF-17.03'], actors: ['Jefe de TI', 'Gerente de Finanzas', 'Jefa de Calidad'],
    render: () => `<div class="page-head"><div class="titles"><h1>Parámetros de negocio</h1><p class="muted" style="margin:0">Umbrales, plazos y tolerancias editables sin desarrollo, con versión, vigencia y aprobación de un segundo perfil.</p></div></div>
      ${L.alert('warning', '1 cambio pendiente de su aprobación', 'Umbral de bloqueo de crédito: 10 % → 12 %, propuesto por Camila Fuentes (Finanzas) el 12-11 a las 17:40.', '<button type="button" class="btn btn-secondary btn-sm" id="pa-rej">Rechazar</button><button type="button" class="btn btn-primary btn-sm" id="pa-ok">Aprobar</button>')}
      <div style="margin-top:var(--sp-5)">${D.parametros.map((g, gi) => L.accordionHtml(esc(g.grupo), `<div class="stack">${g.items.map((it) => `<form class="row-between" data-pf="${it.id}" novalidate style="border-bottom:1px solid var(--c-line-soft);padding-bottom:12px"><div style="flex:1 1 260px"><label for="pa-${it.id}" style="font-weight:600">${esc(it.label)}</label><div class="small muted">${esc(it.rf)} · vigente desde 01-10-2026 · versión ${gi + 3}</div></div><div class="field" style="flex:0 0 220px"><div class="input-group"><input id="pa-${it.id}" class="input num" value="${esc(it.valor)}" data-orig="${esc(it.valor)}" aria-describedby="pa-u-${it.id}"><span class="addon" id="pa-u-${it.id}" style="border-left:0;border-right:1px solid var(--c-line);border-radius:0 6px 6px 0">${esc(it.unidad)}</span></div></div><button type="submit" class="btn btn-secondary btn-sm" disabled>Proponer cambio</button></form>`).join('')}</div>`, gi === 0, ` <span class="badge plain" style="margin-left:8px">${g.items.length}</span>`)).join('')}</div>`,
    mount: (root) => {
      $$('[data-pf]', root).forEach((f) => {
        const inp = $('input', f), btn = $('button', f);
        L.bindField(inp, [(v) => (v === '' ? 'Ingrese un valor.' : /^\d{1,2}:\d{2}$/.test(v) || !isNaN(Number(v)) ? '' : 'Debe ser un número.'), (v) => (Number(v) < 0 ? 'No puede ser negativo.' : '')]);
        inp.addEventListener('input', () => (btn.disabled = inp.value === inp.dataset.orig));
        f.onsubmit = async (e) => { e.preventDefault(); if (!inp._validate()) return; if (await L.confirm({ title: 'Proponer cambio de parámetro', message: `«${esc($('label', f).textContent)}»: ${esc(inp.dataset.orig)} → ${esc(inp.value)}. Tiene impacto operacional: otro perfil debe aprobarlo antes de entrar en vigencia (RF-17.03).`, confirmLabel: 'Enviar a aprobación' })) { btn.disabled = true; btn.textContent = 'Pendiente de aprobación'; L.toast('Cambio propuesto', 'Se notificó al perfil aprobador.', 'success'); } };
      });
      const done = (ok) => { $('.alert', root).outerHTML = L.alert(ok ? 'success' : 'info', ok ? 'Cambio aprobado' : 'Cambio rechazado', ok ? 'Nueva versión vigente desde mañana 00:00. Queda en la auditoría.' : 'Se informó a quien lo propuso.'); };
      $('#pa-ok', root).onclick = async () => { if (await L.confirm({ title: '¿Aprobar el cambio?', message: 'El umbral de bloqueo de crédito pasará de 10 % a 12 % para todos los preventistas.', confirmLabel: 'Aprobar' })) { done(true); L.toast('Parámetro aprobado', '', 'success'); } };
      $('#pa-rej', root).onclick = () => done(false);
    }
  });

  L.route('/admin/auditoria', {
    title: 'Auditoría', parent: '/inicio', block: 'Administración', module: 'Registro de auditoría inalterable', rf: ['RF-17.04', 'RF-17.05'], actors: ['Jefe de TI', 'Gerencias'],
    render: () => `<div class="page-head"><div class="titles"><h1>Auditoría</h1><p class="muted" style="margin:0">Toda operación que crea, modifica o elimina información, con persona, fecha, origen y detalle.</p></div><div class="actions"><button type="button" class="btn btn-secondary" id="au-json">${icon('download')}JSON</button><button type="button" class="btn btn-primary" id="au-csv">${icon('download')}Exportar CSV</button></div></div>
      <section class="card" style="margin-bottom:var(--sp-4)"><div class="form-grid" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr))"><div class="field"><label for="au-d1">Desde</label><input id="au-d1" class="input" type="date" value="2026-11-06"></div><div class="field"><label for="au-d2">Hasta</label><input id="au-d2" class="input" type="date" value="2026-11-13"></div><div class="field combo"><label for="au-p">Persona</label><input id="au-p" class="input" placeholder="Cualquiera"></div><div class="field"><label for="au-o">Operación</label><select id="au-o" class="select"><option value="">Todas</option>${[...new Set(D.auditoria.map((a) => a.operacion))].map((o) => `<option>${o}</option>`).join('')}</select></div></div><div id="au-err" aria-live="polite"></div></section>
      <div class="card card-flush" id="au-t"></div>`,
    mount: (root) => {
      const rows = () => {
        const d1 = $('#au-d1', root).value, d2 = $('#au-d2', root).value, p = $('#au-p', root).value.toLowerCase(), o = $('#au-o', root).value;
        return D.auditoria.filter((a) => a.fecha.slice(0, 10) >= d1 && a.fecha.slice(0, 10) <= d2 && (!p || a.persona.toLowerCase().includes(p)) && (!o || a.operacion === o));
      };
      const tbl = L.dataTable($('#au-t', root), {
        id: 'aut', caption: 'Registro de auditoría', rows, per: 12, searchKeys: ['detalle', 'entidad', 'id'], searchPlaceholder: 'Buscar en el detalle', sort: 'fecha', dir: 'desc',
        filters: [{ key: 'entidad', label: 'Entidad', options: [...new Set(D.auditoria.map((a) => a.entidad))] }, { key: 'origen', label: 'Origen', options: ['Consola web', 'App Kotlin', 'API', 'Portal de clientes'] }],
        columns: [{ key: 'fecha', label: 'Fecha y hora', render: (r) => `<span class="mono small">${fmt.dt(r.fecha)}</span>` }, { key: 'persona', label: 'Persona' }, { key: 'operacion', label: 'Operación', render: (r) => L.badge(r.operacion, r.operacion === 'Eliminación' ? 'danger' : r.operacion === 'Aprobación' ? 'success' : r.operacion === 'Modificación' ? 'warning' : 'info') }, { key: 'entidad', label: 'Entidad' }, { key: 'detalle', label: 'Detalle', wrap: true }, { key: 'origen', label: 'Origen', render: (r) => `${esc(r.origen)}<div class="small muted mono">${r.ip}</div>` }]
      });
      L.combobox($('#au-p', root), () => D.usuarios.map((u) => ({ label: u.nombre, meta: roleName(u.rol) })), { onSelect: () => tbl.draw() });
      ['#au-d1', '#au-d2', '#au-o', '#au-p'].forEach((s) => $(s, root).addEventListener('change', () => {
        const bad = $('#au-d1', root).value > $('#au-d2', root).value;
        $('#au-err', root).innerHTML = bad ? L.alert('danger', 'Rango de fechas no válido', 'La fecha «Desde» debe ser anterior o igual a «Hasta».') : '';
        if (!bad) { tbl.state.page = 1; tbl.draw(); }
      }));
      const cols = [{ label: 'Fecha', key: 'fecha' }, { label: 'Persona', key: 'persona' }, { label: 'Operación', key: 'operacion' }, { label: 'Entidad', key: 'entidad' }, { label: 'Detalle', key: 'detalle' }, { label: 'Origen', key: 'origen' }, { label: 'IP', key: 'ip' }];
      $('#au-csv', root).onclick = (e) => L.busy(e.currentTarget, () => { L.download('auditoria.csv', L.toCSV(tbl.filtered(), cols)); L.toast('Auditoría exportada', `${tbl.filtered().length} registros con el filtro aplicado (CSV UTF-8).`, 'success'); }, 700);
      $('#au-json', root).onclick = (e) => L.busy(e.currentTarget, () => { L.download('auditoria.json', JSON.stringify(tbl.filtered(), null, 2), 'application/json'); L.toast('Auditoría exportada', 'Formato JSON.', 'success'); }, 700);
    }
  });
})(window.LFX);
