# Procedimiento del análisis cualitativo y cuantitativo de riesgos de LafroX

Este documento explica cómo se construyó el análisis de los 34 riesgos R-001 a R-034 y cómo se relaciona cada etapa con el archivo [LafroX_analisis_34_riesgos.xlsx](./LafroX_analisis_34_riesgos.xlsx).

El análisis cualitativo permite priorizar los riesgos. El cuantitativo estima el trabajo adicional, su costo y la demora de la actividad afectada si se materializan. Los resultados numéricos son estimaciones para revisión del equipo, no registros de costos reales ni frecuencias históricas comprobadas.

## 1. Antecedentes y alcance del trabajo

### Paso 1. Establecer qué riesgos se analizarían

Se revisó el archivo `LafroX_registro_riesgos_R001-R039 .xlsm`. Aunque su nombre menciona R001–R039, el contenido entregado tenía 34 registros, desde R-001 hasta R-034. Se trabajó con esos 34, sin crear los cinco riesgos restantes.

Los títulos, categorías, descripciones y explicaciones de responsabilidad se conservaron en la hoja **Registro original**, rango **A5:E39**. La fila 5 contiene los encabezados y las filas 6 a 39 contienen los riesgos.

El ID es la clave que conecta las hojas. Por ejemplo, R-001 corresponde al mismo riesgo en el registro, el análisis cualitativo, el cuantitativo y la priorización del resumen. Las fórmulas de consulta usan el ID para buscar el registro correspondiente.

Se conservaron las observaciones y vacíos de origen: R-001 y R-022 mantienen «revisar», R-029 mantiene su redacción y la columna de competencia de R-030 y R-031 permanece vacía. Los roles y valoraciones añadidos al análisis no se presentan como parte del registro original.

### Paso 2. Separar método, evidencia y supuestos

Se distinguieron tres tipos de información:

| Tipo | Qué aporta | Dónde se documenta en el Excel |
|---|---|---|
| Método | Escalas, zonas de exposición, valor monetario esperado y estimación de tres valores. | **Parámetros**, notas metodológicas de las filas 32 a 51. |
| Evidencia del proyecto | Requisitos, condiciones pendientes, controles ofertados, responsabilidades y calendario. | **Parámetros!A57:F91**, con una referencia por cada uno de los 34 riesgos. |
| Supuestos del análisis | Probabilidades, horas adicionales, tarifas, episodios, demoras y niveles propuestos de alcance/calidad. | Entradas editables y justificaciones de **Cualitativo**, **Cuantitativo** y **Parámetros**. |

La metodología se apoyó en el PDF `FEP04.26 - Gestión de los Riesgos en Proyectos TIC 2.pdf`: páginas físicas 6–8 para elementos, escalas y zonas; 42–48 para los análisis y el valor esperado; y 52–54 para tres valores y sensibilidad. La numeración física del archivo puede diferir de la impresa en las diapositivas.

La plantilla `TFEP03.26_Plantillas (1).docx` se utilizó para organizar el registro, el fundamento de la probabilidad, la composición del impacto, el registro cuantificado y la priorización. Sus cifras de ejemplo, incluidos los $710 millones de costos directos, no se trasladaron a LafroX. Las tablas individuales de riesgos utilizadas incluyen los 34 registros.

Se excluyeron el subdocumento 8 y las valoraciones derivadas de él. La evidencia específica utilizada para cada riesgo puede localizarse por documento y página en la tabla de fuentes del Excel. Esa evidencia respalda el contexto del riesgo; no demuestra por sí sola los porcentajes ni las horas propuestos.

### Paso 3. Delimitar qué consecuencias se valorarían

Se estimó trabajo adicional atribuible a LafroX: preparar información, adaptar una integración, repetir pruebas, coordinar una validación o atender un incidente extraordinario.

No se sumaron automáticamente pérdidas del cliente, como mercadería dañada, vehículos robados o ventas no realizadas. Tampoco se incluyeron multas, compras o servicios externos sin alcance y costo sustentados.

