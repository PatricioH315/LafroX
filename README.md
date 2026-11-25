# Sobre N.° 1 — Antecedentes del Oferente

El Sobre N.° 1 reúne los 23 antecedentes de los cuatro grupos del artículo 39 de las Bases Administrativas y la declaración jurada simple de veracidad del sitio web corporativo exigida en el capítulo 23.3 de las Bases Técnicas Transversales, y cierra con la Boleta de Garantía de Seriedad de la Oferta (Art. 35). El Formulario A-5 abre el sobre; los demás documentos siguen el orden del artículo 39, sin repetir A-5 en el grupo técnico. La foliación es única para el conjunto.

## Documentos incluidos

Las rutas siguientes identifican los PDF que integran el índice A-5. Los folios de inicio y término vigentes se generan en `folios.tex` y se imprimen en `LAFROX-Formulario-A-5.pdf`.

| N.° | Documento | PDF |
|---|---|---|
| 1 | Formulario A-5: Presentación e índice de antecedentes | [LAFROX-Formulario-A-5.pdf](LAFROX-Formulario-A-5.pdf) |
| 2 | Formulario A-1: Identificación del Proponente y de su Representante | [LAFROX-Formulario-A-1.pdf](LAFROX-Formulario-A-1.pdf) |
| 3 | Cédula de identidad del representante legal | [LAFROX-Cedula-Representante-Legal.pdf](LAFROX-Cedula-Representante-Legal.pdf) |
| 4 | Rol Único Tributario de la empresa | [LAFROX-RUT.pdf](antecedentes/1-legales/03-rut-empresa/LAFROX-RUT.pdf) |
| 5 | Certificado de vigencia de la sociedad | [LAFROX-Vigencia.pdf](antecedentes/1-legales/04-certificado-vigencia/LAFROX-Vigencia.pdf) |
| 6 | Patente comercial | [LAFROX-Patente.pdf](antecedentes/1-legales/05-patente-comercial/LAFROX-Patente.pdf) |
| 7 | Escritura de constitución y modificaciones | [LAFROX-Escritura.pdf](antecedentes/1-legales/06-escritura-constitucion/LAFROX-Escritura.pdf) |
| 8 | Poderes vigentes del representante | [LAFROX-Poderes.pdf](antecedentes/1-legales/07-poderes-representante/LAFROX-Poderes.pdf) |
| 9 | Individualización de socios | [LAFROX-Socios.pdf](antecedentes/1-legales/08-individualizacion-socios/LAFROX-Socios.pdf) |
| 10 | Certificado de deudas tributarias | [LAFROX-DeudaTributaria.pdf](antecedentes/2-financieros/09-deuda-tributaria/LAFROX-DeudaTributaria.pdf) |
| 11 | Estados financieros auditados 2023–2025 | [LAFROX-EEFF.pdf](antecedentes/2-financieros/10-estados-financieros/LAFROX-EEFF.pdf) |
| 12 | Certificado de antecedentes comerciales | [LAFROX-AntecedentesComerciales.pdf](antecedentes/2-financieros/11-antecedentes-comerciales/LAFROX-AntecedentesComerciales.pdf) |
| 13 | Antecedentes laborales y previsionales | [LAFROX-BoletinLaboral.pdf](antecedentes/2-financieros/12-boletin-laboral/LAFROX-BoletinLaboral.pdf) |
| 14 | Capacidad bancaria de emisión de garantías | [LAFROX-CertificadoBancario.pdf](antecedentes/2-financieros/13-certificado-bancario/LAFROX-CertificadoBancario.pdf) |
| 15 | Formulario A-2: No afectación por prohibiciones e inhabilidades | [LAFROX-Formulario-A-2.pdf](LAFROX-Formulario-A-2.pdf) |
| 16 | Declaración de no quiebra ni reorganización | [LAFROX-NoQuiebra.pdf](antecedentes/3-declaraciones/15-dj-no-quiebra/LAFROX-NoQuiebra.pdf) |
| 17 | Formulario A-3: Aceptación íntegra de las Bases | [LAFROX-Formulario-A-3.pdf](LAFROX-Formulario-A-3.pdf) |
| 18 | Formulario A-4: Ausencia de conflictos de interés | [LAFROX-Formulario-A-4.pdf](LAFROX-Formulario-A-4.pdf) |
| 19 | Constitución de domicilio en Valparaíso | [LAFROX-Domicilio.pdf](antecedentes/3-declaraciones/18-domicilio-valparaiso/LAFROX-Domicilio.pdf) |
| 20 | Carta de presentación y nómina de contratos similares | [LAFROX-CartaPresentacion.pdf](antecedentes/4-tecnicos/19-carta-presentacion-contratos/LAFROX-CartaPresentacion.pdf) |
| 21 | Cartas compromiso de socios, subcontratistas y proveedores clave | [LAFROX-CartasCompromiso.pdf](antecedentes/4-tecnicos/20-cartas-compromiso/LAFROX-CartasCompromiso.pdf) |
| 22 | Formulario A-6: Declaración de uso de IA generativa | [LAFROX-Formulario-A-6.pdf](LAFROX-Formulario-A-6.pdf) |
| 23 | Certificaciones institucionales y de fabricante | [LAFROX-Certificaciones.pdf](antecedentes/4-tecnicos/23-certificaciones/LAFROX-Certificaciones.pdf) |
| 24 | Declaración jurada simple de veracidad del sitio web corporativo | [LAFROX-DeclaracionWeb.pdf](antecedentes/4-tecnicos/24-dj-sitio-web/LAFROX-DeclaracionWeb.pdf) |
| 25 | Boleta de Garantía de Seriedad de la Oferta (Art. 35) | [LAFROX-BoletaSeriedad.pdf](antecedentes/5-garantias/35-boleta-seriedad/LAFROX-BoletaSeriedad.pdf) |

