# SD9 alineado con el T-15 publicado

> Registro de la primera unidad de cambios. La actualización posterior del catálogo, matriz y criterios internos está en ACTUALIZACION_INTERNA_SD9_2026-10-26.md; sus cifras sustituyen las de regresión y fallas consignadas aquí.

Se corrigen las discrepancias de fechas, holguras, referencias y horas identificadas en la revisión del SD7. La actualización se limita al SD9, sus anexos y formularios T-13/T-17. No se modifica el SD7 ni se presenta su CPM pendiente como validado.

## Referencias de trabajo

- Rama de edición: `LafroX-Subdoc9-LateX`, base `30f7bc62`.
- Fuente SD7: `70aed659`, rama `origin/LafroX-Subdoc7-LateX`, actualizada con `git fetch` antes de editar.
- Fechas de paquetes: tabla fuente `tab_T15_paquetes.tex` (Tabla 7.10 publicada).
- Entregas, actas, límites y holguras: `tab_T15_7.tex` (Tabla 7.8 publicada).
- Base de esfuerzo: 227 paquetes, 220.023 HH. No se adoptan como línea base las fechas distintas obtenidas al volver a ejecutar el CPM.

## Cambios

| Unidad | Corrección |
|---|---|
| T-13 | Sincronizadas fechas y HH de las campañas con el T-15; incorporados banco 2.4.3, mapeo 2.4.4 y piloto 4.1.4; corregidas las subventanas PRE-C y recuperación E1. |
| T-17 | Una sola tabla distingue entrega, acta y límite del acta. Actualizadas las holguras H3/H4/H5/H8/H10; se incorporan H7/H12. Eliminada la afirmación de que T-15 no descuenta feriados. |
| Subsanación | Se usa holgura posterior a revisión formal, no distancia entre entrega y cierre del mes. H1/H7/H12 tienen menos de diez días; se exige revisión preliminar, sin acortar los plazos contractuales ni presumir segunda revisión instantánea. |
| Costo de calidad | Añadidas 880 HH ya incluidas en T-15 como evaluación de conformidad física: banco 320, mapeo 240 y piloto 320. No se incrementa el esfuerzo total del proyecto. |
| Totales | Conformidad: 12.016 HH = 4.224 de prevención + 7.792 de evaluación; 35,2 % / 64,8 %; 5,5 % de 220.023 HH. Actualizados también el escenario de fallas y todas las tablas de síntesis. |
| Trazabilidad | R18-03 incorpora banco, mapeo, piloto y referencia V1–V21 del Anexo 4-W. La aceptación final sigue en marcha blanca/H7, no en el banco. |
| Diagramas | Actualizados los tres diagramas de cronograma, con frío y cierre documental E1 en diciembre; conservadas sus fuentes draw.io. |
| Referencias | Títulos oficiales de T-14/T-15 y prefijos reales de las secciones 7.5/7.6 del T-15. |
| Declaración IA | Se conserva la revisión humana registrada. El usuario confirmó posteriormente la revisión de esta actualización y la continuidad de la declaración; se retiró el estado pendiente. |

El mapeo se clasifica como evaluación por su evidencia física y validación por Calidad; su clase E de estimación no determina la categoría de costo de calidad. Las HH no se vuelven a sumar en integración. El escenario de una falla interna y una externa sería 12.219,6 HH solo si las 203,6 HH de retrabajo son adicionales, no una reserva ni frecuencia prevista.

## Verificación

Desde la raíz del repositorio:

```powershell
python SD9_v_nueva/revision/verificar_alineacion_sd7.py
```

La comprobación compara automáticamente 25 filas de campaña con código único y fecha explícita y diez hitos contra la referencia Git fijada; verifica las sumas y proporciones de HH y detecta cifras/citas antiguas. Admite otra referencia SD7 como argumento para futuras sincronizaciones.

Los cuatro documentos se compilan con LuaLaTeX, sin shell escape, en tres pasadas. Los PDF se revisan por extracción de texto, diagnósticos y renders de las tablas/figuras modificadas antes de reemplazar los entregables. Los temporales y registros quedan bajo `tmp/sd9-alineacion-20261026/` en la raíz; no forman parte de la entrega ni deben añadirse al commit.

Resultado final: comprobación automatizada **OK**; cuatro PDF compilados en tres pasadas, sin referencias indefinidas, etiquetas duplicadas ni desbordes. Páginas finales: cuerpo **35**, anexos **21**, T-13 **28**, T-17 **16**. Verificación visual de las tablas de costo, EDT, holguras, campañas y actas, del cronograma y de la declaración IA.

## Pendientes externos que no se ocultan

- Conciliar en SD7 la diferencia entre el CPM publicado y su reproducción, especialmente H4/H5 y el piloto; después regenerar estos calendarios conjuntamente.
- Resolver en SD7 la relación entre fecha objetivo del paso oficial a producción E2, acta H12 calculada y cobertura desde el primer día del mes 21. SD9 no desplaza esa cobertura ni declara una aceptación sin acta.
- Confirmar personas, turnos y nivelación diaria antes de aprobar la línea base. Sincronizar tablas no acredita disponibilidad de recursos.
- Revisión humana de las modificaciones y su consolidación en A-6.

## Límites de reversión

La unidad de cambio comprende los cuatro contenidos LaTeX, los cuatro PDF, el generador y las tres parejas draw.io/PDF de cronograma, más esta nota y su comprobación. Se puede revertir como unidad sin cambiar las portadas, clase, logotipos, otros subdocumentos ni el informe de auditoría previo del SD7. No se publica ni se crea commit automáticamente.
