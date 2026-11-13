# Formulario T-15 — Nivelación de recursos

> Texto extraído del [PDF final](LAFROX-Formulario-T-15.pdf). Las figuras y la composición visual se consultan en el PDF.

LafroXSpA
LICITACIÓNPÚBLICA
LicitaciónN.°TFEP-01/2026
ProyectodePlataformaDigitaldeMisiónCrítica
Caso—Logística
SobreN.°2—OfertaTécnica
PropuestaTécnica
FormularioT-15—NivelacióndeRecursos
Subdocumento07·FormularioT-15
MANDANTE
DistribuidoraPuelcheS.A.
PROPONENTE
LafroXSpA
RUT77.418.902-K
Av.Brasil2241,Valparaíso
REPRESENTANTELEGAL
AlexAravena
JefedeProyectoyApoderado
contacto@lafrox.cl
+56322504100
FECHADEEMISIÓN
12deoctubrede2026
FIRMADELREPRESENTANTELEGAL
AlexAravena
JefedeProyectoyApoderado·LafroXSpA
LAFROX-Formulario-T-15.pdf 1

---

LafroXSpA
Índicegeneral
Índicegeneral 2
Listadetablas 3
Listadefiguras 4
FormularioT-15:Nivelaciónderecursos 5
1 Métododeestimaciónydeprogramación 5
1.1 Estimación 5
1.2 Programación 6
2 Rutacríticayholguras 6
3 Frentesdetrabajoysolapamientos 7
4 Modelocuantitativoderecursos 11
4.1 Supuestosycálculo 11
4.2 Horasporlos227paquetes 14
4.3 ResumenT-15 29
4.4 Curvasmensuales:horasporetapayplazaspororigen 46
4.5 Reservasdecontingenciaydegestión 56
5 Redagregada,restriccionesyescenariosdecalendario 56
5.1 Cálculoreproducible 56
5.2 Lecturadelassecuenciasylasrestricciones 69
5.3 Holgurasdeloshitosycapacidad 69
5.4 Gobierno 71
5.5 PresentacióndeentregablesyrevisióndelCLIENTE 71
5.6 Medicióndelosnivelesdeatención 72
5.7 Dotaciónrequerida,rolesmínimosydotacióndeclarada 73
6 Listadeactividades:regladel8/80ydelperíododereporte 75
6.1 Paquetesconentregableyplanificacióngradual 75
6.2 Paquetesdeesfuerzocontinuo 106
6.3 Perfilesyesfuerzoparalavalorización 114
Referencias 138
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
2

---

LafroXSpA
Listadetablas
Tabla1 Frentesdetrabajo. 8
Tabla2 Supuestosycálculo. 13
Tabla3 Horasporlos227paquetes. 15
Tabla4 ResumenT-15. 30
Tabla5 Tamañoyesfuerzodelosmódulos(HH). 32
Tabla6 Fundamentodeloptimistaydelpesimistadecadamódulo. 34
Tabla7 Elementosdealcancedecadamódulo. 35
Tabla8 RangosdelPERTportipodepaquete. 44
Tabla9 Paquetesconrangopropioporriesgoidentificado. 44
Tabla10 ConciliacióndelasHHquecambian. 45
Tabla11 Curvamensualdehorasporetapa. 47
Tabla12 Demandamensualdeplazasporgrupodeorigen. 52
Tabla13 Fechastempranas,tardíasyholgurasdelos168paquetesconentregable. 58
Tabla14 Fechasyholgurasdeloshitoscalculadasporduracionesyprecedencias,conla
líneabasede199.219,03HH. 70
Tabla15 SecuenciadelactaintegradadeH7yH12.Calendariosinobservaciones. 72
Tabla16 Plazasprevistasydemandamáximamensualpororigen. 73
Tabla17 Programacióndelospaquetesconentregable. 79
Tabla18 ActividadesdelospaquetesqueterminanhastaelH2. 90
Tabla19 ActividadesdelospaquetesqueterminanhastaelH2. 96
Tabla20 Iteracionesdeconstruccióndelosmódulossegúnlacarta(día/mes). 105
Tabla21 Actividadesdelospaquetesdeesfuerzocontinuo. 108
Tabla22 Perfiles,plazaspropuestasyjornadasequivalentesporfase. 115
Tabla23 AsignacióndeHHporpartidayperfil. 119
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
3

---

LafroXSpA
Listadefiguras
Figura1 CaminoquecontrolaelH12ysuholguracontractual. 7
Figura2 Frentesdetrabajodelosmeses1a21ysolapamientosdelartículo17.2delas
BasesAdministrativas(p.13). 9
Figura3 Planificacióngradualdelcronograma. 77
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
4

---

