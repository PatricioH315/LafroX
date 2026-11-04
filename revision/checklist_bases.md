# Checklist de revisión del prototipo según las bases

Lista de todo lo que el prototipo debe contener o demostrar según las **Bases Técnicas Transversales** y las **Bases Administrativas**. No incluye exigencias del documento del caso (Caso 02 Logística).

Marque cada casilla solo después de comprobarla en el prototipo. Si un punto no se cumple, anote la pantalla o el motivo en la columna de observaciones de la sección final.

## Constancia: lo que el prototipo no puede demostrar por sí mismo

El prototipo es una simulación sin servidor. Las bases no exigen funcionalidad real (Cap. 25.6), pero algunos puntos de esta lista no se comprueban navegando el prototipo: dependen de la publicación, de un proceso de pruebas o de otro entregable.

| # | Exigencia | Fuente | Por qué no se demuestra en la simulación | Cómo se acredita |
|---|---|---|---|---|
| 1 | Acceso garantizado por seis meses | RT-25.07 | Depende del servicio donde se publique, no del prototipo | Publicar en un servicio estable y conservar el enlace |
| 2 | Enlace navegable en línea | RT-25.06 | La copia local con `.bat` no es un enlace en línea | Publicar antes del 13-11-2026 y probar el enlace |
| 3 | Verificación de WCAG con herramientas automatizadas y pruebas manuales | RT-13.01; Art. 26° | Es un proceso de prueba, no una pantalla | Informe de conformidad de accesibilidad (entregable 17) |
| 4 | Pruebas de usabilidad con personas usuarias reales del CLIENTE | RT-13.03; Art. 26° | Requiere participantes reales | Documento de hallazgos y cambios de diseño |
| 5 | Indicadores de usabilidad comprometidos (tiempo, pasos, errores, aprendizaje) | RT-13.04; Art. 26° | Se miden con personas usuarias, no se simulan | Propuesta técnica, con su método de medición |
| 6 | Uso con guantes, a la intemperie y con luminosidad variable | RT-13.08; Art. 26° | Solo se prueba en el dispositivo y el lugar reales | Prueba en terreno con el terminal especificado |
| 7 | Operación real sin conexión | RT-13.08; Cap. 25.2 | El prototipo simula la cola y la sincronización, sin persistencia ni servidor | Pruebas de aceptación con dispositivos reales |
| 8 | Compatibilidad con navegadores | RT-25.06; RT-13.10 | Hay que probarlo en cada navegador; la simulación no lo garantiza | Matriz de navegadores y registro de pruebas |
| 9 | Arquitectura de información | RT-25.09 | Es un documento que acompaña al prototipo, no una pantalla | Documento con mapa del sitio, diagrama, taxonomía, menús y jerarquía |
| 10 | Exportar a documento interactivo sin conexión (deseable) | RT-25.10 | Es un formato de entrega adicional | Archivo exportado entregado junto al enlace |

Estos puntos siguen en la lista, pero se marcan con la evidencia de la última columna, no navegando el prototipo.

> **Revisión externa del 04-11-2026.** De sus observaciones, solo son límites del prototipo RT-25.07 (los seis meses), la revisión con lector de pantalla de RT-25.03 y el uso real con guantes. RT-25.06 se corrige publicando el sitio. Los botones de 38 px y «Cerrar misión» de 14,8 mm ya se corrigieron en el código (✓ 04-11-2026). La clasificación completa, con los requerimientos de SD3 y los errores de datos, está en `checklist_sd3_sd4.md`, sección 10.

## Resultado de la revisión (03-11-2026)

Revisión sobre la rama LafroX-Prototipo-HTML (commit 20cab1d8), con el perfil de evaluación, en servidor local. Se recorrieron las 49 rutas: sin errores de consola, sin enlaces internos rotos y con contraste AA en modo claro y oscuro. Se midieron los 5 tamaños exigidos y los objetivos táctiles de cada pantalla.

