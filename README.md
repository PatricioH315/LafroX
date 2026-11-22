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

## Antecedentes simulados del Art. 39 (`antecedentes/`)

Recreaciones con formato de documento chileno real, datos ficticios y marca de agua «SIMULACIÓN ACADÉMICA» en cada página. Los documentos privados imitan su formato real; los certificados estatales copian solo la estructura, sin emblemas, sellos ni códigos de verificación. El notario es ficticio (`\SIMtimbrenotarial`).

| Art. 39 | Carpeta | Documento |
|---|---|---|
| 1 | `1-legales/02-cedula-representante` | Fotocopia legalizada de la cédula (`-v2`: hoja de datos simulada; la versión con escaneo real es `LAFROX-Cedula-Representante-Legal.tex`) |
| 1 | `1-legales/03-rut-empresa` | Rol Único Tributario |
| 1 | `1-legales/04-certificado-vigencia` | Certificado de vigencia de la sociedad |
| 1 | `1-legales/05-patente-comercial` | Patente comercial legalizada |
| 1 | `1-legales/06-escritura-constitucion` | Escritura de constitución y modificaciones |
| 1 | `1-legales/07-poderes-representante` | Poderes vigentes del representante legal |
| 1 | `1-legales/08-individualizacion-socios` | Individualización de los socios |
| 2 | `2-financieros/09-deuda-tributaria` | Certificado de deudas tributarias |
| 2 | `2-financieros/10-estados-financieros` | Estados financieros auditados 2023–2025 |
| 2 | `2-financieros/11-antecedentes-comerciales` | Certificado de antecedentes comerciales |
| 2 | `2-financieros/12-boletin-laboral` | Boletín Laboral y Previsional (DT) |
| 2 | `2-financieros/13-certificado-bancario` | Certificado bancario de capacidad de garantías |
| 3 | `3-declaraciones/15-dj-no-quiebra` | DJ de no encontrarse en quiebra ni reorganización |
| 3 | `3-declaraciones/18-domicilio-valparaiso` | Constitución de domicilio en Valparaíso |
| 4 | `4-tecnicos/19-carta-presentacion-contratos` | Carta de presentación, nómina de contratos y cartas de referencia |
| 4 | `4-tecnicos/20-cartas-compromiso` | Cartas compromiso de socios y proveedores |
| 4 | `4-tecnicos/23-certificaciones` | Certificaciones institucionales y de fabricante |

Datos comunes en `antecedentes/datos-proponente.tex`; base visual en `antecedentes/sim-oficial.sty`; modelos públicos consultados en `antecedentes/referencias/` (`FUENTES.md`). Compilar con `bash antecedentes/compilar.sh`. Aún no entran en la foliación de `compilar_sobre1.py` ni en el índice A-5.

## Pendiente para completar el sobre (Art. 39)

Integrar los antecedentes simulados a la foliación y al índice A-5, y la Boleta de Garantía de Seriedad (Art. 35). Dos subdocumentos ya anuncian documentos para este sobre: el Subdocumento 1 (sección 1.4: certificados y cartas de referencia del Art. 34) y el Subdocumento 12 (Anexo 12.D: cartas de compromiso firmadas del equipo). Los Formularios A-2, A-3 y A-4 van firmados ante notario. Si se agrega el Subdocumento 14, su declaración de uso de IA se suma al A-6 con `herramientas/consolidar_a6.py`.
