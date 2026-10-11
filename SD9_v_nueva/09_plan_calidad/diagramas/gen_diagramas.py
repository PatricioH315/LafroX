"""Genera los diagramas draw.io del SD9 (v_nueva) y los exporta a PDF.

Escala medida: 1 px de draw.io = 0,72 pt en el PDF exportado.
Texto a 13 px (~9,4 pt) y ancho <= 600 px para insertar a tamaño natural
(ancho de texto de la clase lafrox = 448 pt ~ 622 px).
"""
import html
import subprocess
import sys
from pathlib import Path

DRAWIO = r"C:\Users\henri\AppData\Local\Programs\draw.io\draw.io.exe"
OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

FS = 13
BOX = (f"rounded=1;whiteSpace=wrap;html=1;fontSize={FS};fontFamily=Helvetica;"
       "fillColor=#FFFFFF;strokeColor=#333333;fontColor=#111111;arcSize=8;")
BOXDARK = (f"rounded=1;whiteSpace=wrap;html=1;fontSize={FS};fontFamily=Helvetica;"
           "fillColor=#E6E6E6;strokeColor=#111111;fontColor=#111111;arcSize=8;fontStyle=1;")
BOXACC = (f"rounded=1;whiteSpace=wrap;html=1;fontSize={FS};fontFamily=Helvetica;"
          "fillColor=#FDE8DA;strokeColor=#E8641B;fontColor=#111111;arcSize=8;")
GROUP = (f"rounded=0;whiteSpace=wrap;html=1;fontSize={FS};fontFamily=Helvetica;"
         "fillColor=#F4F4F4;strokeColor=#9A9A9A;fontColor=#111111;verticalAlign=top;"
         "align=left;spacingLeft=8;spacingTop=2;fontStyle=1;")
TEXT = (f"text;html=1;fontSize={FS};fontFamily=Helvetica;fontColor=#111111;"
        "align=left;verticalAlign=middle;whiteSpace=wrap;")
EDGE = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#333333;"
        f"endArrow=block;endFill=1;fontSize={FS};fontFamily=Helvetica;")
EDGEDASH = EDGE + "dashed=1;"
EDGESTRAIGHT = ("rounded=0;html=1;strokeColor=#333333;endArrow=block;endFill=1;"
                f"fontSize={FS};fontFamily=Helvetica;")


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
    d = Diagram("Fig_9-1_Marco_Calidad")
    W = 600
    for title, y in (("Normas", 0), ("Métricas con umbral", 120), ("Control", 240), ("Aceptación", 360)):
        d.box(title, 0, y, W, 100, GROUP)
    n3 = d.box("ISO/IEC/IEEE 29119<br>pruebas", 10, 30, 135, 56)
    n1 = d.box("ISO/IEC 25010<br>producto", 158, 30, 135, 56)
    n2 = d.box("ISO/IEC 25012<br>datos", 306, 30, 135, 56)
    n4 = d.box("PMBOK cap. 8<br>proceso", 455, 30, 135, 56)
    m1 = d.box("42 métricas de producto y datos (Anexo 9.A)", 160, 150, 160, 56)
    m2 = d.box("6 métricas de código bloqueantes", 335, 150, 110, 56)
    m3 = d.box("Métricas de proceso y costo de la calidad", 455, 150, 135, 56)
    c2 = d.box("Pruebas por nivel y ambiente (T-13)", 10, 270, 250, 56)
    c1 = d.box("Puertas G0 a G6", 335, 270, 255, 56)
    e1 = d.box("Expediente y matriz de trazabilidad", 10, 390, 300, 56)
    e2 = d.box("Acta por hito (T-17)", 370, 390, 220, 56, BOXDARK)
    d.edge(n3, c2, exit_=(0.5, 1), entry=(0.26, 0))
    d.edge(n1, m1, exit_=(0.5, 1), entry=(0.3, 0))
    d.edge(n2, m1, exit_=(0.5, 1), entry=(0.75, 0), points=[(373, 112), (280, 112)])
    d.edge(n4, m3, exit_=(0.5, 1), entry=(0.5, 0))
    d.edge(m1, c2, exit_=(0.3, 1), entry=(0.84, 0))
    d.edge(m2, c1, exit_=(0.5, 1), entry=(0.2, 0))
    d.edge(m3, c1, exit_=(0.5, 1), entry=(0.73, 0))
    d.edge(c2, e1, exit_=(0.5, 1), entry=(0.42, 0))
    d.edge(c1, e1, exit_=(0, 0.75), entry=(0.95, 0), points=[(295, 312)])
    d.edge(e1, e2)
    d.save()


