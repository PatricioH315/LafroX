# Limpieza de entrega del SD9

## Objetivo y alcance autorizado
Corregir residuos internos de los cuatro documentos del SD9 sin inventar datos, revisiones ni aprobaciones. Mantener declaraciones IA, contacto obligatorio y firma contractual; no editar clase, portada ni Markdown fuente.

## Ruta y comprobaciones
Ruta delegada por preparación y múltiples archivos. Dos tareas; previsión menor a 40 líneas autoradas, estrategia ask-on-risk. RED estructural: cuatro raíces con borrador, notas activas y versión Borrador de formato; PDF con marcadores humanos. GREEN esperado únicamente para residuos opcionales, no para información humana inexistente. Comprobar cuatro compilaciones latexmk, extracción y portadas/declaraciones. RDD on global; valoración pendiente. Sin commit: superficies preexistentes no rastreadas que pertenecen al usuario; evitar incorporarlas como propias.

## Tareas
- [x] T1 Limpieza segura: desactivar borrador y notas; eliminar versión opcional sin valor verificable y evitar afirmación automática de entrega final. Conservar campos humanos exigidos.
- [ ] T2 Compilar y comprobar cuatro PDF; documentar exactamente bloqueos de revisión humana, contacto y nomenclatura. No certificar listos para entrega.

## Estado y siguiente paso
T1 realizado en cuatro raíces: modo final desactiva marca de agua y macro nota; estado local Documento técnico evita atribuir aprobación final; versión opcional retirada. Después se corrigió únicamente la paginación de la declaración en contenido.tex, preservando las diez entradas completas; anexos, formularios, clase y portada compartida intactos.
T2 comprobaciones ejecutadas, cierre bloqueado por información humana: 16 marcadores requeridos de revisión y cuatro campos pendientes por portada (domicilio, correo, teléfono, nomenclatura). Consolidación A-6 no comprobada. Firma contractual no suprimida ni simulada.
RED pypdf: 119/94/17/18 apariciones de borrador y 10/4/1/1 marcadores. GREEN final: cero borrador y cero nota de orientación; permanecen 10/4/1/1 marcadores. Páginas finales 120/94/17/18. Cuatro comandos latexmk -lualatex -interaction=nonstopmode -halt-on-error <raíz>.tex, todos exit 0 con acceso elevado; primer intento restringido falló por registro MiKTeX (-1073740791). Cero Overfull, Underfull, referencias indefinidas y caracteres ausentes en los cuatro logs.
Se renderizaron e inspeccionaron portadas y declaraciones (SD9 117-120; anexos 93-94; T13 17; T17 18). Portadas sin borrador y sin afirmación final. Se dividió la declaración SD9 en cuatro bloques de hasta tres entradas y salto explícito, preservando las diez entradas completas. SD9 118 ya no invade el borde superior, pero 118 y 119 siguen sin encabezado incluso con thispagestyle explícito; no se certifica limpio. Último rebuild SD9 exit 0 y cero advertencias mencionadas; declaración legible, sin pérdida de campos. Resto de páginas inspeccionadas legibles.
RDD valoración high/unassessable porque los objetivos son archivos preexistentes no rastreados; selección explícita de inventario y consentimiento pendientes del coordinador. Sin commit para no incorporar contenido preexistente del usuario. Espejo Engram a cargo del coordinador.
Siguiente paso: diagnosticar encabezado ausente SD9 118/119 fuera de esta corrección acotada y obtener quién verificó efectivamente cada sección, qué verificó, datos definitivos de contacto/nomenclatura; después actualizar campos, A-6 y recompilar.
