/* Tablero analítico (M10): indicadores con visualizaciones, ocho tipos de gráfico,
   filtros por período y categoría, profundización del indicador al detalle y exportación. */
(function (L) {
  const { esc, icon, $, $$, data: D, fmt } = L;
  const C = L.charts;
  const F = { periodo: '12m', canal: '', zona: '' };
  const factor = () => (F.canal === 'Moderno' ? 1.04 : F.canal === 'Food service' ? 0.99 : F.canal === 'Tradicional' ? 0.97 : 1) * (F.zona ? 0.985 + (F.zona.length % 4) * 0.008 : 1);
  const series = (id) => { const s = D.serie[id].map((v) => +(v * (id === 'otif' || id === 'fill' || id === 'ocupacion' ? Math.min(factor(), 100 / v) : 2 - factor())).toFixed(1)); return F.periodo === '3m' ? s.slice(-3) : F.periodo === '6m' ? s.slice(-6) : s; };
  const labels = () => (F.periodo === '3m' ? D.meses.slice(-3) : F.periodo === '6m' ? D.meses.slice(-6) : D.meses);
  const zonas = ['Talca', 'Curicó', 'Linares', 'Cauquenes', 'Chillán', 'Concepción', 'Los Ángeles', 'Constitución'];

  const filterBar = () => `<section class="card no-print" style="margin-bottom:var(--sp-5);padding:var(--sp-4)" aria-label="Filtros"><div class="row">
      <div class="segmented" role="group" aria-label="Período">${[['3m', '3 meses'], ['6m', '6 meses'], ['12m', '12 meses']].map(([v, l]) => `<button type="button" data-per="${v}" aria-pressed="${F.periodo === v}">${l}</button>`).join('')}</div>
      <label class="sr-only" for="an-canal">Canal</label><select id="an-canal" class="select" style="width:auto"><option value="">Todos los canales</option>${['Tradicional', 'Food service', 'Moderno'].map((c) => `<option ${F.canal === c ? 'selected' : ''}>${c}</option>`).join('')}</select>
      <label class="sr-only" for="an-zona">Zona</label><select id="an-zona" class="select" style="width:auto"><option value="">Todas las zonas</option>${zonas.map((z) => `<option ${F.zona === z ? 'selected' : ''}>${z}</option>`).join('')}</select>
      <div class="row" style="gap:6px"><label for="an-d1" class="small muted">Desde</label><input id="an-d1" type="date" class="input" style="width:auto" value="2025-12-01"><label for="an-d2" class="small muted">hasta</label><input id="an-d2" type="date" class="input" style="width:auto" value="2026-11-13"></div>
      <span class="grow"></span>${F.canal || F.zona ? '<button type="button" class="btn btn-tertiary btn-sm" data-clearf>Limpiar filtros</button>' : ''}
    </div>${F.canal || F.zona ? `<div class="row" style="margin-top:8px">${F.canal ? `<span class="chip">Canal: ${esc(F.canal)}</span>` : ''}${F.zona ? `<span class="chip">Zona: ${esc(F.zona)}</span>` : ''}</div>` : ''}</section>`;

  const chartCard = (id, title, sub, chart, table, extra = '', span = '') => `<section class="card ${span}" aria-labelledby="ch-${id}"><div class="card-head"><div><h2 id="ch-${id}">${esc(title)}</h2>${sub ? `<p class="small muted" style="margin:2px 0 0">${sub}</p>` : ''}</div><div class="menu-wrap no-print"><button type="button" class="btn btn-tertiary btn-icon" data-cm="${id}" aria-label="Opciones de ${esc(title)}">${icon('more')}</button></div></div><div data-chart="${id}">${chart}</div>${extra}<div data-table="${id}" hidden>${table}</div></section>`;

  const wireCharts = (root, exportable) => {
    $$('[data-cm]', root).forEach((b) => L.menu(b, () => [
      { label: $(`[data-table="${b.dataset.cm}"]`, root).hidden ? 'Ver como tabla' : 'Ocultar tabla', icon: 'list', onClick: () => { const t = $(`[data-table="${b.dataset.cm}"]`, root); t.hidden = !t.hidden; } },
      { label: 'Descargar datos (CSV)', icon: 'download', onClick: () => { const ex = exportable[b.dataset.cm]; if (ex) { L.download(`${b.dataset.cm}.csv`, ex()); L.toast('Datos descargados', '', 'success'); } } },
      { label: 'Ampliar', icon: 'external', onClick: () => L.modal({ title: $(`#ch-${b.dataset.cm}`, root).textContent, size: 'lg', body: $(`[data-chart="${b.dataset.cm}"]`, root).innerHTML, actions: [{ label: 'Cerrar', cls: 'btn-primary' }] }) }
    ]));
  };

  L.route('/analitica', {
    title: 'Tablero analítico', parent: '/inicio', block: 'Tablero analítico', module: 'M10 Analítica', rf: ['RF-11.01', 'RF-11.02', 'RF-11.03', 'RF-11.04', 'RF-11.05', 'RF-11.06', 'RF-16.02', 'RNG-09'], actors: ['Gerente Comercial', 'Gerente de Finanzas', 'Gerente de Operaciones', 'Jefa de Calidad'],
    render: () => `<div class="page-head"><div class="titles"><span class="page-kicker">M10 · datos al día · actualizado hace 3 min</span><h1>Tablero analítico</h1><p class="muted" style="margin:0">Indicadores del caso contra la línea base 2025. Haga clic en un indicador o en un gráfico para profundizar hasta la entrega.</p></div>
      <div class="actions no-print"><button type="button" class="btn btn-secondary" id="an-sched">${icon('calendar')}Programar envío</button><button type="button" class="btn btn-secondary" id="an-print">${icon('printer')}Imprimir</button><button type="button" class="btn btn-primary" id="an-exp">${icon('download')}Exportar informe</button></div></div>
      <div id="an-filters"></div><div id="an-body" aria-live="polite"></div>`,
    mount: (root, p, q) => {
      const exportable = {};
      const draw = () => {
        $('#an-filters', root).innerHTML = filterBar();
        const body = $('#an-body', root);
        body.setAttribute('aria-busy', 'true');
        body.innerHTML = `<div class="grid grid-3">${Array.from({ length: 6 }, () => `<div class="card">${L.skeleton(3)}</div>`).join('')}</div>`;
        L.timeout(() => {
          const lb = labels();
          const kp = D.kpis.map((k) => ({ ...k, value: series(k.id).slice(-1)[0] }));
          const otif = series('otif'), fill = series('fill');
          const reZona = zonas.map((z, i) => ({ label: z, short: z.slice(0, 6), value: +(2.1 + ((i * 7) % 5) * 0.45 * (2 - factor())).toFixed(1), drill: '/analitica/reentregas' }));
          const ent = series('entregas');
          const hm = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'].map((_, r) => ['07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17'].map((h, c) => Math.round((40 + Math.sin(c / 1.7) * 30 + (c > 1 && c < 5 ? 55 : 0) + r * 6) * (r === 5 ? 0.55 : 1))));
          const sc = D.clientes.slice(0, 30).map((c) => ({ label: c.nombre, x: c.costoServir, y: +(c.ventaMes / 1e6).toFixed(1), r: c.canal === 'Moderno' ? 9 : 6, color: c.canal === 'Moderno' ? 'var(--chart-2)' : c.canal === 'Food service' ? 'var(--chart-3)' : 'var(--chart-1)', drill: '/clientes/' + c.id }));
          exportable.otif = () => L.toCSV(lb.map((m, i) => ({ m, otif: otif[i], fill: fill[i] })), [{ label: 'Mes', key: 'm' }, { label: 'OTIF %', key: 'otif' }, { label: 'Fill rate %', key: 'fill' }]);
          exportable.zona = () => L.toCSV(reZona, [{ label: 'Zona', key: 'label' }, { label: 'Reentregas %', key: 'value' }]);
          exportable.causas = () => L.toCSV(D.causasRechazo, [{ label: 'Causa', key: 'label' }, { label: '%', key: 'value' }]);
          body.innerHTML = `
            <section aria-label="Indicadores principales"><div class="grid kpi-grid" style="margin-bottom:var(--sp-5)">${kp.map((k) => L.kpiCard(k)).join('')}</div></section>
            <div class="grid grid-2">
              ${chartCard('otif', 'OTIF y fill rate por mes', 'Gráfico de líneas · meta 95 % (RNG-09)', C.line(lb, [{ name: 'OTIF', values: otif, drill: lb.map(() => '/analitica/otif') }, { name: 'Fill rate', values: fill, dashed: true }], { unit: '%', target: 95, min: 70, label: 'OTIF y fill rate por mes' }) + C.legend([{ label: 'OTIF' }, { label: 'Fill rate' }]), C.table(['Mes', 'OTIF', 'Fill rate'], lb.map((m, i) => [m, fmt.pct(otif[i]), fmt.pct(fill[i])])))}
              ${chartCard('zona', 'Reentregas por zona', 'Gráfico de barras · meta bajo 1 %', C.bar(reZona, { unit: '%', target: 1, label: 'Reentregas por zona', highlight: reZona.reduce((m, d, i, a) => (d.value > a[m].value ? i : m), 0) }), C.table(['Zona', 'Reentregas'], reZona.map((d) => [d.label, fmt.pct(d.value)])))}
              ${chartCard('causas', 'Causas de entregas fallidas', 'Gráfico circular · el local cerrado es la excepción más frecuente', `<div class="row" style="justify-content:center">${C.donut(D.causasRechazo.map((d) => ({ ...d, drill: '/analitica/reentregas' })), { center: '1.284', centerSub: 'fallidas', label: 'Causas de entregas fallidas' })}${C.legend(D.causasRechazo.map((d) => ({ label: d.label, value: d.value + ' %' })))}</div>`, C.table(['Causa', '%'], D.causasRechazo.map((d) => [d.label, d.value + ' %'])))}
              ${chartCard('po', 'Perfect Order del mes: 87,4 %', 'Pedidos sin daño, faltante, atraso ni error de documento, contra la orden de venta original', C.hbar([{ label: 'Atraso', value: 5.1 }, { label: 'Faltante', value: 4.2 }, { label: 'Daño', value: 2.0 }, { label: 'Documento', value: 1.3 }], { unit: '%', label: 'Causas que rompen la orden perfecta' }), C.table(['Causa raíz', '% de pedidos'], [['Atraso', '5,1 %'], ['Faltante', '4,2 %'], ['Daño', '2,0 %'], ['Documento', '1,3 %']]))}
              ${chartCard('canal', 'Resultado de entregas por canal', 'Barras apiladas al 100 %', C.stacked(['Tradicional', 'Food service', 'Moderno'], [{ name: 'A tiempo y completa', values: [83, 87, 91] }, { name: 'Tarde', values: [9, 7, 6] }, { name: 'Parcial', values: [5, 4, 2] }, { name: 'Fallida', values: [3, 2, 1], color: 'var(--c-danger)' }], { percent: true, label: 'Resultado por canal' }) + C.legend([{ label: 'A tiempo y completa' }, { label: 'Tarde' }, { label: 'Parcial' }, { label: 'Fallida', color: 'var(--c-danger)' }]), C.table(['Canal', 'A tiempo', 'Tarde', 'Parcial', 'Fallida'], [['Tradicional', '83 %', '9 %', '5 %', '3 %'], ['Food service', '87 %', '7 %', '4 %', '2 %'], ['Moderno', '91 %', '6 %', '2 %', '1 %']]))}
              ${chartCard('vol', 'Entregas por mes', 'Gráfico de área · peak de septiembre (2.600/día)', C.area(lb, [{ name: 'Entregas', values: ent }], { label: 'Entregas por mes' }), C.table(['Mes', 'Entregas'], lb.map((m, i) => [m, fmt.n(ent[i])])))}
              ${chartCard('ocup', 'Ocupación de camiones', 'Indicador de aguja · meta 85 %', `<div style="max-width:320px;margin:0 auto">${C.gauge(series('ocupacion').slice(-1)[0], { target: 85, label: 'Ocupación promedio de camiones' })}</div><p class="small muted" style="text-align:center">Línea base 2025: 68 %, con días de 41 %.</p>`, C.table(['Indicador', 'Valor'], [['Ocupación', fmt.pct(series('ocupacion').slice(-1)[0])], ['Meta', '85 %']]))}
              ${chartCard('hm', 'Entregas por día y hora', 'Mapa de calor · concentración entre 09:00 y 11:00', C.heatmap(['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'], ['07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17'], hm, { label: 'Entregas por día y hora' }), C.table(['Día', ...['07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17']], ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'].map((d, i) => [d, ...hm[i]])), '', 'span-all')}
              ${chartCard('cts', 'Costo de servir frente a venta por cliente', 'Gráfico de dispersión · Etapa 2 (RF-11.02, RF-11.08)', C.scatter(sc, { xLabel: 'Costo de servir (% de la venta)', yLabel: 'Venta mensual (MM$)', xUnit: '%', quadrants: { x: 10, y: 10 }, label: 'Costo de servir frente a venta por cliente' }) + C.legend([{ label: 'Tradicional', color: 'var(--chart-1)' }, { label: 'Food service', color: 'var(--chart-3)' }, { label: 'Moderno', color: 'var(--chart-2)' }]), C.table(['Cliente', 'Costo de servir', 'Venta mensual'], sc.map((s) => [s.label, fmt.pct(s.x), '$' + s.y + ' MM'])), '', 'span-all')}
            </div>`;
          body.removeAttribute('aria-busy');
          wireCharts(root, exportable);
        }, 550);
        $$('[data-per]', root).forEach((b) => (b.onclick = () => { F.periodo = b.dataset.per; draw(); L.announce('Período actualizado'); }));
        $('#an-canal', root).onchange = (e) => { F.canal = e.target.value; draw(); };
        $('#an-zona', root).onchange = (e) => { F.zona = e.target.value; draw(); };
        $('[data-clearf]', root) && ($('[data-clearf]', root).onclick = () => { F.canal = ''; F.zona = ''; draw(); });
        const d1 = $('#an-d1', root), d2 = $('#an-d2', root);
        [d1, d2].forEach((x) => (x.onchange = () => { if (d1.value > d2.value) L.toast('Rango de fechas no válido', '«Desde» debe ser anterior a «hasta».', 'error'); else draw(); }));
      };
      const exportModal = () => L.modal({
        title: 'Exportar informe', body: `<fieldset><legend>Formato</legend><div class="options-row">${['PDF', 'XLSX', 'CSV'].map((f, i) => `<label class="radio"><input type="radio" name="fx" value="${f}" ${i === 2 ? 'checked' : ''}> ${f}</label>`).join('')}</div></fieldset><fieldset style="margin-top:12px"><legend>Contenido</legend>${['Indicadores principales', 'Gráficos con sus datos', 'Detalle por ruta'].map((t) => `<label class="check"><input type="checkbox" checked> ${t}</label>`).join('')}</fieldset><p class="hint">Se exporta con los filtros aplicados: período ${F.periodo}${F.canal ? ', canal ' + F.canal : ''}${F.zona ? ', zona ' + F.zona : ''}.</p>`,
        actions: [{ label: 'Cancelar' }, { label: 'Exportar', cls: 'btn-primary', icon: 'download', onClick: async (api, btn) => { const f = $('[name=fx]:checked', api.el).value; await L.busy(btn, () => {}, 900); if (f === 'CSV') L.download('informe_kpi.csv', L.toCSV(D.kpis.map((k) => ({ ...k, value: series(k.id).slice(-1)[0] })), [{ label: 'Indicador', key: 'label' }, { label: 'Valor', key: 'value' }, { label: 'Base 2025', key: 'base' }, { label: 'Meta', key: 'meta' }, { label: 'Unidad', key: 'unit' }])); L.toast('Informe exportado', f === 'CSV' ? 'Se descargó el archivo CSV.' : `Generación de ${f} simulada.`, 'success'); } }]
      });
      $('#an-exp', root).onclick = exportModal;
      $('#an-print', root).onclick = () => window.print();
      $('#an-sched', root).onclick = () => L.modal({ title: 'Programar envío de reportes', body: `<p class="muted">Reportes ejecutivos en PDF y XLSX a las casillas de gerencia (RF-11.01).</p><div class="form-grid"><div class="field"><label for="sc-f">Frecuencia</label><select id="sc-f" class="select"><option>Semanal, lunes 06:00</option><option>Mensual, día 2</option><option>Diaria, 07:00</option></select></div><div class="field"><label for="sc-t">Hora</label><input id="sc-t" class="input" type="time" value="06:00"></div><div class="field full"><label for="sc-m">Destinatarios</label><input id="sc-m" class="input" value="gerencia@puelche.cl, operaciones@puelche.cl"></div></div>`, onOpen: (d) => L.bindField($('#sc-m', d), [(v) => (v.split(',').every((m) => !L.validators.email(m.trim())) ? '' : 'Revise los correos separados por coma.')]), actions: [{ label: 'Cancelar' }, { label: 'Programar', cls: 'btn-primary', onClick: (api) => { if (!L.validateAll(api.el)) return false; L.toast('Envío programado', $('#sc-f', api.el).value, 'success'); } }] });
      draw();
      if (q.exportar) setTimeout(exportModal, 700);
    }
  });

  /* ---------- Profundización: indicador → ruta/zona → entrega ---------- */
  L.route('/analitica/:kpi', {
    title: (p) => (D.kpis.find((k) => k.id === p.kpi)?.label || (p.kpi === 'costo' ? 'Costo de servir' : 'Detalle del indicador')), parent: '/analitica', block: 'Tablero analítico', module: 'M10 Analítica', rf: ['RF-11.03', 'RF-11.06', 'RF-16.02'], actors: ['Gerencias'],
    render: ({ kpi }) => {
      const k = D.kpis.find((x) => x.id === kpi) || { id: kpi, label: 'Costo de servir', value: 9.4, base: 0, meta: 8, unit: '%', desc: 'Costo logístico por entrega y por cliente.' };
      const rows = D.rutas.map((r) => ({ ...r, val: kpi === 'otif' ? r.otif : kpi === 'ocupacion' ? r.ocupacion : +(k.value * (0.8 + (r.km % 7) / 15)).toFixed(1) }));
      return `<div class="page-head"><div class="titles"><span class="page-kicker">Profundización · nivel 2 de 3</span><h1>${esc(k.label)} por ruta</h1><p class="muted" style="margin:0">${esc(k.desc)} Valor actual ${k.unit === '%' ? fmt.pct(k.value) : k.value + ' ' + k.unit} · meta ${k.meta} ${esc(k.unit)}.</p></div><div class="actions"><button type="button" class="btn btn-secondary" id="dk-exp">${icon('download')}Exportar</button></div></div>
        <section class="card" style="margin-bottom:var(--sp-5)">${C.bar(rows.map((r) => ({ label: r.zona, short: r.id, value: r.val, drill: `/analitica/${kpi}/ruta/${r.id}`, color: (k.good === 'down' ? r.val > k.meta * 2 : r.val < k.meta - 8) ? 'var(--c-danger)' : undefined })), { unit: k.unit === '%' ? '%' : '', target: k.meta, label: `${k.label} por ruta`, h: 280, w: 900 })}<p class="small muted">Haga clic en una barra para ver las entregas de esa ruta.</p></section>
        <section class="card card-flush"><div class="table-wrap"><table class="table"><caption class="sr-only">${esc(k.label)} por ruta</caption><thead><tr><th>Ruta</th><th>Zona</th><th>Conductor</th><th class="right">${esc(k.label)}</th><th></th></tr></thead><tbody>${rows.map((r) => `<tr><td class="mono">${r.id}</td><td>${esc(r.zona)}</td><td>${esc(r.conductor)}</td><td class="num right">${k.unit === '%' ? fmt.pct(r.val) : r.val}</td><td class="right"><a class="btn btn-tertiary btn-sm" href="#/analitica/${kpi}/ruta/${r.id}">Ver entregas${icon('chev-right', 'icon-sm')}</a></td></tr>`).join('')}</tbody></table></div></section>`;
    },
    mount: (root) => { $('#dk-exp', root).onclick = () => { L.download('detalle_por_ruta.csv', L.toCSV(D.rutas, [{ label: 'Ruta', key: 'id' }, { label: 'Zona', key: 'zona' }, { label: 'OTIF', key: 'otif' }, { label: 'Ocupación', key: 'ocupacion' }])); L.toast('Detalle exportado', '', 'success'); }; }
  });

  L.route('/analitica/:kpi/ruta/:id', {
    title: (p) => (p.id ? `Entregas de ${p.id}` : 'Entregas de la ruta'), parent: (p) => `/analitica/${p.kpi || 'otif'}`, block: 'Tablero analítico', module: 'M10 · M6', rf: ['RF-11.03', 'RF-06.06'], actors: ['Gerencias'],
    render: ({ kpi, id }) => {
      const r = D.rutas.find((x) => x.id === id) || D.rutas[0];
      const peds = D.pedidos.filter((p) => p.ruta === r.id && ['En ruta', 'Entregado', 'Parcial', 'Fallido', 'Reprogramado', 'Rendido'].includes(p.estado));
      return `<div class="page-head"><div class="titles"><span class="page-kicker">Profundización · nivel 3 de 3</span><h1>Entregas de ${r.id} · ${esc(r.zona)}</h1><p class="muted" style="margin:0">Cada entrega con su cumplimiento y causal. Una entrega parcial o tardía cuenta como incumplida (RNG-09).</p></div></div>
        <section class="card card-flush"><div class="table-wrap"><table class="table"><thead><tr><th>Pedido</th><th>Cliente</th><th>Ventana</th><th>Llegada real</th><th>A tiempo</th><th>Completa</th><th>Causal</th></tr></thead><tbody>${peds.map((p, i) => { const late = i % 4 === 2, part = i % 5 === 3; return `<tr><td><a class="row-link mono" href="#/pedidos/${p.id}">${p.id}</a></td><td>${esc(p.clienteNombre)}</td><td>${esc(p.ventana)}</td><td class="mono">${p.ventana.split('–')[late ? 1 : 0].replace(/:(\d\d)/, (m, mm) => ':' + String((+mm + 12 + i) % 60).padStart(2, '0'))}</td><td>${late ? L.badge('No', 'danger') : L.badge('Sí', 'success')}</td><td>${part ? L.badge('No', 'danger') : L.badge('Sí', 'success')}</td><td>${late ? 'Tráfico en ruta 5' : part ? 'Faltante en preparación' : '—'}</td></tr>`; }).join('')}</tbody></table></div></section>`;
    }
  });
})(window.LFX);
