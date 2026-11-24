// F. Cierre (53-55) y Anexo (A0-A4).
module.exports = function cierre(ctx) {
  const { kit, D, fmt, pct, uf, OVERRIDES } = ctx;
  const { pres, C, H, B, X0, W, XR, Y0, YB, T, card, darkCard, deco, arc, RINGS, DECOR_RATIO, chartBase, th, td, tblBorder } = kit;
  const ALEX = "Alex Aravena";
  const doc = D.documentos, P = doc.problema, q = doc.calidad, cont = doc.continuidad;
  const prm = D.parametros, fin = D.financiamiento, ind = D.indicadores;

  // ------------------------------------------------------------ 39 Compromisos medibles
  {
    const s = ctx.add("CONTENIDO_OSCURO", "Cierre", ALEX, "14:35",
      `Para cerrar, nuestros compromisos medibles. Llevar el OTIF de ${fmt(P.otif_actual_pct, 1)} % a un nivel sobre ${P.otif_meta_pct} %. Pasar de ${P.retiro_dias} días a menos de ${cont.identificar_clientes_h} horas para identificar a los clientes afectados por un lote. Sostener una disponibilidad mensual de la transacción crítica de al menos ${fmt(q.disponibilidad_pct, 1)} %, medida de extremo a extremo, con una recuperación ante desastres en cuatro horas o menos, probada con conmutación real al menos dos veces al año. Cada uno se verifica en la marcha blanca y en la operación.`);
    deco(s, "onda-naranjo", 1, { x: -11.3, y: 2.5, w: 12.67 });
    arc(s, "onda-naranjo-claro", 1, -11.3, 5.1);
    arc(s, "onda-naranjo", 2, 17.27, 1.93);
    deco(s, "onda-naranjo-claro", 2, { x: 17.24, y: -0.67, w: 12.67 });
    ctx.title(s, "Nuestros compromisos medibles");
    const k = [
      ["OTIF", `hoy ${fmt(P.otif_actual_pct, 1)} %`, `> ${P.otif_meta_pct} %`, "Entregas a tiempo y completas"],
      ["Retiro sanitario", `hoy ${P.retiro_dias} días`, `< ${cont.identificar_clientes_h} h`, "Identificar a los clientes afectados por un lote"],
      ["Disponibilidad", "transacción crítica", `≥ ${fmt(q.disponibilidad_pct, 1)} %`, "Disponibilidad mensual, medida sobre la transacción de negocio de extremo a extremo"],
      ["Recuperación", `RPO ≤ ${q.rpo_min} min`, `RTO ≤ ${q.rto_h} h`, "Ante un desastre; la conmutación real se prueba al menos dos veces al año"],
    ];
    const kw = (W - 3 * 0.4) / 4, kh = 5.3;
    k.forEach((d, i) => {
      const x = X0 + i * (kw + 0.4);
      card(s, x, Y0, kw, kh, { fill: { color: C.text1 }, line: { color: C.accent2, width: 1 }, objectName: `!!tarjeta_${i + 1}` });
      T(s, d[0].toUpperCase(), x + 0.4, Y0 + 0.4, kw - 0.8, 0.4, { fontSize: 16, bold: true, fontFace: H, color: C.accent4 });
      T(s, d[1], x + 0.4, Y0 + 1.0, kw - 0.8, 0.5, { fontSize: 20, color: C.accent6 });
      T(s, d[2], x + 0.4, Y0 + 1.7, kw - 0.8, 1.4, { fontSize: 54, bold: true, fontFace: H, color: C.accent1, valign: "middle" });
      T(s, d[3], x + 0.4, Y0 + 3.5, kw - 0.8, 1.5, { fontSize: 18, color: C.background1 });
    });
    T(s, "Cada compromiso se verifica con indicadores en la marcha blanca y en la operación.", X0, 8.75, W, 0.5, { fontSize: 20, color: C.accent6, objectName: "!!nota" });
  }

  // ------------------------------------------------------------ 40 "9 dias" (fade, avance automatico)
  const heroBase = (s) => {
    ctx.photo(s, 0, 0, 20, 11.25);
    deco(s, "puntos", 1, { x: 1.91, y: 1.12, w: 0.88, h: 0.22 });
    deco(s, "puntos", 2, { x: 17.24, y: 9.9, w: 0.88, h: 0.22 });
    deco(s, "onda-naranjo", 1, { x: -9.91, y: 2.5, w: 12.67, h: 6.33 });
    deco(s, "onda-naranjo-claro", 1, { x: -9.87, y: 5.1, w: 12.67, h: 6.33, rotate: 180, flipH: true });
    deco(s, "onda-naranjo", 2, { x: 17.27, y: 1.93, w: 12.67, h: 6.33, rotate: 180, flipH: true });
    deco(s, "onda-naranjo-claro", 2, { x: 17.24, y: -0.67, w: 12.67, h: 6.33 });
    ctx.brand(s, true, 9.64, 0.25, { k: 1.2, dx: -2.2, dy: 0.72, w: 4.42, align: "center" });
  };
  {
    const s = ctx.add("HERO", "Cierre", ALEX, "14:38", `${P.retiro_dias} días. (Transición automática a la lámina siguiente.)`);
    OVERRIDES[ctx.num()] = { type: "fade", advTm: 1500 };
    heroBase(s);
    ctx.N(s, "!!title", `${P.retiro_dias} días`, 2.0, 2.6, 16, 3.9, { fontSize: 230, bold: true, fontFace: H, color: C.background1, align: "center", valign: "middle" });
  }

  // ------------------------------------------------------------ 41 De 9 dias a < 2 horas
  {
    const s = ctx.add("HERO", "Cierre", ALEX, "15:00",
      `De ${P.retiro_dias} días a menos de ${cont.identificar_clientes_h} horas: el dato capturado donde ocurre, trazable de punta a punta, aun sin señal. Quedamos a disposición de la Comisión Evaluadora; con gusto responderemos sus preguntas. Muchas gracias.`);
    heroBase(s);
    ctx.N(s, "!!pre", `De ${P.retiro_dias} días a`, 2.0, 1.75, 16, 1.1, { fontSize: 48, color: C.background1, align: "center", valign: "middle" });
    ctx.N(s, "!!title", `< ${cont.identificar_clientes_h} horas`, 2.0, 2.75, 16, 3.3, { fontSize: 190, bold: true, fontFace: H, color: C.accent1, align: "center", valign: "middle" });
    ctx.N(s, "!!pie", "para identificar a los clientes afectados", 2.0, 6.1, 16, 0.6, { fontSize: 28, color: C.accent6, align: "center" });
    const contact = [
      ["icono-correo", "contacto@lafrox.cl"], ["icono-ubicacion", "Av. Brasil 2241, Valparaíso"],
      ["icono-web", "lafrox.github.io"], ["icono-telefono", "+56 32 250 4100"],
    ];
    const ih = 0.42;
    contact.forEach(([kind, txt], i) => {
      const x = 4.6 + (i % 2) * 6.4, y = 7.15 + Math.floor(i / 2) * 0.8;
      deco(s, kind, 1, { x, y: y + (0.5 - ih) / 2, w: ih * DECOR_RATIO[kind], h: ih });
      T(s, txt, x + 0.75, y, 5.4, 0.5, { fontSize: 22, color: C.background1, valign: "middle", objectName: `!!contacto_${i + 1}` });
    });
    ctx.N(s, "!!cierre", "Quedamos a disposición de la Comisión Evaluadora", 2.0, 9.0, 16, 0.6, { fontSize: 28, color: C.accent4, align: "center", fontFace: "Inter Light" });
  }

  // ------------------------------------------------------------ Anexo
  const AN = "Anexo";
  {
    const s = ctx.add("SECCION", AN, ALEX, null,
      "Anexo de respaldo para la sesión de preguntas: supuestos del modelo financiero, principales proveedores, adquisiciones de implementación y flujo de caja mensual.");
    RINGS(s, 9.5, -3.2, 13, 1);
    arc(s, "onda-naranjo-claro", 1, -11.4, 5.1);
    deco(s, "onda-naranjo-claro", 2, { x: 17.24, y: -0.67, w: 12.67 });
    s.addText("A", { placeholder: "numero" });
    s.addText("Anexo", { placeholder: "title" });
    s.addText("Material de respaldo para la sesión de preguntas", { placeholder: "subtitulo" });
  }
  const decorA = (s) => {
    deco(s, "cuarto-circulo", 1, { x: 18.5, y: -3.8, w: 6.0, h: 6.0 });
    RINGS(s, -2.47, 9.69, 11.2, 1);
  };
  // A1 Supuestos
  {
    const s = ctx.add("COMPACTO", AN, "Leandro Chamorro", null, "Supuestos del modelo financiero: valores de la UF y del dólar, tasa de descuento, horizonte, IVA, impuesto a la renta, financiamiento y factor de tarifa de recursos humanos. Fuente: hoja PARAMETROS del modelo SD7.");
    decorA(s);
    ctx.title(s, "Anexo · Supuestos del modelo");
    const items = [
      ["Valor de la UF", `$${fmt(prm.uf_clp)}`], ["Tipo de cambio (USD)", `$${fmt(prm.usd_clp)}`],
      ["Tasa de descuento", `${fmt(prm.tasa_descuento_mensual * 100, 3)} % mensual (${fmt(fin.tasa_descuento_anual * 100, 2)} % anual)`],
      ["Horizonte de evaluación", `${prm.horizonte_meses} meses desde ${prm.inicio_proyecto.split("-").reverse().join("-")}`],
      ["IVA", pct(prm.iva, 0)], ["Impuesto a la renta", pct(prm.impuesto, 0)],
      ["Capital inicial", `${fmt(prm.capital_inicial_uf)} UF (${fmt(prm.pct_bancario * 100)} % crédito, ${fmt(prm.pct_propio * 100)} % socios)`],
      ["Costo del crédito", `${fmt(prm.tasa_credito_mensual * 100, 1)} % mensual, ${fin.cuotas} cuotas`],
      ["Costo del capital propio", `${fmt(prm.costo_capital_propio_anual * 100)} % anual`],
      ["Tarifa de RR.HH.", `costo × ${fmt(prm.factor_tarifa_rrhh, 2)} · ${fmt(prm.hh_mes)} HH por mes`],
    ];
    const cw = (W - 0.3) / 2, ch = 1.3;
    items.forEach((it, i) => {
      const x = X0 + (i % 2) * (cw + 0.3), y = 1.95 + Math.floor(i / 2) * (ch + 0.2);
      card(s, x, y, cw, ch, { objectName: `!!tarjeta_${i + 1}` });
      T(s, it[0], x + 0.35, y, 3.4, ch, { fontSize: 18, color: C.accent3, valign: "middle" });
      T(s, it[1], x + 3.6, y, cw - 3.9, ch, { fontSize: 18, bold: true, fontFace: H, valign: "middle" });
    });
    ctx.src(s, "Fuente: modelo financiero SD7, hoja PARAMETROS.", 9.95);
  }
  // A2 Proveedores
  {
    const s = ctx.add("COMPACTO", AN, "Leandro Chamorro", null, "Principales proveedores de implementación según el costo total estimado, con el bien o servicio principal de cada uno. En operación, los servicios de nube de AWS son el principal costo recurrente.");
    decorA(s);
    ctx.title(s, "Anexo · Principales proveedores");
    const rows = [[th("Proveedor"), th("Bien o servicio principal"), th("Implementación (UF)", "right")]];
    D.proveedores.top_implementacion.forEach((p, i) => rows.push([td(p.proveedor, i), td(p.bien, i), td(fmt(p.impl_uf, 1), i, { align: "right" })]));
    s.addTable(rows, { x: X0, y: 1.9, w: W, colW: [6.6, 6.2, 4.0], rowH: 0.62, border: tblBorder(), margin: [0.03, 0.2, 0.03, 0.2], objectName: "Tabla de proveedores" });
    ctx.src(s, `Costo total estimado de implementación, en UF. Operación: los servicios AWS suman ${fmt(D.proveedores.aws_operacion_uf_mes, 1)} UF por mes de referencia (M${D.operacion.mes_desde} a M${D.operacion.mes_hasta}). Fuente: hoja PROVEEDORES.`, 9.95);
  }
  // A3 Adquisiciones
  {
    const s = ctx.add("COMPACTO", AN, "Leandro Chamorro", null, "Adquisiciones de implementación: los diez componentes de mayor costo. El total de la fase de implementación, al pie de la tabla, incluye además los componentes no listados.");
    decorA(s);
    ctx.title(s, "Anexo · Adquisiciones de implementación");
    const a = D.adquisiciones_implementacion;
    const rows = [[th("Categoría"), th("Componente"), th("Cant.", "right"), th("Total (UF)", "right")]];
    a.top.forEach((it, i) => rows.push([td(it.categoria, i), td(it.componente, i), td(fmt(it.cantidad), i, { align: "right" }), td(fmt(it.total_uf, 1), i, { align: "right" })]));
    rows.push([td("Total de adquisiciones de implementación (incluye componentes no listados)", 10, { bold: true, colspan: 3 }), td(fmt(a.total_uf, 1), 10, { bold: true, align: "right" })]);
    s.addTable(rows, { x: X0, y: 1.9, w: W, colW: [4.6, 7.0, 1.6, 3.6], rowH: 0.62, border: tblBorder(), margin: [0.03, 0.2, 0.03, 0.2], objectName: "Tabla de adquisiciones" });
    ctx.src(s, `Costo total sin IVA, en UF. Los 10 componentes mostrados suman ${fmt(a.top.reduce((t, it) => t + it.total_uf, 0), 1)} UF (derivado); el total incluye además el resto de las categorías. Fuente: hoja ADQUISICIONES IMPLEMENTACIÓN.`, 9.95);
  }
  // A4 Flujo mensual
  {
    const F = D.flujo_mensual, CS = D.curva_s;
    const s = ctx.add("COMPACTO", AN, "Leandro Chamorro", null, `Flujo de caja mensual del proyecto, sin financiamiento y antes de impuestos: columnas con el flujo de cada mes y línea con el acumulado. El mínimo acumulado es de ${fmt(F.minimo_acumulado_uf)} UF en el mes ${F.minimo_acumulado_mes}; con el financiamiento inicial, la caja mínima es de ${fmt(CS.caja_minima_uf)} UF en el mes ${CS.caja_minima_mes}.`);
    decorA(s);
    ctx.title(s, "Anexo · Flujo de caja mensual");
    const labels = F.meses.map((m) => String(m));
    s.addChart([
      { type: pres.charts.BAR, data: [{ name: "Flujo del mes", labels, values: F.flujo_proyecto }], options: { barDir: "col", barGapWidthPct: 40, chartColors: ["F29A5E"] } },
      { type: pres.charts.LINE, data: [{ name: "Flujo acumulado", labels, values: F.flujo_acumulado }], options: { chartColors: ["111111"], lineSize: 3, lineDataSymbol: "none" } },
    ], { ...chartBase(), x: X0, y: 1.85, w: W, h: 6.9, showLegend: true, legendPos: "b", showValue: false, valAxisMinVal: -20000, valAxisMaxVal: 40000, valAxisMajorUnit: 10000, valAxisLabelFormatCode: "#,##0", catAxisLabelFrequency: 4, catAxisLabelPos: "low" });
    T(s, `Mínimo acumulado: ${fmt(F.minimo_acumulado_uf)} UF (mes ${F.minimo_acumulado_mes}) · Acumulado al mes ${prm.horizonte_meses}: ${fmt(F.flujo_acumulado[F.flujo_acumulado.length - 1])} UF · Caja mínima con financiamiento: ${fmt(CS.caja_minima_uf)} UF (mes ${CS.caja_minima_mes})`, X0, 8.95, W, 0.8, { fontSize: 18, color: C.text1 });
    ctx.src(s, "UF por mes, flujo del proyecto sin financiamiento ni impuestos. Fuente: modelo financiero SD7, hoja INDICADORES.", 9.95);
  }
};
