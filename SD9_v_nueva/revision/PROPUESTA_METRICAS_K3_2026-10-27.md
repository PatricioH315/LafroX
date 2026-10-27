# K3: definición de métricas para ratificación

**Estado: propuesta, no política aprobada ni configuración implantada.** El usuario pidió prepararla el 27-10-2026. SD9 ya publica los límites; falta ratificar su semántica y trasladarla a T-10. No se cambia el canon ni se declara resuelta C03.

## Definiciones propuestas

| Elemento | Duplicación | Acoplamiento eferente |
|---|---|---|
| Límite existente | ≤3 % | ≤20 clases distintas por clase |
| Medida | 100 × líneas físicas duplicadas / líneas físicas analizables | Cardinalidad del conjunto de clases externas distintas referenciadas por cada clase |
| Regla de cómputo | Cada línea duplicada se cuenta una sola vez, aunque participe en varios clones | Referencias repetidas a la misma clase cuentan una vez; excluir la propia clase |
| Alcance | Código de producto PHP, Kotlin y TypeScript, por lenguaje y total | Clases de producto PHP, Kotlin y TypeScript; máximo individual, no promedio |
| Exclusiones propuestas | Dependencias descargadas, código generado y archivos sin código; inventario versionado de exclusiones | Dependencias descargadas y clases generadas no se evalúan como origen; sus tipos sí cuentan cuando los referencia una clase de producto |
| Puerta | G2, antes de la fusión | G2, antes de la fusión |
| Evidencia | Numerador, denominador, rutas y bloques clonados, versión y configuración del detector | Conjunto de dependencias por clase y lista de clases que exceden el límite, versión y configuración del analizador |

Las pruebas se miden separadamente y no se mezclan con el denominador del producto. El umbral se aplica al conjunto analizado; no se transforma silenciosamente en una regla exclusiva sobre código nuevo. Denominador cero se informa como no evaluable, no como 0 % de duplicación.

## Herramientas y calibración pendientes

El Anexo 9.A ya menciona PHPCPD/jscpd y PhpMetrics/detekt/ESLint. Esa lista **no demuestra equivalencia entre sus métricas** ni que una regla cubra TypeScript. Antes de aprobar:

1. Fijar un detector y su configuración por lenguaje: unidad de líneas, tokens mínimos, tamaño mínimo del clon y tratamiento de comentarios/blancos.
2. Precisar tipos de dependencia contados: herencia, interfaces, propiedades, firmas, instanciaciones y referencias estáticas; decidir tratamiento de tipos primitivos y librerías estándar.
3. Elegir o implementar el adaptador de TypeScript que produzca exactamente el conjunto definido; ESLint genérico no acredita por sí solo acoplamiento eferente.
4. Calibrar con fixtures: sin clones, clones solapados, archivo excluido; clase con 20 y con 21 dependencias, referencias repetidas y dependencias a código generado.
5. Conservar informes reproducibles y demostrar que G2 bloquea al superar el límite y al faltar una medición exigible.

## Propagación al ratificar

- C: T-10, SD6, SD9 Tabla 9.4, Anexo 9.A métricas 9A-33/34, Anexo 9.B G2 y T-13.
- B: referencias del paquete 1.5.2 y esfuerzo de implantación del control.
- E: compatibilidad con la cadena de entrega de SD4; sin dispensas de reglas contractuales.

Las tres coberturas C7 se mantienen independientes: ≥70 % lógica de negocio, ≥80 % global y ≥80 % código modificado. No dependen de la aprobación de esta propuesta.
