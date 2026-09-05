# Sala de Servidores On-Premise v02
## Distribuidora Puelche S.A. — Caso 02 Logística · CD Talca

> **Documento:** Componente de Arquitectura Física — Diseño del recinto de Sala Técnica Secundaria (Cap. 6 / RT-06.01 a RT-06.34) y disponibilidad e2e (RT-10.01)
> **Versión:** 02
> **Referencias normativas:** Sala_De_Servidores.md (profesor, v2.1.0 — estructura de recintos, distribución, energía, clima, racks y cableado); Bases Técnicas Transversales Cap. 6 (RT-06.01 a RT-06.34) y Cap. 10 (RT-10.01)
> **Dependencia:** Tabla de Emplazamiento On-Premise v06 · Dimensionamiento de Infraestructura On-Premise v05 (clúster 3 nodos)
> **Contexto del caso:** La sala actual de Talca (25 m², split AC, UPS 10 min, acceso por llave) NO cumple el Cap. 6 de las Bases Técnicas Transversales (RT-06.20 biometría facial, RT-06.16 detección AnaLASER, RT-06.24 CCTV, RT-06.17 extinción). Este documento define la habilitación del nuevo recinto de sala técnica secundaria de Talca.

---

## 1. Escala y decisión de diseño

| Ítem | Decisión | Justificación |
|---|---|---|
| **Escala** | Sala **mediana** (25–45 m² de sala blanca; 4–12 gabinetes) | Clúster de 3 nodos virtualizados («el clúster mínimo son tres nodos» — profe §7), cableado estructurado certificado, piso técnico. 4 gabinetes cubren cómputo, almacenamiento, red/seguridad y crecimiento |
| **Redundancia** | Componentes N+1 (UPS, clima) + generador; **TIER II objetivo** | TIER II = 99,741 % (≈22,7 h/año caído): UPS + generador + N+1, mantenimiento con caída. Adecuado a criticidad del negocio (ventanas permitidas nocturnas). No se exige TIER III (mantenimiento sin caída) dado costo/RTO del caso. **El TIER II es la clasificación de la infraestructura del recinto (un medio); el compromiso contractual se mide sobre la transacción crítica de negocio de extremo a extremo con disponibilidad mensual ≥ 99,9 % (RT-10.01)** — ver Sección 7, alcanzado con HA de clúster 3 nodos, **enlaces WAN redundantes de 3 tecnologías (fibra + satelital Starlink + LTE, conmutación < 30 s)** y UPS/generador y DRP |
| **Superficie del programa** | Sala blanca **32 m²**; programa completo ≈ **173 m²** | Dentro de 25–45 m² de referencia para 8–12 racks; espacio para 2 filas enfrentadas con pasillo frío confinado, pasillos de servicio de 0,9 m y esclusa interior; incluye recinto de custodia de medios de respaldo (10 m²) |

---

## 2. Programa de recintos (14 recintos)

Tomado de Sala_De_Servidores.md §2 (tabla de los trece recintos), ajustado a las superficies del proyecto y ampliado con el recinto de custodia de medios de respaldo (RT-06.26/RT-06.27):

| Recinto | Función | Quién entra | Línea | m² |
|---|---|---|---|---|
| **Sala de servidores** (sala blanca) | Aloja los 4 racks: cómputo, almacenamiento, red/seguridad, crecimiento | Operador autorizado, acompañado | **3ª** | **32** |
| **Sala de monitoreo (NOC)** | Pantallas DCIM/BMS, consola, alarmas, bitácora | Operación (Jefe de TI) y turno | 2ª | **14** |
| **Sala de climatización** | Unidades de precisión N+1, filtros, tablero del clima | Proveedor de clima, acompañado | 2ª/3ª | **12** |
| **Sala de extinción** | Cilindros FM-200 (RT-06.17), tablero de control, señalética | Proveedor certificado | 2ª | **5** |
| **Control de acceso y custodia** | Guardia, registro de visitas, credenciales, CCTV | Todos, al entrar | **1ª** | **10** |
| **Sala de UPS y baterías** | UPS doble conversión N+1 y banco de baterías (VRLA) | Eléctrico y proveedor | 2ª | **14** |
| **Sala/patio de generador** | Grupo electrógeno + estanque (**24 h**), contención de derrames | Proveedor, con permiso | **Ext.** | **20** |
| **Acometida de comunicaciones (MMR)** | Llegada de enlaces (fibra + LTE + **terminal satelital Starlink por antena en techumbre**), equipos de operadores, ductos de ingreso | Proveedores externos | 2ª | **10** |
| **Acometida eléctrica** | Empalme, tablero general, ATS/TTA | Eléctrico autorizado | 2ª | **10** |
| **Sala de reparación (taller)** | Diagnóstico y armado fuera de la sala blanca | Técnicos | 1ª | **12** |
| **Bodega de insumos** | Repuestos, cables, tapas ciegas, filtros, consumibles | Operación | 1ª | **10** |
| **Custodia de medios de respaldo** | Custodia física de medios de respaldo del sitio primario (RT-06.26): medio transportable a otro lugar a solicitud del CLIENTE; recinto acondicionado con luminosidad, humedad, ventilación controladas (RT-06.27) y control de acceso/inventario | Custodio acreditado por el CLIENTE, con registro | 2ª | **10** |
| **Sala de reuniones** | Proveedores, auditorías, capacitación | Con invitación | 1ª | **14** |
| **Baños y servicios** | Fuera del perímetro técnico, sin muro común con la sala | Todos | **Fuera** | — |

