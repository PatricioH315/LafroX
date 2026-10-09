# Informe de revisión T-12 — Lote B1

Rango revisado: RT-02.01 a RT-07.14. La salida contiene las 130 filas del rango. La columna «Descripción» se conserva literalmente desde el T-12 de origen.

Abreviaturas de evidencia: SD4 = LAFROX-Subdocumento4.md; SD4-Anexos = LAFROX-Subdocumento4-Anexos.md; SD5 = LAFROX-Subdocumento5.md; SD5-Anexos = LAFROX-Subdocumento5-Anexos.md; SD6 = LAFROX-Subdocumento6.md; SD8-Anexos = LAFROX-Subdocumento8-Anexos.md; SD13 = LAFROX-Subdocumento13.md; T-11, T-14 y T-19 corresponden a sus respectivos formularios LafroX.

## 1. Tabla de cambios

| ID | Estado antes → después | Qué cambió y por qué |
| --- | --- | --- |
| RT-02.04 | Cumple → Cumple | Se corrigió el registro a ADR-01–ADR-22, porque SD4 declara 22 decisiones. Evidencia: SD4 §4.1.11; SD4-Anexos §4-O, Tabla A.17. |
| RT-02.10 | Cumple parcialmente → Cumple parcialmente | Se identificó lo cubierto por ECS Fargate y se explicitó la falta de escalamiento de integración, umbrales, límites y costo. Evidencia: SD4 §4.2.4.1.1 y §4.2.6.9. |
| RT-02.12 | Cumple → Cumple parcialmente | Las subredes reservadas no desarrollan la parametrización de nueva bodega, rutas y cartera requerida por el caso. Evidencia: SD4 §4.1.4.3 y §4.2.4.2, Tabla 15. |
| RT-03.03 | Cumple parcialmente → Cumple parcialmente | Se precisó que falta documentar la creación de la cuenta raíz inicial y excluir explícitamente la creación manual de otros recursos. Evidencia: SD4 §4.1.7 y §4.2.4.2; SD4-Anexos §4-O y §4-P; T-11, fila F-02. |
| RT-03.06 | Cumple parcialmente → Cumple parcialmente | Se conservaron Cost Explorer, Budgets y el informe mensual, y se identificó la falta de etiquetas por ambiente, módulo y centro de costo. Evidencia: SD4 §4.2.3.1; T-11, fila N-12; T-14, cuenta 8.4. |
| RT-03.08 | Cumple → Cumple parcialmente | La estrategia de Savings Plans está descrita, pero la estructura de costos no aparece en la evidencia admitida para esta revisión. Evidencia: SD4 §4.2.3.4. |
| RT-03.09 | Cumple parcialmente → Cumple parcialmente | Se identificó ECS Fargate y Lambda como componentes cubiertos; falta el análisis comparativo de costo frente a instancias permanentes. Evidencia: SD4 §4.2.3.1 y §4.2.3.4. |
| RT-03.14 | Cumple → Cumple | Se sustituyó la descripción genérica por los modelos de equipos y niveles de almacenamiento declarados en T-11. Evidencia: SD4 §4.2.1.2 y §4.2.4.3; T-11, filas Servidor del clúster, Servidores de Concepción, E-01, D-05 y Virtualización. |
| RT-03.15 | Cumple parcialmente → Cumple parcialmente | Se mantuvieron las líneas base CIS y la gestión centralizada de parches; se hizo explícita la falta de una ventana acordada con el CLIENTE. Evidencia: SD4 §4.2.2.5; SD4-Anexos §4-O, ADR-21; T-11, fila F-02. |
| RT-03.19 | Cumple parcialmente → Cumple parcialmente | Se precisaron las funciones de borde acreditadas y la falta de filtrado o agregación previa para reducir el volumen transferido. Evidencia: SD4 §4.1.3.2 y §4.1.4.2; T-11, fila B-02. |
| RT-03.24 | Cumple parcialmente → Cumple parcialmente | Se incorporó el estudio de cobertura exigido por el caso; queda pendiente declarar la priorización general de las transacciones operacionales frente al tráfico administrativo. Evidencia: SD4 §4.2.4.2 y §4.3.1.4; T-11, filas Red inalámbrica industrial y D-06. |
| RT-04.04 | Cumple → Cumple | Se citó la sección que describe explícitamente el registro de requisito, commit, prueba, aprobación y despliegue. Evidencia: SD4 §4.1.9; SD6 §6.2.2. |
| RT-04.13 | Cumple → Cumple parcialmente | El apagado o reducción de ambientes está descrito, pero no el ahorro reflejado en costos. Evidencia: SD4 §4.2.3.4. |
| RT-04.14 | No cumple → Cumple parcialmente | T-19 ya contempla recursos efímeros de Terraform para reproducir incidentes; falta crearlos y destruirlos automáticamente por rama o incidencia. Evidencia: T-19, Ficha 2. |
| RT-05.08 | Cumple → Cumple | Se retiró la referencia errónea a SD5 §5.1.10, que trata otra materia, y se citó la sección de retención, protección y cifrado de datos personales. Evidencia: SD5 §5.2.7; SD5-Anexos §5-E. |
| RT-05.10 | Cumple parcialmente → Cumple parcialmente | Se desplegaron en el componente los plazos del caso y se mantuvo como faltante el catálogo con linaje automatizado. Evidencia: SD4 §4.2.4.5, Tabla 17; SD5 §5.2.6 y §5.2.7; SD5-Anexos §5-D y §5-H. |
| RT-05.15 | Cumple → Cumple | Se retiró la atribución a Amazon S3, que no está acreditada como repositorio de consulta de históricos no migrados. Evidencia: SD5 §5.3.5; SD5-Anexos §5-J, Tabla A.21. |
| RT-05.18 | Cumple → Cumple | Se retiró OAuth 2.1 de la celda porque la propuesta acredita mTLS; mTLS satisface la alternativa expresa de la descripción. Evidencia: SD4 §4.1.3.7 y §4.1.10; SD5 §5.2.4; SD5-Anexos §5-E. |
| RT-05.24 | No cumple → No cumple | Se mantuvo el estado y se añadió al componente la lista concreta de capacidades del portal que faltan. No se encontró una sección con desarrollo acreditable. |
| RT-05.30 | Cumple → Cumple parcialmente | SD13 y T-19 ofrecen el modelo y su documentación, mientras SD5 §5.2.6 excluye expresamente la predicción. La contradicción impide afirmar cumplimiento pleno. Evidencia: SD13 §13.3.2; T-19, Ficha 3; SD5 §5.2.6. |
| RT-06.04 | Cumple parcialmente → Cumple parcialmente | Se precisó que están declarados Cat6A, OM4 y certificación, pero no las normas aplicables a piso, canalización, cableado y etiquetado. Evidencia: T-11, filas Piso técnico y cableado y Distribución horizontal. |
| RT-06.12 | Cumple parcialmente → Cumple parcialmente | UPS N+1 y transferencia red-generador no acreditan la doble acometida. Evidencia: SD4 §4.3.1.4; T-11, filas UPS y Transferencia automática. |
| RT-06.15 | No cumple → No cumple | Se explicitó la declaración faltante sobre contención de pasillo frío o caliente y su efecto energético. No se halló desarrollo acreditable en la propuesta. |
| RT-06.25 | No cumple → No cumple | Se explicitó la falta del procedimiento de acceso de terceros con acompañamiento y registro. No se halló desarrollo acreditable en la propuesta. |
| RT-06.28 | Cumple parcialmente → Cumple parcialmente | La rotación y custodia están descritas; faltan inventario, verificación periódica de legibilidad y registro de movimientos. Evidencia: T-11, fila Medio de respaldo físico rotativo. |
| RT-06.29 | Cumple parcialmente → Cumple parcialmente | La zona y las ocho estaciones están descritas; faltan telefonía e Internet. Evidencia: SD4 §4.3.1.4; T-11, fila Estación de trabajo. |
| RT-06.34 | No cumple → Cumple | La propuesta ofrece el esquema 3-2-1-1-0 con copia inmutable adicional y medio físico cifrado bajo custodia externa, y lo justifica frente al borrado y cifrado malicioso. Evidencia: SD4 §4.2.4.5; T-11, filas D-05, N-11 y Medio de respaldo físico rotativo. |
| RT-07.01 | Cumple → Cumple parcialmente | La modalidad activo-pasivo y su justificación frente al RTO y la complejidad están declaradas; falta comparar costos frente a las alternativas. Evidencia: SD4 §4.3.2.1; SD4-Anexos §4-O. |
| RT-07.04 | Cumple → Cumple parcialmente | Se conservó el objetivo RTO/RPO, pero la propuesta admite que la pérdida del sitio tras la falla simultánea de los tres enlaces podría superar el RPO de 15 minutos. Evidencia: SD4 §4.3.2.4, Tabla 38 y párrafo de riesgo residual; SD8-Anexos §8.E. |
| RT-07.08 | No cumple → Cumple parcialmente | La supervisión de salud y detección están descritas, pero la conmutación espera autorización del CLIENTE; no se acredita activación automática ni sus resguardos. Evidencia: SD4 §4.3.2.5. |

