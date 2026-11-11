"""Genera el kit visual del video LafroX (1920x1080 PNG) a partir de plantillas HTML.

Uso:  python generar_visuales.py            -> todas las piezas
      python generar_visuales.py rotulo     -> solo las que contienen "rotulo" en el nombre
Requisitos: Python 3 y Google Chrome (o Edge). Las tipografías (Archivo e IBM Plex Mono, licencia OFL)
están en fuente/fonts, por lo que no se necesita internet.

Identidad, contacto, casos y stack tomados de: sitio oficial https://lafrox.github.io/ (repo lafrox/lafrox.github.io),
T-12 y SD4 (rama LafroX-Subdoc4-LateX-corrigiendo, 09-11-2026) y T-19 (SD13, 09-11-2026).
Para cambiar textos (años de experiencia, fecha, certificaciones) edite CONFIGURACIÓN y vuelva a ejecutar.
"""
import os, sys, subprocess, shutil, tempfile, unicodedata, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lafrox_brand as B

# ============================ CONFIGURACIÓN ============================
WEB = "lafrox.github.io"                 # sitio declarado en el T-12 (RT-23.05 / RT-23.06)
CORREO = "contacto@lafrox.cl"            # sitio web, sección Contacto
TELEFONO = "+56 32 250 4100"             # sitio web, sección Contacto
FECHA = "[fecha de la propuesta]"        # PENDIENTE: fecha real de la Propuesta Final
PROYECTO = "Plataforma de trazabilidad, promesa de entrega y costo de servir"  # PENDIENTE: confirmar nombre oficial
SLOGAN = "Donde se pierde la señal, no se pierde el dato."  # slogan único del video (v05)

# nombre, cargo (AGENTS.md / traslado SD12), años, especialización, certificaciones.
# PENDIENTE (equipo, T-8): años de experiencia y certificaciones. Hoy el CSV del equipo y el sitio web
# se contradicen en 6 de 8 personas; aquí se mantiene el CSV hasta que el T-8 fije una sola versión.
EQUIPO = [
    ("Alex Aravena", "Jefe de Proyecto", "[__]", "Dirección de proyectos TI", ["PMP", "CSM"]),
    ("Leandro Chamorro", "Líder de Datos", "[__]", "Modelo de datos y costo de servir", ["CKAD"]),
    ("Patricio Henríquez", "Líder de Implantación y Gestión del Cambio", "[__]", "Adopción en terreno y capacitación", []),
    ("Maximiliano Miño", "Líder de Calidad", "[__]", "Aseguramiento de calidad y pruebas", []),
    ("Bastián Trejo", "Arquitecto de Solución", "[__]", "Arquitectura híbrida e integración", ["AWS Solutions Architect – Professional"]),
    ("Tomás Pérez", "Líder de Desarrollo", "[__]", "Laravel y móvil Kotlin offline-first", ["CKAD"]),
    ("Guillermo Castillo", "Líder de Operación / SRE", "[__]", "Alta disponibilidad, NOC y niveles de servicio", []),
    ("Álvaro Catalán", "Encargado de Seguridad de la Información", "[__]", "Seguridad Zero Trust y cumplimiento", ["CISSP", "CEH"]),
]
# ======================================================================

AQUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(AQUI, "..", "png"))
LOGO_DIR = os.path.normpath(os.path.join(AQUI, "..", "logo"))
HTML_DIR = os.path.join(AQUI, "html")
e = H.escape
N, P, O = B.NARANJA, B.PANEL, B.NEGRO

