/**
 * Generador de la plantilla LafroX (Canva-style).
 * Uso: node build_template.js   ->  "LafroX - Plantilla.pptx"
 * Todo el contenido es de ejemplo; reutilice las laminas duplicandolas en PowerPoint
 * o edite este generador y vuelva a ejecutarlo (no editar el .pptx a mano).
 */
const path = require("path");
const pptxgen = require("pptxgenjs");

const SKILL =
  "C:/Users/henri/AppData/Local/Claude-Data/claude_pzs8sxrjxfjjc/local-agent-mode-sessions/skills-plugin/0cc4aafe-fe17-40e0-8a2d-d71c9c2b7355/f5b4c97f-b594-476b-8792-d6ce8e876c57/skills/pptx";
const { applyTheme } = require(SKILL + "/scripts/apply_theme.js");

const OUT = path.join(__dirname, "LafroX - Plantilla.pptx");
const A = (f) => path.join(__dirname, "assets", f);

// ---------------------------------------------------------------- Theme
const THEME = {
  name: "LafroX",
  headFontFace: "Inter SemiBold",
  bodyFontFace: "Inter",
  colors: {
    dk1: "111111", lt1: "FFFFFF", dk2: "141414", lt2: "F4F4F4",
    accent1: "E8641B", accent2: "3C3C3C", accent3: "606060",
    accent4: "F29A5E", accent5: "9A9A9A", accent6: "C7C7C7",
    hlink: "E8641B", folHlink: "F29A5E",
  },
};

const pres = new pptxgen();
pres.defineLayout({ name: "LAFROX", width: 20, height: 11.25 });
pres.layout = "LAFROX";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "LafroX - Plantilla";
pres.author = "LafroX SpA";
pres.company = "LafroX SpA";
pres.subject = "Plantilla de presentacion";

const C = pres.SchemeColor;
const H = "+mj-lt"; // heading font (Inter SemiBold)
const B = "+mn-lt"; // body font (Inter)

// Grid constants (inches)
const X0 = 1.61;
const W = 16.8; // content width
const XR = X0 + W; // 18.41
const Y0 = 3.1; // content top
const YB = 10.2; // content bottom

// ---------------------------------------------------------------- Layouts
const brand = (dark) => [
  { image: { x: 1.61, y: 0.93, w: 0.6, h: 0.62, path: A(dark ? "isotipo-naranjo.png" : "isotipo-negro.png") } },
  {
    text: {
      text: "LafroX SpA",
      options: {
        x: 2.39, y: 1.09, w: 3.64, h: 0.33, fontSize: 18, bold: true, fontFace: H,
        color: dark ? C.background1 : C.text1, margin: 0, valign: "middle", align: "left",
      },
    },
  },
];
const numStyle = (dark) => ({
  x: 18.0, y: 10.5, w: 1.5, h: 0.45, fontFace: H, fontSize: 16, align: "right",
  color: dark ? C.background1 : C.accent3,
});
const contentTitle = (color) => ({
  placeholder: {
    options: {
      name: "title", type: "title", x: 1.61, y: 1.65, w: 16.8, h: 0.95, fontSize: 44, bold: true,
      color, align: "left", valign: "top", margin: 0,
    },
    text: "",
  },
});
const photo = { image: { x: 0, y: 0, w: 20, h: 11.25, path: A("fondo-oscuro.jpeg") } };

pres.defineSlideMaster({
  title: "PORTADA",
  background: { color: C.text1 },
  objects: [
    photo,
    ...brand(true),
    {
      placeholder: {
        options: {
          name: "title", type: "title", x: 1.56, y: 2.76, w: 16.8, h: 3.7, fontSize: 100, bold: true,
          color: C.background1, align: "left", valign: "top", margin: 0,
        },
        text: "",
      },
    },
    {
      placeholder: {
        options: {
          name: "subtitulo", type: "body", x: 1.61, y: 6.74, w: 14, h: 1.2, fontSize: 22,
          color: C.background1, align: "left", valign: "top", margin: 0,
        },
        text: "",
      },
    },
  ],
});

pres.defineSlideMaster({
  title: "SECCION",
  background: { color: C.accent1 },
  objects: [
    ...brand(false),
    {
      placeholder: {
        options: {
          name: "numero", type: "body", x: 1.61, y: 2.4, w: 16.8, h: 4.2, fontSize: 280, bold: true, fontFace: H,
          color: C.background1, align: "left", valign: "top", margin: 0,
        },
        text: "",
      },
    },
    {
      placeholder: {
        options: {
          name: "title", type: "title", x: 1.61, y: 7.0, w: 16.8, h: 1.4, fontSize: 66, bold: true,
          color: C.background1, align: "left", valign: "top", margin: 0,
        },
        text: "",
      },
    },
    {
      placeholder: {
        options: {
          name: "subtitulo", type: "body", x: 1.61, y: 8.7, w: 14, h: 0.9, fontSize: 22,
          color: C.background1, align: "left", valign: "top", margin: 0,
        },
        text: "",
      },
    },
  ],
});

pres.defineSlideMaster({
  title: "CONTENIDO",
  background: { color: C.background1 },
  objects: [...brand(false), contentTitle(C.text1)],
  slideNumber: numStyle(false),
});

pres.defineSlideMaster({
  title: "CONTENIDO_OSCURO",
  background: { color: C.text1 },
  objects: [...brand(true), contentTitle(C.background1)],
  slideNumber: numStyle(true),
});

pres.defineSlideMaster({
  title: "CIERRE",
  background: { color: C.text1 },
  objects: [
    photo,
    ...brand(true),
    {
      placeholder: {
        options: {
          name: "mensaje", type: "title", x: 1.61, y: 2.9, w: 16.8, h: 3.2, fontSize: 150, bold: true,
          color: C.accent1, align: "center", valign: "middle", margin: 0,
        },
        text: "",
      },
    },
    {
      placeholder: {
        options: {
          name: "subtitulo", type: "body", x: 1.61, y: 6.4, w: 16.8, h: 0.7, fontSize: 24, fontFace: "Inter Light",
          color: C.background1, align: "center", valign: "top", margin: 0,
        },
        text: "",
      },
    },
  ],
});

