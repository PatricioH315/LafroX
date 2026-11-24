"""Rasteriza assets/decor/*.svg a assets/decor/png/*.png (fallback para Google Slides).
Requiere PyMuPDF:  python -I tools/rasterize_decor.py
"""
import pathlib
import pymupdf

ROOT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "decor"
LONG_SIDE = 2400
(ROOT / "png").mkdir(exist_ok=True)
for svg in sorted(ROOT.glob("*.svg")):
    doc = pymupdf.open(str(svg))
    pdf = pymupdf.open("pdf", doc.convert_to_pdf())
    page = pdf[0]
    zoom = LONG_SIDE / max(page.rect.width, page.rect.height)
    pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha=True)
    pix.save(str(ROOT / "png" / (svg.stem + ".png")))
    print(svg.stem, pix.width, pix.height)
