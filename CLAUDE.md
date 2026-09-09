# CLAUDE.md

Puntero rápido para quienes usan Claude Code con este repositorio.

## Reglas de oro

1. **Fuente de verdad**: los documentos de `Bases/` (todas las decisiones se derivan de ahí). Lee primero `AGENTS.md`.
2. **Idioma**: todo el trabajo es documentación tipo oferta en **español**.
3. **Precedencia** (Art. 5° Bases Administrativas): `Bases_Administrativas.md` > `Bases_Tecnicas_Transversales.md` > `Caso_02_Logistica.md`. El caso puede endurecer requisitos transversales, nunca rebajarlos.
4. **Cronograma 56 meses innegociable** y **despliegue híbrido obligatorio** (nube + on-premise). No se aceptan propuestas solo-nube ni solo-on-premise.
5. **Base canónica**: `Entrega 1/` es el registro congelado de lo entregado el 07-09-2026 y el
   **punto de partida obligatorio** de la Entrega 2. No se edita. Todo cambio ocurre en `Entrega 2/`
   y debe quedar registrado en `Entrega 2/00_trazabilidad_observaciones/` (Art. 45). El criterio de
   qué se conserva es `productos/Informe 1 Entrega 1.docx`. El proyecto LaTeX fue retirado por
   desactualizado: no reintroducirlo ni usarlo como fuente.
6. **Caso 02 — Logística (Distribuidora Puelche S.A.)**: el caso NO es una especificación de requerimientos. Traducir su narrativa en alcance, arquitectura, plan y estrategia es exactamente lo evaluado. Ejes: trazabilidad sanitaria, OTIF y costo de servir.

## Estructura

- `Entrega 1/` — **registro congelado** del Informe 1. Base canónica. **Solo lectura.**
- `Entrega 2/` — entregable en construcción para el Informe 2 (05-10-2026). **Aquí se trabaja.**
- `Bases/` — documentos rectores
- `Requerimientos/` — catálogos RF/RNF, decisiones, reglas de negocio y supuestos
- `Arquitectura/logica/` y `Arquitectura/fisica/` — documentos fuente de arquitectura (no entregables)
- `Diagramas/` — biblioteca de diagramas del repositorio (ninguno llegó al Informe 1 entregado)
- `rubricas/` — rúbricas de calificación por entregable
- `productos/` — el `.docx` de la Entrega 1, formularios T-12 y plantilla de informe
- `TrabajosAnteriores/` — solo referencia de **forma**, no de contenido
- `_staging/` — archivos en tránsito, no versionado

## Cómo instalar las skills equivalentes

El proyecto de opencode versiona sus skills en `.opencode/skills/` y quedan instaladas al clonar, sin depender de la config global de cada máquina. No se requieren steps adicionales una vez clonado el repo.

> Consulta `AGENTS.md` para el detalle completo de reglas, habilidades, materias a investigar y renderizado de diagramas.
