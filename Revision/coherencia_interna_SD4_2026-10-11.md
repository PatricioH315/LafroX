# LafroX — Ajustes de coherencia interna del Subdocumento 4

Fecha: 11 de octubre de 2026. Rama: `rama-md`. Base local: `9e4dce0`; la comparación con `origin/rama-md` en `4212f7c` no mostró diferencias en los tres entregables de `04_arquitectura/` antes de editar. No se realizó pull, commit ni push. Se conserva la exportación antigua no versionada `md para drive/`.

## Ajustes aplicados

| Tema | Correspondencia corregida | Motivo |
| --- | --- | --- |
| Autonomía y guías | 4.1.15, 4.2.2.1, 4.2.2.7, 4.2.5.1 y Anexo 4-J | Operación local no equivale a emitir una nueva guía sin ERP y comunicación tributaria. |
| Calidad | 4.1.3.5, 4.2.5.3, Anexos 4-J y 4-M | Se distingue bloqueo local de una nueva liberación por Calidad; no se afirma un acceso local todavía sin recorrido acreditado. |
| Firewall del ERP | 4.2.2.6 y T-11 F-03 | Las entradas restringidas no impiden la salida tributaria necesaria para INT-07. |
| Vigencias | 4.1.3.7 y 4.2.2.7 | La ruta física de 14,5 h no renueva una credencial de 14 h. |
| Propiedad de funciones | Anexos 4-A, 4-J y 4-V | M3 coordina el pedido, M2 retiene stock y M7 aporta el control de crédito; M2 consume el bloqueo térmico. |
| Alta disponibilidad | 4.2.4.3, Anexo 4-M y ADR-10 | Menos de un minuto se cuenta tras excluir al escritor anterior, no incluye intervención presencial. |
| Recuperación de Talca | 4.3.2.5–6, Anexo 4-M y ADR-09 | Detener DMS no excluye el escritor; perder cómputo no equivale a perder también LAN, firewalls y enlaces. |
| Orden de recuperación regional | Tabla 39 y Anexo 4-M | Reconectar dependencias antes de validar pedidos y cambiar el tráfico; el presupuesto conservador sigue siendo 135 min. |
| Cobertura regional | 4.2.3.1, 4.2.5.2, 4.3.2.1/5 y T-11 | La réplica de datos no restituye automáticamente frontend, AS2, rutas, caché ni ingesta IoT. |
| Mensajes | Tablas 26/33, A.10/A.32 y 4-W.5 | INT-04 es un subconjunto de INT-03. Totales sin doble conteo: 224.652/día normal y 342.933/día peak. |
| Cross-docking | Tabla 23 y Anexo 4-W.2/Tabla A.31 | El perfil global usa el agregado de las tres plataformas, no tres veces ese volumen. |
| Capacidad de API | Tabla 29, T-11, ADR-12 y Anexo 4-W.9 | La cota completa incluye 20 solicitudes/s del canal tradicional: 111,70 solicitudes/s y ocho tareas. |
| Sincronización | 4.2.6.7 y Anexo 4-W.6 | El promedio horario no garantiza diez minutos con retornos simultáneos; se distingue la sensibilidad de prueba. |
| Consulta sanitaria | Tabla 17, 4.2.4.5 y Anexo 4-M | El presupuesto regional de 135 min no acredita el objetivo específico inferior a dos horas. |
| Analítica y seguridad | 4.1.4.7 y Anexo 4-R | Consultas operativas por API no equivalen a BI directo al transaccional; OAuth no sustituye mTLS y los túneles usan IPsec/IKE. |
| Software | Anexo 4-P, Tabla A.19 | El inventario incluye el motor ExpressionLanguage ya declarado en 4.1.3.4. |

## Definiciones y evidencias aún necesarias

1. Acceso local de Calidad: definir y aceptar el recorrido de interfaz, dispositivo, verificación de identidad y auditoría. Mientras tanto, el bloqueo se conserva sin prometer nueva liberación sin nube.
2. Pérdida completa de sala de Talca: concretar procedimiento, equipos y tiempos para restituir la conectividad de piso; el ensayo debe incluirlos dentro del RTO. No se añadieron compras ni cantidades sin sustento.
3. Recuperación regional por servicio: concretar y medir la restitución de consola, rutas, AS2, caché e ingesta IoT, con sus configuraciones y contrapartes. La copia de temperatura en DynamoDB no demuestra recuperación de la ingesta.
4. Consulta sanitaria inferior a dos horas: demostrar un recorrido de consulta disponible antes de terminar la conmutación completa, o elevar la brecha para decisión. No se redujo artificialmente el presupuesto de 135 min.
5. Sincronización y credenciales: medir concurrencia y caudal; verificar que las ventanas reales de autorización cubran las operaciones de la ruta sin renovación offline supuesta.

Estos puntos distinguen coherencia documental de aceptación técnica. No se registran ensayos ejecutados, nuevas aprobaciones del CLIENTE ni revisión humana inexistente. T-12 y los demás subdocumentos permanecen intactos; corresponde revisar sus estados si las definiciones pendientes modifican el cumplimiento acreditable.

## Conservación y comprobaciones

Se mantienen los encabezados, las ocho capas, los doce módulos, los quince actores, las figuras y sus enlaces, y los registros de revisión humana. No se editaron LaTeX ni figuras. La comprobación de los enlaces internos explícitos no reemplaza una revisión visual del PDF ni la revisión de los servicios remotos.

Comprobaciones realizadas: 178 enlaces a anclas explícitas con destino presente y sin anclas duplicadas; encabezados y enlaces de figuras iguales a la base; totales de integración recalculados sin INT-04 como sumando adicional; capacidad de ocho tareas comprobada con 111,70 ÷ 14; secuencia regional con 135 minutos conservados; `git diff --check` sin errores. Un fetch al finalizar confirmó que no se publicaron diferencias nuevas en los tres archivos SD4 respecto de la base utilizada.
