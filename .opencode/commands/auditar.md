---
description: Audita los archivos que el usuario acaba de subir contra la integridad del caso; si están correctos, los consolida a su carpeta correspondiente. Uso: /auditar <archivo(s)>
---

Audita los archivos recién subidos contra las reglas del caso (Licitación TFEP-01/2026,
Caso 02 — Logística) usando `AUDITORIA.md` como checklist de integridad. NO compilas LaTeX:
esa tarea la ejecuta LafroX personalmente.

## Procedimiento

1. **Identifica los archivos.** Localiza los archivos que el usuario menciona (los que
   haya compartido, o una ruta dada en `$ARGUMENTS`). Si no indica ruta, revisa la carpeta
   `_staging/` (tránsito no versionado por `.gitignore`) y cualquier archivo nuevo sin
   consolidar.

2. **Audita contra el checklist** definido en `AUDITORIA.md` (leerlo primero). Verifica,
   para cada archivo nuevo:
   - **Idioma y propósito**: documento tipo oferta en español, coherente con el giro
     logístico del caso (no retail).
   - **Precedencia** (Art. 5°): `Bases_Administrativas.md` > `Bases_Tecnicas_Transversales.md`
     > `Caso_02_Logistica.md`. El caso puede endurecer un transversal, nunca rebajarlo.
   - **Cifras y volumen del Cap. 15**: 14.200 clientes, 31.000 pedidos-mes, 260.000
     líneas, 2,4 M unidades-mes, 62 preventistas, 96 camiones, 68.000 canastillos /
     9.400 pallets, 14 % pérdida, 2,3 % conteo cíclico, 1,7 % merma, 82,4 % OTIF, etc.
     Ninguna cifra inventada o contradictoria.
   - **Cronograma 56 meses innegociable** (Art. 17): Etapa 1 meses 1–15 (producción
     mes 16), Etapa 2 meses 13–20 (producción mes 21), Operación 21–56.
   - **Despliegue híbrido obligatorio** (Art. 16): nube + on-premise. Sin propuestas
     solo-nube ni solo-on-premise.
   - **5 innovaciones obligatorias**, una por tipo (producto/servicio, proceso,
     tecnológica, modelo de negocio, UX/sostenibilidad), trazables con arquitectura,
     EDT y flujo de caja.
   - **Códigos RT contra el documento transversal correcto** (no los mal mapeados del
     Caso Cap. 15): RT-03.23 (no 03.24), RT-03.12 (no 03.13), RT-16.10 (no 05.10), y
     RT-06.01 solo para tipología/aislamiento, no disponibilidad.
   - **Decisiones 16.1**: los supuestos/reglas de negocio deben ser coherentes con las
     16 decisiones del numeral 16.1 (stock, crédito, excursión térmica, reintento,
     devoluciones, envases, precio, OTIF).
   - **Trazabilidad**: si el archivo introduce requerimientos RF/RNF, que referencie su
     origen (párrafo, entrevista, indicador o restricción) y su RT.
   - **Inconsistencias a consulta**: no resolver unilateralmente incoherencias de las
     Bases; señalar como candidata a consulta Art. 43.3 / supuesto.

3. **Registra el resultado en `AUDITORIA.md`.** Agrega una entrada en el registro de
   auditorías con: fecha, archivo(s), rol responsable (si se conoce), veredicto
   (CORRECTO / REQUIERE CAMBIOS), y observaciones por regla incumplida.

4. **Consolida solo si está correcto.** Si el veredicto es CORRECTO y el archivo está en
   `_staging/` (o sin carpeta definitiva), muévelo a su carpeta correspondiente según la
   estructura del repositorio:
   - Documentos rectores / propuestas / consultas → `productos/`.
   - Requerimientos, supuestos, reglas de negocio, trazabilidad → `Requerimientos/`.
   - Diagramas exportados → `Diagramas/`.
   - Fuente de diagramas y documentación → raíz o carpeta del tema.
   Aplica el prefijo/nomenclatura de nomenclatura de archivo (Art. 43.3) si corresponde.

5. **No compiles LaTeX.** Responde marcando el veredicto y qué se movió a dónde (o qué
   debe corregir el responsable), para que cada compañero sepa el estado de su trabajo.