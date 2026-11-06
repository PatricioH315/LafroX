# LafroX — Plan de integración de 4.1 en SD4 corrigiendo

Fecha: 5 de noviembre de 2026. Registro interno de planificación; no modifica ni reemplaza las fuentes LaTeX o sus PDF. La integración documental se ejecutó y verificó en checkout separado; el cierre se registra al final.

## 1. Origen y destino comprobados

- Rama de origen: `LafroX-Subdoc4.1-LateX-corrigiendo`.
- Commit a transferir: `8e00de50b02c837eb6a61165e7d740c349e2ab6f`.
- Mensaje exacto: `cambios de recorreccion logica`.
- Alcance del commit: 32 archivos de mejoras de 4.1, anexos lógicos, referencias/declaración pertinentes, figuras nuevas, dos PDF ensamblados y registros internos.
- Rama destino: `LafroX-Subdoc4-LateX-corrigiendo`.
- Referencia remota comprobada: `origin/LafroX-Subdoc4-LateX-corrigiendo`, commit `31221b23f92122136cfcb59554da18fb6b0dacab`.
- Base común comprobada: `b68ba316d61b7c2d8b129fc16c4a468b22fd4b50`.
- Checkout de origen: `D:/Usuario/Documents/Proyecto_Lafrox/LafroX-rama-latex`.

Quedaron fuera del commit los cambios locales anteriores en `04/AGENTS.md`, `04/formularios/T11/15_anexo_t11.tex` y `entrega/LAFROX-Formulario-T-11.pdf`. Continúan preservados en el checkout de origen, junto con los demás archivos locales preexistentes. No forman parte del trabajo nuevo de 4.1 y no se copiarán indiscriminadamente a destino.

Este plan es posterior al commit de correcciones y no está incluido en él. Se versiona en un commit documental separado de la rama 4.1 y se incorpora mediante merge, sin reescribir el commit de correcciones.

## 2. Diferencias de destino que deben conservarse

El destino añade sobre la base común el commit `31221b23`, `fix(sd4): aclara los máximos coincidentes de TPS`. No debe sustituirse el árbol completo de destino por el de 4.1.

Sus cambios comprenden:

- `04/partes/4.1_logica/03_principios_de_integracion.tex`.
- `04/anexos/logica/partes/23_anexo_4_1_t_desempeno.tex`.
- `04/partes/4.2_fisica/12_k_dimensionamiento.tex`.
- `04/anexos/fisica/16_anexo_4b_memoria_calculo.tex`.
- `04/formularios/T11/15_anexo_t11.tex` y su PDF.
- `Dimensionamiento/dimensionamiento/calculo.py`, `resultados.md` y `verificar_tps.py`.
- `00/trazabilidad/CIERRE_REVISION_I2_TPS_SD4.md`.
- Los dos PDF ensamblados del cuerpo y anexos.

Se conservarán los contenidos de cálculo y documentación técnica de ese commit. El archivo `resultados.md` pertenece a la herramienta de dimensionamiento, no es una fuente editable de subdocumento; se preserva sin usarlo como espejo para corregir LaTeX.

## 3. Simulación realizada

Se actualizó la referencia remota y se efectuó una combinación de tres vías con `git merge-tree`, sin cambiar rama, índice ni archivos de trabajo.

Resultado sobre las referencias indicadas:

- Las fuentes y los registros no presentan conflictos textuales.
- Solo coinciden dos rutas modificadas por ambos frentes, ambas binarias:
  - `entrega/LAFROX-Subdocumento4.pdf`.
  - `entrega/LAFROX-Subdocumento4-Anexos.pdf`.
- Estos dos PDF generan conflictos binarios. La solución consiste en recompilarlos desde las fuentes combinadas; escoger uno de los PDF antiguos como resultado final perdería parte del trabajo del otro frente.
- Evidencia de la simulación: `D:/Usuario/Documents/Proyecto_Lafrox/tmp/sd41_ejecucion_20261105/simulacion_integracion_sd4.txt`.