## 2. Componentes sin versión en la propuesta

Se conservaron los nombres declarados sin añadir números de versión o modelos ausentes. Conviene declarar versión, edición o modelo en las ubicaciones siguientes:

| Producto sin versión o modelo declarado | Filas afectadas | Dónde declararlo |
| --- | --- | --- |
| Aurora PostgreSQL y ElastiCache for Redis | RT-02.05, RT-03.02, RT-03.05 y RT-05.05 | SD4 §4.1.10; T-11, filas N-05 y N-07; SD5 §5.1.1. |
| Proxmox VE y Ceph | RT-03.14 | SD4 §4.2.1.2 y §4.2.4.3; T-11, fila Virtualización. |
| Terraform, Ansible y GitLab CI | RT-02.12, RT-03.03, RT-03.15, RT-04.03, RT-04.05, RT-04.06 y RT-04.14 | SD4 §4.1.7 y §4.2.4.2; T-11, filas F-02 e Integración y entrega continuas; T-19, Ficha 2. |
| OpenAS2 BSD | RT-03.02 y RT-05.23 | T-11, fila N-04 — Transporte AS2; SD4 §4.1.6 y §4.1.17. |
| AWS Distro for OpenTelemetry | RT-03.16 | SD4 §4.1.3.8; T-11, fila F-01. |
| Android Enterprise y Zebra DNA | RT-03.18 | SD4 §4.1.7; T-11, fila N-13. |
| AWS Verified Access y CrowdStrike Falcon | RT-03.22 | SD4 §4.2.2.4 y §4.2.5.2; T-11, filas AWS Verified Access y F-03. |

