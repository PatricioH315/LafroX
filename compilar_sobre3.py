"""Compila y folia el Sobre N.° 3 (Oferta Económica) con los entregables del Formulario E-21.

Uso:
    python compilar_sobre3.py                          # fetch, compila, folia y verifica
    python compilar_sobre3.py --externos CARPETA --zip # además arma SOBRE3_LAFROX_OFERTA_ECONOMICA_AAAAMMDD.ZIP
    python compilar_sobre3.py --sin-fetch              # usa las ramas origin/ ya descargadas
    python compilar_sobre3.py --fecha 20261125

Los documentos 1 y 2 se toman de la última versión de su rama en origin (git
archive, sin tocar la carpeta de trabajo) y se compilan a través de un archivo
envoltorio que cambia el \\setcounter{page}{1} de su portada por el folio que
le corresponde. Las fuentes de las ramas no se modifican.

La hoja resumen (LAFROX-Sobre3-Indice.tex) es el folio 1. Después vienen el
documento 1 (propuesta económica formal) y el documento 2 (análisis
económico-financiero). El modelo financiero (XLSX) y las versiones DOCX de los
documentos 1 y 2 no salen de LaTeX: se dejan en la carpeta --externos con su
nombre exacto y el script los agrega al sobre. Los DOCX deben generarse desde
los PDF ya foliados de _sobre3/, para que conserven los mismos folios.

Requiere LuaLaTeX con latexmk, y pdfinfo y pdftotext (vienen con MiKTeX).
Todo lo generado queda en _sobre3/, que no se versiona.
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
TRABAJO = AQUI / "_sobre3"
BUILD = TRABAJO / "build"
REPO = AQUI

# (número, rama, carpeta dentro de la rama, fuente, título, prefijo del archivo)
# El nombre final es <prefijo>_<fecha>, como exige el Formulario E-21.
DOCUMENTOS = [
    (1, "LafroX-OfertaEconomica-1-Latex", ".", "LaFroX-OfertaEconomica-1.tex",
     "Documento 1: Propuesta económica formal", "LAFROX_OfertaEconomica_1"),
    (2, "LafroX-OfertaEconomica-2-Latex", ".", "LAFROX_AnalisisFinanciero_2_20261113.tex",
     "Documento 2: Análisis económico-financiero", "LAFROX_AnalisisFinanciero_2"),
]
MODELO = ("Documento 3: Modelo financiero", "LAFROX_ModeloFinanciero_3")

INDICE = "LAFROX-Sobre3-Indice"
ARCHIVOS_INDICE = ["lafrox.cls", "lafrox-portada.tex", "latexmkrc", "sobre3-comun.tex",
                   INDICE + ".tex", "FIRMA_Alex_Aravena_transparente.png", "logo"]

# El envoltorio fija el folio inicial y rotula el número como folio, como en los
# Sobres N.° 1 y 2. Si la portada no tiene el \setcounter{page}{1} esperado, la
# compilación se detiene: un folio mal fijado es peor que no compilar.
ENVOLTORIO = r"""%% Generado por compilar_sobre3.py. No editar.
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
    r = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True)
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


def textos(pdf):
    r = correr([herramienta("pdftotext"), "-enc", "UTF-8", str(pdf), "-"])
    partes = r.stdout.split("\f")
    if partes and not partes[-1].strip():
        partes.pop()
    return partes


def extraer(n, sha):
    """Deja en build/docN el árbol de la rama en el commit indicado."""
    destino = BUILD / f"doc{n}"
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


def tt(nombre):
    return "\\texttt{" + nombre.replace("_", "\\_\\allowbreak{}") + "}"


def escribir_filas(carpeta, filas):
    """filas: [(titulo, inicio, termino, [archivos])] -> folios-sobre3.tex"""
    lineas = ["% Generado por compilar_sobre3.py. No editar a mano.\n",
              "\\renewcommand{\\filasindicesobre}{%\n"]
    for i, (tit, ini, fin, archivos) in enumerate(filas, 1):
        celda = "\\newline ".join(tt(a) for a in archivos)
        lineas.append(f"  {i} & {tit} & {ini} & {fin} & {celda} \\\\\n")
    lineas.append("}\n")
    (carpeta / "folios-sobre3.tex").write_text("".join(lineas), encoding="utf-8", newline="\n")


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
    errores, avisos, sin_firma = [], [], []
    for i, texto in enumerate(textos(pdf)):
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


def nomenclatura_portada(pdf, nombre):
    """Aviso si la portada declara un nombre de archivo distinto del entregado."""
    portada = re.sub(r"\s+", "", textos(pdf)[0])
    if f"{nombre}.pdf" not in portada:
        declarado = re.findall(r"LAFROX_\w+?_\d_\d{8}\.pdf", portada)
        return (f"{nombre}.pdf: la portada declara {declarado or 'otro nombre'}; "
                f"corregir «nomenclatura» en la rama del documento")
    return None