## Compilación y control de folios

Desde la raíz de este checkout:

```sh
python compilar_sobre1.py
```

Requiere LuaLaTeX y PyMuPDF. El script estabiliza la extensión del A-5, compila los 23 documentos y recalcula la foliación hasta que sus longitudes no cambian. Al terminar comprueba que cada página de cada PDF tenga exactamente el folio esperado y que la secuencia no tenga saltos ni duplicados. No compilar los documentos sueltos con un `folios.tex` de otra versión.

Los documentos conservan sus carpetas. El nombre base de cada PDF es único; A-5 lo identifica y este cuadro permite localizar su ruta completa. `antecedentes/compilar.sh` conserva el uso de compilación individual de complementarios, pero no sustituye la integración y validación mediante el script principal.

## Datos comunes

- La cédula y el cargo confirmados para Alex Aravena están en `identidad-representante.tex`: 21.529.759-4 y Jefe de Proyecto y Apoderado. Formularios y complementarios usan ese mismo archivo.
- Los datos de empresa y portadas de los formularios se configuran en `lafrox.cls` y `sobre1-comun.tex`; los restantes datos simulados de complementarios, en `antecedentes/datos-proponente.tex`.
- `antecedentes/sim-oficial.sty` aplica el folio correlativo a los complementarios. Conserva la identificación de documento simulado, datos ficticios y ausencia de validez legal. Reutiliza la firma gráfica ya existente de Alex en la media firma de cada página; no añade autorizaciones notariales.
- Las declaraciones de uso de IA de los documentos de origen se reúnen en `formulario-a6/filas.tex`; `herramientas/consolidar_a6.py` permite regenerar esa consolidación. Regenerar requiere comprobar las revisiones humanas efectivamente declaradas.

## Cédula del representante

