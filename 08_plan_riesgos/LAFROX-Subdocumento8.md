# LafroX — Subdocumento 8: Plan de riesgos

# Introducción a los Riesgos

La solución de LafroX integra recepción y trazabilidad, inventario, frío, preventa, reparto y cobranza en E1, y canal moderno, portales y costo de servir en E2. Sus riesgos dependen de una operación que despacha 96 camiones entre 05:30 y 07:00, mantiene los CD 24 horas sin WAN y el terreno 14 horas sin señal, conserva ERP como único emisor tributario y despliega sin detener rutas. Este plan conecta las decisiones comerciales del SD2, alcance del SD3, contratos y dimensionamiento del SD4, gobierno del SD6 y programación del SD7. No utiliza el SD5 aún no consolidado.

El cuerpo establece método y decisiones; los Anexos 8.A–8.F contienen registro ampliado, FMEA, escenarios, reservas y condiciones de evidencia; el T-16 conserva el formato obligatorio separado. La viabilidad del planteamiento no equivale a factibilidad demostrada: existen condiciones de evidencia y una brecha residual de RPO que requieren resolución antes de declarar cumplimiento integral.

## 8.1 Plan de riesgos

Esta sección define cómo se gestionan los riesgos durante los 56 meses: el ciclo y sus instancias, los roles y su autoridad, las escalas con que se analizan y las reglas de registro y cierre.

### 8.1.1 Enfoque y ciclo

El registro vivo sigue identificación, análisis, respuesta y seguimiento conforme a BTT RT-19.04 y al enfoque ISO 31000 exigido por las Bases. Cada entrada distingue causa, evento incierto y consecuencia, sin convertir una inconsistencia observada en riesgo futuro. El Anexo 8.E separa problemas y dependencias actuales. Este método no constituye certificación de LafroX.

JP mantiene el registro único. Los líderes identifican riesgos al revisar interfaces, pruebas, capacidad y despliegues; verifican disparadores semanalmente y ante cada cambio. El Comité de Proyecto quincenal revisa todos los riesgos abiertos, responsables, plazos y evidencia. Los comités Ejecutivo y de Arquitectura mensuales deciden escalamiento y cambios de sus ámbitos, y desde el mes 13 el Comité de Operación mensual revisa los riesgos de servicio: niveles de atención, incidentes, capacidad y continuidad (SD6, sección 6.1.6). Una amenaza a continuidad, seguridad o hito se escala inmediatamente. Marcha blanca exige seguimiento diario; operación mantiene vigilancia diaria de incidentes y colas y revisión en comités.

### 8.1.2 Roles y autoridad

La tabla asigna a cada líder del proyecto su responsabilidad en el registro de riesgos.

| Rol | Responsabilidad |
| --- | --- |
| JP — Alex Aravena | Registro, fechas, contraparte, recursos y escalamiento |
| ARQ — Bastián Trejo | Interfaces, portabilidad, continuidad y resolución propuesta de RPO residual |
| SEG — Álvaro Catalán | Seguridad, acceso, datos y respuesta a incidentes |
| DAT — Leandro Chamorro | Migración, conciliación, trazabilidad y modelos |
| DES — Tomás Pérez | Módulos, integración, idempotencia y equipos separados E1/E2 |
| CAL — Maximiliano Miño | Pruebas, criterios y evidencia de cierre |
| SRE — Guillermo Castillo | Capacidad, infraestructura, enlaces, continuidad y atención |
| IMP — Patricio Henríquez | Olas, usuarios, formación, acuerdos y adopción |

Dirigen equipos; no ejecutan solos todas las HH. La Contraparte Técnica del CLIENTE acepta entregables mediante actas; Operaciones autoriza cortes y continuidad de su ámbito; Calidad del CLIENTE valida decisiones sanitarias. No se presume disponibilidad ni aprobación de esas contrapartes. Los cambios físicos siguen el gobierno de arquitectura, sin modificar silenciosamente SD4/T-11.

### 8.1.3 Escalas previas al análisis

P/I/D son juicios ordinales iniciales sustentados en exposición y controles descritos; no frecuencias medidas ni porcentajes. Horizonte: hasta entregar el control de cada ficha y, para riesgos recurrentes, los 56 meses del contrato. Cambiar el horizonte exige reevaluación.

| Valor | Probabilidad ordinal P | Impacto I: mayor efecto aplicable | Detección D: mayor valor, peor detección |
| --- | --- | --- | --- |
| 1 | Excepcional, sin dependencia expuesta identificada | Corrección local sin afectar aceptación ni servicio | Control automático probado detecta antes de confirmar |
| 2 | Posible con exposición limitada | Retrabajo absorbible en capacidad asignada | Ensayo sistemático detecta antes de habilitar |
| 3 | Plausible por una dependencia expuesta | Consume contingencia o afecta servicio auxiliar | Requiere conciliación o ensayo específico |
| 4 | Exposición recurrente o varias dependencias sin control demostrado | Amenaza hito, SLA o alcance obligatorio | Se aprecia al afectar operación o en revisión tardía |
| 5 | Condiciones muy favorables al evento sin barrera eficaz | Detiene despacho crítico, compromete seguridad/datos/sanidad o impide aceptación | Sin evidencia de detección o reconocible después de pérdida |

