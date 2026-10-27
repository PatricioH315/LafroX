# K4 — Base de programación del frente B

Captura anterior a la modificación de fuentes. HEAD: `93a5e884b3f8397e8f3ec7fc76e1e6a45f351b8e`. Los cinco PDF tenían cambios de recompilación autorizada; las fuentes de fechas, HH y curvas no tenían cambios.

- `K4_PAQUETES.csv`: los 227 paquetes, clase, rol, meses, HH, entregable, aceptación, período/hito y, para 168 paquetes, fechas, equipos y predecesoras. Los otros 59 son continuos.
- `K4_MANIFIESTO.json`: hashes SHA-256 de las cuatro fuentes numéricas para comprobar que no se han cambiado fechas, horas ni curvas por accidente.
- HH de paquetes: 207.487; restauraciones previas: 128; soporte puente: 9.336; reserva protegida: 3.072. Total: **220.023 HH**. No sumar componentes una segunda vez.
- Reserva protegida: meses 13–20, 256 HH DES y 128 HH CAL por mes. No se presta a E2 ni equivale a reserva monetaria o días de holgura.
- Peak de curva conjunta: **64 personas equivalentes, mes 16**. No acredita simultaneidad diaria ni asignación nominal.
- Fechas publicadas de T15 como referencia. Producción objetivo: 05-05/05-10-2028; aceptación objetivo: H7 29-05-2028, H12 25-10-2028. El cierre previo exige procedimiento de revisión compatible y evidencia completa.

La disponibilidad de personas, los refuerzos CAL, la reserva histórica de gestión de 1.600 HH y las reservas por riesgo requieren validación de sus dueños. K4 facilita esa revisión y no certifica recursos disponibles ni resultados de pruebas.

El CSV se conserva como captura inicial. `verificar_frente_b.py` no lo sobrescribe; K6 compara el estado posterior con sus fuentes. Cualquier nueva captura debe versionarse expresamente, sin reemplazar ésta.
