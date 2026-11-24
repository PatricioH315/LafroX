/**
 * Biblioteca compartida LafroX: tema, layouts, helpers de tarjetas/figuras/graficos y
 * post-proceso (SVG de figuras, Morph/transiciones, correccion de graficos combinados).
 * Uso:  const kit = require("./lib/lafrox").createKit({ title, subject });
 */
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");

const SKILL =
  "C:/Users/henri/AppData/Local/Claude-Data/claude_pzs8sxrjxfjjc/local-agent-mode-sessions/skills-plugin/0cc4aafe-fe17-40e0-8a2d-d71c9c2b7355/f5b4c97f-b594-476b-8792-d6ce8e876c57/skills/pptx";
const { applyTheme } = require(SKILL + "/scripts/apply_theme.js");

const ROOT = path.join(__dirname, "..");
const A = (f) => path.join(ROOT, "assets", f);

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

// Grid constants (inches)
const X0 = 1.61, W = 16.8, XR = X0 + W, Y0 = 3.1, YB = 10.2;

const DECOR_KINDS = [
  "onda-naranjo", "onda-naranjo-claro", "anillos", "cuarto-circulo", "hoja", "mosaico", "figura", "aros", "puntos",
  "icono-web", "icono-telefono", "icono-ubicacion", "icono-correo",
];
const decorPng = (kind) => path.join(ROOT, "assets", "decor", "png", kind + ".png");
const decorSvg = (kind) => path.join(ROOT, "assets", "decor", kind + ".svg");
const pngRatio = (file) => {
  const b = fs.readFileSync(file);
  return b.readUInt32BE(16) / b.readUInt32BE(20);
};
const DECOR_RATIO = Object.fromEntries(DECOR_KINDS.map((k) => [k, pngRatio(decorPng(k))]));

