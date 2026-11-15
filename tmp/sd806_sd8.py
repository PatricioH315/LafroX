from pathlib import Path
import re,subprocess,json,hashlib

r=Path(__file__).resolve().parents[1]
assert subprocess.check_output(['git','branch','--show-current'],cwd=r,text=True).strip()=='Lafrox_Subdocumento_8_Latex_Revision'
read=lambda p:(r/p).read_text(encoding='utf-8')
write=lambda p,s:(r/p).write_text(s,encoding='utf-8',newline='\n')
e=read('08_plan_riesgos/anexo-e-controles.tex')
e=e.replace('Al excluir del diseño previsto el control de identidad sin conexión, el control de stock antes identificado como CT-16 pasa a CT-15; CT-01--CT-14 conservan sus identificadores.',
            'CT-03 reúne identidad conectada y local conforme a S4/S9; CT-15 conserva stock, antes identificado como CT-16. Los 15 identificadores vigentes se mantienen; la ampliación de identidad no crea otra contingencia ni renumera stock.')
lines=e.splitlines()
for i,line in enumerate(lines):
    if line.startswith('CT-03 &'):
        lines[i]=r'CT-03 & SEG responde; ARQ diseña; DES/SRE ejecutan; CAL verifica. & Autenticación y sesión conectadas y locales, mínimo privilegio, detección, revocación y auditoría. Manifiesto de bodega de 26 h; al aislar una hora después quedan 25 h. Verificar relevos a las 8/16 h, firma, sitio, dispositivo, rol, PIN y turno. Reinicio/reloj no extienden vigencia. Reparto de 14,5 h con autorización máxima de 16 h desde emisión. & AL-ID-01 y AL-OFF-01 en resiliencia 3.8.4/3.9.3 antes de H5/H10; seguridad sin hallazgos críticos/altos antes de G5. Exigir cero accesos indebidos, cola conservada y conciliación única. Distinguir baja local inmediata y baja central durante aislamiento; verificar el detalle de esta ficha y 8.D.3. Corregir y repetir antes de habilitar. \\'
    elif line.startswith('CT-15 &'):
        lines[i]=r'CT-15 & DAT hasta mes 21; SRE desde 22; ARQ diseña; CAL verifica. & Una reserva central confirmada exige retención local durable de igual UUID, época y cantidad. Mantener una sola autoridad de escritura por ámbito; excluir escritor previo al promover, conciliar sitio/UUID y conservar capturas pendientes sin confirmar desde copia vencida. & AL-STOCK-01: última unidad concurrente, acuse perdido, reintento, cancelación y época obsoleta, sin doble reserva ni stock negativo; preventa real E1 (3.8.1), portal/EDI reales E2 (3.9.1). AL-DR-01: pérdida, promoción, retorno y conciliación (3.8.5/3.9.4), antes de H5/H10. CAL bloquea flujo inconsistente y exige corrección/regresión; simuladores no acreditan producto E2. \\'
    elif line.startswith('\\item[CT-03.]'):
        lines[i]=r'\item[CT-03.] S4, Anexo 4-M, AL-ID-01 y AL-OFF-01, y Anexo 4-R, controles 5.15/5.18, 8.5 y 8.15/8.16: identidad conectada y local, permisos, sesión, bajas y auditoría. S9, T-13, 7.5, asigna resiliencia 3.8.4/3.9.3 y define el expediente de AL-ID-01; T-17, 3.1, conserva versión y actas. La ficha incluye esa continuidad local; los controles de seguridad mantienen sus pruebas y puerta G5. La previsión documental no acredita implementación ni resultados.'
    elif line.startswith('\\item[CT-15 (stock).]'):
        lines[i]=r'\item[CT-15 (stock).] S4, Anexo 4-V, AL-STOCK-01, y Anexo 4-M, AL-DR-01, con procedimientos de conmutación/retorno de 4.3.2: retención local durable, exclusión del escritor previo y conciliación. T-13 de S9, 7.5, asigna 3.8.1 a preventa E1, 3.9.1 a preventa/portal/EDI E2 y 3.8.5/3.9.4 a recuperación. T-17, 3.1, conserva el expediente y el resultado por etapa. Un simulador no acredita producto E2. CT-16 histórico de stock equivale a CT-15 vigente; la identidad local antes separada se integra en CT-03, sin reutilizar CT-15 para identidad.'
