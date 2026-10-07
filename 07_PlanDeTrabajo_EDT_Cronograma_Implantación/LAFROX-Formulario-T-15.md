# Formulario T-15: Nivelación de recursos

Este formulario presenta la información de planificación que pide el Formulario T-15 de las Bases Administrativas para el Subdocumento 7: el método con que se estiman las horas hombre de cada paquete, la programación sobre la red de dependencias, la ruta crítica y sus holguras, y los frentes de trabajo, con el detalle de los solapamientos de los meses 13 a 15 y 19 a 20. Los paquetes de trabajo son los de la EDT del Formulario T-14. Este formulario no contiene precios ni costos (Art. 50.2).

> **Brecha de información de la fuente:** no se declaran las horas hombre O/M/P por paquete, la tabla resumen (Etapa · HH · personas peak · frentes · meses), las curvas de HH, las personas por período ni el cálculo CPM/PERT con probabilidades. La fuente README registra que esos datos faltan y no se inventan aquí. Sus insumos pendientes son el método base del software, la productividad, la duración de iteraciones y la dotación por rol.

## 1 Método de estimación y de programación

La estimación y la programación siguen el PMBOK y la técnica PERT, de modo que cada duración y cada holgura se puedan reconstruir a partir de valores declarados.

### 1.1 Estimación

El esfuerzo de cada paquete se estima con tres valores en horas hombre (Project Management Institute [PMI], 2017, p. 201): el optimista (O), que corresponde al mejor escenario; el más probable (M), con recursos y productividad realistas; y el pesimista (P), que corresponde al peor escenario. La incertidumbre de cada estimación se representa con una distribución beta, que el PMBOK admite entre las distribuciones para modelar la incertidumbre (PMI, 2017, p. 432). Con ella, la técnica PERT calcula el valor esperado y la desviación (Malcolm et al., 1959):

$$T_E = \frac{O + 4M + P}{6} \qquad\qquad \sigma = \frac{P - O}{6}$$

La p. 201 del PMBOK presenta también la distribución triangular, $(O + M + P)/3$. Se usa la beta porque pondera más el valor más probable, que se funda en los requerimientos y cantidades de cada paquete.

Las bases de cada estimación se declaran por tipo de paquete. Los módulos y las integraciones se estiman con los requerimientos del Formulario T-12 asignados al paquete; la infraestructura, con las cantidades del Formulario T-11; la implantación y la capacitación, con las personas y rutas del caso y la dotación del Formulario T-18, sección 2.6; y la operación, con los horarios de cobertura de los paquetes 8.1.1 y 8.1.2 y la periodicidad de los informes. Los paquetes de la fase 8 son de esfuerzo continuo: su estimación es mensual y se multiplica por los 36 meses de operación.

### 1.2 Programación

La duración de cada paquete se obtiene de su esfuerzo esperado y de la dotación asignada. Las dependencias entre paquetes están en el Anexo 7.B del Subdocumento 7, y sobre esa red se aplica el método de la ruta crítica (PMI, 2017, pp. 210–211): una pasada hacia adelante da el inicio y el fin tempranos; una pasada hacia atrás, desde los meses fijos del Art. 17°, da el inicio y el fin tardíos; y su diferencia es la holgura total y libre de cada paquete. Los hitos del Formulario E-25 son restricciones de fecha fija: un camino que no llega a su hito tiene holgura negativa y obliga a replanificar.

La probabilidad de cumplir H5, H7, H10 y H12 se calcula sumando los $T_E$ y las varianzas $\sigma^2$ de los paquetes de la ruta crítica que llega a cada hito, con la aproximación normal de PERT. La nivelación ajusta el inicio de los paquetes con holgura para que ningún rol supere su dotación disponible (PMI, 2017, pp. 211–212); los paquetes de la ruta crítica no se mueven.

## 2 Ruta crítica y holguras

La cadena crítica nace en las interfaces del sistema de gestión sin documentación (Caso 02, sección 17.5): 1.2.3 Especificación de las interfaces, 3.3.2 Integración con el ERP, 3.4 Módulos de la Etapa 1, 3.8.1 Pruebas de integración (H4, mes 10), 3.8.2 a 3.8.6 Pruebas de certificación, 3.8.7 Certificación (H5, mes 12), 4.2.1 Marcha blanca (H6, mes 13) y 4.2.3 Paso a producción (H7, mes 16). La figura siguiente la presenta junto con los caminos casi críticos.

**Figura T-15.1 — Ruta crítica identificada y caminos casi críticos de la implementación.** Fuente: elaboración propia a partir del Anexo 7.B del Subdocumento 7 y de los períodos del Formulario T-14.

Descripción textual: cronograma de los meses 1 a 21, con los hitos H1 (mes 2), H2 (4), H3 (6), H4 (10), H5 (12), H6 (13), H8 (14), H7 (16), H9 (17), H10 (18), H11 (19) y H12 (21). Destaca en rojo la cadena crítica: 1.2.3 Interfaces sin documentación (meses 1–4); 3.3.2 Integración con el ERP y 3.4 Módulos de la Etapa 1 (meses 5–10, hasta H4); 3.8.1 a 3.8.7 Pruebas y certificación (meses 10–12, H4 a H5); 4.2.1 Marcha blanca de la Etapa 1 (meses 13–15); y 4.2.3 Paso a producción (H7, mes 16). Las conexiones indican la precedencia entre tramos. También muestra cuatro caminos casi críticos: sala técnica y sitios (2.3.1 durante meses 2–4 y 5.1.2/6.1–6.6 hasta H3); planificador (1.2.2, luego 3.4.7 M4 Rutas y R18-16 en meses 13–15); acuerdos con terceros (5.4.1 y 5.4.2 en meses 5–12, luego ola 3 en meses 13–15); cadenas del canal moderno (3.6.5 en meses 13–18 y 3.6.6 en meses 19–21). Las ventanas de marcha blanca E1 y E2 se señalan en los meses 13–15 y 19–20.