function createKit(meta = {}) {
  const pres = new pptxgen();
  pres.defineLayout({ name: "LAFROX", width: 20, height: 11.25 });
  pres.layout = "LAFROX";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.title = meta.title || "LafroX";
  pres.author = "LafroX SpA";
  pres.company = "LafroX SpA";
  pres.subject = meta.subject || "";
  const C = pres.SchemeColor;
  const H = "+mj-lt";
  const B = "+mn-lt";

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

  const darkCard = (s, x, y, w, h, name) =>
    card(s, x, y, w, h, { fill: { color: C.text1 }, line: { color: C.text1, width: 1 }, ...(name ? { objectName: name } : {}) });

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

  // Figuras decorativas (assets/decor). Se insertan como PNG de alta resolucion y, al final
  // del build, se les agrega la version SVG (nitida en PowerPoint; Google Slides usa el PNG).
  // Regla Morph: la misma figura conserva el mismo nombre "!!deco_<tipo>_<n>" en laminas consecutivas.
  // o: { x, y, w, h?, rotate?, flipH?, transparency? }  (h se deduce de la proporcion si falta)
  const deco = (s, kind, n, o) => {
    if (!DECOR_RATIO[kind]) throw new Error("Figura desconocida: " + kind);
    const { h, ...rest } = o;
    s.addImage({
      path: decorPng(kind), ...rest, h: h ?? o.w / DECOR_RATIO[kind],
      objectName: `!!deco_${kind}_${n}`, altText: "Figura decorativa",
    });
  };
  // Arco en U invertido que entra desde el borde (rotado 180 y espejado, como en el original).
  const arc = (s, kind, n, x, y, w = 12.67, flip = true) =>
    deco(s, kind, n, { x, y, w, ...(flip ? { rotate: 180, flipH: true } : {}) });
  const RINGS = (s, x, y, d = 11.2, n = 1) => deco(s, "anillos", n, { x, y, w: d, h: d, transparency: 95 });
  const QUARTER = (s, x = 18.2, y = -3.6, d = 6.0) => deco(s, "cuarto-circulo", 1, { x, y, w: d, h: d });

  const lineOpt = (color, w = 0.5) => ({ color, width: w });

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

  // Layouts adicionales (presentacion final): HERO = fondo oscuro sin objetos (todo se arma con
  // formas "!!" para que Morph las anime); COMPACTO = contenido claro sin marca, titulo alto.
  if (meta.extraLayouts) {
    pres.defineSlideMaster({
      title: "HERO",
      background: { color: C.text1 },
      objects: [],
      slideNumber: numStyle(true),
    });
    pres.defineSlideMaster({
      title: "BLANCO",
      background: { color: C.background1 },
      objects: [],
      slideNumber: numStyle(false),
    });
    pres.defineSlideMaster({
      title: "COMPACTO",
      background: { color: C.background1 },
      objects: [
        {
          placeholder: {
            options: {
              name: "title", type: "title", x: 1.61, y: 0.5, w: 16.8, h: 0.95, fontSize: 44, bold: true,
              color: C.text1, align: "left", valign: "top", margin: 0,
            },
            text: "",
          },
        },
      ],
      slideNumber: numStyle(false),
    });
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

  // ---------------------------------------------------------------- Post-proceso
  const kit = {
    pres, C, H, B, THEME, X0, W, XR, Y0, YB, A, DECOR_RATIO,
    T, card, darkCard, pill, circle, source, caption, deco, arc, RINGS, QUARTER, lineOpt, slide, title, chartBase,
    th, td, tblBorder, brand, photo,
  };

  // Transiciones. cfg = { enabled, durMs, type, skip:[n], fade:[n], slides:{ n:{type,durMs,advTm} }, renameTitles }
  kit.finish = async (out, cfg = {}) => {
    const M = { enabled: true, durMs: 1200, type: "morph", skip: [1], fade: [], slides: {}, renameTitles: false, ...cfg };
    await pres.writeFile({ fileName: out });
    await patchCharts(out);
    await patchSlides(out, M);
    await applyTheme(out, THEME);
  };
  return kit;
}

// pptxgenjs escribe fallas en graficos combinados que PowerPoint rechaza
// (tercer axId sin declarar, invertIfNegative / outEnd en series de linea). Se corrigen aqui.
async function patchCharts(file) {
  const JSZip = require("jszip");
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

// Transicion de una lamina: Morph (con respaldo fade) o fade; admite avance automatico (advTm) y duracion.
function transitionXml(t) {
  const adv = t.advTm ? ` advTm="${t.advTm}"` : "";
  if (t.type === "fade") return `<p:transition spd="med"${adv}><p:fade/></p:transition>`;
  return (
    '<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main"><mc:Choice Requires="p159"><p:transition spd="slow" xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" p14:dur="' +
    t.durMs + '"' + adv +
    '><p159:morph option="byObject"/></p:transition></mc:Choice><mc:Fallback><p:transition spd="slow"' + adv +
    "><p:fade/></p:transition></mc:Fallback></mc:AlternateContent>"
  );
}

async function patchSlides(file, M) {
  const JSZip = require("jszip");
  const zip = await JSZip.loadAsync(fs.readFileSync(file));
  const usedSvg = new Set();
  const slideFiles = Object.keys(zip.files).filter((n) => /^ppt\/slides\/slide\d+\.xml$/.test(n));
  for (const name of slideFiles) {
    const num = Number(name.match(/slide(\d+)\.xml$/)[1]);
    const relsName = `ppt/slides/_rels/slide${num}.xml.rels`;
    let x = await zip.file(name).async("string");
    let rels = await zip.file(relsName).async("string");
    x = x.replace(/<p:pic>[\s\S]*?<\/p:pic>/g, (pic) => {
      const m = pic.match(/name="!!deco_([a-z-]+)_\d+"/);
      if (!m) return pic;
      usedSvg.add(m[1]);
      const rid = `rIdSvg${m[1].replace(/-/g, "")}`;
      if (!rels.includes(`Id="${rid}"`)) {
        rels = rels.replace(
          "</Relationships>",
          `<Relationship Id="${rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/decor-${m[1]}.svg"/></Relationships>`
        );
      }
      const ext = `<a:extLst><a:ext uri="{96DAC541-7B7A-43D3-8B79-37D633B846F1}"><asvg:svgBlip xmlns:asvg="http://schemas.microsoft.com/office/drawing/2016/SVG/main" r:embed="${rid}"/></a:ext></a:extLst>`;
      if (/<a:blip [^>]*\/>/.test(pic)) return pic.replace(/<a:blip ([^>]*?)\/>/, `<a:blip $1>${ext}</a:blip>`);
      return pic.replace("</a:blip>", ext + "</a:blip>");
    });
    if (M.renameTitles) {
      // el titulo recibe el nombre "!!title" para que Morph lo empareje entre laminas
      x = x.replace(/<p:sp>(?:(?!<\/p:sp>)[\s\S])*?<p:ph[^>]*type="title"[\s\S]*?<\/p:sp>/g, (sp) =>
        sp.replace(/(<p:cNvPr id="\d+" name=")[^"]*(")/, "$1!!title$2"));
    }
    const ov = M.slides[num] || {};
    if (M.enabled && !M.skip.includes(num) && !x.includes("p159:morph") && !/<p:transition/.test(x)) {
      const type = ov.type || (M.fade.includes(num) ? "fade" : M.type);
      x = x.replace("</p:clrMapOvr>", "</p:clrMapOvr>" + transitionXml({ type, durMs: ov.durMs || M.durMs, advTm: ov.advTm }));
    } else if (M.skip.includes(num) && ov.type === "fade") {
      x = x.replace("</p:clrMapOvr>", "</p:clrMapOvr>" + transitionXml({ type: "fade", advTm: ov.advTm }));
    }
    zip.file(name, x);
    zip.file(relsName, rels);
  }
  for (const kind of usedSvg) zip.file(`ppt/media/decor-${kind}.svg`, fs.readFileSync(decorSvg(kind)));
  let ct = await zip.file("[Content_Types].xml").async("string");
  if (!ct.includes('Extension="svg"')) ct = ct.replace("<Override", '<Default Extension="svg" ContentType="image/svg+xml"/><Override');
  zip.file("[Content_Types].xml", ct);
  fs.writeFileSync(file, await zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" }));
}

module.exports = { createKit, decorPng, THEME, DECOR_KINDS, X0, W, XR, Y0, YB };