Esta delimitación se explica por riesgo en **Cuantitativo!AE:AJ**. Es necesaria para interpretar correctamente el resultado: la cifra representa el costo del trabajo incremental modelado, no todos los daños posibles del evento.

## 2. Procedimiento del análisis cualitativo

### Paso 4. Leer la causa, el evento y el efecto de cada riesgo

Se revisó qué condición origina el riesgo, qué podría ocurrir y qué objetivo del proyecto se vería afectado. Se mantuvo su clasificación RBS original.

En la hoja **Cualitativo**:

- **A–D** identifican el riesgo y recuperan su nombre, enunciado y RBS.
- **E** propone un rol responsable de vigilarlo y coordinar su tratamiento. No constituye un nombramiento aprobado.

La valoración considera los controles ya ofertados en los antecedentes. No se modelaron nuevas acciones de mitigación ni reducciones residuales de probabilidad o impacto.

### Paso 5. Definir la ventana de ocurrencia y los atributos de seguimiento

Se ubicó cada riesgo en el período en que podría afectar al proyecto. Para los riesgos de operación se adoptaron los meses 21 a 56, equivalentes a 36 meses, conforme al SD7: página física 6 para el calendario de 56 meses y página 23 para la operación formal.

En **Cualitativo!T:Y** se incorporaron:

| Columna | Atributo | Uso |
|---|---|---|
| T | Urgencia | Indica cuándo debe atenderse la condición. |
| U | Ventana de ocurrencia | Delimita el período al que corresponde la probabilidad. |
| V | Disparador observable | Señal que permite detectar que la condición requiere atención. |
| W | Controlabilidad | Distingue qué depende de LafroX, del cliente o de un tercero. |
| X | Detectabilidad | Explica si el problema puede advertirse antes de afectar la actividad. |
| Y | Conectividad / IDs | Identifica riesgos relacionados que requieren revisión conjunta. |

Estos atributos ayudan a interpretar y gestionar la prioridad. No se suman como puntos adicionales a la fórmula de exposición.

### Paso 6. Estimar y clasificar la probabilidad

Se propuso una probabilidad por riesgo considerando condiciones documentadas pendientes, dependencia de terceros, controles existentes y duración de la exposición. No se disponía de una serie histórica que permitiera calcular estadísticamente cada porcentaje.

La probabilidad se introduce una sola vez, en **Cuantitativo!C6:C39**. La hoja **Cualitativo** la recupera en la columna **F**, la clasifica en **G** y obtiene su factor de exposición en **H**.

| Nivel | Clasificación | Probabilidad de ocurrencia | Factor P adoptado |
|---|---|---|---:|
| 1 | Muy baja | Mayor que 0% y hasta 10%. | 0,10 |
| 2 | Baja | Mayor que 10% y hasta 30%. | 0,30 |
| 3 | Media | Mayor que 30% y hasta 50%. | 0,50 |
| 4 | Alta | Mayor que 50% y hasta 70%. | 0,70 |
| 5 | Muy alta | Mayor que 70% y hasta 100%. | 0,90 |

Los intervalos enteros del material se extendieron a porcentajes fraccionarios con estos límites explícitos. Una probabilidad de 0% queda fuera de los cinco niveles y recibe nivel y factor cero en el modelo.

Los factores son una convención adoptada para construir la matriz. **Una probabilidad de 35% se convierte en nivel 3 y factor 0,50; esto no cambia su probabilidad real estimada a 50%.** El cálculo monetario sigue utilizando 35%.

El fundamento individual está en **Cualitativo!Z** y su referencia documental en **AA**.

### Paso 7. Valorar el impacto sobre costo, plazo y alcance/calidad

Se evaluaron tres dimensiones de impacto. Cada una utiliza un nivel de 1 a 5.

**a) Impacto en costo.** Se calcula el impacto condicional acumulado de **Cuantitativo!Y** como proporción del monto contractual, que debe introducirse en **Parámetros!B6**. El cociente aparece en **Cualitativo!I** y su nivel en **J**.

