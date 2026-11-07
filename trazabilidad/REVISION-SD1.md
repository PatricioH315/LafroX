# Trazabilidad de correcciones del Subdocumento 1

Fecha: 7 de noviembre de 2026. Rama de implementación: `LafroX-Subdoc1-LateX-CORRIGIENDO`. Base: `ffa82f3a`. Rama adicional de trazabilidad prevista: `codex/trazabilidad-sd1-revision-informe2`.

Fuente: «G02 - LAFROX - Primera Revisión Informe 2.pdf», apartado Subdocumento 1, páginas impresas 3–6. Alcance: nueve observaciones específicas, con el punto conjunto de organigrama y centros de datos en una fila. No se agregan observaciones generales como si fueran particulares del S1.

## Matriz por observación

| ID | Observación de la revisión | Corrección aplicada y ubicación | Estado y límite de cierre |
|---|---|---|---|
| SD1-01 | Sin ventas, patrimonio ni capacidad de garantía. | `contenido.tex`, 1.1, después del inventario de 112 equipos: patrimonio 2023–2025, ventas 2025, liquidez 1,8 y capacidad de emisión de $500 millones; sin tabla repetida. Respaldo académico F-01/F-02 en `ANTECEDENTES-SIMULADOS.md`. | Parcial: resuelta la ausencia de información en S1. No demostrada la suficiencia de garantía ni completados estados auditados y acreditación bancaria para el Sobre 1. |
| SD1-02 | SOC existente, contratado y por implementar a la vez. | 1.1, 1.2 y 1.5: NOC y función CISO existentes; SOC propio por habilitar en Valparaíso con dotación adicional; transición a cargo de CISO y NOC. Se remite calendario al plan de trabajo y T-15. | Corregida la contradicción interna. La rama local S7 mantiene SOC desde mes 13; no se modifica allí la programación ni se acredita su ejecución. Cotejo final con S4 pendiente. |
| SD1-03 | 31 FTE mensuales y 40 desarrolladores simultáneos contra 48 disponibles; debe cuadrar con T-15. | 1.5: retiradas las dos demandas incompatibles y la reserva arbitraria de ocho; conservados 48 desarrolladores corporativos y 15 especialistas de arquitectura e integración, con remisión a T-15. | Parcial: se corrige S1, no se declara nivelación validada. T-15 local distingue curva mensual y máximos simultáneos; su texto declara brechas CAL e implantación. Se requiere conciliación completa por perfil fuera de esta rama. |
| SD1-04 | Organigrama sin Comercial/Administración y sin ubicación de los dos centros de datos. | 1.1 y 1.2: Comercial y Administración y Finanzas bajo Gerencia; centros primario Santiago/secundario Valparaíso, administrados por Infraestructura. Nueva Figura 1.1 nativa en `figuras/organigrama-corporativo.tex`; se conserva el PDF histórico como antecedente no utilizado. | Corregido en S1. Emplazamientos definidos como supuesto del caso; cotejo con arquitectura del S4 pendiente. |
| SD1-05 | Equipo nominado en 1.5, reservado al capítulo 12. | 1.5: siete ámbitos sin nombres, diez roles y coordinación. Retirada tabla nominal y compromisos individuales; remisión explícita a SD12 y T-8. Contenido original preservado en `TRASLADO-SD12.tex.txt`. | Parcial global: S1 corregido. Traslado preparado, no integrado en SD12 porque sus fuentes no están presentes en esta rama ni se localizaron en main local. No se afirma haber editado SD12/T-8. |
| SD1-06 | Plan de certificaciones repetido en viñetas y párrafo. | 1.4: eliminado «El plan precedente formaliza…», conservadas fichas; anticipación de 60 días en ISO 9001/20000-1; cierre breve de prioridades. Se corrige la atribución del plazo de doce meses: corresponde a ISO 27001, no a ISO 20000-1. | Corregido el texto y el fundamento de la contingencia. No se presentan renovaciones como ya obtenidas. |
| SD1-07 | No menciona conocimiento acreditado sanitario y tributario RT-15.02 del caso. | 1.4, antes de Cartera de Clientes: conocimiento sanitario, DTE y experiencia sectorial vinculada a T-6. Registros simulados C-01/C-02 y vínculo E-01 en `ANTECEDENTES-SIMULADOS.md`. | Corregida la omisión y preparado respaldo académico. Pendiente integración formal de evidencias a la entrega y validación humana; no se simula un certificado oficial ni se afirma acreditación externa real. |
| SD1-08 | Alianzas vencen entre meses 2 y 11; falta analizarlo. | 1.6: análisis del primer año, renovación 60 días antes, separación entre membresía y soporte; contingencia mediante extensión o acuerdo previo, sin afirmar continuidad automática. | Corregido el análisis. Contratos concretos y evidencia de renovaciones quedan como compromisos futuros. |
| SD1-09 | Referencia farmacéutica a −22 °C poco habitual; explicar si se conserva. | 1.4, tabla de equivalencia y T-6 (Industria, Alcance, Volumen y cierre): doce cámaras de reactivos/materiales de diagnóstico congelados; 180 vehículos y 12 millones de registros del conjunto. Se conserva −22 °C y SLA 99,9%. | Corregido mediante supuesto académico explícito en el respaldo; no se atribuye esa temperatura a toda la flota ni a toda la industria farmacéutica. |

