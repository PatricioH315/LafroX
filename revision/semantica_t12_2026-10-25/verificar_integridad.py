"""Comprueba integridad del registro; no decide cumplimiento semántico."""
from pathlib import Path
import collections, json, re, subprocess
root=Path(__file__).resolve().parents[2]
ledger=json.loads(Path(__file__).with_name("matriz_revision.json").read_text(encoding="utf-8"))
def rows(text):
    return [line.strip().removesuffix("\\\\").strip().split(" & ") for line in text.splitlines() if re.match(r"^\s*(?:RF|RNF|RT)-\d",line)]
current=rows((root/"LAFROX-Formulario-T-12.tex").read_text(encoding="utf-8-sig"))
base=ledger["revision"]["ramas_consultadas"]["3"]["commit_al_iniciar_revision"]
original=rows(subprocess.check_output(["git","-C",str(root),"show",base+":LAFROX-Formulario-T-12.tex"]).decode("utf-8-sig"))
assert len(current)==len(original)==len(ledger["filas"])==653
assert len({r[0] for r in current})==653
assert [(r[0],r[1]) for r in current]==[(r[0],r[1]) for r in original],"Exigencia alterada"
audit={r["id"]:r for r in ledger["filas"]}
for row in current:
    assert len(row)==6
    r=audit[row[0]]
    assert r["revision_semantica_completada"] and r["observacion_individual"] and r["fuentes_de_exigencia"]
    assert [r["exigencia"],r["estado_final"],r["respuesta_final"],r["secciones_de_respaldo_declaradas"]]==[row[1],row[2],row[3],row[5]]
    assert re.findall(r"\b\d+(?:\.\d+)+\b",row[4])==[p["codigo"] for p in r["EDT"]]
assert dict(collections.Counter(r[2] for r in current))==ledger["revision"]["cobertura"]
print("PASS: 653 filas, exigencias conservadas y registro sincronizado; el juicio semántico requiere lectura.")
