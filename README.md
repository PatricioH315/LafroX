# LafroX — formato del Subdocumento 11

Rama: `LafroX-Subdoc11-LateX-CORRIGIENDO`, creada desde `LafroX-Subdoc11-LateX`, commit `3faaec7ac6ab05a2bb7c0b7187584ad59b0b81e4`.

## Alcance

Plantilla de presentación del SD11. Incluye portada, índice enlazado, jerarquía, foliación, zonas de firma, referencias y declaración de IA. Los textos breves delimitan el tema de cada apartado; no constituyen los planes técnicos ni acreditan cumplimiento. No contiene dimensionamientos, mediciones, presupuestos de capacidad ni compromisos inventados. No está lista para entrega.

Se revisó la rama SD12 CORRIGIENDO `a33dea8` solo como referencia visual. No se incorporan su contenido, organigrama, dotación, T-8 ni anexos. La rama original de SD11 solo contenía el formato genérico y el ejemplo; se conserva ese ejemplo fuera de la compilación para no eliminar material heredado.

## Índice específico

- 11 Introducción a los Planes en operación.
- 11.1 Plan Mantención Preventiva / Evolutiva.
  - 11.1.1 Plan de mantención y presupuesto de capacidad.
  - 11.1.2 Actualización de dependencias, deuda técnica y obsolescencia.
- 11.2 Plan Servicios de Operación.
  - 11.2.1 Ingeniería de confiabilidad.
  - 11.2.2 Gestión de capacidad y prácticas FinOps.
  - 11.2.3 Pruebas de recuperación ante desastres y resiliencia.
- Referencias.
- Declaración de uso de IA.

Son **dos apartados obligatorios** y **cinco subtítulos de menor nivel elegidos para ordenar el desarrollo**. Las aclaraciones no fijan la cantidad de subtítulos adicionales. No existe un 11.3. SD11 no tiene formulario anexo obligatorio asignado en el índice comunicado. Si se necesitan anexos, se desarrollan en un archivo separado; no se crean archivos vacíos de anexos o formularios. Las listas de figuras y tablas se incorporarán cuando existan objetos de contenido técnico reales; no se generan listas vacías para imitar SD12.

## Presentación

- Carta vertical; cuerpo 11 pt, tablas 9,5 pt y figuras mínimo 9 pt.
- Márgenes corporativos heredados: superior 2,9 cm; inferior 3 cm; izquierdo 3,1 cm; derecho 2,7 cm. Son decisiones de plantilla, no cifras impuestas por las Bases.
- Source Serif 4 en cuerpo; Source Sans 3 en títulos; interlineado 1,10.
- Portada identificada como propuesta técnica, SD11, TFEP-01/2026, Caso 02 — Logística, Sobre 2 y LafroX.
- Foliación arábiga correlativa desde la portada (1), abajo a la derecha, sin reinicio en el capítulo.
- Zona de firma completa en portada y zona de media firma abajo a la derecha en todas las páginas, incluida portada. Se reservan espacios; no se copia ni fabrica una firma.
- Se conservan los datos corporativos heredados de la plantilla, sin certificarlos ni investigar su veracidad. Deben ser confirmados antes de la entrega.
- Fecha de emisión de la plantilla: 20 de noviembre de 2026; no se fija fecha de entrega ni nomenclatura ZIP con una fecha no confirmada.
- Nombre del PDF: `LAFROX-Subdocumento11.pdf`.
- Cierre con Referencias y Declaración de uso de IA, sin numeración, en ese orden.
- Revisión humana: `[[REVISIÓN HUMANA]]`; no se atribuye revisión a integrantes.

## Compilar

Desde este checkout, ejecutar LuaLaTeX sobre `LAFROX-Subdocumento11.tex` hasta estabilizar el índice (normalmente tres pasadas):

```powershell
lualatex --interaction=nonstopmode --halt-on-error LAFROX-Subdocumento11.tex
```

`main.tex` es solo una entrada compatible con la plantilla; para generar el PDF con la nomenclatura oficial se usa la raíz nominada. Las notas de desarrollo están en comentarios TeX y en este README, fuera del texto de la oferta.

## Fuentes de forma y contenido futuro

Bases Administrativas, art. 40 y T-7/SD11; Bases Técnicas Transversales, capítulos 3, 7, 10 y 21; comunicado aportado sobre índice obligatorio, secciones 1–7, 9 y capítulo 11. El comunicado del Informe 3 regula la Oferta Económica y no añade títulos a SD11. No se trasladan montos ni estructura económica al capítulo técnico.

Antes de entregar deben desarrollarse los planes con evidencia de la solución, completar las referencias con las páginas de las fuentes entregables, confirmar identidad, incorporar firmas efectivas y registrar la revisión humana real.

## Verificación de la plantilla

PDF de seis páginas revisado visualmente en todas sus páginas. Verificados papel carta, folios 1–6, once enlaces de índice y sus marcadores, correspondencia del 11.2 con el folio 4, ausencia de errores y avisos de compilación, y zonas de firma en cada página. La plantilla no acredita cumplimiento técnico ni aprobación humana.
