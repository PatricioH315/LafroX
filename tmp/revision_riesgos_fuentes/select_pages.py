from pathlib import Path
import json, re

rows=[json.loads(x) for x in Path('tmp/revision_riesgos_fuentes/pages.jsonl').read_text(encoding='utf-8').splitlines()]
queries={
'REC-012':[('Subdocumento 4\\LAFROX-Subdocumento4.pdf',[72,144]),('Subdocumento 7\\LafroX-Formulario-T-14.pdf',[87])],
'REC-014':[('Subdocumento 4\\LAFROX-Subdocumento4.pdf',[144]),('Subdocumento 5\\LAFROX-Subdocumento5.pdf',[19,20])],
'REC-015':[('Subdocumento 4\\LAFROX-Subdocumento4-Anexos.pdf',[65]),('Subdocumento 7\\LafroX-Formulario-T-14.pdf',[87])],
'REC-035':[('Subdocumento 3\\LAFROX-Subdocumento3-Anexos.pdf',[153]),('Subdocumento 7\\LafroX-Formulario-T-18.pdf',[13,14]),('Subdocumento 6\\LAFROX-Subdocumento6-Anexos.pdf',[7])],
'REC-036':[('Subdocumento 3\\LAFROX-Subdocumento3-Anexos.pdf',[126]),('Subdocumento 6\\LAFROX-Subdocumento6-Anexos.pdf',[6])],
'REC-042':[('Subdocumento 7\\LafroX-Formulario-T-18.pdf',[11,13]),('Subdocumento 7\\LafroX-Formulario-T-14.pdf',[81])],
'REC-049':[('Subdocumento 4\\LAFROX-Subdocumento4.pdf',[143]),('Subdocumento 7\\LafroX-Formulario-T-14.pdf',[90])],
'REC-057':[('Subdocumento 4\\LAFROX-Subdocumento4-Anexos.pdf',[54]),('Subdocumento 4\\LAFROX-Subdocumento4.pdf',[104])],
'REC-061':[('Subdocumento 4\\LAFROX-Subdocumento4-Anexos.pdf',[64,65]),('Subdocumento 7\\LafroX-Formulario-T-14.pdf',[88])],
'REC-062':[('Subdocumento 4\\LAFROX-Subdocumento4-Anexos.pdf',[65]),('Subdocumento 4\\LAFROX-Subdocumento4.pdf',[47])],
'REC-063':[('Subdocumento 4\\LAFROX-Subdocumento4-Anexos.pdf',[65]),('Subdocumento 3\\LAFROX-Subdocumento3-Anexos.pdf',[122])],
}
page_map={(r['file'],r['page']):r['text'] for r in rows}
out=[]
for risk,items in queries.items():
    out.append('# '+risk)
    for file,pages in items:
        for page in pages:
            text=page_map.get((file,page),'[MISSING]')
            out.append(f'## {file} p.{page}\n{text}\n')
Path('tmp/revision_riesgos_fuentes/selected_pages.md').write_text('\n'.join(out),encoding='utf-8')
print(len(out),'sections',len('\n'.join(out)),'characters')
