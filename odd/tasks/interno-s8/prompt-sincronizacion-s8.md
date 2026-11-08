# Prompt para sincronizar cada subdocumento de forma independiente

Trabaja únicamente en el subdocumento que se te asigne y sus formularios/anexos. Consulta S8 y los demás documentos sin modificarlos. La referencia vigente es el conjunto `LAFROX-Subdocumento8.pdf`, `LAFROX-Subdocumento8-Anexos.pdf` y `LAFROX-Formulario-T-16.pdf`, con los anexos E–I de la revisión de cierre. Respeta correo principal, Bases Administrativas y observaciones del Informe 2. No presentes modelos o pruebas previstos como resultados ejecutados.

Primero consulta la Tabla 8.I.2: el registro vigente es R-001–R-035. Los ID anteriores de R-001–R-051 son históricos; un mismo número puede representar hoy otro evento. Usa la equivalencia por descripción/causa/evento, no una sustitución global. Los 16 controles CI mantienen su sufijo histórico y no son riesgos declarados al CLIENTE. Al terminar, verifica todas las referencias en el documento asignado y registra los cambios necesarios en los demás sin ejecutarlos.

## Si el destino es S4 y T-11/anexos de arquitectura

Integra las soluciones de la Tabla 8.E.1: CI-009/010 (idempotencia POS y continuidad del servicio de mapas), CI-023–027 (seguridad, terminales, autenticidad EDI, defensa de canales, privilegios/recuperación) y CI-047/048/050 (capacidad efectiva, identidad/relevos y stock/autoridad única). Define componentes, contratos, secuencias de fallo/recuperación, invariantes y controles; no te limites a remitir a S8. Contrasta el diseño existente antes de añadir tecnología. Mantén separados manifiesto 26 h, caché 24 h y credenciales 8/14 h; demuestra cómo se resuelven los relevos de 8/16 h con 24 h sin WAN, sin renovar por silencio ni emitir identidades locales no autorizadas. No declarar resuelta esa continuidad sin una secuencia consistente. Conserva RTO 4 h/RPO 15 min, guías tributarias válidas y la dependencia del ERP del CLIENTE, que LafroX no modifica. Actualiza cada referencia a T-16 con 8.I.2 y deja casos de prueba identificables para S9/T-13.

## Si el destino es S13 y T-19/anexos de innovaciones

Integra CI-034–038 y CI-040 como diseño y validación interna: indicador, control, responsable, evidencia y condición de habilitación; no como defectos transferidos al CLIENTE. CI-034 mantiene paquete 3.10.1.4 meses 11–15, H5 en 11–12, piloto real 13–15 e I-01A en mes 15 con ≥70 % de aciertos y ≥100 avisos evaluables. DAT dirige, IMP coordina piloto y Comercial/Calidad validan catálogo en 7–9. Conserva captura sanitizada antes de salir del terminal, diagnóstico base de INN-02, RNG-04 y fecha impresa de INN-03, bloqueo de inferencia con historia incompleta y validación de comprensión/privacidad de INN-05. La liquidación contractual de INN-04 corresponde al vigente R-027 (histórico R-039); no la confundas con el control de cuentas administrativas CI-027. Alinea valoraciones con 8.F sin presentar p1 como eficacia observada.

## Si el destino es S9 y T-13/T-17/anexos de calidad

Incorpora los controles de 8.E.1 y los modos FMEA de 8.G.1 a casos concretos: requisito, versión, ambiente, juego/escenario, resultado esperado, responsable, evidencia y regresión. Conserva puertas G4/G5 y bloqueo de defectos críticos/altos y pruebas habilitantes fallidas. La eficacia posterior de 8.F es proyectada: no escribir que las pruebas se ejecutaron si no existe evidencia. Mantén el cierre separado de aceptación contractual y comprueba identidad/relevos, autoridad única de stock, capacidad por ventana y dependencia ERP, además de controles de innovaciones. Evita duplicar controles compartidos en la EDT.

## Si el destino es S7 y T-14/T-15/T-18/anexos de planificación

Carga sólo una propuesta conciliada. S8 conserva 1.183,11 HH de exposición inicial; la propuesta posterior es A=180,00 HH planificadas y p1H0=821,13 HH de contingencia específica. Dentro de p1H0 están p1C=137,20 HH y p1L=683,93 HH: no sumarlas otra vez. A+p1H0=1.001,13 HH. La reserva de gestión propuesta es 160 HH derivadas de cuatro ciclos emergentes de 40 (JP8+ARQ16+CAL8+SRE8); las antiguas 1.600 HH quedan sustituidas como propuesta sin base, no como autorización de liberar capacidad.

Consulta 8.H para ventanas, perfiles, exclusiones y sensibilidad. Mantén las 3.072 HH protegidas ya programadas en E1 (1.152 en 13–15 y 1.920 en 16–20) sin sumarlas de nuevo al total programado ni prestarlas a E2. El crédito demostrado inicialmente es cero: reconoce solapamiento sólo con evidencia de mismo riesgo/paquete/perfil/mes y resta una sola vez. No conviertas las 411,82 HH históricas de los CI en costo de control ni reserva.

Relaciona cada ficha con su paquete real de EDT y capacidad ya prevista; descuenta prevención o atención ya presupuestada. Nivelar la propuesta mensual de 8.H.2–3, con DAT/IMP como familia y SRE como responsable desde mes 22, sin duplicar dotación. No convertir HH directamente en días. Recalcula precedencias, ruta crítica y holguras; respeta congelamientos, hitos y las cuatro semanas finales de evidencia. Si no cabe, plantea medidas y decisión formal antes del hito, sin afirmar capacidad disponible ni mover fechas unilateralmente. Entrega al modelo económico la misma diferencia mensual/perfil para valorización con tarifas netas documentadas, sin modificarlo si no es tu documento asignado.

## Si el destino es S6 u otra matriz transversal

Aplica equivalencias 8.I.2, conserva autoridad y responsabilidad de LafroX y actualiza instancias de decisión, contrapartes y plazos de 8.A/8.F. No declares aceptada una dependencia por silencio. Para promoción regional conserva suplente a 15 min y decisión máxima 30 min, sujeto a SLA más exigente. Las coordinaciones no transfieren al CLIENTE una obligación de diseño.

## Criterio de cierre y entrega

Compila el documento asignado y revisa visualmente tablas, folios, firmas y referencias. Entrega matriz observación–respuesta–sección modificada, resultados de comprobación y referencias aún pendientes en otros documentos. Los cinco riesgos posteriores R-002, R-006, R-029, R-030 y R-031 continúan críticos/altos en S8: conserva su plan adicional y bloqueo; no bajes puntuaciones para declarar cumplimiento. Se requiere evidencia o decisión contractual fundada para cerrar su nivel manejable. Ninguna aceptación exime requisitos obligatorios. No modificar las citas protegidas que contienen «contenido academico» cuando aparezcan en el alcance asignado.
