# Justificación del Módulo de Inteligencia de Negocios (BI) y Analítica Operacional

> **Proyecto:** Licitación TFEP-01/2026 — Caso 02: Logística  
> **Entidad:** Distribuidora Puelche S.A.  
> **Documento:** Justificación técnica del módulo de BI/Analítica con trazabilidad a requerimientos de Bases  
> **Fecha de emisión:** 04/09/2026  
> **Revisión:** 1.0  

---

## 1. Objetivo

Este documento justifica la existencia, alcance y diseño del módulo de Inteligencia de Negocios (BI) y Analítica Operacional dentro de la arquitectura propuesta, demostrando que no se trata de una capa optativa sino de un componente **obligatorio** exigido tanto por las Bases Técnicas Transversales como por el Caso 02. Se presenta la trazabilidad completa desde las fuentes normativas hasta los componentes tecnológicos que lo materializan.

---

## 2. Fundamento normativo

### 2.1 Bases Técnicas Transversales (RT)

| ID RT | Requerimiento | Tipo | Naturaleza |
|-------|--------------|------|------------|
| RT-05.25 | Capa analítica con tableros operacionales y de gestión | Obligatorio | Estructura de plataforma |
| RT-05.26 | Tableros con filtros por período, unidad organizacional y drill-down | Obligatorio | Estructura de plataforma |
| RT-14.02 | Acceso propio y permanente a tableros operacionales y de negocio | Obligatorio | Observabilidad |
| RT-14.03 | SLA/SLO medidos sobre experiencia real del usuario (P95) | Obligatorio | Observabilidad |
| RT-14.04 | Alertamiento basado en síntomas de negocio | Obligatorio | Observabilidad |

Las Bases Técnicas Transversales establecen que la capa analítica es un **componente estructural** de la plataforma, no una funcionalidad adicional. Su omisión o subdimensionamiento constituiría una observación grave conforme al Art. 10° de las Bases Administrativas.

### 2.2 Caso 02 — Distribuidora Puelche S.A.

El caso define tres indicadores estratégicos que requieren procesamiento analítico continuo:

| Indicador | Estado actual | Meta | Fuente en Caso |
|-----------|--------------|------|----------------|
| OTIF (On-Time In-Full) | 82.4% | > 95% | Cap. 4.1, 7.1 |
| Fill Rate | 91.3% | > 97% | Cap. 4.1 |
| Costo de Servir por cliente | Desconocido | Calcular y gestionar | Cap. 7.2, 9.8 |

Citas textuales del caso que respaldan la exigencia:

- *"Mi indicador principal es el OTIF"* — Nelson, Gerente Comercial (Cap. 7.1)
- *"El costo de servir es mi obsesión. Si no sabemos cuánto nos cuesta llegar a cada local, ¿cómo vamos a decidir a quién priorizar?"* — Gerente de Finanzas (Cap. 7.2)
- *"Necesito saber el costo de servir por cliente y por entrega"* — Gerente de Finanzas (Cap. 9.8)

Estos indicadores no pueden calcularse sin un componente de analítica que consolide datos transaccionales de múltiples módulos (preventa, transporte, cobranza, telemetría, bodega) y los presente de forma consumible por los gerentes.

---

## 3. Requerimientos funcionales del módulo

### 3.1 Requerimientos propios del módulo (Épica 11)

