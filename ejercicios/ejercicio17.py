jugadores = [
    {'nombre': 'Ash', 'pts': 150},
    {'nombre': 'Gary', 'pts': 200}
]
for jugador in jugadores:
    if jugador["pts"] >= 200: ###harcodear codigo
        mejor_jugador = jugador["nombre"]
print(mejor_jugador)