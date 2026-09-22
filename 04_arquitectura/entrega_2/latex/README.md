# Subdocumento 4.1: arquitectura lógica preliminar

El archivo editable es `subdoc_4.1.tex`. Se incorpora el preliminar solicitado por
Álvaro el 22-09-2026, preparado a partir del Markdown del subdocumento 4.1 y de la
plantilla LafroX. Se conserva la numeración 4.1–4.7 del contenido original.

Es material preliminar para revisión del equipo: sus correcciones técnicas no
equivalen a decisiones aprobadas. La narrativa Markdown de Entrega 2 y los
documentos de arquitectura física conservan su estado previo. Los diagramas
originales se referencian desde la biblioteca `Diagramas/`; su resolución y
contenido son los de esa biblioteca.

## Compilación y trabajo compartido

1. Abrir la raíz del repositorio LafroX en VS Code, en `arquitectura-alvaro`.
2. Abrir `main.tex` en la raíz y guardar. `.vscode/settings.json` contiene
   exactamente la receta LuaLaTeX solicitada, sin depender de latexmk ni Perl.
3. También se puede ejecutar desde la raíz:

   ```sh
   lualatex --interaction=nonstopmode --synctex=1 main.tex
   ```

   Repetir la compilación si LaTeX solicita actualizar índices o referencias.
   El resultado es `main.pdf` junto a `main.tex`.
4. LaTeX Workshop (`james-yu.latex-workshop`) y Live Share
   (`ms-vsliveshare.vsliveshare`) figuran como extensiones recomendadas.
   El anfitrión necesita LuaLaTeX disponible en su PATH.
5. Para empezar una colaboración, iniciar sesión en Live Share, pulsar Share y
   enviar el enlace al compañero. En Shared Terminals, compartir una terminal
   con permiso Read/Write. El compañero puede ejecutar el comando anterior.

Esta preparación no inicia una sesión pública ni distribuye enlaces. El visor
PDF compartido se omite conforme a la instrucción del usuario.

## Cambios heredados del preliminar

Se incorporan el mapa de ocho capas, 13 perfiles representados, ajustes de
acceso mediante APIs, flujo Gateway–ALB, propuesta de continuidad de identidad
desconectada y planificación de actualización tecnológica. Las secciones 4.1,
4.2, 4.3.3, 4.5 y 4.6 contienen las correcciones; 4.7 conserva los 14 diagramas.
La validación técnica de estas propuestas corresponde a la revisión del equipo.
La incorporación se registra como observación 11 de la planilla T-22.