// ---------------------------------------------------------------- Helpers
let nameN = 0;
const T = (s, text, x, y, w, h, o = {}) =>
  s.addText(text, {
    x, y, w, h, margin: 0, isTextBox: true, valign: "top", fontSize: 18, color: C.text1,
    objectName: `Texto ${++nameN}`, ...o,
  });

const card = (s, x, y, w, h, o = {}) =>
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h, rectRadius: 0.15, fill: { color: C.background1 }, line: { color: C.accent6, width: 1 },
    objectName: `Tarjeta ${++nameN}`, ...o,
  });

const darkCard = (s, x, y, w, h) =>
  card(s, x, y, w, h, { fill: { color: C.text1 }, line: { color: C.text1, width: 1 } });

const pill = (s, text, x, y, w, h, o = {}) =>
  s.addText(text, {
    shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: h / 2, x, y, w, h, fill: { color: C.background2 },
    color: C.text1, fontSize: 16, align: "center", valign: "middle", margin: 0,
    objectName: `Pildora ${++nameN}`, ...o,
  });

const circle = (s, text, x, y, d = 0.9) =>
  s.addText(text, {
    shape: pres.shapes.OVAL, x, y, w: d, h: d, fill: { color: C.accent1 }, color: C.background1, bold: true,
    fontSize: 17, fontFace: H, align: "center", valign: "middle", margin: 0, objectName: `Circulo ${++nameN}`,
  });

const source = (s, text, y = 9.85, dark = false) =>
  T(s, text, X0, y, 14, 0.3, { fontSize: 13, color: dark ? C.accent5 : C.accent3 });

const caption = (s, text) => T(s, text, X0, Y0, W, 0.4, { fontSize: 16, color: C.accent3 });

const lineOpt = (color, w = 0.5) => ({ color, width: w });

let sec = null;
const slide = (layout, section, notes) => {
  const s = pres.addSlide({ masterName: layout, sectionTitle: section });
  s.addNotes(notes);
  return s;
};
const title = (s, t) => s.addText(t, { placeholder: "title" });

// Charts: identical axis / label styling everywhere. Hex literals (hex-only options).
const chartBase = () => ({
  catAxisLabelColor: "606060", catAxisLabelFontSize: 14, catAxisLabelFontFace: B,
  valAxisLabelColor: "606060", valAxisLabelFontSize: 14, valAxisLabelFontFace: B,
  valGridLine: { color: "C7C7C7", size: 0.5 }, catGridLine: { style: "none" },
  catAxisLineShow: true, valAxisLineShow: false,
  showValue: true, dataLabelFontSize: 14, dataLabelFontFace: B, dataLabelColor: "111111",
  legendFontFace: B, legendFontSize: 14, legendColor: "606060",
  showTitle: false, showLegend: false,
});

// ---------------------------------------------------------------- Sections
["Apertura", "Contenido", "Tablas", "Gráficos", "Diagramas", "Cierre", "Guía"].forEach((t) => pres.addSection({ title: t }));

// 1 Portada
{
  const s = slide(
    "PORTADA", "Apertura",
    "Portada. Sirve para abrir cualquier presentación de LafroX: cambie el título (dos líneas: la primera en peso regular, la segunda en negrita), el subtítulo y la línea inferior. Se edita directamente en los marcadores de la lámina. Los datos de esta lámina son de Ejemplo."
  );
  s.addText(
    [
      { text: "Propuesta", options: { bold: false, fontFace: B, breakLine: true } },
      { text: "Técnica", options: { bold: true } },
    ],
    { placeholder: "title" }
  );
  s.addText("Distribuidora Puelche · Licitación TFEP-01/2026", { placeholder: "subtitulo" });
  T(s, "Ejemplo · Noviembre de 2026", 1.61, 9.9, 10, 0.4, { fontSize: 18, color: C.accent6 });
}

// 2 Agenda
{
  const s = slide(
    "CONTENIDO", "Apertura",
    "Agenda numerada en dos columnas, seis ítems. Úsela después de la portada para anticipar la estructura. Para cambiar la cantidad de ítems, duplique o elimine tarjetas y mantenga el ritmo de 0,3 in entre ellas. Los textos son de Ejemplo."
  );
  title(s, "Agenda");
  const items = [
    ["01", "Contexto y problema", "Qué ocurre hoy en la operación"],
    ["02", "Diagnóstico de calidad", "Indicadores y causas principales"],
    ["03", "Propuesta de solución", "Proceso rediseñado de punta a punta"],
    ["04", "Plan de implementación", "Etapas, hitos y responsables"],
    ["05", "Costos y beneficios", "Inversión mensual y ahorro esperado"],
    ["06", "Riesgos y próximos pasos", "Qué vigilar y cómo avanzar"],
  ];
  const cw = 8.25, ch = 1.9;
  items.forEach((it, i) => {
    const col = i < 3 ? 0 : 1, row = i % 3;
    const x = X0 + col * (cw + 0.3), y = Y0 + row * (ch + 0.3);
    card(s, x, y, cw, ch);
    T(s, it[0], x + 0.4, y, 1.0, ch, { fontSize: 32, bold: true, fontFace: H, color: C.accent1, valign: "middle" });
    T(s, it[1], x + 1.7, y + 0.42, cw - 2.0, 0.5, { fontSize: 24, bold: true, fontFace: H });
    T(s, it[2], x + 1.7, y + 1.0, cw - 2.0, 0.4, { fontSize: 16, color: C.accent3 });
  });
}

// 3 Divisor de seccion
{
  const s = slide(
    "SECCION", "Apertura",
    "Divisor de sección sobre fondo naranjo. Complete el número (por ejemplo 02), el nombre de la sección y una frase de contexto. Úselo entre bloques temáticos de la presentación. Contenido de Ejemplo."
  );
  s.addText("02", { placeholder: "numero" });
  s.addText("Diagnóstico de calidad", { placeholder: "title" });
  s.addText("Qué ocurre hoy en la operación de Distribuidora Puelche", { placeholder: "subtitulo" });
}

