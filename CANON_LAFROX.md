# Canon LafroX — decisiones transversales

Decisiones fijadas el 27-10-2026 para todos los subdocumentos. Ante cualquier diferencia entre subdocumentos, manda esta tabla. Fuentes: Aclaraciones de la licitación (AL), Bases Administrativas (BA), Bases Técnicas Transversales (BTT) y Bases Técnicas del caso (Caso).

| # | Tema | Regla |
|---|---|---|
| C1 | Nombres de archivo | `LAFROX-SubdocumentoN`, `LAFROX-SubdocumentoN-Anexos`, `LAFROX-Formulario-T-X`, sin guion antes del número y siempre en mayúsculas. ZIP: `SOBRE2_LAFROX_OFERTA_TECNICA_AAAAMMDD.ZIP` (AL §1; BA Art. 50.3). |
| C2 | IDs de riesgo | `R-001…` del Subdocumento 8. Los riesgos de adopción de las innovaciones 1 a 5 parten en `R-034`. El Subdocumento 13 cita esos IDs. No se usa `R8-xx`. |
| C3 | Mes 1 del contrato | Febrero de 2027 (supuesto de cálculo, consulta V-12; BA Art. 10 n.º 2). |
| C4 | Actas de las etapas | Dos actas por etapa: (a) acta de cierre de marcha blanca (BA Art. 17.3), al final del mes 15 / mes 20, que habilita el paso a producción del 05-05-2028 / 05-10-2028; (b) acta de aceptación H7 / H12, 29-05-2028 / 25-10-2028, dentro del mes 16 / 21. La Operación comienza con el paso a producción de la Etapa 2 (BA Art. 17.2 n.º 4). |
| C5 | Dotación de terreno | Preparadores: 120 en Talca y 60 en Concepción (S-39). Conductores: ≈200 (42 propios y ≈160 de transportistas). Tripulación: ≈244 (84 conductores y peonetas propios, más ≈160 conductores de transportistas). Se nombra siempre la métrica que se usa. |
| C6 | SOC | Propio. Opera en el Centro de Operaciones de Valparaíso (Av. Brasil 2241), 24×7, con analistas contratados como personal antes del mes 13 bajo el Encargado de Seguridad. No es una subcontratación (BTT RT-11.17). |
| C7 | Cobertura de pruebas | ≥ 70 % en lógica de negocio (BTT RT-04.11, bloqueante en integración continua); ≥ 80 % global (política interna, Subdocumento 1, sección 1.3); ≥ 80 % del código modificado en cada cambio (Formulario T-10). |
| C8 | Continuidad | RTO ≤ 4 h y RPO ≤ 15 min para servicios críticos (BTT RT-07.04), con tres caminos independientes por centro de distribución, alarmas de retraso de replicación a 5 y 15 min y medición en conmutación real (AL-DR-01 antes del H5 y del H10; semestral, BTT RT-07.07). No se plantean salvedades al compromiso. |
| C9 | Congelamiento | 1 al 25 de septiembre, todo diciembre y los tres primeros días hábiles de cada mes; ventana de despacho de 05:30 a 07:00 sin indisponibilidad (Caso, condición 8; RT-10.05). |
| C10 | Terminología | El Subdocumento 4 y el Formulario T-11 son el diccionario oficial de nombres. Ejemplos: «M12 Telemetría» y «Amazon ElastiCache (Valkey 8.1)», nunca «Redis». Los meses se escriben «mes N», nunca «MN». |
| C11 | Responsables | Sólo los 8 roles del proyecto: Jefe de Proyecto, Arquitecto de Solución, Líder de Desarrollo, Líder de Calidad, Líder de Operación/SRE, Encargado de Seguridad, Líder de Datos y Líder de Implantación y Gestión del Cambio. |
| C12 | Títulos oficiales | Los subdocumentos y formularios se nombran con su título de las Bases. Ejemplos: «Modelo y gestión de datos», «Formulario T-11: Especificaciones técnicas ofertadas», «Formulario T-19: Cartera de innovaciones». |
| C13 | Citas | Los documentos propios no se incluyen en Referencias. Se citan como remisión en el texto: «(Subdocumento 4, sección 4.2.3)» o «(Formulario T-15, sección 5)». Las Bases se citan con documento, capítulo o artículo y página: «(Bases Técnicas del caso, Cap. 7, p. 12)», «(Bases Administrativas, Art. 17, p. 13)» (AL §6). |
| C14 | Declaración de IA | Escala Ninguno / Bajo / Medio / Alto (AL §7.2); nunca «No aplica». Una sección sin figuras declara «Ninguno» en diagramas. Si se declara «Alto», la fila debe nombrar quién revisó y qué verificó. |
| C15 | Numeración de formularios | Cada formulario numera sus secciones desde 1, sin prefijo de capítulo. Se cita «Formulario T-X, sección N.M», sin «§». |
