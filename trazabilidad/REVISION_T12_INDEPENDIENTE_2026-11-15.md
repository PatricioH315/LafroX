# Revisión independiente del formulario T-12

Se contrastó el T-12 local, incluidos sus cambios sin confirmar, con los catálogos del SD3 y las referencias locales de SD4 `69c9a879` y SD7/T-14 `68669bef`. No se modificó SD9 ni el T-13. La comparación de identificadores y textos no sustituye la revisión individual de la suficiencia de cada componente y paquete.

## Correcciones

- El resumen registra 599 filas «Cumple», 32 «Cumple parcialmente» y 22 «No cumple». El cambio a 32 parciales incluye RT-16.18.
- RT-03.24 distingue el diseño predictivo de la verificación en sitio y la medición posterior a la instalación; se precisan las referencias de SD4.
- RT-16.18 declara cumplimiento parcial: conservar una marca de registro y la evidencia descrita no acredita por sí solo el sello de tiempo ni la verificación después del vencimiento del certificado. Deben precisarse el mecanismo y su comprobación con SD4.
- RF-17.02, RF-17.08 y RT-16.14 conservan la referencia 3.3.5, y RF-17.09 la referencia 3.6.4, con una advertencia de que debe precisarse su alcance en T-14. El diccionario describe 3.3.5 como registro auditable de stock, lotes y cobros, y 3.6.4 como integración de avisos; esas descripciones no acreditan por sí solas todas las funciones de reglas y documentos asignadas. No se asignaron códigos nuevos.

## Comprobaciones y dependencias

- Se contaron 653 identificadores únicos con seis columnas y sin celdas vacías; los 270 requisitos de los catálogos están presentes. Los 374 textos RT de BTT coinciden con sus fuentes tras normalizar formato. Tres descripciones RNF difieren textualmente del catálogo (RNF-04.01, RNF-14.06 y RNF-23.04); se examinaron sus diferencias de redacción y no se modificaron en este corte.
- Todos los números de paquete o cuenta extraídos de T-12 aparecen en el diccionario o jerarquía T-14. Esta comprobación de existencia no acredita que cada paquete cubra la función asignada. Además de las cuatro filas señaladas, RT-26.01 y RT-26.03 citan la cuenta 3.10: queda por identificar el paquete específico que cubre su propósito documental.
- El mismo contraste debe extenderse a RT-16.19 y RT-16.29: sus filas citan respectivamente 3.6.4 para generación de documentos y 3.3.5 para exportación asíncrona, funciones no explicitadas en los entregables de esos paquetes.
- El cotejo semántico individual de todos los componentes, referencias y alcances EDT permanece abierto; el inventario anterior es una lectura preliminar y sus huellas deben actualizarse antes de reutilizarlo como estado vigente.
- SD3-04 permanece parcial en el ámbito del T-12: falta precisar pruebas, criterios y cobertura de algunos paquetes. RT-16.14 conserva dos exigencias diferenciadas y RT-16.18 su brecha declarada.
- SD3-06 se atiende reduciendo la repetición de pilas tecnológicas en la columna de componente. Se conservan el módulo o servicio, la función y las condiciones técnicas relevantes; los productos y versiones compartidos se encuentran en SD4 y T-11. Este cierre se refiere a la repetición observada, no a una certificación completa de los requisitos.
