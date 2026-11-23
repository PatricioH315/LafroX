"""Audit SD4 PDF destinations, bibliography and manual T-12 page citations.

Usage: python 04/herramientas/verificar_referencias.py --t12 /path/T12.pdf
Requires pypdf. Does not modify sources or contact external sites.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from pypdf import PdfReader

DATE = r"(?:19|20)\d{2}[a-z]?|s\.\s*f\.[-a-z]*"
ALIASES = {
    "ISO": "International Organization for Standardization",
    "NIST": "National Institute of Standards and Technology",
    "SII": "Servicio de Impuestos Internos",
}


def bibliography_errors(root: Path) -> tuple[int, list[str]]:
    """Check author/date citations within each independently delivered document."""
    documents = {}
    authors = set()
    for directory in ("partes", "anexos", "formularios"):
        bibliography = set()
        body = []
        for path in sorted((root / "04" / directory).rglob("*.tex")):
            for number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
                line = line.replace("~", " ")
                if line.lstrip().startswith("%"):
                    continue
                item = re.match(r"\\item (.*?)\. \(([^)]+)\)", line)
                if item:
                    bibliography.add((item[1], item[2]))
                    authors.add(item[1])
                else:
                    body.append((path.relative_to(root), number, line))
        documents[directory] = (bibliography, body)
    checked = 0
    errors = []
    for bibliography, body in documents.values():
        for path, number, line in body:
            for author in sorted(authors | ALIASES.keys(), key=len, reverse=True):
                pattern = (r"(?<!\w)" + re.escape(author) + r"(?:,\s*|\s*\()"
                           + rf"((?:{DATE})(?:\s*[,y]+\s*(?:{DATE}))*)")
                for match in re.finditer(pattern, line):
                    for date in re.findall(DATE, match[1]):
                        checked += 1
                        key = (ALIASES.get(author, author), date)
                        if key not in bibliography:
                            errors.append(f"{path}:{number}: missing bibliography: {key}")
    return checked, errors


def t12_row_pages(t12: PdfReader) -> dict[str, list[int]]:
    """Read IDs in the table's first column, including IDs split across lines.

    Restricting extraction to the column headed ID avoids accepting a code
    that appears only in another requirement's description or test criterion.
    Text coordinates are compared within the table's text space so this also
    works when the wide table is scaled or rotated on the PDF page.
    """
    rows: dict[str, list[int]] = {}
    for number, page in enumerate(t12.pages, 1):
        runs = []

        def collect(text, cm, tm, font, size):
            runs.append((float(tm[4]), text))

        page.extract_text(visitor_text=collect)
        headers = [x for x, text in runs if re.match(r"ID(?:\s|$)", text.strip())]
        if not headers:
            continue
        left = headers[0]
        column = "".join(text for x, text in runs if abs(x - left) < 2)
        codes = set(re.findall(r"\b(?:RT|RF)-\s*\d{2}\.\d{2}(?![\d.])", column))
        for code in codes:
            code = re.sub(r"\s+", "", code)
            rows.setdefault(code, []).append(number)
    return rows


def t12_errors(root: Path, t12: PdfReader) -> tuple[int, list[str]]:
    """Require the cited page to contain the row, not merely mention its code."""
    rows = t12_row_pages(t12)
    count = 0
    errors = []
    pattern = re.compile(r"((?:RT|RF)-\d{2}\.\d{2}).*?T-12 [AB], p\.~(\d+)")
    for path in sorted((root / "04").rglob("*.tex")):
        for number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
            if line.lstrip().startswith("%"):
                continue
            match = pattern.search(line)
            if not match:
                continue
            count += 1
            code, cited = match[1], int(match[2])
            pages = rows.get(code, [])
            if cited not in pages:
                errors.append(f"{path.relative_to(root)}:{number}: {code}: p{cited}; row at {pages}")
    if count == 0:
        errors.append("No manual T-12 page citations found; verify the source layout.")
    return count, errors


def pdf_errors(root: Path) -> tuple[dict, list[str]]:
    """Validate actual PDF actions, including remote named destinations."""
    names = ("LAFROX-Subdocumento4.pdf", "LAFROX-Subdocumento4-Anexos.pdf",
             "LAFROX-Formulario-T-11.pdf")
    readers = {name: PdfReader(root / "entrega" / name) for name in names}
    destinations = {name: reader.named_destinations for name, reader in readers.items()}
    counts = {"pages": {}, "internal_links": 0, "cross_pdf_links": 0}
    errors = []
    for name, reader in readers.items():
        counts["pages"][name] = len(reader.pages)
        for number, page in enumerate(reader.pages, 1):
            if "??" in (page.extract_text() or ""):
                errors.append(f"{name}:p{number}: unresolved ?? in rendered text")
            for reference in page.get("/Annots", []):
                annotation = reference.get_object()
                if annotation.get("/Subtype") != "/Link":
                    continue
                action = annotation.get("/A")
                action = action.get_object() if action else {}
                kind = action.get("/S")
                target = action.get("/D", annotation.get("/Dest"))
                if kind == "/GoTo" or (kind is None and target is not None):
                    counts["internal_links"] += 1
                    if isinstance(target, str) and target not in destinations[name]:
                        errors.append(f"{name}:p{number}: missing destination {target}")
                elif kind == "/GoToR":
                    counts["cross_pdf_links"] += 1
                    file = action.get("/F", "")
                    if not isinstance(file, str):
                        file = file.get_object().get("/UF", file.get_object().get("/F", ""))
                    target_name = Path(file).name
                    if target_name not in readers:
                        errors.append(f"{name}:p{number}: missing target PDF {file}")
                    elif isinstance(target, str) and target not in destinations[target_name]:
                        errors.append(f"{name}:p{number}: {file}: missing destination {target}")
    return counts, errors


def source_reference_errors(root: Path) -> tuple[int, list[str]]:
    """Resolve ref/pageref (including starred forms) against compiled labels."""
    auxiliary = list((root / "entrega" / "_build").glob("*.aux"))
    if not auxiliary:
        return 0, ["No compiled .aux files; run compilar.ps1 before this audit."]
    labels = {}
    for path in auxiliary:
        pattern = r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{([^}]+)\}"
        for match in re.finditer(pattern, path.read_text(encoding="utf-8")):
            labels[(path.stem + ".pdf", match[1])] = match[2]
    checked = 0
    errors = []
    for path in sorted((root / "04").rglob("*.tex")):
        for number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
            if line.lstrip().startswith("%"):
                continue
            pattern = r"\\(?:ref|pageref|autoref|eqref)\*?\{([^}]+)\}|\\hyperref\[([^]]+)\]"
            for match in re.finditer(pattern, line):
                checked += 1
                target = match[1] or match[2]
                if not any(label == target for _, label in labels):
                    errors.append(f"{path.relative_to(root)}:{number}: missing label {target}")
            pattern = r"\\href\{([^}]+\.pdf)(?:\\)?#([^}]+)\}\{Tabla\s+([A-Z]?\.?\d+)"
            for match in re.finditer(pattern, line):
                actual = labels.get((match[1], match[2]))
                if actual is None or actual != match[3]:
                    errors.append(f"{path.relative_to(root)}:{number}: table {match[3]} != {actual}")
    return checked, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--t12", type=Path, required=True, help="Current T-12 PDF, supplied separately")
    parser.add_argument("--output", type=Path, help="Optional JSON evidence file")
    args = parser.parse_args()
    counts, errors = pdf_errors(args.root)
    counts["t12_page_citations"], page_errors = t12_errors(args.root, PdfReader(args.t12))
    counts["bibliography_citations"], bib_errors = bibliography_errors(args.root)
    errors.extend(page_errors)
    errors.extend(bib_errors)
    counts["source_references"], source_errors = source_reference_errors(args.root)
    errors.extend(source_errors)
    result = {"counts": counts, "errors": errors, "passed": not errors}
    output = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(output + "\n", encoding="utf-8")
    print(output)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
