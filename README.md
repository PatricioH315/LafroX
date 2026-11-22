# Sobre N.° 1 — Antecedentes del Oferente

Documentos administrativos del Sobre N.° 1 (Bases Administrativas, Arts. 39, 48 y 49). Por ahora contiene los seis formularios del Anexo A, con foliación correlativa en todo el sobre.

| Folios | Archivo | Contenido |
|---|---|---|
| 1–4 | `LAFROX-Formulario-A-5.pdf` | Presentación e índice de antecedentes (abre el sobre, Art. 40.3) |
| 5–9 | `LAFROX-Formulario-A-1.pdf` | Identificación del Proponente y de su Representante |
| 10–12 | `LAFROX-Formulario-A-2.pdf` | Declaración jurada de no afectación por prohibiciones e inhabilidades |
| 13–15 | `LAFROX-Formulario-A-3.pdf` | Declaración de aceptación íntegra de las Bases |
| 16–19 | `LAFROX-Formulario-A-4.pdf` | Declaración de ausencia de conflictos de interés |
| 20–43 | `LAFROX-Formulario-A-6.pdf` | Declaración de uso de IA generativa (SD1 a SD13 y Entregable 2 de la Oferta Económica) |

Los folios cambian si se agrega un documento; el índice A-5 y este cuadro se rigen por `folios.tex`.

## Compilar

```
python compilar_sobre1.py
```

Compila los documentos en el orden del sobre con LuaLaTeX (latexmk), lee el último folio de cada uno y reescribe `folios.tex` hasta que los folios no cambian. No compilar los formularios sueltos con otro `folios.tex`: el folio de inicio de cada documento depende del anterior.

## Datos

- Empresa, RUT, domicilio, representante, cargo, correo y teléfono: `lafrox.cls`, sección 6, iguales a los de todas las portadas.
- Cédula del representante, giro, sitio web, contraparte del proceso: `sobre1-comun.tex`.
- Tabla del A-6: `formulario-a6/filas.tex`, generada por `herramientas/consolidar_a6.py` desde la declaración de uso de IA de cada rama vigente. Si cambia una declaración, se corre `git fetch origin`, luego el script y luego la compilación.

## Cédula de identidad del representante legal

Dejar el escaneo en `documentos-adjuntos/cedula-representante-legal.pdf` y compilar. El script agrega `LAFROX-Cedula-Representante-Legal.pdf` después del A-1 (orden del Art. 39), le pone folio y media firma en cada página y actualiza el índice del A-5.

## Pendiente para completar el sobre (Art. 39)

Antecedentes legales y financieros, declaración de no encontrarse en quiebra, constitución de domicilio, carta de presentación con la nómina de contratos, cartas compromiso de socios y proveedores, certificaciones y la Boleta de Garantía de Seriedad (Art. 35). Dos subdocumentos ya anuncian documentos para este sobre: el Subdocumento 1 (sección 1.4: certificados y cartas de referencia del Art. 34) y el Subdocumento 12 (Anexo 12.D: cartas de compromiso firmadas del equipo). Los Formularios A-2, A-3 y A-4 van firmados ante notario. Si se agrega el Subdocumento 14, su declaración de uso de IA se suma al A-6 con `herramientas/consolidar_a6.py`.
