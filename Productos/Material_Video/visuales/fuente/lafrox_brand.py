"""Identidad LafroX para el video, tomada del sitio oficial https://lafrox.github.io/
(repositorio lafrox/lafrox.github.io: img/lafrox-isotipo.svg y css/styles.css).

- Isotipo oficial: zorro naranja #E8641B (archivo lafrox-isotipo.svg, copiado sin modificar).
- Logotipo: isotipo + "LAFROX" en Archivo 900 + "INGENIERÍA LOGÍSTICA" en IBM Plex Mono (igual que el encabezado del sitio).
- Paleta y tipografías del sitio. Fuentes Archivo e IBM Plex Mono con licencia SIL OFL 1.1 (carpeta fonts/).
"""
import os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(AQUI, "fonts")

# Paleta del sitio (css/styles.css)
NEGRO = "#0B0D12"        # --ink
PANEL = "#14181F"        # --panel
TEXTO_SUAVE = "#CBD2DC"  # --text-soft
TEXTO_TENUE = "#93A0B0"  # --text-dim
HUESO = "#F6F7F9"        # --bone
NARANJA = "#FF5A2C"      # --orange
NARANJA_OSC = "#C2410C"  # --orange-dark
AMARILLO = "#FFC20E"     # --yellow
ISOTIPO = "#E8641B"      # color del isotipo
BLANCO = "#FFFFFF"

_iso = open(os.path.join(AQUI, "lafrox-isotipo.svg"), encoding="utf-8").read()
ISO_D = re.search(r'\sd="([^"]+)"', _iso).group(1)
ISO_VB = 432


def font_uri(name):
    return "file:///" + os.path.join(FONTS, name).replace("\\", "/")


FONT_CSS = f"""
@font-face{{font-family:'Archivo';src:url('{font_uri('Archivo-VF.ttf')}') format('truetype');font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:'IBM Plex Mono';src:url('{font_uri('IBMPlexMono-Medium.ttf')}');font-weight:500}}
@font-face{{font-family:'IBM Plex Mono';src:url('{font_uri('IBMPlexMono-SemiBold.ttf')}');font-weight:600}}
"""


def svg_isotipo(tam, color=ISOTIPO):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ISO_VB} {ISO_VB}" width="{tam}" height="{tam}">'
            f'<path fill="{color}" d="{ISO_D}"/></svg>')


def html_logo(alto=60, oscuro=True, sub=True):
    """Logotipo horizontal como en el encabezado del sitio. alto = tamaño del isotipo en px."""
    col = BLANCO if oscuro else NEGRO
    dim = TEXTO_TENUE if oscuro else "#5B6470"
    linea = "rgba(255,255,255,.28)" if oscuro else "rgba(11,13,18,.25)"
    fs = alto * 0.62
    s = (f'<div style="display:inline-flex;align-items:center;gap:{alto*0.28:.0f}px;line-height:1">'
         f'{svg_isotipo(alto)}'
         f'<span style="font-family:Archivo;font-weight:900;font-size:{fs:.0f}px;letter-spacing:.02em;color:{col}">LAFROX</span>')
    if sub:
        s += (f'<span style="font-family:\'IBM Plex Mono\';font-weight:500;font-size:{alto*0.19:.0f}px;letter-spacing:.14em;'
              f'color:{dim};border-left:{max(1, alto//40)}px solid {linea};padding-left:{alto*0.26:.0f}px;line-height:1.3">'
              f'INGENIERÍA<br>LOGÍSTICA</span>')
    return s + '</div>'