> **Adyacencias obligadas (cumplidas aquí):** NOC contiguo a la sala blanca con ventana interior («ver sin entrar»); climatización contigua con puerta propia; UPS junto a la acometida eléctrica (recorrido de fuerza corto); MMR antes de la última línea (2 operadores, ductos de ingreso distintos + **antena Starlink en techumbre con cableado exterior protegido hasta la MMR — RT-06.32**); extinción pegada a la sala con cañería corta; bodega y taller cerca del acceso (no cruzar el perímetro con cajas).
>
> **Prohibiciones respetadas:** sin baños ni cañerías de agua sobre/pegadas a la sala; estanque de combustible **exterior** con contención de derrames; banco de baterías en recinto propio ventilado (hidrógeno + peso, losa verificada); generador en patio exterior (ruido, vibración, gases); sin bodega de material combustible (cartón/plumavit) en el perímetro. Las **instalaciones sanitarias existentes del edificio** (baños de visita, fuera del perímetro técnico y sin muro común con la sala) se declaran en uso tal como están (RT-06.31).

---

## 3. Esquema de distribución elegido y plano de zonificación

### 3.1 Esquema de racks

**Dos filas enfrentadas: pasillo frío confinado.** R01 y R02 frente a R03 y R04, con cerramiento y techo del pasillo frío (confina el aire, evita recirculación).

| Parámetro | Valor |
|---|---|
| Configuración | 2 filas de 2 gabinetes enfrentadas |
| Pasillo frío (entre R01-R02 y R03-R04) | **1,2 m**, confinado con techo + puertas correderas |
| Pasillos calientes (externos, traseros) | 0,9 m cada uno, ventilación superior |
| Fondo de gabinetes | **800 × 1.100 mm** (servidores 1U de perfil completo) |
| Piso técnico | **40 cm** de pleno, baldosas perforadas solo en pasillo frío, sellado de pasadas, detección de agua bajo el piso, rampa de acceso |
| Crecimiento | Margen 20–30 % por gabinete + **R04 dedicado a crecimiento** |

> Se evalúan alternativas superadas: fila única con pasillo caliente confinado (se descarta por menor superficie de pleno de distribución de aire con piso técnico de 40 cm) y pasillo frío sin confinar (gana 1 m de superficie pero pierde entre 15 y 30 % de eficiencia de climatización — se elige el confinado).

### 3.2 Plano de distribución interna con líneas de acceso (RT-06.03 — dibujo requerido)

```
LEVENDA:  [( )] = recinto · *) puerta controlada con credencial ·  ◎) esclusa antipassback
          ⌂ ventana interior (NOC a sala blanca, "ver sin entrar") · D) sala blanca · EXTERIOR = generador

┌───────────────────────────────────────────────────────────────────────────────┐
│                       EDIFICIO EXISTENTE (contexto del CLIENTE)                │
└───────────────────────────────────────────────────────────────────────────────┘
            │  ENTRADA * (guardia + libro de visitas) — 1ª LÍNEA
            ▼
 ┌──────────────────────────┬───────────────────────────┬───────────────────────┐
 │  [( )] CONTROL DE ACCESO │  [( )] SALA DE REUNIONES  │  [( )] TALLER         │
 │  Y CUSTODIA        10 m² │                   14 m²   │  12 m²  + [( )]       │
 │  guardia, credenciales,  │  proveedores / auditorías │  BODEGA INSUMOS 10 m² │
 │  CCTV                    │                           │                       │
 └─────────────┬────────────┴─────────────┬─────────────┴───────────┬───────────┘
                |  puerta controlada (custodia autoriza)              |
               ▼  ▼                                                     ▼
 ┌────────────────────────────────────────────────────────────────────────────────┐
 │                2ª LÍNEA — PASILLO DE SERVICIO (corredor técnico)                │
 │                                                                                │
 │  ┌──────────┐ ┌──────────┐ ┌────────────┐ ┌─────────┐ ┌───────────────┐      │
 │  │ ACOMET.  │ │ MMR      │ │ UPS + BATER.│ │ EXTINCIÓN│ │ CLIMATIZACIÓN │     │
 │  │ ELÉCTRICA│ │ COMUNIC. │ │  14 m² N+1  │ │ 5 m²     │ │  12 m² N+1    │     │
 │  │ 10 m² *  │ │ 10 m² *  │ │  VRLA +     │ │ FM-200   │ │  precisión    │     │
 │  │ empalme+ │ │ 2 ductos  │ │  ventilación│ │ RT-06.17*│ │  (2 equipos,  │     │
 │  │ ATS/TTA  │ │ (fibra,  │ │  losa verif.│ │          │ │  free cooling)│     │
 │  │          │ │  LTE)    │ │             │ │          │ │               │     │
 │  └──────────┘ └──────────┘ └─────────────┘ └─────────┘ └───────────────┘     │
 └────────────────────────────────────────────────────────────────────────────────┘
            |  esclusa de 3.ª línea: doble factor + esclusa antipassback (RT-06.20)
            ▼  ▼
 ┌───────────────────────────────┬───────────────────────────────────────────────┐
 │                               │  ⌂                                             │
 │   [( )]  SALA BLANCA (D)     │  [( )] NOC — MONITOREO                        │
 │   32 m²                     │  14 m²                                         │
 │   ┌────────┐     ┌────────┐ │  DCIM/BMS, alarmas, bitácora                  │
 │   │  R01   │     │  R03   │ │  ventana de vidrio hacia la sala              │
 │   │ SERVIDORES    │ HDA/RESP│ │                                               │
 │   └────────┘     └────────┘ │  nadie entra a la sala para monitorear         │
 │   piso técnico 40 cm        │                                               │
 │   ┌────────┐     ┌────────┐ │                                               │
 │   │  R02   │     │  R04   │ │                                               │
 │   │ RED/SEG│     │ CRECIM.│ │                                               │
 │   └────────┘     └────────┘ │                                               │
 └───────────────────────────────┴───────────────────────────────────────────────┘
            ▼
 ┌────────────────────────────────────────────────────────────────────────────────┐
 │  EXTERIOR — PATIO DE GENERADOR: grupo electrógeno 12 kVA + estanque 24 h (      │
 │  NCh 2777), contención de derrames, prueba mensual con carga real; acceso con  │
 │  permiso; se entra desde el exterior, NO desde la sala.                        │
 └────────────────────────────────────────────────────────────────────────────────┘

          1ª LÍNEA (edificio) ──► 2ª LÍNEA (zona técnica) ──► 3ª LÍNEA (sala blanca)
```