| Nivel | Impacto monetario como porcentaje del contrato |
|---|---|
| 1 | Menor que 0,5%. |
| 2 | Desde 0,5% y menor que 1%. |
| 3 | Desde 1% y menor que 2%. |
| 4 | Desde 2% y hasta 5%. |
| 5 | Mayor que 5%. |

Como no se identificó un monto contractual respaldado en los antecedentes técnicos, **Parámetros!B6 se dejó vacío**. Por eso aparece «Pendiente» en el cociente y 0 en el nivel de costo. Ese cero significa **dimensión no evaluable todavía**, no ausencia de impacto monetario.

**b) Impacto en plazo.** Se toma la demora central por episodio de **Cuantitativo!AD** y se recupera en **Cualitativo!K**. El nivel se calcula en **L**:

| Nivel | Demora en días calendario |
|---|---|
| 1 | Menor que 2 días. |
| 2 | Desde 2 y menor que 7 días. |
| 3 | Desde 7 y menor que 21 días. |
| 4 | Desde 21 y hasta 42 días. |
| 5 | Mayor que 42 días. |

Se adoptaron 7 días por semana. En los límites compartidos de 7 y 21 días se utilizó el nivel superior para evitar ambigüedades.

**c) Impacto en alcance/calidad.** Se propuso el nivel según el efecto sobre la funcionalidad y la evidencia de aceptación comprometidas: desde un efecto menor en funciones secundarias hasta uno muy significativo en capacidades comprometidas. El nivel editable está en **Cualitativo!M** y su justificación específica en **N**.

### Paso 8. Seleccionar el impacto global

Se tomó el mayor nivel entre las dimensiones evaluables:

```text
Impacto global = máximo(nivel costo, nivel plazo, nivel alcance/calidad)
```

El resultado aparece en **Cualitativo!O**. Se usa el máximo para conservar visible la dimensión más severa, en lugar de diluirla en un promedio.

Después se convierte el nivel global en un factor de impacto, ubicado en **P**:

| Nivel global | Factor I adoptado |
|---:|---:|
| 1 | 0,05 |
| 2 | 0,10 |
| 3 | 0,20 |
| 4 | 0,40 |
| 5 | 0,80 |

Estos factores también son una convención declarada del análisis. Mientras falte el monto contractual, el máximo se obtiene de plazo y alcance/calidad, y la clasificación queda provisional. Incorporar la dimensión de costo podría elevarla.

### Paso 9. Calcular la exposición y asignar una zona

En **Cualitativo!Q** se multiplican los dos factores:

```text
Exposición cualitativa = factor P × factor I
```

La zona se determina en **R** con los umbrales del curso:

| Zona | Exposición | Orientación de actuación del método |
|---|---|---|
| Baja | Menor que 0,08. | Observación y aceptación pasiva. |
| Media | Desde 0,08 y menor que 0,20. | Aceptación activa, disparador y contingencia. |
| Alta | Desde 0,20 y menor que 0,40. | Requiere planificar mitigación con costo y plazo. |
| Crítica | Desde 0,40. | Exige revisar el diseño, alcance o decisión de asumir el riesgo. |

La zona señala la necesidad de tratamiento; el archivo no incorpora todavía un plan de respuestas ni calcula exposición residual.

**La exposición es un índice de prioridad.** Un resultado de 0,20 no significa que se perderá el 20% del contrato ni que exista una probabilidad de ocurrencia de 20%.

### Paso 10. Ordenar los riesgos

La prioridad se calcula en **Cualitativo!S** y se presenta para los 34 riesgos en **Resumen!A22:H56**.

Se adoptó esta regla:

1. Mayor exposición cualitativa primero.
2. A igual exposición, mayor valor monetario esperado primero.
3. Si ambos coinciden, ID ascendente.

El VME utilizado para desempatar se recupera en **Cualitativo!AB**. La regla es una elección declarada del análisis; no se atribuye a un enunciado de desempate que no fue entregado.

## 3. Procedimiento del análisis cuantitativo

### Paso 11. Describir el trabajo adicional necesario

Para cada riesgo se definió qué tendría que hacer LafroX si se materializa, evitando incluir nuevamente el trabajo ordinario ya previsto en el proyecto.

