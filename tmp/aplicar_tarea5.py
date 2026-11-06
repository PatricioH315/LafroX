from pathlib import Path
from decimal import Decimal as D, ROUND_HALF_UP
from collections import Counter,defaultdict
import re,json,hashlib
r=Path(__file__).resolve().parents[1]
bp=r/'tmp/tarea5-baseline.json'
if bp.exists():raise SystemExit('Tarea 5 ya aplicada: no repetir sobre la versión ampliada.')
paths=['08_plan_riesgos/contenido.tex','08_plan_riesgos/figuras/rbs.tex','LAFROX-Formulario-T-16.tex','LAFROX-Subdocumento8-Anexos.tex']
before={p:(r/p).read_text(encoding='utf-8') for p in paths}
sourcebase=r.parent/'Informe propuesta tecnica/Informe_2_LafroX'
sources=['Subdocumento_4/LAFROX-Subdocumento4.pdf','Subdocumento_7/LAFROX-Subdocumento7.pdf','Subdocumento_7/LAFROX-Formulario-T-14.pdf','Subdocumento_7/LAFROX-Formulario-T-15.pdf','Subdocumento_13/LAFROX-Subdocumento13.pdf']
bp.write_text(json.dumps({'original':before,'source_hashes':{p:hashlib.sha256((sourcebase/p).read_bytes()).hexdigest() for p in sources}},ensure_ascii=False,indent=2),encoding='utf-8')
b,rb,t,a=[before[p] for p in paths]
records=[
dict(n=41,short='Desacuerdo sobre telemetría impide incorporación',cat='Personas y adopción',owner='Jefe de Proyecto',family='JP',p=45,n_ep=1,omp=[24,64,128],idim=4,
event='Dado que existe objeción sindical a cámaras en cabina y al control de jornada por GPS, aunque la propuesta excluye cámaras en cabina y separa la telemetría operacional, entonces puede que no se acuerden o comprendan las finalidades y controles del uso propuesto antes de la ola de reparto, teniendo como consecuencia resistencia a la incorporación y pruebas o aceptaciones pendientes.',
trigger='Acuerdo de finalidades y controles pendiente a D-5 de la ola, u objeción formal al uso operacional propuesto.',
response='Mitigar y escalar. JP coordina con Operaciones, TI y sindicato el acuerdo 5.4.2 antes de la ola: convocar a D-10 y resolver a D-5. Explicar finalidades, acceso y controles; mantener excluidas las cámaras en cabina y no usar GPS para jornada sin acuerdo previo. Ante desacuerdo, escalar por CT, mantener sólo el uso operacional autorizado y registrar la cobertura de la ola pendiente.',
client='Gerente de Operaciones y Jefe de TI; sindicato de conductores como interlocutor del acuerdo, por CT.',
request='Acta sobre finalidades, acceso y controles de la telemetría y uso de terminales; documentar observaciones y el acuerdo exigible para cualquier control de jornada.',
deadline='Convocar a D-10 y resolver a D-5 del inicio de la ola de reparto; acuerdo 5.4.2 antes de habilitar el uso que lo requiere.',
fallback='JP escala por CT a Operaciones; no habilitar cámaras en cabina ni control de jornada sin acuerdo. Mantener el uso operacional autorizado y la cobertura pendiente identificada.',
window='Desde levantamiento de finalidades hasta incorporación de cada ola de reparto, meses 1--20.',
source='Caso, caps. 10 (restricción 10), 16.1 y 19; S3, S-13; S7, acuerdo 5.4.2.',
probwhy='La objeción ya existe, pero el evento incierto es el desacuerdo sobre el uso propuesto. Se adopta 45\% para una ronda extraordinaria de coordinación previa a la ola; no se supone rechazo seguro.',
work='JP y IMP: cada perfil 12/32/64 HH por episodio; un episodio. Sólo negociación y reprogramación extraordinarias, fuera del levantamiento y acuerdo ordinarios.',
impactwhy='Aceptación: el desacuerdo puede impedir incorporar a los usuarios y completar pruebas de la ola; no se presupone habilitación de vigilancia excluida.'),
dict(n=42,short='Rotación nocturna supera inducción disponible',cat='Personas y adopción',owner='Líder de Implantación y Gestión del Cambio',family='IMP',p=55,n_ep=6,omp=[96,192,384],idim=4,
event='Dado que preparación nocturna tiene rotación anual del 38\% y requiere capacitación continua, entonces puede que las incorporaciones superen la capacidad de tutoría y evaluación o lleguen al flujo sin competencias verificadas, teniendo como consecuencia errores de preparación, refuerzo extraordinario y certificación de la ola pendiente.',
trigger='Preparador nuevo asignado sin tutor o evaluación, o aprendizaje que excede dos horas en el programa 7.1.2.',
response='Mitigar. Mantener 7.1.2 en meses 13--56, turno 22:00--06:00, tutor y evaluación antes del trabajo autónomo, con aprendizaje máximo de dos horas. Bodega y Operaciones entregan altas por turno antes de asignarlas. IMP conduce hasta mes 21 y SRE desde 22, familia IMP. Ante sobrecarga, usar personal certificado, reforzar la inducción y escalar por CT; no duplicar las HH ordinarias de 7.1.2.',
client='Jefa de Bodega y Gerente de Operaciones; comunicación de altas y disponibilidad de tutores por turno.',
request='Nómina de altas, turnos y tutores; registro de tiempo de aprendizaje y evaluación individual del preparador, con cobertura certificada mientras completa formación.',
deadline='Meses 13--56; informar cada alta antes de asignarla al turno y completar inducción/evaluación antes del trabajo autónomo. Revisar cobertura en cada relevo.',
fallback='IMP, y SRE desde mes 22, solicita cobertura certificada y refuerzo por CT a Bodega/Operaciones; mantener sin habilitación autónoma al preparador no evaluado.',
window='Meses 13--56; desde primera marcha blanca y durante la operación nocturna.',
source='Caso, caps. 7.2, 10 (restricción 11) y 19; S7, pp. 21--22 y 32; T-14, 7.1.2; T-15, meses 13--56.',
probwhy='El 38\% es rotación anual, no p0. Se propone 55\% de al menos un desborde de inducción durante 44 meses y, condicionado a ello, seis cohortes con atención extraordinaria; son hipótesis de exposición recurrente.',
work='IMP y CAL: cada perfil 8/16/32 HH por cohorte; seis cohortes. Excluir las 2.816 HH ordinarias de 7.1.2 y el trabajo autónomo del preparador.',
impactwhy='Aceptación y calidad: personal no preparado amenaza la certificación y el flujo nocturno; el esfuerzo condicional de 208 HH también alcanza nivel 4.'),
dict(n=43,short='Interfaces ERP/WMS no verificables a tiempo',cat='Integración y legado',owner='Arquitecto de Solución',family='ARQ',p=50,n_ep=1,omp=[48,128,280],idim=4,
event='Dado que el CLIENTE no tiene documentación técnica de las interfaces del ERP ni del WMS de 2013, que se reemplaza progresivamente, entonces puede que el levantamiento no permita verificar a tiempo contratos de intercambio y extracción del legado, teniendo como consecuencia reproceso de adaptadores o cargas y bloqueo de pruebas de integración o migración.',
trigger='No hay contrato de interfaz o extracción verificado al cierre del mes 1, o el ensayo temprano contradice formato, acceso o comportamiento declarados.',
response='Mitigar y escalar. ARQ solicita a TI acceso, diccionario y condiciones de extracción en mes 1 (1.2.3, 3.3.2 y V-16); DAT verifica la migración del WMS. Probar temprano sin modificar el ERP. Si falta una interfaz, evaluar intercambio de archivos controlado, sujeto a demostrar los requisitos; elevar por CT el bloqueo y sus impactos. La alternativa no acredita por sí sola latencia, integridad ni emisión tributaria.',
client='Jefe de TI; custodios del ERP y WMS y proveedor del legado cuando su acceso sea necesario.',
request='Accesos autorizados, formatos, diccionario y contratos de interfaz/extracción; resultado de ensayo temprano y restricciones del proveedor del ERP/WMS.',
deadline='Solicitar en los primeros cinco días hábiles del mes 1 y verificar contrato inicial al cierre del mes 1; probar cada interfaz antes de su integración y cada extracción antes de validar la carga.',
fallback='ARQ escala por CT a TI, prepara alternativa de archivo controlado y mide sus límites; mantener bloqueada la aceptación dependiente sin modificar el ERP ni omitir datos.',
window='Levantamiento del mes 1 hasta integración y migraciones de ambas etapas, antes de H5/H10.',
source='Caso, cap. 5 y cap. 19; S3, S-18, S-14 y V-16; S7, 1.2.3 y 3.3.2.',
probwhy='Se adopta 50\% ante ausencia documental confirmada y capacidad de acceso aún por verificar, para un bloqueo conjunto de descubrimiento; no se confunde documentación ausente con interfaz inexistente.',
work='ARQ y DAT: cada perfil 24/64/140 HH; un episodio de descubrimiento y reproceso extraordinarios. Excluir levantamiento y adaptadores ordinarios.',
impactwhy='Aceptación y plazo: sin intercambio o extracción verificados se bloquean integración y migración exigidas, aunque los datos históricos existan.'),
dict(n=44,short='Peak y congelamiento impiden cierre de fase',cat='Contrato y licitación',owner='Jefe de Proyecto',family='JP',p=45,n_ep=1,omp=[24,64,160],idim=4,
event='Dado que el peak de septiembre casi duplica entregas durante tres semanas y coincide con el cierre de la marcha blanca E2 en el calendario supuesto de S7, entonces puede que un incidente, una validación pendiente o la falta de disponibilidad de usuarios no pueda resolverse dentro de las ventanas autorizadas, teniendo como consecuencia incumplimiento de condiciones de cierre y necesidad de recuperación de la programación.',
trigger='Incidente alto/crítico, evidencia o certificación pendiente en las semanas finales del peak, sin ventana de intervención o validación disponible.',
response='Mitigar y escalar. JP acuerda con Operaciones y CT disponibilidad y continuidad antes de septiembre; cerrar habilitaciones en agosto según S7. En meses 19--20 mantener evidencia diaria de las seis condiciones de marcha blanca. Un defecto durante 1--25 de septiembre no autoriza despliegue: activar continuidad aprobada y R-022 si requiere autorización. Si persiste una condición incumplida, no declarar cierre; elevar plan de recuperación sin mover hitos por cuenta propia.',
client='Gerente de Operaciones y Contraparte Técnica; gerencias usuarias para disponibilidad de validación.',
request='Agenda de usuarios, decisiones y continuidad autorizada para el peak; estado diario de las condiciones de cierre y resolución formal de impactos en hitos.',
deadline='Preparar antes del mes 19 y completar habilitaciones en agosto bajo el supuesto de inicio de S7. Verificación diaria en meses 19--20 y antes del cierre previsto del mes 20.',
fallback='JP escala inmediatamente por CT al Comité Ejecutivo; mantener continuidad autorizada y no cerrar con condiciones incumplidas ni desplegar en congelamiento sin autorización.',
window='Cierre de E2 en meses 19--20; septiembre del calendario supuesto de inicio de S7, sujeto a confirmar inicio contractual.',
source='Caso, caps. 10 (restricción 8), 17.5 y 19; S7, 7.3.1 y 7.3.5, pp. 37 y 58; T-18.',
probwhy='El peak y el congelamiento son condiciones conocidas. El 45\% representa un bloqueo del cierre en esa coincidencia, no la probabilidad de que septiembre ocurra.',
work='JP y IMP: cada perfil 12/32/80 HH; un episodio. Sólo coordinación, validación y recuperación de calendario; la corrección técnica de una saturación pertenece a R-047.',
impactwhy='Contrato y aceptación: una condición incumplida impide cerrar marcha blanca y amenaza su hito; no se compensa con otras condiciones cumplidas.'),
dict(n=45,short='Cambio de soporte exige adecuación extraordinaria',cat='Solución y tecnología',owner='Arquitecto de Solución',family='ARQ',p=40,n_ep=2,omp=[32,96,224],idim=4,
event='Dado que la propuesta opera durante 56 meses con componentes como Laravel 13, PHP 8.5 y Proxmox, entonces puede que cambien su soporte o compatibilidad de forma que las actualizaciones ordinarias no basten, teniendo como consecuencia una adecuación extraordinaria y revalidación para mantener seguridad y continuidad.',
trigger='Aviso de soporte/compatibilidad que deja una versión necesaria fuera de la política aprobada o hace fallar la regresión de la actualización prevista.',
response='Mitigar. ARQ mantiene inventario de versiones y revisa soporte y compatibilidad trimestralmente desde mes 1, con DES y SRE. Preparar y probar adecuación antes del límite verificado de soporte, dentro de ventanas autorizadas. Si el cambio excede la actualización ordinaria 8.2.5, registrar el esfuerzo extraordinario y elevar impactos por CT; usar reversión ensayada y soporte permitido, sin sostener una versión insegura por conveniencia.',
client='Jefe de TI y Contraparte Técnica; Operaciones para ventanas de actualización y aceptación del servicio.',
request='Calendario de ventanas, política de versiones y conformidad con las pruebas de adecuación; aprobación de cambios que afecten compromisos.',
deadline='Inventario en mes 1, revisión trimestral hasta mes 56; acordar intervención antes del límite de soporte comprobado y antes de activar la versión.',
fallback='ARQ escala por CT el impacto; ensayar reversión y reprogramación autorizada de la adecuación, preservando atención de vulnerabilidades y compromisos de servicio.',
window='Meses 1--56; ciclos de soporte y compatibilidad efectivamente publicados, sin suponer fechas de fin de soporte.',
source='Revisión del Informe 2, S8, análisis 8.2; S4, plataforma declarada; S7, 8.2.5.',
probwhy='Se propone 40\% de al menos una adecuación excepcional en 56 meses y dos episodios condicionados. No se afirma que una versión haya quedado sin soporte ni se inventa fecha de término.',
work='ARQ y DES: cada perfil 8/24/56 HH por episodio; dos episodios. Excluir las actualizaciones anuales ordinarias 8.2.5 y mantenimiento ya incluido.',
impactwhy='Seguridad y servicio: una incompatibilidad que excede mantenimiento ordinario puede impedir conservar la versión segura y el servicio aceptado.'),
dict(n=46,short='Dependencia de proveedor limita salida o sustitución',cat='Solución y tecnología',owner='Arquitecto de Solución',family='ARQ',p=25,n_ep=1,omp=[40,120,280],idim=4,
event='Dado que la arquitectura utiliza servicios gestionados de AWS y capacidades específicas de su plataforma, entonces puede que un cambio de condiciones o una necesidad de salida encuentre restricciones de exportación, credenciales o equivalencia funcional no resueltas, teniendo como consecuencia trabajo extraordinario y demora para sustituir el servicio o ejecutar reversibilidad.',
trigger='Ensayo de exportación/restauración incompleto, acceso o clave no disponible para el CLIENTE, o cambio de condiciones que impide cumplir el plan de salida.',
response='Mitigar. ARQ verifica con TI propiedad de cuentas, acceso a datos, claves, exportaciones e infraestructura como código en la recepción inicial y en cada actualización anual del plan 8.1.4. Probar una restauración utilizable, no sólo descargar archivos. Ante restricción, documentar brecha, mantener continuidad autorizada y escalar por CT alternativas y decisión contractual; no declarar reversibilidad completa ni cambiar de proveedor sin prueba y aprobación.',
client='Jefe de TI y Contraparte Técnica; autoridad contractual del CLIENTE para condiciones de salida y acceso.',
request='Accesos y titularidad de cuentas/claves, evidencia de exportación y restauración y decisión sobre restricciones contractuales de sustitución.',
deadline='Verificar en recepción inicial y actualización anual de 8.1.4; resolver cada restricción antes del ensayo o transición de salida que dependa de ella.',
fallback='ARQ eleva por CT la restricción al Comité Ejecutivo y prepara salida gradual comprobable; conservar acceso y continuidad bajo condiciones autorizadas sin presumir equivalencia entre proveedores.',
window='Meses 1--56 y preparación de la salida contractual; no se asume que la salida extraordinaria ocurrirá.',
source='Revisión del Informe 2, S8, análisis 8.2; S4, servicios gestionados; S7, 8.1.4 y fase 9.',
probwhy='Se propone 25\% para una restricción extraordinaria de salida o sustitución en el contrato; el uso de AWS por sí solo no demuestra bloqueo.',
work='ARQ y SRE: cada perfil 20/60/140 HH; un episodio. Sólo resolución excepcional de restricciones; excluir actualización anual del plan y salida ordinaria contratada.',
impactwhy='Contrato y continuidad: una restricción no resuelta impide una transición comprobable del servicio o la entrega utilizable de datos.'),
dict(n=47,short='Capacidad efectiva insuficiente bajo carga peak',cat='Solución y tecnología',owner='Líder de Operación / SRE',family='SRE',p=40,n_ep=2,omp=[48,144,336],idim=4,
event='Dado que el peak alcanza unas 2.600 entregas diarias y concentra despacho y reconexión, entonces puede que una dependencia o perfil de proceso no sostenga la carga efectiva aun con el escalado previsto, teniendo como consecuencia colas crecientes, incumplimiento de respuesta o indisponibilidad de operaciones críticas.',
trigger='Ensayo de peak o monitoreo que excede los percentiles/plazos aprobados o muestra colas que no se concilian en su ventana.',
response='Mitigar. SRE, ARQ y DES ensayan por ventana despacho, API, sincronización e ingesta, con carga y umbrales de S4, antes de H5/H10 y del peak; el escalado no demuestra capacidad del ERP. Corregir y repetir ensayo antes de aceptar. En operación, priorizar trabajo crítico y aplicar continuidad autorizada, preservando bloqueos y conciliación. Escalar por CT el impacto de servicio; R-044 registra sólo el efecto adicional en el cierre de fase.',
client='Jefe de TI y Gerente de Operaciones; Finanzas para la dependencia de emisión del ERP cuando corresponda.',
request='Carga representativa y ventanas de ensayo, acceso a dependencias del ERP y validación de resultados de servicio por proceso.',
deadline='Acordar datos/ventana a D-10 y confirmar a D-5 de cada ensayo; demostrar capacidad antes de H5/H10 y antes del peak que afecte a la operación.',
fallback='SRE escala por CT a TI/Operaciones, prioriza funciones críticas y repite pruebas tras ajuste. No aceptar colas fuera de plazo ni desactivar bloqueos para aumentar rendimiento.',
window='Ensayos previos a H5/H10 y peaks de operación hasta mes 56; dos episodios extraordinarios condicionados.',
source='Caso, caps. 14, 17.4 y 19; S4, 4.2.6, pp. 153--167; S7, 7.3.5.',
probwhy='Se propone 40\% por incertidumbre de capacidad efectiva y dependencias bajo carga, no por frecuencia medida. Las 2.600 entregas fijan el escenario del ensayo, no p0.',
work='SRE y DES: cada perfil 12/36/84 HH por episodio; dos episodios. Sólo diagnóstico y ajuste excepcionales; excluir dimensionamiento y pruebas obligatorias ordinarios y la coordinación de R-044.',
impactwhy='Servicio: saturación de colas o emisión puede comprometer respuesta y ventana crítica; el escalado de una capa no acredita las dependencias restantes.'),
dict(n=48,short='Indisponibilidad de identidad afecta relevo',cat='Solución y tecnología',owner='Encargado de Seguridad de la Información',family='SEG',p=20,n_ep=2,omp=[16,48,128],idim=4,
event='Dado que altas, bajas y relevos dependen de identidad central y permisos locales vigentes, entonces puede que la indisponibilidad del IdP o la falta de un manifiesto válido impida habilitar al personal requerido o propagar una revocación, teniendo como consecuencia afectación de continuidad y seguridad del relevo.',
trigger='Falla del relevo durante corte, manifiesto no vigente o revocación pendiente que no puede propagarse dentro del procedimiento.',
response='Mitigar. SEG y SRE verifican con ARQ AL-OFF-01 antes de H5/H10: corte de 24 h y relevos a 8/16 h, expiración, denegación y reconciliación. TI y Operaciones confirman personal/turnos antes de emitir permisos. Manifiesto de 26 h, caché de 24 h y credenciales de 8/14 h no son intercambiables. Ante fallo, denegar acceso no válido, conservar auditoría y usar personal previamente autorizado conforme al procedimiento.',
client='Jefe de TI y Gerente de Operaciones; supervisores de turno para nómina, bajas y permisos.',
request='Nómina y permisos previos al relevo, titulares y suplentes y evidencia de bajas; conformidad del ensayo de corte y revocación pendiente.',
deadline='Confirmar turnos y permisos antes de emitir el manifiesto y antes de cada relevo; ensayo AL-OFF-01 antes de H5/H10 y en pruebas de continuidad.',
fallback='SEG/SRE notifican a TI/Operaciones por CT; denegar permisos no válidos, preservar auditoría y aplicar relevo con personal autorizado sin emitir identidades locales nuevas.',
window='Desde primera prueba de autonomía hasta mes 56; dos incidentes condicionados en relevos durante indisponibilidad.',
source='Brecha B-S4-01; S4, Tabla 4, p. 78; pp. 26--27, 46--47 y 81.',
probwhy='Se propone 20\% de incidente de continuidad de identidad en esa ventana; no es probabilidad de phishing ni eficacia residual demostrada del manifiesto.',
work='SEG y SRE: cada perfil 4/12/32 HH por episodio; dos episodios. Excluir implementación, enrolamiento y prueba ordinaria del control de identidad.',
impactwhy='Continuidad y seguridad: el relevo puede quedar impedido o la revocación pendiente, amenazando servicio y autorización sin presuponer pérdida irreversible.'),
dict(n=49,short='ERP indisponible impide nueva guía válida',cat='Integración y legado',owner='Arquitecto de Solución',family='ARQ',p=30,n_ep=2,omp=[32,96,240],idim=4,
event='Dado que el ERP del CLIENTE es el único emisor tributario y reside en Talca, entonces puede que su indisponibilidad, incluida la pérdida de la sala, impida emitir la nueva guía requerida por un cambio de carga o una anulación, teniendo como consecuencia bloqueo de la salida hasta restituir el ERP.',
trigger='Carga sin guía vigente que requiere nueva emisión mientras el ERP está indisponible; pérdida de sala con ERP aún no restituido.',
response='Mitigar y escalar. ARQ/SRE acuerdan con TI y Finanzas restitución del ERP y ensayan AL-DTE-01/AL-DR-01 antes de H5/H10, incluida pérdida de sala. Mantener sólo salidas con guía preemitida aún válida y bloquear las que requieren nueva guía. Recuperar WMS en nube no restaura el ERP ni exceptúa el RTO requerido; registrar y escalar por CT cualquier incumplimiento, sin segundo emisor ni aprobación tributaria por silencio.',
client='Jefe de TI y Gerente de Finanzas; Operaciones coordina cargas y salidas afectadas.',
request='Procedimiento de restitución del ERP, responsables y evidencias de emisión/anulación, con resultado de ensayo de pérdida de sala y cambio de carga.',
deadline='Acordar procedimiento antes del ensayo AL-DTE-01/AL-DR-01 de H5/H10. En incidente, comunicar de inmediato a TI/Finanzas y decidir cada salida antes de despachar.',
fallback='ARQ/SRE escalan por CT a TI/Finanzas; bloquear salida sin guía válida y conservar la carga original sólo si conserva guía vigente. Medir restitución completa frente al RTO exigido.',
window='Desde pruebas de emisión y primer despacho hasta mes 56; dos episodios excepcionales condicionados.',
source='Brecha B-S4-02; Caso, cap. 10, restricciones 1 y 4; S4, pp. 78, 84 y 183.',
probwhy='Se propone 30\% de al menos un bloqueo de nueva emisión por ERP indisponible en el horizonte; no se deriva de la respuesta del SII ni se duplica pérdida de sala como otro evento.',
work='ARQ y SRE: cada perfil 8/24/60 HH por episodio; dos episodios. Sólo coordinación, recuperación y validación extraordinarias de la integración; no incluye reconstruir el ERP del CLIENTE.',
impactwhy='Servicio y contrato: impedir una guía nueva bloquea despachos y amenaza la ventana crítica, aun cuando el WMS esté recuperado.'),
dict(n=50,short='Consolidación central no confirma reservas',cat='Solución y tecnología',owner='Líder de Datos',family='DAT',p=25,n_ep=2,omp=[24,72,192],idim=4,
event='Dado que la reserva global depende del estado central y de una única autoridad de escritura, entonces puede que falle la consolidación o no pueda restituirse una autoridad consistente, teniendo como consecuencia stock central desactualizado y pedidos sin confirmación o con conflictos de reserva.',
trigger='Reserva central fechada o inconsistente, eventos de sitios no conciliados o promoción sin exclusión verificable del escritor anterior.',
response='Mitigar. DAT y ARQ, con SRE, verifican AL-STOCK-01/AL-DR-01 antes de H5/H10: conciliación por sitio y UUID y exclusión del escritor previo antes de promover otro. Mantener operación local y capturas pendientes; no confirmar stock con copia vencida. Operaciones y Comercial validan excepciones. Ante conflicto, aislar el conjunto y escalar por CT hasta conciliar, sin habilitar dos escritores.',
client='Gerentes de Operaciones y Comercial; Jefe de TI para la recuperación de accesos y servicios.',
request='Criterios y decisiones sobre reservas en conflicto, evidencias de conciliación por sitio y conformidad de la recuperación de autoridad de escritura.',
deadline='Acordar criterios antes de AL-STOCK-01/AL-DR-01 de H5/H10; resolver cada conflicto antes de confirmar la reserva o cerrar la recuperación.',
fallback='DAT/SRE escalan por CT a Operaciones/Comercial; conservar capturas pendientes, aislar conflictos y no confirmar reservas con copia vencida ni dos escritores.',
window='Desde integración de sitios hasta mes 56; dos incidentes extraordinarios condicionados.',
source='Brecha B-S4-03; S4, Tabla 4, p. 78; 4.1.15--4.1.16 y 4.3.2.5--4.3.2.6.',
probwhy='Se propone 25\% de fallo de consolidación/recuperación de autoridad; no se toma como frecuencia observada ni como efecto inevitable de un corte WAN.',
work='DAT y SRE: cada perfil 6/18/48 HH por episodio; dos episodios. Excluir construcción de reconciliación y diferencias de inventario previas al corte de R-004.',
impactwhy='Aceptación y servicio: sin estado central consistente se impide confirmar reservas y cerrar la recuperación de operaciones de varios sitios.'),
dict(n=51,short='Conductor externo rechaza uso de la solución',cat='Personas y adopción',owner='Líder de Implantación y Gestión del Cambio',family='IMP',p=40,n_ep=2,omp=[24,64,160],idim=4,
event='Dado que los conductores de terceros no son trabajadores de Puelche y requieren incorporación acordada con su transportista, entonces puede que un conductor autorizado y convocado rechace utilizar el terminal o el flujo digital aun existiendo acuerdo de la empresa, teniendo como consecuencia entregas sin evidencia digital completa y cobertura de adopción de la ola pendiente.',
trigger='Conductor asignado y habilitado rechaza el flujo digital o entrega sin la evidencia requerida, sin que la causa sea firma pendiente o reemplazo sin aviso.',
response='Mitigar y escalar. IMP coordina con Operaciones, transportista y conductor demostración y acompañamiento antes de su salida, dentro de 7.1.3. Confirmar disponibilidad a D-5 de la ola y aceptación práctica en andén. Ante rechazo, solicitar a la empresa conductor certificado y dispuesto, mantener acompañamiento y elevar por CT la cobertura pendiente; no atribuir a LafroX facultades laborales ni declarar completa la evidencia faltante.',
client='Gerente de Operaciones y representante de cada empresa transportista; conductor como participante de la validación práctica.',
request='Disponibilidad de conductores y demostración de uso en andén, evidencia de inducción y compromiso operativo del transportista ante rechazo individual.',
deadline='Confirmar participantes a D-5 de la ola de reparto y demostrar uso antes de la primera salida del conductor; actuar en andén ante cada rechazo.',
fallback='IMP escala por CT a Operaciones y al transportista; solicitar conductor certificado y dispuesto y acompañar. Registrar entregas/evidencias pendientes sin dar cobertura por cumplida.',
window='Incorporación de empresas y conductores, y reemplazos durante operación hasta mes 56.',
source='Caso, caps. 10 (restricción 6), 15, RT-22.04 y 19; S7, 5.4.1 y 7.1.3.',
probwhy='Se propone 40\% de al menos un rechazo individual en incorporación y operación; dos episodios condicionados. El hecho de trabajar para un tercero no demuestra rechazo.',
work='IMP y CAL: cada perfil 6/16/40 HH por episodio; dos episodios. Sólo atención extraordinaria del rechazo; excluir inducción ordinaria de 7.1.3, firma de R-013 y habilitación de R-031.',
impactwhy='Aceptación y adopción: un conductor que no usa el flujo deja evidencia y cobertura pendientes, aun con firma de empresa y certificación previa.'),
]
def fmt(v):return f'{D(v):.2f}'.replace('.',',')
def rnd(v):return D(v).quantize(D('.01'),rounding=ROUND_HALF_UP)
def pl(p):return 1 if p<=10 else 2 if p<=30 else 3 if p<=50 else 4 if p<=70 else 5
def ih(h):return 1 if h<=24 else 2 if h<=80 else 3 if h<=160 else 4 if h<=320 else 5
def zone(e):return 'Baja' if e<D('.08') else 'Media' if e<D('.20') else 'Alta' if e<D('.40') else 'Crítica'
pf=[D('.10'),D('.30'),D('.50'),D('.70'),D('.90')];im=[D('.05'),D('.10'),D('.20'),D('.40'),D('.80')]
for d in records:
 d['rid']=f"R-{d['n']:03}";o,m,p=map(D,d['omp']);d['pert']=(o+4*m+p)/6;d['ve']=D(d['p'])/100*d['pert'];d['ih']=ih(d['pert']);d['impact']=max(d['idim'],d['ih']);d['pl']=pl(d['p']);d['qp']=pf[d['pl']-1];d['qi']=im[d['impact']-1];d['e']=d['qp']*d['qi'];d['zone']=zone(d['e'])
