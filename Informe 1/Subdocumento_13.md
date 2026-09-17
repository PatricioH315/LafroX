# Subdoc 13 · Innovaciones de la Propuesta (Informe 1\)

## Innovación 1 · Tipo (1) Producto/Servicio — Servicio de trazabilidad sanitaria GS1 (EPCIS) end-to-end con respuesta a retiro \< 2 horas

* **Idea:** Vender a Puelche una garantía verificable y contratable: ante un retiro sanitario, la lista de clientes por lote se entrega con evidencia en menos de 2 horas (Criterio de Aceptación N.° 1). Hoy el retiro del lote 24-0217 tardó 9 días y costó $31 millones, porque el 41 % de las recepciones del producto suspendido se registró sin lote.  
* **Tecnología que la sustenta:** Motor de trazabilidad por eventos bajo el estándar **GS1 EPCIS 1.2** (cuádruple Qué GTIN+lote / Dónde GLN / Cuándo / Por qué), sobre repositorio relacional con API REST consultable por lote, capturando eventos en recepción, almacenamiento, picking, carga y entrega/POD con retención mínima de 5 años (RNF-09.02).  
* **Resultado esperado:** Respuesta a retiro de 9 días a **menos de 2 horas** con evidencia sobre el 100 % del lote (R18-01) y cobertura de lote en recepción del 41 % al 100 % hacia adelante (R18-02).  
* **Investigación adicional:** Sí — profundizar la integración de eventos EPCIS con los sistemas legados (ERP y WMS) y con la cadena del DTE, y validar las recomendaciones de codificación GS1 Chile para la flota y los puntos de entrega.

---

## Innovación 2 · Tipo (2) Proceso — Preparación nocturna por olas a −22 °C con guantes y secuenciación térmica

* **Idea:** Rediseñar el proceso de preparación nocturna (22:00–06:00) del CD: de picking por pedido con hoja impresa a **picking por olas de ruta** ejecutado sobre terminales rugged dentro de la cámara a −22 °C, con ordenación FEFO por vencimiento, secuencia térmica de recolección (seco → refrigerado → congelado) y carga dirigida inversa a la ruta. Hoy la diferencia del conteo cíclico es 2,3 %, la merma por vencimiento 1,7 % y el rechazo del food service por cadena de frío llegó a $21 millones.  
* **Tecnología que la sustenta:** Terminales rugged operables a **−22 °C con guantes** (RNF-05.02) con confirmación ≤ 1 s por línea (RNF-05.01); misiones de ola precargadas al inicio del turno; validación GS1; opera sobre la programación offline de la innovación 3, sin costo de telecomunicaciones en cámara.  
* **Resultado esperado:** Sin papel en cámara, precisión de picking ≥ 99,5 % (diferencia de conteo de 2,3 % a ≤ 0,5 %), merma ≤ 1 % en régimen y la carga lista dentro de la ventana 05:30–07:00, evitando los rechazos por frío ($21 millones).  
* **Investigación adicional:** Sí — estudio de mercado y certificación de terminales rugged para uso con guantes a −22 °C (RNF-05.02) y validación del algoritmo de secuenciación térmica y FEFO con la volumetría real del peak de septiembre.

---

## Innovación 3 · Tipo (3) Tecnológica/Arquitectura — Arquitectura offline-first orientada a eventos para operación sin señal (14 h de terreno · 24 h en CD)

* **Idea:** Que preventa (62 preventistas), reparto (\~200 conductores) y bodega (24 h) operen **sin depender de señal**: offline de primera clase con buffer local cifrado, dataloggers de memoria interna \+ BLE/NFC (sin SIM) y reconciliación determinista al reconectar. Hoy la operación se detiene con cortes de fibra (\~4/año) y tramos de \~2 h sin señal nominal, exigiendo hasta un turno completo de 14 h (RT-03.10) y 24 h en CD (RNF-02.01).  
* **Tecnología que la sustenta:** Terminales móviles con buffer local cifrado (RNF-06.01), identificador único y descarte de duplicados (RF-03.16, RT-02.06/02.07); dataloggers de memoria interna \+ BLE/NFC que vuelcan la curva térmica en segundos; broker de colas de eventos con reintento y **reconciliación determinista** (RT-03.12/03.13) y sincronización CD ≤ 2 h al reconectar (RNF-02.01).  
* **Resultado esperado:** **Cero pedidos perdidos ni duplicados por falta de señal** (R18-06), autonomía verificada 24 h CD / 14 h terreno (RNF-20.04) y curva térmica completa.  
* **Investigación adicional:** Sí — diseño y pruebas de estrés (1,5× peak) de la reconciliación determinista, y pruebas de resiliencia por corte de 24 h en el CD (RNF-19.04).