- [x] = cumple, verificado en el prototipo o en su código.
- [ ] con ⚠ = no cumple, parcial o pendiente; el motivo va debajo y se repite en la tabla de pendientes.
- ✓ = observación de la primera revisión, ya corregida y verificada en el navegador.

**Segunda revisión (03-11-2026, tras las correcciones):** sin desplazamiento horizontal en 375, 768, 1024, 1366 y 1920 px; todos los controles con al menos 44 × 44 px (salvo la excepción del mapa de telemetría); contraste AA también en alto contraste; atajos y burbujas de ayuda probados; sin errores de consola.

## Cómo usar esta lista

1. Abra el prototipo desde el enlace en línea que se entregará, no desde la copia local.
2. Recorra las secciones en orden: entrega, alcance mínimo, principios, componentes, interactividad y penalizaciones.
3. Revise cada perfil de persona usuaria al menos una vez.
4. Al final, registre los incumplimientos en la tabla de pendientes.

## Fuentes

| Fuente | Sección | Qué exige |
|---|---|---|
| Bases Técnicas Transversales | Cap. 25 (RT-25.01 a RT-25.10) | El prototipo propiamente tal |
| Bases Técnicas Transversales | Cap. 13 (RT-13.xx) | Usabilidad, accesibilidad y experiencia de usuario de toda interfaz |
| Bases Técnicas Transversales | Cap. A (entregable 27) | Momento de entrega |
| Bases Administrativas | Art. 26° | Accesibilidad y usabilidad |
| Bases Administrativas | Cronograma, hito 10 | Fecha del Informe 3 |

---

## 1. Entrega y acceso

- [ ] Se entrega junto con el **Informe 3**, el **13-11-2026** (Cap. 25.1; entregable 27; cronograma hito 10).
  - ⚠ Pendiente: la entrega es el 13-11-2026.
- [x] Es un prototipo interactivo de **alta fidelidad** (Cap. 25.1).
- [x] Se entrega como **enlace navegable en línea** (RT-25.06).
  - ✓ Corregido el 04-11-2026: publicado en https://patricioh315.github.io/LafroX/ desde la rama LafroX-Prototipo-HTML. Responde 200 y las rutas probadas cargan sin errores.
- [x] Funciona **sin instalación ni complementos** (RT-25.06).
- [ ] Es compatible con los **navegadores modernos vigentes** (RT-25.06).
  - ⚠ Parcial: probado solo en Chromium (navegador integrado); falta Firefox y Safari.
- [ ] El acceso está garantizado por **al menos seis meses** desde la entrega (RT-25.07).
  - ⚠ El enlace ya está publicado (04-11-2026); falta que se cumplan los seis meses.
  - **No corregible en el prototipo**: publicar resuelve el acceso, pero los seis meses solo se comprueban con el paso del tiempo. Se acredita con la publicación estable y el compromiso de mantener el repositorio.
- [x] Simula de forma realista la navegación y los flujos sin servicios de fondo ni base de datos (Cap. 25.1).
- [x] Permite recorrerlo **desde la perspectiva de los distintos perfiles** de personas usuarias (Cap. 25.1).
- [ ] Deseable: se puede exportar a un documento interactivo para revisión **sin conexión** (RT-25.10).
  - ⚠ No verificado: no hay un documento interactivo exportado para revisión sin conexión.

## 2. Alcance mínimo (Cap. 25.2)

### 2.1 Portal principal

- [x] Página de inicio pública.
- [x] Página de inicio con sesión iniciada, **personalizada por perfil**.
- [x] Tablero principal con **componentes configurables**.
- [x] Menú de navegación completo y funcional.
- [x] Rastro de navegación (migas de pan).
- [x] Navegación contextual.

### 2.2 Autenticación e incorporación

- [x] Pantalla de inicio de sesión **unificada**.
- [x] Registro de una persona usuaria externa en **al menos cinco pasos**.
- [x] Recuperación de acceso.
- [x] Segundo factor de autenticación.
- [x] Tablero de primer ingreso con **recorrido guiado**.

### 2.3 Proceso operacional principal

