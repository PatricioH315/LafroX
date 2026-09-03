---
description: Muestra el contenido de un archivo Markdown (.md) renderizado directamente en el chat. Uso: /ver <ruta/al/archivo.md>
---

Lee el archivo Markdown que el usuario indica: `$ARGUMENTS`.

Reglas:
1. Localiza el archivo relativo a la raíz del proyecto y, si no lo encuentras, usa la herramienta `glob` para ubicarlo por nombre.
2. Lee el archivo completo con la herramienta `read`.
3. Muestra su contenido completo, respetando el formato Markdown (títulos, listas, tablas, negritas, citas).
4. Si el archivo no existe o no es un `.md`, indícalo brevemente y sugiere rutas/archivos `.md` cercanos que hayas encontrado.
5. No resumas: entrega el contenido tal cual está en el archivo.
