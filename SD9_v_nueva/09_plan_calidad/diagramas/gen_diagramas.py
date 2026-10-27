"""Genera los diagramas draw.io del SD9 (v_nueva) y los exporta a PDF.

Escala medida: 1 px de draw.io = 0,72 pt en el PDF exportado.
Texto a 13 px (~9,4 pt) y ancho <= 600 px para insertar a tamaño natural
(ancho de texto de la clase lafrox = 448 pt ~ 622 px).
"""
import html

import pymupdf
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
    m2 = d.box("8 métricas de código bloqueantes", 335, 150, 110, 56)
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
        ("<b>Compatibilidad</b><br>100 % de E1 · 15 de 15 al cierre E2<br>0 contratos rotos", 0),
        ("<b>Usabilidad</b><br>WCAG 2.2 AA · métricas por perfil<br>guantes a −22 °C · una mano", 0),
        ("<b>Fiabilidad</b><br>99,9 % críticos · 99,95 % infraestructura<br>0 min de 05:30 a 07:00 · RTO ≤ 4 h · RPO ≤ 15 min", 1),
        ("<b>Seguridad</b><br>0 hallazgos críticos o altos abiertos", 1),
        ("<b>Mantenibilidad</b><br>70 % negocio · 80 % global<br>80 % líneas modificadas", 1),
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
        "<b>G5 · Entrada a Producción (H6 y H11)</b><br>pruebas T-13 · certificación H5/H10 · reversión · datos · capacitación",
        "<b>G6 · Producción supervisada y Operación</b><br>canario · presupuesto de error",
    ]
    ids = [d.box(g, 0, i * 82, 380, 62, BOXDARK if i in (2, 4, 5) else BOX)
           for i, g in enumerate(gates)]
    for a, b in zip(ids, ids[1:]):
        d.edge(a, b)
    rej = d.box("Cambio rechazado<br>vuelve al autor", 450, 224, 140, 200, BOXACC)
    for i, ey in ((2, 0.1), (4, 0.5), (5, 0.9)):
        d.edge(ids[i], rej, EDGEDASH, label="bloquea", exit_=(1, 0.5), entry=(0, ey))
    acta = d.box("<b>Aceptación H7/H12</b><br>seis condiciones<br>Art. 17.3<br>acta T-17", 450, 478, 140, 90, BOXDARK)
    d.edge(ids[6], acta, EDGEDASH, exit_=(1, 0.5), entry=(0, 0.5))
    d.save()


