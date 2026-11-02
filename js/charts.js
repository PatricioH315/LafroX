/* Gráficos SVG propios, sin dependencias externas.
   Tipos: barras, barras horizontales, líneas, área, circular (anillo), barras apiladas,
   mapa de calor, dispersión, indicador de aguja y minigráfico. */
(function (L) {
  const C = (i) => `var(--chart-${(i % 6) + 1})`;
  const esc = (s) => L.esc(s);
  const nice = (max) => { if (max <= 0) return 1; const p = Math.pow(10, Math.floor(Math.log10(max))); const n = max / p; return (n <= 1 ? 1 : n <= 2 ? 2 : n <= 5 ? 5 : 10) * p; };
  const fmtV = (v, unit = '') => (unit === '%' ? L.fmt.pct(v) : unit === '$' ? L.fmt.clp(v) : L.fmt.n(v, v % 1 ? 1 : 0) + (unit ? ' ' + unit : ''));
  const svg = (w, h, label, inner, style = '') => `<svg class="chart" viewBox="0 0 ${w} ${h}" role="img" aria-label="${esc(label)}" preserveAspectRatio="xMidYMid meet" ${style ? `style="${style}"` : ''}><title>${esc(label)}</title>${inner}</svg>`;

  // Tooltip compartido para todos los gráficos
  let tipEl;
  const showTip = (el) => {
    const t = el.getAttribute('data-tip');
    if (!t) return;
    if (!tipEl) { tipEl = document.createElement('div'); tipEl.className = 'chart-tip'; tipEl.setAttribute('aria-hidden', 'true'); document.body.appendChild(tipEl); }
    tipEl.textContent = t;
    const r = el.getBoundingClientRect();
    tipEl.style.left = r.left + r.width / 2 + 'px';
    tipEl.style.top = r.top + 'px';
    tipEl.style.display = 'block';
  };
  const hideTip = () => { if (tipEl) tipEl.style.display = 'none'; };
  document.addEventListener('mouseover', (e) => { const el = e.target.closest?.('.chart [data-tip]'); el ? showTip(el) : hideTip(); });
  document.addEventListener('focusin', (e) => { const el = e.target.closest?.('.chart [data-tip]'); el ? showTip(el) : hideTip(); });
  document.addEventListener('focusout', hideTip);
  window.addEventListener('hashchange', hideTip);

  const focusable = (drill, label) => (drill ? `class="clickable" tabindex="0" role="button" aria-label="${esc(label)}. Ver detalle" data-drill="${esc(drill)}"` : '');

  const yAxis = (W, H, pad, max, unit, ticks = 4) => {
    let g = '';
    for (let i = 0; i <= ticks; i++) {
      const v = (max / ticks) * i;
      const y = H - pad.b - ((H - pad.t - pad.b) * i) / ticks;
      g += `<line class="grid-line" x1="${pad.l}" x2="${W - pad.r}" y1="${y}" y2="${y}"/><text x="${pad.l - 8}" y="${y + 4}" text-anchor="end">${unit === '%' ? Math.round(v) + '%' : unit === '$' ? '$' + L.fmt.n(v / 1e6, 1) + 'M' : L.fmt.n(v)}</text>`;
    }
    return g;
  };

  L.charts = {
    bar(data, { w = 560, h = 260, unit = '', label = 'Gráfico de barras', target, color, highlight } = {}) {
      const pad = { t: 16, r: 12, b: 40, l: 48 };
      const max = nice(Math.max(...data.map((d) => d.value), target || 0) * 1.1);
      const bw = (w - pad.l - pad.r) / data.length;
      const y = (v) => h - pad.b - ((h - pad.t - pad.b) * v) / max;
      let g = yAxis(w, h, pad, max, unit);
      data.forEach((d, i) => {
        const x = pad.l + i * bw + bw * 0.18;
        const bh = h - pad.b - y(d.value);
        const fill = d.color || (highlight != null ? (i === highlight ? C(0) : 'var(--chart-5)') : color || C(0));
        g += `<rect x="${x}" y="${y(d.value)}" width="${bw * 0.64}" height="${Math.max(0, bh)}" rx="3" fill="${fill}" data-tip="${esc(d.label)}: ${fmtV(d.value, unit)}" ${focusable(d.drill, `${d.label}: ${fmtV(d.value, unit)}`)}><animate attributeName="height" from="0" to="${Math.max(0, bh)}" dur="0.5s" fill="freeze"/><animate attributeName="y" from="${h - pad.b}" to="${y(d.value)}" dur="0.5s" fill="freeze"/></rect>`;
        g += `<text x="${x + bw * 0.32}" y="${h - pad.b + 18}" text-anchor="middle">${esc(d.short || d.label)}</text>`;
      });
      if (target != null) g += `<line x1="${pad.l}" x2="${w - pad.r}" y1="${y(target)}" y2="${y(target)}" stroke="var(--c-ink)" stroke-dasharray="5 4" stroke-width="1.5"/><text x="${w - pad.r}" y="${y(target) - 6}" text-anchor="end" style="fill:var(--c-ink);font-weight:600">Meta ${fmtV(target, unit)}</text>`;
      g += `<line class="axis" x1="${pad.l}" x2="${w - pad.r}" y1="${h - pad.b}" y2="${h - pad.b}"/>`;
      return svg(w, h, label, g);
    },

    hbar(data, { w = 560, unit = '', label = 'Gráfico de barras horizontales', max: mx } = {}) {
      const rowH = 34, pad = { t: 8, r: 64, b: 8, l: 150 };
      const h = pad.t + pad.b + data.length * rowH;
      const max = mx || nice(Math.max(...data.map((d) => d.value)) * 1.05);
      let g = '';
      data.forEach((d, i) => {
        const y = pad.t + i * rowH;
        const bw = ((w - pad.l - pad.r) * d.value) / max;
        g += `<text x="${pad.l - 10}" y="${y + rowH / 2 + 4}" text-anchor="end" style="fill:var(--c-ink)">${esc(d.label)}</text>
          <rect x="${pad.l}" y="${y + 7}" width="${w - pad.l - pad.r}" height="${rowH - 14}" rx="4" fill="var(--c-line-soft)"/>
          <rect x="${pad.l}" y="${y + 7}" width="${bw}" height="${rowH - 14}" rx="4" fill="${d.color || C(i === 0 ? 0 : 1)}" data-tip="${esc(d.label)}: ${fmtV(d.value, unit)}" ${focusable(d.drill, `${d.label}: ${fmtV(d.value, unit)}`)}><animate attributeName="width" from="0" to="${bw}" dur="0.5s" fill="freeze"/></rect>
          <text x="${pad.l + bw + 8}" y="${y + rowH / 2 + 4}" style="fill:var(--c-ink);font-weight:600">${fmtV(d.value, unit)}</text>`;
      });
      return svg(w, h, label, g);
    },

    line(labels, series, { w = 560, h = 260, unit = '', label = 'Gráfico de líneas', target, area = false, min = 0 } = {}) {
      const pad = { t: 16, r: 16, b: 40, l: 48 };
      const all = series.flatMap((s) => s.values).concat(target || 0);
      const max = unit === '%' ? Math.min(100, nice(Math.max(...all) * 1.02)) : nice(Math.max(...all) * 1.1);
      const lo = min;
      const x = (i) => pad.l + ((w - pad.l - pad.r) * i) / Math.max(1, labels.length - 1);
      const y = (v) => h - pad.b - ((h - pad.t - pad.b) * (v - lo)) / (max - lo);
      let g = '';
      for (let i = 0; i <= 4; i++) { const v = lo + ((max - lo) / 4) * i; g += `<line class="grid-line" x1="${pad.l}" x2="${w - pad.r}" y1="${y(v)}" y2="${y(v)}"/><text x="${pad.l - 8}" y="${y(v) + 4}" text-anchor="end">${unit === '%' ? Math.round(v) + '%' : L.fmt.n(v)}</text>`; }
      const step = Math.ceil(labels.length / 8);
      labels.forEach((l, i) => { if (i % step === 0 || i === labels.length - 1) g += `<text x="${x(i)}" y="${h - pad.b + 18}" text-anchor="middle">${esc(l)}</text>`; });
      if (target != null) g += `<line x1="${pad.l}" x2="${w - pad.r}" y1="${y(target)}" y2="${y(target)}" stroke="var(--c-ink)" stroke-dasharray="5 4" stroke-width="1.5"/><text x="${w - pad.r}" y="${y(target) - 6}" text-anchor="end" style="fill:var(--c-ink);font-weight:600">Meta ${fmtV(target, unit)}</text>`;
      series.forEach((s, si) => {
        const col = s.color || C(si);
        const pts = s.values.map((v, i) => `${x(i)},${y(v)}`).join(' ');
        if (area) g += `<polygon points="${x(0)},${h - pad.b} ${pts} ${x(s.values.length - 1)},${h - pad.b}" fill="${col}" opacity="${si ? 0.12 : 0.18}"/>`;
        g += `<polyline points="${pts}" fill="none" stroke="${col}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" ${s.dashed ? 'stroke-dasharray="6 5"' : ''} pathLength="1" style="stroke-dasharray:${s.dashed ? '0.012 0.01' : '1'};stroke-dashoffset:${s.dashed ? 0 : 1};animation:${s.dashed ? 'none' : 'draw 0.9s ease forwards'}"/>`;
        s.values.forEach((v, i) => { g += `<circle cx="${x(i)}" cy="${y(v)}" r="${s.values.length > 20 ? 3 : 4.5}" fill="var(--c-surface)" stroke="${col}" stroke-width="2" data-tip="${esc(s.name)} · ${esc(labels[i])}: ${fmtV(v, unit)}" ${focusable(s.drill?.[i], `${s.name} ${labels[i]}: ${fmtV(v, unit)}`)}/>`; });
      });
      g += `<line class="axis" x1="${pad.l}" x2="${w - pad.r}" y1="${h - pad.b}" y2="${h - pad.b}"/>`;
      return svg(w, h, label, `<style>@keyframes draw{to{stroke-dashoffset:0}}</style>${g}`);
    },

    area(labels, series, opts = {}) { return L.charts.line(labels, series, { ...opts, area: true, label: opts.label || 'Gráfico de área' }); },

    donut(data, { size = 220, label = 'Gráfico circular', center = '', centerSub = '' } = {}) {
      const total = data.reduce((a, d) => a + d.value, 0);
      const r = 80, cx = size / 2, cy = size / 2, sw = 30, circ = 2 * Math.PI * r;
      let off = 0, g = '';
      data.forEach((d, i) => {
        const len = (d.value / total) * circ;
        g += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${d.color || C(i)}" stroke-width="${sw}" stroke-dasharray="${len - 2} ${circ - len + 2}" stroke-dashoffset="${-off}" transform="rotate(-90 ${cx} ${cy})" data-tip="${esc(d.label)}: ${fmtV(d.value)} (${L.fmt.pct((d.value / total) * 100)})" ${focusable(d.drill, `${d.label}: ${L.fmt.pct((d.value / total) * 100)}`)}/>`;
        off += len;
      });
      g += `<text x="${cx}" y="${cy + 2}" text-anchor="middle" style="fill:var(--c-ink);font-size:26px;font-weight:700">${esc(center)}</text><text x="${cx}" y="${cy + 22}" text-anchor="middle">${esc(centerSub)}</text>`;
      return svg(size, size, label, g, `max-width:${size}px;flex:0 0 auto`);
    },

    legend(items) { return `<ul class="legend">${items.map((it, i) => `<li><i style="background:${it.color || C(i)}"></i>${esc(it.label)}${it.value != null ? ` · <strong style="color:var(--c-ink)">${esc(it.value)}</strong>` : ''}</li>`).join('')}</ul>`; },

    stacked(labels, series, { w = 560, h = 260, label = 'Gráfico de barras apiladas', unit = '', percent = false } = {}) {
      const pad = { t: 16, r: 12, b: 40, l: 48 };
      const totals = labels.map((_, i) => series.reduce((a, s) => a + s.values[i], 0));
      const max = percent ? 100 : nice(Math.max(...totals) * 1.1);
      const bw = (w - pad.l - pad.r) / labels.length;
      const y = (v) => h - pad.b - ((h - pad.t - pad.b) * v) / max;
      let g = yAxis(w, h, pad, max, percent ? '%' : unit);
      labels.forEach((l, i) => {
        let acc = 0;
        const x = pad.l + i * bw + bw * 0.2;
        series.forEach((s, si) => {
          const v = percent ? (s.values[i] / totals[i]) * 100 : s.values[i];
          g += `<rect x="${x}" y="${y(acc + v)}" width="${bw * 0.6}" height="${Math.max(0, y(acc) - y(acc + v) - 1)}" fill="${s.color || C(si)}" data-tip="${esc(l)} · ${esc(s.name)}: ${percent ? L.fmt.pct(v) : fmtV(s.values[i], unit)}"/>`;
          acc += v;
        });
        g += `<text x="${x + bw * 0.3}" y="${h - pad.b + 18}" text-anchor="middle">${esc(l)}</text>`;
      });
      g += `<line class="axis" x1="${pad.l}" x2="${w - pad.r}" y1="${h - pad.b}" y2="${h - pad.b}"/>`;
      return svg(w, h, label, g);
    },

    heatmap(rows, cols, matrix, { w = 560, label = 'Mapa de calor', unit = '' } = {}) {
      const pad = { t: 24, r: 8, b: 8, l: 44 };
      const cw = (w - pad.l - pad.r) / cols.length, ch = 30;
      const h = pad.t + pad.b + rows.length * ch;
      const flat = matrix.flat(), mx = Math.max(...flat), mn = Math.min(...flat);
      let g = '';
      cols.forEach((c, j) => (g += `<text x="${pad.l + j * cw + cw / 2}" y="${pad.t - 8}" text-anchor="middle">${esc(c)}</text>`));
      rows.forEach((r, i) => {
        g += `<text x="${pad.l - 8}" y="${pad.t + i * ch + ch / 2 + 4}" text-anchor="end">${esc(r)}</text>`;
        cols.forEach((c, j) => {
          const v = matrix[i][j];
          const t = (v - mn) / (mx - mn || 1);
          g += `<rect x="${pad.l + j * cw + 1}" y="${pad.t + i * ch + 1}" width="${cw - 2}" height="${ch - 2}" rx="3" fill="var(--chart-1)" fill-opacity="${(0.08 + t * 0.92).toFixed(2)}" data-tip="${esc(r)} ${esc(c)}: ${fmtV(v, unit)}"/>`;
        });
      });
      return svg(w, h, label, g);
    },

    scatter(points, { w = 560, h = 300, label = 'Gráfico de dispersión', xLabel = '', yLabel = '', xUnit = '', yUnit = '', quadrants } = {}) {
      const pad = { t: 16, r: 16, b: 48, l: 60 };
      const mxX = nice(Math.max(...points.map((p) => p.x)) * 1.1), mxY = nice(Math.max(...points.map((p) => p.y)) * 1.1);
      const x = (v) => pad.l + ((w - pad.l - pad.r) * v) / mxX;
      const y = (v) => h - pad.b - ((h - pad.t - pad.b) * v) / mxY;
      let g = '';
      for (let i = 0; i <= 4; i++) {
        g += `<line class="grid-line" x1="${pad.l}" x2="${w - pad.r}" y1="${y((mxY / 4) * i)}" y2="${y((mxY / 4) * i)}"/><text x="${pad.l - 8}" y="${y((mxY / 4) * i) + 4}" text-anchor="end">${fmtV((mxY / 4) * i, yUnit)}</text>`;
        g += `<text x="${x((mxX / 4) * i)}" y="${h - pad.b + 18}" text-anchor="middle">${fmtV((mxX / 4) * i, xUnit)}</text>`;
      }
      if (quadrants) g += `<line x1="${x(quadrants.x)}" x2="${x(quadrants.x)}" y1="${pad.t}" y2="${h - pad.b}" stroke="var(--c-ink)" stroke-dasharray="4 4"/><line x1="${pad.l}" x2="${w - pad.r}" y1="${y(quadrants.y)}" y2="${y(quadrants.y)}" stroke="var(--c-ink)" stroke-dasharray="4 4"/>`;
      points.forEach((p) => (g += `<circle cx="${x(p.x)}" cy="${y(p.y)}" r="${p.r || 6}" fill="${p.color || C(0)}" fill-opacity="0.75" stroke="var(--c-surface)" data-tip="${esc(p.label)}: ${fmtV(p.x, xUnit)} · ${fmtV(p.y, yUnit)}" ${focusable(p.drill, p.label)}/>`));
      g += `<text x="${(pad.l + w - pad.r) / 2}" y="${h - 8}" text-anchor="middle" style="font-weight:600">${esc(xLabel)}</text><text transform="translate(14 ${(pad.t + h - pad.b) / 2}) rotate(-90)" text-anchor="middle" style="font-weight:600">${esc(yLabel)}</text>`;
      return svg(w, h, label, g);
    },

    gauge(value, { min = 0, max = 100, target, label = 'Indicador', unit = '%', w = 260 } = {}) {
      const cx = w / 2, cy = 130, r = 100;
      const ang = (v) => Math.PI + (Math.PI * (v - min)) / (max - min);
      const pt = (v, rr = r) => [cx + rr * Math.cos(ang(v)), cy + rr * Math.sin(ang(v))];
      const arc = (a, b, col, sw = 20) => { const [x1, y1] = pt(a), [x2, y2] = pt(b); return `<path d="M${x1} ${y1} A${r} ${r} 0 0 1 ${x2} ${y2}" fill="none" stroke="${col}" stroke-width="${sw}" stroke-linecap="butt"/>`; };
      let g = arc(min, max, 'var(--c-line-soft)') + arc(min, value, 'var(--chart-1)');
      if (target != null) { const [a, b] = pt(target, r - 16), [c, d] = pt(target, r + 16); g += `<line x1="${a}" y1="${b}" x2="${c}" y2="${d}" stroke="var(--c-ink)" stroke-width="3"/>`; }
      g += `<text x="${cx}" y="${cy - 14}" text-anchor="middle" style="fill:var(--c-ink);font-size:32px;font-weight:700">${fmtV(value, unit)}</text>`;
      g += `<text x="${cx - r}" y="${cy + 20}" text-anchor="middle">${min}${unit === '%' ? '%' : ''}</text><text x="${cx + r}" y="${cy + 20}" text-anchor="middle">${max}${unit === '%' ? '%' : ''}</text>`;
      if (target != null) g += `<text x="${cx}" y="${cy + 20}" text-anchor="middle">Meta ${fmtV(target, unit)}</text>`;
      return svg(w, 160, `${label}: ${fmtV(value, unit)}${target != null ? `, meta ${fmtV(target, unit)}` : ''}`, g);
    },

    spark(values, { w = 160, h = 36, color = 'var(--chart-1)' } = {}) {
      const mx = Math.max(...values), mn = Math.min(...values);
      const pts = values.map((v, i) => `${(w * i) / (values.length - 1)},${h - 3 - ((h - 6) * (v - mn)) / (mx - mn || 1)}`).join(' ');
      return `<svg class="chart" viewBox="0 0 ${w} ${h}" aria-hidden="true" preserveAspectRatio="none" style="height:${h}px"><polyline points="${pts}" fill="none" stroke="${color}" stroke-width="2" stroke-linejoin="round"/></svg>`;
    },

    // Tabla accesible equivalente al gráfico
    table(headers, rows) {
      return `<div class="table-wrap"><table class="table"><thead><tr>${headers.map((h) => `<th>${esc(h)}</th>`).join('')}</tr></thead><tbody>${rows.map((r) => `<tr>${r.map((c) => `<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
    }
  };

  // Navegación por profundización desde cualquier gráfico
  document.addEventListener('click', (e) => { const d = e.target.closest?.('.chart [data-drill]'); if (d) L.go(d.getAttribute('data-drill')); });
  document.addEventListener('keydown', (e) => { const d = e.target.closest?.('.chart [data-drill]'); if (d && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); L.go(d.getAttribute('data-drill')); } });
})(window.LFX = window.LFX || {});