| ID RF | Nombre | Actor(es) principal(es) | Descripción | Origen |
|-------|--------|------------------------|-------------|--------|
| RF-11.01 | Distribución Automática de Reportes Ejecutivos | Gerente de Finanzas, Gerente Comercial, Jefa de Calidad | Programar y distribuir vía correo reportes ejecutivos consolidados (PDF/XLSX) con periodicidad semanal y mensual, desglosando OTIF, Fill Rate, Merma por vencimiento y Costo de Servir por zona y canal | Cap. 7.1, 7.2, 9.8 |
| RF-11.02 | Cálculo del Costo de Servir por Entrega y Cliente | Gerente de Finanzas, Gerente Comercial | Calcular Costo de Servir real por entrega y cliente, imputando costos directos de transporte (combustible, peajes, tiempo de conducción/descarga) e indirectos prorrateados (bodega, administración) | Cap. 4.4, 7.2, 9.8 |
| RF-11.03 | Cálculo Diario Unificado del Indicador OTIF | Gerente Comercial, Jefa de Calidad, Conductores | Calcular diariamente OTIF por cliente, ruta, zona y total consolidado. On-Time = cumplimiento de fecha/ventana horaria. In-Full = 100% de ítems y unidades pedidas. Obligar registro de causal tipificada ante desvíos | Cap. 7.1, 9.1 |
| RF-11.04 | Medición de Fill Rate y Perfect Order con POD Móvil | Gerente Comercial, Conductores | Calcular automáticamente Fill Rate (unidades entregadas vs pedidas) e índice de Perfect Order contrastando orden original contra datos de entrega física confirmados en dispositivo móvil | Cap. 7.1, 9.4 |
| RF-11.05 | Monitoreo y Alerta de Ocupación de Flota | Planificador de rutas, Gerente Comercial | Calcular diariamente utilización de capacidad volumétrica (m³) y peso (kg) por viaje, alertando camiones con ocupación inferior al umbral configurable (< 65%) | Cap. 4.4, 7.2 |
| RF-11.06 | Tablero de Control Operacional en Tiempo Real | Gerente Comercial, Gerente de Finanzas, Jefa de Calidad | Tablero de Control que consolide avance de rutas de despacho, % entregas cumplidas, devoluciones en tránsito, alertas de cadena de frío y monto recaudado en efectivo | RT-05.29, Cap. 9.1, 9.6 |
| RF-11.07 | Liquidación y Cierre Comercial por Camión | Cajero Liquidador, Conductores, Gerente de Finanzas | Procesar automáticamente la liquidación y cierre comercial por camión al retornar a base, consolidando documentos tributarios, devoluciones, cobranzas y balance de envases retornables | RT-05.29 |
| RF-11.08 | Segmentación de Clientes por Rentabilidad Neta | Gerente Comercial, Preventista, Gerente de Finanzas | Segmentar mensualmente la cartera en matrices de rentabilidad neta (margen comercial vs costo de servir real), sugiriendo ajustes de frecuencia o umbrales mínimos de compra para clientes no rentables | Cap. 7.2, 9.8 |

### 3.2 Requerimientos no funcionales del módulo

| ID RNF | Nombre | Descripción | Prioridad |
|--------|--------|-------------|-----------|
| RNF-11.01 | Latencia de despliegue de indicadores operacionales | Desplegar indicadores del día con latencia ≤ 5 min desde recepción en backend central | Muy Alta |
| RNF-11.02 | Desacople OLAP/BI vs OLTP | Desacoplar procesamiento analítico del motor transaccional, garantizando cero degradación en tiempos de respuesta de bodega (picking ≤ 1s) y preventa (≤ 1.5s) | Alta |

### 3.3 Requerimientos transversales vinculados al módulo

| ID RF | Nombre | Actor(es) | Descripción | RT de origen |
|-------|--------|-----------|-------------|--------------|
| RF-16.02 | Acceso del CLIENTE a tableros operacionales y de negocio | Cliente | Acceso propio y permanente a tableros operacionales y de negocio con datos en tiempo real y capacidad de exportación | RT-14.02 |
| RF-16.03 | Alertamiento basado en síntomas de negocio | Equipo de operaciones | Alertas por síntomas de negocio (OTIF bajo, pedidos no preparados), no solo umbrales de infraestructura. Con supresión de ruido, agrupación, escalamiento y turnos de disponibilidad | RT-14.04 |
| RF-17.12 | Listados ordenables, filtrables, paginados y exportables | Persona usuaria interna | Listados ordenables, filtrables, paginados y exportables en formatos abiertos, con filtro aplicado reflejado en exportación | RT-16.28 |
| RNF-16.01 | SLA/SLO medidos sobre experiencia real del usuario | Equipo de operaciones | Indicadores de nivel de servicio medidos sobre experiencia real (P95), no sobre pruebas sintéticas | RT-14.03 |

### 3.4 Requerimientos de otras épicas con dependencia del módulo BI