new={d['rid']:d for d in records}
oldform={l.split(' & ')[0]:l.split(' & ') for l in t.splitlines() if re.match(r'R-\d{3} &',l)}
oldquant={l.split(' & ')[0]:l.split(' & ') for l in a.splitlines() if re.match(r'R-\d{3} &',l) and len(l.split(' & '))==8}
# Existing IDs retain their events except the two omissions explicitly noted as partial.
c=oldform['R-016'][:]
c[1]='Dado que el planificador del CLIENTE se jubila dentro del horizonte contractual y su ausencia reduce el cumplimiento de entrega entre 6 y 9 puntos porcentuales según el caso, entonces puede que llegue su retiro o indisponibilidad antes de transferir y probar las reglas y excepciones de rutas, teniendo como consecuencia pérdida de conocimiento operativo, reconstrucción extraordinaria y riesgo de no acreditar el resultado R18-16.'
c[4]='4 / 0,40';c[5]='0,12 (Media)';oldform['R-016']=c
c=oldform['R-019'][:]
c[1]='Dado que Concepción parte con fibra de un solo proveedor sin respaldo y los demás sitios también dependen de enlaces externos, entonces puede que se interrumpa el camino disponible antes de verificar los respaldos propuestos o falle el último camino utilizable durante operación, teniendo como consecuencia aislamiento de servicios centrales, acumulación de sincronización y gestión de restitución y conciliación.'
c[3]='2 / 0,30';c[5]='0,12 (Media)';c[6]=c[6].replace('Mantener y ensayar los enlaces ya ofertados:','Mitigar. Verificar respaldos antes de aceptar la ola de Concepción; no considerar disponible un enlace sólo por estar ofertado. Mantener y ensayar los enlaces ya ofertados:');oldform['R-019']=c
tlines=[]
for l in t.splitlines():
 if re.match(r'R-\d{3} &',l):l=' & '.join(oldform[l.split(' & ')[0]])
 tlines.append(l)
