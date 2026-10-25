# Implementación documental de cadena de frío — verificación del 25-10-2026

Fuente: `BRIEF_IMPLEMENTACION_CADENA_FRIO.md` del 24-10-2026 y `Solucion_Cadena_de_Frio_en_Ruta.md`, versión 9.4, conservados en `subdoc-4`, carpeta `00/trazabilidad/`.

## Resultado y alcance

Se editaron SD2, SD3, SD4, SD5, SD6 y SD7 en sus ramas respectivas. Se conservaron las figuras y todos los bloques figure/TikZ, las 139 entidades del diccionario de SD5 y la numeración de los paquetes existentes. No se editaron SD1, SD8, SD9, SD13, Informe 3 ni formularios económicos. No se incorporaron precios ni el riesgo de rechazo del kit por transportistas.

- SD2: artículos y tolerancias del RSA.
- SD3: cuatro RF, cuatro RNF, RNG-17, S-28, R18-03, historia por SSCC y T-12; exclusión E-09 coherente con la compra por LafroX.
- SD4: Greengrass en camión, dos caminos siempre activos, doble evaluación, retención por SSCC, contingencia y disposición; ADR-24, eventos, seguridad, recuperación, T-11 y dimensionamiento reproducible; pruebas V1–V21 especificadas.
- SD5: atributos, catálogos e índice en las entidades existentes; idempotencia, originales de ambos registradores, ausencia de GPS en temperatura y retención de cinco años.
- SD6: compra de frío y conectividad a cargo de LafroX; certificación aplicable y despliegue. Se eliminó la duplicación de la tabla de adquisiciones en el ensamblador del anexo: ahora importa la tabla editada.
- SD7: cinco paquetes nuevos, HH, curvas, esfuerzo continuo, dotación, once actividades tempranas y dependencias D-35–D-38. Servicio móvil/SBD disponible antes del banco; piloto después de integración/H4 y antes de la ola 3; cuatro kits antes del piloto y 28 antes de la ola 3.

## Cifras conciliadas

| Magnitud | Resultado |
|---|---|
| Catálogo SD3 | 270 requerimientos: 180 RF y 90 RNF; 64 críticos, 163 altos y 43 medios |
| Parte A del T-12 | 279 filas: 270 requisitos y 9 alias absorbidos |
| Flota fría | 28 camiones: 18 propios y 10 de transportistas |
| Reserva del kit | 31 por componente unitario; 93 sondas; 93 botellas; 62 SIM M2M |
| INT-05 | 30.548 mensajes/día = 6.048 + 24.360 + 112 + 28 |
| Lecturas térmicas | 127.848/día |
| Integraciones sin doble conteo de INT-04 | 244.280 / 362.561 mensajes/día |
| Suma bruta de calculo.py | 249.880 / 372.961 mensajes/día |
| Temperatura | 6,77 GB/año crudos; 33,83 GB en cinco años; 1,69 GB/año almacenados; DynamoDB treinta días 0,556 GB |
| Satélite | 290 mensajes por camión y día; 8.120 por flota y día, conciliados con móvil |
| EDT | 227 paquetes; nueve fases y 49 cuentas, sin renumeración de paquetes anteriores |
| Esfuerzo | 207.487 HH de paquetes + 128 restauraciones + 9.336 soporte puente + 3.072 reserva = 220.023 HH |
| Incremento | 2.480 HH: 1.200 nuevas y 1.280 de ampliación en paquetes existentes |
| Programación | 168 paquetes con entregable y 59 de esfuerzo continuo; 119 actividades de 60 paquetes hasta H2 |
| Envolvente mensual de personas | 70 en mes 15, con refuerzo separado para la ampliación |

Las HH son estimaciones por analogía con las clases del T-15. La curva conserva la envolvente anterior y agrega techo(HH incrementales/128) por rol como refuerzo separado, sin suponer holgura disponible. La nivelación diaria, asignaciones nominales, feriados y reservas CPM/PERT siguen sujetos a comprobación en la línea base, como ya declaraba el documento; no se presentan como acreditados por la compilación. La base y el cálculo reproducible quedan en `revision/cadena_frio_modelo_base.json`, `revision/recalcular_cadena_frio.py` y `revision/cadena_frio_recursos_verificacion.json` de SD7.

