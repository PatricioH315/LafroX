// C. Ejecucion (laminas 17-29): metodologia, RUP, Gantt, EDT, calidad, RBS y matriz de exposicion.
module.exports = function ejecucion(ctx) {
  const { kit, D, fmt, pct, OVERRIDES } = ctx;
  const { pres, C, H, B, X0, W, XR, Y0, YB, T, card, darkCard, pill, circle, deco, arc, RINGS, QUARTER, lineOpt } = kit;
  const SEC = "Ejecución";
  const ALEX = "Alex Aravena", MM = "Maximiliano Miño", GC = "Guillermo Castillo";
  const doc = D.documentos;
  const hz = D.parametros.horizonte_meses;
  const E = doc.etapas;

  const decorC = (s) => {
    deco(s, "cuarto-circulo", 1, { x: 17.63, y: -3.06, w: 7.02, h: 7.02 });
  };

  // ------------------------------------------------------------ 17 Metodologia
  const msub = (s) => ctx.N(s, "!!msub", "PMBOK + RUP + DevSecOps", X0, 2.5, 9, 0.5, { fontSize: 22, bold: true, fontFace: H, color: C.accent1 });
  {
    const s = ctx.add("CONTENIDO", SEC, ALEX, "6:50",
      `Trabajamos con PMBOK adaptado a ${hz} meses, con valor ganado y alerta si el SPI o el CPI bajan de 0,90. Las entregas son incrementales, en iteraciones de dos semanas, y no se despliega nada en septiembre ni en diciembre. El gobierno tiene un ritmo claro: seguimiento semanal, comité de proyecto quincenal, comité ejecutivo y de arquitectura mensual, y comité de operación desde el mes 13.`);
    decorC(s);
    ctx.title(s, "Metodología");
    msub(s);
    T(s, "CÓMO TRABAJAMOS", X0, 3.2, 6, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, objectName: "!!cab_1" });
    const steps = [
      [`PMBOK adaptado a ${hz} meses`, "valor ganado: alerta si SPI o CPI < 0,90"],
      ["Entregas incrementales", "sin despliegues en septiembre ni diciembre"],
      ["Iteraciones de 2 semanas", "cada cambio pasa por puertas que bloquean"],
      ["Control de tareas Kanban", "flujo del equipo visible para todos"],
    ];
    steps.forEach((st, i) => {
      const y = 3.85 + i * 1.5;
      const c = s.addText(String(i + 1), { shape: pres.shapes.OVAL, x: X0, y, w: 0.7, h: 0.7, fill: { color: i % 2 === 0 ? C.accent1 : C.text1 }, color: C.background1, bold: true, fontSize: 20, fontFace: H, align: "center", valign: "middle", margin: 0, objectName: `!!mstep${i}` });
      T(s, [
        { text: st[0], options: { fontSize: 22, bold: true, fontFace: H, breakLine: true } },
        { text: st[1], options: { fontSize: 16, color: C.accent3 } },
      ], X0 + 1.0, y - 0.1, 6.9, 1.0, { valign: "middle", objectName: `!!msteptxt_${i}` });
    });
    T(s, "RITMO DE GOBIERNO", 10.2, 3.2, 6, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, objectName: "!!cab_2" });
    const gov = [["Semanal", "Seguimiento"], ["Quincenal", "Comité de Proyecto"], ["Mensual", "Ejecutivo y Arquitectura"], [`Mes 13–${hz}`, "Comité de Operación"]];
    gov.forEach((g, i) => {
      const y = 3.85 + i * 1.5;
      s.addText(g[0], { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.42, x: 10.2, y: y - 0.08, w: 2.6, h: 0.86, fill: { color: i === 3 ? C.text1 : C.accent1 }, color: C.background1, bold: true, fontSize: 18, fontFace: H, align: "center", valign: "middle", margin: 0, objectName: `!!gov${i}` });
      T(s, g[1], 13.1, y - 0.08, 5.3, 0.86, { fontSize: 22, bold: true, fontFace: H, valign: "middle", objectName: `!!govtxt_${i}` });
    });
    RINGS(s, 3.4, 7.15, 11.2, 1);
  }

  // ------------------------------------------------------------ 18 RUP + DevSecOps
  {
    const s = ctx.add("CONTENIDO", SEC, ALEX, "7:05",
      "Las fases de RUP ordenan el trabajo: inicio, elaboración, construcción y transición; la construcción concentra la mayor parte de los paquetes de la EDT. Cada cambio recorre además el ciclo DevSecOps, con auditorías, análisis estático, pruebas de contrato y medición de cobertura, y se controla en las puertas G1 a G3 del plan de calidad.");
    decorC(s);
    ctx.title(s, "Metodología");
    msub(s);
    const fases = doc.edt.fases.slice(0, 4);
    const totPt = fases.reduce((a, f) => a + f.pt, 0);
    T(s, "FASES RUP · PAQUETES DE TRABAJO DE LA EDT", X0, 3.2, 12, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, objectName: "!!cab_1" });
    const colors = [C.text1, C.accent2, C.accent1, C.accent4];
    let x = X0;
    fases.forEach((f, i) => {
      const w = (W * f.pt) / totPt;
      const narrow = w < 1.6;
      s.addText(narrow ? "" : [
        { text: f.nombre, options: { fontSize: 16, bold: true, fontFace: H, breakLine: true } },
        { text: `${f.pt} paquetes`, options: { fontSize: 16 } },
      ], { shape: pres.shapes.RECTANGLE, x, y: 3.7, w: w - 0.04, h: 0.95, fill: { color: colors[i] }, color: i === 3 ? C.text1 : C.background1, align: "left", valign: "middle", margin: [0, 0, 0, 0.12], objectName: `!!rup${i}` });
      if (narrow) T(s, `${f.nombre}: ${f.pt} paquetes`, x, 4.75, 3.2, 0.35, { fontSize: 16, color: C.accent3, objectName: `!!ruptxt_${i}` });
      x += w;
    });
    T(s, "DEVSECOPS · CICLO DE CADA CAMBIO", X0, 5.45, 12, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, objectName: "!!cab_2" });
    ["Auditorías", "Análisis estático", "Pruebas de contrato", "Medición de cobertura"].forEach((t, i) => {
      const px = X0 + i * 3.9;
      pill(s, t, px, 5.95, 3.3, 0.8, { fill: { color: C.accent1 }, color: C.background1, bold: true, fontSize: 18, objectName: `!!ciclo_${i + 1}` });
      if (i < 3) s.addShape(pres.shapes.RIGHT_ARROW, { x: px + 3.38, y: 6.2, w: 0.44, h: 0.3, fill: { color: C.text1 }, objectName: `!!ciclo_flecha_${i + 1}` });
    });
    T(s, "DÓNDE SE APLICA", X0, 7.2, 12, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, objectName: "!!cab_3" });
    const q = doc.calidad;
    const gates = [
      ["G1", "Solicitud de fusión", "revisión por pares y secretos"],
      ["G2", "Integración continua", `cobertura ≥ ${q.cobertura_negocio_pct} % negocio y ${q.cobertura_global_pct} % global`],
      ["G3", "Promoción a QA", "sin vulnerabilidades altas"],
    ];
    gates.forEach((g, i) => {
      const gx = X0 + i * 5.7, gw = 5.4;
      card(s, gx, 7.7, gw, 1.9, { objectName: `!!gate_${i + 1}` });
      s.addText(g[0], { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.12, x: gx + 0.3, y: 8.05, w: 0.9, h: 0.9, fill: { color: C.text1 }, color: C.background1, bold: true, fontSize: 20, fontFace: H, align: "center", valign: "middle", margin: 0, objectName: `!!gatenum_${i + 1}` });
      T(s, [
        { text: g[1], options: { fontSize: 20, bold: true, fontFace: H, breakLine: true } },
        { text: g[2], options: { fontSize: 16, color: C.accent3 } },
      ], gx + 1.45, 7.85, gw - 1.65, 1.5, { valign: "middle", objectName: `!!gatetxt_${i + 1}` });
    });
    RINGS(s, 3.4, 7.15, 11.2, 1);
    deco(s, "anillos", 2, { x: 4.43, y: 4.06, w: 11.2, h: 2.74, transparency: 95 });
  }

  // ------------------------------------------------------------ 19 Gantt frentes
  const GV = {}; // gv_k -> [mes inicio, mes fin, relleno]
  const FILL = { dis: C.accent2, e1: C.accent1, mig: C.accent1, mb1: C.accent4, e2: C.text1, mb2: C.accent5, et1: C.accent1, et2: C.accent4, cam: C.accent6, op: C.accent2 };
  const ROWS = [
    // [gv, etiqueta, mes ini, mes fin, relleno]
    [6, "Etapa 1", E.etapa1[0], E.etapa1[1], FILL.et1],
    [7, "Etapa 2", E.etapa2[0], E.etapa2[1], FILL.et2],
    [10, `Operación → m${hz}`, E.operacion[0], hz, FILL.op],
    [0, "Diseño e infraestructura", 1, 12, FILL.dis],
    [1, "Construcción y pruebas E1", 5, 10, FILL.e1],
    [2, "Migración de datos", 7, 12, FILL.mig],
    [3, "Marcha blanca E1", 13, 15, FILL.mb1],
    [4, "Construcción y pruebas E2", 13, 18, FILL.e2],
    [5, "Marcha blanca E2", 19, 20, FILL.mb2],
    [9, "Gestión del cambio", 2, 21, FILL.cam],
  ];
  {
    const s = ctx.add("COMPACTO", SEC, ALEX, "7:20",
      "El proyecto se divide en dos niveles: tres bloques contractuales, que son la Etapa 1, la Etapa 2 y la Operación, solapados en los meses 13 a 15 y 19 a 20, y ocho frentes de trabajo, cada uno con un responsable nominado. Esta estructura permite que la Etapa 2 avance mientras la Etapa 1 está en marcha blanca.");
    deco(s, "mosaico", 2, { x: 17.6, y: -2.6, w: 4.5, h: 4.5 });
    RINGS(s, -2.65, 9.6, 11.45, 1);
    ctx.title(s, "Cómo se divide el proyecto");
    T(s, [
      { text: "2 etapas + operación", options: { fontSize: 36, bold: true, fontFace: H, breakLine: true } },
      { text: "8 frentes con responsable", options: { fontSize: 28, bold: true, fontFace: H, breakLine: true } },
      { text: " ", options: { fontSize: 16, breakLine: true } },
      { text: "Solapes: meses 13–15 y 19–20", options: { fontSize: 22, bold: true, color: C.accent1 } },
    ], X0, 3.6, 6.0, 3.8, { objectName: "!!resumen" });
    // bloques a escala de 56 meses
    const gx = 11.6, gw = 6.8, mw = gw / hz;
    const mx = (m) => gx + (m - 1) * mw;
    T(s, "BLOQUES", 8.0, 1.85, 3, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent1 });
    [[6, "Etapa 1", 2.4], [7, "Etapa 2", 3.0], [10, "Operación", 3.6]].forEach(([gv, lbl, y]) => {
      const row = ROWS.find((r) => r[0] === gv);
      T(s, lbl, 8.0, y - 0.02, 3.4, 0.4, { fontSize: 18, bold: true, fontFace: H, valign: "middle" });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: mx(row[2]), y, w: (row[3] - row[2] + 1) * mw, h: 0.36, rectRadius: 0.1, fill: { color: row[4] }, line: { color: row[4], width: 0.5 }, objectName: `!!gv_${gv}` });
    });
    [1, 13, 21, hz].forEach((m) => T(s, `m${m}`, mx(m) - 0.3, 4.05, 0.7, 0.3, { fontSize: 14, color: C.accent3, align: "center" }));
    T(s, "FRENTES", 8.0, 4.7, 3, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent1 });
    const fr = [
      ["F1 Dirección", "Jefe de Proyecto"], ["F2 Arquitectura", "Arquitecto de Solución"], ["F3 Construcción E1", "Líder de Desarrollo"],
      ["F4 Construcción E2", "Líder de Desarrollo"], ["F5 Plataforma", "Líder de Operación/SRE"], ["F6 Calidad", "Líder de Calidad"],
      ["F7 Implantación", "Líder de Implantación"], ["F8 Operación", "Líder de Operación/SRE"],
    ];
    fr.forEach((f, i) => {
      const y = 5.15 + i * 0.6;
      T(s, f[0], 8.0, y, 4.3, 0.5, { fontSize: 18, bold: true, fontFace: H, valign: "middle" });
      T(s, f[1], 12.4, y, 6.0, 0.5, { fontSize: 18, color: C.accent3, valign: "middle" });
    });
    ctx.src(s, "Fuente: Informe 2, tablas 7.52 y 7.1.", 10.2);
  }

  // ------------------------------------------------------------ 20-21 Gantt colapsado / desplegado
  const ganttFrame = (s, collapsed) => {
    deco(s, "mosaico", 2, { x: 17.6, y: -2.6, w: 4.5, h: 4.5 });
    RINGS(s, -2.65, 9.6, 11.45, 1);
    ctx.title(s, "Gantt de implementación");
    ctx.N(s, "!!gsub", "Meses 1–24 · actividades, hitos y congelamientos (gris)", X0, 1.4, 12, 0.4, { fontSize: 18, color: C.accent3 });
    const gx = 5.9, gw = XR - gx, cw = gw / 24;
    const rowY = (i) => 2.95 + i * 0.62;
    // congelamientos: sep y dic (meses 8, 11, 20, 23)
    [[8, "Sep"], [11, "Dic"], [20, "Sep"], [23, "Dic"]].forEach(([m, l], i) => {
      s.addShape(pres.shapes.RECTANGLE, { x: gx + (m - 1) * cw, y: 2.45, w: cw, h: 7.45, fill: { color: "E9E9E9" }, line: { color: "E9E9E9", width: 0 }, objectName: `!!congela_${i + 1}` });
      T(s, l, gx + (m - 1) * cw - 0.2, 2.1, cw + 0.4, 0.3, { fontSize: 13, bold: true, color: C.accent3, align: "center", objectName: `!!congela_l${i + 1}` });
    });
    for (let m = 1; m <= 24; m++) T(s, String(m), gx + (m - 1) * cw, 2.5, cw, 0.3, { fontSize: 13, color: C.accent3, align: "center", objectName: `!!mes_${m}` });
    ROWS.forEach((r, i) => {
      const y = rowY(i);
      ctx.N(s, `!!glabel_${r[0]}`, r[1], X0, y, gx - X0 - 0.2, 0.4, { fontSize: 16, bold: r[0] >= 6 && r[0] !== 9, fontFace: r[0] >= 6 && r[0] !== 9 ? H : B, valign: "middle" });
      const x0 = gx + (r[2] - 1) * cw;
      const wfull = (Math.min(r[3], 24) - r[2] + 1) * cw;
      s.addText(!collapsed && r[0] === 10 ? `→ m${hz}` : "", { shape: pres.shapes.RECTANGLE, x: x0, y, w: collapsed ? 0.02 : wfull - 0.03, h: 0.4, fill: { color: r[4] }, line: { color: r[4], width: 0 }, color: C.background1, bold: true, fontSize: 14, align: "center", valign: "middle", margin: 0, objectName: `!!gv_${r[0]}` });
    });
    return { gx, cw, yH: rowY(ROWS.length) };
  };
  {
    const s = ctx.add("COMPACTO", SEC, ALEX, "7:22", "(Transición automática: el diagrama se despliega en la lámina siguiente.)");
    OVERRIDES[ctx.num()] = { advTm: 100, durMs: 1400 };
    const g = ganttFrame(s, true);
    ctx.N(s, "!!ghitos", "Hitos", X0, g.yH, 4, 0.4, { fontSize: 16, bold: true, fontFace: H, valign: "middle" });
  }
  {
    const s = ctx.add("COMPACTO", SEC, ALEX, "7:45",
      `Aquí vemos el cronograma mes a mes. En gris, los congelamientos de septiembre y diciembre, en los que no se despliega nada. La Etapa 1 corre del mes ${E.etapa1[0]} al ${E.etapa1[1]} y pasa a producción en el hito H7, mes ${E.h7_mes}; la Etapa 2 corre del mes ${E.etapa2[0]} al ${E.etapa2[1]} y pasa a producción en el hito H12, mes ${E.h12_mes}. La operación se extiende del mes ${E.operacion[0]} al ${E.operacion[1]}.`);
    const g = ganttFrame(s, false);
    ctx.N(s, "!!ghitos", "Hitos", X0, g.yH, 4, 0.4, { fontSize: 16, bold: true, fontFace: H, valign: "middle" });
    D.hitos.forEach((h) => {
      const cx = g.gx + (h.mes - 0.5) * g.cw;
      const key = h.hito === "H7" || h.hito === "H12";
      s.addShape(pres.shapes.DIAMOND, { x: cx - 0.17, y: g.yH + 0.03, w: 0.34, h: 0.34, fill: { color: key ? C.accent1 : C.text1 }, line: { color: key ? C.accent1 : C.text1, width: 0 }, objectName: `!!hito_${h.hito}` });
      T(s, h.hito, cx - 0.35, g.yH + 0.42, 0.7, 0.3, { fontSize: 13, bold: key, color: key ? C.accent1 : C.accent3, align: "center", objectName: `!!hitol_${h.hito}` });
    });
  }

  // ------------------------------------------------------------ 22-24 EDT
  const edt = (s, active, nCuentas) => {
    deco(s, "mosaico", 2, { x: 16.35, y: -1.62, w: 4.5, h: 4.5 });
    RINGS(s, -2.47, 9.69, 11.2, 1);
    ctx.title(s, "EDT: así se organiza el trabajo");
    const total = doc.edt.fases.reduce((a, f) => a + f.pt, 0);
    const totalCc = doc.edt.fases.reduce((a, f) => a + f.cc, 0);
    s.addText(`Proyecto LafroX · ${total} paquetes de trabajo`, { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.12, x: 6.9, y: 1.7, w: 6.2, h: 0.75, fill: { color: C.text1 }, color: C.background1, bold: true, fontSize: 18, fontFace: H, align: "center", valign: "middle", margin: 0, objectName: "!!edtroot" });
    const gap = 0.12, bw = (W - 8 * gap) / 9, by = 3.2, bh = 2.1;
    s.addShape(pres.shapes.LINE, { x: 10.0, y: 2.45, w: 0, h: 0.4, line: lineOpt("C7C7C7", 1), objectName: "!!edtline_0" });
    s.addShape(pres.shapes.LINE, { x: X0 + bw / 2, y: 2.85, w: 8 * (bw + gap), h: 0, line: lineOpt("C7C7C7", 1), objectName: "!!edtline_h" });
    doc.edt.fases.forEach((f, i) => {
      const x = X0 + i * (bw + gap), on = active === f.n, dim = active && !on;
      s.addShape(pres.shapes.LINE, { x: x + bw / 2, y: 2.85, w: 0, h: 0.35, line: lineOpt("C7C7C7", 1), objectName: `!!edtline_${f.n}` });
      s.addText([
        { text: `Fase ${f.n}`, options: { fontSize: 16, bold: true, fontFace: H, color: on ? C.background1 : dim ? C.accent5 : C.accent1, breakLine: true } },
        { text: f.nombre, options: { fontSize: 18, bold: true, fontFace: H, color: on ? C.background1 : dim ? C.accent5 : C.text1 } },
      ], { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.1, x, y: on ? by - 0.1 : by, w: bw, h: on ? bh + 0.35 : bh, fill: { color: on ? C.accent1 : C.background2 }, line: { color: on ? C.accent1 : C.background2, width: 0.5 }, align: "left", valign: "top", margin: [0.12, 0.1, 0, 0.12], objectName: `!!ph${f.n}` });
      T(s, `${f.cc} CC · ${f.pt} PT`, x + 0.12, (on ? by - 0.1 : by) + (on ? 2.0 : 1.7), bw - 0.2, 0.35, { fontSize: 16, bold: true, color: on ? C.background1 : dim ? C.accent5 : C.accent3, objectName: `!!phcc${f.n}` });
      const dotC = [1, 2, 3, 4].includes(f.n) ? C.accent1 : f.n === 8 ? C.text1 : C.accent3;
      for (let k = 0; k < f.cc; k++) {
        s.addShape(pres.shapes.RECTANGLE, { x: x + 0.12 + (k % 5) * 0.3, y: 5.75 + Math.floor(k / 5) * 0.3, w: 0.25, h: 0.25, fill: { color: dim ? "D8D8D8" : dotC }, line: { color: dim ? "D8D8D8" : dotC, width: 0 }, objectName: `!!edt_cc_${f.n}_${k + 1}` });
      }
    });
    if (!active) T(s, `${doc.edt.fases.length} fases · ${totalCc} cuentas de control (CC) · ${total} paquetes de trabajo (PT)`, X0, 7.0, W, 0.35, { fontSize: 16, color: C.accent3, objectName: "!!edtleyenda" });
  };
  const ccBlock = (s, fase) => {
    const f = doc.edt.fases.find((x) => x.n === fase);
    const names = doc.edt.cuentas[String(fase)];
    T(s, `FASE ${f.n} · ${f.nombre.toUpperCase()} · ${f.cc} CUENTAS DE CONTROL`, X0, 7.0, W, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent1, objectName: "!!edtleyenda" });
    const perRow = names.length > 6 ? 6 : names.length, cw = (W - (perRow - 1) * 0.15) / perRow, ch = 1.15;
    names.forEach((nm, i) => {
      const x = X0 + (i % perRow) * (cw + 0.15), y = 7.55 + Math.floor(i / perRow) * (ch + 0.15);
      card(s, x, y, cw, ch, { objectName: `!!cc_${i + 1}` });
      T(s, `${f.n}.${i + 1}`, x + 0.2, y + 0.12, cw - 0.4, 0.3, { fontSize: 16, bold: true, fontFace: H, color: C.accent1, objectName: `!!ccn_${i + 1}` });
      T(s, nm, x + 0.2, y + 0.45, cw - 0.4, 0.65, { fontSize: 16, bold: true, fontFace: H, objectName: `!!cct_${i + 1}` });
    });
  };
  {
    const s = ctx.add("COMPACTO", SEC, ALEX, "8:00",
      `La estructura de desglose del trabajo organiza el proyecto en ${doc.edt.fases.length} fases, ${doc.edt.fases.reduce((a, f) => a + f.cc, 0)} cuentas de control y ${doc.edt.fases.reduce((a, f) => a + f.pt, 0)} paquetes de trabajo. Las fases uno a cuatro siguen la metodología RUP y se ejecutan una vez por etapa; las demás cubren adquisiciones, infraestructura, capacitación, operación y cierre. Recorramos dos de ellas.`);
    edt(s, null);
  }
  {
    const f = doc.edt.fases[2];
    const s = ctx.add("COMPACTO", SEC, ALEX, "8:15",
      `La fase de construcción es la más grande: ${f.cc} cuentas de control y ${f.pt} paquetes de trabajo. Incluye ambientes y entrega continua, servicios de nube, la base compartida, los módulos de cada etapa, las integraciones, la migración de datos, las pruebas, las innovaciones y la documentación.`);
    edt(s, 3);
    ccBlock(s, 3);
  }
  {
    const f = doc.edt.fases[7];
    const s = ctx.add("COMPACTO", SEC, GC, "8:30",
      `La fase de operación y soporte cubre los ${D.parametros.horizonte_meses - E.operacion[0] + 1} meses de servicio posteriores a la puesta en producción: ${f.cc} cuentas de control con ${f.pt} paquetes. Contempla servicios de operación, mantenimiento fuera de los congelamientos, innovaciones, informes periódicos y la transferencia ordenada al término del contrato.`);
    edt(s, 8);
    ccBlock(s, 8);
  }

  // ------------------------------------------------------------ 25 Calidad
  {
    const q = doc.calidad;
    const s = ctx.add("COMPACTO", SEC, MM, "9:00",
      `Nuestra calidad se mide con criterios de aceptación explícitos, no con promesas. En desempeño, el percentil 95 de la preparación debe ser de un segundo o menos. La disponibilidad mensual de la transacción crítica debe ser de al menos ${fmt(q.disponibilidad_pct, 1)} %; la recuperación ante desastres, de cuatro horas como máximo, con pérdida de datos de hasta quince minutos. Planificamos un catálogo inicial de ${fmt(q.casos)} casos de prueba y controlamos el avance en las puertas G0 a G6.`);
    deco(s, "cuarto-circulo", 1, { x: 18.5, y: -3.8, w: 6.0, h: 6.0 });
    RINGS(s, 10.29, 6.25, 11.2, 1);
    ctx.title(s, "Calidad: criterios clave de aceptación");
    const kp = [
      [`≤ ${q.p95_preparacion_s} s`, "p95 de preparación", `Entrega ≤ ${q.p95_entrega_s} s, preventa ≤ ${fmt(q.p95_preventa_s, 1)} s, stock y crédito ≤ ${q.p95_stock_credito_s} s`],
      [`≥ ${fmt(q.disponibilidad_pct, 1)} %`, "Disponibilidad mensual", `Transacción crítica; infraestructura ≥ ${fmt(q.disponibilidad_infra_pct, 2)} %`],
      [`≤ ${q.rto_h} h`, "RTO", "Tiempo máximo de recuperación ante un desastre"],
      [`≤ ${q.rpo_min} min`, "RPO", "Pérdida máxima de datos aceptada"],
      [fmt(q.casos), "casos de prueba", "Catálogo inicial estimado; no son pruebas ya ejecutadas"],
      [q.gates, "puertas de calidad", "G5 habilita Producción en marcha blanca; H7 y H12 son la aceptación contractual"],
    ];
    const cw = (W - 0.6) / 3, chh = 3.55;
    kp.forEach((k, i) => {
      const x = X0 + (i % 3) * (cw + 0.3), y = 1.9 + Math.floor(i / 3) * (chh + 0.3);
      card(s, x, y, cw, chh, { objectName: `!!tarjeta_${i + 1}` });
      T(s, k[0], x + 0.4, y + 0.3, cw - 0.8, 1.2, { fontSize: 54, bold: true, fontFace: H, color: C.accent1, valign: "middle" });
      T(s, k[1], x + 0.4, y + 1.6, cw - 0.8, 0.5, { fontSize: 22, bold: true, fontFace: H });
      T(s, k[2], x + 0.4, y + 2.2, cw - 0.8, 1.2, { fontSize: 16, color: C.accent3 });
    });
    ctx.src(s, "Criterios de aceptación, no resultados ya obtenidos. Fuente: Subdocumento 9 y plan de pruebas T-13.", 9.85);
  }

  // ------------------------------------------------------------ 26-29 Riesgos
  const rbs = doc.rbs;
  const BR_FILL = [C.accent1, C.text1, C.accent4, C.accent2, C.accent3, C.accent5, C.accent6];
  const BR_TXT = [C.background1, C.background1, C.text1, C.background1, C.background1, C.text1, C.text1];
  {
    const s = ctx.add("BLANCO", SEC, ALEX, "9:10",
      `Pasamos a los riesgos. Los clasificamos con ISO 31000 en una estructura de desglose: ${rbs.total} riesgos en siete ramas. La más grande es solución y tecnología, con ${rbs.ramas[0].riesgos}. En total hay ${rbs.zonas.criticos} críticos, ${rbs.zonas.altos} altos, ${rbs.zonas.medios} medios y ${rbs.zonas.bajos} bajo, todos con respuesta, responsable y disparador.`);
    deco(s, "onda-naranjo-claro", 1, { x: -5.44, y: -3.15, w: 12.15, h: 6.07 });
    deco(s, "hoja", 1, { x: 2.9, y: 10.0, w: 3.6, h: 3.6 });
    deco(s, "cuarto-circulo", 2, { x: -0.7, y: 10.0, w: 3.6, h: 3.6 });
    RINGS(s, 14.17, 3.94, 11.2, 1);
    ctx.N(s, "!!title", "RBS: de dónde vienen los riesgos", 1.57, 3.05, 8.8, 2.4, { fontSize: 54, bold: true, fontFace: H, color: C.text1 });
    ctx.N(s, "!!subtitulo", [
      { text: `${rbs.ramas.length} ramas · ${rbs.total} riesgos · ISO 31000`, options: { breakLine: true } },
      { text: `${rbs.zonas.criticos} críticos · ${rbs.zonas.altos} altos · ${rbs.zonas.medios} medios · ${rbs.zonas.bajos} bajo` },
    ], 1.57, 5.7, 8.8, 1.1, { fontSize: 22, color: C.accent3, paraSpaceAfter: 6 });
    rbs.ramas.forEach((r, i) => {
      const y = 0.85 + i * 1.32;
      s.addText(String(r.riesgos), { shape: pres.shapes.OVAL, x: 10.9, y, w: 0.95, h: 0.95, fill: { color: BR_FILL[i] }, line: { color: BR_FILL[i], width: 0 }, color: BR_TXT[i], bold: true, fontSize: 24, fontFace: H, align: "center", valign: "middle", margin: 0, objectName: `!!rama${i + 1}` });
      T(s, [
        { text: `${r.n} · ${r.nombre}`, options: { fontSize: 22, bold: true, fontFace: H, breakLine: true } },
        { text: r.ejemplos, options: { fontSize: 16, color: C.accent3 } },
      ], 12.1, y - 0.05, 6.4, 1.05, { valign: "middle", objectName: `!!ramatxt_${i + 1}` });
    });
  }
  const rbsBase = (s, active) => {
    deco(s, "mosaico", 2, { x: 16.35, y: -1.62, w: 4.5, h: 4.5 });
    RINGS(s, -2.47, 9.69, 11.2, 1);
    ctx.title(s, "RBS: así se clasifican los riesgos");
    s.addText(`Riesgos del proyecto · ${rbs.total}`, { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.12, x: 6.9, y: 1.7, w: 6.2, h: 0.75, fill: { color: C.text1 }, color: C.background1, bold: true, fontSize: 18, fontFace: H, align: "center", valign: "middle", margin: 0, objectName: "!!rbsroot" });
    const gap = 0.12, bw = (W - 6 * gap) / 7, by = 3.2, bh = 1.9;
    s.addShape(pres.shapes.LINE, { x: 10.0, y: 2.45, w: 0, h: 0.4, line: lineOpt("C7C7C7", 1), objectName: "!!rbsline_0" });
    s.addShape(pres.shapes.LINE, { x: X0 + bw / 2, y: 2.85, w: 6 * (bw + gap), h: 0, line: lineOpt("C7C7C7", 1), objectName: "!!rbsline_h" });
    rbs.ramas.forEach((r, i) => {
      const x = X0 + i * (bw + gap), on = active === r.n, dim = active && !on;
      s.addShape(pres.shapes.LINE, { x: x + bw / 2, y: 2.85, w: 0, h: 0.35, line: lineOpt("C7C7C7", 1), objectName: `!!rbsline_${r.n}` });
      s.addText([
        { text: `Rama ${r.n}`, options: { fontSize: 16, bold: true, fontFace: H, color: on ? C.background1 : dim ? C.accent5 : C.accent1, breakLine: true } },
        { text: r.nombre, options: { fontSize: 16, bold: true, fontFace: H, color: on ? C.background1 : dim ? C.accent5 : C.text1 } },
      ], { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.1, x, y: on ? by - 0.1 : by, w: bw, h: on ? bh + 0.3 : bh, fill: { color: on ? C.accent1 : C.background2 }, line: { color: on ? C.accent1 : C.background2, width: 0.5 }, align: "left", valign: "top", margin: [0.12, 0.1, 0, 0.12], objectName: `!!br${r.n}` });
      T(s, `${r.riesgos} riesgos`, x + 0.12, (on ? by - 0.1 : by) + (on ? 1.75 : 1.5), bw - 0.2, 0.35, { fontSize: 16, bold: true, color: on ? C.background1 : dim ? C.accent5 : C.accent3, objectName: `!!brn${r.n}` });
    });
  };
  {
    const s = ctx.add("COMPACTO", SEC, ALEX, "9:20",
      `Esta es la clasificación completa: siete ramas que agrupan los ${rbs.total} riesgos según su origen. Hay una reserva de contingencia de ${fmt(rbs.reserva_hh, 1)} horas-hombre para absorberlos. Revisemos la rama más relevante.`);
    rbsBase(s, null);
    darkCard(s, X0, 5.9, W, 2.6, "!!panel_oscuro");
    T(s, "LECTURA DEL REGISTRO", X0 + 0.5, 6.2, 8, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent4, objectName: "!!panel_t1" });
    T(s, `${rbs.zonas.criticos} críticos · ${rbs.zonas.altos} altos · ${rbs.zonas.medios} medios · ${rbs.zonas.bajos} bajo`, X0 + 0.5, 6.75, W - 1, 0.6, { fontSize: 30, bold: true, fontFace: H, color: C.background1, objectName: "!!panel_t2" });
    T(s, `Todos con respuesta, responsable y disparador. Reserva de contingencia: ${fmt(rbs.reserva_hh, 1)} HH.`, X0 + 0.5, 7.6, W - 1, 0.5, { fontSize: 20, color: C.accent6, objectName: "!!panel_t3" });
  }
  {
    const s = ctx.add("COMPACTO", SEC, GC, "9:35",
      `Solución y tecnología concentra ${rbs.ramas[0].riesgos} riesgos, incluidos los dos críticos del proyecto: el retiro sin trazabilidad completa, R-012, y la recuperación fuera de RTO y RPO, R-015. Para el primero comprometemos un retiro simulado de punta a punta; para el segundo, un ensayo de desastre total antes de la puesta en producción.`);
    rbsBase(s, 1);
    const ZC = { Crítica: [C.accent1, C.background1, C.accent1], Alta: [C.accent4, C.text1, C.accent4], Media: [C.background2, C.text1, "C7C7C7"] };
    const cw = (W - 6 * 0.12) / 7, ch = 1.35;
    doc.rbs.rama1.forEach((r, i) => {
      const x = X0 + (i % 7) * (cw + 0.12), y = 5.75 + Math.floor(i / 7) * (ch + 0.15);
      const z = ZC[r[1]];
      s.addText([
        { text: `${r[0]} · ${r[1]}`, options: { fontSize: 16, bold: true, fontFace: H, breakLine: true } },
        { text: r[2], options: { fontSize: 16 } },
      ], { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.1, x, y, w: cw, h: ch, fill: { color: z[0] }, line: { color: z[2], width: 0.75 }, color: z[1], align: "left", valign: "top", margin: [0.1, 0.1, 0.05, 0.12], objectName: `!!riesgo_${i + 1}` });
    });
    T(s, `RAMA 1 · SOLUCIÓN Y TECNOLOGÍA · ${rbs.ramas[0].riesgos} RIESGOS  ·  ${doc.rbs.rama1.filter((r) => r[1] === "Crítica").length} críticos · ${doc.rbs.rama1.filter((r) => r[1] === "Alta").length} altos · ${doc.rbs.rama1.filter((r) => r[1] === "Media").length} medios`, X0, 5.35, W, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent1, objectName: "!!edtleyenda" });
  }
  {
    const m = doc.matriz_riesgos;
    const s = ctx.add("COMPACTO", SEC, ALEX, "10:00",
      "La matriz cruza probabilidad e impacto; el número de cada celda es la cantidad de riesgos y el color indica la zona de exposición, con cortes en 0,08, 0,20 y 0,40. Los dos riesgos críticos están en probabilidad media e impacto alto. Con esto cerramos la ejecución: un plan con etapas, hitos, calidad verificable y riesgos gestionados.");
    RINGS(s, -5.17, -8.14, 11.2, 1);
    ctx.title(s, "Matriz de exposición");
    const gx = 3.9, cw = 2.8, chh = 1.3, g = 0.1, gy = 1.9;
    m.prob.forEach((p, r) => {
      T(s, p, X0, gy + r * (chh + g), 2.1, chh, { fontSize: 16, bold: true, color: C.accent3, valign: "middle", align: "right", objectName: `!!prob_${r}` });
      m.impacto.forEach((_, c) => {
        const cnt = m.n[r][c];
        const hot = r === 2 && c === 3;
        s.addText(
          cnt ? [
            { text: String(cnt), options: { fontSize: 32, bold: true, fontFace: H, breakLine: true } },
            { text: hot ? "R-012 · R-015" : cnt === 1 ? "riesgo" : "riesgos", options: { fontSize: 16 } },
          ] : "",
          { shape: pres.shapes.RECTANGLE, x: gx + c * (cw + g), y: gy + r * (chh + g), w: cw, h: chh, fill: { color: m.fill[r][c] }, line: { color: m.fill[r][c], width: 0 }, color: hot ? C.background1 : C.text1, align: "center", valign: "middle", margin: 0, objectName: `!!cell${r}${c}` }
        );
      });
    });
    m.impacto.forEach((t, c) => T(s, t, gx + c * (cw + g), gy + 5 * (chh + g), cw, 0.4, { fontSize: 16, bold: true, color: C.accent3, align: "center", objectName: `!!imp_${c}` }));
    T(s, "Filas: probabilidad · Columnas: impacto · Exposición = P × I:  Crítica ≥ 0,40 · Alta ≥ 0,20 · Media ≥ 0,08 · Baja < 0,08", X0, 9.65, W, 0.4, { fontSize: 16, color: C.accent3, objectName: "!!leyenda" });
  }
};
