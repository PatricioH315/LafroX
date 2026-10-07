# Revisión de coherencia del Subdocumento 4 — 2026-10-07

Revisión doble e independiente de los tres entregables compilados el 2026-10-07: `entrega/LAFROX-Subdocumento4.pdf` (148 p.), `entrega/LAFROX-Subdocumento4-Anexos.pdf` (80 p.) y `entrega/LAFROX-Formulario-T-11.pdf` (32 p.), contra las Bases, las Aclaraciones y la revisión del Informe 1.

- **Claude:** lectura completa de los tres PDF, más chequeos automáticos de cifras, códigos, citas a figuras y tablas, indicadores de IA y precios.
- **Codex (ChatGPT):** sesión de solo lectura sobre todas las fuentes `.tex` del alcance (sesión `01a11475-3fea-7db3-aec8-9cd84e1c9607`). Entregó 13 hallazgos y 2 mejoras, sin entradas descartadas.
- **Verificación:** cada hallazgo se comprobó contra el archivo y las Bases antes de clasificarlo. La severidad final es la verificada, no la propuesta por cada revisor.

Resultado: 2 críticos, 5 altos, 7 medios y 7 bajos. Ningún cambio se aplicó al subdocumento en esta revisión.

## Críticos (pueden dejar el subdocumento con puntaje 0)

1. **Declaración de uso de IA** (cuerpo p. 148; anexos pp. 78–80). Dice «Revisión final no realizada», que «la ausencia actual de esa revisión impide tratar este archivo de trabajo como una entrega final conforme», menciona «láminas de Tomás» y «conversión entre Markdown y LaTeX». La tabla del cuerpo solo tiene 4.1 y 4.1.1, sin 4.2, 4.3, Anexo 4-W ni T-11, y el texto habla de «22 anexos» cuando el catálogo tiene 23. Incumple Aclaraciones §7.1(d) y §7.2. *Fuente: Codex y Claude.* Requiere del equipo: quién revisó cada sección y qué verificó.
2. **Figuras de detalle de 4.1.3 recortadas.** Las Figuras 3, 4, 5, 7, 8, 11, 12 y 13 son `figuras/logica/capas_recortes/ARQL-21` a `ARQL-28` «Recorte». La de presentación muestra conexiones cortadas en el borde, texto bajo 9 pt y una caja «App Web» que no existe en la arquitectura. Las Aclaraciones §4 prohíben el recorte como figura de detalle y exigen 9 pt. *Fuente: Codex, verificado por Claude.* Requiere redibujar cada capa.

## Altos

3. **RT-03.14 (Obligatorio): equipos on-premise críticos sin redundancia.** Concepción tiene un servidor único y cada cross-docking un mini-PC E-01 único. Su falla se resuelve por reposición y reconstrucción desde la nube, sin plazo declarado. *Fuente: Codex.* Decisión del equipo: segundo equipo por sitio o justificación explícita con plazo de reposición.
4. **Pérdida de la sala de Talca sin camino para los terminales.** 4.3.2.5 dice que los terminales se conectan por VPN al WMS levantado en la nube, pero los firewalls, el switch de núcleo y las terminaciones de enlace están en el rack R02 de esa misma sala (4.3.1.4). *Fuente: Codex.* Decisión: kit de contingencia fuera de la sala (firewall y switch de reserva ya ofertados, router LTE y Starlink) o redefinir el escenario.
5. **Conmutación regional y mensajes ya aceptados en sa-east-1.** El shipper borra el mensaje local cuando SQS confirma (4.1.3.5). Las colas de us-east-1 se crean vacías, así que lo aceptado y no consumido en la región perdida (reconciliación, solicitudes al ERP y reservas) no tiene recuperación descrita, y la Tabla 37 promete RPO ≤15 min para «mensajes críticos». *Fuente: Codex.* Corrección propuesta: retener el outbox hasta la confirmación del consumidor central y reenviar desde la última marca confirmada al conmutar.
6. **Preproducción y ERP real.** 4.1.9 dice que en Preproducción «se prueban los 186 terminales de bodega… la emisión de guía por el ERP», y el Anexo 4-V ejecuta AL-DTE-01 en Preproducción con ERP, SII y los tres caminos de Talca. Pero 4.2.4 define Preproducción con adaptadores simulados del ERP y sin túnel a las bodegas. *Fuente: Codex y Claude.* Decisión: dónde se ejecuta AL-DTE-01 (ambiente de prueba del ERP o marcha blanca).
7. **Despliegue sin migración de las bases locales.** Los pasos de Preproducción y Producción aplican las migraciones solo a Aurora (paso 4) y luego actualizan `wms_only` en los sitios, sin migrar PostgreSQL de VM-02, VM-C02 y E-01. *Fuente: Codex.* Corrección propuesta: en el paso 7, Ansible aplica las migraciones aditivas a la base local de cada sitio antes de actualizar sus contenedores.

