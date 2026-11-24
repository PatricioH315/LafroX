/**
 * Generador de la presentacion final de LafroX: "LafroX - Presentación Final.pptx".
 * Uso:  python -I tools/extract_final_data.py   (genera data/final.json desde el modelo SD7)
 *       node build_final.js
 * Todas las cifras salen de data/final.json; no hay montos escritos a mano en las laminas.
 * Estructura: tema/layouts/helpers en lib/lafrox.js; una funcion por bloque en slides/*.js.
 */
const fs = require("fs");
const path = require("path");
const { createKit } = require("./lib/lafrox");
const { fmt, pct, uf } = require("./lib/format");

const OUT = path.join(__dirname, "LafroX - Presentación Final.pptx");
const D = JSON.parse(fs.readFileSync(path.join(__dirname, "data", "final.json"), "utf8"));

const kit = createKit({
  title: "LafroX - Presentación Final",
  subject: "Propuesta Técnica y Económica, Licitación TFEP-01/2026",
  extraLayouts: true,
});
const { pres, C, H, B, X0, W, XR, Y0, YB, T } = kit;

["Apertura", "Solución", "Ejecución", "Innovación", "Oferta económica", "Cierre", "Anexo"].forEach((t) =>
  pres.addSection({ title: t })
);

let n = 0;
const OVERRIDES = {}; // transiciones por lamina
const ctx = {
  kit, D, fmt, pct, uf, OVERRIDES,
  num: () => n,
  // Crea una lamina con notas: who = presentador, t = reloj acumulado (m:ss) o null (anexo)
  add(layout, section, who, t, script) {
    n += 1;
    const s = pres.addSlide({ masterName: layout, sectionTitle: section });
    const head = t ? `${who} · Hora objetivo (acumulada): ${t}` : `${who} · Anexo: se proyecta solo si la Comisión lo consulta`;
    s.addNotes(`${head}\n\n${script}`);
    return s;
  },
  title: (s, t) => s.addText(t, { placeholder: "title" }),
  // Texto con nombre "!!" (Morph lo empareja entre laminas consecutivas)
  N: (s, name, text, x, y, w, h, o = {}) => T(s, text, x, y, w, h, { objectName: name, ...o }),
  // Foto de fondo recortada (cover) en la caja dada
  photo(s, x, y, w, h) {
    s.addImage({
      path: kit.A("fondo-oscuro.jpeg"), x, y, w: 20, h: 11.25, sizing: { type: "cover", w, h },
      objectName: "!!foto", altText: "Fotografía de edificios en tonos oscuros",
    });
  },
  // Isotipo + marca como formas con nombre (se animan con Morph)
  brand(s, dark, x, y, o = {}) {
    const k = o.k || 1;
    s.addImage({
      path: kit.A(dark ? "isotipo-naranjo.png" : "isotipo-negro.png"), x, y, w: 0.6 * k, h: 0.62 * k,
      objectName: "!!logo", altText: "Isotipo LafroX",
    });
    T(s, "LafroX SpA", x + (o.dx ?? 0.78 * k), y + (o.dy ?? 0.16 * k), o.w ?? 3.64, 0.33 * k, {
      objectName: "!!brand", fontSize: 18 * k, bold: true, fontFace: H, color: dark ? C.background1 : C.text1,
      valign: "middle", align: o.align || "left",
    });
  },
  src: (s, text, y = 9.85, dark = false) =>
    T(s, text, X0, y, 15.5, 0.3, { fontSize: 13, color: dark ? C.accent5 : C.accent3, objectName: "!!fuente" }),
};

// Orden de la presentacion
require("./slides/apertura")(ctx);
require("./slides/solucion")(ctx);
require("./slides/ejecucion")(ctx);
require("./slides/oferta")(ctx);
require("./slides/cierre")(ctx);

(async () => {
  OVERRIDES[1] = { type: "fade" };
  await kit.finish(OUT, {
    enabled: true, durMs: 1200, skip: [], slides: OVERRIDES, renameTitles: true,
  });
  console.log("OK", OUT, "laminas:", n);
})();