CSS = B.FONT_CSS + f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1920px;height:1080px;overflow:hidden;font-family:'Archivo',sans-serif;color:{B.BLANCO}}}
body.trans{{background:transparent}} body.dark{{background:{O}}}
.k{{font-family:'IBM Plex Mono',monospace;color:{N};font-weight:600;letter-spacing:.14em;text-transform:uppercase;font-size:24px}}
.t{{font-weight:900;font-size:66px;line-height:1.08;margin-top:12px;letter-spacing:-.02em}}
.bar{{width:120px;height:8px;background:{N};margin:26px 0 0;border-radius:4px}}
.wrap{{position:absolute;left:120px;right:120px;top:150px}}
.src{{position:absolute;left:120px;bottom:90px;font-family:'IBM Plex Mono';font-size:18px;color:{B.TEXTO_TENUE}}}
.card{{background:{P};border:1px solid rgba(255,255,255,.12);border-top:6px solid {N};border-radius:18px;padding:32px 30px}}
.card h3{{font-size:32px;font-weight:800;margin-bottom:14px;letter-spacing:-.01em}}
.card p{{font-size:25px;line-height:1.35;color:{B.TEXTO_SUAVE}}}
.num{{color:{N};font-weight:900}}
.grid{{display:grid;gap:28px}}
.chip{{display:inline-block;border:2px solid {N};color:{B.BLANCO};padding:10px 22px;border-radius:999px;font-weight:600;font-size:25px;margin:0 14px 16px 0}}
.panel{{position:absolute;right:60px;top:150px;background:rgba(11,13,18,.92);border:1px solid rgba(255,255,255,.12);border-left:8px solid {N};border-radius:18px;padding:36px 40px}}
"""


def page(body, trans=False):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="{'trans' if trans else 'dark'}">{body}</body></html>"""


def logo_at(x, y, alto, sub=True, centrado=False):
    pos = f"left:0;right:0;text-align:center" if centrado else f"left:{x}px"
    return f'<div style="position:absolute;{pos};top:{y}px">{B.html_logo(alto, True, sub)}</div>'


def titulo(k, t):
    return f'<div class="k">{e(k)}</div><div class="t">{t}</div><div class="bar"></div>'


PIEZAS = {}


def pieza(nombre, body, trans=False):
    PIEZAS[nombre] = (page(body, trans), trans)


# ---------- 00 Capa de marca permanente (RT-24.05) ----------
pieza("00_capa_marca_permanente", f"""
{logo_at(48, 32, 52)}
<div style="position:absolute;right:48px;top:40px;text-align:right;font-family:'IBM Plex Mono';font-size:19px;font-weight:600;line-height:1.55;
 letter-spacing:.06em;text-shadow:0 1px 4px rgba(0,0,0,.6)">LICITACIÓN TFEP-01/2026<br><span style="color:{N}">CASO 02 · LOGÍSTICA · DISTRIBUIDORA PUELCHE</span></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:60px;background:rgba(11,13,18,.9);border-top:3px solid {N};
 display:flex;align-items:center;justify-content:center;gap:44px;font-size:23px;font-weight:600">
 <span>{e(WEB)}</span><span style="color:{N}">●</span><span>{e(CORREO)}</span><span style="color:{N}">●</span><span>{e(TELEFONO)}</span></div>
""", trans=True)

# ---------- 01 Escena 1: placa de título ----------
pieza("01_E1_placa_titulo", f"""
{logo_at(0, 190, 150, centrado=True)}
<div style="position:absolute;left:0;right:0;top:420px;text-align:center">
 <div class="k" style="font-size:28px">Propuesta técnico-económica</div>
 <div style="font-size:56px;font-weight:900;margin:22px 160px 0;line-height:1.12;letter-spacing:-.02em">{e(PROYECTO)}</div>
 <div style="font-size:34px;font-weight:500;margin-top:30px">Licitación TFEP-01/2026 · Caso 02 — Logística · Distribuidora Puelche S.A.</div>
 <div style="font-size:30px;margin-top:34px;color:{B.TEXTO_SUAVE}">Proponente: <b style="color:#fff">LafroX SpA</b> &nbsp;|&nbsp; {e(FECHA)}</div>
</div>""")

