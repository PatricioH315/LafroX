"""Compila y folia el Sobre N.° 2 (Oferta Técnica) en el orden del Formulario T-7.

Uso:
    python compilar_sobre2.py                 # fetch, compila, folia y verifica
    python compilar_sobre2.py --zip           # además arma SOBRE2_LAFROX_OFERTA_TECNICA_AAAAMMDD.ZIP
    python compilar_sobre2.py --sin-fetch     # usa las ramas origin/ ya descargadas
    python compilar_sobre2.py --fecha 20261125

Cada subdocumento se toma de la última versión de su rama en origin (git archive,
sin tocar la carpeta de trabajo) y se compila a través de un archivo envoltorio
que cambia el \\setcounter{page}{1} de su portada por el folio que le
corresponde. Las fuentes de las ramas no se modifican.

La hoja resumen (LAFROX-Sobre2-Indice.tex) es el folio 1. Después vienen, por
subdocumento, el cuerpo, sus anexos y sus formularios técnicos.

Requiere LuaLaTeX con latexmk, y pdfinfo y pdftotext (vienen con MiKTeX).
Todo lo generado queda en _sobre2/, que no se versiona.
"""
from pathlib import Path
import argparse
import io
import json
import re
import shutil
import subprocess
import sys
import tarfile
import zipfile

AQUI = Path(__file__).resolve().parent
TRABAJO = AQUI / "_sobre2"
BUILD = TRABAJO / "build"

RAMAS = {
    1: "LafroX-Subdoc1-LateX-CORRIGIENDO",
    2: "LafroX-Subdoc2-LateX-CORRIGIENDO",
    3: "LafroX-Subdoc3-LateX-CORRIGIENDO",
    4: "LafroX-Subdoc4-LateX-corrigiendo",
    5: "LafroX-Subdoc5-LateX-CORRIGIENDO",
    6: "LafroX-Subdoc6-LateX-corrigiendo",
    7: "LafroX-Subdoc7-LateX-CORRIGIENDO",
    8: "Lafrox_Subdocumento_8_Latex_Revision",
    9: "LafroX-Subdoc9-LateX-corrigiendo",
    10: "LafroX-Subdoc10-LateX-corrigiendo",
    11: "LafroX-Subdoc11-LateX-CORRIGIENDO",
    12: "LafroX-Subdoc12-LateX-CORRIGIENDO",
    13: "LafroX-Subdoc13-LateX-corrigiendo",
    14: "LafroX-Subdoc14-LateX-CORRIGIENDO",
}

SUBDOCUMENTOS = {
    1: "Presentación de la empresa",
    2: "Comprensión del problema y de la necesidad",
    3: "Esquema de solución y alcance",
    4: "Arquitectura lógica y física de la solución",
    5: "Modelo y gestión de datos",
    6: "Metodologías",
    7: "Plan de trabajo, EDT, cronograma e implantación",
    8: "Plan de riesgos",
    9: "Plan de calidad",
    10: "Servicios de operación y niveles de servicio",
    11: "Planes en operación",
    12: "Equipo de trabajo, subcontrataciones y alianzas",
    13: "Innovaciones",
    14: "Ventajas, beneficios y consolidación",
}

FORMULARIOS = {
    "T-6": "Experiencia en proyectos similares",
    "T-8": "Equipo de trabajo, subcontrataciones y alianzas",
    "T-9": "Metodología para la administración y gestión del proyecto",
    "T-10": "Metodología para el desarrollo",
    "T-11": "Especificaciones técnicas ofertadas",
    "T-12": "Matriz de cumplimiento técnico y trazabilidad de requerimientos",
    "T-13": "Plan de pruebas y validación",
    "T-14": "Plan de trabajo, EDT y carta Gantt",
    "T-15": "Nivelación de recursos",
    "T-16": "Plan de riesgos",
    "T-17": "Protocolo de aceptación",
    "T-18": "Propuesta de implantación y puesta en marcha controlada",
    "T-19": "Cartera de innovaciones",
}