e='\n'.join(lines)+'\n'
e=e.replace('Para CT-03--CT-07 no se acredita aún correspondencia individual con casos de S9;', 'Para CT-04--CT-07 no se acredita aún correspondencia individual con casos de S9;')
e+=r'''
\subsection*{Condiciones de identidad local de CT-03}
El manifiesto de bodega dura 26 h y el ensayo corta el enlace una hora después
de emitirlo: quedan 25 h verificables. La caché descriptiva de 24 h no emite
credenciales ni amplía el manifiesto. En los relevos a las 8 y 16 h del corte se
validan firma, emisor, sitio, dispositivo enrolado, rol, PIN y turno vigente;
sin enlace no se habilitan cuentas no preinscritas ni privilegios nuevos.
Manifiesto o turno vencido, permiso inválido, firma alterada o PIN incorrecto
se deniegan y auditan. Reinicio, actividad o retroceso del reloj no extienden
vigencia; sin continuidad demostrable de la hora confiable se deniega sesión nueva.

En reparto, la autorización se emite dentro de la hora previa a salir, cubre
la ruta de 14,5 h y expira al fin programado más 30 min, con máximo de 16 h
desde su emisión. Al vencer, se deniegan nuevas operaciones protegidas y se
conserva la cola. La reautenticación conectada permite conciliar una sola vez
los hechos anteriores al vencimiento; otra ruta exige autorización nueva.

Una baja conocida en el sitio deniega acceso local inmediato. Una baja conocida
sólo por la autoridad central durante el aislamiento deja exposición hasta la
expiración: no se promete revocación remota instantánea. Al reconectar se bloquea
la sesión y se ponen en cuarentena los eventos posteriores a la baja para
conciliación, sin borrarlos. El expediente de AL-ID-01 conserva emisión,
expiración, huella del manifiesto, política, versión del verificador, tiempos,
decisiones y UUID; excluye PIN y secretos. CAL y SEG verifican resultados y
la aprobación competente habilita sólo el alcance probado.
'''
write('08_plan_riesgos/anexo-e-controles.tex',e)

a=read('LAFROX-Subdocumento8-Anexos.tex')
a=a.replace('tras retirar el antiguo CT-15 de identidad, el control de stock pasa de CT-16 a CT-15, sin cambiar CT-01--CT-14.', 'CT-15 conserva stock, antes CT-16, e identidad conectada/local se integra en CT-03; no se renumeran los 15 controles vigentes.')
old=next(l for l in a.splitlines() if l.startswith('Identidad / CT-03 &'))
new=r'Identidad / CT-03 & Autenticación conectada y local con manifiesto, permisos, turno y dispositivo válidos; expiración y baja sin ampliar vigencia. & SEG responde; ARQ diseña; DES/SRE ejecutan; CAL verifica con TI/Operaciones. & AL-ID-01 y AL-OFF-01 antes de H5/H10: 26 h, corte una hora después, relevos a las 8/16 h y ruta de 14,5 h acotada a 16 h. Denegaciones, cola y conciliación conforme a 8.E y matriz 8.D.3; seguridad conserva G5. \\'
a=a.replace(old,new)
old=next(l for l in a.splitlines() if l.startswith('Stock / CT-15 &'))
new=r'Stock / CT-15 & Reserva central confirmada sólo con retención local durable; autoridad única por ámbito, exclusión del escritor anterior y conciliación de UUID, sitio y época. & DAT hasta mes 21; SRE desde 22; ARQ diseña; CAL verifica. & AL-STOCK-01: última unidad, pérdida de acuse y reintento sin doble reserva; preventa E1 y portal/EDI reales E2. AL-DR-01: pérdida, promoción, retorno y conciliación. R-004 trata inventario inicial y R-017 conectividad; no duplicar contingencia. \\'
a=a.replace(old,new)

