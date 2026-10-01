# Subdocumento 4 — arquitectura consolidada

Esta carpeta reúne las fuentes vigentes de 4.1, 4.2 y 4.3. El contenido está congelado respecto de los commits indicados en `00/trazabilidad/MANIFIESTO.json`: los únicos cambios dentro de los fragmentos son rutas de imágenes.

## Organización

```text
00/
  plantilla/logica/
  plantilla/fisica/
  trazabilidad/
04/
  main.tex
  contenido.tex
  main_logica.tex
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

Requiere una instalación existente de LuaLaTeX con los paquetes utilizados por las clases originales de LafroX. Abrir una terminal en esta carpeta `04` y ejecutar:

```powershell
powershell -ExecutionPolicy Bypass -File .\compilar.ps1
```

También puede compilarse el documento principal manualmente, dos veces o hasta estabilizar referencias:

```text
lualatex --interaction=nonstopmode --halt-on-error --output-directory=salida --jobname=LAFROX-Subdocumento4 main.tex
```

El script crea `salida/` y compila todas las raíces con LuaLaTeX. Las salidas son:

| Fuente | Resultado |
| --- | --- |
| `main.tex` | `salida/LAFROX-Subdocumento4.pdf` |
| `main_logica.tex` | `salida/LAFROX-Subdocumento4.1.pdf` |
| `anexos_logica.tex` | `salida/LAFROX-Subdocumento4.1-Anexos.pdf` |
| `formulario_T11.tex` | `salida/LAFROX-Formulario-T-11.pdf` |
| `anexo_4B.tex` | `salida/LAFROX-Anexo-4B.pdf` |

Compilar desde `04`, no desde su carpeta superior. `main.tex` es la entrada del proyecto integrado; las demás raíces permiten revisar o distribuir los complementos por separado.

## Alcance del traslado

Las fuentes de Tomás y los recortes aprobados se conservan. Las clases y sus portadas se copian íntegramente de las dos ramas. El informe de preservación comprueba cada archivo contra su origen, neutralizando únicamente las rutas de figuras cuando corresponde.

Consultar [pendientes de integración](../00/trazabilidad/PENDIENTES.md) antes de presentar esta consolidación como versión armonizada. Los cambios de redacción, numeración editorial y decisiones técnicas se realizarán después, según la instrucción del usuario.
