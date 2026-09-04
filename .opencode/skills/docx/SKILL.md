---
name: docx
description: Creación y edición de documentos Word (.docx) de la propuesta LafroX: formularios oficiales de los sobres, plantillas del mandante, consultas al mandante (Art. 43.3) y documentos tipo oferta. Usar cuando el usuario pida crear/modificar .docx, formularios oficiales, sobres, plantillas o consultas al mandante del proyecto.
---

# DOCX (documentos Word de la licitación)

Generación y edición de los `.docx` del proyecto LafroX. Idioma español,
formato documento tipo oferta.

## Herramientas

- Python con `python-docx` para crear/editar `.docx`.
- Respetar plantillas oficiales: si existe un formulario dado por el mandante,
  llenar sus campos sin alterar estructura, logos ni numeración.
- No modificar secciones que no correspondan; marcar lo pendiente explícitamente.

## Usos en el proyecto

- **Consultas al mandante** (Art. 43.3): cada inconsistencia de las Bases que no
  se resuelva unilateralmente → consulta formal. Nomenclatura FEP/TFEP y tabla de
  consultas coherente con la planilla general.
- **Formularios de los sobres** (Cap. 3 Bases Admin): oferta técnica, oferta
  económica, anexos. Llenar según las Bases Administrativas.
- **Informes T-22**: los informes y presentaciones del calendario, con los
  subdocumentos que exige cada informe (p. ej. Subdoc 3 "esquema de solución y
  alcance", Subdoc 5 "modelo y gestión de datos").
- **Acuse de recibo / presentaciones de propuesta** si aplica al proceso.

## Reglas

- Reglas de negocio y supuestos viven dentro del registro de requerimientos
  (Cap. 17.1), no como capítulos aparte del informe.
- Antes de exportar un `.docx` a PDF, verificar codificación, tablas y que las
  imágenes de `Diagramas/` estén incrustadas.