# LafroX — Resumen del Subdocumento 13: Innovaciones

[Índice de resúmenes](README.md) · [Documento original](../13_innovaciones/LAFROX-Subdocumento13.md)

## Para qué sirve

Presenta cinco aportes adicionales al alcance obligatorio, uno por tipo exigido. Para cada uno explica problema, tecnología o práctica, madurez, incorporación, impacto, indicador y riesgo; T-19 los convierte en fichas formales.

## Las cinco propuestas

- **[INN-01: Seguimiento de vencimiento posentrega en el local](../13_innovaciones/LAFROX-Subdocumento13.md#131-innovaci%C3%B3n-1).** Avisa al preventista sobre lotes que podrían vencer en el negocio del cliente y propone acciones autorizadas. El saldo es estimado y se confirma en la visita; no modifica inventario oficial. Piloto en E1 y materialización en **mes 16**.
- **[INN-02: Reproducción de incidentes de terreno](../13_innovaciones/LAFROX-Subdocumento13.md#132-innovaci%C3%B3n-2).** Convierte un fallo real sin señal en un paquete protegido, reproduce su secuencia en QA y valida la corrección antes de cerrar. Circuito inicial en **mes 5**, beneficio comparado en **mes 15**.
- **[INN-03: Vida útil remanente por historia térmica del lote](../13_innovaciones/LAFROX-Subdocumento13.md#133-innovaci%C3%B3n-3).** Relaciona lote y exposición térmica para estimar vida remanente por familia. Reutiliza la ingesta de **10.920 muestras diarias**; no alarga la fecha impresa ni sustituye la decisión de Calidad. Materialización en **mes 16**.
- **[INN-04: Tramo variable de la Operación ligado al costo de servir](../13_innovaciones/LAFROX-Subdocumento13.md#134-innovaci%C3%B3n-4).** Vincula una parte acotada del pago a reducción comparable de costo, protegida por OTIF. Acompañamiento desde **mes 21**, tres liquidaciones en sombra y primer efecto de pago en **mes 24**.
- **[INN-05: Hoja de negocio del almacenero](../13_innovaciones/LAFROX-Subdocumento13.md#135-innovaci%C3%B3n-5).** Devuelve información de compras durante la visita, en pantalla o papel, sin exigir internet ni dispositivo. Bloques principales en **mes 21**; comparación agregada desde **mes 27** solo con revisión legal favorable.

## Qué significan madurez y beneficio

**TRL** expresa el nivel de madurez de una propuesta. Aunque sus piezas sean conocidas, las integraciones para Puelche parten de niveles iniciales y deben avanzar mediante prototipos y pilotos. Es una evaluación declarada, no experiencia ya demostrada en esta operación.

Las mejoras se miden con líneas base y conjuntos de prueba. Por ejemplo: INN-01 requiere **70 % de avisos confirmados con al menos 100 avisos**; INN-02 busca **30 % menos tiempo de diagnóstico con al menos 20 pares**; INN-03 exige validación por familia antes de habilitarla. El ahorro de producción se mide después, sin sumarlo dos veces a metas obligatorias u otras innovaciones.

## Integración, límites y pendientes

Ninguna agrega hardware a T-11 ni incorpora un modelo aprendido. Los datos viajan por interfaces existentes, con contratos versionados en Anexo 13.A; 13.B los conecta con arquitectura/EDT, y 13.C reúne indicadores y riesgos. Los montos se reservan a la oferta económica.

INN-03 concentra riesgos críticos R8-23/R8-27: una estimación incompleta no autoriza decisiones sanitarias. INN-02 exige sanitizar evidencia; INN-05 exige controlar divulgación del comparativo. Ante falla se conserva la capacidad obligatoria de base.

Los contratos nuevos del Anexo 13.A deben leerse junto al catálogo del SD4, que todavía no los incorpora expresamente en §4.1.6. La declaración de IA mantiene campos de revisión humana por completar; las propuestas e indicadores no se presentan como beneficios ya medidos.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
