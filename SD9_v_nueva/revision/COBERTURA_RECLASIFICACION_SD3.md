# Cotejo de cobertura por reclasificación del SD3

Se comparó la matriz anterior (0e0e0f39) con la generada desde SD3 85596706. Las comprobaciones son previstas. El detalle ejecutable de datos, pasos y evidencia corresponde al plan H1.

| RF | Prioridad anterior → vigente | Casos antes → ahora | Comprobaciones previstas |
|---|---|---:|---|
| RF-01.01 | Crítica → Alta | 5 → 3 | Recepción concordante, discrepancia con alerta y conciliación al cierre sin bloqueo. |
| RF-01.05 | Alta → Crítica | 3 → 5 | Cuarentena y bloqueo de picking, plazo de aviso, reintento de notificación e integridad de cantidades. |
| RF-01.10 | Crítica → Alta | 5 → 3 | Ficha válida, campos obligatorios e historial auditable de GTIN y SKU. |
| RF-02.03 | Alta → Media | 3 → 2 | Propuesta ABC y aprobación; ubicación incompatible o falta de aprobación. |
| RF-02.07 | Alta → Media | 3 → 2 | Consulta de ocupación por zona e histórico; zona sin posiciones configuradas. |
| RF-03.06 | Alta → Media | 3 → 2 | Consulta de historial y productos habituales; cliente sin historial. |
| RF-03.07 | Alta → Media | 3 → 2 | Cálculo del descuento vigente; promoción vencida o no aplicable. |
| RF-03.08 | Crítica → Alta | 5 → 3 | Alerta antes del envío; pedido dentro del cupo y frontera de la regla. |
| RF-03.09 | Crítica → Alta | 5 → 3 | Bloqueo, envío permitido y frontera del umbral que valide Finanzas. Se conserva el estado parcial. |
| RF-03.14 | Alta → Media | 3 → 2 | Sugerencias por historial y promociones; datos insuficientes o promoción vencida. |
| RF-04.02 | Media → Alta | 2 → 3 | Corrección manual, recálculo de ruta y ETA, reasignación inválida y registro del cambio. R18-07 en T‑13 §7.4. |
| RF-04.08 | Alta → Media | 3 → 2 | Cálculo por entrega e insumo de actividad faltante. Evidencia de R18-11. |
| RF-06.02 | Crítica → Alta | 5 → 3 | Firma vinculada a la guía, falta de firma y vía alternativa de RF-06.12. Evidencia de R18-08. |
| RF-06.12 | Media → Alta | 2 → 3 | Firma o fotografía sin teléfono ni señal, evidencia incompleta y vínculo con la guía al sincronizar. Evidencia de R18-08. |
| RF-07.06 | Alta → Media | 3 → 2 | Autorización POS y conciliación; pago rechazado o sin autorización. Cierre y diferencias en T‑17, R18-10. |
| RF-07.07 | Alta → Media | 3 → 2 | Consulta y descarga autenticadas; intento de acceso sin autorización. |
| RF-07.08 | Alta → Media | 3 → 2 | Aprobación y traspaso al ERP; comprobante rechazado o pago aún pendiente. |
| RF-07.10 | Alta → Media | 3 → 2 | Recibo de abono y saldo pendiente; abono inválido. Conciliación diaria en R18-10. |
| RF-08.04 | Alta → Media | 3 → 2 | Aviso dentro de 24 horas al superar el umbral; saldo dentro del umbral. Control de pérdida de envases en R18-12. |
| RF-08.07 | Alta → Media | 3 → 2 | Imputación de devoluciones y mermas; exclusión de duplicados. Evidencia de R18-11. |
| RF-09.06 | Media → Crítica | 2 → 5 | Excursión crítica, retención por SSCC y aviso; excursión menor; umbral aplicable; operación desconectada y reintento; integridad y decisión exclusiva de Calidad. T‑13 §7.4 y V1–V21 del Anexo 4-W. |
| RF-09.07 | Crítica → Alta | 5 → 3 | Rechazo con evidencia, intento sin evidencia y vínculo con sensor y tramo. Ensayo de frío del T‑13 §7.4. |
| RF-11.04 | Alta → Media | 3 → 2 | Fill Rate y Perfect Order frente al pedido original; faltante o inconsistencia y su causal. |
| RF-14.01 | Crítica → Alta | 5 → 3 | Telemetría de los camiones propios, dato no disponible, vigencia y alcance de la fuente. |
| RF-14.03 | Alta → Media | 3 → 2 | Alerta al superar 3 km; desvío igual o inferior al umbral. |
| RF-14.04 | Crítica → Media | 5 → 2 | Imputación de kilómetros y tiempo; datos faltantes o ya imputados. Evidencia de R18-11. |

El dimensionamiento disminuye en 24 casos previstos. Los criterios y los hitos de aceptación se conservan en el T‑17.
