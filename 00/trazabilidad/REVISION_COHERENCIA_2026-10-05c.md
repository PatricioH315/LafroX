# Revisión de coherencia del Subdocumento 4 — 2026-10-05 (tercera pasada)

Revisión de los PDF vigentes (cuerpo de 169 p., anexos de 98 p., T-11 de 34 p.), compilados después del cierre de `REVISION_SUBDOC4_2026-10-05b.md`. Claude leyó completos los tres documentos y cotejó las cifras con el caso (`Bases/Caso_02_Logistica.md`) y las Bases Transversales. GPT (gpt-6-luna, esfuerzo alto, solo lectura) revisó en paralelo cifras, decisiones técnicas y forma; sus hallazgos se verificaron antes de incluirlos. No se modificó ningún archivo del subdocumento.

## Crítico

| # | Hallazgo | Dónde | Corrección mínima |
|---|---|---|---|
| 1 | Las declaraciones de uso de IA siguen con indicadores de la aclaración 7.1 d: «Revisión final no realizada», «láminas de Tomás», «conversión entre Markdown y LaTeX», «archivo de trabajo… no conforme». La tabla del cuerpo solo cubre 4.1 y 4.1.1. El texto dice «22 anexos», pero son 23. La Tabla A.36 dice «No realizada» en todas las filas y omite 4-W y T-11. Los títulos de la Tabla A.37 son nombres de archivo sin tildes. | cuerpo p. 169; anexos pp. 95–98 | Pendiente de decisión del usuario. Reescribir con quién revisó y qué verificó, una fila por apartado (4.1, 4.2, 4.3 y sus subtítulos), por anexo (4-A a 4-W) y por el T-11. |

## Alto

| # | Hallazgo | Dónde | Corrección mínima |
|---|---|---|---|
| 2 | No se dice qué pasa con la sala de servidores actual ni dónde queda el ERP de 2017. El caso lo pide en 17.4, punto 12: «Qué se hace con la sala de servidores actual». El texto ubica el clúster «junto al ERP de 2017» (p. 74) y la ACL «en VM-04 junto al ERP» (p. 91). Pero la sala nueva no aloja el servidor del ERP: no está en la Tabla 34, ni en la Fig. 29, ni en los racks del T-11. Si el ERP sigue en la sala actual (10 min de UPS, sin generador), la emisión de guías depende de un recinto que no cumple el cap. 6. Ese es el servicio crítico al 99,9 % de la Tabla 16. Además, ante la pérdida de la sala de Talca (4.3.2.5, AL-DR-01) solo se recupera wms_only en Fargate. No se recuperan erp-sync ni la ACL de VM-04, así que ninguna bodega obtendría guías nuevas dentro del RTO de 4 h. | cuerpo pp. 74, 91, 154–157, 166; anexos p. 30; T-11 pp. 20, 31 | Decisión del usuario: (a) trasladar el servidor del ERP a la sala nueva y sumar su carga a la Tabla 34, la Fig. 29 y el T-11, o (b) declarar que el ERP queda en su sala actual, con su riesgo y su mitigación. En ambos casos, responder el punto 12 en 4.3.1.4 y agregar a 4.3.2.5 y AL-DR-01 la recuperación de VM-04 (erp-sync y ACL). |
| 3 | La dotación nocturna se contradice y su fuente está mal citada. 4.1.2 dice «120 preparadores nocturnos y 310 personas de centro de distribución (PUCV, 2026a, cap. 14, pp. 24–25)», es decir, 120 en total. En cambio, 4.2.1, la Tabla 24, 4-W.3 y el T-11 usan «120 preparadores nocturnos de Talca y los 60 de Concepción (S-39)», 180 en total. El 120 viene de la entrevista (cap. 8, p. 14), no del cap. 14. Los 84 conductores y peonetas están en el cap. 2.4, no en el cap. 14. | cuerpo p. 15 frente a pp. 77, 137; anexos pp. 69, 78; T-11 p. 12 | En 4.1.2: «120 preparadores nocturnos en Talca (PUCV, 2026a, cap. 8, p. 14)». Citar el cap. 2.4 con su página para los 84 y los 310. |

## Medio