La simulación valida este estado concreto; si cambia la referencia destino, se repetirá antes de aplicar. Ausencia de conflicto textual no equivale a aceptación técnica ni a revisión humana.

## 4. Procedimiento propuesto

### Paso 1 — Actualizar referencias y proteger ambos estados

Consultar otra vez `origin`, confirmar el commit destino y comparar cualquier novedad con este plan. Comprobar que el commit de origen conserva mensaje, padre y 32 rutas. Consultar las instrucciones específicas del destino junto con las instrucciones vigentes de la raíz; una regla histórica incompatible no sustituye la política actual de trabajar con LaTeX/PDF.

Registrar huellas de los diez archivos propios de destino distintos de los dos PDF que se regenerarán. Guardar inventario del checkout de origen para conservar sus cambios locales y archivos sin seguimiento. La corrección de 4.1 ya está comprometida; no es necesario incluir los cambios anteriores de T-11 o AGENTS para transferirla.

Cierre: ambas referencias y la base común identificadas; todo cambio nuevo de destino analizado antes de continuar.

### Paso 2 — Preparar un checkout separado para destino

Utilizar un worktree limpio dentro de `D:/Usuario/Documents/Proyecto_Lafrox`, por ejemplo `tmp/sd4-corrigiendo-integracion`, comprobando que la ruta esté libre y que la rama destino no esté ocupada por otro worktree.

Si no existe rama local destino, crearla siguiendo `origin/LafroX-Subdoc4-LateX-corrigiendo`. Si existe, comprobar su relación con origin y preservar su trabajo. Mantener el checkout original sobre la rama 4.1; no cambiarlo ni guardar sus cambios con operaciones globales para liberar la rama.

Cierre: checkout limpio en la rama correcta, basado en el destino actualizado y sin archivos ajenos.

### Paso 3 — Aplicar el commit completo de correcciones

Integrar la rama `LafroX-Subdoc4.1-LateX-corrigiendo` mediante merge sin commit automático y sin fast-forward. El merge incluye el commit técnico `8e00de50b02c837eb6a61165e7d740c349e2ab6f` y el commit documental posterior de este plan. Sus 32 rutas técnicas se conservan como una unidad. Se resolverán los PDF recompilando antes del commit de merge. Para máxima precaución, se prueba primero en una rama temporal de integración y la rama destino local solo avanza después de verificar el resultado.

Con el destino actual se esperan únicamente los dos conflictos binarios identificados. Si aparecen conflictos de texto, detener la resolución automática, cotejar origen/base/destino y resolver conservando ambas correcciones. No usar una elección global de «ours» o «theirs» sobre todo el árbol.

Para liberar los PDF en conflicto, conservar provisionalmente las versiones del destino, marcarlas como resueltas y sustituirlas después por los PDF recompilados. En este contexto «ours» significa la rama destino. Ese paso provisional no es el resultado de la integración.

Cierre: todas las fuentes de 4.1 integradas y los cambios de TPS del destino conservados; ningún conflicto pendiente ni marcador de conflicto en LaTeX.

### Paso 4 — Verificar coherencia de las fuentes combinadas

Revisar especialmente:

- Identidad: manifiesto de 26 h, renovación horaria, antigüedad máxima de 1 h al corte y credenciales personales independientes; cobertura de ruta de 14,5 h, margen de 30 min y máximo de 16 h desde emisión.
- Pruebas nuevas AL-ID-01, AL-MOD-01, AL-FRIO-01 y AL-UI-01, distinguiendo protocolo diseñado de ensayo ejecutado.
- Matriz individual de 4-E, Tabla A.6a; resumen del cuerpo, Tabla 4.1-A; registro de soporte A.20 y matriz complementaria A.21.
- Figura 1 y variantes de puertas de servicio, negocio e integración: rutas de inclusión válidas y nombres M10 Analítica/M11 Canal moderno.
- Corrección propia de destino: 14,66 TPS como máximo modelado de septiembre en 12:00–13:00 y 6,94 TPS en despacho, con mezcla diferente; los máximos por sitio no se suman sin coincidencia horaria.
- Anexo 4-T de destino: carga de aceptación de 21,99 TPS para el peak y 10,41 TPS para despacho durante 90 min, con cero minutos de indisponibilidad declarados como criterio de ensayo.
- Referencias, declaración de IA y revisiones: preservar el alcance veraz; no convertir comprobación automática en una revisión humana nueva.

