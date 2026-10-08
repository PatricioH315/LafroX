# Reorganización editorial mediante punteo en 4.1

Rama: `subdoc-4`. Se aplicó el plan de lectura aprobado por el usuario, con su condición de conservar el contenido.

Los cambios separan oraciones o cláusulas existentes mediante `itemize` y `enumerate`; no añaden ni eliminan palabras, cifras, condiciones, referencias, títulos o identificadores. Los pasos numerados se limitan al recorrido de reserva física y a la secuencia preparación–guía–entrega–conciliación. Las responsabilidades y excepciones usan viñetas. Se conserva el orden original del contenido.

## Alcance

Se reorganizaron trece fragmentos: principios de integración, capas de arquitectura, módulos y límites de contexto, detalle tecnológico, implantación Laravel, ambientes y promoción, patrones y continuidad, relación entre vistas, funciones sin conexión, reconciliación, POD–DTE–acuse, conductores externos y condiciones de diseño.

Se conservaron los párrafos de fundamentación, las tablas comparativas y las listas existentes que ya facilitan la lectura. Se agruparon los ambientes en una lista de cinco puntos y las condiciones de implantación en seis puntos, para evitar fragmentación excesiva. Los apartados restantes y el ensamblador permanecen íntegros.

## Preservación

Se respaldaron los 23 fuentes `.tex` de lógica inmediatamente antes de editar en `tmp/punteo-4.1-antes/`, fuera del repositorio. La comparación entre respaldo y resultado elimina únicamente comandos de inicio/fin de listas, `\item`, `\par`, el entorno de maquetación `samepage` y diferencias de espacios. El texto completo normalizado debe coincidir exactamente y en el mismo orden para cada archivo.

La comprobación confirmó coincidencia en los 23 archivos; trece cambiaron de organización. El informe reproducible está en `output/pdf/punteo-4.1/preservacion-contenido.json`, fuera del repositorio.

El documento principal se compiló con LuaLaTeX hasta estabilizar sus referencias: 162 páginas, sin referencias indefinidas, errores LaTeX ni desbordamientos `Overfull` en el registro final. Se revisaron páginas renderizadas de presentación, seguridad, reserva comercial, tecnologías, implantación, ambientes, operación offline, reconciliación, secuencia tributaria y conductores. Se ajustó la continuidad de las viñetas de recuperación sin cambiar su texto.

Los diagramas incorporados en la tarea precedente, su límite de letra impresa y los asuntos de coherencia técnica conservan su estado. Esta reorganización editorial no resuelve esas brechas ni modifica decisiones técnicas. No se editaron fuentes de 4.2, 4.3, anexos ni formularios.