- [x] Flujo de negocio central del caso, **de extremo a extremo**.
- [x] Tiene **al menos seis pasos**, desde el inicio hasta el cierre.
- [x] Muestra los **estados intermedios**.
- [x] Incluye el manejo de la **excepción más frecuente**.

### 2.4 Proceso operacional secundario

- [x] Listado.
- [x] Vista de detalle.
- [x] Creación.
- [x] Flujo de aprobación **visual**.

### 2.5 Perfil de terreno u operación

- [x] Vista que usa la persona operacional en su puesto real.
- [x] Versión **móvil**.
- [x] Comportamiento **sin conexión**, si el caso lo requiere.

### 2.6 Gestión de terceros

- [x] Directorio de la contraparte externa (clientes, proveedores u otra).
- [x] Ficha completa.
- [x] Evaluación.
- [x] Historial.

### 2.7 Tablero analítico

- [x] Indicadores principales con visualizaciones.
- [x] **Al menos seis tipos de gráfico distintos**.
- [x] Filtro por **período**.
- [x] Filtro por **categoría**.
- [x] Profundización desde el indicador **hasta el detalle**.
- [x] Exportación de informes.

### 2.8 Administración

- [x] Gestión de personas usuarias.
- [x] Gestión de roles y permisos.
- [x] Parametrización.
- [x] Consulta de auditoría.

### 2.9 Módulos adicionales

- [x] Primer módulo adicional pertinente al caso.
- [x] Segundo módulo adicional pertinente al caso.

## 3. Principios de diseño exigidos

### RT-25.01 · Navegación intuitiva (también RT-13.05)

- [x] Se usa sin necesidad de manual.
- [x] Toda funcionalidad principal se alcanza en **tres interacciones o menos** desde el inicio del perfil.

### RT-25.02 · Retroalimentación (también RT-13.06)

- [x] Hay retroalimentación visual clara ante **cada acción**.
- [x] Hay estados de carga y transiciones fluidos.
- [x] Los errores indican **qué ocurrió y qué hacer**.
- [x] No hay mensajes técnicos dirigidos a la persona usuaria final.

### RT-25.03 · Accesibilidad WCAG 2.2 AA (también RT-13.01, RT-13.07, RT-13.11; Art. 26°)

- [x] Contraste adecuado (texto 4,5:1; texto grande y controles 3:1).
- [x] Tamaños de fuente legibles.
- [x] Objetivos táctiles de **al menos 44 × 44 px**.
  - ✓ Corregido el 04-11-2026: los botones del paso a paso medían 38 px de alto (revisión externa); ahora miden 44 px (`.stepper .step`).
  - ✓ Corregido: todos los controles miden al menos 44 × 44 px en los 5 tamaños. Excepción: en teléfono y tableta los marcadores del mapa de /telemetria se reducen con el SVG; la misma información está en Rutas con controles de 44 px (excepción de función equivalente, WCAG 2.5.8).
- [x] Navegación **completa por teclado**.
- [x] Orden de foco lógico.
- [x] Atajos de teclado para operaciones frecuentes (RT-13.11).
  - ✓ Corregido: «/» buscar, «g» luego «i», «b», «n» o «p» para ir a inicio, bandeja, notificaciones o perfil, y «?» para ver la lista. Se desactivan en Mi perfil › Accesibilidad.
- [x] Textos alternativos en imágenes y gráficos.
- [x] Etiquetas de accesibilidad en controles.
- [x] Iconografía acompañada de texto (RT-13.07).
  - ✓ Corregido en lo principal: la paginación muestra «Anterior» y «Siguiente», y en escritorio amplio los botones de la barra superior muestran «Avisos» y el tema. Siguen solo con ícono el botón «⋯» de cada fila y el de plegar el menú, ambos con nombre accesible.
- [x] Flujos guiados paso a paso para baja alfabetización digital (RT-13.07).
- [x] Alto contraste disponible (RT-13.07).
  - ✓ Corregido: Mi perfil › Accesibilidad › Contraste: alto contraste, en claro y en oscuro.
