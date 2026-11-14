# Ajustes que debe incorporar el T-13 del SD9

Esta lista identifica cambios para la rama `LafroX-Subdoc9-LateX-corrigiendo`. No modifica esa rama ni representa pruebas ejecutadas. La comparación utiliza la matriz T-13 del commit `7483619d` y el T-12 de esta carpeta; antes de regenerar debe fijarse el commit definitivo del SD3.

## Estados y alcances

Actualizar de «Cumple» a «Cumple parcialmente» las fichas siguientes, conservando el detalle de la parte cubierta y de la brecha:

| Identificador | Materia que no se acredita totalmente |
|---|---|
| RF-18.03, RT-16.23 | Apertura de cada SMS cuando el proveedor no la informa. |
| RNF-23.02, RT-08.12 | Grado IP del PAX y características aún condicionadas a la compra para determinados equipos. |
| RT-03.18, RT-08.14 | Todas las funciones remotas de gestión para todos los dispositivos de borde. |
| RT-11.04 | Plazos máximos de remediación si no se autoriza el cambio de emergencia durante congelamiento. |

En el T-13 actual las siete fichas todavía declaran «Cumple». Su procedimiento de prueba debe verificar tanto lo ofrecido como la limitación, sin presentar el requisito íntegro como aprobado.

## Origen y alias

- Actualizar el origen de RF-09.09: capítulo 12 del Caso, no sección 12.
- Actualizar el origen de RF-12.10: retirar RT-10.05 como fuente de la ventana de entrega de 30 minutos; ese código trata la ventana operacional protegida.
- Declarar los requisitos absorbentes de RF-19.01 a RF-19.05: RT-11.03, RT-11.05, RT-11.13, RT-11.18 y RT-11.19, respectivamente. Mantener cero casos adicionales y seguir la prueba de la fila absorbente.
- Mantener los otros cuatro alias y su destino conforme al Anexo 3.A.5a; distinguir el RT-03.13 del Caso de los códigos transversales.

## Componentes, paquetes y pruebas

- Conciliar los ajustes posteriores del T-12 en RF-01.11, RF-03.03, RF-04.08, RF-12.04, RF-12.16, RF-19.05 y RT-03.10. RF-03.03 incorpora el paquete 3.4.2 de Inventario; RT-03.10 incorpora 3.4.8 de Reparto para la jornada de 14 horas. El T-13 debe reflejar ambas fuentes en RT-03.10 y sus escenarios de 24 horas en el CD y 14 horas en terreno. No se han ejecutado esas pruebas.
- El diccionario T-14 de SD7, cuenta 3.3, identifica 3.3.5 con auditoría de stock, lotes y cobros: esa descripción no acredita por sí sola el motor de reglas y su parametrización (RF-17.02 y RT-16.14) ni toda la gestión documental (RF-17.08). La cuenta 3.6 identifica 3.6.4 con avisos a clientes: no demuestra por sí sola la generación general de documentos de RF-17.09. Se requiere asignar o definir paquetes que cubran esas funciones y conciliar T-12/T-13/T-14; no se inventan códigos de paquete en SD3.
- Conciliar las 40 fichas cuyo componente se abrevia en T-12: RF-01.01, RF-01.03 a RF-01.06, RF-01.08, RF-01.11, RF-02.01 a RF-02.03, RF-02.05, RF-02.07, RF-02.09, RF-03.01 a RF-03.08, RF-03.10 a RF-03.16, RF-04.01 a RF-04.05, RF-04.08, RF-12.02, RF-12.04, RF-12.05 y RF-12.07 a RF-12.09. Verificar que cada síntesis conserve la misma función y que las versiones sigan localizables en SD4 y T-11.
- RNF-23.01, RNF-23.02 y RT-08.11 ya usan en T-13 una síntesis con remisión al T-12; conservarla solo si refleja el componente vigente y el estado actualizado.
- RT-26.01, RT-26.02 y RT-26.03 remiten a la cuenta 3.10; RT-26.02 también a la cuenta 8.3. Seguir las tareas concretas de cada innovación en el T-14 y T-19 y verificar su pertinencia por requisito. Una cuenta no es un paquete hoja.
- Para RT-16.14, documentar escenarios diferenciados para el motor de reglas de las Bases Transversales y para la articulación de la prueba de entrega y el acuse exigida por el Caso. Verificar además los demás códigos RT compartidos por ambas fuentes sin presumir equivalencia de significado.
- Conciliar todas las demás discrepancias que surjan del cotejo semántico individual. Los identificadores `/Pnn` del formulario son pruebas previstas: completar sus pasos, datos, ambientes y evidencias en la etapa que el T-13 establece; no declarar una prueba ejecutada por su presencia en la matriz.

El inventario `auditoria_pendientes_sd3.csv` contiene las 653 filas y sus referencias de contraste. Sus campos de revisión actual se mantienen pendientes: la correspondencia de texto o números no prueba suficiencia semántica.
