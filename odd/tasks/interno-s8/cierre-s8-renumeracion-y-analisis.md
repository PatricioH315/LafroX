# Corrección de S8 y renumeración

Alcance: S8, anexos y T-16 dentro de LafroX. Los PDF de S4/S7/S9/S13 y sus formularios se consultan sin editarlos; sus huellas se conservan en `tmp/cierre-s8-base.json`. Se preservan las líneas que contienen «contenido academico».

## Cambios entregados

- 35 riesgos vigentes renumerados R-001–R-035 en orden de ID anterior, con actualización simultánea de registro, respuestas, coordinaciones, B/C, RBS y rankings. La Tabla 8.I.2 cubre los 51 identificadores anteriores y sus 35 destinos R o 16 destinos CI. Un número antiguo no se interpreta como el mismo riesgo vigente.
- Anexo 8.E: 16 soluciones de control interno con dueño, destino documental, prueba y condición de habilitación. Se resuelve la referencia al anexo ausente; el diseño y ejecución externos no se dan por realizados.
- Anexo 8.F: 35 fichas con plazos, responsables/apoyo, esfuerzo A/C y contingencia; 35 valoraciones residuales proyectadas; costo-beneficio y sensibilidad de las 15 respuestas altas/críticas iniciales.
- Anexo 8.G: FMEA de 15 modos con S/O/D/NPR inicial y posterior proyectado, fundamento de detección y acciones. NPR, exposición y HH se mantienen diferenciados.
- Anexo 8.H: conciliación y distribución propuesta por mes/perfil, exclusiones y directrices concretas para cronograma y flujo de caja.
- Anexo 8.I: 14 observaciones con pedido, fuente/página, respuesta, ubicación y estado, más equivalencias y sincronizaciones pendientes. La matriz no declara cierre total por describir trabajo futuro.
- T-16 conserva su tabla inicial de ocho columnas y agrega un resumen posterior T-16.2. Las fichas completas permanecen en los anexos, evitando confundir valoraciones iniciales y proyectadas.

## Hipótesis y números

p0, O/M/P, PERT, VE e impactos iniciales individuales se conservan. El registro inicial suma 1.183,11 HH; las 411,82 HH históricas de controles internos quedan excluidas de contingencia y gestión, sin considerarlas ahorro ni costo de control cierto.

Las nuevas p1, A y C son estimaciones explícitas de planificación, no datos históricos ni eficacia demostrada. A es revisión extraordinaria acumulada por riesgo, no trabajo ordinario de implementación; C es parte del PERT inicial H0, no un costo adicional a éste. L=H0-C. La división 60 % dueño y 40 % apoyo es una hipótesis de asignación de esfuerzo que debe contrastarse con la EDT; no acredita capacidad contratada.

B=p0H0-p1L; T=A+p1C; neto=B-T=(p0-p1)H0-A. Si p1=p0 no existe ahorro de atención por menor ocurrencia y el neto es -A. Se conserva el cálculo de los retornos menores que uno y se justifica el tratamiento por obligaciones sanitarias, de aceptación y continuidad, sin monetizar bienes o multas.

Resultados de la propuesta: A=180,00 HH; p1C=137,20 HH; p1L=683,93 HH; contingencia específica p1H0=821,13 HH; tratamiento esperado A+p1C=317,20 HH; total posterior A+p1H0=1.001,13 HH. No se suman otra vez exposición inicial, C y L. Los valores posteriores se calculan sin redondear; se muestran con dos decimales.

La antigua propuesta de gestión de 1.600 HH sin derivación se sustituye por un escenario de 160 HH: cuatro ciclos de 40, cada uno JP8+ARQ16+CAL8+SRE8, en bloques 1–12, 13–20, 21–38 y 39–56. La sensibilidad de dos ciclos por bloque daría 320 HH, sin adoptar ese importe. Es una tolerancia propuesta para asuntos emergentes no identificados; no financia de nuevo riesgos conocidos ni CI. Requiere autorización; no se cambia T-15 ni se libera capacidad aprobada.

Las 3.072 HH protegidas de S7 siguen siendo E1: 1.152 en 13–15 y 1.920 en 16–20, ya dentro de sus 220.023 HH programadas. Crédito inicial contra la nueva contingencia: cero hasta demostrar riesgo/paquete/perfil/mes coincidentes. La distribución mensual de 8.H es una propuesta de exposición, no ocurrencia cierta ni dotación disponible; redondeos de impresión se regularizan al cargar la planilla. Toda integración exige nivelación y revisión de ruta crítica sin convertir HH directamente a días.

## Pendientes expresos

La proyección conserva 1 crítico, 4 altos, 19 medios y 11 bajos. R-002, R-006, R-029, R-030 y R-031 tienen planes adicionales, plazos, escalamiento y bloqueo de habilitación. No se acredita todavía que sus consecuencias sean manejables; la observación correspondiente permanece parcial. En particular, no se inventa historia sanitaria ni se reduce su impacto por haber establecido un bloqueo.

Faltan integración y verificación externas de controles en S4/S9/S13, la sincronización de las referencias y la incorporación efectiva en S7/T-15 y flujo de caja. La excepción «contenido academico» se conserva por instrucción del autor y se registra como parcial respecto del pedido de quitar esa expresión.

El prompt `prompt-sincronizacion-s8.md` permite trabajar cada destino de forma independiente, tomando S8 y la equivalencia 8.I.2 como referencia común. No autoriza modificar aquí esos destinos ni sustituye sus comprobaciones.

## Validación

`tmp/verificar_cierre_s8.py` comprueba la equivalencia, consecutividad, conservación de valores iniciales, límites y factores, productos y zonas, FMEA, fórmulas de costo-beneficio/sensibilidad, planes adicionales, 56 meses, sumas y ausencia de cambios en fuentes externas/citas protegidas. Las verificaciones numéricas pasan. Los PDF se compilan con LuaLaTeX y se revisan visualmente; el detalle final de páginas y comprobación de copias se registra al entregar.

Entrega final verificada: S8 de 23 páginas, anexos de 121 y T-16 de 21. Las referencias están estabilizadas; no se detectan referencias indefinidas ni desbordamientos en los logs finales. Persisten mensajes preexistentes del motor sobre contracción de pegamento, sin defectos visibles en las páginas examinadas. Se revisaron las hojas de contacto de todas las páginas y detalles de fichas, residual, costo-beneficio, FMEA, reservas, distribución mensual, equivalencias, matriz, RBS, folios y firmas. La comprobación sobre los PDF confirma 35 ID en el registro inicial, 35 en su resumen posterior y los mismos 35 en RBS; no hay referencias «??». Las copias finales se publican en la raíz de LafroX y se verifican por SHA-256 contra la compilación.
