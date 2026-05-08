partidos = [
    {'local': 'Colo-Colo', 'visita': 'La U',      'goles_local': 3, 'goles_visita': 1},
    {'local': 'La U',      'visita': 'Audax',      'goles_local': 0, 'goles_visita': 0},
    {'local': 'Audax',     'visita': 'Colo-Colo',  'goles_local': 1, 'goles_visita': 2},
    {'local': 'Colo-Colo', 'visita': 'Audax',      'goles_local': 1, 'goles_visita': 1},
    {'local': 'La U',      'visita': 'Colo-Colo',  'goles_local': 2, 'goles_visita': 2},
    {'local': 'Audax',     'visita': 'La U',        'goles_local': 0, 'goles_visita': 3},
]

puntos_x_victoria = 3
puntos_x_derrota = 0
puntos_x_empate = 1

liga = []

for partido in partidos:
    if {"equipo": partido.get("local"), "puntos": 0} not in liga:
        liga.append({"equipo": partido.get("local"), "puntos": 0})

for partido in partidos:
    if partido.get("goles_local") > partido.get("goles_visita"):
        for equipo in liga:
            if partido.get("local") == equipo.get("equipo"):
                equipo["puntos"] += puntos_x_victoria
    elif partido.get("goles_local") < partido.get("goles_visita"):
        for equipo in liga:
            if partido.get("visita") == equipo.get("equipo"):
                equipo["puntos"] += puntos_x_victoria
    else:
        for equipo in liga:
            if partido.get("local") == equipo.get("equipo"):
                equipo["puntos"] += puntos_x_empate
            elif partido.get("visita") == equipo.get("equipo"):
                equipo["puntos"] += puntos_x_empate

campeon = liga[0]

for i in range(len(liga)):
        swapped = False
        
        for j in range(0, len(liga) - i - 1):
            if liga[j].get("puntos") > liga[j + 1].get("puntos"):
                liga[j], liga[j + 1] = liga[j + 1], liga[j]
                swapped = True
        
        if not swapped:
            break

for i in range(len(liga)):
    print(f"{i + 1}. {liga[len(liga) - i - 1].get("equipo")}")

print(f"Campeón: {liga[-1].get("equipo")}")