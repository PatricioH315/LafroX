# Ajustes que debe incorporar el T-13 del SD9

Esta lista identifica cambios para la rama `LafroX-Subdoc9-LateX-corrigiendo`. No modifica esa rama ni representa pruebas ejecutadas. El contraste usa la matriz T-13 del commit `0c57a4bb`, el T-14 del SD7 `68669bef`, el SD4 `69c9a879` y el T-12 de esta carpeta; antes de regenerar debe fijarse el commit definitivo del SD3. Los cambios de SD4 desde `2d508f46` afectan referencias, foliación y herramientas de comprobación; no convierten la lectura preliminar en un cotejo semántico completo. Se incorporó en RT-21.21 la actualización remota del SD3 `40d415db`, coincidente con la nueva matriz T-13 y el resumen de T-15.

## Estados y alcances

Actualizar de «Cumple» a «Cumple parcialmente» las fichas siguientes, conservando el detalle de la parte cubierta y de la brecha:

| Identificador | Materia que no se acredita totalmente |
|---|---|
| RF-18.03, RT-16.23 | Apertura de cada SMS cuando el proveedor no la informa. |
| RNF-23.02, RT-08.12 | Grado IP del PAX y características aún condicionadas a la compra para determinados equipos. |
| RT-03.18, RT-08.14 | Todas las funciones remotas de gestión para todos los dispositivos de borde. |
| RT-11.04 | Plazos máximos de remediación si no se autoriza el cambio de emergencia durante congelamiento. |
| RNF-20.06, RT-07.04 | RPO de quince minutos ante el aislamiento de los tres enlaces seguido de destrucción del sitio antes de replicar. |

En el T-13 contrastado las nueve fichas todavía declaran «Cumple». Su procedimiento de prueba debe verificar tanto lo ofrecido como la limitación, sin presentar el requisito íntegro como aprobado. La matriz T-13 contiene 22 fichas parciales mientras su texto introductorio indica 18; T-12 contiene 31 filas parciales.

## Origen y alias

- Corregir en T-13 la transcripción de RT-07.09: las Bases y T-12 indican 3-2-1-1-0, no 3-2-1-0. Las 374 exigencias transversales y los 26 complementos del Caso coinciden en texto normalizado con las fuentes después de ese ajuste; la comparación textual no certifica la solución ni la prueba.
- Actualizar el origen de RF-09.09: capítulo 12 del Caso, no sección 12.
- Actualizar el origen de RF-12.10: retirar RT-10.05 como fuente de la ventana de entrega de 30 minutos; ese código trata la ventana operacional protegida.
- Declarar los requisitos absorbentes de RF-19.01 a RF-19.05: RT-11.03, RT-11.05, RT-11.13, RT-11.18 y RT-11.19, respectivamente. Mantener cero casos adicionales y seguir la prueba de la fila absorbente.
- Mantener los otros cuatro alias y su destino conforme al Anexo 3.A.5a; distinguir el RT-03.13 del Caso de los códigos transversales.

## Componentes, paquetes y pruebas

