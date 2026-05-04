# Define la lista:
# jugadores = [
#     {'nombre': 'Ash', 'pts': 150},
#     {'nombre': 'Gary', 'pts': 200}
# ]
# Encuentra el nombre del jugador con más puntos y guárdalo en una variable llamada mejor_jugador. Imprime esa variable.

jugadores = [{'nombre': 'Ash', 'pts': 150}, {'nombre': 'Gary', 'pts': 200}]
mejor_jugador = ""

mejor_actual = jugadores[0]

for jugador in jugadores:
    if jugador["pts"] > mejor_actual["pts"]:
        mejor_actual = jugador

mejor_jugador = mejor_actual["nombre"]
print(mejor_jugador)


    