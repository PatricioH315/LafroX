# Sobre N.° 2 — Oferta Técnica

Rama del Sobre N.° 2 de la Licitación N.° TFEP-01/2026 (Bases Administrativas, Art. 50). Sigue el mismo esquema que `LafroX-Sobre1-LateX`: plantilla `lafrox.cls` y foliación correlativa en todo el sobre (Art. 40).

## Contenido obligatorio (Art. 50.1)

Conforme al Formulario T-7 y a los formularios técnicos del Anexo B. Los subdocumentos se redactan en sus propias ramas (`LafroX-Subdoc<N>-LateX`); esta rama los reúne en el orden del T-7, con folio y media firma en cada página.

## Restricción absoluta (Art. 50.2)

La Oferta Técnica no puede contener precios, tarifas, valores unitarios ni cifra alguna que permita inferir el monto de la oferta económica. Su inclusión es causal de exclusión inmediata.

## Nomenclatura (Art. 50.3)

`SOBRE2_LAFROX_OFERTA_TECNICA_AAAAMMDD.ZIP`

## Compilación y foliación

```
python compilar_sobre2.py --zip
```

- Toma la última versión de cada rama de subdocumento en `origin` y la compila sin modificar sus fuentes: un archivo envoltorio cambia el folio 1 de la portada por el folio que le corresponde a cada documento.
- Orden: hoja resumen (`LAFROX-Sobre2-Indice.pdf`, folio 1) y luego, por subdocumento del T-7, el cuerpo, sus anexos y sus formularios técnicos. La lista está en `FUENTES`, dentro del script.
- Verifica que cada página lleve «Folio N» correlativo y sin saltos, y avisa de las páginas sin media firma.
- Todo queda en `_sobre2/` (no se versiona): la carpeta `SOBRE2_LAFROX_OFERTA_TECNICA_AAAAMMDD/`, el ZIP y un JSON con el commit de cada rama y los folios de cada documento.
- Una segunda ejecución solo recompila los documentos cuya rama o folio inicial cambió.

Correrlo cuando las ramas de los subdocumentos estén cerradas: cualquier página que se agregue o se quite después corre todos los folios siguientes.