sd4=subprocess.check_output(['git','rev-parse','LafroX-Subdoc4-LateX-corrigiendo'],cwd=r,text=True).strip()
sd9=subprocess.check_output(['git','rev-parse','LafroX-Subdoc9-LateX-corrigiendo'],cwd=r,text=True).strip()
matrix=r'''
\clearpage
\subsection*{Correspondencia de continuidad y evidencia de SD8-06}
\addcontentsline{toc}{subsection}{Correspondencia de continuidad y evidencia de SD8-06}
La matriz 8.D.3 enlaza diseño, riesgo/control y pruebas de S4/S9. Se consultan
las ramas corregidas: S4, \texttt{SD4HASH}, y S9, \texttt{SD9HASH}.
Los commits identifican versiones documentales, no implementaciones probadas.
No se dispone aquí de configuraciones de producto, trazas, mediciones ni actas
de ejecución o aceptación de los tres alcances; se registran como evidencia por obtener.

\begingroup
\renewcommand{\thetable}{8.D.3}
\begin{landscape}
\setlength{\textwidth}{\linewidth}
\renewcommand{\arraystretch}{1.08}
\begin{tablalafrox}{Correspondencia SD8-06: diseño, prueba y evidencia requerida. Fuente: S4, anexos 4-M/4-V y 4.3.2; S9, T-13/T-17.}{tab:sd806-correspondencia}{F{0.11} F{0.18} F{0.19} F{0.15} Y}{\cab{Tema / S8} & \cab{Referencia exacta S4} & \cab{Protocolo y campaña S9} & \cab{Responsable} & \cab{Evidencia requerida y estado}}
ERP / R-034 & Anexo 4-M, AL-DTE-01 y AL-DR-01; 4.3.2, recuperación de Talca y ERP; Anexo 4-V, correspondencia de aceptación. & T-13, 7.5: AL-DTE-01 en resiliencia 3.8.4/3.9.3; AL-DR-01 en recuperación 3.8.5/3.9.4, antes de H5/H10. T-17, 3.1. & ARQ/SRE; TI, Finanzas y Operaciones; CAL verifica y JP registra. & Versión de carga, folio, guía/anulación, acuse y tiempos de 96 salidas, con ERP disponible, indisponible y cambio de carga. RTO de 4 h y RPO de 15 min medidos. Bloquear sin guía válida; recuperar WMS no recupera ERP. Estado: sincronizado documentalmente; implementación, ensayos y acta pendientes. \\
Stock / CT-15 & Anexo 4-V, AL-STOCK-01; Anexo 4-M, AL-DR-01; 4.3.2, conmutación y retorno. & T-13, 7.5: AL-STOCK-01 en integración 3.8.1 (E1) y 3.9.1 (E2); AL-DR-01 en 3.8.5/3.9.4. T-17, 3.1. & DAT hasta 21, SRE desde 22; ARQ diseña; CAL verifica; JP registra. & Estado central/local con retención durable, última unidad, UUID/época, acuses perdidos, exclusión del escritor previo, retorno y conciliación. Preventa real E1; preventa, portal y EDI reales E2. Sin doble reserva ni stock negativo; simulador no acredita E2. Estado: sincronizado documentalmente; implementación, ensayos y acta pendientes. \\
Identidad / CT-03 & Anexo 4-M, AL-ID-01 y AL-OFF-01; Anexo 4-R, controles de identidad; Anexo 4-V, correspondencia. & T-13, 7.5: AL-ID-01 y AL-OFF-01 en resiliencia 3.8.4/3.9.3 antes de H5/H10. T-17, 3.1; seguridad conserva puerta G5. & SEG responde; ARQ diseña; DES/SRE ejecutan con TI/Operaciones; CAL verifica. & Manifiesto de 26 h, corte a una hora, relevos 8/16 h; ruta de 14,5 h y máximo 16 h. Probar expiración, firma, turno, permisos, reinicio/reloj y baja local/central aislada; cero accesos indebidos, cola conservada y conciliación única. Sin PIN ni secretos en expediente. Estado: sincronizado documentalmente; implementación, ensayos y acta pendientes. \\
\end{tablalafrox}
\end{landscape}
\endgroup

\paragraph{Decisión por alcance y etapa}
CAL comprueba versión, configuración, entradas, resultado esperado y observado,
incidencias y repetición tras corrección; JP registra fecha y próxima revisión.
Un protocolo previsto o un PDF compilado no sustituyen una ejecución.
Resultado insuficiente o fallido mantiene el bloqueo y exige corregir y repetir.
Sólo evidencia satisfactoria y aprobación competente habilitan el alcance
concreto; T-17, 3.1, integra el expediente H5/H10 y la Contraparte Técnica acepta
con acta. Un bloqueo correcto de salida sin guía no demuestra continuidad de las
96 salidas. Los controles son obligaciones ordinarias del proveedor, sin nuevas
HH de contingencia. SD8-06 permanece parcial hasta acreditar implementación y
ejecución satisfactoria con las actas exigidas; las valoraciones de T-16 se conservan.

'''.replace('SD4HASH',sd4[:12]).replace('SD9HASH',sd9[:12])
a=a.replace('\\input{08_plan_riesgos/anexo-e-controles.tex}',matrix+'\\input{08_plan_riesgos/anexo-e-controles.tex}')
write('LAFROX-Subdocumento8-Anexos.tex',a)
b=read('08_plan_riesgos/contenido.tex')
old=next(l for l in b.splitlines() if l.startswith('La autenticación, el mínimo privilegio'))
new=('La autenticación conectada y local, el mínimo privilegio, la revocación y la auditoría se verifican mediante CT-03 y AL-ID-01/AL-OFF-01. '
     'Se conserva el manifiesto de bodega de 26 h, corte una hora después, dos relevos a las 8/16 h y reparto de 14,5 h con autorización máxima de 16 h; '
     'la baja local conocida se distingue de la baja central durante aislamiento. CT-15 conserva stock con retención local durable y autoridad única; '
     'CT-16 histórico de stock equivale al CT-15 vigente. La matriz 8.D.3 relaciona R-034, CT-15 y CT-03 con diseño, campañas, responsables y evidencia de S4/S9. '
     'La sincronización documental no acredita implementación ni aceptación: SD8-06 permanece parcial hasta contar con resultados y actas. '
     'R-017 conserva la conectividad externa; estos controles no añaden riesgos ni HH de contingencia.')