t='\n'.join(tlines)+'\n'
newrows=''
for d in records:newrows+=f"{d['rid']} & {d['event']} & {d['cat']} & {d['pl']} / {fmt(d['qp'])} & {d['impact']} / {fmt(d['qi'])} & {fmt(d['e'])} ({d['zone']}) & {d['response']} & {d['owner']} \\\\\n"
start=t.index('\\begin{tablalafrox}{Registro cualitativo');end=t.index('\\end{tablalafrox}',start);t=t[:end]+newrows+t[end:]
t=t.replace('El Anexo 8.D registra la trazabilidad con S4/S7/S13 y cuatro brechas aún no incorporadas ni valoradas en estos 40 riesgos.', 'El Anexo 8.D vincula las cuatro brechas de arquitectura y rotación con R-048, R-049, R-050 y R-042, y verifica las demás omisiones del caso. El Anexo 8.B explicita las hipótesis de probabilidad, episodios y HH de la ampliación.')

# Responses and client coordination, preserving all previous entries except the named adjustments.
alines=[]
for l in a.splitlines():
 if l.startswith('R-019 &') and len(c:=l.split(' & '))==4:c[2]=oldform['R-019'][6];l=' & '.join(c)
 if l.startswith('R-016 &') and len(c:=l.split(' & '))==5:
  c[2]='4 / 4';c[3]='0,40';c[4]='Aceptación: el conocimiento debe quedar transferido y probado antes de la jubilación para acreditar R18-16; el antecedente de caída de 6 a 9 puntos de cumplimiento amenaza continuidad y aceptación. \\\\' ;l=' & '.join(c)
 if l.startswith('R-019 &') and len(c:=l.split(' & '))==8:c[1]='25\\%';c[7]='15,00\\\\';l=' & '.join(c)
 alines.append(l)
