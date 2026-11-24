// C. Ejecucion (laminas 17-43): metodologia, RUP, Gantt, EDT (base + 10 productos), calidad, RBS (ramas, base, 6 ramas),
// top-10 de riesgos y matriz de exposicion. EDT y RBS salen de data/edt_rbs.json (tools/extract_edt_rbs.py).
module.exports = function ejecucion(ctx) {
  const { kit, D, fmt, pct, OVERRIDES } = ctx;
  const { pres, C, H, B, X0, W, XR, Y0, YB, T, card, darkCard, pill, circle, deco, arc, RINGS, QUARTER, lineOpt, th, td, tblBorder } = kit;
  const SEC = "Ejecución";
  const ALEX = "Alex Aravena", MM = "Maximiliano Miño", GC = "Guillermo Castillo";
  const doc = D.documentos;
  // Reloj de la exposicion: cada lamina avanza una duracion (s) desde el cierre de la lamina 16 (solucion.js) y el bloque
  // debe terminar en 10:00 (la lamina siguiente, Innovaciones, termina en 11:00).
  const clk = (() => {
    let t = 5 * 60 + 14; // 5:14, fin de "Trazabilidad y continuidad"
    const f = (v) => `${Math.floor(v / 60)}:${String(v % 60).padStart(2, "0")}`;
    return { step: (d) => f((t += d)), now: () => f(t) };
  })();
  const hz = D.parametros.horizonte_meses;
  const E = doc.etapas;

  const decorC = (s) => {
    deco(s, "cuarto-circulo", 1, { x: 17.63, y: -3.06, w: 7.02, h: 7.02 });
  };

  // ------------------------------------------------------------ 17 Metodologia
  const msub = (s) => ctx.N(s, "!!msub", "PMBOK + cascada por etapa + DevSecOps", X0, 2.5, 9, 0.5, { fontSize: 22, bold: true, fontFace: H, color: C.accent1 });
  {
    const s = ctx.add("CONTENIDO", SEC, ALEX, clk.step(15),
      `Trabajamos con PMBOK adaptado a ${hz} meses, con valor ganado y alerta si el SPI o el CPI bajan de 0,90. El desarrollo sigue una cascada por etapa contractual, con los doce hitos del Formulario E-25 y los períodos del Artículo 17 fijos. No se realizan despliegues ordinarios en septiembre, en diciembre ni en los tres primeros días hábiles de cada mes; el congelamiento total va del 1 al 25 de septiembre, todo diciembre y esos tres primeros días hábiles. El gobierno tiene un ritmo claro: seguimiento semanal, comité de proyecto quincenal, comité ejecutivo y de arquitectura mensual, y comité de operación desde el mes 13.`);
    decorC(s);
    ctx.title(s, "Metodología");
    msub(s);
    T(s, "CÓMO TRABAJAMOS", X0, 3.2, 6, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, objectName: "!!cab_1" });
    const steps = [
      [`PMBOK adaptado a ${hz} meses`, "valor ganado: alerta si SPI o CPI < 0,90"],
      ["Cascada por etapa contractual", "cuatro fases por etapa, en las fechas del Formulario E-25"],
      ["Hitos y períodos fijos", "los doce hitos del E-25 y los períodos del Art. 17° no se adaptan"],
      ["Congelamiento de despliegues", "1–25 sep, todo dic y 3 primeros días hábiles de cada mes"],
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
    const s = ctx.add("CONTENIDO", SEC, ALEX, clk.step(12),
      "Cada etapa contractual sigue cuatro fases en cascada: requisitos y diseño, construcción por frentes en paralelo, integración y certificación, e implantación, cada una cerrada por hitos del Formulario E-25. Cada cambio recorre además el ciclo DevSecOps, con revisión por pares, análisis estático, pruebas de contrato y medición de cobertura, y se controla en las puertas del plan de calidad: G0 y G1 al solicitar la fusión, G2 en la integración continua y G3 en la promoción a QA.");
    decorC(s);
    ctx.title(s, "Metodología");
    msub(s);
    const fases = doc.fases_cascada;
    T(s, "CUATRO FASES EN CASCADA EN CADA ETAPA CONTRACTUAL", X0, 3.2, 14, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, objectName: "!!cab_1" });
    const colors = [C.text1, C.accent2, C.accent1, C.accent4];
    const fw = (W - 3 * 0.12) / 4;
    fases.forEach((f, i) => {
      s.addText([
        { text: f.nombre, options: { fontSize: 18, bold: true, fontFace: H, breakLine: true } },
        { text: f.detalle, options: { fontSize: 15 } },
      ], { shape: pres.shapes.RECTANGLE, x: X0 + i * (fw + 0.12), y: 3.7, w: fw, h: 1.5, fill: { color: colors[i] }, color: i === 3 ? C.text1 : C.background1, align: "left", valign: "middle", margin: [0, 0.12, 0, 0.15], objectName: `!!rup${i}` });
    });
    T(s, "DEVSECOPS · CICLO DE CADA CAMBIO", X0, 5.5, 12, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, objectName: "!!cab_2" });
    ["Revisión por pares", "Análisis estático", "Pruebas de contrato", "Medición de cobertura"].forEach((t, i) => {
      const px = X0 + i * 3.9;
      pill(s, t, px, 5.95, 3.3, 0.8, { fill: { color: C.accent1 }, color: C.background1, bold: true, fontSize: 18, objectName: `!!ciclo_${i + 1}` });
      if (i < 3) s.addShape(pres.shapes.RIGHT_ARROW, { x: px + 3.38, y: 6.2, w: 0.44, h: 0.3, fill: { color: C.text1 }, objectName: `!!ciclo_flecha_${i + 1}` });
    });
    T(s, "DÓNDE SE APLICA", X0, 7.2, 12, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, objectName: "!!cab_3" });
    const q = doc.calidad;
    const gates = [
      ["G0–G1", "Compromiso y solicitud de fusión", "bloquea si falta la aprobación de un par o hay un secreto"],
      ["G2", "Integración continua", `bloquea si falla un umbral (cobertura ≥ ${q.cobertura_negocio_pct} % en negocio y ${q.cobertura_global_pct} % global)`],
      ["G3", "Promoción a QA", "bloquea imagen con vulnerabilidad crítica o alta"],
    ];
    gates.forEach((g, i) => {
      const gx = X0 + i * 5.7, gw = 5.4;
      card(s, gx, 7.7, gw, 1.9, { objectName: `!!gate_${i + 1}` });
      s.addText(g[0], { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.12, x: gx + 0.25, y: 8.05, w: 1.15, h: 0.9, fill: { color: C.text1 }, color: C.background1, bold: true, fontSize: 18, fontFace: H, align: "center", valign: "middle", margin: 0, objectName: `!!gatenum_${i + 1}` });
      T(s, [
        { text: g[1], options: { fontSize: 18, bold: true, fontFace: H, breakLine: true } },
        { text: g[2], options: { fontSize: 16, color: C.accent3 } },
      ], gx + 1.55, 7.85, gw - 1.7, 1.5, { valign: "middle", objectName: `!!gatetxt_${i + 1}` });
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
    const s = ctx.add("COMPACTO", SEC, ALEX, clk.step(12),
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
    ctx.src(s, "Fuente: Subdocumento 7, Formularios T-14 y T-15 (frentes de trabajo; nombres abreviados).", 10.2);
  }

  // ------------------------------------------------------------ 20-21 Gantt colapsado / desplegado
  const ganttFrame = (s, collapsed) => {
    deco(s, "mosaico", 2, { x: 17.6, y: -2.6, w: 4.5, h: 4.5 });
    RINGS(s, -2.65, 9.6, 11.45, 1);
    ctx.title(s, "Gantt de implementación");
    ctx.N(s, "!!gsub", "Meses 1–24 · actividades, hitos y congelamientos (gris: 1–25 sep y todo dic; además, los 3 primeros días hábiles de cada mes)", X0, 1.4, 16.8, 0.4, { fontSize: 16, color: C.accent3 });
    const gx = 5.9, gw = XR - gx, cw = gw / 24;
    const rowY = (i) => 2.95 + i * 0.62;
    // congelamiento total (SD7, "Carta Gantt y calendario"): del 1 al 25 de septiembre y todo diciembre (meses 8, 11, 20 y 23);
    // ademas se restringen los tres primeros dias habiles de cada mes (se indica en el subtitulo, no se dibuja).
    [[8, "1–25 sep", 25 / 30], [11, "Dic", 1], [20, "1–25 sep", 25 / 30], [23, "Dic", 1]].forEach(([m, l, f], i) => {
      s.addShape(pres.shapes.RECTANGLE, { x: gx + (m - 1) * cw, y: 2.45, w: cw * f, h: 7.45, fill: { color: "E9E9E9" }, line: { color: "E9E9E9", width: 0 }, objectName: `!!congela_${i + 1}` });
      T(s, l, gx + (m - 1) * cw - 0.2, 2.1, cw * f + 0.4, 0.3, { fontSize: 13, bold: true, color: C.accent3, align: "center", objectName: `!!congela_l${i + 1}` });
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
    const s = ctx.add("COMPACTO", SEC, ALEX, clk.step(2), "(Transición automática: el diagrama se despliega en la lámina siguiente.)");
    OVERRIDES[ctx.num()] = { advTm: 100, durMs: 1400 };
    const g = ganttFrame(s, true);
    ctx.N(s, "!!ghitos", "Hitos", X0, g.yH, 4, 0.4, { fontSize: 16, bold: true, fontFace: H, valign: "middle" });
  }
  {
    const s = ctx.add("COMPACTO", SEC, ALEX, clk.step(18),
      `Aquí vemos el cronograma mes a mes. En gris, el congelamiento total: del 1 al 25 de septiembre y todo diciembre; además se restringen los tres primeros días hábiles de cada mes. La Etapa 1 pasa a producción en el mes ${E.h7_mes} (hito H7) y se estabiliza hasta el mes 20; la Etapa 2 corre del mes ${E.etapa2[0]} al ${E.etapa2[1]} y pasa a producción en el mes ${E.h12_mes} (hito H12). La Operación se extiende del mes ${E.operacion[0]} al ${E.operacion[1]}.`);
    const g = ganttFrame(s, false);
    ctx.N(s, "!!ghitos", "Hitos", X0, g.yH, 4, 0.4, { fontSize: 16, bold: true, fontFace: H, valign: "middle" });
    D.hitos.forEach((h) => {
      const cx = g.gx + (h.mes - 0.5) * g.cw;
      const key = h.hito === "H7" || h.hito === "H12";
      s.addShape(pres.shapes.DIAMOND, { x: cx - 0.17, y: g.yH + 0.03, w: 0.34, h: 0.34, fill: { color: key ? C.accent1 : C.text1 }, line: { color: key ? C.accent1 : C.text1, width: 0 }, objectName: `!!hito_${h.hito}` });
      T(s, h.hito, cx - 0.35, g.yH + 0.42, 0.7, 0.3, { fontSize: 13, bold: key, color: key ? C.accent1 : C.accent3, align: "center", objectName: `!!hitol_${h.hito}` });
    });
  }

  // ------------------------------------------------------------ 22-32 EDT (misma estructura que la EDT de la presentacion Informe 2 v4:
  // una lamina base y una por producto; la tarjeta activa sube y se vuelve naranjo, sus puntos de cuenta de control
  // se expanden en tarjetas blancas y el resto se atenua). Datos: SD7 (T-14 y T-15) en data/edt_rbs.json.
  const ER = D.edt_rbs;
  const EP = ER.edt.productos, NP = EP.length, ET = ER.edt.total;
  const EX0 = 0.9, EW = 18.2, EGAP = 0.1, EBW = (EW - (NP - 1) * EGAP) / NP;
  const ex = (i) => EX0 + i * (EBW + EGAP);
  const DIM = C.accent6;
  const mg = (l, r, b, t) => [l * 72, r * 72, b * 72, t * 72]; // margenes en pulgadas -> puntos (pptxgenjs: izq, der, abajo, arriba)
  const NOLINE = { type: "none" };
  const hhTxt = (p) => `${fmt(Math.round(p.hh))} HH`;
  const lc = (t) => t.charAt(0).toLowerCase() + t.slice(1);

  const treeFrame = (s, title) => {
    deco(s, "mosaico", 1, { x: -0.85, y: -1.62, w: 4.5, h: 4.5 });
    deco(s, "mosaico", 2, { x: 16.35, y: -1.62, w: 4.5, h: 4.5 });
    RINGS(s, -2.47, 9.69, 11.2, 1);
    ctx.N(s, "!!title", title, 3.5, 0.75, 13, 0.7, { fontSize: 36, bold: true, fontFace: H, align: "center" });
  };
  const treeRoot = (s, name, text) =>
    s.addText(text, { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.1125, x: 6.9, y: 1.6, w: 6.2, h: 0.75, fill: { color: C.text1 }, line: NOLINE, color: C.background1, bold: true, fontSize: 16, fontFace: H, align: "center", valign: "middle", margin: mg(0.15, 0.15, 0.05, 0.05), objectName: name });
  // conectores del arbol: raiz -> barra horizontal -> una bajada por rama (mas corta en la activa)
  const treeLines = (s, prefix, centers, activeIdx) => {
    const L = (name, x, y, w, h) => s.addShape(pres.shapes.LINE, { x, y, w, h, line: lineOpt("9A9A9A", 1.5), objectName: name });
    L(`!!${prefix}line_0`, 10.0, 2.35, 0, 0.7);
    L(`!!${prefix}line_h`, centers[0], 3.05, centers[centers.length - 1] - centers[0], 0);
    centers.forEach((cx, i) => L(`!!${prefix}line_${i + 1}`, cx, 3.05, 0, i === activeIdx ? 0.25 : 0.35));
  };

  const edtBase = (s, active) => {
    treeFrame(s, "EDT: así se organiza el trabajo");
    treeRoot(s, "!!edtroot", `Proyecto LafroX · ${ET.pt} paquetes de trabajo`);
    treeLines(s, "edt", EP.map((_, i) => ex(i) + EBW / 2), active ? active - 1 : -1);
    EP.forEach((p, i) => {
      const on = active === p.n, dim = active && !on;
      const x = ex(i), y = on ? 3.3 : 3.4, h = on ? 2.05 : 1.7;
      s.addText([
        { text: `Producto ${p.n}`, options: { fontSize: 12, bold: true, fontFace: H, color: on ? C.background1 : dim ? DIM : C.accent1, breakLine: true } },
        { text: p.corto, options: { fontSize: on ? 14 : 13, bold: true, fontFace: H, color: on ? C.background1 : dim ? DIM : C.text1 } },
      ], { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.136, x, y, w: EBW, h, fill: { color: on ? C.accent1 : C.background2 }, line: NOLINE, align: "left", valign: "top", margin: mg(0.09, 0.05, 0, 0.11), objectName: `!!ph${p.n}` });
      const tc = on ? C.background1 : dim ? DIM : null;
      T(s, hhTxt(p), x + 0.09, y + (on ? 1.33 : 0.98), EBW - 0.12, 0.32, { fontSize: on ? 15 : 14, bold: true, fontFace: H, color: tc || C.text1, objectName: `!!phhh${p.n}` });
      T(s, `${p.cc} CC · ${p.pt} PT`, x + 0.09, y + (on ? 1.65 : 1.3), EBW - 0.12, 0.3, { fontSize: 13, color: tc || C.accent3, objectName: `!!phcc${p.n}` });
      if (!on) {
        // un punto por cuenta de control; naranjo = productos de implementacion, negro = servicio de operacion
        const dc = p.n === NP ? C.text1 : C.accent1;
        for (let k = 0; k < p.cc; k++) {
          s.addShape(pres.shapes.OVAL, { x: x + 0.1 + (k % 5) * 0.3, y: 5.3 + Math.floor(k / 5) * 0.3, w: 0.22, h: 0.22, fill: { color: dc }, line: NOLINE, objectName: `!!edt_cc_${p.n}_${k + 1}` });
        }
      }
    });
    ctx.N(s, "!!fuente", "HH: valor esperado de los paquetes de trabajo (sin soporte puente, reservas ni roles mínimos). Fuente: Formularios T-14 y T-15, Subdocumento 7.", EX0, 10.35, 14.5, 0.3, { fontSize: 13, color: C.accent3 });
  };
  // cuentas de control del producto activo: tarjetas blancas sobre la cuadricula (mismos nombres que los puntos)
  const edtCuentas = (s, p) => {
    ctx.N(s, "!!edtleyenda", `PRODUCTO ${p.n} · ${p.nombre.toUpperCase()} · ${p.cc} CUENTAS DE CONTROL`, EX0, 6.75, EW, 0.35, { fontSize: 14, bold: true, fontFace: H, color: C.accent1 });
    const n = p.cuentas.length, per = n <= 5 ? n : n === 6 ? 5 : n <= 8 ? 4 : 6, cw = (EW - (per - 1) * 0.15) / per;
    p.cuentas.forEach((c, k) => {
      const x = EX0 + (k % per) * (cw + 0.15), y = 7.2 + Math.floor(k / per) * 1.12;
      s.addText([
        { text: c.codigo, options: { fontSize: 14, bold: true, fontFace: H, color: C.accent1, breakLine: true } },
        { text: c.corto, options: { fontSize: 16, bold: true, fontFace: H, color: C.text1 } },
      ], { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.1176, x, y, w: cw, h: 0.98, fill: { color: C.background1 }, line: { color: C.accent4, width: 1.25 }, align: "left", valign: "middle", margin: mg(0.2, 0.2, 0, 0), objectName: `!!edt_cc_${p.n}_${k + 1}` });
    });
  };
  const EDT_GUION = {
    1: (p) => `${p.nombre}: ${p.cc} cuentas y ${p.pt} paquetes. Constitución, planificación, riesgos, reversibilidad, gobierno, cierre y cumplimiento.`,
    2: (p) => `${p.nombre}: ${p.cc} cuentas y ${p.pt} paquetes. Requisitos, arquitectura, seguridad, sala técnica, cadena de frío y aprobación de los diseños.`,
    3: (p) => `Plataforma base: ambientes y entrega continua, servicios de nube y servicios comunes; ${p.cc} cuentas y ${p.pt} paquetes.`,
    4: (p) => `Software operativo: bodega, calidad, venta y reparto, canal moderno y analítica; ${p.cc} cuentas y ${p.pt} paquetes.`,
    5: (p) => `Integraciones y datos migrados: ERP, WMS y flota, servicios externos, cadenas por EDI y migración; ${p.pt} paquetes.`,
    6: (p) => `Solución certificada: pruebas de integración, aceptación, carga, recuperación y seguridad, más actas y documentación; ${p.pt} paquetes.`,
    7: (p) => `Innovaciones verificadas: una cuenta por innovación, de INN-01 a INN-05, con su evidencia de punta a punta; ${p.pt} paquetes.`,
    8: (p) => `Infraestructura y servicios: hardware, nube y enlaces, sala técnica de Talca, cableado, racks, seguridad física y sitios; ${p.pt} paquetes.`,
    9: (p) => `Implantación y usuarios: marchas blancas, estabilización, aceptación, capacitación y gestión del cambio; ${p.pt} paquetes.`,
    10: (p) => `Servicio de operación y salida: operación continua, mantenimiento, informes, transferencia y salida; ${fmt(Math.round(p.hh))} HH, el producto de mayor esfuerzo.`,
  };
  {
    const s = ctx.add("BLANCO", SEC, ALEX, clk.step(12),
      `La EDT ordena el trabajo por producto, tal como lo recibe y acepta el cliente: ${NP} productos, ${ET.cc} cuentas de control y ${ET.pt} paquetes de trabajo. Recorramos los ${NP}.`);
    edtBase(s, null);
  }
  EP.forEach((p) => {
    const s = ctx.add("BLANCO", SEC, p.n <= 7 ? ALEX : GC, clk.step(9), EDT_GUION[p.n](p));
    edtBase(s, p.n);
    edtCuentas(s, p);
  });

  // ------------------------------------------------------------ 25 Calidad
  {
    const q = doc.calidad;
    const s = ctx.add("COMPACTO", SEC, MM, clk.step(25),
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
      [q.gates, "puertas de calidad", "G5 habilita la marcha blanca (H6 y H11); H7 y H12 son hitos de aceptación contractual, no puertas técnicas"],
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

  // ------------------------------------------------------------ 34-43 Riesgos (misma estructura que la RBS de la presentacion
  // Informe 2 v4: ramas, base con un punto por riesgo, una lamina por rama, top-10 y matriz). Datos: SD8 (RBS v4 de 36 riesgos,
  // T-16 y anexo 8.H) en data/edt_rbs.json.
  const RB = ER.rbs, RR = RB.ramas, NR = RR.length, RZ = RB.zonas, RV = RB.reservas;
  const BR_FILL = [C.accent1, C.text1, C.accent4, C.accent2, C.accent3, C.accent5];
  const ZONA = {
    Crítica: { fill: C.accent1, line: null, txt: C.background1 },
    Alta: { fill: C.accent4, line: null, txt: C.text1 },
    Media: { fill: C.background2, line: C.accent6, txt: C.text1 },
    Baja: { fill: C.background1, line: C.accent6, txt: C.text1 },
  };
  const zoneLine = (z) => (ZONA[z].line ? { color: ZONA[z].line, width: 1.25 } : NOLINE);
  const zonasTxt = `${RZ.criticos} crítico${RZ.criticos === 1 ? "" : "s"} · ${RZ.altos} altos · ${RZ.medios} medios · ${RZ.bajos} bajo${RZ.bajos === 1 ? "" : "s"}`;
  const RGAP = 0.15, RW = (EW - (NR - 1) * RGAP) / NR;
  const rx = (i) => EX0 + i * (RW + RGAP);
  const rbsLeyenda = (s) =>
    ctx.N(s, "!!rbsleyenda", [
      { text: "■ ", options: { color: C.accent1 } }, { text: "Crítica   ", options: { color: C.accent2 } },
      { text: "■ ", options: { color: C.accent4 } }, { text: "Alta   ", options: { color: C.accent2 } },
      { text: "■ ", options: { color: C.accent6 } }, { text: "Media   ", options: { color: C.accent2 } },
      { text: "□ ", options: { color: C.accent5 } }, { text: "Baja", options: { color: C.accent2 } },
    ], EX0, 10.35, 10, 0.4, { fontSize: 14 });

  // 34: ramas (circulos con el numero de riesgos, barra de zonas y raiz)
  {
    const mayor = RR.reduce((a, r) => (r.riesgos > a.riesgos ? r : a));
    const s = ctx.add("BLANCO", SEC, ALEX, clk.step(10),
      `Clasificamos los riesgos con ISO 31000: ${RB.total} riesgos en ${NR === 6 ? "seis" : NR} ramas. La mayor es ${mayor.nombre}, con ${mayor.riesgos}. Hay ${zonasTxt.replace(/ · /g, ", ")}.`);
    deco(s, "hoja", 1, { x: 2.73, y: 9.22, w: 3.6, h: 3.6 });
    deco(s, "cuarto-circulo", 2, { x: -1.25, y: 9.22, w: 3.6, h: 3.6 });
    RINGS(s, 14.17, 3.94, 11.2, 1);
    deco(s, "onda-naranjo", 1, { x: -5.44, y: -3.15, w: 12.15, h: 6.07 });
    ctx.N(s, "!!title", "RBS: de dónde vienen los riesgos", 1.57, 3.05, 8.5, 2.0, { fontSize: 52, bold: true, fontFace: H, color: C.text1 });
    ctx.N(s, "!!rbssub", `${NR} ramas · ${RB.total} riesgos · ISO 31000`, 1.57, 5.3, 8.3, 0.4, { fontSize: 24, color: C.accent2 });
    // barra de zonas proporcional (8 in): critico, altos, medios, bajos
    let bx = 1.57;
    [[RZ.criticos, C.text1], [RZ.altos, C.accent1], [RZ.medios, C.accent4], [RZ.bajos, C.accent6]].forEach(([n, col], i) => {
      const w = (8.0 * n) / RB.total;
      s.addShape(pres.shapes.RECTANGLE, { x: bx, y: 6.3, w, h: 0.55, fill: { color: col }, line: NOLINE, objectName: `!!rbsbarra_${i + 1}` });
      bx += w;
    });
    ctx.N(s, "!!rbszonas", zonasTxt, 1.57, 7.0, 8.3, 0.3, { fontSize: 18, color: C.accent2 });
    // raiz y filas de ramas (el alto de la raiz se mantiene al cambiar el numero de ramas)
    const rowH = 0.98, pitch = (8.06 - rowH) / (NR - 1);
    s.addText([
      { text: String(RB.total), options: { fontSize: 44, bold: true, fontFace: H, color: C.background1, breakLine: true } },
      { text: "riesgos", options: { fontSize: 17, color: C.accent6 } },
    ], { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.152, x: 10.2, y: 1.0, w: 1.9, h: 8.06, fill: { color: C.text1 }, line: NOLINE, align: "center", valign: "middle", margin: 0, objectName: "!!rbstotal" });
    RR.forEach((r, i) => {
      const y = 1.0 + i * pitch;
      s.addShape(pres.shapes.LINE, { x: 12.1, y: y + 0.49, w: 0.4, h: 0, line: lineOpt("9A9A9A", 1.5), objectName: `!!ramalinea_${r.n}` });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 12.5, y, w: 6.9, h: rowH, rectRadius: 0.098, fill: { color: C.background2 }, line: NOLINE, objectName: `!!ramafila_${r.n}` });
      s.addText(String(r.riesgos), { shape: pres.shapes.OVAL, x: 12.65, y: y + 0.14, w: 0.7, h: 0.7, fill: { color: BR_FILL[i] }, line: NOLINE, color: C.background1, bold: true, fontSize: 18, fontFace: H, align: "center", valign: "middle", margin: 0, objectName: `!!rama${r.n}` });
      T(s, `${r.n} · ${r.nombre}`, 13.55, y + 0.08, 5.8, 0.29, { fontSize: 17, bold: true, fontFace: H, objectName: `!!ramatxt_${r.n}` });
      T(s, r.ejemplos, 13.55, y + 0.52, 5.8, 0.24, { fontSize: 14, color: C.accent3, objectName: `!!rama_ej_${r.n}` });
    });
  }

  // 35-41: base y una lamina por rama
  const rbsBase = (s, active) => {
    treeFrame(s, "RBS: así se clasifican los riesgos");
    treeRoot(s, "!!rbsroot", `Riesgos del proyecto · ${RB.total} · reserva ${fmt(RV.contingencia_hh, 1)} HH`);
    treeLines(s, "rbs", RR.map((_, i) => rx(i) + RW / 2), active ? active - 1 : -1);
    RR.forEach((r, i) => {
      const on = active === r.n, dim = active && !on;
      const x = rx(i), y = on ? 3.3 : 3.4, h = on ? 2.05 : 1.7;
      s.addText([
        { text: `Rama ${r.n}`, options: { fontSize: 13, bold: true, fontFace: H, color: on ? C.background1 : dim ? DIM : C.accent1, breakLine: true } },
        { text: r.nombre, options: { fontSize: on ? 17 : 15, bold: true, fontFace: H, color: on ? C.background1 : dim ? DIM : C.text1 } },
      ], { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.136, x, y, w: RW, h, fill: { color: on ? C.accent1 : C.background2 }, line: NOLINE, align: "left", valign: "top", margin: mg(0.15, 0.15, 0, 0.11), objectName: `!!br${r.n}` });
      T(s, `${r.riesgos} riesgos`, x + 0.15, on ? 4.85 : 4.6, RW - 0.3, 0.35, { fontSize: 13, bold: true, fontFace: H, color: on ? C.background1 : dim ? DIM : C.accent3, objectName: `!!brn${r.n}` });
      if (!active) {
        // un punto por riesgo, coloreado por zona (el punto de cada riesgo se convierte en su tarjeta en la lamina de la rama)
        r.lista.forEach((k, j) => {
          const z = ZONA[k.zona];
          s.addShape(pres.shapes.OVAL, { x: x + 0.15 + (j % 7) * 0.32, y: 5.3 + Math.floor(j / 7) * 0.32, w: 0.24, h: 0.24, fill: { color: z.fill }, line: zoneLine(k.zona), objectName: `!!rsk_${k.id}` });
        });
      }
    });
    rbsLeyenda(s);
  };
  const rbsRama = (s, r) => {
    ctx.N(s, "!!rbscab", `RAMA ${r.n} · ${r.nombre.toUpperCase()} · ${r.riesgos} RIESGOS`, EX0, 5.75, EW, 0.35, { fontSize: 14, bold: true, fontFace: H, color: C.accent1 });
    const n = r.lista.length, per = n <= 8 ? 4 : 5, cw = (EW - (per - 1) * 0.15) / per;
    r.lista.forEach((k, j) => {
      const z = ZONA[k.zona];
      const x = EX0 + (j % per) * (cw + 0.15), y = 6.2 + Math.floor(j / per) * 1.12;
      s.addText([
        { text: k.id, options: { fontSize: 14, bold: true, fontFace: H, color: z.txt } },
        { text: `  · ${k.zona}`, options: { fontSize: 13, color: z.txt, breakLine: true } },
        { text: k.corto, options: { fontSize: 16, bold: true, fontFace: H, color: z.txt } },
      ], { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.1176, x, y, w: cw, h: 0.98, fill: { color: z.fill }, line: zoneLine(k.zona), align: "left", valign: "middle", margin: mg(0.2, 0.2, 0, 0), objectName: `!!rsk_${k.id}` });
    });
  };
  {
    const s = ctx.add("BLANCO", SEC, ALEX, clk.step(10),
      `Esta es la RBS completa: cada punto es un riesgo, coloreado por zona. Para absorberlos hay una contingencia específica de ${fmt(RV.contingencia_hh, 1)} horas-hombre y ${fmt(RV.gestion_hh)} de gestión.`);
    rbsBase(s, null);
    s.addText("Cada punto es un riesgo, coloreado por zona", { x: EX0, y: 6.5, w: EW, h: 0.4, fontSize: 14, color: C.accent3, align: "center", margin: 0, valign: "top", isTextBox: true, objectName: "!!rbsnota" });
    s.addText([
      { text: `${NR} ramas · ${RB.total} riesgos`, options: { fontSize: 24, bold: true, fontFace: H, color: C.text1, breakLine: true } },
      { text: `${zonasTxt} · todos con respuesta, responsable y disparador`, options: { fontSize: 15, color: C.accent3 } },
    ], { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.16, x: 3.6, y: 7.45, w: 12.8, h: 1.6, fill: { color: C.background2 }, line: NOLINE, align: "center", valign: "middle", margin: mg(0.15, 0.15, 0, 0), objectName: "!!rbspanel" });
  }
  const RBS_GUION = (r) => {
    const crit = r.lista.filter((k) => k.zona === "Crítica"), alt = r.lista.filter((k) => k.zona === "Alta");
    const nom = (k) => `${k.id} ${lc(k.corto)}`;
    let t = `${r.nombre}: ${r.riesgos} riesgos.`;
    if (crit.length) t += ` ${crit.length === 1 ? "El único crítico del proyecto" : "Críticos"}: ${crit.map(nom).join(", ")}.`;
    if (alt.length) t += ` ${alt.length === 1 ? "Alto" : "Altos"}${alt.length > 3 ? `, entre ellos` : ""}: ${alt.slice(0, 3).map(nom).join(", ")}.`;
    else if (!crit.length) t += " Todos de zona media o baja.";
    return t;
  };
  RR.forEach((r) => {
    const s = ctx.add("BLANCO", SEC, GC, clk.step(9), RBS_GUION(r));
    rbsBase(s, r.n);
    rbsRama(s, r);
  });

  // 42: diez riesgos de mayor exposicion (tabla; antes en el anexo)
  {
    const crit = ER.top_riesgos.filter((r) => r.zona === "Crítica");
    const s = ctx.add("COMPACTO", SEC, GC, clk.step(13),
      `Los diez riesgos de mayor exposición. ${crit.length === 1 ? "El único crítico es" : "Los críticos son"} ${crit.map((r) => `${r.id}, ${fmt(r.e, 2)}`).join(" y ")}. Todos tienen respuesta, responsable y disparador; la contingencia específica es de ${fmt(RV.contingencia_hh, 1)} HH más ${fmt(RV.gestion_hh)} de gestión.`);
    deco(s, "cuarto-circulo", 1, { x: 18.5, y: -3.8, w: 6.0, h: 6.0 });
    RINGS(s, -2.47, 9.69, 11.2, 1);
    ctx.title(s, "Diez riesgos de mayor exposición");
    const rows = [[th("ID"), th("Riesgo"), th("Rama"), th("Exposición P × I"), th("Zona"), th("Respuesta")]];
    ER.top_riesgos.forEach((r, i) => rows.push([
      td(r.id, i, { bold: true }), td(r.nombre, i), td(`Rama ${r.rama}`, i), td(`${fmt(r.p, 2)} × ${fmt(r.i, 2)} = ${fmt(r.e, 2)}`, i),
      td(r.zona, i, { bold: r.zona === "Crítica", color: r.zona === "Crítica" ? C.accent1 : C.text1 }), td(r.respuesta, i),
    ]));
    s.addTable(rows, { x: X0, y: 1.9, w: W, colW: [1.2, 4.2, 1.4, 3.1, 1.4, 5.5], rowH: 0.64, border: tblBorder(), margin: [0.03, 0.15, 0.03, 0.15], objectName: "Tabla de riesgos" });
    ctx.src(s, `Contingencia específica de ${fmt(RV.contingencia_hh, 1)} HH y reserva de gestión de ${fmt(RV.gestion_hh)} HH. Fuente: Subdocumento 8 (Tabla 8.5 y anexo 8.H) y Formulario T-16.`, 9.95);
  }

  // 43: matriz de exposicion
  {
    const m = ER.matriz, cut = m.cortes;
    const zoneOf = (e) => (e >= cut.critica ? "Crítica" : e >= cut.alta ? "Alta" : e >= cut.media ? "Media" : "Baja");
    const OCUPADA = { Crítica: "E8641B", Alta: "F29A5E", Media: "FBD5BA", Baja: "FDEBDD" }; // celdas con riesgos: color pleno de la zona
    const VACIA = { Crítica: "F7C3A0", Alta: "FADBC6", Media: "FDEEE3", Baja: "FEF7F2" }; // celdas vacias: tono suave de la zona
    const crit = ER.top_riesgos.filter((r) => r.zona === "Crítica");
    const cp = crit[0];
    const s = ctx.add("COMPACTO", SEC, ALEX, clk.step(13),
      `La matriz cruza probabilidad e impacto; el número de cada celda es la cantidad de riesgos y el color, la zona de exposición. ${crit.length === 1 ? "El único crítico" : "Los críticos"}, ${crit.map((r) => r.id).join(" y ")}, ${crit.length === 1 ? "está" : "están"} en probabilidad ${lc(m.prob_nombre[m.prob.indexOf(cp.p)])} e impacto máximo. Cerramos la ejecución: etapas, hitos, calidad verificable y riesgos gestionados.`);
    RINGS(s, -5.17, -8.14, 11.2, 1);
    ctx.title(s, "Matriz de exposición");
    const gx = 3.9, cw = 2.8, chh = 1.3, g = 0.1, gy = 1.9;
    m.prob.forEach((p, r) => {
      T(s, `${m.prob_nombre[r]} / ${fmt(p, 2)}`, X0, gy + r * (chh + g), 2.1, chh, { fontSize: 16, bold: true, color: C.accent3, valign: "middle", align: "right", objectName: `!!prob_${r}` });
      m.impacto.forEach((q, c) => {
        const cnt = m.n[r][c], z = zoneOf(p * q), ids = m.ids[r][c];
        const hot = cnt > 0 && z === "Crítica";
        const fill = cnt ? OCUPADA[z] : VACIA[z];
        s.addText(
          cnt ? [
            { text: String(cnt), options: { fontSize: 32, bold: true, fontFace: H, breakLine: true } },
            { text: cnt <= 2 ? ids.join(" · ") : "riesgos", options: { fontSize: 16 } },
          ] : "",
          { shape: pres.shapes.RECTANGLE, x: gx + c * (cw + g), y: gy + r * (chh + g), w: cw, h: chh, fill: { color: fill }, line: { color: fill, width: 0 }, color: hot ? C.background1 : C.text1, align: "center", valign: "middle", margin: 0, objectName: `!!cell${r}${c}` }
        );
      });
    });
    m.impacto.forEach((q, c) => T(s, `Nivel ${c + 1} / ${fmt(q, 2)}`, gx + c * (cw + g), gy + 5 * (chh + g), cw, 0.4, { fontSize: 16, bold: true, color: C.accent3, align: "center", objectName: `!!imp_${c}` }));
    T(s, `Filas: probabilidad · Columnas: impacto · Exposición = P × I:  Crítica ≥ ${fmt(cut.critica, 2)} · Alta ≥ ${fmt(cut.alta, 2)} · Media ≥ ${fmt(cut.media, 2)} · Baja < ${fmt(cut.media, 2)}`, X0, 9.65, W, 0.4, { fontSize: 16, color: C.accent3, objectName: "!!leyenda" });
  }
  if (clk.now() !== "10:00") throw new Error(`El reloj de ejecución termina en ${clk.now()}, no en 10:00`);
};