b=b.replace(old,new);write('08_plan_riesgos/contenido.tex',b)
t=read('LAFROX-Formulario-T-16.tex')
needle='\\begin{landscape}'
note=('La matriz 8.D.3 traza R-034 (ERP), CT-15 (stock) y CT-03 (identidad conectada/local) a S4 y T-13/T-17 de S9. '
      'Se conserva ERP como único emisor, stock con retención local durable e identidad local conforme a AL-ID-01. '
      'Los 36 riesgos, sus valoraciones y reservas no cambian por esta sincronización. SD8-06 continúa parcial: '
      'faltan evidencia de implementación, resultados de ejecución y actas de aceptación; las pruebas previstas no los acreditan.\n\n')
t=t.replace(needle,note+needle,1);write('LAFROX-Formulario-T-16.tex',t)
report={'fecha':'2026-11-15','estado':'documentación sincronizada; implementación, ensayos y aceptación pendientes',
        'sd4':{'rama':'LafroX-Subdoc4-LateX-corrigiendo','commit':sd4},
        'sd9':{'rama':'LafroX-Subdoc9-LateX-corrigiendo','commit':sd9},
        'sd8':{'rama':'Lafrox_Subdocumento_8_Latex_Revision','base':'20289fe0','estado':'cambios locales de SD8-04/05/06 sin commit'}}
write('tmp/sd806-versiones.json',json.dumps(report,ensure_ascii=False,indent=2))
print(sd4,sd9,'CT-03 ampliado; matriz 8.D.3 incorporada.')