# ---------- 02 Escena 2: cifras del problema ----------
CIFRAS = [
    ("02_E2_cifra_1_lote", "41 %", "de las recepciones del producto retirado no tenía lote registrado",
     "<span class='num'>9 días</span> para identificar a los clientes afectados… y fue una estimación"),
    ("02_E2_cifra_2_perdida", "$31 millones", "de pérdida directa por el retiro sanitario de marzo de 2026",
     "<span class='num'>6 meses</span> fuera de un proveedor que es el <span class='num'>6 %</span> de las ventas"),
    ("02_E2_cifra_3_otif", "82,4 %", "de entregas completas y a tiempo (OTIF) · referencia: sobre 95 %",
     "<span class='num'>1,1 %</span> de guías perdidas al mes · <span class='num'>12 días</span> para resolver un reclamo"),
    ("02_E2_cifra_4_competencia", "7,8 %", "de quiebre de stock detectado recién en la preventa",
     "Un competidor ya ofrece autoservicio y entrega en <span class='num'>24 horas</span>; Puelche tarda 48 a 72"),
]
for n, big, lab, sub in CIFRAS:
    pieza(n, f"""<div class="wrap" style="top:250px">
 <div class="num" style="font-size:210px;line-height:1;letter-spacing:-.03em">{e(big)}</div>
 <div style="font-size:50px;font-weight:800;margin-top:24px;max-width:1500px;letter-spacing:-.01em">{e(lab)}</div>
 <div style="font-size:36px;margin-top:36px;color:{B.TEXTO_SUAVE}">{sub}</div></div>
<div class="src">Fuente: Bases Técnicas Caso 02 — Logística, Capítulo 7</div>""")

pieza("02_E2_personas_afectadas", f"""<div class="wrap">{titulo('Impacto en las personas', 'Detrás de cada cifra hay alguien')}
<div class="grid" style="grid-template-columns:repeat(4,1fr);margin-top:56px">
 <div class="card"><h3>Jefa de calidad</h3><p><span class="num">9 días</span> buscando en carpetas y llamando conductores para un retiro sanitario.</p></div>
 <div class="card"><h3>Preparador</h3><p>Turnos de <span class="num">30 min</span> a <span class="num">−22 °C</span>, sin señal y con planillas de papel.</p></div>
 <div class="card"><h3>Conductor</h3><p>Guías en papel y efectivo sin respaldo: <span class="num">$4,2 M</span> de diferencias al mes.</p></div>
 <div class="card"><h3>Almacenero</h3><p>Pide sin ver stock y espera <span class="num">48 a 72 h</span>; a veces recibe producto vencido.</p></div>
</div></div><div class="src">Fuente: Bases Técnicas Caso 02 — Logística, Capítulos 5 y 7</div>""")

# ---------- 03 Escena 3: solución ----------
pieza("03_E3_beneficios", f"""<div class="wrap">{titulo('Beneficios por grupo de interés', 'Cada actor gana algo concreto')}
<div class="grid" style="grid-template-columns:repeat(4,1fr);margin-top:56px">
 <div class="card"><h3>Almacenero</h3><p>Ve el stock, pide cuando quiere y sabe cuándo le llega.</p></div>
 <div class="card"><h3>Conductor y preventista</h3><p>App de una mano que funciona sin señal.</p></div>
 <div class="card"><h3>Calidad y autoridad sanitaria</h3><p>Clientes afectados por un lote en minutos, no en días.</p></div>
 <div class="card"><h3>Gerencia y finanzas</h3><p>Costo de servir real por cliente y por entrega.</p></div>
</div></div>""")

pieza("03_E3_diferenciadores", f"""<div class="wrap">{titulo('Diferenciadores clave', 'Lo que nos hace distintos')}
<div class="grid" style="grid-template-columns:repeat(2,1fr);margin-top:56px">
 <div class="card"><h3>Funciona sin señal</h3><p>Aplicaciones offline-first: registran pedido, entrega y lote, y sincronizan solas.</p></div>
 <div class="card"><h3>La bodega nunca se detiene</h3><p>Arquitectura híbrida: núcleo local en Talca, nube AWS para escala y respaldo.</p></div>
 <div class="card"><h3>Trazabilidad con estándar</h3><p>Lote a lote con GS1 y eventos EPCIS 2.0, desde el andén hasta la firma del cliente.</p></div>
 <div class="card"><h3>Costo de servir por entrega</h3><p>Se acaba el prorrateo por zona de 2016: decisiones con datos reales.</p></div>
</div></div>""")

