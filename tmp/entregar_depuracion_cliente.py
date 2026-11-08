from pathlib import Path
import shutil,hashlib
r=Path(__file__).resolve().parents[1]
for name in ['LAFROX-Subdocumento8','LAFROX-Subdocumento8-Anexos','LAFROX-Formulario-T-16']:
 a=r/'tmp/limpieza-s8-build'/(name+'.pdf');b=r/(name+'.pdf')
 shutil.copy2(a,b)
 assert hashlib.sha256(a.read_bytes()).digest()==hashlib.sha256(b.read_bytes()).digest()
 print('PDF actualizado:',name)
(r/'odd/tasks/interno-s8/depuracion-redaccion-cliente.md').write_text('Revisión editorial adicional: 20 ajustes de redacción autorreferencial y aclaraciones repetidas. No se encontraron nuevas referencias explícitas a numeración retirada o versiones anteriores. Se mantienen las condiciones de aprobación, evidencia y eficacia; las cifras de las tablas técnicas y la declaración completa de IA se comprobaron contra tmp/depuracion-cliente-base.json. PDF recompilados con referencias estabilizadas y revisión visual de las páginas afectadas. No se modificaron otros subdocumentos.',encoding='utf-8')