| Servicios AWS nombrados sin versión o edición declarada: ECS Fargate, Application Load Balancer, Amazon SQS FIFO, API Gateway, CodeBuild, Elastic Container Registry, S3 y CloudFront, Secrets Manager, DynamoDB, Glue, Redshift Serverless, Lambda, CloudWatch, Cost Explorer, Budgets, QuickSight, AWS Backup/Vault Lock, S3 Object Lock, KMS, Site-to-Site VPN/Transit Gateway, AWS DMS, Global Tables, Replication Time Control y Systems Manager Automation | RT-02.05–02.10; RT-03.02–03.09, RT-03.12, RT-03.16 y RT-03.21–03.22; RT-04.05–04.06; RT-05.04–05.08, RT-05.18, RT-05.25 y RT-05.27; RT-06.14; RT-07.03, RT-07.05 y RT-07.09–07.11 | SD4 §4.1.2, §4.1.3.5–§4.1.3.8, §4.1.7, §4.1.10, §4.2.3.1, §4.2.4.2–§4.2.4.5, §4.2.5.2 y §4.3.2.3–§4.3.2.5; T-11, filas N-04, N-05, N-07, N-10, N-11 y N-12; SD5 §5.2.6 y §5.2.7. |
| Room, SQLite y swagger-php | RT-03.11 y RT-05.16 | SD4 §4.1.3.6; SD5 §5.2.4; SD4-Anexos §4-P, Tabla A.20. |
| Terminal de Starlink y puntos de acceso Wi-Fi 6E | RT-03.17, RT-03.23, RT-03.24 y RT-06.32 | T-11, filas D-06 — Enlace satelital y Red inalámbrica industrial; SD4 §4.2.5.1, §4.2.4.2 y §4.3.1.4. |
| UPS de 15 kVA, generador de 25 kVA, climatización de precisión, detector por aspiración láser y cámaras IP | RT-06.07, RT-06.08, RT-06.13, RT-06.16 y RT-06.24 | T-11, filas UPS, Generador, Climatización de precisión, Detección de incendio y Videovigilancia; SD4 §4.3.1.4. |
| Sistema FM-200, control biométrico facial/AFIS y estación de trabajo | RT-06.17, RT-06.20, RT-06.23 y RT-06.29 | T-11, filas Extinción, Control de acceso y Estación de trabajo; SD4 §4.3.1.4. |
| Racks R01 y R02, medios transportables cifrados, y extintores portátiles | RT-06.05, RT-06.18, RT-06.26 y RT-06.28 | T-11, filas Gabinetes, Medio de respaldo físico rotativo y Extinción; SD4 §4.3.1.4. |