Cada tramo de la cadena termina en el mes del hito fijo que lo sigue (mes 4 para el H2, mes 10 para el H4 y mes 12 para el H5), de modo que, a la resolución mensual del cronograma, su holgura es cero. Los caminos casi críticos son la sala técnica (2.3.1, 5.1.2, 6.1, 6.3 y 6.6.3), que llega al H3 del mes 6; la captura de las reglas de ruteo del planificador (1.2.2 y 3.4.7 M4 Rutas), antes de su jubilación; los acuerdos con los diez transportistas y con el sindicato (5.4.1 y 5.4.2), antes de la ola de reparto; y la certificación del intercambio electrónico con las cadenas (3.6.5 y 3.6.6), antes del mes 21.

La holgura se gestiona en las instancias de gobierno de la EDT: el avance de la ruta crítica y de los caminos casi críticos se revisa en la reunión semanal y en el Comité de Proyecto quincenal (paquetes 1.3.5 y 1.8.3); toda desviación que comprometa un hito se escala al Comité Ejecutivo con su análisis de impacto (paquetes 1.4.3 y 1.8.2); y el informe mensual con valor ganado avisa toda desviación mayor al 10 % con su plan dentro de cinco días hábiles (paquete 1.8.6).

## 3 Frentes de trabajo y solapamientos

Un frente de trabajo es un equipo con un responsable y un conjunto de cuentas de control que avanza en paralelo con los demás. La tabla define los frentes a partir de la EDT del Formulario T-14 y de los responsables de su diccionario.

**Tabla T-15.1 — Frentes de trabajo.** Fuente: elaboración propia a partir del Formulario T-14.

| Frente | Responsable | Cuentas de control | Meses activos |
|---|---|---|---|
| F1 Dirección, gobierno y cumplimiento | Jefe de Proyecto | 1.1 a 1.4, 1.6 a 1.9, 5.4.1 a 5.4.3, 8.4, 9 | 1 a 56 |
| F2 Arquitectura, seguridad y datos | Arquitecto de Solución, con Seguridad y Datos | 2.1 a 2.6, 3.3, 3.7, 3.11 | 1 a 21 |
| F3 Construcción de la Etapa 1 | Líder de Desarrollo | 3.4, 3.6.1 a 3.6.4, 3.10.1 a 3.10.3 | 1 a 15 |
| F4 Construcción de la Etapa 2 | Líder de Desarrollo | 3.5, 3.6.5, 3.6.6, 3.10.4 | 13 a 20 |
| F5 Plataforma e infraestructura | Líder de Operación / SRE | 3.1, 3.2, 5.1 a 5.3, 6.1 a 6.6 | 1 a 15 |
| F6 Calidad y pruebas | Líder de Calidad | 1.5, 3.8, 3.9 | 1 a 21 |
| F7 Implantación y gestión del cambio | Líder de Implantación y Gestión del Cambio | 4.1 a 4.3, 7.1 a 7.3 | 9 a 21 |
| F8 Operación y soporte | Líder de Operación / SRE | 8.1 a 8.3, 8.5 | 21 a 56 |

Los frentes se sincronizan en los hitos del Formulario E-25 y en los comités del Art. 71°, cuyas actas registran los acuerdos entre frentes (paquetes 1.8.2 a 1.8.5). La figura presenta su ventana de actividad entre los meses 1 y 21.

**Figura T-15.2 — Frentes de trabajo de los meses 1 a 21 y solapamientos del Art. 17.2.** Fuente: elaboración propia a partir de la Tabla T-15.1 y del Formulario T-14.

Descripción textual: carriles temporales de los ocho frentes, con meses 1 a 21, hitos E-25 H1–H12 y franjas de solapamiento en los meses 13–15 y 19–20. F1 se extiende hasta el mes 56 (sus cuentas mostradas incluyen 8.4 y 9); F2 va de 1 a 21; F3 y F5, de 1 a 15; F4, de 13 a 20; F6, de 1 a 21; F7, de 9 a 21; y F8 comienza en el mes 21 y continúa hasta el 56. Las cuentas y responsables de los frentes se detallan en la tabla precedente.

En los meses 13 a 15 trabajan a la vez F7, en la marcha blanca de la Etapa 1; F3, en las correcciones de esa marcha blanca; F4, en el desarrollo de la Etapa 2; F6, en las pruebas de ambas etapas; y F1 y F2. F3 y F4 dependen del mismo rol, el Líder de Desarrollo, y por eso son equipos distintos: el equipo que atiende la marcha blanca no puede ser el que desarrolla la Etapa 2 (Art. 17.2, punto 1). En los meses 19 y 20 trabajan F7, en la marcha blanca de la Etapa 2; F4, en sus correcciones; F6; y el soporte de la Etapa 1 en producción.

## Referencias

Las fuentes de método citadas en este formulario son las siguientes.

- Malcolm, D. G., Roseboom, J. H., Clark, C. E., & Fazar, W. (1959). Application of a technique for research and development program evaluation. *Operations Research, 7*(5), 646–669.
- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.). Project Management Institute.