- Conciliar RF-01.09: T-12 distingue el evento `RecepcionConfirmada` que alimenta M2 de la solicitud al ERP encolada y procesada por INT-06/ACL con reintento automático. Verificar además que el paquete de integración y los casos previstos cubran el intercambio y la caída del ERP.
- Actualizar los 62 criterios de los catálogos RF modificados en SD3. Sus identificadores individuales aparecen en `auditoria_pendientes_sd3.csv` con `criterio_coincide_catalogo=False`; no se consideran diferencias de contenido las de mera puntuación o formato. Incorporar los cambios de componentes y referencias del mismo inventario y regenerarlo desde el SD3 definitivo.
- Para la columna de componentes, la comparación textual muestra 108 fichas con redacción distinta de la matriz T-13. Algunas diferencias son abreviaciones equivalentes y deben cotejarse por su alcance antes de actualizar; no deben interpretarse automáticamente como 108 errores funcionales.
- Conciliar en T-13 los estados parciales de RNF-20.06 y RT-07.04: el Anexo 4-M de SD4 describe el caso de aislamiento de los tres enlaces seguido de destrucción del sitio como brecha del RPO, sin asumir aceptada una excepción.
- Sustituir en RT-26.02 las cuentas 3.10 y 8.3 por los 23 paquetes hoja de las cinco innovaciones identificados en el T-12 actual. RT-26.01 y RT-26.03 siguen citando la cuenta 3.10 y requieren identificar si existe un paquete específico que cubra su propósito documental.
- Conciliar los nuevos ajustes de RF-01.05 (añade 3.4.2 para M2), RF-12.05 (M11 entrega el pedido a M3 y M4 lo planifica; añade 3.4.7), RF-12.12 (firma o fotografía y nombre según corresponda), RF-12.14 y RF-12.17. La descripción abreviada de M5 y de los portales se aplicó a RF-05.01, RF-05.02, RF-05.05, RF-05.07, RF-12.14 a RF-12.19, RF-12.22, RF-12.23, RF-12.26, RF-12.28 y RF-12.29.
- Corregir los nombres de herramientas en RNF-14.07, RT-04.05 y RT-11.22: PHPStan y PHPUnit, según corresponda. En RT-05.10 explicitar, como en T-12, que el catálogo con linaje automatizado no se oferta; la retención del Caso se mantiene y el cumplimiento sigue siendo parcial.
- Revisar las observaciones técnicas del cotejo de SD4 `04/revision/COTEJO_TRAZABILIDAD_CONTRACTUAL_SD4.md`: en particular RNF-20.06 y RT-07.04, por el escenario de aislamiento seguido de destrucción del sitio; RT-03.24, por las fuentes y la distinción entre estimación de cobertura y medición; y RT-16.18, por la suficiencia del sello temporal. Son hallazgos a contrastar, no resultados de pruebas ejecutadas ni cambios automáticos de estado.
- Conciliar los ajustes posteriores del T-12 en RF-01.11, RF-03.03, RF-04.08, RF-12.04, RF-12.16, RF-19.05 y RT-03.10. RF-03.03 incorpora el paquete 3.4.2 de Inventario; RT-03.10 incorpora 3.4.8 de Reparto para la jornada de 14 horas. El T-13 debe reflejar ambas fuentes en RT-03.10 y sus escenarios de 24 horas en el CD y 14 horas en terreno. No se han ejecutado esas pruebas.
- El diccionario T-14 de SD7, cuenta 3.3, identifica 3.3.5 con auditoría de stock, lotes y cobros: esa descripción no acredita por sí sola el motor de reglas y su parametrización (RF-17.02 y RT-16.14) ni toda la gestión documental (RF-17.08). La cuenta 3.6 identifica 3.6.4 con avisos a clientes: no demuestra por sí sola la generación general de documentos de RF-17.09. Se requiere asignar o definir paquetes que cubran esas funciones y conciliar T-12/T-13/T-14; no se inventan códigos de paquete en SD3.
- Conciliar las 40 fichas cuyo componente se abrevia en T-12: RF-01.01, RF-01.03 a RF-01.06, RF-01.08, RF-01.11, RF-02.01 a RF-02.03, RF-02.05, RF-02.07, RF-02.09, RF-03.01 a RF-03.08, RF-03.10 a RF-03.16, RF-04.01 a RF-04.05, RF-04.08, RF-12.02, RF-12.04, RF-12.05 y RF-12.07 a RF-12.09. Verificar que cada síntesis conserve la misma función y que las versiones sigan localizables en SD4 y T-11.
- RNF-23.01, RNF-23.02 y RT-08.11 ya usan en T-13 una síntesis con remisión al T-12; conservarla solo si refleja el componente vigente y el estado actualizado.
- RT-26.01 y RT-26.03 remiten a la cuenta 3.10. Seguir las tareas concretas de cada innovación en el T-14 y T-19 y verificar su pertinencia por requisito. Una cuenta no es un paquete hoja.
- Para RT-16.14, documentar escenarios diferenciados para el motor de reglas de las Bases Transversales y para la articulación de la prueba de entrega y el acuse exigida por el Caso. Verificar además los demás códigos RT compartidos por ambas fuentes sin presumir equivalencia de significado.
- Conciliar todas las demás discrepancias que surjan del cotejo semántico individual. Los identificadores `/Pnn` del formulario son pruebas previstas: completar sus pasos, datos, ambientes y evidencias en la etapa que el T-13 establece; no declarar una prueba ejecutada por su presencia en la matriz.

El inventario `auditoria_pendientes_sd3.csv` contiene las 653 filas, sus referencias y el resultado individual del examen de componentes. La mayoría tiene lectura preliminar y conserva pendiente el contraste semántico de fuente, alcance del paquete y suficiencia de prueba. La correspondencia de texto o números no prueba suficiencia semántica.