Exposición E = P × I (1–25): baja 1–3, moderada 4–7, alta 8–14 y crítica 15–25. FMEA agrega NPR = P × I × D (1–125), para ordenar dentro del nivel; desempates por impacto y proximidad del plazo. I = 5 exige escalamiento aunque E no alcance 15. No se asigna D = 1 a un control por describirlo. Estas escalas no estiman pérdida monetaria ni probabilidad estadística.

### 8.1.4 Registro y cierre

El responsable actualiza fuente, estado, disparador, tratamiento, consumo de HH y evidencia. Estados: identificado, en tratamiento, control verificado o materializado. Materializar el evento abre un problema y conserva su ID. CAL verifica cierre técnico; JP registra la decisión; la aceptación contractual corresponde al CLIENTE. La puntuación residual se estima después de comprobar controles, no por asignar una mitigación. Ninguna aceptación de riesgo exime requisitos obligatorios.

## 8.2 Identificación y Análisis de Riesgos

Esta sección identifica los riesgos con una RBS y los analiza en dos niveles: uno cualitativo con FMEA y otro cuantitativo con escenarios deterministas y el PERT del cronograma.

### 8.2.1 RBS y análisis separados

La RBS textual tiene raíz «Riesgos de la propuesta LafroX» y tres ramas: solución, desarrollo e implantación. Cada rama clasifica riesgos técnicos, organizacionales, de proyecto, seguridad y operación. Los IDs son únicos aunque una causa afecte varias ramas. Esta representación permite revisar relaciones en Markdown; no acredita revisión visual de una figura final.

Solución: integridad de stock/custodia, ERP/DTE, autonomía, capacidad, RPO, seguridad, obsolescencia y proveedores. Desarrollo: interfaces sin documentación, recursos, contrapartes, conocimiento de rutas, migración y certificación externa. Implantación: congelamientos, cuatro semanas completas, suministros, adopción, relevos y atención. Anexo 8.A desarrolla 30 amenazas; 8.F cubre las cinco innovaciones y una oportunidad de diagnóstico con INN-02. Las tres ramas permiten preparar los análisis separados exigidos por T-22.

### 8.2.2 Resultados cualitativos y FMEA

Anexo 8.B presenta P/I/D, exposición y NPR. La prioridad inicial se concentra en continuidad, RPO, ERP/DTE, seguridad, capacidad y aceptación. T-16 compara exposición; NPR no reemplaza su columna Expos.

No se suman puntuaciones como probabilidad del proyecto. Las relaciones importan: ausencia de contraparte puede atrasar interfaces/cadenas y eliminar semanas de evidencia; migración deficiente puede invalidar trazabilidad y aceptación. Los mismos efectos o consumos no se contabilizan dos veces.

### 8.2.3 Escenarios cuantitativos

Se aplica FMEA y escenarios deterministas, sin Monte Carlo. Anexo 8.C calcula retrabajo, perfiles, duración, demoras de hitos y límite de activación. T-15 programa 202.774 HH, con soporte puente de 9.336 HH y reserva E1 de 3.072 HH ya incluidos; la mesa y el SOC siguen las posiciones del SD4 y el calendario real. El máximo mensual es 66 personas equivalentes en el mes 16; no demuestra contratación ni cobertura por subventana, y la dotación declarada en el SD1 no cubre SEG ni IMP sin contratación o subcontratación (T-15 §5.7). Horas de atención tampoco prueban SLA.

La red agregada reconciliada incluye medio mes de revisión del CLIENTE antes de cada hito y deja reserva de calendario cero antes de H4/H5/H9/H10. Su PERT de duración da σ = 0,51 mes en el camino al H4 y 0,53 al H5: cada hito tiene 50 % de probabilidad de cumplirse, y el 90 % exigiría 0,65 y 0,67 mes de reserva (T-15 §5.3). Una reserva en meses 13–20 no subsana retraso anterior a H5. Las marchas blancas y sus últimas cuatro semanas no son reserva. Febrero de 2027 es ejemplo compatible con E2 en octubre de 2028; V-12 debe confirmar fecha y calendario hábil, preservando producción antes de enero de 2029.

## 8.3 Plan de Acción a Riesgos

Esta sección fija las respuestas a los riesgos analizados, las reservas que las financian en horas y las condiciones que deben cumplirse antes de declarar factible la propuesta.

### 8.3.1 Respuestas y costo-beneficio técnico

Cada ficha 8.A fija responsable, disparador, plazo, mitigación, contingencia y evidencia. Evitar se aplica a cortes inseguros, facturación diferente del pedido y liberación sanitaria sin evidencia; reducir, a controles y pruebas; compartir responsabilidades, a acuerdos externos. Contratar un tercero no transfiere la obligación final de LafroX. La atención auxiliar en contingencia no acredita capacidades obligatorias desactivadas.

