jugadores = [
        { "Nombre": "Ash",  "Pts": 150 },
        { "Nombre": "Gary", "Pts": 200 },
        { "Nombre": "Oak",  "Pts": 180 }
]

mejor_jugador = ""
puntos_mejor_jugador = 0

for i in jugadores:
    if i["Pts"] > puntos_mejor_jugador:
        puntos_mejor_jugador = i["Pts"]
        mejor_jugador = i["Nombre"]
    else:
        continue

print(mejor_jugador, puntos_mejor_jugador)