INNOV = [("INN-01", "Producto o servicio", "Seguimiento de vencimiento posentrega en el local"),
         ("INN-02", "Proceso", "Reproducción de incidentes de terreno"),
         ("INN-03", "Tecnológica", "Vida útil remanente por historia térmica del lote"),
         ("INN-04", "Modelo de negocio", "Tramo variable de la Operación ligado al costo de servir"),
         ("INN-05", "Impacto social", "Hoja de negocio del almacenero")]
pieza("03_E3_innovaciones", f"""<div class="wrap">{titulo('Cinco innovaciones · Formulario T-19', 'Innovación en cada frente')}
<div class="grid" style="grid-template-columns:repeat(5,1fr);margin-top:56px">""" + "".join(
    f'<div class="card" style="min-height:420px"><div class="num" style="font-size:44px;line-height:1">{n}</div>'
    f'<div class="k" style="font-size:19px;margin:16px 0">{e(t)}</div><p style="color:#fff;font-weight:700;font-size:27px">{e(d)}</p></div>'
    for n, t, d in INNOV) + "</div></div><div class='src'>Fuente: Formulario T-19, Subdocumento 13</div>")

METAS = [("OTIF", "82,4 %", "> 95 %"), ("Fill rate", "91,3 %", "> 97 %"), ("Guías perdidas", "1,1 %", "0"),
         ("Reentregas", "4,2 %", "< 1 %")]
pieza("03_E3_resultados_lateral", f"""<div class="panel" style="width:640px">
 <div class="k" style="font-size:21px">Resultados esperados</div>""" + "".join(
    f'<div style="margin-top:24px"><div style="font-size:26px;font-weight:700">{e(a)}</div>'
    f'<div style="font-size:46px;font-weight:900"><span style="color:{B.TEXTO_TENUE}">{e(b)}</span> <span class="num">→ {e(c)}</span></div></div>'
    for a, b, c in METAS) + f"""
 <div style="font-family:'IBM Plex Mono';font-size:16px;color:{B.TEXTO_TENUE};margin-top:26px">Línea base: Caso 02, Cap. 7 · Meta: referencia del caso</div></div>""", trans=True)

# ---------- 04 Escena 4: tecnología ----------
def bloque(t, s, borde=N, w=None):
    st = f"width:{w}px;" if w else ""
    return (f'<div style="{st}background:{P};border:3px solid {borde};border-radius:14px;padding:16px 20px;text-align:center">'
            f'<div style="font-size:26px;font-weight:800">{e(t)}</div><div style="font-size:19px;color:{B.TEXTO_SUAVE};margin-top:6px">{e(s)}</div></div>')

USUARIOS = f"""<div style="position:absolute;left:120px;right:120px;top:150px;display:flex;gap:28px;justify-content:center">
 {bloque('Almacenero', 'Portal y hoja de negocio', '#5B6470', 380)}{bloque('Preventista · Conductor', 'App Kotlin offline en Zebra', '#5B6470', 420)}
 {bloque('Proveedores y cadenas', 'EDI GS1 · EPCIS 2.0', '#5B6470', 380)}{bloque('Sensores de frío', 'Telemetría IoT', '#5B6470', 330)}</div>"""
NUBE = f"""<div style="position:absolute;left:120px;right:120px;top:330px;border:3px dashed {N};border-radius:18px;padding:46px 30px 26px">
 <div style="position:absolute;top:-20px;left:30px;background:{O};padding:0 16px" class="k">Nube AWS</div>
 <div style="display:flex;gap:18px;justify-content:center;flex-wrap:wrap">
 {bloque('CloudFront + WAF', 'Entrada protegida')}{bloque('API Gateway', 'Contratos y cuotas')}{bloque('ECS Fargate', 'Laravel 13 · Horizon')}
 {bloque('Aurora PostgreSQL', 'OLTP y réplica DRP')}{bloque('Keycloak', 'Identidad OIDC')}{bloque('DynamoDB · IoT Core', 'Telemetría de frío')}
 {bloque('S3 · Redshift · QuickSight', 'Analítica y respaldo inmutable')}</div></div>"""