// 4 Equipo
{
  const s = slide(
    "CONTENIDO", "Contenido",
    "Equipo de trabajo: tarjeta oscura de encabezado a la izquierda y cuadrícula de 2x3 tarjetas de persona con iniciales. Reemplace nombres, cargos e iniciales. Para más personas, agregue filas manteniendo el alto de tarjeta. Nombres de Ejemplo."
  );
  title(s, "Equipo de trabajo");
  const gh = 7.0;
  darkCard(s, X0, Y0, 5.4, gh);
  T(s, "EQUIPO", X0 + 0.5, Y0 + 0.5, 4.4, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent4 });
  T(s, "Seis roles, un solo objetivo", X0 + 0.5, Y0 + 1.1, 4.4, 2.4, { fontSize: 36, bold: true, fontFace: H, color: C.background1 });
  T(s, "Cada rol responde por una etapa del proceso y por sus indicadores de calidad.", X0 + 0.5, Y0 + 4.3, 4.4, 2.0, { fontSize: 18, color: C.accent6 });
  const ppl = [
    ["CR", "Camila Rojas", "Gerencia de proyecto"],
    ["MS", "Matías Soto", "Operaciones"],
    ["VP", "Valentina Pino", "Calidad"],
    ["JR", "Joaquín Reyes", "Logística"],
    ["FM", "Francisca Muñoz", "Finanzas"],
    ["TA", "Tomás Araya", "Datos y reportes"],
  ];
  const gx = X0 + 5.4 + 0.3, pw = (XR - gx - 0.3) / 2, ph = (gh - 0.6) / 3;
  ppl.forEach((p, i) => {
    const x = gx + (i % 2) * (pw + 0.3), y = Y0 + Math.floor(i / 2) * (ph + 0.3);
    card(s, x, y, pw, ph);
    circle(s, p[0], x + 0.4, y + (ph - 0.9) / 2);
    T(s, p[1], x + 1.6, y + ph / 2 - 0.45, pw - 1.8, 0.45, { fontSize: 20, bold: true, fontFace: H });
    T(s, p[2], x + 1.6, y + ph / 2 + 0.05, pw - 1.8, 0.4, { fontSize: 16, color: C.accent3 });
  });
}

// 5 KPIs (oscura)
{
  const s = slide(
    "CONTENIDO_OSCURO", "Contenido",
    "KPIs grandes sobre fondo oscuro: cuatro cifras con su etiqueta y un contexto. Cambie la cifra (naranjo), la unidad y la etiqueta. Use la tarjeta inferior para la meta o la conclusión. Todas las cifras son de Ejemplo."
  );
  title(s, "Situación actual en cuatro cifras");
  const k = [
    ["82,4", " %", "OTIF actual", "Entregas a tiempo y completas"],
    ["9", " días", "Plazo de retiro", "Promedio de la carga en origen"],
    ["4.800", " kg", "Carga por retiro", "Volumen medio por ciclo"],
    ["4,2", " %", "Reentregas", "Despachos que se repiten"],
  ];
  const kw = (W - 3 * 0.5) / 4, kh = 4.5;
  k.forEach((d, i) => {
    const x = X0 + i * (kw + 0.5);
    card(s, x, Y0, kw, kh, { fill: { color: C.text1 }, line: { color: C.accent2, width: 1 } });
    T(s, [
      { text: d[0], options: { fontSize: 56, bold: true, fontFace: H, color: C.accent1 } },
      { text: d[1], options: { fontSize: 26, bold: true, fontFace: H, color: C.accent1 } },
    ], x + 0.4, Y0 + 0.6, kw - 0.6, 1.4, { valign: "middle" });
    T(s, d[2], x + 0.4, Y0 + 2.4, kw - 0.6, 0.45, { fontSize: 20, bold: true, fontFace: H, color: C.background1 });
    T(s, d[3], x + 0.4, Y0 + 3.0, kw - 0.6, 0.9, { fontSize: 16, color: C.accent5 });
  });
  const y2 = Y0 + kh + 0.3;
  card(s, X0, y2, W, 1.5, { fill: { color: C.accent2 }, line: { color: C.accent2, width: 1 } });
  T(s, "META DE LA LICITACIÓN", X0 + 0.5, y2 + 0.25, 8, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent4 });
  T(s, "OTIF mayor o igual a 95 % y reentregas menores o iguales a 2 %", X0 + 0.5, y2 + 0.72, W - 1.0, 0.5, { fontSize: 24, color: C.background1 });
  source(s, "Fuente: Ejemplo, datos ilustrativos Distribuidora Puelche, 2026.", 9.95, true);
}

// 6 Problemas + causa raiz
{
  const s = slide(
    "CONTENIDO", "Contenido",
    "Tres tarjetas de problema y una tarjeta oscura con la causa raíz. Úsela para pasar del síntoma al origen. Cambie numeración, títulos y descripciones; mantenga un máximo de cuatro líneas por tarjeta. Datos de Ejemplo."
  );
  title(s, "Tres síntomas, una causa raíz");
  const p = [
    ["01", "Retiros demorados", "La carga espera 9 días en promedio, frente a los 3 días comprometidos en la licitación."],
    ["02", "Entregas fuera de plazo", "El OTIF es 82,4 %, es decir 12,6 puntos bajo la meta de 95 %."],
    ["03", "Reentregas costosas", "El 4,2 % de los despachos se repite y duplica transporte y bodega."],
  ];
  const cw = (W - 0.6) / 3;
  p.forEach((d, i) => {
    const x = X0 + i * (cw + 0.3);
    card(s, x, Y0, cw, 3.7);
    T(s, d[0], x + 0.4, Y0 + 0.4, 1.5, 0.35, { fontSize: 18, bold: true, fontFace: H, color: C.accent1 });
    T(s, d[1], x + 0.4, Y0 + 1.0, cw - 0.8, 0.5, { fontSize: 24, bold: true, fontFace: H });
    T(s, d[2], x + 0.4, Y0 + 1.7, cw - 0.8, 2.3, { fontSize: 18, color: C.accent3 });
  });
  const y2 = Y0 + 3.7 + 0.3;
  darkCard(s, X0, y2, W, 2.5);
  T(s, "CAUSA RAÍZ", X0 + 0.5, y2 + 0.4, 6, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent4 });
  T(s, "No existe un proceso único de preparación y verificación de pedidos: cada bodega lo resuelve a su manera.", X0 + 0.5, y2 + 1.0, W - 1.0, 1.2, { fontSize: 28, color: C.background1 });
}

