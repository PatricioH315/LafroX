# Acreditación de diferencias LaTeX–Markdown del Subdocumento 4

Fecha: 2026-10-07. Revisión de solo lectura del Markdown de `rama-md` frente a las fuentes LaTeX de `subdoc-4` con sus modificaciones locales vigentes. No se modificó el Markdown.

## Fuentes y método

- Markdown cotejado: `LafroX-rama-md/04_arquitectura/LAFROX-Subdocumento4.md`, `LAFROX-Subdocumento4-Anexos.md` y `LAFROX-Formulario-T-11.md`, commit `2ae97a7` de `rama-md`.
- El commit `2ae97a7` declara una regeneración desde el LaTeX `c1f0874`. El conversor `00/herramientas/tex2md.py` fija ese mismo commit para las URL de figuras.
- Se ejecutó el conversor sobre las fuentes LaTeX actuales en una carpeta temporal y se compararon los tres pares de archivos línea por línea. Resultado: 53 bloques distintos en el cuerpo, 22 en anexos y 13 en T-11. Los bloques son diferencias de texto, no 88 hallazgos independientes.
- Se contrastaron las cifras y las decisiones principales con los fragmentos `.tex`, el anexo de cálculo, el T-11 y las figuras modificadas. La comparación no atribuye al Markdown una decisión nueva independiente: deriva de una versión anterior del LaTeX.

## Diferencias sustantivas

| Tema | Markdown de `rama-md` | LaTeX vigente | Evidencia LaTeX | Impacto |
|---|---|---|---|---|
| Alta disponibilidad en sitios | Concepción tiene un servidor; cada cross-docking, un mini-PC. Una falla exige reposición y reconstrucción central. | Concepción tiene dos servidores y cada cross-docking dos mini-PC, con par activo/en espera, réplica sincrónica y toma de control local. La reconstrucción central queda para la pérdida de ambos. | `04/partes/4.2_fisica/02_a_emplazamiento.tex`, `11_j_despliegue.tex`, `04/anexos/logica/partes/18_anexo_4_1_o_decisiones_logicas.tex` | Alto: cambia la continuidad y el cumplimiento de RT-03.14. |
| T-11 y energía de borde | Un servidor de Concepción y UPS de 3 kVA; cinco instancias A-02; cinco cachés/verificadores A-05; cinco colectores F-01. | Dos servidores, UPS de 5 kVA, nueve instancias A-02 (cuatro en espera), nueve cachés/verificadores y nueve colectores. Cambian también carga y UPS calculadas: Concepción 3,42 kVA y cross-docking 0,42 kVA. | `04/formularios/T11/15_anexo_t11.tex`, `04/anexos/fisica/16_anexo_4b_memoria_calculo.tex` | Alto: el inventario y la capacidad ofertada del MD no describen la arquitectura actual. |
| Terminales cross-docking | Siete terminales, con 183 terminales restantes. | Nueve terminales, con 185 restantes. | `04/partes/4.2_fisica/12_k_dimensionamiento.tex`, `04/anexos/fisica/16_anexo_4b_memoria_calculo.tex` | Medio: altera dotación y cálculos de despliegue. |
| Mensajería y observabilidad | INT-14 cuenta 13.000 eventos/día; total 228.852 normal y 351.933 peak. | INT-14 agrega siete nodos en espera a 200 eventos/día: 14.400. Total 230.252 normal y 353.333 peak. | `04/anexos/logica/partes/08_anexo_4_1_g_catalogo_de_interfaces_internas.tex`, `10_anexo_4_1_i_volumen_de_mensajes.tex`, `04/partes/4.2_fisica/12_k_dimensionamiento.tex` | Medio: cuerpo, anexo y memoria del MD conservan totales obsoletos. |
| Red y almacenamiento | El MD conserva varias capacidades previas, por ejemplo Concepción fibra 1,88 Mbps y LTE 1,21 Mbps; temperatura 0,56 GB/año en el cuerpo. | Concepción fibra 2,14 Mbps y LTE 1,44 Mbps; temperatura 0,58 GB/año y 2,89 GB en cinco años. | `04/partes/4.2_fisica/12_k_dimensionamiento.tex`, `04/anexos/fisica/16_anexo_4b_memoria_calculo.tex` | Medio: cambia la justificación de capacidad. El anexo MD ya decía 0,58 GB/año, mientras su cuerpo decía 0,56; el LaTeX actual los alinea. |
| Mesa de ayuda | El resumen MD afirma que siete agentes cubren 2.391 contactos/mes. | El límite de la dotación con dos agentes en franjas valle es 2.283; 2.391 solo se alcanza agregando un tercer agente en esas franjas. | `04/partes/4.2_fisica/12_k_dimensionamiento.tex`, `04/anexos/fisica/16_anexo_4b_memoria_calculo.tex` | Medio: el resumen MD sobrestima la capacidad base, aunque su anexo ya explica el límite de 2.283. |
| Despliegue y recuperación | Actualización de contenedores en sitios sin describir migración aditiva, orden del par ni prueba de conmutación local. | Migraciones aditivas al activo, réplica al equipo en espera, actualización ordenada, ensayo de falla de activo y retención de 24 h del outbox aun tras envío. | `04/partes/4.2_fisica/11_j_despliegue.tex`, `04/partes/4.3_centros_de_datos/06_e_sitio_secundario.tex` | Alto: faltan controles operacionales vinculados al nuevo diseño. |
| Direccionamiento y ERP | Un bloque 10.6.0.0/16 reservado; no explicita la dependencia del ERP para emitir una guía nueva en la contingencia descrita. | Reserva 10.6.0.0/16 y 10.7.0.0/16; aclara que una guía nueva espera la restitución del ERP si se pierde la sala de Talca. | `04/partes/4.2_fisica/11_j_despliegue.tex` | Medio: el MD omite condiciones del crecimiento y de la salida documental. |
| Importes históricos | El cuerpo MD conserva las pérdidas del retiro y el promedio mensual de diferencias de rendición. | El LaTeX actual conserva los problemas operacionales sin esos importes. | `04/partes/4.1_logica/05_modulos_funcionales_y_limites_de_contexto.tex` | Editorial: reproduce un texto que ya fue retirado del entregable vigente. |

