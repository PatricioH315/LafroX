# Alineación del Subdocumento 4 entre `rama-md` y `subdoc-4` — 2026-10-09

Registro interno (no se entrega). Base común: `d397c30` (LaTeX) = `2648853` (Markdown). Después de esa sincronización, cada rama avanzó por separado.

## Del LaTeX al Markdown

Se hizo una mezcla de tres vías (`git merge-file`). Base: Markdown de `2648853`. Lado MD: `rama-md` HEAD `9a7da48`. Lado LaTeX: conversión de `9329485` con `tex2md.py`. Hubo cinco conflictos, resueltos a mano:

- Figuras nuevas de 4.1 (general, ocho capas y cuatro complementarias), retiro de la vista resumida y numeración de figuras en todo el cuerpo. El T-12 cita ahora las Figuras 25 y 26 del SD4.
- Texto de 4.1.5 (dominio lógico), de las secuencias y del acceso local. Nombres funcionales en el cuerpo de 4.1, con las equivalencias técnicas en los Anexos 4-G y 4-P.
- Inventario AWS movido al Anexo 4-P, viñetas de 4.1 y frase repetida de la ACL retirada.
- En el Markdown se corrigieron además restos del conversor: fuente perdida en las figuras apaisadas, «fisica.chapter / [block] 25pt…» y párrafos pegados a viñetas.

## Del Markdown al LaTeX

Se trasladó el contenido propio de `rama-md`:

- Nombres de módulos del SD3, RF-10 en M2 e INT-06, y RF-13 en 4-E.
- Párrafos RT-13.02/05/09/10/11/12, RT-17.08, RT-16.04/05/08/12/19/25, RT-14.09 y RT-11.28 (SAMM).
- Matriz de navegadores de la Tabla A.19.
- Muestras de aceptación, vida útil, sanitización y disposición (4.2.1.2), regresión de carga en CI y reversión técnica ≤ 10 min.
- 4.2.4.1.3 «Implantación por olas en los sitios», sin rastro de Django.
- Acceso de terceros y blindaje (4.3.1.4), y tercer agente de mesa desde el mes 25.
- Referencias a Distribuidora Puelche S.A. en orden alfabético.

Ajustes comunes a ambos lados:

- Una sola declaración de IA al final del cuerpo, con niveles de la escala de Aclaraciones §7.2 y `[[REVISIÓN HUMANA]]`. Se quitó la declaración de los anexos (ensamblador) y la del T-11.
- Las tablas del SD5 citadas en el cuerpo pasan a nombres funcionales. Su equivalencia técnica queda en el Anexo 4-P.
- 4.1.7 sin «paridad» ni «Angular se conserva», con QA de parámetros después de la lista de ambientes.

## Verificación

- Compilación LuaLaTeX: cuerpo de 173 p. y anexos de 83 p., sin referencias indefinidas ni `Overfull`. Los desbordes del T-11, en la tabla de la línea 109, son anteriores a este cambio.
- Al reconvertir el LaTeX con `tex2md.py` se obtiene el Markdown de `rama-md`. Solo difieren los artefactos conocidos del conversor (fuentes de figuras apaisadas, prefijo `l` en las categorías del T-11 y restos entre 4.1 y 4.2), que en el Markdown están corregidos a mano.

## Pendiente

- Revisión humana real de la declaración de IA.
- El SD4 cita el SD5 (LafroX 2026a/b), que es un subdocumento posterior. Lo agregó el equipo en `rama-md` para el T-12; queda a decisión del usuario.
