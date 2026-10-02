# Subdocumento 5 — Modelo y gestión de datos

Versión de diseño documental desarrollada el 2 de octubre de 2026 en `alvaro-modelo-y-gestion-de-datos`, con base en `rama-latex`, commit `2799de341bb425c0323119ca51d0e51e050d506a`.

## Entregables

- `../LAFROX-Subdocumento5.pdf`: cuerpo independiente.
- `../LAFROX-Subdocumento5-Anexos.pdf`: anexos 5-A a 5-H.
- `anexos/datos/fuentes/modelo.json`: entidades, atributos, propietarios, dominios y relaciones.
- `anexos/datos/fuentes/diccionario.csv`: diccionario importable.
- `anexos/datos/fuentes/CALCULOS.json`: resultados cuantitativos reproducibles.
- `formularios/trazabilidad/MATRIZ_RT05.csv`: aporte al T-12 existente.
- `formularios/trazabilidad/FUENTES.json`: inventario y SHA-256 de las fuentes consultadas.
- `formularios/trazabilidad/VERIFICACION.json`: revisión documental y del PDF.
- [Plan ejecutado](PLAN_DESARROLLO.md).

## Estructura

Se conserva la separación de arquitectura entre partes, anexos, formularios y figuras. El índice oficial tiene cuatro apartados; analítica y gobierno pertenecen a Gestión de datos.

```text
main_subdocumento_5.tex
contenido_subdocumento_5.tex
compilar_subdocumento_5.ps1
05/
  preambulo.tex
  anexos_datos.tex
  partes/
    00_introduccion.tex
    5.1_modelo/
    5.2_gestion_de_datos/
    5.3_estrategia_de_migracion/
    5.4_estrategia_de_desempeno/
    90_referencias.tex
    91_declaracion_ia.tex
  anexos/datos/partes/         # anexos A–H
  anexos/datos/fuentes/       # modelo, diccionario y cálculos
  formularios/trazabilidad/   # matriz, inventario y verificaciones
  figuras/fuentes/datos/      # diagramas TikZ editables incorporados al PDF
  herramientas/              # construcción inicial y verificación
  salida/                    # auxiliares locales ignorados por Git
```

## Edición y compilación

Editar el contenido en `partes/` y `anexos/datos/partes/`; editar los diagramas en sus fuentes TikZ. Las raíces coordinan metadatos y ensamblado. `herramientas/desarrollar_subdoc5.py` conserva la construcción inicial: regenera fuentes, por lo que se debe revisar su efecto antes de ejecutarlo sobre ediciones manuales.

Desde la raíz del repositorio, con la instalación existente de LuaLaTeX:

```powershell
./compilar_subdocumento_5.ps1
```

Puede pasarse `-Motor` con la ruta del ejecutable y `-SoloCuerpo` para el cuerpo. El script realiza tres pasadas, guarda auxiliares en `05/salida` y copia los dos PDFs a la raíz. Se reutiliza `00/plantilla/fisica/lafrox.cls`.

Los ensayos de migración, carga y recuperación y las aprobaciones del CLIENTE requieren ejecución y actas reales. La declaración de IA identifica generación sustancial y ausencia de constancia de revisión humana. El manifiesto de `00` describe el traslado histórico del Subdocumento 4; no acredita aceptación del 5.