> **Recorrido de una visita:** el proveedor de fibra entra por la custodia (1ª Línea) y va directo a la MMR (2ª Línea); **nunca pisa la sala blanca**. El que repara un disco entra al taller (1ª Línea). Solamente el operador autorizado, registrado y acompañado cruza la esclusa biocontrolada de la 3ª Línea.
>
> **Ubicación del recinto de custodia de medios (2ª Línea):** se incorpora dentro del programa de la 2ª Línea contiguo a la bodega de insumos, con puerta controlada propia (acceso del custodio acreditado sin cruzar la sala blanca) y condiciones ambientales de §4.5 (RT-06.27). El plano esquemático anterior se actualiza en el plano de arquitectura formal (RT-06.03) con este decimocuarto recinto.

---

## 4. Seguridad física y monitoreo

### 4.1 Cuatro capas de acceso (conforme a profe §4)

| Línea | Mecanismo | Registro | RT correlacionada |
|---|---|---|---|
| **1ª — edificio** | Guardia, credencial visible, libro de visitas | Nombre, empresa, motivo, hora entrada/salida | — |
| **2ª — zona técnica** | Tarjeta de proximidad con perfil por recinto | Traza electrónica por persona y puerta | — |
| **3ª — sala blanca** | **Doble factor + esclusa antipassback** | Traza, acompañamiento, bitácora de tarea | **RT-06.20** |
| **4ª — rack** | Cerradura electrónica por gabinete | Bitácora con Nº de rack y U intervenida | RT-06.05 |

**RT-06.20 (ingreso):** se instala control de acceso **biométrico facial como mecanismo principal**, con **AFIS como respaldo** (lector dactilar externo). La esclusa interior incorpora antipassback: nadie puede abrir la puerta de salida y colarse a la sala; se exige acompañamiento y bitácora de tarea. Número de puertas controladas del diseño: **12** (custodia, MMR, eléctrica, UPS, climatización, extinción, taller, bodega, custodia de medios de respaldo, NOC, esclusa de sala, acceso de sala).

**RT-06.23 (ingreso a la sala):** el acceso se realiza **al término del pasillo** (final de la 2ª Línea, en la esclusa), **una persona a la vez** (la esclusa impide abrirse por ambos lados simultáneamente) y con **re-verificación biométrica** en cada apertura (anti tailgating); la puerta se cierra tras cada ingreso. Toda entrada/salida queda en la bitácora electrónica (RT-06.21).

### 4.2 Detección e incendio

| Sistema | Especificación | RT |
|---|---|---|
| **Detección temprana** | **AnaLASER** por aspiración de aire con tecnología láser (o equivalente superior), + detectores puntuales de humo y temperatura | **RT-06.16** |
| **Extinción automática** | **Agente limpio FM-200** (HFC-227ea) aprobado UL, instalación conforme NFPA 75/2001; cilindros en la sala de extinción; preaviso "EVACUAR", tiempo de evacuación 20–30 s, **botón de aborto**, retención sellada | **RT-06.17** |
| **Extinción manual + extintores portátiles (RT-06.18)** | Pozo/red de aro con agente para el cuarto de apoyo; NO agua sobre equipos energizados. **Extintores portátiles declarados por recinto:** polvo ABC 10 lb en pasillos y recintos de apoyo (≥ 1 por recinto ocupado ≥ 5 m²) y **CO₂** en sala blanca y sala de UPS (protección de equipos energizados); revisión y recarga anual certificada y señalética según norma | NFPA 75 · **RT-06.18** |
| **Sensores ambientales (RT-06.14)** | **Monitoreo en línea de temperatura, humedad y agua** (bajo el piso técnico y en bandeja de condensado) integrado al DCIM/BMS del NOC con alarmas a la central y al Jefe de TI on-call; aire exclusivo de la sala (no se cambia el termostato desde el muro), oxígeno bajo en sala con extinción por gas, puerta abierta, vibración, presencia fuera de horario | RT-06.14 |

### 4.3 CCTV y videovigilancia (RT-06.24)

| Parámetro | Valor |
|---|---|
| Cámaras IP | **7** (cada puerta controlada —incluida la del recinto de custodia de medios— y los dos pasillos de la sala blanca); visión nocturna (IR), funcionan a oscuras |
| Grabación | **En línea y disponible ≥ 30 días recientes**; grabaciones anteriores respaldadas en **medio secundario recuperable y auditable** (NAS local + almacenamiento de objetos en nube) |
| Integración | El video se integra al control de acceso: "la puerta marca el video"; un solo tablero DCIM/BMS en el NOC |

