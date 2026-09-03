# CLAUDE.md

Puntero rápido para quienes usan Claude Code con este repositorio.

## Reglas de oro

1. **Fuente de verdad**: los documentos de `Bases/` (todas las decisiones se derivan de ahí). Lee primero `AGENTS.md`.
2. **Idioma**: todo el trabajo es documentación tipo oferta en **español**.
3. **Precedencia** (Art. 5° Bases Administrativas): `Bases_Administrativas.md` > `Bases_Tecnicas_Transversales.md` > `Caso_02_Logistica.md`. El caso puede endurecer requisitos transversales, nunca rebajarlos.
4. **Cronograma 56 meses innegociable** y **despliegue híbrido obligatorio** (nube + on-premise). No se aceptan propuestas solo-nube ni solo-on-premise.
5. **Caso 02 — Logística (Distribuidora Puelche S.A.)**: el caso NO es una especificación de requerimientos. Traducir su narrativa en alcance, arquitectura, plan y estrategia es exactamente lo evaluado. Ejes: trazabilidad sanitaria, OTIF y costo de servir.

## Estructura

- `Bases/` — documentos rectores
- `Requerimientos/` — planillas Excel de requerimientos
- `productos/` — salidas entregables (consultas, planilla Art. 43.3, decisiones)
- `TrabajosAnteriores/` — solo referencia de **forma**, no de contenido
- `Diagramas/` — exportados de Mermaid/PlantUML
- `_staging/` — archivos pendientes de consolidar en el repo

## Cómo instalar las skills equivalentes

El proyecto de opencode versiona sus skills en `.opencode/skills/` y quedan instaladas al clonar, sin depender de la config global de cada máquina. No se requieren steps adicionales una vez clonado el repo.

> Consulta `AGENTS.md` para el detalle completo de reglas, habilidades, materias a investigar y renderizado de diagramas.
