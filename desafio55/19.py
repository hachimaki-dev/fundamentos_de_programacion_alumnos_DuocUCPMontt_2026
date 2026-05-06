puntos = 1500
rival = 1570

diferencia_puntos = abs(puntos - rival)

if diferencia_puntos <= 50:
    print("La partida es perfecta")

elif diferencia_puntos <= 100:
    print("La partida es justa")

else:
    print("Buscando otro rival...")