**RT-06.24 (respaldo):** se declara respaldo de grabaciones en dispositivo secundario con retención declarada, recuperable y auditable, conforme a la RT.

### 4.4 ¿Quién contesta a las 3 AM?

| Ítem | Compromiso |
|---|---|
| Destinatario | Central de alarmas tercerizada + **Jefe de TI on-call** (rotativo), además del NOC |
| Canal | SMS/email/push simultáneo; escalamiento al ADJUDICATARIO si no hay respuesta en 15 min |
| Tiempo de respuesta | Confirmación remota ≤ 15 min; presencia física en Talca ≤ 90 min (ciudad) |
| Procedimiento escrito | Bitácora de alarmas, secuencia de escalamiento, plan de respuesta a incendio/agua/corte; simulacro anual de evacuación y de recarga de agente |

### 4.5 Custodia física de medios de respaldo del sitio primario (RT-06.26)

**Servicio de custodia declarado (RT-06.26):** para el sitio primario (Talca) se habilitará un **servicio de custodia de medios de respaldo en un medio físico transportable a otro lugar cuando el CLIENTE lo determine**. El NAS local D-05 (Tabla v06 + Dimensionamiento v05 §1.2.4) entrega la copia local de recuperación rápida; sobre esa base se genera un **medio de respaldo transportable** (unidad/disco extraíble cifrado, conforme RT-07.10), que rota (RT-06.28) y se traslada bajo **servicio de custodia/transporte acreditado** hacia una **bóveda de custodia externa** (otro lugar, distinto del sitio primario) señalada por el CLIENTE. Se admite la solución propuesta en 3-2-1-1-0 (pierna inmutable en nube S3) como **complementaria**, pero la custodia física **transportable a otro lugar** se declara explícitamente como medio propio (medio físico + servicio de transporte con cadena de custodia y bitácora RT-06.28).

| Ítem | Declaración |
|---|---|
| Medio de respaldo transportable | Cifrado (RT-07.10/RT-11.09), etiquetado, inventario (RT-06.28) |
| Periodicidad de rotación | Semanal (sincronizada con respaldo completo diario 02:00–04:00) |
| Transporte y custodia externa | Servicio de custodia y transporte acreditado del ADJUDICATARIO o tercero con garantía; retiro/prestación del medio al recinto custodia (2ª línea) |
| Bóveda / otro lugar | Otro lugar geográfico (p. ej., bóveda bajo contrato en otra comuna); dirección y acceso restringido declarable al CLIENTE |
| Cuándo se traslada | Cuando el CLIENTE lo determine (eventualidad, contingencia o auditoría); también verificación periódica de legibilidad desde el medio custodiado |
| Trazabilidad | Bitácora electrónica de entrada/salida de medios (RT-06.28), acta de transporte, cadena de custodia |

**Condiciones ambientales del recinto de custodia (RT-06.27):** el recinto de **10 m²** de la 2ª línea (programa §2) cumple las siguientes exigencias para no afectar la calidad ni la disponibilidad de los medios de respaldo:

| Factor | Valor declarado |
|---|---|
| **Luminosidad** | Iluminación LED sin componente UV; ≤ 300 lux en zonas de estantería; sin exposición a luz solar directa |
| **Humedad relativa** | **40–60 %** (misma envolvente climática del recinto técnico, ASHRAE TC 9.9) |
| **Ventilación** | Renovación de aire forzada con filtrado G4/F7, sin condensación; presurización leve frente al pasillo |
| **Temperatura** | **18–27 °C** (igual rango ASHRAE del recinto técnico) |
| **Otros factores** | Estantería metálica firme (sísmica), sin fuentes magnéticas/EMI cercanas, detección de humo/agua al DCIM/BMS, extintor CO₂, acceso controlado (RT-06.20) e inventario sellado (RT-06.28) |

> El recinto de custodia de medios **no forma parte de la 3ª Línea**: es un recinto de apoyo de 2ª Línea, accesible al custodio acreditado sin necesidad de ingresar a la sala blanca (ver §3.2).

---

## 5. Energía y clima

### 5.1 Cadena eléctrica (siete eslabones)

```
Empalme único (distribuidora) → Tablero general → ATS/TTA (transferencia) → UPS doble conversión N+1
→ PDU de rack (A y B) → Fuente del equipo (dobles fuentes en A/B) → Servidor
```

| Eslabón | Especificación | Protección |
|---|---|---|
| **Empalme** | Único, monofásico/trifásico según disponibilidad local; potencia a contratar ≈ **6 kW** | Generador: corte → ATS parte en 8–15 s; prueba mensual con carga real y bitácora firmada |
| **Tablero general** | Protecciones selectivas, tierra, mag-thermo | Termografía periódica semestral (**RT-06.10**) |
| **ATS/TTA** | Transferencia automática red ↔ generador | Prueba mensual con carga real |
| **UPS** | **Doble conversión on-line, 6 kVA, configuración N+1**, con bypass manual; **autonomía ≥ 30 min a plena carga (RT-06.07)** — banco VRLA dimensionado a 30 min; el generador toma la carga en 8–15 s | Un módulo de respaldo asume la carga; bypass permite mantenimiento sin apagar la sala |
| **PDU del rack** | **2 PDU verticales por gabinete (A y B)** en lados opuestos, con medidor | Alimentación A y B por caminos/ductos independientes (verificar siguiendo el cable) |
| **Fuente del equipo** | Monitores/PDU con conexión A/B; servidores con doble fuente opcional | — |

