"""Regenera formulario-a6/filas.tex, el cuerpo de la tabla del Formulario A-6.

Copia, de la declaración de uso de IA publicada en cada rama vigente, las
columnas Sección, Herramienta, Finalidad del uso y Revisión humana. No cambia
el contenido; solo unifica la grafía de los nombres del equipo con el T-8.
Se detiene si una fila trae marcadores de borrador o un revisor ajeno al T-8.

Uso, desde la raíz de esta rama y con las ramas remotas al día:
    git fetch origin
    python herramientas/consolidar_a6.py
    python compilar_sobre1.py
"""
import subprocess, re, sys, os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.environ.get("LAFROX_REPO", RAIZ)   # repositorio de donde se leen las ramas
OUT = os.path.join(RAIZ, "formulario-a6", "filas.tex")

SRC = [
 ("Subdocumento 1 \\textemdash{} Presentación de la empresa", "origin/LafroX-Subdoc1-LateX-CORRIGIENDO", "contenido.tex", "tab:declaracion_ia"),
 ("Subdocumento 2 \\textemdash{} Comprensión del problema y de la necesidad", "origin/LafroX-Subdoc2-LateX-CORRIGIENDO", "contenido.tex", "{tab:2-3}"),
 ("Subdocumento 3 \\textemdash{} Esquema de solución y alcance", "origin/LafroX-Subdoc3-LateX-CORRIGIENDO", "contenido.tex", "{tab:3-6}"),
 ("Subdocumento 4 \\textemdash{} Arquitectura lógica y física de la solución", "origin/LafroX-Subdoc4-LateX-corrigiendo", "04/partes/cierre/declaracion_de_uso_de_ia.tex", "tab:uso-ia-logica"),
 ("Subdocumento 5 \\textemdash{} Modelo y gestión de datos", "origin/LafroX-Subdoc5-LateX-CORRIGIENDO", "05_modelo_datos/tablas/uso_ia.tex", "tab:sd5-uso-ia"),
 ("Subdocumento 6 \\textemdash{} Metodologías", "origin/LafroX-Subdoc6-LateX-corrigiendo", "subdocumento_6/contenido.tex", "tab:declaracion-uso-ia"),
 ("Subdocumento 7 \\textemdash{} Plan de trabajo, EDT, cronograma e implantación", "origin/LafroX-Subdoc7-LateX-CORRIGIENDO", "subdocumento-07/tablas/tab_SD7_12.tex", "tab:7-ia"),
 ("Subdocumento 8 \\textemdash{} Plan de riesgos", "origin/Lafrox_Subdocumento_8_Latex_Revision", "08_plan_riesgos/contenido.tex", "tab:sd8-cuerpo-7"),
 ("Subdocumento 9 \\textemdash{} Plan de calidad", "origin/LafroX-Subdoc9-LateX-corrigiendo", "SD9_v_nueva/09_plan_calidad/contenido.tex", "tab:sd9-ia"),
 ("Subdocumento 10 \\textemdash{} Servicios de operación y niveles de servicio", "origin/LafroX-Subdoc10-LateX-corrigiendo", "comunes/uso_ia.tex", "tab:sd10-ia"),
 ("Subdocumento 11 \\textemdash{} Planes en operación", "origin/LafroX-Subdoc11-LateX-CORRIGIENDO", "subdocumento-11/tablas/declaracion-ia.tex", "tab:sd11-ia"),
 ("Subdocumento 12 \\textemdash{} Equipo de trabajo, subcontrataciones y alianzas", "origin/LafroX-Subdoc12-LateX-CORRIGIENDO", "subdocumento-12/tablas/tab_SD12_IA.tex", "tab:12-ia"),
 ("Subdocumento 13 \\textemdash{} Innovaciones", "origin/LafroX-Subdoc13-LateX-corrigiendo", "SD13_v_nueva/13_innovaciones/contenido.tex", "tab:sd13-29"),
 ("Oferta Económica \\textemdash{} Entregable 2: Análisis económico-financiero", "origin/LafroX-OfertaEconomica-2-Latex", "02_analisis_economico_financiero/contenido.tex", "tab:e2-ia"),
]

NOMBRES = {"Tomas Perez": "Tomás Pérez", "Bastian Trejo": "Bastián Trejo"}
CANON = ["Alex Aravena", "Bastián Trejo", "Álvaro Catalán", "Leandro Chamorro",
         "Tomás Pérez", "Maximiliano Miño", "Guillermo Castillo", "Patricio Henríquez"]

def split_top(s, sep):
    out, depth, cur, i = [], 0, [], 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            if sep == "\\\\" and s[i:i+2] == "\\\\" and depth == 0:
                out.append("".join(cur)); cur = []; i += 2; continue
            cur.append(s[i:i+2]); i += 2; continue
        if c == "{": depth += 1
        elif c == "}": depth -= 1
        if sep == "&" and c == "&" and depth == 0:
            out.append("".join(cur)); cur = []; i += 1; continue
        cur.append(c); i += 1
    out.append("".join(cur))
    return out

def limpia(x):
    x = re.sub(r"\\allowbreak\{\}", "", x)
    x = re.sub(r"\\mbox\{([^{}]*)\}", r"\1", x)
    x = re.sub(r"\s+", " ", x).strip()
    for a, b in NOMBRES.items():
        x = x.replace(a, b)
    return x

report, bloques, total = [], [], 0
for titulo, br, path, label in SRC:
    sha = subprocess.run(["git", "-C", REPO, "rev-parse", "--short", br], capture_output=True, text=True).stdout.strip()
    t = subprocess.run(["git", "-C", REPO, "show", f"{br}:{path}"], capture_output=True).stdout.decode("utf-8")
    t = "\n".join(l for l in t.splitlines() if not l.lstrip().startswith("%"))
    i = t.index(label)
    h = t.index("Revisi", i)
    nl = t.index("\n", h)
    end = t.index("\\end{", nl)
    body = t[nl:end]
    filas = []
    for r in split_top(body, "\\\\"):
        r = r.strip()
        if not r or r.startswith("\\midrule"):
            continue
        cols = [limpia(c) for c in split_top(r, "&")]
        if len(cols) != 6:
            raise SystemExit(f"{br}:{path}: fila con {len(cols)} columnas: {r[:120]}")
        sec, herr, fin, _, _, rev = cols
        for bad in ("\\ref", "\\pageref", "\\cite", "[[", "pendiente", "No documentada", "borrador"):
            for c in (sec, herr, fin, rev):
                if bad.lower() in c.lower():
                    raise SystemExit(f"marcador {bad!r} en {br}: {c}")
        nombres = [n for n in CANON if n in rev]
        if not nombres:
            raise SystemExit(f"sin revisor canónico en {br}: {rev}")
        filas.append((sec, herr, fin, rev))
    total += len(filas)
    report.append((titulo.split(" \\")[0], br, sha, len(filas)))
    bloques.append((titulo, filas))

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("% Generado por herramientas/consolidar_a6.py. No editar a mano.\n")
    for titulo, filas in bloques:
        f.write("  \\multicolumn{4}{@{}l}{\\intersemibold " + titulo + "} \\\\\n")
        for sec, herr, fin, rev in filas:
            f.write(f"  {sec} & {herr} & {fin} & {rev} \\\\\n")
        if (titulo, filas) != bloques[-1]:
            f.write("  \\midrule\n")
for r in report:
    print(*r)
print("total filas", total)