| ID RF | Épica | Nombre | Dependencia con BI |
|-------|-------|--------|-------------------|
| RF-04.08 | Planificación de Rutas | Cálculo integral del costo de entrega realizada | Alimenta RF-11.02 (costo de servir) con costo calculado por ruta |
| RF-06.07 | Transporte/POD | Sincronización de registros de turno (reporte de cierre) | Alimenta RF-11.07 (liquidación por camión) con datos de cierre |
| RF-07.02 | Cobranza | Rendición Digital Individual de Efectivo | Alimenta RF-11.07 con cuadratura de cobranza |
| RF-07.07 | Cobranza | Consulta de Estado de Cuenta en Portal | Consumida por RF-16.02 (tableros para clientes) |
| RF-08.06 | Logística Inversa | Reporte de Pérdida de Envases Retornables | Alimenta RF-11.02 (costo de servir) con costo de envases perdidos |
| RF-08.07 | Logística Inversa | Integración de Devoluciones y Mermas al Costo de Servir | Alimenta RF-11.02 con componente de devoluciones/mermas |
| RF-09.05 | Trazabilidad | Alerta de excursiones térmicas | Consumida por RF-11.06 (tablero operacional) y RF-16.03 (alertas) |
| RF-14.06 | Telemetría | Integración de telemetría con costo de servir | Alimenta RF-11.02 con km reales y tiempo de viaje por entrega |
| RF-14.09 | Telemetría | Reportes de kilometraje y consumo | Consumida por RF-11.01 (reportes ejecutivos) y RF-11.02 (costo de servir) |
| RF-02.07 | Almacén | Consulta de nivel de ocupación por zona | Consumida por RF-11.06 (tablero operacional) |
| RF-03.08 | Preventa | Alerta por superación del límite de crédito | Consumida por RF-16.03 (alertas de negocio) |

---

## 4. Mapeo de requerimientos a componentes de arquitectura

### 4.1 Componentes del módulo BI

El módulo de BI/Analítica se materializa en los siguientes componentes de la arquitectura:

| Componente | Ubicación | Tecnología | Responsabilidad |
|------------|-----------|------------|-----------------|
| **Motor OLAP / Warehouse** | Cloud (AWS) | Amazon Redshift Serverless | Almacenamiento analítico desacoplado de OLTP. Consolida datos de Aurora PostgreSQL vía DMS CDC. Alimenta RF-11.01–RF-11.08 |
| **Motor transaccional fuente** | Cloud (AWS) | Amazon Aurora PostgreSQL (PostGIS) | Base OLTP de donde se extraen los datos hacia Redshift. Contiene datos de preventa, reparto, cobranza, bodega |
| **Motor transaccional fuente (on-prem)** | On-Premise (Talca) | PostgreSQL + PostGIS (local) | WMS de bodega. Sincroniza con Aurora vía DMS CDC (RPO ≤ 15 min) |
| **Capa de procesamiento analítico** | Cloud (AWS) | Celery workers (Django) + Redshift SQL | Cálculo de OTIF (RF-11.03), Fill Rate (RF-11.04), Costo de Servir (RF-11.02), Ocupación de Flota (RF-11.05), Segmentación (RF-11.08) |
| **Distribución de reportes** | Cloud (AWS) | Celery Beat + SES (correo) + S3 (almacenamiento PDF/XLSX) | RF-11.01: reportes automáticos semanales/mensuales |
| **Tablero operacional** | Cloud (AWS) | Grafana (autoservicio) o Angular SPA | RF-11.06: tablero de control en tiempo real. RF-16.02: acceso del cliente. RF-16.03: alertas de negocio |
| **Sistema de alertas** | Cloud (AWS) | CloudWatch + SNS + Celery | RF-16.03: alertamiento por síntomas de negocio. RF-11.05: alertas de ocupación |
| **Portal de autoatención cliente** | Cloud (AWS) | Angular SPA + API Gateway | RF-16.02: tableros para clientes con datos en tiempo real y exportación |
| **Caché de indicadores** | Cloud (AWS) | Amazon ElastiCache (Redis) | RNF-11.01: latencia ≤ 5 min para despliegue de indicadores |

### 4.2 Diagrama de flujo de datos analíticos

