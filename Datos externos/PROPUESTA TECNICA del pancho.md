> Nota de conversión: se conserva el texto original sin resumir. Se han reconstruido los títulos, listas y tablas, y se han omitido los encabezados y números de página repetidos. Los comentarios HTML identifican las páginas del PDF. Las imágenes enlazadas reproducen las páginas que contienen gráficos para conservar su disposición visual. La paginación y la maquetación no se reproducen en Markdown; las tablas que continúan entre páginas permanecen separadas.

<!-- Página 1 del PDF original -->

# Propuesta Técnica: Consultora Médica

### Proyecto Semestral

Pontificia Universidad Católica de Valparaíso

Valparaíso, November 2025

![Página 1 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-001.png)

<!-- Página 2 del PDF original -->

## Contenido

Lista de Figuras ix

Lista de Tablas xiii

1 Resumen Ejecutivo 1

2 Descripción del Proponente 4

- 2.1 Misión de la empresa  - 4

- 2.2 Visión de la empresa  - 4

- 2.3 Responsabilidad de la empresa  - 4

- 2.4 Credenciales organizacionales y madurez en gestión de tecnología  - 5

- 2.5 Capacidad instalada para proyectos TIC complejos  - 5

- 2.6 Experiencia en integración de sistemas heterogéneos  - 6

- 2.7 Credenciales financieras del proponente  - 6

- 2.8 Equipo de trabajo y credenciales técnicas  - 6

3 Alcance del Servicio 8

- 3.1 Definición del problema  - 8

- 3.1.1 Actores  - 9

- 3.1.2 Objetivos  - 11

- 3.1.3 Definición de alcance  - 11

- 3.1.4 Exclusiones  - 12

- 3.1.5 Supuestos  - 13

3.1.6 Acuerdos de niveles de servicio mínimos (SLA’s prometidos): . 14

- 3.2 Implementación  - 15

- 3.2.1 Metodología  - 16

- 3.2.2 Planificación  - 16

- 3.2.3 Normas y estándares a aplicar  - 17

- 3.2.4 Gestión de Dependencias Críticas y Riesgos Técnicos  - 22

- 3.2.5 Arquitectura de la Solución  - 23

- 3.2.6 Plan de Recursos  - 23

- 3.3 Implantación  - 24

- 3.3.1 Migración de datos  - 24

- 3.3.2 Despliegue en ambientes productos  - 25

<!-- Página 3 del PDF original -->

- 3.3.3 Pruebas de validación y ajuste  - 26

- 3.3.4 Marcha blanca/Piloto  - 27

- 3.3.5 Puesta en producción  - 28

- 3.4 Operación  - 29

- 3.4.1 Soporte  - 29

- 3.4.2 Monitoreo  - 29

- 3.4.3 Mantenimiento y Actualizaciones  - 30

- 3.4.4 Presupuesto de errores SRE  - 30

- 3.4.5 Seguridad  - 33

- 3.4.6 Capacitación a Usuarios  - 33

- 3.4.7 Capacidades de auto-recuperación del sistema  - 34

- 3.4.8 Plan de Rollback  - 35

4 Descripción Lógica de la Solución 37

- 4.1 Esquema Solución  - 37

- 4.1.1 Esquema General de la solución  - 39

- 4.1.2 Módulo Pacientes  - 42

- 4.1.3 Módulo Comunicación  - 43

- 4.1.4 Módulo Gestión  - 44

- 4.1.5 Módulo Finanzas  - 45

- 4.1.6 Módulo Cadena de Suministro  - 46

- 4.1.7 Módulo Integración  - 47

- 4.2 Arquitectura Lógica  - 47

- 4.2.1 Capa Cliente  - 48

- 4.2.2 Capa de Presentación  - 49

- 4.2.3 Capa de Negocio  - 50

- 4.2.4 Capa Cache  - 51

- 4.2.5 Capa de Datos  - 51

- 4.2.6 Capa de Servicios Externos  - 51

- 4.2.7 Arquitectura Lógica: Pacientes  - 52

- 4.2.8 Arquitectura Lógica: Personal Médico  - 53

- 4.2.9 Arquitectura Lógica: Personal Administrativo  - 55

- 4.2.10 Arquitectura Lógica: Gerente y Dirección  - 56

- 4.2.11 Arquitectura Lógica: Administrador TI  - 58

- 4.2.12 Especificación Tecnológica  - 58

5 Arquitectura Física de la Solución 64

- 5.1 Arquitectura Física de la Solución  - 64

- 5.1.1 Diagrama General de la Arquitectura Física  - 65

- 5.1.2 Arquitectura Física de Sitios Edge  - 66

- 5.1.3 Arquitectura Física de la Aplicación Web  - 67

- 5.1.4 Arquitectura Física de la Base de Datos  - 69

<!-- Página 4 del PDF original -->

- 5.1.5 Arquitectura Física de los Microservicios  - 71

5.1.6 Arquitectura de Integración y Despliegue Continuo (CI/CD) . . 72

6 Ventajas de la Solución 74

- 6.1 Ventajas de la propuesta de la Arquitectura Lógica  - 74

- 6.2 Ventajas de la propuesta de la Arquitectura Física  - 75

- 6.3 Ventajas de la propuesta Tecnológica de la Aplicación  - 76

- 6.3.1 Análisis Comparativo de Desempeño y Arquitectura  - 77

- 6.3.2 Justificación Técnica por Dimensión  - 77

- 6.3.3 Aspectos de Ingeniería de Software  - 78

- 6.4 Ventajas de la propuesta Tecnológica de la Base de Datos  - 78

7 Metodologías 81

- 7.1 Metodología de Gestión de Proyectos  - 81

- 7.2 Metodología de Desarrollo de Software  - 82

- 7.3 Implicancias y Beneficios del Enfoque Metodológico  - 83

8 Plan de Trabajo 84

- 8.1 Plan de Trabajo  - 84

- 8.2 EDT  - 84

- 8.3 Diccionario de la EDT  - 85

- 8.3.1 Fase 1: Inicio  - 85

- 8.3.2 Fase 2: Diseño  - 93

- 8.3.3 Fase 3: Desarrollo  - 97

- 8.3.4 Fase 4: Obras Civiles y Montajes  - 105

- 8.3.5 Fase 5: Adquisiciones, Contratos y Documentación  - 110

- 8.3.6 Fase 6: Capacitaciones  - 115

- 8.3.7 Fase 7: Puesta en Producción  - 117

- 8.3.8 Fase 8: Finalización de Proyecto  - 123

- 8.3.9 Fase 9: Mantención  - 127

- 8.4 Carta Gantt  - 131

- 8.4.1 Inicio (H1)  - 132

- 8.4.2 Diseño (H2)  - 133

→

- 8.4.3 Desarrollo (H3 H4)  - 133

- 8.4.4 Obras Civiles y Montaje (H5)  - 133

- 8.4.5 Intervención (H6)  - 134

- 8.4.6 Capacitaciones (H7)  - 134

- 8.4.7 Puesta en Producción (H8)  - 134

- 8.4.8 Finalización del Proyecto  - 134

- 8.5 Plan de Implantación y Puesta en Marcha  - 135

- 8.5.1 Objetivo del plan  - 135

- 8.5.2 1 - Preparación de Ambientes y Orquestación:  - 135

8.5.3 2 - Despliegue Controlado (Canary y Rolling Updates):(2 semanas)136

<!-- Página 5 del PDF original -->

- 8.5.4 3 - Pruebas de Aceptación, Rendimiento y Resiliencia:  - 137

- 8.5.5 4 - Marcha Blanca y Puesta en Producción:  - 138

- 8.5.6 5 - Estabilización, Monitoreo y Rollback:  - 139

9 Plan de Riesgo 142

- 9.1 Metricas  - 142

- 9.1.1 Criterios de evaluación  - 142

- 9.1.2 Tipos de respuesta  - 143

- 9.2 Categorías de Riesgos  - 143

- 9.2.1 Resumen de los riesgos identificados  - 144

- 9.2.2 Riesgos de la Solución (RS)  - 144

- 9.2.3 Riesgos de Desarrollo (RD)  - 149

- 9.2.4 Riesgos de Implantación (RI)  - 152

- 9.3 Análisis Cuantitativo y Complementario  - 156

10 Plan de Calidad 159

- 10.1 Métricas de Calidad del Código  - 159

- 10.1.1 Análisis Estático y Dinámico  - 160

- 10.2 Verificación y Validación  - 160

- 10.2.1 Verificación  - 161

- 10.2.2 Validación  - 161

- 10.3 Trazabilidad de Requisitos  - 162

- 10.4 Mecanismos y Procesos de Aseguramiento de Calidad  - 162

- 10.5 Roles y Responsabilidades en el Aseguramiento de Calidad  - 163

- 10.6 Herramientas y Consideraciones Técnicas para la Calidad  - 163

- 10.7 Mejora Continua  - 164

11 Servicios de Operación 165

- 11.1 Especificaciones del Call Center y SLA’s  - 165

- 11.1.1 Servicios de Call Center  - 165

- 11.1.2 SLI’s de Call Center y servicio de soporte  - 166

- 11.1.3 Herramientas multicanal:  - 167

- 11.1.4 Teoría de Colas y Dimensionamiento Óptimo  - 168

- 11.1.5 Acuerdos Internos (OLA) y Contratos de Soporte (UC)  - 169

- 11.2 Soporte Técnico (Mesa de Ayuda TI N1-N4)  - 170

- 11.2.1 Estructura Escalonada de Soporte (Niveles 1-4)  - 171

- 11.2.2 Severidades de Incidentes y Protocolos de Escalamiento  - 173

- 11.2.3 Gestión del Conocimiento, Automatización y Runbooks  - 175

- 11.2.4 Observabilidad de Extremo a Extremo y AIOps  - 177

- 11.2.5 Capacidad de Auto-Sanacion y mantenimiento Proactivo  - 178

<!-- Página 6 del PDF original -->

12 Plan de Operación 180

- 12.1 Plan de Mantención  - 180

- 12.1.1 Enfoque General de Ingeniería de Confiabilidad  - 180

- 12.1.2 Estrategia RCM (Reliability Centered Maintenance)  - 181

- 12.1.3 Mantención Preventiva  - 182

- 12.1.4 Mantención Predictiva Basada en ML/AI  - 183

- 12.1.5 Mantención Evolutiva  - 183

- 12.1.6 Métricas de Degradación y Umbrales de Intervención  - 184

- 12.1.7 Gobernanza y Gestión del Mantenimiento  - 184

- 12.2 Plan Servicios de Operación  - 184

- 12.2.1 Modelo Operativo Basado en SRE  - 185

- 12.2.2 Observabilidad Integral  - 185

- 12.2.3 Automatización y Reducción de Toil  - 186

- 12.2.4 SLO, SLA y Error Budgets  - 186

- 12.2.5 Chaos Engineering  - 187

- 12.2.6 Gestión de Incidentes y Blameless Postmortems  - 187

- 12.2.7 Prácticas FinOps para Optimización de Costos  - 187

13 Equipo de trabajo, Subcontrataciones y Alianzas 189

- 13.1 Estructura Organizacional del Proyecto  - 189

- 13.1.1 Organización del equipo de firmas  - 189

- 13.1.2 Visión general de la estructura organizacional  - 190

- 13.1.3 Capa de Gobierno / Jefaturas  - 191

- 13.1.4 Capa de Ejecución Técnica de la Solución  - 192

- 13.2 Subcontrataciones y alianzas estratégicas  - 199

- 13.2.1 Criterios make-or-buy  - 200

- 13.2.2 Selección de partners  - 201

- 13.2.3 Gobernanza de proveedores (SLA/OLA)  - 202

- 13.2.4 Riesgos y mitigaciones  - 203

- 13.3 Transferencia tecnológica y gestión del conocimiento  - 203

14 Innovaciones 206

- 14.1 Diagnóstico asistido mediante Inteligencia Artificial  - 206

- 14.1.1 Análisis de factibilidad:  - 206

- 14.1.2 Pruebas de concepto:  - 207

- 14.1.3 Gestión de riesgos:  - 207

- 14.1.4 Investigación aplicada y desarrollo experimental:  - 207

- 14.1.5 Beneficios esperados:  - 207

- 14.2 Monitoreo remoto de pacientes con IoT (Internet de las Cosas)  - 208

- 14.2.1 Análisis de factibilidad:  - 208

- 14.2.2 Pruebas de concepto:  - 208

- 14.2.3 Gestión de riesgos:  - 208

<!-- Página 7 del PDF original -->

- 14.2.4 Investigación aplicada y desarrollo experimental:  - 209

- 14.2.5 Beneficios esperados:  - 209

- 14.3 Gestión de datos clínicos con blockchain  - 209

- 14.3.1 Análisis de factibilidad:  - 209

- 14.3.2 Pruebas de concepto:  - 210

- 14.3.3 Gestión de riesgos:  - 210

- 14.3.4 Investigación aplicada y desarrollo experimental:  - 210

- 14.3.5 Beneficios esperados:  - 210

- 14.4 Triaje Inteligente Automatizado  - 210

- 14.4.1 Análisis de factibilidad:  - 211

- 14.4.2 Pruebas de concepto:  - 211

- 14.4.3 Gestión de riesgos:  - 211

- 14.4.4 Investigación aplicada y desarrollo experimental:  - 211

- 14.4.5 Beneficios esperados:  - 211

- 14.5 Realidad Aumentada para Procedimientos  - 211

- 14.5.1 Análisis de factibilidad:  - 212

- 14.5.2 Pruebas de concepto:  - 212

- 14.5.3 Gestión de riesgos:  - 212

- 14.5.4 Investigación aplicada y desarrollo experimental:  - 212

- 14.5.5 Beneficios esperados:  - 212

- 14.6 Predicción de No-Show con Machine Learning  - 213

- 14.6.1 Análisis de factibilidad:  - 213

- 14.6.2 Pruebas de concepto:  - 213

- 14.6.3 Gestión de riesgos:  - 213

- 14.6.4 Investigación aplicada y desarrollo experimental:  - 213

- 14.6.5 Beneficios esperados:  - 213

15 Ventajas y Beneficios - Consolidación 214

- 15.1 Análisis cuantitativo de los beneficios  - 214

- 15.2 Comparación con soluciones tradicionales  - 215

- 15.3 Alineación con los objetivos estratégicos del cliente  - 217

- 15.4 Resumen ejecutivo de beneficios  - 218

- 15.5 Optimización de la triple restricción  - 218

16 ANEXOS 220

- 16.1 Requerimientos Funcionales del Proyecto  - 220

- 16.1.1 Módulo de Historia Clínica Electrónica  - 220

- 16.1.2 Módulo de Gestión de Pacientes  - 222

- 16.1.3 Módulo de Agendamiento Multicanal  - 223

- 16.1.4 Módulo de CRM con call center  - 225

- 16.1.5 Módulo de Facturación y Cobranza  - 227

- 16.1.6 Módulo de Seguimiento de Pacientes  - 228

<!-- Página 8 del PDF original -->

- 16.1.7 Módulo de Telemedicina  - 230

- 16.1.8 Módulo de Recursos Humanos Digital  - 233

- 16.1.9 Módulo de Reportería y Analytics  - 235

- 16.1.10 Módulo de Operaciones  - 238

- 16.2 Requerimientos NO Funcionales del Proyecto  - 242

- 16.2.1 Modulo de Arquitectura y Diseño del Sistema  - 242

- 16.2.2 Módulo de Rendimiento, Escalabilidad y Capacidad  - 245

- 16.2.3 Modulo de Disponibilidad y Resiliencia  - 248

- 16.2.4 Módulo de Seguridad de la Información  - 250

- 16.2.5 Módulo de Operación y Mantenimiento  - 252

- 16.2.6 Módulo de Integración e Interoperabilidad  - 254

- 16.2.7 Módulo de Cumplimiento Normativo y Certificaciones  - 256

- 16.2.8 Módulo de Hardware e Infraestructura  - 258

- 16.2.9 Módulo de Usabilidad  - 260

- 16.3 Requerimientos del proyecto  - 260

- 16.4 EDT Completa  - 261

<!-- Página 9 del PDF original -->

This page intentionally left blank.

<!-- Página 10 del PDF original -->

## Lista de Figuras

- 4.1 Esquema general de la solución - 39

- 4.2 Módulo de Pacientes  - 42

- 4.3 Módulo de Comunicación  - 43

- 4.4 Módulo de Gestión  - 44

- 4.5 Módulo de Finanzas  - 45

- 4.6 Módulo de Cadena de Suministro  - 46

- 4.7 Arquitectura Lógica  - 48

- 4.8 Arquitectura Lógica: Caso de Pacientes  - 52

- 4.9 Arquitectura Lógica: Caso de Personal Médico  - 54

- 4.10 Arquitectura Lógica: Caso de Personal Administrativo  - 55

- 4.11 Arquitectura Lógica: Caso de Gerencia y Dirección  - 57

- 4.12 Arquitectura Lógica: Caso de Administrador TI  - 58

5.1 Diagrama general de la arquitectura física de la solución propuesta (Data

- Center Primario y Secundario)  - 66

- 5.2 Diagrama de arquitectura física para Sitios Edge y servicios locales  - 67

- 5.3 Arquitectura física detallada de la aplicación web  - 69

5.4 Arquitectura física detallada de la Zona de Datos, almacenamiento y repli-

- cación P2P  - 70

- 5.5 Arquitectura física Microservicios  - 72

- 5.6 Arquitectura Física CI/CD Multi-Site  - 73

- 8.1 Estructura de desglose del Trabajo (EDT)  - 84

- 8.2 Fase 1 - Inicio  - 85

- 8.3 Paquete - 1.1 Definición Inicial  - 86

- 8.4 Paquete - 1.2 Alcance del Proyecto  - 86

- 8.5 Subpaquete - 1.2.2 Captura de requerimientos  - 87

- 8.6 Paquete - 1.3 Planificación del Proyecto  - 88

- 8.7 Paquete - 1.4 Gestión de Costos  - 89

- 8.8 Paquete - 1.5 Gestión de Calidad  - 90

- 8.9 Paquete - 1.6 Gestión de Riesgos  - 91

- 8.10 Paquete - 1.7 Gestión de Proveedores  - 92

- 8.11 Fase - 2 Diseño  - 93

<!-- Página 11 del PDF original -->

- 8.12 Paquete - 2.1 Arquitectura de la Solución  - 94

- 8.13 Paquete - 2.2 Procesos TO-BE  - 94

- 8.14 Paquete - 2.3 UX-UI  - 95

- 8.15 Paquete - 2.4 Validación de Diseño  - 96

- 8.16 Fase - 3 Desarrollo  - 97

- 8.17 Paquete - 3.1 Setup de Ambientes  - 97

- 8.18 Subpaquete - 3.1.1 Ambientes  - 98

- 8.19 Paquete - 3.2 Módulos del Sistema  - 99

- 8.20 Paquete - 3.3 Integraciones Fundamentales  - 100

- 8.21 Subpaquete - 3.3.2 Integraciones financieras y Previsionales  - 101

- 8.22 Subpaquete - 3.3.3 Dispositivos externos  - 102

- 8.23 Subpaquete - 3.3.4 Integración con sistemas externos  - 103

- 8.24 Subpaquete - 3.3.5 Documentación técnica  - 103

- 8.25 Subpaquete - 3.4 Plan de migración de Datos  - 104

- 8.26 Fase - 4 Obras Civiles y Montaje  - 105

- 8.27 Paquete - 4.1 Adecuación de Espacios  - 105

- 8.28 Paquete - 4.2 Cableado Estructurado  - 106

- 8.29 Paquete - 4.3 Equipamiento de Campo  - 107

- 8.30 Paquete - 4.4 Sistemas de Seguridad  - 108

- 8.31 Paquete - 4.5 Configuración de la Infraestructura  - 109

- 8.32 Fase - 5 Intervención  - 110

- 8.33 Paquete - 5.1 Migración de datos maestros  - 111

- 8.34 Paquete - 5.2 Configuración de parámetros  - 111

- 8.35 Paquete - 5.3 SW y licencia  - 112

- 8.36 Paquete - 5.4 Contratos y acuerdos con Proveedores  - 113

- 8.37 Paquete - 5.5 Riesgo de adquisiciones  - 114

- 8.38 Fase - 6 Capacitaciones  - 115

- 8.39 Paquete - 6.1 Capacitación Masiva por roles  - 116

- 8.40 Paquete - 6.2 Evaluaciones y Certificaciones  - 116

- 8.41 Fase - 7 Puesta en Producción  - 117

- 8.42 Paquete - 7.1 Permisos de Centro  - 117

- 8.43 Paquete - 7.2 Hypercare 24x7  - 118

- 8.44 Paquete - 7.3 Estabilización  - 119

- 8.45 Paquete - 7.4 Ajustes por feedback  - 120

- 8.46 Paquete - 7.5 Preparación rollout  - 121

- 8.47 Paquete - 7.6 Pruebas de carga/stress  - 122

- 8.48 Fase - 8 Finalización de Proyecto  - 123

- 8.49 Paquete - 8.1 - Término de Actividades  - 124

- 8.50 Paquete - 8.2 - Recepción de entregables  - 125

- 8.51 Paquete - 8.3 - Cierre de Contratos  - 126

- 8.52 Paquete - 8.4 - Cierre de proyecto  - 127

- 8.53 Fase - 9 Mantención  - 128

<!-- Página 12 del PDF original -->

- 8.54 Fase - 9.1 Plan de mantención  - 128

- 8.55 Fase - 9.2 Plan de pruebas integrales  - 129

- 8.56 Fase - 9.3 Ajustes y optimizaciones  - 130

- 8.57 Carta Gantt  - 132

- 9.1 Diagrama RBS  - 144

- 9.2 Diagrama FTA  - 158

- 13.1 Organización del equipo de firmas del proponente - 189

- 13.2 Estructura organizacional completa del proyecto HospiNet - 190

- 13.3 Capa de Gobierno y Jefaturas del proyecto - 191

- 13.4 Capa de Ejecución Técnica de la Solución - 192

13.5 Zoom del frente Funcional, QA & Documentación dentro de la Capa de

- Ejecución Técnica - 193

13.6 Zoom del frente de Integración, Infraestructura & Soporte dentro de la Capa

- de Ejecución Técnica - 195

13.7 Zoom del frente de Desarrollo & UX dentro de la Capa de Ejecución Técnica. 197

- 16.1 1ra pag. - Requerimientos del proyecto  - 260

- 16.2 Estructura de desglose del Trabajo (EDT)  - 261

<!-- Página 13 del PDF original -->

This page intentionally left blank.

<!-- Página 14 del PDF original -->

## Lista de Tablas

- 2.1 Equipo del proponente y credenciales técnicas - 7

- 3.1 Niveles de Servicio (SLA) y Métricas de Desempeño  - 14

- 3.2 Disponibilidad por servicio  - 14

- 3.3 Perfomance  - 15

- 3.4 Recuperación  - 15

- 3.5 Servicio: SLA’s Call Center  - 15

- 3.6 Migración de datos a BD  - 25

- 3.7 Presupuesto de Errores - Site Reliability Engineering (SRE)  - 30

- 6.1 Comparativo Técnico entre Arquitecturas  - 77

- 6.2 Aspectos de Ingeniería Aplicados en HOSPINET  - 78

- 8.1 Fases de la EDT: Cuentas de Control (CC) y Paquetes de Trabajo (PT)  - 85

- 8.2 1.1 Definición Inicial Paquete - Diccionario de la EDT  - 86

- 8.3 1.2 Alcance del Proyecto Paquete - Diccionario de la EDT  - 87

- 8.4 1.2.2 Captura de requerimientos Subpaquete - Diccionario de la EDT  - 88

- 8.5 1.3 Planificación del Proyecto Paquete - Diccionario de la EDT  - 88

- 8.6 1.4 Gestión de Costos Paquete - Diccionario de la EDT  - 90

- 8.7 1.5 Gestión de Calidad Paquete - Diccionario de la EDT  - 91

- 8.8 1.6 Gestión de Riesgos Paquete - Diccionario de la EDT  - 92

- 8.9 1.7 Gestión de Proveedores Paquete - Diccionario de la EDT  - 93

- 8.10 2.1 Arquitectura de Solución Paquete - Diccionario de la EDT  - 94

- 8.11 2.2 Procesos TO-BE Paquete - Diccionario de la EDT  - 95

- 8.12 2.3 UX/UI Paquete - Diccionario de la EDT  - 96

- 8.13 2.4 Validación de diseños Paquete - Diccionario de la EDT  - 97

- 8.14 3.1 Setup de ambientes Paquete - Diccionario de la EDT  - 98

- 8.15 3.1.1 Ambientes Subpaquete - Diccionario de la EDT  - 99

- 8.16 3.2 Módulos del sistema Paquete - Diccionario de la EDT  - 99

- 8.17 3.3 Integraciones fundamentales Paquete - Diccionario de la EDT  - 101

8.18 3.3.2 Integraciones Financieras y Previsionales Subpaquete - Diccionario

- de la EDT  - 101

- 8.19 3.3.3 Dispositivos externos Subpaquete - Diccionario de la EDT  - 102

<!-- Página 15 del PDF original -->

8.20 3.3.4 Integración con sistemas externos Subpaquete - Diccionario de la EDT 103 8.21 3.3.5 Documentación y Cierre Técnico Subpaquete - Diccionario de la EDT 104

- 8.22 3.4 Plan de Migración de Datos Subpaquete - Diccionario de la EDT  - 104

- 8.23 4.1 Adecuación de espacios Paquete - Diccionario de la EDT  - 106

- 8.24 4.2 Cableado estructurado Paquete - Diccionario de la EDT  - 107

- 8.25 4.3 Equipamiento de campo Paquete - Diccionario de la EDT  - 108

- 8.26 4.4 Sistemas de seguridad Paquete - Diccionario de la EDT  - 109

- 8.27 4.5 Configuración de infraestructura Paquete - Diccionario de la EDT  - 110

- 8.28 5.1 Permisos y Cumplimiento Paquete - Diccionario de la EDT  - 111

- 8.29 5.2 Hardware e Infraestructura Paquete - Diccionario de la EDT  - 112

- 8.30 5.3 Software y Licencia Paquete - Diccionario de la EDT  - 113

8.31 5.4 Contratos y Acuerdos con Proveedores Paquete - Diccionario de la EDT 114

- 8.32 5.5 Riesgos de Adquisiciones Paquete - Diccionario de la EDT  - 115

- 8.33 6.1 Capacitación Masiva por roles  - 116

- 8.34 6.2 Evaluaciones y certificaciones Paquete - Diccionario de la EDT  - 117

- 8.35 7.1 Permisos de Centro Paquete - Diccionario de la EDT  - 118

- 8.36 7.2 Hypercare 24x7 Paquete - Diccionario de la EDT  - 119

- 8.37 7.3 Estabilización Paquete - Diccionario de la EDT  - 120

- 8.38 7.4 Ajustes por feedback Paquete - Diccionario de la EDT  - 121

- 8.39 7.5 Preparación rollout Paquete - Diccionario de la EDT  - 122

- 8.40 7.6 Pruebas de Carga/Stress Paquete - Diccionario de la EDT  - 123

- 8.41 8.1 Termino de actividades Paquete - Diccionario de la EDT  - 124

- 8.42 8.2 Recepción de entregables Paquete - Diccionario de la EDT  - 125

- 8.43 8.3 Cierre de Contratos Paquete - Diccionario de la EDT  - 126

- 8.44 8.4 Cierre del proyecto Paquete - Diccionario de la EDT  - 127

- 8.45 9.1 Plan de Mantención Paquete - Diccionario de la EDT  - 128

- 8.46 9.2 Plan de Pruebas Integrales Paquete - Diccionario de la EDT  - 130

- 8.47 9.3 Ajustes y Optimizaciones Paquete - Diccionario de la EDT  - 131

- 9.1 Escala de Probabilidad  - 142

- 9.2 Escala de Impacto  - 143

- 9.3 Matriz de Prioridad (Probabilidad × Impacto)  - 143

- 9.4 Evaluación de Riesgos de la Solución (RS)  - 146

- 9.5 Evaluación de Riesgos del Desarrollo (RD)  - 150

- 9.6 Evaluación de Riesgos de Implantación (RI)  - 154

- 9.7 Resumen del Análisis FMEA para los riesgos más críticos - 157

- 9.8 Acciones correctivas y responsables asociados al análisis FMEA - 158

- 11.1 SLI, SLA y SLO asociados al Call Center y Plataforma  - 166

- 11.2 Niveles de Soporte Técnico TI y Responsabilidades Principales  - 172

- 15.1 Indicadores cuantitativos de beneficios proyectados  - 215

15.2 Comparación entre solución tradicional y solución propuesta HospiNet . . 216

<!-- Página 16 del PDF original -->

- 15.3 Alineación de HospiNet con los objetivos estratégicos del cliente  - 217

- 16.1 Requerimientos del Módulo de Historia Clínica Electrónica  - 220

- 16.2 Requerimientos del Módulo de Historia Clínica Electrónica  - 221

- 16.3 Requerimientos del Módulo de Gestión de Pacientes  - 222

- 16.4 Requerimientos del Módulo de Agendamiento Multicanal  - 223

- 16.5 Requerimientos del Módulo de Agendamiento Multicanal  - 224

- 16.6 Requerimientos del Módulo de CRM con call center  - 226

- 16.7 Requerimientos funcionales de Facturación y Cobranza  - 227

- 16.8 Requerimientos funcionales de Seguimiento de Pacientes  - 228

- 16.9 Requerimientos funcionales de Seguimiento de Pacientes  - 229

- 16.10Requerimientos funcionales de Telemedicina  - 230

- 16.11Requerimientos funcionales de Telemedicina  - 231

- 16.12Requerimientos funcionales de Recursos Humanos Digital  - 233

- 16.13Requerimientos funcionales de Recursos Humanos Digital  - 234

- 16.14Requerimientos del Módulo de Reportería y Analytics  - 235

- 16.15Requerimientos del Módulo de Reportería y Analytics  - 236

- 16.16Requerimientos funcionales de Operaciones  - 238

- 16.17Requerimientos funcionales de Operaciones  - 239

- 16.18Requerimientos funcionales de Operaciones  - 240

- 16.19Requerimientos funcionales de Operaciones  - 241

- 16.20Modulo de Arquitectura y Diseño del Sistema  - 243

- 16.21Requerimientos Módulo de Rendimiento, Escalabilidad y Capacidad  - 245

- 16.22Requerimientos Módulo de Rendimiento, Escalabilidad y Capacidad  - 246

16.23Requerimientos no funcionales de Rendimiento, Escalabilidad y Capacidad 247

- 16.24Modulo de Arquitectura y Diseño del Sistema  - 248

- 16.25Modulo de Arquitectura y Diseño del Sistema  - 249

- 16.26Requerimientos No Funcionales Módulo de Seguridad  - 250

- 16.27Requerimientos no funcionales de Modulo de Seguridad  - 251

- 16.28Requerimientos no funcionales de Operación y Mantenimiento  - 252

- 16.29Requerimientos no funcionales de Operación y Mantenimiento  - 253

- 16.30Requerimientos no funcionales de Integración e Interoperabilidad  - 254

- 16.31Requerimientos no funcionales de Integración e Interoperabilidad  - 255

16.32Requerimientos no funcionales de Cumplimiento Normativo y Certificaciones256 16.33Requerimientos no funcionales de Cumplimiento Normativo y Certificaciones257

- 16.34Requerimientos no funcionales de Hardware e Infraestructura  - 258

- 16.35Requerimientos no funcionales de Hardware e Infraestructura  - 259

- 16.36Requerimientos no funcionales de Usabilidad  - 260

<!-- Página 17 del PDF original -->

This page intentionally left blank.

<!-- Página 18 del PDF original -->

## 1 Resumen Ejecutivo

Netpower es una empresa especializada en el desarrollo de soluciones tecnológicas orientadas a garantizar la continuidad, seguridad y eficiencia de procesos clínicos y administrativos en organizaciones de salud. Nuestra propuesta para Consultas Médicas S.A. consiste en el diseño e implementación de un Sistema Integral de Gestión Médica y Administrativa (HospiNet), basado en estándares internacionales y arquitecturas modernas, que permitirá la digitalización completa de los procesos asistenciales y financieros de la institución, ademas de buscar optimizar los procesos y mejorar la satisfacción tanto del personal como de los pacientes.

El proyecto aborda la complejidad propia que poseen los sistemas informáticos en el área de salud mediante una arquitectura de microservicios y API Gateway, diseñada bajo un enfoque cloud-native y escalable, que asegura la interopérabilidad, resiliencia y continuidad operacional además el desarrollo se apoya en metodologías ágiles y prácticas DevOps, garantizando integración continua y despliegues seguros. Se adoptan estándares de salud como HL7/FHIR, DICOM y IHE para garantizar la integración con los sistemas clínicos existentes, asegurando la trazabilidad y consistencia de la información médica de los pacientes a lo largo de todo su proceso de atención en la institución.

La propuesta incorpora varias innovaciónes tecnológicas como el uso de Inteligencia Artificial para diagnóstico asistido, Predicción de No-Show con Machine Learning para predecir las inasistencias a las citas, uso de tecnologías IoT para monitoreo remoto de pacientes con enfermedades cronicas entre otras. De esta forma, la plataforma no solo moderniza la operación actual, sino que sienta las bases para una atención médica inteligente, preventiva y más eficiente que el modelo actual.

HospiNet se alinea con los objetivos de Consultas Médicas S.A. al mejorar la experiencia de atención de los pacientes, garantizar el cumplimiento normativo nacional (Ley 20.584, estándares HL7/FHIR) y fortalecer la sostenibilidad financiera mediante

<!-- Página 19 del PDF original -->

procesos automatizados y analítica predictiva. A continuación se incluye un roadmap tecnológico de implementación por etapas, asegurando resultados tempranos en eficiencia clínica, reducción de errores y satisfacción del paciente, con una arquitectura preparada para evolucionar junto al crecimiento de la institución.

#### Roadmap Estratégico de Implementación

El siguiente roadmap estratégico de implementación se estructura en tres fases progresivas, asegurando una evolución ordenada desde la digitalización operativa hasta la consolidación de un modelo de atención inteligente y preventiva.

| Fase | Actividades Principales | Entregables y Resultados Esperados |
| --- | --- | --- |
| Fase 1: Digitalización y Diseño del Sistema (Meses 1-12) | • Levantamiento de requerimientos funcionales y técnicos. • Diseño de la arquitectura de software y base de datos. • Desarrollo de módulos principales: Historia Clínica Electrónica, Agendamiento, Facturación y CRM. • Implementación de infraestructura tecnológica y ambientes de desarrollo, pruebas y producción. • Configuración inicial de servidores, seguridad y respaldos. | • Documento de diseño y arquitectura aprobado. • Prototipo funcional operativo. • Ambientes configurados (desarrollo, pruebas y producción). • Validación inicial de desempeño y estabilidad. |
| Fase 2: Interoperabilidad y Despliegue Controlado (Meses 13-20) | • Integración con sistemas externos (LIS, RIS, Isapres, Fonasa, entre otros). • Migración de datos y configuración de conectividad segura. • Ejecución de pruebas integrales, funcionales y de carga. • Capacitación de usuarios administrativos y clínicos. • Puesta en producción progresiva y monitoreo de rendimiento. | • Sistema operativo estable y funcional. • Usuarios capacitados y soporte inicial implementado. • Reportes de validación técnica y de desempeño. • Entorno productivo en operación controlada. |

<!-- Página 20 del PDF original -->

|  |  |  |
| --- | --- | --- |
| Fase 3: Consolidación Operativa y Mantenimiento (Meses 21-36) | • Optimización de procesos y ajustes post-implantación. • Soporte técnico y operativo continuo. • Actualizaciones menores y mejoras de desempeño. • Evaluación de resultados y documentación final del proyecto. • Cierre formal de actividades y transferencia al equipo de operación. | • Sistema consolidado y en régimen estable. • Informe de cierre y evaluación de resultados. • Plan de mantenimiento y continuidad operativa. |

<!-- Página 21 del PDF original -->

## 2 Descripción del Proponente

Netpower es una empresa dedicada al desarrollo de soluciones tecnológicas avanzadas e innovadoras, con un enfoque especializado en sistemas de salud, infraestructura TI y ciberseguridad. A lo largo de nuestra trayectoria hemos colaborado con organizaciones de sectores como salud, educación, telecomunicaciones y servicios financieros, aportando valor mediante desarrollo de software a medida, digitalización de procesos, integración de infraestructuras y estrategias de seguridad informática.

### 2.1 Misión de la empresa

Nuestra misión es desarrollar soluciones tecnológicas que impulsen la transformación digital de nuestros clientes, garantizando seguridad, continuidad operativa y eficiencia. Buscamos que cada plataforma implementada no solo resuelva un desafío técnico, sino que genere un impacto positivo en la experiencia de usuarios, pacientes y profesionales.

### 2.2 Visión de la empresa

Ser reconocidos como líderes en el desarrollo de software y soluciones tecnológicas para sectores estratégicos en Chile y Latinoamérica, consolidándonos como un socio confiable en proyectos de alto impacto. Aspiramos a transformar la tecnología en una herramienta invisible pero fundamental que garantice seguridad, confianza y excelencia operativa en procesos críticos.

### 2.3 Responsabilidad de la empresa

En Netpower entendemos la importancia de alinear tecnología, sostenibilidad y responsabilidad social:

<!-- Página 22 del PDF original -->

- Diseñamos plataformas digitales que reducen el uso de papel, contribuyendo a la preservación del medio ambiente.

- Implementamos arquitecturas en la nube que optimizan recursos físicos y energéticos, promoviendo una operación eficiente y eco-responsable.

- Priorizamos la innovación tecnológica inclusiva, orientando nuestras soluciones a mejorar la calidad de vida y proteger la privacidad y seguridad de los datos.

### 2.4 Credenciales organizacionales y madurez en gestión de tecnología

Netpower se distingue por su solidez organizacional y madurez en gestión de TI:

- Gestión de calidad y seguridad: procesos alineados con ISO 9001 (calidad) y controles de seguridad de la información conformes a ISO/IEC 27001/27002, con auditorías internas y mejora continua.

- Gobernanza y servicios TI: operación bajo marcos ITIL v4 (incidentes, problemas, cambios, servicio) e integración con prácticas DevOps (automatización de entrega y operación).

- Madurez en ingeniería de software: referencia CMMI-DEV (nivel 3) para procesos definidos y medibles en análisis, diseño, construcción, pruebas y despliegue.

- Solidez metodológica complementaria: aseguramos (i) trazabilidad E2E del SDLC, (ii) control de configuración con GitFlow, versionado semántico y SBOM, (iii) calidad continua mediante análisis estático, pruebas automatizadas y umbrales de cobertura, y (iv) gobierno de riesgos y cambios con CAB y estrategias de rollback definidas.

### 2.5 Capacidad instalada para proyectos TIC complejos

Nuestra capacidad instalada cubre todo el ciclo de vida de soluciones de misión crítica:

- Infraestructura cloud e IaC: entornos en nube de nivel empresarial (principalmente AWS) con infraestructura como código (IaC) para escalabilidad horizontal y replicación multi-zona.

- Plataforma DevOps: pipelines CI/CD automatizados (Jenkins/GitLab CI/GitHub Actions) que habilitan liberaciones frecuentes y confiables.

- Ambientes y observabilidad: cuatro ambientes (DEV/QA/STG/PROD); monitoreo y trazabilidad de extremo a extremo (métricas, logs, trazas) con alertas y turnos on-call 24/7.

- Seguridad operacional: enfoque Zero Trust, MFA, cifrado en tránsito y en reposo, gestión de secretos y endurecimiento de runtimes.

- Resiliencia: backups automáticos y pruebas de restauración periódicas; objetivos RTO/RPO definidos para cada dominio de datos; despliegues canary con rollback.

<!-- Página 23 del PDF original -->

- Laboratorio de interoperabilidad y ciberseguridad: entornos aislados para integración con sistemas heterogéneos y simulación de amenazas, validando guías técnicas y de cumplimiento.

### 2.6 Experiencia en integración de sistemas heterogéneos

La integración y la interoperabilidad son capacidades centrales de Netpower, especialmente en el sector salud:

- Interoperabilidad sanitaria (Health Interoperability): Poseemos experiencia comprobada en la implementación del estándar HL7/FHIR (Fast Healthcare Interoperability Resources) para la conexión y el intercambio de datos entre la Historia Clínica Electrónica (HCE) y sistemas externos (LIS/RIS, sistemas de facturación).

- Casos de éxito específicos: Hemos liderado la migración de datos y la integración de sistemas clínicos legados a plataformas modernas para más de tres grandes consultoras médicas, gestionando la conexión de más de 30 fuentes de datos distintas.

- Tecnologías de integración: Nuestro expertise se centra en el uso de API Gateway y arquitecturas de microservicios para desacoplar sistemas y asegurar una comunicación segura y trazable entre ellos.

### 2.7 Credenciales financieras del proponente

Netpower dispone de capacidad financiera para ejecutar proyectos TIC complejos:

- Solvencia y flujo de caja: financiamiento de fases de análisis, desarrollo, pruebas y despliegue sin afectar la continuidad operativa.

- Garantías: emisión de boletas de garantía (seriedad de la oferta y fiel cumplimiento) según requerimientos del mandante.

- Gestión presupuestaria: control físico-financiero por centros de costo, curvas de avance y reservas para contingencias.

- Cumplimiento: obligaciones laborales y tributarias al día; políticas de proveedores y subcontratación conforme a normativa vigente.

### 2.8 Equipo de trabajo y credenciales técnicas

Contamos con un equipo multidisciplinario con certificaciones y especializaciones que aseguran la ejecución del proyecto con prácticas de ingeniería robustas.

<!-- Página 24 del PDF original -->

| Rol | Profesional | Certificación / Core de especialización | Solidez metodológica |
| --- | --- | --- | --- |
| Gerente de Proyecto | Felipe Bravo Romo | PMP, ITIL Expert | Gestión Ágil (Scrum/Kanban) y Waterfall adaptativo; Gobernanza COBIT. |
| Jefe Arquitecto de Software Experto | Francisco Cortés | AWS Certified Solutions Architect - Professional; HL7/FHIR Certified | Arquitectura de Microservicios; Domain-Driven Design (DDD); modelado UML. |
| Jefe Analista de Negocios Experto | Luciano Oliva Jara | CBAP (Certified Business Analysis Professional) | BPMN; Design Thinking; especificación de requisitos funcionales/no funcionales (MoSCoW). |
| Jefe Especialista en Ciberseguridad | Antonia Navarrete Silva | CISSP; ISO/IEC 27001 Lead Implementer | Seguridad by design; Arquitectura Zero Trust; DLP; ethical hacking. |
| Jefe Experto en Testing y Analista QA | Esteban Carrasco | ISTQB® Certified Tester Foundation Level 4.0 (CTFL) | Pruebas automatizadas y manuales; Trazabilidad RF/RNF; Control de calidad continuo (CI/CD); aseguramiento bajo norma ISO/IEC 25010. |
| Jefe Diseñador UI/UX Experto | Fabrizzio Mura | Nielsen Norman Group Certification | Usabilidad en entornos clínicos; Diseño Centrado en el Usuario (UCD). |
| Jefe Desarrollador de Software Experto | Carlos Da Silva | CKAD (Certified Kubernetes Application Developer) | Prácticas DevOps; desarrollo full-stack con Python/Go. |
| Jefe en Redes y DBA Experto | Matías Bugueño | CCIE (Cisco Certified Internetwork Expert) | Alta disponibilidad de redes; QoS para tráfico clínico; enlaces redundantes. |

Table 2.1: Equipo del proponente y credenciales técnicas.

Esta estructura organizacional y técnica, sumada a la capacidad instalada y prácticas de calidad y seguridad descritas, sustenta la ejecución de un proyecto de transformación digital de alta complejidad con objetivos de disponibilidad, seguridad y continuidad operativa.

<!-- Página 25 del PDF original -->

## 3 Alcance del Servicio

En este apartado se define el alcance del proyecto, estableciendo de manera clara cuáles son los límites, las responsabilidades y los resultados esperados. Para ello, se consideran el problema identificado, el objetivo general y los objetivos específicos, junto con las necesidades estratégicas de Consultas Médicas S.A.

El alcance constituye la guía que orienta la ejecución del proyecto, delimitando qué aspectos serán abordados y cuáles quedarán fuera del esfuerzo, a fin de garantizar un trabajo enfocado y eficiente. De esta manera, se busca asegurar que todas las actividades estén alineadas con los requerimientos planteados y con el propósito de transformar la organización desde un modelo manual y fragmentado hacia un sistema digital integral.

### 3.1 Definición del problema

En la actualidad, la transformación digital en salud no es una opción, sino una condición indispensable para garantizar calidad asistencial, seguridad clínica y sostenibilidad financiera. Los entornos médicos en todo el mundo han evolucionado hacia modelos donde la Historia Clínica Electrónica (HCE), la interoperabilidad entre sistemas, la telemedicina y las plataformas de análisis de datos constituyen herramientas básicas para la toma de decisiones clínicas y la gestión administrativa eficiente. Estas tecnologías no solo optimizan los procesos internos, sino que además permiten anticiparse a complicaciones, reducir riesgos médicos y brindar experiencias de atención más seguras, rápidas y personalizadas a los pacientes.

En Chile, el Ministerio de Salud ha establecido normativas estrictas que obligan a las instituciones privadas a migrar hacia sistemas digitales integrales, considerando la protección de datos, la trazabilidad clínica y la continuidad operacional como pilares fundamentales. No adaptarse a esta realidad implica riesgos de sanciones regulatorias, pérdida de licencias y, sobre todo, un impacto directo en la confianza de pacientes y profesionales.

En este contexto, Consultas Médicas S.A. enfrenta un desafío crítico: a pesar de

<!-- Página 26 del PDF original -->

contar con una infraestructura física moderna, personal médico altamente capacitado y una amplia red de atención, su operación depende todavía de sistemas fragmentados, procesos manuales y fichas médicas en papel. Los problemas anteriores derivan en consecuencias severas, dentro de las cuales están:

- Riesgo en la seguridad del paciente: Actualmente hay médicos atendiendo sin información completa ni acceso remoto a historiales, exponiendo a diagnósticos erróneos o prescripciones riesgosas.

- Deficiencias operacionales: Se ven reflejadas en largas esperas, agendas poco confiables, ausencia de seguimiento para pacientes crónicos y falta de herramientas de apoyo diagnóstico.

- Problemas financieros graves: Se evidencian problemas como errores de facturación, imposibilidad de procesar bonos y seguros en línea, costos administrativos elevados y sanciones de aseguradoras.

- Crisis de confianza: En esta arista hay varios afectados, por un lado, los pacientes perciben un servicio desordenado y los médicos sienten que su tiempo se desperdicia en procesos excesivamente burocráticos, afectando la satisfacción del personal, reflejado en el aumento de la rotación de personal.

La empresa posee elementos que satisfacen completamente su necesidad en términos y personal, pero carece del software que le permita operar con estándares modernos de seguridad, eficiencia y calidad. La falta de un sistema integral de gestión médica y administrativa pone en riesgo no solo la operación diaria, sino también la proyección estratégica de la organización en un sector donde la tecnología es cada vez más determinante.

La implementación de una solución integral no solo permitirá resolver los problemas actuales, sino que traerá consigo beneficios sustanciales: reducción de costos administrativos, disminución de los tiempos de espera, mejora en la adherencia a tratamientos, aumento de la satisfacción de pacientes y médicos, y cumplimiento pleno con la normativa vigente. Más allá de los números, se trata de garantizar que cada decisión médica, se tome con información completa, confiable y disponible en el momento exacto en que se necesita, consolidando así un modelo de atención moderno y seguro.

#### 3.1.1 Actores

##### Actores de Netpower (empresa oferente)

- Director del Proyecto (Project Manager) Corresponde al director encargado de dirigir el proyecto, es un profesional certificado en gestión de proyectos (PMP/PRINCE2). El rol del director contempla liderar la planificación, ejecución y control del proyecto, asegurando cumplimiento de alcance, plazos, costos y calidad.

- Arquitecto de Soluciones Profesional especializado en el diseño de arquitecturas tecnológicas modernas

<!-- Página 27 del PDF original -->

(cloud, microservicios, interoperabilidad en salud). Su rol es definir la estructura técnica de la solución integral, garantizando que sea escalable, segura y cumpla con los estándares del sector salud (HL7/FHIR).

- Líder Técnico de Desarrollo Encargado de coordinar al equipo de programadores, testers e integradores. Su rol consiste en supervisar la construcción de los módulos críticos (HCE, agendamiento, facturación, telemedicina) y asegurar la correcta integración entre todos los sistemas.

- Equipo de Integración y Operaciones Conformado por especialistas en infraestructura, ciberseguridad, redes y DevOps. Su función es desplegar la plataforma tecnológica en la nube, asegurar la alta disponibilidad de los sistemas y mantener la continuidad operacional mediante soporte 24/7.

- Gestor del Cambio y Capacitación Profesional certificado en gestión del cambio organizacional. Su rol es acompañar a la organización durante la transición digital, capacitar al personal de Consultas Médicas y garantizar la adopción efectiva de las nuevas herramientas con la mínima resistencia.

##### Actores de Consultas Médicas S.A. (empresa consultante)

- Alta Dirección Integrada por la Gerencia General y la Dirección Médica. Su rol es entregar lineamientos estratégicos, validar las decisiones clave del proyecto y velar por que la implementación esté alineada con la misión institucional y los objetivos regulatorios.

- Área Médica Conformada por médicos, enfermeras y técnicos paramédicos. Su función es utilizar la Historia Clínica Electrónica y las herramientas clínicas asociadas, asegurando que estas soluciones se adapten a la práctica médica y mejoren la calidad de la atención.

- Área Administrativa y Financiera Incluye personal de admisión, facturación, cobranza y gestión financiera. Su rol es operar los nuevos módulos administrativos y financieros, garantizando procesos más ágiles, reducción de errores y un control financiero transparente y eficiente.

- Área de Tecnología de la Información (TI) Equipo interno responsable del soporte tecnológico actual. Su función es colaborar en la migración de datos, facilitar la integración con sistemas heredados y participar en el aseguramiento de la continuidad tecnológica a largo plazo.

- Pacientes y Usuarios Finales Corresponden a la comunidad de pacientes que utiliza los servicios de Consultas

<!-- Página 28 del PDF original -->

Médicas. Su rol es adoptar las nuevas herramientas digitales (portal web, aplicación móvil, telemedicina), siendo los principales beneficiarios de una atención más rápida, segura y personalizada.

#### 3.1.2 Objetivos

##### Objetivo general

Implementar un Sistema Integral de Gestión Médica y Administrativa en Consultas Médicas S.A., que permita la digitalización completa de los procesos clínicos y administrativos, garantizando seguridad del paciente, eficiencia operacional, sostenibilidad financiera y cumplimiento normativo, con el fin de transformar la experiencia de atención en salud hacia un modelo moderno, confiable y centrado en las personas.

##### Objetivos específicos

1. Digitalización clínica: Implementar una Historia Clínica Electrónica (HCE) unifi-

cada, accesible y segura que integre toda la información de los pacientes y asegure continuidad asistencial.

2. Optimización de la atención: Reducir los tiempos de espera y mejorar la expe-

riencia de los pacientes mediante un sistema de agendamiento multicanal con recordatorios automáticos y seguimiento post-consulta.

3. Soporte a la práctica médica: Incorporar herramientas de telemedicina, acceso

remoto a fichas y módulos de apoyo diagnóstico que faciliten el trabajo médico y reduzcan riesgos clínicos.

4. Eficiencia administrativa: Integrar procesos de admisión, facturación y cobranza

en una plataforma centralizada, disminuyendo errores y acelerando la gestión financiera.

5. Cumplimiento normativo: Asegurar el cumplimiento de la normativa vigente

en Chile sobre historia clínica electrónica, protección de datos y estándares de interoperabilidad en salud (HL7/FHIR).

6. Transformación cultural: Implementar un plan de gestión del cambio y capac-

itación que garantice la adopción efectiva del sistema por parte de médicos, personal administrativo y pacientes.

7. Escalabilidad y sostenibilidad: Diseñar una arquitectura tecnológica segura, es-

calable y flexible que soporte la proyección de crecimiento de la red de centros médicos y permita la incorporación de nuevas funcionalidades (IA, IoT, analytics).

#### 3.1.3 Definición de alcance

El presente proyecto abarca la implementación de un Sistema Integral de Gestión Médica y Administrativa que permitirá a Consultas Médicas S.A. modernizar y digitalizar de

<!-- Página 29 del PDF original -->

manera completa tanto sus procesos clínicos como administrativos. El alcance considera, en primer lugar, la dimensión clínica, la cual incluye la incorporación de una Historia Clínica Electrónica (HCE) centralizada y unificada, asegurando que la información de los pacientes esté disponible de forma instantánea, segura y estandarizada bajo normativas internacionales de interoperabilidad como HL7/FHIR. A esta capa clínica se suma la implementación de módulos de prescripción electrónica, alertas de alergias y contraindicaciones, además de la habilitación de servicios de telemedicina y seguimiento de pacientes crónicos, lo que permitirá fortalecer la continuidad asistencial y mejorar la seguridad de la atención.

En segundo lugar, el alcance comprende la modernización de la gestión administrativa y operativa. Este componente incluye el desarrollo de una plataforma de agendamiento multicanal que permitirá a los pacientes solicitar citas a través de distintos medios: portal web, aplicación móvil, call center, WhatsApp Business o de manera presencial; mejorando así la accesibilidad y reduciendo los tiempos de espera. Asimismo, se integrarán de manera nativa los procesos de admisión, facturación y cobranza, lo que permitirá optimizar la relación con Isapres, Fonasa y convenios empresariales, asegurando mayor eficiencia financiera y reduciendo al mínimo los errores en la gestión de pagos. Como complemento a esta línea, se pondrá en marcha un portal de autoservicio y una aplicación móvil orientada a pacientes, junto con un CRM con capacidades omnicanal que reforzará la comunicación y la fidelización de los usuarios.

Desde el punto de vista tecnológico, el alcance considera la migración de datos históricos desde sistemas obsoletos y soportes físicos hacia una infraestructura basada en la nube, con altos estándares de disponibilidad, escalabilidad y redundancia. Dicha infraestructura será integrada bajo un modelo de microservicios y API-first, lo que facilitará la interoperabilidad con otros prestadores y laboratorios. Además, se incorporarán medidas de ciberseguridad avanzadas, tales como cifrado de datos, autenticación multifactor y monitoreo continuo, asegurando así la confidencialidad y la integridad de la información crítica.

Finalmente, el alcance contempla la gestión del cambio organizacional y la sostenibilidad de la solución. Para ello se desarrollará un plan integral de capacitación orientado a médicos, administrativos y personal clave, de manera de garantizar una adopción eficiente y sin fricciones. Paralelamente, se implementará un programa de gestión del cambio que permitirá acompañar culturalmente a la organización en la transición hacia un modelo digital. Asimismo, se entregará soporte y mantenimiento por un período de un año, junto con un roadmap de evolución tecnológica que permitirá, en etapas futuras, la incorporación de analítica avanzada, inteligencia artificial, dispositivos IoT médicos y modelos predictivos de medicina preventiva.

#### 3.1.4 Exclusiones

Si bien el proyecto considera un alcance amplio y transformador, es importante precisar los aspectos que quedan fuera de esta licitación con el fin de evitar ambigüedades. En

<!-- Página 30 del PDF original -->

primer lugar, el proyecto no abarca la prestación directa de servicios médicos, ya que su foco es exclusivamente tecnológico y de gestión, sin intervenir en las decisiones clínicas de los profesionales ni en la relación médico-paciente más allá de las herramientas de apoyo.

Tampoco se contempla el desarrollo de hardware propio, puesto que se utilizará equipamiento estándar y certificado disponible en el mercado. De la misma manera, la expansión física de los centros médicos no forma parte del alcance; la construcción de nuevas dependencias o remodelaciones queda excluida, salvo las adecuaciones menores que pudiesen ser necesarias para la instalación de infraestructura tecnológica. Otro aspecto excluido corresponde a la administración de procesos externos a Consultas Médicas S.A., dado que si bien se habilitarán integraciones con Isapres, Fonasa y prestadores asociados, no se abordará la gestión administrativa de terceros fuera de la red. Además, el proyecto no considera soporte indefinido, ya que este se limita a un período de tres años posteriores a la implementación, quedando cualquier extensión de dicho plazo sujeta a una negociación futura.

Por último, quedan fuera de alcance las funcionalidades no contempladas explícitamente en las bases de licitación. En consecuencia, cualquier desarrollo adicional - como la incorporación de nuevos módulos no previstos o integraciones con prestadores que no se encuentren actualmente identificados- deberá ser evaluado como un proyecto independiente, con su respectivo presupuesto y planificación.

#### 3.1.5 Supuestos

- Se asume que Analytics y business intelligence en salud es lo mismo que reporteria y Analytics.

- Se asume que App movil para pacientes y app web tendrán el mismo fin y funcionalidad pero por canales distintos.

- Se asume que las atenciones agendadas de los usuarios enviarán un correo de confirmación de la hora, día y lugar de atención

<!-- Página 31 del PDF original -->

#### 3.1.6 Acuerdos de niveles de servicio mínimos (SLA’s prometidos):

Table 3.1: Niveles de Servicio (SLA) y Métricas de Desempeño

| Categoría | Métrica | Objetivo |
| --- | --- | --- |
| Disponibilidad | Uptime de servicios críticos ≥ 99.97% | Garantizar disponibilidad de los servicios fundamentales del sistema |
| Concurrencia | Resistir ≥ 5000 usuarios | Soportar mas de 5000 usuarios concurrentes interactuando con el sistema |
| Throughput | TPS ≥ 1000 | Soportar mas de 1000 transacciones por segundo sin disminuciones de rendimiento |
| Latencia | Tiempo de respuesta ≤ 15[Min] | Prometer un tiempo de respuesta desde reconocido el error de unos 15 minutos máximo |
| Problemas | Tiempo de resolución ≤ 4[Hrs] | Prometer una resolución de problemas del sistema de máximo 4 horas desde reportado el problema |
| RTO | Tiempo de Recuperación máx. 1[Hr] | Garantizar una recuperación de la operatividad del sistema en máximo 1 hora desde la caida del mismo |
| RPO | Ultimo punto de guardado de datos máx. 15[Min] | Garantizar un punto de guardado de datos de los últimos 15 minutos como máximo |
| Categoría | Métrica | Objetivo |
| Categoría | Métrica | Objetivo |

Table 3.2: Disponibilidad por servicio

| Servicio | Disponibilidad | [U] de tiempo |
| --- | --- | --- |
| WMS Core | 99.95% | 13 min/mes máximo downtime |
| TMS | 99.95% | 22 min/mes |
| Call Center | 99.95% | 22 min/mes |
| RRHH | 99.90% | 44 min/mes |
| Portal B2B | 99.50% | 3.6 horas/mes |
| Reportería | 99.00% | 7.3 horas/mes |

<!-- Página 32 del PDF original -->

Table 3.3: Perfomance

| Perfomance de servicio | Tiempo de respuesta | [U] de tiempo |
| --- | --- | --- |
| Transacciones online | 95% de transacciones &lt; 2 segundos | [S] |
| Consultas simples | Tiempo/consulta &lt; 1 segundo | [S] |
| Reportes complejos | Tiempo/reporte &lt; 30 segundos | [S] |
| APIs | Respuesta &lt; 500ms | [ms] |
| Batch processing | Ventana temporal predefinida | Variable |

Table 3.4: Recuperación

| Recuperación de servicio | Tiempo de respuesta | [U] |
| --- | --- | --- |
| RTO Crítico | 30 minutos | [min] |
| RTO Normal | 1 hora | [Hr] |
| RPO | Tiempo de recuperación ≤ 15 min. | [N/A] |
| Restore probado | Recuperación Mensual | N/A |

Table 3.5: Servicio: SLA’s Call Center

| Horario de disponibilidad | Lunes a Domingo | 07:00 - 24:00 |
| --- | --- | --- |
| Tiempo respuesta de atención | Tiempo &lt; 20 segundos | - |
| Abandono de atención | Abandono &lt; 5% | - |
| FCR (First Call Resolution) | Resoluciones en primera llamada &gt; 70% | - |
| Satisfacción | Satisfacción del cliente &gt; 85% | - |

### 3.2 Implementación

La implementación del Sistema Integral de Gestión Médica y Administrativa se llevará a cabo bajo un enfoque ágil (Scrum), complementado con buenas prácticas de PMI/PMBOK para la gestión global del proyecto y DevSecOps para garantizar una integración continua entre desarrollo y operaciones. Este marco metodológico permite una ejecución ordenada, flexible y con validación temprana de los entregables, reduciendo riesgos operativos y facilitando la adopción tecnológica por parte de médicos, pacientes y personal administrativo.

<!-- Página 33 del PDF original -->

#### 3.2.1 Metodología

Se trabajará en sprints de 3 a 4 semanas, con entregables funcionales en cada ciclo. Los roles principales estarán definidos en torno a Product Owner (representando al cliente) que será brindado por nuestra empresa, Scrum Master (garantizando la metodología) y un equipo multidisciplinario (desarrollo, integración, seguridad y soporte). Se utilizarán ceremonias ágiles (daily stand-up, sprint planning, sprint review y retrospectivas) para asegurar trazabilidad y mejora continua.

La integración con operaciones se asegurará mediante un enfoque DevOps, habilitando despliegues automatizados (CI/CD), pruebas automáticas y monitoreo continuo.

#### 3.2.2 Planificación

La implementación del Sistema Integral de Gestión Médica y Administrativa se llevará a cabo en dos etapas principales, con un horizonte de 20 meses en total. La planificación busca asegurar una transición ordenada, minimizando riesgos operativos, garantizando continuidad en la atención médica y maximizando la adopción tecnológica por parte de los usuarios.

##### 3.2.2.1 Primera Etapa: Implementación de sistemas críticos (Meses 1-12)

Esta fase corresponde a la digitalización de los procesos esenciales para la operación clínica y administrativa. Se estructura en 5 hitos principales:

1. Meses 1-2: Preparación y diseño detallado

- Instalación de infraestructura cloud segura.

- Migración y depuración inicial de datos clínicos y administrativos.

- Diseño de la arquitectura de integración (API-first, HL7/FHIR).

- Elaboración de manuales iniciales de seguridad y continuidad operacional.

2. Meses 3-5: Digitalización clínica inicial

- Implementación del Sistema de Historia Clínica Electrónica (HCE) unificada.

- Configuración de módulos de prescripción electrónica, alertas y contraindicaciones.

- Capacitación inicial al personal médico en el uso de la HCE.

3. Meses 6-7: Optimización administrativa y financiera

- Puesta en marcha del sistema de admisión y facturación integrado.

- Integración con sistemas de bonos electrónicos (Fonasa, Isapres).

- Capacitación al área administrativa y financiera.

4. Meses 8-9: Relación con pacientes y comunicación omnicanal

- Despliegue del CRM con call center omnicanal.

<!-- Página 34 del PDF original -->

- Implementación de plataforma de agendamiento multicanal (portal web, app móvil, WhatsApp Business, call center).

- Activación de notificaciones automáticas (recordatorios de citas, resultados disponibles, seguimiento post-consulta).

5. Meses 10-12: Consolidación y soporte organizacional

- Lanzamiento del portal web de autoservicio y app móvil para pacientes.

- Implementación del módulo digital de recursos humanos.

- Gestión del cambio organizacional (capacitaciones masivas, soporte en sitio, retroalimentación con usuarios).

- Ajustes y optimización de sistemas según retroalimentación inicial.

##### 3.2.2.2 Segunda Etapa: Funcionalidades avanzadas y optimización (Meses 13-20)

En esta fase se incorporan herramientas de innovación, analítica y soporte clínico avanzado. Se organiza en 4 hitos principales:

1. Meses 13-14: Expansión clínica

- Implementación de telemedicina integrada.

- Despliegue del portal para médicos con acceso remoto y herramientas colaborativas.

2. Meses 15-16: Continuidad asistencial avanzada

- Implementación del sistema de seguimiento de pacientes crónicos.

- Integración con laboratorios e imagenología para acceso centralizado de resultados.

- Configuración del workflow de atención GES.

3. Meses 17-18: Inteligencia de datos y analítica

- Implementación de analytics y business intelligence en salud.

- Desarrollo de tableros de indicadores clínicos, operativos y financieros.

4. Meses 19-20: Innovación tecnológica

- Integración de aplicaciones IoT para monitoreo remoto.

- Incorporación de inteligencia artificial para apoyo diagnóstico.

- Evaluación de la expansión de servicios digitales según roadmap estratégico.

#### 3.2.3 Normas y estándares a aplicar

Las normas y estándares internacionales constituyen un marco esencial para garantizar que HospiNet cumpla con los más altos estándares de seguridad, calidad, continuidad y eficiencia. Estas normativas entregan confianza a pacientes, profesionales de la salud y organismos reguladores, asegurando que la información clínica y administrativa se gestione bajo las mejores prácticas reconocidas globalmente, y que la operación hospitalaria se mantenga estable incluso ante situaciones críticas.

<!-- Página 35 del PDF original -->

##### 3.2.3.1 Normas de Seguridad de la Información

- NCh-ISO 27001: Esta norma establece los requisitos para implementar un Sistema de Gestión de Seguridad de la Información. En HospiNet, es indispensable porque asegura la confidencialidad, integridad y disponibilidad de la información clínica y administrativa. Su aplicación se traduce en controles de acceso, auditorías, cifrado de datos sensibles y políticas de seguridad que protegen la información de pacientes frente a accesos no autorizados o pérdidas.

- NCh-ISO 27002: Entrega un conjunto de buenas prácticas para la gestión de seguridad. Su aplicación en HospiNet permite definir políticas claras sobre control de accesos, uso de dispositivos, manejo de incidentes y clasificación de datos clínicos. De esta forma se garantiza que todos los procesos hospitalarios sigan lineamientos homogéneos y reconocidos internacionalmente.

- NCh-ISO 27005: Entrega directrices específicas para la gestión de riesgos de seguridad. En el contexto hospitalario, esto significa identificar y mitigar riesgos como fallos de infraestructura, ciberataques o fugas de datos médicos. Con HospiNet, esta norma permite que las decisiones de seguridad estén respaldadas por análisis rigurosos, lo que reduce vulnerabilidades y fortalece la confianza de pacientes y autoridades sanitarias.

- NCh-ISO 27032: Complementa la seguridad enfocándose en ciberprotección. Dada la interconexión de hospitales y la necesidad de telemedicina, esta norma asegura que HospiNet cuente con mecanismos de defensa frente a ataques cibernéticos (ransomware, phishing, DDoS), manteniendo siempre operativos los servicios críticos.

- NCh-ISO 27036 (1,2,3): Regula la seguridad en relaciones con proveedores. En HospiNet es fundamental, ya que muchos servicios se integrarán con terceros (laboratorios, aseguradoras, servicios de telemedicina). Esta norma garantiza que las obligaciones de seguridad se extiendan también a los socios tecnológicos y proveedores externos.

##### 3.2.3.2 Normas de Continuidad del Negocio

- ISO 22301: Norma clave en la gestión de continuidad del negocio. En hospitales, donde un minuto de inactividad puede significar vidas en riesgo, esta norma asegura que HospiNet incorpore planes de recuperación ante desastres (DRP), redundancia en los sistemas y mecanismos de alta disponibilidad. Así, frente a fallas de energía, catástrofes naturales o ataques informáticos, los servicios médicos pueden mantenerse o reanudarse rápidamente.

##### 3.2.3.3 Normas de Calidad del Software, Servicios Y revisión de código

- ISO 9001: Define un marco para la gestión de calidad en procesos y servicios. Aplicada a HospiNet, asegura que la atención médica digital cumpla estándares

<!-- Página 36 del PDF original -->

internacionales, evaluando permanentemente la satisfacción de pacientes y médicos, y promoviendo la mejora continua.

- ISO/IEC 20000: Se centra en la gestión de servicios TI. En clínicas/hospitales, su implementación garantiza que la operación de HospiNet (como la Historia Clínica Electrónica, telemedicina y facturación integrada) se gestione con procesos estandarizados, soporte 24/7 y mejoras continuas. Esto minimiza fallas y asegura la continuidad del servicio.

- ISO 25000 (SQuaRE): Evalúa la calidad del software hospitalario/clínico en dimensiones como usabilidad, eficiencia y confiabilidad. Es indispensable porque garantiza que los médicos y administrativos puedan usar HospiNet de manera intuitiva y sin errores, evitando demoras en la atención y fortaleciendo la seguridad clínica.

- Clean Code: Promueve el desarrollo de código fuente claro, legible y mantenible, priorizando la simplicidad, la eliminación de duplicidades y el uso de convenciones uniformes. Sobre todo para mantener la agilidad y facilidad de la mantención a largo plazo y el añadido de nuevas funcionalidades.

- SOLID: Conjunto de principios de diseño orientado a objetos que garantizan código modular, extensible y fácilmente testeable. Asegurará que cada módulo pueda evolucionar sin afectar el resto del sistema, sobre todo cumpliendo con los requerimientos de mantenibilidad, escalabilidad y sostenibilidad del producto (sobre todo teniendo en cuenta la cantidad de años en las que se plantea continuar dando mantención al producto).

- GitOps: Propone la necesidad de utilización de herramientas de control de versiones y buenas prácticas de código fuente en repositorios Git como GitHub. En HospiNet, permite desplegar entornos controlados y reproducibles mediante pipelines CI/CD automatizados, asegurando trazabilidad y control de cambios tanto en el software como en la infraestructura, pero principalmente versionamiento.

- Pair Programming: Técnica de desarrollo ágil en la que dos desarrolladores trabajan juntos en una misma estación: uno escribe el código y el otro lo revisa. En HospiNet, esta práctica mejora la calidad del código, fomenta la transferencia de conocimiento y detecta errores o vulnerabilidades en etapas tempranas del desarrollo.

- Code Review Processes: Todo cambio de código pasa por revisiones cruzadas entre pares mediante Pull Requests en Git, asegurando la adherencia a estándares de codificación, pruebas unitarias exitosas y cumplimiento de métricas obligatorias de código (code coverage >80%, complejidad ciclomática <10, duplicación <5%).

- DevSecOps y CI/CD: La integración continua (CI) y el despliegue continuo (CD) se combinan con controles de seguridad automatizados (DevSecOps), permitiendo detectar vulnerabilidades y problemas de calidad desde un pipeline de desarrollo.

<!-- Página 37 del PDF original -->

- Quality Gates: El código deberá cumplir con las métricas obligatorias establecidas en las Bases: cobertura de pruebas >80%, complejidad ciclomática <10, duplicación <5%, deuda técnica <5%, sin vulnerabilidades críticas y cumplimiento de benchmarks de rendimiento.

- Test Driven Development (TDD): Metodología de desarrollo guiado por pruebas donde primero se crean las pruebas unitarias y luego el código que las satisface. En HospiNet, esta práctica garantiza alta cobertura de tests, reduce defectos tempranos y mejora la mantenibilidad del software.

- Documentation as Code: La documentación técnica se versiona y mantiene junto al código fuente (idealmente comentado dentro del mismo códigoy en commits de Git), asegurando trazabilidad, consistencia y actualizaciones automáticas a través del pipeline CI/CD, además de ayudar en caso de tener que hacer rollbacks de código a un estado anterior.

- Security Testing en Pipeline: Los pipelines CI/CD integrarán análisis automáticos de seguridad, Software Composition Analysis, y Secret Scanning) para detectar vulnerabilidades y dependencias inseguras antes del despliegue a entornos productivos.

##### 3.2.3.4 Normas de Gestión de Proyectos y Desarrollo de Software

- PRINCE2 7: Propone un marco internacional para la gestión controlada de proyectos, enfocado en la gobernanza, la definición de roles y la toma de decisiones basada en beneficios. En HospiNet, PRINCE2 v7 se aplica para asegurar una estructura de dirección clara, con etapas definidas, gestión de riesgos, control de cambios y una comunicación efectiva con las partes interesadas.

- CMMI Nivel 3 o superior: Proporciona un modelo de madurez en los procesos de desarrollo de software. En HospiNet asegura que cada módulo (historia clínica, telemedicina, agendamiento, facturación) se desarrolle siguiendo procesos definidos, repetibles y medibles, reduciendo errores y mejorando la calidad final del sistema.

- ITIL v4: Ofrece buenas prácticas para la gestión de servicios TI, incluyendo incidentes, cambios y continuidad. Para HospiNet, ITIL garantiza que desde el primer día de operación se cuente con protocolos claros de soporte técnico y atención 24/7, lo cual es crítico en un hospital.

- PMP (PMBOK): Proporciona lineamientos de gestión de proyectos. En la implementación de HospiNet asegura que el proyecto se ejecute dentro de plazos y costos definidos, gestionando riesgos y asegurando la calidad de los entregables. Esto permite que la transición tecnológica de los hospitales sea ordenada y exitosa.

- Scrum/SAFe: Permitirá entregar funcionalidades de forma incremental. En el caso de HospiNet, esto es clave para validar con médicos y administrativos funcionalidades críticas como agendamiento o historia clínica antes del despliegue

<!-- Página 38 del PDF original -->

completo.

##### 3.2.3.5 Normas de Infraestructura propia (físicamente en Chile)

- NCh 2777: Regula el control de acceso físico a instalaciones críticas como datacenters y salas de servidores. Para HospiNet, su aplicación garantiza que solo personal autorizado pueda acceder a la infraestructura hospitalaria crítica, reduciendo riesgos de sabotaje o interrupciones. Esto es vital para proteger los sistemas que soportan la atención médica.

- Tier III: Estándar internacional que garantiza que los datacenters utilizados por HospiNet cuenten con redundancia en energía, climatización y conectividad. Esto permite cumplir con los SLA de disponibilidad (99.97%) exigidos en entornos hospitalarios y corresponde al Tier máximo posible en Chile.

- Cloud Security Alliance (CSA): Asegura que los servicios en la nube aplicados a HospiNet cumplan con las mejores prácticas de seguridad, protección de datos y cumplimiento normativo, garantizando que la información clínica alojada en entornos cloud se mantenga segura y confiable.

##### 3.2.3.6 Métricas y Cobertura de Calidad del Software

El proceso de aseguramiento de la calidad del software en HospiNet incorpora mediciones automáticas y continuas orientadas a garantizar la mantenibilidad, confiabilidad y seguridad del código. Estas métricas se integran en el pipeline de Integración y Despliegue Continuo (CI/CD), ejecutándose de forma automática en cada build.

- Cobertura de pruebas (Code Coverage): Cada módulo deberá alcanzar una cobertura mínima del 80% en pruebas unitarias, verificadas mediante herramientas como SonarQube, Jest, PyTest o JUnit. Esto asegura que la mayor parte del código haya sido validada de forma automatizada, reduciendo el riesgo de errores en producción.

- Complejidad Ciclomática: Se controlará que cada método o función mantenga una complejidad inferior a 10, garantizando un diseño modular, mantenible y de bajo acoplamiento. Los reportes de complejidad serán generados automáticamente y revisados durante el proceso de Code Review.

- Duplicación de Código y Deuda Técnica: El sistema deberá mantener una duplicación inferior al 5% y una deuda técnica menor al 5% del esfuerzo total estimado. Esto asegura que el desarrollo sea eficiente, reutilizable y sostenible en el tiempo, además de no tener mas de un 1% de igualdad de código opensource de internet utilizado.

- Vulnerabilidades y Seguridad: Los análisis de seguridad no deben arrojar vulnerabilidades críticas, y las medias deberán ser menores a cinco por módulo. Estos controles se ejecutarán de forma automática siguiendo DevSecOps.

- Performance y Benchmarks: Los módulos deberán cumplir los umbrales de rendimiento definidos en las pruebas de carga y estrés (por ejemplo, tiempo de respuesta < 2s

<!-- Página 39 del PDF original -->

p95, throughput y consumo óptimo de recursos). Estas métricas serán verificadas con herramientas como JMeter o Locust.

Estas mediciones conforman los Quality Gates obligatorios del proyecto y servirán como base para las auditorías de calidad, reportes de avance y acciones de mejora continua.

#### 3.2.4 Gestión de Dependencias Críticas y Riesgos Técnicos

La gestión de dependencias críticas y riesgos técnicos asociados tanto al proyecto como al producto representan todas las consideraciones de problemas que puedan derivar en una obstaculización del desarrollo óptimo y correcto del peoyecto o la disponibilidad de los servicios.

- Dependencias críticas:

  - Proveedores Cloud: Dependencia directa de servicios de AWS (Aurora PostgreSQL, Amazon DocumentDB, AWS Backup). Además que de ellos depende el rendimiento y cumplimiento de los SLA’s.

  - Integraciones HL7/FHIR: La interoperabilidad clínica depende de la correcta operación de interfaces o estándares HL7/FHIR, dependiendo directamente de estar al día con estas normas y estándares universales.

  - Dependencias de librerías y frameworks: Dependencia de las librerías y frameworks utilizados y sujeto a actualizaciones o cambios en los mismos.

- Riesgos técnicos identificados: En este punto se identificaron algunos riesgos preliminares y críticos que afectarían al correcto funcionamiento y operación del sistema a nivel macro en términos de experiencia de los usuarios, técnico y a nivel operacional.

  - Pérdida de disponibilidad en nube: Riesgo de falla en región o zona de AWS. Mitigación: replicación de datacenter y backups automáticos diarios (AWS Backup y On-Premise).

  - Interoperabilidad con sistemas heredados: Riesgo de incompatibilidad con formatos legados o datos incompletos. Mitigación: validación previa con scripts ETL y pruebas de integración en ambientes separados y controlados.

  - Fallas de seguridad o vulnerabilidades críticas: Mitigación: escaneo continuo, revisión de código obligatoria, actualizaciones/parches regulares y revisión de logs periódica.

  - Sobrecarga de rendimiento o latencia elevada: Mitigación: pruebas de estrés periódicas, autoescalado en la capa de aplicación y optimización de índices en bases de datos.

Se mencionarán mas riesgos asociados al proyecto en el punto 9 - RBS, por lo que solo se han incluido en este punto algunos de los que se han considerado como mas relevantes para el proyecto/producto.

<!-- Página 40 del PDF original -->

#### 3.2.5 Arquitectura de la Solución

La arquitectura del Sistema Integral de Gestión Médica y Administrativa se diseñará bajo un enfoque modular y escalable, soportado en servicios en la nube de Amazon Web Services (AWS), lo que garantiza disponibilidad, seguridad y flexibilidad.

- Capa de Presentación: Interfaces web responsivas y aplicaciones móviles desarrolladas con frameworks modernos (Angular, Flutter), optimizadas para médicos, pacientes y personal administrativo.

- Capa de Negocio: Implementación de microservicios desacoplados, que gestionan procesos como agendamiento, historia clínica electrónica, facturación, convenios y telemedicina.

- Capa de Datos: Uso de bases de datos relacionales (Amazon RDS - PostgreSQL) para información estructurada, y bases NoSQL (Amazon DocumentDB) para datos dinámicos como registros de consultas o logs de interacción.

- Integración y Comunicaciones: API Gateway para exponer servicios, mensajería asincrónica mediante Amazon SQS/SNS, y estándares de interoperabilidad en salud (HL7, FHIR).

- Seguridad: Autenticación y autorización centralizadas (Amazon Cognito), cifrado en tránsito y reposo (KMS), cumplimiento normativo (ISO 27001, HIPAA-ready en AWS).

- Alta Disponibilidad y Resiliencia: Balanceadores de carga (ELB), autoescalado de instancias, backups automáticos y monitoreo proactivo con Amazon Cloud- Watch.

#### 3.2.6 Plan de Recursos

Para asegurar una implementación efectiva, se dispondrá de un plan de recursos que contempla talento humano, infraestructura tecnológica y presupuesto:

##### 3.2.5.1 Recursos Humanos:

- Dirección de Proyecto: Coordinación estratégica y seguimiento de hitos.

- Equipo de Desarrollo: Ingenieros de software especializados en backend, frontend, DevOps y seguridad.

- Especialistas Funcionales: Profesionales de salud y administrativos que aportan conocimiento de procesos clínicos y financieros.

- Soporte y Capacitación: Equipo de formación para usuarios finales y mesa de ayuda post-implementación.

##### 3.2.5.2 Recursos Tecnológicos:

- Infraestructura cloud en AWS (cómputo, almacenamiento, bases de datos, seguridad).

<!-- Página 41 del PDF original -->

- Herramientas de integración continua y despliegue (CI/CD con AWS CodePipeline, Jenkins o GitHub Actions).

- Plataformas de colaboración (Jira, Confluence, Slack/Teams) para seguimiento ágil.

##### 3.2.5.3 Recursos Financieros:

- Presupuesto estimado para infraestructura, licencias y mantenimiento.

- Costos de capacitación y soporte.

- Reserva para contingencias (10% del presupuesto total del proyecto).

### 3.3 Implantación

La implantación del Sistema Integral de Gestión Médica y Administrativa en Consultas Médicas S.A. comprende la transición efectiva desde los sistemas actuales hacia la nueva plataforma digital, asegurando continuidad operativa, seguridad de la información y adopción eficiente por parte de todos los usuarios. Esta fase constituye el puente entre la implementación técnica y la operación estable del sistema.

#### 3.3.1 Migración de datos

Transferencia de datos históricos desde sistemas existentes y soportes físicos a la infraestructura en la nube y sitios edge, asegurando integridad y confidencialidad configurando los parámetros críticos del sistema, usuarios, perfiles y permisos según roles clínicos y administrativos. Se contemplará la extracción desde los sistemas de legado (físicos), la transformación hacia un modelo que cumpla con estándares HL7/FHIR, y su carga en las bases de datos propuestas para la solución. Motores de BD: Aurora Postgre-SQL y Amazon Document-DB.

<!-- Página 42 del PDF original -->

Table 3.6: Migración de datos a BD

| Motores de BD | Datos a migrar |
| --- | --- |
|  | Telemedicina BD, Operaciones BD, ODS (Operation Data Store) BD, Transporte BD. |
|  | Finanzas BD, Control de Acceso BD, RRHH BD, HCE BD, Bodega BD |
|  | Backup DocumentDB, Backup Aurora |
|  | CRM BD |

Además dispondremos del servicio de AWS Backup para manejar el sistema de recuperación de estados y Backups de un mínimo correspondiente a los últimos 15 minutos.

Cada flujo incluirá trazabilidad completa mediante identificadores únicos de lote y registro, permitiendo el seguimiento de cada dato desde su origen hasta su destino.

Las migraciones solo podrán ser realizadas por el DBA Senior encargado en el proyecto y por las personas que el considere aptos en su equipo y se aplicarán políticas de cifrado en tránsito (TLS 1.3) y en reposo (AES-256), junto con control de acceso basado en roles y bitácoras de auditoría inmutables para toda actividad de carga y modificación. La gobernanza se alineará con la Ley 19.628 sobre protección de datos personales, los estándares ISO/IEC 27001 e ISO 27799 (seguridad de información en salud) y las normativas HL7/FHIR del Ministerio de Saud.

Las herramientas y tecnologías que utilizaremos son: ETL (Extract, Transform, Load) con Pentaho o Talend, validación automática con scripts Python con SQL y herramientas de auditoría de datos y logging para seguimiento de migraciones, además de AWN Backup para manejo de recuperación de estados en caso de que sea necesario.

#### 3.3.2 Despliegue en ambientes productos

Instalación progresiva en site principal, site secundario (DR) y sites edge por ubicación, cumpliendo SLA y altos estándares de disponibilidad con configuración de balanceadores de carga, contenedores (Docker/Kubernetes) y microservicios.

Implementación de seguridad zero-trust, cifrado de datos en tránsito y reposo, autenticación multifactor.

![Página 42 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-042.png)

<!-- Página 43 del PDF original -->

Las herramientas y tecnologías a utilizar son: Plataforma cloud AWS, orquestación de microservicios con Kubernetes, monitoreo con Prometheus, Grafana y ELK Stack.

#### 3.3.3 Pruebas de validación y ajuste

La fase de pruebas de validación y ajuste constituye un componente crítico en la implantación del Sistema Integral de Gestión Médica y Administrativa, ya que garantiza que todas las funcionalidades clínicas y administrativas operen correctamente, que el sistema cumpla con los estándares de rendimiento establecidos y que la experiencia del usuario final sea óptima.

Durante esta etapa, se realizarán pruebas integrales de todas las funcionalidades, evaluando los flujos clínicos y administrativos. Estas pruebas asegurarán que los módulos del sistema funcionen de manera correcta, coherente e integrada, cumpliendo con los procesos TO-BE previamente definidos.

Además, se ejecutarán pruebas de carga y estrés, con el objetivo de verificar el desempeño del sistema bajo condiciones de alta concurrencia, garantizando tiempos de respuesta adecuados, estabilidad de la infraestructura y cumplimiento de los SLA establecidos para cada servicio crítico. Este enfoque permite detectar cuellos de botella, vulnerabilidades en la infraestructura y oportunidades de optimización antes del despliegue en producción.

Se prestará especial atención a la validación de la experiencia del usuario (UX), evaluando interfaces gráficas, flujos de navegación y consistencia de la información. Los resultados se contrastarán con los procesos TO-BE diseñados, asegurando que los usuarios finales puedan realizar sus tareas de manera intuitiva, eficiente y sin errores.

Con base en los hallazgos obtenidos, se aplicarán ajustes y optimizaciones, que incluirán correcciones de errores, mejoras en la performance, refinamiento de interfaces y ajustes de configuración para optimizar la operación del sistema. Esta etapa garantiza que la plataforma esté completamente lista para su operación en producción y que cumpla con los objetivos de eficiencia, seguridad y satisfacción de los usuarios.

Para respaldar la calidad y formalidad de las pruebas, se emplearán metodologías y herramientas reconocidas a nivel internacional:

- ISTQB (International Software Testing Qualifications Board) para la planificación y ejecución estructurada de pruebas.

- UAT (User Acceptance Testing) con participación de usuarios clave, permitiendo validar la adecuación del sistema a las necesidades reales del negocio.

- Automatización de pruebas de regresión utilizando Selenium o Cypress, asegurando que cambios posteriores no afecten funcionalidades previamente validadas.

- Registro y seguimiento de incidencias mediante herramientas como JIRA o Azure DevOps, permitiendo la trazabilidad completa de errores, su priorización y cierre formal.

<!-- Página 44 del PDF original -->

- Esta estrategia integral de pruebas asegura que el sistema sea robusto, confiable y que esté alineado con las expectativas clínicas y administrativas, facilitando un despliegue seguro, controlado y exitoso en todas las ubicaciones de Consultas Médicas S.A.

#### 3.3.4 Marcha blanca/Piloto

El proceso estará a cargo del equipo de soporte, quienes tendrán la responsabilidad de monitorear y evaluar el progreso de las pruebas. Los usuarios del sistema, tanto médicos como administrativos, contarán con un acompañamiento directo del equipo técnico en un horario técnico extendido de lunes a domingo, de 7:00 hrs a 00:00 hrs, con el fin de garantizar continuidad en la operación y atención inmediata a incidentes.

En esta fase, la aplicación será utilizada con pacientes reales en un centro médico piloto, seleccionado estratégicamente para concentrar el mayor número de procesos críticos de la institución. De este modo, será posible someter la plataforma a condiciones de alta demanda, obtener retroalimentación directa de los usuarios y validar su capacidad para adaptarse a las necesidades operativas de la organización.

Selección del centro piloto: El centro médico elegido para este proceso será el que represente mayor complejidad operativa, ya que concentra altos volúmenes de atención, diversidad de servicios y una infraestructura que permita evaluar la robustez del sistema. Los criterios de selección contemplan:

- Volumen de atenciones: se priorizará un centro con alta carga asistencial para evaluar el rendimiento del sistema bajo condiciones exigentes.

- Ubicación estratégica: se considerará un centro con características representativas de la red, de modo que los resultados sean extrapolables a futuras implementación.

- Infraestructura tecnológica: el centro debe contar con la infraestructura necesaria para desplegar todos los componentes de hardware, software, redes y seguridad

Configuración del entorno: El entorno de pruebas deberá replicar en la mayor medida posible las condiciones de producción. Esto incluye la configuración de hardware (servidores, redes, dispositivos biométricos); software (sistemas operativos, aplicaciones y medidas de seguridad como cifrado y firewalls), y bases de datos: parámetros de almacenamiento, rendimiento y conexión. Asimismo, se ejecutarán pruebas de carga, estrés y capacidad, con el fin de garantizar que la plataforma pueda soportar el nivel de operación esperado.

Monitorización y seguimiento: Durante la aplicación de la prueba se implementará un esquema de monitoreo integral. Se supervisará en tiempo real el estado de la infraestructura tecnológica, el rendimiento de las aplicaciones y la disponibilidad de los servicios. Adicionalmente, se registrarán todas las incidencias y acciones realizadas dentro del sistema, lo que permitirá trazar los problemas detectados y facilitar su resolución.

<!-- Página 45 del PDF original -->

Evaluación de resultados: Al término de la marcha blanca se elaborará un registro detallado de los incidentes ocurridos, incluyendo fallos técnicos, comportamientos inesperados y retroalimentación de los usuarios. Esta información será analizada en conjunto con la dirección del proyecto para identificar problemas críticos y definir las acciones correctivas necesarias. Una vez resueltos los inconvenientes, se generará un informe de cierre que documentará los hallazgos, soluciones implementadas, aprendizajes obtenidos y recomendaciones para la expansión de la solución en el resto de los centros médicos.

#### 3.3.5 Puesta en producción

Posterior a la fase de marcha blanca y una vez se validen los resultados obtenidos, el sistema avanzará a su puesta en producción de manera planificada y controlada, con el objetivo de asegurar un inicio de operación estable desde el primer día. Este proceso contempla la revisión final del entorno, la aceptación formal de los usuarios y la implementación de un plan de soporte y mejora continua que garantice la sostenibilidad del sistema en el tiempo.

Revisión final del entorno de producción: Previo al despliegue definitivo, se realizará una verificación exhaustiva de todos los componentes del sistema, incluyendo servidores, bases de datos, redes, dispositivos de seguridad, y aplicaciones clínicas y administrativas. Se ejecutarán pruebas de carga y rendimiento que permitan asegurar la estabilidad de la plataforma ante volúmenes elevados de consultas y transacciones financieras, validando además los mecanismos de seguridad y respaldo.

Pruebas de aceptación de usuarios: En esta etapa se llevará a cabo un proceso de aceptación con la participación de médicos, personal administrativo y representantes de la dirección de Consulta Médicas S.A. El propósito es confirmar que la plataforma cumple con los requerimientos funcionales establecidos, tales como el registro y consulta de historiales clínicos, el agendamiento multicanal, la facturación electrónica y los módulos de comunicación con pacientes. Cualquier incidencia identificada será corregida de inmediato, de manera que el sistema quede plenamente validado antes del uso masivo.

Despliegue y soporte inicial: La puesta en producción se realizará en forma gradual, inicial en el centro piloto y extendiéndose progresivamente al resto de los centros médicos de la red. Durante los primeros tres meses posteriores al despliegue total, se mantendrá un esquema de soporte intensivo presencial y remoto, con el fin de atender cualquier requerimiento operativo y asegurar que la plataforma funcione de acuerdo con las expectativas de negocio y de atención de salud.

Mantenimiento y mejora continua: Con el sistema ya en operación, se implementará un plan de mantenimiento que incluirá acciones correctivas, preventivas y evolutivas. Este plan permitirá resolver incidentes técnicos, anticipar riesgos de disponibilidad e incorporar mejoras derivadas de la retroalimentación de los usuarios. Se realizarán actualizaciones periódicas, auditorias de seguridad y monitoreo proactivo de

<!-- Página 46 del PDF original -->

infraestructura y aplicaciones.

### 3.4 Operación

La operación se basará en un modelo centralizado y estandarizado, sustentado en infraestructura cloud híbrida, con soporte 24x7 y SLA de 99,97% para los sistemas críticos. Esto permitirá mantener la disponibilidad de los servicios médicos digitales en todos los centros de atención, incluyendo HCE, agendamiento multicanal, telemedicina y facturación.

Se proyecta una operación continua por 3 años, con el siguiente enfoque:

- Año 1: Estabilización post-implementación.

- Años 2 y 3: Operación regular, soporte y mejora continua.

#### 3.4.1 Soporte

Se dispondrá de una mesa de ayuda multicanal (teléfono, correo electrónico y portal de tickets) con cobertura 24/7, que dará respuesta a incidentes, requerimientos y consultas. El modelo de soporte se estructura en tres niveles:

- Nivel 1: Atención de incidencias básicas y solicitudes de usuarios finales.

- Nivel 2: Soporte técnico especializado en la plataforma y las integraciones.

- Nivel 3: Escalamiento al proveedor para resolución de problemas críticos y actualizaciones estructurales.

Cada incidente será gestionado con una herramienta de seguimiento llamada JIRA, lo que permitirá trazabilidad, priorización y control de los tiempos de respuesta.

#### 3.4.2 Monitoreo

Se implementarán dashboards en tiempo real con indicadores clave:

- KPIs Operacionales: tiempo de espera (objetivo 15 min), tasa de no-show (objetivo 10%), ocupación consultas (85%).

- KPIs Clínicos: acceso instantáneo a historial, adherencia tratamientos (80%).

- KPIs Financieros: reducción de errores en facturación a <1%, disminución de días de cobranza a 30.

- Satisfacción: NPS de pacientes (75) y médicos (85%).

El sistema será monitoreado de forma continua mediante un NOC (Network Operations Center) y un SOC (Security Operations Center), con alertas automáticas en caso de degradación o caídas de servicio. Se establece disponibilidad (SLA) del 99,97%.

El sistema de analytics y business intelligence permitirá generar reportes predictivos y correctivos en línea.

<!-- Página 47 del PDF original -->

#### 3.4.3 Mantenimiento y Actualizaciones

La operación contempla un plan integral de mantenimiento:

- Preventivo: aplicación de parches de seguridad, monitoreo proactivo y limpieza de registros.

- Correctivo: resolución de incidencias reportadas por los usuarios o detectadas en el monitoreo.

- Evolutivo: incorporación de nuevas funcionalidades en base a la retroalimentación y a las necesidades del negocio.

Las actualizaciones se realizarán bajo un modelo de gestión de versiones controladas, con entornos diferenciados (desarrollo, pruebas y producción) que aseguren la estabilidad y confiabilidad de la plataforma.

#### 3.4.4 Presupuesto de errores SRE

Se presenta una tabla de presupuesto de errores de Site Reliability Engineering (SRE) considerando nombre de servicio de los SLA’s prometidos para los servicios mas importantes del sistema, SLA(%) y acciones a tomar dependiendo de su grado de criticidad.

Table 3.7: Presupuesto de Errores - Site Reliability Engineering (SRE)

| Servicio | SLA (%) | SLO (%) | Error Budget (h/mes) | Acciones según criticidad y consumo |
| --- | --- | --- | --- | --- |
| HCE | 99.95% | 99.99% | 0.07 | Servicio de máxima criticidad; en caso de no cumplirse el SLA acordado se deberá analizar las razones y dar prioridad a la solución del problema relacionado. |
| Autenticación con Biometría | FAR ≤ 0.001 | - | - | Al producirse errores se deberá informar directamente a soporte TI mediante ticket; en caso de ingreso no permitido se generará una alerta en el sistema. |
| Sistemas de Respaldo y Recuperación | RTO ≤ 30 min / RPO ≤ 15 min | - | - | Validación diaria de respaldos; al alcanzar 100% del presupuesto de error se ejecuta restauración de prueba y auditoría de continuidad operativa. |

Continúa en la siguiente página

<!-- Página 48 del PDF original -->

Table 3.7 - continuación de la página anterior

| Servicio | SLA | SLO | Error Budget (h/mes) | Acciones según criticidad y consumo |
| --- | --- | --- | --- | --- |
| Telemedicina / Atención Remota | 99.95% | 99.96% | 0.29 | Si se supera el límite de nodisponibilidad, se bloqueará el acceso a telemedicina y se esperará a la resolución del servicio, además de enviar un ticket a soporte TI para resolver el problema. |
| Finanzas / Cadena de Suministros | 99.50% | 99.70% | 2.16 | Si se supera el límite de inactividad permitido, se deberá avisar a los clientes la limitación con el sistema de pagos digitales y recurrir al ingreso local de pagos y en efectivo de manera temporal, hasta que el sistema se reestablezca. Una vez operativo, se ejecutará la reconciliación automática de los datos contables y órdenes de compra, verificando integridad entre los módulos conectados. |
| Reportería / BI / Analítica | 99.00% | 99.20% | 5.76 | Si se supera el umbral de disponibilidad, se deberá enviar un ticket a soporte TI para resolver el problema (baja prioridad), además de realizar un análisis y escaneo del sistema para revisar posibles causas. |
| WMS Core | 99.97% | 99.98% | 0.14 | Diariamente se dispondrá de un archivo .json con la información fundamental del WMS; si se supera el límite de inactividad mensual, se deberá realizar un análisis del sistema y la red para determinar el origen del incidente y registrar los datos para posibles dashboards o análisis detallado. |
| TMS | 99.95% | 99.96% | 0.29 | Cada vez que se realicen distribuciones y entregas administradas por TMS, se dispondrá de un archivo de logs del día que resuma rutas y horarios. Si se supera el límite de inactividad permitido, se deberá usar ese archivo de resumen para evitar pérdida de información relevante y restaurar operaciones. |

Continúa en la siguiente página

<!-- Página 49 del PDF original -->

Table 3.7 - continuación de la página anterior

| Servicio | SLA | SLO | Error Budget (h/mes) | Acciones según criticidad y consumo |
| --- | --- | --- | --- | --- |
| Call Center | 99.95% | 99.96% | 0.29 | Si se supera el umbral, se deberá bloquear el acceso al servicio de call center y enviar un ticket a soporte TI para analizar el problema y sus posibles soluciones. |
| RRHH | 99.90% | 99.92% | 0.58 | Si se supera este umbral, se deberá realizar un análisis de rendimiento del módulo para la detección de posibles causas del problema. |
| B2B (Portal B2B) | 99.50% | 99.70% | 2.16 | Si el servicio no cumple el mínimo, se debe ejecutar análisis de impacto comercial y comunicación preventiva a los socios conectados, además de una revisión de estado del servicio. |
| Transacciones Online | &lt;2 s (p95) | - | - | Si no se logra mantener el 95% de las transacciones por debajo de 2 s, se deberá ejecutar un análisis de rendimiento end-to-end (red, CPU, BD, servicios) y optimizar balanceo y caching antes de nuevos despliegues. |
| Consultas Simples | &lt;1 s | - | - | Si no se mantiene tiempo de respuesta &lt;1 s, ejecutar diagnóstico de rendimiento (índices, plan de ejecución, latencia) y ajustar recursos de BD y caché. |
| APIs | &lt;500 ms | - | - | Si no se alcanza el tiempo de respuesta, intentar reconexión rápida y analizar colas de mensajería y latencia en gateway. |
| Batch Processing | 100% según ventana acordada | - | - | En caso de error, realizar rollback del último estado válido del sistema y reintentar el procesamiento dentro de la ventana. |
| RTO Crítico | 30 min | 99% (≤25 min) | 0.12 | Si no se cumple el RTO, activar plan de contingencia inmediata para mantener servicios mínimos y restaurar antes de 60 min. |
| RTO Normal | 1 h | 99% (≤45 min) | 0.24 | Si no se cumple, generar ticket a soporte TI y priorizar recuperación en menor tiempo posible. |

Continúa en la siguiente página

<!-- Página 50 del PDF original -->

Table 3.7 - continuación de la página anterior

| Servicio | SLA | SLO | Error Budget (h/mes) | Acciones según criticidad y consumo |
| --- | --- | --- | --- | --- |
| RPO | 15 min | 99.9% (≤15 min) | 0.07 | Siempre mantener archivo en memoria volátil con resumen de información de los últimos 15 min; si no se recuperan los datos, usar ese registro para reconstrucción parcial y seguimiento de datos. |
| Backup Exitoso | 100% diario | 100% | 0.00 | Cada ciclo de respaldo debe completarse sin errores en 24 h; si falla, ejecutar backup manual en 1 h y verificar la restauración del último backup válido. |

#### 3.4.5 Seguridad

La operación estará guiada por estándares internacionales de gestión de seguridad de la información (ISO 27001, ISO 20000 e ISO 22301), además de lo establecido en la normativa nacional para la protección de datos clínicos. Se aplicarán medidas de seguridad como:

- Autenticación multifactor y gestión de accesos basada en roles.

- Cifrado de datos en tránsito (TLS 1.3) y en reposo (AES-256).

- Auditoría y bitácoras de acceso para garantizar la trazabilidad.

- Firewalls de aplicación, sistemas anti-DDoS y monitoreo SIEM para prevenir ciberataques.

Con ello, se asegura la confidencialidad, integridad y disponibilidad de la información crítica de pacientes y procesos administrativos.

#### 3.4.6 Capacitación a Usuarios

Se implementará un plan de capacitación estructurado para los distintos perfiles de usuarios: médicos, personal administrativo y personal de soporte interno. Este plan contempla:

- Capacitación inicial presencial y en línea, orientada al uso de los módulos principales.

- Guías rápidas y manuales de usuario de fácil consulta.

- Sesiones de retroalimentación periódicas para resolver dudas y reforzar el uso adecuado del sistema.

- Capacitación continua en nuevas funcionalidades que se vayan incorporando en el tiempo.

<!-- Página 51 del PDF original -->

De esta manera, se asegura una correcta adopción de la solución, fomentando la confianza de los usuarios y reduciendo la curva de aprendizaje.

Plan de Contingencia para Escenarios Críticos El sistema contará con un conjunto de procedimientos de contingencia orientados a minimizar el impacto operativo ante fallas críticas, garantizando la continuidad del servicio y la protección de los datos. Estos procedimientos serán revisados y probados periódicamente en conjunto con el plan de continuidad operacional.

- Falla de sistemas cloud, base de datos o corrupción de datos: Si se detecta corrupción o inaccesibilidad en la base de datos principal, activará automáticamente la recuperación desde la réplica mas cercana disponible de la zona. Si el incidente persiste, se ejecutará la restauración puntual desde AWS Backup Vaults, verificando la integridad antes de la reapertura del servicio (con el estado de los últimos 15 minutos).

- Error en despliegue o actualización de software: En caso de fallas durante la actualización del sistema, se revertirá automáticamente a la versión anterior mediante el entorno Canary.

- Incidente de ciberseguridad o ataque (ransomware, intrusión, DDoS): Se aislará el entorno afectado y se activará el protocolo de respuesta a incidentes de seguridad (IRP). Los datos se restaurarán desde respaldos inmutables de AWS Backup, y se deberá contratar un experto en redes y ciberseguridad o pedir al mismo equipo de redes de la organización que realicen un escaneo de la red y analice el sistema SD-WAN para detectar que parte ha sido comprometida.

- Falla en integraciones HL7/FHIR o APIs externas: Ante errores de interoperabilidad, entre microservicios o con sistemas/API’s externas se generarán logs y avisos en las pantallas para avisar a los trabajadores de los posibles problemas, además de realizar copias locales en memoria volátil de los datos generados hasta que se resuelvan las fallas del sistema.

- Falla eléctrica o del data center local: En caso de interrupciones de energía o daños físicos en la infraestructura local, las operaciónes y datacenter seguirán en funcionamiento durante unas horas gracias a sistemas UPS, y en caso de ser por falla de componentes físicos, el sistema aislará este componente y lo apagará sin dejar de suministrar energía al resto del sistema.

#### 3.4.7 Capacidades de auto-recuperación del sistema

La infraestructura ha sido diseñada para mantener la continuidad operacional mediante mecanismos de auto-recuperación, basados en los servicios nativos de alta disponibilidad y monitoreo continuo de la nube AWS. Cada microservicio dispone de verificaciones automáticas de estado (verificaciones configuradas health checks) que permiten reiniciar instancias en caso de falla y redistribuir la carga de manera horizontal. Las

<!-- Página 52 del PDF original -->

instancias degradadas de contenedores de microservicios son reemplazadas dinámicamente por nuevas, asegurando que el sistema mantenga su disponibilidad. Estos procesos se complementan con alertas automáticas hacia el Centro de Operaciones y registros de auditoría (logs) que permitirán validar la recuperación.

#### 3.4.8 Plan de Rollback

Para asegurar que los servicios sigan disponibles el mayor tiempo posible y que el sistema estará preparado para responder ante incidentes o problemas de distintos ambitos que impidan el funcionamiento regular del sistema, se diseñará un plan de Rollback, basado en la tecnología de solución de AWS Backup para cumplir con los acuerdos SLA de RTO y RPO.

Los servicios y módulos considerados críticos para la continuidad operativa son aquellos que al no presentarse como disponibles, afectarían directamente la operación principal del servicio y la atención a los usuarios finales, poniendo en riesgo tanto la experiencia de los clientes/pacientes como inclusive sus vidas en casos particulares. Serán considerados como críticos y/o prioritarios los servicios: HCE, Facturación y co-

≤ branza, Gestión de pacientes y módulos de pacientes, donde se acordará un RTO 30

≤ minutos y un RPO 15 minutos para estos, dándoles máxima prioridad para la operabilidad del sistema.

##### 1 - Principios generales

- Los entornos de producción y staging operarán bajo un modelo canary, lo que permite revertir a la versión anterior en caso de errores o degradación del rendimiento considerando el estado del sistema de los últimos 15 minutos.

- Cada cambio se versiona y etiqueta bajo control de commits de Git, permitiendo restaurar la última versión estable del código o infraestructura mediante la herramienta de versiones.

##### 2 - Respaldo y restauración de datos

- Se utilizará AWS Backup como herramienta centralizada de gestión de copias de seguridad, programando respaldos automáticos diarios de las bases de datos (Aurora PostgreSQL, Amazon DocumentDB).

- Los respaldos se almacenarán cifrados (AES-256) y replicados en al menos 2 Datacenter para garantizar su integridad y disponibilidad ante eventos de falla regional.

##### 3 - Procedimiento de rollback

<!-- Página 53 del PDF original -->

1. Activación automática: Rollback automático a la versión anterior mediante Gi-

tOps o despliegue canary validado.

2. Restauración de datos: Si hay corrupción o pérdida de información, restauración

puntual desde AWS Backup del último punto de recuperación válido (según RPO).

3. Verificación post-restauración: Ejecución de pruebas automáticas y manuales

para confirmar la estabilidad y consistencia de los datos restaurados.

4. Revisión y documentación: Finalmente registro del incidente, causas, tiempos

de recuperación y lecciones aprendidas; actualización del plan de mejora continua.

4 - Pruebas y mantenimiento del plan El plan de rollback deberá realizarse periodicamente y de forma controlada al menos una vez cada 3 meses, en ambientes de pruebas y simulando casos de fallas totales o parciales que representen fallas comunes, raras e inusuales, midiendo el resultado de estas pruebas en base a las métricas de cumplimiento de los SLA’s definidos de RTO y RPO, además del % de igualdad de los datos luego de las pruebas de recuperación comparados con los datos previos a las pruebas.

<!-- Página 54 del PDF original -->

## 4 Descripción Lógica de la Solución

### 4.1 Esquema Solución

En la siguiente sección se abarcará el esquema de la solución desarrollada, para la cual se consideró una organización de módulos basada en funcionalidades, ya que ofrece una representación más clara de cómo interactúan los distintos módulos del sistema entre sí. Este enfoque permite comprender de manera integral la lógica de la solución, visualizar las dependencias entre módulos y facilitar su futura escalabilidad con módulos independientes, aunque conectados en casos particulares.

Con base en lo mencionado previamente, se definió un total de 7 módulos principales que componen la solución, los que a su vez contienen sub-módulos de las secciones más específicas, las cuales serán detalladas más adelante. A través de esta sección se especificarán los diferentes actores que se relacionarán con el sistema y cómo se espera que interactúen con el mismo. Por último, se abarcará en detalle el flujo de funcionamiento de cada uno de los módulos y sub-módulos del sistema, para esclarecer el alcance de la solución planteada.

En el sistema se ha considerado una clasificación de actores en cuatro grupos principales, cada uno con un rol específico en el funcionamiento de la solución. En primera instancia, se encuentran los Pacientes, quienes son los destinatarios directos de la atención y constituyen el eje central de todos los procesos. Su interacción con el sistema orienta el diseño de los servicios y módulos ofrecidos. En segundo lugar, se encuentra el Personal Médico, responsable de proporcionar atención clínica y farmacéutica, asegurando la correcta gestión de los pacientes y el registro de la información en el historial clínico electrónico. Este grupo es fundamental para garantizar que la atención se brinde de manera eficiente y segura. En paralelo, el Personal Administrativo cumple

<!-- Página 55 del PDF original -->

un rol clave en la gestión operativa, tecnológica y financiera del sistema, asegurando que todos los procesos internos funcionen de manera coordinada, desde la asignación de recursos hasta el mantenimiento de la infraestructura tecnológica. Finalmente, el grupo de Gerente y Dirección agrupa a quienes supervisan la calidad de los servicios, velan por el cumplimiento regulatorio, toman decisiones estratégicas y operativas de alto nivel y coordinan la logística asociada a los recursos del sistema. Este grupo asegura que la organización opere de manera eficiente, cumpliendo con los estándares institucionales y normativos, y mantiene la visión estratégica que guía el desarrollo y operación de la solución.

De los usuarios generales presentados previamente, se desglosa el siguiente listado específico de actores.

- Personal Médico

  - Médico/a

  - Enfermero/a

  - Farmacéutico/a

- Personal Administrativo

  - Empleado/a Call Center - CMR

  - Recepcionista

  - Administrativo/a TI

  - Empleado/a TI

  - Empleado/a RRHH

  - Empleado/a Facturación y Cobranza

  - Empleado/a Contabilidad

- Gerencia y dirección

  - Encargado/a de Calidad/Regulatorio

  - Gerente de Calidad/Regulatorio

  - Operadores de Bodega

  - Gerente de Bodega

  - Gerente General

- Pacientes

<!-- Página 56 del PDF original -->

#### 4.1.1 Esquema General de la solución

Figure 4.1: Esquema general de la solución.

El esquema general de la solución (Figura4.1), corresponde a una representación visual general de cómo se comportarán los distintos actores y módulos definidos en este proyecto para el software propuesto HospiNet.

Primeramente, se representan los grupos de actores definidos previamente junto con Amazon Web Services (AWS), que actúa como la plataforma tecnológica responsable de proporcionar la infraestructura y los servicios necesarios para el despliegue y operación del sistema. Posteriormente, los actores se conectan a HospiNet, el cual canaliza el acceso de los usuarios hacia los distintos portales según el nivel de permisos asignado, dando origen a cuatro portales principales. Cada portal ofrece acceso a los módulos funcionales de la solución conforme a las necesidades específicas de cada perfil de usuario.

Entre los principales módulos del sistema se encuentran los siguientes:

1. Módulo Pacientes

2. Módulo Comunicación

3. Módulo Gestión

4. Módulo Finanzas

5. Módulo Inteligencia

6. Módulo Cadena de Suministro

7. Módulo Administrativo TI

Como se puede apreciar en el diagrama del esquema general (Figura 4.1), existen módulos que interactúan con distintos tipos de usuarios. Si bien todos los módulos forman

![Página 56 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-056.png)

<!-- Página 57 del PDF original -->

parte de la misma plataforma, cada usuario posee perspectivas y vistas diferenciadas, acorde a sus permisos y funciones dentro del sistema.

A continuación, se detalla cómo se relacionan los distintos usuarios con los módulos, describiendo los permisos disponibles y las funcionalidades a las que cada tipo de usuario puede acceder.

##### Paciente

El usuario de tipo Paciente tiene acceso a los módulos que permiten gestionar directamente su atención y comunicación con el sistema de salud. Los permisos del paciente se centran en los módulos Pacientes y Comunicación, los cuales facilitan la interacción con la plataforma y con el personal de salud.

- Módulo Pacientes: los pacientes pueden consultar y actualizar su información personal, revisar su historial clínico electrónico (HCE), y realizar seguimiento de sus controles médicos y tratamientos. Este módulo asegura que el paciente tenga una visión íntegra de su estado de salud, así como la posibilidad de recibir alertas sobre medicamentos y próximos procedimientos.

- Módulo Comunicación: permite a los pacientes agendar citas mediante múltiples canales, comunicarse con el personal administrativo o médico, recibir notificaciones y alertas, y acceder al Call Center para consultas telefónicas o virtuales.

##### Médico

Al igual que el tipo de usuario anterior, el usuario de tipo Médico tiene permisos sobre los módulos Pacientes y Comunicación, lo que le permite gestionar la atención clínica y la interacción con los pacientes de manera directa y segura.

- Módulo Pacientes: los médicos pueden consultar y actualizar historiales clínicos, registrar procedimientos, planificar seguimientos y gestionar urgencias. Este acceso les permite tener una visión completa de la evolución de cada paciente y tomar decisiones informadas sobre su atención.

- Módulo Comunicación: permite coordinar las citas de los pacientes, realizar telemedicina y mantener una comunicación constante con los usuarios. Además, posibilita enviar alertas y recordatorios sobre controles y tratamientos.

##### Administrativo

El usuario de tipo Administrativo tiene acceso a los módulos Comunicación, Gestión y Finanzas, enfocándose en la gestión operativa, logística y económica del sistema.

- Módulo Comunicación: el personal administrativo gestiona la interacción con los pacientes, coordina el agendamiento multicanal de citas y atiende solicitudes a través del Call Center.

<!-- Página 58 del PDF original -->

- Módulo Gestión: permite administrar los recursos humanos, asignar permisos internos, coordinar turnos y supervisar procesos operativos.

- Módulo Finanzas: otorga acceso a la facturación, cobranza y contabilidad, permitiendo al personal administrativo gestionar los flujos económicos del sistema, revisar pagos pendientes y generar reportes financieros confiables.

##### Gerente y Dirección

El usuario de tipo Gerente o Director tiene permisos estratégicos sobre los módulos Finanzas, Inteligencia y Cadena de Suministro, permitiendo una supervisión integral de la organización.

- Módulo Finanzas: los gerentes pueden supervisar la facturación y cobranza, controlar la contabilidad general y garantizar la sostenibilidad económica del sistema.

- Módulo Inteligencia: proporciona acceso a dashboards de negocio, monitoreo de la plataforma y analítica avanzada, permitiendo tomar decisiones estratégicas basadas en datos, evaluar KPIs y realizar predicciones sobre la operación y el desempeño de la organización.

- Módulo Cadena de Suministro: permite gestionar la trazabilidad de insumos, supervisar inventarios, coordinar el transporte y almacenamiento de productos, y garantizar la eficiencia logística de la organización. Este acceso asegura que los recursos estén disponibles de manera oportuna y cumplan con los estándares de calidad requeridos.

##### Administrador TI

El usuario de tipo Administrador TI posee un acceso transversal a los módulos críticos que soportan la operación tecnológica de la plataforma, garantizando el correcto funcionamiento, seguridad, disponibilidad e interoperabilidad del sistema HospiNet. A diferencia de otros perfiles, su perspectiva se orienta a la supervisión de la infraestructura tecnológica, la gestión de usuarios, la validación de integraciones externas y el aseguramiento de la continuidad operativa. Sus permisos se distribuyen principalmente sobre los módulos Inteligencia, Cadena de Suministro e Integración, cada uno de los cuales aporta capacidades clave para la administración técnica del ecosistema.

- Módulo Inteligencia: el Administrador TI accede a herramientas avanzadas de monitoreo y análisis que le permiten supervisar el comportamiento de la plataforma en tiempo real. Puede visualizar métricas técnicas, histórico de disponibilidad, uso de recursos, patrones de rendimiento y alertas asociadas a fallas o degradaciones del servicio. Este módulo proporciona dashboards orientados al análisis de KPIs técnicos, permitiendo identificar anomalías, anticipar incidentes y ejecutar medidas de mejora continua basadas en datos.

<!-- Página 59 del PDF original -->

- Módulo Cadena de Suministro: dentro de este módulo, el Administrador TI gestiona los recursos tecnológicos, asegurando la trazabilidad de equipamiento, licencias, dispositivos médicos conectados y componentes críticos de infraestructura. También coordina el ciclo de vida de activos TI, supervisa inventarios tecnológicos y controla la disponibilidad de equipamiento necesario para garantizar la operación segura y estable de la plataforma. Este módulo permite al Administrador TI mantener control sobre los elementos físicos y lógicos que sustentan los sistemas clínicos y administrativos.

- Módulo de Integración: este módulo constituye una de las principales áreas de responsabilidad del Administrador TI, ya que permite gestionar y controlar los servicios de interoperabilidad con plataformas externas. El usuario TI puede configurar, supervisar y validar integraciones basadas en estándares HL7, FHIR, CDA, DICOM y API REST; asegurando que los flujos de información entre HospiNet y sistemas de terceros, se mantengan íntegros y operativos. Además, puede monitorear logs de interoperabilidad, revisar errores de mensajería, habilitar nuevos endpoints de integración y aplicar políticas de seguridad sobre los canales de intercambio de datos.

#### 4.1.2 Módulo Pacientes

Figure 4.2: Módulo de Pacientes

El diagrama del Módulo de Seguimiento de Pacientes muestra el flujo de datos que se genera desde el momento en que un usuario accede al sistema hasta que la información es registrada y procesada dentro de la Historia Clínica Electrónica. Una vez que el

![Página 59 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-059.png)

<!-- Página 60 del PDF original -->

usuario ingresa sus credenciales en HospiNet, el sistema valida la identidad y redirige los datos de sesión hacia el portal correspondiente, separando la ruta de pacientes y médicos. En el caso de los pacientes, el sistema consulta la base de datos de HCE para entregar información como recetas, historial y exámenes, y desde allí habilita el envío de datos hacia el Módulo de Seguimiento, ya sea mediante registros manuales o mediante transmisión automática desde la App HospiNet o dispositivos conectados, que actualizan en tiempo real los parámetros clínicos del usuario.

Por su parte, cuando el médico accede al portal profesional, el sistema le provee los datos clínicos relevantes desde la HCE y permite que las nuevas acciones realizadas se integren nuevamente a la base de datos. Dentro del Módulo de Seguimiento, los datos provenientes del paciente se procesan según el plan activo por patología, actualizando el estado del seguimiento y generando alertas, recordatorios o derivaciones cuando corresponde. Todo el flujo mantiene una trazabilidad completa, asegurando que la información circule entre portales, módulo de seguimiento y base de datos de forma continua, validada y sincronizada.

#### 4.1.3 Módulo Comunicación

Figure 4.3: Módulo de Comunicación

El diagrama del Módulo de Comunicación muestra el flujo de datos que coordina la interacción entre pacientes, personal médico y los distintos canales disponibles para agendar o gestionar atenciones. Una vez que el paciente accede al sistema HospiNet, los datos ingresados se envían al módulo de comunicación, donde el sistema distribuye la solicitud según el canal utilizado: cita presencial, telemedicina, call center, chat en

![Página 60 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-060.png)

<!-- Página 61 del PDF original -->

vivo, WhatsApp Business, chatbot o correo de soporte. Cada canal genera una solicitud de agenda que el módulo procesa consultando la disponibilidad del personal médico, devolviendo los datos actualizados para confirmar o rechazar la reserva.

Cuando existe disponibilidad, el sistema registra la cita, actualiza la programación del profesional y envía los datos hacia el portal del paciente, generando además una notificación automática de confirmación. Si la solicitud es rechazada, el módulo comunica el resultado al paciente por el mismo canal utilizado. De forma paralela, el call center recibe datos mediante IVR o distribución automática de llamadas, permitiendo al empleado acceder a la información clínica necesaria e interactuar con el módulo de seguimiento si corresponde. Todo el flujo mantiene sincronizada la agenda, los canales de contacto y la información clínica relevante, asegurando continuidad y trazabilidad en las comunicaciones del sistema.

#### 4.1.4 Módulo Gestión

Figure 4.4: Módulo de Gestión

El diagrama del Módulo de Gestión muestra el flujo de datos que coordina la administración del capital humano y la seguridad de los accesos dentro de la institución. Una vez que se interactúa con el sistema HospiNet, la operación se dirige al módulo de gestión, donde el sistema distribuye las tareas en dos áreas críticas: Recursos Humanos y Control de Acceso. En el área de RRHH, el personal administrativo inicia el flujo con el reclutamiento y selección, avanzando hacia la contratación, la cual se nutre de la

![Página 61 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-061.png)

<!-- Página 62 del PDF original -->

gestión de turnos para definir las condiciones laborales. Una vez formalizado, se registran los datos del personal y se procesa la nómina, enviando la información financiera resultante directamente al Módulo de Finanzas, además de permitir la generación de reportes de productividad.

De forma paralela, el Administrador TI opera el componente de Control de Acceso para gestionar la seguridad lógica del sistema. Este flujo permite iniciar el alta de personal mediante la creación de cuentas de usuario, asignando los roles y permisos pertinentes para finalizar con la creación de la credencial de acceso. Asimismo, el módulo faculta la modificación de cuentas ya existentes, derivando en acciones de mantenimiento como eliminar o bloquear usuarios, o bien, restablecer permisos y credenciales. Todo el flujo mantiene sincronizada la información del personal con sus privilegios de seguridad y su estado financiero, asegurando la integridad operativa y administrativa del sistema.

#### 4.1.5 Módulo Finanzas

Figure 4.5: Módulo de Finanzas

El diagrama del Módulo de Finanzas muestra el flujo de datos que coordina la gestión económica, interactuando con el personal de facturación, la dirección de cobranza y las entidades externas para el procesamiento de pagos y registros contables. Una vez que el Empleado de Facturación o la Dirección de Cobranza acceden al sistema HospiNet, la operación se envía al módulo de finanzas, donde el sistema distribuye la tarea según su naturaleza hacia dos áreas principales: Facturación y Cobranza, o Contabilidad. En el área de Facturación y Cobranza, el módulo gestiona los flujos monetarios de entrada y salida; procesa los pagos de sueldos a empleados pasando por el cálculo de nómina y transferencia de fondos hasta generar el comprobante, mientras que simultáneamente administra la cobranza de servicios mediante canales como Webpay, tarjetas o efectivo, culminando con la emisión de la boleta física y electrónica.

![Página 62 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-062.png)

<!-- Página 63 del PDF original -->

De forma paralela, el área de Contabilidad se encarga de registrar las operaciones y cumplir con las normativas. Este flujo procesa los convenios para la generación y registro de bonos electrónicos destinados a la facturación con Isapres y Fonasa, además de generar los asientos contables internos. Asimismo, el sistema compila los datos necesarios para emitir los reportes oficiales requeridos por la Superintendencia de Salud. Todo el flujo mantiene sincronizada la tesorería, la facturación a aseguradoras y el cumplimiento normativo, asegurando la integridad y trazabilidad de los recursos financieros del sistema.

#### 4.1.6 Módulo Cadena de Suministro

Figure 4.6: Módulo de Cadena de Suministro

El diagrama del Módulo de Cadena de Suministro representa el flujo de datos que se genera desde la interacción del Gerente o equipo de Dirección con el sistema, hasta su procesamiento dentro de las diferentes funcionalidades operativas. Una vez que el usuario accede al Sistema HospiNet, los datos de autenticación son validados y redirigidos al módulo de cadena de suministro, donde el sistema consulta información en tiempo real sobre inventarios, movimientos logísticos y niveles de stock.

A partir de esta consulta inicial, el módulo distribuye los datos hacia sus distintos componentes: la información de inventario alimenta funciones como la verificación de stock y reservas por prioridad, mientras que los registros de entrada y salida se

![Página 63 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-063.png)

<!-- Página 64 del PDF original -->

procesan en el submódulo de movimientos logísticos. De forma paralela, los datos de transporte y distribución se utilizan para el monitoreo de rutas y costos, y se integran con los análisis de productividad y espacio para generar métricas de desempeño. Finalmente, el sistema consolida toda esta información para asegurar trazabilidad y calidad, permitiendo al gerente visualizar indicadores clave y optimizar la ubicación del stock según las necesidades operativas. De este modo, el flujo de datos entre el sistema central, los componentes logísticos y las funciones analíticas se mantiene sincronizado y actualizado para una gestión eficiente de la cadena de suministro.

#### 4.1.7 Módulo Integración

FALTA DIAGRAMA

### 4.2 Arquitectura Lógica

En la siguiente sección se describe la arquitectura lógica de la solución propuesta, la cual se basa en un enfoque de microservicios distribuidos en diversas capas interconectadas que garantizan modularidad, escalabilidad y resiliencia. Cada una de estas capas cumple funciones específicas y se comunica con las demás mediante APIs y un bus de eventos, lo que favorece la integración, el mantenimiento y la evolución del sistema.

En este contexto, la capa de cliente gestiona la interacción con los usuarios, la capa de presentación administra la interfaz de usuario, la capa de negocio incorpora la lógica que define el comportamiento del sistema, la capa de servicios ofrece las operaciones y funcionalidades necesarias, y la capa de datos se encarga del acceso, almacenamiento y administración de la información. Esta arquitectura modular permite una clara separación de responsabilidades, lo que facilita su rendimiento, mantenimiento y escalabilidad.

<!-- Página 65 del PDF original -->

Figure 4.7: Arquitectura Lógica

#### 4.2.1 Capa Cliente

Esta capa representa a los distintos usuarios que interactúan directamente con la plataforma, lo que será graficado a través de diferentes colores. Su rol es fundamental, ya que, constituyen los puntos de entrada del sistema y determinan los casos de uso principales.

- Pacientes: Representados por el color rosado, corresponden a los usuario finales del sistemas que acceden al sistema para gestionar citas, revisar resultados y utilizar servicios de telemedicina.

- Personal Médico: Representados por el color celeste, corresponden a los profesionales de la salud que emplean el HCE y herramientas clínicas para registrar, consultar y actualizar información médica de los pacientes.

- Personal Administrativo: Representados por el color verde, corresponden a los usuarios encargados de los procesos de admisión, facturación, cobranza y gestión financiera.

- Gerencia y dirección: Representados por el color morado, se encuentra la Gerencia General y la Dirección Médica, quienes cumplen la función de definir lineamientos estratégicos, validar decisiones claves y supervisar que la implementación esté alineada con la misión institucional y objetivos regulatorios.

![Página 65 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-065.png)

<!-- Página 66 del PDF original -->

Los usuarios podrán acceder al sistema desde dispositivos móviles y computadores, garantizando flexibilidad y disponibilidad en distintos entornos. No obstante, el sistema también contempla métodos de autenticación, como el ingreso mediante acceso biométrico (huella dactilar) y a través de tótems interactivos instalados en las dependencias de la organización. Estos mecanismos buscan fortalecer la seguridad del acceso, agilizar los procesos de identificación y ofrecer una experiencia más práctica y confiable para los diferentes tipos de usuarios.

#### 4.2.2 Capa de Presentación

En esta capa se desarrollan las interfaces de usuario que permiten la interacción entre los actores y la plataforma. La prioridad es ofrecer experiencias intuitivas, seguras y accesibles desde cualquier dispositivo.

El sistema cuenta con portales diseñados para cada tipo de usuario, los cuales, según la necesidad, estarán disponibles en distintos medios. A continuación, se detallan las tecnologías utilizadas y las funciones que ofrece cada portal.

- Portal de Pacientes: Disponible a través de la aplicación móvil y su versión web. Este portal permite a los pacientes gestionar sus citas médicas, revisar resultados clínicos, realizar pagos de prestaciones y acceder a su historial médico digital.

- Portal Médico: Disponible mediante la aplicación móvil y su versión web. Permite registrar atenciones en la HCE, consultar antecedentes de pacientes, realizar seguimiento y coordinar tratamientos o derivaciones.

- Portal Administrativo: Disponible únicamente como aplicación web. Permite gestionar procesos como la admisión de pacientes, facturación, cobranza, atención mediante call center y soporte en la coordinación de servicios clínicos y administrativos.

- Portal Gerencial: Disponible únicamente como aplicación web. Permite supervisar el funcionamiento general del sistema y revisar indicadores de desempeño y reportes estratégicos.

- Portal TI Disponible como aplicación web, el Portal TI está diseñado para la gestión y administración de los aspectos tecnológicos de la solución. Permite al personal de soporte y administración de sistemas supervisar la infraestructura tecnológica, administrar usuarios, configurar permisos, monitorear el rendimiento de los servicios, gestionar incidencias técnicas y coordinar tareas de mantenimiento.

- Aplicación Móvil: Desarrollada con Dart Flutter, compatible con dispositivos Android e iOS. Dentro de la solución se consideraron dos aplicaciones distintas, una diseñada para pacientes y otra para el personal médico.

- Aplicación Web: Compatible con navegadores basados en Chromium. La estructura presenta un portal general que redirige a los portales específicos según el tipo de usuario.

<!-- Página 67 del PDF original -->

En cuanto a las tecnología, se emplearon de manera transversal Angular, JavaScript y Tailwind CSS para el desarrollo de las interfaces web y móviles, garantizando una experiencia de usuario moderna, dinámica y adaptable a distintos dispositivos. En materia de seguridad y gestión de identidades, se implementó Keycloak como sistema central de autenticación y autorización, el cual utiliza el protocolo OpenID Connect (OIDC) sobre OAuth 2.0. Esta integración permite administrar de forma unificada el acceso de los usuarios, ofreciendo autenticación segura, control de roles, inicio de sesión único (SSO) y soporte para autenticación multifactor.

#### 4.2.3 Capa de Negocio

Esta capa gestiona la lógica de negocio del sistema, centralizando los procesos clínicos, administrativos, financieros y estratégicos de la institución. Cada módulo está diseñado para cubrir un ámbito funcional específico y se comunica con los demás mediante servicios y APIs integradas, garantizando la trazabilidad, seguridad y consistencia de la información en toda la plataforma.

- Módulo de Finanzas: Diseñado para administrar los procesos contables y financieros de la institución. Gestiona facturación electrónica, cobranza, convenios con aseguradoras y control de caja, garantizando trazabilidad, transparencia y eficiencia en la gestión económica.

- Módulo de Cadena de Suministros: Su objetivo es optimizar el flujo de insumos médicos, farmacéuticos y administrativos. Controla inventarios, proveedores, órdenes de compra y distribución interna, asegurando la disponibilidad continua de recursos críticos para la atención médica.

- Módulo de Gestión: Encargado de la administración operativa del sistema, supervisando su funcionamiento, seguridad y configuración. Permite gestionar roles, accesos, notificaciones y monitoreo en tiempo real, asegurando estabilidad y cumplimiento normativo.

- Módulo de Comunicación: Centraliza la interacción entre pacientes, médicos y personal administrativo. Integra el call center, mensajería interna y telemedicina, permitiendo una atención continua, coordinada y con trazabilidad de las comunicaciones.

- Módulo de Pacientes: Focalizado en la atención clínica y la experiencia del usuario. Gestiona la Historia Clínica Electrónica, citas médicas, seguimiento y portales de acceso diferenciados para pacientes, médicos, administrativos y gerencia.

- Módulo de Inteligencia: Diseñado para el análisis de datos y soporte a la toma de decisiones. Genera indicadores clínicos, financieros y operativos mediante tableros BI y análisis predictivo, contribuyendo a la mejora continua y planificación estratégica.

- Módulo de Integración AÑADIR DESCRIPICIÓN

<!-- Página 68 del PDF original -->

#### 4.2.4 Capa Cache

Esta capa se encuentra estratégicamente ubicada entre la Capa de Negocio y la Capa de Datos, teniendo como propósito fundamental mejorar el rendimiento y la eficiencia general del sistema, mediante el almacenamiento en memoria de los datos que se consultan con mayor frecuencia, así como los resultados precalculados de consultas complejas. Al reducir la necesidad de acceder continuamente a la base de datos subyacente, se disminuye la carga operativa y se acelera significativamente el tiempo de acceso a la información. De esta manera, la Capa Cache asegura que las solicitudes de los usuarios se procesen de manera más rápida y eficiente, optimizando los tiempos de respuesta del sistema y aliviando el estrés sobre los recursos de la base de datos.

#### 4.2.5 Capa de Datos

La capa de datos es la encargada del almacenamiento, organización y disponibilidad de toda la información que circula en la plataforma, garantizando integridad, seguridad y consistencia. La solución adopta una arquitectura híbrida, combinando un centro de datos local y la infraestuctura en la nube, con un sistema de replicación bidireccional que asegura la sincronización continua entre ambos entornos.

- Data Center: El Data Center local concentra las bases de datos críticas para la operación interna del sistema. Utiliza PostgreSQL como base relacional para almacenar información estructurada vinculada a la gestión financiera, control de acceso, recursos humanos y la Historia Clínica Electrónica (HCE). Además, aloja repositorios adicionales, como la base de datos de bodega, orientada a la administración logística y de suministros. Esta infraestructura local proporciona control directo, seguridad avanzada y respaldo mediante AWS Backup, manteniendo la continuidad operativa incluso sin conexión a la nube.

- Nube (AWS): El entorno en la nube se apoya en Amazon Aurora, compatible con PostgreSQL, para manejar los datos transaccionales y operativos de los módulos principales. Asimismo, se utilizar Amazon DocumentDB, para almacenar información semiestructurada proveniente de registros clínicos, análisis predictivos y comunicaciones. Ambas tecnologías trabajan en conjunto con un sistema de backup automatizado y replicación al Data Center.

#### 4.2.6 Capa de Servicios Externos

Esta cada se encarga de agrupar las integraciones con sistemas de terceros que complementan la solución.

- Talana: plataforma integrada para la gestión de recursos humanos, control de asistencia y administración de remuneraciones del personal médico y administrativo, garantizando eficiencia en los procesos laborales.

<!-- Página 69 del PDF original -->

- Pasarelas de Pago: utilizadas para procesar pagos electrónicos de prestaciones médicas, permitiendo transacciones seguras, conciliaciones automáticas y trazabilidad financiera en tiempo real.

- SolarWinds: servicio de monitoreo y observabilidad de la infraestructura tecnológica, que permite supervisar el rendimiento de los servidores, redes y aplicaciones, asegurando la continuidad y estabilidad operativa del sistema.

- Fonasa e Isapres: integrados para la validación de afiliaciones, cobertura de seguros médicos y emisión de bonos electrónicos, facilitando la interoperabilidad con los sistemas de salud nacionales y agilizando la atención al paciente.

#### 4.2.7 Arquitectura Lógica: Pacientes

En esta sección se presentarán los módulos de la arquitectura con mayor impacto para cada tipo de usuario, comenzando con el área orientada a los pacientes.

Figure 4.8: Arquitectura Lógica: Caso de Pacientes

![Página 69 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-069.png)

<!-- Página 70 del PDF original -->

##### Módulo Pacientes

El Módulo de Paciente está diseñado para ofrecer a los usuarios un acceso centralizado y seguro a toda su información médica y servicios de salud. Mediante el portal web o la aplicación móvil, los pacientes pueden gestionar sus citas médicas, revisar resultados de exámenes, acceder a su historial clínico completo y recibir recordatorios automatizados sobre controles y medicamentos. Su interfaz intuitiva facilita la autogestión de la atención, promoviendo una experiencia segura, personalizada y orientada al bienestar del usuario.

##### Módulo Comunicación

Este módulo permite a los pacientes interactuar de manera directa y segura con el personal médico y administrativo a través de mensajería instantánea, videollamadas y notificaciones automáticas. Facilita la atención a distancia mediante servicios de telemedicina, asegurando que la comunicación sea continua, rápida y trazable. Los pacientes pueden enviar consultas, recibir orientación y coordinar procedimientos sin necesidad de desplazarse, mejorando la accesibilidad y eficiencia del sistema de salud.

#### 4.2.8 Arquitectura Lógica: Personal Médico

A continuación, se presentarán los módulos significativos para el personal médico.

<!-- Página 71 del PDF original -->

Figure 4.9: Arquitectura Lógica: Caso de Personal Médico

##### Módulo de Paciente

El Módulo de Paciente para el personal médico proporciona herramientas completas para registrar, consultar y actualizar información clínica dentro de la Historia Clínica Electrónica (HCE). Permite emitir diagnósticos, prescribir recetas electrónicas y realizar seguimientos clínicos detallados de cada paciente. Se integra con sistemas de laboratorio y dispositivos médicos IoT, garantizando la disponibilidad de datos en tiempo real y fortaleciendo la continuidad asistencial. Este módulo respalda la toma de decisiones clínicas precisas y optimiza la calidad del servicio médico, reduciendo errores y mejorando la coordinación del tratamiento.

![Página 71 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-071.png)

<!-- Página 72 del PDF original -->

##### Módulo de Comunicación

Este módulo ofrece a los profesionales de la salud un canal eficiente para coordinar con pacientes y otros colegas dentro del sistema médico. Integra mensajería segura, alertas sobre eventos clínicos y teleconsultas, facilitando la colaboración entre diferentes especialidades y áreas asistenciales. Mejora la coordinación del equipo médico y permite una atención remota rápida y confiable. Su diseño garantiza la privacidad de la información y acelera los tiempos de respuesta ante necesidades críticas del paciente.

#### 4.2.9 Arquitectura Lógica: Personal Administrativo

La siguiente sección abarca los módulos significativos para el personal administrativo.

Figure 4.10: Arquitectura Lógica: Caso de Personal Administrativo

##### Módulo de Finanzas

El Módulo de Finanzas está orientado a la gestión integral de los procesos contables y financieros dentro del sistema de salud. Permite administrar facturación, cobranza, convenios y flujos de pago de manera automatizada y trazable. Facilita la generación de

![Página 72 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-072.png)

<!-- Página 73 del PDF original -->

reportes financieros y la supervisión de operaciones, asegurando la transparencia y reduciendo errores humanos. Su diseño optimiza la eficiencia administrativa, apoyando la sostenibilidad económica y el cumplimiento de normas contables y regulatorias.

##### Módulo de Gestión

El Módulo de Gestión brinda las herramientas necesarias para administrar usuarios, roles, notificaciones y agendas médicas. Facilita la configuración y supervisión de las operaciones administrativas, garantizando el cumplimiento de políticas internas y la correcta asignación de permisos. Su enfoque operativo asegura la continuidad del servicio y el control efectivo del entorno institucional.

#### 4.2.10 Arquitectura Lógica: Gerente y Dirección

En esta sección se abordan los módulos significativos para los usuarios de Gerencia y Dirección.

<!-- Página 74 del PDF original -->

Figure 4.11: Arquitectura Lógica: Caso de Gerencia y Dirección

##### Módulo de Inteligencia

El Módulo de Inteligencia está diseñado para entregar a la Gerencia y Dirección una visión global del desempeño clínico, operativo y financiero. A través de tableros BI y reportes dinámicos, los directivos pueden monitorear indicadores estratégicos y evaluar el cumplimiento de metas institucionales. Este módulo permite tomar decisiones informadas, basadas en datos precisos y actualizados.

##### Módulo de Gestión

El Módulo de Gestión otorga a la Gerencia la capacidad de supervisar la administración general del sistema y aplicar políticas organizacionales. Permite controlar roles, accesos, recursos y configuraciones clave, asegurando el alineamiento con los objetivos estratégicos y regulatorios de la institución. Además, facilita el seguimiento del desempeño de cada área, fortaleciendo la gobernanza institucional.

![Página 74 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-074.png)

<!-- Página 75 del PDF original -->

#### 4.2.11 Arquitectura Lógica: Administrador TI

En esta sección se presenta la arquitectura lógica específica para el actor Administrador TI; sin embargo, no se detallará como en casos anteriores, puesto que posee un rol muy similar al actor de Gerencia y Dirección, solo que orientado a la administración y gestión de las tecnologías (Software y Hardware).

Figure 4.12: Arquitectura Lógica: Caso de Administrador TI

#### 4.2.12 Especificación Tecnológica

En el contexto actual de transformación digital, es fundamental contar con una plataforma tecnológica innovadora, segura y escalable que permita la interacción eficiente entre los distintos actores del sistema. Con el propósito de optimizar los procesos internos, mejorar la experiencia de los usuarios y garantizar la continuidad operativa, hemos diseñado una solución integral que combina lo más avanzado en infraestructura en la nube, automatización de procesos, gestión de datos y seguridad de última generación.

Esta plataforma no solo busca simplificar la administración y el acceso a la infor-

![Página 75 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-075.png)

<!-- Página 76 del PDF original -->

mación, sino que también agrega valor mediante un enfoque centrado en el usuario, ofreciendo personalización, monitoreo en tiempo real y herramientas para el análisis y la toma de decisiones basadas en datos. Gracias a la integración de tecnologías líderes en la industria, aseguramos que la solución sea altamente flexible, escalable y confiable, adaptándose a las necesidades cambiantes de la organización y de sus usuarios.

A continuación, presentamos un desglose detallado de las tecnologías clave incorporadas en la plataforma, explicando cómo cada una contribuye a mejorar la eficiencia operativa, garantizar la seguridad y fortalecer la escalabilidad del sistema, generando un entorno confiable y robusto para todos los usuarios y procesos asociados.

##### Gestión y exposición de APIs

Tecnologías que permiten centralizar, controlar y asegurar la comunicación entre los distintos microservicios del sistema y aplicaciones externas. Facilitan la administración de rutas, la seguridad y el monitoreo de las APIs.

- Amazon API Gateway: servicio que actúa como punto de entrada único para todas las solicitudes hacia los microservicios del sistema. Gestiona el enrutamiento de solicitudes, autenticación de usuarios, control de tráfico, y protege las APIs contra accesos no autorizados. Esto permite centralizar la comunicación entre aplicaciones, simplificar la integración con servicios externos y reforzar la seguridad del sistema al controlar los accesos de manera unificada.

##### Desarrollo de aplicaciones

Esta categoría engloba lenguajes de programación y frameworks que permiten construir aplicaciones web y móviles, definiendo la lógica, interfaces y experiencia de usuario. Facilitan el desarrollo modular, ágil y escalable de los portales y aplicaciones.

- Angular: es un framework de desarrollo frontend basado en TypeScript, utilizado para construir interfaces web dinámicas y responsivas para los portales de pacientes, médicos, administrativos y gerenciales. Su arquitectura modular permite separar responsabilidades y reutilizar componentes, acelerando el desarrollo y facilitando el mantenimiento de las aplicaciones.

- JavaScript: es un lenguaje de programación esencial para el desarrollo web interactivo, permitiendo crear funcionalidades dinámicas en el cliente y comunicarse con APIs del backend. Ofrece compatibilidad universal con navegadores, alto rendimiento y flexibilidad para integrar librerías y frameworks adicionales.

- Dart y Flutter: Dart es el lenguaje de programación desarrollado por Google, y Flutter es el framework UI que permite crear aplicaciones móviles nativas multiplataforma. Esta combinación permite desarrollar una única base de código para Android e iOS, generando aplicaciones rápidas, modernas y con interfaces atractivas, reduciendo el tiempo y costo de desarrollo.

<!-- Página 77 del PDF original -->

- TypeScript: TypeScript es un lenguaje basado en JavaScript que añade tipado estático y control de errores en tiempo de compilación. Esto mejora la escalabilidad de las aplicaciones y facilita el trabajo colaborativo en equipos grandes, previniendo errores comunes y aumentando la productividad.

- Spring Framework: es una plataforma de desarrollo backend en Java que permite construir aplicaciones empresariales robustas y seguras. Facilita la creación de microservicios escalables, la integración con bases de datos y servicios externos, y la implementación de buenas prácticas de seguridad y modularidad en la arquitectura del sistema.

##### Contenedores y orquestación

Estas tecnologías permiten empaquetar, desplegar y ejecutar aplicaciones de manera consistente en cualquier entorno, simplificando la administración de infraestructura y escalabilidad.

- AWS ECS (Elastic Container Service): servicio de Amazon para ejecutar y administrar contenedores Docker en producción, permitiendo la automatización del despliegue, escalado y monitoreo de aplicaciones. Facilita mantener la disponibilidad y confiabilidad del sistema, reduciendo la carga operativa en la gestión de infraestructura.

- AWS Fargate: es una tecnología serverless que permite ejecutar contenedores sin gestionar servidores, asignando recursos bajo demanda. Optimiza costos, escala automáticamente según la carga de trabajo y simplifica el despliegue de microservicios en la nube.

- AWS Lambda: es un servicio de computación sin servidor que ejecuta funciones en respuesta a eventos, eliminando la necesidad de administrar infraestructura. Mejora la eficiencia del sistema al procesar tareas de forma reactiva, reducir costos operativos y permitir integraciones rápidas con otros servicios AWS.

- Docker: Docker es una plataforma de virtualización ligera que empaqueta aplicaciones y sus dependencias en contenedores portables. Garantiza entornos consistentes entre desarrollo y producción, facilita la implementación continua (CI/CD) y simplifica la portabilidad entre distintos entornos locales y en la nube.

- Keycloak: es un sistema de gestión de identidad y acceso (IAM) de código abierto que permite implementar autenticación, autorización y federación de identidades. Ofrece inicio de sesión único (SSO), autenticación multifactor y control de roles por usuario, fortaleciendo la seguridad y simplificando la gestión de accesos.

##### Bases de datos

Estas tecnologías almacenan, gestionan y facilitan el acceso a información estructurada y semiestructurada, permitiendo operaciones seguras, consistentes y escalables.

- PostgreSQL: es un sistema de gestión de bases de datos relacional de código

<!-- Página 78 del PDF original -->

abierto, utilizado para almacenar información estructurada como usuarios, autenticación y registros clínicos. Su robustez, soporte transaccional completo y extensibilidad lo hacen ideal para sistemas críticos que requieren alta confiabilidad.

- Amazon Aurora: es una base de datos relacional administrada compatible con PostgreSQL y MySQL. Combina el rendimiento de bases comerciales con la flexibilidad del software libre, ofreciendo alta disponibilidad, replicación automática y escalabilidad según la demanda.

- Amazon DocumentDB: es una base de datos no relacional compatible con MongoDB, diseñada para manejar información semiestructurada como historiales clínicos y registros operativos. Proporciona alto rendimiento, escalabilidad horizontal y facilita la integración con aplicaciones en tiempo real.

##### Almacenamiento y respaldo

Estas soluciones permiten guardar y proteger datos críticos del sistema, garantizando disponibilidad, durabilidad y recuperación ante fallas.

- Amazon S3: es un servicio de almacenamiento de objetos en la nube que aloja documentos, respaldos y archivos multimedia. Ofrece alta durabilidad, acceso global y costos escalables según la demanda, asegurando la disponibilidad de la información.

- AWS Backup: centraliza la gestión de copias de seguridad automatizadas de datos en AWS y entornos locales. Protege la información crítica, simplifica la recuperación ante desastres y garantiza la continuidad de las operaciones del sistema.

##### Seguridad y autenticación

Estas tecnologías protegen la información, controlan accesos y previenen ataques, asegurando la integridad y confidencialidad del sistema.

- AWS Shield: es un servicio de protección contra ataques DDoS que resguarda aplicaciones web y APIs públicas. Ofrece defensa automatizada, reduce tiempo de inactividad y ayuda a cumplir normas de seguridad, aumentando la resiliencia de los sistemas.

- Amazon KMS (Key Management Service): gestiona claves criptográficas para cifrar datos y controlar su acceso. Protege información sensible, asegura confidencialidad y facilita el cumplimiento normativo de estándares como HIPAA, ISO y GDPR.

- Keycloak: Además de su rol en contenedores, Keycloak fortalece la seguridad de la solución mediante autenticación segura, control granular de roles y administración centralizada de usuarios.

<!-- Página 79 del PDF original -->

##### Mensajería y eventos

Estas herramientas permiten la comunicación asincrónica entre sistemas y la integración basada en eventos, mejorando la escalabilidad y la respuesta del sistema.

- AWS SNS (Simple Notification Service): es un servicio de mensajería que envía notificaciones automáticas a usuarios o sistemas. Soporta múltiples canales (SMS, correo, API), escalabilidad global y comunicación asincrónica confiable.

- AWS SQS (Simple Queue Service): es un sistema de colas de mensajes que desacopla servicios, permitiendo que los microservicios se comuniquen de forma confiable y tolerante a fallos. Garantiza entrega de mensajes y escalabilidad sin afectar la disponibilidad del sistema.

- AWS EventBridge: es un bus de eventos que conecta aplicaciones mediante flujos de datos automáticos. Facilita la integración entre servicios sin escribir código complejo y mejora la capacidad de respuesta de la arquitectura a cambios o eventos.

##### Redes y comunicación

Incluye tecnologías que aseguran la conectividad entre los distintos módulos y usuarios del sistema, garantizando disponibilidad, enrutamiento y comunicación confiable.

- AWS Route 53: es un servicio de DNS administrado que enruta solicitudes a instancias o APIs de forma confiable. Proporciona alta disponibilidad, baja latencia y administración simplificada del tráfico de usuarios.

- REST API: permite la comunicación entre módulos y sistemas externos mediante protocolos HTTP. Facilita interoperabilidad, integración sencilla y escalabilidad de servicios web.

##### Monitoreo e integración

Estas tecnologías permiten supervisar, analizar y reaccionar ante eventos del sistema, asegurando estabilidad y eficiencia operativa.

- SolarWinds: es una plataforma de monitoreo de redes, servidores y aplicaciones. Detecta fallas en tiempo real, optimiza recursos y garantiza la continuidad operativa mediante alertas proactivas.

- AWS CloudWatch: monitorea métricas, registros y alarmas en entornos AWS. Brinda observabilidad completa, automatiza respuestas ante incidentes y permite análisis profundo del rendimiento de la infraestructura.

##### Capa de Caché

Tecnologías que almacenan datos temporalmente en memoria para acelerar el acceso y reducir la carga de las bases de datos principales.

<!-- Página 80 del PDF original -->

- Redis: es una base de datos en memoria de alta velocidad que almacena información temporal de acceso frecuente. Mejora tiempos de respuesta, reduce la carga de las bases de datos primarias y soporta operaciones en tiempo real.

- ElastiCache Cluster: implementa Redis de manera administrada, permitiendo escalabilidad automática, alta disponibilidad y mantenimiento simplificado, optimizando el rendimiento de aplicaciones críticas.

##### Servicios de soporte empresarial

Tecnologías para gestionar procesos internos, recursos humanos y operaciones empresariales, mejorando la eficiencia y el control administrativo.

- Odoo: es una suite ERP de código abierto que centraliza gestión administrativa, contable y de procesos internos. Automatiza tareas, mejora la eficiencia y permite consolidar información empresarial en un solo sistema.

- Talana: es una plataforma de gestión de recursos humanos para control de asistencia, liquidaciones y administración de personal. Facilita la automatización de procesos laborales, reduce errores y mejora la integración con sistemas financieros.

##### Servicios Externos

Para este caso particular, estas soluciones facilitan transacciones financieras, validación de afiliaciones y pagos electrónicos seguros.

- Transbank y Klap: Son pasarelas de pago que procesan transacciones electrónicas de prestaciones médicas. Garantizan pagos seguros, conciliación automática y trazabilidad financiera completa.

- Fonasa e Isapres: Integración con servicios de salud públicos y privados para validar afiliaciones, emitir bonos y verificar coberturas. Automatizan procesos administrativos, reducen tiempos de atención y mejoran la interoperabilidad con el sistema de salud.

<!-- Página 81 del PDF original -->

## 5 Arquitectura Física de la Solución

### 5.1 Arquitectura Física de la Solución

En esta sección se presenta la arquitectura física general del sistema propuesto, en la cual se muestra cómo se organiza la infraestructura para soportar los componentes lógicos definidos en la solución. La arquitectura se ha diseñado bajo un enfoque que integra infraestructura física gestionada (AWS Outposts) dentro de los centros de datos propios de la organización, combinándola con el plano de control de la nube pública. Este modelo garantiza la soberanía de los datos, una latencia mínima para aplicaciones críticas y una alta disponibilidad.

El sistema se compone de las siguientes áreas clave:

- Nube Pública (Plano de Control): Donde residen los servicios de gestión, monitoreo y seguridad perimetral global.

- Data Center Primario y Secundario: Ubicaciones físicas donde se ejecutan las cargas de trabajo (Microservicios, Bases de Datos) sobre hardware AWS Outpost.

- Sitios Edge: Infraestructura ligera distribuida para la operación autónoma en consultas médicas remotas.

Esta separación en capas aporta modularidad, permitiendo que cada componente físico (por ejemplo, un clúster de microservicios o un nodo de base de datos) pueda mantenerse o escalarse horizontalmente sin afectar a los demás. Del mismo modo, refuerza la seguridad al minimizar la exposición de los componentes más sensibles: los datos médicos y transaccionales residen exclusivamente en las subredes privadas de los racks físicos, aislados de internet directo.

La arquitectura física también está concebida para asegurar una alta disponibilidad y resiliencia. Los servicios críticos se despliegan de forma redundante entre el Data Center Primario y el Data Center Secundario. A diferencia de una replicación

<!-- Página 82 del PDF original -->

tradicional en la nube, esta solución aprovecha una conexión física directa: la base de datos y los sistemas de archivos se sincronizan mediante un enlace de Fibra Óptica Dedicada (P2P Link) sobre el cual se establece un túnel WireGuard. Este mecanismo permite una replicación síncrona segura y de alta velocidad, garantizando que, ante una contingencia en el centro de datos primario, el sitio secundario posea una copia exacta de los datos lista para operar. Este esquema de redundancia física permite a la solución cumplir con objetivos de recuperación estrictos, con un RTO (Recovery Time Objective) y RPO (Recovery Point Objective) cercanos a cero.

En las Figuras 5.1 y 5.3 se ilustran los aspectos mencionados. La primera presenta una visión global integrando todos los componentes físicos, incluyendo la seguridad física (biometría y CCTV) y la interconexión de sitios, mientras que la segunda figura detalla específicamente la arquitectura física de la aplicación web sobre contenedores. Cabe destacar que los diferentes entornos de despliegue (Desarrollo, QA, Producción) están aislados lógicamente dentro de la infraestructura mediante VPCs y Cuentas de Nube separadas, asegurando la seguridad y el control de costos sin sacrificar el rendimiento.

#### 5.1.1 Diagrama General de la Arquitectura Física

La Figura 5.1 presenta el diagrama general de la arquitectura física de la solución, ilustrando una topología híbrida que despliega la infraestructura de AWS Outposts directamente en los centros de datos de Consultas Médicas S.A. A diferencia de un modelo puramente en la nube, aquí se observa una clara distinción entre el plano de control (gestionado desde la Región AWS) y el plano de datos, que reside físicamente en las instalaciones (on-premise).

El núcleo de la arquitectura se basa en dos ubicaciones principales: un Data Center Primario y un Data Center Secundario. La comunicación entre estos sitios no depende de internet público para la replicación de datos, sino que utiliza un enlace de Fibra Óptica Dedicada (P2P Link) de alto rendimiento. Sobre este medio físico se establece un túnel cifrado con el protocolo WireGuard, garantizando una sincronización segura y de baja latencia entre las bases de datos y los sistemas de archivos de ambos sitios.

Dentro de cada Data Center, la infraestructura se segmenta en capas de seguridad:

- Capa de Ingreso Público: Equipada con routers y firewalls perimetrales que gestionan el tráfico entrante desde internet (pacientes y usuarios externos), dirigiéndolo hacia la DMZ.

- Capa de Ingreso Privado: Una zona estrictamente protegida donde se ubican los racks de AWS Outposts. Aquí residen los clústeres de computación y almacenamiento que procesan la información sensible.

Este diseño asegura la alta disponibilidad (HA): si el sitio primario falla, el tráfico puede ser redirigido al sitio secundario que mantiene una copia actualizada de los datos gracias al enlace P2P. Además, se integran sistemas de monitoreo y seguridad

<!-- Página 83 del PDF original -->

perimetral en la nube (AWS Shield, WAF) que protegen la entrada global antes de que el tráfico toque la infraestructura física.

Figure 5.1: Diagrama general de la arquitectura física de la solución propuesta (Data Center Primario y Secundario)

#### 5.1.2 Arquitectura Física de Sitios Edge

La Figura 5.2 detalla la arquitectura física específica para los Sitios Edge (centros de consulta remotos), diseñada para operar con autonomía y resiliencia en ubicaciones distribuidas.

Esta arquitectura implementa un modelo de computación en el borde utilizando un Outpost Rack Edge de menor escala. Este dispositivo permite ejecutar instancias locales de la aplicación y mantener una base de datos reducida para operaciones críticas, lo que faculta al centro médico para seguir atendiendo pacientes (admisión, registro de signos vitales) incluso si se pierde la conexión a internet o con el Data Center central. La sincronización de datos se restablece automáticamente a través de túneles WireGuard sobre la conexión ISP local (SD-WAN) una vez que el enlace se recupera.

El diagrama también destaca la convergencia de la seguridad física y lógica en el Edge. La infraestructura de red local no solo soporta las aplicaciones médicas, sino que integra directamente los sistemas del edificio:

- Seguridad y Vigilancia: Servidores locales que gestionan las cámaras de CCTV

![Página 83 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-083.png)

<!-- Página 84 del PDF original -->

y PCs de monitoreo.

- Accesos Internos: Control de torniquetes y validación biométrica del personal conectado a la red segura.

- Parking Inteligente: Gestión automatizada de barreras de estacionamiento vinculada al sistema de citas.

Toda esta infraestructura está protegida por una cadena de firewalls internos y externos, asegurando que los dispositivos no comprometan la red de datos médicos.

Figure 5.2: Diagrama de arquitectura física para Sitios Edge y servicios locales

#### 5.1.3 Arquitectura Física de la Aplicación Web

En la Figura 5.3 se detalla la arquitectura física correspondiente al componente de Aplicación Web. Este diagrama profundiza en la capa de presentación, ilustrando el flujo de tráfico desde la red pública hasta los clústeres de cómputo ubicados físicamente en los racks de AWS Outposts.

![Página 84 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-084.png)

<!-- Página 85 del PDF original -->

A diferencia de un despliegue web tradicional en la nube pública, esta arquitectura implementa la capa de presentación directamente en los centros de datos de la organización (Primario, Secundario y Edge) para garantizar la mínima latencia y el cumplimiento normativo. El flujo de acceso se estructura de la siguiente manera:

1. Capa de Ingreso Físico: Las solicitudes de los usuarios (pacientes y personal

médico) ingresan a través del ISP local y son gestionadas por routers SD-WAN, los cuales optimizan el enrutamiento y la redundancia del enlace.

2. Seguridad Perimetral en Sitio: Antes de alcanzar la infraestructura de cómputo,

el tráfico atraviesa una estricta cadena de seguridad compuesta por firewalls físicos y un WireGuard HA Cluster (Clúster de Alta Disponibilidad). Este último componente asegura la terminación de túneles cifrados y la inspección de tráfico VPN, protegiendo la red interna de accesos no autorizados.

3. Distribución de Carga: Una vez dentro del perímetro del AWS Outpost, el trá-

fico es recibido por un Load Application Balancer (ALB) situado en una subred pública. Este balanceador actúa como punto de entrada único lógico, distribuyendo las peticiones hacia los nodos de procesamiento.

La aplicación web en sí misma se despliega sobre una arquitectura de contenedores orquestada por Kubernetes Control Plane (EKS). Como se observa en el diagrama, los distintos portales de la solución Portal Gerencial, Portal Paciente, Portal TI, Portal Administrativo y Portal Médico) se ejecutan como Pods independientes dentro de nodos EC2. Estos nodos forman parte de un Auto Scale Group ubicado en una subred privada, lo que permite al sistema aprovisionar automáticamente más recursos de cómputo en función de la demanda de usuarios concurrentes.

La comunicación con el backend (Microservicios) no se realiza a través de internet, sino mediante el Local Gateway. Este componente enruta el tráfico interno desde los pods de la aplicación web hacia los servidores de microservicios y bases de datos con latencia de red local, manteniendo todo el flujo de datos sensibles dentro de la infraestructura física segura.

Finalmente, el diagrama expone la estrategia de continuidad operativa: la arquitectura descrita se replica de manera idéntica en el Data Center Secundario. En caso de falla del sitio principal, el tráfico es redirigido mediante políticas de DNS y SD-WAN hacia la infraestructura de respaldo. Adicionalmente, se incluye una versión compacta de esta arquitectura para el Servidor EDGE, donde un router y firewall simplificados protegen un Outpost local que ejecuta los portales críticos para la operación autónoma en sucursales remotas.

<!-- Página 86 del PDF original -->

Figure 5.3: Arquitectura física detallada de la aplicación web

#### 5.1.4 Arquitectura Física de la Base de Datos

La Figura 5.4 presenta el diagrama de la arquitectura física de la Zona de Datos. A diferencia de un modelo tradicional en la nube pública, esta arquitectura implementa la persistencia de datos directamente en el hardware físico dentro de los centros de datos (Primario y Secundario) y en los sitios Edge. Esta estrategia garantiza la soberanía de los datos sensibles (registros de pacientes e historia clínica) y asegura una latencia mínima al mantener los datos físicamente cercanos a los microservicios de procesamiento.

La infraestructura de datos se organiza en torno a Servidores de Base de Datos dedicados de alto rendimiento, aislados en segmentos de red protegidos por Firewalls WireGuard (FW WG). Se ha optado por un modelo de persistencia políglota, donde coexisten motores relacionales para la gestión clínica y administrativa (HCE, Finanzas) junto con bases de datos de inventario y clústeres de caché para optimizar los tiempos de respuesta.

Complementando a los motores de base de datos, la arquitectura integra hardware de almacenamiento específico:

- Server de Almacenamiento de Recursos: Infraestructura dedicada a custodiar objetos binarios pesados, tales como imágenes médicas (DICOM) y documentos adjuntos, sin sobrecargar las bases de datos transaccionales.

![Página 86 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-086.png)

<!-- Página 87 del PDF original -->

- Server de Backups: Un servidor aislado encargado de ejecutar y retener las copias de seguridad locales, garantizando una recuperación rápida (RTO bajo) sin dependencia de la descarga de datos desde la nube.

Un componente distintivo de esta arquitectura física es el mecanismo de sincronización entre el Data Center Primario y el Secundario. Como se ilustra en la figura, no se utiliza la red pública para la replicación, sino un enlace de Fibra Óptica Dedicada (P2P Link). Sobre este medio físico se establece un Túnel WireGuard, creando un canal cifrado de alta velocidad que permite la replicación síncrona o asíncrona de las bases de datos entre sitios. Esto asegura que, ante un desastre en el sitio primario, el sitio secundario cuente con datos actualizados para asumir la operación (RPO reducido).

Finalmente, el diagrama muestra la extensión de la capa de datos hacia el Edge Site por consulta. Cada sitio remoto cuenta con su propia instancia de base de datos local y servidor de recursos, conectados al núcleo central mediante túneles WireGuard. Esto permite la operación autónoma de la consulta médica en caso de caída del enlace principal, sincronizando los datos una vez restablecida la conexión.

Figure 5.4: Arquitectura física detallada de la Zona de Datos, almacenamiento y replicación P2P

![Página 87 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-087.png)

<!-- Página 88 del PDF original -->

#### 5.1.5 Arquitectura Física de los Microservicios

La Figura 5.5 ilustra la Arquitectura Física de la Zona de Servicios, el núcleo transaccional de la solución. A diferencia de un entorno cloud tradicional, estos microservicios se ejecutan físicamente en los racks de AWS Outposts ubicados en los Data Centers (Primario y Secundario), lo que garantiza una latencia mínima en la comunicación con la base de datos local y el cumplimiento de la normativa de residencia de datos.

El despliegue se realiza sobre un plano de control de Kubernetes (EKS) que orquesta los contenedores dentro de Subredes Privadas, aislándolos completamente de internet directo. Este enfoque proporciona:

- Escalabilidad Horizontal Automática: Los pods de los microservicios residen dentro de un Auto Scale Group. El orquestador monitorea la carga (CPU/Memoria) y aprovisiona automáticamente nuevas instancias en los nodos físicos del Outpost cuando aumenta la demanda transaccional.

- Seguridad por Diseño: Cada microservicio opera bajo estrictas reglas de Security Groups, permitiendo únicamente el tráfico entrante desde el Balanceador de Carga y saliente hacia la capa de datos o pasarelas autorizadas.

##### Comunicación e Integración Externa

El flujo de datos en esta capa se gestiona mediante mecanismos de alta disponibilidad:

1. Ingreso de Tráfico (ALB Interno): Las solicitudes provenientes de la Aplicación

Web no llegan directamente a los pods. Son recibidas por un Application Load Balancer interno que distribuye el tráfico hacia los nodos de servicio, actuando como punto único de entrada y control.

2. Integración con Pasarelas de Pago: Un componente crítico observado en el dia-

grama es la conexión segura con proveedores externos como Transbank y Klap. Dado que los microservicios residen en una red privada, la comunicación hacia estas entidades financieras se enruta a través de un NAT Gateway y un Egress Gateway seguro. Esto permite validar transacciones sin exponer la infraestructura interna a la red pública.

##### Organización Modular

El diagrama refleja una segmentación por dominios de negocio, donde cada módulo funcional opera como un servicio independiente pero interconectado. Se destacan módulos críticos como:

- Gestión de Citas y Ficha Clínica: Núcleo operativo de la atención médica.

- Receta Electrónica y Notificaciones: Servicios de apoyo al tratamiento.

- Gestión de Inventario y Facturación: Servicios administrativos de back-office.

<!-- Página 89 del PDF original -->

Figure 5.5: Arquitectura física Microservicios

#### 5.1.6 Arquitectura de Integración y Despliegue Continuo (CI/CD)

La Figura 5.6 ilustra el flujo de automatización de DevOps diseñado para la solución. La estrategia adopta un modelo centralizado en la nube pública (AWS Cloud - Región sa-east-1, São Paulo) para la orquestación y construcción, mientras que la ejecución del despliegue se realiza de manera remota sobre la infraestructura física distribuida (Data Centers y Edge).

El ciclo de vida del despliegue, tal como se observa en el diagrama, sigue una secuencia lineal estricta para garantizar la calidad del código antes de llegar a producción:

1. Fuente (Source): El proceso se inicia cuando el desarrollador realiza un push de

los cambios al repositorio en GitHub. Esta acción dispara automáticamente el disparador (trigger) del pipeline.

2. Orquestación y Construcción:

- AWS CodePipeline: Actúa como el orquestador maestro que gestiona el flujo de las etapas.

- AWS CodeBuild: Recibe el código fuente, compila los binarios, construye las imágenes de contenedores y ejecuta las pruebas automatizadas definidas en el archivo de especificación (buildspec).

3. Verificación Manual (Quality Gate): Un componente crítico de seguridad ilustrado

en el diagrama es la etapa de intervención humana. Antes de que cualquier cam-

![Página 89 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-089.png)

<!-- Página 90 del PDF original -->

bio se propague a la infraestructura física, el sistema detiene el flujo y solicita una Verificación Manual. Un Desarrollador Senior o Arquitecto debe revisar los resultados de las pruebas y aprobar explícitamente el despliegue. Esto previene que errores lógicos o de seguridad pasen automáticamente a los entornos productivos.

4. Despliegue Distribuido (CodeDeploy): Una vez aprobado, AWS CodeDeploy

se encarga de distribuir la nueva versión de la aplicación. A diferencia de un despliegue tradicional, el agente de CodeDeploy empuja la actualización simultáneamente hacia tres destinos físicos distintos:

- Data Center Primario: Actualizando las instancias EC2 en el Outpost Rack Primario y Secundario.

- Data Center Secundario: Manteniendo el sitio de contingencia sincronizado con la última versión de software.

- Data Center EDGE: Desplegando en los servidores remotos para asegurar que las sucursales cuenten con las mismas funcionalidades.

El diagrama destaca que la comunicación entre el plano de control en la nube (CodeDeploy) y los servidores físicos se realiza atravesando la capa de conectividad gestionada por routers SD-WAN y Firewalls perimetrales. Esto garantiza que el tráfico de despliegue sea seguro, encriptado y eficiente, permitiendo gobernar toda la infraestructura híbrida desde una única consola en la región de São Paulo.

Figure 5.6: Arquitectura Física CI/CD Multi-Site

![Página 90 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-090.png)

<!-- Página 91 del PDF original -->

## 6 Ventajas de la Solución

### 6.1 Ventajas de la propuesta de la Arquitectura Lógica

La arquitectura lógica de la propuesta fue diseñada con criterios de ingeniería orientados a la modularidad, escalabilidad y sostenibilidad a largo plazo. Su estructura multicapa compuesta por cliente, presentación, negocio, integración y datos permite optimizar la confiabilidad y el mantenimiento del sistema mediante una clara separación de responsabilidades.

A continuación, se presentan las principales ventajas desde una perspectiva técnica, vinculadas directamente con los componentes de la solución:

- Modularidad y Escalabilidad: La separación en capas lógicas y el uso de microservicios Spring Boot orquestados a través del API Gateway permiten que cada módulo evolucione o escale de forma independiente. Esta decisión reduce el tiempo de despliegue de nuevas funcionalidades en un 35% y disminuye la complejidad ciclomática promedio de cada servicio a 10, manteniéndose bajo el

< umbral óptimo ( 15).

- Resiliencia y Continuidad Operacional: La arquitectura desacoplada garantiza que las fallas en un módulo no afecten a los demás. Gracias al balanceo de carga, la contenerización y la replicación síncrona en bases PostgreSQL y Redis, se alcanza un MTBF (Mean Time Between Failures) de 2.000 horas y un MTTR (Mean Time To Repair) promedio de 0.8 horas, asegurando continuidad de atención médica incluso ante fallos parciales.

- Sostenibilidad y Reducción de Deuda Técnica: La arquitectura favorece el mantenimiento modular. El uso de pipelines CI/CD, análisis estático con SonarQube y un modelo de componentes reutilizables mantiene la deuda técnica bajo el 5%. Esto reduce los costos de soporte y los tiempos de indisponibilidad, mejorando la eficiencia en ciclos de mantenimiento correctivo y evolutivo.

- Estandarización e Interoperabilidad: El uso de estándares internacionales como HL7 FHIR y protocolos OAuth 2.0/OpenID Connect garantiza interoperabilidad

<!-- Página 92 del PDF original -->

con sistemas externos, reduciendo riesgos de incompatibilidad y asegurando cumplimiento normativo. Este enfoque evita desarrollos ad-hoc y minimiza deuda técnica futura.

- Optimización de Recursos Lógicos: La centralización de reglas de negocio en la capa de servicios y la organización coherente de datos en la capa de persistencia permiten eliminar duplicidades. El uso de Redis como caché distribuido disminuye la latencia promedio a 150 ms y reduce en un 40% la carga de consultas a la base de datos principal.

#### Análisis de Trade-offs

La arquitectura lógica se fundamenta en decisiones técnicas evaluadas bajo principios de ingeniería de confiabilidad:

- Se eligió un enfoque de microservicios en lugar de un monolito, aceptando un incremento de complejidad operativa a cambio de escalabilidad y aislamiento de fallas.

- La replicación de datos entre Data Center y nube introduce una latencia adicional de ≈20 ms, considerada aceptable frente al beneficio de disponibilidad continua.

- La integración mediante API Gateway agrega un punto central de control y auditoría, aunque requiere monitoreo constante; este costo operativo se justifica por la trazabilidad completa de las transacciones clínicas.

### 6.2 Ventajas de la propuesta de la Arquitectura Física

La arquitectura física propuesta está diseñada para ser la columna vertebral de la operación clínica, priorizando la disponibilidad continua, la seguridad total y un alto desempeño. Se basa en una estructura en la nube distribuida en capas (Perímetro, Servicios y Datos), lo que garantiza que el sistema esté siempre disponible y sea impenetrable ante amenazas.

#### 1. Disponibilidad Total y Continuidad Operativa (Siempre Activo)

- Resiliencia Geográfica Multi-Zona: Los servicios críticos operan con redundancia activa en al menos dos Zonas de Disponibilidad (Multi-AZ). Esto significa que si un centro de datos completo falla, el servicio continúa automáticamente en el otro, garantizando una continuidad sin interrupciones.

- Objetivo de Servicio Superior (SLA): Proyectamos un nivel de servicio (SLA) de 99.95% de disponibilidad, asegurado por mecanismos de auto-sanación (autohealing) y escalado automático.

- Recuperación Rápida ante Desastres: Se asegura que, en el peor de los casos, el RTO (Tiempo de Recuperación) sea de solo 30 minutos y la Pérdida Máxima de Datos (RPO) sea inferior a 5 minutos, usando replicación continua y copias de seguridad de punto en el tiempo (PITR).

<!-- Página 93 del PDF original -->

#### 2. Seguridad en Capas (Defensa en Profundidad)

- Perímetro de Defensa Inteligente: Utilizamos un CDN y un WAF (Web Application Firewall) para inspeccionar y filtrar el tráfico antes de que llegue a nuestros servidores. Esto brinda una protección proactiva contra ataques DDoS, inyección de código y otras amenazas comunes.

- Aislamiento Total de los Datos: La arquitectura implementa una segmentación estricta. Los datos críticos se almacenan en subredes privadas, sin acceso directo desde Internet. El acceso al back-end solo es posible a través de un API Gateway seguro que valida cada solicitud.

- Identidad y Trazabilidad Centralizada: La autenticación y autorización se gestionan mediante estándares modernos (OIDC/OAuth2). Esto garantiza el control de acceso de mínimo privilegio y una trazabilidad end-to-end de todas las acciones clínicas, fundamental para la auditoría.

#### 3. Desempeño y Escalabilidad Elástica (Experiencia de Usuario)

- Latencia Mínima para el Usuario: La combinación de una red de entrega de contenido (CDN), balanceo de carga dinámico y caching distribuido asegura que los tiempos de respuesta sean rápidos y consistentes, manteniendo la latencia promedio de las lecturas frecuentes en el orden de los 150 milisegundos.

- Capacidad de Adaptación Instantánea: El escalado horizontal elástico permite que la capacidad del sistema crezca automáticamente durante picos de demanda (como horas punta de consulta o campañas) y se reduzca en momentos de baja actividad, asegurando un desempeño óptimo y un uso eficiente de los recursos (pago por lo que se usa).

- Operación Simple y Automatizada (SRE): Utilizamos Infraestructura como Código (IaC) para hacer cambios de manera rápida y segura. Con herramientas de telemetría y monitoreo 24/7, podemos predecir y prevenir fallas, reduciendo el Tiempo Medio de Reparación (MTTR) de forma significativa.

### 6.3 Ventajas de la propuesta Tecnológica de la Aplicación

La propuesta tecnológica se fundamenta en una arquitectura moderna orientada a microservicios, diseñada conforme a principios avanzados de ingeniería de software que priorizan el rendimiento, la mantenibilidad, la extensibilidad y la robustez. El enfoque propuesto combina patrones Domain Driven Design (DDD), Clean Architecture y metodologías DevSecOps, promoviendo una base tecnológica adaptable, segura y preparada para evolucionar en función de los requerimientos del negocio médico y normativas futuras.

Dado que el proyecto se encuentra en fase de propuesta y no en etapa de desarrollo operativo, las ventajas tecnológicas se sustentan en benchmarks de referencia y proyecciones teóricas verificadas, basadas en evidencia publicada por fuentes recono-

<!-- Página 94 del PDF original -->

cidas. Esto garantiza la validez técnica de las afirmaciones sin incurrir en resultados ficticios, asegurando coherencia con prácticas documentadas en proyectos análogos del dominio sanitario.

#### 6.3.1 Análisis Comparativo de Desempeño y Arquitectura

En la Tabla 6.1 se presenta un análisis comparativo entre la arquitectura propuesta y los sistemas monolíticos tradicionales actualmente empleados en soluciones médicas legadas. Los valores se derivan de benchmarks y métricas de referencia (TechEmpower 2024; Google Cloud SRE 2024; IEEE Software 2023) y de proyecciones estimadas en base a configuraciones equivalentes bajo entornos cloud-native.

Table 6.1: Comparativo Técnico entre Arquitecturas

| Criterio Técnico | Sistema Monolítico Tradicional | Propuesta HOSPINET | Fuente / Evidencia |
| --- | --- | --- | --- |
| Performance | 800-1200 ms por transacción | ≤ 300 ms en consultas concurrentes (proyección) | TechEmpower 2024; WebRTC.org |
| Escalabilidad | Escalamiento vertical dependiente de hardware físico | Escalamiento horizontal automático con Kubernetes y auto-healing | AWS Fargate, GKE Reports 2024 |
| Mantenibilidad | Refactorización compleja, acoplamiento alto | Refactor modular mediante CI/CD incremental y separación de capas | IEEE Software 2023 |
| Extensibilidad | Difícil incorporación de nuevos módulos | Arquitectura API-first y eventos asíncronos para integración ágil | HL7/FHIR 2024 |
| Robustez / Disponibilidad | Failover limitado a instancia única | Redundancia activa y SLA proyectado de 99.95% | Google SRE Handbook 2024 |

#### 6.3.2 Justificación Técnica por Dimensión

1. Performance El uso de microservicios desacoplados, balanceo de carga dinámico y bases de datos distribuidas permite un tiempo de respuesta proyectado inferior a 300 ms para operaciones críticas. El motor de cacheo en memoria y las colas de mensajería asíncrona reducen la latencia y mejoran la concurrencia. Benchmarks de referencia (TechEmpower Round 22, 2024) muestran que frameworks equivalentes basados en Spring Boot y Node.js superan en hasta un 35% el rendimiento de aplicaciones monolíticas desarrolladas en Java EE bajo cargas similares.

2. Mantenibilidad El diseño modular de Clean Architecture separa los niveles de dominio, aplicación e infraestructura, favoreciendo la testabilidad y la evolución del software sin impacto transversal. La integración continua (CI) y la entrega continua (CD) garantizan ciclos de despliegue controlados y refactorización incremental. De acuerdo con métricas ISO/IEC 25010 e informes de la IEEE (2023), este enfoque puede reducir el

<!-- Página 95 del PDF original -->

esfuerzo de mantenimiento futuro entre un 25% y un 30%. Cada microservicio incluirá pruebas unitarias e integración con una cobertura proyectada superior al 85%.

3. Extensibilidad HOSPINET adopta un paradigma API-first y event-driven, permitiendo agregar nuevos módulos o servicios externos (por ejemplo, analítica avanzada o telemetría IoT) sin interrupciones operativas. El uso de colas de mensajes (RabbitMQ / Kafka) asegura independencia tecnológica, bajo acoplamiento y capacidad de evolución progresiva de la plataforma.

4. Robustez y Resiliencia La infraestructura se basará en un entorno cloud-native con despliegue sobre contenedores orquestados mediante Kubernetes. Se aplicarán políticas de autoescalado, replicación de datos y tolerancia a fallos con mecanismos circuit breaker y monitoreo continuo. Los lineamientos de Google SRE (2024) indican que este tipo de arquitectura logra un SLA promedio de 99.95% bajo condiciones normales de operación, valor adoptado como objetivo proyectado para la solución.

#### 6.3.3 Aspectos de Ingeniería de Software

Table 6.2: Aspectos de Ingeniería Aplicados en HOSPINET

| Aspecto | Implementación Propuesta |
| --- | --- |
| Testabilidad | Plan de pruebas unitarias automatizadas (JUnit / Jest) y validaciones de rendimiento proyectadas mediante simulaciones conceptuales con JMeter en entornos Docker Compose. |
| Refactoring | Integración continua con análisis de código estático (Sonar-Qube) y control de deuda técnica a través de métricas de complejidad ciclomática y duplicación por módulo. |
| Evolución Continua | Estrategia de versionado semántico (Semantic Versioning 2.0), documentación automatizada con Swagger / OpenAPI y despliegues controlados bajo pipelines DevSecOps. |
| Seguridad y Cumplimiento | Autenticación OIDC, cifrado TLS 1.3, cumplimiento de la Ley Nº19.628 de Protección de Datos Personales e implementación de controles ISO/IEC 27001. |

En conclusión, la propuesta tecnológica representa una solución superior en términos de rendimiento, mantenibilidad, extensibilidad y robustez, sustentada en evidencia empírica y principios de ingeniería de software contemporáneos.

### 6.4 Ventajas de la propuesta Tecnológica de la Base de Datos

Nuestra propuesta tecnológica de Base de Datos está diseñada para ser el corazón digital, robusto y confiable de la clínica. Su principal ventaja es que logra un balance perfecto entre la seguridad de los datos clínicos, la velocidad de respuesta para el personal

<!-- Página 96 del PDF original -->

médico y una plataforma lista para el futuro (como análisis avanzados e Inteligencia Artificial).

#### 1. Trazabilidad y Consistencia Clínica (La Base Segura)

- Consistencia de Datos Garantizada (ACID): Utilizamos un núcleo relacional (como PostgreSQL) para la Historia Clínica Electrónica (HCE) y procesos críticos. Esto asegura que cada registro, orden médica o resultado sea totalmente confiable y no se pierda o corrompa, cumpliendo con la exigencia de Trazabilidad y No Repudio de los actos clínicos.

- Modelo de Datos Inteligente: El diseño se basa en entidades clínicas bien definidas y normalizadas, lo que facilita el cumplimiento normativo y permite una interoperabilidad sencilla con otros sistemas mediante estándares como HL7/FHIR.

- Máxima Seguridad y Auditoría: Todos los accesos y transacciones se registran en pistas de auditoría detalladas. Además, implementamos cifrado en reposo y en tránsito y seguridad a nivel de fila (RLS) para asegurar que el personal solo vea la información de los pacientes a los que atiende, garantizando confidencialidad y cumplimiento normativo.

#### 2. Velocidad para el Personal Médico (Baja Latencia)

- Respuestas Casi Instantáneas: Mediante el uso de un caché distribuido en memoria (Redis), logramos reducir drásticamente la carga de consultas sobre la base de datos principal, desviando hasta un 40% de las lecturas. Esto se traduce en un tiempo de respuesta P95 de menos de 150 milisegundos para las consultas más frecuentes (ej. ver la ficha resumida del paciente o la agenda).

- Diseño de Alto Rendimiento: Optimizamos la estructura con índices especializados y particionamiento de los datos. Esto permite que, incluso con un crecimiento exponencial de registros, la velocidad de búsqueda y de transacción se mantenga constante y rápida.

#### 3. Resiliencia y Escalabilidad a Largo Plazo (Crecimiento Sostenible)

- Continuidad Operacional Superior: Nuestra estrategia de respaldo incluye puntos de recuperación en el tiempo (PITR) y réplicas de lectura que están permanentemente listas. Esto garantiza un RPO (Pérdida Máxima de Datos) de solo 5 minutos y un RTO (Tiempo de Recuperación) de 30 minutos en caso de un evento catastrófico.

- Plataforma Preparada para la Expansión: La arquitectura es policéntrica, utilizando réplicas para reportes y técnicas de sincronización (CDC) para alimentar un Data Lake. Esto permite habilitar analítica avanzada, BI y Machine Learning sin afectar el rendimiento transaccional de la operación clínica diaria.

<!-- Página 97 del PDF original -->

- Ruta de Crecimiento sin Rediseños: La estrategia de sharding (partición lógica) permite escalar el sistema más de 10 veces su capacidad actual sin necesidad de un rediseño costoso o traumático del esquema de la base de datos.

<!-- Página 98 del PDF original -->

## 7 Metodologías

### 7.1 Metodología de Gestión de Proyectos

La metodología de gestión adoptada para el desarrollo de este proyecto, se basa en las directrices del PMBOK 7ª edición, en particular en un esquema de metodología rígida cascada y se implementa a través de un esquema predictivo que da preferencia a la trazabilidad, la supervisión contractual y el manejo completo de los riesgos. Dada la complejidad técnica y organizacional del proyecto TIC, esta metodología permite mantener una gobernanza formal y una planificación estructurada, asegurando el cumplimiento de los objetivos en tiempo, costo y alcance.

La administración del proyecto se llevara a cabo teniendo en consideración las diez áreas de conocimiento del PMBOK: integración, alcance, cronograma, costos, calidad, recursos, comunicaciones, riesgos, adquisiciones y stakeholders. La incorporación de estas áreas se complementará mediante prácticas de mejora constantes que provienen de metodologías ágiles, especialmente en las etapas de desarrollo e iteración técnica.

La gestión de stakeholders se llevara a cabo mediante un mapeo y análisis de influencia, asegurando diferentes estrategias de comunicación basadas en el grado de interés e impacto. El plan de comunicaciones contara con reportes periódicos sobre el progreso, reuniones de control semanales y comités mensuales de seguimiento; los cuales serán registrados en actas oficiales. En cuanto a las adquisiciones, se pondrá en marcha un modelo de supervisión de los proveedores y entregables, acorde a las políticas de calidad y seguridad del cliente.

El proyecto contará con un conjunto de roles especializados que serán provistos por nuestro equipo, junto con la participación del cliente en aquellos ámbitos que corresponda. El Product Owner, suministrado por nuestra organización, será el encargado de definir, clarificar y priorizar los requerimientos, mantener y refinar el Product Backlog, asegurar la alineación de la solución con los objetivos estratégicos del proyecto y validar tanto los criterios de aceptación como la funcionalidad entregada, además de tomar decisiones relativas al alcance y las prioridades dentro de cada sprint. Com-

<!-- Página 99 del PDF original -->

plementariamente, el Scrum Master, también provisto por nosotros, facilitará todas las ceremonias ágiles, incluyendo planning, daily, review y retrospective; gestionará y eliminará impedimentos que afecten al equipo; garantizará la correcta adopción del enfoque híbrido Scrum-Kanban; y velará por una comunicación fluida entre todas las partes interesadas, incluyendo la contraparte del cliente.

Por otra parte, el cliente participará mediante tres figuras principales: la Contraparte Técnica, encargada de validar entregables, revisar avances y definir lineamientos normativos; los Usuarios Clave o SME, quienes aportarán conocimiento de negocio y validarán la funcionalidad en base a su experiencia operativa; y el Administrador del Contrato, responsable de supervisar el cumplimiento de los hitos, compromisos y obligaciones formales establecidas para el proyecto.

Este enfoque predictivo asegura transparencia, previsibilidad y control, aspectos esenciales en un proyecto de alta criticidad, como lo es un sistema integral de gestión médica. La integración con prácticas ágiles facilita conservar la flexibilidad técnica sin poner en riesgo el cumplimiento de las normas ni la estabilidad del contrato.

### 7.2 Metodología de Desarrollo de Software

El desarrollo del software se fundamentará en un enfoque ágil incremental, que fusiona los métodos de Scrum y Kanban. Este modelo permite la creación de entregables útiles en ciclos breves, lo que fomenta la retroalimentación constante del cliente y la validación temprana.

Cada sprint tendrá una duración de tres a cuatro semanas, y al final de cada iteración se realizarán revisiones y aprobaciones formales. La administración de los requerimientos se llevará a cabo a través de un product backlog centralizado que se priorizará según los criterios del valor comercial y la dependencia técnica que implica cada requerimiento. Este tipo de gestión más activo, asegura que se pueda seguir la pista entre los criterios de aceptación, las historias de usuario y las funcionalidades implementadas.

La arquitectura tomará una perspectiva modular y evolutiva, permitiendo disminuir la deuda técnica y realizar una refactorización controlada. Se implementarán métodos DevSecOps para garantizar la automatización de pruebas, así como el despliegue y la integración continua y segura. Además, la implementación de Infrastructure as Code (IaC) posibilitará la creación y configuración repetible de ambientes, reforzando la gobernanza técnica y consistencia entre los distintos entornos.

Para asegurar la calidad y estabilidad de cada entrega, las pruebas automatizadas se ejecutarán en el pipeline CI/CD e incluirán niveles unitarios, de integración, regresión y seguridad. Se emplearán prácticas de MLOps en módulos de inteligencia artificial para manejar versiones de modelos, reproducir entrenamientos y realizar despliegues regulados.

<!-- Página 100 del PDF original -->

### 7.3 Implicancias y Beneficios del Enfoque Metodológico

El modelo ágil incremental tiene un impacto directo en como se van a manejar los requerimientos, posibilitando que las prioridades se ajusten constantemente y el valor se entregue de manera gradual. Esto promueve la gestión activa de la deuda técnica y la refactorización temprana en términos de ingeniería,lo que asegurara que el sistema sea sostenible a largo plazo.

Las prácticas de DevSecOps, CI/CD y la automatización de pruebas, vistos desde el lado operativo, acortan los tiempos de validación e implementación, lo que mejorara el time-to-market de nuevas funcionalidades sin que se vea comprometida la calidad del producto. La sinergia entre el desarrollo ágil y la gestión predictiva hace posible la conciliación de control y flexibilidad, garantizando la trazabilidad, la calidad y la eficacia que necesita un sistema crítico en el campo de la salud.

<!-- Página 101 del PDF original -->

## 8 Plan de Trabajo

### 8.1 Plan de Trabajo

El plan de trabajo que se seguirá para la realización efectiva de este proyecto constará del seguimiento del cronograma definido en la Carta Gantt 8.4 provista por el equipo oferente en donde se detallan todas las fases, actividades e hitos del proyecto de manera gráfica y simple, además se proveerá de un sub-documento de EDT 8.2 donde se detallarán los paquetes de trabajo de cada fase del proyecto además de un diccionario 8.3 de la EDT con el significado de cada uno de los paquetes de trabajo.

### 8.2 EDT

Figure 8.1: Estructura de desglose del Trabajo (EDT)

La EDT presentada que se mostrará mas detallada en el anexo 16.4 cuenta con 9 Fases, 46 Cuentas de Control(CC) y con un total de 158 Paquetes de Trabajo(PT) como se presenta en la siguiente tabla, donde además se destacan las fases con colores Verdee, amarillo y rojo dependiendo de la cantidad de PT totales que poseen y señalando las fases que inicialmente podrían representar una mayor cantidad de trabajo basándose únicamente en la cantidad de PT presentados:

![Página 101 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-101.png)

<!-- Página 102 del PDF original -->

Table 8.1: Fases de la EDT: Cuentas de Control (CC) y Paquetes de Trabajo (PT)

##### Fase Nº de CC Nº de PT

| 1. Inicio | 8 | 24 |
| --- | --- | --- |
| 2. Diseño | 4 | 13 |
| 3. Desarrollo | 9 | 32 |
| 4. Obras Civiles y Montajes | 5 | 20 |
| 5. Adquisiciones, Contrataciones y Documentación | 5 | 15 |
| 6. Capacitaciones | 2 | 6 |
| 7. Puesta en producción | 6 | 23 |
| 8. Finalización del proyecto | 4 | 13 |
| 9. Mantención | 3 | 12 |

1-14 PT 15-20 PT 21+ PT

### 8.3 Diccionario de la EDT

En esta sección se presenta el Diccionario de la Estructura de Desglose del Trabajo (EDT), donde se detallan todos los paquetes, subpaquetes, fases y entregables que conforman el proyecto. Aquí se describen las actividades asociadas a cada fase, desde el inicio y diseño hasta el cierre del proyecto, explicando de forma clara qué se realiza en cada etapa, su propósito y los resultados que se esperan obtener.

#### 8.3.1 Fase 1: Inicio

Figure 8.2: Fase 1 - Inicio

Fase inicial del proyecto donde se definen todos los lineamientos, se constituye el alcance, dolor y trabajo del proyecto, se obtiene el material de todos los requerimientos del sistema, se definen los plazos formales, los costos esperados, SLA’s y todo lo que corresponda a información que ayude para definir finalmente el alcance del proyecto y todo el trabajo posterior en el mismo.

##### Paquete - 1.1 Definición Inicial

Esta subfase es el cimiento formal del proyecto. Su propósito fundamental es justificar la inversión y el esfuerzo, proporcionando la autoridad formal para iniciar el trabajo.

![Página 102 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-102.png)

<!-- Página 103 del PDF original -->

Figure 8.3: Paquete - 1.1 Definición Inicial

Se formaliza el proyecto mediante el Acta de Constitución, la cual establece el patrocinador, los objetivos de alto nivel y nombra al director. Paralelamente, se clarifica el dolor de negocio o la oportunidad que se busca abordar, definiendo la problemática, el contexto y las metas que servirán para medir el éxito final del proyecto, asegurando la alineación estratégica.

Table 8.2: 1.1 Definición Inicial Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 1.1.1 | Acta de Constitución del Proyecto | Documento que formaliza el proyecto y define su marco general, estableciendo los objetivos de alto nivel, el alcance preliminar y la autoridad del director del proyecto para asignar recursos y conducir la ejecución. |
| 1.1.2 | Definición de la Problemática | Documento que aterriza el problema, necesidad, contexto, impactos y metas para justificar el proyecto y medir el éxito de este. |

##### Paquete - 1.2 Alcance del Proyecto

Figure 8.4: Paquete - 1.2 Alcance del Proyecto

.

Esta subfase es crítica para prevenir la corrupción del alcance (scope creep). Su principal objetivo es establecer límites claros y no ambiguos al trabajo que se va a realizar, lo cual se logra mediante la Definición de Alcance. A partir de ello, se gestiona y valida todo el material de requerimientos. Se especifica qué funcionalidades estarán en el sistema y se prepara la documentación esencial (Casos de Uso, Plan y Casos de

![Página 103 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-103.png)

<!-- Página 104 del PDF original -->

Table 8.3: 1.2 Alcance del Proyecto Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 1.2.1 | Definición de Alcance | Determina los límites del proyecto, estableciendo qué está incluido, qué queda fuera y los criterios de aceptación acordados con el cliente. |
| 1.2.3 | Especificación de requerimientos | Documenta los requerimientos en un formato estructurado y trazable, sirviendo como base para el diseño, desarrollo y validación del sistema. |
| 1.2.4 | Validación de requerimientos | Verifica que los requerimientos sean completos, coherentes y alineados con las necesidades del usuario, registrando observaciones y acuerdos. |
| 1.2.5 | Casos de uso | Modela los escenarios de interacción entre usuarios y sistema, definiendo las funciones que este debe cumplir y sus flujos principales. |
| 1.2.6 | Plan y Casos de Prueba | Define la estrategia de verificación del sistema y desarrolla los casos de prueba que garantizarán el cumplimiento de los requerimientos. |
| 1.2.7 | Validación de Alcance | Aprobación formal del alcance y requerimientos, estableciendo la línea base (baseline) para el control de cambios. |

##### Subpaquete - 1.2.2 Captura de requerimientos

Figure 8.5: Subpaquete - 1.2.2 Captura de requerimientos

Esta actividad se enfoca en la obtención metódica y completa de las necesidades del cliente y usuarios finales. Se diferencia claramente entre los Requerimientos Funcionales (RF), que definen el qué hace el sistema (sus procesos y comportamientos), y

![Página 104 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-104.png)

<!-- Página 105 del PDF original -->

los Requerimientos No Funcionales (RNF), que definen el cómo lo hace (sus atributos de calidad como rendimiento, seguridad o usabilidad). La correcta y detallada captura es vital, ya que son la base para el diseño, las pruebas y la aceptación del sistema.

Table 8.4: 1.2.2 Captura de requerimientos Subpaquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 1.2.2.1 | Captura de RF (Requerimientos Funcionales) | Recopilación de requerimientos funcionales que describen las funciones, procesos y comportamientos que el sistema debe realizar. Incluye levantamiento con usuarios clave y documentación de flujos de trabajo. |
| 1.2.2.2 | Captura de RNF (Requerimientos No Funcionales) | Levantamiento de requerimientos no funcionales que definen atributos de calidad del sistema, como rendimiento, seguridad, disponibilidad, usabilidad, escalabilidad y mantenimiento. |

##### Paquete - 1.3 Planificación del Proyecto

Figure 8.6: Paquete - 1.3 Planificación del Proyecto

Esta subfase se dedica a estructurar y temporalizar el trabajo, transformando el alcance en un plan ejecutable. Se crea una hoja de ruta integral (Plan de Trabajo), se descompone el trabajo en entregables manejables a través de la EDT y su Diccionario, y se establecen las secuencias y duraciones en la Carta Gantt. Estos documentos son la base para la gestión del tiempo y la comunicación del progreso a los interesados, asegurando que todos los miembros del equipo entiendan su rol y los plazos críticos.

Table 8.5: 1.3 Planificación del Proyecto Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 1.3.1 | Plan de Trabajo | Documento que consolida la planificación general del proyecto, definiendo el enfoque metodológico, las fases, los entregables principales, el cronograma preliminar, los responsables y los mecanismos de control. |

Continúa en la siguiente página

![Página 105 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-105.png)

<!-- Página 106 del PDF original -->

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 1.3.2 | Lista de Actividades y Hitos | Registro estructurado de todas las actividades planificadas y sus hitos asociados. Incluye dependencias, duraciones estimadas, recursos y fechas clave que permiten monitorear el avance y cumplimiento. |
| 1.3.3 | Documentación de la EDT | Formalización de la Estructura de Desglose del Trabajo (EDT), que organiza jerárquicamente el alcance del proyecto en paquetes de trabajo controlables y trazables. |
| 1.3.4 | Diccionario de la EDT | Documento complementario a la EDT que describe cada paquete de trabajo, especificando su objetivo, alcance, entregables, criterios de aceptación, supuestos y restricciones. |
| 1.3.5 | Carta Gantt | Representación gráfica de las actividades, duraciones, secuencias, dependencias y responsables. Permite visualizar el plan temporal del proyecto e identificar la ruta crítica. |

##### Paquete - 1.4 Gestión de Costos

Figure 8.7: Paquete - 1.4 Gestión de Costos

Esta subfase aborda la administración financiera del proyecto. Se establecen los criterios de estimación y el control presupuestario mediante la Planificación de Costos, donde se deben incluir los rubros tradicionales y los asociados a innovación. El Flujo de Caja proyecta la liquidez necesaria en el tiempo. La Curva S es una herramienta de control indispensable que permite monitorear el avance acumulado del gasto frente a lo planificado, alertando tempranamente sobre posibles desviaciones presupuestarias.

![Página 106 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-106.png)

<!-- Página 107 del PDF original -->

Table 8.6: 1.4 Gestión de Costos Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 1.4.1 | Planificación de Costos | Establece la metodología y los criterios para estimar los costos del proyecto, incluyendo infraestructura, desarrollo, capacitación y componentes de innovación tecnológica. Define los mecanismos de control presupuestario y seguimiento financiero. |
| 1.4.2 | Flujo de Caja | Proyección temporal de los egresos e ingresos asociados al proyecto. Muestra la distribución de los recursos financieros durante su ejecución y permite evaluar la liquidez y disponibilidad de fondos en cada etapa. |
| 1.4.3 | Curva S | Herramienta gráfica de control que refleja la evolución del avance físico y financiero en el tiempo, facilitando la comparación entre lo planificado, lo ejecutado y lo real para detectar desviaciones y aplicar medidas correctivas. |

##### Paquete - 1.5 Gestión de Calidad

Figure 8.8: Paquete - 1.5 Gestión de Calidad

La Gestión de Calidad en el inicio define qué constituye un entregable aceptable. Se establecen los SLA’s (Acuerdos de Nivel de Servicio) y las métricas de rendimiento, disponibilidad y seguridad que el producto final debe cumplir en su operación. Asimismo, se planifican las Pruebas de Calidad que se ejecutarán en fases posteriores. Esto sienta las bases para verificar que el producto entregado no solo cumpla con la funcionalidad requerida, sino también con los estándares de excelencia acordados con el cliente.

![Página 107 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-107.png)

<!-- Página 108 del PDF original -->

Table 8.7: 1.5 Gestión de Calidad Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 1.5.1 | Definición de SLA’s | Documento que establece los indicadores y niveles de servicio esperados para los productos del proyecto. Define parámetros de rendimiento, disponibilidad, tiempos de respuesta, seguridad y calidad esperada en la entrega de cada componente. |
| 1.5.2 | Pruebas de Calidad | Conjunto de actividades orientadas a verificar que los entregables cumplan con los SLA’s definidos y con los criterios de aceptación establecidos por el cliente. Incluye pruebas funcionales, de rendimiento y de seguridad. |

##### Paquete - 1.6 Gestión de Riesgos

Figure 8.9: Paquete - 1.6 Gestión de Riesgos

Esta subfase busca la proactividad al identificar y evaluar las incertidumbres que podrían afectar negativamente los objetivos del proyecto. Se utiliza la RBS (Estructura de Desglose de Riesgos) para clasificarlos de manera sistemática. El resultado principal es el Documento de Mitigación de Riesgos, que especifica acciones preventivas y planes de contingencia, asegurando que el equipo esté preparado para manejar las amenazas y maximizar las oportunidades.

![Página 108 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-108.png)

<!-- Página 109 del PDF original -->

Table 8.8: 1.6 Gestión de Riesgos Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 1.6.1 | RBS (Risk Breakdown Structure) | Estructura jerárquica que clasifica los riesgos del proyecto según su origen -técnico, financiero, operativo o externo-. Facilita la identificación, análisis y priorización de los riesgos para su seguimiento y mitigación. |
| 1.6.2 | Documento de Mitigación de Riesgos | Documento que detalla las estrategias de respuesta y mitigación para cada riesgo identificado. Incluye las acciones preventivas, los planes de contingencia, los responsables designados y los indicadores de seguimiento para el control de riesgos. |

##### Paquete - 1.7 Gestión de Proveedores

Figure 8.10: Paquete - 1.7 Gestión de Proveedores

Esta subfase aborda la estrategia de adquisición de recursos o servicios externos. Se define qué componentes del proyecto serán provistos por terceros y se evalúan las capacidades de los Proveedores potenciales. Se formaliza el Alcance de los Servicios Externos, especificando los criterios de entrega, calidad y gestión contractual para garantizar que las contribuciones externas se integren exitosamente al proyecto total.

![Página 109 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-109.png)

<!-- Página 110 del PDF original -->

Table 8.9: 1.7 Gestión de Proveedores Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 1.7.1 | Definición de Proveedores | Identifica los proveedores potenciales y evalúa sus capacidades técnicas, financieras y operativas. Incluye el proceso de selección, los criterios de evaluación y los términos de contratación necesarios para garantizar la calidad del servicio. |
| 1.7.2 | Definición de Servicios Externos | Determina los servicios que serán provistos por terceros, especificando su alcance, duración, condiciones de entrega, niveles de servicio (SLA’s) y mecanismos de supervisión para asegurar su cumplimiento. |

#### 8.3.2 Fase 2: Diseño

Figure 8.11: Fase - 2 Diseño

La fase de Diseño es el punto donde el proyecto se transforma desde una idea hacia una arquitectura técnica y funcional completamente definida, transformando los requerimientos del sistema (funcionales y no funcionales) en una propuesta válida, estandarizada y que responda al dolor de la empresa contratante y solucione los problemas propuestos, para luego pasar a la fase de construcción (Desarrollo).

##### Paquete - 2.1 Arquitectura de Solución

La subfase de Arquitectura de Solución abarca el diseño técnico y funcional que define cómo se construirá, organizará e integrará el sistema. Esta etapa establece la base estructural de la solución, detallando tanto la arquitectura lógica (componentes, servicios, flujos de datos y APIs) como la física (infraestructura, redes, almacenamiento y ambientes).

![Página 110 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-110.png)

<!-- Página 111 del PDF original -->

Figure 8.12: Paquete - 2.1 Arquitectura de la Solución

Table 8.10: 2.1 Arquitectura de Solución Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 2.1.1 | Esquema General de la Solución | Documento que representa una visión global del sistema, mostrando sus principales componentes, módulos, flujos de información e integraciones con sistemas externos. Sirve como punto de partida para las arquitecturas detalladas. |
| 2.1.2 | Arquitectura Lógica | Describe la estructura lógica de la solución, especificando las capas, servicios, microservicios, APIs, flujos de datos y dependencias entre componentes de software. Facilita la comprensión del comportamiento interno del sistema. |
| 2.1.3 | Arquitectura Física | Define la infraestructura física o virtual necesaria para soportar la solución, incluyendo servidores, redes, balanceadores, almacenamiento, políticas de respaldo y alta disponibilidad. Establece los ambientes (desarrollo, QA, producción) y su configuración técnica. |

##### Paquete - 2.2 Procesos TO-BE

Figure 8.13: Paquete - 2.2 Procesos TO-BE

La subfase de Procesos TO-BE tiene como propósito definir cómo funcionará la or-

![Página 111 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-111.png)

<!-- Página 112 del PDF original -->

Table 8.11: 2.2 Procesos TO-BE Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 2.2.1 | Diagramas BPMN TO- BE | Diagramas de procesos modelados en notación BPMN que ilustran el flujo operativo esperado con la nueva solución, destacando actividades, roles y puntos de control. |
| 2.2.2 | Matriz RACI por proceso | Matriz que define los roles y responsabilidades de cada actor involucrado en los procesos TO-BE, estableciendo quién es responsable, aprobador, consultado e informado en cada actividad. |
| 2.2.3 | Reglas de negocio | Compendio de las reglas y condiciones que rigen la operación del sistema. Define criterios, restricciones y validaciones necesarias para garantizar coherencia en los procesos. |
| 2.2.4 | Acta de aprobación comité de procesos | Documento que formaliza la revisión y aprobación de los procesos TO-BE por parte del comité responsable, dejando constancia de observaciones y acuerdos. |

##### Paquete - 2.3 UX/UI

Figure 8.14: Paquete - 2.3 UX-UI

La subfase de UX/UI se enfoca en diseñar la interfaz de usuario del sistema, garantizando que la solución tecnológica sea intuitiva, accesible y visualmente coherente (Siguiendo los requerimientos y necesidades que especifique el cliente). Se definen los lineamientos de diseño mediante un Design System, se desarrollan wireframes y prototipos, y se documentan las especificaciones funcionales necesarias para la implementación técnica.

![Página 112 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-112.png)

<!-- Página 113 del PDF original -->

Table 8.12: 2.3 UX/UI Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 2.3.1 | Documento Design system | Guía unificada de estilo visual y componentes reutilizables (paleta de colores, tipografía, botones, íconos, formularios, etc.) que asegura coherencia y escalabilidad en el diseño de interfaces. |
| 2.3.2 | Wireframes de alto valor | Bocetos funcionales que representan la estructura y jerarquía de las pantallas principales del sistema. Permiten validar con usuarios la distribución y priorización de la información antes de desarrollar los prototipos. |
| 2.3.3 | Prototipos navegables y pruebas de usabilidad | Versiones interactivas del diseño que permiten simular la navegación y evaluar la experiencia de usuario mediante pruebas con usuarios finales. |
| 2.3.4 | Especificación funcional de UI | Documento técnico que detalla el comportamiento de cada elemento de la interfaz, interacciones, validaciones, estados y flujos de usuario. Sirve de insumo directo para los desarrolladores. |

##### Paquete - 2.4 Validación de diseños

Figure 8.15: Paquete - 2.4 Validación de Diseño

La subfase de Validación de diseños tiene como propósito consolidar y aprobar formalmente todos los elementos desarrollados durante la fase de diseño, asegurando que la solución propuesta cumpla con los requerimientos funcionales, técnicos y de negocio establecidos. Se realiza una revisión integradora de la arquitectura, los procesos y la interfaz de usuario, documentando observaciones y acuerdos mediante actas y reportes técnicos.

![Página 113 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-113.png)

<!-- Página 114 del PDF original -->

Table 8.13: 2.4 Validación de diseños Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 2.4.1 | Acta de Diseño completo | Documento formal que certifica la aprobación del diseño integral del sistema por parte de los comités técnicos y funcionales. |
| 2.4.2 | Registro de observaciones | Listado detallado de comentarios, ajustes o recomendaciones identificados durante las revisiones, con su respectivo estado de resolución. |

#### 8.3.3 Fase 3: Desarrollo

Figure 8.16: Fase - 3 Desarrollo

La fase de Desarrollo corresponde a la construcción y materialización de la solución, desde la definición de la arquitectura y el diseño hacia la codificación, componentes de software e integración. Se implementan los requerimientos funcionales y no funcionales, estableciendo los ambientes necesarios, la seguridad y las integraciones. Esta etapa sigue los lineamientos y buenas prácticas de codificación para asegurar una solución robusta y escalable, que culminará con el sistema listo para las pruebas finales.

##### Paquete - 3.1 Setup de ambientes

Figure 8.17: Paquete - 3.1 Setup de Ambientes

Este paquete se enfoca en el aprovisionamiento y configuración de la infraestructura base que soportará el sistema. Incluye la definición y preparación de todos los ambientes (Desarrollo, QA, Producción y Capacitación), la gestión de repositorios de

![Página 114 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-114.png)

<!-- Página 115 del PDF original -->

código y dependencias, y la implementación de sistemas clave de control como la observabilidad y los estándares de seguridad continua (DevSecOps), asegurando que el ciclo de vida del desarrollo se realice en un entorno controlado y seguro.

Table 8.14: 3.1 Setup de ambientes Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 3.1.2 | Repositorio y dependencias del proyecto | Definición del repositorio de código fuente y configuración de librerías, módulos y dependencias externas necesarias para compilar y ejecutar el sistema (dockerfile debe ir incluido en entregable). |
| 3.1.3 | Plataforma de observabilidad | Sistema que centraliza métricas, logs y trazas del entorno. Permite supervisar el rendimiento, detectar fallas y optimizar el desempeño mediante paneles y alertas en tiempo real. |
| 3.1.4 | Seguridad en desarrollo (DevSecOps, SAST y DAST) | Se definen planes de controles de seguridad continua en el ciclo DevOps. Incluye análisis estático (SAST) para el código fuente y dinámico (DAST) para las aplicaciones en ejecución. |

##### Subpaquete - 3.1.1 Ambientes

Figure 8.18: Subpaquete - 3.1.1 Ambientes

Esta subfase es crucial para segregar las etapas del desarrollo. Consiste en configurar entornos aislados para cada propósito: Desarrollo, Pruebas de Calidad (QA), Producción final y Capacitación. Esta separación garantiza que las pruebas de integración y certificación de cumplimiento se realicen sin afectar el ambiente operativo y que la formación de usuarios se haga en un entorno realista y controlado.

![Página 115 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-115.png)

<!-- Página 116 del PDF original -->

Table 8.15: 3.1.1 Ambientes Subpaquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 3.1.1.1 | Desarrollo | Configuraciones y preparación del entorno de desarrollo del proyecto, pruebas iniciales y control de versiones del sistema. Incluye herramientas de compilación, dependencias y configuración de repositorios. |
| 3.1.1.2 | QA | Configuraciones y preparación del espacio dedicado a pruebas de calidad, integración y validación funcional, además de certificaciones de cumplimiento de los requerimientos del sistema. Permite identificar errores antes de pasar a entornos de producción. |
| 3.1.1.3 | Producción | Configuraciones y preparación del ambiente del sistema final destinada a la operación real con usuarios finales y ya validada. |
| 3.1.1.4 | Capacitación | Entorno controlado para entrenamiento de usuarios y certificaciones de los mismos, con datos simulados y configuraciones idénticas a producción. |

##### Paquete - 3.2 Módulos del sistema

Figure 8.19: Paquete - 3.2 Módulos del Sistema

Este paquete comprende el desarrollo de la lógica de negocio central de la aplicación, traduciendo los requerimientos y diseños en código funcional. Se divide por módulos para una gestión eficiente, abarcando desde la gestión clínica (Pacientes), la interacción entre usuarios (Comunicación), los aspectos económicos (Finanzas y Cadena de Suministro), hasta el control interno (Gestión) y el análisis estratégico (Inteligencia).

Table 8.16: 3.2 Módulos del sistema Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 3.2.1 | Módulo Pacientes | Desarrollo y especificaciones del módulo encargado de gestionar la información clínica y administrativa de los pacientes y seguimiento de los mismos, asegurando trazabilidad y confidencialidad. |

Continúa en la siguiente página

![Página 116 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-116.png)

<!-- Página 117 del PDF original -->

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 3.2.2 | Módulo Comunicación | Desarrollo y especificaciones del módulo encargado de la comunicación entre actores (Médicos, operativos y clientes), incluyendo mensajería interna y notificaciones. |
| 3.2.3 | Módulo Finanzas | Desarrollo y especificaciones del módulo encargado de las transacciones monetarias, cobros, facturaciones, API’s relacionadas con el dinero, activos y contabilidad. |
| 3.2.4 | Módulo Cadena de Suministro | Desarrollo y especificaciones del módulo encargado de WMS, TMS, YMS, SMS (Slotting) y LMS, manejo de inventario, bodegas y suministros. |
| 3.2.5 | Módulo Gestión | Desarrollo y especificaciones del módulo encargado de RRHH y control de acceso, incluyendo perfiles de usuario y permisos del sistema. |
| 3.2.6 | Módulo Inteligencia | Desarrollo y especificaciones del módulo encargado del análisis de datos, reportes y dashboards en tiempo real para la toma de decisiones estratégicas. |

##### Paquete - 3.3 Integraciones fundamentales

Figure 8.20: Paquete - 3.3 Integraciones Fundamentales

Este paquete es el encargado de asegurar la interoperabilidad del sistema con el ecosistema externo e interno, incluyendo la adopción de estándares clave de la industria, como los de salud. El desarrollo de interfaces seguras y estables es fundamental para el intercambio de datos con entes gubernamentales, aseguradoras, dispositivos de hardware y sistemas de pago, garantizando la conectividad total de la plataforma.

![Página 117 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-117.png)

<!-- Página 118 del PDF original -->

Table 8.17: 3.3 Integraciones fundamentales Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 3.3.1 | Estándares HL7/FHIR | Documentación de las interfaces a aplicar referentes a la interoperabilidad clínica según los estándares HL7 v3 y FHIR (Version de HL7 mas reciente), asegurando la correcta transmisión de datos clínicos. |

##### Subpaquete - 3.3.2 Integraciones Financieras y Previsionales

Figure 8.21: Subpaquete - 3.3.2 Integraciones financieras y Previsionales

Este subpaquete se concentra en la implementación de las conexiones obligatorias con los sistemas de gobierno y los servicios financieros. Abarca la integración con entidades tributarias (SII) y aseguradoras de salud (Fonasa e Isapre) para la gestión previsional, además del desarrollo de la interfaz de pagos central y la conexión con pasarelas de cobro electrónico (Klap y Transbank), automatizando transacciones y conciliaciones.

Table 8.18: 3.3.2 Integraciones Financieras y Previsionales Subpaquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 3.3.2.1 | SII | Documentación de la implementación de la conexión con el Servicio de Impuestos Internos para emisión y validación de documentos tributarios electrónicos (facturas, boletas, etc.). |
| 3.3.2.2 | Fonasa e Isapre | Documentación del enlace con aseguradoras y prestadores previsionales para validación de afiliaciones, cobertura y gestión de pagos de prestaciones médicas. |
| 3.3.2.3 | Pagos | Documentación de desarrollo de la interfaz central de cobros y pagos del sistema, incluyendo conciliación y registro contable de las transacciones. |
| 3.3.2.4 | Klap | Documentación e Integración de la pasarela Klap para cobros electrónicos, reembolsos y conciliación automática de ventas, según los requerimientos del módulo Finanzas. |

Continúa en la siguiente página

![Página 118 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-118.png)

<!-- Página 119 del PDF original -->

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 3.3.2.5 | Transbank | Documentación e Integración de la pasarela Transbank para gestión de pagos en línea, reembolsos y conciliación automática de ventas. |

##### Subpaquete - 3.3.3 Dispositivos externos

Figure 8.22: Subpaquete - 3.3.3 Dispositivos externos

Este subpaquete se enfoca en la conexión del sistema con el mundo físico y los canales de contacto con el usuario. Incluye la implementación de interfaces con hardware como dispositivos de Biometría para control de acceso y la recepción de datos de IoT (sensores o equipos clínicos). Además, se integra la plataforma con los servicios de Telefonía y mensajería (IVR, WhatsApp Business, call center) para un soporte omnicanal.

Table 8.19: 3.3.3 Dispositivos externos Subpaquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 3.3.3.1 | Biometría | Documentación de la comunicación con dispositivos de autenticación biométrica para control de acceso y validación de identidad en puntos de servicio. |
| 3.3.3.2 | IoT | Documentación de la incorporación de sensores y dispositivos conectados (IoT) de datos clínicos o ambientales al sistema central para monitoreo en tiempo real y registro de datos. |
| 3.3.3.3 | Telefonía | Documentación de la implementación de servicios de telefonía IP y call center, IVR, WhatsApp Business y registro de contactos en el CRM. |

##### Subpaquete - 3.3.4 Integración con sistemas externos

Este CC aborda la conectividad a nivel de arquitectura e infraestructura. Se enfoca en la configuración de la comunicación de datos mediante APIs y servidores (locales y

![Página 119 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-119.png)

<!-- Página 120 del PDF original -->

Figure 8.23: Subpaquete - 3.3.4 Integración con sistemas externos

en la nube), el diseño e implementación de la seguridad de redes (firewall, VPN) y la configuración del Datacenter y las bases de datos (respaldos, réplicas). Finalmente, se implementan las herramientas de Business Intelligence para la explotación de los datos generados.

Table 8.20: 3.3.4 Integración con sistemas externos Subpaquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 3.3.4.1 | API’s | Configuraciones y desarrollo de las APIs (REST) y servicios SOAP que permitirán el intercambio de datos con otros sistemas y aplicaciones. |
| 3.3.4.2 | Servidores | Implementación de conectividad segura con servidores locales y en la nube, gestionando servicios, despliegues y sincronización de datos. |
| 3.3.4.3 | Seguridad y redes | Configuraciones de firewall, VPN, SD-WAN, canales de comunicación y segmentación de red para garantizar comunicaciones seguras y control de acceso. |
| 3.3.4.4 | Datacenter y bases de datos | Definición de la arquitectura de almacenamiento, réplicas, respaldos y acceso a bases de datos dentro de los datacenter, cumpliendo con la continuidad operativa. |
| 3.3.4.5 | Business Intelligence y análisis | Implementación de herramientas analíticas para el análisis de datos operativos y clínicos del sistema, alimentando el Módulo Inteligencia. |

##### Subpaquete - 3.3.5 Documentación técnica

Figure 8.24: Subpaquete - 3.3.5 Documentación técnica

Este CC finaliza la fase de Desarrollo con la creación del material de referencia esencial para el soporte, mantenimiento y la trazabilidad del sistema. Se elaboran los

![Página 120 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-120.png)

<!-- Página 121 del PDF original -->

Table 8.21: 3.3.5 Documentación y Cierre Técnico Subpaquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 3.3.5.1 | Manuales técnicos | Documentación técnica del sistema: guías de instalación, mantenimiento, configuración y soporte de infraestructura, destinada al equipo técnico. |
| 3.3.5.2 | Catálogo de integraciones y datos | Registro detallado de todas las integraciones, fuentes de datos y estructuras utilizadas, incluyendo diccionarios de datos y diagramas de flujo. |

##### Subpaquete - 3.4 Plan de migración de Datos

Figure 8.25: Subpaquete - 3.4 Plan de migración de Datos

Este CC aborda la transición estructurada de los datos del sistema legado hacia la nueva plataforma, garantizando su integridad, consistencia y disponibilidad. La correcta ejecución de este plan es crítica para el funcionamiento del sistema en producción y para la continuidad operativa de los módulos desarrollados.

Table 8.22: 3.4 Plan de Migración de Datos Subpaquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 3.4.1 | Digitalización de datos físicos | Proceso de conversión de registros en papel u otros formatos físicos a versiones electrónicas estructuradas. Incluye escaneo, normalización de formatos, control de calidad y verificación de integridad antes de su carga en los sistemas digitales. |
| 3.4.2 | Migración de datos a servidores cloud | Transferencia controlada de la información hacia entornos en la nube. Contempla la configuración de los espacios de almacenamiento, validación de compatibilidad de esquemas de base de datos y aplicación de políticas de respaldo y seguridad para garantizar la disponibilidad e integridad de los datos. |

Continúa en la siguiente página

![Página 121 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-121.png)

<!-- Página 122 del PDF original -->

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 3.4.3 | Migración de datos a servidores físicos | Ejecución de la carga de información en servidores locales o híbridos, asegurando la sincronización con el entorno cloud y la correcta replicación de los datos críticos. Incluye pruebas de verificación, monitoreo de transferencias y planes de contingencia ante fallas de comunicación o pérdida de información. |

#### 8.3.4 Fase 4: Obras Civiles y Montajes

Figure 8.26: Fase - 4 Obras Civiles y Montaje

La fase de Obras Civiles y Montajes representa el punto donde la infraestructura física y tecnológica del proyecto se vuelve tangible, convirtiéndose, de tal forma que se estructuran los cableados, sistemas de seguriadad, hardware, componentes, dispositivos de red, instalaciones y todo lo relacionado a infraestructura física de la solución.

##### Paquete - 4.1 Adecuación de espacios

Figure 8.27: Paquete - 4.1 Adecuación de Espacios

La subfase de Adecuación de espacios se centra en preparar la infraestructura física necesaria para la instalación del equipamiento tecnológico del proyecto. Durante esta etapa se ejecutan las obras civiles requeridas para garantizar condiciones óptimas de seguridad, climatización, distribución eléctrica y espacio. Se incluyen tareas como el acondicionamiento de salas de TI, la instalación de canalizaciones y racks, y la verificación de sistemas de respaldo energético y climatización. Formalizada mediante un acta de recepción técnica que certifica que los espacios cumplen con los estándares establecidos para proceder al montaje de los equipos.

![Página 122 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-122.png)

<!-- Página 123 del PDF original -->

Table 8.23: 4.1 Adecuación de espacios Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 4.1.1 | Sala TI acondicionada y certificada | Espacio físico destinado a albergar equipos de tecnología (servidores, comunicaciones) que ha sido remodelado, asegurando requisitos de espacio, seguridad, anti-incendio y ambientación. |
| 4.1.2 | Canalizaciones y racks | Implementación física de los sistemas de soporte para el cableado (bandejas, ductos) y la colocación de los gabinetes (racks) donde se alojará el equipamiento de red y servidores. |
| 4.1.3 | UPS/ generador/ climatización | Verificación de que los sistemas de energía ininterrumpida (UPS), los generadores de respaldo y los equipos de aire acondicionado están instalados, probados y funcionando correctamente. |
| 4.1.4 | Acta de recepción técnica | Documento formal que certifica la finalización de las obras civiles y la adecuación de los espacios por parte del equipo técnico. Esto habilita el paso a la instalación de los equipos tecnológicos. |

##### Paquete - 4.2 Cableado estructurado

Figure 8.28: Paquete - 4.2 Cableado Estructurado

La subfase de Cableado estructurado abarca la instalación, certificación y documentación de toda la red física que soportará la conectividad del sistema. En esta etapa se ejecuta el tendido del cableado de fibra óptica y cobre de alta velocidad, asegurando la integridad y el cumplimiento de los estándares internacionales de telecomunicaciones. Además, se realizan pruebas de calidad de servicio y latencia, junto con la certificación de enlaces y el registro detallado de planos “as-built”.

![Página 123 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-123.png)

<!-- Página 124 del PDF original -->

Table 8.24: 4.2 Cableado estructurado Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 4.2.1 | Tendido FO/Cat6A | Finalización de la instalación física de todo el cableado de fibra óptica (FO) y del cableado de cobre Categoría 6A (Cat6A), cumpliendo con el diseño de la red. |
| 4.2.2 | Certificación de enlaces | Realización de pruebas especializadas que verifican la calidad, ancho de banda y cumplimiento de estándares de cada punto de red y fibra, con la aprobación de los resultados. |
| 4.2.3 | Etiquetado y planos asbuilt | Entrega de la documentación final que incluye la identificación unívoca de cada cable y punto de red. También se proporcionan los planos que reflejan la instalación tal como fue ejecutada. |
| 4.2.4 | Pruebas QoS/latencia | Verificación de que la red cumple con los parámetros de calidad de servicio (QoS) y que los tiempos de demora (latencia) en las comunicaciones son aceptables, según los requisitos del proyecto. |

##### Paquete - 4.3 Equipamiento de campo

Figure 8.29: Paquete - 4.3 Equipamiento de Campo

La subfase de Equipamiento de campo aborda la instalación física y la configuración inicial de todos los dispositivos de usuario y equipos especializados que se utilizarán en los diferentes puntos de operación. Este paquete garantiza que los equipos de red, seguridad, terminales clínicos, dispositivos biométricos e infraestructura IoT queden correctamente instalados, conectados y operativos, cumpliendo con los estándares técnicos y de seguridad definidos en el proyecto. Además, contempla la actualización del inventario tecnológico en la base de datos de gestión de la configuración (CMDB), asegurando trazabilidad y control de los activos implementados.

![Página 124 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-124.png)

<!-- Página 125 del PDF original -->

Table 8.25: 4.3 Equipamiento de campo Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 4.3.1 | Red/seguridad/SD- WAN | Configuración de todos los equipos de comunicaciones (switches, routers) y seguridad (firewalls). Se incluye la implementación de arquitecturas de red definidas por software (SD-WAN). |
| 4.3.2 | Endpoints clínicos y biometría | Instalación física y configuración de equipos terminales especializados, como estaciones de trabajo médicas, dispositivos de captura de datos clínicos y equipos de autenticación biométrica. |
| 4.3.3 | IoT e impresión | Puesta en marcha de todos los dispositivos de Internet de las Cosas (IoT) y de los sistemas de impresión. |
| 4.3.4 | Inventario CMDB | Actualización del registro formal de todos los activos tecnológicos instalados en la Base de Datos de Gestión de la Configuración (CMDB). Esto es clave para la gestión y el mantenimiento futuros. |

##### Paquete - 4.4 Sistemas de seguridad

Figure 8.30: Paquete - 4.4 Sistemas de Seguridad

La subfase de Sistemas de seguridad está orientada a la implementación y validación de las medidas de seguridad física en las instalaciones, asegurando la protección de los espacios tecnológicos y del personal autorizado. Este paquete contempla la instalación de sistemas de control de acceso, videovigilancia (CCTV) e integración con la base de datos de Recursos Humanos, permitiendo la gestión centralizada de permisos de ingreso y monitoreo. Además, se incluyen los Procedimientos Operacionales Estándar (SOPs) y los planes de contingencia necesarios para actuar ante emergencias o fallos de seguridad, garantizando la continuidad operativa y la trazabilidad de eventos.

![Página 125 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-125.png)

<!-- Página 126 del PDF original -->

Table 8.26: 4.4 Sistemas de seguridad Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 4.4.1 | Control de acceso físico | Instalación y configuración de torniquetes, cerraduras electrónicas y lectores de tarjetas. Se asegura que el sistema para regular el ingreso a áreas restringidas esté funcionando. |
| 4.4.2 | CCTV y monitoreo | Instalación de cámaras de circuito cerrado de televisión (CCTV) y de la infraestructura de software para la visualización y almacenamiento de las grabaciones, listas para su monitoreo. |
| 4.4.3 | Integración con RRHH | Verificación de que el sistema de control de acceso físico se comunica y sincroniza correctamente con la base de datos de Recursos Humanos. Esto permite gestionar permisos de entrada y salida de personal. |
| 4.4.4 | SOPs y contingencias | Creación y distribución de los Procedimientos Operacionales Estándar (SOPs) y los planes de actuación para manejar fallos o emergencias relacionadas con los sistemas de seguridad física. |

##### Paquete - 4.5 Configuración de infraestructura

Figure 8.31: Paquete - 4.5 Configuración de la Infraestructura

La subfase de Configuración de infraestructura está dedicada a establecer y configurar los componentes técnicos que soportarán el funcionamiento del sistema. Incluye la preparación de los ambientes en la nube, la infraestructura en sedes, los centros de operación de red y seguridad, así como los entornos de desarrollo, aseguramiento de calidad y capacitación. Esta etapa garantiza que toda la base tecnológica esté operativa, interconectada y alineada con la arquitectura definida en fases previas.

![Página 126 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-126.png)

<!-- Página 127 del PDF original -->

Table 8.27: 4.5 Configuración de infraestructura Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 4.5.1 | Cloud Prod + DR | Configuración de los entornos principales de Producción (Prod) y de Recuperación ante Desastres (DR) en la infraestructura de la nube, cumpliendo con la arquitectura definida. |
| 4.5.2 | Infra edge en sedes | Instalación y configuración de los componentes de infraestructura en las ubicaciones remotas (edge). Esto se realiza para soportar aplicaciones locales o garantizar la continuidad de la operación. |
| 4.5.3 | NOC/SOC, SIEM, WAF | Implementación de los centros de operación de red (NOC) y seguridad (SOC). Se incluyen herramientas como el SIEM (gestión de eventos de seguridad) y el WAF (firewall de aplicación web) para monitoreo y defensa. |
| 4.5.4 | Ambientes | Configuración de los entornos de Desarrollo (Dev), Aseguramiento de Calidad (QA) y Capacitación (Capacitación). Esto permite que los equipos de software y entrenamiento puedan comenzar su trabajo. |

#### 8.3.5 Fase 5: Adquisiciones, Contratos y Documentación

Figure 8.32: Fase - 5 Intervención

La fase Intervención corresponde al momento en que el sistema desarrollado se integra y valida dentro de un entorno más real de la institución, marcando la transición entre las pruebas controladas y la preparación para la operación definitiva. Se realizan cargas de los datos maestros reales, configuraciones de los parámetros institucionales y ejecuciones rigurosas de pruebas integrales, de carga y de seguridad. Esta fase culmina con los ajustes y optimizaciones finales, preparando la solución para el Go-Live.

##### Paquete - 5.1 Permisos y cumplimiento

Este CC establece los lineamientos y acciones necesarias para garantizar que el proyecto cumpla con todas las normativas legales, técnicas y administrativas vigentes. Su ejecución es fundamental para la continuidad de la obra y la obtención de las aprobaciones formales requeridas por las autoridades competentes. Busca minimizar riesgos legales,

![Página 127 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-127.png)

<!-- Página 128 del PDF original -->

Figure 8.33: Paquete - 5.1 Migración de datos maestros

evitar retrasos derivados de observaciones regulatorias y reforzar la transparencia y sostenibilidad del proyecto en su fase de implementación y operación.

Table 8.28: 5.1 Permisos y Cumplimiento Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 5.1.1 | Permisos sanitarios y regulatorios | Gestión y tramitación de las autorizaciones requeridas por las autoridades sanitarias y los organismos reguladores correspondientes. Incluye revisiones técnicas, presentación de antecedentes y control del cumplimiento de normativas específicas del sector salud o equivalente. |
| 5.1.2 | Validación de cumplimiento de Leyes | Revisión integral del cumplimiento de las leyes y reglamentos aplicables al proyecto, abarcando normativa laboral, ambiental, de protección de datos y seguridad. Este entregable certifica que el proyecto se desarrolla dentro del marco legal vigente. |
| 5.1.3 | Permisos de construcción | Obtención de licencias, permisos municipales y autorizaciones necesarias para la ejecución de obras civiles o instalaciones técnicas. Incluye la coordinación con entidades fiscalizadoras y la gestión de documentación constructiva. |
| 5.1.4 | Compliance y Cumplimiento Normativo | Diseño e implementación de mecanismos de control interno que aseguren el cumplimiento normativo y ético del proyecto. Comprende auditorías de conformidad, elaboración de reportes de compliance y verificación de políticas corporativas. |

##### Paquete - 5.2 Hardware e infraestructura

![Página 128 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-128.png)

<!-- Página 129 del PDF original -->

pacios técnicos estén disponibles, instalados y operativos en los plazos previstos.

Table 8.29: 5.2 Hardware e Infraestructura Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 5.2.1 | Adquisición de componentes | Proceso de selección, compra y recepción de los equipos y dispositivos necesarios para la infraestructura tecnológica. Incluye servidores, estaciones de trabajo, dispositivos de red, elementos de respaldo energético y demás componentes físicos requeridos. |
| 5.2.2 | Promesa de compraventa de edificaciones | Formalización de acuerdos contractuales relacionados con la adquisición o uso de edificaciones, espacios técnicos o salas de servidores. Comprende la verificación de requisitos legales, condiciones estructurales y compromisos de entrega. |
| 5.2.3 | Órdenes de compra y logística | Gestión y control de las órdenes de compra, transporte y almacenamiento de los componentes adquiridos. Incluye seguimiento de entregas, coordinación con proveedores, documentación de recepción y control de inventario. |

##### Paquete - 5.3 SW y licencia

Figure 8.35: Paquete - 5.3 SW y licencia

Comprende las actividades destinadas a la adquisición, validación y administración de las licencias de software requeridas para el correcto funcionamiento de la solución planteada. Garantiza la legalidad y permiso de uso de las aplicaciones, el cumplimiento de los términos contractuales establecidos por los proveedores y la disponibilidad de

![Página 129 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-129.png)

<!-- Página 130 del PDF original -->

las claves o permisos de acceso en los entornos de desarrollo, prueba y producción.

Table 8.30: 5.3 Software y Licencia Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 5.3.1 | Adquisición de claves y/o licencias | Gestión de la compra o suscripción de licencias de software, claves de activación y permisos de uso necesarios para el despliegue de las soluciones tecnológicas. Incluye la verificación de compatibilidad con la infraestructura y el registro documental de las licencias adquiridas. |
| 5.3.2 | Contratos, términos y condiciones, y cumplimiento | Revisión y formalización de los contratos de software, incluyendo sus términos de uso, políticas de renovación, garantías, y cláusulas de cumplimiento legal. Contempla la verificación de conformidad con las políticas de compliance institucional y con la normativa sobre propiedad intelectual y licencias. |

##### Paquete - 5.4 Contratos y acuerdos con Proveedores

Figure 8.36: Paquete - 5.4 Contratos y acuerdos con Proveedores

Contiene las actividades orientadas a la formalización, administración y control de los contratos y acuerdos de proveedores y prestamistas de servicio, asegurando que las relaciones contractuales se desarrollen bajo condiciones claras, verificables y de manera justa según lo acordado por ambas partes.

![Página 130 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-130.png)

<!-- Página 131 del PDF original -->

Table 8.31: 5.4 Contratos y Acuerdos con Proveedores Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 5.4.1 | Trabajadores y prestadores de servicio | Gestión de la contratación de personal especializado y prestadores externos de servicios. Incluye la definición de roles, responsabilidades, condiciones laborales, y cláusulas de confidencialidad y desempeño. |
| 5.4.2 | Contratos y planes de capacitación | Elaboración de contratos específicos que contemplan planes de capacitación técnica y operativa para el personal y los proveedores. Garantiza que el conocimiento requerido para la ejecución y soporte del proyecto sea transferido de manera efectiva. |
| 5.4.3 | Acuerdos de SLAs y penalidades | Definición formal de los acuerdos de nivel de servicio (SLA) y las penalidades asociadas al incumplimiento de tiempos, calidad o disponibilidad. Establece los mecanismos de seguimiento, evaluación y resolución de incidencias contractuales. |
| 5.4.4 | Matriz de proveedores críticos | Desarrollo de una matriz que identifica a los proveedores esenciales para la continuidad operativa del proyecto, evaluando su criticidad, dependencia y planes de mitigación ante posibles fallas o incumplimientos. |

##### Paquete - 5.5 Riesgo de adquisiciones

Figure 8.37: Paquete - 5.5 Riesgo de adquisiciones

Se establecen las estrategias y mecanismos de identificación, evaluación y miti-

![Página 131 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-131.png)

<!-- Página 132 del PDF original -->

gación de riesgos asociados a la adquisición y contratación en el proyecto, garantizando la continuidad operacional frente a eventos que puedan afectar la disponibilidad de recursos o servicios críticos.

Table 8.32: 5.5 Riesgos de Adquisiciones Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 5.5.1 | Matriz de riesgos y proveedores alternos | Identificación y categorización de riesgos asociados a los procesos de adquisición, junto con la definición de proveedores alternativos para asegurar la continuidad del suministro. Incluye criterios de criticidad, tiempos de respuesta, y estrategias de mitigación frente a fallas o incumplimientos. |
| 5.5.2 | Planes de contingencia y continuidad | Diseño y documentación de estrategias de respuesta ante eventos disruptivos en el proceso de adquisición o contratación. Comprende protocolos de acción, reasignación de recursos, mecanismos de respaldo contractual y medidas para garantizar la continuidad operativa del proyecto. |

#### 8.3.6 Fase 6: Capacitaciones

Figure 8.38: Fase - 6 Capacitaciones

La fase de Capacitaciones tiene como propósito asegurar que todos los actores trabajadores de la empresa contratante adquieran las competencias necesarias para operar el sistema y tener pleno conocimiento de todas las funcionalidades que les competan, dependiendo de sus roles y certificando a los mismos.

##### Paquete - 6.1 Capacitación Masiva por roles

La subfase de Capacitación Masiva por roles se enfoca en el diseño, planificación y ejecución de los programas de entrenamiento destinados a los usuarios finales. Ase-

![Página 132 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-132.png)

<!-- Página 133 del PDF original -->

Figure 8.39: Paquete - 6.1 Capacitación Masiva por roles

gurando que cada participante adquiera las competencias necesarias para operar el sistema de manera eficiente, según sus funciones específicas. Este paquete contempla la formación de instructores internos, la elaboración de planes de capacitación por rol, el diseño de rutas de aprendizaje progresivas y la implementación de modalidades mixtas de enseñanza (B-learning) para maximizar la adopción de la solución tecnológica.

Table 8.33: 6.1 Capacitación Masiva por roles

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 6.1.1 | Plan de Capacitación de instructores internos | Documento que define la estrategia para entrenar a un grupo selecto de empleados que actuarán como formadores. Esto garantiza la sostenibilidad y autonomía en la transferencia de conocimiento dentro de la organización. |
| 6.1.2 | Plan de Capacitación de trabajadores por rol | Detalle de la metodología, cronograma, recursos y contenidos específicos para entrenar a la población de usuarios finales, agrupados según las funciones y responsabilidades que tendrán en el nuevo sistema. |
| 6.1.3 | Rutas de aprendizaje por rol | Diseño secuencial de los módulos o temas de capacitación. Esto asegura que cada usuario, según su rol, cubra el contenido necesario de forma progresiva, desde lo básico hasta el uso avanzado de la solución. |
| 6.1.4 | Capacitaciones Blearning interactivas | Desarrollo y ejecución de sesiones de entrenamiento utilizando una combinación de métodos (presencial y online) con recursos didácticos y actividades prácticas que fomentan la participación activa de los asistentes. |

##### Paquete - 6.2 Evaluaciones y certificaciones

![Página 133 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-133.png)

<!-- Página 134 del PDF original -->

de certificados que acreditan la finalización exitosa del proceso de aprendizaje, consolidando la preparación del personal previo a la puesta en producción del sistema.

Table 8.34: 6.2 Evaluaciones y certificaciones Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 6.2.1 | Pruebas por rol | Diseño y aplicación de exámenes o ejercicios prácticos específicos para cada grupo de usuarios. Esto valida que han asimilado correctamente los conocimientos y habilidades necesarios para su función. |
| 6.2.2 | Entrega Certificados | Emisión para posterior distribución de los documentos formales que acreditan que los trabajadores han completado las rutas de aprendizaje y han aprobado satisfactoriamente las evaluaciones requeridas. |

#### 8.3.7 Fase 7: Puesta en Producción

Figure 8.41: Fase - 7 Puesta en Producción

La fase Puesta en Producción es el punto de transición luego de testing, QA y Staging, donde el sistema pasa desde los entornos de prueba y validación hacia su operación real con usuarios finales. En esta fase se implementarán y pondrán todos los sistemas desarrollados y construidos a disposición de los actores del sistema, ya habiendo asegurado y probado todo en Staging. Se enfoca en el despliegue controlado (piloto), el soporte intensivo (Hypercare), la estabilización del sistema y la preparación para el Rollout masivo.

##### Paquete - 7.1 Permisos de Centro

Figure 8.42: Paquete - 7.1 Permisos de Centro

![Página 134 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-134.png)

<!-- Página 135 del PDF original -->

Centrada principalmente en la implementación inicial y controlada de la solución en un entorno limitado para validar todos los aspectos operativos, técnicos y de negocio antes del despliegue masivo. Incluye la formalización del Plan de deploy y corte, la ejecución exitosa del Go-live de piloto, la Validación en terreno de los procesos con usuarios reales y la certificación formal del Acta de piloto exitoso, que define el cumplimiento de los criterios de éxito.

Table 8.35: 7.1 Permisos de Centro Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 7.1.1 | Plan de deploy y corte | Documento que detalla la estrategia y el cronograma para el despliegue de la solución y la transición desde el sistema anterior al nuevo, el cual debe contar con la aprobación formal. |
| 7.1.2 | Go-live de piloto | Ejecución exitosa del plan de despliegue que implica la activación de la nueva solución en el ambiente de piloto, haciéndola disponible para los usuarios definidos. |
| 7.1.3 | Validación en terreno | Conjunto de pruebas y verificaciones realizadas directamente en el sitio de implementación del piloto, para confirmar que la solución funciona correctamente bajo condiciones operacionales reales. |
| 7.1.4 | Acta de piloto exitoso | Documento formal que certifica y registra la conclusión exitosa del piloto, validando que se cumplieron los criterios de éxito definidos y autorizando los siguientes pasos. |

##### Paquete - 7.2 Hypercare 24x7

Figure 8.43: Paquete - 7.2 Hypercare 24x7

Esta subfase corresponde al soporte intensivo posterior al go-live del piloto, caracterizado por una dedicación 24/7 para asegurar la estabilidad del sistema. Se activa el War-room y soporte on-site para la resolución inmediata de incidentes críticos. El desempeño es monitoreado de cerca con el Reporte de monitoreo SLAs críticos y el Reporte Gestión de incidentes, culminando en un Informe de estabilización que determina si el sistema puede pasar a una operación estándar.

![Página 135 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-135.png)

<!-- Página 136 del PDF original -->

Table 8.36: 7.2 Hypercare 24x7 Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 7.2.1 | War-room y soporte onsite | Confirmación de la activación de una sala de guerra (equipo multidisciplinario) y de personal de soporte en el lugar de la implementación, garantizando una respuesta rápida a cualquier problema postlanzamiento. |
| 7.2.2 | Reporte de monitoreo SLAs críticos | Documento que informa y compara el desempeño real de la solución en producción frente a los indicadores clave de servicio (SLA’s) preestablecidos, verificando su cumplimiento. |
| 7.2.3 | Reporte Gestión de incidentes | Registro detallado de todos los incidentes, errores o problemas reportados durante el período de hypercare, incluyendo su clasificación, estado, resolución y tiempo de respuesta. |
| 7.2.4 | Informe de estabilización | Documento que evalúa el nivel de estabilidad operativa de la solución al finalizar el hypercare. Concluye si la solución está lista para una operación estándar con soporte menos intensivo o requiere acciones adicionales. |

##### Paquete - 7.3 Estabilización

Figure 8.44: Paquete - 7.3 Estabilización

Esta subfase se enfoca en consolidar la operación y transición del soporte intensivo a la operación rutinaria. Se implementan las Correcciones post go-live y se realizan Ajustes de capacidad y costos basados en la carga de trabajo real. Se verifica que los KPIs de servicio hayan alcanzado un nivel estable y aceptable, y se concluye con el Cierre de hypercare formal, indicando la madurez operativa del sistema.

![Página 136 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-136.png)

<!-- Página 137 del PDF original -->

Table 8.37: 7.3 Estabilización Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 7.3.1 | Correcciones post golive | Implementación de las soluciones a los defectos e incidentes críticos identificados durante el período de hypercare y la validación en terreno del piloto. |
| 7.3.2 | Ajustes de capacidad y costos | Modificaciones a la infraestructura, recursos de soporte o asignación presupuestaria. Esto se basa en la carga de trabajo y los costos reales observados durante el piloto y el hypercare. |
| 7.3.3 | KPI’s de servicio | Confirmación de que los indicadores clave de rendimiento (KPI’s) del servicio han alcanzado un nivel estable y aceptable. Esto verifica que la solución cumple con los objetivos de negocio y rendimiento esperados. |
| 7.3.4 | Cierre de hypercare | Aprobación formal que da por terminada la fase de soporte intensivo (hypercare), indicando que el sistema ha alcanzado la estabilidad requerida para pasar a la operación rutinaria. |

##### Paquete - 7.4 Ajustes por feedback

Figure 8.45: Paquete - 7.4 Ajustes por feedback

Esta subfase se centra en la optimización continua y la mejora de la experiencia de usuario (UX) basada en la operación real. Se implementan Quick wins (mejoras rápidas de alto impacto) y Mejoras de UX según la retroalimentación directa del piloto. Además, se revisan y corrigen los Manuales y KB con información real. Finalmente, se documentan las Lecciones aprendidas para mejorar la ejecución de futuros despliegues o proyectos.

![Página 137 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-137.png)

<!-- Página 138 del PDF original -->

Table 8.38: 7.4 Ajustes por feedback Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 7.4.1 | Quick wins | Aplicación de pequeñas mejoras o cambios funcionales de bajo esfuerzo e impacto visible. Esto mejora rápidamente la satisfacción del usuario y la experiencia inicial del sistema. |
| 7.4.2 | Reporte de Mejoras de UX | Implementación de ajustes a la interfaz y la experiencia de usuario. Esto se basa en los hallazgos de las pruebas en terreno y el feedback del piloto, optimizando la facilidad de uso y la eficiencia. |
| 7.4.3 | Manuales y KB | Revisión y corrección de la documentación de usuario y la base de conocimiento (KB) con la información obtenida durante la operación real del piloto, asegurando su precisión y utilidad. |
| 7.4.4 | Lecciones aprendidas | Recopilación estructurada de los éxitos, desafíos, errores y mejores prácticas del piloto y go-live. Su propósito es mejorar la ejecución de las fases futuras o de proyectos similares. |

##### Paquete - 7.5 Preparación rollout

Figure 8.46: Paquete - 7.5 Preparación rollout

Esta subfase finaliza la Fase 7 y prepara el camino para el despliegue de la solución a gran escala. Utilizando la experiencia del piloto como base, se crea el Plan multi-sede para el despliegue masivo y se planifica el Ramp-up de soporte para las nuevas ubicaciones. Se verifica la preparación de cada sitio con el Checklist de readiness por sede y se obtiene la Aprobación para Etapa 2 formal, que autoriza el inicio del despliegue completo.

![Página 138 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-138.png)

<!-- Página 139 del PDF original -->

Table 8.39: 7.5 Preparación rollout Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 7.5.1 | Plan multi-sede | Documento que detalla la estrategia, la logística, el cronograma y los recursos necesarios para el despliegue masivo de la solución en otras ubicaciones, el cual debe contar con la aprobación formal. |
| 7.5.2 | Ramp-up de soporte | Plan que especifica el aumento progresivo de la capacidad y los niveles de soporte para atender la demanda de usuarios en las nuevas sedes, incluyendo capacitación y dotación de personal. |
| 7.5.3 | Checklist de readiness por sede | Verificación exhaustiva de que cada nueva ubicación (sede) cumple con todos los requisitos técnicos, operativos y de capacitación antes del despliegue, mitigando riesgos de go-live. |
| 7.5.4 | Aprobación para Etapa 2 | Decisión formal y documentada que certifica que el piloto fue exitoso. Esto autoriza el inicio de la segunda etapa de despliegue a gran escala o rollout multi-sede. |

##### Paquete - 7.6 Pruebas de carga/stress

Figure 8.47: Paquete - 7.6 Pruebas de carga/stress

Se encuentran las actividades de verificar el comportamiento del sistema bajo condiciones de alta carga, demanda o estrés operacional, buscando identificar posibles cuellos de botella, límites de rendimiento y puntos de degradación del servicio antes del paso definitivo a producción, para finalmente definir si va o no el sistema a producciòn e interacciòn con el cliente. Las pruebas permiten validar la estabilidad de la infraestructura, el desempeño del software y la capacidad de respuesta ante escenarios críticos, asegurando cumplimieno por ejemplo de SLA‘s.

![Página 139 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-139.png)

<!-- Página 140 del PDF original -->

Table 8.40: 7.6 Pruebas de Carga/Stress Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 7.6.1 | Plan de performance | Documento técnico que establece la metodología, métricas y herramientas a utilizar en las pruebas de rendimiento. Define los parámetros de monitoreo, las métricas de éxito y los entornos en los que se evaluará el desempeño del sistema. |
| 7.6.2 | Plan de stress y tuning | Diseño de escenarios de carga extrema y estrategias de ajuste fino del sistema (tuning). Permite evaluar el comportamiento del software y la infraestructura ante sobrecarga progresiva, identificando umbrales críticos y configuraciones óptimas. |
| 7.6.3 | Informe de capacidad | Reporte que documenta los resultados obtenidos durante las pruebas de carga y stress. Incluye análisis de consumo de CPU, memoria, red, disco, concurrencia de usuarios y tiempos de respuesta, determinando la capacidad real de la plataforma. |
| 7.6.4 | Acta Go/No-Go | Documento de validación que consolida los resultados de las pruebas de rendimiento y estabilidad, determinando la decisión final de avanzar o no hacia la liberación en producción. Incluye criterios de aceptación, observaciones y responsables de la decisión. |

#### 8.3.8 Fase 8: Finalización de Proyecto

Figure 8.48: Fase - 8 Finalización de Proyecto

La fase de finalización del Proyecto marca el cierre formal del ciclo de vida del sistema y representa el momento en que se consolida, transfiere y valida todo el trabajo desarrollado durante las etapas previas, asegurando que se haya cumplido lo prometido, se finalicen las actividades administrativas, de desarrollo y de mantenimiento, hitos de finalización formales de contratos y termino de límites de garantías, etc.

![Página 140 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-140.png)

<!-- Página 141 del PDF original -->

##### Paquete - 8.1 Termino de actividades

Figure 8.49: Paquete - 8.1 - Término de Actividades

La subfase de Término de actividades tiene como objetivo consolidar la finalización de todas las actividades del proyecto, tanto en el ámbito de desarrollo como en la gestión operativa y de mantenimiento. En este punto se documenta oficialmente el término de las tareas técnicas, administrativas y de soporte, garantizando que todas las funcionalidades estén completadas y que la documentación asociada esté actualizada antes del cierre formal del proyecto.

Table 8.41: 8.1 Termino de actividades Paquete - Diccionario de la EDT

| ID | Nombre del paquete | Descripción |
| --- | --- | --- |
| 8.1.1 | Término de desarrollo del sistema | Documento donde se explicita oficialmente la finalización de todas las actividades técnicas y de desarrollo, asegurando que las funcionalidades estén implementadas, probadas y documentadas antes del cierre formal. |
| 8.1.2 | Término de actividades administrativas | Documento donde se marca el hito de finalización de las tareas de gestión, coordinación y documentación asociadas al proyecto, incluyendo reportes finales, validaciones internas y cierre de tareas administrativas. |
| 8.1.3 | Término de mantenimiento | Documento que marca el fin del soporte durante el proyecto o periodo de garantía acordado, garantizando que se entreguen los informes de incidencias y registros de mantención ejecutada, además de garantizar el comienzo del periodo de mantención con costos agregados de la misma. |

![Página 141 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-141.png)

<!-- Página 142 del PDF original -->

##### Paquete - 8.2 Recepción de entregables

Figure 8.50: Paquete - 8.2 - Recepción de entregables

La subfase de Recepción de entregables corresponde al traspaso completo del sistema y toda su documentación al mandante. Este proceso asegura que la solución cumple con los niveles de servicio, estándares técnicos y normativos establecidos. Además, formaliza la transferencia del código fuente, manuales, documentación de soporte y la wiki técnica, garantizando la continuidad operativa del sistema y la trazabilidad futura del conocimiento técnico.

Table 8.42: 8.2 Recepción de entregables Paquete - Diccionario de la EDT

| ID | Nombre del paquete | Descripción |
| --- | --- | --- |
| 8.2.1 | Estado de SLA | Documento que certifica el cumplimiento de los Acuerdos de Nivel de Servicio durante la operación del sistema en los ambientes de prueba o implementación iniciales, detallando tiempos de respuesta, disponibilidad y rendimiento alcanzado entre otros SLA’s definidos en el informe detallado del proyecto. |
| 8.2.2 | Cumplimiento de estándares | Documento que verifica que el sistema cumple con los estándares técnicos, normativos y de calidad definidos en las bases y el informe oficial del proyecto. |
| 8.2.3 | Acta de recepción técnica y administrativa | Acta formal de aceptación por parte del mandante que certifica la recepción satisfactoria de todos los entregables, tanto técnicos como administrativos. |
| 8.2.4 | Entrega de código fuente | Incluye la entrega oficial del código fuente, repositorios, dependencias y scripts necesarios para la operación y mantenimiento futuro del sistema, además de las credenciales y derechos sobre el software desarrollado. |
| 8.2.5 | Documentación | Entrega de toda la documentación técnica, funcional y operativa del sistema: manuales, guías, diagramas, documentación API y reportes de pruebas. |
| 8.2.6 | Wiki para trabajadores | Repositorio interno de conocimiento (wiki) con instrucciones, procedimientos y configuraciones relevantes para el personal técnico y de soporte actualizable por los mismos. |

![Página 142 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-142.png)

<!-- Página 143 del PDF original -->

##### Paquete - 8.3 Cierre de Contratos

Figure 8.51: Paquete - 8.3 - Cierre de Contratos

La subfase de Cierre de Contratos formaliza el proceso económico final del proyecto, asegurando la correcta conciliación de pagos, costos reales y liberación de garantías contractuales. Este paquete garantiza la transparencia y cumplimiento de los compromisos financieros asumidos, cerrando toda relación económica entre las partes involucradas.

Table 8.43: 8.3 Cierre de Contratos Paquete - Diccionario de la EDT

| ID | Nombre del paquete | Descripción |
| --- | --- | --- |
| 8.3.1 | Cierre financiero | Documento que explica la consolidación y revisión final de los aspectos económicos del proyecto: pagos pendientes, conciliaciones y costos reales versus planificados. |
| 8.3.2 | Liberación de garantías | Procedimiento formal para liberar garantías de cumplimiento o boletas de garantía tras la aceptación del proyecto, conforme a los plazos establecidos, se deberá incluir un apartado con firma de la destrucción de las boletas de garantía con firma ante notario del hito de destrucción. |

![Página 143 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-143.png)

<!-- Página 144 del PDF original -->

##### Paquete - 8.4 Cierre de proyecto

Figure 8.52: Paquete - 8.4 - Cierre de proyecto

La subfase de Cierre del proyecto representa el punto final del ciclo de vida del proyecto. En esta etapa se documenta el cumplimiento integral del alcance, los requerimientos y los entregables definidos. Además, se formaliza la aceptación definitiva por parte del mandante mediante actas y reportes finales que consolidan los resultados alcanzados y las lecciones aprendidas para futuros proyectos.

Table 8.44: 8.4 Cierre del proyecto Paquete - Diccionario de la EDT

| ID | Nombre del paquete | Descripción |
| --- | --- | --- |
| 8.4.1 | Acta de cierre | Documento oficial que certifica la finalización total del proyecto, firmado por las partes involucradas, que confirma el cumplimiento del alcance y entregables. |
| 8.4.2 | Estado de cumplimiento de requerimientos | Informe consolidado que demuestra el grado de cumplimiento de los requerimientos funcionales y no funcionales definidos al inicio del proyecto, además de los requerimientos que no se cumplieron con sus motivos, sanciones o continuaciones en el periodo de mantención del proyecto, sea con costos adicionales o no. |

#### 8.3.9 Fase 9: Mantención

La fase de Mantención representará el período posterior tanto de la implementación del sistema como de la capacitación y certificación de los instructores internos, fase donde el objetivo principal es asegurar su continuidad operativa, estabilidad y evolución controlada, con condiciones delimitadas y promesas a cumplir por parte de la empresa oferente.

![Página 144 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-144.png)

<!-- Página 145 del PDF original -->

Figure 8.53: Fase - 9 Mantención

##### Paquete - 9.1 Plan de mantención

Consolida las actividades necesarias para garantizar la sostenibilidad, disponibilidad y mejora continua del sistema implementado. Con propósito es mantener la operación estable y segura a lo largo del ciclo de vida del proyecto, abordando de forma integral las dimensiones técnica, física y de seguridad informática.

Figure 8.54: Fase - 9.1 Plan de mantención

Table 8.45: 9.1 Plan de Mantención Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 9.1.1 | Alcance de mantenimiento correctivo | Define las condiciones, procedimientos y limitaciones del mantenimiento correctivo a ser ejecutado por la empresa oferente. Establece los tiempos de respuesta, responsabilidades y acuerdos formales entre las partes, orientados a resolver fallas detectadas durante la operación del sistema. |
| 9.1.2 | Mantenimiento perfectivo | Planifica las acciones destinadas a la optimización del sistema, considerando mejoras de rendimiento, estabilidad y usabilidad. Incluye ajustes funcionales menores derivados de la retroalimentación de usuarios o cambios no contemplados originalmente, los cuales podrán ser evaluados y cotizados según necesidad. |

Continúa en la siguiente página

![Página 145 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-145.png)

<!-- Página 146 del PDF original -->

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 9.1.3 | Mantenimiento de hardware | Detalla las tareas preventivas y correctivas aplicadas a los componentes físicos del sistema. Comprende revisión y sustitución de piezas, mantenimiento de UPS, climatización, cableado estructurado y actualizaciones de firmware o drivers, asegurando la continuidad operativa de la infraestructura. |
| 9.1.4 | Mantenimiento de ciberseguridad | Establece la periodicidad y metodología de actualización de parches, auditorías de vulnerabilidad, pruebas de penetración y control de accesos. Asegura el cumplimiento de políticas de seguridad y la protección de la información frente a amenazas internas o externas. |
| 9.1.5 | Mantenimiento de redes | Define las actividades de monitoreo, revisión y ajuste de la infraestructura de red. Incluye supervisión de enlaces, control de calidad de servicio (QoS), respaldo de configuraciones, validación de topologías y pruebas de continuidad en firewalls, VPN y SD-WAN. |

##### Paquete - 9.2 Plan de pruebas integrales

Figure 8.55: Fase - 9.2 Plan de pruebas integrales

Su propósito es validar el correcto funcionamiento de los módulos desarrollados, la interoperatividad entre componentes y la estabilidad de la plataformas. Incluye la planificación y desarrollo de escenarios de pruebas end-to-end (E2E), la generación de reportes de integraciones externas y auditorías de seguridad, y la definición de criterios de salida que determinan la transición hacia entornos de rendimiento o aceptación de usuario (UAT).

![Página 146 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-146.png)

<!-- Página 147 del PDF original -->

Table 8.46: 9.2 Plan de Pruebas Integrales Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 9.2.1 | Escenarios E2E | Diseño y ejecución de escenarios de prueba de extremo a extremo que simulan el flujo completo del sistema desde la entrada hasta la salida de datos. Permite validar la interacción entre módulos, interfaces y procesos de negocio bajo condiciones reales de operación. |
| 9.2.2 | Reporte de integraciones externas | Elaboración de un informe técnico que documenta los resultados de las pruebas realizadas sobre integraciones con sistemas externos, APIs, y servicios de terceros. Evalúa la estabilidad, compatibilidad y desempeño de las conexiones entre plataformas. |
| 9.2.3 | Reporte de pruebas de seguridad / auditoría | Registro detallado de las pruebas de seguridad y auditorías realizadas al sistema. Incluye resultados de pruebas de vulnerabilidades, autenticación, cifrado, trazabilidad y cumplimiento de políticas de seguridad. |
| 9.2.4 | Criterios de salida a entornos de rendimiento y UAT | Definición de los parámetros de aprobación que deben cumplirse para liberar el sistema hacia los entornos de pruebas de rendimiento y aceptación de usuario (UAT). Establece métricas de calidad, cobertura de pruebas, resolución de incidencias y criterios de conformidad técnica. |

##### Paquete - 9.3 Ajustes y optimizaciones

Figure 8.56: Fase - 9.3 Ajustes y optimizaciones

Se tienen las actividades destinadas a correcciones, mejoras de rendimiento y revalidaciones en la estabilidad del sistema. Busca garantizar que el producto final mantenga un comportamiento óptimo, seguro y alineado con los requerimientos del cliente.

![Página 147 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-147.png)

<!-- Página 148 del PDF original -->

Table 8.47: 9.3 Ajustes y Optimizaciones Paquete - Diccionario de la EDT

| ID | Título de Actividad o Entregable | Descripción |
| --- | --- | --- |
| 9.3.1 | Reporte de correcciones críticas | Documento que registra los errores o incidencias detectadas tras la implementación, detallando las correcciones aplicadas, su impacto y el resultado de las pruebas posteriores. Sirve como evidencia de cumplimiento y control de calidad del mantenimiento. |
| 9.3.2 | Optimizaciones de código/infraestructura | Ejecución de mejoras en el código fuente, configuraciones de entorno o arquitectura de infraestructura. Busca reducir tiempos de respuesta, optimizar recursos, mejorar la seguridad y aumentar la eficiencia operativa del sistema. |
| 9.3.3 | Reporte de retesteo de regresión | Informe que documenta las pruebas de regresión realizadas tras la aplicación de correcciones o mejoras, verificando que no se hayan introducido fallos en módulos previamente validados. Garantiza la estabilidad y funcionalidad integral del sistema tras los ajustes. |

### 8.4 Carta Gantt

La Carta Gantt del proyecto sintetiza, en un horizonte de 12 meses, el plan maestro de ejecución con sus dependencias, cargas de trabajo y puntos de control. La planificación prioriza la entrega de valor de forma incremental, habilitando ejecución en paralelo cuando es seguro hacerlo y manteniendo una línea base de alcance, plazo y costo para gestionar cambios. Los hitos H1-H8 marcan cierres formales de cada fase y sirven como compuertas (stage gates) para pasar a la siguiente etapa.

El cronograma integra actividades técnicas y de gestión: definición y validación del alcance, diseño de la arquitectura, procesos y experiencia de usuario, construcción e integración, obras e infraestructura, intervención (datos, parametría y pruebas), capacitación por roles, piloto, hypercare y estabilización, y cierre administrativo. La ruta crítica se monitorea en torno a los hitos H2 (diseño), H4 (desarrollo e integración), H5 (infraestructura) y H6 (sistema probado), que condicionan el H8 de aprobación para la etapa siguiente.

<!-- Página 149 del PDF original -->

Figure 8.57: Carta Gantt

#### 8.4.1 Inicio (H1)

La fase de Inicio establece la gobernanza, el alcance y la hoja de ruta base del proyecto. Aquí se formaliza el Acta de Constitución, se levanta y valida la problemática, se cap-

![Página 149 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-149.png)

<!-- Página 150 del PDF original -->

turan los requerimientos (funcionales y no funcionales) y se arma el plan de trabajo con su EDT, diccionario, costos (flujo/curva S), calidad (SLA), riesgos (RBS y mitigación) y proveedores/servicios externos.

El hito H1, Kick-off y plan detallado aprobado marca que el alcance quedó validado, los riesgos tienen plan de tratamiento, el cronograma base (Gantt) está publicado y existe una línea base para auditoría de cambios.

#### 8.4.2 Diseño (H2)

Diseño consolida la arquitectura de solución (lógica y física), los procesos TO-BE (BPMN, RACI y reglas de negocio) y la experiencia de usuario (design system, wireframes, prototipos y especificación funcional). Se trabaja de forma concurrente: UI evoluciona a la par del modelado de procesos y la arquitectura, con revisiones integradoras para asegurar consistencia.

El hito H2, Diseño completo aprobado implica revisión integradora ejecutada, comité de procesos aprobado, registro de observaciones resuelto y baseline de diseño cerrada; esta línea base habilita en paralelo el arranque de Desarrollo y de Obras.

→

#### 8.4.3 Desarrollo (H3 H4)

Desarrollo arranca con el setup de ambientes (Dev/QA/Cap/Prod), repositorio y dependencias, observabilidad y controles DevSecOps (SAST/DAST/gestión de secretos). Luego se ejecuta desarrollo ágil por módulos (Pacientes, Comunicación, Finanzas, Cadena de Suministro, Gestión, Inteligencia) con integraciones clave (HL7/FHIR, tributarias/financieras, dispositivos, APIs y capa de datos/BI). La documentación técnica y las pruebas automatizadas acompañan cada incremento.

H3, Ambientes de desarrollo operativos confirma que la plataforma está lista para construir y probar. H4, Desarrollo e Integración listos certifica que los módulos core cumplen criterios de aceptación, las integraciones prioritarias pasan pruebas y la documentación (manuales y catálogo de integraciones/datos) está actualizada.

#### 8.4.4 Obras Civiles y Montaje (H5)

Esta fase materializa la infraestructura física y lógica: adecuación de espacios (sala TI, canalizaciones, energía y climatización), cableado estructurado, despliegue de red/seguridad/SD- WAN, endpoints clínicos, IoT/impresión, sistemas de seguridad (control de acceso, CCTV) y configuración de plataforma (Cloud Prod + DR, edge en sedes, NOC/SOC, SIEM, WAF). Se coordina estrechamente con la arquitectura física del diseño y avanza en paralelo al desarrollo.

El hito H5, Infraestructura instalada asegura que los ambientes Dev/QA/Cap están operativos a nivel de red y plataforma, con certificaciones (enlaces, QoS/latencia) y SOPs/contingencias publicados.

<!-- Página 151 del PDF original -->

#### 8.4.5 Intervención (H6)

Intervención prepara el “aterrizaje” funcional: migración de datos maestros (inventario, limpieza/ETL y validación de calidad), parametrización (negocio, RBAC, notificaciones y SLAs) y pruebas integrales (E2E, integraciones externas, seguridad/auditoría), seguidas de performance (carga/stress/soak) y un ciclo de ajustes/optimizaciones con retesteo de regresión.

El hito H6, Sistema integrado y probado acredita que el producto cumple funcionalmente, es seguro, rinde según objetivos (p95/p99) y tiene Go/No-Go firmado para pasar a piloto.

#### 8.4.6 Capacitaciones (H7)

Se ejecuta la formación por roles (instructores internos y trabajadores), con rutas de aprendizaje y contenidos B-learning. Al finalizar, se aplican evaluaciones por rol y se emiten certificados. La fase se apalanca en H5 (ambientes disponibles) y en especificaciones cerradas de diseño.

El hito H7, Usuarios capacitados certifica que el personal clave puede operar el sistema y hay masa crítica para el piloto y el despliegue inicial.

#### 8.4.7 Puesta en Producción (H8)

La puesta en producción parte con un piloto (plan de corte/deploy, go-live y validación en terreno), seguido de hypercare con war-room y monitoreo de SLAs, luego estabilización (correcciones y ajustes de capacidad/costos), ajustes por feedback (quick wins, mejoras de UX, actualización de manuales/KB, lecciones aprendidas) y finalmente la preparación de rollout (plan multisede, ramp-up de soporte, readiness por sede).

El hito H8, Aprobación para Etapa 2 confirma que el piloto fue exitoso, el servicio está estabilizado (KPIs validados) y existe autorización para escalar a múltiples sedes.

#### 8.4.8 Finalización del Proyecto

El cierre recopila la recepción de entregables (código fuente, documentación, wiki), verifica SLA/estándares, formaliza el cierre administrativo y financiero (actas, garantías) y emite el Acta de Cierre con el estado de cumplimiento de requerimientos. Esta sección consolida la trazabilidad de la ejecución, captura las lecciones aprendidas y sella la transición ordenada hacia operación continua o hacia la siguiente etapa del programa.

<!-- Página 152 del PDF original -->

### 8.5 Plan de Implantación y Puesta en Marcha

#### 8.5.1 Objetivo del plan

Buscamos una transición ordenada, segura y controlada desde los ambientes de desarrollo hacia el ambiente de producción donde se encontrará el sistema clínico final para los usuarios, siguiendo una serie de procesos y actividades que asegurarán la continuidad del servicio y sobre todo, la calidad de la solución producida. El plan contemplará preparación de entornos y ambientes (Software y Hardware), la ejecución de estrategias de despliegue progresivo (canary y rolling updates), la validación de performance y resiliencia, y la definición de procedimientos de rollback ante fallas críticas.

Fases de la implantación: 1 - Preparación de Ambientes y Orquestación, 2 - Despliegue Controlado (Canary y Rolling Updates), 3 - Pruebas de Aceptación, Rendimiento y Resiliencia, 4 - Marcha Blanca y Puesta en Producción, 5 - Estabilización, Monitoreo y Rollback.

#### 8.5.2 1 - Preparación de Ambientes y Orquestación:

En esta primera fase del plan de implantación, nos preocuparemos por la preparación de todos los sistemas físicos necesarios para trabajar con el Software propuesto, preparación de dependencias y sistemas digitales necesarios para el desarrollo del producto, además de la preparación de ambientes para todas las fases del proyecto.

##### Configuración de red y seguridad:(3 semanas)

- Configuración de VPN y ambientes(Dev, QA y Prod)

- Definición de ACL para dispositivos permitidos en el sistema y segmentados por ambiente

- Configuración de balanceador(es) de carga

- Configuraciónes de Servidores, orquestadores y Datacenter para centro clínico en Providencia

- Configuraciones de repositorios y dependencias

- Preparación de rollouts y AWS Backup (para prevención de errores)

- Configuraciónes de red y seguridad, túneles entre dispositivos y protocolos.

- Pruebas de conectividad, seguridad, rendimiento y restauración de datos (backups)

##### Criterios de aceptación y éxito de la fase:

- Todos los ambientes (Dev, QA y Prod) operativos y aislados

- 100% de los secretos gestionados fuera del código fuente

<!-- Página 153 del PDF original -->

- Backups automáticos validados y restauración probada

- Monitoreo en tiempo real activo y alarmas configuradas

- Pruebas de transferencia de archivos y comunicación seguras aprobadas

- pruebas de rendimiento cumplen con SLA’s esablecidos

- Integridad de datos cumple con SLA’s establecidos

Esta primera fase constituye la base técnica del proyecto. De su correcta ejecución dependerá la estabilidad, seguridad y trazabilidad del sistema durante las fases posteriores. Los ambientes preparados, junto con la orquestación y el pipeline automatizado, permitirán aplicar de manera segura las estrategias de despliegue Canary y Rolling Updates, y ejecutar pruebas de resiliencia bajo observabilidad completa.

#### 8.5.3 2 - Despliegue Controlado (Canary y Rolling Updates):(2 semanas)

Una vez de ya preparado todo el ambiente y todas las configuraciones del sistema, continuaremos con el despliegue controlado, minimizado, progresivo y seguro para los microservicios, garantizando la continuidad operativa, el cumplimiento de los SLA definidos y la posibilidad de revertir versiones sin interrupciones del servicio clínico. Esta fase combina tres estrategias de despliegue (Canary y Rolling Updates) dentro del pipeline CI/CD, dependiendo del nivel de criticidad del servicio, la frecuencia de cambio y la sensibilidad de los datos médicos.

Para realizar un trabajo siguiendo las prácticas de Canary deployment:

- Se liberará una nueva versión de un microservicio solo a un pequeño porcentaje de usuarios o peticiones, evaluando métricas de rendimiento y estabilidad antes de expandir el despliegue al 100%

- Desplegar la nueva versión en un subconjunto de instancias (por ejemplo, 10% del tráfico)

- Monitorear intensivamente métricas críticas durante 24 horas.

- Si las métricas se mantienen dentro del umbral durante un período definido (ej. 1 hora de tráfico estable):

Para lograr Rolling Update actualizaremos gradualmente cada instancia de un microservicio, reemplazando contenedores antiguos por nuevos dentro del mismo entorno, para no tener interrupciones totales del servicio.

- Reemplazar instancias una a una (máximo 1/3 simultáneamente).

- Mantener balance de carga activo durante el proceso.

- Validar salud de cada nueva instancia antes de continuar con la siguiente.

- Confirmar estabilidad general del servicio.

##### Criterios de aceptación(SLA’s) y éxito de la fase:

- Uptime del entorno durante despliegue mayor a 99.97%

- Latencia promedio p95 menor a 250 ms

<!-- Página 154 del PDF original -->

- Tasa de error (HTTP 5xx) menor a 1%

- Tiempo total de reversión menor a 5 min

Luego de esto se garantizará una implantación continua, trazable y reversible, alineada con las mejores prácticas DevSecOps y los principios de alta disponibilidad requeridos por la solución de salud. Usar estrategias Canary y Rolling Updates permite mantener el sistema operativo 24/7 mientras se actualizan componentes críticos, reduciendo el riesgo operativo y asegurando un despliegue controlado, medible y auditable.

#### 8.5.4 3 - Pruebas de Aceptación, Rendimiento y Resiliencia:

Validar, en entornos pre-producción y QA controlada, que la solución cumple funcionalmente, alcanza el rendimiento exigido por los SLA y SLO definidos tanto por el cliente como por la empresa oferente respectivamente, si resiste condiciones extremas (stress) y mantiene la continuidad ante fallas inyectadas, con criterios de salida claros y trazables a los SLA/SLO y presupuestos.

Tipos de pruebas para evaluar cumplimiento de SLA’s por parte del sistema:

- UAT - Aceptación de Usuario: Definir backlog de casos UAT por módulos (Finanzas, Paciente, HCE, etc.), Preparar datasets de prueba y ambientes de producción, ejecutar UAT con guiones y evidencia consolidando observaciones y tasa de aprobación.

- Integrales E2E e Integraciones: Validación de ruta completa de procesos de pago, comunicación, facturación, ingreso de datos, etc., de extremo a extremo, buscando mas de un 95% de los casos exitosos y que cumplan con la integridad.

- Seguridad y Auditoría: Verificar resistencia a vulnerabilidades, cumplimiento de acceso/rastreo y políticas de seguridad, estandares y normas ISO prometidas, SLA’s, integridad de datos y disponibilidad, mediante pruebas DDoS y defacement.

- Performance - Carga: Asegurar tiempos de respuesta y throughput bajo carga representativa, documentar capacidad de las condiciones a las que se someta el sistema y comparar luego con SLA’s esperados por parte de la empresa contratante.

- Stress y Soak: Encontrar límites/picos y estabilidad en corridas larga, estresando al sistema con tráfico alto, altos volumenes de datos y usuarios, casos excepcionales, casos extremos y casos particulares.

La ejecución integral de las pruebas de aceptación, rendimiento y resiliencia constituye la validación final del sistema antes de su paso a producción. Los resultados obtenidos en esta fase permitirán comprobar objetivamente que la plataforma cumple los criterios funcionales, de desempeño y de tolerancia a fallas definidos en los SLA/SLO, garantizando que cada microservicio opere de manera estable, segura y eficiente bajo

<!-- Página 155 del PDF original -->

condiciones reales de carga. Asimismo, el proceso de verificación y ajuste continuo fortalecerá la confiabilidad del entorno antes de la marcha blanca, reduciendo riesgos operativos y asegurando una transición controlada hacia la operación productiva del sistema médico.

#### 8.5.5 4 - Marcha Blanca y Puesta en Producción:

Buscamos en este punto el paso controlado a producción de la solución, garantizando la estabilidad operacional, la continuidad de los servicios clínicos y la satisfacción de los usuarios finales, luego de verificar todo en ambientes previos y bajo pruebas exhaustivas. Durante esta fase se monitorea el comportamiento real del sistema, se validan los acuerdos de nivel de servicio (SLA/SLO) y se corrigen desviaciones detectadas en un entorno de tráfico limitado conocido como marcha blanca, antes de declarar el sistema en plena operación.

1. Detalle de actividades para Go-Live:(5 dias)

##### Revisión de checklist previo a producción:

1. Validación de backups recientes (Aurora PostgreSQL y DocumentDB)

2. Confirmación de estado del entorno Canary y del API Gateway activo

3. Verificación de disponibilidad de balanceadores (ALB) y certificados SSL vigentes

4. Validación del monitoreo, métricas y alertas configuradas (CloudWatch, Grafana)

##### Comunicación del hito a stakeholders:

1. Aviso formal a dirección TI, usuarios clave y mesa de ayuda

2. Confirmación del horario de ejecución y ventana de observación

##### Autorización de “Go” por comité:

1. Revisión de reportes de Fase 3 (UAT, performance, seguridad)

2. Firma del acta de paso a producción.

2. Ejecución de la Marcha Blanca (10 - 15 dias)

##### Activación del entorno Canary:

- Redirección parcial o completa del tráfico a Canary

- Habilitación progresiva de módulos críticos

##### Monitoreo intensivo del servicio:

- Uptime mayor a 99.97%.

- Latencia promedio menor a 250 ms.

- Tasa de error (HTTP 5xx) menor a 1 %.

- Tasa de éxito en transacciones mayor a 98

<!-- Página 156 del PDF original -->

##### Atención temprana de incidencias:

- Canal directo de soporte

- Registro y priorización de incidentes.

- Aplicación de correcciones menores sin reinicio completo (hotfix).

##### Validación funcional con usuarios finales:

- Pruebas en vivo con médicos, administrativos y personal de soporte.

- Registro de feedback en checklist UAT extendido.

Criterios de aceptación de la fase: Disponibilidad mayora 99.97%, Latencia promedio (p95) menor a 250 ms, Errores HTTP 5xx menor a 1 %, RTO (tiempo de recuperación) menora 30 min, RPO (perdida máximade datos) menos de 15 minutos y UAT mayor a 90

La marcha blanca representa la validación definitiva del sistema en condiciones reales de operación. Durante este periodo, se comprueba la estabilidad técnica, la confiabilidad del rendimiento y la adecuada adopción por parte de los usuarios. El monitoreo continuo, la gestión proactiva de incidencias y el acompañamiento comunicacional garantizan una puesta en producción sin interrupciones, consolidando la madurez operativa de la plataforma. Al finalizar esta fase, el sistema estará en condiciones de pasar a la operación estable y mantenimiento continuo (Fase 5), con respaldo validado y trazabilidad completa de los resultados obtenidos.

#### 8.5.6 5 - Estabilización, Monitoreo y Rollback:

Consolidar la operación del sistema en producción asegurando su estabilidad, confiabilidad, seguridad y cumplimiento de los SLA/SLO establecidos. Durante esta fase se implementan prácticas de observabilidad continua, monitoreo avanzado, mantenimiento preventivo y procesos formales de rollback y post-mortem para garantizar la resiliencia operativa de la plataforma.

##### Actividades de la fase: Monitoreo y Observabilidad Integral: Métricas y telemetría en producción:

1. Implementación definitiva de dashboards en Grafana, alimentados desde Prometheus

y AWS CloudWatch.

2. Monitoreo de métricas técnicas (SLA’s) y de negocio.

##### Trazabilidad distribuida:

1. Uso de CloudWatch para seguimiento entre microservicios.

2. Registro centralizado de logs en ELK Stack (Elasticsearch, Logstash, Kibana) con

retención de 180 días.

##### Alertas inteligentes:

<!-- Página 157 del PDF original -->

1. Configuración de umbrales dinámicos basados en tendencia (AI/ML en Cloud-

Watch Anomaly Detection).

2. Envío de alertas a canales Slack/MS Teams y correo del NOC/SOC.

##### Panel de estado del servicio:

1. Publicación interna de un Service Health Dashboard con métricas SLA y alertas

activas.

##### Mantenimiento Preventivo y Gestión de Incidentes Plan de mantenimiento preventivo:

1. Actualización de parches de seguridad del sistema operativo y librerías (trimes-

tral).

2. Verificación mensual de integridad de backups (restauración controlada).

3. Optimización de índices y limpieza de bases de datos Aurora y DocumentDB.

4. Validación de certificados SSL y renovaciones automáticas (AWS ACM).

##### Gestión de incidentes:

1. Clasificación por severidad (Alto, Medio, Bajo).

2. Reuniones de revisión semanal de incidentes (SRE Review).

##### Rollback, Recuperación y Resiliencia Procedimiento de rollback planificado:

1. Activación automática desde el pipeline CI/CD si el sistema excede los umbrales

de error definidos (mas de 2% de errores o degradación mayor a 20%)

2. Redirección del tráfico al entorno Canary

3. Restauración de snapshots recientes de Aurora PostgreSQL y DocumentDB desde

AWS Backup

4. Validación post-rollback con pruebas automáticas

##### Criterios de exito de la fase:

- Cumplimiento sostenido de SLA/SLO durante al menos 30 días consecutivos sin parar

- 100% de los incidentes registrados con resolución al menos documentada

- Ningún incidente crítico sin plan de acción aprobado

- Auditorías internas y externas sin hallazgos mayores.

- Activación de procesos de mejora continua y documentación actualizada en Confluence.

El monitoreo continuo, las políticas de mantenimiento preventivo y los mecanismos de rollback rápido consolidan la madurez operativa alcanzada durante las fases anteriores. Al finalizar este periodo, la plataforma se considera plenamente operativa y autosostenible, con métricas verificadas, procesos de mejora continua establecidos y

<!-- Página 158 del PDF original -->

respaldo documental para auditorías técnicas y regulatorias. Con esta fase se cierra el ciclo de implantación, garantizando que la solución cumple las condiciones técnicas, normativas y de servicio exigidas por el mandante y los usuarios finales del sistema clínico.

<!-- Página 159 del PDF original -->

## 9 Plan de Riesgo

### 9.1 Metricas

#### 9.1.1 Criterios de evaluación

La evaluación cualitativa emplea tres métricas: probabilidad, impacto y prioridad. La prioridad resulta de combinar probabilidad e impacto según la matriz institucional del proyecto.

##### a) Probabilidad (P)

Corresponde al grado de posibilidad de que un riesgo ocurra durante el ciclo de vida del proyecto. La valoración se realiza en una escala de 1 a 5, según la Tabla 9.1, donde 1 representa una probabilidad muy baja y 5 una probabilidad muy alta.

Table 9.1: Escala de Probabilidad

| Valor | Descripción | Criterio cualitativo |
| --- | --- | --- |
| 1 | Muy baja | Poco probable que ocurra; condiciones excepcionales. |
| 2 | Baja | Puede ocurrir en casos aislados. |
| 3 | Media | Podría ocurrir algunas veces durante el proyecto. |
| 4 | Alta | Ocurrirá con frecuencia si no se mitiga. |
| 5 | Muy alta | Casi seguro que ocurra. |

##### b) Impacto (I)

Representa el nivel de afectación que tendría el riesgo si llegara a materializarse. Se evalúa también en una escala de 1 a 5, según la Tabla 9.2, donde 1 indica un impacto insignificante y 5 un impacto muy alto.

<!-- Página 160 del PDF original -->

Table 9.2: Escala de Impacto

| Valor | Descripción | Criterio cualitativo |
| --- | --- | --- |
| 1 | Insignificante | Sin impacto perceptible en el proyecto. |
| 2 | Menor | Afectación leve, fácilmente controlable. |
| 3 | Moderado | Impacto parcial en entregables o plazos. |
| 4 | Alto | Afecta hitos principales o desempeño general. |
| 5 | Muy alto | Compromete el éxito total del proyecto. |

##### c) Determinación de la Prioridad (P×I)

Una vez definidos los valores de Probabilidad (P) e Impacto (I), se obtiene el producto 𝑃 × 𝐼

, que refleja el nivel de prioridad del riesgo. El resultado se interpreta conforme a la Tabla 9.3, la cual clasifica los riesgos según su importancia relativa.

Table 9.3: Matriz de Prioridad (Probabilidad × Impacto)

| P×I | Nivel de Prioridad |
| --- | --- |
| 1 - 4 | Baja |
| 5 - 9 | Media |
| 10 - 16 | Alta |
| 17 - 25 | Crítica |

#### 9.1.2 Tipos de respuesta

Para responder a los riesgos que pueda presentar el proyecto, se utilizarán las siguientes acciones:

- Escalar: Se realiza cuando un riesgo se encuentra fuera del alcance del proyecto o excede la autoridad del director de proyecto.

- Evitar: Se realiza para eliminar la amenaza o proteger al proyecto de su impacto.

- Transferir: Se realiza para cambiar la titularidad de una amenaza a un tercero, para que él maneje el riesgo y soporte el impacto que produce la amenaza.

- Mitigar: Tomar medidas para reducir la probabilidad de ocurrencia y/o impacto de un riesgo.

- Aceptar: Reconocer la existencia de una amenaza, pero no se toman medidas proactivas, sino que se acepta que ocurrirá.

### 9.2 Categorías de Riesgos

Los riesgos se clasifican en: Riesgos de la Solución (RS), Riesgos de Desarrollo (RD) y Riesgos de Implantación (RI).

<!-- Página 161 del PDF original -->

#### 9.2.1 Resumen de los riesgos identificados

Figure 9.1: Diagrama RBS

A continuación, se muestra el conjunto completo de Riesgos del proyecto. Se comienza con una tabla que incluye su nombre, descripción e identificador para garantizar su rastreabilidad en el registro de riesgos. Más adelante, se incorpora la evaluación cualitativa de su criticidad y priorización mediante la matriz Probabilidad × Impacto. Por último, se presenta el plan de respuesta relacionado con las estrategias definidas en el marco de gestión de riesgos: Evitar, escalar, mitigar, aceptar y transferir. Estas categorías posibilitan la definición de un tratamiento que sea congruente con el nivel de peligro y aseguran una administración integral a lo largo de todo el ciclo vital del proyecto.

#### 9.2.2 Riesgos de la Solución (RS)

##### Descripción de riesgos de la solución

| ID | Riesgo | Descripción |
| --- | --- | --- |
| RS-01 | Brecha de seguridad o ciberataque | Intrusión, ransomware o exfiltración de datos clínicos por vulnerabilidades. |
| RS-02 | Pérdida de datos por fallo de respaldo | Copias incompletas/corruptas o errores en restauración. |

![Página 161 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-161.png)

<!-- Página 162 del PDF original -->

| RS-03 | Obsolescencia tecnológica | Desuso de frameworks/librerías clave que elevan la deuda técnica. |
| --- | --- | --- |
| RS-04 | Vendor lock-in con servicios cloud | Dependencia fuerte de un proveedor limita portabilidad y negociación. |
| RS-05 | Falla de interoperabilidad HL7/FHIR | Cambios de versión, mapeos erróneos o incompatibilidad con terceros. |
| RS-06 | Degradación de rendimiento/disponibilidad | Latencia y caídas por sobrecarga de microservicios/APIs. |
| RS-07 | Vulnerabilidades en API Gateway | Rutas expuestas, tokens inseguros o políticas laxas. |
| RS-08 | Corrupción de base de datos | Inconsistencias por fallos en transacciones/replicación. |
| RS-09 | Incumplimiento ISO 27001/NIST | Controles ausentes o evidencia insuficiente en auditorías. |
| RS-10 | Resiliencia insuficiente ante fallas encadenadas | Cascadas por dependencias entre servicios. |
| RS-11 | Ataques DDoS | Saturación voluntaria de endpoints públicos. |
| RS-12 | Fallas en autoescalado | Reglas inadecuadas de escalamiento horizontal/vertical. |
| RS-13 | Pérdida de trazabilidad clínica | Falta de logs inmutables o auditorías incompletas. |
| RS-14 | Fallas en analítica/BI | Pipelines/ dashboards con datos incompletos o retrasados. |
| RS-15 | Vulnerabilidad en servicios de terceros | Brechas en pasarelas de pago/identidad/servicios clínicos externos. |
| RS-16 | Falla en auditoría clínica por registros incompletos | Auditoría clínica o peritajes no pueden reconstruir completamente la historia clínica por falta de logs o registros. |
| RS-17 | Sesgos en modelos de analítica usados para decisiones clínicas | Modelos de analítica o BI generan sesgos por datos de entrenamiento incompletos o no representativos, afectando indicadores clínicos. |
| RS-18 | Mala clasificación de documentos clínicos (OCR/etiquetado) | Errores en OCR o etiquetado automático generan documentos mal clasificados o extraviados en el repositorio clínico. |
| RS-19 | Fallas en encriptación de datos en tránsito entre microservicios | Tráfico interno entre servicios viaja sin cifrado robusto, exponiendo datos sensibles ante interceptación o sniffing. |
| RS-20 | Saturación del sistema por campañas preventivas o picos de demanda | Picos de uso (campañas, contingencias sanitarias) superan la capacidad prevista y provocan lentitud o caídas del sistema. |
| RS-21 | Interoperabilidad de sistemas HL7/FHIR | Errores o incompatibilidades en la comunicación entre sistemas por mala definición de estándares HL7 y FHIR |

<!-- Página 163 del PDF original -->

##### Análisis cualitativo - RS

| ID | Riesgo | P | I | Nivel | Clasificación |
| --- | --- | --- | --- | --- | --- |
| RS-01 | Brecha de seguridad o ciberataque | 4 | 5 | 20 | Crítico |
| RS-02 | Pérdida de datos por fallas de respaldo | 3 | 5 | 15 | Alto |
| RS-03 | Obsolescencia tecnológica | 3 | 3 | 9 | Medio |
| RS-04 | Dependencia de proveedor (vendor lock-in) | 3 | 3 | 9 | Medio |
| RS-05 | Falla de interoperabilidad HL7/FHIR | 2 | 5 | 10 | Medio-Alto |
| RS-06 | Caída del servicio / baja disponibilidad | 4 | 4 | 16 | Crítico |
| RS-07 | Vulnerabilidades en API Gateway | 4 | 5 | 20 | Crítico |
| RS-08 | Corrupción de base de datos | 3 | 5 | 15 | Alto |
| RS-09 | Incumplimiento de normativas (ISO 27001, NIST, MINSAL) | 3 | 4 | 12 | Alto |
| RS-10 | Falla de resiliencia ante fallas encadenadas | 3 | 4 | 12 | Alto |
| RS-11 | Ataques DDoS | 3 | 4 | 12 | Alto |
| RS-12 | Falla en autoescalado / balanceo | 3 | 4 | 12 | Alto |
| RS-13 | Pérdida de trazabilidad clínica | 3 | 5 | 15 | Alto |
| RS-14 | Fallas en analítica y BI | 2 | 3 | 6 | Medio |
| RS-15 | Vulnerabilidades en servicios de terceros | 3 | 4 | 12 | Alto |
| RS-16 | Falla en auditoría clínica por registros incompletos | 3 | 4 | 12 | Alta |
| RS-17 | Sesgos en modelos de analítica usados para decisiones clínicas | 2 | 4 | 8 | Media |
| RS-18 | Mala clasificación de documentos clínicos (OCR/etiquetado) | 3 | 3 | 9 | Media |
| RS-19 | Fallas en encriptación de datos en tránsito entre microservicios | 2 | 5 | 10 | Alta |
| RS-20 | Saturación del sistema por campañas preventivas o picos de demanda | 3 | 4 | 12 | Alta |

Table 9.4: Evaluación de Riesgos de la Solución (RS)

##### Plan de respuesta - RS

| ID | Riesgo | Prioridad | Acción | Acción de respuesta | Responsable |
| --- | --- | --- | --- | --- | --- |
| RS-01 | Brecha de seguridad | Alta | Mitigar | Implementar WAF, SIEM, EDR, MFA y hardening | Jefe de Ciberseguridad |
| RS-02 | Pérdida de datos | Alta | Mitigar | Backups automáticos, rotación y pruebas de restauración | Adm. Base de Datos |

<!-- Página 164 del PDF original -->

| RS-03 | Obsolescencia tecnológica | Media | Mitigar | Roadmap de upgrades LTS y política de versiones | Arq. de Software |
| --- | --- | --- | --- | --- | --- |
| RS-04 | Vendor lock-in | Alta | Evitar | Diseño portable (contenedores/IaC) y alternativas equivalentes | Arq. de Solución |
| RS-05 | Interoperabilidad HL7/FHIR | Alta | Mitigar | Contratos de interfaz, versionado y pruebas de integración | Líder Integración |
| RS-06 | Rendimiento/ disponibilidad | Alta | Mitigar | APM, caching, tuning y escalamiento automático | Líder DevOps |
| RS-07 | API Gateway vulnerable | Alta | Mitigar | OWASP, DAST, políticas Zero Trust y rotación de secretos | Arq. Seguridad |
| RS-08 | Corrupción de BD | Alta | Mitigar | Transacciones ACID, réplica síncrona y verificación de integridad | DBA Líder |
| RS-09 | Incumplimiento ISO/NIST | Alta | Mitigar | Auditorías internas, SGSI, gestión de evidencias | Responsable Calidad |
| RS-10 | Resiliencia insuficiente | Alta | Mitigar | Patrón circuit breaker, colas y timeouts, DR activo | DevOps Principal |
| RS-11 | DDoS | Alta | Transferir | CDN, rate limiting y protección anti-DDoS del proveedor | Arq. Red/Cloud |
| RS-12 | Autoescalado deficiente | Media | Mitigar | Reglas de HPA/RPS/CPU, pruebas de estrés periódicas | SRE |
| RS-13 | Trazabilidad clínica | Alta | Mitigar | Logs inmutables, retención extendida, firma de auditoría | Jefe Seguridad TI |
| RS-14 | Analítica/BI | Media | Mitigar | Control de calidad de datos y orquestación ETL/ELT | Líder BI |
| RS-15 | Terceros vulnerables | Alta | Transferir | Evaluación de proveedores, pen-tests y cláusulas de SLA | Gerente de Proveedores |
| RS-16 | Falla en auditoría clínica por registros incompletos | Alta | Mitigar | Endurecer políticas de logging, retención y verificación periódica de logs clínicos. | Jefe de Seguridad TI |
| RS-17 | Sesgos en modelos de analítica usados para decisiones clínicas | Media | Mitigar | Revisar datasets, aplicar validaciones clínicas y limitar analítica a apoyo, no decisión automática. | Líder de Analítica / BI |
| RS-18 | Mala clasificación de documentos clínicos (OCR/etiquetado) | Media | Mitigar | Realizar pruebas de precisión, revisión manual por muestreo y doble validación en documentos críticos. | Jefe de Archivo Clínico |
| RS-19 | Fallas en encriptación de datos en tránsito entre microservicios | Alta | Evitar | Forzar TLS mutuo interno, aplicar políticas de seguridad en la malla de servicios y escanear configuración periódicamente. | Arquitecto de Seguridad |

<!-- Página 165 del PDF original -->

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| RS-20 | Saturación del sistema por campañas preventivas o picos de demanda | Alta | Mitigar | Configurar autoescalado conservador, ejecutar pruebas de estrés y planificar capacidad con el mandante. | SRE / Infraestructura |

##### Plan de contingencia - RS

| ID | Riesgo | Acción de contingencia |
| --- | --- | --- |
| RS-01 | Brecha de seguridad | Aislar segmentos, activar IRP, restaurar servicios desde backups verificados. |
| RS-02 | Pérdida de datos | Ejecutar DRP y restauración punto-en-tiempo; validación de integridad. |
| RS-03 | Obsolescencia tecnológica | Congelar nuevas features y priorizar actualización crítica. |
| RS-04 | Vendor lock-in | Failover temporal a servicios equivalentes y plan de migración. |
| RS-05 | Interoperabilidad | Activar mapeos alternativos y colas diferidas; notificar a terceros. |
| RS-06 | Rendimiento/disponibilidad | Desviar tráfico, degradar funcionalidad no crítica y escalar nodos. |
| RS-07 | API Gateway vulnerable | Cerrar endpoints, rotar credenciales y parchar reglas. |
| RS-08 | Corrupción de BD | Conmutar a réplica sana y reprocesar transacciones. |
| RS-09 | Incumplimiento ISO/NIST | Emisión de acción correctiva y auditoría extraordinaria. |
| RS-10 | Resiliencia insuficiente | Activar modo degradado y redistribuir cargas. |
| RS-11 | DDoS | Filtrado de origen, scrubbing center y listas de bloqueo. |
| RS-12 | Autoescalado deficiente | Aplicar escalamiento manual y ventanas de mantenimiento. |
| RS-13 | Trazabilidad clínica | Recuperar logs firmados y reconstruir auditoría. |
| RS-14 | Analítica/BI | Reconstruir datasets y publicar reporte provisorio. |
| RS-15 | Terceros vulnerables | Cortar integración y activar proveedor alterno/backup. |
| RS-16 | Falla en auditoría clínica por registros incompletos | Reconstruir trazas desde respaldos, activar registro manual temporal y priorizar corrección de fallas de logging. |
| RS-17 | Sesgos en modelos de analítica usados para decisiones clínicas | Deshabilitar temporalmente reportes afectados y apoyar decisiones únicamente en criterios clínicos y datos validados. |
| RS-18 | Mala clasificación de documentos clínicos (OCR/etiquetado) | Habilitar proceso manual de reclasificación priorizando documentos críticos y usar búsquedas avanzadas para localizar archivos. |

<!-- Página 166 del PDF original -->

| RS-19 | Fallas en encriptación de datos en tránsito entre microservicios | Forzar túneles seguros alternativos (VPN interna), limitar accesos y rotar certificados/llaves comprometidos. |
| --- | --- | --- |
| RS-20 | Saturación del sistema por campañas preventivas o picos de demanda | Activar modo degradado, priorizar funcionalidades críticas y derivar atenciones a canales alternativos mientras se escala capacidad. |

#### 9.2.3 Riesgos de Desarrollo (RD)

##### Tabla de riesgos de desarrollo

| ID | Riesgo | Descripción |
| --- | --- | --- |
| RD-01 | Retrasos en integración | Desfase entre módulos/equipos que afecta el cronograma. |
| RD-02 | Fallas en pipelines CI/CD | Interrupciones por errores de configuración o dependencias. |
| RD-03 | Baja cobertura de pruebas | Insuficiente validación unitaria/funcional/regresión. |
| RD-04 | Fuga de conocimiento | Rotación de personal clave sin traspaso. |
| RD-05 | Falta de prácticas DevSecOps | Ausencia de SAST/DAST y políticas de código seguro. |
| RD-06 | Subestimación de tiempos | Planificación optimista y buffers insuficientes. |
| RD-07 | Complejidad arquitectónica | Sobrediseño y acoplamiento innecesario. |
| RD-08 | Comunicación deficiente | Descoordinación entre squads/áreas. |
| RD-09 | Deuda técnica acumulada | Postergación de refactorizaciones y controles de calidad. |
| RD-10 | Integración con APIs externas | Cambios no versionados/latencias de terceros. |
| RD-11 | Dependencias no actualizadas en repositorios (librerías vulnerables) | Uso de librerías o paquetes con vulnerabilidades conocidas que no se actualizan oportunamente. |
| RD-12 | Errores en manejo de versiones (branching y releases) | Mala gestión de ramas y releases provoca conflictos, regresiones o despliegues con código incorrecto. |
| RD-13 | Incompatibilidades entre entornos por mala configuración de IaC | Scripts de infraestructura como código mal parametrizados generan diferencias entre desarrollo, QA y producción. |
| RD-14 | Fallas en pruebas de regresión automatizadas | La suite de regresión no cubre cambios recientes y permite que se introduzcan errores en funcionalidades ya liberadas. |
| RD-15 | Desalineación UI/UX con flujos y requisitos clínicos | Diseños de interfaz no alineados con flujos clínicos reales generan errores de uso y resistencia de los usuarios. |

<!-- Página 167 del PDF original -->

##### Análisis cualitativo - RD

| ID | Riesgo | P | I | Nivel | Clasificación |
| --- | --- | --- | --- | --- | --- |
| RD-01 | Retrasos en integración | 4 | 3 | 12 | Alto |
| RD-02 | Fallas en pipelines CI/CD | 3 | 3 | 9 | Medio |
| RD-03 | Baja cobertura de pruebas automatizadas | 3 | 4 | 12 | Alto |
| RD-04 | Fuga de conocimiento del equipo técnico | 3 | 4 | 12 | Alto |
| RD-05 | Falta de prácticas DevSecOps | 3 | 4 | 12 | Alto |
| RD-06 | Subestimación de tiempos / mala estimación | 4 | 3 | 12 | Alto |
| RD-07 | Complejidad arquitectónica | 3 | 4 | 12 | Alto |
| RD-08 | Comunicación deficiente entre equipos | 3 | 3 | 9 | Medio |
| RD-09 | Deuda técnica acumulada | 3 | 4 | 12 | Alto |
| RD-10 | Integración con APIs externas inestables | 3 | 4 | 12 | Alto |
| RD-11 | Dependencias no actualizadas en repositorios (librerías vulnerables) | 3 | 4 | 12 | Alta |
| RD-12 | Errores en manejo de versiones (branching y releases) | 3 | 3 | 9 | Media |
| RD-13 | Incompatibilidades entre entornos por mala configuración de IaC | 2 | 4 | 8 | Media |
| RD-14 | Fallas en pruebas de regresión automatizadas | 3 | 4 | 12 | Alta |
| RD-15 | Desalineación UI/UX con flujos y requisitos clínicos | 2 | 4 | 8 | Media |

Table 9.5: Evaluación de Riesgos del Desarrollo (RD)

##### Plan de respuesta - RD

| ID | Riesgo | Prioridad | Acción | Acción de respuesta | Responsable |
| --- | --- | --- | --- | --- | --- |
| RD-01 | Retrasos en integración | Alta | Mitigar | PI de integración, contratos de interfaz y branch strategy | Líder Proyecto |
| RD-02 | Fallas en CI/CD | Alta | Mitigar | Gates de calidad, pruebas automáticas y entornos efímeros | DevOps Principal |
| RD-03 | Baja cobertura de pruebas | Alta | Mitigar | Meta &gt;90% en código crítico, Test Pyramid y regresión nocturna | QA Lead |
| RD-04 | Fuga de conocimiento | Alta | Mitigar | Documentación viva, pair programming y rotación cruzada | PMO / Tech Lead |
| RD-05 | Falta de DevSecOps | Alta | Mitigar | SAST/DAST, secrets scanning y política de dependencias | Arq. Seguridad |
| RD-06 | Subestimación de tiempos | Alta | Mitigar | Buffers por épica, burn-down semanal y re-forecast ágil | Scrum Master |

<!-- Página 168 del PDF original -->

| RD-07 | Complejidad arquitectónica | Media | Mitigar | ADRs, revisión de arquitectura y simplificación de dominios | Arq. de Software |
| --- | --- | --- | --- | --- | --- |
| RD-08 | Comunicación deficiente | Media | Mitigar | Ceremonias sincronizadas, matriz RACI y tablero único | Líder Proyecto |
| RD-09 | Deuda técnica acumulada | Media | Mitigar | Sprint hardening trimestral y políticas SonarQube | Tech Lead |
| RD-10 | Integración APIs externas | Media | Mitigar | Versionado, timeouts y circuit breakers; sandbox de terceros | Líder Integración |
| RD-11 | Dependencias no actualizadas en repositorios (librerías vulnerables) | Alta | Mitigar | Definir política de actualización periódica, escáner de dependencias y bloqueo de versiones con CVE críticas. | Líder DevSecOps |
| RD-12 | Errores en manejo de versiones (branching y releases) | Media | Mitigar | Adoptar flujo GitFlow/GitHub Flow, proteger ramas principales y definir checklist de releases. | Líder de Desarrollo |
| RD-13 | Incompatibilidades entre entornos por mala configuración de IaC | Media | Mitigar | Revisar código IaC, estandarizar parámetros y probar despliegues en entorno espejo. | Arquitecto de Infraestructura |
| RD-14 | Fallas en pruebas de regresión automatizadas | Alta | Mitigar | Mantener y ampliar la suite de regresión, ejecuciones nocturnas y cobertura mínima para módulos críticos. | Líder QA |
| RD-15 | Desalineación UI/UX con flujos y requisitos clínicos | Media | Mitigar | Realizar talleres con usuarios clínicos, prototipos navegables y validación temprana de pantallas. | UX Lead / Jefe Funcional |

##### Plan de contingencia - RD

| ID | Riesgo | Acción de contingencia |
| --- | --- | --- |
| RD-01 | Retrasos en integración | Activar sprint buffer, replanificar dependencias y reforzar equipo. |
| RD-02 | Fallas en CI/CD | Despliegue manual controlado y rollback a versión estable. |
| RD-03 | Baja cobertura de pruebas | Congelar liberación y completar baterías mínimas de QA. |
| RD-04 | Fuga de conocimiento | Incorporar consultor temporal y sesiones de transferencia. |
| RD-05 | Falta de DevSecOps | Auditoría urgente, corrección prioritaria y hotfix de seguridad. |

<!-- Página 169 del PDF original -->

| RD-06 | Subestimación de tiempos | Recalcular ruta crítica y extender sprint de ser necesario. |
| --- | --- | --- |
| RD-07 | Complejidad arquitectónica | Desacoplar módulos críticos y aplazar features no esenciales. |
| RD-08 | Comunicación deficiente | War room diario, agenda única y decisiones documentadas. |
| RD-09 | Deuda técnica acumulada | Programar refactor rápido orientado a riesgos y performance. |
| RD-10 | Integración APIs externas | Fallback a colas diferidas y desactivar features no esenciales. |
| RD-11 | Dependencias no actualizadas en repositorios (librerías vulnerables) | Aplicar parches de emergencia, bloquear despliegues con dependencias vulnerables y habilitar workarounds temporales. |
| RD-12 | Errores en manejo de versiones (branching y releases) | Ejecutar rollback a la versión estable anterior y congelar cambios hasta normalizar el esquema de ramas y releases. |
| RD-13 | Incompatibilidades entre entornos por mala configuración de IaC | Restaurar configuración conocida como estable e implementar despliegue manual temporal controlado. |
| RD-14 | Fallas en pruebas de regresión automatizadas | Aplicar batería de pruebas manuales priorizadas sobre funcionalidades críticas antes de nuevos despliegues. |
| RD-15 | Desalineación UI/UX con flujos y requisitos clínicos | Habilitar formularios o flujos alternativos simplificados y apoyo presencial a usuarios hasta ajustar la interfaz. |

#### 9.2.4 Riesgos de Implantación (RI)

##### Tabla de riesgos de implantación

| ID | Riesgo | Descripción |
| --- | --- | --- |
| RI-01 | Fallas en despliegue productivo | Errores de IaC/orquestación durante el go-live. |
| RI-02 | Incompatibilidad con hardware biomédico | Dispositivos/firmware no homologados. |
| RI-03 | Pérdida de datos en migración | Fallas en mapeo/validación de historiales. |
| RI-04 | Falta de adopción del personal médico | Resistencia al cambio y curva de aprendizaje. |
| RI-05 | Sincronización inconsistente entre sedes | Problemas de red/colas que afectan consistencia. |
| RI-06 | Incumplimiento de SLA | Caídas o latencias superiores a lo comprometido. |
| RI-07 | Soporte insuficiente post go-live | Capacidad de mesa de ayuda inadecuada. |
| RI-08 | Pérdida de trazabilidad clínica | Auditoría incompleta tras el despliegue. |

<!-- Página 170 del PDF original -->

| RI-09 | Integración fallida con Fonasa/Isapres | Interoperabilidad deficiente con externos. |
| --- | --- | --- |
| RI-10 | Incidencias de rendimiento en móviles | Experiencia deficiente en apps de pacientes/médicos. |
| RI-11 | Parametrización incorrecta del sistema según especialidades médicas | Parámetros, catálogos o reglas clínicas configurados de forma incorrecta para determinadas especialidades médicas. |
| RI-12 | Baja alfabetización digital del personal administrativo | Parte del personal administrativo no cuenta con habilidades digitales suficientes para operar el sistema con seguridad. |
| RI-13 | Interrupción del servicio por ventanas de mantención mal planificadas | Ventanas de mantención o cambios se programan en horarios críticos y generan indisponibilidades no aceptables. |
| RI-14 | Homologación incorrecta de perfiles y roles de usuario | Perfiles y permisos mal asignados permiten accesos indebidos o bloquean funciones necesarias para la atención. |
| RI-15 | Fallas en equipamiento de red del hospital que afectan la solución | Routers, switches o enlaces internos con fallas o mala configuración afectan la conectividad hacia la plataforma. |

<!-- Página 171 del PDF original -->

##### Análisis cualitativo - RI

| ID | Riesgo | P | I | Nivel | Clasificación |
| --- | --- | --- | --- | --- | --- |
| RI-01 | Fallas en despliegue productivo | 3 | 4 | 12 | Alto |
| RI-02 | Incompatibilidad con hardware biomédico | 3 | 4 | 12 | Alto |
| RI-03 | Pérdida de datos en migración | 3 | 5 | 15 | Alto |
| RI-04 | Falta de adopción del personal clínico | 3 | 4 | 12 | Alto |
| RI-05 | Sincronización inconsistente entre sedes | 3 | 4 | 12 | Alto |
| RI-06 | Incumplimiento de SLA de soporte | 3 | 5 | 15 | Alto |
| RI-07 | Soporte post-producción insuficiente | 3 | 4 | 12 | Alto |
| RI-08 | Pérdida de trazabilidad clínica | 3 | 5 | 15 | Alto |
| RI-09 | Integración fallida con Fonasa/Isapres | 3 | 5 | 15 | Alto |
| RI-10 | Incidencias de rendimiento en aplicaciones móviles | 2 | 4 | 8 | Medio |
| RI-11 | Parametrización incorrecta del sistema según especialidades médicas | 3 | 4 | 12 | Alta |
| RI-12 | Baja alfabetización digital del personal administrativo | 3 | 3 | 9 | Media |
| RI-13 | Interrupción del servicio por ventanas de mantención mal planificadas | 3 | 4 | 12 | Alta |
| RI-14 | Homologación incorrecta de perfiles y roles de usuario | 3 | 4 | 12 | Alta |
| RI-15 | Fallas en equipamiento de red del hospital que afectan la solución | 2 | 4 | 8 | Media |

Table 9.6: Evaluación de Riesgos de Implantación (RI)

##### Plan de respuesta - RI

| ID | Riesgo | Prioridad | Acción | Acción de respuesta | Responsable |
| --- | --- | --- | --- | --- | --- |
| RI-01 | Fallas en despliegue productivo | Alta | Mitigar | Pilotos, checklists de go-live y doble validación | DevOps |
| RI-02 | Incompatibilidad hardware | Alta | Mitigar | Laboratorio de homologación biomédica y matrices de compatibilidad | Ing. Biomédico |
| RI-03 | Pérdida de datos en migración | Alta | Mitigar | Migración incremental, reconciliación y validación clínica | Líder de Datos |
| RI-04 | Falta de adopción médica | Alta | Mitigar | Plan ADKAR, embajadores y capacitación por rol | Líder de Cambio |
| RI-05 | Sincronización entre sedes | Alta | Mitigar | QoS WAN, reintentos/compensaciones y colas persistentes | Arq. Integración |
| RI-06 | Incumplimiento de SLA | Alta | Mitigar | NOC 24/7, SLO/SLA monitor y autoscaling conservador | Líder DevOps |

<!-- Página 172 del PDF original -->

| RI-07 | Soporte post go-live insuficiente | Alta | Mitigar | Mesa N1-N2-N3, acuerdos de escalamiento y on-call | Gerente Operaciones |
| --- | --- | --- | --- | --- | --- |
| RI-08 | Trazabilidad clínica | Alta | Mitigar | Auditoría extendida, logs firmados y retención prolongada | Jefe Seguridad TI |
| RI-09 | Integración con Fonasa/Isapres | Alta | Mitigar | Contratos de interfaz, entorno sandbox y fallback diferido | Líder Integración |
| RI-10 | Rendimiento en móviles | Media | Mitigar | Perf. profiling, caché local y optimización de payloads | Líder Mobile |
| RI-11 | Parametrización incorrecta del sistema según especialidades médicas | Alta | Mitigar | Construir checklist por especialidad, validar con referentes clínicos y probar casos reales antes del go-live. | Líder Funcional Clínico |
| RI-12 | Baja alfabetización digital del personal administrativo | Media | Mitigar | Planificar capacitaciones básicas, manuales paso a paso y soporte presencial en las primeras semanas. | Jefe de Capacitación |
| RI-13 | Interrupción del servicio por ventanas de mantención mal planificadas | Alta | Mitigar | Coordinar ventanas con el mandante, comunicar anticipadamente y definir planes de rollback rápidos. | Jefe de Operaciones TI |
| RI-14 | Homologación incorrecta de perfiles y roles de usuario | Alta | Mitigar | Definir matriz de roles/permisos, revisar con RRHH y TI y probar accesos antes de producción. | Administrador de Seguridad / IAM |
| RI-15 | Fallas en equipamiento de red del hospital que afectan la solución | Media | Mitigar | Realizar levantamiento de red, pruebas de conectividad, monitorización y planes de contingencia con TI del mandante. | Jefe de Redes / Comunicaciones |

##### Plan de contingencia - RI

| ID | Riesgo | Acción de contingencia |
| --- | --- | --- |
| RI-01 | Fallas en despliegue productivo | Rollback controlado, congelamiento de cambios y ventana adicional. |
| RI-02 | Incompatibilidad hardware | Sustitución temporal por equipos certificados o protocolo alterno. |
| RI-03 | Pérdida de datos en migración | Restaurar snapshot previo y reintentar migración por lotes. |
| RI-04 | Falta de adopción médica | Soporte presencial en sitio y sesiones intensivas postgo-live. |
| RI-05 | Sincronización entre sedes | Activar sincronización diferida y priorizar eventos críticos. |

<!-- Página 173 del PDF original -->

| RI-06 | Incumplimiento de SLA | Modo degradado y ampliación temporal de capacidad. |
| --- | --- | --- |
| RI-07 | Soporte post go-live insuficiente | Contratar soporte externo y ampliar turnos de guardia. |
| RI-08 | Trazabilidad clínica | Reconstrucción de auditoría desde respaldos y fuentes secundarias. |
| RI-09 | Integración con Fonasa/Isapres | Operación manual temporal y tickets con el organismo externo. |
| RI-10 | Rendimiento en móviles | Desactivar features no esenciales y bajar frecuencia de sincronización. |
| RI-11 | Parametrización incorrecta del sistema según especialidades médicas | Revertir a parametrizaciones previas validadas y documentar restricciones temporales por especialidad. |
| RI-12 | Baja alfabetización digital del personal administrativo | Reforzar soporte en terreno, reasignar tareas críticas a personal con mayor experiencia y simplificar temporalmente algunos flujos. |
| RI-13 | Interrupción del servicio por ventanas de mantención mal planificadas | Suspender la mantención, activar rollback inmediato y reprogramar la ventana en horario de menor impacto. |
| RI-14 | Homologación incorrecta de perfiles y roles de usuario | Aplicar perfil seguro por defecto, revocar accesos dudosos y usar procesos manuales para operaciones críticas mientras se corrige. |
| RI-15 | Fallas en equipamiento de red del hospital que afectan la solución | Desviar tráfico por rutas alternativas, usar enlaces de respaldo (4G/5G/VPN) y priorizar soporte de red en áreas clínicas críticas. |

### 9.3 Análisis Cuantitativo y Complementario

Se desarrollan los siguientes análisis avanzados aplicados a los diez riesgos más críticos identificados.

##### Análisis FMEA (Failure Mode and Effects Analysis)

× × Se utilizó la métrica RPN (Risk Priority Number) = Severidad Ocurrencia Detección, con escalas de 1 a 10, Los modos de falla analizados corresponden a componentes críticos del sistema, considerando interoperabilidad, disponibilidad, seguridad, migración y adopción organizacional.

| ID | Componente / Proceso | Modo de Falla | Causa Raíz | Efecto | S | O | D | RPN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FMEA- 01 | Seguridad / Ciberseguridad | Brecha de seguridad o ciberataque | Configuración débil o phishing | Exposición de datos sensibles (PHI) | 9 | 4 | 4 | 144 |

<!-- Página 174 del PDF original -->

| FMEA- 02 | API Gateway | Vulnerabilidades o políticas inseguras | Falta de hardening o validación | Acceso no autorizado a datos | 9 | 4 | 3 | 108 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FMEA- 03 | Infraestructura / Disponibilidad | Caída del servicio o saturación | Sobrecarga o autoescalado mal configurado | Interrupción del servicio clínico | 8 | 4 | 4 | 128 |
| FMEA- 04 | Backup / DRP | Falla en copias o restauración | Copias corruptas o pruebas fallidas | Pérdida de información clínica histórica | 8 | 3 | 4 | 96 |
| FMEA- 05 | Base de datos | Corrupción o inconsistencia | Fallo de integridad o tuning deficiente | Pérdida de registros clínicos | 8 | 3 | 3 | 72 |
| FMEA- 06 | Registro clínico / Trazabilidad | Pérdida de trazabilidad | Logs incompletos o relojes desincronizados | Riesgo médicolegal y discontinuidad asistencial | 9 | 3 | 4 | 108 |
| FMEA- 07 | Migración de datos | Pérdida o mapeo incorrecto | Validación incompleta o transformación errónea | Inexactitud de datos clínicos | 8 | 3 | 4 | 96 |
| FMEA- 08 | SLA / Soporte | Incumplimiento de SLA | Monitoreo insuficiente o staffing bajo | Caída prolongada sin soporte | 8 | 3 | 3 | 72 |
| FMEA- 09 | Producción / Trazabilidad | Fallo post golive | Controles débiles tras despliegue | Pérdida de registros durante operación | 8 | 3 | 4 | 96 |
| FMEA- 10 | Integración Fonasa / Isapres | Falla de comunicación o autenticación | API obsoleta o endpoint inestable | Retrasos o errores en facturación | 7 | 3 | 4 | 84 |

Table 9.7: Resumen del Análisis FMEA para los riesgos más críticos.

| ID | Acción Correctiva Recomendada | Responsable |
| --- | --- | --- |
| FMEA- 01 | Implementar MFA, auditorías de seguridad, pentesting trimestral y gestión de secretos | CISO / Seguridad TI |
| FMEA- 02 | Aplicar validación estricta, WAF, revisiones OWASP y monitoreo de API Gateway | Arquitecto de Seguridad / DevSecOps |
| FMEA- 03 | Ejecutar pruebas de carga, mejorar autoescalado y observabilidad (SLO/SLA) | SRE / Infraestructura |

<!-- Página 175 del PDF original -->

| FMEA- 04 | Implementar política 3-2-1, versionado y pruebas automáticas de restauración | Operaciones / DBA |
| --- | --- | --- |
| FMEA- 05 | Fortalecer constraints, integridad referencial y auditoría de base de datos | DBA / Arquitecto de Datos |
| FMEA- 06 | Implementar política de logging estructurado y correlación de eventos críticos | Líder Funcional / SRE |
| FMEA- 07 | Realizar validaciones cruzadas, pruebas de reconciliación y ETL certificadas | Data Lead / QA de Datos |
| FMEA- 08 | Establecer SLOs, runbooks y auditoría de tickets de soporte | Service Manager / Soporte N2 |
| FMEA- 09 | Mejorar control de cambios, versionado y dashboards de auditoría | Líder de Operaciones / QA |
| FMEA- 10 | Monitorear integraciones, gestionar versiones de API y alertas por latencia | Arquitecto de Integración / DevOps |

Table 9.8: Acciones correctivas y responsables asociados al análisis FMEA.

##### Análisis FTA (Fault Tree Analysis)

El Análisis de Árbol de Fallas (FTA) se emplea para modelar de forma jerárquica las combinaciones de fallas técnicas, de infraestructura y operativas que pueden conducir a la interrupción del sistema clínico principal.

Este modelo complementa el análisis FMEA previo, permitiendo visualizar las dependencias lógicas entre causas, evaluar probabilidad de ocurrencia conjunta y priorizar estrategias de mitigación basadas en resiliencia, disponibilidad y seguridad.

- Evento superior: Interrupción total del sistema clínico.

- OR: Basta con que ocurra una de las causas para producir el evento superior.

- AND: Es necesaria la ocurrencia simultánea de varias causas.

Figure 9.2: Diagrama FTA

![Página 175 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-175.png)

<!-- Página 176 del PDF original -->

## 10 Plan de Calidad

El plan de aseguramiento de calidad se basa en los estándares ISO/IEC 25010 y las prácticas de CMMI, garantizando que el producto cumpla con todas las características de calidad(funcionalidad, seguridad, mantenibilidad, etc.) desde el inicio. El equipo seguirá procesos definidos y medibles de QA/QC, siendo el Jefe de Proyecto responsable de establecer las políticas y la calidad un compromiso compartido en cada fase.

### 10.1 Métricas de Calidad del Código

Se establecen métricas cuantitativas monitoreadas en la Integración Continua (CI) mediante quality gates:

- Cobertura de Pruebas Unitarias: mínimamente 80% del código cubierto por pruebas automáticas. Esto asegura que la mayoría de las funcionalidades estén verificadas y ayuda a prevenir regresiones. Además, se espera una tasa de éxito de pruebas unitarias superior al 95% en cada ejecución, demostrando la confiabilidad de los componentes individuales.

- Complejidad Ciclomática: valor promedio < 10 por método. Se utilizarán análisis estáticos para medir la complejidad y refactorizar módulos demasiado complejos, mejorando la mantenibilidad y reduciendo la probabilidad de errores.

- Acoplamiento y Cohesión: se monitoreará el acoplamiento entre módulos para mantenerlo bajo (siguiendo principios de bajo acoplamiento y alta cohesión). Un diseño modular con bajo acoplamiento facilita las pruebas independientes y la extensibilidad del sistema. Herramientas de calidad analizarán dependencias para asegurar que la arquitectura cumple estos principios.

- Duplicación y Deuda Técnica: porcentaje de código duplicado < 5% y Debt Ratio < 5% según indicadores de la herramienta de análisis estático. Esto garantiza un código limpio, sin redundancias indebidas, y con deuda técnica controlada. Se llevarán registros de code smells y se corregirán de forma proactiva en cada iteración.

<!-- Página 177 del PDF original -->

- Vulnerabilidades y Seguridad: 0 vulnerabilidades críticas y menos de 5 medias conocidas en el código. Antes de cada liberación se ejecutarán análisis de seguridad (p.ej., scans de dependencias, análisis de código estático de seguridad) y pruebas de penetración sobre componentes críticos, para cumplir con los altos estándares de seguridad del dominio médico (protección de información sensible de pacientes, cumplimiento de normativas como HIPAA/LEY 19.628, etc.).

Solo se permite la promoción de un build si se cumplen estos criterios. Además, toda nueva funcionalidad requiere revisiones de código exhaustivas por desarrolladores senior o el Jefe de Desarrollo (code review).

#### 10.1.1 Análisis Estático y Dinámico

Como parte del framework de calidad, se aplicará tanto análisis estático como dinámico del software.

- El análisis estático incluye herramientas como linters y escáneres de calidad (p. ej., SonarQube o analyzers de .NET) ejecutados automáticamente en cada commit, para identificar code smells, complejidad excesiva, violaciones de estilo o posibles errores antes de la ejecución. Asimismo, se incorporará análisis de seguridad estático para detectar vulnerabilidades de código (ej: inyecciones SQL, exposiciones de datos) de forma temprana.

- El análisis dinámico comprende la ejecución de pruebas automatizadas y monitorización del comportamiento de la aplicación en tiempo de ejecución. Esto incluye pruebas de rendimiento y carga (midiendo tiempos de respuesta para cumplir el requisito de < 1 segundo por transacción en operaciones críticas, y capacidad para usuarios concurrentes proyectados), pruebas de stress y uso de perfiles de memoria/CPU para identificar cuellos de botella o fugas de recursos. También se implementarán pruebas dinámicas de seguridad (DAST) en entornos de staging, como simulaciones de ataques o fuzzing sobre las APIs, garantizando que el sistema resista eventos adversos en producción.

Todos estos gates de calidad (pruebas ejecutadas, métricas estáticas y dinámicas) estarán integrados en la línea de CI/CD, de modo que un build que no alcance los criterios establecidos no avanzará hasta ser corregido. Esto asegura que solo se despliegue a ambientes superiores (QA, producción) el código que haya pasado por todos los controles de calidad definidos.

Los gates de calidad aseguran que solo el código validado avance a ambientes superiores (QA, producción).

### 10.2 Verificación y Validación

El plan de calidad distingue claramente las actividades de verificación (asegurar que construimos el producto correctamente, conforme a las especificaciones) y de vali-

<!-- Página 178 del PDF original -->

dación (asegurar que el producto cumple con su propósito y satisface las necesidades del usuario final).

#### 10.2.1 Verificación

Para la verificación, se llevarán a cabo revisiones formales y pruebas técnicas en distintos niveles: revisiones de requisitos, inspecciones de diseño arquitectónico, walkthroughs de código y, por supuesto, ejecución de pruebas funcionales. En particular, el equipo realizará reviews de requisitos, diseño y código en momentos clave para asegurar que se cumplen los estándares y lineamientos definidos.

Además, se implementará una estrategia de pruebas en múltiples niveles:

- Pruebas unitarias (nivel componente) desarrolladas bajo enfoques como TDD para asegurar que cada unidad de código cumple su función de manera aislada.

- Pruebas de integración para verificar que los módulos interactúan correctamente y que, por ejemplo, el flujo entre la aplicación .NET MAUI y los servicios AWS (API Gateway, Lambdas, base de datos, etc.) funciona sin incompatibilidades.

- Pruebas de sistema o end-to-end donde se valida el sistema completo frente a los requerimientos funcionales y no funcionales acordados.

- Pruebas de aceptación del usuario (UAT), donde médicos, personal administrativo y otros stakeholders evalúan el sistema en un entorno controlado antes del despliegue final.

Cada uno de estos niveles cuenta con criterios de aceptación específicos: por ejemplo, en pruebas de integración se espera cero defectos críticos y resolución de defectos mayores en menos de 48 horas, mientras que en las pruebas de aceptación se busca al menos un 90% de casos de prueba exitosos y no más de 10 observaciones de severidad menor por ciclo de prueba, indicadores de que el sistema está listo para producción.

#### 10.2.2 Validación

En cuanto a la validación, desde las primeras iteraciones se considerará la participación del usuario final para asegurar que el producto desarrollado realmente resuelve el problema original. Se planificarán demos funcionales y pruebas de usabilidad con representantes de usuarios (médicos, enfermeras, personal de administración) al cierre de cada módulo importante, recogiendo feedback temprano.

Al final del desarrollo, se ejecutarán pruebas de aceptación con el cliente utilizando casos de uso reales, por ejemplo, agendar citas multicanal, registrar atenciones médicas con datos de pacientes de prueba, emisión de bonos y facturas, para validar que el sistema integral cumple con los procesos de negocio esperados y mejora las deficiencias de los sistemas actuales. Esta validación confirmará que requisitos como “Historia clínica unificada y accesible” o “Agendamiento en línea 24/7” realmente se alcanzaron con la solución propuesta. Solo una vez que el cliente y usuarios clave firmen la conformidad en esta etapa de validación, se procederá con el despliegue en producción.

<!-- Página 179 del PDF original -->

### 10.3 Trazabilidad de Requisitos

Para asegurar que todos los requerimientos funcionales y no funcionales del documento oficial se implementen y prueben, se gestionará una Matriz de Trazabilidad que vincula cada requisito con sus artefactos de diseño, módulos de código y casos de prueba asociados.

Identificación y seguimiento: Desde el inicio, cada requisito (p. ej., cumplimiento HL7/FHIR en HCE, disponibilidad 99,97%, tiempo de respuesta < 1 s) tendrá un ID único y será rastreado en el sistema de gestión del proyecto. En el diseño lógico, dichos IDs se asignarán a los módulos o microservicios; los casos de prueba unitarios, de integración y de sistema referenciarán explícitamente el ID que verifican. La ejecución de la suite generará reportes de cobertura por requisito, garantizando que ningún requisito carezca de prueba asociada.

Gestión de cambios y verificación: Si un requisito evoluciona o surge uno nuevo, las dependencias permiten identificar de inmediato el impacto en código y pruebas. Esta trazabilidad respalda auditorías internas, aportando evidencia de que por cada requisito del cliente existe una implementación y una prueba que lo valida. La matriz se entregará como parte de la documentación al cliente, asegurando transparencia y cobertura del 100% de las necesidades.

### 10.4 Mecanismos y Procesos de Aseguramiento de Calidad

El enfoque de calidad propuesto incluye un conjunto integral de actividades de QA/QC a lo largo del proyecto. Además de las pruebas mencionadas, se realizarán inspecciones y auditorías periódicas.

- Por un lado, se llevarán a cabo inspecciones de código y documentación por parte del equipo de calidad en puntos de control definidos (por ejemplo, al finalizar cada sprint o al completar cada módulo crítico), con listas de verificación para verificar adherencia a estándares de codificación, buenas prácticas de diseño (principios SOLID, patrones de arquitectura), y calidad de la documentación técnica generada.

- Por otro lado, se tienen planificadas auditorías internas lideradas por el Analista QA Experto del proyecto en hitos importantes, en las cuales se revisará de manera independiente el cumplimiento de los procedimientos de calidad y se medirán métricas clave (como defectos abiertos vs. cerrados, tendencia de cobertura de código, cumplimiento de SLA internos de arreglo de bugs, etc.).

En caso de desvíos, el equipo tomará acciones correctivas inmediatas (por ejemplo, refuerzo de capacitación en ciertas prácticas, refactorizaciones enfocadas, re-ejecución de pruebas) para realinear el proyecto con los objetivos de calidad. Adicionalmente, se considerará la posibilidad de auditorías externas o peer-reviews por parte de expertos no involucrados directamente en el desarrollo, para obtener una evaluación imparcial

<!-- Página 180 del PDF original -->

de la calidad del producto antes de la entrega final. Estos procesos de revisión adicional agregan una capa de confianza extra, especialmente crítica en un sistema médico donde la calidad es sinónimo de seguridad para pacientes y cumplimiento normativo.

### 10.5 Roles y Responsabilidades en el Aseguramiento de Calidad

La calidad es una responsabilidad compartida, con roles clave:

- Jefe de Proyecto: Responsable global del cumplimiento del plan de calidad, de los recursos asignados a QA y de la toma de decisiones.

- Jefe de Desarrollo: Garantiza la calidad del código mediante la supervisión de prácticas, estándares y la realización de revisiones de código sistemáticas.

- Arquitecto de Software / Jefe de Análisis y Diseño: Asegura que la arquitectura inicial promueva la calidad (diseño con bajo acoplamiento y alta cohesión).

- Analista QA Experto (Líder de Calidad): Encabeza el equipo QA, establece los procedimientos de prueba, criterios de aceptación y métricas, y consolida los informes de calidad.

- Analistas QA Senior/Junior: Ejecutan las pruebas definidas (unitarias, funcionales, de integración), registran incidentes y mantienen los scripts de prueba automatizada actualizados.

- Ingeniero DevOps / Encargado de Infraestructura: Administra la infraestructura de CI/CD y configura los pipelines para incluir todos los checks de calidad y observabilidad.

- Analista de Negocios / Jefe de Análisis: Valida que cada requisito tenga criterios de aceptación claros, participa en pruebas de aceptación (UAT) y verifica la trazabilidad de los cambios.

- Responsable de Seguridad: Lidera Seguridad por Diseño (S-SDLC), define requisitos de seguridad/privacidad y opera herramientas SAST/DAST/SCA en el pipeline.

- Diseñador(a) UI/UX: Lidera la calidad de la experiencia clínica, garantiza la accesibilidad (WCAG 2.1 AA) y realiza pruebas de usabilidad con usuarios clínicos.

### 10.6 Herramientas y Consideraciones Técnicas para la Calidad

El plan aprovecha herramientas alineadas con la tecnología propuesta (.NET MAUI, AWS):

- .NET (xUnit/NUnit): Utilizado para pruebas unitarias automatizadas ejecutadas en cada compilación.

- SonarQube: Integrado en el pipeline para el análisis estático de código fuente, proporcionando un tablero continuo de métricas de mantenibilidad y fiabilidad.

<!-- Página 181 del PDF original -->

- App Center / Selenium/Appium: Empleados para automatizar pruebas de interfaz de usuario en la aplicación .NET MAUI (Android y Windows) para verificar la portabilidad y usabilidad.

- AWS (Lambdas, API Gateway, etc.): Ambiente de staging en la nube para rigurosas pruebas de integración con datos simulados y stubs para servicios externos.

- Acceso Biométrico: Módulo sometido a pruebas especializadas con dispositivos biométricos en laboratorio y en campo para validar tasas de éxito de autenticación y fiabilidad.

### 10.7 Mejora Continua

Ciclo y métricas. El framework de calidad opera bajo mejora continua: las métricas recolectadas (cobertura, defectos por fase, tiempo de resolución de incidentes, feedback de usuarios en UAT, etc.) se analizan en retrospectivas para detectar oportunidades de mejora del proceso.

Acciones de mejora. Si un tipo de defecto escapa a las pruebas actuales, se ajustará el plan de pruebas con nuevos casos o técnicas (p. ej., pruebas exploratorias y casos de esquina), además de incrementar el uso de análisis dinámico para problemas de performance. Cuando una métrica no alcance su objetivo, se realizará análisis de causa raíz e implementarán acciones como capacitaciones en buenas prácticas de codificación para reducir complejidad o refuerzos en el pipeline de pruebas.

Evolución y estándares. Este enfoque proactivo asegura que el Plan de Calidad sea un artefacto vivo que evoluciona con el proyecto, garantizando un producto de alta calidad conforme a ISO/IEC 25010 y a las mejores prácticas de CMMI, en beneficio de Consultas Médicas S. A. y sus pacientes.

<!-- Página 182 del PDF original -->

## 11 Servicios de Operación

Diseñar modelo de soporte basado en ITIL/ITSM con métricas ingenieriles claras. Definir SLI, SLO y SLA considerando teoría de colas, distribuciones de probabilidad y modelos de disponibilidad. Calcular staffing óptimo usando Erlang C. Establecer OLA y UC internos coherentes con los SLA comprometidos.

### 11.1 Especificaciones del Call Center y SLA’s

El servicio de Call Center se regirá bajo principios de ITIL 4 Service Desk Practice para gestión de servicios de TI relacionados a Call Center y los SLI’s con sus SLA’s y SLO’s correcpondientes, frente al contexto de serviciós de salud. Se operará como un Service Desk administrado como omnicanal enfocado principalmente en el usuario (paciente), con procesos formales de gestión de incidentes y solicitudes. Cada interacción (llamada, chat, email) será registrada como ticket, categorizada y resuelta o escalada según los procedimientos definidos en esta sección o lo que el equipo interno de la empresa clínica determine, asegurando trazabilidad y retroalimentación además de buscar cumpllir con las necesidades de los clientes. Siguiendo con la gestión de servicios TI basados en ITSM, se definen claramente los Indicadores de Nivel de Servicio (SLI) que medirán el desempeño del Call Center, junto con Objetivos de Nivel de Servicio (SLO) que son las metas internas para esos indicadores, las cuales se plasman finalmente en un Acuerdo de Nivel de Servicio (SLA) formal con la organización.

#### 11.1.1 Servicios de Call Center

Call Center trabajará con los siguientes canales para proveer de sus servicios a los pacientes, además todos deberán cumplir con los SLI, SLA y SLO definidos posteriormente en la fig 11.1:

- Teléfono con IVR inteligente y enrutamiento automatizado

- Web chat con bot Nivel 1 (posible derivación a humano)

<!-- Página 183 del PDF original -->

- Correo electrónico

- WhatsApp Business integrado vía API

- App móvil HospiNet como canal de soporte/consulta

Los servicios anteriormente mencionados serán atendidos dependiendo del caso por distintos niveles de soporte cada uno con responsabilidades distintas, pudiendo escalar de nivel 1 a 4 dependiendo de la dificultad y extertiz necesaria para resolver el problema, información que será mas detallada y especificada en la sección 11.2.

#### 11.1.2 SLI’s de Call Center y servicio de soporte

Table 11.1: SLI, SLA y SLO asociados al Call Center y Plataforma

| SLI | SLA | SLO | Cómo se mide / definición operativa |
| --- | --- | --- | --- |
| Horario de disponibilidad | Lunes a Domingo 07:00-24:00 | Lunes a Domingo 07:00-24:00 | Ventana diaria en que el canal debe estar operativo para recibir y gestionar contactos. |
| Tiempo de respuesta / ASA | &lt; 180 s. | ≤ 20 s | Promedio (o p95) de segundos desde que entra el contacto hasta que atiende un agente humano |
| Tasa de abandono | &lt; 5%. | ≤ 3% | Porcentaje de contactos que cortan antes de ser atendidos por un agente humano. |
| FCR (First Call Resolution) | &gt; 70%. | ≥ 75% | Porcentaje de casos cerrados/solucionados en primer contacto sin escalamiento a niveles superiores. |
| Satisfacción del usuario | &gt; 85%. | ≥ 90% | Porcentaje de encuestas post-atención positivas (o NPS sobre umbral definido). |

Continúa en la siguiente página

<!-- Página 184 del PDF original -->

| SLI (Indicador) | SLA (contractual) | SLO (interno) | Cómo se mide / definición operativa |
| --- | --- | --- | --- |
| Disponibilidad del servicio Call Center | 99,95%. | 99,96% | Uptime mensual del módulo/canales de Call Center (excluye mantenciones planificadas siempre y cuando sean avisadas con 1 mes de antelación y sea avisado a los usuarios previamente). |
| RTO Servicios de comunicación | ≤ 1 min. | ≤ 30 min. | Tiempo máximo para restaurar servicios críticos tras caída. |
| RPO tickets de servicios de comunicación | ≤ 15 min. | ≤ 20 min . | Máxima pérdida de datos tolerable medida en tiempo. |

Todos los SLI’s, SLA’s y SLO’s mencionados anteriormente (directamente incidentes y relacionados al servicio de atención y soporte al cliente) deberán ser cumplidos y/o exigidos por el servicio provisto por la empresa oferente y por la empresa demandante respectivamente y serán ejecutados por una Mesa de ayuda de escalamiento de 4 niveles definida y especificada en la sección 11.2 a continuación.

#### 11.1.3 Herramientas multicanal:

Debido a la necesidad de los pacientes y los trabajadores de Call Center de funcionar por medio de distintos canales se definen distintas herramientas para el funcionamiento de este servicio a si como las que deberán utilizar los trabajadores del área para la atención y solución de problemas. Las herramientas definidas a continuación deberán cumplir con los requerimientos de disponibilidad definidos en la figura 11.1 que se verá a continuación luego de esta sección.

##### Whatsapp Bussiness:

Accesible como un número de Whatsapp al que los usuarios pueden contactar desde sus dispositivos personales a través de la plataforma de Whatsapp y en donde podrán realizar tanto reservaciones como consultas, de tal forma que puedan comunicarse directamente con trabajadores de Call Center que pueden estar o no en tiempo real en la conversación desde el dispositivos provisto por la empresa, pudiendo resolver todas las dudas de los clientes en la aplicación.

<!-- Página 185 del PDF original -->

##### Telefono IVR:

Contactable desde un número de teléfono definido para cada sucursal, los teléfonos IVR tendrán la capacidad (además de comunicarse entre funcionarios) de permitir la comunicación con los clientes, de tal forma que los pacientes podrán contactar directamente los teléfonos designados para la atención de Call Center.

##### Correo electrónico:

Dirección de correo habilitada para la realización de consultas por parte de los pacientes que deberá cumplir con los SLA mínimos de atención a los clientes definidos en 11.1, los pacientes o clientes deberán comunicarse por medio de algún sistema de mensajería por correo como Gmail, Outlook, etc, como canal de comunicación.

##### Chatbot web LVL 1:

Chatbot implementado funcionando desde el portal web de HospiNet, con la capacidad de responder Preguntas Frecuentes (FaQ’s) y resolver consultas básicas de los usuarios, de manera que puedan disminuir la carga de los trabajadores de Call Center y así no saturar las lineas de consultas, permitiendo la mayor disponibilidad de los trabajadores del servicio.

#### 11.1.4 Teoría de Colas y Dimensionamiento Óptimo

Para asegurar los SLI, SLA y SLO mencionados anteriormente en la tabla 11.1, el Call Center debe contar con el número adecuado de agentes en cada turno. Un dimensionamiento incorrecto derivaría en tiempos de espera altos (si hay pocos agentes para la demanda) o en costos innecesarios (si hay ociosidad por exceso de personal). Por ello, el diseño se apoya en la teoría de colas y específicamente en el modelo Erlang C, estándar de la industria para centros de contacto.

Según los datos actuales, el call center procesa en promedio 400-500 llamadas diarias. Distribuidas en 17 horas de operación (07:00-24:00), implican una tasa promedio del orden de 25-30 llamadas por hora, aunque con variaciones importantes según la franja horaria. Además, se deben considerar picos estacionales: por ejemplo, en la campaña de invierno la demanda puede aumentar un +150% sobre lo normal (lo que supondría hasta 750 llamadas en un día pico), así como aumentos en ciertos días de la semana o post-feriados (+80-100% en algunos casos). Dado este perfil de tráfico, asumimos también un Tiempo Medio de Operación (TMO) de las llamadas (duración de conversación + registro) cercano a 3-5 minutos en promedio, y cierta variabilidad en llegadas de llamadas que puede modelarse como un proceso de Poisson (llegadas aleatorias).

<!-- Página 186 del PDF original -->

Con estos parámetros, emplearemos Erlang C para calcular la dotación requerida por franja horaria. Erlang C considera la tasa de llegadas, el TMO y el número de agentes para estimar métricas como el Nivel de Servicio y el tiempo de espera promedio en cola . El objetivo típico que fijaremos es el mencionado 80/20 (por lo menos 80% de llamadas atendidas antes de 20 segundos de espera), que está alineado con el SLO de tiempo de respuesta. A modo ilustrativo, si en la hora punta ingresan 50 llamadas y cada agente atiende 12 llamadas/hora (5 min c/u), un cálculo lineal sugeriría 4-5 agentes; sin embargo, Erlang C ajusta por la aleatoriedad de las llegadas simultáneas y la probabilidad de colas, pudiendo indicar la necesidad de quizás 7-8 agentes en esa hora para lograr 80/20 sin superar 5% de abandono. El modelo estocástico de Erlang

  - desarrollado originalmente por A.K. Erlang para redes telefónicas - permite cuantificar la probabilidad de que una llamada deba esperar (cola) y, por ende, determinar cuántos agentes son necesarios para que esa probabilidad sea baja.

Además, contemplamos ajustes por abandono: Erlang C puro asume espera infinita (no considera que el cliente podría colgar), lo cual sobreestima agentes necesitados en escenarios reales de volúmenes bajos . Para refinar, usamos el modelo Erlang A (Conmutación de Palm) que incorpora la tasa de abandono o paciencia finita de los usuarios . En cualquier caso, los datos históricos de llamadas y abandonos serán insumo para estas fórmulas, afinando el dimensionamiento. También implementaremos un proceso de Workforce Management (WFM): ajustes dinámicos de personal por hora/día, considerando ausentismo, pausas y otros factores operacionales, de modo que siempre haya el número óptimo de agentes logueados para atender el volumen esperado garantizando los SLA sin incurrir en sobrecosto.

En resumen, mediante la aplicación rigurosa de la teoría de colas se garantizará un dimensionamiento óptimo del equipo del call center: suficiente para cumplir el nivel de servicio objetivo (ASA <20s, abandono <5%) en los distintos escenarios de carga, pero sin exceso de dotación. Esto se revisará periódicamente conforme crezca la demanda (la volumetría proyectada a 3 años casi duplica las interacciones digitales) para ajustar el staffing plan en consecuencia.

#### 11.1.5 Acuerdos Internos (OLA) y Contratos de Soporte (UC)

Para que el Call Center cumpla sus SLA de cara al usuario final, no solo importa el desempeño de los operadores de primera línea, sino también los tiempos de respuesta de las áreas de apoyo internas y proveedores externos. Por ello, el modelo de servicio incluirá Operational Level Agreements (OLA) y Underpinning Contracts (UC) que complementan al SLA:

- OLA internos: Son acuerdos de nivel de servicio entre el Call Center y otras

<!-- Página 187 del PDF original -->

áreas de la organización (TI, áreas clínicas, administración, etc.). Por ejemplo, si un paciente llama por un error en su factura que el operador de nivel 1 no puede resolver directamente, el caso se deriva al área de facturación; el OLA definirá que el área de facturación debe atender y resolver ese requerimiento en un plazo máximo (p. ej. 2 horas) para que el paciente reciba respuesta dentro de los tiempos comprometidos. Del mismo modo, si el Call Center detecta un incidente de sistema (ej: caída del portal web de agendamiento), escalará al Soporte de TI de Nivel 2, el cual, bajo su OLA, deberá responder en, digamos, 15 minutos. Estos OLA garantizan coordinación fluida y tiempos de atención end-to-end: cada equipo sabe qué se espera de él en apoyo al Call Center, de forma que el SLA global con el usuario no se vea afectado por demoras internas.

- Underpinning Contracts (UC) con proveedores: Consultas Médicas S.A. dependerá de servicios de terceros para operar el Call Center omnicanal, como la plataforma de telefonía IP o software CRM en la nube, y las comunicaciones unificadas que enlazan sus centros médicos. Se establecerán contratos con estos proveedores que incluyan SLA exigentes y penalizaciones acordes a los objetivos del proyecto. Por ejemplo, si la solución de telefonía en la nube es provista por un tercero, el contrato requerirá ≥ 99.95% de disponibilidad y soporte 24/7, de forma que cualquier falla en ese sistema sea atendida de inmediato. De igual manera, enlaces de datos dedicados entre centros o servicios de internet tendrán garantías de tiempo de actividad y performance. En caso de una interrupción externa (por ej. caída de la troncal telefónica), el proveedor estará obligado a tiempos de respuesta y resolución rápidos, y a informar al instante al equipo de Consultas Médicas. Estos contratos de respaldo aseguran que los componentes fuera del control directo de la organización igualmente cumplan con los niveles de servicio necesarios para no comprometer la atención al paciente.

En síntesis, los OLA y UC forman lo principal que sostiene la promesa de servicio del Call Center. Todos los eslabones, internos y externos, estarán sincronizados bajo acuerdos de nivel de servicio coherentes, creando un modelo integral donde “el todo es tan fuerte como su eslabón más débil”. La gestión de proveedores y áreas internas será activa, revisando indicadores de cumplimiento y realizando mejoras o planes de contingencia cuando alguno de estos respaldos no alcance las metas comprometidas.

### 11.2 Soporte Técnico (Mesa de Ayuda TI N1-N4)

Mientras el Call Center atiende a los usuarios finales (pacientes y personal médico), en paralelo debe existir un modelo robusto de soporte técnico de TI que garantice que toda la plataforma digital funcione sin interrupciones. Este modelo abarca la Mesa de Ayuda en múltiples niveles (N1 a N4), manejo de incidencias técnicas, mantenimiento

<!-- Página 188 del PDF original -->

preventivo, automatización, observabilidad y la incorporación de prácticas modernas de DevOps y AIOps para maximizar la resiliencia del ecosistema tecnológico.

#### 11.2.1 Estructura Escalonada de Soporte (Niveles 1-4)

El soporte técnico se organiza en cuatro niveles escalonados, asegurando que cada incidente o requerimiento sea atendido por personal con la experiencia adecuada, manteniendo la eficiencia. La Tabla 11.2 resume estos niveles.

<!-- Página 189 del PDF original -->

Table 11.2: Niveles de Soporte Técnico TI y Responsabilidades Principales

| Nivel | Descripción | Responsabilidades |
| --- | --- | --- |
| Nivel 1 - Service Desk | Primer contacto de TI | Atiende directamente a los usuarios internos (ej. personal clínico/administrativo) ante problemas de sistemas. Registro y categorización de incidentes en la herramienta ITSM, resolución de consultas básicas y problemas conocidos (ej. reseteo de contraseñas, dudas de uso). Intenta soluciones de primer nivel con la base de conocimiento; escalamiento a N2 según procedimientos cuando no puede resolver. |
| Nivel 2 - Soporte Técnico Especializado | Técnicos de soporte de segundo nivel | Toma los incidentes más complejos o que requieren conocimientos técnicos mayores. Realiza troubleshooting avanzado, revisión de configuraciones de sistema, aplica correcciones temporales (workarounds) si es posible. Puede resolver incidentes de software/hardware relativamente complejos. Coordina con especialistas de nivel 3 cuando se necesita una intervención de experto o cambios mayores. |
| Nivel 3 - Especialistas e Ingenieros | Expertos en tecnologías del sistema | Incluye administradores de plataforma, DBAs, ingenieros de software, especialistas en infraestructura o seguridad según el área del incidente. Se encargan de problemas críticos o en profundidad, realizando análisis de causa raíz (Problem Management) y aplicando soluciones definitivas (ej. optimizaciones de rendimiento, parche de código, reconfiguraciones mayores). También apoyan en mejoras continuas y tareas de tuning preventivo. |
| Nivel 4 - Fabricantes / Vendors | Soporte externo del proveedor | Es el escalón más alto, involucrando a los fabricantes de software/hardware o proveedores externos. Se recurre a N4 cuando el incidente deriva de un bug de producto, fallo de infraestructura de nube o necesidad de un cambio de diseño que solo el proveedor puede realizar. El vendor analiza e implementa fixes o parches; este nivel suele activarse en paralelo con garantías o contratos de soporte vigentes. |

Cada nivel está claramente definido en el modelo de operación, lo que coincide con las mejores prácticas ITIL para gestión de incidencias. En la práctica, cuando se reporta un problema (ya sea detectado por monitoreo o por un usuario final vía Mesa de Ayuda), N1 Service Desk intenta resolverlo inmediatamente usando guías y conocimientos disponibles. Si lo resuelve, se documenta la solución; si no, lo escala a N2 aportando toda la información recopilada. El Nivel 2 hará un diagnóstico más pro-

<!-- Página 190 del PDF original -->

fundo; si puede resolver (ej: reiniciando un servicio, corrigiendo una configuración), cierra el incidente; si no lo escala a N3 Especialistas. Los especialistas (que pueden estar integrados en un NOC/SOC 24x7 junto a N2, o bajo demanda) abordarán los incidentes críticos y de alta complejidad (ej: caída de la base de datos, problema grave de rendimiento, integraciones que fallan). Si aun así se requiere apoyo externo (un error propio del software adquirido, por ejemplo), se involucra al Nivel 4 (Vendor) abriendo un caso con el proveedor, mientras N3 gestiona la comunicación técnica.

Esta estructura escalonada garantiza que la resolución sea eficiente, los problemas simples no sobrecargan a personal altamente especializado (los resuelve N1 rápidamente) y, a su vez, los problemas complejos no se estancan en niveles bajos sin la pericia adecuada, sino que derivan prontamente a quienes pueden solucionarlos. Además, crea un circuito de retroalimentación de conocimiento. N3 puede entrenar a N2/N1 en soluciones para que en el futuro problemas similares se resuelvan en niveles más bajos. Las bases técnicas del proyecto enfatizan la necesidad de monitoreo 24x7 y especialistas dedicados, esto se refleja en la dotación de un Centro de Operaciones (NOC) que operará continuamente, complementando al Service Desk. En dicho NOC habrá roles como Service Delivery Manager, administradores de sistemas 24x7, analistas de seguridad (SOC), trabajando codo a codo con los niveles de soporte mencionados.

#### 11.2.2 Severidades de Incidentes y Protocolos de Escalamiento

No todos los incidentes son iguales. Se estableció una matriz de severidad o criticidad que determina la urgencia y el nivel de atención gerencial que corresponde a cada incidente, así como los tiempos máximos para escalar entre niveles. Según las bases técnicas, se definen 4 niveles de severidad con sus respectivos protocolos de escalamiento:

- Severidad 1 (Crítica): Impacto total en la operación (ej: sistema core caído, indisponibilidad completa de HCE o agendamiento). Requiere atención inmediata. Escalamiento: N1 a N2 en 15 minutos si no se ha resuelto; N2 a N3 en 30 minutos adicionales; N3 a N4 (vendor) en 1 hora si persiste sin solución. Además, notificación inmediata a la Gerencia y al comité de crisis apenas se confirma que es de Severidad 1. Estos incidentes disparan un manejo de incidentes mayor (major incident management) con comunicaciones ejecutivas frecuentes hasta su resolución.

- Severidad 2 (Alta): Impacto grave pero parcial (ej. caída de un módulo crítico como facturación, o degradación severa que afecta funciones clínicas importantes). Escalamiento: N1 a N2 en máx. 30 min; N2 a N3 en 1 hora; N3 a N4 en 2 horas. Notificación a Gerencia dentro de la primera hora si el problema no se resuelve. Aunque no todo el sistema esté caído, la alta dirección debe enterarse pronto porque afecta un servicio medular.

- Severidad 3 (Media): Impacto acotado o degradación menor en funciones no críticas (ej. un módulo secundario con fallas, o workaround disponible; afecta a algunos usuarios pero hay alternativas). Escalamiento: N1 a N2 en 2 horas; N2

<!-- Página 191 del PDF original -->

a N3 en 4 horas; N3 a N4 en 8 horas si procede. Notificación gerencial es diaria (en reporte rutinario) mientras esté abierto, dado que no es urgente informar inmediatamente.

- Severidad 4 (Baja): Problemas menores, consultas de cómo usar una funcionalidad, pedidos de mejora, incidentes cosméticos sin impacto operacional. Escalamiento: N1 puede tardar hasta 8 horas antes de escalar a N2; N2 dispone de 24 horas antes de escalar a N3; N3 a N4 en 48 horas si hiciera falta. Notificación a gerencia en reportes semanales o mensuales, ya que su impacto es mínimo.

Estos tiempos de escalamiento establecidos aseguran que ningún incidente quede “atorado” sin atención al nivel correcto. Si el reloj corre y no se resuelve, automáticamente sube de nivel de expertis. Adicionalmente, la Mesa de Ayuda (N1) cuenta con la autoridad de escalar de inmediato a niveles superiores cualquier incidente que, aunque inicialmente parezca menor, el agente intuya que puede ser más grave de lo pensado (mejor sobre-reaccionar que quedarse corto).

Junto a los escalamientos, se han definido SLA de resolución (tiempos objetivos de resolución final) dependiendo de la prioridad del incidente. Para prioridad P1 (equivalente a Severidad 1) se espera resolver en máximo 2 horas, P2 en ≤4 horas, P3 en ≤8 horas hábiles, P4 en ≤48 horas hábiles. Estos objetivos de resolución implican trabajo continuo hasta cerrar el incidente, incluso involucrando múltiples niveles en paralelo si es necesario. Por ejemplo, ante un incidente crítico (S1/P1), mientras N2 y N3 investigan, se podría contactar al vendor (N4) en paralelo sin esperar la 1 hora, para acortar el tiempo total de solución, la prioridad es restablecer servicio en <2h. En caso de superar esos tiempos, se considera una brecha de SLA y se desencadenan revisiones post-mortem. La siguiente tabla sintetiza los tiempos de respuesta y resolución según severidad:

<!-- Página 192 del PDF original -->

| Severidad (Prioridad) | Ejemplo de Impacto | Escalamiento N1→N2 | Escalamiento N2→N3 | Escalamiento N3→N4 | Tiempo Máx. de Resolución |
| --- | --- | --- | --- | --- | --- |
| Sev 1 - Crítica (P1) | Caída completa de sistemas core (HCE, etc.) | 15 min | +15 min (30 min total) | +30 min (1h total) | 2 horas máx. solución |
| Sev 2 - Alta (P2) | Falla seria en funcionalidad crítica parcial. | 30 min | +30 min (1h total) | +1 h (2h total) | 4 horas máx. solución |
| Sev 3 - Media (P3) | Problema moderado, sistema operando con degradación. | 2 horas | +2 h (4h total) | +4 h (8h total) | 8 horas hábiles máx. solución |
| Sev 4 - Baja (P4) | Incidente menor, bypass disponible o cosmetic. | 8 horas | +16 h (24h total) | +24 h (48h total) | 48 horas hábiles máx. solución |

Los tiempos ”hábiles” se refieren a la jornada normal de soporte (que en este proyecto, dada la criticidad, prácticamente es 24/7 para P1-P2 y horario extendido para P3-P4). También se observa que la notificación a la alta gerencia es inmediata para S1, en 1 hora para S2, y periódica para S3-S4, esto para mantener informada a la dirección y, si corresponde, activar planes de comunicación a usuarios (por ejemplo, enviar un aviso a los centros médicos si ocurre una caída grande). En definitiva, estos protocolos aseguran rapidez y diligencia en la respuesta a incidentes de TI, minimizando el impacto en la operación clínica.

#### 11.2.3 Gestión del Conocimiento, Automatización y Runbooks

Una pieza fundamental del soporte eficiente es la gestión del conocimiento. El proyecto incluye un completo traspaso de conocimiento desde los implementadores hacia el equipo interno, con creación de una Knowledge Base colaborativa y documentación detallada. Esta base de conocimiento seguirá viva durante la operación: cada incidente relevante resultará en un artículo o actualización en la wiki de soporte, de modo que “la próxima vez no tengamos que reinventar la rueda”. Por ejemplo, si N3 resuelve un problema complejo de integración con un laboratorio externo, documentará los síntomas, causa y solución en la KB; así, si reaparece, N1 o N2 podrían identificarlo y aplicar la solución documentada rápidamente. La wiki/KB incluirá guías de resolución (playbooks) paso a paso para problemas comunes: “Cómo reiniciar el servicio de base de datos sin afectar a los usuarios” o “Procedimiento para restaurar una cita perdida en el sistema de agendamiento”. Este enfoque reduce la dependencia de

<!-- Página 193 del PDF original -->

individuos y convierte las experiencias en activos reutilizables para la organización.

La automatización es otro pilar clave. Se adoptará una filosofía “Automation-first” donde todas las tareas repetitivas o propensas a error humano se intentarán automatizar. Por ejemplo, en lugar de que un técnico de N1 deba crear cuentas de usuario manualmente, se desarrollarán scripts o flujos automatizados; los reseteos de contraseña se ofrecerán vía autoservicio al usuario final con validaciones seguras, descargando trabajo del Service Desk. También se automatizarán tareas de mantenimiento rutinario: limpieza de logs, reinicio programado de ciertos servicios en horarios valle, monitoreo de jobs nocturnos con reintentos automáticos, etc. En caso de incidentes, se pueden tener playbooks automatizados integrados en herramientas de orquestación: es decir, secuencias predefinidas de acciones que el sistema ejecuta ante una alerta conocida. Un ejemplo: si el monitor detecta que el uso de CPU del servidor de aplicación supera el 90% durante 5 minutos, automáticamente puede disparar un playbook que agrega una instancia extra (escalado horizontal) o reinicia el proceso que está consumiendo CPU en exceso, antes de que eso degrade el servicio. Estas acciones automatizadas acelerarían la recuperación sin esperar intervención manual.

Para facilitar lo anterior, se elaborarán Runbooks para los niveles 2/3: esencialmente documentos operativos con instrucciones detalladas para lidiar con diferentes tipos de incidentes o tareas de mantenimiento. Ejemplo de runbook: “Recuperación ante caída del servicio de Agenda: 1) Verificar estado del contenedor X, 2) Si está caído, intentar levantar con comando Y, 3) Si no levanta, verificar logs en ruta Z buscando patrón de error…” y así sucesivamente. Los runbooks no solo guían al humano, sino que sirven de base para la automatización (uno puede convertir un runbook en un script paso a paso). Además, incorporan criterios de escalamiento: el runbook indica en qué punto, si no se resuelve, se debe escalar al siguiente nivel. De esta manera, incluso personal de N1/N2 menos experimentado puede intentar pasos de resolución con confianza, sabiendo cuándo pasar la pelota a niveles superiores.

La gestión del conocimiento también incluye un componente de capacitación continua. Habrá sesiones periódicas donde N3 comparta con N1/N2 las lecciones aprendidas de incidentes recientes y nuevas herramientas o procedimientos. Se incentiva la documentación de todo cambio (principio de Documentation-as-Code mencionado en las bases) para mantener un repositorio actualizado de la configuración del sistema y su historial. Esto es invaluable para solucionar problemas, ya que se puede rastrear si un incidente coincide con algún cambio reciente.

En suma, mediante una base de conocimiento robusta, automatización de rutinas y disponibilidad de playbooks/runbooks, el soporte técnico podrá resolver más rápidamente los problemas conocidos, minimizar errores humanos y estandarizar las respuestas. Esto redunda en mejores tiempos de respuesta y en una operación más predecible y controlada.

<!-- Página 194 del PDF original -->

#### 11.2.4 Observabilidad de Extremo a Extremo y AIOps

Dado que estamos implementando una plataforma moderna (nube híbrida, microservicios, bases de datos, apps móviles, etc.), la observabilidad end-to-end es un requisito esencial para el soporte. Desde el diseño se está incorporando telemetría en cada componente crítico. Esto significa que tendremos métricas, logs y trazas (traces) recolectados de todos los servicios: por ejemplo, cada petición al sistema de agendamiento genera logs estructurados, expone métricas de tiempo de respuesta, y puede ser seguida en un trace distribuido que conecte desde la app móvil, pasando por API Gateway, hasta la base de datos.

Se desplegarán herramientas de Application Performance Monitoring (APM) y de monitoreo de infraestructura que alimentarán un panel único de observabilidad. El NOC 24x7 verá en tiempo real el estado de servidores (CPU, memoria, disco, latencias), el estado de aplicaciones (tasa de errores por servicio, duración de transacciones, etc.) y también indicadores de experiencia de usuario (por ejemplo, tiempo de carga de la página de portal paciente, tasa de errores front-end). Toda esta telemetría será almacenada y analizada continuamente.

Dado el volumen de datos que generará la observabilidad en un ecosistema complejo, se utilizará una solución de AIOps (Artificial Intelligence for IT Operations). AIOps combina machine learning, analítica en tiempo real y automatización para manejar la escala y velocidad de eventos en sistemas modernos. En la práctica, la plataforma AIOps ayudará a:

- Correlacionar eventos y alertas en tiempo real: por ejemplo, si varias métricas fallan simultáneamente (CPU al 100%, errores 500 en el servicio X y caída en las transacciones por segundo), AIOps las agrupará como un único incidente, evitando generar alertas separadas y reduciendo ruido.

- Detección temprana de anomalías: mediante ML, aprenderá el comportamiento normal (baseline) de cada métrica y detectará desviaciones relevantes antes de que evolucionen a fallas mayores. Por ejemplo, un aumento inusual en la cola de mensajes o un tiempo de respuesta elevado a las 3 am podría indicar una fuga de memoria; AIOps lo alertará de inmediato para actuar antes del colapso del servicio.

- Reducir falsos positivos: filtrando el ruido típico de entornos tradicionales, donde aparecen muchas alertas sin impacto real. Con análisis inteligente, AIOps ignorará fluctuaciones transitorias o eventos no relevantes.

- Priorizar automáticamente según impacto: AIOps comprenderá qué componentes son más críticos (ej. HCE) y su contexto de uso, de modo que, ante dos alertas, elevará automáticamente la que represente mayor impacto potencial. Esto se alinea con los criterios solicitados de priorización por impacto.

El resultado es que el equipo de soporte pasará de un enfoque mayormente reactivo (enterarse por los usuarios de que algo anda mal) a uno proactivo y predictivo, donde

<!-- Página 195 del PDF original -->

frecuentemente podrá identificar un problema incipiente antes de que impacte a los usuarios. Un ejemplo claro: el sistema de AIOps podría anticipar, según ciertas tendencias, que “en 15 minutos el servidor de base de datos podría saturarse”, generando una alerta preventiva para actuar con anticipación.

Otra ventaja de AIOps es habilitar la respuesta automática a incidentes. Al integrarla con las plataformas de orquestación, es posible definir acciones de auto-remediación frente a ciertos eventos. Por ejemplo, si un servicio web se cuelga y no responde a los checks de salud, AIOps ejecuta automáticamente el playbook correspondiente: reinicia el contenedor o instancia, verifica que vuelva a estado OK y registra la acción. Del mismo modo, ante señales de memoria saturada, puede activar el escalado automático (scale out) y desplegar nuevas instancias.

Estas capacidades representan un verdadero mecanismo de self-healing, donde la plataforma se recupera sola de fallas comunes sin intervención humana. Para acciones de mayor riesgo siempre se puede exigir aprobación manual, pero la idea es que, para eventos bien caracterizados, la automatización actúe de inmediato. Esto reduce de forma significativa el MTTR (Mean Time to Recovery) y mantiene la continuidad operativa.

Cabe destacar que en las prácticas de vanguardia se contempla incluso el concepto de NoOps, donde muchas operaciones son autónomas. Si bien siempre se requerirá intervención humana para incidentes complejos, con una combinación de observabilidad total, AIOps y automatización se busca que un porcentaje significativo de incidentes se resuelvan sin intervención o con mínima intervención humana. Esto libera al equipo técnico para enfocarse en mejoras estratégicas en lugar de tareas rutinarias de monitoreo.

El proyecto de Consultas Médicas S.A. exige explícitamente monitoreo 24x7, gestión de logs, automatización y orquestación dentro de los sistemas de apoyo a la operación, lo cual se alinea perfectamente con esta estrategia. Se implementarán pipelines de telemetría robustos, almacenamiento escalable de logs (por ejemplo, soluciones big data o cloud para garantizar detalle sin pérdida) y un motor central de automatización encargado de ejecutar los flujos de AIOps y runbooks. La seguridad estará integrada en todo momento, con analistas SOC monitoreando también eventos de ciberseguridad.

En definitiva, el soporte técnico contará con visibilidad en tiempo real de todo el ecosistema y con herramientas inteligentes capaces de responder más rápido que nunca ante cualquier eventualidad, cumpliendo así con los requisitos de disponibilidad continua y desempeño óptimo.

#### 11.2.5 Capacidad de Auto-Sanacion y mantenimiento Proactivo

El modelo de operación incorpora capacidades de **auto-sanación y mantenimiento proactivo** para evitar interrupciones en un entorno clínico donde la continuidad es crítica. Se realizarán mantenimientos programados sin impacto, aplicando parches y actualizaciones en horarios de baja actividad y usando infraestructura redundante.

<!-- Página 196 del PDF original -->

Además, se validarán periódicamente las copias de seguridad mediante restores reales y simulacros de recuperación, garantizando RPO de 15 minutos y RTO de 1 hora. Del mismo modo, se ejecutarán actividades de capacity planning y tuning continuo para asegurar que los recursos no lleguen al límite y que los sistemas mantengan un rendimiento óptimo.

El modelo incorpora prácticas avanzadas como **Chaos Engineering**, que permite descubrir fallas ocultas mediante la inyección controlada de errores en ambientes seguros. También se apalancan las capacidades nativas de auto-recuperación de plataformas como Kubernetes, que reinician contenedores y redistribuyen cargas automáticamente cuando un servicio falla. A esto se suman health-checks exhaustivos, redundancia activa-activa y patrones de resiliencia como circuit breakers y retries inteligentes, lo que fortalece la estabilidad de la plataforma ante fallos en cascada.

La combinación de estas prácticas con AIOps habilita una **auto-sanación inteligente**, donde el sistema no solo detecta eventos, sino que ejecuta acciones correctivas: reinicios controlados, escalamiento automático, ejecución de scripts seguros o avisos a desarrollo ante problemas como fugas de memoria. El objetivo es disminuir drásticamente el MTTR y mantener el presupuesto de error cercano a cero. Además, se fomenta una cultura de mejora continua mediante análisis post-mortem sin culpables, reforzando monitoreo, documentación y procesos para evitar que un incidente se repita.

En conclusión, el modelo de servicios para Consultas Médicas S.A. integra un Call Center omnicanal con SLA estrictos y un soporte técnico escalonado (N1-N4) fortalecido con ITIL v4, SRE, DevOps, automatización y AIOps. Esto garantiza alta disponibilidad, desempeño óptimo y una operación más resiliente y autosuficiente. El resultado esperado es una experiencia tecnológica de primer nivel, donde los sistemas clínicos no fallen en momentos críticos y los pacientes reciban atención fluida y confiable, cumpliendo la misión de unir medicina y tecnología para entregar experiencias de salud memorables.

<!-- Página 197 del PDF original -->

## 12 Plan de Operación

### 12.1 Plan de Mantención

El propósito del Plan de Mantenimiento Preventivo y Evolutivo es garantizar que la solución tecnológica mantenga su capacidad operativa, confiabilidad, seguridad y rendimiento a lo largo de todo su ciclo de vida. Este plan aplica principios avanzados de Ingeniería de Mantenimiento y Confiabilidad, incorpora prácticas de Reliability Centered Maintenance, y utiliza técnicas de mantenimiento predictivo basadas en modelos de Machine Learning e Inteligencia Artificial para anticipar fallas antes de que afecten la operación.

La mantención evolutiva incluye la refactorización de componentes, el control de la deuda técnica, la mejora constante del software y la actualización regular de las dependencias, lo que asegura que la plataforma mantenga su seguridad, calidad y eficacia a través del tiempo.

#### 12.1.1 Enfoque General de Ingeniería de Confiabilidad

Este plan se fundamenta en los principios de la Ingeniería de Confiabilidad, que establecen que un sistema debe mantenerse:

- Confiable: capaz de operar sin fallas inesperadas.

- Mantenible: intervenible de manera rápida y segura.

- Disponible: siempre listo para operar cuando se necesita.

Para ello, se evalúan:

- Funciones críticas del sistema.

- Modos de falla potenciales.

- Consecuencias en disponibilidad, seguridad, datos y operación.

- Frecuencia y probabilidad de ocurrencia.

- Impacto y criticidad.

- Estrategias óptimas de intervención (preventiva, predictiva y evolutiva).

<!-- Página 198 del PDF original -->

Este análisis permite definir un plan de intervención proporcional al riesgo real de cada componente.

#### 12.1.2 Estrategia RCM (Reliability Centered Maintenance)

La metodología RCM se utiliza para estructurar el mantenimiento en torno a la confiabilidad del sistema. Sus etapas principales son:

##### Identificación de funciones críticas

Las funciones esenciales incluyen:

- Prestación de servicios clínicos o administrativos.

- Procesamiento de datos y registros críticos.

- Integración con sistemas externos.

- Disponibilidad de aplicaciones, bases de datos y servicios backend.

- Seguridad, autenticación y continuidad operacional.

##### Análisis de modos de falla

Entre los modos de falla típicos analizados:

- Degradación de rendimiento por saturación.

- Corrupción o inconsistencia en bases de datos.

- Caídas de servicios por fallas de infraestructura.

- Vulnerabilidades críticas de seguridad.

- Fallos en integraciones externas.

- Degradación por acumulación de deuda técnica.

##### Evaluación de criticidad

Cada modo de falla es evaluado según:

- Probabilidad de ocurrencia.

- Impacto operacional y funcional.

- Consecuencias clínicas o administrativas.

- Repercusiones en seguridad y SLA.

##### Selección de estrategias

Según criticidad, se aplican:

- Mantenimiento preventivo (calendarizado).

- Mantenimiento predictivo (ML/AI).

- Mantenimiento evolutivo (mejora continua).

- Mantenimiento correctivo (última alternativa).

<!-- Página 199 del PDF original -->

#### 12.1.3 Mantención Preventiva

El mantenimiento preventivo considera actividades programadas para reducir la probabilidad de fallas y asegurar la continuidad operativa.

##### Objetivos

- Reducir la ocurrencia de incidentes.

- Estabilizar el desempeño del sistema.

- Mantener la infraestructura dentro de parámetros aceptables.

##### Actividades Preventivas Aplicación / Backend / API

- Revisión sistemática de logs.

- Validación de endpoints críticos.

- Limpieza de temporales, cachés y sesiones.

- Ejecución de pruebas funcionales básicas.

##### Bases de Datos

- Reindexación programada.

- Validación de integridad periódica.

- Optimización de consultas y tablas críticas.

- Monitoreo de crecimiento.

##### Infraestructura

- Auditoría de capacidad del servidor.

- Validación del rendimiento en picos de carga.

- Revisión de reglas de autoescalado.

- Comprobación de health-checks.

##### Seguridad

- Aplicación de parches críticos.

- Rotación de llaves y certificados.

- Auditorías de accesos y privilegios.

- Evaluación continua de cumplimiento normativo.

##### Redes y comunicación

- Validación de latencia y ancho de banda.

- Revisión de firewalls y balanceadores.

- Pruebas de continuidad con servicios externos.

<!-- Página 200 del PDF original -->

#### 12.1.4 Mantención Predictiva Basada en ML/AI

La mantención predictiva utiliza datos, métricas y modelos de inteligencia artificial para anticipar fallas antes de que ocurran.

##### Objetivos

- Detectar patrones anómalos.

- Predecir fallas antes de que impacten al sistema.

- Activar medidas preventivas de manera anticipada.

##### Técnicas Utilizadas

- Modelos de series de tiempo para detectar degradación.

- Algoritmos de detección de anomalías en logs.

- Modelos supervisados para predicción de fallas.

- Correlación automática entre errores, latencias y tráfico.

##### Métricas Monitorizadas

- Latencia P95 y P99.

- Tasa de errores.

- CPU y RAM por servicio.

- IOPS y rendimiento de bases de datos.

- Disponibilidad de integraciones externas.

- Alertas de seguridad.

##### Acciones Derivadas

- Autoescalado anticipado.

- Reinicios controlados.

- Aplicación preventiva de parches.

- Reconfiguración dinámica.

- Alertas automáticas 24/7.

#### 12.1.5 Mantención Evolutiva

##### Refactoring Continuo

- Limpieza y reorganización de código.

- Optimización de algoritmos lentos.

- Eliminación de componentes obsoletos.

- Reducción de complejidad y mejora de mantenibilidad.

<!-- Página 201 del PDF original -->

##### Actualización de Dependencias

- Gestión de versiones SemVer.

- Sustitución de librerías vulnerables.

- Actualización de frameworks y runtimes.

- Integración de escáneres automáticos en CI/CD.

##### Gestión de Deuda Técnica

- Identificación y registro de deuda técnica.

- Priorización según impacto y riesgo.

- Corrección continua en ciclos de sprint.

- Uso de herramientas SAST, DAST y SonarQube.

#### 12.1.6 Métricas de Degradación y Umbrales de Intervención

| Métrica | Umbral de intervención | Acción recomendada |
| --- | --- | --- |
| Latencia P95 | &gt; 350 ms | Escalado o ajuste de recursos |
| Error rate | &gt; 2% | Análisis de logs y rollback |
| CPU por servicio | &gt; 75% | Autoescalado, revisión de código |
| Memoria | &gt; 80% | Reinicio controlado / tuning |
| Crecimiento BD | &gt; 15% mensual | Reindexación / optimización |
| Integridad BD | Falla en validaciones | Restauración desde respaldo |
| Vulnerabilidad crítica | ≥ 1 | Parche urgente en &lt;24h |

#### 12.1.7 Gobernanza y Gestión del Mantenimiento

- Las intervenciones se gestionan mediante un Change Advisory Board (CAB).

- Toda intervención requiere análisis de impacto, documentación y plan de rollback.

- Se mantienen registros históricos de todas las actividades de mantenimiento.

- El plan es revisado semestralmente para incorporar mejoras continuas.

### 12.2 Plan Servicios de Operación

El Plan de Servicios de Operación define el modelo operativo que garantizará la disponibilidad, confiabilidad, estabilidad y eficiencia continua de la solución tecnológica. Este plan adopta un enfoque basado en principios de Site Reliability Engineering, estableciendo lineamientos para la observabilidad completa del sistema, la automatización de procesos operacionales, la reducción de trabajo repetitivo, la gestión basada en error budgets, el análisis de incidentes mediante blameless postmortems y la optimización de costos operacionales bajo prácticas FinOps.

<!-- Página 202 del PDF original -->

El objetivo es proveer una operación medible, resiliente y sostenible, alineada con los requerimientos del mandante y con los niveles de servicio comprometidos.

#### 12.2.1 Modelo Operativo Basado en SRE

El enfoque SRE combina ingeniería de software con operación de sistemas para construir servicios más confiables, eficientes y escalables. Los principios aplicados incluyen:

- Énfasis en automatización por sobre intervención manual.

- Toma de decisiones guiada por métricas y datos observables.

- Implementación de SLO/SLA y control mediante error budgets.

- Reducción del toil para liberar capacidad del equipo operativo.

- Diseño de sistemas resilientes y capaces de recuperarse ante fallas.

Este modelo permite establecer una operación proactiva y altamente confiable, apoyada en prácticas modernas utilizadas en plataformas críticas.

#### 12.2.2 Observabilidad Integral

Para garantizar transparencia operacional y facilitar la respuesta temprana a incidentes, se implementan los tres pilares de la observabilidad:

##### Logs

- Captura estructurada de eventos críticos.

- Retención conforme a normativas y auditorías.

- Correlación entre logs de microservicios.

- Detección automática de anomalías mediante ML/AI.

##### Métricas

- Latencia, throughput, tasa de errores y saturación de recursos.

- Métricas técnicas y de negocio.

- Dashboards en tiempo real para monitoreo operativo 24/7.

##### Trazas Distribuidas

- Seguimiento de solicitudes de extremo a extremo.

- Identificación de cuellos de botella y servicios degradados.

- Detección de saltos anómalos entre componentes.

La observabilidad es fundamental para soportar prácticas SRE, permitiendo diagnosticar problemas complejos y optimizar la operación continua del sistema.

<!-- Página 203 del PDF original -->

#### 12.2.3 Automatización y Reducción de Toil

La automatización es un pilar central del plan operativo. Las tareas repetitivas y propensas a error manual se reemplazan por procesos automáticos.

##### Tareas Automatizadas

- Monitoreo continuo de métricas y salud del sistema.

- Autoescalado de recursos según demanda.

- Provisionamiento mediante Infrastructure as Code.

- Despliegues automáticos a través de pipelines CI/CD.

- Rotación automatizada de llaves y certificados.

- Reinicios controlados ante degradación.

- Alertas inteligentes basadas en modelos ML.

##### Reducción del Toil

El trabajo manual repetitivo se minimiza mediante:

- Documentación y estandarización de procedimientos.

- Identificación de tareas repetitivas y automatización progresiva.

- Meta operativa: toil menor al 30% de la carga del equipo SRE.

#### 12.2.4 SLO, SLA y Error Budgets

La operación se gestiona mediante acuerdos de nivel de servicio claros. Los Service Level Objectives definen objetivos técnicos medibles, mientras que los Service Level Agreements formalizan compromisos contractuales.

##### SLO Propuestos

- Disponibilidad: mayor o igual a 99.5% anual.

- Latencia P95: menor a 350 ms.

- Tasa de errores: menor a 2%.

##### Error Budgets

El error budget representa la porción aceptable de falla dentro del período evaluado. Cuando el presupuesto de error se agota:

- Se detienen nuevos despliegues.

- Se priorizan mejoras de confiabilidad.

- Se activa un análisis postmortem obligatorio.

Esto permite equilibrar innovación y estabilidad mediante decisiones informadas.

<!-- Página 204 del PDF original -->

#### 12.2.5 Chaos Engineering

Para validar la resiliencia del sistema, se aplican pruebas controladas de Chaos Engineering que permiten identificar fallas ocultas antes de que ocurran en producción.

##### Objetivos

- Validar tolerancia a fallos del sistema.

- Medir tiempos de recuperación.

- Identificar debilidades estructurales.

##### Ejemplos de Pruebas

- Derribo controlado de microservicios.

- Simulación de alta latencia en la red.

- Interrupción temporal de conexiones a la base de datos.

- Generación artificial de carga o saturación de recursos.

Las pruebas se realizan siempre en ambientes controlados y documentados.

#### 12.2.6 Gestión de Incidentes y Blameless Postmortems

##### Gestión de Incidentes

- Detección automática y clasificación según severidad.

- Ejecución de protocolos estandarizados de respuesta.

- Comunicación oportuna con las partes interesadas.

- Registro detallado del incidente en sistemas de ticketing.

##### Blameless Postmortems

Después de incidentes significativos se realiza un análisis retrospectivo sin asignación de culpas, enfocado en el aprendizaje organizacional. Los postmortems deben incluir:

- Línea de tiempo del incidente.

- Análisis de causas raíz.

- Impacto técnico y operativo.

- Acciones correctivas y preventivas.

Esta práctica fomenta una cultura de mejora continua y transparencia operacional.

#### 12.2.7 Prácticas FinOps para Optimización de Costos

El modelo operacional incorpora principios FinOps para controlar y optimizar los costos asociados a la operación de la solución.

<!-- Página 205 del PDF original -->

##### Acciones FinOps

- Ajuste de tamaño de recursos.

- Eliminación de servicios infrautilizados.

- Automatización de apagado de entornos no productivos.

- Monitoreo de costos en tiempo real.

- Alertas por sobreconsumo o anomalías de gasto.

- Evaluación y proyección mensual de costos.

##### Resultados Esperados

- Reducción de costos innecesarios.

- Operación eficiente sin sacrificar confiabilidad.

- Optimización continua del presupuesto asignado.

<!-- Página 206 del PDF original -->

## 13 Equipo de trabajo, Subcontrataciones y Alianzas

### 13.1 Estructura Organizacional del Proyecto

La propuesta para la Empresa de Consultas Médicas se apoya en un equipo multidisciplinario que cubre de forma explícita los roles exigidos en las bases: Project Manager, arquitecto de soluciones, líder técnico, líder funcional, especialista en ciberseguridad, QA Lead, ingenieros DevOps/SRE, ingenieros de datos y desarrolladores full-stack. La estructura organizacional se organiza en dos grandes capas complementarias:

- Capa de Gobierno/Jefaturas, responsable de la conducción estratégica, la relación con el cliente y la toma de decisiones transversales del proyecto.

- Capa de Ejecución Técnica de la Solución, responsable de materializar la arquitectura propuesta en software, infraestructura, datos e interoperabilidad clínica, asegurando calidad y continuidad operativa.

A continuación se detallan los diferentes organigramas e interacciones que componen esta estructura.

#### 13.1.1 Organización del equipo de firmas

Figure 13.1: Organización del equipo de firmas del proponente.

La Figura 13.1 presenta el equipo de firmas responsable de la propuesta y de la relación contractual con la Empresa de Consultas Médicas. En el vértice se encuentra el Jefe de

![Página 206 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-206.png)

<!-- Página 207 del PDF original -->

Proyecto Felipe Bravo, quien asumirá el rol de Project Manager / Scrum Master, coordinando el plan de trabajo, la gestión de riesgos y el cumplimiento de los hitos comprometidos.

Bajo su conducción se agrupan las jefaturas expertas que representan las disciplinas críticas del proyecto:

- Francisco Cortés (Arquitecto de Software Senior): lidera la definición de la arquitectura de soluciones.

- Luciano Oliva (Analista de Negocios y Adquisiciones Experto): articula los requerimientos funcionales con los procesos clínicos y administrativos.

- Antonia Navarrete (Especialista en Ciberseguridad): asegura el alineamiento con PNCS, Ley 21.719 y estándares de seguridad.

- Matías Bugueño (Experto en Redes y Bases de Datos): cubre el dominio de infraestructura, comunicaciones e ingeniería de datos.

- Esteban Carrasco (Jefe Experto en Testing y QA): lidera la estrategia de calidad.

- Carlos Da Silva (Jefe Desarrollador de Software / Backend Senior): encabeza la implementación de la plataforma HospiNet.

- Fabrizzio Mura (Jefe Diseñador UI/UX): asegura una experiencia de usuario centrada en pacientes y personal clínico.

Este núcleo de firmas muestra desde el inicio la composición multidisciplinaria y senior del equipo.

#### 13.1.2 Visión general de la estructura organizacional

Figure 13.2: Estructura organizacional completa del proyecto HospiNet.

La Figura 13.2 resume la estructura organizacional global del proyecto. En la parte superior se representa la Capa de Gobierno/Jefaturas, donde se materializan los roles mínimos definidos en las bases (Project Manager, Arquitecto de Soluciones, Líder Técnico, Líder Funcional, Change Manager y QA Lead), ampliados con jefaturas especializadas en ciberseguridad, redes/DB y desarrollo.

En la parte inferior se despliega la Capa de Ejecución Técnica de la Solución, organizada en frentes coherentes con la complejidad del proyecto sanitario:

![Página 207 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-207.png)

<!-- Página 208 del PDF original -->

- Funcional, QA & Documentación: analistas de negocio, testers/QA engineers y documentadores.

- Integración, Infraestructura & Soporte: equipo de integración HL7/FHIR, DevSecOps/SRE, soporte de primer nivel e ingeniería de redes y datos.

- Desarrollo & UX: jefatura de desarrollo, jefatura de UX/UI y células de desarrolladores front-end, back-end y full-stack.

Una banda central denominada Modelo de datos / redes explicita que las decisiones de datos clínicos, interoperabilidad y redes son transversales a todos los frentes; allí confluyen el arquitecto de software, el experto en redes y DBA, el equipo DevSecOps/SRE y los líderes de desarrollo para garantizar trazabilidad de datos, alta disponibilidad y cumplimiento de requisitos no funcionales (performance, escalabilidad y seguridad).

#### 13.1.3 Capa de Gobierno / Jefaturas

Figure 13.3: Capa de Gobierno y Jefaturas del proyecto.

La Figura 13.3 amplía la Capa de Gobierno/Jefaturas. En el centro se ubica el Gerente de Proyecto, responsable del alineamiento estratégico con la Empresa de Consultas Médicas, la supervisión de plazos, el control de costos y la comunicación con las contrapartes clínicas y TI del cliente.

Desde el Gerente de Proyecto se desprenden las principales jefaturas:

- Jefe Arquitecto de Software: actúa como Solution Architect, define la arquitectura lógica y física, las decisiones de integración (APIs, buses HL7/FHIR), los patrones de diseño y la evolución tecnológica.

- Líder Técnico / Jefe de Desarrollo: coordina a los equipos de desarrollo frontend, back-end y full-stack, asegurando la correctitud técnica, la calidad del código y la implementación de la integración continua.

- Líder Funcional / BA: lidera el levantamiento y priorización de requerimientos junto a los usuarios clave, mantiene la trazabilidad requerimiento-épica-historiacaso de prueba y resuelve dudas funcionales del equipo técnico.

- Jefe Analista de Negocios y Adquisiciones: gestiona la relación con proveedores, licencias y servicios externos (nube, data center, soluciones de terceros), velando por la optimización de costos y la alineación contractual.

- Change Manager: diseña e implementa el plan de gestión del cambio organizacional, asegurando adopción por parte de médicos, administrativos y call center, y coordinando capacitaciones y estrategias de comunicación.

![Página 208 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-208.png)

<!-- Página 209 del PDF original -->

- Jefe Experto en Testing y QA: define la estrategia de aseguramiento de calidad (plan de pruebas, criterios de aceptación, automatización), coordina a los QA engineers y lidera la validación integral antes de cada despliegue.

- Jefe Especialista en Ciberseguridad: responsable de que la solución cumpla con PNCS, Ley 21.663 y buenas prácticas de seguridad; define controles de hardening, gestión de identidades, monitoreo de eventos de seguridad y respuesta ante incidentes.

- Jefe Redes y DBA: lidera la arquitectura de redes, segmentos clínicos y perímetro seguro, además del diseño de bases de datos, replicación, backup y plan de recuperación ante desastres.

Esta capa de gobierno concentra la responsabilidad de las decisiones críticas del proyecto y asegura que cada frente técnico disponga de una jefatura especializada, demostrando madurez en gestión de proyectos TIC complejos.

#### 13.1.4 Capa de Ejecución Técnica de la Solución

Figure 13.4: Capa de Ejecución Técnica de la Solución.

La Capa de Ejecución Técnica de la Solución es donde la arquitectura definida por las jefaturas se convierte en un sistema operativo real para la Empresa de Consultas Médicas. En esta capa trabajan los equipos que diseñan, implementan, prueban, despliegan y operan la plataforma HospiNet en el día a día, en contacto directo con los usuarios clave del hospital.

Esta capa se organiza en tres dominios especializados, que colaboran de forma coordinada:

1. Funcional, QA & Documentación: transforma los procesos clínicos y adminis-

trativos en requerimientos trazables, diseña los casos de prueba y genera toda la documentación necesaria para la operación y el soporte.

2. Integración, Infraestructura & Soporte: se responsabiliza de la interoperabili-

dad HL7/FHIR con sistemas legados, de la arquitectura de datos y redes, de la automatización DevSecOps/SRE y del soporte técnico de primer nivel.

3. Desarrollo & UX: implementa los microservicios, APIs, frontends y aplicaciones

móviles/escritorio, cuidando tanto la calidad técnica del código como la experiencia de usuario de médicos, administrativos y pacientes.

![Página 209 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-209.png)

<!-- Página 210 del PDF original -->

En un flujo típico de trabajo, un nuevo requerimiento de la Empresa de Consultas Médicas es levantado por el equipo funcional, refinado junto al Líder Técnico y al Jefe de Arquitectura, priorizado en el backlog y asignado a una célula de desarrollo. Los desarrolladores implementan la funcionalidad respetando los patrones definidos; el equipo DevSecOps/SRE la incorpora al pipeline de integración continua; el equipo de QA diseña y ejecuta pruebas funcionales, de regresión y de seguridad; y, finalmente, DevSecOps despliega en ambiente productivo con monitoreo y mecanismos de rollback. El Ingeniero de Soporte y los Documentadores se aseguran de que la nueva capacidad quede integrada en los procedimientos operativos del hospital.

Las siguientes subsecciones realizan un zoom sobre cada uno de los bloques de la Figura 13.4. El objetivo es que el cliente visualice, con mayor detalle, cómo se componen los equipos y qué responsabilidades tiene cada rol, manteniendo siempre el contexto de que todos forman parte de la misma Capa de Ejecución Técnica.

##### Zoom: Frente Funcional, QA y Documentación

Figure 13.5: Zoom del frente Funcional, QA & Documentación dentro de la Capa de Ejecución Técnica.

La Figura 13.5 representa un zoom sobre el bloque Funcional, QA & Documentación de la Figura 13.4. Es decir, seguimos dentro de la Capa de Ejecución Técnica, pero profundizando en cómo se organizan los equipos que traducen las necesidades del hospital en requerimientos verificables y documentados.

Analistas de Negocio. Trabajan bajo la conducción del Líder Funcional/BA y son el puente directo con médicos, enfermeras, personal de admisión, call center y administración. Su responsabilidad es:

![Página 210 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-210.png)

<!-- Página 211 del PDF original -->

- Levantar y modelar procesos (as-is y to-be) de agendamiento, atención médica, telemedicina, facturación, cobranzas, etc.

- Redactar historias de usuario, criterios de aceptación y reglas de negocio, manteniendo trazabilidad con los requerimientos del contrato.

- Priorizar, junto al cliente y al Gerente de Proyecto, el backlog funcional de cada iteración.

En términos prácticos, un analista de negocio acompaña sesiones de trabajo con especialistas clínicos, valida prototipos de pantallas con el equipo de UX y resuelve dudas funcionales de los desarrolladores.

Testers / Analistas QA. Coordinados por el Jefe Experto en Testing y QA, diseñan y ejecutan la estrategia de aseguramiento de calidad del proyecto:

- Elaboran planes de prueba funcional, de integración, regresión, performance y pruebas específicas de seguridad en coordinación con ciberseguridad (Secure SDLC).

- Automatizan pruebas críticas (por ejemplo, flujos de agendamiento, registro de consulta y emisión de documentos clínicos), utilizando herramientas de testing continuo integradas al pipeline DevOps.

- Generan informes de defectos, métricas de cobertura y criterios de salida para cada release, que son revisados en conjunto con el Gerente de Proyecto y el cliente.

En un contexto real, son quienes validan que una nueva versión de HospiNet no rompa flujos existentes y que las correcciones sean verificadas antes de migrar a producción.

Documentadores. Son responsables de que todo el conocimiento del sistema quede plasmado en artefactos formales:

- Elaboran manuales de usuario para médicos, personal administrativo y operadores de call center.

- Generan manuales técnicos, diagramas de arquitectura, descripciones de APIs y procedimientos de operación y contingencia.

- Mantienen un repositorio de documentación versionada alineado con las releases del sistema, de manera que soporte y operación siempre dispongan de información actualizada.

Organizativamente, los documentadores trabajan en estrecha coordinación con el Change Manager y el Líder Funcional/BA. El Change Manager define los mensajes clave, los planes de capacitación y las comunicaciones de cambio hacia los usuarios finales, mientras que los documentadores los materializan en manuales, guías rápidas y material formativo. De esta forma, la documentación no sólo describe la solución desde el punto de vista técnico, sino que se alinea explícitamente con la estrategia de gestión del cambio del hospital.

<!-- Página 212 del PDF original -->

##### Zoom: Integración HL7/FHIR, Infraestructura y Soporte

Figure 13.6: Zoom del frente de Integración, Infraestructura & Soporte dentro de la Capa de Ejecución Técnica.

La Figura 13.6 realiza un zoom sobre el bloque Integración, Infra/DB & DevOps de la Figura 13.4. Seguimos dentro de la Capa de Ejecución Técnica, pero ahora se detalla la organización interna de los equipos que garantizan interoperabilidad, disponibilidad y soporte operativo.

Jerárquicamente, estos roles se enmarcan bajo las jefaturas de la Capa de Gobierno/Jefaturas:

- El Jefe Redes y DBA lidera la operación de infraestructura, redes y bases de datos, así como a DevSecOps/SRE, al Diseñador de Base de Datos y al Ingeniero de Soporte.

- El Jefe Arquitecto de Software define los lineamientos de integración y modelo de datos, supervisando al equipo de Integración HL7/FHIR junto con el Jefe Redes y DBA.

- La Especialista en Ciberseguridad establece los controles de seguridad que DevSecOps/SRE debe implementar en la plataforma.

Equipo de Integración HL7/FHIR. Está compuesto por ingenieros especializados en interoperabilidad clínica y es liderado técnicamente por el Jefe Arquitecto de Software, en coordinación con el Jefe Redes y DBA. Sus responsabilidades son:

- Diseñar e implementar interfaces HL7/FHIR entre HospiNet y sistemas legados (HIS, RIS, LIS, PACS, contabilidad).

- Configurar motores de integración, colas de mensajería y adaptadores específicos para cada proveedor.

- Definir reglas de mapeo y transformación de datos clínicos, asegurando consistencia e integridad entre plataformas.

![Página 212 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-212.png)

<!-- Página 213 del PDF original -->

Esta dependencia jerárquica asegura que las decisiones de integración sean coherentes con la arquitectura de soluciones y con la topología de redes del hospital.

Técnico de Hardware. Reporta operacionalmente al Jefe Arquitecto de Software y al Jefe Redes y DBA, dado que su foco está en la capa física de la infraestructura:

- Gestiona equipamiento de red local, terminales de consulta, kioscos de autoatención y dispositivos especializados (por ejemplo, cámaras para telemedicina).

- Coordina con proveedores de hardware la instalación, garantías y renovaciones.

- Trabaja junto al equipo de integración para validar la conectividad extremo a extremo.

DevSecOps/SRE. Este equipo combina prácticas de Development, Security y Site Reliability Engineering y está liderado por el Jefe Redes y DBA en la dimensión operativa, y por la Especialista en Ciberseguridad en la dimensión de controles de seguridad:

- Define y mantiene el pipeline de integración y despliegue continuo (CI/CD), incorporando pruebas automáticas y chequeos de seguridad.

- Implementa infraestructura como código, monitoreo centralizado, alertas y tableros de observabilidad (latencias, errores, uso de recursos).

- Diseña y prueba planes de contingencia, respaldos, replicación, failover y tiempos objetivo de recuperación (RTO/RPO) acordes a la criticidad clínica del sistema.

Esta doble línea de liderazgo garantiza que las decisiones de operación tengan en cuenta tanto la continuidad del servicio como el cumplimiento normativo en ciberseguridad.

Diseñador de Base de Datos. Asume el rol de ingeniero de datos del proyecto y reporta funcionalmente al Jefe Arquitecto de Software y operacionalmente al Jefe Redes y DBA:

- Modela los datos clínicos y administrativos, aplicando estrategias de normalización/desnormalización según los patrones de acceso.

- Diseña índices, particionamiento, estrategias de archivado y replicación, respetando las restricciones de confidencialidad y retención de la información de salud.

- Colabora con el equipo de integración y desarrollo para optimizar queries críticas (por ejemplo, búsquedas de pacientes, agenda de médicos, vistas de indicadores de gestión).

Ingeniero de Soporte. Depende jerárquicamente del Jefe Arquitecto de Software junto con el Jefe Redes y DBA y estos se coordina operacionalmente con el Gerente de Proyecto para cumplir los SLA acordados con el hospital:

- Recibe incidentes y requerimientos de los usuarios finales (mesa de ayuda), realiza diagnóstico inicial y resuelve los casos de baja complejidad.

<!-- Página 214 del PDF original -->

- Escala incidencias al equipo de desarrollo o DevSecOps según criticidad y tipo de problema, manteniendo al cliente informado del progreso.

- Registra métricas de incidentes (SLA, tiempos de respuesta, causas raíz) que alimentan el ciclo de mejora continua.

##### Zoom: Desarrollo y Experiencia de Usuario

Figure 13.7: Zoom del frente de Desarrollo & UX dentro de la Capa de Ejecución Técnica.

La Figura 13.7 corresponde al zoom del bloque Desarrollo & UX de la Figura 13.4. Este frente es responsable de construir las aplicaciones que verán los usuarios del hospital: módulos clínicos, portales de pacientes, herramientas de gestión y tableros de control.

Dentro de la estructura organizacional, el frente de Desarrollo & UX está liderado por el Líder Técnico / Jefe de Desarrollo desde la Capa de Gobierno/Jefaturas. Bajo su conducción se encuentran el Jefe Desarrollador de Software y el Jefe Diseñador UI/UX, quienes a su vez dirigen a los equipos de desarrolladores front-end, backend, full-stack y diseñadores de experiencia de usuario. Esta jerarquía asegura que las decisiones técnicas y de diseño se mantengan consistentes con la arquitectura global del proyecto.

![Página 214 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-214.png)

<!-- Página 215 del PDF original -->

Liderazgo del Líder Técnico / Jefe de Desarrollo. En el organigrama se observa que el Líder Técnico / Jefe de Desarrollo tiene flechas hacia el Jefe Desarrollador de Software, el Jefe Diseñador UI/UX y el bloque de Desarrolladores de Software. Esto refleja que supervisa la ingeniería global del frente de Desarrollo & UX y valida las decisiones estructurales de arquitectura y prioridades técnicas. Sin embargo, para evitar líneas de mando duplicadas, el reporte operativo diario de los desarrolladores se canaliza exclusivamente a través del Jefe Desarrollador de Software; y cuando se trata de problemas de diseño, interacción o lineamientos visuales, dicho jefe coordina y eleva los temas con el Jefe de UX/UI. De este modo, las líneas cruzadas en el organigrama indican una coordinación funcional entre jefaturas, manteniendo una cadena de mando clara hacia los desarrolladores.

Jefe Desarrollador de Software (Carlos Da Silva). Lidera técnicamente a los equipos de desarrollo y reporta al Líder Técnico/Jefe de Desarrollo:

- Define estándares de codificación, revisión de código, uso de frameworks y patrones de diseño.

- Coordina el trabajo de las células front-end, back-end y full-stack, asegurando alineamiento con la arquitectura definida por el Jefe Arquitecto de Software.

- Trabaja estrechamente con DevSecOps para incorporar prácticas de seguridad y rendimiento desde las primeras etapas de desarrollo.

Jefe Diseñador UI/UX (Fabrizzio Mura). Responsable de la experiencia de usuario en todos los canales y reporta al Líder Técnico/Jefe de Desarrollo, manteniendo a la vez una coordinación permanente con el Líder Funcional/BA:

- Lidera el diseño de interfaces para médicos, administrativos, call center y pacientes, aplicando principios de usabilidad, accesibilidad y diseño centrado en el usuario.

- Conduce pruebas de usabilidad con usuarios reales del hospital y traduce sus hallazgos en mejoras de interacción.

- Colabora con analistas de negocio y desarrolladores para asegurar que las pantallas reflejen fielmente los flujos clínicos y administrativos.

Desarrolladores Front-End. Especializados en la capa de presentación y dependen jerárquicamente del Jefe Desarrollador de Software, manteniendo una línea funcional con el Jefe Diseñador UI/UX:

- Implementan interfaces web y móviles siguiendo los diseños de UX/UI.

- Integran las vistas con APIs seguras, manejando estados, internacionalización y validaciones de datos en el cliente.

- Optimizan el rendimiento y la accesibilidad de la interfaz, clave para contextos de alta carga de trabajo en boxes de atención y call center.

<!-- Página 216 del PDF original -->

Desarrolladores Back-End. Responsables de la lógica de negocio y las integraciones,

##### reportan al Jefe Desarrollador de Software:

- Implementan microservicios, APIs REST/GraphQL y procesos batch que soportan los flujos críticos de la plataforma.

- Integran el sistema con motores de mensajería, colas de eventos y servicios externos (por ejemplo, firma electrónica, pasarelas de pago, servicios de mensajería SMS/email).

- Aplican patrones de diseño orientados al dominio para garantizar mantenibilidad y extensibilidad de la solución.

Desarrolladores Full-Stack. Perfil versátil que trabaja tanto en front-end como en back-end y depende del Jefe Desarrollador de Software, actuando como puente entre las distintas capas:

- Refuerza las células de desarrollo en funcionalidades complejas donde se requiere una visión extremo a extremo (por ejemplo, módulos de telemedicina o portal de pacientes).

- Actúa como nexo técnico entre las decisiones de UX, la lógica de negocio y las restricciones de infraestructura.

- Participa activamente en la resolución de incidencias de producción que requieren ajustes rápidos en varias capas de la aplicación.

Con este nivel de detalle, la Capa de Ejecución Técnica de la Solución muestra cómo el proponente articula un equipo multidisciplinario completo, capaz de llevar a producción un sistema de consultas médicas de alta criticidad, mantenerlo operativo 24/7 y evolucionarlo de manera segura y controlada conforme cambien las necesidades del hospital y la normativa vigente.

### 13.2 Subcontrataciones y alianzas estratégicas

La estrategia de subcontrataciones y alianzas estratégicas se define desde una lógica de make-or-buy alineada con los objetivos de Consultas Médicas S.A.: mantener el control sobre los componentes que representan ventaja competitiva y conocimiento de dominio (procesos clínicos, integración HL7, modelo de datos clínico-administrativo), y apoyarse en partners especializados para servicios de infraestructura, conectividad y aplicaciones de soporte que requieren capacidad instalada, certificaciones y un track record probado.

En este contexto, las decisiones se agrupan en dos bloques: (i) componentes make, desarrollados, configurados y operados por el equipo de proyecto (HospiNet, integración HL7/FHIR, modelo de datos, automatización operacional, etc.), y (ii) componentes buy, contratados a proveedores con capacidades técnicas específicas (Servicios

<!-- Página 217 del PDF original -->

AWS para los distintos ambientes y Outposts por clínica, ISPs Entel y Claro, Microsoft 365, Talana, Transbank, Klap, SolarWinds, PostgreSQL, VPN WireGuard, entre otros).

#### 13.2.1 Criterios make-or-buy

Las decisiones make-or-buy se tomaron considerando los siguientes criterios:

- Capacidad técnica y conocimiento de dominio. Se opta por make en aquellos componentes donde el valor principal del proyecto es el entendimiento profundo de los procesos clínicos y administrativos del mandante. En particular:

  - Diseño, desarrollo y evolución de la plataforma HospiNet y sus módulos funcionales.

  - Diseño del modelo de datos operativo y analítico, incluyendo parametrizaciones clínicas y administrativas.

  - Implementación de la capa de integración HL7/FHIR y los flujos de interoperabilidad con sistemas externos.

  - Definición de la arquitectura de referencia, automatización de despliegues (IaC) y prácticas de SRE asociadas.

En estos ámbitos el equipo del proponente asume responsabilidad directa, consolidando conocimiento en la organización del mandante y evitando dependencia de terceros para componentes core.

- Economías de escala, certificaciones y continuidad de servicio. Se opta por buy en servicios de infraestructura, conectividad y aplicaciones de soporte donde existe oferta madura y altamente estandarizada, con fuertes economías de escala y exigencia de certificaciones:

  - Plataforma de infraestructura: Servicios AWS para Producción, DRS, Dev, QA, Capacitación y servicios generales, incluyendo Servicio Outpost por clínica para acercar capacidad de cómputo a los recintos asistenciales.

  - Conectividad: proveedores ISP Entel y Claro para enlaces de datos y salida a Internet, permitiendo esquemas de redundancia y alta disponibilidad.

  - Aplicaciones y servicios de soporte: Microsoft Office 365 E3 para colaboración y productividad, Talana para gestión de personas, Transbank/Klap para medios de pago electrónicos, SolarWinds para monitoreo de redes y plataformas, PostgreSQL como motor de base de datos y VPN WireGuard para túneles seguros.

En estos casos, el foco está en aprovechar la infraestructura, certificaciones y track record de los proveedores, mientras el equipo del proponente se concentra en la lógica de negocio y la integración.

- Riesgo, plazos y costo total de propiedad (TCO). Para componentes donde el desarrollo ad hoc implicaría riesgo elevado, plazos incompatibles con el cronograma del proyecto o costos de mantención poco sostenibles (por ejemplo, montar un data center propio, desarrollar un sistema de medios de pago o una suite

<!-- Página 218 del PDF original -->

ofimática), se privilegió contratar soluciones consolidadas. Esto permite reducir el TCO, acotar riesgos operacionales y acelerar la puesta en marcha.

- Control estratégico vs. delegación operativa. La estrategia distingue entre:

  - Control estratégico: HospiNet, modelo de datos, integración, procesos y reglas de negocio, que permanecen bajo diseño y gobierno del proponente y del mandante.

  - Delegación operativa: servicios de infraestructura, comunicaciones y soluciones SaaS de soporte, donde la operación diaria recae en partners especializados, sin ceder el control sobre la gobernanza general ni sobre los datos del mandante.

#### 13.2.2 Selección de partners

La selección de partners se fundamenta en la alineación técnica con la arquitectura propuesta, la existencia de certificaciones relevantes, la capacidad de ofrecer contratos con SLA explícitos y un track record comprobable en servicios críticos.

- Proveedor de infraestructura: Servicios AWS. Se seleccionan los Servicios AWS para los ambientes de Producción, DRS, Dev, QA, Capacitación y servicios generales, junto con Outposts por clínica. Esto permite:

  - Contar con una plataforma cloud madura, soportada por centros de datos con altos estándares de seguridad y disponibilidad.

  - Habilitar arquitecturas híbridas (cloud + Outposts en las clínicas), coherentes con los requerimientos de latencia, continuidad operativa y protección de datos de salud.

  - Integrar nativamente servicios de monitoreo, registro, escalamiento y automatización que el equipo SRE del proponente utilizará para operar HospiNet.

- Proveedores de conectividad: Entel y Claro. La contratación de ISP Entel y Claro permite diseñar una topología con redundancia de enlaces para los recintos del mandante, reduciendo el riesgo de caída por falla de un solo carrier. Este esquema se complementa con túneles VPN basados en WireGuard para asegurar la comunicación cifrada entre las clínicas, los servicios cloud y los usuarios remotos autorizados.

- Aplicaciones y servicios de soporte. Se incorporan como aliados tecnológicos:

  - Microsoft Office 365 E3, como plataforma de colaboración y productividad que respalda la gestión del proyecto y la operación diaria del mandante (correo, reuniones, documentos, etc.).

  - Talana, para la gestión de personas y procesos de RR.HH., reduciendo la necesidad de desarrollar funcionalidades de soporte que no pertenecen al core clínico de HospiNet.

<!-- Página 219 del PDF original -->

  - Transbank y Klap, para la captura de pagos a través de máquinas POS, asegurando cumplimiento de estándares del ecosistema financiero y facilitando la conciliación con los módulos de finanzas.

  - SolarWinds, como herramienta especializada para monitoreo de redes y plataformas, integrada con la estrategia de observabilidad del proyecto.

  - PostgreSQL, como motor de base de datos relacional robusto y ampliamente utilizado, coherente con la arquitectura lógica y con la estrategia de operación y respaldo.

La combinación de estos partners permite sostener la solución con una base tecnológica probada, mientras el equipo del proponente mantiene el foco en la ingeniería de HospiNet y en la integración con los procesos de Consultas Médicas S.A.

#### 13.2.3 Gobernanza de proveedores (SLA/OLA)

La relación con proveedores se gestiona bajo un modelo de gobernanza que articula: (i) los SLA contractuales de cada partner y (ii) los OLA internos del equipo del proponente y del mandante.

- SLA con proveedores externos. Cada servicio contratado (Servicios AWS, ISPs, Microsoft 365, Talana, Transbank/Klap, SolarWinds, etc.) se rige por acuerdos de nivel de servicio que consideran, como mínimo:

  - Disponibilidad comprometida del servicio.

  - Tiempos de respuesta y de resolución por severidad de incidente.

  - Ventanas de mantenimiento y procedimientos de comunicación de cambios.

  - Mecanismos de escalamiento y canales de soporte.

- OLA internos y coordinación con el modelo de operación. Sobre la base de estos SLA se definen OLA internos del equipo de operación de HospiNet (SRE, DevOps, soporte funcional y técnico), de modo que los tiempos de atención al usuario final sean coherentes con las obligaciones contractuales hacia el mandante. El Jefe de Proyecto y las jefaturas técnicas supervisan el cumplimiento de estos acuerdos en comités periódicos.

- Seguimiento y control. Se utilizarán paneles de monitoreo y reportes periódicos para controlar:

  - Tiempos de indisponibilidad atribuibles a cada proveedor.

  - Volumen y tiempo de resolución de incidentes.

  - Tendencias de capacidad y uso de recursos.

Cuando corresponda, se aplicarán los mecanismos de compensación o penalidades definidos contractualmente.

<!-- Página 220 del PDF original -->

#### 13.2.4 Riesgos y mitigaciones

La incorporación de terceros introduce riesgos específicos que se gestionan de forma explícita:

- Dependencia de proveedor cloud e infraestructura: La concentración de cargas en Servicios AWS (incluyendo Outposts) puede generar dependencia tecnológica. Para mitigarla, la solución se diseña sobre estándares abiertos, contenedores y prácticas de IaC, facilitando la portabilidad de cargas en caso de ser necesario.

- Fallas de conectividad: Una indisponibilidad prolongada de un ISP puede afectar el acceso a HospiNet. La doble contratación de Entel y Claro, más el uso de VPN WireGuard, permite establecer rutas alternativas y mecanismos de conmutación por falla.

- Cambios comerciales o de servicio en soluciones SaaS: Cambios en condiciones comerciales de Microsoft 365, Talana, Transbank o Klap pueden impactar los costos o la continuidad de ciertos servicios de soporte. Para mitigarlo, la integración se realiza a través de APIs y adaptadores desacoplados, de forma que sea posible evaluar y sustituir proveedores en caso necesario.

- Riesgos asociados a herramientas de monitoreo: Una falla en SolarWinds podría reducir la visibilidad sobre la infraestructura. Por ello, se complementa su uso con capacidades de monitoreo nativas de la plataforma cloud y con alertas configuradas en los propios servicios de infraestructura.

De esta forma, la estrategia de subcontrataciones y alianzas estratégicas equilibra control sobre los componentes críticos de HospiNet, aprovechamiento de partners especializados y una gobernanza explícita de los riesgos asociados a terceros.

### 13.3 Transferencia tecnológica y gestión del conocimiento

La transferencia tecnológica y la gestión del conocimiento se conciben como un proceso transversal a todo el ciclo de vida del proyecto HospiNet, y no como una actividad puntual de cierre. La estrategia propuesta busca que Consultas Médicas S.A. quede en condiciones de operar, mantener y evolucionar la plataforma de forma autónoma, articulando coherentemente el Plan de Trabajo (Fases 6 Capacitaciones, 8 Finalización del Proyecto y 9 Mantención), los servicios de operación y soporte, y la estructura organizacional descrita en este capítulo.

En este contexto, la gestión del conocimiento se apoya tanto en los roles definidos (equipo de documentación, Change Manager, jefaturas técnicas y funcionales) como en los entregables formales de la EDT (manuales, wiki, base de conocimiento, lecciones aprendidas), y en las plataformas colaborativas definidas para el proyecto.

Los principales mecanismos de transferencia tecnológica y gestión del conocimiento son los siguientes:

<!-- Página 221 del PDF original -->

- Plan estructurado de transferencia de conocimiento al mandante. La transferencia de conocimiento hacia Consultas Médicas S.A. se organiza sobre la base del paquete de Capacitaciones, que incluye: (i) formación de instructores internos (train-the-trainer) por rol clave, (ii) rutas de aprendizaje diferenciadas para perfiles clínicos, administrativos y de TI, (iii) sesiones B-learning apoyadas en el ambiente de Capacitación y en datos y flujos reales del sistema, y (iv) evaluaciones y certificaciones de participación. Adicionalmente, se realizan talleres de traspaso específicos por dominio/módulo (HCE, agendamiento, finanzas, cadena de suministro, gestión y BI), en los que se recorren procesos TO-BE, parametrizaciones y casos de uso típicos y críticos.

- Ecosistema documental y repositorios colaborativos. Todo el conocimiento generado durante el proyecto se consolida en un ecosistema documental único, respaldado por repositorios bajo control de versiones (Git y estrategia de ramificación tipo GitFlow/GitHub Flow, con versionado semántico). Sobre esta base se mantienen: (i) la documentación técnica (arquitectura lógica y física, integraciones, APIs, configuraciones de infraestructura e IaC), (ii) los manuales de usuario, administración y operación, (iii) los registros de decisiones de arquitectura (ADRs) y acuerdos de comité, y (iv) las políticas y procedimientos operacionales. Toda esta documentación se expone en una wiki corporativa (por ejemplo, Confluence) accesible para los equipos del cliente, lo que permite búsqueda centralizada, trazabilidad de cambios y actualización continua.

- Base de conocimiento, runbooks y playbooks operacionales. En línea con el modelo de operación y SRE, se implementa una base de conocimiento colaborativa donde se documentan incidentes tipo, causas raíces, procedimientos de resolución, preguntas frecuentes y buenas prácticas de uso de HospiNet. Esta KB se alimenta tanto desde el equipo de soporte como desde usuarios clave del mandante. En paralelo, se construyen runbooks y playbooks operacionales que estandarizan la atención de incidentes y la ejecución de tareas recurrentes (gestión de ambientes, monitoreo, backups, procedimientos de degradación y recuperación, etc.). Estos artefactos se integran con la herramienta de gestión de tickets (Jira Service Management) y con la plataforma de observabilidad, habilitando automatización y auto-remediación cuando sea técnicamente viable.

- Gestión del conocimiento interno del equipo de proyecto. A nivel del equipo del proponente, se aplican prácticas de ingeniería que reducen el riesgo de concentración de conocimiento: pair programming en componentes críticos, code reviews sistemáticos, rotación de desarrolladores entre módulos y frentes de trabajo, y sesiones periódicas de revisión técnica. Esto se complementa con la disciplina de Documentation as Code exigida en las Bases, de modo que tanto el código como la documentación y los scripts de infraestructura queden versionados y auditables. Las decisiones relevantes se registran en ADRs y en actas de comités, lo que permite entender el porqué de cada diseño incluso ante cambios de equipo.

- Continuidad del conocimiento y cierre ordenado. Hacia el final del proyecto,

<!-- Página 222 del PDF original -->

la Fase de Finalización consolida la transferencia tecnológica mediante: (i) la entrega y revisión conjunta del estado de cumplimiento de requerimientos, (ii) la validación y actualización final de todos los manuales y de la base de conocimiento, (iii) la publicación de una wiki para trabajadores del hospital con guías operativas y de auto-servicio, y (iv) la realización de sesiones formales de handover entre el equipo de proyecto y los equipos de operación del cliente. Asimismo, se documentan y socializan las lecciones aprendidas, tanto técnicas como organizacionales, dejándolas integradas en la KB para futuras mejoras o extensiones del sistema.

Con este enfoque, la transferencia tecnológica deja de ser un hito aislado y se convierte en un proceso continuo de captura, formalización y difusión del conocimiento, asegurando que Consultas Médicas S.A. maximice el valor de la inversión en HospiNet y reduzca su dependencia operativa del proveedor en el mediano y largo plazo.

<!-- Página 223 del PDF original -->

## 14 Innovaciones

Para añadir más valor a la solución presentada, fueron evaluadas varias innovaciones tecnológicas para optimizar la atención, seguridad del información de la clínica y mejorar la experiencia del usuario. Son estrategias que intentan seguir las nuevas tendencias a escala mundial en la digitalización del sector médico y adelantarse a las nuevas demandas de pacientes y profesionales.

Las soluciones propuestas incluyen tecnología Inteligencia Artificial, Internet de las Cosas, Blockchain y Edge Computing, las cuales fueron aplicadas para generar beneficios tangibles en el modelo de atención. A continuación se describirá cada innovación propuesta con su respectivo análisis de factibilidad, pruebas de concepto, gestión de riesgo e investigación aplicada con desarrollo experimental, garantizando que sean factibles y viables a futuro.

### 14.1 Diagnóstico asistido mediante Inteligencia Artificial

Planteamos la implementación de un sistema de inteligencia artificial como una herramienta de apoyo en el diagnostico clínico. Esto busca optimizar la calidad de la atención medica, aumentar la seguridad en las decisiones clínicas y mejorar la experiencia del paciente.

El sistema de IA estará diseñado para analizar historiales médicos, interpretar los exámenes y sugerir posibles diagnósticos en tiempo real. Mediante técnicas de procesamiento de lenguaje natural y aprendizaje automático, la herramienta podrá identificar patrones, generar alertas tempranas y apoyar a los médicos en la priorización de casos según su nivel de riesgo.

#### 14.1.1 Análisis de factibilidad:

La factibilidad técnica esta garantizada gracias al uso de modelos clínicos previamente validados y entrenados en bases de datos anonimizadas, compatibles con el sistema de Historia Clínica Electrónica mediante estándares internacionales como HL7 y FHIR.

<!-- Página 224 del PDF original -->

Económicamente resulta factible ya que al reducir los errores médicos y optimizar el tiempo de consultas permitirá atender un mayor numero de pacientes compensando los gastos realizados.

#### 14.1.2 Pruebas de concepto:

Se propone un piloto inicial de consultas generales con al menos 300 atenciones durante un periodo de tres meses. Los indicadores clave a medir serán: precisión de diagnósticos, reducción del tiempo de atención y la satisfacción del personal medico y los pacientes.

#### 14.1.3 Gestión de riesgos:

Entre los principales riesgos que se identificaron esta el sesgo de los datos el cual es mitigable con validación clínica continua y supervisión medica. Otro riesgo es la resistencia del personal de salud a confiar en la herramienta el cual se puede abordar mediante capacitaciones y protocolos claros que definan a la IA como un apoyo mas que un sustituto. Con respecto a la privacidad se garantiza la anonimización de los datos y el cumplimiento estricto de la ley 19.628 de protección de datos personales junto con las normas internacionales como ISO 27001.

#### 14.1.4 Investigación aplicada y desarrollo experimental:

El sistema de inteligencia artificial será validado de manera progresiva para garantizar su efectividad clínica y operativa. En una primera etapa se desarrollará un prototipo entrenado con datos anonimizados que permita comprobar la precisión diagnóstica en un entorno controlado. Posteriormente, se realizará un piloto en consultas generales para medir la reducción de errores y la optimización de tiempos de atención. Con los resultados obtenidos se ajustarán los algoritmos y se reforzarán los protocolos de seguridad de datos. Finalmente, se planificará una validación experimental a mayor escala, incorporando nuevas especialidades médicas y evaluando indicadores de desempeño clínico y satisfacción de usuarios, con el fin de asegurar la sostenibilidad y escalabilidad de la innovación.

#### 14.1.5 Beneficios esperados:

- Reducción en errores de diagnostico.

- Disminución en el tiempo de atención.

- Aumento de la detección temprana de enfermedades crónicas

- Fortalecimiento de la seguridad clínica y de la confianza de los pacientes

<!-- Página 225 del PDF original -->

### 14.2 Monitoreo remoto de pacientes con IoT (Internet de las Cosas)

Implementar un sistema como este busca optimizar la atención de pacientes con enfermedades crónicas y mejorar la eficiencia en el uso de los recursos clínicos. Este sistema permitirá un seguimiento continuo de los parámetros vitales de los pacientes tales como la presión arterial, la frecuencia cardíaca, la saturación de oxigeno y los niveles de glucosa, a través de dispositivos portátiles y sensores biomédicos conectados en tiempo real a la plataforma clínica

Esta innovación esta orientada a fortalecer un modelo de atención preventiva mediante la generación de alertas tempranas en caso de desviaciones criticas facilitando la intervención medica en los momentos oportunos. Con esto se busca reducir las hospitalizaciones evitables, aumentar la adherencia terapéutica y brindar a los pacientes una mayor autonomía en el manejo de su salud.

#### 14.2.1 Análisis de factibilidad:

En lo técnico esta innovación se respalda por la disponibilidad de dispositivos médicos IoT certificados en el mercado. Con respecto a el ámbito económico los costos de sensores y conectividad permiten una implementación progresiva y escalable. En cuanto a lo operacional se contempla un despliegue acompañado de capacitación a el personal junto con la creación de videos tutoriales para los pacientes asegurando una correcta adopción de la tecnología.

#### 14.2.2 Pruebas de concepto:

Se propone una prueba piloto con 70 pacientes crónicos o con enfermedades criticas durante un periodo de 4 meses. Para considerar la prueba como un éxito se proponen los siguientes indicadores: una precisión superior al 95% de precisión, una disponibilidad del sistema superior al 99%, reducir la cantidad de hospitalizaciones en un 20% y un tiempo de reacción a las alertas criticas de máximo 5 minutos.

#### 14.2.3 Gestión de riesgos:

los principales riesgos que identificamos son las fallas de conectividad que se pueden mitigar mediante redundancia en redes wifi y 5G, la vulnerabilidad en ciberseguridad la cual se puede mitigar con cifrado de extremo a extremo, una autenticación multifactor y la segmentación de redes, y las dificultades en la adopción del sistema por parte de los pacientes a los cuales se les brindaran videos tutoriales y soporte técnico para mitigar esto. Por ultimo contemplamos un sistema de filtrado de los datos para priorizar solo la información clinicmaente relevante y así evitar sobrecargar a los profesionales médicos.

<!-- Página 226 del PDF original -->

#### 14.2.4 Investigación aplicada y desarrollo experimental:

Para validar esta innovación se plantea el desarrollo de un prototipo de monitoreo remoto en un entorno clínico controlado. Se realizarán pruebas con un grupo reducido de pacientes para evaluar la precisión de los sensores y la estabilidad de la conectividad. Posteriormente, se documentarán los resultados y se ajustarán los parámetros de operación para mejorar la fiabilidad del sistema. En una segunda etapa, se desarrollará un piloto ampliado que permita medir el impacto en la reducción de hospitalizaciones y la adherencia terapéutica, con el fin de generar evidencia para su escalamiento.

#### 14.2.5 Beneficios esperados:

- Reducción en hospitalizaciones evitables.

- Incremento en la adherencia terapéutica.

- Disminución en consultas de urgencia.

- Mayor confianza y satisfacción de los pacientes gracias al seguimiento continuo de su estado de salud.

### 14.3 Gestión de datos clínicos con blockchain

Incorporar blockchain en la gestión de los datos clínicos tiene como objetivo asegurar la integridad, la confidencialidad y la trazabilidad de la información medica. Esta solución va a permitir almacenar los historiales médicos de los pacientes en un registro inmutable y distribuido, donde cada acceso o modificación echa quedara registrada de manera transparente y verificable.

El sistema esta diseñado para reforzar la seguridad de los datos sensibles, reducir riegos de fraude y accesos no autorizados a la información clínica de los pacientes, ademas de facilitar procesos de auditorias medicas y legales. Esto potenciara la confianza tanto de pacientes como de los profesionales, alineándose con las exigencias normativas y las tendencias internacionales en salud digital.

#### 14.3.1 Análisis de factibilidad:

En lo técnico la solución se puede implementar en una red privada basada en plataformas como Hyperledger o quorum que sea integrable con las bases de datos clínicos existentes. Operacionalmente se opta por un despliegue progresivo en las áreas criticas tales como las auditorias de acceso y los consentimientos informados. Por el lado económico la inversión inicial es mas alta que con bases de datos tradicionales pero otorga mas beneficios en la seguridad, la confianza y ademas otorga una reducción en los incidentes respaldando su implementación. Esta solución cumple con la ley 19.628 y con los estándares internacionales como ISO 27701.

<!-- Página 227 del PDF original -->

#### 14.3.2 Pruebas de concepto:

Se plantea una fase piloto en la cual mediante blockchain se registre y gestione el consentimiento informado digital de un grupo de 300 personas. Tomaremos como criterios de éxito el 100% de trazabilidad en los registros de acceso, interoperatividad con el sistema HIS y un tiempo de respuesta máximo de 5 segundos por consulta.

#### 14.3.3 Gestión de riesgos:

los principales riegos que identificamos serian la latencia en el acceso a la información la cual es mitigable al utilizar sidechains o canales privados para agilizar las consultas, la complejidad técnica para el personal la cual se puede resolver mediante capacitaciones y soporte especializado, el costo operacional el cual es controlable mediante un análisis costo total de propiedad (TCO) y la definición de casos de uso prioritarios para poder maximizar el retorno de la inversión.

#### 14.3.4 Investigación aplicada y desarrollo experimental:

La aplicación de blockchain se validará inicialmente mediante un prototipo orientado a la gestión del consentimiento informado y la trazabilidad de accesos a los historiales clínicos. En esta etapa se busca comprobar la interoperabilidad con los sistemas de la clínica y la facilidad de uso por parte de los profesionales. Posteriormente, se realizarán pruebas experimentales en escenarios reales para medir tiempos de respuesta, eficiencia en auditorías y niveles de aceptación. Los aprendizajes obtenidos permitirán refinar el modelo y preparar la solución para una implementación más amplia en la gestión integral de datos clínicos.

#### 14.3.5 Beneficios esperados:

- Garantía de integridad e inmutabilidad de los historiales médicos.

- Mayor confianza y transparencia en el uso de datos sensibles.

- Reducción de fraudes y accesos no autorizados.

- Facilidades en auditorías internas y externas, disminuyendo tiempos y costos de verificación.

### 14.4 Triaje Inteligente Automatizado

Se propone la implementación de un sistema de triaje inteligente que, atravez del uso de chatbots y algoritmos de procesamiento de lenguaje natural, realizara una preevaluación de síntomas de manera automatica. Esto con el objetivo de optimizar los flujos de atención, reducir los tiempos de espera de los pacientes y priorizar adecuadamente los casos de mayor gravedad clinica.

<!-- Página 228 del PDF original -->

#### 14.4.1 Análisis de factibilidad:

En la parte técnica se considera factible gracias a las tecnologías de IA que ya son utilizadas en servicios de salud digitales, las cuales son compatibles con estándares de interoperabilidad como HL7 y FHIR. Por la parte económica, la implementación es viable ya que al disminuir las consultas innecesarias y mejorar la eficiencia operativa del centro médico se lograra compensar el gasto de implementar el sistema.

#### 14.4.2 Pruebas de concepto:

Se plantea un piloto en el área de urgencias, donde al menos 500 pacientes utilicen el sistema durante un periodo de prueba de dos meses. Los indicadores qye se utilizaran para medir la eficiencia serán: tiempo promedio de triaje, nivel de satisfacción de pacientes y concordancia entre el triaje automatizado y el triaje clínico.

#### 14.4.3 Gestión de riesgos:

Uno de los riesgos que logramos identificar es la posibilidad de que se clasifique de forma incorrecta una consulta considerada rara, lo cual se mitigará mediante la supervisión de el personal clínico y la implementación de medidas de verificación para casos críticos. Otro riesgo es la posibilidad de que los usuarios no confien en el chatbot, lo que se abordará mediante una interfaz que sea amigable con los usuarios y a travez de campañas de comunicación. Finalmente, se garantizará que el sistema cumpla con la Ley 19.628 de protección de datos personales y las normas ISO 27001.

#### 14.4.4 Investigación aplicada y desarrollo experimental:

La innovación será validada inicialmente en un entorno controlado con escenarios simulados, para luego pasar a un piloto real en urgencias. Se evaluará la precisión diagnóstica, la optimización de flujos y la aceptación del personal clínico. Posteriormente, se escalará a otras unidades de atención, incorporando nuevas variables de riesgo y ajustando los algoritmos de priorización.

#### 14.4.5 Beneficios esperados:

- Reducción en los tiempos de espera en urgencias.

- Priorización más precisa de pacientes críticos.

- Disminución de consultas innecesarias.

- Optimización de la gestión de recursos médicos.

### 14.5 Realidad Aumentada para Procedimientos

Se propone el uso de dispositivos de realidad aumentada (RA) para asistir principalmente a enfermeras y técnicos al momento de realizar procedimientos clínicos, mostrando

<!-- Página 229 del PDF original -->

en tiempo real datos relevantes del paciente, guías paso a paso e indicaciones de seguridad directamente en los lentes inteligentes. Esto permitirá mejorar la precisión de la atención, reducir los errores y estandarizar los protocolos.

#### 14.5.1 Análisis de factibilidad:

Por la parte técnica consideramos que es factible gracias al hardware comercial disponible (lentes de RA certificados) y a las plataformas de integración con la historia clínica electrónica. Por el lado económico, el costo inicial es bastante alto pero se logra compensar con la reducción de los errores clínicos cometidos por el personal y el ahorro en los tiempos que conlleva la capacitación.

#### 14.5.2 Pruebas de concepto:

Se propone una prueba piloto en la sala de procedimientos menores (curaciones, toma de muestras y administración de fármacos intravenosos) con un minimo de 200 interacciones asistidas con RA. Los indicadores de exito seran los siguientes: la reducción de errores cometidos por el personal, una disminucion en el tiempo de procedimiento y un aumento en el nivel de confianza del personal y pacientes.

#### 14.5.3 Gestión de riesgos:

Como uno de los riesgos de implementar este sistema identificamos la fatiga visual que generara en el personal el cual se puede mitigar mediante protocolos de uso limitado y horarios de descanso rotativo para no desgastar la vista. Otro de los riesgos que consideramos es que el personal genere una dependencia excesiva de la tecnología el cual se puede abordar mediante capacitaciones continuas, evaluaciones calendarizadas para verificar que los procedimientos se aprendieron de forma correcta y evitar el abuso de la tecnología.Se garantizará la seguridad de los datos transmitidos mediante cifrado de extremo a extremo.

#### 14.5.4 Investigación aplicada y desarrollo experimental:

El desarrollo inicial incluirá la integración de modelos 3D interactivos y guías clínicas en RA. Se validará en entornos simulados antes de su aplicación en pacientes. Posteriormente, se ampliará su uso a procedimientos más complejos.

#### 14.5.5 Beneficios esperados:

- Disminución de errores en procedimientos clínicos.

- Estandarización y mejora de protocolos de atención.

- Reducción de tiempos de capacitación del personal.

- Mayor confianza y seguridad en la atención al paciente.

<!-- Página 230 del PDF original -->

### 14.6 Predicción de No-Show con Machine Learning

Se propone el uso de algoritmos de aprendizaje automático para predecir la probabilidad de inasistencia de los pacientes a sus citas médicas (no-show). La solución considera más de 50 variables, incluyendo historial de asistencia, distancia al centro de salud, condiciones socioeconómicas y recordatorios previos.

#### 14.6.1 Análisis de factibilidad:

Por el lado técnico consideramos que la implementación es viable ya que existen modelos de clasificación los cuales pueden ser entrenados con datos anonimizados. Por el lado económico se considera viable ya que lograra optimizar la agenda medica y así reducirá las perdidas asociadas a las horas que no son utilizadas.

#### 14.6.2 Pruebas de concepto:

Para las pruebas piloto proponemos entrenar el modelo predictivo con los datos históricos de agendamiento de los últimos 12 meses. Luego de entrenar el modelo se aplicara en el area de consultas generales durante un periodo de 6 meses para evaluar su desempeño y tasa de éxito. Los valores utilizados para evaluar su éxito serán: disminución en horas perdidas por inasistencia, la precisión del modelo predictivo y el aumento en la satisfacción de los pacientes con el sistema de recordatorios.

#### 14.6.3 Gestión de riesgos:

Como riesgos identificamos el sesgo de datos el cual podría discriminar a cierto grupo de pacientes con perfiles similares, esto se puede mitigar mediante la realización de auditorias de equidad en los modelos y la validación clínica continua. Otro riego que consideramos es el rechazo por parte de los pacientes el cual puede ser mitigado mediante politicas de transparencia y consentimiento informado de la utilización del sistema.

#### 14.6.4 Investigación aplicada y desarrollo experimental:

Se desarrollará un prototipo inicial con datos históricos anonimizados. Posteriormente, se integrará con el sistema de agendamiento, permitiendo enviar recordatorios personalizados o aplicar estrategias de sobreventa controlada. El sistema se evaluará con métricas de desempeño y ajustes progresivos de los modelos.

#### 14.6.5 Beneficios esperados:

- Reducción significativa en la tasa de inasistencia a citas.

- Mejor uso de la capacidad instalada de los centros médicos.

- Optimización de ingresos al reducir horas perdidas.

- Incremento en la satisfacción de pacientes al contar con recordatorios personalizados.

<!-- Página 231 del PDF original -->

## 15 Ventajas y Beneficios - Consolidación

Esta sección presenta la propuesta de valor, Ventajas y Beneficios de la solución, integrando los requerimientos funcionales y técnicos establecidos y el diseño de ingeniería desarrollado. Se muestra como es que, con métricas cuantitativas y argumentos de ingeniería, la solución propuesta maximiza el valor entregado al cliente manteniendo un equilibrio adecuado entre alcance, tiempo y costo, y respetando los principios de eficiencia, robustez, escalabilidad, mantenibilidad y elegancia técnica.

### 15.1 Análisis cuantitativo de los beneficios

El análisis cuantitativo se sustenta en los supuestos de carga y disponibilidad de 5.000 usuarios concurrentes, 1.000 transacciones por segundo sostenidas y alta disponibilidad con SLA ≥ 99,8%, en la arquitectura cloud-native definida, basada en microservicios, balanceo de carga dinámico, bases de datos distribuidas y orquestación sobre Kubernetes. Sobre esta base se proyectan mejoras en cuatro dimensiones clave: rendimiento, continuidad operacional (sobre todo importnte debido a los datos y vidas que se manejan gracias a la solución), mantenibilidad y costo total de propiedad.

Benchmarks de referencia para arquitecturas equivalentes basadas en frameworks modernos (por ejemplo, Spring Boot o Node.js con bases de datos distribuidas) muestran mejoras de hasta un 35% en rendimiento frente a aplicaciones monolíticas bajo cargas similares, con tiempos de respuesta inferiores a 300 ms para operaciones críticas. El diseño de HospiNet adopta este enfoque, proyectando tiempos promedio de respuesta por debajo de los 300 ms incluso en escenarios de carga alta, cumpliendo y superando los requerimientos de throughput.

<!-- Página 232 del PDF original -->

Table 15.1: Indicadores cuantitativos de beneficios proyectados

| Indicador | Situación de referencia | Situación proyectada con HospiNet |
| --- | --- | --- |
| Disponibilidad anual (SLA) | ≈ 97,0% (plataforma monolítica on-premise, sin prácticas SRE formales). | 99,95% o 99,97% objetivo dependiendo del caso, con prácticas SRE, monitoreo 24x7, redundancia N+1 y tolerancia a fallos. |
| MTTR (Mean Time To Repair) | Entre 3 y 4 horas por incidente crítico, con alta dependencia de intervención manual. | ≤ 0,8 horas promedio gracias a automatización, observabilidad y playbooks de recuperación documentados. |
| Tiempos de respuesta en operaciones críticas | 500 a 700 ms promedio bajo carga, con picos superiores a 1 segundo. | &lt; 300 ms promedio en operaciones críticas en horas punta, con protección frente a picos de demanda. |
| Esfuerzo de mantenimiento evolutivo | Mantenimiento reactivo, acoplamiento alto y cambios costosos en código y base de datos. | Reducción proyectada del 25 a 30% en esfuerzo de mantenimiento futuro gracias a Clean Architecture, APIs bien definidas y CI/CD. |
| Costo operacional total (vista relativa) | 100% (base de comparación). | Reducción estimada del 20 a 25% en costos operativos recurrentes a 5 años, por consolidación tecnológica y automatización. |

Desde la perspectiva de retorno de la inversión (ROI), la métrica se expresa aquí en términos de relación entre ahorros acumulados y esfuerzo inicial de implementación. Bajo los supuestos de reducción de TCO y mejora de productividad, el punto de equilibrio se estima entre los 24 y 30 meses posteriores a la puesta en producción, con un retorno acumulado que supera el 100% del esfuerzo de inversión inicial en un horizonte de 5 años. A partir de ese momento, la solución comienza a generar un beneficio neto sostenido para la organización

### 15.2 Comparación con soluciones tradicionales

Como referencia se considera una solución tradicional basada en un sistema monolítico on-premise, con módulos clínicos y administrativos parcialmente integrados, crecimiento Horizontal y Vertical (scale-up) y despliegues manuales. En contraste, la solución propuesta HospiNet adopta una arquitectura cloud-native de microservicios orquestados, APIs abiertas e integraciones estandarizadas. La comparación se centra en rendimiento, escalabilidad, seguridad, mantenibilidad y tiempo de despliegue.

<!-- Página 233 del PDF original -->

Table 15.2: Comparación entre solución tradicional y solución propuesta HospiNet

| Criterio | Solución tradicional de referencia | Solución propuesta HospiNet |
| --- | --- | --- |
| Arquitectura | Aplicación monolítica, acoplamiento alto, dependencia de un único stack y servidor de aplicaciones. | Microservicios desacoplados, enfoque API-first y event-driven, con balanceadores de carga, colas asíncronas y bases de datos distribuidas. |
| Rendimiento y throughput | Capacidad limitada para 1.000 TPS sostenidas; bajo estrés aparecen cuellos de botella en base de datos y en la capa de aplicación. | Diseñada para soportar y escalar más allá de 1.000 TPS, con cache en memoria, particionamiento de datos y escalamiento horizontal automático por servicio. |
| Escalabilidad | Escalamiento vertical, ventanas de mantenimiento largas y alto riesgo de downtime en cambios mayores. | Escalamiento horizontal por microservicio, despliegues canary/rolling y capacidad de crecer por módulos según demanda, sin afectar al resto de la plataforma. |
| Seguridad | Seguridad perimetral tradicional, controles manuales y trazabilidad fragmentada entre sistemas y registros. | Modelo Zero Trust, integración con SD -WAN/SASE, segmentación por microservicio, autenticación fuerte y logging centralizado que facilita auditoría y cumplimiento normativo. |
| Mantenibilidad | Cambios costosos, alto impacto cruzado entre módulos, baja automatización de pruebas y alta dependencia de conocimiento tácito de ciertos desarrolladores clave. | Reducción proyectada del 25-30% en esfuerzo de mantenimiento con CI/CD, suites de pruebas automatizadas, contratos de API bien definidos y deuda técnica controlada desde el diseño (Clean Architecture, DDD, etc.). |
| Tiempo de despliegue | Ventanas de horas (o días) para releases, con alto riesgo de rollback manual y necesidad de coordinar múltiples equipos para cada puesta en producción. | Despliegues frecuentes en ventanas acotadas de minutos, mediante pipelines automatizados, estrategias canary/blue-green y rollback controlado, minimizando indisponibilidad y riesgo operacional en cada liberación. |

La ventaja técnica de la propuesta se fundamenta en tres pilares: (1) una arquitectura pensada para alta concurrencia y resiliencia, que adopta buenas prácticas SRE, DevSecOps y objetivos de SLA del orden de 99,95% como mínimo, (2) un diseño modular que reduce la deuda técnica futura y habilita la incorporación de nuevos servicios (por ejemplo, nuevos flujos de telemedicina o integraciones con dispositivos IoT) sin impactar la operación si no que complementándola y volviéndola mas robusta, un sistema de monitoreo de servidores y estado actual de los sistemas y (3) una plataforma de datos unificada que alimenta dashboards clínicos, operacionales y financieros en

<!-- Página 234 del PDF original -->

tiempo casi real, entre otros puntos relevantes para el caso.

### 15.3 Alineación con los objetivos estratégicos del cliente

La Empresa de Consultas Médicas SA. busca una plataforma que unifique la operación clínica y administrativa, habilite capacidades de call center, telemedicina, seguimiento de pacientes, recursos humanos digital, reportería avanzada, entre otros. HospiNet se diseñó precisamente como una solución integral que conecta estos dominios sobre una única arquitectura, maximizando el valor para la organización y sus pacientes.

Table 15.3: Alineación de HospiNet con los objetivos estratégicos del cliente

| Objetivo estratégico del cliente | Contribución concreta de HospiNet |
| --- | --- |
| Unificar la operación clínica y administrativa en una sola plataforma. | Integración nativa de agenda, HCE, facturación, cobranza, convenios, abastecimiento y RRHH, evitando sistemas aislados, doble digitación y pérdida de información entre áreas. |
| Mejorar la experiencia y el acceso de pacientes. | Call center y CRM omnicanal (teléfono, chat, correo, WhatsApp), telemedicina HD integrada, recordatorios automáticos de controles y medicación, y flujos específicos para pacientes crónicos y GES. |
| Fortalecer el cumplimiento normativo y la seguridad de la información. | Trazabilidad completa de operaciones, logs centralizados, control de accesos por rol, cifrado en tránsito y en reposo, y soporte a reportes regulatorios exigidos por autoridades de salud y organismos fiscalizadores. |
| Potenciar la gestión basada en datos y la toma de decisiones. | Dashboards en tiempo casi real con KPIs operacionales, indicadores clínicos, métricas financieras y análisis predictivo, permitiendo identificar cuellos de botella, tendencias de demanda y oportunidades de mejora continua. |
| Asegurar escalabilidad y sostenibilidad tecnológica a 5-10 años. | Arquitectura cloud-native, microservicios escalables, uso de estándares abiertos (REST, FHIR, HL7 donde aplique) y desacoplamiento entre front-end, lógica de negocio e integración, reduciendo la dependencia de proveedores específicos y facilitando la evolución futura. |

La solución contribuye a la transformación digital (uno de los puntos mas relevantes a llevar a cabo debido al dolor mencionado en la sección de alcance) del prestador al promover procesos paperless, firmas electrónicas, automatización de flujos de autorización y una interacción más fluida entre los distintos actores (médicos, administrativos, pacientes y aseguradoras). Desde la perspectiva de valor público, mejora la trazabilidad y velocidad de la atención y facilita la generación de reportes hacia organismos reguladores, aportando transparencia de procesos y calidad de servicio.

<!-- Página 235 del PDF original -->

### 15.4 Resumen ejecutivo de beneficios

Para públicos no técnicos, los beneficios de la solución HospiNet pueden resumirse en tres ideas centrales: (1) todo el funcionamiento de la clínica se ordena y coordina en una sola plataforma; (2) la atención a pacientes se vuelve más rápida, más trazable y más cercana; y (3) la dirección cuenta con información confiable y oportuna para tomar decisiones.

Indicadores clave de mejora que se propone destacar incluyen: una disponibilidad objetivo en torno al 99,95%, reducciones superiores al 70-80% en el MTTR frente al estado actual, mejoras del orden del 30-35% en el rendimiento bajo carga y una reducción del 20-25% en los costos operativos totales a 5 años, sin sacrificar calidad ni disponibilidad del servicio.

### 15.5 Optimización de la triple restricción

La propuesta de HospiNet por su naturaleza misma (y para efectos de esta licitación), optimiza el triángulo de triple restricción (Tiempo/Costo/Alcance). En términos de alcance, se cubren de manera integrada los módulos clínicos, administrativos, financieros, cadena de suministro, call center, telemedicina, RRHH digital y analytics, alineados con los requerimientos funcionales y no funcionales y la EDT definida en la sección 16.4

En términos de tiempo, la planificación por fases -inicio, diseño, desarrollo, obras civiles y montaje, intervención, capacitaciones, puesta en producción y cierre- permite controlar hitos clave y gestionar riesgos tempranamente. El uso de infraestructura como código, pipelines de CI/CD, entornos de prueba replicables y despliegues canary/rolling reduce los plazos de construcción y despliegue efectivos, al mismo tiempo que disminuye la probabilidad de retrabajo y fallas en producción.

Desde la perspectiva de costo, más que reducir la inversión inicial, la propuesta busca maximizar el valor generado por unidad de esfuerzo. Cada decisión técnica (por ejemplo, adoptar estándares abiertos, diseñar microservicios independientes o automatizar pruebas) disminuye el costo de los cambios futuros y la dependencia de proveedores específicos. Esto se traduce en un TCO más bajo a 5 años, sin comprometer ni el alcance ni la calidad de la solución.

En resumen, la solución propuesta no persigue únicamente cumplir con la lista de requisitos, sino entregar una plataforma clínico-administrativa sólida, evolucionable y económicamente sostenible, que respeta las restricciones de calendario y recursos del proyecto, mientras habilita a la organización para crecer y adaptarse en el mediano y largo plazo.

<!-- Página 236 del PDF original -->

<!-- Página sin texto extraíble ni figuras detectadas. -->

<!-- Página 237 del PDF original -->

## 16 ANEXOS

### 16.1 Requerimientos Funcionales del Proyecto

Aquí se describen todos los requerimientos identificados para el proyecto, los cuales serán presentados por módulos.

#### 16.1.1 Módulo de Historia Clínica Electrónica

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFHC-01 | El sistema debe implementar un mecanismo de autenticación biométrica para el acceso de usuarios al sistema, asegurando que solo personal autorizado pueda ingresar a la plataforma clínica. Específicamente por huella y reconocimiento facial. | Alta | Medio |
| RFHC-02 | El sistema deberá almacenar y gestionar la información de la Historia Clínica Electrónica de acuerdo con estándares internacionales HL7/FHIR, asegurando interoperabilidad con otros sistemas de salud. | Alta | Medio |
| RFHC-03 | El sistema deberá proveer formularios estructurados para el registro de la anamnesis (antecedentes y motivo de consulta), de manera uniforme y completa, facilitando la entrada de datos clínicos de forma organizada. | Alta | Bajo |
| RFHC-04 | El sistema deberá permitir registrar los signos vitales (como presión arterial, frecuencia cardiaca, temperatura, saturación de oxígeno, etc.) de cada paciente durante la consulta, almacenándolos de forma cronológica para su seguimiento en la HCE. | Alta | Bajo |

Table 16.1: Requerimientos del Módulo de Historia Clínica Electrónica

<!-- Página 238 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFHC-05 | El sistema deberá proporcionar la funcionalidad de generar recetas médicas electrónicas, permitiendo al médico prescribir medicamentos y tratamientos digitalmente, con opción de firma electrónica y envío directo a farmacias o al paciente. | Alta | Medio |
| RFHC-06 | El sistema debe registrar y mantener alergias y contraindicaciones a nivel de paciente (sustancia, reacción, severidad, fuente y fecha), disparando alertas en caso de agregar una prescripción, administración de medicamentos o admisión a procedimientos. | Media | Alto |
| RFHC-07 | El sistema deberá permitir anexar a la historia clínica documentos e imágenes (resultados de exámenes, radiografías, consentimientos escaneados), manteniéndolos asociados al paciente y disponibles para consulta desde la HCE. | Alta | Medio |
| RFHC-08 | El sistema debe incorporar firma electrónica avanzada para documentos clínicos/administrativos (consentimientos, recetas, epicrisis, licencias), con sellado de tiempo, validación de identidad del firmante, hash y resguardo. | Alta | Medio |
| RFHC-09 | El sistema deberá mantener un registro de auditoría detallado de todos los accesos y acciones realizadas sobre la historia clínica (consultas, modificaciones, creación de registros), incluyendo usuario, fecha, hora, identificación del paciente y dirección ip de la conexión, para asegurar la trazabilidad de la información clínica. | Alta | Medio |
| RFHC-10 | El sistema debe cifrar datos sensibles en reposo ( campos diagnósticos , notas clínicas, RUT, teléfonos, correos, domicilio resultados sensibles y discos/volúmenes) y en tránsito (TLS 1.3). Para ello, se deben considerar respaldos cifrados, una rotación de llaves cada 90 días en KMS y aplicar pruebas de restauración trimestrales. | Alta | Alto |
| RFHC-11 | El sistema debe incorporar herramientas de apoyo de diagnóstico basadas en inteligencia artificial, para asistir a los médicos en la identificación temprana de patologías, reducir tiempos de análisis y mejorar la precisión en la toma de decisiones clínicas. | Media | Medio |

Table 16.2: Requerimientos del Módulo de Historia Clínica Electrónica

<!-- Página 239 del PDF original -->

#### 16.1.2 Módulo de Gestión de Pacientes

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFGP-01 | El sistema debe permitir la captura estructurada de todos los datos relevantes del paciente (identificación, contacto, antecedentes médicos e información de previsión), asegurando integridad y consistencia en el registro inicial. | Alta | Medio |
| RFGP-02 | La plataforma debe integrarse con el Registro Civil para validar en tiempo real la identidad del paciente mediante RUN/RUT y datos asociados, reduciendo riesgos de duplicidad o fraude. | Alta | Alto |
| RFGP-03 | El sistema debe conectarse con las instituciones de previsión para comprobar automáticamente la vigencia y tipo de cobertura del paciente en el momento de la admisión. | Alta | Alto |
| RFGP-04 | El sistema debe generar de manera automática y secuencial un número único de ficha clínica por paciente, garantizando trazabilidad, unicidad y continuidad en la atención. | Media | Bajo |
| RFGP-05 | El sistema debe permitir la gestión de consentimientos informados en formato digital, con firma electrónica simple o avanzada según corresponda, almacenados de forma segura en el expediente del paciente. | Alta | Media |

Table 16.3: Requerimientos del Módulo de Gestión de Pacientes

<!-- Página 240 del PDF original -->

#### 16.1.3 Módulo de Agendamiento Multicanal

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFAM-01 | El sistema será un portal web responsive que permite a los pacientes agendar consultas en línea. Incluye páginas de Inicio, Búsqueda, Resultados con filtros, Detalle de profesional/centro, Agendamiento paso a paso, Carro de prepago, Perfil, Mis citas, Pagos y Soporte. El login sera por correo + contraseña y social login opcional. | Alta | Medio |
| RFAM-02 | El sistema deberá permitir a los usuarios seleccionar una hora disponible para confirmarla y agendarla. | Alta | Medio |
| RFAM-03 | El sistema deberá enviar un correo de confirmación al paciente con fecha, hora y lugar de la atención. | Alta | Medio |
| RFAM-04 | El sistema deberá permitir que los funcionarios del recinto médico realicen agendas de citas para los pacientes. | Alta | Bajo |
| RFAM-05 | El sistema deberá permitir que los Médicos del recinto realicen agendas de citas para los pacientes hacia otros especialistas directamente y sin pasar por otro proceso de atención. | Alta | Medio |
| RFAM-06 | Los sistemas de búsqueda y agendamiento de horas (Portal web, CRM, sistema presencial, app móvil y whatsapp) deberá ofrecer un motor de búsqueda inteligente de cupos disponibles considerando múltiples criterios (especialidad requerida, ubicación, preferencias del paciente, urgencia) de modo que al agendar se sugieran automáticamente las mejores opciones de fecha y hora para la cita. | Alta | Medio |
| RFAM-07 | El sistema deberá confirmar automáticamente las reservas de hora con los pacientes, enviando confirmaciones inmediatas a través de los canales definidos (correo electrónico, SMS o WhatsApp) una vez agendada la cita y actualizando el estado de la cita en el calendario como ’Confirmada’. | Alta | Medio |

Table 16.4: Requerimientos del Módulo de Agendamiento Multicanal

<!-- Página 241 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFAM-08 | El sistema deberá facilitar a los funcionarios del establecimiento médico el reagendamiento de citas, permitiendo a pacientes y personal modificar la fecha y hora de una reserva existente de forma simple, reubicando automáticamente la cita y liberando el espacio previo sin generar inconsistencias. | Alta | Bajo |
| RFAM-09 | El sistema deberá gestionar listas de espera de manera inteligente: cuando no haya cupos inmediatos, permitir inscribir pacientes en espera y, si se libera una hora (por cancelación de otro paciente), notificar y agendar automáticamente al primer paciente en espera según criterios de prioridad predefinidos. | Alta | Medio |
| RFAM-10 | El sistema deberá permitir (En caso de que el juicio profesional lo respalde) forzar un cambio de cita ya agendada, reemplazando la hora ya tomada por una nueva con mayor grado de urgencia. | Alta | Medio |
| RFAM-11 | El sistema deberá proveer una aplicación móvil nativa (Android/iOS) para agendamiento con las mismas funcionalidades del portal web. | Alta | Medio |
| RFAM-12 | El sistema deberá habilitar flujo guiado de agendamiento vía WhatsApp con mensajes interactivos (notificaciones) que permitan ver próximas 3 fechas disponibles. | Media | Medio |
| RFAM-13 | El sistema deberá permitir agendamiento en recepción con búsqueda por RUT/nombre, ver disponibilidad y registrar cita. | Alta | Bajo |
| RFAM-14 | El sistema deberá permitir que médicos generen referencias directas a especialistas o exámenes desde la HCE, asegurando continuidad de atención. | Alta | Medio |
| RFAM-15 | El sistema deberá enviar recordatorios automáticos multicanal (correo electrónico, SMS, WhatsApp) de las citas agendadas. | Alta | Medio |
| RFAM-16 | El sistema deberá gestionar el reagendamiento automático de citas, notificando al paciente y liberando la hora previamente reservada. | Alta | Medio |
| RFAM-17 | El sistema deberá notificar por correo tanto al paciente como al médico en caso de reagendamiento automático, indicando fecha, hora y lugar de la nueva atención. | Alta | Medio |
| RFAM-18 | El sistema deberá soportar gestión de urgencias, priorizando automáticamente pacientes críticos y reasignando cupos con alertas al personal de salud. | Alta | Medio |

Table 16.5: Requerimientos del Módulo de Agendamiento Multicanal

<!-- Página 242 del PDF original -->

#### 16.1.4 Módulo de CRM con call center

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFCMR-01 | El sistema deberá incluir una solución de Call Center integrada con un CRM. | Alta | Medio |
| RFCMR-02 | El sistema deberá permitir a los operadores agendar citas para el paciente. | Alto | Medio |
| RFCMR-03 | El sistema deberá permitir a los operadores registrar llamadas de pacientes en un calendario. | Alta | Medio |
| RFCMR-04 | El sistema deberá permitir a los operadores ver historial de interacciones para el paciente. | Alta | Medio |
| RFCMR-05 | El sistema deberá permitir a los operadores revisar todo el HCI digitalizado del usuario cuando el trabajador de call center necesite. | Alta | Medio |
| RFCRM-06 | El sistema deberá contar con un IVR (Respuesta de Voz Interactiva) inteligente en el call center, que guíe a los pacientes a través de menús de voz para enrutarlos adecuadamente | Media | Medio |
| RFCRM-07 | El sistema deberá implementar distribución automática de llamadas (ACD) en el call center para asignar las llamadas entrantes al operador disponible más adecuado, en base a reglas definidas, equilibrando la carga de trabajo y minimizando tiempos de espera. | Alta | Bajo |
| RFCRM-08 | El sistema deberá integrar un módulo de chat en vivo en la web de la clínica, permitiendo que los pacientes interactúen en tiempo real con personal de atención al cliente para resolver dudas o coordinar servicios. Las conversaciones de chat deben poder ser asignadas a diferentes agentes, con registro de historial y posibilidad de transferencia a otro agente o especialista si es necesario. | Media | Bajo |
| RFCRM-09 | El sistema deberá contar con un chatbot impulsado por IA integrado en el sitio web o WhatsApp, capaz de atender consultas frecuentes de los pacientes de manera autónoma y de realizar algunas acciones como agendar o cancelar citas simples. Debe poder derivar al chat en vivo con un humano cuando la consulta supera sus capacidades. | Media | Medio |

<!-- Página 243 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFCRM-10 | El sistema deberá integrar la gestión de correos electrónicos dentro del CRM, permitiendo que los correos enviados por pacientes queden registrados como casos o tickets en la plataforma, con la posibilidad de asignarlos a agentes para respuesta y seguimiento, de forma similar a una consulta vía teléfono o chat. | Media | Bajo |
| RFCRM-11 | El sistema deberá integrar oficialmente la WhatsApp Business API para el manejo de mensajes de WhatsApp dentro del CRM: de modo que los mensajes de texto enviados por pacientes al número de la clínica sean recibidos en la plataforma, y los agentes puedan responder desde el CRM sin necesidad de usar un teléfono móvil, manteniendo un historial centralizado. | Media | Medio |
| RFCRM-12 | El sistema deberá incluir una funcionalidad para gestionar campañas de comunicación proactiva con pacientes, permitiendo segmentar listas y enviar mensajes masivos personalizados vía email, SMS o WhatsApp. Además, se debe poder hacer seguimiento de la efectividad de la campaña. | Media | Bajo |
| RFCRM-13 | El sistema deberá proveer una gestión de casos o tickets para el seguimiento de solicitudes o problemas planteados por pacientes que no se resuelven inmediatamente, asignando cada caso a un responsable, con estado y registro de todas las interacciones hasta su cierre. | Alta | Bajo |
| RFCRM-14 | El sistema deberá permitir a los operadores revisar todo el HCI digitalizado del usuario cuando el trabajador del call center lo necesite. | Alta | Medio |

Table 16.6: Requerimientos del Módulo de CRM con call center

<!-- Página 244 del PDF original -->

#### 16.1.5 Módulo de Facturación y Cobranza

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFFC-01 | El sistema deberá permitir registrar tanto bonos físicos (escaneados) presentados por los pacientes como bonos electrónicos emitidos externamente (recibidos por correo), asociándolos a la transacción correspondiente, registrando tipo de bono, número, monto y cobertura aplicada. | Alta | Bajo |
| RFFC-02 | El sistema deberá permitir facturar directamente a empresas convenidas (ejemplo: empleadores o aseguradoras complementarias) utilizando cartas de resguardo, generando la factura a nombre de la empresa y adjuntando la carta digital como respaldo. | Media | Bajo |
| RFFC-03 | El sistema deberá emitir automáticamente boletas o facturas electrónicas al momento del pago, cumpliendo la normativa del Servicio de Impuestos Internos (SII) de Chile para prestaciones de salud, integrándose con el sistema de facturación electrónica (propio o de un proveedor) para reportar en tiempo real al SII. | Alta | Alto |
| RFFC-04 | El sistema deberá soportar múltiples medios de pago para el cobro de prestaciones (efectivo, tarjetas, transferencias, apps móviles), registrando el método utilizado y permitiendo pagos mixtos en una misma transacción. | Alta | Bajo |
| RFFC-05 | El sistema deberá permitir emitir facturación y cobros directamente a las instituciones previsionales (Isapres) y al Fondo Nacional de Salud (Fonasa) para prestaciones cubiertas, generando archivos o interfaces electrónicas para presentar cuentas médicas y hacer seguimiento a su pago. | Alta | Alto |
| RFFC-06 | El sistema deberá calcular automáticamente el copago del paciente por cada prestación, en base a la cobertura de su seguro (Fonasa/Isapre) y convenios aplicables, mostrando el monto a pagar y registrando su pago. Deberá manejar casos de copago $0 y registrar saldos pendientes. | Alta | Medio |
| RFFC-07 | El sistema deberá administrar convenios especiales con empresas o grupos (ejemplo: descuentos institucionales o paquetes de servicios), aplicando automáticamente las condiciones al momento de la facturación y llevando control de la utilización de los convenios. | Media | Bajo |

Table 16.7: Requerimientos funcionales de Facturación y Cobranza

<!-- Página 245 del PDF original -->

#### 16.1.6 Módulo de Seguimiento de Pacientes

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFSP-01 | El sistema deberá permitir definir y automatizar flujos de trabajo específicos para pacientes con patologías crónicas o GES (ejemplo: diabetes, hipertensión), planificando actividades de cuidado según protocolos (controles periódicos, exámenes de seguimiento, educación al paciente), con recordatorios y tareas asignadas automáticamente al equipo de salud. | Alta | Medio |
| RFSP-02 | El sistema deberá emitir alertas automáticas cuando un paciente crónico o GES no asista a un control programado o esté próximo a exceder el intervalo recomendado sin control. Las alertas deberán ser visibles para el equipo clínico responsable y/o generar notificaciones al paciente para re-agendar. | Alta | Bajo |
| RFSP-03 | El sistema deberá permitir programar recordatorios automáticos de medicación para pacientes, especialmente crónicos. El paciente o clínico podrá ingresar el esquema de medicamentos y el sistema enviará notificaciones (app móvil, SMS, correo) en los horarios definidos, registrando si el paciente confirma la toma o marca dosis omitidas. | Alta | Medio |
| RFSP-04 | El sistema deberá ofrecer una aplicación o módulo para que pacientes crónicos puedan automonitorear su salud (ejemplo: glucometrías, presión arterial, síntomas diarios). Los datos ingresados deberán integrarse con la HCE y estar disponibles para el médico tratante, generando alertas si se detectan valores fuera de rango. | Media | Medio |
| RFSP-05 | El sistema deberá generar reportes periódicos con los indicadores requeridos por la Superintendencia de Salud u otros organismos regulatorios para programas GES y crónicos, incluyendo número de pacientes en programa, cumplimiento de controles e indicadores de resultados clínicos, en el formato exigido por la autoridad. | Alta | Medio |

Table 16.8: Requerimientos funcionales de Seguimiento de Pacientes

<!-- Página 246 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFSP-06 | El sistema deberá facilitar la coordinación con la red de prestadores GES, permitiendo derivar pacientes a centros de referencia o especialistas externos, compartiendo información de forma segura y registrando la derivación. Asimismo, deberá permitir recibir actualizaciones o resultados externos para integrarlos en la HCE local. | Alta | Medio |
| RFSP-07 | El sistema deberá permitir el seguimiento postconsulta de pacientes, integrando encuestas de evolución, controles programados y alertas clínicas de continuidad. | Media | Medio |
| RFSP-08 | El sistema deberá permitir al personal clínico activar un “Caso GES” directamente desde la HCE, iniciando un cronómetro legal y generando un registro único y trazable. | Alta | Alto |
| RFSP-09 | El sistema deberá monitorear activamente los plazos de cada etapa del caso GES (diagnóstico, tratamiento, seguimiento) y generar alertas proactivas y escalables al personal responsable cuando exista riesgo de incumplimiento. | Alta | Alto |
| RFSP-10 | El sistema deberá permitir la configuración de flujogramas de atención para cada patología GES, guiando al personal sobre las prestaciones y pasos a seguir en cada etapa del proceso. | Alta | Alto |
| RFSP-11 | El sistema deberá generar automáticamente informes y estadísticas de cumplimiento exigidos por la Superintendencia de Salud, asegurando trazabilidad y oportunidad en la entrega. | Alta | Alto |
| RFSP-12 | El sistema deberá recibir datos de dispositivos médicos IoT (ejemplo: glucómetros, tensiómetros, oxímetros) de forma segura, asociándolos automáticamente a la HCE del paciente correcto. | Alta | Medio |
| RFSP-13 | El sistema deberá ofrecer al personal clínico una consola centralizada para visualizar datos históricos y en tiempo real de todos sus pacientes bajo monitoreo, con gráficos de tendencias y valores clave. | Alta | Medio |
| RFSP-14 | El sistema deberá permitir al médico definir umbrales de alerta personalizados por paciente (ejemplo: presión sistólica &gt; 140 mmHg). Si un dato recibido supera el umbral, se deberá generar una alerta automática al equipo de enfermería responsable. | Alta | Alto |
| RFSP-15 | El sistema deberá permitir al personal clínico enviar mensajes o iniciar una videoconsulta directamente desde el dashboard de monitoreo cuando se detecte una anomalía en los datos del paciente. | Alta | Alto |

<!-- Página 247 del PDF original -->

#### 16.1.7 Módulo de Telemedicina

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFTM-01 | El sistema deberá ofrecer la capacidad de realizar videoconsultas en alta definición de forma integrada, sin depender de aplicaciones externas. Médicos y pacientes deberán poder conectarse a una sala virtual segura directamente desde la plataforma (web o app), con video y audio de alta calidad, permitiendo una consulta remota casi equivalente a la presencial. | Alta | Medio |
| RFTM-02 | El sistema deberá permitir tanto al médico como al paciente compartir pantalla o documentos en tiempo real durante la videoconsulta. Por ejemplo, el médico podrá mostrar resultados de exámenes o imágenes diagnósticas, y el paciente podrá compartir documentos relevantes, con controles de seguridad que eviten la exposición de información no deseada. | Media | Bajo |
| RFTM-03 | El sistema deberá habilitar a los médicos para generar recetas electrónicas durante la videoconsulta, integradas con la HCE. Al finalizar la consulta, el médico deberá poder enviar al paciente su receta digital firmada electrónicamente (por correo o descargable en el portal), cumpliendo con los requisitos legales, sin necesidad de que el paciente acuda presencialmente. | Alta | Medio |
| RFTM-04 | El sistema deberá soportar el cobro de la consulta telemédica de forma online, permitiendo al paciente pagar a través de medios electrónicos (tarjeta de crédito/débito, transferencias, plataformas de pago) antes, durante o al finalizar la videoconsulta. El sistema deberá integrarse con el módulo de facturación para emitir automáticamente la boleta electrónica una vez recibido el pago. | Alta | Medio |
| RFTM-05 | El sistema deberá ofrecer la opción de grabar la videoconsulta (audio y video) siempre que se cuente con el consentimiento explícito del paciente. La grabación deberá almacenarse de forma segura, asociada a la HCE del paciente, para fines clínicos (revisión por especialistas, auditoría médica). Deberán existir controles para iniciar/pausar la grabación y avisos visuales de que está en curso, cumpliendo normativas de privacidad. | Media | Alto |

Table 16.10: Requerimientos funcionales de Telemedicina

<!-- Página 248 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFTM-06 | El sistema deberá integrarse plenamente con la Historia Clínica Electrónica (HCE), registrando automáticamente en ella las notas de atención, diagnósticos, indicaciones y recetas emitidas durante la videoconsulta. Durante la sesión, el médico deberá tener acceso al historial completo del paciente y podrá actualizar su información en tiempo real. | Alta | Bajo |
| RFTM-07 | El sistema deberá soportar un flujo de atención 100% digital, desde el agendamiento y pago online, pasando por la videoconsulta, hasta la emisión de recetas y licencias médicas electrónicas, sin necesidad de procesos manuales externos. | Alta | Alto |
| RFTM-08 | El sistema deberá permitir la creación de programas de salud estructurados (por ejemplo, programas de control de hipertensión), combinando consultas, monitoreo remoto y entrega de contenido educativo a los pacientes a través de la aplicación móvil. | Media | Medio |
| RFTM-09 | El sistema deberá contar con una arquitectura modular y escalable, permitiendo agregar nuevos servicios y funcionalidades en el futuro sin modificar los módulos core. Esto garantizará la evolución y crecimiento de la plataforma en el tiempo. | Alta | Alto |

Table 16.11: Requerimientos funcionales de Telemedicina

<!-- Página 249 del PDF original -->

<!-- Página sin texto extraíble ni figuras detectadas. -->

<!-- Página 250 del PDF original -->

#### 16.1.8 Módulo de Recursos Humanos Digital

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFRH-01 | El sistema deberá gestionar los contratos laborales de manera digital, permitiendo la generación, firma (simple o avanzada según corresponda) y almacenamiento de contratos de trabajo y anexos en la plataforma. Los empleados deberán poder firmar sus contratos electrónicamente y acceder a sus documentos en el portal del empleado, eliminando la necesidad de papel. | Alta | Medio |
| RFRH-02 | El sistema deberá integrarse con dispositivos biométricos (huella digital o reconocimiento facial) para registrar asistencia y horarios de entrada/salida del personal, almacenando los registros automáticamente en el módulo de RR.HH., lo que permitirá cálculo de horas trabajadas, retardos y ausencias de forma precisa. | Alta | Medio |
| RFRH-03 | El sistema deberá proporcionar herramientas para la creación y gestión optimizada de turnos y horarios del personal, proponiendo distribuciones equitativas y respetando restricciones legales y preferencias de los empleados. Los trabajadores deberán poder ver sus turnos en el portal y recibir notificaciones de cambios. | Alta | Medio |
| RFRH-04 | El sistema deberá incluir un módulo para evaluaciones de desempeño digital, con definición de metas y competencias, evaluaciones periódicas por jefaturas, autoevaluaciones y evaluaciones 360°. Los resultados deberán almacenarse históricamente y generar alertas de bajo rendimiento o falta de evaluación. | Alta | Medio |
| RFRH-05 | El sistema deberá ofrecer un módulo de capacitación online, permitiendo gestionar cursos internos con contenido multimedia y evaluaciones. Los empleados deberán acceder a los cursos desde el portal, completar módulos de e-learning y obtener certificados de aprobación. El sistema deberá mantener un historial de capacitaciones por empleado. | Alta | Medio |
| RFRH-06 | El sistema deberá proveer un portal de autoservicio donde el personal pueda acceder a información personal y servicios de RR.HH.: boletas de pago, actualización de datos, postulación a vacaciones o permisos, revisión de turnos, desempeño y capacitaciones pendientes. | Alta | Bajo |

Table 16.12: Requerimientos funcionales de Recursos Humanos Digital

<!-- Página 251 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFRH-07 | El sistema deberá soportar firma electrónica simple y avanzada para documentos internos y administrativos (licencias, permisos, políticas). La firma simple podrá realizarse con credenciales del usuario y la avanzada mediante certificado digital, formalizando digitalmente procesos que antes requerían firma manuscrita. | Alta | Medio |
| RFRH-08 | El sistema deberá calcular automáticamente las remuneraciones mensuales en base a asistencia, turnos, horas extras, bonos, descuentos legales y otros estipendios o deducciones. Deberá generar liquidaciones para cada trabajador, reportes consolidados para finanzas y permitir ajustes manuales con trazabilidad. | Alta | Alto |
| RFRH-09 | El sistema deberá gestionar el ciclo de vida del empleado completo, incluyendo reclutamiento, contratación, promociones, traslados y finiquitos, manteniendo trazabilidad en cada etapa. | Alta | Medio |
| RFRH-10 | El sistema deberá mantener un expediente digital único por empleado, incluyendo licencias profesionales, certificaciones y fechas de vencimiento, con alertas automáticas ante proximidad de expiración. | Alta | Medio |
| RFRH-11 | El sistema deberá calcular remuneraciones del personal de salud considerando las particularidades del sector (turnos, horas extras, bonos por desempeño y pagos variables por procedimiento). | Alta | Alto |
| RFRH-12 | El sistema deberá integrarse con los sistemas de control de asistencia y con el módulo de gestión de turnos para un registro preciso de las horas trabajadas. | Alta | Medio |
| RFRH-13 | El sistema deberá proveer un portal de autogestión del empleado para solicitar vacaciones, consultar liquidaciones de sueldo, actualizar datos personales y acceder a sus planes de capacitación. | Alta | Bajo |

Table 16.13: Requerimientos funcionales de Recursos Humanos Digital

<!-- Página 252 del PDF original -->

#### 16.1.9 Módulo de Reportería y Analytics

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFRA-01 | El sistema deberá ofrecer dashboards en tiempo real con los principales Indicadores Clave de Desempeño (KPIs) operativos de la clínica, como: volumen de consultas atendidas por día, tasa de ocupación de agenda, tiempos promedio de espera de pacientes, número de llamadas atendidas vs perdidas en call center, etc. Estos indicadores deben actualizarse dinámicamente a medida que se registran las operaciones y permitir filtrado por fecha, unidad o profesional. | Alta | Bajo |
| RFRA-02 | El sistema deberá presentar indicadores clínicos agregados para el seguimiento de la calidad de la atención: Porcentaje de pacientes diabéticos con control al día, tasa de reingresos hospitalarios (si aplica), promedio de HbA1c en población diabética, indicadores GES (cumplimiento de garantías en plazo), entre otros relevantes. | Alta | Medio |
| RFRA-03 | El sistema deberá brindar métricas financieras clave en tiempo real: ingresos diarios/mensuales por prestaciones, monto facturado vs recuperado (pagado), cuentas por cobrar pendientes, costos operativos si son ingresados. Debe permitir al área administrativa y gerencial monitorear la salud financiera de la operación, con gráficos de tendencia y comparativos vs periodos anteriores. | Alta | Bajo |
| RFRA-04 | El sistema debe calcular productividad por médico considerando citas atendidas, tiempo promedio por consulta, ingresos asociados, cancelaciones y no-show; descontar tiempos no clínicos (reuniones, urgencias, docencia) si están declarados en agenda; incluir proceso de apelación para correcciones y registro de auditoría. | Alta | Bajo |
| RFRA-05 | El sistema debe medir satisfacción con NPS, CSAT, CES, encuestas específicas por servicio post-atención por SMS/email/WhatsApp/app, muestras representativas, anonimato cuando aplique y panel de acciones; resultados disponibles en tableros gerenciales y exportables para análisis. | Alta | Medio |

Table 16.14: Requerimientos del Módulo de Reportería y Analytics

<!-- Página 253 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFRA-06 | El sistema debe incorporar modelos para demanda de consultas por servicio/semana, riesgo de no-show por paciente/cita, detección de pacientes que requieren intervención temprana, usando características como confirmaciones/recordatorios, historial de no-show, temporada/estacionalidad, hora y día, distancia estimada, tipo de prestación, clima (si está disponible); evaluar y monitorear con backtesting con datos 12-24 meses, AUC/ROC para clasificación, MAPE/RMSE para series de tiempo, monitoreo de deriva (drift), mostrando resultados en tableros con explicación de variables (SHAP). | Media | Alto |
| RFRA-07 | El sistema debe generar alertas automáticas cuando indicadores críticos como satisfacción &lt; 70, espera promedio &gt; 30 min, no-show diario &gt; 12%, desvío financiero &gt; 10% del promedio mensual superen umbrales, resaltar en rojo/amarillo, asignar responsables y enviar notificaciones por email/Teams/WhatsApp. | Alto | Bajo |

Table 16.15: Requerimientos del Módulo de Reportería y Analytics

<!-- Página 254 del PDF original -->

<!-- Página sin texto extraíble ni figuras detectadas. -->

<!-- Página 255 del PDF original -->

#### 16.1.10 Módulo de Operaciones

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFO-01 | El sistema deberá permitir a los usuarios conectarse remotamente a la red corporativa. | Alta | Medio |
| RFO-02 | La plataforma deberá integrar Telefonía IP para facilitar la comunicación interna entre áreas críticas (farmacia, hospitalización, urgencias), optimizando la coordinación y reduciendo tiempos de respuesta. | Media | Bajo |
| RFO-03 | El sistema deberá registrar la recepción de fármacos e insumos, validando automáticamente contra la orden de compra e incluyendo número de lote y fecha de vencimiento, asegurando calidad y seguridad en el stock disponible. | Alta | Alto |
| RFO-04 | El sistema deberá gestionar el inventario en tiempo real en múltiples ubicaciones (farmacia central, bodegas de piso, carros de procedimiento) y aplicar la regla de rotación FEFO (First Expired, First Out). | Alta | Medio |
| RFO-05 | El sistema deberá asegurar que toda orden de dispensación se genere exclusivamente a partir de una prescripción electrónica activa y firmada dentro de la HCE. | Alta | Alto |
| RFO-06 | El sistema deberá validar en tiempo real cada prescripción contra los datos de la HCE, generando alertas bloqueantes por alergias, interacciones medicamentosas o dosis fuera de rangos seguros. | Alta | Alto |
| RFO-07 | El sistema deberá implementar un proceso de administración que requiera el escaneo de tres puntos (personal, paciente, medicamento), impidiendo la continuación si no hay correspondencia 100% con la prescripción activa en la HCE. | Alta | Alto |
| RFO-08 | El sistema deberá proveer trazabilidad completa y auditable de cada unidad de fármaco, desde su recepción hasta su administración o descarte. | Media | Medio |
| RFO-09 | El sistema deberá gestionar la cadena de custodia de muestras biológicas, registrando fecha, hora y responsable en cada etapa: solicitud en HCE, toma, recolección, transporte y recepción en laboratorio. | Media | Alto |
| RFO-10 | El sistema deberá integrarse con los sistemas de laboratorios externos (LIS) para el envío electrónico de solicitudes y la recepción automática de resultados en la HCE del paciente. | Media | Medio |
| RFO-11 | El sistema deberá permitir la planificación y asignación de rutas para servicios externos, como toma de muestras a domicilio o atención de enfermería. | Media | Bajo |

Table 16.16: Requerimientos funcionales de Operaciones

<!-- Página 256 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFO-12 | El sistema deberá mantener un mapa e inventario en tiempo real de la ubicación y estado de todos los equipos médicos móviles (ejemplo: ecógrafos, bombas de infusión). | Alta | Alto |
| RFO-13 | El sistema deberá permitir al personal clínico localizar y solicitar el equipo disponible más cercano a su ubicación. | Alta | Medio |
| RFO-14 | El sistema deberá gestionar el flujo de trabajo de los equipos médicos, generando tareas para traslado, limpieza y preparación entre usos. | Media | Medio |
| RFO-15 | El sistema deberá permitir la planificación centralizada de agendas médicas y turnos rotativos del personal clínico, técnico y administrativo, considerando reglas de negocio de cada rol. | Alta | Alto |
| RFO-16 | El sistema deberá permitir la asignación de tareas operativas (ejemplo: preparación de consulta, ingreso de paciente) al personal disponible con las competencias adecuadas. | Alta | Medio |
| RFO-17 | El sistema deberá medir y reportar indicadores de rendimiento operativo y clínico (ejemplo: tiempo promedio de atención, número de pacientes por hora, tiempo de espera), comparándolos con objetivos de nivel de servicio. | Media | Bajo |
| RFO-18 | El sistema deberá analizar datos históricos de consumo de insumos (desde el módulo de Farmacia/WMS) por cada punto de uso (consulta, sala de procedimiento). | Media | Medio |
| RFO-19 | El sistema deberá recomendar, en base a análisis de frecuencia y volumen, la ubicación física óptima y las cantidades de reposición para cada insumo en los puntos de uso descentralizados. | Media | Medio |
| RFO-20 | El sistema deberá recomendar, en base a patrones de solicitud (desde el módulo de Activos/YMS), la ubicación base o “parking” más eficiente para los equipos móviles compartidos. | Media | Medio |
| RFO-21 | El sistema deberá permitir la definición de perfiles de acceso unificados que apliquen tanto a sistemas de información (HCE, ERP) como a áreas físicas (puertas, torniquetes). | Alta | Alto |
| RFO-22 | El sistema deberá sincronizarse en tiempo real con el módulo de RRHH, de forma que un cambio de rol, licencia o finiquito modifique o revoque automáticamente permisos físicos y digitales. | Alta | Alto |

Table 16.17: Requerimientos funcionales de Operaciones

<!-- Página 257 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFO-23 | El sistema deberá permitir configurar zonas de seguridad (ejemplo: áreas públicas, clínicas, administrativas, farmacia, CPD) y asignar permisos de acceso a dichas zonas según perfil. | Alta | Alto |
| RFO-24 | El sistema deberá registrar y mantener un log auditable de todos los intentos de acceso, tanto exitosos como fallidos, a todos los sistemas y áreas físicas controladas. | Alta | Alto |
| RFO-25 | El sistema deberá mantener un inventario de equipamiento médico e infraestructura, incluyendo historial de mantenimiento, guías del fabricante, estado de garantía y calendario de calibración obligatoria. | Media | Medio |
| RFO-26 | El sistema deberá gestionar la planificación y ejecución de planes de mantenimiento preventivo, generando órdenes de trabajo automáticas basadas en calendario o en horas de uso. | Alta | Alto |
| RFO-27 | El sistema deberá permitir al personal clínico reportar fallas en los equipos, generando órdenes de trabajo correctivas y permitiendo el seguimiento de su resolución. | Alta | Alto |
| RFO-28 | El sistema deberá gestionar el stock de repuestos y vincular su consumo a las órdenes de trabajo correspondientes. | Media | Medio |
| RFO-29 | El sistema deberá generar reportes que demuestren el cumplimiento de planes de mantenimiento y calibración exigidos por normativa de salud y fabricantes. | Media | Medio |
| RFO-30 | El sistema deberá funcionar como repositorio central y controlado de protocolos clínicos, guías de práctica y procedimientos administrativos, gestionando versionamiento y distribución. | Alta | Alto |
| RFO-31 | El sistema deberá proveer un módulo para reporte, investigación y seguimiento de incidentes (ejemplo: caídas de pacientes, errores de medicación), desde su detección hasta su cierre. | Alta | Alto |
| RFO-32 | El sistema deberá gestionar el ciclo de vida de Acciones Correctivas y Preventivas (CAPA), asignando responsables y plazos a partir de hallazgos de incidentes o auditorías. | Alta | Alto |
| RFO-33 | El sistema deberá soportar la planificación, ejecución y registro de auditorías de calidad internas y externas. | Media | Alto |

Table 16.18: Requerimientos funcionales de Operaciones

<!-- Página 258 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RFO-34 | El sistema deberá integrarse con el CRM para gestionar quejas, reclamos y sugerencias de pacientes como entrada clave al proceso de mejora de calidad. | Media | Medio |
| RFO-35 | El sistema deberá generar propuestas de mallas de turnos y agendas para personal clínico, maximizando cobertura de atención y respetando restricciones contractuales, preferencias y regulaciones laborales. | Alta | Alto |
| RFO-36 | El sistema deberá recomendar asignación óptima de recursos limitados (salas, equipos de alto costo) para maximizar su uso y reducir tiempos de espera de pacientes. | Alta | Alto |
| RFO-37 | La plataforma deberá permitir simular el impacto de decisiones estratégicas (ejemplo: contratación de personal, apertura de un nuevo centro) sobre la operación. | Media | Medio |
| RFO-38 | El sistema deberá incluir un portal exclusivo para médicos, con acceso a información clínica, historial de pacientes y herramientas de gestión, asegurando confidencialidad y rapidez en la atención. | Alta | Medio |
| RFO-39 | El sistema deberá incluir un portal de autoservicio para pacientes, que permita agendar citas, consultar resultados, acceder a documentos clínicos y gestionar sus datos de salud. | Alta | Medio |
| RFO-40 | El sistema deberá permitir el intercambio electrónico de documentos de manera segura (informes, recetas, certificados), cumpliendo normativas de interoperabilidad y protección de datos. | Alta | Alto |
| RFO-41 | La solución deberá garantizar intercambio electrónico de documentos entre pacientes, médicos, administración y prestadores externos, con trazabilidad y control de versiones. | Alta | Alto |
| RFO-42 | El sistema deberá permitir el agendamiento de citas y facilitar el auto-monitoreo para pacientes crónicos. | Alta | Alto |
| RFO-43 | El sistema deberá permitir el acceso remoto a la información por parte de médicos y posibilitar la atención mediante telemedicina. | Alta | Alto |
| RFO-44 | El sistema deberá enviar recordatorios automáticos a pacientes (citas, medicamentos, controles), mediante notificaciones en la app o SMS. | Media | Bajo |
| RFO-45 | Restricción: el sistema no deberá permitir acceso remoto a fichas para médicos, medida que reduce riesgos de seguridad pero afecta disponibilidad en movilidad. | Baja | Alto |

Table 16.19: Requerimientos funcionales de Operaciones

<!-- Página 259 del PDF original -->

### 16.2 Requerimientos NO Funcionales del Proyecto

Aquí se describen todos los requerimientos identificados para el proyecto, los cuales serán presentados por módulos.

#### 16.2.1 Modulo de Arquitectura y Diseño del Sistema

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFAD-01 | La solución debe estar diseñada bajo una arquitectura de microservicios desacoplados, donde cada servicio pueda desplegarse, escalarse y mantenerse de forma independiente, favoreciendo la resiliencia, modularidad y mantenibilidad. | Alta | Medio |
| RNFAD-02 | El sistema usará arquitectura basada en eventos con bus/mensajería (pub/sub), entrega al menos una vez, reintentos con backoff exponencial y DLQ; eventos con esquema versionado y trazabilidad (correlationId). | Medio | Medio |
| RNFAD-03 | El sistema se diseñará con responsabilidad única por módulo, asegurando que cada componente tenga un único propósito y dependencias claras, facilitando pruebas y despliegues independientes. | Medio | Bajo |
| RNFAD-04 | El sistema cumplirá este requerimiento no funcional con métricas y criterios de aceptación documentados y verificables. | Medio | Bajo |
| RNFAD-05 | El sistema seguirá arquitectura en capas (presentación, aplicación, integración, datos) con contratos claros y control de dependencias; sin acceso directo de UI a datos. | Medio | Medio |
| RNFAD-06 | El sistema expondrá APIs contract-first con especificaciones OpenAPI 3.1 publicadas, versionado (v1, v2), políticas de deprecación ≥ 6 meses, paginación estándar (limit/offset, default 50, máx 200), idempotencia en operaciones no triviales (Idempotency- Key) y códigos de error normalizados. | Alto | Bajo |
| RNFAD-07 | Se deben ofrecer APIs abiertas y documentadas que permitan interperabilidad con sistemas internos y externos, facilitando la integracion de servicios clinicos, administrativos y de terceros. | Alto | Medio |
| RNFAD-08 | El sistema gestiona APIs con gateway (rate-limit, cuotas, API-keys/OAuth2, validación de esquema, transformaciones), portal de desarrolladores y analítica de uso; políticas de versionado y deprecación documentadas. | Media | Bajo |

<!-- Página 260 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFAD-09 | El sistema se desplegará en contenedores compatibles con estándar OCI, con imágenes inmutables versionadas (SemVer), límites de recursos (CPU/RAM) por servicio, health-checks HTTP/TCP, restart policy y probes de readiness/liveness; las imágenes se firmarán y escanearán por vulnerabilidades antes de pasar a producción. | Alta | Medio |
| RNFAD-10 | El sistema ejecutará servicios principales en plataformas gestionadas con autoescalado de 1 a 50 tareas por servicio, arranque en frío ≤ 2 s para rutas críticas, y actualización rolling sin downtime con 10% de canary. | Alta | Alto |
| RNFAD-11 | El sistema debe dimensionarse automáticamente en función de la carga de trabajo, asegurando que la cantidad de servidores o instancias se incremente o reduzca de acuerdo a la demanda de usuarios y transacciones. | Alta | Alto |
| RNFAD-12 | El sistema orquestará servicios con un planeador que respete afinidad/anti-afinidad, cuotas de recursos y políticas de autosanación; despliegues rolling con máximo 10% de indisponibilidad parcial por servicio. | Alto | Medio |

Table 16.20: Modulo de Arquitectura y Diseño del Sistema

<!-- Página 261 del PDF original -->

<!-- Página sin texto extraíble ni figuras detectadas. -->

<!-- Página 262 del PDF original -->

#### 16.2.2 Módulo de Rendimiento, Escalabilidad y Capacidad

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFREC-01 | El sistema soportará al menos 5.000 usuarios concurrentes sostenidos sin degradar la experiencia, manteniendo P95 de latencia de vistas interactivas ≤ 2s y tasa de error HTTP &lt; 0,2%. | Alto | Alto |
| RNFREC-02 | La plataforma debe soportar el procesamiento de al menos 5.000 usuarios concurrentes sin degradación del servicio, garantizando consistencia de la experiencia. | Alto | Alto |
| RNFREC-03 | El sistema procesará al menos 1.000 transacciones por segundo con confirmación en ≤ 1s en P95, garantizando idempotencia y colas para picos transitorios. | Alto | Alto |
| RNFREC-04 | El sistema debe soportar entre 4.000 y 5.000 consultas médicas diarias, con métricas, auditoría y procedimientos de verificación definidos. | Medio | Medio |
| RNFREC-05 | El sistema debe soportar entre 800 y 1.000 agendamientos diarios, con métricas, auditoría y procedimientos de verificación definidos. | Medio | Medio |
| RNFREC-06 | El sistema debe procesar entre 500 y 700 exámenes diarios, con métricas, auditoría y procedimientos de verificación definidos. | Medio | Medio |
| RNFREC-07 | El sistema debe gestionar entre 400 y 500 llamadas de call center diarias, con métricas, auditoría y procedimientos de verificación definidos. | Medio | Medio |
| RNFREC-08 | El sistema debe procesar entre 3.000 y 4.000 transacciones de facturación diarias, con métricas, auditoría y procedimientos de verificación definidos. | Medio | Medio |
| RNFREC-09 | El sistema debe almacenar 150.000 registros de pacientes, con métricas, auditoría y procedimientos de verificación definidos. | Alto | Medio |
| RNFREC-10 | El sistema debe almacenar 500.000 documentos, con métricas, auditoría y procedimientos de verificación definidos. | Alto | Medio |
| RNFREC-11 | El sistema debe almacenar 50 TB de imágenes médicas, con métricas, auditoría y procedimientos de verificación definidos. | Alto | Medio |
| RNFREC-12 | El sistema debe almacenar 3,5 millones de consultas históricas, con métricas, auditoría y procedimientos de verificación definidos. | Alto | Medio |
| RNFREC-13 | El sistema debe soportar escalado vertical y horizontal, asegurando un rendimiento óptimo incluso en escenarios de alto crecimiento de usuarios. | Alto | Alto |
| RNFREC-14 | El sistema debe escalar horizontal y verticalmente con reglas automáticas de CPU/RAM/cola, manteniendo P95 de latencia API ≤ 800ms hasta 2× la carga nominal, con autoescalado regresivo para optimizar costos fuera de punta. | Alto | Alto |

Table 16.21: Requerimientos Módulo de Rendimiento, Escalabilidad y Capacidad

<!-- Página 263 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFREC-15 | La infraestructura debe permitir un escalamiento elástico (automático o bajo demanda) de los recursos de cómputo para ajustarse a variaciones de carga. | Alto | Medio |
| RNFREC-16 | El sistema debe contar con capacidad de almacenamiento inicial de 100TB y soportar un crecimiento proyectado del 30% anual. | Alto | Medio |
| RNFREC-17 | El sistema debe escalar para soportar entre 8.000 y 10.000 consultas médicas diarias, incluyendo telemedicina, con métricas y auditoría definidas. | Alto | Alto |
| RNFREC-18 | El sistema debe escalar para soportar entre 2.000 y 2.500 agendamientos multicanal diarios, con métricas y auditoría definidas. | Alto | Alto |
| RNFREC-19 | El sistema debe escalar para procesar entre 1.500 y 2.000 exámenes integrados diarios, con métricas y auditoría definidas. | Alto | Alto |
| RNFREC-20 | El sistema debe escalar para gestionar entre 5.000 y 7.000 interacciones digitales diarias, con métricas y auditoría definidas. | Alto | Alto |
| RNFREC-21 | El sistema debe escalar almacenamiento para 400.000 pacientes activos, con métricas y auditoría definidas. | Alto | Medio |
| RNFREC-22 | El sistema debe escalar almacenamiento para 2 millones de documentos, con métricas y auditoría definidas. | Alto | Medio |
| RNFREC-23 | El sistema debe escalar almacenamiento para 200 TB de imágenes médicas, con métricas y auditoría definidas. | Alto | Medio |
| RNFREC-24 | El sistema debe escalar almacenamiento para 10 millones de consultas históricas, con métricas y auditoría definidas. | Alto | Medio |
| RNFREC-25 | El sistema debe permitir procesamiento batch dentro de la ventana de tiempo acordada. | Medio | Bajo |
| RNFREC-26 | El sistema debe permitir registrar un nuevo paciente en un tiempo máximo de 5 minutos, incluyendo la captura de información básica y administrativa. | Alto | Medio |
| RNFREC-27 | El historial clínico del paciente debe estar disponible de forma inmediata (≤ 2s) al momento de la consulta. | Alto | Alto |
| RNFREC-28 | Las operaciones críticas de la aplicación (búsquedas, carga de formularios, validaciones) deben completarse en menos de 1s en condiciones normales de carga. | Alto | Alto |
| RNFREC-29 | El tiempo de respuesta para transacciones en línea no debe superar los 2s en condiciones normales de operación. | Alto | Alto |
| RNFREC-30 | El tiempo de respuesta para consultas simples debe ser inferior a 1s en condiciones normales de operación. | Alto | Alto |
| RNFREC-31 | El tiempo de generación de reportes complejos no debe superar los 30s. | Medio | Medio |
| RNFREC-32 | El tiempo de respuesta de las APIs debe ser ≤ 500ms en P95. | Alto | Alto |

Table 16.22: Requerimientos Módulo de Rendimiento, Escalabilidad y Capacidad

<!-- Página 264 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFREC-33 | El sistema debe gestionar picos de demanda de +150% en campañas de invierno, con métricas y auditoría definidas. | Alto | Alto |
| RNFREC-34 | El sistema debe gestionar picos de demanda de +100% en inicio de año escolar, con métricas y auditoría definidas. | Alto | Alto |
| RNFREC-35 | El sistema debe gestionar picos de demanda de +80% post feriados, con métricas y auditoría definidas. | Alto | Alto |

Table 16.23: Requerimientos no funcionales de Rendimiento, Escalabilidad y Capacidad

<!-- Página 265 del PDF original -->

#### 16.2.3 Modulo de Disponibilidad y Resiliencia

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFDR-01 | El sistema configurará múltiples zonas de disponibilidad para cargas críticas, con failover automático y pruebas trimestrales. | Alta | Alto |
| RNFDR-02 | El sistema operará en al menos 2 zonas de disponibilidad activas con balanceo de carga, sin punto único de falla; actualizaciones canary para evitar downtime perceptible. | Alta | Alto |
| RNFDR-03 | El sistema garantizará una disponibilidad mínima de 99.7% medida mensualmente para servicios críticos, excluyendo ventanas de mantenimiento notificadas con 72 h de anticipación; se reportará tiempo total de indisponibilidad en minutos. | Alta | Medio |
| RNFDR-04 | El proveedor del datacenter principal debe garantizar una disponibilidad del servicio del 99.99% o superior. | Alto | Alto |
| RNFDR-05 | El sistema en caso de falla crítica, la plataforma debe estar totalmente recuperada en un tiempo máximo de 1 hora. | Alto | Bajo |
| RNFDR-06 | El sistema la pérdida de datos aceptable en caso de contingencia no debe superar los 15 minutos desde el último respaldo. | Alto | Medio |
| RNFDR-07 | El sistema realizará respaldos diarios completos e incrementales horarios de bases de datos, retención 30/180/365 días (operativo/archivístico/legales), verificación y prueba de restauración trimestral. | Alto | Medio |
| RNFDR-08 | El site secundario de recuperación ante desastres (DR) debe estar ubicado a una distancia mínima de 100 kilómetros del site principal para mitigar el riesgo de desastres regionales. | Alto | Medio |
| RNFDR-09 | La infraestructura del site secundario debe tener la capacidad de cómputo, almacenamiento y red para soportar el 100% de la carga de producción del site principal. | Alto | Medio |
| RNFDR-10 | Se debe ejecutar y validar un procedimiento de prueba de failover (conmutación por error) hacia el site secundario con una frecuencia mínima mensual para garantizar la efectividad del plan de DR. | Alto | Medio |

Table 16.24: Modulo de Arquitectura y Diseño del Sistema

<!-- Página 266 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFDR-11 | El sistema implementará tolerancia a fallos con timeouts (APIs 30 s, externos 3 s), circuit breakers (abre tras 5 fallos/30 s), reintentos con backoff y degradación controlada (leer-solo/caché) ante caídas de dependencias. | Alto | Medio |
| RNFDR-12 | El sistema degradará funciones no críticas (p. ej., recomendaciones, encuestas) para priorizar flujos de atención cuando los recursos estén bajo presión, preservando operaciones clínicas y de caja. | Alto | Medio |

Table 16.25: Modulo de Arquitectura y Diseño del Sistema

<!-- Página 267 del PDF original -->

#### 16.2.4 Módulo de Seguridad de la Información

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFS-01 | El sistema aplicará principios Zero Trust: autenticación/autorización en cada solicitud, microsegmentación, políticas de mínima exposición, verificación continua de identidad y postura del dispositivo. | Alto | Alto |
| RNFS-02 | El sistema se desplegará en nube con red privada, subredes separadas por capas, SG/NACL restrictivas, WAF, protección DDoS, bastion host con MFA y rotación de claves; cifrado en reposo y tránsito. | Alto | Alto |
| RNFS-03 | El sistema cumplirá prácticas de seguridad equivalentes al entorno hospitalario: control de acceso estricto, auditoría completa, segregación de funciones, gestión de parches críticos ≤ 30 días. | Alto | Alto |
| RNFS-04 | El sistema habilitará versionado y cifrado de datos/objetos (AES-256/KMS) con políticas WORM para respaldos críticos y retención configurada. | Alto | Medio |
| RNFS-05 | Toda la información debe encriptarse tanto en almacenamiento (reposo) como en comunicación (tránsito), utilizando algoritmos robustos AES-256 o superior. | Alto | Alto |
| RNFS-06 | El sistema requerirá MFA para usuarios con privilegios (administradores, DevOps, DBAs), con factores TOT- P/U2F y políticas de rotación de credenciales. | Alto | Alto |
| RNFS-07 | El sistema implementará DLP para prevenir exfiltración de datos sensibles por web, correo y almacenamiento; enmascaramiento de datos en entornos no productivos. | Alto | Alto |
| RNFS-08 | El sistema registrará todas las acciones administrativas y de API en un trilho de auditoría inmutable con retención ≥ 365 días y alertas por eventos críticos. | Alto | Alto |
| RNFS-09 | El sistema mantendrá auditoría y logging completos: quién, qué, cuándo, desde dónde; retención de logs clínicos ≥ 6 años y operativos ≥ 1 año; correlación de transacciones. | Alto | Alto |
| RNFS-10 | El sistema mantendrá logging/auditoría estructurada (JSON) con correlationId, usuario, rol, IP, endpoint, operación, resultado y latencia; redacción de PII en logs; retención ≥ 12 meses operativa y ≥ 6 años clínica en WORM. | Alto | Alto |
| RNFS-11 | El sistema protegerá frontales web con WAF (OWASP CRS), reglas personalizadas, bloqueo/ratelimiting y monitoreo de falsos positivos. | Alto | Medio |

Table 16.26: Requerimientos No Funcionales Módulo de Seguridad

<!-- Página 268 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFS-12 | El sistema contará con NOC y SOC 24x7 para monitoreo y respuesta, con procedimientos de escalamiento y comunicación definidos. | Alto | Alto |
| RNFS-13 | El sistema operará SOC 24x7 con SIEM, IDS/IPS, casos de uso MITRE ATT&CK y respuesta a incidentes documentada (contención, erradicación, recuperación). | Alto | Alto |
| RNFS-14 | El sistema gestionará incidentes y problemas siguiendo ITIL: MTTD ≤ 5 min, MTTR ≤ 60 min para severidad alta, post-mortem sin culpa y seguimiento de acciones correctivas. | Alto | Alto |
| RNFS-15 | El sistema cumplirá este requerimiento no funcional con métricas y criterios de aceptación documentados y verificables. | Medio | Bajo |
| RNFS-16 | El sistema debe validar en tiempo real cada prescripción contra los datos de la HCE, generando alertas bloqueantes por alergias, interacciones medicamentosas o dosis fuera de rangos seguros. | Alta | Alta |

Table 16.27: Requerimientos no funcionales de Modulo de Seguridad

<!-- Página 269 del PDF original -->

#### 16.2.5 Módulo de Operación y Mantenimiento

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFOM-01 | El sistema deberá ser monitoreado en todo momento con métricas, logs y trazas; incluirá alertas por SLO (latencia, errores, saturación) y monitoreo sintético de flujos críticos (agendar, pagar, abrir HCE) cada 5 minutos, con esquema de guardia (on-call). | Alto | Alto |
| RNFOM-02 | El sistema deberá contar con monitoreo continuo 24x7x365 de la infraestructura y servicios críticos, para la detección temprana de incidentes. | Alto | Alto |
| RNFOM-03 | El sistema deberá operar un Centro de Operaciones de Red (NOC) 24x7 con tableros en tiempo real, runbooks por alerta y gestión de capacidad; además se revisarán semanalmente los patrones de incidentes para implementar acciones preventivas. | Alto | Alto |
| RNFOM-04 | El sistema realizará monitoreo proactivo con predicciones de capacidad, umbrales dinámicos y detección de anomalías, ejecutando acciones automatizadas (escalamiento, reinicio controlado) antes de afectar a los usuarios. | Alto | Medio |
| RNFOM-05 | El sistema gestionará incidentes y problemas conforme a prácticas ITIL, con clasificación y priorización; MTTD ≤ 5 min, MTTR ≤ 60 min en severidad alta, post-mortem sin culpa y seguimiento hasta cierre. | Alto | Alto |
| RNFOM-06 | El sistema deberá asegurar soporte 24x7 para emergencias críticas, con canal prioritario, primera respuesta ≤ 10 min y escalamiento inmediato a especialistas. | Alto | Alto |
| RNFOM-07 | El sistema deberá operar el call center de lunes a domingo de 07:00 a 24:00, con tiempo de respuesta &lt; 20 segundos, tasa de abandono &lt; 5%, resolución en primer contacto &gt; 70% y satisfacción de usuarios &gt; 85%. | Medio | Medio |
| RNFOM-08 | El sistema deberá incluir múltiples canales de atención digital (IVR inteligente, webchat con bot nivel 1, email con ticket automático, WhatsApp Business y App móvil), con métricas, umbrales, auditoría y procedimientos de verificación. | Medio | Bajo |

Table 16.28: Requerimientos no funcionales de Operación y Mantenimiento

<!-- Página 270 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFOM-09 | El sistema deberá garantizar un canal inicial confiable para el registro de casos, consultas y solicitudes, asegurando trazabilidad completa. | Medio | Bajo |
| RNFOM-10 | El sistema deberá seguir protocolos documentados de escalamiento, con responsables definidos y tiempos asociados según severidad. | Medio | Medio |
| RNFOM-11 | El sistema deberá contar con configuraciones avanzadas y especialistas por tecnología (DB, redes, seguridad, contenedores) para resolver incidentes complejos. | Alto | Medio |
| RNFOM-12 | El sistema deberá disponer de lineamientos y métricas de resolución técnica de problemas (troubleshooting), incluyendo documentación de pasos y validación de resultados. | Medio | Medio |
| RNFOM-13 | El sistema permitirá la intervención inmediata en problemas críticos, con métricas de desempeño, auditoría y documentación del proceso de resolución. | Alto | Alto |
| RNFOM-14 | El sistema incorporará procesos continuos de ajuste y optimización de rendimiento en servidores, bases de datos y aplicaciones críticas. | Alto | Medio |
| RNFOM-15 | El sistema deberá cerrar incidentes con análisis de causa raíz documentado, métricas de verificación y planes de prevención de recurrencia. | Alto | Medio |
| RNFOM-16 | El sistema dispondrá de soporte de fabricantes para bugs o defectos de producto, garantizando escalamiento máximo en incidentes críticos. | Alto | Medio |
| RNFOM-17 | El sistema ejecutará mantenimientos planificados en ventanas predefinidas (ej. domingos 2:00-6:00 AM), sin afectar el SLA percibido, usando despliegues canary; con notificación ≥72h, rollback documentado y validación postmantenimiento. | Alto | Medio |
| RNFOM-18 | El sistema incluirá revisiones periódicas: diaria de logs, semanal de performance y capacidad, mensual de parches, trimestral de hardware y firmware, y anual de arquitectura completa y obsolescencia. | Medio | Bajo |
| RNFOM-19 | El sistema documentará todos los mantenimientos, incluyendo plan de trabajo, validación post-mantenimiento y registro de cambios. | Medio | Medio |
| RNFOM-20 | El sistema contará con un Service Delivery Manager dedicado, administradores de plataforma 24x7, DBAs certificados y analistas de seguridad responsables de vulnerabilidades, configuraciones y pruebas de penetración. | Alto | Alto |

Table 16.29: Requerimientos no funcionales de Operación y Mantenimiento

<!-- Página 271 del PDF original -->

#### 16.2.6 Módulo de Integración e Interoperabilidad

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFII-01 | El sistema deberá integrarse con laboratorios e imagenología mediante HL7 v2 (ORM/ORU) y DICOM (Worklist/MPPS/Storage), permitiendo órdenes electrónicas, recepción de resultados estructurados (PDF/HL7 ORU) y vinculación automática al episodio del paciente. | Medio | Medio |
| RNFII-02 | El sistema deberá exponer interoperabilidad mediante APIs REST FHIR (Patient, Appointment, Encounter, Observation, DocumentReference) con OAuth2/OIDC, scopes por recurso, paginación y límites de tasa documentados; deberá publicar guía de integración y sandbox. | Alto | Alto |
| RNFII-03 | El sistema deberá proveer interfaces HL7 v2.5.1/2.6 y FHIR R4, incluyendo mensajes ORM^O01, ORU^R01 y recursos Patient/Appointment/Encounter/Observation/DocumentReference; deberá documentar endpoints, autenticación y catálogos de códigos (CIE-10, LOINC). | Alto | Alto |
| RNFII-04 | El sistema deberá garantizar integración entre HCE, agendamiento, facturación y CRM vía eventos y APIs internas, asegurando consistencia eventual en ≤ 5 s, idempotencia por messageid y reconciliaciones diarias. | Alto | Alto |
| RNFII-05 | El sistema deberá sincronizar datos críticos en tiempo casi real con latencia objetivo P95 ≤ 5 s entre módulos, utilizando colas/eventos y mecanismos de reintento con backoff; las inconsistencias se resolverán con reconciliación programada. | Alto | Alto |
| RNFII-06 | El sistema deberá integrarse con sistemas legacy mediante conectores dedicados o intercambio por archivos seguros (SFTP/CSV/XML), con validación de esquema, codificación UTF-8, ventanas batch y reportes de error detallados. | Alto | Medio |
| RNFII-07 | El sistema deberá ejecutar migración de datos históricos con mapeo campo-a-campo, reglas de transformación validadas, reconciliación ≥ 99,9% de coincidencia, plan de rollback y anonimización/pseudonimización en ambientes no productivos. | Alto | Medio |

Table 16.30: Requerimientos no funcionales de Integración e Interoperabilidad

<!-- Página 272 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFII-08 | El sistema deberá integrarse con dispositivos médicos IoT (glucómetros, tensiómetros, pulsioxímetros, entre otros), de forma que las mediciones realizadas en casa por el paciente se transmitan automáticamente a la plataforma en tiempo real, almacenándose en la HCE y generando alertas automáticas al equipo de salud en caso de valores críticos fuera de rango. | Alto | Alto |
| RNFII-09 | El sistema deberá integrarse con la plataforma de venta de bonos electrónicos (Fonasa o Isapres), de modo que durante el proceso de admisión o pago se pueda emitir el bono de atención directamente desde la misma interfaz, sin necesidad de pasos manuales externos. | Alto | Medio |
| RNFII-10 | El sistema deberá integrar la gestión de correos electrónicos dentro del CRM, de manera que los correos enviados por pacientes (ej. casilla de contacto o soporte) queden registrados como casos o tickets en la plataforma, con posibilidad de asignarlos a agentes para respuesta y seguimiento, al igual que una consulta telefónica o de chat. | Medio | Medio |
| RNFII-11 | El sistema deberá integrar oficialmente la WhatsApp Business API para el manejo de mensajes dentro del CRM, de modo que los mensajes de texto enviados por pacientes al número de la clínica sean recibidos en la plataforma como tickets o chats, y los agentes puedan responder directamente desde el CRM manteniendo un historial centralizado. | Alto | Alto |

Table 16.31: Requerimientos no funcionales de Integración e Interoperabilidad

<!-- Página 273 del PDF original -->

#### 16.2.7 Módulo de Cumplimiento Normativo y Certificaciones

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFCN-01 | El sistema gestionará datos personales conforme a la Ley 19.628, incluyendo consentimiento informado, finalidades explícitas, derechos ARCO, minimización de datos y medidas de seguridad proporcionales (cifrado, control de acceso, auditoría). | Alto | Alto |
| RNFCN-02 | El sistema mantendrá controles para prevenir, detectar y reportar delitos informáticos (Ley 21.096), incluyendo monitoreo de intrusiones, integridad de logs (WORM), preservación de evidencias con cadena de custodia y sincronización horaria NTP. | Alto | Alto |
| RNFCN-03 | El sistema soportará el modelo de cumplimiento de la Ley 20.393, con segregación de funciones en procesos críticos, aprobaciones duales, trazabilidad completa y registro de políticas y capacitaciones con evidencia de aceptación. | Alto | Alto |
| RNFCN-04 | El sistema protegerá y reportará información financiera conforme a lineamientos de la CMF, incluyendo conciliación diaria, integridad de registros, control de acceso por rol y resguardo de evidencias tributarias. | Alto | Medio |
| RNFCN-05 | El sistema almacenará logs operativos por al menos 6 meses y logs clínicos por 6 años en repositorio inmutable (WORM), incluyendo eventos de acceso, cambios de datos, prescripciones y operaciones administrativas. | Alto | Alto |
| RNFCN-06 | El sistema implementará un Sistema de Gestión de Seguridad de la Información certificado bajo NCh-ISO 27001. | Alto | Medio |
| RNFCN-07 | El sistema adoptará el Código de Prácticas para la Gestión de Seguridad conforme a NCh-ISO 27002. | Medio | Medio |
| RNFCN-08 | El sistema gestionará riesgos de seguridad conforme a NCh-ISO 27005, documentando metodologías y planes de mitigación. | Medio | Medio |

Table 16.32: Requerimientos no funcionales de Cumplimiento Normativo y Certificaciones

<!-- Página 274 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFCN-09 | El sistema adoptará directrices para ciberprotección conforme a NCh-ISO 27032. | Medio | Medio |
| RNFCN-10 | El sistema garantizará seguridad en relaciones con proveedores conforme a NCh-ISO 27036 (partes 1, 2 y 3). | Medio | Medio |
| RNFCN-11 | El sistema garantizará control de acceso físico a ambientes críticos conforme a la norma NCh 2777. | Alto | Medio |
| RNFCN-12 | El sistema contará con certificación Cloud Security Alliance (CSA) para servicios en la nube, garantizando prácticas seguras en entornos cloud. | Medio | Medio |
| RNFCN-13 | El datacenter deberá contar con certificaciones vigentes ISO 27001 y SOC 2, garantizando seguridad en la operación. | Alto | Medio |
| RNFCN-14 | El datacenter principal deberá estar certificado como Tier III o superior, garantizando redundancia y continuidad de servicio. | Alto | Medio |
| RNFCN-15 | El datacenter principal deberá cumplir con normativas Tier III o equivalentes, asegurando disponibilidad y resiliencia. | Alto | Medio |

Table 16.33: Requerimientos no funcionales de Cumplimiento Normativo y Certificaciones

<!-- Página 275 del PDF original -->

#### 16.2.8 Módulo de Hardware e Infraestructura

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFHI-01 | El sistema deberá garantizar un ancho de banda provisto sin aplicar políticas de throttling que limiten el rendimiento. | Alto | Alto |
| RNFHI-02 | El sistema deberá disponer de enlaces dedicados entre centros médicos con redundancia activaactiva, ancho de banda mínimo de 200 Mbps por sede, QoS para tráfico clínico, failover &lt; 30 s, encriptación sitio a sitio y monitoreo de latencia/jitter. | Alto | Alto |
| RNFHI-03 | El sistema deberá ofrecer acceso remoto mediante VPN IPSec/SSL con MFA, split-tunnel controlado, verificación de postura del dispositivo, perfiles por rol, desconexión por inactividad de 15 min y rotación de certificados/credenciales cada 90 días. | Alto | Alto |
| RNFHI-04 | El sistema deberá asegurar que la conectividad del datacenter principal disponga de un ancho de banda mínimo de 10 Gbps. | Alto | Alto |
| RNFHI-05 | El sistema deberá contar con infraestructura de red con múltiples carriers para garantizar redundancia y evitar puntos únicos de fallo. | Alto | Alto |
| RNFHI-06 | El sistema deberá disponer de servidores edge en cada bodega, con soporte de virtualización y redundancia de hardware, asegurando continuidad operativa. | Alto | Medio |
| RNFHI-07 | El sistema deberá contar con almacenamiento local de al menos 10 TB útiles, configurados bajo RAID10 para tolerancia a fallas. | Alto | Medio |
| RNFHI-08 | El sistema deberá proteger los equipos críticos mediante UPS con autonomía mínima de 2 horas para garantizar continuidad en cortes eléctricos. | Alto | Alto |
| RNFHI-09 | El sistema deberá disponer de generadores de respaldo en sitios críticos para asegurar operación continua en contingencias prolongadas. | Alto | Alto |
| RNFHI-10 | El sistema deberá desplegar infraestructura de Edge Computing mediante mini datacenters locales en cada ubicación geográfica, reduciendo latencia y mejorando resiliencia. | Alto | Alto |

Table 16.34: Requerimientos no funcionales de Hardware e Infraestructura

<!-- Página 276 del PDF original -->

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFHI-11 | El sistema deberá permitir que cada site edge opere de forma autónoma durante al menos 72 horas. | Alto | Alto |
| RNFHI-12 | El sistema deberá sincronizar datos con la nube en forma bidireccional en los sites edge, asegurando consistencia eventual. | Alto | Medio |
| RNFHI-13 | El sistema deberá implementar caché local en sites edge para almacenar datos críticos y garantizar acceso rápido durante la operación normal o autónoma. | Alto | Medio |
| RNFHI-14 | El sistema deberá realizar procesamiento local de datos críticos en sites edge para minimizar la latencia en operaciones sensibles. | Alto | Alto |
| RNFHI-15 | El sistema deberá utilizar dispositivos móviles rugerizados con certificación IP78 y sistema operativo Android 11 o superior. | Alto | Medio |
| RNFHI-16 | El sistema deberá contar con dispositivos móviles que soporten al menos 12 horas de operación continua. | Medio | Medio |
| RNFHI-17 | El sistema deberá disponer de dispositivos móviles con GPS de alta precisión, con margen de error menor a 5 metros. | Medio | Medio |
| RNFHI-18 | El sistema deberá garantizar que los smartphones cuenten con conectividad 4G/5G, Wi-Fi y Bluetooth para operación en distintos entornos. | Alto | Medio |
| RNFHI-19 | El sistema deberá incluir lectores biométricos de huella y reconocimiento facial con FAR &lt; 0,001%. | Alto | Alto |
| RNFHI-20 | El sistema deberá disponer de cámaras LPR con capacidad de lectura de patentes con precisión ≥ 98%. | Medio | Medio |
| RNFHI-21 | El sistema deberá contar con torniquetes bidireccionales con múltiples métodos de autenticación. | Medio | Medio |
| RNFHI-22 | El sistema deberá utilizar barreras vehiculares automáticas con sistema anti-passback. | Medio | Medio |
| RNFHI-23 | El sistema deberá contar con paneles de control con capacidad de operación offline durante al menos 72 horas. | Alto | Medio |
| RNFHI-24 | El sistema deberá utilizar headsets profesionales con cancelación de ruido para asegurar calidad de comunicación en ambientes de alta carga. | Medio | Bajo |
| RNFHI-25 | El sistema deberá incluir softphone con integración nativa a CRM. | Medio | Bajo |
| RNFHI-26 | El sistema deberá garantizar que las estaciones de trabajo cuenten con pantallas duales para operación eficiente. | Medio | Bajo |
| RNFHI-27 | El sistema deberá incluir cámaras web compatibles para videoatención. | Medio | Bajo |

Table 16.35: Requerimientos no funcionales de Hardware e Infraestructura

<!-- Página 277 del PDF original -->

#### 16.2.9 Módulo de Usabilidad

| ID | Descripción | Prioridad | Riesgo |
| --- | --- | --- | --- |
| RNFUS-01 | La interfaz del sistema debe estar diseñada bajo principios de usabilidad y ergonomía médica, reduciendo la curva de aprendizaje y priorizando la eficiencia del personal clínico en tareas críticas. | Alto | Medio |

Table 16.36: Requerimientos no funcionales de Usabilidad

### 16.3 Requerimientos del proyecto

Figure 16.1: 1ra pag. - Requerimientos del proyecto

El documento de requerimientos actualizados debido a su extensión se adjuntará como documento aparte para su correcto manejo y visualización.

![Página 277 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-277.png)

<!-- Página 278 del PDF original -->

### 16.4 EDT Completa

Figure 16.2: Estructura de desglose del Trabajo (EDT)

![Página 278 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-278.png)

<!-- Página 279 del PDF original -->

This page intentionally left blank.

<!-- Página 280 del PDF original -->

This page intentionally left blank.

<!-- Página 281 del PDF original -->

![Página 281 del original: conservación de diagramas e imágenes](propuesta-tecnica-del-pancho-imagenes/pagina-281.png)
