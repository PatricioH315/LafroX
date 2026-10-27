"""Regresión documental del frente C; no certifica pruebas ni revisión humana.

Uso: python verificar_frente_c.py --sd6 RUTA [--output INFORME.json]
La auditoría de tablas es heurística: sus candidatos requieren revisión visual.
"""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return path.read_text(encoding="utf-8")


def audit_tables(path):
    text = read(path)
    tables = []
    for match in re.finditer(
        r"\\begin\{(tablalafrox|tablasimple)\}.*?\\end\{\1\}", text, re.S
    ):
        block = match[0]
        header = next((line for line in block.splitlines() if r"\cab{" in line), "")
        label = re.search(r"\{(tab:[^{}]+)\}", block)
        issues = []
        columns = header.count(r"\cab{")
        declaration = all(key in header for key in ("Nivel en texto", "Nivel en diagramas", "Revisión humana"))
        if columns > 5 and not (columns == 6 and declaration):
            issues.append("más de 5 columnas")
        if label and rf"\ref{{{label[1]}}}" not in text[:match.start()]:
            issues.append("sin llamada previa por label")
        if "Fuente:" not in block and not text[match.end():match.end()+900].lstrip().startswith(r"\fuentesd"):
            issues.append("fuente no detectada")
        if re.search(r"\\cab\{Concepto\}.*?\\cab\{Descripci[oó]n\}", header):
            issues.append("estructura Concepto/Descripción")
        sentences = []
        for line in block.splitlines():
            if " & " not in line or r"\cab{" in line:
                continue
            for cell in line.split(" & "):
                # Solo candidatos: abreviaturas y citas pueden dar falsos positivos.
                if re.search(r"[a-záéíóúñ][.]\s+[A-ZÁÉÍÓÚÑ]", cell):
                    sentences.append(cell.strip())
        if sentences:
            issues.append("posibles celdas con varias frases: revisión semántica")
        tables.append({"file": path.name, "label": label[1] if label else None,
                       "line": text[:match.start()].count("\n") + 1,
                       "columns": columns, "format_basis": "Aclaraciones 7.2: seis columnas" if declaration else "Aclaraciones 5", "candidates": issues,
                       "sentence_candidates": sentences})
    return tables


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sd6", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    sd6 = args.sd6.resolve()
    body6 = read(sd6 / "subdocumento_6/contenido.tex")
    annex6 = read(sd6 / "anexos.tex")
    t9 = read(sd6 / "LAFROX-Formulario-T-9.tex")
    t10 = read(sd6 / "LAFROX-Formulario-T-10.tex")
    purchases = read(sd6 / "subdocumento_6/tablas/adquisiciones.tex")
    body9 = read(ROOT / "09_plan_calidad/contenido.tex")
    t13 = read(ROOT / "T13/contenido.tex")
    assert r"\chapter{Metodologías}" in body6
    for title in ("Referencias", "Declaración de uso de IA"):
        assert rf"\section*{{{title}}}" in body6
        assert rf"\section{{{title}}}" not in body6
    assert "RUP (Kruchten, 2004)" in body6
    assert "Siendo la tabla" not in t9 and "6.A.2" not in t9
    assert "6.B.1" in t9
    assert r"\renewcommand{\thetable}{6.B.\arabic{table}}" in annex6
    assert "CLIENTE: obra civil de separación (RT-06.06)" in purchases
    assert "Meses 5 y 6" not in purchases
    assert "Contratación antes del mes 13" in purchases
    assert "05:30 a 07:00" in t10
    assert r"\renewcommand{\thesection}{\arabic{section}}" in t9
    assert r"\renewcommand{\thesection}{\arabic{section}}" in t10
    assert r"\subsection{" not in t10
    for text in (body6, t9, body9):
        assert "6,4 HH netas" in text and "102,4 HH" in text
    assert "16 evaluadores externos por día" in body6
    assert "instancia interna de LafroX" in body6 and "Art. 71" in t9
    assert body6.index(r"\ref{fig:sd6-control}") < body6.index(r"\label{fig:sd6-control}")
    for path in [sd6 / "anexos.tex", *(sd6 / "subdocumento_6/tablas").glob("*.tex")]:
        assert "elaboración propia" not in read(path), str(path)
    assert "(2026c, cap. 8)" not in body9
    for token in ("7.6 Recuperación", "antes de H5 y de H10", "relojes sincronizados",
                  "RTO ≤ 4 h y RPO ≤ 15 min", "pruebas previstas"):
        assert token in t13, token
    # Quitar coordinación editorial no debe borrar la declaración obligatoria.
    for text in (body6, body9):
        assert r"\section*{Declaración de uso de IA}" in text
        assert "Codex" in text.split(r"\section*{Declaración de uso de IA}", 1)[1]
        assert "Actualización frente C" not in text
    for text in (body6, t9):
        assert "El frente de cronograma" not in text

    proposal = read(ROOT / "revision/PROPUESTA_METRICAS_K3_2026-10-27.md")
    assert "propuesta, no política aprobada" in proposal
    assert 16 * 8 * 0.8 == 102.4
    assert 270 * 15 / 60 == 67.5
    result = {"documentary_checks": "passed", "tables": {
        "SD6": audit_tables(sd6 / "subdocumento_6/contenido.tex"),
        "SD9": audit_tables(ROOT / "09_plan_calidad/contenido.tex")},
        "limits": ["No verifica ejecución real, aceptación ni revisión humana",
                   "No sustituye K2/K6 finales ni revisión visual de tablas",
                   "La matriz heredada mantiene su snapshot histórico"]}
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print("OK: estructura, fuentes, adquisiciones, política K3 y protocolo DR del frente C.")
    for doc, tables in result["tables"].items():
        print(doc, len(tables), "tablas; candidatos a revisión:",
              sum(bool(t["candidates"]) for t in tables))


if __name__ == "__main__":
    main()
