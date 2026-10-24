# LafroX — Justificación de tecnologías del backend

## Autorización y base

El usuario pidió ejecutar el plan de justificación de Laravel/PHP para el monolito modular, incluir Kotlin y Django como contraste con versiones anteriores, partir del último commit de GitHub y publicar con el mensaje `justificacion de tecnologias`.

Antes de editar se ejecutó pull con avance directo. Bases verificadas: `subdoc-4` en `76221edd925b735bb9c380c56fae7cd3ac908778` y `rama-md` en `97fcdae174b79110784a358760601c2298d5c00d`. Se incorporaron los ajustes remotos del SD4 antes de redactar. Los archivos no versionados del checkout LaTeX se preservaron. El contexto Markdown local se respaldó fuera de la rama, se guardó temporalmente con stash y se restituyó sobre el contexto actualizado conservando ambos registros. Sus cambios previos quedan fuera del commit de esta tarea.

## Alcance

- Nueva sección 4.1.7.1, con criterios de adecuación, contraste Django/Python, tabla comparativa, Kotlin y límites de aceptación.
- ADR-23 para el framework; ADR-01 conserva el estilo arquitectónico. Resumen, fecha/estado y recuento actualizados a 23.
- Ajustes de 4.1.13 y Anexo 4-P; referencias oficiales y declaración de uso de IA ampliadas.
- Node.js/NestJS, Spring/Java, Kotlin de servidor y ASP.NET Core se presentan como alternativas. No se incorporan al inventario ofertado.
- Se conservan perfiles, dimensionamiento, contratos y decisiones de despliegue vigentes. No se afirma desempeño medido ni experiencia del equipo sin evidencia.

## Antecedente Django

En `e55133c`, `04_arquitectura/entrega_1/texto/arquitectura_logica.md` declara Django/Python 3.12 para M1–M12. La física del mismo corte describe aplicaciones por dominio y trabajadores Celery. Este antecedente acredita el diseño anterior, no una implantación real. La documentación vigente explicaba la selección con un único runtime; ese criterio se reemplaza porque también puede cumplirse con una solución Python. No se identificó en las fuentes consultadas una medición comparativa ni una motivación histórica adicional que permita atribuirle el cambio; la nueva ficha fundamenta la propuesta actual.

## Evidencia y revisión

La comparación se apoya en documentación oficial de Laravel 13, Django 5.2/6.0, Celery, Spring Modulith, Kotlin/Ktor, NestJS y ASP.NET Core consultada el 24 de octubre de 2026. Las versiones de Django identifican las capacidades comparadas; no son una propuesta de dependencia nueva. Las referencias se incluyen en cuerpo y anexos.

Se conserva la revisión humana previa atribuida a Álvaro Catalán y se marca `[[REVISIÓN HUMANA]]` exclusivamente para la ampliación en las filas 4.1, 4-O y 4-P. La compilación y la publicación no acreditan revisión humana ni ejecución de ensayos de aceptación. La conformidad de entrega de la ampliación requiere esa revisión según las instrucciones del repositorio.

## Verificación técnica

LuaLaTeX compiló cuerpo y anexos con salida 0, sin Overfull ni referencias indefinidas en los logs finales. El cuerpo conserva 189 páginas y los anexos 111. Se inspeccionaron las páginas 67–70, 185, 186 y 188 del cuerpo, y 56 y 108 de los anexos: sección, matriz, transición, referencias, declaración y ADR legibles. La introducción se recompiló al cierre para incluir también ADR-23 en el rango del registro.

Las secciones 4.1.7, 4.1.11 y 4.1.13 de Markdown coinciden íntegramente con la conversión de las fuentes finales, normalizando solo espacios y controles de formato. Las 23 fichas y las 46 filas de los dos resúmenes ADR están presentes. Se conservaron los enlaces de todas las figuras de los dos Markdown y el PDF T-11 permanece idéntico byte por byte a la base. Se actualizó la numeración corrida de tablas y sus remisiones en el cuerpo al insertar la Tabla 3. El resto de los apartados Markdown mantiene su contenido de origen; no se declara una armonización integral de diferencias previas entre ramas.

La publicación incluye las fuentes afectadas, cuerpo y anexos PDF y este registro; en rama-md, solo cuerpo, anexos y registro equivalente. El contexto previo local y los archivos no versionados quedan fuera de esos commits.

SHA-256 del cuerpo: `cccbf44ceb4871478e14ebd090a7cd1b42e461ae34a169853e80fed03128f39b`.

SHA-256 de los anexos: `d006b0827c82b1581e9f8a47521ec12c5e0d1edee527e106abf4d21b774b8675`.
