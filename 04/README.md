# Subdocumento 4 — arquitectura consolidada

Esta carpeta reúne las fuentes vigentes de 4.1, 4.2 y 4.3. El contenido está congelado respecto de los commits indicados en `00/trazabilidad/MANIFIESTO.json`: los únicos cambios dentro de los fragmentos son rutas de imágenes.

## Organización

```text
00/
  plantilla/logica/
  plantilla/fisica/
 trazabilidad/
main.tex
main_logica.tex
contenido.tex
compilar.ps1
LAFROX-Subdocumento4.pdf
LAFROX-Subdocumento4.1.pdf
04/
  anexos_logica.tex
  formulario_T11.tex
  anexo_4B.tex
  partes/4.1_logica/
  partes/4.2_fisica/
  partes/4.3_centros_de_datos/
  anexos/logica/
  anexos/fisica/
  formularios/T11/
  figuras/logica/
  figuras/fisica/
  figuras/centros_de_datos/
  figuras/fuentes/
  salida/                 # resultados locales de compilación, no versionados
```

El documento principal conserva el cuerpo lógico y el ensamblado físico original. Este último incluye centros de datos, ADR, referencias, el T-11 provisional y la memoria de cálculo. Los anexos A–V permanecen separados con su catálogo original. No se crean copias editoriales de tablas ni de figuras entre estas raíces.

## Compilación

Requiere una instalación existente de LuaLaTeX con los paquetes utilizados por las clases originales de LafroX. Abrir una terminal en la raíz del repositorio y ejecutar:

```powershell
powershell -ExecutionPolicy Bypass -File .\compilar.ps1
```

También puede compilarse el documento principal manualmente, dos veces o hasta estabilizar referencias:

```text
lualatex --interaction=nonstopmode --halt-on-error --jobname=LAFROX-Subdocumento4 main.tex
```

El script compila los dos main desde la raíz y los complementos desde `04`; crea `04/salida/` para estos últimos. Puede usarse `-SoloMain` para verificar únicamente los dos main. Las salidas relativas a la raíz del repositorio son:

| Fuente | Resultado |
| --- | --- |
| `main.tex` | `LAFROX-Subdocumento4.pdf` |
| `main_logica.tex` | `LAFROX-Subdocumento4.1.pdf` |
| `04/anexos_logica.tex` | `04/salida/LAFROX-Subdocumento4.1-Anexos.pdf` |
| `04/formulario_T11.tex` | `04/salida/LAFROX-Formulario-T-11.pdf` |
| `04/anexo_4B.tex` | `04/salida/LAFROX-Anexo-4B.pdf` |

Compilar los main desde la raíz del repositorio. Si se compilan los complementos manualmente, hacerlo desde `04`. `main.tex` es la entrada del proyecto integrado; las demás raíces permiten revisar o distribuir los complementos por separado.

## Alcance del traslado

Las fuentes de Tomás y los recortes aprobados se conservan. Las clases y sus portadas se copian íntegramente de las dos ramas. El informe de preservación comprueba cada archivo contra su origen, neutralizando únicamente las rutas de figuras cuando corresponde.

Consultar [pendientes de integración](../00/trazabilidad/PENDIENTES.md) antes de presentar esta consolidación como versión armonizada. Los cambios de redacción, numeración editorial y decisiones técnicas se realizarán después, según la instrucción del usuario.
