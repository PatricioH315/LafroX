# Arquitectura lógica modular — 4.1

La reorganización conserva el contenido técnico existente. No modifica arquitectura física ni cierra las brechas técnicas pendientes de la auditoría.

## Organización

- El main.tex de la raíz sigue siendo la entrada principal.
- subdoc_4.1.tex conserva la entrada del apartado y carga contenido.tex de esta carpeta.
- contenido.tex ordena los 24 fragmentos de partes: apertura, apartados, Referencias y Declaración de IA.
- anexos/contenido.tex ordena los 17 fragmentos de anexos/partes: apertura, anexos A–N, Referencias y Declaración de IA.
- El archivo vecino anexos_4.1.tex conserva el preámbulo y permite compilar los anexos desde la raíz del repositorio o desde su directorio.
- Las figuras siguen en Diagramas/arquitectura_logica_actual: no se duplican dentro del repositorio.
- Los antiguos catalogo_interno_4.1.tex, catalogo_externo_4.1.tex y aceptacion_logica_4.1.tex son comentarios que indican la nueva ubicación, no entradas compilables.

MANIFIESTO_ESTRUCTURA.json registra el orden y las huellas de la migración. Estas huellas históricas no sustituyen una validación tras futuras ediciones.

## Edición y compilación

Editar el fragmento correspondiente, sin mantener otra copia del texto en las entradas compatibles. Compilar con LuaLaTeX dos veces para resolver índices y referencias. Desde la raíz: lualatex --interaction=nonstopmode main.tex. Para anexos: lualatex --interaction=nonstopmode 04_arquitectura/entrega_2/latex/anexos_4.1.tex.

No se trasladaron ajustes de numeración propios del documento físico. La consolidación del capítulo 4 deberá resolver su apertura y sus cierres comunes según las bases.

## Distribución

El exportador local Proyecto_Lafrox/tools/empaquetar_logica_drive.mjs delega en exportar_logica_modular.mjs. Recibe un directorio de salida nuevo y, opcionalmente, un directorio de fuentes y un commit. Produce contenido.tex, main.tex, partes, figuras, anexos, plantilla, README y manifiesto autocontenidos. Las copias de figuras son exclusivamente para distribución.

Compilar principal y anexos y verificar referencias antes de sustituir el paquete y su ZIP, conservando respaldo. El manifiesto distingue commit base y cambios locales: no presenta trabajo sin subir como publicado.

La migración verificó concatenación exacta de fragmentos y texto idéntico por página de los dos PDF. El Markdown lógico no se reescribió, dado que no cambió el contenido técnico.
