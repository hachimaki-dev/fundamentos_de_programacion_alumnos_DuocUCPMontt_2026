jugadores = [{"nombre": "Juan", "pts": 430}, {"nombre": "Miguel", "pts": 390}]

max_puntos = 1
mejor_jugador = ""

for jugador in jugadores:
    if jugador["pts"] > max_puntos:
        max_puntos = jugador["pts"]
        mejor_jugador = jugador["nombre"]

print(f"El mejor jugador es: {mejor_jugador}")