"""Comprueba contenido publicado, compilacion y correspondencia del borrador SD10."""
from pathlib import Path
import hashlib
import json
import re
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
def normalize(text):
    return re.sub(r"\s+", "", re.sub(r"-\s*\n\s*", "", text)).casefold()

results = {"proyecto": "LafroX", "version": "0.2", "estado": "borrador",
           "fecha": "2026-11-17", "pdfs": []}
for stem in ("LAFROX-Subdocumento10", "LAFROX-Subdocumento10-Anexos"):
    path = ROOT / (stem + ".pdf")
    reader = PdfReader(path)
    pages = [p.extract_text() or "" for p in reader.pages]
    assert all(len(text) > 100 for text in pages), "Pagina vacia"
    assert all("??" not in text for text in pages), "Referencia sin resolver"
    full = normalize("\n".join(pages))
    for term in ("Referencias", "Declaración de uso de IA",
                 "Sin revisión humana acreditada", "Uso de IA por sección y anexo"):
        assert normalize(term) in full, (stem, term)
    assert normalize("El usuario autorizó") not in full
    assert normalize("por indicación del usuario") not in full
    assert not re.search(r"tabla[\d.]+[—–-]?continuaci[oó]n", full), "Revisar tabla partida"
    ia = [p for p in pages if normalize("Uso de IA por sección y anexo") in normalize(p)
          and normalize("Herramienta") in normalize(p)]
    assert len(ia) == 1, "La tabla de IA debe estar completa en una pagina"
    for section in ("10.1", "10.2", "10.A", "10.B", "10.C", "10.D", "10.E"):
        assert section in ia[0], section
    if not stem.endswith("Anexos"):
        assert normalize("Introducción a los Servicios") in full
        assert normalize("Hardware no crítico") in full
        assert normalize("resolución en 24 h") in full
    else:
        for number in range(1, 10):
            assert f"GU-{number:02}" in full.upper()
        for term in ("13 meses", "30 días", "24 meses", "12 meses",
                     "media: a solicitud", "sin base de cálculo"):
            assert normalize(term) in full, term
    log = (ROOT / (stem + ".log")).read_text(encoding="utf-8", errors="replace")
    for error in ("Overfull", "undefined references", "Missing character",
                  "LaTeX Error", "! Undefined"):
        assert error not in log, (stem, error)
    results["pdfs"].append({
        "archivo": path.name, "paginas": len(reader.pages),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "errores_compilacion": 0, "referencias_sin_resolver": 0,
        "desbordes_horizontales": 0, "tablas_partidas": 0
    })

main = (ROOT / "10_servicios_operacion/contenido.tex").read_text(encoding="utf-8")
assert r"\chapter{Introducción a los Servicios}" in main
trace = (ROOT / "trazabilidad/SD10_fuentes_y_brechas.md").read_text(encoding="utf-8")
assert all(f"V02-{i:02}" in trace for i in range(1, 13))
assert all(f"B-{i:02}" in trace for i in range(1, 11))
results.update({"cambios_mejora_trazados": 12, "dependencias_documentadas": 10,
                "guias_desarrolladas": 9, "revision_humana_acreditada": False,
                "pruebas_reales_acreditadas": False})
(ROOT / "verificacion/resultado_entrega.json").write_text(
    json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(results, ensure_ascii=False, indent=2))