FormularioT-15:Nivelaciónderecursos
EsteformulariopresentalainformacióndeplanificaciónquepideelFormularioT-15de
lasBasesAdministrativasparaelSubdocumento7:elmétodoconqueseestimanlashoras
hombredecadapaquete,laprogramaciónsobrelareddedependencias,larutacríticaysus
holguras,ylosfrentesdetrabajo,coneldetalledelossolapamientosdelosmeses13a15y19a
20.LospaquetesdetrabajosonlosdelaEDTdelFormularioT-14.Esteformularionocontiene
preciosnicostos(artículo50.2delasBasesAdministrativas(p.29)).
Enesteformulario,BA,BTTyCasodesignanlasBasesAdministrativas,lasBasesTécnicas
TransversalesylasBasesTécnicasdelcaso.SDseguidodeunnúmeroidentificaelSubdocu-
mentocorrespondiente.EDTsignificaestructuradedescomposicióndeltrabajo;PT,paquete
detrabajo;HH,horashombre;yE1/E2,Etapas1y2.EnlascartasGantt,RCidentificalosele-
mentosmarcadoscomorutacríticaenlafuentedeprogramaciónyPT/Hidentificalosdemás
paquetesehitos.H1–H12sonloshitosdelFormularioE-25yF1–F8,losfrentesdetrabajo.QA
designaelambientedecalidad;SRE,elequipodeoperacióneingenieríadefiabilidad;NOC,el
centrodeoperaciones;SOC,elcentrodeoperacionesdeseguridad;yDTE,losdocumentos
tributarioselectrónicos.
1 Métododeestimaciónydeprogramación
LaestimaciónylaprogramaciónsiguenelPMBOKylatécnicaPERT,demodoquecada
duraciónycadaholgurasepuedanreconstruirapartirdevaloresdeclarados.
1.1 Estimación
Elesfuerzodecadapaqueteseestimacontresvaloresenhorashombre(ProjectManage-
mentInstitute[PMI],2017,p.201):eloptimista(O),quecorrespondealmejorescenario;elmás
probable(M),conrecursosyproductividadrealistas;yelpesimista(P),quecorrespondeal
peorescenario.Laincertidumbredecadaestimaciónserepresentaconunadistribuciónbeta,
queelPMBOKadmiteentrelasdistribucionesparamodelarlaincertidumbre(PMI,2017,p.
432).Conella,latécnicaPERTcalculaelvaloresperadoyladesviación(Malcolmetal.,1959):
T_E=(O+4M+P)/6; 𝜎=(P−O)/6.
Lap.201delPMBOKpresentatambiénladistribucióntriangular, (𝑂 +𝑀 +𝑃)/3.Seusalabeta
porqueponderamáselvalormásprobable,quesefundaenlosrequerimientosycantidades
decadapaquete.
Las bases de cada estimación se declaran por tipo de paquete. Los módulos y las inte-
graciones se estiman con los requerimientos del Formulario T-12 asignados al paquete; la
infraestructura,conlascantidadesdelFormularioT-11;laimplantaciónylacapacitación,con
laspersonasyrutasdelcasoyladotacióndelFormularioT-18,sección2.6;ylaoperación,con
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
5

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
loshorariosdecoberturadelospaquetes8.1.1y8.1.2ylaperiodicidaddelosinformes.Los
paquetesdelafase8sondeesfuerzocontinuo:suestimaciónesmensualysemultiplicapor
los36mesesdeoperación.
1.2 Programación
La duración se contrasta con esfuerzo, capacidad efectiva y dependencias. La sección 6
programalospaquetesydescomponeenactividadesde8a80HH,quecabenenunaquincena,
sólolosqueterminanhastaelH2;losdemássedetallanporplanificacióngradualantesde
cada fase. Las ventanas de la sección 4 son supuestos de asignación y la red agregada de la
sección 5 explicita el cálculo del calendario. Las dependencias entre paquetes están en el
Anexo7.BdelSubdocumento7,ysobreesaredseaplicaelmétododelarutacrítica(PMI,2017,
pp.210–211):unapasadahaciaadelantedaelinicioyelfintempranos;unapasadahaciaatrás,
desdelosmesesfijosdelartículo17delasBasesAdministrativas(pp.12–13),daelinicioyel
fintardíos;ladiferenciaLS−ESeslaholguratotal;laholguralibresecalcularespectodelES
desussucesores.LoshitosdelFormularioE-25sonrestriccionesdefechafija:uncaminoque
nollegaasuhitotieneholguranegativayobligaareplanificar.
Lasección5calculalaredconlalíneabasede199.219,03HHylosplazosderevisióndel
CLIENTE,ylasección5.5presentalasecuenciadecierre,actaypasoaproduccióndeH7y
H12.
2 Rutacríticayholguras
El camino de aceptación de H12 pasa por el cierre de la marcha blanca, la revisión del
expedienteyelcorteautorizado.Lagarantía4.3.4setramitaenparaleloydebeestarconstituida
alpresentarelexpediente.Lasección5.5detallaelactaintegradadeH7yH12.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
6

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
4.3.1 — Marcha blanca de la
Etapa 2
Meses 19 y 20
Cierre: 30 de septiembre de
2028
4.3.4 — Garantía
de correcto funcionamiento
7 días hábiles; 80 HH
13 al 25 de septiembre de 2028
4.3.3 — Preparación del acta de aceptación
7 días hábiles; 80 HH
Entrega calculada: 11 de octubre de 2028
Revisión del CLIENTE — Art. 18.3
10 días hábiles
Acta calculada: 25 de octubre de 2028
Figura1 CaminoquecontrolaelH12ysuholguracontractual.Fuente:elaboraciónapartirdelT-15,secciones
5.1–5.3y6.1.
LafiguramuestralacadenaquecontrolaH12;lasdemásramassecalculanenlaTabla 13.H7
yH12tienenholgurascontractualesdediezyochodíashábiles,yH8,dedieciséis.Losciclos
demarchablancamantienensusventanascompletas,sinutilizarsuscuatrosemanasfinales
comoreserva.
LaholgurasegestionaenlasinstanciasdegobiernodelaEDT:elavancedelarutacrítica
y de los caminos casi críticos se revisa en la reunión semanal y en el Comité de Proyecto
quincenal(paquetes1.3.5y1.8.3);todadesviaciónquecomprometaunhitoseescalaalComité
Ejecutivoconsuanálisisdeimpacto(paquetes1.4.3y1.8.2);yelinformemensualconvalor
ganadoavisatodadesviaciónmayoral10%consuplandentrodecincodíashábiles(paquete
1.8.6).
3 Frentesdetrabajoysolapamientos
Unfrentedetrabajoesunequipoconunresponsableyunconjuntodecuentasdecontrol
que avanza en paralelo con los demás. La Tabla1 define los frentes a partir de la EDT del
FormularioT-14ydelosresponsablesdesudiccionario.F3sedivideenlostressubfrentes
del Capítulo 3, sección 3.4.3 (Subdocumento 3): bodega y calidad (M1, M2, M5, M9 y M12);
preventa,rutasyreparto(M3,M4,M6yM8);ydatosyrendición(M7yM10).
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
7

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla1 Frentesdetrabajo.Fuente:(FormularioT-14).
Frente Responsable Cuentasdecontrol Mesesactivos
F1Dirección,gobierno
ycumplimiento
JefedeProyecto 1.1a1.4,1.6a1.9,5.4.1
a5.4.3,8.4,9
1a56
F2Arquitectura,seguri-
dadydatos
ArquitectodeSolución,
conSeguridadyDatos
2.1a2.6,3.3,3.7,3.11 1a21
F3Construcciónyco-
rreccionesE1
LíderdeDesarrollo 3.4,3.6.1a3.6.4,3.10.1
a3.10.3;capacidad
protegida4.2.2
1a20
F4Construccióndela
Etapa2
LíderdeDesarrollo 3.5,3.6.5,3.6.6,3.10.4 13a20
F5Plataforma,infra-
estructuraysoporte
puente
LíderdeOperación/
SRE
3.1,3.2,5.1a5.3,6.1a
6.6;soporte4.2.2
1a20
F6Calidadypruebas LíderdeCalidad 1.5,3.8,3.9 1a21
F7Implantaciónyges-
tióndelcambio
LíderdeImplantacióny
GestióndelCambio
4.1a4.3,7.1a7.3 2a21:diagnóstico
delcambioen2–6,
preparacióndesdeel8y
pilotodefríoen10–11
F8Operaciónysoporte LíderdeOperación/
SRE
8.1a8.3,8.5 21a56
LosfrentessesincronizanenloshitosdelFormularioE-25yenloscomitésdelartículo71
delasBasesAdministrativas(p.37),cuyasactasregistranlosacuerdosentrefrentes(paquetes
1.8.2a1.8.5).LaFigura 2presentasuventanadeactividadentrelosmeses1y21.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
8

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Frentes de trabajo · meses 1 a 21
Lámina 1 de 2 · meses calendario · continuidad de filas y vínculos por ID
ID
Frente y responsable
Inicio
Fin
02
03
04
05
06
07
08
09
10
11
12
01
02
03
04
05
06
07
08
09
10
Período: 02/2027 a 10/2028
F1
F1 Dirección, gobierno y cumplimiento. Jefe
de Proyecto. Cuentas: 1.1 a 1.4, 1.6 a 1.9,
5.4.1 a 5.4.3, 8.4, 9. Meses: 1 a 56
01/02/27
30/09/31
F2
F2 Arquitectura, seguridad y datos.
Arquitecto de Solución, con Seguridad y
Datos. Cuentas: 2.1 a 2.6, 3.3, 3.7, 3.11.
Meses: 1 a 21
01/02/27
31/10/28
F3
F3 Construcción y correcciones E1. Líder de
Desarrollo. Cuentas: 3.4, 3.6.1 a 3.6.4,
3.10.1 a 3.10.3; capacidad protegida 4.2.2.
Meses: 1 a 20
01/02/27
30/09/28
F4
F4 Construcción de la Etapa 2. Líder de
Desarrollo. Cuentas: 3.5, 3.6.5, 3.6.6, 3.10.4.
Meses: 13 a 20
01/02/28
30/09/28
F1–F8 identifican los frentes de trabajo y sus responsables.
Las barras con flecha derecha continúan después del mes 21.
Figura2 Frentesdetrabajodelosmeses1a21ysolapamientosdelartículo17.2delasBasesAdministrativas(p.13).Fuente:elaboraciónapartirdelaTabla 1y
(FormularioT-14).
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
9

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Frentes de trabajo · meses 1 a 21
Lámina 2 de 2 · meses calendario · continuidad de filas y vínculos por ID
ID
Frente y responsable
Inicio
Fin
02
03
04
05
06
07
08
09
10
11
12
01
02
03
04
05
06
07
08
09
10
Período: 02/2027 a 10/2028
F5
F5 Plataforma, infraestructura y soporte
puente. Líder de Operación / SRE. Cuentas:
3.1, 3.2, 5.1 a 5.3, 6.1 a 6.6; soporte 4.2.2.
Meses: 1 a 20
01/02/27
30/09/28
F6
F6 Calidad y pruebas. Líder de Calidad.
Cuentas: 1.5, 3.8, 3.9. Meses: 1 a 21
01/02/27
31/10/28
F7
F7 Implantación y gestión del cambio. Líder
de Implantación y Gestión del Cambio.
Cuentas: 4.1 a 4.3, 7.1 a 7.3. Meses: 2 a 21:
diagnóstico del cambio en 2–6, preparación
desde el 8 y piloto de frío en 10–11
01/03/27
31/10/28
F8
F8 Operación y soporte. Líder de Operación
/ SRE. Cuentas: 8.1 a 8.3, 8.5. Meses: 21 a
56
01/10/28
30/09/31
F1–F8 identifican los frentes de trabajo y sus responsables.
Las barras con flecha derecha continúan después del mes 21.
Figura2(continuación2de2).Frentesdetrabajodelosmeses1a21ysolapamientosdelartículo17.2delasBasesAdministrativas(p.13).Fuente:elaboracióna
partirdelaTabla 1y(FormularioT-14).
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
10

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
En los meses 13 a 15 trabajan a la vez F7, en la marcha blanca de la Etapa 1; F3, en las
correccionesdeesamarchablanca;F4,eneldesarrollodelaEtapa2;F6,enlaspruebasde
ambas etapas; y F1 y F2. F3 y F4 dependen del mismo rol, el Líder de Desarrollo, y por eso
sonequiposdistintos:elequipoqueatiendelamarchablancanopuedeserelquedesarrolla
la Etapa 2 (artículo 17.2 de las Bases Administrativas (p. 13), punto 1). En los meses 19 y 20
trabajanF7,enlamarchablancadelaEtapa2;F4,ensuscorrecciones;F6;yelsoportedela
Etapa1enproducción.
4 Modelocuantitativoderecursos
Basedecálculo: estimaciónporclasesdetamañotrazablealT-12yalT-11,queserecalcula
conelequipoalestablecerlalíneabaseyqueelCapítulo8usaparacuantificarlosriesgos.La
productividadyladotaciónsecontrastanconelavancerealencadaComitédeProyecto.
4.1 Supuestosycálculo
Lossupuestosyelcálculodelmodeloderecursossonlossiguientes.
• Capacidad nominal asumida: 160 HH/persona-mes; disponibilidad programable 80%;
capacidad efectiva 128 HH. El 20% cubre ausencias y coordinación no imputada. No es
unajornadacontractualniuncálculodecumplimientolaboral.
• Esfuerzo por clase: G gestión/acta 80 HH; E diseño/configuración/innovación 240 HH; I
integración/migración480HH;Vprueba320HH(integraciónycierresdecertificación:160
HH);Tinstalación/capacitación160HH.LasclasessefundanenlascantidadesdelT-11y
enelcontenidodecadatipo;latablaalfinaldeestasecciónexplicaquécontienecadauna.
Losmódulos(D)notienenunvalordeclase:seestimanportamañodesdesusrequisitos
delT-12(sección4.3).
• Ridentificaesfuerzorecurrentemensual,incluidosequivalentesmensualesdeactividades
anuales/semestrales: la distribución contable no cambia la frecuencia de ejecución del
T-14.
• A identifica acompañamiento: 13 puestos simultáneos de terreno/coordinación; 12× 24
días ×8horas+160HHdecoordinación=2.464HHporcuatrosemanas;soporteE1meses
16–20conprevisión2.464/1.312/544/544/544HHparapuestos13/7/3/3/3,condicionadaa
losindicadoresdelT-18.Laestabilización4.3.2seiniciaconelpasoaproduccióndel18de
octubrede2028ysuscuatrosemanasreforzadasconcluyenel16denoviembre:11desus
24jornadasdelunesasábadocaenenelmes21y13enel22.Arazónde2.464/24HHpor
jornada,corresponden1.129,33y1.334,67HH.
• Cidentificacoberturaporhoras-posicióndelcalendarioreal,conelmes1enfebrerode
2027(Anexo7.A).ElSOC(8.1.5)mantieneunpuesto24 ×7:díasdelmes ×24,queson744
HHenunmesde31días,720enunode30y672enfebrero.ElNOC(8.1.1)cubretambién
unpuesto24 ×7,conladedicacióndeclaradadelSD4(Subdocumento4),Anexo4-W.7:100%
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
11

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
enlosmeses21a32,75%enlosmeses33a44y50%enlosmeses45a56.Ademásatiende
lamesade20:00a22:00delunesasábadocon1,9horas-posiciónpordíayformaaocho
operadores en los procesos de Puelche: 128 HH en el mes 21 y 64 HH en los meses 33 y
45,más16HHdelinstructorenelmes21.Lamesa(8.1.2,primeralíneadeincidentesdel
artículo78delasBasesAdministrativas(p.40))aplicalasposicionesdelmismoanexo:7
en lahoracargaday 2 en lasotras15 horasde 04:00 a 20:00, o 37 horas-posiciónpor día
delunesasábado.Enseptiembreydiciembredesdeelmes25sumaunterceragenteen
esas15horas,52horas-posiciónpordía,conelqueladotacióncubrelostresnivelesde
servicio hasta 2.391 contactos al mes. En septiembre y diciembre se suman, además, 6
horas-posiciónde22:00a04:00delunesasábadoy24losdomingos.Así,unmesde26días
delunesasábadoexige26 ×37=962HHdemesa,yseptiembrede2029exige25 ×(52+6)
+5 ×24=1.570HH.ElSOCespropiodeLafroXyoperadesdesuCentrodeOperaciones
enValparaíso (RT-11.17; SD4, Anexo 4-W.7); sus HH se imputan aquí. Las posiciones de
lamesaprovienendeunErlangCconsupuestosdedemanda:noacreditanabandononi
resolución al primer contacto, que se miden según la sección 5.6. La curva dimensiona
relevoscon128HHefectivas.
• OyPtienenfundamentopropio:cadamódulosegúnsuficha,cadatipodepaquetesegúnlo
quehacevariarsuesfuerzoylospaquetesconriesgoidentificadosegúneseriesgo(sección
4.3). E = (O + 4M + P)/6. Para A/C, O = M = P: no se reduce cobertura por un escenario
optimista.Losriesgosdedemandayausenciassetratanseparadamente.
• Esereparteuniformementeentrelosmesesinclusivosdeclaradoscomopresupuestopreli-
minar,salvolaspruebasdecertificaciónreprogramadas3.9.2–3.9.7yelacompañamiento
4.3.2, quese imputanpor los días de ejecuciónde cadames.Las ventanas relativaspue-
den abarcar meses de reserva sin trabajo continuo: la Tabla17 fija el inicio y fin de los
paquetesconentregableyeldiccionarioT-14mantienelasrestriccionesdeaceptación.Las
precedenciasdentrodeunmessecompruebanenlareddiariadelasección5.
• La demanda mensual de plazas se calcula por grupo de origen del SD1: las HH del mes
detodoslosrolesdelgruposedividenpor128yseredondeanhaciaarribaunasolavez,
demodoqueunafraccióndemesdecadaperfilnosecuentacomounaplazacompleta.
Las HH de cada rol siguen el reparto de este apartado y las ventanas de la Tabla3. La
mesaN1,elNOCyelSOCconservansushorasdecoberturaporcalendario.Losservicios
especializados contratados por resultado se incluyen en las HH del plan sin imputarles
unnúmerodepersonas.Lasección5.7comparalademandaconlaplantadeclaradayla
asignaciónprevista.
• ReservaprotegidaE1enmeses13–20:dosdesarrolladoresyunQA,256HHdedesarrolloy
128HHdepruebaspormes;noseprestaaE2niseduplicacomotrabajobase.
• Soporte puente E1 meses 16–20: puesto NOC completo y mesa de 04:00 a 22:00 con 41
horas-posición por día de lunes a sábado, más la cobertura 24×7 de septiembre (1.851,
1.786, 1.810, 1.851 y 2.038 HH; total 9.336 HH), imputado a 4.2.2 y financiado dentro de
implementación.ElSOCoperadesdeelmes13por8.1.5,porquelamarchablancayatrata
datosreales.Operacióncontractualempiezaenelmes21.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
12

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
• Lasventanasdelasección4.2reservancapacidadpormes;nosonequivalentesalosdías
efectivosdetodaslasactividadesdelasección6.1.Cuandoelpaqueteempiezaotermina
dentrodeunaventanamásamplia,losmesessinejecuciónsonmargendeprogramación,
notrabajoadicionalniuncambiodealcance.Losplanos2.3.1/2.3.2sehacenenelmes1,la
especificaciónycompra5.1.2enelmes2,lainstalación6.1.1–6.1.4enelmes3ylarecepción
6.1.5 en el mes 4 (D-09 a D-11). Los prototipos 2.6.2 terminan antes de la construcción
3.4(D-05);laidentidad3.3.1empiezadespuésdelplandeseguridad(D-06);losmódulos
se programan con dependencias por interfaz (D-16, D-18 y D-19); y las certificaciones
empiezanalterminarsupruebadeintegración(D-21yD-31).Laactualizaciónanualdel
PlandeReversibilidad1.7.2ocurreenelmes15,primeraniversariodesuentregadelmes
3;lassiguientesson8.1.4.Elacompañamientodesalida9.2.1ocupalosmeses54a56para
cubrirsus90díasdentrodelcontrato.
Laclaseesunaestimaciónporanalogíaynounatarifa:fijaelesfuerzoesperadodeunpaquete
típicodesutipo,yelequipoloajustaenlalíneabase.
LaTabla 2presentasupuestosycálculo.
Tabla2 Supuestosycálculo.Fuente:elaboraciónapartirdelassecs.4.1–4.4deesteformularioyde(Formulario
T-14,paquetesdetrabajo).
Clase Quécontiene Esfuerzo Ejemployrazón
G Documentooactade
gestiónconunrespon-
sableyunarevisión
80HH 1.1.1Actadeconsti-
tución:dospersonas
unasemana,porque
formalizadecisionesya
tomadasenlaoferta
E Diseño,configuración
oespecificaciónque
requiereanálisis,elabo-
raciónyrevisión
240HH 2.2.3Planderespuesta
aincidentesdesegu-
ridad:análisis,elabo-
raciónyrevisióncon
cuatroespecialistas
D Módulofuncionalcon
susrequerimientosdel
T-12,contratosdein-
terfaz,construcciónen
incrementos,pruebase
integraciónenQA
Portamaño:entre280
y1.587,33HH(sección
4.3)
3.4.8Reparto(1.586,67
HH)sumafirmaelec-
trónica,sincronización
delturnoydosdispo-
sitivos;3.5.3Portalde
transportistas(280HH)
tienetresflujossimples
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
13

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla2—continuación
Clase Quécontiene Esfuerzo Ejemployrazón
I Interfazomigración
conanálisisdemues-
trasreales,contrato,
adaptador,pruebasde
fallayentrega
480HH 3.3.2ERP:interfacessin
documentación(Caso
cap.17.5),poresoexige
análisisconmuestrasy
pruebasdelentitud
V Pruebaampliadacon
preparacióndedatos,
dosciclosyregresión
320HH(160enintegra-
ciónycierre)
3.8.4Cargaa1,5veces
elpeakdeseptiembre
T Instalaciónocapacita-
ciónconejecucióny
acta
160HH 6.1.1Coordinacióndela
obracivilypisotécnico
delasala
4.2 Horasporlos227paquetes
La ampliación de frío agrega 1.200 HH: banco 2.4.3, 320 HH (prueba V); mapeo 2.4.4,
240HH(diseñoE);piloto4.1.4,320HH(pruebaV);compra5.1.4,240HH(especificaciónE);
contratos5.3.4,80HH(gestiónG).Reestima320HHenpaquetesexistentes:160HHen6.5.4
para instalación y recepción del kit; 80 HH en 7.1.3 para inducción y 80 HH en 7.2.4 para
contingenciayruptura.Lasreglastérmicas,losescaneos,ladisposición,laingestasatelitaly
losdispositivosdefríoformanpartedelaestimaciónportamañodelosmódulos3.4.4y3.4.5
(sección4.3),yelbanco2.4.3yelpiloto4.1.4tienenrangopropioporriesgo.Elbancovalidael
prototipoantesdelaconstruccióndelaversiónintegrada;suspruebasserepitensobreesa
versiónantesdelpiloto.
Latablasiguientepresentalashorasdecadapaqueteconsustresestimacionesysuvalor
esperado.
LaTabla 3presentahorasporlos227paquetes.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
14

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3 Horasporlos227paquetes.Fuente:elaboraciónapartirdelassecs.4.1–4.4deesteformularioyde(FormularioT-14,EDT).
EDT Clase Rol Meses OHH MHH PHH EHH
1.1.1 G JP 1–1 72.00 80.00 88.00 80.00
1.1.2 G JP 1–1 72.00 80.00 88.00 80.00
1.1.3 G JP 1–1 72.00 80.00 88.00 80.00
1.2.1 G ARQ 1–1 72.00 80.00 88.00 80.00
1.2.2 G IMP 1–3 72.00 80.00 88.00 80.00
1.2.3 G ARQ 1–4 72.00 80.00 88.00 80.00
1.2.4 G CAL 2–2 72.00 80.00 88.00 80.00
1.2.5 G ARQ 13–13 72.00 80.00 88.00 80.00
1.3.1 G JP 1–1 72.00 80.00 88.00 80.00
1.3.2 G JP 2–2 72.00 80.00 88.00 80.00
1.3.3 G JP 2–2 72.00 80.00 88.00 80.00
1.3.4 G JP 2–2 72.00 80.00 88.00 80.00
1.3.5 R JP 1–20 432.00 480.00 528.00 480.00
1.4.1 G JP 1–1 72.00 80.00 88.00 80.00
1.4.2 G JP 1–1 72.00 80.00 88.00 80.00
1.4.3 R JP 1–56 806.40 896.00 985.60 896.00
1.5.1 G CAL 2–2 72.00 80.00 88.00 80.00
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
15

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
1.5.2 G CAL 6–20 72.00 80.00 88.00 80.00
1.6.1 G JP 2–2 72.00 80.00 88.00 80.00
1.6.2 R JP 1–20 144.00 160.00 176.00 160.00
1.7.1 G JP 3–3 72.00 80.00 88.00 80.00
1.7.2 G JP 15–15 72.00 80.00 88.00 80.00
1.8.1 R JP 1–20 288.00 320.00 352.00 320.00
1.8.2 R JP 1–56 403.20 448.00 492.80 448.00
1.8.3 R JP 1–20 216.00 240.00 264.00 240.00
1.8.4 R ARQ 1–56 403.20 448.00 492.80 448.00
1.8.5 R SRE 13–56 316.80 352.00 387.20 352.00
1.8.6 R JP 1–20 432.00 480.00 528.00 480.00
1.8.7 R JP 2–56 396.00 440.00 484.00 440.00
1.8.8 R JP 1–56 403.20 448.00 492.80 448.00
1.9.1 G SEG 1–1 72.00 80.00 88.00 80.00
1.9.2 G SEG 1–1 72.00 80.00 88.00 80.00
1.9.3 G SEG 2–2 72.00 80.00 88.00 80.00
1.9.4 R SEG 1–56 201.60 224.00 246.40 224.00
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
16

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
1.9.5 R JP 1–56 201.60 224.00 246.40 224.00
2.1.1 E ARQ 2–2 192.00 240.00 288.00 240.00
2.1.2 E ARQ 2–2 192.00 240.00 288.00 240.00
2.1.3 E DAT 2–2 192.00 240.00 288.00 240.00
2.1.4 E ARQ 13–13 192.00 240.00 288.00 240.00
2.2.1 E SEG 2–2 192.00 240.00 288.00 240.00
2.2.2 E SEG 3–10 192.00 240.00 288.00 240.00
2.2.3 E SEG 3–3 192.00 240.00 288.00 240.00
2.2.4 E SEG 2–2 192.00 240.00 288.00 240.00
2.3.1 E SRE 1–2 192.00 240.00 288.00 240.00
2.3.2 E SRE 1–2 192.00 240.00 288.00 240.00
2.3.3 E SRE 2–2 192.00 240.00 288.00 240.00
2.4.1 E ARQ 3–3 192.00 240.00 288.00 240.00
2.4.2 E ARQ 13–13 192.00 240.00 288.00 240.00
2.4.3 V SRE 3–3 288.00 320.00 480.00 341.33
2.4.4 E ARQ 4–4 192.00 240.00 288.00 240.00
2.5.1 E SRE 3–3 192.00 240.00 288.00 240.00
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
17

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
2.5.2 E SRE 3–3 192.00 240.00 288.00 240.00
2.6.1 E IMP 2–2 192.00 240.00 288.00 240.00
2.6.2 E IMP 3–3 192.00 240.00 288.00 240.00
2.6.3 E IMP 4–4 192.00 240.00 288.00 240.00
3.1.1 E SRE 5–5 192.00 240.00 288.00 240.00
3.1.2 E SRE 5–5 192.00 240.00 288.00 240.00
3.1.3 E SRE 5–5 192.00 240.00 288.00 240.00
3.1.4 E SRE 4–4 192.00 240.00 288.00 240.00
3.1.5 E SRE 5–5 192.00 240.00 288.00 240.00
3.2.1 E SRE 4–4 192.00 240.00 288.00 240.00
3.2.2 E SRE 4–4 192.00 240.00 288.00 240.00
3.2.3 E SRE 4–4 192.00 240.00 288.00 240.00
3.2.4 E SRE 4–4 192.00 240.00 288.00 240.00
3.2.5 E SEG 4–4 192.00 240.00 288.00 240.00
3.2.6 E SRE 5–5 192.00 240.00 288.00 240.00
3.3.1 I SEG 5–7 384.00 480.00 576.00 480.00
3.3.2 I ARQ 5–6 408.00 480.00 768.00 516.00
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
18

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
3.3.3 I ARQ 5–6 384.00 480.00 576.00 480.00
3.3.4 I ARQ 5–6 384.00 480.00 576.00 480.00
3.3.5 I ARQ 5–7 384.00 480.00 576.00 480.00
3.3.6 I ARQ 5–7 384.00 480.00 576.00 480.00
3.4.1 D DES 5–7 736.00 866.00 1082.00 880.33
3.4.2 D DES 5–7 835.00 982.00 1277.00 1006.67
3.4.3 D DES 5–7 808.00 950.00 1235.00 973.83
3.4.4 D DES 5–8 1414.00 1488.00 2158.00 1587.33
3.4.5 D DES 5–7 819.00 862.00 1250.00 919.50
3.4.6 D DES 5–7 1090.00 1282.00 1667.00 1314.17
3.4.7 D DES 5–8 797.00 886.00 1285.00 937.67
3.4.8 D DES 5–8 1316.00 1548.00 2012.00 1586.67
3.4.9 D DES 5–8 470.00 588.00 706.00 588.00
3.4.10 D DES 5–9 1027.00 1208.00 1631.00 1248.33
3.4.11 D DAT 8–8 694.00 816.00 1061.00 836.50
3.5.1 D DES 14–15 794.00 934.00 1308.00 973.00
3.5.2 D DES 14–15 857.00 1008.00 1310.00 1033.17
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
19

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
3.5.3 D DES 14–15 224.00 280.00 336.00 280.00
3.5.4 D DAT 14–15 537.00 632.00 853.00 653.00
3.6.1 I DAT 7–8 384.00 480.00 576.00 480.00
3.6.2 I DES 6–7 384.00 480.00 576.00 480.00
3.6.3 I DES 6–7 384.00 480.00 576.00 480.00
3.6.4 I DES 6–7 384.00 480.00 576.00 480.00
3.6.5 I DES 13–18 408.00 480.00 768.00 516.00
3.6.6 I DES 17–19 408.00 480.00 720.00 508.00
3.7.1 I DAT 7–9 432.00 480.00 720.00 512.00
3.7.2 I DAT 9–10 432.00 480.00 672.00 504.00
3.7.3 I DAT 11–11 432.00 480.00 672.00 504.00
3.7.4 I DAT 11–11 432.00 480.00 672.00 504.00
3.7.5 I DAT 12–12 384.00 480.00 576.00 480.00
3.8.1 V CAL 9–9 136.00 160.00 184.00 160.00
3.8.2 V CAL 9–10 272.00 320.00 368.00 320.00
3.8.3 V CAL 9–10 272.00 320.00 368.00 320.00
3.8.4 V CAL 9–10 272.00 320.00 368.00 320.00
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
20

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
3.8.5 V CAL 9–10 272.00 320.00 368.00 320.00
3.8.6 V SEG 9–10 272.00 320.00 368.00 320.00
3.8.7 V CAL 10–11 136.00 160.00 184.00 160.00
3.8.8 V SRE 9–10 272.00 320.00 368.00 320.00
3.9.1 V CAL 16–16 136.00 160.00 184.00 160.00
3.9.2 V CAL 17–17 272.00 320.00 368.00 320.00
3.9.3 V CAL 16–17 272.00 320.00 368.00 320.00
3.9.4 V CAL 16–17 272.00 320.00 368.00 320.00
3.9.5 V SEG 16–16 136.00 160.00 184.00 160.00
3.9.6 V CAL 17–17 136.00 160.00 184.00 160.00
3.9.7 V SRE 16–17 136.00 160.00 184.00 160.00
3.10.1.1 E DAT 7–9 192.00 240.00 288.00 240.00
3.10.1.2 E DAT 9–10 192.00 240.00 288.00 240.00
3.10.1.3 E DAT 9–10 192.00 240.00 288.00 240.00
3.10.1.4 E DAT 11–15 192.00 240.00 288.00 240.00
3.10.2.1 E CAL 2–3 192.00 240.00 288.00 240.00
3.10.2.2 E CAL 3–5 192.00 240.00 288.00 240.00
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
21

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
3.10.2.3 E CAL 5–10 192.00 240.00 288.00 240.00
3.10.2.4 E CAL 11–15 192.00 240.00 288.00 240.00
3.10.3.1 E DAT 3–5 192.00 240.00 288.00 240.00
3.10.3.2 E DAT 5–9 192.00 240.00 288.00 240.00
3.10.3.3 E DAT 9–10 192.00 240.00 288.00 240.00
3.10.3.4 E DAT 11–15 192.00 240.00 288.00 240.00
3.10.4.1 E IMP 13–14 192.00 240.00 288.00 240.00
3.10.4.2 E IMP 14–15 192.00 240.00 288.00 240.00
3.10.4.3 E IMP 15–17 192.00 240.00 288.00 240.00
3.10.4.4 E IMP 18–21 192.00 240.00 288.00 240.00
3.11.1 G ARQ 15–21 72.00 80.00 88.00 80.00
3.11.2 G SRE 10–20 72.00 80.00 88.00 80.00
3.11.3 G DES 4–20 72.00 80.00 88.00 80.00
3.11.4 G DES 4–20 72.00 80.00 88.00 80.00
3.11.5 G DES 6–20 72.00 80.00 88.00 80.00
4.1.1 G IMP 10–10 72.00 80.00 88.00 80.00
4.1.2 G IMP 11–11 72.00 80.00 88.00 80.00
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
22

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
4.1.3 G IMP 17–17 72.00 80.00 88.00 80.00
4.1.4 V IMP 10–11 288.00 320.00 480.00 341.33
4.2.1 A IMP 13–15 7392.00 7392.00 7392.00 7392.00
4.2.2 A IMP 16–20 5408.00 5408.00 5408.00 5408.00
4.2.3 G JP 16–16 72.00 80.00 88.00 80.00
4.3.1 A IMP 19–20 4928.00 4928.00 4928.00 4928.00
4.3.2 A IMP 21–22 2464.00 2464.00 2464.00 2464.00
4.3.3 G JP 21–21 72.00 80.00 88.00 80.00
4.3.4 G JP 20–20 72.00 80.00 88.00 80.00
5.1.1 G ARQ 2–2 72.00 80.00 88.00 80.00
5.1.2 G ARQ 2–2 72.00 80.00 88.00 80.00
5.1.3 G SRE 5–5 72.00 80.00 88.00 80.00
5.1.4 E ARQ 1–2 192.00 240.00 288.00 240.00
5.2.1 G SRE 2–2 72.00 80.00 88.00 80.00
5.2.2 G SRE 4–4 72.00 80.00 88.00 80.00
5.2.3 G ARQ 4–4 72.00 80.00 88.00 80.00
5.3.1 G SRE 4–4 72.00 80.00 88.00 80.00
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
23

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
5.3.2 G SRE 4–4 72.00 80.00 88.00 80.00
5.3.3 G SRE 4–4 72.00 80.00 88.00 80.00
5.3.4 G SRE 2–2 72.00 80.00 88.00 80.00
5.4.1 G IMP 9–12 72.00 80.00 88.00 80.00
5.4.2 G IMP 9–12 72.00 80.00 88.00 80.00
5.4.3 G JP 17–20 72.00 80.00 88.00 80.00
5.4.4 G JP 7–7 72.00 80.00 88.00 80.00
6.1.1 T RED 3–3 136.00 160.00 184.00 160.00
6.1.2 T RED 3–3 136.00 160.00 184.00 160.00
6.1.3 T RED 3–3 136.00 160.00 184.00 160.00
6.1.4 T RED 3–3 136.00 160.00 184.00 160.00
6.1.5 T RED 4–4 136.00 160.00 184.00 160.00
6.2.1 T RED 4–4 136.00 160.00 184.00 160.00
6.2.2 T RED 6–6 136.00 160.00 184.00 160.00
6.2.3 T RED 7–7 136.00 160.00 184.00 160.00
6.3.1 T RED 4–5 136.00 160.00 184.00 160.00
6.3.2 T RED 4–5 136.00 160.00 184.00 160.00
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
24

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
6.3.3 T RED 4–4 136.00 160.00 184.00 160.00
6.3.4 T RED 9–9 136.00 160.00 184.00 160.00
6.4.1 T SEG 5–5 136.00 160.00 184.00 160.00
6.4.2 T SEG 5–5 136.00 160.00 184.00 160.00
6.4.3 T SEG 5–6 136.00 160.00 184.00 160.00
6.5.1 T SRE 9–12 136.00 160.00 184.00 160.00
6.5.2 T SRE 10–12 136.00 160.00 184.00 160.00
6.5.3 T SRE 9–11 136.00 160.00 184.00 160.00
6.5.4 T SRE 8–12 272.00 320.00 368.00 320.00
6.5.5 T SRE 10–12 136.00 160.00 184.00 160.00
6.5.6 T SRE 9–12 136.00 160.00 184.00 160.00
6.6.1 T SRE 5–5 136.00 160.00 184.00 160.00
6.6.2 T RED 5–5 136.00 160.00 184.00 160.00
6.6.3 T RED 5–5 136.00 160.00 184.00 160.00
7.1.1 T IMP 10–12 136.00 160.00 184.00 160.00
7.1.2 R IMP 13–56 2534.40 2816.00 3097.60 2816.00
7.1.3 T IMP 11–20 204.00 240.00 276.00 240.00
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
25

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
7.1.4 T IMP 15–20 136.00 160.00 184.00 160.00
7.1.5 T IMP 10–18 136.00 160.00 184.00 160.00
7.1.6 T IMP 10–12 136.00 160.00 184.00 160.00
7.2.1 T IMP 10–16 136.00 160.00 184.00 160.00
7.2.2 T IMP 16–18 136.00 160.00 184.00 160.00
7.2.3 T IMP 2–6 136.00 160.00 184.00 160.00
7.2.4 T IMP 8–20 204.00 240.00 276.00 240.00
7.2.5 T IMP 13–21 136.00 160.00 184.00 160.00
7.3.1 T IMP 13–15 136.00 160.00 184.00 160.00
7.3.2 T IMP 18–18 136.00 160.00 184.00 160.00
8.1.1 C SRE 21–56 21764.20 21764.20 21764.20 21764.20
8.1.2 C SRE 21–56 38246.00 38246.00 38246.00 38246.00
8.1.3 V SRE 21–56 476.00 560.00 644.00 560.00
8.1.4 R JP 21–56 259.20 288.00 316.80 288.00
8.1.5 C SEG 13–56 32112.00 32112.00 32112.00 32112.00
8.1.6 R SRE 21–56 518.40 576.00 633.60 576.00
8.2.1 R DES 21–56 4147.20 4608.00 5068.80 4608.00
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
26

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
8.2.2 R SEG 21–56 1036.80 1152.00 1267.20 1152.00
8.2.3 R SRE 21–56 1036.80 1152.00 1267.20 1152.00
8.2.4 R DES 21–56 2073.60 2304.00 2534.40 2304.00
8.2.5 R SRE 21–56 259.20 288.00 316.80 288.00
8.2.6 R SRE 21–56 259.20 288.00 316.80 288.00
8.2.7 R SRE 21–56 777.60 864.00 950.40 864.00
8.3.1 R CAL 21–56 518.40 576.00 633.60 576.00
8.3.2 R DAT 21–56 259.20 288.00 316.80 288.00
8.3.3 G JP 21–23 72.00 80.00 88.00 80.00
8.3.4 R JP 24–56 475.20 528.00 580.80 528.00
8.3.5 G IMP 22–26 72.00 80.00 88.00 80.00
8.3.6 G IMP 24–27 72.00 80.00 88.00 80.00
8.4.1 R SRE 21–56 518.40 576.00 633.60 576.00
8.4.2 R SRE 21–56 518.40 576.00 633.60 576.00
8.4.3 R SRE 21–56 259.20 288.00 316.80 288.00
8.4.4 R JP 21–56 259.20 288.00 316.80 288.00
8.5.1 R IMP 21–56 1036.80 1152.00 1267.20 1152.00
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
27

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla3—continuación
EDT Clase Rol Meses OHH MHH PHH EHH
8.5.2 G IMP 21–27 72.00 80.00 88.00 80.00
8.5.3 R SRE 21–56 518.40 576.00 633.60 576.00
9.1.1 G DES 21–21 72.00 80.00 88.00 80.00
9.1.2 G JP 21–22 72.00 80.00 88.00 80.00
9.2.1 G JP 54–56 72.00 80.00 88.00 80.00
9.2.2 G SEG 56–56 72.00 80.00 88.00 80.00
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
28

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Se agregan explícitamente soporte puente de NOC y Mesa N1 de 4.2.2 = 9336.00 HH y
reserva F3/QA = 8× (256 + 128) = 3.072 HH. Las ocho restauraciones previas a Operación
aportan 128 HH SRE: 48 en 4.2.1, 48 en 4.2.2 y 32 en 4.3.1. Cada una supone 16 HH para
preparación,ejecución,validacióneinforme.Sondistintasdelas36restauracionesde8.1.6
durante Operación. Al activar los respaldos antes del mes 13 se verificará si RT-07.12 exige
pruebasmensualesadicionales;enesecasoseprogramarányreestimaránexpresamente,sin
imputarlasalasochoyacontadas.Lassieteconmutacionesrealesde8.1.3seestimanen80HH
porcampaña,560HHentotal.LaspruebasdeintrusiónE1yE2seestimanen320y160HH
respectivamente;lareducciónenE2exigequeelinventarioylosprocedimientosdeE1sean
reutilizables. Se confirmarán horas, alcance y disponibilidad con el tercero independiente
antes de ejecutar. Las 128 HH de restauraciones se suman a las 186.683,03 HH de los 227
paquetesparaformarlas186.811,03HHdebase;elsoportepuenteylareservaprotegidase
agreganporseparadoenlascurvassiguientes.
4.3 ResumenT-15
LaTabla 4resumelasHHprogramadasporetapayelmáximodeplazasestimadasensus
meses,segúnlacurvaconjuntadelaTabla 12.Lasetapascompartenperíodos:susmáximos
no se suman ni representan una dotación exclusiva de la etapa. La simultaneidad diaria se
asignaconelregistrodepersonasyturnosdelasección5.7.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
29

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla4 ResumenT-15.Fuente:elaboraciónapartirdelassecs.4.1–4.4deesteformularioyde(FormularioT-14,EDT).
Etapa HHbaseycobertura HHreservaprotegida HHprogramadas Frentes Meses N.°personas
(peak)*
E1Desarrollo 40865.08 0 40865.08 F1,F2,F3,F5,F6,F7 1–12 59
E1Marchablanca 11335.12 1152 12487.12 F1,F2,F3,F5,F6,F7 13–15 50
E2Desarrollo 10579.37 0 10579.37 F1,F2,F4,F5,F6,F7 13–18 57
E2Marchablanca 7452.03 0 7452.03 F1,F2,F4,F6,F7 19–20 56
E1Producciónyestabili-
zación
14816.04 1920 16736.04 F3,F5,F6,F7 16–20 57
Operación 108409.17 0 108409.17 F1,F8 21–56 41
E2Cierreyestabiliza-
ciónposterioralH12
2690.22 0 2690.22 F1,F2,F4,F6,F7 21–22 41
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
30

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Lalíneabasesuma199.219,03HH:186.683,03delos227paquetes,128derestauraciones
previasaOperación,9.336desoportepuentey3.072dereservaprotegida.Lacurvapororigen
alcanza 59 plazas en el mes 5, durante la construcción de los módulos de la Etapa 1. En el
solapamientodelosmeses13a15elmáximoesde50plazasenelmes15,yeneldelosmeses
19y20,de56.Lasplazasprovienendelcontrastemensualdelasección4.4.SegúnelAnexo
4-W.7delSD4,lamesadeayudasumaunterceragenteenlasfranjasdemenordemandasolo
en septiembre y diciembre desde el mes 25, el NOC atiende su franja de 20:00 a 22:00 y la
dedicacióndeclaradadelNOCbajaencadaañodeoperación.
Estimaciónportamañodelosmódulos. Los 15 módulos de software (3.4.1 a 3.4.11 y 3.5.1 a
3.5.4)seestimandesdesucontenido.ParacadamóduloseleenlosrequisitosdelFormulario
T-12quelocitanensucolumna«PaqueteEDT»yseidentificansuselementosdealcance:flujos
funcionales,interfacesconotrossistemas,dispositivosynecesidadesespeciales(operación
sinconexión,objetivosderendimientomedibles,seguridad,accesibilidadotiemporeal).Una
funcionalidadqueelT-12vinculaavariosmódulossecuentaunasolavez,enelmóduloquela
implementa;enlosdemásesunpuntodeintegracióninternaynosumaesfuerzo.
Cada flujo se clasifica por complejidad: S, consulta o registro sin reglas; M, registro con
validaciones, estados o notificaciones; y C, cálculo, optimización, conciliación o motor de
reglas.Elesfuerzomásprobabledecadaelementousaestastasas:flujoS,24HH;flujoM,48
HH;flujoC,96HH;interfazexternaconcontrato,adaptador,cola,reintentoeidempotencia,
64 HH; dispositivo integrado y probado con el equipo real, 64 HH; operación sin conexión
con cola local, sincronización y descarte de duplicados, 120 HH; objetivo de rendimiento
medible,24HH;yotranecesidadespecial,48HH.Sonsupuestosdeplanificaciónporjuiciode
ingenieríadelequipo,norendimientosmedidos;secontrastanconlasHHregistradasencada
iteración.
Elesfuerzomásprobabledelmódulosumacincoactividades:análisisydiseñoespecífico
(8HHporflujoy8HHporinterfazodispositivo);construcción(lasumadeloselementos);
pruebas unitarias y de contrato (25% de la construcción, para la cobertura mínima del RT-
04.11);integraciónyentregaenQA(40HHmás16HHporinterfazodispositivo);yrevisióny
demostracióndeiteraciones(12HHporcadaiteracióndedossemanasdelaTabla 20).Las
pruebasampliadasdelascuentas3.8y3.9certificanelconjuntoynosecuentandentrodel
módulo.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
31

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla5 Tamañoyesfuerzodelosmódulos(HH).Fuente:requisitosdelFormularioT-12porpaqueteEDTytasasdeestasección.
Paque-
te
Req.
T-12
Flujos
S/M/C
Interf.
ydisp.
Sin
conexión
/rend.
/otras
Dise-
ño
Constr. Prue-
bas
Integr.
QA
Iterac. O M P E
3.4.1 12 1/5/0 2 1/1/0 64 536 134 72 60 736 866 1.082 880,33
3.4.2 14 3/6/2 1 0/0/0 96 616 154 56 60 835 982 1.277 1.006,67
3.4.3 14 1/5/1 1 1/1/1 64 616 154 56 60 808 950 1.235 973,83
3.4.4 18 1/4/5 3 0/1/1 104 960 240 88 96 1.414 1.488 2.158 1.587,33
3.4.5 9 1/5/0 3 0/0/1 72 504 126 88 72 819 862 1.250 919,50
3.4.6 22 1/8/2 1 1/3/0 96 856 214 56 60 1.090 1.282 1.667 1.314,17
3.4.7 9 2/3/2 2 0/1/0 72 536 134 72 72 797 886 1.285 937,67
3.4.8 18 3/8/2 3 1/0/1 128 1008 252 88 72 1.316 1.548 2.012 1.586,67
3.4.9 8 3/3/0 1 0/1/0 56 304 76 56 96 470 588 706 588
3.4.10 11 1/5/3 2 0/1/1 88 752 188 72 108 1.027 1.208 1.631 1.248,33
3.4.11 12 0/4/2 1 0/2/1 56 544 136 56 24 694 816 1.061 836,50
3.5.1 13 2/8/0 2 0/1/0 96 584 146 72 36 794 934 1.308 973
3.5.2 16 2/4/2 2 0/0/2 80 656 164 72 36 857 1.008 1.310 1.033,17
3.5.3 3 2/1/0 0 0/0/1 24 144 36 40 36 224 280 336 280
3.5.4 5 0/1/3 1 0/0/0 40 400 100 56 36 537 632 853 653
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
32

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla5—continuación
Paque-
te
Req.
T-12
Flujos
S/M/C
Interf.
ydisp.
Sin
conexión
/rend.
/otras
Dise-
ño
Constr. Prue-
bas
Integr.
QA
Iterac. O M P E
Total 12.418 14.330 19.171 14.818,17
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
33

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
El optimista y el pesimista de cada módulo se fundan en condiciones propias, no en un
porcentajecomún:eloptimistareflejalareutilizacióndisponibleyelpesimista,ladificultad
concretadelmódulo.Elvaloresperadoes (𝑂 + 4𝑀 + 𝑃)/6.
Tabla6 Fundamentodeloptimistaydelpesimistadecadamódulo.Fuente:elaboraciónpropiaapartirdelaficha
decadamódulo.
Paquete O/M Quépermiteeloptimista P/M Quéincluyeelpesimista
3.4.1 0,85 Reutilizaidentidad,auditoríaysin-
cronizacióndelabasecompartida
(3.3)
1,25 VariantesdeetiquetasGS1de
proveedoresyajustesconlaimpre-
soraenelpiloto
3.4.2 0,85 Reutilizaelmodelodeproducto,
loteyubicacióndeM1ydelabase
compartida
1,30 Calibracióndelslottingydela
reposicióncondatosrealesde
rotación
3.4.3 0,85 ReutilizalecturaGS1ycolalocal
deM1
1,30 Repeticióndepruebasencámara
conguantesyconpreparadores
nuevos
3.4.4 0,95 Pocareutilización:reglastérmicas
ydispositivossonpropiosdel
módulo
1,45 Homologacióndesensoresyrepe-
ticióndeensayosdeexcursióny
sinredenelbanco2.4.3
3.4.5 0,95 Pocareutilización:canalesde
comunicaciónpropiosdelcamión
1,45 Coberturavariableenrutayajus-
tesdelosdoscaminosduranteel
piloto4.1.4
3.4.6 0,85 Reutilizalacolalocalylasincroni-
zacióndelabasecompartida
1,30 Conflictosdereservaalsincronizar
yreglascomercialesporvalidar
conComercial
3.4.7 0,90 Elmotorderuteoesuncomponen-
teexistentequeseconfigura
1,45 Calibraciónderestriccionescon
elplanificadoryvalidaciónsinél
(R18-16)
3.4.8 0,85 Reutilizalacolalocalylaidentidad
delabasecompartida
1,30 Pruebasdecampoconimpresoras
yfirmaelectrónicaenrutassin
señal
3.4.9 0,80 Reutilizalaaplicaciónylasincroni-
zacióndereparto(M6)
1,20 Variedaddeenvasesydestinospor
validarconLogística
3.4.10 0,85 Reutilizalaaplicaciónderepartoy
lacoladesincronización
1,35 Certificacióndelterminaldepago
yconciliaciónconFinanzas
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
34

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla6—continuación
Paquete O/M Quépermiteeloptimista P/M Quéincluyeelpesimista
3.4.11 0,85 Reutilizaelmodelodedatosdelos
módulosdeoperación
1,30 Definicionesdeindicadorespor
validarconGerenciaydatosin-
completosalinicio
3.5.1 0,85 Reutilizalavalidacióndepedidosy
lacoladeintegracióndelaEtapa1
1,40 Diferenciasentreperfilesdemen-
sajesdecadacadenaycertifica-
ción(3.6.5)
3.5.2 0,85 Reutilizaelvalidadordecréditoy
stockdepreventa
1,30 Certificaciónconlaplataformade
pagosypruebasdeaccesibilidad
3.5.3 0,80 Reutilizalaautenticacióndel
portaldeclientes
1,20 Ajustedepermisosconcadatrans-
portista
3.5.4 0,85 Reutilizalacapaanalíticadela
Etapa1
1,35 Validacióndelmodelodeimpu-
taciónconFinanzas
Los15módulossuman14.818,17HHesperadas,frentealas15.360HHdelaestimación
anterior por clases. La diferencia proviene de módulos con contenido distinto: el reparto
(3.4.8)ylacalidadconfríoencámaras(3.4.4)superanlas1.580HH,mientrasqueelportalde
transportistas,contresrequisitos,quedaen280HH.Eldetalledeelementosdecadamódulo,
consusrequisitosdelT-12,estáenlaTabla 7.
Tabla7 Elementosdealcancedecadamódulo.Fuente:FormularioT-12,columnaPaqueteEDT;tasasMdeesta
sección.
Paquete Elementodealcance RequisitosT-12 Tipo M(HH)
3.4.1M1 RecepcióncontraOCconalertapordis-
crepancia
RF-01.01 FlujoM 48
CapturadeloteyvencimientoporGS1 RF-01.02,RF-01.03,
RF-01.06
FlujoM 48
Noconformidadconfotografíaycuarente-
na
RF-01.04,RF-01.05 FlujoM 48
GeneracióndeSSCCyetiquetaGS1-128 RF-01.07 FlujoM 48
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
35

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla7—continuación
Paquete Elementodealcance RequisitosT-12 Tipo M(HH)
UbicacióndelSSCCconvalidacióntérmi-
ca
RF-01.08 FlujoS 24
Maestrodeproductos RF-01.10 FlujoM 48
IngresodeinventarioalERPconcolay
reintento
RF-01.09 Interfaz 64
Impresoradeetiquetas RF-01.07 Dispositivo 64
Operaciónsinconexiónenbodega RT-17.01 Sinconexión 120
Registrodeítemdentrodeltiempoexigi-
do
RNF-01.01 Rendimiento 24
3.4.2M2 Instalaciones,zonasyubicaciones RF-02.01 FlujoM 48
Stockconsolidadoydisponibleparaventa RF-02.02,RF-02.05 FlujoM 48
PropuestadeslottingporrotaciónABC RF-02.03 FlujoC 96
Conteocíclicoyajuste RF-02.04 FlujoM 48
Inventarioentránsitoentresitios RF-02.06 FlujoM 48
Ocupaciónporzona RF-02.07 FlujoS 24
ControlFEFOyalertasdevencimiento RF-02.09 FlujoM 48
Lecturasencross-docking RF-02.11 FlujoM 48
Validacióntérmicaenreubicación RF-01.11 FlujoS 24
Mermasporvencimiento RF-08.05 FlujoS 24
Reposiciónsugeridaconpromociones RF-10.01,RF-10.02 FlujoC 96
Traspasodereposiciónytransferenciasal
ERP
RF-10.03,RF-02.06 Interfaz 64
3.4.3M5 Generacióndemisionesporturno RF-05.01 FlujoM 48
Pickingdirigidoconsecuenciaseco,
refrigerado,congelado
RF-02.08,RF-05.04 FlujoC 96
Validaciónporescaneoyregistrodelote RF-05.02,RF-09.08 FlujoM 48
Faltantesconmotivo RF-05.03 FlujoS 24
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
36

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla7—continuación
Paquete Elementodealcance RequisitosT-12 Tipo M(HH)
AsignaciónFEFO RF-05.05 FlujoM 48
Cargaensecuenciainversaalaruta RF-05.07 FlujoM 48
Tiempofueradefríoenandén RF-09.11 FlujoM 48
CierredemisiónalERP RF-05.06 Interfaz 64
Operaciónsincoberturaencámara RNF-09.04,RT-17.01 Sinconexión 120
Confirmacióndelíneaen1segundo RNF-05.01 Rendimiento 24
Interfazoperableconguantesa−22°C RNF-05.02 Necesidad
especial
48
3.4.4M9 Ciclodevidadellote RF-02.10 FlujoC 96
Trazabilidadhaciaadelanteyhaciaatrás RF-09.01,RF-09.02 FlujoC 96
Registrocontinuodetemperaturaen
cámaras
RF-09.03,RNF-09.05 FlujoM 48
Motordeexcursióntérmicaparametriza-
bleyalertas
RF-09.05,RF-09.10 FlujoC 96
Bloqueopreventivodellote RF-09.06 FlujoM 48
Rechazoporsospechaderupturadefrío RF-09.07 FlujoS 24
Evidenciadecumplimientodecadenade
frío
RF-09.09 FlujoM 48
HabilitacióndebajadadeSSCCporlatido
ymanifiesto
RF-09.12 FlujoC 96
Retenciónenelterminalsinred RF-09.13,RNF-09.06 FlujoC 96
Disposicióndelproductoretenido RF-09.14 FlujoM 48
Sensoresygatewaysdecámara RF-09.03 Dispositivo 64
Termógrafocertificadoysimuladoresde
producto
RNF-09.08 Dispositivo 64
Publicaciónalacapaanalítica RT-05.29 Interfaz 64
Coherenciasinpérdidasniduplicadosen
datosdesensores
RNF-09.09 Necesidad
especial
48
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
37

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla7—continuación
Paquete Elementodealcance RequisitosT-12 Tipo M(HH)
Clientesafectadosporloteenmenosde2
horas
RNF-09.01 Rendimiento 24
3.4.5
M12
Registrodetemperaturaencamiones RF-09.04 FlujoM 48
Rutaplanificadafrentearecorrida RF-14.02 FlujoM 48
Alertapordesvíoderuta RF-14.03 FlujoM 48
Envíodekilómetrosytiemposacostode
servir
RF-14.04 FlujoS 24
Vínculoconductor,camiónyviaje RF-14.05 FlujoM 48
Geocercas RF-14.06 FlujoM 48
Gatewaysdecamiónytelemetríadel
tercero
RF-09.04 Dispositivo 64
DoblecaminomóvileIridiumSBD RNF-09.07 Dispositivo 64
Administraciónremotadedispositivos RT-03.18 Interfaz 64
Ingestaentiemporealconcoherenciade
secuencia
RNF-09.09 Necesidad
especial
48
3.4.6M3 Stockconysinconexión RF-03.01,RF-03.02 FlujoM 48
Reservadestockporordendellegadaal
servidor
RF-03.03 FlujoC 96
Créditoydeudaconysinconexión RF-03.04,RF-03.05 FlujoM 48
Historialdecompra RF-03.06 FlujoS 24
Promociones RF-03.07 FlujoM 48
Alerta,bloqueodecréditoyautorización
desupervisor
RF-03.08,RF-03.09,
RF-03.10,RF-07.05
FlujoM 48
Precioacordadoyalertadediscrepancia RF-03.11,RF-03.12 FlujoM 48
Fechayventanadeentregacomprometi-
ble
RF-03.13 FlujoC 96
Sugerenciadeproductos RF-03.14 FlujoM 48
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
38

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla7—continuación
Paquete Elementodealcance RequisitosT-12 Tipo M(HH)
Identificadorúnicoydescartededuplica-
dos
RF-03.15,RF-03.16 FlujoM 48
Cobranzaenefectivodelpreventista RF-07.11 FlujoM 48
Pedido,créditoydeudaconelERP RF-03.04 Interfaz 64
Preventasinconexión RT-17.01 Sinconexión 120
Registrodelíneaen1,5s RNF-03.01 Rendimiento 24
Consultadestockycréditoen2s RNF-03.02 Rendimiento 24
Consultadehistorialen2s RNF-03.03 Rendimiento 24
3.4.7M4 Asignaciónysecuenciaciónporcapacidad
yzona
RF-04.01 FlujoC 96
Ediciónmanualdesecuenciayreasigna-
ción
RF-04.02 FlujoM 48
Bloqueoporpesoyvolumen RF-04.03 FlujoS 24
Ventanashorariasdelclienteenlasecuen-
cia
RF-04.04,RF-04.07 FlujoC 96
Restriccióndepedidosdefríoacamiones
conequipo
RF-04.05 FlujoS 24
Avisodellegadaconventanade30minu-
tos
RF-04.06 FlujoM 48
Planificacióndelaventanadelcanal
moderno
RF-12.10 FlujoM 48
Motorderuteo RF-04.01 Interfaz 64
Notificaciónalcontactodelcliente RF-04.06 Interfaz 64
Rutasdeldíaenmenosde20minutos RNF-04.01 Rendimiento 24
3.4.8M6 Recepciónconformeporlíneaoguía RF-06.01 FlujoM 48
Firmaofotografíacomoevidenciade
entrega
RF-06.02,RF-06.12,
RF-12.12
FlujoM 48
Rechazototaloparcial RF-06.03 FlujoM 48
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
39

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla7—continuación
Paquete Elementodealcance RequisitosT-12 Tipo M(HH)
Localcerrado RF-06.04 FlujoS 24
Horadellegadaytérmino RF-06.06 FlujoS 24
Sincronizacióncompletadelturno RF-06.07 FlujoC 96
IniciodejornadaconOTPparaconducto-
resexternos
RF-06.08 FlujoM 48
ConfirmaciónporQR RF-06.11 FlujoM 48
ComprobantetérmicoporBluetooth RF-06.13 FlujoM 48
EvidenciayacuseconelERP RF-06.14 FlujoM 48
Acusedigitalalcanalmoderno RF-12.13 FlujoM 48
Cumplimientodelaventanade30minu-
tos
RF-12.11 FlujoS 24
FirmaelectrónicaconformealaLey
19.799
RF-18.01 FlujoC 96
Evidenciadeentregayacusetributario
conelERP
RF-06.14 Interfaz 64
ImpresoraportátilBluetooth RF-06.13 Dispositivo 64
Enlacelocalconelgatewaydelcamión RF-09.13 Dispositivo 64
Repartosinconexión RT-17.01 Sinconexión 120
Documentoscifradosconverificaciónde
integridad
RT-16.16 Necesidad
especial
48
3.4.9M8 Envasesdevueltosenlaentrega RF-06.09 FlujoS 24
Cuentacorrientedeenvasesyparque
retornable
RF-06.10,RF-08.03 FlujoM 48
Devoluciónenlaentregasinconexión RF-08.01 FlujoM 48
Destinodeladevoluciónenandén RF-08.02 FlujoM 48
Alertaporumbraldeenvases RF-08.04 FlujoS 24
Reportedepérdidadeenvases RF-08.06 FlujoS 24
DevolucionesalERP RF-08.02 Interfaz 64
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
40

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla7—continuación
Paquete Elementodealcance RequisitosT-12 Tipo M(HH)
Registroenandénen30sporítem RNF-08.01 Rendimiento 24
3.4.10
M7
Montoenefectivorecaudado RF-06.05 FlujoS 24
Montoesperadoderendiciónporcamión RF-07.01 FlujoM 48
Planilladigitalderendición RF-07.02 FlujoC 96
Causalesdediferenciaconbloqueo RF-07.03 FlujoM 48
Consoladecarteradecréditoa30días RF-07.04 FlujoC 96
Cobrocontarjetaenruta RF-07.06 FlujoM 48
Bandejadevalidacióndepagosdelportal RF-07.08 FlujoM 48
Anticiposypagosparciales RF-07.10 FlujoM 48
Liquidaciónycierrecomercialporca-
mión
RF-11.07 FlujoC 96
Recaudaciónidempotentehaciacuentas
porcobrardelERP
RF-07.09 Interfaz 64
TerminaldepagoporBluetooth RF-07.06 Dispositivo 64
Sincronizacióndecobranzasen10minu-
tos
RNF-07.01 Rendimiento 24
Controlesdeseguridaddelmediodepago RF-07.06 Necesidad
especial
48
3.4.11
M10
IndicadorOTIF RF-11.03 FlujoC 96
Fillrateypedidoperfecto RF-11.04 FlujoM 48
Utilizacióndecapacidadporviaje RF-11.05 FlujoM 48
Tablerooperacionalentiemporeal RF-11.06 FlujoC 96
Reportesejecutivosprogramadosyexpor-
tables
RF-11.01,RT-05.28 FlujoM 48
Filtrosydetallehastalatransacción RT-05.26 FlujoM 48
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
41

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla7—continuación
Paquete Elementodealcance RequisitosT-12 Tipo M(HH)
Ingestadesdelabasetransaccional RT-05.25,RT-05.29 Interfaz 64
Indicadoresdeldíaen5minutos RNF-11.01 Rendimiento 24
Indicadoresdegestióndentrodesulaten-
cia
RNF-11.04 Rendimiento 24
Aislamientoentreanalíticaytransaccio-
nes
RNF-11.02 Necesidad
especial
48
3.5.1
M11
Recepcióndelpedidoelectrónico RF-12.01 FlujoM 48
Validacióndelpedido RF-12.02 FlujoM 48
Equivalenciasdeproductoporcadena RF-12.03 FlujoM 48
RegistroautomáticoenelERP RF-12.04 FlujoM 48
Pedidodisponiblepararutas RF-12.05 FlujoS 24
Bandejadeexcepciones RF-12.06 FlujoM 48
Confirmaciónorechazoalacadena RF-12.07 FlujoM 48
Historialdeestadosdelpedido RF-12.08 FlujoS 24
Avisodedespacho(ASN) RF-12.09 FlujoM 48
Portaldeproveedoresdesololectura RF-12.22,RF-12.23,
RF-12.24
FlujoM 48
Mensajeríaconlascadenas RF-12.01,RF-12.07,
RF-12.09
Interfaz 64
PedidosalERP RF-12.04 Interfaz 64
Acusealacadenadentrode30minutos RNF-12.03 Rendimiento 24
3.5.2
M11
Portalpúblicoconcatálogo RF-12.14,RF-17.13,
RT-16.31
FlujoM 48
Pedidoenautoservicioconcréditoystock RF-12.15 FlujoC 96
Estadodeentregas RF-12.16 FlujoS 24
Documentostributariosdescargables RF-12.17 FlujoM 48
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
42

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla7—continuación
Paquete Elementodealcance RequisitosT-12 Tipo M(HH)
Saldo,estadodecuentaycartola RF-12.18,RF-07.07 FlujoM 48
Registro,autenticaciónyrecuperaciónde
acceso
RF-12.25aRF-12.29,
RT-12.12
FlujoC 96
PagoenTransbank RF-12.30 FlujoM 48
Medicióndelaautoatención RT-16.32,RT-16.33 FlujoS 24
SaldoydocumentosdesdeelERP RF-12.17,RF-12.18 Interfaz 64
Plataformadepagos RF-12.30 Interfaz 64
Diseñoresponsivoyparaequiposdebajo
costo
RT-13.02,RT-17.08 Necesidad
especial
48
Seguridaddecuentasdeusuariosexter-
nos
RT-12.12 Necesidad
especial
48
3.5.3
M11
Rutasasignadasdeldíasiguiente RF-12.19 FlujoS 24
Documentacióndedespachoporruta RF-12.20 FlujoS 24
Confirmacióndeconductoryvehículo RF-12.21 FlujoM 48
Segregaciónporempresa RF-12.19 Necesidad
especial
48
3.5.4
M10
Costodecadaentrega RF-04.08 FlujoC 96
Costodedevolucionesymermaspor
cliente
RF-08.07 FlujoM 48
Costodeservirrealporentregaycliente RF-11.02,RF-14.04 FlujoC 96
Segmentaciónporrentabilidad RF-11.08 FlujoC 96
CostosdirectosdesdeelERP RF-11.02 Interfaz 64
RangosdelPERTportipodepaquete. Losdemáspaquetesconentregableconservanelesfuerzo
desuclase,porquesucontenidosíeshomogéneodentrodecadatipo;loquecambiaessu
incertidumbre.Cadatipotieneunrangopropio,fundadoenloquehacevariarsuesfuerzo,
comomuestralaTabla 8.Paraestostiposelrangoessimétricoyelvaloresperadocoincide
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
43

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
conelmásprobable.
Tabla8 RangosdelPERTportipodepaquete.Fuente:elaboraciónpropia;clasesdelaTabladesupuestos.
Clase O/M P/M Fundamentodelrango
G 0,90 1,10 ActaoinformeconformatoycontenidofijadosenelT-14;varíaelnúmero
derondasderevisión.
E 0,80 1,20 DiseñooconfiguraciónquedependededecisionesdelCLIENTEydela
arquitecturaaprobada.
I 0,80 1,20 Interfazomigraciónconcontraparteconocidaydocumentada;loscasos
sindocumentacióntienenrangopropio.
V 0,85 1,15 Casosyciclosfijadosenelplandepruebas;unarepeticiónadicionalusala
reservaprotegidade3.072HH.
T 0,85 1,15 CantidadesdelT-11ysesionesdelplandecapacitación;varíaelaccesoa
lossitios.
R 0,90 1,10 Frecuenciafijadaporcontrato;varíaladuracióndecadaocurrencia.
AyC 1,00 1,00 Coberturaporpuestosycalendario;nosereduceporunescenarioopti-
mista.
D — — Módulos:rangopropiodecadauno(TabladefundamentosdeOyP).
Lospaquetesconunriesgoidentificadoenelcasotienenunpesimistamayory,poreso,
unvaloresperadosuperioralmásprobable.Lalíneabaseprogramaesevaloresperado.
Tabla9 Paquetesconrangopropioporriesgoidentificado.Fuente:elaboraciónpropiaapartirdelcasoydelT-14.
Paquete O/M P/M Fundamento
3.3.2 0,85 1,60 InterfacesdelERPsindocumentación(Caso,sección17.5):elpesimis-
taincluyeunsegundociclodeanálisisconmuestrasydepruebas.
3.6.5 0,85 1,60 Negociaciónycertificaciónconlaprincipalcadena,queelcaso
adviertequenoesdedossemanas.
3.6.6 0,85 1,50 Perfilesdemensajesdistintosencadacadenarestante.
3.7.1 0,90 1,50 Calidaddedatosdesconocida:el41%delasrecepcionesdelretirode
marzonoteníaloteregistrado.
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
44

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla9—continuación
Paquete O/M P/M Fundamento
3.7.2a3.7.4 0,90 1,40 Repeticióndecargasyconciliaciónsobredatosyaperfilados.
2.4.3 0,90 1,50 Bancodefrío:homologacióndesensoresyrepeticióndeensayosde
excursión.
4.1.4 0,90 1,50 Pilotodefríoencuatrocamionesconcoberturavariableenruta.
Conciliaciónconlalíneabaseanterior. LaTabla 10muestralos26paquetescuyasHHcambian.
Lalíneabasepasade220.023a199.219,03HH.Lascurvasmensuales,lareddelasección5y
ladotacióndelasección5.7secalcularonconlasHHvigentes.
Tabla10 ConciliacióndelasHHquecambian.Fuente:Tabladehorasporpaqueteanterioryvigente.
Paquete HHan-
teriores
HHvigentes Diferencia Explicación
2.4.3 320 341,33 21,33 Rangoporriesgoidentificado
3.3.2 480 516 36 Rangoporriesgoidentificado
3.4.1 960 880,33 -79,67 Estimaciónportamaño
3.4.2 960 1.006,67 46,67 Estimaciónportamaño
3.4.3 960 973,83 13,83 Estimaciónportamaño
3.4.4 1.440 1.587,33 147,33 Estimaciónportamaño
3.4.5 1.440 919,50 -520,50 Estimaciónportamaño
3.4.6 960 1.314,17 354,17 Estimaciónportamaño
3.4.7 960 937,67 -22,33 Estimaciónportamaño
3.4.8 960 1.586,67 626,67 Estimaciónportamaño
3.4.9 960 588 -372 Estimaciónportamaño
3.4.10 960 1.248,33 288,33 Estimaciónportamaño
3.4.11 960 836,50 -123,50 Estimaciónportamaño
3.5.1 960 973 13 Estimaciónportamaño
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
45

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla10—continuación
Paquete HHan-
teriores
HHvigentes Diferencia Explicación
3.5.2 960 1.033,17 73,17 Estimaciónportamaño
3.5.3 960 280 -680 Estimaciónportamaño
3.5.4 960 653 -307 Estimaciónportamaño
3.6.5 480 516 36 Rangoporriesgoidentificado
3.6.6 480 508 28 Rangoporriesgoidentificado
3.7.1 480 512 32 Rangoporriesgoidentificado
3.7.2 480 504 24 Rangoporriesgoidentificado
3.7.3 480 504 24 Rangoporriesgoidentificado
3.7.4 480 504 24 Rangoporriesgoidentificado
4.1.4 320 341,33 21,33 Rangoporriesgoidentificado
8.1.1 26.280 21.764,20 -4.515,80 DotacióndeoperacióndelSD4,Anexo4-W.7
8.1.2 54.239 38.246 -15.993 DotacióndeoperacióndelSD4,Anexo4-W.7
Total 99.879 79.075,03 -20.803,97 Lalíneabasepasade220.023a199.219,03HH
Paravalidarlastasasseregistranencadaiteraciónelelementoterminado,lasHHefectivas
ylasHHdereproceso,separandoesperasexternas.Larevisiónquincenalcomparaelementos
de igual tipo y complejidad, y contrasta el tiempo observado con la tasa usada. Dirección
actualiza las estimaciones de los módulos siguientes y verifica su efecto en precedencias,
capacidadycosteoantesdeaprobaruncambiodelíneabase.
4.4 Curvasmensuales:horasporetapayplazaspororigen
AmbascurvasusanelmismorepartomensualdelasHH:ladehorasloagrupaporetapa
yladeplazascontrastalademandadecadarolylaagrupapororigendeladotacióntécnica
del SD1. La sección 6.3 asigna cada perfil a uno de los siete grupos del SD1 o, en el caso de
losasistentesdeterreno,alacontrataciónporobraofaena;lacolumnaImplantaciónreúne
ambos.
LaTabla 11presentacurvamensualdehorasporetapa.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
46

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla11 Curvamensualdehorasporetapa.Fuente:elaboraciónapartirdelasección4.4deesteformulario.
Mes E1desarrollo E1MB E2desarrollo E2MB E1producción
yestabiliza-
ción
Operación E2cierrey
estabilización
posterioral
H12
TotalHH
1 1258.67 0.00 0.00 0.00 0.00 0.00 0.00 1258.67
2 3258.67 0.00 0.00 0.00 0.00 0.00 0.00 3258.67
3 2790.00 0.00 0.00 0.00 0.00 0.00 0.00 2790.00
4 3351.41 0.00 0.00 0.00 0.00 0.00 0.00 3351.41
5 7120.16 0.00 0.00 0.00 0.00 0.00 0.00 7120.16
6 5610.83 0.00 0.00 0.00 0.00 0.00 0.00 5610.83
7 5331.50 0.00 0.00 0.00 0.00 0.00 0.00 5331.50
8 3112.29 0.00 0.00 0.00 0.00 0.00 0.00 3112.29
9 2926.21 0.00 0.00 0.00 0.00 0.00 0.00 2926.21
10 2649.78 0.00 0.00 0.00 0.00 0.00 0.00 2649.78
11 2183.78 0.00 0.00 0.00 0.00 0.00 0.00 2183.78
12 1271.78 0.00 0.00 0.00 0.00 0.00 0.00 1271.78
13 0.00 4050.64 812.92 0.00 0.00 0.00 0.00 4863.56
14 0.00 4194.72 1746.42 0.00 0.00 0.00 0.00 5941.14
15 0.00 4241.76 1753.48 0.00 0.00 0.00 0.00 5995.24
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
47

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla11—continuación
Mes E1desarrollo E1MB E2desarrollo E2MB E1producción
yestabiliza-
ción
Operación E2cierrey
estabilización
posterioral
H12
TotalHH
16 0.00 0.00 2357.72 0.00 4498.93 0.00 0.00 6856.65
17 0.00 0.00 2307.52 0.00 3634.61 0.00 0.00 5942.13
18 0.00 0.00 1601.31 0.00 2800.82 0.00 0.00 4402.13
19 0.00 0.00 0.00 3793.80 2796.22 0.00 0.00 6590.02
20 0.00 0.00 0.00 3658.23 3005.46 0.00 0.00 6663.69
21 0.00 0.00 0.00 0.00 0.00 3341.50 1342.09 4683.59
22 0.00 0.00 0.00 0.00 0.00 3115.59 1348.13 4463.72
23 0.00 0.00 0.00 0.00 0.00 3413.05 0.00 3413.05
24 0.00 0.00 0.00 0.00 0.00 3185.28 0.00 3185.28
25 0.00 0.00 0.00 0.00 0.00 2924.58 0.00 2924.58
26 0.00 0.00 0.00 0.00 0.00 3185.28 0.00 3185.28
27 0.00 0.00 0.00 0.00 0.00 3043.48 0.00 3043.48
28 0.00 0.00 0.00 0.00 0.00 3137.86 0.00 3137.86
29 0.00 0.00 0.00 0.00 0.00 3050.96 0.00 3050.96
30 0.00 0.00 0.00 0.00 0.00 3098.96 0.00 3098.96
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
48

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla11—continuación
Mes E1desarrollo E1MB E2desarrollo E2MB E1producción
yestabiliza-
ción
Operación E2cierrey
estabilización
posterioral
H12
TotalHH
31 0.00 0.00 0.00 0.00 0.00 3137.86 0.00 3137.86
32 0.00 0.00 0.00 0.00 0.00 3657.06 0.00 3657.06
33 0.00 0.00 0.00 0.00 0.00 3015.86 0.00 3015.86
34 0.00 0.00 0.00 0.00 0.00 2870.96 0.00 2870.96
35 0.00 0.00 0.00 0.00 0.00 3578.96 0.00 3578.96
36 0.00 0.00 0.00 0.00 0.00 2951.86 0.00 2951.86
37 0.00 0.00 0.00 0.00 0.00 2709.16 0.00 2709.16
38 0.00 0.00 0.00 0.00 0.00 2912.96 0.00 2912.96
39 0.00 0.00 0.00 0.00 0.00 2870.96 0.00 2870.96
40 0.00 0.00 0.00 0.00 0.00 2951.86 0.00 2951.86
41 0.00 0.00 0.00 0.00 0.00 2832.06 0.00 2832.06
42 0.00 0.00 0.00 0.00 0.00 2951.86 0.00 2951.86
43 0.00 0.00 0.00 0.00 0.00 2951.86 0.00 2951.86
44 0.00 0.00 0.00 0.00 0.00 3477.06 0.00 3477.06
45 0.00 0.00 0.00 0.00 0.00 2829.86 0.00 2829.86
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
49

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla11—continuación
Mes E1desarrollo E1MB E2desarrollo E2MB E1producción
yestabiliza-
ción
Operación E2cierrey
estabilización
posterioral
H12
TotalHH
46 0.00 0.00 0.00 0.00 0.00 2690.96 0.00 2690.96
47 0.00 0.00 0.00 0.00 0.00 3392.96 0.00 3392.96
48 0.00 0.00 0.00 0.00 0.00 2765.86 0.00 2765.86
49 0.00 0.00 0.00 0.00 0.00 2541.16 0.00 2541.16
50 0.00 0.00 0.00 0.00 0.00 2726.96 0.00 2726.96
51 0.00 0.00 0.00 0.00 0.00 2690.96 0.00 2690.96
52 0.00 0.00 0.00 0.00 0.00 2765.86 0.00 2765.86
53 0.00 0.00 0.00 0.00 0.00 2652.06 0.00 2652.06
54 0.00 0.00 0.00 0.00 0.00 2792.52 0.00 2792.52
55 0.00 0.00 0.00 0.00 0.00 2753.62 0.00 2753.62
56 0.00 0.00 0.00 0.00 0.00 3439.51 0.00 3439.51
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
50

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
LaTabla 12presentalasplazasmensualesestimadasporgrupodeorigen.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
51

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla12 Demandamensualdeplazasporgrupodeorigen.Fuente:elaboraciónapartirdelaEDTdelT-14,lasHHdeesteformularioyladotacióndelSD1,
Tabla1.3.
Mes Desarrollo Arq.eintegra-
ción
NOCyredes SREynube Calidad Seguridad Implantación Plazastotales
1 5 2 0 2 0 2 1 12
2 4 9 0 5 3 5 3 29
3 2 3 5 7 2 3 3 25
4 2 4 5 12 1 3 3 30
5 26 10 4 12 1 5 1 59
6 32 9 2 0 1 3 1 48
7 32 7 2 0 1 2 0 44
8 13 11 0 1 1 1 1 28
9 4 8 2 3 7 2 1 27
10 2 5 0 4 6 2 4 23
11 2 9 0 3 2 1 4 21
12 2 5 0 3 1 1 2 14
13 4 6 2 1 2 4 22 41
14 13 4 2 1 2 4 23 49
15 14 4 2 1 2 4 23 50
16 5 1 17 1 5 6 22 57
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
52

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla12—continuación
Mes Desarrollo Arq.eintegra-
ción
NOCyredes SREynube Calidad Seguridad Implantación Plazastotales
17 6 1 16 1 8 4 14 50
18 6 1 17 1 2 4 8 39
19 5 1 17 1 2 4 26 56
20 4 1 18 1 2 4 26 56
21 4 1 17 2 1 5 11 41
22 3 1 16 2 1 5 12 40
23 3 1 18 2 1 5 1 31
24 3 1 16 2 1 5 2 30
25 3 1 15 2 1 4 2 28
26 3 1 16 2 1 5 2 30
27 3 1 16 2 1 5 1 29
28 3 1 16 2 1 5 1 29
29 3 1 16 2 1 5 1 29
30 3 1 16 2 1 5 1 29
31 3 1 16 2 1 5 1 29
32 3 1 21 2 1 5 1 34
33 3 1 16 2 1 5 1 29
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
53

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla12—continuación
Mes Desarrollo Arq.eintegra-
ción
NOCyredes SREynube Calidad Seguridad Implantación Plazastotales
34 3 1 14 2 1 5 1 27
35 3 1 20 2 1 5 1 33
36 3 1 15 2 1 5 1 28
37 3 1 13 2 1 4 1 25
38 3 1 15 2 1 5 1 28
39 3 1 14 2 1 5 1 27
40 3 1 15 2 1 5 1 28
41 3 1 14 2 1 5 1 27
42 3 1 15 2 1 5 1 28
43 3 1 15 2 1 5 1 28
44 3 1 19 2 1 5 1 32
45 3 1 14 2 1 5 1 27
46 3 1 13 2 1 5 1 26
47 3 1 18 2 1 5 1 31
48 3 1 14 2 1 5 1 27
49 3 1 12 2 1 4 1 24
50 3 1 13 2 1 5 1 26
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
54

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla12—continuación
Mes Desarrollo Arq.eintegra-
ción
NOCyredes SREynube Calidad Seguridad Implantación Plazastotales
51 3 1 13 2 1 5 1 26
52 3 1 14 2 1 5 1 27
53 3 1 13 2 1 5 1 26
54 3 1 14 2 1 5 1 27
55 3 1 13 2 1 5 1 26
56 3 1 18 2 1 5 1 31
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
55

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Paraelcontraste,sedistribuyenlas199.219,03HHporperfilyventanadecadapartida.Se
aplicaelcalendariodecoberturaaMesaN1,NOCySOC,elrepartoprevistoalacompañamiento
y los días de ejecución a las pruebas de certificación que cruzan meses. Cuando no hay un
repartomensualespecíficoporperfil,seusaelpromediodesuventana.Así,encadameslas
plazaspor128HHcubrenlasHHdelaTabla 11.Lasección5.7identifica,grupoporgrupo,los
perfilesquecubrencadamáximo.LareservadecorreccionesdeEtapa1semantieneexclusiva,
ylacoberturadiariaseasignaporpersona,dedicaciónyturno.
4.5 Reservasdecontingenciaydegestión
Las 199.219,03 HH de la sección 4.3 son la línea base programada e incluyen 3.072 HH
protegidasparacorreccionesdelaEtapa1.Esacapacidadseusasoloparaesascorrecciones.
Las reservas de riesgos del SD8 (Subdocumento 8) se administran por separado de la línea
base.LaholguracontractualdecadahitosecalculaenlaTabla 14conlasHH,elcalendarioy
lasprecedenciasvigentes.Esunmargendeprogramación,distintodeunareservadeHHo
monetaria.
Cadausodelacontingenciaporriesgoregistraelriesgo,larespuesta,elpaquete,elperfil,
elperíodoylaautorizacióndelSD8.Lareservadegestiónde160HHdelSD8quedafueradel
total programado y de la dotación, y se libera con la aprobación del Comité Ejecutivo. HH,
dineroydíasdeholgurasonmagnitudesdiferentesynosesumanentresí.
5 Redagregada,restriccionesyescenariosdecalendario
ElCPMcalculalasfechasapartirdelasduracionesdetrabajodelassecciones4.2–4.4y
delaspredecesorasdelasección6.1,conlos227paquetesylas199.219,03HH:168paquetes
tienen entregable y 59 son de esfuerzo continuo. La carta de la sección 6.1 programa cada
paquetedentrodesuventanatempranaytardía.
5.1 Cálculoreproducible
Laredagregadamodela401eventosy625relaciones.Cadapaqueteconentregabletiene
inicioyfin;lasrevisionesdeaceptacióndelCLIENTE,lascondicionesdemarchablancaydel
pilotoylospasosaproducciónsoneventosseparados.Seaplicaunapasadahaciaadelante
y otra hacia atrás (PMI, 2017, pp. 210–211). La tabla detallada permite comprobar fechas
tempranas,tardíasyholguras.
• Calendario.Elmes1correspondealsupuestodefebrerode2027.Eldesarrolloylarevisión
administrativausanelcalendariointernodelunesaviernesyferiadosprevistos;entresus
exclusionesestánel21dejuniode2027,el20dejuniode2028,el27deoctubreyel1de
noviembrede2028.EstecalendariorequiereconfirmaciónconelCLIENTEantesdeaprobar
la línea base; cualquier diferencia obliga a recalcular. NOC, mesa y acompañamiento
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
56

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
conservan sus calendarios de servicio de la sección 4.1; no se transforman en trabajo
administrativodelunesaviernes.
• Duración. La duración de cada paquete es⌈𝐻𝐻/(6,4 𝑛máx)⌉ días hábiles, con el equipo
máximodelasección6.1.Cadapaqueteiniciacuandosecumplensusprecedencias,sin
adelantarsealcomienzodesuventana.Lasactividadesdelasección6mantienenellímite
de una quincena. Las ocho semanas de homologación y las seis semanas de piloto se
conservanenlasventanaspublicadas.
• Trabajo interno de los módulos.Las puertas de contratos e integración usan sus HH
efectivasylaconstrucciónusa ⌈(𝐻𝐻 − 240)/(6,4 𝑛máx)⌉.Así,unaesperaporinterfaznose
cuentacomoconstrucción.Las168fechasdelacartaquedanentreeliniciotempranoyel
fintardíodesupaquete.
• Precedencias.FCconectaelfindelpredecesorconeliniciodelsucesor;CCconectasus
inicios.LadisponibilidaddeQAcondicionalaentregadelmódulo,nosuanálisisenDEV.
Enlasinterfaces,laentregaprecedentecondicionaelúltimoincrementodeintegracióndel
sucesor;sereservaalmenosunaactividadde80HHconsuequipomáximo.Enlosmódulos,
A01/A02yelincrementofinalserepresentancomopuertasinternas:laconstrucciónespera
elcontratoA02precedenteylaintegraciónesperalaentregaprecedente.Lasactividades
restantessedetallanporplanificacióngradual.Paraelcorte,losensayoscondicionanA06
y no el análisis preparatorio. No se elimina una dependencia por incumplir una fecha
programada.
• Cadenadefrío. Seincluyenbanco2.4.3,mapeo2.4.4,homologaciónycompra5.1.4,con-
tratos5.3.4,módulos3.4.4/3.4.5ypiloto4.1.4.Elcontratodebancodependedeliniciodela
especificación,CC.ElpilotoesperaH4ycuatroactasparcialesdekits;laoladereparto
esperaelpilotoylas28actas.Noseexigelainstalacióndelos28kitsparaempezarelpiloto
decuatrocamiones.
• CLIENTE.Laentregayelactasoneventosdistintos.Cadaentregadehitoreservadiezdías
hábilespararevisión(BA,art.18.3);secalculasufechalímiteretrocediendodesdeelúltimo
díalaborabledelmescontractual.H6yH11soncomienzosdemarchablanca.EnH7yH12
elactaquecierralamarchablanca(BA,art.17.3)estambiénelactadelhito(BA,art.18.1);
elpasoaproducciónocurredespuésdesufirmaydentrodelmes16o21.
• Holguras.Lapasadainversaimponetantolaventanamáximadecadapaquetecomolas
fechascontractuales.Unaholguranegativaobligaríaareplanificarsindesplazarelcontrato.
Laholguradeunhitocomparaelactayelpasoaproduccióncalculadosconsulímite;la
deunpaquetetambiénconsiderasuventanapropiaypuedesermenor.
• Recursos.Las HH y los máximos de equipo provienen de la sección 6.1. La capacidad
mensualsecontrastaconlasección4yconladotacióndelasección5.7.
LaTabla 13presentafechastempranas,tardíasyholgurasdelos168paquetesconentrega-
ble.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
57

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla13 Fechastempranas,tardíasyholgurasdelos168paquetesconentregable.Fuente:elaboraciónapartirdelassecciones4.2,5.1y6.1ydelAnexo7.B.
EDT Dura-
ción
(días)
Iniciotem-
prano
Fintemprano Iniciotardío Fintardío Hol-
gura
(días)
HH
1.1.1 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.1.2 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.1.3 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.2.1 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.2.3 7 01-02-2027 09-02-2027 20-05-2027 31-05-2027 77 80
1.2.4 7 01-03-2027 09-03-2027 08-03-2027 16-03-2027 5 80
1.2.5 7 01-02-2028 09-02-2028 07-02-2028 15-02-2028 4 80
1.3.1 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.3.2 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
1.3.3 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
1.3.4 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
1.4.1 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.4.2 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.5.1 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
1.6.1 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
1.7.1 7 01-04-2027 09-04-2027 22-04-2027 30-04-2027 15 80
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
58

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla13—continuación
EDT Dura-
ción
(días)
Iniciotem-
prano
Fintemprano Iniciotardío Fintardío Hol-
gura
(días)
HH
1.7.2 7 03-04-2028 11-04-2028 20-04-2028 28-04-2028 12 80
1.9.1 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.9.2 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.9.3 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
2.1.1 19 01-03-2027 25-03-2027 04-03-2027 31-03-2027 3 240
2.1.2 19 01-03-2027 25-03-2027 04-03-2027 31-03-2027 3 240
2.1.3 19 01-03-2027 25-03-2027 04-03-2027 31-03-2027 3 240
2.1.4 10 01-02-2028 14-02-2028 02-02-2028 15-02-2028 1 240
2.2.1 19 01-03-2027 25-03-2027 04-03-2027 31-03-2027 3 240
2.2.3 10 01-04-2027 14-04-2027 07-04-2027 20-04-2027 4 240
2.2.4 19 01-03-2027 25-03-2027 04-03-2027 31-03-2027 3 240
2.3.1 19 01-02-2027 25-02-2027 23-02-2027 19-03-2027 16 240
2.3.2 19 01-02-2027 25-02-2027 23-02-2027 19-03-2027 16 240
2.3.3 19 01-03-2027 25-03-2027 04-03-2027 31-03-2027 3 240
2.4.1 8 15-04-2027 26-04-2027 21-04-2027 30-04-2027 4 240
2.4.2 8 15-02-2028 24-02-2028 16-02-2028 25-02-2028 1 240
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
59

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla13—continuación
EDT Dura-
ción
(días)
Iniciotem-
prano
Fintemprano Iniciotardío Fintardío Hol-
gura
(días)
HH
2.5.1 19 01-04-2027 27-04-2027 06-04-2027 30-04-2027 3 240
2.5.2 19 01-04-2027 27-04-2027 06-04-2027 30-04-2027 3 240
2.6.1 19 01-03-2027 25-03-2027 04-03-2027 31-03-2027 3 240
2.6.2 19 01-04-2027 27-04-2027 06-04-2027 30-04-2027 3 240
2.6.3 19 03-05-2027 28-05-2027 04-05-2027 31-05-2027 1 240
3.1.1 13 01-06-2027 17-06-2027 10-06-2027 30-06-2027 7 240
3.1.2 13 01-06-2027 17-06-2027 10-06-2027 30-06-2027 7 240
3.1.3 13 01-06-2027 17-06-2027 10-06-2027 30-06-2027 7 240
3.1.4 19 03-05-2027 28-05-2027 04-05-2027 31-05-2027 1 240
3.1.5 13 01-06-2027 17-06-2027 10-06-2027 30-06-2027 7 240
3.2.1 19 03-05-2027 28-05-2027 04-05-2027 31-05-2027 1 240
3.2.2 19 03-05-2027 28-05-2027 04-05-2027 31-05-2027 1 240
3.2.3 19 03-05-2027 28-05-2027 04-05-2027 31-05-2027 1 240
3.2.4 19 03-05-2027 28-05-2027 04-05-2027 31-05-2027 1 240
3.2.5 19 03-05-2027 28-05-2027 04-05-2027 31-05-2027 1 240
3.2.6 19 01-06-2027 29-06-2027 02-06-2027 30-06-2027 1 240
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
60

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla13—continuación
EDT Dura-
ción
(días)
Iniciotem-
prano
Fintemprano Iniciotardío Fintardío Hol-
gura
(días)
HH
3.3.1 19 01-06-2027 29-06-2027 04-08-2027 31-08-2027 43 480
3.3.2 21 01-06-2027 01-07-2027 01-07-2027 30-07-2027 20 516
3.3.3 19 01-06-2027 29-06-2027 05-07-2027 30-07-2027 22 480
3.3.4 19 01-06-2027 29-06-2027 05-07-2027 30-07-2027 22 480
3.3.5 19 01-06-2027 29-06-2027 04-08-2027 31-08-2027 43 480
3.3.6 19 01-06-2027 29-06-2027 04-08-2027 31-08-2027 43 480
3.4.1 15 01-06-2027 22-06-2027 09-08-2027 27-08-2027 46 880,33
3.4.2 16 01-06-2027 23-06-2027 04-08-2027 27-08-2027 43 1006,67
3.4.3 16 01-06-2027 25-06-2027 10-08-2027 31-08-2027 45 973,83
3.4.4 24 01-06-2027 06-07-2027 27-08-2027 30-09-2027 60 1587,33
3.4.5 15 01-06-2027 22-06-2027 11-08-2027 31-08-2027 48 919,50
3.4.6 20 01-06-2027 30-06-2027 04-08-2027 31-08-2027 43 1314,17
3.4.7 16 01-06-2027 02-07-2027 08-09-2027 30-09-2027 62 937,67
3.4.8 24 01-06-2027 06-07-2027 27-08-2027 30-09-2027 60 1586,67
3.4.9 11 01-06-2027 17-06-2027 15-09-2027 30-09-2027 71 588
3.4.10 20 01-06-2027 08-07-2027 13-09-2027 12-10-2027 65 1248,33
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
61

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla13—continuación
EDT Dura-
ción
(días)
Iniciotem-
prano
Fintemprano Iniciotardío Fintardío Hol-
gura
(días)
HH
3.4.11 14 01-09-2027 21-09-2027 10-09-2027 30-09-2027 7 836,50
3.5.1 32 10-03-2028 25-04-2028 15-03-2028 28-04-2028 3 973
3.5.2 34 10-03-2028 27-04-2028 13-03-2028 28-04-2028 1 1033,17
3.5.3 11 10-03-2028 24-03-2028 13-04-2028 28-04-2028 24 280
3.5.4 22 10-03-2028 10-04-2028 29-03-2028 28-04-2028 13 653
3.6.1 19 02-08-2027 26-08-2027 03-09-2027 30-09-2027 24 480
3.6.2 19 01-07-2027 28-07-2027 05-08-2027 31-08-2027 24 480
3.6.3 19 01-07-2027 28-07-2027 05-08-2027 31-08-2027 24 480
3.6.4 19 01-07-2027 28-07-2027 05-08-2027 31-08-2027 24 480
3.6.5 21 01-02-2028 29-02-2028 03-07-2028 31-07-2028 105 516
3.6.6 20 01-06-2028 30-06-2028 03-08-2028 31-08-2028 43 508
3.7.1 20 02-08-2027 27-08-2027 01-10-2027 29-10-2027 43 512
3.7.2 20 01-10-2027 29-10-2027 03-11-2027 30-11-2027 21 504
3.7.3 20 01-12-2027 29-12-2027 03-12-2027 31-12-2027 2 504
3.7.4 20 01-12-2027 29-12-2027 03-12-2027 31-12-2027 2 504
3.7.5 15 03-01-2028 21-01-2028 11-01-2028 31-01-2028 6 480
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
62

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla13—continuación
EDT Dura-
ción
(días)
Iniciotem-
prano
Fintemprano Iniciotardío Fintardío Hol-
gura
(días)
HH
3.8.1 13 01-10-2027 20-10-2027 13-10-2027 29-10-2027 7 160
3.8.2 17 21-10-2027 15-11-2027 08-11-2027 30-11-2027 11 320
3.8.3 17 21-10-2027 15-11-2027 08-11-2027 30-11-2027 11 320
3.8.4 13 21-10-2027 09-11-2027 12-11-2027 30-11-2027 15 320
3.8.5 13 21-10-2027 09-11-2027 12-11-2027 30-11-2027 15 320
3.8.6 9 21-10-2027 03-11-2027 18-11-2027 30-11-2027 19 320
3.8.7 7 16-11-2027 24-11-2027 23-12-2027 31-12-2027 26 160
3.8.8 13 21-10-2027 09-11-2027 12-11-2027 30-11-2027 15 320
3.9.1 13 02-05-2028 18-05-2028 08-05-2028 24-05-2028 4 160
3.9.2 10 01-06-2028 14-06-2028 06-06-2028 19-06-2028 3 320
3.9.3 10 19-05-2028 01-06-2028 06-06-2028 19-06-2028 12 320
3.9.4 10 19-05-2028 01-06-2028 06-06-2028 19-06-2028 12 320
3.9.5 5 19-05-2028 25-05-2028 25-05-2028 31-05-2028 4 160
3.9.6 7 15-06-2028 27-06-2028 21-06-2028 30-06-2028 3 160
3.9.7 9 19-05-2028 31-05-2028 07-06-2028 19-06-2028 13 160
3.10.1.1 19 02-08-2027 26-08-2027 04-10-2027 29-10-2027 44 240
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
63

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla13—continuación
EDT Dura-
ción
(días)
Iniciotem-
prano
Fintemprano Iniciotardío Fintardío Hol-
gura
(días)
HH
3.10.1.2 19 01-10-2027 28-10-2027 04-11-2027 30-11-2027 22 240
3.10.1.3 19 01-10-2027 28-10-2027 04-11-2027 30-11-2027 22 240
3.10.1.4 19 01-12-2027 28-12-2027 03-04-2028 28-04-2028 87 240
3.10.2.1 19 01-03-2027 25-03-2027 06-04-2027 30-04-2027 25 240
3.10.2.2 19 01-04-2027 27-04-2027 02-06-2027 30-06-2027 43 240
3.10.2.3 19 01-06-2027 29-06-2027 04-11-2027 30-11-2027 106 240
3.10.2.4 19 01-12-2027 28-12-2027 03-04-2028 28-04-2028 87 240
3.10.3.1 19 01-04-2027 27-04-2027 02-06-2027 30-06-2027 43 240
3.10.3.2 19 01-06-2027 29-06-2027 04-10-2027 29-10-2027 85 240
3.10.3.3 19 01-10-2027 28-10-2027 04-11-2027 30-11-2027 22 240
3.10.3.4 19 01-12-2027 28-12-2027 03-04-2028 28-04-2028 87 240
3.10.4.1 19 01-02-2028 25-02-2028 07-03-2028 31-03-2028 25 240
3.10.4.2 19 01-03-2028 27-03-2028 03-04-2028 28-04-2028 23 240
3.10.4.3 19 03-04-2028 28-04-2028 02-06-2028 30-06-2028 42 240
3.10.4.4 19 03-07-2028 27-07-2028 03-10-2028 31-10-2028 63 240
4.1.1 7 02-11-2027 10-11-2027 22-11-2027 30-11-2027 14 80
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
64

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla13—continuación
EDT Dura-
ción
(días)
Iniciotem-
prano
Fintemprano Iniciotardío Fintardío Hol-
gura
(días)
HH
4.1.2 7 01-12-2027 10-12-2027 23-12-2027 31-12-2027 15 80
4.1.3 7 01-06-2028 09-06-2028 21-06-2028 30-06-2028 13 80
4.2.3 7 02-05-2028 17-05-2028 16-05-2028 31-05-2028 10 80
4.3.3 7 02-10-2028 18-10-2028 13-10-2028 31-10-2028 8 80
4.3.4 7 01-09-2028 11-09-2028 21-09-2028 29-09-2028 12 80
5.1.1 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
5.1.2 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
5.1.3 7 01-06-2027 09-06-2027 18-06-2027 30-06-2027 13 80
5.2.1 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
5.2.2 7 03-05-2027 11-05-2027 20-05-2027 31-05-2027 13 80
5.2.3 7 03-05-2027 11-05-2027 20-05-2027 31-05-2027 13 80
5.3.1 7 03-05-2027 11-05-2027 20-05-2027 31-05-2027 13 80
5.3.2 7 03-05-2027 11-05-2027 20-05-2027 31-05-2027 13 80
5.3.3 7 03-05-2027 11-05-2027 20-05-2027 31-05-2027 13 80
5.4.1 7 01-10-2027 12-10-2027 21-01-2028 31-01-2028 77 80
5.4.2 7 01-10-2027 12-10-2027 21-01-2028 31-01-2028 77 80
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
65

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla13—continuación
EDT Dura-
ción
(días)
Iniciotem-
prano
Fintemprano Iniciotardío Fintardío Hol-
gura
(días)
HH
5.4.3 7 01-06-2028 09-06-2028 21-09-2028 29-09-2028 75 80
5.4.4 7 02-08-2027 10-08-2027 23-08-2027 31-08-2027 15 80
6.1.1 13 01-04-2027 19-04-2027 14-04-2027 30-04-2027 9 160
6.1.2 13 01-04-2027 19-04-2027 14-04-2027 30-04-2027 9 160
6.1.3 13 01-04-2027 19-04-2027 14-04-2027 30-04-2027 9 160
6.1.4 13 01-04-2027 19-04-2027 14-04-2027 30-04-2027 9 160
6.1.5 13 03-05-2027 19-05-2027 04-05-2027 20-05-2027 1 160
6.2.1 13 03-05-2027 19-05-2027 12-05-2027 31-05-2027 7 160
6.2.2 13 01-07-2027 20-07-2027 13-07-2027 30-07-2027 8 160
6.2.3 13 02-08-2027 18-08-2027 13-08-2027 31-08-2027 9 160
6.3.1 13 20-05-2027 08-06-2027 24-05-2027 09-06-2027 1 160
6.3.2 13 20-05-2027 08-06-2027 24-05-2027 09-06-2027 1 160
6.3.3 13 03-05-2027 19-05-2027 12-05-2027 31-05-2027 7 160
6.3.4 13 01-10-2027 20-10-2027 13-10-2027 29-10-2027 7 160
6.4.1 13 01-06-2027 17-06-2027 10-06-2027 30-06-2027 7 160
6.4.2 13 01-06-2027 17-06-2027 10-06-2027 30-06-2027 7 160
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
66

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla13—continuación
EDT Dura-
ción
(días)
Iniciotem-
prano
Fintemprano Iniciotardío Fintardío Hol-
gura
(días)
HH
6.4.3 13 01-06-2027 17-06-2027 13-07-2027 30-07-2027 28 160
6.5.1 13 01-10-2027 20-10-2027 13-01-2028 31-01-2028 71 160
6.5.2 13 02-11-2027 18-11-2027 13-01-2028 31-01-2028 51 160
6.5.3 13 01-10-2027 20-10-2027 15-12-2027 31-12-2027 50 160
6.5.4 17 01-09-2027 24-09-2027 24-11-2027 31-01-2028 57 320
6.5.5 13 02-11-2027 18-11-2027 13-01-2028 31-01-2028 51 160
6.5.6 13 01-10-2027 20-10-2027 13-01-2028 31-01-2028 71 160
6.6.1 13 09-06-2027 29-06-2027 10-06-2027 30-06-2027 1 160
6.6.2 13 09-06-2027 29-06-2027 10-06-2027 30-06-2027 1 160
6.6.3 7 09-06-2027 17-06-2027 18-06-2027 30-06-2027 7 160
7.1.1 13 02-11-2027 18-11-2027 13-01-2028 31-01-2028 51 160
7.1.6 13 02-11-2027 18-11-2027 13-01-2028 31-01-2028 51 160
7.2.2 13 02-05-2028 18-05-2028 13-07-2028 31-07-2028 50 160
7.2.3 13 01-03-2027 17-03-2027 13-07-2027 30-07-2027 92 160
7.3.1 13 01-02-2028 17-02-2028 11-04-2028 28-04-2028 50 160
7.3.2 13 03-07-2028 19-07-2028 13-07-2028 31-07-2028 8 160
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
67

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla13—continuación
EDT Dura-
ción
(días)
Iniciotem-
prano
Fintemprano Iniciotardío Fintardío Hol-
gura
(días)
HH
9.1.1 7 02-10-2028 11-10-2028 20-10-2028 31-10-2028 13 80
9.1.2 7 19-10-2028 30-10-2028 22-11-2028 30-11-2028 22 80
9.2.2 7 01-09-2031 09-09-2031 22-09-2031 30-09-2031 13 80
2.4.3 18 01-04-2027 26-04-2027 07-04-2027 30-04-2027 4 341,33
2.4.4 13 03-05-2027 19-05-2027 12-05-2027 31-05-2027 7 240
4.1.4 27 05-11-2027 17-12-2027 24-11-2027 31-12-2027 10 341,33
5.1.4 19 01-02-2027 25-02-2027 04-03-2027 31-03-2027 23 240
5.3.4 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
68

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
5.2 Lecturadelassecuenciasylasrestricciones
Ningún paquete presenta holgura negativa frente a su ventana ni frente a un hito, y las
fechasdelacartacaendentrodelaventanatempranaytardíadecadapaquete.LaTabla 13
muestralaholguradecadapaquete.EnlaEtapa1,laintegración3.8.1terminaamástardarel
29deoctubrede2027,laspruebasdeaceptaciónysinconexión3.8.2y3.8.3,el30denoviembre,
ylacertificación3.8.7tieneveintiséisdíasdeholgura.Elactadecertificaciónesuntrámite
documental y no interviene sistemas en el congelamiento de diciembre. En la Etapa 2, la
certificación3.9.6eselpaquetemásajustadoantesdelH10,contresdíasdeholgura.Elcierre
formal9.1.2esperaelactaH12yseprogramadel26deoctubreal7denoviembrede2028,en
losmeses21y22.
Elpilotocomienzael9denoviembrede2027,despuésdelactadelH4,yterminael20de
diciembre,enlosmeses10y11.Sutramodediciembrenocontravieneelcongelamiento:la
solucióntodavíanoestáenproducción,loscamionessiguenoperandoconsustermógrafos
actualesyelpilotonomodificaelERP,elWMSnilafacturación.Ningúnkitseinstalanise
ajustaenlaventanadedespachode05:30a07:00.Larecepcióncompletadekitsprecedeala
oladerepartodelmes14.
5.3 Holgurasdeloshitosycapacidad
LaTabla 14presentalaentrega,elacta,elpasoaproducciónylaholguradecadahito.La
últimacolumnarepiteelcálculolimitandolareservasimultáneadelosequiposdedesarrollo
ydepruebasenlospaquetesconentregable;soloelH10pierdeundíadeholgura.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
69

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla14 Fechasyholgurasdeloshitoscalculadasporduracionesyprecedencias,conlalíneabasede199.219,03HH.Fuente:elaboraciónapartirdelas
secciones4.2,5.1y6.1,ydelAnexo7.B.
Hito Entrega Acta Pasoapro-
ducción
Límitecon-
tractual
Holgura
(días
hábiles)
Holguracon
límitede
capacidad
Paquetecontrolante
H1 09-03-2027 23-03-2027 — 31-03-2027 5 5 1.2.4
H2 26-04-2027 10-05-2027 — 31-05-2027 14 14 2.4.1
H3 17-06-2027 05-07-2027 — 30-07-2027 18 18 3.1.5
H4 20-10-2027 04-11-2027 — 30-11-2027 18 18 3.8.1
H5 24-11-2027 03-01-2028 — 31-01-2028 20 20 3.8.7
H6 01-02-2028 01-02-2028 — 01-02-2028 0 0 Iniciocontractualfijo
H8 24-02-2028 09-03-2028 — 31-03-2028 16 16 2.4.2
H7 02-05-2028 16-05-2028 17-05-2028 31-05-2028 10 10 4.2.1y4.2.3
H9 18-05-2028 01-06-2028 — 30-06-2028 19 19 3.9.1
H10 27-06-2028 11-07-2028 — 31-07-2028 14 13 3.9.6
H11 01-08-2028 01-08-2028 — 01-08-2028 0 0 Iniciocontractualfijo
H12 02-10-2028 17-10-2028 18-10-2028 31-10-2028 8 8 4.3.1y4.3.3
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
70

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Todosloshitoscumplensumescontractual.H7secumpleel17demayode2028yH12el
18deoctubrede2028,condiezyochodíashábilesdeholgura.Laholgurausalasduraciones
delalíneabase.Labandauniformede25%sobreladuraciónseusasolocomosensibilidad.
LasreservasderiesgodelSD8seadministransegúnlasección4.5ynoformanpartedeestas
holguras.
Capacidadconjuntayprioridaddehitos. Lacurvadelasección4.4incluyelospaquetescon
entregable,lacoberturacontinuaylareservaprotegida.Lasección5.7contrastaelmáximo
mensual por grupo de origen con las plazas previstas. Para la asignación diaria se asignan
primerolosrolesdelosentregablesconvencimientomáspróximoysereservanporseparado
losturnosdelosservicioscontinuosyelacompañamiento.
5.4 Gobierno
Semantienenlas199.219,03HHylasfechasprogramadas.Todadesviaciónqueconsuma
la holgura de un paquete se presenta al Comité de Proyecto con su plan de recuperación;
cualquierreprogramaciónobligaarepetirlaspasadasyelpresupuestomensual.Lascuatro
semanasfinalesdemarchablancaylosdiezdíasderevisióndelCLIENTEnosonreservade
trabajodelproponente.
Elacompañamientoreforzado4.3.2comienzaconelpasoaproduccióndel18deoctubre
de2028.Silafirmadelactaseatrasa,lasmismasHHseredistribuyenentrelosmeses21y22
sinacortarlascuatrosemanas.
5.5 PresentacióndeentregablesyrevisióndelCLIENTE
LaTabla 14distingueentrega,actaylímitecontractual.LosentregablesdelH4admiten
presentaciónporincrementos;elúltimoinformedeintegraciónylarevisióncompletaquedan
reflejadosenlared.H1,H7yH12disponendecinco,diezyochodíashábilesdeholgura.La
revisiónpreliminardecadaexpedienteporelComitédeProyectoantesdesuentregabusca
evitarobservaciones.SilaContraparteformulaobservacionesalcierredeunamarchablanca,
LafroXlassubsanaenelplazodelartículo18.3y,sialtérminodelperíodonosecumplenlas
seiscondicionesdelartículo17.3,extiendelamarchablancaasucostosindesplazarlasfechas
contractualesdelasfasessiguientes.
ActaintegradadeH7yH12. LoshitosH7yH12secierranconunasolaactaporetapa,conforme
alaagrupacióndeentregablesdelE-25.Durantelamarchablanca,4.2.1y4.3.1producenla
evidenciadiariadeindicadores,conciliación,capacitaciónyrestauraciones,ylaconsolidan
semanaasemana.Elprimerdíahábildespuésdelascuatrosemanasfinales,elpaquete4.2.3
o4.3.3entregaelexpedientecompleto:laevidenciadelasseiscondicionesdelartículo17.3,la
trazabilidadylasobservacionespreviasresueltasqueexigeelartículo18.2,yenE2también
lagarantía4.3.4.LaContraparterevisadurantediezdíashábilesyfirmaelactaquecierrala
marchablancayaceptaelhito(arts.17.3y18.1).Elpasoaproducciónseejecutaeldíahábil
siguiente,fueradelaventanadedespacho,yseregistraenelmismoexpediente.LaTabla 15
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
71

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
muestralasecuencia.
Tabla15 SecuenciadelactaintegradadeH7yH12.Calendariosinobservaciones.
Evento H7:Etapa1 H12:Etapa2
Cierredelascuatrosemanasdeevidencia 30-04-2028 30-09-2028
Entregadelexpedientecompleto 02-05-2028 02-10-2028
Diezdíashábilesderevisión 03–16demayo 03–17deoctubre
Firmadelactadelhito 16-05-2028 17-10-2028
Pasoaproducción 17-05-2028 18-10-2028
Mescontractual 16 21
Cadapaquetedeaceptacióntiene80HHdelJefedeProyectoydelanalistaPMO:consolida-
ciónyentregadelexpediente,atencióndelasconsultasdelaContrapartedurantelarevisióny
registrodelpasoaproducción.ElprocedimientoseconfirmaconelCLIENTEenelactade
inicio1.1.3,juntoconlasventanasdepasoaproducción.
5.6 Medicióndelosnivelesdeatención
Durantelaatenciónde04:00a22:00delunesasábadoysucobertura24 ×7enlospeaksde
septiembreydiciembreyanteincidentescríticosenlaventanadedespacho,LafroXatenderá
almenosel80%deloscontactosantesde20segundos,resolveráalmenosel70%enelprimer
contacto y mantendrá el abandono en un máximo del 5%. Estos resultados se medirán y
reportaránmensualmenteyactivaránlasmedidasderecalibraciónyrefuerzoprevistasen
estasección(BTT,cap.21,RT-21.06,p.36;Caso,cap.15,pp.26–27).
ElErlangCdelamesa(SD4,Anexo4-W.7)dimensionalaesperaconllegadasdePoisson,
atenciónexponencialypacienciainfinita.Sirveparael80%derespuestasantesde20segundos,
pero no modela el abandono ni la resolución al primer contacto del RT-21.06 de las Bases
Técnicas Transversales (p. 36). Para ambos se aplica medición: desde la marcha blanca de
laEtapa1,lamesaregistraporcontactolahoradellegada,derespuestaodeabandonoysi
seresolviósinescalar.Conalmenoscuatrosemanasderegistrossecalibraunmodelocon
abandono(ErlangA)usandolapacienciaobservada,yserecalculaladotaciónde8.1.2antes
delmes21.Laresoluciónalprimercontactosesostieneconlabasedeconocimientode3.11y
lacapacitaciónde7.1,yseinformamensualmente.Siunindicadornosecumpledurantedos
mesesseguidos,seaumentaladotacióndelafranjaafectadasinesperarlarevisiónanual.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
72

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
5.7 Dotaciónrequerida,rolesmínimosydotacióndeclarada
LaTabla 16comparalasplazasprevistasparaelproyectoylademandamáximamensual
con los siete grupos técnicos declarados en el SD1, Tabla 1.3. La sección 6.3 propone 136
plazas:109desdelosgrupostécnicosdeplanta,incluidasMesaN1,SOCyrefuerzosdepruebas
e integración, 9 del área de Implantación y Gestión del Cambio y 18 asistentes de terreno
contratadosporobraofaena.Elregistrodeasignaciónidentificatitular,dedicaciónyturnode
cadaplazaantesdeaprobarlalíneabase.
Tabla16 Plazasprevistasydemandamáximamensualpororigen.Fuente:elaboraciónapartirdelSD1,Tabla1.3,
ydelasección4.4deesteformulario.
Grupodeorigen Planta
SD1
Plazas
previstas
Demanda
máxima
Mesde
máximo
Desarrollodesoftware 48 36 32 6y7
Arquitecturaeintegración 15 15 11 8
NOC24×7yredesdeInfraestructura 32 29 21 32
SREynube 12 12 12 4y5
Calidad 10 10 8 17
Seguridad 7 7 6 16
Implantaciónygestióndelcambio(9deplantay18
porobraofaena)
9 27 26 19y20
Todoslosgruposquedandentrodesuplanta.ArquitecturaeIntegraciónllegaa11plazas
enelmes8,frentea15.Dentrodelgrupo,lacargadedatossuperaasusseisingenierosenlos
meses8,9y11(10,7,7,1y8,6plazas),cuandocoincidenelmódulo3.4.11,laintegración3.6.1
y las migraciones 3.7; la diferencia la cubren los dos ingenieros de integración senior y los
tresarquitectosdesolución,cuyacargapropiaenesosmesesesinferioraunaplaza.SREy
nubellegaa12enlosmeses4y5,igualasuplanta,porquelasinstalacionesfísicasdelasala
técnica,elcableado,losracks,losgabinetesdebordeylosenlaces(6.1,6.2,6.3,6.6.2y6.6.3)
lasejecutapersonalderedesyoperacióndeladivisiónInfraestructura,queenlosmeses3a9
notienecargaenesteproyectoporqueelNOCdePuelchecomienzaenelmes13;elLíderde
Operación/SREsiguecomoresponsabledeesospaquetes.LademandadeSeguridadincluye
elSOC,cubiertoconcuatroespecialistasdelgrupoydosoperadoresdelNOC.Antesdelmes
13,cuandoelSOCaúnnotieneturnos,lademandadeseguridadllegaa4,4plazasenelmes
2ya4,6enelmes5:elEncargadodeSeguridadylosdosespecialistasdeciberseguridadla
cubrencondosdeesoscuatroanalistas.Cadapersonasecuentaunasolavezaunquecubra
variosroles.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
73

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Laobracivildeseparaciónde6.1.1correspondealCLIENTE(RT-06.06);LafroXespecificay
coordina,yproveeelpisotécnicoylasinstalacionesdesualcance.Elmes3esunanecesidad
delaprogramación,nounafechadeentregayaconfirmadaporelCLIENTE.Elactadedispo-
nibilidaddelrecintodebeprecederalostrabajosquedependandeella;6.1.5recibetambién
laobrade6.1.1,ademásdeenergía,climatizacióneincendio.Unretrasoseanalizafrentea
H3antesdeiniciarmontaje.
LaasignaciónyhabilitacióndeanalistasinternosdelSOCdebecompletarseantesdelmes
13bajoelEncargadodeSeguridad.Lacobertura24 ×7ylosrelevosseincluyenen8.1.5;eltotal
desieteespecialistasdeclaradosnodemuestraporsísolodisponibilidadsimultáneaparaSOC
ylasdemástareasdeseguridad.Seconfirmasuasignaciónporturnoysecontrastaelpersonal
dearquitectura,integraciónydatosconlas15plazasdelgrupodeorigen.
Laimplantacióntieneunequipopropio,separadodeDesarrollo.EláreadeImplantacióny
GestióndelCambiodelSD1aportanuevepersonasdeplanta:elLíderdeImplantación,dos
coordinadores,uninstructorycincojefesdefrente(bodegadeTalca,bodegadeConcepción,
plataformas,rutadeTalcayrutadeConcepción).Losjefesdefrentesonconsultoresfunciona-
les:decidenenterrenosielusuariooperacorrectamente,siseaplicalacontingenciaycuándo
seescala.Aellossesuman18asistentesdeimplantaciónenterreno,contratadosdirectamente
por LafroX por obra o faena entre los meses 11 y 22, con experiencia en bodega, reparto o
soporteausuariosyreclutadosenTalcayConcepción.Acompañanapreparadores,operadores
de plataforma, conductores y preventistas, resuelven dudas de uso y registran incidencias,
siempreacargodeunjefedefrente;secapacitanenlosmeses11y12,secertificanantesdel
H6ysuscontratosterminanenformaescalonadasegúnlacurvadeadopción(RT-20.05).El
máximodelafamiliaesde26plazasenelmes19,cubiertoporlas9deplantaylos18asistentes.
Ningúndesarrolladorseasignaaacompañamientoenterreno.
LademandadeDesarrollollegaa32plazasenlosmeses6y7,durantelaconstrucciónde
losmódulosdelaEtapa1:unadedireccióny31deconstrucción.Laconstrucciónlacubren
33 personas del grupo: el Líder de Desarrollo, los 27 desarrolladores móviles, front-end y
back-end,losdosingenierosdeintegraciónjuniorylostresanalistasQAjunior,queenesos
meses participan en la construcción y en las pruebas unitarias de los módulos. Con el Jefe
deProyectoylosdosanalistasPMO,losperfilesdelgruposuman36plazas,dentrodelos48
desarrolladoresdeplanta.Enlosmeses1y2,lospaquetesdeinicioylosplanesdegestión
demandan4,7y3,5plazasdedirección:elJefedeProyectoylosdosanalistasPMOlospreparan
conelLíderdeDesarrolloyundesarrolladorsenior,quenotienencargadeconstrucciónantes
delmes5.Laasignacióndiariaseregistraporpersona,competenciayturno,separadadelos
servicioscontinuos.
Entre el 25-10 y el 11-11-2027, los paquetes de pruebas 3.8.2 a 3.8.5 requieren al menos
1.049,60 HH dentro del intervalo. Con diez personas de planta durante trece días a 6,4 HH
efectivaspordíasecubren832HH.Elplanreservaunmínimodetresrefuerzosdepruebas
paraesetramo:aportan249,60HHyelevanlacapacidadteóricaa1.081,60HH.Antesdeiniciar
laspruebas,Calidaddebeacreditarlosrefuerzosycomprobarladisponibilidaddiariapara
pruebasyserviciossimultáneos.Sinopuedecubrirlos,senivelaelcalendarioysevuelvena
comprobarH5ylasventanasdeaceptación.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
74

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Losrolesmínimosdelnumeral19.2delasBasesTécnicasTransversales(p.34)conservan
susdedicaciones.ElJefedeProyectodirigelaimplementación;elLíderdeDesarrolloparticipa
en el diseño y los prototipos de los primeros meses y después en la construcción; el Líder
Funcional cubre levantamiento, aceptación y olas; y el Líder de Integración mantiene la
responsabilidaddelospaquetesdeinterfaces.ElSD1,sección1.5,identificaalostitulares.Las
HHsecontabilizanunasolavezenlospaquetesdondeintervienecadarol.
6 Listadeactividades:regladel8/80ydelperíododereporte
LaEDTdelFormularioT-14llegahastaelpaquetedetrabajo;fueradeella,cadapaquetese
descomponeenlasactividadesquepermitenprogramarlo,asignarloycontrolarlo(PMI,2017,
pp.183–185).Lasactividadescumplendosreglasdetamaño:
• Regladel8/80. Cadaactividadrequiereentre8y80horashombredeesfuerzo.
• Regladelperíododereporte. Cadaactividadcabeenunaquincena,elperíododereporte
delComitédeProyecto(paquete1.8.3):duracomomáximodiezdíashábiles.Con6,4HH
efectivasporpersonay día, una actividadde80 HH con dospersonasdura ⌈80 ÷12,8⌉=
7díashábiles;sisuventanaesmáscorta,seleasignanmáspersonas.Todaactividadde
niveldeesfuerzosedivideenrelevosde64HHcomomáximo.
La descomposición no cambia las HH de la sección 4: la suma de las actividades de cada
paqueteesigualasuesfuerzoesperadoE.Lasactividadesheredanelresponsableylaventana
delpaquete.LaTabla 17dalasfechasdecadapaqueteylaTabla 18lasactividadeshastaelH2.
Porplanificacióngradual(PMI,2017,p.185),antesdecadafasesedetallanlasactividadesde
lafasesiguienteconlasestimacionesdelequipo,sinmoverloshitosniconsumirmásreserva
quelaregistrada.Elavanceseinformaporelcódigodelaactividad,quecuelgadelcódigode
supaquete.
6.1 Paquetesconentregableyplanificacióngradual
LaTabla 17conservalaprogramaciónpropuestadelos168paquetesconentregable:rol,
personas, HH, inicio, fin y predecesoras. Las personas se expresan como promedio en los
díascontrabajoycomomáximosimultáneo;comolaventanapuedeincluirdíasdemargen,
el promedio puede superar el cociente entre las HH y los días de la ventana. La Tabla13
presentalasfechastempranasytardíasylaholguradeesosmismospaquetes;cadafechade
la carta cae dentro de ese intervalo. QA condiciona la entrega; CC condiciona el inicio; las
interfacescondicionancontratosyentrega/integración.Los59paquetescontinuosmantienen
suscalendariosdeservicio.Laplanificacióngradualdescomponelospaquetessiguientesal
H2antesdecadafase.
Cadapaquetesedescomponeenactividadesde8a80HHquecabenenunaquincena,con
unaplantillaporclase:unmódulo(D,conlasHHdesuestimaciónportamaño)seconstruye
en iteraciones de dos semanas con análisis, diseño de contratos, incrementos, pruebas de
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
75

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
contrato, integración en QA y entrega; una integración (I, 480 HH), en seis actividades; un
diseño(E,240HH),entres;unainstalaciónocapacitación(T,160HH),endos,yunaprueba
ampliada(V,320HH),encuatro.LaTabla 18detallalas119actividadesdelos60paquetesque
terminanhastaelH2(mes4).Elrestosedescomponeporplanificacióngradual(PMI,2017,p.
185):antesdecadafase(H2,H4,H8yH9)ellíderdelfrentedetallalasactividadesdelafase
siguienteconlaestimacióndelequipo,elComitédeProyectolasapruebacomoiteraciones
delprocesodelSD6,sección6.2(Subdocumento6),yseactualizalalíneabasesinmoverlos
hitosnilasfechaslímitedelaTabla 14.
LaFigura 3muestraquépartedelcronogramasedetallaenlaofertayenquémomentose
detallaelresto.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
76

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Inicio, alcance y diseño
E1
Actividades
de 8 a 80 HH
Construcción E1:
base compartida,
módulos e integraciones
Se detalla antes del
H2 (mes 4)
Certificación y marcha
blanca
E1
Se detalla antes del H4
(mes 10)
Diseño y construcción
E2
Antes del H8
con línea base E2
Certificación y marcha
blanca
E2
Se detalla antes del
H9 (mes 17)
H2 H4 H8 H9
1
feb
2
mar
3
abr
4
may
5
jun
6
jul
7
ago
8
sep
9
oct
10
nov
11
dic
12
ene
13
feb
14
mar
15
abr
16
may
17
jun
18
jul
19
ago
20
sep
21
oct
2027 2028Figura3 Planificacióngradualdelcronograma.Fuente:elaboraciónapartirdelasTablas 17y18.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
77

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Lafiguramuestraquesóloloscuatroprimerosmeses,hastaelH2,sepresentandescom-
puestosenactividades.Cadafaseposteriortienesuspaquetes,fechasydependenciasfijos,
ysedetallaenunpuntodereplanificaciónubicadoantesdelhitoquelaprecede,cuandoel
equipoyaconoceeltrabajo:asíelcronogramanoprometeeldíaexactodeunaactividadque
ocurriráunañodespués.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
78

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla17 Programacióndelospaquetesconentregable.Fuente:elaboraciónapartirdelassecciones4.1,4.2y5.1deesteformularioy(Subdocumento7,
Anexo7.B).
Paquete Rol Personas(prom.
/máx.)
HH Inicio Fin Predecesoras(cuentaopaquete)
1.1.1 JP 1,8/2 80 01-02-2027 09-02-2027 —
1.1.2 JP 1,8/2 80 01-02-2027 09-02-2027 —
1.1.3 JP 1,8/2 80 01-02-2027 09-02-2027 —
1.2.1 ARQ 1,8/2 80 01-02-2027 09-02-2027 —
1.2.3 ARQ 1,8/2 80 01-02-2027 09-02-2027 —
1.2.4 CAL 1,8/2 80 01-03-2027 09-03-2027 —
1.2.5 ARQ 1,8/2 80 01-02-2028 09-02-2028 —
1.3.1 JP 1,8/2 80 10-02-2027 18-02-2027 —
1.3.2 JP 1,8/2 80 01-03-2027 09-03-2027 —
1.3.3 JP 1,8/2 80 01-03-2027 09-03-2027 —
1.3.4 JP 1,8/2 80 01-03-2027 09-03-2027 —
1.4.1 JP 1,8/2 80 01-02-2027 09-02-2027 —
1.4.2 JP 1,8/2 80 01-02-2027 09-02-2027 —
1.5.1 CAL 1,8/2 80 01-03-2027 09-03-2027 —
1.6.1 JP 1,8/2 80 01-03-2027 09-03-2027 —
1.7.1 JP 1,8/2 80 01-04-2027 09-04-2027 —
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
79

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla17—continuación
Paquete Rol Personas(prom.
/máx.)
HH Inicio Fin Predecesoras(cuentaopaquete)
1.7.2 JP 1,8/2 80 03-04-2028 11-04-2028 —
1.9.1 SEG 1,8/2 80 01-02-2027 09-02-2027 —
1.9.2 SEG 1,8/2 80 01-02-2027 09-02-2027 —
1.9.3 SEG 1,8/2 80 01-03-2027 09-03-2027 —
2.1.1 ARQ 1,8/2 240 01-03-2027 29-03-2027 1.2.1(D-01,poretapa)
2.1.2 ARQ 1,8/2 240 01-03-2027 29-03-2027 —
2.1.3 DAT 1,8/2 240 01-03-2027 29-03-2027 —
2.1.4 ARQ 3,1/4 240 01-02-2028 15-02-2028 —
2.2.1 SEG 1,8/2 240 01-03-2027 29-03-2027 —
2.2.3 SEG 3,1/4 240 01-04-2027 16-04-2027 —
2.2.4 SEG 1,8/2 240 01-03-2027 29-03-2027 —
2.3.1 SRE 1,8/2 240 01-02-2027 01-03-2027 —
2.3.2 SRE 1,8/2 240 01-02-2027 01-03-2027 —
2.3.3 SRE 1,8/2 240 01-03-2027 29-03-2027 —
2.4.1 ARQ 4,2/5 240 19-04-2027 29-04-2027 2.1.1–2.1.3,2.2.1,2.2.3,2.2.4
2.4.2 ARQ 4,7/5 240 16-02-2028 25-02-2028 1.2.5,2.1.4
2.5.1 SRE 1,8/2 240 01-04-2027 29-04-2027 —
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
80

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla17—continuación
Paquete Rol Personas(prom.
/máx.)
HH Inicio Fin Predecesoras(cuentaopaquete)
2.5.2 SRE 1,8/2 240 01-04-2027 29-04-2027 —
2.6.1 IMP 1,8/2 240 01-03-2027 29-03-2027 —
2.6.2 IMP 1,8/2 240 01-04-2027 29-04-2027 —
2.6.3 IMP 1,8/2 240 03-05-2027 31-05-2027 —
3.1.1 SRE 2,5/3 240 01-06-2027 18-06-2027 3.2.1,3.2.2,3.2.4,3.2.5(D-08)
3.1.2 SRE 2,5/3 240 01-06-2027 18-06-2027 3.2.1,3.2.2,3.2.4,3.2.5(D-08)
3.1.3 SRE 2,5/3 240 01-06-2027 18-06-2027 3.2.1,3.2.2,3.2.4,3.2.5(D-08)
3.1.4 SRE 1,8/2 240 03-05-2027 31-05-2027 —
3.1.5 SRE 2,5/3 240 01-06-2027 18-06-2027 —
3.2.1 SRE 1,8/2 240 03-05-2027 31-05-2027 5.2.1(D-07)
3.2.2 SRE 1,8/2 240 03-05-2027 31-05-2027 5.2.1(D-07)
3.2.3 SRE 1,8/2 240 03-05-2027 31-05-2027 5.2.1(D-07)
3.2.4 SRE 1,8/2 240 03-05-2027 31-05-2027 5.2.1(D-07)
3.2.5 SEG 1,8/2 240 03-05-2027 31-05-2027 5.2.1(D-07)
3.2.6 SRE 1,8/2 240 01-06-2027 29-06-2027 5.2.1(D-07)
3.3.1 SEG 3,3/4 480 01-06-2027 05-08-2027 2.2.1(D-06)
3.3.2 ARQ 3,9/4 516 01-06-2027 01-07-2027 1.2.3(D-02)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
81

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla17—continuación
Paquete Rol Personas(prom.
/máx.)
HH Inicio Fin Predecesoras(cuentaopaquete)
3.3.3 ARQ 3,3/4 480 01-06-2027 07-07-2027 —
3.3.4 ARQ 3,6/4 480 10-06-2027 12-07-2027 —
3.3.5 ARQ 3,3/4 480 01-06-2027 03-08-2027 —
3.3.6 ARQ 3,3/4 480 07-06-2027 03-08-2027 —
3.4.1 DES 6,5/12 880,33 10-06-2027 10-08-2027 2.4.1,2.6.2,3.1(QA),3.3(CC)
3.4.2 DES 7,9/12 1006,67 10-06-2027 11-08-2027 2.4.1,2.6.2,3.1(QA),3.3(CC)
3.4.3 DES 6,1/12 973,83 14-06-2027 18-08-2027 2.4.1,2.6.2,3.1(QA),3.3(CC),3.4.1/3.4.2(interfaz)
3.4.4 DES 12,0/12 1587,33 14-06-2027 29-09-2027 2.4.1,2.6.2,3.1(QA),3.3(CC),3.4.1/3.4.2(interfaz),
2.4.3,2.4.4
3.4.5 DES 7,2/12 919,5 14-06-2027 30-08-2027 2.4.1,2.6.2,3.1(QA),3.2.3,3.3(CC),2.4.3,2.4.4
3.4.6 DES 10,3/12 1314,17 16-06-2027 17-08-2027 2.4.1,2.6.2,3.1(QA),3.3(CC),3.4.2(CC)
3.4.7 DES 8,1/12 937,67 16-06-2027 08-09-2027 1.2.2,2.4.1,2.6.2,3.1(QA),3.3(CC),3.4.3/3.4.6(inter-
faz)
3.4.8 DES 12,0/12 1586,67 16-06-2027 09-09-2027 2.4.1,2.6.2,3.1(QA),3.3(CC),3.4.3/3.4.6(interfaz)
3.4.9 DES 5,1/12 588 18-06-2027 30-09-2027 2.4.1,2.6.2,3.1(QA),3.3(CC)
3.4.10 DES 9,8/12 1248,33 10-06-2027 04-10-2027 2.4.1,2.6.2,3.1(QA),3.3(CC),3.4.8(interfaz)
3.4.11 DAT 7,8/12 836,5 02-09-2027 27-09-2027 2.4.1,2.6.2,3.1(QA),3.3(CC)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
82

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla17—continuación
Paquete Rol Personas(prom.
/máx.)
HH Inicio Fin Predecesoras(cuentaopaquete)
3.5.1 DES 4,8/5 973 15-03-2028 28-04-2028 1.2.5,2.4.2(D-29)
3.5.2 DES 5,0/5 1033,17 15-03-2028 28-04-2028 1.2.5,2.4.2(D-29)
3.5.3 DES 1,4/5 280 15-03-2028 28-04-2028 1.2.5,2.4.2(D-29)
3.5.4 DAT 3,2/5 653 15-03-2028 28-04-2028 1.2.5,2.4.2(D-29)
3.6.1 DAT 3,3/4 480 02-08-2027 01-09-2027 1.1.3
3.6.2 DES 3,3/4 480 01-07-2027 02-08-2027 1.2.3
3.6.3 DES 3,3/4 480 01-07-2027 02-08-2027 1.2.3
3.6.4 DES 3,3/4 480 01-07-2027 02-08-2027 1.2.3
3.6.5 DES 2,3/4 516 01-02-2028 04-07-2028 1.2.3(perfildeintercambio)
3.6.6 DES 2,2/4 508 01-06-2028 23-08-2028 1.2.3(perfildeintercambio)
3.7.1 DAT 3,5/4 512 04-08-2027 01-10-2027 2.1.3,3.3.2
3.7.2 DAT 3,8/4 504 04-10-2027 03-11-2027 3.7.1
3.7.3 DAT 3,5/4 504 01-12-2027 31-12-2027 3.7.2
3.7.4 DAT 3,5/4 504 01-12-2027 31-12-2027 3.7.2
3.7.5 DAT 3,9/5 480 03-01-2028 27-01-2028 3.7.1,3.7.2,3.7.3,3.7.4
3.8.1 CAL 1,8/2 160 05-10-2027 22-10-2027 3.4,3.6.1–3.6.4(D-20)
3.8.2 CAL 2,5/3 320 25-10-2027 19-11-2027 3.8.1
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
83

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla17—continuación
Paquete Rol Personas(prom.
/máx.)
HH Inicio Fin Predecesoras(cuentaopaquete)
3.8.3 CAL 2,5/3 320 25-10-2027 19-11-2027 3.8.1
3.8.4 CAL 3,6/4 320 25-10-2027 11-11-2027 3.8.1
3.8.5 CAL 3,6/4 320 25-10-2027 11-11-2027 3.8.1
3.8.6 SEG 3,9/6 320 25-10-2027 11-11-2027 3.8.1
3.8.7 CAL 3,1/4 160 22-11-2027 01-12-2027 3.8.2,3.8.3,3.8.4,3.8.5,3.8.6,3.8.8
3.8.8 SRE 3,6/4 320 25-10-2027 11-11-2027 3.8.1
3.9.1 CAL 1,8/2 160 02-05-2028 18-05-2028 3.5
3.9.2 CAL 5,0/5 320 02-06-2028 15-06-2028 3.9.1
3.9.3 CAL 5,0/5 320 19-05-2028 01-06-2028 3.9.1
3.9.4 CAL 5,0/5 320 19-05-2028 01-06-2028 3.9.1
3.9.5 SEG 4,2/5 160 19-05-2028 26-05-2028 3.9.1
3.9.6 CAL 3,6/4 160 16-06-2028 28-06-2028 3.9.1,3.9.2,3.9.3,3.9.4,3.9.5,3.9.7
3.9.7 SRE 2,5/3 160 19-05-2028 01-06-2028 3.9.1
3.10.1.1 DAT 1,8/2 240 02-08-2027 08-10-2027 —
3.10.1.2 DAT 1,8/2 240 01-10-2027 19-11-2027 3.10.1.1(protocoloinicial)
3.10.1.3 DAT 1,8/2 240 01-10-2027 19-11-2027 3.10.1.1(protocoloinicial)
3.10.1.4 DAT 1,8/2 240 01-12-2027 20-03-2028 3.10.1.2y3.10.1.3
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
84

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla17—continuación
Paquete Rol Personas(prom.
/máx.)
HH Inicio Fin Predecesoras(cuentaopaquete)
3.10.2.1 CAL 1,8/2 240 01-03-2027 20-04-2027 —
3.10.2.2 CAL 1,8/2 240 01-04-2027 09-06-2027 3.10.2.1(contratodeevidencia)
3.10.2.3 CAL 1,8/2 240 01-06-2027 08-10-2027 3.10.2.2(circuitomínimo)
3.10.2.4 CAL 1,8/2 240 01-12-2027 20-03-2028 3.10.2.3
3.10.3.1 DAT 1,8/2 240 01-04-2027 09-06-2027 —
3.10.3.2 DAT 1,8/2 240 07-06-2027 20-09-2027 3.10.3.1(parámetrosaprobados)
3.10.3.3 DAT 1,8/2 240 01-10-2027 19-11-2027 3.10.3.2
3.10.3.4 DAT 1,8/2 240 01-12-2027 20-03-2028 3.10.3.3
3.10.4.1 IMP 1,8/2 240 01-02-2028 21-03-2028 —
3.10.4.2 IMP 1,8/2 240 01-03-2028 19-04-2028 3.10.4.1(prototipoinicial)
3.10.4.3 IMP 1,8/2 240 03-04-2028 09-06-2028 3.10.4.1y3.10.4.2(diseñovalidado)
3.10.4.4 IMP 1,8/2 240 03-07-2028 29-09-2028 3.10.4.3
4.1.1 IMP 1,8/2 80 02-11-2027 10-11-2027 3.8.1(D-48)
4.1.2 IMP 1,8/2 80 01-12-2027 10-12-2027 4.1.1,3.7.2,3.8.2(D-49)
4.1.3 IMP 1,8/2 80 01-06-2028 09-06-2028 4.1.2,3.9.1(D-50)
4.2.3 JP 1,8/2 80 02-05-2028 17-05-2028 4.2.1,7.3.1(D-28)
4.3.3 JP 1,8/2 80 02-10-2028 18-10-2028 4.3.1,4.3.4,7.1.4,7.3.2(D-33)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
85

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla17—continuación
Paquete Rol Personas(prom.
/máx.)
HH Inicio Fin Predecesoras(cuentaopaquete)
4.3.4 JP 1,8/2 80 13-09-2028 25-09-2028 —
5.1.1 ARQ 1,8/2 80 01-03-2027 09-03-2027 —
5.1.2 ARQ 1,8/2 80 02-03-2027 10-03-2027 2.3.1,2.3.2(D-09)
5.1.3 SRE 1,8/2 80 01-06-2027 09-06-2027 —
5.2.1 SRE 1,8/2 80 01-03-2027 09-03-2027 —
5.2.2 SRE 1,8/2 80 03-05-2027 11-05-2027 —
5.2.3 ARQ 1,8/2 80 03-05-2027 11-05-2027 —
5.3.1 SRE 1,8/2 80 03-05-2027 11-05-2027 —
5.3.2 SRE 1,8/2 80 03-05-2027 11-05-2027 —
5.3.3 SRE 1,8/2 80 03-05-2027 11-05-2027 —
5.4.1 IMP 1,8/2 80 01-10-2027 12-10-2027 —
5.4.2 IMP 1,8/2 80 01-10-2027 12-10-2027 —
5.4.3 JP 1,8/2 80 01-06-2028 09-06-2028 —
5.4.4 JP 1,8/2 80 02-08-2027 10-08-2027 —
6.1.1 RED 1,8/2 160 01-04-2027 20-04-2027 5.1.2(D-10)
6.1.2 RED 1,8/2 160 01-04-2027 20-04-2027 5.1.2(D-10)
6.1.3 RED 1,8/2 160 01-04-2027 20-04-2027 5.1.2(D-10)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
86

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla17—continuación
Paquete Rol Personas(prom.
/máx.)
HH Inicio Fin Predecesoras(cuentaopaquete)
6.1.4 RED 1,8/2 160 01-04-2027 20-04-2027 5.1.2(D-10)
6.1.5 RED 1,8/2 160 03-05-2027 20-05-2027 5.1.2,6.1.1–6.1.4(recepción)
6.2.1 RED 1,8/2 160 03-05-2027 20-05-2027 —
6.2.2 RED 1,8/2 160 01-07-2027 20-07-2027 —
6.2.3 RED 1,8/2 160 02-08-2027 19-08-2027 —
6.3.1 RED 1,8/2 160 24-05-2027 09-06-2027 6.1.5(D-11)
6.3.2 RED 1,8/2 160 24-05-2027 09-06-2027 6.1.5(D-11)
6.3.3 RED 1,8/2 160 03-05-2027 20-05-2027 —
6.3.4 RED 1,8/2 160 01-10-2027 20-10-2027 —
6.4.1 SEG 1,8/2 160 01-06-2027 18-06-2027 —
6.4.2 SEG 1,8/2 160 07-06-2027 24-06-2027 —
6.4.3 SEG 1,8/2 160 22-06-2027 09-07-2027 —
6.5.1 SRE 1,8/2 160 06-10-2027 14-01-2028 3.2.6
6.5.2 SRE 1,8/2 160 04-11-2027 14-01-2028 —
6.5.3 SRE 1,8/2 160 06-10-2027 25-11-2027 —
6.5.4 SRE 2/3 320 01-09-2027 14-01-2028 5.1.4,2.4.3,2.4.4;cuatrokitsal30-09-2027para4.1.4
6.5.5 SRE 1,8/2 160 04-11-2027 14-01-2028 —
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
87

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla17—continuación
Paquete Rol Personas(prom.
/máx.)
HH Inicio Fin Predecesoras(cuentaopaquete)
6.5.6 SRE 1,8/2 160 06-10-2027 14-01-2028 —
6.6.1 SRE 1,8/2 160 10-06-2027 30-06-2027 6.3.1–6.3.3(D-12)
6.6.2 RED 1,8/2 160 10-06-2027 30-06-2027 6.3.1–6.3.3(D-12)
6.6.3 RED 3,6/4 160 10-06-2027 18-06-2027 6.3.1–6.3.3(D-12)
7.1.1 IMP 1,8/2 160 02-11-2027 24-12-2027 —
7.1.6 IMP 1,8/2 160 02-11-2027 24-12-2027 —
7.2.2 IMP 1,8/2 160 02-05-2028 23-06-2028 —
7.2.3 IMP 1,8/2 160 01-03-2027 25-05-2027 —
7.3.1 IMP 1,8/2 160 01-02-2028 24-03-2028 —
7.3.2 IMP 1,8/2 160 03-07-2028 25-07-2028 —
9.1.1 DES 1,8/2 80 02-10-2028 11-10-2028 —
9.1.2 JP 1,8/2 80 26-10-2028 07-11-2028 4.3.3
9.2.2 SEG 1,8/2 80 01-09-2031 09-09-2031 —
2.4.3 SRE 2,7/3 341,33 01-04-2027 30-04-2027 5.1.4,5.3.4;prototipoGreengrassyTC58e
2.4.4 ARQ 2,5/3 240 03-05-2027 28-05-2027 2.4.3;CalidaddelCLIENTE
4.1.4 IMP 1,8/2 341,33 09-11-2027 20-12-2027 2.4.3,2.4.4,3.4.4,3.4.5,3.8.1yH4,5.3.4;cuatroactas
parciales6.5.4
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
88

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla17—continuación
Paquete Rol Personas(prom.
/máx.)
HH Inicio Fin Predecesoras(cuentaopaquete)
5.1.4 ARQ 1,8/2 240 01-02-2027 31-03-2027 EspecificaciónSD4;ochosemanasdehomologación
móvil
5.3.4 SRE 1,8/2 80 01-03-2027 12-03-2027 5.1.4(especificación,CC);serviciodebancoantesde
2.4.3
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
89

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla18 ActividadesdelospaquetesqueterminanhastaelH2.Fuente:elaboraciónapartirdelaTabla 17.Bloque1de2.
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
1.1.1.A01 Elaboración,revisióny
aprobacióndelentregable
JP 2 80 01-02-2027 09-02-2027 7 —
1.1.2.A01 Elaboración,revisióny
aprobacióndelentregable
JP 2 80 01-02-2027 09-02-2027 7 —
1.1.3.A01 Elaboración,revisióny
aprobacióndelentregable
JP 2 80 01-02-2027 09-02-2027 7 —
1.2.1.A01 Elaboración,revisióny
aprobacióndelentregable
ARQ 2 80 01-02-2027 09-02-2027 7 —
1.2.3.A01 Elaboración,revisióny
aprobacióndelentregable
ARQ 2 80 01-02-2027 09-02-2027 7 —
1.2.4.A01 Elaboración,revisióny
aprobacióndelentregable
CAL 2 80 01-03-2027 09-03-2027 7 —
1.3.1.A01 Elaboración,revisióny
aprobacióndelentregable
JP 2 80 10-02-2027 18-02-2027 7 —
1.3.2.A01 Elaboración,revisióny
aprobacióndelentregable
JP 2 80 01-03-2027 09-03-2027 7 —
1.3.3.A01 Elaboración,revisióny
aprobacióndelentregable
JP 2 80 01-03-2027 09-03-2027 7 —
1.3.4.A01 Elaboración,revisióny
aprobacióndelentregable
JP 2 80 01-03-2027 09-03-2027 7 —
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
90

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla18—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
1.4.1.A01 Elaboración,revisióny
aprobacióndelentregable
JP 2 80 01-02-2027 09-02-2027 7 —
1.4.2.A01 Elaboración,revisióny
aprobacióndelentregable
JP 2 80 01-02-2027 09-02-2027 7 —
1.5.1.A01 Elaboración,revisióny
aprobacióndelentregable
CAL 2 80 01-03-2027 09-03-2027 7 —
1.6.1.A01 Elaboración,revisióny
aprobacióndelentregable
JP 2 80 01-03-2027 09-03-2027 7 —
1.7.1.A01 Elaboración,revisióny
aprobacióndelentregable
JP 2 80 01-04-2027 09-04-2027 7 —
1.9.1.A01 Elaboración,revisióny
aprobacióndelentregable
SEG 2 80 01-02-2027 09-02-2027 7 —
1.9.2.A01 Elaboración,revisióny
aprobacióndelentregable
SEG 2 80 01-02-2027 09-02-2027 7 —
1.9.3.A01 Elaboración,revisióny
aprobacióndelentregable
SEG 2 80 01-03-2027 09-03-2027 7 —
2.1.1.A01 Levantamientodeinsu-
mosyanálisis
ARQ 2 80 01-03-2027 09-03-2027 7 1.2.1.A01
2.1.1.A02 Elaboracióndelentrega-
ble
ARQ 2 80 10-03-2027 18-03-2027 7 2.1.1.A01
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
91

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla18—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.1.1.A03 Revisión,correccióny
presentaciónparaaproba-
ción
ARQ 2 80 19-03-2027 29-03-2027 7 2.1.1.A02
2.1.2.A01 Levantamientodeinsu-
mosyanálisis
ARQ 2 80 01-03-2027 09-03-2027 7 —
2.1.2.A02 Elaboracióndelentrega-
ble
ARQ 2 80 10-03-2027 18-03-2027 7 2.1.2.A01
2.1.2.A03 Revisión,correccióny
presentaciónparaaproba-
ción
ARQ 2 80 19-03-2027 29-03-2027 7 2.1.2.A02
2.1.3.A01 Levantamientodeinsu-
mosyanálisis
DAT 2 80 01-03-2027 09-03-2027 7 —
2.1.3.A02 Elaboracióndelentrega-
ble
DAT 2 80 10-03-2027 18-03-2027 7 2.1.3.A01
2.1.3.A03 Revisión,correccióny
presentaciónparaaproba-
ción
DAT 2 80 19-03-2027 29-03-2027 7 2.1.3.A02
2.2.1.A01 Levantamientodeinsu-
mosyanálisis
SEG 2 80 01-03-2027 09-03-2027 7 —
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
92

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla18—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.2.1.A02 Elaboracióndelentrega-
ble
SEG 2 80 10-03-2027 18-03-2027 7 2.2.1.A01
2.2.1.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SEG 2 80 19-03-2027 29-03-2027 7 2.2.1.A02
2.2.3.A01 Levantamientodeinsu-
mosyanálisis
SEG 4 80 01-04-2027 06-04-2027 4 —
2.2.3.A02 Elaboracióndelentrega-
ble
SEG 4 80 07-04-2027 12-04-2027 4 2.2.3.A01
2.2.3.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SEG 4 80 13-04-2027 16-04-2027 4 2.2.3.A02
2.2.4.A01 Levantamientodeinsu-
mosyanálisis
SEG 2 80 01-03-2027 09-03-2027 7 —
2.2.4.A02 Elaboracióndelentrega-
ble
SEG 2 80 10-03-2027 18-03-2027 7 2.2.4.A01
2.2.4.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SEG 2 80 19-03-2027 29-03-2027 7 2.2.4.A02
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
93

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla18—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.3.1.A01 Levantamientodeinsu-
mosyanálisis
SRE 2 80 01-02-2027 09-02-2027 7 —
2.3.1.A02 Elaboracióndelentrega-
ble
SRE 2 80 10-02-2027 18-02-2027 7 2.3.1.A01
2.3.1.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SRE 2 80 19-02-2027 01-03-2027 7 2.3.1.A02
2.3.2.A01 Levantamientodeinsu-
mosyanálisis
SRE 2 80 01-02-2027 09-02-2027 7 —
2.3.2.A02 Elaboracióndelentrega-
ble
SRE 2 80 10-02-2027 18-02-2027 7 2.3.2.A01
2.3.2.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SRE 2 80 19-02-2027 01-03-2027 7 2.3.2.A02
2.3.3.A01 Levantamientodeinsu-
mosyanálisis
SRE 2 80 01-03-2027 09-03-2027 7 —
2.3.3.A02 Elaboracióndelentrega-
ble
SRE 2 80 10-03-2027 18-03-2027 7 2.3.3.A01
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
94

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla18—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.3.3.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SRE 2 80 19-03-2027 29-03-2027 7 2.3.3.A02
2.4.1.A01 Levantamientodeinsu-
mosyanálisis
ARQ 5 80 19-04-2027 21-04-2027 3 2.1.1.A03,2.1.2.A03,
2.1.3.A03,2.2.1.A03,
2.2.3.A03,2.2.4.A03
2.4.1.A02 Elaboracióndelentrega-
ble
ARQ 5 80 22-04-2027 26-04-2027 3 2.4.1.A01
2.4.1.A03 Revisión,correccióny
presentaciónparaaproba-
ción
ARQ 5 80 27-04-2027 29-04-2027 3 2.4.1.A02
2.5.1.A01 Levantamientodeinsu-
mosyanálisis
SRE 2 80 01-04-2027 09-04-2027 7 —
2.5.1.A02 Elaboracióndelentrega-
ble
SRE 2 80 12-04-2027 20-04-2027 7 2.5.1.A01
2.5.1.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SRE 2 80 21-04-2027 29-04-2027 7 2.5.1.A02
2.5.2.A01 Levantamientodeinsu-
mosyanálisis
SRE 2 80 01-04-2027 09-04-2027 7 —
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
95

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla18—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.5.2.A02 Elaboracióndelentrega-
ble
SRE 2 80 12-04-2027 20-04-2027 7 2.5.2.A01
2.5.2.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SRE 2 80 21-04-2027 29-04-2027 7 2.5.2.A02
Tabla19 ActividadesdelospaquetesqueterminanhastaelH2.Fuente:elaboraciónapartirdelaTabla 17.Bloque2de2.
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.6.1.A01 Levantamientodeinsu-
mosyanálisis
IMP 2 80 01-03-2027 09-03-2027 7 —
2.6.1.A02 Elaboracióndelentrega-
ble
IMP 2 80 10-03-2027 18-03-2027 7 2.6.1.A01
2.6.1.A03 Revisión,correccióny
presentaciónparaaproba-
ción
IMP 2 80 19-03-2027 29-03-2027 7 2.6.1.A02
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
96

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla19—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.6.2.A01 Levantamientodeinsu-
mosyanálisis
IMP 2 80 01-04-2027 09-04-2027 7 —
2.6.2.A02 Elaboracióndelentrega-
ble
IMP 2 80 12-04-2027 20-04-2027 7 2.6.2.A01
2.6.2.A03 Revisión,correccióny
presentaciónparaaproba-
ción
IMP 2 80 21-04-2027 29-04-2027 7 2.6.2.A02
2.6.3.A01 Levantamientodeinsu-
mosyanálisis
IMP 2 80 03-05-2027 11-05-2027 7 —
2.6.3.A02 Elaboracióndelentrega-
ble
IMP 2 80 12-05-2027 20-05-2027 7 2.6.3.A01
2.6.3.A03 Revisión,correccióny
presentaciónparaaproba-
ción
IMP 2 80 21-05-2027 31-05-2027 7 2.6.3.A02
3.1.4.A01 Levantamientodeinsu-
mosyanálisis
SRE 2 80 03-05-2027 11-05-2027 7 —
3.1.4.A02 Elaboracióndelentrega-
ble
SRE 2 80 12-05-2027 20-05-2027 7 3.1.4.A01
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
97

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla19—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
3.1.4.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SRE 2 80 21-05-2027 31-05-2027 7 3.1.4.A02
3.2.1.A01 Levantamientodeinsu-
mosyanálisis
SRE 2 80 03-05-2027 11-05-2027 7 5.2.1.A01
3.2.1.A02 Elaboracióndelentrega-
ble
SRE 2 80 12-05-2027 20-05-2027 7 3.2.1.A01
3.2.1.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SRE 2 80 21-05-2027 31-05-2027 7 3.2.1.A02
3.2.2.A01 Levantamientodeinsu-
mosyanálisis
SRE 2 80 03-05-2027 11-05-2027 7 5.2.1.A01
3.2.2.A02 Elaboracióndelentrega-
ble
SRE 2 80 12-05-2027 20-05-2027 7 3.2.2.A01
3.2.2.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SRE 2 80 21-05-2027 31-05-2027 7 3.2.2.A02
3.2.3.A01 Levantamientodeinsu-
mosyanálisis
SRE 2 80 03-05-2027 11-05-2027 7 5.2.1.A01
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
98

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla19—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
3.2.3.A02 Elaboracióndelentrega-
ble
SRE 2 80 12-05-2027 20-05-2027 7 3.2.3.A01
3.2.3.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SRE 2 80 21-05-2027 31-05-2027 7 3.2.3.A02
3.2.4.A01 Levantamientodeinsu-
mosyanálisis
SRE 2 80 03-05-2027 11-05-2027 7 5.2.1.A01
3.2.4.A02 Elaboracióndelentrega-
ble
SRE 2 80 12-05-2027 20-05-2027 7 3.2.4.A01
3.2.4.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SRE 2 80 21-05-2027 31-05-2027 7 3.2.4.A02
3.2.5.A01 Levantamientodeinsu-
mosyanálisis
SEG 2 80 03-05-2027 11-05-2027 7 5.2.1.A01
3.2.5.A02 Elaboracióndelentrega-
ble
SEG 2 80 12-05-2027 20-05-2027 7 3.2.5.A01
3.2.5.A03 Revisión,correccióny
presentaciónparaaproba-
ción
SEG 2 80 21-05-2027 31-05-2027 7 3.2.5.A02
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
99

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla19—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
3.10.2.1.A01 Levantamientodeinsu-
mosyanálisis
CAL 2 80 01-03-2027 09-03-2027 7 —
3.10.2.1.A02 Elaboracióndelentrega-
ble
CAL 2 80 22-03-2027 30-03-2027 7 3.10.2.1.A01
3.10.2.1.A03 Revisión,correccióny
presentaciónparaaproba-
ción
CAL 2 80 12-04-2027 20-04-2027 7 3.10.2.1.A02
5.1.1.A01 Elaboración,revisióny
aprobacióndelentregable
ARQ 2 80 01-03-2027 09-03-2027 7 —
5.1.2.A01 Elaboración,revisióny
aprobacióndelentregable
ARQ 2 80 02-03-2027 10-03-2027 7 2.3.1.A03,2.3.2.A03
5.2.1.A01 Elaboración,revisióny
aprobacióndelentregable
SRE 2 80 01-03-2027 09-03-2027 7 —
5.2.2.A01 Elaboración,revisióny
aprobacióndelentregable
SRE 2 80 03-05-2027 11-05-2027 7 —
5.2.3.A01 Elaboración,revisióny
aprobacióndelentregable
ARQ 2 80 03-05-2027 11-05-2027 7 —
5.3.1.A01 Elaboración,revisióny
aprobacióndelentregable
SRE 2 80 03-05-2027 11-05-2027 7 —
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
100

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla19—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
5.3.2.A01 Elaboración,revisióny
aprobacióndelentregable
SRE 2 80 03-05-2027 11-05-2027 7 —
5.3.3.A01 Elaboración,revisióny
aprobacióndelentregable
SRE 2 80 03-05-2027 11-05-2027 7 —
6.1.1.A01 Preparaciónyejecución
delainstalaciónodela
capacitación
SRE 2 80 01-04-2027 09-04-2027 7 5.1.2.A01
6.1.1.A02 Pruebaoevaluación,
correcciónyacta
SRE 2 80 12-04-2027 20-04-2027 7 6.1.1.A01
6.1.2.A01 Preparaciónyejecución
delainstalaciónodela
capacitación
SRE 2 80 01-04-2027 09-04-2027 7 5.1.2.A01
6.1.2.A02 Pruebaoevaluación,
correcciónyacta
SRE 2 80 12-04-2027 20-04-2027 7 6.1.2.A01
6.1.3.A01 Preparaciónyejecución
delainstalaciónodela
capacitación
SRE 2 80 01-04-2027 09-04-2027 7 5.1.2.A01
6.1.3.A02 Pruebaoevaluación,
correcciónyacta
SRE 2 80 12-04-2027 20-04-2027 7 6.1.3.A01
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
101

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla19—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
6.1.4.A01 Preparaciónyejecución
delainstalaciónodela
capacitación
SRE 2 80 01-04-2027 09-04-2027 7 5.1.2.A01
6.1.4.A02 Pruebaoevaluación,
correcciónyacta
SRE 2 80 12-04-2027 20-04-2027 7 6.1.4.A01
6.1.5.A01 Preparaciónyejecución
delainstalaciónodela
capacitación
SRE 2 80 03-05-2027 11-05-2027 7 5.1.2.A01,
6.1.1.A02–6.1.4.A02
6.1.5.A02 Pruebaoevaluación,
correcciónyacta
SRE 2 80 12-05-2027 20-05-2027 7 6.1.5.A01
6.2.1.A01 Preparaciónyejecución
delainstalaciónodela
capacitación
SRE 2 80 03-05-2027 11-05-2027 7 —
6.2.1.A02 Pruebaoevaluación,
correcciónyacta
SRE 2 80 12-05-2027 20-05-2027 7 6.2.1.A01
6.3.3.A01 Preparaciónyejecución
delainstalaciónodela
capacitación
SRE 2 80 03-05-2027 11-05-2027 7 —
6.3.3.A02 Pruebaoevaluación,
correcciónyacta
SRE 2 80 12-05-2027 20-05-2027 7 6.3.3.A01
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
102

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla19—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
7.2.3.A01 Preparaciónyejecución
delainstalaciónodela
capacitación
IMP 2 80 01-03-2027 09-03-2027 7 —
7.2.3.A02 Pruebaoevaluación,
correcciónyacta
IMP 2 80 17-05-2027 25-05-2027 7 7.2.3.A01
2.4.3.A01 Montajedeprototipoy
lecturaModbus/Green-
grass
SRE 3 80 01-04-2027 07-04-2027 5 5.1.4,5.3.4
2.4.3.A02 Alarmas,satéliteysegun-
daevaluación
SRE 3 80 08-04-2027 14-04-2027 5 2.4.3.A01
2.4.3.A03 Fallas,órdenes,persisten-
ciayrecuperación
SRE 3 80 15-04-2027 21-04-2027 5 2.4.3.A02
2.4.3.A04 Regresión,correccionesy
actadebanco
SRE 3 80 22-04-2027 28-04-2027 5 2.4.3.A03
2.4.4.A01 Preparacióndemapeoy
cargadeensayo
ARQ 3 80 03-05-2027 07-05-2027 5 2.4.3
2.4.4.A02 Comparacióndenúcleo,
simuladoresyaire
ARQ 3 80 10-05-2027 14-05-2027 5 2.4.4.A01
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
103

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla19—continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.4.4.A03 Puntocrítico,volumen,
toleranciasyactacon
Calidad
ARQ 3 80 17-05-2027 21-05-2027 5 2.4.4.A02
5.1.4.A01 Especificación,cotización
localysolicituddeho-
mologacióndesdeel1de
febrero
ARQ 2 80 01-02-2027 09-02-2027 7 EspecificaciónSD4
5.1.4.A02 Evaluacióndeproveedor
yseguimientodehomolo-
gación
ARQ 2 80 10-02-2027 18-02-2027 7 5.1.4.A01
5.1.4.A03 Verificacióndecertifica-
dosycompradeprototipo
ARQ 2 80 23-03-2027 31-03-2027 7 5.1.4.A02;ochosemanas
desdeiniciodegestión
5.3.4.A01 ContratosmóvilesySBD
yhabilitacióndelservicio
debanco
SRE 2 80 01-03-2027 09-03-2027 7 5.1.4.A01(especificación)
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
104

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Secuenciaquincenaldeconstrucción:recepción(3.4.1). El paquete de recepción se desglosa
en la siguiente secuencia de trabajo dentro de su ventana de junio a agosto de 2027. Al co-
mienzo de cada iteración se prioriza el trabajo en Kanban; al cierre, Desarrollo y Calidad
ejecutanlaspruebasdelincremento,registrandefectosydemuestranelresultadoenQA.Estas
demostracionesnoautorizanunpasoaProducción.
• 10–23 de junio: contrato de recepción e interfaces de producto, lote y unidad logística;
revisióndelcontratoconInventario.
• 24dejunio–7dejulio:capturaderecepciónyvalidacióndeproducto,loteyvencimiento;
demostracióndelflujoprincipalydeunrechazo.
• 8–21dejulio:registrodediferencias,retencionesyreintentos;demostracióndequeun
reenvíonoduplicalarecepción.
• 22dejulio–4deagosto:integraciónconInventarioytrazabilidad,conconciliaciónyregre-
siónenQA.
• 5–10deagosto:cierrededefectosdelincrementoyentregadelpaqueteenQA.
Preparaciónpuedeavanzarcondatosdepruebaunavezaprobadoelcontratoderecepción
einventario;supruebaintegradaesperalosincrementosdisponiblesenQA,segúnD-16.Las
pruebas ampliadas de 3.8 y 3.9 certifican el conjunto tras las pruebas de cada incremento.
Lasfechasanterioresdetallanelpaquete3.4.1;losdemásmódulossiguenlamismacadencia
dentrodesuventanadelacarta,conloshitosdeinterfazdelAnexo7.B.
Calendariodeiteracionesdelosmódulos. LaTabla 20dividelaventanadecadamóduloenla
cartaeniteracionesdehasta14díascalendario.Enelprimerintervaloserevisancontratosy
criteriosdeaceptación;cadaintervalointermedioterminacondemostracióndelincremento
ypruebasderegresiónaplicables;elúltimoentregalaversiónintegradaenQA.Cuandoun
contratoounaentregaprecedenteaúnnoestádisponible,sepriorizanpreparaciónypruebas
condatoscontrolados,ysemantienebloqueadalaintegraciónreal.Alcierredecadaiteración
serealizalarevisióndelincrementoconelLíderFuncional;laspruebasdecontrato,integración
yregresióndelincrementoformanpartedelaiteración,ylaspruebasampliadasde3.8y3.9
certificanelconjunto.
Tabla20 Iteracionesdeconstruccióndelosmódulossegúnlacarta(día/mes).
Paquete Año Ventanasdeiteración
3.4.1 2027 10/06–23/06,24/06–07/07,08/07–21/07,22/07–04/08,05/08–10/08
3.4.2 2027 10/06–23/06,24/06–07/07,08/07–21/07,22/07–04/08,05/08–11/08
3.4.3 2027 14/06–27/06,28/06–11/07,12/07–25/07,26/07–08/08,09/08–18/08
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
105

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla20—continuación
Paquete Año Ventanasdeiteración
3.4.4 2027 14/06–27/06,28/06–11/07,12/07–25/07,26/07–08/08,09/08–22/08,23/08–05/09,
06/09–19/09,20/09–29/09
3.4.5 2027 14/06–27/06,28/06–11/07,12/07–25/07,26/07–08/08,09/08–22/08,23/08–30/08
3.4.6 2027 16/06–29/06,30/06–13/07,14/07–27/07,28/07–10/08,11/08–17/08
3.4.7 2027 16/06–29/06,30/06–13/07,14/07–27/07,28/07–10/08,11/08–24/08,25/08–08/09
3.4.8 2027 16/06–29/06,30/06–13/07,14/07–27/07,28/07–10/08,11/08–24/08,25/08–09/09
3.4.9 2027 18/06–01/07,02/07–15/07,16/07–29/07,30/07–12/08,13/08–26/08,27/08–09/09,
10/09–23/09,24/09–30/09
3.4.10 2027 10/06–23/06,24/06–07/07,08/07–21/07,22/07–04/08,05/08–18/08,19/08–01/09,
02/09–15/09,16/09–29/09,30/09–04/10
3.4.11 2027 02/09–15/09,16/09–27/09
3.5.1 2028 15/03–28/03,29/03–11/04,12/04–28/04
3.5.2 2028 15/03–28/03,29/03–11/04,12/04–28/04
3.5.3 2028 15/03–28/03,29/03–11/04,12/04–28/04
3.5.4 2028 15/03–28/03,29/03–11/04,12/04–28/04
6.2 Paquetesdeesfuerzocontinuo
Lospaquetesrecurrentes(R),deacompañamiento(A)ydecobertura(C)sondenivelde
esfuerzo:noproducenunentregableúnico,sinounservicioounareuniónqueserepite.No
sedividenenentregablesmáspequeños,sinoporocurrenciaoporquincena:
• UnpaqueteconfrecuenciapropiaeneldiccionariodelT-14(quincenal,mensual,trimestral,
semestraloanual)tieneunaactividadporocurrencia,ejecutadadentrodeunaquincena.
Siunaocurrenciasupera64HH,sereparteentredosomáspersonas.
• Unpaquetecontinuotieneunaactividadporquincena.Silaquincenaexigemásde64HH,
laactividadsedivideenrelevosopuestos:porejemplo,elNOC24 ×7deunmesde31días
requiere744 ÷2=372HHporquincena,esdecir,seisrelevosde62HH.
• Laspreparacionesdecomitésconfrecuenciacontractualquincenal(1.6.2y1.8.3)tienen
menosde8HHporocurrencia.Sonlaúnicaexcepciónalmínimodelaregla:semantienen
porocurrenciaporquelacadencialafijaelartículo71delasBasesAdministrativas(p.37)y
noconvienefusionarlasconotraactividad.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
106

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Estos59paquetesnosedescomponenenunalistadeactividadesdistintas,porquesutrabajo
serepite:seprogramanporquincenauocurrencia,enrelevosdehasta64HHcadauno.La
Tabla21presentalaregladecadapaquete,elnúmeroderelevosuocurrenciasqueprograma
duranteelcontratoyelesfuerzomáximodecadauno.
Laconciliacióndelinventariodepaquetessepara139.538,20HHdelos59paquetescon-
tinuos y 47.144,83 HH de los 168 con entregable. No hay códigos duplicados entre ambos
grupos;juntosreproducenlas186.683,03HHdelos227paquetes.Aestasseañaden128HHde
restauraciones,9.336HHdesoportepuentey3.072HHdereservaprotegida,parauntotalde
199.219,03HH.Estecrucevalidaelesfuerzo,mientrasquelacoberturadiariaseverificaconel
registrodepersonasyturnosdescritoenlasección5.7.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
107

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla21 Actividadesdelospaquetesdeesfuerzocontinuo.Fuente:elaboraciónapartirdelassecciones4.1,4.2y4.4yeldiccionariode(FormularioT-14).
Paquete Clase Rol Meses EHH Regladeprogramación Relevosu
ocurrencias
programados
HHmáximas
porrelevou
ocurrencia
1.2.2 G IMP 1–3 80 Unaactividadporquincena,porpresenciacontinuao
periódica
6 13.3
1.3.5 R JP 1–20 480 Unaactividaddeniveldeesfuerzoporquincena 40 12.0
1.4.3 R JP 1–56 896 Unaactividaddeniveldeesfuerzoporquincena 112 8.0
1.5.2 G CAL 6–20 80 Unaactividadcada3quincenas,porpresenciacontinua
operiódica
10 8.0
1.6.2 R JP 1–20 160 Unaactividadporocurrencia(quincenal,encada
ComitédeProyecto),ejecutadadentrodeunaquincena;
1actividad(es)porocurrencia
40 4.0
1.8.1 R JP 1–20 320 Unaactividaddeniveldeesfuerzoporquincena 40 8.0
1.8.2 R JP 1–56 448 Unaactividadporocurrencia(mensual),ejecutada
dentrodeunaquincena;1actividad(es)porocurrencia
56 8.0
1.8.3 R JP 1–20 240 Unaactividadporocurrencia(quincenal),ejecutada
dentrodeunaquincena;1actividad(es)porocurrencia
40 6.0
1.8.4 R ARQ 1–56 448 Unaactividadporocurrencia(mensual),ejecutada
dentrodeunaquincena;1actividad(es)porocurrencia
56 8.0
1.8.5 R SRE 13–56 352 Unaactividadporocurrencia(mensual),ejecutada
dentrodeunaquincena;1actividad(es)porocurrencia
44 8.0
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
108

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla21—continuación
Paquete Clase Rol Meses EHH Regladeprogramación Relevosu
ocurrencias
programados
HHmáximas
porrelevou
ocurrencia
1.8.6 R JP 1–20 480 Unaactividadporocurrencia(mensual),ejecutada
dentrodeunaquincena;1actividad(es)porocurrencia
20 24.0
1.8.7 R JP 2–56 440 Unaactividadcada2quincenas,ejecutadaenlaúltima
quincenadelgrupo
55 8.0
1.8.8 R JP 1–56 448 Unaactividadcada2quincenas,ejecutadaenlaúltima
quincenadelgrupo
56 8.0
1.9.4 R SEG 1–56 224 Unaactividadporocurrencia(anual),ejecutadadentro
deunaquincena;1actividad(es)porocurrencia
5 44.8
1.9.5 R JP 1–56 224 Unaactividadcada4quincenas,ejecutadaenlaúltima
quincenadelgrupo
28 8.0
2.2.2 E SEG 3–10 240 Unaactividadporquincena,porpresenciacontinuao
periódica
16 15.0
3.11.1 G ARQ 15–21 80 Unaactividadcada2quincenas,porpresenciacontinua
operiódica
7 11.4
3.11.2 G SRE 10–20 80 Unaactividadcada3quincenas,porpresenciacontinua
operiódica
8 10.0
3.11.3 G DES 4–20 80 Unaactividadcada4quincenas,porpresenciacontinua
operiódica
9 8.9
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
109

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla21—continuación
Paquete Clase Rol Meses EHH Regladeprogramación Relevosu
ocurrencias
programados
HHmáximas
porrelevou
ocurrencia
3.11.4 G DES 4–20 80 Unaactividadcada4quincenas,porpresenciacontinua
operiódica
9 8.9
3.11.5 G DES 6–20 80 Unaactividadcada3quincenas,porpresenciacontinua
operiódica
10 8.0
4.2.1 A IMP 13–15 7392 Unaactividaddeniveldeesfuerzoporquincena,dividi-
daen20relevosopuestos
120 61.6
4.2.2 A IMP 16–20 5408 Unaactividaddeniveldeesfuerzoporquincena,dividi-
daenrelevosopuestossegúnlaHHdecadames
92 61.6
4.3.1 A IMP 19–20 4928 Unaactividaddeniveldeesfuerzoporquincena,dividi-
daen20relevosopuestos
80 61.6
4.3.2 A IMP 21–22 2464 Unaactividaddeniveldeesfuerzoporquincena,dividi-
daenrelevosopuestossegúnlaHHdecadames
40 62.1
7.1.2 R IMP 13–56 2816 Unaactividaddeniveldeesfuerzoporquincena 88 32.0
7.1.3 T IMP 11–20 240 Unaactividadporquincena,porpresenciacontinuao
periódica
20 12.0
7.1.4 T IMP 15–20 160 2ocurrenciasenlaventana,porpresenciacontinuao
periódica
2 80.0
7.1.5 T IMP 10–18 160 2ocurrenciasenlaventana,porpresenciacontinuao
periódica
2 80.0
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
110

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla21—continuación
Paquete Clase Rol Meses EHH Regladeprogramación Relevosu
ocurrencias
programados
HHmáximas
porrelevou
ocurrencia
7.2.1 T IMP 10–16 160 Unaactividadporquincena,porpresenciacontinuao
periódica
14 11.4
7.2.4 T IMP 8–20 240 Unaactividadporquincena,porpresenciacontinuao
periódica
26 9.24
7.2.5 T IMP 13–21 160 Unaactividadporquincena,porpresenciacontinuao
periódica
18 8.9
8.1.1 C SRE 21–56 21764.2 Unaactividaddeniveldeesfuerzoporquincena,dividi-
daenrelevosopuestossegúnlaHHdecadames
380 64.0
8.1.2 C SRE 21–56 38246 Unaactividaddeniveldeesfuerzoporquincena,dividi-
daenrelevosopuestossegúnlaHHdecadames
624 63.4
8.1.3 V SRE 21–56 560 Sietecampañasdeconmutaciónrealde80HH,con
cincoactividadesporcampaña
35 16.0
8.1.4 R JP 21–56 288 Unaactividadporocurrencia(anual),ejecutadadentro
deunaquincena;2actividad(es)porocurrencia
6 48.0
8.1.5 C SEG 13–56 32112 Unaactividaddeniveldeesfuerzoporquincena,dividi-
daenrelevosopuestossegúnlaHHdecadames
528 62.0
8.1.6 R SRE 21–56 576 Unaactividadporocurrencia(mensual),ejecutada
dentrodeunaquincena;1actividad(es)porocurrencia
36 16.0
8.2.1 R DES 21–56 4608 Unaactividaddeniveldeesfuerzoporquincena 72 64.0
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
111

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla21—continuación
Paquete Clase Rol Meses EHH Regladeprogramación Relevosu
ocurrencias
programados
HHmáximas
porrelevou
ocurrencia
8.2.2 R SEG 21–56 1152 Unaactividaddeniveldeesfuerzoporquincena 72 16.0
8.2.3 R SRE 21–56 1152 Unaactividaddeniveldeesfuerzoporquincena 72 16.0
8.2.4 R DES 21–56 2304 Unaactividaddeniveldeesfuerzoporquincena 72 32.0
8.2.5 R SRE 21–56 288 Unaactividadporocurrencia(anual),ejecutadadentro
deunaquincena;2actividad(es)porocurrencia
6 48.0
8.2.6 R SRE 21–56 288 Unaactividadporocurrencia(semestral),ejecutada
dentrodeunaquincena;1actividad(es)porocurrencia
6 48.0
8.2.7 R SRE 21–56 864 Unaactividaddeniveldeesfuerzoporquincena 72 12.0
8.3.1 R CAL 21–56 576 Unaactividaddeniveldeesfuerzoporquincena 72 8.0
8.3.2 R DAT 21–56 288 Unaactividadporocurrencia(semestral),ejecutada
dentrodeunaquincena;1actividad(es)porocurrencia
6 48.0
8.3.3 G JP 21–23 80 3ocurrenciasenlaventana,porpresenciacontinuao
periódica
3 26.7
8.3.4 R JP 24–56 528 Unaactividadporocurrencia(mensual),ejecutada
dentrodeunaquincena;1actividad(es)porocurrencia
33 16.0
8.3.5 G IMP 22–26 80 Unaactividadporquincena,porpresenciacontinuao
periódica
10 8.0
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
112

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla21—continuación
Paquete Clase Rol Meses EHH Regladeprogramación Relevosu
ocurrencias
programados
HHmáximas
porrelevou
ocurrencia
8.3.6 G IMP 24–27 80 Unaactividadporquincena,porpresenciacontinuao
periódica
8 10.0
8.4.1 R SRE 21–56 576 Unaactividadporocurrencia(trimestral),ejecutada
dentrodeunaquincena;1actividad(es)porocurrencia
12 48.0
8.4.2 R SRE 21–56 576 Unaactividadporocurrencia(mensual),ejecutada
dentrodeunaquincena;1actividad(es)porocurrencia
36 16.0
8.4.3 R SRE 21–56 288 Unaactividadporocurrencia(anual),ejecutadadentro
deunaquincena;2actividad(es)porocurrencia
6 48.0
8.4.4 R JP 21–56 288 Unaactividadporocurrencia(semestral),ejecutada
dentrodeunaquincena;1actividad(es)porocurrencia
6 48.0
8.5.1 R IMP 21–56 1152 Unaactividadporocurrencia(dosjornadasporaño),
ejecutadadentrodeunaquincena;3actividad(es)por
ocurrencia
18 64.0
8.5.2 G IMP 21–27 80 Unaactividadcada2quincenas,porpresenciacontinua
operiódica
7 11.4
8.5.3 R SRE 21–56 576 Unaactividaddeniveldeesfuerzoporquincena 72 8.0
9.2.1 G JP 54–56 80 Unaactividadporquincena,porpresenciacontinuao
periódica
6 13.3
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
113

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Así,los227paquetesquedanprogramadosdedosformas:los168paquetesconentregable,
confechasenlaTabla 17yactividadesde80HHomenosdetalladashastaelH2yluegopor
planificacióngradual,y59paquetesdeesfuerzocontinuoqueseprogramanporquincenau
ocurrencia,enrelevosdehasta64HHcadauno.Enamboscasosnadasuperaunaquincena.
Ningúnpaqueteseinformaal50%durantesemanas:elavancedecadaquincenasemidepor
lasactividadesterminadasyporlosrelevosuocurrenciascumplidos,quealimentanelvalor
ganadodelSD6,sección6.1.5.
6.3 Perfilesyesfuerzoparalavalorización
La Tabla22 desglosa 37 perfiles, contando Senior y Junior por separado, e identifica su
categoría E-26, el esfuerzo por fase y las plazas propuestas. Las diez funciones mínimas de
BTT19.2permanecenidentificadas.LoscódigosdeorigenING,ARQ,NOC,SRE,CAL,SEGe
IMPremitenalossietegrupostécnicosdelSD1,incluidaeláreadeImplantaciónyGestión
del Cambio; OF identifica a los asistentes de terreno contratados por obra o faena para la
implantación;lacapacidadylascondicionesdeasignaciónsecontrastanen5.7.
Horas y jornadas.Las HH son el esfuerzo acumulado del equipo de cada perfil, no de una
solapersona.Lasjornadasequivalentesdeochohorassecalculancomo 𝐷𝑒𝑞 = 𝐻𝐻/8.Sonuna
unidaddeesfuerzoparalavalorización:nosondíastranscurridos,díaslaborablesconsecutivos
niduracióndelGantt.Seconservanlosdecimalesdelcálculo;noseredondeacadaperfila
jornadasenteras.
Con 𝑛 personas del mismo perfil, el esfuerzo medio por persona es𝐻𝐻/𝑛, equivalente
a 𝐷𝑒𝑞/𝑛jornadascompletas.Estonosuponequetodastrabajenajornadacompletadurante
todalaventana.Laduraciónyladedicacióndecadaactividadseobtienendelcalendarioylas
precedenciasdelassecciones5y6.1,ylacapacidaddisponiblesecontrastaconlas128HH
efectivasporpersonaymesde4.1.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
114

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla22 Perfiles,plazaspropuestasyjornadasequivalentesporfase.Fuente:elaboraciónapartirdelasHHdelaEDTdelT-14ydelT-15;SD1,Tabla1.3;yBA,
FormularioE-26.
Cód. Origen
pro-
puesto
Perfil CategoríaE-26 Plazas
pro-
pues-
tas
HHimplem. Jornadas
implem.
HH/8
HHoper. Jornadas
oper.HH/8
01 ING JefedeProyecto JefedeProyecto 1 1.377,2 172,15 996,8 124,6
20 ING AnalistaPMO,documentaciónycom-
pras
Analista/Diseña-
dorSenior
2 3.714 464,25 2.244,8 280,6
02 ARQ LíderdeIntegración JefedeTIC 1 947,93 118,4914 57,6 7,2
03S ARQ ArquitectodeSoluciónSenior ArquitectoSenior 2 1.984,02 248,0025 153,6 19,2
03J ARQ ArquitectodeSoluciónJunior ArquitectoJunior 1 991,98 123,9975 76,8 9,6
05 ARQ LíderFuncional JefedeAnálisisy
Diseño
1 144 18 0 0
06S ARQ AnalistaFuncionalyUXSenior Analista/Diseña-
dorSenior
1 557,34 69,6675 0 0
06J ARQ AnalistaFuncionalyUXJunior Analista/Diseña-
dorJunior
1 278,66 34,8325 0 0
12S ARQ IngenierodeIntegraciónSenior IngenieroSenior 2 2.538,72 317,3399 0 0
12J ING IngenierodeIntegraciónJunior IngenieroJunior 2 1.269,35 158,6687 0 0
04 ING LíderdeDesarrollo JefedeDesarrollo 1 1.616 202 691,2 86,4
07S ING DesarrolladorMóvilSenior IngenieroSenior 4 1.979,97 247,4959 460,8 57,6
07J ING DesarrolladorMóvilJunior IngenieroJunior 2 989,98 123,7473 230,4 28,8
08S ING DesarrolladorFront-endSenior IngenieroSenior 3 1.322,31 165,289 691,2 86,4
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
115

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla22—continuación
Cód. Origen
pro-
puesto
Perfil CategoríaE-26 Plazas
pro-
pues-
tas
HHimplem. Jornadas
implem.
HH/8
HHoper. Jornadas
oper.HH/8
08J ING DesarrolladorFront-endJunior IngenieroJunior 3 1.322,31 165,289 691,2 86,4
09S ING DesarrolladorBack-endSenior IngenieroSenior 9 4.743,66 592,9576 2.488,32 311,04
09J ING DesarrolladorBack-endJunior IngenieroJunior 6 3.162,44 395,305 1.658,88 207,36
23 ARQ LíderdeDatos IngenieroExperto 1 1.326,7 165,8375 57,6 7,2
10S ARQ IngenierodeDatosyBasesSenior IngenierodeDatos 3 3.537,87 442,2333 153,6 19,2
10J ARQ IngenierodeDatosyBasesJunior IngenierodeDatos 2 1.768,93 221,1167 76,8 9,6
16 CAL LíderdeCalidadyPruebas AnalistaQAExper-
to
1 414 51,75 43,2 5,4
19S CAL AnalistaQASenior AnalistaQASenior 9 3.523,82 440,4775 399,27 49,90875
19J ING AnalistaQAJunior AnalistaQAJunior 3 1.166,18 145,7725 133,53 16,69125
21 IMP LíderdeImplantaciónyGestióndel
Cambio
JefedeAnálisisy
Diseño
1 1.314,05 164,2563 220,8 27,6
32 IMP CoordinadordeImplantación Analista/Diseña-
dorSenior
2 2.628,08 328,51 441,6 55,2
22 IMP InstructordeCapacitación Analista/Diseña-
dorSenior
1 1.352 169 2.656 332
26 IMP JefedeFrentedeImplantación(bodega,
plataformasyruta)
Analista/Diseña-
dorSenior
5 4.006,96 500,87 0 0
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
116

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla22—continuación
Cód. Origen
pro-
puesto
Perfil CategoríaE-26 Plazas
pro-
pues-
tas
HHimplem. Jornadas
implem.
HH/8
HHoper. Jornadas
oper.HH/8
28 OF AsistentedeImplantaciónenTerreno TIC 18 14.425,04 1.803,13 0 0
24 SRE LíderdeOperación/SRE JefedeTIC 1 812,8 101,6 646,4 80,8
14S SRE IngenieroDevOpsyPlataformaSenior IngenieroDevOps/
SRE
7 3.296,35 412,0437 3.436,8 429,6
14J SRE IngenieroDevOpsyPlataformaJunior IngenieroDevOps/
SRE
4 1.648,18 206,0225 1.718,4 214,8
29 NOC TécnicodeRedeseInstalaciones(sala
técnica,cableado,racksyenlaces)
TIC 5 2.240 280 0 0
17 NOC OperadordeMesaN1 TIC 16 5.664 708 38.246 4.780,75
30 NOC OperadorNOC TIC 6 3.672 459 21.748,2 2.718,525
13 SEG EncargadodeSeguridaddelaInforma-
ción
Encargadode
SeguridadTI
1 1.016 127 232 29
31E SEG EspecialistadeCiberseguridadSenior IngenieroSenior 2 1.464 183 913,6 114,2
31O SEG/
NOC
AnalistaSOC IngenieroSenior 6 5.832 729 26.280 3.285
Totaldeperfiles 136 90.048,83 11.256,10 107.845,40 13.480,675
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
117

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Lasplazassonlapropuestadeprocedenciade5.7,nounanóminaconfirmadanilaapro-
bacióndesuconcurrencia.EnSOCseproponencuatropersonasdeSEGydosdeNOC;cada
personasecuentaunasolavez.LasHHdelosjefesdefrenteydelosasistentesdeterrenose
repartenenproporciónasusplazas.Lasinstalacionesfísicasdelasalatécnica,elcableado,
losracks,losgabinetesdebordeylosenlaces(6.1,6.2,6.3,6.6.2y6.6.3)lasejecutapersonalde
redesyoperacióndeladivisiónInfraestructura(perfil29),bajolaresponsabilidaddelLíderde
Operación/SRE;losproveedoresinstalanlaenergía,laclimatizaciónylaextincióndeincen-
dios(6.1.2a6.1.4).Elperfil29apoyaademáslainstalacióndesensores,kitsdefrío,impresoras
ybalanzas(6.5.3a6.5.6).Sus2.240HHsedescuentandelosperfilesDevOpsenproporción
a sus horas. La selección de categoría económica no acredita por sí sola competencia para
desempeñarelrol.
Conciliaciónporfase. Losperfilesaportan90.048,83HHdeimplementacióny107.845,40HHde
operaciónyreversibilidad.Losserviciosespecializadosporresultadoseañadenporseparado,
sinasignarlesplazas:864HHdeimplementacióny460,80deoperación.Portanto:
𝐻𝐻𝑖𝑚𝑝𝑙𝑒𝑚. = 90,048,83 + 864 = 90 ,912,83,
𝐻𝐻𝑜𝑝𝑒𝑟. = 107,845,40 + 460,80 = 108 ,306,20,
𝐻𝐻𝑝𝑟𝑜𝑦𝑒𝑐𝑡𝑜 = 90,912,83 + 108,306,20 = 199 ,219,03.
Esta separación sigue la fase de valorización de cada paquete; el resumen por etapa de la
sección4.3sigueelmescalendariodeejecución.Poresolaimplementaciónylaoperación
difierenen102,97HHentreambastablas(90.809,86y108.409,17HHenelresumenporetapa),
conelmismototalde199.219,03HH.
En jornadas equivalentes son 11.364,10 de implementación y 13.538,275 de operación:
24.902,38entotal.Estascantidadesnosesumancomoduracióndelproyecto.
Asignaciónporpartida. LaTabla 23asignalasHHdecadapartidaalosperfilesdelaTabla 22.
Lacolumna«PerfilyHH»indicaelcódigodelperfily,entreparéntesis,susHHenlapartida;
elcódigo00identificalosserviciosespecializadosporresultado.CadafilasumalasHHdela
partidaycadaperfilsumalasHHdeimplementaciónydeoperacióndelaTabla 22:197.894,23
HHdelosperfilesy1.324,80HHdeserviciosespecializados,parauntotalde199.219,03HH.
Lasfases8y9.2secuentanenoperación;laspartidasrecurrentesdelasfases1a7quesiguen
despuésdelmes20sedividenenproporciónasusmeses,yelSOCsegúnsucalendario.
Porejemplo,las5.168HHdecapacitaciónycertificación(7.1,7.3y8.5.1)serepartenentre
elInstructordeCapacitación(3.480HH),loscoordinadoresdeimplantación(732,8HH),el
AnalistaPMO,documentaciónycompras(588,8HH)yelLíderdeImplantación(366,4HH).
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
118

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23 AsignacióndeHHporpartidayperfil.Fuente:elaboraciónapartirdelaEDTdelFormularioT-14,lasHHdelaTabla 3ylosperfilesdelaTabla 22.
EDT Partida Familia Meses HH PerfilyHH
1.1.1 Actadeconstitucióndelproyecto,firmadaconlaContrapar-
teTécnica
JP 1–1 80 20(52),01(28)
1.1.2 DocumentodevalidaciónconelCLIENTEdelosproblemas
ymetasdelproyecto
JP 1–1 80 20(52),01(28)
1.1.3 ActadeconfirmaciónconelCLIENTEdelafechadeinicio,
laevidenciaparaelproveedordelácteos,lasventanasde
pasoaproducciónyelacusetributario
JP 1–1 80 20(52),01(28)
1.2.1 Documentodeespecificaciónderequerimientosylínea
basedealcancedelaEtapa1(H1)
ARQ 1–1 80 06S(26,67),05(24),06J(13,33),03S
(10,67),03J(5,33)
1.2.2 Documentodereglasderuteocapturadasalplanificadorde
rutas
IMP 1–3 80 05(24),06S(24),32(13,33),06J(12),
21(6,67)
1.2.3 Documentodeespecificacióndelasinterfacessindocu-
mentacióndelERP,delWMSde2013ydelatelemetríadel
tercero,yperfildeintercambioconlascadenas
ARQ 1–4 80 12S(31,57),02(16,66),12J(15,77),
03S(10,67),03J(5,33)
1.2.4 Matrizdetrazabilidad:requerimiento,módulo,paquetey
prueba(H1)
CAL 2–2 80 19S(47,27),16(24),19J(8,73)
1.2.5 DocumentodelíneabasedealcancedelaEtapa2:canal
modernoycostodeservir(H8)
ARQ 13–13 80 06S(26,67),05(24),06J(13,33),03S
(10,67),03J(5,33)
1.3.1 Planparaladireccióndelproyecto,conelcalendario
decongelamientosdeseptiembre,diciembreyelcierre
mensual
JP 1–1 80 20(52),01(28)
1.3.2 EDTydiccionariodelaEDT(líneabasedelalcance) JP 2–2 80 20(52),01(28)
1.3.3 CartaGanttde56mesesconloshitosH1aH12ylaruta
crítica
JP 2–2 80 20(52),01(28)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
119

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
1.3.4 Documentodenivelaciónderecursosyfrentesdelsolapa-
mientodelosmeses13a15y19a20
JP 2–2 80 20(52),01(28)
1.3.5 Reuniónsemanaldeseguimientoconsuinformesemanal JP 1–20 480 20(312),01(168)
1.4.1 Registrodeinteresadosconsuinfluencia,interésyestrate-
gia
JP 1–1 80 20(52),01(28)
1.4.2 Plandecomunicacionesconcalendarioycanalesporgrupo
deinterés
JP 1–1 80 20(52),01(28)
1.4.3 Registrodesolicitudesdecambioconanálisisdeimpacto JP 1–56 896 20(582,4),01(313,6)
1.5.1 Plandecalidadyplandepruebas CAL 2–2 80 19S(47,27),16(24),19J(8,73)
1.5.2 Puertasdecalidadautomáticas:coberturadelógicade
negociodel70%,globaldel80%ydelcódigomodificado
del80%
CAL 6–20 80 19S(55,45),19J(18,55),16(6)
1.6.1 PlanderiesgosyregistroinicialderiesgossegúnISO31000 JP 2–2 80 20(52),01(28)
1.6.2 RegistroderiesgosrevisadoencadaComitédeProyecto JP 1–20 160 20(104),01(56)
1.7.1 PlandeReversibilidadinicial(primeros90días) JP 3–3 80 20(52),01(28)
1.7.2 PrimeraactualizaciónanualdelPlandeReversibilidad
durantelaimplementación
JP 15–15 80 20(52),01(28)
1.8.1 Oficinadegestióndelproyectoconmetodologíabasadaen
elPMBOK
JP 1–20 320 20(208),01(112)
1.8.2 ActasdelComitéEjecutivomensual,conlaaprobaciónde
loscambiosdealcance
JP 1–56 448 20(291,2),01(156,8)
1.8.3 ActasdelComitédeProyectoquincenal JP 1–20 240 20(156),01(84)
1.8.4 ActasdelComitédeArquitecturamensual ARQ 1–56 448 03S(238,93),03J(119,47),02(89,6)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
120

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
1.8.5 ActasdelComitédeOperaciónmensual,desdeelmes13 SRE 13–56 352 24(264),14S(58,67),14J(29,33)
1.8.6 Informemensualdeavanceconvalorganado JP 1–20 480 20(312),01(168)
1.8.7 TablerodeestadodelproyectodisponibleparaelCLIENTE JP 2–56 440 20(286),01(154)
1.8.8 Espaciocolaborativoconladocumentación,losentregables,
lasactas,losriesgosyloscambios
JP 1–56 448 20(291,2),01(156,8)
1.9.1 Matrizdecumplimientonormativoporobligaciónlegal,
consucontrolysuevidencia
SEG 1–1 80 13(56),31E(24)
1.9.2 AcuerdodetratamientodedatospersonalesconelCLIEN-
TE
SEG 1–1 80 13(56),31E(24)
1.9.3 Registrodeactividadesdetratamientoyevaluaciónde
impactoenproteccióndedatos
SEG 2–2 80 13(56),31E(24)
1.9.4 CertificaciónISO/IEC27001vigenteyentregaanualdelos
informesdecertificación
SEG 1–56 224 13(156,8),31E(67,2)
1.9.5 Garantíadefielcumplimiento,segurosycertificadoslabora-
lesvigentesduranteelcontrato
JP 1–56 224 20(145,6),01(78,4)
2.1.1 Documentodearquitecturalógica:capas,módulosM1a
M12einterfaces
ARQ 2–2 240 12S(94,68),02(49,98),12J(47,34),
03S(32),03J(16)
2.1.2 Documentodearquitecturafísicahíbrida:nube,centrosde
distribuciónyplataformasdecross-docking
ARQ 2–2 240 03S(128),03J(64),02(48)
2.1.3 Modelodedatosydiccionariodedatos,conlatrazabilidad
porlote
DAT 2–2 240 10S(128),10J(64),23(48)
2.1.4 DocumentodediseñodetalladodeM11ydelintercambio
conlascadenas
ARQ 13–13 240 03S(128),03J(64),02(48)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
121

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
2.2.1 Plandeseguridaddelainformación SEG 2–2 240 13(168),31E(72)
2.2.2 Modeladodeamenazasporcomponenteyporintegración
externa,actualizadoantecadacambio
SEG 3–10 240 31E(192),13(48)
2.2.3 Planderespuestaaincidentesdeseguridad,conavisoal
CLIENTEendoshoras
SEG 3–3 240 13(168),31E(72)
2.2.4 Matrizdeclasificacióndelainformaciónymatrizdecontro-
les
SEG 2–2 240 13(168),31E(72)
2.3.1 PlanodelasalatécnicadeTalca,consucálculoeléctricoy
térmico
SRE 1–2 240 14S(144),14J(72),24(24)
2.3.2 PlanodedistribucióndelosracksR01deservidoresyR02
decomunicaciones
SRE 1–2 240 14S(144),14J(72),24(24)
2.3.3 PlanodelosgabinetesdebordedeConcepciónydelas
plataformasdecross-docking
SRE 2–2 240 14S(144),14J(72),24(24)
2.4.1 Actadeaprobacióndelaarquitectura,elplandeseguridad
yelmodelodedatos(H2)
ARQ 3–3 240 03S(128),03J(64),02(48)
2.4.2 ActadeaprobacióndeldiseñodetalladodelaEtapa2(H8) ARQ 13–13 240 03S(128),03J(64),02(48)
2.4.3 Validacióndeldiseñodelkitenbancodepruebas SRE 3–3 341,33 14S(206,22),14J(103,11),24(32)
2.4.4 Mapeotérmicoportipodecarrocería ARQ 4–4 240 03S(128),03J(64),02(48)
2.5.1 PlandecontinuidaddelnegociosegúnISO22301,con
análisisdeimpactoyprocedimientosmanuales
SRE 3–3 240 14S(144),14J(72),24(24)
2.5.2 PlandecontinuidadTICsegúnISO/IEC27031yplande
recuperaciónantedesastres
SRE 3–3 240 14S(144),14J(72),24(24)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
122

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
2.6.1 Investigaciónconpreparadores,preventistas,conductoresy
almaceneros
IMP 2–2 240 05(72),06S(72),32(40),06J(36),21
(20)
2.6.2 Prototiposypruebasdeusabilidadconparticipantesdel
CLIENTE
IMP 3–3 240 06S(136),06J(68),32(24),21(12)
2.6.3 Indicadoresdeusabilidadcomprometidosportransacción
crítica
IMP 4–4 240 06S(136),06J(68),32(24),21(12)
3.1.1 AmbientesdeDesarrolloyQAenlanube(H3) SRE 5–5 240 14S(144),14J(72),24(24)
3.1.2 AmbientesdePreproducciónyProducciónenlanube(H3) SRE 5–5 240 14S(144),14J(72),24(24)
3.1.3 Ambientederecuperaciónantedesastresenlaregión
secundaria(H3)
SRE 5–5 240 14S(144),14J(72),24(24)
3.1.4 Cadenadeintegraciónyentregacontinua,einfraestructura
comocódigo
SRE 4–4 240 14S(144),14J(72),24(24)
3.1.5 Observabilidaddelosdocemódulosydelossitios,con
tablerosparaelCLIENTE(H3)
SRE 5–5 240 14S(144),14J(72),24(24)
3.2.1 Serviciodenubeparalaaplicaciónylosportales SRE 4–4 240 14S(144),14J(72),24(24)
3.2.2 Serviciodenubedebasededatos,cachéymensajería SRE 4–4 240 14S(144),14J(72),24(24)
3.2.3 ServiciodenubedeingestadeIoT,telemetríacruday
plataformaanalítica
SRE 4–4 240 14S(144),14J(72),24(24)
3.2.4 Serviciodenubederespaldoinmutableyréplicaentre
regiones
SRE 4–4 240 14S(144),14J(72),24(24)
3.2.5 Serviciodenubedeseguridadygobierno,ydetecciónen
endpoints
SEG 4–4 240 31E(192),13(48)
3.2.6 Serviciodegestióndedispositivosmóviles SRE 5–5 240 14S(144),14J(72),24(24)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
123

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
3.3.1 Identidadycontroldeacceso,incluidoslosconductores
externosquerotansinaviso
SEG 5–7 480 31E(384),13(96)
3.3.2 IntegraciónconelERPcomoúnicoemisordelaguíade
despacho(INT-06eINT-07)
ARQ 5–6 516 12S(207,11),02(109,33),12J
(103,56),03S(64),03J(32)
3.3.3 ConvivenciaconelWMSde2013duranteelreemplazo ARQ 5–6 480 03S(256),03J(128),02(96)
3.3.4 Integraciónconlatelemetríadelos42camionespropios
(INT-15)
ARQ 5–6 480 12S(189,36),02(99,96),12J(94,68),
03S(64),03J(32)
3.3.5 Registroauditabledestock,lotesycobros ARQ 5–7 480 03S(256),03J(128),02(96)
3.3.6 Operaciónsinconexión:14horasenterrenoy24horasen
elCD
ARQ 5–7 480 03S(256),03J(128),02(96)
3.4.1 Recepcióndemercaderíaconcapturadeloteyvencimiento
(M1Recepción)
DES 5–7 880,33 09S(215,92),07S(195,38),09J
(143,94),07J(97,69),04(96),08S
(65,7),08J(65,7)
3.4.2 Inventarioporubicaciónylote,conFEFOyconteocíclico
(M2Inventario)
DES 5–7 1.006,67 09S(250,7),07S(226,85),09J
(167,13),07J(113,43),04(96),08S
(76,28),08J(76,28)
3.4.3 Preparacióndepedidosenelturnodenocheyenlacámara
decongelado(M5Preparación)
DES 5–7 973,83 12S(341,08),09S(219,73),12J
(170,54),09J(146,48),04(96)
3.4.4 Cadenadefrío,retenciónporSSCCyretirosanitario(M9
Calidadytrazabilidad)
DES 5–8 1.587,33 09S(582,45),09J(388,3),08S
(236,29),08J(236,29),04(144)
3.4.5 Ingestadetemperatura(M9)yposicióndeflota(M12) DES 5–7 919,5 12S(301,32),09S(194,11),12J
(150,66),04(144),09J(129,41)
3.4.6 Aplicaciónmóvildepreventasinconexión,constocky
crédito(M3Preventa)
DES 5–7 1.314,17 12S(473,32),09S(304,91),12J
(236,66),09J(203,28),04(96)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
124

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
3.4.7 Planificaciónderutascorregibleporelplanificador(M4
Rutas)
DES 5–8 937,67 09S(231,71),07S(209,66),09J
(154,47),07J(104,83),04(96),08S
(70,5),08J(70,5)
3.4.8 Aplicaciónmóvilderepartoconpruebadeentregadigital
(M6Reparto)
DES 5–8 1.586,67 09S(410,37),07S(371,33),09J
(273,58),07J(185,67),08S(124,86),
08J(124,86),04(96)
3.4.9 Devolucionesenterrenoycontroldeenvases(M8Devolu-
cionesyenvases)
DES 5–8 588 09S(198,54),09J(132,36),04(96),
08S(80,55),08J(80,55)
3.4.10 Cobroenruta,rendiciónyconciliación(M7Cobranzay
rendición)
DES 5–9 1.248,33 09S(317,23),07S(287,05),09J
(211,49),07J(143,52),08S(96,52),
08J(96,52),04(96)
3.4.11 IndicadoresoperacionalesyOTIFdiario(M10Analítica) DAT 8–8 836,5 10S(446,13),10J(223,07),23(167,3)
3.5.1 Pedidoelectrónicoyavisodedespachoparalascadenas,y
portaldeproveedores(M11Canalmoderno)
DES 14–15 973 12S(340,76),09S(219,52),12J
(170,38),09J(146,34),04(96)
3.5.2 Portalwebdeclientes:cuenta,saldo,entregasydocumen-
tos
DES 14–15 1.033,17 09S(258),07S(233,45),09J(172),
07J(116,72),04(96),08S(78,5),08J
(78,5)
3.5.3 Portalwebdetransportistas:rutasasignadasdeldíasiguien-
te
DES 14–15 280 04(96),09S(50,65),07S(45,84),09J
(33,77),07J(22,92),08S(15,41),08J
(15,41)
3.5.4 Costodeservirporclienteyporentrega(M10Analítica) DAT 14–15 653 10S(348,27),10J(174,13),23(130,6)
3.6.1 Intercambiodeloteytrazabilidadconlosproveedores DAT 7–8 480 10S(256),10J(128),23(96)
3.6.2 Integraciónconlapasareladepagoparaelcobrocon
tarjeta(INT-09)
DES 6–7 480 12S(167,86),09S(108,13),12J
(83,93),09J(72,08),04(48)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
125

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
3.6.3 Integraciónconelserviciodemapasygeocodificación
(INT-10)
DES 6–7 480 12S(167,85),09S(108,13),12J
(83,93),09J(72,09),04(48)
3.6.4 Integraciónconelserviciodeavisosalcliente(INT-11) DES 6–7 480 12S(167,85),09S(108,13),12J
(83,93),09J(72,09),04(48)
3.6.5 Intercambioelectrónicoconlaprincipalcadena,consus
pruebasaprobadas(INT-08)
DES 13–18 516 09S(188,86),09J(125,9),08S(76,62),
08J(76,62),04(48)
3.6.6 Incorporacióndelasdemáscadenasalintercambioelectró-
nico(INT-08)
DES 17–19 508 09S(185,63),09J(123,75),08S
(75,31),08J(75,31),04(48)
3.7.1 Informedeperfilamientoydatossaneados DAT 7–9 512 10S(273,07),10J(136,53),23(102,4)
3.7.2 Datosmaestroscargados:8.400SKU,clienteseinstalaciones DAT 9–10 504 10S(268,8),10J(134,4),23(100,8)
3.7.3 SaldosmigradosdesdeelWMSdeTalca DAT 11–11 504 10S(268,8),10J(134,4),23(100,8)
3.7.4 SaldoscargadosenConcepcióndesdeelconteofísico DAT 11–11 504 10S(268,8),10J(134,4),23(100,8)
3.7.5 Actadeconciliaciónycortefueradelasventanasdeconge-
lamiento
DAT 12–12 480 10S(256),10J(128),23(96)
3.8.1 Pruebasdeintegración,regresióneidempotenciaenQA
(H4)
CAL 9–9 160 19S(110,91),19J(37,09),16(12)
3.8.2 Pruebasdeaceptaciónydeaccesibilidadconpreventistas,
conductoresybodega
CAL 9–10 320 19S(221,82),19J(74,18),16(24)
3.8.3 Cincocondicionesfísicas:−22°Cconguantes,lluvia,calor
superiora34°C,soldirectoyusoconunamano;descone-
xiónseparadade14horas
CAL 9–10 320 19S(221,82),19J(74,18),16(24)
3.8.4 Pruebasdecargaconelpeakdeseptiembreyderesiliencia CAL 9–10 320 19S(221,82),19J(74,18),16(24)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
126

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
3.8.5 Pruebaderecuperaciónantedesastresconconmutación
real
CAL 9–10 320 19S(221,82),19J(74,18),16(24)
3.8.6 PruebadeseguridadofensivadelaEtapa1,poruntercero
independiente
SEG 9–10 320 00(320)
3.8.7 ActadecertificacióndelaEtapa1(H5) CAL 10–11 160 19S(94,55),16(48),19J(17,45)
3.8.8 DemostraciónenPreproduccióndeldesplieguesininte-
rrupcióndelaEtapa1
SRE 9–10 320 14S(192),14J(96),24(32)
3.9.1 PruebasdeintegraciónyregresiónsinafectarlaEtapa1en
producción(H9)
CAL 16–16 160 19S(110,91),19J(37,09),16(12)
3.9.2 Pruebasdeaceptaciónydeaccesibilidadconcadenas,
transportistas,ComercialyFinanzas
CAL 17–17 320 19S(221,82),19J(74,18),16(24)
3.9.3 Pruebasdecargaconambasetapasactivasyderesiliencia CAL 16–17 320 19S(221,82),19J(74,18),16(24)
3.9.4 Pruebaderecuperaciónantedesastresconambasetapas CAL 16–17 320 19S(221,82),19J(74,18),16(24)
3.9.5 PruebadeseguridadofensivadelaEtapa2,poruntercero
independiente
SEG 16–16 160 00(160)
3.9.6 ActadecertificacióndelaEtapa2ycierredeldesarrollo
(H10)
CAL 17–17 160 19S(94,55),16(48),19J(17,45)
3.9.7 DemostraciónenPreproduccióndeldesplieguesininte-
rrupcióndelaEtapa2
SRE 16–17 160 14S(96),14J(48),24(16)
3.10.1.1 Innovación1:documentodecatálogodeaccionesyprotoco-
lodelpiloto(INN-01.P1)
DAT 7–9 240 10S(128),10J(64),23(48)
3.10.1.2 Innovación1:estimadordesaldoyritmodereposición
(INN-01.P2)
DAT 9–10 240 10S(128),10J(64),23(48)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
127

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
3.10.1.3 Innovación1:funcióndelistasinconexiónenlaaplicación
depreventa(INN-01.P3)
DAT 9–10 240 10S(128),10J(64),23(48)
3.10.1.4 Innovación1:informedelpilotoenmarchablancayhabili-
tación(INN-01.P4)
DAT 11–15 240 10S(128),10J(64),23(48)
3.10.2.1 Innovación2:informedemedicióninicialycontratode
evidencia(INN-02.P1)
CAL 2–3 240 19S(166,36),19J(55,64),16(18)
3.10.2.2 Innovación2:circuitomínimodereproducciónenla
preventa(INN-02.P2)
CAL 3–5 240 19S(166,36),19J(55,64),16(18)
3.10.2.3 Innovación2:capturadeevidenciaenlasaplicacionesde
preventa,preparaciónyreparto(INN-02.P3)
CAL 5–10 240 19S(166,36),19J(55,64),16(18)
3.10.2.4 Innovación2:informedevalidacióncomparadadurantela
implementación(INN-02.P4,primeraparte)
CAL 11–15 240 19S(166,36),19J(55,64),16(18)
3.10.3.1 Innovación3:documentodefamiliaspriorizadasyparáme-
trosaprobados(INN-03.P1)
DAT 3–5 240 10S(128),10J(64),23(48)
3.10.3.2 Innovación3:asociaciónlote–sensorenelbordeyenel
camión(INN-03.P2)
DAT 5–9 240 10S(128),10J(64),23(48)
3.10.3.3 Innovación3:vistaenM9yordendesalidasugerido(INN-
03.P3)
DAT 9–10 240 10S(128),10J(64),23(48)
3.10.3.4 Innovación3:informedevalidaciónenmarchablancacon
Calidad(INN-03.P4)
DAT 11–15 240 10S(128),10J(64),23(48)
3.10.4.1 Innovación5:prototipoeinformedelapruebadecompren-
sión(INN-05.P1)
IMP 13–14 240 06S(136),06J(68),32(24),21(12)
3.10.4.2 Innovación5:evaluacióndeprivacidadydiseñodela
impresiónencabina(INN-05.P2)
IMP 14–15 240 32(96),20(48),21(48),22(48)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
128

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
3.10.4.3 Innovación5:cálculoybloques1a3delahojadenegocio
(INN-05.P3)
IMP 15–17 240 32(96),20(48),21(48),22(48)
3.10.4.4 Innovación5:hojacertificada,enmarchablancayen
producción(INN-05.P4,primeraparte)
IMP 18–21 240 32(96),20(48),21(48),22(48)
3.11.1 Documentacióntécnica,funcional,dearquitectura,de
operaciónydeseguridad
ARQ 15–21 80 03S(42,67),03J(21,33),02(16)
3.11.2 Basedeconocimientodeincidentesydecisionesdediseño SRE 10–20 80 14S(48),14J(24),24(8)
3.11.3 Estándaresdecodificaciónydocumentacióndeinterfaces
enOpenAPIyAsyncAPI
DES 4–20 80 12S(27,98),09S(18,02),12J(13,98),
09J(12,02),04(8)
3.11.4 Inventariodecomponentes(SBOM)consuslicenciasde
códigoabierto
DES 4–20 80 09S(19,82),07S(17,93),09J(13,22),
07J(8,97),04(8),08S(6,03),08J
(6,03)
3.11.5 DepósitodelcódigofuenteenelrepositoriodelCLIENTEen
cadaliberación
DES 6–20 80 09S(29,05),09J(19,37),08S(11,79),
08J(11,79),04(8)
4.1.1 PlandeolasdelaEtapa1porsitioyzona:Talca,Concep-
ciónyplataformasdecross-docking
IMP 10–10 80 32(32),20(16),21(16),22(16)
4.1.2 ProcedimientodereversióndelaEtapa1antesdelas05:30,
conversiónoperativalocalyDTEemitidosporelERP
IMP 11–11 80 32(32),20(16),21(16),22(16)
4.1.3 PlandeimplantaciónyreversióndelaEtapa2fueradela
ventanade05:30a07:00
IMP 17–17 80 32(32),20(16),21(16),22(16)
4.1.4 Pilotodecadenadefríoencuatrocamiones IMP 10–11 341,33 32(142,22),21(71,11),20(64),22
(64)
4.2.1 MarchablancadelaEtapa1conconciliacióndiaria(H6) IMP 13–15 7.392 28(5.409,39),26(1.502,61),32(320),
21(160)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
129

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
4.2.2 EstabilizacióndelaEtapa1,acompañamientoenrutay
restauracionesdesoportepuente
IMP 16–20 5.408 28(3.606,26),26(1.001,74),32
(533,33),21(266,67)
4.2.3 ExpedientedeH7 JP 16–16 80 20(52),01(28)
4.3.1 MarchablancadelaEtapa2enconvivenciaconlaEtapa1y
fuenteúnicadedatos(H11)
IMP 19–20 4.928 28(3.606,26),26(1.001,74),32
(213,33),21(106,67)
4.3.2 EstabilizacióndelaEtapa2conComercial,Finanzas,cade-
nasytransportistas
IMP 21–22 2.464 28(1.803,13),26(500,87),32
(106,67),21(53,33)
4.3.3 ExpedientedeH12 JP 21–21 80 20(52),01(28)
4.3.4 Garantíadecorrectofuncionamientoconstituida,condición
delaaceptaciónfinal(H12)
JP 20–20 80 20(52),01(28)
5.1.1 EspecificacióndecompradeequiposdeusoparaelCLIEN-
TE
ARQ 2–2 80 03S(42,67),03J(21,33),02(16)
5.1.2 Especificaciónycompradelasalatécnica,losracks,los
servidoresylosgabinetesdeborde
ARQ 2–2 80 03S(42,67),03J(21,33),02(16)
5.1.3 Actasderecepcióntécnicadelequipamientodeterreno
compradoporelCLIENTEydelainfraestructuraprovista
porLafroX
SRE 5–5 80 20(56),14S(16),14J(8)
5.1.4 Especificaciónycompradelsistemadecadenadefrío ARQ 1–2 240 03S(128),03J(64),02(48)
5.2.1 ContratodelosserviciosdeAWS SRE 2–2 80 20(56),14S(16),14J(8)
5.2.2 Suscripcióndelserviciodegestióndedispositivosyde
detecciónenendpoints
SRE 4–4 80 20(56),14S(16),14J(8)
5.2.3 Licenciasdesoftwaredetercerosconstituidasanombredel
CLIENTE
ARQ 4–4 80 03S(42,67),03J(21,33),02(16)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
130

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
5.3.1 ContratodefibraópticadelosCDdeTalcayConcepción SRE 4–4 80 20(56),14S(16),14J(8)
5.3.2 ContratodeplanesLTEcondosproveedores(ochoplanes) SRE 4–4 80 20(56),14S(16),14J(8)
5.3.3 ContratodeStarlinkparaloscincositios:Talca,Concepción
ylastresplataformasdecross-docking
SRE 4–4 80 20(56),14S(16),14J(8)
5.3.4 ContratodeSIMM2Myserviciosatelitaldeloscamiones
confrío
SRE 2–2 80 20(56),14S(16),14J(8)
5.4.1 Acuerdosoperacionalesfirmadosconlosdieztransportistas IMP 9–12 80 32(32),20(16),21(16),22(16)
5.4.2 Actadeacuerdoconelsindicatosobreterminales,GPSy
cámaras
IMP 9–12 80 32(32),20(16),21(16),22(16)
5.4.3 Fórmulaaprobadadeltramovariable:reglasdeatribución,
canastaeíndices(INN-04.P1)
JP 17–20 80 20(52),01(28)
5.4.4 Contratodecustodiadefuentesconunterceroindepen-
diente
JP 7–7 80 20(72),01(8)
6.1.1 Coordinacióndelaobracivildeseparación,acargodel
CLIENTE(RT-06.06),ypisotécnicodelasala
RED 3–3 160 29(144),24(16)
6.1.2 Hardwaredeenergíainstalado:UPSmodularN+1,genera-
dorcon24horasdeautonomía,transferenciaautomáticay
PDUA/B
RED 3–3 160 00(128),29(32)
6.1.3 HardwaredeclimatizacióndeprecisiónN+1instalado RED 3–3 160 00(128),29(32)
6.1.4 Hardwarededeteccióntempranadeincendioyextinción
poragentelimpioinstalado
RED 3–3 160 00(128),29(32)
6.1.5 Actaderecepcióntécnicadelasala RED 4–4 160 29(144),24(16)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
131

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
6.2.1 CableadodecobreCat6AyfibraOM4tendido,condos
ductosdeingresoindependientes
RED 4–4 160 29(144),24(16)
6.2.2 Certificacióndeenlaces,etiquetadoyplanosas-built RED 6–6 160 29(144),24(16)
6.2.3 Gabinetesdepisoyswitchesdeaccesoinstaladosenlas
bodegasdeTalcayConcepción
RED 7–7 160 29(144),24(16)
6.3.1 RackR01deservidoresmontado:clústerdetresnodos,
respaldolocal,consolaKVMytrasladodelservidordelERP
delCLIENTE
RED 4–5 160 29(144),24(16)
6.3.2 RackR02decomunicacionesmontado:firewalls,switches
denúcleoydegestión,ydistribucióndefibra
RED 4–5 160 29(144),24(16)
6.3.3 GabinetedebordedeConcepciónmontado:servidores
activoyenespera,firewalls,switches,UPS,climatizacióny
monitoreo
RED 4–4 160 29(144),24(16)
6.3.4 GabinetesdebordemontadosenCuricó,ChillányLosÁn-
geles,condosmini-PC(activoyenespera)porplataforma
RED 9–9 160 29(144),24(16)
6.4.1 Hardwaredecontroldeaccesobiométricoyesclusainstala-
do
SEG 5–5 160 31E(128),13(32)
6.4.2 Hardwaredevideovigilanciainstalado SEG 5–5 160 31E(128),13(32)
6.4.3 Recintodecustodiaderespaldoshabilitado SEG 5–6 160 31E(128),13(32)
6.5.1 Terminalesdepreventa,repartoybodegaconfiguradosy
enrolados
SRE 9–12 160 14S(96),14J(48),24(16)
6.5.2 Terminalesdepagoconfigurados,unoporcamión SRE 10–12 160 14S(96),14J(48),24(16)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
132

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
6.5.3 SensoresdecámaraygatewaysIoTinstaladosenTalcay
Concepción
SRE 9–11 160 29(112),14S(21,33),24(16),14J
(10,67)
6.5.4 Kitdecadenadefríoinstaladoyrecibidoenlos28camio-
nesconfrío
SRE 8–12 320 29(224),14S(42,67),24(32),14J
(21,33)
6.5.5 Impresorasdecabinainstaladas SRE 10–12 160 29(112),14S(21,33),24(16),14J
(10,67)
6.5.6 Impresorasdeandénybalanzasderecepcióninstaladas SRE 9–12 160 29(112),14S(21,33),24(16),14J
(10,67)
6.6.1 Softwaredebaseinstaladoenlossitios:virtualización,
contenedores,PostgreSQL,RabbitMQyKeycloak
SRE 5–5 160 14S(96),14J(48),24(16)
6.6.2 Enlacesdefibra,LTEyStarlinkhabilitados,conconmuta-
ciónalrespaldo
RED 5–5 160 29(144),24(16)
6.6.3 BordedelosCDenservicio,conlapruebadeautonomíade
24horasaprobada
RED 5–5 160 29(144),24(16)
7.1.1 Plandecapacitaciónporperfil:usuariosfinales,avanzados,
administradores,equipotécnicoysoporte
IMP 10–12 160 22(120),20(16),32(16),21(8)
7.1.2 Programadecapacitacióncontinuadelturnodenochepor
larotacióndel38%
IMP 13–56 2.816 22(2.112),20(281,6),32(281,6),21
(140,8)
7.1.3 Incorporacióndeconductoresdetransportistas,escaneosy
lecturadelrojo
IMP 11–20 240 32(96),20(48),21(48),22(48)
7.1.4 TraspasoalequipodeTIdecuatropersonasdelCLIENTE IMP 15–20 160 32(64),20(32),21(32),22(32)
7.1.5 Materialesdecapacitación:manualesporperfil,guías
rápidas,preguntasfrecuentesyvideostutoriales
IMP 10–18 160 22(120),20(16),32(16),21(8)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
133

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
7.1.6 Plataformadeautoformaciónenlíneaconregistrode
avance
IMP 10–12 160 22(120),20(16),32(16),21(8)
7.2.1 Acompañamientodelpersonalcon20o30añosenla
compañía
IMP 10–16 160 32(64),20(32),21(32),22(32)
7.2.2 Gestióndelcambioconlascadenasylostransportistas IMP 16–18 160 32(64),20(32),21(32),22(32)
7.2.3 Diagnósticodelimpactoorganizacionalporáreayperfil,
conagentesdecambio
IMP 2–6 160 32(64),20(32),21(32),22(32)
7.2.4 Procedimientosoperativosrediseñados,contingenciade
fríoyrupturaconfirmada
IMP 8–20 240 32(96),20(48),21(48),22(48)
7.2.5 Medicióndelaadopciónyplandeaccióncorrectiva IMP 13–21 160 32(64),20(32),21(32),22(32)
7.3.1 Certificacióndepreventistas,conductoresypreparadores
(Etapa1)
IMP 13–15 160 32(64),20(32),21(32),22(32)
7.3.2 CertificacióndeComercialyFinanzasencostodeservir
(Etapa2)
IMP 18–18 160 32(64),20(32),21(32),22(32)
8.1.1 Serviciodecentrodeoperaciones24 ×7ymesadeservicio
durantelos36mesesdeoperación(04:00a22:00;24 ×7en
septiembreydiciembre)
SRE 21–56 21.764,2 30(21.748,2),22(16)
8.1.2 Serviciodegestióndeincidentes,problemasynivelesde
serviciodelArt.78°durantelos36mesesdeoperación
SRE 21–56 38.246 17(38.246)
8.1.3 Serviciodecontinuidadypruebassemestralesderecupera-
ciónantedesastresdurantelos36mesesdeoperación
SRE 21–56 560 14S(336),14J(168),24(56)
8.1.4 ActualizacionesanualesdelPlandeReversibilidaddurante
los36mesesdeoperación
JP 21–56 288 20(187,2),01(100,8)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
134

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
8.1.5 Serviciodecentrodeoperacionesdeseguridad24 ×7con
SIEMdesdelaprimeramarchablanca(mes13)hastaelmes
56
SEG 13–56 32.112 31O(32.112)
8.1.6 Pruebasmensualesderestauraciónderespaldosdurante
los36mesesdeoperación
SRE 21–56 576 14S(345,6),14J(172,8),24(57,6)
8.2.1 Mantenimientocorrectivoyevolutivodelsoftwaredurante
los36mesesdeoperación,conbolsaanualdehorasyfuera
delasventanasdecongelamiento
DES 21–56 4.608 09S(1.658,88),09J(1.105,92),04
(460,8),07S(460,8),08S(345,6),08J
(345,6),07J(230,4)
8.2.2 Mantenimientodeciberseguridaddurantelos36mesesde
operación:vulnerabilidades,intrusiónanualeinyecciónde
fallas
SEG 21–56 1.152 31E(806,4),00(230,4),13(115,2)
8.2.3 Mantenimientodelhardwaredurantelos36mesesdeopera-
ción:salatécnica,racks,gabinetesdebordeyequipamiento
deterreno
SRE 21–56 1.152 14S(768),14J(384)
8.2.4 Registroyreduccióndeladeudatécnicadurantelos36
mesesdeoperación
DES 21–56 2.304 09S(829,44),09J(552,96),08S
(345,6),08J(345,6),04(230,4)
8.2.5 Actualizacionesanualesdeloscomponentesdebaseduran-
telos36mesesdeoperación
SRE 21–56 288 14S(172,8),14J(86,4),24(28,8)
8.2.6 Revisionessemestralesdelasinstalacioneseléctricasdela
saladurantelos36mesesdeoperación
SRE 21–56 288 00(230,4),14S(38,4),14J(19,2)
8.2.7 Ciclodevidadelequipamientodurantelos36mesesde
operación:reposiciónydisposiciónfinal
SRE 21–56 864 14S(518,4),14J(259,2),24(86,4)
8.3.1 Innovación2:mantenimientodeescenariosderegresión
(INN-02.P4,segundaparte)
CAL 21–56 576 19S(399,27),19J(133,53),16(43,2)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
135

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
8.3.2 Innovación3:revisiónsemestraldeparámetrosdurantelos
36mesesdeoperación(INN-03.P5)
DAT 21–56 288 10S(153,6),10J(76,8),23(57,6)
8.3.3 Innovación4:líneabaseyliquidacionesensombra(INN-
04.P2)
JP 21–23 80 20(52),01(28)
8.3.4 Innovación4:liquidaciónmensualdeltramovariable,
meses24a56(INN-04.P3)
JP 24–56 528 20(343,2),01(184,8)
8.3.5 Innovación5:desplieguegradualporrutas(INN-05.P4,
segundaparte)
IMP 22–26 80 32(32),20(16),21(16),22(16)
8.3.6 Innovación5:bloque4condicionado(INN-05.P5) IMP 24–27 80 32(32),20(16),21(16),22(16)
8.4.1 Gestióndelacapacidadconproyeccióntrimestraldurante
los36mesesdeoperación
SRE 21–56 576 14S(345,6),14J(172,8),24(57,6)
8.4.2 Informesmensualesdeconsumodenube(FinOps)durante
los36mesesdeoperación
SRE 21–56 576 14S(345,6),14J(172,8),24(57,6)
8.4.3 Estimacionesanualesdelahuelladecarbonodelaopera-
ción
SRE 21–56 288 14S(172,8),14J(86,4),24(28,8)
8.4.4 Actualizacionessemestralesdeldepósitodecustodiade
fuentesdurantelos36mesesdeoperación
JP 21–56 288 20(187,2),01(100,8)
8.5.1 Dosjornadasanualesdeactualizaciónycapacitacióndel
personalnuevodurantelos36mesesdeoperación
IMP 21–56 1.152 22(864),20(115,2),32(115,2),21
(57,6)
8.5.2 MentoríaalequipotécnicodelCLIENTEdurantelosseis
mesesposterioresalmes21
IMP 21–27 80 32(32),20(16),21(16),22(16)
8.5.3 Mantenimientodelabasedeconocimientodurantelos36
mesesdeoperación,conmétricasdeuso
SRE 21–56 576 14S(345,6),14J(172,8),24(57,6)
continúaenlapáginasiguiente
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
136

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
Tabla23—continuación
EDT Partida Familia Meses HH PerfilyHH
9.1.1 Entregadelcódigofuente,lainfraestructuracomocódigoy
losprocedimientosdedespliegue
DES 21–21 80 12S(27,98),09S(18,02),12J(13,99),
09J(12,01),04(8)
9.1.2 Informedeleccionesaprendidasyarchivodelaimplemen-
tación
JP 21–22 80 20(52),01(28)
9.2.1 EjecucióndelPlandeReversibilidadyacompañamientode
90días
JP 54–56 80 20(52),01(28)
9.2.2 Certificadodedevoluciónoeliminacióndedatospersonales SEG 56–56 80 31E(64),13(16)
4.2.2 PuenteNOC SRE 16–20 3.672 30(3.672)
4.2.2 PuenteN1 SRE 16–20 5.664 17(5.664)
4.2.1 Restauracionesprevias SRE 13–15 48 14S(28,8),14J(14,4),24(4,8)
4.2.2 Restauracionesprevias SRE 16–20 48 14S(28,8),14J(14,4),24(4,8)
4.3.1 Restauracionesprevias SRE 19–20 32 14S(19,2),14J(9,6),24(3,2)
— ReservaprotegidaDES DES 13–20 2.048 09S(506,03),07S(392,48),09J
(337,36),08S(307,95),08J(307,95),
07J(196,23)
— ReservaprotegidaCAL CAL 13–20 1.024 19S(744,73),19J(279,27)
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
137

