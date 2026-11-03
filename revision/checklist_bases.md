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
- [ ] Es un prototipo interactivo de **alta fidelidad** (Cap. 25.1).
- [ ] Se entrega como **enlace navegable en línea** (RT-25.06).
- [ ] Funciona **sin instalación ni complementos** (RT-25.06).
- [ ] Es compatible con los **navegadores modernos vigentes** (RT-25.06).
- [ ] El acceso está garantizado por **al menos seis meses** desde la entrega (RT-25.07).
- [ ] Simula de forma realista la navegación y los flujos sin servicios de fondo ni base de datos (Cap. 25.1).
- [ ] Permite recorrerlo **desde la perspectiva de los distintos perfiles** de personas usuarias (Cap. 25.1).
- [ ] Deseable: se puede exportar a un documento interactivo para revisión **sin conexión** (RT-25.10).

## 2. Alcance mínimo (Cap. 25.2)

### 2.1 Portal principal

- [ ] Página de inicio pública.
- [ ] Página de inicio con sesión iniciada, **personalizada por perfil**.
- [ ] Tablero principal con **componentes configurables**.
- [ ] Menú de navegación completo y funcional.
- [ ] Rastro de navegación (migas de pan).
- [ ] Navegación contextual.

### 2.2 Autenticación e incorporación

- [ ] Pantalla de inicio de sesión **unificada**.
- [ ] Registro de una persona usuaria externa en **al menos cinco pasos**.
- [ ] Recuperación de acceso.
- [ ] Segundo factor de autenticación.
- [ ] Tablero de primer ingreso con **recorrido guiado**.

### 2.3 Proceso operacional principal

- [ ] Flujo de negocio central del caso, **de extremo a extremo**.
- [ ] Tiene **al menos seis pasos**, desde el inicio hasta el cierre.
- [ ] Muestra los **estados intermedios**.
- [ ] Incluye el manejo de la **excepción más frecuente**.

### 2.4 Proceso operacional secundario

- [ ] Listado.
- [ ] Vista de detalle.
- [ ] Creación.
- [ ] Flujo de aprobación **visual**.

### 2.5 Perfil de terreno u operación

- [ ] Vista que usa la persona operacional en su puesto real.
- [ ] Versión **móvil**.
- [ ] Comportamiento **sin conexión**, si el caso lo requiere.

### 2.6 Gestión de terceros

- [ ] Directorio de la contraparte externa (clientes, proveedores u otra).
- [ ] Ficha completa.
- [ ] Evaluación.
- [ ] Historial.

### 2.7 Tablero analítico

- [ ] Indicadores principales con visualizaciones.
- [ ] **Al menos seis tipos de gráfico distintos**.
- [ ] Filtro por **período**.
- [ ] Filtro por **categoría**.
- [ ] Profundización desde el indicador **hasta el detalle**.
- [ ] Exportación de informes.

### 2.8 Administración

- [ ] Gestión de personas usuarias.
- [ ] Gestión de roles y permisos.
- [ ] Parametrización.
- [ ] Consulta de auditoría.

### 2.9 Módulos adicionales

- [ ] Primer módulo adicional pertinente al caso.
- [ ] Segundo módulo adicional pertinente al caso.

## 3. Principios de diseño exigidos

### RT-25.01 · Navegación intuitiva (también RT-13.05)

- [ ] Se usa sin necesidad de manual.
- [ ] Toda funcionalidad principal se alcanza en **tres interacciones o menos** desde el inicio del perfil.

### RT-25.02 · Retroalimentación (también RT-13.06)

- [ ] Hay retroalimentación visual clara ante **cada acción**.
- [ ] Hay estados de carga y transiciones fluidos.
- [ ] Los errores indican **qué ocurrió y qué hacer**.
- [ ] No hay mensajes técnicos dirigidos a la persona usuaria final.

### RT-25.03 · Accesibilidad WCAG 2.2 AA (también RT-13.01, RT-13.07, RT-13.11; Art. 26°)

- [ ] Contraste adecuado (texto 4,5:1; texto grande y controles 3:1).
- [ ] Tamaños de fuente legibles.
- [ ] Objetivos táctiles de **al menos 44 × 44 px**.
- [ ] Navegación **completa por teclado**.
- [ ] Orden de foco lógico.
- [ ] Atajos de teclado para operaciones frecuentes (RT-13.11).
- [ ] Textos alternativos en imágenes y gráficos.
- [ ] Etiquetas de accesibilidad en controles.
- [ ] Iconografía acompañada de texto (RT-13.07).
- [ ] Flujos guiados paso a paso para baja alfabetización digital (RT-13.07).
- [ ] Alto contraste disponible (RT-13.07).
- [ ] Verificado con herramientas automatizadas **y** pruebas manuales (RT-13.01; Art. 26°).

