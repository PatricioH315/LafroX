// B. Solucion (laminas 6-16): mapa de modulos, arquitectura logica y 8 capas, trazabilidad y continuidad.
module.exports = function solucion(ctx) {
  const { kit, D } = ctx;
  const { pres, C, H, B, X0, W, XR, Y0, YB, T, card, darkCard, pill, deco, RINGS, QUARTER } = kit;
  const BT = "Bastián Trejo", TP = "Tomás Pérez";
  const SEC = "Solución";
  const cont = D.documentos.continuidad;

  const decorB = (s) => {
    deco(s, "cuarto-circulo", 1, { x: 18.5, y: -3.8, w: 6.0, h: 6.0 });
    RINGS(s, -2.47, 9.69, 11.2, 1);
  };

  // ---- 6 Mapa de modulos (nativo)
  {
    const s = ctx.add("COMPACTO", SEC, BT, "3:50",
      "Este es el mapa del sistema: siete interfaces para los distintos actores, doce módulos agrupados por frente y tres sistemas externos, que son el ERP, Transbank y la geolocalización. El dato fluye desde la recepción hacia el inventario, la preparación y el reparto. El ERP sigue siendo el único emisor tributario y se accede mediante una capa anticorrupción; el único módulo que espera a la Etapa 2 es el canal moderno.");
    decorB(s);
    ctx.title(s, "Mapa de módulos");
    // Interfaces
    T(s, "INTERFACES", X0, 1.85, 3.2, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent1 });
    ["App Preventa", "App Reparto", "App Bodega", "Portal Clientes", "Portal Transportistas", "Portal Proveedores", "Consolas"].forEach((t, i) =>
      pill(s, t, X0, 2.4 + i * 0.88, 3.2, 0.7, { objectName: `!!interfaz_${i + 1}` })
    );
    s.addShape(pres.shapes.RIGHT_ARROW, { x: 5.0, y: 5.05, w: 0.5, h: 0.4, fill: { color: C.accent1 }, objectName: "!!flecha_1" });
    // Grupos de modulos
    const group = (title, x, y, w, h, mods, cols) => {
      card(s, x, y, w, h, { objectName: `!!grupo_${title}` });
      T(s, title, x + 0.3, y + 0.2, w - 0.6, 0.4, { fontSize: 18, bold: true, fontFace: H });
      const cw = (w - 0.6 - (cols - 1) * 0.15) / cols, chh = 1.35;
      mods.forEach((m, i) => {
        const cx = x + 0.3 + (i % cols) * (cw + 0.15), cy = y + 0.85 + Math.floor(i / cols) * (chh + 0.15);
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: cx, y: cy, w: cw, h: chh, rectRadius: 0.12, fill: { color: C.background2 }, line: { color: C.background2, width: 0.5 }, objectName: `!!modulo_${m[0]}` });
        T(s, m[0], cx + 0.15, cy + 0.12, cw - 0.3, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent1 });
        T(s, m[1], cx + 0.15, cy + 0.5, cw - 0.3, 0.8, { fontSize: 16, color: C.text1 });
      });
    };
    group("Bodega y calidad", 5.7, 1.85, 6.4, 3.95, [["M1", "Recepción"], ["M2", "Inventario"], ["M5", "Preparación"], ["M9", "Calidad y trazabilidad"], ["M12", "Telemetría"]], 3);
    group("Canal moderno", 12.3, 1.85, 3.3, 3.95, [["M11", "EDI"]], 1);
    group("Preventa, rutas y reparto", 5.7, 6.0, 6.4, 3.95, [["M3", "Preventa"], ["M4", "Rutas + GIS"], ["M6", "Reparto"], ["M8", "Devoluciones y envases"]], 3);
    group("Datos y rendición", 12.3, 6.0, 3.3, 3.95, [["M7", "Cobranza y rendición"], ["M10", "Analítica BI"]], 1);
    // Sistemas externos
    T(s, "SISTEMAS EXTERNOS", 16.1, 1.85, 2.8, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent1 });
    ["ERP 2017", "Transbank", "Geolocalización"].forEach((t, i) =>
      pill(s, t, 16.1, 2.4 + i * 1.2, 2.4, 0.8, { objectName: `!!externo_${i + 1}`, fill: { color: i === 0 ? C.text1 : C.background2 }, color: i === 0 ? C.background1 : C.text1, bold: i === 0 })
    );
    s.addShape(pres.shapes.RIGHT_ARROW, { x: 15.65, y: 2.65, w: 0.4, h: 0.3, fill: { color: C.accent1 }, objectName: "!!flecha_2" });
    ctx.src(s, "Fuente: Subdocumentos 3 y 4 (figuras 3.4 a 3.8 y anexo 4-F).", 10.2);
  }

  // ---- 7 Arquitectura general
  const LAYERS = [
    ["Presentación", "captura y muestra la información", "Aplicaciones, portales y dispositivos de cada actor"],
    ["Borde y exposición", "protege la entrada", "Protección de las entradas públicas, privadas y locales"],
    ["Enlace de servicios", "valida las solicitudes", "Validación de solicitudes y acceso local del WMS"],
    ["Lógica de negocio", "aplica las reglas de M1 a M12 en Laravel", "Reglas de negocio de los doce módulos Laravel"],
    ["Integración y eventos", "conserva y distribuye eventos", "Intercambio de eventos y continuidad de los sitios"],
    ["Acceso a datos", "administra la persistencia", "Propiedad de los datos y persistencia híbrida"],
    ["Seguridad transversal", "atraviesa todas las capas", "Identidad y autorización en todas las capas"],
    ["Observabilidad transversal", "atraviesa todas las capas", "Correlación y seguimiento de la operación"],
  ];
  const IMG_R = 2048 / 1884;
  {
    const s = ctx.add("COMPACTO", SEC, BT, "4:15",
      "La arquitectura lógica relaciona a cada actor con su aplicación, portal o consola y con los módulos M1 a M12. Se lee en ocho capas: presentación, borde, enlace de servicios, lógica de negocio, integración y eventos, y acceso a datos; la seguridad y la observabilidad atraviesan todas ellas. Las conexiones son intercambios autorizados, no acceso directo a las bases de datos, y la puerta local permite que la bodega siga operando sin enlace.");
    decorB(s);
    ctx.title(s, "Arquitectura lógica en ocho capas");
    LAYERS.forEach((l, i) => {
      const y = 2.0 + i * 0.99;
      T(s, String(i + 1), X0, y, 0.6, 0.8, { fontSize: 28, bold: true, fontFace: H, color: C.accent1, valign: "middle", objectName: `!!capalista_n${i + 1}` });
      T(s, [
        { text: l[0], options: { bold: true, fontFace: H, fontSize: 20, breakLine: true } },
        { text: l[1], options: { fontSize: 16, color: C.accent3 } },
      ], X0 + 0.8, y, 6.6, 0.85, { valign: "middle", objectName: `!!capalista_${i + 1}` });
    });
    const th = 8.4, tw = th * IMG_R;
    s.addImage({ path: kit.A("final/arq-general.png"), x: XR + 0.6 - tw, y: 1.8, w: tw, h: th, objectName: "!!thumb", altText: "Diagrama de arquitectura lógica general de ocho capas" });
    ctx.src(s, "Fuente: Subdocumento 4, figura 1.", 10.2);
  }

  // ---- 8-15 Capas
  const HL = [[2.61, 0.81], [3.34, 0.27], [3.53, 0.3], [3.75, 0.71], [4.38, 0.4], [4.69, 0.65], [5.26, 0.34], [5.51, 0.34]]; // v4 (y, h) sobre una miniatura de 3.15 in
  const ORDER = [
    [BT, "4:27"], [TP, "4:39"], [BT, "4:51"], [TP, "5:03"], [BT, "5:15"], [BT, "5:27"], [TP, "5:39"], [TP, "5:51"],
  ];
  const SCRIPT = [
    "Capa 1, presentación. Aquí viven las aplicaciones móviles de preventa, reparto y bodega, los portales de clientes, transportistas y proveedores, y las consolas. Cada actor ve solo lo que necesita para su trabajo.",
    "Capa 2, borde y exposición. Protege las entradas públicas, privadas y locales antes de que cualquier solicitud llegue a la lógica del sistema.",
    "Capa 3, enlace de servicios. Valida cada solicitud y ofrece el acceso local del WMS, de modo que la bodega siga operando si se corta el enlace.",
    "Capa 4, lógica de negocio. Aquí se aplican las reglas de los doce módulos, desarrollados en Laravel; es la capa donde se materializa el valor funcional.",
    "Capa 5, integración y eventos. Conserva y distribuye los eventos entre sitios y con sistemas externos, y sostiene la continuidad cuando se pierde conectividad.",
    "Capa 6, acceso a datos. Cada módulo es dueño de sus datos y la persistencia es híbrida; ningún sistema accede directamente a las bases de otro.",
    "Capa 7, seguridad transversal. Identidad y autorización en todas las capas, con el principio de mínimo privilegio.",
    "Capa 8, observabilidad transversal. Correlaciona y da seguimiento a cada operación, de punta a punta, para detectar y diagnosticar rápidamente.",
  ];
  const thumbX = X0, thumbY = 2.65, thumbH = 3.15, thumbW = thumbH * IMG_R;
  for (let k = 0; k < 8; k++) {
    const s = ctx.add("COMPACTO", SEC, ORDER[k][0], ORDER[k][1], SCRIPT[k]);
    decorB(s);
    ctx.title(s, `Capa ${k + 1}. ${LAYERS[k][0]}`);
    ctx.N(s, "!!vista", "Vista general", thumbX, 2.1, 3.6, 0.4, { fontSize: 16, color: C.accent3 });
    s.addImage({ path: kit.A("final/arq-general.png"), x: thumbX, y: thumbY, w: thumbW, h: thumbH, objectName: "!!thumb", altText: "Miniatura de la arquitectura general" });
    const hy = thumbY + (HL[k][0] - 2.66) * (thumbH / 3.15), hh = HL[k][1] * (thumbH / 3.15);
    s.addShape(pres.shapes.RECTANGLE, { x: thumbX - 0.08, y: hy, w: thumbW + 0.16, h: hh, fill: { type: "none" }, line: { color: C.accent1, width: 2.25 }, objectName: "!!capahl" });
    ctx.N(s, "!!capan", `Capa ${k + 1} de 8`, thumbX, 6.25, 3.6, 0.55, { fontSize: 26, bold: true, color: C.accent1 });
    ctx.N(s, "!!capadesc", LAYERS[k][2], thumbX, 6.95, 3.7, 2.4, { fontSize: 20, color: C.accent3 });
    // capa a pantalla: contener en caja (5.7, 1.8, 12.7 x 8.0), centrada horizontalmente
    const file = kit.A(`final/capa${k + 1}.png`);
    const b = require("fs").readFileSync(file);
    const r = b.readUInt32BE(16) / b.readUInt32BE(20);
    const bx = 5.7, bw = 12.7, bh = 8.0;
    let w = bw, h = bw / r;
    if (h > bh) { h = bh; w = bh * r; }
    s.addImage({ path: file, x: bx + (bw - w) / 2, y: 1.8, w, h, objectName: "!!capaimg", altText: `Diagrama de la capa ${k + 1}: ${LAYERS[k][0]}` });
  }

  // ---- 16 Trazabilidad y continuidad
  {
    const s = ctx.add("COMPACTO", SEC, TP, "6:30",
      `Cerramos la solución con dos garantías. Primera, la trazabilidad: ante un retiro, la lista de clientes afectados por un lote se obtiene en menos de ${cont.identificar_clientes_h} horas, no en nueve días. Segunda, la continuidad: preventa y reparto trabajan ${cont.horas_sin_senal} horas sin señal y el centro de distribución al menos ${cont.horas_sin_enlace} horas sin enlace; al volver la conexión, la sincronización tarda como máximo ${cont.sync_min} minutos y ${cont.sync_horas} horas, respectivamente.`);
    decorB(s);
    ctx.title(s, "Trazabilidad y continuidad");
    card(s, X0, 1.85, 8.0, 7.95, { objectName: "!!tarjeta_1" });
    s.addImage({ path: kit.A("final/fig-trazabilidad.png"), x: X0 + 0.2, y: 2.05, w: 7.6, h: 7.6 / (2046 / 1811), altText: "Figura 3.2: trazabilidad y cadena de frío" });
    T(s, "Figura 3.2 · Trazabilidad y cadena de frío (Subdocumento 3)", X0 + 0.3, 9.25, 7.4, 0.35, { fontSize: 13, color: C.accent3 });
    const rx = 10.0, rw = XR - rx;
    card(s, rx, 1.85, rw, 2.85, { objectName: "!!tarjeta_2" });
    s.addImage({ path: kit.A("final/fig-continuidad.png"), x: rx + 0.2, y: 2.0, w: rw - 0.4, h: (rw - 0.4) / (2044 / 550), altText: "Figura 3.3: continuidad durante cortes" });
    T(s, "Figura 3.3 · Continuidad durante cortes (Subdocumento 3)", rx + 0.3, 4.2, rw - 0.6, 0.35, { fontSize: 13, color: C.accent3 });
    const kp = [
      [`< ${cont.identificar_clientes_h} h`, "para identificar a los clientes afectados por un lote"],
      [`${cont.horas_sin_senal} h / ${cont.horas_sin_enlace} h`, "de operación sin señal en terreno / sin enlace en los centros"],
      [`${cont.sync_min} min / ${cont.sync_horas} h`, "de sincronización máxima al volver la conexión"],
    ];
    kp.forEach((k, i) => {
      const y = 4.95 + i * 1.65;
      card(s, rx, y, rw, 1.45, { objectName: `!!kpi_${i + 1}` });
      T(s, k[0], rx + 0.35, y, 3.4, 1.45, { fontSize: 34, bold: true, fontFace: H, color: C.accent1, valign: "middle" });
      T(s, k[1], rx + 3.9, y, rw - 4.2, 1.45, { fontSize: 18, color: C.accent3, valign: "middle" });
    });
  }
};