## 3. Declaraciones faltantes

| ID | Sección existente donde incorporar el contenido | Borrador |
| --- | --- | --- |
| RT-02.10 | SD4 §4.2.4.1.1 y §4.2.6.9 | Las capas de aplicación e integración escalarán automáticamente según umbrales y límites máximos declarados para cada servicio. El costo asociado se incorporará a la estructura de costos: dato a definir por el equipo. |
| RT-02.12 | SD4 §4.1.4.3 y §4.2.4.2, Tabla 15 | La incorporación de una nueva unidad se resolverá por parametrización del sitio, la bodega, las rutas y la cartera, sin rediseñar la arquitectura. Se documentará la plantilla de configuración correspondiente al nuevo centro. |
| RT-03.03 | SD4 §4.1.7 y §4.2.4.2; T-11, fila F-02 | La creación de la cuenta raíz inicial quedará documentada. Todos los demás recursos se provisionarán mediante infraestructura como código versionada, revisable y reproducible, sin creación manual por consola. |
| RT-03.06 | SD4 §4.2.3.1; T-11, fila N-12; T-14, cuenta 8.4 | Todos los recursos llevarán etiquetas obligatorias de ambiente, módulo y centro de costo. AWS Budgets generará alertas y el consumo se reportará mensualmente al CLIENTE, desglosado por esas etiquetas. |
| RT-03.08 | SD4 §4.2.3.4 | La capacidad base se atenderá con Savings Plans y el peak con capacidad efímera. El compromiso y su costo se reflejarán en la estructura de costos de la oferta: monto, dato a definir por el equipo. |
| RT-03.09 | SD4 §4.2.3.4 | Se comparará el costo de ECS Fargate y AWS Lambda para las cargas variables con el de instancias permanentes bajo el perfil propuesto. Los supuestos y montos del análisis quedan como datos a definir por el equipo. |
| RT-03.15 | SD4 §4.2.2.5; T-11, fila F-02 | Ansible mantendrá las líneas base CIS y la gestión centralizada de parches de los nodos on-premise. LafroX acordará con el CLIENTE la ventana de aplicación antes de iniciar la operación. |
| RT-03.19 | SD4 §4.1.3.2 y §4.1.4.2; T-11, fila B-02 | Los gateways filtrarán y agregarán las lecturas que admitan ese tratamiento antes de transferirlas. La regla aplicada quedará documentada para reducir el volumen transmitido y la dependencia del enlace. |
| RT-03.24 | SD4 §4.2.4.2 y §4.3.1.4; T-11, filas Red inalámbrica industrial y D-06 | La política de calidad de servicio priorizará las transacciones operacionales críticas frente al tráfico administrativo en los enlaces de los sitios. |
| RT-04.13 | SD4 §4.2.3.4 | Desarrollo, QA y Preproducción se apagarán o reducirán fuera de su horario de uso. El ahorro correspondiente se cuantificará e incorporará a la estructura de costos; monto, dato a definir por el equipo. |
| RT-04.14 | T-19, Ficha 2 | Los recursos efímeros de QA o Preproducción se crearán y destruirán automáticamente al asociarse a una rama o incidencia. |
| RT-05.10 | SD5 §5.2.6; SD5-Anexos §5-H | El catálogo de datos registrará automáticamente el linaje de cada indicador de negocio hasta su fuente y permitirá seguir su cadena de transformación. |
| RT-05.24 | SD4 §4.1.2; SD5 §5.2.6 | La solución dispondrá de un portal de servicios para desarrolladores con documentación navegable, ambiente de pruebas y credenciales de prueba autoservidas. |
| RT-05.30 | SD5 §5.2.6; SD13 §13.3.2 y Tabla 13.13; T-19, Ficha 3 | Decisión de alcance por definir por el equipo. Si se mantiene la oferta predictiva: «La analítica predictiva de vida útil por historia térmica del lote se implementará como Innovación 3, con el modelo cinético por familia, sus variables, la métrica y el plan de reentrenamiento documentados en 13.3.2 y la Tabla 13.13». Esa declaración debe reemplazar la exclusión vigente en SD5 §5.2.6. |
| RT-06.04 | T-11, filas Piso técnico y cableado y Distribución horizontal | El piso técnico, las canalizaciones, el cableado estructurado y el etiquetado se ejecutarán conforme a la referencia normativa aplicable: dato a definir por el equipo. Cada enlace se entregará con su certificado de medición. |
| RT-06.12 | SD4 §4.3.1.4; T-11, filas UPS y Transferencia automática | La alimentación del recinto contará con doble acometida y la configuración redundante correspondiente, con transferencia automática. La acometida y el esquema aplicable quedan como datos a definir por el equipo. |
| RT-06.15 | SD4 §4.3.1.4; T-11, fila Climatización de precisión | El diseño declarará si aplica contención de pasillo frío o caliente y describirá su efecto en la eficiencia energética. |
| RT-06.25 | SD4 §4.3.1.4; T-11, fila Control de acceso | El acceso de fabricantes, mantenedores y auditores quedará sujeto a acompañamiento obligatorio y registro de ingreso y salida. |
| RT-06.28 | T-11, fila Medio de respaldo físico rotativo | Se mantendrá un inventario de los medios, con verificación periódica de legibilidad y registro auditable de cada movimiento de entrada y salida, además de la rotación declarada. |
| RT-06.29 | SD4 §4.3.1.4; T-11, fila Estación de trabajo | La zona de trabajo contará con las estaciones declaradas, telefonía y conexión a Internet para la operación y administración de la plataforma. |
| RT-07.01 | SD4 §4.3.2.1; SD4-Anexos §4-O | Se mantiene la modalidad activo-pasivo en caliente en us-east-1, seleccionada frente a activo-activo y restauración en frío. La comparación de costos entre alternativas incorporará sus supuestos y montos: datos a definir por el equipo. |
| RT-07.04 | SD4 §4.3.2.4 y §4.3.2.5; SD8-Anexos §8.E | La prueba de recuperación medirá el RTO y el RPO en cada dominio crítico, incluido el escenario de falla simultánea de los tres enlaces y pérdida del sitio. El diseño indicará qué medida garantiza el RPO máximo de 15 minutos o resolverá el compromiso antes de declararlo cumplido. |
| RT-07.08 | SD4 §4.3.2.5 | La conmutación se activará automáticamente cuando se cumpla el criterio de indisponibilidad definido. Se documentarán los umbrales y las salvaguardas que evitan activaciones innecesarias. |

