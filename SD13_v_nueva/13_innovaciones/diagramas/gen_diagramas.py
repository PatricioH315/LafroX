"""Genera los diagramas draw.io del SD13 y los exporta a PDF.

Mismo estilo que el SD9: 1 px de draw.io = 0,72 pt en el PDF exportado.
Texto a 13 px (~9,4 pt) y ancho ~600 px para insertar a tamaño natural
(ancho de texto de la clase lafrox = 448 pt ~ 622 px).

Uso: python gen_diagramas.py <carpeta_salida>
"""
import html
import subprocess
import sys
from pathlib import Path

import pymupdf

DRAWIO = r"C:\Users\henri\AppData\Local\Programs\draw.io\draw.io.exe"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent
OUT.mkdir(parents=True, exist_ok=True)

FS = 13
BOX = (f"rounded=1;whiteSpace=wrap;html=1;fontSize={FS};fontFamily=Helvetica;"
       "fillColor=#FFFFFF;strokeColor=#333333;fontColor=#111111;arcSize=8;")
BOXACC = (f"rounded=1;whiteSpace=wrap;html=1;fontSize={FS};fontFamily=Helvetica;"
          "fillColor=#FDE8DA;strokeColor=#E8641B;fontColor=#111111;arcSize=8;")
GROUP = (f"rounded=0;whiteSpace=wrap;html=1;fontSize={FS};fontFamily=Helvetica;"
         "fillColor=#F4F4F4;strokeColor=#9A9A9A;fontColor=#111111;verticalAlign=top;"
         "align=left;spacingLeft=8;spacingTop=2;fontStyle=1;")
EDGE = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#333333;"
        f"endArrow=block;endFill=1;fontSize={FS};fontFamily=Helvetica;")
EDGEDASH = EDGE + "dashed=1;"

HELV = pymupdf.Font("helv")
LINE = 16  # alto de línea a 13 px


def alto(texto, ancho, minimo=40):
    """Alto de caja para que el texto quepa en el ancho dado."""
    n = 0
    for parrafo in texto.replace("<b>", "").replace("</b>", "").split("<br>"):
        lineas, actual = 1, ""
        for w in parrafo.split(" "):
            prueba = (actual + " " + w).strip()
            if HELV.text_length(prueba, fontsize=FS) > ancho - 14 and actual:
                lineas, actual = lineas + 1, w
            else:
                actual = prueba
        n += lineas
    return max(minimo, n * LINE + 12)


class Diagram:
    def __init__(self, name):
        self.name = name
        self.cells = []
        self.n = 0

    def _id(self):
        self.n += 1
        return f"c{self.n}"

    def box(self, text, x, y, w, h, style=BOX):
        cid = self._id()
        self.cells.append(
            f'<mxCell id="{cid}" value="{html.escape(text, quote=True)}" style="{style}" '
            f'vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" '
            f'height="{h}" as="geometry"/></mxCell>')
        return cid

    def edge(self, s, t, style=EDGE, label="", points=None, exit_=None, entry=None):
        cid = self._id()
        st = style
        if exit_:
            st += f"exitX={exit_[0]};exitY={exit_[1]};exitDx=0;exitDy=0;"
        if entry:
            st += f"entryX={entry[0]};entryY={entry[1]};entryDx=0;entryDy=0;"
        pts = ""
        if points:
            pts = "<Array as=\"points\">" + "".join(
                f'<mxPoint x="{px}" y="{py}"/>' for px, py in points) + "</Array>"
        self.cells.append(
            f'<mxCell id="{cid}" value="{html.escape(label, quote=True)}" style="{st}" '
            f'edge="1" parent="1" source="{s}" target="{t}"><mxGeometry relative="1" '
            f'as="geometry">{pts}</mxGeometry></mxCell>')
        return cid

    def save(self):
        body = "".join(self.cells)
        xml = ('<mxfile host="drawio"><diagram name="' + self.name + '">'
               '<mxGraphModel dx="800" dy="600" grid="1" gridSize="10" page="0">'
               '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + body +
               '</root></mxGraphModel></diagram></mxfile>')
        src = OUT / f"{self.name}.drawio"
        src.write_text(xml, encoding="utf-8")
        pdf = OUT / f"{self.name}.pdf"
        subprocess.run([DRAWIO, "-x", "-f", "pdf", "--crop", "-b", "4",
                        "-o", str(pdf), str(src)], check=True,
                       capture_output=True)
        print("ok", pdf.name)