## Explicación de los cuatro bloques pedidos

### 1. Solidez financiera y capacidad de garantía

Se incorpora información concreta que faltaba en S1: evolución patrimonial positiva durante tres ejercicios, escala de ventas, liquidez y capacidad de emisión. El respaldo simulado permite comprobar la coherencia aritmética de los supuestos. Sin embargo, declarar $500 millones no demuestra que se cubran las garantías: las Bases fijan seriedad de USD 500.000, fiel cumplimiento de USD 1.000.000 y correcto funcionamiento por 5% de implementación. Sin valor de implementación y capacidad por moneda no se puede certificar suficiencia. Por eso el cierre es parcial y no se inventa un certificado bancario auténtico.

### 2. SOC único y desarrolladores coherentes con T-15

El SOC queda definido exclusivamente como capacidad por habilitar, separada del NOC y del equipo CISO existentes; se explica la transición y se deja su calendario en el documento de planificación. Se conserva una única cifra de capacidad corporativa de desarrollo: 48 personas, además de 15 especialistas de arquitectura e integración. Se retiran la comparación errónea entre 31 FTE totales y 40 desarrolladores simultáneos y la reserva de ocho no demostrada. La conciliación con T-15 no está cerrada: la rama S7 actual contiene magnitudes distintas por mes y simultaneidad y reconoce brechas de otros perfiles. Retirar cifras no equivale a nivelar recursos; esa comprobación se deja abierta expresamente.

### 3. Certificaciones sin repetición y RT-15.02

La eliminación del párrafo duplicado conserva los compromisos en sus fichas y permite analizar prioridades en un cierre breve. La contingencia ISO 20000-1 deja de invocar un plazo normativo que no le corresponde. Para RT-15.02 se explican los conocimientos sanitarios y tributarios y la experiencia en consumo masivo/cadena de frío, con registros académicos simulados identificados. La referencia correcta es Caso 02, página 27; RT-15.02 de las Transversales trata otra materia. Queda pendiente integrar y revisar los respaldos en la entrega formal, sin afirmar certificación externa inexistente.

### 4. Organización en 1.5 y equipo nominado en SD12

La sección 1.5 explica funciones, dependencia y coordinación sin nominación personal, y conserva diez roles agrupados en siete ámbitos más la jefatura. Los nombres, dedicaciones y compromisos retirados se preservan completos para evitar pérdida de información. El Formulario T-7 de las Bases Administrativas, página 59, confirma que el destino es SD12 y el artículo 34, página 22, su complemento con T-8. No se ha integrado el contenido en ese documento: se entrega un archivo de traslado y se informa la dependencia pendiente.

## Fuentes y cotejo entre ramas

- Bases Administrativas: páginas impresas 22–25 (idoneidad, garantías y acreditación), 57 y 59 (estructura T-7, SD1 y SD12).
- Bases Técnicas Transversales: página impresa 28, sección 15.2 (certificaciones).
- Caso 02 - Logística: páginas impresas 27 y 29 (RT-15.02 y materias sectoriales).
- T-15 consultado sin editar: rama `LafroX-Subdoc7-LateX-CORRIGIENDO`, commit `648f2fea626cf57d35e3eb042f2feb53d2adefbb`, `formulario-t15/contenido.tex` y `tablas/tab_T15_4_personas.tex`. Esta curva contiene DES=31 en meses 6 y 7; no es el total técnico ni prueba del máximo simultáneo. El mismo texto expresa que no hay nivelación nominal validada.

## Validación y entrega

Validación realizada el 7 de noviembre de 2026:

- Compilación directa con LuaLaTeX, con pasadas hasta estabilizar índices y referencias. `latexmk` no está disponible funcionalmente porque falta Perl.
- S1: 23 páginas. T-6: 8 páginas. Últimas compilaciones con código de salida 0, sin referencias indefinidas, sin avisos de etiquetas pendientes ni cajas desbordadas.
- Inspección visual del conjunto mediante miniaturas y revisión ampliada del organigrama, declaración de IA y tabla del T-6. Se ajustaron separaciones del organigrama y el inicio de la declaración de IA.
- El registro del S1 conserva el mensaje no fatal de LuaTeX `ignored error Infinite glue shrinkage found in box being split`, asociado al corte de la tabla de IA. La tabla se renderiza legible, con encabezado repetido; no se alteró la plantilla corporativa para resolver ese comportamiento del motor.
- Comprobación del texto de ambos PDF sin marcadores `??`; verificación de que 1.5 no contiene nombres, tabla nominal ni demandas de 31/40 mal comparadas.
- Comprobación de diferencias sin errores de espacios; se conservó el PDF histórico del organigrama, aunque la figura activa es la nueva fuente TikZ.
- La declaración de IA identifica la revisión humana de la entrega anterior y deja explícita la validación pendiente de los nuevos cambios.

Los archivos de esta carpeta son documentación de revisión y apoyo académico; no se incorporan automáticamente como archivo fuera de nomenclatura a la oferta final. Los cuatro párrafos explicativos solicitados están en la sección anterior. El cierre documental de cada observación requiere atender sus límites de estado, aunque el cambio local esté implementado.