## 4. Incoherencias detectadas en otros documentos

- T-12, fila RF-13.03, mantiene «ADR-01 a ADR-21», mientras SD4 §4.1.11 y SD4-Anexos §4-O, Tabla A.17, declaran el registro hasta ADR-22. La fila B1 RT-02.04 queda corregida en el archivo de salida, pero la fila equivalente RF-13.03 está fuera del rango.
- T-12, fila RNF-20.06, permanece en «Cumple» con RTO ≤ 4 h y RPO ≤ 15 min, aunque RT-07.04 pasa a parcial por el riesgo residual admitido en SD4 §4.3.2.4 y SD8-Anexos §8.E. Los dos estados deben armonizarse.
- T-12, fila RF-13.02, está en «Cumple», pero su componente citado solo declara proveedor y regiones de nube; el requerimiento RF pide ubicar cada componente y justificar la ubicación por criterios. Su alcance es más amplio que RT-03.01, que solo pide proveedor y regiones.
- T-12, filas RNF-13.03 a RNF-13.05, conservan un componente genérico de almacenamiento y redundancia. Sus estados «Cumple» coinciden con RT-03.14, aunque la fila B1 incorpora los modelos exactos declarados en T-11.
- T-12, fila RNF-19.02, coincide en «Cumple parcialmente» con RT-02.10; RNF-13.06 también coincide en estado con RT-03.15. En cambio, RNF-13.09 «Cumple» cubre el estudio de cobertura en cámaras que pide el caso; RT-03.24 tiene alcance mayor porque además exige priorización de operaciones críticas frente a tráfico administrativo, por lo que su estado parcial es consistente.
- T-12, filas RNF-01.02, RNF-08.02 y RNF-09.02, están en «Cumple» para plazos específicos de retención. RT-05.10 conserva estado parcial porque agrega el catálogo deseable con linaje automatizado; la diferencia corresponde a ese alcance adicional.
- SD13 §13.3.2, Tabla 13.13, y T-19, Ficha 3, ofrecen la analítica predictiva del RT-05.30; SD5 §5.2.6 excluye expresamente la predicción. La oferta necesita una declaración única de alcance.
- T-12, filas RT-11.17 y RT-21.01, atribuyen «8 a 10 personas» a un solo puesto. SD4-Anexos §4-W.7 establece 8 personas en total para un NOC y un SOC de una posición cada uno (4 por puesto), y 10 personas en total desde el 26-04-2028 (5 por puesto). Estas filas están fuera de B1 y quedan señaladas sin corrección.
