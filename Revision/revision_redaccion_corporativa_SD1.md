# LafroX — Revisión de la presentación corporativa del SD1

## Alcance y resultado — 12 de octubre de 2026

Petición explícita: revisar y corregir desde la introducción hasta §1.3.2, incluidas las preguntas sobre empresa/proyecto, contactos, agentes, Erlang C, CISO, tecnologías y sedes; alinear Markdown con LaTeX. Se comprobaron `rama-md` y el checkout externo `C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX-sd1-latex`, rama `LafroX-Subdoc1-LateX`. Los permisos escalados para edición y compilación externa fueron aprobados. No hubo cambio de rama, commit ni push.

El tramo corregido distingue antecedentes corporativos, capacidad física y aplicación de políticas a este proyecto. Se preservaron las siete tablas y su numeración, los 124 especialistas, los 112 equipos y los antecedentes previamente autorizados. §1.3.3–§1.6 y el T-6 no se modificaron. La bibliografía y la declaración de IA reflejan los cambios del tramo.

## Correcciones realizadas

1. **Presentación institucional:** retirados los horarios contractuales, la reserva de agentes para Puelche y las comparaciones con artículos de las Bases dentro de la reseña. No se convirtió el horario de este contrato en una supuesta política histórica de LafroX.
2. **Capacidad instalada:** la Tabla 1.1 agrupa los 16 puestos compartidos y conserva 92 + 16 + 4 = 112 equipos. La nueva Tabla 1.2 compara los ocho puestos físicos del NOC (seis activos, dos de relevo) y los ocho de mesa (hasta siete de servicio y uno de reserva). Sustituye la tabla de contactos del contrato, sin renumerar las referencias a las demás tablas.
3. **Redacción:** retirada «no se requieren 32 equipos ocupados a la vez» y otras explicaciones defensivas o técnicas que interrumpían la reseña. Simplificados productos, líneas de negocio y cierre de la explicación del NOC.
4. **Sedes:** Santiago es la Sede Central; Valparaíso es el Centro de Operaciones y domicilio declarado en Av. Brasil 2241. La distinción queda explícita desde §1.1 y coincide con las tablas. No se inventó una dirección en Santiago ni se cambió el domicilio de portada.
5. **Dotación:** retirado «(PHP/Laravel, móvil Kotlin)» del rol Desarrollo de software. Esto no cambia las tecnologías de la solución. Definidos SRE, QA y los centros de operación en su explicación correspondiente.
6. **CISO:** explicado como Oficial de Seguridad de la Información. El diagrama anterior lo situaba encima de Gerencia General, contradiciendo la explicación de dependencia. Se redibujó la figura vectorial: Gerencia arriba, Seguridad y Operaciones debajo; las tres divisiones dependen de Operaciones. El CISO preside únicamente el Comité de Seguridad y Privacidad.
7. **Calidad:** separados el sistema corporativo, la evaluación de madurez CMMI y la aplicación de RUP/DevSecOps al proyecto. Eliminada la cita a RT-23.04 como aparente respaldo de la madurez propia. Conservados los controles independientes de 80 % global y 70 % de lógica de negocio.
8. **Seguridad:** corregida la afirmación de que pruebas semestrales incluyen por sí mismas las pruebas antes de cada paso a producción. La periodicidad corporativa y los controles adicionales del proyecto se describen por separado; RT-11.20 se cita con p. 24, previamente cotejada.
9. **Sitio web:** retiradas afirmaciones no demostradas sobre disponibilidad medida en vivo, TLS válido y conformidad WCAG efectiva. No se acreditaron ensayos del sitio.

## Explicación de las cifras retiradas

El Anexo 4-W.7 conserva SV-06: (640 trabajadores + aproximadamente 160 conductores externos) × 2,5 contactos/persona-mes = 2.000 contactos/mes. Es un supuesto para Puelche, no el historial agregado de clientes de LafroX ni una cifra exigida por las Bases. El factor 2,5 no tiene respaldo en un registro de servicio. Equivale a 30 contactos al año por persona y, en un mes ilustrativo de 26 días de atención, unos 77 contactos diarios.

Un contacto es una interacción de soporte: consulta, solicitud, incidente o seguimiento, según la regla de conteo que se adopte. No representa necesariamente una venta, una llamada saliente, una falla distinta o un usuario único. Los agentes son personas que atienden; los puestos son el equipamiento que utilizan. Los 2.283 y 2.391 son límites calculados bajo supuestos de distribución horaria, duración y personal, no demanda prevista ni capacidad corporativa medida.

