# LafroX — Revisión final del borrador SD10

Fecha: 17 de noviembre de 2026. Versión: 0.1. Revisión automática y visual asistida por Codex; no acredita revisión humana ni aceptación del CLIENTE.

## Contenido y procedencia

- La rama hija parte de SD10 LaTeX en 3faaec7ac6ab05a2bb7c0b7187584ad59b0b81e4 y sustituye la plantilla por el capítulo 10.1/10.2.
- Se revisaron fuentes LaTeX y PDF correspondientes de SD1–SD9 y SD13, las plantillas de SD10–SD12, E2 en LaTeX, bases y aclaraciones. Las versiones y huellas se conservan en trazabilidad/fuentes_sd10.json.
- Se documentaron 28 decisiones y diez brechas. N/A identifica el dato específico sin respaldo; no representa cero ni una aprobación.
- El cuerpo desarrolla niveles de atención, horarios, capacidad, conocimiento, observabilidad, seguridad, indicadores, recuperación y coordinación de soporte. Los anexos A–E contienen cálculos, indicadores, guías, brechas y matriz de requisitos.
- Se conservan la clase, portada, logotipos y formato corporativos. El ajuste del título largo se aplica sólo a la portada del SD10 desde main.tex.
- Se excluyen importes económicos nuevos, firmas, contactos operativos inventados, contratos no acreditados y resultados reales de ensayos no realizados. El modelo financiero y las otras ramas no fueron modificados.

## Verificación cuantitativa

El script comprobar_calculos.py reproduce diez controles con las entradas sin redondear de SD4/T-15:

- Erlang C: 90,6 % y 84,2 % de respuesta en veinte segundos con siete y dos agentes. Los límites enteros 2.283 y 2.391 contactos se contrastan con el entero siguiente.
- Sensibilidad de 6.000 contactos: mínimo de quince/cuatro agentes bajo las mismas hipótesis. No se añade contratación ni se presenta como demanda observada.
- Recuperación regional: 135 minutos secuenciales, con 105 minutos de margen respecto de cuatro horas.
- Horario no productivo: 60/168 horas semanales, reducción teórica de 64,3 %. El ahorro monetario requiere valorización por recurso; no equivale a reducir toda la factura por ese porcentaje.
- Capacidad mensual: 962/1.570 horas-posición; cotas agregadas de ocho/trece plazas a 128 HH efectivas. SOC continuo: seis plazas en meses de 31 días.
- Deuda técnica: 2.304 HH sobre 109.791,32 HH dan 2,0985 %. Se conserva abierta la conciliación de alcance con E2.

## Contraste con PDF de fuente

Se comprobó la presencia de cifras y pasajes relevantes en los PDF del mismo commit:

| Fuente | Páginas del archivo PDF | Evidencia contrastada |
|---|---|---|
| SD4, cuerpo | 71, 110, 128, 151 y 181–182 | Horarios, reducción de cómputo y recuperación |
| SD4, anexos | 99, 103–105 y 112–117 | Erlang, días equivalentes y límites de contactos |
| T-14 | 105, 107 y 108 | Responsable, deuda técnica y bolsa evolutiva |
| T-15 | 12, 13 y 75 | HH por calendario, soporte puente y calibración Erlang A |
| SD13, cuerpo | 17–23 | INN-02 y captura seudonimizada |

Las páginas son posiciones de archivo. El cotejo de texto normaliza espacios tipográficos; no acredita que el compromiso ya se haya ejecutado.

## Compilación y presentación

Se compilan por separado main.tex y anexos.tex mediante LuaLaTeX/latexmk, hasta estabilizar índices y referencias. Se comprueban errores, referencias sin resolver, glifos ausentes y desbordes horizontales. Las advertencias de cajas poco llenas en celdas numéricas se revisan visualmente.

Se renderizan todas las páginas con Poppler y se inspeccionan portada, índices, folios, texto, dos diagramas y once tablas. Se ajustan el título largo de portada, la fuente de la tabla de cobertura, los cortes de tablas de anexos y el bloque final de declaración de IA. Los PDF se identifican como borradores y los espacios de firma permanecen vacíos.

## Límites de cierre

No se marca cumplimiento ejecutado. Permanecen B-01 a B-10, detalladas en el Anexo 10.D y en la trazabilidad: sitios, habilitación de canales/guardias, OLAs y contratos, retención, congelamientos, relojes SLA, ERP, calibración/cuadrante, planes de SD11/12 y conciliación técnica-económica. Su cierre necesita evidencia o decisión de quien corresponda; no se sustituye por una suposición.
