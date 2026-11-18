"""Escenario de programación para D-16; no modifica el T-15 ni sus curvas.

Comprueba capacidad neta por equipo. Las habilitaciones externas y la
disponibilidad nominal de cada perfil deben verificarse al nivelar los frentes.
"""

from bisect import bisect_left, bisect_right
from dataclasses import dataclass
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from math import ceil
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PAQUETES = ROOT / "formulario-t15/tablas/tab_T15_paquetes.tex"
CENTAVO = Decimal("0.01")
HH_POR_DIA = Decimal("6.4")
FERIADOS = {date(2027, 6, 21), date(2027, 6, 28), date(2027, 7, 16)}
DIAS = tuple(
    dia
    for n in range(92)
    if (dia := date(2027, 6, 1) + timedelta(days=n)).weekday() < 5
    and dia not in FERIADOS
)


@dataclass(frozen=True)
class Paquete:
    codigo: str
    hh: Decimal
    personas: int
    inicio: date
    fin: date


@dataclass(frozen=True)
class Actividad:
    codigo: str
    nombre: str
    hh: Decimal
    personas: int
    inicio: date
    fin: date
    predecesoras: tuple[str, ...]


# Los pesos de construcción provienen de los elementos de alcance del T-15.
# Los repartos internos de análisis, pruebas, conformidad y entrega son estimaciones.
RECEPCION = (
    ("Diseñar el registro de recepción, lotes, vencimientos y etiquetas", 64),
    ("Verificar los contratos de Recepción con Inventario y Preparación", 28),
    ("Implementar recepción contra OC y discrepancias", 48),
    ("Implementar captura GS1 de lote y vencimiento", 48),
    ("Implementar no conformidad, fotografía y cuarentena", 48),
    ("Generar el SSCC y la etiqueta GS1-128", 48),
    ("Validar condiciones térmicas al ubicar el SSCC", 24),
    ("Incorporar el maestro de productos", 48),
    ("Registrar el ingreso al ERP con cola y reintento", 64),
    ("Conectar y validar la impresora de etiquetas", 64),
    ("Guardar recepciones en el terminal sin red", 60),
    ("Sincronizar recepciones y controlar duplicados al reconectar", 60),
    ("Verificar el tiempo de registro del ítem", 24),
    ("Probar lotes, vencimientos, etiquetas y discrepancias", 70),
    ("Probar cuarentena, reintentos y recuperación de enlace", 64),
    ("Integrar los flujos de Recepción y ejecutar sus pruebas en QA", 72),
    ("Verificar la evidencia y entregar Recepción en QA", 32),
)
INVENTARIO = (
    ("Diseñar las ubicaciones y el saldo por lote", 56),
    ("Diseñar las reglas de conteo, FEFO y reposición", 40),
    ("Verificar los contratos de Inventario con Recepción y Preparación", 28),
    ("Implementar instalaciones, zonas y ubicaciones", 48),
    ("Consolidar el stock y publicar el saldo vendible", 48),
    ("Clasificar SKU por rotación ABC", 48),
    ("Proponer ubicaciones según la clasificación ABC", 48),
    ("Registrar conteos, ajustes y causas", 48),
    ("Registrar existencias en tránsito", 48),
    ("Mostrar ocupación por zona", 24),
    ("Aplicar FEFO y detectar vencimientos", 48),
    ("Incorporar lecturas de cross-docking", 48),
    ("Validar temperatura en reubicaciones", 24),
    ("Registrar mermas por vencimiento", 24),
    ("Calcular la reposición sugerida por SKU", 48),
    ("Aplicar el efecto de promociones sobre la reposición", 48),
    ("Traspasar reposición y transferencias al ERP", 64),
    ("Probar saldos, ubicaciones, conteos y FEFO", 50),
    ("Probar tránsito, reubicaciones térmicas y cross-docking", 52),
    ("Probar reposición, promociones y transferencias al ERP", 52),
    ("Integrar los flujos de Inventario y ejecutar sus pruebas en QA", 56),
    ("Verificar la evidencia y entregar Inventario en QA", 32),
)
PREPARACION = (
    ("Diseñar misiones, recorrido y cierre del pedido", 64),
    ("Verificar las interfaces de Preparación y configurar los simuladores", 28),
    ("Generar misiones de preparación por turno", 48),
    ("Secuenciar el picking de zonas seca y refrigerada", 48),
    ("Incorporar congelado al final del recorrido", 48),
    ("Validar líneas por escaneo y registrar el lote", 48),
    ("Registrar faltantes y su causa", 24),
    ("Asignar lotes aplicando FEFO", 48),
    ("Ordenar la carga en sentido inverso a la ruta", 48),
    ("Controlar el tiempo fuera de frío en el andén", 48),
    ("Enviar al ERP el cierre de misión", 64),
    ("Guardar confirmaciones sin señal en cámara", 60),
    ("Sincronizar las confirmaciones al recuperar cobertura", 60),
    ("Medir el tiempo de confirmación de una línea", 24),
    ("Comprobar el uso del terminal con guantes a −22 °C", 48),
    ("Probar secuencia, escaneo, FEFO y faltantes con datos de prueba", 54),
    ("Probar la desconexión y el control del andén", 50),
    ("Probar el contrato de cierre de misión y preparar los casos integrados", 50),
    ("Integrar Preparación con Recepción e Inventario en QA", 56),
    ("Verificar resultados y entregar Preparación en QA", 32),
)