def main():
    global REPO
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sin-fetch", action="store_true", help="no ejecutar git fetch origin")
    ap.add_argument("--zip", action="store_true", help="armar el ZIP del Sobre N.° 3")
    ap.add_argument("--fecha", default="20261125", help="fecha AAAAMMDD de la nomenclatura")
    ap.add_argument("--externos", type=Path,
                    help="carpeta con el XLSX del modelo financiero y los DOCX de los documentos 1 y 2")
    ap.add_argument("--repo", type=Path, default=AQUI, help="repositorio git (por omisión, esta carpeta)")
    args = ap.parse_args()
    REPO = args.repo.resolve()

    if not args.sin_fetch:
        print("git fetch origin ...", flush=True)
        git("fetch", "-q", "origin")
    shas = {n: git("rev-parse", f"origin/{rama}") for n, rama, *_ in DOCUMENTOS}
    nombres = {n: f"{prefijo}_{args.fecha}" for n, *_, prefijo in DOCUMENTOS}
    modelo = f"{MODELO[1]}_{args.fecha}.xlsx"
    externos = [modelo] + [f"{nombres[n]}.docx" for n, *_ in DOCUMENTOS]

    def filas_de(folios):
        filas = [(tit, a, b, [f"{nombres[n]}.pdf", f"{nombres[n]}.docx"])
                 for (n, _, _, _, tit, _), (a, b) in zip(DOCUMENTOS, folios)]
        filas.append((MODELO[0], "\\textemdash{}", "\\textemdash{}", [modelo]))
        return filas

    # 1. Largo de la hoja resumen con folios de relleno del mismo ancho.
    largo_indice = paginas(compilar_indice(filas_de([(9999, 9999)] * len(DOCUMENTOS))))

    estado_archivo = BUILD / "estado.json"
    estado = json.loads(estado_archivo.read_text(encoding="utf-8")) if estado_archivo.is_file() else {}

    for _ in range(3):
        folio = largo_indice + 1
        folios, resultado = [], []
        for n, _, sub, fuente, _, _ in DOCUMENTOS:
            nombre = nombres[n]
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
            folios.append((folio, fin))
            resultado.append((n, nombre, pdf, folio, fin))
            folio = fin + 1
        indice = compilar_indice(filas_de(folios))
        nuevo = paginas(indice)
        if nuevo == largo_indice:
            break
        print(f"La hoja resumen cambió de {largo_indice} a {nuevo} páginas: se recalculan los folios.")
        largo_indice = nuevo
    else:
        raise SystemExit("Los folios no se estabilizaron")

    # 2. Verificación página por página y nomenclatura de las portadas.
    errores, avisos = verificar(indice, 1)
    for _, nombre, pdf, inicio, _ in resultado:
        e, a = verificar(pdf, inicio)
        errores += e
        avisos += a
        aviso = nomenclatura_portada(pdf, nombre)
        if aviso:
            avisos.append(aviso)

    # 3. Carpeta de entrega y manifiesto.
    nombre_sobre = f"SOBRE3_LAFROX_OFERTA_ECONOMICA_{args.fecha}"
    salida = TRABAJO / nombre_sobre
    if salida.exists():
        shutil.rmtree(salida)
    salida.mkdir(parents=True)
    shutil.copy2(indice, salida / indice.name)
    for _, _, pdf, _, _ in resultado:
        shutil.copy2(pdf, salida / pdf.name)
    faltan = []
    for archivo in externos:
        origen = args.externos / archivo if args.externos else None
        if origen and origen.is_file():
            shutil.copy2(origen, salida / archivo)
        else:
            faltan.append(archivo)
    manifiesto = {
        "fecha": args.fecha,
        "ramas": {f"Documento {n}": {"rama": rama, "commit": shas[n]} for n, rama, *_ in DOCUMENTOS},
        "documentos": [{"archivo": indice.name, "inicio": 1, "termino": largo_indice}] +
                      [{"archivo": pdf.name, "documento": n, "inicio": a, "termino": b}
                       for n, _, pdf, a, b in resultado],
        "externos": [a for a in externos if a not in faltan],
    }
    (TRABAJO / f"{nombre_sobre}.json").write_text(json.dumps(manifiesto, indent=1, ensure_ascii=False),
                                                 encoding="utf-8")

    print(f"\n{'Folios':>13}  Documento")
    print(f"{1:>6}–{largo_indice:<6}  {indice.name}")
    for _, nombre, _, a, b in resultado:
        print(f"{a:>6}–{b:<6}  {nombre}.pdf")
    print(f"\n{len(resultado) + 1} PDF, {resultado[-1][4]} folios. Carpeta: {salida}")
    for a in avisos:
        print("AVISO:", a)
    if faltan:
        print("FALTAN en --externos (la hoja resumen los declara):", ", ".join(faltan))
    if errores:
        for e in errores[:40]:
            print("ERROR:", e)
        raise SystemExit(f"{len(errores)} página(s) con folio incorrecto. No se arma el ZIP.")
    print("Folios verificados: correlativos y sin saltos en todo el sobre.")

    if args.zip:
        if faltan:
            raise SystemExit("No se arma el ZIP: el E-21 no acepta entregas parciales.")
        zip_ruta = TRABAJO / f"{nombre_sobre}.ZIP"
        with zipfile.ZipFile(zip_ruta, "w", zipfile.ZIP_DEFLATED) as z:
            for archivo in sorted(salida.iterdir()):
                z.write(archivo, archivo.name)
        print(f"ZIP: {zip_ruta}")


if __name__ == "__main__":
    main()
