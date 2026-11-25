"""Compila e integra los 23 antecedentes del artículo 39, la declaración del sitio web (BTT 23.3), el acceso al video (BTT 24.5), el enlace al prototipo (BTT 25.5) y la Boleta de Garantía de Seriedad (Art. 35) en un solo índice.

Uso: python compilar_sobre1.py
Requiere LuaLaTeX y PyMuPDF (python -m pip install pymupdf).
Cada PDF conserva su ruta; folios.tex comparte la foliación entre las dos clases.
"""
from pathlib import Path
import os
import re
import subprocess
import sys
import pymupdf

AQUI = Path(__file__).resolve().parent
ANT = "antecedentes/"
CEDULA = AQUI / "documentos-adjuntos/cedula-representante-legal.pdf"
SOBRE = [
 ("LAFROX-Formulario-A-5", "Formulario A-5: Presentación e índice de antecedentes"),
 ("LAFROX-Formulario-A-1", "Formulario A-1: Identificación del Proponente y de su Representante"),
 (ANT+"1-legales/02-cedula-representante/LAFROX-Cedula-Representante-Legal-v2", "Cédula de identidad del representante legal"),
 (ANT+"1-legales/03-rut-empresa/LAFROX-RUT", "Rol Único Tributario de la empresa"),
 (ANT+"1-legales/04-certificado-vigencia/LAFROX-Vigencia", "Certificado de vigencia de la sociedad"),
 (ANT+"1-legales/05-patente-comercial/LAFROX-Patente", "Patente comercial"),
 (ANT+"1-legales/06-escritura-constitucion/LAFROX-Escritura", "Escritura de constitución y modificaciones"),
 (ANT+"1-legales/07-poderes-representante/LAFROX-Poderes", "Poderes vigentes del representante"),
 (ANT+"1-legales/08-individualizacion-socios/LAFROX-Socios", "Individualización de socios"),
 (ANT+"2-financieros/09-deuda-tributaria/LAFROX-DeudaTributaria", "Certificado de deudas tributarias"),
 (ANT+"2-financieros/10-estados-financieros/LAFROX-EEFF", "Estados financieros auditados 2023–2025"),
 (ANT+"2-financieros/11-antecedentes-comerciales/LAFROX-AntecedentesComerciales", "Certificado de antecedentes comerciales"),
 (ANT+"2-financieros/12-boletin-laboral/LAFROX-BoletinLaboral", "Antecedentes laborales y previsionales"),
 (ANT+"2-financieros/13-certificado-bancario/LAFROX-CertificadoBancario", "Capacidad bancaria de emisión de garantías"),
 ("LAFROX-Formulario-A-2", "Formulario A-2: No afectación por prohibiciones e inhabilidades"),
 (ANT+"3-declaraciones/15-dj-no-quiebra/LAFROX-NoQuiebra", "Declaración de no quiebra ni reorganización"),
 ("LAFROX-Formulario-A-3", "Formulario A-3: Aceptación íntegra de las Bases"),
 ("LAFROX-Formulario-A-4", "Formulario A-4: Ausencia de conflictos de interés"),
 (ANT+"3-declaraciones/18-domicilio-valparaiso/LAFROX-Domicilio", "Constitución de domicilio en Valparaíso"),
 (ANT+"4-tecnicos/19-carta-presentacion-contratos/LAFROX-CartaPresentacion", "Carta de presentación y nómina de contratos similares"),
 (ANT+"4-tecnicos/20-cartas-compromiso/LAFROX-CartasCompromiso", "Cartas compromiso de socios, subcontratistas y proveedores clave"),
 ("LAFROX-Formulario-A-6", "Formulario A-6: Declaración de uso de IA generativa"),
 (ANT+"4-tecnicos/23-certificaciones/LAFROX-Certificaciones", "Certificaciones institucionales y de fabricante"),
 (ANT+"4-tecnicos/24-dj-sitio-web/LAFROX-DeclaracionWeb", "Declaración jurada simple de veracidad del sitio web corporativo"),
 ("LAFROX-Video-Acceso-Enlace", "Video de presentación: enlace de descarga y contraseña de acceso (BTT 24.5)"),
 ("LAFROX-Prototipo-Acceso-Enlace", "Prototipo interactivo: enlace de acceso (BTT 25.5)"),
 (ANT+"5-garantias/35-boleta-seriedad/LAFROX-BoletaSeriedad", "Boleta de Garantía de Seriedad de la Oferta (Art. 35)"),
]