def leer_paquetes() -> dict[str, Paquete]:
    paquetes = {}
    for linea in PAQUETES.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\s*4\.1\.[123]\s*&", linea):
            continue
        codigo, _, equipo, hh, inicio, fin, _ = [s.strip() for s in linea.split(" & ")]
        a, b = (date.fromisoformat("-".join(d.split("-")[::-1])) for d in (inicio, fin))
        paquetes[codigo] = Paquete(
            codigo, Decimal(hh.replace(",", ".")), int(equipo.split("/")[-1]), a, b
        )
    if set(paquetes) != {"4.1.1", "4.1.2", "4.1.3"}:
        raise ValueError("Falta un paquete de D-16 en la tabla de programación")
    return paquetes


def repartir(hh: Decimal, tareas: tuple[tuple[str, int], ...]) -> list[Decimal]:
    peso_total = sum(peso for _, peso in tareas)
    horas = [(hh * peso / peso_total).quantize(CENTAVO, ROUND_HALF_UP) for _, peso in tareas]
    horas[-1] += hh - sum(horas)
    return horas


def programar(
    paquete: Paquete,
    tareas: tuple[tuple[str, int], ...],
    esperas: dict[int, tuple[Actividad, ...]],
    limite: date,
) -> list[Actividad]:
    """Usa la capacidad neta de un equipo fijo; no acredita asignación nominal."""
    horas = repartir(paquete.hh, tareas)
    if paquete.codigo == "4.1.3":
        # La integración real de Preparación no consume menos de 80 HH en el T-15.
        horas[-1] += horas[-2] - Decimal(80)
        horas[-2] = Decimal(80)
    capacidad = paquete.personas * HH_POR_DIA
    cursor = bisect_left(DIAS, paquete.inicio) * capacidad
    resultado: list[Actividad] = []
    for indice, ((nombre, _), hh) in enumerate(zip(tareas, horas, strict=True), 1):
        precedencias = esperas.get(indice, ())
        for anterior in precedencias:
            cursor = max(cursor, bisect_right(DIAS, anterior.fin) * capacidad)
        primero = int(cursor // capacidad)
        cursor += hh
        ultimo = int((cursor - CENTAVO) // capacidad)
        if not 8 <= hh <= 80 or ultimo - primero + 1 > 10:
            raise ValueError(f"{paquete.codigo}.A{indice:02}: excede la regla de tamaño")
        if ultimo >= len(DIAS) or DIAS[ultimo] > limite:
            fecha = DIAS[ultimo] if ultimo < len(DIAS) else "fuera del calendario"
            raise ValueError(f"{paquete.codigo}.A{indice:02}: termina {fecha}, después de {limite}")
        ids = [a.codigo for a in precedencias]
        if resultado:
            ids.insert(0, resultado[-1].codigo)
        resultado.append(
            Actividad(
                f"{paquete.codigo}.A{indice:02}", nombre, hh, paquete.personas,
                DIAS[primero], DIAS[ultimo], tuple(ids),
            )
        )
    if sum(a.hh for a in resultado) != paquete.hh:
        raise ValueError(f"{paquete.codigo}: HH no conciliadas")
    return resultado


def escenario(paquetes: dict[str, Paquete], entregar_recepcion: date) -> list[Actividad]:
    m1, m2, m5 = (paquetes[codigo] for codigo in ("4.1.1", "4.1.2", "4.1.3"))
    r = programar(m1, RECEPCION, {}, entregar_recepcion)
    i = programar(m2, INVENTARIO, {}, m2.fin)
    # La construcción puede avanzar contra simuladores; la integración real no.
    p = programar(m5, PREPARACION, {2: (r[1], i[2]), 19: (r[-1], i[-1])}, m5.fin)
    return r + i + p


def fin_integracion_desde_entrega(entrega: date, personas: int) -> date:
    """Calcula el fin más temprano para 80 HH con un vínculo fin–comienzo."""
    dias = ceil(Decimal(80) / (personas * HH_POR_DIA))
    return DIAS[bisect_right(DIAS, entrega) + dias - 1]


def informe(actividades: list[Actividad]) -> str:
    lines = [
        "| Actividad | Resultado | Inicio | Fin | HH | Personas máx. | Predecesoras |",
        "|---|---|---|---|---:|---:|---|",
    ]
    for a in actividades:
        hh = f"{a.hh:.2f}".replace(".", ",")
        predecessors = ", ".join(a.predecesoras) or "Inicio del paquete"
        lines.append(
            f"| {a.codigo} | {a.nombre} | {a.inicio:%d-%m-%Y} | {a.fin:%d-%m-%Y} | "
            f"{hh} | {a.personas} | {predecessors} |"
        )
    return "\n".join(lines)


def verificar() -> None:
    paquetes = leer_paquetes()
    fin_publicado = max(paquetes["4.1.1"].fin, paquetes["4.1.2"].fin)
    assert fin_integracion_desde_entrega(
        fin_publicado, paquetes["4.1.3"].personas
    ) == date(2027, 8, 10)
    assert repartir(Decimal("100.01"), (("a", 1), ("b", 1))) == [
        Decimal("50.01"), Decimal("50.00")
    ]
    actividades = escenario(paquetes, date(2027, 8, 2))
    assert len({a.codigo for a in actividades}) == len(actividades)
    por_codigo = {a.codigo: a for a in actividades}
    ultima = {a.codigo.rsplit(".", 1)[0]: a for a in actividades}
    assert ultima["4.1.1"].fin == date(2027, 8, 2)
    assert ultima["4.1.3"].fin == paquetes["4.1.3"].fin
    real = por_codigo["4.1.3.A19"]
    assert real.hh == 80
    assert real.inicio > max(ultima["4.1.1"].fin, ultima["4.1.2"].fin)
    try:
        escenario(paquetes, date(2027, 7, 30))
    except ValueError as error:
        assert "después" in str(error)
    else:
        raise AssertionError("El equipo no puede entregar Recepción el 30-07")


if __name__ == "__main__":
    if sys.argv[1:] == ["--verificar"]:
        verificar()
        print("D-16: verificados totales, fechas, dependencias y caso inviable")
    else:
        print(informe(escenario(leer_paquetes(), date(2027, 8, 2))))