También hay correcciones de referencias, formulaciones de seguridad, detalle de dispositivos Zebra, cambios en ADR-10, soporte de RabbitMQ y lista bibliográfica. Son cambios del LaTeX actual; la tabla recoge los que afectan decisiones o cifras.

## Defectos de conversión y figuras

1. El Markdown conserva los importes como `\31 millones` y `\4,2 millones` en lugar de una representación legible de `\$`. El conversor no trata correctamente el dólar literal de LaTeX. La corrección editorial actual elimina ambos pasajes, pero el defecto del conversor sigue existiendo para otros `\$` futuros.
2. Todas las URL de figuras del Markdown apuntan al commit fijo `c1f0874`. Hay tres PNG del LaTeX modificados después de ese commit: `Arquitectura_Fisica_General.png`, `Arquitectura_Fisica_Crossdocking.png` y `Arquitectura_Fisica_CD_Concepcion.png`. Regenerar solo el texto con el conversor actual seguiría mostrando las imágenes antiguas en Markdown.
3. La representación Markdown de tablas, referencias y figuras procede de `tex2md.py`. La comparación de bloques de texto no prueba por sí sola equivalencia visual con los PDF; especialmente las figuras deben revisarse desde sus archivos actuales al sincronizar.

## Dictamen

El LaTeX está más avanzado en las decisiones y cifras comparadas. El Markdown de `rama-md` no está acreditado como reflejo vigente del Subdocumento 4: mezcla la versión anterior de alta disponibilidad y T-11 con algunos cálculos que ya habían sido corregidos en sus anexos. Para alinearlo, hay que regenerar los tres archivos desde el LaTeX actual, actualizar el destino de las figuras a una revisión que contenga los PNG actuales y repetir esta comparación. Ningún cambio se aplicó a `rama-md` durante esta auditoría.

## Cierre posterior de sincronización

Por solicitud posterior del usuario, los tres Markdown de `rama-md` se regeneraron desde el LaTeX vigente. Los tres archivos copiados son idénticos a la conversión preparada; ya no contienen los dos importes históricos ni los totales antiguos 228.852/351.933. Se verificaron 327 enlaces internos sin destinos ausentes y los tres enlaces locales a los PNG físicos vigentes. Se actualizó `compct/CONTEXTO_SESION.md` en la rama Markdown. Las tres imágenes modificadas se enlazan al checkout hermano `LafroX`, por lo que el contenido queda alineado dentro de este workspace; para publicar los Markdown como documentos independientes habrá que sustituir esas rutas por enlaces a una revisión publicada de los PNG actuales.