def documentos():
    docs = list(SOBRE)
    if CEDULA.is_file():
        docs[2] = ("LAFROX-Cedula-Representante-Legal", docs[2][1])
    for archivo, _ in docs:
        if not (AQUI / (archivo + ".tex")).is_file():
            raise SystemExit(f"Fuente ausente: {archivo}.tex")
    return docs

def contar(archivo):
    with pymupdf.open(AQUI / (archivo + ".pdf")) as pdf:
        return len(pdf)

def escribir_folios(docs, paginas):
    lineas = ["% Generado por compilar_sobre1.py. No editar a mano.\n"]
    filas = []
    folio = 1
    for n, (archivo, titulo) in enumerate(docs, 1):
        nombre = Path(archivo).name
        fin = folio + paginas[archivo] - 1
        lineas.append(f"\\definirfolio{{{nombre}}}{{{folio}}}{{{fin}}}\n")
        # Los nombres base son únicos. README conserva las rutas completas.
        etiqueta = nombre.replace("-", "-\\allowbreak{}") + ".pdf"
        filas.append(f"  {n} & {titulo} & {folio} & {fin} & \\texttt{{{etiqueta}}} " + r"\\" + "\n")
        folio = fin + 1
    lineas.append("\\renewcommand{\\filasindicesobre}{%\n" + "".join(filas) + "}\n")
    ruta = AQUI / "folios.tex"
    texto = "".join(lineas)
    viejo = ruta.read_text(encoding="utf-8") if ruta.exists() else ""
    if texto != viejo:
        ruta.write_text(texto, encoding="utf-8", newline="\n")
    return texto != viejo

def compilar(archivo):
    fuente = AQUI / (archivo + ".tex")
    for _ in range(2):
        comando = ["lualatex", "--interaction=nonstopmode", "--halt-on-error", "--no-shell-escape",
                   f"--include-directory={AQUI}", f"--include-directory={AQUI / 'antecedentes'}", fuente.name]
        r = subprocess.run(comando, cwd=fuente.parent, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        if r.returncode:
            print(r.stdout[-4000:])
            raise SystemExit(f"Error al compilar {archivo}.tex")

def verificar(docs, paginas):
    esperado = 1
    for archivo, _ in docs:
        with pymupdf.open(AQUI / (archivo + ".pdf")) as pdf:
            for pagina in pdf:
                pie = pagina.get_text(clip=pymupdf.Rect(0, pagina.rect.height-65, pagina.rect.width, pagina.rect.height))
                folios = re.findall(r"Folio\s+(\d+)", pie)
                if folios != [str(esperado)]:
                    raise SystemExit(f"Folio incorrecto en {archivo}: esperado {esperado}, encontrados {folios}")
                esperado += 1
    if esperado - 1 != sum(paginas.values()):
        raise SystemExit("El total de folios no coincide con las páginas")
    print(f"Verificados {len(docs)} documentos y {esperado-1} folios consecutivos.")

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    docs = documentos()
    paginas = {a: max(1, contar(a)) if (AQUI / (a+".pdf")).exists() else 1 for a, _ in docs}
    # A-5 se estabiliza primero: su longitud determina todos los folios siguientes.
    for _ in range(5):
        escribir_folios(docs, paginas)
        compilar(docs[0][0])
        nuevas = contar(docs[0][0])
        if nuevas == paginas[docs[0][0]]:
            break
        paginas[docs[0][0]] = nuevas
    else:
        raise SystemExit("El índice A-5 no se estabilizó")
    for pasada in range(1, 6):
        escribir_folios(docs, paginas)
        for archivo, _ in docs:
            print(f"Pasada {pasada}: {archivo}", flush=True)
            if pasada != 1 or archivo != docs[0][0]:
                compilar(archivo)
        nuevas = {a: contar(a) for a, _ in docs}
        if any(n < 1 for n in nuevas.values()):
            raise SystemExit("Un PDF compilado no tiene páginas")
        if nuevas == paginas:
            verificar(docs, nuevas)
            break
        paginas = nuevas
    else:
        raise SystemExit("Los folios no se estabilizaron")
    folio = 1
    for archivo, _ in docs:
        fin = folio + paginas[archivo] - 1
        print(f"{folio}–{fin}: {archivo}.pdf")
        folio = fin + 1

if __name__ == "__main__":
    main()
