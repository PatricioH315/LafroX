// A. Apertura (laminas 1-5): portada, equipo, agenda, "9 dias", problematica.
module.exports = function apertura(ctx) {
  const { kit, D, fmt, pct } = ctx;
  const { pres, C, H, B, X0, W, XR, Y0, T, card, darkCard, circle, deco, arc, RINGS, QUARTER, DECOR_RATIO } = kit;
  const P = D.documentos.problema;
  const ALEX = "Alex Aravena";

  // Ondas del bloque de apertura (mismos nombres en laminas consecutivas para que se deslicen)
  const wavesCover = (s) => {
    deco(s, "onda-naranjo-claro", 1, { x: 6.66, y: -7.43, w: 24.16, h: 12.08 });
    deco(s, "onda-naranjo", 1, { x: 8.28, y: 0.98, w: 24.16, h: 12.08, rotate: 180, flipH: true });
  };

  // ---- 1 Portada (fade)
  {
    const s = ctx.add("HERO", "Apertura", ALEX, "0:20",
      "Buenos días, señoras y señores de la Comisión Evaluadora de Distribuidora Puelche. Somos LafroX SpA y presentamos nuestra oferta para la Licitación TFEP-01/2026: el Sistema Integral de Gestión Logística Puelche. Dispondremos de quince minutos de exposición y quince minutos de preguntas.");
    ctx.photo(s, 0, 0, 20, 11.25);
    wavesCover(s);
    ctx.brand(s, true, 1.61, 0.93);
    s.addText(
      [
        { text: "Propuesta", options: { bold: false, fontFace: B, breakLine: true } },
        { text: "Técnica y Económica", options: { bold: true } },
      ],
      {
        x: 1.56, y: 2.6, w: 14.2, h: 3.3, margin: 0, isTextBox: true, valign: "top", fontSize: 80, color: C.background1,
        fontFace: H, objectName: "!!title",
      }
    );
    ctx.N(s, "!!subtitulo", [
      { text: "Licitación TFEP-01/2026 · Sistema Integral de Gestión Logística Puelche", options: { breakLine: true } },
      { text: "ante la Comisión Evaluadora de Distribuidora Puelche S.A. · 27 de noviembre de 2026" },
    ], 1.61, 6.4, 12.5, 1.2, { fontSize: 22, color: C.background1, paraSpaceAfter: 6 });
    ctx.N(s, "!!oferente", "LafroX SpA · Oferente", 1.61, 9.9, 10, 0.4, { fontSize: 18, color: C.accent6 });
  }

  // ---- 2 Equipo (la foto se achica a un panel izquierdo)
  {
    const s = ctx.add("BLANCO", "Apertura", ALEX, "0:45",
      "Nos dirige Alex Aravena, Jefe de Proyecto e interlocutor frente al cliente. Junto a él, nueve líderes de especialidad cubren arquitectura, seguridad, datos, desarrollo, calidad, operación, implantación, el frente funcional y la integración: diez personas nominadas para los diez roles mínimos que exigen las bases. Varios de ellos presentarán partes de esta oferta.");
    ctx.photo(s, 0, 0, 9.6, 11.25);
    deco(s, "onda-naranjo", 1, { x: -9.91, y: 2.5, w: 12.67, h: 6.33 });
    deco(s, "onda-naranjo-claro", 1, { x: -9.87, y: 5.1, w: 12.67, h: 6.33, rotate: 180, flipH: true });
    deco(s, "onda-naranjo", 2, { x: 20.33, y: 1.93, w: 12.67, h: 6.33, rotate: 180, flipH: true });
    deco(s, "onda-naranjo-claro", 2, { x: 20.33, y: -0.67, w: 12.67, h: 6.33 });
    RINGS(s, 15.21, 0.83, 9.57, 1);
    ctx.brand(s, true, 1.61, 0.93);
    ctx.N(s, "!!title", "El Equipo", 3.0, 4.45, 6.3, 1.79, { fontSize: 54, bold: true, fontFace: H, color: C.background1, valign: "middle" });
    const x = 9.9, w = XR + 1.0 - x;
    const ppl = D.documentos.equipo;
    darkCard(s, x, 0.8, w, 1.4, "!!tarjeta_1");
    circle(s, ppl[0][0], x + 0.4, 0.8 + 0.25, 0.9);
    T(s, ppl[0][1], x + 1.6, 0.8 + 0.25, w - 1.9, 0.5, { fontSize: 24, bold: true, fontFace: H, color: C.background1, objectName: "!!nombre_1" });
    T(s, ppl[0][2] + " · interlocutor frente al cliente", x + 1.6, 0.8 + 0.77, w - 1.9, 0.4, { fontSize: 16, color: C.accent6, objectName: "!!cargo_1" });
    // nueve tarjetas (3 x 3): nombres y cargos tal como figuran en el Formulario T-8
    const cw = (w - 0.6) / 3, ch = 2.3;
    ppl.slice(1).forEach((p, i) => {
      const cx = x + (i % 3) * (cw + 0.3), cy = 2.45 + Math.floor(i / 3) * (ch + 0.2);
      card(s, cx, cy, cw, ch, { objectName: `!!tarjeta_${i + 2}` });
      circle(s, p[0], cx + 0.3, cy + 0.25, 0.7);
      T(s, p[1], cx + 0.3, cy + 1.05, cw - 0.4, 0.4, { fontSize: 18, bold: true, fontFace: H, objectName: `!!nombre_${i + 2}` });
      T(s, p[2], cx + 0.3, cy + 1.5, cw - 0.4, 0.7, { fontSize: 15, color: C.accent3, valign: "top", objectName: `!!cargo_${i + 2}` });
    });
  }

  // ---- 3 Agenda / protocolo (la foto pasa a un panel derecho)
  {
    const s = ctx.add("BLANCO", "Apertura", ALEX, "1:10",
      "Este es el protocolo de la sesión: cinco actos, cada uno a cargo del responsable del área. Comenzamos con el entendimiento del problema, seguimos con la solución técnica, la ejecución y la calidad, la innovación y la oferta económica, y cerramos con nuestros compromisos medibles. Reservamos quince minutos para las preguntas de la Comisión.");
    ctx.photo(s, 11.6, 3.0, 6.8, 7.05);
    deco(s, "onda-naranjo", 1, { x: -9.91, y: 2.5, w: 12.67, h: 6.33 });
    deco(s, "onda-naranjo-claro", 1, { x: -9.87, y: 5.1, w: 12.67, h: 6.33, rotate: 180, flipH: true });
    deco(s, "onda-naranjo", 2, { x: 20.33, y: 1.93, w: 12.67, h: 6.33, rotate: 180, flipH: true });
    deco(s, "onda-naranjo-claro", 2, { x: 20.33, y: -0.67, w: 12.67, h: 6.33 });
    RINGS(s, 15.21, 0.83, 9.57, 1);
    ctx.brand(s, false, 1.61, 0.93);
    ctx.N(s, "!!title", "Agenda de la exposición", 1.61, 1.65, 10.5, 0.95, { fontSize: 44, bold: true, fontFace: H, color: C.text1 });
    const acts = [
      ["01", "Entendimiento del problema", "0:00 a 3:00", "Alex Aravena"],
      ["02", "Solución técnica", "3:00 a 6:30", "Bastián Trejo y Tomás Pérez"],
      ["03", "Ejecución y calidad", "6:30 a 10:00", "Alex Aravena, Maximiliano Miño y Guillermo Castillo"],
      ["04", "Innovación y oferta económica", "10:00 a 14:15", "Patricio Henríquez y Leandro Chamorro"],
      ["05", "Cierre y compromisos", "14:15 a 15:00", "Alex Aravena"],
    ];
    const ah = 1.25, ag = 0.2;
    acts.forEach((a, i) => {
      const y = 3.0 + i * (ah + ag);
      card(s, X0, y, 9.7, ah, { objectName: `!!tarjeta_${i + 1}` });
      T(s, a[0], X0 + 0.35, y, 0.9, ah, { fontSize: 28, bold: true, fontFace: H, color: C.accent1, valign: "middle" });
      T(s, a[1], X0 + 1.4, y + 0.2, 5.6, 0.45, { fontSize: 22, bold: true, fontFace: H });
      T(s, a[2], X0 + 7.1, y + 0.22, 2.3, 0.4, { fontSize: 18, bold: true, color: C.accent3, align: "right" });
      T(s, a[3], X0 + 1.4, y + 0.74, 8.0, 0.4, { fontSize: 16, color: C.accent3 });
    });
    ctx.N(s, "!!tiempo", [
      { text: "15 min", options: { fontSize: 66, bold: true, fontFace: H, color: C.background1, breakLine: true } },
      { text: "de exposición", options: { fontSize: 22, color: C.accent6, breakLine: true } },
      { text: " ", options: { fontSize: 22, breakLine: true } },
      { text: "15 min", options: { fontSize: 66, bold: true, fontFace: H, color: C.accent1, breakLine: true } },
      { text: "de preguntas de la Comisión", options: { fontSize: 22, color: C.accent6 } },
    ], 12.1, 3.6, 5.9, 5.5, { valign: "middle" });
  }

  // ---- 4 "9 dias" (la foto vuelve a pantalla completa)
  {
    const s = ctx.add("HERO", "Apertura", ALEX, "1:40",
      `Marzo de 2026: un retiro sanitario. Distribuidora Puelche tardó ${P.retiro_dias} días en saber a qué clientes había llegado el producto. Fueron ${fmt(P.kg)} kilos retirados, y el proveedor de lácteos, que representa el ${P.ventas_riesgo_pct} % de las ventas, suspendió a Puelche por ${P.suspension_meses} meses. Les pedimos que recuerden esta cifra: nueve días.`);
    ctx.photo(s, 0, 0, 20, 11.25);
    deco(s, "onda-naranjo", 1, { x: -9.91, y: 2.5, w: 12.67, h: 6.33 });
    deco(s, "onda-naranjo-claro", 1, { x: -9.87, y: 5.1, w: 12.67, h: 6.33, rotate: 180, flipH: true });
    deco(s, "onda-naranjo", 2, { x: 17.27, y: 1.93, w: 12.67, h: 6.33, rotate: 180, flipH: true });
    deco(s, "onda-naranjo-claro", 2, { x: 17.24, y: -0.67, w: 12.67, h: 6.33 });
    ctx.brand(s, true, 9.64, 0.25, { k: 1.2, dx: -2.2, dy: 0.72, w: 4.42, align: "center" });
    ctx.N(s, "!!kicker", "MARZO 2026 · RETIRO SANITARIO", 2.0, 1.95, 16, 0.5, { fontSize: 22, bold: true, color: C.accent4, align: "center", fontFace: H });
    ctx.N(s, "!!reloj", `${P.retiro_dias} días`, 2.0, 2.6, 16, 3.9, { fontSize: 230, bold: true, fontFace: H, color: C.background1, align: "center", valign: "middle" });
    ctx.N(s, "!!pie", "para identificar a los clientes afectados", 2.0, 6.55, 16, 0.6, { fontSize: 30, color: C.accent6, align: "center" });
    const stats = [[`${fmt(P.kg)} kg`, "retirados"], [`${P.suspension_meses} meses`, "de suspensión del proveedor"], [`${P.ventas_riesgo_pct} %`, "de las ventas, el proveedor suspendido"]];
    stats.forEach((st, i) => {
      const x = 2.6 + i * 5.1;
      ctx.N(s, `!!dato_${i + 1}`, [
        { text: st[0], options: { fontSize: 40, bold: true, fontFace: H, color: C.accent1, breakLine: true } },
        { text: st[1], options: { fontSize: 20, color: C.accent6 } },
      ], x, 7.9, 4.6, 1.5, { align: "center" });
    });
  }

  // ---- 5 Problematica (el reloj se achica dentro de la primera tarjeta)
  {
    const s = ctx.add("BLANCO", "Apertura", ALEX, "2:35",
      `Tres problemas que parecen distintos y tienen una sola causa. Primero, una habilitación sanitaria y comercial comprometida: ${P.retiro_dias} días para identificar clientes. Segundo, un servicio que pierde competitividad: el OTIF es de ${fmt(P.otif_actual_pct, 1)} %, frente a una referencia sobre ${P.otif_meta_pct} %. Tercero, un costo de servir desconocido, calculado con un criterio de prorrateo de ${P.costo_servir_anio}. La causa común es que el dato no se registra donde ocurre el hecho; esa es la brecha que cierra nuestra solución.`);
    deco(s, "onda-naranjo", 1, { x: -5.92, y: 7.63, w: 12.15, h: 6.07 });
    RINGS(s, 10.29, 6.25, 11.2, 1);
    deco(s, "cuarto-circulo", 1, { x: 17.63, y: -3.06, w: 7.02, h: 7.02 });
    ctx.brand(s, false, 1.61, 0.93);
    ctx.N(s, "!!title", "Problemática", 1.61, 1.75, 8.39, 1.5, { fontSize: 60, bold: true, fontFace: H, color: C.text1 });
    ctx.N(s, "!!subtitulo", "Tres problemas y una sola causa", 1.61, 3.2, 8.4, 0.5, { fontSize: 24, color: C.accent3 });
    darkCard(s, X0, 4.9, 7.4, 2.9, "!!panel_oscuro");
    T(s, "CAUSA RAÍZ", X0 + 0.45, 5.25, 5, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent4 });
    T(s, "El dato no se registra donde ocurre el hecho.", X0 + 0.45, 5.8, 6.5, 1.8, { fontSize: 28, bold: true, fontFace: H, color: C.background1 });
    const cx = 10.4, cw = 8.0, ch = 2.05;
    const items = [
      ["01", "Habilitación sanitaria y comercial comprometida", "Retiro de", "!!reloj", `${P.retiro_dias} días`],
      ["02", "Pérdida de competitividad del servicio", "OTIF", "!!otif", `${fmt(P.otif_actual_pct, 1)} %`],
      ["03", "Desconocimiento estructural del costo de servir", "Criterio de", "!!costo", String(P.costo_servir_anio)],
    ];
    items.forEach((it, i) => {
      const y = 2.9 + i * (ch + 0.3);
      card(s, cx, y, cw, ch, { objectName: `!!tarjeta_${i + 1}` });
      T(s, it[0], cx + 0.4, y + 0.35, 1.0, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent1 });
      T(s, it[1], cx + 0.4, y + 0.75, 4.2, 1.2, { fontSize: 20, bold: true, fontFace: H });
      T(s, it[2], cx + cw - 3.6, y + 0.3, 3.2, 0.4, { fontSize: 16, color: C.accent3, align: "right", objectName: `!!meta_${i + 1}` });
      ctx.N(s, it[3], it[4], cx + cw - 3.6, y + 0.85, 3.2, 0.9, { fontSize: 44, bold: true, fontFace: H, color: C.accent1, align: "right", valign: "middle" });
    });
    ctx.src(s, "Fuente: Subdocumento 2, Comprensión del problema y de la necesidad.", 9.85);
  }
};