ONPREM = f"""<div style="position:absolute;left:120px;right:120px;top:700px;border:3px solid #5B6470;border-radius:18px;padding:46px 30px 26px">
 <div style="position:absolute;top:-20px;left:30px;background:{O};padding:0 16px;color:{B.TEXTO_SUAVE}" class="k">On-premise · operación</div>
 <div style="display:flex;gap:22px;justify-content:center">
 {bloque('CD Talca', 'WMS maestro + PostgreSQL', '#5B6470', 420)}{bloque('Borde Concepción', 'Autonomía local', '#5B6470', 420)}
 {bloque('3 cross-docking', 'Gabinetes de borde', '#5B6470', 380)}{bloque('Enlaces', 'Fibra · LTE · Starlink', '#5B6470', 340)}</div></div>
<div style="position:absolute;left:950px;top:660px;font-family:'IBM Plex Mono';font-size:19px;color:{N};font-weight:600">⇅ ENLACE CIFRADO · RÉPLICA DE DATOS CRÍTICOS</div>"""
pieza("04_E4_arquitectura_paso1", USUARIOS)
pieza("04_E4_arquitectura_paso2", USUARIOS + NUBE)
pieza("04_E4_arquitectura_paso3", USUARIOS + NUBE + ONPREM)

STACK = [("Móvil", "Android nativo (Kotlin) en terminales Zebra · base local SQLite cifrada · sincronización offline"),
         ("Aplicación", "Monolito modular Laravel 13 (PHP 8.5) · colas con Horizon y Redis · contenedores Docker"),
         ("Datos", "PostgreSQL + PostGIS on-premise · Aurora PostgreSQL · DynamoDB · S3 + Redshift + QuickSight"),
         ("Integración", "Amazon API Gateway · RabbitMQ local · Amazon SQS · EDI GS1 · eventos EPCIS 2.0 · DTE SII"),
         ("Seguridad", "Keycloak (OIDC) · AWS WAF · confianza cero · cifrado en reposo y TLS en tránsito"),
         ("Infraestructura", "AWS ECS Fargate · CD Talca + borde en Concepción y cross-docks · fibra + LTE + Starlink"),
         ("Operación", "OpenTelemetry · Amazon CloudWatch · NOC 24/7 · infraestructura como código (Terraform)")]
pieza("04_E4_stack_tecnologico", f"""<div class="wrap" style="top:140px">{titulo('Conjunto tecnológico completo', 'Stack de la solución')}
<div style="margin-top:34px">""" + "".join(
    f'<div style="display:flex;border-bottom:1px solid rgba(255,255,255,.12);padding:15px 0"><div style="width:300px;color:{N};font-weight:800;font-size:28px">{e(a)}</div>'
    f'<div style="font-size:27px;flex:1">{e(b)}</div></div>' for a, b in STACK)
    + "</div></div><div class='src'>Fuente: Subdocumento 4 — Arquitectura (versión del 09-11-2026)</div>")

pieza("04_E4_seguridad_lateral", f"""<div class="panel" style="width:620px">
 <div class="k" style="font-size:21px">Seguridad y cumplimiento</div><div style="margin-top:26px">""" + "".join(
    f'<span class="chip">{e(c)}</span>' for c in
    ["Zero Trust", "ISO/IEC 27001:2022", "Ley 21.719 · datos personales", "Ley 19.799 · firma electrónica", "Cifrado en reposo y en tránsito"]) + "</div></div>", trans=True)

# ---------- 05 Escena 5: ventajas ----------
TW, PH, LH, GX, GY, X0, Y0 = 420, 250, 150, 24, 24, 84, 140
mask_holes, labels = [], []
for i, (n, c, a, esp, certs) in enumerate(EQUIPO):
    col, row = i % 4, i // 4
    x, y = X0 + col * (TW + GX), Y0 + row * (PH + LH + GY)
    mask_holes.append(f'<rect x="{x}" y="{y}" width="{TW}" height="{PH}" rx="18" fill="black"/>')
    cert = " · ".join(certs)
    labels.append(f'<div style="position:absolute;left:{x}px;top:{y+PH}px;width:{TW}px;height:{LH}px;background:{P};'
                  f'border-top:5px solid {N};padding:12px 16px;line-height:1.3">'
                  f'<div style="font-size:23px;font-weight:800">{e(n)}</div>'
                  f'<div style="font-size:17px;color:{N};font-weight:700">{e(c)}</div>'
                  f'<div style="font-size:16px">{e(a)} años · {e(esp)}</div>'
                  f'<div style="font-family:\'IBM Plex Mono\';font-size:14px;color:{B.TEXTO_TENUE}">{e(cert)}</div></div>')