a='\n'.join(alines)
start=a.index('\\begin{tablalafrox}{Matriz de respuestas');end=a.index('\\end{tablalafrox}',start)
rows=''.join(f"{d['rid']} & {d['trigger']} & {d['response']} Evidencia y coordinación: Tabla 8.A.2. & {d['owner']} \\\\\n" for d in records)
a=a[:end]+rows+a[end:]
start=a.index('\\begin{tablalafrox}{Contrapartes, solicitudes');end=a.index('\\end{tablalafrox}',start)
rows=''.join(f"{d['rid']} / {d['family']} & {d['client']} & {d['request']} & {d['deadline']} & {d['fallback']} \\\\\n" for d in records)
a=a[:end]+rows+a[end:]
a=a.replace('Esta matriz desarrolla los 20 riesgos R-001--R-007, R-011--R-018, R-021--R-022, R-031--R-032 y R-039.', 'Esta matriz desarrolla la coordinación del CLIENTE en R-001--R-007, R-011--R-018, R-021--R-022, R-031--R-032, R-039 y R-041--R-051. La contraparte coordina insumos o decisiones; su presencia no transfiere al CLIENTE los controles de diseño, capacidad, seguridad o mantenimiento que corresponden a LafroX.')

# Quantitative rows and aggregate totals are regenerated from the same declared inputs.
q={}
for rid,c in oldquant.items():
 o,m,p=[D(x.replace(',','.')) for x in c[3:6]];h=(o+4*m+p)/6;p0=25 if rid=='R-019' else int(c[1].split('\\')[0]);q[rid]={'p':p0,'h':h,'ve':D(p0)/100*h}
