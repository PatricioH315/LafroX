from pathlib import Path
import json
def cargar():
    return json.loads(Path(__file__).with_name("consolidado.json").read_text(encoding="utf8"))["rnf"]