La explicación está en **Cuantitativo!AE**. Por ejemplo, un problema de telemetría puede requerir revisar una alternativa autorizada, adaptar el conector y repetir sus pruebas.

Aunque el material propone concentrar el esfuerzo cuantitativo en riesgos priorizados, se cuantificaron **los 34 riesgos** para cumplir la cobertura completa solicitada.

### Paso 12. Seleccionar perfiles y estimar horas con tres escenarios

Se modeló el trabajo de dos perfiles por riesgo. Cada perfil tiene horas por episodio para tres escenarios:

- **O, optimista:** resolución acotada y pocas iteraciones.
- **M, más probable:** ronda adicional descrita en la justificación del riesgo.
- **P, pesimista:** varias iteraciones o resolución más compleja.

En el Excel:

| Columnas | Contenido |
|---|---|
| E | Primer perfil. |
| F, G, H | Horas optimistas, más probables y pesimistas del primer perfil. |
| K | Segundo perfil. |
| L, M, N | Horas optimistas, más probables y pesimistas del segundo perfil. |

Las HH representan horas-persona: dos personas trabajando cuatro horas cada una consumen ocho HH. Para explicar esfuerzos en jornadas se utilizó una referencia de ocho HH por jornada; ello no transforma automáticamente el esfuerzo en duración calendario.

La elección de dos perfiles es una simplificación del modelo. Si se identifica un tercer perfil necesario, debe ampliarse la estructura y sus fórmulas para no omitir su costo.

### Paso 13. Calcular las horas centrales mediante PERT

Se utilizó el promedio ponderado:

```text
Valor central = (optimista + 4 × más probable + pesimista) / 6
```

El escenario más probable recibe mayor peso, pero los extremos también influyen. El resultado está en **J** para el primer perfil y **P** para el segundo.

El valor central puede diferir de M. Los escenarios propuestos no son percentiles estadísticos ni provienen de una distribución calibrada o de una entrevista formal a expertos.

### Paso 14. Convertir las horas en costo

Se multiplicaron las horas de cada perfil por su tarifa. Los perfiles y tarifas se encuentran en **Parámetros!A10:E19**; las tarifas editables están en **C11:C19**. La hoja cuantitativa las consulta automáticamente en **I** y **O**.

| Perfil | Función | Tarifa estimada CLP/HH |
|---|---|---:|
| INT | Integración | $22.000 |
| QA | Pruebas | $16.000 |
| DAT | Datos y migración | $20.000 |
| FUN | Análisis funcional | $18.000 |
| IMP | Implantación/capacitación | $18.000 |
| SRE | Operación/continuidad | $24.000 |
| ARQ | Arquitectura | $28.000 |
| SEG | Seguridad | $26.000 |
| JP | Jefatura de proyecto | $26.000 |

No se encontraron tarifas documentadas para estos perfiles. Se propuso una estructura relativa de costos internos tomando integración como ancla analítica y diferenciando especialización y responsabilidad. **No son cotizaciones ni resultados de un estudio de mercado.** Deben sustituirse por costos internos comprobados antes de comprometer una reserva.

### Paso 15. Incorporar desembolsos adicionales cuando corresponda

Las columnas **Q, R y S** contienen gastos optimistas, más probables y pesimistas distintos de las HH ya contabilizadas. La columna **T** muestra su promedio ponderado.

En la versión elaborada, esos gastos son cero porque no se identificaron desembolsos incrementales sustentados dentro del alcance delimitado. Su explicación está en **AJ**. Si se confirman viajes, servicios externos o repuestos necesarios, deben estimarse e incorporarse; el cero actual no demuestra que sean gratuitos.

### Paso 16. Obtener el costo por episodio

Para cada escenario se calculó:

```text
Costo por episodio = HH del perfil 1 × tarifa 1
                   + HH del perfil 2 × tarifa 2
                   + gastos adicionales
```

En las columnas **U, V y W** aparecen los costos O, M y P. En **X** se calcula el costo central:

```text
X = (U + 4 × V + W) / 6
```

