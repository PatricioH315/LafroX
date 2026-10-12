from PIL import Image, ImageOps, ImageDraw
from pathlib import Path
import sys
p=Path(sys.argv[1])
fs=sorted(p.glob('page-*.png'), key=lambda x:int(x.stem.split('-')[-1]))
thumbw=260; pad=12; thumbs=[]
for f in fs:
    im=Image.open(f).convert('RGB')
    h=round(im.height*thumbw/im.width)
    im=ImageOps.expand(im.resize((thumbw,h)), border=1, fill='gray')
    thumbs.append((f.name,im))
cols=4; rows=(len(thumbs)+cols-1)//cols
cellh=max(im.height for _,im in thumbs)+30
sheet=Image.new('RGB',(cols*(thumbw+pad)+pad,rows*cellh+pad),'white')
d=ImageDraw.Draw(sheet)
for i,(n,im) in enumerate(thumbs):
    x=pad+(i%cols)*(thumbw+pad); y=pad+(i//cols)*cellh
    d.text((x,y),n,fill='black'); sheet.paste(im,(x,y+22))
sheet.save(p/'contact.png')