// ---- table helpers
const th = (t, align = "left") => ({
  text: t, options: { bold: true, color: C.background1, fill: { color: C.accent1 }, align, valign: "middle", fontSize: 18 },
});
const td = (t, i, o = {}) => ({
  text: t,
  options: { color: C.text1, fill: { color: i % 2 === 0 ? C.background1 : C.background2 }, valign: "middle", fontSize: 18, ...o },
});
const tblBorder = () => ({ type: "solid", pt: 0.5, color: "C7C7C7" });

// 7 Tabla estandar
{
  const s = slide(
    "CONTENIDO", "Tablas",
    "Tabla estándar: encabezado naranjo, filas alternadas, columnas numéricas alineadas a la derecha, fila de total en negrita y nota de fuente debajo. Para más filas, agregue filas manteniendo el alto de 0,7 in. Datos de Ejemplo."
  );
  title(s, "Costo mensual de no calidad por etapa");
  const rows = [
    ["Recepción", "Operaciones", "38", "620.000"],
    ["Preparación", "Bodega", "64", "950.000"],
    ["Despacho", "Logística", "82", "1.180.000"],
    ["Reentregas", "Calidad", "51", "880.000"],
    ["Administración", "Finanzas", "30", "570.000"],
  ];
  const data = [[th("Etapa"), th("Responsable"), th("Horas al mes", "right"), th("Costo (CLP)", "right")]];
  rows.forEach((r, i) => data.push([td(r[0], i), td(r[1], i), td(r[2], i, { align: "right" }), td(r[3], i, { align: "right" })]));
  const t = 5;
  data.push([
    td("Total", t, { bold: true }), td("", t, { bold: true }), td("265", t, { bold: true, align: "right" }),
    td("4.200.000", t, { bold: true, align: "right" }),
  ]);
  s.addTable(data, {
    x: X0, y: Y0, w: W, colW: [6.8, 4.4, 2.6, 3.0], rowH: 0.75, border: tblBorder(), margin: [0.05, 0.25, 0.05, 0.25],
    objectName: "Tabla de costos",
  });
  source(s, "Fuente: Ejemplo, estimación interna a partir de datos ilustrativos de Distribuidora Puelche (CLP, $4,2 M/mes).", 8.7);
}

// 8 Tabla comparativa antes / despues
{
  const s = slide(
    "CONTENIDO", "Tablas",
    "Tabla comparativa antes/después con marcas de estado en forma de píldora (✓ cumple, ✗ pendiente). Las píldoras son formas posicionadas sobre la columna Estado: si cambia el alto de las filas, muévalas con ellas. Datos de Ejemplo."
  );
  title(s, "Antes y después de la propuesta");
  const rows = [
    ["OTIF mensual", "82,4 %", "96,0 %", true],
    ["Plazo de retiro", "9 días", "3 días", true],
    ["Reentregas", "4,2 %", "1,8 %", true],
    ["Costo no calidad", "$4,2 M/mes", "$3,1 M/mes", true],
    ["Trazabilidad por lote", "Parcial", "Completa", true],
    ["Reportes automáticos", "No", "Por implementar", false],
  ];
  const hdr = 0.7, rh = 0.8;
  const data = [[th("Indicador"), th("Antes", "right"), th("Después", "right"), th("Estado", "center")]];
  rows.forEach((r, i) => data.push([td(r[0], i), td(r[1], i, { align: "right" }), td(r[2], i, { align: "right", bold: true }), td("", i)]));
  s.addTable(data, {
    x: X0, y: Y0, w: W, colW: [6.0, 3.2, 3.2, 4.4], rowH: [hdr, ...rows.map(() => rh)], border: tblBorder(),
    margin: [0.05, 0.25, 0.05, 0.25], objectName: "Tabla antes y después",
  });
  rows.forEach((r, i) => {
    const px = X0 + 6.0 + 3.2 + 3.2 + (4.4 - 2.8) / 2, py = Y0 + hdr + i * rh + (rh - 0.5) / 2;
    pill(s, r[3] ? "✓  Cumple" : "✗  Pendiente", px, py, 2.8, 0.5, {
      fill: { color: r[3] ? C.accent1 : C.accent2 }, color: C.background1, bold: true, fontSize: 16,
    });
  });
  source(s, "Fuente: Ejemplo, valores objetivo de la propuesta técnica TFEP-01/2026 (datos ilustrativos).", Y0 + hdr + 6 * rh + 0.3);
}

// 9 Barras horizontal
{
  const s = slide(
    "CONTENIDO", "Gráficos",
    "Gráfico de barras horizontal de una serie con una barra destacada en naranjo y un recuadro de comentario a la derecha. Edite los datos desde PowerPoint (Editar datos). Datos de Ejemplo."
  );
  title(s, "Una causa explica un tercio de las reentregas");
  caption(s, "Reentregas por motivo, número de casos, enero a junio de 2026");
  const labels = ["Otros", "Error de documento", "Producto dañado", "Pedido incompleto", "Cliente ausente", "Dirección incompleta"];
  const values = [6, 9, 14, 21, 27, 38];
  s.addChart(pres.charts.BAR, [{ name: "Casos", labels, values }], {
    ...chartBase(), x: X0, y: 3.6, w: 10.9, h: 6.1, barDir: "bar", barGapWidthPct: 45,
    chartColors: ["C7C7C7", "C7C7C7", "C7C7C7", "C7C7C7", "C7C7C7", "E8641B"],
    dataLabelPosition: "outEnd", dataLabelFormatCode: "0", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 45,
  });
  const cx = 12.8, cw = XR - cx;
  darkCard(s, cx, 3.6, cw, 6.1);
  T(s, "LECTURA", cx + 0.45, 4.05, cw - 0.9, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent4 });
  T(s, "33,0 %", cx + 0.45, 4.6, cw - 0.9, 1.3, { fontSize: 66, bold: true, fontFace: H, color: C.accent1 });
  T(s, "de las reentregas se origina en direcciones incompletas.", cx + 0.45, 6.1, cw - 0.9, 1.3, { fontSize: 20, color: C.background1 });
  T(s, "Validar la dirección al ingresar el pedido atacaría la causa más frecuente.", cx + 0.45, 7.8, cw - 0.9, 1.5, { fontSize: 16, color: C.accent6 });
  source(s, "Fuente: Ejemplo, registro ilustrativo de reentregas (n = 115).");
}

