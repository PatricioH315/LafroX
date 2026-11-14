import subprocess,re,csv,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf8')
git=lambda p:subprocess.check_output(['git','show','origin/LafroX-Subdoc4-LateX-corrigiendo:'+p]).decode('utf8')
btt=git('Bases/Bases_Tecnicas_Transversales.md')
caso=git('Bases/Caso_02_Logistica.md')
rx=r'\*\*(RT-\d{2}\.\d{2})\*\*'
bids=set(re.findall(rx,btt)); cids=set(re.findall(rx,caso))
rows=list(csv.DictReader(open('trazabilidad/auditoria_pendientes_sd3.csv',encoding='utf-8-sig')))
problems=[]
for r in rows:
    origin=r['origen_declarado']
    for seg in origin.split(';'):
        vals=re.findall(r'RT-\d{2}\.\d{2}',seg)
        is_btt=bool(re.search(r'BTT|Transversales',seg,re.I))
        is_case=bool(re.search(r'Caso',seg,re.I))
        for val in vals:
            if is_btt and val not in bids: problems.append((r['id'],val,'BTT'))
            if is_case and val not in cids: problems.append((r['id'],val,'Caso'))
print('IDs BTT',len(bids),'Caso',len(cids),'candidatos de origen',len(problems))
for row in problems: print(' | '.join(row))
