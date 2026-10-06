# Subdocumento 4 — arquitectura consolidada

Esta carpeta reúne las fuentes vigentes de 4.1, 4.2 y 4.3. El contenido está congelado respecto de los commits indicados en `00/trazabilidad/MANIFIESTO.json`: los únicos cambios dentro de los fragmentos son rutas de imágenes.

## Organización

```text
00/
  plantilla/logica/
  plantilla/fisica/
 trazabilidad/
main.tex
contenido.tex
compilar.ps1
entrega/                  # los tres PDF entregables
04/
  anexos_logica.tex
  formulario_T11.tex
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
```

El cuerpo (`main.tex`) contiene 4.1, 4.2 y 4.3, las referencias y la declaración de uso de IA. Los anexos 4-A a 4-W y el Formulario T-11 se compilan como archivos propios (aclaraciones, sección 1).

## Compilación

Requiere una instalación existente de LuaLaTeX con los paquetes utilizados por las clases originales de LafroX. Abrir una terminal en la raíz del repositorio y ejecutar:

```powershell
powershell -ExecutionPolicy Bypass -File .\compilar.ps1
```

También puede compilarse el documento principal manualmente, dos veces o hasta estabilizar referencias:

```text
lualatex --interaction=nonstopmode --halt-on-error --jobname=LAFROX-Subdocumento4 main.tex
```

El script compila los tres entregables y los deja juntos en la carpeta `entrega/` de la raíz: el cuerpo desde la raíz y el anexo y el formulario desde `04`. Puede usarse `-SoloMain` para compilar solo el cuerpo.

| Fuente | Resultado |
| --- | --- |
| `main.tex` | `entrega/LAFROX-Subdocumento4.pdf` |
| `04/anexos_logica.tex` | `entrega/LAFROX-Subdocumento4-Anexos.pdf` |
| `04/formulario_T11.tex` | `entrega/LAFROX-Formulario-T-11.pdf` |

Compilar el main desde la raíz del repositorio. Si se compilan los complementos manualmente, hacerlo desde `04`. `main.tex` es la entrada del proyecto integrado; las demás raíces permiten revisar o distribuir los complementos por separado.

## Alcance del traslado

Las fuentes de Tomás y los recortes aprobados se conservan. Las clases y sus portadas se copian íntegramente de las dos ramas. El informe de preservación comprueba cada archivo contra su origen, neutralizando únicamente las rutas de figuras cuando corresponde.

Consultar [pendientes de integración](../00/trazabilidad/PENDIENTES.md) antes de presentar esta consolidación como versión armonizada. Los cambios de redacción, numeración editorial y decisiones técnicas se realizarán después, según la instrucción del usuario.