## Verificación ejecutada

1. Coincidencia exacta de los 227 paquetes hoja de la EDT con las 227 filas del T-15; ninguno duplicado ni faltante. Coincidencia de conteos por fase y responsable.
2. Cada RF-09.11–RF-09.14 y RNF-09.06–RNF-09.09 aparece una vez en su tabla de anexo y una vez en el T-12.
3. Suma de HH de paquetes, columnas de etapas, 56 meses y total general; esfuerzo continuo 7.1.3/7.2.4 y actividad de cada paquete nuevo hasta H2. Las once actividades nuevas tienen 80 HH, entre cinco y siete días hábiles y capacidad individual suficiente.
4. Precedencias por fecha: compra y conectividad antes del banco; banco antes del mapeo; mapeo, M9 e integración antes del piloto. Piloto de seis semanas: 08-11 a 17-12-2027 bajo el inicio nominal del plan; 28 actas antes de ola 3.
5. Reejecución de `calculo.py` sin diferencias en `resultados.md` y cotejo de todas las cifras del brief.
6. Comparación SHA-256 de figuras y comparación textual de bloques figure/TikZ contra el estado inicial: ningún cambio. Comparación del conjunto de entidades de SD5: 139 antes y después.
7. Compilación de 19 raíces con tres pasadas de LuaLaTeX. Los 16 PDF con contenido editado se publicaron en sus destinos; los tres PDF de control sin cambios de contenido conservan su versión previa. MiKTeX quedó con instalación automática y se instaló el paquete faltante `float`.
8. Extracción de texto de los 19 PDF y verificación de los códigos/cifras nuevos; revisión visual de 28 páginas seleccionadas de cuerpos, anexos y formularios. Se corrigieron desbordes nuevos de identificadores en SD5 y encabezados de declaración en SD3. No hay caracteres faltantes ni referencias indefinidas en los logs finales.
9. Revisión de diferencias y separación del trabajo previo: se conservan las eliminaciones ya preparadas antes de esta tarea y los registros ajenos sin agregarlos al commit. Las fuentes técnicas previas utilizadas por los PDF se conservan e integran para mantener reproducibilidad entre fuente y entrega.

Advertencia de maquetación conservada: la figura panorámica preexistente del T-14 (`formulario-t14/contenido.tex`, bloque de `EDT-EDT completa.drawio.pdf`) genera un Overfull hbox de 16,69 pt. No se alteró su bloque ni su figura, conforme a la prohibición del brief. Los anexos de datos conservan avisos de división de tablas largas; los 19 motores terminaron correctamente.

## Pendientes de figuras — no editadas

