mis_puntos = 1500
rival_puntos = 1570
diferencia_de_puntos = abs(rival_puntos - mis_puntos)
if diferencia_de_puntos <= 50:
    print("Partida Perfecta")
elif diferencia_de_puntos <=100:
    print("Partida Justa")
else:
    print("Buscando otro rival...")