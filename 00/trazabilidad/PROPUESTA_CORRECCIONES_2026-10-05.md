# Propuesta de correcciones — Subdocumento 4 (2026-10-05)

Esta propuesta se aplica solo con aprobación. Las referencias numéricas corresponden a `REVISION_COHERENCIA_2026-10-05c.md`. En cada caso se indica el texto actual (→) y el texto propuesto (⇒).

## A. Traslado del ERP a la sala nueva (decisión del usuario, hallazgo 2)

### Supuesto de cálculo

No se conoce la potencia del servidor del ERP. Se usa como cota la misma de un nodo del clúster: 2U y 1.600 W de placa. Se declara como parámetro de diseño en la Tabla A.28 (4-W), «a confirmar al medir el equipo en el levantamiento», y no como supuesto S-xx, para no tocar el registro del SD3.

| Concepto | Hoy | Con el ERP |
|---|---|---|
| Carga TI base (Tabla 34) | 5.850 W | 7.450 W |
| Carga TI de diseño (+20 %) | 7.020 W ≈ 7,0 kW | 8.940 W ≈ 8,9 kW |
| UPS: kVA ÷ 0,95 y ÷ 0,8 | 7,4 → 9,2 kVA; UPS de 10 kVA | 9,4 → 11,8 kVA; **UPS de 15 kVA** |
| PUE: TI + clima + sala UPS + iluminación + pérdidas | 10,7 kW; 1,5 | 8,9 + 2,7 + 0,4 + 0,6 + 0,78 ≈ 13,4 kW; 1,5 |
| Generador: carga del sitio ÷ 0,8 | 10,8 kW → 13,5 kVA; 20 kVA | 13,5 kW → 16,9 kVA; **25 kVA** (68 %; con 20 kVA quedaría al 84 %, sobre el criterio del 80 %) |
| Climatización de precisión 2 × 10 kW N+1 | cubre 7,0 kW | cubre 8,9 kW (sin cambio de equipos) |
| Rack R01 | 12U (29 %); 5,2 / 6,2 kW | 15U (36 %): ERP 2U en U25–U26 y conmutador de transferencia 1U en U27; 6,8 / 8,2 kW |

### Cambios de texto

1. **4.3.1.4, lista de equipamiento:** se agrega «El servidor del ERP de 2017 del CLIENTE, trasladado desde la sala actual.»
2. **4.3.1.4, párrafo nuevo después de la lista (responde al caso 17.4, punto 12):**
   ⇒ «La sala actual de 25 m² del edificio de oficinas aloja hoy el servidor del ERP de 2017. Ese servidor se traslada sin cambios de software al rack R01 de la sala nueva, durante la Etapa 1, después del hito H3 y antes de la marcha blanca de Talca. El traslado ocurre en una ventana dominical y después de un respaldo completo verificado. Así, el ERP que emite las guías queda con UPS en N+1, generador de 24 horas, climatización redundante y control de acceso. La sala actual queda sin servidores y se libera para otro uso del CLIENTE (PUCV, 2026a, cap. 17, p. 33). Si el servidor tiene una sola fuente, se conecta a los circuitos A y B mediante un conmutador de transferencia de rack (RT-08.04; PUCV, 2026b, cap. 8, p. 18).»
3. **Tabla 34:** fila nueva «Servidor del ERP de 2017 (del CLIENTE, 2U) | 1 | 1.600 W (cota hasta medirlo) | 1.600 W». Base de 7.450 W, margen de 1.490 W y diseño de 8.940 W ≈ 8,9 kW.
4. **Pasos 1–3 del cálculo eléctrico, Tabla 35 y el texto de climatización y de la sala de UPS:** se actualizan con las cifras de la tabla anterior. «sin alterar el UPS de 10 kVA ni el generador de 20 kVA» ⇒ «… de 15 kVA … de 25 kVA».
5. **Texto de racks:** «Cada rack ocupa 12U de 42 (29 %). La carga de R01 es de 5,2 kW base y 6,2 kW de diseño» ⇒ «R01 ocupa 15U de 42 (36 %) y R02, 12U (29 %). La carga de R01 es de 6,8 kW base y 8,2 kW de diseño».
6. **4.2 (vista general, p. 74):** «… seis máquinas virtuales, junto al ERP de 2017 y al respaldo NAS WORM» ⇒ «… seis máquinas virtuales, el servidor del ERP de 2017, trasladado desde la sala actual, y el respaldo NAS WORM».
7. **A-04 (p. 91):** «corre en VM-04 junto al ERP de 2017» ⇒ «corre en VM-04, en la misma sala que el ERP de 2017».
8. **4.3.2.5, después de «Cuando se pierde solo la sala de Talca…»:**
   ⇒ «La pérdida de la sala incluye el servidor del ERP, que es del CLIENTE y no se modifica. Mientras el CLIENTE lo restituye, salen solo las cargas con guía preemitida, cuyo folio conserva la copia del WMS en Aurora. Una guía nueva espera el ERP restituido, y erp-sync y la ACL se reinstalan desde la misma imagen.»