def fig2():
    d = Diagram("Fig_9-2_Modelo_ISO25010")
    root = d.box("Calidad del producto<br>ISO/IEC 25010", 180, 0, 240, 50, BOXDARK)
    items = [
        ("<b>Funcionalidad</b><br>100 % de requisitos ofertados con prueba aprobada", 0),
        ("<b>Desempeño</b><br>preparación ≤ 1 s · entrega ≤ 2 s · preventa ≤ 1,5 s; p95 a 21,99 TPS", 0),
        ("<b>Compatibilidad</b><br>15 de 15 integraciones · 0 contratos rotos", 0),
        ("<b>Usabilidad</b><br>WCAG 2.2 AA · guantes a −22 °C · una mano", 0),
        ("<b>Fiabilidad</b><br>99,9 % críticos · 0 min de 05:30 a 07:00 · RTO ≤ 4 h · RPO ≤ 15 min", 1),
        ("<b>Seguridad</b><br>0 hallazgos críticos o altos abiertos", 1),
        ("<b>Mantenibilidad</b><br>cobertura 70 % negocio y 80 % global", 1),
        ("<b>Portabilidad</b><br>mismo artefacto de QA a Producción", 1),
    ]
    left = [t for t, c in items if c == 0]
    right = [t for t, c in items if c == 1]
    for col, texts in ((0, left), (1, right)):
        x = 0 if col == 0 else 320
        for i, t in enumerate(texts):
            y = 90 + i * 92
            b = d.box(t, x, y, 280, 72)
            sx = 0.35 if col == 0 else 0.65
            spine = 290 if col == 0 else 310
            d.edge(root, b, exit_=(sx, 1), entry=(1 if col == 0 else 0, 0.5),
                   points=[(spine, 70), (spine, y + 36)])
    d.save()


def fig3():
    d = Diagram("Fig_9-3_Puertas_Calidad")
    gates = [
        "<b>G0 · Compromiso local</b><br>formato y pruebas del módulo",
        "<b>G1 · Solicitud de fusión</b><br>revisión por pares · secretos",
        "<b>G2 · Integración continua</b><br>coberturas · complejidad · acoplamiento · duplicación · SAST/SCA · contratos",
        "<b>G3 · Promoción a QA</b><br>imagen sin vulnerabilidades altas · sin regresión de desempeño",
        "<b>G4 · Promoción a Preproducción</b><br>regresión · DAST · WCAG",
        "<b>G5 · Paso a producción (H7 y H12)</b><br>pruebas del T-13 · acta del T-17",
        "<b>G6 · Operación</b><br>canario · presupuesto de error",
    ]
    ids = []
    for i, g in enumerate(gates):
        ids.append(d.box(g, 0, i * 82, 380, 62, BOXDARK if i in (2, 4, 5) else BOX))
    for a, b in zip(ids, ids[1:]):
        d.edge(a, b)
    rej = d.box("Cambio rechazado<br>vuelve al autor", 450, 2 * 82 + 60, 140, 200, BOXACC)
    for i, ey in ((2, 0.1), (4, 0.5), (5, 0.9)):
        d.edge(ids[i], rej, EDGEDASH, label="bloquea", exit_=(1, 0.5), entry=(0, ey))
    d.save()


def fig4():
    d = Diagram("Fig_9-4_Niveles_Ambientes")
    W = 600
    groups = [
        ("Desarrollo", 0, ["Unitarias y de componente<br>PHPUnit · JUnit 5 · Jest", "Contrato<br>Pact · Spectral"]),
        ("QA", 100, ["Integración de los 15 flujos", "Sistema y regresión automatizada", "DAST · accesibilidad · carga de regresión"]),
        ("Preproducción", 200, ["Aceptación de usuario", "Carga 1,5× y estrés", "Resiliencia con inyección de fallas", "Migración · despliegue y reversión", "Intrusión por un tercero"]),
        ("Producción", 400, ["Marcha blanca: indicadores diarios"]),
    ]
    gids = {}
    for title, y, items in groups:
        h = 90 if len(items) <= 3 else 190
        gids[title] = d.box(title, 0, y, 420, h, GROUP)
        for i, it in enumerate(items):
            col, row = i % 3, i // 3
            if len(items) > 3:
                col, row = i % 2, i // 2
                bw = 195
                d.box(it, 10 + col * 205, y + 28 + row * 54, bw, 46)
            else:
                bw = 128 if len(items) == 3 else (195 if len(items) == 2 else 400)
                d.box(it, 10 + col * (bw + 8), y + 28, bw, 52)
    ter = d.box("Terreno y cámara", 450, 200, 150, 190, GROUP)
    d.box("14 h sin señal<br>−22 °C con guantes<br>lluvia · sol directo<br>una mano", 460, 230, 130, 150)
    dr = d.box("Recuperación", 450, 400, 150, 90, GROUP)
    d.box("Conmutación real<br>RTO ≤ 4 h<br>RPO ≤ 15 min", 460, 428, 130, 56)
    d.edge(gids["Desarrollo"], gids["QA"]); d.edge(gids["QA"], gids["Preproducción"])
    d.edge(gids["Preproducción"], gids["Producción"])
    d.edge(gids["Preproducción"], ter, exit_=(1, 0.5), entry=(0, 0.5))
    d.edge(gids["Producción"], dr, exit_=(1, 0.5), entry=(0, 0.5))
    d.save()


