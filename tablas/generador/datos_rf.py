from pathlib import Path
import json
def cargar():
    return {x["id"]: x for x in json.loads(Path(__file__).with_name("consolidado.json").read_text(encoding="utf8"))["rf"]}