// 10 Columnas apiladas
{
  const s = slide(
    "CONTENIDO", "Gráficos",
    "Columnas apiladas: esfuerzo mensual por rol. La primera serie va en naranjo (la que se quiere destacar) y las demás en neutros. En gráficos apilados las etiquetas solo pueden ir al centro o dentro de la barra. Datos de Ejemplo."
  );
  title(s, "Esfuerzo por mes y por rol");
  caption(s, "Horas de trabajo por mes, enero a junio de 2026");
  const labels = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"];
  s.addChart(pres.charts.BAR, [
    { name: "Operaciones", labels, values: [120, 140, 150, 130, 110, 100] },
    { name: "Calidad", labels, values: [40, 60, 70, 80, 70, 60] },
    { name: "TI", labels, values: [30, 80, 90, 60, 40, 30] },
    { name: "Gestión", labels, values: [30, 30, 40, 40, 30, 30] },
  ], {
    ...chartBase(), x: X0, y: 3.6, w: W, h: 6.1, barDir: "col", barGrouping: "stacked", barGapWidthPct: 50,
    chartColors: ["E8641B", "F29A5E", "9A9A9A", "C7C7C7"], dataLabelPosition: "ctr", dataLabelFormatCode: "0",
    showLegend: true, legendPos: "b",
  });
  source(s, "Fuente: Ejemplo, horas ilustrativas registradas por el equipo.");
}

// 11 Lineas
{
  const s = slide(
    "CONTENIDO", "Gráficos",
    "Gráfico de líneas: indicador real frente a una meta, con recuadro de lectura a la derecha. La serie principal va en naranjo y la meta en gris oscuro. Edite los datos desde PowerPoint. Datos de Ejemplo."
  );
  title(s, "OTIF mensual frente a la meta");
  caption(s, "OTIF mensual, porcentaje de entregas a tiempo y completas, 2026");
  const labels = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"];
  s.addChart(pres.charts.LINE, [
    { name: "OTIF real", labels, values: [79.2, 80.1, 81.0, 80.6, 82.0, 82.4] },
    { name: "Meta", labels, values: [95, 95, 95, 95, 95, 95] },
  ], {
    ...chartBase(), x: X0, y: 3.6, w: 11.4, h: 6.1, chartColors: ["E8641B", "3C3C3C"], lineSize: 3,
    lineDataSymbolSize: 9, dataLabelPosition: "t", dataLabelFormatCode: '0.0" %"', valAxisMinVal: 70, valAxisMaxVal: 100,
    valAxisMajorUnit: 10, valAxisLabelFormatCode: '0" %"', showLegend: true, legendPos: "b",
  });
  const cx = 13.3, cw = XR - cx;
  darkCard(s, cx, 3.6, cw, 6.1);
  T(s, "BRECHA A JUNIO", cx + 0.45, 4.05, cw - 0.9, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent4 });
  T(s, "12,6 pp", cx + 0.45, 4.6, cw - 0.9, 1.3, { fontSize: 66, bold: true, fontFace: H, color: C.accent1 });
  T(s, "entre el OTIF de 82,4 % y la meta de 95 %.", cx + 0.45, 6.1, cw - 0.9, 1.3, { fontSize: 20, color: C.background1 });
  T(s, "La mejora es sostenida, pero lenta: cerca de 0,7 pp por mes.", cx + 0.45, 7.8, cw - 0.9, 1.5, { fontSize: 16, color: C.accent6 });
  source(s, "Fuente: Ejemplo, datos ilustrativos Distribuidora Puelche.");
}

// 12 Dona
{
  const s = slide(
    "CONTENIDO", "Gráficos",
    "Dona con total en el centro y leyenda propia a la derecha. El texto central es un cuadro de texto aparte: actualícelo cuando cambie el total. Datos de Ejemplo."
  );
  title(s, "Dónde se concentra el costo de no calidad");
  caption(s, "Distribución del costo mensual de no calidad, porcentaje del total");
  const cols = ["E8641B", "F29A5E", "9A9A9A", "C7C7C7"];
  const names = ["Reentregas", "Mermas y daños", "Penalizaciones", "Reclamos"];
  const vals = [38, 27, 21, 14];
  const dx = X0, dy = 3.6, dw = 7.2, dh = 6.1;
  s.addChart(pres.charts.DOUGHNUT, [{ name: "Costo", labels: names, values: vals }], {
    ...chartBase(), x: dx, y: dy, w: dw, h: dh, chartColors: cols, holeSize: 62, showPercent: true, showValue: false,
    dataLabelFormatCode: "0%", dataLabelColor: "111111", showLegend: false,
  });
  T(s, "$4,2 M", dx + dw / 2 - 1.6, dy + dh / 2 - 0.55, 3.2, 0.7, { fontSize: 44, bold: true, fontFace: H, align: "center", valign: "middle" });
  T(s, "por mes", dx + dw / 2 - 1.6, dy + dh / 2 + 0.2, 3.2, 0.4, { fontSize: 16, color: C.accent3, align: "center" });
  const lx = 10.3, lw = XR - lx, rh = 1.3;
  names.forEach((n, i) => {
    const y = 3.9 + i * (rh + 0.3);
    card(s, lx, y, lw, rh);
    s.addShape(pres.shapes.OVAL, { x: lx + 0.4, y: y + rh / 2 - 0.2, w: 0.4, h: 0.4, fill: { color: cols[i] }, line: { color: "C7C7C7", width: 1 }, objectName: `Marca ${i + 1}` });
    T(s, n, lx + 1.2, y, 4.5, rh, { fontSize: 20, bold: true, fontFace: H, valign: "middle" });
    T(s, `${vals[i]} %`, lx + lw - 2.6, y, 2.2, rh, { fontSize: 28, bold: true, fontFace: H, align: "right", valign: "middle" });
  });
  source(s, "Fuente: Ejemplo, estimación ilustrativa (total $4,2 M/mes).");
}

