jugadores = [{"nombre": "Ash", "pts": 150}, {"nombre":"Gary", "pts": 200}]
mejor_jugador = jugadores[0]
for jugador in jugadores:
    if jugador["pts"] > mejor_jugador["pts"]:
        mejor_jugador = jugador
print(mejor_jugador["nombre"])