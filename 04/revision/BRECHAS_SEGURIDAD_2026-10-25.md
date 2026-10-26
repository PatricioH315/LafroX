# Brechas de seguridad: conversación y aplicación

## Estado y límites

Continuación autorizada por el usuario. Se aplica el diseño documental del borde AS2. Las otras tres brechas no se declaran resueltas. No se modifican SD7, HH, cronogramas, T-13, simulaciones ni la conciliación de SD8/SD9. No se ejecuta una nueva revisión completa de admisibilidad antes de resolver las decisiones restantes.

| Brecha | Tratamiento actual | Condición para el cierre |
|---|---|---|
| MFA externo: RF-15.03 / RT-12.03 | En conversación. Solo el portal de clientes es opcional para comprar; no se llamó opcional al portal de transportistas/proveedores como obligación operativa. | Definir factores por perfil y recuperación, comprobar aplicación en todas las entradas, sin cuenta/teléfono obligatorio para la compra asistida ni conexión permanente en terreno. |
| AS2: RT-11.07 | Aplicado documentalmente: CloudFront/WAF/Shield → ALB restringido → 2 OpenAS2 privados en 2 AZ. T-12 pasa a Cumple como diseño comprometido, no como ensayo ejecutado. | Interoperabilidad firmada/cifrada y MDN por cadena; pruebas negativas y costeo de recursos. |
| TLS: RT-11.08 | Sigue Cumple parcialmente. No se editó la excepción previa mientras se discute su sustitución. | Levantar protocolo ERP/terceros; TLS 1.3 en cada tramo o modificación/aclaración formal de bases que admita la limitación. No basta un proxy que oculte un tramo TLS 1.2. |
| Vulnerabilidades: RT-11.04 | Sigue Cumple parcialmente. | Resolver formalmente la coexistencia de máximos 7/15/30 días y prohibición de intervenir sistemas. Contener, aceptar riesgo o remediar al terminar el congelamiento no equivale a cumplir los máximos. |

## AS2 aplicado

- Una distribución CloudFront y ACL WAF dedicadas globales; un ALB por región habilitada sustituye al NLB. Se conservan las dos tareas privadas por región habilitada y los acuerdos por cadena.
- Lista administrada de prefijos CloudFront y encabezado de origen secreto, regla predeterminada 403 y tareas accesibles solo desde el ALB. No se usan valores secretos de ejemplo en los fuentes.
- TLS 1.3 en los tres tramos; la política automática ALB de backend no se describe falsamente como una política personalizada TLS-1.3-only: es el destino OpenAS2 el que rechaza versiones anteriores.
- Cuerpo MIME intacto, sin caché/compresión, POST y rutas autorizadas, control de IP/tasa y reglas gestionadas/personalizadas sin bypass general ni retos de navegador. WAF no descifra ni valida el EDI cifrado; OpenAS2/M11 lo hacen después.
- Límite de sobre propuesto: 32 MiB, verificable incluso sin Content-Length. No es una cifra de las bases: se comprueba contra el mayor mensaje de cada cadena en la aceptación. Acuse síncrono hasta 30 s y alternativa MDN asíncrona firmada; timeout de origen/ALB 60 s, reenvío y deduplicación por Message-ID. No se confunde MDN con aceptación comercial.
- Alineados: nube, conexiones/superficie, segmentación, Anexo 4-N/P/R, ADR-11, T-11, figuras físicas general/nube y RT-11.07 de T-12. Se conservaron todas las figuras originales. La nueva vista de nube distingue el ingreso de frío por IoT Core/CloudConnect del tráfico de aplicaciones.
- Costeo: contabilizar ALB/LCU, distribución/solicitudes/transferencia y ACL/reglas/solicitudes; descontar el NLB sustituido. Se registra para conciliación económica, sin inventar precios ni modificar SD7. No se afirma costo neto cero ni se altera una oferta económica no examinada.

## Dos consultas concretas para resolver restricciones reales

**TLS:** BA 21.2 y RT-11.08 exigen TLS 1.3. El caso cap.10 restricción4 prohíbe modificar o reemplazar el ERP y cap.5 no documenta sus interfaces. Solicitar el protocolo real y aclarar qué integración externa, sin modificar el ERP, es admisible si el extremo legado no soporta TLS 1.3. Una autorización comercial del fabricante no sustituye una aclaración de bases. No prometer un ERP diferente, escrituras SQL directas ni otro emisor tributario.

**Parches:** BA 21.1 y RT-11.04 fijan máximos; el caso cap.10 restricción8 prohíbe intervenir sistemas del 1 al 25 de septiembre, diciembre y los primeros tres días hábiles del mes. Solicitar que se precise formalmente el procedimiento y prelación de cambios de seguridad que deban ejecutarse dentro del congelamiento, responsables de autorización y plazos que permitan cumplir los máximos. BA 5.3 fija prelación y BA 5.4 exige consultar contradicciones; no se atribuye aprobación anticipada del CLIENTE ni se supone que blue/green deja de ser intervención.

## Verificación y alcance de rollback

Ejecutar `verificar_borde_as2.py --sd3 <worktree SD3>`. El JSON asociado conserva las comprobaciones y hashes actuales. Las compilaciones/inspecciones visuales verifican maquetación, no comportamiento AS2 real. Harness de runtime: **no disponible**, este repositorio contiene una oferta documental; los casos de ensayo quedan comprometidos, no ejecutados.

Unidad de trabajo: borde AS2, su inventario/trazabilidad, dos figuras derivadas y fila RT-11.07 de T-12. Para revertirla, usar el diff y `BASELINE_PRE_AS2_2026-10-25.json`; no revertir los cambios previos de frío ni restaurar archivos enteros que también los contienen. Sin commit ni push.

## Fuentes técnicas contrastadas

- [AWS: proteger ALB con encabezado de origen y prefijos de CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html).
- [AWS: comportamiento de solicitudes POST, cabeceras y TLS de CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html).
- [AWS: políticas TLS del ALB y política automática al backend](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html).
- [Keycloak: autenticación y flujos](https://www.keycloak.org/docs/latest/server_admin/index.html#_authentication-flows), para la propuesta MFA aún no aplicada.

## Resultado de la comprobación documental

39 comprobaciones correctas. PDF actuales: SD4 195 páginas, anexos 116, T-11 46 y T-12 264. T-12 conserva 653 IDs y exigencias literales; cuenta 597 Cumple / 34 Cumple parcialmente / 22 No cumple. Solo cambian RT-26.01 (frío previo) y RT-11.07 (AS2) contra HEAD de SD3. Los tres PDF de SD13/T-19 mantienen los hashes de la corrección anterior.

Inspección visual: figuras física general/nube; nueva sección AS2 (p.148), Anexo 4-R (p.73), T-11 (p.33) y T-12 (p.197). Sin nuevos Overfull, referencias indefinidas ni glifos faltantes en el cuerpo; anexos conservan cuatro avisos menores preexistentes de Anexo 4-A (1,23–1,52pt), sin editarlo. Los PNG originales versionados son idénticos a HEAD; los draw.io originales locales siguen disponibles pero no están en HEAD, por lo que no se les atribuye esa comparación histórica.
