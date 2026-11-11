/* Autenticación e incorporación: inicio de sesión unificado (SSO), registro en 5 pasos,
   recuperación de acceso, segundo factor y tablero de primer ingreso con recorrido guiado. */
(function (L) {
  const { esc, icon, $, $$, data: D } = L;

  const stepperHtml = (labels, cur, clickable = false) => `<ol class="stepper" aria-label="Progreso">${labels.map((l, i) => `<li class="${i < cur ? 'done' : i === cur ? 'current' : ''}"><${clickable && i < cur ? 'button type="button"' : 'div'} class="step" ${clickable && i < cur ? `data-goto="${i}"` : ''} ${i === cur ? 'aria-current="step"' : ''}><span class="bar"></span><span class="lbl">${esc(l)}<span class="sr-only">${i < cur ? ' (completado)' : i === cur ? ' (paso actual)' : ''}</span></span></${clickable && i < cur ? 'button' : 'div'}></li>`).join('')}</ol>`;
  L.stepperHtml = stepperHtml;

  const passwordField = (id, label, hint = true) => `<div class="field"><label for="${id}">${label} <span class="req" aria-hidden="true">*</span></label>
    <div class="input-wrap">${icon('lock')}<input id="${id}" class="input" type="password" autocomplete="${id.includes('new') || id.includes('rg') ? 'new-password' : 'current-password'}" required style="padding-right:52px"><span class="suffix"><button type="button" class="btn btn-tertiary btn-icon" data-reveal="${id}" aria-label="Mostrar contraseña" aria-pressed="false">${icon('eye')}</button></span></div>
    ${hint ? `<div class="progress" style="margin-top:6px" aria-hidden="true"><span data-strength="${id}" style="width:0%"></span></div><span class="hint" data-strength-txt="${id}">Mínimo 10 caracteres, una mayúscula y un número.</span>` : ''}</div>`;

  const wirePasswords = (root) => {
    $$('[data-reveal]', root).forEach((b) => (b.onclick = () => { const i = $('#' + b.dataset.reveal, root); const show = i.type === 'password'; i.type = show ? 'text' : 'password'; b.setAttribute('aria-pressed', show); b.setAttribute('aria-label', show ? 'Ocultar contraseña' : 'Mostrar contraseña'); b.innerHTML = icon(show ? 'eye-off' : 'eye'); }));
    $$('[data-strength]', root).forEach((bar) => {
      const inp = $('#' + bar.dataset.strength, root);
      const txt = $(`[data-strength-txt="${bar.dataset.strength}"]`, root);
      inp.addEventListener('input', () => {
        const v = inp.value;
        const sc = (v.length >= 10) + /[A-Z]/.test(v) + /\d/.test(v) + /[^A-Za-z0-9]/.test(v) + (v.length >= 14);
        bar.style.width = sc * 20 + '%';
        bar.parentElement.className = 'progress ' + (sc <= 2 ? 'danger' : sc <= 3 ? '' : 'dark');
        txt.textContent = !v ? 'Mínimo 10 caracteres, una mayúscula y un número.' : `Seguridad: ${['muy baja', 'muy baja', 'baja', 'media', 'alta', 'muy alta'][sc]}`;
      });
    });
  };

  /* ---------- Inicio de sesión unificado ---------- */
  L.route('/ingresar', {
    title: 'Ingresar', layout: 'public', parent: '/', block: 'Autenticación e incorporación', module: 'Base compartida (Keycloak)', rf: ['RF-15.01', 'RF-15.02', 'RF-12.26', 'RF-06.08'], actors: ['Todos los perfiles'],
    render: () => `<div class="auth-wrap"><div class="card auth-card" style="padding:var(--sp-6)">
      <div class="row" style="margin-bottom:var(--sp-4)">${L.logo('brand-logo')}<div><h1 style="margin:0">Ingresar</h1><p class="muted small" style="margin:0">Un solo acceso para portal, consolas y aplicaciones</p></div></div>
      <section aria-labelledby="qa-h" class="stack">
        <h2 id="qa-h" style="font-size:var(--fs-lg);margin:0">Ingresar con un perfil predeterminado</h2>
        <p class="small muted" style="margin:0">Sin contraseña. Hay un perfil por cada actor del sistema.</p>
        <div class="field"><label for="li-prof">Actor del sistema</label>${L.profileSelectHtml('li-prof', 'evaluador')}</div>
        <div class="card" id="li-card" style="box-shadow:none;padding:var(--sp-4)" aria-live="polite">${L.profileCard('evaluador')}</div>
        <button type="button" class="btn btn-primary btn-block big-btn" id="li-go">${icon('arrow-right')}Ingresar como este perfil</button>
      </section>
      <hr>
      ${L.accordionHtml(`${icon('lock')} Ingresar con credenciales`, `
        <div class="segmented" role="tablist" aria-label="Método de ingreso" style="width:100%;margin-bottom:var(--sp-4)">
          <button type="button" role="tab" aria-selected="true" data-mode="pwd" style="flex:1">Correo y contraseña</button>
          <button type="button" role="tab" aria-selected="false" data-mode="otp" style="flex:1">Conductor externo</button>
        </div>
        <div id="login-err"></div>
        <form id="f-pwd" novalidate class="stack">
          <div class="field"><label for="li-e">Correo electrónico <span class="req" aria-hidden="true">*</span></label><div class="input-wrap">${icon('mail')}<input id="li-e" class="input" type="email" autocomplete="username" required placeholder="nombre@empresa.cl"></div></div>
          ${passwordField('li-p', 'Contraseña', false)}
          <div class="row-between"><label class="check"><input type="checkbox" id="li-r" checked> Recordar este equipo</label><a href="#/recuperar">¿Olvidó su contraseña?</a></div>
          <button class="btn btn-secondary btn-block big-btn" type="submit">Ingresar</button>
          <p class="hint" style="margin:0">Simulación: cualquier contraseña de 4 o más caracteres funciona; «error» muestra el manejo de credenciales incorrectas. Los perfiles de consola piden segundo factor.</p>
        </form>
        <form id="f-otp" novalidate class="stack" hidden>
          <p class="small muted" style="margin:0">Para conductores de empresas transportistas sin correo corporativo. El jefe de flota solicita un código de un solo uso para el alta inicial, que exige conexión. Después se ingresa con el PIN personal y la asignación aprobada por despacho.</p>
          <fieldset><legend class="sr-only">Tipo de ingreso</legend><div class="options-row"><label class="radio"><input type="radio" name="ot-modo" value="alta" checked> Alta inicial con código (OTP)</label><label class="radio"><input type="radio" name="ot-modo" value="pin"> Ingreso con PIN personal</label></div></fieldset>
          <div class="field"><label for="ot-r">RUT del conductor <span class="req" aria-hidden="true">*</span></label><input id="ot-r" class="input mono" inputmode="text" placeholder="12.345.678-5" required></div>
          <div class="field" id="ot-c-wrap"><label for="ot-c">Código de un solo uso <span class="req" aria-hidden="true">*</span></label><input id="ot-c" class="input mono" inputmode="numeric" maxlength="8" placeholder="8 dígitos" required></div>
          <div class="field" id="ot-p-wrap" hidden><label for="ot-p">PIN personal <span class="req" aria-hidden="true">*</span></label><input id="ot-p" class="input mono" type="password" inputmode="numeric" maxlength="6" placeholder="4 a 6 dígitos"></div>
          <button class="btn btn-secondary btn-block big-btn" type="submit">Ingresar</button>
          <p class="hint" style="margin:0" id="ot-hint">Simulación: el código emitido para Óscar Vidal (RUT 15.482.337-9) es <span class="mono">48213705</span>. Otro código se rechaza; <span class="mono">00000000</span> simula un código vencido.</p>
        </form>`)}
      <p class="small muted" style="margin:var(--sp-4) 0 0;text-align:center">¿Su cadena aún no tiene cuenta? <a href="#/registro">Solicite una cuenta</a>. Los almacenes activan la suya con su preventista.</p>
    </div></div>`,
    mount: (root) => {
      // Acceso directo por perfil
      const sel = $('#li-prof', root);
      sel.onchange = () => ($('#li-card', root).innerHTML = L.profileCard(sel.value));
      $('#li-go', root).onclick = (e) => L.busy(e.currentTarget, () => L.enterAs(sel.value), 500);

      // Ingreso con credenciales (se conserva el sistema completo)
      let attempts = 3;
      const fp = $('#f-pwd', root), fo = $('#f-otp', root), err = $('#login-err', root);
      $$('[data-mode]', root).forEach((b) => (b.onclick = () => { $$('[data-mode]', root).forEach((x) => x.setAttribute('aria-selected', x === b)); fp.hidden = b.dataset.mode !== 'pwd'; fo.hidden = b.dataset.mode === 'pwd'; err.innerHTML = ''; }));
      wirePasswords(root);
      L.bindField($('#li-e', root), ['email']);
      L.bindField($('#li-p', root), [(v) => (v.length >= 4 ? '' : 'Ingrese su contraseña.')]);
      L.bindField($('#ot-r', root), ['rut'], { okMsg: 'RUT válido' });
      L.bindField($('#ot-c', root), [(v) => (/^\d{8}$/.test(v) ? '' : 'El código tiene 8 dígitos.')]);
      $('#ot-r', root).addEventListener('blur', (e) => { if (L.rut.valid(e.target.value)) e.target.value = L.rut.format(e.target.value); });
      const finish = (pid) => {
        L.signIn(pid);
        const p = L.profile(pid);
        const next = L.store.get('next', '') || '/inicio';
        L.store.set('next', '');
        if (p.mfa) { L.store.set('pending2fa', next); L.go('/verificacion'); }
        else if (L.session().first) L.go('/bienvenida');
        else L.go(next);
      };
      fp.onsubmit = (e) => {
        e.preventDefault();
        err.innerHTML = '';
        if (!L.validateAll(fp)) return;
        L.busy($('[type=submit]', fp), () => {
          if ($('#li-p', root).value.toLowerCase() === 'error') {
            attempts--;
            err.innerHTML = L.alert('danger', 'Correo o contraseña incorrectos', attempts > 0 ? `Le quedan ${attempts} intentos antes de que la cuenta se bloquee por 15 minutos. ¿<a href="#/recuperar">Recuperar acceso</a>?` : 'La cuenta quedó bloqueada por 15 minutos por seguridad. Use «¿Olvidó su contraseña?» para recuperarla.');
            $('#li-p', root).focus();
            return;
          }
          const mail = $('#li-e', root).value.toLowerCase();
          const u = D.usuarios.find((x) => x.correo === mail);
          const pid = (u && D.profiles.find((pp) => pp.name === u.nombre)?.id) || (mail.includes('almacen') ? 'cliente' : 'evaluador');
          L.toast('Identidad verificada', 'Sesión única para todos los módulos.', 'success');
          finish(pid);
        }, 1100);
      };
      $$('[name=ot-modo]', fo).forEach((r) => (r.onchange = () => {
        const pin = $('[name=ot-modo]:checked', fo).value === 'pin';
        $('#ot-c-wrap', fo).hidden = pin; $('#ot-p-wrap', fo).hidden = !pin;
        $('#ot-c', fo).required = !pin;
        $('#ot-hint', fo).innerHTML = pin ? 'Simulación: PIN <span class="mono">4821</span> para Óscar Vidal (RUT 15.482.337-9).' : 'Simulación: el código emitido para Óscar Vidal (RUT 15.482.337-9) es <span class="mono">48213705</span>. Otro código se rechaza; <span class="mono">00000000</span> simula un código vencido.';
      }));
      fo.onsubmit = (e) => {
        e.preventDefault();
        if (!L.validateAll(fo)) return;
        const pinMode = $('[name=ot-modo]:checked', fo).value === 'pin';
        const code = $('#ot-c', fo).value, rut = L.rut.clean($('#ot-r', fo).value);
        if (pinMode) {
          const pin = $('#ot-p', fo).value;
          if (!/^\d{4,6}$/.test(pin)) { err.innerHTML = L.alert('warning', 'PIN incompleto', 'Ingrese su PIN personal de 4 a 6 dígitos.'); $('#ot-p', fo).focus(); return; }
          L.busy($('[type=submit]', fo), () => {
            if (rut !== '154823379' || pin !== '4821') { err.innerHTML = L.alert('danger', 'RUT o PIN incorrecto', 'Revise los datos. Si no recuerda su PIN, pida al jefe de flota un nuevo alta con código.'); $('#ot-p', fo).focus(); return; }
            const asg = ((L.store.get('asignaciones', {}) || {}) || {})['R-09'];
            if (asg && asg.estado !== 'Aprobada') { err.innerHTML = L.alert('warning', 'Asignación pendiente de despacho', 'Su asignación conductor–vehículo–turno aún no está aprobada. Despacho debe aprobarla antes de la salida.'); return; }
            err.innerHTML = ''; L.toast('Asignación vigente', 'Vence 30 min después del fin de la ruta, sin superar 16 h. No se renueva sin conexión.', 'success'); finish('conductor-ext');
          }, 800);
          return;
        }
        L.busy($('[type=submit]', fo), () => {
          if (code === '00000000') { err.innerHTML = L.alert('danger', 'Código vencido', 'Este código ya no es válido: sirve una sola vez, para el alta. Pida uno nuevo a su jefe de flota.'); $('#ot-c', fo).focus(); return; }
          if (code !== '48213705' || rut !== '154823379') { err.innerHTML = L.alert('danger', 'Código o RUT incorrecto', 'El código no corresponde a este RUT. Revise ambos datos o pida un código nuevo a su jefe de flota.'); $('#ot-c', fo).focus(); return; }
          err.innerHTML = ''; L.toast('Alta completada', 'El código de un solo uso queda consumido. Desde ahora ingresa con su PIN personal; la asignación vence 30 min después del fin de la ruta, sin superar 16 h.', 'success'); finish('conductor-ext');
        }, 1000);
      };
    }
  });

  /* ---------- Segundo factor ---------- */
  L.route('/verificacion', {
    title: 'Verificación en dos pasos', layout: 'public', parent: '/ingresar', block: 'Autenticación e incorporación', module: 'Base compartida (Keycloak)', rf: ['RF-15.03'], actors: ['Perfiles administradores y de consola'],
    render: () => {
      const p = L.me();
      const portalSet = new Set(['cliente', 'cliente-moderno', 'transportista', 'proveedor']);
      return `<div class="auth-wrap"><form class="card auth-card" id="f2" novalidate style="padding:var(--sp-6)">
        <span class="modal-icon info" style="margin-bottom:var(--sp-3)">${icon('fingerprint')}</span>
        <h1>Verificación en dos pasos</h1>
        <p class="muted">Su perfil (${esc(p ? p.role : '')}) exige un segundo factor. ${p?.id === 'ti' ? 'La administración usa una clave FIDO2 (llave de seguridad).' : portalSet.has(p?.id) ? 'En los portales se usa una aplicación TOTP o una clave de acceso.' : 'Ingrese el código de 6 dígitos de su aplicación autenticadora.'}</p>
        <div class="segmented" role="radiogroup" aria-label="Método" style="margin-bottom:var(--sp-4)"><button type="button" role="radio" aria-checked="true" aria-pressed="true" data-m="app">${icon('phone', 'icon-sm')} App autenticadora</button><button type="button" role="radio" aria-checked="false" aria-pressed="false" data-m="sms">${icon('mail', 'icon-sm')} SMS al +56 9 •••• 4821</button><button type="button" role="radio" aria-checked="false" aria-pressed="false" data-m="key">${icon('key', 'icon-sm')} Llave de seguridad o clave de acceso</button></div>
        <div id="fido" hidden class="card" style="box-shadow:none;margin-bottom:var(--sp-3)"><p class="small" style="margin-top:0">Factor resistente a suplantación (FIDO2 / WebAuthn): toque su llave de seguridad o confirme con la huella o el rostro en su equipo.</p><button type="button" class="btn btn-primary btn-block big-btn" id="fido-go">${icon('fingerprint')}Usar llave de seguridad</button></div>
        <fieldset><legend class="sr-only">Código de verificación</legend>
          <div class="row" style="gap:8px;flex-wrap:nowrap" id="otp">${Array.from({ length: 6 }, (_, i) => `<input class="input mono" inputmode="numeric" maxlength="1" aria-label="Dígito ${i + 1} de 6" style="width:48px;height:56px;text-align:center;font-size:var(--fs-xl);padding:0" autocomplete="${i === 0 ? 'one-time-code' : 'off'}">`).join('')}</div>
        </fieldset>
        <div id="f2-msg" aria-live="polite" style="margin-top:var(--sp-3)"></div>
        <p class="hint">Demostración: cualquier código de 6 dígitos es válido; «000000» muestra el error.</p>
        <button class="btn btn-primary btn-block big-btn" type="submit" style="margin-top:var(--sp-3)">Verificar e ingresar</button>
        <div class="row-between" style="margin-top:var(--sp-3)"><button type="button" class="btn btn-tertiary" id="resend" disabled>Reenviar código en 30 s</button><a href="#/ingresar" class="btn btn-tertiary">Usar otra cuenta</a></div>
      </form></div>`;
    },
    mount: (root) => {
      if (!L.session()) { L.go('/ingresar'); return; }
      // SD4 Capa 7: TI usa FIDO2; los portales usan TOTP o clave de acceso (sin SMS)
      const who = L.me()?.id;
      const portal = ['cliente', 'cliente-moderno', 'transportista', 'proveedor'].includes(who);
      if (who === 'ti' || portal) $('[data-m=sms]', root).remove();
      if (who === 'ti') $('[data-m=app]', root).remove();
      const ins = $$('#otp input', root);
      ins.forEach((inp, i) => {
        inp.addEventListener('input', () => { inp.value = inp.value.replace(/\D/g, ''); if (inp.value && ins[i + 1]) ins[i + 1].focus(); });
        inp.addEventListener('keydown', (e) => { if (e.key === 'Backspace' && !inp.value && ins[i - 1]) ins[i - 1].focus(); });
        inp.addEventListener('paste', (e) => { const t = (e.clipboardData.getData('text') || '').replace(/\D/g, '').slice(0, 6); if (t.length) { e.preventDefault(); t.split('').forEach((c, j) => (ins[j].value = c)); ins[Math.min(5, t.length)].focus(); } });
      });
      ins[0].focus();
      const modes = $$('[data-m]', root);
      modes.forEach((b) => (b.onclick = () => { $$('[data-m]', root).forEach((x) => { x.setAttribute('aria-checked', x === b); x.setAttribute('aria-pressed', x === b); }); if (b.dataset.m === 'sms') L.toast('Código enviado', 'Revise el SMS en su teléfono terminado en 4821.', 'info'); $('#fido', root).hidden = b.dataset.m !== 'key'; $('#otp', root).closest('fieldset').hidden = b.dataset.m === 'key'; $('#f2 [type=submit]', root).hidden = b.dataset.m === 'key'; }));
      if (who === 'ti') modes[0].click();
      $('#fido-go', root).onclick = (e) => L.busy(e.currentTarget, () => { L.toast('Llave de seguridad verificada', 'Segundo factor FIDO2 aceptado.', 'success'); const next = L.store.get('pending2fa', '/inicio'); L.go(L.session().first ? '/bienvenida' : next); }, 1400);
      let s = 30;
      const rs = $('#resend', root);
      const t = L.interval(() => { s--; rs.textContent = s > 0 ? `Reenviar código en ${s} s` : 'Reenviar código'; if (s <= 0) { rs.disabled = false; clearInterval(t); } }, 1000);
      rs.onclick = () => { L.toast('Código reenviado', '', 'info'); rs.disabled = true; };
      $('#f2', root).onsubmit = (e) => {
        e.preventDefault();
        const code = ins.map((i) => i.value).join('');
        const msg = $('#f2-msg', root);
        if (code.length < 6) { msg.innerHTML = L.alert('warning', 'Faltan dígitos', 'Complete los 6 dígitos del código.'); ins.find((i) => !i.value)?.focus(); return; }
        L.busy($('[type=submit]', root), () => {
          if (code === '000000') { msg.innerHTML = L.alert('danger', 'El código no es válido o expiró', 'Revise que la hora de su teléfono esté sincronizada o pida un código nuevo.'); ins.forEach((i) => (i.value = '')); ins[0].focus(); return; }
          L.toast('Segundo factor verificado', '', 'success');
          const next = L.store.get('pending2fa', '/inicio');
          L.go(L.session().first ? '/bienvenida' : next);
        }, 900);
      };
    }
  });

  /* ---------- Recuperación de acceso ---------- */
  L.route('/recuperar', {
    title: 'Recuperar acceso', layout: 'public', parent: '/ingresar', block: 'Autenticación e incorporación', module: 'Base compartida (Keycloak)', rf: ['RF-12.27'], actors: ['Todos los perfiles'],
    render: () => `<div class="auth-wrap"><div class="card auth-card" style="padding:var(--sp-6)" id="rc">
      ${stepperHtml(['Correo', 'Código', 'Nueva contraseña'], 0)}
      <form id="rc1" novalidate class="stack">
        <h1>Recuperar acceso</h1><p class="muted" style="margin:0">Le enviaremos un enlace y un código para crear una nueva contraseña.</p>
        <div class="field"><label for="rc-e">Correo registrado <span class="req" aria-hidden="true">*</span></label><div class="input-wrap">${icon('mail')}<input id="rc-e" class="input" type="email" autocomplete="email" required></div></div>
        <button class="btn btn-primary btn-block big-btn" type="submit">Enviar instrucciones</button>
        <a href="#/ingresar" class="btn btn-tertiary">${icon('arrow-left')}Volver a ingresar</a>
      </form>
      <form id="rc2" novalidate class="stack" hidden>
        <h1>Revise su correo</h1><p class="muted" style="margin:0">Enviamos un código de 6 dígitos a <strong id="rc-mail"></strong>. Vence en 15 minutos.</p>
        <div class="field"><label for="rc-c">Código recibido <span class="req" aria-hidden="true">*</span></label><input id="rc-c" class="input mono" inputmode="numeric" maxlength="6" required></div>
        <button class="btn btn-primary btn-block big-btn" type="submit">Continuar</button>
      </form>
      <form id="rc3" novalidate class="stack" hidden>
        <h1>Cree una nueva contraseña</h1>
        ${passwordField('rc-new', 'Nueva contraseña')}
        <div class="field"><label for="rc-new2">Repita la contraseña <span class="req" aria-hidden="true">*</span></label><input id="rc-new2" class="input" type="password" autocomplete="new-password" required></div>
        <button class="btn btn-primary btn-block big-btn" type="submit">Guardar contraseña</button>
      </form>
    </div></div>`,
    mount: (root) => {
      const step = (n) => { ['rc1', 'rc2', 'rc3'].forEach((id, i) => ($('#' + id, root).hidden = i !== n)); $('.stepper', root).outerHTML = stepperHtml(['Correo', 'Código', 'Nueva contraseña'], n); $(`#rc${n + 1} input`, root)?.focus(); };
      wirePasswords(root);
      L.bindField($('#rc-e', root), ['email']);
      L.bindField($('#rc-c', root), [(v) => (/^\d{6}$/.test(v) ? '' : 'El código tiene 6 dígitos.')]);
      L.bindField($('#rc-new', root), ['password']);
      L.bindField($('#rc-new2', root), [(v) => (v === $('#rc-new', root).value ? '' : 'Las contraseñas no coinciden.')]);
      $('#rc1', root).onsubmit = (e) => { e.preventDefault(); if (!L.validateAll(e.target)) return; L.busy($('#rc1 [type=submit]', root), () => { $('#rc-mail', root).textContent = $('#rc-e', root).value; L.toast('Correo enviado', 'Si la cuenta existe, recibirá las instrucciones.', 'info'); step(1); }); };
      $('#rc2', root).onsubmit = (e) => { e.preventDefault(); if (!L.validateAll(e.target)) return; L.busy($('#rc2 [type=submit]', root), () => step(2), 700); };
      $('#rc3', root).onsubmit = (e) => { e.preventDefault(); if (!L.validateAll(e.target)) return; L.busy($('#rc3 [type=submit]', root), () => { $('#rc', root).innerHTML = L.empty('done', 'Contraseña actualizada', 'Por seguridad cerramos las sesiones abiertas en otros equipos.', '<a class="btn btn-primary" href="#/ingresar">Ingresar ahora</a>'); }); };
    }
  });

  /* ---------- Registro de cliente en 5 pasos ---------- */
  const regiones = { "O'Higgins": ['Rancagua', 'San Fernando', 'Santa Cruz'], Maule: ['Talca', 'Curicó', 'Linares', 'Cauquenes', 'Constitución', 'Molina', 'San Javier', 'Parral', 'Empedrado'], Ñuble: ['Chillán', 'San Carlos', 'Bulnes'], 'Biobío': ['Concepción', 'Los Ángeles', 'Talcahuano'], 'La Araucanía': ['Temuco', 'Angol', 'Victoria'] };
  const STEPS = ['Empresa', 'Local y recepción', 'Contacto', 'Documentos', 'Acceso y confirmación'];

  L.route('/registro', {
    title: 'Registro de cliente', layout: 'public', parent: '/', block: 'Autenticación e incorporación', module: 'Portal de clientes (M11 canal, M3)', rf: ['RF-12.25', 'RF-18.02', 'RF-17.08'], actors: ['Cliente del canal tradicional', 'Cliente del canal moderno'],
    render: () => `<div class="auth-wrap"><div class="card auth-card wide" style="padding:var(--sp-6)" id="rg">
      <span class="page-kicker">Solicitud de cuenta · 5 pasos</span>
      <h1 id="rg-title">Datos de la empresa</h1>
      ${stepperHtml(STEPS, 0, true)}
      <form id="rg-f" novalidate>
        <section data-step="0" class="form-grid">
          <div class="field"><label for="rg-rut">RUT de la empresa <span class="req" aria-hidden="true">*</span></label><input id="rg-rut" class="input mono" required placeholder="76.123.456-7" aria-describedby="rg-rut-h"><span class="hint" id="rg-rut-h">Validamos el dígito verificador mientras escribe.</span></div>
          <div class="field"><label for="rg-rs">Razón social <span class="req" aria-hidden="true">*</span></label><input id="rg-rs" class="input" required autocomplete="organization"></div>
          <div class="field"><label for="rg-nf">Nombre de fantasía</label><input id="rg-nf" class="input" placeholder="Ej.: Almacén Doña Rosa"></div>
          <div class="field"><label for="rg-giro">Giro <span class="req" aria-hidden="true">*</span></label><select id="rg-giro" class="select" required><option value="">Seleccione…</option><option>Almacén de barrio</option><option>Minimarket</option><option>Botillería</option><option>Restaurante o casino</option><option>Supermercado</option><option>Panadería</option></select></div>
          <div class="full" id="rg-rut-msg"></div>
          <fieldset class="full"><legend>Canal <span class="req" aria-hidden="true">*</span></legend><div class="options-row"><label class="radio"><input type="radio" name="rg-canal" value="Moderno" checked> Moderno</label></div><span class="hint">El autorregistro es del canal moderno (RF-12.25). Los almacenes del canal tradicional activan su cuenta, si la desean, en la visita de su preventista con un código por SMS; la compra asistida sigue sin cuenta.</span></fieldset>
        </section>
        <section data-step="1" class="form-grid" hidden>
          <div class="field"><label for="rg-reg">Región <span class="req" aria-hidden="true">*</span></label><select id="rg-reg" class="select" required><option value="">Seleccione…</option>${Object.keys(regiones).map((r) => `<option>${esc(r)}</option>`).join('')}</select></div>
          <div class="field"><label for="rg-com">Comuna <span class="req" aria-hidden="true">*</span></label><select id="rg-com" class="select" required disabled><option value="">Primero elija la región</option></select></div>
          <div class="field full combo"><label for="rg-dir">Dirección del local <span class="req" aria-hidden="true">*</span></label><div class="input-wrap">${icon('pin')}<input id="rg-dir" class="input" required placeholder="Escriba calle y número"></div><span class="hint">Sugerencias de direcciones normalizadas para el ruteo.</span></div>
          <fieldset class="full"><legend>Días en que puede recibir <span class="req" aria-hidden="true">*</span></legend><div class="options-row" id="rg-dias">${['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'].map((d, i) => `<label class="check"><input type="checkbox" value="${d}" ${i < 5 ? 'checked' : ''}> ${d}</label>`).join('')}</div><div class="field-msg error" id="rg-dias-err" aria-live="polite"></div></fieldset>
          <div class="field"><label for="rg-desde">Recibe desde <span class="req" aria-hidden="true">*</span></label><input id="rg-desde" class="input" type="time" value="09:00" required></div>
          <div class="field"><label for="rg-hasta">Recibe hasta <span class="req" aria-hidden="true">*</span></label><input id="rg-hasta" class="input" type="time" value="13:00" required></div>
          <div class="full">${L.alert('info', 'Ventana de recepción', 'Con esta ventana el planificador secuencia sus entregas y le avisamos por SMS una ventana de 30 minutos.')}</div>
        </section>
        <section data-step="2" class="form-grid" hidden>
          <div class="field"><label for="rg-cn">Nombre de contacto <span class="req" aria-hidden="true">*</span></label><input id="rg-cn" class="input" required autocomplete="name"></div>
          <div class="field"><label for="rg-cargo">Cargo</label><select id="rg-cargo" class="select"><option>Dueña o dueño</option><option>Administrador</option><option>Encargado de compras</option></select></div>
          <div class="field"><label for="rg-ce">Correo corporativo <span class="req" aria-hidden="true">*</span></label><input id="rg-ce" class="input" type="email" required autocomplete="email"></div>
          <div class="field"><label for="rg-tel">Teléfono móvil <span class="req" aria-hidden="true">*</span></label><div class="input-group"><span class="addon">+56</span><input id="rg-tel" class="input" inputmode="tel" required placeholder="9 1234 5678" autocomplete="tel-national"></div></div>
          <fieldset class="full"><legend>¿Cómo quiere recibir avisos de entrega?</legend><div class="options-row">${[['SMS', true], ['Correo electrónico', true], ['WhatsApp', false], ['Notificación en la app', false]].map(([c, on]) => `<label class="check"><input type="checkbox" ${on ? 'checked' : ''}> ${c}</label>`).join('')}</div></fieldset>
        </section>
        <section data-step="3" hidden>
          <p class="muted">Adjunte la carpeta tributaria y la patente municipal. Formatos PDF, JPG o PNG, máximo 10 MB cada uno.</p>
          <div class="dropzone" id="rg-drop">${icon('upload', 'icon-lg')}<div><strong>Arrastre los archivos aquí</strong> o haga clic para buscarlos</div><span class="small">PDF, JPG o PNG · máx. 10 MB</span></div>
          <div class="row" style="margin-top:var(--sp-3)"><button type="button" class="btn btn-secondary btn-sm" id="rg-sample">${icon('file', 'icon-sm')}Usar archivos de ejemplo</button><span class="hint">Para la demostración, sin necesidad de archivos propios.</span></div>
          <div id="rg-docs-err" aria-live="polite" style="margin-top:var(--sp-3)"></div>
        </section>
        <section data-step="4" hidden>
          <div class="form-grid">
            <div class="field full"><label for="rg-user">Correo de acceso</label><input id="rg-user" class="input" type="email" readonly></div>
            ${passwordField('rg-pw', 'Contraseña')}
            <div class="field"><label for="rg-pw2">Repita la contraseña <span class="req" aria-hidden="true">*</span></label><input id="rg-pw2" class="input" type="password" autocomplete="new-password" required></div>
          </div>
          <h2 style="margin-top:var(--sp-5)">Revise sus datos</h2>
          <div id="rg-sum" class="grid grid-2"></div>
          <div class="field" style="margin-top:var(--sp-4)"><label class="check"><input type="checkbox" id="rg-terms" required> Acepto los <button type="button" class="btn btn-tertiary btn-sm" id="rg-terms-open" style="padding:0 4px;min-height:0">términos de uso y la política de privacidad</button></label></div>
        </section>
        <div class="row-between" style="margin-top:var(--sp-5);border-top:1px solid var(--c-line-soft);padding-top:var(--sp-4)">
          <button type="button" class="btn btn-secondary" id="rg-back">${icon('arrow-left')}Atrás</button>
          <span class="small muted" id="rg-count" aria-live="polite">Paso 1 de 5</span>
          <button type="submit" class="btn btn-primary" id="rg-next">Continuar${icon('arrow-right')}</button>
        </div>
      </form>
    </div></div>`,
    mount: (root) => {
      let cur = 0;
      const f = $('#rg-f', root);
      const secs = $$('[data-step]', f);
      const titles = ['Datos de la empresa', 'Local y recepción', 'Persona de contacto', 'Documentos de respaldo', 'Acceso y confirmación'];
      const rutIn = $('#rg-rut', root);
      L.bindField(rutIn, ['rut'], { okMsg: 'RUT válido' });
      rutIn.addEventListener('input', () => { const c = L.rut.clean(rutIn.value); if (c.length >= 2) { const pos = rutIn.value.length; rutIn.value = L.rut.format(c); if (pos === rutIn.value.length) rutIn.setSelectionRange(pos, pos); } });
      L.bindField($('#rg-rs', root), ['required']);
      L.bindField($('#rg-giro', root), ['required']);
      const reg = $('#rg-reg', root), com = $('#rg-com', root);
      L.bindField(reg, ['required']);
      L.bindField(com, ['required']);
      reg.onchange = () => { com.disabled = !reg.value; com.innerHTML = `<option value="">Seleccione…</option>${(regiones[reg.value] || []).map((c) => `<option>${esc(c)}</option>`).join('')}`; };
      const dir = $('#rg-dir', root);
      L.bindField(dir, ['required']);
      L.combobox(dir, () => ['Av. Lircay', 'Calle 1 Sur', 'Calle 2 Norte', 'Av. San Miguel', 'Camino a Duao', 'Calle Prat', 'Av. Balmaceda', 'Calle Victoria'].flatMap((s, i) => [120, 512, 1180].map((n) => ({ label: `${s} ${n + i}`, meta: com.value || 'Maule' }))), { min: 2 });
      const desde = $('#rg-desde', root), hasta = $('#rg-hasta', root);
      L.bindField(hasta, [(v) => (v > desde.value ? '' : 'La hora de término debe ser posterior al inicio.'), (v) => { const [a, b] = desde.value.split(':').map(Number); const [c, d] = v.split(':').map(Number); return c * 60 + d - (a * 60 + b) >= 60 ? '' : 'La ventana debe durar al menos 1 hora.'; }]);
      L.bindField(desde, ['required']);
      L.bindField($('#rg-cn', root), ['required']);
      L.bindField($('#rg-ce', root), ['email']);
      L.bindField($('#rg-tel', root), [(v) => L.validators.phone('+56 ' + v)]);
      wirePasswords(root);
      L.bindField($('#rg-pw', root), ['password']);
      L.bindField($('#rg-pw2', root), [(v) => (v && v === $('#rg-pw', root).value ? '' : 'Las contraseñas no coinciden.')]);
      L.bindField($('#rg-terms', root), [(v) => (v ? '' : 'Debe aceptar los términos para continuar.')]);
      const dz = L.dropzone($('#rg-drop', root), { accept: '.pdf,.jpg,.jpeg,.png,image/*', maxMB: 10, onChange: () => ($('#rg-docs-err', root).innerHTML = '') });
      $('#rg-sample', root).onclick = async () => { dz.add([await L.fakeFile('carpeta_tributaria.pdf', 'application/pdf', 820), await L.fakeFile('patente_municipal.png', 'image/png')]); };
      $('#rg-terms-open', root).onclick = (e) => { e.preventDefault(); L.modal({ title: 'Términos de uso', body: '<p>Prototipo: texto de referencia. Los datos se tratan conforme a la Ley N.º 19.628 y solo se usan para gestionar pedidos, entregas y cobranza.</p><p>Puede solicitar acceso, rectificación o eliminación escribiendo a privacidad@puelche.cl.</p>', actions: [{ label: 'Entendido', cls: 'btn-primary' }] }); };

      const extraValid = () => {
        if (cur === 0) { const canal = $('[name=rg-canal]:checked', root).value; const hab = D.clientes.filter((c) => c.canal === 'Moderno').map((c) => L.rut.clean(c.rut)); const ok = canal !== 'Moderno' || hab.includes(L.rut.clean(rutIn.value)); $('#rg-rut-msg', root).innerHTML = ok ? '' : L.alert('danger', 'RUT no habilitado para el canal moderno', `Este RUT no figura como cliente activo de Puelche en el sistema de gestión. Contacte a su ejecutivo comercial para habilitarlo. Para la demostración puede usar ${D.clientes.find((c) => c.canal === 'Moderno').rut}.`); return ok; }
        if (cur === 1) { const any = $$('#rg-dias input:checked', root).length > 0; $('#rg-dias-err', root).style.display = any ? 'none' : 'flex'; $('#rg-dias-err', root).innerHTML = any ? '' : `${icon('alert-circle', 'icon-sm')}Elija al menos un día.`; $('#rg-dias-err', root).style.color = 'var(--c-danger)'; return any; }
        if (cur === 3) { const ok = dz.files.length > 0; if (!ok) $('#rg-docs-err', root).innerHTML = L.alert('danger', 'Falta adjuntar documentos', 'Adjunte al menos la carpeta tributaria para continuar.'); return ok; }
        return true;
      };
      const summary = () => {
        const v = (id) => esc($('#' + id, root).value || '—');
        const block = (t, step, rows) => `<div class="card" style="box-shadow:none"><div class="row-between"><h3 style="margin:0">${t}</h3><button type="button" class="btn btn-tertiary btn-sm" data-goto="${step}">${icon('edit', 'icon-sm')}Editar<span class="sr-only"> ${t}</span></button></div><dl class="desc-list" style="margin-top:8px">${rows.map(([a, b]) => `<dt>${a}</dt><dd>${b}</dd>`).join('')}</dl></div>`;
        $('#rg-sum', root).innerHTML = block('Empresa', 0, [['RUT', v('rg-rut')], ['Razón social', v('rg-rs')], ['Canal', esc($('[name=rg-canal]:checked', root).value)]]) + block('Local', 1, [['Comuna', v('rg-com')], ['Dirección', v('rg-dir')], ['Ventana', `${v('rg-desde')}–${v('rg-hasta')}`]]) + block('Contacto', 2, [['Nombre', v('rg-cn')], ['Correo', v('rg-ce')], ['Teléfono', '+56 ' + v('rg-tel')]]) + block('Documentos', 3, [['Adjuntos', `${dz.files.length} archivo(s)`]]);
      };
      const show = (n) => {
        cur = n;
        secs.forEach((s, i) => (s.hidden = i !== n));
        $('.stepper', root).outerHTML = stepperHtml(STEPS, n, true);
        $('#rg-title', root).textContent = titles[n];
        $('#rg-count', root).textContent = `Paso ${n + 1} de 5`;
        $('#rg-back', root).style.visibility = n === 0 ? 'hidden' : 'visible';
        $('#rg-next', root).innerHTML = n === 4 ? `${icon('send')}Enviar solicitud` : `Continuar${icon('arrow-right')}`;
        if (n === 4) { $('#rg-user', root).value = $('#rg-ce', root).value; summary(); }
        $('#rg-title', root).setAttribute('tabindex', '-1');
        $('#rg-title', root).focus();
      };
      root.addEventListener('click', (e) => { const g = e.target.closest('[data-goto]'); if (g) show(+g.dataset.goto); });
      $('#rg-back', root).onclick = () => show(Math.max(0, cur - 1));
      f.onsubmit = (e) => {
        e.preventDefault();
        const okFields = L.validateAll(secs[cur]);
        const okExtra = extraValid();
        if (!okFields || !okExtra) { L.toast('Revise los datos del paso', 'Hay campos que necesitan corrección.', 'error'); return; }
        if (cur < 4) { L.busy($('#rg-next', root), () => show(cur + 1), 450); return; }
        L.busy($('#rg-next', root), () => {
          $('#rg', root).innerHTML = `${stepperHtml(STEPS, 5)}${L.empty('done', 'Solicitud enviada', `Folio SOL-${Math.floor(Math.random() * 9000 + 1000)}. Comercial validará su crédito y le escribirá dentro de 24 horas hábiles a ${$('#rg-ce', root)?.value || 'su correo'}.`, '<div class="btn-group"><a class="btn btn-primary" href="#/ingresar">Ir a ingresar</a><a class="btn btn-secondary" href="#/">Volver al inicio</a></div>')}`;
          L.toast('Solicitud recibida', 'Le enviamos un correo de confirmación de la cuenta.', 'success');
        }, 1200);
      };
      show(0);
      rutIn.focus();
    }
  });

  /* ---------- Tablero de primer ingreso ---------- */
  L.route('/bienvenida', {
    title: 'Bienvenida', parent: '/inicio', block: 'Autenticación e incorporación', module: 'Transversal', rf: ['RF-17.07', 'RF-18.02'], actors: ['Todos los perfiles'],
    render: () => {
      const p = L.me();
      const items = [['Confirme sus datos de perfil', 'user', '/perfil', true], ['Configure cómo recibe notificaciones', 'bell', '/perfil', false], ['Conozca su tablero en un recorrido de 5 pasos', 'help', '#tour', false], [p.field ? 'Descargue los datos para trabajar sin conexión' : 'Revise su bandeja de tareas', p.field ? 'wifi-off' : 'inbox', p.field ? '#offline' : '/bandeja', false]];
      return `<div class="page-head"><div class="titles"><span class="page-kicker">Primer ingreso</span><h1>Bienvenida, ${esc(p.name.split(' ')[0])}</h1><p class="muted" style="margin:0">${esc(p.role)} · ${esc(p.iface)}</p></div></div>
        <div class="split">
          <div class="card"><div class="card-head"><h2>Prepare su espacio</h2><span class="small muted" id="ob-count">1 de 4 completados</span></div>
            <div class="progress" aria-hidden="true" style="margin-bottom:var(--sp-4)"><span id="ob-bar" style="width:25%"></span></div>
            <ul class="list" id="ob-list">${items.map(([t, i, r, done], k) => `<li><span class="avatar" style="border-radius:10px">${icon(done ? 'check' : i)}</span><div class="grow"><div class="title">${esc(t)}</div><div class="sub">${done ? 'Completado' : 'Pendiente'}</div></div><button type="button" class="btn ${done ? 'btn-tertiary' : 'btn-secondary'} btn-sm" data-ob="${k}" data-r="${r}" ${done ? 'disabled' : ''}>${done ? 'Listo' : 'Hacer ahora'}</button></li>`).join('')}</ul>
          </div>
          <div class="card card-accent stack"><h2>Su perfil incluye</h2><ul class="list">${(p.all ? L.nav.flatMap((g) => g.items).slice(0, 8) : L.nav.flatMap((g) => g.items).filter((i) => L.allowed(i.path))).map((i) => `<li>${icon(i.icon)}<span class="grow">${esc(i.label)}</span></li>`).join('')}</ul>
            <button type="button" class="btn btn-primary big-btn" id="ob-tour">${icon('play')}Iniciar recorrido guiado</button><a class="btn btn-tertiary" href="#/inicio">Ir directo a mi inicio</a></div>
        </div>`;
    },
    mount: (root) => {
      let done = 1;
      const tick = (b) => { b.closest('li').querySelector('.avatar').innerHTML = icon('check'); b.closest('li').querySelector('.sub').textContent = 'Completado'; b.textContent = 'Listo'; b.disabled = true; b.className = 'btn btn-tertiary btn-sm'; done++; $('#ob-count', root).textContent = `${done} de 4 completados`; $('#ob-bar', root).style.width = done * 25 + '%'; if (done === 4) L.toast('¡Todo listo!', 'Su espacio está preparado.', 'success'); };
      $$('[data-ob]', root).forEach((b) => (b.onclick = () => {
        const r = b.dataset.r;
        if (r === '#tour') { L.go('/inicio'); setTimeout(L.startTour, 500); return; }
        if (r === '#offline') { L.busy(b, () => { tick(b); L.toast('Datos descargados', 'Clientes, precios y stock con fecha de hoy 06:00.', 'success'); }, 1400); return; }
        if (b.dataset.ob === '1') { L.modal({ title: 'Preferencias de notificación', body: `<fieldset><legend>Canales</legend>${['Notificación en la app', 'Correo electrónico', 'SMS'].map((c, i) => `<label class="check"><input type="checkbox" ${i < 2 ? 'checked' : ''}> ${c}</label>`).join('')}</fieldset><div class="field" style="margin-top:12px"><label for="nf-freq">Frecuencia de resúmenes</label><select id="nf-freq" class="select"><option>Inmediata</option><option>Resumen diario a las 08:00</option><option>Resumen semanal</option></select></div>`, actions: [{ label: 'Cancelar' }, { label: 'Guardar preferencias', cls: 'btn-primary', onClick: () => { tick(b); L.toast('Preferencias guardadas', '', 'success'); } }] }); return; }
        L.go(r);
      }));
      $('#ob-tour', root).onclick = () => { L.go('/inicio'); setTimeout(L.startTour, 500); };
      const s = L.session(); if (s) { s.first = false; L.setSession(s); L.store.set('seen.' + s.profile, true); }
    }
  });
})(window.LFX);