pieza("05_E5_mosaico_equipo", f"""
<svg width="1920" height="1080" style="position:absolute;left:0;top:0"><defs><mask id="m">
<rect width="1920" height="1080" fill="white"/>{''.join(mask_holes)}</mask></defs>
<rect width="1920" height="1080" fill="{O}" mask="url(#m)"/></svg>
{''.join(labels)}""", trans=True)

CASOS = [("LogiNacional S.A.", "Logística · consumo masivo · 2021–2022",
          "Sistema híbrido de reparto con ERP y facturación en ruta, en AWS y 14 centros de distribución con borde.",
          [("420", "camiones"), ("22.000", "entregas diarias")]),
         ("FarmaRed S.A.", "Cadena de frío · farmacéutica · 2022–2023",
          "Telemetría y cadena de frío IoT: cámaras a −22 °C y flota refrigerada con alertas normativas.",
          [("180", "vehículos refrigerados"), ("12 M", "registros térmicos/mes")]),
         ("Lácteos del Sur S.A.", "Preventa · alimentos perecibles · 2023–2024",
          "Preventa y ruteo sin conexión: persistencia local cifrada, sincronización y crédito comercial.",
          [("280", "preventistas"), ("18.000", "transacciones diarias")])]
pieza("05_E5_casos_exito", f"""<div class="wrap">{titulo('Experiencia · desde 2012', 'Casos de éxito en operación continua')}
<div class="grid" style="grid-template-columns:repeat(3,1fr);margin-top:50px">""" + "".join(
    f'<div class="card" style="min-height:470px"><div class="k" style="font-size:17px">{e(sec)}</div>'
    f'<h3 style="font-size:36px;margin-top:12px">{e(nom)}</h3><p>{e(desc)}</p><div style="display:flex;gap:30px;margin-top:22px">'
    + "".join(f'<div><div class="num" style="font-size:46px">{e(v)}</div><div style="font-size:19px;color:{B.TEXTO_SUAVE}">{e(l)}</div></div>' for v, l in st)
    + '</div></div>' for nom, sec, desc, st in CASOS)
    + f"</div></div><div class='src'>Fuente: sitio oficial {e(WEB)} y Formulario T-6 (Subdocumento 1) · contrapartes autorizadas, contacto bajo solicitud</div>")

pieza("05_E5_compromisos_lateral", f"""<div class="panel" style="width:640px">
 <div class="k" style="font-size:21px">Garantías y compromisos</div><div style="margin-top:26px">""" + "".join(
    f'<span class="chip">{e(c)}</span>' for c in ["56 meses de contrato", "Híbrido nube + on-premise", "Sin dependencia de un proveedor",
                                                  "Niveles de servicio por hito", "ISO 9001 · ISO/IEC 20000-1 · CMMI-DEV 3"]) + "</div></div>", trans=True)

# ---------- 06 Escena 6: cierre ----------
glab = "".join(
    f'<div style="background:rgba(11,13,18,.92);border-top:4px solid {N};border-radius:10px;padding:8px 12px;line-height:1.25">'
    f'<div style="font-size:18px;font-weight:800">{e(n)}</div><div style="font-size:14px;color:{N};font-weight:700">{e(c)}</div>'
    f'<div style="font-size:13px">{e(a)} años · {e(esp)}</div></div>' for n, c, a, esp, _ in EQUIPO)
pieza("06_E6_rotulos_plano_grupal", f"""
<div style="position:absolute;left:48px;right:48px;bottom:84px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px">{glab}</div>""", trans=True)

