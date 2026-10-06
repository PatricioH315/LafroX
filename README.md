# LafroX — plantilla común de subdocumentos LaTeX

La rama `rama-formato-Latex-base` contiene el formato compartido. Cada rama hija debe llamarse exactamente `LafroX-Subdoc<N>-LateX`, por ejemplo `LafroX-Subdoc4-LateX`. Conservar las mayúsculas y minúsculas indicadas.

## Estructura y procedencia

```text
main.tex                         Metadatos y montaje del documento
lafrox.cls                       Clase y formato corporativo
lafrox-portada.tex               Diseño de portada
latexmkrc                        Compilación con LuaLaTeX
logo/                           Isotipos de portada y encabezado
subdocumento-ejemplo/
    contenido.tex               Capítulo autocontenido de muestra
    tablas/ejemplo_tabla.tex     Ejemplo de tabla
README.md
.gitignore
```

Origen: `D:\Usuario\Descargas\lafrox`, recibido el 5 de octubre de 2026. Se conservan la clase, portada, logotipos y un ejemplo. `subdoc/` duplicaba el ejemplo y su ZIP contiene otras versiones del formato; ambos se excluyen para conservar una única fuente. Los temporales y el PDF principal generado no se publican. `main.tex` se adapta como ejemplo compilable y `latexmkrc` elimina las rutas personales del equipo original.

Esta base tiene historia independiente para contener únicamente la plantilla. Crear sus ramas hijas desde ella permite compartir las mejoras por merge. Integrar una rama antigua con historia distinta requiere una importación coordinada; no forzar la unión de historias independientes.

## Crear una rama hija

Si aún no tienes una copia del repositorio:

```bash
git clone --single-branch --branch rama-formato-Latex-base https://github.com/PatricioH315/LafroX.git LafroX-Subdoc4-LateX
cd LafroX-Subdoc4-LateX
```

Si ya tienes una copia, guarda o registra tu trabajo pendiente antes de cambiar de rama. Dentro del repositorio, cambia `4` por el número correspondiente:

```bash
git fetch origin rama-formato-Latex-base:refs/remotes/origin/rama-formato-Latex-base
git switch --no-track -c LafroX-Subdoc4-LateX origin/rama-formato-Latex-base
git push -u origin LafroX-Subdoc4-LateX
```

Si tu clon descarga ramas limitadas, agrega tu rama hija a la configuración para recibir sus actualizaciones:

```bash
git remote set-branches --add origin LafroX-Subdoc4-LateX
git fetch origin
git branch --set-upstream-to=origin/LafroX-Subdoc4-LateX LafroX-Subdoc4-LateX
```

## Adaptar el subdocumento

1. Renombra `subdocumento-ejemplo/` con el número y tema, por ejemplo `04_arquitectura/`.
2. Conserva `contenido.tex` como entrada de la carpeta. Debe empezar con `\chapter{Título obligatorio del subdocumento}`. Sustituye el texto, etiquetas y tabla de muestra por tu contenido.
3. Organiza dentro de la carpeta `partes/`, `tablas/`, `figuras/`, `anexos/` y `formularios/` según necesidad. Git conserva carpetas cuando contienen archivos.
4. En `main.tex`, cambia la llamada a `\subdocumento{04_arquitectura}`. Si compilas el Subdocumento 4 por separado, añade `\setcounter{chapter}{3}` inmediatamente antes. Para N utiliza N−1. Al consolidar el informe, coordina el contador desde el documento raíz y monta los capítulos en orden.
5. Actualiza en `\datoslafrox` el documento, subtítulo/informe, alcance, formulario aplicable, fecha, versión y nomenclatura. La nomenclatura de muestra no es válida para entregar; verifica la oficial en las Bases. Los valores con comas deben ir entre llaves y los guiones bajos se escriben `\_`.
6. Revisa los datos institucionales heredados de la clase. Los valores confirmados se pueden sobrescribir mediante `\datoslafrox` en `main.tex`, sin editar la clase. No dar por acreditados los valores predeterminados.
7. Incorpora las secciones obligatorias, referencias, anexos, formularios y declaración de uso de IA según las Bases y aclaraciones vigentes. La plantilla controla presentación y no acredita cumplimiento del contenido.

