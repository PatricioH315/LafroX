"""Genera la entrega de RT-25.10 a partir de los recursos del prototipo."""
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parents[1]
destination = root / "entrega/LafroX-Prototipo-SinConexion.zip"
destination.parent.mkdir(exist_ok=True)
html = (root / "index.html").read_text(encoding="utf-8")
html = re.sub(r'^.*<link [^>]+https://fonts\.google(?:apis|static)\.com[^>]+>\s*\n', '', html, flags=re.M)
instructions = """Prototipo LafroX para revisión sin conexión
1. Extraiga todo el ZIP en una carpeta.
2. Abra index.html en el navegador con JavaScript habilitado.
3. Entre por Ingresar, seleccione Evaluación y abra Flujo de un pedido.
Los datos y las integraciones de la demostración son simulados.
"""
with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
    archive.writestr("index.html", html)
    archive.writestr("LEEME.txt", instructions)
    archive.write(root / "abrir-prototipo.bat", "abrir-prototipo.bat")
    for folder in ("assets", "css", "js"):
        for path in sorted((root / folder).rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(root).as_posix())
print(destination)
