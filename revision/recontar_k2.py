"""Recuento de solo lectura de los catálogos activos y el T-12.

Uso: python revision/recontar_k2.py [ruta_SD3] [ruta_SD5]
Imprime JSON; no modifica fuentes ni estados.
"""
from pathlib import Path
from collections import Counter
import re,json,sys

sd3=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
sd5=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else sd3.parent/'LafroX-Subdoc5-LateX'
def rows(path):
    s=path.read_text(encoding='utf8')
    for m in re.finditer(r'(?m)^\s*((?:RF|RNF|RT)-[\w.-]+)\s*&',s):
        end=s.find('\\\\',m.end());assert end>=0
        cells=re.split(r'(?<!\\)&',s[m.start():end].strip())
        yield m[1],[re.sub(r'\s+',' ',x).strip() for x in cells]
catalog=[]
for file in ['rf_caso','rf_btt','rf_propios','rnf_caso','rnf_btt','rnf_propios']:
    catalog.extend(rows(sd3/'tablas_anexo'/(file+'.tex')))
t12=list(rows(sd3/'LAFROX-Formulario-T-12.tex'));cat={id:c for id,c in catalog};matrix={id:c for id,c in t12}
assert len(cat)==len(catalog) and len(matrix)==len(t12),'IDs duplicados'
result={'catalogo_unico':len(cat),'clases_catalogo':dict(Counter(id.split('-')[0] for id in cat)),'prioridades':dict(Counter(c[-2].split('/')[0].strip() for c in cat.values())),'filas_t12':len(t12),'clases_t12':dict(Counter(id.split('-')[0] for id in matrix)),'estados_t12':dict(Counter(c[2] for c in matrix.values())),'estados_por_clase':{cl:dict(Counter(c[2] for id,c in matrix.items() if id.startswith(cl+'-'))) for cl in ['RF','RNF','RT']},'aliases_absorbidos':sorted(id for id in matrix if not id.startswith('RT-') and id not in cat),'catalogo_sin_t12':sorted(set(cat)-set(matrix))}
if sd5.exists():
    entities={}
    for n in range(2,11):
        for line in (sd5/f'05_modelo_datos/anexos/tablas/A_{n}.tex').read_text(encoding='utf8').splitlines():
            line=line.replace('\\allowbreak{}','').replace('\\_','_')
            m=re.match(r'\s*\\texttt\{([^}]*)\}\s*&\s*\\texttt\{([^}]*)\}',line)
            if m:entities.setdefault(m[1],[]).append(m[2])
    result['entidades_sd5']=len(entities);result['atributos_sd5']=sum(map(len,entities.values()))
    result['atributos_duplicados']={e:[a for a,n in Counter(attrs).items() if n>1] for e,attrs in entities.items() if len(attrs)!=len(set(attrs))}
print(json.dumps(result,ensure_ascii=False,indent=2))