// 13 Combo Pareto
{
  const s = slide(
    "CONTENIDO", "Gráficos",
    "Gráfico combinado de Pareto: columnas con la frecuencia y línea con el porcentaje acumulado en eje secundario. Las tres primeras causas (naranjo) concentran el 74,8 %. Datos de Ejemplo."
  );
  title(s, "Tres causas concentran el 75 % de los casos");
  caption(s, "Reentregas por motivo (casos) y porcentaje acumulado");
  const labels = ["Dirección incompleta", "Cliente ausente", "Pedido incompleto", "Producto dañado", "Error de documento", "Otros"];
  const base = chartBase();
  const axisCat = { catAxisLabelColor: "606060", catAxisLabelFontSize: 14, catAxisLabelFontFace: B, catGridLine: { style: "none" } };
  s.addChart([
    {
      type: pres.charts.BAR,
      data: [{ name: "Casos", labels, values: [38, 27, 21, 14, 9, 6] }],
      options: { barDir: "col", barGapWidthPct: 40, chartColors: ["E8641B", "E8641B", "E8641B", "C7C7C7", "C7C7C7", "C7C7C7"] },
    },
    {
      type: pres.charts.LINE,
      data: [{ name: "% acumulado", labels, values: [33.0, 56.5, 74.8, 87.0, 94.8, 100.0] }],
      options: { chartColors: ["111111"], secondaryValAxis: true, secondaryCatAxis: true, lineSize: 3, lineDataSymbolSize: 9 },
    },
  ], {
    ...base, x: X0, y: 3.6, w: W, h: 6.1, showLegend: true, legendPos: "b", dataLabelPosition: "outEnd", dataLabelFormatCode: "0",
    valAxes: [
      { ...{ valAxisLabelColor: "606060", valAxisLabelFontSize: 14, valAxisLabelFontFace: B, valGridLine: { color: "C7C7C7", size: 0.5 }, valAxisLineShow: false }, valAxisMinVal: 0, valAxisMaxVal: 40 },
      { valAxisLabelColor: "606060", valAxisLabelFontSize: 14, valAxisLabelFontFace: B, valGridLine: { style: "none" }, valAxisLineShow: false, valAxisMinVal: 0, valAxisMaxVal: 100, valAxisLabelFormatCode: '0" %"' },
    ],
    catAxes: [axisCat, { ...axisCat, catAxisHidden: true }],
  });
  source(s, "Fuente: Ejemplo, registro ilustrativo de reentregas (n = 115).");
}

// 14 Gantt
{
  const s = slide(
    "CONTENIDO", "Diagramas",
    "Línea de tiempo simplificada (Gantt) con barras por etapa e hitos en rombos. Mueva y estire las barras para ajustar fechas; cada columna es un mes. Etapas y fechas de Ejemplo."
  );
  title(s, "Plan de implementación en seis meses");
  const lw = 3.8, gx = X0 + lw, gw = XR - gx, cw = gw / 6;
  const months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"];
  const hy = Y0, hh = 0.6, ry = hy + hh + 0.2, rs = 0.95, bh = 0.55;
  months.forEach((m, i) => {
    T(s, m, gx + i * cw, hy, cw, hh, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, align: "center", valign: "middle" });
  });
  for (let i = 0; i <= 6; i++) {
    s.addShape(pres.shapes.LINE, { x: gx + i * cw, y: hy, w: 0, h: 6.05, line: lineOpt("C7C7C7", 0.5), objectName: `Guia ${i}` });
  }
  const st = [
    ["Diagnóstico", 0, 1.5, "6 semanas"],
    ["Diseño del proceso", 1, 2.5, "6 semanas"],
    ["Piloto en una bodega", 2.5, 4, "6 semanas"],
    ["Implementación", 3.5, 5.5, "8 semanas"],
    ["Control y cierre", 5, 6, "4 semanas"],
  ];
  st.forEach((e, i) => {
    const y = ry + i * rs;
    T(s, e[0], X0, y, lw - 0.3, bh, { fontSize: 18, bold: true, fontFace: H, valign: "middle" });
    s.addText(e[3], {
      shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.15, x: gx + e[1] * cw + 0.05, y, w: (e[2] - e[1]) * cw - 0.1, h: bh,
      fill: { color: C.accent1 }, color: C.background1, bold: true, fontSize: 14, align: "center", valign: "middle", margin: 0,
      objectName: `Barra ${i + 1}`,
    });
  });
  const my = ry + 5 * rs + 0.1;
  T(s, "Hitos", X0, my, lw - 0.3, 0.4, { fontSize: 18, bold: true, fontFace: H, valign: "middle" });
  [[1.5, "Informe de diagnóstico"], [4, "Piloto aprobado"], [5.85, "Cierre"]].forEach((m, i) => {
    const cx = gx + m[0] * cw;
    s.addShape(pres.shapes.DIAMOND, { x: cx - 0.2, y: my, w: 0.4, h: 0.4, fill: { color: C.text1 }, objectName: `Hito ${i + 1}` });
    const w = 3.2, x = Math.min(cx - w / 2, XR - w);
    T(s, m[1], x, my + 0.5, w, 0.35, { fontSize: 14, color: C.accent3, align: i === 2 ? "right" : "center" });
  });
}