```
┌─────────────────────────────────────────────────────────────┐
│                    FUENTES TRANSACCIONALES                   │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Preventa │  │  Bodega  │  │Transporte│  │ Cobranza │   │
│  │  (App)   │  │  (WMS)   │  │  (GPS)   │  │  (App)   │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│       │              │              │              │         │
└───────┼──────────────┼──────────────┼──────────────┼─────────┘
        │              │              │              │
        ▼              ▼              ▼              ▼
┌─────────────────────────────────────────────────────────────┐
│              MOTOR TRANSACCIONAL (Aurora PostgreSQL)         │
│  ┌─────────┐  ┌──────────┐  ┌───────────┐  ┌───────────┐  │
│  │ Preventa│  │ Inventario│  │Transporte │  │ Cobranza  │  │
│  │  (OLTP) │  │  (OLTP)  │  │  (OLTP)   │  │  (OLTP)   │  │
│  └────┬────┘  └────┬─────┘  └─────┬─────┘  └─────┬─────┘  │
└───────┼────────────┼───────────────┼────────────────┼───────┘
        │            │               │                │
        ▼            ▼               ▼                ▼
┌─────────────────────────────────────────────────────────────┐
│                  DMS CDC (extracción continua)               │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│            MOTOR ANALÍTICO (Redshift Serverless)             │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Dim-Tiempo   │  │ Dim-Cliente  │  │ Dim-Ruta     │     │
│  │ Dim-Producto │  │ Dim-Vehículo │  │ Dim-Zona     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              HECHOS (Fact Tables)                     │  │
│  │  fact_entregas │ fact_costos │ fact_inventario │ ... │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              MATERIALIZED VIEWS                       │  │
│  │  mv_otif_diario │ mv_costo_servir │ mv_fill_rate  │  │
│  │  mv_ocupacion_flota │ mv_rentabilidad_cliente     │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────────┬─────────────────────────────────┘
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼
┌───────────────────────┐  ┌───────────────────────┐
│   TABLERO GERENCIAL   │  │  DISTRIBUCIÓN EMAIL   │
│   (Grafana/Angular)   │  │  (SES + Celery Beat)  │
│                       │  │                       │
│  • RF-11.06: Operac.  │  │  • RF-11.01: Semanal  │
│  • RF-16.02: Cliente  │  │  • RF-11.01: Mensual  │
│  • RF-16.03: Alertas  │  │                       │
└───────────────────────┘  └───────────────────────┘
```

### 4.3 Justificación del desacople OLAP/OLTP (RNF-11.02)

El RNF-11.02 exige que las consultas analíticas **no degraden** los tiempos de respuesta transaccionales. Esto se resuelve mediante:

1. **Motor separado:** Redshift Serverless es un sistema OLAP independiente de Aurora PostgreSQL (OLTP). Las cargas analíticas corren en un clúster dedicado con recursos aislados.

2. **Extracción asíncrona:** DMS CDC copia cambios de Aurora → Redshift sin bloquear transacciones OLTP. La extracción es incremental y continua.

3. **Vistas materializadas pre-calculadas:** Los indicadores (OTIF, Fill Rate, Costo de Servir) se calculan como vistas materializadas en Redshift, que se refrescan periódicamente (cada 5–15 min según RNF-11.01). Las consultas de tablero leen de estas vistas, no de tablas crudas.

4. **Caché Redis para tableros:** Los resultados de consultas frecuentes se cachean en ElastiCache Redis, reduciendo aún más la carga sobre Redshift para dashboards de alta concurrencia.

**Resultado:** Picking en bodega mantiene latencia ≤ 1s y preventa ≤ 1.5s (RF de bodega/preventa) mientras los gerentes consultan tableros analíticos simultáneamente.

---

## 5. Componente de Costo de Servir

El cálculo del Costo de Servir (RF-11.02) es el requerimiento analítico más complejo del módulo, ya que consolida datos de 4 fuentes distintas:

