# Subdocumento 8 — Plan de riesgos

`contenido.tex` monta el cuerpo, los anexos 8.A–8.F y el formulario T-16.
El documento raíz `main.tex` fija el capítulo en 8 y conserva el formato
compartido de `lafrox.cls` y la portada.

## Fuentes

Se trasladaron los tres Markdown de
`Bases PTE/Git Markdown/LafroX/08_plan_riesgos/`:

- `LAFROX-Subdocumento8.md`
- `LAFROX-Subdocumento8-Anexos.md`
- `LAFROX-Formulario-T-16.md`

El texto, las cifras, las citas y las declaraciones de IA se conservan.
El diagrama Mermaid se traduce a TikZ con la misma jerarquía y los 32 riesgos.
Las tablas usan `tablalafrox`, con encabezados repetidos y páginas verticales.
Las tablas sin rótulo en la fuente reciben rótulos auxiliares; B.1 y C.1
se identifican según las referencias del propio texto.

Para actualizar la conversión, desde la raíz del repositorio:

```powershell
python convertir_sd8.py
```

El conversor comprueba que todos los párrafos, viñetas y celdas de las
fuentes están presentes en las salidas. El diagrama se mantiene por separado.

## Pendientes de entrega y validación

- Completar la fecha de entrega y confirmar la nomenclatura oficial en `main.tex`.
- Completar los campos `[[REVISIÓN HUMANA]]` que vienen de las fuentes.
- Compilar con LuaLaTeX y revisar visualmente el PDF. En esta sesión MiKTeX
  no logró iniciar, incluso para `--version`, y no generó PDF ni registro
  de compilación. La disposición final de tablas y páginas queda pendiente
  de esa revisión.