Mientras no exista `documentos-adjuntos/cedula-representante-legal.pdf`, el índice incorpora la recreación de datos `LAFROX-Cedula-Representante-Legal-v2.pdf`. Si se aporta el escaneo, el compilador lo reemplaza por el documento raíz `LAFROX-Cedula-Representante-Legal.pdf`, sin duplicar el antecedente, y vuelve a calcular los folios. La recreación no acredita una fotocopia auténtica legalizada.

## Simulación notarial y cartas de proveedores

A-2, A-3 y A-4 incorporan la imagen ficticia aportada por el usuario, guardada sin alteraciones como `firma notario.jpeg`, junto a la leyenda «Constancia notarial simulada». Se conserva la firma de Alex como declarante. Esto completa su representación documental dentro de la simulación; no acredita una autorización notarial real. Por petición posterior del usuario, la firma gráfica existente de Alex Aravena se reutiliza en todas las medias firmas de los complementarios y en los bloques de firma de sus cinco documentos propios: socios, estados financieros, no quiebra, domicilio y carta de presentación. Las firmas de notarios, auditores, bancos y proveedores no se sustituyen por la del representante.

Los antecedentes simulados no constituyen certificaciones, auditorías, actuaciones notariales ni compromisos reales. Se retiraron referencias al curso y a fines académicos del texto impreso, conservando explícitamente la simulación; las firmas de Alex reutilizan el recurso gráfico existente y la constancia notarial usa únicamente la imagen ficticia aportada por el usuario.

La Boleta de Garantía de Seriedad de los artículos 35 y 49.2 está en `antecedentes/5-garantias/35-boleta-seriedad/LAFROX-BoletaSeriedad.pdf` (USD 500.000, vence el 30-04-2027). Es adicional a los 23 antecedentes del artículo 39 y no se sustituye por el certificado bancario. Cierra la foliación del sobre (N.° 25 del índice A-5, orden del Art. 49.2) y se entrega en original impreso (Art. 35.5). El documento laboral distingue F30 (antecedentes del Boletín Laboral y Previsional) de F30-1. La nómina de experiencia reproduce los once campos del T-6 vigente y sus cartas simuladas ya no contradicen esos montos, SLA y arquitectura; se retiraron remisiones a facturas ausentes. Las Bases no fijan antigüedad máxima para la individualización de socios. El usuario confirmó que Alex Aravena revisó las correcciones y su nombre quedó registrado en A-6. Las cuatro alianzas se ajustaron al alcance de SD12/T-8; las cartas incompatibles de montaje externo y colocation se conservaron sólo en el respaldo de revisión.

El antecedente 21 incorpora tres cartas con el mismo formato de las cuatro alianzas: Rom Mayer para la instalación de Talca y la revisión eléctrica semestral, Netprovider para las pruebas independientes y Telsur como proveedor clave de fibra de Talca y Concepción. Las dos primeras corresponden a los siete servicios declarados en SD12 y T-8 y su contratación requiere autorización previa y escrita del CLIENTE. Las cartas son simuladas y no acreditan compromisos reales.

Si se requirieran documentos auténticos fuera del ejercicio, las recreaciones y sellos simulados no sustituirían certificados ni actuaciones reales. El conjunto compilado contiene 25 PDF y 96 folios: A-5 en 1–5; A-1 en 6–9; cédula en 10; carta y nómina en 48–52; cartas compromiso en 53–60; A-6 en 61–85; certificaciones en 86–94; declaración del sitio web en 95; boleta de garantía en 96.

## Carátula física del sobre (Art. 49.1)

La carátula exterior del Sobre N.° 1 cerrado se compila desde `LAFROX-Caratula-Sobre1.tex` → [LAFROX-Caratula-Sobre1.pdf](LAFROX-Caratula-Sobre1.pdf) (1 página tamaño carta, sin folio, firmada por el representante legal conforme al Art. 40.2). Va adherida por fuera del sobre físico y no entra en la secuencia de folios del índice A-5.