---

## Innovación 4 · Tipo (4) Modelo de negocio/contratación — Servicio gestionado de TI con pago por uso para un equipo interno de 4 personas

* **Idea:** Entregar y contratar la plataforma de modo que **toda función que exigiría un administrador dedicado se ofrezca como servicio costeado por uso**, de manera que Puelche no dimensiona un área TI mayor a su equipo actual de 4 personas en una operación 24×7 (bodega nocturna, despacho 05:30–07:00).  
* **Tecnología que la sustenta:** Servicio gestionado con **pago por uso**: NOC 24×7×365 (RNF-21.01), mesa de ayuda dimensionada con **Erlang C** (RNF-21.05), SRE y administración de nube (secretos RT-21.4, observabilidad única), gestión centralizada de \~270 dispositivos (RT-03.18) y cómputo elástico facturado por consumo, con contratos de estándares abiertos.  
* **Resultado esperado:** 100 % de las funciones de administración dedicada como servicio costeado (supuesto Equipo TI); 80 % de llamadas atendidas en 20 s y 70 % al primer contacto (RNF-21.03); costo de operación mensual y variable alineado al volumen real (peak de septiembre), evitando ≥ 2 roles dedicados durante la Operación.  
* **Investigación adicional:** Sí — dimensionamiento Erlang C con la volumetría real del canal y de la mesa de ayuda, y definición contractual del servicio gestionado (SLA, reversibilidad, tarifas por uso).

---

## Innovación 5 · Tipo (5) UX/Sostenibilidad/Impacto social — Inclusión digital del canal tradicional: autoatención y UX de terreno en 14.200 puntos

* **Idea:** Que el canal tradicional —parte importante personas naturales sin internet ni correo— consiga autoatención **sin descargar ninguna app** (Restricción 5), y que la UX de terreno sirva al trabajador de la calle que opera a una mano, bajo sol/lluvia y con guantes, incluidos los conductores de terceros. Hoy 14.200 puntos no tienen autoatención y un competidor entró a Talca con una app.  
* **Tecnología que la sustenta:** Chatbot transaccional sobre **WhatsApp Business API** (botones guiados, plantillas aprobadas: ETA de despacho, saldo, stock y reposición) \+ portal web complementario (RT-16.30); UX de terminales adaptada: operación a una mano, legibilidad bajo sol, botones grandes, sin gestos complejos (RNF-05.03); conductores de terceros identificados por OTP/PIN sin correo (RF-06.08).  
* **Resultado esperado:** ≥ 60 % de los puntos del canal tradicional con ≥ 1 consulta autónoma mensual al mes 24 de Operación, descongestión de la mesa telefónica y retención del canal frente al competidor; sin inversión de app para el cliente (setup USD 4.000–6.000 \+ \~USD 400–700/mes).  
* **Investigación adicional:** Sí — validación de tarifas y política de plantillas de WhatsApp 


Anexo · Candidatas consideradas y descartadas como innovación (Art. 28°)

En aplicación del criterio del pliego (no procede como innovación lo que es funcionalidad ya exigida o estándar de industria sin diseño de incorporación propio):

* **Motor de optimización de rutas VRP-TW/ALNS** — la ruta automática en menos de 20 minutos es criterio de aceptación exigido (RF-04.01). Se entrega como funcionalidad base; su know-how se protege con el registro de ajustes del planificador.  
* **Motor de costeo del costo de servir (ABC)** — es requisito del catálogo (RF-11.02, decisión N.° 7); es analítica base que se beneficia de los eventos de la innovación 3\.  
* **Registro continuo de temperatura en cámaras y vehículos** — es exigencia de periféricos (RT-17.06 / RF-09.05); lo innovador es el mecanismo offline de captura, cubierto por la innovación 3\.  
* **Portal web clásico de clientes** — estándar de industria sin diseño de incorporación diferenciado; se integra como soporte de la innovación 5\.

## Fuentes de referencia

* de Koster, R., Le-Duc, T., & Roodbergen, K. J. (2007). Design and control of warehouse order picking: A literature review. *European Journal of Operational Research, 182*(2), 481–501.  
* GS1 AISBL. (2016). *EPCIS and Core Business Vocabulary* (v1.2, ratificado 2017). GS1.  
* Helland, P. (2007). Life beyond distributed transactions: An apostate's opinion. En *Proceedings of CIDR '07*.  
* Kleppmann, M. (2017). *Designing data-intensive applications*. O'Reilly Media.  
* Ministerio de Salud de Chile. (1996). *Reglamento Sanitario de los Alimentos* (D.S. N.° 977/96).  
* Vogels, W. (2009). Eventually consistent. *Communications of the ACM, 52*(1), 40–44.

