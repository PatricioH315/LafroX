import fitz,re
from pathlib import Path

d=fitz.open('LafroX-Subdocumento7.pdf')
rows=[]
for i,p in enumerate(d):
    nums=sorted(set(int(x) for x in re.findall(r'Figura\s+7\.(\d+)',p.get_text())))
    if nums and i>4:
        rows.append((i+1,nums))
print(rows)
