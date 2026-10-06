# Revisión del Subdocumento 4 — 2026-10-05 (después de incorporar alvaro-md)

Revisión de los PDF compilados el 5 de octubre después de trasladar los cambios de `alvaro-md`: cuerpo de 169 p., anexos de 98 p. y T-11 de 34 p. Claude leyó completos el cuerpo y los anexos, y revisó el T-11 en los puntos modificados. GPT (gpt-6-luna, esfuerzo alto, solo lectura) revisó en paralelo tres frentes: números, formato e indicadores de IA, y requisitos. Los hallazgos marcados (GPT) los propuso Codex y Claude los verificó en las Bases. No se modificó ningún archivo del subdocumento.

## Crítico

| # | Hallazgo | Dónde | Corrección mínima |
|---|---|---|---|
| 1 | Las declaraciones de uso de IA siguen siendo indicadores de IA: «Revisión final no realizada», «láminas de Tomás», «conversión entre Markdown y LaTeX» y «archivo de trabajo… no conforme». La de anexos dice «No realizada» en todas las filas. Los títulos de la Tabla A.37 vienen de nombres de archivo y no llevan tildes («4.1.1 especificaciones tecnologias…», «16 1 del caso»). Se omiten 4.2, 4.3, 4-W y T-11, y el cuerpo dice «22 anexos» cuando son 23. | cuerpo p.169; anexos pp.95–98 | Reescribir ambas tablas con quién revisó y qué verificó. Cubrir todos los apartados y anexos, usar los títulos reales y quitar las frases de estado interno. |

## Alto

| # | Hallazgo | Dónde | Corrección mínima |
|---|---|---|---|
| 2 | La reversión del WMS contradice el 4.1.8 que se trasladó de alvaro-md. El 4.1.8 dice que el WMS de 2013 queda en solo lectura y que la reversión no lo reactiva como escritor. Pero 4.2.4.1.3 dice «sitio piloto… con el WMS de 2013 disponible para la reversión» (paso 3) y «La reversión devuelve el tráfico al escritor de origen» (paso 6). La Tabla 1 dice «feature flag (reversión inmediata)» y 4.2.4.1.2 dice «revertir una ola es apagar su indicador». | cuerpo p.114 (4.2.4.1.3, pasos 1, 3 y 6); p.113; Tabla 1 p.31–32 | Alinear 4.2.4.1.3 con el 4.1.8: revertir significa volver a la entrega previa del nuevo servicio, con el legado solo como lectura y referencia de conciliación. En la Tabla 1, «reversión a la entrega previa». |
| 3 | (GPT) RT-02.02 es obligatorio: «Se rechazará toda arquitectura monolítica que no permita desplegar de forma independiente sus componentes críticos». El texto separa perfiles de ejecución, pero no dice en ninguna parte que los componentes críticos se desplieguen de forma independiente. Al contrario, insiste en «la misma versión del artefacto». | 4.1.3.4 p.25; ADR-01; 4.2.4.1.1 p.110 | Declarar explícitamente qué componentes críticos se despliegan y revierten por separado: perfil WMS por sitio, erp-sync/ACL, shipper, consumidor, motor M4, AS2 y consolas. Citar RT-02.02 y respaldarlo en ADR-01 con su evidencia. |
| 4 | M3 se sigue describiendo como síncrono, pero con la reserva coordinada (CD-05) el pedido se confirma de forma asíncrona, tras el acuse del sitio. 4.1.3.5 dice «M3 coordina de manera síncrona la confirmación de un pedido y solicita a M2 una reserva», mientras 4-G dice «Modo asíncrono con respuesta durable». Además, 4-G remite a un «umbral de confirmación del pedido» que no está definido en el Anexo 4-T. | cuerpo p.27; Fig. 9 p.29; anexos p.16 y Tabla A.24 p.61 | Reescribir la frase de 4.1.3.5: M3 solicita la reserva y queda pendiente hasta el acuse durable. Definir en A.24 un objetivo de confirmación con enlace (p95), o quitar la mención al umbral. |
| 5 | El actor Empresa transportista y su portal contradicen el nuevo modelo de actores. N-02 dice que «los conductores externos entran con una clave de un solo uso» al Portal de Transportistas. La capa 7 dice que «el transportista administra sus conductores y rutas asignadas». 4.1.4.8 dice que «el transportista consulta y asigna viajes desde su portal». Según 4.1.18 y la Tabla A.16, el conductor usa la app de reparto, el portal es del representante y entra en E2, y en E1 la asignación la registra despacho. | cuerpo p.87 (N-02), p.36, p.47 | N-02: lo usan representantes de la empresa desde E2; el conductor entra por la app de reparto. Ajustar las otras dos frases. |