**Dónde están los tres recintos eléctricos (profe §2):** Acometida eléctrica (empalme + ATS, **accesible desde fuera del perímetro**: cortar la energía no exige cruzar tres puertas), Sala de UPS y baterías (2ª línea, **ventilación obligatoria por hidrógeno + losa verificada**), y Patio de generador (exterior, estanque **24 h** + contención de derrames + **contrato de reabastecimiento** declarado — RT-06.08).

### 5.2 Dimensionamiento de potencia y autonomía

| Paso (método del profesor §5) | Cálculo | Resultado |
|---|---|---|
| Potencia por rack | R01 (servidores) ≈ 1,5 kW · R02 (red/seguridad + **router Starlink D-06**) ≈ 0,7 kW · R03/R04 ≈ 0,3 kW | **0,7 kW promedio** · R01 = rack de mayor densidad (1,5 kW) |
| Carga TI de diseño | 3 nodos (~1,4 kW) + NAS + red/seguridad + Gateway + **kit Starlink (~0,08 kW)** ≈ **2,5 kW** × 1,25 holgura crecimiento 3 años | **≈ 3,1 kW** |
| Capacidad de UPS | 3,1 kW ÷ 0,8 factor de utilización = 3,9 kVA | **UPS 6 kVA doble conversión N+1** (con bypass manual) |
| Autonomía | **≥ 30 min a plena carga (RT-06.07)** — banco VRLA dimensionado a 30 min | El generador toma en 8–15 s; margen amplio para apagado ordenado (al 20 % de batería ≈ T-24 min) |
| Factor de potencia | Objetivo **≥ 0,95** con banco de corrección en el tablero general | Cumple RT-06.11 (kW, factor de potencia y PUE declarados) |
| Carga total del sitio | TI (3,1 kW) × PUE 1,7 ≈ 5,3 kW + iluminación ≈ 0,3 kW | **≈ 5,6 kW** |
| Generador | Cubre TI + clima + partida de motores | **12 kVA**, estanque **24 h** (RT-06.08), prueba mensual con carga real, **contrato de reabastecimiento declarado** y monitoreo de nivel de estanque |
| Potencia a contratar | Se declara ante la distribuidora con margen | **≈ 6,2 kW** |

**La secuencia del corte (profe §5, con autonomía RT-06.07/06.08):**
1. **T-0:** corta la red → el UPS N+1 (≥ 30 min) sostiene sin corte perceptible; alarmas activas a NOC + celular del Jefe de TI.
2. **T-5 a 15 s:** ATS parte el generador; toma la carga completa (TI + clima). 
3. **T-15 a 60 s:** BMS verifica transferencia; los racks quedan por PDU A/B; el clima pasa a generador.
4. **T-2 a 24 min:** si el generador no tomó, el UPS sostiene hasta los 30 min; al **20 % de batería (~T-24 min)** se inicia **apagado ordenado automático** (secuencia: BD WMS primero, luego VMs web, al final hipervisores).
5. **T-24 h:** permanencia en generador con estanque de **24 h** (RT-06.08), monitoreo de nivel y **contrato de reabastecimiento** que garantiza continuidad más allá de las 24 h.

> **Regla que resume el diseño:** por encima del cielo de la sala no pasa ninguna cañería de agua salvo la del propio clima, y esa va con **detección de fuga bajo la bandeja de condensado**.

### 5.3 Clima de precisión (N+1, ASHRAE TC 9.9)

| Parámetro | Valor |
|---|---|
| Carga térmica | Consumo TI ≈ **3,1 kW** + pérdidas UPS ≈ 0,3 kW + iluminación/personas → **≈ 3,6 kW de diseño** |
| Unidades | **2 unidades de precisión (CRAC) de ≈ 12.000 BTU/h (3,5 kW) cada una, en N+1**, montadas en la sala de climatización; velocidades variables; **free cooling** cuando el aire exterior está más frío que el retorno (zona central de Chile, sobre todo de noche) |
| Redundancia | N+1: si una unidad falla, la otra asume la carga completa sin cortar la sala |
| Temperatura | **18–27 °C** ASHRAE TC 9.9, **medida en la toma de aire del equipo** (no en el muro) |
| Humedad relativa | **40–60 % HR** |
| Confinamiento | Pasillo frío confinado con techo y puertas + tapas ciegas en toda U vacía + sellado de pasadas del piso técnico + baldosas perforadas solo en el pasillo frío → ahorro declarado de **15–30 %** en energía de climatización |
| Si el clima cae por completo | Alcanza el límite térmico de los servidores 1U en **≈ 10–15 min**; el BMS ordena apagado térmico por secuencia (temp ≥ 30 °C a la toma) ANTES de daño; procedimiento escrito |

### 5.4 PUE de diseño, puntos de medición y compromiso

**PUE = Energía total de la instalación ÷ Energía entregada al equipamiento TI.**

- **PUE de diseño: 1,7** (la sala mediana de referencia del profesor; free cooling + confinamiento + UPS de doble conversión eficiente).
- **Punto de medición Nº 1 (Numerador):** medidor de energía total en el **tablero general de la acometida eléctrica** (incluye TI + clima + iluminación + pérdidas del UPS).
- **Punto de medición Nº 2 (Denominador):** **suma de los PDU de los 4 racks** (energía entregada al equipamiento TI, medida en cada PDU con medidor).
- **Compromiso:** el ADJUDICATARIO mide ambos puntos de forma **continua (medidores en línea)**, reporta el PUE al CLIENTE **trimestralmente con informe** y mantiene **meta operacional PUE ≤ 1,7**; cualquier desviación > 0,2 activa plan de mejora de climatización.