9. **Tabla 4, fila «ERP y emisión DTE»**, columna Efecto: ⇒ «Se retrasa una nueva guía; perder la sala de Talca la detiene hasta restituir el ERP.»
10. **AL-DR-01 (4-M):** se agrega «Con la sala de Talca perdida se comprueba que salen las cargas con guía preemitida y que una carga nueva queda bloqueada hasta restituir el ERP.»
11. **T-11:**
    - UPS de 15 kVA.
    - Generador de 25 kVA (carga de ≈ 13,5 kW).
    - Climatización: «carga térmica de diseño de 8,9 kW».
    - Gabinetes: R01 con ERP en U25–U26 y conmutador en U27, 15U (36 %).
    - Filas nuevas: «Servidor del ERP de 2017 (existente del CLIENTE), traslado y montaje — 1» y «Conmutador de transferencia de rack — 1».
12. **Figura 29 (racks): la debes editar tú.** Agregar el ERP de 2U en U25–U26 y el conmutador de 1U en U27 de R01, y cambiar la ocupación a 15U (36 %). Revisa también si la Fig. 28 muestra el ERP dentro de la sala.

**Opcional (decide tú):** copiar el respaldo del ERP del CLIENTE en D-05 y en S3 Object Lock para acelerar su restitución. No lo incluyo salvo que lo pidas.

## B. Correcciones sin decisión

| # | Dónde | → Actual | ⇒ Propuesto |
|---|---|---|---|
| 3 | 4.1.2 (p. 15) | «… 84 conductores propios y peonetas, unos 160 conductores de transportistas, 120 preparadores nocturnos y 310 personas de centro de distribución (PUCV, 2026a, cap. 14, pp. 24–25)» | «… 84 conductores propios y peonetas, unos 160 conductores de transportistas y 310 personas de centro de distribución (PUCV, 2026a, cap. 2, p. 5); de ellas, 120 preparan pedidos en el turno nocturno de Talca (PUCV, 2026a, cap. 8, p. 14)» |
| 4 | 4.1.1 (p. 12) | «se ejecutan como procesos separables cuando su carga lo exija» | «se ejecutan como procesos separados, con su propio escalado» |
| 5 | 4.2.3.3 (p. 97) | «porque el caso no exige desplegar ni escalar cada módulo por separado y el equipo de TI no operaría su plano de control» | «porque el monolito modular se despliega en pocos perfiles independientes (API, consumidor, trabajos, consolas, AS2 y motor de rutas) que ECS Fargate ya despliega y revierte por separado (RT-02.02; PUCV, 2026b, cap. 2, p. 6); Kubernetes se justifica con decenas de servicios y el equipo de TI de cuatro personas no operaría su plano de control» |
| 6 | 4.2.4.1, Producción (p. 104) | «VM-01 y VM-03 en Talca» | «VM-01, VM-03 y VM-04 en Talca» |
| 7 | 4.2.1.2, viñeta de Talca, y ADR-10 | (sin mención de RT-03.14) | Frase añadida: «Conforme a RT-03.14 y al Art. 16.4, el nivel declarado es Ceph sin RAID por hardware, con réplica de tres copias: tolera la falla de un disco y de un nodo. RAID 10 bajo Ceph se descarta porque duplica la protección y reduce la capacidad útil (PUCV, 2026b, cap. 3, p. 9; PUCV, 2026c, art. 16.4, p. 12).» |
| 8 | 4.2.4.2 (p. 118) | «La evidencia de entrega no se suma, porque el terreno la envía por la red celular sin pasar por el centro de distribución.» | «La evidencia de entrega no se suma al drenaje, porque durante el corte del centro de distribución el terminal la envía por la red celular.» |
| 9 | 4.3.1.1 (p. 151) y 4-R, fila 5.23 | «se acredita en la matriz … (apartado 4.1)» / «Responsabilidad compartida por servicio de nube. — Control ISO 27017/27018 aplicable y dueño.» | Cuerpo: «se acredita en la fila 5.23 del Anexo 4-R (RT-11.06; PUCV, 2026b, cap. 11, p. 23)». 4-R: «Matriz de responsabilidad compartida por servicio (ISO/IEC 27017); datos personales cifrados con claves KMS del CLIENTE y registro de tratamiento (ISO/IEC 27018). — Matriz aprobada por servicio y registro de tratamiento.» |
| 10 | 4.1, 34 citas | p. ej. «(RT-03.10)» | «(RT-03.10; PUCV, 2026b, cap. 3, p. 9)», con el mismo formato que 4.2. Páginas verificadas en el PDF: cap. 2, pp. 6–7; cap. 3, p. 9; cap. 4, pp. 10–11; cap. 5, pp. 12–13; cap. 10, p. 22; cap. 11, pp. 23–24; cap. 12, pp. 25–26; cap. 14, p. 27; cap. 16, p. 29; Art. 16.4, p. 12. También «(PUCV, 2026a, cap. 17)» ⇒ «cap. 17, p. 31». |
| 11 | pp. 49, 70–71 | Páginas casi vacías | Quitar el `\clearpage` de `22_condiciones…tex` (línea 10). Ajustar la posición de la Fig. 14, sin tocar la imagen. |
| 12 | A.11, AL-DTE-01, 4-U y A.26 | Falta la regla de la guía anulada | Añadir «Una guía anulada no se reutiliza y esa salida espera un documento válido.» |
| 13 | N-09 (p. 89) y Tabla 13 | «una cola FIFO por sitio devuelve sus respuestas» / «recibe las respuestas de su sitio» | «una cola FIFO de respuesta para Concepción y para cada cross-docking (Talca las recibe por RabbitMQ local)» / «… fuera de Talca, recibe las respuestas de su sitio» |
| 14 | Tablas A.10 y A.31 (coordinación) | «260.000 ÷ 22,14 × 4; peak × 1,857» | «260.000 ÷ 22,14 × 4; peak: 21.807 líneas × 4» |
| 15 | 4-N, antes de la Tabla A.15 | «La última columna remite a la Tabla 8 del apartado 4.2.2…» | «La última columna resume el criterio de correspondencia; la realización física de cada identificador está en la Tabla 8 del apartado 4.2.2.» |
| 16 | 4.1.3.1 (p. 19) | «Las aplicaciones de los trabajadores (preventa, reparto y bodega) se construyen en Kotlin nativo…» | «…se construyen como una sola aplicación Kotlin nativa con tres perfiles…» |
| 17 | 4.1.18 (p. 67) | «(~160, de 10 empresas)», que se imprime «( 160» | «(≈ 160, de 10 empresas)» |
| 18 | Anexo 4-W | Título seguido de título | Una frase de introducción antes de 4-W.1 |
| 19 | 4.2.2.7 (p. 93) | «validación de frío» | «lectura del termógrafo en la recepción» |
| 21 | Encabezados de 4.1 | Repiten el título del capítulo | «Arquitectura lógica», igual que 4.2 y 4.3 |

Sin cambios, salvo que lo pidas:
- 20: versión de referencia de RabbitMQ. Requiere confirmar la rama vigente.
- 22: `calculo.py`, que es interno y no se entrega.

## C. Declaración de uso de IA (una sola, al final del cuerpo)

Según la aclaración §7.2, va una sola declaración después de las Referencias del cuerpo. Tiene un texto breve y una tabla de seis columnas: Sección | Herramienta | Finalidad | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó). Lleva una fila por cada sección: 4.1, 4.1.1 a 4.1.21, 4.2, 4.2.1 a 4.2.6, 4.3, 4.3.1 y 4.3.2. Además, una fila por cada anexo (4-A a 4-W, o agrupados por bloque) y una por el Formulario T-11. La declaración del PDF de anexos (Tablas A.36 y A.37) se elimina. Falta saber quién revisó cada parte y qué verificó.

