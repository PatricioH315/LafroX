# Reemplazo de las figuras de arquitectura lógica

Rama de trabajo: `subdoc-4`. Base: `d397c30ff8ad232ec4e3ea02caf5f3cb6800a547`.

Se incorporó el XML aprobado que reúne el general definitivo y ocho vistas independientes de capa. Fuente conservada en `04/figuras/fuentes/Arquitectura-logica-general-y-8-capas.drawio.xml`; SHA-256: `48b829eb2a731cd408f3f1bb17b990da34ad36426782717149e45853fb2ac14c`.

Las nueve páginas se exportaron con draw.io a PDF de una página y texto seleccionable en `04/figuras/logica/capas/`. Se preservaron todos los elementos y conexiones del XML recibido. Los originales y recortes anteriores permanecen como respaldo, pero las ocho figuras de detalle del apartado Capas ya no los insertan. La vista resumida, los diagramas de secuencia, el acceso local y el modelo conceptual mantienen sus archivos anteriores.

El fragmento `04/partes/4.1_logica/04_capas_de_la_arquitectura.tex` inserta las nuevas figuras en páginas horizontales, conserva sus títulos externos, etiquetas, referencias y fuentes, y amplía la explicación de dispositivos y canales de presentación. El resto del contenido técnico se mantiene.

## Verificación

El documento principal compiló con LuaLaTeX en tres pasadas. Se revisaron las nueve páginas renderizadas y se comprobó su correspondencia con las figuras insertadas, sin referencias indefinidas en el registro final. El resultado contiene 160 páginas. No se modificaron fuentes físicas, anexos ni formularios.

| Vista | Página del PDF | Menor letra medida dentro de la figura (pt) |
| --- | --- | --- |
| General | 13 | 2,18 |
| Presentación | 16 | 3,28 |
| Borde | 19 | 7,97 |
| Enlace de servicios | 21 | 5,63 |
| Negocio | 24 | 5,13 |
| Integración y eventos | 26 | 5,56 |
| Datos | 33 | 6,85 |
| Seguridad | 36 | 7,97 |
| Observabilidad | 41 | 8,23 |

Las medidas se obtuvieron del texto Arial de los PDF insertados, excluyendo títulos externos, cabeceras y pies. Las cifras describen el resultado impreso, no los tamaños nominales de draw.io.

## Brecha abierta de presentación

El reemplazo está aplicado, pero las figuras todavía no cumplen el mínimo impreso de 9 puntos de las aclaraciones. El PDF vectorial mejora la nitidez y permite ampliar en pantalla; eso no acredita legibilidad sin ampliar. La composición general completa y la vista de presentación son especialmente densas. La capa 1 también conserva etiquetas contiguas de TypeScript/Tailwind que deben separarse al adaptar su composición.

Para cerrar esta brecha se requiere adaptar la composición de publicación: aumentar letras y espacio de los rótulos, aprovechar el formato legal horizontal permitido y preparar vistas complementarias independientes cuando el contenido no quepa, conservando todas las relaciones en los fuentes editables. No se ha simplificado el general definitivo ni eliminado recorridos para aparentar cumplimiento.

La sustitución tampoco acredita por sí sola una auditoría completa de cada conexión contra todos los permisos del Anexo 4-N. Se verificó la correspondencia de las tecnologías y responsabilidades principales con el apartado de capas; no se cambió una decisión técnica para acomodarla al dibujo.
