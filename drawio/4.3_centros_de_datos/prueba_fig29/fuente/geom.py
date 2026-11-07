"""Geometría única del recinto técnico del CD Talca (metros, origen en la esquina
interior suroeste de la zona de trabajo; x hacia el este, y hacia el norte)."""

T_INT = 0.15   # tabique interior
T_EXT = 0.20   # muro perimetral con blindaje
H_WALL = 3.0   # altura libre (para la vista 3D)

ROOMS = {
    # id: (x0, y0, x1, y1, nombre)
    'W': (0.00, 0.00, 2.40, 2.50, 'Zona de trabajo y respaldo'),
    'P': (2.55, 0.00, 3.75, 3.00, 'Pasillo de control'),
    'E': (2.55, 3.15, 3.75, 4.35, 'Esclusa'),
    'U': (3.90, 0.00, 7.50, 2.00, 'Sala de UPS y baterías'),
    'S': (3.90, 2.15, 7.50, 5.65, 'Sala de servidores y comunicaciones'),
}
NUM = {'W': 1, 'P': 2, 'E': 3, 'U': 4, 'S': 5}

FACADE_Y = 5.65 + T_EXT          # cara exterior del muro norte del edificio

# Puertas: (id, muro, cara del muro hacia donde abre, desde, hasta, abre hacia, bisagra)
# muro 'h' = muro horizontal; 'v' = vertical. 'cara' es la coordenada de la cara del
# muro del lado hacia donde abre la hoja.
DOORS = [
    ('entrada', 'h', 0.00, 2.75, 3.65, 'N', 'W'),   # acceso principal al pasillo
    ('W',       'v', 2.40, 1.60, 2.40, 'W', 'N'),   # pasillo -> zona de trabajo
    ('U',       'v', 3.90, 0.55, 1.35, 'E', 'S'),   # pasillo -> sala UPS
    ('E_in',    'h', 3.15, 2.75, 3.55, 'N', 'W'),   # pasillo -> esclusa
    ('E_out',   'v', 3.90, 3.40, 4.20, 'E', 'N'),   # esclusa -> sala de servidores
]

# Equipos en planta: (id, x0, y0, x1, y1, rótulo, familia, alto_3D)
EQUIP = [
    # Sala de servidores: fila de 1,8 m con frente al sur (pasillo frío)
    ('CL1', 4.90, 3.35, 5.20, 4.55, 'Clima 10 kW', 'clima', 2.00),
    ('R01', 5.20, 3.35, 5.80, 4.55, 'R01', 'rack', 2.00),
    ('R02', 5.80, 3.35, 6.40, 4.55, 'R02', 'rack', 2.00),
    ('CL2', 6.40, 3.35, 6.70, 4.55, 'Clima 10 kW', 'clima', 2.00),
    ('ASD', 3.90, 4.80, 4.05, 5.40, 'ASD', 'incendio', 1.60),
    # Sala de UPS: línea de 1,8 m contra el muro norte
    ('UPS', 4.80, 1.15, 5.40, 2.00, 'UPS', 'energia', 1.90),
    ('BAT1', 5.40, 1.15, 6.00, 2.00, 'Bat.', 'energia', 1.90),
    ('BAT2', 6.00, 1.15, 6.60, 2.00, 'Bat.', 'energia', 1.90),
    ('TAB', 7.35, 0.35, 7.50, 1.15, '', 'energia', 1.80),
    ('SPL', 6.80, 1.85, 7.40, 2.00, '', 'clima', 2.60),
    # Zona de trabajo y respaldo
    ('DESK', 0.00, 1.85, 1.20, 2.50, 'Puesto', 'mueble', 0.75),
    ('ARM', 0.00, 0.50, 0.50, 1.50, 'Custodia', 'mueble', 1.80),
    ('EST', 0.60, 0.00, 1.80, 0.40, 'Repuestos', 'mueble', 1.80),
    # Pasillo: mesón de enrolamiento
    ('ENR', 2.55, 0.95, 2.95, 1.55, 'EN', 'mueble', 1.00),
]
FM200 = (6.45, 5.30, 0.15)      # cilindro: centro x, y, radio

# Exterior (al norte de la fachada)
EXTERIOR = [
    ('GEN', 0.00, 6.15, 3.50, 8.15, 'Grupo electrógeno de 25 kVA<br>con estanque de 24 h<br>(losa de 3,50 × 2,00 m)', 'energia', 2.00),
    ('ATS', 3.85, 7.40, 4.85, 7.90, 'TA', 'energia', 1.60),
    ('CD3', 3.95, 6.25, 4.75, 6.60, 'CO', 'clima', 0.70),
    ('CD1', 5.20, 6.25, 6.20, 6.70, 'CO', 'clima', 1.00),
    ('CD2', 6.45, 6.25, 7.45, 6.70, 'CO', 'clima', 1.00),
]
DUCTS = [('Fibra', 5.45, 7.45), ('LTE', 7.25, 7.00)]   # entradas separadas por el muro norte


def area(k):
    x0, y0, x1, y1, _ = ROOMS[k]
    return (x1 - x0) * (y1 - y0)


if __name__ == '__main__':
    tot = 0
    for k in ROOMS:
        x0, y0, x1, y1, n = ROOMS[k]
        print(f'{n:40s} {x1-x0:.2f} x {y1-y0:.2f} = {area(k):.2f}')
        tot += area(k)
    print('total', round(tot, 2))
