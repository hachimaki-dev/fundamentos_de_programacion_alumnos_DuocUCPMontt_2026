jugadores = [
    {'nombre': 'Ash', 'pts': 150},
    {'nombre': 'Gary', 'pts': 200}
]
mejor_jugador = "" 
max_puntos = -1
for jugador in jugadores:
    if jugador["pts"] > max_puntos:
        max_puntos = jugador['pts']
        mejor_jugador = jugador["nombre"]

print(mejor_jugador)