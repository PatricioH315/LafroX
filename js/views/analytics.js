/* Analítica de demostración: filtros, gráficos, detalle y CSV leen la misma muestra. */
(function (L) {
  const { $, $$, esc, data: D, fmt, charts: C } = L;
  const canales = ['Tradicional', 'Food service', 'Moderno'];
  const zonas = [...new Set(D.rutas.map((r) => r.zona))].sort();
  const base = new Date(D.today);
  const iso = (d) => [d.getFullYear(), d.getMonth() + 1, d.getDate()].map((v, i) => i ? String(v).padStart(2, '0') : v).join('-');
  const last = iso(base);
  const since = (months) => iso(new Date(base.getFullYear(), base.getMonth() + 1 - months, 1));
  const first = since(12);
  const closed = ['Entregado', 'Rendido', 'Parcial', 'Fallido', 'Reprogramado'];
  const percent = (n, d) => d ? +(100 * n / d).toFixed(1) : 0;
  const sum = (rows, name) => rows.reduce((n, row) => n + row[name], 0);
  const group = (rows, key) => {
    const bins = new Map();
    for (const row of rows) {
      const value = row[key];
      if (!bins.has(value)) bins.set(value, []);
      bins.get(value).push(row);
    }
    return [...bins].sort(([a], [b]) => a.localeCompare(b, 'es'));
  };
  const filters = (q) => ({
    desde: /^\d{4}-\d\d-\d\d$/.test(q.desde || '') ? q.desde : first,
    hasta: /^\d{4}-\d\d-\d\d$/.test(q.hasta || '') ? q.hasta : last,
    canal: canales.includes(q.canal) ? q.canal : '',
    zona: zonas.includes(q.zona) ? q.zona : ''
  });
  const routeFor = (path, f) => path + '?' + new URLSearchParams(f);
  const href = (path, f) => esc('#' + routeFor(path, f));
  const span = (f) => esc([f.desde + ' a ' + f.hasta, f.canal || 'todos los canales', f.zona || 'todas las zonas'].join(' · '));

  const time = (m) => String(Math.floor(m / 60) % 24).padStart(2, '0') + ':' + String(m % 60).padStart(2, '0');
  const minutes = (s) => { const [h, m] = s.split(':').map(Number); return h * 60 + m; };
  function select(f) {
    return D.pedidos.flatMap((p) => {
      const route = D.rutas.find((r) => r.id === p.ruta);
      const date = iso(new Date(p.entrega));
      if (!route || !closed.includes(p.estado) || date < f.desde || date > f.hasta ||
        (f.canal && f.canal !== p.canal) || (f.zona && f.zona !== route.zona)) return [];
      // Los datos de ejemplo no tienen horas de llegada ni cantidades aceptadas.
      // Se generan una sola vez por ID en esta consulta y se exponen en el detalle y el CSV.
      const n = Number(p.id.slice(-4));
      const [start, end] = p.ventana.split('–').map(minutes);
      const units = sum(p.lineas, 'cant');
      const visited = !['Fallido', 'Reprogramado'].includes(p.estado);
      const delivered = !visited ? 0 : p.estado === 'Parcial' ? Math.floor(units * 0.72) : units;
      const late = visited && n % 5 === 0;
      const cause = !visited ? (p.estado === 'Reprogramado' ? 'Reprogramación' : 'Local cerrado') :
        delivered < units ? 'Faltante en entrega' : late ? 'Fuera de ventana' : 'Sin incidencia';
      const km = +(route.km / route.paradas).toFixed(1), unload = 9 + n % 15;
      return [{ id: p.id, cliente: p.clienteNombre, canal: p.canal, zona: route.zona, ruta: route.id,
        date, status: p.estado, window: p.ventana, arrival: visited ? time(late ? end + 12 : start + Math.floor((end - start) / 2)) : '—',
        units, delivered, onTime: visited && !late, complete: delivered === units, cause,
        ocupacion: route.ocupacion, total: p.total, km, unload,
        transport: Math.round(km * 690), handling: visited ? 2400 + unload * 210 : 0 }];
    });
  }
  const metrics = {
    otif: (rows) => percent(rows.filter((r) => r.complete && r.onTime).length, rows.length),
    fill: (rows) => percent(sum(rows, 'delivered'), sum(rows, 'units')),
    reentregas: (rows) => percent(rows.filter((r) => ['Fallido', 'Reprogramado'].includes(r.status)).length, rows.length),
    ocupacion: (rows) => {
      const trips = [...new Map(rows.map((r) => [r.ruta + ':' + r.date, r])).values()];
      return trips.length ? +(sum(trips, 'ocupacion') / trips.length).toFixed(1) : 0;
    },
    costo: (rows) => percent(sum(rows, 'transport') + sum(rows, 'handling'), sum(rows, 'total')),
    entregas: (rows) => rows.length
  };
  const kpis = [...D.kpis.filter((k) => metrics[k.id]),
    { id: 'costo', label: 'Costo de servir', unit: '%', desc: 'Transporte y descarga de la muestra sobre importe del pedido.' },
    { id: 'entregas', label: 'Pedidos de la muestra', unit: 'pedidos', desc: 'Pedidos con resultado de reparto en el período.' }];
  const kpi = (id) => kpis.find((x) => x.id === id) || kpis[0];
  const valueText = (k, val) => k.unit === '%' ? fmt.pct(val) : fmt.n(val) + ' ' + k.unit;
  const detailColumns = [
    ['Pedido', 'id'], ['Cliente', 'cliente'], ['Canal', 'canal'], ['Zona', 'zona'], ['Ruta', 'ruta'], ['Fecha', 'date'],
    ['Estado', 'status'], ['Ventana', 'window'], ['Llegada simulada', 'arrival'], ['Unidades pedidas', 'units'],
    ['Unidades entregadas', 'delivered'], ['A tiempo', 'onTime'], ['Completa', 'complete'], ['Causal', 'cause'],
    ['Ocupación del viaje (%)', 'ocupacion'], ['Transporte (CLP)', 'transport'], ['Descarga (CLP)', 'handling']
  ];
  const csv = (rows, columns) => L.toCSV(rows, columns.map(([label, key]) => ({ label, key })));
  const rowsTable = (rows) => C.table(detailColumns.map(([label]) => label),
    rows.map((r) => detailColumns.map(([, key]) => typeof r[key] === 'boolean' ? (r[key] ? 'Sí' : 'No') : r[key])));
  const empty = () => L.empty('box', 'Sin registros para estos filtros', 'Elija otra fecha, canal o zona. No se mezclan datos de otras selecciones.');

  function graphics(rows, f) {
    const dates = group(rows, 'date'), routes = group(rows, 'ruta'), states = group(rows, 'status'), byChannel = group(rows, 'canal');
    const datesLabels = dates.map(([d]) => d.slice(5));
    const otif = dates.map(([, r]) => metrics.otif(r)), fill = dates.map(([, r]) => metrics.fill(r));
    const statusValues = states.map(([label, r]) => ({ label, value: r.length }));
    const routeValues = routes.map(([label, r]) => ({ label, value: metrics.otif(r), drill: routeFor('/analitica/otif/ruta/' + label, f) }));
    const units = dates.map(([, r]) => sum(r, 'delivered'));
    const channels = states.map(([name]) => ({ name, values: byChannel.map(([, r]) => r.filter((x) => x.status === name).length) }));
    const days = ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'];
    const hours = Array.from({ length: 12 }, (_, i) => String(7 + i).padStart(2, '0'));
    const heat = days.map((_, d) => hours.map((h) => rows.filter((r) =>
      new Date(r.date + 'T12:00:00').getDay() === d && r.arrival.startsWith(h + ':')).length));
    const occ = metrics.ocupacion(rows);
    const points = rows.map((r) => ({ label: r.id, x: r.total, y: r.transport + r.handling, drill: routeFor('/analitica/costo/ruta/' + r.ruta, f) }));
    return [
      { title: 'OTIF y fill rate por día', labels: ['Día', 'OTIF (%)', 'Fill rate (%)'],
        data: dates.map(([d], i) => [d, otif[i], fill[i]]),
        graphic: C.line(datesLabels, [{ name: 'OTIF', values: otif }, { name: 'Fill rate', values: fill }], { unit: '%', label: 'OTIF y fill rate por día' }) + C.legend([{ label: 'OTIF' }, { label: 'Fill rate' }]) },
      { title: 'OTIF por ruta', labels: ['Ruta', 'OTIF (%)'], data: routeValues.map((r) => [r.label, r.value]),
        graphic: C.bar(routeValues, { unit: '%', label: 'OTIF por ruta' }) },
      { title: 'Resultado del reparto', labels: ['Estado', 'Pedidos'], data: statusValues.map((r) => [r.label, r.value]),
        graphic: '<div class="row">' + C.donut(statusValues, { center: String(rows.length), centerSub: 'pedidos', label: 'Resultado del reparto' }) + C.legend(statusValues) + '</div>' },
      { title: 'Unidades entregadas por día', labels: ['Día', 'Unidades'], data: dates.map(([d], i) => [d, units[i]]),
        graphic: C.area(datesLabels, [{ name: 'Unidades', values: units }], { label: 'Unidades entregadas por día' }) },
      { title: 'Resultado por canal', labels: ['Canal', ...channels.map((s) => s.name)],
        data: byChannel.map(([c], i) => [c, ...channels.map((s) => s.values[i])]),
        graphic: C.stacked(byChannel.map(([c]) => c), channels, { label: 'Resultado por canal' }) + C.legend(channels.map((s) => ({ label: s.name }))) },
      { title: 'Entregas por día y hora', labels: ['Día', ...hours], data: days.map((d, i) => [d, ...heat[i]]),
        graphic: C.heatmap(days, hours, heat, { label: 'Entregas por día y hora' }) },
      { title: 'Ocupación de los viajes de la muestra', labels: ['Indicador', 'Valor (%)'], data: [['Ocupación', occ]],
        graphic: C.gauge(occ, { target: 85, label: 'Ocupación de los viajes de la muestra' }) },
      { title: 'Costo frente a importe del pedido', labels: ['Pedido', 'Importe (CLP)', 'Costo (CLP)'], data: points.map((p) => [p.label, p.x, p.y]),
        graphic: C.scatter(points, { label: 'Costo frente a importe del pedido', xLabel: 'Importe del pedido', yLabel: 'Transporte y descarga' }) }
    ];
  }

  function exportReport(f, rows, charts) {
    const sections = [
      { id: 'kpis', label: 'Indicadores principales' },
      { id: 'charts', label: 'Gráficos con sus datos' },
      { id: 'detail', label: 'Detalle por ruta' }
    ];
    L.modal({ title: 'Exportar informe CSV',
      body: `<p>${span(f)} · ${rows.length} pedidos.</p><fieldset><legend>Secciones del informe</legend>${sections.map((s) => `<label class="check"><input type="checkbox" name="an-section" value="${s.id}" checked> ${s.label}</label>`).join('')}</fieldset><p id="an-export-error" role="alert"></p>`,
      actions: [{ label: 'Cancelar' }, { label: 'Descargar CSV', cls: 'btn-primary', onClick: (api) => {
        const enabled = new Set($$('[name=an-section]:checked', api.el).map((x) => x.value));
        if (!enabled.size) { $('#an-export-error', api.el).textContent = 'Seleccione al menos una sección.'; return false; }
        const records = [];
        const add = (section, row, column, value) => records.push({ section, row, column, value });
        Object.entries(f).forEach(([key, val]) => add('Filtros', 'Selección', key, val || 'Todos'));
        if (enabled.has('kpis')) kpis.forEach((k) => add('Indicadores principales', k.label, k.unit, rows.length ? metrics[k.id](rows) : 'Sin datos'));
        if (enabled.has('charts')) charts.forEach((c) => c.data.forEach(([label, ...values]) => values.forEach((v, i) => add(c.title, label, c.labels[i + 1], v))));
        if (enabled.has('detail')) rows.forEach((r) => detailColumns.forEach(([label, key]) => add('Detalle por ruta', r.id, label, r[key])));
        L.download('informe_analitico.csv', csv(records, [['Sección', 'section'], ['Registro', 'row'], ['Campo', 'column'], ['Valor', 'value']]));
        L.toast('Informe descargado', 'Contiene las secciones y los filtros seleccionados.', 'success');
      }}]
    });
  }


  function scheduleReport(f, root) {
    L.modal({ title: 'Programar informe · simulación',
      body: `<p>Guarda la configuración de la demostración, no envía correos. Filtros: ${span(f)}.</p>
        <div class="form-grid"><div class="field"><label for="sc-f">Frecuencia</label><select id="sc-f" class="select"><option>Semanal</option><option>Mensual</option><option>Diaria</option></select></div>
        <div class="field"><label for="sc-t">Hora</label><input id="sc-t" class="input" type="time" value="06:00" required></div>
        <div class="field full"><label for="sc-m">Destinatario de ejemplo</label><input id="sc-m" class="input" type="email" value="gerencia@puelche.cl" required></div></div>`,
      onOpen: (dlg) => { L.bindField($('#sc-t', dlg), ['required']); L.bindField($('#sc-m', dlg), ['required', L.validators.email]); },
      actions: [{ label: 'Cancelar' }, { label: 'Guardar programación simulada', cls: 'btn-primary', onClick: (api) => {
        if (!L.validateAll(api.el)) return false;
        const entry = { filtros: f, frecuencia: $('#sc-f', api.el).value, hora: $('#sc-t', api.el).value, destino: $('#sc-m', api.el).value };
        L.store.set('analitica.programacion', entry);
        $('#an-schedule-status', root).textContent = 'Programación simulada: ' + entry.frecuencia.toLowerCase() + ' · ' + entry.hora + ' · ' + entry.destino;
        L.toast('Programación guardada', 'Solo para esta demostración.', 'success');
      }}]
    });
  }

  L.route('/analitica', {
    title: 'Tablero analítico', parent: '/inicio', block: 'Tablero analítico', module: 'M10 Analítica',
    rf: ['RF-11.01', 'RF-11.02', 'RF-11.03', 'RF-11.04', 'RF-11.05', 'RF-11.06', 'RF-16.02', 'RNG-09'],
    actors: ['Gerente Comercial', 'Gerente de Finanzas', 'Gerente de Operaciones', 'Jefa de Calidad'],
    render: (_, q) => {
      const f = filters(q), rows = select(f), charts = rows.length ? graphics(rows, f) : [];
      return `<div class="page-head"><div class="titles"><h1>Tablero analítico</h1><p class="muted">Muestra simulada. Las horas, cantidades aceptadas y costos del detalle son datos de demostración.</p></div><div class="actions no-print">
        <button type="button" class="btn btn-secondary" id="an-sched">Programar envío</button><button type="button" class="btn btn-secondary" id="an-print">Imprimir</button><button type="button" class="btn btn-primary" id="an-exp">Exportar informe</button></div></div>
        <form class="card form-grid no-print" id="an-filters">
          <div class="field"><label for="an-d1">Desde</label><input id="an-d1" name="desde" type="date" class="input" min="${first}" max="${last}" value="${f.desde}" required></div>
          <div class="field"><label for="an-d2">Hasta</label><input id="an-d2" name="hasta" type="date" class="input" min="${first}" max="${last}" value="${f.hasta}" required></div>
          <div class="field"><label for="an-canal">Canal</label><select name="canal" id="an-canal" class="select"><option value="">Todos</option>${canales.map((c) => `<option ${f.canal === c ? 'selected' : ''}>${esc(c)}</option>`).join('')}</select></div>
          <div class="field"><label for="an-zona">Zona</label><select name="zona" id="an-zona" class="select"><option value="">Todas</option>${zonas.map((z) => `<option ${f.zona === z ? 'selected' : ''}>${esc(z)}</option>`).join('')}</select></div>
          <div class="full btn-group"><button type="submit" class="btn btn-primary" id="an-apply">Aplicar filtros</button>${[3,6,12].map((m) => `<button type="button" class="btn btn-secondary" data-period="${m}">${m} meses</button>`).join('')}</div>
          <div class="full" id="an-error" role="alert"></div>
        </form>
        <p id="an-schedule-status" class="small muted" role="status"></p>
        <p id="an-summary" role="status" style="margin-top:var(--sp-4)">${rows.length} pedidos · ${span(f)}</p>
        ${rows.length ? `<section class="grid kpi-grid" aria-label="Indicadores principales" style="margin-bottom:var(--sp-5)">${kpis.map((k) => `<div class="kpi-with-help"><a class="card card-link kpi" href="${href('/analitica/' + k.id, f)}"><span class="label">${esc(k.label)}</span><span class="value">${valueText(k, metrics[k.id](rows))}</span><span class="meta">Ver detalle por ruta</span></a><div class="kpi-help">${L.tip(k.desc)}</div></div>`).join('')}</section>
        <div class="grid grid-2">${charts.map((c) => `<section class="card"><h2>${esc(c.title)}</h2>${c.graphic}${L.accordionHtml('Ver datos en tabla', C.table(c.labels, c.data))}</section>`).join('')}</div>` : empty()}`;
    },
    mount: (root, _, q) => {
      const form = $('#an-filters', root), f = filters(q), rows = select(f);
      const apply = (event) => {
        event.preventDefault();
        const next = Object.fromEntries(new FormData(form));
        if (next.desde > next.hasta) { $('#an-error', root).textContent = 'La fecha inicial debe ser anterior o igual a la fecha final.'; return; }
        L.go(routeFor('/analitica', filters(next)));
      };
      form.onsubmit = apply;
      $$('[data-period]', root).forEach((button) => button.onclick = () => {
        form.elements.desde.value = since(Number(button.dataset.period));
        form.elements.hasta.value = last;
        form.requestSubmit();
      });
      $('#an-exp', root).onclick = () => exportReport(f, rows, rows.length ? graphics(rows, f) : []);
      $('#an-print', root).onclick = () => window.print();
      $('#an-sched', root).onclick = () => scheduleReport(f, root);
      const scheduled = L.store.get('analitica.programacion', null);
      if (scheduled) $('#an-schedule-status', root).textContent = 'Programación simulada: ' + scheduled.frecuencia.toLowerCase() + ' · ' + scheduled.hora + ' · ' + scheduled.destino;
      if (q.exportar) $('#an-exp', root).click();
    }
  });

  L.route('/analitica/:kpi', {
    title: (p) => kpi(p.kpi).label, parent: '/analitica', block: 'Tablero analítico', module: 'M10 Analítica',
    rf: ['RF-11.03', 'RF-11.06', 'RF-16.02'], actors: ['Gerencias'],
    render: ({ kpi: id }, q) => {
      const f = filters(q), k = kpi(id), rows = select(f), routes = group(rows, 'ruta');
      return `<div class="page-head"><div class="titles"><h1>${esc(k.label)} por ruta</h1><p>${span(f)}</p><p>${esc(k.desc)} ${rows.length ? 'Resultado: ' + valueText(k, metrics[k.id](rows)) : ''}</p></div><div class="actions">
        <a class="btn btn-secondary" href="${href('/analitica', f)}">Volver al tablero filtrado</a><button type="button" class="btn btn-primary" id="dk-exp">Exportar detalle CSV</button></div></div>
        ${rows.length ? `<section class="card stack">${C.bar(routes.map(([label, rs]) => ({ label, value: metrics[k.id](rs), drill: routeFor('/analitica/' + k.id + '/ruta/' + label, f) })), { unit: k.unit === '%' ? '%' : '', label: k.label + ' por ruta' })}
          <ul class="list">${routes.map(([r, rs]) => `<li><a class="item-link" href="${href('/analitica/' + k.id + '/ruta/' + r, f)}">${r} · ${rs.length} pedidos · ${valueText(k, metrics[k.id](rs))} · Ver entregas</a></li>`).join('')}</ul></section>` : empty()}`;
    },
    mount: (root, _, q) => { $('#dk-exp', root).onclick = () => L.download('detalle_por_ruta.csv', csv(select(filters(q)), detailColumns)); }
  });

  L.route('/analitica/:kpi/ruta/:id', {
    title: (p) => (p.id ? 'Entregas de ' + p.id : 'Entregas de la ruta'), parent: (p) => '/analitica/' + kpi(p.kpi).id,
    block: 'Tablero analítico', module: 'M10 · M6', rf: ['RF-11.03', 'RF-06.06'], actors: ['Gerencias'],
    render: ({ kpi: id, id: route }, q) => {
      const f = filters(q), rows = select(f).filter((r) => r.ruta === route);
      return `<div class="page-head"><div class="titles"><h1>Entregas de ${esc(route)}</h1><p>${span(f)} · ${rows.length} pedidos.</p></div><div class="actions">
        <a class="btn btn-secondary" href="${href('/analitica/' + kpi(id).id, f)}">Volver al detalle filtrado</a><button type="button" class="btn btn-primary" id="dr-exp">Exportar entregas CSV</button></div></div>
        ${rows.length ? '<section class="card">' + rowsTable(rows) + '</section>' : empty()}`;
    },
    mount: (root, p, q) => { $('#dr-exp', root).onclick = () => L.download('entregas_' + p.id + '.csv', csv(select(filters(q)).filter((r) => r.ruta === p.id), detailColumns)); }
  });
})(window.LFX);