## Medio

| # | Hallazgo | Dónde | Corrección mínima |
|---|---|---|---|
| 6 | La regla térmica graduada (RNG-04) no llegó a todos los textos. Varios todavía dicen que cualquier excursión bloquea: «Una excursión térmica bloquea localmente la salida» (4.1.3.5), «bloquean el despacho en menos de 5 segundos» (4.1.7), B-02, Tabla 21, Fig. 28, Tabla A.12 y ADR-22. | cuerpo p.28, p.53, p.89, p.131, p.153; anexos p.25 y p.48 | Agregar «crítica y sostenida» en esas frases. |
| 7 | La cita de la sala de 25 m² está mal atribuida. La frase «dimensionada para sostener recepción, preparación y despacho» y lo de los 25 m² vienen del RT-06.01 del caso (PUCV, 2026a, cap. 15), pero se citan como «(PUCV, 2026b, p. 14)», sin capítulo. | cuerpo p.151 (4.3.1.4) | Citar el caso (cap. 15 y su página impresa) y dejar las Bases Técnicas Transversales cap. 6, p.14 solo para la tipología. |
| 8 | ADR-17 cita RF-07.09, que trata de anticipos y pagos parciales. El requisito del envío al ERP al cerrar la preparación es RF-05.06. | anexos p.45 | Cambiar por RF-05.06. |
| 9 | (GPT) 4.3.2.2 y ADR-19 dicen que, si el CLIENTE no aprueba us-east-1, la región secundaria «se cambia a otra región AWS aprobada». Contradice la regla de nombrar solo sa-east-1 y us-east-1, y deja indefinido el despliegue del T-11. | cuerpo p.161; anexos p.46 | Decisión del usuario: mantenerlo, o declarar us-east-1 como condición sujeta a aprobación sin abrir otra región. |

## Bajo

| # | Hallazgo | Dónde |
|---|---|---|
| 10 | El 4.2 todavía resume la regla de la guía en su forma anterior («el camión sale solo con la carga amparada… y el ajuste pasa a la ruta siguiente»). No menciona que una guía anulada no se reutiliza y que entonces la salida queda bloqueada. | p.71, p.131; ADR-17; 4-M; 4-U; Tabla A.11 |
| 11 | El paso 1 de 4.2.4.1.3 habla de «el esquema PostgreSQL de partida, que es la línea base de las migraciones Laravel». Choca con el 4.1.8, que dice que el esquema de destino lo define el modelo de datos de la solución. | p.114 |
| 12 | AL-OFF-01 incluye una «reserva local» durante el corte. Con CD-05, durante el aislamiento no se confirma una reserva remota nueva; conviene decir «retención local». | anexos p.31 |
| 13 | En la Tabla A.1 aparece «T12» en vez de «T-12». | anexos p.5 |
| 14 | Hay una nota al pie con la referencia completa de Laravel junto a la cita APA (Laravel, 2026). Se debe dejar solo la cita en el texto. | cuerpo p.52 |
| 15 | Se menciona TOGAF sin referencia en la lista. | cuerpo p.13 |
| 16 | La bitácora del recinto se conserva «coherente con el piso que las Bases fijan», pero sin cita ni página. | cuerpo p.157 |

### Frente formal de GPT (verificado)

| # | Hallazgo | Dónde | Nivel |
|---|---|---|---|
| 17 | La Tabla 20 tiene celdas con dos frases explicativas, por ejemplo en «Servidor de borde de Concepción». La aclaración §5 pide una frase por celda. | `02_c_conexiones.tex` l.139; cuerpo p.129 | Medio |
| 18 | La cita de RT-11.05 dice «(PUCV, 2026b, cap. 11)», sin página. | `21_anexo_4_1_r_controles_seguridad.tex` l.6 | Medio |
| 19 | Se cita «(AWS, s. f.-a…)», pero la referencia está bajo «Amazon Web Services». En la primera cita debe ir «Amazon Web Services [AWS]». | `04_capas_de_la_arquitectura.tex` l.117 | Bajo |

