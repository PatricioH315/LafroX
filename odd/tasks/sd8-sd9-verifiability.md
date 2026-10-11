# LafroX — Verificabilidad de los planes SD8 y SD9

## Objetivo y alcance autorizado

Hacer explícitas la clasificación y la verificación de los 32 riesgos existentes, el control documental y el cierre por eficacia de las mejoras de calidad. Editar únicamente los cuerpos SD8/SD9 y los anexos SD8, además de este registro operativo. No editar contexto, formularios, otros anexos, figuras ni planillas.

## Restricciones y decisiones

- Rama vigente: `rama-md`; no cambiar de rama ni publicar.
- Conservar 32 riesgos, asignaciones de la Figura 8.1, fichas, cifras, umbrales, reservas, diagramas y marcas de revisión humana.
- La EDR explica las ramas existentes; no reclasifica ni incorpora amenazas nuevas.
- La matriz enlaza controles y evidencia planificados: no acredita ensayos, aprobación ni eficacia.
- Preservar H6/H11 como inicio de marcha blanca y H7/H12 como pasos contractuales a producción.
- No añadir FTA, herramientas, nuevos CP, compromisos ni umbrales.
- Documentación pasiva: no existe RED/GREEN significativo; se aplican lectura semántica y comprobaciones estructurales.

## Tareas y ruta

- [x] V-01 — SD8: explicar ramas/categorías; agregar índice EDR de 32 riesgos enlazado a sus fichas, síntesis ejecutiva sin cifras duplicadas y matriz de 32 verificaciones en anexos.
  - Ruta: delegada; lectura y escritura analítica en dos archivos no triviales.
  - Aceptación: asignaciones idénticas al diagrama/fichas; control, criterio, plazo y responsable sustentados en cada ficha; evidencia no presentada como obtenida.
  - Commit de unidad: pendiente del coordinador.
- [x] V-02 — SD9: agregar navegación, checklist documental antes de 9.2.6 y ciclo de mejora con verificación de eficacia en el siguiente Comité de Calidad mensual.
  - Ruta: delegada; tercera edición no trivial integrada con V-01.
  - Aceptación: mantener gobierno, títulos obligatorios, umbrales y aceptación contractual; checklist utilizable y cierre de acción sustentado por evidencia.
  - Commit de unidad: pendiente del coordinador.

## Verificación

- OK: `git diff --check`, salida 0 tras la edición final.
- OK: script de lectura, 32 ID únicos de EDR iguales a Figura 8.1 y fichas; 32 filas de verificación y enlaces a encabezados válidos.
- OK: fichas completas y cifras idénticas a HEAD; diagramas intactos; marcadores preexistentes conservados. Se añaden dos marcadores pendientes por Anexo 8.G (cuerpo y declaración propia), sin atribuir revisión.
- OK: títulos existentes estables; lectura semántica de nuevas secciones y cotejo T-13 secciones 5/9 y T-17 secciones 1–3.
- OK: cambios exclusivamente en las cuatro rutas autorizadas.
- N/A: ejecución de pruebas, simulación, PDF o revisión humana; no forman parte de este cambio documental.

## Entrega y recuperación

- Estrategia: `ask-on-risk`; previsión de 190–260 líneas añadidas más eliminadas, incluidos registros. Heurística de 400 líneas orientativa, no límite de claridad.
- Conteo observado: entregables 141 añadidas + 6 eliminadas = 147 líneas; registro operativo 42 líneas nuevas; total 189 antes de commits.
- Espejo Engram: versión inicial confirmada por coordinador (#87); actualización final pendiente de espejo.
- Próximo paso: coordinador actualiza espejo, comprueba una muestra y gestiona commits/política de revisión. V-01/V-02 completadas documentalmente; commits pendientes. No se ejecutaron ensayos ni simulación.
