# -*- coding: utf-8 -*-
"""Utilidades comunes del generador de tablas del Subdocumento 3."""
import re, os
from pathlib import Path

RAIZ = str(Path(__file__).resolve().parents[3])
SD3 = os.path.join(RAIZ, "03_esquema_solucion_alcance")
TAB = os.path.join(SD3, "tablas")
REQ = os.path.join(RAIZ, "Requerimientos")
BASES = os.path.join(RAIZ, "Bases")

_REEMPLAZOS = [
    ("\\", r"\textbackslash{}"),
    ("&", r"\&"), ("%", r"\%"), ("#", r"\#"), ("_", r"\_"),
    ("$", r"\$"), ("{", r"\{"), ("}", r"\}"),
    ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}"),
]
_UNI = [
    ("≤", r"$\leq$"), ("≥", r"$\geq$"), ("×", r"$\times$"), ("−", r"$-$"),
    ("→", r"$\rightarrow$"), ("←", r"$\leftarrow$"), ("↔", r"$\leftrightarrow$"),
    ("–", "--"), ("—", "---"), ("…", "..."), ("\u00a0", " "), ("≈", r"$\approx$"),
    ("“", "«"), ("”", "»"), ('"', "\u201d"),
]


def tex(s):
    """Escapa texto plano para LaTeX (LuaLaTeX, fontspec)."""
    if s is None:
        return ""
    s = str(s).replace("\r", "").replace("\n", " ").strip()
    s = re.sub(r"\s+", " ", s)
    out = []
    for ch in s:
        rep = None
        for a, b in _REEMPLAZOS:
            if ch == a:
                rep = b
                break
        out.append(rep if rep is not None else ch)
    s = "".join(out)
    for a, b in _UNI:
        s = s.replace(a, b)
    # comillas rectas dobles -> latinas
    s = re.sub(r"\u201d([^\u201d]*)\u201d", r"«\1»", s)
    s = s.replace("\u201d", "»")
    # °C con espacio fino
    s = re.sub(r"(\d)\s?°\s?C", r"\1\\,°C", s)
    return s


def fila(celdas):
    return " & ".join(celdas) + r" \\"


def escribir(nombre, contenido):
    ruta = os.path.join(TAB, nombre)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(contenido)
    return ruta


def cabecera(origen):
    return ("%% Generado a partir de " + origen + ".\n"
            "%% Tabla de anexo o formulario: se compone en pagina horizontal.\n\n")


def tabla(caption, label, cols, head, filas, nota=None):
    """Tabla institucional (tablalafrox) con filas ya formateadas."""
    t = []
    t.append("\\begin{tablalafrox}{%s}{%s}%%\n  {%s}%%\n  {%s}\n"
             % (caption, label, cols, " & ".join("\\cab{%s}" % h for h in head)))
    for f in filas:
        t.append("  " + f + "\n")
    t.append("\\end{tablalafrox}\n")
    if nota:
        t.append(nota + "\n")
    return "".join(t)