for d in records:q[d['rid']]={'p':d['p'],'h':d['pert'],'ve':d['ve']}
total=sum((rnd(d['ve']) for d in q.values()),D(0))
topq=sorted(q,key=lambda k:(-q[k]['ve'],k))[:10];topsum=sum((rnd(q[k]['ve']) for k in topq),D(0));pct=topsum/total*100
start=a.index('\\begin{tablalafrox}{Estimación acumulada');end=a.index('\\multicolumn{6}{r}{Total VE}',start)
add=''.join(f"{d['rid']} & {d['p']}\\% & {d['n_ep']} & {' & '.join(fmt(x) for x in d['omp'])} & {fmt(d['pert'])} & {fmt(d['ve'])}\\\\\n" for d in records)
a=a[:end]+add+a[end:]
a=re.sub(r'(\\multicolumn\{6\}\{r\}\{Total VE\} & & )[^\n]+',lambda m:m[1]+fmt(total)+'\\\\',a,count=1)

ledger=r'''
\subsection*{Hipótesis de la ampliación y control de doble conteo}
\addcontentsline{toc}{subsection}{Hipótesis de la ampliación y control de doble conteo}

Las probabilidades y HH de R-041--R-051 son juicios explícitos de planificación basados en las condiciones citadas, no frecuencias observadas ni compromisos aceptados. $p_0$ significa al menos un episodio del evento durante la ventana indicada; $n$ estima episodios condicionados a que el evento ocurra. Los escenarios O/M/P de 8.B.1 son acumulados: se suman los dos perfiles por episodio y se multiplican por $n$ una sola vez, antes de aplicar PERT y $p_0$. El 38\% de rotación anual y las 2.600 entregas del peak no se usan como probabilidades.

Las HH representan trabajo extraordinario de LafroX por encima del alcance ordinario; no valorizan pérdidas de mercadería, reconstrucción del ERP del CLIENTE, tareas ordinarias de capacitación ni aumentos de demanda ya incluidos en el dimensionamiento. R-044 recoge sólo coordinación y recuperación de programación; la remediación de capacidad pertenece a R-047. Un incidente recibe un ID causal principal y sus HH se imputan una sola vez; los efectos en otros riesgos quedan vinculados sin repetir el esfuerzo. R-019 no duplica el mismo corte WAN como caída de ERP, SII, POS o stock central; R-049 y R-050 cuantifican fallas propias de sus dependencias. R-045--R-048 y R-050 conservan la responsabilidad técnica de LafroX: sus controles de diseño y mantenimiento ordinario se verifican en arquitectura/calidad y no se presupuestan otra vez como contingencia.

R-019 se revisa de $p_0=5\%$ a $25\%$ por incluir la exposición inicial de Concepción con un enlace sin respaldo verificado y la falla del último camino utilizable hasta mes 56. Es una hipótesis, no una frecuencia inferida del caso ni de los cortes de Talca. Se conservan sus ocho episodios condicionados y escenarios acumulados 24/48/144 HH; PERT sigue en 60 HH y VE pasa de 3 a 15 HH. R-016 conserva $p_0=20\%$ y sus HH; su impacto pasa a 4 por el resultado R18-16 y la jubilación dentro del horizonte, sin convertir el retiro conocido en un suceso probabilístico.

\begingroup
\renewcommand{\thetable}{8.B.2}
\begin{landscape}
\setlength{\textwidth}{\linewidth}
\begin{tablalafrox}{Hipótesis de ocurrencia, ventana y esfuerzo extraordinario de los nuevos riesgos. Fuente: condiciones citadas y estimación de planificación de LafroX.}{tab:sd8-ampliacion-hipotesis}{G{0.07} F{0.19} Y F{0.28} F{0.18}}{\cab{ID / $p_0$ / $n$} & \cab{Ventana de exposición} & \cab{Fundamento del juicio de probabilidad} & \cab{Base O/M/P y exclusiones} & \cab{Fuente de la condición}}
'''
for d in records:ledger+=f"{d['rid']} / {d['p']}\\% / {d['n_ep']} & {d['window']} & {d['probwhy']} & {d['work']} & {d['source']} \\\\\n"
ledger+='\\end{tablalafrox}\n\\end{landscape}\n\\endgroup\n\n'
anchor='\\clearpage\n\\section{Anexo 8.C:';at=a.index(anchor);a=a[:at]+ledger+a[at:]
start=a.index('\\begin{tablalafrox}{Fundamento del impacto inicial');end=a.index('\\end{tablalafrox}',start)
add=''.join(f"{d['rid']} & {fmt(d['pert'])} / {d['ih']} & {d['idim']} / {d['impact']} & {fmt(d['qi'])} & {d['impactwhy']} \\\\\n" for d in records)
a=a[:end]+add+a[end:]
a=a.replace('no se modifica ninguna estimación de ese anexo.', 'la base y las revisiones de estimación se explicitan en 8.B.2.')

