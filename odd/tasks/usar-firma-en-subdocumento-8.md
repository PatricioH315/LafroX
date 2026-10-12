# Incorporar la firma al Subdocumento 8

## Objetivo
Aplicar en las dos salidas del SD8 (cuerpo y anexos) la colocación de firma que utiliza la rama de SD9, limitada al SD8 y sin modificar la clase/portada compartida.

## Decisiones y evidencia
- La rama observada es `origin/LafroX-Subdoc9-LateX`; en `SD9_v_nueva/lafrox-portada.tex:269–271` superpone la firma de 13 mm en la zona manuscrita de la portada, y `SD9_v_nueva/sd9-comun.tex:20–37` añade la firma de 7 mm en el pie derecho sin cambiar la altura del pie.
- El PNG externo `Datos externos/FIRMA_Alex_Aravena_transparente.png` tiene el mismo objeto Git que el activo de SD9 `SD9_v_nueva/logo/FIRMA_Alex_Aravena_transparente.png` (SHA1 `e55414216aaf678cbf46d907bae68bf622f250c6`). Mantener intacto el original externo y copiarlo al `logo/` local para ruta portable.
- Aplicar solo a `main.tex` y `LafroX-Subdocumento-8-Anexos.tex` mediante soporte `sd8-comun.tex`; no cambiar `lafrox.cls`, `lafrox-portada.tex`, T-16 ni otros entregables.
- Se permite el uso del archivo de firma explícitamente solicitado por el usuario.
- No reemplazar PDFs rastreados del proyecto; compilar y revisar ambas salidas en una copia temporal del repo.

## Alcance
- Añadir `logo/FIRMA_Alex_Aravena_transparente.png`.
- Crear `sd8-comun.tex` con el overlay de portada y redefinición del pie equivalentes a SD9, adaptados/limitados al SD8.
- Incluir ese soporte en `main.tex` y `LafroX-Subdocumento-8-Anexos.tex`.

## Tareas
1. [done] Integrar una copia portable del activo de firma en `logo/`, sin alterar el original en Datos externos.
2. [done] Añadir soporte SD8-local para firma en portada y pie, basado en el patrón SD9.
3. [done] Activar soporte únicamente en el cuerpo y anexo del SD8.
4. [done] Verificar diff, compilar ambas fuentes desde copia temporal, inspeccionar portadas y pies; confirmar que los PDFs originales permanecen intactos.

## Resultado y verificación
- `logo/FIRMA_Alex_Aravena_transparente.png` coincide con el activo externo y el de SD9 (SHA-256 `9110733598c0c51293c5c49e075c92e8eae38007db4cf6bd6e019d584c6b3208`); el original externo sigue intacto.
- `sd8-comun.tex` define un overlay de 13 mm para portada y una firma de 7 mm con filete de 3,4 cm en el pie. El wrapper se llama `\LFXportadasd`: TeX no admite el dígito `8` en el nombre de un control sequence.
- Compilación aislada en `C:/Users/maxim/AppData/Local/Temp/lafrox-sd8-signature-7kYveo/`: `main.pdf` (18 páginas) y `LafroX-Subdocumento-8-Anexos.pdf` (28 páginas) compilaron. Se inspeccionaron portada y página interior de ambas salidas; las firmas se ven y no presentan recorte ni solapamiento.
- `git diff --check -- sd8-comun.tex main.tex LafroX-Subdocumento-8-Anexos.tex` pasó. No se compiló ni sobrescribió ningún PDF del espacio original; no se creó commit por la restricción expresa del usuario.

## Resguardos
- El estado inicial muestra el PNG externo como untracked; preservarlo. La firma fue expresamente solicitada.
- El class/cover shared no se edita para evitar afectar T-16 u otros documentos.
- Si el hook overlay no es visible o interfiere con el nombre/caja del representante, ajustar sobre la copia temporal antes de aceptar.