def fig5():
    d = Diagram("Fig_9-5_Datos_Prueba")
    v = d.box("Volumetría del Caso<br>14.200 clientes · 8.400 SKU<br>31.000 pedidos al mes", 0, 0, 270, 66)
    g = d.box("Generador sintético<br>reglas del SD3 y del SD5", 0, 100, 270, 52)
    j = d.box("Juegos versionados<br>restituidos antes de cada ciclo", 0, 186, 270, 52, BOXDARK)
    qa = d.box("QA", 0, 272, 125, 44)
    pre = d.box("Preproducción<br>volumen de peak", 145, 272, 125, 44)
    h = d.box("Datos históricos del CLIENTE<br>32,11 GB", 320, 0, 270, 66)
    a = d.box("Anonimización", 320, 100, 270, 52)
    mz = d.box("Verificación con Amazon Macie<br>y prueba de reidentificación", 320, 186, 270, 52, BOXDARK)
    pm = d.box("Preproducción<br>solo ensayos de migración", 320, 272, 270, 44)
    p = d.box("Producción", 0, 360, 270, 44)
    x = d.box("Prohibido: sin copia a QA ni a Preproducción", 320, 360, 270, 44, BOXACC)
    d.edge(v, g); d.edge(g, j); d.edge(j, qa); d.edge(j, pre)
    d.edge(h, a); d.edge(a, mz); d.edge(mz, pm)
    d.edge(p, x, EDGEDASH)
    d.save()


def fig6():
    d = Diagram("Fig_9-6_Modelo_V")
    left = ["Necesidad y 16 resultados<br>Caso cap. 18", "Requisitos<br>SD3 · T-12 (H1)",
            "Arquitectura y datos<br>SD4 · SD5 (H2)", "Diseño de módulo y contrato", "Código"]
    right = ["Marcha blanca y resultados del caso (H7 · H12)", "Aceptación de usuario<br>(H5 · H10)",
             "Sistema, carga, resiliencia, recuperación (H5 · H10)", "Integración y contrato<br>(H4 · H9)",
             "Unitarias"]
    lids, rids = [], []
    for i, t in enumerate(left):
        lids.append(d.box(t, i * 20, i * 76, 200, 56, BOX))
    for i, t in enumerate(right):
        rids.append(d.box(t, 400 - i * 20, i * 76, 200, 56, BOXDARK if i < 2 else BOX))
    for a, b in zip(lids, lids[1:]):
        d.edge(a, b, exit_=(0.5, 1), entry=(0.5, 0))
    for a, b in zip(rids[::-1], rids[::-1][1:]):
        d.edge(a, b, exit_=(0.5, 0), entry=(0.5, 1))
    d.edge(lids[4], rids[4], exit_=(1, 0.5), entry=(0, 0.5))
    labels = ["valida", "valida", "verifica", "verifica"]
    for i in range(4):
        d.edge(lids[i], rids[i], EDGEDASH + "endArrow=none;", label=labels[i],
               exit_=(1, 0.5), entry=(0, 0.5))
    d.save()