| Componente de costo | Fuente de datos | Módulo productor | Fórmula simplificada |
|---------------------|----------------|------------------|----------------------|
| Combustible devengado | Telemetría GPS (litros/km) | Telemetría (Épica 14) | km recorridos × precio litro × rendimiento vehicular |
| Peajes | Registro de viaje | Transporte (Épica 6) | Monto real de peajes por viaje |
| Tiempo de conducción | Telemetría GPS (horas) | Telemetría (Épica 14) | Horas de conducción × costo hora conductor |
| Tiempo de descarga | App móvil de reparto | Transporte (Épica 6) | Minutos de descarga × costo hora |
| Costo de bodega (prorrateo) | WMS | Almacén (Épica 2) | Costo total bodega ÷ volumen almacenado × volumen cliente |
| Costo administrativo (prorrateo) | Facturación ERP | Administración | Costo fijo administrativo ÷ N pedidos × pedidos cliente |
| Costo de devoluciones/mermas | Logística inversa | Logística Inversa (Épica 8) | Costo de envases perdidos + productos dañados |
| Costo de mermas por vencimiento | Inventario | Almacén (Épica 2) | Valor de producto vencido imputado al cliente |

La fórmula de rentabilidad neta resultante (RF-11.08):

```
Margen neto = Ingreso por venta - Costo de mercadería - Costo de servir real
```

Donde el Costo de servir real = Σ(componentes anteriores) por cliente y por entrega.

---

## 6. Componente de Alertas de Negocio (RF-16.03)

Las alertas por síntomas de negocio se distinguen de las alertas de infraestructura en que miden **impacto al negocio**, no estado de servidores:

| Síntoma de negocio | Umbral configurable | Fuente de datos | Acción |
|--------------------|--------------------|--------------------|--------|
| OTIF diario < meta | < 95% (configurable) | Redshift (mv_otif_diario) | Notificación gerente comercial + calidad |
| Fill Rate mensual < meta | < 97% (configurable) | Redshift (mv_fill_rate) | Alerta gerente comercial |
| Costo de servir > umbral | > $X por entrega (configurable) | Redshift (mv_costo_servir) | Alerta gerente finanzas |
| Ocupación de flota < umbral | < 65% (configurable) | Redshift (mv_ocupacion_flota) | Alerta planificador de rutas |
| Excursión térmica en tránsito | > umbral por tipo producto | IoT/DynamoDB + SNS (Lambda validador) | Alerta conductor + calidad |
| Crédito de cliente excedido | Deuda + pedido > cupo | Aurora PostgreSQL (OLTP) | Bloqueo en app de preventa |
| Envases retornables excedidos | Saldo > umbral configurable | Aurora PostgreSQL (OLTP) | Alerta preventista |

---

## 7. Requerimientos de tableros (RT-05.25, RT-05.26)

Las Bases exigen tableros con las siguientes capacidades:

| Capacidad exigida | RT | Implementación |
|-------------------|----|--------------------|
| Tableros operacionales y de gestión | RT-05.25 | Dashboards separados: operacional (tiempo real, RF-11.06) y estratégico (periódico, RF-11.01) |
| Filtros por período | RT-05.26 | Filtros de rango de fechas en Grafana/Angular (hoy, semana, mes, trimestre, año) |
| Filtros por unidad organizacional | RT-05.26 | Filtros por zona, ruta, sucursal, cliente, canal de comercialización |
| Drill-down | RT-05.26 | Navegación de resumen → detalle: total → zona → ruta → cliente → entrega individual |
| Datos en tiempo real | RT-14.02 | Actualización cada ≤ 5 min (RNF-11.01) vía Redis cache + Redshift refresh |
| Acceso del cliente | RT-14.02 | Portal web Angular con autenticación Keycloak, RF-16.02 |
| Exportación | RT-16.28 | Descarga en PDF, XLSX, CSV con filtros aplicados, RF-17.12 |

### 7.1 Tablero operacional (RF-11.06)

| Panel | Indicadores mostrados | Fuente | Frecuencia actualización |
|-------|----------------------|--------|-------------------------|
| Avance de rutas | Pedidos completados / total, % avance por ruta | Aurora PostgreSQL (OLTP) | Tiempo real (< 1 min) |
| Entregas cumplidas | % OTIF del día, entregas a tiempo vs atrasadas | Redshift (mv_otif_diario) | ≤ 5 min |
| Devoluciones en tránsito | Cantidad de devoluciones, productos devueltos | Aurora PostgreSQL (OLTP) | Tiempo real |
| Alertas cadena de frío | Excursiones térmicas activas, historial 24h | DynamoDB (IoT) + SNS (Lambda validador) | Tiempo real |
| Recaudación del día | Monto recaudado en efectivo, cheques, transferencias | Aurora PostgreSQL (cobranza) | Tiempo real |