def fig4():
    d = Diagram("Fig_9-4_Niveles_Ambientes")
    W = 600
    groups = [
        ("Desarrollo", 0, ["Unitarias y de componente<br>PHPUnit · JUnit 5 · Jest", "Contrato<br>Pact · Spectral"]),
        ("QA", 100, ["Integración aplicable<br>por etapa", "Sistema y regresión automatizada", "DAST · accesibilidad · carga de regresión"]),
        ("Preproducción", 200, ["Aceptación de usuario", "Carga 1,5× y estrés", "Resiliencia · sitios aislados 24 h<br>gateways de frío", "Migración · despliegue y reversión", "Intrusión por un tercero"]),
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
    d.box("14 h sin señal<br>−22 °C con guantes<br>lluvia · sobre 34 °C<br>sol directo · una mano", 460, 230, 130, 150)
    dr = d.box("Recuperación", 450, 400, 150, 90, GROUP)
    d.box("Conmutación real<br>nube y WMS Talca<br>RTO ≤ 4 h<br>RPO ≤ 15 min", 460, 420, 130, 66)
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
    right = ["Resultados: H7/H12<br>OTIF por tramos · envases a 12 meses", "Aceptación de usuario<br>(H5 · H10)",
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


BAR = "rounded=0;html=1;strokeColor=none;fillColor=%s;"
DIAM = "rhombus;html=1;strokeColor=none;fillColor=%s;"
BANDA = "rounded=0;html=1;strokeColor=none;fillColor=#FDE8DA;"
REJ = "rounded=0;html=1;strokeColor=none;fillColor=#C7C7C7;"
TXTC = TEXT + "align=center;"
C_DES, C_MB, C_OPE, C_CERT, C_PUNTO = "#555555", "#E8641B", "#BBBBBB", "#111111", "#111111"
# Congelamientos del Caso (RT-10.05): septiembre = mes 8 + 12k; diciembre = mes 11 + 12k
CONGELADOS = [m for k in range(5) for m in (8 + 12 * k, 11 + 12 * k) if m <= 56]


def leyenda(d, y, items):
    x = 0
    for txt, estilo in items:
        d.box("", x, y + 5, 14, 12, estilo)
        w = 9 + 7 * len(txt)
        d.box(txt, x + 18, y, w, 22, TEXT)
        x += 18 + w + 10
        if x > 470:
            x = 0
            y += 22
    return y + 22


def fig9():
    """Vista general de los 56 meses: fases, certificaciones, hitos y cada
    prueba periodica de la Operacion en su mes."""
    d = Diagram("Fig_9-9_Calidad_Cronograma")
    LW, PX, RH = 186, 7.4, 26
    X0 = LW + 6

    def mx(m):
        return X0 + (m - 1) * PX

    filas = 12
    yA = 44
    alto = filas * RH
    for m in CONGELADOS:                      # bandas de congelamiento al fondo
        d.box("", mx(m), yA - 4, PX, alto + 4, BANDA)
    for etq, m in (("2027", 1), ("2028", 12), ("2029", 24), ("2030", 36), ("2031", 48)):
        d.box(etq, mx(m) + 2, 0, 44, 20, TEXT)
        d.box("", mx(m), 20, 0.6, alto + 24, REJ)
    for m in (1, 13, 21, 32, 44, 56):          # meses de referencia
        d.box(str(m), mx(m) - 6, 20, 20, 20, TXTC)
    d.box("mes", 0, 20, LW, 20, TEXT + "fontColor=#5F5F5F;")

    def fila(i, rotulo):
        y = yA + i * RH
        d.box(rotulo, 0, y, LW, 22, TEXT)
        return y

    y = fila(0, "Etapa 1")
    d.box("", mx(1), y + 4, 12 * PX, 14, BAR % C_DES)
    d.box("", mx(13), y + 4, 3 * PX, 14, BAR % C_MB)
    d.box("", mx(16), y + 4, 5 * PX, 14, BAR % C_OPE)
    y = fila(1, "Etapa 2")
    d.box("", mx(13), y + 4, 6 * PX, 14, BAR % C_DES)
    d.box("", mx(19), y + 4, 2 * PX, 14, BAR % C_MB)
    y = fila(2, "Operación (36 meses)")
    d.box("", mx(21), y + 4, 36 * PX, 14, BAR % C_OPE)
    y = fila(3, "Certificación y cierre documental")
    for a, b in ((9, 11), (16, 17)):
        d.box("", mx(a), y + 4, (b - a + 1) * PX, 14, BAR % C_CERT)
    y = fila(4, "Hitos H1 a H12")
    for m in (2, 4, 6, 10, 12, 13, 14, 16, 17, 18, 19, 21):
        d.box("", mx(m), y + 5, PX, 12, DIAM % C_PUNTO)
    y = fila(5, "Recuperación (8.1.3)")
    for m in (21, 27, 33, 39, 45, 51, 54):
        d.box("", mx(m) - 2, y + 4, PX + 4, 14, DIAM % C_PUNTO)
    y = fila(6, "Resiliencia (8.2.2)")
    for m in (26, 32, 38, 44, 50, 55):
        d.box("", mx(m) - 2, y + 4, PX + 4, 14, DIAM % C_PUNTO)
    y = fila(7, "Intrusión (8.2.2)")
    for m in (28, 40, 52):
        d.box("", mx(m) - 2, y + 4, PX + 4, 14, DIAM % C_PUNTO)
    y = fila(8, "Restauración mensual")
    d.box("", mx(13), y + 8, 44 * PX, 6, BAR % C_PUNTO)
    y = fila(9, "Puertas automáticas")
    d.box("", mx(6), y + 8, 51 * PX, 6, BAR % C_PUNTO)

    y = fila(10, "Banco y mapeo de frío")
    d.box("", mx(3), y + 4, 2 * PX, 14, BAR % C_CERT)
    y = fila(11, "Piloto de frío (4.1.4)")
    d.box("", mx(10), y + 4, 2 * PX, 14, BAR % C_CERT)

    leyenda(d, yA + alto + 10, [
        ("Desarrollo", BAR % C_DES), ("Marcha blanca", BAR % C_MB),
        ("Producción y Operación", BAR % C_OPE), ("Certificación", BAR % C_CERT),
        ("Hito o prueba puntual", DIAM % C_PUNTO), ("Congelamiento (sep. y dic.)", BANDA),
    ])
    d.save()


def fig10():
    """Detalle de la implementacion (meses 1 a 21) a escala mensual."""
    d = Diagram("Fig_9-10_Calidad_Implementacion")
    LW, PX, RH = 210, 18, 24
    X0 = LW + 4

    def mx(m):
        return X0 + (m - 1) * PX

    filas = [
        ("1.2.4 · 1.5.1 Matriz y plan", [(2, 2)]),
        ("2.6.1–2.6.3 Usabilidad", [(2, 4)]),
        ("2.4.3–2.4.4 Banco y mapeo frío", [(3, 4)]),
        ("4.1.4 Piloto de frío", [(10, 11)]),
        ("3.10.2 INN-02", [(2, 15)]),
        ("1.5.2 Puertas automáticas", [(6, 20)]),
        ("3.7.2–3.7.5 Migración y corte", [(9, 12)]),
        ("3.8.1 Integración E1", [(9, 9)]),
        ("3.8.2–3.8.8 Pruebas y acta E1", [(9, 11)]),
        ("Evaluadores subcontratados", [(9, 12), (16, 18)]),
        ("4.1.2 Ensayo de reversión", [(11, 11)]),
        ("4.2.1 Marcha blanca E1", [(13, 15)]),
        ("3.9.1 Integración E2", [(16, 16)]),
        ("3.9.2–3.9.7 Certificación E2", [(16, 17)]),
        ("4.3.1 Marcha blanca E2", [(19, 20)]),
    ]
    yA = 66
    n = len(filas) + 2                         # + restauracion + hitos
    alto = n * RH + 24
    for m in (8, 11, 20):                      # sep-2027, dic-2027, sep-2028
        d.box("", mx(m), yA - 4, PX, alto, BANDA)
    # encabezado: ano, inicial del mes y numero de mes (mes 1 = febrero de 2027)
    d.box("2027", mx(1), 0, 11 * PX, 20, TXTC + "fontStyle=1;")
    d.box("2028", mx(12), 0, 10 * PX, 20, TXTC + "fontStyle=1;")
    d.box("", mx(12), 0, 0.8, alto + yA - 4, REJ)
    iniciales = "FMAMJJASONDEFMAMJJASO"
    for m in range(1, 22):
        d.box(iniciales[m - 1], mx(m), 20, PX, 20, TXTC)
        d.box(str(m), mx(m) - 2, 40, PX + 4, 20, TXTC + "fontColor=#5F5F5F;")
    d.box("mes del contrato", 0, 40, LW, 20, TEXT + "fontColor=#5F5F5F;")

    for i, (rot, tramos) in enumerate(filas):
        y = yA + i * RH
        d.box(rot, 0, y, LW, 22, TEXT)
        es_mb = "Marcha blanca" in rot
        es_cert = "Certificación" in rot
        color = C_MB if es_mb else (C_CERT if es_cert else C_DES)
        for a, b in tramos:
            d.box("", mx(a) + 1, y + 4, (b - a + 1) * PX - 2, 14, BAR % color)
    y = yA + len(filas) * RH
    d.box("Restauración de respaldos", 0, y, LW, 22, TEXT)
    for m in range(13, 21):
        d.box("", mx(m) + 3, y + 5, PX - 6, 12, DIAM % C_PUNTO)
    y += RH
    d.box("Hitos del E-25", 0, y + 6, LW, 22, TEXT)
    hitos = [("H1", 2), ("H2", 4), ("H3", 6), ("H4", 10), ("H5", 12), ("H6", 13),
             ("H8", 14), ("H7", 16), ("H9", 17), ("H10", 18), ("H11", 19), ("H12", 21)]
    for k, (h, m) in enumerate(hitos):
        d.box("", mx(m) + 3, y + 12, PX - 6, 12, DIAM % C_PUNTO)
        ty = y - 6 if k % 2 == 0 else y + 26
        d.box(h, mx(m) - 8, ty, PX + 16, 18, TXTC)

    leyenda(d, yA + alto + 8, [
        ("Paquete de calidad", BAR % C_DES), ("Certificación", BAR % C_CERT),
        ("Marcha blanca", BAR % C_MB), ("Hito o restauración", DIAM % C_PUNTO),
        ("Congelamiento", BANDA),
    ])
    d.save()


def fig10v():
    """Detalle de la implementacion en vertical: una fila por mes (1 a 21)."""
    d = Diagram("Fig_9-10_Calidad_Implementacion_vertical")
    CM, CF, CA, CH = 104, 128, 316, 52        # anchos: mes, fase, actividades, hito
    X = [0, CM, CM + CF, CM + CF + CA]
    W = CM + CF + CA + CH
    CAB = TEXT + "fontStyle=1;verticalAlign=middle;"
    for x, w, t in zip(X, (CM, CF, CA, CH), ("Mes", "Fase del contrato", "Actividades de calidad (paquete EDT)", "Hito")):
        d.box(t, x + 4, 0, w - 4, 24, CAB)
    d.box("", 0, 25, W, 1.2, "rounded=0;html=1;strokeColor=none;fillColor=#111111;")
    meses = ["feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic", "ene",
             "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct"]
    fase = {**{m: "E1 · desarrollo" for m in range(1, 13)},
            **{m: "E1 · marcha blanca<br>E2 · desarrollo" for m in (13, 14, 15)},
            **{m: "E1 · producción<br>E2 · desarrollo" for m in (16, 17, 18)},
            19: "E2 · marcha blanca", 20: "E2 · marcha blanca", 21: "Operación"}
    act = {
        1: "—",
        2: "Matriz de trazabilidad (1.2.4) · plan de calidad y de pruebas (1.5.1) · investigación con usuarios (2.6.1) · inicio de INN-02 (3.10.2)",
        3: "Prototipos y usabilidad (2.6.2) · banco de frío (2.4.3) · INN-02",
        4: "Indicadores de usabilidad (2.6.3) · mapeo de frío (2.4.4) · INN-02",
        5: "INN-02",
        6: "Puertas automáticas activas (1.5.2) · INN-02",
        7: "Puertas automáticas · INN-02",
        8: "Puertas automáticas · INN-02",
        9: "Integración y regresión E1 (3.8.1) · inicio de la certificación E1 (3.8.2–3.8.8) · ensayo de migración 1 (3.7.2) · evaluadores",
        10: "Cierre de pruebas E1 · expediente (3.8.7) · piloto de frío (4.1.4) · evaluadores",
        11: "Entrega documental H5 (3.8.7) · piloto sin cambios productivos · reversión y migración en Preproducción · evaluadores",
        12: "Acta de conciliación y corte (3.7.5) · evaluadores",
        13: "Marcha blanca E1 con indicadores diarios (4.2.1) · restauración mensual",
        14: "Acta H8 del diseño entregado en febrero · marcha blanca E1 · restauración mensual",
        15: "Marcha blanca E1 · restauración mensual · cierre de INN-02 (3.10.2.4)",
        16: "Integración y regresión E2 (3.9.1) · certificación E2 (3.9.2–3.9.7) · restauración mensual · evaluadores",
        17: "Acta de certificación E2 (3.9.6) · restauración mensual · evaluadores",
        18: "Restauración mensual · evaluadores",
        19: "Marcha blanca E2 en convivencia (4.3.1) · restauración mensual",
        20: "Marcha blanca E2 con el peak de septiembre · restauración mensual",
        21: "Inicio de la Operación · primera recuperación con conmutación real (8.1.3) · restauración (8.1.6)",
    }
    hito = {2: "H1", 4: "H2", 6: "H3", 10: "H4", 12: "H5", 13: "H6", 14: "H8", 16: "H7",
            17: "H9", 18: "H10", 19: "H11", 21: "H12"}
    congelado = {8, 11, 20}
    helv = pymupdf.Font("helv")

    def lineas_de(txt, ancho):
        n, linea = 1, ""
        for w in txt.split(" "):
            prueba = (linea + " " + w).strip()
            if helv.text_length(prueba, fontsize=13) > ancho and linea:
                n, linea = n + 1, w
            else:
                linea = prueba
        return n
    y = 30
    LIN = 16                                  # alto de linea a 13 px
    for m in range(1, 22):
        lin_act = lineas_de(act[m], CA - 16)
        lineas = max(lin_act, 2 if "<br>" in fase[m] else 1, 2 if m in congelado else 1)
        h = lineas * LIN + 6
        if m in congelado:
            d.box("", 0, y, W, h, BANDA)
        año = "2027" if m <= 11 else "2028"
        etiqueta = f"<b>{m}</b> · {meses[m - 1]} {año}" + ("<br><i>congelamiento</i>" if m in congelado else "")
        d.box(etiqueta, X[0] + 4, y, CM - 4, h, TEXT)
        d.box(fase[m], X[1] + 4, y, CF - 4, h, TEXT)
        d.box(act[m], X[2] + 4, y, CA - 8, h, TEXT)
        if m in hito:
            d.box(f"<b>{hito[m]}</b>", X[3] + 4, y, CH - 4, h, TEXT)
        y += h
        d.box("", 0, y, W, 0.6, REJ)
    d.save()


if __name__ == "__main__":
    pedidas = set(sys.argv[2:])
    for f in (fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig10v):
        if not pedidas or f.__name__ in pedidas:
            f()