# (subdocumento, carpeta dentro de la rama, fuente, nombre del PDF)
# Orden del sobre: cuerpo, anexos y formularios en orden de número.
FUENTES = [
    (1, ".", "LAFROX-Subdocumento1.tex", "LAFROX-Subdocumento1"),
    (1, ".", "LAFROX-Formulario-T-6.tex", "LAFROX-Formulario-T-6"),
    (2, ".", "LAFROX-Subdocumento2.tex", "LAFROX-Subdocumento2"),
    (2, ".", "LAFROX-Subdocumento2-Anexos.tex", "LAFROX-Subdocumento2-Anexos"),
    (3, ".", "LAFROX-Subdocumento3.tex", "LAFROX-Subdocumento3"),
    (3, ".", "LAFROX-Subdocumento3-Anexos.tex", "LAFROX-Subdocumento3-Anexos"),
    (3, ".", "LAFROX-Formulario-T-12.tex", "LAFROX-Formulario-T-12"),
    (4, ".", "main.tex", "LAFROX-Subdocumento4"),
    (4, "04", "anexos_logica.tex", "LAFROX-Subdocumento4-Anexos"),
    (4, "04", "formulario_T11.tex", "LAFROX-Formulario-T-11"),
    (5, ".", "LAFROX-Subdocumento5.tex", "LAFROX-Subdocumento5"),
    (5, ".", "LAFROX-Subdocumento5-Anexos.tex", "LAFROX-Subdocumento5-Anexos"),
    (6, ".", "LAFROX-Subdocumento6.tex", "LAFROX-Subdocumento6"),
    (6, ".", "LAFROX-Subdocumento6-Anexos.tex", "LAFROX-Subdocumento6-Anexos"),
    (6, ".", "LAFROX-Formulario-T-9.tex", "LAFROX-Formulario-T-9"),
    (6, ".", "LAFROX-Formulario-T-10.tex", "LAFROX-Formulario-T-10"),
    (7, ".", "LAFROX-Subdocumento7.tex", "LAFROX-Subdocumento7"),
    (7, ".", "LAFROX-Subdocumento7-Anexos.tex", "LAFROX-Subdocumento7-Anexos"),
    (7, ".", "LAFROX-Formulario-T-14.tex", "LAFROX-Formulario-T-14"),
    (7, ".", "LAFROX-Formulario-T-15.tex", "LAFROX-Formulario-T-15"),
    (7, ".", "LAFROX-Formulario-T-18.tex", "LAFROX-Formulario-T-18"),
    (8, ".", "LAFROX-Subdocumento8.tex", "LAFROX-Subdocumento8"),
    (8, ".", "LAFROX-Subdocumento8-Anexos.tex", "LAFROX-Subdocumento8-Anexos"),
    (8, ".", "LAFROX-Formulario-T-16.tex", "LAFROX-Formulario-T-16"),
    (9, "SD9_v_nueva", "LAFROX-Subdocumento9.tex", "LAFROX-Subdocumento9"),
    (9, "SD9_v_nueva", "LAFROX-Subdocumento9-Anexos.tex", "LAFROX-Subdocumento9-Anexos"),
    (9, "SD9_v_nueva", "LAFROX-Formulario-T-13.tex", "LAFROX-Formulario-T-13"),
    (9, "SD9_v_nueva", "LAFROX-Formulario-T-17.tex", "LAFROX-Formulario-T-17"),
    (10, ".", "main.tex", "LAFROX-Subdocumento10"),
    (10, ".", "anexos.tex", "LAFROX-Subdocumento10-Anexos"),
    (11, ".", "LAFROX-Subdocumento11.tex", "LAFROX-Subdocumento11"),
    (12, ".", "LAFROX-Subdocumento12.tex", "LAFROX-Subdocumento12"),
    (12, ".", "LAFROX-Subdocumento12-Anexos.tex", "LAFROX-Subdocumento12-Anexos"),
    (12, ".", "LAFROX-Formulario-T-8.tex", "LAFROX-Formulario-T-8"),
    (13, "SD13_v_nueva", "LAFROX-Subdocumento13.tex", "LAFROX-Subdocumento13"),
    (13, "SD13_v_nueva", "LAFROX-Subdocumento13-Anexos.tex", "LAFROX-Subdocumento13-Anexos"),
    (13, "SD13_v_nueva", "LAFROX-Formulario-T-19.tex", "LAFROX-Formulario-T-19"),
    (14, ".", "LAFROX-Subdocumento14.tex", "LAFROX-Subdocumento14"),
]