# Resolve gap status without erasing the audit IDs.
gapmap={'B-S4-01':'R-048','B-S4-02':'R-049','B-S4-03':'R-050','B-S7-01':'R-042'}
st=a.index('Las cuatro brechas B-S4-01');en=a.index('\n\n',st)
a=a[:st]+r'Las cuatro brechas se incorporan como B-S4-01 $\rightarrow$ R-048, B-S4-02 $\rightarrow$ R-049, B-S4-03 $\rightarrow$ R-050 y B-S7-01 $\rightarrow$ R-042. Sus eventos, respuestas y valoraciones se desarrollan en T-16 y Anexos 8.A--8.C; los códigos B se conservan sólo como trazabilidad del hallazgo. La Tabla 8.D.3 verifica además las omisiones del caso y las materias técnicas señaladas en la revisión. Las condiciones de cobertura RF y la redundancia por componente siguen sujetas a evidencia de arquitectura/calidad: no se crea un riesgo por componente ni se presume eficacia comprobada de los controles.'+a[en:]
st=a.index('Cada código B identifica');en=a.index('\n\n',st)
a=a[:st]+r'Cada código B conserva el hallazgo y su ID de riesgo incorporado. La valoración está en 8.B--8.C y las respuestas en 8.A y T-16; esta tabla conserva la regla de no duplicación. La tasa de rotación y los tiempos de autonomía no son probabilidades. Las respuestas citan controles previstos y condiciones de verificación, sin atribuirles eficacia residual demostrada.'+a[en:]
lines=[]
for l in a.splitlines():
 if re.match(r'TR-0[345] &|TR-13 &',l):
  c=l.split(' & ');rid={'TR-03':'R-048','TR-04':'R-049','TR-05':'R-050','TR-13':'R-042'}[c[0]]
  c[2]+=' Incorporado: '+rid+'.';c[3]=c[3].replace('No hay riesgo específico','No había riesgo específico').replace('Falta el evento','Faltaba el evento').replace('Falta un evento','Faltaba un evento')
  c[4]=c[4].replace('Brecha registrada; incorporación y valoración pendientes.',f'Incorporado como {rid} en T-16 y 8.A--8.C.').replace('Brecha registrada una sola vez; incorporación y valoración pendientes.',f'Incorporado una sola vez como {rid} en T-16 y 8.A--8.C.');l=' & '.join(c)
 if re.match(r'B-S[47]-\d{2} &',l):
  c=l.split(' & ');c[0]+=' / '+gapmap[c[0]];l=' & '.join(c)
 lines.append(l)
a='\n'.join(lines)
a=a.replace('Brechas registradas para incorporación y valoración','Brechas incorporadas y regla de no duplicación').replace('Brechas de cobertura detectadas, sin valoración ni incorporación anticipada al T-16.','Brechas de cobertura incorporadas y vinculadas al T-16.').replace('\\cab{Brecha} & \\cab{Condición}', '\\cab{Brecha / riesgo} & \\cab{Condición}')

