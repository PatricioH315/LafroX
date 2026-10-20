# Guion: diapositivas de calidad (mini v5) contrastadas con el Subdocumento 9

Duración estimada: unos 4 minutos. Cada bloque indica qué decir y en qué parte del SD9 se respalda.

---

## 24 · Gantt de implementación (fila Calidad) · ~30 s

**Decir:**
"En el cronograma, la calidad tiene su propia fila. Hay dos certificaciones: en los meses 9–10, antes de la marcha blanca de la Etapa 1, y en los meses 16–17, antes de la de la Etapa 2. Desde el mes 13 corren las restauraciones de respaldo, que en la Operación pasan a ser mensuales."

**Respaldo SD9:** Figura 9.9 y su tabla. Cuenta 3.8, meses 9 y 10, 2.240 HH. Cuenta 3.9, meses 16 y 17, 1.600 HH. Restauraciones previas en los meses 13 a 20, 128 HH, y luego restauración mensual en la Operación.
**Estado:** ✅ Calza.

---

## 28 · Normas y leyes · ~40 s

**Decir:**
"Las Bases, en el Art. 4.3, dicen que nombrar un estándar sin evidencia vale cero. Por eso cada norma va con la forma en que la acreditamos:
- ISO 25010, con ocho características y un umbral para cada una.
- ISO 25012, con datos medidos y conciliados.
- ISO 29119, con un proceso de prueba en tres niveles.
- PMBOK, que planifica, gestiona y controla la calidad, con su costo.
- WCAG, con herramienta automática y revisión manual.
- OWASP, con análisis estático y dinámico.

ISO 9001 aporta el marco de auditoría y CMMI nivel 3, la madurez del proceso."

**Respaldo SD9:**
- Tabla 9.2, que tiene seis estándares: 25010, 25012, 29119, PMBOK, WCAG y OWASP.
- §9.1.4, Modelos de madurez: ISO 9001 y CMMI-DEV N3.

**Estado:** ✅ Las normas calzan con el SD9. Las leyes (Decreto 977, SII/DTE, Art. 25 bis, GS1/EDI) se definen en el SD2 y se mantienen en la diapositiva. La Ley 21.719 también la aplica el SD9 a los datos de prueba. Frase de apoyo: "las leyes las definimos en el SD2; el plan de calidad verifica que se cumplan".
---

## 29 · Calidad del producto · ~45 s

**Decir:**
"¿Con qué se mide la calidad? Con cuatro objetivos:
- 100 % de los requisitos con una prueba aprobada.
- Cero defectos críticos o altos al cierre.
- Cero minutos de caída entre las 05:30 y las 07:00, que es la ventana del despacho.
- Los 16 resultados del Caso.

Además, cada una de las ocho características de ISO 25010 tiene un umbral. Desempeño y fiabilidad son las que más pesan, porque el despacho depende de segundos y tiene que seguir funcionando sin enlace."

**Respaldo SD9:**

| Contenido de la diapositiva | Origen |
|---|---|
| Objetivos | Tabla 9.1 |
| Modelo | Figura 9.2 |
| Umbrales | Tabla 9.3 y Anexo 9.A |

Los umbrales de la tabla también calzan: p95 ≤ 1 s y ≤ 1,5 s, ≥ 99,9 %, RTO ≤ 4 h, RPO ≤ 15 min, cobertura de 70/80 % y −22 °C con guantes.
**Estado:** ✅ Calza.

---

## 30 · Calidad que bloquea · ~45 s

**Decir:**
"Hay siete puertas, de G0 a G6, y ninguna se salta. G0 a G2 corren en minutos con cada cambio. En G2 bloquean las métricas de código:
- cobertura de al menos 70 % en la lógica de negocio y 80 % global;
- complejidad de 10 como máximo;
- duplicación de 3 % como máximo.

Nadie puede levantar un bloqueo: se corrige o no se avanza. Además, el Líder de Calidad no responde a Desarrollo y puede vetar una promoción. Para aceptar el sistema se exigen las seis condiciones del Art. 17.3, que deben cumplirse todas."

**Respaldo SD9:**

| Contenido de la diapositiva | Origen |
|---|---|
| Puertas | Figura 9.3 y Tabla 9.7 (bloqueo y autoridad por puerta) |
| Métricas de G2 | Tabla 9.4 (complejidad ≤ 10 según McCabe, acoplamiento ≤ 20, duplicación ≤ 3 %) |
| Veto | §9.1, organización: "Puede vetar una promoción" |
| Condiciones de aceptación | Art. 17.3 |

**Estado:** ✅ Calza.

---

## 31 · Pruebas: del código al terreno · ~45 s

**Decir:**
"Son doce tipos de prueba: los diez que exige la BTT y dos que agregamos, el perfil operacional y el despliegue sin interrupción. Cada uno corre en un ambiente cada vez más parecido a producción, y lo que llega a producción es la misma imagen que se probó. Lo que no cabe en la nube se prueba en terreno: 14 horas sin señal y una cámara a −22 °C con guantes. La carga no la elegimos nosotros: es 1,5 veces el peak de septiembre, 21,99 TPS. Son 1.316 casos, 80 % automatizados, y la regresión completa cabe en una noche. Ningún ambiente de prueba usa datos reales sin anonimizar."

**Respaldo SD9:**

| Contenido de la diapositiva | Origen |
|---|---|
| Niveles por ambiente | Figura 9.4 |
| Tipos de prueba (10 de la BTT § 20.1 + 2) | Tabla 9.8 |
| Carga de prueba (21,99 TPS) | Tabla 9.9 |
| Origen y control de los datos de prueba | Figura 9.5 |
| Carga, casos y protocolos | T-13 |
| Regla de datos (Ley 21.719) | §9.2 |

**Estado:** ✅ Calza.

---

## 32 · Trazabilidad y mejora · ~40 s

**Decir:**
"Para ver cómo se conecta todo, tomemos el ejemplo del retiro sanitario en menos de 2 horas. La cadena va así:
- requisito RF-09.01;
- módulo M9;
- paquete 3.4.4 de la EDT;
- simulacro de retiro;
- código, fusionado con el ID del requisito;
- despliegue, con el digest de la imagen firmada;
- acta del H7.

La matriz se genera desde el repositorio, no se arma a mano. Si un resultado se desvía, el ciclo PDCA lo corrige con diagramas de control, Pareto y análisis de causa raíz. Cumplir con la calidad nos cuesta 11.136 HH, el 5,1 % de la línea base: 37,9 % es prevención y 62,1 % es evaluación."

**Respaldo SD9:**

| Contenido de la diapositiva | Origen |
|---|---|
| Trazabilidad de extremo a extremo | Figura 9.7 |
| Verificación y validación por hito | Figura 9.6 |
| Ciclo PDCA | Figura 9.8 |
| Costo de la calidad | Tabla 9.6 (11.136 / 217.543 = 5,1 %) y Anexo 9.C |

**Estado:** ✅ Calza.