| Rama / archivo | Dato que requiere actualización o cotejo manual |
|---|---|
| SD3 `figures/figura 3.2.pdf` | Historia térmica por SSCC, cámara–andén–compartimento y escaneos de salida/carga/bajada |
| SD3 `figures/Diagrama de la solución.pdf` y `figures/DIAGRAMA-INTERFACES.pdf` | Gateway del camión, Iridium y segunda evaluación local; cotejar el recorrido representado |
| SD4 `04/figuras/logica/capas/ARQL-01_General_definitivo.pdf` | Suma bruta 249.880/372.961, INT-05 30.548 y nuevo borde de camión |
| SD4 `04/figuras/logica/capas/ARQL-22_Borde.pdf` | Greengrass también en camión, latido y evaluación independiente |
| SD4 `04/figuras/fisica/Arquitectura_Fisica_General.png` | Kit completo y caminos móvil/Iridium activos |
| SD4 `04/partes/4.2_fisica/02_a_emplazamiento.tex`, figura TikZ que contiene B-03 | Añadir los componentes del kit y nuevos flujos; bloque íntegro, incluida su referencia a termógrafos |
| SD5 `05_modelo_datos/figuras/Fig_5-5_Custodia_EPCIS.pdf` y `Fig_5-10_Telemetria_Cache.pdf` | Atributos compartimento, tipos/orígenes y catálogo de disposición; conservar entidades |
| SD7 `imagenes/Imagenes de la edt/EDT-EDT completa.drawio.pdf` y láminas de fases 2, 4 y 5 | Cinco paquetes nuevos y 227 paquetes totales |
| SD7 `imagenes/Diagramas que faltaban/Fig_T14-2_Cuentas_m1-21_Fases1-3.pdf` y `Fig_T14-3_Cuentas_m1-21_Fases4-7.pdf` | Ventanas de banco, mapeo, contrato y piloto; conectividad desde mes 2 y piloto meses 10–11 |
| SD7 `imagenes/Diagramas que faltaban/Fig_7-7_T15-1_Ruta_Critica.pdf` y `Fig_7-6_T15-2_Frentes_Trabajo.pdf` | Dependencias D-35–D-38 y ventana del nuevo trabajo; las cifras históricas no acreditan nivelación vigente |
| SD7 `imagenes/Diagramas que faltaban/Fig_T15-3_Planificacion_Gradual.pdf` | Cotejar incorporación de cuatro paquetes tempranos y detalle de 119 actividades/60 paquetes |

## Pendientes fuera de alcance

- SD13: `SD13_v_nueva/13_innovaciones/contenido.tex:346` y `SD13_v_nueva/T19/contenido.tex:81` conservan 10.920 mensajes diarios. Su base debe pasar a 30.548 mensajes y 127.848 lecturas; no se editaron.
- SD9: `SD9_v_nueva/09_anexos/contenido.tex:208` y `SD9_v_nueva/09_plan_calidad/contenido.tex:139` conservan el denominador 217.543 HH. Deben conciliarse con 220.023 HH y revisarse los esfuerzos de QA y la cobertura de ocho requisitos nuevos en T-13. SD9 no se editó.
- El generador heredado del SD3 emite archivos `tablas/anx_*` que no monta el documento vigente; se conservaron los ocho requisitos nuevos en su JSON de entrada y se editaron las tablas activas `tablas_anexo/`. No se regeneraron tablas históricas ajenas al documento vigente.
- La cotización local, certificación de equipos, rango de registradores bajo −20 °C, oferta contractual CloudConnect/segundo destino y pruebas físicas V1–V21 requieren evidencia de ingeniería. Esta tarea especifica su aceptación; no acredita su realización ni compra de equipos.

## Identificadores nuevos y localización

| Identificador | Localización |
|---|---|
| RF-09.11 a RF-09.14 | SD3 `tablas_anexo/rf_propios.tex` y T-12 |
| RNF-09.06 a RNF-09.09 | SD3 `tablas_anexo/rnf_propios.tex` y T-12 |
| RNG-17 | SD3 `tablas_anexo/reglas_negocio.tex` |
| ADR-24 | SD4 registro y Anexo 4-O |
| B-04 a B-15 | SD4 Formulario T-11, componentes del kit y SIM |
| 2.4.3 y 2.4.4 | SD7 cuenta 2.4, `tab_T14_15.tex`; T-15 y aceptación R18-03 |
| 4.1.4 | SD7 cuenta 4.1, `tab_T14_29.tex`; T-15, T-18 y aceptación |
| 5.1.4 | SD7 cuenta 5.1, `tab_T14_32.tex`; T-15, SD6 y referencias T-12 |
| 5.3.4 | SD7 cuenta 5.3, `tab_T14_34.tex`; T-15 y SD6 |
| D-35 a D-38 | SD7 Anexo 7.B |
| Actividades A01–A04 de 2.4.3, A01–A03 de 2.4.4/5.1.4 y A01 de 5.3.4 | SD7 `formulario-t15/tablas/tab_T15_9_bloque_2.tex` |

## Filas actualizadas de la declaración de uso de IA