## Aplicado (2026-10-05, aprobado por el usuario)

- A completo (puntos 1–11): 4.3.1.4 (lista, párrafo de la sala actual, Tabla 34, UPS de 15 kVA, PUE, generador de 25 kVA, Tabla 35, climatización, racks), 4.2 (vista general y A-04), 4.3.2.5, Tabla 4, AL-DR-01, T-11 (traslado, conmutador, UPS, generador, climatización, gabinetes) y Tabla A.28 (parámetro del ERP). Páginas del caso verificadas: cap. 2, p. 5; cap. 8, p. 14; cap. 17, p. 33.
- B3 dotación nocturna, B5 EKS y B6 VM-04.
- Pendiente del usuario: actualizar la Fig. 29 (ERP en U25–U26, conmutador en U27, R01 de 15U, 36 %) y revisar la Fig. 28. Pendientes de aprobación: B7–B21, opción de respaldo del ERP y declaración de IA.
- Aplicado después (aprobado): B7 RAID (4.2.1.2 y ADR-10), B8 evidencia, B9 ISO 27017/27018 (4.3.1.1 y 4-R, fila 5.23), B10 35 citas a RT con página más Art. 16.4 y cap. 17, p. 31, B11 (`\clearpage` retirado; párrafos de 4.1.5 movidos antes de la Fig. 14), B12–B19 y B21 (encabezado «Arquitectura lógica» en 4.1). Sin cambios: B20 (RabbitMQ) y B22 (calculo.py). Compilación limpia: cuerpo de 170 p., anexos de 98 p. y T-11 de 35 p. en `entrega/`.
- Citas a las Bases (decisión del usuario): las 295 citas «PUCV, 2026a/b/c» pasan al formato de la aclaración §6: «(Bases Técnicas del caso, cap. X, p. Y)», «(Bases Técnicas Transversales, …)» y «(Bases Administrativas, art. X, p. Y)». Cuando el documento ya se nombra en la frase, el paréntesis lleva solo capítulo o artículo y página. Las demás fuentes siguen en APA. Las listas de Referencias conservan las tres entradas de las Bases.