| # | Hallazgo | Dónde | Corrección mínima |
|---|---|---|---|
| 4 | La separación de procesos se contradice. 4.1.1 dice que «sincronización, mensajería EDI y telemetría se ejecutan como procesos separables cuando su carga lo exija». 4.1.2 dice que «tienen trabajadores y capacidad de escalado independientes desde el inicio (RT-02.02)», igual que la Tabla 13 y ADR-01. | cuerpo p. 12 frente a pp. 14, 112 | En 4.1.1: «se ejecutan como procesos separados». |
| 5 | Para descartar EKS, 4.2.3.3 dice que «el caso no exige desplegar ni escalar cada módulo por separado». Eso choca con RT-02.02, que es obligatorio, y con la afirmación de 4.1.3.4 de que los componentes críticos se despliegan por separado. | cuerpo p. 97 | «porque ECS Fargate y los sitios ya despliegan por separado los componentes críticos (RT-02.02), y EKS agregaría un plano de control que el equipo de TI no operaría». |
| 6 | El despliegue en Producción no considera VM-04. El paso 7 actualiza «VM-01 y VM-03 en Talca, VM-C01 y VM-C04 en Concepción y E-01». Sin embargo, erp-sync es un perfil de la misma imagen y corre en VM-04 (Tabla 13; T-11, fila A-01: «VM-01, VM-C01, E-01, VM-03, VM-C04 y VM-04»). | cuerpo p. 104 | Agregar VM-04. Revisar si la Fig. 23 tiene la misma omisión (solo reportar). |
| 7 | RT-03.14 (obligatorio) pide declarar «el nivel RAID escogido» y que el almacenamiento tolere la falla de un disco. Para Talca, el texto dice «Ceph sin RAID» y no lo relaciona con RT-03.14. La tolerancia a la falla de un disco aparece solo en la Tabla 20. (GPT) | cuerpo pp. 78, 160; ADR-10; T-11 p. 3 | Una frase en 4.2.1.2 o ADR-10: «RT-03.14: protección por réplica Ceph size=3 sin RAID por hardware; tolera la falla de un disco y de un nodo; RAID 10 descartado por capacidad». |
| 8 | La evidencia de entrega pasa o no pasa por el enlace del CD según la sección. 4.2.4.2 dice que «La evidencia de entrega no se suma, porque el terreno la envía por la red celular sin pasar por el centro de distribución». En cambio, 4.2.6.6/7 y 4-W.6 hacen sincronizar en el CD a los 64 camiones que regresan («en los centros de distribución la sincronización ocurre por Wi-Fi»), y el peor caso de Talca (3,29 + 1,87 Mbps) incluye el retorno de la flota. | cuerpo p. 118 frente a pp. 140–141; anexos pp. 83, 85 | En 4.2.4.2: «no se suma al drenaje, porque durante el corte del CD el terminal la envía por la red celular». |
| 9 | Se menciona ISO/IEC 27017/27018 sin evidencia. 4.3.1.1 dice que su cumplimiento «se acredita en la matriz de controles… (apartado 4.1)», pero la matriz está en el Anexo 4-R y solo trae «Control ISO 27017/27018 aplicable y dueño». La aclaración §3 asigna puntaje cero a la sola mención de un estándar. | cuerpo p. 151; anexos p. 56 | Remitir al Anexo 4-R. En la fila 5.23, nombrar uno o dos controles concretos (por ejemplo, responsabilidad compartida y cifrado con KMS del CLIENTE) con su evidencia, o quitar la mención. |
| 10 | El apartado 4.1 cita 34 veces un RT sin documento ni página, por ejemplo «(RT-03.10)», «(RT-02.02)», «(RT-11.11–11.12)» y «Art. 16.4». En 4.2 y 4.3 todas las citas llevan «(PUCV, 2026b, cap. X, p. Y)». Además, «(PUCV, 2026a, cap. 17)» no tiene página (es la p. 31) y los anexos tienen dos citas genéricas «(PUCV, 2026b)». | cuerpo pp. 12–59 y p. 48; anexos pp. 6, 38 | Agregar documento y página con el mismo formato de 4.2 (aclaración §6). (GPT, en parte) |
| 11 | Hay páginas casi vacías. La p. 49 contiene solo «retirarse.», porque la Fig. 14 pasa a la página siguiente. Las pp. 70 y 71 tienen tres líneas cada una por un `\clearpage` sobrante en la línea 10 de `22_condiciones_y_supuestos_de_diseno.tex`. El Informe 1 ya fue penalizado por páginas semivacías. | cuerpo pp. 49, 70, 71 | Quitar el `\clearpage`. En la p. 49, ajustar el párrafo previo a la Fig. 14 o la posición del flotante. |

## Bajo