La rama base conserva el ejemplo; cada rama hija lo sustituye por su capítulo real.

### Fragmentos, figuras y tablas

Monta fragmentos con `\parte{partes/nombre}` o `\parte{tablas/nombre}`, sin `.tex`. Las rutas se resuelven dentro de la carpeta del subdocumento: evita rutas absolutas o `../`.

Inserta figuras con `\figuralafrox{0.9}{figuras/diagrama.pdf}{Descripción}{fig:sd4-diagrama}`. Prefija las etiquetas por capítulo (`cap:sd4`, `fig:sd4-...`, `tab:sd4-...`) para evitar colisiones al consolidar.

Las tablas utilizan `tablalafrox` con cuatro argumentos: título, etiqueta, columnas y encabezado. Consulta `tablas/ejemplo_tabla.tex`. Conserva la legibilidad de figuras y tablas; no reduzcas la tipografía para ocultar problemas de espacio.

## Qué cambiar y qué conservar

| Adaptar en cada rama | Conservar como formato compartido |
|---|---|
| Contenido, título y número del capítulo | `lafrox.cls` y sus comandos |
| Metadatos y montaje de `main.tex` | Diseño de `lafrox-portada.tex` |
| Tablas, figuras, anexos y formularios | Logotipos, fuentes y paleta |
| Etiquetas y bibliografía | Márgenes, encabezados, pies y foliación |
| Opciones acordadas para la entrega | Configuración común de LuaLaTeX |

La clase admite `carta`, `oficio`, `borrador`, `final`, `firma`, `sinfirma`, `apa` y `sinnotas`. Usa `borrador` durante la redacción y `final` para la entrega revisada. El tamaño de papel y las firmas deben corresponder a lo acordado para la entrega.

Coordina las mejoras de diseño desde `rama-formato-Latex-base` para que todos reciban el mismo formato. Configura el visor PDF y las rutas personales en el editor o equipo de cada integrante.

## Compilar

Se requiere una distribución TeX con LuaLaTeX, `latexmk` y los paquetes declarados en `lafrox.cls`. `latexmk` requiere Perl, que en Windows puede necesitar instalación separada. La clase utiliza Source Serif 4, Source Sans 3, IBM Plex Mono (`plex-mono`) y STIX Two Math. Con la opción `apa` también se requieren `biblatex-apa` y Biber.

Desde la raíz:

```bash
latexmk main.tex
```

Se genera `main.pdf` en la raíz. Para recompilar automáticamente, utiliza `latexmk -pvc main.tex`.

Si no tienes `latexmk` o Perl, ejecuta LuaLaTeX hasta estabilizar índices y referencias:

```bash
lualatex --interaction=nonstopmode --synctex=1 main.tex
lualatex --interaction=nonstopmode --synctex=1 main.tex
lualatex --interaction=nonstopmode --synctex=1 main.tex
```

Con bibliografía Biber, ejecuta `biber main` después de la primera pasada y vuelve a compilar. El editor y visor son opcionales. El ejemplo no necesita `--shell-escape`.

Revisa errores de compilación y comprueba portada, número de capítulo, folios, índices, figuras, tablas y referencias en el PDF. La existencia del PDF no demuestra por sí sola una compilación correcta. `.gitignore` conserva los PDF de figuras y logotipos y excluye el PDF principal y auxiliares.

## Registrar y publicar

```bash
git status
git add main.tex 04_arquitectura
git commit -m "Actualiza Subdocumento 4"
git push
```

Adapta la carpeta y el mensaje a tu capítulo. Revisa los archivos incluidos antes de registrar.

## Recibir mejoras de la base

Las ramas hijas conservan la plantilla de la que partieron; no se actualizan automáticamente. Guarda o registra tu trabajo y ejecuta:

```bash
git switch LafroX-Subdoc4-LateX
git fetch origin rama-formato-Latex-base:refs/remotes/origin/rama-formato-Latex-base
git merge origin/rama-formato-Latex-base
```

Resuelve los conflictos conservando el contenido y los metadatos de tu capítulo e incorporando las mejoras comunes. Revisa `main.tex` y recompila antes del push. Integrar capítulos de distintas ramas requiere una consolidación acordada porque cada uno adapta su documento raíz.