coverage=[
('Conocimiento de rutas; Caso, caps. 7.2, 18 y 19.','R-016','Retiro dentro del horizonte y antecedente de caída de 6 a 9 puntos; transferencia 1--3 y prueba sin el planificador en 13--15. IMP, con Operaciones/planificador.','Se revalora impacto a 4 y zona Media; p0 y HH conservados. No agregar otro riesgo por jubilación.'),
('Objeción sindical; Caso, cap. 10, restricción 10, y cap. 19.','R-041','Acuerdo de finalidades y controles antes de la ola; JP, Operaciones, TI y sindicato. Sin cámaras en cabina ni control de jornada no acordado.','Separado de R-015: desacuerdo institucional, no mera adopción individual.'),
('Rechazo de conductores de terceros; Caso, cap. 19.','R-051','Validación práctica, acompañamiento y respuesta del transportista antes de salida; IMP y Operaciones.','R-013 es firma de empresa; R-031 es sustituto no habilitado. R-051 es rechazo individual aun con acuerdo/habilitación.'),
('Rotación de preparación nocturna; Caso, caps. 7.2, 10 y 19; S7, 7.1.2.','R-042','Programa continuo 13--56, tutor y evaluación antes del trabajo autónomo; IMP hasta 21/SRE desde 22.','38\% es tasa anual, no p0. Una sola entrada enlaza B-S7-01 y excluye HH ordinarias de capacitación.'),
('Interfaces del ERP/WMS sin documentación; Caso, cap. 5 y cap. 19.','R-043','Levantamiento y ensayo temprano en mes 1, antes de integrar o migrar; ARQ/DAT y TI. ERP no se modifica; WMS se sustituye progresivamente.','R-003/R-007 son calidad o volumen de historia. R-043 es contrato de intercambio/extracción no verificable.'),
('Enlace único inicial de Concepción; Caso, cap. 6 y cap. 19; S4, 4.2.5.3.','R-019','Respaldos efectivamente recibidos antes de aceptar la ola; SRE verifica caminos y continuidad por sitio.','Se amplía el evento existente y se revisa p0 a 25\%; no crear otra fila por Concepción ni declarar instalado un respaldo sólo ofertado.'),
('Peak de septiembre durante una fase; Caso, caps. 10, 17.5 y 19; S7, 7.3.5.','R-044','Plan de continuidad y usuarios antes del mes 19; seguimiento diario del cierre E2 en meses 19--20. JP con CT/Operaciones.','R-022 es autorización urgente; R-047 es saturación técnica. R-044 imputa sólo coordinación y recuperación del cierre.'),
('Obsolescencia; Revisión del Informe 2, S8, 8.2; plataforma declarada en S4.','R-045','Inventario mes 1 y revisión trimestral hasta 56; ARQ con DES/SRE. Adecuación antes del límite de soporte verificado.','Cambio excepcional de soporte/compatibilidad, excluyendo actualizaciones anuales ordinarias de 8.2.5.'),
('Dependencia del proveedor; Revisión del Informe 2, S8, 8.2; S4 y S7, 8.1.4.','R-046','Exportación/restauración utilizable y acceso del CLIENTE, en recepción y revisión anual del plan de salida; ARQ/SRE con TI.','La presencia de AWS no prueba bloqueo; el evento es una restricción efectiva de sustitución o salida.'),
('Escalabilidad; Revisión del Informe 2, S8, 8.2; S4, 4.2.6.','R-047','Ensayo por ventana y dependencia antes de H5/H10 y peak; SRE/ARQ/DES con TI/Operaciones.','Validar capacidad efectiva, no sólo escalado declarado. Separar remediación técnica de la coordinación de R-044.'),
]
cov=r'''
\subsection*{Cobertura de las omisiones identificadas}
\addcontentsline{toc}{subsection}{Cobertura de las omisiones identificadas}
\begingroup
\renewcommand{\thetable}{8.D.3}
\begin{landscape}
\setlength{\textwidth}{\linewidth}
\begin{tablalafrox}{Correspondencia de las omisiones del caso y de la revisión con el registro ampliado. Fuente: capítulos y documentos indicados.}{tab:sd8-cobertura-omisiones}{F{0.23} G{0.08} Y F{0.31}}{\cab{Materia y fuente} & \cab{ID} & \cab{Tratamiento, momento y responsable} & \cab{Delimitación para evitar duplicación}}
'''
for row in coverage:cov+=' & '.join(row)+' \\\\\n'
cov+='\\end{tablalafrox}\n\\end{landscape}\n\\endgroup\n\n'
a=a.replace('\\section*{Referencias}',cov+'\\section*{Referencias}',1)
ref='\nDistribuidora Puelche S.A. (2026b). \\emph{Bases Técnicas del Caso 02: Logística} (caps. 5--7, 10, 14--19).\n\nLafroX. (2026). \\emph{Primera revisión del Informe 2}, sección Subdocumento 8.\n'
at=a.rindex('\\endgroup');a=a[:at]+ref+a[at:]

# All rollups share the same registry values.
registry={l.split(' & ')[0]:l.split(' & ') for l in t.splitlines() if re.match(r'R-\d{3} &',l)}
assert len(registry)==51
catcounts=Counter(c[2] for c in registry.values());zcounts=Counter(re.search(r'\(([^)]+)\)',c[5])[1] for c in registry.values())
evals={rid:D(c[5].split()[0].replace(',','.')) for rid,c in registry.items()};top=sorted(evals,key=lambda k:(-evals[k],k))[:10]
start=b.index('R-002 & 0,70',b.index('\\subsection{Análisis cualitativo de riesgos}'));end=b.index('\\end{tablalafrox}',start)
table=''.join(f"{rid} & {registry[rid][3].split(' / ')[1]} & {registry[rid][4].split(' / ')[1]} & {fmt(evals[rid])} & {zone(evals[rid])} \\\\\n" for rid in top);b=b[:start]+table+b[end:]
st=b.index('R-002, R-037 y R-038 encabezan');en=b.index('\\subsection{Análisis cuantitativo}',st)
b=b[:st]+f"R-002, R-037 y R-038 conservan exposición 0,56 y zona Crítica. El registro ampliado contiene {zcounts['Crítica']} riesgos críticos, {zcounts['Alta']} altos, {zcounts['Media']} medios y {zcounts['Baja']} bajos. R-042 se incorpora con 0,28; los empates del producto se resuelven por ID ascendente. La Tabla 8.5 es una selección de diez, no el conjunto de riesgos altos. El Anexo 8.C justifica el impacto y 8.B.2 explicita las hipótesis nuevas. Las condiciones de habilitación de las innovaciones se conservan y la eficacia residual no se descuenta de esta valoración inicial.\n\n"+b[en:]
st=b.index('\\begin{tablalafrox}{Diez mayores valores esperados');rs=b.index('\nR-',st)+1;en=b.index('\\end{tablalafrox}',rs)
oldshort={l.split(' & ')[0]:l.split(' & ')[1] for l in before[paths[0]].splitlines() if re.match(r'R-\d{3} &',l) and '\\%' in l}
shorts={rid:(new[rid]['short'] if rid in new else oldshort.get(rid,registry[rid][1][:50])) for rid in q}
table=''.join(f"{rid} & {shorts[rid]} & {q[rid]['p']}\\% & {fmt(q[rid]['h'])} & {fmt(q[rid]['ve'])} \\\\\n" for rid in topq);b=b[:rs]+table+b[en:]
# Replace aggregate numbers using the published rounding convention.
totaltext=fmt(total);toptext=fmt(topsum);pcttext=f'{pct:.1f}'.replace('.',',')
b=b.replace('1.100,60',totaltext).replace('624,20',toptext).replace('56,7',pcttext)
st=b.index('La matriz de trazabilidad del Anexo 8.D registra');en=b.index('\n\n',st)
b=b[:st]+r'Las brechas de trazabilidad se incorporan como B-S4-01 $\rightarrow$ R-048 (identidad), B-S4-02 $\rightarrow$ R-049 (ERP y guías), B-S4-03 $\rightarrow$ R-050 (consolidación de stock) y B-S7-01 $\rightarrow$ R-042 (rotación nocturna). R-041, R-043--R-047 y R-051 completan las otras omisiones del caso y de la revisión. El Anexo 8.D conserva sus fuentes y reglas de no duplicación. El 38\% de rotación anual no es $p_0$; las hipótesis de ocurrencia, episodios y esfuerzo extraordinario se explicitan en 8.B.2. R-017 sigue tratando ausencia a sesiones, no rotación.'+b[en:]
b=b.replace('Esa brecha se registra como B-S4-02, sin declarar demostrada la continuidad completa.', 'La dependencia se registra en R-049, vinculada a B-S4-02; su valoración no acredita por sí sola continuidad completa.')
# Append the new events to their existing source branches and correct category counts.
b=b.replace('Esta rama contiene ocho riesgos.', 'Esta rama contiene trece riesgos.',1).replace('Agrupa siete riesgos.', 'Agrupa nueve riesgos.',1).replace('La rama contiene ocho riesgos.', 'La rama contiene once riesgos.',1)
b=b.replace('ambos de la innovación 3. Esta rama', 'ambos de la innovación 3. Se agregan obsolescencia excepcional (R-045), dependencia del proveedor (R-046), capacidad bajo peak (R-047), continuidad de identidad (R-048) y consolidación central (R-050). Esta rama')
b=b.replace('y caída del servicio de mapas (R-010). Agrupa', 'y caída del servicio de mapas (R-010). Incluye además interfaces ERP/WMS no verificadas (R-043) y nueva emisión tributaria con ERP indisponible (R-049). Agrupa')
b=b.replace('La rama contiene once riesgos.', 'Añade acuerdo de telemetría (R-041), rotación nocturna (R-042) y rechazo individual de conductores externos (R-051). La rama contiene once riesgos.')
b=b.replace('\\textbf{Contrato y licitación} contiene dos riesgos:', '\\textbf{Contrato y licitación} contiene tres riesgos:').replace('y disputas en la liquidación del tramo variable de la innovación 4 (R-039).', 'disputas en la liquidación del tramo variable de la innovación 4 (R-039) y cierre de fase afectado por el peak y congelamiento (R-044).').replace('Cada una de estas dos ramas contiene dos riesgos.', 'Contrato y licitación contiene tres riesgos y Regulatorio y externo conserva dos.')
b=b.replace('\\textbf{Solución y tecnología} (8)', '\\textbf{Solución y tecnología} (13)').replace('\\textbf{Integración y legado} (7)', '\\textbf{Integración y legado} (9)').replace('\\textbf{Personas y adopción} (8)', '\\textbf{Personas y adopción} (11)').replace('\\textbf{Contrato y licitación} (2)', '\\textbf{Contrato y licitación} (3)')