---

## 6. Racks y cableado

### 6.1 Cálculo de racks (método en 8 pasos del profesor §6)

| Paso | Cálculo | Resultado |
|---|---|---|
| 1 — U de cómputo | 3 nodos 1U (Nodo-1/2/3) + NAS D-05 2U | **5 U** |
| 2 — U de almacenamiento | NAS contado en cómputo (D-05); sin arreglo externo (Ceph integrado a los nodos Proxmox, Dimensionamiento v05) | **0 U adicionales** |
| 3 — U de red y seguridad | 2 switches core (2U) + 2 firewalls UTM (2U) + 1 switch de gestión (1U) + Gateway IoT (1U) | **6 U** |
| 4 — U de infraestructura | Patch panels fibra + cobre (4U) + organizadores (4U) + consola KVM (1U) | **≈ 9 U** |
| 5 — Subtotal | 5 + 6 + 9 | **≈ 20 U** |
| 6 — U utilizables por gabinete | 42U − 25–30 % reserva de crecimiento | **≈ 30 U/gabinete** |
| 7 — Racks necesarios | 20 ÷ 30 | **1** (redondeado) |
| 8 — Racks del diseño | Cómputo + red/seguridad separados (**RT-06.05**), + respaldo/crecimiento + gabinete de operadores | **4 gabinetes** |

### 6.2 Distribución de los 4 gabinetes y ocupación proyectada

| Rack | Función | Equipamiento | U ocupadas (de 42U) | Margen de crecimiento |
|---|---|---|---|---|
| **R01** | **Servidores y almacenamiento** | Nodo-1, Nodo-2, Nodo-3 (1U c/u), NAS D-05 (2U), Gateway IoT (1U) | 5 → 9 U con paneles/organizadores | ≈ 30 % (programado físico en U 31–24 con tapas ciegas) |
| **R02** | **Comunicaciones y seguridad** (rack **independiente de servidores — RT-06.05**) | 2 switches core L3 (stack/MLAG), 2 firewalls UTM HA, 1 switch de gestión, patch panels de enlace | ≈ 15 U | ≈ 20 % |
| **R03** | **Red de distribución (HDA) + respaldo local** | Patch panels de fibra OM4/cat6A, cableado horizontal certificado | ≈ 12 U | ≈ 30 % |
| **R04** | **Crecimiento / operadores** | Paneles + espacio reservado 3 años (no se instala hoy) | ≈ 8 U | **100 % (gabinete de crecimiento)** |

### 6.3 Elevación del gabinete R01 (dibujo requerido — profe §6)

```
                      R01 — SERVIDORES Y ALMACENAMIENTO (42U, 800×1100 mm)
   ┌──────────────────────────────────────────────┐
   │ U42  │ Patch panel fibra OM4 (troncal HDA)    │────────── patch panels (donde llega la red)
   │ U41  │ Patch panel cobre Cat6A 24 puertos    │
   │ U40  │ Organizador horizontal                 │
   │ U39  │ NODO-1 — hipervisor clúster (1U)      │
   │ U38  │ NODO-2 — hipervisor clúster (1U)      │────────── cómputo a la altura del pecho
   │ U37  │ NODO-3 — hipervisor clúster (1U)      │          (se manipula sin agacharse)
   │ U36  │ Organizador horizontal                 │
   │ U35  │ Gateway IoT Greengrass (B-02, 1U)     │
   │ U34  │ NAS D-05 (2U) — respaldo local        │────────── almacenamiento (pesado, abajo)
   │ U33  │  (NAS D-05, continuación)             │
   │ U32  │ Consola KVM (1U)                      │
   │ U31–U24 │ TAPAS CIEGAS · reserva 20 %       │────────── 20 % libre SIEMPRE con tapa ciega
   │ U23–U48 │ (sin usar, tapas ciegas)           │
   │ PDU-A │ (lado izquierdo) · PDU-B (derecho)   │────────── 2 PDU verticales A/B, lados opuestos
   └──────────────────────────────────────────────┘
```

> **Reglas aplicadas a todos los racks:** PDU vertical A/B en lados opuestos (caminos eléctricos distintos), tapas ciegas en toda U vacía, organizadores horizontales entre equipos activos, gabinete anclado al piso (no vuelca, ~500–900 kg cargado), puertas que abren el 100 % (no pegado al muro ni a la fila vecina), latiguillos < 1,5 m.

### 6.4 Cableado estructurado certificado

| Aspecto | Especificación |
|---|---|
| **Topología** | **ANSI/TIA-942: ENI → MDA → HDA → ZDA → EDA** |
| **ENI** | Entrada de instalación en la **MMR** (sala de acometida de comunicaciones): llegan fibra óptica y LTE de los 2 operadores, cada uno por **ducto distinto**, más la **antena Starlink en techumbre** con cableado exterior protegido hasta el router de la MMR (RT-06.32); frontera de responsabilidad de cada contrato |
| **MDA** | Distribuidor principal (Rack R02): repartidores de fibra OM4 y cobre, switch core L3 | 
| **HDA/ZDA** | Distribuidores horizontales (R03/R02): troncales de fibra hacia cada ZDA de fila |
| **EDA** | Áreas de equipos: patch panels en cada gabinete (U40/R01, etc.) |
| **Medios** | **Cat 6A F/UTP** horizontal (10 Gbps hasta 100 m) · **Fibra OM4** troncal (10–100 Gbps 150–400 m) · latiguillos bajo 1,5 m · DAC dentro del rack para nodos ↔ switch |
| **Separación datos/energía** | Bandejas distintas o separación física ≥ 20 cm; cruces a 90°; radio mínimo de curvatura respetado en la fibra |
| **Etiquetado** | Nomenclatura declarada **`R01-U38-P12`** (rack-U-puerto), rotulando **ambos extremos**; planilla/DCIM actualizada el mismo día; **colores por función** (gestión, producción, respaldo, DMZ) |
| **Certificación** | Cableado nuevo **certificado con equipo y con informe entregable** (item de costo del proyecto); incluye canalización |
| **Gabinete de comunicaciones separado** | R02 cumple **RT-06.05**: racks de servidores son independientes de los racks de equipos de comunicación |

