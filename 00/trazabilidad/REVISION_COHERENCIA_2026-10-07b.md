# Revisión de coherencia total del Subdocumento 4 — 2026-10-07 (segunda)

Alcance: cuerpo (4.1, 4.2, 4.3), Anexos 4-A a 4-W, Formulario T-11, `calculo.py` y todas las figuras. Contrastado con las decisiones D1–D41, la ficha de ARQL-01 (componentes retirados) y las Bases.

- **Claude:** lectura completa de las fuentes `.tex`, revisión visual de todas las figuras y chequeos automáticos (componentes retirados, indicadores de IA, páginas de citas, cifras contra `calculo.py`).
- **ChatGPT (gpt-6-sol, medio, solo lectura):** tres frentes en paralelo (A: 4.1 y anexos lógicos; B: 4.2, 4.3, 4-W y T-11; C: forma, citas y componentes retirados). 11 hallazgos; 9 válidos tras verificar contra archivo y Bases.

## Corregido en esta revisión (compilado sin errores: 149 / 81 / 34 p.)

| # | Hallazgo | Fuente | Corrección |
|---|---|---|---|
| 1 | Terminales de cross-docking: 4.2.6 y 4-W decían 7; el cálculo, el T-11 e INT-13 usan 9 (6 + 1 por plataforma, 207 en total) | Claude | 7 → 9 en 4.2.6 y 4-W; «183 restantes» → 185 en 4.2.1 |
| 2 | Anexo 4-D atribuía la autoatención a M11 | Claude y ChatGPT | «autoatención desde el Portal de Clientes» |
| 3 | Anexo 4-M (AL-DR-01): «Concepción se reconstruye desde eventos centrales» ante la falla del servidor, contra D41 | ChatGPT | El servidor en espera toma el control; solo la pérdida de ambos obliga a reconstruir |
| 4 | T-11 N-09: «13 colas» sin decir que cada una tiene cola de fallidos | ChatGPT | «13 colas, cada una con su cola de fallidos» |
| 5 | 4.2.2 atribuía al Art. 21 «impedir exponer los sitios» y «la DMZ»; eso no está en el Art. 21 | ChatGPT (verificado en las Bases) | RT-03.22 (BTT cap. 3, p. 10) y Art. 21.2 (capa de borde, p. 15) |
| 6 | 4.2.4: el Art. 78.3 fija un MTTR mensual, no un tope por reversión | ChatGPT | Redacción ajustada |
| 7 | 4.2.4: RT-02.02 citado en p. 7; está en p. 6 | Claude | p. 6 |
| 8 | `calculo.py` no incluía la coordinación de reservas (daba 183.284 / 266.105) | ChatGPT | Fila agregada; ahora 230.252 / 353.333, igual que el documento |
| 9 | 4.1.4 reproducía dos montos históricos del caso sin función técnica | Revisión posterior | Se retiraron los importes de M9 y M7; se conservaron el incidente sanitario y la necesidad de investigar los descuadres. El Art. 50.2 prohíbe cifras que permitan inferir la oferta económica, no todo monto histórico del caso. |

## Pendiente: decisión del equipo

1. **Figuras recortadas de 4.1.3 (Figs. 3–5, 7, 8, 11–13; ARQL-21 a 28). Crítico.** Además de ser recortes, contradicen el texto y muestran componentes retirados:
   - Capa 5: EventBridge («bus de eventos») y su logo.
   - Capa 8: AMP, X-Ray «30 días» y Grafana OSS (ADR-14 fija solo CloudWatch).
   - Capa 7: caché de Keycloak con TTL de 8 h (el texto dice 24 h) y códigos internos «D13» y «D15».
   - Capa 4: «Sin Control de Jornada (D1)» y logo de Transbank.
   - Capa 1: caja «App Web» inexistente y solo 13 de los 15 actores.
   - Capa 6: BD_RUTAS en el sitio (ARQL-01 la retiró) y nube rotulada «Analítica + DR + Orquestación».
   Opciones: (a) retirar los ocho recortes y dejar el texto de cada capa apoyado en la Figura 1 (ARQL-01, ya corregida a 9 pt); (b) redibujar cada capa desde ARQL-01.
2. **Figuras de secuencia ARQL-15, 16 y 17** (del usuario): texto sin tildes («publica», «credito», «excepcion», «auditoria», «recepcion»…). ARQL-17 dice «120 terminales HHT» (el diseño usa 186 en el turno nocturno) y omite M8.
3. **ARQL-01** rotula «M12 Flota»; el texto y el Subdocumento 3 dicen «M12 Telemetría».
4. **`calculo.py`, dotación peak:** `resultados.md` dice 15/17 personas; 4.2.6 y 4-W dicen 15/17 normal y 17/19 en septiembre y diciembre. Solo afecta al archivo interno.
5. Siguen abiertos: declaración de IA (1), sala de Talca con la red dentro (4), AL-DTE-01 en Preproducción (6), tablas de tres páginas (17), firma de portadas (20).

## Bajo, no aplicado

- Varias citas narrativas usan «del Artículo 16.2 de las Bases Administrativas (art. 16.2, p. 11)»; es válido en APA narrativo.
- Anexo 4-B usa estilo telegráfico («Comité Arquitectura», «Traspaso equipo 4 personas»).
- Tabla de ventanas de 4.2.4: «22:00–06:00, sí» se superpone con «05:30–07:00, no».

## Verificado sin diferencias

Componentes retirados ausentes del texto, del T-11 y de las figuras ARQL-01, ARQL-19, Nube, General, Talca, Concepción y cross-docking (EventBridge, X-Ray, Grafana, AMP, Transfer Family, Redis/Horizon en sitios, Lambda fuera del autorizador). Sin regiones adicionales ni subdocumentos posteriores. Mensajes 230.252 / 353.333 y sus subtotales por grupo; 13 colas; 433 equipos MDM; EDR 11 + 14 + 192 = 217; terminales 207 → 235; Wi-Fi 65 + 7; racks 15U / 12U con la posición de cada equipo; carga TI 7.450 W → 8,9 kW, UPS 15 kVA, generador 25 kVA, PUE 1,5; UPS de borde 3,42 / 0,88 / 0,42 kVA; Aurora db.r6g.2xlarge y 111,70 sol/s; tareas Fargate 2 / 4 / 7 bajo techo 8; secuencia de 135 min; 36 componentes 13 + 11 + 12 y su tabla de criterios; D41 coherente en texto y figuras.