pieza("06_E6_placa_final", f"""
{logo_at(0, 200, 170, centrado=True)}
<div style="position:absolute;left:0;right:0;top:480px;text-align:center">
 <div style="font-size:48px;font-weight:900;margin:0 220px;line-height:1.18;letter-spacing:-.02em">{e(SLOGAN)}</div>
 <div style="width:160px;height:8px;background:{N};margin:40px auto;border-radius:4px"></div>
 <div style="font-size:40px;font-weight:800">{e(WEB)}</div>
 <div style="font-size:32px;margin-top:16px">{e(CORREO)} &nbsp;·&nbsp; {e(TELEFONO)}</div>
 <div style="font-family:'IBM Plex Mono';font-size:22px;margin-top:40px;color:{B.TEXTO_TENUE};letter-spacing:.06em">LAFROX SPA · LICITACIÓN TFEP-01/2026 · CASO 02 — LOGÍSTICA · DISTRIBUIDORA PUELCHE S.A.</div>
</div>""")

# ---------- Rótulos individuales (RT-24.02 / RT-24.03) ----------
def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return "_".join(s.split())

for i, (n, c, a, esp, certs) in enumerate(EQUIPO, 1):
    certs_html = "".join(f'<span style="display:inline-block;border:2px solid {N};border-radius:999px;padding:4px 16px;'
                         f'font-family:\'IBM Plex Mono\';font-size:19px;font-weight:600;margin:12px 10px 0 0">{e(x)}</span>' for x in certs)
    pieza(f"rotulo_{i:02d}_{slug(n)}", f"""
<div style="position:absolute;left:80px;bottom:100px;min-width:760px;max-width:1100px;background:rgba(11,13,18,.93);
 border-left:12px solid {N};border-radius:0 18px 18px 0;padding:22px 36px 24px">
 <div style="font-size:48px;font-weight:900;text-transform:uppercase;letter-spacing:.01em">{e(n)}</div>
 <div style="font-size:28px;font-weight:700;color:{N};margin-top:4px">{e(c)} · {e(a)} años de experiencia</div>
 <div style="font-size:26px;margin-top:6px;color:{B.TEXTO_SUAVE}">{e(esp)}</div>{('<div>' + certs_html + '</div>') if certs else ''}
</div>""", trans=True)


def chrome():
    for c in [shutil.which("chrome"), shutil.which("msedge"),
              r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", shutil.which("google-chrome")]:
        if c and os.path.exists(c):
            return c
    sys.exit("No se encontró Chrome ni Edge.")


def render(html_path, png_path, trans, w=1920, h=1080):
    prof = tempfile.mkdtemp()
    args = [chrome(), "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
            f"--user-data-dir={prof}", f"--window-size={w},{h}", "--virtual-time-budget=4000", f"--screenshot={png_path}"]
    if trans:
        args.append("--default-background-color=00000000")
    args.append("file:///" + html_path.replace("\\", "/"))
    subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    shutil.rmtree(prof, ignore_errors=True)


def main():
    os.makedirs(OUT, exist_ok=True); os.makedirs(HTML_DIR, exist_ok=True); os.makedirs(LOGO_DIR, exist_ok=True)
    filtro = sys.argv[1] if len(sys.argv) > 1 else ""
    if not filtro or "logo" in filtro:
        logos = {
            "logo_lafrox_fondo_oscuro": (f'<div style="padding:40px">{B.html_logo(220, True)}</div>', 1500, 300),
            "logo_lafrox_fondo_claro": (f'<div style="padding:40px">{B.html_logo(220, False)}</div>', 1500, 300),
            "isotipo_lafrox": (B.svg_isotipo(1024), 1024, 1024),
        }
        for nombre, (body, w, h) in logos.items():
            hp = os.path.join(HTML_DIR, nombre + ".html")
            open(hp, "w", encoding="utf-8").write(page(body, True).replace("width:1920px;height:1080px", f"width:{w}px;height:{h}px"))
            render(hp, os.path.join(LOGO_DIR, nombre + ".png"), True, w, h)
            print("ok", nombre)
    for nombre, (doc, trans) in PIEZAS.items():
        if filtro not in nombre:
            continue
        hp = os.path.join(HTML_DIR, nombre + ".html")
        open(hp, "w", encoding="utf-8").write(doc)
        render(hp, os.path.join(OUT, nombre + ".png"), trans)
        print("ok", nombre)


if __name__ == "__main__":
    main()
