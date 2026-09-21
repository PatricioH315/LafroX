# CLAUDE.md

Puntero rápido para quienes usan Claude Code con este repositorio.

## Reglas de oro

1. **Fuente de verdad**: los documentos de `Bases/` (todas las decisiones se derivan de ahí). Lee primero `AGENTS.md`.
2. **Idioma**: todo el trabajo es documentación tipo oferta en **español**.
3. **Precedencia** (Art. 5° Bases Administrativas): `Bases_Administrativas.md` > `Bases_Tecnicas_Transversales.md` > `Caso_02_Logistica.md`. El caso puede endurecer requisitos transversales, nunca rebajarlos.
4. **Cronograma 56 meses innegociable** y **despliegue híbrido obligatorio** (nube + on-premise). No se aceptan propuestas solo-nube ni solo-on-premise.
5. **Estructura por subdocumento (T-7)**: el repositorio se organiza según los **14 subdocumentos** del Formulario T-7, no por entregas. Cada carpeta `NN_...` es un subdocumento y adentro conviven `entrega_1/` (congelada), `entrega_2/` (en construcción), etc.
6. **Snapshots congelados**: cualquier `entrega_1/` es el registro del Informe 1 entregado el 07-09-2026 y **no se edita**. El trabajo ocurre en `entrega_2/` y todo cambio se registra en `00_trazabilidad_observaciones/` (Art. 45). El criterio de qué se conserva es `Productos/Informe 1 Entrega 1.docx`. 
7. **Caso 02 — Logística (Distribuidora Puelche S.A.)**: el caso NO es una especificación de requerimientos. Traducir su narrativa en alcance, arquitectura, plan y estrategia es exactamente lo evaluado. Ejes: trazabilidad sanitaria, OTIF y costo de servir.

## Estructura

**14 subdocumentos** al root (numeración exacta del Formulario T-7):

`01_presentacion_empresa/` · `02_problema_necesidad/` · `03_esquema_solucion_alcance/` · `04_arquitectura/` (lógica y física juntas) · `05_modelo_datos/` · `06_metodologias/` · `07_plan_trabajo_edt/` · `08_plan_riesgos/` · `09_plan_calidad/` · `10_operacion_niveles_servicio/` · `11_planes_operacion/` · `12_equipo_subcontrataciones/` · `13_innovaciones/` · `14_ventajas_beneficios_consolidacion/`.

Cada subdocumento contiene un `README.md` con lo que exige T-7 y `entrega_1/entrega_2/` con el trabajo.

**Transversales**:

- `00_trazabilidad_observaciones/` — bitácora de observaciones y respuestas entre entregas + manifiestos de extracción.
- `Bases/` — documentos rectores.
- `Requerimientos/` — catálogos RF/RNF, decisiones, reglas de negocio y supuestos.
- `Arquitectura/logica/` y `Arquitectura/fisica/` — documentos fuente de arquitectura (no entregables).
- `Diagramas/` — biblioteca completa (los 15 diagramas del Informe 1 más el material de trabajo).
- `Formularios/` — formularios técnicos y económicos.
- `Rúbricas/` — rúbricas de calificación por entregable.
- `Productos/` — el `.docx` de la Entrega 1, formularios T-12, presentación y narración.
- `Trabajos Anteriores/` — solo referencia de **forma**, no de contenido.
- `_staging/` — archivos en tránsito, no versionado.

## Cómo instalar las skills equivalentes

El proyecto de opencode versiona sus skills en `.opencode/skills/` y quedan instaladas al clonar, sin depender de la config global de cada máquina. No se requieren steps adicionales una vez clonado el repo.

> Consulta `AGENTS.md` para el detalle completo de reglas, habilidades, materias a investigar y renderizado de diagramas.