Descartados: la tabla de IA con seis columnas (es el formato que exige la aclaración §7.2) y «peak» como anglicismo (el caso usa ese término 20 veces).

## Solo reportar (figuras)

- Las Figuras 1, 3 y 7 no muestran necesariamente los 15 actores del SD3 ni el portal en E2.
- La Fig. 28 dice que el gateway «bloquea el despacho ante una excursión térmica», sin la graduación.
- Pendientes anteriores: Fig. 24 (ECR de sa-east-1), Fig. 19 (ECR y colas en us-east-1) y Figs. 15 y 28 (un gateway en Talca).

## Verificado coherente

- Los supuestos S-28 y S-30 a S-41 que cita el cuerpo existen en el registro del SD3 (alvaro-md) con el mismo significado.
- La dotación de 84 conductores propios y peonetas y unos 160 externos coincide con la tabla del caso (cap. 14) y con S-23.
- Los RF corregidos coinciden con T-12: RF-03.16, RF-07.05/09, RF-07.02 y RF-09.05/06/07.
- Mensajes 225.629/347.383 en las Tablas 26, A.10 y A.31, en la Dimensión 11 y en el texto. La coordinación suma 46.968/87.228 y el grupo INT-01 a 04 suma 119.678/222.260.
- T-11 N-09 tiene 13 colas, coherente con 4.2.2.4, la Tabla 11 y la Tabla 13.
- Los catálogos de actores coinciden: Tabla A.16, 4.1.3.1 y SD3 3.4.2.1.
- No hay precios. No se citan subdocumentos posteriores al 3.

## Cierre (2026-10-05, compilado sin advertencias)

- **2 Reversión del WMS:** 4.2.4.1.2, 4.2.4.1.3 (pasos 1, 3, 5 y 6) y la Tabla 1 ahora revierten a la entrega previa del nuevo servicio. El WMS de 2013 queda en solo lectura, como referencia de conciliación.
- **3 RT-02.02:** se declara el despliegue y la reversión independientes de cada componente crítico en 4.1.3.4, 4.2.4.1.1 y ADR-01.
- **4 Reserva asíncrona:** se reescribió el 4.1.3.5. La Tabla A.24 agrega «Confirmar reserva con enlace, p95 ≤ 10 s» y 4-G remite a ese objetivo. RT-09.01 del caso solo fija 1,5 s para registrar la línea.
- **5 Portal de Transportistas:** N-02, la capa 7 y 4.1.4.8 ahora dicen que lo usa el representante desde la Etapa 2 y que el conductor usa la app de reparto.
- **6 Regla térmica:** se agregó «crítica y sostenida» en los siete puntos.
- **7 Cita de la sala de 25 m²:** RT-06.01 del caso (PUCV, 2026a, cap. 15, p. 26), página verificada en el escaneo.
- **8 ADR-17:** RF-05.06.
- **10 Guía anulada:** se agregó en 4.2 (introducción y cierre de la Tabla 21) y en ADR-17.
- **11 Esquema de destino:** se corrigió en 4.2.4.1.3.
- **12–15:** «retención local», «T-12», cita «(Laravel, 2026)» en vez de la nota al pie, y se quitó TOGAF.
- **16 Bitácora:** cita a RT-16.10 (PUCV, 2026b, cap. 16, p. 29), página verificada.
- **17 Tabla 20:** celdas de una frase; la explicación pasó al párrafo siguiente.
- **18 RT-11.05:** p. 23, verificada.
- **19 Cita de AWS:** «Amazon Web Services [AWS]» en la primera cita.
- **9:** queda pendiente; se propuso al usuario una solución con una copia en Talca.
- **WMS 2013 (aclaración del usuario):** el WMS se reemplaza por completo. Deja de escribir en cuanto se habilita cada ola y se apaga y retira al cerrar la marcha blanca de Talca. Se aplicó en 4.1.3.5 (Tabla 1), 4.1.8 y 4.2.4.1.2/3.
- **9 Región:** se quitó la rama «si el CLIENTE no aprueba». Las regiones son sa-east-1 y us-east-1, sometidas a aprobación (Art. 23) con su base de licitud; se elige us-east-1 porque ofrece todos los servicios de recuperación. Se aplicó en 4.3.2.2, ADR-19, Tabla 37 y 4.2.4.4.2.