### RT-25.04 · Diseño responsivo (también RT-13.02)

- [ ] Escritorio **1920 × 1080**.
- [ ] Escritorio **1366 × 768**.
- [ ] Tableta **768 × 1024 vertical**.
- [ ] Tableta **1024 × 768 horizontal**.
- [ ] Teléfono **375 × 812**.
- [ ] Puntos de quiebre coherentes.
- [ ] El contenido se adapta, no solo se reduce (RT-13.02).

### RT-25.05 · Sistema de diseño documentado (también RT-13.09)

- [ ] Paleta de **a lo más cinco colores principales**.
- [ ] **A lo más dos familias tipográficas**, jerarquizadas.
- [ ] Iconografía coherente.
- [ ] Retícula y espaciado consistentes.
- [ ] Componentes reutilizables.
- [ ] El sistema está **documentado** (entregable 17 y RT-25.05).

### Interfaces de terreno (RT-13.08, según caso; Art. 26°)

- [ ] Usable con guantes (objetivos amplios).
- [ ] Legible a la intemperie y con luminosidad variable.
- [ ] Funciona sin conexión.

### Deseable (RT-13.12)

- [ ] Modo oscuro.
- [ ] Personalización de la interfaz por persona usuaria.

## 4. Componentes de interfaz obligatorios (Cap. 25.4)

### Navegación

- [ ] Menú principal.
- [ ] Menú secundario contextual.
- [ ] Rastro de navegación.
- [ ] Paginación.
- [ ] Pestañas.
- [ ] Acordeones.
- [ ] Navegación por pasos.
- [ ] Menú de acciones rápidas.

### Formularios

- [ ] Campos de texto con validación en tiempo real.
- [ ] Selectores y desplegables.
- [ ] Casillas de verificación.
- [ ] Botones de opción.
- [ ] Selector de fecha.
- [ ] Selector de hora.
- [ ] Carga de archivos con arrastrar y soltar.
- [ ] Autocompletado.
- [ ] Formulario de múltiples pasos.

### Visualización de datos

- [ ] Tabla con ordenamiento.
- [ ] Tabla con filtrado.
- [ ] Gráfico de barras.
- [ ] Gráfico de líneas.
- [ ] Gráfico circular.
- [ ] Tarjetas de información.
- [ ] Línea de tiempo.
- [ ] Indicadores de progreso.
- [ ] Distintivos y etiquetas.
- [ ] Información contextual emergente (tooltip).

### Retroalimentación

- [ ] Mensaje de éxito.
- [ ] Mensaje de error.
- [ ] Mensaje de advertencia.
- [ ] Mensaje de información.
- [ ] Ventanas modales y diálogos.
- [ ] Notificaciones emergentes.
- [ ] Esqueletos de carga.
- [ ] Indicadores de progreso.
- [ ] Estados vacíos **ilustrados**.

### Acción

- [ ] Botón primario.
- [ ] Botón secundario.
- [ ] Botón terciario.
- [ ] Botón de acción flotante.
- [ ] Acciones en línea.
- [ ] Menús contextuales.
- [ ] Acciones masivas.
- [ ] Confirmación de acciones críticas.

## 5. Nivel de interactividad (RT-25.08)

- [ ] Navegación completa entre pantallas.
- [ ] Simulación de ingreso de datos.
- [ ] Transiciones y animaciones básicas.
- [ ] Estados de posado (hover).
- [ ] Estados activos.
- [ ] Simulación de carga de archivos.
- [ ] Elementos desplegables funcionales.
- [ ] Simulación de validaciones.

## 6. Arquitectura de información (RT-25.09)

Se entrega junto al prototipo, como documento aparte.

- [ ] Mapa del sitio completo.
- [ ] Diagrama de navegación.
- [ ] Taxonomía y nomenclatura.
- [ ] Estructura de menús.
- [ ] Jerarquía de la información.

## 7. Causas de penalización (Cap. 25.6)

Cada casilla marcada significa que el riesgo **no** está presente.

- [ ] No hay pantallas estáticas ni no navegables.
- [ ] El diseño está personalizado al caso, no es genérico.
- [ ] No hay incumplimientos de accesibilidad.
- [ ] No hay navegación confusa.
- [ ] No hay **enlaces rotos**.
- [ ] No hay inconsistencias visuales evidentes.
- [ ] Responde bien en **todos** los tamaños exigidos.

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

## 9. Pendientes detectados

| Punto | Pantalla o ruta | Observación | Responsable |
|---|---|---|---|
| | | | |
