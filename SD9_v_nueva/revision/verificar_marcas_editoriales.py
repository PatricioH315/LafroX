"""Detecta notas editoriales impropias de los entregables SD6/SD9.

No detecta autoría ni acredita revisión humana. Conserva la declaración de IA.
Uso: python verificar_marcas_editoriales.py --sd6 RUTA
"""
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DECLARATION = r"\section*{Declaración de uso de IA}"
MARKERS = re.compile(
    r"Actualización frente C|Revalidación C0[1-9]|El frente de cronograma|"
    r"\[cite(?:[:\s]|\])|\?\?|\b(?:INSERTAR|TODO)\b|"
    r"por indicación del usuario|en este chat|Fuente:\s*elaboración propia"
)
TOOLS = re.compile(r"\b(?:Chat\s?GPT|Codex|Claude(?: Code)?|OpenAI)\b", re.I)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sd6", required=True, type=Path)
    args = parser.parse_args()
    sd6 = args.sd6.resolve()
    files = [
        *sorted((sd6 / "subdocumento_6").rglob("*.tex")),
        sd6 / "anexos.tex",
        sd6 / "LAFROX-Formulario-T-9.tex",
        sd6 / "LAFROX-Formulario-T-10.tex",
        *(ROOT / name / "contenido.tex" for name in (
            "09_plan_calidad", "09_anexos", "T13", "T17")),
        ROOT / "T13/matriz_requisitos.tex",
    ]
    issues = []
    declarations = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        # Comentarios internos del generador no se imprimen en la propuesta.
        visible = re.sub(r"(?<!\\)%[^\n]*", "", text)
        body, separator, declaration = visible.partition(DECLARATION)
        for number, line in enumerate(visible.splitlines(), 1):
            if MARKERS.search(line):
                issues.append(f"{path}:{number}: marcador editorial")
        for number, line in enumerate(body.splitlines(), 1):
            if TOOLS.search(line):
                issues.append(f"{path}:{number}: revisar mención fuera de declaración")
        if separator:
            declarations += 1
            assert "Codex" in declaration, path
            assert "Revisión humana" in declaration, path
    assert declarations == 2, declarations
    assert not issues, "\n".join(issues)
    print(f"OK: {len(files)} fuentes revisadas; sin los marcadores editoriales buscados.")
    print("OK: declaraciones de IA conservadas en SD6 y SD9, sin inventar revisión humana.")
    print("Esto no es un detector de autoría ni una certificación de revisión humana.")


if __name__ == "__main__":
    main()
