from pathlib import Path
import subprocess
r=Path(__file__).resolve().parents[1]
assert subprocess.check_output(['git','branch','--show-current'],cwd=r,text=True).strip()=='LafroX-Subdoc9-LateX-corrigiendo'
def edit(name,needle,addition):
    p=r/name; data=p.read_bytes(); ending='\r\n' if b'\r\n' in data else '\n'
    s=data.decode('utf-8').replace('\r\n','\n');assert s.count(needle)==1
    s=s.replace(needle,addition+needle);p.write_bytes(s.replace('\n',ending).encode('utf-8'))
edit('SD9_v_nueva/T13/contenido.tex',r'\textbf{AL-ID-01. Identidad local durante el corte.}',r'''
\paragraph{Correspondencia con S8 y control de evidencia}
R-034 de S8 identifica la dependencia del ERP; CT-15, la consistencia del stock;
CT-03, la identidad conectada y local. El Anexo 4-V de S4 recoge la misma
correspondencia y el Anexo 4-M define continuidad e identidad. AL-DTE-01 usa
resiliencia 3.8.4/3.9.3 y AL-DR-01 recuperación 3.8.5/3.9.4; sus resultados
deben distinguir recuperación WMS de restitución ERP, RTO de 4 h, RPO de 15 min
y continuidad de las 96 salidas con guía válida. AL-STOCK-01 usa integración
3.8.1 en E1 y 3.9.1 en E2: probar retención local durable, última unidad,
acuse perdido, UUID y época, sin doble reserva ni stock negativo. El retorno
exige excluir al escritor previo y conciliar con AL-DR-01.

AL-ID-01 y AL-OFF-01 usan resiliencia 3.8.4/3.9.3. Las condiciones detalladas
de manifiesto de 26 h, aislamiento a una hora, relevos a las 8/16 h, reparto
de 14,5 h y máximo de 16 h, reloj, expiración y baja durante aislamiento se
vinculan a CT-03; no alteran su puerta de seguridad G5. CAL contrasta cobertura
real de etapa y versión con el expediente T-17, 3.1; un simulador no acredita
portal o EDI de E2. Los protocolos son pruebas por ejecutar: faltan registros
de implementación, resultados y actas para declarar su eficacia. Evidencia
insuficiente o prueba fallida mantienen el bloqueo hasta corregir y repetir.

''')
edit('SD9_v_nueva/T17/contenido.tex',r'\subsection*{3.2 Definición de terminado (RT-20.07)}',r'''
\paragraph{Expediente de continuidad: correspondencia SD8-06}
El expediente de H5/H10 relaciona los tres temas siguientes con S8, matriz
8.D.3, S4, anexos 4-M/4-V, y las campañas del T-13, 7.5. Cada registro identifica
versión o digest, configuración, datos de entrada, fecha, responsables,
resultado esperado y observado, trazas, incidencias, corrección, repetición y
acta de la Contraparte Técnica. Una referencia documental no acredita ejecución.

\begin{tablasimple}{Y Y Y}
{\cab{Tema y referencia S8} & \cab{Prueba y cobertura exigida} & \cab{Evidencia para decisión}}
ERP / R-034 & AL-DTE-01 en 3.8.4/3.9.3; AL-DR-01 en 3.8.5/3.9.4, antes de H5/H10. ERP único emisor, disponible e indisponible y carga modificada. & Folio, guía vigente, anulación/nueva emisión, acuse y tiempos para 96 salidas. RTO de 4 h y RPO de 15 min medidos. Bloqueo correcto no equivale a continuidad; recuperar WMS no restituye ERP. \\
Stock / CT-15 & AL-STOCK-01 en 3.8.1 para preventa E1 y 3.9.1 para preventa, portal y EDI reales E2; AL-DR-01 para conmutación/retorno. & Retención local durable, estado central/local, última unidad, UUID/época, pérdida de acuse y exclusión de escritor previo. Conciliación, p95, cero doble reserva y ningún stock negativo. Simuladores no acreditan producto E2. \\
Identidad / CT-03 & AL-ID-01 y AL-OFF-01 en 3.8.4/3.9.3; identidad conectada y local, antes de H5/H10, sin sustituir seguridad G5. & Manifiesto de 26 h y corte a una hora; relevos 8/16 h; reparto 14,5 h y máximo 16 h. Firma, turno, permisos, expiración, reloj/reinicio y baja local/central aislada: cero accesos indebidos, cola conservada y conciliación única. Excluir PIN y secretos. \\
\end{tablasimple}
\fuentesd{Fuente: (SD4, anexos 4-M y 4-V); (SD8, R-034, CT-15, CT-03 y matriz 8.D.3); (T-13, sección 7.5).}

CAL verifica con ARQ/SRE, DAT y SEG según el tema; JP registra el estado por
alcance y etapa, y TI/Operaciones aportan configuración y validaciones de su
competencia. Estado inicial: documentación sincronizada, implementación y
ejecución sin evidencia aportada y aceptación sin acta. Resultado insuficiente
o fallido mantiene el bloqueo y exige corregir y repetir. Sólo evidencia
satisfactoria y aprobación competente permiten habilitar el alcance; el hito
exige el acta correspondiente. Estos controles ordinarios no generan nuevas
HH de contingencia; SD8-06 conserva estado parcial hasta acreditar su eficacia.

''')
rev=r/'SD9_v_nueva/revision';rev.mkdir(exist_ok=True)
(rev/'SINCRONIZACION_SD806_2026-11-15.md').write_text('''# Sincronización SD8-06

15 de noviembre de 2026. Rama `LafroX-Subdoc9-LateX-corrigiendo`, actualizada desde remoto `0c57a4bbe6fd02a3fc5ccfe263756e6135a2a56a` antes de editar.

SD4 sincronizado: rama `LafroX-Subdoc4-LateX-corrigiendo`, commit `fabbeec2`. SD8 conserva base `20289fe0` en `Lafrox_Subdocumento_8_Latex_Revision`, con cambios locales autorizados de SD8-04/05/06; el contenido local posterior no se atribuye al commit base.

T-13, 7.5, añade las referencias R-034/CT-15/CT-03 y T-17, 3.1, el expediente por tema. Se conservan los protocolos, campañas, hitos y condiciones vigentes; no cambian cronograma, riesgo, reservas ni los controles ordinarios. CT-03 de SD8 se amplía a identidad conectada/local, sin renumerar stock CT-15.

Pendientes: configuraciones implementadas, resultados de ejecución, trazas, mediciones y actas de aceptación de ERP, stock e identidad. Compilar los formularios y comprobar referencias acredita sólo correspondencia documental. SD8-06 permanece parcial por falta de esa evidencia.
''',encoding='utf-8',newline='\n')
print('T-13/T-17 actualizados, sin modificar protocolos originales ni campañas.')