- [ ] Verificado con herramientas automatizadas **y** pruebas manuales (RT-13.01; Art. 26°).
  - ⚠ Pendiente: no hay informe de conformidad; en esta revisión se hizo un barrido automático de contraste y de tamaños.
  - **No corregible en el prototipo**: la revisión con lector de pantalla (NVDA o VoiceOver) es una prueba manual que se documenta en el informe de conformidad, no un cambio de pantalla.

### RT-25.04 · Diseño responsivo (también RT-13.02)

- [x] Escritorio **1920 × 1080**.
- [x] Escritorio **1366 × 768**.
- [x] Tableta **768 × 1024 vertical**.
- [x] Tableta **1024 × 768 horizontal**.
- [x] Teléfono **375 × 812**.
- [x] Puntos de quiebre coherentes.
- [x] El contenido se adapta, no solo se reduce (RT-13.02).

### RT-25.05 · Sistema de diseño documentado (también RT-13.09)

- [x] Paleta de **a lo más cinco colores principales**.
- [x] **A lo más dos familias tipográficas**, jerarquizadas.
- [x] Iconografía coherente.
- [x] Retícula y espaciado consistentes.
- [x] Componentes reutilizables.
- [x] El sistema está **documentado** (entregable 17 y RT-25.05).
  - ✓ Corregido: docs/sistema_diseno.md.

### Interfaces de terreno (RT-13.08, según caso; Art. 26°)

- [ ] Usable con guantes (objetivos amplios).
  - ⚠ No verificable en simulación: el uso real con guantes **no se puede corregir** en el prototipo. ✓ Lo corregible ya se hizo: «Cerrar misión» medía 14,8 mm y ahora mide 60 px (≈ 15,9 mm, RNF-05.02).
- [ ] Legible a la intemperie y con luminosidad variable.
  - ⚠ No verificable en simulación.
- [ ] Funciona sin conexión.
  - ⚠ Simulado: la app muestra la cola y la sincronización; la operación real no se puede probar.

### Deseable (RT-13.12)

- [x] Modo oscuro.
- [x] Personalización de la interfaz por persona usuaria.

## 4. Componentes de interfaz obligatorios (Cap. 25.4)

### Navegación

- [x] Menú principal.
- [x] Menú secundario contextual.
- [x] Rastro de navegación.
- [x] Paginación.
- [x] Pestañas.
- [x] Acordeones.
- [x] Navegación por pasos.
- [x] Menú de acciones rápidas.

### Formularios

- [x] Campos de texto con validación en tiempo real.
- [x] Selectores y desplegables.
- [x] Casillas de verificación.
- [x] Botones de opción.
- [x] Selector de fecha.
- [x] Selector de hora.
- [x] Carga de archivos con arrastrar y soltar.
- [x] Autocompletado.
- [x] Formulario de múltiples pasos.

### Visualización de datos

- [x] Tabla con ordenamiento.
- [x] Tabla con filtrado.
- [x] Gráfico de barras.
- [x] Gráfico de líneas.
- [x] Gráfico circular.
- [x] Tarjetas de información.
- [x] Línea de tiempo.
- [x] Indicadores de progreso.
- [x] Distintivos y etiquetas.
- [x] Información contextual emergente (tooltip).

### Retroalimentación

- [x] Mensaje de éxito.
- [x] Mensaje de error.
- [x] Mensaje de advertencia.
- [x] Mensaje de información.
- [x] Ventanas modales y diálogos.
- [x] Notificaciones emergentes.
- [x] Esqueletos de carga.
- [x] Indicadores de progreso.
- [x] Estados vacíos **ilustrados**.

### Acción

- [x] Botón primario.
- [x] Botón secundario.
- [x] Botón terciario.
- [x] Botón de acción flotante.
- [x] Acciones en línea.
- [x] Menús contextuales.
- [x] Acciones masivas.
- [x] Confirmación de acciones críticas.

## 5. Nivel de interactividad (RT-25.08)

- [x] Navegación completa entre pantallas.
- [x] Simulación de ingreso de datos.
- [x] Transiciones y animaciones básicas.
- [x] Estados de posado (hover).
- [x] Estados activos.
- [x] Simulación de carga de archivos.
- [x] Elementos desplegables funcionales.
- [x] Simulación de validaciones.

