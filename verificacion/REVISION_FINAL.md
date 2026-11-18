# LafroX — Revisión final del SD10, versión 0.2

Fecha: 17 de noviembre de 2026. Estado: borrador revisado. La revisión automática y visual asistida por Codex no acredita revisión humana ni aceptación del CLIENTE.

## Cambios verificados frente al contraste

| Punto | Resultado documental |
|---|---|
| Índice obligatorio | Capítulo «Introducción a los Servicios», con 10.1 y 10.2 conservados. |
| Declaración de IA | Tabla de seis columnas y siete filas: secciones 10.1/10.2 y anexos 10.A–10.E. No se atribuye revisión humana. |
| Redacción y fuentes | Retirada la frase «El usuario autorizó…» y la referencia técnica a la plantilla. Citas de bases con páginas; notas de preparación sustituidas por condiciones del servicio. |
| Atención y escalamiento | Recepción telefónica y alertas vinculadas al ticket; clasificación, transferencia, primera atención, restitución, confirmación de cierre y relevo definidos. |
| Acuerdos operacionales | Funciones, disparadores, evidencia y coordinación desarrollados. La derivación no reinicia relojes ni suma tiempo al máximo externo. Presupuestos numéricos internos y formalización siguen sin acreditarse. |
| Hardware | Mínimos BTT 8.4 incorporados: crítico 24×7/4h, no crítico 24 h, reemplazo crítico 4 h desde diagnóstico, fabricante y reserva mínima 10 %. No se añaden compras ni precios. |
| Retención | Política técnica incorporada desde SD4/SD5: registros 12 meses en línea + 24 meses de archivo, métricas 13 meses, trazas 30 días sin archivo adicional, auditoría/seguridad 7 años; ADOT 24 h temporal. |
| Procedimientos | Nueve guías GU-01–GU-09 con responsables, acciones, escalamiento, precauciones y comprobación. Recuperación regional y retorno controlado desarrollados. |
| Indicadores | Causa raíz media a solicitud y baja no exigida; fórmulas operacionales y tratamiento de denominador cero. Se distinguen contacto, ticket, restauración y cierre. |
| Calendario | Ventanas y congelamientos explícitos; prohibición de paso en septiembre completo de SD4 conservada sin presumir excepciones. |
| Detección proactiva | Mecanismo determinista de comparación histórica y prueba de degradación gradual recogido desde SD4. |
| Matriz y trazabilidad | Estados diferenciados entre diseño documentado, formalización, ensayo y conciliación económica; doce cambios V02-01–V02-12 trazados. |

## Comprobaciones realizadas

Se conserva el conjunto de fuentes congelado para la versión 0.1. Las incorporaciones se cotejan con fuentes LaTeX y sus PDF, sin espejos Markdown de subdocumentos. Bases y aclaraciones se consultan en sus archivos de origen.

El desglose de retención sí estaba en SD4, fuente lógica líneas 582 y 623–625, y en SD5, gestión línea 85. Se corrige la omisión del contraste previo. En los PDF del mismo commit se localizan los pasajes de SD4 en páginas de archivo 47–49 y el de SD5 en página 35. La política de archivo adicional de métricas no se inventa ni se generaliza desde los registros técnicos.

Se cotejan visualmente los folios impresos 6 de BA (artículo 5),19 de BTT (soporte de hardware) y 26–27 del Caso (p95 y ventanas). En esos PDF de imagen, la posición de archivo es el folio+1. Las huellas se añaden al manifiesto de fuentes.

El script comprobar_calculos.py reproduce diez controles: Erlang C 90,6%/84,2%; límites enteros de contactos; sensibilidad 6.000; DR 135 min; reducción teórica de horas 64,3%; plazas 8/13 y fracción de deuda técnica 2,0985%. No acredita abandono real, demanda observada ni ensayo ejecutado.

El script comprobar_entrega.py verifica PDF legible y sin páginas vacías, título, declaración de IA completa en una página, nueve guías, retención, causa raíz media, ausencia de notas del usuario, referencias resueltas, ausencia de glifos faltantes, desbordes horizontales y tablas partidas. Conserva páginas y SHA-256 en resultado_entrega.json.

Se renderizan todas las páginas de ambos PDF para inspeccionar portada, índices, folios, contenido, tablas y diagramas. Se ajusta el ancho de la declaración de IA y se evita la separación automática de palabras en tablas, conservando tipografía y clase corporativas.

## Dependencias conservadas y límites

La versión desarrolla lo respaldado, sin asignar nombres, contactos, productos, contratos, mediciones, firmas o aprobaciones inexistentes. B-04 ya no identifica ausencia de política técnica; mantiene la comprobación del costo asociado en E2 fuera de este alcance. Las condiciones B-01–B-10 conservan las dependencias de sitio adicional, habilitación, acuerdos específicos, relojes, ERP, cuadrante/calibración, SD11/12 y conciliación técnica-económica.

No se requiere fingir contratos ya suscritos para declarar cobertura propuesta. Sí se requiere formalizar y habilitar el servicio, y someter sus procedimientos a las pruebas indicadas. Los nuevos campos de registro y las fórmulas se identifican como elaboración procedimental y metodológica, no como citas literales ni decisiones aprobadas.

Sólo se modifica la rama de corrección de SD10. El Excel, E2 y los demás subdocumentos no se editan. El resultado continúa siendo borrador hasta contar con revisión humana real.
