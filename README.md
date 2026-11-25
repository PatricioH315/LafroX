# Sobre N.° 3 — Oferta Económica

Rama del Sobre N.° 3 de la Licitación N.° TFEP-01/2026 (Bases Administrativas, Art. 51). Sigue el mismo esquema que `LafroX-Sobre1-LateX`: plantilla `lafrox.cls` y foliación correlativa en todo el sobre (Art. 40).

## Contenido obligatorio (Art. 51.1)

Conforme al Formulario E-21, con sus tres entregables. Los entregables se redactan en las ramas `LafroX-OfertaEconomica-1-Latex` y `LafroX-OfertaEconomica-2-Latex`; esta rama los reúne con folio y media firma en cada página.

## Formato (Art. 51.2)

Valores en CLP, UF y USD; valores netos; IVA desglosado; totales por ítem y total general; tipo de cambio del Formulario E-24. Según el Art. 40.4, el modelo financiero va en XLSX y los documentos 1 y 2 de la Oferta Económica además en DOCX.

## Coherencia (Art. 51.4)

Los valores de los tres entregables deben ser idénticos entre sí y coherentes con la Oferta Técnica. Toda discrepancia no explicada es causal de descalificación.

## Nomenclatura (Art. 51.3)

`SOBRE3_LAFROX_OFERTA_ECONOMICA_AAAAMMDD.ZIP`

## Compilación y foliación

```
python compilar_sobre3.py --externos <carpeta> --zip
```

- Toma la última versión de `LafroX-OfertaEconomica-1-Latex` y `LafroX-OfertaEconomica-2-Latex` en `origin` y las compila sin modificar sus fuentes: un archivo envoltorio cambia el folio 1 de cada portada por el folio que le corresponde.
- Orden: hoja resumen (`LAFROX-Sobre3-Indice.pdf`, folio 1), documento 1 y documento 2. La hoja resumen declara también el modelo financiero (XLSX, sin folios) y los DOCX de los documentos 1 y 2 (Art. 40.4: no se revisan documentos que no consten en el índice).
- Los PDF salen con la nomenclatura del E-21: `LAFROX_OfertaEconomica_1_AAAAMMDD.pdf` y `LAFROX_AnalisisFinanciero_2_AAAAMMDD.pdf`. Avisa si la portada declara otro nombre.
- `--externos` es la carpeta con `LAFROX_ModeloFinanciero_3_AAAAMMDD.xlsx` y los dos DOCX con el mismo nombre que su PDF. Los DOCX se generan desde los PDF ya foliados, para que conserven los folios. Sin esos tres archivos no se arma el ZIP.
- Verifica que cada página lleve «Folio N» correlativo y sin saltos, y avisa de las páginas sin media firma.
- Todo queda en `_sobre3/` (no se versiona): la carpeta `SOBRE3_LAFROX_OFERTA_ECONOMICA_AAAAMMDD/`, el ZIP y un JSON con el commit de cada rama y los folios de cada documento.

Correrlo cuando las ramas de los documentos 1 y 2 estén cerradas: cualquier página que se agregue o se quite después corre los folios siguientes.
