# Revisión semántica T-12 y correspondencia T-11 — 25-10-2026

Se revisaron semánticamente las 653 filas del T-12 y la correspondencia de los 98 recursos del T-11. Resultado documental final: **595 Cumple, 36 Cumple parcialmente y 22 No cumple**. Se corrigieron 62 filas y se cambiaron 27 estados; no se alteró la descripción de ninguna exigencia.

El informe individual y sus CSV/JSON se guardan en `revision/REVISION_SEMANTICA_T12_2026-10-25.md` y `revision/semantica_t12_2026-10-25/` de la rama `LafroX-Subdoc3-LateX`. El registro de los 98 recursos del T-11 está en [REVISION_SEMANTICA_T11_2026-10-25.json](REVISION_SEMANTICA_T11_2026-10-25.json).

Las correcciones distinguen inventario/picking, cierre financiero/analítica, contenido preparado enviado al ERP, estado sanitario y disposición de Calidad, cobro del preventista, alta conectada de conductores y sincronización por dispositivo. Se corrigió AI 11 (producción, no recepción) según [GS1](https://ref.gs1.org/ai/), el registro ADR-24, el diccionario de 121 entidades/995 atributos y la base de 128.853,67 HH de Operación para deuda técnica.

Las brechas se mantienen expresas: umbral de crédito ambiguo, MFA para todas las entradas externas, excepción TLS1.2, protección AS2, remediación durante congelamientos, campaña semestral de intrusión, salida de plantillas, apertura SMS, especificación/gestión remota de ciertos dispositivos, base de conocimiento de todo el contrato y la vista térmica anterior del SD13. La página institucional publicada no acredita recursos, recorrido virtual, métricas en vivo ni calculadora; los estados se ajustaron a la evidencia recuperada.

T-11 distingue el artefacto único de los cinco perfiles operacionales y explicita la hipótesis de un compartimento/una puerta por camión. El mapeo valida cantidades y los ensayos validan integración/rangos/autonomía. Los ocho PC nuevos aún requieren especificación de compra y el inventario de la entrada SBD debe precisarse respecto de las 13 colas de aplicación. No se inventaron modelos ni pruebas ejecutadas.

El detalle completo está en la rama del T-12. Esta revisión comprueba significado y coherencia documental de la propuesta; no acredita implantación, ensayos físicos, certificados de terceros, conformidad legal independiente ni aceptación del CLIENTE. Las figuras y las ramas excluidas permanecen sin cambios.

## Verificación de las salidas

Siete raíces afectadas recompiladas con tres pasadas de LuaLaTeX; T-12 final de 264 páginas y T-11 de 45. Se comprobó la presencia de los 653 identificadores en el PDF del T-12 y se revisaron visualmente 23 páginas seleccionadas de las siete salidas. Se corrigió el espaciado del bloque de fuente/nota del T-11 y se verificó el PDF final. Sin caracteres faltantes ni referencias LaTeX indefinidas; T-11 y T-12 sin desbordes. Se conservan dos advertencias inferiores a 1 pt en la declaración IA de SD3 y advertencias de pegamento en tablas inalteradas de SD5. Figuras y bloques TikZ/figure íntegros respecto de la línea base. Las huellas SHA-256 finales quedan en el JSON de verificación.
