# LafroX — Resultado de las mejoras de arquitectura lógica 4.1

Fecha: 5 de noviembre de 2026. Rama: `LafroX-Subdoc4.1-LateX-corrigiendo`.

Registro interno de ejecución y trazabilidad. Las fuentes contractuales siguen siendo LaTeX y PDF. Este registro no es un espejo Markdown del subdocumento ni acredita aprobación del solicitante.

## Cambios aplicados

| Acción | Observación atendida | Cambio y localizador |
| --- | --- | --- |
| M07 | Trazabilidad por familias insuficiente | 16 obligaciones individuales en Anexo 4-E, Tabla A.6a; cuatro recorridos críticos en cuerpo, Tabla 4.1-A. Origen, componente/capa, contrato, prueba y aceptación. |
| M08 | Identidad durante corte y relevos | Anexo 4-M: AL-OFF-01 ampliado y nuevo AL-ID-01; política en capas/ADR-06. Manifiesto de 26 h, antigüedad inicial máxima de 1 h, vigencia remanente mínima de 25 h y dos relevos en 24 h. |
| M09 | Credencial de 14 h frente a ruta de 14,5 h | Sección de conductores, capas y anexos G/H/P: asignación emitida dentro de la hora anterior a salir, fin programado más 30 min, máximo absoluto de 16 h desde emisión. Conservación de cola y bloqueo al vencer. |
| M10 | Controles y exposición residual | 4.1.12 y Anexo 4-R: escritor dueño, idempotencia, baja desconocida durante corte, ERP y bloqueo de frío. AL-MOD-01 y AL-FRIO-01 comprueban fronteras y autoridad de Calidad. |
| M11 | Cambio a Laravel no reconocido | 4.1.7.1 y ADR-23: antecedente Django del Informe 1, motivo de selección, contratos conservados y herramientas/pruebas afectadas. No se atribuye código previo migrado. |
| M12 | Existencia y compatibilidad de versiones | Anexo 4-P, Tabla A.20 consolidada: lanzamiento, restricciones y soporte de ocho productos; referencias oficiales y política de actualización. Se eliminó una tabla duplicada y se conservaron los números A.20/A.21. |
| M13 | Figura 1 ilegible | Nueva variante vectorial de navegación por ocho capas, con 12 módulos y separación entre bodega local, captura móvil y canales web. Letra mínima final de 10,41 pt. Original intacto. |
| M15 | Nombres M10/M11 inconsistentes | M10 Analítica y M11 Canal moderno en vista general y variantes de puertas de servicio, negocio e integración. Los originales se conservan. |
| M16 | Fuentes genéricas | Leyendas específicas de las figuras lógicas, dominio y protocolos; ajuste de tabla de eventos para evitar desbordes y guiones dentro de palabras de identificadores. |
| M19 | Extensión y repetición | Listados M2/M3/M4/M7 a 4-D, criterios de interacción a 4-N y custodia a 4-R; el cuerpo conserva decisiones y remisiones. |
| M20 | Revisión humana insuficientemente acreditada | Filas lógicas intervenidas distinguen revisión antes declarada de correcciones verificadas automáticamente. No se inventan revisores ni aprobaciones adicionales. |

## Alcance de las evidencias

Se comprobaron fuentes oficiales, coherencia temporal del diseño, nombres, estructura LaTeX, compilación, referencias y páginas renderizadas. AL-ID-01, AL-MOD-01, AL-FRIO-01 y AL-UI-01 son especificaciones nuevas de ensayo, con resultados esperados; no se ejecutaron contra una aplicación operativa. Tampoco se acredita una nueva revisión humana del contenido.

La cota temporal se comprobó para emisión al salir y 30/60 minutos antes: el fin de ruta de 14,5 h más 30 minutos queda cubierto sin superar 16 h desde emisión. La renovación horaria del manifiesto deja al menos 25 h para un aislamiento de 24 h. Es una comprobación del diseño, no una medición de un servicio desplegado.

## Preservación