### 7.2 Tablero gerencial (RF-11.01)

| Reporte | Periodicidad | Indicadores | Destinatarios |
|---------|-------------|-------------|---------------|
| Reporte semanal ejecutivo | Cada lunes 06:00 AM | OTIF semanal, Fill Rate, Costo de Servir por zona, devoluciones | Gerente Comercial, Jefa de Calidad |
| Reporte mensual ejecutivo | Día 2 de cada mes | OTIF mensual, Fill Rate, Merma por vencimiento, Costo de Servir por zona y canal, rentabilidad por cliente | Gerente Comercial, Gerente de Finanzas, Jefa de Calidad |

---

## 8. Cumplimiento de Bases Administrativas

| Artículo Bases Admin. | Exigencia | Cumplimiento del módulo BI |
|----------------------|-----------|---------------------------|
| Art. 5° Capacidad Analítica | Proponer BI/OI como servicio horizontal | Módulo de BI como servicio horizontal sobre Redshift, consumido por todas las épicas |
| Cap. 5° Innovación | 1 innovación obligatoria (análisis predictivo) | Análisis predictivo de demanda (consumo de Redshift ML o SageMaker) usando histórico OTIF, Fill Rate y patrones de compra |
| Art. 39° Acceso a datos | Garantizar acceso y exportación de datos | Tableros con exportación PDF/XLSX/CSV (RF-17.12), portal de autoatención para clientes (RF-16.02) |

---

## 9. Resumen de cobertura

### 9.1 Conteo por origen

| Fuente | Cantidad de RF/RNF que alimentan al módulo BI |
|--------|-----------------------------------------------|
| Épica 11 (propios) | 8 RF + 2 RNF = 10 |
| Transversales (Bases) | 3 RF + 1 RNF = 4 |
| Otras épicas (dependencias) | 11 RF |
| **Total** | **25 requerimientos** |

### 9.2 Conteo por tipo de requerimiento

| Tipo | Cantidad |
|------|----------|
| Requerimientos funcionales (RF) | 22 |
| Requerimientos no funcionales (RNF) | 3 |
| **Total** | **25** |

### 9.3 Conclusión

El módulo de BI/Analítica no es una funcionalidad agregada por iniciativa propia de la propuesta. Es un componente **obligatorio** exigido por:

- Las Bases Técnicas Transversales (RT-05.25, RT-05.26, RT-14.02, RT-14.03, RT-14.04)
- El Caso 02 de Logística (indicadores OTIF, Fill Rate, Costo de Servir)
- 25 requerimientos trazables a las fuentes normativas

Su omisión constituiría una inconsistencia grave con las Bases y haría imposible la medición de los 3 indicadores estratégicos del negocio (OTIF > 95%, Fill Rate > 97%, Costo de Servir conocido y gestionable).

---

## Referencias

| Documento | Sección/Capítulo | Relevancia |
|-----------|-----------------|------------|
| Bases_Tecnicas_Transversales.md | RT-05.25, RT-05.26 | Capa analítica obligatoria con tableros |
| Bases_Tecnicas_Transversales.md | RT-14.02, RT-14.03, RT-14.04 | Acceso a tableros, SLI, alertas de negocio |
| Caso_02_Logistica.md | Cap. 4.1, 7.1, 7.2, 9.8 | Indicadores OTIF, Fill Rate, Costo de Servir |
| Bases_Administrativas.md | Art. 5°, Cap. 5°, Art. 39° | Capacidad analítica, innovación, acceso a datos |
| Consolidado RF.csv | Épica 11 (RF-11.01–RF-11.08) | 8 requerimientos funcionales del módulo |
| Consolidado RNF.csv | RNF-11.01, RNF-11.02 | Latencia y desacople OLAP/OLTP |
| Consolidado bases.csv | RF-16.02, RF-16.03, RF-17.12, RNF-16.01 | Tableros, alertas, exportación, SLI |
| Propuesta_Arquitectura_Cloud.md | §3.2.10, §3.2.15, §3.2.16 | Redshift, Grafana, reportes programados |
| Dimensionamiento_Infraestructura.md | §2.3, §3.3 | Dimensionamiento de Redshift y Grafana |