Con las mismas tarifas para los tres escenarios, este resultado también equivale a sumar el costo de las horas centrales de ambos perfiles y los gastos centrales. Las fórmulas conservan la precisión interna y los importes se muestran redondeados a pesos enteros.

### Paso 17. Considerar la repetición del riesgo

La columna **D** aproxima la cantidad media de episodios durante la ventana de exposición, condicionada a que ocurra al menos uno. Su justificación está en **AG**.

Para una condición puntual se utilizó un episodio. Para algunos incidentes operativos se propusieron varios episodios durante los 36 meses completos, sin multiplicarlos nuevamente por meses, sitios o dispositivos.

El impacto acumulado condicionado a la ocurrencia se calcula en **Y**:

```text
Impacto condicional acumulado = costo central por episodio × episodios
Y = X × D
```

Esta representación supone que X es un costo medio representativo de los episodios incluidos. Si los episodios tienen severidades o costos muy distintos, corresponde reestimar el costo acumulado o ampliar el modelo. Los conteos actuales son supuestos, no frecuencias observadas.

### Paso 18. Calcular el valor monetario esperado

La columna **Z** combina probabilidad e impacto:

```text
VME = probabilidad de al menos un episodio × impacto condicional acumulado
Z = C × Y
```

Se utiliza la probabilidad porcentual de C, no el factor de la matriz cualitativa. El VME expresa el costo medio modelado del riesgo al considerar la posibilidad de que no ocurra; no es una predicción de la factura exacta de un incidente.

### Paso 19. Estimar la demora de la actividad afectada

Las columnas **AA, AB y AC** contienen demoras O, M y P en días calendario por episodio. **AD** calcula su promedio ponderado. El fundamento está en **AF**.

La demora puede incluir espera de un proveedor, disponibilidad de personas o aprobación del cliente. Por eso no se obtiene simplemente dividiendo las HH por ocho.

No se multiplicó la demora por los episodios ni se sumaron las demoras de los 34 riesgos para declarar un atraso total. Esa conclusión requiere modelar concurrencia, secuencia, recursos, holguras y ruta crítica del cronograma.

### Paso 20. Revisar exclusiones y costos compartidos

Se delimitaron los costos de causas relacionadas para evitar valorar dos veces el mismo trabajo:

- **AH** explica exclusiones y límites del impacto.
- **AI** advierte posibles costos compartidos con otros riesgos.
- **AK** identifica el carácter estimado de las entradas y remite a su evidencia contextual.

Por ejemplo, R-020 cubre fallas del enlace. R-009, R-010 y R-011 se acotan a fallas de sus contrapartes con enlace operativo. Una misma atención de incidente no debe imputarse simultáneamente a ambas causas.

La hoja documenta estas delimitaciones, pero **no detecta automáticamente que dos incidentes registrados en la realidad sean el mismo**. El equipo debe respetar la imputación por causa y revisar los supuestos compartidos.

### Paso 21. Agregar los valores esperados

La suma de **Cuantitativo!Z6:Z39** alimenta **Resumen!B7**. La versión explicada en este documento muestra:

```text
Contingencia estimada = $21.759.833 CLP
```

La suma de los impactos condicionales aparece separada en **Resumen!B8** y asciende a **$51.124.333 CLP**. Es una suma de impactos centrales condicionados por riesgo; no es una reserva recomendada ni un peor caso estadístico del proyecto.

La suma de valores esperados no exige independencia entre los eventos para ser matemáticamente válida, pero sí una definición coherente de los costos, sin duplicaciones. Para estimar un percentil de suficiencia o un escenario conjunto sería necesario modelar también las dependencias y la distribución de resultados.

Los costos directos de **Parámetros!B7** también quedaron pendientes. Por ello, **Resumen!B9** no calcula todavía la contingencia como porcentaje de costos directos.

## 4. Ejemplo completo: R-001, acceso a telemetría

R-001 está en la fila 6 de **Cualitativo** y **Cuantitativo**. El registro describe la posibilidad de que el proveedor no habilite acceso a posición, velocidad o kilometraje en las condiciones necesarias para M12.

### 4.1 Fundamento y probabilidad