| # | Hallazgo | Dónde |
|---|---|---|
| 12 | La regla «una guía anulada no se reutiliza y la salida queda bloqueada» no llegó a la Tabla A.11 (fila Nueva guía), a AL-DTE-01 en 4-M, a 4-U ni a la Tabla A.26. | anexos pp. 23, 29–30, 63, 65 |
| 13 | Colas de respuesta: N-09 en 4.2.2.4 dice «una cola FIFO por sitio devuelve sus respuestas» y la Tabla 13 dice que cada shipper «recibe las respuestas de su sitio». El T-11 cuenta 4, porque Talca recibe por RabbitMQ local. | cuerpo pp. 89, 112; T-11 p. 26 |
| 14 | La derivación del peak de coordinación dice «46.968… peak × 1,857», que da 87.220. El valor 87.228 sale de redondear primero las líneas (21.807 × 4). Lo mismo ocurre con INT-06 (3.761 frente a 3.762). | cuerpo Tabla 26; anexos Tablas A.10 y A.31 |
| 15 | La Tabla A.15 dice que su última columna «remite a la Tabla 8 del apartado 4.2.2», pero contiene criterios («Entrada pública única», «Validación sin WAN»). | anexos p. 33 |
| 16 | ADR-07 y el T-11 declaran «1 artefacto para 3 perfiles», mientras el cuerpo, la Fig. 18 y el T-11 (C-01, C-02) hablan de «app de preventa» y «app de reparto». Conviene una frase que diga que son perfiles de una misma aplicación Kotlin. | cuerpo pp. 19, 85; anexos p. 41; T-11 p. 30 |
| 17 | «(~160, de 10 empresas)» se imprime «( 160», porque `~` es un espacio duro en LaTeX. Usar `$\approx$`. | cuerpo p. 67 |
| 18 | El título del Anexo 4-W va seguido directamente del título de 4-W.1 (aclaración §3). | anexos p. 68 |
| 19 | En la Tabla 10, el cross-docking «mantiene… validación de frío», pero no tiene sensores ni gateway. Precisar que es la lectura del termógrafo en la recepción. | cuerpo p. 93 |
| 20 | La versión de referencia de RabbitMQ (4.3.x) pierde el soporte comunitario el 30-11-2026, antes de la Etapa 1. Conviene tomar como referencia la rama vigente. | anexos p. 49 |
| 21 | El encabezado de las páginas de 4.1 repite el título del capítulo. Las de 4.2 y 4.3 dicen «Arquitectura física» y «Data center». | cuerpo pp. 12–71 |
| 22 | Uso interno (no se entrega): `calculo.py` y `resultados.md` siguen con 178.661/260.155 mensajes, sin la coordinación de reserva (225.629/347.383 en el documento). (GPT) | `Dimensionamiento/` |

Descartado: «SII, s. f.-c sin cita» (GPT). Sí se cita en el Anexo 4-U.

## Solo reportar (figuras, no se editan)

- Figs. 15 y 28: dibujan un gateway IoT en Talca, pero el texto, la Tabla 7, ADR-22 y el T-11 indican dos.
- Fig. 19: no muestra en us-east-1 el ECR replicado ni las colas y temas vacíos que describen 4.2.4.1.1 y la Tabla 39.
- Fig. 24: la réplica recibe las entregas «desde el ECR de sa-east-1». El texto dice que usa el ECR replicado.
- Fig. 23: verificar si el paso 7 incluye VM-04 (hallazgo 6).
- Figs. 1, 3 y 7: no se cotejaron con los 15 actores ni con el portal en E2.

## Verificado coherente

- Inventario: Tabla 7, reservas del 10 % (69/106/205/72/7/4/24/31/4), crecimiento a tres años (+15/+8/+28), T-11 y 4-W.3.
- Emplazamiento: 36 componentes (13/11/12) y Tabla 9 contados componente por componente.
- Mensajes: total normal de 225.629, recalculado.
- TPS: 12,30/14,66/3,76/6,94, portal 9,63, prueba de 21,99 y dimensiones 4–6.
- Almacenamiento y migración: 50,75, 87,72, 0,56 + 3,20 y 32,11 GB.
- Enlaces y drenaje: 1,68/1,09/0,27 GB, 1,87/1,21/0,30 Mbps y Tabla 27.
- Ventana dominical: 203/101 equipos y 12 domingos.
- Energía: Tabla 34 (5.850/7.020 W), UPS de 10 kVA, PUE ≈1,5, generador de 20 kVA, racks de 12U y UPS de los gabinetes (Tabla A.34).
- Capacidad de Talca y Concepción: 26 vCPU/59–61 GB, 1,92 TB útiles y utilizaciones.
- Mesa y NOC/SOC: 15/17/19 personas.
- RTO, RPO y conmutación: 135 min, autorizador en 30 min, 99,95 % frente a 99,9 %.
- Identidad: TTL de 24 h, manifiesto de 26 h, credenciales de 8/14 h.
- Regla térmica graduada, guía preemitida, regiones (solo sa-east-1 y us-east-1) y exclusión de geolocalización.
- Referencias del cuerpo y de los anexos: citas y lista se corresponden.
- No hay precios de la oferta. Las cifras en pesos son datos del caso.
- No se citan subdocumentos posteriores al 3.
- No hay tablas del cuerpo con más de 5 columnas.