## Medios

8. **Guía nueva sin plazo al perder la sala.** El ERP queda en la sala perdida y la guía nueva espera su restitución por el CLIENTE, pero la Tabla 16 clasifica esa emisión como crítica con resolución de 4 h. *Fuente: Codex (rebajado de crítico: el despacho continúa con la regla de la carga amparada).* Corrección: declarar la excepción en la Tabla 16 y en la Tabla 4.
9. **RPO de objetos críticos «para el 99,99 %».** La Tabla 37 acota el RPO de evidencias y documentos tributarios al 99,99 % de los objetos. *Fuente: Codex (rebajado).* Corrección de redacción: RPO ≤15 min con RTC y recopia por evento.
10. **Drenaje de Talca al 93,59 % de la subida satelital supuesta de 2 Mbps** (Tabla 27). No hay margen para VPN ni retransmisiones. *Fuente: Codex (rebajado).* Corrección: medir en la instalación y declarar el margen.
11. **Servidor del ERP sin EDR.** El F-03 del T-11 cubre siete equipos físicos y no incluye el servidor del ERP trasladado al rack R01. *Fuente: Codex (rebajado).* Corrección: incluirlo o declarar la exclusión con control compensatorio.
12. **EventBridge sin declarar.** Se usa para los hallazgos de GuardDuty (4.2.3.1 y T-11 N-12), pero no aparece en la Tabla 11 ni en la lista de servicios de 4.1.7. *Fuente: Claude.*
13. **Producción explica la figura antes de mostrarla.** La lista de pasos queda en la p. 91 y la Figura 23 en la p. 92. Las Aclaraciones §4 piden explicar después. *Fuente: Claude.*
14. **RabbitMQ 4.3.x como referencia,** con fin de soporte comunitario el 30-11-2026, antes de iniciar el contrato (Anexo 4-P). *Fuente: Claude.*

## Bajos

15. La Tabla 28 no se cita en el texto antes de aparecer (p. 121). *Claude.*
16. La Tabla 7 y el total de «8 equipos» no mencionan el servidor del ERP del CLIENTE en Talca. *Codex (rebajado).*
17. Las Tablas 3 y 20 ocupan tres páginas cada una; las Aclaraciones §5 piden, como referencia, no superar una. *Claude.*
18. Las referencias del T-11 rotulan AWS como s. f.-d, -e y -f sin a, b ni c en ese documento. *Claude.*
19. La séptima instalación del año 3 (caso, cap. 14.1) y el CD de Los Lagos hacia 2030 comparten un único bloque reservado, 10.6.0.0/16 (Tabla 15). *Claude.*
20. Las portadas tienen la línea de firma vacía. *Revisión del 2026-10-06.*
21. 4.1.3.1 dice que el parque Zebra EC55/TC58e/MC9400 está «desplegado en los centros de distribución», pero EC55 y TC58e son de terreno. *Claude.*

## Descartados tras verificar

- Palabras pegadas («BasesTécnicasTransversales», «laVPN»): artefacto de la extracción de texto, en el PDF se ven bien.
- «Formulario T-7» en las portadas: correcto, el T-7 es el formulario que estructura los subdocumentos (Aclaraciones §11).
- «Séptima instalación a tres años»: el caso la proyecta (cap. 14.1, «Instalaciones a cubrir: 6 → 7»).
- «≈ 7.700 km» de us-east-1: está en la Tabla 36 y es correcto (São Paulo–Virginia del Norte ≈ 7.660 km). Retirarlo de la Figura 24 sigue siendo válido porque repite la tabla.

## Verificado sin diferencias

Terminales de bodega 186 → 205 → 233 → 235; preventa 62 → 69 → 77; reparto 96 → 106 → 121; 28 + 3 termógrafos; 21 puntos de frío y 3 gateways; Wi-Fi 65 + 7; mensajes 225.629 / 347.383 e IoT 10.584; TPS 12,30 / 6,94 / 14,66 / 21,99; enlaces y drenajes; carga eléctrica 7.450 W → 8,9 kW, UPS 15 kVA, generador 25 kVA y PUE ≈1,5; UPS de gabinetes; Aurora db.r6g.xlarge; 13 colas y 8 cuentas; RTO 4 h, RPO 15 min y 135 min de conmutación; dotación 15/17/19; bloques de direccionamiento; cronograma del Art. 17; hito H3 del E-25.

## Mejoras no bloqueantes

- IMP-1 (Codex): fechar las fichas ADR. El usuario ya la había postergado el 2026-10-03.
- IMP-2 (Codex): registrar en la aceptación la subida satelital medida.
- IMP-3 (Claude): agregar la columna 3.3 a la Tabla 8, que las Aclaraciones sugieren (mapeo 3.3 → 4.1 → 4.2).
- IMP-4 (Claude): evaluar PostgreSQL 17 en vez de 16, cuyo soporte termina en noviembre de 2028.