La consulta V-15 mantiene por confirmar las condiciones contractuales de acceso a la telemetría: SD3-Anexos, página física 149. Esa referencia aparece en **Parámetros!A58:F58**.

Se propuso **35%**, almacenado en **Cuantitativo!C6**, por la dependencia externa pendiente y considerando el adaptador de solo lectura previsto. El porcentaje no figura en esa página del proyecto; es un supuesto razonado del análisis.

### 4.2 Horas y costos

| Elemento | Optimista | Más probable | Pesimista | Ubicación |
|---|---:|---:|---:|---|
| Horas de integración | 24 | 64 | 160 | F6:H6 |
| Horas de QA | 16 | 32 | 64 | L6:N6 |
| Gastos adicionales | $0 | $0 | $0 | Q6:S6 |
| Costo por episodio | $784.000 | $1.920.000 | $4.544.000 | U6:W6 |

Con tarifas de $22.000/HH para integración y $16.000/HH para QA:

```text
Costo optimista = 24 × $22.000 + 16 × $16.000 = $784.000
Costo más probable = 64 × $22.000 + 32 × $16.000 = $1.920.000
Costo pesimista = 160 × $22.000 + 64 × $16.000 = $4.544.000

Costo central = ($784.000 + 4 × $1.920.000 + $4.544.000) / 6
              = $2.168.000
```

Las horas centrales son aproximadamente **73,33 HH de integración** y **34,67 HH de QA**, visibles en **J6** y **P6**. No deben confundirse con las 64 y 32 HH del escenario M.

Se consideró un episodio en **D6**:

```text
Impacto condicional acumulado, Y6 = $2.168.000 × 1 = $2.168.000
Valor monetario esperado, Z6 = 0,35 × $2.168.000 = $758.800
```

### 4.3 Demora y clasificación cualitativa

Se estimaron 3, 10 y 28 días por episodio en **AA6:AC6**:

```text
Demora central, AD6 = (3 + 4 × 10 + 28) / 6 = 11,83 días
```

La relación con **Cualitativo** es la siguiente:

| Resultado | Valor | Celda |
|---|---:|---|
| Probabilidad estimada | 35% | F6 |
| Nivel de probabilidad | 3 | G6 |
| Factor P | 0,50 | H6 |
| Nivel de costo relativo | 0: pendiente por falta de monto contractual | J6 |
| Demora central | 11,83 días | K6 |
| Nivel de plazo | 3 | L6 |
| Nivel de alcance/calidad | 4 | M6 |
| Impacto global | Máximo de los niveles: 4 | O6 |
| Factor I | 0,40 | P6 |
| Exposición | 0,50 × 0,40 = 0,20 | Q6 |
| Zona | Alta | R6 |
| Prioridad en la versión elaborada | 9 | S6 |

El nivel 4 de alcance/calidad se fundamentó en que, sin acceso utilizable, no puede verificarse M12 con la cobertura comprometida hasta acordar y probar una alternativa.

Los **0,20 de exposición** sirven para priorizar. Los **$758.800 de VME** sirven para contribuir a la contingencia. Son resultados distintos con finalidades diferentes.

## 5. Cómo se conectan las hojas del Excel

| Hoja | Función | Relaciones principales |
|---|---|---|
| Registro original | Conserva los 34 registros recibidos. | Entrega identificación y texto a las hojas de análisis mediante el ID. |
| Parámetros | Centraliza tarifas, factores, bases económicas pendientes, método y evidencia. | Las tarifas alimentan Cuantitativo; los factores y el monto contractual alimentan Cualitativo. |
| Cuantitativo | Contiene supuestos de probabilidad, esfuerzo, recurrencia y demora; calcula costos y VME. | Envía probabilidad, impacto monetario, demora y VME a Cualitativo y resultados monetarios a Resumen. |
| Cualitativo | Clasifica P e impactos y calcula exposición, zona y prioridad. | Alimenta la matriz, las cantidades por zona y el orden de Resumen. |
| Resumen | Presenta la contingencia, la distribución por zonas y los 34 riesgos priorizados. | Lee los resultados de los análisis sin introducir nuevos supuestos de esfuerzo. |