Cierre: coherencia entre ambas correcciones y evidencia por requisito. No ampliar el trabajo a otros subdocumentos.

### Paso 5 — Regenerar los dos PDF desde destino

Compilar desde el worktree de destino el cuerpo y los anexos con sus ensambladores vigentes y las pasadas necesarias para estabilizar índices y referencias. Regenerar las dos rutas binarias en conflicto usando las fuentes combinadas.

Preservar el PDF T-11 del destino: esta transferencia no modifica su fuente y no requiere sustituirlo por el archivo local heredado del origen. Evitar una ejecución indiscriminada del script completo que lo regenere sin necesidad.

Cierre: ambos PDF reflejan simultáneamente las mejoras lógicas y la corrección de TPS. No conservar como entrega final el PDF antiguo de ninguno de los dos frentes.

### Paso 6 — Comprobar contenido, presentación y preservación

Verificar compilación sin errores, referencias indefinidas, destinos duplicados o desbordes; revisar visualmente Figura 1, tablas nuevas, protocolos, índices y numeración. La medida de 10,41 pt de Figura 1 debe comprobarse de nuevo al tamaño final de destino.

Comparar los archivos propios de destino con sus huellas previas. Exceptuar únicamente los dos PDF recompilados y cualquier ajuste adicional explícitamente justificado, que se registrará. T-11 debe conservar su contenido y versión de destino.

Comprobar las 32 rutas del commit original: los 30 archivos no conflictivos deben conservar su aporte y los dos PDF deben tener generación nueva. Copiar este plan al registro interno de destino y actualizar el resultado de ejecución con los localizadores y huellas de los PDF integrados. El registro de validación de la rama 4.1 se conserva como evidencia histórica, no como validación automática del destino.

Cierre: lista de cambios revisada, comprobaciones documentadas y archivos ajenos preservados. La validación es documental y de compilación, sin afirmar ejecución de pruebas funcionales sobre una aplicación.

### Paso 7 — Registrar la integración local

Crear el commit de integración solo después de resolver, recompilar y verificar. Mensaje propuesto: `integra recorreccion logica 4.1 en sd4 corrigiendo`. Su descripción debe citar `8e00de50b02c837eb6a61165e7d740c349e2ab6f`, el commit TPS conservado y las comprobaciones realizadas.

Comprobar que la rama destino conserva su historia y las correcciones de ambos frentes, que no hay conflictos ni cambios inesperados y que el checkout de origen sigue intacto. No publicar la rama como parte de este plan; el push requiere una petición del usuario.

## 5. Condiciones de detención o recuperación

- Si cambió origin o aparecieron cambios locales de destino, preservar e inspeccionar antes de aplicar; no hacer reset ni sobrescribirlos.
- Si la combinación no conserva el cambio TPS o requiere decisiones técnicas nuevas, mantener la integración sin cerrar hasta resolverlas.
- Si falla la compilación, corregir en el checkout de integración y volver a verificar antes de registrar el resultado.
- Si debe descartarse el intento y Git mantiene un merge activo, utilizar su mecanismo de aborto en el checkout de integración. Si no existe ese estado, conservar el checkout y sus evidencias antes de decidir cómo recuperarlo; no usar limpieza recursiva o restablecimiento global automático.

## 6. Inventario exacto del commit a transferir