// 15 Proceso en pasos
{
  const s = slide(
    "CONTENIDO", "Diagramas",
    "Proceso en cinco pasos con flechas. Cada paso tiene círculo numerado, título y descripción corta. Para cuatro o seis pasos, redistribuya el ancho manteniendo 0,5 in entre tarjetas. Contenido de Ejemplo."
  );
  title(s, "Proceso de despacho en cinco pasos");
  const steps = [
    ["Recepción", "Se registra la orden y se valida la información."],
    ["Verificación", "Se revisa la carga contra la guía de despacho."],
    ["Preparación", "Se arma el pedido y se etiqueta por lote."],
    ["Despacho", "Se asigna ruta y se retira la carga."],
    ["Confirmación", "El cliente confirma la entrega en línea."],
  ];
  const gap = 0.5, cw = (W - 4 * gap) / 5, ch = 4.2;
  steps.forEach((d, i) => {
    const x = X0 + i * (cw + gap);
    card(s, x, Y0, cw, ch);
    circle(s, String(i + 1).padStart(2, "0"), x + 0.4, Y0 + 0.45);
    T(s, d[0], x + 0.4, Y0 + 1.7, cw - 0.8, 0.5, { fontSize: 22, bold: true, fontFace: H });
    T(s, d[1], x + 0.4, Y0 + 2.4, cw - 0.8, 1.9, { fontSize: 16, color: C.accent3 });
    if (i < 4) {
      s.addShape(pres.shapes.RIGHT_ARROW, { x: x + cw + (gap - 0.36) / 2, y: Y0 + ch / 2 - 0.18, w: 0.36, h: 0.36, fill: { color: C.accent1 }, objectName: `Flecha ${i + 1}` });
    }
  });
  const y2 = Y0 + ch + 0.3;
  darkCard(s, X0, y2, W, 1.9);
  T(s, "RESULTADO ESPERADO", X0 + 0.5, y2 + 0.4, 8, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent4 });
  T(s, "Retiro en 3 días y OTIF sobre 95 % en todas las bodegas.", X0 + 0.5, y2 + 0.95, W - 1.0, 0.6, { fontSize: 24, color: C.background1 });
}

// 16 Dos columnas texto + imagen
{
  const s = slide(
    "CONTENIDO", "Diagramas",
    "Dos columnas: texto a la izquierda y un recuadro gris para imagen o diagrama a la derecha. Borre el recuadro e inserte su imagen con el mismo tamaño y esquinas redondeadas. Texto de Ejemplo."
  );
  title(s, "Propuesta para la bodega central");
  T(s, "Un flujo único de principio a fin", X0, Y0, 7.6, 1.2, { fontSize: 28, bold: true, fontFace: H });
  T(s, [
    { text: "Zonas separadas para recepción, preparación y despacho.", options: { bullet: true, breakLine: true } },
    { text: "Un solo registro por pedido, con trazabilidad por lote.", options: { bullet: true, breakLine: true } },
    { text: "Verificación de la carga antes de cada retiro de 4.800 kg.", options: { bullet: true } },
  ], X0, Y0 + 1.6, 7.6, 4.5, { fontSize: 20, paraSpaceAfter: 14 });
  const ix = 9.9;
  s.addText([
    { text: "Imagen o diagrama", options: { breakLine: true, fontSize: 24, bold: true, fontFace: H } },
    { text: "Proporción sugerida 5:6", options: { fontSize: 16 } },
  ], {
    shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.15, x: ix, y: Y0, w: XR - ix, h: 6.9, fill: { color: C.background2 },
    color: C.accent3, align: "center", valign: "middle", margin: 0, objectName: "Marcador de imagen",
  });
}

// 17 Matriz 2x2 riesgos
{
  const s = slide(
    "CONTENIDO", "Diagramas",
    "Matriz 2x2 de riesgos (probabilidad por impacto). Ubique cada riesgo como píldora dentro del cuadrante que corresponda; el cuadrante crítico va en tarjeta oscura. Riesgos de Ejemplo."
  );
  title(s, "Matriz de riesgos");
  const gx = 2.9, gy = Y0, qw = (XR - gx - 0.3) / 2, qh = 2.9;
  const quad = [
    // col,row, label, sub, risks, dark
    [0, 0, "Vigilar", "Impacto alto, probabilidad baja", ["R3 Cambio de bases"], false],
    [1, 0, "Crítico", "Impacto alto, probabilidad alta", ["R1 Falta de conductores", "R2 Rechazo de entregas"], true],
    [0, 1, "Aceptar", "Impacto bajo, probabilidad baja", ["R6 Rotación de personal"], false],
    [1, 1, "Mitigar", "Impacto bajo, probabilidad alta", ["R4 Quiebre de stock", "R5 Datos incompletos"], false],
  ];
  quad.forEach((q) => {
    const x = gx + q[0] * (qw + 0.3), y = gy + q[1] * (qh + 0.3);
    if (q[5]) darkCard(s, x, y, qw, qh); else card(s, x, y, qw, qh);
    T(s, q[2], x + 0.4, y + 0.3, qw - 0.8, 0.5, { fontSize: 24, bold: true, fontFace: H, color: q[5] ? C.background1 : C.text1 });
    T(s, q[3], x + 0.4, y + 0.85, qw - 0.8, 0.35, { fontSize: 16, color: q[5] ? C.accent6 : C.accent3 });
    q[4].forEach((r, i) => {
      pill(s, r, x + 0.4, y + 1.45 + i * 0.65, 4.6, 0.5, q[5] ? { fill: { color: C.accent1 }, color: C.background1, bold: true } : {});
    });
  });
  T(s, "IMPACTO", X0 - 2.45 + 0.5 - 0.05, gy + (qh * 2 + 0.3) / 2 - 0.2, 5.0, 0.4, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, align: "center", valign: "middle", rotate: 270 });
  T(s, "PROBABILIDAD", gx, gy + qh * 2 + 0.3 + 0.25, XR - gx, 0.4, { fontSize: 16, bold: true, fontFace: H, color: C.accent3, align: "center" });
}