def fig7():
    d = Diagram("Fig_9-7_Cadena_Trazabilidad")
    steps = [
        ("Origen", "Caso cap. 18, resultado 1: retiro sanitario en menos de 2 h"),
        ("Requisito", "RF-09.01 trazabilidad hacia adelante (T-12)"),
        ("Componente", "M9 Calidad y trazabilidad (SD4)"),
        ("Paquete EDT", "3.4.4 Cadena de frío, retención de lotes y retiro sanitario (T-14)"),
        ("Caso de prueba", "Simulacro de retiro (T-13, sección 7.4)"),
        ("Cambio de código", "Solicitud de fusión con el ID del requisito"),
        ("Despliegue", "Digest de la imagen firmada"),
        ("Aceptación", "Acta del H7 (T-17)"),
    ]
    prev = None
    for i, (k, v) in enumerate(steps):
        y = i * 66
        b = d.box(f"<b>{k}</b>", 0, y, 150, 48, BOXDARK)
        d.box(v, 170, y, 430, 48, TEXT)
        if prev:
            d.edge(prev, b)
        prev = b
    d.save()


def fig8():
    d = Diagram("Fig_9-8_Ciclo_Mejora")
    inp = d.box("<b>Entradas</b>: métricas 9.1.5 y 9.1.6 · diagramas de control · auditorías · observaciones del CLIENTE · retrospectivas",
                0, 0, 600, 56)
    p = d.box("<b>Planificar</b><br>causa raíz · acción · dueño · plazo", 60, 100, 220, 70)
    h = d.box("<b>Hacer</b><br>corregir proceso, control o prueba", 320, 100, 220, 70)
    v = d.box("<b>Verificar</b><br>en el comité mensual siguiente, contra el mismo criterio", 320, 220, 220, 70)
    a = d.box("<b>Actuar</b><br>cerrar con evidencia o escalar", 60, 220, 220, 70)
    ll = d.box("Registro de lecciones aprendidas", 0, 340, 280, 50, BOXDARK)
    sc = d.box("Solicitud de cambio (Formulario T-9), si toca la línea base", 320, 340, 280, 50, BOXACC)
    d.edge(inp, p, exit_=(0.28, 1), entry=(0.5, 0))
    d.edge(p, h); d.edge(h, v); d.edge(v, a)
    d.edge(a, p, exit_=(0.5, 0), entry=(0.5, 1))
    d.edge(a, ll, exit_=(0.5, 1), entry=(0.5, 0))
    d.edge(a, sc, EDGEDASH, exit_=(1, 0.75), entry=(0.5, 0), points=[(300, 272), (300, 320), (460, 320)])
    d.save()


def fig9():
    d = Diagram("Fig_9-9_Calidad_Cronograma")
    LW, PX = 190, 7.4   # ancho de rotulos y px por mes (56 meses = 414 px)
    X0 = LW + 6

    def mx(m):  # inicio del mes m (1 = feb-2027)
        return X0 + (m - 1) * PX

    # Eje de anos: feb-27 es mes 1; enero de cada ano: m = 12k
    years = [("feb 2027", 1), ("2028", 12), ("2029", 24), ("2030", 36), ("2031", 48)]
    for yr, m in years:
        d.box(str(yr), mx(m) + 2, 0, 70, 20, TEXT + "align=left;")
    rows = [
        ("Matriz y plan (H1)", 2, 2),
        ("Usabilidad con usuarios", 2, 4),
        ("Puertas automáticas (1.5.2)", 6, 20),
        ("Ensayos de migración", 9, 11),
        ("Integración y regresión E1 (H4)", 9, 9),
        ("Certificación E1 (H5)", 9, 10),
        ("Marcha blanca E1", 13, 15),
        ("Integración y regresión E2 (H9)", 16, 16),
        ("Certificación E2 (H10)", 16, 17),
        ("Marcha blanca E2", 19, 20),
        ("Pruebas de la Operación", 21, 56),
    ]
    y0 = 28
    for i, (lab, a, b) in enumerate(rows):
        y = y0 + i * 26
        d.box(lab, 0, y, LW, 22, TEXT)
        d.box("", mx(a), y + 4, (b - a + 1) * PX, 14,
              "rounded=0;html=1;fillColor=#333333;strokeColor=none;")
    yfz = y0 + len(rows) * 26
    d.box("Congelamientos (sep. y dic.)", 0, yfz, LW, 22, TEXT)
    # septiembre = mes 8 + 12k; diciembre = mes 11 + 12k (k = 0..4)
    for k in range(5):
        for m in (8 + 12 * k, 11 + 12 * k):
            if m <= 56:
                d.box("", mx(m), yfz + 4, PX, 14,
                      "rounded=0;html=1;fillColor=#E8641B;strokeColor=none;")
    # rejilla anual
    for yr, m in years:
        d.box("", mx(m), 22, 0.6, yfz + 22 - 22 + 4,
              "rounded=0;html=1;fillColor=#C7C7C7;strokeColor=none;")
    d.save()


for f in (fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9):
    f()
