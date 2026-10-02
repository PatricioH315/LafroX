from pathlib import Path

root=Path(__file__).resolve().parents[2]
readme='''# Subdocumento 5 — Modelo y gestión de datos

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
'''
(root/'05/README.md').write_text(readme,encoding='utf-8')
p=root/'05/PLAN_DESARROLLO.md'
s=p.read_text(encoding='utf-8')
s=s.replace('Estado: plan de trabajo; ejecución documental pendiente.','Estado: desarrollo documental ejecutado; ensayos y revisión humana corresponden a implantación y presentación final.')
s=s.replace('## Estructura del cuerpo y cobertura','## Estructura inicial del plan y cobertura (reorganizada conforme al índice obligatorio)')
report='''
## Resultado de ejecución

El índice definitivo sigue las aclaraciones: **5.1 Modelo**, **5.2 Gestión de datos**, **5.3 Estrategia de migración** y **5.4 Estrategia de desempeño**. La división inicial en seis apartados se corrigió: persistencia, analítica y gobierno se desarrollan dentro de 5.2. Esa distribución prevalece sobre la estructura inicial conservada más abajo como registro del plan.

| Etapa | Resultado documental | Evidencia |
| --- | --- | --- |
| P0 | Fuentes fijadas con SHA-256 y discrepancias de códigos cotejadas | FUENTES.json; Anexo 5-H |
| P1 | 59 entidades, 549 atributos, quince dominios y relaciones canónicas | 5.1; Anexos 5-A/B; modelo.json; diccionario.csv |
| P2 | Autoridad por sitio/agregado, transacciones y protocolo de eventos | 5.2; Anexo 5-C |
| P3 | 32,11 GB de migración estimados; saneamiento, dos ensayos, corte y reversión definidos | 5.3; Anexo 5-D |
| P4 | Índices, particiones, caché, consultas y sensibilidad alineados con arquitectura | 5.4; Anexo 5-E; CALCULOS.json |
| P5 | Modelo dimensional, fórmulas, linaje y objetivos 5 min / 2 h / 4 h | 5.2.4; Anexo 5-F |
| P6 | Calidad, protección, auditoría, exportación y retención por representación | 5.2.5–6; Anexo 5-G |
| P7 | Fuentes modulares, diagramas, raíces y compilación en PDFs separados | Raíces LaTeX; compilar_subdocumento_5.ps1 |
| P8 | Matriz de 30 requisitos, escenarios, criterios y condiciones de aceptación | MATRIZ_RT05.csv; Anexo 5-H; VERIFICACION.json |

ENS-1/ENS-2, pruebas AC/VD, aprobación del CLIENTE y revisión humana no se consideran realizados. PD-01–PD-10 del Anexo 5-H registran evidencias de implantación requeridas. La revisión visual y de compilación se registra en VERIFICACION.json.

'''
if '## Resultado de ejecución' not in s:s=s.replace('## Objetivo y base',report+'## Objetivo y base')
p.write_text(s,encoding='utf-8')
# Ajustes cuantitativos/editoriales del constructor y de las fuentes resultantes.
for p in [root/'05/herramientas/desarrollar_subdoc5.py',root/'05/partes/5.3_estrategia_de_migracion/01_migracion.tex',root/'05/anexos/datos/partes/E_anexo.tex']:
    s=p.read_text(encoding='utf-8').replace('Total × 2 / 1.048.576','Total × 2 / 1.000.000').replace('29,9049','29,9044')
    s=s.replace('164,28 GB/año','164,28 GB/año')
    p.write_text(s,encoding='utf-8')
# El modelo lógico analítico está ahora desarrollado en el diccionario.
for p in [root/'05/herramientas/desarrollar_subdoc5.py',root/'05/anexos/datos/partes/H_anexo.tex']:
    s=p.read_text(encoding='utf-8').replace('Esquemas de dim/hechos detallados en código','Implementación física de hechos y dimensiones').replace('Esquemas de dim/hechos detallados en código','Implementación física de hechos y dimensiones')
    p.write_text(s,encoding='utf-8')
print('Documentación de cierre actualizada')
