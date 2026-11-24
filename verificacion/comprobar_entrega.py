"""Comprueba contenido publicado, compilacion y correspondencia del borrador SD10."""
from pathlib import Path
import hashlib
import json
import re
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
def normalize(text):
    return re.sub(r"\s+", "", re.sub(r"-\s*\n\s*", "", text)).casefold()

results = {"proyecto": "LafroX", "version": "1.0", "estado": "correccion local verificada",
           "fecha": "2026-11-24", "pdfs": []}
for stem in ("LAFROX-Subdocumento10", "LAFROX-Subdocumento10-Anexos"):
    path = ROOT / (stem + ".pdf")
    reader = PdfReader(path)
    pages = [p.extract_text() or "" for p in reader.pages]
    for page in reader.pages:
        assert (round(float(page.mediabox.width)), round(float(page.mediabox.height))) == (612, 792)
    assert all(len(text) > 100 for text in pages), "Página sin contenido suficiente"
    assert all(text.split()[-1] == str(number) for number, text in enumerate(pages, 1)), (
        stem, "Foliación discontinua"
    )
    assert all("??" not in text for text in pages), "Referencia sin resolver"
    toc_links = [a.get_object() for a in reader.pages[1].get("/Annots", [])]
    assert any(a.get("/Subtype") == "/Link" for a in toc_links), (stem, "Índice sin enlaces")
    assert not re.search(r"\b(?:UF|CLP|USD)\s*\d|\d\s*(?:UF|CLP|USD)\b", "\n".join(pages)), (
        stem, "Revisar valores monetarios en la oferta técnica"
    )
    full = normalize("\n".join(pages))
    assert normalize("Referencias") in full, (stem, "Referencias")
    assert normalize("El usuario autorizó") not in full
    assert normalize("por indicación del usuario") not in full
    assert normalize("aún en plantilla") not in full
    assert not re.search(r"tabla[\d.]+[—–-]?continuaci[oó]n", full), "Revisar tabla partida"
    ia = [p for p in pages if normalize("Uso de IA por sección y anexo") in normalize(p)
          and normalize("Herramienta") in normalize(p)]
    if stem.endswith("Anexos"):
        assert not ia, "La tabla de IA se incluye solo en el SD10 principal"
        for term in ("Declaración de uso de IA", "Uso de IA por sección y anexo"):
            assert normalize(term) not in full, (stem, term)
    else:
        assert normalize("Declaración de uso de IA") in full
        assert len(ia) == 1, "La tabla de IA debe estar completa en una pagina"
        for section in ("10.1", "10.2", "10.A", "10.B", "10.C", "10.D", "10.E"):
            assert section in ia[0], section
    if not stem.endswith("Anexos"):
        assert normalize("Introducción a los Servicios") in full
        assert normalize("Hardware no crítico") in full
        assert normalize("resolución en 24 h") in full
        for term in ("10.3.3", "H3/M6", "diez días hábiles", "carga intacta", "no reduce el denominador", "casa matriz de Talca"):
            assert normalize(term) in full, (stem, term)
    else:
        for number in range(1, 10):
            assert f"GU-{number:02}" in full.upper()
        for term in ("13 meses", "30 días", "24 meses", "12 meses",
                     "media: a solicitud", "sin base de cálculo", "cinco días hábiles",
                     "V17", "Comprobación de recorridos de negocio",
                     "Ensayos y evidencia de aceptación", "Prueba de intrusión independiente",
                     "Para cada dispositivo de reparto", "eventos pendientes de las últimas 24 horas",
                     "Cobertura de guías y automatización", "B-11",
                     "Contactos adicionales mensuales por perfil", "Respuesta por franja de peak",
                     "Presupuesto de tiempos internos propuesto", "Objetivos analíticos y térmicos"):
            assert normalize(term) in full, term
    log = (ROOT / (stem + ".log")).read_text(encoding="utf-8", errors="replace")
    for error in ("Overfull", "undefined references", "Missing character",
                  "LaTeX Error", "! Undefined"):
        assert error not in log, (stem, error)
    results["pdfs"].append({
        "archivo": path.name, "paginas": len(reader.pages),
        "formato": "carta",
        "foliacion_correlativa": True,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "errores_compilacion": 0, "referencias_sin_resolver": 0,
        "desbordes_horizontales": 0, "tablas_partidas": 0
    })

main = (ROOT / "10_servicios_operacion/contenido.tex").read_text(encoding="utf-8")
assert r"\chapter{Introducción a los Servicios}" in main
trace = (ROOT / "trazabilidad/SD10_fuentes_y_brechas.md").read_text(encoding="utf-8")
assert all(f"V02-{i:02}" in trace for i in range(1, 13))
assert all(f"B-{i:02}" in trace for i in range(1, 12))
audit_ids = re.findall(r"^\| ([CL][0-9]{2}) \|", trace, re.MULTILINE)
assert sorted(audit_ids) == [f"{prefix}{i:02}" for prefix in ("C", "L") for i in range(1, 17)]
offer_ids = re.findall(r"^\| O04-([0-9]{2}) \|", trace, re.MULTILINE)
assert sorted(offer_ids) == [f"{i:02}" for i in range(1, 14)]
review_ids = re.findall(r"^\| CO05-([0-9]{2}) \|", trace, re.MULTILINE)
assert sorted(review_ids) == [f"{i:02}" for i in range(1, 17)]
results.update({"puntos_auditoria_trazados": len(audit_ids), "puntos_oferta_v04_trazados": len(offer_ids),
                "puntos_v05_trazados": len(review_ids), "cambios_mejora_v02_trazados": 12, "dependencias_documentadas": 11,
                "guias_desarrolladas": 9, "revision_humana_verificada_en_esta_tarea": False,
                "pruebas_reales_acreditadas": False})
(ROOT / "verificacion/resultado_entrega.json").write_text(
    json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(results, ensure_ascii=False, indent=2))