| Documento | Filas |
|---|---|
| SD2 | 2.2 Comprensión |
| SD3 | 3.1–3.4; anexos 3.A, 3.B, 3.C, 3.D, 3.G y 3.J; T-12 |
| SD4 declaración única | 4.1–4.3; 4-A, 4-G, 4-I, 4-J, 4-N, 4-O, 4-P, 4-Q, 4-W; T-11 |
| SD5 | 5.1, 5.2, 5.4, 5-A, 5-C y 5-F |
| SD6 | 6.1, 6.2 y anexos |
| SD7 | 7.1–7.3, anexos y formularios T-14/T-15/T-18; declaraciones propias de esos entregables |

Las revisiones humanas anteriores se conservan como antecedentes. La actualización de esta sesión no se atribuye a un revisor humano ni acredita ensayos físicos.

## Informe 3 — no editado

El sistema de frío pasa a inversión de LafroX: sensores/gateways de cámara y componentes para 31 kits de camión. Las 62 SIM M2M y el servicio satelital son operación de LafroX. Se deberá reflejar en la oferta económica correspondiente, sin precios en estos subdocumentos.

## Ramas y checkouts

- SD2: `LafroX-Subdoc2-LateX` — checkout dedicado, sin cambiar el checkout principal de SD4.
- SD3: `LafroX-Subdoc3-LateX` — checkout dedicado, sin cambiar el checkout principal de SD4.
- SD4: `subdoc-4` — checkout dedicado, sin cambiar el checkout principal de SD4.
- SD5: `LafroX-Subdoc5-LateX` — checkout dedicado, sin cambiar el checkout principal de SD4.
- SD6: `LafroX-Subdoc6-LateX` — checkout dedicado, sin cambiar el checkout principal de SD4.
- SD7: `LafroX-Subdoc7-LateX` — checkout dedicado, sin cambiar el checkout principal de SD4.

## PDF verificados

| SD | Documento | Páginas |
|---|---|---|
| 2 | LAFROX-Subdocumento2-Anexos | 19 |
| 2 | LAFROX-Subdocumento2 | 30 |
| 3 | LAFROX-Formulario-T-12 | 265 |
| 3 | LAFROX-Subdocumento3-Anexos | 167 |
| 3 | LAFROX-Subdocumento3 | 41 |
| 4 | LAFROX-Formulario-T-11 | 45 |
| 4 | LAFROX-Subdocumento4-Anexos | 115 |
| 4 | LAFROX-Subdocumento4 | 196 |
| 5 | LAFROX-Subdocumento5-Anexos | 219 |
| 5 | LAFROX-Subdocumento5 | 47 |
| 6 | LAFROX-Formulario-T-10 | 5 |
| 6 | LAFROX-Formulario-T-9 | 8 |
| 6 | LAFROX-Subdocumento6-Anexos | 8 |
| 6 | LAFROX-Subdocumento6 | 12 |
| 7 | LafroX-Formulario-T-14 | 103 |
| 7 | LafroX-Formulario-T-15 | 86 |
| 7 | LafroX-Formulario-T-18 | 24 |
| 7 | LafroX-Subdocumento7-Anexos | 24 |
| 7 | LafroX-Subdocumento7 | 58 |

## Cotejo correctivo T-12/T-11 — 25-10-2026

Se detectó y corrigió la atribución de compra de sensores al CLIENTE que permanecía en la introducción del T-11. En el T-12 se sustituyeron las descripciones genéricas del kit por componentes y paquetes específicos para registro de cámaras, picking, rechazo, parametrización, evidencia y disposición; se distinguió M5 Preparación de M9 y se corrigió la referencia del tiempo de andén a 3.4.3. Se actualizaron ciclo de vida, autonomía, gestión de dispositivos y referencias B-04–B-15. Se retiraron del T-11 las dos referencias bibliográficas del registrador ELA sustituido.

Este cotejo corrige la alineación documental de la ampliación. No equivale a certificar cumplimiento integral de cada fila de toda la matriz ni a acreditar cotizaciones, certificaciones o ensayos físicos.