Conceptualmente se identifica y se valora el riesgo antes de dimensionar su costo. En la implementación se integraron ambos análisis: **Cuantitativo** es el lugar único donde se edita la probabilidad y se calcula la demora que usa **Cualitativo**. Esta alimentación no es una circularidad: los cálculos cuantitativos no dependen de su propia zona ni de su prioridad cualitativa.

Con los supuestos de la versión elaborada, el resumen presenta **1 riesgo crítico, 10 altos, 19 medios y 4 bajos**. La matriz cuenta riesgos según nivel de probabilidad e impacto global. La distribución puede cambiar al revisar entradas o completar el monto contractual.

## 6. Uso y actualización del archivo

1. **Buscar el ID** en Registro original y revisar que el evento siga vigente y conserve su alcance.
2. **Consultar la evidencia** en Parámetros!A57:F91 y revisar las condiciones o controles que hayan cambiado.
3. **Actualizar la probabilidad** en Cuantitativo!C, siempre para la ventana completa definida en Cualitativo!U.
4. **Actualizar episodios, perfiles, HH, gastos y demoras** en las entradas amarillas de Cuantitativo.
5. **Actualizar tarifas** en Parámetros!C11:C19 cuando se disponga de costos internos comprobados. Las columnas I y O las recuperan por perfil.
6. **Revisar alcance/calidad** en Cualitativo!M y mantener coherente su explicación en N.
7. **Completar las bases económicas** en Parámetros!B6 y B7 solo con información respaldada: monto contractual y costos directos, respectivamente.
8. **Revisar los textos de fundamento.** Las justificaciones describen los supuestos iniciales y no se reescriben automáticamente al editar un número.
9. **Revisar exclusiones y costos compartidos** antes de interpretar el nuevo total o imputar un incidente a varios riesgos.
10. **Comprobar Resumen**: deben seguir apareciendo los 34 IDs, sin repeticiones, y el orden debe ser coherente con exposición, VME e ID.

No se deben reemplazar por valores las celdas que contienen fórmulas. Las entradas y resultados están diferenciados mediante color y encabezados.

Los factores de exposición se consultan desde Parámetros y pueden actualizarse allí. **Los límites de clasificación de probabilidad, plazo, costo y zona están codificados en las fórmulas:** cambiar únicamente el texto o los intervalos de la tabla de parámetros no cambia esos límites. Una modificación metodológica exige ajustar y comprobar también las fórmulas afectadas.

Las fórmulas de consulta y priorización se construyeron para los 34 registros entregados. Agregar un nuevo riesgo requiere ampliar los rangos, tablas, controles y referencias; no basta con escribir una fila adicional.

## 7. Verificaciones realizadas y límites del resultado

Se verificaron:

- Cobertura exacta de R-001 a R-034 en las hojas de análisis y en la priorización completa.
- Conservación del contenido original, incluidos sus vacíos.
- Cálculo independiente de costos y valores esperados de los 34 riesgos.
- Suma de cantidades por zona igual a 34 y prioridades únicas de 1 a 34.
- Ausencia de errores de fórmula detectados en el archivo exportado.
- Treinta comprobaciones de modificación y límites: cambios de probabilidad, horas y tarifas; límites de clasificación; tratamiento de un esfuerzo faltante; y umbrales de zona. Se restauraron las entradas originales después de las pruebas.
- Revisión visual de las cinco hojas y de vistas de identificación, resultados, fundamentos y evidencia.

Los recálculos se comprobaron en el motor utilizado para generar el archivo y se inspeccionaron los resultados guardados en el XLSX. No se realizó una comprobación interactiva de todas las fórmulas en la aplicación Microsoft Excel.

El resultado sigue sujeto a la calidad de los supuestos. No se ejecutó una simulación Monte Carlo, no se calculó P80, no se estimó atraso global de la red del proyecto y no se modelaron respuestas adicionales ni reserva residual. La contingencia calculada representa el valor esperado del trabajo incremental delimitado, pendiente de revisión del equipo y de sustitución de supuestos por datos comprobados cuando existan.