## 6. Arquitectura de información (RT-25.09)

Se entrega junto al prototipo, como documento aparte.

- [x] Mapa del sitio completo.
  - ✓ Corregido: docs/arquitectura_informacion.md, sección 1.
- [x] Diagrama de navegación.
  - ✓ Corregido: docs/arquitectura_informacion.md, sección 2.
- [x] Taxonomía y nomenclatura.
  - ✓ Corregido: docs/arquitectura_informacion.md, sección 3.
- [x] Estructura de menús.
  - ✓ Corregido: docs/arquitectura_informacion.md, sección 4.
- [x] Jerarquía de la información.
  - ✓ Corregido: docs/arquitectura_informacion.md, sección 5.

## 7. Causas de penalización (Cap. 25.6)

Cada casilla marcada significa que el riesgo **no** está presente.

- [x] No hay pantallas estáticas ni no navegables.
- [x] El diseño está personalizado al caso, no es genérico.
- [x] No hay incumplimientos de accesibilidad.
  - ✓ Corregido: objetivos de 44 px; el informe formal de conformidad sigue pendiente (ver RT-13.01).
- [x] No hay navegación confusa.
- [x] No hay **enlaces rotos**.
- [x] No hay inconsistencias visuales evidentes.
- [x] Responde bien en **todos** los tamaños exigidos.

No se exige (Cap. 25.6): servicios de fondo reales, base de datos, procesamiento real, integraciones externas, autenticación real ni persistencia de datos.

## 8. Documentos asociados que no son el prototipo

Las bases los piden en otros entregables. Se listan para no confundirlos con el prototipo.

| Exigencia | Fuente | Dónde va |
|---|---|---|
| Informe de conformidad de accesibilidad | RT-13.01; Art. 26° | Entregable 17, Sobre N° 2 |
| Investigación y pruebas de usabilidad con personas usuarias reales | RT-13.03; Art. 26° | Propuesta técnica |
| Indicadores de usabilidad (tiempo, pasos, tasa de error, aprendizaje por perfil) | RT-13.04; Art. 26° | Propuesta técnica |
| Matriz de navegadores y política de actualización | RT-13.10; Art. 26° | Propuesta técnica |
| Matriz de cumplimiento sobre todos los RT | Formulario T-12 | Entregable 24, Sobre N° 2 |

## Continuación: pantallas de Prioridad 3 (03-11-2026)

Repetido el barrido de 49 rutas reales en los cinco tamaños exigidos: 245 combinaciones, sin errores de JavaScript ni desplazamiento horizontal de página. Se corrigieron stepper, OTP y enlaces táctiles. Para las diez pantallas intervenidas, se revisó el contraste del texto HTML en claro, oscuro y alto contraste (200 combinaciones); esta medición no cubre SVG, imágenes ni todos los estados de interacción.

Las funciones de Prioridad 3 tienen pruebas reproducibles en `verify.cjs`; alcance, resultados y límites en `verificacion_prioridad3.md`. No constituye el informe formal de accesibilidad ni cierra los pendientes documentales de esta lista.

## 9. Pendientes detectados

| Punto | Pantalla o ruta | Observación | Responsable |
|---|---|---|---|
| RT-25.06 | Todo el sitio | ✓ Publicado en https://patricioh315.github.io/LafroX/ | |
| RT-25.07 | Todo el sitio | Seis meses de acceso: no demostrable en la entrega; se acredita con publicación estable | |
| RT-25.03 | `/flujo`, pasos | ✓ Corregido: botones del paso a paso a 44 px | |
| RNF-05.02 | `/flujo?paso=4` | ✓ Corregido: «Cerrar misión» a 60 px (≈ 15,9 mm) | |
| RT-13.01 | Documento aparte | Informe de conformidad WCAG con pruebas automáticas y manuales | |
| RT-25.10 (deseable) | Documento aparte | Exportar el prototipo para revisión sin conexión | |