- `00/trazabilidad/PLAN_MEJORA_SD4_REVISION_INFORME2_2026-11-05.md`.
- `00/trazabilidad/RESULTADO_MEJORAS_SD41_2026-11-05.md`.
- `04/anexos/logica/partes/02_anexo_4_1_a_catalogo_de_eventos_canonicos.tex`.
- `04/anexos/logica/partes/05_anexo_4_1_d_matriz_de_los_doce_modulos.tex`.
- `04/anexos/logica/partes/06_anexo_4_1_e_trazabilidad_funcional.tex`.
- `04/anexos/logica/partes/08_anexo_4_1_g_catalogo_de_interfaces_internas.tex`.
- `04/anexos/logica/partes/09_anexo_4_1_h_catalogo_de_interfaces_externas.tex`.
- `04/anexos/logica/partes/14_anexo_4_1_m_verificacion_de_continuidad_logica.tex`.
- `04/anexos/logica/partes/15_anexo_4_1_n_correspondencia_de_componentes_logicos.tex`.
- `04/anexos/logica/partes/16_referencias.tex`.
- `04/anexos/logica/partes/18_anexo_4_1_o_decisiones_logicas.tex`.
- `04/anexos/logica/partes/19_anexo_4_1_p_tecnologias_soporte.tex`.
- `04/anexos/logica/partes/21_anexo_4_1_r_controles_seguridad.tex`.
- `04/anexos/logica/partes/25_anexo_4_1_v_aceptacion_y_dependencias.tex`.
- `04/figuras/fuentes/logica/generar_vistas_41_corregidas.py`.
- `04/figuras/logica/capas/ARQL-01_General_41_corregida.pdf`.
- `04/figuras/logica/capas/ARQL-23_Enlace_servicios_41_corregida.pdf`.
- `04/figuras/logica/capas/ARQL-24_Negocio_41_corregida.pdf`.
- `04/figuras/logica/capas/ARQL-25_Integracion_eventos_41_corregida.pdf`.
- `04/partes/4.1_logica/04_capas_de_la_arquitectura.tex`.
- `04/partes/4.1_logica/05_modulos_funcionales_y_limites_de_contexto.tex`.
- `04/partes/4.1_logica/06_modelo_de_datos_conceptual.tex`.
- `04/partes/4.1_logica/08_detalle_de_tecnologias_seleccionadas.tex`.
- `04/partes/4.1_logica/09_implantacion_progresiva_del_backend_laravel.tex`.
- `04/partes/4.1_logica/13_puntos_unicos_de_falla_y_riesgos_residuales.tex`.
- `04/partes/4.1_logica/16_funciones_disponibles_y_no_disponibles_sin_conexion.tex`.
- `04/partes/4.1_logica/19_identidad_y_ciclo_de_vida_de_conductores_externos.tex`.
- `04/partes/4.1_logica/22_condiciones_y_supuestos_de_diseno.tex`.
- `04/partes/cierre/declaracion_de_uso_de_ia.tex`.
- `04/partes/cierre/referencias.tex`.
- `entrega/LAFROX-Subdocumento4-Anexos.pdf`.
- `entrega/LAFROX-Subdocumento4.pdf`.

## 7. Resultado de la ejecución

El merge de la rama 4.1 se preparó sobre `31221b23` en un worktree limpio y una rama temporal. Las fuentes se combinaron sin conflictos; los dos conflictos binarios se resolvieron recompilando cuerpo y anexos desde el árbol integrado. Se verificaron TPS, referencias, presentación y preservación antes del commit de merge y de crear la rama destino local.

Origen incorporado: `964736de83cf175b899cbbd56d940bf05407f303` (incluye `8e00de50`, correcciones, y el commit documental del plan). El registro completo y las huellas están en `00/trazabilidad/RESULTADO_INTEGRACION_SD41_SD4_2026-11-05.md`. La publicación en origin queda fuera de esta operación.
