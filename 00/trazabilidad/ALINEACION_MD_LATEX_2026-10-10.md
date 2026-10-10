# Alineación del Subdocumento 4 desde `rama-md` — 2026-10-10

Registro interno (no se entrega). Base: Markdown de `rama-md` en `df021b9` (incluye `bcbc3b2`, `c74b783` y `42c01cc`). Destino: `subdoc-4` sobre `e151405`.

## Método

1. Conversión del LaTeX con `tex2md.py` y comparación línea a línea con el Markdown.
2. Se descartaron los artefactos conocidos del conversor: enlaces de figuras, numeración de figuras, «Fuente» de figuras apaisadas, prefijo `l` del T-11 y restos entre 4.1 y 4.2.
3. Port de 82 bloques de contenido con un script de inserción por ancla, conservando los finales de línea de cada archivo.

## Qué se trasladó

- 4.1: autoatención (RT-16.33), autorregistro RF-12.25, WCAG RT-13.01/06/07, bandeja RT-16.13, búsqueda RT-16.27, listados RT-16.28, compresión RT-03.19, doble aprobación RT-16.03, escalamiento RT-16.11, retos WAF RT-11.12, identidad RT-12.01/10/11/12 y RT-16.01, alertas sin IA RT-14.09, agrupación RT-14.04, registros sin datos sensibles RT-14.07, regla térmica preventiva, frecuencia RNF-09.05, nuevo sitio RT-02.12, RF-04.06/07, RNF-17.02, RF-05.03, RF-06.09, baja comercial, RT-16.15, RF-17.09, RT-16.22, cuenta raíz RT-03.03, capacitación RT-22.09 y firma RT-16.18.
- 4.2: interfaces de terreno RNF-05.02 y RT-13.08, vida útil RT-08.19, integridad RT-08.02, parches RT-03.15, etiquetado RT-03.06, RT-15.06, RT-03.09, herramientas del pipeline, congelamientos y vulnerabilidades, QoS RT-03.24, exclusión del escritor y retorno como réplica, recuperación funcional e histórica, medios RT-06.28, ensayo de particiones, márgenes RT-08.05, búsqueda global en la Tabla de umbrales y dotación por período.
- 4.3: contención de racks RT-06.15 y comparación de modalidades RT-07.01.
- Anexos 4-B, 4-H, 4-N, 4-O, 4-P, 4-R y 4-W; T-11; referencias (LafroX 2026c, PostgreSQL Failover y SD3 en anexos); filas de la declaración de IA.

## Ajustes de redacción respecto del Markdown

- Presente en lugar de futuro, frases cortas y sin muletillas («conservando… existentes», «sin equiparar», «persona usuaria»).
- Se quitaron nombres de tablas del SD5 (`mae_producto`, `cal_regla_termica`, `env_movimiento.evidencia_obj_id`) y la cita «SD5-Anexos 5-A y 5-C», según la convención de nombres funcionales del cuerpo.
- Se agregaron las páginas que faltaban a las citas de las Bases en el párrafo de despliegue.
- «Tabla 14/17/30» pasan a `\ref`.
- Anexo 4-P: la ventana dominical está en 4.2.6.6, no en 4.2.6.12 (pruebas de carga). Corregido en LaTeX; el Markdown conserva el error.
- Se omitió «el registro del paquete 8.2.4» en la lista del pipeline (referencia ambigua a un formulario posterior).
- La Figura 17 (TikZ) se conserva en LaTeX; el Markdown la retiró porque no puede mostrarla.

## Verificación

- `compilar.ps1`: cuerpo 183 p., anexos 85 p., T-11 35 p. Sin referencias indefinidas. Sin `Overfull` en cuerpo ni anexos; el T-11 mantiene los desbordes menores (< 4 pt) de su tabla larga, anteriores a este cambio.
- Nueva conversión con `tex2md.py`: todos los bloques del Markdown tienen su par en LaTeX; solo difieren la redacción pulida y los artefactos del conversor.

## Pendiente

- Llevar al Markdown la redacción pulida y la corrección 4.2.6.6, si el usuario lo aprueba.
- Revisión humana real de la declaración de IA.
- El cuerpo sigue citando el SD5 (LafroX 2026a/b) y paquetes del T-14, que son posteriores.
