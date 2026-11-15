# Referencias corregidas y verificadas — SD4 corrigiendo

Se corrigieron las 24 referencias manuales de página al T-12, el enlace Zebra que devolvía HTTP 404 y la entrada de Tailwind ausente en la bibliografía de anexos. No se alteraron decisiones técnicas, diagramas, compromisos ni documentos de otras ramas.

## Versiones contrastadas

- SD4: `LafroX-Subdoc4-LateX-corrigiendo`, base `2d508f46`.
- T-12: `origin/LafroX-Subdoc3-LateX-CORRIGIENDO`, commit `40d415dbd8a6d361e17eec55104b898a56cc5897`, 260 páginas. Huella SHA-256 en `referencias_20261114/urls.json`.
- Inventario de contraste: 30 ramas locales y 36 remotas después de `git fetch --all --prune`. Las menciones a los apartados de SD1, SD3, SD5 y SD13 se contrastaron con sus fuentes vigentes, sin incorporar esos subdocumentos aquí.

## Correcciones

Las páginas indican la fila del requisito, no otra fila que solo menciona su código.

| Requisito | Página anterior | Página actual del T-12 |
|---|---:|---:|
| RT-02.01 | 131 | 128 |
| RT-02.04 / RT-02.06 | 132 | 129 |
| RT-02.11 | 134 | 131 |
| RT-02.13 | 135 | 132 |
| RT-03.10 | 139 | 136 |
| RT-03.12 | 140 | 137 |
| RT-03.13, caso y Transversales | 141 | 138 |
| RT-11.01 / RT-11.02 | 193 | 191 |
| RT-12.01 | 203 | 201 |
| RT-12.05 / RT-12.07 | 204 | 202 |
| RT-13.01 | 207 | 205 |
| RT-16.08 | 219 | 217 |
| RF-03.16 | 24 | 22 |
| RF-05.02 | 29 | 26 |
| RF-07.03 | 38 | 35 |
| RF-09.06 | 50 | 47 |

- **Tabla 4.1-A del cuerpo:** cuatro remisiones corregidas, en `04/partes/4.1_logica/05_modulos_funcionales_y_limites_de_contexto.tex`.
- **Tabla A.6a del Anexo 4-E:** veinte remisiones corregidas, en `04/anexos/logica/partes/06_anexo_4_1_e_trazabilidad_funcional.tex`.
- **Bibliografía del T-11:** enlace Zebra cambiado de `/us/en/` a `/la/es/`, con título español de la página de especificaciones. El destino respondió HTTP 200 y contiene los modelos citados.
- **Bibliografía de anexos:** añadida la entrada `Tailwind Labs. (s. f.). Responsive design`, ya citada en el Anexo 4-N y presente en la bibliografía del cuerpo.

## Verificación y límites

- Compilación de los tres entregables con `compilar.ps1`: tres pasadas LuaLaTeX por documento, sin errores, etiquetas indefinidas ni destinos duplicados en los registros finales.
- Se mantienen **192 / 139 / 51 páginas**, respectivamente cuerpo / anexos / T-11.
- **404 referencias de fuente**, incluidas `pageref*`, con etiqueta compilada existente; rótulos numéricos de los enlaces a tablas contrastados con los auxiliares.
- **491 enlaces internos y 18 entre PDF**, todos con destino existente; sin `??` en texto extraído.
- **24 remisiones de página al T-12 y 196 citas autor-fecha reconocidas**, sin errores en el verificador final. La revisión de autor-fecha no acredita por sí sola el sustento técnico de cada afirmación.
- El verificador detectó las 24 páginas obsoletas y la bibliografía de Tailwind ausente en la versión anterior; la versión corregida devuelve `passed: true`.
- Comparación de texto antes/después: cambian únicamente cuerpo p. 51, anexos pp. 19–21 y 139, y T-11 p. 51. Las seis páginas se renderizaron e inspeccionaron; no hay cambios en otras páginas ni en la numeración.
- **102 URL únicos:** 101 destinos comprobados por HTTP o por acceso secundario a la fuente primaria. Opensignal sigue sin confirmación por HTTP 403; no se sustituyó por otra edición ni se declaró roto. El detalle conserva los bloqueos originales y el método de verificación secundaria en `referencias_20261114/urls.json`.
- Esta comprobación cubre integridad de referencias y las remisiones externas indicadas; no acredita ensayos de infraestructura, aprobación humana ni una auditoría normativa o contractual completa.

## Repetir el control

Requiere Python con `pypdf`. Compilar primero y proporcionar una copia del T-12 vigente, sin incorporarla a esta rama:

```powershell
powershell -ExecutionPolicy Bypass -File .\compilar.ps1
python .\04\herramientas\verificar_referencias.py --t12 'ruta\al\T12-vigente.pdf'
```

El verificador es de solo lectura, devuelve código 1 ante errores y admite `--output` para guardar el resultado JSON. No consulta sitios web: los estados web son evidencia de esta revisión, no una garantía de disponibilidad futura.