> **Interfaces hacia el resto del sitio:** se declara el recorrido del cableado desde la sala hasta la bodega (APs Wi-Fi 6E industriales, terminales MC9400), con hitos de certificación por tramo y una planilla CCIS/DCIM única de toda la red on-premise.

---

## 7. Parámetros declarados (ficha técnica — anexo del profesor)

| Parámetro | Unidad | Valor declarado |
|---|---|---|
| Superficie de la sala de servidores | m² | **32 m² útiles** (sala blanca) + ≈ 141 m² de recintos de apoyo |
| Esquema de distribución | tipo y holguras | **2 filas enfrentadas (2+2 racks), pasillo frío confinado de 1,2 m, pasillos calientes de 0,9 m** |
| Cantidad de racks y ocupación | gabinetes y % U | **4 gabinetes de 42U; ocupación actual ≈ 20–25 % de la capacidad útil; reserva 20–30 % por gabinete + R04 de crecimiento** |
| Potencia por rack | kW | **0,7 kW promedio; 1,5 kW el rack de mayor densidad (R01)** |
| Carga TI de diseño | kW | **3,1 kW con 25 % de holgura a 3 años** |
| PUE estimado | adimensional | **1,7** (diseño), con compromiso de medición continua en 2 puntos y reporte trimestral |
| Factor de potencia | adimensional | **≥ 0,95** con banco de corrección en tablero general (RT-06.11) |
| Capacidad y topología del UPS | kVA y configuración | **6 kVA doble conversión on-line, N+1, con bypass manual** |
| Autonomía de respaldo | minutos | **≥ 30 min a plena carga (RT-06.07)**; generador toma la carga en 8–15 s |
| Generador | kVA y horas de estanque | **12 kVA — 24 h de estanque (RT-06.08)**, prueba mensual con carga real, contrato de reabastecimiento |
| Carga térmica y clima | kW y configuración | **≈ 3,6 kW — 2 unidades de precisión (≈12.000 BTU/h c/u) en N+1**, con free cooling |
| Temperatura y humedad | °C y % HR | **18–27 °C y 40–60 % HR** en la toma de aire de los equipos (ASHRAE TC 9.9) |
| Nivel de disponibilidad objetivo | TIER y % | **Infraestructura del recinto: TIER II (99,741 %)**; **compromiso contractual e2e de la transacción crítica: ≥ 99,9 % mensual (RT-10.01)** |
| Enlaces | Mbps y proveedores | **Fibra 50 Mbps (D-03) · Starlink respaldo automático plan 1 TB (D-06) · LTE 10 Mbps terciario (D-04) — 3 caminos/proveedores distintos, conmutación < 30 s** (2 ductos MMR + antena Starlink en techumbre) |
| RTO y RPO | horas | **RTO 4 h · RPO 15 min** (alineado con Dimensionamiento v05 y cloud) |
| Puertas controladas | cantidad | **12 puertas** (4 líneas de acceso; incluye recinto de custodia de medios) |
| CCTV | cámaras y retención | **7 cámaras IP, grabación ≥ 30 días en línea + respaldo secundario auditable (RT-06.24)** |

---

## 8. Cumplimiento de requisitos del Cap. 6 (RT-06.01 a RT-06.24)

