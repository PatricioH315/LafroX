"""Compila el Sobre N.° 1 con foliación correlativa.

Orden del sobre: el índice (A-5) abre el sobre y los demás documentos siguen
el orden del Artículo 39° de las Bases Administrativas. Cada pasada compila
todos los documentos, lee el último folio de cada uno en su .aux (LastPage) y
reescribe folios.tex hasta que los folios no cambian.

Uso:  python compilar_sobre1.py
"""
import os, re, subprocess, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CEDULA = os.path.join("documentos-adjuntos", "cedula-representante-legal.pdf")

# (archivo sin extensión, documento en el índice A-5, observación, condición)
SOBRE = [
    ("LAFROX-Formulario-A-5", "Formulario A-5: Presentación e índice de antecedentes", None),
    ("LAFROX-Formulario-A-1", "Formulario A-1: Identificación del Proponente y de su Representante", None),
    ("LAFROX-Cedula-Representante-Legal", "Copia de la cédula de identidad del representante legal", CEDULA),
    ("LAFROX-Formulario-A-2", "Formulario A-2: Declaración jurada de no afectación por prohibiciones e inhabilidades", None),
    ("LAFROX-Formulario-A-3", "Formulario A-3: Declaración de aceptación íntegra de las Bases", None),
    ("LAFROX-Formulario-A-4", "Formulario A-4: Declaración de ausencia de conflictos de interés", None),
    ("LAFROX-Formulario-A-6", "Formulario A-6: Declaración de uso de inteligencia artificial generativa", None),
]


def documentos():
    return [(a, d) for a, d, req in SOBRE if req is None or os.path.exists(os.path.join(AQUI, req))]


def escribir_folios(docs, paginas):
    lineas = ["% Generado por compilar_sobre1.py. No editar a mano.\n"]
    filas, folio = [], 1
    for n, (archivo, doc) in enumerate(docs, 1):
        ini, fin = folio, folio + paginas[archivo] - 1
        lineas.append(f"\\definirfolio{{{archivo}}}{{{ini}}}{{{fin}}}\n")
        filas.append(f"  {n} & {doc} & {ini} & {fin} & \\texttt{{{archivo}.pdf}} \\\\\n")
        folio = fin + 1
    lineas.append("\\renewcommand{\\filasindicesobre}{%\n" + "".join(filas) + "}\n")
    texto = "".join(lineas)
    ruta = os.path.join(AQUI, "folios.tex")
    viejo = open(ruta, encoding="utf-8").read() if os.path.exists(ruta) else ""
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    return texto != viejo


def compilar(archivo):
    r = subprocess.run(["latexmk", "-g", f"{archivo}.tex"], cwd=AQUI,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.stdout.write(r.stdout[-3000:])
        raise SystemExit(f"Error al compilar {archivo}.tex")


def paginas_de(archivo):
    aux = open(os.path.join(AQUI, f"{archivo}.aux"), encoding="utf-8", errors="replace").read()
    m = re.search(r"\\newlabel\{LastPage\}\{\{[^}]*\}\{(\d+)\}", aux)
    if not m:
        raise SystemExit(f"{archivo}.aux no tiene LastPage")
    ultimo = int(m.group(1))
    m2 = re.search(r"\\definirfolio\{" + re.escape(archivo) + r"\}\{(\d+)\}",
                   open(os.path.join(AQUI, "folios.tex"), encoding="utf-8").read())
    inicio = int(m2.group(1)) if m2 else 1
    return ultimo - inicio + 1


def main():
    docs = documentos()
    paginas = {a: 1 for a, _ in docs}
    escribir_folios(docs, paginas)
    for pasada in range(1, 6):
        for archivo, _ in docs:
            compilar(archivo)
        paginas = {a: paginas_de(a) for a, _ in docs}
        if not escribir_folios(docs, paginas):
            print(f"Folios estables en la pasada {pasada}.")
            break
    else:
        raise SystemExit("Los folios no se estabilizaron")
    folio = 1
    for archivo, _ in docs:
        print(f"{archivo}.pdf  folios {folio}-{folio + paginas[archivo] - 1}")
        folio += paginas[archivo]


if __name__ == "__main__":
    main()