El costo-beneficio compara HH de prevención/verificación con retrabajo y afectación de servicio/hitos, según 8.C. Los 160/320 HH derivan de clases del T-15; son referencias supuestas, no ensayos ejecutados ni ampliaciones aprobadas. El cumplimiento obligatorio prevalece sobre el cociente de ahorro. Valorización, tarifas y reservas monetarias corresponden exclusivamente a la Oferta Económica (BA Art. 50.2).

### 8.3.2 Reservas y cronograma

Anexo 8.D distingue la capacidad protegida E1 de 3.072 HH, ya incluida; el soporte puente de 9.336 HH como servicio base; contingencias dimensionadas fuera del T-15 con su ventana: 400 HH de integración E1 en los meses 7 a 11, 400 HH de integración E2 en los meses 15 a 18, 442 HH/mes de atención si la demanda supera 2.200 contactos y 2.464 HH por cada cuatro semanas de extensión de marcha blanca; y la reserva de gestión para riesgos no identificados. Cada contingencia se dimensiona con el mayor escenario individual de su ámbito, sin sumar escenarios del mismo defecto ni prestarse entre etapas. JP solicita su uso al Comité Ejecutivo con causa, perfiles, ventana e impacto; los montos pertenecen a la Oferta Económica (Art. 50.2). No se inventa un porcentaje.

Cada uso registra un cargo único por evento/mes/perfil y remanente. Riesgos correlacionados comparten consumo real; E1 no presta su reserva a E2. Los recursos adicionales requieren actualizar T-15 y calendario, sin ampliar automáticamente los 56 meses. Los meses 21 y 22 separan 2.834,54 HH de cierre y estabilización de implementación de la operación.

### 8.3.3 Factibilidad y aceptación

Anexo 8.E registra condiciones actuales: productividad/dotación, secuencias diarias y plazos de revisión/subsanación del Art.18.3, fecha contractual, continuidad de 96 despachos, RPO remoto, atención y evidencia láctea. La física del SD4 permanece intacta: A31/A32 ya incluyen CD-05; se necesita contrastar multiplicidad y drenaje. El límite residual RPO requiere resolución, no aceptación como sustituto de cumplimiento.

No se autoriza corte sin continuidad medida ni aceptación sin las seis condiciones simultáneas del Art. 17.3 y acta según Art. 18. La suspensión láctea de septiembre de 2026 es antecedente ocurrido; V-13 debe precisar evidencia y restitución con CLIENTE/proveedor. El proyecto no demuestra una solución retroactiva. La conclusión es viabilidad propuesta con condiciones de cierre identificadas; la factibilidad integral requiere resolver brechas y aportar decisiones, pruebas y actas.

## Referencias

- Distribuidora Puelche S.A. (2026). Bases Administrativas TFEP-01/2026, artículos 17, 18, 50.2 y formularios T-16/T-22.
- Distribuidora Puelche S.A. (2026). Bases Técnicas Transversales, RT-07.04/07, RT-19.04, RT-21.06/07 y RT-26.04.
- Distribuidora Puelche S.A. (2026). Caso 02 — Logística, capítulos 10–14 y requisitos específicos citados.
- Aclaraciones de licitación (2026), capítulo 8 y reglas de presentación.
- LafroX. SD1–4, SD6 y SD7, con anexos y formularios citados. SD5 no utilizado.
- International Electrotechnical Commission. (2018). *IEC 60812:2018 Failure modes and effects analysis (FMEA and FMECA)*. IEC.
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. ISO.
- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.), capítulo 11. Project Management Institute.

## Declaración de uso de IA

Codex y Claude Code apoyaron la redacción, la organización, el análisis ordinal FMEA y los cálculos deterministas. No se generaron imágenes; la RBS se representa textualmente. Esta declaración no acredita ensayos ejecutados, aprobación del CLIENTE ni conformidad formal de una presentación final, y se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Introducción | Codex | Redacción a partir de SD2–SD4, SD6 y SD7 (6 de octubre de 2026) | Alto | Ninguno | No documentada |
| 8.1 Plan de riesgos | Codex; Claude Code | Método, roles y escalas; Comité de Operación y textos de sección (7 de octubre de 2026) | Alto | Ninguno | No documentada |
| 8.2 Identificación y Análisis de Riesgos | Codex; Claude Code | RBS textual, FMEA y escenarios; actualización con el T-15 y el PERT (7 de octubre de 2026) | Alto | Ninguno (RBS textual) | No documentada |
| 8.3 Plan de Acción a Riesgos | Codex; Claude Code | Respuestas, reservas y factibilidad; contingencias dimensionadas (7 de octubre de 2026) | Alto | Ninguno | No documentada |
| Anexos 8.A a 8.F | Codex; Claude Code | Ver la declaración de los anexos | Alto | Ninguno | No documentada |
| Formulario T-16 | Codex; Claude Code | Ver la declaración del formulario | Alto | Ninguno | No documentada |