Erlang C es un modelo de colas: relaciona llegadas, duración media y agentes simultáneos para estimar espera y atención dentro de un tiempo objetivo. No determina cuántos contactos generará la operación. El modelo básico supone que quienes esperan no abandonan; tampoco mide resolución al primer contacto. Referencias consultadas: [Genesys](https://help.genesys.com/pureconnect/mergedProjects/wh_ia/desktop/io_erlang_c.htm) y [documentación del modelo](https://www.erlang.com/erlangforexcel-manual/the_erlang_c_traffic_model.htm). La sigla CISO se contrastó con [NIST](https://csrc.nist.gov/glossary/term/ciso).

No se sustituyó SV-06 por otra tasa inventada. SD4, SD7 y T-15 permanecen fuera del alcance de edición de esta petición. La falta de sustento del escenario sigue abierta en `Revision/revision_demanda_mesa_SD1_SD4.md`; retirar su presentación corporativa no resuelve el dimensionamiento contractual.

## Verificación

- Comparación de todo el cuerpo: 117 bloques de prosa/bibliografía y 46 filas de tabla coinciden entre Markdown y LaTeX tras normalizar únicamente formato, referencias automáticas y notación matemática.
- Títulos conservados; siete tablas, una figura, diez remisiones internas con destino válido. Ninguna referencia a la antigua tabla `capacidad_mesa` permanece en el SD1.
- 56 bloques del tramo revisado cotejados con el texto del PDF, sin ausencias después de excluir encabezados y pies.
- Última compilación: tres pasadas LuaLaTeX con `--no-shell-escape`, todas con salida 0. PDF de 19 páginas carta, sin Overfull/Underfull, referencias indefinidas ni figuras demasiado grandes.
- Revisadas visualmente las 19 páginas mediante cinco paneles; la figura, tablas y textos del tramo se comprobaron con mayor detalle. Corregida la palabra huérfana al inicio de p. 10 manteniendo unido el párrafo de antigüedad. Las páginas 9 y 10 finales se volvieron a renderizar y revisar.
- Texto del organigrama en el PDF: 9,118 puntos efectivos. Inventario 112, dotación 124, NOC 32 y margen bruto 272 horas verificados aritméticamente.
- T-6 y fuentes compartidas sin modificaciones; cambios ajenos del checkout Markdown y del checkout LaTeX preservados. Sólo Markdown escrito en `rama-md`.
- Se detectó que un PDF pequeño con stream ASCII85 podía ser clasificado por Git como texto y quedar expuesto a conversión LF/CRLF. La figura se guarda con stream comprimido binario, conservando exactamente su geometría y texto. No se modificó la configuración de Git ni se añadieron atributos compartidos.

## Límites y siguientes pasos

Identificación del corte verificado (SHA-256):

- SD1 Markdown: `0459eed0c1fe54c7bac9f979a79070699959ca88f700fd08dec8f43cbc9bc52c`.
- `contenido.tex`: `71cf68f2af44352f276a58345a6c8285aeace64b286b162e88a3688803ee6cf3`.
- Figura 1.1: `13bfa301cd5d105d3d24a226ad3510d38827284a902ab53a69487468e7606511`.
- PDF SD1: `99cd2e80f9de7928a1e8c8068475e16aa17967d7bb9194f24be52d26f2f675af`.

La corrección y la sincronización del tramo no constituyen acreditación de certificados, clientes, experiencia ni mediciones de capacidad. No se afirma conformidad 100 % de todo el SD1 o de la oferta. Siguen vigentes los hallazgos fuera del alcance sobre citas y folios del T-6.

Las revisiones humanas anteriores de Alex Aravena se conservan en §1.4–§1.6 y T-6. Las filas §1.1–§1.3 requieren revisión de su nueva redacción y llevan `[[REVISIÓN HUMANA]]`; la figura redibujada se declara con nivel Alto. La entrega de esta versión sigue bloqueada hasta la revisión y firma efectivas. Ninguna revisión humana fue fabricada.

Engram no expone herramientas en este entorno; no se inventó una identidad de sesión ni se cambió su configuración. Decisiones, descubrimientos y resumen de sesión quedan registrados aquí y en `compct/CONTEXTO_SESION.md` como respaldo local.
