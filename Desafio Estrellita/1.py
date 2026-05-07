jugadores = [
    {'nombre': 'Nico',   'puntaje': 4200},
    {'nombre': 'Valeria','puntaje': 8750},
    {'nombre': 'Diego',  'puntaje': 3100},
    {'nombre': 'Camila', 'puntaje': 8750},
    {'nombre': 'Matías', 'puntaje': 6300},
]

clasificacion = {"Bronce": 0, "Plata": 0, "Oro": 0}

for jugador in jugadores:
    if jugador.get("puntaje") < 5000:
        clasificacion.update({"Bronce": clasificacion.get("Bronce") + 1})
    elif jugador.get("puntaje") >= 5000 and jugador.get("puntaje") < 8000:
        clasificacion.update({"Plata": clasificacion.get("Plata") + 1})
    else:
        clasificacion.update({"Oro": clasificacion.get("Oro") + 1})

print(clasificacion)