| Requisito | Estado | Cómo se cumple |
|---|---|---|
| **RT-06.01** — tipología de sala | Cumple | Sala Técnica Secundaria de Talca habilitada a nuevo (la sala actual de 25 m² no cumplía Cap. 6); gabinetes de borde en Concepción y 3 cross-docking según Tabla v06 |
| **RT-06.05** — racks independientes de comunicación | Cumple | R02 (comunicaciones) separado de R01 (servidores); ocupación proyectada y margen declarados por rack (§6.2) |
| **RT-06.07** — autonomía de respaldo | Cumple | UPS doble conversión N+1 con **autonomía ≥ 30 min a plena carga**, banco VRLA dimensionado a 30 min; generador toma la carga en 8–15 s (§5.1 y §5.2) |
| **RT-06.08** — generación autónoma mín. 24 h | Cumple | Grupo electrógeno con estanque de **24 h**, contención de derrames, monitoreo de nivel y **contrato de reabastecimiento declarado** (§2 y §5.2) |
| **RT-06.10** — medición semestral instalaciones eléctricas | Cumple | Termografía y medición semestral con informe entregable al CLIENTE; sincronizada con la prueba DR semestral |
| **RT-06.11** — kW, factor de potencia y PUE | Cumple | Carga proyectada ≈ 3,1 kW declarada, **factor de potencia ≥ 0,95** con banco de corrección y **PUE 1,7** con medición continua en 2 puntos y reporte trimestral (§5.2, §5.4 y §7) |
| **RT-06.14** — sensores ambientales | Cumple | Monitoreo en línea de temperatura, humedad y agua (bajo piso técnico y bandeja de condensado) al DCIM/BMS del NOC, con alarmas (§4.2) |
| **RT-06.16** — detección temprana por aspiración | Cumple | AnaLASER o equivalente con tecnología láser en la sala blanca (+ detectores puntuales) |
| **RT-06.17** — extinción automática agente limpio | Cumple | FM-200 aprobado UL, instalación NFPA 75/2001, preaviso, evacuación y botón de aborto |
| **RT-06.18** — extinción manual y extintores | Cumple | Pozo/red de aro para cuartos de apoyo; extintores portátiles declarados por recinto (ABC 10 lb en pasillos/soporte y **CO₂** en sala blanca y UPS), revisión y recarga anual certificada (§4.2) |
| **RT-06.20** — acceso biométrico facial | Cumple | Control de acceso biométrico facial (principal) + AFIS de respaldo; 3ª Línea con esclusa antipassback |
| **RT-06.23** — acceso a la sala | Cumple | Acceso al término del pasillo, **una persona a la vez** con re-verificación biométrica (anti tailgating) y registro en bitácora electrónica (§4.1) |
| **RT-06.24** — CCTV ≥ 30 días + respaldo | Cumple | 7 cámaras IP en línea ≥ 30 días (cubre cada puerta controlada —incluida la de custodia de medios— y los pasillos de la sala blanca); grabaciones históricas en medio secundario recuperable y auditable |
| **RT-06.26** — custodia de medios de respaldo del sitio primario | Cumple | Servicio de custodia en **medio físico transportable a otro lugar** cuando el CLIENTE lo determine (§4.5): medio cifrado rotado semanal, transporte/custodia acreditada a bóveda externa, alta/retiro registrados (RT-06.28); la pierna inmutable S3 es complementaria, no reemplaza la custodia física |
| **RT-06.27** — condiciones ambientales del recinto de custodia | Cumple | Recinto de custodia de **10 m²** (2ª línea) con luminosidad (LED sin UV, ≤ 300 lux), humedad **40–60 %**, ventilación forzada filtrada, 18–27 °C y monitoreo DCIM/BMS — §4.5 |
| **RT-06.28** — inventario de medios | Cumple | Inventario de medios de respaldo (NAS local + almacenamiento de objetos) con **rotación**, verificación periódica de legibilidad y **registro de todo movimiento de entrada y salida**; parte de la bitácora electrónica del NOC |
| **RT-06.31** — uso de sanitarias y áreas existentes | Cumple | Se utiliza tal como están los baños de visita, zonas de seguridad y áreas exteriores existentes del edificio del CLIENTE, declaradas en §2; no se reconstruyen (RT-06.31) |
| **RT-10.01** — disponibilidad e2e | Cumple | **Disponibilidad mensual ≥ 99,9 % de extremo a extremo** sobre la transacción crítica de negocio (venta/despacho), declarada como compromiso contractual; la TIER II es la clasificación de la infraestructura del recinto, no el SLO e2e (§1 y §7) |
| **RT-06.01 a RT-06.24 (resto)** | Cumple | Energía (UPS N+1 + generador + ATS), clima de precisión N+1 ASHRAE, piso técnico, cableado ANSI/TIA-942 certificado, monitoreo DCIM/BMS, seguridad física por capas |

---

*Versión 01 — Entregable de Sala de Servidores alineado a Tabla de Emplazamiento v05 y Dimensionamiento v04. Decide clúster de virtualización de 3 nodos, 4 gabinetes (R01 servidores, R02 comunicaciones, R03 HDA/respaldo, R04 crecimiento), TIER II objetivo, PUE de diseño 1,7 con medición comprometida en 2 puntos (tablero general + PDU de racks), y cumplimiento íntegro de RT-06.01 a RT-06.24. Las superficies de los 13 recintos y el plano de zonificación con las tres líneas de acceso se presentan en §2 y §3.*

*Versión 02 — Corrección de brechas de la Matriz de Cumplimiento BTT (on-premise): generador con estanque **24 h** y contrato de reabastecimiento (RT-06.08); autonomía de UPS **≥ 30 min a plena carga** (RT-06.07); **factor de potencia ≥ 0,95** y PUE con medición (RT-06.11); **sensores ambientales en línea** de temperatura, humedad y agua (RT-06.14); **extintores por recinto** ABC/CO₂ (RT-06.18); acceso a la sala **una persona a la vez** con re-verificación biométrica (RT-06.23); inventario de medios con rotación y registro de movimientos (RT-06.28); uso declarado de instalaciones sanitarias existentes (RT-06.31); **disponibilidad e2e ≥ 99,9 % mensual sobre la transacción crítica** (RT-10.01), distinta de la clasificación TIER II del recinto. Referencias cruzadas actualizadas a Tabla v06 y Dimensionamiento v05.*

*Versión 03 — Cierre de pendientes de la Matriz (RT-06.26/RT-06.27): recinto de **custodia de medios de respaldo de 10 m²** incorporado al programa de recintos (14 recintos, 2ª línea); servicio de custodia de medios del sitio primario en **medio físico transportable a otro lugar** cuando el CLIENTE lo determine (cuando la custodia externa opera con bóveda bajo contrato y bitácora RT-06.28); condiciones ambientales del recinto (luminosidad LED sin UV, humedad 40–60 %, ventilación forzada, 18–27 °C) declaradas en §4.5; puertas controladas pasan de 11 a **12** y CCTV de 6 a **7** (cubre la puerta del recinto de custodia); superficie del programa ≈ **173 m²**. Referencias cruzadas a Tabla v06 (D-05) y Dimensionamiento v05 (NAS D-05).*