INDICE = "LAFROX-Sobre2-Indice"
ARCHIVOS_INDICE = ["lafrox.cls", "lafrox-portada.tex", "latexmkrc", "sobre2-comun.tex",
                   INDICE + ".tex", "FIRMA_Alex_Aravena_transparente.png", "logo"]

# El envoltorio fija el folio inicial y rotula el número como folio, como en el
# Sobre N.° 1. Si la portada no tiene el \setcounter{page}{1} esperado, la
# compilación se detiene: un folio mal fijado es peor que no compilar.
ENVOLTORIO = r"""%% Generado por compilar_sobre2.py. No editar.
\RequirePackage{etoolbox}
\def\LFXfolioinicial{@FOLIO@}
\AddToHook{begindocument/end}{%
  \providecommand{\LFXfolio}{}\renewcommand{\LFXfolio}{Folio}%
  \ifdefined\portadalafrox
    \patchcmd{\portadalafrox}{\setcounter{page}{1}}{\setcounter{page}{\LFXfolioinicial}}{}{%
      \patchcmd{\portadalafrox}{\LFXfolioinicial}{\LFXfolioinicial}{}{%
        \GenericError{}{FOLIACION: la portada no fija la pagina 1}{}{}}}%
  \else
    \GenericError{}{FOLIACION: el documento no usa portadalafrox}{}{}%
  \fi
  \setcounter{page}{\LFXfolioinicial}}
\input{@FUENTE@}
"""


