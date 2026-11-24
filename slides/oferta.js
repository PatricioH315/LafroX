// D. Innovacion (30) y E. Oferta economica (31-38).
module.exports = function oferta(ctx) {
  const { kit, D, fmt, pct, uf } = ctx;
  const { pres, C, H, B, X0, W, XR, Y0, YB, T, card, darkCard, pill, circle, deco, arc, RINGS, QUARTER, chartBase, th, td, tblBorder } = kit;
  const PH = "Patricio Henríquez", LC = "Leandro Chamorro";
  const doc = D.documentos, P = D.parametros, ind = D.indicadores, fin = D.financiamiento;
  const T_ = D.tarifa, K_ = D.costo, M_ = D.margen;
  const OP = D.operacion, CS = D.curva_s, SN = D.sensibilidad, INN = D.innovaciones;
  const hh = (m) => D.hitos.find((h) => h.hito === m);
  const decorE = (s) => {
    deco(s, "cuarto-circulo", 1, { x: 18.5, y: -3.8, w: 6.0, h: 6.0 });
    RINGS(s, -2.47, 9.69, 11.2, 1);
  };

  // ------------------------------------------------------------ 30 Innovaciones (iconos !!inn_n)
  {
    const s = ctx.add("COMPACTO", "Innovación", PH, "11:00",
      `Además del alcance base, proponemos cinco innovaciones con una meta, un indicador y un momento de evaluación definidos: seguimiento posentrega de vencimientos, reproducción de incidentes de terreno, vida útil estimada por historia térmica, un pago ligado al costo de servir y una hoja de negocio para el almacenero. Las metas se mantienen en la oferta, pero los beneficios están sujetos a medición: no los presentamos como ahorros ya demostrados.`);
    deco(s, "aros", 1, { x: 16.0, y: -3.6, w: 8.2, h: 6.56 });
    RINGS(s, -2.47, 9.69, 11.2, 1);
    ctx.title(s, "Cinco innovaciones con evaluación");
    const cw = (W - 4 * 0.25) / 5, chh = 6.9;
    doc.innovaciones_info.forEach((it, i) => {
      const x = X0 + i * (cw + 0.25), y = 1.95;
      card(s, x, y, cw, chh, { objectName: `!!tarjeta_${i + 1}` });
      s.addText(String(i + 1).padStart(2, "0"), { shape: pres.shapes.OVAL, x: x + 0.3, y: y + 0.3, w: 0.95, h: 0.95, fill: { color: C.accent1 }, line: { color: C.accent1, width: 0 }, color: C.background1, bold: true, fontSize: 22, fontFace: H, align: "center", valign: "middle", margin: 0, objectName: `!!inn_${i + 1}` });
      T(s, it.tipo.toUpperCase(), x + 0.3, y + 1.5, cw - 0.5, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent1 });
      T(s, it.nombre, x + 0.3, y + 2.0, cw - 0.5, 1.5, { fontSize: 22, bold: true, fontFace: H });
      T(s, it.meta, x + 0.3, y + 3.6, cw - 0.5, 2.2, { fontSize: 16, color: C.accent3 });
      T(s, [{ text: "Evaluación", options: { fontSize: 16, color: C.accent3, breakLine: true } }, { text: it.evaluacion, options: { fontSize: 18, bold: true, fontFace: H } }], x + 0.3, y + chh - 1.1, cw - 0.5, 0.9, {});
    });
    ctx.src(s, "Metas y condiciones en la oferta. Beneficios sujetos a medición; no son ahorros ya demostrados.", 9.95);
  }

  // ------------------------------------------------------------ 31 Seccion
  {
    const s = ctx.add("SECCION", "Oferta económica", LC, "11:05",
      "Pasamos a nuestra oferta económica. Les mostraremos el precio, de qué está compuesto, cómo se paga, cómo se financia el proyecto y qué tan robusta es la rentabilidad frente a cambios en los supuestos.");
    RINGS(s, 9.5, -3.2, 13, 1);
    arc(s, "onda-naranjo-claro", 1, -11.4, 5.1);
    deco(s, "onda-naranjo-claro", 2, { x: 17.24, y: -0.67, w: 12.67 });
    s.addText("05", { placeholder: "numero" });
    s.addText("Nuestra oferta", { placeholder: "title" });
    s.addText("Oferta económica · Licitación TFEP-01/2026", { placeholder: "subtitulo" });
  }

  // ------------------------------------------------------------ 32 Precio total (hero)
  const precioTxt = `${fmt(T_.total.uf)} UF`;
  {
    const s = ctx.add("HERO", "Oferta económica", LC, "11:35",
      `El precio total de nuestra oferta es de ${precioTxt}, sin IVA. A la UF de ${fmt(P.uf_clp)} pesos, equivale a ${fmt(T_.total.clp)} pesos o ${fmt(T_.total.usd)} dólares, al tipo de cambio de ${P.usd_clp} pesos. De ese monto, ${fmt(T_.implementacion.uf)} UF corresponden a la implementación y ${fmt(T_.soporte.uf)} UF al soporte durante los ${OP.meses} meses de operación.`);
    deco(s, "onda-naranjo", 1, { x: -9.91, y: 2.5, w: 12.67, h: 6.33 });
    deco(s, "onda-naranjo-claro", 1, { x: -9.87, y: 5.1, w: 12.67, h: 6.33, rotate: 180, flipH: true });
    deco(s, "onda-naranjo", 2, { x: 17.27, y: 1.93, w: 12.67, h: 6.33, rotate: 180, flipH: true });
    deco(s, "onda-naranjo-claro", 2, { x: 17.24, y: -0.67, w: 12.67, h: 6.33 });
    ctx.brand(s, true, 9.64, 0.25, { k: 1.2, dx: -2.2, dy: 0.72, w: 4.42, align: "center" });
    ctx.N(s, "!!kicker", "PRECIO TOTAL DE LA OFERTA · SIN IVA", 2.0, 1.95, 16, 0.5, { fontSize: 22, bold: true, color: C.accent4, align: "center", fontFace: H });
    ctx.N(s, "!!precio", precioTxt, 2.0, 2.6, 16, 3.0, { fontSize: 150, bold: true, fontFace: H, color: C.background1, align: "center", valign: "middle" });
    ctx.N(s, "!!equivale", `CLP ${fmt(T_.total.clp)}  ·  USD ${fmt(T_.total.usd)}`, 2.0, 5.65, 16, 0.7, { fontSize: 34, color: C.accent6, align: "center" });
    [["Implementación", T_.implementacion.uf], ["Soporte y operación", T_.soporte.uf]].forEach((it, i) => {
      const x = 3.5 + i * 6.7;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 7.1, w: 6.3, h: 2.3, rectRadius: 0.15, fill: { color: C.accent2 }, line: { color: C.accent2, width: 0 }, objectName: `!!tarjeta_${i + 1}` });
      T(s, [
        { text: it[0], options: { fontSize: 20, color: C.accent6, breakLine: true } },
        { text: `${fmt(it[1])} UF`, options: { fontSize: 44, bold: true, fontFace: H, color: C.accent1 } },
      ], x + 0.5, 7.1, 5.3, 2.3, { valign: "middle", objectName: `!!tarjetatxt_${i + 1}` });
    });
  }

  // ------------------------------------------------------------ 33 Precio -> estructura de costo
  {
    const s = ctx.add("COMPACTO", "Oferta económica", LC, "12:05",
      `El precio se descompone en un costo de ${fmt(K_.total.uf)} UF y un margen de ${fmt(M_.total.uf)} UF. Ese margen equivale a una rentabilidad nominal de ${pct(D.rentabilidad_nominal, 2)}, por debajo del tope de ${pct(P.rentabilidad_maxima, 0)} que fijan las bases. Más de dos tercios del costo son recursos humanos; el resto corresponde a servicios, adquisiciones de implementación y capacitaciones.`);
    decorE(s);
    ctx.title(s, "Del precio a la estructura de costo");
    darkCard(s, X0, 1.95, 6.3, 2.2, "!!precio_card");
    T(s, "Precio total (sin IVA)", X0 + 0.4, 2.15, 5.5, 0.4, { fontSize: 18, color: C.accent6, objectName: "!!precio_l" });
    ctx.N(s, "!!precio", precioTxt, X0 + 0.4, 2.65, 5.5, 1.2, { fontSize: 50, bold: true, fontFace: H, color: C.background1, valign: "middle" });
    card(s, X0, 4.4, 6.3, 2.2, { objectName: "!!tarjeta_2" });
    T(s, [
      { text: "Costo total", options: { fontSize: 18, color: C.accent3, breakLine: true } },
      { text: `${fmt(K_.total.uf)} UF`, options: { fontSize: 44, bold: true, fontFace: H } },
    ], X0 + 0.4, 4.4, 5.5, 2.2, { valign: "middle", objectName: "!!costo_t" });
    card(s, X0, 6.85, 6.3, 2.75, { objectName: "!!tarjeta_3" });
    T(s, [
      { text: "Margen", options: { fontSize: 18, color: C.accent3, breakLine: true } },
      { text: `${fmt(M_.total.uf)} UF`, options: { fontSize: 44, bold: true, fontFace: H, color: C.accent1, breakLine: true } },
      { text: `${pct(D.rentabilidad_nominal, 2)} ≤ ${pct(P.rentabilidad_maxima, 0)} (tope de las bases)`, options: { fontSize: 18 } },
    ], X0 + 0.4, 6.85, 5.6, 2.75, { valign: "middle", objectName: "!!margen_t" });
    T(s, "Estructura del costo, UF (sin IVA)", 8.4, 1.95, 10, 0.4, { fontSize: 18, bold: true, fontFace: H, color: C.accent3 });
    const cats = [...D.estructura_costo].reverse();
    const short = { "RR.HH. implementacion": "RR.HH. implementación", "Adquisiciones implementacion": "Adquisiciones implementación", "Servicios implementacion": "Servicios implementación" };
    s.addChart(pres.charts.BAR, [{ name: "Costo (UF)", labels: cats.map((c) => short[c.categoria] || c.categoria), values: cats.map((c) => Math.round(c.costo_uf)) }], {
      ...chartBase(), x: 8.4, y: 2.4, w: XR - 8.4, h: 7.2, barDir: "bar", barGapWidthPct: 45,
      chartColors: cats.map((_, i) => (i === cats.length - 1 ? "E8641B" : "C7C7C7")),
      dataLabelPosition: "outEnd", dataLabelFormatCode: "#,##0", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 100000,
    });
    ctx.src(s, "Fuente: modelo financiero SD7, hoja RESUMEN. Precios y costos sin IVA.", 9.85);
  }

  // ------------------------------------------------------------ 34 Forma de pago
  {
    const s = ctx.add("COMPACTO", "Oferta económica", LC, "12:35",
      `La forma de pago se estructura en doce hitos de implementación, ligados a entregables verificables, y una cuota mensual de operación de ${fmt(OP.cuota_uf_mes, 2)} UF entre los meses ${OP.mes_desde} y ${OP.mes_hasta}. Los hitos H7, en el mes ${hh("H7").mes}, y H12, en el mes ${hh("H12").mes}, corresponden a la puesta en producción de las etapas 1 y 2. Los montos no incluyen IVA.`);
    decorE(s);
    ctx.title(s, "Forma de pago: doce hitos y una cuota mensual");
    const lw = 1.6, cwid = 0.84, tx = X0, cx = tx + lw;
    s.addChart(pres.charts.BAR, [{ name: "Pago (UF)", labels: D.hitos.map((h) => h.hito), values: D.hitos.map((h) => Math.round(h.uf)) }], {
      ...chartBase(), x: cx - 0.05, y: 1.85, w: 12 * cwid + 0.1, h: 5.9, barDir: "col", barGapWidthPct: 35,
      chartColors: D.hitos.map((h) => (h.hito === "H7" || h.hito === "H12" ? "E8641B" : "C7C7C7")),
      dataLabelPosition: "outEnd", dataLabelFormatCode: "#,##0", valAxisHidden: true, catAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 14000,
    });
    const hdr = [{ text: "Hito", options: { bold: true, fontSize: 16, color: C.accent3, align: "left" } }].concat(D.hitos.map((h) => ({ text: h.hito, options: { bold: true, fontSize: 16, align: "center", color: h.hito === "H7" || h.hito === "H12" ? C.accent1 : C.text1 } })));
    const r2 = [{ text: "Mes", options: { fontSize: 16, color: C.accent3 } }].concat(D.hitos.map((h) => ({ text: String(h.mes), options: { fontSize: 16, align: "center" } })));
    const r3 = [{ text: "% del pago", options: { fontSize: 16, color: C.accent3 } }].concat(D.hitos.map((h) => ({ text: fmt(h.pct * 100), options: { fontSize: 16, align: "center" } })));
    s.addTable([hdr, r2, r3], { x: tx, y: 7.85, w: lw + 12 * cwid, colW: [lw, ...Array(12).fill(cwid)], rowH: 0.55, margin: [0, 0.03, 0, 0.05], valign: "middle", border: { type: "solid", pt: 0.5, color: "C7C7C7" }, fill: { color: "FFFFFF" }, objectName: "Tabla de hitos" });
    const rx = 13.5, rw = XR - rx;
    darkCard(s, rx, 1.95, rw, 4.2, "!!panel_oscuro");
    T(s, "CUOTA DE OPERACIÓN", rx + 0.35, 2.25, rw - 0.7, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent4 });
    T(s, `${fmt(OP.cuota_uf_mes, 2)} UF`, rx + 0.35, 2.75, rw - 0.7, 0.9, { fontSize: 38, bold: true, fontFace: H, color: C.accent1, valign: "middle" });
    T(s, `por mes, de M${OP.mes_desde} a M${OP.mes_hasta} (${OP.meses} cuotas)`, rx + 0.35, 3.75, rw - 0.7, 0.8, { fontSize: 18, color: C.background1 });
    T(s, `Total soporte: ${fmt(T_.soporte.uf)} UF`, rx + 0.35, 4.9, rw - 0.7, 0.8, { fontSize: 18, color: C.accent6 });
    card(s, rx, 6.4, rw, 3.2, { objectName: "!!tarjeta_2" });
    T(s, [
      { text: "12 hitos", options: { fontSize: 30, bold: true, fontFace: H, breakLine: true } },
      { text: `${fmt(T_.implementacion.uf)} UF: el 100 % de la tarifa de implementación`, options: { fontSize: 18, color: C.accent3 } },
    ], rx + 0.35, 6.4, rw - 0.7, 3.2, { valign: "middle" });
    ctx.src(s, "Montos en UF, sin IVA. Naranjo: H7 (Etapa 1 a producción) y H12 (Etapa 2 a producción). Fuente: modelo financiero SD7.", 9.85);
  }

  // ------------------------------------------------------------ 35 Innovaciones en el flujo
  {
    const s = ctx.add("COMPACTO", "Oferta económica", LC, "13:00",
      `Las innovaciones están incorporadas en nuestro flujo. LafroX invierte ${fmt(INN.inversion_total_uf)} UF y asume ${fmt(INN.costo_operacion_total_uf)} UF de costo de operación. El beneficio estimado para Puelche es de ${fmt(INN.beneficio_cliente_total_uf)} UF; lo presentamos como una estimación y no forma parte del flujo de LafroX. Solo el tramo variable de la innovación cuatro, de hasta ${fmt(INN.tabla[3].ingreso_lafrox_uf)} UF, representaría un ingreso para nosotros, y está condicionado al cumplimiento del servicio.`);
    decorE(s);
    ctx.title(s, "Innovaciones: inversión y beneficio");
    const cols = [[9.0, 2.5, "Inversión (UF)"], [11.7, 2.6, "Costo de operación (UF)"], [14.5, 3.9, "Beneficio estimado para Puelche (UF)*"]];
    T(s, "Innovación", X0 + 1.4, 1.85, 5, 0.4, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, valign: "middle" });
    cols.forEach((c) => T(s, c[2], c[0], 1.7, c[1], 0.7, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, align: "right", valign: "middle" }));
    INN.tabla.forEach((it, i) => {
      const y = 2.55 + i * 1.1, info = doc.innovaciones_info[i];
      card(s, X0, y, W, 0.95, { objectName: `!!fila_${i + 1}` });
      s.addText(String(i + 1).padStart(2, "0"), { shape: pres.shapes.OVAL, x: X0 + 0.25, y: y + 0.1, w: 0.75, h: 0.75, fill: { color: C.accent1 }, line: { color: C.accent1, width: 0 }, color: C.background1, bold: true, fontSize: 18, fontFace: H, align: "center", valign: "middle", margin: 0, objectName: `!!inn_${i + 1}` });
      T(s, [{ text: `${info.id} · ${info.nombre}`, options: { fontSize: 20, bold: true, fontFace: H } }], X0 + 1.4, y, 7.4, 0.95, { valign: "middle" });
      const vals = [it.inversion_uf, it.costo_operacion_uf, it.beneficio_cliente_uf];
      cols.forEach((c, k) => T(s, fmt(vals[k]), c[0], y, c[1] - 0.15, 0.95, { fontSize: 22, bold: k === 2, fontFace: k === 2 ? H : B, align: "right", valign: "middle" }));
    });
    const yt = 2.55 + 5 * 1.1;
    darkCard(s, X0, yt, W, 1.0, "!!panel_oscuro");
    T(s, "Total", X0 + 1.4, yt, 5, 1.0, { fontSize: 22, bold: true, fontFace: H, color: C.background1, valign: "middle" });
    [INN.inversion_total_uf, INN.costo_operacion_total_uf, INN.beneficio_cliente_total_uf].forEach((v, k) =>
      T(s, fmt(v), cols[k][0], yt, cols[k][1] - 0.15, 1.0, { fontSize: 24, bold: true, fontFace: H, color: k === 2 ? C.accent4 : C.accent1, align: "right", valign: "middle" })
    );
    T(s, `* Beneficio estimado para Puelche (no forma parte del flujo de LafroX). Ingreso variable de INN-04: hasta ${fmt(INN.tabla[3].ingreso_lafrox_uf)} UF, en el escenario con pago.`, X0, 9.15, W, 0.8, { fontSize: 16, color: C.accent3, objectName: "!!nota" });
  }

  // ------------------------------------------------------------ 36 Curva S
  {
    const s = ctx.add("COMPACTO", "Oferta económica", LC, "13:25",
      `Esta es la curva S del proyecto: el ingreso comercial acumulado frente al egreso acumulado, en UF, entre el mes cero y el mes ${P.horizonte_meses}. El ingreso excluye el capital inicial de ${fmt(P.capital_inicial_uf)} UF. El egreso incluye costos, intereses y amortización del crédito. El ingreso supera al egreso desde el mes ${CS.payback_mes}. Marcamos los hitos H7 y H12, en los meses ${hh("H7").mes} y ${hh("H12").mes}.`);
    decorE(s);
    ctx.title(s, "Curva S: ingresos y egresos acumulados");
    const labels = CS.meses.map((m) => String(m));
    const top = 280000;
    const bars = CS.meses.map((m) => (m === hh("H7").mes || m === hh("H12").mes ? top : null));
    s.addChart([
      { type: pres.charts.BAR, data: [{ name: "Hitos H7 y H12", labels, values: bars }], options: { barDir: "col", barGapWidthPct: 500, chartColors: ["F29A5E"] } },
      { type: pres.charts.LINE, data: [{ name: "Ingreso comercial acumulado", labels, values: CS.ingreso_comercial_acum }, { name: "Egreso acumulado", labels, values: CS.egreso_acum }], options: { chartColors: ["E8641B", "3C3C3C"], lineSize: 3, lineDataSymbol: "none" } },
    ], {
      ...chartBase(), x: X0, y: 1.8, w: 11.6, h: 7.9, showLegend: true, legendPos: "b", showValue: false, valAxisMinVal: 0, valAxisMaxVal: top, valAxisMajorUnit: 40000,
      valAxisLabelFormatCode: "#,##0", catAxisLabelFrequency: 4, catAxisLabelPos: "low",
    });
    const rx = 13.5, rw = XR - rx;
    darkCard(s, rx, 1.95, rw, 7.6, "!!panel_oscuro");
    T(s, "LECTURA", rx + 0.4, 2.3, rw - 0.8, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent4 });
    T(s, `Mes ${CS.payback_mes}`, rx + 0.4, 2.85, rw - 0.8, 1.1, { fontSize: 60, bold: true, fontFace: H, color: C.accent1 });
    T(s, "el ingreso comercial acumulado supera al egreso acumulado", rx + 0.4, 4.05, rw - 0.8, 1.5, { fontSize: 20, color: C.background1 });
    T(s, [
      { text: `H7 · mes ${hh("H7").mes}`, options: { fontSize: 20, bold: true, fontFace: H, color: C.accent4, breakLine: true } },
      { text: "Etapa 1 a producción", options: { fontSize: 16, color: C.accent6, breakLine: true } },
      { text: " ", options: { fontSize: 12, breakLine: true } },
      { text: `H12 · mes ${hh("H12").mes}`, options: { fontSize: 20, bold: true, fontFace: H, color: C.accent4, breakLine: true } },
      { text: "Etapa 2 a producción", options: { fontSize: 16, color: C.accent6 } },
    ], rx + 0.4, 5.9, rw - 0.8, 3.0, {});
    ctx.src(s, `UF acumuladas por mes. Ingreso = hitos y cuotas de operación, sin el capital inicial de ${fmt(P.capital_inicial_uf)} UF. Fuente: modelo financiero SD7, hoja CURVA S.`, 9.85);
  }

  // ------------------------------------------------------------ 37 Rentabilidad (KPIs)
  {
    const s = ctx.add("COMPACTO", "Oferta económica", LC, "13:50",
      `El proyecto es rentable. El valor actual neto, antes de impuestos, es de ${fmt(ind.van_sin_impuestos_uf)} UF, y de ${fmt(ind.van_sobre_impuestos_uf)} UF después de impuestos, con una tasa de descuento de ${fmt(P.tasa_descuento_mensual * 100, 3)} % mensual. La tasa interna de retorno es de ${fmt(ind.tir_sin_imp_mensual * 100, 2)} % mensual, equivalente a ${fmt(ind.tir_sin_imp_anual * 100, 1)} % anual, sin impuestos. La inversión se recupera en el mes ${CS.payback_mes} y la caja mínima es de ${fmt(CS.caja_minima_uf)} UF en el mes ${CS.caja_minima_mes}, con un capital inicial de ${fmt(P.capital_inicial_uf)} UF.`);
    decorE(s);
    ctx.title(s, "Rentabilidad del proyecto");
    const kp = [
      ["VAN", `${fmt(ind.van_sin_impuestos_uf)} UF`, "Valor actual neto, sin impuestos", `Tasa de descuento ${fmt(P.tasa_descuento_mensual * 100, 3)} % mensual (${fmt(fin.tasa_descuento_anual * 100, 2)} % anual). Sobre impuestos: ${fmt(ind.van_sobre_impuestos_uf)} UF`],
      ["TIR", `${fmt(ind.tir_sin_imp_mensual * 100, 2)} %`, "mensual, sin impuestos", `(${fmt(ind.tir_sin_imp_anual * 100, 1)} % anual equivalente). Después de impuestos: ${fmt(ind.tir_post_imp_mensual * 100, 2)} % mensual`],
      ["Recuperación", `Mes ${CS.payback_mes}`, "de la inversión", "El ingreso comercial acumulado supera al egreso acumulado"],
      ["Caja mínima", `${fmt(CS.caja_minima_uf)} UF`, `en el mes ${CS.caja_minima_mes}`, `Con el financiamiento inicial de ${fmt(P.capital_inicial_uf)} UF`],
    ];
    const cw = (W - 3 * 0.3) / 4, chh = 4.7;
    kp.forEach((k, i) => {
      const x = X0 + i * (cw + 0.3);
      card(s, x, 1.9, cw, chh, { objectName: `!!kpi_${i + 1}`, ...(i === 0 ? { fill: { color: C.text1 }, line: { color: C.text1, width: 1 } } : {}) });
      T(s, k[0].toUpperCase(), x + 0.35, 2.15, cw - 0.7, 0.35, { fontSize: 16, bold: true, fontFace: H, color: i === 0 ? C.accent4 : C.accent3 });
      T(s, k[1], x + 0.35, 2.65, cw - 0.7, 1.0, { fontSize: i === 0 ? 40 : 38, bold: true, fontFace: H, color: C.accent1, valign: "middle" });
      T(s, k[2], x + 0.35, 3.75, cw - 0.7, 0.8, { fontSize: 18, bold: true, fontFace: H, color: i === 0 ? C.background1 : C.text1 });
      T(s, k[3], x + 0.35, 4.6, cw - 0.7, 1.9, { fontSize: 16, color: i === 0 ? C.accent6 : C.accent3 });
    });
    T(s, "FINANCIAMIENTO INICIAL", X0, 6.95, 8, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent1 });
    const bw = W * fin.pct_bancario;
    s.addShape(pres.shapes.RECTANGLE, { x: X0, y: 7.4, w: bw - 0.04, h: 0.55, fill: { color: C.accent1 }, line: { color: C.accent1, width: 0 }, objectName: "!!fin_banco" });
    s.addShape(pres.shapes.RECTANGLE, { x: X0 + bw, y: 7.4, w: W - bw, h: 0.55, fill: { color: C.accent4 }, line: { color: C.accent4, width: 0 }, objectName: "!!fin_socios" });
    T(s, [
      { text: `Crédito bancario: ${fmt(fin.credito_uf)} UF (${fmt(fin.pct_bancario * 100)} %)`, options: { fontSize: 20, bold: true, fontFace: H, breakLine: true } },
      { text: `${fmt(fin.tasa_credito_mensual * 100, 1)} % mensual · ${fin.cuotas} cuotas desde el mes ${P.mes_amortizacion_credito}`, options: { fontSize: 16, color: C.accent3 } },
    ], X0, 8.1, bw - 0.3, 1.2, {});
    T(s, [
      { text: `Socios: ${fmt(fin.aporte_socios_uf)} UF (${fmt(fin.pct_propio * 100)} %)`, options: { fontSize: 20, bold: true, fontFace: H, breakLine: true } },
      { text: `costo de capital ${fmt(fin.costo_capital_propio_anual * 100)} % anual`, options: { fontSize: 16, color: C.accent3 } },
    ], X0 + bw, 8.1, W - bw, 1.2, {});
    ctx.src(s, "Fuente: modelo financiero SD7, hojas INDICADORES, CURVA S y FINANCIAMIENTO. VAN y TIR sobre el flujo del proyecto sin financiamiento.", 9.85);
  }

  // ------------------------------------------------------------ 38 Sensibilidad (tornado)
  {
    const s = ctx.add("COMPACTO", "Oferta económica", LC, "14:15",
      `La rentabilidad es robusta. Variamos cada supuesto un veinte por ciento, uno a la vez. El VAN es más sensible a los ingresos: se anula si los ingresos caen a ${fmt(SN.ingreso_minimo_pct * 100, 1)} % de lo proyectado. Por el lado de los costos, el costo de recursos humanos podría subir hasta ${fmt(SN.aumento_max_costo_hh * 100, 2)} % antes de que el VAN llegue a cero. La tasa de descuento tiene un efecto mucho menor.`);
    decorE(s);
    ctx.title(s, "Sensibilidad del VAN");
    const base = SN.van_base_uf;
    const order = [...SN.tabla]; // ya viene ordenada por magnitud: ingresos, HH, otros egresos, tasa
    const rev = [...order].reverse();
    const labels = rev.map((v) => v.variable);
    T(s, "Cambio del VAN respecto del caso base (UF), variable por variable", X0, 1.85, 9.5, 0.4, { fontSize: 18, bold: true, fontFace: H, color: C.accent3 });
    s.addChart(pres.charts.BAR, [
      { name: "Variable −20 %", labels, values: rev.map((v) => Math.round(v.van[0] - base)) },
      { name: "Variable +20 %", labels, values: rev.map((v) => Math.round(v.van[4] - base)) },
    ], {
      ...chartBase(), x: X0, y: 2.3, w: 9.9, h: 5.6, barDir: "bar", barGrouping: "stacked", barGapWidthPct: 45, chartColors: ["9A9A9A", "E8641B"],
      showValue: false, showLegend: true, legendPos: "b", valAxisLabelFormatCode: "#,##0", catAxisLabelPos: "low", valAxisMinVal: -40000, valAxisMaxVal: 40000, valAxisMajorUnit: 20000,
    });
    const rows = [[th("VAN (UF)"), th("−20 %", "right"), th("+20 %", "right")]];
    order.forEach((v, i) => rows.push([td(v.variable, i), td(fmt(v.van[0]), i, { align: "right" }), td(fmt(v.van[4]), i, { align: "right" })]));
    rows.push([td(`Caso base: ${fmt(base)}`, 4, { bold: true }), td("", 4), td("", 4)]);
    s.addTable(rows, { x: 11.8, y: 2.3, w: XR - 11.8, colW: [3.0, 1.8, 1.8], rowH: 0.78, border: tblBorder(), margin: [0.05, 0.12, 0.05, 0.12], objectName: "Tabla de sensibilidad" });
    darkCard(s, X0, 8.15, W, 1.65, "!!panel_oscuro");
    T(s, "VAN = 0", X0 + 0.5, 8.15, 2.6, 1.65, { fontSize: 32, bold: true, fontFace: H, color: C.accent1, valign: "middle" });
    T(s, [
      { text: `si los ingresos caen a ${fmt(SN.ingreso_minimo_pct * 100, 1)} % de lo proyectado`, options: { fontSize: 22, bold: true, fontFace: H, color: C.background1, breakLine: true } },
      { text: `o si el costo de RR.HH. sube hasta +${fmt(SN.aumento_max_costo_hh * 100, 2)} % (cada caso por separado)`, options: { fontSize: 18, color: C.accent6 } },
    ], X0 + 3.3, 8.15, W - 3.8, 1.65, { valign: "middle" });
    ctx.src(s, "Fuente: modelo financiero SD7, hoja SENSIBILIDAD. Variaciones de −20 % y +20 % sobre el flujo base; las demás variables se mantienen constantes.", 9.95);
  }
};