---

LafroXSpA FormularioT-15:Nivelaciónderecursos
## Referencias
LasfuentescitadasenesteformularioselistanenformatoAPA7.ªedición.LasBasesse
citaneneltextoconsudocumentoyelartículo,capítulo,secciónocódigodelrequisito.
• DireccióndelTrabajo.(s.f.). Código del Trabajo: artículos 35 y 35 ter y compendio de feriados
legales. https://dt.gob.cl/legislacion/1624/articles-95516_recurso_1.pdf
• DistribuidoraPuelcheS.A.(2026a). Bases Administrativas, Licitación TFEP-01/2026.
• DistribuidoraPuelcheS.A.(2026b). Bases Técnicas Transversales, Licitación TFEP-01/2026.
• DistribuidoraPuelcheS.A.(2026c). Bases Técnicas del Caso Logística.
• Malcolm,D.G.,Roseboom,J.H.,Clark,C.E.,&Fazar,W.(1959).Applicationofatechnique
forresearchanddevelopmentprogramevaluation. Operations Research, 7(5),646–669.
• ProjectManagementInstitute.(2017). Guía de los fundamentos para la dirección de proyectos
(Guía del PMBOK)(6.ªed.).ProjectManagementInstitute.
LafroXSpA
FormularioT-15
Mediafirma: AlexAravena
138
