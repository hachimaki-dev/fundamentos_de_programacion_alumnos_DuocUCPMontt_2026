
mis_puntos = 1500
puntos_rival = 1570
diferencia_de_puntos = abs(mis_puntos - puntos_rival)
if diferencia_de_puntos <= 50:
    print("--partida perfecta--")
elif diferencia_de_puntos <=100:
    print("--partida justa--")
elif diferencia_de_puntos > 100:
    print("--buscando otro rival--")