// 18 Cita
{
  const s = slide(
    "CONTENIDO", "Cierre",
    "Cita o mensaje clave a pantalla completa. Úsela para dejar una idea central antes del cierre: reemplace el texto y la atribución. Mensaje de Ejemplo."
  );
  title(s, "Mensaje clave");
  T(s, "“", X0, Y0 - 0.1, 3, 2.2, { fontSize: 200, bold: true, fontFace: H, color: C.accent1 });
  T(s, "La calidad del servicio se gana en cada entrega, no en cada informe.", X0, Y0 + 2.2, W, 3.6, { fontSize: 54, bold: true, fontFace: H });
  T(s, "Equipo LafroX · Propuesta técnica, Distribuidora Puelche", X0, Y0 + 6.0, W, 0.5, { fontSize: 20, color: C.accent3 });
}

// 19 Cierre
{
  const s = slide(
    "CIERRE", "Cierre",
    "Lámina de cierre y preguntas sobre fondo oscuro. Cambie el mensaje grande (naranjo), el subtítulo y los datos de contacto, que aquí son de Ejemplo."
  );
  s.addText("¿Preguntas?", { placeholder: "mensaje" });
  s.addText("Gracias por su atención", { placeholder: "subtitulo" });
  T(s, "contacto@lafrox.cl  ·  +56 9 1234 5678", X0, 8.0, W, 0.5, { fontSize: 20, color: C.background1, align: "center" });
  T(s, "lafrox.cl  ·  Santiago, Chile", X0, 8.6, W, 0.5, { fontSize: 20, color: C.accent6, align: "center" });
}

// 20 Guia de estilo
{
  const s = slide(
    "CONTENIDO", "Guía",
    "Guía de estilo de la plantilla: paleta con códigos HEX, escala tipográfica y reglas de uso. Consúltela antes de crear láminas nuevas. Esta lámina es referencia, no se presenta."
  );
  title(s, "Guía de estilo");
  const pal = [
    ["Negro", "111111"], ["Carbón", "141414"], ["Grafito", "3C3C3C"], ["Gris oscuro", "606060"], ["Gris", "9A9A9A"],
    ["Gris claro", "C7C7C7"], ["Humo", "F4F4F4"], ["Blanco", "FFFFFF"], ["Naranjo", "E8641B"], ["Durazno", "F29A5E"],
  ];
  const sw = (W - 9 * 0.3) / 10;
  pal.forEach((p, i) => {
    const x = X0 + i * (sw + 0.3);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: Y0, w: sw, h: 1.1, rectRadius: 0.15, fill: { color: p[1] }, line: { color: "C7C7C7", width: 1 }, objectName: `Muestra ${p[0]}` });
    T(s, p[0], x, Y0 + 1.25, sw, 0.3, { fontSize: 14, bold: true, fontFace: H });
    T(s, "#" + p[1], x, Y0 + 1.58, sw, 0.3, { fontSize: 14, color: C.accent3 });
  });
  const ty = 5.4, lw = 10.2;
  const sc = [
    ["Título principal", 44, true, "Inter SemiBold · 44 pt", 0.9],
    ["Subtítulo de lámina", 28, true, "Inter SemiBold · 28 pt", 0.7],
    ["Cuerpo de texto para explicar", 18, false, "Inter Regular · 18 pt", 0.6],
    ["Nota de fuente o pie de gráfico", 13, false, "Inter Regular · 13 pt", 0.5],
  ];
  let yy = ty;
  sc.forEach((r) => {
    T(s, r[0], X0, yy, lw - 3.6, r[4], { fontSize: r[1], bold: r[2], fontFace: r[2] ? H : B, color: r[1] === 13 ? C.accent3 : C.text1, valign: "middle" });
    T(s, r[3], X0 + lw - 3.4, yy, 3.4, r[4], { fontSize: 14, color: C.accent3, valign: "middle", align: "right" });
    yy += r[4] + 0.2;
  });
  const rx = X0 + lw + 0.5, rw = XR - rx;
  card(s, rx, ty - 0.1, rw, 3.6);
  T(s, "REGLAS DE USO", rx + 0.4, ty + 0.25, rw - 0.8, 0.35, { fontSize: 16, bold: true, fontFace: H, color: C.accent1 });
  T(s, [
    { text: "Una idea por lámina.", options: { bullet: true, breakLine: true } },
    { text: "Naranjo solo para destacar.", options: { bullet: true, breakLine: true } },
    { text: "Cuerpo desde 16 pt, pies 13 pt.", options: { bullet: true, breakLine: true } },
    { text: "Cifras con coma decimal: 82,4 %.", options: { bullet: true, breakLine: true } },
    { text: "Sin líneas bajo los títulos.", options: { bullet: true } },
  ], rx + 0.4, ty + 0.85, rw - 0.8, 2.5, { fontSize: 16, paraSpaceAfter: 8 });
}

// pptxgenjs writes a few chart faults in combo charts that PowerPoint rejects
// (undeclared third axId, invertIfNegative / outEnd on line series). Patch them.
async function patchCharts(file) {
  const JSZip = require("jszip");
  const fs = require("fs");
  const zip = await JSZip.loadAsync(fs.readFileSync(file));
  for (const name of Object.keys(zip.files)) {
    if (!/^ppt\/charts\/chart\d+\.xml$/.test(name)) continue;
    let x = await zip.file(name).async("string");
    x = x.replace('<c:roundedCorners val="1"/>', '<c:roundedCorners val="0"/>');
    if (x.includes("<c:lineChart>") && x.includes("<c:barChart>")) {
      x = x.replace(/(<c:axId val="\d+"\/><c:axId val="\d+"\/>)<c:axId val="\d+"\/>(<\/c:(?:bar|line)Chart>)/g, "$1$2");
      x = x.replace(/<c:lineChart>[\s\S]*?<\/c:lineChart>/, (lc) =>
        lc.replace(/<c:invertIfNegative val="0"\/>/g, "").replace(/<c:dLblPos val="outEnd"\/>/g, '<c:dLblPos val="t"/>')
      );
      x = x.replace(/(<c:dLbls>[\s\S]*?<\/c:dLbls>)((?:\s*<c:dPt>[\s\S]*?<\/c:dPt>)+)/g, "$2$1");
    }
    zip.file(name, x);
  }
  fs.writeFileSync(file, await zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" }));
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await patchCharts(OUT);
  await applyTheme(OUT, THEME);
  console.log("OK", OUT);
})();