def fig1():
    """Figura 13.1: ubicación de las cinco innovaciones en la arquitectura."""
    d = Diagram("Fig_13-1_Mapa_Innovaciones")
    W, GAP, TOP = 600, 20, 28

    # Capas 1 y 2, lado a lado. C-02 y B-03 en la misma fila (B-03 -> C-02).
    y = 0
    c_txt = ["C-02 App de reparto e impresora de cabina<br>(INN-02, INN-03, INN-05)",
             "C-01 App de preventa<br>(INN-01, INN-02, INN-05)",
             "C-03 Terminales de bodega<br>(INN-02)"]
    b_txt = ["B-03 Termógrafos de camión<br>(INN-03)",
             "B-01 Sensores de temperatura<br>(INN-03)",
             "B-02 Gateway IoT<br>(INN-03)"]
    rh = max(alto(t, 320) for t in c_txt + b_txt)
    gh = TOP + 3 * rh + 2 * 16 + 10
    g1 = d.box("Capa 1 · Presentación", 0, y, 340, gh, GROUP)
    g2 = d.box("Capa 2 · Borde y exposición", 360, y, 240, gh, GROUP)
    c02, c01, c03 = (d.box(t, 10, y + TOP + i * (rh + 16), 320, rh) for i, t in enumerate(c_txt))
    b03, b01, b02 = (d.box(t, 370, y + TOP + i * (rh + 16), 220, rh) for i, t in enumerate(b_txt))
    d.edge(b03, c02, exit_=(0, 0.5), entry=(1, 0.5))
    d.edge(b01, b02, exit_=(0.5, 1), entry=(0.5, 0))
    y1_mid = y + gh / 2
    b02_mid = y + TOP + 2 * (rh + 16) + rh / 2

    # Capa 5: integración y eventos.
    y += gh + GAP
    sync_t = "Cola de sincronización de los terminales<br>(INN-01, INN-02, INN-05)"
    epc_t = "Eventos EPCIS 2.0 con datos de sensor<br>(INN-03)"
    h5 = max(alto(sync_t, 218), alto(epc_t, 170))
    d.box("Capa 5 · Integración y eventos", 0, y, W, TOP + h5 + 10, GROUP)
    sync = d.box(sync_t, 128, y + TOP, 218, h5)
    epcis = d.box(epc_t, 420, y + TOP, 170, h5)
    d.edge(g1, sync, exit_=(0.75, 1), entry=(0.583, 0))
    d.edge(b02, epcis, exit_=(0.5, 1), entry=(0.353, 0))

    # Capa 4: lógica de negocio. M10 a la izquierda para recibir de N-10.
    y += TOP + h5 + 10 + GAP
    m_txt = ["M10 Analítica<br>(INN-01, INN-03, INN-04, INN-05)",
             "M2 Inventario · M3 Preventa<br>(INN-01, INN-03, INN-05)",
             "M5 Preparación · M6 Reparto<br>(INN-02 a INN-05)",
             "M7 Cobranza y rendición · M8 Devoluciones y envases<br>(INN-01, INN-04)",
             "M9 Calidad y trazabilidad<br>(INN-01, INN-03)"]
    mw, mx = 108, [10, 128, 246, 364, 482]
    h4 = max(alto(t, mw) for t in m_txt)
    g4h = TOP + h4 + 10
    d.box("Capa 4 · Lógica de negocio", 0, y, W, g4h, GROUP)
    m10, m23, m56, m78, m9 = (d.box(t, mx[i], y + TOP, mw, h4) for i, t in enumerate(m_txt))
    d.edge(sync, m23, exit_=(0.422, 1), entry=(0.85, 0))
    d.edge(sync, m56, exit_=(0.79, 1), entry=(0.5, 0))
    d.edge(epcis, m9, exit_=(0.676, 1), entry=(0.5, 0))
    y_gap = y + g4h + GAP / 2

    # Capa 6: acceso a datos.
    y += g4h + GAP
    n10_t = "N-10 Plataforma analítica<br>(INN-01, INN-03, INN-04, INN-05)"
    n06_t = "N-06 Telemetría cruda · N-08 Ingesta de IoT<br>(INN-03)"
    nx, nw = 10, 410
    h6 = max(alto(n10_t, nw), alto(n06_t, 150))
    d.box("Capa 6 · Acceso a datos", 0, y, W, TOP + h6 + 10, GROUP + "align=right;spacingRight=8;")
    n10 = d.box(n10_t, nx, y + TOP, nw, h6)
    n0608 = d.box(n06_t, 440, y + TOP, 150, h6)
    n06_mid = y + TOP + h6 / 2
    for m, i in ((m23, 1), (m56, 2), (m78, 3)):
        ex = {1: 0.85, 2: 0.5, 3: 0.3}[i]
        cx = mx[i] + mw * ex
        d.edge(m, n10, exit_=(ex, 1), entry=(round((cx - nx) / nw, 3), 0))
    d.edge(m9, n10, exit_=(0.2, 1), entry=(0.976, 0),
           points=[(mx[4] + mw * 0.2, y_gap), (nx + nw * 0.976, y_gap)])
    d.edge(n10, m10, exit_=(round((mx[0] + mw / 2 - nx) / nw, 3), 0), entry=(0.5, 1))
    d.edge(n0608, n10, exit_=(0, 0.5), entry=(1, 0.5))
    d.edge(b02, n0608, exit_=(1, 0.5), entry=(1, 0.5),
           points=[(611, b02_mid), (611, n06_mid)])

    # Capas transversales.
    y += TOP + h6 + 10 + GAP
    l7_t = ("<b>Capa 7 · Seguridad:</b> sanitización (INN-02), versionado del modelo (INN-03), "
            "auditoría de la liquidación (INN-04), limitación al receptor (INN-05)")
    l8_t = "<b>Capa 8 · Observabilidad:</b> trazas OpenTelemetry y Amazon CloudWatch (INN-02)"
    h7, h8 = alto(l7_t, 580), alto(l8_t, 580)
    d.box("Capas transversales", 0, y, W, TOP + h7 + 8 + h8 + 10, GROUP)
    d.box(l7_t, 10, y + TOP, 580, h7)
    l8 = d.box(l8_t, 10, y + TOP + h7 + 8, 580, h8)
    d.edge(g1, l8, EDGEDASH, exit_=(0, 0.5), entry=(0, 0.5),
           points=[(-11, y1_mid), (-11, y + TOP + h7 + 8 + h8 / 2)])
    d.save()


if __name__ == "__main__":
    pedidas = set(sys.argv[2:])
    for f in (fig1,):
        if not pedidas or f.__name__ in pedidas:
            f()