def correr(comando, **kw):
    return subprocess.run(comando, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", **kw)


def git(*args, binario=False):
    r = subprocess.run(["git", "-C", str(AQUI), *args], capture_output=True)
    if r.returncode:
        raise SystemExit(f"git {' '.join(args)}: {r.stderr.decode(errors='replace')}")
    return r.stdout if binario else r.stdout.decode().strip()


def herramienta(nombre):
    ruta = shutil.which(nombre)
    if not ruta:
        raise SystemExit(f"No se encontró {nombre} en el PATH.")
    return ruta


def paginas(pdf):
    r = correr([herramienta("pdfinfo"), str(pdf)])
    m = re.search(r"^Pages:\s+(\d+)", r.stdout, re.M)
    if not m:
        raise SystemExit(f"pdfinfo no pudo leer {pdf}")
    return int(m.group(1))


def extraer(n, sha):
    """Deja en build/sdN el árbol de la rama en el commit indicado."""
    destino = BUILD / f"sd{n:02d}"
    marca = destino / ".foliacion-sha"
    if marca.is_file() and marca.read_text().strip() == sha:
        return destino
    if destino.exists():
        shutil.rmtree(destino)
    destino.mkdir(parents=True)
    datos = git("-c", "core.autocrlf=false", "archive", "--format=tar", sha, binario=True)
    with tarfile.open(fileobj=io.BytesIO(datos)) as tar:
        tar.extractall(destino, filter="data")
    marca.write_text(sha)
    return destino


def compilar(carpeta, fuente, nombre, folio):
    """Compila fuente con el folio inicial dado y devuelve la ruta del PDF."""
    envoltorio = carpeta / f"_folio_{nombre}.tex"
    envoltorio.write_text(ENVOLTORIO.replace("@FOLIO@", str(folio)).replace("@FUENTE@", fuente),
                          encoding="utf-8", newline="\n")
    pdf = carpeta / f"{nombre}.pdf"
    pdf.unlink(missing_ok=True)
    r = correr([herramienta("latexmk"), "-lualatex", "-interaction=nonstopmode", "-halt-on-error",
                "-file-line-error", f"-jobname={nombre}", envoltorio.name], cwd=carpeta)
    if r.returncode or not pdf.is_file():
        log = carpeta / f"{nombre}.log"
        cola = log.read_text(encoding="utf-8", errors="replace")[-3000:] if log.is_file() else r.stdout[-3000:]
        print(cola)
        raise SystemExit(f"Error al compilar {nombre} (ver {log})")
    return pdf


def titulo(n, nombre):
    if nombre.endswith("-Anexos"):
        return f"Anexos del Subdocumento {n}"
    m = re.search(r"Formulario-(T-\d+)$", nombre)
    if m:
        return f"Formulario {m.group(1)}: {FORMULARIOS[m.group(1)]}"
    return f"Subdocumento {n}: {SUBDOCUMENTOS[n]}"


def escribir_filas(carpeta, filas):
    """filas: [(titulo, inicio, termino, archivo)] -> folios-sobre2.tex"""
    lineas = ["% Generado por compilar_sobre2.py. No editar a mano.\n",
              "\\renewcommand{\\filasindicesobre}{%\n"]
    for i, (tit, ini, fin, archivo) in enumerate(filas, 1):
        etiqueta = archivo.replace("-", "-\\allowbreak{}")
        lineas.append(f"  {i} & {tit} & {ini} & {fin} & \\texttt{{{etiqueta}}} \\\\\n")
    lineas.append("}\n")
    (carpeta / "folios-sobre2.tex").write_text("".join(lineas), encoding="utf-8", newline="\n")


def compilar_indice(filas):
    carpeta = BUILD / "indice"
    carpeta.mkdir(parents=True, exist_ok=True)
    for nombre in ARCHIVOS_INDICE:
        origen = AQUI / nombre
        if origen.is_dir():
            shutil.copytree(origen, carpeta / nombre, dirs_exist_ok=True)
        else:
            shutil.copy2(origen, carpeta / nombre)
    escribir_filas(carpeta, filas)
    pdf = carpeta / f"{INDICE}.pdf"
    pdf.unlink(missing_ok=True)
    r = correr([herramienta("latexmk"), "-lualatex", "-interaction=nonstopmode", "-halt-on-error",
                f"{INDICE}.tex"], cwd=carpeta)
    if r.returncode or not pdf.is_file():
        print(r.stdout[-3000:])
        raise SystemExit("Error al compilar la hoja resumen")
    return pdf


def verificar(pdf, inicio):
    """Devuelve (errores, avisos) del folio y la media firma de cada página."""
    r = correr([herramienta("pdftotext"), "-enc", "UTF-8", str(pdf), "-"])
    textos = r.stdout.split("\f")
    if textos and not textos[-1].strip():
        textos.pop()
    errores, avisos, sin_firma = [], [], []
    for i, texto in enumerate(textos):
        esperado = inicio + i
        folios = re.findall(r"Folio\s+(\d+)", texto)
        if not folios or int(folios[-1]) != esperado:
            numeros = re.findall(r"\b\d+\b", texto)
            ultimo = numeros[-1] if numeros else "ninguno"
            errores.append(f"{pdf.name} página {i + 1}: se esperaba «Folio {esperado}», "
                           f"se leyó {folios[-1:] or 'sin rótulo'} (último número: {ultimo})")
        if i > 0 and "Media firma" not in texto:
            sin_firma.append(i + 1)
    if sin_firma:
        avisos.append(f"{pdf.name}: sin «Media firma» en {len(sin_firma)} página(s), "
                      f"p. ej. {sin_firma[:8]}")
    return errores, avisos


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sin-fetch", action="store_true", help="no ejecutar git fetch origin")
    ap.add_argument("--zip", action="store_true", help="armar el ZIP del Sobre N.° 2")
    ap.add_argument("--fecha", default="20261125", help="fecha AAAAMMDD de la nomenclatura")
    args = ap.parse_args()

    if not args.sin_fetch:
        print("git fetch origin ...", flush=True)
        git("fetch", "-q", "origin")
    shas = {n: git("rev-parse", f"origin/{rama}") for n, rama in RAMAS.items()}

    # 1. Largo de la hoja resumen con folios de relleno del mismo ancho.
    relleno = [(titulo(n, nombre), 9999, 9999, nombre + ".pdf") for n, _, _, nombre in FUENTES]
    largo_indice = paginas(compilar_indice(relleno))

    estado_archivo = BUILD / "estado.json"
    estado = json.loads(estado_archivo.read_text(encoding="utf-8")) if estado_archivo.is_file() else {}

    for intento in range(3):
        folio = largo_indice + 1
        filas, resultado = [], []
        for n, sub, fuente, nombre in FUENTES:
            carpeta = extraer(n, shas[n]) / sub
            pdf = carpeta / f"{nombre}.pdf"
            previo = estado.get(nombre, {})
            if previo.get("sha") == shas[n] and previo.get("inicio") == folio and pdf.is_file():
                print(f"  {nombre}: sin cambios (folio {folio})", flush=True)
            else:
                print(f"  {nombre}: compilando desde el folio {folio} ...", flush=True)
                compilar(carpeta, fuente, nombre, folio)
            total = paginas(pdf)
            estado[nombre] = {"sha": shas[n], "inicio": folio, "paginas": total}
            estado_archivo.write_text(json.dumps(estado, indent=1, ensure_ascii=False), encoding="utf-8")
            fin = folio + total - 1
            filas.append((titulo(n, nombre), folio, fin, nombre + ".pdf"))
            resultado.append((n, nombre, pdf, folio, fin))
            folio = fin + 1
        indice = compilar_indice(filas)
        nuevo = paginas(indice)
        if nuevo == largo_indice:
            break
        print(f"La hoja resumen cambió de {largo_indice} a {nuevo} páginas: se recalculan los folios.")
        largo_indice = nuevo
    else:
        raise SystemExit("Los folios no se estabilizaron")

    # 2. Verificación página por página.
    errores, avisos = verificar(indice, 1)
    for _, _, pdf, inicio, _ in resultado:
        e, a = verificar(pdf, inicio)
        errores += e
        avisos += a

    # 3. Carpeta de entrega y manifiesto.
    nombre_sobre = f"SOBRE2_LAFROX_OFERTA_TECNICA_{args.fecha}"
    salida = TRABAJO / nombre_sobre
    if salida.exists():
        shutil.rmtree(salida)
    salida.mkdir(parents=True)
    shutil.copy2(indice, salida / indice.name)
    for _, _, pdf, _, _ in resultado:
        shutil.copy2(pdf, salida / pdf.name)
    manifiesto = {
        "fecha": args.fecha,
        "ramas": {f"SD{n}": {"rama": RAMAS[n], "commit": shas[n]} for n in RAMAS},
        "documentos": [{"archivo": indice.name, "inicio": 1, "termino": largo_indice}] +
                      [{"archivo": pdf.name, "subdocumento": n, "inicio": a, "termino": b}
                       for n, _, pdf, a, b in resultado],
    }
    (TRABAJO / f"{nombre_sobre}.json").write_text(json.dumps(manifiesto, indent=1, ensure_ascii=False),
                                                 encoding="utf-8")

    print(f"\n{'Folios':>13}  Documento")
    print(f"{1:>6}–{largo_indice:<6}  {indice.name}")
    for _, nombre, _, a, b in resultado:
        print(f"{a:>6}–{b:<6}  {nombre}.pdf")
    total = resultado[-1][4]
    print(f"\n{len(resultado) + 1} documentos, {total} folios. Carpeta: {salida}")
    for a in avisos:
        print("AVISO:", a)
    if errores:
        for e in errores[:40]:
            print("ERROR:", e)
        raise SystemExit(f"{len(errores)} página(s) con folio incorrecto. No se arma el ZIP.")
    print("Folios verificados: correlativos y sin saltos en todo el sobre.")

    if args.zip:
        zip_ruta = TRABAJO / f"{nombre_sobre}.ZIP"
        with zipfile.ZipFile(zip_ruta, "w", zipfile.ZIP_DEFLATED) as z:
            for archivo in sorted(salida.iterdir()):
                z.write(archivo, archivo.name)
        print(f"ZIP: {zip_ruta}")


if __name__ == "__main__":
    main()