- 34 archivos protegidos conservan sus huellas: fuentes de 4.2/4.3, T-11, memoria física, figuras físicas y AGENTS específico.
- Los cuatro PDF originales de figuras lógicas sustituidos en la inclusión permanecen idénticos a Git; se generan variantes con nombres nuevos.
- Filas de declaración no intervenidas conservadas; 4.2, 4.3 y T-11 no se editaron.
- Las 98 páginas de arquitectura física y centros de datos mantienen su extensión y secuencia de tablas. La comparación del texto renderizado solo detecta cifras de paginación/referencias recalculadas y espacios.
- Los cambios locales anteriores se conservaron. La ejecución inicial precedió al commit solicitado después por el usuario; su identificación se registra en el plan de integración. No se publicó la rama.

## Síntesis y distribución

El recuento por espacios de las fuentes del cuerpo 4.1 pasó de 29.005 a 27.048 palabras (aproximadamente −6,7 %). Su tramo dentro del cuerpo pasó de páginas 7–87 a 7–84: tres páginas menos. El PDF completo del cuerpo pasó de 194 a 192 páginas, incluida la declaración ampliada. Los anexos incorporan evidencia individual y protocolos, además del detalle trasladado: su extensión final es de 128 páginas, frente a 117 de la entrega anterior. El crecimiento corresponde a la evidencia individual, los protocolos y los catálogos concentrados, sin presentar pruebas como ejecutadas.

## Fuentes oficiales verificadas para M12

- Laravel 13: https://laravel.com/docs/13.x/releases
- PHP: https://www.php.net/supported-versions.php
- Angular, lanzamiento/soporte: https://angular.dev/reference/releases
- Angular, compatibilidad: https://angular.dev/reference/versions
- TypeScript 6.0: https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/
- Kotlin, historial y soporte de biblioteca estándar JVM: https://kotlinlang.org/docs/releases.html
- PostgreSQL: https://www.postgresql.org/support/versioning/
- RabbitMQ: https://www.rabbitmq.com/release-information
- Keycloak 26: https://www.keycloak.org/2024/10/keycloak-2600-released
- Node 22.22.3: https://nodejs.org/en/blog/release/v22.22.3

Verificación documental del 5 de noviembre de 2026 contra la fecha de oferta del 12 de octubre de 2026. La disponibilidad publicada no sustituye la construcción y regresión del conjunto exacto de dependencias.

## M22 — Comprobación final

Verificación terminada:

- Tres pasadas de LaTeX de cada entregable final; sin referencias indefinidas, etiquetas múltiples, destinos duplicados ni desbordes.
- Revisión visual de 4.1 y declaración mediante contactos de páginas; inspección detallada de Figura 1, recorridos críticos, identidad, matrices de anexos, soporte, protocolos y tabla de eventos.
- Figura 1: 10,41 pt mínimos al tamaño final; fuente vectorial. Las figuras lógicas originales permanecen intactas.
- 34 archivos protegidos con las mismas huellas; comparación de 98 páginas físicas sin cambios léxicos tras descontar cifras de paginación/referencias y espacios.
- `git diff --check` sin observaciones; rama de ejecución confirmada.

Localizadores finales principales: cuerpo, Figura 1 p. 13; Tabla 4.1-A p. 51; cambio de backend p. 66. Anexos: Tabla A.6a p. 19; AL-ID-01 pp. 40–41; Tabla A.20 pp. 71–72; AL-MOD-01/AL-FRIO-01/AL-UI-01 p. 94. La Tabla A.21 conserva su número.

Archivos de entrega y huellas SHA-256:


- `D:/Usuario/Documents/Proyecto_Lafrox/LafroX-rama-latex/entrega/LAFROX-Subdocumento4.pdf` — 192 páginas; SHA-256 `da0d14adb320e729cba0a7367ae741dda35284040ab131aa2a4379d055e85d82`.

- `D:/Usuario/Documents/Proyecto_Lafrox/LafroX-rama-latex/entrega/LAFROX-Subdocumento4-Anexos.pdf` — 128 páginas; SHA-256 `7c68dafc0349b8342ca4171c90567c41556e9cfdc028c181583de00fb1cba5db`.

Respaldo, registros de compilación y comprobaciones: `D:/Usuario/Documents/Proyecto_Lafrox/tmp/sd41_ejecucion_20261105/`. El estado documental está implementado y verificado; no se acredita revisión humana adicional ni ensayos funcionales sobre un sistema operativo.
