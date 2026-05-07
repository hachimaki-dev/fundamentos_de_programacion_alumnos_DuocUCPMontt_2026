user_puntos = 1500
rival_puntos = 1570
matchmaking = {"Partida Perfecta": 50, "Partida Justa": 100}
if abs(user_puntos - rival_puntos) <= matchmaking["Partida Perfecta"]:
    print("Partida Perfecta")
elif abs(user_puntos - rival_puntos) <= matchmaking["Partida Justa"]:
    print("Partida Justa")
else:
    print("Buscando otro rival...")