# Count updates do not touch the user-protected academic citations or historical source facts.
def counts(s):
 out=[]
 for l in s.splitlines():
  if 'contenido academico' not in l:
   for x,y in [('40 riesgos','51 riesgos'),('40 eventos','51 eventos'),('40 registros','51 registros'),('entre los 40','entre los 51'),('los 40,','los 51,'),('R-001--R-040','R-001--R-051'),('R-001 a R-040','R-001 a R-051'),('20 dependencias del CLIENTE','31 riesgos con coordinación del CLIENTE'),('las 20 dependencias','los 31 riesgos con coordinación'),('los 20 riesgos que requieren','los 31 riesgos que requieren'),('las 20 dependencias','la coordinación de los 31 riesgos')]:l=l.replace(x,y)
  out.append(l)
 return '\n'.join(out)+'\n'
b,a,t=map(counts,[b,a,t])
# The categorical product is invariant; only source branch counts change.
cats=['Solución y tecnología','Integración y legado','Operación del cliente','Personas y adopción','Contrato y licitación','Regulatorio y externo']
oldrbs={m[0]:(m[1],m[2]) for m in re.findall(r'\\RBSrisk\{(R-\d{3})\}\{([^\n]+)\}\{([^}]+)\}',rb)}
for rid,(short,z) in list(oldrbs.items()):
 rb=re.sub(r'(\\RBSrisk\{'+rid+r'\}\{[^\n]+\})\{[^}]+\}',lambda m:m[1]+'{'+re.search(r'\(([^)]+)\)',registry[rid][5])[1]+'}',rb)
for cat in cats:
 title=f'{cats.index(cat)+1} · {cat}'
 st=rb.index(title);en=rb.index('\\end{minipage}',st)
 segment=rb[st:en];segment=re.sub(r'\{\\small \d+ riesgos\}',lambda m:'{\\small '+str(catcounts[cat])+' riesgos}',segment,count=1)
 segment+=''.join(f"\\RBSrisk{{{d['rid']}}}{{{d['short']}}}{{{d['zone']}}}\n" for d in records if d['cat']==cat)
 rb=rb[:st]+segment+rb[en:]
rb=rb.replace('40 riesgos','51 riesgos')
# Compact only the inter-risk gap; retain the existing readable font.
rb=rb.replace('#2\\par\\vspace{1pt}', '#2\\par\\vspace{0pt}')
for p,s in zip(paths,[b,rb,t,a]):(r/p).write_text(s,encoding='utf-8')

serial=[{k:(str(v) if isinstance(v,D) else v) for k,v in d.items()} for d in records]
(r/'tmp/tarea5-nuevos-riesgos.json').write_text(json.dumps(serial,ensure_ascii=False,indent=2),encoding='utf-8')
note=['# Tarea 5: omisiones incorporadas','', 'Se agregan once riesgos R-041–R-051 y se conservan los cuarenta IDs anteriores. R-016 explicita jubilación y caída de 6–9 puntos y revalora I=4; R-019 explicita el enlace único inicial de Concepción y revisa p0 de 5 % a 25 %, manteniendo sus HH condicionales.','', '## Asunciones y cuantificación','', 'Las probabilidades nuevas son hipótesis de planificación, no estadísticas del caso ni riesgos residuales demostrados. Fuente, ventana, episodios y bases de esfuerzo en 8.B.2; impacto máximo en 8.C.1. Se excluyen tareas ordinarias, pérdidas de bienes y reconstrucción del ERP del CLIENTE. El 38 % de rotación y las 2.600 entregas no se usan como p0.','', f'Total ampliado: {fmt(total)} HH esperadas. Diez mayores: {fmt(topsum)} HH ({pcttext} %). Se suman VE por riesgo redondeados a dos decimales; cada VE usa PERT sin redondear. Base anterior 1.100,60 HH; incremento R-019 de 12 HH y nuevos riesgos de '+fmt(sum((rnd(d['ve']) for d in records),D(0)))+' HH. No se deriva ni asigna una reserva aprobada, ni se modifica T-15, presupuesto o cronograma.','', '## Correspondencia para sincronización final','', '| ID | Omisión / fuente |', '|---|---|']
for d in records:note.append(f"| {d['rid']} | {d['short']}; {d['source']} |")
note+=['','Brechas de tarea 4: B-S4-01→R-048; B-S4-02→R-049; B-S4-03→R-050; B-S7-01→R-042. Estados actualizados en Anexo 8.D.','', 'S4: enlazar riesgos R-043 y R-045–R-050 con contratos, capacidad, dependencia de AWS, identidad, ERP y stock. No atribuir a controles no ensayados eficacia demostrada. S7: vincular R-041 con 5.4.2, R-042 con 7.1.2 (13–56, IMP hasta21/SRE desde22), R-043 con1.2.3/3.3.2, R-044 con cierre E2 y R-051 con7.1.3. S3: conservar exclusión de cámaras en cabina, ERP único no modificable y WMS sustituido progresivamente.','', 'S6/T9: integrar contrapartes y objetivos de coordinación de los once nuevos riesgos sin transferir responsabilidad de diseño. S13: conservar sincronizaciones pendientes de tarea2 y R-034 según tarea4.','', 'R-044 y R-047 no son duplicados: coordinación/cierre frente a saturación técnica. R-013/R-031/R-051 separan firma, habilitación de reemplazo y rechazo individual. R-017/R-042 separan inasistencia y sobrecarga de inducción por rotación. R-008/R-049 separan SII y ERP. R-004/R-019/R-050 separan conciliación inicial, WAN y consolidación central.','', '## Pendientes siguientes','', 'Tarea6 revisa los trece internos originales y la ubicación de controles técnicos añadidos (R-045–R-048/R-050), preservando su trazabilidad según naturaleza; no se adelanta su reubicación. Tarea7 completa costo-beneficio, esfuerzo de respuesta y riesgo residual. Tarea8 concilia la nueva exposición de esfuerzo con reservas y cronograma. Tarea9 aplica la técnica requerida.']
n='\n'.join(note)+'\n'
for x,y in [('hasta21','hasta 21'),('desde22','desde 22'),('con1.2.3','con 1.2.3'),('con7.1.3','con 7.1.3'),('tarea2','tarea 2'),('tarea4','tarea 4'),('Tarea6','Tarea 6'),('Tarea7','Tarea 7'),('Tarea8','Tarea 8'),('Tarea9','Tarea 9')]:n=n.replace(x,y)
(r/'odd/tasks/tarea-5-riesgos-omitidos.md').write_text(n,encoding='utf-8')
print('Nuevos',len(new),'total',len(registry),'categorías',dict(catcounts),'zonas',dict(zcounts))
print('Total VE',totaltext,'Top VE',toptext,pcttext+'%','Top',topq)
